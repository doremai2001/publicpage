# -*- coding: utf-8 -*-
"""Endometrial-cancer topic module (Chinese side, plus the wiring to the
English one).

Naming: hub em.html / em-en.html, articles em-<slug>.html -- the hub shares
the prefix exactly as ec / cx / pel do, so topicbuild's own _hub_name gives
"em.html" / "em-en.html" and there is NO monkeypatch here (liver and gbm
needed one; em does not).  Checked before writing this module:
topicbuild._hub_name("em", "zh") == "em.html".

The source fragments under /home/claude/endo/body and /home/claude/endo/en
already carry the em- prefix (and the English ones do NOT carry a -en
suffix); stage_endo_figs.py strips the prefix and inserts the eleven figures,
so the builder's "<PREFIX>-<slug>.html" never comes out as em-em-*.  SLUGS
below are therefore the unprefixed tails.

Article metadata: meta/{A,B,C,D}.json are keyed "em-<slug>"; _ZH is re-keyed
on the tail.  Nothing is retyped -- the titles in those files are already
SPEC.md 修正 16's canonical set.

A disease topic, so the JSON-LD "about" entity is the topicbuild default,
MedicalCondition -- no ABOUT_TYPE override.

The conflict-of-interest paragraph (SPEC section 二) sits before the first
<h4> of exactly four articles -- B1 adjuvant, B2 vaginal-brachy,
B3 chemo-rt, B4 molecular-adjuvant -- and nowhere else; verify_endo pins that.
"""

import json
import os

import endo_en

_STAGE = "/home/claude/endo/staging"

# ------------------------------------------------------------------ sources --
SRC = {
    "body_zh": os.path.join(_STAGE, "body"),
    "body_en": os.path.join(_STAGE, "en"),
    "meta_zh": ["/home/claude/endo/meta/%s.json" % g for g in "ABCD"],
    "meta_en": ["/home/claude/endo/meta/%s-en.json" % g for g in "ABCD"],
}

REPO = "/home/claude/repo"

# Existing hub pages the tag labels are harvested from, so no label is
# retyped.  cx for brachy/menopause/fertility/sexual, bc for
# genetic/lymphedema/bone/endocrine, gbm for molecular, lc for prevention,
# nt for evidence/cost, liver for followup/recurrence/trial, pc for recovery.
TAG_SOURCES = {
    "zh": [os.path.join(REPO, n) for n in
           ("hn.html", "rc.html", "cc.html", "bc.html", "nt.html", "cx.html",
            "liver.html", "brt.html", "pel.html", "ec.html", "gbm.html",
            "pc.html", "lc.html")],
    "en": [os.path.join(REPO, n) for n in
           ("hn-en.html", "rc-en.html", "cc-en.html", "bc-en.html",
            "nt-en.html", "cx-en.html", "liver-en.html", "brt-en.html",
            "pel-en.html", "ec-en.html", "gbm-en.html", "pc-en.html",
            "lc-en.html")],
}

# ------------------------------------------------------------------ identity --
PREFIX = "em"
KICKER = "ENDOMETRIAL CANCER"
NAME_ZH = "子宮內膜癌專題"
NAME_EN = "Endometrial Cancer Guide"
CONDITION_ZH = "子宮內膜癌"
CONDITION_EN = "Endometrial cancer"
DATE = "2026-09-10"

# staging / decision / imaging / evidence / molecular / surgery / brachy /
# workflow / sexual / chemo / immuno / biomarker / nhi / trial / fertility /
# endocrine / nutrition / exercise / prevention / genetic / screening /
# menopause / bone / followup / recurrence / lymphedema / recovery / daily /
# survivor / work / qol / sideeffect all exist on the harvested hubs and are
# reused verbatim.  These three are new; English labels follow the existing
# hubs' convention (Title Case noun phrases, British spelling).
LABEL_ADD = {
    "bleeding": ("異常出血", "Abnormal Bleeding"),
    "hysterectomy": ("子宮切除", "Hysterectomy"),
    "sentinel": ("前哨淋巴結", "Sentinel Node"),
}

# ------------------------------------------------------------------ sections --
# Group titles and per-group order verbatim from SPEC section 五 (4/5/4/4).
SECTIONS = [
    {
        "zh": "確診與分期",
        "stepsub_zh": "停經後出血為什麼不能等、兩種內膜癌怎麼變成四型、"
                      "FIGO 2023 改掉的是描述而不是治療，"
                      "以及手術會拿掉什麼、淋巴結怎麼處理。",
        "slugs": ["bleeding", "two-kinds", "staging-2023", "surgery"],
    },
    {
        "zh": "治療與實證",
        "stepsub_zh": "開完刀還要不要照放療、只照陰道的那一種是什麼、"
                      "加化療換到什麼又付出什麼、分子分型正在怎麼改掉這些決定，"
                      "以及免疫治療到底誰真的有效。",
        "slugs": ["adjuvant", "vaginal-brachy", "chemo-rt",
                  "molecular-adjuvant", "immuno"],
    },
    {
        "zh": "特殊處境",
        "stepsub_zh": "想留住子宮生小孩的條件有多嚴、體重與糖尿病到底解釋了多少、"
                      "Lynch 驗出來會怎樣，以及治療結束後的荷爾蒙那一題。",
        "slugs": ["fertility", "obesity", "lynch", "hormone-after"],
    },
    {
        "zh": "之後",
        "stepsub_zh": "追蹤怎麼排、它能做到什麼做不到什麼，復發之後還救不救得回來，"
                      "下肢水腫怎麼防怎麼處理，以及日子怎麼過回去。",
        "slugs": ["followup", "recurrence", "lymphedema", "daily"],
    },
]

TAGS = {
    "bleeding": ["bleeding", "imaging", "staging", "decision"],
    "two-kinds": ["molecular", "staging", "evidence", "decision"],
    "staging-2023": ["staging", "evidence", "molecular", "decision"],
    "surgery": ["hysterectomy", "surgery", "sentinel", "staging"],
    "adjuvant": ["evidence", "decision", "sideeffect", "staging"],
    "vaginal-brachy": ["brachy", "workflow", "sideeffect", "sexual"],
    "chemo-rt": ["chemo", "evidence", "sideeffect", "decision"],
    "molecular-adjuvant": ["molecular", "evidence", "decision", "trial"],
    "immuno": ["immuno", "biomarker", "nhi", "evidence"],
    "fertility": ["fertility", "endocrine", "decision", "evidence"],
    "obesity": ["nutrition", "exercise", "prevention", "evidence"],
    "lynch": ["genetic", "screening", "molecular", "decision"],
    "hormone-after": ["menopause", "endocrine", "sexual", "bone"],
    "followup": ["followup", "imaging", "recurrence", "evidence"],
    "recurrence": ["recurrence", "decision", "brachy", "trial"],
    "lymphedema": ["lymphedema", "sideeffect", "recovery", "daily"],
    "daily": ["survivor", "exercise", "work", "qol"],
}

# ---------------------------------------------------------- article metadata --
_ZH = {}
for _p in SRC["meta_zh"]:
    with open(_p, encoding="utf-8") as _fh:
        for _k, _rec in json.load(_fh).items():
            _ZH[_k[len("em-"):]] = _rec

ART = {}
for _slug, _tags in TAGS.items():
    _m = dict(_ZH[_slug])
    _m["tags"] = _tags
    ART[_slug] = _m

EN = endo_en.EN
SECTIONS_EN = endo_en.SECTIONS_EN
HUB_EN = endo_en.HUB

# ----------------------------------------------------------------- hub copy --
HUB = {
    "title": "子宮內膜癌專題｜停經後出血、四型分子分類、FIGO 2023、"
             "開完刀還要不要放療、陰道近接、化療與免疫、保留子宮與之後的日子"
             "｜吳正友醫師",
    "desc": "子宮內膜癌病人最需要知道的 17 件事：停經後出血為什麼查一次就有答案、"
            "兩種內膜癌怎麼變成四型、FIGO 2023 改掉的是描述不是治療、"
            "手術拿掉什麼淋巴結怎麼處理、開完刀還要不要做放療與 PORTEC-1 的三句話、"
            "陰道近接治療實際上會發生什麼、加化療換到什麼又付出什麼、"
            "分子分型會怎麼改掉你的治療、免疫治療依 MMR 狀態誰真的有效、"
            "想保留子宮生小孩的條件有多嚴、體重與糖尿病解釋了多少又沒解釋什麼、"
            "Lynch 症候群驗出來會怎樣、治療結束後的荷爾蒙問題、追蹤怎麼排、"
            "復發之後還救不救得回來、下肢淋巴水腫怎麼防怎麼處理，"
            "以及治療結束之後的日常。每篇附原始文獻連結。",
    "sub": "從病理報告那一天，到治療結束好幾年——一個問題一篇。",
    "intro": "這是全站少數「大多數人會好」的癌別，這件事要寫清楚；"
             "但它不能變成「所以怎麼做都差不多」。這個病最大的兩個傷害來源，"
             "一邊是低風險的人被照了換不到存活的骨盆腔放療"
             "（PORTEC-1 的併發症 25% 對 6%），一邊是出血拖了半年才來。"
             "這 17 篇照著你真正會走過的順序排：確診與分期、治療與實證、"
             "特殊處境，最後是之後。先說我的位置：陰道近接治療和骨盆腔放療，"
             "是我自己每週在做的那一段；這個專題比較的另一邊，"
             "是婦癌科同事的刀和婦癌科、腫瘤內科同事的藥——"
             "所以拿放療去比手術和藥的那四篇，開頭都有同一段利益揭露，"
             "每一個比較都附上原始文獻，讓你可以拿著它回婦癌科門診聽第二意見。"
             "還有一件事跟別的癌別相反：這個病大多數人是先開刀、再決定要不要放療化療，"
             "所以真正的決策時刻，是你拿到病理報告的那一天。"
             "證據弱的地方我會直接說弱，數字查不到的地方我會說查不到。",
    "closing": "以上為一般性衛教說明，不能取代面對面的診療。"
               "子宮內膜癌的治療同時取決於組織型態、分化度、期別、分子分型"
               "與手術發現，同一個期別在不同人身上會導向不同建議，"
               "實際治療請與你的婦癌科主治醫師和多專科團隊討論。",
}

# No cross-topic sentence rewrites: the em fragments carry no relative links
# at all (every in-topic and on-site cross-reference is an unlinked title, as
# SPEC-EN section 3 prescribes), so there is nothing to rewrite at build time.
BODY_EDITS = {"zh": [], "en": []}

# topics.html / topics-en.html cards, inserted after the gbm one (the last
# card on the pulled topics pages, which carry 12 cards).
TOPIC_CARD_ZH = """  <a class="topiccard" href="em.html">
    <div class="k">ENDOMETRIAL CANCER</div>
    <div class="t">子宮內膜癌專題</div>
    <div class="d">大多數人會好，但那不等於怎麼做都差不多——停經後出血為什麼查一次就有答案、開完刀還要不要照放療、分子分型正在怎麼改掉這個決定、想留住子宮生小孩的條件有多嚴，從病理報告到治療結束好幾年，一個問題一篇。</div>
    <div class="steps"><span>確診與分期</span><span>治療與實證</span><span>特殊處境</span><span>之後</span></div>
    <div class="go"><span class="n">17 篇</span><span class="ar">進入專題 →</span></div>
  </a>
"""

TOPIC_CARD_EN = """  <a class="topiccard" href="em-en.html">
    <div class="k">ENDOMETRIAL CANCER</div>
    <div class="t">Endometrial Cancer Guide</div>
    <div class="d">Most people will be well, and that is not the same as it hardly mattering what you do — why bleeding after the menopause is settled by a single test, whether radiotherapy is still needed after the operation, how molecular classification is changing that decision, and what it takes to keep the uterus and have a child. From the pathology report to years after treatment, one question per article.</div>
    <div class="steps"><span>Diagnosis and staging</span><span>Treatment and the evidence</span><span>Special situations</span><span>After treatment</span></div>
    <div class="go"><span class="n">17 articles</span><span class="ar">Open the guide →</span></div>
  </a>
"""

# JSON-LD hasPart entries appended to the topics pages' CollectionPage.
HASPART_ZH = {"@type": "CollectionPage", "name": NAME_ZH,
              "url": "https://doremai2001.github.io/publicpage/em.html"}
HASPART_EN = {"@type": "CollectionPage", "name": NAME_EN,
              "url": "https://doremai2001.github.io/publicpage/em-en.html"}

# ------------------------------------------------------- 修正 20 build chore --
# SPEC.md 修正 20: pel-who(-en).html says the endometrial-cancer topic is
# "being planned".  The SPEC enumerates four spots, but those four are the two
# asymmetric halves of three mirrored pairs -- body sentence, figure alt,
# closing note -- so fixing only four would leave the zh and en versions of
# the alt and of the closing note disagreeing.  All six are rewritten: three
# per file, one per mirrored pair.
#
# Two rules hold throughout:
#   * the bladder-cancer half stays byte-identical in BOTH languages (that
#     topic really is still unwritten);
#   * NO <a> is added.  pel-who's body carries no in-body site links at all;
#     every pointer on that page is an unlinked 〈title〉 (zh) or "title" (en),
#     and 修正 20's "指向 em.html" means pointing in sense, not in markup.
# verify_endo pins the diff to exactly these six substitutions.
PEL_WHO_EDITS = {
    "pel-who.html": [
        (
            "子宮內膜癌另有專題規劃中。</p>",
            "這三個試驗各自的細節、以及分子分型正在怎麼改掉這一格，"
            "都在〈子宮內膜癌專題〉。</p>",
        ),
        (
            "照的範圍不同，鄰居就不同；子宮內膜癌另有專題規劃中。",
            "照的範圍不同，鄰居就不同；子宮內膜癌另有專題。",
        ),
        (
            "你那一格的細節我都指到既有專題去了，膀胱癌與子宮內膜癌兩篇還在規劃中。",
            "你那一格的細節我都指到既有專題去了，子宮內膜癌現在也有自己的專題，"
            "膀胱癌那一篇還在規劃中。",
        ),
    ],
    "pel-who-en.html": [
        (
            "A separate endometrial cancer topic is being planned.</p>",
            "The detail of each of those three trials, and how molecular "
            "classification is changing this cell, is in \"Endometrial "
            "Cancer Guide\".</p>",
        ),
        (
            "change the extent and the neighbours change; a separate series "
            "is planned.",
            "change the extent and the neighbours change; a separate series "
            "on endometrial cancer already exists.",
        ),
        (
            "the topic that already covers it; the bladder cancer and "
            "endometrial cancer topics are still being planned.",
            "the topic that already covers it; endometrial cancer now has a "
            "topic of its own, and the bladder cancer topic is still being "
            "planned.",
        ),
    ],
}
