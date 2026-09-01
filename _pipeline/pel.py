# -*- coding: utf-8 -*-
"""Pelvic-radiotherapy topic module (Chinese side; the English wiring is
present but switched off for round 1).

ZH_ONLY is the round switch, the same design brt.py used.  While True
(round 1) the builder wrote the thirteen Chinese articles plus pel.html, left
the hreflang block / the English canonical partner / the language-switch chip
out of every page, patched topics.html only, and added fourteen sitemap URLs.
Round 2 sets it False: all 28 pages are rewritten -- the thirteen Chinese ones
and pel.html regain hreflang and the language switch, and are otherwise
byte-identical to what is already published -- topics-en.html gets its card,
and fourteen more sitemap URLs are appended.  Both English SVG variants were
already copied into the repo in round 1, so round 2 transfers no figures.

ROUND 2 IS ACTIVE (ZH_ONLY = False).  Round 1 is live as commits 55610da and
fa7e5a4, so the build/verify baseline is the git HEAD blob of each file, not a
scratch snapshot: verify check 13 diffs every regenerated Chinese page against
its published version and requires the difference to be confined to the
hreflang / language-switch lines.  No Chinese source was corrected between the
rounds, so ALL THIRTEEN articles and the hub must come out hreflang-only --
there is no EXPECTED_BODY_DIFF list here, and any body difference is a
failure, not something to declare.

Naming: the hub is pel.html / pel-en.html and the articles are pel-<slug>.html,
i.e. the hub shares the prefix exactly as cx / hn / bc / brt do, so
topicbuild's own _hub_name is correct and there is NO monkeypatch here.

The source fragments under /home/claude/pel/body already carry the pel-
prefix; stage_pel_figs.py strips it (and inserts the figures) so the builder's
"<PREFIX>-<slug>.html" never comes out as pel-pel-*.  SLUGS below are
therefore the unprefixed tails.

Article metadata: the pel meta files are keyed A1/A2/... , NOT by slug (this
differs from brt, whose keys were the slugs).  _ZH below is re-keyed on each
record's own "slug" field with the "pel-" prefix stripped; nothing is retyped.

Titles: the formal article titles are the meta titles.  SPEC section 四's list
headings are working code names and were superseded -- see the ruling at the
top of FIXES.md.  Nothing here may retype them.

This is a cross-cancer TREATMENT topic (five cancers share one anatomical
region), not a topic about one disease, so the JSON-LD "about" entity follows
nextgen.py rather than the disease topics: ABOUT_TYPE = MedicalProcedure with
the therapy itself as the name, exactly as nt does with 放射治療新技術.
"""

import json
import os

import pel_en

# ------------------------------------------------------------------ switch --
ZH_ONLY = False

_STAGE = ("/tmp/claude-0/-home-claude/4bc50b06-d4e4-5989-80b2-34f0f02eed26/"
          "scratchpad/staging-pel")

# ------------------------------------------------------------------ sources --
SRC = {
    "body_zh": os.path.join(_STAGE, "body"),
    "body_en": os.path.join(_STAGE, "en"),
    "meta_zh": ["/home/claude/pel/meta/%s.json" % g for g in "ABC"],
    "meta_en": ["/home/claude/pel/meta/%s-en.json" % g for g in "ABC"],
}

REPO = "/home/claude/repo"

# Existing hub pages the tag labels are harvested from, so no label is
# retyped.  pc is in the list for urinary/recovery, rc for bowel, lc for
# emergency, nt for evidence/cost, brt for imrt/tomo.
TAG_SOURCES = {
    "zh": [os.path.join(REPO, n) for n in
           ("hn.html", "rc.html", "cc.html", "bc.html", "nt.html", "cx.html",
            "lc.html", "pc.html", "brt.html")],
    "en": [os.path.join(REPO, n) for n in
           ("hn-en.html", "rc-en.html", "cc-en.html", "bc-en.html",
            "nt-en.html", "cx-en.html", "lc-en.html", "pc-en.html",
            "brt-en.html")],
}

# ------------------------------------------------------------------ identity --
PREFIX = "pel"
KICKER = "PELVIC RADIOTHERAPY"
NAME_ZH = "骨盆腔放射治療專題"
NAME_EN = "Pelvic Radiotherapy Guide"
CONDITION_ZH = "骨盆腔放射治療"
CONDITION_EN = "Pelvic radiotherapy"
ABOUT_TYPE = "MedicalProcedure"      # cross-cancer treatment topic; see nt
DATE = "2026-09-01"

# decision / staging / nhi / evidence / prep / workflow / imaging / daily /
# bowel / urinary / cost / imrt / tomo / proton / sideeffect / qol / skin /
# nutrition / emergency / lateeffect all exist on the
# hn/rc/cc/bc/nt/cx/lc/pc/brt hubs and are reused verbatim.  These three are
# new; English labels follow the existing hubs' convention (Title Case noun
# phrases, the abbreviation kept where the zh label keeps it).
LABEL_ADD = {
    "igrt": ("影像導引", "Image Guidance"),
    "implant": ("植入物", "Implants"),
    "fistula": ("廔管", "Fistula"),
}

# ------------------------------------------------------------------ sections --
# Group titles verbatim from SPEC section 四 (the GROUP headings are not
# affected by the FIXES篇名 ruling -- only the per-article list headings were).
# 13 articles in 4 / 4 / 5, in the agreed reading order.
SECTIONS = [
    {
        "zh": "誰會被照、怎麼準備",
        "stepsub_zh": "五個癌別各自被照的位置與換到什麼、定位那一天會發生的事、"
                      "膀胱與腸道每天要複製的那個狀態，"
                      "還有兩種植入物各自不同形狀的證據。",
        "slugs": ["who", "sim-day", "bladder-bowel", "implants"],
    },
    {
        "zh": "技術怎麼選",
        "stepsub_zh": "調控、影像導引與粒子是三件可以疊起來的事，不是三選一；"
                      "哪些終點改善了、哪些沒有，以及質子的證據走到哪一格。",
        "slugs": ["technique-map", "igrt", "toxicity", "proton"],
    },
    {
        "zh": "療程中與之後",
        "stepsub_zh": "皮膚、腸道與解尿各自的時間窗，療程結束幾個月後才開始的晚期出血，"
                      "以及廔管的警訊與處理順序。",
        "slugs": ["skin", "colitis", "urinary", "late", "fistula"],
    },
]

TAGS = {
    "who": ["decision", "staging", "nhi", "evidence"],
    "sim-day": ["prep", "workflow", "imaging", "daily"],
    "bladder-bowel": ["prep", "daily", "bowel", "urinary"],
    "implants": ["implant", "evidence", "cost", "nhi"],
    "technique-map": ["imrt", "tomo", "proton", "igrt", "decision"],
    "igrt": ["igrt", "imaging", "workflow", "evidence"],
    "toxicity": ["imrt", "sideeffect", "evidence", "qol"],
    "proton": ["proton", "evidence", "cost", "nhi"],
    "skin": ["skin", "sideeffect", "daily"],
    "colitis": ["bowel", "sideeffect", "nutrition", "daily"],
    "urinary": ["urinary", "sideeffect", "emergency"],
    "late": ["lateeffect", "bowel", "evidence", "emergency"],
    "fistula": ["fistula", "lateeffect", "emergency", "evidence"],
}

# ---------------------------------------------------------- article metadata --
# The pel meta files are keyed A1/A2/... ; re-key on each record's own slug.
_ZH = {}
for _p in SRC["meta_zh"]:
    with open(_p, encoding="utf-8") as _fh:
        for _rec in json.load(_fh).values():
            _ZH[_rec["slug"][len("pel-"):]] = _rec

ART = {}
for _slug, _tags in TAGS.items():
    _m = dict(_ZH[_slug])
    _m["tags"] = _tags
    ART[_slug] = _m

# Round 2: pel_en now carries EN and HUB as well.  The getattr form is kept
# so the module still imports if this file is ever run against a round-1 stub.
EN = getattr(pel_en, "EN", None)
SECTIONS_EN = pel_en.SECTIONS_EN
HUB_EN = getattr(pel_en, "HUB", None)

# ----------------------------------------------------------------- hub copy --
HUB = {
    "title": "骨盆腔放射治療專題｜誰會被照、定位與每天的準備、"
             "技術怎麼分層、療程中與之後的照顧｜吳正友醫師",
    "desc": "骨盆腔是同一個解剖區，膀胱癌、子宮頸癌、子宮內膜癌、直腸癌、"
            "攝護腺癌共用同一套準備、技術與照顧。這裡有 13 篇："
            "五個癌別各自被照的位置與換到什麼、定位那一天會發生什麼、"
            "膀胱與腸道每天要複製的是計畫裡的那個狀態、"
            "金標與間隔物兩種形狀相反的證據、"
            "調控與影像導引與粒子怎麼疊起來、每天對位換到的是什麼終點、"
            "調控放療改善了哪些副作用又沒改善哪些、質子的證據走到哪一格，"
            "以及皮膚、腸道、解尿、晚期出血與廔管。"
            "每篇附原始文獻連結與證據等級標籤。",
    "sub": "五個癌別共用的準備、技術與照顧——一個問題一篇。",
    "intro": "骨盆腔是同一個解剖區：膀胱癌、子宮頸癌、子宮內膜癌、直腸癌與"
             "攝護腺癌的放射治療，共用同一套定位、準備、技術與照顧，"
             "所以這個專題寫的是這些共用的部分。"
             "五個癌別各自要不要照、照多大範圍、和手術或全身治療怎麼排，"
             "那些留在各自的疾病專題，這裡只指路，不重開。"
             "寫的時候有幾條規矩：「劑量學上比較好」和「臨床結果證實比較好」"
             "永遠分開寫，每個數字帶上癌別、劑量與技術的標籤；"
             "膀胱準備不是一律憋尿——有的計畫要滿、有的要空，"
             "主題是複製計畫當初做出來的那個狀態，不是憋越多越好；"
             "技術的選擇寫成適應症的問題，不是預算的問題。"
             "骨盆腔的放射治療是我每天在做的治療，"
             "所以每一篇開頭都有同一段利益揭露；"
             "費用查得到官方公告就引，查不到就寫請問醫務課。"
             "每一篇都附上原始文獻連結，證據弱的地方我會直接說弱，"
             "數字查不到的地方我會說查不到。",
    "closing": "以上為一般性衛教說明，不能取代面對面的診療。"
               "骨盆腔放射治療的範圍、次數與技術同時取決於癌別、期別、"
               "手術方式與全身治療計畫，同一個部位在不同人身上會導向不同做法；"
               "五個癌別各自的治療決定請看各自的專題，"
               "實際治療請與你的主治醫師和多專科團隊討論。",
}

# No cross-topic sentence rewrites: the only relative links in the pel
# fragments point at nt-proton.html and insight-proton.html, which exist on
# the site under exactly those names.
BODY_EDITS = {"zh": [], "en": []}

# topics.html card, inserted after the brt one (the last card on the pulled
# topics.html).
TOPIC_CARD_ZH = """  <a class="topiccard" href="pel.html">
    <div class="k">PELVIC RADIOTHERAPY</div>
    <div class="t">骨盆腔放射治療專題</div>
    <div class="d">膀胱、子宮頸、子宮內膜、直腸、攝護腺共用同一個解剖區：定位那一天、每天要複製的膀胱與腸道狀態、技術怎麼分層，以及療程中與結束之後的照顧。</div>
    <div class="steps"><span>誰會被照、怎麼準備</span><span>技術怎麼選</span><span>療程中與之後</span></div>
    <div class="go"><span class="n">13 篇</span><span class="ar">進入專題 →</span></div>
  </a>
"""

# The topics-en.html card, inserted after the brt-en one.  Untouched in
# round 1 (pel-en.html did not exist yet); added in round 2.
TOPIC_CARD_EN = """  <a class="topiccard" href="pel-en.html">
    <div class="k">PELVIC RADIOTHERAPY</div>
    <div class="t">Pelvic Radiotherapy Guide</div>
    <div class="d">Bladder, cervix, endometrium, rectum and prostate share one anatomical region: the day of the planning scan, the bladder and bowel state you copy each day, how the techniques stack, and care during treatment and after it ends.</div>
    <div class="steps"><span>Who Is Treated, and Getting Ready</span><span>How the Technique Is Chosen</span><span>During Treatment and After</span></div>
    <div class="go"><span class="n">13 articles</span><span class="ar">Open the guide →</span></div>
  </a>
"""

# JSON-LD hasPart entries appended to the topics pages' CollectionPage.
HASPART_ZH = {"@type": "CollectionPage", "name": NAME_ZH,
              "url": "https://doremai2001.github.io/publicpage/pel.html"}
HASPART_EN = {"@type": "CollectionPage", "name": NAME_EN,
              "url": "https://doremai2001.github.io/publicpage/pel-en.html"}
