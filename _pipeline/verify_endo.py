# -*- coding: utf-8 -*-
"""Verification pass over the generated endometrial-cancer pages.

The cervix / liver / pel / esoph / gbm standard, printed as one PASS/FAIL
line per check:

  1  body text == source fragment byte-for-byte once the inserted <figure>
     blocks are stripped (zh and en, all 17); <hr> never leaks; h4 and
     citation counts equal source AND equal between zh and en
  2  reference list == source <ol> item by item; meta N == count; [n]
     markers run 1..N in first-use order; zh == en reference counts
  3  figure position per manifest after_h4 (same section index in en)
  4  figure files / alt / caption / height per manifest, escaped exactly once
  5  hreflang zh-Hant / en / x-default + canonical, both directions
  6  language switch chip points at the partner page, both directions
  7  JSON-LD parses on every page; about / name / url / inLanguage / dates
  8  topics.html and topics-en.html differ from prebackup by exactly one
     card (13th, after the gbm one) and one appended hasPart entry
  9  sitemap differs from prebackup by exactly the new contiguous block
     (after gb-recurrence-en.html, before carc.html), 714 -> 750, priorities
 10  pages produced (36) == sitemap URLs added; every page in the sitemap;
     17 zh == 17 en, groups 4/5/4/4
 11  every internal .html link and svg src/srcset in the repo resolves; the
     44 SVGs are byte-identical to /home/claude/endo/figs
 12  the disclosure paragraph sits before the first <h4> of exactly
     em-adjuvant / em-vaginal-brachy / em-chemo-rt / em-molecular-adjuvant,
     byte-identical across the four (zh == SPEC.md 二, en == SPEC-EN 1), and
     appears in no other article
 13  h1 / <title> / og:title / description / ld headline == meta title & dek;
     hub card titles == meta titles; hub tag counts consistent; every
     cross-reference title is verbatim 修正 16 / SPEC-EN section 3 or a live
     page's own title, with no near-miss variant
 14  every byte outside the substituted slots equals the cc template; style
     identical across the 36 pages; no double-escaped entities
 15  pel-who.html and pel-who-en.html differ from prebackup by exactly the
     three 修正 20 substitutions each (body / figure alt / closing note);
     no <a> added, 0 in-body site links; the bladder-cancer half is untouched
 16  git status shows only the expected new files and the five shared
     modifications -- nothing staged, nothing committed

Note on 修正 20: the SPEC names four spots, but those four are the two
asymmetric halves of three mirrored pairs (body sentence, figure alt, closing
note).  Fixing only four would leave the zh and en alt, and the zh and en
closing note, disagreeing -- so all six are rewritten, three per file, and
check 15 pins that.  The bladder-cancer half stays byte-identical in both
languages, and no <a> is added: pel-who's body links nothing.
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
import endo
import topicbuild as tb

REPO = "/home/claude/repo"
PRE = "/home/claude/endo/prebackup"
EM = "/home/claude/endo"
NART = 17
NFIG = 11
NSVG = 44
GROUPS = [4, 5, 4, 4]
ORD = [s for sec in endo.SECTIONS for s in sec["slugs"]]
LANGS = [("zh", ""), ("en", "-en")]
ART_TPL = {"zh": "cc-first-month.html", "en": "cc-first-month-en.html"}
HUB_TPL = {"zh": "cc.html", "en": "cc-en.html"}
SM_PREV = "gb-recurrence-en.html"
SM_NEXT = "carc.html"
PREV_CARD = {"zh": "gbm.html", "en": "gbm-en.html"}
NCARD = 13
SM_BEFORE, SM_AFTER = 714, 750
DISC_ARTS = ["adjuvant", "vaginal-brachy", "chemo-rt", "molecular-adjuvant"]
ANCHOR = {"zh": "先說我的位置", "en": "My position first"}
NEW_PIPELINE = ["build_endo.py", "endo.py", "endo_en.py",
                "stage_endo_figs.py", "verify_endo.py"]
SHARED = ["pel-who-en.html", "pel-who.html", "sitemap.xml",
          "topics-en.html", "topics.html"]

# The only 〈...〉 in the Chinese bodies that is not a cross-reference to a
# page: a cited journal article's own title, quoted in em-staging-2023.
ALLOW_ZH_ANGLE = {"FIGO 2023 endometrial cancer staging: too much, too soon?"}

hubs = ["em.html", "em-en.html"]
arts = ["em-%s%s.html" % (s, suf) for _, suf in LANGS for s in ORD]
pages = hubs + arts
svgs = sorted(n for n in os.listdir(os.path.join(EM, "figs"))
              if n.endswith(".svg"))
manifest = json.load(open(os.path.join(EM, "figs", "manifest.json"),
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
    """The em fragments keep the em- prefix in BOTH languages; the English
    ones carry no -en suffix, only a different directory."""
    return os.path.join(EM, "body" if lang == "zh" else "en", "em-%s.html" % slug)


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
                  rd(EM, "figs", svg_name))
    assert m and m.group(1) == "1440", svg_name
    return str(int(decimal.Decimal(m.group(2)).quantize(
        decimal.Decimal("1"), rounding=decimal.ROUND_HALF_UP)))


for p in pages:
    if not os.path.exists(os.path.join(REPO, p)):
        print("FATAL: missing %s" % p)
        sys.exit(2)

# 1 ------------------------------------------ body == source minus figures --
for slug in ORD:
    counts = {}
    for lang, suf in LANGS:
        body, items, n = tb.split_fragment(rd(src_path(slug, lang)))
        pb = page_body(rd(REPO, "em-%s%s.html" % (slug, suf)))
        nofig = RE_FIG_STRIP.sub("\n", pb)
        # the figure sits between two sections; stripping it may leave a
        # collapsed blank line, so compare after normalising the separator
        chk(re.sub(r"\n{2,}", "\n\n", nofig).strip()
            == re.sub(r"\n{2,}", "\n\n", body).strip(),
            "em-%s%s body differs from source outside the figure block"
            % (slug, suf))
        chk("<hr>" not in pb, "em-%s%s: <hr> leaked into body" % (slug, suf))
        nh4 = len(re.findall(r"<h4>", pb))
        ncit = len(re.findall(r'<sup class="cit">', pb))
        chk(nh4 == len(re.findall(r"<h4>", body)),
            "em-%s%s: h4 count" % (slug, suf))
        chk(ncit == len(re.findall(r'<sup class="cit">', body)),
            "em-%s%s: citation count" % (slug, suf))
        counts[lang] = (nh4, ncit)
    chk(counts["zh"][0] == counts["en"][0],
        "em-%s: zh %d h4 vs en %d" % (slug, counts["zh"][0], counts["en"][0]))
    chk(counts["zh"][1] == counts["en"][1],
        "em-%s: zh %d citations vs en %d"
        % (slug, counts["zh"][1], counts["en"][1]))
report(1, "body-html == source fragment byte-for-byte after stripping the "
          "inserted <figure> (17 zh + 17 en); <hr> never leaks; h4 and "
          "citation counts equal the source and equal each other across "
          "languages")

# 2 ------------------------------------------------- references item by item --
for slug in ORD:
    for lang, suf in LANGS:
        body, items, n = tb.split_fragment(rd(src_path(slug, lang)))
        page = rd(REPO, "em-%s%s.html" % (slug, suf))
        pr = page_refs(page)
        chk(pr == items, "em-%s%s: reference <ol> content differs from source"
            % (slug, suf))
        src_li = re.findall(r"<li>.*?</li>", items, re.S)
        page_li = re.findall(r"<li>.*?</li>", pr, re.S)
        chk(len(src_li) == len(page_li) == n,
            "em-%s%s: %d/%d/%d reference items" % (slug, suf, len(src_li),
                                                   len(page_li), n))
        for k, (a, b) in enumerate(zip(src_li, page_li)):
            chk(a == b, "em-%s%s: reference %d differs" % (slug, suf, k + 1))
        chk("<ol>" not in pr and "<p></p>" not in pr,
            "em-%s%s: nested <ol> or trailing empty <p>" % (slug, suf))
        mm = re.search(r'<div class="meta">(.*?)</div>', page).group(1)
        chk(int(re.search(r"\d+", mm.split(" · ")[2]).group(0)) == n,
            "em-%s%s: meta reference count != %d" % (slug, suf, n))
        nums = [int(x) for x in
                re.findall(r'<sup class="cit">\[(\d+)\]</sup>', page_body(page))]
        first = [v for i, v in enumerate(nums) if v not in nums[:i]]
        chk(first == list(range(1, n + 1)),
            "em-%s%s: [n] markers not 1..%d in first-use order" % (slug, suf, n))
    zn = tb.split_fragment(rd(src_path(slug, "zh")))[2]
    en_ = tb.split_fragment(rd(src_path(slug, "en")))[2]
    chk(zn == en_, "em-%s: zh %d refs vs en %d" % (slug, zn, en_))
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
    want = per.get("em-" + slug, [])
    src_h4 = re.findall(r"<h4>(.*?)</h4>", rd(src_path(slug, "zh")))
    want_pos = []
    for f in want:
        chk(f["placement"]["after_h4"] in src_h4,
            "%s: after_h4 not found in em-%s" % (f["id"], slug))
        if f["placement"]["after_h4"] in src_h4:
            want_pos.append(src_h4.index(f["placement"]["after_h4"]) + 1)
    for lang, suf in LANGS:
        body = page_body(rd(REPO, "em-%s%s.html" % (slug, suf)))
        figs = RE_FIG.findall(body)
        chk(len(figs) == len(want), "em-%s%s: %d figures, want %d"
            % (slug, suf, len(figs), len(want)))
        pos, h4 = [], 0
        for m in re.finditer(r'<h4>|<figure class="article-figure">', body):
            if m.group(0) == "<h4>":
                h4 += 1
            else:
                pos.append(h4)
        chk(pos == want_pos, "em-%s%s: figure after h4 #%s, want #%s"
            % (slug, suf, pos, want_pos))
        # the figure closes its section: the next thing after it is an <h4>
        for m in re.finditer(r"</figure>\n+", body):
            chk(body[m.end():m.end() + 4] == "<h4>",
                "em-%s%s: figure is not immediately followed by the next <h4>"
                % (slug, suf))
        for got, fig in zip(figs, want):
            alt_pairs.append((lang, slug, fig, got))
        nfig += len(figs)
chk(nfig == NFIG * 2, "%d figure instances, want %d (%d x 2 languages)"
    % (nfig, NFIG * 2, NFIG))
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
    tag = "em-%s (%s)" % (slug, lang)
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
report(4, "all %d figure instances: mobile/desktop files per language, "
          "height = desktop viewBox, alt attribute-escaped once, caption "
          "text-escaped once, all equal to the manifest" % (NFIG * 2))

# 5 ----------------------------------------------------------- hreflang -------
for slug in ORD + [None]:
    z = "em.html" if slug is None else "em-%s.html" % slug
    en = "em-en.html" if slug is None else "em-%s-en.html" % slug
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
    z = "em.html" if slug is None else "em-%s.html" % slug
    en = "em-en.html" if slug is None else "em-%s-en.html" % slug
    sz, se = rd(REPO, z), rd(REPO, en)
    chk('<div class="lang"><span class="on">中</span><a href="%s" '
        'hreflang="en">EN</a></div>' % en in sz, "%s lang switch -> %s" % (z, en))
    chk('<div class="lang"><a href="%s" hreflang="zh-Hant">中</a>'
        '<span class="on">EN</span></div>' % z in se,
        "%s lang switch -> %s" % (en, z))
    chk(sz.count('<div class="lang">') == 1
        and se.count('<div class="lang">') == 1,
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
    chk(ld["about"]["name"] == (endo.CONDITION_EN if en
                                else endo.CONDITION_ZH),
        "%s about.name %s" % (p, ld["about"]["name"]))
    chk(ld["author"]["@type"] == "Physician", "%s author" % p)
    if p in hubs:
        chk(ld["@type"] == "CollectionPage", "%s type" % p)
        chk(ld["name"] == (endo.NAME_EN if en else endo.NAME_ZH), "%s name" % p)
        chk([e["url"] for e in ld["hasPart"]]
            == [tb.BASE + "em-%s%s.html" % (s_, "-en" if en else "")
                for s_ in ORD], "%s hasPart urls" % p)
        meta = endo.EN if en else endo.ART
        chk([e["name"] for e in ld["hasPart"]]
            == [meta[s_]["title"] for s_ in ORD], "%s hasPart names" % p)
    else:
        slug = p[len("em-"):-len(".html")]
        if en:
            slug = slug[:-3]
        meta = (endo.EN if en else endo.ART)[slug]
        chk(ld["@type"] == "MedicalWebPage", "%s type" % p)
        chk(ld["headline"] == meta["title"], "%s headline" % p)
        chk(ld["description"] == meta["dek"], "%s description" % p)
        chk(ld["datePublished"] == endo.DATE
            and ld["dateModified"] == endo.DATE, "%s dates" % p)
    chk(s.count('<script type="application/ld+json">') == 1, "%s ld count" % p)
report(7, "JSON-LD parses on all 36 pages; @type / url / inLanguage / "
          "about = MedicalCondition %s|%s / headline / dates / hub hasPart "
          "all correct" % (endo.CONDITION_ZH, endo.CONDITION_EN))

# 8 ---------------------------------------------------- topics pages diff ---
for f, card, hp, href, prev_href in (
        ("topics.html", endo.TOPIC_CARD_ZH, endo.HASPART_ZH, "em.html",
         PREV_CARD["zh"]),
        ("topics-en.html", endo.TOPIC_CARD_EN, endo.HASPART_EN,
         "em-en.html", PREV_CARD["en"])):
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
        "%s: JSON-LD line not just extended by the em hasPart entry" % f)
    rest = [l for l in added if '"hasPart":[' not in l]
    chk("".join(rest) == card, "%s: added text is not exactly the em card" % f)
    grid = re.search(r'<div class="topicgrid">(.*?)\n  </div>', now, re.S).group(1)
    cards = re.findall(r'<a class="topiccard" href="([^"]+)"', grid)
    chk(len(cards) == NCARD and cards[-1] == href and cards[-2] == prev_href,
        "%s: card order %s" % (f, cards))
    chk(now.count('class="topiccard"') == pre.count('class="topiccard"') + 1,
        "%s: card count" % f)
    ld, pre_ld = ld_of(now), ld_of(pre)
    chk(ld["hasPart"][:-1] == pre_ld["hasPart"] and ld["hasPart"][-1] == hp,
        "%s: hasPart not old + em" % f)
    chk('<div class="k">%s</div>' % endo.KICKER in card, "%s: card kicker" % f)
    chk('<span class="n">%d %s</span>' % (NART, "篇" if f == "topics.html"
                                          else "articles") in card,
        "%s: card count label" % f)
report(8, "topics.html and topics-en.html differ from prebackup by exactly "
          "the em card (after the gbm card, %dth) and one appended hasPart "
          "entry; card says %s / %d" % (NCARD, endo.KICKER, NART))

# 9 --------------------------------------------------------- sitemap diff ---
sm, pre_sm = rd(REPO, "sitemap.xml"), rd(PRE, "sitemap.xml")
RE_LOC = re.compile(re.escape(tb.BASE) + r"([^<]*)</loc>")
RE_EM = re.compile(r"<loc>%s(em\.html|em-)" % re.escape(tb.BASE))
sml = sm.splitlines()
em_lines = [l for l in sml if RE_EM.search(l)]
kept = [l for l in sml if not RE_EM.search(l)]
chk(kept == pre_sm.splitlines(), "non-em sitemap lines changed or reordered")
chk(not any(RE_EM.search(l) for l in pre_sm.splitlines()),
    "prebackup already had em lines")
chk(pre_sm.count("<url>") == SM_BEFORE, "prebackup <url> = %d, want %d"
    % (pre_sm.count("<url>"), SM_BEFORE))
chk(sm.count("<url>") == SM_AFTER, "sitemap <url> = %d, want %d"
    % (sm.count("<url>"), SM_AFTER))
chk(len(em_lines) == 36, "%d em sitemap lines, want 36" % len(em_lines))
want_order = (["em.html", "em-en.html"] + ["em-%s.html" % s for s in ORD]
              + ["em-%s-en.html" % s for s in ORD])
chk([RE_LOC.search(l).group(1) for l in em_lines] == want_order,
    "em block order is not hub zh, hub en, 17 zh, 17 en")
prio = {"em.html": "0.85", "em-en.html": "0.75"}
prio.update(("em-%s.html" % s, "0.75") for s in ORD)
prio.update(("em-%s-en.html" % s, "0.65") for s in ORD)
for l in em_lines:
    n = RE_LOC.search(l).group(1)
    chk("<priority>%s</priority>" % prio[n] in l, "%s priority" % n)
    chk("<lastmod>%s</lastmod>" % endo.DATE in l, "%s lastmod" % n)
    chk("<changefreq>monthly</changefreq>" in l, "%s changefreq" % n)
i_prev = [i for i, l in enumerate(sml)
          if "<loc>%s%s</loc>" % (tb.BASE, SM_PREV) in l]
chk(len(i_prev) == 1, "anchor %s not found once" % SM_PREV)
if i_prev:
    i = i_prev[0]
    chk(all(RE_EM.search(l) for l in sml[i + 1:i + 37]),
        "em block not contiguous right after %s" % SM_PREV)
    chk("<loc>%s%s</loc>" % (tb.BASE, SM_NEXT) in sml[i + 37],
        "em block not immediately before %s" % SM_NEXT)
chk("em-em-" not in sm and not any("em-em-" in n for n in os.listdir(REPO)),
    "double-prefixed name somewhere")
report(9, "sitemap differs from prebackup by exactly one contiguous 36-line "
          "block after %s / before %s; <url> %d -> %d; order hub zh, hub en, "
          "17 zh, 17 en; priorities 0.85/0.75/0.75/0.65; lastmod %s"
          % (SM_PREV, SM_NEXT, SM_BEFORE, SM_AFTER, endo.DATE))

# 10 ---------------------------------------------- pages == sitemap adds ----
sm_names = set(m.group(1) for m in RE_LOC.finditer(sm))
pre_names = set(m.group(1) for m in RE_LOC.finditer(pre_sm))
added_names = sm_names - pre_names
chk(len(pages) == 36, "%d pages, want 36" % len(pages))
chk(added_names == set(pages), "sitemap additions != produced pages: +%s -%s"
    % (sorted(added_names - set(pages)), sorted(set(pages) - added_names)))
chk(len(ORD) == NART and [len(s["slugs"]) for s in endo.SECTIONS] == GROUPS,
    "reading order is not %d in %s" % (NART, GROUPS))
chk([len(s["slugs"]) for s in endo.SECTIONS_EN] == GROUPS,
    "English group sizes differ from the Chinese")
chk([s["slugs"] for s in endo.SECTIONS] == [s["slugs"] for s in endo.SECTIONS_EN],
    "zh and en reading orders differ")
chk(len([p for p in arts if p.endswith("-en.html")])
    == len([p for p in arts if not p.endswith("-en.html")]) == NART,
    "zh/en article counts unequal")
repo_html = set(n for n in os.listdir(REPO) if n.endswith(".html"))
chk(all(n in repo_html for n in sm_names if n.endswith(".html")),
    "sitemap URL without a file: %s"
    % sorted(n for n in sm_names if n.endswith(".html") and n not in repo_html))
report(10, "36 pages produced (2 hubs + 17 zh + 17 en, groups 4/5/4/4, same "
           "order in both languages) == the 36 sitemap URLs added; every "
           "sitemap URL has a file")

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
# em pages specifically: every svg they reference is an em svg
for p in pages:
    s = rd(REPO, p)
    for t in re.findall(r'(?:src|srcset)="([^"]+\.svg)"', s):
        chk(t in svgs, "%s references non-em svg %s" % (p, t))
for n in svgs:
    chk(os.path.exists(os.path.join(REPO, n)), "svg missing in repo: %s" % n)
    chk(filecmp.cmp(os.path.join(EM, "figs", n), os.path.join(REPO, n),
                    shallow=False), "svg differs in repo: %s" % n)
chk(len(svgs) == NSVG, "%d svgs, want %d" % (len(svgs), NSVG))
report(11, "%d internal .html links and %d svg src/srcset across the repo all "
           "resolve (0 broken); the %d em SVGs are byte-identical to "
           "endo/figs" % (nlinks, nimg, NSVG))

# 12 --------------------------------------------------------- disclosure ----
for lang, suf in LANGS:
    discs = {}
    for slug in ORD:
        body = page_body(rd(REPO, "em-%s%s.html" % (slug, suf)))
        head = body[:body.index("<h4>")]
        hits = [p_ for p_ in re.findall(r"<p>.*?</p>", head, re.S)
                if ANCHOR[lang] in p_]
        whole = ANCHOR[lang] in body
        if slug in DISC_ARTS:
            chk(len(hits) == 1, "em-%s%s: disclosure missing before first <h4>"
                % (slug, suf))
            chk(body.count(ANCHOR[lang]) == 1,
                "em-%s%s: disclosure anchor appears more than once"
                % (slug, suf))
            if hits:
                discs[slug] = hits[0]
        else:
            chk(not whole, "em-%s%s: disclosure text present but not allowed"
                % (slug, suf))
    chk(len(set(discs.values())) == 1 and len(discs) == 4,
        "%s disclosure not byte-identical across B1/B2/B3/B4 (%d variants)"
        % (lang, len(set(discs.values()))))
    if lang == "en" and discs:
        spec = rd(EM, "SPEC-EN.md")
        want = spec[spec.index("> <p>My position first"):].split("\n", 1)[0][2:]
        chk(list(discs.values())[0] == want,
            "en disclosure != SPEC-EN.md section 1")
    if lang == "zh" and discs:
        spec = rd(EM, "SPEC.md")
        blk = spec[spec.index("> 先說我的位置"):]
        blk = blk[:blk.index("\n\n")]
        want = "".join(l.lstrip("> ").strip() for l in blk.splitlines())
        chk(list(discs.values())[0] == "<p>%s</p>" % want,
            "zh disclosure != SPEC.md section 二")
report(12, "disclosure paragraph before the first <h4> of exactly "
           "em-adjuvant / em-vaginal-brachy / em-chemo-rt / "
           "em-molecular-adjuvant, byte-identical across the four "
           "(zh == SPEC 二, en == SPEC-EN 1), absent from the other 13 -- "
           "both languages")

# 13 ----------------------------------------- titles, meta & cross-references --
for p in arts:
    s = rd(REPO, p)
    en = p.endswith("-en.html")
    slug = p[len("em-"):-len(".html")]
    if en:
        slug = slug[:-3]
    m = (endo.EN if en else endo.ART)[slug]
    si = [i for i, sec in enumerate(endo.SECTIONS) if slug in sec["slugs"]][0]
    chk("<h1>%s</h1>" % tb.esc(m["title"]) in s, "%s h1" % p)
    title = re.search(r"<title>(.*?)</title>", s, re.S).group(1)
    chk(tb.esca(m["title"]) in title, "%s <title>" % p)
    chk(tb.esca(endo.NAME_EN if en else endo.NAME_ZH) in title,
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
    kicker = endo.SECTIONS_EN[si]["en"].upper()
    chk('<div class="kicker">%s</div>' % tb.esc(kicker) in s, "%s kicker" % p)
    sec_name = (endo.SECTIONS_EN[si]["en"] if en else endo.SECTIONS[si]["zh"])
    mm = re.search(r'<div class="meta">(.*?)</div>', s).group(1).split(" · ")
    chk(mm[0] == (endo.NAME_EN if en else endo.NAME_ZH) and mm[1] == sec_name,
        "%s meta line %s" % (p, mm))
    chk(('<a href="topics-en.html" class="on">' if en
         else '<a href="topics.html" class="on">') in s, "%s nav active" % p)
    chk('class="backlink" href="%s"' % ("em-en.html" if en else "em.html") in s,
        "%s backlink" % p)
    for k in endo.ART[slug]["tags"]:
        chk('href="%s?tag=%s"' % ("em-en.html" if en else "em.html", k) in s,
            "%s tag chip %s" % (p, k))
    # pnav chain
    i = ORD.index(slug)
    pn = re.search(r'<div class="pnav">(.*?)</div>', s, re.S).group(1)
    if i == 0:
        chk(pn.startswith("<span></span>"), "%s first has prev" % p)
    else:
        chk('class="pv" href="em-%s%s.html"' % (ORD[i - 1], "-en" if en else "")
            in pn, "%s prev" % p)
    if i == NART - 1:
        chk(pn.endswith("<span></span>"), "%s last has next" % p)
    else:
        chk('class="nx" href="em-%s%s.html"' % (ORD[i + 1], "-en" if en else "")
            in pn, "%s next" % p)
for lang, page in (("zh", "em.html"), ("en", "em-en.html")):
    s = rd(REPO, page)
    hub = endo.HUB if lang == "zh" else endo.HUB_EN
    chk("<title>%s</title>" % tb.esca(hub["title"]) in s, "%s title" % page)
    chk('<meta name="description" content="%s">' % tb.esca(hub["desc"]) in s,
        "%s description" % page)
    chk('<div class="kicker">%s</div>' % endo.KICKER in s, "%s kicker" % page)
    chk(tb.esc(hub["intro"]) in s or hub["intro"] in s, "%s intro" % page)
    chk(hub["closing"] in s, "%s closing" % page)
    meta_l = endo.ART if lang == "zh" else endo.EN
    cards = re.findall(r'<a class="postcard" data-tags="([^"]*)" href="([^"]*)"', s)
    chk([c[1] for c in cards] == ["em-%s%s.html" % (s_, "-en" if lang == "en"
                                                    else "") for s_ in ORD],
        "%s card order" % page)
    for slug in ORD:
        chk('<div class="t">%s</div>' % tb.esc(meta_l[slug]["title"]) in s,
            "%s card title %s" % (page, slug))
    grp = re.findall(r'<div class="postgroup hnstep">.*?\n  </div>', s, re.S)
    chk([g.count('class="postcard"') for g in grp] == GROUPS,
        "%s group sizes" % page)
    for si, sec in enumerate(endo.SECTIONS):
        nm = sec["zh"] if lang == "zh" else endo.SECTIONS_EN[si]["en"]
        chk("<h3><b>%d</b>%s</h3>" % (si + 1, tb.esc(nm)) in s,
            "%s group title %d" % (page, si + 1))
    bar = tb.RE_HUB_TAGC.search(s).group(2)
    cnts = dict((k, int(n)) for k, n in
                re.findall(r'data-tag="([^"]*)">[^<]*<i>(\d+)</i>', bar))
    want = {"": NART}
    for slug in ORD:
        for k in endo.ART[slug]["tags"]:
            want[k] = want.get(k, 0) + 1
    chk(cnts == want, "%s tagbar counts %s" % (page, cnts))
    li = 0 if lang == "zh" else 1
    for k, lab in endo.LABEL_ADD.items():
        chk('data-tag="%s">#%s <i>' % (k, tb.esc(lab[li])) in bar,
            "%s new label %s" % (page, k))

# cross-reference titles: 修正 16 (zh) / SPEC-EN section 3 (en), verbatim
zh_titles = set(endo.ART[s]["title"] for s in ORD)
en_titles = set(endo.EN[s]["title"] for s in ORD)
spec = rd(EM, "SPEC.md")
tbl = spec[spec.index("### 修正 16"):spec.index("### 修正 17")]
fix16 = dict(re.findall(r"\| \`(em-[a-z0-9-]+)\` \| (.+?) \|", tbl))
chk(len(fix16) == NART, "修正 16 table has %d rows" % len(fix16))
for slug in ORD:
    chk(endo.ART[slug]["title"] == fix16.get("em-" + slug),
        "em-%s title != 修正 16 table" % slug)
sp_en = rd(EM, "SPEC-EN.md")
sec3 = sp_en[sp_en.index("## 3. Canonical English titles"):
             sp_en.index("## 4. Structure")]
spec_en_titles = dict(re.findall(r"- (em-[a-z0-9-]+) → \"(.+?)\"", sec3))
chk(len(spec_en_titles) == NART,
    "SPEC-EN section 3 has %d rows" % len(spec_en_titles))
for slug in ORD:
    chk(endo.EN[slug]["title"] == spec_en_titles.get("em-" + slug),
        "em-%s en title != SPEC-EN section 3" % slug)

live_h1, live_head = set(), set()
for n in os.listdir(REPO):
    if not n.endswith(".html") or n == "em.html" or n.startswith("em-"):
        continue
    s = rd(REPO, n)
    m = re.search(r"<h1>(.*?)</h1>", s, re.S)
    if m:
        live_h1.add(m.group(1))
    if n.endswith("-en.html"):
        m = re.search(r"<title>(.*?)</title>", s, re.S)
        if m:
            live_head.add(re.split(r"[｜|]", m.group(1))[0].strip())
n_zh_xref = 0
for slug in ORD:
    body = page_body(rd(REPO, "em-%s.html" % slug))
    for t in re.findall(r"〈([^〉]*)〉", body):
        if t in zh_titles or t in live_h1:
            n_zh_xref += 1
            continue
        chk(t in ALLOW_ZH_ANGLE,
            "em-%s: cross-reference 〈%s〉 matches no canonical title"
            % (slug, t))
known_en = en_titles | live_head
n_en_xref = 0
for slug in ORD:
    body = page_body(rd(REPO, "em-%s-en.html" % slug))
    body = RE_FIG_STRIP.sub("\n", body)
    for q in re.findall(r'"([^"]{18,110})"', body):
        if q in known_en:
            n_en_xref += 1
            continue
        ratio, near = max((difflib.SequenceMatcher(None, q, k).ratio(), k)
                          for k in known_en)
        chk(ratio < 0.86,
            "em-%s-en: quoted \"%s\" is a near-miss of \"%s\" (%.2f)"
            % (slug, q, near, ratio))
chk(n_zh_xref >= NART and n_en_xref >= NART,
    "suspiciously few cross-references found (zh %d, en %d)"
    % (n_zh_xref, n_en_xref))
report(13, "h1 / <title> / og:title / description / dek / lead / note / "
           "kicker / meta line / tag chips / pnav chain == meta & module on "
           "all 34 articles; hub title/desc/intro/closing, 4 groups 4/5/4/4, "
           "card titles = meta titles, tag counts = card counts, new labels "
           "rendered; %d zh and %d en cross-reference titles are verbatim "
           "修正 16 / SPEC-EN 3 or a live page's own title, no near-miss "
           "variants" % (n_zh_xref, n_en_xref))

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
        chk(skeleton(rd(REPO, "em-%s%s.html" % (slug, suf))) == t,
            "em-%s%s: skeleton differs from %s" % (slug, suf, ART_TPL[lang]))
for lang, page in (("zh", "em.html"), ("en", "em-en.html")):
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

# 15 --------------------------------------------------------- pel-who diff ---
for f in ("pel-who.html", "pel-who-en.html"):
    pre, now = rd(PRE, f), rd(REPO, f)
    pl, nl = pre.splitlines(True), now.splitlines(True)
    chk(len(pl) == len(nl), "%s: line count changed %d -> %d"
        % (f, len(pl), len(nl)))
    diff_idx = [i for i, (a, b) in enumerate(zip(pl, nl)) if a != b]
    chk(len(diff_idx) == 3, "%s: %d changed lines, want 3 (lines %s)"
        % (f, len(diff_idx), [i + 1 for i in diff_idx]))
    edits = endo.PEL_WHO_EDITS[f]
    chk(len(edits) == 3, "%s: %d edits declared, want 3" % (f, len(edits)))
    want = pre
    for old, new in edits:
        chk(want.count(old) == 1, "%s: anchor not present exactly once in the "
            "prebackup: %r" % (f, old[:40]))
        want = want.replace(old, new)
    chk(now == want, "%s: content is not the prebackup with exactly the three "
        "修正 20 substitutions applied" % f)
    for old, new in edits:
        chk(old not in now, "%s: old wording still present: %r" % (f, old[:40]))
        chk(now.count(new) == 1, "%s: new wording not present exactly once: %r"
            % (f, new[:40]))
    # no <a> was added: pel-who's body carries no in-body site links at all,
    # and the new pointers follow that page's unlinked 〈title〉 / "title" style
    def body_links(s):
        b = re.search(r'<div class="body-html">\n(.*?)\n    </div>',
                      s, re.S).group(1)
        return re.findall(r'href="([^":]+\.html)(?:[#?][^"]*)?"', b)
    chk(body_links(now) == [] == body_links(pre),
        "%s: in-body site links %s, want 0 (prebackup had %d)"
        % (f, body_links(now), len(body_links(pre))))
    chk(now.count("<a ") == pre.count("<a ") and now.count("<a href=")
        == pre.count("<a href="), "%s: anchor count changed %d -> %d"
        % (f, pre.count("<a href="), now.count("<a href=")))
# the endometrial topic is now pointed at, unlinked, in both languages
chk("〈子宮內膜癌專題〉" in rd(REPO, "pel-who.html"),
    "pel-who.html does not point at 〈子宮內膜癌專題〉")
chk('"Endometrial Cancer Guide"' in rd(REPO, "pel-who-en.html"),
    'pel-who-en.html does not point at "Endometrial Cancer Guide"')
chk('href="em.html"' not in rd(REPO, "pel-who.html")
    and 'href="em-en.html"' not in rd(REPO, "pel-who-en.html"),
    "an <a> to the em hub was added to pel-who -- that page links nothing "
    "in body")
# the bladder-cancer half is byte-identical, in both languages, all 3 spots
chk("膀胱癌另有專題規劃中。" in rd(REPO, "pel-who.html"),
    "pel-who.html: the bladder-cancer alt sentence was changed")
chk("膀胱癌那一篇還在規劃中" in rd(REPO, "pel-who.html"),
    "pel-who.html: the bladder half of the closing note was dropped")
chk("A separate bladder cancer topic is being planned"
    in rd(REPO, "pel-who-en.html"),
    "pel-who-en.html: the bladder-cancer body sentence was changed")
chk("a separate series on bladder cancer is planned"
    in rd(REPO, "pel-who-en.html"),
    "pel-who-en.html: the bladder-cancer alt sentence was changed")
chk("the bladder cancer topic is still being planned"
    in rd(REPO, "pel-who-en.html"),
    "pel-who-en.html: the bladder half of the closing sentence was dropped")
# no "planned" claim about the endometrial topic survives, either language
chk("子宮內膜癌另有專題規劃中" not in rd(REPO, "pel-who.html")
    and "子宮內膜癌兩篇還在規劃中" not in rd(REPO, "pel-who.html"),
    "pel-who.html still says the endometrial topic is being planned")
chk("A separate endometrial cancer topic is being planned"
    not in rd(REPO, "pel-who-en.html")
    and "the neighbours change; a separate series is planned"
    not in rd(REPO, "pel-who-en.html")
    and "endometrial cancer topics are still being planned"
    not in rd(REPO, "pel-who-en.html"),
    "pel-who-en.html still says the endometrial topic is being planned")
report(15, "pel-who.html and pel-who-en.html differ from prebackup by exactly "
           "the three 修正 20 substitutions each (3 changed lines per file, "
           "one per mirrored pair: body / figure alt / closing note); both "
           "point at the topic unlinked in the page's own style with 0 "
           "in-body site links and no anchor added; the bladder-cancer half "
           "is byte-identical in both languages")

# 16 --------------------------------------------------------- git status ----
st = subprocess.run(["git", "-C", REPO, "status", "--short", "--porcelain"],
                    capture_output=True, text=True).stdout.splitlines()
mod = sorted(l[3:] for l in st if l.startswith(" M") or l.startswith("M "))
new = sorted(l[3:] for l in st if l.startswith("??"))
other = [l for l in st if not (l.startswith(" M") or l.startswith("M ")
                               or l.startswith("??"))]
staged = [l for l in st if l[0] not in " ?"]
want_new = sorted(pages + svgs + ["_pipeline/" + n for n in NEW_PIPELINE])
chk(mod == SHARED, "modified files: %s" % mod)
chk(new == want_new, "untracked: extra %s / missing %s"
    % (sorted(set(new) - set(want_new)), sorted(set(want_new) - set(new))))
chk(not other, "unexpected git status entries: %s" % other)
chk(not staged, "something is staged for commit: %s" % staged)
head = subprocess.run(["git", "-C", REPO, "log", "-1", "--format=%s"],
                      capture_output=True, text=True).stdout.strip()
chk("endo" not in head.lower() and "em:" not in head.lower(),
    "HEAD looks like an endo commit -- this round is local only: %r" % head)
report(16, "git status: exactly %s modified; untracked = 36 pages + %d svgs + "
           "5 _pipeline modules; nothing staged, nothing committed"
           % (", ".join(SHARED), NSVG))

print()
nfail = sum(1 for r in results if not r[2])
if nfail:
    print("FAILED: %d of %d checks" % (nfail, len(results)))
    sys.exit(1)
print("ALL %d CHECKS PASSED" % len(results))
