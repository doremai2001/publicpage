# -*- coding: utf-8 -*-
"""Breast-cancer topic module (Chinese side, plus the wiring to the English one).

Everything the builder needs to know about this topic lives here; the prose
itself is read from the finished source files under /home/claude/breast.

Unlike hn / rc / cc this topic has 24 articles in four sections of six.  The
builder does not care -- nothing in topicbuild.py counts to four or to sixteen --
so the only thing that changes here is the length of the lists.
"""

import json
import os

import breast_en

# ------------------------------------------------------------------ sources --
SRC = {
    "body_zh": "/home/claude/breast/body",
    "body_en": "/home/claude/breast/en",
    "meta_zh": "/home/claude/breast/meta/all.json",
    "meta_en": "/home/claude/breast/meta/all-en.json",
}

REPO = "/home/claude/repo"

# Existing hub pages the tag labels are harvested from, so no label is retyped.
TAG_SOURCES = {
    "zh": [os.path.join(REPO, "hn.html"),
           os.path.join(REPO, "rc.html"),
           os.path.join(REPO, "cc.html")],
    "en": [os.path.join(REPO, "hn-en.html"),
           os.path.join(REPO, "rc-en.html"),
           os.path.join(REPO, "cc-en.html")],
}

# ------------------------------------------------------------------ identity --
PREFIX = "bc"
KICKER = "BREAST CANCER"
NAME_ZH = "乳癌專題"
NAME_EN = "Breast Cancer Guide"
CONDITION_ZH = "乳癌"
CONDITION_EN = "Breast cancer"
DATE = "2026-08-29"

# Tag keys already used by hn/rc/cc are reused verbatim; these four are new.
# English labels follow the existing English hubs' convention: Title Case, the
# same noun-phrase register, British spelling ("lymphoedema", as in the sources).
LABEL_ADD = {
    "endocrine": ("內分泌治療", "Endocrine Therapy"),
    "reconstruct": ("乳房重建", "Breast Reconstruction"),
    "lymphedema": ("淋巴水腫", "Lymphoedema"),
    "bone": ("骨骼健康", "Bone Health"),
}

# ------------------------------------------------------------------ sections --
SECTIONS = [
    {
        "zh": "確診之後",
        "stepsub_zh": "從報告出來到治療計畫定案，這幾週在決定什麼、哪幾行報告真的有份量。",
        "slugs": [
            "first-month",
            "receptor-report",
            "three-subtypes",
            "which-lines-matter",
            "imaging-extent",
            "germline-brca",
        ],
    },
    {
        "zh": "治療怎麼決定",
        "stepsub_zh": "切多少、要不要化療、藥怎麼排、吃幾年——這六篇是你真正握有發言權的地方。",
        "slugs": [
            "breast-conserving",
            "sentinel-node",
            "neoadjuvant",
            "genomic-chemo",
            "her2-therapy",
            "endocrine-years",
        ],
    },
    {
        "zh": "療程中的照護",
        "stepsub_zh": "放療做幾次、哪些副作用要當天打電話，以及那些真正讓人吃不下去的事。",
        "slugs": [
            "rt-hypofx",
            "rt-omission",
            "rt-regional",
            "chemo-side-effects",
            "endocrine-side-effects",
            "fertility-young",
        ],
    },
    {
        "zh": "結束之後",
        "stepsub_zh": "追蹤怎麼排、手會不會腫、骨頭怎麼顧，以及轉移之後的兩個題目。",
        "slugs": [
            "followup-schedule",
            "lymphoedema",
            "bone-health",
            "self-pay-and-trials",
            "metastatic-genomics",
            "metastatic-outlook",
        ],
    },
]

TAGS = {
    "first-month": ["prep", "workflow", "mdt", "nhi"],
    "receptor-report": ["staging", "biomarker", "prep"],
    "three-subtypes": ["staging", "decision", "biomarker"],
    "which-lines-matter": ["biomarker", "genetic", "decision", "nhi"],
    "imaging-extent": ["imaging", "staging", "decision", "surgery"],
    "germline-brca": ["genetic", "screening", "surgery", "nhi", "decision"],
    "breast-conserving": ["surgery", "decision", "reconstruct", "qol"],
    "sentinel-node": ["surgery", "staging", "decision", "lymphedema"],
    "neoadjuvant": ["chemo", "decision", "surgery", "workflow"],
    "genomic-chemo": ["biomarker", "chemo", "decision", "nhi"],
    "her2-therapy": ["targeted", "chemo", "decision", "nhi"],
    "endocrine-years": ["endocrine", "decision", "recurrence", "nhi"],
    "rt-hypofx": ["hypofx", "decision", "workflow"],
    "rt-omission": ["decision", "lateeffect", "endocrine", "recurrence"],
    "rt-regional": ["reconstruct", "surgery", "lateeffect", "decision", "proton"],
    "chemo-side-effects": ["sideeffect", "chemo", "targeted", "daily", "nhi"],
    "endocrine-side-effects": ["endocrine", "sideeffect", "qol", "bone", "daily"],
    "fertility-young": ["fertility", "sexual", "endocrine", "nhi"],
    "followup-schedule": ["followup", "imaging", "recurrence", "nhi"],
    "lymphoedema": ["lymphedema", "lateeffect", "surgery", "exercise"],
    "bone-health": ["bone", "exercise", "lateeffect", "nhi"],
    "self-pay-and-trials": ["nhi", "trial", "biomarker", "decision"],
    "metastatic-genomics": ["biomarker", "targeted", "genetic", "nhi", "recurrence"],
    "metastatic-outlook": ["recurrence", "decision", "qol", "survivor"],
}

# ---------------------------------------------------------- article metadata --
with open(SRC["meta_zh"], encoding="utf-8") as _fh:
    _ZH = json.load(_fh)

ART = {}
for _slug, _tags in TAGS.items():
    _m = dict(_ZH[_slug])
    _m["tags"] = _tags
    ART[_slug] = _m

EN = breast_en.EN
SECTIONS_EN = breast_en.SECTIONS_EN
HUB_EN = breast_en.HUB

# ----------------------------------------------------------------- hub copy --
HUB = {
    "title": "乳癌專題｜受體報告、要不要化療、放療與內分泌治療、追蹤與復發｜吳正友醫師",
    "desc": "乳癌病人最需要知道的 24 件事：確診後第一個月在等什麼、受體報告哪幾行有份量、"
            "三種亞型怎麼分、基因檢測到底要證明什麼、乳房保留還是全乳切除、前哨淋巴結、"
            "術前化療、21 基因分數、HER2 標靶怎麼排、內分泌治療要吃幾年、放療做幾次、"
            "哪些副作用要當天打電話、年輕病人的生育保存、追蹤怎麼排、淋巴水腫、骨骼健康、"
            "自費與臨床試驗，以及轉移之後。每篇附原始文獻連結。",
    "sub": "從確診那一天，到治療結束好幾年——一個問題一篇。",
    "intro": "乳癌病人在門診裡最重的三題通常是：我會不會失去乳房、我要不要做化療、會不會復發、"
             "藥要吃幾年。這 24 篇就是照著這三題往外長的，順序跟你真正會走過的一樣："
             "確診之後、治療怎麼決定、療程中的照護，最後是結束之後。基因檢測我特別放了五篇，"
             "因為病人聽到「基因檢測」的時候腦子裡是一件事，臨床上卻是目的完全不同的三件事："
             "一種是要證明你可以不做化療，一種是要找出可以用的藥，"
             "還有一種測的是你與家人與生俱來的風險。每一篇都附上原始文獻連結，"
             "證據弱的地方我會直接說弱。",
    "closing": "以上為一般性衛教說明，不能取代面對面的診療。乳癌的治療高度取決於亞型、"
               "期別與你的身體條件，同一個期別在不同亞型的人身上會導向完全不同的建議，"
               "實際治療請與你的主治醫師和多專科團隊討論。",
}

# No cross-topic sentence rewrites are needed for this topic: nothing in the
# breast sources points at another guide, and the sources carry no relative
# links at all.
BODY_EDITS = {"zh": [], "en": []}

# topics.html / topics-en.html cards, inserted after the colon one.
TOPIC_CARD_ZH = """  <a class="topiccard" href="bc.html">
    <div class="k">BREAST CANCER</div>
    <div class="t">乳癌專題</div>
    <div class="d">三種亞型三條路、基因檢測到底要證明什麼、放療做幾次、藥要吃幾年——從確診到治療結束好幾年，一個問題一篇。</div>
    <div class="steps"><span>確診之後</span><span>治療怎麼決定</span><span>療程中的照護</span><span>結束之後</span></div>
    <div class="go"><span class="n">24 篇</span><span class="ar">進入專題 →</span></div>
  </a>
"""

TOPIC_CARD_EN = """  <a class="topiccard" href="bc-en.html">
    <div class="k">BREAST CANCER</div>
    <div class="t">Breast Cancer Guide</div>
    <div class="d">Three subtypes and three different roads, what a genetic test is actually meant to prove, how many radiotherapy sessions, how many years on the tablets. One question per article, from diagnosis to years after treatment ends.</div>
    <div class="steps"><span>After the Diagnosis</span><span>How Treatment Is Decided</span><span>During Treatment</span><span>After Treatment</span></div>
    <div class="go"><span class="n">24 articles</span><span class="ar">Open the guide →</span></div>
  </a>
"""
