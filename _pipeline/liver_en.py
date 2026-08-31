# -*- coding: utf-8 -*-
"""English side of the liver-cancer topic: section names, hub copy,
per-article metadata.  The article metadata is read from the four finished
English metadata files (one per SPEC group, in reading order) rather than
restated here; keys there carry the lv- prefix, the builder's slugs do not,
so they are remapped in liver.py.  Titles are the canonical SPEC-EN section 3
titles, verbatim."""

import json

META_EN = ["/home/claude/liver/meta/%s-en.json" % g for g in "ABCD"]

_RAW = {}
for _p in META_EN:
    with open(_p, encoding="utf-8") as _fh:
        _RAW.update(json.load(_fh))

EN = {k[len("lv-"):]: v for k, v in _RAW.items()}

SECTIONS_EN = [
    {
        "en": "After the Diagnosis",
        "stepsub_en": "Why a biopsy is often unnecessary, why liver function "
                      "is the currency, which box the staging chart puts you "
                      "in — the first five questions after diagnosis.",
    },
    {
        "en": "How Treatment Is Decided",
        "stepsub_en": "Surgery, ablation, radiation, transplant, embolisation "
                      "— how the roads divide the work; these five articles "
                      "are where you genuinely have a say.",
    },
    {
        "en": "During Treatment",
        "stepsub_en": "The two weeks of SBRT, life on targeted therapy and "
                      "immunotherapy, the days around TACE, and which "
                      "situations mean returning the same day.",
    },
    {
        "en": "After Treatment",
        "stepsub_en": "How follow-up is scheduled, the road after recurrence, "
                      "a liver that needs care for life, life after "
                      "transplant, and the days on the waiting list.",
    },
]

HUB = {
    "title": "Liver Cancer Guide | Diagnosis without a biopsy, cancer and "
             "cirrhosis, surgery, ablation or radiation, transplant, TACE, "
             "SBRT and protons | Dr. Robert J.-Y. Wu",
    "desc": "Twenty things patients with liver cancer need to know: why the "
            "diagnosis often needs no biopsy, why you have two diseases — "
            "the cancer and the cirrhosis, where the BCLC staging chart puts "
            "you, why the hepatitis B and C antivirals matter more now, how "
            "the first month unfolds, the three roads for a small liver "
            "cancer, why SBRT works in the liver and when it is the wrong "
            "answer, protons and where the trials stand, transplantation, "
            "TACE and Y-90, what the two weeks of SBRT actually look like, "
            "when to come back the same day, life on targeted therapy and "
            "immunotherapy, albumin, muscle and what to eat, the days before "
            "and after TACE, follow-up and AFP, the road after recurrence, "
            "lifelong care of the liver, life after a transplant, and the "
            "days on the waiting list. Every article links its primary "
            "sources.",
    "sub": "From the day of diagnosis to years after treatment ends — one "
           "question per article.",
    "intro": "What sets liver cancer apart is that you usually have two "
             "diseases at once: the cancer, and the cirrhosis underneath it "
             "— every step of treatment is paid for in liver function. These "
             "twenty articles follow the order you will actually live "
             "through: after the diagnosis, how treatment is decided, care "
             "during treatment, and what comes after it ends. My position "
             "first: stereotactic body radiotherapy and proton therapy are "
             "the treatments I deliver every day, and much of that work is "
             "self-paid; the other side of every comparison in this guide is "
             "my colleagues' surgery and ablation. So every sentence about "
             "radiotherapy here is written more conservatively than anyone "
             "else would write it — for patients fit for surgery with good "
             "liver function, resection remains the default. Every article "
             "links its primary sources, and where the evidence is weak I "
             "say so plainly.",
    "closing": "This is general patient education and does not replace a "
               "consultation. Treatment for liver cancer depends on the "
               "tumour and on liver function at the same time; the same "
               "stage leads to different advice in different people, so "
               "decisions about your own treatment belong with your "
               "physician and the multidisciplinary team.",
}
