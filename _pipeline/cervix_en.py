# -*- coding: utf-8 -*-
"""English side of the cervical-cancer topic: section names, hub copy,
per-article metadata.  The article metadata is read from the finished English
metadata file rather than restated here; keys there carry the cx- prefix, the
builder's slugs do not, so they are remapped in cervix.py."""

import json

META_EN = "/home/claude/cervix/meta/all-en.json"

with open(META_EN, encoding="utf-8") as _fh:
    _RAW = json.load(_fh)

EN = {k[len("cx-"):]: v for k, v in _RAW.items()}

SECTIONS_EN = [
    {
        "en": "After the Diagnosis",
        "stepsub_en": "The words on the report, how the stage is assigned, "
                      "and the heaviest question of all — who gave this to me.",
    },
    {
        "en": "How Treatment Is Decided",
        "stepsub_en": "Surgery or radiotherapy, why chemotherapy is added, "
                      "the fertility window — these four articles are where "
                      "you genuinely have a say.",
    },
    {
        "en": "During Treatment",
        "stepsub_en": "The brachytherapy days, how the five to six weeks go, "
                      "and which situations mean phoning the same day.",
    },
    {
        "en": "After Treatment",
        "stepsub_en": "Menopause, sex, follow-up — and the road after "
                      "recurrence.",
    },
]

HUB = {
    "title": "Cervical Cancer Guide | CIN and staging, surgery or "
             "radiotherapy, brachytherapy, HPV and follow-up | "
             "Dr. Robert J.-Y. Wu",
    "desc": "Sixteen things patients with cervical cancer need to know: how "
            "an abnormal smear differs from cancer, how the stage is "
            "assigned, the question that weighs most — who gave this to me, "
            "what the first month is for, surgery versus radiotherapy, why "
            "minimally invasive surgery hit the brakes, why chemotherapy is "
            "added to radiation, the fertility window, what brachytherapy "
            "actually is, how the five to six weeks of pelvic radiotherapy "
            "go, weekly cisplatin, vaginal care during treatment, "
            "treatment-induced menopause and hormone therapy, dilators and "
            "sex, follow-up and HPV testing, and the road after recurrence. "
            "Every article links its primary sources.",
    "sub": "From the day of diagnosis to years after treatment ends — one "
           "question per article.",
    "intro": "The three heaviest questions patients with cervical cancer "
             "bring to clinic are usually these: why is mine radiotherapy "
             "and not surgery, what exactly is brachytherapy, and the one "
             "that is hardest to say out loud — who gave this to me. These "
             "sixteen articles grew outward from those three questions, in "
             "the order you will actually live through: after the diagnosis, "
             "how treatment is decided, care during treatment, and then what "
             "comes after it ends. Definitive chemoradiation and "
             "brachytherapy are the treatments I deliver every day, so every "
             "sentence about radiotherapy in this guide is written more "
             "conservatively than anyone else would write it. Every article "
             "links its primary sources, and where the evidence is weak I "
             "say so plainly.",
    "closing": "This is general patient education and does not replace a "
               "consultation. Treatment for cervical cancer depends heavily "
               "on the stage, the size of the tumour and your own condition; "
               "the same stage leads to different advice in different "
               "people, so decisions about your own treatment belong with "
               "your physician and the multidisciplinary team.",
}
