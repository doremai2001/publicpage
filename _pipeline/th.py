# -*- coding: utf-8 -*-
"""Thyroid-cancer topic module (Chinese side, plus the wiring to the English
one).

Naming: hub th.html / th-en.html, articles th-<slug>.html -- the hub shares
the prefix exactly as bl / bt / em / ec / cx / pel do, so topicbuild's own
_hub_name gives "th.html" / "th-en.html" and there is NO monkeypatch here.
Checked before writing this module, not assumed:
topicbuild._hub_name("th", "zh") == "th.html".

The source fragments under /home/claude/th/body carry the th- prefix; the
English ones under /home/claude/th/en carry BOTH the th- prefix and a -en
suffix (the bl / bt convention, not the em one).  stage_th_figs.py strips
both and inserts the twelve figures at thirteen places.

Article metadata: meta/{A,B,C,D,E}.json are keyed "th-<slug>"; _ZH is
re-keyed on the tail.  Nothing is retyped -- the titles in those files are
already SPEC.md 四's canonical set (and 修正 10's retitle of A5).

A disease topic, so the JSON-LD "about" entity is the topicbuild default,
MedicalCondition -- no ABOUT_TYPE override.

The conflict-of-interest paragraph (SPEC section 二) sits before the first
<h4> of exactly ONE article -- D5 th-ebrt -- and nowhere else; verify_th
pins that.  Unlike bl, whose disclosure ran across three articles because
the topic argued a position the author benefits from, this one discloses a
conclusion that costs the author: external beam radiotherapy is his own
part of the work and the article concludes that almost nobody needs it.

THIS ROUND HAS NO SHARED-FILE CHORE.  Nothing already published promises a
thyroid topic -- re-checked rather than assumed: pel-who's promise was the
bladder one and gb-what-it-is's was the brain one, both already redeemed --
so SHARED is three files (topics.html, topics-en.html, sitemap.xml) and no
existing article body is edited.  bl's PEL_WHO_EDITS machinery and the
verifier check that pinned it are deleted rather than left inert.
"""

import json
import os

import th_en

_STAGE = "/home/claude/th/staging"

# ------------------------------------------------------------------ sources --
SRC = {
    "body_zh": os.path.join(_STAGE, "body"),
    "body_en": os.path.join(_STAGE, "en"),
    "meta_zh": ["/home/claude/th/meta/%s.json" % g for g in "ABCDE"],
    "meta_en": ["/home/claude/th/meta/%s-en.json" % g for g in "ABCDE"],
}

REPO = "/home/claude/repo"

# Existing hub pages the tag labels are harvested from, so no label is
# retyped.  First hub listed wins for a key two hubs label differently, and
# two of this topic's keys are contested: em leads because it owns the plain
# "followup" (追蹤與復健 / Follow-up; pc calls it 追蹤與 PSA and lc just 追蹤)
# and the plain "screening" (篩檢 / Screening; lc calls it 篩檢與結節).  Both
# plain forms are the ones this topic wants.  pc follows for "surveil".
TAG_SOURCES = {
    "zh": [os.path.join(REPO, n) for n in
           ("em.html", "pc.html", "ec.html", "pel.html", "bt.html",
            "bl.html", "gbm.html", "liver.html", "cx.html", "bc.html",
            "lc.html", "nt.html", "brt.html", "cc.html", "rc.html",
            "hn.html")],
    "en": [os.path.join(REPO, n) for n in
           ("em-en.html", "pc-en.html", "ec-en.html", "pel-en.html",
            "bt-en.html", "bl-en.html", "gbm-en.html", "liver-en.html",
            "cx-en.html", "bc-en.html", "lc-en.html", "nt-en.html",
            "brt-en.html", "cc-en.html", "rc-en.html", "hn-en.html")],
}

# ------------------------------------------------------------------ identity --
PREFIX = "th"
KICKER = "THYROID CANCER"
NAME_ZH = "甲狀腺癌專題"
NAME_EN = "Thyroid Cancer Guide"
CONDITION_ZH = "甲狀腺癌"
CONDITION_EN = "Thyroid cancer"
DATE = "2026-09-14"

# imaging / screening / decision / evidence / staging / molecular /
# recurrence / prevention / surveil / surgery / endocrine / trial /
# sideeffect / recovery / nhi / prep / daily / nutrition / bone / followup /
# biomarker / targeted / mdt / lateeffect / genetic / emergency / work /
# qol / regulation / cost all exist on the harvested hubs and are reused
# verbatim.  These two are new:
#
#   radioiodine -- the site has no key for I-131 at all.  The nearest
#     existing keys are radiotherapy modalities (brachy, proton, imrt) or
#     the non-hub "radsafety", none of which is a systemic radioisotope
#     given by mouth; three of these twenty articles are about it.
#   voice -- the site has swallow, dental, xerostomia, trismus and orn for
#     the head and neck, but nothing for the voice.  The recurrent
#     laryngeal nerve is the signature complication of this operation and
#     two articles turn on it, so it gets its own key rather than being
#     folded into the generic "sideeffect".
LABEL_ADD = {
    "radioiodine": ("放射碘", "Radioiodine"),
    "voice": ("聲音", "Voice"),
}

# ------------------------------------------------------------------ sections --
# Group titles and per-group order verbatim from SPEC section 四 (5/4/2/5/4).
SECTIONS = [
    {
        "zh": "確診與分期",
        "stepsub_zh": "超音波說「懷疑惡性」到底是什麼意思、細針報告上那個編號怎麼讀、"
                      "乳突與濾泡與 NIFTP 的差別、為什麼分期要看你幾歲，"
                      "以及這個病為什麼忽然變那麼多。",
        "slugs": ["nodule", "fna", "pathology", "staging", "overdiagnosis"],
    },
    {
        "zh": "低風險那一格：要不要那麼積極",
        "stepsub_zh": "不開刀先看著這件事有哪些明文條件、半切還是全切那條線畫在哪裡、"
                      "淋巴結要不要一起清，以及開完刀身上會少掉什麼。",
        "slugs": ["active-surveillance", "lobectomy", "neck-dissection",
                  "surgery-risks"],
    },
    {
        "zh": "放射碘",
        "stepsub_zh": "四個去階梯試驗各自回答了哪個問題、誰現在還需要做，"
                      "以及真的要做的話那幾天怎麼過。",
        "slugs": ["rai-whether", "rai-days"],
    },
    {
        "zh": "追蹤與進階",
        "stepsub_zh": "吃一輩子的那顆藥要吃到多少、追蹤到底在看什麼、"
                      "Tg 上升卻找不到東西怎麼辦、放射碘無效之後還有什麼，"
                      "以及體外放射線治療在這個病裡的位置。",
        "slugs": ["tsh", "followup", "recurrence", "rai-refractory", "ebrt"],
    },
    {
        "zh": "另外兩個病，以及台灣",
        "stepsub_zh": "髓質癌與它背後的遺傳、未分化癌為什麼是急症、"
                      "疤與聲音與體重與回去上班，以及這條路在台灣怎麼走。",
        "slugs": ["mtc", "atc", "daily", "taiwan"],
    },
]

TAGS = {
    "nodule": ["imaging", "screening", "decision", "evidence"],
    "fna": ["staging", "molecular", "decision", "evidence"],
    "pathology": ["staging", "molecular", "evidence", "recurrence"],
    "staging": ["staging", "evidence", "decision", "recurrence"],
    "overdiagnosis": ["screening", "evidence", "prevention", "decision"],
    "active-surveillance": ["surveil", "decision", "evidence", "imaging"],
    "lobectomy": ["surgery", "decision", "evidence", "endocrine"],
    "neck-dissection": ["surgery", "evidence", "trial", "recurrence"],
    "surgery-risks": ["surgery", "sideeffect", "voice", "recovery"],
    "rai-whether": ["radioiodine", "decision", "evidence", "nhi"],
    "rai-days": ["radioiodine", "prep", "daily", "nutrition"],
    "tsh": ["endocrine", "bone", "sideeffect", "followup"],
    "followup": ["followup", "imaging", "biomarker", "recurrence"],
    "recurrence": ["recurrence", "biomarker", "imaging", "decision"],
    "rai-refractory": ["radioiodine", "targeted", "trial", "nhi"],
    "ebrt": ["evidence", "decision", "mdt", "lateeffect"],
    "mtc": ["genetic", "biomarker", "surgery", "targeted"],
    "atc": ["emergency", "mdt", "targeted", "molecular"],
    "daily": ["voice", "work", "qol", "recovery"],
    "taiwan": ["nhi", "regulation", "cost", "mdt"],
}

# ---------------------------------------------------------- article metadata --
_ZH = {}
for _p in SRC["meta_zh"]:
    with open(_p, encoding="utf-8") as _fh:
        for _k, _rec in json.load(_fh).items():
            _ZH[_k[len("th-"):]] = _rec

ART = {}
for _slug, _tags in TAGS.items():
    _m = dict(_ZH[_slug])
    _m["tags"] = _tags
    ART[_slug] = _m

EN = th_en.EN
SECTIONS_EN = th_en.SECTIONS_EN
HUB_EN = th_en.HUB

# ----------------------------------------------------------------- hub copy --
HUB = {
    "title": "甲狀腺癌專題｜照到一顆結節、細針報告的編號、不開刀先看著、半切還是全切、"
             "放射碘、吃一輩子的那顆藥，以及在台灣這條路怎麼走｜吳正友醫師",
    "desc": "甲狀腺癌病人最需要知道的 20 件事：超音波說「懷疑惡性」是什麼意思、"
            "為什麼四套風險分層表對同一顆結節會給不同答案、細針報告上那個編號怎麼讀、"
            "乳突與濾泡與 NIFTP 改名這件事、為什麼分期要看你幾歲、"
            "期別與復發風險為什麼是兩套不連在一起的系統、這個病為什麼忽然變那麼多、"
            "過度診斷對你個人到底意味著什麼、不開刀先看著有哪些明文的納入與退出條件、"
            "半切還是全切那條線畫在哪裡、淋巴結要不要一起清、開完刀身上會少掉什麼、"
            "要不要做放射碘以及真的要做的話那幾天怎麼過、"
            "吃一輩子的那顆藥要吃到多少與代價是什麼、追蹤在看什麼、"
            "Tg 上升卻找不到東西怎麼辦、放射碘無效之後還有什麼、"
            "體外放射線治療在這個病裡的位置、髓質癌與未分化癌是另外兩個病、"
            "疤與聲音與體重與回去上班，以及在台灣健保付到哪裡。每篇附原始文獻連結。",
    "sub": "從健檢照到的那一顆，到之後好幾年的追蹤——一個問題一篇。",
    "intro": "這個病的讀者跟站上其他專題都不一樣：絕大多數人是在完全沒有不舒服的時候"
             "被告知得了癌症——健檢超音波照到一顆，或摸到一個不痛的東西。"
             "所以第一個問號不是「我還能活多久」，而是「這到底算不算一回事」。"
             "而這個問號會往兩個相反的方向出錯。往下，是「聽說甲狀腺癌是最好的癌」"
             "——於是不回診、不追蹤，或者被這句話安慰之後，"
             "才發現自己其實站在高風險那一格。往上，是把「癌」這個字讀成必須立刻全切、"
             "必須做放射碘、必須終身抑制——於是拿到一個不需要的手術、"
             "一段不需要的輻射、一輩子過量的甲狀腺素。"
             "這個專題真正的工作，是把你放進正確的那一格，並且把那一格的代價講清楚。"
             "所以這裡每一個存活或復發數字都帶著它的風險組、年齡切點、組織型與終點，"
             "而那些安慰但不給資訊的說法不會出現。我的位置也先說在這裡："
             "體外放射線治療是我自己在做的那一段，而那一篇的結論是"
             "分化型甲狀腺癌裡絕大多數人不需要它——那一篇開頭放了利益揭露。"
             "證據弱的地方我會直接說弱，數字查不到的地方我會說查不到。",
    "closing": "以上為一般性衛教說明，不能取代面對面的診療。"
               "甲狀腺癌怎麼處理，同時取決於組織型與亞型、腫瘤大小與有沒有侵犯到腺體外、"
               "淋巴結、你的年齡、超音波看到什麼、甲狀腺球蛋白與抗體的狀態，"
               "以及你整體的身體狀況；同一份報告在不同人身上會導向不同建議。"
               "放射碘的劑量、隔離規定與低碘飲食一律依你醫院核子醫學科的規定，不是依這一頁。"
               "實際治療請與你的內分泌科、外科、核子醫學科主治醫師與多專科團隊討論。",
}

# Cross-topic sentence rewrites applied to the fragments at build time.
#
# bl had none.  This topic has three, all on the English side and all of the
# same kind: SPEC-EN section 5 requires the three off-series English pages
# this topic points at to be named by their LIVE <h1>, "上線前要再核一次",
# and EN-REPORT-A.md and EN-REPORT-D.md record that the writing session could
# not reach those pages and left placeholder strings behind, flagged as a
# blocking item for build time.  This is that replacement, done here rather
# than in the source fragments so that the fragments stay the thing the
# verifier diffs against.  The right-hand sides are the live pages' own
# <h1>, read off the repo, not retyped from the spec:
#   hn-late-effects-en.html   -> The side effects that arrive years later
#   hn-followup-en.html       -> Why the first year of follow-up is so crowded
#   sit-second-opinion-en.html-> Asking for a second opinion, out loud
# The Chinese side needs none of this: its three pointers -- 〈晚期副作用什麼
# 時候來〉〈療程結束後，追蹤怎麼排〉〈想聽第二個意見，怎麼開口〉 -- already
# equal those pages' live <h1> exactly.
BODY_EDITS = {
    "zh": [],
    "en": [
        ("〈When do the late effects arrive〉",
         "〈The side effects that arrive years later〉"),
        ("〈How follow-up is scheduled once treatment ends〉",
         "〈Why the first year of follow-up is so crowded〉"),
        ("〈Asking for a second opinion〉",
         "〈Asking for a second opinion, out loud〉"),
    ],
}

# topics.html / topics-en.html cards, inserted after the bl one (the last
# card on the pulled topics pages, which carry 15 cards).
TOPIC_CARD_ZH = """  <a class="topiccard" href="th.html">
    <div class="k">THYROID CANCER</div>
    <div class="t">甲狀腺癌專題</div>
    <div class="d">這個病的讀者大多是在完全沒有不舒服的時候被告知得了癌症，所以第一個問號不是「我還能活多久」，而是「這到底算不算一回事」。這個問號會往兩個相反的方向出錯。這個專題的工作是把你放進正確的那一格，並且把那一格的代價講清楚，一個問題一篇。</div>
    <div class="steps"><span>確診與分期</span><span>低風險那一格</span><span>放射碘</span><span>追蹤與進階</span><span>另外兩個病與台灣</span></div>
    <div class="go"><span class="n">20 篇</span><span class="ar">進入專題 →</span></div>
  </a>
"""

TOPIC_CARD_EN = """  <a class="topiccard" href="th-en.html">
    <div class="k">THYROID CANCER</div>
    <div class="t">Thyroid Cancer Guide</div>
    <div class="d">Most people reading this were told they had cancer while feeling perfectly well, so the first question is not how long anyone has left — it is whether this counts as anything at all. That question goes wrong in two opposite directions. The work of this guide is to put you in the right box and to be honest about what that box costs, one question per article.</div>
    <div class="steps"><span>Diagnosis and staging</span><span>The low-risk box</span><span>Radioiodine</span><span>Follow-up and beyond</span><span>Two other diseases, and Taiwan</span></div>
    <div class="go"><span class="n">20 articles</span><span class="ar">Open the guide →</span></div>
  </a>
"""

# JSON-LD hasPart entries appended to the topics pages' CollectionPage.
HASPART_ZH = {"@type": "CollectionPage", "name": NAME_ZH,
              "url": "https://doremai2001.github.io/publicpage/th.html"}
HASPART_EN = {"@type": "CollectionPage", "name": NAME_EN,
              "url": "https://doremai2001.github.io/publicpage/th-en.html"}
