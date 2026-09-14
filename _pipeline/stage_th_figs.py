# -*- coding: utf-8 -*-
"""Stage the th fragments for topicbuild: strip the th- prefix (and, on the
English side, the -en suffix) and insert the site's article-figure markup at
the position the manifest prescribes.

The th English fragments are en/th-<slug>-en.html -- both the prefix and the
suffix come off here, so the builder's "<PREFIX>-<slug>.html" composes
cleanly for both languages (the bl / bt convention, not em's).

Like lv / brt / pel / ec / gb / em / bl, every th figure carries
placement.after_h4 -- the heading TEXT of the section the figure closes --
rather than a fixed ordinal.  The heading is matched in the zh fragment and
the same section index is reused for the en fragment (h4 counts are asserted
equal first), because the English headings are rewritten with tension rather
than translated word for word and so never match by string.

PLACEMENT IS A LIST, one entry per article the figure is inserted into, and
it must agree with used_by as a SET -- the mechanism bl's round had to fix
after a single-dict placement silently dropped a figure from the second
article that claimed it.  Here fig-th-mtc-atc is the two-article figure
(SPEC 十 item 12 draws it for E1 AND E2, one column per disease), so twelve
figures make THIRTEEN insertions per language: A1 / A2 / A4 / A5 / B1 / B2 /
B4 / C1 / D1 / D2 / D4 / E1 / E2.

Where one article takes more than one figure the placements are inserted in
descending section order, so that an earlier insertion cannot shift the <h4>
offsets a later one is computed against; the per-article list is asserted to
be in ascending section order first, because the verifier compares the built
page's figure positions against the manifest order.  (No th article takes
two figures, but the rule is kept: it costs nothing and the next topic
copies this file.)

Figures are inserted HERE, into the staged copy the builder reads, so the
source fragments under /home/claude/th/body and /home/claude/th/en stay
figure-free and remain the thing the verifier diffs the built body against.

Alt text is attribute-escaped (&, <, >, "); captions are text nodes and get
"&" and "<" escaped only.  The <img> height is the per-language desktop
SVG's viewBox height; the th SVGs carry integer heights, but the pel-style
round-half-up is kept so a fractional one would not break the build.

Set TH_STAGE to match th.py's _STAGE.
"""
import decimal
import glob
import json
import os
import re

TH = "/home/claude/th"
STAGE = os.environ.get("TH_STAGE", "./staging-th")

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
    s = open(TH + "/figs/" + name, encoding="utf-8").read()
    vb = re.search(r'viewBox="0 0 (\d+(?:\.\d+)?) (\d+(?:\.\d+)?)"', s)
    assert vb and vb.group(1) == "1440", name
    return int(decimal.Decimal(vb.group(2)).quantize(
        decimal.Decimal("1"), rounding=decimal.ROUND_HALF_UP))


def insert_after_section(text, n, block):
    """Insert block at the end of h4 section #n (1-based), i.e. just before
    <h4> #(n+1).  Every th placement has a following section (asserted)."""
    starts = [m.start() for m in re.finditer(r"<h4>", text)]
    assert n < len(starts), "figure would fall after the last <h4>"
    i = starts[n]          # start of the NEXT <h4>
    j = i
    while text[j - 1] == "\n":
        j -= 1
    sep = text[j:i]
    # bl asserted sep in ("\n", "\n\n").  Two of the th Chinese fragments
    # (th-mtc, th-taiwan) separate a few sections with THREE newlines, so the
    # assertion is on the character class instead and the separator found is
    # reproduced on both sides of the figure.  Nothing downstream cares: the
    # verifier normalises runs of blank lines on both sides before comparing
    # the built body with the source.
    assert sep and set(sep) == {"\n"}, repr(sep)
    return text[:j] + sep + block.rstrip("\n") + sep + text[i:]


def stage():
    os.makedirs(STAGE + "/body", exist_ok=True)
    os.makedirs(STAGE + "/en", exist_ok=True)
    manifest = json.load(open(TH + "/figs/manifest.json", encoding="utf-8"))
    per = {}
    nplace = 0
    for fig in manifest:
        places = fig["placement"]
        assert isinstance(places, list) and places, fig["id"]
        arts = [pl["article"] for pl in places]
        assert sorted(arts) == sorted(fig["used_by"]), fig["id"]
        for pl in places:
            per.setdefault(pl["article"], []).append((fig, pl))
        nplace += len(places)
    n_ins = 0
    for p in sorted(glob.glob(TH + "/body/*.html")):
        slug = os.path.basename(p)[:-5]              # th-<tail>
        zh = open(p, encoding="utf-8").read()
        en = open("%s/en/%s-en.html" % (TH, slug), encoding="utf-8").read()
        zh_h4 = re.findall(r"<h4>(.*?)</h4>", zh)
        assert len(zh_h4) == len(re.findall(r"<h4>", en)), slug
        figs = per.get(slug, [])
        secno = []                                   # 1-based h4 section no.
        for fig, pl in figs:
            secno.append(zh_h4.index(pl["after_h4"]) + 1)
        assert secno == sorted(secno) and len(set(secno)) == len(secno), slug
        for lang, text, sub in (("zh", zh, "body"), ("en", en, "en")):
            # descending, so an insertion never moves a later one's <h4>
            for (fig, pl), n in sorted(zip(figs, secno),
                                       key=lambda t: -t[1]):
                f = fig["files"]
                d = f["desktop"] if lang == "zh" else f["en"]
                m = f["mobile"] if lang == "zh" else f["en_mobile"]
                text = insert_after_section(text, n, TPL % {
                    "mobile": m, "desktop": d, "h": svg_height(d),
                    "alt": ea(fig["zh_alt"] if lang == "zh" else fig["en_alt"]),
                    "caption": et(fig["zh_caption"] if lang == "zh"
                                  else fig["en_caption"])})
                n_ins += 1
            open(os.path.join(STAGE, sub, slug[3:] + ".html"),
                 "w", encoding="utf-8").write(text)
    assert n_ins == 2 * nplace, (n_ins, nplace)
    return n_ins


if __name__ == "__main__":
    print("figure insertions:", stage())
