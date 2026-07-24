# PyMACS Website

Educational Flask website for PyMACS, the molecular dynamics automation workflow built around GROMACS, CHARMM-family force fields, CGenFF ligand parameterization, trajectory analysis, network visualization, and figurebook reporting.

The site is designed for users who are new to molecular dynamics. A visitor should be able to learn the core MD vocabulary, understand what each PyMACS script does, copy example commands, and recognize the main outputs produced by the workflow.

## What The Site Covers

- Molecular dynamics basics: atoms, force fields, time steps, temperature, pressure, trajectories, and checkpoints.
- Force field education: CHARMM36, CHARMM36/LJ-PME, CGenFF, and common alternatives such as AMBER, OPLS, GROMOS, and Martini.
- PyMACS workflow pages: setup, parameterization, solvation, ions, EM, NVT, NPT, production MD, analysis, NETWORX, PROTAC analysis, and figurebook generation.
- Example walkthroughs: copyable start-to-finish commands for protein-ligand, cofactor-aware, RNA/protein, and PROTAC systems.
- Analysis interpretation: RMSD, RMSF, radius of gyration, contact frequency, interaction heatmaps, network panels, and PDF reports.

## Project Structure

```text
website/
├── .python-version
├── Procfile
├── app.py
├── content.py
├── docs_content.py
├── requirements.txt
├── static/
│   ├── css/styles.css
│   ├── img/
│   └── js/theme.js
└── templates/
    ├── base.html
    ├── home.html
    ├── basics.html
    ├── force_fields.html
    ├── getting_started.html
    ├── workflow.html
    ├── workflow_detail.html
    ├── equilibration_detail.html
    ├── engine.html
    ├── docs_index.html
    ├── docs_detail.html
    ├── analysis.html
    ├── examples.html
    ├── glossary.html
    └── resources.html
```

## Run Locally

Create a clean Python environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Start the Flask app:

```bash
python app.py
```

Open the site:

```text
http://127.0.0.1:5000
```

## Main Routes

| Route | Purpose |
| --- | --- |
| `/` | Home page, quick facts, learning path, workflow preview, and output gallery |
| `/basics.html` | Beginner introduction to molecular dynamics |
| `/force-fields.html` | Force field comparison and CHARMM/CGenFF explanation |
| `/getting-started.html` | First-run PyMACS guide |
| `/engine.html` | Command-level explanation of what PyMACS automates |
| `/docs.html` | Documentation hub rebuilt from the detailed PyMACS README |
| `/docs/<slug>.html` | Detailed documentation pages for install, environments, flags, examples, troubleshooting, and more |
| `/workflow.html` | Script-by-script workflow overview |
| `/workflow/<slug>.html` | Detail page for each workflow stage |
| `/workflow/equilibration/energy-minimization.html` | EM teaching page |
| `/workflow/equilibration/nvt-equilibration.html` | NVT teaching page |
| `/workflow/equilibration/npt-equilibration.html` | NPT teaching page |
| `/analysis.html` | Analysis outputs and interpretation guide |
| `/examples.html` | Copyable example workflows |
| `/glossary.html` | Beginner-friendly MD vocabulary |
| `/resources.html` | Paper, GitHub, and supporting resources |

## Editing Content

Most educational copy lives in `content.py` and `docs_content.py`. The templates render that structured content into pages.

Use this pattern for updates:

1. Add or revise content in `content.py` or `docs_content.py`.
2. Update the matching template only when the page structure needs to change.
3. Add CSS in `static/css/styles.css` only for reusable layout or component styles.
4. Run the validation checks below before pushing.

## Validation Before Pushing

Run a syntax check:

```bash
python -m py_compile app.py content.py docs_content.py
```

Render every public route with Flask's test client:

```bash
python - <<'PY'
from app import app

client = app.test_client()
routes = [
    "/",
    "/basics.html",
    "/force-fields.html",
    "/getting-started.html",
    "/engine.html",
    "/docs.html",
    "/docs/install.html",
    "/docs/repository-map.html",
    "/docs/requirements-environments.html",
    "/docs/inputs-structures.html",
    "/docs/force-fields.html",
    "/docs/ligands-cgenff.html",
    "/docs/run-templates.html",
    "/docs/pipeline-scripts.html",
    "/docs/cli-flags.html",
    "/docs/restarts.html",
    "/docs/analysis-outputs.html",
    "/docs/examples-lfs.html",
    "/docs/troubleshooting.html",
    "/docs/best-practices.html",
    "/workflow.html",
    "/analysis.html",
    "/examples.html",
    "/glossary.html",
    "/resources.html",
    "/workflow/equilibration/energy-minimization.html",
    "/workflow/equilibration/nvt-equilibration.html",
    "/workflow/equilibration/npt-equilibration.html",
]

for route in routes:
    response = client.get(route)
    print(f"{route}: {response.status_code}")
    if response.status_code != 200:
        raise SystemExit(1)

with app.app_context():
    from content import SCRIPT_STEPS

for step in SCRIPT_STEPS:
    route = f"/workflow/{step['slug']}.html"
    response = client.get(route)
    print(f"{route}: {response.status_code}")
    if response.status_code != 200:
        raise SystemExit(1)
PY
```

Scan for local paths or development-only strings:

```bash
grep -RInE "/Users/|jxs794|TemporaryItems|__pycache__|\\.pyc|TODO|FIXME|Lorem" .
```

## Assets

The site uses the PyMACS logo as its brand image and favicon:

```text
static/img/pymacs-logo.png
```

Analysis gallery images live under:

```text
static/img/gallery/
```

If a template references a new image, put that image in `static/img/` and verify the route renders before pushing.

## Deployment Notes

This repository is a Flask application. It is not a static-only site unless you add a static export workflow later.

## Heroku Deployment

The app includes the files Heroku needs in the website repo root:

```text
Procfile
.python-version
requirements.txt
```

The `Procfile` starts the Flask app with Gunicorn:

```text
web: gunicorn app:app --bind 0.0.0.0:$PORT
```

Deploy from this directory:

```bash
heroku login
heroku create pymacs
git push heroku main
heroku open
```

If the Heroku app already exists:

```bash
heroku git:remote -a <your-heroku-app-name>
git push heroku main
```

Heroku detects this as a Python app from `requirements.txt`, uses `.python-version` for the Python major version, installs Flask and Gunicorn, and starts the `web` process from `Procfile`.

Other hosting options that can run Flask include Render, Fly.io, Railway, PythonAnywhere, a VM, or any server that supports WSGI Python apps.

## Do Not Commit

Keep generated and local-only files out of the website repository:

- `.venv/`
- `__pycache__/`
- `*.pyc`
- `.env`
- local logs
- editor files
- operating-system metadata such as `.DS_Store`

The included `.gitignore` covers these common cases.

## Project Links

- PyMACS source code: <https://github.com/schurerlab/Pymacs>
- PyMACS paper: <https://www.sciencedirect.com/science/article/pii/S0223523426004836>
