# Source-verification pass — six factual questions
Date: 2026-09-13. All quotations below are transcribed from the primary source at the URL given.

---

## Q1 — Ogasawara 2021, Biomedicines 9(3):319 (PMID 33801089, PMC8004084)

**URL read:** full text via Europe PMC / PubMed Central, PMCID PMC8004084
(`https://pmc.ncbi.nlm.nih.gov/articles/PMC8004084/`, retrieved through the PubMed MCP
`get_full_text_article` tool; DOI https://doi.org/10.3390/biomedicines9030319)

### (a) Parasagittal — verbatim

> "Parasagittal meningiomas can grow to considerable size before presenting with symptoms []. They mostly present with Jacksonian seizures of the lower limbs or headache and advanced anterior parasagittal meningiomas, which are characteristically present with papilledema and **homonymous hemianopia** []."

### (b) Peritorcular — verbatim

> "Peritorcular meningiomas symptoms are commonly caused by compression of the occipital lobe or the cerebellum and present with a headache with occipital localized pain, papilledema, and **homonymous field deficits**, as well as ataxia, dysmetria, hypotonia, and nystagmus []."

(The empty square brackets are where the reference-number markup sat in the source; the
wording is otherwise exact. The paper uses US spelling "papilledema", not "papilloedema".)

### Direct answer to the question asked
The paper says **"homonymous hemianopia"** (parasagittal) and **"homonymous field deficits"**
(peritorcular). The phrase **"ipsilateral hemianopia" does not appear anywhere in the article.**

**VERDICT: the draft is wrong.** 「同側偏盲」 (ipsilateral hemianopia) misnames the deficit —
the source says *homonymous*, i.e. 同向性偏盲 (the matching half of the visual field in *both*
eyes, contralateral to the lesion). "Ipsilateral" names the wrong side and the wrong concept.

---

## Q2 — Pituitary apoplexy meta-analysis, Front Surg 2025;12:1579498

**URLs read:**
- `https://www.frontiersin.org/journals/surgery/articles/10.3389/fsurg.2025.1579498/full`
- full text XML: `https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12174462/fullTextXML`
(PMID 40535550, PMCID PMC12174462)

### What the OR is attached to — verbatim (Results)

> "However, there were significant differences in recovery from ocular palsy recovery (OR: 0.31; 95% CI 0.10–0.92; *p* = 0.04; Figure 5A) between surgical and conservative treatment groups. Heterogeneity in ophthalmoplegia recovery was low between studies (I² = 0%, p = 0.83; Figure 5A)."

### The outcome definition — verbatim (Methods, "The definition of the outcome")

> "Ophthalmoplegia recovery denotes the resolution or improvement of ophthalmoplegia symptoms post-treatment, often involving dysfunction of the third, fourth, and sixth cranial nerves that lead to eye movement disorders."

### The direction convention — verbatim (Methods, "Statistical analysis")

> "We recorded the number of patients undergoing surgical and conservative treatments both before and after surgery, focusing on the primary observations. The recovery rates for the four main observations were assessed using Reman v5.3. **A fixed-effect model evaluated the pooled odds ratios (OR), where an OR of less than 1 favored surgical treatment, and an OR greater than 1 favored conservative management.** We assessed the heterogeneity between studies using the Cochran Q (chi-square) test and I² statistics."

### Figure captions — verbatim (note the ordering)

> "Figure 5 (A) Comparing the efficacy of **conservative treatments and surgical treatments** for ocular palsy. (B) Funnel plot for detecting and displaying system heterogeneity."

Compare the other three figures, which are ordered the other way round:

> "Figure 3 (A) … the surgical treatment was compared to the conservative treatment for its efficacy in the visual field."
> "Figure 4 (A) Conservative and surgical treatments were compared in terms of their effectiveness in treating pituitary endocrine function."

### Abstract and Conclusion — verbatim

> "The meta-analysis results indicated that surgical treatment significantly improved recovery from ocular muscle paralysis compared to conservative treatment (OR: 0.31; 95% CI 0.10–0.92; *p* = 0.04)."

> "In summary, our findings suggest that surgical intervention is more effective than conservative approaches in improving ocular palsy recovery rates following pituitary apoplexy…"

### Settling the direction

- The outcome variable is **recovery** (ophthalmoplegia/ocular palsy recovery), *not* persistent
  deficit and *not* non-recovery. That is stated explicitly in the outcome definition.
- The paper never writes out a numerator/denominator in words. The only direction statement is
  the methods convention: **"an OR of less than 1 favored surgical treatment."** Under that
  convention the reference/numerator arm for this comparison is the **conservative** group —
  which is consistent with the Figure 5A caption naming conservative first, unlike Figures 2–4.
- So the authors' own claim is that **surgery is better** for ophthalmoplegia recovery, and
  0.31 is the number they attach to that claim.

**VERDICT: the draft's clinical direction is right but its wording is wrong and unsafe to keep.**
The draft 「眼肌麻痺的恢復開刀明顯較好，勝算比 0.31」 states the authors' conclusion correctly
(surgery better), but it invites exactly the misreading the reviewer flagged: an OR of 0.31 read
in the ordinary way ("odds of recovery, surgery vs conservative") would mean surgery is *worse*.
The 0.31 is only "surgery better" because this paper declares a reversed convention in which
OR < 1 favours surgery. Two further cautions worth recording: (i) the paper's own reporting is
internally inconsistent — the pituitary endocrine OR of 0.67 is also < 1, which under the stated
convention would "favour surgery", yet it is reported as no significant difference; (ii) the
Results sentence is ungrammatical ("differences in recovery from ocular palsy recovery"). Do not
quote the bare number as an odds of recovery. Either drop the OR and state the direction in
words, or state it as "OR 0.31 (95% CI 0.10–0.92), reported by the authors under a convention in
which OR < 1 favours surgery".

---

## Q3 — Sheehan et al., SRS for acromegaly, Neurosurgery (DOI 10.1093/neuros/nyy178)

**URL read:** abstract via Europe PMC
`https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:"10.1093/neuros/nyy178"&resultType=core&format=json`
and via the PubMed MCP tool (PMID 29757421, PMCID PMC6505445).

**Access note:** the Results body could **not** be obtained. The PMC record for PMC6505445
returns an empty `full_text` (author-manuscript embargo) and the Europe PMC `fullTextXML`
endpoint returns HTTP 404 for both PMC6505445 and MED/29757421. Everything below is therefore
from the **author-written structured abstract**, which states both figures directly.

### Verbatim (Results section of the abstract)

> "The study cohort comprised 371 patients with a mean endocrine follow-up of 79 mo. IGF-1 lowering medications were held in 56% of patients who were on pre-SRS medical therapy. The mean SRS treatment volume and margin dose were 3.0 cm3 and 24.2 Gy, respectively. **The actuarial rates of initial and durable endocrine remission at 10 yr were 69% and 59%, respectively. The mean time to durable remission after SRS was 38 mo.** Biochemical relapse after initial remission occurred in 9%, with a mean time to recurrence of 17 mo."

**VERDICT on "mean or median": the draft is wrong if it says median — the source says MEAN.**
The sentence is "The **mean** time to durable remission after SRS was 38 mo." The word "median"
does not appear in the abstract. (Note the paper reports means throughout: mean follow-up 79 mo,
mean time to recurrence 17 mo.)

**VERDICT on the 10-year rates: the draft is right.** "The actuarial rates of initial and durable
endocrine remission at 10 yr were 69% and 59%, respectively" — 69% initial, 59% durable, both
actuarial, both at 10 years.

*Caveat:* verified at abstract level only. If the article body must be quoted, the full text
could not be obtained by any route tried here.

---

## Q4 — Three French national-database progestogen/meningioma studies

All three were read as author-written structured abstracts via Europe PMC
(`https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:"<doi>"&resultType=core&format=json`);
the BMJ paper was additionally read at `https://www.bmj.com/content/372/bmj.n37.full`.

### 4a — Weill et al., BMJ 2021;372:n37 — cyproterone acetate

**URL read:** `https://www.bmj.com/content/372/bmj.n37.full` (PMID 33536184)

Verbatim:

> "Overall, 69 meningiomas in the exposed group (during 289 544 person years of follow-up) and 20 meningiomas in the control group (during 439 949 person years of follow-up) were treated by surgery or radiotherapy. **The incidence of meningioma in the two groups was 23.8 and 4.5 per 100 000 person years, respectively (crude relative risk 5.2, 95% confidence interval 3.2 to 8.6; adjusted hazard ratio 6.6, 95% confidence interval 4.0 to 11.1). The adjusted hazard ratio for a cumulative dose of cyproterone acetate of more than 60 g was 21.7 (10.8 to 43.5). After discontinuation of cyproterone acetate for one year, the risk of meningioma in the exposed group was 1.8-fold higher (1.0 to 3.2) than in the control group.**"

Results-table column header, verbatim: **"Adjusted hazard ratio (95% CI)"**

- **Effect measure: ADJUSTED HAZARD RATIO** for 6.6 (4.0 to 11.1) and 21.7 (10.8 to 43.5).
  (A *crude relative risk* of 5.2 (3.2 to 8.6) is reported alongside — do not confuse the two.)
- Population, verbatim: "253 777 girls and women aged 7-70 years living in France who started
  cyproterone acetate between 2007 and 2014."
- Exposure definition, verbatim: "Participants were considered to be exposed when they had
  received a cumulative dose of at least 3 g during the first six months (139 222 participants)
  and very slightly exposed (control group) when they had received a cumulative dose of less
  than 3 g (114 555 participants)."
- Absolute incidences **23.8 (exposed) and 4.5 (control) per 100 000 person years** — confirmed.
- **1.8 (1.0 to 3.2)** one year after stopping — confirmed. Note the precise wording: the risk
  "was 1.8-fold higher … than in the control group", i.e. it is still a comparison against the
  control group, and the lower bound touches 1.0.

**VERDICT: the draft is right on the numbers, but wrong if it calls these "relative risk".**
6.6 and 21.7 are **adjusted hazard ratios**. 4.5 / 23.8 per 100 000 person-years and 1.8 (1.0–3.2)
are all confirmed exactly.

### 4b — Hoisnard/Roland et al., Lancet Reg Health Eur 2024;100928 — nomegestrol acetate

**URL read:** `https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:"10.1016/j.lanepe.2024.100928"&resultType=core&format=json`
(PMID 38800110, PMCID PMC11127190, open access). Title: "Prolonged use of nomegestrol acetate and
risk of intracranial meningioma: a population-based cohort study".

Verbatim:

> "Observational cohort study using SNDS data (France). … **Poisson models assessed the relative risk (RR) of meningioma.**"

> "In total, 1,060,779 women were included in the cohort (535,115 in the exposed group and 525,664 in the control group). **The incidence of meningioma in the two groups was 19.3 and 7.0 per 100,000 person-years, respectively (age-adjusted RRa = 2.9 [2.4–3.7]). The RRa for a cumulative dose of more than 6 g NOMAC was 12.0 [9.9–16.0]. In the event of treatment discontinuation for at least one year, the risk of meningioma was identical to that in the control group (RRa = 1.0 [0.8–1.3]).**"

- **Effect measure: age-adjusted RELATIVE RISK (RRa), from Poisson models.** Not a hazard ratio.
- Exposure definition, verbatim: "Exposure was defined as a cumulative dose >150 mg NOMAC within
  six months after first dispensing."
- Absolute incidences: **19.3 (exposed) vs 7.0 (control) per 100,000 person-years** — confirmed.
- **RRa = 1.0 [0.8–1.3]** one year after stopping — confirmed, and the authors' own gloss is
  "the risk of meningioma was **identical** to that in the control group".

**VERDICT: the draft is right on the numbers (2.9, 12.0, 7.0 vs 19.3, 1.0).** Measure is
age-adjusted **relative risk** (Poisson), not a hazard ratio. Note the high-dose threshold is
**">6 g"**, and the paper writes the incidences exposed-first (19.3 vs 7.0).

### 4c — Eur J Neurol 2024 — chlormadinone acetate

**URL read:** `https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:"10.1111/ene.16505"&resultType=core&format=json`
(PMID 39503288, PMCID PMC11622271, open access). Title: "Prolonged use of chlormadinone acetate
and risk of intracranial meningioma: A population-based cohort study".

Verbatim:

> "An observational cohort study was conducted based on the French national health data system. Women aged 10-70 years and who started CMA between 2007 and 2017 were included. Participants were considered to be exposed if they had received a cumulative dose >360 mg of CMA during the first 6 months and very slightly exposed (control group) when they had received a cumulative dose ≤360 mg. The outcome was surgery or radiotherapy for one or more intracranial meningioma(s). **Poisson models assessed the relative risk (RR) of meningioma.**"

> "In total, 828,499 women were included: 469,976 in the exposed group (mean age 39.1 years, SD 10.1) and 358,523 in the control group (38.3 years, SD 11.0). Surgery or radiotherapy for intracranial meningioma between 2007 and 2017 was recorded for 164 and 104 women in the exposed and control groups, respectively. **The incidence of meningioma was 18.5 and 6.8 per 100,000 person-years for the exposed and control groups respectively (crude RR = 2.7, 95% confidence interval [CI] 2.1-3.5; age-adjusted RR = 3.1, 95% CI 2.4-4.0). Meningioma incidence reached almost 47 cases/100,000 person-years in the most exposed group (>8.64 g), giving an age-adjusted RR of 6.9, 95% CI 5.1-9.2, relative to the control group.**"

- **Effect measure: age-adjusted RELATIVE RISK, from Poisson models.** (Crude RR 2.7 also given.)
- Absolute incidences **18.5 (exposed) vs 6.8 (control) per 100,000 person-years** — confirmed.
- The >8.64 g group: "almost 47 cases/100,000 person-years" — confirmed, and the paper attaches
  an **age-adjusted RR of 6.9 (5.1–9.2)** to it, which the draft appears not to carry.
- Cohort size: **828,499** (the draft's "~822,000" is slightly off; use ~828,000).

**VERDICT: the draft is right on 3.1, 6.8 vs 18.5 and ~47 per 100,000 person-years.**
Measure is age-adjusted **relative risk**, not a hazard ratio. Two corrections: the cohort is
**828,499**, not ~822,000; and the >8.64 g stratum carries a stated RR of 6.9 (5.1–9.2).

### Cross-cutting note for Q4
The three studies do **not** share one effect measure. Weill/BMJ reports **adjusted hazard
ratios** (Cox); the NOMAC and CMA studies report **age-adjusted relative risks** from **Poisson**
models. Any Chinese draft that renders all three as a single term (e.g. 「風險比」 or 「相對風險」
across the board) is wrong for at least one of them.

---

## Q5 — NICE NG99, meningioma follow-up table

**URL read:** `https://www.nice.org.uk/guidance/ng99/chapter/Recommendations`
(table transcribed from the page's own HTML markup, not from a rendered summary)

### The governing recommendation — verbatim

> "1.5.3 Consider the follow‑up schedule given in table 7 for people with meningioma."

### Table title — verbatim

> "Table 7 Possible regular clinical review schedule by years after end of treatment for people with meningioma depending on grade of tumour"

### IMPORTANT — the table does not use "completely excised (Simpson 1 to 3)"

The Simpson 1–3 wording the question asks about belongs to a **different table** in NG99 (the
*management* table, whose column headers are "Completely excised (Simpson 1 to 3)",
"Incompletely excised (Simpson 4 to 5)", "No excision (radiological only diagnosis)",
"Recurrent"). **Table 7, the follow-up table, is indexed by residual tumour instead**, with
columns: "Grade 1: no residual tumour", "Grade 1: residual tumour", "Grade 1: after
radiotherapy", "Grade 2", "Grade 3". The nearest equivalent to "grade 1, completely excised" is
therefore the **"Grade 1: no residual tumour"** column, and NG99 attaches this note:

> "Note: the presence of any residual tumour can only be established after the first scan at 3 months."

### The requested row — "Grade 1: no residual tumour", verbatim, every year band

| Year band | Grade 1: no residual tumour |
|---|---|
| 0 to 1 years | Scan at 3 months |
| 1 to 2 years | Annually |
| 2 to 3 years | Annually |
| 3 to 4 years | Once every 2 years |
| 4 to 5 years | Once every 2 years |
| 5 to 6 years | Once every 2 years |
| 6 to 7 years | Once every 2 years |
| 7 to 8 years | Once every 2 years |
| 8 to 9 years | Once every 2 years |
| >9 years (for the rest of life) | Consider discharge |

### Full Table 7 as it actually reads (for reference)

| | Grade 1: no residual tumour | Grade 1: residual tumour | Grade 1: after radiotherapy | Grade 2 | Grade 3 |
|---|---|---|---|---|---|
| 0 to 1 years | Scan at 3 months | Scan at 3 months | Scan 6 months after radiotherapy | Scan at 3 months, then 6 to 12 months later | Every 3 to 6 months |
| 1 to 2 years | Annually | Annually | Annually | Annually | Every 3 to 6 months |
| 2 to 3 years | Annually | Annually | Annually | Annually | Every 6 to 12 months |
| 3 to 4 years | Once every 2 years | Annually | Once every 2 years | Annually | Every 6 to 12 months |
| 4 to 5 years | Once every 2 years | Annually | Once every 2 years | Annually | Every 6 to 12 months |
| 5 to 6 years | Once every 2 years | Once every 2 years | Once every 2 years | Once every 2 years | Annually |
| 6 to 7 years | Once every 2 years | Once every 2 years | Once every 2 years | Once every 2 years | Annually |
| 7 to 8 years | Once every 2 years | Once every 2 years | Once every 2 years | Once every 2 years | Annually |
| 8 to 9 years | Once every 2 years | Once every 2 years | Once every 2 years | Once every 2 years | Annually |
| >9 years (for the rest of life) | Consider discharge | Consider discharge | Consider discharge | Consider discharge | Annually |

### Discharge language — verbatim

> ">9 years (for the rest of life) … **Consider discharge**"

(Note the column heading is ">9 years (for the rest of life)", not "after year 9". For Grade 3
this cell reads "Annually", i.e. **no discharge is offered for grade 3**.)

### Asymptomatic incidental finding — verbatim

> "For asymptomatic incidental meningioma: scan at 12 months and if no change, consider discharge or scan at 5 years."

This appears as a footnote under Table 7, not as a row of it. The related recommendation:

> "1.5.6 Arrange a clinical review, including appropriate imaging, for people with meningioma (including incidental meningioma) who develop new or changing neurological symptoms or signs at any time."

**VERDICT: the draft is substantively right about the every-two-years stretch, but wrong in
framing, and the "transcription artefact" the reviewer suspected is not an error.** In NG99 the
bands **3–4, 4–5, 5–6, 6–7, 7–8 and 8–9 years are all "Once every 2 years"** for grade 1 with no
residual tumour — so "years 3–5 every two years" and "years 5–9 every two years" are both true
and not a duplication; they are simply an awkward way of saying one continuous 3-to-9-year block.
Recommend rewriting as a single band. Three real corrections: (1) NG99 indexes this row by
**"no residual tumour"**, not by Simpson 1–3 — the Simpson wording comes from a different table,
so do not present "Simpson 1–3" as NG99's follow-up category; (2) **years 1–2 and 2–3 are
"Annually"**, which a draft jumping from "scan at 3 months" to "every two years" would drop;
(3) the discharge cell is ">9 years (for the rest of life)", and it is "**Consider** discharge",
not discharge.

---

## Q6 — CNS 2016 guideline, non-functioning pituitary adenoma surveillance

**URL read:** `https://www.cns.org/guidelines/management-nonfunctioning-pituitary-adenomas/8-post-treatment-follow-up-evaluation`
(chapter 8, "Post Treatment Follow-up Evaluation"; journal version: Congress of Neurological
Surgeons Systematic Review and Evidence-Based Guideline on Posttreatment Follow-up Evaluation of
Patients With Nonfunctioning Pituitary Adenomas, *Neurosurgery* 2016, DOI 10.1227/NEU.0000000000001392)

### The sentence asked for — verbatim

The guideline splits this across two recommendations. **Frequency** is the one graded
"Inconclusive":

> **Level Inconclusive:** "There is insufficient evidence to make a recommendation regarding the frequency of radiologic surveillance follow-up after surgical or radiation treatment of patients with NFPAs."

**Duration** ("length of time") is a trailing clause inside a Level III recommendation:

> **Level III:** "Long-term radiologic surveillance monitoring after surgical or radiation therapy treatment of NFPAs to evaluate for tumor recurrence or regrowth is recommended. **There is insufficient evidence to make a recommendation on the length of time of surveillance.**"

A third, parallel statement covers ophthalmologic follow-up and combines both in one sentence:

> **Level III:** "Postoperative ophthalmologic follow-up in patients undergoing surgical and/or radiation therapy treatment for NFPAs is recommended to evaluate the change in visual field and visual acuity postoperatively. **There is insufficient evidence to make a recommendation on the length of time for this surveillance and the frequency.**"

### Other directly relevant recommendations — verbatim

> **Level III:** "It is recommended that the first radiologic study to evaluate the extent of resection of the NFPA be performed 3-4 months after surgical intervention."

> **Level III:** "It is recommended that patients who undergo radiologically proven gross total resection of the NFPA be followed less frequently than those undergoing subtotal resection."

> **Level Inconclusive:** "There is insufficient evidence to make a recommendation regarding the timing of initial radiologic follow-up after radiation therapy."

**VERDICT: the draft is right, but only if it reports the two halves separately.** There is no
single sentence covering both duration and frequency for *radiologic* surveillance. **Frequency**
is graded **Level Inconclusive**; **duration ("length of time")** is stated inside a **Level III**
recommendation that *does* positively recommend long-term surveillance. A draft that compresses
this into "CNS says there is insufficient evidence for the duration and frequency of imaging
surveillance" overstates the nihilism — CNS affirmatively recommends long-term surveillance, a
first scan at 3–4 months, and less frequent follow-up after gross total resection. (The one
sentence that does join duration and frequency is the *ophthalmologic* one, which is Level III.)
