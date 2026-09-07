# -*- coding: utf-8 -*-
"""Glioblastoma topic module (Chinese side, plus the wiring to the English
one).

Naming: the articles are gb-<slug>.html, but the hub is gbm.html /
gbm-en.html -- the same irregularity liver has (hub liver.html, articles
lv-*).  topicbuild's core is not to be modified, so _hub_name is overridden
here at import time; the builder and the verifier both import this module and
therefore see the same names.  PREFIX stays "gb" so the article file names,
the backlink hrefs and the tag-chip hrefs all come out right.

The source fragments under /home/claude/gbm/body already carry the gb-
prefix; stage_gbm_figs.py strips it (and inserts the eight figures) so the
builder's "<PREFIX>-<slug>.html" never comes out as gb-gb-*.  The slugs below
are therefore the unprefixed tails.

Article metadata: meta/{A,B,C,D}.json are keyed "gb-<slug>"; _ZH is re-keyed
on the tail.  Nothing is retyped.

A disease topic, so the JSON-LD "about" entity is the topicbuild default,
MedicalCondition -- no ABOUT_TYPE override.

The conflict-of-interest paragraph (SPEC section 二) sits before the first
<h4> of exactly four articles -- A3 surgery, B1 standard, B4 numbers,
B5 newthings -- and nowhere else; verify_gbm pins that.
"""

import json
import os

import gbm_en
import topicbuild as _tb

_STAGE = "/home/claude/gbm/staging"

# ------------------------------------------------------------------ sources --
SRC = {
    "body_zh": os.path.join(_STAGE, "body"),
    "body_en": os.path.join(_STAGE, "en"),
    "meta_zh": ["/home/claude/gbm/meta/%s.json" % g for g in "ABCD"],
    "meta_en": ["/home/claude/gbm/meta/%s-en.json" % g for g in "ABCD"],
}

REPO = "/home/claude/repo"

# Existing hub pages the tag labels are harvested from, so no label is
# retyped.  hn for prep/workflow/caregiver, nt for evidence/cost/bnct/proton,
# brt for imrt, pel for emergency, liver for followup/recurrence/trial,
# ec for the newest additions.
TAG_SOURCES = {
    "zh": [os.path.join(REPO, n) for n in
           ("hn.html", "rc.html", "cc.html", "bc.html", "nt.html", "cx.html",
            "liver.html", "brt.html", "pel.html", "ec.html")],
    "en": [os.path.join(REPO, n) for n in
           ("hn-en.html", "rc-en.html", "cc-en.html", "bc-en.html",
            "nt-en.html", "cx-en.html", "liver-en.html", "brt-en.html",
            "pel-en.html", "ec-en.html")],
}

# ------------------------------------------------------------------ identity --
PREFIX = "gb"
KICKER = "GLIOBLASTOMA"
NAME_ZH = "膠質母細胞瘤專題"
NAME_EN = "Glioblastoma Guide"
CONDITION_ZH = "膠質母細胞瘤"
CONDITION_EN = "Glioblastoma"
DATE = "2026-09-07"

# ------------------------------------------- hub naming (see the docstring) --
HUB_NAME = {"zh": "gbm.html", "en": "gbm-en.html"}
_orig_hub_name = _tb._hub_name


def _hub_name(prefix, lang):
    if prefix == PREFIX:
        return HUB_NAME[lang]
    return _orig_hub_name(prefix, lang)


_tb._hub_name = _hub_name

# staging / decision / imaging / workflow / evidence / biomarker / chemo /
# targeted / trial / cost / proton / hypofx / imrt / sideeffect / daily /
# work / prep / mdt / caregiver / emergency / lateeffect / qol / followup /
# recurrence all exist on the harvested hubs and are reused verbatim.  These
# five are new; English labels follow the existing hubs' convention (Title
# Case noun phrases).
LABEL_ADD = {
    "neurosurgery": ("神經外科", "Neurosurgery"),
    "seizure": ("癲癇", "Seizures"),
    "steroid": ("類固醇", "Steroids"),
    "cognition": ("認知", "Cognition"),
    "molecular": ("分子檢測", "Molecular Testing"),
}

# ------------------------------------------------------------------ sections --
# Group titles and per-group order verbatim from SPEC section 五 (5/5/4/3).
SECTIONS = [
    {
        "zh": "確診與分類",
        "stepsub_zh": "報告上那一行字是怎麼被寫出來的、頭幾天的每一件事各有"
                      "順序、開刀「全部拿掉」到底指什麼、那兩週的報告在等什麼，"
                      "以及 IDH-mutant 走的是另一條路。",
        "slugs": ["what-it-is", "first-days", "surgery", "pathology",
                  "lowgrade"],
    },
    {
        "zh": "治療與實證",
        "stepsub_zh": "同步的六週和維持的六個療程怎麼吃、MGMT 那一行決定什麼、"
                      "什麼情況可以縮短、那個數字要怎麼讀，"
                      "以及五種新療法各走到哪一格。",
        "slugs": ["standard", "mgmt", "elderly", "numbers", "newthings"],
    },
    {
        "zh": "療程中的照護",
        "stepsub_zh": "放療那六週實際長什麼樣、類固醇為什麼要慢慢減、"
                      "癲癇藥與開車這件事，以及哪些狀況不能等到下次門診。",
        "slugs": ["rt-weeks", "steroid", "seizure", "warning-signs"],
    },
    {
        "zh": "之後",
        "stepsub_zh": "追蹤片子怎麼排、變大不一定是惡化、"
                      "記憶與人格改變背後有哪幾格，以及復發之後還有哪些路。",
        "slugs": ["followup", "cognition", "recurrence"],
    },
]

TAGS = {
    "what-it-is": ["molecular", "staging", "decision"],
    "first-days": ["prep", "workflow", "mdt", "steroid"],
    "surgery": ["neurosurgery", "decision", "imaging", "evidence"],
    "pathology": ["molecular", "biomarker", "staging", "workflow"],
    "lowgrade": ["molecular", "decision", "targeted", "evidence"],
    "standard": ["imrt", "chemo", "workflow", "evidence"],
    "mgmt": ["molecular", "biomarker", "chemo", "evidence"],
    "elderly": ["hypofx", "decision", "chemo", "evidence"],
    "numbers": ["evidence", "decision", "qol"],
    "newthings": ["trial", "evidence", "proton", "cost"],
    "rt-weeks": ["imrt", "workflow", "daily", "sideeffect"],
    "steroid": ["steroid", "sideeffect", "daily"],
    "seizure": ["seizure", "work", "sideeffect", "daily"],
    "warning-signs": ["emergency", "sideeffect", "caregiver", "daily"],
    "followup": ["followup", "imaging", "recurrence", "evidence"],
    "cognition": ["cognition", "lateeffect", "caregiver", "qol"],
    "recurrence": ["recurrence", "decision", "trial", "qol"],
}

# ---------------------------------------------------------- article metadata --
_ZH = {}
for _p in SRC["meta_zh"]:
    with open(_p, encoding="utf-8") as _fh:
        for _k, _rec in json.load(_fh).items():
            _ZH[_k[len("gb-"):]] = _rec

ART = {}
for _slug, _tags in TAGS.items():
    _m = dict(_ZH[_slug])
    _m["tags"] = _tags
    ART[_slug] = _m

EN = gbm_en.EN
SECTIONS_EN = gbm_en.SECTIONS_EN
HUB_EN = gbm_en.HUB

# ----------------------------------------------------------------- hub copy --
HUB = {
    "title": "膠質母細胞瘤專題｜報告上那一行字、開刀還剩多少、六週同步六個月維持、"
             "MGMT、那個數字、電場與新療法｜吳正友醫師",
    "desc": "膠質母細胞瘤病人與家屬最需要知道的 17 件事：2021 年的分類怎麼決定"
            "「膠質母細胞瘤」這個名字、發現那顆瘤之後頭幾天的順序、"
            "開刀「全部拿掉」其實問的是術後還剩多少、報告等兩週在等什麼、"
            "報告寫 IDH-mutant 為什麼是另一條路、六週同步與六個月維持怎麼吃、"
            "MGMT 那一行決定什麼又不決定什麼、"
            "年紀大或體能不好療程可以怎麼縮短、那個存活數字要怎麼讀、"
            "電場免疫疫苗質子與 BNCT 各走到哪一格、放療那六週實際長什麼樣、"
            "類固醇為什麼要慢慢減、癲癇藥與開車這件事、哪些狀況要當天回來、"
            "追蹤 MRI 怎麼排與變大不一定是惡化、記憶專注與人格改變，"
            "以及復發之後還有哪些路。每篇附原始文獻連結。",
    "sub": "從報告上那一行字，到治療結束之後——一個問題一篇。",
    "intro": "這是全站預後最差的一個癌別，所以我用跟別的專題不一樣的方式寫："
             "不靠「還有很多路」來安慰，也不把中位存活丟給你當期限——"
             "那個數字不是為你一個人算的。這 17 篇照著你真正會走過的順序排："
             "確診與分類、治療與實證、療程中的照護，最後是之後。"
             "先說我的位置：GBM 的放射治療是我自己在做的那一段，"
             "這個專題比較的另一邊，是神經外科同事的刀和神經腫瘤科同事的藥；"
             "電場治療我沒有在用，也不是我科裡的項目——"
             "所以拿放射去比手術和藥的那四篇，開頭都有同一段利益揭露。"
             "每一篇都附上原始文獻連結，負的試驗我寫負的，"
             "證據弱的地方我直接說弱，查不到的我就寫查不到。",
    "closing": "以上為一般性衛教說明，不能取代面對面的診療。"
               "膠質母細胞瘤的治療同時取決於分子分型、術後的殘餘體積、"
               "年齡、體能狀態與神經功能，同一個診斷在不同人身上會導向不同建議，"
               "實際治療請與你的主治醫師和多專科團隊討論。",
}

# No cross-topic sentence rewrites: every relative link in the gb fragments
# already points at a page that exists on the site under exactly that name
# (sit-ttfields, nt-bnct, nt-proton, sit-reirradiation, sit-pseudo,
# lc-brainmet, sit-elderly, sit-decide-for, sit-documents, sit-last-weeks,
# sit-trial-how, care-fever and their -en partners).
BODY_EDITS = {"zh": [], "en": []}

# topics.html / topics-en.html cards, inserted after the ec one (the last
# card on the pulled topics pages, which carry 11 cards).
TOPIC_CARD_ZH = """  <a class="topiccard" href="gbm.html">
    <div class="k">GLIOBLASTOMA</div>
    <div class="t">膠質母細胞瘤專題</div>
    <div class="d">我還有多久、開刀能不能拿乾淨、有沒有新的療法可以救——這是全站預後最差的一個癌別，所以不靠「還有很多路」安慰，也不把中位存活丟給你當期限。從報告上那一行字到治療結束之後，一個問題一篇。</div>
    <div class="steps"><span>確診與分類</span><span>治療與實證</span><span>療程中的照護</span><span>之後</span></div>
    <div class="go"><span class="n">17 篇</span><span class="ar">進入專題 →</span></div>
  </a>
"""

TOPIC_CARD_EN = """  <a class="topiccard" href="gbm-en.html">
    <div class="k">GLIOBLASTOMA</div>
    <div class="t">Glioblastoma Guide</div>
    <div class="d">How long have I got, did the surgery get it all, is there anything new that could save me — this is the worst prognosis of any cancer on this site, so there is no comfort taken from saying there are still plenty of roads, and no median survival handed to you as a deadline. From that line on the report to what comes after treatment, one question per article.</div>
    <div class="steps"><span>After the Diagnosis</span><span>What the Evidence Says</span><span>During Treatment</span><span>Afterwards</span></div>
    <div class="go"><span class="n">17 articles</span><span class="ar">Open the guide →</span></div>
  </a>
"""

# JSON-LD hasPart entries appended to the topics pages' CollectionPage.
HASPART_ZH = {"@type": "CollectionPage", "name": NAME_ZH,
              "url": "https://doremai2001.github.io/publicpage/gbm.html"}
HASPART_EN = {"@type": "CollectionPage", "name": NAME_EN,
              "url": "https://doremai2001.github.io/publicpage/gbm-en.html"}
