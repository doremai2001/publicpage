# -*- coding: utf-8 -*-
"""English side of the next-generation-therapy topic: section names, hub copy,
per-article metadata.  The article metadata is read from the finished English
metadata file rather than restated here; keys there carry the nt- prefix, the
builder's slugs do not, so they are remapped in nextgen.py."""

import json

META_EN = "/home/claude/nextgen/meta/all-en.json"

with open(META_EN, encoding="utf-8") as _fh:
    _RAW = json.load(_fh)

EN = {k[len("nt-"):]: v for k, v in _RAW.items()}

SECTIONS_EN = [
    {
        "en": "Read these two first",
        "stepsub_en": "A ruler for judging any new treatment, and a map of "
                      "regulatory status — the four articles that follow are "
                      "built on these two.",
    },
    {
        "en": "The four technologies",
        "stepsub_en": "Each is put through the same six questions: what it "
                      "changes, how far the evidence has climbed, whose data, "
                      "what status it holds, what it costs, and when it is "
                      "reasonable.",
    },
]

HUB = {
    "title": "Next-Generation Therapy Guide | Protons, carbon ions, FLASH and "
             "BNCT — where the evidence stands, regulatory status, costs | "
             "Dr. Robert J.-Y. Wu",
    "desc": "Six things patients need to know about next-generation "
            "radiotherapy: a ruler for judging any new treatment (the evidence "
            "ladder and five practical tests), why approved, covered and "
            "effective are three different things, what proton precision "
            "actually buys, why heavier carbon ions are not automatically "
            "better, why FLASH is still in phase 1, and where BNCT's "
            "selectivity comes from — and where it stops. Most of these "
            "treatments are self-pay and the evidence is young, so every "
            "article carries its verification date and links its primary "
            "sources.",
    "sub": "New ways of treating, and how far each has actually come — the "
           "evidence is thin because it is new.",
    "intro": "This topic is different from the others on this site. The disease "
             "guides follow a patient's timeline; this one collects the names "
             "you will meet in the news and in advertising — protons, carbon "
             "ions, FLASH, BNCT, and in time cell therapy, hyperthermia "
             "combinations and histotripsy will join them. What they share is "
             "this: they are new, so the evidence is still thin, and most of "
             "them are paid out of pocket. So every article puts its subject "
             "through the same set of questions: what it changes, how far the "
             "evidence has climbed, what its status is in Taiwan and abroad, "
             "what it costs, and when it is reasonable. Read the first two "
             "articles first — they are the ruler every later article leans "
             "on. This topic goes out of date faster than the others, so every "
             "article carries its verification date.",
    "closing": "This is general patient education and does not replace a "
               "consultation. Whether a new technology is right for you "
               "depends heavily on the cancer type, the stage, previous "
               "treatment and your own condition, and both the evidence and "
               "the regulatory status change quickly; decisions about your own "
               "treatment belong with your physician and the multidisciplinary "
               "team, and check each article's verification date.",
}
