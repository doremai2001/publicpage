# -*- coding: utf-8 -*-
"""Stage the nextgen source fragments for topicbuild:

1. copy body/<nt-slug>.html -> staging/body/<slug>.html (prefix stripped, so
   the unchanged generator produces nt-<slug>.html without double-prefixing);
2. insert the site's article-figure markup at the agreed <h4> boundaries,
   zh files getting the zh SVGs/alt/captions, en files the -en ones.

Placement rule (from the build instructions):
  default        -> after the 2nd <h4> section (i.e. before the 3rd <h4>)
  special case   -> fig-nt-depth-dose in nt-how-to-read goes after the FIRST
                    <h4> section (before the 2nd <h4>)
  second figure  -> after the 4th <h4> (before the 5th <h4>)
"""
import json
import os
import re

NG = "/home/claude/nextgen"
SCR = os.path.dirname(os.path.abspath(__file__))
STAGE = os.path.join(SCR, "staging")

manifest = json.load(open(os.path.join(NG, "figs", "manifest.json"), encoding="utf-8"))

# viewBox heights of the desktop files, read from the SVGs themselves
def svg_height(name):
    s = open(os.path.join(NG, "figs", name), encoding="utf-8").read()
    vb = re.search(r'viewBox="0 0 (\d+) (\d+)"', s)
    assert vb and vb.group(1) == "1440", name
    return int(vb.group(2))

# figures per article, in manifest order (manifest order = first/second figure)
per_article = {}
for fig in manifest:
    for slug in fig["used_by"]:
        per_article.setdefault(slug, []).append(fig)

def before_h4(slug, fig_index, fig_id):
    if slug == "nt-how-to-read" and fig_id == "fig-nt-depth-dose":
        return 2          # after the 1st <h4> section
    if fig_index == 1:
        return 5          # second figure: after the 4th <h4>
    return 3              # default: after the 2nd <h4> section

FIG_TPL = (
    '<figure class="article-figure">\n'
    '  <picture>\n'
    '    <source media="(max-width:620px)" srcset="%(mobile)s">\n'
    '    <img src="%(desktop)s" width="1440" height="%(h)d" loading="lazy" '
    'decoding="async" alt="%(alt)s">\n'
    '  </picture>\n'
    '  <figcaption>%(caption)s</figcaption>\n'
    '</figure>\n'
)

def attr(s):
    assert "<" not in s and ">" not in s and "&" not in s and '"' not in s, s
    return s

def insert(text, n, block):
    """Insert block immediately before the n-th <h4> occurrence, reusing the
    file's own block separator (some fragments use \n, some \n\n)."""
    spots = [m.start() for m in re.finditer(r"<h4>", text)]
    i = spots[n - 1]
    j = i
    while text[j - 1] == "\n":
        j -= 1
    sep = text[j:i]
    assert sep in ("\n", "\n\n"), "odd separator before <h4> #%d" % n
    return text[:j] + sep + block.rstrip("\n") + sep + text[i:]

for lang, subdir in (("zh", "body"), ("en", "en")):
    for slug in ("nt-how-to-read", "nt-approval", "nt-proton",
                 "nt-carbon", "nt-flash", "nt-bnct"):
        src = os.path.join(NG, subdir, slug + ".html")
        text = open(src, encoding="utf-8").read()
        for fi, fig in enumerate(per_article.get(slug, [])):
            f = fig["files"]
            desktop = f["desktop"] if lang == "zh" else f["en"]
            mobile = f["mobile"] if lang == "zh" else f["en_mobile"]
            block = FIG_TPL % {
                "mobile": mobile,
                "desktop": desktop,
                "h": svg_height(desktop),
                "alt": attr(fig["zh_alt"] if lang == "zh" else fig["en_alt"]),
                "caption": fig["zh_caption"] if lang == "zh" else fig["en_caption"],
            }
            text = insert(text, before_h4(slug, fi, fig["id"]), block)
        out = os.path.join(STAGE, subdir, slug[len("nt-"):] + ".html")
        with open(out, "w", encoding="utf-8") as fh:
            fh.write(text)
        print("staged %-4s %-16s figs=%d" % (lang, slug, len(per_article.get(slug, []))))
