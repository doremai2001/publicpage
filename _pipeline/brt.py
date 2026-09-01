# -*- coding: utf-8 -*-
"""Breast-radiotherapy topic module (Chinese side; the English wiring is
present but switched off for round 1).

ZH_ONLY is the round switch.  While True (round 1) the builder wrote the ten
Chinese articles plus brt.html, left the hreflang block / the English
canonical partner / the language-switch chip out of every page, patched
topics.html only, and added eleven sitemap URLs.  Round 2 sets it False: all
22 pages are rewritten -- the ten Chinese ones and brt.html regain hreflang
and the language switch, and are otherwise byte-identical to what is already
published -- topics-en.html gets its card, and eleven more sitemap URLs are
appended.

ROUND 2 IS ACTIVE (ZH_ONLY = False).  Round 1 is live as commits 4949329 and
9b9c5f6, so the build/verify baseline is the git HEAD blob of each file, not a
scratch snapshot: verify check 13 diffs every regenerated Chinese page against
its published version and requires the difference to be confined to the
hreflang / language-switch lines.  Two Chinese sources were corrected between
the rounds (brt-tomo's NHI attribution sentence per FIXES F10, and
RadComp -> RADCOMP in brt-technique-map), so those two pages carry an expected
body diff as well; they are declared in verify_brt.EXPECTED_BODY_DIFF and
printed in full rather than waved through.

Naming: the hub is brt.html / brt-en.html and the articles are brt-<slug>.html,
i.e. the hub shares the prefix exactly as cx / hn / bc do, so topicbuild's own
_hub_name is correct and there is NO monkeypatch here (liver needed one only
because its hub was liver.html while its articles were lv-*).

The source fragments under /home/claude/brt/body already carry the brt-
prefix; stage_brt_figs.py strips it (and inserts the figures) so the builder's
"<PREFIX>-<slug>.html" never comes out as brt-brt-*.

A treatment topic for a disease, so the JSON-LD "about" entity stays
topicbuild's default MedicalCondition, named 乳癌 / Breast cancer -- no
ABOUT_TYPE override.

Article titles come from meta/{A,B,C}.json.  SPEC section 四's list headings
are working code names and were superseded (see the ruling at the top of
FIXES.md); nothing here may retype them.
"""

import json
import os

import brt_en

# ------------------------------------------------------------------ switch --
ZH_ONLY = False

_STAGE = ("/tmp/claude-0/-home-claude/4bc50b06-d4e4-5989-80b2-34f0f02eed26/"
          "scratchpad/staging-brt")

# ------------------------------------------------------------------ sources --
SRC = {
    "body_zh": os.path.join(_STAGE, "body"),
    "body_en": os.path.join(_STAGE, "en"),
    "meta_zh": ["/home/claude/brt/meta/%s.json" % g for g in "ABC"],
    "meta_en": ["/home/claude/brt/meta/%s-en.json" % g for g in "ABC"],
}

REPO = "/home/claude/repo"

# Existing hub pages the tag labels are harvested from, so no label is
# retyped.  lc is in the list for the pneumonitis label (C3); the rest match
# liver's list.
TAG_SOURCES = {
    "zh": [os.path.join(REPO, n) for n in
           ("hn.html", "rc.html", "cc.html", "bc.html", "nt.html", "cx.html",
            "lc.html")],
    "en": [os.path.join(REPO, n) for n in
           ("hn-en.html", "rc-en.html", "cc-en.html", "bc-en.html",
            "nt-en.html", "cx-en.html", "lc-en.html")],
}

# ------------------------------------------------------------------ identity --
PREFIX = "brt"
KICKER = "BREAST RADIOTHERAPY"
NAME_ZH = "乳房放射治療專題"
NAME_EN = "Breast Radiotherapy Guide"
CONDITION_ZH = "乳癌"
CONDITION_EN = "Breast cancer"
DATE = "2026-08-31"

# decision / staging / surgery / nhi / hypofx / evidence / cost / proton /
# trial / prep / workflow / daily / skin / sideeffect / pneumonitis /
# lymphedema / lateeffect / survivor / followup / imaging all exist on the
# hn/rc/cc/bc/nt/cx/lc hubs and are reused verbatim.  These four are new;
# English labels follow the existing hubs' convention (Title Case noun
# phrases, the abbreviation kept where the zh label keeps it).
LABEL_ADD = {
    "imrt": ("強度調控放療", "IMRT"),
    "tomo": ("螺旋斷層治療", "TomoTherapy"),
    "dibh": ("深吸氣閉氣", "Breath-Hold"),
    "heart": ("心臟劑量", "Heart Dose"),
}

# ------------------------------------------------------------------ sections --
# Section titles verbatim from SPEC section 四; the three groups A-C keep the
# SPEC's per-group article order (A1-A3, B1-B3, C1-C4).
SECTIONS = [
    {
        "zh": "為什麼照、怎麼決定",
        "stepsub_zh": "手術型式與淋巴結顆數把你放在哪一格、"
                      "為什麼你的次數和別人不一樣、"
                      "還有那幾個技術名詞各自管什麼。",
        "slugs": ["who-needs", "fractionation", "technique-map"],
    },
    {
        "zh": "技術怎麼選",
        "stepsub_zh": "左側的心臟劑量是這一組的核心；"
                      "TOMO 與質子各自的證據走到哪一格、"
                      "哪些情境差得出來、哪些差不出來。",
        "slugs": ["heart", "tomo", "proton"],
    },
    {
        "zh": "療程與自我照顧",
        "stepsub_zh": "定位那天到第一次治療、皮膚什麼時候開始反應、"
                      "皮膚以外還有什麼，以及療程結束之後的那幾年。",
        "slugs": ["sim-to-first", "skin", "beyond-skin", "after"],
    },
]

TAGS = {
    "who-needs": ["decision", "staging", "surgery", "nhi"],
    "fractionation": ["hypofx", "decision", "evidence", "nhi"],
    "technique-map": ["imrt", "tomo", "proton", "dibh", "decision"],
    "heart": ["heart", "dibh", "evidence", "cost"],
    "tomo": ["tomo", "imrt", "cost", "nhi"],
    "proton": ["proton", "heart", "trial", "cost"],
    "sim-to-first": ["prep", "workflow", "dibh", "daily"],
    "skin": ["skin", "sideeffect", "daily"],
    "beyond-skin": ["pneumonitis", "sideeffect", "lymphedema", "lateeffect"],
    "after": ["followup", "lateeffect", "survivor", "imaging"],
}

# ---------------------------------------------------------- article metadata --
_ZH = {}
for _p in SRC["meta_zh"]:
    with open(_p, encoding="utf-8") as _fh:
        _ZH.update(json.load(_fh))

ART = {}
for _slug, _tags in TAGS.items():
    _m = dict(_ZH["brt-" + _slug])
    _m["tags"] = _tags
    ART[_slug] = _m

EN = brt_en.EN
SECTIONS_EN = brt_en.SECTIONS_EN
HUB_EN = brt_en.HUB

# ----------------------------------------------------------------- hub copy --
HUB = {
    "title": "乳房放射治療專題｜誰需要照、幾次、IMRT 與 TOMO 與質子、"
             "心臟劑量與深吸氣閉氣、皮膚照護與結束之後｜吳正友醫師",
    "desc": "已經被告知要做放射治療的乳癌病人最常問的 10 件事："
            "手術型式與淋巴結顆數把你放在哪一格、為什麼我不是低分次、"
            "IMRT 與 TOMO 與質子和深吸氣閉氣各自管什麼、"
            "左側的心臟劑量怎麼看、TOMO 與一般 IMRT 差在哪、"
            "質子在乳房的證據走到哪一格、定位到第一次治療會發生什麼、"
            "皮膚反應什麼時候來怎麼顧、皮膚以外的疲倦與肺與淋巴水腫、"
            "以及結束之後的恢復與長期追蹤。每篇附原始文獻連結與證據等級。",
    "sub": "已經確定要照了，接下來的問題是怎麼照——一個問題一篇。",
    "intro": "這個專題的讀者，是已經被告知要做放射治療的乳癌病人。"
             "要不要照、範圍多大、能不能省略，那些是乳癌專題的題目；"
             "這裡處理的是怎麼照、用什麼技術、怎麼過這五到六週、"
             "以及自己能做什麼。寫的時候有幾條規矩："
             "「劑量學上比較好」和「臨床結果證實比較好」永遠分開寫、"
             "不互相冒充；每個數字帶上族群、側別與技術的標籤；"
             "深吸氣閉氣是姿勢不是機器，可以疊在任何光子技術上，"
             "所以技術的選擇寫成適應症的問題，不是預算的問題。"
             "這個專題比較的技術裡，比較貴的幾種有自費成分、"
             "而且是我自己科裡執行的項目，所以每一篇開頭都有同一段利益揭露；"
             "費用的部分，查得到官方公告就引，查不到就寫請問醫務課。"
             "每一篇都附上原始文獻連結，證據弱的地方我會直接說弱。",
    "closing": "以上為一般性衛教說明，不能取代面對面的診療。"
               "放射治療的範圍、次數與技術同時取決於手術型式、病理報告與"
               "全身治療計畫，同一個期別在不同人身上會導向不同建議，"
               "實際治療請與你的主治醫師和多專科團隊討論。",
}

# No cross-topic sentence rewrites: the only relative links in the brt
# fragments point at nt-proton.html and insight-proton.html, which exist on
# the site under exactly those names.
BODY_EDITS = {"zh": [], "en": []}

# topics.html card, inserted after the liver one (the last card before brt).
# Already published in round 1, so round 2's patcher finds it in place and
# leaves topics.html untouched.
TOPIC_CARD_ZH = """  <a class="topiccard" href="brt.html">
    <div class="k">BREAST RADIOTHERAPY</div>
    <div class="t">乳房放射治療專題</div>
    <div class="d">已經確定要照了，接下來是怎麼照：誰需要照、幾次、IMRT 與 TOMO 與質子差在哪、左側的心臟劑量、皮膚怎麼顧，以及結束之後的那幾年。</div>
    <div class="steps"><span>為什麼照、怎麼決定</span><span>技術怎麼選</span><span>療程與自我照顧</span></div>
    <div class="go"><span class="n">10 篇</span><span class="ar">進入專題 →</span></div>
  </a>
"""

# The topics-en.html card, inserted after the liver-en one.  Untouched in
# round 1 (brt-en.html did not exist yet); added in round 2.
TOPIC_CARD_EN = """  <a class="topiccard" href="brt-en.html">
    <div class="k">BREAST RADIOTHERAPY</div>
    <div class="t">Breast Radiotherapy Guide</div>
    <div class="d">The decision to irradiate has been made; what follows is how. Who needs it, how many treatments, what IMRT, TomoTherapy and protons each do, heart dose on the left side, skin care, and the years after treatment ends.</div>
    <div class="steps"><span>Why, and How It Is Decided</span><span>Choosing the Technique</span><span>Treatment and Self-Care</span></div>
    <div class="go"><span class="n">10 articles</span><span class="ar">Open the guide →</span></div>
  </a>
"""

# JSON-LD hasPart entries appended to the topics pages' CollectionPage.
HASPART_ZH = {"@type": "CollectionPage", "name": NAME_ZH,
              "url": "https://doremai2001.github.io/publicpage/brt.html"}
HASPART_EN = {"@type": "CollectionPage", "name": NAME_EN,
              "url": "https://doremai2001.github.io/publicpage/brt-en.html"}
