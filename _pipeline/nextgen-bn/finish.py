# -*- coding: utf-8 -*-
"""把既有頁面的導覽指向改掉、補 sitemap 與 topics 卡片，全部寫進 out/。"""
import os, re, shutil, sys
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = "/root/publicpage"
OUT = os.path.join(HERE, "out")
BASE = "https://doremai2001.github.io/publicpage/"
ORDER = ["principle", "dose", "depth", "drugs", "pet", "newagents", "thor", "accelerator",
         "headneck", "gbm", "newgbm", "melanoma", "meningioma", "others", "safety", "approval", "who"]


def out(name):
    return os.path.join(OUT, name)


def load(name):
    p = out(name)
    return open(p if os.path.exists(p) else os.path.join(REPO, name), encoding="utf-8").read()


def save(name, s):
    open(out(name), "w", encoding="utf-8").write(s)


def main():
    changed = []

    # 1) 20 篇熱治療 × 中英：backlink 與 tagchip 改指向 nt-ht
    ht = sorted(n for n in os.listdir(REPO) if n.startswith("nt-ht-") and n.endswith(".html"))
    for n in ht:
        s = load(n)
        suf = "-en" if n.endswith("-en.html") else ""
        o = s
        s = s.replace('class="backlink" href="nt%s.html"' % suf,
                      'class="backlink" href="nt-ht%s.html"' % suf)
        s = s.replace('class="tagchip" href="nt%s.html?tag=' % suf,
                      'class="tagchip" href="nt-ht%s.html?tag=' % suf)
        if s != o:
            save(n, s); changed.append(n)

    # 2) nt-bnct：下一篇由 nt-ht-what 改成 BNCT 分組第一篇
    for suf in ("", "-en"):
        n = "nt-bnct%s.html" % suf
        s = load(n)
        first = "nt-bn-principle%s.html" % suf
        title = re.search(r"<h1>(.*?)</h1>",
                          load(first), re.S).group(1)
        s2 = re.sub(r'<a class="nx" href="nt-ht-what%s\.html"><span>(.*?)</span>.*?</a>' % suf,
                    lambda m: '<a class="nx" href="%s"><span>%s</span>%s</a>' % (first, m.group(1), title),
                    s, count=1, flags=re.S)
        if s2 != s:
            save(n, s2); changed.append(n)

    # 3) nt-ht-what：上一篇改成空（它現在是熱治療分組的第一篇）
    for suf in ("", "-en"):
        n = "nt-ht-what%s.html" % suf
        s = load(n)
        s2 = re.sub(r'<a class="pv" href="nt-bnct%s\.html">.*?</a>' % suf, "<span></span>",
                    s, count=1, flags=re.S)
        if s2 != s:
            save(n, s2); changed.append(n)

    # 4) sitemap
    sm = load("sitemap.xml")
    def entry(name, prio):
        return ('  <url><loc>%s%s</loc><lastmod>2026-09-08</lastmod>'
                '<changefreq>monthly</changefreq><priority>%s</priority></url>\n' % (BASE, name, prio))
    lines = sm.splitlines(True)

    def insert_after(lines, loc, block):
        for i, ln in enumerate(lines):
            if "<loc>%s%s</loc>" % (BASE, loc) in ln:
                return lines[:i + 1] + block + lines[i + 1:]
        raise RuntimeError("sitemap anchor not found: " + loc)

    if "nt-bn.html" not in sm:
        lines = insert_after(lines, "nt.html", [entry("nt-bn.html", "0.80"), entry("nt-ht.html", "0.80")])
        lines = insert_after(lines, "nt-en.html", [entry("nt-bn-en.html", "0.70"), entry("nt-ht-en.html", "0.70")])
        lines = insert_after(lines, "nt-bnct.html", [entry("nt-bn-%s.html" % s, "0.75") for s in ORDER])
        lines = insert_after(lines, "nt-bnct-en.html", [entry("nt-bn-%s-en.html" % s, "0.65") for s in ORDER])
        save("sitemap.xml", "".join(lines)); changed.append("sitemap.xml")

    # 5) topics 卡片的篇數與分段標籤
    for suf, n26, n43, steps in (("", "26 篇", "43 篇", ("熱治療二十篇", "兩個深入分組")),
                                 ("-en", "26 articles", "43 articles", ("Twenty on hyperthermia", "Two sections in depth"))):
        n = "topics%s.html" % suf
        s = load(n)
        o = s
        s = s.replace('<span class="n">%s</span>' % n26, '<span class="n">%s</span>' % n43)
        s = s.replace("<span>%s</span>" % steps[0], "<span>%s</span>" % steps[1])
        if s != o:
            save(n, s); changed.append(n)

    total = len([x for x in os.listdir(OUT) if x.endswith(".html")])
    print("改到既有頁面 %d 個：%s" % (len(changed), ", ".join(changed[:6]) + (" …" if len(changed) > 6 else "")))
    print("out/ 目前 %d 個 html、%d 個 svg" %
          (total, len([x for x in os.listdir(OUT) if x.endswith(".svg")])))


if __name__ == "__main__":
    main()
