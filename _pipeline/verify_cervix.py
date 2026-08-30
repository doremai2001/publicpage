# -*- coding: utf-8 -*-
"""Verification pass over the generated cervical-cancer pages."""
import difflib, filecmp, html, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cervix, topicbuild as tb

REPO = "/home/claude/repo"
UPLOAD = "/home/claude/upload-cervix"
PRE = ("/tmp/claude-0/-home-claude/4bc50b06-d4e4-5989-80b2-34f0f02eed26/"
       "scratchpad/prebackup-cx")
CX = "/home/claude/cervix"
ORD = [s for sec in cervix.SECTIONS for s in sec["slugs"]]
ART_TPL = {"zh": "cc-first-month.html", "en": "cc-first-month-en.html"}
HUB_TPL = {"zh": "cc.html", "en": "cc-en.html"}
fails = []

def chk(ok, msg):
    if not ok:
        fails.append(msg)

def rd(*p):
    return open(os.path.join(*p), encoding="utf-8").read()

def esca(s):
    return html.escape(s, quote=False).replace('"', "&quot;")

hubs = ["cx.html", "cx-en.html"]
arts = ["cx-%s.html" % s for s in ORD] + ["cx-%s-en.html" % s for s in ORD]
pages = hubs + arts
svgs = sorted(n for n in os.listdir(os.path.join(CX, "figs")) if n.endswith(".svg"))

# 1 --------------------------------------- page count + sitemap, both ways ---
chk(len(pages) == 34, "page count %d" % len(pages))
for p in pages:
    chk(os.path.exists(os.path.join(REPO, p)), "missing %s" % p)
    chk(os.path.exists(os.path.join(UPLOAD, p)), "missing from upload dir: %s" % p)
for n in svgs + ["topics.html", "topics-en.html", "sitemap.xml"]:
    chk(os.path.exists(os.path.join(UPLOAD, n)), "upload missing %s" % n)
chk(len(os.listdir(UPLOAD)) == 57, "upload dir has %d files" % len(os.listdir(UPLOAD)))
sm = rd(REPO, "sitemap.xml")
pre_sm = rd(PRE, "sitemap.xml")
chk(sm.count("<url>") == pre_sm.count("<url>") + 34,
    "sitemap count %d (was %d)" % (sm.count("<url>"), pre_sm.count("<url>")))
for p in pages:
    chk(("<loc>%s%s</loc>" % (tb.BASE, p)) in sm, "sitemap missing %s" % p)
for p, prio in ([("cx.html", "0.85"), ("cx-en.html", "0.75")]
                + [("cx-%s.html" % s, "0.75") for s in ORD]
                + [("cx-%s-en.html" % s, "0.65") for s in ORD]):
    ln = [l for l in sm.splitlines() if "<loc>%s%s</loc>" % (tb.BASE, p) in l][0]
    chk("<lastmod>%s</lastmod>" % cervix.DATE in ln, "%s lastmod" % p)
    chk("<priority>%s</priority>" % prio in ln, "%s priority" % p)
# existing entries and their order untouched
kept = [l for l in sm.splitlines()
        if not re.search(r"<loc>%scx(-|\.)" % re.escape(tb.BASE), l)]
chk(kept == pre_sm.splitlines(), "existing sitemap lines changed or reordered")
chk("cx-cx-" not in sm and not any("cx-cx-" in n for n in os.listdir(REPO)),
    "double-prefixed name somewhere")
# the cx block sits right after the nt block, before bc.html
sml = sm.splitlines()
i_nt = [i for i, l in enumerate(sml) if "<loc>%snt-bnct-en.html</loc>" % tb.BASE in l][0]
chk("<loc>%scx.html</loc>" % tb.BASE in sml[i_nt + 1], "cx block not after nt block")
chk("<loc>%sbc.html</loc>" % tb.BASE in sml[i_nt + 35], "cx block not before bc block")
# full file <-> sitemap diff, both directions
sm_names = set(m.group(1) for m in
               re.finditer(re.escape(tb.BASE) + r"([^<]*)</loc>", sm))
repo_html = set(n for n in os.listdir(REPO) if n.endswith(".html"))
in_sm_not_repo = sorted(n for n in sm_names if n.endswith(".html")
                        and n not in repo_html)
in_repo_not_sm = sorted(n for n in repo_html if n not in sm_names)
pre_names = set(m.group(1) for m in
                re.finditer(re.escape(tb.BASE) + r"([^<]*)</loc>", pre_sm))
pre_not_sm = sorted(n for n in repo_html if not n.startswith("cx")
                    and n not in pre_names)
chk(in_sm_not_repo == [], "sitemap urls without a file: %s" % in_sm_not_repo)
chk(in_repo_not_sm == pre_not_sm,
    "repo html not in sitemap changed: %s (was %s)" % (in_repo_not_sm, pre_not_sm))
chk(all(p in sm_names for p in pages), "a cx page missing from sitemap")
print("1. 34 pages (32 articles + 2 hubs) exist in repo and upload dir; upload dir = "
      "%d files (34 pages + %d svgs + topics x2 + sitemap); sitemap <url> = %d "
      "(was %d, +34), priorities 0.85/0.75 hub and 0.75/0.65 articles, lastmod %s; "
      "cx block sits between the nt and bc blocks; all pre-existing lines "
      "byte-unchanged and in order; full file<->sitemap diff both ways: every "
      "sitemap URL has a file, files-not-in-sitemap unchanged from before the "
      "build (%s)"
      % (len(os.listdir(UPLOAD)), len(svgs), sm.count("<url>"),
         pre_sm.count("<url>"), cervix.DATE, in_repo_not_sm or "none"))

# 2 --------------------------------------------- link scan incl. figure svg --
files = set(os.listdir(REPO))
bad, nlinks, nimg = [], 0, 0
for name in sorted(files):
    if name.endswith(".html"):
        s = rd(REPO, name)
        for t in re.findall(r'href="([^":]+\.html)(?:[#?][^"]*)?"', s):
            nlinks += 1
            if t not in files:
                bad.append((name, t))
        for t in re.findall(r'(?:src|srcset)="([^"]+\.svg)"', s):
            nimg += 1
            if t not in files:
                bad.append((name, t))
chk(not bad, "broken links: %s" % bad[:10])
print("2. %d internal .html links and %d svg src/srcset references across the repo: "
      "%d unresolved %s" % (nlinks, nimg, len(bad), bad[:10] if bad else ""))

# 3 ------------- citation / h4 / reference symmetry vs the ORIGINAL sources --
rows = []
for slug in ORD:
    fr = {}
    for lang, d in (("zh", os.path.join(CX, "body")), ("en", os.path.join(CX, "en"))):
        src = rd(d, "cx-%s.html" % slug)          # original, figure-free source
        body, items, n = tb.split_fragment(src)
        page = rd(REPO, "cx-%s%s.html" % (slug, "-en" if lang == "en" else ""))
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
        # page body minus its <figure> blocks == original source body
        pb_nofig = re.sub(r'\n?<figure class="article-figure">.*?</figure>\n?',
                          "\n", pb, flags=re.S)
        chk(re.sub(r"\s+", " ", pb_nofig).strip()
            == re.sub(r"\s+", " ", body).strip(),
            "%s %s body text differs from source outside figures" % (slug, lang))
    chk(fr["zh"][:3] == fr["en"][:3],
        "%s zh/en mismatch %s %s" % (slug, fr["zh"], fr["en"]))
    rows.append((slug, fr["zh"][0], fr["zh"][1], fr["zh"][2]))
print("3. citations / <h4> / references, page == original source and zh == en; "
      "body text outside the figure blocks byte-equivalent to source:")
for r in rows:
    print("     %-16s cit=%-3d h4=%-2d refs=%d" % r)

# 3b ------------------------------------------- figures per manifest used_by --
manifest = json.load(open(os.path.join(CX, "figs", "manifest.json"), encoding="utf-8"))
per = {}
for fig in manifest:
    for u in fig["used_by"]:
        per.setdefault(u, []).append(fig)
nfig_checked = 0
for slug in ORD:
    want = per.get("cx-" + slug, [])
    for lang, suf in (("zh", ""), ("en", "-en")):
        s = rd(REPO, "cx-%s%s.html" % (slug, suf))
        figs = re.findall(
            r'<figure class="article-figure">\s*<picture>\s*'
            r'<source media="\(max-width:620px\)" srcset="([^"]+)">\s*'
            r'<img src="([^"]+)" width="1440" height="(\d+)" loading="lazy" '
            r'decoding="async" alt="([^"]*)">\s*</picture>\s*'
            r'<figcaption>(.*?)</figcaption>\s*</figure>', s, re.S)
        chk(len(figs) == len(want), "cx-%s%s: %d figures, want %d"
            % (slug, suf, len(figs), len(want)))
        for got, fig in zip(figs, want):
            f = fig["files"]
            mob = f["mobile"] if lang == "zh" else f["en_mobile"]
            dsk = f["desktop"] if lang == "zh" else f["en"]
            alt = esca(fig["zh_alt"] if lang == "zh" else fig["en_alt"])
            cap = fig["zh_caption"] if lang == "zh" else fig["en_caption"]
            vb = re.search(r'viewBox="0 0 1440 (\d+)"', rd(CX, "figs", dsk)).group(1)
            chk(got[0] == mob, "cx-%s%s srcset %s" % (slug, suf, got[0]))
            chk(got[1] == dsk, "cx-%s%s src %s" % (slug, suf, got[1]))
            chk(got[2] == vb, "cx-%s%s height %s != viewBox %s" % (slug, suf, got[2], vb))
            chk(got[3] == alt, "cx-%s%s alt differs" % (slug, suf))
            chk(got[4] == cap, "cx-%s%s caption differs" % (slug, suf))
            nfig_checked += 1
    # zh placement audit once per slug: figure after <h4> #2
    s = rd(REPO, "cx-%s.html" % slug)
    body = re.search(r'<div class="body-html">\n(.*?)\n    </div>', s, re.S).group(1)
    pos = []
    h4 = 0
    for m in re.finditer(r'<h4>|<figure class="article-figure">', body):
        if m.group(0) == "<h4>":
            h4 += 1
        else:
            pos.append(h4)
    if per.get("cx-" + slug):
        chk(pos == [2], "cx-%s figure placement %s" % (slug, pos))
    else:
        chk(pos == [], "cx-%s unexpected figure %s" % (slug, pos))
print("3b. %d figure instances match the manifest (files per language, alt "
      "attribute-escaped, caption, height = desktop viewBox); placement: every "
      "figure after <h4> #2, no exceptions" % nfig_checked)
for n in svgs:
    chk(filecmp.cmp(os.path.join(CX, "figs", n), os.path.join(REPO, n),
                    shallow=False), "svg differs in repo: %s" % n)

# 4 -------------------------- style = template + injected figure CSS, stable --
hh = rd(REPO, "hn-first-week.html")
a = hh.index("/* ---------- article figures ---------- */")
b = hh.index("/* ----------", a + 10)
BLOCK = hh[a:b]
tpl_style = tb.RE_STYLE.search(rd(REPO, ART_TPL["zh"])).group(0)
for f in (ART_TPL["en"], HUB_TPL["zh"], HUB_TPL["en"]):
    chk(tb.RE_STYLE.search(rd(REPO, f)).group(0) == tpl_style,
        "%s template style differs" % f)
i = tpl_style.index("</style>")
# The cc template now carries the figure css itself (the site owner added it),
# so generated pages simply keep the template style unchanged.
WANT_STYLE = tpl_style if ".article-figure{" in tpl_style else tpl_style[:i] + BLOCK + tpl_style[i:]
seen = set()
for p in pages:
    s = rd(REPO, p)
    for tag in ("<style>", "</style>", "<body>", "</body>", "</html>",
                "<head>", "</head>"):
        chk(s.count(tag) == 1, "%s: %s x%d" % (p, tag, s.count(tag)))
    st = tb.RE_STYLE.search(s).group(0)
    chk(st == WANT_STYLE, "%s: style != template + figure css" % p)
    seen.add(st)
chk(len(seen) == 1, "style not byte-stable across the 34")
chk(BLOCK.startswith("/* ---------- article figures ---------- */")
    and BLOCK.count(".article-figure") == 9, "figure css block looks wrong")
print("4. <style> on all 34 pages is byte-identical (%d bytes) and equals the shared "
      "template style (%d bytes) + the article-figure block copied verbatim from "
      "hn-first-week.html (%d bytes); head/body tags exactly once each"
      % (len(WANT_STYLE), len(tpl_style), len(BLOCK)))

# 5 ------------------------------------------------------------- hreflang ----
npair = 0
for slug in ORD + [None]:
    z = "cx.html" if slug is None else "cx-%s.html" % slug
    e = "cx-en.html" if slug is None else "cx-%s-en.html" % slug
    npair += 1
    for p, other in ((z, e), (e, z)):
        s = rd(REPO, p)
        chk('<link rel="alternate" hreflang="zh-Hant" href="%s%s">' % (tb.BASE, z) in s,
            "%s hreflang zh" % p)
        chk('<link rel="alternate" hreflang="en" href="%s%s">' % (tb.BASE, e) in s,
            "%s hreflang en" % p)
        chk('<link rel="alternate" hreflang="x-default" href="%s%s">' % (tb.BASE, z) in s,
            "%s hreflang x-default" % p)
        chk('<link rel="canonical" href="%s%s">' % (tb.BASE, p) in s, "%s canonical" % p)
        chk('href="%s" hreflang=' % other in s, "%s lang switch -> %s" % (p, other))
print("5. hreflang zh-Hant/en/x-default + canonical + nav language switch, both "
      "directions, on all %d pairs (16 articles + the hub)" % npair)

# 6 ------------------------------------------------- topics.html diff --------
for f, card, hp in (("topics.html", cervix.TOPIC_CARD_ZH, cervix.HASPART_ZH),
                    ("topics-en.html", cervix.TOPIC_CARD_EN, cervix.HASPART_EN)):
    a = rd(PRE, f).splitlines(True)
    b = rd(REPO, f).splitlines(True)
    d = list(difflib.unified_diff(a, b, n=0))
    added = [l[1:] for l in d if l.startswith("+") and not l.startswith("+++")]
    removed = [l[1:] for l in d if l.startswith("-") and not l.startswith("---")]
    entry = "," + json.dumps(hp, ensure_ascii=False, separators=(",", ":"))
    chk(len(removed) == 1 and '"hasPart":[' in removed[0], "%s removed lines" % f)
    ld_new = [l for l in added if '"hasPart":[' in l]
    chk(len(ld_new) == 1 and removed[0].count("}]}</script>") == 1
        and ld_new[0] == removed[0].replace("}]}</script>",
                                            "}%s]}</script>" % entry),
        "%s json-ld line not just extended" % f)
    rest = [l for l in added if '"hasPart":[' not in l]
    chk("".join(rest) == card, "%s: added text is not exactly the card" % f)
    s = "".join(b)
    n = 7
    chk(s.count('class="topiccard"') == n, "%s: %d cards" % (f, s.count('class="topiccard"')))
    grid = re.search(r'<div class="topicgrid">(.*?)\n  </div>', s, re.S).group(1)
    chk(grid.count('class="topiccard"') == n, "%s cards not all inside grid" % f)
    chk(".topicgrid{display:grid;grid-template-columns:1fr 1fr;" in s,
        "%s grid columns changed" % f)
    cards = re.findall(r'<a class="topiccard" href="([^"]+)"', grid)
    chk(cards[-1] == ("cx.html" if f == "topics.html" else "cx-en.html")
        and cards[-2].startswith("lc"), "%s card order %s" % (f, cards))
    ld = json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>',
                              s, re.S).group(1))
    chk([e["url"] for e in ld["hasPart"]][-1].endswith(cards[-1]),
        "%s hasPart last entry" % f)
    chk(len(ld["hasPart"]) == 7, "%s hasPart %d" % (f, len(ld["hasPart"])))
    print("6. %-15s differs from the pulled version ONLY by the cx card (after the "
          "lung card, %d lines) and the hasPart entry; 7 cards in the 2-column "
          "grid; hasPart = 7 hubs ending with cx" % (f, len(rest)))

# 7 ------------------------------------------------------------- hub render ---
for lang, page in (("zh", "cx.html"), ("en", "cx-en.html")):
    s = rd(REPO, page)
    bar = tb.RE_HUB_TAGC.search(s).group(2)
    cnts = dict((k, int(n)) for k, n in
                re.findall(r'data-tag="([^"]*)">[^<]*<i>(\d+)</i>', bar))
    want = {}
    for slug in ORD:
        for k in cervix.ART[slug]["tags"]:
            want[k] = want.get(k, 0) + 1
    want[""] = 16
    chk(cnts == want, "%s tagbar counts differ: %s" % (page, cnts))
    cards = re.findall(r'<a class="postcard" data-tags="([^"]*)" href="([^"]*)"', s)
    chk(len(cards) == 16, "%s: %d postcards" % (page, len(cards)))
    dom = {}
    for tags, _ in cards:
        for k in tags.split():
            dom[k] = dom.get(k, 0) + 1
    chk(dom == {k: v for k, v in cnts.items() if k},
        "%s: tagbar counts != card counts" % page)
    grp = re.findall(r'<div class="postgroup hnstep">.*?\n  </div>', s, re.S)
    chk(len(grp) == 4, "%s: %d postgroups" % (page, len(grp)))
    chk(all(g.count('class="postcard"') == 4 for g in grp), "%s group sizes" % page)
    for i, slug in enumerate(ORD):
        chk(cards[i][1] == "cx-%s%s.html" % (slug, "-en" if lang == "en" else ""),
            "%s card %d order" % (page, i))
    for i in (1, 2, 3, 4):
        chk(s.count("<h3><b>%d</b>" % i) == 1, "%s section heading %d" % (page, i))
    chk("<h3><b>5</b>" not in s, "%s extra section heading" % page)
    ld = json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>',
                              s, re.S).group(1))
    chk(len(ld["hasPart"]) == 16, "%s hasPart %d" % (page, len(ld["hasPart"])))
    # new tag labels rendered with the agreed zh/en labels
    lab = cervix.LABEL_ADD
    li = 0 if lang == "zh" else 1
    for k in lab:
        want_btn = 'data-tag="%s">#%s <i>' % (k, html.escape(lab[k][li], quote=False))
        chk(want_btn in bar, "%s new label %s not rendered as %r" % (page, k, want_btn))
print("7. hub: 4 groups x 4 cards in reading order; 全部/All button = 16; "
      "%d per-tag counts each equal the number of cards carrying that tag; "
      "JSON-LD hasPart lists 16; new labels brachy/hpv/menopause rendered "
      "as agreed in both languages" % (len(want) - 1))

# 8 --------------------------------------------------- ld / nav / dates -------
for p in pages:
    s = rd(REPO, p)
    en = p.endswith("-en.html")
    chk(('<a href="topics-en.html" class="on">' if en
         else '<a href="topics.html" class="on">') in s, "%s nav active" % p)
    ld = json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>',
                              s, re.S).group(1))
    chk(ld["about"]["@type"] == "MedicalCondition", "%s about type" % p)
    chk(ld["about"]["name"] == ("Cervical cancer" if en else "子宮頸癌"),
        "%s about.name=%s" % (p, ld["about"]["name"]))
    chk(ld["inLanguage"] == ("en" if en else "zh-Hant"), "%s inLanguage" % p)
    if ld["@type"] == "MedicalWebPage":
        chk(ld["datePublished"] == "2026-08-30" and ld["dateModified"] == "2026-08-30",
            "%s dates" % p)
print("8. nav active state per language; JSON-LD about = MedicalCondition "
      "(子宮頸癌 / Cervical cancer) on all 34; datePublished = dateModified = "
      "2026-08-30 on all 32 articles")

# 9 -------------------------------------------------------------- pnav chain --
for lang, suf in (("zh", ""), ("en", "-en")):
    for i, slug in enumerate(ORD):
        s = rd(REPO, "cx-%s%s.html" % (slug, suf))
        pn = re.search(r'<div class="pnav">(.*?)</div>', s, re.S).group(1)
        if i == 0:
            chk(pn.startswith("<span></span>"), "%s%s first has prev" % (slug, suf))
        else:
            chk('class="pv" href="cx-%s%s.html"' % (ORD[i - 1], suf) in pn,
                "%s%s prev" % (slug, suf))
        if i == len(ORD) - 1:
            chk(pn.endswith("<span></span>"), "%s%s last has next" % (slug, suf))
        else:
            chk('class="nx" href="cx-%s%s.html"' % (ORD[i + 1], suf) in pn,
                "%s%s next" % (slug, suf))
print("9. pnav chains all 16 in reading order, both languages; ends use <span></span>")

# 10 ------------------------ everything outside the slots is intact -----------
def skeleton(s):
    s = tb.RE_TITLE.sub("@", s); s = tb.RE_DESC.sub("@", s)
    s = tb.RE_OGT.sub("@", s); s = tb.RE_OGD.sub("@", s); s = tb.RE_OGU.sub("@", s)
    s = tb.RE_CANON.sub("@", s); s = tb.RE_ALTS.sub("@", s); s = tb.RE_LD.sub("@", s)
    s = tb.RE_LANG.sub("@", s)
    s = tb.RE_STYLE.sub("@", s)
    s = re.sub(r'(<div class="article">).*?(\n  </div>\n</section>)', r"\1@\2",
               s, flags=re.S)
    s = re.sub(r'<section class="band narrow">.*?\n</section>', "@", s, flags=re.S)
    return s

for lang, suf in (("zh", ""), ("en", "-en")):
    t = skeleton(rd(REPO, ART_TPL[lang]))
    for slug in ORD:
        g = skeleton(rd(REPO, "cx-%s%s.html" % (slug, suf)))
        chk(g == t, "cx-%s%s: skeleton differs from %s" % (slug, suf, ART_TPL[lang]))
for lang, page in (("zh", "cx.html"), ("en", "cx-en.html")):
    t = skeleton(rd(REPO, HUB_TPL[lang]))
    g = skeleton(rd(REPO, page))
    chk(g == t, "%s: skeleton differs from %s" % (page, HUB_TPL[lang]))
print("10. every byte outside the substituted slots (and the style injection, "
      "checked in 4) is identical to the template")

# 11 ------------------------------------------------- no double escaping ------
for p in pages:
    s = rd(REPO, p)
    chk("&amp;amp;" not in s and "&amp;quot;" not in s and "&#x27;" not in s
        and "&amp;gt;" not in s, "%s: double-escaped entity" % p)
print("11. no double-escaped entities on any page")

# 12 ------------------------------------------------- upload dir is a mirror --
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
            print("   " + str(f))
    sys.exit(1)
print("ALL CHECKS PASSED")
