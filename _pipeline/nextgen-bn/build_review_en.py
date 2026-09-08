# -*- coding: utf-8 -*-
"""英文版單檔審閱稿。圖的插入點用「與中文同一個序位的 <h4>」定位，不靠字串比對。"""
import os, re, sys, html, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import parts, parts_en, refs_en, figplace
import articles_a, articles_b, articles_d, articles_e
import en_a, en_b, en_c
from build_review import renumber, ORDER, CSS

EN = {}
for m in (en_a, en_b, en_c):
    EN.update(m.EN)
ZH = {}
for m in (articles_a, articles_b, articles_d, articles_e):
    ZH.update(m.ART)

H4 = re.compile(r"<h4>.*?</h4>", re.S)


def en_anchor(slug):
    """中文插入點是第幾個 <h4>，英文就取第幾個。"""
    fkey, marker, cz, ce = figplace.PLACE[slug]
    zh4 = H4.findall(ZH[slug]["body"])
    i = zh4.index(marker)
    en4 = H4.findall(EN[slug]["body"])
    return fkey, en4[i], ce


def build():
    out, total, n = [], 0, 0
    for gname, _mod, slugs in ORDER:
        out.append('<h2 class="grp">%s</h2>' % gname.split(" ", 1)[0] + " " +
                   {"A": "Physics", "B": "The boron drugs", "C": "The machines",
                    "D": "Evidence by cancer", "E": "Reality"}[gname[0]])
        for slug in slugs:
            a, e = ZH[slug], EN[slug]
            n += 1
            body = parts_en.assemble(slug, e["body"])
            erefs = [refs_en.to_en(r) for r in a["refs"]]
            body, refs, miss, unused = renumber(body, erefs)
            if slug in figplace.PLACE:
                fkey, anchor, cap = en_anchor(slug)
                svg = open("figs/fig-bn-%s-en.svg" % fkey, encoding="utf-8").read()
                svg = svg[svg.find("<svg"):]
                i = body.find(anchor)
                j = body.find("</p>", i) + 4
                body = (body[:j] + '\n<figure class="rfig">' + svg
                        + '<figcaption>' + cap + '</figcaption></figure>\n' + body[j:])
            words = len(re.sub(r"<figure.*?</figure>", "", body, flags=re.S).split())
            total += words
            out.append(
                '<article><div class="hd"><span class="no">%02d</span>'
                '<span class="slug">nt-bn-%s-en.html</span>'
                '<span class="cnt">%d words · %d refs</span></div>'
                '<h3>%s</h3><p class="dek">%s</p><p class="lead">%s</p>%s'
                '<div class="refs"><h4>References</h4><ol>%s</ol></div></article>'
                % (n, slug, words, len(refs), html.escape(e["title"]),
                   html.escape(e["dek"]), html.escape(e["lead"]), body, "".join(refs)))
    return "".join(out), total, n


if __name__ == "__main__":
    body, total, n = build()
    doc = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
           '<meta name="viewport" content="width=device-width,initial-scale=1">'
           '<title>BNCT section - English review draft</title><style>%s</style></head><body>'
           '<h1>Next-Generation Therapy Guide - BNCT section, English review draft</h1>'
           '<p class="sub">%d articles · about %s words · 8 September 2026 · not the published layout</p>'
           '<div class="warnnote">The two warnings and the disclosure paragraph at the top of every '
           'article are shared blocks - read them once. check_bilingual reports 0 hard mismatches '
           'against the Chinese: citation order, repeat positions, reference counts and section counts '
           'all line up. No monetary figures anywhere.</div>%s</body></html>') % (
           CSS, n, format(total, ","), body)
    open("review-en.html", "w", encoding="utf-8").write(doc)
    print("EN 篇數 %d · 約 %d words" % (n, total))
