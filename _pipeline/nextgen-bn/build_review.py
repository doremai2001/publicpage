# -*- coding: utf-8 -*-
"""把 17 篇組裝成單檔審閱稿，並依首次出現順序重編引用號（沿用熱治療那組的 renumber 做法）。"""
import os, re, sys, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import parts, articles_a, articles_b, articles_d, articles_e, figplace

ORDER = [
 ("A 原理", articles_a, ["principle", "dose", "depth"]),
 ("B 硼藥物", articles_b, ["drugs", "pet", "newagents"]),
 ("C 機器", articles_b, ["thor", "accelerator"]),
 ("D 各癌別的實證", articles_d, ["headneck", "gbm", "newgbm", "melanoma", "meningioma", "others"]),
 ("E 現實面", articles_e, ["safety", "approval", "who"]),
]

RE_CIT = re.compile(r'<a href="([^"]+)" target="_blank" rel="noopener"><sup class="cit">\[(\d+)\]</sup></a>')
RE_REF_URL = re.compile(r'<a href="([^"]+)" target="_blank" rel="noopener">')


def renumber(body, refs):
    """依 body 裡引用連結首次出現的順序重新編號，並照同一順序重排參考清單。"""
    order, seen = [], set()
    for m in RE_CIT.finditer(body):
        u = m.group(1)
        if u not in seen:
            seen.add(u); order.append(u)
    ref_by_url = {}
    for item in refs:
        m = RE_REF_URL.search(item)
        if not m:
            raise RuntimeError("ref item has no link: %s" % item[:80])
        ref_by_url[m.group(1)] = item
    missing = [u for u in order if u not in ref_by_url]
    unused = [u for u in ref_by_url if u not in seen]
    num = {u: i + 1 for i, u in enumerate(order)}
    body = RE_CIT.sub(lambda m: '<a href="%s" target="_blank" rel="noopener"><sup class="cit">[%d]</sup></a>'
                      % (m.group(1), num[m.group(1)]), body)
    return body, [ref_by_url[u] for u in order], missing, unused


def build():
    out, problems, total = [], [], 0
    n = 0
    for gname, mod, slugs in ORDER:
        out.append('<h2 class="grp">%s</h2>' % gname)
        for slug in slugs:
            a = mod.ART[slug]
            n += 1
            body = parts.assemble(parts.DISPLACE[slug], a["body"])
            if slug in figplace.PLACE:
                fkey, marker, cz, _ce = figplace.PLACE[slug]
                svg = open("figs/fig-bn-%s.svg" % fkey, encoding="utf-8").read()
                svg = svg[svg.find("<svg"):]
                # 插在該小標之後的第一段之後
                i = body.find(marker)
                j = body.find("</p>", i) + 4
                body = (body[:j] + '\n<figure class="rfig">' + svg
                        + '<figcaption>' + cz + '</figcaption></figure>\n' + body[j:])
            body, refs, missing, unused = renumber(body, a["refs"])
            if missing: problems.append("%s: 引用了沒有參考條目的網址 %s" % (slug, missing))
            if unused: problems.append("%s: 參考條目沒有被引用 %s" % (slug, unused))
            txt = re.sub(r"<figure.*?</figure>", "", body, flags=re.S)
            txt = re.sub(r"<[^>]+>", "", txt)
            chars = len(txt.replace(" ", "").replace("\n", ""))
            total += chars
            out.append(
                '<article><div class="hd"><span class="no">%02d</span>'
                '<span class="slug">nt-bn-%s.html</span>'
                '<span class="cnt">%d 字 · 參考 %d 篇</span></div>'
                '<h3>%s</h3><p class="dek">%s</p>'
                '<p class="lead">%s</p>%s'
                '<div class="refs"><h4>參考資料</h4><ol>%s</ol></div></article>'
                % (n, slug, chars, len(refs), html.escape(a["h1"]), html.escape(a["dek"]),
                   html.escape(a["lead"]), body, "".join(refs)))
    return "".join(out), problems, total, n


CSS = """
body{max-width:820px;margin:0 auto;padding:28px 18px 80px;font-family:-apple-system,"Noto Sans TC",sans-serif;line-height:1.85;color:#1c1c1c;background:#fbfaf7}
h1{font-size:24px;margin:0 0 6px} .sub{color:#666;font-size:14px;margin:0 0 28px}
h2.grp{margin:44px 0 10px;font-size:15px;letter-spacing:.1em;color:#8a6d1f;border-bottom:1px solid #e2ddd2;padding-bottom:6px}
article{background:#fff;border:1px solid #e6e1d8;border-radius:10px;padding:22px 24px;margin:16px 0}
.hd{display:flex;gap:12px;align-items:baseline;font-size:12px;color:#8a8378;margin-bottom:6px;flex-wrap:wrap}
.no{font-weight:700;color:#A98722} .slug{font-family:ui-monospace,monospace}
article h3{font-size:20px;margin:2px 0 6px} .dek{color:#5a5548;font-size:15px;margin:0 0 10px}
.lead{background:#f6f3ec;border-left:3px solid #A98722;padding:10px 14px;margin:0 0 18px;font-size:15px}
h4{font-size:16px;margin:22px 0 6px} p{margin:0 0 12px}
sup.cit{font-size:11px;color:#A98722} sup.cit::before{content:""}
.refs{margin-top:22px;border-top:1px dashed #ddd7cc;padding-top:12px}
.refs h4{font-size:13px;color:#8a8378;margin:0 0 6px}
.refs ol{font-size:12.5px;color:#5a5548;padding-left:20px} .refs li{margin-bottom:6px}
a{color:#5C77C4}\n.rfig{margin:22px 0;padding:0}\n.rfig svg{width:100%;height:auto;display:block;border-radius:14px}\n.rfig figcaption{font-size:13px;color:#8a8378;margin-top:8px} .warnnote{background:#fff8e6;border:1px solid #e8d8a0;padding:12px 16px;border-radius:8px;font-size:14px}
"""

if __name__ == "__main__":
    body, problems, total, n = build()
    doc = ("<!doctype html><html lang=\"zh-Hant\"><head><meta charset=\"utf-8\">"
           "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">"
           "<title>BNCT 分組審閱稿</title><style>%s</style></head><body>"
           "<h1>次世代治療專題 — BNCT 分組審閱稿</h1>"
           "<p class=\"sub\">%d 篇中文正文 · 合計約 %s 字 · 2026-09-08 · 非上線版式</p>"
           "<div class=\"warnnote\">每篇最上方的雙警語與利益揭露段是共用區塊，"
           "審閱時看一次即可；本組的利益揭露特別寫明「我的醫院沒有 BNCT、我也不執行它」。"
           "所有金額數字已依指示避開。引用號由程式依首次出現順序重編。</div>"
           "%s</body></html>") % (CSS, n, format(total, ","), body)
    open("review-zh.html", "w", encoding="utf-8").write(doc)
    print("篇數 %d · 總字數 %d" % (n, total))
    if problems:
        print("問題:"); [print(" -", p) for p in problems]
    else:
        print("引用／參考對照：0 錯誤")
