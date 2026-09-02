# 食道癌專題 — English edition spec

Supplementary. **Read `/home/claude/repo/_pipeline/colon/SPEC-EN.md` first** (no-drift rules,
British spelling, register, report-don't-fix). Then `/home/claude/esoph/SPEC.md` §一/§二/§四/§九 —
all bind the English equally. The Chinese fragment is the master; the English says the same
things, with the same numbers, the same hedges, the same citation numbers pointing at the same URLs.

Live English exemplars (same author's voice): `/home/claude/repo/lv-three-roads-en.html`,
`/home/claude/repo/cx-surgery-or-rt-en.html`, `/home/claude/repo/hn-first-week-en.html`.

## 1. Fixed disclosure — one rendering, byte-identical in A4, B1, B2, B5 (and nowhere else)

> <p>My position first: concurrent chemoradiotherapy and proton therapy for oesophageal cancer are treatments I deliver myself, every week; the other side of every comparison in this topic is my thoracic-surgery colleagues' operation and my gastroenterology colleagues' endoscopy. That is why every comparison comes with its primary source, so you can take it to the surgical and gastroenterology clinics for a second opinion; hearing them out before you decide is the process I recommend, not a concession.</p>

## 2. The passages English will break

- **紅線 1 (ec-surgery-or-watch)**, bidirectional. "The clinic still recommends surgery" stays at
  full strength with its numbers (pT0 35.6%, preSANO 31%→10%, preSINO NPV 68.7%, SANO 2-year
  non-inferiority with its four labels). Nothing readable as "if you respond well you can skip
  surgery"; nothing readable as "definitive chemoradiotherapy is the inferior option for those
  who cannot have surgery". 「非劣性…證明的是『沒差太多』，不是『一樣好』」 → "non-inferiority
  … proves 'not much worse', not 'as good'". 「方向偏向手術」 → "the direction favoured surgery".
  「正在被驗證」 → "is being tested", never "is emerging as an option".
- **紅線 2 (ec-immunotherapy)**: "the three phase III trials … none met its primary endpoint";
  SKYSCRAPER-07 keeps both halves (primary endpoint not met; atezolizumab-alone arm OS HR 0.69,
  descriptive). CheckMate 577 OS: "did not reach statistical significance" — no HR. NHI clauses:
  second line 113/4/1, first line with chemotherapy 115/2/1, TC≧1%, two years, prior approval;
  "no clause for adjuvant nivolumab"; pembrolizumab "not yet reimbursed for this indication".
- **紅線 3 (ec-feeding-tube)**: 「掉一成是啟動評估的門檻，不是放管指令」 → "a 10% loss is the
  threshold that starts the assessment, not an order to place a tube". The three routes each keep
  their guideline slot (ESGE <4 weeks nasal, >4 weeks percutaneous, gastric first; ESPEN surgical
  guideline for intra-operative jejunostomy). Jejunostomy keeps its bowel-obstruction figure.
  Stent: ESGE quoted verbatim in English (it already is English) — "does not recommend SEMS as a
  bridge to surgery or before preoperative chemoradiotherapy". "Reimbursed ≠ recommended" stays.
- **紅線 4 (ec-warning-signs)**: fever rule = "a single reading of 38.0°C — go" (aligned with the
  live care-fever-en page; READ it and copy its exact phrasing of the rule). Drug names and
  symptoms stay specific. Fistula: 22–24%, median 100 days after CRT start, "during and for
  months after treatment".
- **紅線 5 (ec-esophagitis, ec-crt-dose)**: 「不能拿現代回溯當『可以隨便停』的證據」 → "the
  modern retrospective data cannot be used as evidence that 'stopping for a few days is fine'";
  "arranged by the doctor, sessions made up afterwards" survives verbatim in sense. The
  "when I will stop it, and when you must not stop it yourself" section stays a section.
- **紅線 6 (ec-proton)**: Lin 2020 = randomised phase IIB, primary endpoint total toxicity burden,
  PFS/OS the same — never "protons improved outcomes"; "photon IMRT is already very good" remains
  a complete section; price keeps its label (that centre's published fee page, dated, not an
  oesophagus-specific bundle); never "worth it"; NRG-GI006 completion 2031.
- **紅線 7 (ec-esd)**: depth ladder with cohort label; JCOG0508 = single-arm; "removed does not
  mean done" at full strength.
- **Reimbursement register**: 「查不到…問醫務課／個管師」 → "I could not find a listed item —
  ask the medical affairs office / your case manager"; never "not covered" as a flat claim.
  NHI clause quotes: translate faithfully and mark them as translations of the clause.
- **Institution names**: keep them exactly where the Chinese has them (study source / official
  price page); add none.
- **Word-proportion rule**: 「約三分之二」= "about two-thirds", 「一成」= "10%", 「近三成」=
  "nearly 30%" — every number identical; hedges at equal strength.
- **Alcohol/betel/tobacco**: no blame in either language; 「戒斷是治療的一部分」 → "quitting is
  part of the treatment".

## 3. Canonical English titles (use verbatim for cross-references)

- ec-two-diseases → "Squamous and adenocarcinoma are two different diseases"
- ec-workup → "The tests that decide whether surgery is possible"
- ec-treatment-map → "The oesophageal cancer treatment map: which box are you in"
- ec-surgery-or-watch → "After chemoradiotherapy, do you still need surgery"
- ec-crt-dose → "Radiation dose: why higher is not better"
- ec-immunotherapy → "Who does immunotherapy actually help"
- ec-surgery → "What surgery removes, and where the stomach goes"
- ec-esd → "Can endoscopy alone deal with an early lesion"
- ec-proton → "Protons for oesophageal cancer: the case and where the trials stand"
- ec-feeding-tube → "Can't swallow, weight falling: a feeding tube first?"
- ec-esophagitis → "Getting through radiation oesophagitis"
- ec-warning-signs → "When to come back the same day"
- ec-before-start → "Things to settle before treatment starts"
- ec-eating-after → "Eating after an oesophagectomy"
- ec-stricture-or-recurrence → "Swallowing worse again: stricture or recurrence"
- ec-followup → "How follow-up is scheduled, and the second cancer people forget"
- ec-recurrence → "After recurrence or spread, what roads remain"

Cross-references inside the topic: the English title in double quotes, unlinked (as the live
-en pages do). Pointers to existing site pages keep the live English title and the `-en.html`
href: read `care-fever-en.html`, `nt-proton-en.html`, `insight-proton-en.html` and copy the exact
`<title>` head text (the part before ｜).

## 4. Structure, terminology, metadata

Same `<h4>` count and order as the Chinese (headings rewritten with tension, not word-for-word);
900–1,500 words, faithfulness wins over the cap; same reference list (same count, same order, same
hrefs) rendered as `<hr><h3>References</h3><ol>…</ol><p></p>`; every statistical term glossed on
first use in each article. Allowed tags identical to the Chinese spec.

Terminology (fixed): 鱗癌 → squamous cell carcinoma (SCC after first use); 腺癌 → adenocarcinoma;
胃食道接合部 → gastro-oesophageal junction; 同步化放療 → concurrent chemoradiotherapy (CRT);
根治性化放療 → definitive chemoradiotherapy; 術前化放療 → preoperative chemoradiotherapy (say
"neoadjuvant" only when quoting a trial name); 三合一（化放療加手術）→ trimodality treatment
(chemoradiotherapy followed by surgery); 主動監測 → active surveillance; 臨床完全反應 → clinical
complete response (cCR); 病理完全反應 → pathological complete response (pCR); 救援手術／救援食道切除
→ salvage oesophagectomy; 食道切除 → oesophagectomy; 胃管／胃管食道 → gastric conduit; 吻合口 →
anastomosis; 滲漏 → anastomotic leak; 狹窄 → stricture; 擴張 → dilatation; 氣管食道廔管 →
tracheo-oesophageal fistula; 穿孔 → perforation; 食道炎 → oesophagitis; 傾倒症候群 → dumping
syndrome; 逆流 → reflux; 鼻胃管 → nasogastric tube; 胃造廔 → gastrostomy (PEG); 空腸造廔 → feeding
jejunostomy; 金屬支架 → self-expanding metal stent (SEMS); 近接治療 → brachytherapy; 內視鏡黏膜下剝離
→ endoscopic submucosal dissection (ESD); 內視鏡超音波 → endoscopic ultrasound (EUS); 正子 → PET-CT;
支氣管鏡 → bronchoscopy; 頸段 → cervical oesophagus; 質子 → proton therapy; 強度調控放射治療 → IMRT;
總毒性負擔 → total toxicity burden; 淋巴球低下 → lymphopenia; 免疫檢查點抑制劑 → immune checkpoint
inhibitor; 整體存活 → overall survival (OS); 無病存活 → disease-free survival; 風險比 → hazard ratio
(HR); 勝算比 → odds ratio (OR); 95% 信賴區間 → 95% confidence interval (CI); 非劣性 → non-inferiority;
第 3 級 → grade 3; 檳榔 → betel quid; 重大傷病證明 → catastrophic illness certificate; 個管師 → case
manager; 醫務課 → medical affairs office; 健保 → National Health Insurance (NHI); 癌症登記 → Taiwan
Cancer Registry; 衛福部 → Ministry of Health and Welfare; 國健署 → Health Promotion Administration.
Trial names, drug names (lower-case generics), Gy, CPS/TPS/TC stay as-is. British spelling
(oesophagus, tumour, centre, randomised, litre).

Metadata per group → `/home/claude/esoph/meta/<X>-en.json`, keys `ec-<slug>` → {title (verbatim from
§3), dek, lead, note}; lead must not paraphrase the English first paragraph.
