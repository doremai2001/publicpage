# brief A — 原理、劑量、硼藥、機器（查證日 2026-09-08）

規則：只有標 PASS 的可以寫進正文。FAIL 一律不寫，不得以「約略」形式繞過。

## 1. 核反應

- **PASS｜熱中子捕獲截面 3837 barn**（¹⁰B，0.025 eV）。兩個獨立來源一致：
  MIT OCW 22.55J BNCT 講義 https://ocw.mit.edu/courses/22-55j-principles-of-radiation-interactions-fall-2004/382568947f61a0473afc13cbe688b3e4_bnct_lect_so4.pdf
  ／ Terranova ML, J Nucl Eng 2026;7(1):6 https://www.mdpi.com/2673-4362/7/1/6
  另有來源寫 3838（PMC9601095）與 3990（PMC9238127，離群值，不用）。
  **正文寫「約 3837 barn」。**
- **PASS｜反應分支與能量**：基態 93.7%（總能量 2.31 MeV）、激發態 6.3%（2.79 MeV，伴隨 0.48 MeV γ）。
  來源：PMC9601095。
- **PASS｜合計射程 5–9 μm，約一個哺乳類細胞直徑**。
  Barth RF et al., Clin Cancer Res 2005;11(11):3987（"limited path lengths in tissue (5–9 μm)"）
  https://aacrjournals.org/clincancerres/article/11/11/3987/290719/
  ＋ Terranova 2026（"4–10 μm, comparable to the diameter of a mammalian cell"）。
- **FAIL｜α 與 ⁷Li 各自的射程**：來源互相矛盾（5/8–9 μm vs 50–100 μm），LET 歸屬也對調。
  **正文只寫合計，不得拆開。**
- **FAIL｜α = 1.47 MeV、⁷Li = 0.84 MeV 個別能量**：查無可引用來源。**不得使用。**

## 2. 劑量

- **PASS｜四個成分**（Koivunoro H, IAEA https://nucleus.iaea.org/sites/accelerators/TMBNCT/Document%20Backup/KOIVUNORO-1.pdf ）：
  硼劑量（高 LET）／¹⁴N(n,p)¹⁴C 質子 0.54 MeV／¹H 快中子反跳質子／低 LET 光子
  （組織內 ¹H(n,γ)²H 2.2 MeV ＋ 射束 γ 污染，兩者合併的分類見 MIT OCW 講義）。
  交叉佐證：Barth 2005。
- **PASS｜Gy-Eq 與加權式** Dw = wb·Db + wγ·Dγ + wn·Dn + wp·Dp（MIT OCW 講義）。
- **PASS｜CBE / RBE 數值**：腫瘤 3.8、皮膚 2.5、口腔黏膜 2.5、腦與脊髓 1.3；
  高 LET 射束成分通用 RBE 3.2。腫瘤 3.8／皮膚 2.5／RBE 3.2 由 Barth 2005 與 MIT 講義雙來源確認。
- **FAIL｜BSH 的 CBE 值**：所有來源皆未提供。**不得寫。**
- **FAIL｜Coderre & Morris 1999 原文**（PMID 9973079）：全文取不到。
  可寫「CBE 概念一般歸功於 Coderre & Morris」，但**數字必須引 Barth 2005**。

## 3. 深度

- **PASS｜超熱中子能量範圍 0.5 eV–10 keV**（Barth 2005；Barth 2012 寫 ~0.4 eV–10 keV）。
- **PASS｜熱中子束通量峰值在皮下約 2–3 cm，10 cm 處降至峰值約十分之一**（PMC9601095）。
- **PASS｜超熱中子可涵蓋皮下 6–8 cm 的淺層腫瘤**（PMC9601095）。
- **PASS｜腦部中線腫瘤在約 8 cm 深處治療比仍 >1**
  Barth RF et al., Radiat Oncol 2012;7:146 https://link.springer.com/content/pdf/10.1186/1748-717X-7-146.pdf
  **這是最權威、最適合引用的深度說法。**

## 4. BPA / borofalan(10B)

- **PASS｜LAT1（SLC7A5）主動轉運**。Kondo N et al., Pharmaceutics 2022;14(5):1106
  https://pmc.ncbi.nlm.nih.gov/articles/PMC9143228/ ；Zheng X et al., Int J Mol Med 2025;56(5)
  https://www.spandidos-publications.com/10.3892/ijmm.2025.5611
- **PASS｜水溶性極差（0.6–0.7 g/L），須與果糖或山梨醇形成複合物**（Kondo 2022）；
  果糖複合後溶解度大幅提升（ISNCT https://isnct.net/bnct-boron-compounds/ ，學會網站非同儕審查，引用需註明）。
  Kondo 2022 另載：不溶造成尿中結晶、可能出現血尿。
- **PASS｜BPA-F 的組織/血液硼濃度比：腫瘤 3.5、正常腦 1.0、皮膚 1.5**（Barth 2012）。
- **PASS｜日本核准品**：販売名「ステボロニン点滴静注バッグ9000mg／300mL」、
  一般名「ボロファラン（10B）」、製造販売元 ステラファーマ株式会社。
  KEGG/JAPIC https://www.kegg.jp/medicus-bin/japic_med?japic_code=00068760
- **PASS｜核准適應症日文原文**：「切除不能な局所進行又は局所再発の頭頸部癌」。
  併用規定原文：「本剤とともに癌を標的として使用することを目的として承認された
  ホウ素中性子捕捉療法用中性子照射装置を使用し、中性子を照射すること。」
  英文（PMDA 審議結果報告書 https://www.pmda.go.jp/files/000237990.pdf ）：
  "Unresectable, locally advanced or locally recurrent head and neck cancer"；併用裝置 "BNCT30"(NeuCure)。
- **PASS｜製造販売承認 2020 年 3 月 25 日；薬価基準収載與発売 2020 年 5 月 20 日**
  （brief C 第 7 節查得，日経メディカル／PR TIMES／KEGG 三來源）。
  註：brief A 當時只確認到「2020 年 3 月」，以 brief C 的日期為準。

## 5. BSH

- **PASS｜被動分布，靠腫瘤處血腦障壁破損進入，細胞攝取差**
  Laird M et al., Nanoscale Adv 2023 https://pubs.rsc.org/en/content/articlehtml/2023/na/d2na00839d ；ISNCT。
- **PASS｜主要用於腦瘤／高惡性度膠質瘤**；化學式 Na₂B₁₂H₁₁SH（Barth 2012）。
- **PASS｜法規身分：至今未取得藥品核准，僅用於臨床試驗。**
  逐字："In 2020, the Japanese Ministry of Health, Labour and Welfare approved BPA under the name of
  borofalan (10B), however, BSH is still only used in clinical trials."（Nanoscale Adv 2023）
  **這句是很好用的對照引句。**

## 6. ¹⁸F-BPA PET 與 T/N 門檻

- **PASS｜T/N > 2.5 是正式收案條件**，出自台北榮總主辦之 NCT01173172
  （"Tumor to Normal tissue (T/N) ratio for BPA >2.5 by 18F-BPA PET scan."）
  鏡像頁 https://ctv.veeva.com/study/boron-neutron-capture-therapy-bnct-for-locally-recurrent-head-and-neck-cancer
  其他收案條件：局部復發且組織學證實之頭頸部惡性腫瘤、曾接受常規放療、
  手術／放療／化療皆不適合救援、病灶最大徑 ≤12 cm、年齡 >18 且 <80、ECOG ≤2。
  **這一組條件就是 B5 與 B17「不是人人可做」的實據。**
- **PASS｜Barth 2012 亦載「if the L/N ratio was more than 2.5, then BNCT was initiated」。**
- **注意**：Lin KH et al., QIMS 2024 的 2.5 是回溯性分層，非前瞻收案條件。
  要說「收案門檻」請引 NCT01173172，不要引 Lin 2024。

## 7. 機器

- **PASS｜住友重機械 NeuCure™ BNCT System ＋ NeuCure™ Dose Engine，
  日本厚生勞動省 2020 年 3 月 12 日核准，為全球首個取得醫材身分的 BNCT 系統。**
  30 MeV 質子 AVF 迴旋加速器、鈹靶。
  https://www.shi.co.jp/english/info/2019/6kgpsq0000002ji0.html
- **PASS｜芬蘭赫爾辛基大學醫院 2025 年 6 月完成歐洲首例加速器型 BNCT 治療**，
  系統為 Neutron Therapeutics nuBeam，病人為進行中臨床試驗的收案者
  （不可切除、局部復發頭頸癌）。
  https://www.raysearchlabs.com/media/press-releases/2025/raystation-used-for-pioneering-clinical-milestone-at-helsinki-university-hospital--first-treatment-with-accelerator-based-bnct-in-europe/
  **更正：nuBeam 不是直線加速器，是緊湊型靜電加速器（2.6 MeV 質子）。正文不得寫成 linac。**
- **PASS（規格）／FAIL（已治療人數）｜筑波 iBNCT001**：8 MeV 質子直線加速器＋鈹靶，
  第一期試驗（新診斷 GBM），目標收案 12–18 人。Nakai K et al., Appl Radiat Isot 2025;226:112152。
  **論文是試驗計畫書，未報告任何已治療人數。正文只能寫「第一期試驗進行中」。**
- **FAIL｜CICS-1（東京國立癌症中心）、韓國 linac、湘南鎌倉 nuBeam 的狀態**：
  僅見於單一綜述，無一手佐證。**不列入。**

## 8. 新一代硼載體

- **PASS（確認為否定）｜臨床上實際用於人體的硼藥仍只有 BPA 與 BSH；
  硼簇脂質體、抗體偶聯、胜肽偶聯全數停留在臨床前，查無任何一個進入人體試驗。**
  Karihtala P, Health Technol 2024 https://link.springer.com/article/10.1007/s12553-024-00862-7 ；
  Zheng D et al., Cancers 2026;18(3):498 https://www.mdpi.com/2072-6694/18/3/498
- **FAIL｜新一代載體的臨床期別**：不存在該數字。**不得編造期別。**
- **陷阱**：有綜述把 "Borofalan(10B)"（就是 BPA）與 "L-¹⁸F-BPA"（PET 顯影劑）
  列在「近期試驗藥劑」表中。**這兩者都不是新一代載體，不得誤寫成已進入臨床。**
