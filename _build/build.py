"""Builds the seven HTML 'sheets' of Kavya Agrawal's site.
Run:  python3 _build/build.py   (from the site folder)
Content lives in this file; the shared frame (header, index to sheets, footer) is added to every page."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

PAGES = [  # file, nav label, sheet title, grid position (row, col)
    ("index.html", "Home", "Home", (1, 1)),
    ("research.html", "Research", "Research", (0, 0)),
    ("publications.html", "Publications & talks", "Publications", (0, 1)),
    ("teaching.html", "Teaching", "Teaching", (0, 2)),
    ("projects.html", "Projects", "Projects", (1, 0)),
    ("experience.html", "Engagement", "Engagement", (1, 2)),
    ("cv.html", "CV", "CV", (2, 1)),
]
SEA = {(2, 0): "Arabian Sea", (2, 2): "Bay of Bengal"}

TICKS = """<div class="ticks" aria-hidden="true">
  <span class="t-top" style="left:8%">77°00′E</span><span class="t-top" style="left:36%">77°05′E</span>
  <span class="t-top" style="left:64%">77°10′E</span><span class="t-top" style="left:90%">77°15′E</span>
  <span class="t-left" style="top:12%">28°35′N</span><span class="t-left" style="top:48%">28°32′N</span><span class="t-left" style="top:84%">28°29′N</span>
</div>"""

LINKS = {
    "email": "mailto:kavya.agrawal@terisas.ac.in",
    "linkedin": "https://www.linkedin.com/in/kavya-agrawal02/",
    "scholar": "https://scholar.google.com/citations?user=yXQUQ6YAAAAJ&hl=en",
    "orcid": "https://orcid.org/0009-0009-1032-2541",
    "researchgate": "https://www.researchgate.net/profile/Kavya-Agrawal-4",
    "github": "https://github.com/kavyaagrawal-02",
}

PROFILE_LINKS = f"""<a href="{LINKS['email']}">kavya.agrawal@terisas.ac.in</a>
<a href="{LINKS['scholar']}">Google Scholar</a>
<a href="{LINKS['orcid']}">ORCID</a>
<a href="{LINKS['researchgate']}">ResearchGate</a>
<a href="{LINKS['linkedin']}">LinkedIn</a>
<a href="{LINKS['github']}">GitHub</a>"""


def nav(current):
    cur = ' aria-current="page"'
    return "".join(
        f'<li><a href="{f}"{cur if f == current else ""}>{label}</a></li>'
        for f, label, _, _ in PAGES)


def index_grid(current):
    cells = {pos: (f, t, i + 1) for i, (f, _, t, pos) in enumerate(PAGES)}
    out = []
    for r in range(3):
        for c in range(3):
            if (r, c) in cells:
                f, t, n = cells[(r, c)]
                cur = ' aria-current="page"' if f == current else ""
                out.append(f'<a href="{f}"{cur}><small>Sheet {n}</small>{t}</a>')
            else:
                out.append(f'<span class="sea" aria-hidden="true">{SEA[(r, c)]}</span>')
    return "".join(out)


def page(fname, title, description, body, band=None):
    n = [p[0] for p in PAGES].index(fname) + 1
    band_html = ""
    if band:
        sheet_title, lede = band
        band_html = f"""<header class="band">
  <img src="assets/contours-band.svg" alt="">
  <div class="band-inner">
    <p class="sheet-no">Sheet {n} of {len(PAGES)}</p>
    <h1>{sheet_title}</h1>
    <p class="lede">{lede}</p>
  </div>
</header>"""
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:image" content="https://kavyaagrawal-02.github.io/assets/img/kavya-portrait-hero.jpg">
<meta name="author" content="Kavya Agrawal">
<link rel="icon" href="assets/img/favicon-32.png" sizes="32x32">
<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Alegreya+Sans:ital,wght@0,400;0,500;0,700;1,400&family=IM+Fell+English:ital@0;1&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
<script>try{{var t=localStorage.getItem('theme');if(t)document.documentElement.dataset.theme=t;}}catch(e){{}}</script>
</head>
<body>
<a class="skip" href="#content">Skip to content</a>
<div class="sheet">
{TICKS}
<div class="mast">
  <a class="name" href="index.html">Kavya Agrawal</a>
  <nav aria-label="Sheets"><ul>{nav(fname)}</ul></nav>
  <button class="theme-btn" type="button" id="theme">Dark map</button>
</div>
{band_html}
<main id="content">
{body}
</main>
<footer class="foot">
  <div class="index">
    <h2>Index to sheets</h2>
    <div class="index-grid">{index_grid(fname)}</div>
  </div>
  <div class="colophon">
    <p><strong>Kavya Agrawal</strong>, PhD scholar, Department of Natural &amp; Applied Sciences, TERI School of Advanced Studies, Vasant Kunj Institutional Area, New Delhi 110070, India.</p>
    <p class="contact-line">{PROFILE_LINKS}</p>
    <p class="scale"><i aria-hidden="true"></i> Compiled and surveyed by the author, 2026</p>
  </div>
</footer>
</div>
<script>
(function(){{var b=document.getElementById('theme'),r=document.documentElement;
function dark(){{return r.dataset.theme?r.dataset.theme==='dark':matchMedia('(prefers-color-scheme: dark)').matches;}}
function label(){{b.textContent=dark()?'Paper map':'Dark map';}}
label();b.addEventListener('click',function(){{r.dataset.theme=dark()?'light':'dark';try{{localStorage.setItem('theme',r.dataset.theme);}}catch(e){{}}label();}});}})();
</script>
</body>
</html>
"""
    (ROOT / fname).write_text(html, encoding="utf-8")


def entry(when, title, sym=None, where="", note="", tags=()):
    s = f'<span class="sym {sym}" aria-hidden="true"></span>' if sym else ""
    t = "".join(f'<span class="tag{" red" if r else ""}">{x}</span> ' for x, r in tags)
    w = f'<p class="where">{where}</p>' if where else ""
    nt = f"<p>{note}</p>" if note else ""
    tg = f"<div>{t}</div>" if t else ""
    return f'<li class="entry"><div class="when">{when}</div><div class="what"><h3>{s}<span>{title}</span></h3>{w}{nt}{tg}</div></li>'


LEGEND = """<div class="legend">
  <h2>Legend</h2>
  <ul>
    <li><span class="sym pub" aria-hidden="true"></span> Published</li>
    <li><span class="sym sub" aria-hidden="true"></span> Submitted, under review</li>
    <li><span class="sym prog" aria-hidden="true"></span> In progress</li>
    <li><span class="sym award" aria-hidden="true"></span> Award</li>
    <li><span class="sym teach" aria-hidden="true"></span> Teaching</li>
  </ul>
</div>"""

# ------------------------------------------------------------------ HOME
NEWS = [
    ("Jun 2026", "Teaching <em>Principles of Remote Sensing</em> (NRG169) and <em>Principles of GIS and GNSS</em> (NRG176) in the MSc Geoinformatics programme, July–December 2026.", "teach"),
    ("Apr 2026", "First Position (oral presentation) and Best Paper Award at ICSSR EHP NEXUS 2026, Gautam Buddha University, for work on machine-learning-based uranium risk assessment.", "award"),
    ("Mar 2026", "Rapporteur at the National Workshop on Geospatial Technology for Climate Action, Sustainability and Disaster Risk Reduction (TERI SAS with NRSC, ISRO).", None),
    ("Feb 2026", "Delegate at the World Sustainable Development Summit 2026, Silver Jubilee edition.", None),
    ("Jan 2026", "Completed the PhD comprehensive examination. Submitted the paper <em>Predicting Uranium Occurrences in Groundwater throughout India</em>.", "sub"),
]
news = "".join(
    f'<li class="highlight"><span class="sym {s}" aria-hidden="true"></span><div><span class="when water-label">{d}</span><p style="margin:.1rem 0 0">{t}</p></div></li>'
    if s else
    f'<li class="highlight"><span aria-hidden="true"></span><div><span class="when water-label">{d}</span><p style="margin:.1rem 0 0">{t}</p></div></li>'
    for d, t, s in NEWS)

home = f"""
<section class="hero" aria-label="Introduction">
  <div class="hero-text">
    <p class="sheet-no">Sheet 1 of 7</p>
    <h1>Kavya Agrawal</h1>
    <p class="role">PhD scholar in groundwater, remote sensing and machine learning</p>
    <p>I study where groundwater becomes unsafe to drink, and why. My doctoral research at the TERI School of Advanced Studies, New Delhi, builds national-scale models that predict uranium, fluoride and arsenic contamination across India from satellite, climate, terrain and hydrochemical data, then turns those predictions into maps of risk, exposure and governance priority.</p>
    <p>I trained as a geographer and still think in maps. Before groundwater I worked on land surface temperature trends in the Indus River Basin, permafrost and snow cover, and urban land use in Delhi.</p>
    <p class="muted" style="font-size:1rem">Supervised by Prof. Chander Kumar Singh, co-supervised by Dr. Adwitiya Sinha.</p>
    <p class="contact-line">{PROFILE_LINKS}</p>
  </div>
  <figure class="plate" style="margin:0">
    <img src="assets/contours-plate.svg" alt="">
    <img class="photo" src="assets/img/kavya-portrait-hero.jpg" alt="Portrait of Kavya Agrawal">
  </figure>
</section>

<div class="cols">
  <div>
    <section>
      <h2>News</h2>
      <ul class="entries" style="list-style:none;padding:0;margin:0">{news}</ul>
    </section>
  </div>
  <aside>
    {LEGEND}
    <div class="legend">
      <h2>Research keywords</h2>
      <p class="keywords" style="margin:0"><span>groundwater quality</span><span>uranium</span><span>fluoride</span><span>arsenic</span><span>population exposure</span><span>groundwater governance</span><span>Google Earth Engine</span><span>AutoML</span><span>explainable AI</span><span>downscaling</span><span>cryosphere</span></p>
    </div>
  </aside>
</div>

<section>
  <h2>Where to go next</h2>
  <div class="routes">
    <a class="route" href="research.html"><span class="num">Sheet 2</span><h3>Research</h3><p>The contamination framework, the three contaminants, and the data scales I work across.</p></a>
    <a class="route" href="publications.html"><span class="num">Sheet 3</span><h3>Publications &amp; talks</h3><p>Papers, manuscripts under review and conference presentations.</p></a>
    <a class="route" href="cv.html"><span class="num">Sheet 7</span><h3>Full CV</h3><p>Education, awards, service and everything else, on one printable page.</p></a>
  </div>
</section>
"""
page("index.html", "Kavya Agrawal, PhD scholar",
     "Kavya Agrawal, PhD scholar at TERI School of Advanced Studies, New Delhi: groundwater contamination, remote sensing, GIS and machine learning.",
     home)

# ------------------------------------------------------------------ RESEARCH
DATASETS = [  # name, native resolution in metres
    ("SRTM", 30), ("JRC Surface Water", 30), ("MERIT Hydro", 93), ("GHSL Built", 100),
    ("OpenLandMap soils", 232), ("MODIS LST, NDVI", 927), ("GPW population", 1000),
    ("TerraClimate", 4638), ("CHIRPS", 5566), ("ERA5-Land", 11132), ("GLDAS", 27830), ("GRACE", 111319),
]


def scalebar():
    import math
    W, L, R = 1000, 40, 960
    lo, hi = math.log10(10), math.log10(200000)
    x = lambda m: L + (math.log10(m) - lo) / (hi - lo) * (R - L)
    parts = []
    # alternating segments per decade
    decades = [10, 100, 1000, 10000, 100000, 200000]
    for i in range(len(decades) - 1):
        cls = "bar-a" if i % 2 == 0 else "bar-b"
        parts.append(f'<rect class="{cls}" x="{x(decades[i]):.1f}" y="150" width="{x(decades[i+1]) - x(decades[i]):.1f}" height="12"/>')
    for m, lab in [(10, "10 m"), (100, "100 m"), (1000, "1 km"), (10000, "10 km"), (100000, "100 km")]:
        parts.append(f'<text class="unit" x="{x(m):.1f}" y="185" text-anchor="middle">{lab}</text>')
    for i, (name, m) in enumerate(DATASETS):
        up = i % 2 == 0
        level = (i // 2) % 3
        ty = (30 + level * 34) if up else (215 + level * 26)
        y1, y2 = (ty + 6, 150) if up else (162, ty - 14)
        parts.append(f'<line class="lead" x1="{x(m):.1f}" y1="{y1}" x2="{x(m):.1f}" y2="{y2}"/>')
        parts.append(f'<circle class="dot" cx="{x(m):.1f}" cy="{150 if up else 162}" r="3.5"/>')
        parts.append(f'<text x="{x(m):.1f}" y="{ty}" text-anchor="middle">{name}</text>')
    return f'<div class="scalebar"><svg viewBox="0 0 {W} 290" role="img" aria-label="Logarithmic scale bar showing the native resolution of each dataset, from SRTM at 30 metres to GRACE at about 111 kilometres">{"".join(parts)}</svg></div>'


research = f"""
<div class="cols">
<div>
<section>
  <h2>The doctoral framework</h2>
  <p>My PhD, <em>Development of an Adaptable Machine Learning Based Framework for Multi-Contaminant Prediction</em>, asks how far we can predict groundwater contamination across a country as large and varied as India, and what those predictions mean for the people who drink the water.</p>
  <p>The framework joins groundwater observations and hydrochemistry with remote sensing and GIS layers on climate, hydrology, terrain, soil, geology, land use, human modification and population. Machine learning, deep learning and automated machine learning do the prediction; spatial statistics, independent validation and explainable AI check whether the predictions hold up and make physical sense.</p>
</section>

<section>
  <h2>Three contaminants</h2>
  <div class="contaminants">
    <div class="well">
      <div class="el">U<small>uranium</small></div>
      <p>Predicting where uranium occurs in groundwater throughout India with AutoML, then mapping risk, population exposure and groundwater governance priority for decision support.</p>
      <span class="tag">Submitted to journal</span> <span class="tag red">Best Paper Award 2026</span>
    </div>
    <div class="well">
      <div class="el">F<small>fluoride</small></div>
      <p>Benchmarking deep learning models for India-wide fluoride prediction, and testing how spatial resolution (native, 500 m, 1 km, 5 km) changes what a model can see.</p>
      <span class="tag">In progress</span>
    </div>
    <div class="well">
      <div class="el">As<small>arsenic</small></div>
      <p>Distribution, speciation and controls on arsenic mobilisation in aquifers of the Middle Gangetic Plain, including the roles of pH, iron, redox potential and sulfate.</p>
      <span class="tag">Presented at As2024</span>
    </div>
  </div>
</section>

<section>
  <h2>Scales I work across</h2>
  <p>Contamination models draw on Earth observation data recorded at very different resolutions. Part of my work is aggregating them honestly to a common grid without quietly losing groundwater observations. These are the native resolutions of some of the datasets in the fluoride predictor stack.</p>
  {scalebar()}
</section>

<section>
  <h2>Downscaling environmental predictors</h2>
  <p>A related paper in progress builds <em>a physically informed framework for multi-resolution downscaling and upscaling of environmental predictors</em> from satellite data. A pilot on CHIRPS precipitation over Punjab (2013–2022) uses sub-pixel fractions and conservation-based aggregation to separate genuine spatial downscaling from simple resampling, checked against Moran's I, semivariograms and aggregation consistency.</p>
</section>

<section>
  <h2>Earlier work: mountains and ice</h2>
  <p>Before groundwater, I worked on the cryosphere and climate of the Himalaya and Indus Basin: daytime and nighttime land surface temperature trends by elevation (published in the <em>Journal of Mountain Science</em>, 2023), identifying and mapping permafrost in the Indus Basin from roughly twenty years of MAAT, PISR, BMAT, snow and precipitation estimates in Google Earth Engine, and snow cover change in Indian basins.</p>
</section>

<section>
  <h2>Tools and methods</h2>
  <div class="toolset">
    <div><h3>Earth observation &amp; GIS</h3><ul><li>Google Earth Engine (JavaScript)</li><li>ArcGIS Pro, QGIS</li><li>ERDAS Imagine</li><li>DEM processing, orthorectification, mosaicking</li><li>Landsat, Sentinel, MODIS, VIIRS</li></ul></div>
    <div><h3>Modelling</h3><ul><li>Python, pandas</li><li>AutoGluon (AutoML)</li><li>LightGBM, Random Forest</li><li>Deep learning</li><li>SHAP and LIME</li></ul></div>
    <div><h3>Spatial statistics</h3><ul><li>Mann–Kendall and Theil–Sen trends</li><li>Time-series modelling</li><li>Moran's I, semivariograms</li><li>Independent validation</li></ul></div>
    <div><h3>Data care</h3><ul><li>Provenance and data lineage</li><li>Duplicate and sentinel-value audits</li><li>Coordinate and geometry checks</li><li>Resolution harmonisation</li></ul></div>
  </div>
</section>
</div>
<aside>
  <div class="legend">
    <h2>Data on the map</h2>
    <ul>
      <li><span class="water-label">CHIRPS, ERA5-Land, TerraClimate</span></li>
      <li><span class="water-label">GLDAS, GRACE</span></li>
      <li><span class="water-label">MERIT Hydro, JRC Surface Water</span></li>
      <li><span class="water-label">SRTM, OpenLandMap soils</span></li>
      <li><span class="water-label">GHSL, GPW, Human Modification</span></li>
      <li><span class="water-label">CGWB hydrochemistry</span></li>
    </ul>
  </div>
  <div class="legend">
    <h2>Questions I'd like to explore</h2>
    <ul class="plain" style="padding-left:1rem">
      <li style="display:list-item">Permafrost identification and modelling</li>
      <li style="display:list-item">Glacier, ice and snow mapping</li>
      <li style="display:list-item">High Mountain Asia, the Arctic and Antarctica</li>
      <li style="display:list-item">Remote sensing for history and archaeology</li>
    </ul>
  </div>
</aside>
</div>
"""
page("research.html", "Research, Kavya Agrawal",
     "National-scale prediction of groundwater uranium, fluoride and arsenic contamination in India using remote sensing, GIS and machine learning.",
     research, ("Research", "Predicting groundwater contamination across India, and what it means for the people who drink it."))

# ------------------------------------------------------------------ PUBLICATIONS
pubs = "".join([
    entry("Nov 2023", 'Evaluating spatial and elevation-wise daytime/nighttime LST trends across the Indus River Basin', "pub",
          "Mal, S., <strong>Agrawal, K.</strong>, Rani, S. et al. <em>Journal of Mountain Science</em> 20, 3154–3172.",
          '<a href="https://doi.org/10.1007/s11629-023-8157-8">doi.org/10.1007/s11629-023-8157-8</a>'),
])
manuscripts = "".join([
    entry("2025–26", "Predicting Uranium Occurrences in Groundwater throughout India", "sub", "Research paper, submitted to journal."),
    entry("2026", "Comparing and Benchmarking Deep Learning Models for Predicting Groundwater Contamination caused by Fluoride with the effects of Spatial Resolution on Prediction", "prog", "Research paper in progress."),
    entry("2026", "A Physically Informed Framework for Multi-Resolution Downscaling and Upscaling of Environmental Predictors (Satellite Data)", "prog", "Research paper in progress."),
])
talks = "".join([
    entry("Apr 2026", "Machine-Learning-Based Uranium Risk Assessment, Population Exposure and Groundwater Governance", "award",
          "ICSSR EHP NEXUS 2026, Track 10: AI and Predictive Analytics, Gautam Buddha University, 27–28 April 2026.", "",
          (("First Position, oral presentation", True), ("Best Paper Award", True))),
    entry("Oct 2024", "Distribution, Speciation and Controls on As Mobilization in the Groundwater in Aquifers of the Middle Gangetic Plain, India", "prog",
          "9th International Congress &amp; Exhibition on Arsenic in the Environment (As2024), KIIT Deemed to be University, Bhubaneswar, 20–24 October 2024."),
    entry("Nov 2022", "Problems and Prospects of Delhi's Drinking Water Supply", None,
          "IGU Thematic Conference on Sustainability, Future Earth and Humanities, Department of Geography, Central University of Haryana, 24–25 November 2022."),
    entry("Jul 2022", "Educational Relevance of Ramayana in Modern India", None,
          "National Seminar on Promoting Human Values and Culture for Peaceful Co-Existence, Amity University Haryana (sponsored by ICPR), 22 July 2022."),
    entry("May 2022", "Digital Enhancement of Physical Space and Connective Turn in Tourism Industry during and Post-COVID-19 Period", None,
          "International Conference on Geography and the Digital: Intersections and Conflations, Delhi School of Economics, University of Delhi, 23–25 May 2022."),
    entry("May 2022", "Migrant College Students during Covid Pandemic: Evidence from the Field", None,
          "Jamia International Conference on Education 2022, Faculty of Education, Jamia Millia Islamia, 6–8 May 2022."),
    entry("Apr 2022", "Migrant College Students during Covid Pandemic: Evidence from the Field", None,
          "International Conference on Challenges to Disaster Risk Reduction and Resilient Habitat, Shaheed Bhagat Singh College, University of Delhi, 5–6 April 2022."),
]).replace('<span class="sym prog" aria-hidden="true"></span><span>Distribution', '<span>Distribution')

publications = f"""
<div class="cols">
<div>
<section>
  <h2>Journal articles</h2>
  <!-- To add a new paper: copy one <li class="entry"> ... </li> block below and edit it. Newest first. -->
  <ul class="entries">{pubs}</ul>
  <figure style="margin:1.6rem 0 0;max-width:640px">
    <img src="assets/img/lst-trends.png" alt="Figure from the paper: daytime and nighttime LST trends across the Indus River Basin" loading="lazy" style="border:1px solid var(--rule)">
    <figcaption class="muted" style="font-size:.95rem;margin-top:.5rem">Land surface temperature trends across the Indus River Basin, from the 2023 paper.</figcaption>
  </figure>
</section>
<section>
  <h2>Manuscripts</h2>
  <ul class="entries">{manuscripts}</ul>
</section>
<section>
  <h2>Conference presentations</h2>
  <ul class="entries">{talks}</ul>
</section>
</div>
<aside>{LEGEND}
  <div class="legend">
    <h2>Profiles</h2>
    <ul>
      <li><a href="{LINKS['scholar']}">Google Scholar</a></li>
      <li><a href="{LINKS['orcid']}">ORCID 0009-0009-1032-2541</a></li>
      <li><a href="{LINKS['researchgate']}">ResearchGate</a></li>
    </ul>
  </div>
</aside>
</div>
"""
page("publications.html", "Publications and talks, Kavya Agrawal",
     "Journal articles, manuscripts and conference presentations by Kavya Agrawal.",
     publications, ("Publications &amp; talks", "Papers, work under review and conference presentations, newest first."))

# ------------------------------------------------------------------ TEACHING
teaching_entries = "".join([
    entry("Jul–Dec 2026", "Principles of GIS and GNSS (NRG176)", "teach", "MSc Geoinformatics, TERI School of Advanced Studies",
          "4 credits, 60 hours (lecture–tutorial–practical 42–2–32)."),
    entry("Jul–Dec 2026", "Principles of Remote Sensing (NRG169)", "teach", "MSc Geoinformatics, TERI School of Advanced Studies",
          "4 credits, 60 hours (lecture–tutorial–practical 42–2–32)."),
    entry("Jul–Dec 2025", "Principles of Remote Sensing (NRG169)", "teach", "MSc Geoinformatics, TERI School of Advanced Studies",
          "Taught the practical component: 32 hours of hands-on lab sessions."),
])
teaching = f"""
<div class="cols">
<div>
<section>
  <h2>Courses</h2>
  <ul class="entries">{teaching_entries}</ul>
</section>
<section>
  <h2>In the lab</h2>
  <p>Practical sessions take students from the satellite to the map: GPS and GNSS fieldwork, georeferencing, working with Landsat 8 and 9 imagery in ArcGIS Pro and ERDAS Imagine, and applied exercises on urban patterns, vegetation and geomorphology.</p>
  <figure style="margin:1.4rem 0 0;max-width:680px">
    <img src="assets/img/delhi-lulc.png" alt="Land use and land cover classification map of South West Delhi from Landsat 8, October 2019" loading="lazy" style="border:1px solid var(--rule)">
    <figcaption class="muted" style="font-size:.95rem;margin-top:.5rem">Land use and land cover of South West Delhi from Landsat 8, October 2019: an example of the classification work students learn to do.</figcaption>
  </figure>
</section>
</div>
<aside>
  <div class="legend">
    <h2>Geography I studied</h2>
    <ul class="plain" style="padding-left:1rem;font-size:.95rem">
      {"".join(f'<li style="display:list-item">{s}</li>' for s in ["Geomorphology","Climatology &amp; oceanography","Cartographic techniques","Thematic cartography","Remote sensing &amp; GIS","Statistical methods in geography","Fieldwork &amp; research methodology","Geography of India","Human, social &amp; political geography","Economic &amp; agricultural geography","Population &amp; settlement geography","Environmental geography","Disaster management","Regional planning &amp; development","History of geographical thought"])}
    </ul>
  </div>
</aside>
</div>
"""
page("teaching.html", "Teaching, Kavya Agrawal", "Courses Kavya Agrawal teaches in the MSc Geoinformatics programme at TERI SAS.",
     teaching, ("Teaching", "Remote sensing, GIS and GNSS for MSc Geoinformatics students at TERI SAS."))

# ------------------------------------------------------------------ PROJECTS
def plist(items):
    return '<ul class="plain two-col">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"

projects = f"""
<section>
  <h2>Doctoral research, 2024 to now</h2>
  <ul class="entries">
    {entry("2026", "Fluoride and spatial resolution", "prog", "Deep learning benchmarks for India-wide fluoride prediction, with predictor stacks built at native, 500 m, 1 km and 5 km scales.")}
    {entry("2026", "Physically informed downscaling of satellite predictors", "prog", "Downscaling and upscaling environmental predictors while preserving their physical meaning.")}
    {entry("2025–26", "Uranium in groundwater throughout India", "sub", "National-scale AutoML prediction, risk classes, population exposure and groundwater governance indicators.")}
    {entry("2024–25", "Arsenic in the Middle Gangetic Plain", None, "Distribution, speciation and controls on arsenic mobilisation; presented at As2024.")}
  </ul>
</section>
<section>
  <h2>Earlier research</h2>
  <ul class="entries">
    {entry("2023", "Land surface temperature trends, Indus River Basin", "pub", "Spatial and elevation-wise daytime and nighttime LST trends with Google Earth Engine, ArcGIS and trend analysis. Published in the <em>Journal of Mountain Science</em>.")}
    {entry("2023", "Permafrost in the Indus Basin", None, "Identification and mapping from about twenty years of MAAT, PISR, BMAT, snow and precipitation estimates in Google Earth Engine.")}
    {entry("2023", "Snow cover and change in Indian basins", None, "")}
  </ul>
  <figure style="margin:1.6rem 0 0;max-width:620px">
    <img src="assets/img/indus-study-area.png" alt="Study area map of the Indus River Basin showing elevation, rivers and major cities" loading="lazy" style="border:1px solid var(--rule)">
    <figcaption class="muted" style="font-size:.95rem;margin-top:.5rem">Study area map of the Indus River Basin.</figcaption>
  </figure>
</section>
<section>
  <h2>Postgraduate projects, MA Geography, 2021–2023</h2>
  {plist(["Measuring the Problems and Emotions of Urban-Ward Migrants: A Case Study of Construction Workers in Delhi",
          "Monitoring the Effects of Light Pollution &amp; Evaluating the Effectiveness of Indian Regulations",
          "Community Awareness, Participation, &amp; CCDRR: Reflections from North-West India",
          "Experience of Migrant College Students During COVID-19 Pandemic",
          "Analyzing the Possibilities and Prospects of 24/7 Water Supply in Delhi, India",
          "Geography of Ramayana",
          "Digital Enhancement of Physical Space and Connective Turn in the Tourism Industry during and Post-COVID-19 Period"])}
</section>
<section>
  <h2>Undergraduate projects, BA Geography, 2018–2021</h2>
  {plist(["Forest Monitoring &amp; Urban Sprawl Analysis Using GIS in Delhi",
          "LULC Change Detection for 20 Years in South-West Delhi",
          "Social Indicators &amp; Status Analysis of Jammu &amp; Kashmir",
          "Socio-Economic Impact of COVID-19 in Delhi",
          "HRVC Analysis of Jim Corbett",
          "Studying Human Trafficking in Delhi through Remote Sensing",
          "Understanding Ansal Plaza Mall of South Delhi as a Gendered Landscape: A Temporal Study"])}
</section>
"""
page("projects.html", "Projects, Kavya Agrawal", "Research and student projects by Kavya Agrawal, from Delhi land use to national groundwater models.",
     projects, ("Projects", "From mapping Delhi's land use as an undergraduate to national groundwater models."))

# ------------------------------------------------------------------ ENGAGEMENT
engagement = f"""
<div class="cols">
<div>
<section>
  <h2>Rapporteur</h2>
  <ul class="entries">
    {entry("Mar 2026", "National Workshop on Geospatial Technology for Climate Action, Sustainability and Disaster Risk Reduction", None, "TERI SAS with NRSC, ISRO, 16–20 March 2026. Also participant and volunteer.")}
    {entry("2025", "Ministerial Session: NDC 3.0 and Multilateralism on the Road to COP30 and COP33", None, "World Sustainable Development Summit 2025, TERI")}
    {entry("2025", "High-Level Plenary on Achieving Sustainable Development through Integrated Action", None, "World Sustainable Development Summit 2025, TERI")}
  </ul>
</section>
<section>
  <h2>Judge and facilitator</h2>
  <ul class="entries">
    {entry("2026", "Facilitator and judge, Programme LEAD 2026", None, "TERI SAS. Sustainable City Design Challenge for students in classes 9 to 12.")}
    {entry("Nov 2025", "Judge and panel member, TERI SAS Sustainability Hackathon 2025", None, "18–19 November 2025. Evaluated school and undergraduate sustainability proposals.")}
    {entry("2025", "Judge, KnoxCode 2025 Geospatial Innovation Challenge", None, "Organised by GeoknoX, TERI SAS, at Aahwaan Fest 2025. Judged GIS, remote sensing, raster analysis and geospatial storytelling.")}
  </ul>
</section>
<section>
  <h2>Summits and policy dialogues</h2>
  <ul class="entries">
    {entry("Feb 2026", "World Sustainable Development Summit 2026, Silver Jubilee edition", None, "Delegate. Taj Palace, New Delhi, 25–27 February 2026.")}
    {entry("Feb 2026", "Water as a Commons workshop, Water Governance Working Group", None, "With the Ostrom Workshop, Indiana University Bloomington and IU India Gateway, 26–27 February 2026, including a Yamuna River field visit with INTACH Delhi.")}
    {entry("Feb 2026", "Delhi Climate Innovation Week: Ambition to Action Climathon", None, "Climate Career &amp; Sustainability Expo, Innovate X Delhi, 21 February 2026.")}
    {entry("Oct 2025", "Act4Earth Dialogue: Strengthening Multilateralism on the Road to COP30 and Beyond", None, "Virtual, 17 October 2025.")}
    {entry("Sep 2025", "Science Summit 2025: Marine Resources for Sustainable Development", None, "16 September 2025.")}
    {entry("Mar 2025", "World Sustainable Development Summit 2025", None, "New Delhi, 5–7 March 2025.")}
  </ul>
</section>
<section>
  <h2>Training and schools</h2>
  <ul class="entries">
    {entry("Aug 2025", "QGreenland Educator Workshop", None, "Virtual, 5–7 August 2025. Building teaching activities with QGreenland data.")}
    {entry("Dec 2024", "UAV and Drone Applications in Agriculture and Natural Resource Management", None, "TERI SAS with IIT BHU, IIT Roorkee, Namami Gange, Hokkaido University and partners, 10–12 December 2024.")}
    {entry("Nov–Dec 2024", "21-day Winter School in Geospatial Science and Technology", None, "Amity University Noida, supported by the National Geospatial Programme, DST, Government of India.")}
    {entry("Mar 2024", "Geospatial Technology for Forest Fire Disaster Management", None, "One-week capacity building programme, Amity University Noida, 11–15 March 2024.")}
    {entry("", "Climate Skills: Seeds for Transition", None, "TERI SAS and TERI with British Council and HSBC.")}
  </ul>
</section>
<section>
  <h2>Lectures and seminars attended</h2>
  <ul class="entries">
    {entry("Feb 2026", "Soil Carbon Sequestration as a Climate Mitigation Mechanism", None, "Guest lecture by Violeta Martinkė, InSoil, 13 February 2026.")}
    {entry("Oct 2025", "DHI Urban Water Solutions", None, "Expert talk by Morten Just Kjølby, DHI Denmark, TERI SAS, 7 October 2025.")}
    {entry("Jul 2025", "Roots to Resilience Seminar", None, "TERI SAS with UNEP, UNESCO and Akashvani, 25 July 2025.")}
    {entry("Oct 2024", "Groundwater and sustainable development", None, "Lecture by Prof. John A. Cherry, Lee Kuan Yew Water Prize laureate, 24 October 2024.")}
  </ul>
</section>
</div>
<aside>
  <div class="legend">
    <h2>Earlier roles</h2>
    <ul class="plain" style="padding-left:1rem">
      <li style="display:list-item">Editor-in-Chief, Geography Association, University of Delhi, 2018–2021</li>
      <li style="display:list-item">Magazine Coordinator, <em>Vani</em>, SBSC, University of Delhi, 2018–2020</li>
      <li style="display:list-item">English Editor, <em>Vani</em>, 2019</li>
      <li style="display:list-item">Volunteer coordinator, Vasundhara, 2018–2019</li>
      <li style="display:list-item">NSS volunteer, 2019–2021</li>
      <li style="display:list-item">Volunteer, SWAPO NGO, since 2016</li>
    </ul>
  </div>
</aside>
</div>
"""
page("experience.html", "Engagement, Kavya Agrawal", "Rapporteurship, judging, summits, training and academic service by Kavya Agrawal.",
     engagement, ("Engagement", "Rapporteur, judge, delegate and student of the field: work beyond my own research."))

# ------------------------------------------------------------------ CV
edu = "".join([
    entry("2024–now", "PhD, Natural &amp; Applied Sciences", None, "TERI School of Advanced Studies, New Delhi",
          "Thesis: <em>Development of an Adaptable Machine Learning Based Framework for Multi-Contaminant Prediction</em>. Coursework CGPA 9.0/10; comprehensive examination completed January 2026. Supervisor Prof. Chander Kumar Singh; co-supervisor Dr. Adwitiya Sinha."),
    entry("2021–2023", "MA Geography", None, "Dr. B.R. Ambedkar University, Agra", "CGPA 7.60"),
    entry("2018–2021", "BA (Honours) Geography", None, "University of Delhi", "CGPA 7.86"),
    entry("2016–2018", "Senior Secondary", None, "Delhi Public School, Aligarh", "CGPA 9.80"),
    entry("2014–2016", "Secondary", None, "St. Francis Inter College, Hathras", "CGPA 9.20"),
])
awards = "".join([
    entry("2026", "First Position, oral presentation, and Best Paper Award", "award", "ICSSR EHP NEXUS 2026, Gautam Buddha University"),
    entry("2025", "2nd rank, Map Making Competition", "award", "Amity University"),
    entry("2018", "State Child Scientist Award", "award", "National Science Congress"),
    entry("2015–2018", "Top 3 ranks in consecutive English Olympiads", "award", "British Olympiad Foundation"),
    entry("2016, 2018", "Merit Awards", "award", ""),
    entry("", "20 cultural and general knowledge awards", "award", "Various organisations, including prizes in dance"),
])
coursework = "".join(f"<li>{c}</li>" for c in [
    "RPR275 Research and Publication Ethics, grade A", "RPR271 Research Methodology, grade A",
    "NRE115 Environmental Statistics, grade A", "NRG172 Digital Image Processing &amp; Information Extraction, grade A"])

cv = f"""
<div class="cols">
<div>
<section>
  <h2>Education</h2>
  <ul class="entries">{edu}</ul>
  <h3 style="margin-top:1.4rem">PhD coursework</h3>
  <ul class="plain">{coursework}</ul>
</section>
<section>
  <h2>Awards and achievements</h2>
  <ul class="entries">{awards}</ul>
</section>
<section>
  <h2>Research, teaching and service</h2>
  <p>The full record is spread across the other sheets:</p>
  <ul class="plain">
    <li><a href="publications.html">Publications, manuscripts and seven conference presentations</a></li>
    <li><a href="research.html">Research framework, methods and tools</a></li>
    <li><a href="teaching.html">Courses taught in MSc Geoinformatics</a></li>
    <li><a href="experience.html">Rapporteurship, judging, summits and training</a></li>
    <li><a href="projects.html">Doctoral, postgraduate and undergraduate projects</a></li>
  </ul>
</section>
<section>
  <h2>Off the map</h2>
  <p>What I do when I'm not modelling groundwater.</p>
  <div class="stamps">
    <div class="stamp"><span class="glyph" aria-hidden="true">🪙</span><span>Collecting old coins and stamps</span></div>
    <div class="stamp"><span class="glyph" aria-hidden="true">📜</span><span>Reading historic stories and accounts</span></div>
    <div class="stamp"><span class="glyph" aria-hidden="true">📷</span><span>Photography and videography</span></div>
    <div class="stamp"><span class="glyph" aria-hidden="true">🧭</span><span>Travelling</span></div>
    <div class="stamp"><span class="glyph" aria-hidden="true">🏸</span><span>Badminton</span></div>
    <div class="stamp"><span class="glyph" aria-hidden="true">💃</span><span>Dance</span></div>
    <div class="stamp"><span class="glyph" aria-hidden="true">✍️</span><span>Blogging and writing, 2018–2023</span></div>
  </div>
</section>
</div>
<aside>
  <div class="legend">
    <h2>Contact</h2>
    <p style="margin:0 0 .6rem">Department of Natural &amp; Applied Sciences, TERI School of Advanced Studies, Vasant Kunj Institutional Area, New Delhi 110070</p>
    <ul>
      <li><a href="{LINKS['email']}">kavya.agrawal@terisas.ac.in</a></li>
      <li><a href="{LINKS['linkedin']}">LinkedIn</a></li>
      <li><a href="{LINKS['scholar']}">Google Scholar</a></li>
      <li><a href="{LINKS['orcid']}">ORCID</a></li>
    </ul>
  </div>
  <div class="legend">
    <h2>Save a copy</h2>
    <p style="margin:0 0 .7rem">Print this page or save it as a PDF.</p>
    <button class="theme-btn" type="button" onclick="window.print()">Print CV</button>
  </div>
</aside>
</div>
"""
page("cv.html", "CV, Kavya Agrawal", "Curriculum vitae of Kavya Agrawal: education, awards and links to the full research record.",
     cv, ("Curriculum vitae", "Education, awards and the rest of the record, on one page."))

print("built", len(PAGES), "pages")
