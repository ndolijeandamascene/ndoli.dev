/**
 * Main Client Script for ndoli.dev
 */
document.addEventListener('DOMContentLoaded', () => {
  // --- Mobile Navigation Drawer ---
  const mobileMenuBtn = document.getElementById('mobile-menu-btn');
  const mobileDrawer = document.getElementById('mobile-nav-drawer');

  if (mobileMenuBtn && mobileDrawer) {
    mobileMenuBtn.addEventListener('click', () => {
      const isOpen = mobileDrawer.classList.toggle('open');
      mobileMenuBtn.setAttribute('aria-expanded', isOpen.toString());
    });

    // Close drawer on ESC key
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && mobileDrawer.classList.contains('open')) {
        mobileDrawer.classList.remove('open');
        mobileMenuBtn.setAttribute('aria-expanded', 'false');
        mobileMenuBtn.focus();
      }
    });
  }

  // --- Copy Code to Clipboard ---
  const codeBlocks = document.querySelectorAll('pre');
  codeBlocks.forEach((pre) => {
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
});
