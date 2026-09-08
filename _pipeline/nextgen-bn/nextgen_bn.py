# -*- coding: utf-8 -*-
"""次世代治療專題 — BNCT 分組建題模組。頁名 nt-bn-<slug>.html。"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import notes

REPO = "/root/publicpage"
SRC = {"body_zh": os.path.join(HERE, "body_bn"),
       "body_en": os.path.join(HERE, "en_bn")}
TAG_SOURCES = {"zh": [os.path.join(REPO, n) for n in ("hn.html", "rc.html", "cc.html", "bc.html", "nt.html")],
               "en": [os.path.join(REPO, n) for n in ("hn-en.html", "rc-en.html", "cc-en.html", "bc-en.html", "nt-en.html")]}

PREFIX = "nt"
NAME_ZH = "次世代治療專題"
NAME_EN = "Next-Generation Therapy Guide"
CONDITION_ZH = "放射治療新技術"
CONDITION_EN = "Next-generation radiotherapy"
ABOUT_TYPE = "MedicalProcedure"
DATE = "2026-09-08"

LABEL_ADD = {}   # 需要的標籤在 nt.html 上都有了

_G = [
 ("BNCT：原理", "BNCT: the physics",
  "反應本身、劑量單位、以及中子走得到多深——後面所有數字都建立在這三篇上。",
  "The reaction itself, the dose unit, and how deep the neutrons get. Every number later rests on these three.",
  ["principle", "dose", "depth"]),
 ("BNCT：硼藥物", "BNCT: the boron drugs",
  "機器決定中子從哪裡來，藥決定硼跑到哪裡去。六十年來能用的只有兩種。",
  "The machine decides where the neutrons come from; the drug decides where the boron goes. In sixty years there have been two.",
  ["drugs", "pet", "newagents"]),
 ("BNCT：機器", "BNCT: the machines",
  "台灣的反應器，以及把反應器換成加速器改變了什麼、沒有改變什麼。",
  "Taiwan's reactor, and what swapping a reactor for an accelerator did and did not change.",
  ["thor", "accelerator"]),
 ("BNCT：各癌別的實證", "BNCT: the evidence",
  "六個癌別，每一篇都標明證據層級、分母與終點。這個領域沒有隨機分派試驗。",
  "Six cancers, each with its level of evidence, denominator and endpoint stated. There are no randomised trials in this field.",
  ["headneck", "gbm", "newgbm", "melanoma", "meningioma", "others"]),
 ("BNCT：現實面", "BNCT: the reality",
  "副作用、四個地方的法規身分，以及我該不該去問這件事的四個先決條件。",
  "Side effects, the regulatory status in four places, and the four conditions for whether to ask about this at all.",
  ["safety", "approval", "who"]),
]

SECTIONS = [{"zh": g[0], "stepsub_zh": g[2], "slugs": ["bn-" + s for s in g[4]]} for g in _G]
SECTIONS_EN = [{"en": g[1], "stepsub_en": g[3], "slugs": ["bn-" + s for s in g[4]]} for g in _G]

_TAGS = {
 "principle": ["bnct", "evidence"],
 "dose": ["bnct", "evidence"],
 "depth": ["bnct", "evidence", "decision"],
 "drugs": ["bnct", "evidence", "regulation"],
 "pet": ["bnct", "decision", "trial"],
 "newagents": ["bnct", "evidence"],
 "thor": ["bnct", "regulation", "cost", "trial"],
 "accelerator": ["bnct", "evidence", "regulation"],
 "headneck": ["bnct", "evidence", "trial"],
 "gbm": ["bnct", "evidence", "trial", "decision"],
 "newgbm": ["bnct", "evidence", "trial"],
 "melanoma": ["bnct", "evidence"],
 "meningioma": ["bnct", "evidence"],
 "others": ["bnct", "evidence", "decision"],
 "safety": ["bnct", "evidence", "decision"],
 "approval": ["bnct", "regulation", "nhi", "cost"],
 "who": ["bnct", "decision", "cost"],
}
TAGS = {"bn-" + k: v for k, v in _TAGS.items()}

_zh = json.load(open(os.path.join(HERE, "meta-all.json"), encoding="utf-8"))
_en = json.load(open(os.path.join(HERE, "meta-all-en.json"), encoding="utf-8"))
ART, EN = {}, {}
for _k, _v in _TAGS.items():
    ART["bn-" + _k] = dict(_zh[_k], tags=_v, note=notes.ZH[_k])
    EN["bn-" + _k] = dict(_en[_k], note=notes.EN[_k])

BODY_EDITS = {"zh": [], "en": []}
