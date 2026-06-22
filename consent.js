/* Google Analytics with cookie consent (Consent Mode v2).
   GA is loaded but analytics storage stays denied until the visitor
   accepts. Choice is remembered in localStorage. No framework. */
(function () {
  var GA_ID = 'G-ZWJG6VE6V2';
  var KEY = 'ga-consent';

  window.dataLayer = window.dataLayer || [];
  function gtag() { dataLayer.push(arguments); }
  window.gtag = gtag;

  // Default everything to denied until the visitor chooses.
  gtag('consent', 'default', {
    ad_storage: 'denied',
    ad_user_data: 'denied',
    ad_personalization: 'denied',
    analytics_storage: 'denied',
    wait_for_update: 500
  });

  // Load the GA library. It honours the consent state above.
  var s = document.createElement('script');
  s.async = true;
  s.src = 'https://www.googletagmanager.com/gtag/js?id=' + GA_ID;
  document.head.appendChild(s);

  gtag('js', new Date());
  gtag('config', GA_ID);

  var stored = null;
  try { stored = localStorage.getItem(KEY); } catch (e) {}

  if (stored === 'granted') {
    gtag('consent', 'update', { analytics_storage: 'granted' });
  }
  if (stored === 'granted' || stored === 'denied') {
    return; // already chosen; no banner
  }

  var css =
    '.cc-banner{position:fixed;left:1rem;right:1rem;bottom:1rem;z-index:9999;' +
    'max-width:680px;margin:0 auto;background:#1f2937;color:#f5f5f5;' +
    'border:1px solid #374151;border-radius:8px;padding:1rem 1.25rem;display:flex;' +
    'gap:1rem;align-items:center;flex-wrap:wrap;box-shadow:0 6px 24px rgba(0,0,0,.28);' +
    "font-family:-apple-system,BlinkMacSystemFont,'Inter',sans-serif;font-size:.9rem;line-height:1.5}" +
    '.cc-text{margin:0;flex:1 1 260px}' +
    '.cc-banner a{color:#8fbac4}' +
    '.cc-actions{display:flex;gap:.5rem;flex:0 0 auto}' +
    '.cc-btn{cursor:pointer;border-radius:6px;border:1px solid #4b5563;' +
    'padding:.5rem 1.1rem;font-size:.85rem;font-weight:600;font-family:inherit}' +
    '.cc-accept{background:#8fbac4;color:#10242a;border-color:#8fbac4}' +
    '.cc-reject{background:transparent;color:#f5f5f5}' +
    '.cc-btn:focus-visible{outline:2px solid #8fbac4;outline-offset:2px}' +
    '@media (max-width:480px){.cc-actions{flex:1 1 100%}.cc-btn{flex:1}}';
  var style = document.createElement('style');
  style.textContent = css;
  document.head.appendChild(style);

  function showBanner() {
    var bar = document.createElement('div');
    bar.className = 'cc-banner';
    bar.setAttribute('role', 'dialog');
    bar.setAttribute('aria-live', 'polite');
    bar.setAttribute('aria-label', 'Cookie choice');
    bar.innerHTML =
      '<p class="cc-text">This site uses Google Analytics cookies to understand how it is used. ' +
      'We only set them if you agree. See our <a href="/privacy.html">privacy notice</a>.</p>' +
      '<div class="cc-actions">' +
      '<button type="button" class="cc-btn cc-accept">Accept</button>' +
      '<button type="button" class="cc-btn cc-reject">Reject</button>' +
      '</div>';
    document.body.appendChild(bar);

    bar.querySelector('.cc-accept').addEventListener('click', function () {
      try { localStorage.setItem(KEY, 'granted'); } catch (e) {}
      gtag('consent', 'update', { analytics_storage: 'granted' });
      bar.remove();
    });
    bar.querySelector('.cc-reject').addEventListener('click', function () {
      try { localStorage.setItem(KEY, 'denied'); } catch (e) {}
      bar.remove();
    });
  }

  if (document.body) { showBanner(); }
  else { document.addEventListener('DOMContentLoaded', showBanner); }
})();
