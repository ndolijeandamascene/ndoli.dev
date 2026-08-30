/**
 * Anti-flicker Theme Controller for ndoli.dev
 * Dark Mode is the primary default theme.
 */
(function () {
  const THEME_STORAGE_KEY = 'ndoli_theme';

  function getPreferredTheme() {
    const stored = localStorage.getItem(THEME_STORAGE_KEY);
    if (stored === 'dark' || stored === 'light') {
      return stored;
    }
    // Default to Dark Mode for all visitors
    return 'dark';
  }

  function applyTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    const toggleBtn = document.getElementById('theme-toggle-btn');
    if (toggleBtn) {
      toggleBtn.setAttribute('aria-label', `Switch to ${theme === 'dark' ? 'light' : 'dark'} mode`);
      const iconSpan = toggleBtn.querySelector('.theme-icon');
      if (iconSpan) {
        iconSpan.textContent = theme === 'dark' ? '☀️' : '🌙';
      }
    }
  }

  // Apply immediately before page rendering to prevent theme flicker
  const currentTheme = getPreferredTheme();
  applyTheme(currentTheme);

  // Global toggle function
  window.toggleTheme = function () {
    const current = document.documentElement.getAttribute('data-theme') || 'dark';
    const next = current === 'dark' ? 'light' : 'dark';
    localStorage.setItem(THEME_STORAGE_KEY, next);
    applyTheme(next);
  };

  // Re-apply icon state when DOM loads
  document.addEventListener('DOMContentLoaded', () => {
    applyTheme(document.documentElement.getAttribute('data-theme') || 'dark');
  });
})();
