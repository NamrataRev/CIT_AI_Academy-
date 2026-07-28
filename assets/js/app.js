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

// ---- Close mobile nav after choosing a lesson ----
document.addEventListener('click', function(e){
  var a = e.target.closest('.nav-topics a');
  if (a) document.body.classList.remove('nav-open');
});

// ---- Mermaid ----
// kramdown + Rouge renders ```mermaid fences as highlighted code blocks; we
// pull the raw text back out and hand it to Mermaid.
var _mermaid = null;
var _mermaidSources = [];
function currentMermaidTheme(){
  return document.documentElement.getAttribute('data-theme') === 'dark' ? 'dark' : 'neutral';
}
function prepareMermaid(){
  var candidates = document.querySelectorAll('.language-mermaid, pre > code.language-mermaid, pre.mermaid');
  candidates.forEach(function(node){
    if (node.classList.contains('mermaid') && node.tagName === 'PRE') return; // already prepared
    var codeEl = node.querySelector('code') || node;
    var src = codeEl.textContent;
    var pre = document.createElement('pre');
    pre.className = 'mermaid';
    pre.textContent = src;
    var wrap = document.createElement('div');
    wrap.className = 'mermaid-wrap';
    wrap.appendChild(pre);
    // Replace the outermost rouge container if present.
    var target = node.closest('.highlighter-rouge') || node.closest('pre') || node;
    if (target && target.parentNode) target.parentNode.replaceChild(wrap, target);
  });
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
  }catch(e){ /* offline: leave the source visible */ }
}

window.addEventListener('load', function(){
  prepareMermaid();
  renderMermaid(false);
});
