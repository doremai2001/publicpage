# -*- coding: utf-8 -*-
"""次世代治療專題（含熱治療分組）— 建題模組。
沿用 nextgen.py 的設計；slug 是去掉 nt- 前綴的尾巴，熱治療分組的 slug 以 ht- 開頭。"""
import json, os
import nextgen_ht_en

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = {"body_zh": os.path.join(HERE, "hubbuild/body"),
       "body_en": os.path.join(HERE, "hubbuild/en"),
       "meta_zh": os.path.join(HERE, "hubbuild/meta-zh.json"),
       "meta_en": os.path.join(HERE, "hubbuild/meta-en.json")}
REPO = "/home/claude/publicpage"
TAG_SOURCES = {"zh": [os.path.join(REPO, n) for n in ("hn.html","rc.html","cc.html","bc.html")],
               "en": [os.path.join(REPO, n) for n in ("hn-en.html","rc-en.html","cc-en.html","bc-en.html")]}

PREFIX = "nt"
KICKER = "NEXT-GENERATION THERAPY"
NAME_ZH = "次世代治療專題"
NAME_EN = "Next-Generation Therapy Guide"
CONDITION_ZH = "放射治療新技術"
CONDITION_EN = "Next-generation radiotherapy"
ABOUT_TYPE = "MedicalProcedure"
DATE = "2026-08-30"   # 舊六篇的發表日；新二十篇在 build 後改成 2026-09-07

LABEL_ADD = {
 "carbonion": ("重粒子", "Carbon-Ion Therapy"),
 "flash": ("FLASH", "FLASH"),
 "bnct": ("硼中子", "BNCT"),
 "regulation": ("法規與給付", "Regulation & Coverage"),
 "evidence": ("證據判讀", "Evidence"),
 "cost": ("費用與自費", "Costs & Self-Pay"),
}

SECTIONS = [
 {"zh": "先讀這兩篇",
  "stepsub_zh": "一把判斷任何新療法的尺，和一張法規身分的地圖——後面四篇都建立在這兩篇上。",
  "slugs": ["how-to-read", "approval"]},
 {"zh": "四種技術",
  "stepsub_zh": "各自照同一組六個問題檢視：改變什麼、走到哪一格、誰的資料、什麼身分、代價、什麼時候合理。",
  "slugs": ["proton", "carbon", "flash", "bnct"]},
 {"zh": "熱治療：先分清楚",
  "stepsub_zh": "五種不同的治療共用一個名字，想法有一百年，而它的證據要用另一把尺讀。從這三篇開始。",
  "slugs": ["ht-what", "ht-history", "ht-how-to-read"]},
 {"zh": "熱治療：它怎麼作用",
  "stepsub_zh": "它不自己殺癌細胞。它擋住修復、改善缺氧、讓藥物進得去——而這些在沒有加熱到的療程裡，一層都不會發生。",
  "slugs": ["ht-biology", "ht-chemo", "ht-dose"]},
 {"zh": "熱治療：機器與測溫",
  "stepsub_zh": "深度、測溫與品質保證。也包括那一類不主張靠溫度作用的設備，以及哪些人不適合做。",
  "slugs": ["ht-machines", "ht-meht", "ht-thermometry", "ht-safety"]},
 {"zh": "熱治療：各癌別的實證",
  "stepsub_zh": "六個癌別，每一篇都回答同樣六個問題：研究設計、分母、終點，以及這中間標準治療變了沒有。",
  "slugs": ["ht-breast", "ht-headneck", "ht-cervix", "ht-bladder", "ht-prostate-anal", "ht-others"]},
 {"zh": "熱治療：加上免疫與細胞治療",
  "stepsub_zh": "這個領域最好講的故事，也是證據最薄的一格。這兩篇的警語比結論多。",
  "slugs": ["ht-immuno", "ht-cell"]},
 {"zh": "熱治療：收束",
  "stepsub_zh": "在台灣要怎麼問，以及我自己正在研究的那個組合——它是一個研究題目，還不是一個療程。",
  "slugs": ["ht-taiwan", "ht-proton"]},
]

TAGS = {
 "how-to-read": ["evidence","decision","trial"],
 "approval": ["regulation","nhi","cost","evidence"],
 "proton": ["proton","evidence","cost","nhi"],
 "carbon": ["carbonion","evidence","cost"],
 "flash": ["flash","evidence","trial"],
 "bnct": ["bnct","evidence","cost","trial"],
 "ht-what": ["hyperthermia","evidence"],
 "ht-history": ["hyperthermia","evidence"],
 "ht-how-to-read": ["hyperthermia","evidence","decision"],
 "ht-biology": ["hyperthermia","evidence"],
 "ht-chemo": ["hyperthermia","evidence"],
 "ht-dose": ["hyperthermia","evidence","decision"],
 "ht-machines": ["hyperthermia","decision"],
 "ht-meht": ["hyperthermia","evidence","decision"],
 "ht-thermometry": ["hyperthermia","decision"],
 "ht-safety": ["hyperthermia","cost","decision"],
 "ht-breast": ["hyperthermia","evidence"],
 "ht-headneck": ["hyperthermia","evidence"],
 "ht-cervix": ["hyperthermia","evidence"],
 "ht-bladder": ["hyperthermia","evidence"],
 "ht-prostate-anal": ["hyperthermia","evidence"],
 "ht-others": ["hyperthermia","evidence"],
 "ht-immuno": ["hyperthermia","evidence","trial"],
 "ht-cell": ["hyperthermia","evidence","cost"],
 "ht-taiwan": ["hyperthermia","cost","decision"],
 "ht-proton": ["hyperthermia","proton","evidence"],
}

with open(SRC["meta_zh"], encoding="utf-8") as _fh:
    _ZH = json.load(_fh)
ART = {}
for _slug, _tags in TAGS.items():
    _m = dict(_ZH["nt-" + _slug]); _m["tags"] = _tags; ART[_slug] = _m

EN = nextgen_ht_en.EN
SECTIONS_EN = nextgen_ht_en.SECTIONS_EN
HUB_EN = nextgen_ht_en.HUB

HUB = {
 "title": "次世代治療專題｜質子、重粒子、FLASH、BNCT、熱治療——證據走到哪、法規身分與費用｜吳正友醫師",
 "desc": "關於次世代癌症治療的 26 篇：一把判斷任何新療法的尺、核准與給付與有效為什麼是三件不同的事、質子打得準之後換到了什麼、重粒子為什麼不等於比較好、FLASH 為什麼還在第一期、BNCT 的選擇性停在哪裡，以及二十篇的熱治療分組——機轉、熱劑量與測溫、各癌別的實證、與免疫和細胞治療的組合，還有質子加熱治療。多數自費，每一篇都標了查證日期，並附原始文獻連結。",
 "sub": "新的治療方法，以及它們各自走到哪裡——證據因為新而累積得少，除了那個舊的。",
 "intro": "這個專題和站上其他專題不一樣。疾病專題照病人的時間軸走；這裡收的是你會在新聞和廣告上看到的名詞——質子、重粒子、FLASH、BNCT，以及現在加入的熱治療。它們共同的特徵是：多數自費、多數在標準治療之外。所以每一篇都用同一組問題檢視：它改變什麼、證據走到哪一格、在台灣和國際是什麼身分、代價是什麼、什麼情況下合理。先讀前兩篇，那是後面所有文章共用的那把尺。熱治療那一組另有自己的一把尺（在該組第三篇），因為它的證據形狀不一樣：它有隨機試驗，而那些試驗是四十年前的。這個專題比其他專題更容易過時，所以每一篇都標了查證日期。",
 "closing": "以上為一般性衛教說明，不能取代面對面的診療。新技術的適用與否高度取決於癌別、期別、先前治療與身體條件，且證據與法規狀態變動很快，實際決定請與你的主治醫師和多專科團隊討論，並確認文章的查證日期。",
}

BODY_EDITS = {"zh": [], "en": []}

TOPIC_CARD_ZH = """  <a class="topiccard" href="nt.html">
    <div class="k">NEXT-GENERATION THERAPY</div>
    <div class="t">次世代治療專題</div>
    <div class="d">質子、重粒子、FLASH、BNCT、熱治療——新的方法，多數自費、多數在標準治療之外。一把判斷任何新療法的尺，先讀再決定。</div>
    <div class="steps"><span>先讀這兩篇</span><span>四種技術</span><span>熱治療二十篇</span></div>
    <div class="go"><span class="n">26 篇</span><span class="ar">進入專題 →</span></div>
  </a>
"""
TOPIC_CARD_EN = """  <a class="topiccard" href="nt-en.html">
    <div class="k">NEXT-GENERATION THERAPY</div>
    <div class="t">Next-Generation Therapy Guide</div>
    <div class="d">Protons, carbon ions, FLASH, BNCT and hyperthermia — mostly self-pay, mostly outside standard treatment. A ruler for judging any new treatment: read it first, then decide.</div>
    <div class="steps"><span>Read these two first</span><span>The four technologies</span><span>Twenty on hyperthermia</span></div>
    <div class="go"><span class="n">26 articles</span><span class="ar">Open the guide →</span></div>
  </a>
"""
HASPART_ZH = {"@type": "CollectionPage", "name": NAME_ZH,
              "url": "https://doremai2001.github.io/publicpage/nt.html"}
HASPART_EN = {"@type": "CollectionPage", "name": NAME_EN,
              "url": "https://doremai2001.github.io/publicpage/nt-en.html"}
