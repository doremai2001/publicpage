# -*- coding: utf-8 -*-
"""English side of the bladder-cancer topic.

SECTIONS_EN[i]["en"] is load-bearing on BOTH languages: topicbuild derives
every article's kicker from SECTIONS_EN[i]["en"].upper() regardless of the
language being built.  The five group names are the ones agreed for the
topic (Diagnosis and staging / Non-muscle-invasive / Muscle-invasive: two
roads / Metastatic and systemic therapy / Taiwan, and afterwards).

Article titles are verbatim from SPEC-EN.md section 4 by way of
meta/{A,B,C,D,E}-en.json, which are keyed "bl-<slug>"; EN is re-keyed on the
unprefixed tail because topicbuild composes "<PREFIX>-<slug>.html".

British spelling throughout (tumour, randomised, favourable, catheterisation),
as on the rest of the site's English pages.
"""

import json

# Group names -> article kickers (shared with the zh build; do not retitle).
SECTIONS_EN = [
    {
        "en": "Diagnosis and staging",
        "stepsub_en": "What painless blood in the urine means and what the "
                      "first round of tests is, why the first resection "
                      "decides everything after it, what Ta, T1 and CIS are, "
                      "and what staging can and cannot see.",
        "slugs": ["hematuria", "turbt", "report", "staging"],
    },
    {
        "en": "Non-muscle-invasive",
        "stepsub_en": "What decides whether you get instillations at all, "
                      "what BCG actually is and what it is not, what follows "
                      "when it stops working, and how long the cystoscopies "
                      "go on.",
        "slugs": ["nmibc-risk", "bcg", "bcg-fail", "nmibc-followup"],
    },
    {
        "en": "Muscle-invasive: two roads",
        "stepsub_en": "Removing the bladder or keeping it and what the "
                      "evidence for that comparison really is, why "
                      "chemotherapy comes first, what the operation and the "
                      "three diversions cost, how trimodality therapy is "
                      "done and who it suits, and what the bladder you kept "
                      "needs afterwards.",
        "slugs": ["two-roads", "neoadjuvant", "cystectomy", "tmt",
                  "tmt-after"],
    },
    {
        "en": "Metastatic and systemic therapy",
        "stepsub_en": "What first-line treatment is now, where the licence "
                      "and the reimbursement part company in Taiwan, and "
                      "which biomarker cell actually has a drug in it.",
        "slugs": ["metastatic", "biomarker"],
    },
    {
        "en": "Taiwan, and afterwards",
        "stepsub_en": "Why so much of Taiwan's urothelial cancer grows in "
                      "the upper tract and what the aristolochic acid "
                      "evidence does and does not say, smoking and this "
                      "disease without a word of blame, and getting back to "
                      "your days with a stoma or a neobladder.",
        "slugs": ["utuc", "smoking", "daily"],
    },
]

# Article metadata, titles verbatim from SPEC-EN.md section 4.
EN = {}
for _g in "ABCDE":
    with open("/home/claude/bl/meta/%s-en.json" % _g, encoding="utf-8") as _fh:
        for _k, _rec in json.load(_fh).items():
            EN[_k[len("bl-"):]] = _rec

HUB = {
    "title": "Bladder Cancer Guide | Painless blood in the urine, Ta and T1 "
             "and CIS, BCG, removing the bladder or keeping it, trimodality "
             "therapy, the upper tract, and getting your days back "
             "| Dr. Robert J.-Y. Wu",
    "desc": "Eighteen articles on bladder cancer: why painless visible blood "
            "in the urine is the kind that gets investigated and what the "
            "first round of tests is, why the first resection decides "
            "everything after it, what Ta, T1 and CIS mean and why the line "
            "between non-muscle-invasive and muscle-invasive disease is the "
            "hardest line in this cancer, what risk stratification decides, "
            "what BCG actually is and what the shortage means, what follows "
            "when BCG stops working, how long the cystoscopies go on, "
            "removing the bladder against keeping it and what the evidence "
            "for that comparison really is, why chemotherapy comes before "
            "the operation, what cystectomy and the three urinary "
            "diversions cost, how trimodality therapy is done and who it "
            "suits, what the preserved bladder needs afterwards, "
            "first-line treatment after it has spread and where Taiwan's "
            "licence and reimbursement part company, which biomarker cell "
            "actually has a drug in it, why so much of Taiwan's urothelial "
            "cancer grows in the upper tract, smoking, and life with a "
            "stoma or a neobladder. Every article links its primary sources.",
    "sub": "From the first drop of blood in the urine to the years of "
           "follow-up afterwards — one question per article.",
    "intro": "Two lines run through this whole guide, and almost every "
             "mistake made about bladder cancer is a number that crossed "
             "one of them. The first is between non-muscle-invasive disease "
             "— Ta, T1, carcinoma in situ — and muscle-invasive disease from "
             "T2 up: the treatments, the outlook and the follow-up are not "
             "shared, and a survival figure quoted without saying which side "
             "it belongs to is wrong even when the arithmetic is right. The "
             "second is between the bladder and the upper tract, the renal "
             "pelvis and ureter: the same cells under the microscope, "
             "different surgery, different follow-up, and in Taiwan a "
             "completely different epidemiology. So every number here "
             "carries its side, and the word \"superficial\" — which the "
             "European guideline explicitly tells us not to use — does not "
             "appear. My position first: the radiotherapy inside trimodality "
             "therapy is the part I deliver myself, and this guide argues "
             "that Taiwan under-uses bladder preservation, which is an "
             "argument that suits me. Three of these articles open with that "
             "declaration of interest, every comparison carries its primary "
             "source, and I have written down what bladder preservation "
             "cannot do as well as what it can — including that there is no "
             "successfully completed randomised trial comparing it with "
             "removing the bladder, and that about one in five people who "
             "keep their bladder lose it later anyway. Where the evidence is "
             "weak I say so, and where a number could not be found I say "
             "that too.",
    "closing": "This is general patient education and does not replace a "
               "consultation. What to do about bladder cancer depends at the "
               "same time on whether the tumour invades muscle, its grade, "
               "whether carcinoma in situ is present, whether there is "
               "hydronephrosis, how completely the first resection was done "
               "and whether it contained detrusor muscle, your kidney "
               "function and your health as a whole; the same report leads "
               "to different recommendations in different people. Decisions "
               "about your own treatment belong with your urologist, your "
               "radiation oncologist, your medical oncologist and the "
               "multidisciplinary team.",
}
