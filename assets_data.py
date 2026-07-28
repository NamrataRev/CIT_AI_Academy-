# -*- coding: utf-8 -*-
"""Branding + UI assets (CSS / JS / SVG) for the generated site."""

# Revature wordmark. Muted, professional. Orange wordmark + navy dot mark.
LOGO_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 40" role="img" aria-label="Revature">
  <g fill="#d9772e" font-family="Inter, Segoe UI, Arial, sans-serif" font-weight="700">
    <text x="0" y="29" font-size="30" letter-spacing="-0.5">revature</text>
  </g>
  <circle cx="205" cy="10" r="4" fill="#1b2a41"/>
</svg>
"""

FAVICON_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">
  <rect width="32" height="32" rx="7" fill="#1b2a41"/>
  <text x="16" y="22" font-family="Inter, Arial, sans-serif" font-size="17" font-weight="700"
        fill="#d9772e" text-anchor="middle">r</text>
</svg>
"""

STYLE_CSS = r"""
:root{
  --brand-navy:#1b2a41;
  --brand-navy-2:#24384f;
  --accent:#d9772e;          /* muted Revature orange, used sparingly */
  --accent-strong:#c4661e;
  --accent-soft:rgba(217,119,46,.12);

  --bg:#f5f6f8;
  --surface:#ffffff;
  --surface-2:#fafbfc;
  --sidebar-bg:#ffffff;
  --header-bg:#ffffff;
  --text:#1f2a37;
  --text-strong:#12202f;
  --muted:#64748b;
  --border:#e4e8ee;
  --border-strong:#d3dae3;
  --code-bg:#f4f6f8;
  --shadow:0 1px 2px rgba(16,32,52,.04),0 4px 16px rgba(16,32,52,.06);
  --radius:12px;
  --header-h:60px;
  --sidebar-w:302px;
}
:root[data-theme="dark"]{
  --bg:#0e161f;
  --surface:#151f2b;
  --surface-2:#111a24;
  --sidebar-bg:#111a24;
  --header-bg:#0f1822;
  --text:#dbe4ee;
  --text-strong:#f0f5fa;
  --muted:#93a4b6;
  --border:#233242;
  --border-strong:#2c3e50;
  --code-bg:#0f1821;
  --accent:#e08a44;
  --shadow:0 1px 2px rgba(0,0,0,.3),0 6px 20px rgba(0,0,0,.35);
}

*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{
  margin:0;
  font-family:'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Arial,sans-serif;
  background:var(--bg);
  color:var(--text);
  line-height:1.65;
  font-size:16px;
  -webkit-font-smoothing:antialiased;
}
a{color:var(--accent-strong);text-decoration:none}
a:hover{text-decoration:underline}
:root[data-theme="dark"] a{color:var(--accent)}

.skip-link{position:absolute;left:-999px;top:0;background:var(--brand-navy);color:#fff;padding:10px 16px;z-index:200;border-radius:0 0 8px 0}
.skip-link:focus{left:0}

/* ---------- Header ---------- */
.site-header{
  position:sticky;top:0;z-index:100;height:var(--header-h);
  display:flex;align-items:center;gap:14px;
  padding:0 20px;background:var(--header-bg);
  border-bottom:1px solid var(--border);
}
.brand{display:flex;align-items:center;gap:12px;text-decoration:none!important}
.brand-logo{height:26px;width:auto;display:block}
.brand-divider{width:1px;height:24px;background:var(--border-strong)}
.brand-text{color:var(--text);font-size:14px;font-weight:500;letter-spacing:.2px;white-space:nowrap}
.brand-text strong{color:var(--brand-navy);font-weight:700}
:root[data-theme="dark"] .brand-text strong{color:var(--text-strong)}
.theme-toggle{margin-left:auto;background:transparent;border:1px solid var(--border);color:var(--muted);
  width:36px;height:36px;border-radius:9px;display:grid;place-items:center;cursor:pointer;transition:.15s}
.theme-toggle:hover{color:var(--accent);border-color:var(--accent)}
.menu-toggle{display:none;flex-direction:column;gap:4px;background:transparent;border:0;cursor:pointer;padding:6px}
.menu-toggle span{width:22px;height:2px;background:var(--text);border-radius:2px;transition:.2s}

/* ---------- Layout ---------- */
.layout{display:flex;align-items:flex-start;max-width:1360px;margin:0 auto}
.sidebar{
  position:sticky;top:var(--header-h);
  width:var(--sidebar-w);flex:0 0 var(--sidebar-w);
  height:calc(100vh - var(--header-h));overflow-y:auto;
  background:var(--sidebar-bg);border-right:1px solid var(--border);
  padding:22px 14px 60px;
}
.content{
  flex:1 1 auto;min-width:0;
  padding:40px clamp(20px,5vw,72px) 90px;
  max-width:920px;margin:0 auto;
}

/* ---------- Sidebar nav ---------- */
.side-nav .nav-group{margin-bottom:2px;border-radius:8px}
.nav-section{
  cursor:pointer;list-style:none;
  padding:9px 12px;border-radius:8px;
  font-size:13.5px;font-weight:600;color:var(--text-strong);
  display:flex;align-items:center;gap:8px;user-select:none;
}
.nav-section::-webkit-details-marker{display:none}
.nav-section::before{
  content:"";width:6px;height:6px;border-right:2px solid var(--muted);border-bottom:2px solid var(--muted);
  transform:rotate(-45deg);transition:transform .18s;flex:0 0 auto;margin-right:2px;
}
.nav-group[open] > .nav-section::before{transform:rotate(45deg)}
.nav-section:hover{background:var(--surface-2);color:var(--accent-strong)}
.nav-topics{list-style:none;margin:2px 0 8px;padding:0 0 0 4px}
.nav-topics li a{
  display:block;padding:7px 12px 7px 22px;margin:1px 0;
  font-size:13.5px;color:var(--muted);border-radius:7px;border-left:2px solid transparent;
  text-decoration:none;transition:.12s;
}
.nav-topics li a:hover{background:var(--surface-2);color:var(--text);text-decoration:none}
.nav-topics li.active a{
  background:var(--accent-soft);color:var(--accent-strong);font-weight:600;border-left-color:var(--accent);
}
:root[data-theme="dark"] .nav-topics li.active a{color:var(--accent)}

.nav-scrim{display:none}

/* ---------- Breadcrumb + head ---------- */
.breadcrumb{font-size:13px;color:var(--muted);margin-bottom:18px}
.breadcrumb a{color:var(--muted)}
.breadcrumb a:hover{color:var(--accent-strong)}
.breadcrumb .sep{margin:0 8px;opacity:.5}
.page-head{margin-bottom:30px;padding-bottom:22px;border-bottom:1px solid var(--border)}
.eyebrow{
  text-transform:uppercase;letter-spacing:1.4px;font-size:12px;font-weight:600;
  color:var(--accent-strong);margin:0 0 8px;
}
:root[data-theme="dark"] .eyebrow{color:var(--accent)}
.page-head h1{font-size:34px;line-height:1.2;margin:0;color:var(--text-strong);font-weight:700;letter-spacing:-.5px}

/* ---------- Prose ---------- */
.prose{font-size:16px}
.prose h2{font-size:23px;margin:44px 0 14px;color:var(--text-strong);font-weight:700;letter-spacing:-.3px;
  padding-bottom:8px;border-bottom:1px solid var(--border)}
.prose h3{font-size:18.5px;margin:32px 0 10px;color:var(--text-strong);font-weight:600}
.prose h4{font-size:16px;margin:24px 0 8px;color:var(--text-strong);font-weight:600}
.prose p{margin:14px 0}
.prose ul,.prose ol{margin:14px 0;padding-left:26px}
.prose li{margin:6px 0}
.prose li::marker{color:var(--accent)}
.prose strong{color:var(--text-strong);font-weight:650}
.prose hr{border:0;border-top:1px solid var(--border);margin:34px 0}
.prose em{color:var(--text)}

/* inline code */
.prose :not(pre) > code{
  background:var(--code-bg);border:1px solid var(--border);
  padding:.12em .42em;border-radius:6px;font-size:.88em;
  font-family:'JetBrains Mono',ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;color:var(--accent-strong);
}
:root[data-theme="dark"] .prose :not(pre) > code{color:var(--accent)}

/* code blocks */
.prose pre{
  background:var(--code-bg);border:1px solid var(--border);border-radius:10px;
  padding:16px 18px;overflow-x:auto;margin:18px 0;font-size:13.5px;line-height:1.6;
}
.prose pre code{font-family:'JetBrains Mono',ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;color:var(--text)}

/* blockquote / callout */
.prose blockquote{
  margin:20px 0;padding:14px 18px;border-left:4px solid var(--accent);
  background:var(--accent-soft);border-radius:0 10px 10px 0;color:var(--text);
}
.prose blockquote p{margin:6px 0}
.prose blockquote strong{color:var(--accent-strong)}
:root[data-theme="dark"] .prose blockquote strong{color:var(--accent)}

/* tables */
.prose table{
  width:100%;border-collapse:collapse;margin:20px 0;font-size:14.5px;
  border:1px solid var(--border);border-radius:10px;overflow:hidden;display:block;overflow-x:auto;
}
.prose thead th{background:var(--brand-navy);color:#fff;text-align:left;font-weight:600;padding:11px 14px;white-space:nowrap}
.prose tbody td{padding:11px 14px;border-top:1px solid var(--border);vertical-align:top}
.prose tbody tr:nth-child(even){background:var(--surface-2)}

/* mermaid */
.mermaid-wrap{margin:22px 0;padding:18px;background:var(--surface-2);border:1px solid var(--border);
  border-radius:10px;overflow-x:auto;text-align:center}
.mermaid{display:inline-block;min-width:min(100%,320px)}

/* images */
.prose img{max-width:100%;height:auto;border-radius:10px}

/* ---------- Pager ---------- */
.pager{display:flex;justify-content:space-between;gap:16px;margin-top:56px;padding-top:26px;border-top:1px solid var(--border)}
.pager-link{
  display:flex;flex-direction:column;gap:4px;max-width:46%;
  padding:14px 18px;border:1px solid var(--border);border-radius:12px;background:var(--surface);
  text-decoration:none!important;transition:.15s;box-shadow:var(--shadow);
}
.pager-link:hover{border-color:var(--accent);transform:translateY(-2px)}
.pager-link.next{text-align:right;margin-left:auto}
.pager-dir{font-size:12px;text-transform:uppercase;letter-spacing:1px;color:var(--muted)}
.pager-title{font-size:15px;font-weight:600;color:var(--text-strong)}

/* ---------- Home ---------- */
.hero{
  background:linear-gradient(135deg,var(--brand-navy) 0%,var(--brand-navy-2) 100%);
  color:#fff;border-radius:18px;padding:52px clamp(24px,5vw,56px);margin-bottom:44px;position:relative;overflow:hidden;
}
.hero::after{content:"";position:absolute;right:-60px;top:-60px;width:260px;height:260px;border-radius:50%;
  background:radial-gradient(circle,rgba(217,119,46,.28),transparent 70%)}
.hero .eyebrow{color:var(--accent)}
.hero h1{font-size:clamp(30px,4.5vw,46px);margin:6px 0 14px;font-weight:700;letter-spacing:-.8px;line-height:1.1}
.hero-sub{font-size:17px;max-width:640px;color:#cdd7e2;margin:0 0 30px}
.hero-stats{display:flex;gap:40px;flex-wrap:wrap;margin-bottom:32px}
.hero-stats div{display:flex;flex-direction:column}
.hero-stats strong{font-size:30px;color:#fff;font-weight:700}
.hero-stats span{font-size:13px;color:#9fb0c0;text-transform:uppercase;letter-spacing:1px}
.hero-cta{
  display:inline-block;background:var(--accent);color:#fff!important;padding:13px 26px;border-radius:10px;
  font-weight:600;font-size:15px;text-decoration:none!important;transition:.15s;
}
.hero-cta:hover{background:var(--accent-strong);transform:translateY(-2px)}

.grid-title{font-size:22px;margin:0 0 20px;color:var(--text-strong);font-weight:700}
.sec-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:20px}
.sec-card{
  background:var(--surface);border:1px solid var(--border);border-radius:14px;padding:22px;
  box-shadow:var(--shadow);transition:.18s;display:flex;flex-direction:column;
}
.sec-card:hover{border-color:var(--accent);transform:translateY(-3px)}
.sec-card-head{display:flex;align-items:baseline;gap:12px;margin-bottom:12px}
.sec-num{font-family:'JetBrains Mono',monospace;font-size:14px;font-weight:600;color:var(--accent);
  background:var(--accent-soft);padding:3px 9px;border-radius:7px}
.sec-card-head h3{margin:0;font-size:17.5px;line-height:1.3;font-weight:650}
.sec-card-head h3 a{color:var(--text-strong)}
.sec-card-head h3 a:hover{color:var(--accent-strong);text-decoration:none}
.sec-card-topics{list-style:none;margin:0;padding:0;border-top:1px solid var(--border);padding-top:12px}
.sec-card-topics li{margin:0}
.sec-card-topics li a{display:block;padding:6px 8px;border-radius:7px;font-size:14px;color:var(--muted);
  border-left:2px solid transparent}
.sec-card-topics li a:hover{background:var(--surface-2);color:var(--text);text-decoration:none;border-left-color:var(--accent)}

/* ---------- Syntax (highlight.js token classes) ---------- */
.hljs-comment,.hljs-quote{color:#8a97a5;font-style:italic}
.hljs-keyword,.hljs-selector-tag,.hljs-built_in,.hljs-name{color:#c4661e}
.hljs-string,.hljs-attr,.hljs-template-variable,.hljs-addition{color:#3f7d4e}
.hljs-number,.hljs-literal,.hljs-variable{color:#0b6b8f}
.hljs-title,.hljs-section,.hljs-function .hljs-title{color:#2a5fa5}
.hljs-type,.hljs-class .hljs-title{color:#8a5cc4}
:root[data-theme="dark"] .hljs-keyword,:root[data-theme="dark"] .hljs-built_in{color:#e08a44}
:root[data-theme="dark"] .hljs-string,:root[data-theme="dark"] .hljs-attr{color:#7bc088}
:root[data-theme="dark"] .hljs-number,:root[data-theme="dark"] .hljs-literal{color:#5fb3d4}
:root[data-theme="dark"] .hljs-title,:root[data-theme="dark"] .hljs-section{color:#79a6e0}
:root[data-theme="dark"] .hljs-type{color:#b48ce0}

/* ---------- Responsive ---------- */
@media (max-width:1000px){
  .menu-toggle{display:flex}
  .sidebar{
    position:fixed;top:var(--header-h);left:0;z-index:90;
    transform:translateX(-100%);transition:transform .22s ease;
    box-shadow:2px 0 20px rgba(0,0,0,.14);width:min(84vw,320px);
  }
  body.nav-open .sidebar{transform:translateX(0)}
  body.nav-open .nav-scrim{display:block;position:fixed;inset:var(--header-h) 0 0 0;background:rgba(10,18,28,.45);z-index:80}
  .content{max-width:none}
}
@media (max-width:560px){
  .brand-text{display:none}
  .hero-stats{gap:26px}
  .pager{flex-direction:column}
  .pager-link,.pager-link.next{max-width:none;text-align:left;margin-left:0}
}
"""

APP_JS = r"""
// ---- Theme ----
(function(){
  var saved = null;
  try { saved = localStorage.getItem('cit-theme'); } catch(e){}
  if (saved === 'dark' || (saved === null && window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
    document.documentElement.setAttribute('data-theme','dark');
  }
})();
function toggleTheme(){
  var el = document.documentElement;
  var next = el.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
  el.setAttribute('data-theme', next);
  try { localStorage.setItem('cit-theme', next); } catch(e){}
  renderMermaid(true);
}

// ---- Close mobile nav on link click ----
document.addEventListener('click', function(e){
  var a = e.target.closest('.nav-topics a');
  if (a) document.body.classList.remove('nav-open');
});

// ---- Highlight.js (loaded via CDN, may be async) ----
function runHighlight(){
  if (window.hljs) {
    document.querySelectorAll('pre code').forEach(function(b){
      try { window.hljs.highlightElement(b); } catch(e){}
    });
  }
}

// ---- Mermaid (dynamic import) ----
var _mermaid = null;
var _mermaidSources = [];
function currentMermaidTheme(){
  return document.documentElement.getAttribute('data-theme') === 'dark' ? 'dark' : 'neutral';
}
async function renderMermaid(rerender){
  var nodes = Array.prototype.slice.call(document.querySelectorAll('pre.mermaid'));
  if (!nodes.length) return;
  try{
    if (!_mermaid){
      var mod = await import('https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs');
      _mermaid = mod.default;
    }
    if (rerender){
      nodes.forEach(function(n,i){ if(_mermaidSources[i]!==undefined){ n.removeAttribute('data-processed'); n.innerHTML=_mermaidSources[i]; } });
    } else {
      nodes.forEach(function(n,i){ _mermaidSources[i]=n.textContent; });
    }
    _mermaid.initialize({ startOnLoad:false, theme: currentMermaidTheme(), securityLevel:'loose',
      fontFamily:'Inter, Segoe UI, Arial, sans-serif' });
    await _mermaid.run({ nodes: nodes });
  }catch(e){ /* offline: leave source visible */ }
}

window.addEventListener('load', function(){
  runHighlight();
  renderMermaid(false);
});
"""
