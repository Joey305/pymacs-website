QUICK_FACTS = [
    {
        "label": "Core engine",
        "value": "GROMACS",
        "detail": "PyMACS automates the commands that prepare, simulate, and process GROMACS systems.",
        "link_label": "Need GROMACS? Install it",
        "href": "/docs/gromacs-installation.html",
    },
    {
        "label": "Primary force field",
        "value": "CHARMM36 / LJ-PME",
        "detail": "The workflow ships CHARMM36-family files and highlights the LJ-PME variant for compatible runs.",
    },
    {
        "label": "Small molecules",
        "value": "CGenFF",
        "detail": "Ligands and cofactors can use CGenFF-style MOL2 and STR files converted into GROMACS topology files.",
    },
    {
        "label": "Main outputs",
        "value": "Trajectories, CSVs, figures, PDFs",
        "detail": "PyMACS turns raw MD files into stability plots, contact maps, networks, and figurebooks.",
    },
]


GROMACS_INSTALLER = {
    "repo_url": "https://github.com/Joey305/gromacs-installation",
    "doc_url": "/docs/gromacs-installation.html",
    "badges": [
        "Linux",
        "WSL2",
        "GROMACS 2026.3",
        "NVIDIA CUDA",
        "Conda-independent",
    ],
    "quick_command": """git clone https://github.com/Joey305/gromacs-installation.git
cd gromacs-installation
chmod +x install_gromacs.sh
./install_gromacs.sh
hash -r
source /etc/profile.d/gromacs.sh
gmx --version""",
    "verify_command": "gmx --version",
    "shell_refresh_command": """hash -r
source /etc/profile.d/gromacs.sh
gmx --version
which gmx""",
    "environment_check_command": """conda activate base
which gmx
gmx --version

conda activate mdanalysis
which gmx
gmx --version

conda activate cgenff
which gmx
gmx --version""",
    "shadow_check_command": """type -a gmx
/usr/local/bin/gmx --version""",
    "gpu_check_command": """nvidia-smi
gmx --version""",
    "flow": [
        {"step": "1", "title": "GROMACS", "body": "System simulation engine"},
        {"step": "2", "title": "PyMACS", "body": "Automation scripts and workflow"},
        {"step": "3", "title": "Python environments", "body": "cgenff and mdanalysis"},
        {"step": "4", "title": "First simulation", "body": "Run Example 1"},
    ],
    "shared_engine": {
        "label": "/usr/local/bin/gmx",
        "consumers": [
            "base",
            "cgenff",
            "mdanalysis",
            "future environments",
            "ordinary shell",
        ],
        "message": "Conda manages the Python environments. GROMACS remains a shared system-level simulation engine.",
    },
    "paths": [
        {
            "title": "Local Linux / WSL2 workstation",
            "body": "Use the PyMACS companion installer when you want a reproducible system-wide GROMACS build that stays visible from your normal shell and Conda environments.",
        },
        {
            "title": "University cluster / HPC / SLURM environment",
            "body": "Use the GROMACS module or administrator-managed installation provided by the institution whenever appropriate. PyMACS can work with alternate GROMACS executables supported by the project.",
        },
    ],
}


LEARNING_PATH = [
    {
        "title": "Learn what MD is",
        "body": "Start with atoms, forces, time steps, temperature, pressure, and why a trajectory is more informative than one static structure.",
        "href": "/basics.html",
    },
    {
        "title": "Understand force fields",
        "body": "Compare CHARMM, AMBER, OPLS, GROMOS, Martini, and the role of CGenFF for drug-like molecules.",
        "href": "/force-fields.html",
    },
    {
        "title": "Follow the PyMACS scripts",
        "body": "Walk through setup, parameterization, equilibration, production MD, trajectory analysis, networks, and report generation.",
        "href": "/workflow.html",
    },
    {
        "title": "Run the first example",
        "body": "Use the curated Example 1 path to see exactly what files are copied, which environments are activated, and which commands are run.",
        "href": "/getting-started.html",
    },
    {
        "title": "Interpret the outputs",
        "body": "Learn what RMSD, RMSF, radius of gyration, contact maps, interaction types, and figurebooks mean in practice.",
        "href": "/analysis.html",
    },
]


GETTING_STARTED = {
    "intro": "The recommended first experience is the curated protein-ligand walkthrough. It shows the full rhythm of PyMACS without asking a new user to design a new simulation from scratch.",
    "prerequisites": [
        "A working GROMACS executable. Local Linux and WSL2 users can use the companion installer; HPC users should use the module or managed build provided by their institution.",
        "The PyMACS repository files, including MDP templates and force-field folders",
        "The cgenff environment for setup and ligand conversion",
        "The mdanalysis environment for simulation control, analysis, plotting, and reports",
        "Ligand CGenFF files when running ligand or cofactor systems",
    ],
    "environment_summary": "After GROMACS is available, install PyMACS, create the two recommended Conda environments, and confirm that both environments still resolve to the same shared system gmx executable.",
    "run_steps": [
        {
            "title": "Create a clean run folder",
            "body": "Keep each system in its own directory so generated topologies, trajectories, CSV tables, plots, and logs stay reproducible.",
            "command": "mkdir -p RUNS/Example_CPD32 && cd RUNS/Example_CPD32",
        },
        {
            "title": "Prepare the system",
            "body": "Run Step 1 in the cgenff environment. This cleans the structure, builds topologies, places solvent and ions, and writes the energy-minimization input.",
            "command": "conda activate cgenff\npython 1_AutomateGromacs.py --pdb CPD32_9G94.pdb",
        },
        {
            "title": "Run equilibration and production",
            "body": "Run Step 2 in the analysis/simulation environment. This executes minimization, NVT, NPT, and production MD.",
            "command": "conda activate mdanalysis\npython 2_AutomateGromacs.py",
        },
        {
            "title": "Analyze the trajectory",
            "body": "Step 3A recenters the trajectory, calculates stability and flexibility metrics, extracts binding-pocket contacts, and prepares network-ready tables.",
            "command": "python 3A_AutomateGromacs.py",
        },
        {
            "title": "Render networks and reports",
            "body": "Step 3B creates ligand-residue network views when the required contact tables exist. Step 4 assembles the final figurebook.",
            "command": "python 3B_NETWORX.py\npython 4PDF4MD.py",
        },
    ],
    "checks": [
        "Read mdrun.log after every stage; it records commands and setup decisions.",
        "Inspect em.gro, nvt.gro, and npt.gro before trusting production output.",
        "Check RMSD and Rg before interpreting contacts.",
        "Treat contact maps as evidence of proximity and persistence, not direct binding free energy.",
        "Review CGenFF penalty scores for ligands before publication-grade conclusions.",
    ],
}


QUICK_INSTALL = {
    "title": "Quick Start Install",
    "summary": "Use this when you want to create a clean PyMACS run or working folder without manually downloading the repository or copying files yourself.",
    "plain": "First, cd into the folder where you want the PyMACS files to appear. Your current working directory simply means the folder your terminal is presently pointing at. The command below temporarily clones PyMACS, copies everything into that folder, includes hidden files such as .gitignore and .gitattributes, skips the cloned repository's .git folder, and then removes the temporary clone when it is finished.",
    "guards": [
        "Checks that git is installed before doing anything.",
        "Warns before copying into a non-empty directory.",
        "Asks before overwriting similarly named files.",
        "Uses Git LFS when available and warns if large example assets may still be pointer files.",
    ],
    "command": """bash <<'EOF'
set -e

REPO_URL="https://github.com/schurerlab/Pymacs.git"
TMP_DIR="$(mktemp -d)"
TARGET_DIR="$(pwd)"

cleanup() {
  rm -rf "$TMP_DIR"
}

trap cleanup EXIT

echo "======================================"
echo " PyMACS Quick Start Install"
echo "======================================"
echo
echo "This will copy a fresh PyMACS instance into:"
echo "  $TARGET_DIR"
echo

if ! command -v git >/dev/null 2>&1; then
  echo "ERROR: git is not installed or not available in PATH."
  echo "Please install git first, then run this command again."
  exit 1
fi

if [ "$(find "$TARGET_DIR" -mindepth 1 -maxdepth 1 | wc -l)" -gt 0 ]; then
  echo "WARNING: This directory is not empty."
  echo "Files with the same names as PyMACS files may be overwritten."
  echo
  printf "Continue copying PyMACS into this directory? [y/N]: "
  read -r answer </dev/tty
  case "$answer" in
    y|Y|yes|YES) ;;
    *)
      echo "Install cancelled."
      exit 0
      ;;
  esac
fi

echo
echo "Cloning PyMACS into a temporary folder..."
git clone "$REPO_URL" "$TMP_DIR/pymacs"

cd "$TMP_DIR/pymacs"

if command -v git-lfs >/dev/null 2>&1 || git lfs version >/dev/null 2>&1; then
  echo "Git LFS detected. Pulling large tracked files..."
  git lfs install
  git lfs pull
else
  echo "WARNING: Git LFS was not detected."
  echo "Core PyMACS files will still be copied, but large example assets may remain as LFS pointer files."
  echo "Install Git LFS later and re-run this installer if you need the full example datasets."
fi

echo
echo "Copying PyMACS files into your current directory..."

shopt -s dotglob nullglob
for item in "$TMP_DIR/pymacs"/*; do
  base="$(basename "$item")"
  if [ "$base" = ".git" ]; then
    continue
  fi

  if [ -e "$TARGET_DIR/$base" ]; then
    printf "Overwrite existing %s? [y/N]: " "$base"
    read -r overwrite </dev/tty
    case "$overwrite" in
      y|Y|yes|YES)
        rm -rf "$TARGET_DIR/$base"
        ;;
      *)
        echo "Skipping $base"
        continue
        ;;
    esac
  fi

  cp -R "$item" "$TARGET_DIR/"
done

echo "Cleaning up temporary clone..."
cleanup
trap - EXIT

cd "$TARGET_DIR"

echo
echo "Done. PyMACS has been copied into:"
echo "  $TARGET_DIR"
echo
echo "Next recommended steps:"
echo "  conda env create -f environment_cgenff.yml"
echo "  conda env create -f environment_mdanalysis.yml"
echo
echo "Then follow the Step 1 / Step 2 / Step 3 workflow on this page."
EOF""",
}


EQUILIBRATION_STAGES = [
    {
        "slug": "energy-minimization",
        "short": "EM",
        "title": "Energy Minimization",
        "stage": "Before dynamics",
        "mdp": "em.mdp",
        "input": "solv_ions.gro from Step 1",
        "output": "em.gro, em.edr, em.log",
        "summary": "Energy minimization relaxes severe steric clashes and unfavorable contacts before atoms are allowed to move with real velocities.",
        "plain": "Imagine the prepared structure has a few atoms placed too close together during model building, protonation, solvation, or ion placement. If production dynamics started immediately, those overlaps could create huge forces and crash the simulation. EM gently finds a nearby lower-energy geometry first.",
        "what_happens": [
            "GROMACS reads the prepared solvated and ionized system plus the topology.",
            "The minimizer calculates forces from the force field rather than assigning thermal velocities.",
            "Coordinates are adjusted downhill on the potential-energy surface, usually with steepest descent.",
            "The process stops when the maximum force is low enough or the configured step limit is reached.",
        ],
        "pipeline_role": [
            "Confirms the topology, coordinates, and MDP file can be compiled together.",
            "Removes dangerous local clashes introduced during setup.",
            "Produces a cleaner coordinate file for temperature equilibration.",
        ],
        "watch": [
            "EM is not sampling. It does not tell you whether the system is stable over time.",
            "A failed EM often points to topology mismatches, missing parameters, atom naming problems, bad ligand placement, or severe clashes.",
            "A successful EM is necessary but not sufficient; you still need NVT, NPT, and production checks.",
        ],
        "beginner_checks": [
            "Did `grompp` succeed without fatal topology errors?",
            "Did `mdrun` finish and write `em.gro`?",
            "Are the final forces reasonable for the chosen `em.mdp` criteria?",
            "Does the minimized structure still preserve the intended ligand or cofactor placement?",
        ],
        "analogy": "EM is like placing a complicated object on a table and letting the obviously strained pieces settle before you start shaking the table.",
    },
    {
        "slug": "nvt-equilibration",
        "short": "NVT",
        "title": "NVT Equilibration",
        "stage": "Temperature stabilization",
        "mdp": "nvt.mdp",
        "input": "em.gro from energy minimization",
        "output": "nvt.gro, nvt.cpt, nvt.edr, nvt.log",
        "summary": "NVT equilibration brings the minimized system to the target temperature while keeping the box volume fixed.",
        "plain": "After minimization, atoms are in a low-strain geometry, but the system is not yet a warm molecular environment. NVT assigns velocities and couples the system to a thermostat so solvent, ions, protein, and ligand begin moving at the intended temperature.",
        "what_happens": [
            "Initial velocities are generated according to the target temperature.",
            "The number of particles, volume, and temperature are controlled.",
            "Position restraints commonly keep heavy solute atoms from drifting while solvent and ions relax around them.",
            "The thermostat removes or adds kinetic energy so the temperature approaches the desired value.",
        ],
        "pipeline_role": [
            "Turns a minimized coordinate set into a thermally equilibrated system.",
            "Lets water and ions start adjusting around the restrained biomolecule.",
            "Creates a checkpoint that carries velocities and thermostat state into later stages.",
        ],
        "watch": [
            "NVT does not allow the box volume to change, so density and pressure are not fully settled yet.",
            "Temperature should stabilize near the target, but short fluctuations are normal.",
            "Large structural movement during restrained NVT may indicate bad setup or inappropriate restraints.",
        ],
        "beginner_checks": [
            "Does the temperature trace approach the intended target?",
            "Did `nvt.cpt` get written for continuation?",
            "Are restraints applied to the intended groups?",
            "Does the system remain intact when viewed after NVT?",
        ],
        "analogy": "NVT is like warming up the system in a fixed container before asking the container itself to find the right size.",
    },
    {
        "slug": "npt-equilibration",
        "short": "NPT",
        "title": "NPT Equilibration",
        "stage": "Pressure and density stabilization",
        "mdp": "npt.mdp",
        "input": "nvt.gro and nvt.cpt from NVT",
        "output": "npt.gro, npt.cpt, npt.edr, npt.log",
        "summary": "NPT equilibration lets the box volume adjust so pressure, density, solvent packing, and the restrained solute environment become production-ready.",
        "plain": "Once temperature is controlled, the simulation box still needs to breathe. NPT introduces pressure coupling so the box can expand or contract until the water, ions, protein, ligand, and cofactors occupy a physically reasonable density.",
        "what_happens": [
            "The simulation continues from NVT coordinates and checkpoint state.",
            "Temperature coupling remains active while pressure coupling is introduced.",
            "The box vectors can change, allowing the volume and density to relax.",
            "Position restraints are often retained or gradually reduced before production.",
        ],
        "pipeline_role": [
            "Builds a pressure- and density-equilibrated starting point for production MD.",
            "Reduces artifacts caused by a box that is too expanded or compressed after solvation.",
            "Produces the coordinate and checkpoint files used to launch production.",
        ],
        "watch": [
            "Pressure fluctuates strongly in small biomolecular systems; averages and density are usually more informative than instant values.",
            "Box instability, vacuum bubbles, or exploding coordinates signal a setup or parameter problem.",
            "Production should not begin until density and overall structure look reasonable.",
        ],
        "beginner_checks": [
            "Does density stabilize around a plausible value for solvated biomolecular systems?",
            "Does the box stop changing dramatically?",
            "Did `npt.cpt` get written cleanly?",
            "Do RMSD or visual inspection show that the restrained solute stayed coherent?",
        ],
        "analogy": "NPT is like letting a sealed but flexible container settle to the right pressure before you start collecting the experiment.",
    },
]


ENGINE_STEPS = [
    {
        "number": 1,
        "script": "1_AutomateGromacs.py",
        "phase": "Input selection",
        "title": "Choose or fetch the starting structure",
        "manual": "Pick a `.pdb`, `.cif`, or `.mmcif` file, or download a PDB entry by hand.",
        "command": "python 1_AutomateGromacs.py --pdb <complex.pdb>\n# or\npython 1_AutomateGromacs.py --fetch-pdb <PDB_ID>",
        "does": "PyMACS records the selected source, normalizes structure input, and prepares a reproducible setup workspace.",
    },
    {
        "number": 2,
        "script": "1_AutomateGromacs.py",
        "phase": "Structure cleanup",
        "title": "Separate protein from retained components",
        "manual": "grep -v \"<LIG>\" <complex.pdb> > protein.pdb",
        "command": "protein.pdb = complex minus selected ligand/cofactors\nretained_components = <LIG>, <COFACTOR>, ...",
        "does": "Instead of relying on fragile residue-name grep commands, PyMACS detects ligands, cofactors, waters, ions, polymers, and chain choices in a controlled way.",
    },
    {
        "number": 3,
        "script": "1_AutomateGromacs.py",
        "phase": "Structure cleanup",
        "title": "Repair and standardize the biomolecule",
        "manual": "Manually inspect missing atoms, hydrogens, chain IDs, residue names, and termini prompts.",
        "command": "repair protein.pdb\nwrite protein_pdb2gmx_ready.pdb\ncache chain names and component metadata",
        "does": "The script prepares the structure for GROMACS, stores chain/component metadata, and makes later automation less ambiguous.",
    },
    {
        "number": 4,
        "script": "1_AutomateGromacs.py",
        "phase": "Protein topology",
        "title": "Run pdb2gmx",
        "manual": "gmx pdb2gmx -f protein.pdb -o protein_processed.gro -p topol.top -ignh -water spc -ter",
        "command": "gmx pdb2gmx -f <protein_ready.pdb> -o protein_processed.gro -p topol.top -water spc -ter",
        "does": "PyMACS automates force-field selection and chain-aware termini choices so the protein topology is generated consistently.",
    },
    {
        "number": 5,
        "script": "1_AutomateGromacs.py",
        "phase": "Ligand topology",
        "title": "Prepare ligand parameter inputs",
        "manual": "Rename long CGenFF files, change residue names like `obj01` to `<LIG>`, and keep MOL2/STR files aligned.",
        "command": "<LIG>.cgenff.mol2\n<LIG>.str\nresidue name = <LIG>",
        "does": "The script checks the retained component path and expects ligand naming to line up across coordinates, MOL2, STR, and topology outputs.",
    },
    {
        "number": 6,
        "script": "1_AutomateGromacs.py",
        "phase": "Ligand topology",
        "title": "Convert CGenFF output to GROMACS files",
        "manual": "python cgenff_charmm2gmx_py3_nx2.py <LIG> <LIG>.cgenff.mol2 <LIG>.str charmm36_ljpme-jul2022.ff",
        "command": "python cgenff_charmm2gmx_py3_nx2.py <LIG> <LIG>.cgenff.mol2 <LIG>.str <charmm_forcefield>",
        "does": "PyMACS wraps the conversion path that creates ligand `.itp`, `.prm`, and coordinate helper files for GROMACS.",
    },
    {
        "number": 7,
        "script": "1_AutomateGromacs.py",
        "phase": "Ligand coordinates",
        "title": "Convert ligand coordinates",
        "manual": "gmx editconf -f <ligand>_ini.pdb -o <ligand>.gro",
        "command": "gmx editconf -f <ligand_pose.pdb> -o <ligand>.gro",
        "does": "The script generates GROMACS coordinate files for retained small molecules so they can be merged back into the complex.",
    },
    {
        "number": 8,
        "script": "1_AutomateGromacs.py",
        "phase": "System assembly",
        "title": "Merge protein and retained components",
        "manual": "Copy protein_processed.gro to complex.gro, paste ligand atoms at the end, then update the atom count.",
        "command": "protein_processed.gro + <ligand>.gro -> complex.gro\nupdate atom count",
        "does": "PyMACS assembles the coordinate file while preserving atom counts and component placement more reliably than manual copy/paste editing.",
    },
    {
        "number": 9,
        "script": "1_AutomateGromacs.py",
        "phase": "Topology assembly",
        "title": "Patch topology includes and molecule counts",
        "manual": "#include \"<ligand>.itp\"\n#include \"<ligand>.prm\"\n[ molecules ]\nProtein_chain_A 1\n<LIG> 1",
        "command": "topol.top includes force field, ligand parameters, ligand topology, and molecule counts",
        "does": "The script updates `topol.top` so GROMACS knows which molecules exist and where their parameters are defined.",
    },
    {
        "number": 10,
        "script": "1_AutomateGromacs.py",
        "phase": "Box setup",
        "title": "Define the simulation box",
        "manual": "gmx editconf -f complex.gro -o newbox.gro -bt cubic -d 1.0",
        "command": "gmx editconf -f complex.gro -o newbox.gro -bt <box_type> -d <box_distance>",
        "does": "PyMACS creates a box around the solute with configurable geometry and padding.",
    },
    {
        "number": 11,
        "script": "1_AutomateGromacs.py",
        "phase": "Solvation",
        "title": "Fill the box with water",
        "manual": "gmx solvate -cp newbox.gro -cs spc216.gro -p topol.top -o solv.gro",
        "command": "gmx solvate -cp newbox.gro -cs spc216.gro -p topol.top -o solv.gro",
        "does": "The script adds solvent molecules and updates the topology molecule counts.",
    },
    {
        "number": 12,
        "script": "1_AutomateGromacs.py",
        "phase": "Ion preparation",
        "title": "Compile the ion-placement system",
        "manual": "gmx grompp -f ions.mdp -c solv.gro -p topol.top -o ions.tpr -maxwarn 2",
        "command": "gmx grompp -f ions.mdp -c solv.gro -p topol.top -o ions.tpr -maxwarn 2",
        "does": "PyMACS builds the temporary binary input needed for `genion` and can retry known ordering problems when safe.",
    },
    {
        "number": 13,
        "script": "1_AutomateGromacs.py",
        "phase": "Ionization",
        "title": "Detect solvent and add ions",
        "manual": "Choose `SOL` interactively, then run genion to neutralize the box.",
        "command": "gmx genion -s ions.tpr -o solv_ions.gro -p topol.top -pname NA -nname CL -neutral -conc 0.15",
        "does": "The script detects the water group, replaces water molecules with counterions, neutralizes the system, and adds physiological salt when configured.",
    },
    {
        "number": 14,
        "script": "1_AutomateGromacs.py",
        "phase": "EM preparation",
        "title": "Compile energy minimization input",
        "manual": "gmx grompp -f em.mdp -c solv_ions.gro -p topol.top -o em.tpr -maxwarn 2",
        "command": "gmx grompp -f em.mdp -c solv_ions.gro -p topol.top -o em.tpr -maxwarn 2",
        "does": "Step 1 ends by writing `em.tpr`, which proves the solvated, ionized system can be compiled for minimization.",
    },
    {
        "number": 15,
        "script": "2_AutomateGromacs.py",
        "phase": "Energy minimization",
        "title": "Run EM and inspect the result",
        "manual": "gmx mdrun -v -deffnm em\n# optional CPU pinning / GPU session settings",
        "command": "gmx mdrun -v -deffnm em <resource_options>",
        "does": "PyMACS runs minimization, chooses CPU/GPU behavior, logs the command, and checks the minimization output before continuing.",
    },
    {
        "number": 16,
        "script": "2_AutomateGromacs.py",
        "phase": "Indexes and restraints",
        "title": "Build index groups and optional restraints",
        "manual": "gmx make_ndx -f em.gro -o index.ndx\n# manually name groups like Protein_LIG, Water_and_ions, Ligase, Target_A",
        "command": "gmx make_ndx -f em.gro -o index.ndx\noptional: gmx genrestr -f <ligand>.gro -o posre_<ligand>.itp",
        "does": "The script creates or validates index groups used by NVT/NPT/production and can generate ligand restraints when the workflow needs them.",
    },
    {
        "number": 17,
        "script": "2_AutomateGromacs.py",
        "phase": "NVT",
        "title": "Compile and run temperature equilibration",
        "manual": "gmx grompp -f nvt.mdp -c em.gro -r em.gro -p topol.top -n index.ndx -o nvt.tpr -maxwarn 2\ngmx mdrun -v -deffnm nvt",
        "command": "gmx grompp -f nvt.mdp -c em.gro -r em.gro -p topol.top -n index.ndx -o nvt.tpr\ngmx mdrun -v -deffnm nvt <resource_options>",
        "does": "PyMACS warms the minimized system at fixed volume, carries the correct index groups, and writes checkpoint files for continuation.",
    },
    {
        "number": 18,
        "script": "2_AutomateGromacs.py",
        "phase": "NPT and production",
        "title": "Equilibrate pressure, then collect the trajectory",
        "manual": "gmx grompp -f npt.mdp -c nvt.gro -r nvt.gro -t nvt.cpt -p topol.top -n index.ndx -o npt.tpr\ngmx mdrun -deffnm npt\ngmx grompp -f md.mdp -c npt.gro -t npt.cpt -p topol.top -n index.ndx -o md_0_1.tpr\ngmx mdrun -deffnm md_0_1",
        "command": "gmx grompp -f npt.mdp ... -o npt.tpr\ngmx mdrun -deffnm npt\ngmx grompp -f md.mdp ... -o md_0_1.tpr\ngmx mdrun -deffnm md_0_1 <resume_or_gpu_options>",
        "does": "PyMACS stabilizes density and pressure, compiles the production input, runs or resumes production MD, and records resource choices such as GPU IDs, thread counts, and checkpoint use.",
    },
    {
        "number": 19,
        "script": "3A_AutomateGromacs.py",
        "phase": "Analysis setup",
        "title": "Choose the analysis mode and load trajectory files",
        "manual": "Manually decide whether this is ligand, protein-only, peptide/interface, biological, or PROTAC analysis, then point every script to the right `.gro`, `.xtc`, `.tpr`, ligand code, and output folder.",
        "command": "python 3A_AutomateGromacs.py --mode <ligand|protein|peptide|biological|protac> --ligand <LIG>",
        "does": "PyMACS detects or prompts for the analysis route, loads the production trajectory, creates `Analysis_Results/`, and keeps the user's ligand, chain, and component choices connected to the setup metadata.",
    },
    {
        "number": 20,
        "script": "3A_AutomateGromacs.py",
        "phase": "Trajectory cleanup",
        "title": "Recenter and export the final trajectory",
        "manual": "Run `trjconv` or write custom MDAnalysis code to remove periodic-boundary jumps, center the complex, and export analysis-ready files.",
        "command": "md_0_1.xtc + npt.gro -> Final_Trajectory.xtc\nFinal_Trajectory.pdb",
        "does": "The script writes centered `Final_Trajectory` files so downstream calculations and visualization tools operate on a coherent molecular system.",
    },
    {
        "number": 21,
        "script": "3A_AutomateGromacs.py",
        "phase": "Pocket extraction",
        "title": "Build a binding-pocket trajectory",
        "manual": "Select residues within a cutoff of the ligand, write a smaller PDB/XTC, and keep the selection consistent across frames.",
        "command": "select protein residues within <pocket_cutoff> A of <LIG>\nwrite binding_pocket_only.pdb / binding_pocket_only.xtc",
        "does": "PyMACS creates pocket-only files that are easier to inspect and faster to use for ligand-centered analysis.",
    },
    {
        "number": 22,
        "script": "3A_AutomateGromacs.py",
        "phase": "Metadata reuse",
        "title": "Reuse chain and component registries",
        "manual": "Keep notes mapping atom ranges to chain names, ligand IDs, cofactors, and biological components, then rewrite those mappings in every analysis notebook.",
        "command": "read atomIndex.txt\nread pymacs_system_registry.json\nread pymacs_components.json",
        "does": "The analysis stage reuses setup metadata so chain-resolved plots and component-aware outputs keep the same names the user chose earlier.",
    },
    {
        "number": 23,
        "script": "3A_AutomateGromacs.py",
        "phase": "Global stability",
        "title": "Calculate protein and full-complex RMSD",
        "manual": "Align each frame to a reference, calculate RMSD over time, export a CSV table, and make a plot.",
        "command": "Protein_RMSD.csv / .png\nFullComplex_RMSD.csv / .png",
        "does": "PyMACS creates the basic stability plots that tell users whether the protein or full simulated assembly drifted, plateaued, or changed substantially.",
    },
    {
        "number": 24,
        "script": "3A_AutomateGromacs.py",
        "phase": "Chain dynamics",
        "title": "Calculate chain-resolved RMSD and RMSF",
        "manual": "Split the system by chain, align selections carefully, compute RMSD/RMSF for each chain, then label plots and CSVs by hand.",
        "command": "RMSD_<CHAIN>.csv / .png\nRMSF_<CHAIN>.csv / .png\nRMSF_<CHAIN>_per_residue.csv",
        "does": "The script breaks global motion into chain-level stability and flexibility so users can see which protein region is rigid, mobile, or asymmetric.",
    },
    {
        "number": 25,
        "script": "3A_AutomateGromacs.py",
        "phase": "Ligand dynamics",
        "title": "Measure ligand pose stability and flexibility",
        "manual": "Select ligand atoms, align to the protein or complex, calculate ligand RMSD and per-atom RMSF, then format ligand-specific plots.",
        "command": "<LIG>_Ligand_RMSD.csv / .png\n<LIG>_Ligand_RMSF.csv / .png",
        "does": "PyMACS shows whether the ligand stayed near the original binding pose, sampled nearby poses, became internally flexible, or left the pocket.",
    },
    {
        "number": 26,
        "script": "3A_AutomateGromacs.py",
        "phase": "Compactness",
        "title": "Calculate radius of gyration",
        "manual": "Compute compactness traces for the protein, ligand, and complex, then overlay them into a readable figure.",
        "command": "Radius_of_Gyration_Protein.csv / .png\nRadius_of_Gyration_Protein_Ligand_Complex.csv\nRadius_of_Gyration_Overlay.png",
        "does": "The script adds a compactness check that complements RMSD by showing expansion, collapse, or breathing motion.",
    },
    {
        "number": 27,
        "script": "3A_AutomateGromacs.py",
        "phase": "Secondary structure",
        "title": "Run DSSP and summarize SSE behavior",
        "manual": "Run secondary-structure assignment, encode residue states over time, make heatmaps, and summarize helix/sheet/coil fractions.",
        "command": "DSSP_raw.csv\nDSSP_encoded_numeric.csv\nDSSP_Heatmap.png\nSSE_Fractions.png\nResidue_SSE_Persistence.csv",
        "does": "PyMACS helps users see whether helices, sheets, loops, and structural motifs persist or change during the trajectory.",
    },
    {
        "number": 28,
        "script": "3A_AutomateGromacs.py",
        "phase": "Contact analysis",
        "title": "Scan ligand or partner contacts frame by frame",
        "manual": "For every frame, calculate distances between ligand/partner atoms and nearby protein residues, apply cutoffs, and save a large contact table.",
        "command": "AllContacts_Framewise.csv\nFilteredContacts_Framewise.csv\n--contact_cutoff <distance>",
        "does": "The script turns a trajectory into residue-level contact evidence: which residues touch the ligand or partner, how often, and when.",
    },
    {
        "number": 29,
        "script": "3A_AutomateGromacs.py",
        "phase": "Interaction typing",
        "title": "Classify and plot interaction behavior",
        "manual": "Separate distance contacts from hydrogen-bond-like, hydrophobic, ionic, and water-mediated patterns, then build timelines, heatmaps, violins, and ranked residue plots.",
        "command": "InteractionTypes_Framewise.csv\nInteractionTypes_Summary.csv\ninteraction_heatmap_normalized.png\ninteraction_type_violin.png\nbinding_importance_ranking.png",
        "does": "PyMACS converts raw contacts into chemically interpretable summaries that are easier for medicinal chemistry and structural biology users to read.",
    },
    {
        "number": 30,
        "script": "3A_AutomateGromacs.py",
        "phase": "Interface analysis",
        "title": "Handle protein, peptide, and biological-system interfaces",
        "manual": "Write separate scripts for chain-chain contacts, protein-peptide contacts, biological macromolecule distances, and mode-specific outputs.",
        "command": "Biomolecule_Chain_Interaction_Heatmap.png\nBiomolecule_Chain_Interaction_Distances.png\nInterface_* outputs when applicable",
        "does": "When the system is not a simple small-molecule case, PyMACS routes analysis toward chain interfaces, peptide contacts, or biological assemblies instead of forcing a ligand-only interpretation.",
    },
    {
        "number": 31,
        "script": "3A_AutomateGromacs.py -> 3_PROTAC_Analysis.py",
        "phase": "PROTAC handoff",
        "title": "Dispatch ternary-complex analysis when needed",
        "manual": "Manually decide frame stride, component roles, linker handling, protein partners, and which expensive analyses to run for a PROTAC trajectory.",
        "command": "python 3_PROTAC_Analysis.py --ligand <PROTAC> --frame-step <N>\noptional: --quick-test, --basic-only, --contacts-only",
        "does": "In PROTAC mode, PyMACS hands off to the dedicated ternary-complex analyzer with controlled sampling and mode-specific outputs.",
    },
    {
        "number": 32,
        "script": "3_PROTAC_Analysis.py",
        "phase": "PROTAC outputs",
        "title": "Generate component-aware PROTAC reports",
        "manual": "Write separate analyses for ligand contacts by protein partner, ternary geometry, networks, water bridges, PCA, QC manifests, and figure routing.",
        "command": "Analysis_Results/PROTAC/RMSD_RMSF/\nAnalysis_Results/PROTAC/Contacts/\nAnalysis_Results/PROTAC/Networks/\nAnalysis_Results/PROTAC/QC/protac_figure_manifest.csv",
        "does": "The PROTAC script organizes ternary-complex results into a dedicated tree that keeps component roles, contact summaries, structures, geometry, and QC metadata together.",
    },
    {
        "number": 33,
        "script": "3B_NETWORX.py",
        "phase": "Network rendering",
        "title": "Render ligand-residue or peptide-contact networks",
        "manual": "Read contact summary CSVs, draw a ligand or peptide interaction map, label residues, choose thresholds, and export presentation-ready panels.",
        "command": "python 3B_NETWORX.py --ligand <LIG>\nAnalysis_Results/NETWORX/<LIG>_bar.png\nAnalysis_Results/NETWORX/<LIG>_network.png\nAnalysis_Results/NETWORX/<LIG>_expanded_clean.png",
        "does": "NETWORX translates contact and interaction tables into visual residue-network figures that are much easier to discuss than spreadsheets.",
    },
    {
        "number": 34,
        "script": "4PDF4MD.py",
        "phase": "Figurebook",
        "title": "Compile plots into a review-ready PDF",
        "manual": "Collect the useful PNGs, write captions, arrange pages, handle missing figures, and build separate report formats for ligand, protein, peptide, biological, or PROTAC runs.",
        "command": "python 4PDF4MD.py\nMD_ANALYSIS_FIGUREBOOK.pdf\nPROTAC_MD_ANALYSIS_FIGUREBOOK.pdf",
        "does": "The final script packages the generated analyses into a clean figurebook so users can review and share the simulation without hunting through folders.",
    },
    {
        "number": 35,
        "script": "00_Pymacs_X_analysis.py",
        "phase": "Optional comparison",
        "title": "Compare multiple completed runs",
        "manual": "Open several `Analysis_Results/` folders, normalize naming, compare RMSD/RMSF/contact outputs, and build a side-by-side summary by hand.",
        "command": "python 00_Pymacs_X_analysis.py --root <runs_folder> --outdir <dashboard_folder>",
        "does": "For larger projects, the optional comparative dashboard builder helps compare apo, ligand-bound, mutant, species, or replicate simulations after individual runs have been analyzed.",
    },
]


SCRIPT_STEPS = [
    {
        "slug": "system-preparation",
        "kicker": "Step 1",
        "title": "System Preparation",
        "script": "1_AutomateGromacs.py",
        "summary": "Cleans the input structure, handles chains and components, prepares CHARMM-compatible topologies, solvates the system, adds ions, and produces a simulation-ready minimization input.",
        "why": "MD is unforgiving: a missing atom, ambiguous ligand, wrong chain, or bad topology can invalidate everything downstream. Step 1 turns messy structural input into a reproducible GROMACS system.",
        "concepts": [
            "PDB, CIF, and mmCIF inputs",
            "structure cleanup and hydrogen handling",
            "protein, ligand, cofactor, peptide, RNA, and DNA recognition",
            "CHARMM36 or CHARMM36/LJ-PME topology generation",
            "CGenFF ligand conversion through charmm2gmx",
            "box definition, solvation, ionization, and energy-minimization setup",
        ],
        "outputs": [
            "protein.pdb",
            "protein_processed.gro",
            "complex.gro",
            "solv_ions.gro",
            "topol.top",
            "index.ndx",
            "atomIndex.txt",
            "em.tpr",
            "mdrun.log",
        ],
        "commands": [
            "python 1_AutomateGromacs.py --pdb CPD32_9G94.pdb",
            "python 1_AutomateGromacs.py --pdb CPD32_9G94.pdb --box-type dodecahedron --box-distance 1.0",
            "python 1_AutomateGromacs.py --pdb CPD32_9G94.pdb --strict-pdb-validation",
        ],
    },
    {
        "slug": "simulation",
        "kicker": "Step 2",
        "title": "Equilibration and Production MD",
        "script": "2_AutomateGromacs.py",
        "summary": "Runs energy minimization, NVT equilibration, NPT equilibration, and production molecular dynamics with configurable MDP files and CPU/GPU resource controls.",
        "why": "The prepared system must relax, reach the target temperature, reach the target pressure and density, and only then produce a trajectory suitable for interpretation.",
        "concepts": [
            "steepest-descents energy minimization",
            "NVT temperature equilibration",
            "NPT pressure and density equilibration",
            "production trajectory generation",
            "checkpoint-aware restart behavior",
            "CPU, GPU, thread, MPI, and index-group control",
        ],
        "outputs": [
            "em.gro",
            "nvt.tpr",
            "npt.tpr",
            "md_0_1.tpr",
            "md_0_1.xtc",
            "md_0_1.edr",
            "md_0_1.cpt",
            "mdrun.log",
        ],
        "commands": [
            "python 2_AutomateGromacs.py",
            "python 2_AutomateGromacs.py --compute GPU --gpu-id 0 --ntomp 8 --ntmpi 1",
            "python 2_AutomateGromacs.py --equilibration-plan docs/equilibration_plan_example.json",
        ],
        "stage_links": ["energy-minimization", "nvt-equilibration", "npt-equilibration"],
    },
    {
        "slug": "trajectory-analysis",
        "kicker": "Step 3A",
        "title": "Trajectory Analysis",
        "script": "3A_AutomateGromacs.py",
        "summary": "Recenters trajectories, builds analysis-ready subsets, calculates RMSD/RMSF/Rg, detects contacts, classifies interaction behavior, and writes plots plus CSV tables.",
        "why": "A trajectory is only useful after it is translated into scientific questions: did the system stabilize, where did it fluctuate, and which contacts persisted?",
        "concepts": [
            "Final_Trajectory exports",
            "binding-pocket extraction",
            "RMSD, RMSF, and radius of gyration",
            "secondary structure persistence",
            "ligand RMSD and ligand RMSF",
            "contact cutoffs, hydrogen-bond-like events, and interaction summaries",
        ],
        "outputs": [
            "Analysis_Results/Protein_RMSD.png",
            "Analysis_Results/FullComplex_RMSD.png",
            "Analysis_Results/Radius_of_Gyration_Overlay.png",
            "Analysis_Results/*_Ligand_RMSD.png",
            "Analysis_Results/FilteredContacts_Framewise.csv",
            "Analysis_Results/InteractionTypes_Summary.csv",
        ],
        "commands": [
            "python 3A_AutomateGromacs.py",
            "python 3A_AutomateGromacs.py --pocket-cutoff 6.0",
            "python 3A_AutomateGromacs.py --contact_cutoff 4.0 --hbond-distance-cutoff 3.5 --hbond-angle-cutoff 135",
        ],
    },
    {
        "slug": "network-rendering",
        "kicker": "Step 3B",
        "title": "Interaction Network Rendering",
        "script": "3B_NETWORX.py",
        "summary": "Builds ligand-centered interaction diagrams that connect chemically drawn ligand atoms to nearby residues and interaction classes.",
        "why": "Contact tables are powerful, but medicinal chemists often need a visual map that shows which residues matter and how they relate to the ligand scaffold.",
        "concepts": [
            "NETWORX ligand-residue panels",
            "residue contact filtering",
            "interaction-type-specific edges",
            "expanded clean figures for presentations",
            "combined network PDFs",
        ],
        "outputs": [
            "Analysis_Results/NETWORX/*_bar.png",
            "Analysis_Results/NETWORX/*_network.png",
            "Analysis_Results/NETWORX/*_expanded_clean.png",
            "Analysis_Results/NETWORX/*_combined.pdf",
        ],
        "commands": ["python 3B_NETWORX.py"],
    },
    {
        "slug": "protac-analysis",
        "kicker": "Specialized",
        "title": "PROTAC and Ternary Complex Analysis",
        "script": "3_PROTAC_Analysis.py",
        "summary": "Adds dedicated analysis for ternary-complex systems, including component-aware contacts, networks, geometry, quality-control manifests, and optional water bridges.",
        "why": "PROTAC simulations ask extra questions about a linker, two protein partners, ternary-interface geometry, and contact persistence across components.",
        "concepts": [
            "PROTAC role detection",
            "component-specific RMSD/RMSF",
            "ligand contacts by protein component",
            "ternary interaction networks",
            "geometry and water-bridge options",
            "QC manifests for figurebook routing",
        ],
        "outputs": [
            "Analysis_Results/PROTAC/QC/protac_figure_manifest.csv",
            "Analysis_Results/PROTAC/Contacts/ligand_contacts_detailed.csv",
            "Analysis_Results/PROTAC/Networks/protac_interaction_network_all_components.png",
            "PROTAC_MD_ANALYSIS_FIGUREBOOK.pdf",
        ],
        "commands": [
            "python 3_PROTAC_Analysis.py --ligand PTC",
            "python 3_PROTAC_Analysis.py --ligand PTC --quick-test",
            "python 3_PROTAC_Analysis.py --ligand PTC --contacts-only",
        ],
    },
    {
        "slug": "figurebook",
        "kicker": "Step 4",
        "title": "Figurebook Generation",
        "script": "4PDF4MD.py",
        "summary": "Compiles the plots, notes, contact summaries, and structural panels into a report-ready PDF figurebook.",
        "why": "A good MD workflow should not stop at scattered files. Step 4 packages results so a team can review, compare, and communicate the simulation clearly.",
        "concepts": [
            "figure manifest detection",
            "standard ligand, protein, peptide, biological, and PROTAC report paths",
            "plot captions and interpretive notes",
            "publication-ready PDF assembly",
        ],
        "outputs": [
            "MD_ANALYSIS_FIGUREBOOK.pdf",
            "PROTAC_MD_ANALYSIS_FIGUREBOOK.pdf",
        ],
        "commands": ["python 4PDF4MD.py"],
    },
]


FORCE_FIELDS = [
    {
        "name": "CHARMM36",
        "position": "PyMACS primary family",
        "description": "A widely used additive force-field family for proteins, nucleic acids, lipids, carbohydrates, ions, and related biomolecular systems.",
        "strengths": ["broad biomolecular coverage", "well established in GROMACS workflows", "strong pairing with CGenFF for ligands"],
        "watch": "Users still need compatible residue names, sensible protonation choices, and ligand parameters that match the chemistry being simulated.",
    },
    {
        "name": "CHARMM36/LJ-PME",
        "position": "Highlighted PyMACS variant",
        "description": "A CHARMM36-compatible variant that treats long-range Lennard-Jones interactions with particle-mesh Ewald methods for systems parameterized for that approach.",
        "strengths": ["consistent long-range dispersion treatment", "efficient nonbonded settings", "bundled in the PyMACS repository"],
        "watch": "Use it when the force-field files and system class are compatible; do not mix assumptions across variants casually.",
    },
    {
        "name": "CGenFF",
        "position": "Small-molecule parameterization",
        "description": "The CHARMM General Force Field assigns atom types, charges, bonded terms, and penalty scores for drug-like molecules and cofactors.",
        "strengths": ["good coverage of medicinal chemistry scaffolds", "penalty scores flag uncertain parameters", "fits CHARMM-family workflows"],
        "watch": "High penalty scores may require expert refinement before results are publication-grade.",
    },
    {
        "name": "AMBER",
        "position": "Common alternative",
        "description": "A major force-field family often used for proteins, nucleic acids, and biomolecular simulations, with GAFF commonly used for small molecules.",
        "strengths": ["large user community", "strong protein and nucleic-acid history", "many tutorials and tools"],
        "watch": "AMBER-style parameterization choices are not interchangeable with CHARMM choices without careful conversion and validation.",
    },
    {
        "name": "OPLS",
        "position": "Common alternative",
        "description": "A family used in biomolecular and small-molecule simulations, often associated with liquid-phase and organic chemistry parameterization traditions.",
        "strengths": ["useful small-molecule coverage", "established in several MD packages", "clear bonded and nonbonded forms"],
        "watch": "Topology generation and ligand workflows differ from CHARMM/CGenFF conventions.",
    },
    {
        "name": "GROMOS",
        "position": "Common alternative",
        "description": "A force-field family with a long history in biomolecular simulation and GROMACS-oriented workflows.",
        "strengths": ["historically important in GROMACS", "efficient united-atom options", "well known in European MD communities"],
        "watch": "United-atom and all-atom assumptions can affect how results compare with CHARMM or AMBER simulations.",
    },
    {
        "name": "Martini",
        "position": "Coarse-grained alternative",
        "description": "A coarse-grained force field that groups atoms into beads, allowing larger systems or longer timescales than typical all-atom MD.",
        "strengths": ["longer timescale sampling", "large membrane and assembly studies", "reduced computational cost"],
        "watch": "Coarse-grained simulations answer different questions than all-atom PyMACS/CHARMM workflows.",
    },
]


OUTPUT_GALLERY = [
    {
        "title": "Protein RMSD",
        "image": "gallery/Protein_RMSD.png",
        "caption": "Tracks global backbone stability after alignment. A plateau usually suggests the protein has settled into a stable conformational regime.",
    },
    {
        "title": "Ligand RMSD",
        "image": "gallery/A1D_Ligand_RMSD.png",
        "caption": "Shows whether the ligand preserves its starting binding pose, samples nearby sub-poses, or leaves the pocket.",
    },
    {
        "title": "Radius of Gyration",
        "image": "gallery/Radius_of_Gyration_Overlay.png",
        "caption": "Measures compactness for the protein, ligand, and full complex as the trajectory evolves.",
    },
    {
        "title": "Contact Frequency",
        "image": "gallery/A1D_contact_frequency_filtered.png",
        "caption": "Ranks binding-pocket residues by how persistently they contact the ligand across the sampled trajectory.",
    },
    {
        "title": "Interaction Heatmap",
        "image": "gallery/interaction_heatmap_normalized.png",
        "caption": "Summarizes how interaction types and residues distribute through time.",
    },
    {
        "title": "NETWORX Panel",
        "image": "gallery/A1D_expanded_clean.png",
        "caption": "Converts contact tables into a ligand-centered network view for interpretation and reporting.",
    },
]


EXAMPLE_SETS = [
    {
        "slug": "example-1",
        "name": "Example 1",
        "type": "Protein-ligand",
        "system": "CPD32_9G94 with ligand A1D",
        "difficulty": "Best first run",
        "time": "Short test: 0.25 ns",
        "lesson": "The shortest full demonstration of setup, production MD, ligand analysis, NETWORX output, and a final figurebook.",
        "best_for": "New users, teaching demos, environment checks, and the standard protein plus small-molecule workflow.",
        "included": [
            ("input/CPD32_9G94.pdb", "Starting protein-ligand structure"),
            ("parameters/A1D.str", "CGenFF stream file for A1D"),
            ("parameters/A1D.cgenff.mol2", "CGenFF MOL2 file for A1D"),
            ("prepared_system/", "Reference setup outputs"),
            ("completed_run/", "Reference MD and analysis outputs"),
        ],
        "steps": [
            {
                "title": "Prepare a clean working copy",
                "body": "Run this from the PyMACS repository root. It activates the setup environment, creates a disposable run folder, and copies the required input and ligand files.",
                "command": "conda activate cgenff\nmkdir -p RUNS/example1_beginner_test\ncd RUNS/example1_beginner_test\ncp ../../Example_Choices/Example1/input/CPD32_9G94.pdb .\ncp ../../Example_Choices/Example1/parameters/A1D.str .\ncp ../../Example_Choices/Example1/parameters/A1D.cgenff.mol2 .",
                "expect": "You should now be inside RUNS/example1_beginner_test with CPD32_9G94.pdb, A1D.str, and A1D.cgenff.mol2.",
            },
            {
                "title": "Run Script 1 setup",
                "body": "This builds the CHARMM/CGenFF-compatible GROMACS system: cleaned coordinates, topology, box, solvent, ions, and EM input.",
                "command": "python ../../1_AutomateGromacs.py --pdb CPD32_9G94.pdb --ligand A1D",
                "expect": "Look for topol.top, complex.gro, solv_ions.gro, index.ndx, atomIndex.txt, and em.tpr.",
            },
            {
                "title": "Run EM, NVT, NPT, and short production MD",
                "body": "Switch to the MD/analysis environment and run a small CPU-only test. Increase --ns later after the workflow works.",
                "command": "conda activate mdanalysis\npython ../../2_AutomateGromacs.py --mode ligand --ligand A1D --ns 0.25 --compute CPU --headless",
                "expect": "Look for em.gro, nvt.gro, npt.gro, md_0_1.xtc, md_0_1.tpr, md_0_1.edr, and md_0_1.log.",
            },
            {
                "title": "Analyze ligand stability and contacts",
                "body": "Script 3A recenters the trajectory, makes RMSD/RMSF/Rg plots, detects ligand contacts, and writes analysis tables.",
                "command": "python ../../3A_AutomateGromacs.py --mode ligand --ligand A1D --headless",
                "expect": "Look for Final_Trajectory.pdb, Final_Trajectory.xtc, binding_pocket_only files, and Analysis_Results/.",
            },
            {
                "title": "Build networks and the figurebook",
                "body": "NETWORX turns contact tables into ligand-residue network figures. The PDF script packages finished plots into a review-ready report.",
                "command": "python ../../3B_NETWORX.py --ligand A1D\npython ../../4PDF4MD.py",
                "expect": "Look for Analysis_Results/NETWORX/ and MD_ANALYSIS_FIGUREBOOK.pdf.",
            },
        ],
        "checks": [
            "Use this example first if you are unsure where to start.",
            "Keep --ns 0.25 until the full command chain finishes once.",
            "Do not rename A1D files unless you also update every topology and command reference.",
        ],
    },
    {
        "slug": "example-2",
        "name": "Example 2",
        "type": "Cofactor-aware receptor",
        "system": "9UWJ / AVPR1A with A1E and CLR",
        "difficulty": "Second example",
        "time": "Short test: 0.25 ns",
        "lesson": "Shows retained non-protein components and multi-chain topology handling.",
        "best_for": "Users with a main ligand plus a retained cofactor, cholesterol-like component, heme, ion, or other important context molecule.",
        "included": [
            ("input/9UWJ.cif", "Starting receptor structure"),
            ("parameters/A1E.str", "Main ligand CGenFF stream file"),
            ("parameters/A1E.cgenff.mol2", "Main ligand MOL2 file"),
            ("parameters/CLR.str", "Retained cofactor stream file"),
            ("parameters/CLR.cgenff.mol2", "Retained cofactor MOL2 file"),
            ("completed_run/", "Reference MD-stage outputs"),
        ],
        "steps": [
            {
                "title": "Prepare a clean working copy",
                "body": "Run this from the PyMACS repository root. It copies the receptor, main ligand, and retained cofactor files into a fresh run folder.",
                "command": "conda activate cgenff\nmkdir -p RUNS/example2_beginner_test\ncd RUNS/example2_beginner_test\ncp ../../Example_Choices/Example2/input/9UWJ.cif .\ncp ../../Example_Choices/Example2/parameters/A1E.str .\ncp ../../Example_Choices/Example2/parameters/A1E.cgenff.mol2 .\ncp ../../Example_Choices/Example2/parameters/CLR.str .\ncp ../../Example_Choices/Example2/parameters/CLR.cgenff.mol2 .",
                "expect": "You should now have 9UWJ.cif plus A1E and CLR parameter files in the run folder.",
            },
            {
                "title": "Run Script 1 with ligand and cofactor named",
                "body": "A1E is the main ligand for analysis. CLR is retained as a cofactor/context component so setup does not discard it.",
                "command": "python ../../1_AutomateGromacs.py --pdb 9UWJ.cif --ligand A1E --cofactors CLR",
                "expect": "Look for topol.top, component registry JSON files, cofactor topology includes, solv_ions.gro, and em.tpr.",
            },
            {
                "title": "Run EM, NVT, NPT, and a short MD test",
                "body": "This keeps the run intentionally short and CPU-safe while you confirm the cofactor-aware path works.",
                "command": "conda activate mdanalysis\npython ../../2_AutomateGromacs.py --mode ligand --ligand A1E --cofactors CLR --ns 0.25 --compute CPU --headless",
                "expect": "Look for md_0_1.xtc, md_0_1.tpr, md_0_1.edr, md_0_1.gro, and stage logs.",
            },
            {
                "title": "Analyze the main ligand while retaining context",
                "body": "The analysis targets A1E but keeps CLR as biological context rather than treating it as the ligand of interest.",
                "command": "python ../../3A_AutomateGromacs.py --mode ligand --ligand A1E --cofactors CLR --headless",
                "expect": "Look for Analysis_Results/ with ligand stability plots, contact tables, and interaction summaries.",
            },
            {
                "title": "Render interaction networks and report",
                "body": "Run these after 3A creates the contact and interaction tables.",
                "command": "python ../../3B_NETWORX.py --ligand A1E\npython ../../4PDF4MD.py",
                "expect": "Look for NETWORX figures and, when enough figures exist, MD_ANALYSIS_FIGUREBOOK.pdf.",
            },
        ],
        "checks": [
            "Use --cofactors for retained non-protein components that are not the main analysis ligand.",
            "If setup drops CLR, rerun Script 1 and check the ligand/cofactor names.",
            "The packaged completed_run folder is mainly an MD-stage reference for this example.",
        ],
    },
    {
        "slug": "example-3",
        "name": "Example 3",
        "type": "RNA/protein assembly",
        "system": "1URN",
        "difficulty": "Biological assembly",
        "time": "Short test: 0.25 ns",
        "lesson": "Demonstrates biological-system setup and simulation for mixed biomolecular assemblies.",
        "best_for": "RNA-protein systems, mixed biomolecular assemblies, and non-ligand workflows where the question is about the biological complex.",
        "included": [
            ("input/1URN.pdb", "Starting RNA-protein structure"),
            ("prepared_system/", "Reference RNA/protein topology and restraint files"),
            ("completed_run/Final_Trajectory.*", "Reference processed trajectory files"),
            ("completed_run/Analysis_Results/", "Reference biological analysis outputs"),
            ("completed_run/MD_ANALYSIS_FIGUREBOOK.pdf", "Reference figurebook"),
        ],
        "steps": [
            {
                "title": "Prepare a clean working copy",
                "body": "Run this from the PyMACS repository root. This example has no separate ligand parameter files.",
                "command": "conda activate cgenff\nmkdir -p RUNS/example3_beginner_test\ncd RUNS/example3_beginner_test\ncp ../../Example_Choices/Example3/input/1URN.pdb .",
                "expect": "You should now be inside RUNS/example3_beginner_test with 1URN.pdb.",
            },
            {
                "title": "Run Script 1 setup",
                "body": "Run Script 1 interactively or with only the input file so PyMACS can handle chain and component interpretation.",
                "command": "python ../../1_AutomateGromacs.py --pdb 1URN.pdb",
                "expect": "Look for RNA/protein topology includes, topol.top, index.ndx, solv_ions.gro, and em.tpr.",
            },
            {
                "title": "Run EM, NVT, NPT, and short biological MD",
                "body": "Biological mode tells Script 2 this is not a ligand-centered simulation.",
                "command": "conda activate mdanalysis\npython ../../2_AutomateGromacs.py --mode biological --ns 0.25 --compute CPU --headless",
                "expect": "Look for md_0_1.xtc, md_0_1.tpr, md_0_1.edr, md_0_1.gro, and stage logs.",
            },
            {
                "title": "Analyze the biological assembly",
                "body": "Script 3A creates chain-aware stability, secondary-structure, and biomolecular interaction outputs where supported.",
                "command": "python ../../3A_AutomateGromacs.py --mode biological --headless",
                "expect": "Look for Analysis_Results/, Final_Trajectory files, RMSD/RMSF outputs, DSSP outputs, and chain interaction summaries.",
            },
            {
                "title": "Build the figurebook",
                "body": "Use this once the analysis folder contains plots worth packaging.",
                "command": "python ../../4PDF4MD.py",
                "expect": "Look for MD_ANALYSIS_FIGUREBOOK.pdf.",
            },
        ],
        "checks": [
            "Choose biological mode, not ligand mode.",
            "Do not expect A1D/A1E/PTC-style ligand files in this example.",
            "Use the packaged completed_run folder to compare chain-level outputs.",
        ],
    },
    {
        "slug": "example-4",
        "name": "Example 4",
        "type": "PROTAC ternary complex",
        "system": "5T35 with PTC",
        "difficulty": "Advanced",
        "time": "Short test: 0.25 ns plus quick-test analysis",
        "lesson": "Highlights ternary-complex bookkeeping, contacts by component, geometry, networks, and PROTAC reporting.",
        "best_for": "PROTACs, ternary complexes, targeted-degradation systems, and users who need component-aware contact analysis.",
        "included": [
            ("input/5T35.pdb", "Starting ternary-complex structure"),
            ("parameters/PTC.str", "PROTAC CGenFF stream file"),
            ("parameters/PTC.cgenff.mol2", "PROTAC MOL2 file"),
            ("prepared_system/", "Reference VHL/BRD4/PTC setup outputs"),
            ("completed_run/", "Reference MD-stage outputs"),
        ],
        "steps": [
            {
                "title": "Prepare a clean working copy",
                "body": "Run this from the PyMACS repository root. It copies the ternary-complex input and PTC parameter files into a fresh run folder.",
                "command": "conda activate cgenff\nmkdir -p RUNS/example4_beginner_test\ncd RUNS/example4_beginner_test\ncp ../../Example_Choices/Example4/input/5T35.pdb .\ncp ../../Example_Choices/Example4/parameters/PTC.str .\ncp ../../Example_Choices/Example4/parameters/PTC.cgenff.mol2 .",
                "expect": "You should now have 5T35.pdb, PTC.str, and PTC.cgenff.mol2 in the run folder.",
            },
            {
                "title": "Run Script 1 setup",
                "body": "PTC is the PROTAC-like molecule. Script 1 still prepares the system through the standard setup path.",
                "command": "python ../../1_AutomateGromacs.py --pdb 5T35.pdb --ligand PTC",
                "expect": "Look for topol.top, protein partner topology files, PTC includes, solv_ions.gro, atomIndex.txt, and em.tpr.",
            },
            {
                "title": "Run EM, NVT, NPT, and short PROTAC MD",
                "body": "Use protac mode and a short CPU run first. Ternary systems can be expensive, so smoke-test before a long run.",
                "command": "conda activate mdanalysis\npython ../../2_AutomateGromacs.py --mode protac --ligand PTC --ns 0.25 --compute CPU --headless",
                "expect": "Look for md_0_1.xtc, md_0_1.tpr, md_0_1.edr, md_0_1.gro, and stage logs.",
            },
            {
                "title": "Run quick PROTAC analysis",
                "body": "The dedicated PROTAC script checks component roles, scans a smaller frame window, and writes component-aware outputs.",
                "command": "python ../../3_PROTAC_Analysis.py --ligand PTC --quick-test --headless",
                "expect": "Look for Analysis_Results/PROTAC/ with QC files, contact summaries, networks, and component plots.",
            },
            {
                "title": "Build the PROTAC figurebook",
                "body": "Use this after PROTAC analysis creates a manifest and enough figures.",
                "command": "python ../../4PDF4MD.py",
                "expect": "Look for PROTAC_MD_ANALYSIS_FIGUREBOOK.pdf, or a standard figurebook if only standard figures are present.",
            },
        ],
        "checks": [
            "Choose protac mode for Step 2.",
            "Use --quick-test before full PROTAC analysis.",
            "Keep atomIndex.txt because the PROTAC analyzer uses component atom ranges.",
        ],
    },
]


GLOSSARY = [
    ("Atomistic MD", "A simulation where each atom is represented explicitly and moved according to classical mechanics."),
    ("Trajectory", "The time-ordered coordinate file that records how atoms move during production MD."),
    ("Topology", "The file set describing atoms, bonds, angles, dihedrals, charges, masses, and nonbonded parameters."),
    ("Force field", "A mathematical model that estimates the energy and forces of a molecular system."),
    ("CHARMM36", "The CHARMM-family force field used by PyMACS for biomolecular topology generation."),
    ("CGenFF", "The CHARMM General Force Field used to parameterize many drug-like ligands and cofactors."),
    ("MDP file", "A GROMACS parameter file that controls integrator settings, timesteps, cutoffs, temperature coupling, pressure coupling, and output frequency."),
    ("Energy minimization", "A relaxation step that removes severe clashes before dynamics begin."),
    ("NVT", "Constant number of particles, volume, and temperature; often used to stabilize temperature."),
    ("NPT", "Constant number of particles, pressure, and temperature; often used to stabilize density and pressure."),
    ("Production MD", "The unrestrained simulation stage used for scientific analysis."),
    ("RMSD", "Root-mean-square deviation; a measure of structural change relative to a reference."),
    ("RMSF", "Root-mean-square fluctuation; a per-atom or per-residue measure of flexibility."),
    ("Radius of gyration", "A compactness measure that reports how spread out a molecular object is around its center."),
    ("Contact cutoff", "A distance threshold used to decide when a ligand and residue are close enough to count as a contact."),
    ("Binding pocket", "The set of protein residues near the ligand or partner molecule during the simulation."),
    ("Checkpoint", "A restart file that allows an interrupted simulation to continue without losing progress."),
]


RESOURCES = [
    {
        "title": "PyMACS website documentation",
        "href": "/docs.html",
        "body": "Clickable pymacs.com documentation pages rebuilt from the detailed README: install, environments, flags, force fields, CGenFF, examples, restarts, and troubleshooting.",
    },
    {
        "title": "PyMACS GitHub repository",
        "href": "https://github.com/schurerlab/Pymacs",
        "body": "Source code, examples, environment files, force-field folders, and user-facing documentation.",
    },
    {
        "title": "PyMACS paper",
        "href": "https://www.sciencedirect.com/science/article/pii/S0223523426004836",
        "body": "European Journal of Medicinal Chemistry, Volume 316, Article 119038, DOI 10.1016/j.ejmech.2026.119038.",
    },
    {
        "title": "Output gallery in the repository",
        "href": "https://github.com/schurerlab/Pymacs/tree/main/docs",
        "body": "Repository documentation that explains expected plots, CSV files, network panels, and figurebooks.",
    },
    {
        "title": "PyMACS GROMACS Installer",
        "href": "https://github.com/Joey305/gromacs-installation",
        "body": "Reproducible system-wide GROMACS installation for supported Linux and WSL2 PyMACS workstations, including optional NVIDIA CUDA acceleration and Conda-independent gmx access.",
    },
    {
        "title": "GROMACS documentation",
        "href": "https://manual.gromacs.org/",
        "body": "Reference documentation for the MD engine that PyMACS automates.",
    },
]
