# Colon cancer series — English edition spec

Supplementary to `SPEC.md`. **Read `SPEC.md` first, including 第十一節 (the
research-driven corrections), then this file.** Everything in `SPEC.md` about
allowed tags, citation mechanics, file-ending shape, 醫療法 §84/§86 restrictions,
and the cross-reference ownership table applies unchanged.

The English edition is **not a rewrite**. It is the same set of facts in another
language.

---

## 1. The rule that matters most: no drift

Three hard rules. A violation of any one is a factual error, not a style problem.

**1.1 — Citation `[n]` in the English article must point to exactly the same URL
as `[n]` in the Chinese article.** Same number of entries, same order, same hrefs,
character for character. Do not renumber, do not reorder, do not add, do not drop.

**1.2 — Every number is identical.** Percentages, hazard ratios, confidence
intervals, denominators, doses, cycle counts, years. Including numbers written as
words: 「四分之一」 is *one in four*, not *one in five*, and 「兩成」 is *20%*, not
*a fifth of a percentage point*. A proportion rendered in words is where drift
hides, because a pure numeric diff cannot see it.

**1.3 — Every hedge survives at the same strength.** This is the one translators
break, because English academic register pulls hard toward smoothing a blunt
negative into something publishable.

- 「這件事目前沒有定論」 → "this is not settled", NOT "evidence suggests"
- 「這個試驗的品質其實不算好」 → "the trial quality is honestly not good", NOT
  "the evidence base is limited"
- 「我查不到可以引用的正式條文」 → "I could not find a formal provision I could
  cite", NOT "reimbursement details vary"
- 「主要終點未達標」 → "the primary endpoint was not met", NOT "the trial did not
  reach statistical significance for its primary endpoint" softened into a trend
- 「我不會替它說有或沒有」 → "I am not going to tell you it is covered or that it
  isn't"

**Softening a hedge is factual drift.** The uncertainty is the content.

The same applies in reverse: do not sharpen. If the Chinese says 「可能更差」 about
an imprecise pooled estimate (修正 1), the English says "may be worse", not "is
worse".

## 2. If you think the Chinese is wrong

**Stop and report it. Do not fix one language.** A one-sided correction produces
two published versions that say different things, and nobody finds it afterwards.
List it in your report; both versions get fixed together.

## 3. Spelling, register, terminology

British spelling throughout: tumour, randomised, oesophagus, programme, anaemia,
haematological, oedema, paediatric. Keep it consistent across all sixteen.

Register: the same first-person clinic voice. A practising oncologist talking, not
a patient leaflet and not a review article. Contractions are fine. Do not restore
the throat-clearing that the Chinese deliberately avoids ("With advances in modern
medicine…").

Fixed term mappings — use these, and only these, across all sixteen articles:

- 輔助化療 → adjuvant chemotherapy
- 無病存活 → disease-free survival (DFS)
- 無復發存活 → recurrence-free survival (RFS)
- 風險比 → hazard ratio (HR)
- 勝算比 → odds ratio (OR)
- 信賴區間 → confidence interval (CI)
- 非劣性 → non-inferiority
- 絕對風險差／百分點 → absolute difference / percentage points (never "percent")
- 錯配修復功能缺失 → mismatch repair deficient (dMMR)
- 微衛星不穩定性高 → microsatellite instability-high (MSI-H)
- 微量殘存疾病 → molecular residual disease (MRD)
- 循環腫瘤 DNA → circulating tumour DNA (ctDNA)
- 周邊神經病變 → peripheral neuropathy
- 手足症候群 → hand-foot syndrome
- 暫時性造口 → temporary stoma
- 個管師 → case manager
- 醫務課 → the hospital's medical affairs office
- 健保 → Taiwan's National Health Insurance (NHI)
- 藥品給付規定 → the NHI drug reimbursement regulations
- 醫療服務給付項目及支付標準 → the NHI fee schedule
- 重大傷病證明 → catastrophic illness certificate
- 糞便潛血檢查 → faecal immunochemical test (FIT)
- 癌症資源中心 → hospital cancer resource centre

Every statistical term still needs a plain-language rendering **on its first
appearance in that article**, exactly as in Chinese — a reader landing on article
11 from a search engine has not read article 2.

## 4. Structure

- Same number of `<h4>` sections, in the same order, carrying the same content.
- Headings are **rewritten, not translated literally**. They must still be
  questions or statements with tension, never noun labels. "Side effects" is a
  failed heading in either language.
- **1,100–2,100 English words** of body text. (Revised: the original 900–1,500
  ceiling was set before the Chinese articles were finalised at 1,840–2,400
  characters. Faithful rendering of that density lands at 1,600–2,000 words.
  **Cutting to hit a word count is how hedges and denominators get lost — the
  no-drift rule outranks the length target.**) Do not pad to hit a number either.
- Same `<hr>`, same `<h3>` — but the heading text is `<h3>References</h3>`.
- File ends with `<p></p>`.
- Write to `colon/en/<slug>.html`, same slug as the Chinese file.

## 5. Red lines — how each one continues in English

Every red line in `SPEC.md` 第八節 and every correction in 第十一節 applies to the
English text with equal force. The ones that break under translation:

**Red line 1 (`stage-ii-chemo`)** — the English must contain no general
recommendation in either direction. Watch for English's habit of resolving a
balanced passage with "ultimately, most patients…". Delete any such sentence.
The dMMR harm signal keeps its interval (OS HR 2.95, 95% CI 1.02–8.54) and keeps
being described as very imprecise.

**Red line 2 (`immunotherapy-dmmr`)** — every statement that checkpoint inhibitors
do not work in MSS disease carries the full qualifier **metastatic** and
**single-agent**, every single time, with no "as noted above" elision. ATOMIC's
benefit and its 84.1% grade 3–4 adverse-event rate stay in the same paragraph.
NICHE-2 stays labelled single-arm, n=115, 26-month median follow-up, three-year
DFS unpublished — in the same sentence as the no-recurrence observation, not after
it.

**Red line 3 (`ctdna-mrd`)** — both directions stay blocked. "Undetectable" must
never become "clear", "negative", or "no residual disease" in English; those words
carry more finality than the Chinese does. Escalation was **tested and failed**,
not "not yet established". Non-inferiority is explained before the first
non-inferiority result appears.

**Red line 4 (`metastatic-cure`)** — the preconditions stay attached to every
statement about cure. English's "can be cured" reads as a general claim in a way
the Chinese does not; keep the conditions in the same sentence. No "miracle",
no "second chance", no individual stories.

**Red line 5 (`oxaliplatin-neuropathy`) and 修正 10** — the three-clause split
between holding an oral tablet and stopping an infusion is worded **identically in
both `oxaliplatin-neuropathy` and `capecitabine-at-home`**, in English as in
Chinese. Agree the English wording between those two files and use it byte for
byte. The two fever thresholds (38.1 °C from the Xeloda label, 38.3 °C from IDSA)
stay separately attributed and are never merged.

**Fixed red line A** — `capecitabine-at-home` carries the complete same-day-contact
list for the whole series, all seven items including mouth ulceration severe enough
to prevent swallowing. Never "contact your doctor if you feel unwell".

**Fixed red line C** — every Taiwan reimbursement gap stays a gap. "Confirm with
your case manager or the hospital's medical affairs office." Never soften this into
"coverage may vary" — that reads as though the answer is known and merely variable.
Never write that a cost is manageable.

**Fixed red line D** — `surveillance-intensity`'s uncomfortable conclusion stays in
the opening movement, not in a closing caveat.

## 6. Register that was deliberately set

Where the Chinese chose a flatter, less alarming register (for instance the way
`bowel-recovery` states unknowns rather than reassuring, or the way
`supplements` declines to name products), the English holds the same register.
Do not "restore" a cautionary tone the Chinese deliberately dialled down, and do
not warm up a passage the Chinese deliberately left cool.

## 7. Cross-reference titles — use these exact English titles

Chinese uses 〈…〉; English uses the article's English title in double quotes.
These are canonical. Do not invent variants.

- `malignant-polyp` → "The polyp is out. Why operate again?"
- `reading-stage-report` → "Where T3N1 actually comes from"
- `first-month` → "What the first month after diagnosis looks like"
- `biomarkers-and-family` → "Your gene report decides more than your treatment"
- `lymph-node-yield` → "What the node count really decides"
- `stage-ii-chemo` → "Stage II: chemotherapy or not?"
- `three-or-six-months` → "Three months or six"
- `immunotherapy-dmmr` → "Immunotherapy is not an option for everyone"
- `oxaliplatin-neuropathy` → "Numb hands and feet: when to speak up"
- `capecitabine-at-home` → "The chemotherapy you take at home"
- `bowel-recovery` → "How long until your bowel settles down"
- `supplements` → "Supplements during treatment: worth it?"
- `surveillance-intensity` → "Is closer follow-up worth it?"
- `ctdna-mrd` → "What an undetectable ctDNA actually means"
- `metastatic-cure` → "Metastatic disease: is cure still possible?"
- `exercise-recurrence` → "Exercise lowers recurrence. How much do you need?"

In your report, **list every cross-reference sentence you wrote**, so the series
can be checked for title drift.

## 8. Metadata

Produce `colon/meta/<group>-en.json`, keyed by slug, each value
`{"title", "dek", "lead", "note"}` — the English titles above, plus English `dek`
(one sentence, what the article solves), `lead` (which must not paraphrase the
English first paragraph) and `note`. Same content as the Chinese metadata, same
hedges, same numbers.

## 9. Before finishing

```
python3 /root/.claude/skills/synced/cancer-topic-series/scripts/check_article_html.py <your en files> --lang en
python3 /root/.claude/skills/synced/cancer-topic-series/scripts/check_bilingual.py /home/claude/colon/body /home/claude/colon/en
```

The bilingual checker compares citation counts, URL by position, `<h3>`/`<h4>`
counts and proportions expressed in words. Its word-proportion output is
"needs a human look", not a hard fail — but read every line of it.
