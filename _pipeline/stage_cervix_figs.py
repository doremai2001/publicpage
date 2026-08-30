# -*- coding: utf-8 -*-
"""Stage cervix fragments for topicbuild: strip the cx- prefix and insert the
site's article-figure markup after the 2nd <h4> section (no exceptions).
Alt text is attribute-escaped (a cx alt legitimately contains '>4 cm').
Set STAGE to match cervix.py's _STAGE for the current session."""
import json, os, re, glob
CX = "/home/claude/cervix"
STAGE = os.environ.get("CX_STAGE", "./staging-cx")
os.makedirs(STAGE + "/body", exist_ok=True); os.makedirs(STAGE + "/en", exist_ok=True)
manifest = json.load(open(CX + "/figs/manifest.json", encoding="utf-8"))
per = {}
for fig in manifest:
    ub = fig["used_by"]
    for slug in ([ub] if isinstance(ub, str) else ub):
        per.setdefault(slug, []).append(fig)
def svg_height(name):
    s = open(CX + "/figs/" + name, encoding="utf-8").read()
    vb = re.search(r'viewBox="0 0 (\d+) (\d+)"', s); assert vb and vb.group(1) == "1440", name
    return int(vb.group(2))
TPL = ('<figure class="article-figure">\n  <picture>\n'
 '    <source media="(max-width:620px)" srcset="%(mobile)s">\n'
 '    <img src="%(desktop)s" width="1440" height="%(h)d" loading="lazy" decoding="async" alt="%(alt)s">\n'
 '  </picture>\n  <figcaption>%(caption)s</figcaption>\n</figure>\n')
ea = lambda s: s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;").replace('"',"&quot;")
et = lambda s: s.replace("&","&amp;").replace("<","&lt;")
def insert(text, n, block):
    i = [m.start() for m in re.finditer(r"<h4>", text)][n-1]; j = i
    while text[j-1] == "\n": j -= 1
    sep = text[j:i]; assert sep in ("\n", "\n\n")
    return text[:j] + sep + block.rstrip("\n") + sep + text[i:]
for lang, sub in (("zh","body"),("en","en")):
    for p in sorted(glob.glob(CX+"/body/*.html")):
        slug = os.path.basename(p)[:-5]
        text = open(f"{CX}/{sub}/{slug}.html", encoding="utf-8").read()
        for fig in per.get(slug, []):
            f = fig["files"]
            d = f["desktop"] if lang=="zh" else f["en"]; m = f["mobile"] if lang=="zh" else f["en_mobile"]
            text = insert(text, 3, TPL % {"mobile":m,"desktop":d,"h":svg_height(d),
                "alt":ea(fig["zh_alt"] if lang=="zh" else fig["en_alt"]),
                "caption":et(fig["zh_caption"] if lang=="zh" else fig["en_caption"])})
        open(os.path.join(STAGE, sub, slug[3:] + ".html"), "w", encoding="utf-8").write(text)
