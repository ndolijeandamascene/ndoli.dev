/**
 * Main Client Script for ndoli.dev
 */

// ==========================================================================
// 1. RECRUITER FAST-TRACK DRAWER CONTROLLER
// ==========================================================================
window.openRecruiterDrawer = function () {
  const drawer = document.getElementById('recruiter-drawer');
  const backdrop = document.getElementById('recruiter-drawer-backdrop');
  if (drawer && backdrop) {
    drawer.classList.add('open');
    backdrop.classList.add('open');
    drawer.setAttribute('aria-hidden', 'false');
    backdrop.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';
  }
};

window.closeRecruiterDrawer = function () {
  const drawer = document.getElementById('recruiter-drawer');
  const backdrop = document.getElementById('recruiter-drawer-backdrop');
  if (drawer && backdrop) {
    drawer.classList.remove('open');
    backdrop.classList.remove('open');
    drawer.setAttribute('aria-hidden', 'true');
    backdrop.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
  }
};

// ==========================================================================
// 2. TOAST NOTIFICATION UTILITY
// ==========================================================================
window.showToast = function (message) {
  const container = document.getElementById('toast-container');
  if (!container) return;

  const toast = document.createElement('div');
  toast.className = 'toast-message';
  toast.innerHTML = `<svg width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M5 13l4 4L19 7"/></svg> <span>${message}</span>`;
  container.appendChild(toast);

  setTimeout(() => {
    toast.style.transition = 'opacity 0.3s, transform 0.3s';
    toast.style.opacity = '0';
    toast.style.transform = 'translateY(10px)';
    setTimeout(() => toast.remove(), 300);
  }, 3500);
};

window.copyEmailToClipboard = async function (email) {
  try {
    await navigator.clipboard.writeText(email);
    window.showToast(`Copied ${email} to clipboard!`);
  } catch (err) {
    window.showToast(`Email: ${email}`);
  }
};

// ==========================================================================
// 3. INTERACTIVE PROJECT SCOPE ESTIMATOR
// ==========================================================================
window.updateEstimator = function () {
  const estimator = document.getElementById('project-estimator');
  if (!estimator) return;

  const selectedType = estimator.querySelector('input[name="est_type"]:checked');
  const selectedAddons = estimator.querySelectorAll('input[name="est_addon"]:checked');
  const selectedPace = estimator.querySelector('input[name="est_pace"]:checked');

  let baseWeeks = selectedType ? parseFloat(selectedType.getAttribute('data-weeks') || 3) : 3;
  let typeName = selectedType ? selectedType.getAttribute('data-type-name') : 'Custom Software Solution';
  let typeVal = selectedType ? selectedType.value : 'software_dev';

  let addonWeeks = 0;
  let addonNames = [];
  selectedAddons.forEach((addon) => {
    addonWeeks += parseFloat(addon.getAttribute('data-weeks') || 0);
    addonNames.push(addon.getAttribute('data-name'));
  });

  const paceMultiplier = selectedPace ? parseFloat(selectedPace.value || 1.0) : 1.0;
  let totalWeeks = Math.max(1, Math.round((baseWeeks + addonWeeks) * paceMultiplier * 10) / 10);
  
  const weeksDisplay = document.getElementById('est-total-weeks');
  const stackTags = document.getElementById('est-stack-tags');
  const deliverablesList = document.getElementById('est-deliverables-list');
  const submitBtn = document.getElementById('est-submit-btn');

  let weeksStr = totalWeeks <= 1.5 ? '1 - 2 Weeks' : `${Math.floor(totalWeeks)} - ${Math.ceil(totalWeeks + 1)} Weeks`;
  if (weeksDisplay) weeksDisplay.textContent = weeksStr;

  // Recommended Stack & Deliverables by Type
  let tags = [];
  let deliverables = [];

  if (typeVal === 'systems_admin') {
    tags = ['Linux (Debian/Ubuntu)', 'Windows Server', 'Docker', 'Networking & VPN', 'Backup Scripts'];
    deliverables = [
      'Production server provisioning & OS hardening',
      'Enterprise network setup (DNS, TCP/IP, Firewall)',
      'Automated daily backup & disaster recovery schedule',
      'Documentation & Tier 2 support handover checklist'
    ];
  } else if (typeVal === 'django_app') {
    tags = ['Django 5.0+', 'Python', 'PostgreSQL', 'HTML5 / CSS3', 'REST APIs'];
    deliverables = [
      'Clean domain modeling & database schema architecture',
      'Authentication, RBAC & custom admin control panel',
      'Responsive user interface & core business workflows',
      'Dockerized deployment checklist on cloud VPS'
    ];
  } else if (typeVal === 'ai_rag') {
    tags = ['PostgreSQL + pgvector', 'RAG Pipeline', 'LLM Orchestration', 'Django / Python', 'Document Ingestion'];
    deliverables = [
      'Document parsing, semantic chunking & vector indexing',
      'Top-K cosine similarity retrieval pipeline in PostgreSQL',
      'Strict grounding & citation verification engine',
      'Private API integration with local or cloud LLMs'
    ];
  } else {
    tags = ['Security Hardening', 'SSL / TLS', 'UFW / Firewalls', 'Fail2ban', 'Nginx Reverse Proxy'];
    deliverables = [
      'Vulnerability audit & endpoint configuration review',
      'Automated SSL/TLS certificate management',
      'SSH key authentication & brute-force mitigation',
      'Security audit report & remediation verification'
    ];
  }

  if (stackTags) {
    stackTags.innerHTML = tags.map((t) => `<span>${t}</span>`).join('');
  }

  if (deliverablesList) {
    deliverablesList.innerHTML = deliverables.map((d) => `<li>${d}</li>`).join('');
  }

  if (submitBtn) {
    let categoryParam = 'software_dev';
    if (typeVal === 'systems_admin') categoryParam = 'it_operations';
    else if (typeVal === 'ai_rag') categoryParam = 'ai_rag';
    else if (typeVal === 'security_audit') categoryParam = 'network_security';

    const descText = `Estimated Project: ${typeName} (~${weeksStr}). Add-ons: ${addonNames.join(', ') || 'Standard'}.`;
    submitBtn.href = `/hire/?category=${categoryParam}&role=${encodeURIComponent(typeName)}&desc=${encodeURIComponent(descText)}`;
  }
};

// ==========================================================================
// 4. ARCHITECTURE EXPLORER TABS (CASE STUDIES)
// ==========================================================================
window.switchArchTab = function (tabId, btn) {
  const container = btn.closest('.arch-explorer-card');
  if (!container) return;

  const buttons = container.querySelectorAll('.arch-tab-btn');
  const panels = container.querySelectorAll('.arch-tab-panel');

  buttons.forEach((b) => b.classList.remove('active'));
  btn.classList.add('active');

  panels.forEach((p) => {
    if (p.id === `arch-tab-${tabId}`) {
      p.style.display = 'block';
      p.classList.add('active');
    } else {
      p.style.display = 'none';
      p.classList.remove('active');
    }
  });
};

// ==========================================================================
// 5. INTERACTIVE SKILL EVIDENCE MODAL
// ==========================================================================
const SKILL_EVIDENCE_MAP = {
  'Django': {
    category: 'Backend Framework',
    level: 'Core Expertise (Advanced)',
    tenure: '3+ Years Production',
    desc: 'Architected multiple scalable web systems with complex relational schemas, authentication, custom administration dashboards, and REST APIs.',
    projects: ['IHKIP Health Knowledge Platform', 'Enterprise Hospital System', 'Tourism & Hotel Booking Platform']
  },
  'Python': {
    category: 'Programming Language',
    level: 'Primary Language',
    tenure: '4+ Years Active Use',
    desc: 'Built backend pipelines, automation scripts, data chunking utilities for RAG vector search, and web server backends.',
    projects: ['IHKIP Platform', 'Django Web Applications', 'Automation & IT Scripts']
  },
  'PostgreSQL': {
    category: 'Database & Storage',
    level: 'Production Database',
    tenure: '3+ Years Active Use',
    desc: 'Managed high-availability PostgreSQL databases, multi-table indexing, automated backup scripts, and high-dimensional vector embeddings with pgvector.',
    projects: ['IHKIP Vector Search', 'Enterprise Business Systems', 'ndoli.dev Core Platform']
  },
  'pgvector': {
    category: 'Vector & AI Search',
    level: 'Specialized Architecture',
    tenure: '2+ Years Production',
    desc: 'Implemented high-dimensional semantic search and cosine distance matching for local medical RAG pipelines with sub-second retrieval SLAs.',
    projects: ['IHKIP — Intelligent Health Knowledge Platform']
  },
  'Linux & Windows Server': {
    category: 'Systems & Infrastructure',
    level: 'Core Systems Administration',
    tenure: '3+ Years Production',
    desc: 'Provisioned and administered Debian/Ubuntu Linux and Windows Server environments, managing user permissions, firewalls, and 24/7 uptime monitoring.',
    projects: ['GIRA LTD Infrastructure', 'Cloud VPS Hosting', 'ndoli.dev Production Host']
  },
  'Docker': {
    category: 'Infrastructure & DevOps',
    level: 'Containerization Standard',
    tenure: '2+ Years Production',
    desc: 'Containerized multi-service applications (Web + Database + WhiteNoise + Gunicorn) ensuring seamless local-to-production parity and zero deployment drift.',
    projects: ['ndoli.dev Platform', 'Enterprise Services Stack']
  },
  'Networking (TCP/IP, DNS)': {
    category: 'Security & Networking',
    level: 'Enterprise Networking',
    tenure: '3+ Years Enterprise',
    desc: 'Configured corporate network topologies, DNS routing, subnetting, VPN access, and reverse proxies with strict SSL/TLS certificates.',
    projects: ['GIRA LTD Corporate Network', 'AfriRegister Domain Management']
  }
};

window.openSkillEvidence = function (el) {
  const skillName = el.getAttribute('data-skill-name') || el.innerText.trim();
  const data = SKILL_EVIDENCE_MAP[skillName] || {
    category: el.getAttribute('data-category') || 'Technology Specialization',
    level: 'Verified Technical Skill',
    tenure: '3+ Years Experience',
    desc: `Applied in production systems, enterprise infrastructure, and full-stack software development at ndoli.dev and client organizations.`,
    projects: ['IHKIP Platform', 'Enterprise IT Operations', 'ndoli.dev']
  };

  const modal = document.getElementById('skill-evidence-modal');
  const backdrop = document.getElementById('skill-evidence-backdrop');
  if (!modal || !backdrop) return;

  document.getElementById('skill-modal-title').textContent = skillName;
  document.getElementById('skill-modal-category').textContent = data.category;
  document.getElementById('skill-modal-level').textContent = data.level;
  document.getElementById('skill-modal-tenure').textContent = data.tenure;
  document.getElementById('skill-modal-description').textContent = data.desc;

  const projContainer = document.getElementById('skill-modal-projects');
  projContainer.innerHTML = data.projects.map((p) => `<span class="modal-project-pill">${p}</span>`).join('');

  modal.classList.add('open');
  backdrop.classList.add('open');
  modal.setAttribute('aria-hidden', 'false');
  backdrop.setAttribute('aria-hidden', 'false');
};

window.closeSkillEvidenceModal = function () {
  const modal = document.getElementById('skill-evidence-modal');
  const backdrop = document.getElementById('skill-evidence-backdrop');
  if (modal && backdrop) {
    modal.classList.remove('open');
    backdrop.classList.remove('open');
    modal.setAttribute('aria-hidden', 'true');
    backdrop.setAttribute('aria-hidden', 'true');
  }
};

// ==========================================================================
// 6. MOBILE NAVIGATION DRAWER CONTROLLER
// ==========================================================================
window.toggleMobileNav = function (e) {
  if (e) {
    e.preventDefault();
    e.stopPropagation();
  }
  const drawer = document.getElementById('mobile-nav-drawer');
  const btn = document.getElementById('mobile-menu-btn');
  if (drawer) {
    const isOpen = drawer.classList.toggle('open');
    if (btn) btn.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    document.body.style.overflow = isOpen ? 'hidden' : '';
  }
};

window.closeMobileNav = function () {
  const drawer = document.getElementById('mobile-nav-drawer');
  const btn = document.getElementById('mobile-menu-btn');
  if (drawer && drawer.classList.contains('open')) {
    drawer.classList.remove('open');
    if (btn) btn.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = '';
  }
};

// ==========================================================================
// 7. DOM READY INITIALIZATIONS
// ==========================================================================
document.addEventListener('DOMContentLoaded', () => {
  const mobileDrawer = document.getElementById('mobile-nav-drawer');
  if (mobileDrawer) {
    // Auto-close on link tap
    mobileDrawer.querySelectorAll('.mobile-drawer-link').forEach((link) => {
      link.addEventListener('click', () => {
        window.closeMobileNav();
      });
    });

    // Close on click outside
    document.addEventListener('click', (e) => {
      const btn = document.getElementById('mobile-menu-btn');
      if (mobileDrawer.classList.contains('open') && !mobileDrawer.contains(e.target) && (!btn || !btn.contains(e.target))) {
        window.closeMobileNav();
      }
    });
  }

  // Global ESC Key Listener
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      window.closeRecruiterDrawer();
      window.closeSkillEvidenceModal();
      window.closeMobileNav();
    }
  });

  // Copy Code in Pre Blocks
  const codeBlocks = document.querySelectorAll('pre');
  codeBlocks.forEach((pre) => {
    if (pre.closest('.arch-explorer-card')) return; // Skip diagram blocks
    const copyBtn = document.createElement('button');
    copyBtn.className = 'btn btn-outline btn-sm no-print';
    copyBtn.style.cssText = 'position: absolute; top: 8px; right: 8px; font-size: 11px; padding: 2px 6px;';
    copyBtn.textContent = 'Copy';
    copyBtn.setAttribute('aria-label', 'Copy code to clipboard');

    pre.style.position = 'relative';
    pre.appendChild(copyBtn);

    copyBtn.addEventListener('click', async () => {
      const code = pre.querySelector('code')?.innerText || pre.innerText;
      try {
        await navigator.clipboard.writeText(code);
        copyBtn.textContent = 'Copied!';
        setTimeout(() => {
          copyBtn.textContent = 'Copy';
        }, 2000);
      } catch (err) {
        copyBtn.textContent = 'Failed';
      }
    });
  });

  // Initialize Estimator if present
  if (document.getElementById('project-estimator')) {
    window.updateEstimator();
  }

  // Auto-fill hire form fields if query params present
  const urlParams = new URLSearchParams(window.location.search);
  const catParam = urlParams.get('category');
  const roleParam = urlParams.get('role');
  const descParam = urlParams.get('desc');

  if (catParam) {
    const catSelect = document.getElementById('id_job_category');
    if (catSelect) catSelect.value = catParam;
  }
  if (roleParam) {
    const roleInput = document.getElementById('id_job_title');
    if (roleInput && !roleInput.value) roleInput.value = roleParam;
  }
  if (descParam) {
    const descTextarea = document.getElementById('id_job_description');
    if (descTextarea && !descTextarea.value) descTextarea.value = descParam;
  }
});

// ==========================================================================
// 8. FLOATING WHATSAPP CHAT WIDGET CONTROLLER
// ==========================================================================
window.dismissWhatsAppTooltip = function (e) {
  if (e) {
    e.preventDefault();
    e.stopPropagation();
  }
  const tooltip = document.getElementById('whatsapp-tooltip');
  if (tooltip) {
    tooltip.style.transition = 'opacity 0.25s, transform 0.25s';
    tooltip.style.opacity = '0';
    tooltip.style.transform = 'translateY(8px)';
    setTimeout(() => {
      tooltip.style.display = 'none';
    }, 250);
  }
};
