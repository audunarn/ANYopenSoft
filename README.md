# ANYopenSoft

**ANYopenSoft** is the central open-source portal and web interface for the ANY software ecosystem — a collection of Python packages and desktop applications built for marine, offshore, and structural engineering adhering strictly to DNV standards.

![ANYopenSoft Web Interface](https://img.shields.io/badge/License-GPL--3.0-blue.svg)
![FE Formulation](https://img.shields.io/badge/Element%20Scope-Shell%20%26%20Beam-purple)
![DNV Standards](https://img.shields.io/badge/DNV-OS--C101%20%7C%20RP--C201%20%7C%20RP--C202%20%7C%20RP--C203-cyan)
![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Ready-emerald)

---

## Ecosystem Overview

### Main Applications
- **[ANYfem](https://github.com/audunarn/ANYfem)**: **Full End-to-End FEM Program** designed specifically for **shell and beam structures**. Covers geometric modeling (surfaces, beam axes, loads, boundary conditions), shell & beam element stiffness matrix assembly, linear static and non-linear solver execution via `ANYsolver`, and interactive 3D postprocessing (von Mises stress contours, principal stresses, displacements, beam axial/shear/bending forces).
- **[ANYstructure](https://github.com/audunarn/ANYstructure)**: Flagship desktop steel-structure design application for stiffened plate fields and cylindrical shells. Performs weight, weld, and cost optimization adhering strictly to **DNV-OS-C101** (thickness, section modulus, shear area), **DNVGL-RP-C201** (plate buckling), **DNV-RP-C202** (shell buckling), and **DNVGL-RP-C203** (fatigue). Integrates direct FE solver coupling via `ANYsolver`.
- **[ANYtimeseries](https://github.com/audunarn/ANYtimeseries)**: Main standalone software tool for **analyzing all time-series data**. Comprehensive processing suite for general signal processing, statistical distributions, power spectral density (PSD) estimation, peak detection, frequency filtering, rainflow cycle counting, structural response histories, and marine/offshore environmental load time-series.

### Calculation Engines
- **[ANYsolver](https://github.com/audunarn/ANYsolver)**: **Finite Element Calculation Engine specializing in shell and beam elements**. Supports linear static analysis, arc-length continuation path solver for non-linear load-deflection paths, follower pressure loads on current deformed area, von Karman or corotational shell kinematics, non-linear prestress, and buckling capacity recovery. Exposed via public contract `resolve_runtime_analysis()`.
- **[ANYbuckling](https://github.com/audunarn/ANYbuckling)**: Standalone calculation engine extracted from ANYstructure (no GUI, depends only on NumPy & SciPy). Implements prescriptive flat-plate buckling under **DNV-RP-C201** (`anybuckling.FlatStru`), cylindrical shell buckling under **DNV-RP-C202** (`anybuckling.CylStru`), and **PULS-type S3/U3 semi-analytical solver** (`anybuckling.semianalytical`) for ultimate capacity assessments.

### Core Supporting Libraries
- **[ANYgeometry](https://github.com/audunarn/ANYgeometry)**: Shared neutral surface geometry authority and parametric 3D CAD generator. Provides `anygeometry.generators` for plate fields, stiffened panels, cylinders, cones, and beam frame assemblies. Establishes a single lazy-cached `GeometryModel` instance for structural and meshing consumers.
- **[ANYmaterial](https://github.com/audunarn/ANYmaterial)**: Material property management database and authority. Contains structural steel definitions (NV S235, S315, S355, S420, S460, ABS-DH36), DNV material safety factors (γm = 1.15), temperature-dependent stress-strain curves, E-modulus (210 GPa), Poisson ratio (ν = 0.3), and orthotropic property representations.
- **[ANYmesh](https://github.com/audunarn/ANYmesh)**: 2D/3D shell element and beam element mesh generation and control library. Generates quadrilateral (4-node) and triangular (3-node) shell meshes for stiffened panels and cylindrical surfaces, 2-node beam element discretizations, local element coordinate systems, and mesh density controls.
- **[ANYio](https://github.com/audunarn/ANYio)**: Neutral file import/export library, IFC 3D product export (single joined IFC product without global Boolean union performance overhead), neutral data exchange pipelines, Excel project file parsing, and CAD file format inspectors.
- **[ANYtk3D](https://github.com/audunarn/ANYtk3D)**: Lightweight 3D shell surface and beam element visualization widgets designed for embedding inside Python Tkinter desktop applications. Renders CAD geometry models, 3D beam frames, quad/tri FE element meshes, and postprocessing stress fields.

---

## Empirical Verification & Benchmark Studies

The core calculation engines are rigorously validated against industry benchmarks:
- **DNV-RP-C201 & PULS S3/U3 Buckling**: Validated on standard stiffened plate fields against DNV prescriptive formulas and semi-analytical capacity limit curves.
- **Non-Linear Arc-Length Path Solver**: Validated against Bathe shallow cylindrical shell snap-through and Timoshenko beam bending benchmarks.
- **ASTM E1049-85 Rainflow Fatigue**: 100% exact cycle counting correlation on multi-peak offshore wave time-histories and JONSWAP wave spectra.

---

## Local Development & Testing

You can serve and test the static web page locally using Python's built-in HTTP server:

```powershell
# Navigate to ANYopenSoft repository
cd C:\Github\ANYopenSoft

# Start local web server on port 8000
python -m http.server 8000
```

Then open your browser at `http://localhost:8000`.

---

## GitHub Pages Deployment

To host this interface live on GitHub Pages:

1. Push all files (`index.html`, `styles.css`, `app.js`, `.nojekyll`, `README.md`) to the `main` branch of the `ANYopenSoft` repository on GitHub.
2. In your repository settings on GitHub, navigate to **Pages** (under Code and automation).
3. Under **Build and deployment** > **Source**, select **Deploy from a branch**.
4. Set the branch to `main` / `(root)` and click **Save**.
5. Your site will be published at `https://audunarn.github.io/ANYopenSoft/`!

---

## License

ANYopenSoft and its ecosystem libraries are licensed under the **GNU General Public License v3.0**.
