# -*- coding: utf-8 -*-
"""English side of the colon-cancer topic: section names, hub copy, per-article
metadata.  The article metadata is read from the finished English metadata file
rather than restated here."""

import json
import os

META_EN = "/home/claude/colon/meta/all-en.json"

with open(META_EN, encoding="utf-8") as _fh:
    EN = json.load(_fh)

SECTIONS_EN = [
    {
        "en": "After the Diagnosis",
        "stepsub_en": "What the weeks between the report and the finished treatment "
                      "plan are deciding, and which of them cannot be skipped.",
    },
    {
        "en": "How Treatment Is Decided",
        "stepsub_en": "How much is taken out, whether chemotherapy is worth it and "
                      "for how long — these four are where you actually have a say.",
    },
    {
        "en": "During Treatment",
        "stepsub_en": "What the days look like once treatment has started, and which "
                      "symptoms mean phoning the same day.",
    },
    {
        "en": "After Treatment",
        "stepsub_en": "How follow-up is scheduled, what can still be done if it comes "
                      "back, and one thing a randomised trial has actually shown to work.",
    },
]

HUB = {
    "title": "Colon Cancer Guide | Staging reports, chemotherapy decisions, "
             "side-effect care and follow-up | Dr. Robert J.-Y. Wu",
    "desc": "Sixteen things patients with colon cancer need to know: whether a "
            "malignant polyp needs completion surgery, where T3N1 on the report comes "
            "from, which findings in the gene report are inherited, what the lymph node "
            "count decides, whether stage II needs chemotherapy, three months or six, "
            "who immunotherapy is for, when to report numb hands and feet, how to watch "
            "oral chemotherapy at home, bowel recovery and stoma, how intensive "
            "follow-up should be, ctDNA, whether metastatic disease can still be cured, "
            "and exercise after treatment. Every article links its primary sources.",
    "sub": "From the day of diagnosis to years after treatment ends — one question "
           "per article.",
    "intro": "Patients with colon cancer usually arrive in clinic with the same three "
             "questions: do I have to have chemotherapy, will I end up with a bag, and "
             "if it has already spread is that the end of it. These sixteen articles "
             "grow out of those three, in the order you will actually live through "
             "them: after the diagnosis, how treatment is decided, care during "
             "treatment, and then what happens once it ends. Every article links its "
             "primary sources, and where the evidence is weak I say so rather than "
             "rounding it up. The treatment logic of rectal cancer is different from "
             "that of colon cancer; for that, see the "
             "<a href=\"rc-en.html\">Rectal Cancer Guide</a>.",
    "closing": "This is general patient education and does not replace a consultation. "
               "Treatment for colon cancer depends heavily on the stage, on the risk "
               "features written on the pathology report and on your own condition; the "
               "same stage leads to different advice in different people, so decisions "
               "about your own treatment belong with your physician and the "
               "multidisciplinary team.",
}
