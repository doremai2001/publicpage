# -*- coding: utf-8 -*-
"""Liver-cancer topic module (Chinese side, plus the wiring to the English
one).

Like cx, the source files under /home/claude/liver already carry the lv-
prefix in their names.  The builder composes output names as
"<PREFIX>-<slug>.html", so the slugs here are the *unprefixed* tails and the
staging step (stage_liver_figs.py) copies each source to a stripped name —
that same step also inserts the article figures at the manifest's placement,
which the raw fragments deliberately do not contain.  Output names therefore
come out as lv-no-biopsy.html, never lv-lv-no-biopsy.html.

One deliberate irregularity: the hub pages are liver.html / liver-en.html
(not lv.html), while the articles keep the lv- prefix.  topicbuild's core is
not to be modified, so _hub_name is overridden here at import time — both the
builder and the verifier import this module and see the same names.

A disease topic, so the JSON-LD "about" entity is the topicbuild default,
MedicalCondition — no ABOUT_TYPE override.

cervix kept a redundant leads.json next to its meta; nothing in the build
ever read it (only meta/all.json), so liver has no leads file — the lead
lives in the meta files' "lead" field, which is what the builder uses.
"""

import json
import os

import liver_en
import topicbuild as _tb

_STAGE = ("/tmp/claude-0/-home-claude/4bc50b06-d4e4-5989-80b2-34f0f02eed26/"
          "scratchpad/staging-lv")

# ------------------------------------------------------------------ sources --
SRC = {
    "body_zh": os.path.join(_STAGE, "body"),
    "body_en": os.path.join(_STAGE, "en"),
    "meta_zh": ["/home/claude/liver/meta/%s.json" % g for g in "ABCD"],
    "meta_en": ["/home/claude/liver/meta/%s-en.json" % g for g in "ABCD"],
}

REPO = "/home/claude/repo"

# Existing hub pages the tag labels are harvested from, so no label is retyped.
TAG_SOURCES = {
    "zh": [os.path.join(REPO, n) for n in
           ("hn.html", "rc.html", "cc.html", "bc.html", "nt.html", "cx.html")],
    "en": [os.path.join(REPO, n) for n in
           ("hn-en.html", "rc-en.html", "cc-en.html", "bc-en.html",
            "nt-en.html", "cx-en.html")],
}

# ------------------------------------------------------------------ identity --
PREFIX = "lv"
KICKER = "LIVER CANCER"
NAME_ZH = "肝癌專題"
NAME_EN = "Liver Cancer Guide"
CONDITION_ZH = "肝癌"
CONDITION_EN = "Liver cancer"
DATE = "2026-08-30"

# ------------------------------------------------- hub naming (see docstring)
HUB_NAME = {"zh": "liver.html", "en": "liver-en.html"}
_orig_hub_name = _tb._hub_name


def _hub_name(prefix, lang):
    if prefix == PREFIX:
        return HUB_NAME[lang]
    return _orig_hub_name(prefix, lang)


_tb._hub_name = _hub_name

# staging / imaging / decision / surgery / followup / recurrence / nhi / prep
# / workflow / mdt / sideeffect / daily / qol / trial / nutrition / targeted /
# immuno / proton / cost all exist on the hn/rc/cc/bc/nt/cx hubs and are
# reused verbatim.  These five are new; English labels follow the existing
# hubs' convention (Title Case noun phrases, "&" where the zh label has 與).
LABEL_ADD = {
    "sbrt": ("立體定位放射", "SBRT"),
    "liverfunction": ("肝功能", "Liver Function"),
    "transplant": ("肝臟移植", "Liver Transplant"),
    "tace": ("栓塞與 Y-90", "TACE & Y-90"),
    "hepatitis": ("B 肝與 C 肝", "Hepatitis B & C"),
}

# ------------------------------------------------------------------ sections --
# Section titles verbatim from SPEC section 四; the four groups A-D keep the
# SPEC's per-group article order.
SECTIONS = [
    {
        "zh": "確診之後",
        "stepsub_zh": "為什麼常常不用切片、肝功能為什麼是貨幣、"
                      "分期表把你放在哪一格——確診後最先撞上的五題。",
        "slugs": ["no-biopsy", "two-diseases", "staging-bclc", "hepatitis",
                  "first-month"],
    },
    {
        "zh": "治療怎麼決定",
        "stepsub_zh": "開刀、燒灼、放射、換肝、栓塞——幾條路怎麼分工，"
                      "這五篇是你真正握有發言權的地方。",
        "slugs": ["three-roads", "sbrt", "proton", "transplant", "tace-y90"],
    },
    {
        "zh": "療程中的照護",
        "stepsub_zh": "SBRT 的兩週、標靶與免疫的日子、TACE 前後那幾天，"
                      "以及哪些狀況要當天回醫院。",
        "slugs": ["sbrt-weeks", "warning-signs", "systemic-days", "nutrition",
                  "tace-days"],
    },
    {
        "zh": "結束之後",
        "stepsub_zh": "追蹤怎麼排、復發之後的路、肝要顧一輩子、"
                      "換肝之後，以及在等待名單上的日子。",
        "slugs": ["followup", "recurrence", "liver-care", "post-transplant",
                  "bridging"],
    },
]

TAGS = {
    "no-biopsy": ["imaging", "staging", "decision"],
    "two-diseases": ["liverfunction", "staging", "decision"],
    "staging-bclc": ["staging", "decision", "mdt"],
    "hepatitis": ["hepatitis", "nhi", "daily"],
    "first-month": ["prep", "workflow", "mdt", "nhi"],
    "three-roads": ["decision", "surgery", "sbrt", "nhi"],
    "sbrt": ["sbrt", "decision", "liverfunction"],
    "proton": ["proton", "sbrt", "cost", "trial"],
    "transplant": ["transplant", "decision", "surgery"],
    "tace-y90": ["tace", "decision", "nhi"],
    "sbrt-weeks": ["sbrt", "workflow", "daily"],
    "warning-signs": ["sideeffect", "daily", "liverfunction"],
    "systemic-days": ["targeted", "immuno", "sideeffect", "nhi"],
    "nutrition": ["nutrition", "liverfunction", "daily"],
    "tace-days": ["tace", "sideeffect", "daily"],
    "followup": ["followup", "imaging", "workflow"],
    "recurrence": ["recurrence", "decision", "sbrt"],
    "liver-care": ["liverfunction", "hepatitis", "daily", "qol"],
    "post-transplant": ["transplant", "followup", "qol"],
    "bridging": ["transplant", "sbrt", "tace", "workflow"],
}

# ---------------------------------------------------------- article metadata --
_ZH = {}
for _p in SRC["meta_zh"]:
    with open(_p, encoding="utf-8") as _fh:
        _ZH.update(json.load(_fh))

ART = {}
for _slug, _tags in TAGS.items():
    _m = dict(_ZH["lv-" + _slug])
    _m["tags"] = _tags
    ART[_slug] = _m

EN = liver_en.EN
SECTIONS_EN = liver_en.SECTIONS_EN
HUB_EN = liver_en.HUB

# ----------------------------------------------------------------- hub copy --
HUB = {
    "title": "肝癌專題｜不用切片的確診、肝癌與肝硬化、開刀燒灼放射怎麼選、"
             "換肝與 TACE、SBRT 與質子｜吳正友醫師",
    "desc": "肝癌病人最需要知道的 20 件事：為什麼常常不用切片就確診、"
            "你同時有兩個病（肝癌與肝硬化）、BCLC 分期表把你放在哪一格、"
            "B 肝 C 肝的抗病毒藥、確診後第一個月、小顆肝癌的三條路、"
            "SBRT 為什麼行什麼時候不行、質子治療的升級理由與試驗現況、"
            "換肝、TACE 與 Y-90、SBRT 的兩週實際長怎樣、"
            "哪些狀況要當天回醫院、標靶與免疫治療的日子、白蛋白肌肉與飲食、"
            "TACE 前後那幾天、追蹤與 AFP、復發之後的路、肝要顧一輩子、"
            "換肝之後的日子，以及在等待名單上的日子。每篇附原始文獻連結。",
    "sub": "從確診那一天，到治療結束好幾年——一個問題一篇。",
    "intro": "肝癌和多數癌症最不一樣的地方，是你通常同時有兩個病：肝癌，"
             "和它腳下的肝硬化——治療的每一步都要用肝功能付帳。"
             "這 20 篇照著你真正會走過的順序排：確診之後、治療怎麼決定、"
             "療程中的照護，最後是結束之後。先說我的位置："
             "肝癌的立體定位放射治療與質子治療是我自己每天在做、"
             "而且多數要自費的治療，這個專題比較的另一邊是別科同事的手術和燒灼，"
             "所以關於放射的每一句話，我寫得比別人更保守——"
             "開得了刀、肝功能好的病人，切除仍然是預設。"
             "每一篇都附上原始文獻連結，證據弱的地方我會直接說弱。",
    "closing": "以上為一般性衛教說明，不能取代面對面的診療。"
               "肝癌的治療同時取決於腫瘤條件與肝功能，"
               "同一個期別在不同人身上會導向不同建議，"
               "實際治療請與你的主治醫師和多專科團隊討論。",
}

# No cross-topic sentence rewrites: the lv fragments' only relative links
# point at nt-proton(-en).html and insight-proton(-en).html, which exist on
# the site under exactly those names.
BODY_EDITS = {"zh": [], "en": []}

# topics.html / topics-en.html cards, inserted after the cervical-cancer one.
TOPIC_CARD_ZH = """  <a class="topiccard" href="liver.html">
    <div class="k">LIVER CANCER</div>
    <div class="t">肝癌專題</div>
    <div class="d">你同時有兩個病：肝癌與肝硬化——為什麼常常不用切片、開刀燒灼放射怎麼分工、換肝與等待名單，從確診到治療結束好幾年，一個問題一篇。</div>
    <div class="steps"><span>確診之後</span><span>治療怎麼決定</span><span>療程中的照護</span><span>結束之後</span></div>
    <div class="go"><span class="n">20 篇</span><span class="ar">進入專題 →</span></div>
  </a>
"""

TOPIC_CARD_EN = """  <a class="topiccard" href="liver-en.html">
    <div class="k">LIVER CANCER</div>
    <div class="t">Liver Cancer Guide</div>
    <div class="d">You have two diseases at once: the cancer and the cirrhosis — why a biopsy is often unnecessary, how surgery, ablation and radiation divide the work, transplant and the waiting list. From diagnosis to years after treatment ends, one question per article.</div>
    <div class="steps"><span>After the Diagnosis</span><span>How Treatment Is Decided</span><span>During Treatment</span><span>After Treatment</span></div>
    <div class="go"><span class="n">20 articles</span><span class="ar">Open the guide →</span></div>
  </a>
"""

# JSON-LD hasPart entries appended to the topics pages' CollectionPage.
HASPART_ZH = {"@type": "CollectionPage", "name": NAME_ZH,
              "url": "https://doremai2001.github.io/publicpage/liver.html"}
HASPART_EN = {"@type": "CollectionPage", "name": NAME_EN,
              "url": "https://doremai2001.github.io/publicpage/liver-en.html"}
