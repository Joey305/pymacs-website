"""Anonymous, best-effort PyMACS website analytics with no content capture."""
from __future__ import annotations

import json, os, re, secrets, threading
from urllib.parse import urlparse
from urllib.request import Request, urlopen

from flask import Response, g, request

EVENTS = {
    "page_view": {""}, "docs_opened": {""}, "workflow_opened": {""}, "examples_opened": {""},
    "getting_started_opened": {""}, "triton_guide_opened": {""}, "leela_guide_opened": {""},
    "command_copied": {"quick_install", "full_bash_setup", "already_configured", "gromacs_install", "environment_setup", "triton_setup", "leela_setup", "workflow_example", "example_1", "example_2", "example_3", "example_4"},
    "github_opened": {""}, "paper_opened": {""}, "gromacs_installer_opened": {""},
    "citation_opened": {""}, "resource_opened": {""}, "cgenff_access_request_opened": {"triton", "leela"},
}


def enabled(): return os.environ.get("PYMACS_ANALYTICS_ENABLED", "").lower() in {"1", "true", "yes", "on"}


def _receiver():
    url, token = os.environ.get("PYMACS_ANALYTICS_RANDY_URL", "").strip().rstrip("/"), os.environ.get("PYMACS_ANALYTICS_RANDY_TOKEN", "").strip()
    return (url, token) if enabled() and url and token else None


def _id(name):
    cached = getattr(g, name, None)
    if cached: return cached
    value = request.cookies.get(name, "")
    value = value if len(value) >= 12 and value.replace("_", "").replace("-", "").isalnum() else secrets.token_urlsafe(18)
    setattr(g, name, value)
    return value


def _send(payload):
    receiver = _receiver()
    if not receiver: return
    try:
        url, token = receiver
        req = Request(url + "/event", data=json.dumps(payload).encode(), headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json", "User-Agent": "pymacs-analytics/1.0"}, method="POST")
        urlopen(req, timeout=2.0).close()
    except Exception: pass


def _campaign():
    value = request.args.get("utm_campaign", "").strip().lower()
    return value if re.fullmatch(r"youtube-[a-z0-9-]{1,60}", value) else ""

def track(event_type, feature="", status="", path=None, campaign=None):
    visitor, session = _id("pymacs_visitor"), _id("pymacs_session")
    if event_type not in EVENTS or feature not in EVENTS[event_type]: return visitor, session
    safe_path = path or request.path
    if not safe_path.startswith("/") or "?" in safe_path or len(safe_path) > 240: return visitor, session
    agent = request.user_agent.string.lower()
    device = "mobile" if any(x in agent for x in ("mobile", "android", "iphone")) else "tablet" if "ipad" in agent else "desktop"
    browser = "firefox" if "firefox" in agent else "safari" if "safari" in agent and "chrome" not in agent else "chrome" if "chrome" in agent else "other"
    referrer_host = urlparse(request.referrer or "").hostname or ""
    public_host = urlparse(os.environ.get("PYMACS_PUBLIC_BASE_URL", "")).hostname or ""
    referrer = "internal" if referrer_host and public_host and referrer_host == public_host else (referrer_host[:255] or "direct")
    payload = {"event_id": secrets.token_urlsafe(18), "event_type": event_type, "visitor_id": visitor, "session_id": session, "path": safe_path, "referrer": referrer, "device": device, "browser": browser, "feature": feature, "status": status, "campaign": campaign if campaign is not None else _campaign()}
    threading.Thread(target=_send, args=(payload,), daemon=True).start()
    return visitor, session


def attach(response: Response):
    if not enabled(): return response
    visitor, session = _id("pymacs_visitor"), _id("pymacs_session")
    if not request.cookies.get("pymacs_visitor"): response.set_cookie("pymacs_visitor", visitor, max_age=31536000, secure=True, httponly=True, samesite="Lax")
    if not request.cookies.get("pymacs_session"): response.set_cookie("pymacs_session", session, max_age=1800, secure=True, httponly=True, samesite="Lax")
    if request.method == "GET" and response.status_code < 400 and not request.path.startswith("/static/"):
        track("page_view")
        named = {"/docs.html": "docs_opened", "/workflow.html": "workflow_opened", "/examples.html": "examples_opened", "/getting-started.html": "getting_started_opened", "/triton": "triton_guide_opened", "/leela": "leela_guide_opened"}
        if request.path in named: track(named[request.path])
    return response


def browser_event(payload):
    if not isinstance(payload, dict): return False
    event_type, feature = payload.get("event_type"), payload.get("feature", "")
    if event_type not in EVENTS or feature not in EVENTS[event_type]: return False
    campaign = str(payload.get("campaign") or "")
    track(event_type, feature, campaign=campaign if re.fullmatch(r"youtube-[a-z0-9-]{1,60}", campaign) else "")
    return True
