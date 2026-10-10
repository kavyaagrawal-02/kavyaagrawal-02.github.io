(function () {
  "use strict";
  var canvas = document.getElementById("scene");
  var ctx = canvas.getContext("2d");
  var orbit = document.getElementById("orbit");
  var intro = document.querySelector(".orbit-text");
  var ending = document.querySelector(".orbit-end");
  var pxOut = document.querySelector(".readout .px");
  var dsOut = document.querySelector(".readout .ds");
  var off = document.createElement("canvas");
  var offCtx = off.getContext("2d");

  // Each zoom step is a dataset Kavya works with, at its native resolution.
  var STEPS = [
    { px: "111 km", ds: "GRACE, water storage", block: 72 },
    { px: "27.8 km", ds: "GLDAS, land surface", block: 46 },
    { px: "11.1 km", ds: "ERA5-Land, climate", block: 30 },
    { px: "5.6 km", ds: "CHIRPS, rainfall", block: 20 },
    { px: "927 m", ds: "MODIS, temperature and greenness", block: 11 },
    { px: "100 m", ds: "GHSL, built-up land", block: 5 },
    { px: "30 m", ds: "SRTM, elevation", block: 2 },
    { px: "Ground", ds: "One village well", block: 1 }
  ];
  var TARGET = { x: 0.72, y: 0.73 };   // a village beside the river
  var MAXZOOM = 4.8;

  var sources = { "true": "assets/img/scene-true.jpg", "false": "assets/img/scene-false.jpg", "thermal": "assets/img/scene-thermal.jpg" };
  var images = {};
  var band = "true";
  function load(name) {
    if (images[name]) return images[name];
    var im = new Image();
    im.onload = draw;
    im.src = sources[name];
    images[name] = im;
    return im;
  }
  load("true");
  window.addEventListener("load", function () { load("false"); load("thermal"); });

  var dpr = 1, cw = 0, ch = 0;
  function resize() {
    dpr = Math.min(window.devicePixelRatio || 1, 2);
    cw = canvas.clientWidth; ch = canvas.clientHeight;
    canvas.width = Math.round(cw * dpr); canvas.height = Math.round(ch * dpr);
    draw();
  }

  function clamp(v, a, b) { return Math.max(a, Math.min(b, v)); }
  function progress() {
    var r = orbit.getBoundingClientRect();
    var span = orbit.offsetHeight - window.innerHeight;
    return clamp(-r.top / span, 0, 1);
  }
  function ease(t) { return t < .5 ? 2 * t * t : 1 - Math.pow(-2 * t + 2, 2) / 2; }

  var lastStep = -1;
  function draw() {
    var im = images[band];
    if (!im || !im.complete || !im.naturalWidth || !cw) return;
    var p = progress();
    var e = ease(p);
    var z = Math.exp(Math.log(MAXZOOM) * e);
    var iw = im.naturalWidth, ih = im.naturalHeight;
    // cover-fit base view
    var scale = Math.max(cw / iw, ch / ih);
    var vw = cw / scale / z, vh = ch / scale / z;
    var cx = iw * (0.5 + (TARGET.x - 0.5) * e), cy = ih * (0.5 + (TARGET.y - 0.5) * e);
    var sx = clamp(cx - vw / 2, 0, iw - vw), sy = clamp(cy - vh / 2, 0, ih - vh);

    var step = Math.min(STEPS.length - 1, Math.floor(p * STEPS.length * 1.02));
    var block = Math.max(1, Math.round(STEPS[step].block * dpr));
    var ow = Math.ceil(canvas.width / block), oh = Math.ceil(canvas.height / block);
    if (off.width !== ow || off.height !== oh) { off.width = ow; off.height = oh; }
    offCtx.imageSmoothingEnabled = true;
    offCtx.imageSmoothingQuality = "high";
    offCtx.drawImage(im, sx, sy, vw, vh, 0, 0, ow, oh);
    ctx.imageSmoothingEnabled = block <= 1;
    ctx.drawImage(off, 0, 0, ow, oh, 0, 0, ow * block, oh * block);

    if (step !== lastStep) {
      pxOut.textContent = STEPS[step].px;
      dsOut.textContent = STEPS[step].ds;
      lastStep = step;
    }
    intro.style.opacity = clamp(1 - p * 3.2, 0, 1);
    intro.style.visibility = p > .32 ? "hidden" : "visible";
    ending.style.opacity = clamp((p - .8) * 5, 0, 1);
  }

  // band switcher
  document.querySelectorAll(".bands button").forEach(function (b) {
    b.addEventListener("click", function () {
      band = b.dataset.band;
      load(band);
      document.querySelectorAll(".bands button").forEach(function (o) { o.setAttribute("aria-pressed", o === b ? "true" : "false"); });
      draw();
    });
  });

  // stage tracking: bar colours, nav highlight, drop meter
  var sections = Array.prototype.slice.call(document.querySelectorAll("[data-stage]"));
  var bar = document.querySelector(".bar");
  var meter = document.querySelector(".drop-meter");
  var fill = document.getElementById("drop-fill");
  var stageOut = meter.querySelector(".stage");
  var depthOut = meter.querySelector(".depth");
  var navLinks = document.querySelectorAll(".bar nav a");
  var current = null;
  function track() {
    var y = 56;
    var s = sections[0];
    for (var i = 0; i < sections.length; i++) {
      if (sections[i].getBoundingClientRect().top <= y) s = sections[i];
    }
    if (s !== current) {
      current = s;
      var dark = s.dataset.tone === "dark";
      var root = document.documentElement.style;
      root.setProperty("--bar-ink", dark ? "#E4EEF0" : "#142830");
      root.setProperty("--bar-bg", dark ? s.dataset.bg || "#08131C" : s.dataset.bg || "#E9F2F4");
      stageOut.textContent = s.dataset.stage;
      depthOut.textContent = s.dataset.depth;
      navLinks.forEach(function (a) { a.classList.toggle("on", a.getAttribute("href") === "#" + s.id); });
    }
    bar.classList.toggle("solid", window.scrollY > window.innerHeight * 2.6);
    var doc = document.documentElement;
    var pct = clamp(window.scrollY / (doc.scrollHeight - window.innerHeight), 0, 1);
    fill.setAttribute("y", String(40 - 34 * pct));
    fill.setAttribute("height", String(34 * pct + 1));
  }

  var ticking = false;
  window.addEventListener("scroll", function () {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(function () { draw(); track(); ticking = false; });
  }, { passive: true });
  window.addEventListener("resize", resize);
  resize(); track();

  // postcards
  document.querySelectorAll(".postcard").forEach(function (c) {
    c.addEventListener("click", function () {
      c.setAttribute("aria-pressed", c.getAttribute("aria-pressed") === "true" ? "false" : "true");
    });
  });
  // coin: back to orbit
  var coin = document.querySelector(".coin");
  if (coin) coin.addEventListener("click", function () { window.scrollTo({ top: 0, behavior: "smooth" }); });
})();
