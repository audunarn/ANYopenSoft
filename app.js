/**
 * ANYopenSoft - Interactive Web Application Logic
 * Architecture Node Visualizer, Live DNV-RP-C201 Buckling Calculator, Repo Search/Filter
 */

document.addEventListener('DOMContentLoaded', () => {
  initThemeToggle();
  initCopyButtons();
  initQuickStartTabs();
  initRepoFilter();
  initBucklingCalculator();
  initArchitectureCanvas();
});

/* ==========================================================================
   1. Theme Toggle (Dark / Light)
   ========================================================================== */
function initThemeToggle() {
  const toggleBtn = document.getElementById('theme-toggle');
  const htmlEl = document.documentElement;

  // Saved theme preference or dark default
  const savedTheme = localStorage.getItem('anyopensoft_theme') || 'dark';
  htmlEl.className = savedTheme;

  toggleBtn.addEventListener('click', () => {
    const isDark = htmlEl.classList.contains('dark');
    const newTheme = isDark ? 'light' : 'dark';
    htmlEl.className = newTheme;
    localStorage.setItem('anyopensoft_theme', newTheme);
  });
}

/* ==========================================================================
   2. Copy to Clipboard & Toast Notifications
   ========================================================================== */
function initCopyButtons() {
  const toast = document.getElementById('toast');

  document.querySelectorAll('.copy-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const textToCopy = btn.getAttribute('data-copy');
      if (!textToCopy) return;

      navigator.clipboard.writeText(textToCopy).then(() => {
        showToast('Copied to clipboard!');
      }).catch(() => {
        showToast('Failed to copy');
      });
    });
  });

  function showToast(msg) {
    toast.textContent = msg;
    toast.classList.add('show');
    setTimeout(() => {
      toast.classList.remove('show');
    }, 2200);
  }
}

/* ==========================================================================
   3. Quick Start Code Tabs
   ========================================================================== */
function initQuickStartTabs() {
  const tabBtns = document.querySelectorAll('.tab-btn');
  const tabContents = document.querySelectorAll('.tab-content');

  tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const targetId = btn.getAttribute('data-tab');

      tabBtns.forEach(b => b.classList.remove('active'));
      tabContents.forEach(c => c.classList.remove('active'));

      btn.classList.add('active');
      document.getElementById(targetId).classList.add('active');
    });
  });
}

/* ==========================================================================
   4. Repository Grid Search & Filtering
   ========================================================================== */
function initRepoFilter() {
  const searchInput = document.getElementById('repo-search');
  const filterTabs = document.querySelectorAll('.filter-tab');
  const repoCards = document.querySelectorAll('.repo-card');

  let currentFilter = 'all';
  let searchQuery = '';

  filterTabs.forEach(tab => {
    tab.addEventListener('click', () => {
      filterTabs.forEach(t => t.classList.remove('active'));
      tab.classList.add('active');
      currentFilter = tab.getAttribute('data-filter');
      applyFilters();
    });
  });

  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      searchQuery = e.target.value.toLowerCase().trim();
      applyFilters();
    });
  }

  function applyFilters() {
    repoCards.forEach(card => {
      const category = card.getAttribute('data-category');
      const keywords = card.getAttribute('data-keywords').toLowerCase();
      const title = card.querySelector('.repo-title').textContent.toLowerCase();

      const matchesFilter = currentFilter === 'all' || category === currentFilter;
      const matchesSearch = !searchQuery || title.includes(searchQuery) || keywords.includes(searchQuery);

      if (matchesFilter && matchesSearch) {
        card.style.display = 'flex';
      } else {
        card.style.display = 'none';
      }
    });
  }
}

/* ==========================================================================
   5. Interactive Live DNV-RP-C201 Plate Buckling Calculator
   ========================================================================== */
function initBucklingCalculator() {
  const spanInput = document.getElementById('input-span');
  const spacingInput = document.getElementById('input-spacing');
  const thickInput = document.getElementById('input-thick');
  const yieldInput = document.getElementById('input-yield');
  const sigxInput = document.getElementById('input-sigx');
  const sigyInput = document.getElementById('input-sigy');
  const tauInput = document.getElementById('input-tau');

  const valSpan = document.getElementById('val-span');
  const valSpacing = document.getElementById('val-spacing');
  const valThick = document.getElementById('val-thick');

  const resSigmaE = document.getElementById('res-sigma-e');
  const resLambda = document.getElementById('res-lambda');
  const resSigmaCr = document.getElementById('res-sigma-cr');
  const resSigmaVm = document.getElementById('res-sigma-vm');
  const ufValue = document.getElementById('uf-value');
  const gaugeCircle = document.getElementById('gauge-circle');
  const statusPill = document.getElementById('status-pill');

  if (!spanInput) return;

  const inputs = [spanInput, spacingInput, thickInput, yieldInput, sigxInput, sigyInput, tauInput];
  inputs.forEach(input => input.addEventListener('input', calculateBuckling));

  function calculateBuckling() {
    const span = parseFloat(spanInput.value); // L (mm)
    const spacing = parseFloat(spacingInput.value); // s (mm)
    const thick = parseFloat(thickInput.value); // t (mm)
    const fy = parseFloat(yieldInput.value); // fy (MPa)
    const sigx = parseFloat(sigxInput.value) || 0; // MPa
    const sigy = parseFloat(sigyInput.value) || 0; // MPa
    const tau = parseFloat(tauInput.value) || 0; // MPa

    // Update range labels
    valSpan.textContent = `${span} mm`;
    valSpacing.textContent = `${spacing} mm`;
    valThick.textContent = `${thick} mm`;

    // Engineering Constants
    const E = 210000; // Elastic Modulus (MPa)
    const nu = 0.3; // Poisson's Ratio

    // 1. Elastic Ideal Buckling Stress for unstiffened plate field (DNV-RP-C201)
    // sigma_Ee = (pi^2 * E / (12 * (1 - nu^2))) * (t / s)^2
    const factor = (Math.PI * Math.PI * E) / (12 * (1 - nu * nu));
    const sigmaEe = factor * Math.pow(thick / spacing, 2);

    // 2. Reduced Slenderness lambda_p
    const lambdaP = Math.sqrt(fy / sigmaEe);

    // 3. Reduction factor kappa
    let kappa = 1.0;
    if (lambdaP > 0.673) {
      kappa = (lambdaP - 0.22) / (lambdaP * lambdaP);
    }
    kappa = Math.min(1.0, Math.max(0.05, kappa));

    // 4. Critical Buckling Stress sigma_cr
    const sigmaCr = kappa * fy;

    // 5. Von Mises Equivalent Stress
    const sigmaVm = Math.sqrt(sigx * sigx + sigy * sigy - sigx * sigy + 3 * tau * tau);

    // 6. Buckling Usage Factor (UF)
    const uf = sigmaVm / sigmaCr;

    // Render Results
    resSigmaE.textContent = `${sigmaEe.toFixed(1)} MPa`;
    resLambda.textContent = lambdaP.toFixed(3);
    resSigmaCr.textContent = `${sigmaCr.toFixed(1)} MPa`;
    resSigmaVm.textContent = `${sigmaVm.toFixed(1)} MPa`;
    ufValue.textContent = uf.toFixed(2);

    // Update Gauge Visual & Status
    const angle = Math.min(360, Math.max(0, uf * 360));
    let statusText = 'SAFE CAPACITY';
    let statusClass = 'status-pill';
    let colorHex = '#06b6d4';

    if (uf > 1.0) {
      statusText = 'OVER-UTILIZED (EXCEEDED)';
      statusClass = 'status-pill status-danger';
      colorHex = '#f43f5e';
    } else if (uf > 0.85) {
      statusText = 'HIGH CAPACITY UTILIZATION';
      statusClass = 'status-pill status-warning';
      colorHex = '#f59e0b';
    }

    statusPill.className = statusClass;
    statusPill.textContent = statusText;
    gaugeCircle.style.background = `conic-gradient(${colorHex} 0deg ${angle}deg, rgba(255, 255, 255, 0.08) ${angle}deg 360deg)`;
  }

  // Run initial calculation
  calculateBuckling();
}

/* ==========================================================================
   6. Interactive Architecture Canvas Visualizer
   ========================================================================== */
function initArchitectureCanvas() {
  const canvas = document.getElementById('arch-canvas');
  const tooltip = document.getElementById('node-tooltip');
  const infoTitle = document.getElementById('info-title');
  const infoDesc = document.getElementById('info-desc');
  const infoChips = document.getElementById('info-chips');

  if (!canvas) return;

  const ctx = canvas.getContext('2d');

  // Set crisp pixel resolution
  function resizeCanvas() {
    const rect = canvas.getBoundingClientRect();
    canvas.width = rect.width * window.devicePixelRatio;
    canvas.height = rect.height * window.devicePixelRatio;
    ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
  }

  resizeCanvas();
  window.addEventListener('resize', resizeCanvas);

  // Nodes Definition
  const nodes = [
    {
      id: 'anystructure',
      label: 'ANYstructure',
      type: 'main',
      x: 0.5, y: 0.2,
      desc: 'Flagship Desktop Steel-Structure App & FE GUI. Integrates DNV buckling standards, optimization, and FE solvers.',
      tags: ['Desktop App', 'DNV RP-C201/202', 'Tkinter GUI', 'Optimization']
    },
    {
      id: 'anyfem',
      label: 'ANYfem',
      type: 'main',
      x: 0.32, y: 0.48,
      desc: 'Finite Element Analysis (FEA) core framework providing element stiffness matrices and assembly routines.',
      tags: ['FE Engine', 'Stiffness Assembly', 'Plate/Beam Elements']
    },
    {
      id: 'anysolver',
      label: 'ANYsolver',
      type: 'main',
      x: 0.68, y: 0.48,
      desc: 'FE Solver runtime. Handles arc-length static, follower pressure, non-linear prestress, and buckling recovery.',
      tags: ['FE Solver', 'Arc-Length', 'Follower Pressure', 'Kinematics']
    },
    {
      id: 'anytimeseries',
      label: 'ANYtimeseries',
      type: 'standalone',
      x: 0.86, y: 0.2,
      desc: 'Main Standalone App for marine & offshore environmental load time-series analysis, wave & wind histories.',
      tags: ['Standalone App', 'Hydrodynamics', 'Wave/Wind Time-Series']
    },
    {
      id: 'anybuckling',
      label: 'ANYbuckling',
      type: 'sub',
      x: 0.15, y: 0.78,
      desc: 'Standalone prescriptive (DNV-RP-C201/C202) and PULS semi-analytical panel & shell buckling engine.',
      tags: ['Buckling Engine', 'DNV RP-C201', 'DNV RP-C202', 'PULS']
    },
    {
      id: 'anygeometry',
      label: 'ANYgeometry',
      type: 'sub',
      x: 0.35, y: 0.78,
      desc: 'Shared neutral surface geometry authority and parametric 3D CAD generators.',
      tags: ['Geometry Authority', 'Parametric CAD', 'Surface Models']
    },
    {
      id: 'anymaterial',
      label: 'ANYmaterial',
      type: 'sub',
      x: 0.53, y: 0.78,
      desc: 'Material property authority, DNV material factors, and orthotropic stress-strain definitions.',
      tags: ['Material Database', 'DNV Steel Specs', 'Orthotropic']
    },
    {
      id: 'anymesh',
      label: 'ANYmesh',
      type: 'sub',
      x: 0.70, y: 0.78,
      desc: '2D/3D FE mesh generation, quad/tri element mesher, and preview controls.',
      tags: ['Mesh Generator', 'Quad/Tri Meshes', 'FE Controls']
    },
    {
      id: 'anyio',
      label: 'ANYio',
      type: 'sub',
      x: 0.87, y: 0.78,
      desc: 'Neutral file I/O, IFC 3D product conversion, and format exchange inspectors.',
      tags: ['IFC 3D Export', 'File I/O', 'CAD Exchange']
    }
  ];

  // Connections (Source -> Target)
  const connections = [
    { from: 'anystructure', to: 'anyfem' },
    { from: 'anystructure', to: 'anysolver' },
    { from: 'anystructure', to: 'anybuckling' },
    { from: 'anystructure', to: 'anygeometry' },
    { from: 'anystructure', to: 'anymaterial' },
    { from: 'anystructure', to: 'anymesh' },
    { from: 'anystructure', to: 'anyio' },
    { from: 'anyfem', to: 'anysolver' },
    { from: 'anygeometry', to: 'anymesh' },
    { from: 'anymesh', to: 'anysolver' }
  ];

  // Animated particle pulses flowing along connections
  const particles = connections.map((conn, idx) => ({
    conn,
    progress: (idx * 0.25) % 1.0,
    speed: 0.006 + (idx % 3) * 0.002
  }));

  let hoveredNode = null;

  function getNodePos(node, width, height) {
    return {
      x: node.x * width,
      y: node.y * height
    };
  }

  // Animation Loop
  function draw() {
    const width = canvas.getBoundingClientRect().width;
    const height = canvas.getBoundingClientRect().height;

    ctx.clearRect(0, 0, width, height);

    // 1. Draw Connections
    connections.forEach(conn => {
      const source = nodes.find(n => n.id === conn.from);
      const target = nodes.find(n => n.id === conn.to);
      if (!source || !target) return;

      const p1 = getNodePos(source, width, height);
      const p2 = getNodePos(target, width, height);

      const isConnectedToHover = hoveredNode && (hoveredNode.id === source.id || hoveredNode.id === target.id);

      ctx.beginPath();
      ctx.moveTo(p1.x, p1.y);
      ctx.lineTo(p2.x, p2.y);
      ctx.strokeStyle = isConnectedToHover ? 'rgba(6, 182, 212, 0.8)' : 'rgba(255, 255, 255, 0.12)';
      ctx.lineWidth = isConnectedToHover ? 2.5 : 1.2;
      ctx.stroke();
    });

    // 2. Draw Moving Particles
    particles.forEach(p => {
      p.progress += p.speed;
      if (p.progress > 1.0) p.progress = 0.0;

      const source = nodes.find(n => n.id === p.conn.from);
      const target = nodes.find(n => n.id === p.conn.to);
      if (!source || !target) return;

      const p1 = getNodePos(source, width, height);
      const p2 = getNodePos(target, width, height);

      const px = p1.x + (p2.x - p1.x) * p.progress;
      const py = p1.y + (p2.y - p1.y) * p.progress;

      ctx.beginPath();
      ctx.arc(px, py, 3, 0, Math.PI * 2);
      ctx.fillStyle = '#06b6d4';
      ctx.shadowColor = '#06b6d4';
      ctx.shadowBlur = 8;
      ctx.fill();
      ctx.shadowBlur = 0;
    });

    // 3. Draw Nodes
    nodes.forEach(node => {
      const pos = getNodePos(node, width, height);
      const isHovered = hoveredNode && hoveredNode.id === node.id;
      const radius = node.type === 'main' ? 24 : node.type === 'standalone' ? 22 : 18;

      // Glow aura for main/hovered nodes
      ctx.beginPath();
      ctx.arc(pos.x, pos.y, radius + (isHovered ? 8 : 4), 0, Math.PI * 2);
      if (node.type === 'main') {
        ctx.fillStyle = isHovered ? 'rgba(6, 182, 212, 0.35)' : 'rgba(6, 182, 212, 0.15)';
      } else if (node.type === 'standalone') {
        ctx.fillStyle = isHovered ? 'rgba(16, 185, 129, 0.35)' : 'rgba(16, 185, 129, 0.15)';
      } else {
        ctx.fillStyle = isHovered ? 'rgba(139, 92, 246, 0.35)' : 'rgba(139, 92, 246, 0.15)';
      }
      ctx.fill();

      // Node Body Circle
      ctx.beginPath();
      ctx.arc(pos.x, pos.y, radius, 0, Math.PI * 2);
      if (node.type === 'main') {
        ctx.fillStyle = '#06b6d4';
      } else if (node.type === 'standalone') {
        ctx.fillStyle = '#10b981';
      } else {
        ctx.fillStyle = '#8b5cf6';
      }
      ctx.fill();
      ctx.lineWidth = 2;
      ctx.strokeStyle = '#ffffff';
      ctx.stroke();

      // Node Label
      ctx.font = node.type === 'main' ? 'bold 13px Outfit, sans-serif' : '12px Outfit, sans-serif';
      ctx.fillStyle = '#f8fafc';
      ctx.textAlign = 'center';
      ctx.fillText(node.label, pos.x, pos.y + radius + 18);
    });

    requestAnimationFrame(draw);
  }

  requestAnimationFrame(draw);

  // Mouse Move Interaction
  canvas.addEventListener('mousemove', (e) => {
    const rect = canvas.getBoundingClientRect();
    const mx = e.clientX - rect.left;
    const my = e.clientY - rect.top;
    const width = rect.width;
    const height = rect.height;

    let found = null;

    nodes.forEach(node => {
      const pos = getNodePos(node, width, height);
      const radius = node.type === 'main' ? 24 : node.type === 'standalone' ? 22 : 18;
      const dist = Math.hypot(mx - pos.x, my - pos.y);

      if (dist <= radius + 10) {
        found = node;
      }
    });

    hoveredNode = found;

    if (found) {
      canvas.style.cursor = 'pointer';
      tooltip.style.display = 'block';
      tooltip.style.left = `${mx + 15}px`;
      tooltip.style.top = `${my - 15}px`;
      tooltip.innerHTML = `<strong>${found.label}</strong><br><span style="color:#94a3b8">${found.tags[0]}</span>`;

      // Update Info Card
      infoTitle.textContent = found.label;
      infoDesc.textContent = found.desc;
      infoChips.innerHTML = found.tags.map(t => `<span class="chip">${t}</span>`).join(' ');
    } else {
      canvas.style.cursor = 'default';
      tooltip.style.display = 'none';
    }
  });
}
