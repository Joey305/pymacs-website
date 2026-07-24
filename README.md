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
├── app.py
├── content.py
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
| `/basics` | Beginner introduction to molecular dynamics |
| `/force-fields` | Force field comparison and CHARMM/CGenFF explanation |
| `/getting-started` | First-run PyMACS guide |
| `/engine` | Command-level explanation of what PyMACS automates |
| `/workflow` | Script-by-script workflow overview |
| `/workflow/<slug>` | Detail page for each workflow stage |
| `/workflow/equilibration/energy-minimization` | EM teaching page |
| `/workflow/equilibration/nvt-equilibration` | NVT teaching page |
| `/workflow/equilibration/npt-equilibration` | NPT teaching page |
| `/analysis` | Analysis outputs and interpretation guide |
| `/examples` | Copyable example workflows |
| `/glossary` | Beginner-friendly MD vocabulary |
| `/resources` | GitHub, paper, and supporting resources |

## Editing Content

Most educational copy lives in `content.py`. The templates render that structured content into pages.

Use this pattern for updates:

1. Add or revise content in `content.py`.
2. Update the matching template only when the page structure needs to change.
3. Add CSS in `static/css/styles.css` only for reusable layout or component styles.
4. Run the validation checks below before pushing.

## Validation Before Pushing

Run a syntax check:

```bash
python -m py_compile app.py content.py
```

Render every public route with Flask's test client:

```bash
python - <<'PY'
from app import app

client = app.test_client()
routes = [
    "/",
    "/basics",
    "/force-fields",
    "/getting-started",
    "/engine",
    "/workflow",
    "/analysis",
    "/examples",
    "/glossary",
    "/resources",
    "/workflow/equilibration/energy-minimization",
    "/workflow/equilibration/nvt-equilibration",
    "/workflow/equilibration/npt-equilibration",
]

for route in routes:
    response = client.get(route)
    print(f"{route}: {response.status_code}")
    if response.status_code != 200:
        raise SystemExit(1)

with app.app_context():
    from content import SCRIPT_STEPS

for step in SCRIPT_STEPS:
    route = f"/workflow/{step['slug']}"
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

For production, run the app behind a WSGI server such as Gunicorn:

```bash
python -m pip install gunicorn
gunicorn "app:app"
```

Hosting options that can run Flask include Render, Fly.io, Railway, PythonAnywhere, a VM, or any server that supports WSGI Python apps.

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
