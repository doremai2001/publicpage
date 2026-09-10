# -*- coding: utf-8 -*-
"""English side of the endometrial-cancer topic.

SECTIONS_EN[i]["en"] is load-bearing on BOTH languages: topicbuild derives
every article's kicker from SECTIONS_EN[i]["en"].upper() regardless of the
language being built.  The four group names are the ones agreed for the
topic (Diagnosis and staging / Treatment and the evidence / Special
situations / After treatment).

Article titles are verbatim from SPEC-EN.md section 3 by way of
meta/{A,B,C,D}-en.json, which are keyed "em-<slug>"; EN is re-keyed on the
unprefixed tail because topicbuild composes "<PREFIX>-<slug>.html".

British spelling throughout (lymphoedema, randomised, gynaecological), as on
the rest of the site's English pages.
"""

import json

# Group names -> article kickers (shared with the zh build; do not retitle).
SECTIONS_EN = [
    {
        "en": "Diagnosis and staging",
        "stepsub_en": "Why bleeding after the menopause cannot be waited "
                      "out, how the four molecular groups are told apart, "
                      "what FIGO 2023 changed and what it did not, and what "
                      "the operation removes and does to the lymph nodes.",
        "slugs": ["bleeding", "two-kinds", "staging-2023", "surgery"],
    },
    {
        "en": "Treatment and the evidence",
        "stepsub_en": "Whether radiotherapy is still needed after the "
                      "operation, what the vault-only kind actually "
                      "involves, what adding chemotherapy buys and costs, "
                      "how molecular classification changes those decisions, "
                      "and who immunotherapy really helps.",
        "slugs": ["adjuvant", "vaginal-brachy", "chemo-rt",
                  "molecular-adjuvant", "immuno"],
    },
    {
        "en": "Special situations",
        "stepsub_en": "What it takes to keep the uterus and have a child, "
                      "how much weight and diabetes actually account for, "
                      "what a Lynch result means for you and your family, "
                      "and the hormone question after treatment.",
        "slugs": ["fertility", "obesity", "lynch", "hormone-after"],
    },
    {
        "en": "After treatment",
        "stepsub_en": "How follow-up is scheduled and what it is and is not "
                      "good for, whether a recurrence can still be treated, "
                      "preventing and managing lower-limb lymphoedema, and "
                      "getting daily life back.",
        "slugs": ["followup", "recurrence", "lymphedema", "daily"],
    },
]

# Article metadata, titles verbatim from SPEC-EN.md section 3.
EN = {}
for _g in "ABCD":
    with open("/home/claude/endo/meta/%s-en.json" % _g, encoding="utf-8") as _fh:
        for _k, _rec in json.load(_fh).items():
            EN[_k[len("em-"):]] = _rec

HUB = {
    "title": "Endometrial Cancer Guide | Bleeding after the menopause, the "
             "four molecular groups, FIGO 2023, radiotherapy after surgery, "
             "brachytherapy, chemotherapy, immunotherapy, keeping the uterus "
             "and life afterwards | Dr. Robert J.-Y. Wu",
    "desc": "Seventeen articles on endometrial cancer: why bleeding after "
            "the menopause is not something to wait out and what the one "
            "clinic test settles, why two kinds of endometrial cancer are "
            "now four molecular groups, what FIGO 2023 changed and why your "
            "treatment does not change with it, what the operation removes "
            "and what happens to the lymph nodes, whether you still need "
            "radiotherapy after the operation and what PORTEC-1 really "
            "showed, what vaginal brachytherapy actually involves, what "
            "adding chemotherapy buys and what it costs, how molecular "
            "classification is changing adjuvant treatment, who "
            "immunotherapy actually helps by MMR status, what it takes to "
            "keep the uterus and have a child, what weight and diabetes do "
            "and do not explain, what a Lynch syndrome result means for you "
            "and your family, hormones after treatment, how follow-up is "
            "scheduled, whether a recurrence can still be treated, "
            "lower-limb lymphoedema, and life after treatment. Every "
            "article links its primary sources.",
    "sub": "From the pathology report to years after treatment — one "
           "question per article.",
    "intro": "Most people with endometrial cancer will be well, and that "
             "has to be said plainly — but it must never turn into \"so it "
             "hardly matters what you do\". The two things that do the most "
             "harm in this cancer are overtreatment and delay: on one side "
             "a low-risk woman irradiated for no gain (PORTEC-1's "
             "complications, 25% against 6%), on the other a woman who bled "
             "for six months before coming in. These seventeen articles "
             "follow the order you will actually walk: diagnosis and "
             "staging, treatment and the evidence, the situations that need "
             "their own answer, and what comes after. My position first: "
             "vaginal brachytherapy and pelvic radiotherapy are the part I "
             "deliver myself, and the other side of every comparison here "
             "is my gynaecological-oncology colleagues' surgery and my "
             "gynaecological-oncology and medical-oncology colleagues' "
             "drugs — so the four articles that compare them open with the "
             "same declaration of interest, and every comparison carries "
             "its primary source so you can take it back to the "
             "gynaecological oncology clinic for a second opinion. Note the "
             "order in this cancer: surgery usually comes first, and the "
             "decision that matters is made afterwards, with the pathology "
             "report in your hand. Where the evidence is weak I say so "
             "plainly, and where a number could not be found I say that too.",
    "closing": "This is general patient education and does not replace a "
               "consultation. Treatment for endometrial cancer depends at "
               "the same time on histology, grade, stage, molecular group "
               "and what the operation found, and the same stage leads to "
               "different recommendations in different people; decisions "
               "about your own treatment belong with your gynaecological "
               "oncologist and the multidisciplinary team.",
}
