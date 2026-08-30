# -*- coding: utf-8 -*-
"""English side of the breast-cancer topic: section names, hub copy, per-article
metadata.  The article metadata is read from the finished English metadata file
rather than restated here."""

import json

META_EN = "/home/claude/breast/meta/all-en.json"

with open(META_EN, encoding="utf-8") as _fh:
    EN = json.load(_fh)

SECTIONS_EN = [
    {
        "en": "After the Diagnosis",
        "stepsub_en": "What the weeks between the report coming back and the "
                      "treatment plan being settled are deciding, and which lines "
                      "on the report actually carry weight.",
    },
    {
        "en": "How Treatment Is Decided",
        "stepsub_en": "How much is taken out, whether chemotherapy is needed, how "
                      "the drugs are ordered and for how many years — these six are "
                      "where you actually have a say.",
    },
    {
        "en": "During Treatment",
        "stepsub_en": "How many radiotherapy sessions there are, which side effects "
                      "mean phoning the same day, and the things that genuinely make "
                      "treatment hard to keep taking.",
    },
    {
        "en": "After Treatment",
        "stepsub_en": "How follow-up is scheduled, whether the arm will swell, how "
                      "to look after your bones, and two articles on what happens "
                      "once it has spread.",
    },
]

HUB = {
    "title": "Breast Cancer Guide | Receptor reports, chemotherapy decisions, "
             "radiotherapy and endocrine therapy, follow-up and recurrence | "
             "Dr. Robert J.-Y. Wu",
    "desc": "Twenty-four things patients with breast cancer need to know: what the "
            "first month is waiting for, which lines of the receptor report matter, "
            "how the three subtypes split, what each kind of genetic test is actually "
            "meant to prove, breast conservation versus mastectomy, the sentinel node, "
            "chemotherapy before surgery, the 21-gene score, how HER2 treatment is "
            "sequenced, how many years the endocrine tablets run, how many "
            "radiotherapy sessions, which side effects mean phoning the same day, "
            "fertility preservation, how follow-up is scheduled, lymphoedema, bone "
            "health, self-pay options and trials, and what happens once it has spread. "
            "Every article links its primary sources.",
    "sub": "From the day of diagnosis to years after treatment ends — one question "
           "per article.",
    "intro": "Patients with breast cancer arrive in clinic carrying the same heavy "
             "questions: will I lose my breast, do I have to have chemotherapy, will "
             "it come back, how many years do I have to stay on the tablets. These "
             "twenty-four articles grow out of those questions, in the order you will "
             "actually live through them: after the diagnosis, how treatment is "
             "decided, care during treatment, and then what happens once it ends. I "
             "have given genetic testing five articles of its own, because when a "
             "patient hears the words \"genetic testing\" one thing comes to mind, "
             "while in the clinic it is three quite different things: one is meant to "
             "prove that you can be spared chemotherapy, one is looking for a drug "
             "that can be used, and one measures the risk you and your family were "
             "born with. Every article links its primary sources, and where the "
             "evidence is weak I say so rather than rounding it up.",
    "closing": "This is general patient education and does not replace a "
               "consultation. Treatment for breast cancer depends heavily on the "
               "subtype, on the stage and on your own condition; the same stage leads "
               "to completely different advice in people with different subtypes, so "
               "decisions about your own treatment belong with your physician and the "
               "multidisciplinary team.",
}
