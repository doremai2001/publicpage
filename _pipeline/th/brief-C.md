# C 組（放射碘，C1 th-rai-whether／C2 th-rai-days）查證 brief

查證日：2026-09-14　查證者：C 組
主要路徑：Europe PMC REST（search / fullTextXML）、clinicaltrials.gov API v2、isrctn.com WHO-format API、pmc.ncbi.nlm.nih.gov 全文、law.moj.gov.tw、erss.nusc.gov.tw（核安會主管法規共用系統）

---

## ⚠ 與 SPEC 假設不同形狀的事

### ⚠C-1　ATA 已有 2025 年新版指引，SPEC 的「暫以 2015 版為準」必須整批改寫

- **SPEC 怎麼假設**：§六 待研究確認第一條「ATA 指引是否已有 2015 之後的新版（本 SPEC 暫以 2015 版為準，**必須查證**）」。
- **實際是什麼**：有。`2025 American Thyroid Association Management Guidelines for Adult Patients with Differentiated Thyroid Cancer`，Thyroid 2025;35(8):841–985，另有 Executive Summary（Thyroid 2025;35(11):1214–1220）與一份 Corrigendum（Thyroid 2025;35(11):1350）。**書名也變了**：2015 版是「Thyroid Nodules **and** Differentiated Thyroid Cancer」，2025 版把甲狀腺結節拆出去，只管 DTC。
- **證據**：Europe PMC `EXT_ID:40844370` 回傳上述逐字標題與卷期頁；全文經 `https://pmc.ncbi.nlm.nih.gov/articles/PMC13090833/` 取得（HTTP 200，2,436,560 bytes），逐條建議與 GRADE 等級可逐字抄。
- **建議怎麼裁決**：全專題（不只 C 組）以 2025 ATA 為主指引，2015 版只在「講變化」時出現。**注意 Europe PMC 的 `fullTextXML` 對 PMC13090833 回 404**（它是 "Free" 而非 "Open access"），要抓全文只能走 pmc.ncbi.nlm.nih.gov 的 HTML。

### ⚠C-2　ATA 復發風險分層已經不是三級，是四級，而且帶了數字區間

- **SPEC／RESEARCH-COMMON 怎麼假設**：RESEARCH-COMMON §一.2 明寫「ATA **三級**復發風險分層」；SPEC A4 也照這個講。
- **實際是什麼**：2025 ATA Risk Stratification System 是**四格**，而且每格直接掛上復發機率：逐字為「categories are designated as **low (<10%), low-intermediate (10–15%), intermediate-high (≥16–30%), and high (>30%) risk of recurrence**」。指引自己也承認改動：「Previous ATA guidelines (2009 and 2015 versions) … recommended a three-tiered categorical system stratifying patients as low, intermediate, or high risk of structural disease persistence/recurrence.」
- **證據**：ATA 2025 全文，Clinical Management Principles 字彙段與 Recommendation 28 段落。
- **建議怎麼裁決**：改寫 RESEARCH-COMMON §一.2 與 SPEC A4／C1；C1 講「誰該做放射碘」時必須用四格講，**中間風險那一格已經被切成兩半，而且這兩半的放射碘建議在指引裡是同一句（見 ⚠C-8）**。另注意：這四個百分比是**結構性復發**的機率，不是死亡率，也不是期別。

### ⚠C-3　IoN 已經讀出來了，而且登錄系統跟論文對不起來

- **SPEC 怎麼假設**：§六「ESTIMABL2／IoN 的長期追蹤是否已讀出」寫成未知；SPEC §四 C1 把 IoN 跟其他三個試驗並列成「去階梯證據」。
- **實際是什麼**：**IoN 已於 2025 年 6 月在 Lancet 正式發表**：`Thyroidectomy with or without postoperative radioiodine for patients with low-risk differentiated thyroid cancer in the UK (IoN): a randomised, multicentre, non-inferiority trial.` Lancet 2025;406(10498):52–62（PMID 40543520）。
  - 但 **ClinicalTrials.gov NCT01398085 至今狀態仍是 `ACTIVE_NOT_RECRUITING`，primary completion 標 `2031-03 (ESTIMATED)`，且沒有 results section**（API v2 回傳的 JSON 內無 `resultsSection`）。
  - ISRCTN80416929 的 WHO-format 記錄則已把 `results_url_link` 指到該篇論文，`results_date_first_publication` = 24/06/2025，`results_date_completed` = 31/03/2031，`results_actual_enrolment` = 504，`target_size` = 570，`recruitment_status` = No longer recruiting。
  - 論文自述「is still in active follow-up」。
- **建議怎麼裁決**：C1 必須寫「IoN 已經發表五年結果，追蹤還沒結束」。**不可以只查 ClinicalTrials.gov 就說「尚未讀出」**——這正是本專題最容易出錯的一個點。

### ⚠C-4　「Martinique principles」的四個學會名單，任務書寫錯了

- **任務書怎麼假設**：寫成「joint ETA/EANM/**ESTRO**/SNMMI」。
- **實際是什麼**：逐字標題為 `Controversies, Consensus, and Collaboration in the Use of 131I Therapy in Differentiated Thyroid Cancer: A Joint Statement from the **American Thyroid Association**, the **European Association of Nuclear Medicine**, the **Society of Nuclear Medicine and Molecular Imaging**, and the **European Thyroid Association**.` Thyroid 2019;29(4):461–470。**ESTRO 不是簽署方；ATA 才是。**
- 起因逐字：「the European Association of Nuclear Medicine and the Society of Nuclear Medicine and Molecular Imaging **declined to endorse the ATA guidelines**」——這是 2015 ATA 指引核醫界不背書所引發的會議。
- **後續文件存在**：`Brief progress report from the intersocietal working group on differentiated thyroid cancer.` Eur J Nucl Med Mol Imaging 2020;47(6):1345–1347（PMC7188695，OA）。該文明講 2019 年第二次會議「the available evidence was found to be insufficient to provide any definitive guidance … we could not arrive at consensus opinions on these important topics」。**2020 年之後查無第三份 intersocietal 共識文件。**
- **建議怎麼裁決**：C1 若要提這段歷史，學會名單要照上面四個抄；不可寫成「四大學會達成共識」，2020 年那份說得很清楚是**沒有**達成共識。

### ⚠C-5　HiLo／ESTIMABL1 回答的不是「要不要做」，是「做的話用多少」——SPEC 把兩題綁在同一行

- **SPEC 怎麼假設**：§四 C1「ESTIMABL2／IoN／HiLo／ESTIMABL1 的去階梯證據」寫成一串。
- **實際是什麼**：這是**兩個不同的臨床問題**。
  - HiLo（NEJM 2012）與 ESTIMABL1（NEJM 2012）：**所有人都做放射碘**，隨機的是 1.1 GBq vs 3.7 GBq、以及 rhTSH vs 停藥。終點是 **6–9／8 個月的 ablation success**。
  - ESTIMABL2（NEJM 2022）與 IoN（Lancet 2025）：隨機的是**做 vs 不做**。
- **建議怎麼裁決**：C1 的骨架必須分兩段寫，不可混為一句「四個試驗都說放射碘可以少做」。HiLo／ESTIMABL1 對「要不要做」**沒有提供任何證據**。

### ⚠C-6　ESTIMABL2 排除掉的，正好是台灣最常見的那一種人

- ESTIMABL2 的排除條件逐字（ClinicalTrials.gov NCT01837745）：「Patients with cancer classified as **pT1a unifocal (in which ablation is not necessary)**, or pT1N1, pT2, pT3, pT4 or N1 (who have a higher risk of recurrence) (classification TNM 2010)」。
- 也就是說：**單一顆、≤1 公分的乳突微小癌（PTMC）根本不在試驗裡**，理由是「本來就不必做」；而**任何 N1、任何 pT2 以上也不在裡面**。納入的是 pT1am（多發、總和 >1 且 ≤2 公分）N0/Nx 或 pT1b N0/Nx。
- **建議怎麼裁決**：C1 不可以寫成「ESTIMABL2 證明低風險的人都不用做」。要寫「它證明的是**這一格**的人不用做，而更小的那一格是連試驗都認為不必問的」——這一句要與紅線 2 合看，避免讀者把自己那顆自動歸進去。

### ⚠C-7　紅線 6 與指引原文直接衝突：2025 ATA 在正文裡給了整張劑量表

- ATA 2025 Table 10「Summary of Recommendations for Initial RAI Following Thyroidectomy」逐格列出每個風險組的建議 GBq／mCi 區間。低碘飲食也給了「approximately 1–2 weeks」。停藥也給了「LT4 should be withdrawn for 3–4 weeks」。
- **SPEC 紅線 6 禁止把這些數字寫進文章。**
- **建議怎麼裁決**：brief 裡保留原文供編輯核對，**C1／C2 正文一律不得出現 GBq／mCi／週數／隔離天數**。C2 可以寫「指引對停藥時間、飲食天數確實有一個範圍，但各國法規與各院核醫科的做法不同，請照你這家醫院核醫科給你的那張紙」。C1 講到 HiLo／ESTIMABL1 時，建議寫成「低劑量與高劑量的兩組」而不寫數值——但這一點請編輯裁決，因為 1.1 vs 3.7 GBq 是那兩篇的**識別特徵**，拿掉之後句子會變得很難讀。**C 組傾向：C1 可寫「試驗比較的是低活度與標準（較高）活度兩種做法」，不給數字；若編輯認為必須給，請在 §九 明文豁免。**

### ⚠C-8　2025 ATA 的放射碘建議：中間風險的兩格用的是同一句，而且是最弱的一句

Recommendation 32 逐字（含強度與證據等級，逐字抄）：

> A. Remnant ablation is not recommended routinely after total thyroidectomy for patients with ATA low-risk DTC. **(Strong recommendation, High certainty evidence)**
> B. RAI adjuvant therapy may be considered after total thyroidectomy in patients with ATA low-intermediate and intermediate-high risk of recurrent DTC. **(Conditional recommendation, Low certainty evidence)**
> C. RAI adjuvant therapy is recommended routinely after total thyroidectomy for patients with ATA high-risk DTC. **(Strong recommendation, Moderate certainty evidence)**
> D. In patients with an initial diagnosis of DTC with distant metastases, RAI therapy is recommended routinely after total thyroidectomy. **(Strong recommendation, Moderate certainty evidence)**

注意：**低風險「不常規做」是 Strong + High；高風險「常規做」只是 Strong + Moderate；中間風險是 Conditional + Low。** 指引自己在正文承認「There are few studies that have evaluated RAI in a cohort of patients who are uniquely at intermediate risk or that can be classified as low-intermediate or intermediate-high risk of recurrence, **limiting strong recommendations**」。這個強弱倒置是 C1 最重要的一個支點：**不做的證據，比做的證據強。**

### ⚠C-9　2025 ATA 引入「Good Practice Statement」，它**沒有**證據等級

指引逐字：「When the quality of evidence was low or insufficient, a Good Practice Statement (GPS) served as an alternative to a graded recommendation … **A GPS is not GRADE-d** but is like a strong recommendation」。

**C2 要用的幾乎全部是 GPS**：低碘飲食（R35）、出院／防護說明（R39）、唾液腺與淚管（R40）、第二癌（R41）、懷孕哺乳與生育（R43）都是 GPS。
**建議怎麼裁決**：RESEARCH-COMMON §三 要求「建議強度與證據等級要一起抄」。C2 引用這些條文時，必須寫成「這是 ATA 2025 的 Good Practice Statement（指引自述未經 GRADE 評級）」，**不可以自己補一個等級上去，也不可以寫成『高證據等級』**。

### ⚠C-10　2025 ATA 有引註編號錯置，不可以透過指引轉引

抓下全文的參考文獻清單（1,458 筆）逐一比對後，至少兩處編號指錯：

1. 正文「pregnancy should be postponed for 1 year after RAI administration because of an increased miscarriage rate, **883**」——但 ref 883 是 `Ohori NP, Schoedel KE. Variability in the atypia of undetermined significance/follicular lesion of undetermined significance diagnosis in the Bethesda System for Reporting Thyroid Cytopathology…`，一篇細胞學判讀變異度的論文，與流產率無關。
2. 正文「This suggested that use of low-dose RAI for patients with low-risk DTC is noninferior … **763**. Similar findings were observed at 5 years of follow-up in the ESTIMABL1 trial. **764**」——ref 763 是 Boucai 等人的基因體學論文、ref 764 是 Cao 等人的 BRAF/TERT 論文，**都不是 ESTIMABL1**。
3. 2025 年 10 月的 Corrigendum（Thyroid 2025;35(11):1350）只更正了兩位作者的服務單位、一個中間名縮寫、與 Table 8 的一個列標題，**沒有**更正上述引註。

**建議怎麼裁決**：凡是要引用的數字，一律回原始論文抓，不得寫「ATA 2025 引用了某某研究」。

### ⚠C-11　一篇被 ATA 2025 引為 rhTSH 生活品質證據的統合分析，自己把數字標錯了

`Recombinant human thyrotropin-aided versus thyroid hormone withdrawal-aided radioiodine treatment for differentiated thyroid cancer after total thyroidectomy: a meta-analysis.` Radiother Oncol 2014;110(1):25–30 摘要中：

- 生活品質「RR=3.92, 95% CI: 3.44–5.40」——**風險比的信賴區間應該幾何對稱**，3.92² = 15.4，而 3.44×5.40 = 18.6，不對稱。
- 同一段又出現「RR=-0.9, 95% CI: -2.20–0.39」與「RR=-0.14, 95% CI: -0.73–0.45」、「RR=-10.51」——**風險比不可能是負數**，這些顯然是平均差（mean difference）被標成 RR。

依 RESEARCH-COMMON §三，這是**來源自己標錯**。**判定：這篇的 ablation 成功率 RR=0.97（0.94–1.01）可用；生活品質那幾個數字一律不得引用。** rhTSH 的生活品質請改引 ATA 2025 正文敘述（GPS 層級）或 ESTIMABL1／HiLo 原文。

### ⚠C-12　台灣端：查無任何規範放射碘住院隔離或出院基準的法規

三條路都走過，逐一記錄於來源清單 [C-S38]–[C-S46]。結論是：

- **核安會（原原能會）主管法規共用系統「輻射防護」法規體系共 68 筆，逐筆看過，沒有任何一筆與碘-131 病人住院、隔離或出院基準有關。**
- 全國法規資料庫以「碘-131」全文檢索：法規名稱 0 筆、法條內容 12 筆，12 筆逐筆看過全部無關（工廠危險物品申報辦法、食品工廠建築及設備設廠標準、核子事故緊急應變法等）。以「碘131」「放射性同位素治療病人」檢索：0 筆。
- 《輻射醫療曝露品質保證標準》（唯一與醫療輻射品保有關的法規命令）第 2 條列舉的適用設備只有：醫用直線加速器、含鈷六十之遠隔治療機、遙控後荷式近接治療設備、電腦斷層治療機、電腦刀、加馬刀，另加乳房 X 光攝影儀與診斷用電腦斷層掃描儀。**碘-131 不在內。**
- 《醫療機構設置標準》的特殊病床列舉中有「隔離病床」，但**無「核醫」「放射性」「同位素」字樣**。
- **aec.gov.tw 已不可連（本 session 代理回 502 connect_rejected）**；核安會現址 nusc.gov.tw 的全文檢索是前端 Google CSE，伺服器端不回結果；erss.nusc.gov.tw 的關鍵字檢索是 ASP.NET postback，多次嘗試回 0 bytes。**這三條路都要在 brief 寫明為「技術上取不到」，不是「不存在」。**

**真正存在、可以引用的上位規定只有兩條**（兩條都不講天數）：
- 《游離輻射防護法》第 7 條第 2 項逐字：「前項輻射防護作業，設施經營者應先擬訂輻射防護計畫，報請主管機關核准後實施。未經核准前，不得進行輻射作業。」
- 《游離輻射防護安全標準》第 12 條逐字：「輻射作業造成一般人之年劑量限度，依下列規定：一、有效劑量不得超過一毫西弗。……」

**建議怎麼裁決**：C2 的台灣段就寫成——規則是各醫院在自己那份**經主管機關核准的輻射防護計畫**裡定的，法規訂的是**旁人一年不得超過的劑量上限**，不是天數；所以天數會因人、因活度、因住家狀況而不同，要照你這家醫院核醫科給你的規定走。**這一段完全落在紅線 6 的安全側，也不違反紅線 4**（沒有從法條推論臨床實務普及度）。

### ⚠C-13　rhTSH 在 2025 ATA 變成「優先」，這是相對 2015 的明確改變

Recommendation 34 A 逐字：「In patients with DTC in whom RAI remnant ablation or adjuvant therapy is planned, **preparation with rhTSH stimulation is preferred over thyroid hormone withdrawal. (Strong recommendation, High certainty evidence)**」。
E 項逐字：「In patients with known distant metastases, either LT4 withdrawal or rhTSH can be used for preparation. (Conditional recommendation, Low certainty evidence)」。
**這對 C2〈那幾天怎麼過〉的框架影響很大**：「要不要停藥」在國際指引上已經不是預設，但**能不能用 rhTSH 牽涉到藥品可及性與給付**，而那件事 C 組**查不到台灣列項**（見「查不到的東西」）。

### ⚠C-14　SPEC §五 的站外指路，`faq.html` 那一段確認存在

`/home/claude/repo/faq.html` 第 593 行逐字：「會需要注意的是另外一類治療：例如甲狀腺癌的**放射碘**、以及某些把射源放進體內的**近接治療**。那些有各自的防護規定，若你的療程包含這些，團隊一定會事先個別說明。」
**建議**：C2 可以指過去，但要注意那一段的語氣是「體外放療不會殘留輻射」的對照句，C2 不能寫成「詳見 FAQ」——FAQ 那句沒有任何細節。

---

## 來源清單

### 一、去階梯的隨機試驗（做 vs 不做）

**[C-S1] Thyroidectomy without Radioiodine in Patients with Low-Risk Thyroid Cancer.** The New England journal of medicine 2022;386(10):923-932. PMID 35263518；Europe PMC 回傳 DOI 欄位為 `10.1056/nejmoa2111953`（全小寫，出版社原式為 NEJMoa，引用時請用 PMID 或 NEJM 官方寫法，勿逐字貼小寫版 DOI）
- 狀態：**PASS**
- 查證路徑：`https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE:"Thyroidectomy without Radioiodine in Patients with Low-Risk Thyroid Cancer"&resultType=core&format=json` → hitCount 2（本篇與五年追蹤）。另打 `https://clinicaltrials.gov/api/v2/studies/NCT01837745?format=json` 取納入／排除條件。
- 可用的數字：
  - 收案 776 人（ACTUAL，CTG）；三年可評估 730 人。（組織型＝分化型：乳突／濾泡／嗜酸性細胞，排除侵襲性亞型；分期系統＝TNM 2010（第七版）pT1am N0/Nx 或 pT1b N0/Nx；**未做過放射碘的世代**；手術＝全甲狀腺切除 R0）
  - 三年無事件比率：不做組 **95.6%**（95% CI 93.0–97.5）vs 做組 **95.9%**（95% CI 93.3–97.7），差 **−0.3 個百分點**（two-sided 90% CI −2.7 到 2.2），達非劣性。（終點＝**複合「事件」**，包含影像異常、超音波異常、Tg 或 TgAb 升高；**不是** structural recurrence，**更不是** survival）
  - 非劣性界限：**5 個百分點**。
  - 事件內容：結構性或功能性異常 8 人；生化性異常 23 人（共 25 個事件）。（終點＝structural／biochemical 分開列，**要分開寫**）
  - 「Events were more frequent in patients with a postoperative serum thyroglobulin level of more than 1 ng per milliliter during thyroid hormone treatment.」（Tg 閾值：**全甲狀腺切除後、服用甲狀腺素狀態下**，不可外推到單葉切除）
  - 「No treatment-related adverse events were reported.」
- 納入／排除（逐字自 CTG，**這是本篇最重要的部分**）：
  - 納入 4：「Patients with low risk of recurrence: pT1amN0 or pT1amNx with a sum of the size of the lesions above 1 cm and equal to or less than 2 cm, or pT1bN0 or pT1bNx (TNM 2010 classification).」
  - 排除 4：「Patients with cancer classified as pT1a unifocal (in which ablation is not necessary), or pT1N1, pT2, pT3, pT4 or N1 (who have a higher risk of recurrence) (classification TNM 2010)」
  - 排除 2：「Patients with aggressive histotype (poorly differentiated, tall-clear-cylindric cell, diffuse sclerosing, or with an anaplastic component)」
  - 納入 1 允許嗜酸性細胞（Hurthle）：「papillary, follicular or **with Hurthle cells**」——**與 HiLo／ESTIMABL1 不同，那兩篇把 Hürthle 排除掉**（見 [C-S7]、[C-S9]）。
  - 年齡 ≥18 歲，PS 0–1，術後 2–5 個月內納入，術後頸部超音波無側頸異常。

**[C-S2] Thyroidectomy without radioiodine in patients with low-risk thyroid cancer: 5 years of follow-up of the prospective randomised ESTIMABL2 trial.** The lancet. Diabetes & endocrinology 2025;13(1):38-46. PMID 39586309；DOI（EPMC 回傳）`10.1016/s2213-8587(24)00276-6`
- 狀態：**PASS**
- 查證路徑：同上查詢的第 1 筆；再以 `EXT_ID:39586309&resultType=core` 取摘要全文。
- 可用的數字：
  - 776 人入組（女 642 人 82.7%、男 134 人 17.3%；中位年齡 **52.9 歲**，IQR 42.6–63.1）；五年可評估 **698** 人。
  - 五年無事件比率：不做組 **93.2%** vs 做組 **94.8%**，差 **−1.6%**（90% CI −4.5 到 1.4）→ 仍達非劣性（界限 −5%）。（終點同 [C-S1] 的複合事件；風險組＝ATA low；分期＝pT1am／pT1b N0/Nx）
  - 事件：結構性或功能性 11 人、生化性 31 人。
  - 結論逐字：「There is no loss of opportunity in following these patients without postoperative ablation.」
  - 試驗狀態逐字：「This study … is **completed**.」（與 CTG 上 NCT01837745 顯示 `ACTIVE_NOT_RECRUITING`、completion `2030-01 ESTIMATED` **不一致**——登錄資料未更新）

**[C-S3] Thyroidectomy with or without postoperative radioiodine for patients with low-risk differentiated thyroid cancer in the UK (IoN): a randomised, multicentre, non-inferiority trial.** Lancet (London, England) 2025;406(10498):52-62. PMID 40543520；DOI（EPMC 回傳）`10.1016/s0140-6736(25)00629-4`
- 狀態：**PASS**
- 查證路徑：先由 ISRCTN WHO-format API 得知有 results（見 [C-S5]），再以 Europe PMC `query=(ISRCTN80416929) OR (TITLE:"IoN" AND TITLE:"radioiodine")` 命中，最後 `EXT_ID:40543520&resultType=core` 取全摘要。
- 可用的數字（全部：分化型；TNM7 或 TNM8；全甲狀腺切除 R0；RAI-naive 世代）：
  - 33 個英國癌症中心；2012-06-26 至 2020-03-18 收 **504 人**（女 390 人 77%、男 114 人 23%）；ITT：不做 251／做 253。Per-protocol：不做組 249／做組 231。
  - 中位追蹤 **6.8 年**（IQR 5.6–8.6，不做組）／**6.6 年**（4.8–8.5，做組）。
  - 追蹤期間共 **17 次復發**（不做組 8、做組 9，ITT）。
  - 五年**無復發率**（ITT）：不做 **97.9%**（95% CI 96.1–99.7）vs 做 **96.3%**（93.9–98.7）；per-protocol 97.9%（96.1–99.7）vs 96.9%（94.7–99.1）。
  - 五年絕對風險差 **0.5 個百分點**（95% CI −2.2 到 3.2，p(non-inferiority)=0.033）→ 達非劣性；**非劣性界限 5 個百分點**。
  - 終點定義逐字：「5-year recurrence-free survival, defined by the absence of locoregional recurrent or persistent structural disease, distant metastases, or **death from thyroid cancer**」（＝**structural recurrence + 疾病特異性死亡**的複合，**與 ESTIMABL2 的複合終點不是同一個東西**）
  - 次群組（**這是 C1 最該寫的一段**）：pT3／pT3a 者 46 人中 4 人（**9%**）復發，pT1／pT2 者 458 人中 13 人（**3%**）；N1a 者 47 人中 6 人（**13%**）復發，N0／Nx 者 457 人中 11 人（**2%**）。逐字：「but they were similar among those who did not receive ablation」——**風險較高的那些人，做不做放射碘的復發率一樣。**
  - 不良事件（per-protocol）：疲倦 63/249（25%）vs 65/231（28%）；嗜睡 34（14%）vs 32（14%）；**口乾 24（10%）vs 21（9%）**；無治療相關死亡。（**這個口乾比率是「低活度 ablation」情境下的，不可外推到高活度或多次治療**）
  - 結論逐字（範圍**比納入條件窄**）：「ablation (or postoperative radioiodine) can be avoided for patients with **pT1, pT2, and N0 or Nx tumours with no adverse features**.」
- 納入條件（自 CTG NCT01398085，逐字節選）：「pT1a (≤1cm) unifocal with positive level VI lymph nodes (pN1a); pT1a(m): all individual foci ≤1cm; pT1b and pT1b(m): >1-2cm; pT2 and pT2(m): >2-4cm; pT3 and pT3(m): >4cm confined to the thyroid; pT3 R0 +/- (m): any size with minimal ETE if recommended by the MDT; pN0; pN1a; pNX」；濾泡癌（**including oncocytic or Hürthle cell cancer**）限 minimally invasive。排除：pT1a 單一、≤1 公分、無淋巴結、行單葉切除者。
- 避孕條件（**C2 可用，但屬試驗規定不是指引**）：逐字「Willing to use contraception for the duration of the trial until **6 months post radioiodine treatment (for females)** or **4 months post treatment (for males)**」

**[C-S4] ClinicalTrials.gov NCT01398085（IoN）**　URL：`https://clinicaltrials.gov/api/v2/studies/NCT01398085?format=json`
- 狀態：**PASS**（作為「登錄狀態」的證據；**不可用來論斷結果是否發表**）
- 查證路徑：先以 `query.titles=Is ablative radio-iodine Necessary` 命中 NCT01398085，再取全紀錄。
- 看到什麼：officialTitle「Is Ablative Radio-iodine Necessary for Low Risk Differentiated Thyroid Cancer Patients」；acronym `IoN`；sponsor University College, London；orgStudyId `UCL/10/0299`；EudraCT `2011-000144-21`；CRUK `CRUK/11/010`；ISRCTN `ISRCTN80416929`；狀態 `ACTIVE_NOT_RECRUITING`；start `2012-06-26 ACTUAL`；primary completion `2031-03 ESTIMATED`；enrollment 504 ACTUAL；**無 resultsSection**。
- Primary outcome 逐字：「Phase III: Disease-free thyroid specific survival — DFS measured from randomisation until date of recurrence or death from thyroid cancer」。

**[C-S5] ISRCTN80416929（ION）**　URL：`https://www.isrctn.com/api/query/format/who?q=ISRCTN80416929`
- 狀態：**PASS**
- 查證路徑：上列 API，HTTP 200，回 XML。
- 看到什麼：public_title「ION - Is ablative radiOiodine Necessary for low risk differentiated thyroid cancer patients?」；scientific_title「Randomised trial comparing total thyroidectomy, thyriod stimulating hormone (TSH) suppression and radioactive iodine ablation with total thyroidectomy and TSH suppression, in low-risk patients with thyroid cancer」（原文 `thyriod` 為登錄方的錯字，逐字抄錄）；study_design「Randomized non-blind non-inferiority Phase II/III multicentre trial」；target_size 570；results_actual_enrolment 504；recruitment_status「No longer recruiting」；results_date_first_publication 24/06/2025；results_date_completed 31/03/2031。

**[C-S6] Is radioiodine necessary for patients with low-risk differentiated thyroid cancer after thyroidectomy: a pooled analysis of ESTIMABL2 and IoN trials.** Frontiers in oncology 2025;15:1670978. PMID 41229489；DOI `10.3389/fonc.2025.1670978`；PMCID PMC12602227（**OA**）
- 狀態：**PASS（但只作為「合併起來也沒差」的佐證，不作為主要引用）**——只納入 2 篇 RCT，異質性高，且第一作者群與兩個原試驗無關。
- 查證路徑：Europe PMC 同上查詢命中；`EXT_ID:41229489&resultType=core`。
- 可用的數字（分化型；ATA low risk；RAI-naive vs RAI；終點各自不同已如上）：
  - 2 篇第三期 RCT、**1,280 人**。
  - 復發 RR **0.78**（0.36–1.70），P=0.53；RFS HR **0.96**（0.80–1.15），P=0.68。
  - 結構性事件 RR 0.83（0.68–1.02）P=0.07；生化性事件 RR 0.88（0.71–1.08）P=0.23。
  - 不良事件 RR 0.97（0.79–1.20）；grade 3–5 AE RR 0.25（0.03–2.20）；**死亡 RR 1.28（0.48–3.41）P=0.62**；**第二原發癌 RR 1.26（0.58–2.73）P=0.55**。（終點＝all-cause death；**不是** disease-specific survival；人數與事件數都極少，**只能用來說「看不出差別」，不能用來說「一樣安全」**）
  - PROSPERO CRD420251105509。

### 二、劑量與準備方式的隨機試驗（做的話怎麼做）

**[C-S7] Ablation with low-dose radioiodine and thyrotropin alfa in thyroid cancer.** The New England journal of medicine 2012;366(18):1674-1685. PMID 22551128；DOI（EPMC 回傳）`10.1056/nejmoa1109589`
- 狀態：**PASS**
- 查證路徑：`TITLE:"Ablation with low-dose radioiodine and thyrotropin alfa in thyroid cancer"` hitCount 1；另打 `https://clinicaltrials.gov/api/v2/studies/NCT00415233?format=json` 取納入排除。
- 可用的數字（分化型，**排除 Hürthle 與侵襲性亞型**；T1–T3、可有 N1、M0；年齡 16–80 歲；全甲狀腺切除 R0；2×2 factorial）：
  - 隨機 **438 人**，可分析 421 人。
  - **Ablation success**（終點＝6–9 個月的殘餘組織清除成功率，**不是**復發、**不是**存活）：低活度 **85.0%** vs 高活度 **88.9%**；rhTSH **87.1%** vs 停藥 **86.7%**；所有差值 95% CI 落在 ±10 個百分點內 → 非劣性。
  - 低活度+rhTSH **84.3%** vs 高活度+停藥 **87.6%** vs 高活度+rhTSH **90.2%**。
  - **住院 ≥3 天比率：高活度 36.3% vs 低活度 13.0%（P<0.001）**（C2 可用：說明「為什麼活度會影響要待幾天」，但**不得把 36.3%／13.0% 寫成台灣的天數**）
  - 不良事件比率：低活度 **21%** vs 高活度 **33%**（P=0.007）；rhTSH **23%** vs 停藥 **30%**（P=0.11）。
- CTG 排除逐字：「No **Hurthle cell carcinoma** or aggressive variants, including … Tall cell, insular, poorly differentiated disease with diffuse sclerosing」；避孕：女性治療後 6 個月、男性 4 個月。

**[C-S8] Recurrence after low-dose radioiodine ablation and recombinant human thyroid-stimulating hormone for differentiated thyroid cancer (HiLo): long-term results of an open-label, non-inferiority randomised controlled trial.** The lancet. Diabetes & endocrinology 2019;7(1):44-51. PMID 30501974；DOI `10.1016/s2213-8587(18)30306-1`；PMCID PMC6299255（**OA**）
- 狀態：**PASS**
- 查證路徑：`TITLE:"HiLo" AND TITLE:"radioiodine"` hitCount 2，取本篇；`EXT_ID:30501974&resultType=core`。
- 可用的數字（分化型；T1–T3、可有淋巴結、無遠端轉移、無顯微殘存；**RAI-treated 世代**）：
  - 2007-01-16 至 2010-07-01 隨機 438 人；追蹤至 2017-12-31，中位 **6.5 年**（IQR 4.5–7.6），434 人（低 217／高 217）。
  - 確認復發 **21 人**（低活度 11、高活度 10）；其中 4 人（每組 2 人）判為持續性疾病。
  - **累積復發率**（終點＝structural recurrence，非存活）：3 年 1.5% vs 2.1%；5 年 **2.1% vs 2.7%**；7 年 **5.9% vs 7.3%**；HR **1.10**（95% CI 0.47–2.59），p=0.83。
  - rhTSH vs 停藥：3 年 1.5% vs 2.1%；5 年 2.1% vs 2.7%；7 年 **8.3% vs 5.0%**；HR **1.62**（95% CI 0.67–3.91），p=0.28。
  - 逐字：「No material difference in risk was seen for T3 or N1 disease.」
  - 逐字：「**Data on adverse events were not collected during follow-up.**」（**C2 重要**：HiLo 長期追蹤**沒有**長期副作用資料，不可拿它說「長期沒有副作用」）

**[C-S9] Strategies of radioiodine ablation in patients with low-risk thyroid cancer.** The New England journal of medicine 2012;366(18):1663-1673. PMID 22551127；DOI（EPMC 回傳）`10.1056/nejmoa1108586`
- 狀態：**PASS**
- 查證路徑：`TITLE:"Strategies of radioiodine ablation in patients with low-risk thyroid cancer"` hitCount 1；CTG NCT00435851。
- 可用的數字（分化型乳突／濾泡，**排除 Hürthle 與侵襲性亞型**；納入 pT1 ≤1cm 且 N1/Nx、pT1 >1–2cm 任何 N、或 pT2N0；**未標明 TNM 版本，收案期 2007–2010，應為第六／七版——寫進文章時必須註明「版本未載明」**）：
  - 2007–2010 共 752 人；**92% 為乳突癌**。
  - 684 人可評估：頸部超音波正常 652 人（**95%**）；其中無 Tg 抗體者 621/652（**95%**）刺激後 Tg ≤1.0 ng/mL。
  - **Ablation 完全成功 631/684（92%）**；兩種活度之間、兩種 TSH 刺激方式之間皆等效（equivalence 設計）。
  - 逐字：「There were no unexpected serious adverse events.」

**[C-S10] Outcome after ablation in patients with low-risk thyroid cancer (ESTIMABL1): 5-year follow-up results of a randomised, phase 3, equivalence trial.** The lancet. Diabetes & endocrinology 2018;6(8):618-626. PMID 29807824；DOI `10.1016/s2213-8587(18)30113-x`
- 狀態：**PASS**
- 查證路徑：`TITLE:"ESTIMABL1"` hitCount 1；`EXT_ID:29807824&resultType=core`。
- 可用的數字（同上族群；**RAI-treated 世代**）：
  - 726 人（原 752 人的 **97%**）接受追蹤；中位追蹤 **5.4 年**（range 0.5–9.2）。
  - **715 人（98%）無疾病證據**（定義逐字：「serum thyroglobulin of 1 ng/mL or less on levothyroxine treatment and normal results on neck ultrasonography, when performed」——**這是全甲狀腺切除且做過放射碘之後的閾值**）。
  - 其餘 11 人：結構性疾病 4 人、Tg 升高 5 人、超音波不確定 2 人。其中 6 人原受低活度（5 人 rhTSH、1 人停藥）、5 人原受高活度（2 人 rhTSH、3 人停藥）。
  - 逐字：「Our findings suggest that disease recurrence was **not related to the strategy used for ablation**.」

### 三、指引與共識

**[C-S11] 2025 American Thyroid Association Management Guidelines for Adult Patients with Differentiated Thyroid Cancer.** Thyroid : official journal of the American Thyroid Association 2025;35(8):841-985. PMID 40844370；DOI `10.1177/10507256251363120`；PMCID PMC13090833
- 狀態：**PASS**（全文取得並逐條核對）
- 查證路徑：Europe PMC `TITLE:"American Thyroid Association" AND TITLE:"Guidelines" AND TITLE:"Differentiated Thyroid Cancer"` sort by date → 命中。`https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13090833/fullTextXML` **回 404**（非 OA 子集）；改打 `https://pmc.ncbi.nlm.nih.gov/articles/PMC13090833/` → HTTP 200、2.43 MB，抽出正文 988,291 字元與 1,458 筆參考文獻。
- 方法學（逐字）：「Published English-language articles were eligible for inclusion, with a **final search date of July 1, 2024**.」「A modified Grading of Recommendations Assessment, Development and Evaluation system was used」。**單一例外**：納入 2025 年新版 WHO 內分泌腫瘤分類。
- 風險分層（逐字）：「categories are designated as **low (<10%), low-intermediate (10–15%), intermediate-high (≥16–30%), and high (>30%) risk of recurrence**」（終點＝biochemical or structural recurrence；與 AJCC 第八版**併用**，不是取代）
- Recommendation 32（誰該做放射碘）：**見 ⚠C-8，四句逐字並附強度與等級。**
- Recommendation 32 正文中對低風險的關鍵敘述（逐字，**這是 C1「有沒有存活好處」最直接的答案**）：
  - 「There is increasing evidence suggesting **lack of a clinical benefit of RAI in ATA low-risk thyroid cancer**, particularly for patients categorized as having an excellent response after surgery.」
  - 「A multi-institutional, retrospective study followed 1298 patients with ATA low-risk DTC for a median of 10.3 years and determined that **there was no benefit of RAI therapy with respect to overall or disease-free survival**.」（＝[C-S19]）
  - 「The National Thyroid Cancer Treatment Cooperative Study Group (NTCTCSG) also found that RAI treatment for patients with **Stage I and II DTC** does not influence **disease-specific and disease-free survival**.」
  - 「However, it is important to note that studies are limited in truly determining RAI-associated outcomes **due to the low incidence of disease-related mortality and morbidity in this cohort**.」
  - 「One potential limitation of these studies is the **relatively limited duration of follow-up**.」
- 中間風險段（逐字，**C1 必須照抄這句不確定性**）：「There are few studies that have evaluated RAI in a cohort of patients who are uniquely at intermediate risk … **limiting strong recommendations**. Further studies are needed in this group of patients」。Lamartina 的系統性回顧被描述為「11 nonrandomized studies suggested benefit, whereas **13 studies did not**」。
- 高風險段：SEER 資料顯示遠端轉移的 PTC 與 FTC 使用術後放射碘與較佳 overall survival 相關（**終點＝OS，回溯性 SEER，不是 RCT**）。
- Table 10：逐格劑量區間（**紅線 6，正文不得引用**），註腳逐字：「Consistent with the Martinique documents, the final recommendation for administered activity should be based on **multidisciplinary management recommendations**.」
- Recommendation 34（準備方式）：**見 ⚠C-13。**C 項逐字：「If thyroid hormone withdrawal is planned prior to RAI therapy or diagnostic testing, LT4 should be withdrawn for 3–4 weeks. If LT4 is withdrawn for ≥4 weeks, substitution of LT4 with liothyronine (LT3) in the initial weeks should be considered. In such circumstances LT3 should be withdrawn for at least 2 weeks. (Good Practice Statement)」D 項：「A goal of TSH >30 mIU/L should be employed in preparation for RAI therapy or diagnostic testing. (Good Practice Statement)」
- **Recommendation 35（低碘飲食）逐字全文**：「A low-iodine diet for approximately 1–2 weeks should be used for patients undergoing RAI remnant ablation or treatment. **(Good Practice Statement)**」
  - 正文自承不確定（逐字）：「However, there are **unresolved questions regarding the actual impact of a low-iodine diet on the outcome of remnant ablation**, with the best available evidence largely restricted to retrospective analyses using historical controls.」「**The optimal stringency and duration of a low-iodine diet (if any) prior to therapeutic RAI administration are not known.**」
- **Recommendation 39（輻射防護說明）逐字全文**：「Patients should be provided oral and written instructions before preparation for RAI begins to minimize exposure to their families and members of the public, **consistent with guidelines in the country where therapy is performed** (e.g., in the United States, those of the Nuclear Regulatory Commission). (Good Practice Statement)」
  - 正文逐字（**C2 台灣段的完美接點**）：「Administration of RAI generally is performed as an **outpatient** procedure.」「Models can be used to calculate the time during which a patient should follow precautions to protect others. **Some controversy exists concerning which model most accurately predicts radiation exposure.**」「key parameters include biological half-life …, time of exposure, distance from source, and shielding.」「Recent data indicate that more traditional models **overestimate** radiation exposure contamination」「**Length of time precautions should be determined by calculations using an appropriate model.**」「In general, release to home is preferred; **release to hotel is discouraged**.」
- **Recommendation 40（唾液腺與淚管）逐字全文**：
  - 「A. Patients should be counseled that RAI treatment may be associated with (acute and chronic) salivary gland morbidity, lacrimal duct stenosis, and potential risk of secondary malignancies. (Good Practice Statement)」
  - 「B. For prevention of salivary gland side effects after RAI, **general measures including hydration** are recommended. (Good Practice Statement)」
  - 「C. Patients with xerostomia are at increased risk of dental caries and should discuss preventive strategies with their dental health professional. (Good Practice Statement)」
  - 「D. Surgical correction should be considered for nasolacrimal outflow obstruction, which often presents with excessive tearing (epiphora) but also predisposes to infection. (Good Practice Statement)」
  - 酸糖（逐字，**C2 最該抄的一句**）：「Some centers suggest use of sour lozenges to promote salivary secretion after RAI therapy, but **other groups consider it harmful**, and there is **no evidence of reduction in salivary gland radiation-absorbed dose with vitamin C tablets**. Hence, **the role of sour candies to increase salivary secretion after RAI is uncertain**.」「**evidence is insufficient to recommend for or against these modalities**」「One study suggested sour candy **may increase salivary gland damage when given within one hour of RAI therapy**, as compared to starting its use 24 hours post-therapy.」「Another study showed that the use of lemon slices within 20 minutes of 123I administration resulted in **increased** radiation absorbed dose to the salivary glands.」「Other studies have suggested that early use and multiple administered doses of lemon juice **transiently decreased** radiation exposure to the parotid glands, so the exact role and details of use of sialagogues to prevent salivary gland damage **remain uncertain**.」
  - 逐字：「There is **probably no administered activity of RAI that is completely safe**, nor is there any maximum cumulative administered dose that could not be used in selected situations.」
- **Recommendation 41（第二原發癌）逐字全文**：「Patients should be counseled about the risks of second primary malignancy (SPM) after RAI treatment for DTC. **The absolute increase in risk attributable to RAI appears to be small and does not warrant additional screening for SPM.** (Good Practice Statement)」
- **Recommendation 43（懷孕、哺乳、性腺）逐字全文**：
  - 「A. Female patients of reproductive age receiving RAI therapy should have a negative screening evaluation for pregnancy prior to RAI administration and **avoid pregnancy for at least 6 months** after receiving RAI. (Good Practice Statement)」
  - 「B. RAI should not be given to nursing female patients. Depending on the clinical situation, RAI therapy should be deferred until lactating women **have stopped breast-feeding or pumping for at least 3 months**. A diagnostic 123I scan may be performed in recently lactating women to detect breast uptake that may warrant deferral of therapy. (Good Practice Statement)」
  - 「C. **Male patients receiving cumulative radioiodine activities >14.8 GBq (400 mCi) should be counseled regarding potential risks of infertility.** (Good Practice Statement)」
  - 「D. **Female patients receiving RAI should be counseled that such therapy has not been shown to impact future fertility.** (Good Practice Statement)」
  - 男性受孕間隔（正文，逐字）：「Although data are limited, **it has been recommended that males who receive 131I wait at least 120 days (the lifespan of sperm) after 131I therapy before attempting conception** or providing a sperm sample for assisted reproduction.」（指引把此句歸給 2017 ATA 妊娠指引，**非本指引自身的編號建議**）
  - 逐字：「Gonadal radiation exposure is reduced with good hydration, frequent micturition to empty the bladder, and avoidance of constipation.」「The use of laxatives may decrease radiation exposure for the bowel … vigorous oral hydration reduces exposure of the bladder and gonads.」
- **Recommendation 42**：「Patients receiving therapeutic administration of RAI should have a baseline complete blood count and assessment of renal function. (Good Practice Statement)」

**[C-S12] Executive Summary of the 2025 American Thyroid Association Management Guidelines for Adult Patients with Differentiated Thyroid Cancer.** Thyroid 2025;35(11):1214-1220. PMID 41173539；DOI `10.1177/10507256251390877`
- 狀態：**PASS（僅摘要層級；全文 Subscription required，未取得）**
- 查證路徑：Europe PMC `EXT_ID:41173539&resultType=core`，`fullTextUrlList` 僅有 `Subscription required`。
- 可用內容（逐字）：「The updated guidelines emphasize individualized care through the **DATA framework** (Diagnosis, risk/benefit Assessment, Treatment decisions, and response Assessment)」「Highlights include expanded role of molecular diagnostics, **refined risk stratification**, greater emphasis on active surveillance and lobectomy … **De-escalation of surveillance for low-risk patients** and introduction of the concept of **complete remission** are also new.」

**[C-S13] Corrigendum to: 2025 American Thyroid Association Management Guidelines for Adult Patients with Differentiated Thyroid Cancer.** Thyroid 2025;35(11):1350. PMID 41182278；DOI `10.1177/10507256251387671`；PMCID PMC13521431（**OA**）
- 狀態：**PASS**
- 查證路徑：`https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13521431/fullTextXML` HTTP 200。
- 內容：只更正 Angela Leung 與 Gregory A. Brent 的服務單位、Joseph R. Osborne 的中間名縮寫、Table 8 列標題由「Follicular Carcinoma」改為「Follicular Carcinoma and IEFVPTC」以配合 2025 WHO 用語，以及「additional minor spelling errors」。**⚠C-10 的引註錯置未被更正。**

**[C-S14] Controversies, Consensus, and Collaboration in the Use of 131I Therapy in Differentiated Thyroid Cancer: A Joint Statement from the American Thyroid Association, the European Association of Nuclear Medicine, the Society of Nuclear Medicine and Molecular Imaging, and the European Thyroid Association.** Thyroid 2019;29(4):461-470. PMID 30900516；DOI `10.1089/thy.2018.0597`
- 狀態：**PASS（摘要層級；全文 Subscription required，未取得逐條九原則）**
- 查證路徑：Europe PMC `"Martinique Principles"` 全文檢索命中（hitCount 552，其中絕大多數是加勒比海馬提尼克島的流行病學論文，須人工挑）；`EXT_ID:30900516&resultType=core`。
- 可用內容（摘要逐字）：九原則的五項摘要包含「define the goals of 131I therapy as **remnant ablation, adjuvant treatment, or treatment of known disease**」「describe the importance of evaluating **postoperative disease status** and multiple other factors **beyond clinicopathologic staging** in 131I therapy decision making」「recognize that the **optimal administered activity of 131I adjuvant treatment cannot be definitely determined from the published literature**」「acknowledge that current **definitions of 131I-refractory disease are suboptimal**」。
- **⚠ 九原則的逐條原文未取得**（付費牆）。C1 只能引用上述摘要層級的五點。

**[C-S15] The Martinique Principles.** Journal of nuclear medicine 2019;60(9):1334-1335. PMID 31227575；DOI `10.2967/jnumed.119.232066`
- 狀態：**FAIL（作為內容來源）／PASS（作為「同一份文件在核醫期刊同步刊出」的證據）**
- 理由：Europe PMC 該筆 `abstractText` 為空、`isOpenAccess` = N，沒有可引用的內容。
- 查證路徑：`EXT_ID:31227575&resultType=core`。

**[C-S16] Brief progress report from the intersocietal working group on differentiated thyroid cancer.** European journal of nuclear medicine and molecular imaging 2020;47(6):1345-1347. PMID 32166513；DOI `10.1007/s00259-020-04744-8`；PMCID PMC7188695（**OA，全文已取得**）
- 狀態：**PASS**
- 查證路徑：`https://www.ebi.ac.uk/europepmc/webservices/rest/PMC7188695/fullTextXML` HTTP 200, 19,963 bytes。
- 可用內容（逐字）：「In 2017, the European Association of Nuclear Medicine, the Society of Nuclear Medicine and Molecular Imaging, the European Thyroid Association, and the American Thyroid Association established an **intersocietal working group** on differentiated thyroid cancer.」「the group is intended to serve as a '**think-tank**' rather than a forum for the development of detailed guidelines. Specifically, the working group **will not interfere with the formal guideline process** of the respective societies.」「Despite extensive efforts to review the literature, **the available evidence was found to be insufficient to provide any definitive guidance**. Furthermore … **we could not arrive at consensus opinions on these important topics**.」
- 2019 年討論的四個題目逐字：「(1) the criteria for success of I-131 therapy, (2) whether there are variations in peri-therapeutic diagnostics which may lead to differences in treatment, (3) the optimal tests to include for post-surgical diagnostic imaging to guide the decision on whether or not to pursue I-131 therapy and (4) the arguments in favour of and against empirical and dosimetry-based approaches」。

**[C-S17] 2022 ETA Consensus Statement: What are the indications for post-surgical radioiodine therapy in differentiated thyroid cancer?** European thyroid journal 2022;11(1):e210046. PMID 34981741；DOI `10.1530/etj-21-0046`；PMCID PMC9142814（**OA，全文已取得**）
- 狀態：**PASS**，但**⚠ 這份共識的每一條建議都沒有標註建議強度或證據等級**——全文逐字檢查，Recommendation 1–8 後面沒有任何 GRADE 標記。引用時必須寫明「該文未標示強度與等級」。
- 查證路徑：`https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9142814/fullTextXML` HTTP 200, 121,446 bytes。
- 八條建議逐字（節選 C 組要用的四條）：
  - **Recommendation 2**：「The use of I-131 therapy as adjuvant treatment or treatment of known disease is indicated for patients in the **high risk of recurrence category or with known structural disease**. In this setting, high activities (≥3700 MBq) of radioiodine are preferred over low activities.」
  - **Recommendation 3**：「In the **intermediate-risk** category, RAI therapy **may be indicated and should be tailored according to individual cases**.」
  - **Recommendation 4**：「In **low-risk** patients, the benefit of I-131 therapy is **a matter of intensive scientific debate** and the decision on whether to perform RAI therapy should be based on the presence of individual risk modifiers.」
  - **Recommendation 5**：「**Recombinant human TSH** during l-T4 treatment **should be the preferred method of preparation** for RAI administration.」
  - **Recommendation 8**：「A low-iodine diet **may be prescribed but its utility is not demonstrated unequivocally**. Any iodine-containing drug should be avoided.」
- 低風險段可用的數字（逐字）：「in these patients the risk of **disease-specific deaths is less than 1%** and that of **persistent/recurrent disease is low (2–3%)**」（風險組＝ATA low；組織型＝分化型；終點分別為 DSS 與 persistent/recurrent disease）；「It is hard to imagine that retrospective studies can demonstrate any benefit in terms of disease-free survival when the overall risk is as low as 2–3%.」
- 微小癌逐字：「RAI remnant ablation is **unlikely to improve the outcome of papillary microcarcinoma (<1 cm, uni- or multi-focal)**, in absence of other higher-risk features and **RAI should not be used in these patients**.」（腫瘤大小＝≤1 公分 PTMC，**這是 PTMC 專屬的一句，不可外推到 1–4 公分**）
- 低風險但 Tg 可測者逐字：「low-risk patients with post-operatively detectable serum Tg … or with abnormal ultrasound findings have a higher risk of recurrence, and RAI therapy **may be considered, although there is no evidence that it can improve disease-free survival**.」
- 低碘飲食段逐字：「**no prospective study has ever determined the cut-off over which interference may actually occur**」「a LID allowing for ≤50 µg/day of iodine for 1–2 weeks prior to RAI administration appeared to be associated with an increase in RAI uptake, compared to no LID, but **there is conflicting evidence on the impact of LID on the remnant ablation success**.」
- 停藥造成的低下逐字：「this induces hypothyroidism with a **major decrease in quality of life, which may last for up to 2–3 months**」。
- **⚠ 時效**：這份 2022 共識的低風險段寫「two major randomized trials … are **ongoing** in France (ESTIMABL 2) and UK (Ion)」，IoN 當時未讀出。引用時必須加註「發表於 IoN 結果之前」。

**[C-S18] SNMMI Procedure Standard/EANM Practice Guideline for Nuclear Medicine Evaluation and Therapy of Differentiated Thyroid Cancer: Abbreviated Version.** Journal of nuclear medicine 2022;63(6):15N-35N. PMID 35649660；**Europe PMC 回傳 DOI 為 None**
- 狀態：**FAIL（作為內容來源）**
- 理由：Europe PMC `abstractText` 為空、無 DOI、無 PMCID、非 OA。只能確認「這份文件存在、是核醫兩會的聯合實務指引」，內容一字都沒拿到。
- 查證路徑：`EXT_ID:35649660&resultType=core`。
- **建議**：若 C1／C2 需要核醫學界的正式立場，改用 [C-S17] 與 [C-S16]；或請編輯決定是否另尋管道。

**[C-S19] Impact on overall survival of radioactive iodine in low-risk differentiated thyroid cancer patients.** The Journal of clinical endocrinology and metabolism 2012;97(5):1526-1535. PMID 22344193；DOI `10.1210/jc.2011-2512`
- 狀態：**PASS**
- 查證路徑：`DOI:"10.1210/jc.2011-2512"` hitCount 1。
- 可用的數字（分化型；ATA low risk；1975–2005 收案；**回溯性、非隨機**）：
  - 1,298 人，中位追蹤 **10.3 年**；做放射碘 911 人 vs 未做 387 人。
  - 單變項：**10 年 OS** 未做 **95.8%** vs 做 **94.6%**（P=0.006）；**10 年 DFS** 未做 **93.1%** vs 做 **88.7%**（P=0.001）。（**⚠ 未做組看起來比較好，這是適應症偏誤——做放射碘的人本來風險就高。不可以照字面寫。**）
  - 多變項 Cox：放射碘與 OS（P=0.243）、DFS（P=0.2659）**均無顯著且非獨立相關**。
  - 傾向分數分層後：OS 無差異（P=0.3524），HR **0.75**（95% CI 0.40–1.38）；DFS 無差異（P=0.48）。（終點：OS 與 DFS；**不是** disease-specific survival）

**[C-S20] Low-risk differentiated thyroid cancer and radioiodine remnant ablation: a systematic review of the literature.** The Journal of clinical endocrinology and metabolism 2015;100(5):1748-1761. PMID 25679996；DOI `10.1210/jc.2014-3882`
- 狀態：**PASS**
- 查證路徑：`TITLE:"Radioiodine remnant ablation" AND TITLE:"low-risk" AND TITLE:"systematic review" AND AUTH:"Lamartina"` hitCount 1。
- 可用內容（逐字）：「**No OP demonstrating RRA benefit on recurrence in LR patients was found**; two OPs found no evidence of benefit. We found **11 OPs that observed some benefit** in reducing recurrence rates with RRA in **IR** patients and **13 OPs that failed to show benefit** from RRA in this group.」「Neck ultrasonography and serum thyroglobulin measurement are equivalent or superior in detecting and localizing residual disease compared to post-therapy whole-body scan.」（風險組：LR＝ATA low、IR＝ATA intermediate（**2015 版的三級系統**，非 2025 四級）；終點＝復發）

### 四、第二原發癌

**[C-S21] Second primary malignancies in thyroid cancer patients.** British journal of cancer 2003;89(9):1638-1644. PMID 14583762；DOI `10.1038/sj.bjc.6601319`；PMCID PMC2394426（**OA**）
- 狀態：**PASS**（**這是「劑量—風險」關係唯一的一手數字來源**）
- 查證路徑：`TITLE:"Second primary malignancies in thyroid cancer patients" AND AUTH:"Rubino"` hitCount 1。
- 可用的數字（組織型＝乳突與濾泡癌；1934–1995 診斷；平均診斷年齡 44 歲；瑞典／義大利／法國三個世代合併）：
  - **6,841 人**（存活滿 2 年者）；17% 曾接受體外放療、**62% 接受過碘-131**；共 **576 人**發生第二原發癌。
  - 相較各國一般族群，第二原發癌風險整體增加 **27%（95% CI 15–40）**。（**分母是「甲狀腺癌病人 vs 一般人口」，不是「做 vs 不做放射碘」——兩者不可混用**）
  - **劑量—反應**（**這是 ATA 2025 引用的那組數字**）：隨累積活度上升，實體腫瘤與白血病風險皆增加，**每 GBq 碘-131、每 10 萬人年，超額絕對風險為實體癌 14.4、白血病 0.8**。
  - 與碘-131 有關係的部位：骨與軟組織、大腸直腸、唾液腺。
  - 作者結論逐字：「These results strongly highlight the necessity to **delineate the indications of 131I treatment** in thyroid cancer patients in order to restrict its use to patients in whom clinical benefits are expected.」

**[C-S22] Second primary malignancy risk after radioactive iodine treatment for thyroid cancer: a systematic review and meta-analysis.** Thyroid 2009;19(5):451-457. PMID 19281429；DOI `10.1089/thy.2008.0392`
- 狀態：**PASS**
- 查證路徑：`TITLE:"Second primary malignancy risk after radioactive iodine treatment for thyroid cancer: a systematic review and meta-analysis"` hitCount 1。
- 可用的數字（做 vs 不做放射碘；潛伏期最短 2–3 年）：
  - 納入 **2 篇多中心研究**（一歐一北美），資料來自 **16,502 人**。
  - 任何第二原發癌 **RR 1.19（95% CI 1.04–1.36，p=0.010）**。
  - 白血病 **RR 2.5（95% CI 1.13–5.53，p=0.024）**。
  - **⚠ 只有 2 篇研究**——ATA 2025 稱之為「A meta-analysis of two large multicenter studies」。C1 引用時必須寫出這個分母。

**[C-S23] A Systematic Review and Meta-Analysis of Subsequent Malignant Neoplasm Risk After Radioactive Iodine Treatment of Thyroid Cancer.** Thyroid 2018;28(12):1662-1673. PMID 30370820；DOI `10.1089/thy.2018.0244`
- 狀態：**PASS**
- 查證路徑：`TITLE:"subsequent malignant neoplasm risk after radioactive iodine treatment of thyroid cancer"` hitCount 1。
- 可用的數字（做 vs 不做放射碘）：
  - 17 篇研究（3 篇系統性回顧 + 14 篇原始研究）。
  - **未校正**的任何續發惡性腫瘤 **RR 0.98（95% CI 0.76–1.27）**；10 篇研究、**65,539 人**；異質性 Q=64.26, df=9, p<0.001, **I²=85.99**。
  - **校正干擾因子後**的合併 RR **1.16（95% CI 0.97–1.39）**；6 篇研究、至少 11,241 人；Q=10.86, df=5。
  - **⚠ 這篇的 0.98 與 [C-S22] 的 1.19 方向相反**；ATA 2025 同時引用兩者。C1 必須把兩個都寫出來，**不可以只挑一個**。

**[C-S24] Second primary malignancies induced by radioactive iodine treatment of differentiated thyroid carcinoma - a critical review and evaluation of the existing evidence.** European journal of nuclear medicine and molecular imaging 2022;49(9):3247-3256. PMID 35320386；DOI `10.1007/s00259-022-05762-4`；PMCID PMC9250458（**OA**）
- 狀態：**PASS**（**GRADE 評級是這篇最有價值的部分**）
- 查證路徑：`TITLE:"Second primary malignancies induced by radioactive iodine treatment of differentiated thyroid carcinoma"` hitCount 1。
- 可用的數字：
  - 納入 **10 篇**研究。
  - 「SPM」的相對效應（RR／HR／OR）「**ranged from 1.14 to 1.84** across studies, but **most results were not statistically significant**」。
  - 「SHM」（續發血液惡性腫瘤）「reported relative effects **ranged from 1.30 to 2.50**, with **2/3 of the studies presenting statistically significant results**」。
  - 「**In 7/8 of the studies, increased risk for SPM was shown with increasing cumulative RAI activity.**」
  - **證據品質**：SPM 與劑量—反應皆為「**very low**」；SHM 為「**low**」。（**這一句是 C1 講第二癌時必須帶的護欄**）

**[C-S25] Risk of Hematologic Malignancies After Radioiodine Treatment of Well-Differentiated Thyroid Cancer.** Journal of clinical oncology 2018;36(18):1831-1839. PMID 29252123；DOI `10.1200/jco.2017.75.0232`；PMCID PMC8462524
- 狀態：**PASS**
- 查證路徑：`TITLE:"Risk of Hematologic Malignancies After Radioiodine Treatment of Well-Differentiated Thyroid Cancer"` hitCount 2（另一筆為同題的讀者投書 PMID 29723090，勿誤引）。
- 可用的數字（SEER；分化型；做 vs 不做放射碘）：
  - **148,215 人**：53% 只手術、47% 接受放射碘。
  - **783 人**在中位 **6.5 年**（IQR 3.3–11.2）後發生續發血液惡性腫瘤。
  - 多變項：AML **HR 1.79（95% CI 1.13–2.82），P=0.01**；CML **HR 3.44（95% CI 1.87–6.36），P<0.001**。
  - 逐字：「This increased risk of AML and CML after RAI treatment was seen **even in low-risk and intermediate-risk WDTC tumors**.」
  - 發生 AML 者的中位 OS **8.0 年 vs 配對對照 31.0 年（P=0.001）**；RAI 後的 AML 相較 de novo AML 中位 OS **1.2 年 vs 2.9 年（P=0.06）**。
  - **⚠ 分母**：783/148,215 ≈ 0.53%，且那是「所有續發血液惡性腫瘤、兩組合計」。C1 寫這段時**必須同時給絕對數字與相對風險**，否則 HR 3.44 會被讀成「三倍多的人會得白血病」。

**[C-S26] Association Between Radioactive Iodine Treatment for Pediatric and Young Adulthood Differentiated Thyroid Cancer and Risk of Second Primary Malignancies.** Journal of clinical oncology 2022;40(13):1439-1449. PMID 35044839；DOI `10.1200/jco.21.01841`；PMCID PMC9061144（**OA**）
- 狀態：**PASS**
- 查證路徑：`AUTH:"Pasqual E" AND TITLE:"second primary malignancies" AND SRC:MED` hitCount 1。
- 可用的數字（**年齡限定：45 歲以前診斷**；SEER 九個登錄處 1975–2017；非轉移性 DTC）：
  - 存活滿 5 年者 **27,050 人**（中位追蹤 **15 年**），45% 接受放射碘 → 實體惡性腫瘤 **RR 1.23（95% CI 1.11–1.37）**。
  - 子宮頸／體癌 RR 1.55（1.03–2.32）；唾液腺 RR 2.15（0.91–5.08，**不顯著**）；胃 RR 1.61（0.70–3.69，**不顯著**）；肺 RR 1.42（0.97–2.08，**不顯著**）；女性乳癌 RR 1.18（0.99–1.40，**不顯著**）。
  - 存活滿 20 年者：實體癌 RR 1.47（1.24–1.74）；乳癌 RR 1.46（1.10–1.95）。
  - 存活滿 2 年者 **32,171 人**：血液惡性腫瘤 **RR 1.51**（摘要在此處被 Europe PMC 截斷，**CI 未取得 → 這個 1.51 不得單獨引用**）。
  - **⚠ 這是「45 歲以前診斷」的族群**，不可外推到中老年診斷者。

### 五、低碘飲食

**[C-S27] Dietary iodine restriction in preparation for radioactive iodine treatment or scanning in well-differentiated thyroid cancer: a systematic review.** Thyroid 2010;20(10):1129-1138. PMID 20860420；DOI `10.1089/thy.2010.0055`；PMCID PMC2956383
- 狀態：**PASS（僅書目層級）**
- 查證路徑：`TITLE:"Dietary iodine restriction in preparation for radioactive iodine treatment or scanning in well-differentiated thyroid cancer"` hitCount 1；**Europe PMC 回傳的 `abstractText` 為空**，故只取得書目。
- **可用的內容**：僅能作為「ETA 2022 所引的那份系統性回顧」的書目確認（ETA 2022 逐字轉述其結論：「a LID allowing for ≤50 µg/day of iodine for 1–2 weeks prior to RAI administration appeared to be associated with an increase in RAI uptake, compared to no LID」）。**本篇自身的數字一律不得引用。**

**[C-S28] Two weeks of a low-iodine diet are equivalent to 3 weeks for lowering urinary iodine and increasing thyroid radioactive iodine uptake.** Thyroid 2011;21(1):61-67. PMID 21162685；DOI `10.1089/thy.2010.0232`
- 狀態：**PASS（僅書目與 ATA 轉述層級）**
- 查證路徑：`TITLE:"Two weeks of a low-iodine diet are equivalent to 3 weeks…"` hitCount 1；`abstractText` 為空。
- ATA 2025 對它的逐字轉述（**引用時要註明是經指引轉述**）：「In a randomized controlled trial including **46 patients**, the increase in uptake and reduction in urinary iodine excretion **did not significantly differ** between patients who followed a low-iodine diet for **2 weeks compared with 3 weeks** prior to RAI **scanning**, suggesting that there may be little reason to extend the low-iodine diet beyond 2 weeks.」（**注意：是 scanning，不是 therapy；n=46**）
- **⚠ 依 ⚠C-10，這一句經由 ATA 2025 轉引是目前唯一途徑，但 ATA 2025 的引註編號已被證實有錯置紀錄；C2 若要寫「兩週和三週沒有差」，建議只寫「有一個小型隨機試驗發現延長沒有多拿到什麼」，不給 n 與週數。**

**[C-S29] The Urinary Iodine Level Based on Different Duration of Low-Iodine Diet for Radioactive Iodine Therapy.** AACE endocrinology and diabetes 2026;13(4):571-574. PMID 42491485；DOI `10.1016/j.aed.2026.03.011`；PMCID PMC13377963（**OA**）
- 狀態：**PASS**（**但只是 72 人的單中心回溯，且為 ATA 2025 文獻截止日之後**）
- 查證路徑：`(TITLE:"low-iodine diet") AND PUB_YEAR:[2022 TO 2026]` hitCount 11。
- 可用的數字：72 人（中位 46 歲，range 19–82；63.9% 女性）；1 週 53 人、2 週 19 人。2 週後尿碘中位 0.228 µmol/L（29 µg/L）vs 1 週 0.362 µmol/L（46 µg/L），**P=0.24（不顯著）**。作者逐字：「**There is a need for future large prospective randomized control trials** to identify the optimal duration of LID」。
- **C2 用法**：只用來支持「連『要幾天』都還沒有定論」這個論點，**不得給天數建議**。

### 六、唾液腺、淚管

**[C-S30] Salivary gland side effects commonly develop several weeks after initial radioactive iodine ablation.** Journal of nuclear medicine 2009;50(10):1605-1610. PMID 19759114；DOI `10.2967/jnumed.108.061382`
- 狀態：**PASS**
- 查證路徑：`DOI:"10.2967/jnumed.108.061382"` hitCount 1。
- 可用的數字（**回溯性**；262 人；66% 女性；**93% 乳突癌**；單次 ablation，**中位活度 5,217 MBq / 141 mCi**——這是相對高的活度，**不可外推到低活度 ablation 或到 IoN 的 10% 口乾**）：
  - 第一年內出現唾液腺副作用者 **39%**。
  - 中位 **7 年**後仍持續者：整體世代的 **≤5%**；但**在第一年有症狀的人裡面**，末次追蹤仍持續者為 **5%–13%**。
  - 劑量—反應：與**唾液腺腫脹**有統計顯著關係（P=0.001），與口乾（P=0.63）、味覺改變（P=0.27）、唾液腺疼痛（P=0.152）**無**顯著關係。
  - ATA 2025 轉述的分層（**原文摘要未載，僅見於指引正文，引用需註明**）：活度 1.1 GBq（30 mCi）者 **14%** 出現唾液腺副作用；**≥2.8 GBq（75 mCi）者 40%**（P=0.046）。準備方式：停藥組活度較高，但唾液腺腫脹反而較少（**10% vs rhTSH 20%，P=0.017**）；口乾、味覺改變、疼痛則無差異。

**[C-S31] Does lemon candy decrease salivary gland damage after radioiodine therapy for thyroid cancer?** Journal of nuclear medicine 2005;46(2):261-266. PMID 15695785；**Europe PMC 回傳 DOI 為 None**
- 狀態：**PASS**（無 DOI，引用時用 PMID）
- 查證路徑：`AUTH:"Nakada K" AND TITLE:"lemon candy"` hitCount 1（**注意：標題含問號，直接以整句 TITLE 查詢會讓 Europe PMC 回 504 Gateway Time-out**）。
- 可用的數字（**非隨機、前後期對照**；兩組平均活度 3.96 vs 3.87 GBq；排除既有唾液腺疾病、糖尿病、膠原病、曾接受放射碘或頸部放療者）：
  - A 組 105 人：碘-131 服用後 **1 小時內**開始吃檸檬糖；B 組 125 人：**24 小時後**才開始。
  - 唾液腺炎 **63.8% vs 36.8%（P<0.001）**；味覺減退或喪失 **39.0% vs 25.6%（P<0.01）**；口乾（含反覆唾液腺炎）**23.8% vs 11.2%（P<0.005）**。
  - **永久性口乾症：A 組 15 人（14.3%）vs B 組 7 人（5.6%），P<0.05。**
  - 結論逐字：「An early start of sucking lemon candy **may induce a significant increase in salivary gland damage**. Lemon candy **should not be given until 24 h after** radioiodine therapy.」
  - **⚠ 這是前後兩期的世代比較，不是隨機分派**，且 ATA 2025 明講整體證據「insufficient to recommend for or against」。C2 寫法建議：「有一份研究發現太早開始反而更糟，也有研究發現早點吃可以暫時降低腮腺劑量——所以現在的指引是**兩邊都不建議**，照你醫院核醫科怎麼說。」

**[C-S32] Nasolacrimal drainage system obstruction from radioactive iodine therapy for thyroid carcinoma.** The Journal of clinical endocrinology and metabolism 2002;87(12):5817-5820. PMID 12466391；DOI `10.1210/jc.2002-020210`
- 狀態：**PASS**
- 查證路徑：`TITLE:"Nasolacrimal drainage system obstruction from radioactive iodine therapy for thyroid carcinoma"` hitCount 1。
- 可用的數字（**16 個月的單中心臨床觀察，不是前瞻世代**；上皮來源甲狀腺癌）：
  - 共 423 人接受常規照護，其中 **390 人**曾接受碘-131 ablation 或治療；**10 人**出現溢淚（epiphora）。
  - 這 10 人的**平均累積活度 17,279 ± 2,923 MBq（467 ± 79 mCi）**、**平均單次活度 6,660 ± 555 MBq（180 ± 15 mCi）**。（**這是高累積活度族群，與只做一次低活度 ablation 的人完全不同一條線**）
  - 症狀在末次碘-131 後 **6.5 ± 1.4 個月（range 3–16）**出現；**從症狀出現到正確診斷平均 18 ± 5 個月**。
  - 作者逐字：「Patients reporting epiphora should be evaluated promptly by an oculoplastic surgeon.」
  - **C2 寫法**：重點是「一直流眼淚不要當成小事、也不要當成過敏，那是要找眼科（眼整形）看的」，**不要給累積活度數字**（紅線 6）。

### 七、生育、懷孕、哺乳

**[C-S33] A systematic review examining the effects of therapeutic radioactive iodine on ovarian function and future pregnancy in female thyroid cancer survivors.** Clinical endocrinology 2008;69(3):479-490. PMID 18284643；DOI `10.1111/j.1365-2265.2008.03222.x`
- 狀態：**PASS**
- 查證路徑：`DOI:"10.1089/thy.2008.0392" OR DOI:"10.1111/j.1365-2265.2008.03222.x"`。
- 可用的數字（16 篇、**3,023 名女性或青少女**；**全部為觀察性研究，無長期 RCT**；首次治療年齡 8–50 歲；累積活度 30–1,099 mCi）：
  - 「**Transient absence of menstrual periods occurred in 8–27% of women within the first year after RAI**, particularly in older women.」
  - 「RAI-treated women experienced **menopause at a slightly younger age**」
  - 「In the first year after RAI therapy, several studies reported **increased rates of spontaneous and induced abortions**.」
  - 「However, RAI treatment for DTC was **generally not associated with a significantly increased risk of long-term infertility, miscarriage, induced abortions, stillbirths, or offspring neonatal mortality or congenital defects**.」
  - ATA 2025 另轉述同一系列的更新版統合分析：停經年齡平均 **49.5 歲 vs 對照 51 歲**，治療後一年 AMH 略降，**懷孕率無差異**。（**該更新版的獨立書目 C 組未取得，見「查不到的東西」**）

**[C-S34] Longitudinal Analysis of the Effect of Radioiodine Therapy on Ovarian Reserve in Females with Differentiated Thyroid Cancer.** Thyroid 2020;30(4):580-587. PMID 31928168；DOI `10.1089/thy.2019.0504`
- 狀態：**PASS**
- 查證路徑：`TITLE:"Longitudinal Analysis of the Effect of Radioiodine Therapy on Ovarian Reserve in Females with Differentiated Thyroid Cancer"` hitCount 1。
- 可用的數字（前瞻縱貫；16 歲至停經前女性；DTC；**RAI-treated**）：
  - **65 人**（平均年齡 **32 歲**；中位 5 次測量；中位追蹤 **34 個月**）。
  - AMH 隨時間非線性變化：**單次放射碘組在 12 個月時下降 55%**，之後持平。
  - **多次放射碘組**在持平後繼續下降，**48 個月時下降 85%**。
  - **⚠ n=65，且 AMH 是卵巢庫存的替代指標，不是懷孕率。** C2 必須寫成「卵巢庫存的指標會掉，但這不等於不能懷孕」，並與 [C-S33]、[C-S35] 並陳。

**[C-S35] Association Between Pregnancy Outcomes and Radioactive Iodine Treatment After Thyroidectomy Among Women With Thyroid Cancer.** JAMA internal medicine 2020;180(1):54-61. PMID 31633736；DOI `10.1001/jamainternmed.2019.4644`；PMCID PMC6806426
- 狀態：**PASS**
- 查證路徑：`DOI:"10.1001/jamainternmed.2019.4644"` hitCount 1。
- 可用的數字（**韓國 HIRA 全民健保資料庫**；2008-01-01 至 2015-12-31 因 DTC 接受甲狀腺切除的 20–49 歲女性 **111,459 人**；只手術 59,483 人（53.4%）vs 手術+放射碘 51,976 人（46.6%）；懷孕結局追蹤至 2017-12-31）：
  - 結局：流產（自然與人工）、早產、先天畸形。
  - ATA 2025 對本篇的逐字轉述：「there were **no differences in the assessed outcomes if pregnancy occurred more than 6 months after RAI** was administered. When pregnancy occurred **less than 6 months** after RAI, there was a **small but significant increase in congenital malformations in the offspring (OR 1.74 [CI 1.01–2.97])**.」
  - **⚠ 該 OR 的信賴區間 1.01–2.97：幾何中心為 √(1.01×2.97)=1.73，與 OR 1.74 相符（幾何對稱，通過檢查）。**
  - **⚠ Europe PMC 摘要在 Results 段被截斷，上述 OR 是經 ATA 2025 轉述取得**；依 ⚠C-10，C2 若要寫這個數字，建議只寫「在治療後很短的時間內懷孕，資料上看得到一點差別」而不給 OR。

**[C-S36] Impact on testicular function of a single ablative activity of 3.7 GBq radioactive iodine for differentiated thyroid carcinoma.** Human reproduction (Oxford, England) 2018;33(8):1408-1416. PMID 29912343；DOI `10.1093/humrep/dey222`
- 狀態：**PASS**
- 查證路徑：`DOI:"10.1093/humrep/dey222"` hitCount 1（**直接以標題查會 504 timeout**）。
- 可用的數字（**前瞻縱貫多中心**；DTC；**40 名 18–55 歲男性**；**單次 3.7 GBq**；治療前 V0、3 個月 V3、13 個月 V13）：
  - 治療前所有人性腺功能正常。
  - V3：FSH 顯著上升、inhibin B 顯著下降；**精蟲濃度與正常形態百分比顯著下降（P<0.0001）**。
  - 逐字：「These modifications were **transient** as both sperm concentration and normal morphology rate returne[d]…」（摘要在此被 Europe PMC 截斷）
  - ATA 2025 轉述：「A longitudinal prospective multicenter study observed **no DNA fragmentation in sperm**, but a **statistically significant increase in chromosomal abnormalities 3 months** after a single 131I ablative dose with activity of 3.7 GBq. The slight increase in chromosomal abnormalities **persisted 13 months** after therapy.」
  - **⚠ n=40，單次活度。** 這是 C2 男性段最重要的一手證據：**短期會掉、會回來，但染色體異常在 13 個月時還看得到一點。** 這正是「男性建議等 120 天」這個建議的背景。

### 八、rhTSH vs 停藥（品質有問題的來源）

**[C-S37] Recombinant human thyrotropin-aided versus thyroid hormone withdrawal-aided radioiodine treatment for differentiated thyroid cancer after total thyroidectomy: a meta-analysis.** Radiotherapy and oncology 2014;110(1):25-30. PMID 24485353；DOI `10.1016/j.radonc.2013.12.018`
- 狀態：**部分 PASS／部分 FAIL**
- **PASS 的部分**：7 篇 RCT、**1,535 人**；**ablation 成功率 RR 0.97（95% CI 0.94–1.01，p=0.1）**——rhTSH 與停藥無顯著差異。
- **FAIL 的部分（來源自己標錯，見 ⚠C-11）**：生活品質「RR=3.92, 95% CI: 3.44–5.40」信賴區間非幾何對稱；同段落出現負值的「RR」（−0.9、−0.14、−10.51），風險比不可能為負，顯係平均差被標成 RR。**這幾個數字一律不得引用。**
- 查證路徑：`DOI:"10.1016/j.radonc.2013.12.018" OR DOI:"10.3346/jkms.2014.29.6.786"` → 只回本篇（**另一篇 Pak 的 J Korean Med Sci 統合分析用該 DOI 查不到，見「查不到的東西」**）。

### 九、台灣端

**[C-S38] 游離輻射防護法**（全國法規資料庫 pcode `J0160009`；核安會系統 `LawContent.aspx?id=FL011952`）
- 狀態：**PASS**
- 查證路徑：`https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=J0160009`，全文抓下後逐關鍵字檢索「病人」「出院」「核醫」「治療」「醫療」。
- 逐字可用：
  - 第 7 條第 2 項：「前項輻射防護作業，設施經營者應先擬訂輻射防護計畫，報請主管機關核准後實施。未經核准前，不得進行輻射作業。」
  - 定義（第 2 條第 10 款）：「醫療曝露：指在醫療過程中病人及其協助者所接受之曝露。」
  - 「醫療機構對於協助病人接受輻射醫療者，其有遭受曝露之虞時，應事前告知及施以適當之輻射防護。」
- **查無**：「出院」0 筆、「核醫」0 筆、任何隔離天數規定 0 筆。

**[C-S39] 游離輻射防護安全標準**（pcode `J0160004`）
- 狀態：**PASS**
- 查證路徑：`https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=J0160004`。
- 逐字可用：
  - 第 12 條：「輻射作業造成一般人之年劑量限度，依下列規定：一、有效劑量不得超過**一毫西弗**。二、眼球水晶體之等價劑量不得超過**十五毫西弗**。三、皮膚之等價劑量不得超過**五十毫西弗**。」
  - 第 2 條定義段：「前項第三款個人劑量，指個人接受體外曝露及體內曝露所造成劑量之總和，**不包括由背景輻射曝露及醫療曝露所產生之劑量**。」（**這一句很重要：病人自己接受的治療劑量不受年限值管；受年限值管的是「旁人」。**）
- **查無**：「病人」0 筆、「出院」0 筆、「核醫」0 筆、「治療」0 筆（除職業曝露醫務監護一處外）。

**[C-S40] 輻射醫療曝露品質保證標準**（pcode `J0160063`；核安會系統 `LawContent.aspx?id=FL033174`；最後修正民國 112.04.12）
- 狀態：**PASS（作為「碘-131 不在管制品項內」的證據）**
- 查證路徑：`https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=J0160063`，全 13 條逐條讀過。
- 第 2 條逐字列舉：「一、醫用直線加速器。二、含鈷六十放射性物質之遠隔治療機。三、含放射性物質之遙控後荷式近接治療設備。四、電腦斷層治療機。五、電腦刀。六、加馬刀。」另第 9-1 條乳房 X 光攝影儀、第 9-2 條診斷用電腦斷層掃描儀。
- **碘-131 治療不在其中。**

**[C-S41] 核能安全委員會主管法規共用系統「輻射防護」法規體系（共 68 筆）**
- 狀態：**PASS（作為「查無」的證據）**
- 查證路徑：`https://erss.nusc.gov.tw/law/LawCategoryContentList.aspx?CategoryID=004&page=1` 至 `page=7`，逐頁抓下、逐筆列出 68 個名稱（含法律 1、命令若干、行政規則、行政指導、令釋）。
- **看到什麼**：68 筆中**沒有任何一筆**的名稱與碘-131、核醫治療病人、住院隔離或出院基準有關。最接近醫療的四筆是：輻射醫療曝露品質保證標準、輻射醫療曝露品質保證組織與專業人員設置及委託相關機構管理辦法、輻射醫療曝露品質保證標籤核發作業要點、普查醫用放射性物質及可發生游離輻射設備實施要點——**四筆都與病人出院基準無關**。
- 另逐一檢查：「放射性物質與可發生游離輻射設備及其輻射作業管理辦法」（FL022712）、「非密封放射性物質輻射防護措施計畫指引」（GL000037）、「游離輻射防護法施行細則」（FL022710）全文——「病人」「病房」「核醫」「出院」皆 0 筆。

**[C-S42] 全國法規資料庫關鍵字檢索：「碘-131」「碘131」「放射性同位素治療病人」**
- 狀態：**PASS（作為「查無」的證據）**
- 查證路徑：`https://law.moj.gov.tw/Law/LawSearchResult.aspx?ty=ONEBAR&kw=<關鍵字>`，再取 `cur=Ld`（法條內容）分頁。
- 看到什麼：
  - 「碘-131」：**法規名稱 0 筆、法條內容 12 筆**；12 筆逐筆檢視為工廠危險物品申報辦法、先驅化學品工業原料之種類及申報檢查辦法、行政院原子能委員會核子事故調查評議委員會設置辦法、空氣污染防制法施行細則、食品工廠建築及設備之設置標準、食品工廠建築及設備設廠標準、食品原料阿拉伯樹膠規格標準、原子能法施行細則、核子反應器設施管制法施行細則、核子事故緊急應變法、核子事故緊急應變法施行細則、都市計畫法臺灣省施行細則——**全部無關**。
  - 「碘131」：法規名稱 0 筆。
  - 「放射性同位素治療病人」：法規名稱 0 筆。
- **依 RESEARCH-COMMON §三：零筆就寫零筆。**

**[C-S43] 醫療機構設置標準**（pcode `L0020025`）
- 狀態：**PASS（作為「查無」的證據）**
- 查證路徑：`https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=L0020025`。
- 看到什麼：特殊病床的列舉逐字為「加護病床、精神科加護病床、燒傷加護病床、燒傷病床、亞急性呼吸照護病床、慢性呼吸照護病床、**隔離病床**、骨髓移植病床、安寧病床、嬰兒病床、嬰兒床、血液透析床、腹膜透析床、手術恢復床、急診觀察床、性侵害犯罪加害人強制治療病床、急性後期照護病床、整合醫學急診後送病床、戒護病床及司法精神病床」——**「核醫」「放射性」「同位素」皆 0 筆**；「隔離病床」是一般感染隔離，**不得解讀為放射碘病房**。

**[C-S44] aec.gov.tw（原行政院原子能委員會網域）**
- 狀態：**FAIL（技術上不可達）**
- 查證路徑：`curl https://www.aec.gov.tw/` → exit code 56，代理回「connect_rejected（the egress proxy denied the CONNECT (organization policy) or could not reach the destination）」。
- **註**：該機關已改制為核能安全委員會（nusc.gov.tw），法規已全數移轉到 erss.nusc.gov.tw，見 [C-S41]。

**[C-S45] nusc.gov.tw 全文檢索與 erss.nusc.gov.tw 關鍵字檢索**
- 狀態：**FAIL（技術上取不到結果）**
- 查證路徑：
  - `https://www.nusc.gov.tw/fulltext/search.html?q=碘-131` HTTP 200，但回傳頁面只有 Google Custom Search 的容器 `<div class="gsc-...">`，**結果由前端 JavaScript 產生，伺服器端無資料**。
  - `https://erss.nusc.gov.tw/law/LawQuery.aspx` 為 ASP.NET postback；帶 `__VIEWSTATE`／`__EVENTVALIDATION`／cookie jar 送出 POST 後回 HTTP 200 但 **size_download = 0**。
- **必須寫成「這條路技術上走不通」，不可寫成「查無資料」。**

**[C-S46] mohw.gov.tw**
- 狀態：**FAIL（技術上取不到結果）**
- 查證路徑：`https://www.mohw.gov.tw/cp-16-search.html?q=放射性碘` → **HTTP 404**；首頁的站內搜尋連結指向 `https://www.google.com.tw/advanced_search?...as_sitesearch=www.mohw.gov.tw`，即衛福部站內搜尋外包給 Google，**無可程式化的端點**。

**[C-S47] Radiation safety in the treatment of patients with thyroid diseases by radioiodine 131I : practice recommendations of the American Thyroid Association.** Thyroid 2011;21(4):335-346. PMID 21417738；DOI `10.1089/thy.2010.0403`
- 狀態：**PASS（僅摘要層級）**
- 查證路徑：`TITLE:"Radiation safety in the treatment of patients with thyroid diseases by radioiodine"` hitCount 1。
- 可用內容（逐字，**C2 台灣段最好的對照**）：「Reviews of Nuclear Regulatory Commission regulations and International Commission on Radiological Protection recommendations formed the basic structure of the recommendations.」「**There are insufficient data on long-term outcomes to create evidence-based guidelines.**」「Examples of the development of tables to ascertain the **number of hours or days (24-hour cycles) of radiation precaution appropriate for individual patients**」
- **重點**：連 ATA 自己這份 2011 年的輻射安全建議都說「防護要幾天」是**一人一算**的表格，不是一個固定數字——這正是紅線 6 要的那個說法。**但這是 2011 年的文件，且是美國 NRC 架構，C2 不得用來描述台灣。**

**[C-S48] /home/claude/repo/faq.html 第 593 行**
- 狀態：**PASS**
- 查證路徑：`grep -n "放射碘" /home/claude/repo/faq.html`。
- 逐字：「會需要注意的是另外一類治療：例如甲狀腺癌的**放射碘**、以及某些把射源放進體內的**近接治療**。那些有各自的防護規定，若你的療程包含這些，團隊一定會事先個別說明。」

---

## 本組各篇可以寫的東西

### C1 `th-rai-whether`〈要不要做放射碘〉

**能站得住的支點（依強度排序）：**

1. **「不常規做」現在是 2025 ATA 裡**證據等級最高**的一句話。** Recommendation 32A 是 Strong + **High certainty**；而高風險「要做」只有 Strong + Moderate，中間風險是 Conditional + **Low**。這個強弱關係本身就是文章的骨架：**「不做」不是省略、不是放棄，是目前證據最硬的那一格。** ⟨[C-S11]⟩

2. **兩個隨機試驗，兩個國家，兩套終點，同一個方向。** ESTIMABL2 三年與五年（法國，複合事件終點）、IoN 六年多的追蹤與五年無復發率（英國，結構性復發＋疾病特異性死亡終點）。兩者的非劣性界限都是 5 個百分點，兩者都達標。**兩個終點不是同一個東西，要分開講。** ⟨[C-S1][C-S2][C-S3]⟩

3. **IoN 的次群組是這篇文章最有價值的一段。** pT3／pT3a 的人復發率是 pT1／pT2 的三倍（9% vs 3%），N1a 的人是 N0/Nx 的六倍多（13% vs 2%）——**但這些人做不做放射碘，復發率一樣。** 這句話同時做到兩件事：讓風險高的人知道自己風險高（不違反紅線 1 的下行方向），又不讓他們以為放射碘就是解答。⟨[C-S3]⟩

4. **「誰不必做」有兩層，不是一層。** 最裡面那一層是**單一顆、≤1 公分的乳突微小癌**——ESTIMABL2 直接把他們從試驗排除，理由逐字是「in which ablation is not necessary」；ETA 2022 逐字說「RAI should not be used in these patients」。外面那一層才是試驗真正回答的 pT1am／pT1b／pT2、N0 或 Nx。⟨[C-S1][C-S3][C-S17]⟩

5. **誰該做：遠端轉移與 ATA 高風險，兩句都是 Strong。** 這一段要寫得同樣清楚——文章不能只往「不用做」一個方向倒。⟨[C-S11]⟩

6. **存活這件事要講得很老實**（見下面「寫不了的句子」）。

7. **第二原發癌：三組數字並陳，不挑。** Sawka 2009 的 RR 1.19（1.04–1.36，只有 2 篇研究、16,502 人）、Yu 2018 校正後的 1.16（0.97–1.39，**不顯著**）與未校正的 0.98（I²=86）、Reinecke 2022 的 1.14–1.84 區間與「**very low** 證據品質」評級。血液惡性腫瘤那一支比較一致：Sawka 2009 白血病 RR 2.5、Molenaar 2018 AML HR 1.79／CML HR 3.44、Reinecke 2022 的 1.30–2.50。**劑量關係**只有 Rubino 2003 的一手數字（每 GBq 每 10 萬人年超額 14.4 個實體癌、0.8 個白血病），以及 Reinecke 2022 的「8 篇有 7 篇看到累積活度越高風險越高」。⟨[C-S21]–[C-S26]⟩

8. **HiLo／ESTIMABL1 是「要做的話，可以做得比較輕」這一段的支點，不是「要不要做」。** HiLo 七年復發率 5.9% vs 7.3%（HR 1.10, 0.47–2.59）、ESTIMABL1 五年 98% 無疾病證據，**兩者的隨機分派裡人人都做了放射碘**。⟨[C-S7]–[C-S10]⟩

**寫不了的句子（逐句列出來，給寫作組當黑名單）：**

- ❌「放射碘不會延長低風險病人的壽命」——**沒有任何隨機試驗以存活為主要終點**。ESTIMABL2 的終點是複合事件，IoN 的終點是無復發存活（含疾病特異性死亡但事件數只有 17 個），合併分析的全因死亡 RR 1.28（0.48–3.41）只反映「事件太少，看不出來」。**可以寫的是：到目前為止沒有研究顯示做了會活得比較久，也沒有研究顯示不做會活得比較短；這兩件事在低風險這一格都還沒有被證明過。** ⟨[C-S1][C-S3][C-S6][C-S11]⟩
- ❌「低風險的人做放射碘沒有好處」——ATA 2025 逐字是「**increasing evidence suggesting lack of a clinical benefit**」，並自承「studies are limited … due to the low incidence of disease-related mortality and morbidity in this cohort」與「relatively limited duration of follow-up」。
- ❌「Schvartz 的研究發現不做放射碘的人活得比較久」——單變項確實是 95.8% vs 94.6%，但那是**適應症偏誤**，多變項與傾向分數分層後兩組都沒差。這個數字**只能連同校正後的結果一起寫，或乾脆不寫**。⟨[C-S19]⟩
- ❌ 任何 GBq／mCi 數值（紅線 6）。ATA 2025 Table 10 與 ETA 2022 Recommendation 2／6 裡都有，**不得搬進正文**。
- ❌「四大學會已經有共識」——2020 年的 intersocietal 報告逐字說「we could not arrive at consensus opinions」。⟨[C-S16]⟩
- ❌「IoN 還沒有結果」（SPEC 原假設）——已發表。反過來也不能寫「IoN 已經結束」——論文自述仍在追蹤中，ISRCTN 記載完成日 2031-03-31。⟨[C-S3][C-S5]⟩
- ❌ 把 ATA 的復發風險組講成「期別」，或把 2015 的三級直接搬過來用。⟨⚠C-2⟩
- ❌「白血病風險是三倍」——Molenaar 的 CML HR 3.44 必須連同分母（148,215 人中 783 人發生任何續發血液惡性腫瘤）一起寫。⟨[C-S25]⟩
- ❌ 拿 HiLo／ESTIMABL1 的 ablation 成功率當「治癒率」或「復發率」。那是 6–10 個月時殘餘組織是否清乾淨的替代指標。

### C2 `th-rai-days`〈那幾天怎麼過〉

**能站得住的支點：**

1. **低碘飲食在管什麼**：它不是「對身體好」的飲食，是要把**體內的穩定碘清出來**，讓放射碘進得去該去的地方。而**它到底有沒有用、要多嚴、要多久，指引自己都寫「不知道」**——ATA 2025 逐字「The optimal stringency and duration of a low-iodine diet (if any) … are not known」，ETA 2022 逐字「its utility is not demonstrated unequivocally」「no prospective study has ever determined the cut-off」。2026 年還有人在做 1 週 vs 2 週的比較，而且 P=0.24。**這一段可以寫得很誠實，而且完全不必給天數。** ⟨[C-S11][C-S17][C-S29]⟩

2. **停藥 vs rhTSH**：2025 ATA 已把 rhTSH 列為**優先**（Strong + High certainty），ETA 2022 也是 preferred。理由是**效果一樣、副作用少、生活品質在施打當天明顯比較好**（ablation 成功率 RR 0.97, 0.94–1.01；HiLo 的不良事件 23% vs 30%）。**停藥造成的低下「may last for up to 2–3 months」**（ETA 2022 逐字）。寫作重點：這不是「哪個比較好」的個人偏好題，是有指引立場的；但**能不能用，牽涉到藥品可及與給付，C 組查不到台灣列項**（見下）。⟨[C-S11][C-S17][C-S7][C-S37 的 PASS 部分]⟩

3. **唾液腺**：機轉可以講（唾液腺會表現 NIS，所以碘會跑進去）。發生率有一手數字，但**必須標明那是中位 141 mCi 的高活度世代**：第一年 39%、七年後整體 ≤5% 仍有症狀；IoN 的低活度組口乾是 10%（做）vs 9%（不做）——**兩邊幾乎一樣，這個對照非常有說服力**。ATA 2025 唯一推薦的預防措施逐字只有「general measures including **hydration**」。⟨[C-S30][C-S3][C-S11]⟩

4. **檸檬糖這件事要寫成一個「反而」**：Nakada 2005 發現**太早吃（1 小時內）比 24 小時後才吃，永久性口乾多了將近三倍（14.3% vs 5.6%）**；另有研究發現維他命 C 錠對唾液腺吸收劑量沒有幫助；也有研究發現早吃能暫時降低腮腺劑量。ATA 2025 的結論逐字是「the exact role and details of use of sialagogues … **remain uncertain**」、「**evidence is insufficient to recommend for or against**」。**寫法：不要自己買糖來吃，也不要以為吃了就沒事；時機這件事有過相反的發現，照你醫院核醫科怎麼說。** ⟨[C-S31][C-S11]⟩

5. **淚管**：溢淚（epiphora）不是小事，也不是過敏。Kloos 2002 最值得寫的不是發生率（那個世代累積活度很高），而是**從症狀出現到被正確診斷平均花了 18 個月**。ATA 2025 Recommendation 40D 明寫可以手術矯正。⟨[C-S32][C-S11]⟩

6. **生育（女性）**：ATA 2025 逐字「avoid pregnancy for **at least 6 months**」（GPS）、且「such therapy **has not been shown to impact future fertility**」（GPS）。同時有 AMH 會掉的證據（單次 −55%、多次 −85%，n=65）與停經略早（49.5 vs 51 歲）——**這兩件事要並陳，不可只寫其中一個**。月經暫時停掉 8–27%。⟨[C-S11][C-S33][C-S34]⟩

7. **生育（男性）**：ATA 2025 逐字「Male patients receiving **cumulative** radioiodine activities >14.8 GBq (400 mCi) should be counseled regarding potential risks of infertility」（GPS）與「wait **at least 120 days** (the lifespan of sperm) … before attempting conception」。一手證據是 Bourcigaux 2018（n=40，單次）：3 個月時 FSH 上升、inhibin B 與精蟲濃度下降，**之後會回來**；但染色體異常的小幅上升**到 13 個月還在**。⟨[C-S11][C-S36]⟩
   - **⚠ 紅線 6 的判斷**：「120 天」與「6 個月」是**指引的建議間隔**，不是劑量也不是隔離天數。C 組認為**這兩個數字可以寫**，因為它們是病人要拿去和婦產科／泌尿科討論的東西，而且不寫會讓文章失去實用性。**但請編輯在 §九 明文裁決。** 若裁定不能寫，改為「指引對男女各有一個建議的等待期間，而且兩邊不一樣長，要問你的治療團隊」。

8. **哺乳**：ATA 2025 逐字「RAI should **not** be given to nursing female patients … until lactating women have stopped breast-feeding or pumping for **at least 3 months**」（GPS）。機轉可寫：哺乳中的乳腺會濃集碘。**注意：這是「治療前要停多久」，不是「治療後多久可以餵」——這兩件事很容易被寫反。** ⟨[C-S11]⟩

9. **隔離規定為什麼存在（台灣段）**：
   - 法規管的是**旁人**，不是你。《游離輻射防護安全標準》第 12 條：一般人年有效劑量不得超過一毫西弗；同標準第 2 條明定**醫療曝露不計入**。
   - 天數怎麼算：ATA 2025 逐字說關鍵參數是「biological half-life …, time of exposure, distance from source, and shielding」，而且「**Some controversy exists concerning which model most accurately predicts radiation exposure**」、「Length of time precautions should be determined by **calculations using an appropriate model**」。ATA 2011 的輻射安全建議也是給**表格**讓人一人一算。
   - 台灣由誰定：《游離輻射防護法》第 7 條第 2 項——各醫院要先擬訂**輻射防護計畫**報主管機關核准。
   - **⚠ 全國法規與核安會 68 筆法規裡，查無任何一筆規定碘-131 病人要住幾天或出院標準。** 所以文章的結論就是：**「規定存在，但它管的是劑量不是天數；天數是你這家醫院按你的情況算出來的。」** ⟨[C-S38][C-S39][C-S41][C-S42][C-S11][C-S47]⟩

**寫不了的句子：**

- ❌ 任何天數、任何 GBq／mCi、任何「幾公尺」「幾小時」的具體防護參數（紅線 6）。
- ❌「低碘飲食可以提高治療成功率」——證據是回溯性的、衝突的，兩份指引都自承未定。
- ❌「吃檸檬糖可以保護唾液腺」——**這是最該擋下來的一句**，證據方向是相反的或不明的。
- ❌「放射碘不會影響生育」——ATA 的原句是「has **not been shown to** impact future fertility」，這與「不會影響」不是同一件事；而且 AMH 明確會掉。
- ❌「治療後 X 個月就可以哺乳」——指引講的是**治療前**要停 3 個月；治療後的哺乳問題 C 組**查無**明確的指引句（ATA 2025 只寫「RAI should not be given to nursing female patients」）。
- ❌ 把 IoN 的口乾 10% 講成「放射碘的口乾機率是 10%」——那是**低活度單次 ablation** 的數字，而且對照組（沒做的人）是 9%。
- ❌ 從健保或法規條文推論台灣有多少人做、怎麼做（紅線 4）。
- ❌ 寫哪一家醫院有隔離病房、有幾間、自費多少（紅線 7）。
- ❌ 用「不用擔心」「很安全」這類安慰句取代「這些規定管的是什麼」的說明（紅線 1 的功能等價句）。

---

## 查不到的東西（明寫查無／取不到）

1. **Martinique 九原則的逐條原文**——Thyroid 2019;29(4):461-470 全文為 Subscription required（Europe PMC `fullTextUrlList` 只有 `Subscription required`）；同名的 J Nucl Med 2019 版（PMID 31227575）在 Europe PMC 連摘要都是空的。**目前只能引用摘要層級的五點概述。**
2. **SNMMI Procedure Standard/EANM Practice Guideline for … Differentiated Thyroid Cancer (2022) 的任何內容**——PMID 35649660，Europe PMC 無 DOI、無 PMCID、無摘要。**一字未取得。**
3. **Sawka 2010 低碘飲食系統性回顧的自身數字**——Europe PMC 回傳 `abstractText` 為空（PMID 20860420）。目前只能經由 ETA 2022 的轉述使用。
4. **Morsch 2011（2 週 vs 3 週）的自身數字**——同上，`abstractText` 為空（PMID 21162685）。只能經由 ATA 2025 轉述，而 ATA 2025 已被證實有引註錯置紀錄（⚠C-10）。
5. **ATA 2025 所引的「36 篇、比較有無放射碘的卵巢功能與懷孕率統合分析」的獨立書目**——指引把它掛在 ref 879（Sawka 2008, Clin Endocrinol），但 Sawka 2008 的摘要說的是 16 篇、3,023 人，**不是 36 篇**。這兩者對不上，可能是另一篇更新版被誤標。**C 組未能定位該篇，49.5 歲 vs 51 歲的停經年齡數字暫不得引用。**
6. **Pak 等人 J Korean Med Sci 的 rhTSH vs 停藥統合分析**——以 ATA 2025 參考文獻列出的 DOI `10.3346/jkms.2014.29.6.786` 於 Europe PMC 查詢 0 筆。**DOI 可能有誤，未取得。**
7. **台灣：規範碘-131 住院隔離或出院基準的可引用文件——查無。**
   - 全國法規資料庫「碘-131」法規名稱 **0 筆**、法條內容 12 筆全部無關；「碘131」「放射性同位素治療病人」**各 0 筆**。
   - 核安會「輻射防護」法規體系 **68 筆逐筆檢視，0 筆相關**。
   - 《輻射醫療曝露品質保證標準》管制品項 **不含碘-131**。
   - 《醫療機構設置標準》**無核醫／放射性病床項目**。
   - **這不是「不存在」的證明**——nusc.gov.tw 全文檢索為前端 Google CSE、erss.nusc.gov.tw 關鍵字檢索為 ASP.NET postback 且回 0 bytes、mohw.gov.tw 站內搜尋外包 Google、aec.gov.tw 已不可連（代理 502）。**四條路都技術性受阻。** 依 RESEARCH-COMMON §三：**寫成「查無列項，要問醫院核子醫學科」，不推論有或沒有。**
8. **台灣 rhTSH（Thyrogen／重組人類 TSH）的藥證與健保給付狀態**——本組未查（屬 E4 範圍）。**C2 不得寫「台灣有／沒有 rhTSH」或「健保給不給付」，也不得寫成「大多數人是用停藥的」。** 建議 C2 寫成：「國際指引現在偏好打針那一種準備方式；台灣這邊能不能用、要不要自費，請直接問你的核子醫學科或個管師。」並請 E 組在 §九 補上查證結果。
9. **ESTIMABL2 與 IoN 的生活品質／成本子研究**——Europe PMC 以 `ISRCTN80416929` 與 ESTIMABL2 相關查詢皆未命中獨立的 QoL 或成本論文。**查無。**
10. **2020 年之後的 intersocietal working group 後續共識文件**——以 `"Martinique Principles"` 全文檢索（552 筆，逐筆篩選）與 `TITLE:"radioiodine" AND TITLE:"consensus"` 皆未命中 2020 年之後的第三份文件。**查無。**
11. **EANM 針對「分化型甲狀腺癌」的現行放射碘治療指引**——2023 年新版 EANM 放射碘指引（EJNMMI 2023;50(11):3324-3348）是**良性甲狀腺疾病**的，不可誤用；分化型甲狀腺癌的 EANM 指引仍是 2008 年版（EJNMMI 2008;35(10):1941-1959）。**⚠ 這兩份很容易被混用，請寫作組注意。**
12. **AJCC／TNM 版本**：ESTIMABL1（NEJM 2012）的納入條件在 ClinicalTrials.gov 與論文摘要中**皆未載明使用第幾版 TNM**。依 RESEARCH-COMMON §一.3，**該篇的任何期別描述都必須註明「原文未載明版本」**。ESTIMABL2 明載 TNM 2010（第七版），IoN 明載 TNM7 或 TNM8，HiLo 未於摘要載明版本（收案 2007–2010）。

---

## 給編輯的三個待裁決

1. **C1／C2 可否出現 1.1 GBq 與 3.7 GBq 作為 HiLo／ESTIMABL1 的識別特徵？**（⚠C-7）C 組傾向「不寫數值、寫『低活度組與較高活度組』」，但若編輯認為句子會變得難讀，請在 §九 明文豁免並限定只在 C1 出現。
2. **C2 可否出現「女性至少 6 個月、男性至少 120 天」這兩個建議間隔？**（C2 支點 7）C 組傾向可以寫，因為它們是指引的 Good Practice Statement、不是劑量也不是隔離天數，而且是病人真的要拿去問醫師的東西。請 §九 裁決。
3. **RESEARCH-COMMON §一.2 的「ATA 三級復發風險分層」需要改成四級並附百分比區間**（⚠C-2），這會影響 A、B、C、D 四組，請跨組統一後再動筆。
