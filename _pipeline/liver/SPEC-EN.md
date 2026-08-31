# 肝癌專題 — English edition spec

Supplementary. **Read `/home/claude/colon/SPEC-EN.md` first** (no-drift rules, British
spelling, structure, report-don't-fix). Then `/home/claude/liver/SPEC.md` §一/§三 and
§八/§九 修正 — all bind the English equally.

## 1. Fixed disclosure — one rendering, byte-identical across 20

> <p>My position first: stereotactic body radiotherapy and proton therapy for liver
> cancer are treatments I deliver myself — and much of it is self-paid. The other side
> of every comparison in this topic is my colleagues' surgery and ablation. That is why
> every comparison comes with its primary source, so you can take it to the surgical
> and hepatology clinics for a second opinion; hearing them out before you decide is
> the process I recommend, not a concession.</p>

## 2. The passages English will break

- **紅線 1 (lv-three-roads)**: resection stays the default for the resectable,
  well-compensated patient — at full strength, both anchors; nothing readable as
  "not operating is just as good for operable patients", and nothing that demotes
  SBRT back to "a last resort". The bidirectional failure condition binds English too.
- **OS discipline**: 「看不出差別」= "no difference could be seen", never "equally
  good" / "just as good".
- **Xi 2025**: the population label (recurrent, ≤5 cm, single, single-centre) travels
  with EVERY appearance — B1, C1, D2. "Superior local control in that trial" never
  becomes "SBRT is superior to RFA".
- **紅線 2/修正 6 (lv-proton)**: the Korean RCT proved **non-inferiority** — "writing
  superiority would be overreach, so I will not" stays a full sentence; PP/ITT numbers
  and 90% CI lower bounds identical; "photon SBRT is already very good" remains a
  complete section; the price keeps its label ("that hospital's published bundle,
  not liver-specific"); never "worth it".
- **修正 5 (lv-sbrt)**: RTOG 1112 keeps BOTH p values (one-sided 0.06, adjusted 0.04)
  and the arm labels on every number.
- **紅線 3 (lv-sbrt)**: "when SBRT is the wrong answer" section at full strength,
  AASLD CTP≥8 included.
- **修正 16 (lv-liver-care)**: the NHI clause quoted faithfully, the list's missing
  SBRT stated as absence-plus-vintage, NEVER as "NHI refuses antivirals to SBRT
  patients"; "confirm case by case with your case manager" preserved.
- **Reimbursement register**: 「查無給付」= "I could find no listed item" (and the
  self-limiting parenthesis in B5 survives); never "not covered" as a flat claim.
  Zero-hit searches stay zero hits; gaps stay gaps ("ask the medical affairs office").
- **修正 13 (C group)**: the five number-shaped holes STAY holes in English — no
  interval days, session minutes, admission days, syndrome duration, fever cutoff.
- **Word-proportion rule**: 「約六成」= "about 60%" — every number identical including
  those written as Chinese proportions; hedges at equal strength.

## 3. Canonical English titles

- lv-no-biopsy → "Why liver cancer is often diagnosed without a biopsy"
- lv-two-diseases → "You have two diseases: the cancer and the cirrhosis"
- lv-staging-bclc → "Where the staging chart puts you"
- lv-hepatitis → "Hepatitis B and C: the antivirals matter more now"
- lv-first-month → "How the first month after diagnosis unfolds"
- lv-three-roads → "Three roads for a small liver cancer"
- lv-sbrt → "Why SBRT works in the liver, and when it is the wrong answer"
- lv-proton → "Protons for liver cancer: the upgrade and the trials"
- lv-transplant → "Transplant: the one option that treats both diseases"
- lv-tace-y90 → "TACE and Y-90: the intermediate-stage workhorses"
- lv-sbrt-weeks → "What the two weeks of SBRT actually look like"
- lv-warning-signs → "When to come back to hospital the same day"
- lv-systemic-days → "Life on targeted therapy and immunotherapy"
- lv-nutrition → "Albumin, muscle and what to eat"
- lv-tace-days → "The days before and after TACE"
- lv-followup → "Follow-up and AFP: how often to scan"
- lv-recurrence → "Recurrence is not failure — it is how this disease behaves"
- lv-liver-care → "The liver needs care for life after treatment ends"
- lv-post-transplant → "Life after a liver transplant"
- lv-bridging → "The days on the waiting list"

Cross-references inside the topic use these titles verbatim, unlinked 〈…〉 style
converted to English quotation convention used on the live -en pages. B3's pointers
to existing site pages keep their live English titles — READ the live `-en` page to
copy the exact title (nt-proton-en, insight-proton-en).

## 4. Structure & metadata

Same `<h4>` count/order; headings rewritten with tension; 1,100–2,100 words
(faithfulness wins); `<h3>References</h3>`; ends `<p></p>`; every statistical term
glossed on first use per article, glosses not converged. Terminology:
立體定位放射治療 → stereotactic body radiotherapy (SBRT); 射頻燒灼 → radiofrequency
ablation (RFA); 肝動脈化學栓塞 → transarterial chemoembolisation (TACE); 釔九十 →
Y-90 (selective internal radiotherapy); 肝硬化 → cirrhosis; 失代償 → decompensation;
肝性腦病變 → hepatic encephalopathy; 食道靜脈瘤 → oesophageal varices; 腹水 →
ascites; 換肝／肝臟移植 → liver transplant; 米蘭準則 → Milan criteria; 橋接治療 →
bridging therapy; 降期 → downstaging; 放射性肝損傷 → radiation-induced liver disease
(RILD); 栓塞後症候群 → post-embolisation syndrome; 個管師 → case manager; 重大傷病
證明 → catastrophic illness certificate; 醫務課 → medical affairs office; 健保 →
National Health Insurance (NHI). Child-Pugh / ALBI / BCLC stay as-is. British
spelling throughout (tumour, oesophageal, litre, -ise). Metadata per group
`meta/<X>-en.json`, titles verbatim from §3.
