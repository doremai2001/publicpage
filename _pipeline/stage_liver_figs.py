# -*- coding: utf-8 -*-
"""Stage liver fragments for topicbuild: strip the lv- prefix (and the -en
suffix on the English side) and insert the site's article-figure markup at the
position the manifest prescribes — unlike cx (always after <h4> #2), each lv
figure carries placement.after_h4, the heading TEXT of the section the figure
closes.  The heading is matched in the zh fragment and the same section index
is reused for the en fragment (h4 counts are verified equal).  Alt text is
attribute-escaped (an lv alt legitimately contains '>' / '<' comparisons; a cx
alt once shipped an unescaped '>4 cm').  Set LV_STAGE to match liver.py's
_STAGE for the current session."""
import json, os, re, glob
LV = "/home/claude/liver"
STAGE = os.environ.get("LV_STAGE", "./staging-lv")

TPL = ('<figure class="article-figure">\n  <picture>\n'
 '    <source media="(max-width:620px)" srcset="%(mobile)s">\n'
 '    <img src="%(desktop)s" width="1440" height="%(h)d" loading="lazy" decoding="async" alt="%(alt)s">\n'
 '  </picture>\n  <figcaption>%(caption)s</figcaption>\n</figure>\n')
ea = lambda s: s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;").replace('"',"&quot;")
et = lambda s: s.replace("&","&amp;").replace("<","&lt;")


def svg_height(name):
    s = open(LV + "/figs/" + name, encoding="utf-8").read()
    vb = re.search(r'viewBox="0 0 (\d+) (\d+)"', s)
    assert vb and vb.group(1) == "1440", name
    return int(vb.group(2))


def insert_after_section(text, n, block):
    """Insert block at the end of h4 section #n (1-based), i.e. just before
    <h4> #(n+1).  Every lv placement has a following section (asserted)."""
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
    manifest = json.load(open(LV + "/figs/manifest.json", encoding="utf-8"))
    per = {}
    for fig in manifest:
        for slug in fig["used_by"]:
            per.setdefault(slug, []).append(fig)
    for p in sorted(glob.glob(LV + "/body/*.html")):
        slug = os.path.basename(p)[:-5]              # lv-<tail>
        zh = open(p, encoding="utf-8").read()
        en = open("%s/en/%s-en.html" % (LV, slug), encoding="utf-8").read()
        zh_h4 = re.findall(r"<h4>(.*?)</h4>", zh)
        assert len(zh_h4) == len(re.findall(r"<h4>", en)), slug
        figs = per.get(slug, [])
        secno = []                                   # 1-based h4 section no.
        for fig in figs:
            assert fig["placement"]["article"] == slug, fig["id"]
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
