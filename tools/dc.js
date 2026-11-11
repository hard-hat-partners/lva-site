/* LVA Mayan Stucco site runtime.
   Renders the page template in <template id="dc-tpl"> into #dc-root with the
   page's Component class, and patches the DOM in place on every setState so
   videos, focus and animations are never reset. No dependencies. */
(function () {
  'use strict';
  var handlers = [];

  window.DCLogic = function (props) { this.props = props || {}; this.state = {}; };
  window.DCLogic.prototype.setState = function (s) {
    var n = typeof s === 'function' ? s(this.state) : s;
    for (var k in n) this.state[k] = n[k];
    schedule();
  };
  window.DCLogic.prototype.forceUpdate = function () { schedule(); };

  function get(scope, path) {
    path = path.trim();
    if (path === 'true') return true;
    if (path === 'false') return false;
    if (path === 'null') return null;
    if (/^-?\d+(\.\d+)?$/.test(path)) return Number(path);
    var parts = path.split('.'), v = scope;
    for (var i = 0; i < parts.length; i++) { if (v == null) return undefined; v = v[parts[i]]; }
    return v;
  }
  function interp(str, scope) {
    var m = str.match(/^\s*\{\{([^}]+)\}\}\s*$/);
    if (m) return get(scope, m[1]);
    return str.replace(/\{\{([^}]+)\}\}/g, function (_, p) { var v = get(scope, p); return v == null ? '' : String(v); });
  }

  // Turn a template subtree into live nodes for one scope.
  function proc(node, scope, out) {
    if (node.nodeType === 3) {
      var t = node.nodeValue;
      out.push(document.createTextNode(t.indexOf('{{') > -1 ? interp(t, scope) : t));
      return;
    }
    if (node.nodeType !== 1) return;
    var tag = node.localName;
    if (tag === 'sc-if') {
      out.push(document.createComment('dc-open'));
      if (interp(node.getAttribute('value'), scope)) kids(node, scope, out);
      out.push(document.createComment('dc-close'));
      return;
    }
    if (tag === 'sc-for') {
      var list = interp(node.getAttribute('list'), scope) || [], as = node.getAttribute('as');
      out.push(document.createComment('dc-open'));
      for (var i = 0; i < list.length; i++) {
        var s = Object.create(scope); s[as] = list[i]; s.$index = i;
        kids(node, s, out);
      }
      out.push(document.createComment('dc-close'));
      return;
    }
    var el = node.namespaceURI === 'http://www.w3.org/2000/svg'
      ? document.createElementNS(node.namespaceURI, node.tagName)
      : document.createElement(tag);
    for (var a = 0; a < node.attributes.length; a++) {
      var at = node.attributes[a], name = at.name, val = at.value;
      if (name.indexOf('hint-') === 0) continue;
      if (/^on[a-z]+$/.test(name)) {
        var fn = interp(val, scope);
        if (typeof fn === 'function') { handlers.push({ ev: name.slice(2), fn: fn }); el.setAttribute('data-dc-on', String(handlers.length - 1)); }
        continue;
      }
      if (val.indexOf('{{') > -1) {
        var v = interp(val, scope);
        if (v === false || v == null) continue;
        val = v === true ? '' : String(v);
      }
      el.setAttribute(name, val);
    }
    if (tag === 'video') { el.muted = el.hasAttribute('muted'); el.playsInline = true; }
    var inner = [];
    kids(node.content || node, scope, inner);
    for (var c = 0; c < inner.length; c++) el.appendChild(inner[c]);
    out.push(el);
  }
  function kids(node, scope, out) {
    for (var c = node.firstChild; c; c = c.nextSibling) proc(c, scope, out);
  }

  // Group a flat node list into items; dc-open/dc-close markers become blocks.
  function group(nodes) {
    var root = [], stack = [root];
    for (var i = 0; i < nodes.length; i++) {
      var n = nodes[i];
      if (n.nodeType === 8 && n.nodeValue === 'dc-open') {
        var g = { open: n, kids: [], close: null };
        stack[stack.length - 1].push(g); stack.push(g.kids); stack[stack.length - 1].owner = g;
      } else if (n.nodeType === 8 && n.nodeValue === 'dc-close') {
        stack[stack.length - 1].owner.close = n; stack.pop();
      } else if (n.nodeType === 8) {
        continue;
      } else stack[stack.length - 1].push(n);
    }
    return root;
  }
  function itemNodes(it, out) {
    if (it.open) { out.push(it.open); for (var i = 0; i < it.kids.length; i++) itemNodes(it.kids[i], out); out.push(it.close); }
    else out.push(it);
    return out;
  }
  function insertItem(parent, it, ref) {
    var ns = itemNodes(it, []);
    for (var i = 0; i < ns.length; i++) parent.insertBefore(ns[i], ref);
  }
  function removeItem(parent, it) {
    var ns = itemNodes(it, []);
    for (var i = 0; i < ns.length; i++) if (ns[i].parentNode === parent) parent.removeChild(ns[i]);
  }
  function patchList(parent, olds, news, endRef) {
    var i;
    for (i = 0; i < news.length; i++) {
      var o = olds[i], n = news[i];
      if (!o) { insertItem(parent, n, endRef); continue; }
      if (o.open && n.open) { patchList(parent, o.kids, n.kids, o.close); continue; }
      if (!o.open && !n.open && same(o, n)) { patchNode(o, n); continue; }
      insertItem(parent, n, o.open || o);
      removeItem(parent, o);
    }
    for (; i < olds.length; i++) removeItem(parent, olds[i]);
  }
  function same(o, n) {
    return o.nodeType === n.nodeType && o.nodeName === n.nodeName;
  }
  function patchNode(o, n) {
    if (o.nodeType === 3) { if (o.nodeValue !== n.nodeValue) o.nodeValue = n.nodeValue; return; }
    var a, i;
    for (i = o.attributes.length - 1; i >= 0; i--) {
      a = o.attributes[i].name;
      if (!n.hasAttribute(a)) o.removeAttribute(a);
    }
    for (i = 0; i < n.attributes.length; i++) {
      a = n.attributes[i];
      if (o.getAttribute(a.name) !== a.value) o.setAttribute(a.name, a.value);
    }
    patchList(o, group(Array.prototype.slice.call(o.childNodes)), group(Array.prototype.slice.call(n.childNodes)), null);
  }

  var inst, tpl, rootEl, pending = false, mounted = false;
  function render() {
    pending = false;
    handlers = [];
    var vals = inst.renderVals ? inst.renderVals() : {};
    var out = [];
    kids(tpl.content, vals, out);
    var news = group(out);
    var olds = group(Array.prototype.slice.call(rootEl.childNodes));
    patchList(rootEl, olds, news, null);
    var vs = rootEl.querySelectorAll('video[autoplay]');
    for (var i = 0; i < vs.length; i++) { var v = vs[i]; if (v.paused && !v.ended && !v.dataset.dcStarted) { v.dataset.dcStarted = '1'; v.muted = v.hasAttribute('muted'); var pr = v.play(); if (pr && pr.catch) pr.catch(function () {}); } }
  }
  function schedule() {
    if (!mounted || pending) return;
    pending = true;
    (window.requestAnimationFrame || setTimeout)(render);
  }
  function fire(e) {
    var el = e.target && e.target.closest ? e.target.closest('[data-dc-on]') : null;
    if (!el) return;
    var h = handlers[+el.getAttribute('data-dc-on')];
    if (h && h.ev === e.type) h.fn(e);
  }

  function boot() {
    tpl = document.getElementById('dc-tpl');
    rootEl = document.getElementById('dc-root');
    var code = document.getElementById('dc-logic').textContent;
    var Component = new Function(code + '\nreturn Component;')();
    inst = new Component({});
    document.addEventListener('click', fire);
    render();
    mounted = true;
    document.documentElement.classList.add('dc-ready');
    if (inst.componentDidMount) inst.componentDidMount();
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot);
  else boot();
})();
