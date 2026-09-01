# 乳房放射治療專題 — English edition spec

Supplementary. **Read `/home/claude/colon/SPEC-EN.md` first** (no-drift rules, British
spelling, structure, report-don't-fix). Then `/home/claude/brt/SPEC.md` §一/§三 and
§八 修正, plus `/home/claude/brt/FIXES.md` (the invariants section) — all bind the
English equally.

## 1. Fixed disclosure — one rendering, byte-identical across 10

> <p>My position first: every technique compared in this topic — ordinary
> intensity-modulated radiotherapy, TOMO, deep inspiration breath-hold — has a
> self-paid component among the more expensive options, and all of them are delivered
> in my own department; protons mean a referral elsewhere. So every "better" here comes
> with its primary source and the level of evidence behind it, and on cost I cite the
> official schedule where one exists and tell you to ask the medical affairs office
> where it does not. Concluding that the basic option is enough for you is a completely
> reasonable conclusion.</p>

## 2. The passages English will break

- **紅線 1 (B group, bidirectional)**: nothing readable as "you cannot protect the
  heart without paying"; the sentence **"the heart-sparing of ordinary
  intensity-modulated radiotherapy does real work"** stays a full paragraph in B1, B2
  and B3. Reverse direction equally: the dosimetric advantage is never shrunk to
  "they are all the same". Technique choice is written as decided by indication,
  never by budget.
- **Evidence-level labels never swap**: "dosimetric" vs "clinical outcome" vs
  "modelled estimate" vs "retrospective" vs "randomised" — each stays attached to its
  own number. DIBH: the reduction is **dosimetric**, and "there is no direct evidence
  that DIBH reduces cardiac events" stays at full strength.
- **DIBH reduction** = "about 20 to 70%, and it varies a lot between people" — never
  a single mid-range figure.
- **修正 5 (B2)**: TOMO is never written as "better for the heart". The Taiwanese
  108-patient comparison (VMAT mean heart dose 3.82 Gy vs TOMO 5.13 Gy) travels with
  the pro-TOMO numbers, and "there is no randomised clinical comparison of TOMO
  against ordinary IMRT" stays. TomoDirect keeps its identity — it is the tomotherapy
  unit's own fixed-field mode, **not** IMRT on a linac.
- **修正 6 (B3)**: RADCOMP is **not read out**, and the registry's estimated primary
  completion is 2036 — "not read out" is not "about to read out". Proton skin
  reaction stays two-sided (97.2% vs 75% in one randomised interim ↔ 47% vs 48% under
  skin constraints): "the entrance side has none of the photon skin-sparing effect, so
  skin dose depends on the plan".
- **Cost register**: 「查無公告」= "I could find no official announcement" — never a
  flat "not covered", and never inferred as "so there is a fee". The Kaohsiung Chang
  Gung breath-hold price keeps **both** labels: it is a **proton** item, and it is not
  a reference price for photon breath-hold. The non-recommendation sentence after the
  price list stays.
- **紅線 2 (A2)**: the clinic's practice and the international direction are both
  left standing. The missing-cell paragraph (breast conservation + 1–3 positive nodes
  + whole breast only) keeps its exact framing: **"this is an institutional
  limitation, not a doubt about the evidence"**.
- **紅線 3 (C2)**: the BC Cancer grade-to-action pairing is quoted faithfully —
  moist desquamation = **URGENT, medical assessment within 24 hours**; the four
  infection signs complete; "come back and let us look at it"; and no self-care
  sentence may be moved above that line or soften it. Never instruct a patient to
  dress an open wound themselves.
- **修正 2 (A1)**: 1–3 positive nodes = "a decision to discuss"; ≥4 = "recommended".
  The two EBCTCG figures stay separate and SUPREMO is presented alongside.
- **The 11 number-shaped holes stay holes**: days from simulation to first treatment,
  minutes per session, seconds per breath-hold, a week-by-week skin script, months for
  pigmentation to fade, years for mammograms to settle, Taiwanese dressing
  reimbursement. Where the Chinese says "I could not find a citable source, so I am
  not giving a number", the English says the same, at the same strength.
- **Word-proportion rule**: every number identical, including ones written as Chinese
  proportions; hedges at equal strength.

## 3. Canonical English titles

- brt-who-needs → "The operation is done — why radiotherapy as well?"
- brt-fractionation → "Why am I not on the shorter course?"
- brt-technique-map → "The machine, and the breathing"
- brt-heart → "Heart dose: the core question on the left side"
- brt-tomo → "TOMO and ordinary IMRT: where the difference is"
- brt-proton → "Protons for the breast: where the evidence stands"
- brt-sim-to-first → "From planning scan to first treatment"
- brt-skin → "Skin reactions: when they come, how to care for them"
- brt-beyond-skin → "Beyond the skin: fatigue, lungs, lymphoedema"
- brt-after → "After it ends: recovery and the long run"

Cross-references inside the topic use these titles verbatim. Pointers to existing site
pages keep their live English titles — READ the live `-en` page and copy the exact
title (bc-rt-regional-en, bc-rt-hypofx-en, bc-rt-omission-en, bc-lymphoedema-en,
bc-followup-schedule-en, care-fatigue-en, nt-proton-en, insight-proton-en). Link style
follows the Chinese: in-topic references are unlinked, the two cross-topic proton
pointers in B3 keep their links.

## 4. Structure & metadata

Same `<h4>` count/order; headings rewritten with natural English tension. 1,100–2,100
words (faithfulness wins). Ends `<hr><h3>References</h3><ol>…</ol><p></p>`; reference
entries identical to the Chinese, including author lists and en-dash page ranges.
Every statistical term glossed on first use per article.

Terminology: 乳房保留手術 → breast-conserving surgery; 全乳房切除 → mastectomy;
術後放射治療 → post-mastectomy radiotherapy (PMRT) where it follows mastectomy,
otherwise adjuvant radiotherapy; 全乳照射 → whole-breast irradiation; 區域淋巴 →
regional nodal irradiation; 內乳淋巴結 → internal mammary nodes; 鎖骨上 →
supraclavicular; 低分次 → hypofractionation; 傳統分次 → conventional fractionation;
分次 → fraction; 強度調控放射治療 → intensity-modulated radiotherapy (IMRT); 弧形調控 →
volumetric modulated arc therapy (VMAT); 旋轉調控 → rotational techniques; 深吸氣閉氣 →
deep inspiration breath-hold (DIBH); 定位／模擬攝影 → planning scan (CT simulation);
擺位 → set-up; 照野 → field; 標靶 → target volume; 危及器官 → organs at risk;
劑量學 → dosimetric; 平均心臟劑量 → mean heart dose; 左前降支 → left anterior
descending artery (LAD); 濕性脫屑 → moist desquamation; 放射性皮膚炎 → radiation
dermatitis; 纖維化 → fibrosis; 毛細血管擴張 → telangiectasia; 色素沉著 →
pigmentation; 放射性肺炎 → radiation pneumonitis; 淋巴水腫 → lymphoedema;
組織等效物 → bolus; 醫務課 → medical affairs office; 健保 → National Health Insurance
(NHI); 給付碼 → reimbursement code. Gy, TOMO, IMRT, VMAT, DIBH, LAD stay as-is.
British spelling throughout (tumour, oesophagus, randomised, centre, favour,
lymphoedema, -ise). Metadata per group `meta/<X>-en.json`, titles verbatim from §3.
