# ANYopenSoft

**ANYopenSoft** is the public GitHub Pages portal and the governance,
ecosystem documentation and coordination home for the ANY open engineering
ecosystem — a set of independent Python packages and desktop applications for
structural, marine and offshore engineering.

This portal is a static site: plain HTML, CSS and a small dependency-free
JavaScript enhancement layer. All core content is readable with JavaScript
disabled; scripting only adds navigation toggling and project-directory
filtering.

## What is on the portal

- **Recent developments** — dated highlights of current ecosystem work, each
  linked to its public commit or repository on GitHub. Development labels
  describe progress, not release readiness.
- **Project directory** — every ecosystem repository with its role in one or
  two lines: canonical owners, applications, adapters and retired paths.
- **Ownership map** — which repository owns which engineering domain, and the
  contracts (public APIs, clear errors, SI boundaries, persistent identity)
  that govern dependencies.
- **Entry points** — where to start as an application user, a package
  developer or a governance follower.

Portal content reflects public repository records as of **6 October 2026**.
Each repository is the source of truth for its own scope, releases and
license; this portal makes no blanket standards-compliance, capability or
license claims across repositories.

## Key ecosystem facts (as of 2026-10-06)

- **ANYloads** defines loads and their evaluation independently of solver,
  geometry and mesh; pressure fields can be written as expressions, code or
  tables ([commit 8fdb08d](https://github.com/audunarn/ANYloads/commit/8fdb08de69c8e2ccfe7be9a746e6b4cd10c68d0b)).
- **ANYfem** is a separate FEM application with the Qt workbench by default;
  it integrates pressure definitions in Python or CSV/Excel through ANYloads
  ([commit 9848be2](https://github.com/audunarn/ANYfem/commit/9848be2),
  [commit 6f90a44](https://github.com/audunarn/ANYfem/commit/6f90a44)).
  **ANYstructure** retains its Tk-based FEM interface.
- **ANYgeometry** owns geometry, topology and intersections; recent work adds
  exact angular lifts for cylinder boundary rulings
  ([commit c6dc426](https://github.com/audunarn/ANYgeometry/commit/c6dc426)).
- **ANYmesh** owns discretization and is published as the Python distribution
  **ANYmesher** (`anymesher`); a provisional prepared planar network mesh
  consumer is in development
  ([commit 7182cb3](https://github.com/audunarn/ANYmesh/commit/7182cb3)).
- **ANYfileIO** is the canonical interchange repository; **ANYio**'s duplicate
  publishing path is retired; **ANYfileio-occt** is an optional OCCT adapter.
- **ANY3dView** owns backend-neutral 3D view contracts; **ANYtk3D** is the Tk
  adapter. **ANYworkspaceAI** is a distinct orchestration product.
- **ANYsolver**'s nonlinear-shell and general-contact routes are in
  development alongside its linear static engine.

## Local development

Serve the static site locally with Python's built-in HTTP server:

```powershell
cd C:\Github\ANYopenSoft
python -m http.server 8000
```

Then open `http://localhost:8000` in a browser. No build step, package
manager or framework is required.

## GitHub Pages deployment

1. Push `index.html`, `styles.css`, `app.js`, `README.md`, `assets/` and
   `.nojekyll` to the `main` branch of this repository.
2. In the repository settings on GitHub, open **Pages** (under Code and
   automation).
3. Under **Build and deployment** > **Source**, select **Deploy from a
   branch**, set the branch to `main` / `(root)` and save.
4. The site publishes at `https://audunarn.github.io/ANYopenSoft/`.

## Governance

- [ECOSYSTEM_GUIDE.md](https://github.com/audunarn/ANYopenSoft/blob/main/ECOSYSTEM_GUIDE.md) —
  ownership, development practice, testing and release rules for every ANY
  repository.
- [governance/ECOSYSTEM_PHILOSOPHY.md](https://github.com/audunarn/ANYopenSoft/blob/main/governance/ECOSYSTEM_PHILOSOPHY.md) —
  canonical doctrine and engineering policy.
- [governance/ROADMAP.md](https://github.com/audunarn/ANYopenSoft/blob/main/governance/ROADMAP.md) —
  the ecosystem plan.

## License

ANYopenSoft is licensed under the GNU General Public License v3.0; see
[LICENSE](LICENSE). Other ecosystem repositories state their own licenses in
their own repositories.
