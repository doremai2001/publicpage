# -*- coding: utf-8 -*-
"""Stage the brt fragments for topicbuild: strip the brt- prefix (and, in
round 2, the -en suffix on the English side) and insert the site's
article-figure markup at the position the manifest prescribes.

Like lv, every brt figure carries placement.after_h4 -- the heading TEXT of
the section the figure closes -- rather than a fixed ordinal.  The heading is
matched in the zh fragment; in round 2 the same section index is reused for
the en fragment (h4 counts are asserted equal first).

Figures are inserted HERE, into the staged copy the builder reads, so the
source fragments under /home/claude/brt/body stay figure-free and remain the
thing the verifier diffs the built body against.

Alt text is attribute-escaped (a brt alt legitimately contains ">" / "<" in
dose comparisons and "&" in trial names); captions are text nodes and get
"&" and "<" escaped only.

Set BRT_STAGE to match brt.py's _STAGE for the current session.

ROUND 1 IS ZH-ONLY: with zh_only=True (the default, taken from brt.ZH_ONLY)
the English side is skipped entirely, because /home/claude/brt/en does not
exist yet.  Round 2 passes zh_only=False and the en loop runs unchanged.
"""
import glob
import json
import os
import re

BRT = "/home/claude/brt"
STAGE = os.environ.get("BRT_STAGE", "./staging-brt")

TPL = ('<figure class="article-figure">\n  <picture>\n'
       '    <source media="(max-width:620px)" srcset="%(mobile)s">\n'
       '    <img src="%(desktop)s" width="1440" height="%(h)d" loading="lazy"'
       ' decoding="async" alt="%(alt)s">\n'
       '  </picture>\n  <figcaption>%(caption)s</figcaption>\n</figure>\n')

ea = lambda s: (s.replace("&", "&amp;").replace("<", "&lt;")
                 .replace(">", "&gt;").replace('"', "&quot;"))
et = lambda s: s.replace("&", "&amp;").replace("<", "&lt;")


def svg_height(name):
    s = open(BRT + "/figs/" + name, encoding="utf-8").read()
    vb = re.search(r'viewBox="0 0 (\d+) (\d+)"', s)
    assert vb and vb.group(1) == "1440", name
    return int(vb.group(2))


def insert_after_section(text, n, block):
    """Insert block at the end of h4 section #n (1-based), i.e. just before
    <h4> #(n+1).  Every brt placement has a following section (asserted)."""
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
        import brt
        zh_only = brt.ZH_ONLY
    os.makedirs(STAGE + "/body", exist_ok=True)
    if not zh_only:
        os.makedirs(STAGE + "/en", exist_ok=True)
    manifest = json.load(open(BRT + "/figs/manifest.json", encoding="utf-8"))
    per = {}
    for fig in manifest:
        for slug in fig["used_by"]:
            per.setdefault(slug, []).append(fig)
    for p in sorted(glob.glob(BRT + "/body/*.html")):
        slug = os.path.basename(p)[:-5]              # brt-<tail>
        zh = open(p, encoding="utf-8").read()
        zh_h4 = re.findall(r"<h4>(.*?)</h4>", zh)
        pairs = [("zh", zh, "body")]
        if not zh_only:
            en = open("%s/en/%s-en.html" % (BRT, slug), encoding="utf-8").read()
            assert len(zh_h4) == len(re.findall(r"<h4>", en)), slug
            pairs.append(("en", en, "en"))
        figs = per.get(slug, [])
        secno = []                                   # 1-based h4 section no.
        for fig in figs:
            assert fig["placement"]["article"] == slug, fig["id"]
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
