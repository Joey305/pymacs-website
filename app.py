from flask import Flask, abort, render_template

from docs_content import DOC_PAGE_MAP, DOC_PAGES

from content import (
    EQUILIBRATION_STAGES,
    ENGINE_STEPS,
    EXAMPLE_SETS,
    FORCE_FIELDS,
    GROMACS_INSTALLER,
    GETTING_STARTED,
    GLOSSARY,
    LEARNING_PATH,
    OUTPUT_GALLERY,
    QUICK_INSTALL,
    QUICK_FACTS,
    RESOURCES,
    SCRIPT_STEPS,
)


app = Flask(__name__)


@app.context_processor
def inject_site_context():
    return {
        "site_name": "PyMACS",
        "github_url": "https://github.com/schurerlab/Pymacs",
        "paper_url": "https://www.sciencedirect.com/science/article/pii/S0223523426004836",
        "gromacs_installer_url": GROMACS_INSTALLER["repo_url"],
        "gromacs_docs_url": "/docs/gromacs-installation.html",
        "nav_items": [
            {"label": "Home", "href": "/", "active": ["home"]},
            {"label": "MD Basics", "href": "/basics.html", "active": ["basics"]},
            {"label": "Force Fields", "href": "/force-fields.html", "active": ["force_fields"]},
            {"label": "Install & Run", "href": "/getting-started.html", "active": ["getting_started"]},
            {"label": "Workflow", "href": "/workflow.html", "active": ["workflow", "workflow_detail", "equilibration_detail"]},
            {"label": "Docs", "href": "/docs.html", "active": ["docs_index", "docs_detail"]},
            {"label": "Analysis", "href": "/analysis.html", "active": ["analysis"]},
            {"label": "Examples", "href": "/examples.html", "active": ["examples"]},
            {"label": "Resources", "href": "/resources.html", "active": ["resources", "glossary"]},
        ],
        "docs_pages": DOC_PAGES,
    }


@app.route("/")
def home():
    return render_template(
        "home.html",
        gromacs=GROMACS_INSTALLER,
        quick_facts=QUICK_FACTS,
        learning_path=LEARNING_PATH,
        script_steps=SCRIPT_STEPS,
        gallery=OUTPUT_GALLERY[:3],
    )


@app.route("/basics.html")
@app.route("/basics")
def basics():
    return render_template("basics.html")


@app.route("/force-fields.html")
@app.route("/force-fields")
def force_fields():
    return render_template("force_fields.html", force_fields=FORCE_FIELDS)


@app.route("/getting-started.html")
@app.route("/getting-started")
def getting_started():
    return render_template(
        "getting_started.html",
        guide=GETTING_STARTED,
        gromacs=GROMACS_INSTALLER,
        quick_install=QUICK_INSTALL,
    )


@app.route("/engine.html")
@app.route("/engine")
def engine():
    return render_template("engine.html", engine_steps=ENGINE_STEPS)


@app.route("/workflow.html")
@app.route("/workflow")
def workflow():
    return render_template("workflow.html", script_steps=SCRIPT_STEPS)


@app.route("/workflow/<slug>.html")
@app.route("/workflow/<slug>")
def workflow_detail(slug):
    step = next((item for item in SCRIPT_STEPS if item["slug"] == slug), None)
    if step is None:
        abort(404)
    return render_template(
        "workflow_detail.html",
        step=step,
        script_steps=SCRIPT_STEPS,
        equilibration_stages=EQUILIBRATION_STAGES,
    )


@app.route("/workflow/equilibration/<slug>.html")
@app.route("/workflow/equilibration/<slug>")
def equilibration_detail(slug):
    stage = next((item for item in EQUILIBRATION_STAGES if item["slug"] == slug), None)
    if stage is None:
        abort(404)
    return render_template(
        "equilibration_detail.html",
        stage=stage,
        stages=EQUILIBRATION_STAGES,
    )


@app.route("/docs.html")
def docs_index():
    return render_template("docs_index.html", docs_pages=DOC_PAGES)


@app.route("/docs/<slug>.html")
def docs_detail(slug):
    page = DOC_PAGE_MAP.get(slug)
    if page is None:
        abort(404)
    return render_template("docs_detail.html", page=page, docs_pages=DOC_PAGES)


@app.route("/analysis.html")
@app.route("/analysis")
def analysis():
    return render_template("analysis.html", gallery=OUTPUT_GALLERY)


@app.route("/examples.html")
@app.route("/examples")
def examples():
    return render_template("examples.html", examples=EXAMPLE_SETS, quick_install=QUICK_INSTALL)


@app.route("/glossary.html")
@app.route("/glossary")
def glossary():
    return render_template("glossary.html", glossary=GLOSSARY)


@app.route("/resources.html")
@app.route("/resources")
def resources():
    return render_template("resources.html", resources=RESOURCES)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
