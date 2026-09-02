# -*- coding: utf-8 -*-
"""Oesophageal-cancer topic module (Chinese side, plus the wiring to the
English one).

Naming: hub ec.html / ec-en.html, articles ec-<slug>.html -- the hub shares
the prefix exactly as cx / pel do, so topicbuild's own _hub_name is correct
and there is NO monkeypatch here (liver needed one; ec does not).

The source fragments under /home/claude/esoph/body already carry the ec-
prefix; stage_esoph_figs.py strips it (and inserts the nine figures) so the
builder's "<PREFIX>-<slug>.html" never comes out as ec-ec-*.  SLUGS below are
therefore the unprefixed tails.

Article metadata: meta/{A,B,C,D}.json are keyed "ec-<slug>"; _ZH is re-keyed
on the tail.  Nothing is retyped.

A disease topic, so the JSON-LD "about" entity is the topicbuild default,
MedicalCondition -- no ABOUT_TYPE override.

The conflict-of-interest paragraph (SPEC section 二) sits before the first
<h4> of exactly four articles -- A4 surgery-or-watch, B1 crt-dose,
B2 immunotherapy, B5 proton -- and nowhere else; verify_esoph pins that.
"""

import json
import os

import esoph_en

_STAGE = "/home/claude/esoph/staging"

# ------------------------------------------------------------------ sources --
SRC = {
    "body_zh": os.path.join(_STAGE, "body"),
    "body_en": os.path.join(_STAGE, "en"),
    "meta_zh": ["/home/claude/esoph/meta/%s.json" % g for g in "ABCD"],
    "meta_en": ["/home/claude/esoph/meta/%s-en.json" % g for g in "ABCD"],
}

REPO = "/home/claude/repo"

# Existing hub pages the tag labels are harvested from, so no label is
# retyped.  hn for swallow/quitting/dental/caregiver, nt for evidence/cost,
# liver for followup/recurrence/trial, pel for emergency, brt for heart.
TAG_SOURCES = {
    "zh": [os.path.join(REPO, n) for n in
           ("hn.html", "rc.html", "cc.html", "bc.html", "nt.html", "cx.html",
            "liver.html", "brt.html", "pel.html")],
    "en": [os.path.join(REPO, n) for n in
           ("hn-en.html", "rc-en.html", "cc-en.html", "bc-en.html",
            "nt-en.html", "cx-en.html", "liver-en.html", "brt-en.html",
            "pel-en.html")],
}

# ------------------------------------------------------------------ identity --
PREFIX = "ec"
KICKER = "OESOPHAGEAL CANCER"
NAME_ZH = "食道癌專題"
NAME_EN = "Oesophageal Cancer Guide"
CONDITION_ZH = "食道癌"
CONDITION_EN = "Oesophageal cancer"
DATE = "2026-09-02"

# staging / decision / quitting / evidence / imaging / workflow / surgery /
# organsave / sideeffect / chemo / immuno / nhi / biomarker / screening /
# proton / cost / heart / nutrition / swallow / daily / emergency / prep /
# dental / caregiver / survivor / recurrence / followup / trial / qol all
# exist on the harvested hubs and are reused verbatim ("swallow" is hn's
# existing 吞嚥與進食 / Swallowing key, so no new "swallowing" key is added).
# These three are new; English labels follow the existing hubs' convention
# (Title Case noun phrases, British spelling).
LABEL_ADD = {
    "esophagectomy": ("食道切除", "Oesophagectomy"),
    "feedingtube": ("管路與營養", "Feeding Tubes"),
    "endoscopy": ("內視鏡", "Endoscopy"),
}

# ------------------------------------------------------------------ sections --
# Group titles and per-group order verbatim from SPEC section 五 (4/5/4/4).
SECTIONS = [
    {
        "zh": "治療怎麼決定",
        "stepsub_zh": "鱗癌和腺癌是兩種病、哪幾張檢查決定能不能開刀、"
                      "整張治療地圖你在哪一格，以及化放療做完最常被問的那一題："
                      "還要不要開刀。",
        "slugs": ["two-diseases", "workup", "treatment-map",
                  "surgery-or-watch"],
    },
    {
        "zh": "每種治療的實證效益",
        "stepsub_zh": "放療劑量為什麼加了沒換到控制、免疫治療到底幫了誰、"
                      "開刀拿掉什麼、早期病灶內視鏡夠不夠，以及質子的試驗走到哪一格。",
        "slugs": ["crt-dose", "immunotherapy", "surgery", "esd", "proton"],
    },
    {
        "zh": "療程中的照護",
        "stepsub_zh": "管路要不要先放、食道炎那幾週怎麼過又為什麼不能自己停、"
                      "哪些狀況要當天回來，以及開始前必談的幾件事。",
        "slugs": ["feeding-tube", "esophagitis", "warning-signs",
                  "before-start"],
    },
    {
        "zh": "結束之後",
        "stepsub_zh": "胃被拉進胸腔之後怎麼吃、吞嚥又變差是狹窄還是復發、"
                      "追蹤怎麼排與別忘了的第二原發癌，以及復發之後還有哪些路。",
        "slugs": ["eating-after", "stricture-or-recurrence", "followup",
                  "recurrence"],
    },
]

TAGS = {
    "two-diseases": ["staging", "decision", "quitting", "evidence"],
    "workup": ["staging", "imaging", "workflow", "decision"],
    "treatment-map": ["decision", "staging", "surgery", "workflow"],
    "surgery-or-watch": ["decision", "surgery", "organsave", "evidence"],
    "crt-dose": ["evidence", "chemo", "sideeffect", "decision"],
    "immunotherapy": ["immuno", "biomarker", "nhi", "evidence"],
    "surgery": ["esophagectomy", "surgery", "sideeffect", "evidence"],
    "esd": ["endoscopy", "screening", "nhi", "evidence"],
    "proton": ["proton", "heart", "cost", "evidence"],
    "feeding-tube": ["feedingtube", "nutrition", "swallow", "daily"],
    "esophagitis": ["sideeffect", "swallow", "nutrition", "daily"],
    "warning-signs": ["emergency", "sideeffect", "daily"],
    "before-start": ["prep", "quitting", "dental", "caregiver"],
    "eating-after": ["esophagectomy", "nutrition", "swallow", "survivor"],
    "stricture-or-recurrence": ["swallow", "recurrence", "endoscopy",
                                "followup"],
    "followup": ["followup", "imaging", "screening", "recurrence"],
    "recurrence": ["recurrence", "decision", "trial", "qol"],
}

# ---------------------------------------------------------- article metadata --
_ZH = {}
for _p in SRC["meta_zh"]:
    with open(_p, encoding="utf-8") as _fh:
        for _k, _rec in json.load(_fh).items():
            _ZH[_k[len("ec-"):]] = _rec

ART = {}
for _slug, _tags in TAGS.items():
    _m = dict(_ZH[_slug])
    _m["tags"] = _tags
    ART[_slug] = _m

EN = esoph_en.EN
SECTIONS_EN = esoph_en.SECTIONS_EN
HUB_EN = esoph_en.HUB

# ----------------------------------------------------------------- hub copy --
HUB = {
    "title": "食道癌專題｜鱗癌還是腺癌、化放療後要不要開刀、劑量與免疫、"
             "質子、管路與食道切除後的日子｜吳正友醫師",
    "desc": "食道癌病人最需要知道的 17 件事：鱗癌和腺癌其實是兩種病、"
            "決定能不能開刀的是哪幾張檢查、整張治療地圖你在哪一格、"
            "化放療做完還要不要開刀、放療劑量為什麼不是越高越好、"
            "免疫治療到底幫了誰、開刀會拿掉什麼胃會被拉到哪裡、"
            "早期病灶內視鏡就能解決嗎、質子在食道癌的升級理由與現況、"
            "吞不下體重一直掉時管路要不要先放、放療期間的食道炎怎麼過、"
            "哪些狀況要當天回來、開始治療前必談的幾件事、"
            "食道切掉之後怎麼吃、吞嚥又變差是狹窄還是復發、"
            "追蹤怎麼排與別忘了第二原發癌，以及復發與轉移之後還有哪些路。"
            "每篇附原始文獻連結。",
    "sub": "從病理報告那一天，到治療結束好幾年——一個問題一篇。",
    "intro": "食道癌病人心裡最重的三件事：還能不能吃東西、要不要開那個大刀、"
             "免疫治療是不是我的解藥。這 17 篇照著你真正會走過的順序排："
             "治療怎麼決定、每種治療的實證效益、療程中的照護，最後是結束之後。"
             "先說我的位置：食道癌的同步化放療和質子治療，是我自己每週在做的治療；"
             "這個專題比較的另一邊，是胸腔外科同事的手術和腸胃科同事的內視鏡——"
             "所以拿放射去比手術和內視鏡的那四篇，開頭都有同一段利益揭露，"
             "每一個比較都附上原始文獻，讓你可以拿著它去外科和腸胃科聽第二意見。"
             "台灣九成以上是鱗癌，所以主線寫鱗癌；腺癌走另一條路，單獨一篇講清楚。"
             "每一篇都附上原始文獻連結，證據弱的地方我會直接說弱，"
             "數字查不到的地方我會說查不到。",
    "closing": "以上為一般性衛教說明，不能取代面對面的診療。"
               "食道癌的治療同時取決於組織型態、期別、腫瘤位置、"
               "體能狀況與營養狀態，同一個期別在不同人身上會導向不同建議，"
               "實際治療請與你的主治醫師和多專科團隊討論。",
}

# No cross-topic sentence rewrites: the ec fragments' only relative links
# point at care-fever(-en).html, nt-proton(-en).html and
# insight-proton(-en).html, which exist on the site under exactly those names.
BODY_EDITS = {"zh": [], "en": []}

# topics.html / topics-en.html cards, inserted after the pel one (the last
# card on the pulled topics pages, which carry 10 cards).
TOPIC_CARD_ZH = """  <a class="topiccard" href="ec.html">
    <div class="k">OESOPHAGEAL CANCER</div>
    <div class="t">食道癌專題</div>
    <div class="d">還能不能吃、要不要開那個大刀、免疫治療是不是解藥——鱗癌與腺癌怎麼分、化放療後開不開刀的證據走到哪、管路與食道切除後的日子，從病理報告到治療結束好幾年，一個問題一篇。</div>
    <div class="steps"><span>治療怎麼決定</span><span>每種治療的實證效益</span><span>療程中的照護</span><span>結束之後</span></div>
    <div class="go"><span class="n">17 篇</span><span class="ar">進入專題 →</span></div>
  </a>
"""

TOPIC_CARD_EN = """  <a class="topiccard" href="ec-en.html">
    <div class="k">OESOPHAGEAL CANCER</div>
    <div class="t">Oesophageal Cancer Guide</div>
    <div class="d">Will I still be able to eat, do I need the big operation, is immunotherapy my answer — squamous versus adenocarcinoma, where the evidence on surgery after chemoradiotherapy stands, feeding tubes and life after an oesophagectomy. From the pathology report to years after treatment, one question per article.</div>
    <div class="steps"><span>How Treatment Is Decided</span><span>What the Evidence Says for Each Treatment</span><span>During Treatment</span><span>After Treatment</span></div>
    <div class="go"><span class="n">17 articles</span><span class="ar">Open the guide →</span></div>
  </a>
"""

# JSON-LD hasPart entries appended to the topics pages' CollectionPage.
HASPART_ZH = {"@type": "CollectionPage", "name": NAME_ZH,
              "url": "https://doremai2001.github.io/publicpage/ec.html"}
HASPART_EN = {"@type": "CollectionPage", "name": NAME_EN,
              "url": "https://doremai2001.github.io/publicpage/ec-en.html"}
