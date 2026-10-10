"""Builds new/cv.html: the plain CV, every item under its own heading."""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "new"
L = {
    "email": "mailto:kavya.agrawal@terisas.ac.in",
    "linkedin": "https://www.linkedin.com/in/kavya-agrawal02/",
    "scholar": "https://scholar.google.com/citations?user=yXQUQ6YAAAAJ&hl=en",
    "orcid": "https://orcid.org/0009-0009-1032-2541",
    "researchgate": "https://www.researchgate.net/profile/Kavya-Agrawal-4",
    "github": "https://github.com/kavyaagrawal-02",
}


def item(when, title, note="", badges=()):
    b = "".join(f'<span class="badge{" red" if red else ""}">{t}</span>' for t, red in badges)
    n = f"<p>{note}</p>" if note else ""
    return f'<li class="item"><span class="when">{when}</span><div><h4>{title}</h4>{n}{b}</div></li>'


def items(*rows):
    return '<ul class="items">' + "".join(item(*r) for r in rows) + "</ul>"


def simple(lst, cls="simple"):
    return f'<ul class="{cls}">' + "".join(f"<li>{x}</li>" for x in lst) + "</ul>"


SECTIONS = []


def sec(id_, title, body):
    SECTIONS.append((id_, title, f'<section id="{id_}"><h2>{title}</h2>{body}</section>'))


sec("about", "About", """
<p>I am a PhD scholar in Natural and Applied Sciences at the TERI School of Advanced Studies, New Delhi, working at the intersection of environmental systems, human activity and technology. My doctoral research focuses on large-scale prediction and risk assessment of groundwater contamination, integrating hydrogeochemistry and environmental geoinformatics with remote sensing, GIS and multi-source environmental data.</p>
<p>I work across uranium, fluoride and arsenic contamination, using machine learning, deep learning, AI and spatial modelling to investigate contamination patterns, environmental controls and spatially differentiated risk. My broader interests include population exposure, environmental vulnerability, groundwater governance, climate and cryosphere systems, environmental change and water security.</p>""")

sec("education", "Education", items(
    ("2024 to present", "PhD, Natural &amp; Applied Sciences", "TERI School of Advanced Studies, New Delhi. Coursework CGPA 9.0/10."),
    ("2021–2023", "MA Geography", "Dr. B.R. Ambedkar University, Agra. CGPA 7.60."),
    ("2018–2021", "BA (Honours) Geography", "University of Delhi. CGPA 7.86."),
    ("2016–2018", "Senior Secondary School", "Delhi Public School, Aligarh. CGPA 9.80."),
    ("2014–2016", "Secondary School", "St. Francis Inter College, Hathras. CGPA 9.20."),
))

sec("phd", "Doctoral research", f"""
{items(
    ("Thesis", "Development of an Adaptable Machine Learning Based Framework for Multi-Contaminant Prediction"),
    ("Supervisors", "Prof. Chander Kumar Singh (supervisor), Dr. Adwitiya Sinha (co-supervisor)"),
    ("Status", "Full-time. Registered February 2024. Comprehensive examination completed 28 January 2026."),
)}
<h3>PhD coursework</h3>
{simple(["RPR275 Research and Publication Ethics, 2 credits, grade A",
         "RPR271 Research Methodology, 3 credits, grade A",
         "NRE115 Environmental Statistics, 4 credits, grade A",
         "NRG172 Digital Image Processing &amp; Information Extraction, 4 credits, grade A"])}""")

sec("research", "Research areas", f"""
<h3>Current</h3>
{items(
    ("Uranium", "National-scale prediction of uranium in groundwater across India", "AutoML (AutoGluon) prediction with independent validation, spatial risk classes, population exposure and groundwater governance indicators for decision support."),
    ("Fluoride", "India-wide fluoride prediction and the effect of spatial resolution", "Benchmarking deep learning models; predictor stacks built at native, 500 m, 1 km and 5 km scales from Google Earth Engine."),
    ("Arsenic", "Arsenic mobilisation in the Middle Gangetic Plain", "Distribution, speciation and geogenic controls; pH, iron, redox potential and sulfate; explainable AI (SHAP, LIME)."),
    ("Downscaling", "Physically informed downscaling and upscaling of satellite predictors", "Sub-pixel fractions and conservation-based aggregation, piloted on CHIRPS precipitation over Punjab (2013–2022); validated with Moran's I, semivariograms and aggregation consistency."),
)}
<h3>Earlier</h3>
{items(
    ("2023", "Land surface temperature trends across the Indus River Basin", "Spatial and elevation-wise daytime and nighttime trends; Google Earth Engine, ArcGIS, Mann–Kendall and Theil–Sen."),
    ("2023", "Identification and mapping of permafrost in the Indus Basin", "About twenty years of MAAT, PISR, BMAT, snow and precipitation estimates in Google Earth Engine."),
    ("2023", "Snow cover and changes in Indian basins"),
)}
<h3>Interests I would like to explore</h3>
{simple(["Permafrost identification, modelling and assessment", "Glacier, ice and snow mapping",
         "Climate change assessments and impacts", "High Mountain Asia, the Himalaya, the Arctic and Antarctica",
         "Remote sensing for history and archaeology"])}""")

sec("publications", "Publications", f"""
<!-- To add a paper: copy one <li class="item"> ... </li> line in the HTML and edit it. Newest first. -->
{items(("Nov 2023", 'Mal, S., <strong>Agrawal, K.</strong>, Rani, S. et al. Evaluating spatial and elevation-wise daytime/nighttime LST trends across the Indus River Basin.',
        '<em>Journal of Mountain Science</em> 20, 3154–3172. <a href="https://doi.org/10.1007/s11629-023-8157-8">doi.org/10.1007/s11629-023-8157-8</a>', (("Published", False),)))}""")

sec("manuscripts", "Manuscripts", items(
    ("2025–2026", "Predicting Uranium Occurrences in Groundwater throughout India", "Research paper.", (("Submitted to journal", False),)),
    ("2026", "Comparing and Benchmarking Deep Learning Models for Predicting Groundwater Contamination caused by Fluoride with the effects of Spatial Resolution on Prediction", "Research paper.", (("In progress", False),)),
    ("2026", "A Physically Informed Framework for Multi-Resolution Downscaling and Upscaling of Environmental Predictors (Satellite Data)", "Research paper.", (("In progress", False),)),
))

sec("conferences", "Conference presentations", items(
    ("Apr 2026", "Machine-Learning-Based Uranium Risk Assessment, Population Exposure and Groundwater Governance", "ICSSR EHP NEXUS 2026, Track 10: AI and Predictive Analytics, Gautam Buddha University, 27–28 April 2026.", (("First Position, oral presentation", True), ("Best Paper Award", True))),
    ("Oct 2024", "Distribution, Speciation and Controls on As Mobilization in the Groundwater in Aquifers of the Middle Gangetic Plain, India", "9th International Congress &amp; Exhibition on Arsenic in the Environment (As2024), KIIT Deemed to be University, Bhubaneswar, 20–24 October 2024."),
    ("Nov 2022", "Problems and Prospects of Delhi's Drinking Water Supply", "IGU Thematic Conference on Sustainability, Future Earth and Humanities, Department of Geography, Central University of Haryana, 24–25 November 2022."),
    ("Jul 2022", "Educational Relevance of Ramayana in Modern India", "National Seminar on Promoting Human Values and Culture for Peaceful Co-Existence, Amity University Haryana, sponsored by ICPR, 22 July 2022."),
    ("May 2022", "Digital Enhancement of Physical Space and Connective Turn in Tourism Industry during and Post-COVID-19 Period", "International Conference on Geography and the Digital: Intersections and Conflations, Delhi School of Economics, University of Delhi, 23–25 May 2022."),
    ("May 2022", "Migrant College Students during Covid Pandemic: Evidence from the Field", "Jamia International Conference on Education 2022, Faculty of Education, Jamia Millia Islamia, 6–8 May 2022."),
    ("Apr 2022", "Migrant College Students during Covid Pandemic: Evidence from the Field", "International Conference on Challenges to Disaster Risk Reduction and Resilient Habitat, Shaheed Bhagat Singh College, University of Delhi, 5–6 April 2022."),
))

sec("teaching", "Teaching", items(
    ("Jun–Dec 2026", "Principles of GIS and GNSS (NRG176)", "MSc Geoinformatics, TERI SAS. 4 credits, 60 hours, L-T-P 42-2-32."),
    ("Jun–Dec 2026", "Principles of Remote Sensing (NRG169)", "MSc Geoinformatics, TERI SAS. 4 credits, 60 hours, L-T-P 42-2-32."),
    ("Jul–Dec 2025", "Principles of Remote Sensing (NRG169)", "MSc Geoinformatics, TERI SAS. 32 practical learning hours."),
) + "<p>Practical sessions cover GPS and GNSS, georeferencing, ArcGIS Pro, ERDAS Imagine, Landsat 8/9 imagery, and urban, vegetation and geomorphology analysis.</p>")

sec("projects", "Projects", f"""
<h3>Postgraduate projects, 2021–2023</h3>
{simple(["Measuring the Problems and Emotions of Urban-Ward Migrants: A Case Study of Construction Workers in Delhi",
         "Monitoring the Effects of Light Pollution &amp; Evaluating the Effectiveness of Indian Regulations",
         "Community Awareness, Participation, &amp; CCDRR: Reflections from North-West India",
         "Experience of Migrant College Students During COVID-19 Pandemic",
         "Analyzing the Possibilities and Prospects of 24/7 Water Supply in Delhi, India",
         "Geography of Ramayana",
         "Digital Enhancement of Physical Space and Connective Turn in the Tourism Industry during and Post-COVID-19 Period"])}
<h3>Undergraduate projects, 2018–2021</h3>
{simple(["Forest Monitoring &amp; Urban Sprawl Analysis Using GIS in Delhi",
         "LULC Change Detection for 20 Years in South-West Delhi",
         "Social Indicators &amp; Status Analysis of Jammu &amp; Kashmir",
         "Socio-Economic Impact of COVID-19 in Delhi",
         "HRVC Analysis of Jim Corbett",
         "Studying Human Trafficking in Delhi through Remote Sensing",
         "Understanding Ansal Plaza Mall of South Delhi as a Gendered Landscape: A Temporal Study"])}""")

sec("awards", "Awards and achievements", items(
    ("2026", "First Position, oral presentation, and Best Paper Award", "ICSSR EHP NEXUS 2026, Gautam Buddha University."),
    ("2025", "2nd rank, Map Making Competition", "Amity University."),
    ("2018", "State Child Scientist Award", "National Science Congress."),
    ("2015–2018", "Consecutive top 3 ranks, English Olympiads", "British Olympiad Foundation."),
    ("2016, 2018", "Merit Awards"),
    ("", "20 cultural and general knowledge awards", "From various organisations, including prizes in dance."),
))

sec("rapporteur", "Rapporteurship and policy engagement", items(
    ("Mar 2026", "Rapporteur, National Workshop on Geospatial Technology for Climate Action, Sustainability and Disaster Risk Reduction", "TERI SAS in collaboration with NRSC, ISRO, 16–20 March 2026."),
    ("Mar 2025", "Rapporteur, Ministerial Session: NDC 3.0 and Multilateralism on the Road to COP30 and COP33", "World Sustainable Development Summit 2025, TERI."),
    ("Mar 2025", "Rapporteur, High-Level Plenary on Achieving Sustainable Development through Integrated Action", "World Sustainable Development Summit 2025, TERI."),
))

sec("positions", "Positions of responsibility", items(
    ("2026", "Facilitator and Judge, Programme LEAD 2026", "TERI SAS. Sustainable City Design Challenge for students of classes 9–12."),
    ("Nov 2025", "Judge and Panel Member, TERI SAS Sustainability Hackathon 2025", "Expert evaluation panel for school and undergraduate sustainability proposals, 18–19 November 2025."),
    ("2025", "Judge, KnoxCode 2025 / Geospatial Innovation Challenge", "Organised by GeoknoX, TERI SAS, as part of Aahwaan Fest 2025."),
    ("2018–2021", "Editor-in-Chief, Geography Association", "University of Delhi."),
    ("2018–2020", "Magazine Coordinator, <em>Vani</em>", "Shaheed Bhagat Singh College, University of Delhi."),
    ("2019", "English Editor, <em>Vani</em>", "Shaheed Bhagat Singh College, University of Delhi."),
))

sec("summits", "Summits and policy events attended", items(
    ("Feb 2026", "World Sustainable Development Summit 2026, Silver Jubilee edition (delegate)", "Taj Palace, New Delhi, 25–27 February 2026. Transformations: Vision, Voices, and Values for Sustainable Development and Climate Action."),
    ("Feb 2026", "Delhi Climate Innovation Week, Ambition to Action: Climathon", "Climate Career &amp; Sustainability Expo, Innovate X Delhi, 21 February 2026."),
    ("Oct 2025", "Act4Earth Dialogue: Strengthening Multilateralism on the Road to COP30 and Beyond", "Virtual, 17 October 2025."),
    ("Sep 2025", "Science Summit 2025, session on Marine Resources for Sustainable Development", "16 September 2025."),
    ("Mar 2025", "World Sustainable Development Summit 2025", "New Delhi, 5–7 March 2025. Partnerships for Accelerating Sustainable Development and Climate Solutions."),
))

sec("training", "Workshops, training and schools", items(
    ("Mar 2026", "National Workshop on Geospatial Technology for Climate Action, Sustainability and Disaster Risk Reduction", "TERI SAS with NRSC, ISRO, 16–20 March 2026. Participant and volunteer."),
    ("Feb 2026", "Water as a Commons workshop, Water Governance Working Group", "With the Ostrom Workshop, Indiana University Bloomington and IU India Gateway, 26–27 February 2026; included a Yamuna River field visit with INTACH Delhi."),
    ("Aug 2025", "QGreenland Educator Workshop", "Virtual, 5–7 August 2025."),
    ("Dec 2024", "Capacity Building Workshop on UAV/Drone Applications in Agriculture and Natural Resource Management", "TERI SAS with IIT BHU, IIT Roorkee, Namami Gange, Hokkaido University, GLP Earth, GLP Japan, Abhipsa Foundation and Kambil, 10–12 December 2024."),
    ("Nov–Dec 2024", "21-day Winter School in Geospatial Science and Technology", "Amity University Noida, supported by the National Geospatial Programme, DST, Government of India, 18 November–7 December 2024."),
    ("Mar 2024", "Harnessing Geospatial Technology for Forest Fire Disaster Management", "One-week capacity building programme, Amity University Noida, 11–15 March 2024."),
    ("", "Climate Skills: Seeds for Transition", "TERI SAS and TERI with British Council and HSBC."),
))

sec("lectures", "Expert lectures and seminars attended", items(
    ("Feb 2026", "Soil Carbon Sequestration as a Climate Mitigation Mechanism", "Guest lecture by Ms. Violeta Martinkė, InSoil, 13 February 2026."),
    ("Oct 2025", "DHI Urban Water Solutions", "Expert talk by Mr. Morten Just Kjølby, DHI Denmark, TERI SAS, 7 October 2025."),
    ("Jul 2025", "Roots to Resilience Seminar", "TERI SAS with UNEP, UNESCO and Akashvani, 25 July 2025."),
    ("Oct 2024", "Groundwater and sustainable development", "Lecture by Prof. John A. Cherry, Lee Kuan Yew Water Prize recipient, 24 October 2024."),
))

sec("skills", "Skills", """<div class="skills">
<div><h3>GIS and remote sensing</h3><ul><li>Google Earth Engine (JavaScript)</li><li>ArcGIS / ArcGIS Pro, QGIS</li><li>ERDAS Imagine, Google Earth</li><li>Image enhancement and feature extraction</li><li>Orthorectification and mosaicking</li><li>DEM processing</li></ul></div>
<div><h3>Programming and machine learning</h3><ul><li>Python, pandas</li><li>Machine learning, deep learning, AutoML (AutoGluon)</li><li>LightGBM, Random Forest</li><li>Explainable AI: SHAP, LIME</li></ul></div>
<div><h3>Spatial and statistical analysis</h3><ul><li>Spatial data analysis and visualisation</li><li>Time-series modelling and trend analysis</li><li>Mann–Kendall test, Theil–Sen slope</li><li>Moran's I, semivariograms</li></ul></div>
<div><h3>Data management and QA/QC</h3><ul><li>Provenance and data lineage</li><li>Duplicate and sentinel-value handling</li><li>Coordinate validation and geometry reconstruction</li><li>Resolution harmonisation, independent validation</li></ul></div>
<div><h3>Earth observation data</h3><ul><li>Landsat 8/9, Sentinel, MODIS, VIIRS, FIRMS</li><li>CHIRPS, IMD, ERA5-Land, TerraClimate</li><li>GLDAS, GRACE, SRTM, MERIT Hydro</li><li>JRC Global Surface Water, OpenLandMap, GPW, GHSL, GHM, LCZ</li><li>CGWB hydrochemical observations</li></ul></div>
<div><h3>Professional</h3><ul><li>Academic writing and conference presentations</li><li>Scientific communication and reporting</li><li>Rapporteurship and policy-session documentation</li><li>Editorial and content development</li><li>Field and survey-based research</li></ul></div>
</div>""")

sec("volunteering", "Volunteering and co-curricular", items(
    ("2016 to present", "Volunteer, SWAPO NGO"),
    ("2019–2021", "National Service Scheme (NSS)"),
    ("2018–2019", "Coordination of Volunteers, Vasundhara"),
    ("2018–2023", "Personal blogging and content writing"),
))

sec("interests", "Interests", """<ul class="chips"><li>Collecting old coins and stamps</li><li>Reading historic stories and accounts</li><li>Photography and videography</li><li>Travelling</li><li>Badminton</li><li>Dance</li></ul>""")

sec("contact", "Contact", f"""
<p>Department of Natural &amp; Applied Sciences, TERI School of Advanced Studies, Vasant Kunj Institutional Area, New Delhi 110070, India</p>
<div class="links"><a href="{L['email']}">kavya.agrawal@terisas.ac.in</a><a href="{L['linkedin']}">LinkedIn</a><a href="{L['scholar']}">Google Scholar</a><a href="{L['orcid']}">ORCID</a><a href="{L['researchgate']}">ResearchGate</a><a href="{L['github']}">GitHub</a></div>""")

toc = "".join(f'<li><a href="#{i}">{t}</a></li>' for i, t, _ in SECTIONS)
body = "\n".join(h for _, _, h in SECTIONS)

html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Kavya Agrawal, CV</title>
<meta name="description" content="Curriculum vitae of Kavya Agrawal, PhD scholar at TERI School of Advanced Studies, New Delhi.">
<link rel="icon" href="assets/img/favicon-32.png" sizes="32x32">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,600;12..96,700&family=Literata:ital,opsz,wght@0,7..72,400;0,7..72,500;1,7..72,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/plain.css">
</head>
<body>
<a class="skip" href="#about">Skip to content</a>
<div class="layout">
  <nav class="toc" aria-label="CV sections">
    <a class="who" href="#top">Kavya Agrawal</a>
    <ol>{toc}</ol>
  </nav>
  <main id="top">
    <header class="head">
      <img src="assets/img/kavya-portrait-hero.jpg" alt="Portrait of Kavya Agrawal">
      <div>
        <h1>Kavya Agrawal</h1>
        <p class="role">PhD Scholar, Natural &amp; Applied Sciences</p>
        <p>TERI School of Advanced Studies, New Delhi. Groundwater contamination, remote sensing, GIS and machine learning.</p>
        <div class="links"><a href="{L['email']}">kavya.agrawal@terisas.ac.in</a><a href="{L['scholar']}">Google Scholar</a><a href="{L['orcid']}">ORCID</a><a href="{L['researchgate']}">ResearchGate</a><a href="{L['linkedin']}">LinkedIn</a></div>
        <div class="actions"><button class="btn" type="button" onclick="window.print()">Print or save as PDF</button></div>
      </div>
    </header>
{body}
  </main>
</div>
<a class="journey-btn" href="index.html"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.5c0 0-6.5 8-6.5 12.2a6.5 6.5 0 0 0 13 0C18.5 10.5 12 2.5 12 2.5z" fill="#fff"/></svg>Back to the journey</a>
<script>
(function(){{var links=[].slice.call(document.querySelectorAll('.toc ol a'));
var secs=links.map(function(a){{return document.querySelector(a.getAttribute('href'));}});
function on(){{var cur=0;secs.forEach(function(s,i){{if(s.getBoundingClientRect().top<120)cur=i;}});
links.forEach(function(a,i){{a.classList.toggle('on',i===cur);}});
if(last!==cur){{last=cur;var ol=links[cur].closest('ol');if(ol.scrollWidth>ol.clientWidth)ol.scrollLeft=links[cur].parentNode.offsetLeft-16;}}}}var last=-1;
addEventListener('scroll',on,{{passive:true}});on();}})();
</script>
</body>
</html>
"""
(OUT / "cv.html").write_text(html, encoding="utf-8")
print("plain built", len(SECTIONS), "sections")
