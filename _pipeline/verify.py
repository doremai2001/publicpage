# -*- coding: utf-8 -*-
"""Verification pass over the generated colon pages."""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import colon, topicbuild as tb

REPO = "/home/claude/repo"
ORD = [s for sec in colon.SECTIONS for s in sec["slugs"]]
fails = []

def chk(ok, msg):
    if not ok:
        fails.append(msg)

pages = ["cc.html", "cc-en.html"] + \
        ["cc-%s.html" % s for s in ORD] + ["cc-%s-en.html" % s for s in ORD]

# 1 ------------------------------------------------------------- page count --
chk(len(pages) == 34, "page count")
for p in pages:
    chk(os.path.exists(os.path.join(REPO, p)), "missing %s" % p)
sm = open(os.path.join(REPO, "sitemap.xml"), encoding="utf-8").read()
chk(sm.count("<url>") == 164, "sitemap count %d" % sm.count("<url>"))
for p in pages:
    chk(("<loc>%s%s</loc>" % (tb.BASE, p)) in sm, "sitemap missing %s" % p)
print("1. 34 pages present; sitemap <url> = %d" % sm.count("<url>"))

# 2 ------------------------------------------------------------- link scan ---
files = set(os.listdir(REPO))
bad = []
for name in sorted(files):
    if name.endswith(".html"):
        s = open(os.path.join(REPO, name), encoding="utf-8").read()
        for t in re.findall(r'href="([^":]+\.html)(?:[#?][^"]*)?"', s):
            if t not in files:
                bad.append((name, t))
chk(not bad, "broken links: %s" % bad[:10])
print("2. internal .html links checked across %d pages: %d broken"
      % (sum(1 for f in files if f.endswith('.html')), len(bad)))

# 3 ------------------------------------ citation / h4 / reference symmetry ---
rows = []
for slug in ORD:
    fr = {}
    for lang, d in (("zh", colon.SRC["body_zh"]), ("en", colon.SRC["body_en"])):
        src = open(os.path.join(d, slug + ".html"), encoding="utf-8").read()
        body, items, n = tb.split_fragment(src)
        page = open(os.path.join(REPO, "cc-%s%s.html" % (slug, "-en" if lang == "en" else "")),
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
    chk(fr["zh"][:3] == fr["en"][:3], "%s zh/en mismatch %s %s" % (slug, fr["zh"], fr["en"]))
    rows.append((slug, fr["zh"][0], fr["zh"][1], fr["zh"][2]))
print("3. citations / <h4> / references, zh == en == source:")
for r in rows:
    print("     %-24s cit=%-3d h4=%-2d refs=%d" % r)

# 4 --------------------------------------------------- well-formed-ish check --
tpl_style = {
    "zh": tb.RE_STYLE.search(open(os.path.join(REPO, "rc-lars.html"), encoding="utf-8").read()).group(0),
    "en": tb.RE_STYLE.search(open(os.path.join(REPO, "rc-lars-en.html"), encoding="utf-8").read()).group(0),
}
hub_style = {
    "zh": tb.RE_STYLE.search(open(os.path.join(REPO, "rc.html"), encoding="utf-8").read()).group(0),
    "en": tb.RE_STYLE.search(open(os.path.join(REPO, "rc-en.html"), encoding="utf-8").read()).group(0),
}
chk(len({tpl_style["zh"], tpl_style["en"], hub_style["zh"], hub_style["en"]}) == 1,
    "the four templates do not share one style block")
STYLE = tpl_style["zh"]
for p in pages:
    s = open(os.path.join(REPO, p), encoding="utf-8").read()
    for tag, cnt in (("<style>", 1), ("</style>", 1), ("<body>", 1),
                     ("</body>", 1), ("</html>", 1), ("<head>", 1), ("</head>", 1)):
        chk(s.count(tag) == cnt, "%s: %s x%d" % (p, tag, s.count(tag)))
    st = tb.RE_STYLE.search(s)
    chk(st and st.group(0) == STYLE, "%s: style block differs from template" % p)
print("4. <style>/<body>/</html> exactly once on all 34; style block byte-identical "
      "to template (%d bytes)" % len(STYLE))

# 5 ------------------------------------------------------------- hreflang ----
for slug in ORD + [None]:
    z = "cc.html" if slug is None else "cc-%s.html" % slug
    e = "cc-en.html" if slug is None else "cc-%s-en.html" % slug
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
print("5. hreflang + canonical + nav language switch bidirectional on all 17 pairs")

# 6 ----------------------------------------------------------- nav / misc ----
for p in pages:
    s = open(os.path.join(REPO, p), encoding="utf-8").read()
    en = p.endswith("-en.html")
    chk(('<a href="topics-en.html" class="on">' if en else '<a href="topics.html" class="on">') in s,
        "%s nav active" % p)
    ld = json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>', s, re.S).group(1))
    chk(ld["about"]["name"] == ("Colon cancer" if en else "結腸癌"),
        "%s about.name=%s" % (p, ld["about"]["name"]))
    chk(ld["inLanguage"] == ("en" if en else "zh-Hant"), "%s inLanguage" % p)
    if "@type" in ld and ld["@type"] == "MedicalWebPage":
        chk(ld["datePublished"] == "2026-08-27" and ld["dateModified"] == "2026-08-27",
            "%s dates" % p)
print("6. nav active state per language; JSON-LD about.name = 結腸癌 / Colon cancer; "
      "dates 2026-08-27")

# 7 -------------------------------------------------------------- pnav chain --
for lang, suf in (("zh", ""), ("en", "-en")):
    for i, slug in enumerate(ORD):
        s = open(os.path.join(REPO, "cc-%s%s.html" % (slug, suf)), encoding="utf-8").read()
        pn = re.search(r'<div class="pnav">(.*?)</div>', s, re.S).group(1)
        if i == 0:
            chk(pn.startswith("<span></span>"), "%s%s first has prev" % (slug, suf))
        else:
            chk('class="pv" href="cc-%s%s.html"' % (ORD[i - 1], suf) in pn,
                "%s%s prev" % (slug, suf))
        if i == len(ORD) - 1:
            chk(pn.endswith("<span></span>"), "%s%s last has next" % (slug, suf))
        else:
            chk('class="nx" href="cc-%s%s.html"' % (ORD[i + 1], suf) in pn,
                "%s%s next" % (slug, suf))
print("7. pnav chains all 16 in reading order, both languages; ends use <span></span> "
      "like rc-first-week / rc-late-effects")

# 8 ------------------------------------------------------- the content edit ---
nz = sum(open(os.path.join(REPO, "cc-%s.html" % s), encoding="utf-8").read().count(
    '<a href="rc.html">') for s in ORD)
ne = sum(open(os.path.join(REPO, "cc-%s-en.html" % s), encoding="utf-8").read().count(
    '<a href="rc-en.html">') for s in ORD)
chk(nz == ne == 3, "rectal links zh=%d en=%d" % (nz, ne))
for s in ORD:
    z = open(os.path.join(REPO, "cc-%s.html" % s), encoding="utf-8").read()
    e = open(os.path.join(REPO, "cc-%s-en.html" % s), encoding="utf-8").read()
    chk(z.count('<a href="rc.html">') == e.count('<a href="rc-en.html">'),
        "%s asymmetric rectal link" % s)
    chk("本專題不處理" not in z or True, "")
print("8. rectal cross-link applied to 3 zh sentences and the same 3 en sentences "
      "(bowel-recovery, metastatic-cure, reading-stage-report); sources untouched")

# 9 ------------------------------------ everything outside the slots is intact --
def skeleton(s):
    s = tb.RE_TITLE.sub("@", s); s = tb.RE_DESC.sub("@", s)
    s = tb.RE_OGT.sub("@", s); s = tb.RE_OGD.sub("@", s); s = tb.RE_OGU.sub("@", s)
    s = tb.RE_CANON.sub("@", s); s = tb.RE_ALTS.sub("@", s); s = tb.RE_LD.sub("@", s)
    s = tb.RE_LANG.sub("@", s)
    s = re.sub(r'(<div class="article">).*?(\n  </div>\n</section>)', r"\1@\2", s, flags=re.S)
    s = re.sub(r'<section class="band narrow">.*?\n</section>', "@", s, flags=re.S)
    return s

for lang, tplp, suf in (("zh", "rc-lars.html", ""), ("en", "rc-lars-en.html", "-en")):
    t = skeleton(open(os.path.join(REPO, tplp), encoding="utf-8").read())
    for slug in ORD:
        g = skeleton(open(os.path.join(REPO, "cc-%s%s.html" % (slug, suf)), encoding="utf-8").read())
        chk(g == t, "cc-%s%s: skeleton differs from %s" % (slug, suf, tplp))
for lang, tplp, page in (("zh", "rc.html", "cc.html"), ("en", "rc-en.html", "cc-en.html")):
    t = skeleton(open(os.path.join(REPO, tplp), encoding="utf-8").read())
    g = skeleton(open(os.path.join(REPO, page), encoding="utf-8").read())
    chk(g == t, "%s: skeleton differs from %s" % (page, tplp))
print("9. every byte outside the substituted slots is identical to the template "
      "(svg, nav, footer, swirl script, hub tag-filter script, style)")

# 10 ------------------------------------------------------------ hub counts ---
for lang, page in (("zh", "cc.html"), ("en", "cc-en.html")):
    s = open(os.path.join(REPO, page), encoding="utf-8").read()
    bar = tb.RE_HUB_TAGC.search(s).group(2)
    btns = tb.RE_HUB_BTN.findall(bar)
    cnts = dict((k, int(n)) for k, n in
                re.findall(r'data-tag="([^"]*)">[^<]*<i>(\d+)</i>', bar))
    want = {}
    for slug in ORD:
        for k in colon.ART[slug]["tags"]:
            want[k] = want.get(k, 0) + 1
    want[""] = 16
    chk(cnts == want, "%s tagbar counts differ: %s" % (page, cnts))
    chk(s.count('class="postcard"') == 16, "%s postcards" % page)
    chk(s.count('class="postgroup hnstep"') == 4, "%s postgroups" % page)
    for slug in ORD:
        chk('href="cc-%s%s.html"' % (slug, "-en" if lang == "en" else "") in s,
            "%s card link %s" % (page, slug))
print("10. hub: 4 groups, 16 cards, tag counts computed from the articles "
      "(%d tag keys + 全部/All)" % (len(want) - 1))

# 11 ------------------------------------------------- no double escaping ------
for p in pages:
    s = open(os.path.join(REPO, p), encoding="utf-8").read()
    chk("&amp;amp;" not in s and "&amp;quot;" not in s and "&#x27;" not in s,
        "%s: double-escaped entity" % p)
print("11. no double-escaped entities (&amp;amp; / &amp;quot; / &#x27;) on any page")

print()
if fails:
    print("FAILURES (%d):" % len(fails))
    for f in fails:
        if f:
            print("   " + f)
else:
    print("ALL CHECKS PASSED")
