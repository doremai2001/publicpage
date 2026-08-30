# -*- coding: utf-8 -*-
"""Cervical-cancer topic module (Chinese side, plus the wiring to the English
one).

Like nt, the source files under /home/claude/cervix already carry the cx-
prefix in their names.  The builder composes output names as
"<PREFIX>-<slug>.html", so the slugs here are the *unprefixed* tails and the
staging step (scratchpad/stage_cx.py) copies each source to a stripped name —
that same step also inserts the article figures, which the raw fragments
deliberately do not contain.  Output names therefore come out as
cx-cin-vs-cancer.html, never cx-cx-cin-vs-cancer.html.

Unlike nt this is a disease topic, so the JSON-LD "about" entity is the
topicbuild default, MedicalCondition — no ABOUT_TYPE override.
"""

import json
import os

import cervix_en

_STAGE = ("/tmp/claude-0/-home-claude/4bc50b06-d4e4-5989-80b2-34f0f02eed26/"
          "scratchpad/staging-cx")

# ------------------------------------------------------------------ sources --
SRC = {
    "body_zh": os.path.join(_STAGE, "body"),
    "body_en": os.path.join(_STAGE, "en"),
    "meta_zh": "/home/claude/cervix/meta/all.json",
    "meta_en": "/home/claude/cervix/meta/all-en.json",
}

REPO = "/home/claude/repo"

# Existing hub pages the tag labels are harvested from, so no label is retyped.
TAG_SOURCES = {
    "zh": [os.path.join(REPO, n) for n in
           ("hn.html", "rc.html", "cc.html", "bc.html", "nt.html")],
    "en": [os.path.join(REPO, n) for n in
           ("hn-en.html", "rc-en.html", "cc-en.html", "bc-en.html",
            "nt-en.html")],
}

# ------------------------------------------------------------------ identity --
PREFIX = "cx"
KICKER = "CERVICAL CANCER"
NAME_ZH = "子宮頸癌專題"
NAME_EN = "Cervical Cancer Guide"
CONDITION_ZH = "子宮頸癌"
CONDITION_EN = "Cervical cancer"
DATE = "2026-08-30"

# screening / staging / imaging / decision / surgery / chemo / fertility /
# sexual / followup / recurrence / nhi / prep / workflow / mdt / sideeffect /
# daily / qol / lateeffect / trial / endocrine / bone all exist on the
# hn/rc/cc/bc/nt hubs and are reused verbatim.  These three are new; English
# labels follow the existing hubs' convention (Title Case noun phrases, "&"
# where the zh label has 與).
LABEL_ADD = {
    "brachy": ("近接治療", "Brachytherapy"),
    "hpv": ("HPV 與疫苗", "HPV & Vaccines"),
    "menopause": ("停經與荷爾蒙", "Menopause & Hormones"),
}

# ------------------------------------------------------------------ sections --
SECTIONS = [
    {
        "zh": "確診之後",
        "stepsub_zh": "報告上的名詞、分期怎麼來、以及那一題最重的"
                      "「是誰傳給我的」。",
        "slugs": ["cin-vs-cancer", "staging", "hpv", "first-month"],
    },
    {
        "zh": "治療怎麼決定",
        "stepsub_zh": "開刀還是放療、為什麼加化療、生育窗口——"
                      "這四篇是你真正握有發言權的地方。",
        "slugs": ["surgery-or-rt", "mis-brake", "why-chemo", "fertility"],
    },
    {
        "zh": "療程中的照護",
        "stepsub_zh": "近接治療那幾天、五六週怎麼過、"
                      "哪些狀況要當天打電話。",
        "slugs": ["brachytherapy", "pelvic-rt-weeks", "weekly-cisplatin",
                  "vagina-during-rt"],
    },
    {
        "zh": "結束之後",
        "stepsub_zh": "停經、性生活、追蹤，以及復發之後的路。",
        "slugs": ["menopause-hrt", "dilator-sex", "followup-hpv",
                  "recurrence"],
    },
]

TAGS = {
    "cin-vs-cancer": ["screening", "staging", "decision"],
    "staging": ["staging", "imaging", "prep"],
    "hpv": ["hpv", "screening", "qol"],
    "first-month": ["prep", "workflow", "mdt", "nhi"],
    "surgery-or-rt": ["decision", "surgery", "brachy"],
    "mis-brake": ["surgery", "decision"],
    "why-chemo": ["chemo", "decision", "trial", "nhi"],
    "fertility": ["fertility", "decision", "surgery"],
    "brachytherapy": ["brachy", "decision", "sideeffect", "nhi"],
    "pelvic-rt-weeks": ["sideeffect", "daily", "workflow"],
    "weekly-cisplatin": ["chemo", "sideeffect", "daily"],
    "vagina-during-rt": ["sideeffect", "daily", "sexual"],
    "menopause-hrt": ["menopause", "endocrine", "bone", "qol"],
    "dilator-sex": ["sexual", "qol", "lateeffect"],
    "followup-hpv": ["followup", "hpv", "screening", "nhi"],
    "recurrence": ["recurrence", "decision", "trial", "nhi"],
}

# ---------------------------------------------------------- article metadata --
with open(SRC["meta_zh"], encoding="utf-8") as _fh:
    _ZH = json.load(_fh)

ART = {}
for _slug, _tags in TAGS.items():
    _m = dict(_ZH["cx-" + _slug])
    _m["tags"] = _tags
    ART[_slug] = _m

EN = cervix_en.EN
SECTIONS_EN = cervix_en.SECTIONS_EN
HUB_EN = cervix_en.HUB

# ----------------------------------------------------------------- hub copy --
HUB = {
    "title": "子宮頸癌專題｜原位癌與分期、開刀還是放療、近接治療、"
             "HPV 與追蹤｜吳正友醫師",
    "desc": "子宮頸癌病人最需要知道的 16 件事：抹片異常與原位癌差在哪、"
            "分期怎麼來、那一題最重的「是誰傳給我的」、確診後第一個月、"
            "開刀還是放療、微創手術為什麼踩了煞車、為什麼放療要加化療、"
            "生育保存的窗口、近接治療到底是什麼、骨盆放療五六週怎麼過、"
            "每週順鉑、放療期間的陰道照護、治療引起的停經與荷爾蒙補充、"
            "擴張器與性生活、追蹤與 HPV 檢測，以及復發之後的路。"
            "每篇附原始文獻連結。",
    "sub": "從確診那一天，到治療結束好幾年——一個問題一篇。",
    "intro": "子宮頸癌的病人在門診裡最重的三題通常是：為什麼我的是放療不是開刀、"
             "近接治療到底是什麼、還有那句很難說出口的「是誰傳給我的」。"
             "這 16 篇就是照著這三題往外長的，順序跟你真正會走過的一樣："
             "確診之後、治療怎麼決定、療程中的照護，最後是結束之後。"
             "根治性化放療與近接治療是我自己每天在做的治療，"
             "所以這個專題裡關於放療的每一句話，我寫得比別人更保守。"
             "每一篇都附上原始文獻連結，證據弱的地方我會直接說弱。",
    "closing": "以上為一般性衛教說明，不能取代面對面的診療。"
               "子宮頸癌的治療高度取決於期別、腫瘤大小與你的身體條件，"
               "同一個期別在不同人身上會導向不同建議，"
               "實際治療請與你的主治醫師和多專科團隊討論。",
}

# No cross-topic sentence rewrites: the cx fragments carry no relative links
# that need redirecting.
BODY_EDITS = {"zh": [], "en": []}

# topics.html / topics-en.html cards, inserted after the lung-cancer one.
TOPIC_CARD_ZH = """  <a class="topiccard" href="cx.html">
    <div class="k">CERVICAL CANCER</div>
    <div class="t">子宮頸癌專題</div>
    <div class="d">為什麼是放療不是開刀、近接治療到底是什麼、以及「是誰傳給我的」——從確診到治療結束好幾年，一個問題一篇。</div>
    <div class="steps"><span>確診之後</span><span>治療怎麼決定</span><span>療程中的照護</span><span>結束之後</span></div>
    <div class="go"><span class="n">16 篇</span><span class="ar">進入專題 →</span></div>
  </a>
"""

TOPIC_CARD_EN = """  <a class="topiccard" href="cx-en.html">
    <div class="k">CERVICAL CANCER</div>
    <div class="t">Cervical Cancer Guide</div>
    <div class="d">Why radiotherapy and not surgery, what brachytherapy actually is, and "who gave this to me" — from diagnosis to years after treatment ends, one question per article.</div>
    <div class="steps"><span>After the Diagnosis</span><span>How Treatment Is Decided</span><span>During Treatment</span><span>After Treatment</span></div>
    <div class="go"><span class="n">16 articles</span><span class="ar">Open the guide →</span></div>
  </a>
"""

# JSON-LD hasPart entries appended to the topics pages' CollectionPage.
HASPART_ZH = {"@type": "CollectionPage", "name": NAME_ZH,
              "url": "https://doremai2001.github.io/publicpage/cx.html"}
HASPART_EN = {"@type": "CollectionPage", "name": NAME_EN,
              "url": "https://doremai2001.github.io/publicpage/cx-en.html"}
