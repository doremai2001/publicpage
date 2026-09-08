# -*- coding: utf-8 -*-
"""產出中英兩側的 body fragment（供 check_bilingual 比對），以及雙語審閱稿。"""
import os, re, sys, html, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import parts, parts_en, refs_en, figplace
import articles_a, articles_b, articles_d, articles_e
import en_a, en_b, en_c
from build_review import renumber, ORDER

EN = {}
for m in (en_a, en_b, en_c):
    EN.update(m.EN)
ZH = {}
for m in (articles_a, articles_b, articles_d, articles_e):
    ZH.update(m.ART)

ORDER_SLUGS = [s for _g, _m, ss in ORDER for s in ss]


def frag(body, refs, lang="zh"):
    h3 = "參考資料" if lang == "zh" else "References"
    return (body + "\n<hr>\n<h3>%s</h3>\n<ol>\n" % h3 + "\n".join(refs)
            + "\n</ol>\n<p></p>\n")


def main():
    for d in ("body", "en"):
        if not os.path.isdir(d):
            os.makedirs(d)
    rows = []
    for slug in ORDER_SLUGS:
        a = ZH[slug]
        zb = parts.assemble(parts.DISPLACE[slug], a["body"])
        zb, zrefs, m1, u1 = renumber(zb, a["refs"])
        open("body/%s.html" % slug, "w", encoding="utf-8").write(frag(zb, zrefs, "zh"))

        e = EN[slug]
        eb = parts_en.assemble(slug, e["body"])
        erefs_src = [refs_en.to_en(r) for r in a["refs"]]
        eb, erefs, m2, u2 = renumber(eb, erefs_src)
        open("en/%s.html" % slug, "w", encoding="utf-8").write(frag(eb, erefs, "en"))

        rows.append((slug, len(re.sub(r"<[^>]+>", "", zb).replace(" ", "").replace("\n", "")),
                     len(re.sub(r"<[^>]+>", " ", eb).split()), len(zrefs), len(erefs),
                     zb.count("<h4>"), eb.count("<h4>"), m1 + u1 + m2 + u2))
    print("slug            zh字  en字 refs h4 問題")
    for r in rows:
        print("%-15s %5d %5d  %d/%d %d/%d %s" % (r[0], r[1], r[2], r[3], r[4], r[5], r[6],
                                                 r[7] if r[7] else ""))
    meta = {s: dict(title=EN[s]["title"], dek=EN[s]["dek"], lead=EN[s]["lead"]) for s in ORDER_SLUGS}
    open("meta-all-en.json", "w", encoding="utf-8").write(json.dumps(meta, ensure_ascii=False, indent=1))
    print("\n中文 %d 篇、英文 %d 篇寫入 body/ 與 en/" % (len(rows), len(rows)))


if __name__ == "__main__":
    main()
