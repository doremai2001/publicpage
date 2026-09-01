# 骨盆腔放射治療專題 — English edition spec

Supplementary. **Read `/home/claude/colon/SPEC-EN.md` first** (no-drift rules, British
spelling, structure, report-don't-fix). Then `/home/claude/pel/SPEC.md` §一/§三 and §八
修正 1–17, plus `/home/claude/pel/FIXES.md` (the invariants section) — all bind the
English equally.

## 1. Fixed disclosure — one rendering, byte-identical across 13

> <p>My position first: pelvic radiotherapy is what I do every day, so every good word
> about radiotherapy in this topic is written more conservatively than anyone else would
> write it. Implants such as the rectal spacer are not something my department provides;
> I write about them as an option you can go and ask about, and for cost and for who
> performs them, please ask that department and the medical affairs office.</p>

## 2. The passages English will break

- **紅線 1 (B group, bidirectional)**: nothing readable as "you cannot be looked after
  properly without paying". The paragraph on what **ordinary intensity-modulated
  radiotherapy already does** stays at full weight in B1, B3 and B4, with its real
  numbers, never adjectives. Reverse direction equally: differences are never shrunk to
  "they are all the same". Technique is decided by indication, never by budget.
- **紅線 2 (A3), the topic's most important frame**: bladder preparation is **not
  "hold as much as you can"**. Full or empty is decided by the plan; the job is to
  reproduce the state the plan was built on. The three safety valves survive at full
  strength: say it rather than push through if you cannot hold it or cannot empty
  properly; **holding too much has its own cost** (the 300–500 mL structure, both
  directions, with its cervical/single-centre/retrospective labels); and **being
  adjusted mid-course is not the patient getting it wrong**. The loosening of rectal
  emptying is never over-extended into "you need not prepare at all".
- **紅線 3 (A4)**: "not something my department provides" stays; the "who does not need
  it" section stays a section; and **"in the severe-toxicity cell, the meta-analyses
  found no difference"** stays — that sentence is the evidence behind the red line.
  BSG's "have not improved GI outcomes" keeps its acute-prevention context label and is
  never extended to late rectal toxicity.
- **紅線 4 (C4/C5)**: the three fistula anchors — EMBRACE-I 5-year grade 3 or worse
  **3.2%** with "that is the most modern technique there is" attached; the risk factors
  (smoking OR 5.14 as the only significant multivariable factor, stage IVA OR 6.87,
  bevacizumab, prior pelvic surgery, instrumentation); and BSG verbatim **"rule out
  disease recurrence before assuming that it is secondary to radiation injury"**.
  Never "a newer technique avoids it", never "nothing to worry about". The fistula
  emergency-warning section keeps every symptom and the "that is an emergency" line.
  Hyperbaric oxygen: trial by trial, **design label before the numbers** — HOT2 missed
  **both** co-primary endpoints with the authors' "we found no evidence"; RICH-ART is
  positive but **open-label** with 31.4% never responding at five years; Cochrane's
  ceiling is "may be justified". The cost section (30–40 sessions, myopia, seizure
  rate) and the contraindications stay. Taiwan reimbursement: **no conclusion in either
  direction.**
- **Evidence-level labels never swap**: dosimetric / clinical endpoint / modelled /
  retrospective / single-arm / open-label / non-comparative phase II each stays welded
  to its own number. Percentages from different studies are never subtracted or lined
  up as if comparable (B4's explicit prohibition stays a sentence).
- **PARCER** is labelled "image-guided intensity-modulated radiotherapy (delivered on a
  helical tomotherapy unit in that trial)" — never "TOMO beats ordinary IMRT", and
  never "TOMO has no clinical evidence".
- **PARTIQoL**: "the only randomised comparison that has read out showed no difference"
  — not "there is no randomised evidence yet", and not "protons were shown not to work".
- **Cost register**: 「查無公告」= "I could find no official announcement"; never a flat
  "not covered", and **never inferred in either direction** — the five reverse-inference
  prohibitions in the Chinese all survive. Never "worth it".
- **The 48 number-shaped holes stay holes**, at the same strength: days from planning
  scan to first treatment, minutes per session, a week-by-week pelvic skin script (the
  breast series' "peaks about two weeks after finishing" must **not** be borrowed),
  weeks for acute urinary symptoms, the C. difficile proportion, Taiwanese prices for
  spacers and fiducials.

## 3. Canonical English titles

- pel-who → "Which cancers pelvic radiotherapy is used for"
- pel-sim-day → "What happens on the day of the planning scan"
- pel-bladder-bowel → "Bladder and bowel: copying the same state each day"
- pel-implants → "Markers and spacers: two purposes, two kinds of evidence"
- pel-technique-map → "Not three machines — three layers"
- pel-igrt → "Daily imaging: the underrated half"
- pel-toxicity → "What you buy is side effects, not survival"
- pel-proton → "Protons in the pelvis: where the evidence stands"
- pel-skin → "Pelvic skin breaks down in the folds"
- pel-colitis → "Bowel reactions: when they come, how to get through"
- pel-urinary → "Those weeks of bladder and passing urine"
- pel-late → "Late bleeding: treatments and their evidence"
- pel-fistula → "Fistula: risk, warning signs, order of care"

Cross-references inside the topic use these titles verbatim, unlinked. Pointers to
existing site pages keep their live English titles — READ the live `-en` page and copy
the exact title (cx-surgery-or-rt-en, cx-why-chemo-en, cx-pelvic-rt-weeks-en,
cx-brachytherapy-en, rc-five-or-twentyfive-en, rc-diarrhoea-en, rc-perineum-en,
rc-lars-en, pc-rt-how-en, pc-rp-vs-rt-en, pc-bowel-urinary-en, brt-skin-en,
nt-proton-en, insight-proton-en). The two proton pointers in B4 keep their links; all
other cross-references are unlinked.

## 4. Structure & metadata

Same `<h4>` count/order; headings rewritten with natural English tension. 1,100–2,100
words (faithfulness wins). Ends `<hr><h3>References</h3><ol>…</ol><p></p>`; reference
entries identical to the Chinese including author lists and en-dash page ranges. Every
statistical term glossed on first use per article.

Terminology: 骨盆腔 → pelvis / pelvic; 定位（模擬攝影） → planning scan (CT simulation);
固定具 → immobilisation device; 擺位 → set-up; 照野 → field; 標靶 → target volume;
危及器官 → organs at risk; 邊界 → margin; 影像導引 → image guidance (IGRT);
錐狀束電腦斷層 → cone-beam CT; 線上適應性放療 → online adaptive radiotherapy;
強度調控放射治療 → intensity-modulated radiotherapy (IMRT); 弧形調控 → volumetric
modulated arc therapy (VMAT); 螺旋斷層 → helical tomotherapy; 旋轉調控 → rotational
techniques; 質子 → protons; 金標 → fiducial marker; 直腸間隔物 → rectal spacer;
脹尿／滿膀胱 → a full bladder; 空膀胱 → an empty bladder; 再現性 → reproducibility;
分次 → fraction; 低分次 → hypofractionation; 保留膀胱三聯療法 → trimodality
bladder-preserving therapy; 近接治療 → brachytherapy; 放射性皮膚炎 → radiation
dermatitis; 濕性脫屑 → moist desquamation; 皺摺與摩擦處 → folds and areas of friction;
放射性腸炎／直腸炎 → radiation enteritis / proctitis; 裡急後重 → tenesmus;
放射性膀胱炎 → radiation cystitis; 廔管 → fistula; 高壓氧 → hyperbaric oxygen therapy;
氬氣電漿凝固 → argon plasma coagulation; 硫醣鋁 → sucralfate; 栓塞 → embolisation;
造口 → stoma; 醫務課 → medical affairs office; 健保 → National Health Insurance (NHI);
重大傷病 → catastrophic illness certificate. Gy, cc, IMRT, VMAT, TOMO, IGRT, QUANTEC,
PARCER, EMBRACE stay as-is. British spelling throughout (tumour, oesophagus,
randomised, centre, favour, colour, -ise). Metadata per group `meta/<X>-en.json`, same
A1/A2 keying with a `slug` field, titles verbatim from §3.
