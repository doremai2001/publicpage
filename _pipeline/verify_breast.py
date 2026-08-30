# -*- coding: utf-8 -*-
"""Verification pass over the generated breast pages."""
import difflib, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import breast, topicbuild as tb

REPO = "/home/claude/repo"
UPLOAD = "/home/claude/upload-breast"
PRE = "/home/claude/prebackup"
ORD = [s for sec in breast.SECTIONS for s in sec["slugs"]]
ART_TPL = {"zh": "cc-first-month.html", "en": "cc-first-month-en.html"}
HUB_TPL = {"zh": "cc.html", "en": "cc-en.html"}
fails = []

def chk(ok, msg):
    if not ok:
        fails.append(msg)

hubs = ["bc.html", "bc-en.html"]
arts = ["bc-%s.html" % s for s in ORD] + ["bc-%s-en.html" % s for s in ORD]
pages = hubs + arts

# 1 ------------------------------------------------------------- page count --
chk(len(arts) == 48, "article page count %d" % len(arts))
chk(len(pages) == 50, "page count %d" % len(pages))
for p in pages:
    chk(os.path.exists(os.path.join(REPO, p)), "missing %s" % p)
    chk(os.path.exists(os.path.join(UPLOAD, p)), "missing from upload dir: %s" % p)
for extra in ("topics.html", "topics-en.html", "sitemap.xml"):
    chk(os.path.exists(os.path.join(UPLOAD, extra)), "upload missing %s" % extra)
chk(len(os.listdir(UPLOAD)) == 53, "upload dir has %d files" % len(os.listdir(UPLOAD)))
sm = open(os.path.join(REPO, "sitemap.xml"), encoding="utf-8").read()
pre_sm = open(os.path.join(PRE, "sitemap.xml"), encoding="utf-8").read()
chk(sm.count("<url>") == pre_sm.count("<url>") + 50,
    "sitemap count %d (was %d)" % (sm.count("<url>"), pre_sm.count("<url>")))
for p in pages:
    chk(("<loc>%s%s</loc>" % (tb.BASE, p)) in sm, "sitemap missing %s" % p)
# priorities + lastmod on the new entries only
for p, prio in ([("bc.html", "0.85"), ("bc-en.html", "0.75")]
                + [("bc-%s.html" % s, "0.75") for s in ORD]
                + [("bc-%s-en.html" % s, "0.65") for s in ORD]):
    ln = [l for l in sm.splitlines() if "<loc>%s%s</loc>" % (tb.BASE, p) in l][0]
    chk("<lastmod>%s</lastmod>" % breast.DATE in ln, "%s lastmod" % p)
    chk("<priority>%s</priority>" % prio in ln, "%s priority" % p)
# existing entries and their order untouched
old_lines = [l for l in pre_sm.splitlines()]
new_lines = [l for l in sm.splitlines() if "/bc" not in l or "/bc-" not in l]
kept = [l for l in sm.splitlines()
        if not re.search(r"<loc>%sbc(-|\.)" % re.escape(tb.BASE), l)]
chk(kept == old_lines, "existing sitemap lines changed or reordered")
print("1. %d article pages + %d hubs = %d new pages; sitemap <url> = %d (was %d, +%d); "
      "all pre-existing sitemap lines unchanged and in order; upload dir = %d files"
      % (len(arts), len(hubs), len(pages), sm.count("<url>"),
         pre_sm.count("<url>"), sm.count("<url>") - pre_sm.count("<url>"),
         len(os.listdir(UPLOAD))))

# 2 ------------------------------------------------------------- link scan ---
files = set(os.listdir(REPO))
bad = []
nlinks = 0
for name in sorted(files):
    if name.endswith(".html"):
        s = open(os.path.join(REPO, name), encoding="utf-8").read()
        for t in re.findall(r'href="([^":]+\.html)(?:[#?][^"]*)?"', s):
            nlinks += 1
            if t not in files:
                bad.append((name, t))
chk(not bad, "broken links: %s" % bad[:10])
print("2. %d internal .html links across %d pages in the repo: %d unresolved %s"
      % (nlinks, sum(1 for f in files if f.endswith('.html')), len(bad),
         bad[:10] if bad else ""))

# 3 ------------------------------------ citation / h4 / reference symmetry ---
rows = []
for slug in ORD:
    fr = {}
    for lang, d in (("zh", breast.SRC["body_zh"]), ("en", breast.SRC["body_en"])):
        src = open(os.path.join(d, slug + ".html"), encoding="utf-8").read()
        body, items, n = tb.split_fragment(src)
        page = open(os.path.join(REPO, "bc-%s%s.html"
                                 % (slug, "-en" if lang == "en" else "")),
                    encoding="utf-8").read()
        pb = re.search(r'<div class="body-html">\n(.*?)\n    </div>', page, re.S).group(1)
        pr = re.search(r'<div class="refs">.*?<ol>(.*?)</ol>', page, re.S).group(1)
        fr[lang] = (
            len(re.findall(r'<sup class="cit">', body)),
            len(re.findall(r"<h4>", body)),
            n,
            len(re.findall(r'<sup class="cit">', pb)),
            len(re.findall(r"<h4>", pb)),
            len(re.findall(r"<li>", pr)),
        )
        chk(fr[lang][0] == fr[lang][3], "%s %s citations page!=source" % (slug, lang))
        chk(fr[lang][1] == fr[lang][4], "%s %s h4 page!=source" % (slug, lang))
        chk(fr[lang][2] == fr[lang][5], "%s %s refs page!=source" % (slug, lang))
        chk("<ol>" not in pr and "</ol>" not in pr, "%s %s nested <ol>" % (slug, lang))
        chk("<p></p>" not in pr, "%s %s trailing empty p" % (slug, lang))
        chk("<hr>" not in pb, "%s %s hr leaked into body" % (slug, lang))
        mm = re.search(r'<div class="meta">(.*?)</div>', page).group(1)
        num = int(re.search(r"\d+", mm.split(" · ")[2]).group(0))
        chk(num == n, "%s %s meta N" % (slug, lang))
    chk(fr["zh"][:3] == fr["en"][:3],
        "%s zh/en mismatch %s %s" % (slug, fr["zh"], fr["en"]))
    rows.append((slug, fr["zh"][0], fr["zh"][1], fr["zh"][2]))
print("3. citations / <h4> / references, page == source and zh == en:")
for r in rows:
    print("     %-24s cit=%-3d h4=%-2d refs=%d" % r)

# 4 --------------------------------------------------- well-formed-ish check --
styles = {}
for lang in ("zh", "en"):
    for f in (ART_TPL[lang], HUB_TPL[lang]):
        styles[f] = tb.RE_STYLE.search(
            open(os.path.join(REPO, f), encoding="utf-8").read()).group(0)
chk(len(set(styles.values())) == 1, "the four templates do not share one style block")
STYLE = styles[ART_TPL["zh"]]
for p in pages:
    s = open(os.path.join(REPO, p), encoding="utf-8").read()
    for tag, cnt in (("<style>", 1), ("</style>", 1), ("<body>", 1),
                     ("</body>", 1), ("</html>", 1), ("<head>", 1), ("</head>", 1)):
        chk(s.count(tag) == cnt, "%s: %s x%d" % (p, tag, s.count(tag)))
    st = tb.RE_STYLE.search(s)
    chk(st and st.group(0) == STYLE, "%s: style block differs from template" % p)
print("4. <style>/</style>/<body>/</body>/</html>/<head>/</head> exactly once on all "
      "%d; style block byte-identical to the template's (%d bytes)"
      % (len(pages), len(STYLE)))

# 5 ------------------------------------------------------------- hreflang ----
npair = 0
for slug in ORD + [None]:
    z = "bc.html" if slug is None else "bc-%s.html" % slug
    e = "bc-en.html" if slug is None else "bc-%s-en.html" % slug
    npair += 1
    for p, other in ((z, e), (e, z)):
        s = open(os.path.join(REPO, p), encoding="utf-8").read()
        chk('<link rel="alternate" hreflang="zh-Hant" href="%s%s">' % (tb.BASE, z) in s,
            "%s hreflang zh" % p)
        chk('<link rel="alternate" hreflang="en" href="%s%s">' % (tb.BASE, e) in s,
            "%s hreflang en" % p)
        chk('<link rel="alternate" hreflang="x-default" href="%s%s">' % (tb.BASE, z) in s,
            "%s hreflang x-default" % p)
        chk('<link rel="canonical" href="%s%s">' % (tb.BASE, p) in s, "%s canonical" % p)
        chk('href="%s" hreflang=' % other in s, "%s lang switch -> %s" % (p, other))
print("5. hreflang zh-Hant/en/x-default + canonical + nav language switch, both "
      "directions, on all %d pairs (24 articles + the hub)" % npair)

# 6 ------------------------------------------------- topics.html diff ---------
for f, card in (("topics.html", breast.TOPIC_CARD_ZH),
                ("topics-en.html", breast.TOPIC_CARD_EN)):
    a = open(os.path.join(PRE, f), encoding="utf-8").read().splitlines(True)
    b = open(os.path.join(REPO, f), encoding="utf-8").read().splitlines(True)
    d = list(difflib.unified_diff(a, b, n=0))
    added = [l[1:] for l in d if l.startswith("+") and not l.startswith("+++")]
    removed = [l[1:] for l in d if l.startswith("-") and not l.startswith("---")]
    chk(removed == [], "%s: %d removed lines" % (f, len(removed)))
    chk("".join(added) == card, "%s: added text is not exactly the card" % f)
    print("6. %-15s +%d lines, -%d lines; the added block is byte-exactly the "
          "topiccard" % (f, len(added), len(removed)))
# four cards, two-column grid
for f in ("topics.html", "topics-en.html"):
    s = open(os.path.join(REPO, f), encoding="utf-8").read()
    chk(s.count('class="topiccard"') == 4, "%s: %d cards" % (f, s.count('class="topiccard"')))
    chk(s.count('<div class="topicgrid">') == 1, "%s topicgrid" % f)
    chk(".topicgrid{display:grid;grid-template-columns:1fr 1fr;" in s,
        "%s grid columns changed" % f)
    chk("@media (max-width:760px){.topicgrid{grid-template-columns:1fr}}" in s,
        "%s grid mobile rule changed" % f)
    body = re.search(r'<div class="topicgrid">(.*?)\n  </div>', s, re.S).group(1)
    chk(body.count('class="topiccard"') == 4, "%s cards not all inside the grid" % f)
print("   topicgrid is still 'grid-template-columns:1fr 1fr' (1fr on <=760px) and now "
      "holds 4 cards -> two full rows of two; nothing else on either page changed")

# 7 ------------------------------------------------------------- hub render ---
for lang, page in (("zh", "bc.html"), ("en", "bc-en.html")):
    s = open(os.path.join(REPO, page), encoding="utf-8").read()
    bar = tb.RE_HUB_TAGC.search(s).group(2)
    cnts = dict((k, int(n)) for k, n in
                re.findall(r'data-tag="([^"]*)">[^<]*<i>(\d+)</i>', bar))
    want = {}
    for slug in ORD:
        for k in breast.ART[slug]["tags"]:
            want[k] = want.get(k, 0) + 1
    want[""] = 24
    chk(cnts == want, "%s tagbar counts differ: %s" % (page, cnts))
    # every per-tag count equals the number of cards actually carrying that tag
    cards = re.findall(r'<a class="postcard" data-tags="([^"]*)" href="([^"]*)"', s)
    chk(len(cards) == 24, "%s: %d postcards" % (page, len(cards)))
    dom = {}
    for tags, _ in cards:
        for k in tags.split():
            dom[k] = dom.get(k, 0) + 1
    chk(dom == {k: v for k, v in cnts.items() if k},
        "%s: tagbar counts != card counts" % page)
    chk(sum(1 for _ in re.finditer(r'class="postgroup hnstep"', s)) == 4,
        "%s postgroups" % page)
    for si in range(4):
        grp = re.findall(r'<div class="postgroup hnstep">.*?\n  </div>', s, re.S)
        chk(len(grp) == 4, "%s groups" % page)
        chk(grp[si].count('class="postcard"') == 6,
            "%s group %d has %d cards" % (page, si + 1, grp[si].count('class="postcard"')))
    for i, slug in enumerate(ORD):
        chk(cards[i][1] == "bc-%s%s.html" % (slug, "-en" if lang == "en" else ""),
            "%s card %d order" % (page, i))
    chk(s.count("<h3><b>1</b>") == 1 and s.count("<h3><b>4</b>") == 1,
        "%s section headings" % page)
    ld = json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>',
                              s, re.S).group(1))
    chk(len(ld["hasPart"]) == 24, "%s hasPart %d" % (page, len(ld["hasPart"])))
print("7. hub: 4 groups x 6 cards = 24, in reading order; 全部/All button = 24; "
      "%d per-tag counts each equal the number of cards carrying that tag; "
      "JSON-LD hasPart lists 24" % (len(want) - 1))

# 8 --------------------------------------------------- ld / nav / dates -------
for p in pages:
    s = open(os.path.join(REPO, p), encoding="utf-8").read()
    en = p.endswith("-en.html")
    chk(('<a href="topics-en.html" class="on">' if en else '<a href="topics.html" class="on">')
        in s, "%s nav active" % p)
    ld = json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>',
                              s, re.S).group(1))
    chk(ld["about"]["name"] == ("Breast cancer" if en else "乳癌"),
        "%s about.name=%s" % (p, ld["about"]["name"]))
    chk(ld["inLanguage"] == ("en" if en else "zh-Hant"), "%s inLanguage" % p)
    if ld["@type"] == "MedicalWebPage":
        chk(ld["datePublished"] == "2026-08-29" and ld["dateModified"] == "2026-08-29",
            "%s dates" % p)
print("8. nav active state per language; JSON-LD about.name = 乳癌 / Breast cancer; "
      "datePublished = dateModified = 2026-08-29 on all 48 articles")

# 9 -------------------------------------------------------------- pnav chain --
for lang, suf in (("zh", ""), ("en", "-en")):
    for i, slug in enumerate(ORD):
        s = open(os.path.join(REPO, "bc-%s%s.html" % (slug, suf)), encoding="utf-8").read()
        pn = re.search(r'<div class="pnav">(.*?)</div>', s, re.S).group(1)
        if i == 0:
            chk(pn.startswith("<span></span>"), "%s%s first has prev" % (slug, suf))
        else:
            chk('class="pv" href="bc-%s%s.html"' % (ORD[i - 1], suf) in pn,
                "%s%s prev" % (slug, suf))
        if i == len(ORD) - 1:
            chk(pn.endswith("<span></span>"), "%s%s last has next" % (slug, suf))
        else:
            chk('class="nx" href="bc-%s%s.html"' % (ORD[i + 1], suf) in pn,
                "%s%s next" % (slug, suf))
print("9. pnav chains all 24 in reading order, both languages; ends use <span></span>")

# 10 ------------------------ everything outside the slots is intact -----------
def skeleton(s):
    s = tb.RE_TITLE.sub("@", s); s = tb.RE_DESC.sub("@", s)
    s = tb.RE_OGT.sub("@", s); s = tb.RE_OGD.sub("@", s); s = tb.RE_OGU.sub("@", s)
    s = tb.RE_CANON.sub("@", s); s = tb.RE_ALTS.sub("@", s); s = tb.RE_LD.sub("@", s)
    s = tb.RE_LANG.sub("@", s)
    s = re.sub(r'(<div class="article">).*?(\n  </div>\n</section>)', r"\1@\2", s, flags=re.S)
    s = re.sub(r'<section class="band narrow">.*?\n</section>', "@", s, flags=re.S)
    return s

for lang, suf in (("zh", ""), ("en", "-en")):
    t = skeleton(open(os.path.join(REPO, ART_TPL[lang]), encoding="utf-8").read())
    for slug in ORD:
        g = skeleton(open(os.path.join(REPO, "bc-%s%s.html" % (slug, suf)),
                          encoding="utf-8").read())
        chk(g == t, "bc-%s%s: skeleton differs from %s" % (slug, suf, ART_TPL[lang]))
for lang, page in (("zh", "bc.html"), ("en", "bc-en.html")):
    t = skeleton(open(os.path.join(REPO, HUB_TPL[lang]), encoding="utf-8").read())
    g = skeleton(open(os.path.join(REPO, page), encoding="utf-8").read())
    chk(g == t, "%s: skeleton differs from %s" % (page, HUB_TPL[lang]))
print("10. every byte outside the substituted slots is identical to the template "
      "(svg, nav, footer, swirl script, hub tag-filter script, style)")

# 11 ------------------------------------------------- no double escaping ------
for p in pages:
    s = open(os.path.join(REPO, p), encoding="utf-8").read()
    chk("&amp;amp;" not in s and "&amp;quot;" not in s and "&#x27;" not in s,
        "%s: double-escaped entity" % p)
print("11. no double-escaped entities (&amp;amp; / &amp;quot; / &#x27;) on any page")

# 12 ------------------------------------------------- upload dir is a mirror --
import filecmp
for n in os.listdir(UPLOAD):
    chk(filecmp.cmp(os.path.join(UPLOAD, n), os.path.join(REPO, n), shallow=False),
        "upload copy differs: %s" % n)
print("12. all %d files in %s are byte-identical to the repo copies"
      % (len(os.listdir(UPLOAD)), UPLOAD))

print()
if fails:
    print("FAILURES (%d):" % len(fails))
    for f in fails:
        if f:
            print("   " + f)
else:
    print("ALL CHECKS PASSED")
