"""Builds new/index.html: the creative 'journey of a drop' page."""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "new"

LINKS = {
    "email": "mailto:kavya.agrawal@terisas.ac.in",
    "linkedin": "https://www.linkedin.com/in/kavya-agrawal02/",
    "scholar": "https://scholar.google.com/citations?user=yXQUQ6YAAAAJ&hl=en",
    "orcid": "https://orcid.org/0009-0009-1032-2541",
    "researchgate": "https://www.researchgate.net/profile/Kavya-Agrawal-4",
    "github": "https://github.com/kavyaagrawal-02",
}

_pm = 0


def postmark(city, date, color="#1E3C46"):
    global _pm
    _pm += 1
    i = _pm
    return f"""<svg class="postmark" viewBox="0 0 80 80" aria-hidden="true" style="color:{color}">
  <defs><path id="pm{i}" d="M40,40 m-27,0 a27,27 0 1,1 54,0 a27,27 0 1,1 -54,0"/></defs>
  <circle cx="40" cy="40" r="37" fill="none" stroke="currentColor" stroke-width="2"/>
  <circle cx="40" cy="40" r="20" fill="none" stroke="currentColor" stroke-width="1.2"/>
  <text fill="currentColor"><textPath href="#pm{i}" startOffset="0">{city.upper()} ✦ {city.upper()} ✦</textPath></text>
  <text x="40" y="43" text-anchor="middle" fill="currentColor" style="font-size:9px">{date}</text>
</svg>"""


CARDS = [
    dict(town="Hathras", yrs="2014–2016", code="HRS", c1="#E0892E", c2="#B5541F", date="2016",
         msg="Secondary school at St. Francis Inter College, CGPA 9.20. The start of four years of top-3 ranks in the English Olympiads, and a Merit Award in 2016.",
         addr=["St. Francis Inter College", "Secondary school", "CGPA 9.20"]),
    dict(town="Aligarh", yrs="2016–2018", code="ALJN", c1="#3F7FA3", c2="#24506B", date="2018",
         msg="Senior secondary at Delhi Public School, CGPA 9.80. Won the State Child Scientist Award at the National Science Congress in 2018.",
         addr=["Delhi Public School", "Senior secondary", "CGPA 9.80"]),
    dict(town="Delhi", yrs="2018–2021", code="DLI", c1="#9A4A6E", c2="#62284A", date="2021",
         msg="BA (Hons) Geography at the University of Delhi. Editor-in-Chief of the Geography Association, ran the college magazine Vani, NSS volunteer. My first GIS maps: Delhi's forests, sprawl and land use.",
         addr=["University of Delhi", "BA (Hons) Geography", "CGPA 7.86"]),
    dict(town="Agra", yrs="2021–2023", code="AGC", c1="#3B8B78", c2="#1F5A4B", date="2023",
         msg="MA Geography at Dr. B.R. Ambedkar University. Five conference papers in 2022, and my first journal paper, on temperature trends across the Indus Basin.",
         addr=["Dr. B.R. Ambedkar University", "MA Geography", "CGPA 7.60"]),
    dict(town="New Delhi", yrs="2024 to now", code="NDLS", c1="#2A5C9A", c2="#163762", date="2026",
         msg="PhD at TERI School of Advanced Studies. Coursework CGPA 9.0; comprehensive exam cleared in January 2026. Now predicting groundwater contamination across India.",
         addr=["TERI School of Advanced Studies", "PhD, Natural & Applied Sciences", "Coursework CGPA 9.0"]),
]


def postcard(c):
    addr = "".join(f"<li>{a}</li>" for a in c["addr"])
    return f"""<li><button class="postcard" type="button" aria-pressed="false" aria-label="{c['town']}, {c['yrs']}. Turn the postcard over">
  <span class="inner">
    <span class="face front" style="background:linear-gradient(150deg,{c['c1']},{c['c2']})">
      <span class="greet">Greetings from</span>
      <span class="stamp" aria-hidden="true"><i style="background:{c['c2']}">{c['code']}<small>INDIA</small></i></span>
      {postmark(c['town'], c['date'], '#ffffff')}
      <span class="town">{c['town']}</span>
      <span class="yrs">{c['yrs']}</span>
    </span>
    <span class="face back">
      <span class="msg">{c['msg']}</span>
      <span class="addr"><ul>{addr}</ul>{postmark(c['town'], c['date'])}</span>
    </span>
  </span>
</button></li>"""


TALKS = [
    ("Greater Noida", "IV.2026", "Machine-learning-based uranium risk assessment, population exposure and groundwater governance", "ICSSR EHP NEXUS 2026, Gautam Buddha University. First position and Best Paper Award."),
    ("Bhubaneswar", "X.2024", "Controls on arsenic mobilisation in aquifers of the Middle Gangetic Plain", "As2024, 9th International Congress on Arsenic in the Environment, KIIT."),
    ("Mahendragarh", "XI.2022", "Problems and prospects of Delhi's drinking water supply", "IGU Thematic Conference, Central University of Haryana."),
    ("Gurugram", "VII.2022", "Educational relevance of Ramayana in modern India", "National Seminar, Amity University Haryana (ICPR)."),
    ("Delhi", "V.2022", "Digital enhancement of physical space in tourism during and after COVID-19", "Geography and the Digital, Delhi School of Economics."),
    ("New Delhi", "V.2022", "Migrant college students during the Covid pandemic", "Jamia International Conference on Education 2022, Jamia Millia Islamia."),
    ("Delhi", "IV.2022", "Migrant college students during the Covid pandemic", "Disaster Risk Reduction and Resilient Habitat, SBS College, University of Delhi."),
]


def talk(city, date, title, where):
    return f"""<li>{postmark(city, date, 'currentColor')}<div><h3>{title}</h3><p>{where}</p></div></li>"""


TAP_SVG = """<svg viewBox="0 0 200 300" aria-hidden="true">
  <rect x="10" y="20" width="22" height="70" rx="4" fill="#8A9A96"/>
  <path d="M32 40 h70 a26 26 0 0 1 26 26 v24 h-30 v-18 a6 6 0 0 0 -6 -6 h-60 z" fill="#A9B7B3"/>
  <rect x="58" y="14" width="22" height="26" rx="3" fill="#8A9A96"/>
  <rect x="44" y="8" width="50" height="10" rx="5" fill="#2C7D8C"/>
  <rect x="96" y="90" width="34" height="10" rx="3" fill="#8A9A96"/>
  <path class="fall" d="M113 112 c0 0 -9 12 -9 18 a9 9 0 0 0 18 0 c0 -6 -9 -18 -9 -18z" fill="#2C7D8C"/>
  <ellipse cx="113" cy="282" rx="60" ry="8" fill="#C9D0C5"/>
</svg>"""

RIDGE = """<svg class="ridge" viewBox="0 0 1440 140" preserveAspectRatio="none" aria-hidden="true">
  <path d="M0 140 L0 92 L90 60 L150 84 L240 22 L300 70 L370 48 L460 100 L540 40 L610 66 L700 6 L770 58 L850 36 L930 88 L1010 30 L1090 74 L1170 44 L1250 96 L1330 52 L1440 80 L1440 140 Z" fill="#E9F2F4"/>
  <path d="M240 22 L262 40 L250 38 L232 46 Z M700 6 L728 30 L712 26 L690 34 Z M1010 30 L1034 50 L1020 46 L1000 54 Z" fill="#ffffff"/>
</svg>"""

RIVER_SVG = """<svg class="river-line" viewBox="0 0 360 2400" preserveAspectRatio="none" aria-hidden="true">
  <path d="M180 0 C 330 200, 30 360, 180 600 S 330 1000, 180 1200 S 20 1600, 190 1800 S 340 2200, 180 2400" stroke-width="30" opacity=".25"/>
  <path d="M180 0 C 330 200, 30 360, 180 600 S 330 1000, 180 1200 S 20 1600, 190 1800 S 340 2200, 180 2400" stroke-width="12" opacity=".9"/>
</svg>"""

DROP_ICON = """<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.5c0 0-6.5 8-6.5 12.2a6.5 6.5 0 0 0 13 0C18.5 10.5 12 2.5 12 2.5z" fill="#2C7D8C"/><path d="M9 15.5a3 3 0 0 0 3 3" stroke="#fff" stroke-width="1.6" fill="none" stroke-linecap="round"/></svg>"""

html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Kavya Agrawal</title>
<meta name="description" content="Kavya Agrawal, PhD scholar at TERI School of Advanced Studies, New Delhi. Follow one drop of water from orbit to a village tap through her research on groundwater contamination, remote sensing and machine learning.">
<meta property="og:title" content="Kavya Agrawal">
<meta property="og:description" content="Groundwater, remote sensing and machine learning: follow one drop of water from orbit to a village tap.">
<meta property="og:image" content="https://kavyaagrawal-02.github.io/new/assets/img/scene-true.jpg">
<link rel="icon" href="assets/img/favicon-32.png" sizes="32x32">
<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,500;12..96,600;12..96,700;12..96,800&family=Caveat:wght@500&family=Literata:ital,opsz,wght@0,7..72,400;0,7..72,500;1,7..72,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/journey.css">
</head>
<body>
<a class="skip" href="#glacier">Skip to content</a>

<header class="bar">
  <a class="me" href="#orbit">Kavya Agrawal</a>
  <nav aria-label="Stages of the journey"><ol>
    <li><a href="#orbit">Orbit</a></li><li><a href="#glacier">Glacier</a></li><li><a href="#river">River</a></li>
    <li><a href="#ground">Ground</a></li><li><a href="#tap">Tap</a></li><li><a href="#sky">Sky</a></li>
  </ol></nav>
</header>

<a class="plain-btn" href="cv.html">{DROP_ICON}Read the plain CV</a>

<div class="drop-meter" aria-hidden="true">
  <svg viewBox="0 0 30 42">
    <defs><clipPath id="dropclip"><path d="M15 2c0 0-12 15-12 24a12 12 0 0 0 24 0C27 17 15 2 15 2z"/></clipPath></defs>
    <rect id="drop-fill" x="0" y="40" width="30" height="1" fill="#2C7D8C" clip-path="url(#dropclip)"/>
    <path d="M15 2c0 0-12 15-12 24a12 12 0 0 0 24 0C27 17 15 2 15 2z" fill="none" stroke="currentColor" stroke-width="2"/>
  </svg>
  <span class="txt"><span class="stage">Orbit</span><span class="depth">705 km up</span></span>
</div>

<main>
<!-- 0 ORBIT -->
<section id="orbit" data-stage="Orbit" data-depth="705 km up" data-tone="dark" data-bg="#08131C" aria-label="Introduction">
  <div class="orbit-pin">
    <canvas id="scene" aria-label="Illustrative satellite scene of mountains, a river and farmland, which sharpens as you scroll from coarse to fine resolution" role="img"></canvas>
    <div class="orbit-shade"></div>
    <div class="orbit-text"><div class="wrap">
      <h1>Kavya<br>Agrawal</h1>
      <p class="role">PhD scholar in groundwater, remote sensing and machine learning</p>
      <p>I use satellites and machine learning to predict where groundwater in India is unsafe to drink, and who is drinking it. I'm doing my PhD at the TERI School of Advanced Studies, New Delhi.</p>
      <p class="hint">Scroll down to zoom in from orbit and follow one drop of water.</p>
    </div></div>
    <div class="bands" role="group" aria-label="Satellite band">
      <button type="button" data-band="true" aria-pressed="true">True colour</button>
      <button type="button" data-band="false" aria-pressed="false">False colour</button>
      <button type="button" data-band="thermal" aria-pressed="false">Thermal</button>
    </div>
    <div class="readout" aria-live="off">
      <span class="px">111 km</span>
      <span class="ds">GRACE, water storage</span>
      <span class="note">Pixel size. Illustrative scene, not real data.</span>
    </div>
    <p class="orbit-end">Ground level. Now follow one drop of water, from the mountains to a village tap.</p>
  </div>
</section>

<!-- 1 GLACIER -->
<section id="glacier" data-stage="Glacier" data-depth="5,000 m up" data-tone="light" data-bg="#E9F2F4">
  {RIDGE}
  <div class="wrap">
    <p class="stage-name">1. Where the drop begins</p>
    <h2>Snow, ice and mountain heat</h2>
    <div class="glacier-grid">
      <div>
        <p>Most of the water in North India's rivers starts as snow and ice in the Himalaya. That's where my research started too: measuring how fast the mountains are warming, and where the ground stays frozen.</p>
        <div class="paper-card">
          <span class="kind">Published, Journal of Mountain Science, 2023</span>
          <h3>Evaluating spatial and elevation-wise daytime/nighttime LST trends across the Indus River Basin</h3>
          <p>Mal, S., <strong>Agrawal, K.</strong>, Rani, S. et al. <em>J. Mt. Sci.</em> 20, 3154–3172.</p>
          <p><a href="https://doi.org/10.1007/s11629-023-8157-8">Read the paper (doi.org/10.1007/s11629-023-8157-8)</a></p>
        </div>
        <ul class="ice-list">
          <li><strong>Permafrost in the Indus Basin.</strong> Identifying and mapping frozen ground from about twenty years of air temperature, solar radiation, snow and precipitation estimates in Google Earth Engine.</li>
          <li><strong>Snow cover in Indian basins.</strong> How snow cover is changing across the country's river basins.</li>
        </ul>
        <p class="someday">Someday: permafrost, glaciers and ice across High Mountain Asia, the Arctic and Antarctica.</p>
      </div>
      <figure class="glacier-fig" style="margin:0">
        <img src="assets/img/indus-study-area.png" alt="Study area map of the Indus River Basin with elevation, rivers and major cities" loading="lazy">
        <figcaption>The Indus River Basin, study area of the 2023 paper.</figcaption>
      </figure>
    </div>
  </div>
</section>

<!-- 2 RIVER -->
<section id="river" data-stage="River" data-depth="Down in the plains" data-tone="light" data-bg="#DCE8E2">
  {RIVER_SVG}
  <div class="wrap">
    <div class="intro">
      <p class="stage-name">2. Downstream</p>
      <h2>Towns along the way</h2>
      <p>The drop flows down through the plains of Uttar Pradesh to Delhi, the same way I did. Each stop is a postcard from a school or university.</p>
    </div>
    <p class="flip-hint">Tap a postcard to turn it over.</p>
    <ol class="cards" style="padding:0;margin-top:1.5rem">
      {"".join(postcard(c) for c in CARDS)}
    </ol>
  </div>
</section>

<!-- 3 GROUND -->
<section id="ground" data-stage="Ground" data-depth="Below the water table" data-tone="dark" data-bg="#5E4A30">
  <div class="wrap">
    <p class="stage-name lead">3. Into the ground</p>
    <h2 class="lead">What the drop picks up</h2>
    <p class="lead">As water seeps down through soil and rock it dissolves minerals. Some of them are harmful. My PhD, <em>Development of an Adaptable Machine Learning Based Framework for Multi-Contaminant Prediction</em>, predicts where across India groundwater carries too much uranium, fluoride or arsenic. It combines groundwater samples with satellite, climate, terrain, soil and population data.</p>
    <p class="lead" style="font-size:.98rem;opacity:.85">Supervisor: Prof. Chander Kumar Singh. Co-supervisor: Dr. Adwitiya Sinha.</p>

    <div class="watertable"><span>Water table</span></div>

    <h3 style="font-size:1.6rem">Sampling stations</h3>
    <p>Each line of my research, labelled like a water sample.</p>
    <div class="stations">
      <article class="label" style="--c:var(--u)">
        <div class="row1"><span>Station U-01</span><span class="status award">Best Paper Award 2026</span></div>
        <div class="el"><b>U</b><h3>Uranium in groundwater throughout India</h3></div>
        <p>A national-scale AutoML model of where uranium occurs, turned into maps of risk, population exposure and groundwater governance priority.</p>
        <dl><dt>Method</dt><dd>AutoGluon ensemble, independent validation</dd><dt>Status</dt><dd><span class="status">Submitted to journal</span></dd></dl>
      </article>
      <article class="label" style="--c:var(--f)">
        <div class="row1"><span>Station F-02</span><span>2026</span></div>
        <div class="el"><b>F</b><h3>Fluoride and spatial resolution</h3></div>
        <p>Benchmarking deep learning models for India-wide fluoride prediction, and testing how the resolution of predictors (native, 500 m, 1 km, 5 km) changes the answer.</p>
        <dl><dt>Threshold</dt><dd>1.5 mg/L</dd><dt>Status</dt><dd><span class="status">In progress</span></dd></dl>
      </article>
      <article class="label" style="--c:var(--as)">
        <div class="row1"><span>Station As-03</span><span>2024–25</span></div>
        <div class="el"><b>As</b><h3>Arsenic in the Middle Gangetic Plain</h3></div>
        <p>Distribution, speciation and controls on arsenic mobilisation, with pH, iron, redox potential and sulfate as key factors.</p>
        <dl><dt>Shared at</dt><dd>As2024 congress, Bhubaneswar</dd><dt>Status</dt><dd><span class="status">Presented</span></dd></dl>
      </article>
      <article class="label" style="--c:var(--ds)">
        <div class="row1"><span>Station DS-04</span><span>2026</span></div>
        <div class="el"><b>↕</b><h3>Downscaling satellite predictors</h3></div>
        <p>A physically informed way to move environmental data between coarse and fine resolutions without faking detail, piloted on CHIRPS rainfall over Punjab.</p>
        <dl><dt>Checks</dt><dd>Moran's I, semivariograms, aggregation consistency</dd><dt>Status</dt><dd><span class="status">In progress</span></dd></dl>
      </article>
    </div>

    <h3 style="font-size:1.6rem;margin-top:4rem">Borehole log: my toolkit</h3>
    <div class="borehole">
      <div class="core" aria-hidden="true">
        <div style="background:#C2A878"></div><div style="background:#9C8358"></div><div style="background:#6F7A6A"></div><div style="background:#3D6670"></div>
      </div>
      <ol class="layers">
        <li><h3>Earth observation and GIS</h3><p>Google Earth Engine (JavaScript), ArcGIS Pro, QGIS, ERDAS Imagine. Landsat, Sentinel, MODIS, VIIRS, SRTM, GRACE, CHIRPS, ERA5-Land and more.</p></li>
        <li><h3>Machine learning</h3><p>Python and pandas, AutoGluon, LightGBM, Random Forest, deep learning, SHAP and LIME for explaining models.</p></li>
        <li><h3>Spatial statistics</h3><p>Mann–Kendall and Theil–Sen trends, time-series modelling, Moran's I, semivariograms, independent validation.</p></li>
        <li><h3>Careful data</h3><p>Provenance tracking, duplicate and sentinel-value audits, coordinate checks, resolution harmonisation, never silently dropping an observation.</p></li>
      </ol>
    </div>

    <h3 style="font-size:1.6rem;margin-top:4rem">Papers</h3>
    <ul class="papers">
      <li><span class="yr">2023</span><div><h3>Evaluating spatial and elevation-wise daytime/nighttime LST trends across the Indus River Basin. <em>Journal of Mountain Science</em>.</h3></div></li>
      <li><span class="yr">Submitted</span><div><h3>Predicting Uranium Occurrences in Groundwater throughout India.</h3></div></li>
      <li><span class="yr">In progress</span><div><h3>Comparing and Benchmarking Deep Learning Models for Predicting Groundwater Contamination caused by Fluoride with the effects of Spatial Resolution on Prediction.</h3></div></li>
      <li><span class="yr">In progress</span><div><h3>A Physically Informed Framework for Multi-Resolution Downscaling and Upscaling of Environmental Predictors (Satellite Data).</h3></div></li>
    </ul>
  </div>
</section>

<!-- 4 TAP -->
<section id="tap" data-stage="Tap" data-depth="At the surface" data-tone="light" data-bg="#E4E9E1">
  <div class="wrap">
    <p class="stage-name">4. At the tap</p>
    <h2>Who drinks it, and what to do about it</h2>
    <div class="tap-grid">
      <div class="tap-art">{TAP_SVG}</div>
      <div>
        <div class="tap-block">
          <p>A contamination map matters only once it reaches the people who drink the water and the people who manage it. So my models end in estimates of population exposure and indicators of where groundwater governance should act first.</p>
        </div>
        <div class="tap-block">
          <h3 style="font-size:1.6rem;margin-bottom:.6rem">Teaching</h3>
          <div class="course"><span class="when">Jun–Dec 2026</span><div><h3>Principles of GIS and GNSS (NRG176)</h3><p>MSc Geoinformatics, TERI SAS. 4 credits, 60 hours.</p></div></div>
          <div class="course"><span class="when">Jun–Dec 2026</span><div><h3>Principles of Remote Sensing (NRG169)</h3><p>MSc Geoinformatics, TERI SAS. 4 credits, 60 hours.</p></div></div>
          <div class="course"><span class="when">Jul–Dec 2025</span><div><h3>Principles of Remote Sensing (NRG169)</h3><p>Taught the 32 hours of practical lab sessions.</p></div></div>
        </div>
        <div class="tap-block">
          <h3 style="font-size:1.6rem;margin-bottom:.2rem">Sharing it further</h3>
          <ul class="roles">
            <li><b>Rapporteur</b>, National Workshop on Geospatial Technology for Climate Action, TERI SAS with NRSC, ISRO, 2026</li>
            <li><b>Rapporteur</b>, Ministerial Session and High-Level Plenary, World Sustainable Development Summit 2025</li>
            <li><b>Delegate</b>, World Sustainable Development Summit 2026</li>
            <li><b>Facilitator and judge</b>, Programme LEAD 2026, Sustainable City Design Challenge</li>
            <li><b>Judge</b>, TERI SAS Sustainability Hackathon 2025</li>
            <li><b>Judge</b>, KnoxCode 2025 Geospatial Innovation Challenge</li>
          </ul>
          <p style="margin-top:1rem"><a href="cv.html#rapporteur">All rapporteurship, summits, training and lectures in the plain CV</a></p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- 5 SKY -->
<section id="sky" data-stage="Sky" data-depth="Evaporating" data-tone="light" data-bg="#EEF5F8">
  <div class="wrap">
    <p class="stage-name">5. Back into the air</p>
    <h2>And the cycle starts again</h2>

    <div class="sky-block">
      <h3 style="font-size:1.6rem">Awards</h3>
      <div class="vapour">
        <div class="bubble big"><span class="yr">2026</span><h3>First Position and Best Paper Award</h3><p>ICSSR EHP NEXUS 2026, Gautam Buddha University</p></div>
        <div class="bubble"><span class="yr">2025</span><h3>2nd rank, Map Making Competition</h3><p>Amity University</p></div>
        <div class="bubble"><span class="yr">2018</span><h3>State Child Scientist Award</h3><p>National Science Congress</p></div>
        <div class="bubble"><span class="yr">2015–2018</span><h3>Top 3 in English Olympiads, four years running</h3><p>British Olympiad Foundation</p></div>
        <div class="bubble"><span class="yr">2016, 2018</span><h3>Merit Awards</h3><p>And 20 cultural and general knowledge awards, including prizes in dance</p></div>
      </div>
    </div>

    <div class="sky-block">
      <h3 style="font-size:1.6rem">Talks, postmarked</h3>
      <ul class="marks">{"".join(talk(*t) for t in TALKS)}</ul>
    </div>

    <div class="sky-block">
      <h3 style="font-size:1.6rem">Off the map</h3>
      <ul class="hobbies">
        <li>collecting old coins</li><li>and stamps</li><li>historic stories</li><li>photography</li><li>travelling</li><li>badminton</li><li>dance</li><li>writing</li>
      </ul>
    </div>

    <div class="contact">
      <div>
        <h3 style="font-size:1.6rem">Say hello</h3>
        <p style="margin:.4rem 0 0">Department of Natural &amp; Applied Sciences, TERI School of Advanced Studies, Vasant Kunj Institutional Area, New Delhi 110070</p>
        <ul>
          <li><a href="{LINKS['email']}">kavya.agrawal@terisas.ac.in</a></li>
          <li><a href="{LINKS['scholar']}">Google Scholar</a></li>
          <li><a href="{LINKS['orcid']}">ORCID</a></li>
          <li><a href="{LINKS['researchgate']}">ResearchGate</a></li>
          <li><a href="{LINKS['linkedin']}">LinkedIn</a></li>
          <li><a href="{LINKS['github']}">GitHub</a></li>
        </ul>
      </div>
      <button class="coin" type="button" aria-label="Back to the top">
        <span class="c-inner"><span class="side a"><span>₹</span><small>KAVYA</small></span><span class="side b">Back to<br>orbit</span></span>
      </button>
    </div>
    <p class="foot-note">The opening satellite scene is generated for illustration and does not show a real place.</p>
  </div>
</section>
</main>
<script src="assets/journey.js"></script>
</body>
</html>
"""
(OUT / "index.html").write_text(html, encoding="utf-8")
print("journey built")
