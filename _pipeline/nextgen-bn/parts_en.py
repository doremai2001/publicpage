# -*- coding: utf-8 -*-
"""BNCT 分組英文版共用區塊。兩則警語逐字沿用已上線的英文頁面，不得改寫。"""

WARN1 = ('<p><strong>Warning 1 (what this displaces):</strong> Most of the treatments in this topic are paid '
         'out of pocket, and most sit outside standard treatment. Before you decide, you need to know that '
         'what they displace is usually not time but three things of real value: <strong>standard treatment '
         'you have not yet used up, money you will need for later lines, and your eligibility for clinical '
         'trials</strong> (many trials exclude people who have recently received other experimental treatments). '
         'And there is one more, harder to see — physical reserve. The strength burnt through in a course that '
         'does not work may no longer be there when a genuinely useful option appears. So the question is not '
         'whether this is worth trying — it is <strong>what you give up by doing it</strong>.</p>')

WARN2 = ('<p><strong>Warning 2 (finding the right doctor):</strong> Do not make this kind of decision alone, '
         'and do not make it on the word of the person offering the treatment. The doctor you are looking for '
         'is one willing to tell you "this is not right for you" — <strong>if they never once say who this is '
         'NOT for, that is not a consultation, it is a sale.</strong></p>')

DISCLOSE = ('<p>My position first: proton therapy and hyperthermia are both technologies within my own field, '
            'and the hospital I work at has the equipment for them. BNCT is not — my hospital does not offer '
            'it and I do not deliver it. I have nothing to sell you in this section. You should know that, '
            'because it changes how you read every sentence I write here.</p>')

DATED = '<p>Facts checked: September 2026.</p>'

_SHARED = ('<p>BNCT is almost always used somewhere that has already been irradiated once, so it displaces one '
           'more thing that other self-paid treatments do not touch: <strong>your re-irradiation allowance</strong> '
           '— any one site can take only so much radiation in total, and what is spent does not come back. ')

_TAIL = {
 "principle": "The physics in this article is why that allowance cannot simply be added back up.",
 "dose": "And how much of it this one course uses, you cannot even calculate cleanly - which is what this article is about.",
 "depth": "Where the depth is wrong, that allowance buys particularly little.",
 "drugs": "How much it buys depends on how much boron your cells took up. That is the drug's business, not the machine's.",
 "pet": "The scan in this article is the one chance you get to estimate that before you spend it.",
 "newagents": "So waiting for a better boron drug is sometimes not delay, it is keeping the chip in your hand.",
 "thor": "The two routes in this article draw on the same allowance.",
 "accelerator": "The machine changed. The arithmetic of that allowance did not.",
 "headneck": "Most patients in this group have only this one left, so how it is spent matters more than usual.",
 "gbm": "In the brain that allowance is especially a one-off, and this article takes apart what it bought.",
 "newgbm": "You have not spent that allowance yet - which is exactly the reason not to spend it early.",
 "melanoma": "Skin lesions can usually still be irradiated a second time, so the squeeze here is lighter than elsewhere. That is only fair to say.",
 "meningioma": "This is the hard part of a rare cancer: when you spend it, no large trial is there to tell you whether it was worth it.",
 "others": "And this article is about the places where that allowance buys nothing at all.",
 "safety": "What happens when it is exceeded is what this whole article is about.",
 "approval": "Regulation will not judge whether that allowance should be spent. It only decides which door you go through.",
 "who": "The four conditions here are asking whether you should spend it at all.",
}

DISPLACE = {k: _SHARED + v + "</p>" for k, v in _TAIL.items()}


def assemble(slug, body):
    return "\n".join([WARN1, DISPLACE[slug], WARN2, DISCLOSE, body.strip(), DATED])
