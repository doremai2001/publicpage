# -*- coding: utf-8 -*-
"""Stage the ec fragments for topicbuild: strip the ec- prefix (and the -en
suffix on the English side) and insert the site's article-figure markup at
the position the manifest prescribes.

Like lv / brt / pel, every ec figure carries placement.after_h4 -- the
heading TEXT of the section the figure closes -- rather than a fixed ordinal.
The heading is matched in the zh fragment and the same section index is
reused for the en fragment (h4 counts are asserted equal first).

PLACEMENT IS THE AUTHORITY.  All nine ec figures have a single-article
used_by that agrees with placement, so nine figures make nine insertions,
one per article in A3 / A4 / B1 / B2 / B5 / C1 / C2 / D1 / D3.

Figures are inserted HERE, into the staged copy the builder reads, so the
source fragments under /home/claude/esoph/body stay figure-free and remain
the thing the verifier diffs the built body against.

Alt text is attribute-escaped (&, <, >, "); captions are text nodes and get
"&" and "<" escaped only.  The <img> height is the desktop SVG's viewBox
height; the ec SVGs carry integer heights, but the pel-style round-half-up
is kept so a fractional one would not break the build.

Set EC_STAGE to match esoph.py's _STAGE.
"""
import decimal
import glob
import json
import os
import re

EC = "/home/claude/esoph"
STAGE = os.environ.get("EC_STAGE", "./staging-ec")

TPL = ('<figure class="article-figure">\n  <picture>\n'
       '    <source media="(max-width:620px)" srcset="%(mobile)s">\n'
       '    <img src="%(desktop)s" width="1440" height="%(h)d" loading="lazy"'
       ' decoding="async" alt="%(alt)s">\n'
       '  </picture>\n  <figcaption>%(caption)s</figcaption>\n</figure>\n')

ea = lambda s: (s.replace("&", "&amp;").replace("<", "&lt;")
                 .replace(">", "&gt;").replace('"', "&quot;"))
et = lambda s: s.replace("&", "&amp;").replace("<", "&lt;")


def svg_height(name):
    """Desktop viewBox height, rounded half-up to an HTML integer."""
    s = open(EC + "/figs/" + name, encoding="utf-8").read()
    vb = re.search(r'viewBox="0 0 (\d+(?:\.\d+)?) (\d+(?:\.\d+)?)"', s)
    assert vb and vb.group(1) == "1440", name
    return int(decimal.Decimal(vb.group(2)).quantize(
        decimal.Decimal("1"), rounding=decimal.ROUND_HALF_UP))


def insert_after_section(text, n, block):
    """Insert block at the end of h4 section #n (1-based), i.e. just before
    <h4> #(n+1).  Every ec placement has a following section (asserted)."""
    starts = [m.start() for m in re.finditer(r"<h4>", text)]
    assert n < len(starts), "figure would fall after the last <h4>"
    i = starts[n]          # start of the NEXT <h4>
    j = i
    while text[j - 1] == "\n":
        j -= 1
    sep = text[j:i]
    assert sep in ("\n", "\n\n"), repr(sep)
    return text[:j] + sep + block.rstrip("\n") + sep + text[i:]


def stage():
    os.makedirs(STAGE + "/body", exist_ok=True)
    os.makedirs(STAGE + "/en", exist_ok=True)
    manifest = json.load(open(EC + "/figs/manifest.json", encoding="utf-8"))
    per = {}
    for fig in manifest:
        art = fig["placement"]["article"]
        assert art in fig["used_by"], fig["id"]
        per.setdefault(art, []).append(fig)
    for p in sorted(glob.glob(EC + "/body/*.html")):
        slug = os.path.basename(p)[:-5]              # ec-<tail>
        zh = open(p, encoding="utf-8").read()
        en = open("%s/en/%s-en.html" % (EC, slug), encoding="utf-8").read()
        zh_h4 = re.findall(r"<h4>(.*?)</h4>", zh)
        assert len(zh_h4) == len(re.findall(r"<h4>", en)), slug
        figs = per.get(slug, [])
        secno = []                                   # 1-based h4 section no.
        for fig in figs:
            secno.append(zh_h4.index(fig["placement"]["after_h4"]) + 1)
        for lang, text, sub in (("zh", zh, "body"), ("en", en, "en")):
            for fig, n in zip(figs, secno):
                f = fig["files"]
                d = f["desktop"] if lang == "zh" else f["en"]
                m = f["mobile"] if lang == "zh" else f["en_mobile"]
                text = insert_after_section(text, n, TPL % {
                    "mobile": m, "desktop": d, "h": svg_height(d),
                    "alt": ea(fig["zh_alt"] if lang == "zh" else fig["en_alt"]),
                    "caption": et(fig["zh_caption"] if lang == "zh"
                                  else fig["en_caption"])})
            open(os.path.join(STAGE, sub, slug[3:] + ".html"),
                 "w", encoding="utf-8").write(text)


if __name__ == "__main__":
    stage()
