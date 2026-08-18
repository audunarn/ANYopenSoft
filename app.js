/**
 * ANYopenSoft - Technical Portal Application Logic
 * Interactive Engine: Precision Vector Schematics, Ecosystem Architecture Canvas,
 * DNV-RP-C201 Live Calculator, Tab Switcher, Code Copier, and Repository Search.
 */

// 1. Technical Schematic Vector Schematics for All 10 Packages
const PACKAGE_SCHEMATICS = {
  anyfem: {
    title: 'ANYfem — Full End-to-End Shell & Beam FEM Program',
    tag: 'Modeling • Solving • Postprocessing',
    footer: 'Complete end-to-end shell (quad/tri) and 2-node beam finite element program covering geometric modeling, stiffness assembly, linear/non-linear solving via ANYsolver, and postprocessing stress plots.',
    svg: `<svg viewBox="0 0 800 240" fill="none" xmlns="http://www.w3.org/2000/svg" class="schematic-svg">
      <defs>
        <pattern id="grid-fem" width="30" height="30" patternUnits="userSpaceOnUse"><path d="M 30 0 L 0 0 0 30" fill="none" stroke="var(--border-color)" stroke-width="0.5"/></pattern>
        <linearGradient id="stress-grad" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop offset="0%" stop-color="#38bdf8"/>
          <stop offset="35%" stop-color="#2ea043"/>
          <stop offset="70%" stop-color="#d29922"/>
          <stop offset="100%" stop-color="#f85149"/>
        </linearGradient>
      </defs>
      <rect width="800" height="240" fill="url(#grid-fem)"/>
      
      <!-- Coordinate Triad (x,y,z) -->
      <g transform="translate(60, 200)">
        <line x1="0" y1="0" x2="35" y2="0" stroke="#38bdf8" stroke-width="1.8"/>
        <line x1="0" y1="0" x2="0" y2="-35" stroke="#2ea043" stroke-width="1.8"/>
        <line x1="0" y1="0" x2="-20" y2="15" stroke="#818cf8" stroke-width="1.8"/>
        <text x="40" y="4" fill="#38bdf8" font-size="10" font-family="Fira Code" font-weight="600">x</text>
        <text x="-4" y="-40" fill="#2ea043" font-size="10" font-family="Fira Code" font-weight="600">y</text>
        <text x="-32" y="24" fill="#818cf8" font-size="10" font-family="Fira Code" font-weight="600">z</text>
      </g>

      <!-- 3D Shell Mesh Isometric Plane -->
      <path d="M 160 170 L 640 170 L 560 80 L 220 80 Z" fill="rgba(56, 189, 248, 0.06)" stroke="#38bdf8" stroke-width="1.6"/>
      <!-- Mesh Lines Quad-4 -->
      <line x1="280" y1="170" x2="305" y2="80" stroke="rgba(56, 189, 248, 0.4)" stroke-width="1.2"/>
      <line x1="400" y1="170" x2="390" y2="80" stroke="rgba(56, 189, 248, 0.4)" stroke-width="1.2"/>
      <line x1="520" y1="170" x2="475" y2="80" stroke="rgba(56, 189, 248, 0.4)" stroke-width="1.2"/>
      <line x1="190" y1="125" x2="600" y2="125" stroke="rgba(56, 189, 248, 0.4)" stroke-width="1.2"/>
      <!-- Diagonal Tri-3 Transitions -->
      <line x1="280" y1="170" x2="390" y2="125" stroke="rgba(129, 140, 248, 0.4)" stroke-dasharray="2 2"/>
      <line x1="400" y1="125" x2="520" y2="170" stroke="rgba(129, 140, 248, 0.4)" stroke-dasharray="2 2"/>

      <!-- 2-Node Beam Stiffeners Standing on Shell -->
      <path d="M 280 170 L 280 120 L 305 30 L 305 80 Z" fill="rgba(99, 102, 241, 0.15)" stroke="#6366f1" stroke-width="1.5"/>
      <path d="M 520 170 L 520 120 L 475 30 L 475 80 Z" fill="rgba(99, 102, 241, 0.15)" stroke="#6366f1" stroke-width="1.5"/>

      <!-- Fixed Boundary Glyphs -->
      <polygon points="160,170 150,185 170,185" fill="none" stroke="#f85149" stroke-width="1.4"/>
      <polygon points="640,170 630,185 650,185" fill="none" stroke="#f85149" stroke-width="1.4"/>
      <line x1="145" y1="188" x2="175" y2="188" stroke="#f85149" stroke-width="1.2"/>
      <line x1="625" y1="188" x2="655" y2="188" stroke="#f85149" stroke-width="1.2"/>

      <!-- Stress Contour Legend Bar -->
      <g transform="translate(560, 40)">
        <rect x="0" y="0" width="180" height="12" rx="2" fill="url(#stress-grad)"/>
        <text x="0" y="24" fill="var(--text-secondary)" font-size="9" font-family="Fira Code">0 MPa</text>
        <text x="70" y="24" fill="var(--text-secondary)" font-size="9" font-family="Fira Code">σ_vm</text>
        <text x="135" y="24" fill="#f85149" font-size="9" font-family="Fira Code">355 MPa</text>
      </g>

      <!-- Annotations -->
      <text x="140" y="25" fill="#818cf8" font-size="11" font-family="Fira Code">2-Node Corotational Beam</text>
      <text x="620" y="115" fill="#38bdf8" font-size="11" font-family="Fira Code">Quad-4 / Tri-3 Shell Mesh</text>
      <text x="150" y="210" fill="#f85149" font-size="10" font-family="Fira Code">Fixed BCs [u=v=w=θ=0]</text>
    </svg>`
  },

  anystructure: {
    title: 'ANYstructure — Desktop Steel-Structure Application',
    tag: 'DNV-OS-C101 • DNV-RP-C201 • Scantling Optimization',
    footer: 'Desktop steel-structure application for stiffened plate fields and cylindrical shells. Performs scantling optimization adhering to DNV standards.',
    svg: `<svg viewBox="0 0 800 240" fill="none" xmlns="http://www.w3.org/2000/svg" class="schematic-svg">
      <defs>
        <pattern id="grid-struct" width="30" height="30" patternUnits="userSpaceOnUse"><path d="M 30 0 L 0 0 0 30" fill="none" stroke="var(--border-color)" stroke-width="0.5"/></pattern>
        <marker id="arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 0 L 10 5 L 0 10 z" fill="#22d3ee"/>
        </marker>
      </defs>
      <rect width="800" height="240" fill="url(#grid-struct)"/>

      <!-- Plate Baseline -->
      <rect x="120" y="150" width="560" height="14" fill="rgba(34, 211, 238, 0.15)" stroke="#22d3ee" stroke-width="1.8"/>
      <!-- Stiffener 1 (T-Profile) -->
      <path d="M 220 150 L 220 65 L 255 65 L 255 78 L 234 78 L 234 150 Z" fill="#22d3ee" stroke="#22d3ee" stroke-width="1"/>
      <!-- Stiffener 2 (T-Profile) -->
      <path d="M 400 150 L 400 65 L 435 65 L 435 78 L 414 78 L 414 150 Z" fill="#22d3ee" stroke="#22d3ee" stroke-width="1"/>
      <!-- Stiffener 3 (T-Profile) -->
      <path d="M 580 150 L 580 65 L 615 65 L 615 78 L 594 78 L 594 150 Z" fill="#22d3ee" stroke="#22d3ee" stroke-width="1"/>

      <!-- Pressure Load Arrows q = 0.01 MPa -->
      <g stroke="#f85149" stroke-width="1.5" marker-end="url(#arrow)">
        <line x1="220" y1="215" x2="220" y2="175"/>
        <line x1="310" y1="215" x2="310" y2="175"/>
        <line x1="400" y1="215" x2="400" y2="175"/>
        <line x1="490" y1="215" x2="490" y2="175"/>
        <line x1="580" y1="215" x2="580" y2="175"/>
      </g>
      <text x="320" y="232" fill="#f85149" font-size="10" font-family="Fira Code">Lateral Pressure Load q (MPa)</text>

      <!-- Dimension Lines -->
      <line x1="220" y1="45" x2="400" y2="45" stroke="#38bdf8" stroke-width="1.2"/>
      <line x1="220" y1="40" x2="220" y2="50" stroke="#38bdf8" stroke-width="1.2"/>
      <line x1="400" y1="40" x2="400" y2="50" stroke="#38bdf8" stroke-width="1.2"/>
      <text x="270" y="38" fill="#38bdf8" font-size="10" font-family="Fira Code">s = 680 mm</text>

      <!-- Callout Tags -->
      <text x="60" y="145" fill="#22d3ee" font-size="10" font-family="Fira Code">Plate t = 12 mm</text>
      <text x="445" y="60" fill="#38bdf8" font-size="10" font-family="Fira Code">Stiffener: hw=260, tw=12, bf=49, tf=28</text>

      <!-- DNV Pass Badge -->
      <rect x="570" y="18" width="180" height="26" rx="4" fill="rgba(46, 160, 67, 0.15)" stroke="#2ea043" stroke-width="1.2"/>
      <text x="580" y="35" fill="#2ea043" font-size="10" font-family="Fira Code" font-weight="600">DNV-RP-C201: UF = 0.45</text>
    </svg>`
  },

  anysolver: {
    title: 'ANYsolver — Shell & Beam FE Calculation Engine',
    tag: 'Calculation Engine • Linear Static • Arc-Length Path Solver',
    footer: 'Finite element calculation engine runtime specializing in shell and beam elements. Features arc-length continuation path solver and follower pressure capability.',
    svg: `<svg viewBox="0 0 800 240" fill="none" xmlns="http://www.w3.org/2000/svg" class="schematic-svg">
      <defs>
        <pattern id="grid-solver" width="30" height="30" patternUnits="userSpaceOnUse"><path d="M 30 0 L 0 0 0 30" fill="none" stroke="var(--border-color)" stroke-width="0.5"/></pattern>
      </defs>
      <rect width="800" height="240" fill="url(#grid-solver)"/>

      <!-- Axes (Displacement u vs Load Factor Lambda) -->
      <line x1="120" y1="195" x2="680" y2="195" stroke="var(--border-color)" stroke-width="1.5"/>
      <line x1="120" y1="195" x2="120" y2="35" stroke="var(--border-color)" stroke-width="1.5"/>
      <text x="690" y="198" fill="var(--text-secondary)" font-size="11" font-family="Fira Code">Deflection u</text>
      <text x="80" y="35" fill="#818cf8" font-size="11" font-family="Fira Code">Load λ</text>

      <!-- Non-Linear Snap-Through Equilibrium Path -->
      <path d="M 120 195 Q 260 30 400 110 T 660 70" fill="none" stroke="#818cf8" stroke-width="2.5"/>

      <!-- Arc-Length Iteration Constraint Sphere/Circle -->
      <circle cx="275" cy="85" r="42" fill="rgba(56, 189, 248, 0.08)" stroke="#38bdf8" stroke-width="1.2" stroke-dasharray="3 3"/>
      <circle cx="275" cy="85" r="5" fill="#f85149"/>
      <circle cx="317" cy="85" r="5" fill="#38bdf8"/>
      <line x1="275" y1="85" x2="317" y2="85" stroke="#38bdf8" stroke-width="1.8"/>

      <!-- Snap-Through Limit Point -->
      <circle cx="250" cy="55" r="5" fill="#d29922"/>
      <text x="260" y="50" fill="#d29922" font-size="10" font-family="Fira Code">Limit Point (Snap-Through)</text>

      <text x="325" y="80" fill="#38bdf8" font-size="10" font-family="Fira Code">Arc-Length Step Δs</text>
      <text x="470" y="125" fill="#818cf8" font-size="10" font-family="Fira Code">Post-Buckling Branch [K_T(u)]</text>
      <text x="140" y="220" fill="var(--text-muted)" font-size="10" font-family="Fira Code">Riks-Crisfield Continuation Path Formulation</text>
    </svg>`
  },

  anytimeseries: {
    title: 'ANYtimeseries — Standalone Tool for Analyzing ALL Time Series',
    tag: 'Signal Processing • PSD Spectrum • Rainflow Cycle Counting',
    footer: 'Main standalone application for analyzing all time-series data: signal processing, power spectral density (PSD) estimation, peak detection, and rainflow fatigue cycle counting.',
    svg: `<svg viewBox="0 0 800 240" fill="none" xmlns="http://www.w3.org/2000/svg" class="schematic-svg">
      <defs>
        <pattern id="grid-ts" width="30" height="30" patternUnits="userSpaceOnUse"><path d="M 30 0 L 0 0 0 30" fill="none" stroke="var(--border-color)" stroke-width="0.5"/></pattern>
      </defs>
      <rect width="800" height="240" fill="url(#grid-ts)"/>

      <!-- Left Panel: Time History Signal x(t) -->
      <g transform="translate(40, 20)">
        <rect x="0" y="0" width="340" height="175" rx="4" fill="rgba(22, 27, 34, 0.8)" stroke="var(--border-color)"/>
        <line x1="20" y1="90" x2="320" y2="90" stroke="var(--border-subtle)" stroke-width="1"/>
        <path d="M 20 90 Q 50 20 80 90 T 140 90 T 200 90 T 260 90 T 320 90" fill="none" stroke="#2ea043" stroke-width="2"/>
        <circle cx="50" cy="55" r="4" fill="#f85149"/><circle cx="110" cy="125" r="4" fill="#f85149"/>
        <circle cx="170" cy="55" r="4" fill="#f85149"/><circle cx="230" cy="125" r="4" fill="#f85149"/>
        <text x="15" y="22" fill="#2ea043" font-size="11" font-family="Fira Code" font-weight="600">Signal Time-Trace x(t)</text>
        <text x="15" y="160" fill="var(--text-muted)" font-size="9" font-family="Fira Code">Peak-to-Peak &amp; Zero-Crossing Analysis</text>
      </g>

      <!-- Right Panel: Power Spectral Density S(f) & Rainflow -->
      <g transform="translate(420, 20)">
        <rect x="0" y="0" width="340" height="175" rx="4" fill="rgba(22, 27, 34, 0.8)" stroke="var(--border-color)"/>
        <path d="M 20 140 C 60 140 80 30 110 30 C 140 30 170 120 220 135 C 270 140 300 140 320 140" fill="none" stroke="#38bdf8" stroke-width="2"/>
        <text x="15" y="22" fill="#38bdf8" font-size="11" font-family="Fira Code" font-weight="600">Power Spectral Density S(f)</text>
        <text x="110" y="25" fill="#d29922" font-size="10" font-family="Fira Code">Peak f_p = 0.12 Hz</text>
        <line x1="110" y1="30" x2="110" y2="140" stroke="#d29922" stroke-width="1" stroke-dasharray="3 3"/>
        <text x="15" y="160" fill="var(--text-muted)" font-size="9" font-family="Fira Code">ASTM E1049 Rainflow Fatigue Spectrum</text>
      </g>
    </svg>`
  },

  anybuckling: {
    title: 'ANYbuckling — Prescriptive & PULS S3/U3 Buckling Engine',
    tag: 'DNV-RP-C201 • DNV-RP-C202 • PULS S3/U3 Solver',
    footer: 'Standalone calculation engine implementing prescriptive DNV-RP-C201 flat plate, DNV-RP-C202 cylinder, and PULS S3/U3 semi-analytical panel buckling solvers.',
    svg: `<svg viewBox="0 0 800 240" fill="none" xmlns="http://www.w3.org/2000/svg" class="schematic-svg">
      <defs>
        <pattern id="grid-buck" width="30" height="30" patternUnits="userSpaceOnUse"><path d="M 30 0 L 0 0 0 30" fill="none" stroke="var(--border-color)" stroke-width="0.5"/></pattern>
      </defs>
      <rect width="800" height="240" fill="url(#grid-buck)"/>

      <!-- Buckling Half-Wave Mode Shape -->
      <g transform="translate(100, 30)">
        <path d="M 50 130 Q 300 20 550 130" fill="none" stroke="#d29922" stroke-width="2.8" stroke-dasharray="5 3"/>
        <line x1="50" y1="130" x2="550" y2="130" stroke="var(--border-color)" stroke-width="1.5"/>
        
        <!-- Compressive Stress Influx Vectors -->
        <line x1="10" y1="130" x2="45" y2="130" stroke="#f85149" stroke-width="2"/>
        <line x1="590" y1="130" x2="555" y2="130" stroke="#f85149" stroke-width="2"/>
        <text x="0" y="115" fill="#f85149" font-size="11" font-family="Fira Code">σ_x</text>
        <text x="560" y="115" fill="#f85149" font-size="11" font-family="Fira Code">σ_x</text>

        <text x="210" y="55" fill="#d29922" font-size="11" font-family="Fira Code" font-weight="600">Eigenmode w(x,y) = w_0 sin(πx/a) sin(πy/b)</text>
      </g>

      <!-- Capacity Evaluation Box -->
      <g transform="translate(480, 160)">
        <rect x="0" y="0" width="280" height="42" rx="4" fill="rgba(210, 153, 34, 0.12)" stroke="#d29922"/>
        <text x="12" y="18" fill="#d29922" font-size="10" font-family="Fira Code" font-weight="600">PULS S3/U3: σ_cr = 266.5 MPa</text>
        <text x="12" y="32" fill="var(--text-secondary)" font-size="9" font-family="Fira Code">DNV-RP-C201 Prescriptive λ_p = 1.067</text>
      </g>
    </svg>`
  },

  anygeometry: {
    title: 'ANYgeometry — Neutral Surface Geometry Authority',
    tag: 'GeometryModel • Parametric Shell CAD • Beam Layouts',
    footer: 'Shared neutral surface geometry authority and parametric 3D CAD generator exposing GeometryModel for plate fields, stiffened panels, cylinders, cones, and beam frames.',
    svg: `<svg viewBox="0 0 800 240" fill="none" xmlns="http://www.w3.org/2000/svg" class="schematic-svg">
      <defs>
        <pattern id="grid-geom" width="30" height="30" patternUnits="userSpaceOnUse"><path d="M 30 0 L 0 0 0 30" fill="none" stroke="var(--border-color)" stroke-width="0.5"/></pattern>
      </defs>
      <rect width="800" height="240" fill="url(#grid-geom)"/>

      <!-- Parametric Curved Surface Patch (u,v) -->
      <path d="M 180 160 C 260 70 440 70 520 160" fill="none" stroke="#38bdf8" stroke-width="2"/>
      <path d="M 220 130 C 300 50 480 50 560 130" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3 3"/>
      <path d="M 260 100 C 340 30 520 30 600 100" fill="none" stroke="#38bdf8" stroke-width="1"/>

      <!-- Transverse Isocurves -->
      <line x1="180" y1="160" x2="260" y2="100" stroke="#818cf8" stroke-width="1.2"/>
      <line x1="350" y1="115" x2="430" y2="65" stroke="#818cf8" stroke-width="1.2"/>
      <line x1="520" y1="160" x2="600" y2="100" stroke="#818cf8" stroke-width="1.2"/>

      <text x="280" y="195" fill="#38bdf8" font-size="11" font-family="Fira Code">Parametric Surface Patch S(u, v)</text>
      <text x="120" y="50" fill="#818cf8" font-size="10" font-family="Fira Code">GeometryModel Authority</text>
    </svg>`
  },

  anymaterial: {
    title: 'ANYmaterial — Structural Material Database & Authority',
    tag: 'DNV Steel Specs • Safety Factors (γm=1.15) • Orthotropic',
    footer: 'Material property authority containing DNV steel specs (NV S235-S460, ABS-DH36), material safety factors (γm=1.15), and orthotropic property representations.',
    svg: `<svg viewBox="0 0 800 240" fill="none" xmlns="http://www.w3.org/2000/svg" class="schematic-svg">
      <defs>
        <pattern id="grid-mat" width="30" height="30" patternUnits="userSpaceOnUse"><path d="M 30 0 L 0 0 0 30" fill="none" stroke="var(--border-color)" stroke-width="0.5"/></pattern>
      </defs>
      <rect width="800" height="240" fill="url(#grid-mat)"/>

      <!-- True Stress-Strain Elastoplastic Curve -->
      <line x1="140" y1="190" x2="660" y2="190" stroke="var(--border-color)" stroke-width="1.5"/>
      <line x1="140" y1="190" x2="140" y2="40" stroke="var(--border-color)" stroke-width="1.5"/>
      
      <path d="M 140 190 L 280 65 L 620 65" fill="none" stroke="#38bdf8" stroke-width="2.5"/>
      <line x1="280" y1="65" x2="280" y2="190" stroke="rgba(248, 81, 73, 0.6)" stroke-width="1.5" stroke-dasharray="3 3"/>
      
      <!-- Design Strength Line f_d = f_y / γ_m -->
      <line x1="140" y1="80" x2="620" y2="80" stroke="#d29922" stroke-width="1.5" stroke-dasharray="4 2"/>

      <text x="290" y="60" fill="#38bdf8" font-size="11" font-family="Fira Code">NV S355 (f_y = 355 MPa)</text>
      <text x="290" y="98" fill="#d29922" font-size="10" font-family="Fira Code">Design Strength f_d = 308.7 MPa (γ_m = 1.15)</text>
      <text x="160" y="140" fill="var(--text-secondary)" font-size="10" font-family="Fira Code">E = 210 GPa, ν = 0.3</text>
    </svg>`
  },

  anymesh: {
    title: 'ANYmesh — 2D/3D Shell & Beam Element Mesher',
    tag: 'Quad (4-Node) Shells • Tri (3-Node) Shells • 2-Node Beam Mesh',
    footer: '2D/3D shell element and beam element mesh generator for quadrilateral, triangular shell elements, and 2-node beam element discretizations.',
    svg: `<svg viewBox="0 0 800 240" fill="none" xmlns="http://www.w3.org/2000/svg" class="schematic-svg">
      <defs>
        <pattern id="grid-mesh" width="30" height="30" patternUnits="userSpaceOnUse"><path d="M 30 0 L 0 0 0 30" fill="none" stroke="var(--border-color)" stroke-width="0.5"/></pattern>
      </defs>
      <rect width="800" height="240" fill="url(#grid-mesh)"/>

      <!-- Quad Structured Grid -->
      <g transform="translate(140, 50)">
        <rect x="0" y="0" width="200" height="130" fill="rgba(56, 189, 248, 0.08)" stroke="#38bdf8" stroke-width="1.8"/>
        <line x1="66" y1="0" x2="66" y2="130" stroke="#38bdf8" stroke-width="1"/>
        <line x1="133" y1="0" x2="133" y2="130" stroke="#38bdf8" stroke-width="1"/>
        <line x1="0" y1="65" x2="200" y2="65" stroke="#38bdf8" stroke-width="1"/>
        <text x="35" y="150" fill="#38bdf8" font-size="11" font-family="Fira Code">Quad-4 Shell Elements</text>
      </g>

      <!-- Tri Unstructured Transition Grid -->
      <g transform="translate(460, 50)">
        <polygon points="0,0 200,0 100,130" fill="rgba(129, 140, 248, 0.08)" stroke="#818cf8" stroke-width="1.8"/>
        <line x1="0" y1="0" x2="100" y2="130" stroke="#818cf8" stroke-width="1"/>
        <line x1="200" y1="0" x2="100" y2="130" stroke="#818cf8" stroke-width="1"/>
        <line x1="100" y1="0" x2="100" y2="130" stroke="#818cf8" stroke-width="1"/>
        <text x="35" y="150" fill="#818cf8" font-size="11" font-family="Fira Code">Tri-3 Shell Transition</text>
      </g>
    </svg>`
  },

  anyio: {
    title: 'ANYio — Neutral File Import/Export & IFC 3D Library',
    tag: 'IFC 3D Export • Neutral Exchange • Excel Project Parsing',
    footer: 'Neutral file import/export library handling single joined IFC 3D product export without global Boolean union overhead, and Excel project parsing.',
    svg: `<svg viewBox="0 0 800 240" fill="none" xmlns="http://www.w3.org/2000/svg" class="schematic-svg">
      <defs>
        <pattern id="grid-io" width="30" height="30" patternUnits="userSpaceOnUse"><path d="M 30 0 L 0 0 0 30" fill="none" stroke="var(--border-color)" stroke-width="0.5"/></pattern>
      </defs>
      <rect width="800" height="240" fill="url(#grid-io)"/>

      <!-- IFC Model Product Pipeline Diagram -->
      <g transform="translate(100, 60)">
        <rect x="0" y="0" width="160" height="110" rx="6" fill="rgba(34, 211, 238, 0.12)" stroke="#22d3ee"/>
        <text x="25" y="45" fill="#22d3ee" font-size="12" font-family="Fira Code" font-weight="600">IFC 3D Product</text>
        <text x="20" y="75" fill="var(--text-secondary)" font-size="9" font-family="Fira Code">IfcBuildingElement</text>
      </g>

      <g transform="translate(320, 105)">
        <line x1="0" y1="0" x2="150" y2="0" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4 2"/>
        <polygon points="150,0 140,-5 140,5" fill="#38bdf8"/>
        <text x="15" y="-12" fill="#38bdf8" font-size="10" font-family="Fira Code">Single-Product Stream</text>
      </g>

      <g transform="translate(530, 60)">
        <rect x="0" y="0" width="170" height="110" rx="6" fill="rgba(46, 160, 67, 0.12)" stroke="#2ea043"/>
        <text x="25" y="45" fill="#2ea043" font-size="12" font-family="Fira Code" font-weight="600">ANYstructure</text>
        <text x="20" y="75" fill="var(--text-secondary)" font-size="9" font-family="Fira Code">Zero-Union Overhead</text>
      </g>
    </svg>`
  },

  anytk3d: {
    title: 'ANYtk3D — Lightweight 3D Viewport Widget for Tkinter',
    tag: 'Tkinter Widget • 3D Surface Viewport • Stress Rendering',
    footer: 'Lightweight 3D shell surface and beam element visualization widget designed for embedding inside Python Tkinter desktop applications.',
    svg: `<svg viewBox="0 0 800 240" fill="none" xmlns="http://www.w3.org/2000/svg" class="schematic-svg">
      <defs>
        <pattern id="grid-tk" width="30" height="30" patternUnits="userSpaceOnUse"><path d="M 30 0 L 0 0 0 30" fill="none" stroke="var(--border-color)" stroke-width="0.5"/></pattern>
      </defs>
      <rect width="800" height="240" fill="url(#grid-tk)"/>

      <rect x="180" y="35" width="440" height="165" rx="6" fill="rgba(15, 23, 42, 0.9)" stroke="#818cf8" stroke-width="1.8"/>
      <path d="M 280 155 L 520 155 L 460 85 L 340 85 Z" fill="rgba(56, 189, 248, 0.12)" stroke="#38bdf8" stroke-width="1.5"/>
      <line x1="400" y1="155" x2="400" y2="85" stroke="#38bdf8" stroke-width="1"/>
      <line x1="310" y1="120" x2="490" y2="120" stroke="#38bdf8" stroke-width="1"/>
      
      <!-- Arcball Gizmo Circle -->
      <circle cx="560" cy="75" r="24" fill="none" stroke="#818cf8" stroke-width="1.2" stroke-dasharray="3 3"/>
      <ellipse cx="560" cy="75" rx="24" ry="10" fill="none" stroke="#818cf8" stroke-width="1"/>

      <text x="200" y="60" fill="#818cf8" font-size="11" font-family="Fira Code" font-weight="600">Tkinter OpenGL 3D Viewport</text>
      <text x="320" y="180" fill="#38bdf8" font-size="10" font-family="Fira Code">Embedded Tk Canvas Widget</text>
    </svg>`
  }
};

// 2. Package Image Showcase Controller
function initPackageImageShowcase() {
  const pkgTabs = document.querySelectorAll('.pkg-tab');
  const titleEl = document.getElementById('schematic-title');
  const tagEl = document.getElementById('schematic-tag');
  const viewportEl = document.getElementById('schematic-viewport');
  const footerEl = document.getElementById('schematic-footer-text');

  if (!viewportEl) return;

  function updateShowcase(pkgKey) {
    const data = PACKAGE_SCHEMATICS[pkgKey] || PACKAGE_SCHEMATICS.anyfem;

    // Update Tabs Active State
    pkgTabs.forEach(tab => {
      if (tab.getAttribute('data-pkg') === pkgKey) {
        tab.classList.add('active');
      } else {
        tab.classList.remove('active');
      }
    });

    // Fade Out & In for Smooth Transitions
    viewportEl.style.opacity = '0.3';
    setTimeout(() => {
      if (titleEl) titleEl.textContent = data.title;
      if (tagEl) tagEl.textContent = data.tag;
      if (footerEl) footerEl.textContent = data.footer;
      viewportEl.innerHTML = data.svg;
      viewportEl.style.opacity = '1';
    }, 120);
  }

  // Bind Tab Clicks & Hover
  pkgTabs.forEach(tab => {
    const pkg = tab.getAttribute('data-pkg');
    tab.addEventListener('mouseenter', () => updateShowcase(pkg));
    tab.addEventListener('click', () => updateShowcase(pkg));
  });

  // Also synchronize when hovering over main cards & repo cards
  const cardsWithPkg = document.querySelectorAll('[data-pkg]');
  cardsWithPkg.forEach(card => {
    card.addEventListener('mouseenter', () => {
      const pkg = card.getAttribute('data-pkg');
      if (PACKAGE_SCHEMATICS[pkg]) {
        updateShowcase(pkg);
      }
    });
  });

  // Initial Render (ANYfem)
  updateShowcase('anyfem');
}

// 3. Theme Toggle Controller
function initTheme() {
  const toggleBtn = document.getElementById('theme-toggle');
  const htmlEl = document.documentElement;

  const savedTheme = localStorage.getItem('any_theme') || 'dark';
  htmlEl.className = savedTheme;

  if (toggleBtn) {
    toggleBtn.addEventListener('click', () => {
      const current = htmlEl.classList.contains('dark') ? 'dark' : 'light';
      const next = current === 'dark' ? 'light' : 'dark';
      htmlEl.className = next;
      localStorage.setItem('any_theme', next);
    });
  }
}

// 4. Copy-to-Clipboard Functionality
function initCopyButtons() {
  const copyBtns = document.querySelectorAll('.copy-btn');
  const toast = document.getElementById('toast');

  function showToast(msg) {
    if (!toast) return;
    toast.textContent = msg || 'Copied to clipboard!';
    toast.classList.add('show');
    setTimeout(() => {
      toast.classList.remove('show');
    }, 2200);
  }

  copyBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const textToCopy = btn.getAttribute('data-copy');
      if (textToCopy) {
        navigator.clipboard.writeText(textToCopy).then(() => {
          showToast('Copied to clipboard!');
        }).catch(() => {
          showToast('Failed to copy');
        });
      }
    });
  });
}

// 5. Code Tabs Switching
function initTabs() {
  const tabBtns = document.querySelectorAll('.tab-btn');
  const tabContents = document.querySelectorAll('.tab-content');

  tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const targetId = btn.getAttribute('data-tab');

      tabBtns.forEach(b => b.classList.remove('active'));
      tabContents.forEach(c => c.classList.remove('active'));

      btn.classList.add('active');
      const targetContent = document.getElementById(targetId);
      if (targetContent) {
        targetContent.classList.add('active');
      }
    });
  });
}

// 6. Repository Search & Filtering
function initRepoFilters() {
  const searchInput = document.getElementById('repo-search');
  const filterTabs = document.querySelectorAll('.filter-tab');
  const repoCards = document.querySelectorAll('.repo-card');

  let activeCategory = 'all';
  let searchQuery = '';

  function applyFilters() {
    repoCards.forEach(card => {
      const cardCat = card.getAttribute('data-category');
      const keywords = (card.getAttribute('data-keywords') || '').toLowerCase();
      const textContent = card.textContent.toLowerCase();

      const matchesCat = (activeCategory === 'all') || (cardCat === activeCategory);
      const matchesSearch = !searchQuery || keywords.includes(searchQuery) || textContent.includes(searchQuery);

      if (matchesCat && matchesSearch) {
        card.style.display = 'flex';
      } else {
        card.style.display = 'none';
      }
    });
  }

  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      searchQuery = e.target.value.toLowerCase().trim();
      applyFilters();
    });
  }

  filterTabs.forEach(tab => {
    tab.addEventListener('click', () => {
      filterTabs.forEach(t => t.classList.remove('active'));
      tab.classList.add('active');
      activeCategory = tab.getAttribute('data-filter');
      applyFilters();
    });
  });
}

// 7. Interactive DNV-RP-C201 Buckling Calculator Engine
function initBucklingCalculator() {
  const inputSpan = document.getElementById('input-span');
  const inputSpacing = document.getElementById('input-spacing');
  const inputThick = document.getElementById('input-thick');
  const inputYield = document.getElementById('input-yield');
  const inputSigX = document.getElementById('input-sigx');
  const inputSigY = document.getElementById('input-sigy');
  const inputTau = document.getElementById('input-tau');

  const valSpan = document.getElementById('val-span');
  const valSpacing = document.getElementById('val-spacing');
  const valThick = document.getElementById('val-thick');

  const ufValue = document.getElementById('uf-value');
  const gaugeCircle = document.getElementById('gauge-circle');
  const statusPill = document.getElementById('status-pill');
  const resSigmaE = document.getElementById('res-sigma-e');
  const resLambda = document.getElementById('res-lambda');
  const resSigmaCr = document.getElementById('res-sigma-cr');
  const resSigmaVm = document.getElementById('res-sigma-vm');

  if (!inputSpan || !inputSpacing || !inputThick || !inputYield) return;

  function calculate() {
    const L = parseFloat(inputSpan.value);       // mm
    const s = parseFloat(inputSpacing.value);    // mm
    const t = parseFloat(inputThick.value);      // mm
    const fy = parseFloat(inputYield.value);     // MPa
    const sigX = parseFloat(inputSigX.value) || 0;
    const sigY = parseFloat(inputSigY.value) || 0;
    const tau = parseFloat(inputTau.value) || 0;

    // Display Range Value Labels
    if (valSpan) valSpan.textContent = `${L} mm`;
    if (valSpacing) valSpacing.textContent = `${s} mm`;
    if (valThick) valThick.textContent = `${t} mm`;

    // Engineering Formulas (DNV-RP-C201 Section 5)
    const E = 210000; // MPa
    const nu = 0.3;
    const gammaM = 1.15;

    // Aspect Ratio & Buckling Factor kl
    const alpha = L / s;
    const kl = alpha >= 1.0 ? 4.0 : Math.pow(alpha + 1.0 / alpha, 2);

    // Elastic Ideal Buckling Stress: sigma_E = kl * (pi^2 * E) / (12 * (1 - nu^2)) * (t/s)^2
    const sigmaE = kl * (Math.PI * Math.PI * E) / (12 * (1 - nu * nu)) * Math.pow(t / s, 2);

    // Reduced Plate Slenderness: lambda_p = sqrt(fy / sigma_E)
    const lambdaP = Math.sqrt(fy / Math.max(sigmaE, 1e-6));

    // Buckling Reduction Factor: kappa
    let kappa = 1.0;
    if (lambdaP > 0.673) {
      kappa = (lambdaP - 0.055 * (3 + alpha * 0.1)) / Math.pow(lambdaP, 2);
      kappa = Math.min(Math.max(kappa, 0.05), 1.0);
    }

    // Critical Buckling Stress
    const sigmaCr = kappa * fy;

    // Von Mises Equivalent Stress: sigma_vm = sqrt(sigx^2 + sigy^2 - sigx*sigy + 3*tau^2)
    const sigmaVm = Math.sqrt(Math.max(0, sigX * sigX + sigY * sigY - sigX * sigY + 3 * tau * tau));

    // Usage Factor (UF) against Critical Buckling Capacity (with safety factor gammaM)
    const capacity = sigmaCr / gammaM;
    const uf = capacity > 0 ? (sigmaVm / capacity) : 9.99;
    const ufClamped = Math.min(Math.max(uf, 0), 2.5);

    // Update UI Elements
    if (ufValue) ufValue.textContent = uf.toFixed(2);
    if (resSigmaE) resSigmaE.textContent = `${sigmaE.toFixed(1)} MPa`;
    if (resLambda) resLambda.textContent = lambdaP.toFixed(3);
    if (resSigmaCr) resSigmaCr.textContent = `${sigmaCr.toFixed(1)} MPa`;
    if (resSigmaVm) resSigmaVm.textContent = `${sigmaVm.toFixed(1)} MPa`;

    // Visual Gauge & Status Pill Coloring
    const degrees = Math.min(360, (ufClamped / 1.5) * 360);
    let color = 'var(--accent-blue)';
    let statusText = 'SAFE CAPACITY';
    let statusClass = 'status-pill';

    if (uf <= 0.85) {
      color = '#2ea043';
      statusText = 'SAFE CAPACITY';
    } else if (uf <= 1.0) {
      color = '#d29922';
      statusText = 'OPTIMAL CAPACITY';
      statusClass = 'status-pill status-warning';
    } else {
      color = '#f85149';
      statusText = 'BUCKLING EXCEEDED';
      statusClass = 'status-pill status-danger';
    }

    if (gaugeCircle) {
      gaugeCircle.style.background = `conic-gradient(${color} 0deg ${degrees}deg, var(--border-color) ${degrees}deg 360deg)`;
    }
    if (statusPill) {
      statusPill.textContent = statusText;
      statusPill.className = statusClass;
    }
  }

  const inputs = [inputSpan, inputSpacing, inputThick, inputYield, inputSigX, inputSigY, inputTau];
  inputs.forEach(inp => {
    if (inp) {
      inp.addEventListener('input', calculate);
      inp.addEventListener('change', calculate);
    }
  });

  calculate();
}

// 8. Interactive Architecture Graph Visualizer (Canvas 2D)
function initArchitectureCanvas() {
  const canvas = document.getElementById('arch-canvas');
  if (!canvas) return;

  const ctx = canvas.getContext('2d');
  const tooltip = document.getElementById('node-tooltip');
  const infoTitle = document.getElementById('info-title');
  const infoDesc = document.getElementById('info-desc');
  const infoChips = document.getElementById('info-chips');

  const nodes = [
    {
      id: 'anyfem',
      label: 'ANYfem',
      type: 'main',
      x: 0.28, y: 0.28,
      desc: 'Full End-to-End Finite Element Program for shell & beam structures. Covers geometric modeling (surfaces, beam axes, loads), solver execution via ANYsolver, and postprocessing.',
      tags: ['Full FEM Suite', 'Shell & Beam Workflow', 'Modeling', 'Solving', 'Postprocessing']
    },
    {
      id: 'anystructure',
      label: 'ANYstructure',
      type: 'main',
      x: 0.65, y: 0.28,
      desc: 'Desktop Steel-Structure Application for plate fields & cylinders. Performs weight/weld/cost optimization adhering strictly to DNV-OS-C101, DNV-RP-C201, DNV-RP-C202, and DNVGL-RP-C203.',
      tags: ['Desktop App', 'DNV-OS-C101', 'DNV-RP-C201/202', 'DNVGL-RP-C203', 'Optimization']
    },
    {
      id: 'anysolver',
      label: 'ANYsolver',
      type: 'main',
      x: 0.50, y: 0.52,
      desc: 'Finite element calculation engine runtime specializing in shell and beam element models. Supports linear static analysis, arc-length continuation path solver, follower pressure on deformed area, corotational kinematics, and buckling recovery.',
      tags: ['Calculation Engine', 'Shell & Beam FE Solver', 'Linear Static', 'Arc-Length', 'Follower Pressure', 'Corotational Shells']
    },
    {
      id: 'anytimeseries',
      label: 'ANYtimeseries',
      type: 'standalone',
      x: 0.86, y: 0.28,
      desc: 'Main Standalone Software for analyzing ALL time-series data: general signal processing, statistical distributions, power spectral density (PSD) estimation, peak detection, frequency filtering, rainflow cycle counting, and time-history response analytics.',
      tags: ['Standalone App', 'All Time-Series Analysis', 'Signal Processing', 'PSD Estimation', 'Rainflow Counting']
    },
    {
      id: 'anybuckling',
      label: 'ANYbuckling',
      type: 'sub',
      x: 0.15, y: 0.78,
      desc: 'Standalone calculation engine extracted from ANYstructure (no GUI). Implements DNV-RP-C201 (FlatStru), DNV-RP-C202 (CylStru), and PULS-type S3/U3 semi-analytical panel capacity solver.',
      tags: ['Calculation Engine', 'DNV-RP-C201', 'DNV-RP-C202', 'PULS S3/U3']
    },
    {
      id: 'anygeometry',
      label: 'ANYgeometry',
      type: 'sub',
      x: 0.35, y: 0.78,
      desc: 'Shared neutral surface-geometry authority and parametric CAD generator. Exposes anygeometry.generators for plate fields, stiffened panels, cylinders, cones, and beam frames.',
      tags: ['Surface CAD Authority', 'GeometryModel', 'Parametric Shells', 'Beam Frames']
    },
    {
      id: 'anymaterial',
      label: 'ANYmaterial',
      type: 'sub',
      x: 0.53, y: 0.78,
      desc: 'Material property authority and database. Contains DNV steel specifications (NV S235-S460, ABS-DH36), material factors (γm=1.15), temperature curves, and orthotropic properties.',
      tags: ['Material Database', 'DNV Steel Specs', 'Safety Factors (γm)', 'Orthotropic']
    },
    {
      id: 'anymesh',
      label: 'ANYmesh',
      type: 'sub',
      x: 0.70, y: 0.78,
      desc: '2D/3D shell element and beam element mesh generator. Produces quad (4-node) and tri (3-node) shell element meshes, 2-node beam element discretizations, and density controls.',
      tags: ['Quad (4-Node) Shells', 'Tri (3-Node) Shells', '2-Node Beam Mesh']
    },
    {
      id: 'anyio',
      label: 'ANYio',
      type: 'sub',
      x: 0.87, y: 0.78,
      desc: 'Neutral file import/export library and format inspector. Handles single joined IFC 3D product export without global Boolean union overhead, and Excel project parsing.',
      tags: ['IFC 3D Export', 'Neutral File Exchange', 'Excel Parsing']
    }
  ];

  const connections = [
    { from: 'anyfem', to: 'anysolver' },
    { from: 'anystructure', to: 'anysolver' },
    { from: 'anystructure', to: 'anyfem' },
    { from: 'anystructure', to: 'anybuckling' },
    { from: 'anyfem', to: 'anygeometry' },
    { from: 'anyfem', to: 'anymesh' },
    { from: 'anygeometry', to: 'anymesh' },
    { from: 'anyfem', to: 'anymaterial' },
    { from: 'anystructure', to: 'anymaterial' },
    { from: 'anystructure', to: 'anyio' },
    { from: 'anyfem', to: 'anyio' }
  ];

  let hoveredNode = null;
  let selectedNode = nodes[0];

  function resizeCanvas() {
    const rect = canvas.getBoundingClientRect();
    canvas.width = rect.width * window.devicePixelRatio;
    canvas.height = rect.height * window.devicePixelRatio;
    ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
    draw();
  }

  function draw() {
    const w = canvas.getBoundingClientRect().width;
    const h = canvas.getBoundingClientRect().height;

    ctx.clearRect(0, 0, w, h);

    // Draw Subtle Grid
    ctx.strokeStyle = document.documentElement.classList.contains('light') ? '#e1e4e8' : '#21262d';
    ctx.lineWidth = 0.5;
    const gridSize = 25;
    for (let x = 0; x < w; x += gridSize) {
      ctx.beginPath();
      ctx.moveTo(x, 0);
      ctx.lineTo(x, h);
      ctx.stroke();
    }
    for (let y = 0; y < h; y += gridSize) {
      ctx.beginPath();
      ctx.moveTo(0, y);
      ctx.lineTo(w, y);
      ctx.stroke();
    }

    // Draw Connection Lines
    connections.forEach(conn => {
      const src = nodes.find(n => n.id === conn.from);
      const dst = nodes.find(n => n.id === conn.to);
      if (!src || !dst) return;

      const x1 = src.x * w;
      const y1 = src.y * h;
      const x2 = dst.x * w;
      const y2 = dst.y * h;

      const isHighlighted = (hoveredNode && (hoveredNode.id === src.id || hoveredNode.id === dst.id)) ||
                            (selectedNode && (selectedNode.id === src.id || selectedNode.id === dst.id));

      ctx.beginPath();
      ctx.moveTo(x1, y1);
      ctx.lineTo(x2, y2);
      ctx.strokeStyle = isHighlighted ? '#38bdf8' : (document.documentElement.classList.contains('light') ? '#d0d7de' : '#30363d');
      ctx.lineWidth = isHighlighted ? 2.2 : 1.2;
      ctx.setLineDash(isHighlighted ? [] : [4, 4]);
      ctx.stroke();
      ctx.setLineDash([]);
    });

    // Draw Nodes
    nodes.forEach(node => {
      const cx = node.x * w;
      const cy = node.y * h;
      const isHovered = hoveredNode && hoveredNode.id === node.id;
      const isSelected = selectedNode && selectedNode.id === node.id;

      let radius = node.type === 'main' ? 24 : (node.type === 'standalone' ? 22 : 18);
      let fillColor = '#161b22';
      let strokeColor = '#30363d';
      let textColor = '#f0f6fc';

      if (document.documentElement.classList.contains('light')) {
        fillColor = '#ffffff';
        strokeColor = '#d0d7de';
        textColor = '#1f2328';
      }

      if (node.type === 'main') {
        strokeColor = '#38bdf8';
        if (isHovered || isSelected) fillColor = 'rgba(56, 189, 248, 0.2)';
      } else if (node.type === 'standalone') {
        strokeColor = '#2ea043';
        if (isHovered || isSelected) fillColor = 'rgba(46, 160, 67, 0.2)';
      } else {
        strokeColor = '#818cf8';
        if (isHovered || isSelected) fillColor = 'rgba(129, 140, 248, 0.2)';
      }

      if (isSelected) {
        ctx.beginPath();
        ctx.arc(cx, cy, radius + 5, 0, Math.PI * 2);
        ctx.strokeStyle = 'rgba(56, 189, 248, 0.4)';
        ctx.lineWidth = 2;
        ctx.stroke();
      }

      ctx.beginPath();
      ctx.arc(cx, cy, radius, 0, Math.PI * 2);
      ctx.fillStyle = fillColor;
      ctx.fill();
      ctx.strokeStyle = strokeColor;
      ctx.lineWidth = isHovered || isSelected ? 2.5 : 1.5;
      ctx.stroke();

      // Node Label Text
      ctx.fillStyle = textColor;
      ctx.font = '600 11px Inter, sans-serif';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      ctx.fillText(node.label, cx, cy + radius + 14);
    });
  }

  function updateInfoCard(node) {
    if (!node) return;
    if (infoTitle) infoTitle.textContent = `${node.label} (${node.tags[0]})`;
    if (infoDesc) infoDesc.textContent = node.desc;
    if (infoChips) {
      infoChips.innerHTML = '';
      node.tags.forEach(tag => {
        const chip = document.createElement('span');
        chip.className = 'chip';
        chip.textContent = tag;
        infoChips.appendChild(chip);
      });
    }
  }

  function getNodeAtPos(x, y) {
    const rect = canvas.getBoundingClientRect();
    const px = x - rect.left;
    const py = y - rect.top;
    const w = rect.width;
    const h = rect.height;

    for (let node of nodes) {
      const nx = node.x * w;
      const ny = node.y * h;
      const dist = Math.hypot(px - nx, py - ny);
      const radius = node.type === 'main' ? 28 : 22;
      if (dist <= radius) return node;
    }
    return null;
  }

  canvas.addEventListener('mousemove', (e) => {
    const node = getNodeAtPos(e.clientX, e.clientY);
    if (node !== hoveredNode) {
      hoveredNode = node;
      canvas.style.cursor = node ? 'pointer' : 'default';
      draw();

      if (tooltip && node) {
        tooltip.style.display = 'block';
        tooltip.style.left = `${e.clientX - canvas.getBoundingClientRect().left + 12}px`;
        tooltip.style.top = `${e.clientY - canvas.getBoundingClientRect().top + 12}px`;
        tooltip.textContent = `${node.label} — ${node.tags[0]}`;
      } else if (tooltip) {
        tooltip.style.display = 'none';
      }
    }
  });

  canvas.addEventListener('mouseleave', () => {
    hoveredNode = null;
    if (tooltip) tooltip.style.display = 'none';
    draw();
  });

  canvas.addEventListener('click', (e) => {
    const node = getNodeAtPos(e.clientX, e.clientY);
    if (node) {
      selectedNode = node;
      updateInfoCard(node);
      draw();
    }
  });

  window.addEventListener('resize', resizeCanvas);
  resizeCanvas();
  updateInfoCard(selectedNode);
}

// 9. Initialize Application
document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  initCopyButtons();
  initTabs();
  initRepoFilters();
  initPackageImageShowcase();
  initBucklingCalculator();
  initArchitectureCanvas();
});
