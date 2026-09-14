# VERIFY-EN — seven contested findings, settled against primary sources

Round date 2026-09-14. **Verification only — no article was edited.**
Every block marked "verbatim" was pulled from the source named in the same block during this round.
Where a source could not be obtained, it says so; nothing has been reconstructed from memory.

Routes used: Europe PMC REST (`search?query=EXT_ID:<PMID>&resultType=core`, `/<PMCID>/fullTextXML`),
PMC HTML (`https://pmc.ncbi.nlm.nih.gov/articles/<PMCID>/`) with a browser User-Agent,
ClinicalTrials.gov API v2, Semantic Scholar and Unpaywall (availability checks only). NCCN not consulted.

---

## Q1 — Korea's thyroid-cancer-specific mortality denominator

**Question.** `th-overdiagnosis.html` / `th-overdiagnosis-en.html` prints 1.94 → 0.76 → 2.70 per 1,000 person-years
under the heading `"The death rate never moved" is not right either`. Is the denominator all Koreans, or
people already diagnosed with thyroid cancer?

**Source.** [A-S36c] Kim KJ, Chun J, Park SG, Park YJ, Kim SG. *Thyroid cancer-specific mortality during
2005–2018 in Korea, aftermath of the overdiagnosis issue: a nationwide population-based cohort study.*
Int J Surg 2024;110(9):5489–5495. PMID 38874484. PMCID PMC11392158 (OA).
Obtained: `/europepmc/webservices/rest/PMC11392158/fullTextXML`, HTTP 200, 68,076 bytes, full text read.

**Verbatim — the methods sentence that settles it** (Statistical analysis):

> "Mortality rates for patients with TC were calculated by dividing the number of deaths by **the total
> person-years of all TC patients** and represented as the rate per 1000 person-years (PYs) according to
> the year of TC diagnosis. To estimate the standardized mortality rates in TC patients, we used the age
> distribution (5-year intervals) and sex distribution based on person-years of **all TC patients in 2013**
> as reference population in the calculations."

**Verbatim — the abstract's own framing of the denominator:**

> "The age-standardized and sex-standardized mortality rates of TC per 1000 person-years were calculated
> **considering the number of patients diagnosed with TC in 2013 per our database** to evaluate the
> TC-specific mortality trends according to the year of TC diagnosis."

**Verbatim — follow-up definition** (Methods):

> "The follow-up duration was defined as the time from the first date of the TC claim to the date of the
> death claim or the last data collection in this cohort (31 December 2019). Age-standardized and
> sex-standardized mortality rates were analyzed to determine TC-specific deaths **in patients diagnosed
> with TC in the indicated year**."

**Verbatim — the paper itself rules out the comparison the article makes** (Discussion):

> "Previous Korean studies that used data from Korean statistics demonstrated that age-standardized
> mortality rates from TC per 100 000 population increased from 1985 to 2004 and then continuously
> decreased until 2015. **The recent mortality trends were discordant with the present study because the
> previous study examined the age-standardized mortality rate of TC in that year based on the overall
> general population, whereas our study analyzed the mortality trend based on the calendar year of
> diagnosis as a reference for patients with TC diagnosed in 2013.**"

**Verbatim — the paper's own limitation on the 2018 end of the curve:**

> "The relatively short follow-up duration is also a major disadvantage of this study."

(Data cut 31 Dec 2019; patients diagnosed in 2018 contribute at most ~2 years of person-time, so the 2.70
figure is dominated by deaths occurring soon after diagnosis.)

**Verdict: FINDING UPHELD.**

The denominator is person-years accumulated by **people already diagnosed with thyroid cancer**, not
Koreans. The quantity is a case-fatality rate indexed to year of diagnosis, not a population mortality
rate. It behaves exactly as the reviewer says: while screening was pouring low-risk cases into the
denominator (to 2012), the rate fell (1.94 → 0.76); when that inflow stopped, the rate rose (0.76 → 2.70)
with no implication whatever about deaths per head of population. The authors say so themselves, and in
the same paragraph record that the Korean *population* mortality rate fell continuously to 2015.

Using it under the heading `"The death rate never moved" is not right either` is a category error.
The English article does carry a partial hedge — "the denominator here is person-years, a different
calculation from the per-100,000 figures above" — but that names the wrong difference. Persons vs
person-years is not the problem; **diagnosed patients vs the general population** is.

Note what survives: the *other* leg of that paragraph — ATA 2025's "the mortality rate from that same
period increased annually by 1.1% in advanced disease" (1974–2013, US, population-level) — is a genuine
population-mortality statement and continues to support the paragraph's conclusion on its own.

**Wording I would defend** (replacing the Korean sentence's rhetorical job, not its facts):

> A Korean nationwide cohort followed 434,228 people **who had already been diagnosed with thyroid
> cancer**, and measured deaths per 1,000 person-years **within that group**, indexed to the year of
> diagnosis: 1.94 in 2005, 0.76 in 2013, 2.70 in 2018. Read it for what it is — while screening was
> adding large numbers of low-risk cases to the diagnosed group, the death rate inside that group fell;
> once screening fell away, it rose again. It is not the country's death rate, and the authors say
> plainly that it does not line up with the country's death rate, which fell continuously to 2015.
> What does move the population figure is the American one: between 1974 and 2013 mortality rose 1.1%
> a year in advanced disease.

---

## Q2 — ATA 2025 Recommendation 28A's full text

**Question.** `th-staging.html` / `-en.html` cites Rec 28A to establish that recurrence-risk stratification
speaks only to recurrence. Does it say "and/or survival"? Does ATA 2025 anywhere say the recurrence-risk
system does **not** predict death? And what is [A-S24]?

**Source.** [A-S1] *2025 American Thyroid Association Management Guidelines for Adult Patients with
Differentiated Thyroid Cancer.* Thyroid 2025;35(8):841–985. PMID 40844370. PMCID PMC13090833.
Obtained this round: `https://pmc.ncbi.nlm.nih.gov/articles/PMC13090833/` with a browser User-Agent,
HTTP 200, 2,436,560 bytes, text extracted and read.
(`europepmc.org/articles/PMC13090833?pdf=render` returned 403 this round; `/PMC13090833/fullTextXML`
returns 404. The PMC HTML route worked and is the one to use.)

**Verbatim — Recommendation 28, under the heading "How should risk of recurrence and initial assessment
be performed after surgery?":**

> **RECOMMENDATION 28**
> **A.** "The 2025 ATA Risk Stratification System, which evaluates the histopathologic features of the
> tumor and number of cervical lymph nodes in combination with the AJCC staging system, postoperative
> imaging, and serum Tg and TgAb testing (if appropriate), is recommended to determine the risk of
> structural disease persistence/recurrence (locoregionally and/or distantly) **and/or survival** in
> patients with DTC."
> **(Strong Recommendation, Moderate certainty evidence)**
>
> **B.** "Molecular profiling of histologic specimens postoperatively is not recommended routinely.
> However, if such data have been obtained, they can be used to further estimate risks of recurrence
> derived from the 2025 ATA Risk Stratification System."
> **(Conditional recommendation, Low certainty evidence)**

**Does ATA 2025 anywhere say the recurrence-risk system does not predict death?** No. Searched the full
text for "does not predict", "not predict", "designed to predict", "predicts disease-specific survival".
The asymmetry runs the *other* way, and only the other way:

> "AJCC/UICC staging is designed to predict disease-specific survival and thus **does not predict overall
> risk of structural persistence/recurrence**."

> "The 2015 ATA Risk of Recurrence stratification system has been reported to be a **better** predictor of
> structural persistence/recurrence than AJCC/UICC TNM staging, which predicts disease-specific survival."

And a second passage attributes mortality insight to the ATA system directly:

> "While **the ATA Risk of Recurrence and tumor staging estimates** provide important insights into a
> patient's risk of clinical recurrence **and disease-specific mortality**, they are not designed for
> individualization of therapy based on response to treatment."

So the guideline says staging does not predict recurrence. It never says the recurrence system does not
predict death; twice it says or implies it does bear on survival.

**[A-S24] — what it actually is.** *Using the American Thyroid Association Risk-Stratification System to
Refine and Individualize the American Joint Committee on Cancer Eighth Edition **Disease-Specific
Survival** Estimates in Differentiated Thyroid Cancer.* Thyroid 2018;28(10):1293–1300. PMID 29897011.
MSKCC registry, 4,881 adults <55, 122 (2.5%) disease deaths; the whole point of the paper is crossing
AJCC 8th stage with ATA recurrence risk to produce **better 10-year DSS** estimates (Stage I/ATA low 100%
down to Stage II/ATA high, 45–55, 61%). The English article already uses exactly these DSS numbers, at
reference [5], two paragraphs after asserting that recurrence risk predicts only recurrence.

**Verdict: FINDING UPHELD (all three limbs).**
The article's rendering — "its stated purpose is determining the risk of structural disease persistence
or recurrence" — truncates the recommendation at the comma before "and/or survival". The clean slogan
"Stage predicts death. Recurrence risk stratification predicts structural recurrence." is not the
guideline's position, is contradicted by the guideline's own Rec 28A and by its "clinical recurrence and
disease-specific mortality" sentence, and is undercut by the article's own reference [5], which is a paper
about using the ATA risk system to sharpen disease-specific survival.

**Wording I would defend:**

> Recommendation 28A of the 2025 edition — a strong recommendation on moderate certainty evidence — asks
> for the 2025 ATA Risk Stratification System to be used "to determine the risk of structural disease
> persistence/recurrence (locoregionally and/or distantly) and/or survival". The asymmetry the guideline
> does assert runs one way only: AJCC/UICC staging "is designed to predict disease-specific survival and
> thus does not predict overall risk of structural persistence/recurrence". So: stage is built for death
> and is poor at recurrence; the recurrence system is built for recurrence and, layered on top of stage,
> sharpens the survival estimate as well. That is why the table below — stage crossed with recurrence
> risk — is a table of disease-specific survival.

---

## Q3 — the direction of Sanabria 2022's prophylactic central neck dissection result

**Question.** `th-neck-dissection.html` / `-en.html` prints 11/409 (2.7%) with dissection versus 9/354
(2.5%) without, then glosses NNT 500 as "you would have to perform prophylactic dissection on 500 people
to spare one of them a single recurrence". Which arm had more recurrences, what does the NNT refer to,
in which direction, and what do the authors conclude?

**Source.** Sanabria Á, Betancourt-Agüero C, Sánchez-Delgado JG, García-Lozano C. Ann Surg
2022;276(1):66–73. PMID 35129470. DOI 10.1097/SLA.0000000000005388.
Obtained: Europe PMC core record (full structured abstract), cross-checked against the Semantic Scholar
record of the same DOI — the two agree word for word.
**Full text could not be obtained.** Unpaywall reports `is_oa: false`, `oa_status: closed`, zero OA
locations; Europe PMC `isOpenAccess: N`, `inEPMC: N`, no PMCID; `doi.org` resolves to journals.lww.com
and returns 403. Consequently **the sentence in which the authors define the NNT of 500 and give its sign
is not in hand.** That limit is stated again in the verdict.

**Verbatim — title:**

> "Prophylactic Central Neck Lymph Node Dissection in Low-risk Thyroid Carcinoma Patients **Does Not
> Decrease the Incidence of Locoregional Recurrence**: A Meta-analysis of Randomized Trials."

**Verbatim — Results:**

> "Five RCTs with 763 patients were included (354 in the T group and 409 in the T+CND group). Most
> studies were classified as having a low risk of bias. Publication bias was not found. **Structural
> recurrence occurred in 11/409 (2.7%) patients in the T+CND group and 9/354 (2.5%) patients in the T
> group, with a risk difference (RD) = 0% [95% confidence interval (CI) –2% to 2%].** For biochemical
> recurrence, the RD was 0% (95% CI –5% to 4%). **The number needed to treat was 500.** The rate of
> permanent hypoparathyroidism was higher in the T+CND group than in the T group [RD 3% (95% CI 0%–6%)]."

**Verbatim — Conclusions:**

> "**We did not find a beneficial effect of prophylactic CND** associated with T on locoregional or
> biochemical recurrence but did confirm a higher risk of permanent hypoparathyroidism associated with
> this procedure."

**Verdict: FINDING UPHELD.**

1. **Which arm had more recurrences: the dissection arm.** 11/409 (2.69%) with T+CND against 9/354
   (2.54%) with thyroidectomy alone. The crude difference, such as it is, runs *against* dissection.
2. **The NNT of 500 cannot mean what the article says it means.** The pooled risk difference is 0%
   (95% CI −2% to 2%) — a point estimate that rounds to zero, with the raw counts pointing the wrong way.
   1/0.002 = 500, and 2.7% − 2.5% = 0.2%: the reciprocal is being taken of a difference that is null to
   two decimal places and, at the observed point estimate, adverse. Reading it as "dissect 500 to spare
   one recurrence" converts a null result into a small benefit.
3. **The authors conclude the opposite of a benefit** — in the title ("Does Not Decrease") and in the
   Conclusions ("We did not find a beneficial effect").

**What is *not* true.** The article's overall argument is not inverted. Its thesis — prophylactic central
dissection does not buy you less recurrence and does buy you more permanent hypoparathyroidism — is
exactly what Sanabria found. The sign error runs in the *concessive* direction: the gloss hands back a
benefit the paper says it did not find, and the section's framing ("31 becomes 500") reads as
"large benefit becomes tiny benefit" when the truth is "apparent benefit becomes no benefit". The fix
strengthens the article rather than reversing it. (Wang 2013's NNT of 31 *is* a benefit NNT — RR 0.59
favouring dissection, non-significant — so the two NNTs are not the same kind of number and should not be
set side by side as if they were.)

**Honest limit.** Without the full text I cannot quote the authors' own definition of the NNT or read its
sign off the page. Everything above rests on the verbatim abstract, which is sufficient to establish that
the dissection arm had more recurrences and that the authors found no benefit — and therefore sufficient
to establish that the article's gloss is not supportable — but is not sufficient to state positively that
the authors labelled 500 a number-needed-to-harm.

**Wording I would defend:**

> A 2022 meta-analysis took randomised trials only — 5 trials, 763 people (354 total thyroidectomy alone,
> 409 with dissection). Structural recurrence was 11/409 (2.7%) in the dissection arm against 9/354 (2.5%)
> without it — slightly more, not fewer — and the risk difference was 0% (95% confidence interval minus 2%
> to 2%); for biochemical recurrence it was also 0%. The authors report a number needed to treat of 500,
> which is what you get by taking the reciprocal of a difference that is essentially zero; it is not a
> count of people spared anything. Their title says it straight: prophylactic central neck dissection
> "does not decrease the incidence of locoregional recurrence", and their conclusion is that they "did not
> find a beneficial effect".

---

## Q4 — ATA 2025 Recommendation 19A's exact wording versus ATA 2015 Recommendation 36C

**Sources.**
ATA 2025 — as in Q2, PMC HTML of PMC13090833.
ATA 2015 — *2015 American Thyroid Association Management Guidelines for Adult Patients with Thyroid
Nodules and Differentiated Thyroid Cancer.* Thyroid 2016;26(1):1–133. PMID 26462967. PMCID PMC4739132.
Obtained: `https://pmc.ncbi.nlm.nih.gov/articles/PMC4739132/`, HTTP 200, 2,065,326 bytes, text extracted.
(First two attempts returned a Google reCAPTCHA interstitial; a third attempt after a pause returned the
article. The proxy status endpoint showed no relay failures, so the block was PMC-side rate limiting.)

**Verbatim — ATA 2025, under "When should prophylactic central-compartment lymph node resection be
performed?":**

> **RECOMMENDATION 19**
> **A.** "Prophylactic central-compartment lymph node dissection should not be performed for **most**
> small, noninvasive, clinically node-negative PTC (cT1-T2, cN0) and for **most** FTCs."
> **(Strong recommendation, Moderate certainty evidence)**
>
> **B.** "Prophylactic central-compartment neck dissection may be considered in patients with PTC and
> clinically uninvolved lymph nodes (cN0) who have advanced primary tumors (T3 or T4) or for whom the
> information will be used to plan further steps in therapy, but this approach should be weighed against
> the risks as they evolve during thyroidectomy."
> **(Conditional recommendation, Low certainty evidence)**

**Verbatim — ATA 2015, Recommendation 36:**

> **(B)** "Prophylactic central-compartment neck dissection (ipsilateral or bilateral) should be
> considered in patients with papillary thyroid carcinoma with clinically uninvolved central neck lymph
> nodes (cN0) who have advanced primary tumors (T3 or T4) **or clinically involved lateral neck nodes
> (cN1b)**, or if the information will be used to plan further steps in therapy."
> **(Weak recommendation, Low-quality evidence)**
>
> **(C)** "Thyroidectomy without prophylactic central neck dissection **is appropriate** for small (T1 or
> T2), noninvasive, clinically node-negative PTC (cN0) and for **most** follicular cancers."
> **(Strong recommendation, Moderate-quality evidence)**

**Verdict: FINDING UPHELD.**

Laid side by side, the 2025 edition made three changes, and the article carries two of them:

| | 2015 Rec 36C | 2025 Rec 19A |
|---|---|---|
| Verb | "is appropriate" (permissive) | "should not be performed" (prohibitive) |
| Qualifier before PTC | **none** — "for small (T1 or T2), noninvasive, clinically node-negative PTC (cN0)" | **"most"** — "for most small, noninvasive, clinically node-negative PTC (cT1-T2, cN0)" |
| Qualifier before follicular | "most follicular cancers" | "most FTCs" |
| Grade | Strong recommendation, Moderate-quality evidence | Strong recommendation, Moderate certainty evidence |

So yes: **2025 added a "most" before PTC that 2015 did not have**, at the same moment it hardened the
verb. The article captures the verb change faithfully ("From 'not doing it is fine' to 'it should not be
done'") and preserves the 2015 "most" before follicular cancers — but renders the 2025 clause as
"should not be performed **in these people**", which carries neither "most". Read as written, the article
reports a prohibition where the guideline wrote a strong default with an explicit exception built into it.

The article's separate observation about Rec 19B — that cN1b has been dropped as a situation in which
prophylactic dissection may be considered — is confirmed verbatim above and stands.

**Wording I would defend:**

> Recommendation 36C of the 2015 edition said that for small (T1 or T2), noninvasive, clinically
> node-negative papillary cancers and most follicular cancers, thyroidectomy without prophylactic central
> neck dissection "is appropriate". Strong recommendation, moderate-quality evidence. Recommendation 19A
> of the 2025 edition hardens the verb and softens the scope in the same breath: prophylactic
> central-compartment dissection "should not be performed for **most** small, noninvasive, clinically
> node-negative PTC (cT1-T2, cN0) and for **most** FTCs". Strong recommendation, moderate certainty
> evidence. Two changes, not one. "Not doing it is fine" became "it should not be done" — and a "most"
> appeared in front of papillary cancer that was not there in 2015, which is the guideline leaving room
> for the case that does not fit.

---

## Q5 — IoN's five-year rates and its stated absolute difference

**Source.** *Thyroidectomy with or without postoperative radioiodine for patients with low-risk
differentiated thyroid cancer in the UK (IoN): a randomised, multicentre, non-inferiority trial.*
Lancet 2025;406(10498):52–62. PMID 40543520. DOI 10.1016/S0140-6736(25)00629-4.
Obtained: Europe PMC core record, full structured abstract, verbatim.
**Full text could not be obtained** — Europe PMC `isOpenAccess: N`, no PMCID.

**Verbatim — Methods (the estimand and the margin):**

> "The primary endpoint was **5-year recurrence-free survival**, defined by the absence of locoregional
> recurrent or persistent structural disease, distant metastases, or death from thyroid cancer.
> **Non-inferiority was assessed with a margin of 5 percentage points.** Per-protocol and
> intention-to-treat (ITT) analyses were done for the primary endpoint, and safety was analysed in the
> per-protocol population."

**Verbatim — Findings:**

> "Median follow-up was 6·8 years (IQR 5·6–8·6) in the no ablation group and 6·6 years (4·8–8·5) in the
> ablation group; 17 recurrences (eight in the no ablation group and nine in the ablation group; ITT
> population) occurred during follow-up. **5-year recurrence-free rates were 97·9% (95% CI 96·1–99·7) in
> the no ablation group versus 96·3% (93·9–98·7) in the ablation group in the ITT analysis, and 97·9%
> (96·1–99·7) versus 96·9% (94·7–99·1) in the per-protocol analysis. The 5-year absolute risk difference
> was 0·5 percentage points (95% CI −2·2 to 3·2, p(non-inferiority)=0·033; ITT analysis), showing that
> non-inferiority was reached.**"

**Verdict: PARTLY — the two statements are reconcilable, but not on the article's present wording.**

What 97.9 and 96.3 are: **5-year recurrence-free rates** (not survival percentages, not the difference's
inputs) — 97.9% in the **no-ablation** arm, 96.3% in the **ablation** arm, ITT.

What the reported difference is: **0.5 percentage points, 95% CI −2.2 to 3.2**, p(non-inferiority) = 0.033,
ITT, against a prespecified margin of **5 percentage points**.

Why 0.5 and not 1.6: the crude gap between the two Kaplan-Meier point estimates is 1.6 percentage points
(97.9 − 96.3) in favour of *no* ablation, and 1.0 point in the per-protocol analysis. The reported 0.5 is
none of these. It is a separately estimated 5-year absolute risk difference, and its sign is the one the
non-inferiority test requires: the trial declares non-inferiority because the **upper** bound of that
interval (3.2) sits below the 5-point margin, which is only meaningful if the quantity is the excess risk
carried by the no-ablation arm. In other words the difference is positive in the direction of no-ablation
being marginally worse, while the raw 5-year rates read the other way. **By what method it was estimated
is not stated in the abstract, and the full text is not obtainable** — so the precise estimator
(model-based, stratified on the minimisation factors, or otherwise) is something I cannot report.
Recorded as: could not obtain.

The unreconcilable part is purely the article's sentence, which reads the three numbers as one arithmetic
chain — "Five-year recurrence-free rates were 97.9% without and 96.3% with, an absolute difference of 0.5
percentage points" — where in the paper the first two are Kaplan-Meier point estimates and the third is a
separately estimated quantity that does not equal their difference and does not point the same way.

**Wording I would defend:**

> IoN, in the UK, asked the same question across 33 centres in 504 people, with median follow-up of 6.8
> and 6.6 years. Five-year recurrence-free rates were 97.9% (95% confidence interval 96.1 to 99.7) without
> ablation and 96.3% (93.9 to 98.7) with it. The trial's own headline is not the gap between those two
> figures: it reports a 5-year absolute risk difference of 0.5 percentage points (95% confidence interval
> −2.2 to 3.2), and non-inferiority is declared because the top of that interval sits under the 5-point
> margin fixed in advance. Across the whole trial there were 17 recurrences — eight without ablation, nine
> with. With numbers that small, what the trial establishes is that leaving it out is not worse by more
> than the margin; it does not establish that leaving it out is better.

---

## Q6 — Lamartina's "intermediate risk" population

**Source.** [C-S20] Lamartina L, Durante C, Filetti S, Cooper DS. *Low-risk differentiated thyroid cancer
and radioiodine remnant ablation: a systematic review of the literature.* J Clin Endocrinol Metab
2015;100(5):1748–1761. PMID 25679996. DOI 10.1210/jc.2014-3882.
Obtained: Europe PMC core record, full structured abstract, verbatim.

**Verbatim — Methods (what an "OP" is and how patients were grouped):**

> "From a PubMed search, we selected original papers (OPs) using the following inclusion criteria: 1) DTC;
> 2) **LR and IR patients**; 3) non-RRA-treated patients or RRA-treated vs non-RRA-treated groups; 4) a
> report of the outcome of cancer recurrence; and 5) publication since 2008."

**Verbatim — the sentence carrying the counts:**

> "No OP demonstrating RRA benefit on recurrence in LR patients was found; two OPs found no evidence of
> benefit. **We found 11 OPs that observed some benefit in reducing recurrence rates with RRA in IR
> patients and 13 OPs that failed to show benefit from RRA in this group.**"

**Verbatim — Conclusions:**

> "There is no evidence of RRA benefit in recurrence prevention for LR patients. There are conflicting
> data on IR patients and only a few studies with homogenous and properly stratified populations."

**Which classification.** Published May 2015; Cooper chaired the ATA 2015 task force. LR and IR are
**ATA low risk and ATA intermediate risk in the three-tier system** — the categories in force when the
review was written. The four-tier 2025 system (low <10% / low-intermediate 10–15% / intermediate-high
≥16–30% / high >30%) did not exist for another decade. There is no reading on which "IR" in this paper
means "the middle two tiers of the 2025 four-tier system".

**Verdict: FINDING UPHELD.**

The English article attaches the counts to the 2025 system's middle two boxes: "For the two middle boxes,
'may be considered' is a conditional recommendation on low certainty[1]. … A systematic review lays it
barer still: **in this group**, 11 observational studies saw a benefit and 13 did not[6]." "In this group"
resolves to the 2025 four-tier middle two. It should resolve to ATA 2015 three-tier intermediate — a
differently drawn population, from a review published before the 2015 guideline it belongs to, let alone
the 2025 one. The article demonstrates elsewhere in the same piece that it knows how to flag this
("that analysis used the older three-tier stratification", on the leukaemia data), which makes the
omission here a slip rather than a policy.

Two smaller points that hold: the studies really are observational ("original papers", non-randomised),
and the article says so; and the 11/13 split is the review's own, not a secondary count.

**Wording I would defend:**

> The guideline explains its own softness in the middle — there are very few studies of people who sit
> only in the middle. A systematic review from the three-tier era lays it barer still: among people
> classed intermediate risk under the older three-tier system, 11 observational studies saw a benefit from
> ablation and 13 did not, and its authors add that only a few of those studies had properly stratified
> populations. The boundaries have been redrawn since — that middle is not exactly today's two middle
> boxes — but the shape of the disagreement has not changed. The literature itself says two things at
> once. Two doctors saying two things to you is not strange.

---

## Q7 — overall survival in the radioiodine-refractory trials

**The sentence under test.** Article body: "What these drugs buy is time with the disease held down, not a
cure; on overall survival, **not one of the trials above produced a significant difference**." Card text
(`meta/D-en.json`): "on overall survival, not one of the phase 3 trials produced a significant difference."

### SELECT — Schlumberger et al., N Engl J Med 2015;372(7):621–630. PMID 25671254
Europe PMC core record (abstract, verbatim). **Full text could not be obtained** — no PMCID, not OA.
Registry: ClinicalTrials.gov NCT01321554, API v2, results section present.

> Methods, verbatim: "…we randomly assigned 261 patients to receive lenvatinib … and 131 patients to
> receive placebo. **At the time of disease progression, patients in the placebo group could receive
> open-label lenvatinib.** The primary end point was progression-free survival. **Secondary end points
> included the response rate, overall survival, and safety.**"
> Results, verbatim: "**The median overall survival was not reached in either group.**"

Registry, NCT01321554 results, outcome measure "Overall Survival (OS)": type SECONDARY; description
"Overall survival measured from the date of randomization until date of death from any cause.
**Overall survival is adjusted with rank preserving structural failure time**"; both arms report median
NA (not reached), lower CI limits 22.0 and 14.3 months; **zero posted statistical analyses** — no hazard
ratio, no p-value.

- Tested? OS was a prespecified secondary endpoint. **No significance test is reported** in the abstract
  or in the registry results.
- Hazard ratio published? **No** — not in the abstract, not in the registry. Could not check the NEJM body.
- Crossover permitted? **Yes**, on progression; the registry's OS analysis is RPSFT-adjusted, which is a
  crossover correction and therefore confirms crossover occurred.
- What the paper says: median OS not reached in either group. Nothing more.

### DECISION — Brose et al., Lancet 2014;384(9940):319–328. PMID 24768112, PMCID PMC4366116
Obtained: `https://pmc.ncbi.nlm.nih.gov/articles/PMC4366116/` (author manuscript), HTTP 200, full text read.
(Two earlier attempts hit a reCAPTCHA interstitial; the third succeeded.)

> Results, verbatim: "**There was no statistically significant difference in OS (HR, 0·80; 95%CI,
> 0·54–1·19; P=0·14)** … **Median OS had not been reached at the time of primary analysis. A total of 150
> (71·4%) patients receiving placebo crossed over to receive open-label sorafenib at progression.**"
> Discussion, verbatim: "Median OS was not reached in either arm and there was no statistically
> significant difference in OS at data cut-off. **OS results may be confounded by post-progression
> crossover from placebo to open-label sorafenib by the majority of placebo patients.**"
> Methods, verbatim: "**Secondary endpoints included overall survival (OS)**…"

- Tested? Yes. HR published? Yes, 0.80 (95% CI 0.54–1.19, P=0.14). Crossover? Yes, 71.4% of placebo
  patients. The authors themselves flag the OS result as confounded.

### COSMIC-311 — interim, Brose et al., Lancet Oncol 2021;22(8):1126–1138. PMID 34237250
Europe PMC core record (abstract, verbatim). **Full text could not be obtained** — no PMCID, not OA.

> Methods, verbatim: "**Patients receiving placebo could cross over to open-label cabozantinib on disease
> progression confirmed by blinded independent radiology committee (BIRC).** The primary endpoints were
> objective response rate … and progression-free survival …"

The abstract **reports no overall-survival result at all**. Median follow-up was 6.2 months (ITT).
Whether the 2021 body reports an OS figure could not be checked.

### COSMIC-311 — extended analysis, Brose et al., Cancer 2022;128(24):4203–4212. PMID 36259380, PMC10092751 (OA)
Obtained: `/europepmc/webservices/rest/PMC10092751/fullTextXML`, HTTP 200, full text read.

> Results, verbatim: "There were 37 deaths from any cause (22%) among the 170 patients assigned to the
> cabozantinib arm and 21 (24%) among the 88 patients assigned to the placebo. … **Despite 40 patients
> crossing over from the placebo to cabozantinib, there was a trend for improved survival in the
> cabozantinib arm with an HR of 0.76 (95% CI, 0.45–1.31).**"
> Discussion, verbatim: "In agreement with the previous analysis, **OS favored cabozantinib, but
> interpretation is limited by the crossover of patients from the placebo to open-label cabozantinib.
> The study was unblinded on April 16, 2021, to enable the potential crossover of patients assigned to the
> placebo to receive cabozantinib treatment, and this will confound future analyses of OS.**"
> Methods, verbatim: "**Other efficacy end points included overall survival (OS…)**" — i.e. not a primary
> endpoint, and this analysis is described in the abstract as "an exploratory analysis using an extended
> datacut".

- Tested? Descriptively. HR published? Yes, 0.76 (95% CI 0.45–1.31) — non-significant, point estimate
  favouring the drug. Crossover? Yes, 40 placebo patients; the authors say twice that OS interpretation is
  limited and will be confounded going forward.

### BRAF phase III (dabrafenib + trametinib) — Lancet Oncol 2026;27(8):994–1003. PMID 42442381
Europe PMC core record (abstract, verbatim). **Full text could not be obtained** — no PMCID, not OA.
Registry: ClinicalTrials.gov NCT04940052, API v2.

> Methods, verbatim: "The primary endpoint was progression-free survival … **The secondary outcomes were
> overall survival**, overall response rate, duration of response, and safety. This trial is registered
> with ClinicalTrials.gov, NCT04940052, **and is ongoing.**"
> Findings, verbatim: "**An interim analysis of overall survival did not achieve significance for
> dabrafenib plus trametinib over placebo (stratified HR 0·66, 95% CI 0·36–1·19; p=0·083).**"

Registry NCT04940052, verbatim: "**Patients randomized to the placebo arm who experience disease
progression as per RECIST 1.1 confirmed by BIRC and meet eligibility criteria will have the option to
cross over to the open-label combination of dabrafenib plus trametinib.**" The results section carries a
named "Crossover Population Set" and crossover arms, so crossover both was permitted and happened.

- Tested? Yes, at interim. HR published? Yes, stratified 0.66 (95% CI 0.36–1.19, p=0.083). Crossover?
  Yes, by protocol. Trial still running; OS not mature.

### Verdict: PARTLY — the blanket sentence is defensible as a statement of fact and misleading as a
### statement of evidence.

Literally, nothing contradicts it: no trial reported a statistically significant OS advantage. But the
sentence implies four negative survival tests, and that is not what the record shows.

1. **SELECT never published an overall-survival hazard ratio or significance test at all.** What it
   reported is that median OS was not reached in either arm — a statement about immaturity, not about
   equivalence. Saying it "produced no significant difference" credits the trial with a result it did not
   report.
2. **OS was a secondary or exploratory endpoint in every one of the four.** None was powered for it.
3. **All four permitted placebo patients to cross to active drug on progression** — 71.4% in DECISION, 40
   patients in COSMIC-311, by protocol in SELECT and in the BRAF trial — and two of the four say in their
   own words that this confounds OS ("may be confounded by post-progression crossover"; "this will confound
   future analyses of OS"). A design that hands the control arm the drug cannot answer the survival
   question, and was never meant to.
4. **The two hazard ratios that do exist both point toward the drug**: cabozantinib 0.76 (0.45–1.31),
   dabrafenib plus trametinib 0.66 (0.36–1.19). Non-significant, small numbers, wide intervals — but
   "produced no significant difference" invites the reader to hear "made no difference", which these
   intervals do not license in either direction.
5. **The BRAF figure is an interim analysis of a trial still enrolling follow-up**, which the paper says
   outright.

**Wording I would defend** (body):

> What these drugs buy is time with the disease held down. Whether they lengthen life is a question none
> of these trials was built to answer: overall survival was a secondary endpoint in every one, and every
> one let people on placebo move to the active drug once their disease progressed — 71.4% of them did in
> the sorafenib trial, and its authors write that the survival result "may be confounded" by exactly that.
> So the record reads: sorafenib, no significant difference, hazard ratio 0.80 (0.54 to 1.19);
> cabozantinib, a non-significant hazard ratio of 0.76 (0.45 to 1.31) that the authors say is limited by
> crossover; dabrafenib plus trametinib, an interim analysis that did not reach significance, hazard ratio
> 0.66 (0.36 to 1.19), in a trial still running; lenvatinib, no hazard ratio published at all — only that
> median survival had not been reached in either arm. No survival benefit has been shown. That is not the
> same sentence as "there is none", and I am not going to write the second one.

**Wording I would defend** (card):

> What these drugs buy is time with the disease held down, not a cure — no trial has shown a survival
> benefit, and none was designed to look for one. When to start is a decision you are entitled to take
> part in.

---

## Sources that could not be obtained this round

| Source | Why | What it would have settled |
|---|---|---|
| Sanabria 2022, Ann Surg 276(1):66–73, full text | Closed access; Unpaywall `is_oa: false`, zero OA locations; DOI resolves to journals.lww.com, 403 | The authors' own definition and sign of the NNT = 500 (Q3). The abstract is enough to establish the direction of the event counts and the absence of benefit. |
| IoN, Lancet 2025;406(10498):52–62, full text | Europe PMC `isOpenAccess: N`, no PMCID | The estimator used for the 0.5-percentage-point absolute risk difference (Q5) |
| SELECT, NEJM 2015;372(7):621–630, full text | No PMCID, not OA | Whether an OS hazard ratio appears in the body (Q7). Abstract and ClinicalTrials.gov results both show none. |
| COSMIC-311 interim, Lancet Oncol 2021;22(8):1126–1138, full text | No PMCID, not OA | Whether the 2021 paper reported any OS figure (Q7). The 2022 paper's "in agreement with the previous analysis" implies it did. |
| BRAF phase III, Lancet Oncol 2026;27(8):994–1003, full text | No PMCID, not OA | Crossover uptake numbers (Q7). Protocol-level crossover confirmed from NCT04940052. |

## Route notes for whoever verifies next

- `europepmc.org/articles/<PMCID>?pdf=render` returned **403** for PMC13090833 this round; the working
  route for ATA 2025 is `https://pmc.ncbi.nlm.nih.gov/articles/PMC13090833/` with a desktop browser
  User-Agent. `/europepmc/webservices/rest/PMC13090833/fullTextXML` returns 404 (subscription content).
- PMC HTML rate-limits to a Google reCAPTCHA interstitial after two or three rapid requests. Detect it by
  grepping the saved file for `recaptcha`; a 60-second pause cleared it both times. The agent proxy status
  endpoint showed `recentRelayFailures: []` throughout, so these were origin-side blocks, not policy denials.
- Kim 2024 (PMC11392158) and COSMIC-311 2022 (PMC10092751) are both open access and come back cleanly from
  `/europepmc/webservices/rest/<PMCID>/fullTextXML`.
