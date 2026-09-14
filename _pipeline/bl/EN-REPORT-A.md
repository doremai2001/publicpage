# EN-REPORT-A — group A (bl-hematuria, bl-turbt, bl-report, bl-staging)

Third adversarial pass, produced while writing the English edition (2026-09-14).
**Nothing below was fixed in the English.** Every sentence listed was translated as
it stands in the Chinese master; the editor decides and fixes both languages together.

---

## A1 — `bl-hematuria`: a bladder-cancer five-year survival pair with no side of the line

**Section**: 〈女性這一格，同一份指引寫了兩件相反的事〉
**Sentence**: 「指引引用的存活落差是女性五年 73.3% 對男性 78.2%，措辭是「可能有一部分歸因於」診斷延遲」

**What is wrong.** This is a bladder-cancer five-year survival figure carrying no side of
the muscle-invasion line, no stage mix, no denominator, no registry and no years.
修正 5 bans exactly this shape topic-wide (「『膀胱癌五年存活 73%』這種沒有邊的句子全專題禁止」),
and `bl-report` makes it a stated commitment of the whole topic
(「這篇裡我不會給任何一個沒有標明是線的哪一邊的存活數字」). Group A therefore currently
contains one article that states the rule and one that breaks it.

It is made worse by a coincidence: **73.3% here is within a third of a percentage point of
SEER's "Localized" 73.0%** quoted in `bl-report`, and SEER's "Localized" is the very box the
topic spends a paragraph explaining contains both T1 and T2. A reader who has read both
articles can very easily fuse the two numbers.

The figure is being used only as a sex contrast, and the guideline's hedge
(「可能有一部分歸因於」/"may be attributable in part to") is intact, so the *argument* is not
drifting. It is the label that is missing.

**Suggested fix (both languages together).** Either attach the labels the AUA/SUFU guideline
itself gives the pair (all stages combined, which registry, which years), or drop the pair and
keep only the guideline's hedged attribution sentence, which carries the point on its own.

---

## A2 — `bl-report`: 原位癌 / "carcinoma in situ" labels two different quantities two paragraphs apart

**Section**: 〈台灣的人，站在線的哪一邊〉
**Sentences**:
- 「0 期那一格要拆開看…Ta 有 1,321 例、Tis（原位癌）只有 102 例」
- 「同一年長表統計的 3,809 例則包含原位癌 1,452 例（38.1%）與侵襲癌 2,357 例」

**What is wrong.** The same term, 原位癌, is attached to **102** in one paragraph and to
**1,452** two paragraphs later, in the article whose entire argument is that labels on this
report have to be exact.

The two numbers are not in conflict with the source — they are different fields. The
arithmetic confirms which is which: stage 0 is 38.08% of 3,737 = **1,423**, and
Ta 1,321 + Tis 102 = **1,423** exactly. So the 1,452 figure is the registry's **in-situ
behaviour count**, which in the bladder includes non-invasive papillary Ta, while the 102 is
the **Tis stage field** alone. They measure different things and must not be compared.

This is sharper in English than in Chinese, because both render as "carcinoma in situ" and the
paragraph explicitly sets 1,452 against 2,357 invasive as a partition of 3,809 — inviting the
reader to set 102 against it.

**Suggested fix.** Label the 1,452 as the in-situ *behaviour* count (Ta and Tis together) at
the point of use, or move the Ta/Tis split so the two are not read as the same field. Note that
`bl-turbt` and `bl-staging` both cite the same source for other fields, so whatever wording is
chosen should be reused there.

---

## A3 — `bl-hematuria`: the microhaematuria threshold may be off by one

**Section**: 〈試紙上那個紅字，還不算血尿〉
**Sentence**: 「一次適當採集的尿液，顯微鏡下每高倍視野超過三顆紅血球」

**What is wrong.** 「超過三顆」 is *more than three* (i.e. four or more). The AUA/SUFU
definition of microhaematuria is **three or more** (≥3) red blood cells per high-power field.
If 超過 is a slip for ≥, the definitional threshold of the whole article is off by one, and
every stratum built on top of it inherits the shift.

Translated as it stands: "more than three red blood cells per high-power field".

**Suggested fix.** Check against the guideline text and, if it is ≥3, change both languages.

---

## A4 — `bl-turbt`: the en-bloc P value and its confidence intervals do not sit together as printed

**Section**: 〈整塊切除：一個試驗說有差，兩個說沒有〉
**Sentence**: 「一年復發率 29%（18–37）對標準刮除 38%（28–46），P=0.007」

**What is wrong.** The two 95% intervals overlap across nine percentage points (28–37). For
276 pathologically confirmed patients that is not compatible with P=0.007 for a comparison of
those two proportions; a normal-approximation test on 29% vs 38% at that n lands near P≈0.11.

The most likely explanation is that the intervals are Kaplan-Meier one-year estimates while
**P=0.007 comes from a log-rank comparison of the whole time-to-recurrence curve**, not from
the one-year rates. If so, the sentence is attaching the P value to the wrong quantity and the
analysis needs naming — which matters here, because this is the one trial in the section that
found a difference, and the article's conclusion rests on how narrowly it is stated.

Translated as it stands, with the same attachment.

**Suggested fix.** Read the endpoint definition in Teoh 2024 and label the P value with the
analysis it came from.

---

## A5 — `bl-hematuria`: an odds ratio with no stated outcome or reference group

**Section**: 〈「拖了就會變末期」這句話，我不用〉
**Sentence**: 「以顯微血尿表現者 T2 以上佔 11.6%，肉眼血尿者 17.9%，多變項勝算比 1.69（1.05–2.71，P=0.03）」

**What is wrong.** The OR sits between two percentages with no outcome and no reference group
stated; the reader has to infer from word order that it is the odds of ≥T2 disease in visible
against microscopic haematuria. The topic's own rule is that every number carries its labels
(SPEC 四, 固定紅線), and an odds ratio is the number in this topic most often mis-read as a
multiple of probability.

Translated with the same structure — the English resolves it no more than the Chinese does.

**Suggested fix.** Name the outcome and the reference group in the sentence.

---

## A6 — `bl-staging`: the bone-scintigraphy 2×2 implies a far higher prevalence than the surrounding text

**Section**: 〈骨骼掃描與腦部影像，不是每個人都要做〉
**Sentence**: 「陽性預測值 56%、陰性預測值 89%、敏感度 27%、特異度 96%」, immediately after
「骨骼掃描只在 1,148 人中的 19 人（1.7%）影響了原定的處置」

**What is wrong.** Those four values are mutually consistent only if roughly **16%** of the
cohort was positive on the reference standard. That is hard to square with the same paragraph's
statement that bone metastases are rare at initial presentation of invasive bladder cancer, and
with management having changed in 19 of 1,148 (1.7%).

Most likely the diagnostic performance was computed against a composite or follow-up reference
standard rather than against bone metastasis at presentation. If so, the four values need that
label, otherwise they read as though one patient in six scheduled for radical cystectomy had
bone metastases.

Lowest priority of the six; the numbers are internally consistent as a 2×2 and only the
reference standard is unstated. Translated as it stands.

---

## Not defects — recorded so they are not re-raised

- **`bl-hematuria` and `bl-report` still have near-twin closing `<h4>`s in Chinese**
  (〈下次門診，把這四句問出口〉 / 〈把報告攤開，下次門診問這四句〉). 乙6 only required the
  `bl-hematuria` / `bl-turbt` pair to be split, and it was. In English I deliberately made the
  two distinct ("Four sentences to get said out loud at the next appointment" /
  "Lay the report out and ask these four at the next appointment"). Flagging in case the editor
  wants the Chinese pair separated too when the figures are drawn.
- **Emphasis trimmed relative to the Chinese, deliberately** (SPEC-EN §5, "do not reintroduce
  it"): three `<strong>`s dropped in `bl-staging` (the three-noun list of what imaging cannot
  see) and one in `bl-report` ("all variants as high grade"). No numbers, labels, hedges or
  conclusions were touched. Density is reported in the hand-back note.
- **`check_bilingual.py` word-proportion flag on `bl-turbt` is a false positive**: the script's
  percentage regex matches "percent" inside "**percentage points**", so
  "5.4 percentage points" is read as 5.4% (0.054) and compared against a Chinese text that
  writes 「5.4 個百分點」 with no % sign. Same class the script's own footer warns about. No change made.
- **`check_bilingual.py` reports "沒有英文版" for all 18 files** when run directly against
  `/home/claude/bl/en`, because this topic's spec names the English files `<slug>-en.html`
  while the script expects `<slug>.html` (the colon convention). Run with renamed copies, all
  four group-A files pass (citations, entries and sections all equal).

---

## Cross-reference sentences written (for title-drift checking)

`bl-hematuria`
- What happens at the resection is in "The first resection decides everything after it"; how the
  words on the report are read is in "Ta, T1 and CIS on the report"; which question each scan
  answers is in "How staging is done, and what the scan can see".

`bl-turbt`
- The terms themselves are defined in "Ta, T1 and CIS on the report" and are not re-explained
  here; the stretch before this operation … is in "Blood in the urine that does not hurt".
- What comes next is which risk group you fall into and whether you get instillations, which is
  in "Low, intermediate, high: what decides whether you get instillations"; and if what goes in
  is BCG, that is an entirely different matter — see "BCG is not chemotherapy, and not a
  vaccination".

`bl-report`
- How those four boxes decide whether you get instillations is in "Low, intermediate, high: what
  decides whether you get instillations", and is not opened up here.
- … what imaging can answer and what it cannot is in "How staging is done, and what the scan can
  see". On the right-hand side of the line a route has to be chosen between removing the bladder
  and keeping it, which is in "Remove the bladder, or keep it". … see "It grows in the upper
  tract too".

`bl-staging`
- The terms themselves are defined in "Ta, T1 and CIS on the report" and are not re-explained here.
- … the stage field in a registry and the line drawn in clinic … are two different languages.
  That is written up in "Ta, T1 and CIS on the report".
- Second resection is dealt with in "The first resection decides everything after it".
- … a route has to be chosen between removing the bladder and keeping it, which is in "Remove
  the bladder, or keep it"; and for the kind that grows in the renal pelvis and the ureter, the
  numbers cannot be applied across to the bladder — see "It grows in the upper tract too".

All eleven use the SPEC-EN §4 canonical titles verbatim, in double quotation marks, unlinked.
No pointer to a live site page occurs in group A.
