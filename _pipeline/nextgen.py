# -*- coding: utf-8 -*-
"""Next-generation-therapy topic module (Chinese side, plus the wiring to the
English one).

Two departures from the disease topics, both by design:

* The source files under /home/claude/nextgen already carry the nt- prefix in
  their names (nt-how-to-read.html ...).  The builder composes output names as
  "<PREFIX>-<slug>.html", so the slugs here are the *unprefixed* tails and the
  staging step (scratchpad/stage_figs.py) copies each source to a stripped
  name — that same step also inserts the article figures, which the raw
  fragments deliberately do not contain.  Output names therefore come out as
  nt-how-to-read.html, never nt-nt-how-to-read.html.

* The topic is about a set of treatments, not a disease, so the JSON-LD
  "about" entity is a MedicalProcedure (ABOUT_TYPE below; topicbuild defaults
  to MedicalCondition when the attribute is absent).
"""

import json
import os

import nextgen_en

_STAGE = ("/tmp/claude-0/-home-claude/4bc50b06-d4e4-5989-80b2-34f0f02eed26/"
          "scratchpad/staging")

# ------------------------------------------------------------------ sources --
SRC = {
    "body_zh": os.path.join(_STAGE, "body"),
    "body_en": os.path.join(_STAGE, "en"),
    "meta_zh": "/home/claude/nextgen/meta/all.json",
    "meta_en": "/home/claude/nextgen/meta/all-en.json",
}

REPO = "/home/claude/repo"

# Existing hub pages the tag labels are harvested from, so no label is retyped.
TAG_SOURCES = {
    "zh": [os.path.join(REPO, n) for n in
           ("hn.html", "rc.html", "cc.html", "bc.html")],
    "en": [os.path.join(REPO, n) for n in
           ("hn-en.html", "rc-en.html", "cc-en.html", "bc-en.html")],
}

# ------------------------------------------------------------------ identity --
PREFIX = "nt"
KICKER = "NEXT-GENERATION THERAPY"
NAME_ZH = "次世代治療專題"
NAME_EN = "Next-Generation Therapy Guide"
CONDITION_ZH = "放射治療新技術"
CONDITION_EN = "Next-generation radiotherapy"
ABOUT_TYPE = "MedicalProcedure"
DATE = "2026-08-30"

# proton / nhi / trial / decision already exist on the hn/rc/cc/bc hubs and are
# reused verbatim (hyperthermia also exists but is not used by these six).
# These six are new; English labels follow the existing hubs' convention
# (Title Case noun phrases, "&" where the zh label has 與).
LABEL_ADD = {
    "carbonion": ("重粒子", "Carbon-Ion Therapy"),
    "flash": ("FLASH", "FLASH"),
    "bnct": ("硼中子", "BNCT"),
    "regulation": ("法規與給付", "Regulation & Coverage"),
    "evidence": ("證據判讀", "Evidence"),
    "cost": ("費用與自費", "Costs & Self-Pay"),
}

# ------------------------------------------------------------------ sections --
SECTIONS = [
    {
        "zh": "先讀這兩篇",
        "stepsub_zh": "一把判斷任何新療法的尺，和一張法規身分的地圖——"
                      "後面四篇都建立在這兩篇上。",
        "slugs": ["how-to-read", "approval"],
    },
    {
        "zh": "四種技術",
        "stepsub_zh": "各自照同一組六個問題檢視：改變什麼、走到哪一格、"
                      "誰的資料、什麼身分、代價、什麼時候合理。",
        "slugs": ["proton", "carbon", "flash", "bnct"],
    },
]

TAGS = {
    "how-to-read": ["evidence", "decision", "trial"],
    "approval": ["regulation", "nhi", "cost", "evidence"],
    "proton": ["proton", "evidence", "cost", "nhi"],
    "carbon": ["carbonion", "evidence", "cost"],
    "flash": ["flash", "evidence", "trial"],
    "bnct": ["bnct", "evidence", "cost", "trial"],
}

# ---------------------------------------------------------- article metadata --
with open(SRC["meta_zh"], encoding="utf-8") as _fh:
    _ZH = json.load(_fh)

ART = {}
for _slug, _tags in TAGS.items():
    _m = dict(_ZH["nt-" + _slug])
    _m["tags"] = _tags
    ART[_slug] = _m

EN = nextgen_en.EN
SECTIONS_EN = nextgen_en.SECTIONS_EN
HUB_EN = nextgen_en.HUB

# ----------------------------------------------------------------- hub copy --
HUB = {
    "title": "次世代治療專題｜質子、重粒子、FLASH、BNCT——證據走到哪、"
             "法規身分與費用｜吳正友醫師",
    "desc": "關於次世代放射治療，病人最需要知道的 6 件事：一把判斷任何新療法的尺"
            "（證據階梯與五個判準）、核准、給付、有效為什麼是三件不同的事、"
            "質子打得準之後換到了什麼、重粒子為什麼不等於比較好、"
            "FLASH 為什麼還在第一期、BNCT 的選擇性從哪裡來又停在哪裡。"
            "多數自費、證據因為新而累積得少，每一篇都標了查證日期，並附原始文獻連結。",
    "sub": "新的治療方法，以及它們各自走到哪裡——證據因為新，累積得還少。",
    "intro": "這個專題和站上其他專題不一樣。疾病專題照病人的時間軸走；"
             "這裡收的是你會在新聞和廣告上看到的名詞——質子、重粒子、FLASH、BNCT，"
             "之後還會加入細胞治療、熱治療合併、組織碎化這些新方法。"
             "它們共同的特徵是：新，所以證據累積得少，而且多數自費。"
             "所以每一篇都用同一組問題檢視：它改變什麼、證據走到哪一格、"
             "在台灣和國際是什麼身分、代價是什麼、什麼情況下合理。"
             "先讀前兩篇，那是後面所有文章共用的那把尺。"
             "這個專題比其他專題更容易過時，所以每一篇都標了查證日期。",
    "closing": "以上為一般性衛教說明，不能取代面對面的診療。"
               "新技術的適用與否高度取決於癌別、期別、先前治療與身體條件，"
               "且證據與法規狀態變動很快，實際決定請與你的主治醫師和多專科團隊討論，"
               "並確認文章的查證日期。",
}

# No cross-topic sentence rewrites: the nt fragments carry no relative links.
BODY_EDITS = {"zh": [], "en": []}

# topics.html / topics-en.html cards, inserted after the breast one.
TOPIC_CARD_ZH = """  <a class="topiccard" href="nt.html">
    <div class="k">NEXT-GENERATION THERAPY</div>
    <div class="t">次世代治療專題</div>
    <div class="d">質子、重粒子、FLASH、BNCT——新的方法，證據因為新而累積得少。一把判斷任何新療法的尺，先讀再決定。</div>
    <div class="steps"><span>先讀這兩篇</span><span>四種技術</span></div>
    <div class="go"><span class="n">6 篇</span><span class="ar">進入專題 →</span></div>
  </a>
"""

TOPIC_CARD_EN = """  <a class="topiccard" href="nt-en.html">
    <div class="k">NEXT-GENERATION THERAPY</div>
    <div class="t">Next-Generation Therapy Guide</div>
    <div class="d">Protons, carbon ions, FLASH, BNCT — new ways of treating, with evidence still thin because it is new. A ruler for judging any new treatment: read it first, then decide.</div>
    <div class="steps"><span>Read these two first</span><span>The four technologies</span></div>
    <div class="go"><span class="n">6 articles</span><span class="ar">Open the guide →</span></div>
  </a>
"""

# JSON-LD hasPart entries appended to the topics pages' CollectionPage.
HASPART_ZH = {"@type": "CollectionPage", "name": NAME_ZH,
              "url": "https://doremai2001.github.io/publicpage/nt.html"}
HASPART_EN = {"@type": "CollectionPage", "name": NAME_EN,
              "url": "https://doremai2001.github.io/publicpage/nt-en.html"}
