# -*- coding: utf-8 -*-
"""English side of the breast-radiotherapy topic (round 2).

Round 1 shipped the Chinese pages alone with brt.ZH_ONLY = True and this
module reduced to SECTIONS_EN.  Round 2 fills in EN and HUB and flips that
switch; nothing else in the build changed.

SECTIONS_EN[i]["en"] is load-bearing on BOTH languages: topicbuild derives
every article's kicker from SECTIONS_EN[i]["en"].upper() regardless of the
language being built, so the three group names below are exactly the ones the
already-published Chinese pages carry.  They are reproduced here unchanged --
retitling one would silently rewrite a live Chinese page's kicker.

Article titles are verbatim from SPEC-EN.md section 3 (canonical English
titles) by way of meta/{A,B,C}-en.json; nothing is retyped here.  Terminology
and register follow SPEC-EN.md section 4: British spelling, and the hub copy
stays descriptive rather than promotional.
"""

import json

# Group names -> article kickers (shared with the zh build; do not retitle).
SECTIONS_EN = [
    {
        "en": "Why, and How It Is Decided",
        "stepsub_en": "Which box the type of operation and the node count put "
                      "you in, why your number of treatments differs from "
                      "someone else's, and what each of those technical terms "
                      "actually governs.",
        "slugs": ["who-needs", "fractionation", "technique-map"],
    },
    {
        "en": "Choosing the Technique",
        "stepsub_en": "Heart dose on the left side is the core of this group; "
                      "where the evidence for TOMO and for protons has got "
                      "to, which situations show a difference and which do "
                      "not.",
        "slugs": ["heart", "tomo", "proton"],
    },
    {
        "en": "Treatment and Self-Care",
        "stepsub_en": "From the planning scan to the first treatment, when the "
                      "skin starts to react, what there is beyond the skin, "
                      "and the years after the course ends.",
        "slugs": ["sim-to-first", "skin", "beyond-skin", "after"],
    },
]

# Article metadata, titles verbatim from SPEC-EN.md section 3.
EN = {}
for _g in "ABC":
    with open("/home/claude/brt/meta/%s-en.json" % _g, encoding="utf-8") as _fh:
        for _k, _v in json.load(_fh).items():
            EN[_k[len("brt-"):]] = _v

HUB = {
    "title": "Breast Radiotherapy Guide | Who needs it, how many treatments, "
             "IMRT, TOMO and protons, heart dose and breath-hold, skin care "
             "and the years after | Dr. Robert J.-Y. Wu",
    "desc": "Ten things to know once you have been told you will have "
            "radiotherapy for breast cancer: which box the type of operation "
            "and the node count put you in, why you may not be on the shorter "
            "course, what IMRT, TOMO, protons and deep inspiration breath-hold "
            "each govern, how to read heart dose on the left side, where TOMO "
            "and ordinary IMRT actually differ, where the evidence for protons "
            "in the breast stands, what happens between the planning scan and "
            "the first treatment, when skin reactions come and how to care for "
            "them, fatigue, lungs and lymphoedema beyond the skin, and "
            "recovery and follow-up after it ends. Every article links its "
            "primary sources and labels the level of evidence.",
    "sub": "The decision to irradiate has been made; the question now is how "
           "— one question per article.",
    "intro": "These articles are for patients who have already been told they "
             "will have radiotherapy for breast cancer. Whether to irradiate "
             "at all, how large a volume, and when it can be omitted belong to "
             "the breast cancer guide; what is here is how it is delivered, "
             "which technique, how the five to six weeks go, and what you can "
             "do yourself. A few rules held throughout: \"better on "
             "dosimetry\" and \"better on clinical outcomes\" are always "
             "written separately and never stand in for one another; "
             "every figure carries the population, the side and the technique "
             "it came from; and deep inspiration breath-hold is a posture "
             "rather than a machine, so it can be added to any photon "
             "technique, which is why the choice of technique is written as a "
             "question of indication rather than of budget. Among the "
             "techniques compared here, the more expensive ones have a "
             "self-paid component and are delivered in my own department, so "
             "every article opens with the same declaration of interest; on "
             "cost I cite the official schedule where one exists and tell you "
             "to ask the medical affairs office where it does not. Every "
             "article links its primary sources, and where the evidence is "
             "weak I say so plainly.",
    "closing": "This is general patient education and does not replace a "
               "consultation. The volume, the number of treatments and the "
               "technique depend at the same time on the type of operation, "
               "the pathology report and the systemic treatment plan; the same "
               "stage leads to different advice in different people, so "
               "decisions about your own treatment belong with your physician "
               "and the multidisciplinary team.",
}
