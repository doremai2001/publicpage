# -*- coding: utf-8 -*-
"""Benign-brain-tumour topic module (Chinese side, plus the wiring to the
English one).

Naming: hub bt.html / bt-en.html, articles bt-<slug>.html -- the hub shares
the prefix exactly as em / ec / cx / pel do, so topicbuild's own _hub_name
gives "bt.html" / "bt-en.html" and there is NO monkeypatch here (liver and
gbm needed one; bt does not).  Checked before writing this module:
topicbuild._hub_name("bt", "zh") == "bt.html".

Three of the twenty-one slugs carry a sub-prefix of their own -- mg- for
meningioma, an- for vestibular schwannoma, pit- for pituitary adenoma --
so the composed file names come out bt-mg-grade.html, bt-an-hearing.html,
bt-pit-apoplexy.html and so on, as SPEC.md section 五 prescribes.  The
sub-prefix is part of the slug, not a second build-time concept.

The source fragments under /home/claude/bt/body carry the bt- prefix; the
English ones under /home/claude/bt/en carry BOTH the bt- prefix and a -en
suffix (unlike endo, whose English fragments carried neither suffix).
stage_bt_figs.py strips the prefix and the suffix and inserts the twelve
figures, so the builder's "<PREFIX>-<slug>.html" never comes out as
bt-bt-*.

Article metadata: meta/{A,B,C,D,E}.json are keyed "bt-<slug>"; _ZH is
re-keyed on the tail.  Nothing is retyped -- the titles in those files are
already SPEC.md 修正 21's canonical set.

A disease topic, so the JSON-LD "about" entity is the topicbuild default,
MedicalCondition -- no ABOUT_TYPE override.

The conflict-of-interest paragraph (SPEC section 二) sits before the first
<h4> of exactly four articles -- B3 mg-rt, B4 mg-adjuvant, C2 an-choice and
D3 pit-surgery-rt -- and nowhere else; verify_bt pins that.
"""

import json
import os

import bt_en

_STAGE = "/home/claude/bt/staging"

# ------------------------------------------------------------------ sources --
SRC = {
    "body_zh": os.path.join(_STAGE, "body"),
    "body_en": os.path.join(_STAGE, "en"),
    "meta_zh": ["/home/claude/bt/meta/%s.json" % g for g in "ABCDE"],
    "meta_en": ["/home/claude/bt/meta/%s-en.json" % g for g in "ABCDE"],
}

REPO = "/home/claude/repo"

# Existing hub pages the tag labels are harvested from, so no label is
# retyped.  First hub listed wins for a key that two hubs label differently:
# gbm leads because it is the sibling brain topic and already carries
# seizure / steroid / neurosurgery / cognition; liver comes next because it
# is the hub whose "sbrt" chip reads 立體定位放射 rather than pc/lc's
# SBRT／SRS, which is the wording this topic wants.
TAG_SOURCES = {
    "zh": [os.path.join(REPO, n) for n in
           ("gbm.html", "liver.html", "em.html", "pel.html", "brt.html",
            "cx.html", "bc.html", "nt.html", "cc.html", "rc.html",
            "hn.html", "ec.html", "lc.html", "pc.html")],
    "en": [os.path.join(REPO, n) for n in
           ("gbm-en.html", "liver-en.html", "em-en.html", "pel-en.html",
            "brt-en.html", "cx-en.html", "bc-en.html", "nt-en.html",
            "cc-en.html", "rc-en.html", "hn-en.html", "ec-en.html",
            "lc-en.html", "pc-en.html")],
}

# ------------------------------------------------------------------ identity --
PREFIX = "bt"
KICKER = "BENIGN BRAIN TUMOUR"
NAME_ZH = "良性腦瘤專題"
NAME_EN = "Benign Brain Tumour Guide"
CONDITION_ZH = "良性腦瘤"
CONDITION_EN = "Benign brain tumour"
DATE = "2026-09-13"

# imaging / decision / surveil / evidence / staging / molecular /
# neurosurgery / followup / surgery / recurrence / sbrt / proton / nhi /
# trial / endocrine / regulation / screening / recovery / sideeffect / qol /
# biomarker / fertility / emergency / steroid / seizure / work / lateeffect /
# genetic all exist on the harvested hubs and are reused verbatim.  These two
# are new; English labels follow the existing hubs' convention (Title Case
# noun phrases, British spelling).
LABEL_ADD = {
    "hearing": ("聽力", "Hearing"),
    "pituitary": ("腦下垂體", "Pituitary"),
    # Not a new label: "sbrt" is the one key two published hubs word
    # differently in English -- liver-en says "SBRT", lc-en and pc-en say
    # "SBRT / SRS".  This topic treats single-session radiosurgery, so the
    # SRS half has to be visible; pinned here to lc-en/pc-en's wording
    # (copied from those pages, not invented) while the Chinese keeps
    # liver.html's 立體定位放射, which is already the generic one.
    "sbrt": ("立體定位放射", "SBRT / SRS"),
}

# ------------------------------------------------------------------ sections --
# Group titles and per-group order verbatim from SPEC section 五 (4/5/3/4/5).
SECTIONS = [
    {
        "zh": "共同的起點",
        "stepsub_zh": "影像上發現一顆東西之後的第一輪問題、三種病為什麼不共用同一套邏輯、"
                      "位置為什麼比大小重要，以及「先觀察」到底是什麼樣的處置。",
        "slugs": ["incidental", "three-kinds", "where", "watch"],
    },
    {
        "zh": "腦膜瘤",
        "stepsub_zh": "報告上的第 1、2、3 級怎麼判、手術拿掉多少還算不算數、"
                      "單次還是分次、開完刀要不要加放療，"
                      "以及黃體素藥物那一題證據到底說了什麼。",
        "slugs": ["mg-grade", "mg-surgery", "mg-rt", "mg-adjuvant",
                  "mg-hormone"],
    },
    {
        "zh": "聽神經瘤",
        "stepsub_zh": "為什麼這一題的主角是聽力、觀察與放射手術與開刀怎麼比"
                      "（每個數字都要帶自己的那把尺），以及治療之後的平衡、聽力與臉。",
        "slugs": ["an-hearing", "an-choice", "an-after"],
    },
    {
        "zh": "腦下垂體瘤",
        "stepsub_zh": "先看它有沒有在分泌、為什麼只有泌乳素瘤是先吃藥、"
                      "經鼻手術與放療各自的位置，以及兩個要先問清楚的急症面。",
        "slugs": ["pit-function", "pit-prolactinoma", "pit-surgery-rt",
                  "pit-apoplexy"],
    },
    {
        "zh": "共同的之後",
        "stepsub_zh": "癲癇、水腫與類固醇（含開車那一題）、追蹤怎麼排追到什麼時候、"
                      "復發之後能做的是什麼、放射線會不會長出第二個瘤，"
                      "以及多發性、NF2 與家人的事。",
        "slugs": ["seizure-steroid", "followup", "recurrence",
                  "radiation-induced", "nf2"],
    },
]

TAGS = {
    "incidental": ["imaging", "surveil", "decision", "evidence"],
    "three-kinds": ["staging", "molecular", "evidence", "decision"],
    "where": ["imaging", "staging", "neurosurgery", "decision"],
    "watch": ["surveil", "imaging", "followup", "decision"],
    "mg-grade": ["staging", "molecular", "evidence", "recurrence"],
    "mg-surgery": ["neurosurgery", "surgery", "recurrence", "evidence"],
    "mg-rt": ["sbrt", "proton", "evidence", "nhi"],
    "mg-adjuvant": ["sbrt", "evidence", "trial", "decision"],
    "mg-hormone": ["endocrine", "regulation", "evidence", "decision"],
    "an-hearing": ["hearing", "imaging", "screening", "evidence"],
    "an-choice": ["sbrt", "surgery", "hearing", "decision"],
    "an-after": ["hearing", "recovery", "sideeffect", "qol"],
    "pit-function": ["pituitary", "endocrine", "biomarker", "decision"],
    "pit-prolactinoma": ["pituitary", "endocrine", "fertility", "evidence"],
    "pit-surgery-rt": ["neurosurgery", "sbrt", "pituitary", "evidence"],
    "pit-apoplexy": ["emergency", "pituitary", "steroid", "endocrine"],
    "seizure-steroid": ["seizure", "steroid", "work", "evidence"],
    "followup": ["followup", "imaging", "surveil", "evidence"],
    "recurrence": ["recurrence", "sbrt", "trial", "decision"],
    "radiation-induced": ["lateeffect", "sbrt", "evidence", "decision"],
    "nf2": ["genetic", "hearing", "screening", "decision"],
}

# ---------------------------------------------------------- article metadata --
_ZH = {}
for _p in SRC["meta_zh"]:
    with open(_p, encoding="utf-8") as _fh:
        for _k, _rec in json.load(_fh).items():
            _ZH[_k[len("bt-"):]] = _rec

ART = {}
for _slug, _tags in TAGS.items():
    _m = dict(_ZH[_slug])
    _m["tags"] = _tags
    ART[_slug] = _m

EN = bt_en.EN
SECTIONS_EN = bt_en.SECTIONS_EN
HUB_EN = bt_en.HUB

# ----------------------------------------------------------------- hub copy --
HUB = {
    "title": "良性腦瘤專題｜腦膜瘤、聽神經瘤、腦下垂體腺瘤：影像上發現一顆東西、"
             "先觀察也是一種處置、放射手術還是開刀、聽力、荷爾蒙，"
             "以及之後的日子｜吳正友醫師",
    "desc": "三種最常見的良性腦瘤病人最需要知道的 21 件事："
            "影像上發現一顆東西之後第一輪要問什麼、「常不常見」為什麼有三個分母、"
            "腦膜瘤看分級與位置、聽神經瘤看聽力、腦下垂體腺瘤先看它有沒有在分泌"
            "——三套邏輯為什麼不能混用、位置為什麼比大小重要、"
            "先觀察是什麼樣的處置又要付出什麼、腦膜瘤的第 1 到第 3 級怎麼判、"
            "Simpson 分級還算不算數、單次還是分次、開完刀要不要加放療、"
            "黃體素藥物那一題證據說了什麼、聽力保存率為什麼一定要帶那把尺、"
            "泌乳素瘤為什麼是唯一先吃藥的那一種、垂體中風與腎上腺功能不足、"
            "癲癇與開車、追蹤追到什麼時候、復發之後能做的是什麼、"
            "放射線會不會長出第二個瘤，以及多發性、NF2 與家人的事。"
            "每篇附原始文獻連結。",
    "sub": "從報告上那一行字，到之後好幾年的追蹤——一個問題一篇。",
    "intro": "這個專題的方向跟膠質母細胞瘤專題相反。那邊要防的是絕望，"
             "這裡要防的是過度治療、過度恐慌，以及「良性」兩個字造成的兩種誤讀。"
             "一邊，「良性」被讀成「不用管」——但壓到視神經的腦膜瘤、正在長的泌乳素瘤、"
             "已經造成單側聽損的聽神經瘤，都不是不用管的東西。"
             "另一邊，「腦瘤」被讀成「腦癌」，一個第 1 級凸面腦膜瘤的人，"
             "可能因為兩個字就去要求開刀。兩個方向都要擋，而且常常要在同一段裡擋。"
             "第二件事是三種病不合寫成一套：腦膜瘤看分級與位置，聽神經瘤看聽力，"
             "腦下垂體腺瘤先看它有沒有在分泌——所以這裡每一個數字都帶著"
             "「這是哪一種瘤」的標籤，一個讀起來三種通用的數字，就算算術沒錯也是錯的。"
             "先說我的位置：立體定位放射手術與分次放療是我自己在做的那一段；"
             "這個專題比較的另一邊，是神經外科、神經耳科與內分泌科同事的工作"
             "——所以拿放療去比刀和藥的那四篇，開頭都有同一段利益揭露，"
             "每一個比較都附上原始文獻，讓你可以拿著它去那幾科聽第二意見。"
             "證據弱的地方我會直接說弱，數字查不到的地方我會說查不到。",
    "closing": "以上為一般性衛教說明，不能取代面對面的診療。"
               "良性腦瘤要怎麼處理，同時取決於瘤別、有分級的看分級、"
               "長在哪裡與貼到什麼、大小與生長速度、聽力與荷爾蒙功能，"
               "以及你整體的身體狀況；同一張影像在不同人身上會導向不同建議。"
               "實際治療請與你的神經外科、神經耳科、內分泌科、放射腫瘤科主治醫師"
               "與多專科團隊討論。",
}

# No cross-topic sentence rewrites inside the bt fragments: every in-topic and
# on-site cross-reference is an unlinked 〈title〉 (zh) or "title" (en), as
# SPEC-EN section 4 prescribes, so there is nothing to rewrite at build time.
BODY_EDITS = {"zh": [], "en": []}

# topics.html / topics-en.html cards, inserted after the em one (the last
# card on the pulled topics pages, which carry 13 cards).
TOPIC_CARD_ZH = """  <a class="topiccard" href="bt.html">
    <div class="k">BENIGN BRAIN TUMOUR</div>
    <div class="t">良性腦瘤專題</div>
    <div class="d">「良性」會被讀成不用管，「腦瘤」會被讀成腦癌，兩個方向都要擋——腦膜瘤、聽神經瘤、腦下垂體腺瘤這三種病，看的是三套不同的邏輯，任何一個數字都要帶「這是哪一種瘤」的標籤。從報告上那一行字，到之後好幾年的追蹤，一個問題一篇。</div>
    <div class="steps"><span>共同的起點</span><span>腦膜瘤</span><span>聽神經瘤</span><span>腦下垂體瘤</span><span>共同的之後</span></div>
    <div class="go"><span class="n">21 篇</span><span class="ar">進入專題 →</span></div>
  </a>
"""

TOPIC_CARD_EN = """  <a class="topiccard" href="bt-en.html">
    <div class="k">BENIGN BRAIN TUMOUR</div>
    <div class="t">Benign Brain Tumour Guide</div>
    <div class="d">"Benign" gets read as "ignore it" and "brain tumour" gets read as "brain cancer", and both readings have to be blocked — meningioma, vestibular schwannoma and pituitary adenoma run on three separate logics, and every number here carries a label saying which tumour it belongs to. From the line on the report to the years of follow-up after it, one question per article.</div>
    <div class="steps"><span>Where everyone starts</span><span>Meningioma</span><span>Vestibular schwannoma</span><span>Pituitary adenoma</span><span>What comes after</span></div>
    <div class="go"><span class="n">21 articles</span><span class="ar">Open the guide →</span></div>
  </a>
"""

# JSON-LD hasPart entries appended to the topics pages' CollectionPage.
HASPART_ZH = {"@type": "CollectionPage", "name": NAME_ZH,
              "url": "https://doremai2001.github.io/publicpage/bt.html"}
HASPART_EN = {"@type": "CollectionPage", "name": NAME_EN,
              "url": "https://doremai2001.github.io/publicpage/bt-en.html"}

# ------------------------------------------------------- build-time chore ---
# gb-what-it-is(-en).html is the one published page that promises this topic
# rather than pointing at it: it says the meningioma topic is one the author
# "另開專題" / "is giving ... a topic of its own", and it dismisses pituitary
# tumours and acoustic neuroma with "這兩個都不是這個專題在講的東西" /
# "Neither of those is what this topic is about" without saying where they
# are.  Both sentences are mirrored zh/en pairs, so both are rewritten in
# both files -- two substitutions per file, four in all.
#
# On the LINK question this differs from the endo round's pel-who chore, and
# the difference was checked rather than assumed.  pel-who's body carried
# zero in-body site links, so 修正 20 pointed in sense only.  gb-what-it-is
# does carry one, and it sits one sentence above the first edit, in the same
# block of paragraphs:
#     站上另有一篇〈<a href="lc-brainmet.html">腦轉移不等於末期</a>〉。
#     …a separate article on the site, <a href="lc-brainmet-en.html">Brain
#     metastases are not the end</a>.
# So a LINKED title is this page's own house style for an on-site pointer,
# and an unlinked one two sentences later would be the odd one out.  The
# first new pointer therefore carries an <a>, matching that form exactly;
# the second, in the next sentence of the same paragraph, stays unlinked so
# the paragraph does not carry the same href twice.  Nothing else on either
# page moves -- verify_bt pins the diff to exactly these two substitutions
# per file, and pins the pre-existing lc-brainmet link unchanged.
GB_WHAT_EDITS = {
    "gb-what-it-is.html": [
        (
            "那是另一個病，作者另開專題。",
            "那是另一個病，站上另有〈<a href=\"bt.html\">良性腦瘤專題</a>〉。",
        ),
        (
            "這兩個都不是這個專題在講的東西。",
            "這兩個都不是這個專題在講的東西，它們和腦膜瘤一起寫在〈良性腦瘤專題〉裡。",
        ),
    ],
    "gb-what-it-is-en.html": [
        (
            "That is another disease, and the author is giving it a topic "
            "of its own.",
            "That is another disease, and it has a topic of its own, "
            "<a href=\"bt-en.html\">Benign Brain Tumour Guide</a>.",
        ),
        (
            "Neither of those is what this topic is about.",
            "Neither of those is what this topic is about; both of them, "
            "along with meningioma, are in \"Benign Brain Tumour Guide\".",
        ),
    ],
}
