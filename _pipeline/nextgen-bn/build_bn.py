# -*- coding: utf-8 -*-
"""產出 17 篇 × 中英的文章頁到 out/，並把 hub 指向改成 nt-bn.html。"""
import os, re, sys, shutil
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.dirname(HERE))
import topicbuild as tb
import nextgen_bn as topic
import figplace

REPO = "/root/publicpage"
OUT = os.path.join(HERE, "out")
TPL = {"zh": os.path.join(REPO, "nt-ht-dose.html"),
       "en": os.path.join(REPO, "nt-ht-dose-en.html")}
H4 = re.compile(r"<h4>.*?</h4>", re.S)


def insert_figures(path, slug, lang):
    """把 <figure> 插在與中文同序位的 <h4> 之後的第一段之後。"""
    base = slug[3:]
    if base not in figplace.PLACE:
        return False
    fkey, zh_anchor, cz, ce = figplace.PLACE[base]
    zh_body = open(os.path.join(HERE, "body_bn", slug + ".html"), encoding="utf-8").read()
    i = H4.findall(zh_body).index(zh_anchor)
    s = open(path, encoding="utf-8").read()
    body = re.search(r'<div class="body-html">\n(.*?)\n    </div>', s, re.S).group(1)
    anchor = H4.findall(body)[i]
    j = body.find(anchor)
    k = body.find("</p>", j) + 4
    cap = cz if lang == "zh" else ce
    alt = figplace.ALT[fkey][0 if lang == "zh" else 1]
    sizes = re.search(r'width="(\d+)" height="(\d+)"',
                      open(os.path.join(HERE, "figs", "fig-bn-%s%s.svg"
                                        % (fkey, "" if lang == "zh" else "-en")),
                           encoding="utf-8").read())
    fig = figplace.figure_html(fkey, lang, cap, alt, (int(sizes.group(1)), int(sizes.group(2))))
    nb = body[:k] + "\n" + fig + body[k:]
    s = s.replace(body, nb, 1)
    open(path, "w", encoding="utf-8").write(s)
    return True


def main():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    pages = []
    for lang in ("zh", "en"):
        pages += tb.build(topic, lang, TPL[lang], OUT)
    # hub 指向：文章頁的 backlink 與 tagchip 從 nt.html 改成 nt-bn.html
    nfig = 0
    for p in pages:
        s = open(p, encoding="utf-8").read()
        s = s.replace('class="backlink" href="nt.html"', 'class="backlink" href="nt-bn.html"')
        s = s.replace('class="backlink" href="nt-en.html"', 'class="backlink" href="nt-bn-en.html"')
        s = s.replace('class="tagchip" href="nt.html?tag=', 'class="tagchip" href="nt-bn.html?tag=')
        s = s.replace('class="tagchip" href="nt-en.html?tag=', 'class="tagchip" href="nt-bn-en.html?tag=')
        open(p, "w", encoding="utf-8").write(s)
        name = os.path.basename(p)
        slug = name[3:-5].replace("-en", "") if name.endswith("-en.html") else name[3:-5]
        lang = "en" if name.endswith("-en.html") else "zh"
        if insert_figures(p, slug, lang):
            nfig += 1
    for n in sorted(os.listdir(os.path.join(HERE, "figs"))):
        if n.endswith(".svg"):
            shutil.copy2(os.path.join(HERE, "figs", n), os.path.join(OUT, n))
    print("文章頁 %d 個（中英各 %d），插圖 %d 處，SVG %d 個"
          % (len(pages), len(pages) // 2, nfig,
             len([n for n in os.listdir(OUT) if n.endswith(".svg")])))


if __name__ == "__main__":
    main()
