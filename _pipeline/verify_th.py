# -*- coding: utf-8 -*-
"""Verification pass over the generated thyroid-cancer pages.

The cervix / liver / pel / esoph / gbm / endo / bt / bl standard, printed as
one PASS/FAIL line per check:

  1  body text == source fragment byte-for-byte once the inserted <figure>
     blocks are stripped and BODY_EDITS applied (zh and en, all 20); <hr>
     never leaks; h4 and citation counts equal source AND equal between
     zh and en
  2  reference list == source <ol> item by item; meta N == count; [n]
     markers run 1..N in first-use order; zh == en reference counts
  3  figure position per manifest after_h4 (same section index in en); every
     article a figure declares in used_by actually carries it
  4  figure files / alt / caption / height per manifest, escaped exactly once
  5  hreflang zh-Hant / en / x-default + canonical, both directions
  6  language switch chip points at the partner page, both directions
  7  JSON-LD parses on every page; about / name / url / inLanguage / dates
  8  topics.html and topics-en.html differ from prebackup by exactly one
     card (16th, after the bl one) and one appended hasPart entry
  9  sitemap differs from prebackup by exactly the new contiguous block
     (after bl-daily-en.html, before carc.html), 832 -> 874, priorities
 10  pages produced (42) == sitemap URLs added; every page in the sitemap;
     20 zh == 20 en, groups 5/4/2/5/4
 11  every internal .html link and svg src/srcset in the repo resolves; the
     48 SVGs are byte-identical to /home/claude/th/figs
 12  the disclosure paragraph sits before the first <h4> of exactly
     th-ebrt (zh == SPEC.md 二, en == SPEC-EN 1) and appears in no other
     article
 13  h1 / <title> / og:title / description / ld headline == meta title & dek;
     hub card titles == meta titles; hub tag counts consistent; every
     cross-reference title is verbatim SPEC 四 / SPEC-EN section 4 or a live
     page's own heading, with no unresolved variant, on TWO surfaces --
     prose with the <figure> blocks stripped, and the figures' own alt and
     figcaption text
 14  every byte outside the substituted slots equals the cc template; style
     identical across the 42 pages; no double-escaped entities
 15  THE INVARIANT OF THIS ROUND: the topic adds no edit to any pre-existing
     page.  Every tracked file in the repo except the three index files is
     byte-identical to HEAD; the module declares no chore machinery; the
     three off-series pages this topic points at are untouched and are named
     by their own live <h1>; and no live page was left promising a thyroid
     topic that this round would have had to redeem
 16  git status shows only the expected new files and the three shared
     modifications -- nothing staged, nothing committed

WHAT CHANGED FROM verify_bl.py, and why.

(a) THERE IS NO SHARED-FILE CHORE, so bl's check 15 -- which pinned the five
    pel-who substitutions -- has nothing to pin.  It is NOT renumbered away
    and it is NOT left inert: it is replaced by the stronger statement this
    round actually makes.  bl could only say "the two pages I edited changed
    in exactly these five places".  th says "NOTHING outside the three index
    files changed at all", read off `git diff` against HEAD over every
    tracked file, not off a two-file prebackup.  The premise was re-checked
    rather than inherited: pel-who's pending promise was the bladder topic's
    and gb-what-it-is's was the brain topic's, both already redeemed, and a
    scan of every live page for a promised-thyroid-topic sentence comes back
    empty (that scan is part of the check, so a promise appearing later
    fails it rather than passing silently).

(b) THE ENGLISH CROSS-REFERENCE SCAN READS 〈...〉, NOT QUOTE PAIRS.  bl's
    English bodies named sister articles as "Title"; the th English bodies
    use 〈Title〉, the same book-title brackets as the Chinese (HOUSE-STYLE
    line 52, and SPEC-EN 鐵律 4's ban on adding anything the Chinese does
    not have).  So the prose scan is symmetric between the languages --
    an explicit delimiter on both sides -- which is strictly stronger than
    quote-pairing: an unresolved 〈...〉 fails outright instead of having to
    clear a 0.86 similarity ratio.  ALLOW_ZH_ANGLE and ALLOW_EN_ANGLE are
    both empty, and that is a finding: all 78 〈...〉 in the 20 Chinese
    bodies and all 78 in the English ones resolve to a canonical title or a
    live page's own heading.
    bl's quote-pair scan is kept where it is still the right tool: the
    figures' English alt text quotes sister-article titles with "..." (an
    alt attribute is not prose), so en_quoted / near-miss survives verbatim
    for surface (b).

(c) BODY_EDITS IS NON-EMPTY AND IS VERIFIED.  SPEC-EN section 5 requires the
    three off-series English pages to be named by their live <h1> and says
    so has to be re-checked at build time; EN-REPORT-A.md and EN-REPORT-D.md
    record that the writing session could not reach those pages and left
    placeholder strings, flagged as a blocking item.  th.BODY_EDITS makes
    the substitution at build time; check 1 applies the same edits to the
    source before diffing, and check 15 pins each replacement against the
    live page's own <h1> so a stale string cannot pass.

(d) Kept from bl unchanged: check 3's used_by coverage rule (every article a
    figure declares must actually carry it, placement held to used_by as a
    set); the HTML-unescaping of live <title> and <h1> text before
    comparison; and check 13's two-surface design.
"""
import sys

sys.dont_write_bytecode = True      # keep _pipeline/__pycache__ from coming
                                    # back behind check 16

import decimal
import difflib
import filecmp
import html
import json
import os
import re
import subprocess

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import th
import topicbuild as tb

REPO = "/home/claude/repo"
PRE = "/home/claude/th/prebackup"
TH = "/home/claude/th"
NART = 20
NFIG = 12
NSVG = 48
GROUPS = [5, 4, 2, 5, 4]
ORD = [s for sec in th.SECTIONS for s in sec["slugs"]]
LANGS = [("zh", ""), ("en", "-en")]
ART_TPL = {"zh": "cc-first-month.html", "en": "cc-first-month-en.html"}
HUB_TPL = {"zh": "cc.html", "en": "cc-en.html"}
SM_PREV = "bl-daily-en.html"
SM_NEXT = "carc.html"
PREV_CARD = {"zh": "bl.html", "en": "bl-en.html"}
NCARD = 16
SM_BEFORE, SM_AFTER = 832, 874
DISC_ARTS = ["ebrt"]
ANCHOR = {"zh": "先說我的位置", "en": "My position first"}
NEW_PIPELINE = ["build_th.py", "th.py", "th_en.py",
                "stage_th_figs.py", "verify_th.py"]
SHARED = ["sitemap.xml", "topics-en.html", "topics.html"]
NPAGES = 2 + 2 * NART

# The three already-live pages this topic points at (SPEC 修正 54 / SPEC-EN
# section 5).  They are pointed AT, never edited.
OFFSITE = {
    "hn-late-effects.html": "hn-late-effects-en.html",
    "hn-followup.html": "hn-followup-en.html",
    "sit-second-opinion.html": "sit-second-opinion-en.html",
}

# Both empty on purpose -- see the module docstring.  Every 〈...〉 in the 20
# Chinese bodies and the 20 English ones (prose and figure alt alike) is a
# page cross-reference; the guidelines, chapter headings and phrases-not-to-
# use the bodies quote by name are quoted in 「...」 (zh) or "..." (en),
# which this check does not touch.
ALLOW_ZH_ANGLE = set()
ALLOW_EN_ANGLE = set()

hubs = ["th.html", "th-en.html"]
arts = ["th-%s%s.html" % (s, suf) for _, suf in LANGS for s in ORD]
pages = hubs + arts
svgs = sorted(n for n in os.listdir(os.path.join(TH, "figs"))
              if n.endswith(".svg"))
manifest = json.load(open(os.path.join(TH, "figs", "manifest.json"),
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
    """The th fragments keep the th- prefix in BOTH languages, and the
    English ones carry a -en suffix on top of it (the bl / bt convention,
    not em's, whose English fragments carried neither)."""
    if lang == "zh":
        return os.path.join(TH, "body", "th-%s.html" % slug)
    return os.path.join(TH, "en", "th-%s-en.html" % slug)


def src_body(slug, lang):
    """Source body with the module's build-time BODY_EDITS applied -- the
    thing the built page is supposed to equal."""
    body, items, n = tb.split_fragment(rd(src_path(slug, lang)))
    for old, new in th.BODY_EDITS[lang]:
        body = body.replace(old, new)
    return body, items, n


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
RE_TAG = re.compile(r"<[^>]+>")


def vb_height(svg_name):
    m = re.search(r'viewBox="0 0 (\d+(?:\.\d+)?) (\d+(?:\.\d+)?)"',
                  rd(TH, "figs", svg_name))
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
        body, items, n = src_body(slug, lang)
        pb = page_body(rd(REPO, "th-%s%s.html" % (slug, suf)))
        nofig = RE_FIG_STRIP.sub("\n", pb)
        # the figure sits between two sections; stripping it may leave a
        # collapsed blank line, so compare after normalising the separator
        chk(re.sub(r"\n{2,}", "\n\n", nofig).strip()
            == re.sub(r"\n{2,}", "\n\n", body).strip(),
            "th-%s%s body differs from source outside the figure block"
            % (slug, suf))
        chk("<hr>" not in pb, "th-%s%s: <hr> leaked into body" % (slug, suf))
        nh4 = len(re.findall(r"<h4>", pb))
        ncit = len(re.findall(r'<sup class="cit">', pb))
        chk(nh4 == len(re.findall(r"<h4>", body)),
            "th-%s%s: h4 count" % (slug, suf))
        chk(ncit == len(re.findall(r'<sup class="cit">', body)),
            "th-%s%s: citation count" % (slug, suf))
        counts[lang] = (nh4, ncit)
    chk(counts["zh"][0] == counts["en"][0],
        "th-%s: zh %d h4 vs en %d" % (slug, counts["zh"][0], counts["en"][0]))
    chk(counts["zh"][1] == counts["en"][1],
        "th-%s: zh %d citations vs en %d"
        % (slug, counts["zh"][1], counts["en"][1]))
report(1, "body-html == source fragment byte-for-byte after stripping the "
          "inserted <figure> and applying BODY_EDITS (%d zh + %d en); <hr> "
          "never leaks; h4 and citation counts equal the source and equal "
          "each other across languages" % (NART, NART))

# 2 ------------------------------------------------- references item by item --
for slug in ORD:
    for lang, suf in LANGS:
        body, items, n = src_body(slug, lang)
        page = rd(REPO, "th-%s%s.html" % (slug, suf))
        pr = page_refs(page)
        chk(pr == items, "th-%s%s: reference <ol> content differs from source"
            % (slug, suf))
        src_li = re.findall(r"<li>.*?</li>", items, re.S)
        page_li = re.findall(r"<li>.*?</li>", pr, re.S)
        chk(len(src_li) == len(page_li) == n,
            "th-%s%s: %d/%d/%d reference items" % (slug, suf, len(src_li),
                                                   len(page_li), n))
        for k, (a, b) in enumerate(zip(src_li, page_li)):
            chk(a == b, "th-%s%s: reference %d differs" % (slug, suf, k + 1))
        chk("<ol>" not in pr and "<p></p>" not in pr,
            "th-%s%s: nested <ol> or trailing empty <p>" % (slug, suf))
        mm = re.search(r'<div class="meta">(.*?)</div>', page).group(1)
        chk(int(re.search(r"\d+", mm.split(" · ")[2]).group(0)) == n,
            "th-%s%s: meta reference count != %d" % (slug, suf, n))
        nums = [int(x) for x in
                re.findall(r'<sup class="cit">\[(\d+)\]</sup>', page_body(page))]
        first = [v for i, v in enumerate(nums) if v not in nums[:i]]
        chk(first == list(range(1, n + 1)),
            "th-%s%s: [n] markers not 1..%d in first-use order" % (slug, suf, n))
    zn = src_body(slug, "zh")[2]
    en_ = src_body(slug, "en")[2]
    chk(zn == en_, "th-%s: zh %d refs vs en %d" % (slug, zn, en_))
report(2, "reference list == source <ol> item by item on all %d pages; meta "
          "N == count; [n] markers run 1..N in first-use order; zh == en "
          "reference counts" % (2 * NART))

# 3 ------------------------------------------------ figure placement ---------
per = {}
NPLACE = 0
for fig in manifest:
    places = fig["placement"]
    chk(isinstance(places, list) and len(places) >= 1,
        "%s: placement is not a non-empty list" % fig["id"])
    if not isinstance(places, list):
        places = [places]
    pl_arts = [pl["article"] for pl in places]
    chk(sorted(pl_arts) == sorted(fig["used_by"]),
        "%s: placement articles %s != used_by %s"
        % (fig["id"], pl_arts, fig["used_by"]))
    for pl in places:
        per.setdefault(pl["article"], []).append((fig, pl))
    NPLACE += len(places)
chk(len(manifest) == NFIG, "manifest has %d figures, want %d"
    % (len(manifest), NFIG))
nfig = 0
alt_pairs = []
for slug in ORD:
    want = per.get("th-" + slug, [])
    src_h4 = re.findall(r"<h4>(.*?)</h4>", rd(src_path(slug, "zh")))
    want_pos = []
    for f, pl in want:
        chk(pl["after_h4"] in src_h4,
            "%s: after_h4 not found in th-%s" % (f["id"], slug))
        if pl["after_h4"] in src_h4:
            want_pos.append(src_h4.index(pl["after_h4"]) + 1)
    for lang, suf in LANGS:
        body = page_body(rd(REPO, "th-%s%s.html" % (slug, suf)))
        figs = RE_FIG.findall(body)
        chk(len(figs) == len(want), "th-%s%s: %d figures, want %d"
            % (slug, suf, len(figs), len(want)))
        pos, h4 = [], 0
        for m in re.finditer(r'<h4>|<figure class="article-figure">', body):
            if m.group(0) == "<h4>":
                h4 += 1
            else:
                pos.append(h4)
        chk(pos == want_pos, "th-%s%s: figure after h4 #%s, want #%s"
            % (slug, suf, pos, want_pos))
        # the figure closes its section: the next thing after it is an <h4>
        for m in re.finditer(r"</figure>\n+", body):
            chk(body[m.end():m.end() + 4] == "<h4>",
                "th-%s%s: figure is not immediately followed by the next <h4>"
                % (slug, suf))
        for got, (fig, pl) in zip(figs, want):
            alt_pairs.append((lang, slug, fig, got))
        nfig += len(figs)
chk(nfig == NPLACE * 2, "%d figure instances, want %d (%d placements x 2 "
    "languages)" % (nfig, NPLACE * 2, NPLACE))
# EVERY article a figure declares in used_by must actually carry it.  bt
# asserted len(used_by) == 1 instead, which is a bt fact and not a rule: a
# figure drawn to serve two articles is legitimate, but then both of them
# have to receive it.  placement is a LIST here for exactly that reason --
# fig-th-mtc-atc is the two-article figure this round -- and is held to
# used_by as a set above; this block is the independent check, read off the
# built pages rather than off the manifest.
for fig in manifest:
    for art in fig["used_by"]:
        for lang, suf in LANGS:
            want_src = fig["files"]["desktop" if lang == "zh" else "en"]
            p = "%s%s.html" % (art, suf)
            if not os.path.exists(os.path.join(REPO, p)):
                chk(False, "%s: used_by names %s, which is not a page"
                    % (fig["id"], p))
                continue
            chk('src="%s"' % want_src in rd(REPO, p),
                "%s: used_by declares %s but %s carries no such figure "
                "(placement names %s)"
                % (fig["id"], art, p,
                   [q["article"] for q in fig["placement"]]))
report(3, "%d manifest figures -> %d insertions per language, each closing "
          "the h4 section named by its placement.after_h4 (same section index "
          "in en); placement articles == used_by as a set, and every article "
          "a figure declares in used_by actually carries it"
          % (NFIG, NPLACE))

# 4 ---------------------------------------- figure files / alt / caption -----
for lang, slug, fig, got in alt_pairs:
    f = fig["files"]
    mob = f["mobile"] if lang == "zh" else f["en_mobile"]
    dsk = f["desktop"] if lang == "zh" else f["en"]
    raw_alt = fig["zh_alt"] if lang == "zh" else fig["en_alt"]
    raw_cap = fig["zh_caption"] if lang == "zh" else fig["en_caption"]
    tag = "th-%s (%s)" % (slug, lang)
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
          "text-escaped once, all equal to the manifest" % (NPLACE * 2))

# 5 ----------------------------------------------------------- hreflang -------
for slug in ORD + [None]:
    z = "th.html" if slug is None else "th-%s.html" % slug
    en = "th-en.html" if slug is None else "th-%s-en.html" % slug
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
report(5, "hreflang zh-Hant / en / x-default + self-canonical on all %d "
          "pairs, both directions" % (NART + 1))

# 6 -------------------------------------------------------- lang switch ------
for slug in ORD + [None]:
    z = "th.html" if slug is None else "th-%s.html" % slug
    en = "th-en.html" if slug is None else "th-%s-en.html" % slug
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
    chk(ld["about"]["name"] == (th.CONDITION_EN if en else th.CONDITION_ZH),
        "%s about.name %s" % (p, ld["about"]["name"]))
    chk(ld["author"]["@type"] == "Physician", "%s author" % p)
    if p in hubs:
        chk(ld["@type"] == "CollectionPage", "%s type" % p)
        chk(ld["name"] == (th.NAME_EN if en else th.NAME_ZH), "%s name" % p)
        chk([e["url"] for e in ld["hasPart"]]
            == [tb.BASE + "th-%s%s.html" % (s_, "-en" if en else "")
                for s_ in ORD], "%s hasPart urls" % p)
        meta = th.EN if en else th.ART
        chk([e["name"] for e in ld["hasPart"]]
            == [meta[s_]["title"] for s_ in ORD], "%s hasPart names" % p)
    else:
        slug = p[len("th-"):-len(".html")]
        if en:
            slug = slug[:-3]
        meta = (th.EN if en else th.ART)[slug]
        chk(ld["@type"] == "MedicalWebPage", "%s type" % p)
        chk(ld["headline"] == meta["title"], "%s headline" % p)
        chk(ld["description"] == meta["dek"], "%s description" % p)
        chk(ld["datePublished"] == th.DATE
            and ld["dateModified"] == th.DATE, "%s dates" % p)
    chk(s.count('<script type="application/ld+json">') == 1, "%s ld count" % p)
report(7, "JSON-LD parses on all %d pages; @type / url / inLanguage / "
          "about = MedicalCondition %s|%s / headline / dates / hub hasPart "
          "all correct" % (NPAGES, th.CONDITION_ZH, th.CONDITION_EN))

# 8 ---------------------------------------------------- topics pages diff ---
for f, card, hp, href, prev_href in (
        ("topics.html", th.TOPIC_CARD_ZH, th.HASPART_ZH, "th.html",
         PREV_CARD["zh"]),
        ("topics-en.html", th.TOPIC_CARD_EN, th.HASPART_EN,
         "th-en.html", PREV_CARD["en"])):
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
        "%s: JSON-LD line not just extended by the th hasPart entry" % f)
    rest = [l for l in added if '"hasPart":[' not in l]
    chk("".join(rest) == card, "%s: added text is not exactly the th card" % f)
    grid = re.search(r'<div class="topicgrid">(.*?)\n  </div>', now, re.S).group(1)
    cards = re.findall(r'<a class="topiccard" href="([^"]+)"', grid)
    chk(len(cards) == NCARD and cards[-1] == href and cards[-2] == prev_href,
        "%s: card order %s" % (f, cards))
    chk(now.count('class="topiccard"') == pre.count('class="topiccard"') + 1,
        "%s: card count" % f)
    ld, pre_ld = ld_of(now), ld_of(pre)
    chk(ld["hasPart"][:-1] == pre_ld["hasPart"] and ld["hasPart"][-1] == hp,
        "%s: hasPart not old + th" % f)
    chk('<div class="k">%s</div>' % th.KICKER in card, "%s: card kicker" % f)
    chk('<span class="n">%d %s</span>' % (NART, "篇" if f == "topics.html"
                                          else "articles") in card,
        "%s: card count label" % f)
report(8, "topics.html and topics-en.html differ from prebackup by exactly "
          "the th card (after the bl card, %dth) and one appended hasPart "
          "entry; card says %s / %d" % (NCARD, th.KICKER, NART))

# 9 --------------------------------------------------------- sitemap diff ---
sm, pre_sm = rd(REPO, "sitemap.xml"), rd(PRE, "sitemap.xml")
RE_LOC = re.compile(re.escape(tb.BASE) + r"([^<]*)</loc>")
RE_TH = re.compile(r"<loc>%s(th\.html|th-)" % re.escape(tb.BASE))
sml = sm.splitlines()
th_lines = [l for l in sml if RE_TH.search(l)]
kept = [l for l in sml if not RE_TH.search(l)]
chk(kept == pre_sm.splitlines(), "non-th sitemap lines changed or reordered")
chk(not any(RE_TH.search(l) for l in pre_sm.splitlines()),
    "prebackup already had th lines")
chk(pre_sm.count("<url>") == SM_BEFORE, "prebackup <url> = %d, want %d"
    % (pre_sm.count("<url>"), SM_BEFORE))
chk(sm.count("<url>") == SM_AFTER, "sitemap <url> = %d, want %d"
    % (sm.count("<url>"), SM_AFTER))
chk(len(th_lines) == NPAGES, "%d th sitemap lines, want %d"
    % (len(th_lines), NPAGES))
want_order = (["th.html", "th-en.html"] + ["th-%s.html" % s for s in ORD]
              + ["th-%s-en.html" % s for s in ORD])
chk([RE_LOC.search(l).group(1) for l in th_lines] == want_order,
    "th block order is not hub zh, hub en, %d zh, %d en" % (NART, NART))
prio = {"th.html": "0.85", "th-en.html": "0.75"}
prio.update(("th-%s.html" % s, "0.75") for s in ORD)
prio.update(("th-%s-en.html" % s, "0.65") for s in ORD)
for l in th_lines:
    n = RE_LOC.search(l).group(1)
    chk("<priority>%s</priority>" % prio[n] in l, "%s priority" % n)
    chk("<lastmod>%s</lastmod>" % th.DATE in l, "%s lastmod" % n)
    chk("<changefreq>monthly</changefreq>" in l, "%s changefreq" % n)
i_prev = [i for i, l in enumerate(sml)
          if "<loc>%s%s</loc>" % (tb.BASE, SM_PREV) in l]
chk(len(i_prev) == 1, "anchor %s not found once" % SM_PREV)
if i_prev:
    i = i_prev[0]
    chk(all(RE_TH.search(l) for l in sml[i + 1:i + 1 + NPAGES]),
        "th block not contiguous right after %s" % SM_PREV)
    chk("<loc>%s%s</loc>" % (tb.BASE, SM_NEXT) in sml[i + 1 + NPAGES],
        "th block not immediately before %s" % SM_NEXT)
chk("th-th-" not in sm and not any("th-th-" in n for n in os.listdir(REPO)),
    "double-prefixed name somewhere")
report(9, "sitemap differs from prebackup by exactly one contiguous %d-line "
          "block after %s / before %s; <url> %d -> %d; order hub zh, hub en, "
          "%d zh, %d en; priorities 0.85/0.75/0.75/0.65; lastmod %s"
          % (NPAGES, SM_PREV, SM_NEXT, SM_BEFORE, SM_AFTER, NART, NART,
             th.DATE))

# 10 ---------------------------------------------- pages == sitemap adds ----
sm_names = set(m.group(1) for m in RE_LOC.finditer(sm))
pre_names = set(m.group(1) for m in RE_LOC.finditer(pre_sm))
added_names = sm_names - pre_names
chk(len(pages) == NPAGES, "%d pages, want %d" % (len(pages), NPAGES))
chk(added_names == set(pages), "sitemap additions != produced pages: +%s -%s"
    % (sorted(added_names - set(pages)), sorted(set(pages) - added_names)))
chk(len(ORD) == NART and [len(s["slugs"]) for s in th.SECTIONS] == GROUPS,
    "reading order is not %d in %s" % (NART, GROUPS))
chk([len(s["slugs"]) for s in th.SECTIONS_EN] == GROUPS,
    "English group sizes differ from the Chinese")
chk([s["slugs"] for s in th.SECTIONS] == [s["slugs"] for s in th.SECTIONS_EN],
    "zh and en reading orders differ")
chk(len([p for p in arts if p.endswith("-en.html")])
    == len([p for p in arts if not p.endswith("-en.html")]) == NART,
    "zh/en article counts unequal")
repo_html = set(n for n in os.listdir(REPO) if n.endswith(".html"))
chk(all(n in repo_html for n in sm_names if n.endswith(".html")),
    "sitemap URL without a file: %s"
    % sorted(n for n in sm_names if n.endswith(".html") and n not in repo_html))
report(10, "%d pages produced (2 hubs + %d zh + %d en, groups %s, same "
           "order in both languages) == the %d sitemap URLs added; every "
           "sitemap URL has a file"
           % (NPAGES, NART, NART, "/".join(str(g) for g in GROUPS), NPAGES))

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
# th pages specifically: every svg they reference is a th svg
for p in pages:
    s = rd(REPO, p)
    for t in re.findall(r'(?:src|srcset)="([^"]+\.svg)"', s):
        chk(t in svgs, "%s references non-th svg %s" % (p, t))
for n in svgs:
    chk(os.path.exists(os.path.join(REPO, n)), "svg missing in repo: %s" % n)
    chk(filecmp.cmp(os.path.join(TH, "figs", n), os.path.join(REPO, n),
                    shallow=False), "svg differs in repo: %s" % n)
chk(len(svgs) == NSVG, "%d svgs, want %d" % (len(svgs), NSVG))
report(11, "%d internal .html links and %d svg src/srcset across the repo all "
           "resolve (0 broken); the %d th SVGs are byte-identical to "
           "th/figs" % (nlinks, nimg, NSVG))

# 12 --------------------------------------------------------- disclosure ----
for lang, suf in LANGS:
    discs = {}
    for slug in ORD:
        body = page_body(rd(REPO, "th-%s%s.html" % (slug, suf)))
        head = body[:body.index("<h4>")]
        hits = [p_ for p_ in re.findall(r"<p>.*?</p>", head, re.S)
                if ANCHOR[lang] in p_]
        whole = ANCHOR[lang] in body
        if slug in DISC_ARTS:
            chk(len(hits) == 1, "th-%s%s: disclosure missing before first <h4>"
                % (slug, suf))
            chk(body.count(ANCHOR[lang]) == 1,
                "th-%s%s: disclosure anchor appears more than once"
                % (slug, suf))
            if hits:
                discs[slug] = hits[0]
        else:
            chk(not whole, "th-%s%s: disclosure text present but not allowed"
                % (slug, suf))
    chk(len(set(discs.values())) == 1 and len(discs) == len(DISC_ARTS),
        "%s disclosure not found on exactly %s (%d variants)"
        % (lang, DISC_ARTS, len(set(discs.values()))))
    if lang == "en" and discs:
        spec = rd(TH, "SPEC-EN.md")
        want = spec[spec.index("> <p>My position first"):].split("\n", 1)[0][2:] \
            if "> <p>My position first" in spec else None
        if want is None:
            want = "<p>%s</p>" % spec[spec.index("> My position first"):] \
                .split("\n", 1)[0][2:]
        chk(list(discs.values())[0] == want,
            "en disclosure != SPEC-EN.md section 1")
    if lang == "zh" and discs:
        spec = rd(TH, "SPEC.md")
        blk = spec[spec.index("> 先說我的位置"):]
        blk = blk[:blk.index("\n\n")]
        want = "".join(l.lstrip("> ").strip() for l in blk.splitlines())
        chk(list(discs.values())[0] == "<p>%s</p>" % want,
            "zh disclosure != SPEC.md section 二")
report(12, "disclosure paragraph before the first <h4> of exactly th-ebrt "
           "(zh == SPEC 二, en == SPEC-EN 1), absent from the other %d -- "
           "both languages" % (NART - len(DISC_ARTS)))

# 13 ----------------------------------------- titles, meta & cross-references --
for p in arts:
    s = rd(REPO, p)
    en = p.endswith("-en.html")
    slug = p[len("th-"):-len(".html")]
    if en:
        slug = slug[:-3]
    m = (th.EN if en else th.ART)[slug]
    si = [i for i, sec in enumerate(th.SECTIONS) if slug in sec["slugs"]][0]
    chk("<h1>%s</h1>" % tb.esc(m["title"]) in s, "%s h1" % p)
    title = re.search(r"<title>(.*?)</title>", s, re.S).group(1)
    chk(tb.esca(m["title"]) in title, "%s <title>" % p)
    chk(tb.esca(th.NAME_EN if en else th.NAME_ZH) in title,
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
    kicker = th.SECTIONS_EN[si]["en"].upper()
    chk('<div class="kicker">%s</div>' % tb.esc(kicker) in s, "%s kicker" % p)
    sec_name = (th.SECTIONS_EN[si]["en"] if en else th.SECTIONS[si]["zh"])
    mm = re.search(r'<div class="meta">(.*?)</div>', s).group(1).split(" · ")
    chk(mm[0] == (th.NAME_EN if en else th.NAME_ZH) and mm[1] == sec_name,
        "%s meta line %s" % (p, mm))
    chk(('<a href="topics-en.html" class="on">' if en
         else '<a href="topics.html" class="on">') in s, "%s nav active" % p)
    chk('class="backlink" href="%s"' % ("th-en.html" if en else "th.html") in s,
        "%s backlink" % p)
    for k in th.ART[slug]["tags"]:
        chk('href="%s?tag=%s"' % ("th-en.html" if en else "th.html", k) in s,
            "%s tag chip %s" % (p, k))
    # pnav chain
    i = ORD.index(slug)
    pn = re.search(r'<div class="pnav">(.*?)</div>', s, re.S).group(1)
    if i == 0:
        chk(pn.startswith("<span></span>"), "%s first has prev" % p)
    else:
        chk('class="pv" href="th-%s%s.html"' % (ORD[i - 1], "-en" if en else "")
            in pn, "%s prev" % p)
    if i == NART - 1:
        chk(pn.endswith("<span></span>"), "%s last has next" % p)
    else:
        chk('class="nx" href="th-%s%s.html"' % (ORD[i + 1], "-en" if en else "")
            in pn, "%s next" % p)
for lang, page in (("zh", "th.html"), ("en", "th-en.html")):
    s = rd(REPO, page)
    hub = th.HUB if lang == "zh" else th.HUB_EN
    chk("<title>%s</title>" % tb.esca(hub["title"]) in s, "%s title" % page)
    chk('<meta name="description" content="%s">' % tb.esca(hub["desc"]) in s,
        "%s description" % page)
    chk('<div class="kicker">%s</div>' % th.KICKER in s, "%s kicker" % page)
    chk(tb.esc(hub["intro"]) in s or hub["intro"] in s, "%s intro" % page)
    chk(hub["closing"] in s, "%s closing" % page)
    meta_l = th.ART if lang == "zh" else th.EN
    cards = re.findall(r'<a class="postcard" data-tags="([^"]*)" href="([^"]*)"', s)
    chk([c[1] for c in cards] == ["th-%s%s.html" % (s_, "-en" if lang == "en"
                                                    else "") for s_ in ORD],
        "%s card order" % page)
    for slug in ORD:
        chk('<div class="t">%s</div>' % tb.esc(meta_l[slug]["title"]) in s,
            "%s card title %s" % (page, slug))
    grp = re.findall(r'<div class="postgroup hnstep">.*?\n  </div>', s, re.S)
    chk([g.count('class="postcard"') for g in grp] == GROUPS,
        "%s group sizes" % page)
    for si, sec in enumerate(th.SECTIONS):
        nm = sec["zh"] if lang == "zh" else th.SECTIONS_EN[si]["en"]
        chk("<h3><b>%d</b>%s</h3>" % (si + 1, tb.esc(nm)) in s,
            "%s group title %d" % (page, si + 1))
    bar = tb.RE_HUB_TAGC.search(s).group(2)
    cnts = dict((k, int(n)) for k, n in
                re.findall(r'data-tag="([^"]*)">[^<]*<i>(\d+)</i>', bar))
    want = {"": NART}
    for slug in ORD:
        for k in th.ART[slug]["tags"]:
            want[k] = want.get(k, 0) + 1
    chk(cnts == want, "%s tagbar counts %s" % (page, cnts))
    li = 0 if lang == "zh" else 1
    for k, lab in th.LABEL_ADD.items():
        chk('data-tag="%s">#%s <i>' % (k, tb.esc(lab[li])) in bar,
            "%s new label %s" % (page, k))

# cross-reference titles: SPEC 四 (zh) / SPEC-EN section 4 (en), verbatim
zh_titles = set(th.ART[s]["title"] for s in ORD)
en_titles = set(th.EN[s]["title"] for s in ORD)
spec = rd(TH, "SPEC.md")
sec4 = spec[spec.index("## 四、分組與 20 篇"):spec.index("## 五、標題長度")]
spec_zh = dict(re.findall(r"\*\*[A-E]\d+ \`(th-[a-z0-9-]+)\`\*\*〈(.+?)〉", sec4))
chk(len(spec_zh) == NART, "SPEC section 四 lists %d titled slugs, want %d"
    % (len(spec_zh), NART))
for slug in ORD:
    chk(th.ART[slug]["title"] == spec_zh.get("th-" + slug),
        "th-%s title != SPEC section 四" % slug)
sp_en = rd(TH, "SPEC-EN.md")
s4 = sp_en[sp_en.index("## 4. 二十個英文標題"):sp_en.index("## 5. 站外指路")]
spec_en_titles = dict(re.findall(r"\| (th-[a-z0-9-]+) \| (.+?) \|", s4))
chk(len(spec_en_titles) == NART,
    "SPEC-EN section 4 has %d canonical rows" % len(spec_en_titles))
for slug in ORD:
    chk(th.EN[slug]["title"] == spec_en_titles.get("th-" + slug),
        "th-%s en title != SPEC-EN section 4" % slug)

# Live pages this topic may point at, read off the pages themselves so a
# stale spec cannot bless a stale body.  Head text and <h1> are both
# HTML-UNESCAPED before comparison: an apostrophe in a live title reads as
# &#x27; in the head, and the bodies quote titles as prose.
live_h1, live_head, live_h1_en = {}, {}, {}
for n in os.listdir(REPO):
    if not n.endswith(".html") or n == "th.html" or n.startswith("th-"):
        continue
    s = rd(REPO, n)
    m = re.search(r"<h1>(.*?)</h1>", s, re.S)
    if n.endswith("-en.html"):
        if m:
            live_h1_en.setdefault(html.unescape(m.group(1)),
                                  n[:-len("-en.html")] + ".html")
        mt = re.search(r"<title>(.*?)</title>", s, re.S)
        if mt:
            live_head.setdefault(
                html.unescape(re.split(r"[｜|]", mt.group(1))[0].strip()),
                n[:-len("-en.html")] + ".html")
    elif m:
        live_h1.setdefault(m.group(1), n)
zh_key = dict((th.ART[s]["title"], s) for s in ORD)
en_key = dict((th.EN[s]["title"], s) for s in ORD)
known_en = en_titles | set(live_h1_en) | set(live_head)


def en_quoted(text):
    """Every span between two consecutive quote marks, both parities.

    Kept verbatim from verify_bl: the th English FIGURE alt text quotes
    sister-article titles with "..." (an alt attribute is not prose), and a
    plain '"(.{18,110})"' scan pairs quotes left to right and loses a title
    whenever an odd number of scare quotes precedes it."""
    q = [m.start() for m in re.finditer('"', text)]
    return [text[a + 1:b] for a, b in zip(q, q[1:])]


def en_quote_scan(text, where):
    """Count the canonical titles QUOTED in a piece of English text (tags
    already removed, entities already resolved), failing on a near miss."""
    seen = {}
    for q in en_quoted(text):
        if not 18 <= len(q) <= 110:
            continue
        if q in known_en:
            k = en_key.get(q) or live_h1_en.get(q) or live_head[q]
            seen[k] = seen.get(k, 0) + 1
            continue
        ratio, near = max((difflib.SequenceMatcher(None, q, k).ratio(), k)
                          for k in known_en)
        chk(ratio < 0.86,
            "%s: quoted \"%s\" is a near-miss of the canonical \"%s\" (%.2f)"
            % (where, q, near, ratio))
    return seen


def en_scan(text, where):
    """The th English PROSE names sister articles in 〈...〉, exactly as the
    Chinese does (HOUSE-STYLE line 52; SPEC-EN 鐵律 4 forbids the English
    from carrying anything the Chinese does not).  An explicit delimiter on
    both sides makes the two languages' per-article multisets comparable and
    makes an unresolved pointer a failure outright, rather than something
    that has to clear a similarity ratio."""
    seen = {}
    for t in re.findall(r"〈([^〉]*)〉", text):
        if t in known_en:
            k = en_key.get(t) or live_h1_en.get(t) or live_head[t]
            seen[k] = seen.get(k, 0) + 1
            continue
        chk(t in ALLOW_EN_ANGLE,
            "%s: cross-reference 〈%s〉 matches no canonical or live title"
            % (where, t))
    return seen


def zh_scan(body, where):
    seen = {}
    for t in re.findall(r"〈([^〉]*)〉", body):
        if t in zh_titles or t in live_h1:
            k = zh_key.get(t) or live_h1[t]
            seen[k] = seen.get(k, 0) + 1
            continue
        chk(t in ALLOW_ZH_ANGLE,
            "%s: cross-reference 〈%s〉 matches no canonical title" % (where, t))
    return seen


# (a) prose.  The <figure> blocks are stripped in BOTH languages so that the
#     per-article multisets are comparable.
n_zh_xref = n_en_xref = 0
zh_refs, en_refs = {}, {}
for slug in ORD:
    body = RE_FIG_STRIP.sub("\n", page_body(rd(REPO, "th-%s.html" % slug)))
    zh_refs[slug] = zh_scan(body, "th-%s" % slug)
    n_zh_xref += sum(zh_refs[slug].values())
for slug in ORD:
    body = RE_FIG_STRIP.sub("\n", page_body(rd(REPO, "th-%s-en.html" % slug)))
    # the th bodies wrap every citation in <a href="https://...">, so the
    # pointer text is read out of the TEXT, not the markup
    en_refs[slug] = en_scan(html.unescape(RE_TAG.sub("", body)),
                            "th-%s-en" % slug)
    n_en_xref += sum(en_refs[slug].values())
# the two languages must point at the same pages, the same number of times
for slug in ORD:
    chk(zh_refs[slug] == en_refs[slug],
        "th-%s: cross-references differ between languages, zh %s vs en %s"
        % (slug, sorted(zh_refs[slug].items()), sorted(en_refs[slug].items())))
chk(n_zh_xref >= NART and n_en_xref >= NART,
    "suspiciously few cross-references found (zh %d, en %d)"
    % (n_zh_xref, n_en_xref))

# (b) the inserted figures.  A title named inside a figure's alt text or
#     caption is a cross-reference like any other and is held to the same
#     canonical rule, in both languages -- 〈...〉 in the Chinese alt, "..."
#     in the English one.
n_zh_fig = n_en_fig = 0
for slug in ORD:
    for lang, suf in LANGS:
        body = page_body(rd(REPO, "th-%s%s.html" % (slug, suf)))
        for m in re.finditer(
                r'<figure class="article-figure">.*?</figure>', body, re.S):
            blk = m.group(0)
            alt = html.unescape(re.search(r'alt="([^"]*)"', blk).group(1))
            cap = html.unescape(re.search(r"<figcaption>(.*?)</figcaption>",
                                          blk, re.S).group(1))
            where = "th-%s%s figure" % (slug, suf)
            if lang == "zh":
                n_zh_fig += sum(zh_scan(alt + "\n" + cap, where).values())
            else:
                n_en_fig += sum(
                    en_quote_scan(alt + "\n" + cap, where).values())
report(13, "h1 / <title> / og:title / description / dek / lead / note / "
           "kicker / meta line / tag chips / pnav chain == meta & module on "
           "all %d articles; hub title/desc/intro/closing, 5 groups %s, "
           "card titles = meta titles, tag counts = card counts, new labels "
           "%s rendered; %d zh and %d en cross-reference titles in prose "
           "(plus %d zh / %d en inside figure alt and caption text) are "
           "verbatim SPEC 四 / SPEC-EN 4 or a live page's own heading, none "
           "unresolved, and every article points at the same pages the same "
           "number of times in both languages"
           % (2 * NART, "/".join(str(g) for g in GROUPS),
              " + ".join(sorted(th.LABEL_ADD)), n_zh_xref, n_en_xref,
              n_zh_fig, n_en_fig))

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
        chk(skeleton(rd(REPO, "th-%s%s.html" % (slug, suf))) == t,
            "th-%s%s: skeleton differs from %s" % (slug, suf, ART_TPL[lang]))
for lang, page in (("zh", "th.html"), ("en", "th-en.html")):
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
           "<style> byte-identical on all %d (figure css present once); "
           "head/body tags once; no double-escaped entities" % NPAGES)

# 15 ------------------------------- no pre-existing page is edited ----------
# bl's slot here pinned the five pel-who substitutions.  This round makes no
# such edit, so the check states the stronger fact instead, read off git
# rather than off a prebackup of two hand-picked files.
new_files = set(pages) | set(svgs) | set("_pipeline/" + n for n in NEW_PIPELINE)
diffed = sorted(
    l for l in subprocess.run(
        ["git", "-C", REPO, "diff", "--name-only", "HEAD"],
        capture_output=True, text=True).stdout.splitlines() if l)
chk(diffed == SHARED,
    "tracked files differing from HEAD: %s, want exactly %s"
    % (diffed, SHARED))
# and nothing at all is declared that would edit a published page
chk(not hasattr(th, "PEL_WHO_EDITS"),
    "th still carries bl's PEL_WHO_EDITS machinery")
chk(th.BODY_EDITS["zh"] == [],
    "th.BODY_EDITS['zh'] is not empty: %s" % th.BODY_EDITS["zh"])
src = rd(os.path.join(REPO, "_pipeline", "build_th.py"))
# the machinery, not the prose: both files explain in their docstrings why
# bl's chore is gone, so the test is for a definition, a call or an attribute
# reference, never for the words.
chk(re.search(r"^\s*def patch_pel_who", src, re.M) is None
    and "patch_pel_who(" not in src and "th.PEL_WHO_EDITS" not in src
    and "PEL_WHO_EDITS.items()" not in src,
    "build_th.py still carries chore machinery")
chk(tuple(sorted(re.search(r"^SHARED = \((.*?)\)", src, re.S | re.M)
                 .group(1).replace("\n", " ").split(", ")))
    == tuple(sorted('"%s"' % n for n in SHARED)),
    "build_th.py's SHARED is not the three index files")
# the three off-series pages this topic points at: untouched, and named by
# their own live <h1> on both sides
for zf, ef in sorted(OFFSITE.items()):
    for f in (zf, ef):
        chk(os.path.exists(os.path.join(REPO, f)), "off-series page missing: %s"
            % f)
        chk(f not in diffed, "off-series page %s was modified" % f)
        chk('href="th.html"' not in rd(REPO, f)
            and 'href="th-' not in rd(REPO, f),
            "%s: a th link was added -- this round points in sense only" % f)
# BODY_EDITS: three English placeholder pointers replaced by the live <h1>
chk(len(th.BODY_EDITS["en"]) == 3,
    "%d English BODY_EDITS declared, want 3" % len(th.BODY_EDITS["en"]))
live_targets = {}
for zf, ef in OFFSITE.items():
    live_targets[html.unescape(
        re.search(r"<h1>(.*?)</h1>", rd(REPO, ef), re.S).group(1))] = ef
for old, new in th.BODY_EDITS["en"]:
    t = new.strip("〈〉")
    chk(t in live_targets,
        "BODY_EDITS replacement 〈%s〉 is not the live <h1> of any of the "
        "off-series pages %s" % (t, sorted(OFFSITE.values())))
    n_old = sum(rd(src_path(s, "en")).count(old) for s in ORD)
    chk(n_old == 1, "BODY_EDITS anchor %r occurs %d times in the English "
                    "sources, want 1" % (old, n_old))
    hits = sum(page_body(rd(REPO, "th-%s-en.html" % s)).count(new)
               for s in ORD)
    chk(hits == 1, "replacement %r appears %d times in the built English "
                   "pages, want 1" % (new, hits))
    chk(all(old not in page_body(rd(REPO, "th-%s-en.html" % s)) for s in ORD),
        "placeholder %r survives in a built page" % old)
# the Chinese pointers needed no edit: they already equal the live <h1>
for zf in OFFSITE:
    h1 = re.search(r"<h1>(.*?)</h1>", rd(REPO, zf), re.S).group(1)
    chk(any("〈%s〉" % h1 in rd(src_path(s, "zh")) for s in ORD),
        "no Chinese body names %s by its live <h1> 〈%s〉" % (zf, h1))
# and no live page was left promising a thyroid topic this round should have
# redeemed (the premise of "no chore", checked rather than inherited)
promises = []
for n in sorted(os.listdir(REPO)):
    if not n.endswith(".html") or n in new_files:
        continue
    s = rd(REPO, n)
    for m in re.finditer(r"[^。；\n]{0,40}甲狀腺[^。；\n]{0,40}", s):
        seg = m.group(0)
        if "另有專題" in seg or "規劃中" in seg or "專題規劃" in seg:
            promises.append((n, seg))
    for m in re.finditer(r"[^.\n]{0,60}thyroid[^.\n]{0,60}", s, re.I):
        seg = m.group(0)
        if "being planned" in seg or "separate topic" in seg.lower():
            promises.append((n, seg))
chk(not promises,
    "a live page promises a thyroid topic, so this round DID have a chore: %s"
    % promises[:4])
report(15, "the topic adds no edit to any pre-existing page: git diff against "
           "HEAD is exactly %s; no chore machinery is declared (BODY_EDITS "
           "rewrites only this topic's own English fragments, three "
           "placeholder pointers -> the live <h1> of %s); those pages are "
           "untouched and carry no th link; and no live page was left "
           "promising a thyroid topic"
           % (", ".join(SHARED), ", ".join(sorted(OFFSITE.values()))))

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
chk(not head.lower().startswith("th") and "th:" not in head.lower()
    and "甲狀腺癌" not in head,
    "HEAD looks like a th commit -- this round is local only: %r" % head)
report(16, "git status: exactly %s modified; untracked = %d pages + %d svgs + "
           "5 _pipeline modules; nothing staged, nothing committed"
           % (", ".join(SHARED), NPAGES, NSVG))

print()
nfail = sum(1 for r in results if not r[2])
if nfail:
    print("FAILED: %d of %d checks" % (nfail, len(results)))
    sys.exit(1)
print("ALL %d CHECKS PASSED" % len(results))
