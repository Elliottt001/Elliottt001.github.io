/* Open every navigable site link in a separate tab, except page-local anchors. */
(() => {
  const openLinksInNewTabs = () => {
    document.querySelectorAll('a[href]').forEach((link) => {
      const href = link.getAttribute('href')?.trim();
      if (!href || href.startsWith('#')) return;

      link.setAttribute('target', '_blank');
      const rel = new Set((link.getAttribute('rel') || '').split(/\s+/).filter(Boolean));
      rel.add('noopener');
      rel.add('noreferrer');
      link.setAttribute('rel', [...rel].join(' '));
    });
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', openLinksInNewTabs, { once: true });
  } else {
    openLinksInNewTabs();
  }
})();
