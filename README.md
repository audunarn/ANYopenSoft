# ANYopenSoft

**ANYopenSoft** is the central open-source portal and web interface for the ANY software ecosystem — a collection of Python packages and desktop applications built for marine, offshore, and structural engineering according to DNV standards.

![ANYopenSoft Web Interface](https://img.shields.io/badge/License-GPL--3.0-blue.svg)
![DNV Standards](https://img.shields.io/badge/DNV-OS--C101%20%7C%20RP--C201%20%7C%20RP--C202-cyan)
![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Ready-emerald)

---

## Ecosystem Overview

### Main Interconnected Suite
- **[ANYstructure](https://github.com/audunarn/ANYstructure)**: Flagship desktop steel-structure design application for plate fields and cylinders, including weight, weld, and cost optimization based on DNV standards.
- **[ANYfem](https://github.com/audunarn/ANYfem)**: Finite Element Method (FEA) core framework providing element stiffness matrices and assembly routines.
- **[ANYsolver](https://github.com/audunarn/ANYsolver)**: Finite Element solver runtime supporting linear static, arc-length, follower pressure, and non-linear prestress/buckling recovery.

### Main Standalone Application
- **[ANYtimeseries](https://github.com/audunarn/ANYtimeseries)**: Processing suite for marine and offshore environmental time-series data, wave and wind loading histories, and structural response fatigue.

### Core Supporting Libraries
- **[ANYbuckling](https://github.com/audunarn/ANYbuckling)**: Standalone prescriptive (DNV-RP-C201/C202) and semi-analytical (PULS S3/U3) panel & shell buckling calculation engine.
- **[ANYgeometry](https://github.com/audunarn/ANYgeometry)**: Neutral surface geometry authority and parametric 3D CAD generator.
- **[ANYmaterial](https://github.com/audunarn/ANYmaterial)**: Material property database, DNV steel specifications, and orthotropic material definitions.
- **[ANYmesh](https://github.com/audunarn/ANYmesh)**: 2D/3D finite element mesh generator and preview controls.
- **[ANYio](https://github.com/audunarn/ANYio)**: Neutral file import/export, 3D IFC export, and format inspectors.
- **[ANYtk3D](https://github.com/audunarn/ANYtk3D)**: 3D CAD geometry and FE mesh visualization widgets for Tkinter desktop GUIs.

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
