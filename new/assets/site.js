(function () {
  "use strict";
  var root = document.documentElement;
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  function $(s, c) { return (c || document).querySelector(s); }
  function $$(s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); }
  function cssVar(n) { return getComputedStyle(root).getPropertyValue(n).trim(); }
  function clamp(v, a, b) { return Math.max(a, Math.min(b, v)); }

  /* ---------- bands (theme) ---------- */
  var bandBtns = $$(".bands button");
  function setBand(b, save) {
    root.dataset.band = b;
    bandBtns.forEach(function (x) { x.setAttribute("aria-pressed", x.dataset.band === b ? "true" : "false"); });
    if (save) { try { localStorage.setItem("band", b); } catch (e) {} }
    drawHere(); loadScene(b);
  }
  bandBtns.forEach(function (x) { x.addEventListener("click", function () { setBand(x.dataset.band, true); }); });

  /* ---------- panel (mobile) ---------- */
  var panel = $("#panel"), toggle = $(".panel-toggle");
  function closePanel() { panel.classList.remove("open"); toggle.setAttribute("aria-expanded", "false"); }
  toggle.addEventListener("click", function () {
    var open = !panel.classList.contains("open");
    panel.classList.toggle("open", open); toggle.setAttribute("aria-expanded", open ? "true" : "false");
  });
  function isMobile() { return window.matchMedia("(max-width: 900px)").matches; }

  /* ---------- layers: show/hide and fly-to ---------- */
  var chapters = $$(".chapter");
  $$("[data-toggle]").forEach(function (cb) {
    cb.addEventListener("change", function () {
      var ch = document.getElementById(cb.dataset.toggle);
      ch.hidden = !cb.checked;
      cb.closest(".layer").classList.toggle("off", !cb.checked);
      track();
    });
  });
  function flyTo(el, focusEl) {
    var ch = el.closest(".chapter") || el;
    if (ch.hidden) {
      ch.hidden = false;
      var cb = $('[data-toggle="' + ch.id + '"]'); if (cb) { cb.checked = true; cb.closest(".layer").classList.remove("off"); }
    }
    if (!reduce) {
      var r = document.createElement("div"); r.className = "zoom-ring"; r.innerHTML = "<i></i>";
      document.body.appendChild(r); setTimeout(function () { r.remove(); }, 800);
    }
    el.scrollIntoView({ behavior: reduce ? "auto" : "smooth", block: el === ch ? "start" : "center" });
    if (el === ch && !reduce) { ch.classList.remove("arrive"); void ch.offsetWidth; ch.classList.add("arrive"); }
    if (focusEl) { focusEl.classList.remove("flash"); void focusEl.offsetWidth; focusEl.classList.add("flash"); }
    if (isMobile()) closePanel();
  }
  $$(".layer a, .me").forEach(function (a) {
    a.addEventListener("click", function (e) {
      var id = a.getAttribute("href").slice(1), t = document.getElementById(id);
      if (!t) return;
      e.preventDefault(); flyTo(t);
      try { history.replaceState(null, "", "#" + id); } catch (er) {}
    });
  });

  /* ---------- current chapter, meter ---------- */
  var mName = $("#m-name"), mCoords = $("#m-coords"), fill = $("#drop-fill"), current = null;
  function track() {
    var y = window.innerHeight * 0.3, cur = chapters[0];
    chapters.forEach(function (c) { if (!c.hidden && c.getBoundingClientRect().top <= y) cur = c; });
    if (cur !== current) {
      current = cur;
      mName.textContent = cur.dataset.name; mCoords.textContent = cur.dataset.coords;
      $$(".layer").forEach(function (l) { l.classList.toggle("on-screen", l.dataset.for === cur.id); });
    }
    var pct = clamp(window.scrollY / Math.max(1, document.documentElement.scrollHeight - window.innerHeight), 0, 1);
    fill.setAttribute("y", String(40 - 34 * pct)); fill.setAttribute("height", String(34 * pct + 1));
  }

  /* ---------- search ---------- */
  var q = $("#q"), results = $("#results");
  var SEL = ".news li, .currently div, .stratum, .sample li, .tile, .sheet, .pcard, .pubcard, .slayer, .slayer li, .badge, .entry, .patch, .minute, .idcard, .masthead li, .trophy, .cell, .explore li, .manual, .beyond-grid li, .framework p";
  var index = $$(SEL).map(function (el) {
    var h = el.querySelector("h3, b, .nm, h4");
    var title = (h ? h.textContent : el.textContent).replace(/\s+/g, " ").trim();
    return { el: el, text: el.textContent.replace(/\s+/g, " ").toLowerCase(), title: title.length > 90 ? title.slice(0, 88) + "…" : title,
      ch: (el.closest(".chapter") || {}).dataset ? el.closest(".chapter").dataset.name : "" };
  });
  q.addEventListener("input", function () {
    var v = q.value.trim().toLowerCase();
    results.innerHTML = "";
    if (v.length < 2) return;
    var hits = index.filter(function (i) { return i.text.indexOf(v) !== -1; }).slice(0, 8);
    if (!hits.length) { results.innerHTML = '<li class="none">Nothing found. Try another word, like "uranium" or "2024".</li>'; return; }
    hits.forEach(function (h) {
      var li = document.createElement("li"), b = document.createElement("button");
      b.type = "button";
      var t = document.createTextNode(h.title), s = document.createElement("small");
      s.textContent = h.ch; b.appendChild(s); b.appendChild(t);
      b.addEventListener("click", function () {
        var sheet = h.el.closest(".sheet"); if (sheet) openSheet(sheet, true);
        if (h.el.matches(".tile")) h.el.click();
        flyTo(h.el, h.el);
      });
      li.appendChild(b); results.appendChild(li);
    });
  });

  /* ---------- summary map background ---------- */
  var hereCanvas = $("#here-map");
  function drawHere() {
    if (!hereCanvas) return;
    var w = hereCanvas.clientWidth, h = hereCanvas.clientHeight, dpr = Math.min(window.devicePixelRatio || 1, 2);
    if (!w) return;
    hereCanvas.width = w * dpr; hereCanvas.height = h * dpr;
    var c = hereCanvas.getContext("2d"); c.setTransform(dpr, 0, 0, dpr, 0, 0); c.clearRect(0, 0, w, h);
    var line = cssVar("--line"), acc = cssVar("--accent"), soil = cssVar("--accent-2");
    c.strokeStyle = line; c.lineWidth = 1;
    for (var i = 1; i < 8; i++) { c.beginPath(); c.moveTo(w * i / 8, 0); c.lineTo(w * i / 8, h); c.stroke(); c.beginPath(); c.moveTo(0, h * i / 8); c.lineTo(w, h * i / 8); c.stroke(); }
    // contour rings around two hills, wobbly
    function rings(cx, cy, n, col) {
      c.strokeStyle = col; c.globalAlpha = 0.45;
      for (var k = 1; k <= n; k++) {
        c.beginPath();
        for (var a = 0; a <= 64; a++) {
          var t = a / 64 * Math.PI * 2, r = k * Math.min(w, h) * 0.045 * (1 + 0.12 * Math.sin(3 * t + k) + 0.06 * Math.cos(5 * t - k));
          var x = cx + Math.cos(t) * r * 1.25, y = cy + Math.sin(t) * r;
          a ? c.lineTo(x, y) : c.moveTo(x, y);
        }
        c.closePath(); c.stroke();
      }
      c.globalAlpha = 1;
    }
    rings(w * 0.2, h * 0.25, 6, soil); rings(w * 0.82, h * 0.78, 7, soil);
    // a river
    c.strokeStyle = acc; c.lineWidth = 3; c.globalAlpha = 0.55; c.beginPath();
    c.moveTo(w * 0.05, h * 0.05);
    c.bezierCurveTo(w * 0.35, h * 0.3, w * 0.15, h * 0.6, w * 0.45, h * 0.62);
    c.bezierCurveTo(w * 0.75, h * 0.64, w * 0.6, h * 0.92, w * 0.95, h * 0.98); c.stroke(); c.globalAlpha = 1;
  }

  /* ---------- research: orbit zoom ---------- */
  var orbit = $("#orbit"), canvas = $("#scene");
  var ctx = canvas ? canvas.getContext("2d") : null;
  var off = document.createElement("canvas"), offCtx = off.getContext("2d");
  var STEPS = [
    { px: "111 km", ds: "GRACE, water storage", block: 72 }, { px: "27.8 km", ds: "GLDAS, land surface", block: 46 },
    { px: "11.1 km", ds: "ERA5-Land, climate", block: 30 }, { px: "5.6 km", ds: "CHIRPS, rainfall", block: 20 },
    { px: "927 m", ds: "MODIS, temperature and greenness", block: 11 }, { px: "100 m", ds: "GHSL, built-up land", block: 5 },
    { px: "30 m", ds: "SRTM, elevation", block: 2 }, { px: "Ground", ds: "One village well", block: 1 }];
  var imgs = {}, sceneBand = "false", lastStep = -1;
  function loadScene(b) {
    sceneBand = b;
    if (!imgs[b]) { var im = new Image(); im.onload = drawScene; im.src = "assets/img/scene-" + b + ".jpg"; imgs[b] = im; }
    drawScene();
  }
  function sizeScene() {
    if (!canvas) return;
    var dpr = Math.min(window.devicePixelRatio || 1, 2);
    canvas.width = Math.round(canvas.clientWidth * dpr); canvas.height = Math.round(canvas.clientHeight * dpr);
    drawScene();
  }
  function drawScene() {
    if (!canvas) return;
    var im = imgs[sceneBand];
    if (!im || !im.complete || !im.naturalWidth || !canvas.width) return;
    var r = orbit.getBoundingClientRect();
    if (r.bottom < -50 || r.top > window.innerHeight + 50) return;
    var span = orbit.offsetHeight - window.innerHeight, p = clamp(-r.top / Math.max(1, span), 0, 1);
    var e = p < .5 ? 2 * p * p : 1 - Math.pow(-2 * p + 2, 2) / 2;
    var z = Math.exp(Math.log(4.8) * e), iw = im.naturalWidth, ih = im.naturalHeight;
    var W = canvas.width, H = canvas.height, sc = Math.max(W / iw, H / ih);
    var vw = W / sc / z, vh = H / sc / z;
    var cx = iw * (0.5 + 0.22 * e), cy = ih * (0.5 + 0.23 * e);
    var sx = clamp(cx - vw / 2, 0, iw - vw), sy = clamp(cy - vh / 2, 0, ih - vh);
    var step = Math.min(STEPS.length - 1, Math.floor(p * STEPS.length * 1.02));
    var dpr = Math.min(window.devicePixelRatio || 1, 2), block = Math.max(1, Math.round(STEPS[step].block * dpr));
    var ow = Math.ceil(W / block), oh = Math.ceil(H / block);
    if (off.width !== ow || off.height !== oh) { off.width = ow; off.height = oh; }
    offCtx.imageSmoothingEnabled = true; offCtx.drawImage(im, sx, sy, vw, vh, 0, 0, ow, oh);
    ctx.imageSmoothingEnabled = block <= 1; ctx.drawImage(off, 0, 0, ow, oh, 0, 0, ow * block, oh * block);
    if (step !== lastStep) { $(".readout .px").textContent = STEPS[step].px; $(".readout .ds").textContent = STEPS[step].ds; lastStep = step; }
  }

  /* ---------- research tiles ---------- */
  var detail = $("#tile-detail");
  $$(".tile").forEach(function (t) {
    t.addEventListener("click", function () {
      var d = window.DETAILS[t.dataset.tile]; if (!d) return;
      $$(".tile").forEach(function (o) { o.setAttribute("aria-expanded", o === t ? "true" : "false"); });
      detail.style.setProperty("--tc", d.c);
      var dl = d.d.map(function (x) { return "<div><dt>" + x[0] + "</dt><dd>" + x[1] + "</dd></div>"; }).join("");
      detail.innerHTML = '<div><span class="k">' + d.k + "</span><h3>" + d.t + "</h3><p>" + d.p + "</p></div><dl>" + dl + "</dl>";
    });
  });

  /* ---------- teaching demo ---------- */
  var DEMO = {
    "true": ["True colour", "Red, green and blue light, roughly what your eyes would see from orbit. Fields look green, bare soil brown, water dark."],
    "false": ["False colour", "Near-infrared is shown as red. Healthy plants reflect a lot of near-infrared, so crops and forests glow red, while towns look blue-grey and water almost black."],
    "thermal": ["Thermal", "Land surface temperature. Bright yellow is hot ground on the plains, purple is cool: the river, its wet floodplain and the snowy mountains."]
  };
  $$("[data-demo]").forEach(function (b) {
    b.addEventListener("click", function () {
      var k = b.dataset.demo, img = $("#demo-img");
      $$("[data-demo]").forEach(function (o) { o.setAttribute("aria-pressed", o === b ? "true" : "false"); });
      img.src = "assets/img/scene-" + k + ".jpg"; img.alt = "Illustrative satellite scene in " + DEMO[k][0].toLowerCase();
      $("#demo-h").textContent = DEMO[k][0]; $("#demo-p").textContent = DEMO[k][1];
    });
  });

  /* ---------- projects ---------- */
  function openSheet(s, force) {
    var open = force ? true : !s.classList.contains("open");
    s.classList.toggle("open", open); s.querySelector("button").setAttribute("aria-expanded", open ? "true" : "false");
  }
  $$(".sheet > button").forEach(function (b) { b.addEventListener("click", function () { openSheet(b.parentNode); }); });
  $$(".filters button").forEach(function (b) {
    b.addEventListener("click", function () {
      var f = b.dataset.f;
      $$(".filters button").forEach(function (o) { o.setAttribute("aria-pressed", o === b ? "true" : "false"); });
      $$(".sheet").forEach(function (s) { s.hidden = !(f === "all" || s.dataset.theme === f); });
    });
  });

  /* ---------- skills ---------- */
  $$("[data-skill]").forEach(function (cb) {
    cb.addEventListener("change", function () {
      var i = cb.dataset.skill;
      $('[data-layer="' + i + '"]').classList.toggle("off", !cb.checked);
      $('[data-core="' + i + '"]').classList.toggle("off", !cb.checked);
    });
  });

  /* ---------- training ---------- */
  var cert = $("#cert");
  $$("[data-patch]").forEach(function (b) {
    b.addEventListener("click", function () {
      var d = window.PATCHES[b.dataset.patch];
      $$("[data-patch]").forEach(function (o) { o.setAttribute("aria-expanded", o === b ? "true" : "false"); });
      cert.querySelector("h3").textContent = d.t; cert.querySelector("p").textContent = d.w;
    });
  });

  /* ---------- copy ---------- */
  $$("[data-copy]").forEach(function (b) {
    b.addEventListener("click", function () {
      var t = b.dataset.copy;
      function done(msg) { b.textContent = msg; setTimeout(function () { b.textContent = "Copy"; }, 1800); }
      try { navigator.clipboard.writeText(t).then(function () { done("Copied"); }, function () { done("Select and copy"); }); }
      catch (e) { done("Select and copy"); }
    });
  });

  /* ---------- go ---------- */
  var ticking = false;
  window.addEventListener("scroll", function () {
    if (ticking) return; ticking = true;
    requestAnimationFrame(function () { track(); drawScene(); ticking = false; });
  }, { passive: true });
  window.addEventListener("resize", function () { drawHere(); sizeScene(); });
  setBand(root.dataset.band || "false", false);
  sizeScene(); track();
  if (location.hash && document.getElementById(location.hash.slice(1))) {
    setTimeout(function () { document.getElementById(location.hash.slice(1)).scrollIntoView(); }, 50);
  }
})();
