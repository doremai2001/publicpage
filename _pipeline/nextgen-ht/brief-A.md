# brief-A — 原理、熱劑量、機器、測溫（H1–H10）

查證日期：2026-09-07｜查證路徑：Europe PMC REST（EXT_ID／欄位查詢），書目欄位逐字抄錄 API 回傳值。
PASS＝標題／作者／卷期頁／年／DOI 由 API 回傳值抄錄。**只有 PASS 的來源可以引用。**

## 一、可用的數值錨點（每條標明出處）

- 臨床熱治療的溫度區間：39–45 °C（[A1] 摘要原文 "selective heating of tumor tissues to
  temperatures ranging between 39 and 45°C"）。**H1 的溫度光譜圖以此為準，不可自行外推。**
- 熱劑量定義與 R 常數：$\mathrm{CEM43}=\sum_i t_i R^{(43-T_i)}$，$R=0.5\,(T>43)$、$R=0.25\,(T<43)$
  ——原始出處 [A2]（Sapareto & Dewey 1984）。H6 的公式與分段計算示範以此為唯一依據。
- 加熱與放療的時間間隔會影響結果：400 名局部晚期子宮頸癌病人的分析 [A3]，另有同組評論 [A4]。
  **H4／H6 只能寫「間隔會影響結果」，不可寫出具體最佳分鐘數**（該值隨研究而異）。
- 熱抑制 DNA 修復的機轉整理：[A5]（"one treatment to inhibit them all"）。
- 溫和熱治療改善腫瘤氧合的生理機轉：[A6]。
- 順鉑的熱增強（藥物吸收與 DNA 加合物）：[A7]。**H5 只能引用機轉，不可引申為臨床劑量建議。**
- 加熱技術總覽（各類機器與穿透深度）：[A8]（Kok 2020 綜述）。**H7 的穿透深度譜以此為底。**
- MR 測溫的臨床表現與潛力：[A9]。H9 用。
- 品質保證指引：淺部 [A10]；深部區域熱療的臨床研究品保 [A11]；深部設備品保的多中心研究 [A12]。
  **H9 的「什麼叫做有品質的熱治療」以這三份為骨。**

## 二、mEHT 專用（H8）——立場已定，此處只列可引用的原始出處

作者指定的角度：**強調 mEHT 現行不主張以熱效應為作用機轉**，因此熱劑量指標與
以溫度為介入變項的試驗結論，對它既不構成義務、也不能外推。

可引用的第一手來源（皆為該方法研究群本身的論文，符合「引用他們自己的說法」的規格要求）：

- [A13] 機轉主張的近期整理（Krenacs 等，Int J Mol Sci 2020，OA）
- [A14] 臨床證據綜述（Szasz AM 等，Front Oncol 2019，OA）
- [A15] 方法本身的物理／生物電磁學論述（Szasz A，Curr Oncol 2025，OA）
- [A16] 臨床驗證整理（Lee SY 等，Cancers 2023，OA）
- [A17] **南非第三期隨機試驗（Minnaar 等，PLoS One 2019，OA）**——摘要載明為
  ongoing Phase III randomised controlled trial，FIGO IIB–IIIB 鱗癌，mEHT 每週兩次、
  於體外放療前施行，**主要終點為六個月局部疾病控制**，分層含 HIV 狀態。
  **注意：本文報告的是六個月局部控制，不是三年存活。**
- [A18] 二年與三年存活的後續報告（Minnaar 等，Cancers 2022，OA）——
  **作者簡報中的「3 年 DFS 35.4% 對 13.7%」須對應到本篇而非 [A17]；引用前逐字核對。**

**H8 撰稿限制（來自 SPEC 紅線）**：不寫「mEHT 無效」、不寫「非熱效應不存在」、
不用貶抑性字眼、不點名醫院、不涉費用。所有機轉描述必須可回溯到 [A13]–[A16] 的原文。

## Sources

- **[A1] PASS** — Datta NR, Ordóñez SG, Gaipl US, Paulides MM, Crezee H, Gellermann J, et al. *Local hyperthermia combined with radiotherapy and-/or chemotherapy: recent advances and promises for the future.* Cancer Treatment Reviews, 41(9), 742-753 (2015). DOI: 10.1016/j.ctrv.2015.05.009。PMID 26051911；OA N。Route: Europe PMC REST
- **[A2] PASS** — Sapareto SA, Dewey WC. *Thermal dose determination in cancer therapy.* International Journal of Radiation Oncology, Biology, Physics, 10(6), 787-800 (1984). DOI: 10.1016/0360-3016(84)90379-1。PMID 6547421；OA N。Route: Europe PMC REST
- **[A3] PASS** — Kroesen M, Mulder HT, van Holthe JML, Aangeenbrug AA, Mens JWM, van Doorn HC, et al. *The Effect of the Time Interval Between Radiation and Hyperthermia on Clinical Outcome in 400 Locally Advanced Cervical Carcinoma Patients.* Frontiers in Oncology, 9, 134 (2019). DOI: 10.3389/fonc.2019.00134。PMID 30906734；OA Y。Route: Europe PMC REST
- **[A4] PASS** — Kroesen M, Mulder HT, van Rhoon GC, Franckena M. *Commentary: The Impact of the Time Interval Between Radiation and Hyperthermia on Clinical Outcome in Patients With Locally Advanced Cervical Cancer.* Frontiers in Oncology, 9, 1387 (2019). DOI: 10.3389/fonc.2019.01387。PMID 31921644；OA Y。Route: Europe PMC REST
- **[A5] PASS** — Oei AL, Vriend LE, Crezee J, Franken NA, Krawczyk PM. *Effects of hyperthermia on DNA repair pathways: one treatment to inhibit them all.* Radiation Oncology, 10, 165 (2015). DOI: 10.1186/s13014-015-0462-0。PMID 26245485；OA Y。Route: Europe PMC REST
- **[A6] PASS** — Vaupel P, Piazena H, Notter M, Thomsen AR, Grosu AL, Scholkmann F, et al. *From Localized Mild Hyperthermia to Improved Tumor Oxygenation: Physiological Mechanisms Critically Involved in Oncologic Thermo-Radio-Immunotherapy.* Cancers, 15(5), 1394 (2023). DOI: 10.3390/cancers15051394。PMID 36900190；OA Y。Route: Europe PMC REST
- **[A7] PASS** — Ohno S, Siddik ZH, Kido Y, Zwelling LA, Bull JM. *Thermal enhancement of drug uptake and DNA adducts as a possible mechanism for the effect of sequencing hyperthermia on cisplatin-induced cytotoxicity.* Cancer Chemotherapy and Pharmacology, 34(4), 302-306 (1994). DOI: 10.1007/bf00686037。PMID 8033297；OA N。Route: Europe PMC REST
- **[A8] PASS** — Kok HP, Cressman ENK, Ceelen W, Brace CL, Ivkov R, Grüll H, Ter Haar G, et al. *Heating technology for malignant tumors: a review.* International Journal of Hyperthermia, 37(1), 711-741 (2020). DOI: 10.1080/02656736.2020.1779357。PMID 32579419；OA N。Route: Europe PMC REST
- **[A9] PASS** — Feddersen TV, Hernandez-Tamames JA, Franckena M, van Rhoon GC, Paulides MM. *Clinical Performance and Future Potential of Magnetic Resonance Thermometry in Hyperthermia.* Cancers, 13(1), 31 (2020). DOI: 10.3390/cancers13010031。PMID 33374176；OA Y。Route: Europe PMC REST
- **[A10] PASS** — Trefná HD, Crezee H, Schmidt M, Marder D, Lamprecht U, Ehmann M, Hartmann J, et al. *Quality assurance guidelines for superficial hyperthermia clinical trials: I. Clinical requirements.* International Journal of Hyperthermia, 33(4), 471-482 (2017). DOI: 10.1080/02656736.2016.1277791。PMID 28049386；OA N。Route: Europe PMC REST
- **[A11] PASS** — Bruggmoser G, Bauchowitz S, Canters R, Crezee H, Ehmann M, Gellermann J, et al. *Quality assurance for clinical studies in regional deep hyperthermia.* Strahlentherapie und Onkologie, 187(10), 605-610 (2011). DOI: 10.1007/s00066-011-1145-x。PMID 21932026；OA N。Route: Europe PMC REST
- **[A12] PASS** — De Lazzari M, Carrapiço-Seabra C, Marder D, van Rhoon GC, Curto S, Dobsicek Trefna H, et al. *Toward enhanced quality assurance guidelines for deep hyperthermia devices: a multi-institution study.* International Journal of Hyperthermia, 41(1), 2436005 (2024). DOI: 10.1080/02656736.2024.2436005。PMID 39658024；OA N。Route: Europe PMC REST
- **[A13] PASS** — Krenacs T, Meggyeshazi N, Forika G, Kiss E, Hamar P, Szekely T, Vancsik T. *Modulated Electro-Hyperthermia-Induced Tumor Damage Mechanisms Revealed in Cancer Models.* International Journal of Molecular Sciences, 21(17), 6270 (2020). DOI: 10.3390/ijms21176270。PMID 32872532；OA Y。Route: Europe PMC REST
- **[A14] PASS** — Szasz AM, Minnaar CA, Szentmártoni G, Szigeti GP, Dank M. *Review of the Clinical Evidences of Modulated Electro-Hyperthermia (mEHT) Method: An Update for the Practicing Oncologist.* Frontiers in Oncology, 9, 1012 (2019). DOI: 10.3389/fonc.2019.01012。PMID 31737558；OA Y。Route: Europe PMC REST
- **[A15] PASS** — Szasz A. *Bioelectromagnetism for Cancer Treatment-Modulated Electro-Hyperthermia.* Current Oncology, 32(3), 158 (2025). DOI: 10.3390/curroncol32030158。PMID 40136362；OA Y。Route: Europe PMC REST
- **[A16] PASS** — Lee SY, Lorant G, Grand L, Szasz AM. *The Clinical Validation of Modulated Electro-Hyperthermia (mEHT).* Cancers, 15(18), 4569 (2023). DOI: 10.3390/cancers15184569。PMID 37760538；OA Y。Route: Europe PMC REST
- **[A17] PASS** — Minnaar CA, Kotzen JA, Ayeni OA, Naidoo T, Tunmer M, Sharma V, Vangu MD, et al. *The effect of modulated electro-hyperthermia on local disease control in HIV-positive and -negative cervical cancer women in South Africa: Early results from a phase III randomised controlled trial.* PLoS One, 14(6), e0217894 (2019). DOI: 10.1371/journal.pone.0217894。PMID 31216321；OA Y。Route: Europe PMC REST
- **[A18] PASS** — Minnaar CA, Maposa I, Kotzen JA, Baeyens A. *Effects of Modulated Electro-Hyperthermia (mEHT) on Two and Three Year Survival of Locally Advanced Cervical Cancer Patients.* Cancers, 14(3), 656 (2022). DOI: 10.3390/cancers14030656。PMID 35158924；OA Y。Route: Europe PMC REST
- **[A19] PASS** — Overgaard J. *Effect of hyperthermia on malignant cells in vivo. A review and a hypothesis.* Cancer, 39(6), 2637-2646 (1977). DOI: 10.1002/1097-0142(197706)39:6<2637::aid-cncr2820390650>3.0.co;2-s。PMID 872062；OA N。Route: Europe PMC REST
- **[A20] PASS** — Overgaard J. *The effect of sequence and time intervals of combined hyperthermia and radiation treatment.* The British Journal of Radiology, 50(598), 763-765 (1977). DOI: 10.1259/0007-1285-50-598-763。PMID 922287；OA N。Route: Europe PMC REST
- **[A21] PASS** — Song CW, Lin JC, Chelstrom LM, Levitt SH. *The kinetics of vascular thermotolerance in SCK tumors of A/J mice.* International Journal of Radiation Oncology, Biology, Physics, 17(4), 799-802 (1989). DOI: 10.1016/0360-3016(89)90069-2。PMID 2777670；OA N。Route: Europe PMC REST（**動物實驗——引用時必須標明**）
