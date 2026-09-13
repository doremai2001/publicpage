# -*- coding: utf-8 -*-
"""Verification pass over the generated benign-brain-tumour pages.

The cervix / liver / pel / esoph / gbm / endo standard, printed as one
PASS/FAIL line per check:

  1  body text == source fragment byte-for-byte once the inserted <figure>
     blocks are stripped (zh and en, all 21); <hr> never leaks; h4 and
     citation counts equal source AND equal between zh and en
  2  reference list == source <ol> item by item; meta N == count; [n]
     markers run 1..N in first-use order; zh == en reference counts
  3  figure position per manifest after_h4 (same section index in en)
  4  figure files / alt / caption / height per manifest, escaped exactly once
  5  hreflang zh-Hant / en / x-default + canonical, both directions
  6  language switch chip points at the partner page, both directions
  7  JSON-LD parses on every page; about / name / url / inLanguage / dates
  8  topics.html and topics-en.html differ from prebackup by exactly one
     card (14th, after the em one) and one appended hasPart entry
  9  sitemap differs from prebackup by exactly the new contiguous block
     (after em-daily-en.html, before carc.html), 750 -> 794, priorities
 10  pages produced (44) == sitemap URLs added; every page in the sitemap;
     21 zh == 21 en, groups 4/5/3/4/5
 11  every internal .html link and svg src/srcset in the repo resolves; the
     48 SVGs are byte-identical to /home/claude/bt/figs
 12  the disclosure paragraph sits before the first <h4> of exactly
     bt-mg-rt / bt-mg-adjuvant / bt-an-choice / bt-pit-surgery-rt,
     byte-identical across the four (zh == SPEC.md 二, en == SPEC-EN 1), and
     appears in no other article
 13  h1 / <title> / og:title / description / ld headline == meta title & dek;
     hub card titles == meta titles; hub tag counts consistent; every
     cross-reference title is verbatim 修正 21 / SPEC-EN section 4 or a live
     page's own title, with no near-miss variant; SPEC-EN section 4's
     seventeen "existing site page" titles still equal those pages' own
     live <title> head
 14  every byte outside the substituted slots equals the cc template; style
     identical across the 44 pages; no double-escaped entities
 15  gb-what-it-is.html and gb-what-it-is-en.html differ from prebackup by
     exactly the two GB_WHAT_EDITS substitutions each (four in all); exactly
     one anchor added per file -- the first pointer's link to the bt hub, in
     this page's own lc-brainmet form -- the second pointer unlinked, the
     pre-existing lc-brainmet link untouched, nothing else moves
 16  git status shows only the expected new files and the five shared
     modifications -- nothing staged, nothing committed

Note on the gb-what-it-is chore: unlike endo's pel-who chore (three mirrored
pairs, three changed lines per file), both bt substitutions land inside the
SAME paragraph -- gb-what-it-is line 497 in both languages -- so the pinned
shape is ONE changed line carrying TWO substitutions per file, four in all.
The sentence that promised a meningioma topic ("作者另開專題" / "the author
is giving it a topic of its own") now names 〈良性腦瘤專題〉 /
"Benign Brain Tumour Guide", and the sentence that dismissed pituitary
tumours and acoustic neuroma ("這兩個都不是這個專題在講的東西" / "Neither of
those is what this topic is about") now says where they are covered.

THE LINK QUESTION, checked rather than inherited -- a future round should
take this fact from here and not from the endo round.  pel-who, endo's chore
page, carried ZERO in-body site links, so 修正 20 pointed in sense only.
gb-what-it-is is not that page: one sentence above the first edit, in the
same block of paragraphs, it already points at another site page AS A LINK,
〈<a href="lc-brainmet.html">腦轉移不等於末期</a>〉 in Chinese and <a
href="lc-brainmet-en.html">Brain metastases are not the end</a> in English.
A LINKED title is therefore this page's own house style for an on-site
pointer.  The first round of this chore copied pel-who's "everything is
unlinked" premise without re-checking it; the editorial ruling that followed
put the <a> back on the FIRST pointer, in exactly the lc-brainmet form, and
left the SECOND pointer -- the next sentence of the same paragraph -- plain,
so the paragraph does not carry the same href twice.  Check 15 pins both
halves of that ruling plus the shape of the whole diff: exactly one anchor
added per file, the in-body site-link list going from [lc-brainmet] to
[lc-brainmet, bt] in order, the topic named twice per file with exactly one
of those occurrences inside an <a>, and the pre-existing lc-brainmet link
untouched.

ALLOW_ZH_ANGLE is EMPTY for this topic, and that is a finding rather than an
omission: every 〈...〉 in all 21 Chinese bodies resolves to either a 修正 21
canonical title or a live page's own <h1>.  The bt bodies do quote source
documents' own titles, but they do so inside 「...」 (and, for English
journal titles, in Latin script without 〈 〉), so no non-cross-reference
〈...〉 exists to allow-list.  See the note above check 13.

Four deliberate deviations from verify_endo.py.  Three are in check 13 and
all three are strictly stronger rather than weaker:
  * the quoted-string scan runs over the body with its tags removed, not the
    raw markup.  The bt bodies carry inline <a href="https://..."> around
    every citation (the em bodies did not), so the raw regex would have
    harvested the URL attribute values and the stray text between one tag's
    closing quote and the next tag's opening quote as if they were quoted
    prose.
  * the scan walks consecutive quote PAIRS instead of regex-matching
    '"(.{18,110})"', which pairs quotes left to right and so loses any title
    sitting behind an odd number of scare quotes in the same paragraph.  The
    two fixes together find 97 quoted cross-references where endo's scan
    found 69, and the 28 it recovered include a real one:
    bt-mg-grade-en's second pointer at "Three tumours, three different
    logics", hidden behind 'What "benign" and "malignant" each mean...'.
  * SPEC-EN section 4's seventeen pointer titles are themselves re-checked
    against the live -en.html pages they name, and every article's set of
    cross-references must be the same in both languages (same pages, same
    number of times) -- 97 zh and 97 en, symmetric across all 21.
The fourth is check 15's in-body-link invariant, which pins one added anchor
and an unchanged pre-existing one rather than endo's "zero in-body links";
see THE LINK QUESTION above for why that is the truthful pin, not a weaker
one.
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
import bt
import topicbuild as tb

REPO = "/home/claude/repo"
PRE = "/home/claude/bt/prebackup"
BT = "/home/claude/bt"
NART = 21
NFIG = 12
NSVG = 48
GROUPS = [4, 5, 3, 4, 5]
ORD = [s for sec in bt.SECTIONS for s in sec["slugs"]]
LANGS = [("zh", ""), ("en", "-en")]
ART_TPL = {"zh": "cc-first-month.html", "en": "cc-first-month-en.html"}
HUB_TPL = {"zh": "cc.html", "en": "cc-en.html"}
SM_PREV = "em-daily-en.html"
SM_NEXT = "carc.html"
PREV_CARD = {"zh": "em.html", "en": "em-en.html"}
NCARD = 14
SM_BEFORE, SM_AFTER = 750, 794
DISC_ARTS = ["mg-rt", "mg-adjuvant", "an-choice", "pit-surgery-rt"]
ANCHOR = {"zh": "先說我的位置", "en": "My position first"}
NEW_PIPELINE = ["build_bt.py", "bt.py", "bt_en.py",
                "stage_bt_figs.py", "verify_bt.py"]
SHARED = ["gb-what-it-is-en.html", "gb-what-it-is.html", "sitemap.xml",
          "topics-en.html", "topics.html"]

# Empty on purpose -- see the module docstring.  Every 〈...〉 in the 21
# Chinese bodies is a page cross-reference; the source documents the bodies
# quote by name are quoted in 「...」, which this check does not touch.
ALLOW_ZH_ANGLE = set()

hubs = ["bt.html", "bt-en.html"]
arts = ["bt-%s%s.html" % (s, suf) for _, suf in LANGS for s in ORD]
pages = hubs + arts
svgs = sorted(n for n in os.listdir(os.path.join(BT, "figs"))
              if n.endswith(".svg"))
manifest = json.load(open(os.path.join(BT, "figs", "manifest.json"),
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
    """The bt fragments keep the bt- prefix in BOTH languages, and the
    English ones carry a -en suffix on top of it (unlike em, whose English
    fragments carried neither suffix, only a different directory)."""
    if lang == "zh":
        return os.path.join(BT, "body", "bt-%s.html" % slug)
    return os.path.join(BT, "en", "bt-%s-en.html" % slug)


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
                  rd(BT, "figs", svg_name))
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
        pb = page_body(rd(REPO, "bt-%s%s.html" % (slug, suf)))
        nofig = RE_FIG_STRIP.sub("\n", pb)
        # the figure sits between two sections; stripping it may leave a
        # collapsed blank line, so compare after normalising the separator
        chk(re.sub(r"\n{2,}", "\n\n", nofig).strip()
            == re.sub(r"\n{2,}", "\n\n", body).strip(),
            "bt-%s%s body differs from source outside the figure block"
            % (slug, suf))
        chk("<hr>" not in pb, "bt-%s%s: <hr> leaked into body" % (slug, suf))
        nh4 = len(re.findall(r"<h4>", pb))
        ncit = len(re.findall(r'<sup class="cit">', pb))
        chk(nh4 == len(re.findall(r"<h4>", body)),
            "bt-%s%s: h4 count" % (slug, suf))
        chk(ncit == len(re.findall(r'<sup class="cit">', body)),
            "bt-%s%s: citation count" % (slug, suf))
        counts[lang] = (nh4, ncit)
    chk(counts["zh"][0] == counts["en"][0],
        "bt-%s: zh %d h4 vs en %d" % (slug, counts["zh"][0], counts["en"][0]))
    chk(counts["zh"][1] == counts["en"][1],
        "bt-%s: zh %d citations vs en %d"
        % (slug, counts["zh"][1], counts["en"][1]))
report(1, "body-html == source fragment byte-for-byte after stripping the "
          "inserted <figure> (21 zh + 21 en); <hr> never leaks; h4 and "
          "citation counts equal the source and equal each other across "
          "languages")

# 2 ------------------------------------------------- references item by item --
for slug in ORD:
    for lang, suf in LANGS:
        body, items, n = tb.split_fragment(rd(src_path(slug, lang)))
        page = rd(REPO, "bt-%s%s.html" % (slug, suf))
        pr = page_refs(page)
        chk(pr == items, "bt-%s%s: reference <ol> content differs from source"
            % (slug, suf))
        src_li = re.findall(r"<li>.*?</li>", items, re.S)
        page_li = re.findall(r"<li>.*?</li>", pr, re.S)
        chk(len(src_li) == len(page_li) == n,
            "bt-%s%s: %d/%d/%d reference items" % (slug, suf, len(src_li),
                                                   len(page_li), n))
        for k, (a, b) in enumerate(zip(src_li, page_li)):
            chk(a == b, "bt-%s%s: reference %d differs" % (slug, suf, k + 1))
        chk("<ol>" not in pr and "<p></p>" not in pr,
            "bt-%s%s: nested <ol> or trailing empty <p>" % (slug, suf))
        mm = re.search(r'<div class="meta">(.*?)</div>', page).group(1)
        chk(int(re.search(r"\d+", mm.split(" · ")[2]).group(0)) == n,
            "bt-%s%s: meta reference count != %d" % (slug, suf, n))
        nums = [int(x) for x in
                re.findall(r'<sup class="cit">\[(\d+)\]</sup>', page_body(page))]
        first = [v for i, v in enumerate(nums) if v not in nums[:i]]
        chk(first == list(range(1, n + 1)),
            "bt-%s%s: [n] markers not 1..%d in first-use order" % (slug, suf, n))
    zn = tb.split_fragment(rd(src_path(slug, "zh")))[2]
    en_ = tb.split_fragment(rd(src_path(slug, "en")))[2]
    chk(zn == en_, "bt-%s: zh %d refs vs en %d" % (slug, zn, en_))
report(2, "reference list == source <ol> item by item on all 42 pages; meta "
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
    want = per.get("bt-" + slug, [])
    src_h4 = re.findall(r"<h4>(.*?)</h4>", rd(src_path(slug, "zh")))
    want_pos = []
    for f in want:
        chk(f["placement"]["after_h4"] in src_h4,
            "%s: after_h4 not found in bt-%s" % (f["id"], slug))
        if f["placement"]["after_h4"] in src_h4:
            want_pos.append(src_h4.index(f["placement"]["after_h4"]) + 1)
    for lang, suf in LANGS:
        body = page_body(rd(REPO, "bt-%s%s.html" % (slug, suf)))
        figs = RE_FIG.findall(body)
        chk(len(figs) == len(want), "bt-%s%s: %d figures, want %d"
            % (slug, suf, len(figs), len(want)))
        pos, h4 = [], 0
        for m in re.finditer(r'<h4>|<figure class="article-figure">', body):
            if m.group(0) == "<h4>":
                h4 += 1
            else:
                pos.append(h4)
        chk(pos == want_pos, "bt-%s%s: figure after h4 #%s, want #%s"
            % (slug, suf, pos, want_pos))
        # the figure closes its section: the next thing after it is an <h4>
        for m in re.finditer(r"</figure>\n+", body):
            chk(body[m.end():m.end() + 4] == "<h4>",
                "bt-%s%s: figure is not immediately followed by the next <h4>"
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
    tag = "bt-%s (%s)" % (slug, lang)
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
    z = "bt.html" if slug is None else "bt-%s.html" % slug
    en = "bt-en.html" if slug is None else "bt-%s-en.html" % slug
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
report(5, "hreflang zh-Hant / en / x-default + self-canonical on all 22 "
          "pairs, both directions")

# 6 -------------------------------------------------------- lang switch ------
for slug in ORD + [None]:
    z = "bt.html" if slug is None else "bt-%s.html" % slug
    en = "bt-en.html" if slug is None else "bt-%s-en.html" % slug
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
    chk(ld["about"]["name"] == (bt.CONDITION_EN if en else bt.CONDITION_ZH),
        "%s about.name %s" % (p, ld["about"]["name"]))
    chk(ld["author"]["@type"] == "Physician", "%s author" % p)
    if p in hubs:
        chk(ld["@type"] == "CollectionPage", "%s type" % p)
        chk(ld["name"] == (bt.NAME_EN if en else bt.NAME_ZH), "%s name" % p)
        chk([e["url"] for e in ld["hasPart"]]
            == [tb.BASE + "bt-%s%s.html" % (s_, "-en" if en else "")
                for s_ in ORD], "%s hasPart urls" % p)
        meta = bt.EN if en else bt.ART
        chk([e["name"] for e in ld["hasPart"]]
            == [meta[s_]["title"] for s_ in ORD], "%s hasPart names" % p)
    else:
        slug = p[len("bt-"):-len(".html")]
        if en:
            slug = slug[:-3]
        meta = (bt.EN if en else bt.ART)[slug]
        chk(ld["@type"] == "MedicalWebPage", "%s type" % p)
        chk(ld["headline"] == meta["title"], "%s headline" % p)
        chk(ld["description"] == meta["dek"], "%s description" % p)
        chk(ld["datePublished"] == bt.DATE
            and ld["dateModified"] == bt.DATE, "%s dates" % p)
    chk(s.count('<script type="application/ld+json">') == 1, "%s ld count" % p)
report(7, "JSON-LD parses on all 44 pages; @type / url / inLanguage / "
          "about = MedicalCondition %s|%s / headline / dates / hub hasPart "
          "all correct" % (bt.CONDITION_ZH, bt.CONDITION_EN))

# 8 ---------------------------------------------------- topics pages diff ---
for f, card, hp, href, prev_href in (
        ("topics.html", bt.TOPIC_CARD_ZH, bt.HASPART_ZH, "bt.html",
         PREV_CARD["zh"]),
        ("topics-en.html", bt.TOPIC_CARD_EN, bt.HASPART_EN,
         "bt-en.html", PREV_CARD["en"])):
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
        "%s: JSON-LD line not just extended by the bt hasPart entry" % f)
    rest = [l for l in added if '"hasPart":[' not in l]
    chk("".join(rest) == card, "%s: added text is not exactly the bt card" % f)
    grid = re.search(r'<div class="topicgrid">(.*?)\n  </div>', now, re.S).group(1)
    cards = re.findall(r'<a class="topiccard" href="([^"]+)"', grid)
    chk(len(cards) == NCARD and cards[-1] == href and cards[-2] == prev_href,
        "%s: card order %s" % (f, cards))
    chk(now.count('class="topiccard"') == pre.count('class="topiccard"') + 1,
        "%s: card count" % f)
    ld, pre_ld = ld_of(now), ld_of(pre)
    chk(ld["hasPart"][:-1] == pre_ld["hasPart"] and ld["hasPart"][-1] == hp,
        "%s: hasPart not old + bt" % f)
    chk('<div class="k">%s</div>' % bt.KICKER in card, "%s: card kicker" % f)
    chk('<span class="n">%d %s</span>' % (NART, "篇" if f == "topics.html"
                                          else "articles") in card,
        "%s: card count label" % f)
report(8, "topics.html and topics-en.html differ from prebackup by exactly "
          "the bt card (after the em card, %dth) and one appended hasPart "
          "entry; card says %s / %d" % (NCARD, bt.KICKER, NART))

# 9 --------------------------------------------------------- sitemap diff ---
sm, pre_sm = rd(REPO, "sitemap.xml"), rd(PRE, "sitemap.xml")
RE_LOC = re.compile(re.escape(tb.BASE) + r"([^<]*)</loc>")
RE_BT = re.compile(r"<loc>%s(bt\.html|bt-)" % re.escape(tb.BASE))
sml = sm.splitlines()
bt_lines = [l for l in sml if RE_BT.search(l)]
kept = [l for l in sml if not RE_BT.search(l)]
chk(kept == pre_sm.splitlines(), "non-bt sitemap lines changed or reordered")
chk(not any(RE_BT.search(l) for l in pre_sm.splitlines()),
    "prebackup already had bt lines")
chk(pre_sm.count("<url>") == SM_BEFORE, "prebackup <url> = %d, want %d"
    % (pre_sm.count("<url>"), SM_BEFORE))
chk(sm.count("<url>") == SM_AFTER, "sitemap <url> = %d, want %d"
    % (sm.count("<url>"), SM_AFTER))
chk(len(bt_lines) == 44, "%d bt sitemap lines, want 44" % len(bt_lines))
want_order = (["bt.html", "bt-en.html"] + ["bt-%s.html" % s for s in ORD]
              + ["bt-%s-en.html" % s for s in ORD])
chk([RE_LOC.search(l).group(1) for l in bt_lines] == want_order,
    "bt block order is not hub zh, hub en, 21 zh, 21 en")
prio = {"bt.html": "0.85", "bt-en.html": "0.75"}
prio.update(("bt-%s.html" % s, "0.75") for s in ORD)
prio.update(("bt-%s-en.html" % s, "0.65") for s in ORD)
for l in bt_lines:
    n = RE_LOC.search(l).group(1)
    chk("<priority>%s</priority>" % prio[n] in l, "%s priority" % n)
    chk("<lastmod>%s</lastmod>" % bt.DATE in l, "%s lastmod" % n)
    chk("<changefreq>monthly</changefreq>" in l, "%s changefreq" % n)
i_prev = [i for i, l in enumerate(sml)
          if "<loc>%s%s</loc>" % (tb.BASE, SM_PREV) in l]
chk(len(i_prev) == 1, "anchor %s not found once" % SM_PREV)
if i_prev:
    i = i_prev[0]
    chk(all(RE_BT.search(l) for l in sml[i + 1:i + 45]),
        "bt block not contiguous right after %s" % SM_PREV)
    chk("<loc>%s%s</loc>" % (tb.BASE, SM_NEXT) in sml[i + 45],
        "bt block not immediately before %s" % SM_NEXT)
chk("bt-bt-" not in sm and not any("bt-bt-" in n for n in os.listdir(REPO)),
    "double-prefixed name somewhere")
report(9, "sitemap differs from prebackup by exactly one contiguous 44-line "
          "block after %s / before %s; <url> %d -> %d; order hub zh, hub en, "
          "21 zh, 21 en; priorities 0.85/0.75/0.75/0.65; lastmod %s"
          % (SM_PREV, SM_NEXT, SM_BEFORE, SM_AFTER, bt.DATE))

# 10 ---------------------------------------------- pages == sitemap adds ----
sm_names = set(m.group(1) for m in RE_LOC.finditer(sm))
pre_names = set(m.group(1) for m in RE_LOC.finditer(pre_sm))
added_names = sm_names - pre_names
chk(len(pages) == 44, "%d pages, want 44" % len(pages))
chk(added_names == set(pages), "sitemap additions != produced pages: +%s -%s"
    % (sorted(added_names - set(pages)), sorted(set(pages) - added_names)))
chk(len(ORD) == NART and [len(s["slugs"]) for s in bt.SECTIONS] == GROUPS,
    "reading order is not %d in %s" % (NART, GROUPS))
chk([len(s["slugs"]) for s in bt.SECTIONS_EN] == GROUPS,
    "English group sizes differ from the Chinese")
chk([s["slugs"] for s in bt.SECTIONS] == [s["slugs"] for s in bt.SECTIONS_EN],
    "zh and en reading orders differ")
chk(len([p for p in arts if p.endswith("-en.html")])
    == len([p for p in arts if not p.endswith("-en.html")]) == NART,
    "zh/en article counts unequal")
repo_html = set(n for n in os.listdir(REPO) if n.endswith(".html"))
chk(all(n in repo_html for n in sm_names if n.endswith(".html")),
    "sitemap URL without a file: %s"
    % sorted(n for n in sm_names if n.endswith(".html") and n not in repo_html))
report(10, "44 pages produced (2 hubs + 21 zh + 21 en, groups 4/5/3/4/5, same "
           "order in both languages) == the 44 sitemap URLs added; every "
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
# bt pages specifically: every svg they reference is a bt svg
for p in pages:
    s = rd(REPO, p)
    for t in re.findall(r'(?:src|srcset)="([^"]+\.svg)"', s):
        chk(t in svgs, "%s references non-bt svg %s" % (p, t))
for n in svgs:
    chk(os.path.exists(os.path.join(REPO, n)), "svg missing in repo: %s" % n)
    chk(filecmp.cmp(os.path.join(BT, "figs", n), os.path.join(REPO, n),
                    shallow=False), "svg differs in repo: %s" % n)
chk(len(svgs) == NSVG, "%d svgs, want %d" % (len(svgs), NSVG))
report(11, "%d internal .html links and %d svg src/srcset across the repo all "
           "resolve (0 broken); the %d bt SVGs are byte-identical to "
           "bt/figs" % (nlinks, nimg, NSVG))

# 12 --------------------------------------------------------- disclosure ----
for lang, suf in LANGS:
    discs = {}
    for slug in ORD:
        body = page_body(rd(REPO, "bt-%s%s.html" % (slug, suf)))
        head = body[:body.index("<h4>")]
        hits = [p_ for p_ in re.findall(r"<p>.*?</p>", head, re.S)
                if ANCHOR[lang] in p_]
        whole = ANCHOR[lang] in body
        if slug in DISC_ARTS:
            chk(len(hits) == 1, "bt-%s%s: disclosure missing before first <h4>"
                % (slug, suf))
            chk(body.count(ANCHOR[lang]) == 1,
                "bt-%s%s: disclosure anchor appears more than once"
                % (slug, suf))
            if hits:
                discs[slug] = hits[0]
        else:
            chk(not whole, "bt-%s%s: disclosure text present but not allowed"
                % (slug, suf))
    chk(len(set(discs.values())) == 1 and len(discs) == 4,
        "%s disclosure not byte-identical across B3/B4/C2/D3 (%d variants)"
        % (lang, len(set(discs.values()))))
    if lang == "en" and discs:
        spec = rd(BT, "SPEC-EN.md")
        want = spec[spec.index("> <p>My position first"):].split("\n", 1)[0][2:]
        chk(list(discs.values())[0] == want,
            "en disclosure != SPEC-EN.md section 1")
    if lang == "zh" and discs:
        spec = rd(BT, "SPEC.md")
        blk = spec[spec.index("> 先說我的位置"):]
        blk = blk[:blk.index("\n\n")]
        want = "".join(l.lstrip("> ").strip() for l in blk.splitlines())
        chk(list(discs.values())[0] == "<p>%s</p>" % want,
            "zh disclosure != SPEC.md section 二")
report(12, "disclosure paragraph before the first <h4> of exactly bt-mg-rt / "
           "bt-mg-adjuvant / bt-an-choice / bt-pit-surgery-rt, "
           "byte-identical across the four (zh == SPEC 二, en == SPEC-EN 1), "
           "absent from the other 17 -- both languages")

# 13 ----------------------------------------- titles, meta & cross-references --
for p in arts:
    s = rd(REPO, p)
    en = p.endswith("-en.html")
    slug = p[len("bt-"):-len(".html")]
    if en:
        slug = slug[:-3]
    m = (bt.EN if en else bt.ART)[slug]
    si = [i for i, sec in enumerate(bt.SECTIONS) if slug in sec["slugs"]][0]
    chk("<h1>%s</h1>" % tb.esc(m["title"]) in s, "%s h1" % p)
    title = re.search(r"<title>(.*?)</title>", s, re.S).group(1)
    chk(tb.esca(m["title"]) in title, "%s <title>" % p)
    chk(tb.esca(bt.NAME_EN if en else bt.NAME_ZH) in title,
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
    kicker = bt.SECTIONS_EN[si]["en"].upper()
    chk('<div class="kicker">%s</div>' % tb.esc(kicker) in s, "%s kicker" % p)
    sec_name = (bt.SECTIONS_EN[si]["en"] if en else bt.SECTIONS[si]["zh"])
    mm = re.search(r'<div class="meta">(.*?)</div>', s).group(1).split(" · ")
    chk(mm[0] == (bt.NAME_EN if en else bt.NAME_ZH) and mm[1] == sec_name,
        "%s meta line %s" % (p, mm))
    chk(('<a href="topics-en.html" class="on">' if en
         else '<a href="topics.html" class="on">') in s, "%s nav active" % p)
    chk('class="backlink" href="%s"' % ("bt-en.html" if en else "bt.html") in s,
        "%s backlink" % p)
    for k in bt.ART[slug]["tags"]:
        chk('href="%s?tag=%s"' % ("bt-en.html" if en else "bt.html", k) in s,
            "%s tag chip %s" % (p, k))
    # pnav chain
    i = ORD.index(slug)
    pn = re.search(r'<div class="pnav">(.*?)</div>', s, re.S).group(1)
    if i == 0:
        chk(pn.startswith("<span></span>"), "%s first has prev" % p)
    else:
        chk('class="pv" href="bt-%s%s.html"' % (ORD[i - 1], "-en" if en else "")
            in pn, "%s prev" % p)
    if i == NART - 1:
        chk(pn.endswith("<span></span>"), "%s last has next" % p)
    else:
        chk('class="nx" href="bt-%s%s.html"' % (ORD[i + 1], "-en" if en else "")
            in pn, "%s next" % p)
for lang, page in (("zh", "bt.html"), ("en", "bt-en.html")):
    s = rd(REPO, page)
    hub = bt.HUB if lang == "zh" else bt.HUB_EN
    chk("<title>%s</title>" % tb.esca(hub["title"]) in s, "%s title" % page)
    chk('<meta name="description" content="%s">' % tb.esca(hub["desc"]) in s,
        "%s description" % page)
    chk('<div class="kicker">%s</div>' % bt.KICKER in s, "%s kicker" % page)
    chk(tb.esc(hub["intro"]) in s or hub["intro"] in s, "%s intro" % page)
    chk(hub["closing"] in s, "%s closing" % page)
    meta_l = bt.ART if lang == "zh" else bt.EN
    cards = re.findall(r'<a class="postcard" data-tags="([^"]*)" href="([^"]*)"', s)
    chk([c[1] for c in cards] == ["bt-%s%s.html" % (s_, "-en" if lang == "en"
                                                    else "") for s_ in ORD],
        "%s card order" % page)
    for slug in ORD:
        chk('<div class="t">%s</div>' % tb.esc(meta_l[slug]["title"]) in s,
            "%s card title %s" % (page, slug))
    grp = re.findall(r'<div class="postgroup hnstep">.*?\n  </div>', s, re.S)
    chk([g.count('class="postcard"') for g in grp] == GROUPS,
        "%s group sizes" % page)
    for si, sec in enumerate(bt.SECTIONS):
        nm = sec["zh"] if lang == "zh" else bt.SECTIONS_EN[si]["en"]
        chk("<h3><b>%d</b>%s</h3>" % (si + 1, tb.esc(nm)) in s,
            "%s group title %d" % (page, si + 1))
    bar = tb.RE_HUB_TAGC.search(s).group(2)
    cnts = dict((k, int(n)) for k, n in
                re.findall(r'data-tag="([^"]*)">[^<]*<i>(\d+)</i>', bar))
    want = {"": NART}
    for slug in ORD:
        for k in bt.ART[slug]["tags"]:
            want[k] = want.get(k, 0) + 1
    chk(cnts == want, "%s tagbar counts %s" % (page, cnts))
    li = 0 if lang == "zh" else 1
    for k, lab in bt.LABEL_ADD.items():
        chk('data-tag="%s">#%s <i>' % (k, tb.esc(lab[li])) in bar,
            "%s new label %s" % (page, k))

# cross-reference titles: 修正 21 (zh) / SPEC-EN section 4 (en), verbatim
zh_titles = set(bt.ART[s]["title"] for s in ORD)
en_titles = set(bt.EN[s]["title"] for s in ORD)
spec = rd(BT, "SPEC.md")
tbl = spec[spec.index("### 修正 21"):spec.index("### 修正 22")]
fix21 = dict(re.findall(r"\| \`(bt-[a-z0-9-]+)\` \| (.+?) \|", tbl))
chk(len(fix21) == NART, "修正 21 table has %d rows" % len(fix21))
for slug in ORD:
    chk(bt.ART[slug]["title"] == fix21.get("bt-" + slug),
        "bt-%s title != 修正 21 table" % slug)
sp_en = rd(BT, "SPEC-EN.md")
sec4 = sp_en[sp_en.index("## 4. Canonical English titles"):
             sp_en.index("## 5. Structure")]
spec_en_titles = dict(re.findall(r"- `(bt-[a-z0-9-]+)` → \"(.+?)\"", sec4))
chk(len(spec_en_titles) == NART,
    "SPEC-EN section 4 has %d canonical rows" % len(spec_en_titles))
for slug in ORD:
    chk(bt.EN[slug]["title"] == spec_en_titles.get("bt-" + slug),
        "bt-%s en title != SPEC-EN section 4" % slug)

# SPEC-EN section 4 also fixes the English titles for the seventeen ALREADY
# LIVE pages this topic points at.  Re-derive them from the live pages so a
# stale spec cannot bless a stale body.
ptr = sec4[sec4.index("**Pointers to existing site pages"):]
ptr_rows = re.findall(r"→ \"(.+?)\" \(`([a-z0-9\-]+\.html)`\)", ptr)
chk(len(ptr_rows) == 17, "SPEC-EN section 4 lists %d live-page pointers, "
                         "want 17" % len(ptr_rows))
for want_t, fn in ptr_rows:
    if not os.path.exists(os.path.join(REPO, fn)):
        chk(False, "SPEC-EN pointer names a page that does not exist: %s" % fn)
        continue
    head = re.split(r"[｜|]", re.search(r"<title>(.*?)</title>",
                                       rd(REPO, fn), re.S).group(1))[0].strip()
    chk(head == want_t, "SPEC-EN pointer title for %s is %r, the live page's "
                        "own title is %r" % (fn, want_t, head))

live_h1, live_head = {}, {}
for n in os.listdir(REPO):
    if not n.endswith(".html") or n == "bt.html" or n.startswith("bt-"):
        continue
    s = rd(REPO, n)
    m = re.search(r"<h1>(.*?)</h1>", s, re.S)
    if m:
        live_h1.setdefault(m.group(1), n)
    if n.endswith("-en.html"):
        m = re.search(r"<title>(.*?)</title>", s, re.S)
        if m:
            live_head.setdefault(re.split(r"[｜|]", m.group(1))[0].strip(),
                                 n[:-len("-en.html")] + ".html")
zh_key = dict((bt.ART[s]["title"], s) for s in ORD)
en_key = dict((bt.EN[s]["title"], s) for s in ORD)


def en_quoted(text):
    """Every span between two consecutive quote marks, both parities.

    verify_endo.py used a plain '"(.{18,110})"' scan, which pairs quotes
    left to right and therefore loses a title whenever an odd number of
    scare quotes precedes it in the same paragraph -- bt-mg-grade-en's
    second pointer at "Three tumours, three different logics" sits behind
    'What "benign" and "malignant" each mean...' and was invisible to that
    scan (69 hits instead of 97).  Walking consecutive quote PAIRS covers
    both parities, so no cross-reference can hide behind a scare quote."""
    q = [m.start() for m in re.finditer('"', text)]
    return [text[a + 1:b] for a, b in zip(q, q[1:])]


known_en = en_titles | set(live_head)
n_zh_xref = n_en_xref = 0
zh_refs, en_refs = {}, {}
for slug in ORD:
    body = page_body(rd(REPO, "bt-%s.html" % slug))
    seen = {}
    for t in re.findall(r"〈([^〉]*)〉", body):
        if t in zh_titles or t in live_h1:
            n_zh_xref += 1
            k = zh_key.get(t) or live_h1[t]
            seen[k] = seen.get(k, 0) + 1
            continue
        chk(t in ALLOW_ZH_ANGLE,
            "bt-%s: cross-reference 〈%s〉 matches no canonical title"
            % (slug, t))
    zh_refs[slug] = seen
for slug in ORD:
    body = RE_FIG_STRIP.sub("\n", page_body(rd(REPO, "bt-%s-en.html" % slug)))
    # bt bodies wrap every citation in <a href="https://...">, so the quoted
    # strings are read out of the TEXT, not the markup -- otherwise every URL
    # attribute value would be scanned as if it were a quoted title.
    text = html.unescape(RE_TAG.sub("", body))
    seen = {}
    for q in en_quoted(text):
        if not 18 <= len(q) <= 110:
            continue
        if q in known_en:
            n_en_xref += 1
            k = en_key.get(q) or live_head[q]
            seen[k] = seen.get(k, 0) + 1
            continue
        ratio, near = max((difflib.SequenceMatcher(None, q, k).ratio(), k)
                          for k in known_en)
        chk(ratio < 0.86,
            "bt-%s-en: quoted \"%s\" is a near-miss of \"%s\" (%.2f)"
            % (slug, q, near, ratio))
    en_refs[slug] = seen
# the two languages must point at the same pages, the same number of times
for slug in ORD:
    chk(zh_refs[slug] == en_refs[slug],
        "bt-%s: cross-references differ between languages, zh %s vs en %s"
        % (slug, sorted(zh_refs[slug].items()), sorted(en_refs[slug].items())))
chk(n_zh_xref >= NART and n_en_xref >= NART,
    "suspiciously few cross-references found (zh %d, en %d)"
    % (n_zh_xref, n_en_xref))
report(13, "h1 / <title> / og:title / description / dek / lead / note / "
           "kicker / meta line / tag chips / pnav chain == meta & module on "
           "all 42 articles; hub title/desc/intro/closing, 5 groups 4/5/3/4/5, "
           "card titles = meta titles, tag counts = card counts, new labels "
           "rendered; %d zh and %d en cross-reference titles are verbatim "
           "修正 21 / SPEC-EN 4 or a live page's own title, no near-miss "
           "variants, and every article points at the same pages the same "
           "number of times in both languages; SPEC-EN 4's 17 live-page "
           "titles still match those pages" % (n_zh_xref, n_en_xref))

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
        chk(skeleton(rd(REPO, "bt-%s%s.html" % (slug, suf))) == t,
            "bt-%s%s: skeleton differs from %s" % (slug, suf, ART_TPL[lang]))
for lang, page in (("zh", "bt.html"), ("en", "bt-en.html")):
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
           "<style> byte-identical on all 44 (figure css present once); "
           "head/body tags once; no double-escaped entities")

# 15 ---------------------------------------------------- gb-what-it-is diff ---
def body_links(s):
    b = re.search(r'<div class="body-html">\n(.*?)\n    </div>',
                  s, re.S).group(1)
    return re.findall(r'href="([^":]+\.html)(?:[#?][^"]*)?"', b)


chk(sorted(bt.GB_WHAT_EDITS) == ["gb-what-it-is-en.html", "gb-what-it-is.html"],
    "GB_WHAT_EDITS covers %s" % sorted(bt.GB_WHAT_EDITS))
n_subs = 0
for f in ("gb-what-it-is.html", "gb-what-it-is-en.html"):
    pre, now = rd(PRE, f), rd(REPO, f)
    pl, nl = pre.splitlines(True), now.splitlines(True)
    chk(len(pl) == len(nl), "%s: line count changed %d -> %d"
        % (f, len(pl), len(nl)))
    diff_idx = [i for i, (a, b) in enumerate(zip(pl, nl)) if a != b]
    # both substitutions live in the same paragraph, so ONE line changes
    chk(len(diff_idx) == 1, "%s: %d changed lines, want 1 (lines %s)"
        % (f, len(diff_idx), [i + 1 for i in diff_idx]))
    edits = bt.GB_WHAT_EDITS[f]
    chk(len(edits) == 2, "%s: %d edits declared, want 2" % (f, len(edits)))
    want = pre
    for old, new in edits:
        chk(want.count(old) == 1, "%s: anchor not present exactly once in the "
            "prebackup: %r" % (f, old[:40]))
        want = want.replace(old, new)
        n_subs += 1
    chk(now == want, "%s: content is not the prebackup with exactly the two "
        "gb-what-it-is substitutions applied" % f)
    for old, new in edits:
        chk(old not in now, "%s: old wording still present: %r" % (f, old[:40]))
        chk(now.count(new) == 1, "%s: new wording not present exactly once: %r"
            % (f, new[:40]))
    # Exactly ONE anchor is added per file, and it is the first pointer's
    # link to the bt hub.  NOTE, and this is the checked fact a future round
    # should inherit: unlike pel-who (endo's chore page, which linked
    # nothing in body and so pointed in sense only), gb-what-it-is already
    # carries one in-body site link -- the
    # 〈<a href="lc-brainmet.html">腦轉移不等於末期</a>〉 pointer one sentence
    # above the first edit, in the same block of paragraphs -- so a LINKED
    # title is this page's own house style for an on-site pointer, and the
    # first new pointer matches that form.  Both the old and the new link
    # are pinned by value and in order: anything else added, removed or
    # reordered fails.
    en_f = f.endswith("-en.html")
    pre_links = ["lc-brainmet-en.html" if en_f else "lc-brainmet.html"]
    want_links = pre_links + ["bt-en.html" if en_f else "bt.html"]
    chk(body_links(pre) == pre_links,
        "%s: prebackup in-body site links %s, expected %s"
        % (f, body_links(pre), pre_links))
    chk(body_links(now) == want_links,
        "%s: in-body site links %s, expected %s"
        % (f, body_links(now), want_links))
    chk(now.count("<a ") == pre.count("<a ") + 1
        and now.count("<a href=") == pre.count("<a href=") + 1,
        "%s: anchor count %d -> %d, want exactly one added"
        % (f, pre.count("<a href="), now.count("<a href=")))
chk(n_subs == 4, "%d substitutions declared in all, want 4" % n_subs)
# The topic is named twice per file: the FIRST pointer carries the <a>, in
# gb-what-it-is's own 〈link〉 / prose-link form; the SECOND, one sentence
# later in the same paragraph, stays unlinked so the paragraph does not
# carry the same href twice.  Both halves of that ruling are pinned.
zgw, egw = rd(REPO, "gb-what-it-is.html"), rd(REPO, "gb-what-it-is-en.html")
zh_linked = '〈<a href="bt.html">%s</a>〉' % bt.NAME_ZH
zh_plain = "〈%s〉" % bt.NAME_ZH
en_linked = '<a href="bt-en.html">%s</a>' % bt.NAME_EN
en_plain = '"%s"' % bt.NAME_EN
chk(zgw.count(bt.NAME_ZH) == 2,
    "gb-what-it-is.html names %s %d times, want 2"
    % (bt.NAME_ZH, zgw.count(bt.NAME_ZH)))
chk(zgw.count(zh_linked) == 1,
    "gb-what-it-is.html: the first pointer is not the linked 〈<a>title</a>〉 "
    "form this page uses for lc-brainmet")
chk(zgw.count(zh_plain) == 1,
    "gb-what-it-is.html: the second pointer is not the unlinked 〈title〉 "
    "form (found %d)" % zgw.count(zh_plain))
chk(egw.count(bt.NAME_EN) == 2,
    'gb-what-it-is-en.html names "%s" %d times, want 2'
    % (bt.NAME_EN, egw.count(bt.NAME_EN)))
chk(egw.count(en_linked) == 1,
    "gb-what-it-is-en.html: the first pointer is not the linked form this "
    "page uses for lc-brainmet-en")
chk(egw.count(en_plain) == 1,
    'gb-what-it-is-en.html: the second pointer is not the unlinked "title" '
    "form (found %d)" % egw.count(en_plain))
chk(zgw.count('href="bt.html"') == 1 and egw.count('href="bt-en.html"') == 1,
    "gb-what-it-is links the bt hub %d/%d times, want exactly one per file"
    % (zgw.count('href="bt.html"'), egw.count('href="bt-en.html"')))
chk('href="bt-' not in zgw and 'href="bt-' not in egw.replace(
        'href="bt-en.html"', ""),
    "gb-what-it-is links a bt ARTICLE -- the pointer is to the hub only")
# the page still promises nothing: no "a topic of its own is being written"
chk("作者另開專題" not in zgw,
    "gb-what-it-is.html still promises a meningioma topic instead of naming it")
chk("the author is giving it a topic of its own" not in egw,
    "gb-what-it-is-en.html still promises a meningioma topic instead of "
    "naming it")
# ... and the glioblastoma facts around the two rewritten sentences are
# byte-identical: same paragraph, same citations, same numbers
chk("佔全部腦瘤的 42.6%" in zgw and "發生率每 10 萬人 2.02" in zgw,
    "gb-what-it-is.html: the CNS5 / CBTRUS figures around the edit moved")
chk("42.6% of all brain tumours" in egw
    and "incidence 2.02 per 100,000" in egw,
    "gb-what-it-is-en.html: the CNS5 / CBTRUS figures around the edit moved")
report(15, "gb-what-it-is.html and gb-what-it-is-en.html differ from "
           "prebackup by exactly the two GB_WHAT_EDITS substitutions each "
           "(one changed line per file, both edits inside the same "
           "paragraph; four substitutions in all); each file gains exactly "
           "one anchor, the first pointer's link to the bt hub in this "
           "page's own lc-brainmet form, while the second pointer stays "
           "unlinked; the pre-existing lc-brainmet link is unchanged and "
           "nothing else on either page moved")

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
chk(not head.lower().startswith("bt") and "bt:" not in head.lower()
    and "良性腦瘤" not in head,
    "HEAD looks like a bt commit -- this round is local only: %r" % head)
report(16, "git status: exactly %s modified; untracked = 44 pages + %d svgs + "
           "5 _pipeline modules; nothing staged, nothing committed"
           % (", ".join(SHARED), NSVG))

print()
nfail = sum(1 for r in results if not r[2])
if nfail:
    print("FAILED: %d of %d checks" % (nfail, len(results)))
    sys.exit(1)
print("ALL %d CHECKS PASSED" % len(results))
