# -*- coding: utf-8 -*-
"""產生 nt-bn.html／nt-bn-en.html（BNCT 子目錄頁）、nt-ht.html／nt-ht-en.html（熱治療子目錄頁），
並把 nt.html／nt-en.html 收成卡片式。全部以現有的 nt.html／nt-en.html 為版型來源做定點替換。"""
import json, os, re, sys, html
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import nextgen_bn as T
import notes

REPO = "/root/publicpage"
OUT = os.path.join(HERE, "out")
BASE = "https://doremai2001.github.io/publicpage/"

RE_TITLE = re.compile(r"<title>(.*?)</title>", re.S)
RE_DESC = re.compile(r'<meta name="description" content="(.*?)">', re.S)
RE_OGT = re.compile(r'<meta property="og:title" content="(.*?)">', re.S)
RE_OGD = re.compile(r'<meta property="og:description" content="(.*?)">', re.S)
RE_OGU = re.compile(r'<meta property="og:url" content="(.*?)">', re.S)
RE_CANON = re.compile(r'<link rel="canonical" href="(.*?)">')
RE_ALTS = re.compile(r'<link rel="alternate" hreflang="zh-Hant" href="[^"]*">\n'
                     r'<link rel="alternate" hreflang="en" href="[^"]*">\n'
                     r'<link rel="alternate" hreflang="x-default" href="[^"]*">\n')
RE_LD = re.compile(r'<script type="application/ld\+json">.*?</script>', re.S)
RE_LANG = re.compile(r'<div class="lang">.*?</div>', re.S)
RE_H2 = re.compile(r"<h2>.*?</h2>", re.S)
RE_INTRO = re.compile(r'<p class="note" style="margin-top:18px">.*?</p>', re.S)
RE_TAGC = re.compile(r'<div class="tagbar-c">.*?</div>', re.S)
RE_GROUPS = re.compile(r'(  <div class="postgroup hnstep">.*</div>)(\n\n  <p class="note">)', re.S)
RE_CARD = re.compile(r'<a class="postcard"[^>]*>.*?</a>', re.S)


def esc(s): return html.escape(s, quote=False)
def esca(s): return html.escape(s, quote=False).replace('"', "&quot;")


def tag_labels(lang):
    """從 nt 的 hub 抓標籤中英標籤文字。"""
    src = os.path.join(REPO, "nt.html" if lang == "zh" else "nt-en.html")
    s = open(src, encoding="utf-8").read()
    bar = RE_TAGC.search(s).group(0)
    out = {}
    for k, lab in re.findall(r'<button class="tagf(?: on)?" data-tag="([^"]*)">(.*?) <i>\d+</i></button>', bar):
        if k:
            out[k] = html.unescape(lab.lstrip("#"))
    return out


def card(href, title, dek, meta, tags, labels):
    chips = "".join("<span>#%s</span>" % esc(labels[t]) for t in tags if t in labels)
    return ('    <a class="postcard" data-tags="%s" href="%s">\n'
            '      <div class="t">%s</div>\n'
            '      <div class="d">%s</div>\n'
            '      <div class="m">%s</div>\n'
            '      <div class="cardtags">%s</div>\n'
            '    </a>\n' % (esca(" ".join(tags)), esca(href), esc(title), esc(dek), esc(meta), chips))


def tagbar(cards_tags, labels, all_label, order):
    n = len(cards_tags)
    buttons = ['<button class="tagf on" data-tag="">%s <i>%d</i></button>' % (esc(all_label), n)]
    for k in order:
        c = sum(1 for t in cards_tags if k in t)
        if c:
            buttons.append('<button class="tagf" data-tag="%s">#%s <i>%d</i></button>'
                           % (esca(k), esc(labels[k]), c))
    return '<div class="tagbar-c">%s</div>' % "".join(buttons)


def patch_head(t, title, desc, url, alt_zh, alt_en, ld):
    t = RE_TITLE.sub(lambda m: "<title>%s</title>" % esca(title), t, 1)
    t = RE_DESC.sub(lambda m: '<meta name="description" content="%s">' % esca(desc), t, 1)
    t = RE_OGT.sub(lambda m: '<meta property="og:title" content="%s">' % esca(title), t, 1)
    t = RE_OGD.sub(lambda m: '<meta property="og:description" content="%s">' % esca(desc), t, 1)
    t = RE_OGU.sub(lambda m: '<meta property="og:url" content="%s">' % esca(url), t, 1)
    t = RE_CANON.sub(lambda m: '<link rel="canonical" href="%s">' % esca(url), t, 1)
    t = RE_ALTS.sub(lambda m: ('<link rel="alternate" hreflang="zh-Hant" href="%s">\n'
                               '<link rel="alternate" hreflang="en" href="%s">\n'
                               '<link rel="alternate" hreflang="x-default" href="%s">\n')
                    % (esca(alt_zh), esca(alt_en), esca(alt_zh)), t, 1)
    raw = json.dumps(ld, ensure_ascii=False, separators=(",", ":"))
    t = RE_LD.sub(lambda m: '<script type="application/ld+json">%s</script>' % raw, t, 1)
    return t


# ------------------------------------------------------------------ 文案 --
BN = {
 "zh": dict(
  name="次世代治療專題・BNCT",
  sub="硼中子捕獲治療的十七篇：原理、硼藥物、機器，以及各癌別的實證走到哪一格。",
  title="BNCT 硼中子捕獲治療｜原理、硼藥物、機器與各癌別實證｜吳正友醫師",
  desc="關於 BNCT 的十七篇：殺傷範圍不到一顆細胞的物理、為什麼它的劑量不能拿去跟放療比、中子走得到多深、BPA 與 BSH、治療前的正子攝影篩選、清大反應器與加速器型的差別，以及頭頸癌、膠質母細胞瘤、腦膜瘤、黑色素瘤與深部器官各自的證據層級。每一篇都標了查證日期並附原始文獻連結。",
  intro="這是次世代治療專題底下的 BNCT 分組。它從<a href=\"nt-bnct.html\">總論那一篇</a>往外擴：原理三篇解釋這個技術唯一真正特別的地方，硼藥物三篇講決定成敗的另外一半，機器兩篇講台灣的反應器與加速器型的差別，各癌別六篇逐一標明證據層級、分母與終點，最後三篇是副作用、四個地方的法規身分，以及該不該去問這件事的四個先決條件。這個領域沒有隨機分派試驗，所以每一篇都寫明數字是從什麼設計、幾個人身上來的。",
  all_label="全部", refs="參考文獻 %d 篇",
  entry_h3="從這裡開始", entry_sub="這一篇是整個分組的入口：物理上真實的細胞層級選擇性、日本的藥證，以及台灣的門路。",
  back="← 回到次世代治療專題",
 ),
 "en": dict(
  name="Next-Generation Therapy Guide · BNCT",
  sub="Seventeen articles on boron neutron capture therapy: the physics, the drugs, the machines, and where the evidence actually stands.",
  title="Boron Neutron Capture Therapy | physics, boron drugs, machines and the evidence by cancer | Dr Jeng-You Wu",
  desc="Seventeen articles on BNCT: the physics of a kill radius smaller than one cell, why its dose cannot be compared with radiotherapy, how deep the neutrons get, BPA and BSH, the PET screening step before treatment, Taiwan's reactor and how accelerator-based systems differ, and the level of evidence for head and neck cancer, glioblastoma, meningioma, melanoma and the deep organs. Every article carries the date it was checked and links to the primary sources.",
  intro="This is the BNCT section of the next-generation therapy guide. It builds outwards from <a href=\"nt-bnct-en.html\">the overview article</a>: three articles on the physics, three on the boron drugs that decide half the outcome, two on Taiwan's reactor and how accelerator-based systems differ, six that state the level of evidence, denominator and endpoint for each cancer, and three on side effects, regulatory status in four places, and the four conditions for whether to ask about this at all. There are no randomised trials in this field, so every article says what design and how many people each number came from.",
  all_label="All", refs="%d references",
  entry_h3="Start here", entry_sub="This one is the way in: the real cell-level selectivity, Japan's approval, and the routes that exist in Taiwan.",
  back="← Back to the Next-Generation Therapy Guide",
 ),
}

HT = {
 "zh": dict(
  name="次世代治療專題・熱治療",
  sub="腫瘤熱治療的二十篇：機轉、熱劑量與測溫、各癌別的實證，以及與化療、免疫和質子的組合。",
  title="腫瘤熱治療｜機轉、熱劑量與測溫、各癌別實證與組合治療｜吳正友醫師",
  desc="關於腫瘤熱治療的二十篇：中文裡至少五種東西都叫熱療、一百年前的想法憑什麼放在次世代治療底下、加熱為什麼讓放療更有效、四十二度不是重點而熱劑量才是、機器與測溫的差別，以及乳癌、頭頸癌、子宮頸癌、膀胱癌、骨盆腔與肉瘤各自的證據。多數自費，每一篇都標了查證日期。",
  intro="這是次世代治療專題底下的熱治療分組。它的證據形狀和其他技術不一樣：熱治療有陽性的隨機試驗，但那些試驗多半是四十年前的，樣本不大，而且療效高度取決於這一次有沒有真的加熱到。所以這一組另有自己的一把尺，在第三篇。",
  all_label="全部", refs="參考文獻 %d 篇",
  back="← 回到次世代治療專題",
 ),
 "en": dict(
  name="Next-Generation Therapy Guide · Hyperthermia",
  sub="Twenty articles on tumour hyperthermia: the mechanism, thermal dose and thermometry, the evidence by cancer, and the combinations.",
  title="Tumour Hyperthermia | mechanism, thermal dose, thermometry and the evidence by cancer | Dr Jeng-You Wu",
  desc="Twenty articles on tumour hyperthermia: at least five different things share the name, why a hundred-year-old idea sits under next-generation therapy, why heating makes radiotherapy work better, why thermal dose matters more than 42 degrees, how the machines and the thermometry differ, and the evidence in breast, head and neck, cervical and bladder cancer, the pelvis and sarcoma. Mostly self-paid; every article carries the date it was checked.",
  intro="This is the hyperthermia section of the next-generation therapy guide. Its evidence has a different shape from the other technologies here: hyperthermia does have positive randomised trials, but most of them are forty years old, the samples are small, and the effect depends heavily on whether this particular session actually reached dose. So this section has a ruler of its own, in its third article.",
  all_label="All", refs="%d references",
  back="← Back to the Next-Generation Therapy Guide",
 ),
}


TAG_ORDER = ["bnct", "hyperthermia", "proton", "carbonion", "flash", "regulation",
             "nhi", "evidence", "decision", "trial", "cost"]


def group_block(num, h3, sub, cards):
    return ('  <div class="postgroup hnstep">\n    <h3><b>%d</b>%s</h3>\n'
            '    <p class="stepsub">%s</p>\n%s  </div>\n'
            % (num, esc(h3), esc(sub), "".join(cards)))


def nrefs(slug, lang):
    d = "body_bn" if lang == "zh" else "en_bn"
    s = open(os.path.join(HERE, d, slug + ".html"), encoding="utf-8").read()
    return len(re.findall(r"(?m)^<li>", s.split("<hr>", 1)[1]))


def build_bn_hub(lang):
    tplname = "nt.html" if lang == "zh" else "nt-en.html"
    t = open(os.path.join(REPO, tplname), encoding="utf-8").read()
    cfg = BN[lang]
    labels = tag_labels(lang)
    suf = "" if lang == "zh" else "-en"
    hub = "nt-bn%s.html" % suf
    meta = T.ART if lang == "zh" else T.EN

    # 入口卡片（既有的 nt-bnct 總論）
    src = open(os.path.join(REPO, "nt-bnct%s.html" % suf), encoding="utf-8").read()
    e_title = re.search(r"<h1>(.*?)</h1>", src, re.S).group(1)
    e_dek = re.search(r'<p class="dek">(.*?)</p>', src, re.S).group(1)
    e_refs = len(re.findall(r"(?m)^<li>", re.search(r'<div class="refs">.*?<ol>(.*?)</ol>', src, re.S).group(1)))
    entry = card("nt-bnct%s.html" % suf, html.unescape(e_title), html.unescape(e_dek),
                 cfg["refs"] % e_refs, ["bnct", "evidence", "cost", "trial"], labels)

    groups = [group_block(1, cfg["entry_h3"], cfg["entry_sub"], [entry])]
    all_tags = [["bnct", "evidence", "cost", "trial"]]
    n = 1
    secs = T.SECTIONS if lang == "zh" else T.SECTIONS_EN
    for sec in secs:
        n += 1
        cards = []
        for slug in sec["slugs"]:
            m = meta[slug]
            tags = T.TAGS[slug]
            all_tags.append(tags)
            cards.append(card("nt-%s%s.html" % (slug, suf), m["title"], m["dek"],
                              cfg["refs"] % nrefs(slug, lang), tags, labels))
        groups.append(group_block(n, sec["zh" if lang == "zh" else "en"],
                                  sec["stepsub_zh" if lang == "zh" else "stepsub_en"], cards))

    t = patch_head(t, cfg["title"], cfg["desc"], BASE + hub,
                   BASE + "nt-bn.html", BASE + "nt-bn-en.html",
                   {"@context": "https://schema.org", "@type": "CollectionPage",
                    "name": cfg["name"], "url": BASE + hub,
                    "inLanguage": "zh-Hant" if lang == "zh" else "en",
                    "about": {"@type": "MedicalProcedure",
                              "name": "硼中子捕獲治療" if lang == "zh" else "Boron neutron capture therapy"},
                    "author": {"@type": "Physician", "name": "吳正友 Robert Jeng-You Wu", "url": BASE},
                    "hasPart": [{"@type": "MedicalWebPage", "name": meta[s]["title"],
                                 "url": BASE + "nt-%s%s.html" % (s, suf)}
                                for sec in secs for s in sec["slugs"]]})
    other = "nt-bn-en.html" if lang == "zh" else "nt-bn.html"
    t = RE_LANG.sub(lambda m: ('<div class="lang"><span class="on">中</span><a href="%s" hreflang="en">EN</a></div>' % other)
                    if lang == "zh" else
                    ('<div class="lang"><a href="%s" hreflang="zh-Hant">中</a><span class="on">EN</span></div>' % other), t, 1)
    t = RE_H2.sub(lambda m: '<h2>%s<span class="sub">%s</span></h2>' % (esc(cfg["name"]), esc(cfg["sub"])), t, 1)
    t = RE_INTRO.sub(lambda m: '<p class="note" style="margin-top:18px">%s</p>' % cfg["intro"], t, 1)
    t = RE_TAGC.sub(lambda m: tagbar(all_tags, labels, cfg["all_label"], TAG_ORDER), t, 1)
    t = RE_GROUPS.sub(lambda m: "".join(groups).rstrip("\n") + m.group(2), t, 1)
    t = t.replace('</section>', '  <p class="note" style="margin-top:26px">'
                  '<a href="nt%s.html">%s</a></p>\n</section>' % (suf, esc(cfg["back"])), 1)
    open(os.path.join(OUT, hub), "w", encoding="utf-8").write(t)
    return hub, len(all_tags)


RE_GRP1 = re.compile(r'  <div class="postgroup hnstep">\s*<h3><b>(\d+)</b>(.*?)</h3>\s*'
                     r'<p class="stepsub">(.*?)</p>\n(.*?)  </div>\n', re.S)


def parse_groups(text):
    return [(int(m.group(1)), m.group(2), m.group(3), m.group(4)) for m in RE_GRP1.finditer(text)]


def cards_tags(block):
    return [m.split() for m in re.findall(r'data-tags="([^"]*)"', block)]


def build_ht_hub(lang):
    tplname = "nt.html" if lang == "zh" else "nt-en.html"
    t = open(os.path.join(REPO, tplname), encoding="utf-8").read()
    cfg = HT[lang]
    labels = tag_labels(lang)
    suf = "" if lang == "zh" else "-en"
    hub = "nt-ht%s.html" % suf
    grps = parse_groups(t)
    keep = [g for g in grps if g[0] >= 3]          # 原本的第 3–8 段就是熱治療
    blocks, all_tags, names = [], [], []
    for i, (_n, h3, sub, body) in enumerate(keep, 1):
        title = re.sub(r"^(熱治療：|Hyperthermia: )", "", h3)
        title = title[0].upper() + title[1:] if lang == "en" else title
        blocks.append(group_block(i, title, sub, [body]))
        all_tags += cards_tags(body)
        for h, ti in re.findall(r'href="([^"]+)">\s*<div class="t">(.*?)</div>', body, re.S):
            names.append((html.unescape(ti), h))
    t = patch_head(t, cfg["title"], cfg["desc"], BASE + hub,
                   BASE + "nt-ht.html", BASE + "nt-ht-en.html",
                   {"@context": "https://schema.org", "@type": "CollectionPage",
                    "name": cfg["name"], "url": BASE + hub,
                    "inLanguage": "zh-Hant" if lang == "zh" else "en",
                    "about": {"@type": "MedicalProcedure",
                              "name": "腫瘤熱治療" if lang == "zh" else "Tumour hyperthermia"},
                    "author": {"@type": "Physician", "name": "吳正友 Robert Jeng-You Wu", "url": BASE},
                    "hasPart": [{"@type": "MedicalWebPage", "name": ti, "url": BASE + h}
                                for ti, h in names]})
    other = "nt-ht-en.html" if lang == "zh" else "nt-ht.html"
    t = RE_LANG.sub(lambda m: ('<div class="lang"><span class="on">中</span><a href="%s" hreflang="en">EN</a></div>' % other)
                    if lang == "zh" else
                    ('<div class="lang"><a href="%s" hreflang="zh-Hant">中</a><span class="on">EN</span></div>' % other), t, 1)
    t = RE_H2.sub(lambda m: '<h2>%s<span class="sub">%s</span></h2>' % (esc(cfg["name"]), esc(cfg["sub"])), t, 1)
    t = RE_INTRO.sub(lambda m: '<p class="note" style="margin-top:18px">%s</p>' % esc(cfg["intro"]), t, 1)
    t = RE_TAGC.sub(lambda m: tagbar(all_tags, labels, cfg["all_label"], TAG_ORDER), t, 1)
    t = RE_GROUPS.sub(lambda m: "".join(blocks).rstrip("\n") + m.group(2), t, 1)
    t = t.replace('</section>', '  <p class="note" style="margin-top:26px">'
                  '<a href="nt%s.html">%s</a></p>\n</section>' % (suf, esc(cfg["back"])), 1)
    open(os.path.join(OUT, hub), "w", encoding="utf-8").write(t)
    return hub, len(all_tags), len(blocks)


NT = {
 "zh": dict(sub="新的治療方法，以及它們各自走到哪裡——證據因為新而累積得少，除了那個舊的。",
   g3="兩個深入分組", g3sub="熱治療與 BNCT 各自有一整組文章。點進去看那一組的完整目錄。",
   ht_t="腫瘤熱治療（二十篇）", ht_d="加熱不是把腫瘤燒掉，是讓放療與化療更有效。它有隨機試驗，但那些試驗是四十年前的——這一組另有自己的一把尺。",
   bn_t="BNCT 硼中子捕獲治療（十七篇）", bn_d="殺傷範圍不到一顆細胞，選擇性住在硼的分布裡。原理、硼藥物、機器，以及各癌別的證據走到哪一格。",
   n="%d 篇", all_label="全部",
   intro="這個專題和站上其他專題不一樣。疾病專題照病人的時間軸走；這裡收的是你會在新聞和廣告上看到的名詞——質子、重粒子、FLASH、BNCT、熱治療。它們共同的特徵是：多數自費、多數在標準治療之外。所以每一篇都用同一組問題檢視：它改變什麼、證據走到哪一格、在台灣和國際是什麼身分、代價是什麼、什麼情況下合理。先讀前兩篇，那是後面所有文章共用的那把尺。熱治療與 BNCT 各自有一整組文章，從下面的兩張卡片進去。這個專題比其他專題更容易過時，所以每一篇都標了查證日期。"),
 "en": dict(sub="New ways of treating, and how far each has actually come — the evidence is thin because it is new, except where it is old.",
   g3="Two sections in depth", g3sub="Hyperthermia and BNCT each have a full set of articles. Open one for its complete contents.",
   ht_t="Tumour hyperthermia (twenty articles)", ht_d="Heating does not burn the tumour away; it makes radiotherapy and chemotherapy work better. It has randomised trials, but they are forty years old - this section has a ruler of its own.",
   bn_t="Boron neutron capture therapy (seventeen articles)", bn_d="A kill radius smaller than one cell, with the selectivity living in where the boron went. The physics, the drugs, the machines, and where the evidence stands for each cancer.",
   n="%d articles", all_label="All",
   intro="This guide works differently from the disease topics on this site. Those follow a patient's timeline; this one collects the words you will meet in the news and in advertising - protons, carbon ions, FLASH, BNCT, hyperthermia. What they have in common is that most are paid out of pocket and most sit outside standard treatment. So each article is put through the same set of questions: what it changes, how far the evidence has come, what its regulatory status is here and abroad, what it costs, and when it is reasonable. Read the first two first; they are the ruler the rest are built on. Hyperthermia and BNCT each have a full section, reached from the two cards below. This guide dates faster than the others, so every article carries the date it was checked."),
}


def build_nt(lang):
    tplname = "nt.html" if lang == "zh" else "nt-en.html"
    t = open(os.path.join(REPO, tplname), encoding="utf-8").read()
    cfg = NT[lang]
    labels = tag_labels(lang)
    suf = "" if lang == "zh" else "-en"
    grps = parse_groups(t)
    keep = [g for g in grps if g[0] <= 2]
    blocks, all_tags, names = [], [], []
    for i, (_n, h3, sub, body) in enumerate(keep, 1):
        blocks.append(group_block(i, h3, sub, [body]))
        all_tags += cards_tags(body)
        for h, ti in re.findall(r'href="([^"]+)">\s*<div class="t">(.*?)</div>', body, re.S):
            names.append((html.unescape(ti), h))
    ht_tags = ["hyperthermia", "evidence", "decision"]
    bn_tags = ["bnct", "evidence", "regulation", "cost"]
    two = [card("nt-ht%s.html" % suf, cfg["ht_t"], cfg["ht_d"], cfg["n"] % 20, ht_tags, labels),
           card("nt-bn%s.html" % suf, cfg["bn_t"], cfg["bn_d"], cfg["n"] % 17, bn_tags, labels)]
    all_tags += [ht_tags, bn_tags]
    blocks.append(group_block(3, cfg["g3"], cfg["g3sub"], two))
    ld = json.loads(RE_LD.search(t).group(0).split(">", 1)[1].rsplit("<", 1)[0])
    ld["hasPart"] = ([{"@type": "MedicalWebPage", "name": ti, "url": BASE + h} for ti, h in names]
                     + [{"@type": "CollectionPage", "name": cfg["ht_t"], "url": BASE + "nt-ht%s.html" % suf},
                        {"@type": "CollectionPage", "name": cfg["bn_t"], "url": BASE + "nt-bn%s.html" % suf}])
    t = RE_LD.sub(lambda m: '<script type="application/ld+json">%s</script>'
                  % json.dumps(ld, ensure_ascii=False, separators=(",", ":")), t, 1)
    t = RE_H2.sub(lambda m: m.group(0), t, 1)
    t = RE_INTRO.sub(lambda m: '<p class="note" style="margin-top:18px">%s</p>' % esc(cfg["intro"]), t, 1)
    t = RE_TAGC.sub(lambda m: tagbar(all_tags, labels, cfg["all_label"], TAG_ORDER), t, 1)
    t = RE_GROUPS.sub(lambda m: "".join(blocks).rstrip("\n") + m.group(2), t, 1)
    open(os.path.join(OUT, "nt%s.html" % suf), "w", encoding="utf-8").write(t)
    return "nt%s.html" % suf, len(all_tags), len(blocks)


if __name__ == "__main__":
    for lang in ("zh", "en"):
        print(build_bn_hub(lang), build_ht_hub(lang), build_nt(lang))
