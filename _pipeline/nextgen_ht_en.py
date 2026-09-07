# -*- coding: utf-8 -*-
"""English side of the next-generation topic, now including the hyperthermia group."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(HERE, "hubbuild/meta-en.json"), encoding="utf-8") as _fh:
    _RAW = json.load(_fh)
EN = {k[len("nt-"):]: v for k, v in _RAW.items()}

SECTIONS_EN = [
 {"en": "Read these two first",
  "stepsub_en": "A ruler for judging any new treatment, and a map of regulatory status — the four articles that follow are built on these two."},
 {"en": "The four technologies",
  "stepsub_en": "Each is put through the same six questions: what it changes, how far the evidence has climbed, whose data, what status it holds, what it costs, and when it is reasonable."},
 {"en": "Hyperthermia: getting oriented",
  "stepsub_en": "Five different treatments share one name, the idea is a hundred years old, and the evidence needs its own ruler. Start here."},
 {"en": "Hyperthermia: how it works",
  "stepsub_en": "It does not kill cancer cells itself. It blocks repair, improves oxygenation, and helps drugs get in — and none of it happens unless the temperature is reached."},
 {"en": "Hyperthermia: devices and thermometry",
  "stepsub_en": "Depth, measurement and quality assurance. Also the device class that does not claim to work by temperature at all, and who should not have this treatment."},
 {"en": "Hyperthermia: the evidence, site by site",
  "stepsub_en": "Six cancer sites, each answered with the same six questions — study design, denominator, endpoint, and whether standard treatment has moved since."},
 {"en": "Hyperthermia with immunotherapy and cell therapy",
  "stepsub_en": "The most persuasive story in the field and the thinnest evidence. Both articles carry more warnings than conclusions."},
 {"en": "Hyperthermia: closing",
  "stepsub_en": "What to ask in Taiwan, and the one combination I am researching myself — which is a research question, not yet a treatment."},
]

HUB = {
 "title": "Next-Generation Therapy Guide | Protons, carbon ions, FLASH, BNCT and hyperthermia — where the evidence stands, regulatory status, costs | Dr. Robert J.-Y. Wu",
 "desc": "Twenty-six articles on next-generation cancer treatment: a ruler for judging any new therapy, why approved, covered and effective are three different things, what proton precision actually buys, why heavier carbon ions are not automatically better, why FLASH is still in phase 1, where BNCT's selectivity stops — and a twenty-article group on hyperthermia: the mechanism, thermal dose and thermometry, the evidence site by site, the combinations with immunotherapy and cell therapy, and proton plus hyperthermia. Most are self-pay; every article carries its verification date and links its primary sources.",
 "sub": "New ways of treating, and how far each has actually come — the evidence is thin because it is new, except where it is old.",
 "intro": "This topic is different from the others on this site. The disease guides follow a patient's timeline; this one collects the names you will meet in the news and in advertising — protons, carbon ions, FLASH, BNCT, and now hyperthermia. Most of them are self-pay and most sit outside standard treatment. Every article is put through the same questions: what it changes, how far the evidence has climbed, whose data, what status it holds here and abroad, what it costs, and when it is reasonable. Read the first two articles before anything else — they are the ruler the rest of the topic uses. The hyperthermia group has its own ruler in its third article, because its evidence is a different shape: it has randomised trials, and they are forty years old. This topic dates faster than the others, so every article carries its verification date.",
 "closing": "This is general patient education and cannot replace a face-to-face consultation. Whether any of these technologies suits you depends heavily on the cancer, the stage, previous treatment and your general condition, and both the evidence and the regulatory position change quickly. Discuss any actual decision with your treating doctor and the multidisciplinary team, and check the verification date on the article.",
}
