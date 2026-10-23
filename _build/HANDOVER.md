# Kavya Agrawal CV website: handover

Live site: https://kavyaagrawal-02.github.io
Repo: github.com/kavyaagrawal-02/kavyaagrawal-02.github.io (branch `main`, GitHub Pages from root, `.nojekyll`)
Last deploy: commit 3ba5b54, 23 October 2026

## 1. What the site is
An elegant, simple, sober academic site with five pages and a downloadable PDF CV:
- **Home** (`index.html`): teal banner with closed contour rings, name, role, buttons (Explore research, Download CV, Email), uncropped portrait; an at-a-glance strip; About; Highlights (photo cards); Research streams (tabs); Writing (2 LinkedIn articles); Recent engagement timeline; What I do; Research interests (chips); Where I would like to go next; Let's connect; a "Beyond research" band (hobbies and stories).
- **Research**: doctoral research, current work (uranium, fluoride, downscaling, arsenic with element badges), earlier cryosphere work, future research directions, projects.
- **Publications**: journal articles, manuscripts, conference presentations. The NEXUS and As2024 photo galleries are shown directly.
- **Teaching**: courses and an expanded "In the lab" section for NRG169 and NRG176.
- **CV** (`cv.html` + `Kavya_Agrawal_CV.pdf`, 9 pages, A4): the complete record from the information inventory, including every skill, parameter, data source, QA/QC item, the subjects studied, coursework with credits, future interests and research keywords.

## 2. Design decisions (locked)
- Font: Newsreader (self-hosted WOFF in `assets/fonts`).
- Colours: deep lagoon teal `#0F3B47` banner, blue `#1D6A80` / `#4A90A8` for links and lines, and a **rose accent `#A9566F`** (picked to go with the pink in her shirt) for kickers, glance numbers, timeline dots, the active nav item and small labels. Pale blue and sage section bands. Dark mode is supported.
- Header: social icon buttons on the left, navigation on the right, no name in the header.
- Headings sit above the text, with a soft highlighter mark.
- Photos are never cropped: they use natural aspect or `object-fit: contain`. The portrait has soft rounded edges.
- No "observe chain"; no orange.
- Banner role reads: "PhD Scholar, Department of Natural & Applied Sciences / TERI School of Advanced Studies, New Delhi".
- Photo and certificate galleries are shown directly, not behind a "show more" button.

## 3. Content rules (must keep)
- **No phone number** anywhere, including the PDF.
- **Unpublished numbers stay hidden** until publication: no uranium exposure figures, model scores, dataset counts or fluoride counts.
- Uranium paper status: **"Submitted to journal"**.
- **One supervisor only: Prof. Chander Kumar Singh**, linked to https://www.linkedin.com/in/chander-kumar-singh-01542227/. Adwitiya Sinha is NOT a co-supervisor.
- Public contacts: kavya.agrawal@terisas.ac.in, kavyateriuniversity@gmail.com, LinkedIn, Google Scholar, ORCID 0009-0009-1032-2541, ResearchGate, GitHub.
- IWWA 2023 paper is included.
- Do not use marksheets, the ID card or the registration number.
- No "(with Shweta Gautam)" anywhere.
- Prof. John A. Cherry is described as the 2020 Stockholm Water Prize laureate (verified). He is mentioned in the CV only, not in Highlights.
- The aztrix-codes/kavya site was made by someone else. Borrow components only. Its errors must not be carried over: WSDS dated 2025 instead of 2026, teaching dated 2024, an old Gmail address, a "16,756" count and unpublished numbers.

## 4. Highlights (current cards)
1. EHP NEXUS 2026: First Position and Best Paper Award. Wide card with the talk and stage photos, uncropped.
2. LST paper, Journal of Mountain Science 2023: shows the seasonal LST trends figure (`assets/img/lst-trends.png`).
3. As2024 poster, KIIT Bhubaneswar (Oct 2024): photo at the standee (added 23 Oct 2026).
4. WSDS 2026 Delegate: **photo slot is waiting**.
5. Water as a Commons with the Ostrom Workshop (Yamuna field visit): **photo slot is waiting**.
6. WSDS 2025 Rapporteur: **photo slot is waiting** (use the pictures from her LinkedIn post).
7. QGreenland Educator Workshop: **photo slot is waiting**.
8. Teaching MSc Geoinformatics (normal-width text tile; 8 cards fill the 3-column grid with NEXUS wide).

Removed at her request: the Cherry/Stockholm card, the Map Making card, the State Child Scientist card and the NRSC-ISRO card. These items remain in the CV.

## 5. Pictures still to add (attach these in the new chat)
| Slot | Where it shows | What to attach |
|---|---|---|
| WSDS 2026 delegate | Highlight 3 | Photo(s) from WSDS 2026, Taj Palace |
| Ostrom / Water as a Commons | Highlight 4 | Yamuna field-visit photos |
| WSDS 2025 rapporteur | Highlight 5 | Same pictures as her LinkedIn post (activity 7307294640695586816) |
| QGreenland | Highlight 6 | A screenshot or certificate |
| NDC 3.0 article | Writing card 1 | The picture used in that LinkedIn article |
| Plenary article | Writing card 2 | The picture used in that LinkedIn article |
| LST paper (optional swap) | Highlight 2 | The figure the journal highlighted, if different from the trends plot |
| Other events (optional) | Publications/CV galleries | Certificates and photos for any talk or workshop |
| Cherry visit photo | Not placed yet | She sent a HEIC that cannot be converted here; needs a JPG/screenshot if she wants it. A drone (DJI Matrice + Zenmuse L1) photo was also sent; she said to leave both for now. |

Done on 23 Oct 2026: certificates are shown directly under their CV/Publications entries (helpers `gal()` and `cert()` in build.py; files `assets/img/cert-*.jpg`, `as2024-*.jpg`). Corrections taken from the certificates: UAV workshop title says "in Environment and Natural Resources Management"; forest fire programme was under ISRO DMS-CB, sponsored by IIRS; NGP-DST Winter School (Level 1), Grade A; Vani English Editor 2019–20; WSDS 2025 volunteer; NRSC 2026 workshop with RRSC-North. The map award is **2nd Position, GeoPitch, World GIS Day, Amity, 23 Nov 2024** (this replaces "Map Making 2025"; she confirmed they are the same award). New items: National Science Day 2025, WRSC 2023 (IIT Bombay CSRE + IEEE GRSS), NIDM online training Feb 2022. The As2024 poster photo is shown; she approved it even though it has model numbers.

Images cannot be downloaded from Google Drive or LinkedIn inside the sandbox, so they must be **attached in chat**. To fill a slot, in `_build/build.py` replace `art=slot("…","…")` with `pic=("assets/img/<file>.jpg", "<alt text>")`, or with a list of tuples for several photos. For writing cards, replace the `<div class="pic art">…</div>` with `<div class="pic"><img src="…" alt="…"></div>`.

## 6. How to build and deploy
Source of truth: `_build/build.py` (all content and page templates) and `assets/site.css`. Both are in the repo.
1. Edit `_build/build.py` and/or `assets/site.css`.
2. Run `python3 _build/build.py`. This writes the 5 HTML pages to the root.
3. Regenerate the PDF from `cv.html` with Playwright/Chromium `page.pdf` (A4, margins 16/16/18 mm, footer "Kavya Agrawal, CV n/N", print CSS already in site.css). Use `/opt/npm-tools/node_modules/playwright`, because npm install is blocked by the proxy. The Newsreader font must be installed in `~/.fonts` for the PDF.
4. Commit and push to `main`. Pages updates in about 2–5 minutes. Verify with a cache-busting query.
5. Redirect stubs are kept: `projects.html` → research, `experience.html` → cv, `new/` → root. `previous/` holds an older comparison copy.

## 7. Open questions for Kavya
- **Editor-in-Chief**: LinkedIn says the departmental magazine *Landscape* (Jul 2019 – May 2021), but the CV says Geography Association (2018–2021). The site currently follows the CV.
- **Class XII result**: LinkedIn says 93.4%, but the CV says CGPA 9.80. The site follows the CV.
- **SWAPO dates**: the inventory says 2016–2023, but the CV says 2016–present. The site follows the CV ("present").
- **Start dates** for the permafrost and snow papers are unverified. The site shows 2023 with "Paper in progress".
- Should the `/previous/` comparison copy be deleted now?
- Is a Debate and MUN icon wanted in "Beyond research"? It is currently shown.

## 8. Her working preferences
- Ask or confirm key choices before big multi-step work, and offer a 2–3 line plan first.
- Give concise answers, one step at a time.
- She is new to GitHub, so explain any steps she needs to do herself.

## 9. Refresh of 23 October 2026 (second round)
- Header: real brand logos (Simple Icons / Font Awesome paths in `_build/brand_icons.json`) in brand colours; a "KA" monogram in contour rings comes first, linking home. Favicons (`favicon-32/48.png`, `apple-touch-icon.png`) are rendered from the same monogram.
- Rose accent is now `#B4527A` (a little pinker). More colour: tinted chips, alternating timeline dots, coloured card tops. Blue contours and the blue header are unchanged (she loves them).
- Highlights: 2 featured cards (NEXUS, As2024) with photo sliders, then 6 equal cards (LST, WSDS 2025, QGreenland, WSDS 2026, Ostrom, Teaching). Every card has a logo strip on top; logos are cropped from her certificates (`assets/img/logos/`), and the IU trident comes from Indiana University's rivet-source repo.
- "On LinkedIn" section embeds the NEXUS and WSDS 2025 posts by iframe (`linkedin.com/embed/feed/update/urn:li:activity:…`). If an embed stays blank, use LinkedIn's "Embed this post" code (urn:li:share or ugcPost) instead.
- Certificates: one per event, the cleanest version only. Photographed ones are perspective-corrected (helper `scan.py` logic: OpenCV quad detection or hand-picked corners). NRSC: volunteer certificate under Rapporteur, participation certificate under Training.
- "What I do" is renamed "Recently". Future directions: history and archaeology from space (leading block), cryosphere of HMA and the poles (permafrost, glaciers/ice, snow), climate change, groundwater policy in India.
- Pending: pictures from the two LinkedIn articles (they cannot be fetched; she would need to attach them).
