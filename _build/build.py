"""Builds the five pages of kavyaagrawal-02.github.io.  Run: python3 _build/build.py
All content lives here. To add a paper, add a line to PUBS (newest first) and rebuild,
or edit publications.html and cv.html directly."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

L = {
    "teri": "kavya.agrawal@terisas.ac.in",
    "gmail": "kavyateriuniversity@gmail.com",
    "scholar": "https://scholar.google.com/citations?user=yXQUQ6YAAAAJ&hl=en",
    "orcid": "https://orcid.org/0009-0009-1032-2541",
    "researchgate": "https://www.researchgate.net/profile/Kavya-Agrawal-4",
    "linkedin": "https://www.linkedin.com/in/kavya-agrawal02/",
    "github": "https://github.com/kavyaagrawal-02",
}
PAGES = [("index.html", "Home"), ("research.html", "Research"), ("publications.html", "Publications"),
         ("teaching.html", "Teaching"), ("cv.html", "CV")]

CONTOUR = """<svg class="contour" viewBox="0 0 1200 28" preserveAspectRatio="none" aria-hidden="true">
<path d="M0 20 C 150 8, 300 26, 470 14 S 800 4, 960 16 S 1130 24, 1200 12"/>
<path d="M0 25 C 170 15, 320 28, 490 20 S 820 11, 980 22 S 1140 28, 1200 19" opacity=".6"/></svg>"""
DL = '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M8 2v8m0 0-3-3m3 3 3-3M3 13h10" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'


def page(fname, title, desc, body):
    cur = ' aria-current="page"'
    nav = "".join(f'<li><a href="{f}"{cur if f == fname else ""}>{n}</a></li>' for f, n in PAGES)
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="author" content="Kavya Agrawal">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="https://kavyaagrawal-02.github.io/assets/img/kavya-portrait-hero.jpg">
<link rel="icon" href="assets/img/favicon-32.png" sizes="32x32">
<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
<link rel="preload" href="assets/fonts/Newsreader.woff" as="font" type="font/woff" crossorigin>
<link rel="stylesheet" href="assets/site.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-head">
  <div class="wrap">
    <a class="name" href="index.html">Kavya Agrawal</a>
    <nav aria-label="Main"><ul class="nav">{nav}</ul></nav>
  </div>
  <div class="wrap">{CONTOUR}</div>
</header>
<main id="main"><div class="wrap">
{body}
</div></main>
<footer class="site-foot"><div class="wrap">
  <span class="coords">28°32′N 77°09′E, TERI School of Advanced Studies, New Delhi</span>
  <span><a href="mailto:{L['teri']}">{L['teri']}</a> &nbsp;·&nbsp; Updated October 2026</span>
</div></footer>
</body>
</html>
"""
    (ROOT / fname).write_text(html, encoding="utf-8")


def entry(when, title, meta="", text="", methods="", status="", award=False):
    parts = [f"<h3>{title}</h3>"]
    if meta: parts.append(f'<p class="meta">{meta}</p>')
    if text: parts.append(f'<p class="desc">{text}</p>')
    if methods: parts.append(f'<p class="methods">{methods}</p>')
    if status: parts.append(f'<span class="status{" award" if award else ""}">{status}</span>')
    return f'<li class="entry"><span class="when">{when}</span><div>{"".join(parts)}</div></li>'


def lst(items):
    return '<ul class="list">' + "".join(items) + "</ul>"


# ================================================================= DATA
PUBS = [
    entry("2023", "Evaluating spatial and elevation-wise daytime/nighttime LST trends across the Indus River Basin",
          'Mal, S., <strong>Agrawal, K.</strong>, Rani, S. et al. <em>Journal of Mountain Science</em> 20, 3154–3172. '
          '<a href="https://doi.org/10.1007/s11629-023-8157-8">doi.org/10.1007/s11629-023-8157-8</a>'),
    entry("2023", "Analyzing the Possibilities and Prospects of 24/7 Water Supply in Delhi, India",
          'Sanu, S. K., Chandrakanta, <strong>Agrawal, K.</strong>, Sharma, V. R., &amp; Bajaj, A. <em>Journal of Indian Water Works Association</em>, LV(1). UGC-CARE Group I, ISSN 0970-275X.'),
]
MANUSCRIPTS = [
    entry("2025–26", "Predicting Uranium Occurrences in Groundwater throughout India", "Research paper", status="Submitted to journal"),
    entry("2026", "Comparing and Benchmarking Deep Learning Models for Predicting Groundwater Contamination caused by Fluoride with the effects of Spatial Resolution on Prediction", "Research paper", status="In progress"),
    entry("2026", "A Physically Informed Framework for Multi-Resolution Downscaling and Upscaling of Environmental Predictors (Satellite Data)", "Research paper", status="In progress"),
]
TALKS = [
    entry("Apr 2026", "Machine-Learning-Based Uranium Risk Assessment, Population Exposure and Groundwater Governance",
          "ICSSR EHP NEXUS 2026, Track 10: AI and Predictive Analytics, Gautam Buddha University, 27–28 April 2026.",
          status="First Position, oral presentation, and Best Paper Award", award=True),
    entry("Oct 2024", "Distribution, Speciation and Controls on As Mobilization in the Groundwater in Aquifers of the Middle Gangetic Plain, India",
          "9th International Congress &amp; Exhibition on Arsenic in the Environment (As2024), KIIT Deemed to be University, Bhubaneswar, 20–24 October 2024. Poster."),
    entry("Nov 2022", "Problems and Prospects of Delhi's Drinking Water Supply",
          "IGU Thematic Conference on Sustainability, Future Earth and Humanities, Department of Geography, Central University of Haryana, Mahendragarh, 24–25 November 2022."),
    entry("Jul 2022", "Educational Relevance of Ramayana in Modern India",
          "National Seminar on Promoting Human Values and Culture for Peaceful Co-Existence, Amity University Haryana, sponsored by ICPR, 22 July 2022."),
    entry("May 2022", "Digital Enhancement of Physical Space and Connective Turn in Tourism Industry during and Post-COVID-19 Period",
          "International Conference on Geography and the Digital: Intersections and Conflations, Department of Geography, Delhi School of Economics, University of Delhi, 23–25 May 2022."),
    entry("May 2022", "Migrant College Students during Covid Pandemic: Evidence from the Field",
          "Jamia International Conference on Education 2022, Faculty of Education, Jamia Millia Islamia, New Delhi, 6–8 May 2022."),
    entry("Apr 2022", "Migrant College Students during Covid Pandemic: Evidence from the Field",
          "International Conference on Challenges to Disaster Risk Reduction and Resilient Habitat, Centre for Disaster Management Studies, Shaheed Bhagat Singh College, University of Delhi, 5–6 April 2022."),
]
TEACHING = [
    entry("Jun–Dec 2026", "Principles of GIS and GNSS (NRG176)", "MSc Geoinformatics, TERI School of Advanced Studies. 4 credits, 60 hours (L-T-P 42-2-32).", status="Course teaching"),
    entry("Jun–Dec 2026", "Principles of Remote Sensing (NRG169)", "MSc Geoinformatics, TERI School of Advanced Studies. 4 credits, 60 hours (L-T-P 42-2-32).", status="Course teaching"),
    entry("Jul–Dec 2025", "Principles of Remote Sensing (NRG169)", "MSc Geoinformatics, TERI School of Advanced Studies. 32 practical learning hours.", status="Course taught"),
]
EDUCATION = [
    entry("2024 – present", "PhD, Natural &amp; Applied Sciences", "TERI School of Advanced Studies, New Delhi. Coursework CGPA 9.0/10."),
    entry("2021 – 2023", "MA Geography", "Dr. B.R. Ambedkar University, Agra. CGPA 7.60."),
    entry("2018 – 2021", "BA (Honours) Geography", "University of Delhi. CGPA 7.86."),
    entry("2016 – 2018", "Senior Secondary School", "Delhi Public School, Aligarh. CGPA 9.80."),
    entry("2014 – 2016", "Secondary School", "St. Francis Inter College, Hathras. CGPA 9.20."),
]
CURRENT = [
    entry("2025 – 26", "Uranium in groundwater across India",
          text="A national-scale model of where uranium occurs in India's groundwater, built from groundwater observations and environmental predictors and checked against an independent validation dataset. The predictions are turned into spatial risk classes, estimates of population exposure, and governance indicators showing where monitoring and action are most needed.",
          methods="<b>Methods:</b> automated machine learning (AutoGluon), independent validation, spatial risk mapping, exposure assessment.",
          status="Paper submitted to journal; Best Paper Award, ICSSR EHP NEXUS 2026", award=False),
    entry("2026 –", "Fluoride and the effect of spatial resolution",
          text="India-wide prediction of fluoride contamination, benchmarking deep learning models and testing how the resolution of environmental predictors changes the result. Predictor stacks are built in Google Earth Engine at native resolution and at 500 m, 1 km and 5 km, keeping every groundwater observation in the data.",
          methods="<b>Methods:</b> deep learning, multi-resolution predictor extraction, 1.5 mg/L threshold.",
          status="In progress"),
    entry("2026 –", "Downscaling and upscaling environmental predictors",
          text="A physically informed framework for moving satellite data between coarse and fine resolutions without inventing detail. A pilot on CHIRPS rainfall over Punjab (2013–2022) targets 5 km, 1 km and 500 m using sub-pixel fractions and conservation-based aggregation.",
          methods="<b>Methods:</b> machine learning, conservation-based aggregation; validated with Moran's I, semivariograms and aggregation consistency.",
          status="In progress"),
    entry("2024 – 25", "Arsenic in the Middle Gangetic Plain",
          text="The distribution, speciation and controls on arsenic mobilisation in the aquifers of the Middle Gangetic Plain, looking at geogenic and hydrogeochemical factors such as pH, iron, redox potential and sulfate.",
          methods="<b>Methods:</b> hydrogeochemistry, explainable AI (SHAP, LIME).",
          status="Presented at As2024, Bhubaneswar"),
]
EARLIER = [
    entry("2023", "Land surface temperature trends across the Indus River Basin",
          text="Spatial and elevation-wise trends in daytime and nighttime land surface temperature across the Indus River Basin.",
          methods="<b>Methods:</b> Google Earth Engine (JavaScript), ArcGIS, Mann–Kendall and Theil–Sen trend analysis.",
          status="Published, Journal of Mountain Science"),
    entry("2023", "Identification and mapping of permafrost in the Indus Basin",
          text="Mapping likely permafrost from about twenty years of mean annual air temperature (MAAT), potential incoming solar radiation (PISR), BMAT, snow and precipitation estimates in Google Earth Engine."),
    entry("2023", "Snow cover and changes in Indian basins"),
]
PG = ["Measuring the Problems and Emotions of Urban-Ward Migrants: A Case Study of Construction Workers in Delhi",
      "Monitoring the Effects of Light Pollution &amp; Evaluating the Effectiveness of Indian Regulations",
      "Community Awareness, Participation, &amp; CCDRR: Reflections from North-West India",
      "Experience of Migrant College Students During COVID-19 Pandemic",
      "Analyzing the Possibilities and Prospects of 24/7 Water Supply in Delhi, India",
      "Geography of Ramayana",
      "Digital Enhancement of Physical Space and Connective Turn in the Tourism Industry during and Post-COVID-19 Period"]
UG = ["Forest Monitoring &amp; Urban Sprawl Analysis Using GIS in Delhi",
      "LULC Change Detection for 20 Years in South-West Delhi",
      "Social Indicators &amp; Status Analysis of Jammu &amp; Kashmir",
      "Socio-Economic Impact of COVID-19 in Delhi",
      "Snow Cover &amp; Changes in Indian Basins",
      "HRVC Analysis of Jim Corbett",
      "Studying Human Trafficking in Delhi through Remote Sensing",
      "Understanding Ansal Plaza Mall of South Delhi as a Gendered Landscape: A Temporal Study"]
EXPLORE = ["Permafrost identification, modelling and assessment", "Glacier, ice and snow mapping",
           "Climate change assessments and impacts", "High Mountain Asia, the Himalaya, the Arctic and Antarctica",
           "Remote sensing for history and archaeology"]


def ul(items, cls="plain-list"):
    return f'<ul class="{cls}">' + "".join(f"<li>{x}</li>" for x in items) + "</ul>"


PROFILE_LINKS = f"""<a href="mailto:{L['teri']}">Email</a><a href="{L['scholar']}">Google Scholar</a><a href="{L['orcid']}">ORCID</a>
<a href="{L['researchgate']}">ResearchGate</a><a href="{L['linkedin']}">LinkedIn</a><a href="{L['github']}">GitHub</a>"""

# ================================================================= HOME
NEWS = [
    entry("Jun 2026", "Teaching <em>Principles of Remote Sensing</em> and <em>Principles of GIS and GNSS</em> in the MSc Geoinformatics programme."),
    entry("Apr 2026", "First Position and Best Paper Award at ICSSR EHP NEXUS 2026, Gautam Buddha University, for machine-learning-based uranium risk assessment."),
    entry("Mar 2026", "Rapporteur at the National Workshop on Geospatial Technology for Climate Action, Sustainability and Disaster Risk Reduction (TERI SAS with NRSC, ISRO)."),
    entry("Feb 2026", "Delegate at the World Sustainable Development Summit 2026."),
    entry("Jan 2026", "Completed the PhD comprehensive examination, and submitted the uranium paper to a journal."),
]
home = f"""
<div class="intro">
  <div>
    <h1>Kavya Agrawal</h1>
    <p class="role">PhD Scholar, Department of Natural &amp; Applied Sciences<br>TERI School of Advanced Studies, New Delhi</p>
    <p>I am a PhD scholar working at the intersection of environmental systems, human activity and technology. My doctoral research focuses on large-scale prediction and risk assessment of groundwater contamination in India, integrating hydrogeochemistry and environmental geoinformatics with remote sensing, GIS and multi-source environmental data.</p>
    <p>I work across uranium, fluoride and arsenic contamination, using machine learning, deep learning and spatial modelling to understand contamination patterns, their environmental controls and where risk is highest. My broader interests include population exposure, groundwater governance, climate and cryosphere systems, environmental change and water security. I am always open to new questions, methods and collaborations.</p>
    <p class="muted small" style="margin-top:1.2rem">Supervisor: Prof. Chander Kumar Singh &nbsp;·&nbsp; Co-supervisor: Dr. Adwitiya Sinha</p>
    <div class="links">{PROFILE_LINKS}</div>
    <p style="margin-top:1.6rem"><a class="btn" href="Kavya_Agrawal_CV.pdf">{DL}Download CV (PDF)</a></p>
  </div>
  <figure class="portrait">
    <img src="assets/img/kavya-portrait-hero.jpg" alt="Portrait of Kavya Agrawal" width="499" height="484">
    <figcaption>{L['teri']}</figcaption>
  </figure>
</div>
<section><h2>Research interests</h2>
<p class="interests">Groundwater quality and contamination (uranium, fluoride, arsenic) · hydrogeochemistry · remote sensing and GIS · machine learning, AutoML and explainable AI · multi-resolution modelling and downscaling · population exposure and groundwater governance · cryosphere and climate · water security.</p></section>
<section class="news"><h2>News</h2>{lst(NEWS)}</section>
"""
page("index.html", "Kavya Agrawal", "Kavya Agrawal, PhD scholar at TERI School of Advanced Studies, New Delhi: groundwater contamination, remote sensing, GIS and machine learning.", home)

# ================================================================= RESEARCH
research = f"""
<div class="col">
<h1 class="page-title">Research</h1>
<p class="lede">How far can we predict groundwater contamination across a country as large and varied as India, and what do those predictions mean for the people who drink the water?</p>
</div>
<section><h2>Doctoral research</h2>
<div class="col">
<p><em>Development of an Adaptable Machine Learning Based Framework for Multi-Contaminant Prediction</em></p>
<p>My PhD builds a national-scale framework for predicting groundwater contamination and assessing its risk. It combines groundwater observations and hydrochemistry with remote sensing and GIS layers on climate, hydrology, terrain, soil, geology, land use, human modification and population. The aims run from prediction and spatial risk mapping to testing uncertainty and robustness, understanding environmental controls, estimating exposure and supporting governance decisions.</p>
<p class="muted small">Supervisor: Prof. Chander Kumar Singh. Co-supervisor: Dr. Adwitiya Sinha. Registered February 2024; comprehensive examination completed January 2026.</p>
</div></section>
<section><h2>Current work</h2>{lst(CURRENT)}</section>
<section><h2>Earlier work: climate and cryosphere</h2>{lst(EARLIER)}
<figure class="figure col"><img src="assets/img/indus-study-area.png" alt="Study area map of the Indus River Basin showing elevation, rivers and major cities" loading="lazy" width="1022" height="739">
<figcaption>The Indus River Basin, study area of the 2023 land surface temperature paper.</figcaption></figure></section>
<section><h2>Questions I would like to explore</h2>{ul(EXPLORE)}</section>
<section><h2>Projects</h2>
<h3>Postgraduate, 2021–2023</h3>{ul(PG)}
<h3>Undergraduate, 2018–2021</h3>{ul(UG)}</section>
"""
page("research.html", "Research, Kavya Agrawal", "Groundwater contamination prediction across India with remote sensing, GIS and machine learning: uranium, fluoride, arsenic and downscaling.", research)

# ================================================================= PUBLICATIONS
publications = f"""
<div class="col"><h1 class="page-title">Publications</h1>
<p class="lede">Journal articles, manuscripts and conference presentations, newest first.</p>
<div class="links"><a href="{L['scholar']}">Google Scholar</a><a href="{L['orcid']}">ORCID 0009-0009-1032-2541</a><a href="{L['researchgate']}">ResearchGate</a></div></div>
<section><h2>Journal articles</h2>{lst(PUBS)}</section>
<section><h2>Manuscripts</h2>{lst(MANUSCRIPTS)}</section>
<section><h2>Conference presentations</h2>{lst(TALKS)}</section>
"""
page("publications.html", "Publications, Kavya Agrawal", "Journal articles, manuscripts and conference presentations by Kavya Agrawal.", publications)

# ================================================================= TEACHING
teaching = f"""
<div class="col"><h1 class="page-title">Teaching</h1>
<p class="lede">Course teaching in the MSc Geoinformatics programme at TERI School of Advanced Studies.</p></div>
<section><h2>Courses</h2>{lst(TEACHING)}</section>
<section><h2>In the lab</h2><div class="col">
<p>Practical sessions cover GPS and GNSS, satellite navigation, georeferencing, ArcGIS Pro, ERDAS Imagine and Landsat 8/9 imagery, with applied exercises in urban pattern, vegetation and geomorphology analysis.</p></div>
<figure class="figure"><img src="assets/img/delhi-lulc.png" alt="Land use and land cover classification map of South West Delhi from Landsat 8, October 2019" loading="lazy" width="919" height="589">
<figcaption>Land use and land cover of South West Delhi from Landsat 8 (October 2019), the kind of classification students learn in the lab.</figcaption></figure></section>
"""
page("teaching.html", "Teaching, Kavya Agrawal", "Courses taught by Kavya Agrawal in the MSc Geoinformatics programme at TERI SAS.", teaching)

# ================================================================= CV
CV_SECTIONS = []


def cvs(id_, title, body):
    CV_SECTIONS.append((id_, title, f'<section id="{id_}"><h2>{title}</h2>{body}</section>'))


cvs("education", "Education", lst(EDUCATION))
cvs("doctoral", "Doctoral research", lst([
    entry("Thesis", "Development of an Adaptable Machine Learning Based Framework for Multi-Contaminant Prediction"),
    entry("Supervisors", "Prof. Chander Kumar Singh (supervisor); Dr. Adwitiya Sinha (co-supervisor)"),
    entry("Status", "Full-time. Registered 1 February 2024. Comprehensive examination completed 28 January 2026."),
    entry("Coursework", "Research and Publication Ethics (RPR275), A; Research Methodology (RPR271), A; Environmental Statistics (NRE115), A; Digital Image Processing &amp; Information Extraction (NRG172), A"),
]))
cvs("research", "Research experience", lst(CURRENT + EARLIER))
cvs("publications", "Publications", lst(PUBS))
cvs("manuscripts", "Manuscripts", lst(MANUSCRIPTS))
cvs("conferences", "Conference presentations", lst(TALKS))
cvs("teaching", "Teaching", lst(TEACHING))
cvs("projects", "Projects", f"<h3>Postgraduate, 2021–2023</h3>{ul(PG)}<h3>Undergraduate, 2018–2021</h3>{ul(UG)}")
cvs("awards", "Awards and achievements", lst([
    entry("2026", "First Position, oral presentation, and Best Paper Award", "ICSSR EHP NEXUS 2026, Gautam Buddha University."),
    entry("2025", "2nd Rank, Map Making Competition", "Amity University."),
    entry("2018", "State Child Scientist Award", "National Science Congress."),
    entry("2015 – 2018", "Consecutive top 3 ranks, English Olympiads", "British Olympiad Foundation."),
    entry("2016, 2018", "Merit Awards"),
    entry("", "20 cultural and general knowledge awards", "From various organisations, including prizes in dance."),
]))
cvs("rapporteur", "Rapporteurship and policy engagement", lst([
    entry("Mar 2026", "Rapporteur, National Workshop on Geospatial Technology for Climate Action, Sustainability and Disaster Risk Reduction", "TERI School of Advanced Studies in collaboration with NRSC, ISRO, 16–20 March 2026."),
    entry("Feb 2026", "Delegate, World Sustainable Development Summit 2026", "Taj Palace, New Delhi, 25–27 February 2026. Transformations: Vision, Voices, and Values for Sustainable Development and Climate Action."),
    entry("Mar 2025", "Rapporteur, Ministerial Session: NDC 3.0 and Multilateralism on the Road to COP30 and COP33", "World Sustainable Development Summit 2025, TERI."),
    entry("Mar 2025", "Rapporteur, High-Level Plenary on Achieving Sustainable Development through Integrated Action", "World Sustainable Development Summit 2025, TERI."),
]))
cvs("positions", "Positions of responsibility", lst([
    entry("2026", "Facilitator and Judge, Programme LEAD 2026", "TERI SAS. Sustainable City Design Challenge for students of classes 9–12."),
    entry("Nov 2025", "Judge and Panel Member, TERI SAS Sustainability Hackathon 2025", "Expert evaluation panel for school and undergraduate sustainability proposals, 18–19 November 2025."),
    entry("2025", "Judge, KnoxCode 2025, Geospatial Innovation Challenge", "Organised by GeoknoX, TERI SAS, as part of Aahwaan Fest 2025."),
    entry("2018 – 2021", "Editor-in-Chief, Geography Association", "University of Delhi."),
    entry("2018 – 2020", "Magazine Coordinator, <em>Vani</em>", "Shaheed Bhagat Singh College, University of Delhi."),
    entry("2019", "English Editor, <em>Vani</em>", "Shaheed Bhagat Singh College, University of Delhi."),
]))
cvs("workshops", "Workshops, seminars and summits attended", lst([
    entry("Feb 2026", "Water as a Commons workshop, Water Governance Working Group", "With the Ostrom Workshop, Indiana University Bloomington and IU India Gateway, 26–27 February 2026; included a Yamuna River field visit with INTACH Delhi."),
    entry("Feb 2026", "Ambition to Action: Climathon, Delhi Climate Innovation Week", "Climate Career &amp; Sustainability Expo, Innovate X Delhi, 21 February 2026."),
    entry("Feb 2026", "Guest lecture: Soil Carbon Sequestration as a Climate Mitigation Mechanism", "Ms. Violeta Martinkė, Project Development Lead, InSoil, 13 February 2026."),
    entry("Oct 2025", "Act4Earth Dialogue: Strengthening Multilateralism on the Road to COP30 and Beyond", "Virtual, 17 October 2025."),
    entry("Oct 2025", "Expert talk: DHI Urban Water Solutions", "Mr. Morten Just Kjølby, Product Portfolio Manager for MIKE+, DHI Denmark, TERI SAS, 7 October 2025."),
    entry("Sep 2025", "Science Summit 2025: Marine Resources for Sustainable Development", "16 September 2025."),
    entry("Aug 2025", "QGreenland Educator Workshop", "Virtual, 5–7 August 2025. Developing educational activities with QGreenland data."),
    entry("Jul 2025", "Roots to Resilience Seminar", "TERI SAS with UNEP, UNESCO and Akashvani, 25 July 2025."),
    entry("Mar 2025", "World Sustainable Development Summit 2025", "New Delhi, 5–7 March 2025. Partnerships for Accelerating Sustainable Development and Climate Solutions."),
    entry("Oct 2024", "Lecture by Professor John A. Cherry on groundwater and sustainable development", "Lee Kuan Yew Water Prize recipient, 24 October 2024."),
    entry("", "Climate Skills: Seeds for Transition", "TERI SAS and TERI with British Council and HSBC Bank."),
]))
cvs("training", "Training, capacity building and schools", lst([
    entry("Mar 2026", "National Workshop on Geospatial Technology for Climate Action, Sustainability and Disaster Risk Reduction", "TERI SAS in collaboration with NRSC, ISRO, 16–20 March 2026. Participant, volunteer and rapporteur."),
    entry("Dec 2024", "Capacity Building Workshop on UAV/Drone Applications in Agriculture and Natural Resource Management", "TERI SAS with IIT BHU, IIT Roorkee, Namami Gange, Hokkaido University, GLP Earth, GLP Japan, Abhipsa Foundation and Kambil, 10–12 December 2024."),
    entry("Nov – Dec 2024", "21-day Winter School Capacity Building Program in Geospatial Science and Technology", "Amity University, Noida, supported by the National Geospatial Program, DST, Government of India, 18 November – 7 December 2024."),
    entry("Mar 2024", "Harnessing Geospatial Technology for Forest Fire Disaster Management: Mapping, Monitoring and Mitigation", "One-week capacity building programme, Amity University, Noida, 11–15 March 2024."),
]))
SK = [
    ("GIS and remote sensing", "Google Earth Engine (JavaScript), ArcGIS / ArcGIS Pro, QGIS, ERDAS Imagine, Google Earth; image enhancement and feature extraction, orthorectification and mosaicking, DEM processing, satellite image acquisition and processing."),
    ("Programming and machine learning", "Python, pandas; machine learning, deep learning and AutoML (AutoGluon); Random Forest, LightGBM; explainable AI (SHAP, LIME)."),
    ("Spatial analysis and statistics", "Spatial data analysis and visualisation; time-series modelling and trend analysis; Mann–Kendall test, Theil–Sen slope; Moran's I, semivariograms."),
    ("Earth observation and environmental data", "Landsat 8/9, Sentinel, MODIS, VIIRS, FIRMS, CHIRPS, IMD, ERA5-Land, TerraClimate, GLDAS, GRACE, SRTM, MERIT Hydro, JRC Global Surface Water, OpenLandMap, GPW, GHM, GHSL, SMOD, LCZ; CGWB hydrochemical observations."),
    ("Parameters", "MAAT, BMAT, PISR, land surface temperature, NDVI/NDBI, night-time light, snow, precipitation, slope, aerosols and solar radiation, hydrochemistry (pH, EC, major ions, nitrate, fluoride, uranium)."),
    ("Data quality", "Provenance and lineage, duplicate and sentinel-value handling, coordinate validation, unit checks, resolution harmonisation, independent validation, masked-pixel handling."),
    ("Research and field", "Field and survey-based research, socio-environmental data analysis, drinking-water quality assessment, disaster risk reduction, climate–water–environment interactions, sustainability and climate policy."),
    ("Professional", "Academic writing and conference presentations, scientific communication and reporting, editorial and content development, rapporteurship and policy documentation, academic coordination, interdisciplinary collaboration."),
]
cvs("skills", "Skills", '<div class="skills">' + "".join(f"<div><h3>{a}</h3><p>{b}</p></div>" for a, b in SK) + "</div>")
cvs("volunteering", "Volunteering and co-curricular", lst([
    entry("2016 – present", "Volunteer, SWAPO NGO"),
    entry("2019 – 2021", "National Service Scheme (NSS)"),
    entry("2018 – 2019", "Coordination of Volunteers, Vasundhara"),
    entry("2018 – 2023", "Personal blogging and content writing"),
]))
cvs("interests", "Interests", "<p>Collecting old coins and stamps, reading historic stories and accounts, photography and videography, travelling, badminton and dance.</p>")
cvs("contact", "Contact", f"""<p>Department of Natural &amp; Applied Sciences, TERI School of Advanced Studies, Vasant Kunj Institutional Area, New Delhi 110070, India</p>
<p><a href="mailto:{L['teri']}">{L['teri']}</a> &nbsp;·&nbsp; <a href="mailto:{L['gmail']}">{L['gmail']}</a></p>
<p class="links" style="margin-top:0"><a href="{L['scholar']}">Google Scholar</a><a href="{L['orcid']}">ORCID</a><a href="{L['researchgate']}">ResearchGate</a><a href="{L['linkedin']}">LinkedIn</a><a href="{L['github']}">GitHub</a></p>""")

toc = "".join(f'<li><a href="#{i}">{t}</a></li>' for i, t, _ in CV_SECTIONS)
cv = f"""
<div class="cv-head">
  <div><h1 class="page-title" style="margin-bottom:.2rem">Curriculum Vitae</h1>
  <p class="muted" style="margin:0">Kavya Agrawal, PhD Scholar, TERI School of Advanced Studies, New Delhi</p>
  <p class="print-only muted" style="margin:.2rem 0 0">{L['teri']} · {L['gmail']} · kavyaagrawal-02.github.io</p></div>
  <a class="btn no-print" href="Kavya_Agrawal_CV.pdf">{DL}Download PDF</a>
</div>
<ul class="toc" aria-label="CV sections">{toc}</ul>
{''.join(h for _, _, h in CV_SECTIONS)}
"""
page("cv.html", "CV, Kavya Agrawal", "Curriculum vitae of Kavya Agrawal, PhD scholar at TERI School of Advanced Studies, New Delhi.", cv)
print("built", len(PAGES), "pages")
