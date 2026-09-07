# -*- coding: utf-8 -*-
"""English side of the glioblastoma topic.

SECTIONS_EN[i]["en"] is load-bearing on BOTH languages: topicbuild derives
every article's kicker from SECTIONS_EN[i]["en"].upper() regardless of the
language being built.  The four group names are the ones agreed for the
topic (After the Diagnosis / What the Evidence Says / During Treatment /
Afterwards).

Article titles are verbatim from SPEC-EN.md section 3 by way of
meta/{A,B,C,D}-en.json, which are keyed "gb-<slug>"; EN is re-keyed on the
unprefixed tail because topicbuild composes "<PREFIX>-<slug>.html" and the
PREFIX is gb (the hub, however, is gbm-en.html -- see gbm.py).

British spelling throughout (tumour, randomised, centre), as on the rest of
the site's English pages.
"""

import json

# Group names -> article kickers (shared with the zh build; do not retitle).
SECTIONS_EN = [
    {
        "en": "After the Diagnosis",
        "stepsub_en": "How that line on the report came to be written, the "
                      "order behind everything in the first few days, what "
                      "taking it all out actually means, what the two-week "
                      "wait for the report is waiting for, and the different "
                      "road an IDH-mutant report puts you on.",
        "slugs": ["what-it-is", "first-days", "surgery", "pathology",
                  "lowgrade"],
    },
    {
        "en": "What the Evidence Says",
        "stepsub_en": "How the six concurrent weeks and the six maintenance "
                      "cycles are actually taken, what the MGMT line decides, "
                      "when the course can be shortened, how to read that "
                      "number, and where each of the five new treatments "
                      "stands.",
        "slugs": ["standard", "mgmt", "elderly", "numbers", "newthings"],
    },
    {
        "en": "During Treatment",
        "stepsub_en": "What those six weeks of radiotherapy are really like, "
                      "how steroids have to come back down, anti-seizure "
                      "drugs and driving, and what cannot wait for the next "
                      "appointment.",
        "slugs": ["rt-weeks", "steroid", "seizure", "warning-signs"],
    },
    {
        "en": "Afterwards",
        "stepsub_en": "How the follow-up scans are scheduled and why bigger "
                      "is not always worse, what lies behind the changes in "
                      "memory and in who he is, and the roads that remain "
                      "after recurrence.",
        "slugs": ["followup", "cognition", "recurrence"],
    },
]

# Article metadata, titles verbatim from SPEC-EN.md section 3.
EN = {}
for _g in "ABCD":
    with open("/home/claude/gbm/meta/%s-en.json" % _g, encoding="utf-8") as _fh:
        for _k, _rec in json.load(_fh).items():
            EN[_k[len("gb-"):]] = _rec

HUB = {
    "title": "Glioblastoma Guide | That line on the report, how much is left "
             "after surgery, six weeks and six cycles, MGMT, that number, "
             "fields and what is new | Dr. Robert J.-Y. Wu",
    "desc": "Seventeen articles on glioblastoma: how the 2021 classification "
            "decides whether the name is glioblastoma at all, the order "
            "behind the first few days after they find it, why taking it all "
            "out is really about how much is left on the postoperative scan, "
            "what the two-week wait for the pathology report is waiting for, "
            "why an IDH-mutant report puts you on a different road, how the "
            "six concurrent weeks and the six maintenance cycles are actually "
            "taken, what the MGMT line decides and what it does not, when "
            "being older or less strong means the course can be shortened, "
            "how to read that survival number and the denominator behind each "
            "figure on the tail, where tumour-treating fields, immunotherapy, "
            "vaccines, protons and BNCT each stand, what those six weeks of "
            "radiotherapy are actually like, how steroids come back down, "
            "anti-seizure drugs and driving, when to come back the same day, "
            "how the follow-up scans are scheduled and why bigger is not "
            "always worse, memory, concentration and changes in who he is, "
            "and what roads remain after recurrence. Every article links its "
            "primary sources.",
    "sub": "From that line on the pathology report to what comes after "
           "treatment — one question per article.",
    "intro": "This is the worst prognosis of any cancer on this site, so it "
             "is written differently from the other guides: no comfort taken "
             "from saying there are still plenty of roads, and no median "
             "survival handed to you as a deadline — that number was not "
             "calculated for you alone. These seventeen articles follow the "
             "order you will actually walk: the diagnosis and the "
             "classification, what the evidence says for each treatment, care "
             "during the course, and what comes afterwards. My position "
             "first: the radiotherapy part of glioblastoma treatment is the "
             "part I do myself, and the other side of every comparison here "
             "is my neurosurgical colleagues' operation and my neuro-oncology "
             "colleagues' drugs; tumour-treating fields I do not use, and "
             "they are not a service of my department — so the four articles "
             "that weigh radiotherapy against surgery and drugs all open with "
             "the same declaration of interest. Every article links its "
             "primary sources: negative trials are written as negative, weak "
             "evidence is called weak, and where a number could not be found "
             "I say that too.",
    "closing": "This is general patient education and does not replace a "
               "consultation. Treatment for glioblastoma depends at the same "
               "time on the molecular subtype, the residual volume left after "
               "surgery, age, performance status and neurological function, "
               "and the same diagnosis leads to different recommendations in "
               "different people; decisions about your own treatment belong "
               "with your physician and the multidisciplinary team.",
}
