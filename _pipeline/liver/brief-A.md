# Brief A — 肝癌專題確診之後群（A1–A5）

研究員：Group A｜查證日期：2026-08-30｜期刊書目與數字全部經 Europe PMC REST 逐筆核對（DOI、卷期頁、摘要數字）；指引與共識引語出自可取得之全文（NCBI PMC 全文 XML，逐字擷取）；台灣官方頁面與 PDF 經實際抓取（抓取路徑逐條註明）。
引用規則：**只有標 PASS 的來源可以進正文引用。** FAIL / NOT-CITABLE 條目保留。每個數字帶族群標籤（肝硬化狀態、病因、地區）。
跨組約定（SPEC §八修正 4）：**各指引對 SBRT 的措辭光譜歸 B 組 brief 所有**（B 之 [S13] BCLC 2022、[S15] AASLD 2023、[S18] APASL 2017、[S20][S21] TLCA、FAIL-2 ESMO）——A3 寫指引差異時直接指向 B brief 的來源 ID，本組不重查、不重列。

## ⚠ 五件與 SPEC 假設不同形狀的事（動筆前必讀）

1. **「肝癌腹超篩檢政策」查證結果：不存在全國性肝癌腹部超音波公費篩檢。** 官方文件是〈國家肝炎及肝癌防治計畫（2026-2030年）〉[S41]：公費項目是 **45–79 歲（原住民 40–79 歲）終身一次的 B、C 肝篩檢**（2020-09-28 調整生效，2024 年起每案補助 200→370 元），肝癌的早期發現則依賴 B/C 肝個案的醫療端追蹤（健保「B 型肝炎帶原者及 C 型肝炎感染者醫療給付改善方案」，2010 年起）。該計畫自己承認缺口：台灣早期（BCLC 0-A）診斷比例約 40.4%、日本 62%，並點名 PIVKA-II 健保給付僅限「肝硬化之慢性肝炎與肝癌接受根除治療之患者」是限制之一[S41]。A4/D1 寫追蹤時照這個形狀寫，不要寫成「政府有肝癌超音波篩檢」。
2. **NHI 網站 HTML 全面擋爬（Cloudflare 403），藥品給付規定原始條文取不到；但 B 肝抗病毒的「肝癌條款」在官方計畫文件裡有逐字轉述。** 〈國家肝炎及肝癌防治計畫（2026-2030年）〉載明：「自2019年2月1日起增列**肝癌並接受根除性治療且 HBV DNA≧2000 IU/mL，可長期使用 B 型肝炎口服治療藥品，直至肝癌復發且未能再次接受根除性治療止**」[S41]。引用時標明出處是官方計畫文件的轉述，不是給付規定條文本身（FAIL-3）；未涵蓋的情境（如 HBV DNA<2000 的肝癌病人、非根除性治療者的預防性投藥）寫「請與醫療團隊確認現行給付條件」。
3. **DAA 與肝癌復發的故事已經「結案」，而且結局比 SPEC 預期的更乾淨。** 2016 年 Reig 的警訊（58 人、中位追蹤 5.7 個月、復發 27.6%）[S31]→ 2017 年統合迴歸（41 篇、13,875 人）校正追蹤時間與年齡後無差異[S32]→ 2019 年北美 31 中心世代：復發 HR 0.90（無關聯）[S33]、死亡 HR 0.54（SVR 者 0.29）[S34]→ AASLD 2023 指引原文收尾：「two large multicenter studies from North America and Italy **confirmed** that eradication of HCV with direct-acting antiviral therapy **does not increase risk of HCC recurrence and improves survival**」[S1]。A4 可以放心寫成「一場已經被解決的虛驚」，但要把警訊研究的存在誠實寫出來。
4. **LR-5 的正確賣點是「陽性很準」，不是「抓得全」。** LR-5 判為肝癌的正確率（PPV）94–96%[S9][S10]，但 LR-5 對肝癌的**敏感度只有 61.3%**（IPD 統合，4,727 個病灶）[S11]——很多真的肝癌一開始不落在 LR-5。A1 不可寫成「影像可以抓到所有肝癌」；「沒切片就確診」的正當性在特異度端，不在敏感度端。
5. **重大傷病證明查到法規層級原文：肝癌（惡性腫瘤 C00-C96.9 之「其他惡性腫瘤」類）有效期限五年。** 出處是〈全民健康保險保險對象免自行負擔費用辦法〉第二條附表一（114-01-01 起適用版，法務部全國法規資料庫附件 PDF 實際下載）[S39][S40]。比預期更完整：申請文件、診斷證明 30 日內有效、保險人 14 日內核定、免部分負擔範圍（第 6 條）全部有原文。

---

## A1 `lv-no-biopsy`〈為什麼肝癌常常不用切片就確診〉

### Key facts

**可引用的診斷準則（原文逐字，PMC 全文核對）**

- AASLD 2023[S1]：「In most at-risk patients, including those with HBV infection or cirrhosis from any etiology, **the diagnosis of HCC should be based on noninvasive imaging criteria or pathology**.」；正式建議句：「In at-risk patients with cirrhosis or chronic HBV infection, the diagnosis of HCC should be based on noninvasive imaging criteria and/or pathology (**Level 1, Strong Recommendation**)」「The noninvasive diagnosis of HCC should be based on either dynamic contrast-enhanced MRI or multiphasic CT (Level 1, Strong Recommendation)」。AASLD 明言支持 LI-RADS 演算法（特徵：大小、動脈期顯影 APHE、延遲期 washout、包膜）。
- **反面（何時必須切片）**，AASLD 2023 原文[S1]：「**Pathological diagnosis of HCC should be obtained for liver nodules in patients without cirrhosis or without HBV infection because LI-RADS criteria are not applicable to this population.**」「Noninvasive imaging criteria have insufficient accuracy in these patient populations (Level 1, Strong Recommendation)」；LR-M（非典型、疑非肝癌惡性）：「Biopsy should be performed in patients with an LR-M observation given the risk of mixed tumors and malignant non-HCC tumors (Level 1, Strong Recommendation)」；LR-TIV（血管內腫瘤）同樣建議切片；臨床試驗情境：「AASLD also advises performing biopsies in the setting of clinical trials for all LR-4–5 lesions」，並可由多專科團隊考慮於試驗外執行以取得分子資訊。
- LI-RADS 適用族群限制（原文）：「LI-RADS criteria have only been validated in populations warranting HCC surveillance, including patients with cirrhosis, noncirrhotic HBV infection with intermediate or high risk of HCC, or history of prior HCC.」[S1]（非肝硬化 HBV 帶原者研究：280 人中 PAGE-B≥10 者 LR-5 為肝癌機率 >90%[S1]。）
- EASL：2018 年版（歐洲的影像診斷準則出處）[S2]與 2025 年新版[S3]均存在，**內文措辭均取不到（FAIL-1、FAIL-4），只可引書目**；歐洲準則的具體條件正文不引，寫「EASL 同樣採影像診斷路線（限肝硬化病人），原文我取不到可公開引用的版本」。

**LR 各分類實際是肝癌的比例（分母齊全）**

- van der Pol 2019 系統性回顧（17 篇回溯性研究、2,760 人、3,556 個病灶、2,482 個肝癌；高風險族群）[S9]：**LR-5：94% 是肝癌**（95% CI 92–96%）、97% 是惡性；**LR-4：74%**（67–80%）；**LR-3：38%**（31–45%）；LR-2：13%；**LR-M：36% 是肝癌、但 93% 是惡性**；LR-TIV：79% 是肝癌。作者自註：LR-2/LR-3 的肝癌比例顯示現行管理可能太被動；有 verification bias。
- Adamo 2025 IPD 統合（46 篇、6,765 人、7,500 個病灶，LI-RADS v2018）[S10]:**LR-5 合併 PPV 95.81%**（91.06–98.09）、LR-4 80.82%、LR-3 58.28%（此統合的 LR-3 偏高、80% 研究至少一項偏倚高風險——與 [S9] 的 38% 並陳時要標各自族群與版本）。
- **敏感度的誠實面**：Goins 2023 IPD 統合（24 篇、3,840 人、4,727 病灶，中位大小 19 mm）[S11]：LR-5 敏感度 **61.3%**（45.9–74.7）、PPV 92.3%。
- AASLD 對各分類的管理建議（原文）[S1]：LR-5＝肝癌機率「95%–99%」（其引用之統合）；LR-4 ~75%→「biopsy or close-interval follow-up imaging at 3 months」＋多專科討論；LR-3 ~30%→「repeat CT or MRI in 3–6 months」；「For patients in whom an immediate diagnosis would make an impact on management decisions, the AASLD advises biopsy over repeat imaging.」

**切片本身的代價與極限（拿掉「切片才安心」的迷思用）**

- AASLD 2023 原文[S1]：切片敏感度「between 70% and 93% for most tumors but has been reported as low as ~60% in tumors < 2 cm」；「A negative biopsy does not eliminate the possibility of HCC」（陰性建議追蹤、必要時二次切片）；併發症（腫瘤針道散播、出血）「~3%」，同軸技術已大幅下降。
- AASLD 反對用血液指標確診：「AASLD advises against use of biomarkers, including AFP alone or liquid biopsy, to make a diagnosis of HCC given insufficient accuracy.」[S1]

**台灣錨點（官方共識原文，OA 全文核對）**

- TLCA/消化系醫學會 2023 共識[S4]，Statement 2-3（同意度 100%）：「**For nodules larger than 1 cm in patients with cirrhosis or chronic hepatitis B or C, characteristic vascular patterns on a four-phase CEUS, MDCT, MRI, or EOB-MRI image could be diagnosed without biopsy.**」＋「In cases where the vascular pattern is not characteristic, or in patients with non-cirrhotic livers or without chronic hepatitis B or C, biopsy may be performed.」＋切片陰性追蹤 2 年（Statement 2-4）；<1 cm 者 3–6 個月追蹤（Statement 2-1）。台灣演算法納入 EOB-MRI 與 CEUS 是在地特色[S4]。

### Claim ceiling

- 可寫：「在肝硬化或慢性 B/C 肝的高風險族群，>1 cm 的結節若在動態影像呈典型血流特徵，國際（AASLD）與台灣（TLCA）準則都允許不切片確診」；「LR-5 判肝癌，錯的機率約 4–6%（統合分析）」；「LR-3 約三到四成、LR-4 約四分之三最後是肝癌——所以它們的答案是追蹤或切片，不是放心」；「切片不是零成本：小腫瘤敏感度可低到六成、陰性不能排除、併發症約 3%」；「沒有肝硬化也不是 B 肝帶原→影像準則不適用，需要切片」。
- **不可寫**：「影像診斷比切片準」（兩者角色不同；LR-5 敏感度只有六成一）；「LR-5 = 100% 肝癌」；「不用切片＝不用組織」（LR-M、無肝硬化、試驗都要）；「AFP 可以確診肝癌」（AASLD 明文反對）；不可引用 EASL 2018/2025 的具體條文措辭（取不到原文）。
- 每個百分比帶標籤：全部來自「高風險（肝硬化／B肝）監測族群」，不可外推到一般人的偶見肝結節。

### Caveats

- [S9][S10] 均為回溯性研究之合併，verification bias 與 case-control 設計是主要偏倚（[S9] 作者自承）。
- LR-3/LR-4 的「不確定地帶」是這篇的誠實核心：AASLD 的處置（3–6 個月追蹤／3 個月影像或切片＋多專科討論）要寫成正文，不是註腳。
- CEUS（顯影超音波）在 AASLD 是二線[S1]、在台灣共識是特定條件下的一線之一（Sonazoid Kupffer 相，Statement 1-3）[S4]——差異可如實並陳。

### 台灣現況

- 診斷路徑錨在 TLCA 2023 共識[S4]（OA、逐字可引）。健保影像檢查給付細節（MRI/CT 事前審查等）**查無可引用之官方原文**（NHI 網站擋爬，FAIL-3）→寫「檢查安排依醫院與健保規定，細節問個管師」。

---

## A2 `lv-two-diseases`〈你同時有兩個病〉（全專題地基篇）

### Key facts

**Child-Pugh：是什麼、從哪來、弱點在哪（全部有原文）**

- 起源：Pugh 1973（食道靜脈曲張出血手術的風險分級；Child-Turcotte 1964 的修改版）[S12]——書目可引，內文無摘要，**分項內容引 [S13] 的轉述**。
- Demirtas 2021（JHEP Reports 綜述，OA 全文核對）[S13]：「CPS is made up of **5 parameters: albumin, bilirubin, prothrombin/international normalised ratio, extent of ascites, and degree of hepatic encephalopathy**, each parameter of which is weighted to derive a cumulative score」；分級與預後：「**CP-A is associated with a 2-year survival of 85%, CP-B 60% and CP-C 35%**」；史源：「originally introduced in 1964 for the preoperative assessment of mortality from bleeding varices」；弱點：「the assessment of 2 key components of the score, hepatic encephalopathy and ascites, are **subjective** and the severity may vary with the use of lactulose and diuretics」。
- BCLC 2022 已經把 Child-Pugh 降位（原文）[S7]：「the evaluation of underlying liver function, for which **the Child-Pugh classification was already abandoned in the last BCLC version**, warrants a further update」＋「Decompensation of liver disease (jaundice, ascites, encephalopathy) reflects non-preserved liver function **irrespective of the Child-Pugh or MELD score**」＋「compensated liver function could be stratified with additional granularity by using the albumin-bilirubin (ALBI) score」。

**ALBI（可引用的起源論文）**

- Johnson 2015（J Clin Oncol）[S14]：日本 1,313 位各期肝癌病人推導、其他地區 5,097 人＋切除 525 人＋sorafenib 1,132 人驗證；只用**白蛋白與總膽紅素**兩個客觀值；表現至少與 Child-Pugh 相當；**在 Child-Pugh A 之內再分出兩群預後明顯不同的人**；「This new model eliminates the need for subjective variables such as ascites and encephalopathy.」

**失代償事件的預後重量（數字齊、標籤齊）**

- D'Amico 2014（義大利單中心 inception cohort，494 人、82% HCV、平均追蹤 145 個月）[S16]：五個臨床階段的 **5 年死亡率：代償無靜脈曲張 1.5%→有靜脈曲張 10%→出血 20%→第一次非出血性失代償 30%→第二次失代償事件 88%**。失代償定義：腹水、出血、黃疸、肝性腦病變。
- D'Amico 2006（118 篇系統性回顧，「代償與失代償是兩種病」的經典出處）[S17]：**書目可引；常被轉述的中位存活數字無法核對（無摘要、無 OA 全文）——數字一律用 [S16]，不用記憶中的「12 年 vs 2 年」（FAIL-8）**。

**競爭風險：死於肝，還是死於癌（A2 的思想核心，兩個層級的證據）**

- Cabibbo 2017（義大利 ITA.LI.CA，328 位 HCV 肝硬化、BCLC 0/A 根治後完全反應）[S18]：5 年存活 44%；一年內**肝失代償**者死亡 HR **7.52**（95% CI 1.23–13.48），一年內**腫瘤復發**者 HR **2.50**（1.23–5.05）——同一群病人裡，肝的事件比癌的事件更致命（HCV 族群、DAA 前時代，標籤要帶）。
- 指引層級的同一句話，AASLD 2023 原文[S1]：「Surveillance…has **no benefit in most patients with Child-Turcotte-Pugh C cirrhosis—outside of liver transplantation—given the high competing risk of liver-related mortality**.」（連「要不要找癌」都取決於肝——競爭風險的官方版。）

**MELD 一句話**

- Kamath 2001[S15]：MELD＝膽紅素、肌酸酐、INR 的數學式，預測末期肝病 3 個月死亡（住院失代償病人 c-statistic 0.87），後來成為移植分配的排序工具。（美國以 MELD-Na 分配、HCC 有 MELD exception 加分制度——引 AASLD 敘述[S1]，一句話帶過，細節歸 B4。）

### Claim ceiling

- 可寫：「Child-Pugh 用五個項目把肝功能分 A/B/C；A 級兩年存活約 85%、B 約 60%、C 約 35%（綜述引用值，非台灣族群）」；「它有兩個著名弱點：腹水與腦病變靠人判斷、而且原本是 1960 年代替靜脈曲張出血手術設計的」；「ALBI 只用白蛋白＋膽紅素，能在 Child-Pugh A 裡再分出預後不同的兩群人（1,313 人推導、6,000 多人驗證）」；「失代償是分水嶺：同一批病人，從代償無靜脈曲張到第二次失代償，5 年死亡率從 1.5% 一路升到 88%（義大利世代，多為 C 肝）」；「治好腫瘤的人，早期肝失代償對存活的威脅（HR 7.5）大於腫瘤早期復發（HR 2.5）（HCV 族群）」。
- **不可寫**：「Child-Pugh 已被淘汰」（BCLC 的原文是「在 BCLC 分期內」棄用、AASLD 說它仍是最廣用工具[S1]——寫「分期系統逐步改用更細的工具，臨床仍每天在用」）；「ALBI 比 Child-Pugh 準」（原文是 performed at least as well）；「失代償＝死刑」（D'Amico 的 88% 是「第二次失代償事件」那格、且是 5 年）；不可使用「12 年 vs 2 年」這類無法核對的轉述數字。
- 全系列肝功能名詞引用本篇，不重複解釋（SPEC §五）。

### Caveats

- [S16] 是 1980 年代收案的義大利世代（HCV 為主、無現代抗病毒治療）——數字方向可靠、絕對值對今日台灣 B 肝病人偏悲觀，要標年代。
- [S18] 是 DAA 前的 HCV 族群；其作者自己說 DAA 可能透過保住肝功能改善存活——與 A4 的 DAA 段落互相呼應。
- 競爭風險的白話翻譯建議：「兩個病在賽跑」；統計名詞第一次出現要翻白話（colon SPEC §三）。

### 台灣現況

- 肝功能分級本身無給付／政策爭點。台灣端的落點在 A4（抗病毒給付以「肝功能／纖維化」為條件）與 B 組（37047B 給付條件含 Child-Pugh A–B）——一句話指路即可。

---

## A3 `lv-staging-bclc`〈分期表把你放在哪一格，以及它沒說的〉

### Key facts

**BCLC 2022 本體與它自己承認的限制（OA 全文逐字，PMC8866082）**

- 結構：五期（0/A/B/C/D）連結第一線治療建議[S7]；2022 版把肝功能評估從 Child-Pugh 改為「失代償事件＋ALBI/MELD 分層」＋加入 AFP[S7]（AASLD 的轉述可並用：「The BCLC was updated in 2022 to refine prognostication by highlighting the benefit of using objective scores, such as MELD and ALBI」[S1]）。
- **「臨床決策」段落（這篇文章的靈魂，原文逐字）**[S7]：「clinical practice guidelines and algorithms such as the BCLC model reveal the current state of knowledge…but **the ultimate decision must be taken by the responsible physician and tumour board**」;「**Therefore, clinical decision-making and treatment recommendations should not merely be based on a simplified figure but on a complex process that requires personal insights and expertise.**」
- **治療期別轉移（treatment stage migration, TSM）原文**[S7]：「the specific profile of an individual patient may induce a shift in the recommendation to a treatment considered a priority for a more advanced stage (TSM concept)」；Key point：「Tumour progression and/or treatment-related adverse events may lead to treatment recommendations that would usually be for a more advanced stage even if BCLC stage has not changed.」
- BCLC 自認 B 期異質[S7]：「the magnitude of tumour burden may be quite heterogeneous in this stage, and prognosis is also influenced by AFP concentration and the degree of liver function impairment even if still belonging to Child-Pugh class A」。
- 多專科入文[S7]：「In clinical practice, the evaluation of a patient's status incorporates BCLC staging and, simultaneously, the expert and personalised approach of the treating physician and **multidisciplinary tumour board**…」
- **BCLC 2026 更新版已出版**（J Hepatol 2026;84:631–654）[S8]——僅書目可引，內文措辭取不到（FAIL-2，同 B brief FAIL-1）；正文寫「2026 年更新版我取不到原文，本文引用停在 2022 版」。

**有紀錄的批評與亞太的另一套做法（每個數字帶標籤）**

- BCLC B 異質性的起點文獻：Bolondi 2012（專家小組，提出 B1–B4 次分類）[S19]：「comprises a highly heterogeneous patient population」。
- **香港 HKLC**（Yau 2014，Gastroenterology；香港瑪麗醫院 3,856 人、**以 B 肝為主**）[S20]：判別力優於 BCLC（AUC ~0.84 vs 0.80）；把一部分 BCLC B/C 病人劃入積極治療：BCLC-B 中被 HKLC 歸為 II 者，根治性治療 5 年存活 **52.1% vs TACE 18.7%**；BCLC-C 中 HKLC-II 者，根治性治療 5 年存活 48.6% vs 全身治療 0%（p<0.0001）——回溯、單中心、B 肝族群，未在西方驗證（作者自承）。
- **手術界的實況調查**：Torzilli 2013（東西方 10 個高量中心、2,046 位切除病人）[S21]：**36% 是 BCLC B、14% 是 BCLC C**——半數手術落在指引建議之外；5 年存活 BCLC 0-A 61%、**B 57%**、C 38%；90 天死亡率 2.7%。作者結論：現行實務廣泛超出 EASL/AASLD 建議，「justifying an update of the guidelines in this sense」。
- **超出 Milan 的多顆可切除肝癌，隨機試驗**：Yin 2014（中國單中心 RCT，n=173，可切除多顆、超出 Milan）[S22]：切除 vs TACE，3 年 OS **51.5% vs 18.1%**（HR 0.434，p<0.001）——中國、B 肝為主、單中心，不能外推成「B 期都該開」。
- **APASL 2017 的亞洲立場（OA 原文）**[S6]：「in Asian countries where locoregional treatments are the mainstay strategy for HCC, LT is not recommended for Child–Pugh class A patients」；切除端：「when restricted to Child–Pugh class A patients within the Milan criteria, the 5-year survival rate reaches above 70%」；對 Child-Pugh 的批評：「it provides too rough an estimate to allow accurate quantitative evaluation of the liver functional reserve」。
- **台灣官方共識也把 B 期寫成光譜**：TLCA 2025 中期肝癌共識（OA 全文核對）[S5]，Statement 1（同意度 100%）：「Intermediate-stage (BCLC B) HCC is a **heterogeneous** group, and treatment should be tailored based on tumor burden and liver reserve」；「**curative-intent options, including surgical resection, local ablation, or liver transplantation under extended criteria, may be feasible for select individuals** with intermediate-stage HCC and limited tumor burden」；up-to-7／up-to-11 作為 TACE 適合性分界（超過 up-to-11 強烈不建議 TACE）[S5]。

**實務怎麼分歧（全球流行病學）**

- BRIDGE 研究（14 國 42 中心、18,031 人，2005–2012 診斷）[S23]：**台灣（n=1,587）與日本最常在 BCLC 0/A 期診斷（約七成在 0/A）**，北美/歐洲/中國/韓國最常見診斷期別是 C；**台灣的第一線治療最常見是切除**（北美/歐洲/中國/韓國是 TACE、日本是 RFA/PEI）；台灣中位存活未達（censoring 與 lead-time 使此數不可比，作者自承）。**限制：台灣資料來自單一中心**（作者聲明選點具代表性，仍要標）[S23]。

**SBRT 措辭光譜（跨組）**

- 依 SPEC §八修正 4：BCLC/AASLD/APASL/台灣共識對 SBRT 的原文措辭**引 B brief [S13][S15][S18][S20][S21]**，ESMO 2025 取不到（B 之 FAIL-2）→寫「取不到原文，不引用」。A3 只用一句話把讀者指到 B1/B2 的深度。

### Claim ceiling

- 可寫：「BCLC 是預後分期＋第一線建議的地圖，2022 版自己寫明：最終決定屬於醫師與多專科團隊，不是那張圖」；「BCLC 自己內建了『治療期別轉移』：同一格的病人可以正當地被建議用『更晚期那格』的治療」；「B 期是光譜不是一格——這句話 BCLC、國際專家小組、台灣肝癌醫學會共識（同意度 100%）都說過」；「亞洲高量中心一半的切除手術落在指引建議之外，B 期切除 5 年存活 57%（回溯、選擇過的病人）」；「一個超出 Milan 的可切除多顆肝癌隨機試驗：切除 3 年存活 51.5%、TACE 18.1%（中國、B 肝為主）」；「台灣病人七成在早期被診斷、第一線最常見是切除（跨國登錄、台灣為單一中心）」。
- **不可寫**：「BCLC 過時／錯誤」（批評對象是「把圖當判決」的讀法，不是分期本身——它的預後分層沒有爭議[S7]）；「B 期應該開刀」（證據是「部分經選擇的 B 期病人」）；「HKLC 比 BCLC 好」（判別力數字限香港 B 肝族群、未在西方驗證）；「台灣存活全球最好」（BRIDGE 的台灣中位存活未達是統計 artefact，作者自己說不可靠）；不可轉述 BCLC 2026 或 ESMO 2025 的內文。
- SBRT 在各指引的位階：本篇一句話＋指向 B 組，不重寫（修正 4）。

### Caveats

- Torzilli、Yau、BRIDGE 全是回溯／登錄資料；Yin 是單中心 RCT。每次引用帶「病因＋地區＋研究設計」三標籤。
- 「分期表沒說的」第二層：分期在治療後會重算（BCLC 2022 的 BCLCp-B 概念、進展型態預後不同[S7]）——可作收尾材料。
- 台灣讀者的實際落點：TLCA 2025 的 up-to-7/up-to-11 是台灣醫師實際用的語言[S5]，寫進正文比只寫 Bolondi 有用。

### 台灣現況

- TLCA 2023[S4] 與 TLCA 2025 中期共識[S5] 都是 OA、可逐字引用的台灣官方共識。多專科團隊在台灣的制度面（癌症診療品質認證）歸 A5 寫，本篇一句話。

---

## A4 `lv-hepatitis`〈B 肝 C 肝：抗病毒藥這時候更重要〉

### Key facts

**B 肝：抗病毒藥降低復發與死亡（三個層級）**

- **台灣全國資料**：Wu 2012（JAMA；台灣健保資料庫，100,938 位肝癌病人中取 4,569 位 B 肝相關、根治性切除）[S24]：服核苷酸類似物組復發 20.5% vs 未服 43.6%；校正競爭死因後 6 年復發 45.6% vs 54.6%、6 年總死亡 29.0% vs 42.4%；**復發 HR 0.67**（95% CI 0.55–0.81）。回溯、給藥組肝硬化比例反而較高（48.6% vs 38.7%）——偏差方向對主張有利，可寫。
- **隨機試驗**：Huang 2015（Ann Surg RCT，n=200，HBV 相關肝癌 R0 切除後，adefovir vs 無）[S25]：5 年 RFS 46.1% vs 27.1%、**5 年 OS 63.1% vs 41.5%**；死亡 RR 0.42（95% CI 0.27–0.65）；主要作用在晚期復發（HR 0.35）。
- **連低病毒量都有效**：Huang 2018（Ann Surg RCT，n=200，術前 HBV-DNA 低者）[S26]：5 年 RFS 52.0% vs 32.3%、5 年 OS 64.1% vs 43.7%（皆顯著）——「病毒量低就不用吃」不成立（中國族群、單中心）。

**B 肝再活化：為什麼治療期間更不能斷（不可自行中斷紅線的證據本體，D3 共用）**

- 概念與嚴重度（綜述）：Loomba & Liang 2017（Gastroenterology）[S29]：免疫抑制／癌症治療相關 HBV 再活化是「important cause of morbidity and mortality」，從無症狀到猛爆性肝炎、肝衰竭。
- **TACE 的隨機證據**：Jang 2006（Hepatology RCT，n=73，HBsAg+ 肝癌接受動脈化療栓塞）[S27]：**未預防投藥組 29.7% 發生再活化肝炎 vs 預防性 lamivudine 組 2.8%**（p=0.002），重度肝炎也較多；HBV DNA >10⁴ copies/mL 是獨立預測因子。
- **放射治療**：Jun 2018（韓國多中心回溯，133 位 HBsAg+ 肝癌接受 RT）[S28]：整體再活化 12.7%；**未用抗病毒者 33.3% vs 有用者 7.5%**（p<0.001）；B 肝相關肝炎 14.8% vs 3.8%；無抗病毒治療 OR 8.34、RT 合併 TACE OR 5.31。→ 這條紅線同樣適用於放射腫瘤科自己的療程，作者可用第一人稱寫。
- **「醫師監督下停藥」都有死亡風險，何況自行停**：RETRACT-B（Gastroenterology 2022；1,552 位「經挑選、HBeAg 陰性、非肝硬化為主、有監測」的慢性 B 肝停用 NA）[S30]：停藥後仍有肝失代償（發生率 0.48/1000 人年，**19 位失代償中 7 位死亡**）；作者結論最佳停藥候選人是「病毒抑制、HBeAg 陰性、**非肝硬化**、HBsAg 低」且需嚴密監測——肝癌＋肝硬化病人不在此列。寫法：「連在試驗條件下挑過的病人都有人因停藥失代償死亡；肝癌病人的停藥不是病人可以自己做的決定」。
- 台灣官方文件對停藥標準的轉述（2017-01-01 起之給付規定：HBeAg 陽性治療至轉陰後鞏固 1 年；陰性者至少 2 年＋三次測不到病毒；復發可再治療、不限次數）[S41]——證明「什麼時候能停」是有明文規則、由醫師依檢驗判定的事。

**C 肝 DAA 與肝癌：虛驚與結案（依 ⚠3 的弧線寫）**

- 警訊：Reig 2016（西班牙 4 中心，58 位根治後 HCC 接受 DAA）[S31]：中位 5.7 個月內復發 27.6%——作者自稱「note of caution」、樣本很小。
- 統合：Waziry 2017（41 篇、13,875 人，J Hepatol）[S32]：校正追蹤時間與年齡後，DAA vs 干擾素時代，發生 RR 0.68（p=0.55）、復發 RR 0.62（p=0.56）——「no evidence for differential HCC occurrence or recurrence risk」。
- 北美世代：Singal 2019 兩篇（31 中心，793/797 位根治後 HCV-HCC）[S33][S34]：復發 HR 0.90（0.70–1.16）、復發型態無差；**死亡 HR 0.54（0.33–0.90），達 SVR 者 HR 0.29**、未達 SVR 者無益（HR 1.13）。
- 收尾句（AASLD 2023 原文）[S1]：「two large multicenter studies from North America and Italy confirmed that eradication of HCV with direct-acting antiviral therapy does not increase risk of HCC recurrence and improves survival.」＋通則：「Antiviral treatment significantly decreases HCC risk in patients with and without cirrhosis from HBV or HCV infection」「Antivirals should be given in all patients who meet criteria for treatment according to AASLD Guidance documents.」
- 誠實提醒（AASLD 原文）：SVR 後肝癌風險降低但**肝硬化者風險不歸零**，肝硬化者治癒後仍要終身監測[S1]——接 D1/D3。

**台灣現況（本篇主場；出處＝官方計畫文件[S41]，抓取路徑見來源）**

- **B 肝抗病毒健保給付、肝癌條款**：「自2019年2月1日起增列肝癌並接受根除性治療且 HBV DNA≧2000 IU/mL，可長期使用 B 型肝炎口服治療藥品，直至肝癌復發且未能再次接受根除性治療止」[S41]。另 2021-03-01 起放寬給付範圍、2023-10-01 起 e 抗原陰性者條件再放寬（ALT≥2 倍改 1 次即可、纖維化 ≥F3 放寬為 ≥F2）[S41]。**給付規定逐條原文取不到（FAIL-3）**——涵蓋外情境寫「與醫療團隊確認」。
- **C 肝口服新藥（DAA）**：2017-01-24 起納入健保給付；2017–2024 編列 C 肝治療預算 428.12 億元[S41]。
- **公費 BC 肝篩檢現況（2026-08-30 有效）**：2011-08-01 起成人預防保健提供 1966 年後出生滿 45 歲終身一次；**2020-09-28 調整為 45–79 歲成人（原住民 40–79 歲）終身一次**，不需搭配成人健檢；2022-03 起擴大到成健特約機構所有專科醫師可執行；2024 年起每案補助 200→370 元；截至 2024-09，45–79 歲曾接受 C 肝篩檢者 689 萬人[S41]。
- **肝癌監測（腹超）**：見 ⚠1——無全國性公費肝癌超音波篩檢；官方路徑是篩檢陽性→轉介健保院所→「B 型肝炎帶原者及 C 型肝炎感染者醫療給付改善方案」（2010 年起）個管追蹤[S41]；追蹤中的超音波屬健保醫療，不是篩檢政策。PIVKA-II 給付限「肝硬化之慢性肝炎（含酒精性）及肝癌接受根除治療之患者」（計畫文件自述之限制）[S41]。
- 治療規模（截至 2025-05）：健保 B 肝治療約 36.1 萬人、C 肝約 17.8 萬人[S41]。

### Claim ceiling

- 可寫：「B 肝相關肝癌切除後吃抗病毒藥：台灣全國資料復發風險降三分之一（HR 0.67）、隨機試驗 5 年存活 63% vs 42%」；「病毒量低也一樣有隨機試驗證據」；「癌症治療會喚醒 B 肝病毒：TACE 未預防投藥者三成再活化（RCT）、放射治療未用抗病毒者三成三（回溯）——所以治療期間抗病毒藥是保命裝備，不是可有可無」;「自行停藥的風險：連醫師監督下的計畫性停藥都有失代償死亡個案（國際世代）」；「C 肝治好不會讓肝癌復發變多——2016 年的警訊研究已被統合分析與大型世代推翻，且治癒者死亡風險約減半（北美世代 HR 0.54）」；「台灣健保 2019 年起明文給付根除性治療後的肝癌病人長期用 B 肝口服藥（官方計畫文件轉述）」。
- **不可寫**：「DAA 完全安全無虞」（要把 Reig 的存在與其後續寫出來——誠實勝過乾淨）；「治好 C 肝就不會得肝癌」（肝硬化者風險不歸零[S1]）；「所有肝癌病人 B 肝藥都有健保給付」（查證到的條款限「根除性治療後＋HBV DNA≥2000」；其餘寫確認）；「B 肝可以治癒」；不可把 [S28]（回溯）寫成隨機證據。
- 「不可自行中斷」的警語句是本篇與 D3 的共同紅線：本篇給證據，D3 給長期照護——不重複展開。

### Caveats

- Huang 兩個 RCT 都是中國單中心、adefovir 年代——方向可信、藥物已換代（現行為 entecavir/tenofovir），寫「現在用的藥更強」但不比較品牌。
- Jang 2006 的化療栓塞是 chemo-lipiodolization（含全身性化療成分），與台灣常規 TACE 不完全等同——標註。
- Waziry 統合中 DAA 組追蹤明顯較短（1.0 vs 5.5 年）——這正是為什麼要校正、也是初期恐慌的來源，可用來教「粗率比較會騙人」。
- 45–79 篩檢的 689 萬人是「C 肝篩檢」累計數；B 肝數字未在同段——不要合併成一個數。

### 台灣現況

（已併入 Key facts 台灣段；來源路徑見 [S41]。）

---

## A5 `lv-first-month`〈確診之後的第一個月〉

### Key facts

**科別分工（citable 錨點）**

- TLCA 2023 共識的作者組成（原文）[S4]：「The guidelines were updated by two teams comprising experts from various fields, including **epidemiology, hepatology, surgery, medical oncology, radiation oncology, and diagnostic and interventional radiology**」；診斷組 7 人（流病＋影像）、全身治療組 22 人（肝膽、外科、腫內、放腫、介入影像）——台灣肝癌照護的科別地圖，官方共識自己寫的。
- 誰先接手影響預後（美國 VA，n=3,988）[S36]：診斷 30 天內看過肝膽專科（HR 0.70）、腫瘤內科（HR 0.82）、外科（HR 0.79）與經多專科腫瘤會議討論（HR 0.83）皆與較低死亡相關；學術醫院（OR 1.97）與多專科評估（OR 1.60）與較高「接受積極治療」機率相關——回溯、關聯非因果。

**多專科團隊（MDT）的證據與誠實**

- 統合分析：Seif El Dahan 2023（12 篇、15,365 位 HCC）[S35]：MDT 與較佳存活相關（**HR 0.63**，95% CI 0.45–0.88）；但「接受根治治療」未達顯著（RR 1.60，CI 跨 1）、異質性極高（I²>90%）、且 MDT 組較早期（RR 1.60）——作者自己點名**轉診偏差**可能貢獻了存活差。誠實寫法：「方向一致、但這種研究天生無法排除『被送進 MDT 的人本來就不一樣』」。
- 單中心前後比較：Yopp 2014（美國安全網醫院，355 人）[S37]：MDT 成立後更早期診斷（BCLC A 44% vs 26%）、**診斷到治療中位時間 2.3 vs 5.3 個月**、校正後存活較佳。

**時間該多快：證據的兩面（小心 confounding，SPEC 原註）**

- 真實世界的節奏（美國 NCDB，2017–2020，23,922 人）[S38]：**診斷到第一線治療的中位時間約 49–51 天**；手術 41 天、消融 52–55 天、全身治療 42–47 天、放射 60–62 天。可拿來回答「等一個月正常嗎」。
- 等待與結果：Brahmania 2017（多倫多，219 位早期 HCC 接受根治性 RFA）[S43]：診斷到 RFA 中位 96 天；**每多等 30 天，殘留腫瘤風險 +9%、死亡風險 +23%**（多變項）——回溯、單中心，適應症干擾不可排除（等比較久的人可能病情本來不同）；不可據此發明「必須 X 週內」的門檻，寫成「不要無故拖、也不必為了搶快跳過該做的評估」。
- （MDT 使時間縮短的實例即 [S37] 的 2.3 vs 5.3 個月。）

**第一個月的檢查各自決定什麼（交叉引用地圖，不重寫）**

- 動態影像（CT/MRI）→確診與範圍（A1[S1][S4]）；肝功能組合（Child-Pugh/ALBI/失代償病史）→付得起哪種治療（A2[S13][S14]）；分期（BCLC/腫瘤負荷）→哪一格與哪些路（A3[S7]）；B/C 肝病毒學（HBsAg、HBV DNA、anti-HCV）→抗病毒與再活化預防（A4[S41][S27]）；胃鏡與血小板（門脈高壓）→影響手術與 atezo+bev 前提（指向 B/C 組，一句話）。

**台灣行政面（官方原文）**

- **重大傷病證明**：〈全民健康保險保險對象免自行負擔費用辦法〉（法規原文，2026-08-30 抓取）[S39]：重大傷病項目及有效期限依第二條附表一；申請檢附申請書＋**開立 30 日內有效之診斷證明書**（需填 ICD 碼）＋身分證明，可由本人、代理人或醫院代辦；保險人**14 日內（不含例假日）核定**；證明註記於健保卡。第 6 條免自行負擔範圍：證明所載傷病及**經診治醫師認定與該傷病相關之治療**；住院期間申請獲准者當次住院即免部分負擔。效期屆滿前 3 個月（效期 ≥2 年者）可申請展延銜接。附表一（114-01-01 起適用版）[S40]：**「除（一）–（四）之其他惡性腫瘤」（含肝癌 C22）證明有效期限五年**（例外三年者：甲狀腺癌、第一期口腔口咽下咽癌、第一期乳癌、第一期子宮頸癌）。
- **MDT 的制度面**：國健署「癌症診療品質」頁（2026-08-30 抓取）[S42]：引 WHO「以多專科醫療團隊的服務模式，依據實證醫學的標準來提供醫療服務」；2003 年《癌症防治法》通過、2005 年頒訂「癌症診療品質保證措施準則」；**2026 年計補助 100 家醫院辦理「全方位癌症防治策進計畫」**，涵蓋癌症登記、腫瘤個案管理、**癌症單一資源服務窗口**等健保未給付項目；頁面附「癌症診療品質認證醫院名單」PDF[S42]。→「個管師」在台灣是有政策預算的角色，不是各院自選配件；病人可查認證醫院名單。
- 移植登錄與等待歸 B4/D5（B brief 已查證 TORSC 動態頁取不到數字）；本篇不碰。

### Claim ceiling

- 可寫：「肝癌在台灣同時住在好幾科：肝膽腸胃、外科、腫瘤內科、放射腫瘤、影像與介入──台灣共識的作者名單本身就是這張地圖」；「多專科討論與較佳存活相關（統合 HR 0.63），但這類研究無法排除轉診偏差——即使如此，讓每一科都看過你的片子仍是合理要求」；「美國真實世界診斷到治療中位約 50 天；等待不是零成本（多倫多資料每 30 天死亡風險 +23%，回溯），但也沒有任何指引訂出『幾週內必須』的門檻」；「重大傷病：癌症診斷證明 30 日內有效、健保署 14 日內核定、肝癌效期五年、就醫該病免部分負擔（法規原文）」；「2026 年全台 100 家醫院有政策補助的癌症個管與單一窗口」。
- **不可寫**：「MDT 保證更好的結果」（關聯、異質性高、轉診偏差[S35]）；「越快治療越好，X 週內一定要開始」（[S43] 是回溯＋適應症干擾；NCDB 的 50 天是描述不是標準）；「重大傷病＝全部免費」（免的是「該傷病相關」的部分負擔，範圍在辦法第 6 條）；不可點名個別醫院（醫療法紅線）；認證醫院名單指向官方 PDF，不摘錄名單。
- 重大傷病與行政流程全系列由本篇寫完整（比照 colon SPEC 交叉引用慣例），其他篇一句話。

### Caveats

- [S36][S37] 是美國體系（VA／安全網醫院），制度細節不可平移，只取「哪些科、多快、有沒有一起看」的結構性結論。
- 台灣「第一個月實際節奏」（排程、住院天數）**查無官方可引數字**——寫成經驗描述（作者門診口吻）而非數據，或指向個管師。
- 45–79 BC 肝篩檢是「還沒確診的家人」的行動點（接 A4[S41]）——收尾「下次門診問出口的問題」可包含「我的家人要不要去做終身一次的公費篩檢」。

---

## 給 B/C/D 組的協調備註

- A2 建立肝功能名詞（Child-Pugh 五項、ALBI、MELD、失代償、競爭風險）——各組引用不重釋。
- A4 擁有「抗病毒不可自行中斷」的證據本體（[S27][S28][S29][S30]）與健保給付現況（[S41]）；D3 寫長期照護時引 A4 的結論句即可，數字不重列。
- A5 擁有重大傷病與 MDT 制度面（[S39][S40][S42]）；其他篇一句話。
- 45–79 公費篩檢與「無全國腹超政策」的形狀（⚠1）供 D1 追蹤篇沿用，出處同 [S41]。

---

## Sources（單一序列；PASS 才可入正文）

**指引與共識（引語以全文為準）**

- [S1] **PASS（全文引語經 NCBI PMC 全文核對，PMC10663390）** Singal AG, Llovet JM, Yarchoan M, et al. AASLD Practice Guidance on prevention, diagnosis, and treatment of hepatocellular carcinoma. *Hepatology*. 2023;78(6):1922–1965. DOI: 10.1097/HEP.0000000000000466. PMID 37199193. https://doi.org/10.1097/HEP.0000000000000466
- [S2] **PASS（僅書目；內文不可引，見 FAIL-4）** European Association for the Study of the Liver. EASL Clinical Practice Guidelines: Management of hepatocellular carcinoma. *J Hepatol*. 2018;69(1):182–236. DOI: 10.1016/j.jhep.2018.03.019. PMID 29628281. https://doi.org/10.1016/j.jhep.2018.03.019
- [S3] **PASS（僅書目；內文不可引，見 FAIL-1）** European Association for the Study of the Liver. EASL Clinical Practice Guidelines on the management of hepatocellular carcinoma. *J Hepatol*. 2025;82(2):315–374. DOI: 10.1016/j.jhep.2024.08.028. PMID 39690085. https://doi.org/10.1016/j.jhep.2024.08.028
- [S4] **PASS（OA，全文引語核對，PMC11493393）** Teng W, Wang HW, Lin SM; TLCA Diagnosis Group and Systemic Therapy Group. Management Consensus Guidelines for Hepatocellular Carcinoma: 2023 Update on Surveillance, Diagnosis, Systemic Treatment, and Posttreatment Monitoring by the Taiwan Liver Cancer Association and the Gastroenterological Society of Taiwan. *Liver Cancer*. 2024;13(5):468–486. DOI: 10.1159/000537686. PMID 39435274. https://doi.org/10.1159/000537686
- [S5] **PASS（OA，全文引語核對，PMC12538147）** Lee IC, Wang HW, Teng W, et al. Taiwan liver cancer association management consensus guidelines for intermediate-stage hepatocellular carcinoma. *Clin Mol Hepatol*. 2025;31(4):1213–1232. DOI: 10.3350/cmh.2025.0724. PMID 40755008. https://doi.org/10.3350/cmh.2025.0724
- [S6] **PASS（OA，全文引語核對，PMC5491694）** Omata M, Cheng AL, Kokudo N, et al. Asia-Pacific clinical practice guidelines on the management of hepatocellular carcinoma: a 2017 update. *Hepatol Int*. 2017;11(4):317–370. DOI: 10.1007/s12072-017-9799-9. PMID 28620797. https://doi.org/10.1007/s12072-017-9799-9
- [S7] **PASS（全文引語經 NCBI PMC 全文核對，PMC8866082）** Reig M, Forner A, Rimola J, et al. BCLC strategy for prognosis prediction and treatment recommendation: The 2022 update. *J Hepatol*. 2022;76(3):681–693. DOI: 10.1016/j.jhep.2021.11.018. PMID 34801630. https://doi.org/10.1016/j.jhep.2021.11.018
- [S8] **PASS（僅書目；內文不可引，見 FAIL-2）** Reig M, Sanduzzi-Zamparelli M, Forner A, et al. BCLC strategy for prognosis prediction and treatment recommendations: The 2026 update. *J Hepatol*. 2026;84(3):631–654. DOI: 10.1016/j.jhep.2025.10.020. PMID 41151697. https://doi.org/10.1016/j.jhep.2025.10.020

**A1 期刊（Europe PMC REST 核對，數字出自摘要）**

- [S9] **PASS** van der Pol CB, Lim CS, Sirlin CB, et al. Accuracy of the Liver Imaging Reporting and Data System in Computed Tomography and Magnetic Resonance Image Analysis of Hepatocellular Carcinoma or Overall Malignancy—A Systematic Review. *Gastroenterology*. 2019;156(4):976–986. DOI: 10.1053/j.gastro.2018.11.020. PMID 30445016. https://doi.org/10.1053/j.gastro.2018.11.020
- [S10] **PASS** Adamo RG, van der Pol CB, Alabousi M, et al. Diagnostic Performance of CT/MRI LI-RADS Version 2018 Major Feature Combinations: Individual Participant Data Meta-Analysis. *Radiology*. 2025;315(3):e243450. DOI: 10.1148/radiol.243450. PMID 40492918. https://doi.org/10.1148/radiol.243450
- [S11] **PASS** Goins SM, Jiang H, van der Pol CB, et al. Individual Participant Data Meta-Analysis of LR-5 in LI-RADS Version 2018 versus Revised LI-RADS for Hepatocellular Carcinoma Diagnosis. *Radiology*. 2023;309(3):e231656. DOI: 10.1148/radiol.231656. PMID 38112549. https://doi.org/10.1148/radiol.231656

**A2 期刊**

- [S12] **PASS（僅書目，無摘要；分項內容引 [S13]）** Pugh RN, Murray-Lyon IM, Dawson JL, Pietroni MC, Williams R. Transection of the oesophagus for bleeding oesophageal varices. *Br J Surg*. 1973;60(8):646–649. DOI: 10.1002/bjs.1800600817. PMID 4541913. https://doi.org/10.1002/bjs.1800600817
- [S13] **PASS（OA，全文引語核對，PMC8411239）** Demirtas CO, D'Alessio A, Rimassa L, Sharma R, Pinato DJ. ALBI grade: Evidence for an improved model for liver functional estimation in patients with hepatocellular carcinoma. *JHEP Rep*. 2021;3(5):100347. DOI: 10.1016/j.jhepr.2021.100347. PMID 34505035. https://doi.org/10.1016/j.jhepr.2021.100347
- [S14] **PASS** Johnson PJ, Berhane S, Kagebayashi C, et al. Assessment of liver function in patients with hepatocellular carcinoma: a new evidence-based approach—the ALBI grade. *J Clin Oncol*. 2015;33(6):550–558. DOI: 10.1200/JCO.2014.57.9151. PMID 25512453. https://doi.org/10.1200/JCO.2014.57.9151
- [S15] **PASS** Kamath PS, Wiesner RH, Malinchoc M, et al. A model to predict survival in patients with end-stage liver disease. *Hepatology*. 2001;33(2):464–470. DOI: 10.1053/jhep.2001.22172. PMID 11172350. https://doi.org/10.1053/jhep.2001.22172
- [S16] **PASS** D'Amico G, Pasta L, Morabito A, et al. Competing risks and prognostic stages of cirrhosis: a 25-year inception cohort study of 494 patients. *Aliment Pharmacol Ther*. 2014;39(10):1180–1193. DOI: 10.1111/apt.12721. PMID 24654740. https://doi.org/10.1111/apt.12721
- [S17] **PASS（僅書目；轉述數字不可引，見 FAIL-8）** D'Amico G, Garcia-Tsao G, Pagliaro L. Natural history and prognostic indicators of survival in cirrhosis: a systematic review of 118 studies. *J Hepatol*. 2006;44(1):217–231. DOI: 10.1016/j.jhep.2005.10.013. PMID 16298014. https://doi.org/10.1016/j.jhep.2005.10.013
- [S18] **PASS** Cabibbo G, Petta S, Barbara M, et al; ITA.LI.CA group. Hepatic decompensation is the major driver of death in HCV-infected cirrhotic patients with successfully treated early hepatocellular carcinoma. *J Hepatol*. 2017;67(1):65–71. DOI: 10.1016/j.jhep.2017.01.033. PMID 28192185. https://doi.org/10.1016/j.jhep.2017.01.033

**A3 期刊**

- [S19] **PASS** Bolondi L, Burroughs A, Dufour JF, et al. Heterogeneity of patients with intermediate (BCLC B) hepatocellular carcinoma: proposal for a subclassification to facilitate treatment decisions. *Semin Liver Dis*. 2012;32(4):348–359. DOI: 10.1055/s-0032-1329906. PMID 23397536. https://doi.org/10.1055/s-0032-1329906
- [S20] **PASS** Yau T, Tang VY, Yao TJ, Fan ST, Lo CM, Poon RT. Development of Hong Kong Liver Cancer staging system with treatment stratification for patients with hepatocellular carcinoma. *Gastroenterology*. 2014;146(7):1691–1700.e3. DOI: 10.1053/j.gastro.2014.02.032. PMID 24583061. https://doi.org/10.1053/j.gastro.2014.02.032
- [S21] **PASS** Torzilli G, Belghiti J, Kokudo N, et al. A snapshot of the effective indications and results of surgery for hepatocellular carcinoma in tertiary referral centers: is it adherent to the EASL/AASLD recommendations? An observational study of the HCC East-West Study Group. *Ann Surg*. 2013;257(5):929–937. DOI: 10.1097/SLA.0b013e31828329b8. PMID 23426336. https://doi.org/10.1097/SLA.0b013e31828329b8
- [S22] **PASS** Yin L, Li H, Li AJ, et al. Partial hepatectomy vs. transcatheter arterial chemoembolization for resectable multiple hepatocellular carcinoma beyond Milan Criteria: a RCT. *J Hepatol*. 2014;61(1):82–88. DOI: 10.1016/j.jhep.2014.03.012. PMID 24650695. https://doi.org/10.1016/j.jhep.2014.03.012
- [S23] **PASS（OA，全文引語核對，PMC4691343）** Park JW, Chen M, Colombo M, et al. Global patterns of hepatocellular carcinoma management from diagnosis to death: the BRIDGE Study. *Liver Int*. 2015;35(9):2155–2166. DOI: 10.1111/liv.12818. PMID 25752327. https://doi.org/10.1111/liv.12818

**A4 期刊**

- [S24] **PASS** Wu CY, Chen YJ, Ho HJ, et al. Association between nucleoside analogues and risk of hepatitis B virus-related hepatocellular carcinoma recurrence following liver resection. *JAMA*. 2012;308(18):1906–1914. DOI: 10.1001/2012.jama.11975. PMID 23162861. https://doi.org/10.1001/2012.jama.11975
- [S25] **PASS** Huang G, Lau WY, Wang ZG, et al. Antiviral therapy improves postoperative survival in patients with hepatocellular carcinoma: a randomized controlled trial. *Ann Surg*. 2015;261(1):56–66. DOI: 10.1097/SLA.0000000000000858. PMID 25072444. https://doi.org/10.1097/SLA.0000000000000858
- [S26] **PASS** Huang G, Li PP, Lau WY, et al. Antiviral Therapy Reduces Hepatocellular Carcinoma Recurrence in Patients With Low HBV-DNA Levels: A Randomized Controlled Trial. *Ann Surg*. 2018;268(6):943–954. DOI: 10.1097/SLA.0000000000002727. PMID 29521740. https://doi.org/10.1097/SLA.0000000000002727
- [S27] **PASS** Jang JW, Choi JY, Bae SH, et al. A randomized controlled study of preemptive lamivudine in patients receiving transarterial chemo-lipiodolization. *Hepatology*. 2006;43(2):233–240. DOI: 10.1002/hep.21024. PMID 16440357. https://doi.org/10.1002/hep.21024
- [S28] **PASS（OA）** Jun BG, Kim YD, Kim SG, et al. Hepatitis B virus reactivation after radiotherapy for hepatocellular carcinoma and efficacy of antiviral treatment: A multicenter study. *PLoS One*. 2018;13(7):e0201316. DOI: 10.1371/journal.pone.0201316. PMID 30059513. https://doi.org/10.1371/journal.pone.0201316
- [S29] **PASS** Loomba R, Liang TJ. Hepatitis B Reactivation Associated With Immune Suppressive and Biological Modifier Therapies: Current Concepts, Management Strategies, and Future Directions. *Gastroenterology*. 2017;152(6):1297–1309. DOI: 10.1053/j.gastro.2017.02.009. PMID 28219691. https://doi.org/10.1053/j.gastro.2017.02.009
- [S30] **PASS** Hirode G, Choi HSJ, Chen CH, et al; RETRACT-B Study Group. Off-Therapy Response After Nucleos(t)ide Analogue Withdrawal in Patients With Chronic Hepatitis B: An International, Multicenter, Multiethnic Cohort (RETRACT-B Study). *Gastroenterology*. 2022;162(3):757–771.e4. DOI: 10.1053/j.gastro.2021.11.002. PMID 34762906. https://doi.org/10.1053/j.gastro.2021.11.002
- [S31] **PASS** Reig M, Mariño Z, Perelló C, et al. Unexpected high rate of early tumor recurrence in patients with HCV-related HCC undergoing interferon-free therapy. *J Hepatol*. 2016;65(4):719–726. DOI: 10.1016/j.jhep.2016.04.008. PMID 27084592. https://doi.org/10.1016/j.jhep.2016.04.008
- [S32] **PASS** Waziry R, Hajarizadeh B, Grebely J, et al. Hepatocellular carcinoma risk following direct-acting antiviral HCV therapy: A systematic review, meta-analyses, and meta-regression. *J Hepatol*. 2017;67(6):1204–1212. DOI: 10.1016/j.jhep.2017.07.025. PMID 28802876. https://doi.org/10.1016/j.jhep.2017.07.025
- [S33] **PASS** Singal AG, Rich NE, Mehta N, et al. Direct-Acting Antiviral Therapy Not Associated With Recurrence of Hepatocellular Carcinoma in a Multicenter North American Cohort Study. *Gastroenterology*. 2019;156(6):1683–1692.e1. DOI: 10.1053/j.gastro.2019.01.027. PMID 30660729. https://doi.org/10.1053/j.gastro.2019.01.027
- [S34] **PASS** Singal AG, Rich NE, Mehta N, et al. Direct-Acting Antiviral Therapy for Hepatitis C Virus Infection Is Associated With Increased Survival in Patients With a History of Hepatocellular Carcinoma. *Gastroenterology*. 2019;157(5):1253–1263.e2. DOI: 10.1053/j.gastro.2019.07.040. PMID 31374215. https://doi.org/10.1053/j.gastro.2019.07.040

**A5 期刊**

- [S35] **PASS（OA）** Seif El Dahan K, Reczek A, Daher D, et al. Multidisciplinary care for patients with HCC: a systematic review and meta-analysis. *Hepatol Commun*. 2023;7(5):e0143. DOI: 10.1097/HC9.0000000000000143. PMID 37102768. https://doi.org/10.1097/HC9.0000000000000143
- [S36] **PASS** Serper M, Taddei TH, Mehta R, et al; VOCAL Study Group. Association of Provider Specialty and Multidisciplinary Care With Hepatocellular Carcinoma Treatment and Mortality. *Gastroenterology*. 2017;152(8):1954–1964. DOI: 10.1053/j.gastro.2017.02.040. PMID 28283421. https://doi.org/10.1053/j.gastro.2017.02.040
- [S37] **PASS** Yopp AC, Mansour JC, Beg MS, et al. Establishment of a multidisciplinary hepatocellular carcinoma clinic is associated with improved clinical outcome. *Ann Surg Oncol*. 2014;21(4):1287–1295. DOI: 10.1245/s10434-013-3413-8. PMID 24318095. https://doi.org/10.1245/s10434-013-3413-8
- [S38] **PASS（OA）** Rasic G, Beaulieu-Jones BR, Chung SH, et al. The Impact of the COVID-19 Pandemic on Hepatocellular Carcinoma Time to Treatment Initiation: A National Cancer Database Study. *Ann Surg Oncol*. 2023;30(7):4249–4259. DOI: 10.1245/s10434-023-13468-6. PMID 37099088. https://doi.org/10.1245/s10434-023-13468-6 （正文引其 Pre-COVID 中位 TTI 51 天／各治療別數字）
- [S43] **PASS** Brahmania M, Ahmed O, Kelley M, et al. Wait Time for Curative Intent Radio Frequency Ablation is Associated with Increased Mortality in Patients with Early Stage Hepatocellular Carcinoma. *Ann Hepatol*. 2017;16(5):765–771. DOI: 10.5604/01.3001.0010.2776. PMID 28809734. https://doi.org/10.5604/01.3001.0010.2776

**官方頁面／文件（實際抓取，取得日 2026-08-30；抓取路徑逐條註明）**

- [S39] **PASS** 〈全民健康保險保險對象免自行負擔費用辦法〉全文（重大傷病定義、申請程序、14 日核定、第 6 條免部分負擔範圍）。法務部全國法規資料庫，pcode=L0060015。抓取路徑：law.moj.gov.tw 直接 GET（偶發連線中斷，重試成功）。https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=L0060015
- [S40] **PASS** 同辦法第二條**附表一「全民健康保險重大傷病項目及其證明有效期限」**（PDF，含 113-12-31 前與 114-01-01 起兩版；114 版：「(五)除(一)-(四)之其他惡性腫瘤 五年」，C00.0–C96.9）。抓取路徑：law.moj.gov.tw 附件下載（LawGetFile，首次回 Error 頁、重試取得 433KB PDF，pdftotext 核對）。https://law.moj.gov.tw/LawClass/LawGetFile.ashx?FileId=0000375263&lan=C
- [S41] **PASS** 衛生福利部國民健康署〈國家肝炎及肝癌防治計畫（2026-2030年）〉（70 頁 PDF，行政院核定計畫；本 brief 引用之原文段落均經 pdftotext 逐字核對：45–79 歲終身一次 BC 肝篩檢沿革與 2020-09-28 調整、2024 年補助 370 元、689 萬人、B 肝 2017 停藥標準、**2019-02-01 肝癌根除性治療後長期給付條款**、2021-03-01／2023-10-01 放寬、C 肝 DAA 2017-01-24 納入給付與 428.12 億預算、B 肝治療 36.1 萬／C 肝 17.8 萬人、早期診斷 40.4% vs 日本 62%、PIVKA-II 給付限制、2010 年起 B/C 肝醫療給付改善方案）。頁面：https://www.hpa.gov.tw/Pages/Detail.aspx?nodeid=616&pid=19687 ；PDF：https://www.hpa.gov.tw/Pages/ashx/GetFile.ashx?lang=c&type=1&sid=1621363c04fa4c1ea0a5e515f47c321f 。抓取路徑：hpa.gov.tw 伺服器 TLS 憑證鏈不完整（缺 TWCA 中繼憑證），以憑證 AIA 指向之官方中繼憑證（http://sslserver.twca.com.tw/cacert/secure_sha2_2023G3.crt）補齊後正常驗證抓取；一般瀏覽器讀者不受影響。
- [S42] **PASS** 衛生福利部國民健康署「癌症診療品質」頁（WHO 多專科團隊引文、2003 癌症防治法、2005 癌症診療品質保證措施準則、2026 年補助 100 家醫院「全方位癌症防治策進計畫」、癌症登記／腫瘤個案管理／癌症單一資源服務窗口；附「癌症診療品質認證醫院名單」PDF 連結）。https://www.hpa.gov.tw/Pages/List.aspx?nodeid=208 （名單 PDF：https://www.hpa.gov.tw/Pages/ashx/GetFile.ashx?lang=c&type=2&sid=0423b100cbdb44f2a697380318c3570a ）。抓取路徑同 [S41]。
- 補充（指路用，不入正文引註）：國健署「肝病防治及肝癌」專區 https://www.hpa.gov.tw/Pages/List.aspx?nodeid=207

**FAIL ／ NOT-CITABLE（保留紀錄，不得入正文引用）**

- [FAIL-1] **EASL 2025 指引（[S3]）內文措辭**：journal-of-hepatology.eu 全文頁 403、無 PMC、無 OA 副本。診斷準則的歐洲版原文不可引；正文寫「我取不到可公開引用的版本」。
- [FAIL-2] **BCLC 2026 更新版（[S8]）內文**：付費牆（同 B brief FAIL-1 的查證結果，2026-08-30 再確認書目存在）。A3 只可引「2026 年更新版已出版」的書目事實。
- [FAIL-3] **nhi.gov.tw 所有 HTML 頁面**（重大傷病專區、藥品給付規定專區、就醫權益頁）：Cloudflare「Just a moment…」403，多組 UA／header 無效（直接 PDF 連結可通，但給付規定 PDF 的網址無法在站外發現；一般搜尋引擎 DuckDuckGo/Bing/Google/Mojeek/Brave 對本環境全部擋爬或回假頁，web.archive.org 遭 egress policy 封鎖）。**替代驗證**：重大傷病改以法規資料庫原文 [S39][S40]；B 肝給付肝癌條款改引官方計畫文件轉述 [S41]。**藥品給付規定逐條原文＝gap**，正文涉及未轉述之給付細節一律寫「向個管師／醫務課確認」。
- [FAIL-4] **EASL 2018（[S2]）內文措辭**：付費牆、無 PMC。僅書目。
- [FAIL-5] **全國性「肝癌腹部超音波篩檢」政策**：hpa.gov.tw 肝病防治專區與 2026-2030 國家計畫遍查無此項目——不存在（見 ⚠1），非查證失敗；正文不得寫「政府提供肝癌超音波篩檢」，改寫官方實際路徑（45–79 BC 肝篩檢＋醫療端追蹤）。
- [FAIL-6] **hpa.gov.tw TLS 憑證鏈不完整**：程序註記（見 [S41] 抓取路徑），不影響引用效力。
- [FAIL-7] **台灣「確診到治療」在地時程數字**：查無官方或可引用學術數字。A5 用美國 NCDB [S38] 標明地區，台灣節奏寫成門診經驗描述。
- [FAIL-8] **D'Amico 2006 的「代償中位存活 >12 年 vs 失代償約 2 年」轉述數字**：原文無摘要、無 OA 全文可核對——不可引用；失代償預後數字一律用 D'Amico 2014 [S16]。

---

## 給撰稿人的一句話總結

A 組查證後整體比 SPEC 假設更硬：A1 的「不切片」有 AASLD 強建議原文＋台灣共識逐字句（Statement 2-3）雙錨，且拿到誠實的反面數字（LR-5 敏感度僅 61.3%——影像是「說是就幾乎是」，不是「說不是就不是」）；A2 的地基材料全部到位（五項目、A/B/C 兩年存活 85/60/35%、失代償五階梯 1.5%→88%、失代償 HR 7.52 vs 復發 2.50 的競爭風險本體）；A3 的批評每一條都有可引原文，包括 BCLC 自己的「不能只看那張圖」與台灣共識 100% 同意度的「B 期是異質群」；A4 是本組最強的一篇——抗病毒有台灣全國資料＋兩個 RCT，再活化有 TACE 的 RCT（29.7% vs 2.8%）與 RT 的多中心資料（33.3% vs 7.5%），DAA 虛驚有完整的「警訊→統合→世代→指引結案」弧線，健保肝癌條款有官方計畫文件逐字轉述。兩個要小心的形狀：NHI 網站全面擋爬，藥品給付規定逐條原文是 gap（已用法規資料庫與國家計畫文件補位）；「肝癌腹超篩檢政策」不存在，官方路徑是 45–79 終身一次 BC 肝篩檢＋醫療端個管追蹤，D1 寫追蹤時照這個形狀。最薄的一篇是 A5 的「台灣第一個月實際節奏」——重大傷病與 MDT 制度面拿到法規／官方頁原文，但排程時間數字只有美國資料，台灣端要靠作者門診口吻補。
