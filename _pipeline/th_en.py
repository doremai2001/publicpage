# -*- coding: utf-8 -*-
"""English side of the thyroid-cancer topic.

SECTIONS_EN[i]["en"] is load-bearing on BOTH languages: topicbuild derives
every article's kicker from SECTIONS_EN[i]["en"].upper() regardless of the
language being built.  The five group names are the ones agreed for the
topic (Diagnosis and staging / The low-risk box: how aggressive to be /
Radioiodine / Follow-up and beyond / Two other diseases, and Taiwan).

Article titles are verbatim from SPEC-EN.md section 4 by way of
meta/{A,B,C,D,E}-en.json, which are keyed "th-<slug>"; EN is re-keyed on the
unprefixed tail because topicbuild composes "<PREFIX>-<slug>.html".

British spelling throughout (tumour, randomised, anaesthetic, oesophagus),
as on the rest of the site's English pages.
"""

import json

# Group names -> article kickers (shared with the zh build; do not retitle).
SECTIONS_EN = [
    {
        "en": "Diagnosis and staging",
        "stepsub_en": "What a suspicious nodule on an ultrasound actually "
                      "means and whether it needs a needle, what the number "
                      "on the fine-needle report is, how to read papillary "
                      "and follicular and NIFTP, why the stage depends on "
                      "your age, and why there is suddenly so much of this "
                      "cancer.",
        "slugs": ["nodule", "fna", "pathology", "staging", "overdiagnosis"],
    },
    {
        "en": "The low-risk box: how aggressive to be",
        "stepsub_en": "Watching a small cancer instead of operating and the "
                      "conditions that come with it, half the gland against "
                      "all of it, whether the nodes should come out too, and "
                      "what the operation takes with it.",
        "slugs": ["active-surveillance", "lobectomy", "neck-dissection",
                  "surgery-risks"],
    },
    {
        "en": "Radioiodine",
        "stepsub_en": "What four de-escalation trials did and did not show "
                      "about who still needs radioiodine, and what those few "
                      "days are actually like.",
        "slugs": ["rai-whether", "rai-days"],
    },
    {
        "en": "Follow-up and beyond",
        "stepsub_en": "How much of the tablet you take for life, what "
                      "follow-up is looking at, what a rising thyroglobulin "
                      "with nothing on the scan means, what follows when "
                      "radioiodine stops working, and where external beam "
                      "radiotherapy sits in all this.",
        "slugs": ["tsh", "followup", "recurrence", "rai-refractory", "ebrt"],
    },
    {
        "en": "Two other diseases, and Taiwan",
        "stepsub_en": "Medullary cancer and the genetics that come with it, "
                      "anaplastic cancer and why it is an emergency, the "
                      "scar and the voice and the weight and going back to "
                      "work, and how the whole path runs in Taiwan.",
        "slugs": ["mtc", "atc", "daily", "taiwan"],
    },
]

# Article metadata, titles verbatim from SPEC-EN.md section 4.
EN = {}
for _g in "ABCDE":
    with open("/home/claude/th/meta/%s-en.json" % _g, encoding="utf-8") as _fh:
        for _k, _rec in json.load(_fh).items():
            EN[_k[len("th-"):]] = _rec

HUB = {
    "title": "Thyroid Cancer Guide | A nodule on a scan, the Bethesda "
             "number, watching instead of operating, half the gland or all "
             "of it, radioiodine, the tablet for life, and how this goes in "
             "Taiwan | Dr. Robert J.-Y. Wu",
    "desc": "Twenty articles on thyroid cancer: what a suspicious nodule on "
            "an ultrasound means and why four risk-stratification systems "
            "disagree about the same nodule, what the number on your "
            "fine-needle report is, how to read papillary and follicular "
            "and NIFTP, why the stage depends on your age and why staging "
            "and recurrence risk are two different systems, why there is "
            "suddenly so much of this cancer and what overdiagnosis does "
            "and does not mean for you, watching a small cancer instead of "
            "operating and the conditions that come with it, half the gland "
            "against all of it, whether the nodes should come out too, what "
            "the operation takes with it, whether to have radioiodine and "
            "what those few days are like, how much of the tablet you take "
            "for life and what it costs, what follow-up is looking at, a "
            "rising thyroglobulin with nothing on the scan, what follows "
            "when radioiodine stops working, where external beam "
            "radiotherapy sits, medullary and anaplastic cancer as separate "
            "diseases, the scar and the voice and the work, and how the "
            "whole path runs in Taiwan. Every article links its primary "
            "sources.",
    "sub": "From the nodule someone found by accident to the years of "
           "follow-up afterwards — one question per article.",
    "intro": "Most people reading this were told they had cancer while "
             "feeling perfectly well: an ultrasound at a health check found "
             "something, or a hand found a painless lump. So the first "
             "question is not how long anyone has left. It is whether this "
             "counts as anything at all — and that question can go wrong in "
             "two opposite directions. Downwards, into \"thyroid cancer is "
             "the good kind\", which is how people stop coming back for "
             "follow-up, and which lands very badly on the ones who turn out "
             "to be in the high-risk box. Upwards, into reading the word "
             "cancer as an instruction to remove the whole gland, have "
             "radioiodine and suppress TSH for life — which is how people "
             "end up with an operation, a dose of radiation and a tablet "
             "they never needed. The work of this guide is to put you in the "
             "right box and to be honest about what that box costs. So "
             "every number here carries its risk group, its age cut-off, its "
             "histology and its endpoint, and the phrases that comfort "
             "without informing are not used. My position first, in one "
             "place: external beam radiotherapy is the part of this I do "
             "myself, and the article about it concludes that almost nobody "
             "with differentiated thyroid cancer needs it. That declaration "
             "opens that one article. Where the evidence is weak I say so, "
             "and where a number could not be found I say that too.",
    "closing": "This is general patient education and does not replace a "
               "consultation. What to do about thyroid cancer depends at "
               "the same time on the histology and its subtype, the size of "
               "the tumour and whether it extends beyond the gland, the "
               "nodes, your age, what the ultrasound shows, your "
               "thyroglobulin and antibody status, and your health as a "
               "whole; the same report leads to different recommendations "
               "in different people. Doses, isolation rules and low-iodine "
               "diets follow your own hospital's nuclear medicine "
               "department, not this page. Decisions about your own "
               "treatment belong with your endocrinologist, your surgeon, "
               "your nuclear medicine physician and the multidisciplinary "
               "team.",
}
