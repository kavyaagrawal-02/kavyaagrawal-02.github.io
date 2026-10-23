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


def sectionize(html):
    import re
    def rep(m):
        attrs, h2, rest = m.group(1), m.group(2), m.group(3)
        return f'<section{attrs} data-sec><div class="sec-label"><h2>{h2}</h2></div><div class="sec-body">{rest}</div></section>'
    return re.sub(r'<section((?:(?!class="(?:hero|beyond)")[^>])*)><h2>(.*?)</h2>(.*?)</section>', rep, html, flags=re.S)


SOCIAL = [("mailto:" + L["teri"], "Email", '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3.5" y="6" width="17" height="12" rx="2"/><path d="M4 7l8 6 8-6"/></svg>'),
          (L["linkedin"], "LinkedIn", '<span>in</span>'),
          (L["scholar"], "Google Scholar", '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M2.5 9.5L12 5l9.5 4.5L12 14z"/><path d="M6.5 11.5v4c1.5 1.6 3.4 2.4 5.5 2.4s4-.8 5.5-2.4v-4"/></svg>'),
          (L["orcid"], "ORCID", '<span>iD</span>'),
          (L["researchgate"], "ResearchGate", '<span>RG</span>'),
          (L["github"], "GitHub", '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 8l-4 4 4 4M16 8l4 4-4 4M13.5 6l-3 12"/></svg>')]
RINGS = """<svg class="rings" viewBox="0 0 1600 820" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><path d="M1295,250 L1295,252 L1295,255 L1294,257 L1293,260 L1291,261 L1289,263 L1286,265 L1284,266 L1281,267 L1279,268 L1277,270 L1275,271 L1273,272 L1271,273 L1268,275 L1266,275 L1263,276 L1260,276 L1257,276 L1254,276 L1251,276 L1249,275 L1246,274 L1243,273 L1241,272 L1238,271 L1236,269 L1234,268 L1232,266 L1230,264 L1229,261 L1229,259 L1229,257 L1229,254 L1229,252 L1230,250 L1231,248 L1231,246 L1231,244 L1232,242 L1232,240 L1232,237 L1233,235 L1234,233 L1235,230 L1237,228 L1240,227 L1243,226 L1245,225 L1248,225 L1251,224 L1254,224 L1257,224 L1260,224 L1263,225 L1266,225 L1268,225 L1271,226 L1274,227 L1276,228 L1278,229 L1280,231 L1282,232 L1284,234 L1285,236 L1287,238 L1288,239 L1290,241 L1291,243 L1293,245 L1294,248 L1295,250 Z"/><path d="M1330,250 L1331,255 L1330,260 L1328,265 L1325,269 L1321,273 L1316,276 L1311,279 L1307,281 L1302,284 L1298,286 L1294,289 L1290,292 L1286,294 L1281,297 L1277,300 L1271,302 L1266,303 L1260,304 L1254,304 L1248,303 L1243,302 L1237,300 L1232,298 L1227,296 L1222,294 L1217,291 L1213,288 L1208,285 L1205,281 L1202,277 L1200,272 L1199,268 L1198,263 L1199,259 L1199,254 L1200,250 L1201,246 L1202,242 L1202,238 L1202,233 L1203,229 L1204,224 L1205,219 L1207,214 L1210,210 L1214,207 L1219,204 L1225,201 L1231,200 L1237,199 L1243,199 L1249,199 L1254,200 L1260,200 L1265,200 L1271,201 L1276,201 L1282,202 L1287,204 L1292,206 L1296,208 L1301,211 L1304,214 L1308,218 L1311,221 L1314,225 L1318,229 L1321,232 L1324,236 L1327,241 L1329,245 L1330,250 Z"/><path d="M1365,250 L1365,257 L1364,265 L1360,271 L1355,278 L1349,283 L1343,288 L1336,292 L1329,296 L1323,300 L1317,304 L1311,308 L1305,312 L1299,317 L1293,322 L1285,326 L1277,329 L1269,331 L1260,332 L1251,332 L1242,331 L1234,328 L1226,326 L1218,322 L1210,319 L1203,315 L1196,311 L1190,306 L1184,301 L1179,296 L1174,290 L1171,283 L1169,276 L1168,270 L1168,263 L1169,256 L1170,250 L1171,244 L1172,238 L1172,231 L1172,224 L1173,217 L1174,210 L1176,203 L1180,196 L1185,190 L1191,184 L1199,180 L1208,177 L1217,176 L1226,175 L1235,175 L1244,175 L1252,176 L1260,176 L1268,177 L1276,177 L1284,178 L1292,179 L1300,181 L1308,184 L1315,187 L1322,191 L1328,196 L1333,201 L1338,206 L1343,212 L1348,217 L1352,223 L1357,229 L1361,236 L1363,243 L1365,250 Z"/><path class="idx" d="M1399,250 L1399,260 L1396,269 L1392,278 L1385,286 L1377,294 L1368,300 L1360,306 L1351,311 L1343,316 L1335,322 L1328,328 L1321,334 L1313,341 L1304,347 L1294,352 L1284,357 L1272,360 L1260,361 L1248,361 L1236,359 L1225,355 L1214,351 L1204,346 L1194,341 L1185,335 L1176,330 L1168,324 L1160,317 L1153,310 L1147,302 L1143,294 L1140,285 L1138,276 L1138,267 L1138,259 L1139,250 L1140,242 L1140,233 L1140,224 L1141,215 L1141,206 L1143,196 L1147,186 L1152,177 L1159,169 L1168,162 L1179,157 L1191,154 L1203,152 L1215,151 L1227,152 L1238,152 L1249,153 L1260,153 L1271,153 L1281,154 L1292,154 L1303,155 L1314,158 L1324,161 L1334,165 L1344,170 L1352,177 L1359,183 L1366,191 L1373,198 L1379,206 L1384,214 L1390,222 L1394,231 L1397,240 L1399,250 Z"/><path d="M1432,250 L1431,262 L1428,274 L1422,285 L1414,295 L1404,304 L1394,312 L1383,319 L1373,326 L1364,333 L1355,340 L1346,348 L1337,356 L1327,365 L1316,373 L1304,380 L1290,386 L1275,389 L1260,391 L1245,389 L1230,386 L1216,381 L1203,376 L1191,369 L1179,362 L1168,355 L1157,348 L1147,340 L1137,332 L1129,324 L1121,314 L1115,304 L1111,293 L1108,283 L1107,272 L1107,261 L1107,250 L1107,239 L1107,228 L1108,217 L1108,206 L1109,194 L1112,182 L1117,170 L1124,159 L1134,149 L1146,141 L1159,135 L1174,131 L1190,129 L1205,129 L1220,129 L1234,130 L1247,130 L1260,131 L1273,130 L1286,130 L1300,130 L1314,131 L1328,133 L1342,137 L1354,142 L1366,149 L1377,157 L1386,165 L1395,174 L1402,184 L1410,194 L1416,205 L1422,215 L1427,226 L1430,238 L1432,250 Z"/><path d="M1463,250 L1462,264 L1458,278 L1451,291 L1441,303 L1431,314 L1419,323 L1407,332 L1396,341 L1385,350 L1375,359 L1364,369 L1354,380 L1342,390 L1328,400 L1313,409 L1296,415 L1279,419 L1260,420 L1242,418 L1224,413 L1207,407 L1192,399 L1178,391 L1164,382 L1152,374 L1139,365 L1127,357 L1115,347 L1104,337 L1095,326 L1087,315 L1081,302 L1077,289 L1074,276 L1073,263 L1073,250 L1073,237 L1073,224 L1074,210 L1075,196 L1077,182 L1081,167 L1088,154 L1097,141 L1109,129 L1124,120 L1141,114 L1159,110 L1177,108 L1195,107 L1212,108 L1229,108 L1245,108 L1260,108 L1276,107 L1292,106 L1308,106 L1325,106 L1343,108 L1359,112 L1375,118 L1390,126 L1403,136 L1414,147 L1424,158 L1432,170 L1440,183 L1447,195 L1453,209 L1459,222 L1462,236 L1463,250 Z"/><path d="M1493,250 L1491,266 L1487,282 L1479,297 L1469,311 L1458,324 L1445,335 L1432,346 L1419,357 L1407,368 L1396,379 L1384,392 L1371,404 L1357,417 L1341,428 L1323,438 L1303,445 L1282,449 L1260,449 L1239,446 L1218,440 L1199,431 L1182,422 L1166,412 L1151,402 L1136,392 L1121,382 L1107,372 L1093,362 L1080,351 L1068,339 L1058,325 L1050,311 L1044,296 L1040,281 L1039,265 L1038,250 L1038,234 L1039,219 L1040,203 L1042,186 L1045,170 L1051,153 L1059,138 L1071,123 L1086,111 L1103,101 L1123,94 L1144,89 L1165,87 L1186,86 L1205,87 L1224,87 L1242,86 L1260,85 L1278,83 L1297,81 L1317,80 L1337,80 L1358,82 L1378,86 L1397,94 L1414,103 L1429,115 L1442,128 L1452,142 L1462,157 L1470,172 L1477,187 L1484,202 L1489,218 L1492,234 L1493,250 Z"/><path class="idx" d="M1522,250 L1520,268 L1515,286 L1508,303 L1497,319 L1485,334 L1472,348 L1458,361 L1444,374 L1431,387 L1418,401 L1404,415 L1390,430 L1373,444 L1354,457 L1333,467 L1309,475 L1285,478 L1260,477 L1236,472 L1213,465 L1191,455 L1172,443 L1154,432 L1137,420 L1121,409 L1104,399 L1087,388 L1071,377 L1055,365 L1040,352 L1027,337 L1017,321 L1010,304 L1005,286 L1002,268 L1002,250 L1002,232 L1003,214 L1005,195 L1009,177 L1014,158 L1021,140 L1032,122 L1046,106 L1063,93 L1084,82 L1106,74 L1130,69 L1153,67 L1176,66 L1198,65 L1219,65 L1240,63 L1260,61 L1281,58 L1303,55 L1326,53 L1350,52 L1374,55 L1397,60 L1419,69 L1438,80 L1455,94 L1469,110 L1481,126 L1490,144 L1498,161 L1506,178 L1512,196 L1517,214 L1520,232 L1522,250 Z"/><path d="M291,600 L291,602 L291,604 L290,606 L289,608 L288,610 L286,612 L284,613 L282,615 L280,616 L278,617 L276,618 L274,619 L272,620 L270,622 L268,623 L265,624 L263,625 L260,626 L257,626 L254,626 L252,625 L249,624 L247,623 L245,621 L243,620 L241,618 L240,616 L238,615 L236,613 L235,612 L234,610 L232,608 L232,606 L231,604 L231,602 L231,600 L231,598 L232,596 L232,594 L233,592 L233,590 L234,588 L235,586 L236,584 L237,582 L239,580 L241,579 L244,577 L246,577 L249,577 L252,577 L255,577 L258,577 L260,578 L262,578 L265,579 L267,579 L270,579 L272,579 L275,580 L277,580 L280,581 L282,582 L284,584 L286,586 L287,588 L288,590 L289,592 L290,594 L290,596 L291,598 L291,600 Z"/><path d="M321,600 L321,604 L320,608 L319,613 L317,617 L314,620 L311,624 L307,626 L303,629 L299,631 L295,634 L292,636 L288,639 L284,641 L280,644 L276,647 L271,649 L266,651 L260,652 L254,652 L249,652 L243,650 L238,648 L234,645 L230,642 L226,639 L223,635 L220,632 L217,629 L214,626 L211,623 L208,620 L205,616 L203,612 L202,608 L201,604 L201,600 L201,596 L202,592 L203,588 L204,584 L205,580 L207,576 L209,571 L211,567 L215,564 L218,560 L223,558 L228,555 L233,554 L239,554 L245,554 L250,555 L255,555 L260,556 L265,557 L269,557 L274,558 L279,558 L284,558 L290,559 L295,560 L300,562 L305,564 L309,567 L312,571 L314,575 L316,579 L318,583 L319,587 L320,592 L321,596 L321,600 Z"/><path d="M350,600 L350,606 L349,613 L347,619 L344,625 L340,630 L336,635 L331,640 L325,644 L319,648 L314,651 L308,655 L303,659 L297,663 L291,667 L284,671 L276,675 L268,677 L260,679 L251,679 L243,678 L235,675 L228,671 L221,667 L215,662 L210,657 L205,652 L201,647 L196,643 L191,639 L186,634 L182,629 L178,624 L174,618 L172,612 L170,606 L170,600 L170,594 L171,588 L173,581 L175,575 L177,569 L180,563 L183,557 L187,551 L192,546 L198,541 L205,537 L213,534 L221,533 L229,532 L237,532 L245,533 L253,534 L260,535 L267,535 L274,536 L282,536 L289,536 L297,536 L305,537 L313,539 L321,542 L328,546 L334,550 L339,556 L342,562 L345,568 L347,575 L348,581 L349,587 L350,594 L350,600 Z"/><path class="idx" d="M378,600 L377,608 L376,616 L374,624 L371,632 L367,640 L361,647 L355,653 L348,659 L340,664 L333,669 L325,675 L318,680 L310,686 L301,691 L292,696 L282,701 L271,704 L260,705 L249,705 L237,703 L227,699 L217,694 L209,687 L202,681 L195,674 L188,668 L182,662 L176,657 L169,651 L162,645 L155,639 L149,632 L144,625 L140,617 L138,609 L138,600 L138,591 L140,583 L142,575 L146,567 L149,559 L153,551 L158,543 L164,535 L171,528 L179,522 L188,517 L198,514 L208,512 L219,511 L230,511 L241,512 L250,512 L260,513 L269,514 L279,514 L289,513 L300,513 L310,513 L322,515 L333,517 L343,521 L352,527 L359,533 L365,541 L370,549 L373,558 L375,567 L376,575 L377,584 L377,592 L378,600 Z"/><path d="M404,600 L404,610 L403,620 L401,630 L398,640 L393,650 L387,659 L379,667 L371,674 L362,682 L353,688 L343,695 L334,702 L323,709 L313,715 L301,721 L288,726 L274,730 L260,731 L246,730 L232,727 L219,722 L208,715 L197,707 L188,699 L180,691 L172,684 L164,677 L155,670 L146,664 L137,657 L128,649 L120,641 L113,632 L108,621 L105,611 L104,600 L105,589 L108,579 L112,568 L116,558 L121,548 L127,539 L134,529 L141,520 L150,512 L160,505 L171,499 L184,494 L197,491 L210,490 L223,490 L236,490 L248,491 L260,491 L272,491 L284,491 L297,490 L310,489 L324,490 L338,491 L352,495 L365,500 L376,507 L385,516 L392,526 L397,537 L400,548 L402,559 L403,569 L403,580 L404,590 L404,600 Z"/><path d="M430,600 L431,612 L430,624 L429,636 L426,648 L421,660 L414,671 L405,681 L395,691 L385,700 L373,708 L362,716 L350,724 L337,732 L324,740 L309,746 L293,752 L277,755 L260,756 L243,754 L227,750 L212,744 L198,736 L186,727 L175,717 L165,708 L155,700 L145,692 L134,684 L123,677 L111,669 L99,660 L89,650 L81,638 L74,626 L71,613 L70,600 L72,587 L76,574 L81,562 L87,550 L94,538 L102,527 L110,516 L119,506 L130,496 L142,487 L155,480 L170,475 L185,471 L200,469 L216,468 L231,468 L246,468 L260,468 L274,467 L289,467 L305,466 L321,465 L338,466 L355,468 L372,472 L387,479 L400,488 L410,499 L418,512 L423,525 L426,538 L427,551 L428,564 L429,576 L430,588 L430,600 Z"/><path d="M456,600 L457,614 L458,628 L457,642 L454,657 L449,671 L442,684 L432,696 L421,708 L408,718 L395,728 L381,738 L366,747 L351,756 L334,764 L317,771 L299,776 L280,779 L260,780 L241,778 L222,772 L205,765 L189,755 L175,745 L163,735 L151,725 L138,716 L126,707 L112,699 L98,691 L84,681 L70,671 L57,659 L47,646 L40,631 L36,616 L36,600 L39,585 L44,570 L51,555 L60,542 L68,529 L78,516 L88,504 L99,492 L111,481 L125,471 L140,462 L156,456 L173,451 L191,448 L208,446 L226,445 L243,445 L260,444 L277,443 L295,441 L314,440 L333,440 L353,441 L373,444 L391,450 L408,458 L423,470 L434,483 L442,498 L447,513 L450,529 L452,544 L453,559 L454,573 L455,586 L456,600 Z"/><path d="M1465,650 L1465,652 L1464,653 L1464,655 L1464,657 L1464,659 L1463,661 L1463,663 L1462,665 L1461,667 L1459,668 L1457,669 L1455,670 L1452,671 L1450,671 L1447,672 L1445,672 L1442,672 L1440,672 L1438,672 L1435,672 L1433,671 L1431,671 L1428,670 L1426,669 L1425,668 L1423,666 L1422,665 L1420,663 L1419,662 L1418,660 L1416,659 L1415,657 L1413,656 L1412,654 L1411,652 L1410,650 L1410,648 L1410,646 L1411,644 L1412,642 L1414,640 L1416,639 L1418,638 L1420,636 L1422,635 L1424,634 L1425,633 L1427,632 L1429,631 L1431,630 L1433,629 L1435,629 L1438,628 L1440,628 L1442,628 L1445,628 L1447,629 L1449,629 L1452,630 L1454,631 L1456,631 L1458,632 L1460,634 L1462,635 L1464,637 L1465,638 L1466,640 L1467,642 L1467,644 L1466,646 L1466,648 L1465,650 Z"/><path d="M1490,650 L1490,653 L1489,657 L1489,660 L1489,664 L1488,668 L1488,672 L1487,676 L1485,680 L1482,684 L1478,687 L1474,689 L1470,691 L1465,692 L1459,693 L1454,693 L1450,693 L1445,693 L1440,693 L1435,693 L1431,692 L1426,692 L1422,691 L1417,689 L1413,687 L1409,685 L1406,683 L1403,680 L1400,677 L1397,674 L1394,671 L1392,668 L1389,665 L1386,662 L1384,658 L1382,654 L1380,650 L1380,646 L1381,642 L1382,638 L1385,634 L1389,631 L1392,628 L1396,626 L1400,623 L1404,621 L1408,619 L1411,617 L1415,615 L1418,612 L1422,610 L1426,608 L1430,607 L1435,605 L1440,605 L1445,605 L1450,606 L1455,607 L1459,608 L1464,609 L1468,611 L1472,613 L1477,615 L1481,618 L1484,620 L1487,623 L1490,627 L1491,631 L1492,635 L1492,639 L1492,643 L1491,646 L1490,650 Z"/><path d="M1515,650 L1515,655 L1514,660 L1514,666 L1514,672 L1514,677 L1513,684 L1511,690 L1508,696 L1504,701 L1498,705 L1491,709 L1484,711 L1477,713 L1469,714 L1461,714 L1454,714 L1447,714 L1440,713 L1433,713 L1426,712 L1419,712 L1413,710 L1406,709 L1400,706 L1394,703 L1388,699 L1383,695 L1379,691 L1375,687 L1370,682 L1366,678 L1362,673 L1358,668 L1355,662 L1352,656 L1350,650 L1350,644 L1352,638 L1355,632 L1359,626 L1364,622 L1370,618 L1376,614 L1381,611 L1387,608 L1392,604 L1397,601 L1402,597 L1407,593 L1412,590 L1419,586 L1425,584 L1433,582 L1440,581 L1447,581 L1455,582 L1462,584 L1469,586 L1476,589 L1482,592 L1488,595 L1494,598 L1500,602 L1505,606 L1510,611 L1513,616 L1516,622 L1517,628 L1518,633 L1517,639 L1516,645 L1515,650 Z"/><path class="idx" d="M1541,650 L1541,657 L1541,664 L1541,672 L1541,679 L1540,687 L1539,696 L1536,704 L1531,711 L1525,718 L1518,724 L1509,728 L1499,731 L1488,733 L1478,734 L1468,734 L1458,733 L1449,733 L1440,733 L1431,733 L1422,732 L1413,732 L1403,730 L1394,728 L1386,725 L1378,721 L1370,717 L1363,711 L1357,706 L1351,700 L1346,694 L1340,687 L1335,681 L1330,674 L1326,666 L1323,658 L1321,650 L1322,642 L1324,634 L1328,626 L1334,619 L1341,613 L1348,608 L1356,603 L1363,598 L1370,594 L1376,589 L1382,584 L1389,579 L1395,573 L1403,568 L1411,564 L1420,560 L1430,558 L1440,557 L1450,557 L1460,559 L1470,562 L1479,565 L1487,569 L1496,573 L1504,577 L1512,582 L1519,587 L1526,593 L1531,599 L1536,606 L1540,613 L1542,620 L1543,628 L1543,636 L1542,643 L1541,650 Z"/><path d="M1568,650 L1568,659 L1568,668 L1568,677 L1568,687 L1567,697 L1565,708 L1561,718 L1555,727 L1547,736 L1537,742 L1525,747 L1513,751 L1500,752 L1487,753 L1474,753 L1463,752 L1451,752 L1440,752 L1429,752 L1417,752 L1406,752 L1394,751 L1383,748 L1371,745 L1361,740 L1351,735 L1342,728 L1335,721 L1327,713 L1320,705 L1314,697 L1308,689 L1302,680 L1298,670 L1294,660 L1293,650 L1294,640 L1297,630 L1302,621 L1310,612 L1318,604 L1327,598 L1336,592 L1344,586 L1352,580 L1360,574 L1367,567 L1375,560 L1383,553 L1393,546 L1403,540 L1415,536 L1427,533 L1440,532 L1453,533 L1465,535 L1477,539 L1488,544 L1499,549 L1509,554 L1519,560 L1528,566 L1537,572 L1545,579 L1552,587 L1559,595 L1563,604 L1566,613 L1568,623 L1568,632 L1568,641 L1568,650 Z"/><path d="M724,95 L723,97 L723,98 L723,100 L722,102 L722,103 L721,105 L720,106 L719,108 L717,109 L716,110 L714,111 L712,112 L710,113 L709,114 L707,115 L704,115 L702,116 L700,116 L698,116 L695,116 L693,116 L691,115 L689,114 L687,112 L686,111 L685,109 L684,108 L683,107 L682,105 L680,104 L679,103 L678,102 L676,100 L675,99 L674,97 L674,95 L674,93 L674,91 L675,90 L675,88 L677,86 L678,85 L679,83 L681,82 L682,81 L684,79 L685,78 L687,77 L689,77 L691,76 L694,76 L696,76 L698,76 L700,76 L702,77 L704,77 L706,77 L708,77 L710,78 L712,78 L715,78 L717,79 L719,80 L721,81 L722,82 L724,84 L724,86 L725,88 L725,90 L724,92 L724,93 L724,95 Z"/><path d="M747,95 L746,98 L746,101 L745,105 L745,108 L744,111 L743,115 L741,118 L738,121 L736,123 L732,126 L729,128 L725,130 L721,131 L717,133 L713,134 L709,136 L705,137 L700,137 L695,138 L691,137 L686,136 L682,134 L678,132 L675,129 L673,126 L670,124 L668,121 L665,118 L663,116 L660,113 L658,111 L655,108 L652,105 L649,102 L648,99 L647,95 L647,91 L647,88 L649,84 L651,81 L653,78 L656,75 L659,72 L662,69 L665,67 L668,64 L671,62 L675,60 L679,59 L683,58 L687,57 L692,57 L696,57 L700,57 L704,58 L708,58 L712,59 L716,59 L721,59 L725,60 L730,61 L734,62 L738,64 L742,67 L745,70 L747,73 L748,77 L749,81 L748,85 L748,88 L747,92 L747,95 Z"/><path d="M769,95 L768,100 L768,105 L768,110 L767,115 L766,120 L765,125 L762,130 L758,134 L754,138 L749,142 L744,145 L738,148 L732,150 L726,152 L720,154 L713,156 L707,157 L700,158 L693,158 L686,157 L680,155 L674,153 L668,149 L663,146 L659,142 L655,137 L652,134 L648,130 L644,126 L640,123 L635,119 L631,115 L627,111 L623,106 L620,101 L619,95 L619,89 L620,84 L623,78 L626,74 L630,69 L635,65 L639,61 L644,57 L648,54 L653,50 L658,47 L663,44 L669,41 L675,40 L681,38 L687,38 L694,38 L700,38 L706,38 L712,39 L719,39 L725,40 L732,41 L738,42 L745,43 L752,46 L758,49 L763,53 L767,57 L770,63 L771,68 L772,74 L771,80 L771,85 L770,90 L769,95 Z"/></svg>"""
SOCIAL_HTML = "".join(f'<a class="soc" href="{h}" aria-label="{n}" title="{n}">{i}</a>' for h, n, i in SOCIAL)


def page(fname, title, desc, body, pre="", post="", mcls=""):
    home = fname == "index.html"
    top_open = '<div class="top">' + RINGS if home else ""
    top_close = "</div>" if home else ""
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
<meta property="og:image" content="https://kavyaagrawal-02.github.io/assets/img/headshot.jpg">
<link rel="icon" href="assets/img/favicon-32.png" sizes="32x32">
<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
<link rel="preload" href="assets/fonts/Newsreader.woff" as="font" type="font/woff" crossorigin>
<link rel="stylesheet" href="assets/site.css">
</head>
<body class="{"home" if home else ""}">
<a class="skip" href="#main">Skip to content</a>
{top_open}<header class="site-head">
  <div class="wrap bar">
    <div class="socials" aria-label="Contact and profiles">{SOCIAL_HTML}</div>
    <nav aria-label="Main"><ul class="nav">{nav}</ul></nav>
  </div>
  {"" if home else '<div class="wrap">' + CONTOUR + '</div>'}
</header>{pre}{top_close}
<main id="main" class="{mcls}"><div class="wrap">
{body}
</div>{post}</main>
<footer class="site-foot"><div class="wrap">
  <span class="coords">28°32′N 77°09′E, TERI School of Advanced Studies, New Delhi</span>
  <span><a href="mailto:{L['teri']}">{L['teri']}</a> &nbsp;·&nbsp; Updated October 2026</span>
</div></footer>
<dialog class="lightbox" id="lightbox"><button type="button" class="lb-close" aria-label="Close">×</button><img alt=""><p></p></dialog>
<script>
(function(){{var d=document.getElementById('lightbox');if(!d||!d.showModal)return;var im=d.querySelector('img'),cap=d.querySelector('p');
document.querySelectorAll('.hl .pic img, .gallery img, .zoomable').forEach(function(i){{i.tabIndex=0;i.setAttribute('role','button');
function open(){{im.src=i.currentSrc||i.src;im.alt=i.alt;cap.textContent=i.alt;d.showModal();}}
i.addEventListener('click',open);i.addEventListener('keydown',function(e){{if(e.key==='Enter'||e.key===' '){{e.preventDefault();open();}}}});}});
d.addEventListener('click',function(e){{if(e.target===d||e.target.classList.contains('lb-close'))d.close();}});}})();
document.querySelectorAll('[data-tabs]').forEach(function(t){{var b=[].slice.call(t.querySelectorAll('[role=tab]'));
function sel(x){{b.forEach(function(o){{var on=o===x;o.setAttribute('aria-selected',on);o.tabIndex=on?0:-1;document.getElementById(o.getAttribute('aria-controls')).hidden=!on;}});}}
b.forEach(function(x,i){{x.addEventListener('click',function(){{sel(x);}});x.addEventListener('keydown',function(e){{var j=e.key==='ArrowRight'?i+1:e.key==='ArrowLeft'?i-1:-9;if(j!==-9){{j=(j+b.length)%b.length;sel(b[j]);b[j].focus();}}}});}});}});
</script>
</body>
</html>
"""
    (ROOT / fname).write_text(html, encoding="utf-8")


def entry(when, title, meta="", text="", methods="", status="", award=False, badge=None, more="", more_label="Photos and certificate"):
    parts = []
    if badge:
        sym, z, col, method = badge
        parts.append(f'<span class="el{" method" if method else ""}" style="--c:{col}" aria-hidden="true">{f"<small>{z}</small>" if z else ""}<b>{sym}</b></span>')
    parts.append(f"<h3>{title}</h3>")
    if meta: parts.append(f'<p class="meta">{meta}</p>')
    if text: parts.append(f'<p class="desc">{text}</p>')
    if methods: parts.append(f'<p class="methods">{methods}</p>')
    if status: parts.append(f'<span class="status{" award" if award else ""}">{status}</span>')
    if more: parts.append(f'<div class="more"><p class="more-label">{more_label}</p>{more}</div>')
    return f'<li class="entry{" has-badge" if badge else ""}"><span class="when">{when}</span><div>{"".join(parts)}</div></li>'


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
def gal(*pics):
    return '<div class="gallery">' + "".join(f'<img src="assets/img/{f}" alt="{a}" loading="lazy">' for f, a in pics) + '</div>'


def cert(f, a):
    return gal((f, a))


AS2024_MORE = gal(("as2024-standee.jpg", "At the As2024 congress, KIIT Deemed to be University, Bhubaneswar"),
                  ("as2024-poster.jpg", "Poster: distribution, speciation and controls on arsenic mobilisation in the Middle Gangetic Plain"),
                  ("as2024-hall.jpg", "Opening session of As2024, Bhubaneswar"),
                  ("as2024-cert-poster.jpg", "Certificate of participation for the poster presentation, As2024"),
                  ("as2024-cert-participation.jpg", "Certificate of participation, As2024")) + '<p class="small muted">Theme: <em>Arsenic and other Pollutants, Water Security and One Health under Global Climate Change Scenario</em>. Organised by KIIT Deemed to be University with ISGSD and KTH Royal Institute of Technology, Sweden.</p>'
NEXUS_MORE = '<div class="gallery"><img src="assets/img/award-talk.jpg" alt="Presenting the uranium risk framework at EHP NEXUS 2026" loading="lazy"><img src="assets/img/award-certificate.jpg" alt="Certificate of Excellence, first position for the oral presentation, EHP NEXUS 2026" loading="lazy"><img src="assets/img/cert-nexus-2026-participation.jpg" alt="Certificate of participation, EHP NEXUS 2026" loading="lazy"><img src="assets/img/award-stage.jpg" alt="Inaugural session of EHP NEXUS 2026, Gautam Buddha University" loading="lazy"></div><p class="small muted">Conference: <em>The Nexus Imperative: Environment, Public Health and Policy for a Sustainable Future</em>, organised by the Department of Environmental Science, SoVSAS, Gautam Buddha University, Greater Noida.</p>'
TALKS = [
    entry("Apr 2026", "A Machine Learning-Based Framework for Uranium Risk Assessment, Population Exposure and Groundwater Governance in Urban India",
          'ICSSR EHP NEXUS 2026, Track X: AI and Predictive Analytics for Society and Environment, Gautam Buddha University, 27–28 April 2026. <a href="https://www.linkedin.com/feed/update/urn:li:activity:7455656612595126273/">LinkedIn post</a>',
          status="First Position, oral presentation, and Best Paper Award", award=True, more=NEXUS_MORE),
    entry("Oct 2024", "Distribution, Speciation and Controls on As Mobilization in the Groundwater in Aquifers of the Middle Gangetic Plain, India",
          "9th International Congress &amp; Exhibition on Arsenic in the Environment (As2024), KIIT Deemed to be University, Bhubaneswar, 20–24 October 2024. Poster.", more=AS2024_MORE),
    entry("Nov 2022", "Problems and Prospects of Delhi's Drinking Water Supply",
          "IGU Thematic Conference on Sustainability, Future Earth and Humanities, Department of Geography, Central University of Haryana, Mahendragarh, 24–25 November 2022."),
    entry("Jul 2022", "Educational Relevance of Ramayana in Modern India",
          "National Seminar on Promoting Human Values and Culture for Peaceful Co-Existence, Amity University Haryana, sponsored by ICPR, 22 July 2022.", more=cert("cert-amity-seminar-2022.jpg", "Certificate of appreciation, National Seminar, Amity University Haryana"), more_label="Certificate"),
    entry("May 2022", "Digital Enhancement of Physical Space and Connective Turn in Tourism Industry during and Post-COVID-19 Period",
          "International Conference on Geography and the Digital: Intersections and Conflations, Department of Geography, Delhi School of Economics, University of Delhi, 23–25 May 2022."),
    entry("May 2022", "Migrant College Students during Covid Pandemic: Evidence from the Field",
          "Jamia International Conference on Education 2022, Faculty of Education, Jamia Millia Islamia, New Delhi, 6–8 May 2022."),
    entry("Apr 2022", "Migrant College Students during Covid Pandemic: Evidence from the Field",
          "International Conference on Challenges to Disaster Risk Reduction and Resilient Habitat, Centre for Disaster Management Studies, Shaheed Bhagat Singh College, University of Delhi, 5–6 April 2022.", more=cert("cert-cdms-conference-2022.jpg", "Certificate of participation, CDMS international conference"), more_label="Certificate"),
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
    entry("2025 – 26", "Uranium in groundwater across India", badge=("U","92","#9DB52A",False),
          text="A national-scale model of where uranium occurs in India's groundwater, built from groundwater observations and environmental predictors and checked against an independent validation dataset. The predictions are turned into spatial risk classes, estimates of population exposure, and governance indicators showing where monitoring and action are most needed.",
          methods="<b>Methods:</b> automated machine learning (AutoGluon), independent validation, spatial risk mapping, exposure assessment.",
          status="Paper submitted to journal; Best Paper Award, ICSSR EHP NEXUS 2026", award=False),
    entry("2026 –", "Fluoride and the effect of spatial resolution", badge=("F","9","#4A9CC9",False),
          text="India-wide prediction of fluoride contamination, benchmarking deep learning models and testing how the resolution of environmental predictors changes the result. Predictor stacks are built in Google Earth Engine at native resolution and at 500 m, 1 km and 5 km, keeping every groundwater observation in the data.",
          methods="<b>Methods:</b> deep learning, multi-resolution predictor extraction, 1.5 mg/L threshold.",
          status="In progress"),
    entry("2026 –", "Downscaling and upscaling environmental predictors", badge=("DS","","#E3A13B",True),
          text="A physically informed framework for moving satellite data between coarse and fine resolutions without inventing detail. A pilot on CHIRPS rainfall over Punjab (2013–2022) targets 5 km, 1 km and 500 m using sub-pixel fractions and conservation-based aggregation.",
          methods="<b>Methods:</b> machine learning, conservation-based aggregation; validated with Moran's I, semivariograms and aggregation consistency.",
          status="In progress"),
    entry("2024 – 25", "Arsenic in the Middle Gangetic Plain", badge=("As","33","#A8557E",False),
          text="The distribution, speciation and controls on arsenic mobilisation in the aquifers of the Middle Gangetic Plain, looking at geogenic and hydrogeochemical factors such as pH, iron, redox potential and sulfate.",
          methods="<b>Methods:</b> hydrogeochemistry, explainable AI (SHAP, LIME).",
          status="Presented at As2024, Bhubaneswar"),
]
EARLIER = [
    entry("2023", "Land surface temperature trends across the Indus River Basin", badge=("LST","","#7E8FC9",True),
          text="Spatial and elevation-wise trends in daytime and nighttime land surface temperature across the Indus River Basin.",
          methods="<b>Methods:</b> Google Earth Engine (JavaScript), ArcGIS, Mann–Kendall and Theil–Sen trend analysis.",
          status="Published, Journal of Mountain Science"),
    entry("2023", "Identification and mapping of permafrost in the Indus Basin",
          text="Mapping likely permafrost from about twenty years of mean annual air temperature (MAAT), potential incoming solar radiation (PISR), BMAT, snow and precipitation estimates in Google Earth Engine.", status="Paper in progress"),
    entry("2023", "Snow cover and changes in Indian basins", text="Changes in snow cover across Indian river basins.", status="Paper in progress"),
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
FUTURE_ITEMS = [
    ("Permafrost", "Identification, modelling and assessment of permafrost."),
    ("Glaciers, ice and snow", "Mapping and calculations of glacier, ice and snow change."),
    ("Climate change", "Assessments of climate change, its impacts and its parameters."),
    ("High Mountain Asia and the poles", "The Himalaya, High Mountain Asia, the Arctic and Antarctica."),
    ("History and archaeology", "Remote sensing assessments and calculations for history and archaeology."),
]
FUTURE = "".join(f'<div><h3>{a}</h3><p>{b}</p></div>' for a, b in FUTURE_ITEMS)
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
MAIL = '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3.5" y="6" width="17" height="12" rx="2"/><path d="M4 7l8 6 8-6"/></svg>'
ICONS = {
    "Old coins": '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="6"/><path d="M10 10.5h4M10 12.5h4M11 10.5c2 0 2 2 0 2l3 3"/>',
    "Stamps": '<path d="M5 3h14v18H5z" stroke-dasharray="2 1.6"/><rect x="8" y="6.5" width="8" height="8"/><path d="M8 17.5h8"/>',
    "Historic stories": '<path d="M3 5c3-1.2 6-1 9 1 3-2 6-2.2 9-1v14c-3-1.2-6-1-9 1-3-2-6-2.2-9-1z"/><path d="M12 6v14"/>',
    "Photography": '<rect x="3" y="7" width="18" height="13" rx="2"/><circle cx="12" cy="13.5" r="3.6"/><path d="M8.5 7l1.4-2.5h4.2L15.5 7"/>',
    "Travel": '<circle cx="12" cy="12" r="9"/><path d="M15.8 8.2l-2.3 5.3-5.3 2.3 2.3-5.3z"/>',
    "Badminton": '<path d="M9.5 14L6.5 3.5h11L14.5 14z"/><path d="M8 9h8M12 3.5V14"/><circle cx="12" cy="17.6" r="3"/>',
    "Dance": '<path d="M3 8.5c6 4.5 12 4.5 18 0"/><circle cx="7" cy="14.5" r="2"/><circle cx="12" cy="16" r="2"/><circle cx="17" cy="14.5" r="2"/>',
    "Debate and MUN": '<path d="M4 5h11v8H9l-4 3v-3H4z"/><path d="M15 9h5v8h-1v3l-4-3h-4v-2"/>',
}
STORIES = [
    ("Since 2016", "Social work with SWAPO", "A volunteer with the SWAPO NGO for ten years, helping manage and organise its activities. Also NSS (2019–2021) and volunteer coordinator at college."),
    ("2018 – 2021", "Editor at heart", "Editor-in-Chief for the Geography Association at the University of Delhi, and coordinator and English editor of <em>Vani</em>, the college magazine. A personal blog from 2018 to 2023."),
    ("School days", "On stage and on court", "Top-3 ranks in the English Olympiads four years running, a State Child Scientist Award, 20 cultural and general-knowledge awards, prizes in dance, MUN, extempore, basketball and badminton."),
]
beyond = ('<svg class="wave" viewBox="0 0 1440 70" preserveAspectRatio="none" aria-hidden="true"><path d="M0 70 V38 C 200 8, 420 8, 640 34 S 1100 66, 1440 26 V70 Z"/></svg>'
          '<section class="beyond" aria-label="Beyond research"><div class="wrap"><h2>Beyond research</h2>'
          '<p class="lead">Collecting, reading, travelling, and a long habit of writing and volunteering.</p><ul class="icons">'
          + "".join(f'<li><svg viewBox="0 0 24 24" aria-hidden="true">{v}</svg>{k}</li>' for k, v in ICONS.items())
          + '</ul><div class="stories">'
          + "".join(f'<div class="story"><span class="kick">{k}</span><h3>{t}</h3><p>{d}</p></div>' for k, t, d in STORIES)
          + '</div></div></section>')

STREAMS = [
    ("u", "U", "92", "#9DB52A", False, "Uranium", "National-scale uranium assessment",
     "A national-scale model of where uranium occurs in India's groundwater, checked against an independent validation dataset and turned into maps of risk, population exposure and governance priority.",
     "Paper submitted to journal; Best Paper Award, EHP NEXUS 2026"),
    ("f", "F", "9", "#4A9CC9", False, "Fluoride", "Fluoride and spatial resolution",
     "India-wide fluoride prediction that benchmarks deep learning models and tests how the resolution of environmental predictors (native, 500 m, 1 km, 5 km) changes what a model can see.",
     "In progress"),
    ("as", "As", "33", "#A8557E", False, "Arsenic", "Arsenic in the Middle Gangetic Plain",
     "Distribution, speciation and controls on arsenic mobilisation, with explainable AI used to check that model explanations stay physically plausible.",
     "Presented at As2024, Bhubaneswar"),
    ("ds", "DS", "", "#5B8FB9", True, "Downscaling", "Downscaling satellite predictors",
     "A physically informed framework for moving environmental data between coarse and fine resolutions without inventing detail, piloted on CHIRPS rainfall over Punjab.",
     "In progress"),
]
tabs = "".join(f'<button type="button" role="tab" id="tab-{k}" aria-controls="panel-{k}" aria-selected="{"true" if i == 0 else "false"}" tabindex="{0 if i == 0 else -1}"><span class="el{" method" if m else ""}" style="--c:{c}" aria-hidden="true">{f"<small>{z}</small>" if z else ""}<b>{sym}</b></span>{lab}</button>'
               for i, (k, sym, z, c, m, lab, t, d, st) in enumerate(STREAMS))
panels = "".join(f'<div class="panel" role="tabpanel" id="panel-{k}" aria-labelledby="tab-{k}"{"" if i == 0 else " hidden"}><h3>{t}</h3><p>{d}</p><span class="status">{st}</span></div>'
                 for i, (k, sym, z, c, m, lab, t, d, st) in enumerate(STREAMS))

TIMELINE = [
    ("2026", "Teaching NRG169 and NRG176", "Principles of Remote Sensing; Principles of GIS and GNSS. MSc Geoinformatics, June–December 2026"),
    ("2026", "First Position and Best Paper Award", "ICSSR EHP NEXUS 2026, Gautam Buddha University, 27–28 April"),
    ("2026", "Rapporteur, National Geospatial Technology Workshop", "TERI SAS with NRSC, ISRO, 16–20 March"),
    ("2026", "World Sustainable Development Summit 2026", "Delegate, 25–27 February"),
    ("2026", "Water as a Commons workshop", "Water Governance Working Group with the Ostrom Workshop, Indiana University, 26–27 February"),
    ("2026", "PhD comprehensive examination completed", "January; uranium paper submitted to a journal"),
    ("2025", "Judge, TERI SAS Sustainability Hackathon", "18–19 November"),
    ("2025", "Taught Principles of Remote Sensing practicals", "NRG169, 32 practical hours, July–December"),
    ("2025", "Rapporteur for two sessions, WSDS 2025", "World Sustainable Development Summit, 6–7 March"),
    ("2024", "As2024 conference presentation", "Arsenic in the Environment, KIIT, Bhubaneswar, 20–24 October"),
]
timeline = '<ol class="timeline">' + "".join(f'<li><span class="yr">{y}</span><div><h3>{t}</h3><p>{m}</p></div></li>' for y, t, m in TIMELINE) + "</ol>"


def hl(kick, title, text, links, pic=None, art=None, wide=False, fit=False):
    if pic:
        pics = pic if isinstance(pic, list) else [pic]
        p = f'<div class="pic{" fit" if fit else ""}{" stack" if len(pics) > 1 else ""}">' + "".join(f'<img src="{a}" alt="{b}" loading="lazy">' for a, b in pics) + '</div>'
    else:
        p = f'<div class="pic art" aria-hidden="true"><span>{art[0]}<small>{art[1]}</small></span></div>'
    go = "".join(f'<a href="{h}">{t}</a>' for t, h in links)
    return f'<article class="hl{" wide" if wide else ""}">{p}<div class="txt"><span class="kick">{kick}</span><h3>{title}</h3><p>{text}</p>{f"<div class=go>{go}</div>" if go else ""}</div></article>'


def slot(a, b):
    """Placeholder tile for a photo that is still to be added."""
    return (a, b)


HIGHLIGHTS = "".join([
    hl("April 2026, Gautam Buddha University", "First Position and Best Paper Award, EHP NEXUS 2026",
       "At the ICSSR-sponsored national conference <em>The Nexus Imperative: Environment, Public Health and Policy for a Sustainable Future</em>, my machine-learning framework for uranium risk assessment, population exposure and groundwater governance in urban India won first position for the oral presentation.",
       [("Photos and certificate", "publications.html#conferences"), ("LinkedIn post", "https://www.linkedin.com/feed/update/urn:li:activity:7455656612595126273/")],
       pic=[("assets/img/award-talk.jpg", "Presenting the uranium risk framework at EHP NEXUS 2026"), ("assets/img/award-stage.jpg", "Receiving the Best Paper Award at EHP NEXUS 2026")], wide=True),
    hl("2023, Journal of Mountain Science", "Land surface temperature trends across the Indus River Basin",
       "Our peer-reviewed paper on spatial and elevation-wise daytime and nighttime LST trends, built in Google Earth Engine. The figure shows how the trends differ by season, day and night.",
       [("Read the paper", "https://doi.org/10.1007/s11629-023-8157-8")],
       pic=("assets/img/lst-trends.png", "Seasonal daytime and nighttime LST trends across the Indus River Basin, from the paper"), fit=True),
    hl("October 2024, KIIT, Bhubaneswar", "Poster at As2024, the International Congress on Arsenic in the Environment",
       "At the 9th International Congress and Exhibition on Arsenic in the Environment, I presented the distribution, speciation and controls on arsenic mobilisation in the aquifers of the Middle Gangetic Plain.",
       [("Photos and certificates", "publications.html#conferences")],
       pic=("assets/img/as2024-standee.jpg", "At the As2024 congress, Bhubaneswar")),
    hl("February 2026, Taj Palace, New Delhi", "Delegate, World Sustainable Development Summit 2026",
       "The Silver Jubilee edition of TERI's flagship summit: <em>Transformations: Vision, Voices, and Values for Sustainable Development and Climate Action</em>.",
       [("In the CV", "cv.html#rapporteur")], art=slot("WSDS", "2026, Delegate")),
    hl("February 2026, New Delhi", "Water as a Commons, with the Ostrom Workshop",
       "A Water Governance Working Group workshop with the Ostrom Workshop, Indiana University Bloomington and IU India Gateway, including a field visit along the Yamuna with INTACH Delhi.",
       [("In the CV", "cv.html#workshops")], art=slot("Yamuna", "Field visit")),
    hl("March 2025, World Sustainable Development Summit", "Rapporteur for two high-level sessions",
       "Documented the ministerial session on NDC 3.0 and the high-level plenary on integrated action at WSDS 2025, and wrote their published summaries.",
       [("NDC 3.0 session", "https://www.linkedin.com/pulse/ndc-30-multilateralism-strategic-insights-road-cop30-cop33-agrawal-fzeic/"), ("Plenary session", "https://www.linkedin.com/pulse/high-level-plenary-achieving-sustainable-development-through-agrawal-wfsxc/"), ("LinkedIn post", "https://www.linkedin.com/feed/update/urn:li:activity:7307294640695586816/")],
       art=slot("WSDS", "2025, Rapporteur")),
    hl("August 2025, virtual", "QGreenland Educator Workshop",
       "Three days developing classroom activities with QGreenland, the free GIS data package for Greenland and the Arctic, linking my teaching with my interest in the cryosphere.",
       [("In the CV", "cv.html#training")], art=slot("QGreenland", "Educator workshop")),
    hl("2025 – 2026, TERI SAS", "Teaching MSc Geoinformatics",
       "Principles of Remote Sensing and Principles of GIS and GNSS, including the hands-on lab sessions.",
       [("Teaching page", "teaching.html")], art=("MSc", "Geoinformatics")),
])

WRITING = f"""<div class="writing">
  <article class="article"><div class="pic art" aria-hidden="true"><span>NDC 3.0<small>Ministerial session</small></span></div><div class="txt"><span class="kick">15 March 2025, LinkedIn article</span>
    <h3>NDC 3.0 and Multilateralism: Strategic Insights on the Road to COP30 and COP33</h3>
    <p>Key messages from the WSDS 2025 ministerial session, with Prof. Jim Skea (IPCC) and ministers from Brazil, Norway, Nepal and the Maldives: climate finance, locally led action and early warning systems.</p>
    <a class="read" href="https://www.linkedin.com/pulse/ndc-30-multilateralism-strategic-insights-road-cop30-cop33-agrawal-fzeic/">Read the article</a></div></article>
  <article class="article"><div class="pic art" aria-hidden="true"><span>Plenary<small>Integrated action</small></span></div><div class="txt"><span class="kick">16 March 2025, LinkedIn article</span>
    <h3>High-level Plenary: Achieving Sustainable Development through Integrated Action</h3>
    <p>A summary of the WSDS 2025 plenary, with five action points on just transition, community empowerment, collaboration, climate-resilient policy and science-based solutions.</p>
    <a class="read" href="https://www.linkedin.com/pulse/high-level-plenary-achieving-sustainable-development-through-agrawal-wfsxc/">Read the article</a></div></article>
</div>"""

hero = f"""
<div class="banner"><div class="banner-inner">
  <div>
    <h1>Kavya Agrawal</h1>
    <p class="role">PhD Scholar, Department of Natural &amp; Applied Sciences<br>TERI School of Advanced Studies, New Delhi</p>
    <div class="cta">
      <a class="btn" href="research.html">Explore research</a>
      <a class="btn ghost" href="Kavya_Agrawal_CV.pdf">{DL}Download CV</a>
      <a class="btn ghost" href="mailto:{L['teri']}">{MAIL}Email</a>
    </div>
  </div>
  <figure class="portrait"><img src="assets/img/headshot.jpg" alt="Portrait of Kavya Agrawal" width="537" height="716"></figure>
</div></div>
<ul class="glance" aria-label="At a glance">
  <li><a href="research.html#current"><b>3</b><span>contaminants studied: uranium, fluoride, arsenic</span></a></li>
  <li><a href="publications.html#articles"><b>2</b><span>journal articles, with 3 manuscripts in progress</span></a></li>
  <li><a href="publications.html#conferences"><b>7</b><span>conference presentations since 2022</span></a></li>
  <li><a href="#highlights"><b>1st</b><span>Best Paper Award, EHP NEXUS 2026</span></a></li>
</ul>"""

home = f"""
<section id="about"><h2>About</h2>
<div class="about">
  <div>
    <p>I work where Earth observation, water and people meet. As a PhD scholar at TERI School of Advanced Studies, I build national-scale machine-learning frameworks that predict groundwater contamination across India, from uranium and fluoride to arsenic, and turn those predictions into maps of risk, population exposure and governance priorities.</p>
    <p>My toolkit brings together remote sensing, GIS, Google Earth Engine, hydrogeochemistry, machine learning and deep learning. Along the way I have studied land surface temperature, permafrost and snow in the Indus Basin, worked on downscaling satellite data, taught remote sensing and GIS to MSc students, and served as a rapporteur at the World Sustainable Development Summit.</p>
    <p>I want to carry these methods to bigger questions: climate change and the cryosphere in High Mountain Asia and the polar regions, water security, and even reading history and archaeology from space. I am always glad to hear about new ideas and collaborations.</p>
  </div>
  <aside>
    <h3>Doctoral research</h3><p><em>Development of an Adaptable Machine Learning Based Framework for Multi-Contaminant Prediction</em></p>
    <h3>Supervisor</h3><p><a href="https://www.linkedin.com/in/chander-kumar-singh-01542227/">Prof. Chander Kumar Singh</a></p>
    <h3>Department</h3><p>Natural &amp; Applied Sciences, TERI School of Advanced Studies</p>
  </aside>
</div></section>
<section id="highlights" class="band-a"><h2>Highlights</h2>
<div class="highlights">{HIGHLIGHTS}</div></section>
<section id="streams"><h2>Research streams</h2>
<div class="tabs" data-tabs><div class="tablist" role="tablist" aria-label="Research streams">{tabs}</div>{panels}</div>
<p class="small" style="margin-top:1rem"><a href="research.html">More on the research page</a></p></section>
<section id="writing" class="band-b"><h2>Writing</h2>
<p class="lead">Session summaries from my work as a rapporteur.</p>{WRITING}</section>
<section id="engagement"><h2>Recent engagement</h2>{timeline}
<p class="small" style="margin-top:1rem"><a href="cv.html">The full record is in the CV</a></p></section>
<section id="what" class="band-a"><h2>What I do</h2>
<div class="now">
  <div><h3>Research</h3><p>Predicting groundwater contamination and its risk with remote sensing, GIS and machine learning, building on earlier work on land surface temperature, permafrost and snow.</p></div>
  <div><h3>Teaching</h3><p>Remote sensing, GIS and GNSS for MSc Geoinformatics, with hands-on lab practicals.</p></div>
  <div><h3>Service</h3><p>Judging and facilitating student challenges in sustainability and geospatial innovation.</p></div>
  <div><h3>Engagement</h3><p>Rapporteuring and taking part in summits, workshops and dialogues on climate, water and sustainable development.</p></div>
</div></section>
<section id="interests"><h2>Research interests</h2>
<ul class="chips">{"".join(f"<li>{x}</li>" for x in ["Groundwater quality", "Uranium, fluoride, arsenic", "Hydrogeochemistry", "Remote sensing and GIS", "Google Earth Engine", "Machine learning and AutoML", "Explainable AI", "Multi-resolution modelling", "Population exposure", "Groundwater governance", "Cryosphere and climate", "Water security", "Remote sensing for history and archaeology"])}</ul></section>
<section id="future"><h2>Where I would like to go next</h2>
<p class="lead">Research directions I hope to take up in the years ahead.</p>
<div class="future">{FUTURE}</div></section>
<section id="connect" class="band-b"><h2>Let's connect</h2>
<div class="connect">
  <div>
    <p>I welcome research collaborations, teaching opportunities and interdisciplinary work across environmental AI, groundwater quality, Earth observation and environmental governance.</p>
    <p class="addr">Department of Natural &amp; Applied Sciences<br>TERI School of Advanced Studies, Vasant Kunj Institutional Area, New Delhi 110070</p>
    <p><a href="mailto:{L['teri']}">{L['teri']}</a><br><a href="mailto:{L['gmail']}">{L['gmail']}</a></p>
    <p class="cta"><a class="btn" href="mailto:{L['teri']}">{MAIL}Email me</a><a class="btn ghost" href="Kavya_Agrawal_CV.pdf">{DL}Download CV</a></p>
  </div>
  <ul class="profiles">
    <li><a href="{L['linkedin']}">LinkedIn<span aria-hidden="true">↗</span></a></li>
    <li><a href="{L['scholar']}">Google Scholar<span aria-hidden="true">↗</span></a></li>
    <li><a href="{L['orcid']}">ORCID<span aria-hidden="true">↗</span></a></li>
    <li><a href="{L['researchgate']}">ResearchGate<span aria-hidden="true">↗</span></a></li>
    <li><a href="{L['github']}">GitHub<span aria-hidden="true">↗</span></a></li>
  </ul>
</div></section>
"""
page("index.html", "Kavya Agrawal", "Kavya Agrawal, PhD scholar at TERI School of Advanced Studies, New Delhi: groundwater contamination, remote sensing, GIS and machine learning.", home, pre=hero, post=beyond, mcls="home")

# ================================================================= RESEARCH
research = f"""
<div class="col page-head">
<h1 class="page-title">Research</h1>
<p class="lede">How far can we predict groundwater contamination across a country as large and varied as India, and what do those predictions mean for the people who drink the water?</p>
</div>
<section><h2>Doctoral research</h2>
<div class="col">
<p><em>Development of an Adaptable Machine Learning Based Framework for Multi-Contaminant Prediction</em></p>
<p>My PhD builds a national-scale framework for predicting groundwater contamination and assessing its risk. It combines groundwater observations and hydrochemistry with remote sensing and GIS layers on climate, hydrology, terrain, soil, geology, land use, human modification and population. The aims run from prediction and spatial risk mapping to testing uncertainty and robustness, understanding environmental controls, estimating exposure and supporting governance decisions.</p>
<p class="muted small">Supervisor: <a href="https://www.linkedin.com/in/chander-kumar-singh-01542227/">Prof. Chander Kumar Singh</a>. Registered February 2024; comprehensive examination completed January 2026.</p>
</div></section>
<section id="current"><h2>Current work</h2>{lst(CURRENT)}</section>
<section><h2>Earlier work: climate and cryosphere</h2>{lst(EARLIER)}</section>
<section id="future"><h2>Future research directions</h2><div class="future">{FUTURE}</div></section>
<section><h2>Projects</h2>
<h3>Postgraduate, 2021–2023</h3>{ul(PG)}
<h3>Undergraduate, 2018–2021</h3>{ul(UG)}</section>
"""
page("research.html", "Research, Kavya Agrawal", "Groundwater contamination prediction across India with remote sensing, GIS and machine learning: uranium, fluoride, arsenic and downscaling.", research)

# ================================================================= PUBLICATIONS
publications = f"""
<div class="col page-head"><h1 class="page-title">Publications</h1>
<p class="lede">Journal articles, manuscripts and conference presentations, newest first.</p>
<div class="links"><a href="{L['scholar']}">Google Scholar</a><a href="{L['orcid']}">ORCID 0009-0009-1032-2541</a><a href="{L['researchgate']}">ResearchGate</a></div></div>
<section id="articles"><h2>Journal articles</h2>{lst(PUBS)}</section>
<section id="manuscripts"><h2>Manuscripts</h2>{lst(MANUSCRIPTS)}</section>
<section id="conferences"><h2>Conference presentations</h2>{lst(TALKS)}</section>
"""
page("publications.html", "Publications, Kavya Agrawal", "Journal articles, manuscripts and conference presentations by Kavya Agrawal.", publications)

# ================================================================= TEACHING
teaching = f"""
<div class="col page-head"><h1 class="page-title">Teaching</h1>
<p class="lede">Course teaching in the MSc Geoinformatics programme at TERI School of Advanced Studies.</p></div>
<section><h2>Courses</h2>{lst(TEACHING)}</section>
<section id="lab"><h2>In the lab</h2>
<div class="col"><p>Most of my teaching happens at the computer, with students working on real satellite data from Indian landscapes. Each practical starts from a question, such as how a city has grown or how healthy a crop looks, and works out which data and which steps will answer it.</p></div>
<div class="labs">
  <div><span class="kick">NRG169</span><h3>Principles of Remote Sensing</h3>
  <ul>
    <li>Getting started with ERDAS IMAGINE: opening, displaying and navigating Landsat 8/9 scenes</li>
    <li>Band combinations, true and false colour composites, and what each one reveals</li>
    <li>Reading spectral signatures of vegetation, water, soil and built-up land straight from Landsat bands</li>
    <li>Image enhancement and visual interpretation of land cover</li>
    <li>Applied exercises on urban patterns, vegetation and geomorphology</li>
  </ul></div>
  <div><span class="kick">NRG176</span><h3>Principles of GIS and GNSS</h3>
  <ul>
    <li>How GPS and GNSS work, and collecting and checking positions in the field</li>
    <li>Satellite navigation systems and positioning accuracy</li>
    <li>Georeferencing scanned maps and imagery</li>
    <li>Building, editing and mapping spatial data in ArcGIS Pro</li>
    <li>Applied exercises on urban patterns, vegetation and geomorphology</li>
  </ul></div>
</div>
<div class="col"><p class="small muted" style="margin-top:1rem">Both courses carry 4 credits and 60 hours (L-T-P 42-2-32). NRG169 in 2025 included 32 practical hours.</p></div></section>
"""
page("teaching.html", "Teaching, Kavya Agrawal", "Courses taught by Kavya Agrawal in the MSc Geoinformatics programme at TERI SAS.", teaching)

# ================================================================= CV
CV_SECTIONS = []


def cvs(id_, title, body):
    CV_SECTIONS.append((id_, title, f'<section id="{id_}"><h2>{title}</h2>{body}</section>'))


cvs("profile", "Profile", "<p>PhD scholar in Natural and Applied Sciences working at the intersection of groundwater systems, hydrogeochemistry, environmental geoinformatics and artificial intelligence. My doctoral work focuses on large-scale prediction and risk assessment of groundwater contamination, integrating groundwater observations with remote sensing, GIS and multi-source environmental data across uranium, fluoride and arsenic contamination. Methods include machine learning, deep learning, automated machine learning and spatial modelling, with broader interests in population exposure, environmental vulnerability, groundwater governance, water security, sustainable development and the cryosphere.</p>")
cvs("education", "Education", lst(EDUCATION))
cvs("doctoral", "Doctoral research", lst([
    entry("Thesis", "Development of an Adaptable Machine Learning Based Framework for Multi-Contaminant Prediction"),
    entry("Supervisor", '<a href="https://www.linkedin.com/in/chander-kumar-singh-01542227/">Prof. Chander Kumar Singh</a>'),
    entry("Status", "Full-time. Registered 1 February 2024. Comprehensive examination completed 28 January 2026."),
    entry("Coursework", "PhD coursework, CGPA 9.0/10", '<ul class="plain-list"><li>RPR275 Research and Publication Ethics, 2 credits, grade A</li><li>RPR271 Research Methodology, 3 credits, grade A</li><li>NRE115 Environmental Statistics, 4 credits, grade A</li><li>NRG172 Digital Image Processing &amp; Information Extraction, 4 credits, grade A</li></ul>'),
    entry("Framework", "National-scale framework for groundwater contamination prediction and risk assessment", "Combines groundwater observations, hydrochemistry, remote sensing, GIS, climate, hydrology, terrain, soil, geology, land use, human modification and population information. Aims: contamination prediction, spatial risk mapping, uncertainty and robustness assessment, environmental controls, exposure assessment and governance decision support."),
]))
cvs("research", "Research experience", lst(CURRENT + EARLIER))
cvs("publications", "Publications", lst(PUBS))
cvs("manuscripts", "Manuscripts", lst(MANUSCRIPTS))
cvs("conferences", "Conference presentations", lst(TALKS))
cvs("teaching", "Teaching", lst(TEACHING))
cvs("projects", "Projects", f"<h3>Postgraduate, 2021–2023</h3>{ul(PG)}<h3>Undergraduate, 2018–2021</h3>{ul(UG)}<h3>Other</h3>{ul(['Working With Geospatial Datasets', 'High-Quality Research Writing'])}")
cvs("awards", "Awards and achievements", lst([
    entry("2026", "First Position, oral presentation, and Best Paper Award", "ICSSR EHP NEXUS 2026, Gautam Buddha University."),
    entry("Nov 2024", "2nd Position, GeoPitch: 60 Seconds of GIS Work", "MAPPIT, World GIS Day celebration, Geoscience Club, Amity Institute of Geoinformatics and Remote Sensing, Amity University Uttar Pradesh, Noida, 23 November 2024.", more=cert("cert-geopitch-2024.jpg", "Certificate of achievement, GeoPitch, World GIS Day 2024"), more_label="Certificate"),
    entry("2018", "State Child Scientist Award", "National Science Congress."),
    entry("2015 – 2018", "Consecutive top 3 ranks, English Olympiads", "British Olympiad Foundation."),
    entry("2016, 2018", "Merit Awards"),
    entry("", "20 cultural and general knowledge awards", "From various organisations, including prizes in dance."),
]))
cvs("rapporteur", "Rapporteurship and policy engagement", lst([
    entry("Mar 2026", "Rapporteur, National Workshop on Geospatial Technology for Climate Action, Sustainability and Disaster Risk Reduction", "TERI School of Advanced Studies with the Regional Remote Sensing Centre–North, NRSC, ISRO, 16–20 March 2026. Also a volunteer for the programme.", more=gal(("cert-nrsc-volunteer-2026.jpg", "Certificate of appreciation as a volunteer, RRSC-North, NRSC, ISRO"), ("cert-nrsc-participation-2026.jpg", "Certificate of appreciation for participating, RRSC-North, NRSC, ISRO")), more_label="Certificates"),
    entry("Feb 2026", "Delegate, World Sustainable Development Summit 2026", "Taj Palace, New Delhi, 25–27 February 2026. Transformations: Vision, Voices, and Values for Sustainable Development and Climate Action."),
    entry("Mar 2025", "Rapporteur, Ministerial Session: NDC 3.0 and Multilateralism on the Road to COP30 and COP33", 'World Sustainable Development Summit 2025, TERI. India Habitat Centre, New Delhi, 6 March 2025. <a href="https://www.linkedin.com/pulse/ndc-30-multilateralism-strategic-insights-road-cop30-cop33-agrawal-fzeic/">Session summary</a>'),
    entry("Mar 2025", "Rapporteur, High-Level Plenary on Achieving Sustainable Development through Integrated Action", 'World Sustainable Development Summit 2025, TERI. India Habitat Centre, New Delhi, 7 March 2025. <a href="https://www.linkedin.com/pulse/high-level-plenary-achieving-sustainable-development-through-agrawal-wfsxc/">Session summary</a>'),
]))
cvs("positions", "Positions of responsibility", lst([
    entry("2026", "Facilitator and Judge, Programme LEAD 2026", "TERI SAS. Sustainable City Design Challenge for students of classes 9–12."),
    entry("Nov 2025", "Judge and Panel Member, TERI SAS Sustainability Hackathon 2025", "Expert evaluation panel for school and undergraduate sustainability proposals, 18–19 November 2025."),
    entry("2025", "Judge, KnoxCode 2025, Geospatial Innovation Challenge", "Organised by GeoknoX, TERI SAS, as part of Aahwaan Fest 2025."),
    entry("2018 – 2021", "Editor-in-Chief, Geography Association", "University of Delhi."),
    entry("2018 – 2020", "Magazine Coordinator, <em>Vani</em>", "Shaheed Bhagat Singh College, University of Delhi."),
    entry("2019 – 20", "English Editor, <em>Vani</em>", "Magazine Committee, Shaheed Bhagat Singh College, University of Delhi.", more=cert("cert-vani-editor-2019.jpg", "Certificate of appreciation, English Editor, Magazine Committee 2019–20"), more_label="Certificate"),
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
    entry("Mar 2025", "World Sustainable Development Summit 2025", "New Delhi, 5–7 March 2025. Partnerships for Accelerating Sustainable Development and Climate Solutions. Rapporteur and volunteer.", more=cert("cert-wsds2025-volunteer.jpg", "Certificate of appreciation as a volunteer, WSDS 2025"), more_label="Certificate"),
    entry("Feb 2025", "National Science Day 2025", "Vigyan Bhawan, New Delhi, 28 February 2025. <em>Empowering Indian Youth for Global Leadership in Science and Innovation for Viksit Bharat</em>, Department of Science and Technology, Government of India.", more=cert("cert-science-day-2025.jpg", "Certificate of participation, National Science Day 2025"), more_label="Certificate"),
    entry("Oct 2024", "Lecture by Professor John A. Cherry on groundwater and sustainable development", "2020 Stockholm Water Prize laureate, 24 October 2024. Prof. Cherry also spent four hours at the Analytical and Geochemistry Laboratory, TERI SAS, discussing the lab's current and future work."),
    entry("2023", "Workshop on Remote Sensing of Cryosphere (WRSC 2023)", "Three-day workshop, Centre of Studies in Resources Engineering, IIT Bombay, with the IEEE GRSS Bombay Chapter.", more=cert("cert-wrsc-2023.jpg", "Certificate of participation, WRSC 2023"), more_label="Certificate"),
    entry("", "Climate Skills: Seeds for Transition", "TERI SAS and TERI with British Council and HSBC Bank."),
]))
cvs("training", "Training, capacity building and schools", lst([
    entry("Mar 2026", "National Workshop on Geospatial Technology for Climate Action, Sustainability and Disaster Risk Reduction", "TERI SAS in collaboration with NRSC, ISRO, 16–20 March 2026. Participant, volunteer and rapporteur."),
    entry("Dec 2024", "Capacity Building Workshop on UAV/Drone Applications in Environment and Natural Resources Management: A Hands-on Training Program", "Three days, TERI SAS with IIT BHU, IIT Roorkee, Namami Gange, Hokkaido University, Global Land Programme, GLP Japan, GuruJal (Abhipsa Foundation) and Kambil, 10–12 December 2024.", more=cert("cert-uav-workshop-2024.jpg", "Certificate of completion, UAV/Drone workshop, TERI SAS"), more_label="Certificate"),
    entry("Nov – Dec 2024", "NGP-DST Winter School on Geospatial Technologies (Level 1)", "21-day capacity building programme, Amity School of Natural Resources and Sustainable Development, Amity University, Noida, supported by the National Geospatial Programme, DST, Government of India, 18 November – 7 December 2024. Grade A. Included a visit to Esri India.", more=cert("cert-ngp-winter-school-2024.jpg", "Certificate, NGP-DST Winter School on Geospatial Technologies"), more_label="Certificate"),
    entry("Mar 2024", "Harnessing Geospatial Technology for Forest Fire Disaster Management: Mapping, Monitoring and Mitigation", "One-week capacity building programme under the ISRO Disaster Management Support Capacity Building (DMS-CB) Programme, sponsored by IIRS, ISRO, Dehradun. Amity School of Natural Resources and Sustainable Development, Amity University, Noida, 11–15 March 2024.", more=cert("cert-forest-fire-2024.jpg", "Certificate, forest fire disaster management programme, Amity University"), more_label="Certificate"),
    entry("Feb 2022", "Disaster Management Plans to Enhance Resilience of Institutional Buildings", "Online training, National Institute of Disaster Management, Ministry of Home Affairs, with the Centre for Disaster Management Studies, Shaheed Bhagat Singh College, 23–25 February 2022.", more=cert("cert-nidm-2022.jpg", "Certificate, NIDM online training"), more_label="Certificate"),
]))
SK = [
    ("Technical skills", ["GIS and remote sensing methods and techniques", "ArcGIS / ArcGIS Pro", "QGIS", "Google Earth / Google Earth Engine", "ERDAS / ERDAS Imagine", "Python", "JavaScript for Google Earth Engine", "pandas", "Machine learning, deep learning and automated machine learning", "AutoGluon", "Random Forest", "LightGBM", "SHAP and LIME explainable AI", "Spatial data analysis and visualisation", "Time-series modelling and trend analysis", "Mann–Kendall trend testing and Theil–Sen slope", "Remote-sensing image enhancement and feature extraction", "Orthorectification and mosaicking", "Satellite-image acquisition, processing and visualisation", "DEM processing"]),
    ("Research and professional skills", ["Field-based and survey-based research", "Socio-environmental data analysis", "Groundwater contamination and drinking-water quality assessment", "Disaster risk reduction and resilience concepts", "Climate–water–environment interactions", "Sustainability and climate policy", "Academic writing and conference presentations", "Scientific communication and reporting", "Editorial and content development", "Rapporteurship and policy-session documentation", "Academic coordination and event support", "Interdisciplinary collaboration"]),
    ("Remote-sensing and environmental parameters", ["MAAT", "BMAT", "PISR", "Forest monitoring", "NDVI / NDBI", "Mann–Kendall trend and Theil–Sen slope", "Urban sprawl analysis", "Snow estimates", "Slope", "Night-time light", "Time-series modelling", "MODIS Terra/Aqua", "Trend tests", "Land-use and environmental history", "Remote-sensing data repositories", "Land surface temperature", "Image enhancement and feature extraction", "Orthorectification and mosaicking", "Satellite-image acquisition and processing", "Precipitation", "DEM", "Landsat", "SRTM", "Climate variables: temperature, precipitation, aerosols, solar radiation and air temperature", "Cryosphere-related parameters and processes"]),
    ("Earth observation, environmental and hydrogeochemical data", ["Landsat 8/9", "Sentinel", "MODIS Terra/Aqua", "VIIRS", "FIRMS", "CHIRPS", "IMD precipitation products", "ERA5-Land", "TerraClimate", "GLDAS", "GRACE", "SRTM", "MERIT Hydro", "JRC Global Surface Water", "OpenLandMap soil products", "GPW", "GHM", "GHSL", "SMOD", "LCZ", "CSP Global Human Modification and related datasets", "CGWB groundwater and hydrogeochemical observations", "Literature-derived groundwater quality observations", "Hydrochemical variables: pH, EC, Ca, Mg, Na, K, HCO<sub>3</sub>, Cl, SO<sub>4</sub>, NO<sub>3</sub>, fluoride, phosphate and uranium"]),
    ("Data management, QA/QC and research reliability", ["Duplicate detection and duplicate-preservation rules", "Administrative-name normalisation and standardisation", "Coordinate validation and geometry reconstruction", "Sentinel-value handling", "Missing-value identification", "Source preservation and data lineage/provenance", "Unit verification", "Temporal and spatial compatibility checks", "Resolution harmonisation", "Independent validation", "Masked-pixel handling", "Denominator consistency in exposure estimates", "Correlation versus causation in interpretation", "Caution about Pearson correlation as a hard feature filter", "Ground truth, transferability, uncertainty and physical plausibility", "Temporal mismatch between monitoring observations and environmental predictors", "Resampling methodology: true downscaling versus interpolation", "Geogenic versus environmental controls in groundwater contamination"]),
]
cvs("skills", "Skills and working knowledge", "".join(f'<h3>{a}</h3><ul class="dots">' + "".join(f"<li>{x}</li>" for x in b) + "</ul>" for a, b in SK))
SUBJECTS = ["Geomorphology", "Climatology &amp; Oceanography", "Cartographic Techniques", "Thematic Cartography", "Remote Sensing &amp; GIS", "Statistical Methods in Geography", "Field Work &amp; Research Methodology", "Academic Writing &amp; Composition", "Geography of India", "Human Geography", "Disaster Management", "Media &amp; Communication Skills", "History of Geographical Thought", "Social Geography", "Political Geography", "Economic Geography", "Agricultural Geography", "Population &amp; Settlement Geography", "Environmental Geography", "Regional Planning &amp; Development"]
cvs("subjects", "Subjects studied", '<ul class="dots">' + "".join(f"<li>{x}</li>" for x in SUBJECTS) + "</ul>")
cvs("future", "Future research interests", ul([f"<b>{a}</b>: {b[0].lower() + b[1:]}" for a, b in FUTURE_ITEMS]))
cvs("volunteering", "Volunteering and co-curricular", lst([
    entry("2016 – present", "Volunteer, SWAPO NGO"),
    entry("2019 – 2021", "National Service Scheme (NSS)"),
    entry("2018 – 2019", "Coordination of Volunteers, Vasundhara"),
    entry("2018 – 2023", "Personal blogging and content writing"),
]))
cvs("interests", "Personal interests", "<p>Collecting old coins and stamps, reading historic stories and accounts, photography and videography, travelling, badminton, dance, debating and Model UN.</p>")
cvs("keywords", "Research keywords", "<p>Groundwater contamination; groundwater quality; groundwater quantity; hydrogeochemistry; uranium; fluoride; arsenic; groundwater risk assessment; population exposure; environmental vulnerability; groundwater governance; water security; environmental geoinformatics; geospatial data science; remote sensing; GIS; Google Earth Engine; machine learning; deep learning; AutoML; explainable AI; spatial modelling; spatial statistics; multi-resolution modelling; downscaling; upscaling; Earth observation; hydrology; climate–water interactions; hydro-environmental systems; cryosphere; permafrost; snow; glacier-fed hydrology; LST; climate change; sustainability; disaster risk reduction; policy engagement; environmental inequality; exposure assessment.</p>")
cvs("contact", "Contact", f"""<p>Department of Natural &amp; Applied Sciences, TERI School of Advanced Studies, Vasant Kunj Institutional Area, New Delhi 110070, India</p>
<p><a href="mailto:{L['teri']}">{L['teri']}</a> &nbsp;·&nbsp; <a href="mailto:{L['gmail']}">{L['gmail']}</a></p>
<p class="links" style="margin-top:0"><a href="{L['scholar']}">Google Scholar</a><a href="{L['orcid']}">ORCID</a><a href="{L['researchgate']}">ResearchGate</a><a href="{L['linkedin']}">LinkedIn</a><a href="{L['github']}">GitHub</a></p>""")

toc = "".join(f'<li><a href="#{i}">{t}</a></li>' for i, t, _ in CV_SECTIONS)
cv = f"""
<div class="cv-head page-head">
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
