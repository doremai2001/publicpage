# -*- coding: utf-8 -*-
"""Colon-cancer topic module (Chinese side, plus the wiring to the English one).

Everything the builder needs to know about this topic lives here; the prose
itself is read from the finished source files under /home/claude/colon.
"""

import json
import os

import colon_en

# ------------------------------------------------------------------ sources --
SRC = {
    "body_zh": "/home/claude/colon/body",
    "body_en": "/home/claude/colon/en",
    "meta_zh": "/home/claude/colon/meta/all.json",
    "meta_en": "/home/claude/colon/meta/all-en.json",
}

REPO = "/home/claude/repo"

# Existing hub pages the tag labels are harvested from, so no label is retyped.
TAG_SOURCES = {
    "zh": [os.path.join(REPO, "hn.html"), os.path.join(REPO, "rc.html")],
    "en": [os.path.join(REPO, "hn-en.html"), os.path.join(REPO, "rc-en.html")],
}

# ------------------------------------------------------------------ identity --
PREFIX = "cc"
KICKER = "COLON CANCER"
NAME_ZH = "結腸癌專題"
NAME_EN = "Colon Cancer Guide"
CONDITION_ZH = "結腸癌"
CONDITION_EN = "Colon cancer"
DATE = "2026-08-27"

# Tag keys already used by hn/rc are reused verbatim; only this one is new.
LABEL_ADD = {"genetic": ("遺傳與家族", "Genetics & Family")}

# ------------------------------------------------------------------ sections --
SECTIONS = [
    {
        "zh": "確診之後",
        "stepsub_zh": "報告出來到治療計畫定案，這幾個星期在決定什麼、哪幾項不能省。",
        "slugs": [
            "malignant-polyp",
            "reading-stage-report",
            "first-month",
            "biomarkers-and-family",
        ],
    },
    {
        "zh": "治療怎麼決定",
        "stepsub_zh": "手術切多少、化療要不要做、做多久——這四篇是你真正握有發言權的地方。",
        "slugs": [
            "lymph-node-yield",
            "stage-ii-chemo",
            "three-or-six-months",
            "immunotherapy-dmmr",
        ],
    },
    {
        "zh": "療程中的照護",
        "stepsub_zh": "療程開始之後的日子怎麼過，以及哪些狀況要當天打電話。",
        "slugs": [
            "oxaliplatin-neuropathy",
            "capecitabine-at-home",
            "bowel-recovery",
            "supplements",
        ],
    },
    {
        "zh": "結束之後",
        "stepsub_zh": "追蹤怎麼排、復發還能做什麼、以及一件真的被試驗證明有用的事。",
        "slugs": [
            "surveillance-intensity",
            "ctdna-mrd",
            "metastatic-cure",
            "exercise-recurrence",
        ],
    },
]

TAGS = {
    "malignant-polyp": ["decision", "surgery", "staging", "prep"],
    "reading-stage-report": ["staging", "prep", "decision"],
    "first-month": ["prep", "workflow", "mdt", "imaging", "nhi"],
    "biomarkers-and-family": ["biomarker", "genetic", "screening", "nhi", "decision"],
    "lymph-node-yield": ["surgery", "staging", "decision"],
    "stage-ii-chemo": ["decision", "chemo", "biomarker", "nhi"],
    "three-or-six-months": ["chemo", "decision", "sideeffect", "nhi"],
    "immunotherapy-dmmr": ["immuno", "biomarker", "decision", "sideeffect", "nhi"],
    "oxaliplatin-neuropathy": ["sideeffect", "chemo", "daily", "lateeffect"],
    "capecitabine-at-home": ["chemo", "sideeffect", "daily", "nhi"],
    "bowel-recovery": ["bowel", "surgery", "daily", "stoma"],
    "supplements": ["nutrition", "supplement", "fertility", "daily"],
    "surveillance-intensity": ["followup", "imaging", "recurrence", "nhi"],
    "ctdna-mrd": ["biomarker", "trial", "followup", "recurrence", "nhi"],
    "metastatic-cure": ["recurrence", "decision", "surgery", "trial"],
    "exercise-recurrence": ["exercise", "survivor", "recurrence", "qol"],
}

# ---------------------------------------------------------- article metadata --
with open(SRC["meta_zh"], encoding="utf-8") as _fh:
    _ZH = json.load(_fh)

ART = {}
for _slug, _tags in TAGS.items():
    _m = dict(_ZH[_slug])
    _m["tags"] = _tags
    ART[_slug] = _m

EN = colon_en.EN
SECTIONS_EN = colon_en.SECTIONS_EN
HUB_EN = colon_en.HUB

# ----------------------------------------------------------------- hub copy --
HUB = {
    "title": "結腸癌專題｜期別報告、化療怎麼決定、副作用照護與追蹤｜吳正友醫師",
    "desc": "結腸癌病人最需要知道的 16 件事：惡性息肉要不要追加手術、報告上的 T3N1 怎麼算出來、"
            "基因報告哪幾格會遺傳、拿幾顆淋巴結決定什麼、第二期到底要不要化療、三個月還是六個月、"
            "免疫治療誰用得上、手麻腳麻什麼時候該說、在家吃的化療藥要盯住什麼、術後排便與造口、"
            "追蹤要做多密、ctDNA、已經轉移還有沒有機會治癒，以及運動與復發。每篇附原始文獻連結。",
    "sub": "從確診那一天，到治療結束好幾年——一個問題一篇。",
    "intro": "結腸癌的病人在門診裡最重的三題通常是：我要不要做化療、我會不會裝袋子、"
             "已經轉移了是不是就沒救了。這 16 篇就是照著這三題往外長的，順序跟你真正會走過的一樣："
             "確診之後、治療怎麼決定、療程中的照護，最後是結束之後。每一篇都附上原始文獻連結，"
             "證據弱的地方我會直接說弱。直腸癌的治療邏輯與結腸癌不同，"
             "那一部分請看<a href=\"rc.html\">直腸癌專題</a>。",
    "closing": "以上為一般性衛教說明，不能取代面對面的診療。結腸癌的治療高度取決於期別、"
               "病理報告上的風險特徵與你的身體條件，同一個期別在不同人身上會導向不同建議，"
               "實際治療請與你的主治醫師和多專科團隊討論。",
}

# ------------------------------------------------- one content edit, both langs
# The site now HAS a rectal topic, so the sentences that say rectal cancer works
# differently and is not covered here get 直腸癌 / "rectal cancer" linked to it.
# Applied at generation time only; the sources under /home/claude/colon are never
# touched.  The two languages are edited in lockstep.
BODY_EDITS = {
    "zh": [
        (
            "直腸癌的治療邏輯與結腸癌不同，本專題不處理。",
            '<a href="rc.html">直腸癌</a>的治療邏輯與結腸癌不同，本專題不處理。',
        ),
        (
            "直腸癌雖然用同一套 TNM，治療邏輯與結腸癌不同，本專題不處理。",
            '<a href="rc.html">直腸癌</a>雖然用同一套 TNM，治療邏輯與結腸癌不同，本專題不處理。',
        ),
    ],
    "en": [
        (
            "The treatment logic of rectal cancer is different from that of colon "
            "cancer, and this series does not deal with it.",
            'The treatment logic of <a href="rc-en.html">rectal cancer</a> is '
            "different from that of colon cancer, and this series does not deal "
            "with it.",
        ),
        (
            "Rectal cancer uses the same TNM system, but its treatment logic differs "
            "from colon cancer and this series does not cover it.",
            '<a href="rc-en.html">Rectal cancer</a> uses the same TNM system, but its '
            "treatment logic differs from colon cancer and this series does not "
            "cover it.",
        ),
    ],
}

# topics.html / topics-en.html cards, inserted after the rectal one.
TOPIC_CARD_ZH = """  <a class="topiccard" href="cc.html">
    <div class="k">COLON CANCER</div>
    <div class="t">結腸癌專題</div>
    <div class="d">化療要不要做、做多久、結束之後怎麼追蹤——從確診那一天到治療結束好幾年，一個問題一篇。</div>
    <div class="steps"><span>確診之後</span><span>治療怎麼決定</span><span>療程中的照護</span><span>結束之後</span></div>
    <div class="go"><span class="n">16 篇</span><span class="ar">進入專題 →</span></div>
  </a>
"""

TOPIC_CARD_EN = """  <a class="topiccard" href="cc-en.html">
    <div class="k">COLON CANCER</div>
    <div class="t">Colon Cancer Guide</div>
    <div class="d">Whether to have chemotherapy, for how long, and how the follow-up works afterwards. One question per article, from the day of diagnosis to years after treatment ends.</div>
    <div class="steps"><span>After the Diagnosis</span><span>How Treatment Is Decided</span><span>During Treatment</span><span>After Treatment</span></div>
    <div class="go"><span class="n">16 articles</span><span class="ar">Open the guide →</span></div>
  </a>
"""
