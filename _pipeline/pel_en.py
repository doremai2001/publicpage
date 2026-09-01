# -*- coding: utf-8 -*-
"""English side of the pelvic-radiotherapy topic (round 2).

Round 1 shipped the Chinese pages alone with pel.ZH_ONLY = True and this
module reduced to SECTIONS_EN.  Round 2 fills in EN and HUB and flips that
switch; nothing else in the build changed.

SECTIONS_EN[i]["en"] is load-bearing on BOTH languages: topicbuild derives
every article's kicker from SECTIONS_EN[i]["en"].upper() regardless of the
language being built, so the three group names below are exactly the ones the
already-published Chinese pages carry.  They are reproduced here unchanged --
retitling one would silently rewrite a live Chinese page's kicker.

Article titles are verbatim from SPEC-EN.md section 3 (canonical English
titles) by way of meta/{A,B,C}-en.json; nothing is retyped here.  Those meta
files are keyed A1/A2/... rather than by slug, exactly like the Chinese ones,
so EN is re-keyed below on each record's own "slug" field with the "pel-"
prefix stripped -- the slugs used throughout the build are the unprefixed
tails, because topicbuild composes "<PREFIX>-<slug>.html".

Terminology and register follow SPEC-EN.md section 4: British spelling, and
the hub copy stays descriptive rather than promotional -- it says what the
topic is (the preparation, technique and care the five pelvic cancers share)
and sends each cancer's own treatment decisions back to its own guide.
"""

import json

# Group names -> article kickers (shared with the zh build; do not retitle).
SECTIONS_EN = [
    {
        "en": "Who Is Treated, and Getting Ready",
        "stepsub_en": "Where each of the five cancers is irradiated and what "
                      "that buys, what happens on the day of the planning "
                      "scan, the bladder and bowel state you copy each day, "
                      "and two implants whose evidence has opposite shapes.",
        "slugs": ["who", "sim-day", "bladder-bowel", "implants"],
    },
    {
        "en": "How the Technique Is Chosen",
        "stepsub_en": "Modulation, image guidance and particles are three "
                      "things that stack rather than three to choose between; "
                      "which endpoints improved and which did not, and where "
                      "the evidence for protons stands.",
        "slugs": ["technique-map", "igrt", "toxicity", "proton"],
    },
    {
        "en": "During Treatment and After",
        "stepsub_en": "The time windows for skin, bowel and urinary symptoms, "
                      "the late bleeding that starts months after the course "
                      "ends, and the warning signs and order of care for a "
                      "fistula.",
        "slugs": ["skin", "colitis", "urinary", "late", "fistula"],
    },
]

# Article metadata, titles verbatim from SPEC-EN.md section 3.
EN = {}
for _g in "ABC":
    with open("/home/claude/pel/meta/%s-en.json" % _g, encoding="utf-8") as _fh:
        for _rec in json.load(_fh).values():
            EN[_rec["slug"][len("pel-"):]] = _rec

HUB = {
    "title": "Pelvic Radiotherapy Guide | Who is treated, the planning scan "
             "and the daily preparation, how the technique is chosen, and "
             "care during treatment and after | Dr. Robert J.-Y. Wu",
    "desc": "The pelvis is one anatomical region, and bladder, cervical, "
            "endometrial, rectal and prostate cancer share the same "
            "preparation, the same techniques and the same care. Thirteen "
            "articles: where each of the five cancers is irradiated and what "
            "that buys, what happens on the day of the planning scan, why the "
            "bladder and bowel state you copy each day is the one your plan "
            "was built on, the opposite evidence shapes of fiducial markers "
            "and rectal spacers, how modulation, image guidance and particles "
            "stack, what daily imaging actually buys, which side effects "
            "intensity-modulated radiotherapy improves and which it does not, "
            "where the evidence for protons stands, and skin, bowel, urinary "
            "symptoms, late bleeding and fistula. Every article links its "
            "primary sources and labels the level of evidence.",
    "sub": "The preparation, technique and care the five pelvic cancers share "
           "— one question per article.",
    "intro": "The pelvis is one anatomical region: radiotherapy for bladder, "
             "cervical, endometrial, rectal and prostate cancer shares the "
             "same planning scan, the same preparation, the same techniques "
             "and the same care, and it is that shared part these articles "
             "are about. Whether each of those cancers should be irradiated "
             "at all, how large a volume, and how radiotherapy sits alongside "
             "surgery and systemic treatment belong to the individual disease "
             "guides; here they are pointed to rather than reopened. A few "
             "rules held throughout: \"better on dosimetry\" and \"better on "
             "clinical outcomes\" are always written separately, and every "
             "figure carries the cancer, the dose and the technique it came "
             "from; bladder preparation is not simply holding as much as you "
             "can — some plans want a full bladder and some an empty one, and "
             "the job is to reproduce the state the plan was built on; and "
             "the choice of technique is written as a question of indication "
             "rather than of budget. Pelvic radiotherapy is what I do every "
             "day, so every article opens with the same declaration of "
             "interest; on cost I cite the official schedule where one exists "
             "and tell you to ask the medical affairs office where it does "
             "not. Every article links its primary sources; where the "
             "evidence is weak I say so plainly, and where a number could not "
             "be found I say that too.",
    "closing": "This is general patient education and does not replace a "
               "consultation. The volume, the number of treatments and the "
               "technique depend at the same time on the cancer, the stage, "
               "the operation and the systemic treatment plan, and the same "
               "region leads to different approaches in different people; "
               "each cancer's own treatment decisions belong in its own "
               "guide, and decisions about your own treatment belong with "
               "your physician and the multidisciplinary team.",
}
