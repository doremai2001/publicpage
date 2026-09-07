# -*- coding: utf-8 -*-
"""建站時把 <figure> 插進 body fragment（正文本身不含圖，保持機械查核乾淨）。"""
import json, os, re
M = json.load(open("figs-manifest.json", encoding="utf-8"))
def block(f, lang="zh"):
    base = f["id"] + ("" if lang == "zh" else "-en")
    alt = f["%s_alt" % lang]; cap = f["%s_caption" % lang]
    return ('<figure class="article-figure">\n  <picture>\n'
            '    <source media="(max-width:620px)" srcset="%s-mobile.svg">\n'
            '    <img src="%s.svg" width="%d" height="%d" loading="lazy" decoding="async" alt="%s">\n'
            '  </picture>\n  <figcaption>%s</figcaption>\n</figure>' %
            (base, base, f["w"], f["h"], alt.replace('"', "&quot;"), cap))
def stage(bodydir="body", outdir="body-staged", lang="zh"):
    os.makedirs(outdir, exist_ok=True)
    used = {}
    for f in M:
        used.setdefault(f["used_by"], []).append(f)
    for name in os.listdir(bodydir):
        if not name.endswith(".html"): continue
        slug = name[:-5]
        h = open(os.path.join(bodydir, name), encoding="utf-8").read()
        for f in used.get(slug, []):
            anchor = f["anchor_%s" % lang]
            i = h.find(anchor)
            if i < 0: raise SystemExit("anchor not found in %s: %s" % (slug, anchor[:40]))
            j = h.find("\n", i + len(anchor))
            h = h[:j+1] + block(f, lang) + "\n" + h[j+1:]
        open(os.path.join(outdir, name), "w", encoding="utf-8").write(h)
    return sum(len(v) for v in used.values())
if __name__ == "__main__":
    print("staged", stage(), "figures")
