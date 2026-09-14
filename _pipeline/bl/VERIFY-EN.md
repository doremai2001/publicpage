# VERIFY-EN — source-verification pass, five questions

Date: 2026-09-14. Every quotation below was read at the URL given in the same section.
Nothing here is from memory. Where I could not reach a source I say so.

---

## Q1 — Müller 2023: is 12.823 (2.927–22.720) an odds ratio or a regression coefficient?

**Paper:** Müller G, Butea-Bocu MC, Beyer B, Tully KH, Berg S, Roghmann F, Noldus J, Bahlburg H.
*Prospective evaluation of return to work, health-related quality of life and psychosocial distress
after radical cystectomy: 1-year follow-up in 230 employed German bladder cancer patients.*
World J Urol. 2023;41(10):2707–2713. DOI 10.1007/s00345-023-04570-1. PMID 37702752. PMCID PMC10581950. Open Access.

**URL read:** `https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10581950/fullTextXML`
(full text also retrieved via PubMed Central through the PubMed MCP tool; DOI:
[10.1007/s00345-023-04570-1](https://doi.org/10.1007/s00345-023-04570-1)). According to PubMed / PMC.

### What the paper actually says, verbatim

Results, "Quality of life" section:

> "Linear regression analysis identified RTW as the only predictor for better global HRQoL at T4
> (OR [odds ratio] 12.823, 95% CI [confidence interval] 2.927–22.720, p = 0.012). Urinary diversion,
> age, sex, tumor stage or lymph node metastases were not predictors in this model."

Abstract, Results (same number, same label):

> "Linear regression analysis identified RTW as the only predictor for better HRQoL at T4
> (OR [odds ratio] 12.823, 95% CI [confidence interval] 2.927–22.720, p = 0.012)."

Discussion, restated without a number:

> "Linear regression analysis identified RTW as the only predictor for improved global HRQoL at T4."

### Dependent variable, predictor, and what the paper gives us

- **Dependent variable:** global HRQoL at T4. T4 is defined in Methods as **12 months after surgery**
  ("HRQoL and PD were evaluated at the beginning (T1) and end (T2) of IR as well as both 6 (T3) and
  12 months (T4) after surgery"), and HRQoL is the **EORTC QLQ-C30** "Global health status/quality of
  life" scale — a continuous 0–100 score. Table 2 gives its T4 value: **Total mean 65.5 (SD 21.3)**.
- **Predictor:** RTW (return to work) at T4. The paper also reports the unadjusted gap on that same
  0–100 scale: "At T4, patients with RTW had better global HRQoL than patients without RTW
  (mean 69.8 (SD 18.9) vs. 55.1 (SD 25.4); p = 0.004)."
- **There is no table for this model.** The paper has four tables. Table 4 is a *different* model —
  "**Table 4  Logistic regression analysis to identify predictors for return to work at 12 months after
  radical cystectomy**", whose columns are headed "**Univariate | Multivariate | OR (95% CI) | p |
  OR (95% CI) | p**" with the footnote "**OR odds ratio, CI confidence interval**". That is where
  7.842 and 0.220 live, and in that table "OR" is correct because the outcome (RTW yes/no) is binary.
  The 12.823 figure appears **only in running text**, with no table, no column header, and no footnote.

### Verdict

**The draft is right about what the source prints, and the source is internally inconsistent.**

Müller 2023 itself writes "OR [odds ratio] 12.823" — twice, in the abstract and in the Results — inside
a sentence that says the analysis was a **linear regression**. So the Chinese sentence's 勝算比 is a
faithful transcription of the authors' own label, not a translation error introduced by the draft.

But the label cannot be correct as printed: an odds ratio is not a quantity a linear regression on a
continuous QLQ-C30 score produces, and the paper supplies **nothing** — no table, no B column, no
footnote, no erratum (I searched Europe PMC for a correction: `TITLE:"Correction" AND TITLE:"return to
work" AND TITLE:"radical cystectomy"` → hitCount 0; and a search on the DOI stem `s00345-023-04570`
returns the single original article only) — that would let anyone establish from the source that it is
a B coefficient. Two things in the paper are consistent with a B coefficient on the 0–100 scale and I
record them as observations, explicitly **not** as the paper's own words: the interval is arithmetically
symmetric around the point estimate (2.927 + 22.720)/2 = 12.8235, and the unadjusted RTW-vs-no-RTW gap
on that same scale is 69.8 − 55.1 = 14.7 points, the right order of magnitude for a 12.823-point
coefficient. **I could not obtain a statement in the source resolving this.**

**Consequence for the article:** the number cannot be presented as 勝算比 / "odds ratio" and it also
cannot safely be presented as "a 12.8-point gain in quality-of-life score", because the source does not
say that either. The defensible move is to drop the number and keep only the finding the paper states
in words — "linear regression analysis identified RTW as the only predictor for better global HRQoL at
T4" — plus the plain unadjusted means (69.8 vs 55.1, p = 0.004), which *are* unambiguous and quotable.

---

## Q2 — EV-302 / enfortumab vedotin: which population does each figure come from?

**Source:** U.S. FDA, PADCEV (enfortumab vedotin-ejfv) for injection, prescribing information.
Label version 18, `effective_time` **20260804**, SPL set id **b5631d3e-4604-4363-8f20-11dfc5a4a8ed**.

**URL read:** `https://api.fda.gov/drug/label.json?search=openfda.brand_name:"PADCEV"&limit=1`
(same SPL is viewable at `https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=b5631d3e-4604-4363-8f20-11dfc5a4a8ed`).

### The label's own population key — the sentence that settles all of this

Section 6.1 Adverse Reactions, verbatim:

> "The safety population described in the WARNINGS AND PRECAUTIONS reflect exposure to PADCEV 1.25 mg/kg
> in combination with intravenous pembrolizumab for the treatment of MIBC in **570 patients** in EV-303
> (NCT03924895) and EV-304 (NCT04700124) and for the treatment of la/mUC in **564 patients** in EV-302
> (NCT04223856) and EV-103 (NCT03288545); PADCEV as a single agent at 1.25 mg/kg in **720 patients** in
> EV-301 (NCT03474107), EV‑201 (NCT03219333), EV-203 (NCT04995419), EV-101 (NCT02091999), and EV-102
> (NCT03070990)."

So **nothing in section 5 is reported on the 440-vs-433 EV-302 randomised population.** Section 5 runs
on three pooled populations: 570 (MIBC combination), 564 (la/mUC combination), 720 (monotherapy).

The 440/433 figures are real but belong to section 6.1 only. Verbatim, section 6.1, "Previously
Untreated LA/mUC — EV-302":

> "The safety of PADCEV in combination with intravenous pembrolizumab was evaluated in an open-label,
> randomized, multicenter trial (EV-302) in patients with la/mUC. Patients received either PADCEV
> 1.25 mg/kg and pembrolizumab (n=440) or gemcitabine and platinum chemotherapy (either cisplatin or
> carboplatin) (n=433)."

### Figure 1 — median time to first grade ≥2 peripheral neuropathy, 6 months (range 0.3–25)

Section **5.4 Peripheral Neuropathy**, verbatim:

> "When PADCEV was given in combination with intravenous pembrolizumab for the treatment of la/mUC,
> 67% of the **564 patients** treated with combination therapy had peripheral neuropathy of any grade,
> 36% had Grade 2 neuropathy, and 7% had Grade 3 neuropathy. The incidence of peripheral neuropathy
> occurred at a higher rate when PADCEV was given in combination with intravenous pembrolizumab compared
> to PADCEV as a single agent. **The median time to onset of Grade ≥2 peripheral neuropathy was 6 months
> (range: 0.3 to 25 months)** [see Adverse Reactions ( 6.1 )]."

For contrast, the monotherapy figure in the same section is different: "The median time to onset of
Grade ≥2 peripheral neuropathy was **4.9 months (range: 0.1 to 20 months)**" — for the 720-patient
single-agent population.

→ **n = 564 pooled la/mUC combination population (EV-302 + EV-103). `brief/D.md` is correct.**

### Figure 2 — 373 patients, 13% resolved, 87% not fully resolved

Same section 5.4, the sentence immediately after the one above:

> "Of the patients who experienced neuropathy and had data regarding resolution (**n=373**), **13% had
> complete resolution, and 87% of patients had residual neuropathy at last evaluation**. Of the patients
> with residual neuropathy at last evaluation, 45% (146/326) had Grade ≥2 neuropathy."

→ **Also the n = 564 la/mUC combination population; 373 is the subset of those 564 who had neuropathy
and had resolution data. `brief/D.md` is correct.** One wording note: the label says "**had residual
neuropathy at last evaluation**", not "not fully resolved" — "residual at last evaluation" is the
honest phrasing and should be kept, because the label is reporting a snapshot at last assessment, not a
permanent state.

### Figure 3a — the Stevens-Johnson syndrome / toxic epidermal necrolysis warning

**This is the one `brief/D.md` gets wrong.** SJS/TEN is not a section-5.1 finding attached to the 564
la/mUC population. It is a **boxed warning**, stated for the drug as a whole, verbatim:

> "**WARNING: SERIOUS SKIN REACTIONS** • PADCEV can cause severe and fatal cutaneous adverse reactions
> including Stevens-Johnson syndrome (SJS) and Toxic Epidermal Necrolysis (TEN), which occurred
> predominantly during the first cycle of treatment, but may occur later. • Closely monitor patients for
> skin reactions. • Immediately withhold PADCEV and consider referral for specialized care for suspected
> SJS or TEN or severe skin reactions. • Permanently discontinue PADCEV in patients with confirmed SJS
> or TEN; or Grade 4 or recurrent Grade 3 skin reactions…"

Section **5.1 Skin Reactions** opens with the same population-free statement:

> "Severe cutaneous adverse reactions, including fatal cases of SJS or TEN occurred in patients treated
> with PADCEV. SJS and TEN occurred predominantly during the first cycle of treatment but may occur later."

The **only** place in section 5.1 where SJS is enumerated inside a named population is the **MIBC**
combination population of **570**, not the la/mUC 564:

> "Skin reactions occurred in 65% (all grades) of the **570 patients** treated with PADCEV in combination
> with intravenous pembrolizumab for the treatment of MIBC in clinical trials… Grade 3-4 skin reactions
> occurred in 13% of patients (Grade 3: 12%, Grade 4: 1.1%), including maculo-papular rash, rash,
> **Stevens-Johnson syndrome**, dermatitis… **A fatal reaction of TEN occurred in one patient (0.2%).**"

The la/mUC **564** paragraph in the same section names no SJS and no TEN; its fatal event was different:

> "Skin reactions occurred in 70% (all grades) of the **564 patients** treated with PADCEV in combination
> with intravenous pembrolizumab for the treatment of la/mUC in clinical trials… Grade 3-4 skin reactions
> occurred in 17% of patients (Grade 3: 16%, Grade 4: 1%), including maculo-papular rash, bullous
> dermatitis, dermatitis, exfoliative dermatitis, pemphigoid, rash, erythematous rash, macular rash, and
> papular rash. **A fatal reaction of bullous dermatitis occurred in one patient (0.2%).**"

→ **The SJS/TEN warning is a boxed, drug-wide warning ("in patients treated with PADCEV"), not a
564-population finding. `brief/D.md`'s attribution to the n=564 la/mUC pool is not supported.** For a
patient-facing article this is the *safer* correction, not a weaker one: the warning applies to anyone
on the drug, and should be written that way rather than fenced off to one trial population.

### Figure 3b — median onset of hyperglycaemia of 0.5 months

Section **5.2 Hyperglycemia**, verbatim:

> "Hyperglycemia and diabetic ketoacidosis (DKA), including fatal events, occurred in patients with and
> without pre‑existing diabetes mellitus, treated with PADCEV. Patients with baseline hemoglobin A1C ≥8%
> were excluded from clinical trials. In clinical trials of PADCEV **as a single agent, 17% of the 720
> patients** treated with PADCEV developed hyperglycemia of any grade; 7% of patients developed Grade 3-4
> hyperglycemia (Grade 3: 6.5%, Grade 4: 0.6%). Fatal events of hyperglycemia and diabetic ketoacidosis
> occurred in one patient each (0.1%). The incidence of Grade 3-4 hyperglycemia increased consistently in
> patients with higher body mass index and in patients with higher baseline A1C. **The median time to
> onset of hyperglycemia was 0.5 months (range: 0 to 20 months).**"

→ **n = 720 enfortumab-vedotin monotherapy population. `brief/D.md` is correct.**

### Verdict

**The draft is wrong on one of three, right on two — and wrong on the framing paragraph.**

1. Median time to grade ≥2 neuropathy 6 months (0.3–25): **n=564 la/mUC combination pool** — brief correct.
2. 373 / 13% / 87%: **subset of the same n=564 pool** — brief correct (prefer "residual at last evaluation").
3. SJS/TEN: **boxed warning, drug-wide, not the n=564 pool** — brief wrong, correct it.
4. Hyperglycaemia median onset 0.5 months: **n=720 monotherapy pool** — brief correct.
5. **The paragraph's own opening is the real defect:** it defines its population as "the EV-302 safety
   population, 440 versus 433" and then reports four figures, **none of which come from that population.**
   The label says in plain words that section 5 runs on the 570 / 564 / 720 pools. The paragraph needs to
   stop claiming 440-vs-433 as the denominator for anything in section 5.

---

## Q3 — Pyrgidis: what is the 11% a proportion of?

**Paper:** Pyrgidis N, Schulz GB, Scilipoti P, et al. *The Role of Salvage Cystectomy After Prior
Trimodality Therapy: A Multinational Match-paired Analysis.* Eur Urol Focus. 2026;12(1):88–95.
DOI 10.1016/j.euf.2025.04.028. PMID 40300977. **Not open access** — abstract only.

**URL read:** `https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:"10.1016/j.euf.2025.04.028"&resultType=core&format=json`
According to PubMed / Europe PMC. DOI: [10.1016/j.euf.2025.04.028](https://doi.org/10.1016/j.euf.2025.04.028)

### Verbatim, from the "Key findings and limitations" section of the abstract

> "We included **118 patients (59 per group)** with a median age of 73 yr (interquartile range [IQR]:
> 66–79). **Seven patients (11%) developed severe, grade 4 or 5 perioperative complications during RC
> after prior TMT.** The 30- and 90-d survival rates of salvage RC after prior TMT were 93% and 91%,
> respectively."

And the design sentence that defines the two groups, from Methods:

> "Patients undergoing salvage RC after prior TMT due to recurrence in the urinary bladder from 13
> high-volume centers were matched with a propensity score analysis in a 1:1 ratio with patients without
> prior TMT undergoing primary RC."

### Verdict

**The draft is wrong; the source says the 11% is 7 of the 59-patient salvage arm, not of 118.**

The sentence is explicit: the complications are "**during RC after prior TMT**" — i.e. within the
salvage arm only. 7/59 = 11.9%, which rounds to the 11% the authors print; 7/118 = 5.9%, which they do
not print. The 118 is the *matched-pair total* (59 salvage + 59 primary). Any Chinese sentence that sets
118 as the denominator and then says 7 人（11%）makes the reader compute 5.9% and conclude one of the two
numbers is a typo. The same applies to the 30-day and 90-day survival of 93% and 91%, which the abstract
also ties explicitly to "salvage RC after prior TMT" — the 59, not the 118.

---

## Q4 — the haematuria pair: five-year survival 73.3% in women vs 78.2% in men

### Step 1 — where the article's proximate source puts it

**Source:** Microhematuria: AUA/SUFU Guideline, published 2020, amended 2025, unabridged version.
**URL read:** `https://www.auanet.org/documents/Guidelines/PDF/2025%20Guidelines/MH%20Unabridged%20FINAL.pdf`
(linked from `https://www.auanet.org/guidelines-and-quality/guidelines/microhematuria`)

Introduction, verbatim:

> "Women with hematuria have been especially prone to delays in evaluation, often due to practitioners
> ascribing hematuria to a urinary tract infection (UTI) or gynecologic source, resulting in inadequate
> evaluation and delay in cancer diagnosis.19,25 … In turn, despite having a lower incidence of bladder
> cancer than men, **women diagnosed with bladder cancer have a lower 5-year survival rate than men
> (73.3% versus 78.2%), which may be in part attributable to delay in diagnosis leading to higher stage
> disease at diagnosis.27**"

Reference 27 in that PDF's bibliography, verbatim:

> "27.  Howlader N, N. A., Krapcho M et al: Seer cancer statistics review, 1975-2016, national cancer
> institute. Bethesda, md, https://seer.Cancer.Gov/csr/1975_2016/, based on november 2018 seer data
> submission, posted to the seer web site. 2019;"

So the pair is **not from a study at all** — no cohort, no protocol, no stage-restricted population.
It is a cell from a **national registry statistics report**.

### Step 2 — the primary source

**Source:** SEER Cancer Statistics Review 1975–2016, National Cancer Institute, **Table 27.8**.
**URL read:** `https://seer.cancer.gov/archive/csr/1975_2016/results_merged/topic_survival.pdf`

Table header, verbatim:

> "**Table 27.8 — Cancer of the Urinary Bladder (Invasive and In Situ)** —
> **5-Year Relative and Period Survival (Percent) by Race, Sex, Diagnosis Year, Stage and Age** —
> SEER Cancer Statistics Review 1975-2016"

Column structure: `All Races (Total | Males | Females) | Whites (Total | Males | Females) | Blacks (Total | Males | Females)`.

The exact pair appears in the **5-Year Period Survival** block, All Races:

> "**5-Year Period Survival (Percent)** … **2015**   77.0   **78.2**   **73.3**   77.5   78.4   74.4   63.5   67.1   56.9"

with the method footnote, verbatim:

> "Period survival provides a 2015 estimate of survival by piecing together the most recent conditional
> survival estimates from several cohorts. It is computed here using three year calendar blocks
> (2010-2012: 0-1 year survival), (2009-2011: 1-2 year survival), (2008-2010: 2-3 year survival),
> (2007-2009: 3-4 year survival), (2006-2008: 4-5 years survival)."

A near-identical pair sits in the relative-survival-by-stage block and I record it so nobody mistakes
one for the other: "**Stage: All Stages**   77.1   **78.3**   **73.2**" for 2009–2015. The AUA prints
78.2/73.3, which matches the **2015 period-survival row** exactly; the guideline does not say which row
it took, so I note the near-match rather than assert it away.

### Step 3 — the answer to the actual question

- **Population:** everyone in the registry with a bladder cancer diagnosis — and note the table title:
  "**Cancer of the Urinary Bladder (Invasive and In Situ)**". SEER counts **in situ** bladder tumours as
  cases, which most cancer sites do not.
- **Registry:** SEER. Footnote c, verbatim: "**SEER 18 areas** (San Francisco, Connecticut, Detroit,
  Hawaii, Iowa, New Mexico, Seattle, Utah, Atlanta, San Jose-Monterey, Los Angeles, Alaska Native
  Registry, Rural Georgia, California excluding SF/SJM/LA, Kentucky, Louisiana, New Jersey and Georgia
  excluding ATL/RG). … **Based on follow-up of patients into 2016.**"
- **Years:** diagnosis years **2009–2015** for the stage distribution and the stage-specific survival;
  the 78.2/73.3 period estimate is assembled from calendar blocks 2006–2012 as quoted above.
- **Denominator:** the stage-distribution block gives it, verbatim:
  "**Stage Distribution (%) 2009-2015 … All Stages … Number of cases   90,571   68,619   21,952**"
  (All Races total / Males / Females).
- **Stage mix — and this is the decisive part.** The SEER table states it outright, in the block
  immediately under the survival rows, All Races (Total | Males | Females):

> "**In Situ   51   52   50** / **Localized   34   34   33** / **Regional   7   7   8** /
> **Distant   5   4   6** / **Unstaged/Unknown   3   3   3**"

  with footnote e: "Stage at diagnosis is classified using SEER Summary Stage 2000. Stage distribution
  percentages may not sum to 100 due to rounding."

### Verdict

**The draft is wrong to use this pair at all under the topic's stated rule — and the source does state
its stage composition, which is what makes it unusable.**

Yes, it is a whole-cohort, all-stage figure: SEER Table 27.8, urinary bladder, **invasive and in situ
combined**, SEER 18, diagnoses 2009–2015, n = 90,571. And the source *does* give the stage mix, in the
same table: **51% in situ and 34% localized — roughly 85% of the denominator sits on the non-muscle-
invasive side of the line**, with only 7% regional and 5% distant. So a 73.3%-vs-78.2% "five-year
survival" is overwhelmingly a statement about NMIBC, and the article's rule — no bladder-cancer survival
figure without saying which side of the NMIBC/MIBC line it belongs to — cannot be satisfied by writing
"all stages"; it would have to say "a mix that is about half carcinoma in situ".

Two further cautions from the source itself, both quotable: the AUA's own wording is hedged — "**which
may be in part attributable to** delay in diagnosis" — so the pair is not evidence of a delay effect;
and SEER Table 27.8 shows the same sex gap is present *within* stage strata ("**Localized   69.5   71.8
   62.0**", "**Regional   36.3   37.2   34.0**"), so the whole-cohort gap is not simply a stage-mix
artefact either. If the article wants to make the sex-disparity point, the stage-specific rows are the
honest place to make it; the headline pair is not.

---

## Q5 — Sylvester 2016: the HR 1.26 and the 12.0% vs 11.2%

**Paper:** Sylvester RJ, Oosterlinck W, Holmang S, et al. *Systematic Review and Individual Patient Data
Meta-analysis of Randomized Trials Comparing a Single Immediate Instillation of Chemotherapy After
Transurethral Resection with Transurethral Resection Alone in Patients with Stage pTa-pT1 Urothelial
Carcinoma of the Bladder: Which Patients Benefit from the Instillation?* Eur Urol. 2016;69(2):231–244.
DOI 10.1016/j.eururo.2015.05.050. PMID 26091833. **Not open access.**

**URL read:** `https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:26091833&resultType=core&format=json`
According to PubMed / Europe PMC. DOI: [10.1016/j.eururo.2015.05.050](https://doi.org/10.1016/j.eururo.2015.05.050)

**What I could not get:** the full text. `https://doi.org/10.1016/j.eururo.2015.05.050` redirects to
`https://linkinghub.elsevier.com/retrieve/pii/S030228381500456X`, which returned no content to WebFetch.
Europe PMC reports `isOpenAccess: N` and no PMCID. So **the median duration of follow-up is not something
I could obtain** — it is not in the abstract and the full text was unreachable. Everything below is from
the abstract, which is enough to settle the question asked.

### The population, verbatim (Evidence synthesis)

> "A total of 13 eligible studies were identified. IPD were obtained for 11 studies randomizing **2278
> eligible patients, 1161 to TURB and 1117 to a single instillation** of epirubicin, mitomycin C,
> pirarubicin, or thiotepa. A total of 1128 recurrences, 108 progressions, and **460 deaths (59 due to
> bladder cancer [BCa])** occurred."

### The sentence carrying both numbers, verbatim

> "The instillation did not prolong either the time to progression or death from BCa, but it **resulted
> in an increase in the overall risk of death (HR: 1.26; 95% CI, 1.05-1.51; p=0.015; 5-yr death rates
> 12.0% vs 11.2%), with the difference appearing in patients with an European Organization for Research
> and Treatment of Cancer (EORTC) recurrence score ≥5.**"

### The authors' own interpretation, verbatim (Conclusions, then Patient summary)

> "A single immediate instillation reduced the risk of recurrence, except in patients with a prior
> recurrence rate of more than one recurrence per year or an EORTC recurrence score ≥5. It does not
> prolong either time to progression or death from BCa. **The instillation may be associated with an
> increase in the risk of death in patients at high risk of recurrence in whom the instillation is not
> effective or recommended.**"

> "A single instillation of chemotherapy immediately after resection reduces the risk of recurrence in
> non-muscle-invasive bladder cancer; however, **it should not be given to patients at high risk of
> recurrence due to its lack of efficacy in this subgroup.**"

### Settling the question

The grammar of the abstract sentence settles it and both halves of the draft's suspicion are half-right:

- **The HR 1.26 is the whole-cohort estimate**, not a high-risk-subgroup estimate. Its subject is "the
  instillation" — the same subject as the two preceding whole-cohort clauses in that sentence (time to
  progression, death from BCa) — and its outcome is "**the overall risk of death**", i.e. **all-cause
  mortality**, across all 2278 randomised patients (1161 vs 1117). The `≥5` subgroup appears only in a
  trailing qualifier saying **where the difference showed up**, not what the HR was computed on.
- **The 12.0% and 11.2% are also whole-cohort**, and are **5-year all-cause death rates**, the same
  outcome as the HR, read at a single 5-year timepoint.
- **So the mismatch is the second of the two hypotheses, not the first:** a Cox HR over the trials' full
  follow-up versus two point-in-time percentages at 5 years. The abstract does not state the follow-up
  duration, so I cannot quantify how far past 5 years the HR reaches — that is the piece I could not
  obtain — but the HR is not a five-year quantity and the percentages are not a subgroup quantity.

### Verdict

**The draft is wrong on the population label; the source says both the HR 1.26 and the 12.0% vs 11.2%
are whole-cohort (all 2278 patients, pTa–pT1), not "in patients at high risk of recurrence".**

The draft's Chinese sentence — 「在高復發風險者身上整體死亡風險反而上升（HR 1.26 … 五年死亡率 12.0% vs 11.2%）」
— moves both numbers into the high-risk subgroup. What the abstract actually says is that the *increase*
in overall risk of death is a whole-cohort finding whose *difference appeared in* the EORTC recurrence
score ≥5 subgroup. That distinction matters for the article, because the authors' own recommendation
(quoted above) rests on the subgroup *lacking efficacy*, not on a measured subgroup mortality figure.
The accurate rendering is: across all 2278 patients, all-cause mortality was higher with the instillation
(HR 1.26, 95% CI 1.05–1.51, p=0.015; 5-year all-cause death 12.0% vs 11.2%), and the authors report that
this difference was concentrated among patients with an EORTC recurrence score ≥5 — the same patients in
whom the instillation did not reduce recurrence, which is why they say it should not be given to them.

Also worth fixing while here: "五年死亡率" needs to read as **all-cause** death, not bladder-cancer death.
The abstract is explicit that the instillation "did not prolong … death from BCa" and that only 59 of the
460 deaths were from bladder cancer.

---

## Summary table

| # | Question | Verdict |
|---|---|---|
| Q1 | Müller 12.823 — OR or B? | **Could not obtain a resolving statement.** The source itself prints "OR [odds ratio] 12.823" in a sentence saying "Linear regression analysis"; there is no table, no B column, no erratum. The draft faithfully copies the source's own inconsistent label. Drop the number. |
| Q2 | EV-302 / PADCEV label populations | **Mixed.** Neuropathy 6 mo (0.3–25) → n=564 ✓; 373/13%/87% → n=564 ✓; hyperglycaemia 0.5 mo → n=720 ✓; **SJS/TEN → boxed, drug-wide, NOT n=564 ✗**. And the paragraph's "EV-302 safety population, 440 vs 433" framing is wrong for every section-5 figure. |
| Q3 | Pyrgidis 7 patients (11%) | **The draft is wrong.** 11% is 7/59 — the salvage-RC arm — not 7/118. 118 is the matched-pair total. |
| Q4 | 73.3% vs 78.2% | **The draft is wrong to use it.** SEER CSR 1975–2016 Table 27.8, urinary bladder **invasive and in situ**, SEER 18, 2009–2015, n=90,571. Whole-cohort all-stage; the source **does** state the stage mix — **51% in situ, 34% localized** — i.e. ~85% NMIBC. Fails the topic's NMIBC/MIBC rule. |
| Q5 | Sylvester HR 1.26 / 12.0% vs 11.2% | **The draft is wrong on population.** Both are **whole-cohort** (2278 pTa–pT1, 1161 vs 1117), both **all-cause death**. HR = full follow-up; percentages = 5 years. The ≥5 subgroup is where the difference *appeared*, not what was computed. Follow-up duration: could not obtain (non-OA). |
