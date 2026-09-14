# -*- coding: utf-8 -*-
"""Bladder-cancer topic module (Chinese side, plus the wiring to the English
one).

Naming: hub bl.html / bl-en.html, articles bl-<slug>.html -- the hub shares
the prefix exactly as bt / em / ec / cx / pel do, so topicbuild's own
_hub_name gives "bl.html" / "bl-en.html" and there is NO monkeypatch here.
Checked before writing this module: topicbuild._hub_name("bl", "zh") ==
"bl.html".

The source fragments under /home/claude/bl/body carry the bl- prefix; the
English ones under /home/claude/bl/en carry BOTH the bl- prefix and a -en
suffix (the bt convention, not the em one).  stage_bl_figs.py strips both and
inserts the twelve figures.

Article metadata: meta/{A,B,C,D,E}.json are keyed "bl-<slug>"; _ZH is re-keyed
on the tail.  Nothing is retyped -- the titles in those files are already
SPEC.md 修正 25's canonical set.

A disease topic, so the JSON-LD "about" entity is the topicbuild default,
MedicalCondition -- no ABOUT_TYPE override.

The conflict-of-interest paragraph (SPEC section 二) sits before the first
<h4> of exactly three articles -- C1 two-roads, C4 tmt, C5 tmt-after -- and
nowhere else; verify_bl pins that.  Unlike the previous topics this one
discloses an argument rather than a procedure: the author holds that Taiwan
under-uses bladder preservation, and SPEC 修正 2 fixes the three pillars that
claim may rest on and forbids any Taiwanese utilisation figure.
"""

import json
import os

import bl_en

_STAGE = "/home/claude/bl/staging"

# ------------------------------------------------------------------ sources --
SRC = {
    "body_zh": os.path.join(_STAGE, "body"),
    "body_en": os.path.join(_STAGE, "en"),
    "meta_zh": ["/home/claude/bl/meta/%s.json" % g for g in "ABCDE"],
    "meta_en": ["/home/claude/bl/meta/%s-en.json" % g for g in "ABCDE"],
}

REPO = "/home/claude/repo"

# Existing hub pages the tag labels are harvested from, so no label is
# retyped.  First hub listed wins for a key two hubs label differently:
# em leads because it owns "bleeding"; pc follows for "surveil" and
# "urinary"; ec for "organsave"; hn for "quitting".
TAG_SOURCES = {
    "zh": [os.path.join(REPO, n) for n in
           ("em.html", "pc.html", "ec.html", "pel.html", "bt.html",
            "gbm.html", "liver.html", "cx.html", "bc.html", "lc.html",
            "nt.html", "brt.html", "cc.html", "rc.html", "hn.html")],
    "en": [os.path.join(REPO, n) for n in
           ("em-en.html", "pc-en.html", "ec-en.html", "pel-en.html",
            "bt-en.html", "gbm-en.html", "liver-en.html", "cx-en.html",
            "bc-en.html", "lc-en.html", "nt-en.html", "brt-en.html",
            "cc-en.html", "rc-en.html", "hn-en.html")],
}

# ------------------------------------------------------------------ identity --
PREFIX = "bl"
KICKER = "BLADDER CANCER"
NAME_ZH = "膀胱癌專題"
NAME_EN = "Bladder Cancer Guide"
CONDITION_ZH = "膀胱癌"
CONDITION_EN = "Bladder cancer"
DATE = "2026-09-14"

# bleeding / imaging / screening / decision / surgery / staging / molecular /
# evidence / surveil / recurrence / immuno / sideeffect / emergency / trial /
# followup / organsave / chemo / urinary / sexual / recovery / lateeffect /
# nhi / targeted / biomarker / prevention / quitting / qol / work all exist on
# the harvested hubs and are reused verbatim.  This one is new: the site's
# existing "stoma" label reads 人工肛門, which is a bowel stoma and wrong for
# a urinary one, so the topic gets its own key rather than borrowing it.
LABEL_ADD = {
    "urostomy": ("尿路造口", "Urostomy"),
}

# ------------------------------------------------------------------ sections --
# Group titles and per-group order verbatim from SPEC section 五 (4/4/5/2/3).
SECTIONS = [
    {
        "zh": "確診與分期",
        "stepsub_zh": "不痛的血尿為什麼是要查的那一種、第一次刮除為什麼決定了後面所有事、"
                      "報告上的 Ta、T1、CIS 是什麼意思，以及影像看得到與看不到什麼。",
        "slugs": ["hematuria", "turbt", "report", "staging"],
    },
    {
        "zh": "非肌肉侵犯型",
        "stepsub_zh": "風險分層決定了要不要灌藥、卡介苗到底是什麼又不是什麼、"
                      "它沒效之後還有哪些路，以及膀胱鏡要照到什麼時候。",
        "slugs": ["nmibc-risk", "bcg", "bcg-fail", "nmibc-followup"],
    },
    {
        "zh": "肌肉侵犯型：兩條路",
        "stepsub_zh": "切掉膀胱還是保留膀胱、這個比較的實證到底長什麼樣、開刀前為什麼要先化療、"
                      "手術與三種尿路改道的代價、三聯療法怎麼做誰適合，"
                      "以及保留下來的膀胱之後要顧什麼。",
        "slugs": ["two-roads", "neoadjuvant", "cystectomy", "tmt",
                  "tmt-after"],
    },
    {
        "zh": "轉移與全身治療",
        "stepsub_zh": "轉移之後的第一線現在是什麼、台灣的藥證與健保在哪裡分家，"
                      "以及基因檢測的哪一格真的有藥。",
        "slugs": ["metastatic", "biomarker"],
    },
    {
        "zh": "台灣與之後",
        "stepsub_zh": "台灣為什麼有那麼多尿路上皮癌長在上泌尿道、馬兜鈴酸的證據說了什麼又沒說什麼、"
                      "抽菸這一題怎麼寫才不是責備，以及帶著造口或新膀胱怎麼回到日子裡。",
        "slugs": ["utuc", "smoking", "daily"],
    },
]

TAGS = {
    "hematuria": ["bleeding", "imaging", "screening", "decision"],
    "turbt": ["surgery", "staging", "imaging", "evidence"],
    "report": ["staging", "molecular", "evidence", "decision"],
    "staging": ["imaging", "staging", "decision", "evidence"],
    "nmibc-risk": ["surveil", "decision", "evidence", "recurrence"],
    "bcg": ["immuno", "sideeffect", "emergency", "evidence"],
    "bcg-fail": ["immuno", "trial", "decision", "recurrence"],
    "nmibc-followup": ["followup", "surveil", "imaging", "recurrence"],
    "two-roads": ["decision", "surgery", "organsave", "evidence"],
    "neoadjuvant": ["chemo", "immuno", "surgery", "evidence"],
    "cystectomy": ["surgery", "urostomy", "sexual", "recovery"],
    "tmt": ["organsave", "chemo", "evidence", "nhi"],
    "tmt-after": ["followup", "lateeffect", "urinary", "recurrence"],
    "metastatic": ["chemo", "immuno", "nhi", "evidence"],
    "biomarker": ["molecular", "targeted", "biomarker", "nhi"],
    "utuc": ["screening", "prevention", "surgery", "evidence"],
    "smoking": ["quitting", "prevention", "evidence", "qol"],
    "daily": ["urostomy", "qol", "work", "recovery"],
}

# ---------------------------------------------------------- article metadata --
_ZH = {}
for _p in SRC["meta_zh"]:
    with open(_p, encoding="utf-8") as _fh:
        for _k, _rec in json.load(_fh).items():
            _ZH[_k[len("bl-"):]] = _rec

ART = {}
for _slug, _tags in TAGS.items():
    _m = dict(_ZH[_slug])
    _m["tags"] = _tags
    ART[_slug] = _m

EN = bl_en.EN
SECTIONS_EN = bl_en.SECTIONS_EN
HUB_EN = bl_en.HUB

# ----------------------------------------------------------------- hub copy --
HUB = {
    "title": "膀胱癌專題｜不痛的血尿、Ta 與 T1 與 CIS、卡介苗、切掉膀胱還是保留膀胱、"
             "三聯療法、上泌尿道，以及回到日子裡｜吳正友醫師",
    "desc": "膀胱癌病人最需要知道的 18 件事：不痛的血尿為什麼是要查的那一種、"
            "第一次刮除為什麼決定了後面所有事、報告上的 Ta、T1、CIS 是什麼意思、"
            "非肌肉侵犯型與肌肉侵犯型這條線為什麼是這個病最硬的一條線、"
            "風險分層決定了要不要灌藥、卡介苗到底是什麼又為什麼全球在缺、"
            "卡介苗沒效之後還有哪些路、膀胱鏡要照到什麼時候、"
            "切掉膀胱還是保留膀胱以及這個比較的實證到底長什麼樣、"
            "開刀前為什麼要先化療、膀胱全切除與三種尿路改道的代價、"
            "三聯療法怎麼做誰適合、保留下來的膀胱之後要顧什麼、"
            "轉移之後的第一線與台灣藥證和健保分家的那一格、基因檢測哪一格真的有藥、"
            "台灣為什麼那麼多長在上泌尿道、抽菸這一題，"
            "以及帶著造口或新膀胱怎麼回到日子裡。每篇附原始文獻連結。",
    "sub": "從第一滴不痛的血尿，到之後好幾年的追蹤——一個問題一篇。",
    "intro": "這個專題有兩條線，關於膀胱癌的誤解幾乎都是某個數字越過了其中一條。"
             "第一條是非肌肉侵犯型（Ta、T1、原位癌）與肌肉侵犯型（T2 以上）之間："
             "治療、預後與追蹤都不共用，一個沒有標明站在哪一邊的存活數字，"
             "就算算術沒錯也是錯的。第二條是膀胱與上泌尿道（腎盂、輸尿管）之間："
             "顯微鏡下是同一種細胞，手術不同、追蹤不同，在台灣連流行病學都完全不同。"
             "所以這裡每一個數字都帶著它的邊，而「表淺型」這三個字不會出現"
             "——歐洲的指引明文寫著不要用它。"
             "先說我的位置：三聯療法裡的放射治療是我自己在做的那一段，"
             "而這個專題主張台灣的保留膀胱做得太少，這個主張對我有利。"
             "所以有三篇開頭放了同一段利益揭露，每一個比較都附原始文獻，"
             "而且我把保留膀胱做不到的地方也寫出來——包括這一題到今天"
             "沒有一個成功完成的隨機試驗，以及保留膀胱的人裡大約每五個有一個，"
             "最後還是切掉了。證據弱的地方我會直接說弱，數字查不到的地方我會說查不到。",
    "closing": "以上為一般性衛教說明，不能取代面對面的診療。"
               "膀胱癌怎麼處理，同時取決於有沒有侵犯肌肉層、分化度、有沒有原位癌、"
               "有沒有水腎、第一次刮除刮得乾不乾淨與檢體裡有沒有逼尿肌、腎功能，"
               "以及你整體的身體狀況；同一份報告在不同人身上會導向不同建議。"
               "實際治療請與你的泌尿科、放射腫瘤科、腫瘤內科主治醫師與多專科團隊討論。",
}

# No cross-topic sentence rewrites inside the bl fragments: every in-topic and
# on-site cross-reference is an unlinked 〈title〉 (zh) or "title" (en), as
# SPEC-EN section 4 prescribes, so there is nothing to rewrite at build time.
BODY_EDITS = {"zh": [], "en": []}

# topics.html / topics-en.html cards, inserted after the bt one (the last
# card on the pulled topics pages, which carry 14 cards).
TOPIC_CARD_ZH = """  <a class="topiccard" href="bl.html">
    <div class="k">BLADDER CANCER</div>
    <div class="t">膀胱癌專題</div>
    <div class="d">關於這個病的誤解，幾乎都是某個數字越過了兩條線的其中一條——非肌肉侵犯型與肌肉侵犯型之間，膀胱與上泌尿道之間。所以這裡每個數字都帶著它的邊。從第一滴不痛的血尿，到切掉膀胱還是保留膀胱那一題的實證到底長什麼樣，一個問題一篇。</div>
    <div class="steps"><span>確診與分期</span><span>非肌肉侵犯型</span><span>肌肉侵犯型</span><span>轉移與全身治療</span><span>台灣與之後</span></div>
    <div class="go"><span class="n">18 篇</span><span class="ar">進入專題 →</span></div>
  </a>
"""

TOPIC_CARD_EN = """  <a class="topiccard" href="bl-en.html">
    <div class="k">BLADDER CANCER</div>
    <div class="t">Bladder Cancer Guide</div>
    <div class="d">Almost every misunderstanding about this disease is a number that crossed one of two lines — between non-muscle-invasive and muscle-invasive disease, and between the bladder and the upper tract. So every number here carries its side. From the first painless drop of blood in the urine to what the evidence for removing the bladder against keeping it actually looks like, one question per article.</div>
    <div class="steps"><span>Diagnosis and staging</span><span>Non-muscle-invasive</span><span>Muscle-invasive</span><span>Metastatic therapy</span><span>Taiwan and afterwards</span></div>
    <div class="go"><span class="n">18 articles</span><span class="ar">Open the guide →</span></div>
  </a>
"""

# JSON-LD hasPart entries appended to the topics pages' CollectionPage.
HASPART_ZH = {"@type": "CollectionPage", "name": NAME_ZH,
              "url": "https://doremai2001.github.io/publicpage/bl.html"}
HASPART_EN = {"@type": "CollectionPage", "name": NAME_EN,
              "url": "https://doremai2001.github.io/publicpage/bl-en.html"}

# ------------------------------------------------------- build-time chore ---
# pel-who(-en).html is the page that has been promising this topic since the
# pelvic-radiotherapy round: three places in Chinese, two in English.
#
# On the LINK question this follows the endo round, not the bt one, and the
# difference was re-checked on 2026-09-14 rather than assumed: pel-who's body
# carries ZERO in-body site links -- every pointer on that page is an unlinked
# 〈title〉, including the 〈子宮內膜癌專題〉 the endo round put there -- so this
# round points in sense too and adds no <a>.  (gb-what-it-is was the opposite
# case: it already linked lc-brainmet, so the bt round matched its house form
# and did add one.)  Verified: 12 unlinked 〈…〉 pointers in the body, 0 links.
#
# verify_bl pins the diff to exactly these five substitutions.
PEL_WHO_EDITS = {
    "pel-who.html": [
        (
            "膀胱癌另有專題規劃中，這裡不代寫疾病介紹。",
            "膀胱癌另有專題〈膀胱癌專題〉，這裡不代寫疾病介紹。",
        ),
        (
            "整顆膀胱要照時很多醫院用的是空膀胱流程；膀胱癌另有專題規劃中。",
            "整顆膀胱要照時很多醫院用的是空膀胱流程；膀胱癌另有專題。",
        ),
        (
            "子宮內膜癌現在也有自己的專題，膀胱癌那一篇還在規劃中。",
            "子宮內膜癌與膀胱癌現在都有自己的專題了。",
        ),
    ],
    "pel-who-en.html": [
        (
            "A separate bladder cancer topic is being planned; I am not "
            "writing the disease introduction here.",
            "There is a separate topic on bladder cancer, \"Bladder Cancer "
            "Guide\"; I am not writing the disease introduction here.",
        ),
        (
            "endometrial cancer now has a topic of its own, and the bladder "
            "cancer topic is still being planned.",
            "endometrial cancer and bladder cancer now both have topics of "
            "their own.",
        ),
    ],
}
