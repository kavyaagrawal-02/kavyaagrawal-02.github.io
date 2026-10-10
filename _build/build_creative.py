"""Builds new/index.html: the creative one-page site, one chapter per CV heading."""
import math
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "new"

L = {
    "teri": "kavya.agrawal@terisas.ac.in",
    "gmail": "kavyateriuniversity@gmail.com",
    "linkedin": "https://www.linkedin.com/in/kavya-agrawal02/",
    "scholar": "https://scholar.google.com/citations?user=yXQUQ6YAAAAJ&hl=en",
    "orcid": "https://orcid.org/0009-0009-1032-2541",
    "researchgate": "https://www.researchgate.net/profile/Kavya-Agrawal-4",
    "github": "https://github.com/kavyaagrawal-02",
}
TERI = "28°32′N 77°09′E"

CHAPTERS = [  # id, layer name, swatch, coordinates, place
    ("summary", "Summary", "#E2B341", TERI, "TERI SAS, New Delhi"),
    ("education", "Education", "#B98E64", "27°36′N 78°03′E to " + TERI, "Hathras to New Delhi"),
    ("research", "Research", "#63C3D6", "22°N 79°E", "India, national scale"),
    ("teaching", "Teaching", "#5B9E58", TERI, "MSc Geoinformatics, TERI SAS"),
    ("projects", "Projects", "#C98A4E", "28°37′N 77°13′E", "Delhi and beyond"),
    ("publications", "Publications", "#7DC2E8", TERI, "Journals"),
    ("skills", "Skills", "#9C8772", TERI, "Toolkit"),
    ("conferences", "Conferences & presentations", "#D58DB6", "28°25′N 77°32′E", "Latest: Gautam Buddha University"),
    ("talks", "Expert talks, seminars & workshops", "#8FB9A8", "28°37′N 77°13′E", "New Delhi"),
    ("training", "Training & schools", "#F0B45A", "28°33′N 77°20′E", "Amity University, Noida"),
    ("rapporteur", "Rapporteurship & policy", "#6C8FD6", "28°36′N 77°10′E", "World Sustainable Development Summit"),
    ("positions", "Positions of responsibility", "#B9A6F0", TERI, "TERI SAS and University of Delhi"),
    ("awards", "Awards & achievements", "#FFD166", "28°25′N 77°32′E", "Latest: Gautam Buddha University"),
    ("beyond", "Beyond the CV", "#E07A6C", "", "Off the map"),
    ("contact", "Contact", "#1F6F80", TERI, "Vasant Kunj, New Delhi"),
]
NUM = {c[0]: i + 1 for i, c in enumerate(CHAPTERS)}


def head(cid, title, lede):
    c = next(x for x in CHAPTERS if x[0] == cid)
    coords = f"<span>{c[3]}</span><span class='n'>{c[4]}</span>" if c[3] else f"<span>Beyond the neatline</span><span class='n'>{c[4]}</span>"
    return f"""<header class="ch-head"><p class="coords" style="margin:0"><span class="n">Layer {NUM[cid]:02d}</span>{coords}</p>
<h2>{title}</h2>{f'<p class="lede">{lede}</p>' if lede else ''}</header>"""


def chapter(cid, inner, label):
    c = next(x for x in CHAPTERS if x[0] == cid)
    return f'<section class="chapter" id="{cid}" data-name="{c[1]}" data-coords="{c[3] or "Off the map"}" aria-label="{label}">{inner}</section>'


_pm = 0


def postmark(city, date, cls="pm"):
    global _pm
    _pm += 1
    return f"""<svg class="{cls}" viewBox="0 0 80 80" aria-hidden="true"><defs><path id="p{_pm}" d="M40,40 m-27,0 a27,27 0 1,1 54,0 a27,27 0 1,1 -54,0"/></defs>
<circle cx="40" cy="40" r="37" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="40" cy="40" r="19" fill="none" stroke="currentColor" stroke-width="1.2"/>
<text fill="currentColor"><textPath href="#p{_pm}">{city.upper()} ✦ {city.upper()} ✦</textPath></text>
<text x="40" y="43" text-anchor="middle" fill="currentColor" style="font-size:9px">{date}</text></svg>"""


# ---------------------------------------------------------------- 1 SUMMARY
PLACES = [  # text, level, x%, y%
    ("Groundwater quality", 1, 50, 12), ("Uranium", 1, 18, 30), ("Fluoride", 1, 82, 33), ("Arsenic", 1, 50, 86),
    ("Remote sensing", 2, 22, 62), ("GIS", 2, 84, 60), ("Machine learning", 2, 76, 76), ("Population exposure", 2, 27, 76),
    ("Google Earth Engine", 2, 50, 72), ("Groundwater governance", 2, 50, 95),
    ("AutoML", 3, 13, 46), ("Explainable AI", 3, 85, 47), ("Downscaling", 3, 16, 88), ("Cryosphere", 3, 85, 88),
    ("Hydrogeochemistry", 3, 23, 18), ("Water security", 3, 79, 18),
]
places = "".join(f'<span class="place l{lv}" style="left:{x}%;top:{y}%">{t}</span>' for t, lv, x, y in PLACES)

NEWS = [
    ("Jun 2026", "Started teaching <em>Principles of Remote Sensing</em> (NRG169) and <em>Principles of GIS and GNSS</em> (NRG176) in the MSc Geoinformatics programme."),
    ("Apr 2026", "Won First Position (oral presentation) and the Best Paper Award at ICSSR EHP NEXUS 2026, Gautam Buddha University, for my work on uranium risk."),
    ("Mar 2026", "Rapporteur at the National Workshop on Geospatial Technology for Climate Action, Sustainability and Disaster Risk Reduction (TERI SAS with NRSC, ISRO)."),
    ("Feb 2026", "Delegate at the World Sustainable Development Summit 2026, Silver Jubilee edition."),
    ("Jan 2026", "Completed my PhD comprehensive examination, and submitted <em>Predicting Uranium Occurrences in Groundwater throughout India</em> to a journal."),
]
news = "".join(f'<li><span class="d">{d}</span><p>{t}</p></li>' for d, t in NEWS)

summary = head("summary", "", "") .replace("<h2></h2>", "") + f"""
<div class="here">
  <div>
    <h1>Kavya<br>Agrawal</h1>
    <p class="tagline">PhD scholar in groundwater, remote sensing and machine learning</p>
    <p>I am a PhD scholar in Natural and Applied Sciences at the TERI School of Advanced Studies, New Delhi, working where environmental systems, human activity and technology meet. My doctoral research predicts and assesses groundwater contamination across India, bringing together hydrogeochemistry, remote sensing, GIS and multi-source environmental data.</p>
    <p>I work on uranium, fluoride and arsenic, using machine learning, deep learning and spatial modelling to understand contamination patterns, what controls them, and where the risk is highest. I'm also interested in population exposure, groundwater governance, climate and cryosphere systems and water security, and I'm always open to new questions, methods and collaborations.</p>
    <p class="muted" style="font-size:.95rem">Supervisor: Prof. Chander Kumar Singh. Co-supervisor: Dr. Adwitiya Sinha.</p>
    <div class="links"><a href="mailto:{L['teri']}">{L['teri']}</a><a href="{L['scholar']}">Google Scholar</a><a href="{L['orcid']}">ORCID</a><a href="{L['researchgate']}">ResearchGate</a><a href="{L['linkedin']}">LinkedIn</a><a href="{L['github']}">GitHub</a></div>
  </div>
  <div class="mapbox" role="img" aria-label="Map-style graphic: Kavya's portrait as a pin at TERI SAS, New Delhi, surrounded by her research keywords set like place names">
    <canvas id="here-map" aria-hidden="true"></canvas>
    {places}
    <div class="pin"><div class="head"><img src="assets/img/kavya-portrait-hero.jpg" alt=""></div></div>
    <div class="pin-label">You are here<small>{TERI}</small></div>
  </div>
</div>
<div class="summary-grid">
  <div><h3 class="sub" style="margin-top:0">News</h3><ul class="news">{news}</ul></div>
  <aside class="currently"><h3>Currently, 2025–26</h3><dl>
    <div><dt>Research</dt><dd>Uranium, fluoride, arsenic and downscaling of environmental predictors</dd></div>
    <div><dt>Teaching</dt><dd>Principles of Remote Sensing; Principles of GIS and GNSS (MSc Geoinformatics)</dd></div>
    <div><dt>Service</dt><dd>Judge at Programme LEAD, the Sustainability Hackathon and KnoxCode</dd></div>
    <div><dt>Policy and academic engagement</dt><dd>WSDS 2025 and 2026, Water as a Commons workshop, National Geospatial Technology workshop</dd></div>
    <div><dt>Capacity building</dt><dd>QGreenland, UAV and drones, geospatial forest-fire management, winter school</dd></div>
  </dl></aside>
</div>"""

# ---------------------------------------------------------------- 2 EDUCATION
STRATA = [  # years label, title, place, cgpa, colour, texture, rock, extra, height(px)
    ("2024 to now", "PhD, Natural &amp; Applied Sciences", "TERI School of Advanced Studies, New Delhi", "9.0",
     "#DCCFA8", "repeating-linear-gradient(0deg, rgba(0,0,0,.25) 0 1px, transparent 1px 7px)", "Fresh alluvium, still being deposited",
     """<p style="margin-top:.5rem"><em>Development of an Adaptable Machine Learning Based Framework for Multi-Contaminant Prediction</em></p>
<p>Full-time, registered 1 February 2024. Comprehensive examination completed 28 January 2026. Coursework CGPA 9.0.</p>
<div class="grains"><span>Research and Publication Ethics: A</span><span>Research Methodology: A</span><span>Environmental Statistics: A</span><span>Digital Image Processing &amp; Information Extraction: A</span></div>""", 210),
    ("2021–2023", "MA Geography", "Dr. B.R. Ambedkar University, Agra", "7.60",
     "#CDAE7E", "radial-gradient(rgba(0,0,0,.35) 1px, transparent 1.3px)", "Sandstone", "", 140),
    ("2018–2021", "BA (Honours) Geography", "University of Delhi", "7.86",
     "#BF9670", "radial-gradient(ellipse 6px 2px, rgba(0,0,0,.25) 50%, transparent 52%)", "Clay with mineral grains", "", 200),
    ("2016–2018", "Senior Secondary School", "Delhi Public School, Aligarh", "9.80",
     "#AE9A84", "radial-gradient(circle 4px, rgba(0,0,0,.28) 60%, transparent 64%)", "Gravel", "", 140),
    ("2014–2016", "Secondary School", "St. Francis Inter College, Hathras", "9.20",
     "#A9A49B", "repeating-linear-gradient(45deg, rgba(0,0,0,.22) 0 1px, transparent 1px 9px), repeating-linear-gradient(-45deg, rgba(0,0,0,.22) 0 1px, transparent 1px 9px)", "Bedrock", "", 140),
]
strata = "".join(f"""<div class="stratum" style="background:{c};--tex:{tex};min-height:{h}px">
<span class="ylabel">{y}</span><span class="cgpa">CGPA {g}</span><span class="yrs">{y}</span><h3>{t}</h3><p>{pl}</p>{ex}<span class="rock">{rock}</span></div>"""
                 for y, t, pl, g, c, tex, rock, ex, h in STRATA)
SUBJECTS = ["Geomorphology", "Climatology &amp; Oceanography", "Cartographic Techniques", "Thematic Cartography", "Remote Sensing &amp; GIS",
            "Statistical Methods in Geography", "Field Work &amp; Research Methodology", "Academic Writing &amp; Composition", "Geography of India",
            "Human Geography", "Disaster Management", "Media &amp; Communication Skills", "History of Geographical Thought", "Social Geography",
            "Political Geography", "Economic Geography", "Agricultural Geography", "Population &amp; Settlement Geography", "Environmental Geography",
            "Regional Planning &amp; Development"]
education = head("education", "Education", "Read it like a rock column: the oldest layer at the bottom, the newest on top.") + f"""
<div class="strata">
  <div class="column">{strata}</div>
  <aside class="sample"><h3>Core sample: subjects in my geography degrees</h3><ul>{''.join(f'<li>{s}</li>' for s in SUBJECTS)}</ul></aside>
</div>"""

# ---------------------------------------------------------------- 3 RESEARCH
DATASETS = [("SRTM", 30), ("JRC Surface Water", 30), ("MERIT Hydro", 93), ("GHSL Built", 100), ("OpenLandMap soils", 232),
            ("MODIS LST, NDVI", 927), ("GPW population", 1000), ("TerraClimate", 4638), ("CHIRPS", 5566), ("ERA5-Land", 11132),
            ("GLDAS", 27830), ("GRACE", 111319)]


def scalebar():
    L0, R0 = 40, 960
    lo, hi = math.log10(10), math.log10(200000)
    x = lambda m: L0 + (math.log10(m) - lo) / (hi - lo) * (R0 - L0)
    p = []
    dec = [10, 100, 1000, 10000, 100000, 200000]
    for i in range(len(dec) - 1):
        p.append(f'<rect class="{"a" if i % 2 == 0 else "b"}" x="{x(dec[i]):.1f}" y="150" width="{x(dec[i+1]) - x(dec[i]):.1f}" height="12"/>')
    for m, lab in [(10, "10 m"), (100, "100 m"), (1000, "1 km"), (10000, "10 km"), (100000, "100 km")]:
        p.append(f'<text class="unit" x="{x(m):.1f}" y="186" text-anchor="middle">{lab}</text>')
    for i, (n, m) in enumerate(DATASETS):
        up = i % 2 == 0
        lv = (i // 2) % 3
        ty = (30 + lv * 34) if up else (218 + lv * 26)
        y1, y2 = (ty + 6, 150) if up else (162, ty - 14)
        p.append(f'<line class="lead" x1="{x(m):.1f}" y1="{y1}" x2="{x(m):.1f}" y2="{y2}"/>')
        p.append(f'<circle class="dot" cx="{x(m):.1f}" cy="{150 if up else 162}" r="3.5"/>')
        p.append(f'<text x="{x(m):.1f}" y="{ty}" text-anchor="middle">{n}</text>')
    return f'<div class="scalebar"><svg viewBox="0 0 1000 292" role="img" aria-label="Logarithmic scale bar of dataset resolutions, from SRTM at 30 metres to GRACE at about 111 kilometres">{"".join(p)}</svg></div>'


TILES = [  # key, symbol, z, name, year label, decimal year, colour, method?
    ("cr", "LST", "", "Land surface temperature and cryosphere", "2023", 2023.1, "#B9A6F0", True),
    ("as", "As", "33", "Arsenic", "2024", 2024.5, "#D58DB6", False),
    ("u", "U", "92", "Uranium", "2025", 2025.25, "#C9DB34", False),
    ("f", "F", "9", "Fluoride", "2026", 2026.0, "#7DC2E8", False),
    ("ds", "DS", "", "Downscaling satellite predictors", "2026", 2026.12, "#F0B45A", True),
]
DETAILS = {
    "u": ("Uranium", "Predicting Uranium Occurrences in Groundwater throughout India",
          "A national-scale model of where uranium occurs in India's groundwater, built from groundwater observations and environmental predictors and checked against an independent validation dataset. The predictions feed into spatial risk classes, estimates of how many people may be exposed, and governance indicators that show where monitoring and action are most needed.",
          [("Methods", "Automated machine learning (AutoGluon ensemble), independent validation, spatial risk classes, population exposure, groundwater governance indicators"),
           ("Status", "Research paper submitted to a journal (Sep 2025 to Jan 2026)"),
           ("Recognition", "Presented as <em>An ML-based Uranium Risk Assessment for Urban Groundwater Governance and Population Exposure in India</em>: First Position and Best Paper Award, ICSSR EHP NEXUS 2026")]),
    "f": ("Fluoride", "Comparing and Benchmarking Deep Learning Models for Predicting Groundwater Contamination caused by Fluoride with the effects of Spatial Resolution on Prediction",
          "India-wide fluoride prediction that asks two questions: which deep learning models work best, and how much the resolution of the environmental predictors changes the answer. Predictor stacks are built in Google Earth Engine at native resolution and at 500 m, 1 km and 5 km, while every groundwater observation is kept in the data.",
          [("Methods", "Deep learning benchmarking, multi-resolution predictor stacks (means for continuous data, majority for categories, aspect as northness and eastness), 1.5 mg/L threshold"),
           ("Status", "Research paper in progress, since January 2026")]),
    "as": ("Arsenic", "Distribution, Speciation and Controls on As Mobilization in the Groundwater in Aquifers of the Middle Gangetic Plain, India",
           "How arsenic is distributed in the aquifers of the Middle Gangetic Plain, which forms it takes, and what releases it into groundwater. The work looks at geogenic and hydrogeochemical controls such as pH, iron, redox potential and sulfate, and uses explainable AI to check that model results make physical sense.",
           [("Methods", "Hydrogeochemistry, explainable AI (SHAP, LIME), attention to temporal transferability and physical plausibility"),
            ("Status", "Presented at As2024, the 9th International Congress on Arsenic in the Environment, Bhubaneswar (Jul 2024 to Apr 2025)")]),
    "ds": ("Downscaling", "A Physically Informed Framework for Multi-Resolution Downscaling and Upscaling of Environmental Predictors (Satellite Data)",
           "Moving satellite data between coarse and fine resolutions without inventing detail. A pilot on CHIRPS rainfall over Punjab (2013–2022, about 5.6 km) targets 5 km, 1 km and 500 m, using sub-pixel fractions and conservation-based aggregation, with machine learning to tell genuine downscaling apart from simple resampling.",
           [("Methods", "Sub-pixel fractions, conservation-based aggregation, ML prediction; validated with Moran's I, semivariograms and aggregation consistency"),
            ("Engineering", "Two-step aggregation and chunked hybrid Python processing to work around Google Earth Engine memory limits"),
            ("Status", "Research paper in progress, since February 2026")]),
    "cr": ("Cryosphere", "Mountains, snow and ice: where my research began",
           "Before groundwater, I studied the climate of the Indus River Basin and the Himalaya: how daytime and nighttime land surface temperatures are changing with elevation, where permafrost is likely, and how snow cover is changing in Indian basins.",
           [("Published", 'Mal, S., <strong>Agrawal, K.</strong>, Rani, S. et al. (2023). Evaluating spatial and elevation-wise daytime/nighttime LST trends across the Indus River Basin. <em>Journal of Mountain Science</em> 20, 3154–3172. <a href="https://doi.org/10.1007/s11629-023-8157-8">DOI</a>'),
            ("Permafrost", "Identification and mapping in the Indus Basin from about 20 years of MAAT, PISR, BMAT, snow and precipitation estimates in Google Earth Engine"),
            ("Snow cover", "Snow cover and changes in Indian basins"),
            ("Methods", "Google Earth Engine (JavaScript), ArcGIS, time-series and trend analysis (Mann–Kendall, Theil–Sen)")]),
}
tiles = "".join(f"""<button class="tile{' method' if m else ''}" type="button" style="--tc:{c}" data-tile="{k}" aria-expanded="{'true' if k == 'u' else 'false'}" aria-controls="tile-detail">
<span class="z">{z if z else 'method'}</span><span class="yr">{yl}</span><span class="sym">{s}</span><span class="nm">{n}</span></button>""" for k, s, z, n, yl, dy, c, m in TILES)


def river_svg():
    xd = lambda d: 60 + (d - 2023) / (2026.6 - 2023) * 880
    parts = [f'<path class="stem" d="M{xd(2023):.0f} 120 L{xd(2024.08):.0f} 120" stroke-dasharray="2 14" style="stroke-width:6"/>',
             f'<path class="stem" d="M{xd(2024.08):.0f} 120 L{xd(2026.6):.0f} 120"/>',
             f'<text class="lbl" x="{xd(2024.08):.0f}" y="146">PhD begins, Feb 2024</text>']
    for i, (k, s, z, n, yl, dy, c, m) in enumerate(TILES):
        tx = 100 + i * 200
        parts.append(f'<path class="trib" stroke="{c}" d="M{tx} 0 C {tx} 70, {xd(dy):.0f} 60, {xd(dy):.0f} 116"/>')
    for yv in [2023, 2024, 2025, 2026]:
        parts.append(f'<text x="{xd(yv):.0f}" y="170" text-anchor="middle">{yv}</text>')
    return f'<svg class="river-svg" viewBox="0 0 1000 178" aria-hidden="true">{"".join(parts)}</svg>'


def js_str(s):
    import json
    return json.dumps(s)


details_obj = {k: {"k": v[0], "t": v[1], "p": v[2], "d": v[3], "c": next(t[6] for t in TILES if t[0] == k)} for k, v in DETAILS.items()}


def detail_html(k):
    v = details_obj[k]
    dl = "".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in v["d"])
    return f'<div><span class="k">{v["k"]}</span><h3>{v["t"]}</h3><p>{v["p"]}</p></div><dl>{dl}</dl>'


research = head("research", "Research", "My PhD asks how far we can predict groundwater contamination across a country as large and varied as India, and what the predictions mean for the people who drink the water.") + f"""
<div class="orbit" id="orbit">
  <div class="orbit-pin">
    <canvas id="scene" role="img" aria-label="Illustrative satellite scene that sharpens from coarse to fine pixels as you scroll"></canvas>
    <div class="shade"></div>
    <div class="txt"><h3>Scales I work across</h3><p>Scroll to zoom in. The pixel size steps down through datasets I use, from 111 km down to 30 m.</p></div>
    <div class="readout"><span class="px">111 km</span><span class="ds">GRACE, water storage</span><span class="note">Pixel size. Illustrative scene, not real data.</span></div>
  </div>
</div>
<div class="framework">
  <div>
    <p>My thesis, <em>Development of an Adaptable Machine Learning Based Framework for Multi-Contaminant Prediction</em>, builds a national-scale framework for predicting groundwater contamination and assessing its risk.</p>
    <p>It brings together groundwater observations and hydrochemistry with remote sensing and GIS layers on climate, hydrology, terrain, soil, geology, land use, human modification and population. The aims run from prediction and risk mapping to checking uncertainty and robustness, understanding environmental controls, estimating exposure, and supporting governance decisions.</p>
  </div>
  <p class="sup">Supervisor: Prof. Chander Kumar Singh<br>Co-supervisor: Dr. Adwitiya Sinha<br><br>Element tiles are contaminants (with atomic numbers). Dashed tiles are methods and earlier work.</p>
</div>
<h3 class="sub">Research lines, joining the PhD over time</h3>
<div class="tiles" role="group" aria-label="Research lines">{tiles}</div>
{river_svg()}
<div class="detail" id="tile-detail" style="--tc:{details_obj['u']['c']}" aria-live="polite">{detail_html('u')}</div>
<h3 class="sub">The data behind the models</h3>
<p class="muted">Native resolutions of some of the datasets in my predictor stacks. Part of the work is bringing them onto one grid without losing a single groundwater observation.</p>
{scalebar()}
<h3 class="sub">Figures</h3>
<div class="figs">
  <figure class="fig"><img src="assets/img/lst-trends.png" alt="Violin plots of daytime, nighttime and mean LST trends by season across the Indus River Basin" loading="lazy"><figcaption>Seasonal LST trends across the Indus River Basin (Journal of Mountain Science, 2023).</figcaption></figure>
  <figure class="fig"><img src="assets/img/indus-study-area.png" alt="Study area map of the Indus River Basin with elevation, rivers and major cities" loading="lazy"><figcaption>The Indus River Basin study area.</figcaption></figure>
</div>
<h3 class="sub">Questions I'd like to explore</h3>
<ul class="explore"><li>Permafrost identification and modelling</li><li>Glacier, ice and snow mapping</li><li>Climate change impacts</li><li>High Mountain Asia and the Himalaya</li><li>The Arctic and Antarctica</li><li>Remote sensing for history and archaeology</li></ul>
"""

# ---------------------------------------------------------------- 4 TEACHING
def manual(code, title, runs, topics):
    r = "".join(f"<li>{x}</li>" for x in runs)
    t = ", ".join(topics)
    return f"""<article class="manual"><span class="code">{code}</span><h3>{title}</h3>
<table><tr><td>Programme</td><td>MSc Geoinformatics, TERI SAS</td></tr><tr><td>Credits</td><td>4</td></tr><tr><td>Contact hours</td><td>60</td></tr><tr><td>In the lab</td><td>{t}</td></tr></table>
<div class="ltp" role="img" aria-label="Lecture 42 hours, tutorial 2 hours, practical 32 hours"><i style="flex:42;background:#1F6F80"></i><i style="flex:2;background:#8A5A2B"></i><i style="flex:32;background:#5B9E58"></i></div>
<div class="ltp-key"><span><b style="background:#1F6F80"></b>Lecture 42</span><span><b style="background:#8A5A2B"></b>Tutorial 2</span><span><b style="background:#5B9E58"></b>Practical 32</span></div>
<ul class="runs">{r}</ul></article>"""


teaching = head("teaching", "Teaching", "Course teaching in the MSc Geoinformatics programme at TERI SAS.") + f"""
<div class="semesters" style="grid-template-columns:repeat(3,minmax(0,1fr))">
  <div class="s">Jul–Dec 2025<span class="bar" style="background:#7DC2E8">NRG169 practicals, 32 hours</span></div>
  <div class="s">Jan–May 2026<span class="bar" style="background:var(--line);color:var(--ink)">Comprehensive exam, Jan 2026</span></div>
  <div class="s">Jun–Dec 2026<span class="bar" style="background:#7DC2E8">NRG169 Remote Sensing</span><span class="bar" style="background:#9CCB8A">NRG176 GIS and GNSS</span></div>
</div>
<div class="manuals">
  {manual("NRG169", "Principles of Remote Sensing", ["Jun–Dec 2026: course teaching", "Jul–Dec 2025: taught the 32 practical learning hours"], ["Landsat 8/9 imagery", "ERDAS Imagine", "image enhancement", "urban, vegetation and geomorphology analysis"])}
  {manual("NRG176", "Principles of GIS and GNSS", ["Jun–Dec 2026: course teaching"], ["GPS and GNSS", "satellite navigation", "georeferencing", "ArcGIS Pro"])}
</div>
<h3 class="sub">Try it: what a satellite band shows</h3>
<div class="demo">
  <div class="demo-img"><img id="demo-img" src="assets/img/scene-true.jpg" alt="Illustrative satellite scene in true colour" loading="lazy"></div>
  <div>
    <div class="demo-btns" role="group" aria-label="Band">
      <button type="button" data-demo="true" aria-pressed="true">True colour</button>
      <button type="button" data-demo="false" aria-pressed="false">False colour</button>
      <button type="button" data-demo="thermal" aria-pressed="false">Thermal</button>
    </div>
    <h3 id="demo-h">True colour</h3>
    <p id="demo-p">Red, green and blue light, roughly what your eyes would see from orbit. Fields look green, bare soil brown, water dark.</p>
    <p class="muted" style="font-size:.85rem">Students learn to switch between band combinations like this in the remote sensing lab. The scene is generated for illustration.</p>
  </div>
</div>
<h3 class="sub">An example from the lab</h3>
<figure class="fig" style="max-width:760px"><img src="assets/img/delhi-lulc.png" alt="Land use and land cover classification of South West Delhi from Landsat 8, October 2019" loading="lazy"><figcaption>Land use and land cover of South West Delhi, Landsat 8, October 2019.</figcaption></figure>
"""

# ---------------------------------------------------------------- 5 PROJECTS
THEMES = {"urban": ("Urban and land", "#C98A4E"), "society": ("Society and migration", "#D58DB6"), "water": ("Water", "#63C3D6"),
          "hazard": ("Disaster and risk", "#E07A6C"), "culture": ("Culture and history", "#B9A6F0"), "ice": ("Snow and ice", "#7DC2E8")}
PROJ = [
    ("PG 1", "Measuring the Problems and Emotions of Urban-Ward Migrants: A Case Study of Construction Workers in Delhi", "society", "Postgraduate, 2021–2023", "A case study of the everyday problems and emotional experiences of construction workers who migrated to Delhi."),
    ("PG 2", "Monitoring the Effects of Light Pollution &amp; Evaluating the Effectiveness of Indian Regulations", "urban", "Postgraduate, 2021–2023", "Tracking the effects of light pollution and assessing how well Indian regulations deal with it."),
    ("PG 3", "Community Awareness, Participation, &amp; CCDRR: Reflections from North-West India", "hazard", "Postgraduate, 2021–2023", "How community awareness and participation shape community-centred disaster risk reduction in North-West India."),
    ("PG 4", "Experience of Migrant College Students During COVID-19 Pandemic", "society", "Postgraduate, 2021–2023", "Field evidence on what migrant college students went through during the pandemic, presented at two conferences in 2022."),
    ("PG 5", "Analyzing the Possibilities and Prospects of 24/7 Water Supply in Delhi, India", "water", "Postgraduate, 2021–2023", "Whether round-the-clock piped water is possible for Delhi, and what it would take. Published in the Journal of Indian Water Works Association."),
    ("PG 6", "Geography of Ramayana", "culture", "Postgraduate, 2021–2023", "A geographical reading of the places and landscapes in the Ramayana."),
    ("PG 7", "Digital Enhancement of Physical Space and Connective Turn in the Tourism Industry during and Post-COVID-19 Period", "culture", "Postgraduate, 2021–2023", "How digital technology reshaped tourist spaces during and after COVID-19, presented at the Delhi School of Economics in 2022."),
    ("UG 1", "Forest Monitoring &amp; Urban Sprawl Analysis Using GIS in Delhi", "urban", "Undergraduate, 2018–2021", "Mapping Delhi's forest cover and the spread of the city with GIS."),
    ("UG 2", "LULC Change Detection for 20 Years in South-West Delhi", "urban", "Undergraduate, 2018–2021", "Twenty years of land use and land cover change in South-West Delhi, from satellite imagery."),
    ("UG 3", "Social Indicators &amp; Status Analysis of Jammu &amp; Kashmir", "society", "Undergraduate, 2018–2021", "An analysis of social indicators and development status across Jammu and Kashmir."),
    ("UG 4", "Socio-Economic Impact of COVID-19 in Delhi", "society", "Undergraduate, 2018–2021", "The social and economic effects of COVID-19 on Delhi."),
    ("UG 5", "Snow Cover &amp; Changes in Indian Basins", "ice", "Undergraduate, 2018–2021", "How snow cover is changing across India's river basins."),
    ("UG 6", "HRVC Analysis of Jim Corbett", "hazard", "Undergraduate, 2018–2021", "A hazard, risk, vulnerability and capacity (HRVC) analysis of the Jim Corbett area."),
    ("UG 7", "Studying Human Trafficking in Delhi through Remote Sensing", "society", "Undergraduate, 2018–2021", "Exploring what remote sensing can add to the study of human trafficking in Delhi."),
    ("UG 8", "Understanding Ansal Plaza Mall of South Delhi as a Gendered Landscape: A Temporal Study", "urban", "Undergraduate, 2018–2021", "A study over time of a South Delhi shopping mall as a gendered landscape."),
]
filters = '<button type="button" data-f="all" aria-pressed="true">All 15</button>' + "".join(
    f'<button type="button" data-f="{k}" aria-pressed="false">{v[0]}</button>' for k, v in THEMES.items())
sheets = "".join(f"""<div class="sheet" data-theme="{th}" style="--tcol:{THEMES[th][1]}"><button type="button" aria-expanded="false"><span class="no"><span>Sheet {no}</span><i>{THEMES[th][0]}</i></span><h3>{t}</h3></button>
<div class="card"><small>{lvl}</small>{d}</div></div>""" for no, t, th, lvl, d in PROJ)
projects = head("projects", "Projects", "Postgraduate and undergraduate projects, laid out like a map-sheet index. Filter by theme, then open a sheet to pull out its card.") + f"""
<div class="filters" role="group" aria-label="Filter projects by theme">{filters}</div>
<div class="sheets">{sheets}</div>"""

# ---------------------------------------------------------------- 6 PUBLICATIONS
publications = head("publications", "Publications", "Every paper moves along the same pipeline. Published work sits at the end.") + f"""
<div class="pipeline">
  <div class="stage"><h3><b>1</b>Drafting</h3>
    <div class="pcard"><b>Fluoride</b>Comparing and Benchmarking Deep Learning Models for Predicting Groundwater Contamination caused by Fluoride with the effects of Spatial Resolution on Prediction</div>
    <div class="pcard"><b>Downscaling</b>A Physically Informed Framework for Multi-Resolution Downscaling and Upscaling of Environmental Predictors (Satellite Data)</div></div>
  <div class="stage"><h3><b>2</b>Submitted</h3>
    <div class="pcard"><b>Uranium</b>Predicting Uranium Occurrences in Groundwater throughout India</div></div>
  <div class="stage"><h3><b>3</b>Under review</h3><p class="empty">The next stop for the papers on the left.</p></div>
  <div class="stage"><h3><b>4</b>Published</h3>
    <div class="pcard"><b>2023</b>LST trends across the Indus River Basin, <em>Journal of Mountain Science</em></div>
    <div class="pcard"><b>2023</b>24/7 water supply in Delhi, <em>Journal of Indian Water Works Association</em></div></div>
</div>
<!-- To add a published paper: copy one <article class="pubcard"> block below and edit it. -->
<div class="published">
  <article class="pubcard"><div class="figure"><img src="assets/img/lst-trends.png" alt="LST trend figure from the paper" loading="lazy"></div>
    <div class="txt"><span class="tag">Journal of Mountain Science, November 2023</span><h3>Evaluating spatial and elevation-wise daytime/nighttime LST trends across the Indus River Basin</h3>
    <p>Mal, S., <strong>Agrawal, K.</strong>, Rani, S. et al. <em>J. Mt. Sci.</em> 20, 3154–3172.</p>
    <p><a href="https://doi.org/10.1007/s11629-023-8157-8">doi.org/10.1007/s11629-023-8157-8</a></p></div></article>
  <article class="pubcard"><div class="figure type"><span>24/7 water for Delhi?</span><small>Journal of Indian Water Works Association, UGC-CARE Group I</small></div>
    <div class="txt"><span class="tag">Journal of Indian Water Works Association, 2023</span><h3>Analyzing the Possibilities and Prospects of 24/7 Water Supply in Delhi, India</h3>
    <p>Sanu, S. K., Chandrakanta, <strong>Agrawal, K.</strong>, Sharma, V. R., &amp; Bajaj, A. <em>Journal of Indian Water Works Association</em>, LV(1). ISSN 0970-275X.</p></div></article>
</div>
<p class="links"><a href="{L['scholar']}">Google Scholar</a><a href="{L['orcid']}">ORCID 0009-0009-1032-2541</a><a href="{L['researchgate']}">ResearchGate</a></p>
"""

# ---------------------------------------------------------------- 7 SKILLS
def sym(shape, c):
    s = {"square": f'<rect x="3" y="3" width="16" height="16" fill="{c}"/>',
         "circle": f'<circle cx="11" cy="11" r="8" fill="{c}"/>',
         "tri": f'<path d="M11 2 L20 19 L2 19 Z" fill="{c}"/>',
         "diamond": f'<path d="M11 1 L21 11 L11 21 L1 11 Z" fill="{c}"/>',
         "hex": f'<path d="M6 2 H16 L21 11 L16 20 H6 L1 11 Z" fill="{c}"/>',
         "wave": f'<path d="M1 8 q5 -6 10 0 t10 0 M1 15 q5 -6 10 0 t10 0" stroke="{c}" stroke-width="3" fill="none"/>',
         "cross": f'<path d="M8 1 h6 v7 h7 v6 h-7 v7 h-6 v-7 h-7 v-6 h7 z" fill="{c}"/>',
         "star": f'<path d="M11 1 l3 7 7 .5 -5.5 4.5 2 7 -6.5 -4 -6.5 4 2 -7 -5.5 -4.5 7 -.5z" fill="{c}"/>'}[shape]
    return f'<svg class="legend" viewBox="0 0 22 22" aria-hidden="true">{s}</svg>'


SKILLS = [
    ("GIS and remote sensing software", "#C2A878", "square", ["ArcGIS / ArcGIS Pro", "QGIS", "Google Earth Engine", "Google Earth", "ERDAS Imagine"]),
    ("Programming and machine learning", "#9C8358", "tri", ["Python", "JavaScript (Earth Engine)", "pandas", "Machine learning", "Deep learning", "AutoML (AutoGluon)", "Random Forest", "LightGBM", "SHAP", "LIME"]),
    ("Spatial analysis and statistics", "#6F7A6A", "circle", ["Spatial data analysis and visualisation", "Time-series modelling", "Trend analysis", "Mann–Kendall test", "Theil–Sen slope", "Moran's I", "Semivariograms", "Image enhancement and feature extraction", "Orthorectification and mosaicking", "DEM processing", "Satellite image acquisition and processing"]),
    ("Earth observation and environmental data", "#4F7F86", "wave", ["Landsat 8/9", "Sentinel", "MODIS Terra/Aqua", "VIIRS", "FIRMS", "CHIRPS", "IMD", "ERA5-Land", "TerraClimate", "GLDAS", "GRACE", "SRTM", "MERIT Hydro", "JRC Global Surface Water", "OpenLandMap soils", "GPW", "GHM", "GHSL", "SMOD", "LCZ", "CSP Global Human Modification", "CGWB groundwater observations", "Literature-derived water quality data", "pH, EC, Ca, Mg, Na, K, HCO₃, Cl, SO₄, NO₃, F, PO₄, U"]),
    ("Parameters I work with", "#3D6670", "diamond", ["MAAT", "BMAT", "PISR", "Land surface temperature", "NDVI / NDBI", "Night-time light", "Snow estimates", "Precipitation", "Slope and DEM", "Temperature, aerosols, solar radiation", "Cryosphere parameters", "Forest monitoring", "Urban sprawl", "Land-use and environmental history"]),
    ("Data quality and QA/QC", "#2E5260", "hex", ["Duplicate detection and preservation rules", "Administrative-name standardisation", "Coordinate validation and geometry reconstruction", "Sentinel and missing values", "Provenance and data lineage", "Unit verification", "Temporal and spatial compatibility", "Resolution harmonisation", "Independent validation", "Masked-pixel handling", "Consistent exposure denominators", "Correlation versus causation", "Ground truth, transferability, uncertainty, physical plausibility", "True downscaling versus resampling", "Geogenic versus environmental controls"]),
    ("Research and field", "#24414C", "cross", ["Field and survey-based research", "Socio-environmental data analysis", "Groundwater and drinking-water quality assessment", "Disaster risk reduction and resilience", "Climate–water–environment interactions", "Sustainability and climate policy"]),
    ("Professional", "#1A2F38", "star", ["Academic writing and conference presentations", "Scientific communication and reporting", "Editorial and content development", "Rapporteurship and policy-session documentation", "Academic coordination and event support", "Interdisciplinary collaboration"]),
]
core = "".join(f'<i style="--c:{c};flex:{len(items)}" data-core="{i}"></i>' for i, (n, c, sh, items) in enumerate(SKILLS))
slayers = "".join(f"""<li class="slayer" data-layer="{i}"><div class="row"><label><input type="checkbox" checked data-skill="{i}">{sym(sh, c)}<h3>{n}</h3></label></div>
<ul class="items">{''.join(f'<li>{x}</li>' for x in items)}</ul></li>""" for i, (n, c, sh, items) in enumerate(SKILLS))
skills = head("skills", "Skills", "A borehole through my toolkit. Each layer has its own legend symbol; untick a layer to fold it away.") + f"""
<div class="bore"><div class="core" style="display:flex;flex-direction:column" aria-hidden="true">{core}</div><ul class="slayers">{slayers}</ul></div>"""

# ---------------------------------------------------------------- 8 CONFERENCES
TALKS = [
    ("ICSSR EHP NEXUS 2026", "Machine-Learning-Based Uranium Risk Assessment, Population Exposure and Groundwater Governance", "Track 10: AI and Predictive Analytics, Gautam Buddha University, 27–28 April 2026", "Greater Noida", "IV.2026", "First Position and Best Paper Award"),
    ("As2024", "Distribution, Speciation and Controls on As Mobilization in the Groundwater in Aquifers of the Middle Gangetic Plain, India", "9th International Congress &amp; Exhibition on Arsenic in the Environment, KIIT Deemed to be University, Bhubaneswar, 20–24 October 2024", "Bhubaneswar", "X.2024", ""),
    ("IGU Thematic Conference", "Problems and Prospects of Delhi's Drinking Water Supply", "Sustainability, Future Earth and Humanities, Central University of Haryana, Mahendragarh, 24–25 November 2022", "Mahendragarh", "XI.2022", ""),
    ("National Seminar, ICPR", "Educational Relevance of Ramayana in Modern India", "Promoting Human Values and Culture for Peaceful Co-Existence, Amity University Haryana, 22 July 2022", "Gurugram", "VII.2022", ""),
    ("Geography and the Digital", "Digital Enhancement of Physical Space and Connective Turn in Tourism Industry during and Post-COVID-19 Period", "Department of Geography, Delhi School of Economics, University of Delhi, 23–25 May 2022", "Delhi", "V.2022", ""),
    ("Jamia International Conference on Education 2022", "Migrant College Students during Covid Pandemic: Evidence from the Field", "Faculty of Education, Jamia Millia Islamia, New Delhi, 6–8 May 2022", "New Delhi", "V.2022", ""),
    ("Disaster Risk Reduction and Resilient Habitat", "Migrant College Students during Covid Pandemic: Evidence from the Field", "Centre for Disaster Management Studies, Shaheed Bhagat Singh College, University of Delhi, 5–6 April 2022", "Delhi", "IV.2022", ""),
]
badges = "".join(f"""<article class="badge{' won' if aw else ''}">{postmark(city, dt)}<span class="ev">{ev}</span><span class="who">Kavya Agrawal</span><h3>{t}</h3><span class="where">{w}</span>{f'<span class="ribbon">{aw}</span>' if aw else ''}</article>"""
                 for ev, t, w, city, dt, aw in TALKS)
conferences = head("conferences", "Conferences and paper presentations", "Seven presentations since 2022, each badge postmarked with its city and date.") + f'<div class="badges">{badges}</div>'

# ---------------------------------------------------------------- 9 TALKS ATTENDED
EVENTS = [
    ("16–20 Mar 2026", "National Workshop on Geospatial Technology for Climate Action, Sustainability and Disaster Risk Reduction", "TERI SAS with NRSC, ISRO. Participant, volunteer and rapporteur.", "Satellite data is most useful when it reaches disaster and climate planners."),
    ("26–27 Feb 2026", "Water as a Commons, Water Governance Working Group", "With the Ostrom Workshop, Indiana University Bloomington and IU India Gateway; Yamuna River field visit with INTACH Delhi.", "Water is shared, so its governance has to be shared too."),
    ("21 Feb 2026", "Ambition to Action: Climathon", "Delhi Climate Innovation Week, Climate Career &amp; Sustainability Expo, Innovate X Delhi.", "Climate ideas need a path from pitch to practice."),
    ("13 Feb 2026", "Soil Carbon Sequestration as a Climate Mitigation Mechanism", "Guest lecture by Ms. Violeta Martinkė, Project Development Lead, InSoil.", "Soil can store carbon, but scaling it needs careful measurement."),
    ("17 Oct 2025", "Strengthening Multilateralism on the Road to COP30 and Beyond", "Act4Earth Dialogue, virtual.", "Global climate goals depend on countries working together."),
    ("7 Oct 2025", "DHI Urban Water Solutions", "Expert talk by Mr. Morten Just Kjølby, Product Portfolio Manager for MIKE+, DHI Denmark, at TERI SAS.", "City water systems can be modelled before problems reach the street."),
    ("16 Sep 2025", "Marine Resources for Sustainable Development", "Science Summit 2025.", "The ocean is part of the water story too."),
    ("5–7 Aug 2025", "QGreenland Educator Workshop", "Virtual. Designing teaching activities with QGreenland data.", "Polar data can be brought into any classroom."),
    ("25 Jul 2025", "Roots to Resilience Seminar", "TERI SAS with UNEP, UNESCO and Akashvani.", "Resilience starts with communities and ecosystems."),
    ("5–7 Mar 2025", "World Sustainable Development Summit 2025", "New Delhi. Partnerships for Accelerating Sustainable Development and Climate Solutions.", "Partnerships decide how fast climate solutions move."),
    ("24 Oct 2024", "Groundwater and sustainable development", "Lecture by Professor John A. Cherry, Lee Kuan Yew Water Prize recipient.", "Groundwater is slow to pollute and slower to clean, so protecting it comes first."),
    ("", "Climate Skills: Seeds for Transition", "TERI SAS and TERI with the British Council and HSBC Bank.", "Every green transition needs people with the right skills."),
]
entries = "".join(f'<div class="entry"><span class="d">{d}</span><div><h3>{t}</h3><p>{w}</p><p class="take">{tk}</p></div></div>' for d, t, w, tk in EVENTS)
talks = head("talks", "Expert talks, seminars and workshops attended", "Entries from my field notebook, each with one thing I took away.") + f'<div class="notebook">{entries}</div>'

# ---------------------------------------------------------------- 10 TRAINING
PATCHES = [
    ("uav", "UAV and drones", "Dec 2024", "#5B9E58", "Capacity Building Workshop on UAV/Drone Applications in Agriculture and Natural Resource Management",
     "10–12 December 2024. TERI SAS in collaboration with IIT BHU, IIT Roorkee, Namami Gange, Hokkaido University, GLP Earth, GLP Japan, Abhipsa Foundation and Kambil."),
    ("winter", "Winter School", "Nov–Dec 2024", "#1F6F80", "21-day Winter School Capacity Building Program in Geospatial Science and Technology",
     "18 November to 7 December 2024. Amity University, Noida, supported by the National Geospatial Program, Department of Science and Technology, Government of India."),
    ("fire", "Forest fire", "Mar 2024", "#B23A2C", "Harnessing Geospatial Technology for Forest Fire Disaster Management: Mapping, Monitoring and Mitigation",
     "One-week capacity building programme, 11–15 March 2024, Amity University, Noida."),
]
patches = "".join(f"""<button class="patch" type="button" data-patch="{k}" aria-expanded="{'true' if i == 0 else 'false'}" aria-controls="cert"><span class="emb" style="--pc:{c}"><span>{n}<small>{d}</small></span></span><span class="cap">{t}</span></button>"""
                  for i, (k, n, d, c, t, w) in enumerate(PATCHES))
p0 = PATCHES[0]
training = head("training", "Training, capacity building and schools", "Three programmes, three patches. Select a patch to read its certificate details.") + f"""
<div class="patches">{patches}</div>
<div class="cert" id="cert" aria-live="polite"><span class="t">Certificate of participation</span><h3>{p0[4]}</h3><p>{p0[5]}</p></div>"""

# ---------------------------------------------------------------- 11 RAPPORTEUR
MINUTES = [
    ("Rapporteur", "National Workshop on Geospatial Technology for Climate Action, Sustainability and Disaster Risk Reduction", "TERI School of Advanced Studies with NRSC, ISRO", "16–20 March 2026", ""),
    ("Rapporteur", "Ministerial Session: NDC 3.0 and Multilateralism on the Road to COP30 and COP33", "World Sustainable Development Summit 2025, TERI", "5–7 March 2025", "Partnerships for Accelerating Sustainable Development and Climate Solutions"),
    ("Rapporteur", "High-Level Plenary on Achieving Sustainable Development through Integrated Action", "World Sustainable Development Summit 2025, TERI", "5–7 March 2025", "Partnerships for Accelerating Sustainable Development and Climate Solutions"),
    ("Delegate", "World Sustainable Development Summit 2026, Silver Jubilee edition", "Taj Palace, Chanakyapuri, New Delhi", "25–27 February 2026", "Transformations: Vision, Voices, and Values for Sustainable Development and Climate Action"),
]
minutes = "".join(f"""<article class="minute"><div class="doc"><span>Minutes of session</span><span>{d}</span></div><h3>{t}</h3>
<table><tr><td>Role</td><td>{r}</td></tr><tr><td>Event</td><td>{e}</td></tr><tr><td>Date</td><td>{d}</td></tr></table>{f'<p class="theme">Theme: {th}</p>' if th else ''}</article>""" for r, t, e, d, th in MINUTES)
rapporteur = head("rapporteur", "Rapporteurship and academic and policy engagement", "Recording what was said in high-level sessions, and taking part as a delegate.") + f'<div class="minutes">{minutes}</div>'

# ---------------------------------------------------------------- 12 POSITIONS
IDS = [("Programme LEAD 2026", "Facilitator and Judge", "TERI SAS. Sustainable City Design Challenge for students of classes 9–12.", "2026", "PL"),
       ("Sustainability Hackathon 2025", "Judge and Panel Member", "TERI SAS. Evaluated school and undergraduate sustainability proposals, 18–19 November 2025.", "2025", "SH"),
       ("KnoxCode 2025", "Judge", "Geospatial Innovation Challenge by GeoknoX, TERI SAS, at Aahwaan Fest 2025. GIS, remote sensing, raster analysis and geospatial storytelling.", "2025", "KC")]
idcards = "".join(f"""<article class="idcard"><div class="top"><span>{org}</span><span>{yr}</span></div><div class="body"><span class="face" aria-hidden="true">{ini}</span><div><h3>{role}</h3><p>{d}</p></div></div></article>""" for org, role, d, yr, ini in IDS)
positions = head("positions", "Positions of responsibility", "") + f"""
<div class="idcards">{idcards}</div>
<div class="masthead"><div class="mh">Editor's corner<small>University of Delhi, 2018–2021</small></div>
<ul><li><b>Editor-in-Chief</b><span>Geography Association, University of Delhi, 2018–2021</span></li>
<li><b>Magazine Coordinator</b><span><em>Vani</em>, Shaheed Bhagat Singh College, 2018–2020</span></li>
<li><b>English Editor</b><span><em>Vani</em>, Shaheed Bhagat Singh College, 2019</span></li></ul></div>"""

# ---------------------------------------------------------------- 13 AWARDS
def cup(metal, big=False):
    m, d = metal, metal + "-d"
    return f"""<svg viewBox="0 0 100 130" aria-hidden="true"><path class="{m}" d="M22 8 h56 v28 a28 28 0 0 1 -56 0 z"/><path d="M22 14 h-12 a14 14 0 0 0 14 24 M78 14 h12 a14 14 0 0 1 -14 24" fill="none" stroke-width="5" stroke="{ {'gold':'#B98A24','silver':'#8F9AA1','bronze':'#94602F'}[metal] }"/>
<rect class="{d}" x="44" y="62" width="12" height="22"/><rect class="{m}" x="30" y="84" width="40" height="10" rx="2"/><rect class="wood" x="22" y="96" width="56" height="26" rx="3"/>{'<path d="M50 20 l4 9 10 1 -8 6 3 10 -9 -6 -9 6 3 -10 -8 -6 10 -1z" fill="#fff" opacity=".7"/>' if big else ''}</svg>"""


def medal(metal):
    return f"""<svg viewBox="0 0 100 130" aria-hidden="true"><path d="M32 4 L50 50 L68 4 Z" fill="#1F6F80"/><path d="M40 4 L50 40 L60 4 Z" fill="#B23A2C"/><circle class="{metal}-d" cx="50" cy="82" r="32"/><circle class="{metal}" cx="50" cy="82" r="25"/><path d="M50 66 l4 9 10 1 -8 6 3 10 -9 -6 -9 6 3 -10 -8 -6 10 -1z" fill="#fff" opacity=".6"/></svg>"""


def scroll():
    return """<svg viewBox="0 0 100 130" aria-hidden="true"><rect x="18" y="30" width="64" height="80" rx="3" fill="#F4EBD6"/><rect x="12" y="24" width="76" height="12" rx="6" fill="#D8C49A"/><rect x="12" y="104" width="76" height="12" rx="6" fill="#D8C49A"/><path d="M28 50 h44 M28 62 h44 M28 74 h30" stroke="#8A5A2B" stroke-width="3"/><circle cx="66" cy="90" r="9" fill="#B23A2C"/></svg>"""


def trophy(svg, title, sub, big=False):
    return f'<div class="trophy{" big" if big else ""}">{svg}<div class="plaque"><b>{title}</b><span>{sub}</span></div></div>'


awards = head("awards", "Awards and achievements", "The newest and biggest at the front of the shelf.") + f"""
<div class="shelf">
  {trophy(cup('silver'), '2nd rank, Map Making Competition', 'Amity University, 2025')}
  {trophy(cup('gold', True), 'First Position and Best Paper Award', 'ICSSR EHP NEXUS 2026, Gautam Buddha University', True)}
  {trophy(scroll(), 'PhD coursework CGPA 9.0/10', 'TERI SAS')}
</div>
<div class="shelf">
  {trophy(medal('gold'), 'State Child Scientist Award', 'National Science Congress, 2018')}
  {trophy(medal('silver'), 'Top 3 in English Olympiads', 'British Olympiad Foundation, 2015–2018, four years running')}
  {trophy(medal('bronze'), 'Merit Awards', '2016 and 2018')}
  {trophy(cup('bronze'), '20 cultural and general knowledge awards', 'Various organisations, including prizes in dance')}
</div>"""

# ---------------------------------------------------------------- 14 BEYOND
ICONS = {
    "Old coins": '<circle cx="27" cy="29" r="20" fill="#C9A044"/><circle cx="27" cy="29" r="15" fill="none" stroke="#8E6B22" stroke-width="2"/><text x="27" y="35" text-anchor="middle" font-size="16" font-weight="700" fill="#5A4210">₹</text>',
    "Stamps": '<rect x="8" y="9" width="38" height="40" fill="#fff" stroke="#B23A2C" stroke-width="2" stroke-dasharray="3 2"/><rect x="14" y="15" width="26" height="22" fill="#1F6F80"/><circle cx="37" cy="40" r="9" fill="none" stroke="#2A1E14" stroke-width="1.5"/>',
    "Historic stories": '<path d="M6 12 q11 -5 21 2 q10 -7 21 -2 v32 q-11 -5 -21 2 q-10 -7 -21 -2z" fill="#F4EBD6" stroke="#6B4A2E" stroke-width="2"/><path d="M27 14 v32" stroke="#6B4A2E" stroke-width="2"/>',
    "Photography": '<rect x="6" y="16" width="42" height="28" rx="4" fill="#2A1E14"/><rect x="18" y="11" width="14" height="7" rx="2" fill="#2A1E14"/><circle cx="27" cy="30" r="9" fill="#6FA8C8" stroke="#E9DFC9" stroke-width="2"/>',
    "Travelling": '<circle cx="27" cy="29" r="20" fill="#F4EBD6" stroke="#2A1E14" stroke-width="2"/><path d="M27 12 l5 17 -5 17 -5 -17z" fill="#B23A2C"/><path d="M27 29 l5 0 -5 17z" fill="#2A1E14"/>',
    "Badminton": '<path d="M20 34 l7 -24 7 24z" fill="#fff" stroke="#2A1E14" stroke-width="1.5"/><path d="M22 28 h10 M24 20 h6" stroke="#2A1E14" stroke-width="1"/><circle cx="27" cy="40" r="7" fill="#C9A044"/>',
    "Dance": '<path d="M12 22 q15 10 30 0" stroke="#8E6B22" stroke-width="3" fill="none"/><circle cx="16" cy="32" r="5" fill="#C9A044"/><circle cx="27" cy="36" r="5" fill="#C9A044"/><circle cx="38" cy="32" r="5" fill="#C9A044"/>',
    "Writing": '<path d="M14 44 l4 -12 22 -22 8 8 -22 22z" fill="#1F6F80"/><path d="M14 44 l4 -12 8 8z" fill="#F4EBD6"/><path d="M8 48 h38" stroke="#2A1E14" stroke-width="2"/>',
}
tray = "".join(f'<div class="cell"><svg viewBox="0 0 54 54" aria-hidden="true">{svg}</svg><span>{n}</span></div>' for n, svg in ICONS.items())
beyond = head("beyond", "Beyond the CV", "Where old mapmakers drew sea monsters, I keep my hobbies.") + f"""
<div class="offmap"><p class="here-be">Here be coins, stamps, stories and a badminton racket</p><div class="tray">{tray}</div></div>
<div class="beyond-grid">
  <div><h3 class="sub" style="margin-top:0">Volunteering</h3><ul><li>Volunteer, SWAPO NGO, since 2016</li><li>National Service Scheme (NSS), 2019–2021</li><li>Coordination of Volunteers, Vasundhara, 2018–2019</li><li>Personal blogging and content writing, 2018–2023</li></ul></div>
  <div><h3 class="sub" style="margin-top:0">Places I want to research</h3><ul><li>The Himalaya and High Mountain Asia</li><li>The Arctic</li><li>Antarctica</li><li>Historic and archaeological landscapes, from space</li></ul></div>
</div>"""

# ---------------------------------------------------------------- 15 CONTACT
contact = head("contact", "Contact", "") + f"""
<div class="postcard-back">
  <div class="stamps"><a href="{L['scholar']}" style="--sc:#4F7F86">Google Scholar</a><a href="{L['orcid']}" style="--sc:#5B9E58">ORCID</a><a href="{L['researchgate']}" style="--sc:#2A8E86">Research Gate</a><a href="{L['linkedin']}" style="--sc:#1F5E9E">LinkedIn</a><a href="{L['github']}" style="--sc:#2A1E26">GitHub</a></div>
  <p class="msg">Thanks for visiting! If you work on groundwater, remote sensing or anything in between, I'd love to hear from you. I'm open to collaborations.<br><br>Kavya</p>
  <div class="addr">
    <div class="line"><a href="mailto:{L['teri']}">{L['teri']}</a><button class="copy" type="button" data-copy="{L['teri']}">Copy</button></div>
    <div class="line"><a href="mailto:{L['gmail']}">{L['gmail']}</a><button class="copy" type="button" data-copy="{L['gmail']}">Copy</button></div>
    <div class="line">Department of Natural &amp; Applied Sciences</div>
    <div class="line">TERI School of Advanced Studies, Vasant Kunj Institutional Area</div>
    <div class="line">New Delhi 110070, India</div>
  </div>
</div>
<div class="locator">
  <svg viewBox="0 0 180 180" role="img" aria-label="Locator: TERI SAS at {TERI}">
    <rect width="180" height="180" rx="12" fill="var(--bg-2)"/>
    <g stroke="var(--line)" fill="none"><circle cx="90" cy="90" r="25"/><circle cx="90" cy="90" r="50"/><circle cx="90" cy="90" r="75"/><path d="M90 6 V174 M6 90 H174"/></g>
    <path d="M90 92 c0 0 -16 -18 -16 -30 a16 16 0 0 1 32 0 c0 12 -16 30 -16 30z" fill="var(--hot)"/><circle cx="90" cy="62" r="6" fill="var(--surface)"/>
    <text x="90" y="116" text-anchor="middle" style="font:600 11px var(--display);fill:var(--ink)">TERI SAS</text>
    <text x="90" y="131" text-anchor="middle" style="font:10px var(--display);fill:var(--ink-soft)">{TERI}</text>
  </svg>
  <p>Find me at the Department of Natural &amp; Applied Sciences, TERI School of Advanced Studies, in Vasant Kunj, South West Delhi.</p>
</div>"""

# ---------------------------------------------------------------- PAGE
layers = "".join(f"""<li class="layer" data-for="{cid}"><input type="checkbox" checked aria-label="Show {name}" data-toggle="{cid}"><span class="sw" style="background:{sw}"></span><a href="#{cid}">{name}</a></li>"""
                 for cid, name, sw, co, pl in CHAPTERS)
body = "\n".join([
    chapter("summary", summary, "Summary"), chapter("education", education, "Education"), chapter("research", research, "Research"),
    chapter("teaching", teaching, "Teaching"), chapter("projects", projects, "Projects"), chapter("publications", publications, "Publications"),
    chapter("skills", skills, "Skills"), chapter("conferences", conferences, "Conferences"), chapter("talks", talks, "Talks attended"),
    chapter("training", training, "Training"), chapter("rapporteur", rapporteur, "Rapporteurship"), chapter("positions", positions, "Positions"),
    chapter("awards", awards, "Awards"), chapter("beyond", beyond, "Beyond the CV"), chapter("contact", contact, "Contact"),
])

import json
patch_data = json.dumps({k: {"t": t, "w": w} for k, n, d, c, t, w in PATCHES})
detail_data = json.dumps(details_obj)

html = f"""<!doctype html>
<html lang="en" data-band="false">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Kavya Agrawal</title>
<meta name="description" content="Kavya Agrawal, PhD scholar at TERI School of Advanced Studies, New Delhi: groundwater contamination, remote sensing, GIS and machine learning.">
<meta property="og:title" content="Kavya Agrawal">
<meta property="og:description" content="PhD scholar in groundwater, remote sensing and machine learning, TERI SAS, New Delhi.">
<meta property="og:image" content="https://kavyaagrawal-02.github.io/new/assets/img/kavya-portrait-hero.jpg">
<link rel="icon" href="assets/img/favicon-32.png" sizes="32x32">
<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,500;12..96,600;12..96,700;12..96,800&family=Caveat:wght@500&family=Literata:ital,opsz,wght@0,7..72,400;0,7..72,500;1,7..72,400&display=swap" rel="stylesheet">
<script>try{{var b=localStorage.getItem('band');if(b)document.documentElement.dataset.band=b;}}catch(e){{}}</script>
<link rel="stylesheet" href="assets/site.css">
</head>
<body>
<a class="skip" href="#summary">Skip to content</a>
<button class="panel-toggle" type="button" aria-controls="panel" aria-expanded="false"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3 2 8l10 5 10-5-10-5zm-10 9 10 5 10-5M2 16l10 5 10-5" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/></svg>Layers</button>
<nav class="panel" id="panel" aria-label="Layers">
  <a class="me" href="#summary">Kavya Agrawal<small>PhD scholar, TERI SAS</small></a>
  <div class="search"><label class="vh" for="q">Search the site</label><input id="q" type="search" placeholder="Search the site" autocomplete="off"><ul class="results" id="results"></ul></div>
  <h2><span>Layers</span><span>{len(CHAPTERS)}</span></h2>
  <ul class="layers">{layers}</ul>
  <div class="bands" role="group" aria-label="Satellite band (colour theme)">
    <button type="button" data-band="true" aria-pressed="false">True colour</button>
    <button type="button" data-band="false" aria-pressed="false">False colour</button>
    <button type="button" data-band="thermal" aria-pressed="false">Thermal</button>
  </div>
  <p class="band-label">Band: switches the colour theme</p>
</nav>
<a class="plain-btn" href="cv.html"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 2h9l5 5v15H6z M14 2v6h6 M9 13h8 M9 17h8" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/></svg>Read the plain CV</a>
<div class="meter" aria-hidden="true"><svg viewBox="0 0 30 42"><defs><clipPath id="dc"><path d="M15 2c0 0-12 15-12 24a12 12 0 0 0 24 0C27 17 15 2 15 2z"/></clipPath></defs><rect id="drop-fill" x="0" y="40" width="30" height="1" fill="var(--accent)" clip-path="url(#dc)"/><path d="M15 2c0 0-12 15-12 24a12 12 0 0 0 24 0C27 17 15 2 15 2z" fill="none" stroke="currentColor" stroke-width="2"/></svg><span><span id="m-name">Summary</span><span class="c" id="m-coords">{TERI}</span></span></div>
<main id="main">
{body}
</main>
<footer class="foot"><div class="wrap"><span>Kavya Agrawal, PhD scholar, TERI School of Advanced Studies, New Delhi</span><span><a href="cv.html">Plain CV</a> &nbsp; <a href="mailto:{L['teri']}">{L['teri']}</a> &nbsp; Updated October 2026</span></div></footer>
<script>window.DETAILS={detail_data};window.PATCHES={patch_data};</script>
<script src="assets/site.js"></script>
</body>
</html>
"""
(OUT / "index.html").write_text(html, encoding="utf-8")
print("creative built", len(html) // 1024, "KB")
