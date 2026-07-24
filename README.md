# PyMACS Website

Website repository for [pymacs.com](https://www.pymacs.com), the educational companion site for [PyMACS](https://github.com/schurerlab/Pymacs).

PyMACS is a Python-based automation suite for GROMACS molecular dynamics setup, simulation, analysis, visualization, and report generation. This website turns the detailed PyMACS README into a clickable learning hub for users who may be brand new to molecular dynamics, force fields, GROMACS, CHARMM, CGenFF, trajectory analysis, and command-line workflows.

## Live Website

| Page | What it teaches |
| --- | --- |
| [pymacs.com](https://www.pymacs.com/) | Main learning path, workflow overview, and representative outputs |
| [MD Basics](https://www.pymacs.com/basics.html) | Atoms, forces, time steps, temperature, pressure, trajectories, and scientific interpretation |
| [Force Fields](https://www.pymacs.com/force-fields.html) | CHARMM36, CHARMM36/LJ-PME, CGenFF, AMBER, OPLS, GROMOS, Martini, and why PyMACS centers CHARMM |
| [Run PyMACS](https://www.pymacs.com/getting-started.html) | First-run guide for preparing, simulating, analyzing, and reporting a PyMACS system |
| [Workflow](https://www.pymacs.com/workflow.html) | Script-by-script map of the PyMACS pipeline |
| [Engine](https://www.pymacs.com/engine.html) | The manual bash and analysis steps that PyMACS expedites |
| [Documentation Hub](https://www.pymacs.com/docs.html) | README-level technical documentation broken into clickable pages |
| [Analysis](https://www.pymacs.com/analysis.html) | RMSD, RMSF, radius of gyration, contact maps, heatmaps, NETWORX, and figurebooks |
| [Examples](https://www.pymacs.com/examples.html) | Copyable start-to-finish commands for curated example systems |
| [Glossary](https://www.pymacs.com/glossary.html) | Beginner-friendly molecular dynamics vocabulary |
| [Resources](https://www.pymacs.com/resources.html) | Paper, source code, GROMACS documentation, and project links |

## Detailed Documentation Pages

The website includes README-depth documentation as separate `.html` pages so users can click directly to the topic they need.

| Documentation page | Purpose |
| --- | --- |
| [Install PyMACS](https://www.pymacs.com/docs/install.html) | Quick Start installer, Git/Git LFS behavior, and next steps |
| [Repository Map](https://www.pymacs.com/docs/repository-map.html) | What each script, folder, force-field directory, and output directory is for |
| [Requirements And Environments](https://www.pymacs.com/docs/requirements-environments.html) | Python, Conda, GROMACS, setup environment, analysis environment, and fallback setup |
| [Inputs And Structures](https://www.pymacs.com/docs/inputs-structures.html) | PDB, CIF, mmCIF, PDB fetching, chain selection, and structure cleanup flags |
| [Force Fields](https://www.pymacs.com/docs/force-fields.html) | Why both CHARMM force-field folders are shipped and what force fields control |
| [Ligands And CGenFF](https://www.pymacs.com/docs/ligands-cgenff.html) | Ligand parameter files, CGenFF modes, conversion paths, and penalty-score cautions |
| [Run Templates](https://www.pymacs.com/docs/run-templates.html) | Local workstation, MPI/HPC, and analysis-only run-folder templates |
| [Pipeline Scripts](https://www.pymacs.com/docs/pipeline-scripts.html) | Step 1, Step 2, Step 3A, Step 3B/3C, PROTAC analysis, and Step 4 figurebooks |
| [CLI Flags](https://www.pymacs.com/docs/cli-flags.html) | Beginner-safe flags and categories for setup, simulation, hardware, restarts, and analysis |
| [Restarts](https://www.pymacs.com/docs/restarts.html) | Checkpoint-aware production MD continuation and clean restart behavior |
| [Analysis Outputs](https://www.pymacs.com/docs/analysis-outputs.html) | Stability plots, contact tables, interaction summaries, networks, and figurebooks |
| [Examples And Git LFS](https://www.pymacs.com/docs/examples-lfs.html) | Curated examples, large-file handling, and figurebook demo guidance |
| [Troubleshooting](https://www.pymacs.com/docs/troubleshooting.html) | Common folder, environment, GROMACS, ligand, topology, and analysis failures |
| [Best Practices](https://www.pymacs.com/docs/best-practices.html) | Provenance, scientific judgment, CGenFF review, and citation guidance |

## Workflow Pages

The workflow section explains every major PyMACS script as a page that can be shared directly.

| Workflow page | Script or stage |
| --- | --- |
| [System Preparation](https://www.pymacs.com/workflow/system-preparation.html) | `1_AutomateGromacs.py` |
| [Equilibration And Production MD](https://www.pymacs.com/workflow/simulation.html) | `2_AutomateGromacs.py` |
| [Energy Minimization](https://www.pymacs.com/workflow/equilibration/energy-minimization.html) | EM before dynamics |
| [NVT Equilibration](https://www.pymacs.com/workflow/equilibration/nvt-equilibration.html) | Temperature equilibration |
| [NPT Equilibration](https://www.pymacs.com/workflow/equilibration/npt-equilibration.html) | Pressure and density equilibration |
| [Trajectory Analysis](https://www.pymacs.com/workflow/trajectory-analysis.html) | `3A_AutomateGromacs.py` |
| [Network Rendering](https://www.pymacs.com/workflow/network-rendering.html) | `3B_NETWORX.py` |
| [PROTAC Analysis](https://www.pymacs.com/workflow/protac-analysis.html) | `3_PROTAC_Analysis.py` |
| [Figurebook Generation](https://www.pymacs.com/workflow/figurebook.html) | `4PDF4MD.py` |

## Curated Example Walkthroughs

The [Examples page](https://www.pymacs.com/examples.html) is built for users who need copyable commands and clear expected outputs.

| Example | System | What it demonstrates |
| --- | --- | --- |
| [Example 1](https://www.pymacs.com/examples.html#example-1) | `CPD32_9G94` with ligand `A1D` | Standard protein-ligand setup, MD, analysis, NETWORX, and figurebook workflow |
| [Example 2](https://www.pymacs.com/examples.html#example-2) | `9UWJ / AVPR1A` with `A1E` and `CLR` | Main ligand plus retained cofactor/context component |
| [Example 3](https://www.pymacs.com/examples.html#example-3) | `1URN` | RNA/protein biological assembly workflow |
| [Example 4](https://www.pymacs.com/examples.html#example-4) | `5T35` with `PTC` | PROTAC ternary-complex setup and component-aware analysis |

## What This Repository Contains

```text
pymacs-website/
├── .gitignore
├── .python-version
├── Procfile
├── README.md
├── app.py
├── content.py
├── docs_content.py
├── requirements.txt
├── static/
│   ├── css/styles.css
│   ├── img/pymacs-logo.png
│   ├── img/gallery/
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

## How The Site Is Organized

| File | Role |
| --- | --- |
| `app.py` | Flask routes, `.html` aliases, context variables, and page rendering |
| `content.py` | Main educational content, workflows, examples, glossary, resources, output gallery, and quick installer |
| `docs_content.py` | README-level documentation pages rendered under `/docs/*.html` |
| `templates/base.html` | Shared header, navigation, footer, favicon, fonts, theme toggle, and base layout |
| `templates/docs_index.html` | Documentation hub |
| `templates/docs_detail.html` | Reusable documentation detail page for docs content |
| `static/css/styles.css` | Site-wide visual system, responsive layout, docs tables, examples, command blocks, and dark mode |
| `static/js/theme.js` | Light/dark mode and mobile navigation behavior |
| `static/img/pymacs-logo.png` | Logo and favicon source |
| `static/img/gallery/` | Representative PyMACS analysis figures |
| `Procfile` | Heroku web process declaration |
| `.python-version` | Python major version for Heroku and compatible tooling |
| `requirements.txt` | Flask and Gunicorn dependencies |

## Run Locally

Clone or enter the website repository:

```bash
cd pymacs-website
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Start the Flask development server:

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

Useful local checks:

```bash
python -m py_compile app.py content.py docs_content.py
curl -I http://127.0.0.1:5000/docs.html
curl -I http://127.0.0.1:5000/examples.html
```

## Heroku Deployment

This repository includes the standard files Heroku needs for a Flask app:

```text
Procfile
.python-version
requirements.txt
```

`Procfile`:

```text
web: gunicorn app:app --bind 0.0.0.0:$PORT
```

`.python-version`:

```text
3.13
```

Deploy from the website repo root:

```bash
heroku login
heroku create pymacs
git push heroku main
heroku open
```

For an existing Heroku app:

```bash
heroku git:remote -a <your-heroku-app-name>
git push heroku main
```

Heroku detects the Python app from `requirements.txt`, installs Flask and Gunicorn, uses `.python-version` for the Python runtime, and starts the `web` process from `Procfile`.

## Content Editing Guide

Most changes do not require new routes.

| Goal | Edit |
| --- | --- |
| Add a new docs page | Add an entry to `DOC_PAGES` in `docs_content.py` |
| Change homepage learning path | Edit `LEARNING_PATH` in `content.py` |
| Change workflow pages | Edit `SCRIPT_STEPS` or `EQUILIBRATION_STAGES` in `content.py` |
| Change examples | Edit `EXAMPLE_SETS` in `content.py` |
| Change force-field education | Edit `FORCE_FIELDS` in `content.py` |
| Change analysis gallery | Edit `OUTPUT_GALLERY` in `content.py` and add image assets under `static/img/gallery/` |
| Change shared navigation or footer | Edit `templates/base.html` |
| Change visual design | Edit `static/css/styles.css` |

## Validation Before Pushing

Run syntax checks:

```bash
python -m py_compile app.py content.py docs_content.py
```

Render the main public pages:

```bash
python - <<'PY'
from app import app

routes = [
    "/",
    "/basics.html",
    "/force-fields.html",
    "/getting-started.html",
    "/engine.html",
    "/docs.html",
    "/analysis.html",
    "/examples.html",
    "/glossary.html",
    "/resources.html",
]

client = app.test_client()
for route in routes:
    response = client.get(route)
    print(route, response.status_code)
    if response.status_code != 200:
        raise SystemExit(1)
PY
```

Render every docs page:

```bash
python - <<'PY'
from app import app
from docs_content import DOC_PAGES

client = app.test_client()
for page in DOC_PAGES:
    route = f"/docs/{page['slug']}.html"
    response = client.get(route)
    print(route, response.status_code)
    if response.status_code != 200:
        raise SystemExit(1)
PY
```

Render every workflow page:

```bash
python - <<'PY'
from app import app
from content import EQUILIBRATION_STAGES, SCRIPT_STEPS

client = app.test_client()
for step in SCRIPT_STEPS:
    route = f"/workflow/{step['slug']}.html"
    response = client.get(route)
    print(route, response.status_code)
    if response.status_code != 200:
        raise SystemExit(1)

for stage in EQUILIBRATION_STAGES:
    route = f"/workflow/equilibration/{stage['slug']}.html"
    response = client.get(route)
    print(route, response.status_code)
    if response.status_code != 200:
        raise SystemExit(1)
PY
```

Scan for local development strings before publishing:

```bash
grep -RInE "/Users/|TemporaryItems|__pycache__|\\.pyc|TODO|FIXME|Lorem" . --exclude-dir=.git
```

Check what Git would add:

```bash
git add --dry-run .
```

Expected deploy files include `Procfile`, `.python-version`, `requirements.txt`, Flask source files, templates, CSS/JS, logo, and gallery images. They should not include `.venv/`, `__pycache__/`, `.pyc`, `.env`, logs, or screenshots.

## Design System

The site uses a restrained green/orange palette inspired by Miami colors without using university branding.

Key visual features:

- Sticky header with PyMACS logo
- Light/dark mode toggle
- Shared footer
- Copyable command cards
- Documentation cards and tables
- Workflow step cards
- Gallery cards for analysis plots
- Responsive layouts for mobile and desktop

## Public Project Links

- [Live website](https://www.pymacs.com)
- [PyMACS GitHub repository](https://github.com/schurerlab/Pymacs)
- [PyMACS paper](https://www.sciencedirect.com/science/article/pii/S0223523426004836)
- [GROMACS documentation](https://manual.gromacs.org/)

## Citation

Joseph M. Schulz, Robert C. Reynolds, Stephan C. Schurer. PyMACS: A python-based automation suite for GROMACS molecular dynamics setup, simulation, and analysis. European Journal of Medicinal Chemistry, Volume 316, Article 119038. DOI: 10.1016/j.ejmech.2026.119038.
