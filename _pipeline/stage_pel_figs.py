# -*- coding: utf-8 -*-
"""Stage the pel fragments for topicbuild: strip the pel- prefix (and, in
round 2, the -en suffix on the English side) and insert the site's
article-figure markup at the position the manifest prescribes.

Like lv and brt, every pel figure carries placement.after_h4 -- the heading
TEXT of the section the figure closes -- rather than a fixed ordinal.  The
heading is matched in the zh fragment; in round 2 the same section index is
reused for the en fragment (h4 counts are asserted equal first).

PLACEMENT IS THE AUTHORITY, NOT used_by.  Four of the five pel figures have a
single-article used_by that agrees with placement.  fig-pel-timeline is the
exception: its used_by lists BOTH pel-colitis and pel-late, but the manifest
gives it exactly ONE placement object, naming pel-colitis and the h4
〈四段時間，指引都寫進去了〉.  There is no second placement, and pel-late's
body neither mentions nor needs a second copy, so the figure is inserted
ONCE, in pel-colitis; used_by's second entry records that pel-late covers the
same material, not that the image is repeated.  Five figures, five insertions.

Figures are inserted HERE, into the staged copy the builder reads, so the
source fragments under /home/claude/pel/body stay figure-free and remain the
thing the verifier diffs the built body against.

Alt text is attribute-escaped (&, <, >, "); captions are text nodes and get
"&" and "<" escaped only.

The pel SVGs carry FRACTIONAL viewBox heights (e.g. 1894.65), unlike every
earlier topic's.  The width/height attributes of <img> are HTML integers, so
the height is rounded to the nearest integer with round-half-up; verify_pel
recomputes it the same way, from the same viewBox.

Set PEL_STAGE to match pel.py's _STAGE for the current session.

ROUND 1 WAS ZH-ONLY: with zh_only=True (the default, taken from pel.ZH_ONLY)
the English side is skipped entirely, because /home/claude/pel/en was empty.
ROUND 2 IS ACTIVE: zh_only=False and the en loop runs unchanged, taking the
en / en_mobile files and en_alt / en_caption from the same manifest entries
and reusing the h4 section index matched in the Chinese fragment.
"""
import decimal
import glob
import json
import os
import re

PEL = "/home/claude/pel"
STAGE = os.environ.get("PEL_STAGE", "./staging-pel")

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
    s = open(PEL + "/figs/" + name, encoding="utf-8").read()
    vb = re.search(r'viewBox="0 0 (\d+(?:\.\d+)?) (\d+(?:\.\d+)?)"', s)
    assert vb and vb.group(1) == "1440", name
    return int(decimal.Decimal(vb.group(2)).quantize(
        decimal.Decimal("1"), rounding=decimal.ROUND_HALF_UP))


def insert_after_section(text, n, block):
    """Insert block at the end of h4 section #n (1-based), i.e. just before
    <h4> #(n+1).  Every pel placement has a following section (asserted)."""
    starts = [m.start() for m in re.finditer(r"<h4>", text)]
    assert n < len(starts), "figure would fall after the last <h4>"
    i = starts[n]          # start of the NEXT <h4>
    j = i
    while text[j - 1] == "\n":
        j -= 1
    sep = text[j:i]
    assert sep in ("\n", "\n\n"), repr(sep)
    return text[:j] + sep + block.rstrip("\n") + sep + text[i:]


def stage(zh_only=None):
    if zh_only is None:
        import pel
        zh_only = pel.ZH_ONLY
    os.makedirs(STAGE + "/body", exist_ok=True)
    if not zh_only:
        os.makedirs(STAGE + "/en", exist_ok=True)
    manifest = json.load(open(PEL + "/figs/manifest.json", encoding="utf-8"))
    per = {}
    for fig in manifest:
        art = fig["placement"]["article"]
        assert art in fig["used_by"], fig["id"]
        per.setdefault(art, []).append(fig)
    for p in sorted(glob.glob(PEL + "/body/*.html")):
        slug = os.path.basename(p)[:-5]              # pel-<tail>
        zh = open(p, encoding="utf-8").read()
        zh_h4 = re.findall(r"<h4>(.*?)</h4>", zh)
        pairs = [("zh", zh, "body")]
        if not zh_only:
            en = open("%s/en/%s-en.html" % (PEL, slug), encoding="utf-8").read()
            assert len(zh_h4) == len(re.findall(r"<h4>", en)), slug
            pairs.append(("en", en, "en"))
        figs = per.get(slug, [])
        secno = []                                   # 1-based h4 section no.
        for fig in figs:
            secno.append(zh_h4.index(fig["placement"]["after_h4"]) + 1)
        for lang, text, sub in pairs:
            for fig, n in zip(figs, secno):
                f = fig["files"]
                d = f["desktop"] if lang == "zh" else f["en"]
                m = f["mobile"] if lang == "zh" else f["en_mobile"]
                text = insert_after_section(text, n, TPL % {
                    "mobile": m, "desktop": d, "h": svg_height(d),
                    "alt": ea(fig["zh_alt"] if lang == "zh" else fig["en_alt"]),
                    "caption": et(fig["zh_caption"] if lang == "zh"
                                  else fig["en_caption"])})
            open(os.path.join(STAGE, sub, slug[4:] + ".html"),
                 "w", encoding="utf-8").write(text)


if __name__ == "__main__":
    stage()
