# -*- coding: utf-8 -*-
"""English side of the oesophageal-cancer topic.

SECTIONS_EN[i]["en"] is load-bearing on BOTH languages: topicbuild derives
every article's kicker from SECTIONS_EN[i]["en"].upper() regardless of the
language being built.  The four group names are the ones agreed for the
topic (How Treatment Is Decided / What the Evidence Says for Each Treatment /
During Treatment / After Treatment); the two shared with liver are spelled
exactly as liver_en spells them.

Article titles are verbatim from SPEC-EN.md section 3 by way of
meta/{A,B,C,D}-en.json, which are keyed "ec-<slug>"; EN is re-keyed on the
unprefixed tail because topicbuild composes "<PREFIX>-<slug>.html".

British spelling throughout (oesophageal, oesophagectomy, randomised), as on
the rest of the site's English pages.
"""

import json

# Group names -> article kickers (shared with the zh build; do not retitle).
SECTIONS_EN = [
    {
        "en": "How Treatment Is Decided",
        "stepsub_en": "Squamous and adenocarcinoma are two diseases, the "
                      "scans that decide whether an operation is possible, "
                      "the map of every treatment road, and the question "
                      "asked most after chemoradiotherapy: do I still need "
                      "surgery.",
        "slugs": ["two-diseases", "workup", "treatment-map",
                  "surgery-or-watch"],
    },
    {
        "en": "What the Evidence Says for Each Treatment",
        "stepsub_en": "Why a higher radiation dose did not buy more control, "
                      "who immunotherapy actually helps, what the operation "
                      "removes, when endoscopy alone is enough, and where "
                      "the proton trials stand.",
        "slugs": ["crt-dose", "immunotherapy", "surgery", "esd", "proton"],
    },
    {
        "en": "During Treatment",
        "stepsub_en": "Whether a feeding tube should go in first, the "
                      "oesophagitis weeks and why you must not stop on your "
                      "own, what needs a same-day visit, and what to settle "
                      "before the course starts.",
        "slugs": ["feeding-tube", "esophagitis", "warning-signs",
                  "before-start"],
    },
    {
        "en": "After Treatment",
        "stepsub_en": "Eating with a stomach that now sits in the chest, "
                      "telling a stricture from a recurrence, how follow-up "
                      "is scheduled and the second cancer it must not miss, "
                      "and the roads that remain after recurrence.",
        "slugs": ["eating-after", "stricture-or-recurrence", "followup",
                  "recurrence"],
    },
]

# Article metadata, titles verbatim from SPEC-EN.md section 3.
EN = {}
for _g in "ABCD":
    with open("/home/claude/esoph/meta/%s-en.json" % _g, encoding="utf-8") as _fh:
        for _k, _rec in json.load(_fh).items():
            EN[_k[len("ec-"):]] = _rec

HUB = {
    "title": "Oesophageal Cancer Guide | Squamous or adenocarcinoma, surgery "
             "after chemoradiotherapy, dose, immunotherapy, protons, feeding "
             "tubes and life after an oesophagectomy | Dr. Robert J.-Y. Wu",
    "desc": "Seventeen articles on oesophageal cancer: why squamous cell "
            "carcinoma and adenocarcinoma are two different diseases, the "
            "tests that decide whether surgery is possible, the treatment map "
            "and which box you are in, whether you still need surgery after "
            "chemoradiotherapy, why a higher radiation dose is not better, "
            "who immunotherapy actually helps, what the operation removes and "
            "where the stomach goes, whether endoscopy alone can deal with an "
            "early lesion, the case for protons and where the trials stand, "
            "whether a feeding tube should go in first, getting through "
            "radiation oesophagitis, when to come back the same day, what to "
            "settle before treatment starts, eating after an oesophagectomy, "
            "whether worse swallowing is a stricture or a recurrence, how "
            "follow-up is scheduled and the second cancer people forget, and "
            "what roads remain after recurrence or spread. Every article "
            "links its primary sources.",
    "sub": "From the pathology report to years after treatment — one "
           "question per article.",
    "intro": "Three things weigh most on someone with oesophageal cancer: "
             "whether they will still be able to eat, whether they need the "
             "big operation, and whether immunotherapy is their answer. "
             "These seventeen articles follow the order you will actually "
             "walk: how treatment is decided, what the evidence says for each "
             "treatment, care during the course, and what comes after. My "
             "position first: concurrent chemoradiotherapy and proton therapy "
             "for oesophageal cancer are treatments I deliver myself, every "
             "week, and the other side of every comparison here is my "
             "thoracic-surgery colleagues' operation and my gastroenterology "
             "colleagues' endoscopy — so the four articles that compare them "
             "open with the same declaration of interest, and every "
             "comparison carries its primary source so you can take it to "
             "the surgical and gastroenterology clinics for a second opinion. "
             "In Taiwan more than nine in ten cases are squamous cell "
             "carcinoma, so that is the main line; adenocarcinoma takes a "
             "different road and gets its own article. Every article links "
             "its primary sources; where the evidence is weak I say so "
             "plainly, and where a number could not be found I say that too.",
    "closing": "This is general patient education and does not replace a "
               "consultation. Treatment for oesophageal cancer depends at the "
               "same time on histology, stage, the tumour's position, fitness "
               "for surgery and nutritional state, and the same stage leads "
               "to different recommendations in different people; decisions "
               "about your own treatment belong with your physician and the "
               "multidisciplinary team.",
}
