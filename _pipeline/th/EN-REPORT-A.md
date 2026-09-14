# EN-REPORT-A — third adversarial round, found while rewriting group A in English

Rule followed: **report, don't fix.** Every item below was rendered into English exactly as the Chinese has it, defect and all. Nothing here was silently corrected in `/home/claude/th/en/*.html`.

Severity scale: **High** = the claim as written is stronger than, or different from, what the source supports, and a reader or a downstream editor could act on it. **Medium** = sourcing/attribution defect, or a gloss that does not survive being said plainly. **Low** = a missing qualifier, an over-simplified next step, an unverifiable aside.

Counts: **High 2 · Medium 5 · Low 7** (14 total).

---

## HIGH

### H-1 — `body/th-overdiagnosis.html`, §〈「死亡率完全沒動」這句話也不對〉 — a denominator switch is used to rebut a claim about a different denominator

Quoted text:

> 韓國一個涵蓋 434,228 名甲狀腺癌病人的全國世代（女性 352,678、男性 81,550，平均年齡 48.6 歲，中位追蹤 7.4 年），甲狀腺癌特異性的標準化死亡率（分母是人年，和上面每十萬人的不是同一種算法）是：2005 年每 1000 人年 1.94，2013 年降到 0.76，然後 2018 年又升到 2.70。

**What is wrong.** The section heading asserts that "the death rate never moved" is false. The claim being rebutted ("死亡率沒有變") is, in every place it circulates, a statement about **population** mortality — deaths per 100,000 of the general population. The Korean figure is a **cohort case-fatality rate**: the denominator is person-years accumulated by the 434,228 people who already have a thyroid cancer diagnosis. Those two quantities can move in opposite directions for purely mechanical reasons. When screening added ~45,000 mostly indolent cases a year to the denominator, cohort case-fatality had to fall; when screening fell back after 2015 and the incident case-mix stopped being diluted, it had to rise again. A rise from 0.76 to 2.70 per 1,000 person-years is therefore compatible with a completely flat population mortality rate, and does not by itself show that population mortality moved.

The article's own parenthetical — 「分母是人年，和上面每十萬人的不是同一種算法」 — shows the author noticed the *unit* mismatch (person-years vs. 100,000) but not the *population* mismatch (patients vs. everybody), and then drew the conclusion anyway.

**What the source actually says.** [A-S36c] (Int J Surg 2024;110(9):5489–5495) is described in the brief as a "nationwide population-based cohort study" of 434,228 thyroid cancer patients, endpoint "thyroid-cancer-specific mortality", rate expressed per 1,000 person-years. It reports a rate **within diagnosed patients**. It makes no claim about the general-population mortality rate, and the brief attaches no such claim to it.

**Note.** SPEC §九 修正 10 does mandate carrying the 0.76 → 2.70 figure, so the number belongs in the article. The defect is the framing: the section presents a patient-cohort rate as a refutation of a population-rate claim. The rebuttal that *does* work on its own terms — ATA 2025's 1.1%/yr rise in advanced-disease mortality — is in the very next paragraph and needs no denominator switch.

**Severity: High.** The article's summary sentence 「整體死亡率的變化很小，但變化不是零」 rests partly on this comparison.

---

### H-2 — `body/th-staging.html`, §〈分期在回答的問題，只有一個：死亡〉 — Recommendation 28A is quoted with four words removed, and those four words are the ones that weaken the article's thesis

Quoted text:

> 2025 年版的對應條文是第 28A 條，同樣是強烈建議、中等確定性證據，目的寫的是判定結構性疾病殘存或復發的風險。

**What is wrong.** The article's central claim — 「期別預測死亡，復發風險分層預測結構性復發。這是兩把尺」, and the whole closing section 〈兩條軸之間，我不畫箭頭〉 — is built on the premise that the recurrence-risk system does not speak to survival. The recommendation it cites to establish that premise does speak to survival, and the article drops the phrase.

**What the source actually says.** [A-S1] gives Rec 28A verbatim: "…is recommended to determine the risk of structural disease persistence/recurrence (locoregionally and/or distantly) **and/or survival** in patients with DTC. (Strong Recommendation, Moderate certainty evidence)". The 2025 ATA risk stratification system is recommended for recurrence risk **and/or survival**. Separately, [A-S24] — which this same article uses for the cross-table — is an entire paper about using the ATA risk system to refine **disease-specific survival** estimates, i.e. it demonstrates the risk system predicting death.

The asymmetry the guideline actually asserts runs one way only: staging does *not* predict recurrence ("AJCC/UICC staging is designed to predict disease-specific survival and thus does not predict overall risk of structural persistence/recurrence"). There is no matching guideline sentence saying the risk system does not predict death.

**Severity: High.** This is selective quotation in service of the article's thesis, and 修正 9 makes that thesis the spine of A4 and of fig-th-two-systems. The figure's "no arrow between the two axes" instruction is not affected — the two axes are still two axes — but the sentence as written misrepresents a recommendation it quotes by number and grade.

---

## MEDIUM

### M-1 — `body/th-staging.html`, §〈另一套系統：復發風險，而且它也改版了〉 — 修正 5 violation: primary-study numbers transcluded through ATA 2025

Quoted text:

> 三級系統時代的復發率（乳突癌、終點是結構性復發）是低風險 1.5%、中風險 5.4%、高風險 25%；只看 1 公分以下的微小乳突癌，是 1.6%、7.4%、22.7%<sup>[1]</sup>

**What is wrong.** Citation [1] is ATA 2025. These six percentages are not ATA 2025's own; the brief records them as "（Kim 等轉引）" — ATA 2025's citation of a primary study. SPEC §九 修正 5 reads 「絕對禁止透過 ATA 2025 轉引原始論文 … 每一個試驗數字都要回到原著」, and lists five instances in which ATA 2025's transcluded numbers were demonstrably wrong (ref 883, ref 763/764, ref 1194, Rec 53's arithmetic, Rec 62's AE grading). This set was never traced back to Kim et al.

**What the source actually says.** [A-S1] bullet: 「2015 ATA 三級系統的復發率（ATA 2015 三級／PTC／終點＝structural recurrence）：低風險 1.5%、中風險 5.4%、高風險 25%（Kim 等轉引）；只看 T1a PTC：1.6%／7.4%／22.7%」 — the brief itself marks it as 轉引.

**Severity: Medium.** The numbers are plausible and internally consistent; the violation is procedural, but 修正 5 exists precisely because ATA 2025's transclusions were caught being wrong five times in one round.

---

### M-2 — `body/th-pathology.html`, §〈被膜與血管〉 and §〈濾泡癌要數「幾條」〉 — three percentage ranges attributed to ATA 2015, but obtained from ATA 2025

Quoted text:

> 2015 年那一版指引把有血管侵犯的乳突癌歸在中度復發風險，結構性復發風險 15% 到 30%<sup>[6]</sup>
> 2015 年那一版把廣泛血管侵犯（4 條以上）列為高復發風險，結構性復發風險 30% 到 55%；微小侵犯（少於 4 條）列為低風險，2% 到 3%<sup>[6]</sup>

**What is wrong.** Citation [6] is ATA 2015 (`10.1089/thy.2015.0020`). All three ranges — 15–30%, 30–55%, 2–3% — appear in the brief **only** under [A-S1] (ATA 2025), in bullets that begin "2015 ATA 把…列為". The brief's own extraction of [A-S4] (ATA 2015) lists Table 11's *criteria* and Table 12's NED/biochemical/structural percentages, and contains none of these three ranges. So the article cites a document for text the verification round did not extract from that document; what it actually read was ATA 2025's account of ATA 2015.

**What the source actually says.** Nothing in the A brief places these strings inside the ATA 2015 PDF. If they are there (ATA 2015's risk-of-recurrence continuum figure is the likely location), the citation is fine and the fix is to record the extraction; if they are not, the citation is to the wrong document and the material is a 修正 5 transclusion like M-1.

**Severity: Medium** — unresolved attribution, and it sits on two of the report lines the article calls the most decision-changing.

---

### M-3 — `body/th-nodule.html`, §〈同一顆結節，兩套表會不同意〉 — an "internal inconsistency" is declared in a source that is not inconsistent

Quoted text:

> 第 4 類這一格請注意：同一篇的表格寫 1 到 1.5 公分，前面敘述那一顆結節時用的是 1.0 公分，來源自己兩處不一致，我照抄。

**What is wrong.** The article accuses a PASS source of contradicting itself. It does not. K-TIRADS category 4 has a *range* as its threshold, deliberately, and 1.0 cm is the bottom of that range — so a table reading ">1–1.5 cm" and a narrative saying a 1.0–1.5 cm nodule "enables cytologic diagnosis with a FNAB threshold of 1.0 cm" are the same statement, not two.

**What the source actually says.** [A-S5], the 2021 K-TIRADS consensus itself: category 4 threshold ">1.0–1.5 cm", with the original note that 「切點應在 1 與 1.5 cm 之間依超音波特徵、結節位置、臨床與病人因素決定」. [A-S7] Table 5 renders it as "4 >1–1.5 cm" and the discussion quotes the 1.0 cm end. Both are consistent with the primary document.

**Severity: Medium.** Publicly labelling a cited paper self-contradictory when it is not is a reliability claim the article cannot support, and it would survive screenshotting.

---

### M-4 — `body/th-nodule.html`, §〈四套表〉 — "unnecessary biopsy rate" is glossed with the wrong denominator

Quoted text:

> 比的是：照這套表走，會有多少人挨了不必要的一針。答案是 ACR TI-RADS 41%（95% 信賴區間 32–49）…2016 年版 K-TIRADS 79%（74–83）

**What is wrong.** As written, the sentence reads as "this share of *people* take an unnecessary needle" — i.e. a proportion of everyone scanned. The metric is a proportion of those the table *sends* for a needle: among nodules biopsied on that table's recommendation, the share that turn out benign. Read the article's way, 79% of everyone scanned under the 2016 K-TIRADS would be getting a needle they did not need, which is not what the meta-analysis measured and is not arithmetically compatible with the malignancy prevalences in these cohorts.

**What the source actually says.** [A-S8] reports 「合併不必要切片率」 — pooled unnecessary biopsy rate, a rate conditioned on biopsy having been recommended.

**Severity: Medium.** The gloss is the load-bearing sentence for the whole "four tables" section, and it is the one number readers will quote back.

---

### M-5 — `body/th-fna.html`, §〈這張報告在回答的問題，比你以為的窄〉 — a NIFTP-specific limit is generalised to capsular invasion as a whole

Quoted text:

> 最典型的例子是被膜有沒有被穿破——那必須把整顆腫瘤的被膜在顯微鏡下看過一輪才知道，細胞學做不到<sup>[1]</sup>

**What is wrong.** The cited verbatim in [A-S13] is specifically about NIFTP: "A definitive diagnosis of NIFTP requires an extensive histological examination of the entire tumour capsule. Therefore, NIFTP cannot be diagnosed by cytology." The article converts a statement about one diagnostic entity into a general statement about assessing capsular invasion. The general statement is very likely true and is uncontroversial clinically, but it is not the sentence the citation carries, and `th-pathology` uses the same source for the narrow, correct version.

**Severity: Medium** — citation carries less than the claim.

---

## LOW

### L-1 — `body/th-nodule.html` — 「那篇比較研究沒有交代它用的是哪一版 K-TIRADS」
The brief records no such observation about [A-S7], and the K-TIRADS thresholds [A-S7] tabulates (3 >2 cm, 4 >1–1.5 cm, 5 >1 cm) match the 2021 consensus [A-S5] exactly. The disclaimer may be correct about the paper's prose, but it is an assertion about a source that the verification round did not make, and it is repeated twice. **Low.**

### L-2 — `body/th-nodule.html` — the sub-centimetre K-TIRADS 5 exception drops its lower bound
Article: 「1 公分以下的高度可疑結節，只有在貼著氣管、或是長在後內側被膜…才建議切片」. [A-S5] scopes the exception to nodules **>0.5 cm and ≤1 cm**. The omission widens the stated rule downward. Direction is non-dangerous (sub-5 mm nodules are not biopsied under K-TIRADS either), but the label is missing. **Low.**

### L-3 — `body/th-nodule.html` — the 7–15% denominator is presented as the guideline's own wording
Article: 「2015 年那份指引寫的是：在那些『因為需要排除癌症而被臨床評估』的結節裡，惡性佔 7% 到 15%」. The ATA sentence is "The clinical importance of thyroid nodules rests with the need to exclude thyroid cancer, which occurs in 7%–15% of cases…" — it does not itself define the denominator as "nodules brought to clinical evaluation". That framing is the brief's interpretive ruling ([A-S4] note), and the article attributes it to the document. **Low.**

### L-4 — `body/th-fna.html` — category V's next step is truncated
Article: 「第五類與第六類進到手術的討論」. [A-S13]: category V = "Molecular testing, lobectomy, or near-total thyroidectomy" — molecular testing is one of the listed options and is dropped, in an article whose whole point is what molecular testing is for. **Low.**

### L-5 — `body/th-staging.html` — a claim about the 2025 edition is cited to the 2015 edition
Article: 「2015 年那一版指引的分期表用的還是第七版，切點寫 45 歲；2025 年版才是這個學會第一份以第八版為基礎的分化型甲狀腺癌指引<sup>[2]</sup>」. Citation [2] is ATA 2015, which cannot source a statement about what the 2025 edition is. The 修正 8 claim itself is correct; only the citation anchor is wrong. **Low.**

### L-6 — `body/th-staging.html` — T4a's first-listed structure is dropped
Article lists T4a as 「肉眼侵犯到喉、氣管、食道或喉返神經」. [A-S22] verbatim includes **subcutaneous soft tissue** ahead of larynx. **Low.**

### L-7 — `body/th-overdiagnosis.html` — 「整體死亡率的變化很小」 is an uncited cross-country generalisation
This clause sits in the article's summary sentence with no citation, and the sources point in more than one direction: USPSTF says US incidence rose "without a corresponding change in the mortality rate" [A-S32], while [A-S35] reports Korea's age-standardised **mortality** rate declining since the early 2000s and [A-S1] reports a rise in advanced disease. The article's own §〈台灣的數字〉 states that no year-by-year Taiwanese mortality series could be found. A summary of "overall mortality" across all three settings is asserted without a source. **Low.**

---

## Not a defect, but flag before publication

- `en/th-fna-en.html` points at the off-series second-opinion page as 〈Asking for a second opinion〉. SPEC-EN §5 requires that title to be taken from the live `sit-second-opinion-en.html` `<h1>`, which this session could not read. **Verify the string before the page goes up.** The Chinese 〈想聽第二個意見，怎麼開口〉 was left untouched.
- 修正 2 (ATA labelled as the 2015 edition throughout A1/A2), 修正 8/9 (two systems; an AJCC edition on every stage figure), 修正 10–13 (Korean chronology, the 1.1%/yr advanced-disease rise, no Taiwan overdiagnosis percentage, Taiwan incidence *counts* only), 修正 16, 修正 17 and 紅線 2 were each checked line by line in all five articles and are all satisfied. No new 修正 5 violation was introduced by the English edition; M-1 and M-2 are pre-existing in the Chinese.
