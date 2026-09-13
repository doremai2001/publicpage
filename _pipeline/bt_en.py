# -*- coding: utf-8 -*-
"""English side of the benign-brain-tumour topic.

SECTIONS_EN[i]["en"] is load-bearing on BOTH languages: topicbuild derives
every article's kicker from SECTIONS_EN[i]["en"].upper() regardless of the
language being built.  The five group names are the ones agreed for the
topic (Where everyone starts / Meningioma / Vestibular schwannoma /
Pituitary adenoma / What comes after).

Article titles are verbatim from SPEC-EN.md section 4 by way of
meta/{A,B,C,D,E}-en.json, which are keyed "bt-<slug>"; EN is re-keyed on the
unprefixed tail because topicbuild composes "<PREFIX>-<slug>.html".  Note
that three of the tails carry their own sub-prefix (mg- / an- / pit-), so
the composed names come out bt-mg-grade.html, bt-an-hearing.html and so on,
exactly as SPEC.md section 五 prescribes.

British spelling throughout (tumour, oedema, randomised, counselling), as on
the rest of the site's English pages.
"""

import json

# Group names -> article kickers (shared with the zh build; do not retitle).
SECTIONS_EN = [
    {
        "en": "Where everyone starts",
        "stepsub_en": "What it means to find something on a scan, how the "
                      "three diseases are told apart and why their logics "
                      "are never shared, why where it sits matters more "
                      "than how big it is, and what watching actually "
                      "involves.",
        "slugs": ["incidental", "three-kinds", "where", "watch"],
    },
    {
        "en": "Meningioma",
        "stepsub_en": "How a meningioma gets called grade 1, 2 or 3, how "
                      "much the operation took out and whether that still "
                      "counts, one session or fractionated, whether "
                      "radiotherapy is added after surgery, and what the "
                      "progestogen evidence does and does not say.",
        "slugs": ["mg-grade", "mg-surgery", "mg-rt", "mg-adjuvant",
                  "mg-hormone"],
    },
    {
        "en": "Vestibular schwannoma",
        "stepsub_en": "Why hearing is what this decision is really about, "
                      "how watching, radiosurgery and surgery compare when "
                      "every figure carries its own ruler, and what "
                      "happens afterwards to balance, hearing and the face.",
        "slugs": ["an-hearing", "an-choice", "an-after"],
    },
    {
        "en": "Pituitary adenoma",
        "stepsub_en": "Whether it is secreting, why prolactinoma is the one "
                      "that starts with a drug, where endonasal surgery and "
                      "radiotherapy fit, and the two emergencies to know "
                      "about in advance.",
        "slugs": ["pit-function", "pit-prolactinoma", "pit-surgery-rt",
                  "pit-apoplexy"],
    },
    {
        "en": "What comes after",
        "stepsub_en": "Seizures, oedema and steroids including driving, how "
                      "follow-up is scheduled and when it stops, what can "
                      "be done if it comes back, whether radiotherapy grows "
                      "a second tumour, and what more than one of them "
                      "means for your family.",
        "slugs": ["seizure-steroid", "followup", "recurrence",
                  "radiation-induced", "nf2"],
    },
]

# Article metadata, titles verbatim from SPEC-EN.md section 4.
EN = {}
for _g in "ABCDE":
    with open("/home/claude/bt/meta/%s-en.json" % _g, encoding="utf-8") as _fh:
        for _k, _rec in json.load(_fh).items():
            EN[_k[len("bt-"):]] = _rec

HUB = {
    "title": "Benign Brain Tumour Guide | Meningioma, vestibular "
             "schwannoma and pituitary adenoma: what an incidental finding "
             "means, watching as treatment, radiosurgery or surgery, "
             "hearing, hormones, and what comes after "
             "| Dr. Robert J.-Y. Wu",
    "desc": "Twenty-one articles on the three commonest benign brain "
            "tumours: what it means when a scan finds something and why "
            "\"how common is this\" has three different denominators, why "
            "meningioma, vestibular schwannoma and pituitary adenoma run on "
            "three separate logics that must never be merged, why where a "
            "tumour sits matters more than how big it is, what watching "
            "actually involves and what it costs, how a meningioma is "
            "graded, what Simpson grade still means, one session or "
            "fractionated, whether radiotherapy is added after surgery, "
            "what the progestogen evidence says, why hearing is the real "
            "question in vestibular schwannoma and why every "
            "hearing-preservation figure has to carry its ruler, whether a "
            "pituitary tumour is secreting, why prolactinoma starts with a "
            "drug when the others start with surgery, pituitary apoplexy "
            "and adrenal insufficiency, seizures and driving, how "
            "follow-up is scheduled and when it stops, what can be done if "
            "it comes back, whether radiotherapy grows a second tumour, and "
            "what more than one of them means for your family. Every "
            "article links its primary sources.",
    "sub": "From the line on the report to the years of follow-up after it "
           "— one question per article.",
    "intro": "This guide runs in the opposite direction to the "
             "glioblastoma one. There the enemy is despair; here it is "
             "overtreatment, unnecessary fear, and the two ways the word "
             "\"benign\" gets misread. On one side, benign is heard as "
             "\"ignore it\" — but a meningioma pressing on the optic "
             "pathway, a prolactinoma that is growing, and a vestibular "
             "schwannoma that has already cost hearing are none of them "
             "things to leave alone. On the other, \"brain tumour\" is "
             "heard as \"brain cancer\", and someone with a small grade 1 "
             "convexity meningioma asks for an operation because of two "
             "words. Both readings have to be blocked, often in the same "
             "paragraph. The second thing this guide refuses to do is "
             "merge the three diseases: meningioma turns on grade and "
             "site, vestibular schwannoma on hearing, and a pituitary "
             "adenoma on whether it is secreting at all — so every number "
             "here carries a label saying which tumour it belongs to, and "
             "a figure that reads as applying to all three is a mistake "
             "even when the arithmetic is right. My position first: "
             "stereotactic radiosurgery and fractionated radiotherapy are "
             "the part I deliver myself, and the other side of every "
             "comparison here is my neurosurgical, neuro-otology and "
             "endocrinology colleagues' work — so the four articles that "
             "compare them open with the same declaration of interest, and "
             "every comparison carries its primary source so you can take "
             "it to those clinics for a second opinion. Where the evidence "
             "is weak I say so plainly, and where a number could not be "
             "found I say that too.",
    "closing": "This is general patient education and does not replace a "
               "consultation. What to do about a benign brain tumour "
               "depends at the same time on the type of tumour, its grade "
               "where one applies, where it sits and what it is touching, "
               "its size and growth, your hearing and hormone function and "
               "your health as a whole; the same scan leads to different "
               "recommendations in different people. Decisions about your "
               "own treatment belong with your neurosurgeon, your "
               "neuro-otologist, your endocrinologist, your radiation "
               "oncologist and the multidisciplinary team.",
}
