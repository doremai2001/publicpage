# -*- coding: utf-8 -*-
"""Verification pass over the generated breast-radiotherapy pages.

The cervix/liver 12-check standard, adjusted for ROUND 1 = ZH ONLY, plus two
checks specific to this topic:

  3c  the conflict-of-interest disclosure paragraph (SPEC section 二, FIXES
      invariant 1) is byte-identical on all ten articles and sits before the
      first <h4>;
  3d  every figure's alt attribute equals the manifest's zh_alt with exactly
      one level of attribute escaping applied (and nothing raw left in it).

  13  every regenerated Chinese page differs from its PUBLISHED version only
      in the hreflang block and the language-switch chip -- except the two
      articles whose Chinese source was corrected between the rounds, whose
      remaining difference is printed in full and must be confined to the
      body slot.

ZH_ONLY (taken from brt.ZH_ONLY) drives the whole file:
  * round 1 (True): check 5 asserts hreflang / canonical-partner / language
    switch are ABSENT, so the zh-only promise is verified rather than skipped;
    topics-en.html must be byte-identical to what is live; check 3 has no
    zh/en symmetry leg; check 13 is inert (nothing published yet).
  * round 2 (False): all of those switch on.

The baseline everywhere is the git HEAD blob (round 1 is published as commits
4949329 / 9b9c5f6, so HEAD is what the site is serving) rather than a scratch
snapshot -- that is what makes "the existing sitemap lines are byte-unchanged"
and check 13 mean something after a round has already shipped.
"""
import difflib
import filecmp
import html
import json
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import brt
import topicbuild as tb

REPO = "/home/claude/repo"
UPLOAD = "/home/claude/upload-brt"
BASE_REF = "HEAD"          # round 1 is published, so HEAD == what is live
BRT = "/home/claude/brt"
# Chinese sources corrected between round 1 and round 2 (declared, not waived:
# check 13 prints their remaining diff and confines it to the body slot).
EXPECTED_BODY_DIFF = {
    "brt-tomo.html": "FIXES F10: the NHI attribution sentence",
    "brt-technique-map.html": "RadComp -> RADCOMP",
}
ZH_ONLY = brt.ZH_ONLY
LANGS = [("zh", "")] if ZH_ONLY else [("zh", ""), ("en", "-en")]
ORD = [s for sec in brt.SECTIONS for s in sec["slugs"]]
GROUP_SIZES = [len(sec["slugs"]) for sec in brt.SECTIONS]
ART_TPL = {"zh": "cc-first-month.html", "en": "cc-first-month-en.html"}
HUB_TPL = {"zh": "cc.html", "en": "cc-en.html"}
fails = []


def chk(ok, msg):
    if not ok:
        fails.append(msg)


def rd(*p):
    return open(os.path.join(*p), encoding="utf-8").read()


def base(name):
    """The file as published (its blob at BASE_REF), or None if new."""
    r = subprocess.run(["git", "-C", REPO, "show", "%s:%s" % (BASE_REF, name)],
                       capture_output=True)
    return r.stdout.decode("utf-8") if r.returncode == 0 else None


def esca(s):
    return html.escape(s, quote=False).replace('"', "&quot;")


def src_path(slug, lang):
    return os.path.join(BRT, "body" if lang == "zh" else "en",
                        "brt-%s%s.html" % (slug, "" if lang == "zh" else "-en"))


hubs = ["brt.html"] + ([] if ZH_ONLY else ["brt-en.html"])
arts = []
for _l, _s in LANGS:
    arts += ["brt-%s%s.html" % (s, _s) for s in ORD]
pages = hubs + arts
svgs = sorted(n for n in os.listdir(os.path.join(BRT, "figs"))
              if n.endswith(".svg"))
NPAGE = len(pages)
# both languages' SVGs are shipped in round 1 so round 2 needs no transfer
NUPLOAD = NPAGE + len(svgs) + (1 if ZH_ONLY else 2) + 1

# 1 --------------------------------------- page count + sitemap, both ways ---
chk(NPAGE == (11 if ZH_ONLY else 22), "page count %d" % NPAGE)
for p in pages:
    chk(os.path.exists(os.path.join(REPO, p)), "missing %s" % p)
shared = ["topics.html", "sitemap.xml"] + ([] if ZH_ONLY else ["topics-en.html"])
sm = rd(REPO, "sitemap.xml")
pre_sm = base("sitemap.xml")
RE_LOC = re.compile(re.escape(tb.BASE) + r"([^<]*)</loc>")
RE_BRT_LOC = re.compile(r"<loc>%s(brt\.html|brt-)" % re.escape(tb.BASE))
brt_lines = [l for l in sm.splitlines() if RE_BRT_LOC.search(l)]
kept = [l for l in sm.splitlines() if not RE_BRT_LOC.search(l)]
pre_kept = [l for l in pre_sm.splitlines() if not RE_BRT_LOC.search(l)]
pre_brt = [l for l in pre_sm.splitlines() if RE_BRT_LOC.search(l)]
chk(len(brt_lines) == NPAGE, "sitemap has %d brt urls, want %d"
    % (len(brt_lines), NPAGE))
chk(kept == pre_kept, "existing (non-brt) sitemap lines changed or reordered")
want_urls = pre_sm.count("<url>") - len(pre_brt) + NPAGE
chk(sm.count("<url>") == want_urls,
    "sitemap <url> %d, want %d" % (sm.count("<url>"), want_urls))
for p in pages:
    chk(("<loc>%s%s</loc>" % (tb.BASE, p)) in sm, "sitemap missing %s" % p)
want_prio = [("brt.html", "0.85")] + [("brt-%s.html" % s, "0.75") for s in ORD]
if not ZH_ONLY:
    want_prio += ([("brt-en.html", "0.75")]
                  + [("brt-%s-en.html" % s, "0.65") for s in ORD])
for p, prio in want_prio:
    ln = [l for l in sm.splitlines()
          if "<loc>%s%s</loc>" % (tb.BASE, p) in l][0]
    chk("<lastmod>%s</lastmod>" % brt.DATE in ln, "%s lastmod" % p)
    chk("<priority>%s</priority>" % prio in ln, "%s priority" % p)
# lines published in an earlier round keep their exact bytes
pre_brt_map = dict((RE_LOC.search(l).group(1), l) for l in pre_brt)
for l in brt_lines:
    n = RE_LOC.search(l).group(1)
    if n in pre_brt_map:
        chk(l == pre_brt_map[n], "published sitemap line rewritten: %s" % n)
chk("brt-brt-" not in sm
    and not any("brt-brt-" in n for n in os.listdir(REPO)),
    "double-prefixed name somewhere")
# the brt block is one contiguous run between the lv block and carc.html
sml = sm.splitlines()
i_lv = [i for i, l in enumerate(sml)
        if "<loc>%slv-bridging-en.html</loc>" % tb.BASE in l][0]
chk("<loc>%sbrt.html</loc>" % tb.BASE in sml[i_lv + 1],
    "brt block not after lv block")
chk("<loc>%scarc.html</loc>" % tb.BASE in sml[i_lv + 1 + NPAGE],
    "brt block not before carc block")
chk(all(RE_BRT_LOC.search(l) for l in sml[i_lv + 1: i_lv + 1 + NPAGE]),
    "brt sitemap block is not contiguous")
# full file <-> sitemap diff, both directions
sm_names = set(m.group(1) for m in RE_LOC.finditer(sm))
repo_html = set(n for n in os.listdir(REPO) if n.endswith(".html"))
in_sm_not_repo = sorted(n for n in sm_names if n.endswith(".html")
                        and n not in repo_html)
pre_names = set(m.group(1) for m in RE_LOC.finditer(pre_sm))
in_repo_not_sm = sorted(n for n in repo_html if n not in sm_names)
pre_not_sm = sorted(n for n in repo_html
                    if not (n.startswith("brt-") or n in hubs)
                    and n not in pre_names)
chk(in_sm_not_repo == [], "sitemap urls without a file: %s" % in_sm_not_repo)
chk(in_repo_not_sm == pre_not_sm,
    "repo html not in sitemap changed: %s (was %s)"
    % (in_repo_not_sm, pre_not_sm))
chk(all(p in sm_names for p in pages), "a brt page missing from sitemap")
print("1. %d brt pages (%d articles + %d hub%s) exist in the repo; sitemap "
      "<url> = %d (published %d, +%d this round), all %d brt URLs present at "
      "0.85 hub / 0.75 zh articles%s, lastmod %s; the brt block is one "
      "contiguous run between the lv block and carc.html; every non-brt line "
      "byte-unchanged and in order, and every brt line published in round 1 "
      "byte-unchanged too; full file<->sitemap diff both ways: every sitemap "
      "URL has a file, files-not-in-sitemap unchanged (%s)"
      % (NPAGE, len(arts), len(hubs), "" if ZH_ONLY else "s",
         sm.count("<url>"), pre_sm.count("<url>"),
         sm.count("<url>") - pre_sm.count("<url>"), NPAGE,
         "" if ZH_ONLY else " / 0.75 en hub / 0.65 en articles",
         brt.DATE, in_repo_not_sm or "none"))

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
print("2. %d internal .html links and %d svg src/srcset references across the "
      "repo: %d unresolved %s"
      % (nlinks, nimg, len(bad), bad[:10] if bad else ""))

# 3 ------------- citation / h4 / reference symmetry vs the ORIGINAL sources --
rows = []
for slug in ORD:
    fr = {}
    for lang, suf in LANGS:
        src = rd(src_path(slug, lang))          # original, figure-free source
        body, items, n = tb.split_fragment(src)
        page = rd(REPO, "brt-%s%s.html" % (slug, suf))
        pb = re.search(r'<div class="body-html">\n(.*?)\n    </div>',
                       page, re.S).group(1)
        pr = re.search(r'<div class="refs">.*?<ol>(.*?)</ol>',
                       page, re.S).group(1)
        fr[lang] = (
            len(re.findall(r'<sup class="cit">', body)),
            len(re.findall(r"<h4>", body)),
            n,
            len(re.findall(r'<sup class="cit">', pb)),
            len(re.findall(r"<h4>", pb)),
            len(re.findall(r"<li>", pr)),
        )
        chk(fr[lang][0] == fr[lang][3],
            "%s %s citations page!=source" % (slug, lang))
        chk(fr[lang][1] == fr[lang][4], "%s %s h4 page!=source" % (slug, lang))
        chk(fr[lang][2] == fr[lang][5], "%s %s refs page!=source" % (slug, lang))
        chk("<ol>" not in pr and "</ol>" not in pr,
            "%s %s nested <ol>" % (slug, lang))
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
            "%s %s body text differs from source outside figures"
            % (slug, lang))
    if not ZH_ONLY:
        chk(fr["zh"][:3] == fr["en"][:3],
            "%s zh/en mismatch %s %s" % (slug, fr["zh"], fr["en"]))
    rows.append((slug, fr["zh"][0], fr["zh"][1], fr["zh"][2]))
print("3. citations / <h4> / references, page == original source%s; body text "
      "outside the figure blocks byte-equivalent to source:"
      % ("" if ZH_ONLY else " and zh == en"))
for r in rows:
    print("     %-16s cit=%-3d h4=%-2d refs=%d" % r)

# 3b ------------------------- figures per manifest used_by AND placement -----
manifest = json.load(open(os.path.join(BRT, "figs", "manifest.json"),
                          encoding="utf-8"))
per = {}
for fig in manifest:
    for u in fig["used_by"]:
        per.setdefault(u, []).append(fig)
RE_FIG = re.compile(
    r'<figure class="article-figure">\s*<picture>\s*'
    r'<source media="\(max-width:620px\)" srcset="([^"]+)">\s*'
    r'<img src="([^"]+)" width="1440" height="(\d+)" loading="lazy" '
    r'decoding="async" alt="([^"]*)">\s*</picture>\s*'
    r'<figcaption>(.*?)</figcaption>\s*</figure>', re.S)
nfig_checked, alt_pairs = 0, []
for slug in ORD:
    want = per.get("brt-" + slug, [])
    # expected placement: 1-based no. of the source <h4> the manifest names
    src_h4 = re.findall(r"<h4>(.*?)</h4>", rd(src_path(slug, "zh")))
    want_pos = [src_h4.index(f["placement"]["after_h4"]) + 1 for f in want]
    for lang, suf in LANGS:
        s = rd(REPO, "brt-%s%s.html" % (slug, suf))
        figs = RE_FIG.findall(s)
        chk(len(figs) == len(want), "brt-%s%s: %d figures, want %d"
            % (slug, suf, len(figs), len(want)))
        for got, fig in zip(figs, want):
            f = fig["files"]
            mob = f["mobile"] if lang == "zh" else f["en_mobile"]
            dsk = f["desktop"] if lang == "zh" else f["en"]
            alt = esca(fig["zh_alt"] if lang == "zh" else fig["en_alt"])
            # captions are text nodes: & and < carry one level of escaping
            cap = (fig["zh_caption"] if lang == "zh" else fig["en_caption"]
                   ).replace("&", "&amp;").replace("<", "&lt;")
            vb = re.search(r'viewBox="0 0 1440 (\d+)"',
                           rd(BRT, "figs", dsk)).group(1)
            chk(got[0] == mob, "brt-%s%s srcset %s" % (slug, suf, got[0]))
            chk(got[1] == dsk, "brt-%s%s src %s" % (slug, suf, got[1]))
            chk(got[2] == vb, "brt-%s%s height %s != viewBox %s"
                % (slug, suf, got[2], vb))
            chk(got[3] == alt, "brt-%s%s alt differs" % (slug, suf))
            chk(got[4] == cap, "brt-%s%s caption differs" % (slug, suf))
            alt_pairs.append((lang, slug, fig, got[3]))
            nfig_checked += 1
        # placement audit: figure #k closes the h4 section the manifest names
        body = re.search(r'<div class="body-html">\n(.*?)\n    </div>',
                         s, re.S).group(1)
        pos, h4 = [], 0
        for m in re.finditer(r'<h4>|<figure class="article-figure">', body):
            if m.group(0) == "<h4>":
                h4 += 1
            else:
                pos.append(h4)
        chk(pos == want_pos, "brt-%s%s figure placement %s want %s"
            % (slug, suf, pos, want_pos))
print("3b. %d figure instances match the manifest (files per language, "
      "caption, height = desktop viewBox); placement per manifest after_h4, "
      "audited on every page that carries a figure (5 figures, one per "
      "article, in %s)"
      % (nfig_checked,
         ", ".join(f["placement"]["article"] for f in manifest)))
for n in svgs:
    chk(filecmp.cmp(os.path.join(BRT, "figs", n), os.path.join(REPO, n),
                    shallow=False), "svg differs in repo: %s" % n)
chk(len(svgs) == 20, "expected 20 svgs, found %d" % len(svgs))
print("    all %d SVGs (zh + en, desktop + mobile) byte-identical to "
      "/home/claude/brt/figs" % len(svgs))

# 3c ------------------- disclosure paragraph, verbatim on all 10, per SPEC ---
import hashlib
DISC_MD5 = "28a12f17e2fb"        # FIXES.md invariant 1, md5 of the inner text
ANCHOR = {"zh": "\u5148\u8aaa\u6211\u7684\u4f4d\u7f6e",
          "en": "My position first"}
for lang, suf in LANGS:
    src0 = rd(src_path(ORD[0], lang))
    ps = re.findall(r"<p>.*?</p>", src0[:src0.index("<h4>")], re.S)
    disc = ps[1]                           # fixed disclosure, 2nd lead-in <p>
    chk(ANCHOR[lang] in disc,
        "%s disclosure paragraph not where expected" % lang)
    seen_disc = set()
    for slug in ORD:
        page = rd(REPO, "brt-%s%s.html" % (slug, suf))
        body = re.search(r'<div class="body-html">\n(.*?)\n    </div>',
                         page, re.S).group(1)
        head = body[:body.index("<h4>")]
        chk(head.count(disc) == 1,
            "brt-%s%s: disclosure paragraph missing or altered before first "
            "<h4>" % (slug, suf))
        hps = re.findall(r"<p>.*?</p>", head, re.S)
        chk(len(hps) == 2 and hps[1] == disc,
            "brt-%s%s: disclosure is not the second of exactly two lead-in "
            "paragraphs" % (slug, suf))
        seen_disc.add(head.count(disc) == 1 and disc or "MISMATCH-" + slug)
    chk(len(seen_disc) == 1,
        "%s disclosure paragraph not byte-identical across 10" % lang)
    inner_md5 = hashlib.md5(disc[3:-4].encode("utf-8")).hexdigest()
    if lang == "zh":
        chk(inner_md5.startswith(DISC_MD5),
            "disclosure md5 %s does not match FIXES invariant 1 (%s...)"
            % (inner_md5, DISC_MD5))
        pin = "inner-text md5 %s matches FIXES.md invariant 1" % inner_md5[:12]
    else:
        # SPEC-EN.md section 1 gives the one permitted English rendering
        spec = rd(BRT, "SPEC-EN.md")
        blk = spec[spec.index("> <p>My position first"):spec.index("## 2.")]
        want = re.sub(r"\s+", " ",
                      " ".join(l.lstrip("> ").strip()
                               for l in blk.strip().splitlines())).strip()
        chk(re.sub(r"\s+", " ", disc).strip() == want,
            "en disclosure does not match SPEC-EN.md section 1 verbatim")
        pin = "matches SPEC-EN.md section 1 verbatim"
    print("3c. [brt-specific] the %s conflict-of-interest disclosure is "
          "byte-identical on all 10 articles (%d bytes) and is the SECOND of "
          "exactly two paragraphs before the first <h4> on every one; %s"
          % (lang, len(disc.encode("utf-8")), pin))

# 3d ---------- figure alt == manifest zh_alt, escaped exactly once -----------
for lang, slug, fig, got in alt_pairs:
    key = "zh_alt" if lang == "zh" else "en_alt"
    raw = fig[key]
    tag = "brt-%s (%s)" % (slug, lang)
    chk(got == esca(raw), "%s: alt != escaped %s" % (tag, key))
    chk(html.unescape(got) == raw, "%s: alt does not unescape to %s"
        % (tag, key))
    # nothing raw survives inside the attribute, and nothing is escaped twice
    chk('"' not in got and "<" not in got and ">" not in got,
        "%s: raw quote/angle bracket left in alt" % tag)
    chk("&amp;amp;" not in got and "&amp;quot;" not in got
        and "&amp;lt;" not in got and "&amp;gt;" not in got,
        "%s: double-escaped alt" % tag)
    chk(re.match(r"^(?:[^&]|&(?:amp|lt|gt|quot|#\d+);)*$", got) is not None,
        "%s: bare & in alt" % tag)
print("3d. [brt-specific] all %d figure alts (%s) equal the manifest's "
      "%s attribute-escaped exactly once (round-trip through html.unescape; "
      "no raw \", <, > left; no &amp;amp;/&amp;quot; double escape; every & a "
      "well-formed entity)"
      % (len(alt_pairs),
         " + ".join("%d %s" % (len([1 for l, _, _, _ in alt_pairs if l == la]),
                               la) for la, _ in LANGS),
         "zh_alt" if ZH_ONLY else "zh_alt / en_alt"))

# 4 -------------------------- style = template + injected figure CSS, stable --
hh = rd(REPO, "hn-first-week.html")
a = hh.index("/* ---------- article figures ---------- */")
b = hh.find("/* ----------", a + 10)
e = hh.index("</style>", a)
if b < 0 or b > e:
    b = e
BLOCK = hh[a:b]
tpl_style = tb.RE_STYLE.search(rd(REPO, ART_TPL["zh"])).group(0)
others = [HUB_TPL["zh"]] if ZH_ONLY else [ART_TPL["en"], HUB_TPL["zh"],
                                          HUB_TPL["en"]]
for f in others:
    chk(tb.RE_STYLE.search(rd(REPO, f)).group(0) == tpl_style,
        "%s template style differs" % f)
i = tpl_style.index("</style>")
# The cc template carries the figure css itself (the site owner added it), so
# inject_css is a no-op and generated pages keep the template style unchanged.
WANT_STYLE = (tpl_style if ".article-figure{" in tpl_style
              else tpl_style[:i] + BLOCK + tpl_style[i:])
chk(".article-figure{" in tpl_style,
    "cc template no longer carries the figure css -- inject_css path changed")
seen = set()
for p in pages:
    s = rd(REPO, p)
    for tag in ("<style>", "</style>", "<body>", "</body>", "</html>",
                "<head>", "</head>"):
        chk(s.count(tag) == 1, "%s: %s x%d" % (p, tag, s.count(tag)))
    st = tb.RE_STYLE.search(s).group(0)
    chk(st == WANT_STYLE, "%s: style != template + figure css" % p)
    seen.add(st)
chk(len(seen) == 1, "style not byte-stable across the %d" % NPAGE)
chk(BLOCK.startswith("/* ---------- article figures ---------- */")
    and BLOCK.count(".article-figure") == 9, "figure css block looks wrong")
print("4. <style> on all %d pages is byte-identical (%d bytes) and equals the "
      "shared template style with the article-figure block present "
      "(inject_css idempotent: the cc template already carries it, so nothing "
      "was injected); head/body tags exactly once each" % (NPAGE,
                                                           len(WANT_STYLE)))

# 5 --------------------------------- hreflang: ZH-ONLY this round ------------
if ZH_ONLY:
    for p in pages:
        s = rd(REPO, p)
        chk("hreflang" not in s, "%s still carries hreflang" % p)
        chk('<div class="lang">' not in s, "%s still carries a lang switch" % p)
        chk('<link rel="canonical" href="%s%s">' % (tb.BASE, p) in s,
            "%s canonical" % p)
        chk(s.count("<link rel=\"canonical\"") == 1, "%s canonical count" % p)
        chk("brt-en.html" not in s and not re.search(r"brt-[a-z-]+-en\.html", s),
            "%s links to a not-yet-published English page" % p)
    print("5. 本輪 zh-only，hreflang / 語言切換 / 英文 canonical 對應暫不檢查 -- "
          "instead verified ABSENT on all %d pages (no hreflang attribute, no "
          "<div class=\"lang\">, no link to brt-en.html or brt-*-en.html), and "
          "each page's self-canonical is present exactly once" % NPAGE)
else:
    npair = 0
    for slug in ORD + [None]:
        z = "brt.html" if slug is None else "brt-%s.html" % slug
        en = "brt-en.html" if slug is None else "brt-%s-en.html" % slug
        npair += 1
        for p, other in ((z, en), (en, z)):
            s = rd(REPO, p)
            chk('<link rel="alternate" hreflang="zh-Hant" href="%s%s">'
                % (tb.BASE, z) in s, "%s hreflang zh" % p)
            chk('<link rel="alternate" hreflang="en" href="%s%s">'
                % (tb.BASE, en) in s, "%s hreflang en" % p)
            chk('<link rel="alternate" hreflang="x-default" href="%s%s">'
                % (tb.BASE, z) in s, "%s hreflang x-default" % p)
            chk('<link rel="canonical" href="%s%s">' % (tb.BASE, p) in s,
                "%s canonical" % p)
            chk('href="%s" hreflang=' % other in s,
                "%s lang switch -> %s" % (p, other))
    print("5. hreflang zh-Hant/en/x-default + canonical + nav language switch, "
          "both directions, on all %d pairs (10 articles + the hub)" % npair)

# 6 ------------------------------------------------- topics pages diff ------
targets = [("topics.html", brt.TOPIC_CARD_ZH, brt.HASPART_ZH,
            "brt.html", "liver.html")]
if not ZH_ONLY:
    targets.append(("topics-en.html", brt.TOPIC_CARD_EN, brt.HASPART_EN,
                    "brt-en.html", "liver-en.html"))
NCARD = 9
for f, card, hp, href, prev_href in targets:
    pre = base(f)
    now = rd(REPO, f)
    already = ('href="%s"' % href) in pre
    if already:
        # the card shipped in an earlier round; this round must not touch it
        chk(now == pre, "%s changed although its card is already published" % f)
        verdict = ("byte-identical to the published version (its card shipped "
                   "in round 1)")
        nrest = 0
    else:
        a, b = pre.splitlines(True), now.splitlines(True)
        d = list(difflib.unified_diff(a, b, n=0))
        added = [l[1:] for l in d
                 if l.startswith("+") and not l.startswith("+++")]
        removed = [l[1:] for l in d
                   if l.startswith("-") and not l.startswith("---")]
        entry = "," + json.dumps(hp, ensure_ascii=False,
                                 separators=(",", ":"))
        chk(len(removed) == 1 and '"hasPart":[' in removed[0],
            "%s removed lines: %d" % (f, len(removed)))
        ld_new = [l for l in added if '"hasPart":[' in l]
        chk(len(ld_new) == 1 and removed[0].count("}]}</script>") == 1
            and ld_new[0] == removed[0].replace("}]}</script>",
                                                "}%s]}</script>" % entry),
            "%s json-ld line not just extended" % f)
        rest = [l for l in added if '"hasPart":[' not in l]
        chk("".join(rest) == card, "%s: added text is not exactly the card" % f)
        nrest = len(rest)
        verdict = ("differs from the published version ONLY by the brt card "
                   "(appended after the %s card, %d lines) and the one "
                   "appended hasPart entry" % (prev_href[:-5], nrest))
    chk(now.count('class="topiccard"') == NCARD,
        "%s: %d card anchors" % (f, now.count('class="topiccard"')))
    chk(now.count("topiccard") == pre.count("topiccard") + (0 if already else 1),
        "%s: topiccard strings %d, was %d"
        % (f, now.count("topiccard"), pre.count("topiccard")))
    grid = re.search(r'<div class="topicgrid">(.*?)\n  </div>',
                     now, re.S).group(1)
    chk(grid.count('class="topiccard"') == NCARD,
        "%s cards not all inside grid" % f)
    chk(".topicgrid{display:grid;grid-template-columns:1fr 1fr;" in now,
        "%s grid columns changed" % f)
    cards = re.findall(r'<a class="topiccard" href="([^"]+)"', grid)
    chk(cards[-1] == href and cards[-2] == prev_href,
        "%s card order %s" % (f, cards))
    old_cards = re.findall(
        r'<a class="topiccard" href="([^"]+)"',
        re.search(r'<div class="topicgrid">(.*?)\n  </div>',
                  pre, re.S).group(1))
    chk((cards if already else cards[:-1]) == old_cards,
        "%s: existing cards changed or reordered" % f)
    ld = json.loads(re.search(
        r'<script type="application/ld\+json">(.*?)</script>',
        now, re.S).group(1))
    chk([e["url"] for e in ld["hasPart"]][-1].endswith(cards[-1]),
        "%s hasPart last entry" % f)
    chk(len(ld["hasPart"]) == NCARD, "%s hasPart %d" % (f, len(ld["hasPart"])))
    pre_ld = json.loads(re.search(
        r'<script type="application/ld\+json">(.*?)</script>',
        pre, re.S).group(1))
    chk((ld["hasPart"] if already else ld["hasPart"][:-1]) == pre_ld["hasPart"],
        "%s: existing hasPart entries changed" % f)
    print("6. %-15s %s; %d cards in the unchanged 2-column grid, the "
          "pre-existing ones byte-identical and in order; hasPart = %d hubs "
          "ending with %s" % (f, verdict, NCARD, NCARD, href))
if ZH_ONLY:
    chk(rd(REPO, "topics-en.html") == base("topics-en.html"),
        "topics-en.html was modified in a zh-only round")
    chk(not os.path.exists(os.path.join(UPLOAD, "topics-en.html")),
        "topics-en.html leaked into the upload dir in a zh-only round")
    print("   topics-en.html byte-identical to the published copy and absent "
          "from the upload dir (\u672c\u8f2a zh-only\uff0c\u82f1\u6587 hub "
          "\u5c1a\u672a\u5b58\u5728)")

# 7 ------------------------------------------------------------- hub render ---
for lang, page in ([("zh", "brt.html")] if ZH_ONLY
                   else [("zh", "brt.html"), ("en", "brt-en.html")]):
    s = rd(REPO, page)
    bar = tb.RE_HUB_TAGC.search(s).group(2)
    cnts = dict((k, int(n)) for k, n in
                re.findall(r'data-tag="([^"]*)">[^<]*<i>(\d+)</i>', bar))
    want = {}
    for slug in ORD:
        for k in brt.ART[slug]["tags"]:
            want[k] = want.get(k, 0) + 1
    want[""] = 10
    chk(cnts == want, "%s tagbar counts differ: %s" % (page, cnts))
    cards = re.findall(
        r'<a class="postcard" data-tags="([^"]*)" href="([^"]*)"', s)
    chk(len(cards) == 10, "%s: %d postcards" % (page, len(cards)))
    dom = {}
    for tags, _ in cards:
        for k in tags.split():
            dom[k] = dom.get(k, 0) + 1
    chk(dom == {k: v for k, v in cnts.items() if k},
        "%s: tagbar counts != card counts" % page)
    grp = re.findall(r'<div class="postgroup hnstep">.*?\n  </div>', s, re.S)
    chk(len(grp) == 3, "%s: %d postgroups" % (page, len(grp)))
    chk([g.count('class="postcard"') for g in grp] == GROUP_SIZES,
        "%s group sizes %s want %s"
        % (page, [g.count('class="postcard"') for g in grp], GROUP_SIZES))
    for i, slug in enumerate(ORD):
        chk(cards[i][1] == "brt-%s%s.html"
            % (slug, "-en" if lang == "en" else ""),
            "%s card %d order" % (page, i))
    for i in (1, 2, 3):
        chk(s.count("<h3><b>%d</b>" % i) == 1,
            "%s section heading %d" % (page, i))
    chk("<h3><b>4</b>" not in s, "%s extra section heading" % page)
    for si, sec in enumerate(brt.SECTIONS):
        chk("<h3><b>%d</b>%s</h3>" % (si + 1, sec["zh"] if lang == "zh"
                                      else brt.SECTIONS_EN[si]["en"]) in s,
            "%s section title %d" % (page, si + 1))
    ld = json.loads(re.search(
        r'<script type="application/ld\+json">(.*?)</script>',
        s, re.S).group(1))
    chk(len(ld["hasPart"]) == 10, "%s hasPart %d" % (page, len(ld["hasPart"])))
    # titles on the hub are the meta titles, not SPEC section 四's code names
    meta_l = brt.ART if lang == "zh" else brt.EN
    for slug in ORD:
        t = meta_l[slug]["title"]
        chk('<div class="t">%s</div>' % html.escape(t, quote=False) in s,
            "%s card title for %s is not the meta title" % (page, slug))
    lab = brt.LABEL_ADD
    li = 0 if lang == "zh" else 1
    for k in lab:
        want_btn = 'data-tag="%s">#%s <i>' % (k, html.escape(lab[k][li],
                                                             quote=False))
        chk(want_btn in bar, "%s new label %s not rendered as %r"
            % (page, k, want_btn))
print("7. hub: 3 groups of %s cards in reading order with the SPEC section 四 "
      "titles; 全部 button = 10; %d per-tag counts each equal the number of "
      "cards carrying that tag; every card title is the meta title (not a SPEC "
      "code name); JSON-LD hasPart lists 10; new labels imrt/tomo/dibh/heart "
      "rendered as agreed" % ("/".join(str(n) for n in GROUP_SIZES),
                              len(want) - 1))

# 8 --------------------------------------------------- ld / nav / dates -------
nh1 = 0
for p in pages:
    s = rd(REPO, p)
    en = p.endswith("-en.html")
    chk(('<a href="topics-en.html" class="on">' if en
         else '<a href="topics.html" class="on">') in s, "%s nav active" % p)
    ld = json.loads(re.search(
        r'<script type="application/ld\+json">(.*?)</script>',
        s, re.S).group(1))
    chk(ld["about"]["@type"] == "MedicalCondition", "%s about type" % p)
    chk(ld["about"]["name"] == ("Breast cancer" if en else "乳癌"),
        "%s about.name=%s" % (p, ld["about"]["name"]))
    chk(ld["inLanguage"] == ("en" if en else "zh-Hant"), "%s inLanguage" % p)
    if ld["@type"] == "MedicalWebPage":
        chk(ld["datePublished"] == brt.DATE and ld["dateModified"] == brt.DATE,
            "%s dates" % p)
        slug = p[len("brt-"):-len(".html")]
        if en:
            slug = slug[:-3]
        want_t = (brt.EN if en else brt.ART)[slug]["title"]
        chk("<h1>%s</h1>" % html.escape(want_t, quote=False) in s,
            "%s h1 is not the meta title" % p)
        chk(ld["headline"] == want_t, "%s ld headline" % p)
        chk("<title>%s" % tb.esca(want_t)[:12] in s
            or tb.esca(want_t) in re.search(r"<title>(.*?)</title>",
                                            s, re.S).group(1),
            "%s <title> does not carry the meta title" % p)
        nh1 += 1
print("8. nav active state per language; JSON-LD about = MedicalCondition "
      "(乳癌%s) on all %d; datePublished = dateModified = %s on all %d "
      "articles; every h1 / <title> / ld headline is the meta title from "
      "meta/{A,B,C}%s.json"
      % ("" if ZH_ONLY else " / Breast cancer", NPAGE, brt.DATE, nh1,
         "" if ZH_ONLY else "{,-en}"))

# 9 -------------------------------------------------------------- pnav chain --
for lang, suf in LANGS:
    for i, slug in enumerate(ORD):
        s = rd(REPO, "brt-%s%s.html" % (slug, suf))
        pn = re.search(r'<div class="pnav">(.*?)</div>', s, re.S).group(1)
        if i == 0:
            chk(pn.startswith("<span></span>"), "%s%s first has prev"
                % (slug, suf))
        else:
            chk('class="pv" href="brt-%s%s.html"' % (ORD[i - 1], suf) in pn,
                "%s%s prev" % (slug, suf))
        if i == len(ORD) - 1:
            chk(pn.endswith("<span></span>"), "%s%s last has next"
                % (slug, suf))
        else:
            chk('class="nx" href="brt-%s%s.html"' % (ORD[i + 1], suf) in pn,
                "%s%s next" % (slug, suf))
print("9. pnav chains all 10 in SPEC reading order (A1 A2 A3 B1 B2 B3 C1 C2 C3 "
      "C4); ends use <span></span>")

# 10 ------------------------ everything outside the slots is intact -----------
def skeleton(s):
    s = tb.RE_TITLE.sub("@", s)
    s = tb.RE_DESC.sub("@", s)
    s = tb.RE_OGT.sub("@", s)
    s = tb.RE_OGD.sub("@", s)
    s = tb.RE_OGU.sub("@", s)
    s = tb.RE_CANON.sub("@", s)
    s = tb.RE_LD.sub("@", s)
    s = tb.RE_STYLE.sub("@", s)
    # zh-only: the hreflang block and the language chip are REMOVED from the
    # generated pages, so they are stripped from both sides here (their
    # absence is what check 5 asserts).  Round 2 substitutes them instead.
    if ZH_ONLY:
        s = tb.RE_ALTS.sub("", s)
        s = tb.RE_LANG.sub("", s)
    else:
        s = tb.RE_ALTS.sub("@", s)
        s = tb.RE_LANG.sub("@", s)
    s = re.sub(r'(<div class="article">).*?(\n  </div>\n</section>)',
               r"\1@\2", s, flags=re.S)
    s = re.sub(r'<section class="band narrow">.*?\n</section>', "@", s,
               flags=re.S)
    return s


for lang, suf in LANGS:
    t = skeleton(rd(REPO, ART_TPL[lang]))
    for slug in ORD:
        g = skeleton(rd(REPO, "brt-%s%s.html" % (slug, suf)))
        chk(g == t, "brt-%s%s: skeleton differs from %s"
            % (slug, suf, ART_TPL[lang]))
for lang, page in ([("zh", "brt.html")] if ZH_ONLY
                   else [("zh", "brt.html"), ("en", "brt-en.html")]):
    t = skeleton(rd(REPO, HUB_TPL[lang]))
    g = skeleton(rd(REPO, page))
    chk(g == t, "%s: skeleton differs from %s" % (page, HUB_TPL[lang]))
print("10. every byte outside the substituted slots (and the style, checked in "
      "4) is identical to the cc template%s"
      % ("; the hreflang block and the language chip are stripped from both "
         "sides this round" if ZH_ONLY
         else " (hreflang block and language chip compared as slots)"))

# 11 ------------------------------------------------- no double escaping ------
for p in pages:
    s = rd(REPO, p)
    chk("&amp;amp;" not in s and "&amp;quot;" not in s and "&#x27;" not in s
        and "&amp;gt;" not in s and "&amp;lt;" not in s,
        "%s: double-escaped entity" % p)
print("11. no double-escaped entities on any page")

# 12 ------------------- upload dir == exactly what still needs uploading -----
produced = ([os.path.join(REPO, n) for n in pages]
            + [os.path.join(REPO, n) for n in svgs]
            + [os.path.join(REPO, n) for n in shared])
want_upload, already_live = [], []
for path in produced:
    n = os.path.basename(path)
    b = base(n)
    if b is None or b != rd(path):
        want_upload.append(n)
    else:
        already_live.append(n)
have = sorted(os.listdir(UPLOAD))
chk(have == sorted(want_upload),
    "upload dir contents differ from the changed-vs-published set: "
    "extra %s / missing %s"
    % (sorted(set(have) - set(want_upload)),
       sorted(set(want_upload) - set(have))))
for n in have:
    chk(filecmp.cmp(os.path.join(UPLOAD, n), os.path.join(REPO, n),
                    shallow=False), "upload copy differs from repo: %s" % n)
for n in already_live:
    chk(rd(REPO, n) == base(n), "%s claimed unchanged but differs" % n)
npg = len([n for n in have if n in pages])
print("12. %s holds exactly the %d files whose bytes differ from the "
      "published version (%d pages + %d shared: %s), each byte-identical to "
      "its repo copy; the %d produced files already live (%s) are correctly "
      "absent"
      % (UPLOAD, len(have), npg, len(have) - npg,
         ", ".join(n for n in have if n not in pages),
         len(already_live),
         "%d svgs%s" % (len([n for n in already_live if n.endswith(".svg")]),
                        "".join(", " + n for n in already_live
                                if not n.endswith(".svg")))))

# 13 ---------- regenerated zh pages vs what is PUBLISHED: hreflang only ------
def strip_lang(t):
    """Remove the hreflang block and the language chip -- the only two things
    a round-2 rebuild is allowed to change on an already-published zh page."""
    t = tb.RE_ALTS.sub("", t)
    t = tb.RE_LANG.sub("", t)
    return t


zh_pages = ["brt.html"] + ["brt-%s.html" % s for s in ORD]
pure, bodydiff, unpublished = [], [], []
for n in zh_pages:
    pre = base(n)
    if pre is None:
        unpublished.append(n)
        continue
    now = rd(REPO, n)
    same = strip_lang(pre) == strip_lang(now)
    if not ZH_ONLY:
        # the three alternates and the chip must be present now and absent
        # before (round 1 shipped them stripped)
        chk(tb.RE_ALTS.search(now) is not None, "%s has no hreflang block" % n)
        chk(tb.RE_LANG.search(now) is not None, "%s has no language chip" % n)
        chk(tb.RE_ALTS.search(pre) is None and tb.RE_LANG.search(pre) is None,
            "%s published copy already had hreflang" % n)
    if same:
        chk(n not in EXPECTED_BODY_DIFF,
            "%s was expected to carry a body correction but does not" % n)
        pure.append(n)
        continue
    chk(n in EXPECTED_BODY_DIFF,
        "%s differs from the published page outside the hreflang lines" % n)
    if n not in EXPECTED_BODY_DIFF:
        continue
    # the remaining difference must sit inside the body-html slot
    a = re.search(r'<div class="body-html">\n(.*?)\n    </div>',
                  strip_lang(pre), re.S).group(1)
    b = re.search(r'<div class="body-html">\n(.*?)\n    </div>',
                  strip_lang(now), re.S).group(1)
    chk(strip_lang(pre).replace(a, "\x00") == strip_lang(now).replace(b, "\x00"),
        "%s differs outside the body slot as well" % n)
    d = [l for l in difflib.unified_diff(a.split("\n"), b.split("\n"),
                                         "published", "rebuilt", n=0,
                                         lineterm="")]
    changed = [l for l in d if l[:1] in "+-" and not l.startswith(("+++", "---"))]
    chk(len(changed) == 2, "%s: %d changed body lines, want 1 replaced"
        % (n, len(changed)))
    bodydiff.append((n, EXPECTED_BODY_DIFF[n], d))
if ZH_ONLY:
    print("13. \u672c\u8f2a\u70ba\u9996\u767c\uff0c\u7121\u5df2\u767c"
          "\u5e03\u7248\u672c\u53ef\u6bd4\u5c0d -- inert this round (%d "
          "zh pages not yet published)" % len(unpublished))
else:
    chk(not unpublished, "zh pages missing from the published version: %s"
        % unpublished)
    chk(len(pure) + len(bodydiff) == 11,
        "only %d of 11 zh pages compared" % (len(pure) + len(bodydiff)))
    chk(sorted(n for n, _, _ in bodydiff) == sorted(EXPECTED_BODY_DIFF),
        "body-diff set %s != declared %s"
        % (sorted(n for n, _, _ in bodydiff), sorted(EXPECTED_BODY_DIFF)))
    print("13. all %d Chinese pages diffed against their PUBLISHED version "
          "(%s): %d are hreflang-only -- with the 3 <link rel=alternate> lines "
          "and the <div class=\"lang\"> chip stripped from both sides they are "
          "byte-identical, and both were absent from the published copy; the "
          "remaining %d carry a declared source correction, confined to the "
          "body-html slot, one replaced line each:"
          % (len(zh_pages), BASE_REF, len(pure), len(bodydiff)))
    for n in pure:
        print("      %-24s hreflang-only" % n)
    for n, why, d in bodydiff:
        print("      %-24s body diff (%s):" % (n, why))
        for l in d:
            if l.startswith(("---", "+++")):
                continue
            if l.startswith("@@"):
                print("         %s" % l)
            else:
                print("         %s %s" % (l[0], l[1:].strip()))

print()
if fails:
    print("FAILURES (%d):" % len(fails))
    for f in fails:
        if f:
            print("   " + str(f))
    sys.exit(1)
print("ALL CHECKS PASSED  (mode: %s)"
      % ("ZH-ONLY round 1" if ZH_ONLY else "zh + en"))
