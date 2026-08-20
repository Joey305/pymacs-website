from content import GROMACS_INSTALLER


DOC_PAGES = [
    {
        "slug": "gromacs-installation",
        "kicker": "GROMACS",
        "title": "Install GROMACS for PyMACS on Linux or WSL2",
        "meta_title": "Install GROMACS for PyMACS | PyMACS Documentation",
        "meta_description": "Install and verify GROMACS for PyMACS on supported Linux and WSL2 systems, configure NVIDIA CUDA support, and use one system GROMACS executable across PyMACS Conda environments.",
        "summary": "Install GROMACS for PyMACS on Linux or WSL2, verify the shared system executable, understand Conda-independent usage, and continue into the PyMACS workflow.",
        "sections": [
            {
                "heading": "Overview",
                "body": "PyMACS requires access to GROMACS for system setup, equilibration, production MD, trajectory processing, and related helper commands. The companion installer provides a reproducible Linux and WSL2 path that installs GROMACS at the system level instead of inside a Conda environment.",
                "badges": GROMACS_INSTALLER["badges"],
                "links": [
                    ("Companion installer repository", GROMACS_INSTALLER["repo_url"]),
                    ("Continue to PyMACS installation", "/docs/install.html"),
                ],
            },
            {
                "heading": "Who should use this installer?",
                "cards": [
                    {
                        "title": "Good fit",
                        "body": "Linux workstation users, WSL2 users, PyMACS users without a working GROMACS installation, and users who want one shared system gmx executable across base, cgenff, and mdanalysis.",
                    },
                    {
                        "title": "Use another path",
                        "body": "Managed HPC systems, administrator-provided module environments, and platforms not supported by the companion installer should generally keep using the local institutional GROMACS path instead of replacing it.",
                    },
                ],
            },
            {
                "heading": "Why install GROMACS system-wide?",
                "body": "Python dependencies and GROMACS solve different problems. PyMACS may use separate cgenff and mdanalysis environments for Python packages, but those environments should still call the same system executable at /usr/local/bin/gmx.",
                "architecture": {
                    "flow": GROMACS_INSTALLER["flow"],
                    "engine_label": GROMACS_INSTALLER["shared_engine"]["label"],
                    "consumers": GROMACS_INSTALLER["shared_engine"]["consumers"],
                    "message": GROMACS_INSTALLER["shared_engine"]["message"],
                },
                "bullets": [
                    "One GROMACS installation instead of duplicated environment-specific copies.",
                    "Consistent debugging because every environment resolves to the same executable.",
                    "Cleaner separation between Python package management and the MD engine.",
                    "Versioned installation paths and build records that support reproducibility.",
                ],
            },
            {
                "heading": "Quick installation",
                "body": "Run the companion installer from a normal Linux or WSL2 shell. The current repository installs GROMACS 2026.3 under /usr/local/gromacs-2026.3, creates a stable /usr/local/gromacs symlink, and exposes /usr/local/bin/gmx.",
                "code": GROMACS_INSTALLER["quick_command"],
                "links": [
                    ("Full installation guide", GROMACS_INSTALLER["repo_url"]),
                ],
            },
            {
                "heading": "Verify the installation",
                "body": "Refresh the current shell, then confirm that gmx runs and resolves to the intended system executable.",
                "code": GROMACS_INSTALLER["shell_refresh_command"],
                "bullets": [
                    "Expected executable path: /usr/local/bin/gmx",
                    "For a CUDA-enabled build, gmx --version should report GROMACS version 2026.3 and GPU support: CUDA when the installer detected a supported NVIDIA path.",
                ],
            },
            {
                "heading": "Verify across environments",
                "body": "The point of this workflow is that Conda environments manage Python packages while the system GROMACS executable remains shared.",
                "code": GROMACS_INSTALLER["environment_check_command"],
                "bullets": [
                    "base, mdanalysis, and cgenff should all resolve to /usr/local/bin/gmx in the shared workstation workflow.",
                    "If one environment resolves somewhere else, inspect the PATH and check for a second GROMACS installation inside that environment.",
                ],
            },
            {
                "heading": "NVIDIA GPU / CUDA and WSL2",
                "body": "The companion repository can detect NVIDIA GPU availability and build CUDA-enabled GROMACS when the machine and toolkit satisfy the documented requirements. On WSL2, Windows provides the NVIDIA driver layer and the Linux side should follow the repository's WSL-aware CUDA guidance.",
                "code": GROMACS_INSTALLER["gpu_check_command"],
                "bullets": [
                    "Check GPU visibility with nvidia-smi before troubleshooting CUDA-enabled builds.",
                    "The current installer repository documents CUDA >= 12.1 support and prefers cuda-toolkit-12-6 on supported Ubuntu and WSL2 paths.",
                    "Do not install a Linux NVIDIA display driver inside WSL2; follow the repository's toolkit guidance instead.",
                ],
                "links": [
                    ("Advanced installer options on GitHub", GROMACS_INSTALLER["repo_url"]),
                ],
            },
            {
                "heading": "Conda shadowing and gmx: command not found",
                "body": "A later Conda package can expose a different gmx than the intended system executable. When that happens, PyMACS may call the wrong binary or fail to find the system copy you expected.",
                "code": """type -a gmx

hash -r
source /etc/profile.d/gromacs.sh
which gmx
gmx --version""",
                "bullets": [
                    "The intended system executable for this workflow is /usr/local/bin/gmx.",
                    "If a Conda environment exposes its own $CONDA_PREFIX/bin/gmx, remove that separate Conda GROMACS package or call the system executable explicitly.",
                    "If gmx is still missing, rerun the latest companion installer and follow its troubleshooting guidance.",
                ],
            },
            {
                "heading": "Existing GROMACS installations and HPC users",
                "cards": [
                    {
                        "title": "Already have GROMACS?",
                        "body": "If gmx --version already works and the version and build are appropriate for your PyMACS workflow, you may not need to install another copy.",
                    },
                    {
                        "title": "Cluster or MPI environment",
                        "body": "Workstation defaults should not automatically replace cluster-specific installations. HPC users should normally use module systems, administrator-provided GROMACS builds, and cluster-specific MPI or GPU instructions, then point PyMACS at the proper executable.",
                    },
                ],
            },
            {
                "heading": "Continue to PyMACS",
                "cta": {
                    "title": "GROMACS working?",
                    "body": "Continue to the PyMACS installation guide, then create the cgenff and mdanalysis environments and run Example 1.",
                    "label": "Install PyMACS",
                    "href": "/docs/install.html",
                },
            },
        ],
    },
    {
        "slug": "install",
        "kicker": "Start here",
        "title": "Install PyMACS and create a clean working folder",
        "summary": "Use this page when you need PyMACS files in a fresh directory and want the safest path before running the examples.",
        "sections": [
            {
                "heading": "Before installing PyMACS",
                "body": "PyMACS requires access to a working GROMACS installation. For supported Linux and WSL2 workstations, start with the companion installer. If your institution already provides GROMACS on a cluster or managed workstation, verify that path first and continue when gmx is available.",
                "code": "gmx --version",
                "links": [
                    ("Install GROMACS", "/docs/gromacs-installation.html"),
                    ("Examples page", "/examples.html"),
                ],
            },
            {
                "heading": "What the installer does",
                "body": "The Quick Start installer temporarily clones the PyMACS repository, copies the files into the folder your terminal is currently pointing at, skips the cloned repository's .git folder, includes hidden project files, and removes the temporary clone when it is done.",
                "bullets": [
                    "Checks that git exists before copying anything.",
                    "Warns before copying into a non-empty directory.",
                    "Asks before overwriting files with the same names.",
                    "Uses Git LFS when available so large example assets are downloaded.",
                    "Warns when Git LFS is missing so users understand why large files may look incomplete.",
                ],
            },
            {
                "heading": "One-command install",
                "body": "Run this from the folder where you want the PyMACS files to appear.",
                "code": """bash <<'EOF'
set -e

REPO_URL="https://github.com/schurerlab/Pymacs.git"
TMP_DIR="$(mktemp -d)"
TARGET_DIR="$(pwd)"

cleanup() {
  rm -rf "$TMP_DIR"
}

trap cleanup EXIT

echo "PyMACS Quick Start Install"
echo "Target: $TARGET_DIR"

if ! command -v git >/dev/null 2>&1; then
  echo "ERROR: git is not installed or not available in PATH."
  exit 1
fi

if [ "$(find "$TARGET_DIR" -mindepth 1 -maxdepth 1 | wc -l)" -gt 0 ]; then
  echo "WARNING: This directory is not empty."
  printf "Continue copying PyMACS into this directory? [y/N]: "
  read -r answer </dev/tty
  case "$answer" in
    y|Y|yes|YES) ;;
    *) echo "Install cancelled."; exit 0 ;;
  esac
fi

git clone "$REPO_URL" "$TMP_DIR/pymacs"
cd "$TMP_DIR/pymacs"

if command -v git-lfs >/dev/null 2>&1 || git lfs version >/dev/null 2>&1; then
  git lfs install
  git lfs pull
else
  echo "WARNING: Git LFS was not detected."
fi

shopt -s dotglob nullglob
for item in "$TMP_DIR/pymacs"/*; do
  base="$(basename "$item")"
  [ "$base" = ".git" ] && continue

  if [ -e "$TARGET_DIR/$base" ]; then
    printf "Overwrite existing %s? [y/N]: " "$base"
    read -r overwrite </dev/tty
    case "$overwrite" in
      y|Y|yes|YES) rm -rf "$TARGET_DIR/$base" ;;
      *) echo "Skipping $base"; continue ;;
    esac
  fi

  cp -R "$item" "$TARGET_DIR/"
done

cleanup
trap - EXIT
cd "$TARGET_DIR"

echo "Done. Next:"
echo "conda env create -f environment_cgenff.yml"
echo "conda env create -f environment_mdanalysis.yml"
EOF""",
            },
            {
                "heading": "After installation",
                "bullets": [
                    "Create the cgenff environment for structure setup and ligand conversion.",
                    "Create the mdanalysis environment for simulation control, analysis, plots, and reports.",
                    "Confirm GROMACS is visible with gmx --version.",
                    "Start with the Example 1 workflow before attempting a new scientific system.",
                ],
                "links": [
                    ("Need GROMACS first?", "/docs/gromacs-installation.html"),
                    ("Requirements and environments", "/docs/requirements-environments.html"),
                ],
            },
        ],
    },
    {
        "slug": "repository-map",
        "kicker": "Orientation",
        "title": "Repository map and what each folder is for",
        "summary": "PyMACS includes scripts, templates, force fields, curated examples, documentation, and analysis assets. Knowing the folder layout prevents many beginner mistakes.",
        "sections": [
            {
                "heading": "Main project files",
                "table": [
                    ("Path", "Purpose"),
                    ("1_AutomateGromacs.py", "System setup, topology generation, box, solvation, ions, and EM input."),
                    ("2_AutomateGromacs.py", "Energy minimization, NVT, NPT, production MD, CPU/GPU controls, and restarts."),
                    ("3A_AutomateGromacs.py", "Trajectory processing, RMSD/RMSF/Rg, contacts, interaction summaries, and mode routing."),
                    ("3B_NETWORX.py", "Ligand-residue or peptide-contact network rendering."),
                    ("3C_Interface_RIN.py", "Protein-protein or protein-peptide interface residue interaction networks."),
                    ("3_PROTAC_Analysis.py", "Dedicated ternary-complex and PROTAC analysis."),
                    ("4PDF4MD.py", "Figurebook assembly from generated analysis plots."),
                ],
            },
            {
                "heading": "Folders users should recognize",
                "table": [
                    ("Folder", "What it contains"),
                    ("MDPs/", "GROMACS parameter templates for EM, NVT, NPT, and production MD."),
                    ("charmm36.ff/", "Standard CHARMM36-family force-field folder."),
                    ("charmm36_ljpme-jul2022.ff/", "CHARMM36-compatible LJ-PME force-field folder."),
                    ("Example_Choices/", "Curated example systems and reference outputs."),
                    ("docs/", "Supporting notes, output-gallery documentation, and citation guidance."),
                    ("Analysis_Results/", "Generated analysis outputs created after a run."),
                ],
            },
            {
                "heading": "Beginner rule",
                "body": "Do not edit force-field folders, MDP templates, generated topology files, or packaged example outputs until you understand why that edit is necessary. Copy examples into a fresh RUNS folder instead.",
            },
        ],
    },
    {
        "slug": "requirements-environments",
        "kicker": "Setup",
        "title": "System requirements and environments",
        "summary": "PyMACS expects a Python environment, GROMACS, and the correct setup and analysis dependencies. Most users should keep setup and analysis environments separate.",
        "sections": [
            {
                "heading": "Required tools",
                "bullets": [
                    "Python for running the PyMACS automation scripts.",
                    "GROMACS for topology processing, minimization, equilibration, production MD, and trajectory conversion.",
                    "Conda or another environment manager for repeatable dependencies.",
                    "Git and Git LFS when cloning the full repository and curated example assets.",
                ],
            },
            {
                "heading": "How the stack fits together",
                "body": "Conda environments manage Python dependencies. They do not need to own the system GROMACS installation. In the companion workstation workflow, all environments should still call /usr/local/bin/gmx.",
                "architecture": {
                    "flow": [
                        {"step": "System", "title": "GROMACS", "body": "/usr/local/bin/gmx"},
                        {"step": "Conda", "title": "cgenff", "body": "Preparation and parameterization dependencies"},
                        {"step": "Conda", "title": "mdanalysis", "body": "Trajectory analysis and plotting dependencies"},
                    ],
                    "engine_label": "/usr/local/bin/gmx",
                    "consumers": ["cgenff", "mdanalysis", "future environments"],
                    "message": "PyMACS uses the Conda environments for Python packages while keeping the simulation engine independent and shared.",
                },
            },
            {
                "heading": "Recommended Conda environments",
                "code": """conda env create -f environment_cgenff.yml
conda env create -f environment_mdanalysis.yml

conda activate cgenff
python 1_AutomateGromacs.py --help

conda activate mdanalysis
python 2_AutomateGromacs.py --help
python 3A_AutomateGromacs.py --help""",
            },
            {
                "heading": "Verify GROMACS visibility",
                "body": "Run these checks after environment creation and again if a later package install changes which gmx executable is active.",
                "code": """which gmx
gmx --version
type -a gmx""",
                "bullets": [
                    "gmx --version confirms that GROMACS is callable.",
                    "which gmx shows the active executable that your shell will use first.",
                    "type -a gmx shows every visible gmx on PATH and helps diagnose Conda shadowing.",
                ],
                "links": [
                    ("See GROMACS installation", "/docs/gromacs-installation.html"),
                ],
            },
            {
                "heading": "Non-Conda fallback",
                "body": "Advanced users can use a Python virtual environment, but they must still make GROMACS and any force-field or ligand-conversion tools visible on PATH.",
                "code": """python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
gmx --version""",
            },
            {
                "heading": "Pre-repairing structures",
                "body": "If PyMACS cannot repair a deposited structure cleanly, prepare the protein or biological assembly first with a dedicated structure-repair tool, then give the repaired file to Script 1.",
            },
        ],
    },
    {
        "slug": "inputs-structures",
        "kicker": "Structures",
        "title": "Supported inputs and structure preparation",
        "summary": "PyMACS can start from local structural files or fetch structures from the PDB. The important beginner skill is knowing what the selected input contains.",
        "sections": [
            {
                "heading": "Supported starts",
                "bullets": [
                    "Local PDB files.",
                    "Local CIF or mmCIF files.",
                    "Fetched PDB entries using a PDB ID.",
                    "Curated example inputs under Example_Choices/.",
                ],
            },
            {
                "heading": "Common commands",
                "code": """python 1_AutomateGromacs.py --pdb model.pdb
python 1_AutomateGromacs.py --pdb model.mmcif
python 1_AutomateGromacs.py --fetch-pdb 9UWJ
python 1_AutomateGromacs.py --fetch-pdb 9UWJ --fetch-format pdb""",
            },
            {
                "heading": "Chain and cleanup controls",
                "table": [
                    ("Flag", "Use"),
                    ("--keep-chains A,B", "Keep only selected polymer chains."),
                    ("--drop-chains B", "Remove selected polymer chains."),
                    ("--chain-names Rap1B,Rap1GAP", "Apply readable chain names in chain order."),
                    ("--chain-map A:Rap1B,B:Rap1GAP", "Apply explicit chain ID to name mapping."),
                    ("--remove-input-waters", "Remove crystallographic waters before setup."),
                    ("--remove-input-ions", "Remove ordinary ions before setup."),
                    ("--strict-pdb-validation", "Stop early when selected structure warnings should be treated as fatal."),
                ],
            },
            {
                "heading": "Beginner checks",
                "bullets": [
                    "Confirm the ligand or cofactor residue name in the input structure.",
                    "Do not drop chains unless you know those chains are irrelevant.",
                    "Use CIF or mmCIF when PDB formatting loses important structure details.",
                    "View the selected structure before trusting a long simulation.",
                ],
            },
        ],
    },
    {
        "slug": "force-fields",
        "kicker": "Physics",
        "title": "Force fields included in PyMACS",
        "summary": "The force field defines the classical physics model used by the simulation. PyMACS centers CHARMM-family workflows and ships both standard and LJ-PME-compatible CHARMM folders.",
        "sections": [
            {
                "heading": "Why both CHARMM folders are shipped",
                "bullets": [
                    "Some systems are best prepared with the standard CHARMM36-family folder.",
                    "Some runs need the CHARMM36/LJ-PME-compatible route.",
                    "PyMACS can automatically try both paths when setup requires fallback behavior.",
                    "Shipping both makes curated examples and user systems more portable.",
                ],
            },
            {
                "heading": "What the force field controls",
                "table": [
                    ("Term", "Meaning"),
                    ("Bonds, angles, dihedrals", "How bonded atoms resist stretching, bending, and rotation."),
                    ("Charges", "How atoms interact electrostatically."),
                    ("Lennard-Jones terms", "How atoms attract or repel at short and medium range."),
                    ("Topology files", "The atom, residue, molecule, and parameter definitions GROMACS needs."),
                ],
            },
            {
                "heading": "How to think about alternatives",
                "body": "AMBER, OPLS, GROMOS, and Martini are important MD ecosystems. PyMACS highlights them educationally, but the automated workflow is built around CHARMM-family topology handling and CGenFF-style small-molecule support.",
            },
        ],
    },
    {
        "slug": "ligands-cgenff",
        "kicker": "Ligands",
        "title": "Ligand parameterization and CGenFF support",
        "summary": "Small molecules need parameters that agree with the biomolecular force field. PyMACS supports practical CGenFF workflows while keeping ligand names and topology files aligned.",
        "sections": [
            {
                "heading": "Canonical ligand files",
                "table": [
                    ("File", "Purpose"),
                    ("<LIG>.str", "CGenFF stream file containing ligand parameters."),
                    ("<LIG>.cgenff.mol2", "CGenFF MOL2 file with atom names/types/charges."),
                    ("<lig>.itp", "Converted GROMACS include topology."),
                    ("<lig>.prm", "Converted ligand parameter file."),
                    ("posre_<lig>.itp", "Optional position-restraint include for the ligand."),
                ],
            },
            {
                "heading": "Three supported modes",
                "table": [
                    ("Mode", "When to use it"),
                    ("Pre-converted GROMACS ligand files", "You already have .itp/.prm/restraint files and want to import them."),
                    ("CGenFF server outputs only", "Recommended for many users: provide .str and .cgenff.mol2 and let PyMACS convert."),
                    ("Local SILCSBio/CGenFF automation", "Advanced local processing when the full local toolchain is available."),
                ],
            },
            {
                "heading": "Common setup command",
                "code": """cp Example_Choices/Example1/input/CPD32_9G94.pdb .
cp Example_Choices/Example1/parameters/A1D.str .
cp Example_Choices/Example1/parameters/A1D.cgenff.mol2 .
python 1_AutomateGromacs.py --pdb CPD32_9G94.pdb --ligand A1D""",
            },
            {
                "heading": "Scientific warning",
                "body": "CGenFF penalty scores should be reviewed before publication-grade conclusions. Automation reduces typing mistakes, but it does not replace chemical judgment.",
            },
        ],
    },
    {
        "slug": "run-templates",
        "kicker": "Recipes",
        "title": "Quick start templates for real run folders",
        "summary": "The README contains repeatable run-folder templates. The website version separates them into workstation, MPI/HPC, and analysis-only patterns.",
        "sections": [
            {
                "heading": "Template A: local workstation",
                "code": """mkdir -p RUNS/my_system
cd RUNS/my_system

cp ../../1_AutomateGromacs.py ../../2_AutomateGromacs.py ../../3A_AutomateGromacs.py ../../4PDF4MD.py .
cp -R ../../MDPs .
cp -R ../../charmm36.ff ../../charmm36_ljpme-jul2022.ff .
cp ../../my_input_structure.pdb .

conda activate cgenff
python 1_AutomateGromacs.py --pdb my_input_structure.pdb --ligand LIG

conda activate mdanalysis
python 2_AutomateGromacs.py --mode ligand --ligand LIG --ns 0.25 --compute auto
python 3A_AutomateGromacs.py --mode ligand --ligand LIG --headless
python 4PDF4MD.py""",
            },
            {
                "heading": "Template B: MPI or HPC folder",
                "code": """mkdir -p RUNS/my_hpc_system
cd RUNS/my_hpc_system

cp ../../1_AutomateGromacs_MPI.py ../../2_AutomateGromacs_MPI.py ../../3A_AutomateGromacs_MPI.py .
cp -R ../../MDPs ../../charmm36.ff ../../charmm36_ljpme-jul2022.ff .
cp ../../my_input_structure.pdb .

conda activate cgenff
python 1_AutomateGromacs_MPI.py --pdb my_input_structure.pdb --ligand LIG --gmx-bin gmx_mpi

conda activate mdanalysis
python 2_AutomateGromacs_MPI.py --mode ligand --ligand LIG --gmx-bin gmx_mpi --ns 0.25
python 3A_AutomateGromacs_MPI.py --mode ligand --ligand LIG --headless""",
            },
            {
                "heading": "Template C: analysis-only",
                "code": """conda activate mdanalysis
python 3A_AutomateGromacs.py --mode ligand --ligand LIG --headless
python 3B_NETWORX.py --ligand LIG
python 4PDF4MD.py""",
            },
        ],
    },
    {
        "slug": "pipeline-scripts",
        "kicker": "Pipeline",
        "title": "Pipeline stages and what each script does",
        "summary": "The PyMACS scripts are numbered because each one answers a different scientific and operational need.",
        "sections": [
            {
                "heading": "Step 1: setup",
                "body": "Script 1 cleans the input structure, detects chains and retained components, prepares CHARMM-compatible topologies, converts CGenFF ligand files when needed, defines the simulation box, solvates, adds ions, and creates the energy-minimization input.",
                "code": "python 1_AutomateGromacs.py --pdb complex.pdb --ligand LIG",
            },
            {
                "heading": "Step 2: EM, NVT, NPT, and production",
                "body": "Script 2 runs the physics stages in order: energy minimization, temperature equilibration, pressure/density equilibration, and production MD. It also handles CPU/GPU choices and checkpoint-safe continuation.",
                "code": "python 2_AutomateGromacs.py --mode ligand --ligand LIG --ns 1 --compute auto",
            },
            {
                "heading": "Step 3A: trajectory analysis",
                "body": "Script 3A turns raw trajectories into interpretable outputs: centered final trajectories, RMSD, RMSF, radius of gyration, secondary-structure summaries, ligand contacts, interaction-type tables, and mode-specific analyses.",
                "code": "python 3A_AutomateGromacs.py --mode ligand --ligand LIG --headless",
            },
            {
                "heading": "Step 3B and 3C: networks",
                "body": "Step 3B renders ligand-centered or peptide-contact networks. Step 3C handles protein-protein and protein-peptide interface residue interaction networks.",
                "code": """python 3B_NETWORX.py --ligand LIG
python 3C_Interface_RIN.py --contact-cutoff 4.0 --min-contact-frac 0.10""",
            },
            {
                "heading": "Step 4: figurebook",
                "body": "Step 4 packages generated figures into a PDF figurebook for review, sharing, and manuscript preparation.",
                "code": "python 4PDF4MD.py",
            },
        ],
    },
    {
        "slug": "cli-flags",
        "kicker": "Reference",
        "title": "Command-line flags and beginner-safe defaults",
        "summary": "PyMACS exposes many controls, but most first runs only need a small set of flags. This page groups the important ones by decision type.",
        "sections": [
            {
                "heading": "Most useful beginner flags",
                "table": [
                    ("Goal", "Command"),
                    ("Run a short test", "python 2_AutomateGromacs.py --ns 0.25"),
                    ("Use CPU only", "python 2_AutomateGromacs.py --compute CPU --ns 0.25"),
                    ("Use automatic GPU selection", "python 2_AutomateGromacs.py --compute auto --ns 0.25"),
                    ("Use a compact box", "python 1_AutomateGromacs.py --box-type dodecahedron"),
                    ("Increase box padding", "python 1_AutomateGromacs.py --box-distance 1.2"),
                    ("Resume an interrupted run", "python 2_AutomateGromacs.py --resume --production_only --ns 50"),
                    ("Make contact analysis stricter", "python 3A_AutomateGromacs.py --contact_cutoff 3.5"),
                    ("Make pocket analysis broader", "python 3A_AutomateGromacs.py --pocket-cutoff 6.0"),
                ],
            },
            {
                "heading": "Flag categories",
                "table": [
                    ("Category", "Examples"),
                    ("Structure input", "--pdb, --fetch-pdb, --fetch-format"),
                    ("Chain handling", "--keep-chains, --drop-chains, --chain-names, --chain-map"),
                    ("System identity", "--mode, --ligand, --cofactors"),
                    ("Box and solvent", "--box-type, --box-distance"),
                    ("MDP customization", "--mdp-dir, --em-mdp, --nvt-mdp, --npt-mdp, --md-mdp"),
                    ("Hardware", "--compute, --gpu-id, --ntomp, --ntmpi, --gmx-bin"),
                    ("Restarts", "--resume, --production_only, --force_restart"),
                    ("Analysis", "--contact_cutoff, --pocket-cutoff, --min_contact_frac"),
                    ("PROTAC", "--quick-test, --basic-only, --contacts-only, --distance-cutoff"),
                ],
            },
            {
                "heading": "Beginner safety rule",
                "body": "Change one thing at a time. If you change the input structure, force field, box size, hardware mode, run length, and analysis cutoffs all at once, debugging becomes much harder.",
            },
        ],
    },
    {
        "slug": "restarts",
        "kicker": "Recovery",
        "title": "Restarting and resuming production MD",
        "summary": "Long simulations can be interrupted. PyMACS supports checkpoint-aware restart behavior so users do not have to throw away completed work.",
        "sections": [
            {
                "heading": "Files to check before resuming",
                "bullets": [
                    "md_0_1.cpt or another valid checkpoint file.",
                    "md_0_1.tpr describing the current production run.",
                    "md_0_1.xtc or trajectory outputs already written.",
                    "md_0_1.log for the last completed status.",
                ],
            },
            {
                "heading": "Resume production only",
                "code": "python 2_AutomateGromacs.py --resume --production_only --ns 50",
            },
            {
                "heading": "CPU-only resume",
                "code": "python 2_AutomateGromacs.py --resume --production_only --compute CPU --ns 50",
            },
            {
                "heading": "Force a clean restart",
                "body": "Use this only when old checkpoint state is suspected to be wrong or incompatible.",
                "code": "python 2_AutomateGromacs.py --force_restart --ns 1",
            },
            {
                "heading": "Important note about --ns",
                "body": "For restarts, --ns should describe the intended production length for the continuing production path. Always confirm logs and output timing before interpreting a resumed run.",
            },
        ],
    },
    {
        "slug": "analysis-outputs",
        "kicker": "Interpretation",
        "title": "Analysis outputs and interaction definitions",
        "summary": "PyMACS translates raw trajectories into plots, CSV tables, networks, and figurebooks. The goal is not just to produce files, but to make the simulation interpretable.",
        "sections": [
            {
                "heading": "Core stability outputs",
                "table": [
                    ("Output", "What it helps answer"),
                    ("Protein_RMSD.png", "Did the protein drift or settle?"),
                    ("FullComplex_RMSD.png", "Did the whole simulated assembly remain coherent?"),
                    ("RMSF plots", "Which residues, chains, or ligand atoms were flexible?"),
                    ("Radius_of_Gyration_Overlay.png", "Did the system compact, expand, or breathe?"),
                    ("DSSP_Heatmap.png", "Did secondary structure persist or change?"),
                ],
            },
            {
                "heading": "Contact and interaction outputs",
                "table": [
                    ("Output", "Meaning"),
                    ("AllContacts_Framewise.csv", "Frame-by-frame contact table before filtering."),
                    ("FilteredContacts_Framewise.csv", "Contacts passing persistence or cutoff rules."),
                    ("InteractionTypes_Framewise.csv", "Interaction classifications over time."),
                    ("InteractionTypes_Summary.csv", "Residue-level interaction summary."),
                    ("interaction_heatmap_normalized.png", "Heatmap of persistent residue/interaction behavior."),
                    ("binding_importance_ranking.png", "Ranked residues for interpretation."),
                ],
            },
            {
                "heading": "Interaction definitions",
                "body": "Contact analysis is based on geometric cutoffs and residue chemistry. It is evidence of proximity, persistence, and interaction type; it is not a direct binding free energy calculation.",
            },
            {
                "heading": "Figurebooks",
                "body": "The figurebook scripts collect useful plots into MD_ANALYSIS_FIGUREBOOK.pdf or PROTAC_MD_ANALYSIS_FIGUREBOOK.pdf so users can review results without hunting through the output tree.",
            },
        ],
    },
    {
        "slug": "examples-lfs",
        "kicker": "Examples",
        "title": "Curated examples and Git LFS",
        "summary": "The repository includes examples for protein-ligand, cofactor-aware, biological assembly, and PROTAC workflows. Large example assets may require Git LFS.",
        "sections": [
            {
                "heading": "Curated examples",
                "table": [
                    ("Example", "System and lesson"),
                    ("Example 1", "CPD32_9G94 with A1D; standard protein-ligand setup through analysis and figurebook."),
                    ("Example 2", "9UWJ / AVPR1A with A1E and CLR; retained cofactor/context workflow."),
                    ("Example 3", "1URN; RNA/protein biological assembly workflow."),
                    ("Example 4", "5T35 with PTC; PROTAC ternary-complex workflow."),
                ],
            },
            {
                "heading": "Git LFS check",
                "code": """git lfs version
git lfs install
git lfs pull""",
            },
            {
                "heading": "Reproduce the figurebook demo",
                "body": "Start with Example 1, use a short production run, run 3A analysis, run NETWORX when contact tables exist, and finish with 4PDF4MD.py. Then compare your outputs with the packaged completed_run folder.",
            },
            {
                "heading": "Website walkthrough",
                "body": "The examples page provides copyable commands for each curated example.",
                "links": [("Open examples", "/examples.html")],
            },
        ],
    },
    {
        "slug": "troubleshooting",
        "kicker": "Debugging",
        "title": "Troubleshooting common PyMACS problems",
        "summary": "Most first failures are caused by environment, folder, input-file, ligand-name, or topology mismatches. Check the simple things before changing scientific settings.",
        "sections": [
            {
                "heading": "First commands to run",
                "code": """pwd
ls
python --version
gmx --version
find . -maxdepth 2 -type f | sort | head -80""",
            },
            {
                "heading": "Common problems",
                "table": [
                    ("Symptom", "Likely cause"),
                    ("python: command not found", "Python is not available in the active shell."),
                    ("conda: command not found", "Conda is not installed or not initialized."),
                    ("gmx: command not found", "GROMACS is not installed, loaded, or visible on PATH."),
                    ("Script cannot find the input file", "You are in the wrong folder or did not copy the input file."),
                    ("Ligand parameters missing", "The .str or .cgenff.mol2 file is absent or named differently from the ligand code."),
                    ("grompp fails", "Topology mismatch, atom-name mismatch, missing parameter, or incompatible MDP/index selection."),
                    ("No plots appear", "Analysis did not finish or Analysis_Results was written somewhere else."),
                ],
            },
            {
                "heading": "What to save when asking for help",
                "bullets": [
                    "The exact command you ran.",
                    "The last 20-30 terminal lines before the error.",
                    "The current folder from pwd.",
                    "A file listing from ls.",
                    "Relevant log files such as mdrun.log or grompp output.",
                ],
            },
        ],
    },
    {
        "slug": "best-practices",
        "kicker": "Judgment",
        "title": "Best practices, provenance, and citation",
        "summary": "PyMACS automates the workflow, but users still need scientific judgment. This page collects the practices that make runs easier to trust and easier to explain.",
        "sections": [
            {
                "heading": "Best practices",
                "bullets": [
                    "Use a fresh run folder for every system or replicate.",
                    "Start with a short test run before committing to long production MD.",
                    "Keep raw inputs, parameter files, logs, and generated outputs together.",
                    "Record the ligand code, cofactor codes, force-field path, box type, and run length.",
                    "Review CGenFF penalty scores before treating ligand simulations as publication-grade.",
                    "Inspect RMSD and radius of gyration before interpreting contacts.",
                    "Treat contact maps as persistence evidence, not binding free energy.",
                ],
            },
            {
                "heading": "Provenance note",
                "body": "A reproducible MD workflow should preserve the input structure, topology decisions, MDP settings, software environments, generated logs, and analysis outputs. PyMACS helps by keeping the numbered stages explicit.",
            },
            {
                "heading": "Citation",
                "body": "Joseph M. Schulz, Robert C. Reynolds, Stephan C. Schurer. PyMACS: A python-based automation suite for GROMACS molecular dynamics setup, simulation, and analysis. European Journal of Medicinal Chemistry, Volume 316, Article 119038. DOI: 10.1016/j.ejmech.2026.119038.",
            },
            {
                "heading": "Project links",
                "links": [
                    ("PyMACS GitHub", "https://github.com/schurerlab/Pymacs"),
                    ("PyMACS paper", "https://www.sciencedirect.com/science/article/pii/S0223523426004836"),
                ],
            },
        ],
    },
]


DOC_PAGE_MAP = {page["slug"]: page for page in DOC_PAGES}
