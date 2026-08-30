# 乳癌專題 — English edition spec

Supplementary. **Read `/home/claude/colon/SPEC-EN.md` first — sections 1 (no drift),
2 (if you think the Chinese is wrong), 3 (British spelling and the shared term table),
4 (structure), 6 (deliberately-set register) and 9 (checks) apply unchanged.**
This file adds only what is specific to breast cancer.

Also read `/home/claude/breast/SPEC.md` §四（紅線）and §七（修正）— every red line and
every correction applies to the English text with equal force.

Chinese sources: `breast/body/<slug>.html`. English output: `breast/en/<slug>.html`.

---

## 1. The three hard rules, restated because this topic breaks them differently

1. **`[n]` points to the same URL as the Chinese `[n]`** — same count, same order,
   character for character.
2. **Every number identical**, including proportions written as words, and including
   **percentage points**, which stay "percentage points" and never become "percent".
3. **Every hedge survives at the same strength.** Softening is drift; so is sharpening.

**A fourth rule exists only in this topic**: **every number keeps its subtype and
population label.** 「HR 陽性／HER2 陰性、停經後、淋巴結 1–3 顆」 must survive as
"hormone-receptor-positive, HER2-negative, postmenopausal, with one to three positive
nodes" — not compressed to "in this group". An unlabelled figure is a factual error
in breast cancer, and English's appetite for brevity is exactly what strips the label.

## 2. Terminology — breast-specific additions to colon/SPEC-EN.md §3

- 荷爾蒙受體陽性 → hormone-receptor-positive (HR-positive)
- 三陰性 → triple-negative
- 停經前／停經後 → premenopausal / postmenopausal
- 卵巢功能抑制 → ovarian function suppression
- 芳香環轉化酶抑制劑 → aromatase inhibitor
- 內分泌治療 → endocrine therapy (never "hormone therapy")
- 多基因表現分析 → multigene expression assay
- 生殖系（檢測） → germline (testing); 腫瘤（體細胞）變異 → somatic/tumour alteration
- 前哨淋巴結切片 → sentinel lymph node biopsy; 腋下廓清 → axillary dissection
- 保留乳房手術 → breast-conserving surgery
- 乳房切除後放療 → post-mastectomy radiotherapy
- 區域淋巴照射 → regional nodal irradiation
- 大分割 → hypofractionation; 部分乳房照射 → partial breast irradiation
- 病理完全緩解 → pathological complete response (pCR)
- 間質性肺病 → interstitial lung disease
- 淋巴水腫 → lymphoedema
- 重大傷病證明 → catastrophic illness certificate
- 個管師 → case manager；醫務課 → the hospital's medical affairs office
- 健保 → Taiwan's National Health Insurance (NHI)

## 3. Red lines — where English breaks them

**紅線 1 (`genomic-chemo`)** — no general recommendation in either direction. English
resolves balanced passages by reflex: delete anything of the shape "ultimately, most
patients…" or "on balance…". The eligibility sentence — **hormone-receptor-positive,
HER2-negative only** — stays early and plain, so a triple-negative or HER2-positive
reader cannot mistake it for hers. A low score is never "no risk". Non-inferiority is
explained on first use **in this article**.

**紅線 2 (`metastatic-genomics`)** — the sentence saying the whole article is about
**metastatic** disease stays near the top and stays blunt. Never let "no actionable
target" become "the test failed" or "bad news". Benefit and cost stay in the same
paragraph for every drug. Do not write that capivasertib prolongs survival.

**紅線 3 (`rt-omission`)** — nothing readable as "radiotherapy can be skipped", and
nothing readable as "everyone must have it". The EUROPA finding (endocrine therapy
alone had **worse** 24-month global health status; the recurrence endpoint is **not yet
reported**) keeps its full force. Every omission trial assumes continued endocrine
therapy — that assumption stays visible.

**紅線 4 (`breast-conserving`)** — breast conservation is conserving surgery **plus
radiotherapy**; it is never the option that avoids radiotherapy. Per 修正 6, write
"not worse, and possibly better in observational data", not "the same". The
contralateral-mastectomy passage keeps its mechanism (contralateral cancer is a
**marker** of high-risk biology, not the cause of death) — that mechanism is what keeps
a frightened reader reading, and English politeness tends to cut it.

**紅線 5 (`endocrine-years`, `endocrine-side-effects`)** — report symptoms, yes; stop on
your own, no; and the reason (the duration is part of the effect) stays. Nothing
readable as "if it's unbearable, take a break".

**紅線 6 (`metastatic-outlook`)** — survival figures keep their subtype. Oligometastatic
disease says no more than "the randomised breast-specific data do not yet support it".
No NRG-BR002 figure. No miracle narrative, and no "metastatic means terminal".

**修正 8 (`sentinel-node`)** — nothing readable as "the axilla can be left alone".

**修正 14 (`rt-regional`)** — nothing readable as "proton is better or safer for breast
cancer". This is the author's own modality; the line is tighter in English, not looser.

**固定紅線 A (`chemo-side-effects`)** — the complete same-day-contact list, drug by drug,
including **abemaciclib venous thromboembolism** and **T-DM1 and T-DXd interstitial lung
disease** with their unremarkable early symptoms. Never "contact your doctor if you feel
unwell".

**固定紅線 C** — every Taiwan reimbursement gap stays a gap: "confirm with your case
manager or the hospital's medical affairs office". Never "coverage may vary" — that reads
as though the answer is known and merely variable. Never say a cost is manageable.

## 4. Structure

Same `<h4>` count and order as the Chinese; headings rewritten, not translated literally.
**1,100–2,100 English words** of body — and where faithfulness and the ceiling conflict,
**faithfulness wins**. `<h3>References</h3>`. Ends `<p></p>`. Every statistical term gets
a plain-language rendering on first appearance **in that article**; the Chinese
deliberately gives different articles different glosses, so do not converge them.

## 5. Cross-reference titles — use these exact English titles

Chinese uses 〈…〉; English uses the English title in double quotes. Canonical:

- `first-month` → "What the first month after diagnosis looks like"
- `receptor-report` → "What ER, PR and HER2 are telling you"
- `three-subtypes` → "Three breast cancers, three different roads"
- `which-lines-matter` → "Which lines of the report actually change treatment"
- `imaging-extent` → "The size on the scan isn't the real size"
- `germline-brca` → "Family history: should you test for BRCA now?"
- `breast-conserving` → "Conservation or mastectomy: is survival the same?"
- `sentinel-node` → "How much of the axilla has to go?"
- `neoadjuvant` → "Surgery first, or chemotherapy first?"
- `genomic-chemo` → "What this test is actually trying to prove"
- `her2-therapy` → "HER2-positive: how the drugs are ordered"
- `endocrine-years` → "Five years of endocrine therapy, or ten?"
- `rt-hypofx` → "Five treatments, fifteen, or twenty-five"
- `rt-omission` → "Omitting radiotherapy: every condition has to hold"
- `rt-regional` → "Should the axilla and supraclavicular area be treated too?"
- `chemo-side-effects` → "Which side effects mean phoning the same day"
- `endocrine-side-effects` → "The side effects that actually make people stop"
- `fertility-young` → "Young patients: fertility preservation and ovarian function"
- `followup-schedule` → "Does follow-up need a yearly whole-body scan?"
- `lymphoedema` → "A swollen arm: the real odds of lymphoedema"
- `bone-health` → "Bone density, bone-targeted drugs and exercise"
- `self-pay-and-trials` → "This test is self-pay. Is it worth it?"
- `metastatic-genomics` → "After metastasis, genomic testing is about finding a drug"
- `metastatic-outlook` → "Metastatic disease: what happens next"

**List every cross-reference sentence you write in your report**, so title drift can be
checked.

## 6. Metadata

`breast/meta/<group>-en.json`, keyed by slug, `{"title", "dek", "lead", "note"}`.
Titles from §5 verbatim. The `lead` must not paraphrase the English first paragraph,
and must keep any denominator or subtype label its number needs.
`genomic-chemo`'s dek must state the hormone-receptor-positive, HER2-negative
restriction — the Chinese title was changed for exactly this reason.

## 7. Checks

```
python3 <scripts>/check_article_html.py <your en files> --lang en --min 1100 --max 2100
python3 <scripts>/check_bilingual.py /home/claude/breast/body /home/claude/breast/en
```
