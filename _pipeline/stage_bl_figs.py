# -*- coding: utf-8 -*-
"""Stage the bl fragments for topicbuild: strip the bl- prefix (and, on the
English side, the -en suffix) and insert the site's article-figure markup at
the position the manifest prescribes.

Unlike em -- whose English fragments were en/em-<slug>.html, the same
basename as the Chinese one, with only the directory telling them apart --
the bl English fragments are en/bl-<slug>-en.html.  Both the prefix and the
suffix come off here, so the builder's "<PREFIX>-<slug>.html" composes
cleanly for both languages.

Like lv / brt / pel / ec / gb / em, every bl figure carries
placement.after_h4 -- the heading TEXT of the section the figure closes --
rather than a fixed ordinal.  The heading is matched in the zh fragment and
the same section index is reused for the en fragment (h4 counts are asserted
equal first), because the English headings are rewritten with tension rather
than translated word for word and so never match by string.

PLACEMENT IS A LIST, one entry per article the figure is inserted into,
and it must agree with used_by as a SET.  bt could get away with a single
article because every bt figure served one article; fig-bl-followup does
not -- SPEC 七 item 9 and 修正 26 item 9 draw it for B4 AND C5, and the
figure really is two columns, one per route -- so a single-article
placement could not express it and the figure silently missed C5.  Twelve
figures therefore make THIRTEEN insertions per language: A1 / A2 / A3 /
B1 / B2 / B4 / C1 / C3 / C4 / C5 / D1 / E1 / E2.

Where one article takes more than one figure the placements are inserted
in descending section order, so that an earlier insertion cannot shift the
<h4> offsets a later one is computed against; the per-article list is
asserted to be in ascending section order first, because the verifier
compares the built page's figure positions against the manifest order.

Figures are inserted HERE, into the staged copy the builder reads, so the
source fragments under /home/claude/bl/body and /home/claude/bl/en stay
figure-free and remain the thing the verifier diffs the built body against.

Alt text is attribute-escaped (&, <, >, "); captions are text nodes and get
"&" and "<" escaped only.  The <img> height is the per-language desktop
SVG's viewBox height; the bl SVGs carry integer heights, but the pel-style
round-half-up is kept so a fractional one would not break the build.

Set BL_STAGE to match bl.py's _STAGE.
"""
import decimal
import glob
import json
import os
import re

BL = "/home/claude/bl"
STAGE = os.environ.get("BL_STAGE", "./staging-bl")

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
    s = open(BL + "/figs/" + name, encoding="utf-8").read()
    vb = re.search(r'viewBox="0 0 (\d+(?:\.\d+)?) (\d+(?:\.\d+)?)"', s)
    assert vb and vb.group(1) == "1440", name
    return int(decimal.Decimal(vb.group(2)).quantize(
        decimal.Decimal("1"), rounding=decimal.ROUND_HALF_UP))


def insert_after_section(text, n, block):
    """Insert block at the end of h4 section #n (1-based), i.e. just before
    <h4> #(n+1).  Every bt placement has a following section (asserted)."""
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
    manifest = json.load(open(BL + "/figs/manifest.json", encoding="utf-8"))
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
    for p in sorted(glob.glob(BL + "/body/*.html")):
        slug = os.path.basename(p)[:-5]              # bt-<tail>
        zh = open(p, encoding="utf-8").read()
        en = open("%s/en/%s-en.html" % (BL, slug), encoding="utf-8").read()
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
