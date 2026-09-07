# -*- coding: utf-8 -*-
"""Verification pass over the generated glioblastoma pages.

The cervix / liver / pel / esoph standard, printed as one PASS/FAIL line per
check:

  1  body text == source fragment byte-for-byte once the inserted <figure>
     blocks are stripped (zh and en, all 17)
  2  reference list == source <ol> item by item; meta N == count; [n]
     markers run 1..N in first-use order
  3  figure position per manifest after_h4 (same section index in en)
  4  figure files / alt / caption / height per manifest, escaped exactly once
  5  hreflang zh-Hant / en / x-default + canonical, both directions
  6  language switch chip points at the partner page, both directions
  7  JSON-LD parses on every page; about / name / url / inLanguage / dates
  8  topics.html and topics-en.html differ from prebackup by exactly one
     card (after the ec card) and one appended hasPart entry
  9  sitemap differs from prebackup by exactly the new contiguous block
     (after ec-recurrence-en.html, before carc.html), 600 -> 636, priorities
 10  pages produced (36) == sitemap URLs added; every page in the sitemap
 11  every internal .html link and svg src/srcset in the repo resolves; the
     32 SVGs are byte-identical to /home/claude/gbm/figs
 12  the disclosure paragraph sits before the first <h4> of exactly
     gb-surgery / gb-standard / gb-numbers / gb-newthings, byte-identical
     across the four (zh == SPEC.md section 二, en == SPEC-EN.md section 1),
     and appears in no other article
 13  h1 / <title> / og:title / description / ld headline == meta title & dek;
     hub card titles == meta titles; hub tag counts consistent
 14  every byte outside the substituted slots equals the cc template; style
     identical across the 36 pages; no double-escaped entities
 15  upload dir == exactly the produced files, byte-identical to the repo
 16  git status shows only the expected new files and the three shared
     modifications

The hub is gbm.html / gbm-en.html while the articles are gb-*; gbm.py
overrides topicbuild._hub_name at import time, so importing gbm here gives
the verifier exactly the names the builder used.
"""
import decimal
import difflib
import filecmp
import html
import json
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gbm
import topicbuild as tb

REPO = "/home/claude/repo"
UPLOAD = "/home/claude/upload-gbm"
PRE = "/home/claude/gbm/prebackup"
GB = "/home/claude/gbm"
NART = 17
NFIG = 8
NSVG = 32
GROUPS = [5, 5, 4, 3]
ORD = [s for sec in gbm.SECTIONS for s in sec["slugs"]]
LANGS = [("zh", ""), ("en", "-en")]
ART_TPL = {"zh": "cc-first-month.html", "en": "cc-first-month-en.html"}
HUB_TPL = {"zh": "cc.html", "en": "cc-en.html"}
HUB_ZH = gbm.HUB_NAME["zh"]
HUB_EN_NAME = gbm.HUB_NAME["en"]
SM_PREV = "ec-recurrence-en.html"
SM_NEXT = "carc.html"
PREV_CARD = {"zh": "ec.html", "en": "ec-en.html"}
NCARD = 12
PRE_URLS = 600
NEW_URLS = PRE_URLS + 2 + 2 * NART
DISC_ARTS = ["surgery", "standard", "numbers", "newthings"]
ANCHOR = {"zh": "先說我的位置", "en": "My position first"}
NEW_PIPELINE = ["build_gbm.py", "gbm.py", "gbm_en.py",
                "stage_gbm_figs.py", "verify_gbm.py"]

hubs = [HUB_ZH, HUB_EN_NAME]
arts = ["gb-%s%s.html" % (s, suf) for _, suf in LANGS for s in ORD]
pages = hubs + arts
svgs = sorted(n for n in os.listdir(os.path.join(GB, "figs"))
              if n.endswith(".svg"))
manifest = json.load(open(os.path.join(GB, "figs", "manifest.json"),
                          encoding="utf-8"))

results = []
_cur = []


def chk(ok, msg):
    if not ok:
        _cur.append(msg)


def report(no, label):
    global _cur
    ok = not _cur
    results.append((no, label, ok, list(_cur)))
    print("%-4s %s -- %s" % ("PASS" if ok else "FAIL", "%2d." % no, label))
    for m in _cur[:12]:
        print("        " + str(m))
    if len(_cur) > 12:
        print("        ... %d more" % (len(_cur) - 12))
    _cur = []


def rd(*p):
    return open(os.path.join(*p), encoding="utf-8").read()


def esca(s):
    return html.escape(s, quote=False).replace('"', "&quot;")


def src_path(slug, lang):
    return os.path.join(GB, "body" if lang == "zh" else "en",
                        "gb-%s%s.html" % (slug, "" if lang == "zh" else "-en"))


def hub_of(lang):
    return HUB_ZH if lang == "zh" else HUB_EN_NAME


def page_body(s):
    return re.search(r'<div class="body-html">\n(.*?)\n    </div>', s,
                     re.S).group(1)


def page_refs(s):
    return re.search(r'<div class="refs">.*?<ol>(.*?)</ol>', s, re.S).group(1)


def ld_of(s):
    return json.loads(re.search(
        r'<script type="application/ld\+json">(.*?)</script>', s,
        re.S).group(1))


RE_FIG = re.compile(
    r'<figure class="article-figure">\s*<picture>\s*'
    r'<source media="\(max-width:620px\)" srcset="([^"]+)">\s*'
    r'<img src="([^"]+)" width="1440" height="(\d+)" loading="lazy" '
    r'decoding="async" alt="([^"]*)">\s*</picture>\s*'
    r'<figcaption>(.*?)</figcaption>\s*</figure>', re.S)
RE_FIG_STRIP = re.compile(
    r'\n?<figure class="article-figure">.*?</figure>\n?', re.S)


def vb_height(svg_name):
    m = re.search(r'viewBox="0 0 (\d+(?:\.\d+)?) (\d+(?:\.\d+)?)"',
                  rd(GB, "figs", svg_name))
    assert m and m.group(1) == "1440", svg_name
    return str(int(decimal.Decimal(m.group(2)).quantize(
        decimal.Decimal("1"), rounding=decimal.ROUND_HALF_UP)))


for p in pages:
    if not os.path.exists(os.path.join(REPO, p)):
        print("FATAL: missing %s" % p)
        sys.exit(2)

# 1 ------------------------------------------ body == source minus figures --
for slug in ORD:
    for lang, suf in LANGS:
        body, items, n = tb.split_fragment(rd(src_path(slug, lang)))
        pb = page_body(rd(REPO, "gb-%s%s.html" % (slug, suf)))
        nofig = RE_FIG_STRIP.sub("\n", pb)
        # the figure sits between two sections; stripping it may leave a
        # collapsed blank line, so compare after normalising the separator
        chk(re.sub(r"\n{2,}", "\n\n", nofig).strip()
            == re.sub(r"\n{2,}", "\n\n", body).strip(),
            "gb-%s%s body differs from source outside the figure block"
            % (slug, suf))
        chk("<hr>" not in pb, "gb-%s%s: <hr> leaked into body" % (slug, suf))
        chk(len(re.findall(r"<h4>", pb)) == len(re.findall(r"<h4>", body)),
            "gb-%s%s: h4 count" % (slug, suf))
        chk(len(re.findall(r'<sup class="cit">', pb))
            == len(re.findall(r'<sup class="cit">', body)),
            "gb-%s%s: citation count" % (slug, suf))
report(1, "body-html == source fragment byte-for-byte after stripping the "
          "inserted <figure> (17 zh + 17 en); <hr> never leaks; h4 and "
          "citation counts equal")

# 2 ------------------------------------------------- references item by item --
for slug in ORD:
    for lang, suf in LANGS:
        body, items, n = tb.split_fragment(rd(src_path(slug, lang)))
        page = rd(REPO, "gb-%s%s.html" % (slug, suf))
        pr = page_refs(page)
        chk(pr == items, "gb-%s%s: reference <ol> content differs from source"
            % (slug, suf))
        src_li = re.findall(r"<li>.*?</li>", items, re.S)
        page_li = re.findall(r"<li>.*?</li>", pr, re.S)
        chk(len(src_li) == len(page_li) == n,
            "gb-%s%s: %d/%d/%d reference items" % (slug, suf, len(src_li),
                                                   len(page_li), n))
        for k, (a, b) in enumerate(zip(src_li, page_li)):
            chk(a == b, "gb-%s%s: reference %d differs" % (slug, suf, k + 1))
        chk("<ol>" not in pr and "<p></p>" not in pr,
            "gb-%s%s: nested <ol> or trailing empty <p>" % (slug, suf))
        mm = re.search(r'<div class="meta">(.*?)</div>', page).group(1)
        chk(int(re.search(r"\d+", mm.split(" · ")[2]).group(0)) == n,
            "gb-%s%s: meta reference count != %d" % (slug, suf, n))
        nums = [int(x) for x in
                re.findall(r'<sup class="cit">\[(\d+)\]</sup>', page_body(page))]
        first = [v for i, v in enumerate(nums) if v not in nums[:i]]
        chk(first == list(range(1, n + 1)),
            "gb-%s%s: [n] markers not 1..%d in first-use order" % (slug, suf, n))
    zn = tb.split_fragment(rd(src_path(slug, "zh")))[2]
    en_ = tb.split_fragment(rd(src_path(slug, "en")))[2]
    chk(zn == en_, "gb-%s: zh %d refs vs en %d" % (slug, zn, en_))
report(2, "reference list == source <ol> item by item on all 34 pages; meta "
          "N == count; [n] markers run 1..N in first-use order; zh == en "
          "reference counts")

# 3 ------------------------------------------------ figure placement ---------
per = {}
for fig in manifest:
    art = fig["placement"]["article"]
    chk(art in fig["used_by"], "%s: placement article not in used_by" % fig["id"])
    chk(len(fig["used_by"]) == 1, "%s: used_by lists more than one article"
        % fig["id"])
    per.setdefault(art, []).append(fig)
chk(len(manifest) == NFIG, "manifest has %d figures, want %d"
    % (len(manifest), NFIG))
nfig = 0
alt_pairs = []
for slug in ORD:
    want = per.get("gb-" + slug, [])
    src_h4 = re.findall(r"<h4>(.*?)</h4>", rd(src_path(slug, "zh")))
    want_pos = []
    for f in want:
        chk(f["placement"]["after_h4"] in src_h4,
            "%s: after_h4 not found in gb-%s" % (f["id"], slug))
        if f["placement"]["after_h4"] in src_h4:
            want_pos.append(src_h4.index(f["placement"]["after_h4"]) + 1)
    for lang, suf in LANGS:
        body = page_body(rd(REPO, "gb-%s%s.html" % (slug, suf)))
        figs = RE_FIG.findall(body)
        chk(len(figs) == len(want), "gb-%s%s: %d figures, want %d"
            % (slug, suf, len(figs), len(want)))
        pos, h4 = [], 0
        for m in re.finditer(r'<h4>|<figure class="article-figure">', body):
            if m.group(0) == "<h4>":
                h4 += 1
            else:
                pos.append(h4)
        chk(pos == want_pos, "gb-%s%s: figure after h4 #%s, want #%s"
            % (slug, suf, pos, want_pos))
        # the figure closes its section: the next thing after it is an <h4>
        for m in re.finditer(r"</figure>\n+", body):
            chk(body[m.end():m.end() + 4] == "<h4>",
                "gb-%s%s: figure is not immediately followed by the next <h4>"
                % (slug, suf))
        for got, fig in zip(figs, want):
            alt_pairs.append((lang, slug, fig, got))
        nfig += len(figs)
chk(nfig == 2 * NFIG, "%d figure instances, want %d (%d x 2 languages)"
    % (nfig, 2 * NFIG, NFIG))
report(3, "%d manifest figures -> %d insertions per language, each closing "
          "the h4 section named by placement.after_h4 (same section index in "
          "en)" % (NFIG, NFIG))

# 4 ---------------------------------------- figure files / alt / caption -----
for lang, slug, fig, got in alt_pairs:
    f = fig["files"]
    mob = f["mobile"] if lang == "zh" else f["en_mobile"]
    dsk = f["desktop"] if lang == "zh" else f["en"]
    raw_alt = fig["zh_alt"] if lang == "zh" else fig["en_alt"]
    raw_cap = fig["zh_caption"] if lang == "zh" else fig["en_caption"]
    tag = "gb-%s (%s)" % (slug, lang)
    chk(got[0] == mob, "%s: srcset %s != %s" % (tag, got[0], mob))
    chk(got[1] == dsk, "%s: src %s != %s" % (tag, got[1], dsk))
    chk(got[2] == vb_height(dsk), "%s: height %s != viewBox %s"
        % (tag, got[2], vb_height(dsk)))
    chk(got[3] == esca(raw_alt), "%s: alt != escaped manifest alt" % tag)
    chk(html.unescape(got[3]) == raw_alt, "%s: alt does not round-trip" % tag)
    chk('"' not in got[3] and "<" not in got[3] and ">" not in got[3],
        "%s: raw quote/angle bracket in alt" % tag)
    chk(got[4] == raw_cap.replace("&", "&amp;").replace("<", "&lt;"),
        "%s: caption != escaped manifest caption" % tag)
    chk("&amp;amp;" not in got[3] + got[4] and "&amp;lt;" not in got[3] + got[4],
        "%s: double-escaped alt/caption" % tag)
report(4, "all %d figure instances: mobile/desktop files per language, height "
          "= desktop viewBox, alt attribute-escaped once, caption "
          "text-escaped once, all equal to the manifest" % (2 * NFIG))

# 5 ----------------------------------------------------------- hreflang -------
for slug in ORD + [None]:
    z = HUB_ZH if slug is None else "gb-%s.html" % slug
    en = HUB_EN_NAME if slug is None else "gb-%s-en.html" % slug
    for p in (z, en):
        s = rd(REPO, p)
        chk('<link rel="alternate" hreflang="zh-Hant" href="%s%s">'
            % (tb.BASE, z) in s, "%s hreflang zh-Hant" % p)
        chk('<link rel="alternate" hreflang="en" href="%s%s">'
            % (tb.BASE, en) in s, "%s hreflang en" % p)
        chk('<link rel="alternate" hreflang="x-default" href="%s%s">'
            % (tb.BASE, z) in s, "%s hreflang x-default" % p)
        chk('<link rel="canonical" href="%s%s">' % (tb.BASE, p) in s,
            "%s canonical" % p)
        chk(s.count('rel="alternate"') == 3, "%s alternate count" % p)
        chk(s.count('rel="canonical"') == 1, "%s canonical count" % p)
report(5, "hreflang zh-Hant / en / x-default + self-canonical on all 18 "
          "pairs, both directions")

# 6 -------------------------------------------------------- lang switch ------
for slug in ORD + [None]:
    z = HUB_ZH if slug is None else "gb-%s.html" % slug
    en = HUB_EN_NAME if slug is None else "gb-%s-en.html" % slug
    sz, se = rd(REPO, z), rd(REPO, en)
    chk('<div class="lang"><span class="on">中</span><a href="%s" '
        'hreflang="en">EN</a></div>' % en in sz, "%s lang switch -> %s" % (z, en))
    chk('<div class="lang"><a href="%s" hreflang="zh-Hant">中</a>'
        '<span class="on">EN</span></div>' % z in se,
        "%s lang switch -> %s" % (en, z))
    chk(sz.count('<div class="lang">') == 1 and se.count('<div class="lang">') == 1,
        "%s/%s lang chip count" % (z, en))
report(6, "language switch chip on every page points at its partner "
          "(zh -> -en, en -> zh), exactly one chip per page")

# 7 --------------------------------------------------------------- JSON-LD ---
for p in pages:
    s = rd(REPO, p)
    try:
        ld = ld_of(s)
    except Exception as e:      # noqa
        chk(False, "%s: JSON-LD does not parse (%s)" % (p, e))
        continue
    en = p.endswith("-en.html")
    chk(ld["@context"] == "https://schema.org", "%s @context" % p)
    chk(ld["url"] == tb.BASE + p, "%s ld url %s" % (p, ld["url"]))
    chk(ld["inLanguage"] == ("en" if en else "zh-Hant"), "%s inLanguage" % p)
    chk(ld["about"]["@type"] == "MedicalCondition", "%s about type" % p)
    chk(ld["about"]["name"] == (gbm.CONDITION_EN if en else gbm.CONDITION_ZH),
        "%s about.name %s" % (p, ld["about"]["name"]))
    chk(ld["author"]["@type"] == "Physician", "%s author" % p)
    if p in hubs:
        chk(ld["@type"] == "CollectionPage", "%s type" % p)
        chk(ld["name"] == (gbm.NAME_EN if en else gbm.NAME_ZH), "%s name" % p)
        chk([e["url"] for e in ld["hasPart"]]
            == [tb.BASE + "gb-%s%s.html" % (s_, "-en" if en else "")
                for s_ in ORD], "%s hasPart urls" % p)
        meta = gbm.EN if en else gbm.ART
        chk([e["name"] for e in ld["hasPart"]]
            == [meta[s_]["title"] for s_ in ORD], "%s hasPart names" % p)
    else:
        slug = p[len("gb-"):-len(".html")]
        if en:
            slug = slug[:-3]
        meta = (gbm.EN if en else gbm.ART)[slug]
        chk(ld["@type"] == "MedicalWebPage", "%s type" % p)
        chk(ld["headline"] == meta["title"], "%s headline" % p)
        chk(ld["description"] == meta["dek"], "%s description" % p)
        chk(ld["datePublished"] == gbm.DATE
            and ld["dateModified"] == gbm.DATE, "%s dates" % p)
    chk(s.count('<script type="application/ld+json">') == 1, "%s ld count" % p)
report(7, "JSON-LD parses on all 36 pages; @type / url / inLanguage / about = "
          "MedicalCondition %s|%s / headline / dates / hub hasPart all correct"
          % (gbm.CONDITION_ZH, gbm.CONDITION_EN))

# 8 ---------------------------------------------------- topics pages diff ---
for f, card, hp, href, prev_href in (
        ("topics.html", gbm.TOPIC_CARD_ZH, gbm.HASPART_ZH, HUB_ZH,
         PREV_CARD["zh"]),
        ("topics-en.html", gbm.TOPIC_CARD_EN, gbm.HASPART_EN, HUB_EN_NAME,
         PREV_CARD["en"])):
    pre, now = rd(PRE, f), rd(REPO, f)
    d = list(difflib.unified_diff(pre.splitlines(True), now.splitlines(True),
                                  n=0))
    added = [l[1:] for l in d if l.startswith("+") and not l.startswith("+++")]
    removed = [l[1:] for l in d if l.startswith("-") and not l.startswith("---")]
    entry = "," + json.dumps(hp, ensure_ascii=False, separators=(",", ":"))
    chk(len(removed) == 1 and '"hasPart":[' in removed[0],
        "%s: %d removed lines (want only the JSON-LD line)" % (f, len(removed)))
    ld_new = [l for l in added if '"hasPart":[' in l]
    chk(len(ld_new) == 1 and removed and
        ld_new[0] == removed[0].replace("}]}</script>", "}%s]}</script>" % entry),
        "%s: JSON-LD line not just extended by the gbm hasPart entry" % f)
    rest = [l for l in added if '"hasPart":[' not in l]
    chk("".join(rest) == card, "%s: added text is not exactly the gbm card" % f)
    grid = re.search(r'<div class="topicgrid">(.*?)\n  </div>', now, re.S).group(1)
    cards = re.findall(r'<a class="topiccard" href="([^"]+)"', grid)
    chk(len(cards) == NCARD and cards[-1] == href and cards[-2] == prev_href,
        "%s: card order %s" % (f, cards))
    chk(now.count('class="topiccard"') == pre.count('class="topiccard"') + 1,
        "%s: card count" % f)
    ld, pre_ld = ld_of(now), ld_of(pre)
    chk(ld["hasPart"][:-1] == pre_ld["hasPart"] and ld["hasPart"][-1] == hp,
        "%s: hasPart not old + gbm" % f)
    chk('<div class="k">%s</div>' % gbm.KICKER in card, "%s: card kicker" % f)
    chk('<span class="n">%d %s</span>' % (NART, "篇" if f == "topics.html"
                                          else "articles") in card,
        "%s: card count label" % f)
report(8, "topics.html and topics-en.html differ from prebackup by exactly "
          "the gbm card (after the ec card, %dth) and one appended hasPart "
          "entry; card says %s / %d" % (NCARD, gbm.KICKER, NART))

# 9 --------------------------------------------------------- sitemap diff ---
sm, pre_sm = rd(REPO, "sitemap.xml"), rd(PRE, "sitemap.xml")
RE_LOC = re.compile(re.escape(tb.BASE) + r"([^<]*)</loc>")
RE_GB = re.compile(r"<loc>%s(gbm\.html|gbm-en\.html|gb-)" % re.escape(tb.BASE))
sml = sm.splitlines()
gb_lines = [l for l in sml if RE_GB.search(l)]
kept = [l for l in sml if not RE_GB.search(l)]
chk(kept == pre_sm.splitlines(), "non-gb sitemap lines changed or reordered")
chk(not any(RE_GB.search(l) for l in pre_sm.splitlines()),
    "prebackup already had gb lines")
chk(pre_sm.count("<url>") == PRE_URLS, "prebackup <url> = %d, want %d"
    % (pre_sm.count("<url>"), PRE_URLS))
chk(sm.count("<url>") == NEW_URLS, "sitemap <url> = %d, want %d"
    % (sm.count("<url>"), NEW_URLS))
chk(len(gb_lines) == 2 + 2 * NART, "%d gb sitemap lines, want %d"
    % (len(gb_lines), 2 + 2 * NART))
want_order = ([HUB_ZH, HUB_EN_NAME] + ["gb-%s.html" % s for s in ORD]
              + ["gb-%s-en.html" % s for s in ORD])
chk([RE_LOC.search(l).group(1) for l in gb_lines] == want_order,
    "gb block order is not hub zh, hub en, 17 zh, 17 en")
prio = {HUB_ZH: "0.85", HUB_EN_NAME: "0.75"}
prio.update(("gb-%s.html" % s, "0.75") for s in ORD)
prio.update(("gb-%s-en.html" % s, "0.65") for s in ORD)
for l in gb_lines:
    n = RE_LOC.search(l).group(1)
    chk("<priority>%s</priority>" % prio[n] in l, "%s priority" % n)
    chk("<lastmod>%s</lastmod>" % gbm.DATE in l, "%s lastmod" % n)
    chk("<changefreq>monthly</changefreq>" in l, "%s changefreq" % n)
i_prev = [i for i, l in enumerate(sml)
          if "<loc>%s%s</loc>" % (tb.BASE, SM_PREV) in l]
chk(len(i_prev) == 1, "anchor %s not found once" % SM_PREV)
if i_prev:
    i = i_prev[0]
    nblk = 2 + 2 * NART
    chk(all(RE_GB.search(l) for l in sml[i + 1:i + 1 + nblk]),
        "gb block not contiguous right after %s" % SM_PREV)
    chk("<loc>%s%s</loc>" % (tb.BASE, SM_NEXT) in sml[i + 1 + nblk],
        "gb block not immediately before %s" % SM_NEXT)
chk("gb-gb-" not in sm and not any("gb-gb-" in n for n in os.listdir(REPO)),
    "double-prefixed name somewhere")
report(9, "sitemap differs from prebackup by exactly one contiguous %d-line "
          "block after %s / before %s; <url> %d -> %d; order hub zh, hub en, "
          "17 zh, 17 en; priorities 0.85/0.75/0.75/0.65; lastmod %s"
          % (2 + 2 * NART, SM_PREV, SM_NEXT, PRE_URLS, NEW_URLS, gbm.DATE))

# 10 ---------------------------------------------- pages == sitemap adds ----
sm_names = set(m.group(1) for m in RE_LOC.finditer(sm))
pre_names = set(m.group(1) for m in RE_LOC.finditer(pre_sm))
added_names = sm_names - pre_names
chk(len(pages) == 2 + 2 * NART, "%d pages, want %d"
    % (len(pages), 2 + 2 * NART))
chk(added_names == set(pages), "sitemap additions != produced pages: +%s -%s"
    % (sorted(added_names - set(pages)), sorted(set(pages) - added_names)))
chk(len(ORD) == NART and [len(s["slugs"]) for s in gbm.SECTIONS] == GROUPS,
    "reading order is not %d in %s" % (NART, "/".join(str(g) for g in GROUPS)))
repo_html = set(n for n in os.listdir(REPO) if n.endswith(".html"))
chk(all(n in repo_html for n in sm_names if n.endswith(".html")),
    "sitemap URL without a file: %s"
    % sorted(n for n in sm_names if n.endswith(".html") and n not in repo_html))
report(10, "36 pages produced (2 hubs + 17 zh + 17 en, groups %s) == the 36 "
           "sitemap URLs added; every sitemap URL has a file"
           % "/".join(str(g) for g in GROUPS))

# 11 ------------------------------------------------------ internal links ---
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
# gb pages specifically: every href / svg resolves and svgs match the source
for p in pages:
    s = rd(REPO, p)
    for t in re.findall(r'(?:src|srcset)="([^"]+\.svg)"', s):
        chk(t in svgs, "%s references non-gb svg %s" % (p, t))
for n in svgs:
    chk(os.path.exists(os.path.join(REPO, n)), "svg missing in repo: %s" % n)
    chk(filecmp.cmp(os.path.join(GB, "figs", n), os.path.join(REPO, n),
                    shallow=False), "svg differs in repo: %s" % n)
chk(len(svgs) == NSVG, "%d svgs, want %d" % (len(svgs), NSVG))
report(11, "%d internal .html links and %d svg src/srcset across the repo all "
           "resolve; the %d gb SVGs are byte-identical to gbm/figs"
           % (nlinks, nimg, NSVG))

# 12 --------------------------------------------------------- disclosure ----
for lang, suf in LANGS:
    discs = {}
    for slug in ORD:
        body = page_body(rd(REPO, "gb-%s%s.html" % (slug, suf)))
        head = body[:body.index("<h4>")]
        hits = [p_ for p_ in re.findall(r"<p>.*?</p>", head, re.S)
                if ANCHOR[lang] in p_]
        whole = ANCHOR[lang] in body
        if slug in DISC_ARTS:
            chk(len(hits) == 1, "gb-%s%s: disclosure missing before first <h4>"
                % (slug, suf))
            if hits:
                discs[slug] = hits[0]
        else:
            chk(not whole, "gb-%s%s: disclosure text present but not allowed"
                % (slug, suf))
    chk(len(set(discs.values())) == 1 and len(discs) == len(DISC_ARTS),
        "%s disclosure not byte-identical across %s (%d variants)"
        % (lang, "/".join(DISC_ARTS), len(set(discs.values()))))
    if lang == "en" and discs:
        spec = rd(GB, "SPEC-EN.md")
        want = spec[spec.index("> <p>My position first"):].split("\n", 1)[0][2:]
        chk(list(discs.values())[0] == want,
            "en disclosure != SPEC-EN.md section 1")
    if lang == "zh" and discs:
        spec = rd(GB, "SPEC.md")
        blk = spec[spec.index("> 先說我的位置"):]
        blk = blk[:blk.index("\n\n")]
        want = "".join(l.lstrip("> ").strip() for l in blk.splitlines())
        chk(list(discs.values())[0] == "<p>%s</p>" % want,
            "zh disclosure != SPEC.md section 二")
report(12, "disclosure paragraph before the first <h4> of exactly "
           "gb-surgery / gb-standard / gb-numbers / gb-newthings, "
           "byte-identical across the four (zh == SPEC 二, en == SPEC-EN 1), "
           "absent from the other 13 -- both languages")

# 13 ----------------------------------------------- titles & meta -----------
for p in arts:
    s = rd(REPO, p)
    en = p.endswith("-en.html")
    slug = p[len("gb-"):-len(".html")]
    if en:
        slug = slug[:-3]
    m = (gbm.EN if en else gbm.ART)[slug]
    si = [i for i, sec in enumerate(gbm.SECTIONS) if slug in sec["slugs"]][0]
    chk("<h1>%s</h1>" % tb.esc(m["title"]) in s, "%s h1" % p)
    title = re.search(r"<title>(.*?)</title>", s, re.S).group(1)
    chk(tb.esca(m["title"]) in title, "%s <title>" % p)
    chk(tb.esca(gbm.NAME_EN if en else gbm.NAME_ZH) in title,
        "%s <title> lacks topic name" % p)
    chk('<meta property="og:title" content="%s">' % title in s, "%s og:title" % p)
    chk('<meta name="description" content="%s">' % tb.esca(m["dek"]) in s,
        "%s description" % p)
    chk('<meta property="og:description" content="%s">' % tb.esca(m["dek"]) in s,
        "%s og:description" % p)
    chk('<p class="dek">%s</p>' % tb.esc(m["dek"]) in s, "%s dek" % p)
    chk('<div class="leadbox"><p>%s</p></div>' % tb.esc(m["lead"]) in s,
        "%s lead" % p)
    chk(tb.esc(m["note"]) in s, "%s mdnote" % p)
    kicker = gbm.SECTIONS_EN[si]["en"].upper()
    chk('<div class="kicker">%s</div>' % tb.esc(kicker) in s, "%s kicker" % p)
    sec_name = (gbm.SECTIONS_EN[si]["en"] if en else gbm.SECTIONS[si]["zh"])
    mm = re.search(r'<div class="meta">(.*?)</div>', s).group(1).split(" · ")
    chk(mm[0] == (gbm.NAME_EN if en else gbm.NAME_ZH) and mm[1] == sec_name,
        "%s meta line %s" % (p, mm))
    chk(('<a href="topics-en.html" class="on">' if en
         else '<a href="topics.html" class="on">') in s, "%s nav active" % p)
    chk('class="backlink" href="%s"' % hub_of("en" if en else "zh") in s,
        "%s backlink" % p)
    for k in gbm.ART[slug]["tags"]:
        chk('href="%s?tag=%s"' % (hub_of("en" if en else "zh"), k) in s,
            "%s tag chip %s" % (p, k))
    # pnav chain
    i = ORD.index(slug)
    pn = re.search(r'<div class="pnav">(.*?)</div>', s, re.S).group(1)
    if i == 0:
        chk(pn.startswith("<span></span>"), "%s first has prev" % p)
    else:
        chk('class="pv" href="gb-%s%s.html"' % (ORD[i - 1], "-en" if en else "")
            in pn, "%s prev" % p)
    if i == NART - 1:
        chk(pn.endswith("<span></span>"), "%s last has next" % p)
    else:
        chk('class="nx" href="gb-%s%s.html"' % (ORD[i + 1], "-en" if en else "")
            in pn, "%s next" % p)
for lang, page in (("zh", HUB_ZH), ("en", HUB_EN_NAME)):
    s = rd(REPO, page)
    hub = gbm.HUB if lang == "zh" else gbm.HUB_EN
    chk("<title>%s</title>" % tb.esca(hub["title"]) in s, "%s title" % page)
    chk('<meta name="description" content="%s">' % tb.esca(hub["desc"]) in s,
        "%s description" % page)
    chk('<div class="kicker">%s</div>' % gbm.KICKER in s, "%s kicker" % page)
    chk(tb.esc(hub["intro"]) in s or hub["intro"] in s, "%s intro" % page)
    chk(hub["closing"] in s, "%s closing" % page)
    meta_l = gbm.ART if lang == "zh" else gbm.EN
    cards = re.findall(r'<a class="postcard" data-tags="([^"]*)" href="([^"]*)"', s)
    chk([c[1] for c in cards] == ["gb-%s%s.html" % (s_, "-en" if lang == "en"
                                                    else "") for s_ in ORD],
        "%s card order" % page)
    for slug in ORD:
        chk('<div class="t">%s</div>' % tb.esc(meta_l[slug]["title"]) in s,
            "%s card title %s" % (page, slug))
    grp = re.findall(r'<div class="postgroup hnstep">.*?\n  </div>', s, re.S)
    chk([g.count('class="postcard"') for g in grp] == GROUPS,
        "%s group sizes" % page)
    for si, sec in enumerate(gbm.SECTIONS):
        nm = sec["zh"] if lang == "zh" else gbm.SECTIONS_EN[si]["en"]
        chk("<h3><b>%d</b>%s</h3>" % (si + 1, tb.esc(nm)) in s,
            "%s group title %d" % (page, si + 1))
    bar = tb.RE_HUB_TAGC.search(s).group(2)
    cnts = dict((k, int(n)) for k, n in
                re.findall(r'data-tag="([^"]*)">[^<]*<i>(\d+)</i>', bar))
    want = {"": NART}
    for slug in ORD:
        for k in gbm.ART[slug]["tags"]:
            want[k] = want.get(k, 0) + 1
    chk(cnts == want, "%s tagbar counts %s" % (page, cnts))
    li = 0 if lang == "zh" else 1
    for k, lab in gbm.LABEL_ADD.items():
        chk('data-tag="%s">#%s <i>' % (k, tb.esc(lab[li])) in bar,
            "%s new label %s" % (page, k))
report(13, "h1 / <title> / og:title / description / dek / lead / note / "
           "kicker / meta line / tag chips / pnav chain == meta & module on "
           "all 34 articles; hub title/desc/intro/closing, 4 groups %s, card "
           "titles = meta titles, tag counts = card counts, new labels "
           "rendered" % "/".join(str(g) for g in GROUPS))

# 14 -------------------------------------- skeleton / style / escaping ------
def skeleton(s):
    for rx in (tb.RE_TITLE, tb.RE_DESC, tb.RE_OGT, tb.RE_OGD, tb.RE_OGU,
               tb.RE_CANON, tb.RE_LD, tb.RE_STYLE, tb.RE_ALTS, tb.RE_LANG):
        s = rx.sub("@", s)
    s = re.sub(r'(<div class="article">).*?(\n  </div>\n</section>)',
               r"\1@\2", s, flags=re.S)
    s = re.sub(r'<section class="band narrow">.*?\n</section>', "@", s,
               flags=re.S)
    return s


for lang, suf in LANGS:
    t = skeleton(rd(REPO, ART_TPL[lang]))
    for slug in ORD:
        chk(skeleton(rd(REPO, "gb-%s%s.html" % (slug, suf))) == t,
            "gb-%s%s: skeleton differs from %s" % (slug, suf, ART_TPL[lang]))
for lang, page in (("zh", HUB_ZH), ("en", HUB_EN_NAME)):
    chk(skeleton(rd(REPO, page)) == skeleton(rd(REPO, HUB_TPL[lang])),
        "%s: skeleton differs from %s" % (page, HUB_TPL[lang]))
tpl_style = tb.RE_STYLE.search(rd(REPO, ART_TPL["zh"])).group(0)
chk(".article-figure{" in tpl_style,
    "cc template no longer carries the figure css -- inject_css path changed")
styles = set()
for p in pages:
    s = rd(REPO, p)
    st = tb.RE_STYLE.search(s).group(0)
    styles.add(st)
    chk(st == tpl_style, "%s: style != template" % p)
    chk(s.count(".article-figure{") == 1, "%s: figure css count" % p)
    for tag in ("<style>", "</style>", "<body>", "</body>", "</html>",
                "<head>", "</head>"):
        chk(s.count(tag) == 1, "%s: %s x%d" % (p, tag, s.count(tag)))
    chk("&amp;amp;" not in s and "&amp;quot;" not in s and "&#x27;" not in s
        and "&amp;gt;" not in s and "&amp;lt;" not in s,
        "%s: double-escaped entity" % p)
chk(len(styles) == 1, "style not byte-stable across pages")
report(14, "every byte outside the substituted slots equals the cc template; "
           "<style> byte-identical on all 36 (figure css present once); "
           "head/body tags once; no double-escaped entities")

# 15 --------------------------------------------------------- upload dir ----
produced = pages + svgs + ["topics.html", "topics-en.html", "sitemap.xml"]
have = sorted(os.listdir(UPLOAD))
chk(have == sorted(produced), "upload dir != produced set: extra %s missing %s"
    % (sorted(set(have) - set(produced)), sorted(set(produced) - set(have))))
for n in have:
    if n in produced:
        chk(filecmp.cmp(os.path.join(UPLOAD, n), os.path.join(REPO, n),
                        shallow=False), "upload copy differs: %s" % n)
report(15, "%s holds exactly the %d produced files (36 pages + %d svgs + 3 "
           "shared), each byte-identical to its repo copy"
           % (UPLOAD, len(produced), NSVG))

# 16 --------------------------------------------------------- git status ----
st = subprocess.run(["git", "-C", REPO, "status", "--short", "--porcelain"],
                    capture_output=True, text=True).stdout.splitlines()
mod = sorted(l[3:] for l in st if l.startswith(" M") or l.startswith("M "))
new = sorted(l[3:] for l in st if l.startswith("??"))
other = [l for l in st if not (l.startswith(" M") or l.startswith("M ")
                               or l.startswith("??"))]
want_new = sorted(pages + svgs + ["_pipeline/" + n for n in NEW_PIPELINE])
chk(mod == ["sitemap.xml", "topics-en.html", "topics.html"],
    "modified files: %s" % mod)
chk(new == want_new, "untracked: extra %s / missing %s"
    % (sorted(set(new) - set(want_new)), sorted(set(want_new) - set(new))))
chk(not other, "unexpected git status entries: %s" % other)
report(16, "git status: exactly topics.html, topics-en.html, sitemap.xml "
           "modified; untracked = 36 pages + %d svgs + 5 _pipeline modules"
           % NSVG)

print()
nfail = sum(1 for r in results if not r[2])
if nfail:
    print("FAILED: %d of %d checks" % (nfail, len(results)))
    sys.exit(1)
print("ALL %d CHECKS PASSED" % len(results))
