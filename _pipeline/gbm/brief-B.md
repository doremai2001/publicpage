# Brief B — GBM 專題「治療與實證」群（B1–B5）

研究員：Group B｜查證日期：**2026-09-03**
期刊書目資料全部經 Europe PMC REST（`/webservices/rest/search?query=EXT_ID:<PMID>&resultType=core`）逐筆核對
（title／journal／year／volume(issue)／pages／DOI／PMID／isOpenAccess）；每一個要寫進 Key facts 的數字，
都在**摘要或可取得的全文**裡看得到，看不到的一律標明「取不到」。
指引引官方或期刊全文原文（EANO 2021 全文 XML、Cochrane 摘要、ClinicalTrials.gov API v2）。**未引用 NCCN。**
台灣端全部走官方 PDF／法規原文直連（健保署藥品給付規定第 9 節 PDF、支付標準全表 txt 匯出檔、
全國法規資料庫特管辦法與附表 PDF、衛福部醫事司公告附件）。

**引用規則：只有標 PASS 的來源可以進正文。** FAIL / NOT-CITABLE 條目保留在最後，讓寫作者知道查過什麼、
哪幾句只能寫「我查不到可以引用的來源」。**本 brief 的 [S1]…[S75] 編號與 Brief A 各自獨立、不共用。**

---

## ⚠ 與 SPEC 假設不同形狀的事（動筆前必讀，共 12 條）

> 每一條在下面篇章節裡有完整原文與 [Sn]；這裡只列「哪裡跟 SPEC 或直覺不一樣」。
> 另外請先讀 Brief A 開頭那一節（2021 WHO CNS5 的 GBM 定義、RANO resect 2023 只看術後殘餘體積、
> vorasidenib 監管落差）——B 組所有「GBM」的族群標籤都建立在 A 組那個定義上。

**1. NRG-BN001 已經有結果了，而且是 registry 上就查得到的完整結果。**
SPEC 把它寫成「進行中的劑量升高試驗」。實際狀態：ACTIVE_NOT_RECRUITING、預計 2026-12-31 結案、
**hasResults = True**，ClinicalTrials.gov 已張貼主要與次要終點[S7]。可分析 431 人。
光子中心組：標準 16.3 個月 vs 加量 18.8 個月，**HR 0.95（95% CI 0.81–1.10），log-rank p=0.25——沒有差別**。
質子中心組：標準 22.0 vs 加量 22.8 個月，HR 0.81（0.67–0.98），log-rank p=0.11[S7]。
→ B1 的「劑量升高」段落**必須從「等結果」改成「結果出來了，光子那一半是陰性」**。
→ 而且這是 B5 質子段最重要的一條：**BN001 不是質子對光子的隨機比較**（見第 2 條）。

**2. BN001 的質子數字看起來比較好，但那是中心之間的比較，不是隨機分派的比較。**
BN001 是**在每一個中心組內部**各自隨機（光子中心：標準 vs 加量；質子中心：標準 vs 加量），
兩個實驗組彼此的比較是次要終點，且規約寫明「**只有在兩個實驗組都各自打敗自己的對照組時才做**」——
條件沒有成立，**這個比較沒有執行**[S7]。關鍵事實：質子中心的**兩組**（22.0 與 22.8 個月）都高於
光子中心的**兩組**（16.3 與 18.8 個月）——**連對照組都比較高**，這是中心／收案族群的差異，不是射線的功勞。
另外 registry 自陳限制：「質子中心收案比預期慢，因此縮小目標樣本數、延長追蹤、重算檢定力」[S7]。
→ B5 質子段的正確寫法：「有一個把質子放進來的隨機試驗，它證明的是**加量沒有用**；至於質子本身好不好，
它沒有設計來回答，而且它的數字剛好示範了為什麼不能直接比中心。」

**3. 「未甲基化的人做 TMZ 有沒有效」——EORTC 原始數據裡 OS 沒差，但 PFS 差很多。**
EORTC 26981-22981 的回溯分層（原始數字經 OA 全文轉引可驗）：未甲基化者
**OS 放療 11.8 個月（9.7–14.1，n=54）vs 放療+TMZ 12.7 個月（11.6–14.4，n=60），沒有統計差異**；
但同一群人的 **PFS 是 5.9 個月（5.3–7.7，n=46）vs 10.3 個月（6.5–14，n=46）**[S18]。
SPEC 假設這題是「有小獲益 vs 無獲益」的二選一；真實形狀是**三層**：OS 看不出來、PFS 明顯、
而高齡族群（Perry）的 OS 差異是 10.0 vs 7.9 個月、HR 0.75（0.56–1.01）、**p=0.055 剛好沒過**[S29]。
→ B2 的紅線段必須把 OS 與 PFS 分開講，不能合併成一句「有沒有效」。

**4. 台灣健保的 temozolomide 條文裡，沒有「六個月」「六個療程」這個東西。**
現行條文（自 111/9/1 生效）只寫「新診斷的多形神經膠母細胞瘤，與放射線治療同步進行，然後作為輔助性治療」，
加上「**需經事前審查核准後使用，每日最大劑量 200mg/m2。每次申請事前審查之療程以三個月為限，
再次申請必須提出客觀證據（如：影像學）證實無惡化，才可繼續使用**」[S70]。
→ 病人實際會遇到的是「**每三個月一關、要拿影像去換下一段**」，不是「講好六個月」。
B1 講療程時間軸時這一句很重要，因為它跟 D1 的追蹤 MRI 是同一件事的兩面。

**5. 延長維持期到 12 個月，兩個層級的證據都說「不會活比較久」。**
四個隨機試驗的個別病人資料合併分析（n=624 符合資格）：超過 6 個療程者 PFS 略好
（HR 0.80，0.65–0.98，P=.03；甲基化亞群 HR 0.65，0.50–0.85，P<.01），但 **OS 沒有差別
（HR 0.92，0.71–1.19，P=.52）**[S11]。西班牙 GEINO 14-01 隨機試驗（n=159）：6 個月 PFS
55.7% vs 61.3%，**PFS、OS 都沒有差別，淋巴球低下、血小板低下、噁心嘔吐都顯著較多**[S12]。
→ B1 可以正面回答門診最常被問的「可不可以多吃幾個月」。

**6. 高齡篇的骨架不是三個試驗，是五個，而且有一個更根本的問題在最前面。**
SPEC 列的 Roa 2004／Roa 2015／Nordic／NOA-08／Perry 2017 都對，但**前面少了一個**：
Keime-Guibert 2007 NEJM 隨機把 ≥70 歲、KPS ≥70 的病人分到「只做支持性照護」與「放療 50 Gy + 支持性照護」，
中位存活 **16.9 週 vs 29.1 週，HR 0.47（0.29–0.76），p=0.002**，試驗在第一次期中分析就因效果達標而停止[S30]。
→ B3 的第一句不是「可以縮短」，是「**先確定要不要治療**，而這一題有隨機試驗，答案是要」。
不先立這一條，「縮短療程」很容易被讀成「反正差不多，那就不要治了」。

**7. 「短程放療不輸標準放療」在高齡族群是高確定性證據，但只在特定條件下成立。**
Cochrane 2020：低分次 vs 常規分次整體 HR 0.95（0.78–1.17），證據等級**極低**；
但限定在「≥60 歲的 GBM」這個亞組（2 個試驗、293 人）HR 1.16（0.92–1.46），證據等級**高**[S5]。
→ 正確措辭是「**在六十歲以上的膠質母細胞瘤，短療程與長療程的存活看不出差別，這一條的證據是高等級的**」，
不能寫成通則。同一份 Cochrane 也給了「放療 vs 不放療」的合併 HR 2.01（1.58–2.55）[S5]，可與第 6 條並用。

**8. 免疫治療三個第三期不只是「沒有比較好」，其中一個是「比較差」。**
CheckMate-498（新診斷、MGMT 未甲基化，n=560）：nivolumab+放療 13.4 個月 vs TMZ+放療 14.9 個月，
**HR 1.31（1.09–1.58），P=.0037——這是統計上顯著地比較差**[S54]。
CheckMate-548（甲基化，N=716）：OS 28.9 vs 32.1 個月，HR 1.1（0.9–1.3），且 grade 3/4 治療相關不良事件
**52.4% vs 33.6%**[S55]。CheckMate-143（復發，n=369）：OS 9.8 vs 10.0 個月，HR 1.04（0.83–1.30），P=.76；
但**客觀緩解率 nivolumab 7.8% vs bevacizumab 23.1%**[S56]。
→ 紅線 7 的「負的就寫負的」在這裡要更狠一格：其中一個試驗的方向是**反向且顯著**。

**9. DCVax-L 的問題不只是「外部對照」，是整個試驗設計在中途換掉了。**
可引用的同儕評議批評（OA）指出：原始主要終點是 PFS；因為設計允許 crossover，**兩組合計約 90% 的病人
最後都用到了 DCVax-L**，安慰劑組被掏空；主要終點於是**從 PFS 改成 OS**，對照組改用文獻回顧選出的
其他隨機試驗對照組、以 matching-adjusted indirect comparison 校正；作者群自己的結論是
「**經過設計與主要終點的修改之後，這個研究等於是一個帶外部對照的非隨機單臂試驗**」[S58]。
而且**最後公布的 PFS 數字是 DCVax-L 比較差：6.2 vs 7.6 個月（p=0.47）**[S58]。試驗 2007 年開始、
2008–2011 年因財務因素中止、約 90% 的病人是 2012–2015 年才隨機分派的[S58]。
→ B5 不能只寫「外部對照有爭議」，要寫「換終點、換對照、九成的人兩組都吃到了藥」。

**10. TTFields 的「每天戴幾小時」次族群分析，方向與 SPEC 的直覺一致，但它是預後、不是療效。**
Toms 2019（EF-14 事後次族群）：>90% 配戴率者中位存活 24.9 個月（自診斷起 28.7 個月）、
5 年存活率 29.3%；≥75% vs <75% 的 OS HR 0.78，p=0.031，且在校正性別、切除程度、MGMT、年齡、
地區、體能狀態後仍成立[S52]。**作者用的字是 prognostic（預後），不是 predictive**。
→ 站上〈貼片〉已經立過這條線，B5 沿用同一措辭，不得更寬鬆。
**新增可查證事實**：TRIDENT／EF-32（TTFields 與放療同步，n=981）在 ClinicalTrials.gov 上
**狀態 COMPLETED、主要完成日 2026-02-19、尚未張貼結果、Europe PMC 查不到正式論文**[S53]。
→ 「還有一個更大的試驗剛做完、還沒公布」是 2026 年 9 月的正確現況。

**11. 台灣端的三個查證，兩個查到了、一個查不到，而且質子那個查到的東西比預期硬。**
✅ **TTFields 沒有健保代碼**：2026-09-03 匯出健保署「醫療服務給付項目及支付標準」全表（5,995 筆），
搜「電場」**零筆**；「中子」「硼」也各零筆[S71]。**特管辦法附表二**（114/12/31 修正、115/1/1 施行）
的特定醫療儀器清單裡，有「質子機」與「重粒子治療設備」，**沒有任何交流電場類設備**[S72]。
→ 與站上〈貼片〉2026-08-30 的查證一致，重新確認通過，本專題沿用、一句指路、不重寫。
❌ **TTFields 的食藥署醫療器材許可證**：查不到（食藥署許可證查詢站台在本次連線被拒，
無法取得官方頁面）→ **寫「我查不到可以引用的官方資料」，永不推論有無**[FAIL-3]。
✅ **質子在台灣的官方身分比想像的清楚**：支付標準全表裡質子有 **N21301–N21308 八個代碼、
支付點數全部為 0、備註欄標「HTA項目」、自 105/12/05 起**[S71]；特管辦法附表二把質子機列為
特定醫療儀器，並要求機構「**依中央主管機關規定，收受符合醫用粒子治療適應症之病人、收費及
對治療後病人之追蹤管理**」[S72]；衛福部公告的官方同意書範本裡，費用欄位就叫「**自費費用**」[S73]。
**但那份公告的說明書沒有列出任何適應症清單，也沒有提到膠質母細胞瘤**[S73]。

**12. 衛福部自己的官方同意書範本，對質子的療效講得比任何廣告都保守——這句可以直接引。**
「**目前對於治療效果(腫瘤縮小)，僅有間接證據支持醫用粒子(質子/重粒子)放射治療優於傳統放射線治療，
直接證據(前瞻比較性臨床試驗)正在進行中。**」以及「**目前世界各國對醫用粒子(質子/重粒子)放射治療的
使用上較有共識是適用於治療局限性的腫瘤或傳統放射治療有效的其他臨床狀況。**」[S73]
→ 這是 B5 質子段最有力的一句台灣端引語：不是我說的，是主管機關印在同意書上要醫師唸給你聽的。

---

## gb-standard〈六週同步，六個月維持：標準治療長什麼樣〉（B1）

> 本篇有利益揭露段（SPEC §二，逐字）。

### Key facts

**A. Stupp 2005 主論文——設計、族群、劑量（每個數字都在摘要裡）**[S1]

- **試驗身分**：EORTC 26981-22981／NCIC CE.3，隨機、第三期，**85 個中心、573 人**，
  收案期間 2000-08-17 至 2002-03-22（收案期出自五年追蹤論文[S2]）。主要終點：整體存活。
- **族群標籤**：新診斷、組織學確認的 glioblastoma（**2005 年的組織學定義，不是 2021 WHO CNS5 的分子定義——
  見 Brief A**）；**中位年齡 56 歲**；**84% 接受過減積手術**（其餘為切片）。
- **放療（兩組相同）**：「fractionated focal irradiation in daily fractions of 2 Gy given 5 days per week
  for 6 weeks, for a total dose of **60 Gy**」——**每天 2 Gy、一週五天、六週、總共 60 Gy／30 次**[S1]。
- **同步期（concomitant）**：temozolomide **75 mg/m²/天**，**一週七天**（含週末），
  「from the first to the last day of radiotherapy」——**放療第一天吃到最後一天，中間不停**[S1]。
  EANO 2021 的措辭一樣：「75 mg/m² daily throughout radiotherapy, **including at weekends**」[S13]。
- **維持期（adjuvant/maintenance）**：**六個療程**，每個療程 28 天，**每個療程只吃 5 天**，
  劑量 **150–200 mg/m²**[S1][S13]。
- **同步期與維持期之間有一段休息**：CheckMate-548 的試驗規約把標準治療寫成
  「TMZ 75 mg/m² QD during RT, **then 4-week break**, then 150–200 mg/m² QD on days 1–5 of every
  28-day cycle for 6 cycles」[S15]；GBM AGILE 的對照組寫「**Rest Period 2–6 weeks** from the last day
  of radiation, and the start of the first cycle of Maintenance Therapy」[S16]。
  → **四週是規約常用值，但範圍是 2–6 週**，正文要這樣寫，不要寫死。
- **結果**：中位追蹤 28 個月時，**中位存活 14.6 個月 vs 12.1 個月**；
  **HR 0.63（95% CI 0.52–0.75），P<0.001**（log-rank）；**兩年存活率 26.5% vs 10.4%**[S1]。
- **毒性**：**同步期的 grade 3 或 4 血液毒性 7%**[S1]。作者結論用的字是
  「clinically meaningful and statistically significant survival benefit **with minimal additional toxicity**」[S1]。

**B. Stupp 2009 五年追蹤——尾巴的實際比例**[S2]

- 中位追蹤超過 5 年。**放療組 286 人中 278 人（97%）死亡；合併治療組 287 人中 254 人（89%）死亡**。
- 合併治療組：**2 年 27.2%（22.2–32.5）、3 年 16.0%（12.0–20.6）、4 年 12.1%（8.5–16.4）、
  5 年 9.8%（6.4–14.0）**。
- 單獨放療組：**2 年 10.9%（7.6–14.8）、3 年 4.4%（2.4–7.2）、4 年 3.0%（1.4–5.7）、
  5 年 1.9%（0.6–4.4）**。**HR 0.6（0.5–0.7），p<0.0001**[S2]。
- 作者原話兩句，都要用：「**A benefit of combined therapy was recorded in all clinical prognostic
  subgroups, including patients aged 60–70 years.**」與「**A few patients in favourable prognostic
  categories survive longer than 5 years.**」[S2]
- MGMT 是回溯測的，**只有 206 人的檢體可測**（見 B2）[S2]。

**C. 為什麼是 60 Gy——劑量反應的歷史證據，以及「再高沒有更好」的證據**

- **劑量有反應**（往上到 60 Gy 這一段是真的）：EANO 2021 的敘述句可直接引——
  「For decades, radiotherapy (**60 Gy in 1.8–2 Gy fractions**) has been the standard of care for
  glioblastoma, **approximately doubling median OS durations**」[S13]。
- **可引用的隨機劑量比較**：MRC BR2（Bleehen & Stenning 1991，OA），474 位 grade 3/4 astrocytoma，
  2:1 隨機到 **60 Gy／30 次／6 週（318 人）vs 45 Gy／20 次／4 週（156 人）**，未給輔助化療。
  結果：**中位存活 45 Gy 組 9 個月 → 60 Gy 組 12 個月，HR 0.75，χ²=7.36，P=0.007**；
  「Over 80% of patients reported no morbidity from the radiotherapy, and there was no evidence of
  increased short-term morbidity in the higher dose group. **Late morbidity was not assessed.**」[S3]
  → 這是「為什麼不是 45 Gy」最乾淨的一筆隨機證據。
- **再往上加，四個層級的證據都說沒有更好**：
  1. **加立體定位放射手術當 boost**：RTOG 93-05（n=203，腫瘤 ≤40 mm，SRS 15–24 Gy 後接 60 Gy + BCNU
     vs 60 Gy + BCNU）：中位存活 **13.5 個月（11.0–14.8）vs 13.6 個月（11.2–15.2），p=0.5711**；
     2 年、3 年存活率與失敗型態都沒有差別；生活品質與認知功能的惡化程度相當[S6]。
  2. **改分次方式**：Cochrane 2020（11 個隨機試驗、2,062 人）：超分次與加速放療對常規分次的資料
     「could not be pooled」——**證據不足以下結論**[S5]。EANO：「Neither accelerated hyperfractionated
     or hypofractionated regimens nor brachytherapy, radiosurgery or a stereotactic radiotherapy boost
     are superior to standard radiotherapy regimens in terms of OS」[S13]。
  3. **在術中直接加一劑**：INTRAGO-II（2026 Lancet Oncol，18 個中心、7 國、隨機第三期，
     術中放療 30 Gy + 標準治療 vs 標準治療，full-analysis set 298 人）：
     **中位 PFS 11.0 個月（9.2–12.6）vs 11.4 個月（9.7–13.9），HR 1.1（0.85–1.44），p=0.47**；
     局部復發仍是主要失敗型態（72% vs 71%）；**放射性壞死 11 例（7%）vs 3 例（2%），p=0.06**。
     作者結論原文：「did not improve outcomes, **questioning the value of further local dose
     intensification in resectable glioblastoma**」[S8]。
  4. **NRG-BN001（見下）**。

**D. NRG-BN001 現況（ClinicalTrials.gov API v2 查證，2026-09-03）**[S7]

- **NCT02179086**｜Randomized Phase II Trial of Hypofractionated Dose-Escalated Photon IMRT or Proton
  Beam Therapy Versus Conventional Photon Irradiation With Concomitant and Adjuvant Temozolomide in
  Patients With Newly Diagnosed Glioblastoma。
- **狀態 ACTIVE_NOT_RECRUITING**；最後更新 2026-08-28；狀態驗證 2026-06；
  開始 2014-12-04；主要完成 2025-07-07；預計結案 2026-12-31；**實際收案 624 人**；**hasResults = True**。
- **設計**（這一段決定了它能證明什麼）：**兩個中心組各自獨立隨機**——
  Group 1 = 光子 IMRT 中心（Arm A1 標準 vs Arm B 加量），Group 2 = 質子中心（Arm A2 標準 vs Arm C 加量）；
  組內 **1:2 隨機、偏向實驗組**；檢定力 80%、假設風險降低 28%、**單尾 type I error 0.15**。
  加量臂：**選擇性標的 50 Gy(RBE)／30 次，boost 標的 75 Gy(RBE)／30 次**。
- **分析人數 431**（A1 94、B 144、A2 77、C 116）；中位追蹤 Group 1 為 16.2 個月、Group 2 為 18.3 個月。
- **主要終點（各組內比較）**：
  - Group 1（光子）：**16.3 個月（14.0–20.5）vs 18.8 個月（16.0–23.9）；HR 0.95（0.81–1.10），
    log-rank p=0.25**。
  - Group 2（質子）：**22.0 個月（15.8–27.8）vs 22.8 個月（20.0–28.6）；HR 0.81（0.67–0.98），
    log-rank p=0.11**。
- **次要終點 PFS**：Group 1 為 6.3 vs 6.5 個月（HR 1.19，0.90–1.57，p=0.29）；
  Group 2 為 8.3 vs 8.8 個月（HR 1.00，0.71–1.40，p=0.99）[S7]。
- **兩個實驗臂之間的比較（質子 vs 光子）**：規約寫明「**只有在兩個實驗臂都各自顯著優於自己的對照臂時
  才進行**」，條件未成立，**該分析沒有執行**，registry 對應欄位是空的[S7]。
- **registry 自陳限制**（原文）：「Due to slower than anticipated accrual in Group 2 (proton centers),
  the target sample size was reduced, follow-up duration was increased, and the power calculations
  were revised accordingly」[S7]。
- 期中的認知功能次要終點（光子組，SNO 2020 會議摘要）：**兩組在 cycle 3 與 cycle 12 的
  Clinical Trial Battery Composite 變化沒有差別**（p=0.370 與 p=0.977）[S67]。

**E. 治療中斷與延遲——有 GBM 自身資料，但只有「開始時間」這一種**

- **開始放療的時間**：Blumenthal 2009 JCO，RTOG 資料庫 1974–2003 年 16 個試驗、2,855 位
  幕上 glioblastoma，依手術到放療的間隔分四組（≤2 週、2–3 週、3–4 週、>4 週至規約上限 6 週）。
  結果：**沒有看到延後開始放療會讓存活變差**；反而**間隔最長那一組（>4 週）的中位存活顯著高於
  最短那一組（≤2 週）：12.5 個月 vs 9.2 個月，P<.0001**；多變項分析中，間隔 >4 週與較好的 RPA
  分級都是較佳存活的預測因子[S9]。
  **必寫的解讀**：這是回溯次級分析、且**收案本來就限制在六週內**；「拖久一點反而好」幾乎確定是
  選擇偏差（狀況差、術後恢復不良的人會被更早排進放療），**不可寫成「晚一點開始比較好」**。
  作者自己的結論句只到「There is no evident reduction in survival by delaying initiation of RT
  **within the relatively narrow constraint of 6 weeks**」[S9]。
- **同方向的第二筆**：巴西雙機構回溯（n=115），中位等待 6 週（範圍 1.3–17.6 週）：
  ≤6 週 13.5 個月（9.1–17.9）vs >6 週 14.2 個月（11.2–17.2），HR 1.165（0.770–1.762），p=0.470；
  多變項中與存活相關的是 **KPS、切除程度、輔助治療**，不是等待時間[S10]。
  作者原話：「**Although there are no data to ensure that delays to RT are tolerable**, we may reassure
  patients that the time-length to initiate treatment does not seem to influence the control of the
  disease」[S10]。
- **療程中間斷掉幾天會怎樣（overall treatment time / treatment interruption）**：
  **在 GBM 沒有可引用的專門研究。** Europe PMC 以 `TITLE:"interruption" AND TITLE:"glioblastoma"`、
  `TITLE:"overall treatment time" AND TITLE:"glioblastoma"` 查詢，**命中數皆為 0**[FAIL-5]。
  → 正文只能寫：「**放療中間停幾天會不會有影響，膠質母細胞瘤自己沒有可以引用的資料**；
  我能給你的只有『開始的時間在六週內不影響存活』這一條，以及一句臨床上的常識——
  能不停就不停，真的要停由團隊決定怎麼補。」**不可以借用其他癌別的 overall treatment time 資料**。

**F. 為什麼是六個月，不是十二個月**

- **合併分析（四個隨機試驗的個別病人資料）**：2,214 位新診斷 GBM 中，符合資格者 624 人
  （第 6 個療程後 28 天仍無惡化）：**291 人繼續用到惡化或最多 12 個療程、333 人在 6 個療程後停藥**。
  校正年齡、體能狀態、切除程度、MGMT 之後：**PFS 略好（HR 0.80，0.65–0.98，P=.03；
  甲基化亞群 n=342，HR 0.65，0.50–0.85，P<.01）；OS 沒有受影響（HR 0.92，0.71–1.19，P=.52），
  甲基化亞群亦然（HR 0.89，0.63–1.26，P=.51）**。作者結論：「**Continuing TMZ beyond 6 cycles was
  not shown to increase overall survival**」[S11]。**注意**：是否繼續由當地醫師決定，不是隨機的[S11]。
- **隨機試驗**：GEINO 14-01（西班牙 20 家醫院，第二期隨機，n=159；6 個療程後未惡化者隨機分到停藥或
  續用到 12 個療程）：主要終點 **6 個月 PFS 55.7%（停）vs 61.3%（續），沒有差別**；PFS、OS 亦無差別；
  **續用組的淋巴球低下（P<0.001）、血小板低下（P<0.001）、噁心嘔吐（P=0.001）都顯著較多**。
  作者結論：「**greater toxicity but confers no additional benefit**」[S12]。
  獨立預後因子是 **MGMT 甲基化與沒有可測量病灶**[S12]。

**G. 指引原文（EANO 2021，可逐字引用）**[S13]

- 「The standard of care for patients with **IDH-wild-type glioblastoma aged <70 years and with a
  KPS > 70** includes resection as feasible or biopsy followed by involved-field radiotherapy and
  concomitant radiotherapy and **six cycles of maintenance temozolomide chemotherapy**
  (EORTC 26981-NCIC CE.3). **C: I; L: A.**」
- 「Concomitant radiotherapy and chemotherapy with temozolomide (75 mg/m² daily throughout radiotherapy,
  including at weekends) plus six cycles of maintenance temozolomide (150–200 mg/m², 5 out of 28 days)
  is the standard of care for adults with newly diagnosed glioblastoma who are in good general and
  neurological condition and are **aged <70 years**」
- 「Radiotherapy (50 Gy in 1.8 Gy fractions) improved OS relative to best supportive care in patients
  **aged ≥70 years with a good KPS (≥70)**」（指向 Keime-Guibert[S30]）

### 反方向的資料（誠實必列）

- Stupp 2005 的效果量放在絕對值上是 **2.5 個月的中位差**；作者自己寫的是「clinically meaningful」，
  不是「大幅延長」。要跟 B4 的讀法一起講。
- **Stupp 2005 的族群不是今天定義下的 GBM**：2000–2002 年收案，依組織學診斷，**沒有 IDH 檢測**。
  依 Brief A 的 CNS5 定義，其中一部分今天會被改叫 *Astrocytoma, IDH-mutant, grade 4*——
  那是預後較好的一群。**所以那條曲線的尾巴，有一部分不是今天的 GBM 病人**（見 B4）。
- 60 Gy 的證據強度分層要誠實：45→60 Gy 有隨機證據[S3]；60 Gy 以上的每一種加量嘗試，
  到 2026 年為止都是陰性或無法下結論[S5][S6][S7][S8]。
- MRC BR2「**Late morbidity was not assessed**」[S3]——「更高劑量沒有更多短期副作用」不能延伸成
  「沒有長期副作用」，這一句跟 D2 的認知副作用要接得上。

### Claim ceiling（B1）

- **可寫**：「同步期是六週、天天吃（含週末）、劑量 75；維持期是六個療程、每個療程 28 天只吃 5 天、
  劑量 150–200；中間隔 2–6 週」[S1][S13][S15][S16]；「加上 temozolomide，中位存活從 12.1 到 14.6 個月，
  兩年存活率從 10.4% 到 26.5%，五年 1.9% 到 9.8%」[S1][S2]；「60 Gy 這個數字有隨機試驗撐著——
  45 Gy 對 60 Gy，中位存活 9 個月對 12 個月」[S3]；「往上加劑量的每一種做法，到目前為止都沒有做出更好的結果，
  包含 2026 年剛發表的術中放療試驗與已張貼結果的 NRG-BN001 光子組」[S6][S7][S8]；
  「維持期延長到 12 個月，PFS 略好、整體存活沒有差別、副作用比較多」[S11][S12]；
  「手術到放療的間隔在六週內，看不出對存活的影響」[S9][S10]。
- **不可寫**：
  - 「延後開始放療比較好」——那是選擇偏差，Blumenthal 自己只說「六週內看不出減損」[S9]。
  - 「療程中間停幾天沒關係」或「停幾天會怎樣」的任何具體說法——**GBM 沒有這個資料**[FAIL-5]。
  - 「劑量再高一點也許對某些人有用」——BN001 的質子組數字**不是**這句話的證據（見不同形狀 2）。
  - 任何把 14.6 個月當成個人期限的句子；本篇出現存活數字時**一律接一句指向 B4**（SPEC §六）。
  - 「同步期的化療很輕」——原文是 grade 3/4 血液毒性 7%，要照數字寫，不加形容詞[S1]。
  - 不可寫「六個月做完就結束了」——台灣的事前審查是**三個月一關**（見台灣端）[S70]。

### Caveats／safety notes（寫作者必寫）

1. **同步期與維持期是兩種不同的吃法，病人最常搞混的是「週末要不要吃」**：同步期**含週末**、
   天天吃；維持期是**28 天裡只吃 5 天**[S1][S13]。這一段建議用表格或圖，配合 `fig-gb-timeline`。
2. **同步期的血球監測與感染警訊**歸 C4，本篇一句帶過並指路〈哪些狀況要當天回來〉。
3. **不可自行決定停藥或補藥**。台灣的事前審查每三個月要重新申請、要附影像[S70]，
   所以「這次 MRI 排在什麼時候」不只是追蹤問題，也是拿藥問題——這句要跟 D1 對得起來。
4. 本篇有**利益揭露段**（SPEC §二逐字）：放療是作者自己做的那一段。
5. 「一半的人在中位數之前」這句話**不要在 B1 說完**，留給 B4；B1 只交代治療長什麼樣。

### 台灣端（B1 主場之一）

**temozolomide 健保給付條文（現行，逐字）**——健保署「藥品給付規定」第 9 節 抗癌瘤藥物，
9.25 Temozolomide（如 Temodal），**生效沿革標示 94/3/1、97/1/1、98/9/1、111/9/1，附表八之二**[S70]：

> 限用於
> 1.經手術或放射線治療後復發之下列病人：
> 　(1)退行性星狀細胞瘤(AA-anaplastic astrocytoma)
> 　(2)多形神經膠母細胞瘤(GBM-Glioblastoma multiforme)
> 　(3)退行性寡樹突膠質細胞瘤(anaplastic oligodendroglioma)(98/9/1)
> 2.新診斷的多形神經膠母細胞瘤，**與放射線治療同步進行，然後作為輔助性治療**。（97/1/1）
> 3.**需經事前審查核准後使用，每日最大劑量200mg/m2。每次申請事前審查之療程以三個月為限，
> 　再次申請必須提出客觀證據（如：影像學）證實無惡化，才可繼續使用。**(98/9/1、111/9/1)

- **條文的三個可用重點**：(a) 條文本身就把「同步」與「輔助（維持）」寫成兩段，
  跟 Stupp 的兩段完全對應；(b) **條文沒有寫幾個療程、沒有寫六個月**；
  (c) 真正的節奏器是「**三個月一關 + 影像證明沒有惡化**」。
- **條文用的病名是舊的**（「多形神經膠母細胞瘤」＝ glioblastoma multiforme，
  以及已被 2021 WHO CNS5 刪除的「退行性星狀細胞瘤」「退行性寡樹突膠質細胞瘤」）。
  → 可以誠實寫：**分類 2021 年改了，健保條文還停在舊名字**，這跟 Brief A 第 4 條（美國登記也還在追）
  是同一個現象。**但不可以據此推論給付範圍變寬或變窄**。

**放療的健保代碼**：支付標準全表中與 GBM 常規療程相關者為
36012B「直線加速器遠隔照射治療，每一複雜照野」1,334 點、36015B「電腦治療規劃--複雜」11,483 點、
36021C「3D電腦斷層模擬攝影」8,500 點、36018B「模擬定位攝影」3,619 點、
37016B/37030B「固定模具之設計及製作（大／小）」1,943／1,657 點等[S71]。
**全表中沒有「強度調控放射治療」的獨立項目名稱**（該詞只出現在 36015B 的說明文字裡）[S71]。
→ 正文不必列代碼，**若要提，只能提到「放療本身是健保給付項目」這個層次**；細目請問醫務課。

**查不到的**：台灣癌症登記的腦瘤／GBM 發生數（Brief A 已標 FAIL）；GBM 病人實際完成六個療程的比例
（無台灣資料）[FAIL-6]。

### 給繪圖組的數字（`fig-gb-timeline`）

- 手術 →（間隔，資料支持 ≤6 週不影響存活[S9][S10]）→ **同步期 6 週：放療 2 Gy × 30 次 = 60 Gy，
  週一至週五；TMZ 75 mg/m²，一週七天**[S1]
- → **休息 2–6 週（規約常寫 4 週）**[S15][S16]
- → **維持期 6 個療程，每療程 28 天，只有第 1–5 天吃 TMZ 150–200 mg/m²**[S1]
- 側欄可放：**台灣健保事前審查每 3 個月一關，續用要附影像**[S70]
- 側欄可放：**延長到 12 個療程：PFS 略好、OS 一樣、副作用較多**[S11][S12]（不要畫成第二條主線）

---

## gb-mgmt〈MGMT 那一行，決定什麼、不決定什麼〉（B2）

> **紅線所在**：「未甲基化的人做 TMZ 到底有沒有效」必須把「有獲益但較小」與「沒有獲益」的證據
> **分開列**，而且要把 **OS 與 PFS 分開**（見不同形狀 3）。
> 報告怎麼讀（IDH／MGMT／1p19q 的檢測本身）歸 A4；本篇只寫**它對治療決策決定什麼**。

### Key facts

**A. Hegi 2005 NEJM——原始的分層結果**[S17]

- **族群**：EORTC 26981-22981／NCIC CE.3 的檢體回溯分析；**206 例可判讀**；
  檢測方法 **methylation-specific PCR（MSP）**。
- **甲基化比例：206 例中 45%**[S17]。
- **MGMT 甲基化本身是預後因子（與治療無關）**：「Irrespective of treatment, MGMT promoter methylation
  was an independent favorable prognostic factor（P<0.001 by the log-rank test; **hazard ratio, 0.45;
  95% CI, 0.32 to 0.61**）」[S17]。
- **甲基化的人加 TMZ**：中位存活 **21.7 個月（17.4–30.4）vs 15.3 個月（13.0–20.9），P=0.007**[S17]。
- **未甲基化的人加 TMZ（摘要原文）**：「In the absence of methylation of the MGMT promoter, there was
  a **smaller and statistically insignificant** difference in survival between the treatment groups.」[S17]
- 作者結論句（常被過度引用的那一句）：「Patients with glioblastoma containing a methylated MGMT promoter
  benefited from temozolomide, **whereas those who did not have a methylated MGMT promoter did not have
  such a benefit**.」[S17]

**B. 未甲基化那一格的實際數字——這是本篇的核心，四層證據**

**第一層｜EORTC 原始分層的實際數字**（Hegi 2005 的分層數字，經 OA 全文轉引可驗）[S18]：
- **OS**：放療單獨 **11.8 個月（9.7–14.1），n=54**；放療 + TMZ **12.7 個月（11.6–14.4），n=60**
  → **信賴區間大幅重疊，沒有統計差異**。
- **PFS**：放療單獨 **5.9 個月（5.3–7.7），n=46**；放療 + TMZ **10.3 個月（6.5–14），n=46**
  → **差了將近一倍，但人數很少、區間很寬**。
- → 誠實的一句：「**在未甲基化的人身上，TMZ 讓腫瘤晚一點長回來這件事是看得到的；
  讓人活得比較久這件事，這個試驗看不出來。**」

**第二層｜統合分析：沒有人做過「未甲基化：放療 vs 放療+TMZ」的前瞻隨機比較**[S18]
- Alnahhas 2020（Neuro-Oncology Advances，OA）系統回顧與統合分析，只納入第三期試驗：
  - **未甲基化、接受放療 + TMZ**（5 個第三期試驗、**N=655**）：
    **中位 OS 14.11 個月（95% CI 13.18–15.04）；中位 PFS 4.99 個月（4.25–5.72）**。
  - **甲基化、接受放療 + TMZ**（6 個試驗、**N=753**）：
    **中位 OS 24.59 個月（22.19–26.99）**；PFS（7 個試驗、N=805）**9.51 個月（7.41–11.61）**。
  - **高齡、未甲基化、只做放療**（NOA-08、Nordic、Perry 三個試驗的放療臂合併，**N=223**）：
    **中位 OS 8.35 個月（6.46–10.25）**。
- 作者的三句關鍵原文（**全部可引**）：
  1. 「**no study has prospectively compared RT versus RT plus TMZ in the MGMT unmethylated GBM subgroup**」
  2. 「**There is paucity in historic data to drive any conclusions regarding withholding TMZ in unmethylated
     GBM, including the elderly with good functional status.**」
  3. 「Median survival differs vastly between MGMT methylated and unmethylated GBM and **estimates from this
     analysis should be cited when discussing prognosis with patients**.」[S18]
- 作者自己的實務立場（也可引，因為它示範了「證據不足時醫師怎麼決定」）：
  「we have otherwise **continued to treat 'low-risk', non-elderly patients with unmethylated MGMT gene
  promoter GBM with RT and TMZ** based on a small improvement in median survival over RT alone noted in
  our analysis」；同時認為在「有顯著共病、化療風險較高的高齡未甲基化病人」身上排除 TMZ「appears
  reasonable」[S18]。

**第三層｜高齡族群裡最接近直接答案的隨機數字**（Perry 2017 CE.6）[S29]
- **未甲基化亞群（n=189）**：短程放療 + TMZ **10.0 個月** vs 短程放療 **7.9 個月**；
  **HR 0.75（95% CI 0.56–1.01），P=0.055；交互作用 P=0.08**。
- **甲基化亞群（n=165）**：**13.5 個月 vs 7.7 個月；HR 0.53（0.38–0.73），P<0.001**[S29]。
- → **這是全部證據裡唯一一組「同一個試驗、同一個放療劑量、只差有沒有加 TMZ」的未甲基化隨機數字。**
  它的方向偏向有益，**但沒有跨過統計顯著的線**。這句要一字不改地寫給讀者。

**第四層｜「不吃 TMZ 反而比較好」的資料（NOA-08 的方向）**[S28]
- NOA-08（>65 歲、KPS ≥60，TMZ 單獨 vs 放療 60 Gy 單獨；**注意這裡沒有合併治療組**）：
  **未甲基化者的 EFS，做放療的比做 TMZ 的長：4.6 個月（3.7–6.3）vs 3.3 個月（3.0–3.5）**；
  甲基化者則相反：TMZ **8.4 個月（5.5–11.7）** vs 放療 **4.6 個月（4.2–5.0）**[S28]。
- → 這條的正確讀法是「**未甲基化的人如果只能選一種，選放療**」，
  **不是**「未甲基化的人吃 TMZ 有害」。兩者差別很大，必須寫清楚。

**C. MGMT 是預後因子，也是療效預測因子——兩件事要分開**

- **預後（不管做什麼治療都比較好）**：Hegi 2005 的 HR 0.45（0.32–0.61），與治療無關[S17]。
- **在都有做 TMZ 的族群裡，仍然是強預後因子**：RTOG 0525（n=833，兩組都有 TMZ，比的是標準 vs 高密度給法）：
  **甲基化 vs 未甲基化：OS 21.2 vs 14.0 個月，HR 1.74，P<.001；PFS 8.7 vs 5.7 個月，HR 1.63，P<.001；
  緩解率也較好（P=.012）**；而**高密度 TMZ 在兩種 MGMT 狀態下都沒有做出更好的結果**
  （OS 16.6 vs 14.9 個月，HR 1.03，P=.63；grade ≥3 毒性 34% → 53%，P<.001）[S22]。
- **在只做放療的族群裡也仍然是預後因子**：Nordic 試驗中，接受**放療**者的甲基化與未甲基化
  **沒有差別（HR 0.97，0.69–1.38，p=0.81）**；接受 **TMZ** 者則有差別（9.7 vs 6.8 個月，
  HR 0.56，0.34–0.93，p=0.02）[S27]。
  → **這一組對照剛好示範了什麼叫「療效預測因子」**：它只在用烷化劑的人身上把兩群人分開。
  這是 B2 最好的教學材料，比任何比喻都準。

**D. MGMT 甲基化在治療決策上真正決定的第三件事：它決定你有沒有資格走另一條路**

- **CeTeG／NOA-09**（Lancet 2019）：**只收 MGMT 甲基化**、18–70 歲、KPS ≥70 的新診斷 GBM，
  17 家德國大學醫院，隨機分到標準 TMZ 化放療 vs **lomustine + TMZ + 放療**。
  mITT **129 人（63 vs 66）**：**中位存活 31.4 個月（27.7–47.1）→ 48.1 個月（32.6–未達）；
  HR 0.60（0.35–1.03），log-rank p=0.0492**；ITT（n=141）HR 0.60，p=0.0432。
  **grade ≥3 不良事件 51% vs 59%**，無治療相關死亡[S23]。
- **必寫的限制（作者自己寫的）**：「The findings should be interpreted with caution, **owing to the
  small size of the trial**」[S23]。EANO 2021 的評語更直接：這個組合方案
  「appears to be **largely restricted to some sites in German-speaking countries**」[S13]。
- → 對病人的意義：「MGMT 那一行如果是甲基化，你比較有機會**被納入某些試驗或某些方案**——
  但那個方案在台灣不是常規，要問你的神經腫瘤科團隊。」**不可寫成「甲基化就應該加 lomustine」**。

**E. 檢測方法與 cut-off——治療決策面（A4 已寫報告怎麼讀，本篇只寫「會不會影響要不要吃藥」）**

- **指引原文（EANO 2021）**[S13]：
  - 「**MGMT promoter methylation status should be determined in glioblastoma, notably in elderly or
    frail patients, to aid in decision-making for the use of temozolomide. C: I; L: B.**」
  - 「MGMT promoter methylation status should be tested using **methylation-specific PCR, pyrosequencing
    or methylation arrays (such as the MGMT-STP27 model)**」
  - 「**Immunocytochemistry is not an adequate method to determine the MGMT promoter methylation status.**」
  - 自陳兩個未解問題：「(1) establishing reliable MGMT promoter methylation status assays that can be used
    with **high interlaboratory agreement**, and (2) estimating the effect of **limited MGMT promoter
    methylation, an intermediate state between the non-methylated and methylated phenotypes**, on outcomes」
- **統合分析層級的方法比較**（Brandner 2021，Neuro-Oncology，以 Cochrane 系統回顧為基礎；
  **32 個獨立世代、3,474 人、兩種以上方法對照**）[S21]：
  - 「**Methylation-specific PCR (MSP) and pyrosequencing (PSQ) techniques were more prognostic than
    immunohistochemistry for MGMT protein, and PSQ is a slightly better predictor than MSP.**」
  - 「our meta-analysis **does not provide strong evidence about the best CpG sites or threshold**」；
    MSP 主要研究 CpG 76–80 與 84–87，PSQ 涵蓋 CpG 72–95；
    「A cutoff threshold of **9%** for CpG sites 74–78 performed better than higher thresholds of
    **28% or 29%** in 2 of the 3 good-quality studies.」[S21]
- **「灰色地帶」有多大——這是本篇最實用的一個數字**（Hegi 2019，四個隨機試驗合併）[S20]：
  - **4,041 人有有效 MGMT 結果，其中 1,725 人是隨機分派過的**；以定量 MSP 建模。
  - 非監督式切點 1.27（分開未甲基化與甲基化）；以存活監督後的最佳切點為 **−0.28（AUC 0.61）**，
    把被判為「未甲基化」的人再切成**「真正未甲基化」（≤−0.28）與「灰色地帶」（>−0.28, ≤1.27）**，
    **灰色地帶約佔全部病例的 10%**。
  - 相對於「真正未甲基化」，**甲基化者 HR 0.35（0.27–0.45），P<0.0001；灰色地帶者 HR 0.58
    （0.43–0.78），P<0.001**，並在測試集獲得驗證。
  - **在甲基化那一側，甲基化程度更高並不對應更好的結果**（「for patients with MGMT methylation
    (>1.27) more methylation was **not** related to better outcome」）。
  - 檢測重測一致性很好：218 對配對檢體 **R²=0.94**。
  - 作者結論（可直接引）：「**Low MGMT methylation (gray zone) may confer some sensitivity to temozolomide
    treatment, hence the lower safety margin should be considered for selecting patients with unmethylated
    GBM into trials omitting temozolomide.**」[S20]
- → **對病人的翻譯**：「報告上那一行只有兩個字，但它背後其實是一條連續的數字；
  大約每十個人裡就有一個，落在兩邊之間的灰帶。落在灰帶的人，
  **在設計『不給 TMZ』的試驗時會被特別排除**——理由就是怕誤傷。」[S20]

**F. MGMT 在高齡族群的權重（本篇只寫「它決定什麼」，療程選擇寫在 B3）**

- **EANO 2021 的兩句，直接決定了台灣門診常見的兩個對話**[S13]：
  1. 「**Temozolomide might only be active in patients with MGMT promoter-methylated tumours whereas
     its activity in patients with MGMT promoter-unmethylated tumours is probably marginal. C: II; L: B.**」
  2. 「**Elderly patients not considered candidates for temozolomide chemoradiotherapy should be treated
     on the basis of MGMT promoter methylation status (NOA-08, Nordic Trial) with radiotherapy
     (such as 15 × 2.66 Gy) or temozolomide (5 out of 28 days) alone. C: II; L: B.**」
- **EANO 對這一題的歷史敘述（極其誠實，值得整段轉述）**[S13]：
  「Until 2016, the broad consensus was that the results of all trials involving patients with tumours
  without MGMT promoter methylation showed **no detriment from the omission of temozolomide**, challenging
  the view that this agent should be used in every patient regardless of MGMT promoter methylation status.
  **This notion has become controversial again** after a minor OS prolongation with radiotherapy plus
  temozolomide versus radiotherapy alone was observed in elderly patients with glioblastomas lacking MGMT
  promoter methylation and with the negative outcome of the CheckMate 498 trial.」
- → **這一段是 B2 最好的收尾**：連指引本身都寫「這件事又變得有爭議了」。
  加上 Hegi & Stupp 2015 的那篇編輯評論標題本身就是內容：
  **《Withholding temozolomide in glioblastoma patients with unmethylated MGMT promoter — still a dilemma?》**
  （Neuro-Oncology 2015;17(11):1425–1427）[S19]。**全文取不到，只能引標題與其存在，不可引內文。**

### 反方向的資料（誠實必列）

- **MGMT 可能在復發時改變**：統合型文獻回顧（476 人）顯示 **115 人（24%，CI 0.21–0.28）**
  在復發時 MGMT 甲基化狀態與原發時不同；作者自陳原因可能包含**技術問題、腫瘤異質性、治療的選擇壓力**，
  並明說「**The clinical implications are still ambiguous and do not yet support a change in clinical
  practice**」[S24]。→ 可寫成「報告上那一行不是刻在石頭上的」，**但不可寫成「復發要重測」的建議**。
- Hegi 2005 的分層是**回溯的、只有 206 人（573 人中的 36%）**[S17][S2]，
  未甲基化亞組實際只有 50–60 人一組[S18]——這是「統計看不出來」的一個原因，
  **「看不出來」與「證明沒有」不是同一件事**。
- Alnahhas 的合併估計是**單臂中位數的合併**（沒有對照組可比），作者自己說
  「a direct comparison was not possible」，且納入研究多數為 moderate risk of bias、未設盲[S18]。

### Claim ceiling（B2＝全專題第二重的紅線）

- **可寫**：
  - 「MGMT 甲基化本身就是好的預後訊號，不管做什麼治療」（HR 0.45）[S17]；
  - 「甲基化的人加 TMZ，中位存活 15.3 → 21.7 個月」[S17]；
  - 「未甲基化的人加 TMZ：**存活的差距在那個試驗裡看不出來（11.8 vs 12.7 個月）；
    但腫瘤長回來的時間有差（5.9 vs 10.3 個月）**」[S18]；
  - 「**從來沒有人做過『未甲基化的人，放療 vs 放療加 TMZ』的前瞻隨機試驗**」[S18]；
  - 「高齡族群唯一一組直接的隨機數字（Perry）：10.0 vs 7.9 個月，**沒有跨過統計顯著的線**（P=0.055）」[S29]；
  - 「大約十分之一的人落在甲基化與未甲基化中間的灰帶，這些人在設計『不給藥』的試驗時會被排除」[S20]；
  - 「檢測方法有差：免疫組化不是合格的方法；焦磷酸定序略優於甲基化特異性 PCR；
    切點目前沒有共識」[S13][S21]；
  - 「指引的原話是『在未甲基化的人身上，temozolomide 的活性**可能是邊緣的**』，建議強度 C:II; L:B」[S13]。
- **不可寫**：
  - 「未甲基化就不用吃 TMZ」——**這是本篇最大的紅線**。可引的反證有三：沒有隨機試驗支持[S18]；
    Perry 的方向偏有益[S29]；灰帶約 10%[S20]；且 EANO 自己說這件事「又變得有爭議」[S13]。
  - 「未甲基化吃 TMZ 沒有用」——只能寫「**這個試驗看不出存活的差別**」，不能寫「沒有用」。
  - 「未甲基化吃 TMZ 有害」——**沒有任何資料支持**；NOA-08 的 EFS 方向是「二選一時選放療」，
    不是「TMZ 有害」[S28]。
  - 「甲基化就一定活得久」「未甲基化就沒救」——B4 的長期存活者裡兩種都有（見 B4，Briceno 2024
    明寫「there were LTS with **typical poor prognostic molecular markers**」[S39]）。
  - 「甲基化程度越高越好」——Hegi 2019 明確否定[S20]。
  - 「甲基化的人應該加 lomustine」——CeTeG 是 129 人的試驗，作者自己要求謹慎解讀，
    且不是台灣常規[S23][S13]。
  - 任何具體的 cut-off 數字被寫成「你的報告應該用幾 %」——**cut-off 沒有共識，這是給實驗室的問題**[S21]。
  - 勝算比／風險比不可寫成「機率的幾倍」（固定紅線）。

### Caveats／safety notes

1. **不可讓讀者拿這一篇去要求停藥或改藥。** 每一段的結尾都要回到「這一行決定的是**討論的內容**，
   不是**你的處方**」，並要求把問題帶去門診。
2. MGMT 檢測**不是急診資訊**；等報告的兩週歸 A4。
3. 本篇出現的所有存活數字都要一句指向 B4（SPEC §六）。
4. 灰帶那一段不可寫成「你可以要求重測」——重測與否是團隊決定，且復發時重測的臨床意義未定[S24]。

### 台灣端

- **健保條文裡沒有 MGMT。** 現行 9.25 Temozolomide 的給付規定**完全沒有提到 MGMT 或任何分子標記**，
  只有病名、同步／輔助、事前審查與三個月一關[S70]。
  → 可以誠實寫：「**在台灣，MGMT 那一行不決定你拿不拿得到藥；它決定的是你和醫師怎麼談這個藥值不值得。**」
  這一句對「未甲基化要不要吃」的紅線非常有用——因為它把問題從「能不能拿到」還原成「要不要用」。
- **MGMT 檢測本身的給付**：健保「藥品給付規定」不涵蓋檢驗；本次未查到可引用的檢驗給付條文
  → **gap，寫「檢測費用與給付請問個管師或醫務課」**[FAIL-7]。
  （附註：特管辦法附表四「實驗室開發檢測」第一項為「抗癌瘤藥物之伴隨檢測」[S72]，
  但該附表管的是 LDT 的施行程序，**不是健保給付**，不可混用。）
- **carmustine 植入劑（Gliadel Wafer）**在台灣有給付但與本篇相關的是一條限制：
  9.35「作為復發性多形神經膠母細胞瘤病人的手術輔助，且**不得與 temozolomide 併用**；需經事前審查
  核准後使用」（100/2/1，附表八之四）[S70]。→ 這條屬 A3／D3，B2 不寫，僅列出供交叉引用。

### 給繪圖組的數字（`fig-gb-mgmt`）

**主圖：同一個試驗、兩群人、兩種治療**（全部出自 EORTC 26981-22981）
| | 放療單獨 | 放療＋TMZ |
|---|---|---|
| **甲基化** 中位 OS | 15.3 個月（13.0–20.9） | **21.7 個月（17.4–30.4）** P=0.007 [S17] |
| **未甲基化** 中位 OS | 11.8 個月（9.7–14.1），n=54 | 12.7 個月（11.6–14.4），n=60 — 無統計差異 [S18] |
| **未甲基化** 中位 PFS | 5.9 個月（5.3–7.7），n=46 | 10.3 個月（6.5–14），n=46 [S18] |

**副圖／側欄（三選一即可，不要全放）**
- **灰帶**：約 **10%** 的病例落在「真正未甲基化」與「甲基化」之間；相對於真正未甲基化，
  灰帶 HR 0.58（0.43–0.78），甲基化 HR 0.35（0.27–0.45）[S20]
- **高齡的直接隨機數字**：Perry 甲基化 13.5 vs 7.7（HR 0.53）；未甲基化 10.0 vs 7.9
  （HR 0.75，**P=0.055**）[S29]——**P 值要畫進去**
- **預後 vs 預測**：Nordic 的對照——放療組甲基化與否無差（HR 0.97，p=0.81）；
  TMZ 組有差（HR 0.56，p=0.02）[S27]

---

## gb-elderly〈年紀大或體能不好，療程可以縮短〉（B3）

> 一般性框架（要不要治療、怎麼跟家屬談）指向站上〈八十歲，要不要治療〉；
> MGMT「決定什麼」寫在 B2，本篇只寫**療程選擇**。存活數字一律一句指向 B4。

### Key facts

**A. 先立的那一條：要不要治療，有隨機試驗**（SPEC 沒列，但必須放第一個 h4）

- **Keime-Guibert 2007 NEJM**（法國 ANOCEF）[S30]：
  **≥70 歲、新診斷 anaplastic astrocytoma 或 glioblastoma、KPS ≥70**，隨機分到
  **只做支持性照護** vs **支持性照護 + 放療（50 Gy／1.8 Gy 分次、一週五天）**。
  - 10 個中心、**85 人隨機**；最終分析針對 **81 位 glioblastoma**，中位年齡 **73 歲（70–85）**。
  - **試驗在第一次期中分析就因為達到預設的療效界線而停止**。
  - 中位追蹤 21 週：**放療組 29.1 週（n=39）vs 支持性照護組 16.9 週（n=42）；
    HR 0.47（95% CI 0.29–0.76），P=0.002**。
  - **「There were no severe adverse events related to radiotherapy.」**
    **「The results of quality-of-life and cognitive evaluations over time did not differ significantly
    between the treatment groups.」**[S30]
- **同方向的統合層級證據**：Cochrane 2020，四個隨機試驗合併（397 人），
  **術後放療 vs 術後支持性照護：HR 2.01（1.58–2.55），P<0.00001，中等確定性證據**；
  這些試驗「did not note any significant toxicity attributable to radiation」[S5]。
- → **B3 的第一句**：「療程可以縮短，前提是**還是要治療**。這一題有隨機試驗，答案是要治療；
  而且做了放療的那一組，生活品質與認知功能並沒有變得比較差。」

**B. 四個「縮短療程」的隨機試驗，按時間排**

| 試驗 | 年 | 族群（收案條件） | n | 比較 | 主要結果 |
|---|---|---|---|---|---|
| **Roa 2004**[S25] | 2004 | **≥60 歲**、GBM、術後 | 100 | **60 Gy／30 次／6 週** vs **40 Gy／15 次／3 週** | 中位 OS **5.1 vs 5.6 個月，log-rank P=.57**；6 個月存活 44.7% vs 41.7% |
| **Malmström 2012（Nordic）**[S27] | 2012 | **≥60 歲**、新診斷 GBM | 342 收案／291 三組隨機 | TMZ vs **34 Gy／10 次（3.4 Gy）／2 週** vs **60 Gy／30 次／6 週** | 見下 |
| **Wick 2012（NOA-08）**[S28] | 2012 | **>65 歲**、KPS ≥60、AA 或 GBM | 412 收案／373 分析 | **TMZ 100 mg/m² d1–7 一週吃一週停** vs **60 Gy／30 次（1.8–2.0 Gy）／6–7 週** | 見下 |
| **Roa 2015（IAEA）**[S26] | 2015 | 三種：**frail**（≥50 歲、KPS 50–70）、**elderly & frail**（≥65 歲、KPS 50–70）、**elderly**（≥65 歲、KPS 80–100） | 98 | **25 Gy／5 次／1 週** vs **40 Gy／15 次／3 週** | 中位 OS **7.9（6.3–9.6）vs 6.4（5.1–7.6），P=.988**；PFS 4.2 vs 4.2（P=.716） |

**Roa 2004 的細節**（B3 最重要的一筆，因為 40 Gy／15 次就是今天的標準短程）[S25]：
- 所有病人在分析時皆已死亡。**KPS 分數兩組沒有顯著差異（Wilcoxon P=.63）**。
- **完成放療者中，需要增加術後類固醇劑量的比例：標準組 49% vs 短程組 23%（χ² P=.02）**
  → **這是「短療程對病人比較好」最具體的一個數字**，而且它是關於類固醇的（連到 C2）。
- FACT-Br 問卷完成率只有 45%，**生活品質無法有意義比較**（作者自述）[S25]。
- 作者結論用字：短程放療「**seems to be a reasonable treatment option**」[S25]——是「合理選項」，
  不是「更好」。

**Nordic 的細節**（唯一同時比三種方案的試驗）[S27]：
- 分組：TMZ **200 mg/m²，每 28 天的第 1–5 天，最多 6 個療程**；低分次放療 **34.0 Gy／3.4 Gy 分次／2 週**；
  標準放療 **60.0 Gy／2.0 Gy 分次／6 週**。三組隨機：TMZ 93、低分次 98、標準 100。
- **vs 標準放療**：TMZ **8.3 個月（7.1–9.5）vs 6.0 個月（5.1–6.8），HR 0.70（0.52–0.93），p=0.01**；
  低分次放療 **7.5 個月（6.5–8.6），HR 0.85（0.64–1.12），p=0.24（沒有顯著差異）**。
- **TMZ vs 低分次放療（全部 242 人）**：8.4（7.3–9.4）vs 7.4（6.4–8.4），
  **HR 0.82（0.63–1.06），p=0.12——看不出差別**。
- **>70 歲這個亞群，兩種短方案都打敗標準放療**：TMZ vs 標準 **HR 0.35（0.21–0.56），p<0.0001**；
  低分次 vs 標準 **HR 0.59（0.37–0.93），p=0.02**[S27]。
- 毒性：TMZ 組最常見的 grade 3–4 是**嗜中性球低下 12 人、血小板低下 18 人**；
  三組合計 grade 3–5 感染 18 人；**2 例致死性感染（TMZ 組 1、標準放療組 1）**，
  另 1 例 TMZ 組因腸胃道出血手術後併發症死亡[S27]。
- 作者結論：「**Standard radiotherapy was associated with poor outcomes, especially in patients older
  than 70 years.**」[S27]

**NOA-08 的細節**（非劣性，而且非劣性的方向要說清楚）[S28]：
- **非劣性設計、margin 25%**。中位 OS **TMZ 8.6 個月（7.3–10.2）vs 放療 9.6 個月（8.2–10.8）；
  HR 1.09（0.84–1.42），p(non-inferiority)=0.033**。EFS 3.3 vs 4.7 個月，HR 1.15（0.92–1.43），
  p(non-inferiority)=0.043[S28]。
- **注意 HR 的方向**：點估計 1.09 是**偏向放療**的；試驗證明的是「TMZ 不比放療差超過設定的邊界」，
  **不是「TMZ 比較好」**。這一點在寫給病人時最容易被誤傳。
- MGMT：209 人可測，**甲基化 73 人（35%）**；甲基化 vs 未甲基化 OS **11.9 個月（9.0–未達）
  vs 8.2 個月（7.0–10.0），HR 0.62（0.42–0.91），p=0.014**[S28]。
- 毒性（TMZ vs 放療，人數）：嗜中性球低下 16 vs 2、淋巴球低下 **46 vs 1**、血小板低下 14 vs 4、
  肝酵素上升 30 vs 16、感染 35 vs 23、**血栓栓塞事件 24 vs 8**[S28]。
  → **血栓那一欄要記住，它是紅線 6（C4）的 DVT／PE 條目的直接證據來源之一。**

**Roa 2015 IAEA 的細節**（一週五次那個）[S26]：
- **這是唯一一個把「體能不好但不老」（≥50 歲、KPS 50–70）明確寫進收案條件的試驗**——
  它的標題就叫「Elderly **and/or Frail**」。分層因子：年齡（<65／≥65）、KPS、切除程度。
- 中位追蹤只有 **6.3 個月**；治療後 4 週與 8 週的生活品質兩組無差異[S26]。
- 作者結論用字：25 Gy／5 次「**may be recommended as a treatment option**」，理由是
  「**in view of the reduced treatment time**」[S26]。

**C. 加不加 TMZ：Perry 2017 CE.6（本篇的軸心）**[S29]

- **設計**：≥65 歲、新診斷 GBM；**兩組的放療完全一樣（40 Gy／15 次）**，只差有沒有同步 + 輔助 TMZ。
- **n=562（各 281）**；**中位年齡 73 歲（65–90）**。
- **主要結果**：中位 OS **9.3 vs 7.6 個月；HR 0.67（0.56–0.80），P<0.001**。
  中位 PFS **5.3 vs 3.9 個月；HR 0.50（0.41–0.60），P<0.001**。
- **MGMT 分層**：甲基化 n=165，**13.5 vs 7.7 個月，HR 0.53（0.38–0.73），P<0.001**；
  未甲基化 n=189，**10.0 vs 7.9 個月，HR 0.75（0.56–1.01），P=0.055；交互作用 P=0.08**。
- **「Quality of life was similar in the two trial groups.」**[S29]
- → 這是全部高齡試驗裡**唯一一個「短程放療 ± TMZ」的直接隨機比較**，
  也是今天大多數高齡病人實際會被建議的方案。

**D. 統合層級的排序（Cochrane 網絡統合分析，本篇最強的一筆）**[S31]

- Hanna 2020，Cochrane Database Syst Rev 2020;3:CD013261。**12 個隨機試驗、約 1,818 人**；
  「elderly」定義為 70 歲以上，若研究自稱 65 歲以上亦納入。**多數受試者可自我照顧**。
- 網絡統合分析納入 7 個試驗、7 種介入：**只做支持性照護、低分次放療（RT40）、標準放療（RT60）、
  TMZ、化放療（CRT）、bevacizumab+CRT、bevacizumab+RT**。
- **主要結果（整體存活）**：
  - **CRT 優於 RT40：HR 0.67（0.56–0.80），高確定性證據**。
  - **TMZ vs CRT：HR 1.42（1.01–1.98），低確定性證據**（即 CRT 可能優於單獨 TMZ）。
  - **加 bevacizumab 到 CRT：HR 0.83（95% CrI 0.48–1.44），低確定性——可能沒有差別**。
  - 排序：**CRT > TMZ > RT > 只做支持性照護**；**bevacizumab + RT 是唯一一個相對於只做支持性照護
    看不出存活好處的方案**。
  - **無法比較 CRT 用 60 Gy／30 次與 40 Gy／15 次的差別（資料不足）**——重要的誠實限制。
- **PFS**：CRT vs RT40 HR 0.50（0.41–0.61），高確定性；RT60 vs 支持性照護 HR 0.28（0.17–0.46），中等確定性。
- **生活品質**：TMZ 與放療之間**大致沒有差別**，例外是「**因溝通障礙造成的不適**在放療組較常見
  （1 個研究、306 人，P=0.002）」，中等確定性[S31]。
- **嚴重不良事件**：**TMZ 相對 RT60 的 grade 3+ 血栓栓塞事件 RR 2.74（1.26–5.94）**，中等確定性；
  TMZ 也增加 grade 3+ 嗜中性球、淋巴球與血小板低下；**CRT 相對單獨低分次放療也增加
  grade 3+ 嗜中性球低下、白血球低下與血小板低下**；**bevacizumab 加到 CRT 增加血栓風險
  RR 16.63（1.00–275.42）**[S31]。
- 作者結論（可引）：「For elderly people with glioblastoma who are **self-caring**, evidence suggests
  that CRT prolongs survival compared with RT and may prolong overall survival compared with TMZ alone.」
  以及「**Current evidence provides little justification for using BEV in elderly patients outside a
  clinical trial setting.**」[S31]
- **關於 TTFields 的一句**：EF-14 因為是在完成化放療之後才隨機，無法納入網絡統合分析；
  Cochrane 的評語是「findings from the trial suggest that the intervention **probably improves overall
  survival in this selected patient population**」，但「evidence on QoL and tolerability is needed in an
  elderly population」[S31]。

**E. 短療程本身輸不輸——證據等級要分開講**[S5]

- Cochrane 2020（Khan）：**低分次 vs 常規分次，5 個試驗 943 人，HR 0.95（0.78–1.17），P=0.63，
  但證據確定性是「極低」**。
- **限定在「≥60 歲的 glioblastoma」這個亞組（2 個試驗、293 人）：HR 1.16（0.92–1.46），P=0.21，
  證據確定性是「高」**[S5]。
- 安全性：兩種分次都「well tolerated with mild acute adverse effects」；
  **整個回顧中只有 1 位低分次組病人出現需要手術的症狀性放射性壞死**[S5]。
- → 正確措辭見「不同形狀 7」。

**F. 是年齡還是體能——KPS 才是那個變項**

- **RPA 的原始結構**（Curran 1993，1,578 位惡性膠質瘤、1974–1989 年三個 RTOG 試驗）：
  第一個切點是年齡（50 歲）；**但在 ≥50 歲那一支，「performance status 是最重要的變項」**，
  之後只有「心智狀態正常與否」在體能較差組造成有意義的再分割[S32]。
  12 個亞組的中位存活從 **4.7 到 58.6 個月**[S32]。
- **簡化版 RPA**（Li 2011，1,672 位 GBM）：最終模型只用四個變項——**年齡、體能狀態、切除程度、
  神經功能**；三個分級的中位存活 **17.1／11.2／7.5 個月**[S33]。
- **Roa 2015 是唯一把「不老但體能差」寫進收案條件的試驗**（≥50 歲、KPS 50–70 就算 frail）[S26]。
- **EANO 的措辭把兩者並列，不是只講年齡**：
  「**Patients with unfavourable prognostic factors (defined by age and/or KPS)** can be treated with
  hypofractionated radiotherapy (such as 40 Gy in 15 fractions), which has similar activity to
  irradiation with 60 Gy in 30 fractions」[S13]。
  以及總則：「**Karnofsky performance score (KPS), neurological function, age, and individual risks and
  benefits should be considered for clinical decision-making. C: IV; L: A.**」[S13]
- **反過來，Stupp 2009 說標準治療的好處在 60–70 歲那一組也看得到**：
  「A benefit of combined therapy was recorded in all clinical prognostic subgroups, **including patients
  aged 60–70 years**」[S2]。
  → **合起來的正確訊息**：「**不是滿六十五歲就自動換成短療程。**決定的是體能、神經功能與你自己的
  取捨；六十幾歲、狀況好的人，標準六週療程的好處在試驗裡是看得到的。」

**G. 指引原文彙整（B3 可直接引的兩句）**[S13]

1. 「Patients with unfavourable prognostic factors (defined by age and/or KPS) can be treated with
   hypofractionated radiotherapy (such as **40 Gy in 15 fractions**), which has **similar activity** to
   irradiation with 60 Gy in 30 fractions.」
2. 「**Further hypofractionation to 5 × 5 Gy does not seem to compromise OS but is likely to cause
   neurocognitive adverse events if, in the future, elderly patients with glioblastoma live longer
   because of improved systemic treatment.**」
   → 這第二句非常重要：**指引自己對 25 Gy／5 次留了一個保留意見**，理由是認知副作用（連到 D2）。
   寫 Roa 2015 時**必須並陳這一句**。

### 反方向的資料（誠實必列）

- Roa 2004 只有 100 人、Roa 2015 只有 98 人、中位追蹤 6.3 個月[S25][S26]——
  「沒有差別」在小型試驗裡也可能只是**看不出來**。
- Nordic 的低分次放療 **vs 標準放療在全體族群沒有達到顯著（HR 0.85，p=0.24）**[S27]；
  它的顯著優勢只出現在 **>70 歲**那個亞群[S27]。
- NOA-08 的點估計方向偏放療（HR 1.09）[S28]；Cochrane NMA 也把 CRT 排在 TMZ 前面（HR 1.42，
  低確定性）[S31]。→ **「可以只吃藥不放療」不是通則**，是 MGMT 甲基化 + 不適合化放療者的選項。
- Cochrane NMA 的所有受試者「Most participants were capable of self-care」[S31]；
  真正臥床、KPS 很低的人**被排除在幾乎所有隨機試驗之外**——Cochrane 兩份回顧都明說了：
  「These HGG individuals with poor prognosis have **generally been excluded from randomised trials**
  based on poor performance status. **No randomised trial has compared comfort measures or best supportive
  care with an active intervention** using radiotherapy or chemotherapy in these people」[S5]。
  → **這一句是本篇最誠實、也最需要寫進去的一句**，它同時處理了「體能很差的人怎麼辦」與
  「什麼時候談安寧」（指向站上〈最後那幾週，會發生什麼〉）。

### Claim ceiling（B3）

- **可寫**：「≥70 歲、體能還可以的人，放療對支持性照護有隨機試驗：29.1 週 vs 16.9 週，
  而且沒有讓生活品質或認知變差」[S30]；「六十歲以上，40 Gy／15 次與 60 Gy／30 次的存活看不出差別，
  而且短程組需要加類固醇的人少一半（23% vs 49%）」[S25]；「這一條在六十歲以上 GBM 是**高等級**證據」[S5]；
  「更短的 25 Gy／5 次，在體能差或高齡的人身上，存活與 40 Gy／15 次看不出差別」[S26]；
  「短程放療加上 TMZ，比只做短程放療多 1.7 個月的中位存活（9.3 vs 7.6），生活品質相當」[S29]；
  「甲基化的人加 TMZ 差很多（13.5 vs 7.7），未甲基化的人差比較少而且沒有跨過統計的線
  （10.0 vs 7.9，P=0.055）」[S29]；「超過七十歲，標準六週放療的表現是三個方案裡最差的」[S27]；
  「統合分析的排序是：化放療 > 單獨 TMZ > 單獨放療 > 只做支持性照護」[S31]；
  「決定療程長短的不只是年齡，是體能狀態、神經功能與切除程度」[S32][S33][S13]。
- **不可寫**：
  - 「年紀大就該做短療程」——EANO 的條件是 age **and/or** KPS，而 Stupp 2009 說 60–70 歲仍看得到
    標準治療的好處[S13][S2]。
  - 「短療程效果一樣好」（無條件式）——只有「≥60 歲 GBM」這個格是高確定性；整體族群的證據是極低確定性[S5]。
  - 「高齡可以只吃藥、不用放療」——那是 **MGMT 甲基化且不適合化放療**的選項，
    且 Cochrane NMA 把 CRT 排在單獨 TMZ 之前[S13][S31]。
  - 「25 Gy／5 次跟其他一樣好，所以最省事」——**必須並陳 EANO 對認知副作用的保留**[S13]。
  - 把 5.1／5.6／7.9 這些月份寫成個人期限——一律指向 B4。
  - 「TMZ 比放療好」（NOA-08 是非劣性、點估計偏放療）[S28]。
  - 任何讓「年紀大就不用治療」讀起來成立的句子——**Keime-Guibert 是本篇的防火牆**[S30]。
  - 高齡族群用 bevacizumab——Cochrane 明說臨床試驗之外「little justification」[S31]。

### Caveats／safety notes

1. **TMZ 在高齡族群的血液與血栓毒性要具體寫**：NOA-08 的淋巴球低下 46 vs 1、血栓栓塞 24 vs 8[S28]；
   Cochrane 的 TMZ vs RT60 血栓 RR 2.74（1.26–5.94）[S31]。**DVT／PE 的警訊症狀寫在 C4，本篇一句指路。**
2. **短程放療不是「打折的治療」**：Roa 2004 的類固醇需求差異（23% vs 49%）要正面寫[S25]，
   它是「短療程對身體比較輕」的證據，不是「將就」。
3. **KPS 很低的人沒有隨機試驗**[S5]——不要替他們編造建議；寫「這時候的討論是另一種討論」，
   指向站上〈八十歲，要不要治療〉與〈最後那幾週，會發生什麼〉。
4. 一般性的高齡決策框架不在本篇重寫（SPEC §六）。

### 台灣端

- **temozolomide 的健保條文對年齡沒有任何限制**，也沒有區分同步／維持以外的分層[S70]。
  → 「高齡不影響給付資格」這件事**可以寫**，因為條文原文可查；但**不可推論「所以一定會核准」**——
  仍需事前審查[S70]。
- **放療分次數與健保**：支付標準對常規分次放療是按「每一照野」計費（36011B–36013B）[S71]，
  **沒有針對高齡短程療程的特別項目**；低分次放療的專屬項目只有乳癌（36022B、36023B）與
  直腸癌（36024B）[S71]。→ **不可推論腦部低分次放療的給付狀態**，若讀者要問，寫「問醫務課」。
- 高齡相關的一般給付（重大傷病）見 Brief A [S30 of A]，本篇不重複。

### 給繪圖組的數字（`fig-gb-elderly`）

**建議畫成「同一張圖上四個試驗的設計 + 結果」，橫軸是療程長度（週），縱軸是中位存活（月）**

| 試驗 | 療程 | 中位 OS | 對照 | 差異 |
|---|---|---|---|---|
| Keime-Guibert 2007 | 50 Gy／28 次 vs **不放療** | **29.1 週** vs 16.9 週 | ≥70 歲、KPS≥70 | HR 0.47（0.29–0.76）[S30] |
| Roa 2004 | 60 Gy／6 週 vs **40 Gy／3 週** | 5.1 vs **5.6** 個月 | ≥60 歲 | P=.57（看不出差別）[S25] |
| Nordic 2012 | 60 Gy／6 週 vs **34 Gy／2 週** vs **TMZ** | 6.0 vs 7.5 vs **8.3** 個月 | ≥60 歲 | TMZ vs 標準 HR 0.70（p=0.01）[S27] |
| Roa 2015 | 40 Gy／3 週 vs **25 Gy／1 週** | 6.4 vs **7.9** 個月 | 高齡／體能差 | P=.988（看不出差別）[S26] |
| **Perry 2017** | 40 Gy／3 週 ± TMZ | **9.3** vs 7.6 個月 | ≥65 歲，n=562 | HR 0.67（0.56–0.80）[S29] |

**必畫的兩個註記**
- Perry 的 MGMT 分層：甲基化 13.5 vs 7.7（HR 0.53，**P<0.001**）；未甲基化 10.0 vs 7.9
  （HR 0.75，**P=0.055**）[S29]
- Roa 2004 的類固醇：**標準組 49% 需要加量、短程組 23%**[S25]

---

## gb-numbers〈那個數字，我要怎麼跟你講〉（B4）【全系列最高紅線，雙向】

> 這一篇要的是**「怎麼正確讀存活曲線」的素材**，不是更多數字。
> 下面每一節的排列順序，刻意對應紅線 1 的兩個方向：先給曲線的形狀，再給尾巴是誰，
> 再給「中位數不是個人預測」的方法學，最後給「病人想不想知道、怎麼講」的實證。

### (a) 五年存活率與曲線尾巴的實際比例

**試驗族群（EORTC 26981-22981，Stupp 2009 五年追蹤）**[S2]
- 合併治療組（放療 + TMZ，n=287）：**2 年 27.2%（22.2–32.5）、3 年 16.0%（12.0–20.6）、
  4 年 12.1%（8.5–16.4）、5 年 9.8%（6.4–14.0）**
- 單獨放療組（n=286）：**2 年 10.9%、3 年 4.4%、4 年 3.0%、5 年 1.9%**
- **死亡人數**：放療組 278/286（**97%**）、合併組 254/287（**89%**）——
  **五年之後仍存活的人，在這個試驗裡是一成上下，不是零**[S2]。
- 作者原話：「**A few patients in favourable prognostic categories survive longer than 5 years.**」[S2]

**真實世界族群（Poon 2020，Scientific Reports，OA；23 個族群、來自 63 篇研究）**[S40]
- **2 年存活：2005 年前收案 9%（95% CI 6–12%，1,488/17,507）→ 2005 年後 18%（14–22%，5,670/32,390）**
- **3 年存活：4%（2–6%，325/10,556）→ 11%（9–14%，1,900/16,397）**
- **5 年存活：3%（1–5%，401/14,919）→ 4%（2–5%，1,291/28,748）**
- 作者結論原文：「**Meta-analyses of real-world data suggested a doubling of 2- and 3-year survival in
  glioblastoma patients since 2005. However, 5-year survival remains poor with no apparent improvement.**」
  以及「Detailed clinically annotated population-based data and further molecular characterization of
  longer-term survivors may explain the unchanged survival beyond 5 years.」[S40]
- → **B4 最重要的一組對照**：試驗裡五年 9.8%[S2]，真實世界五年 4%[S40]。
  **兩年與三年這一段真的改善了；五年那一段沒有。** 這一句同時擋住兩個方向的誤讀。

### (b) 長期存活者的實證研究——他們有什麼共同點

**比例（三個不同定義，不要混用）**
- **>3 年**：Krex 2007（Brain）敘述句：「The median survival of glioblastoma patients is approximately
  12 months. However, **3–5% of the patients survives for more than 3 years** and are referred to as
  long-term survivors.」[S36]
- **≥2／3／5 年（族群基礎）**：見上 Poon 2020[S40]。
- **≥10 年**：Tykocki 2018（系統回顧，36 篇研究、162 例、1950–2014 年發表）：
  「The rate of long survivors in the cohort studied was established **0.76%**」；
  「The **10-year survival rate** in the cohort studied with GBM was estimated **0.71%**」[S38]。
  該世代平均診斷年齡 **31.1 ± 11.1 歲**、平均 OS **15.9 ± 6.3 年**、PFS **11.9 ± 5.6 年**；
  全切除 82 例、次全切除 58 例、僅切片 9 例；**全切與次全切之間的 PFS、OS、年齡都沒有統計差異**[S38]。
  → **必寫的限制**：這 162 例橫跨 1950–2014 年、**大多沒有 IDH 檢測**，
  依 2021 WHO CNS5 有相當比例今天不會被叫做 GBM（見 Brief A 與下面 Hartmann）。
  **「有人活了十年」這句話，正確的說法是「在舊分類下有人活了十年」。**

**他們的共同點（四筆研究，方向一致）**
1. **Krex 2007**（德國膠質瘤網絡，55 位原發 GBM 長期存活者，>3 年）[S36]：
   - 特徵：**診斷時年輕、初始 KPS 好**。
   - 「**None of the evaluated socioeconomic, environmental and occupational factors were associated with
     long-term survival.**」→ **這一句要寫進去**：吃什麼、住哪裡、做什麼工作，這個研究都看過了，
     跟長期存活沒有關係。
   - 分子：**MGMT 過度甲基化 28/36（74%）**、TP53 突變 9/31（29%）、EGFR 擴增 10/38（26%）、
     1p/19q 共同缺失 2/32（6%）。
   - 與 141 位未經選擇的連續病人比較，**長期存活組的 MGMT 過度甲基化顯著較常見**[S36]。
2. **Hartmann 2013**（Clin Cancer Res；69 位中央病理確認、存活 >36 個月的 GBM「LTS-36」，
   其中 33 位 >60 個月「LTS-60」；對照 257 位存活 <36 個月）[S37]：
   - **IDH1/2 突變率：LTS-36 為 34%（23/67），對照組 4.3%（11/257）**
     → **這是「IDH 狀態誤分類的比例」最直接的一筆數字**：在舊分類的長期存活者裡，
     每三個就有一個帶 IDH 突變，也就是今天會被改叫 *Astrocytoma, IDH-mutant, grade 4* 的那條路（Brief A）。
   - 帶 IDH 突變的長期存活者：較年輕、幾乎沒有 EGFR 擴增、較常有 1p/19q 共同缺失與 TP53 突變。
   - **IDH 野生型的長期存活者**：「showed **no distinguishing features** from other patients with
     IDH1/2 wild-type glioblastomas **except for a higher rate of MGMT promoter methylation**」[S37]
     → 也就是說：**在今天定義的 GBM 裡，除了 MGMT，我們找不出長期存活者跟其他人的差別。**
3. **Briceno 2024**（Neuro-Oncology Advances；**分子確認 IDH 野生型**、存活 ≥3 年者 23 人 vs <3 年 75 人）[S39]：
   - LTS 傾向較年輕；診斷時 MRI 較常見 T1 低訊號；**腫瘤富含 MGMTp 甲基化與 TP53 突變**。
   - **「Three patients with classic GBM histology were reclassified based on NGS and methylation testing.」**
     → 即使在一個以分子確認為前提的世代裡，**仍有 3 人在完整分子檢測後被改診斷**。
   - **「Additionally, there were LTS with typical poor prognostic molecular markers.」**
     → **帶著壞標記卻活得久的人，是存在的。**
   - 作者結論（**本篇最該引的一句**）：「Our findings emphasize that **generalized predictions of prognosis
     are inaccurate for individual patients** and underscore the need for complete clinical evaluation
     including molecular work-up to confirm the diagnosis.」[S39]
4. **切除程度那一邊**：Tykocki 的十年存活世代裡，**全切除與次全切除之間看不出差別**[S38]；
   而切除程度與存活的關聯**全部是觀察性資料**（紅線 2，歸 A3）。
   → B4 提到「把人往右邊推的因素」時，切除程度那一項**必須降半格寫**，並一句指向 A3。

### (c) 預後分層工具與它們的限制

**RTOG RPA（Curran 1993）**[S32]
- 資料來源：**1974–1989 年三個 RTOG 惡性膠質瘤試驗、1,578 人**（含 GBM 與 anaplastic astrocytoma）；
  分析 **26 個治療前變項 + 6 個治療相關變項**。
- 樹的結構：第一個切點是**年齡 50 歲**；<50 歲依組織學再分，≥50 歲則**體能狀態是最重要的變項**。
- 結果：**12 個亞組，中位存活從 4.7 到 58.6 個月**，各亞組人數 32–256 人[S32]。
- **作者自己寫的用途**：「to identify subgroups with survival rates sufficiently different to create
  **improvements in the design and stratification of clinical trials**」——
  **它是為了設計試驗、做分層用的工具，不是為了預測某一個人。** 這句要寫出來。

**簡化版 RPA（Li 2011）**[S33]
- 1,672 位 GBM（排除 AA）+ 488 人測試集。
- 最終模型：**把第 V 與第 VI 類合併成三類，只用四個變項——年齡、體能狀態、切除程度、神經功能**。
- 三類的中位存活：**17.1／11.2／7.5 個月**。
- **限制（本篇要引的關鍵）**：「The original RPA model **explained more variation in survival** in the
  test dataset than did the new models（**20% vs 15%**）」；簡化版的 explained variation 是 **18%**[S33]。
  → **翻譯給病人**：「這一套目前最好用的分級工具，**只解釋了存活差異的兩成**。
  剩下的八成，我們不知道是什麼。」——**這是本篇最有力的一句，而且它是原始論文自己的數字。**

**Gorlia nomogram（2008）**[S34]
- EORTC 26981-22981／NCIC CE.3 的 573 人；分三個族群建模：全體（n=573）、
  接受 TMZ + 放療者（n=287）、其中有 MGMT 結果且接受過切除者（**n=103**）。
- 獨立預後因子：**合併 TMZ 治療、切除範圍較大、年齡較輕、MMSE ≥27 分、基線未使用類固醇**；
  在 TMZ 組另加**體能狀態**；在 n=103 那一組則是 **MGMT 甲基化、體能狀態、MMSE ≥27**。
- 工具位置：http://www.eortc.be/tools/gbmcalculator[S34]。
- **限制**：這是原始試驗的 **exploratory subanalysis**（作者用字）；
  MGMT 那個模型只建立在 **103 人**上；族群是 2000–2002 年、依組織學診斷的病人[S34][S1]。

**性別分開的列線圖（Patil 2021）**[S35]
- NRG/RTOG 0525（752 人）建模、NRG/RTOG 0825（599 人）獨立驗證。
- **兩性共同的顯著預測因子：診斷年齡、KPS、MGMT 啟動子甲基化、腫瘤位置**；
  **切除程度與類固醇使用只在男性顯著**。
- 輸出的是 **6 個月、12 個月、24 個月的存活機率**，不是「你可以活多久」[S35]。
- → **可用的一句**：連工具本身給的都是「**在某個時間點還活著的機率**」，不是一個日期。

### (d) 中位存活的統計意義——「中位數不是個人預測」的可引用方法學

**基本定義層**[S50]
- Clark 2003（Br J Cancer，OA，四篇一組的 survival analysis 教學文獻第一篇）
  可作為「存活分析基本概念與 Kaplan–Meier」的方法學引用來源[S50]。
  **注意**：本 brief 只取其書目與「它是教學性方法學文獻」這個身分；**未逐句抓取其內文，
  正文若要引語必須先取全文核對**（見 NOT-CITABLE 註記）。

**可操作的框架層——best case / typical / worst case（本篇的核心方法學素材）**
- **Kiely 2011（J Clin Oncol，轉移性乳癌）**[S43]：
  36 個第一線化療隨機試驗、13,083 位女性。從每條 OS 曲線取四個百分位數：
  **第 90 百分位＝最壞情況、第 75＝典型偏差、第 25＝典型偏好、第 10＝最好情況**。
  發現這四個情境可以用**中位數的簡單倍數**估計：**0.25×（最壞）、0.5×（典型下緣）、
  2×（典型上緣）、3×（最好）**。準確度（落在實際值的 0.75–1.33 倍內）：
  **最壞 73%、典型下緣 97%、典型上緣 95%、最好 96%**。
  作者結論：「Simple multiples of an OS curve's median can accurately estimate **typical (half to double
  the median), best-case (triple the median), and worst-case (one quarter of the median)** scenarios
  for survival.」[S43]
- **Kiely 2012（Lung Cancer，晚期非小細胞肺癌）**[S44]：
  60 個試驗、29,657 人。各情境與中位數的比值：**最壞 0.26（IQR 0.21–0.29）、典型下緣 0.53、
  典型上緣 1.81、最好 2.84**——「These values can be approximated by the simple multiples:
  **0.25, 0.5, 2 and 3.**」[S44]
- **⚠ 這個方法沒有在膠質瘤驗證過。** Europe PMC 以
  `(TITLE:"scenarios for survival" OR TITLE:"best-case" OR TITLE:"worst-case") AND ABSTRACT:"glioma"`
  與 `TITLE:"life expectancy" AND TITLE:"glioblastoma" AND TITLE:"scenarios"` 查詢，**命中皆為 0**[FAIL-8]。
  → **Claim ceiling（硬）**：可以寫「**在轉移性乳癌與晚期肺癌，有人驗證過一種講法：
  把中位數乘以 0.25、0.5、2、3，得到最壞、典型、最好的區間**」，並說明這是**一種講法的形狀**；
  **絕對不可以把這四個倍數套到 GBM 的中位數上算出具體月數寫給讀者。**
  正確的替代做法：**直接用 Stupp 2009 的實際百分比**[S2]（見「給繪圖組」）。

**條件式存活（conditional survival）——「已經走過一段的人，前面的路不一樣」**
- **Johnson 2012（Cancer；SEER 1998–2008、接受含放療方案、n=10,022）**[S41]：
  - 中位存活 **12.61 個月**。
  - **「再活兩年」的條件機率：從診斷當下的 19.8%，到診斷後五年時的 65.9%。**
  - 「The proportion of patients surviving 12 months **from time of diagnosis as well as from 6, 12, and
    18 months after diagnosis** was significantly higher in patients diagnosed in 2005 through 2008 than
    those diagnosed in 1998 through 2004.」
  - 在人口統計與治療相關因子中，**只有年齡在診斷當下、1 年後、3 年後三個時點都與死亡風險相關
    （每個時點 P<.0001）**。
  - 作者結論：「Patients surviving past 2 years from diagnosis have a relatively favorable conditional
    probability of survival into the future compared to newly diagnosed patients. This effect becomes more
    pronounced with increasing time since diagnosis. **These data will assist in the counseling of
    glioblastoma survivors.**」[S41]
- **Mueller 2026（Int J Cancer，OA；315 位 IDH 野生型 GBM 前瞻登記世代，2008-01 至 2017-06）**[S42]：
  - **12 個月條件存活**（在已存活 s 個月的前提下，再活 12 個月的機率）：
    **s=0：0.51（0.45–0.56）；s=6：0.46（0.39–0.52）；s=12：0.41（0.33–0.49）；
    s=18：0.43（0.33–0.52）；s=24：0.56（0.42–0.67）**。
  - 診斷當下（s=0）與 12 個月存活顯著相關的因子：**年齡 >60、術前腫瘤環狀體積 >20 cm³、
    沒有 MGMT 甲基化、術後 KPS ≥70、術後殘餘腫瘤 >1 cm³ 或只做切片**。
  - **「Residual tumor volume mainly influences survival in the initial months following surgery,
    while MGMT promoter methylation and age remain significant predictors beyond this period.」**[S42]
    → **這一句是本篇的珍寶**：**預後因子的權重會隨時間改變**。手術切了多少，主要影響前面幾個月；
    再往後，是 MGMT 和年齡在說話。這正面回答了「我開完刀殘留一點，是不是就沒救了」。
  - **注意族群標籤**：這是 2008–2017 年的單一登記世代、n=315、以 IDH 野生型定義，
    數字**不可以當作台灣病人的機率**。

### (e) 近年真實世界資料的存活是否有改善

- **Poon 2020**（見 (a)）：2/3 年存活翻倍、**5 年沒有改善**[S40]。
- **Johnson 2012**：SEER 中 2005–2008 年診斷者，在多個時點的 12 個月存活率**顯著高於** 1998–2004 年
  診斷者[S41]。
- **CBTRUS（美國全國登記，2018–2022 年資料，2025 年 10 月出版）**[S46]：
  - 所有原發性腦與中樞神經系統腫瘤年齡標準化發生率 **26.05／10 萬**（惡性 6.86、非惡性 19.19）
  - **glioblastoma 佔全部腦瘤 13.7%、佔惡性腦瘤 52.2%**；男性較多
  - **惡性腦與中樞神經系統腫瘤的五年相對存活率 34.8%**（非惡性 91.7%）
  - **⚠ 這個 34.8% 是「所有惡性腦瘤」，不是 GBM。GBM 的專屬五年存活率不在摘要裡，
    全文在 Europe PMC 取不到**[FAIL-9]。**正文若引 34.8%，必須明寫它涵蓋所有惡性腦瘤、不是 GBM，
    否則就是誤導。建議乾脆不引，用 Poon 2020 的 4% 就好。**
- **台灣的時間趨勢：查不到可引用的官方資料**（見台灣端）[FAIL-4]。

### (f) 醫病溝通文獻——病人想不想知道、怎麼講

**病人想不想知道（晚期癌症，非 GBM 專屬，族群標籤要標）**
- **Hagerty 2004（J Clin Oncol，126 位無法治癒的轉移性癌症病人，澳洲）**[S51]：
  - **>95%** 想知道副作用、症狀與治療選項。
  - **85%** 想知道「接受治療後最長的存活時間」；**80%** 想知道五年存活率；**81%** 想知道「平均存活」。
  - **「Words and numbers were preferred over pie charts or graphs.」**
  - **59%** 希望在剛被診斷為轉移時就討論預期存活；**38%／44%** 希望「討論存活／討論死亡」的時機
    可以商量。
  - **憂鬱分數較高者較想知道「不治療的最短存活時間」（P=.047）與「平均存活」（P=.049）**；
    憂鬱分數較低者較常表示「永遠不想討論預期存活」（P=.03）。
  - 結論：「Most metastatic cancer patients want detailed prognostic information but prefer to
    **negotiate the extent, format, and timing**」[S51]。
- **Hagerty 2005（J Clin Oncol，同一世代）**[S47]：
  - **98%** 希望醫師**務實（realistic）**、給提問的機會、把自己當一個個別的人看。
  - 被評為最能給希望的醫師行為：**提供最新的治療（90%）**、**看起來對這個癌症知道得很清楚（87%）**、
    **說疼痛會被控制住（87%）**。
  - 被評為**無助於**建立希望的：**醫師看起來緊張或不自在（91%）**、**先把預後告訴家屬（87%）**、
    **使用委婉語（82%）**。
  - 最被認同的兩種風格：**「務實 + 個別化照顧」**與**「專業／正向／協作」**[S47]。
  - → **「先告訴家屬」被 87% 的病人列為無助於希望**，這一條對台灣的門診現實（家屬常常先知道，
    SPEC §三就寫了）特別重要，**建議寫進正文**。
- **Enzinger 2015（J Clin Oncol，590 位化療後仍惡化的轉移性實體癌病人，追蹤至死亡）**[S48]：
  - 中位存活 **5.4 個月**。**71% 想被告知餘命，但只有 17.6% 記得醫師曾告知過**。
  - 在 299 位願意自估餘命的病人中：**記得被告知者的中位自估 12 個月（IQR 6–36），
    不記得者 48 個月（IQR 12–180），P<0.001**。
  - 自估與實際存活相差超過 **2 年**的比例：30.2% vs 49.2%（OR 0.45，0.14–0.82）；
    相差超過 **5 年**：9.5% vs 35.5%（OR 0.19，0.08–0.47）。
  - 校正後，記得被告知與自估餘命**減少 17.2 個月（95% CI 6.2–28.2）**相關。
  - 自估餘命越長，**簽 DNR 的機率越低（每多估 12 個月，aOR 0.439，0.296–0.630）**，
    **偏好延長生命而非舒適導向照護的機率越高（aOR 1.493，1.091–1.939）**。
  - **關鍵結論**：「**Prognostic disclosures are associated with more realistic patient expectations of
    LE, without decrements to their emotional well-being or the patient–physician relationship.**」
    以及「Prognostic disclosure was **not associated with worse patient-physician relationship ratings,
    sadness, or anxiety** in adjusted analyses.」[S48]
  - → **這是本篇最重要的一筆實證**：**告知不會讓人更焦慮、不會傷害醫病關係，但會改變決定。**
- **膠質瘤專屬的那一份**：Diamond 2014（J Neurooncol，系統回顧，14 篇研究）[S49]：
  - 「The definition and measurement of PA（prognostic awareness）across studies **varied**, and the
    prevalence of **accurate PA ranged from 25 to 100%** of participants.」
  - 「There is likely a **subset of patients who do not desire accurate prognostic information**,
    although the patient and disease characteristics that predict this preference are currently unknown.」
  - 「This review suggests that patients with MG **desire prognostic information communicated in a manner
    that preserves hope**.」
  - 作者也明說：「**Systematic investigation to define communication needs for prognostic information in
    the unique clinical setting of MG is needed.**」[S49]
  - → 惡性膠質瘤有它自己的處境（認知功能會受影響、家屬常常比病人先知道），
    **而這件事的研究本身還不夠**——這句誠實的話應該寫進去。
- **「三個情境比一個中位數好」的病人偏好實證**：Kiely 2013（Support Care Cancer，505 位有癌症經驗者，
  門診 251 + 乳癌病友團體 254；中位年齡 58 歲、74% 女性、64% 乳癌）[S45]：
  - 相對於「只講中位存活」，「講最好／最壞／典型三個情境」被認為：
    **說得通 93% vs 75%、有幫助 93% vs 69%、能傳達希望 68% vs 44%、令人安心 60% vs 40%**；
    而**「會讓人難過」反而較低：24% vs 36%**（全部 p<0.001）。
  - 認為每一個情境都該講的比例：**最好 89%、最壞 82%、典型 92%**。
  - 問到自己的預後時，**88% 想要三個情境全部，只有 5% 想要單一的中位數**[S45]。
  - **族群標籤要標**：受訪者以乳癌為主，**不是 GBM 病人**。

### 反方向的資料（誠實必列）

- **告知也有代價的證據面**：Enzinger 顯示告知會讓自估餘命**縮短 17.2 個月**、
  並改變 DNR 與照護偏好的機率[S48]——這是**改變決定**，不是中性的。
  正文要誠實：「講清楚會改變你的決定，那正是我講的原因；但這不是無痛的。」
- **不是每個人都想知道**：Diamond 的系統回顧明說有一群人不想要精確的預後資訊，
  而且我們**不知道怎麼事先辨認他們**[S49]；Hagerty 也顯示憂鬱程度較低者較常表示永遠不想談[S51]。
  → **本篇必須給讀者一個「不想看的話可以停在這裡」的出口。**
- **長期存活者裡有帶壞標記的人**[S39]，也有帶好標記卻沒有活久的人
  （Hartmann：11 位帶 IDH 突變卻沒有長期存活，與長期存活者的唯一差別是 MGMT 甲基化較少）[S37]。
  → **兩個方向都要寫**，這正是紅線 1 的雙向。
- **舊文獻的「長期存活者」有相當比例不是今天的 GBM**：Hartmann 的 34% IDH 突變率[S37]、
  Briceno 的 3 例重新分類[S39]、Tykocki 世代的平均診斷年齡 31 歲[S38]。
  → 「有人活了十年」這句話**必須帶上分類的年份**。

### Claim ceiling（B4＝全系列最高紅線，逐條）

**可寫**
- 「中位存活是**一半的人在它之前、一半在它之後**；它是描述一群人的數字，不是為你一個人算的。」
  （方法學支撐：RPA 的 explained variation 只有 18–20%[S33]；Briceno 的結論句
  「generalized predictions of prognosis are inaccurate for individual patients」[S39]）
- 「曲線有尾巴，而且尾巴上的人是真的」：試驗族群五年 9.8%[S2]、真實世界五年 4%[S40]、
  十年約 0.7%[S38]。
- 「兩年、三年這一段真的改善了；五年那一段沒有」[S40]。
- 「已經走過一段之後，前面的機率會改變」：Johnson 的 19.8% → 65.9%[S41]；
  Mueller 的逐年條件存活[S42]。
- 「不同的因素在不同時間說話：切了多少主要影響前面幾個月，MGMT 和年齡影響更後面」[S42]。
- 「把人往右邊推的因素」（逐項帶來源，且各自標明證據等級）：
  **年輕**[S32][S33][S36][S37][S41][S42]、**體能狀態好（KPS）**[S32][S33][S34][S42]、
  **MGMT 甲基化**[S17][S20][S34][S35][S42]、**切除程度／術後殘餘量少**（⚠ **全部是觀察性資料**，
  降半格寫，一句指向 A3 與紅線 2）[S33][S34][S42]、
  **神經功能與心智狀態（MMSE ≥27）**[S33][S34]。
- 「有一種比較誠實的講法：不給一個數字，給三個情境——最好的、最壞的、典型的。
  這種講法在乳癌與肺癌被驗證過，**在腦瘤還沒有**；而問過的病人裡，
  **88% 寧可聽三個情境，只有 5% 想聽一個中位數**」[S43][S44][S45][FAIL-8]。
- 「絕大多數人想知道，而且**知道之後並不會更焦慮、也不會傷害醫病關係**——但它會改變你的決定」[S48]。
- 「有人不想知道，這也是被研究過、被承認的一種選擇」[S49][S51]。
- 「**先告訴家屬**，有 87% 的病人認為那無助於他們保有希望」[S47]——這一條建議寫進正文。
- 一句作者自己的位置（SPEC 要求）：他不給數字當期限的理由，可以建立在
  **RPA 只解釋兩成的變異**[S33] 與 **Briceno 的結論句**[S39] 這兩個可引用的事實上。

**不可寫（硬上限）**
- **「平均只能活 X 個月」**——連「平均」這個詞都不要用（試驗報的是中位數，不是平均數）。
- 任何把單一數字放在句子主詞位置的寫法（「膠質母細胞瘤的存活是 14.6 個月」）。
- **把 Kiely 的 0.25／0.5／2／3 倍數套到 GBM 的中位數上算出月數**——沒有在膠質瘤驗證過[FAIL-8]。
- **把 CBTRUS 的 34.8% 五年相對存活寫成 GBM 的數字**——那是所有惡性腦瘤[S46][FAIL-9]。
- 「有人活了十年」寫成期待、寫成「所以你也可能」；**每一次提到尾巴，都要同時給比例與分類年份**。
- 「治癒」兩個字（SPEC 紅線 1）。
- 任何讓「反正也沒差」讀起來成立的句子——**標準治療的隨機證據要在同一段裡出現**：
  兩年存活 10.4% → 26.5%[S1]、五年 1.9% → 9.8%[S2]、
  高齡族群放療 vs 不放療 HR 0.47[S30]、Cochrane 合併 HR 2.01[S5]。
- 把 Mueller 的 315 人瑞士登記世代條件存活數字寫成「你的機率」[S42]。
- 用 Tykocki 的十年世代（平均診斷年齡 31 歲、舊分類）暗示今天的病人[S38]。
- 勝算比不是機率倍數（固定紅線）——本篇有大量 OR/HR，**每一個都要用「風險比」「勝算比」的正確語意**。

### Caveats／safety notes（寫作者必寫）

1. **本篇要有一個「不想看的話停在這裡」的明確出口**，位置在第一個 h4 之前或之後。
   實證支撐：有一群病人不想要精確的預後資訊，而且無法事先辨認[S49]。
2. **本篇有利益揭露段（SPEC §二逐字）。**
3. **家屬先知道這件事要正面處理**：87% 的病人認為「先告訴家屬」無助於保有希望[S47]，
   而 SPEC §三說台灣的現實常常就是家屬先知道。這段要寫得很小心，**不是責備家屬**，
   是給一個把病人放回討論中心的說法。
4. **每一個「把人往右邊推」的因素都要標證據等級**；切除程度那一項**必須**降半格並指向 A3。
5. **不要在本篇重述治療方案**（歸 B1／B3），也不要重述 MGMT 的檢測細節（歸 A4／B2）。
6. 本篇是其他所有篇章的存活數字出口（SPEC §六）——**其他篇不得出現存活數字當結論**。

### 台灣端

- **台灣的 GBM 存活時間趨勢：查不到可引用的官方資料。** 國健署癌症登記年報的腦瘤分項在本次查證
  未取得可引用原文（Brief A 已標同一 gap）[FAIL-4]。
  → **正文寫「我查不到台灣自己的膠質母細胞瘤存活統計，所以上面每一個數字都是別人的族群」**，
  這句本身就是本篇最誠實的一段。
- **重大傷病**已由 Brief A 查到官方原文（腦惡性腫瘤走第一大項第（五）小項、證明有效期限五年），
  本篇不重查、一句指路 A2。
- 費用相關：本篇不涉及自費項目。

### 給繪圖組的數字（`fig-gb-curve`——全專題最重要的一張）

**這張圖的任務有兩個，缺一不可：讓人看見中位數的位置，也讓人看見尾巴是真的。**

**主軸（建議用 Stupp 2009 的實際百分比畫階梯，不要用倍數法估算）**[S1][S2]
| 時間點 | 放療＋TMZ | 只做放療 |
|---|---|---|
| 中位存活 | **14.6 個月** | 12.1 個月 |
| 2 年 | **27.2%**（22.2–32.5） | 10.9%（7.6–14.8） |
| 3 年 | **16.0%**（12.0–20.6） | 4.4%（2.4–7.2） |
| 4 年 | **12.1%**（8.5–16.4） | 3.0%（1.4–5.7） |
| 5 年 | **9.8%**（6.4–14.0） | 1.9%（0.6–4.4） |

**必須畫進去的三個標註**
1. **中位數的那條線上，要標「一半的人在這邊、一半在那邊」**——這是圖的主要教學點。
2. **尾巴要標實際比例**，並註明「這是 2000–2002 年收案的試驗族群」；
   旁邊放一個對照數字：**真實世界的五年存活約 4%**[S40]。
3. **「走過一段之後，機率會變」**：可用一個小副圖畫 Johnson 的條件機率
   （**再活兩年的機率：診斷當下 19.8% → 診斷後五年 65.9%**）[S41]，
   或 Mueller 的 12 個月條件存活折線（0.51 → 0.46 → 0.41 → 0.43 → 0.56）[S42]。

**可選的第四個標註（若版面允許）**
- **RPA 只解釋了兩成的存活變異**[S33]——建議做成圖說的一句話，不是圖上的元素。

**不要畫的**
- 不要畫「平均值」。
- 不要用 Kiely 的倍數法在 GBM 曲線上標「最好情況」的月數[FAIL-8]；
  若要表現三情境的概念，**用文字說明方法，不要在 GBM 的軸上標數字**。
- 不要畫任何形式的「你在這裡」的指示箭頭。

---

## gb-newthings〈電場、免疫、疫苗、質子、BNCT：各走到哪一格〉（B5）【紅線 7】

> 本篇有利益揭露段（SPEC §二逐字）。**TTFields 的物理與台灣法規身分已在站上〈貼片〉查證過
> （2026-08-30），本 brief 於 2026-09-03 重新確認通過，本篇沿用並一句指路，不重寫**[S75][S71][S72]。
> 質子的物理與法規指向 `nt-proton`／`insight-proton`；BNCT 指向 `nt-bnct`。
> **排擠效應警語照舊**（SPEC §一②）。

### 一、TTFields（電場治療）

**EF-14 主要數字（Stupp 2017 JAMA，2026-09-03 重新確認，可沿用站上〈貼片〉的查證）**[S59]
- **設計**：隨機、**開放標籤**（沒有假裝置對照）、2:1 分派；83 個中心；2009-07 至 2014 年收案，
  追蹤至 2016-12。**n=695（TTFields+TMZ 466、單獨 TMZ 229）**。
- **收案時機（最重要的設計事實）**：「patients with glioblastoma whose tumor was resected or biopsied
  and **had completed concomitant radiochemotherapy**（median time from diagnosis to randomization,
  **3.8 months**）」[S59]
  → **這個試驗收的是「已經撐過六週同步治療、腫瘤沒有立刻惡化」的人**。
  所有數字都要帶這個標籤，否則就是把一群本來就篩選過的人的結果，說成全部病人的結果。
- **介入**：TTFields **200 kHz、每天 ≥18 小時**、頭皮剃光後貼 4 組換能貼片、連接可攜式裝置；
  兩組都用 TMZ **150–200 mg/m²、每 28 天 5 天、6–12 個療程**[S59]。
- **主要終點 PFS（自隨機分派起算）：6.7 vs 4.0 個月；HR 0.63（0.52–0.76），P<.001**
  （在 α=.046 檢定）[S59]。
- **次要終點 OS（階層式檢定，α=.048）：20.9 vs 16.0 個月；HR 0.63（0.53–0.76），P<.001**[S59]。
- **完成率**：695 人中 **637（92%）完成試驗**。中位年齡 56 歲（IQR 48–63），男性 473（68%）[S59]。
- **不良事件**：**全身性不良事件 48% vs 44%**；
  **貼片下方的輕到中度皮膚毒性 52% vs 0%**[S59]。

**每天配戴時數的次族群分析與其限制**（Toms 2019，J Neurooncol，OA；EF-14 的事後次族群分析）[S52]
- 以裝置紀錄的每月使用百分比分組，Cox 模型校正**性別、切除程度、MGMT 甲基化、年齡、地區、
  體能狀態**。
- **50% 這個門檻**：相對於單獨 TMZ，PFS **HR 0.70（0.47–1.05）**、OS **HR 0.67（0.45–0.99）**。
- **>90% 配戴率**：中位存活 **24.9 個月（自診斷起 28.7 個月）**，**5 年存活率 29.3%**。
- **≥75% vs <75%：OS HR 0.78；p=0.031**，且與性別、切除程度、MGMT、年齡、地區、體能狀態獨立。
- **作者自己用的詞是「prognostic」**（標題就是 *…is prognostic for improved survival*）[S52]。
- **必寫的限制（與站上〈貼片〉同一措辭，不得更寬鬆）**：
  這是**事後分析、在同一組人裡面、依一個病人自己部分控制得了的變項分組**；
  能戴到 90% 的人平均而言身體狀況本來就比較好。
  **兩句話都要說**：戴得久的人確實活得比較久，但那不完全是機器的功勞；
  反過來也一樣重要——戴不到 18 小時的人沒有害到自己，**這件事不該變成家裡的壓力來源**。

**指引的位置（要並陳，因為兩邊不一樣）**
- **EANO 2021**：「**Tumour-treating fields remain controversial when applied in the temozolomide
  maintenance setting despite a phase III trial with positive results and are not widely available in
  Europe.**」；同段並註明「questions have been raised regarding the mode of action, the study design…」[S13]
- **Cochrane（高齡族群 NMA）**：因為 EF-14 是在完成化放療之後才隨機，**無法納入網絡統合分析**；
  評語為「the intervention **probably improves overall survival in this selected patient population**」，
  但「evidence on QoL and tolerability is needed in an elderly population」[S31]。
- → 正確寫法：「這是一個第三期隨機試驗做出來的正結果，**而歐洲的指引到今天仍然把它標成有爭議**；
  Cochrane 用的字是 *在這個被篩選過的族群裡，可能改善存活*。」

**還在路上的那一個（2026 年 9 月的現況，可查證）**
- **TRIDENT／EF-32（NCT04471844）**：把 TTFields 提前到**與放療同步**使用；
  隨機、開放標籤；**實際收案 981 人**；狀態 **COMPLETED**，開始 2020-12-08，
  **主要完成日與結案日皆為 2026-02-19**，最後更新 2026-03-30；主要終點 OS。
  **ClinicalTrials.gov 上尚未張貼結果（hasResults = False）**，且 Europe PMC 查不到正式論文[S53]。
- → 可寫：「**還有一個更大的試驗（981 人）在 2026 年 2 月剛做完，結果還沒有公布。**
  如果你正在決定要不要用，這件事值得跟醫師提一句。」

**台灣現況（作者交代的寫法：不寫「本院沒有」、不點名醫院）**
- **健保沒有這個項目**：2026-09-03 匯出健保署「醫療服務給付項目及支付標準」全表（5,995 筆），
  搜「電場」**零筆**[S71]。
- **不在特管辦法附表二**：現行特管辦法（114/12/31 修正、115/1/1 施行）附表二所列的特定醫療儀器裡，
  有電腦斷層掃描儀、磁振造影機、正子斷層掃描儀、**質子機（單治療室／多治療室）**、
  **重粒子治療設備**、深層透熱治療系統等，**沒有任何交流電場類設備**[S72]。
- **醫療器材許可證狀態：查不到**（食藥署許可證查詢站台在本次連線被拒，無法取得官方頁面）
  → **寫「我查不到可以引用的官方資料」，永不推論有無**[FAIL-3]。
- **可及性的寫法**（SPEC §一②）：「**不是每家醫院都有，要用得先問轉去哪裡**」；
  費用寫「**沒有全國統一價，自費收費標準由各縣市主管機關逐家核定，而且它是只要還在治療就持續發生的
  月費型支出**，要一份書面明細，問醫務課」——**絕不寫「值得」**。

### 二、免疫治療：三個第三期，逐一列清楚（三個都沒有達到主要終點，其中一個方向是反的）

**CheckMate-498｜新診斷、MGMT 未甲基化**（Omuro 2023，Neuro-Oncology，OA）[S54]
- **設計**：開放標籤、第三期；**1:1 隨機**；**放療 60 Gy + nivolumab**（240 mg q2w × 8，
  之後 480 mg q4w）**vs 放療 60 Gy + temozolomide**（放療期間 75 mg/m²/日，維持期 150–200 mg/m²，
  每 28 天 5 天）。**注意這是「取代」不是「加上」。**
- **n=560（各 280）**。**主要終點：OS。**
- **結果**：**中位 OS 13.4 個月（12.6–14.3）vs 14.9 個月（13.3–16.1）；
  HR 1.31（1.09–1.58），P=.0037** → **nivolumab 組顯著較差**。
- 中位 PFS **6.0（5.7–6.2）vs 6.2（5.9–6.7）；HR 1.38（1.15–1.65）**。
- 緩解率 **7.8%（9/116）vs 7.2%（8/111）**。
- 安全性：**grade 3/4 治療相關不良事件 21.9% vs 25.1%；任何等級的嚴重治療相關不良事件
  17.3% vs 7.6%**（nivolumab 組較高）。
- 作者結論原文：「The study **did not meet the primary endpoint** of improved OS; **TMZ + RT demonstrated
  a longer mOS than NIVO + RT**. …The difference between the study treatment arms is consistent with the
  use of TMZ + RT as the standard of care for GBM.」[S54]
- → **這一格對 B2 有直接意義**：這是目前唯一一個在「未甲基化」族群裡，把 TMZ 拿掉換成別的東西的
  第三期試驗，而**拿掉 TMZ 的那一組比較差**。EANO 就是引這一點說「這件事又變得有爭議了」[S13]。

**CheckMate-548｜新診斷、MGMT 甲基化或狀態不明**（Lim 2022，Neuro-Oncology，OA）[S55]
- **設計**：**1:1 隨機、單盲（安慰劑對照）**；**標準化放療（放療 60 Gy/6 週 + TMZ）＋ nivolumab
  vs ＋安慰劑**。**這是「加上」不是「取代」。**
- **N=716**。**雙主要終點：PFS 與 OS，分別在「基線未使用類固醇者」與「全部隨機分派者」兩個族群評估。**
- **結果（2020-12-22 資料截止）**：
  - 中位 PFS（獨立中央判讀）**10.6 個月（8.9–11.8）vs 10.3 個月（9.7–12.5）；HR 1.1（0.9–1.3）**
  - 中位 OS **28.9 個月（24.4–31.6）vs 32.1 個月（29.4–33.8）；HR 1.1（0.9–1.3）**
  - 基線未使用類固醇者：**31.3 個月（28.6–34.8）vs 33.0 個月（31.0–35.1）；HR 1.1（0.9–1.4）**
- **安全性：grade 3/4 治療相關不良事件 52.4% vs 33.6%**——**多了近二十個百分點**[S55]。
- 作者結論：「NIVO added to RT + TMZ **did not improve survival**… No new safety signals were observed.」[S55]
- → 對讀者最有用的一句：**在甲基化這一群人身上，加了免疫治療，存活沒有變好，
  但嚴重副作用的比例從三分之一升到一半以上。** 這就是紅線 7 說的「代價」。

**CheckMate-143｜復發**（Reardon 2020，JAMA Oncology，OA）[S56]
- **設計**：開放標籤、第三期；**首次復發**（標準放療與 TMZ 之後）；
  **nivolumab 3 mg/kg vs bevacizumab 10 mg/kg，每 2 週一次**，至確認惡化、無法耐受或死亡。
- 57 個中心、多國；**439 人收案、369 人隨機（各 184／185）**；2014-09 至 2015-05 收案；
  中位追蹤 9.5 個月。**主要終點：OS。**
- **MGMT 分布**：甲基化 23.4%（43/184）／22.7%（42/185）；未甲基化 32.1%（59/184）／36.2%（67/185）；
  其餘未報告。
- **結果**：中位 OS **9.8 個月（8.2–11.8）vs 10.0 個月（9.0–11.8）；HR 1.04（0.83–1.30），P=.76**；
  **12 個月存活率兩組都是 42%**。
- **客觀緩解率：nivolumab 7.8%（4.1–13.3）vs bevacizumab 23.1%（16.7–30.5）** → **免疫組低很多。**
- grade 3/4 治療相關不良事件 33/182（18.1%）vs 25/165（15.2%）；無非預期的神經毒性或治療相關死亡[S56]。
- 作者結論：「Although the **primary end point was not met**…mOS was comparable between nivolumab and
  bevacizumab in the overall patient population with recurrent glioblastoma.」[S56]
- → **注意對照組是 bevacizumab，不是安慰劑**；bevacizumab 本身在復發 GBM 的存活效果也未被證實
  （EANO：「Bevacizumab has **not been compared with placebo**, and an effect on OS was not observed upon
  combination with lomustine as compared with lomustine alone」[S13]）。
  所以正確的話是「**跟一個本身也沒有被證明能延長存活的藥打平**」，不是「跟有效的藥一樣好」。

**一個第二期的正向訊號（要標明它就只是第二期）**
- Cloughesy 2019（Nature Medicine，OA）：**35 位**可手術切除的復發 GBM，隨機分到
  「手術前先給 pembrolizumab、術後續用」vs「只在術後給」。
  「Patients who were randomized to receive **neoadjuvant** pembrolizumab, with continued adjuvant therapy
  following surgery, had **significantly extended overall survival** compared to patients that were
  randomized to receive adjuvant, post-surgical PD-1 blockade alone.」並觀察到腫瘤內 T 細胞與干擾素相關
  基因表現上調[S61]。
- → **可寫的一句**：「有一個 35 個人的小試驗顯示『先給再開刀』和『開完刀才給』結果不一樣，
  這是很有意思的機轉線索——**但它是 35 個人的第二期試驗，不是可以據以治療的證據。**」
  **不可以**寫成「免疫治療換個時機就有效」。

### 三、疫苗

**DCVax-L（Liau 2023，JAMA Oncology，OA）**[S57]
- **試驗身分**：**phase 3, prospective, externally controlled, non-randomized trial**（論文副標自陳）；
  94 個中心、4 個國家；2007-08 至 2015-11 收案；資料分析 2020-10 至 2021-09。
- **收案與分派**：331 人收案，**232 人隨機到 DCVax-L、99 人到安慰劑**；
  比較對象是**同期、以配對方式從其他正式隨機試驗的對照組取得的外部對照族群**。
- **新診斷（n=232）**：中位 OS **19.3 個月（17.5–21.3）自隨機分派起算（自手術起 22.4 個月）
  vs 外部對照 16.5 個月（16.0–17.5）；HR 0.80（98% CI 0.00–0.94），P=.002**。
  **48 個月存活 15.7% vs 9.9%；60 個月 13.0% vs 5.7%。**
- **復發（n=64）**：**13.2 個月（9.7–16.8）vs 7.8 個月（7.2–8.2）；HR 0.58（98% CI 0.00–0.76），P<.001**；
  復發後 24／30 個月存活 20.7% vs 9.6%、11.1% vs 5.1%。
- **MGMT 甲基化的新診斷者**：HR 0.74（98% CI 0.55–1.00），P=.03[S57]。

**外部對照組的設計爭議——SPEC 要求必寫，以下每一條都有可引用的同儕評議來源**[S58]
1. **原始主要終點是 PFS，不是 OS。** 第一份 2018 年的期中報告沒有報 PFS，說要留待專家小組
   多因子中央判讀[S58]。
2. **crossover 把對照組掏空**：設計允許所有病人在復發後接受 DCVax-L；
   「With cross-over at progression, overall, **90% of patients from the two arms, experimental and
   control, received DCVax-L**」[S58]。
3. **主要終點在研究後期被改掉**：「the study design was changed and adapted at later stages of the
   research project, and **the primary endpoint of the study was changed from PFS to OS**」[S58]。
4. **對照組是事後建構的**：以系統性文獻回顧從其他隨機試驗的對照臂選出比較族群，
   再用 **matching-adjusted indirect comparison** 校正[S58]。
5. **評論者的結論句（可直接引）**：「**this study is configured, after modification of the study design
   and of the primary endpoint, as a non-randomized single-arm trial with an external control group**」[S58]。
6. **最後公布的 PFS 是反方向的**：「the median PFS was **6.2 months for the DCVax-L arm and 7.6 months
   for the placebo group（p = 0.47）**」[S58]。
7. **時間跨度**：試驗 2007 年開始、**2008–2011 年因財務因素中止**、2015 年結束，
   **約 90% 的病人是 2012–2015 年才隨機分派的**[S58]。
8. 另一份同儕評議社論的標題本身即為立場：**Preusser & van den Bent,
   *Autologous tumor lysate-loaded dendritic cell vaccination (DCVax-L) in glioblastoma:
   Breakthrough or fata morgana?* Neuro-Oncology 2023;25(4):631–634**[S60]。
   **全文取不到，只能引標題與其存在，不可引內文。**
- → **B5 的寫法**：先照原文寫出它報了什麼數字，再逐條寫出上面 1–7；
  結尾一句：「**一個試驗如果在中途換掉主要終點、換掉對照組，而且兩組有九成的人最後都用到了那個藥，
  它報出來的存活差距就不能當成隨機試驗的證據看。**」

**rindopepimut／ACT IV（Weller 2017，Lancet Oncol）**[S62]
- **設計**：隨機、**雙盲**、國際第三期；**165 家醫院、22 個國家**；
  收 **經中央檢測確認表現 EGFRvIII** 的新診斷 GBM，已完成最大安全切除與標準化放療且未惡化。
- **分層因子**：EORTC RPA class、MGMT 甲基化、地區。**1:1 隨機**：
  rindopepimut（500 μg + GM-CSF 150 μg）vs 對照（keyhole limpet haemocyanin 100 μg），
  每月皮內注射至惡化或無法耐受，同時併用標準口服 TMZ 6–12 個療程或更久。
- **n=745**（**最小殘存病灶 MRD 405 人**、顯著殘存病灶 SRD 338 人、2 人無法評估）；
  2012-04-12 至 2014-12-15 收案。
- **主要終點：MRD 族群的 OS。** **試驗在預設期中分析後因無效（futility）終止。**
- **最終結果**：**中位 OS 20.1 個月（18.5–22.1）vs 20.0 個月（18.1–21.9）；
  HR 1.01（0.79–1.30），p=0.93**。
- 常見 grade 3–4 不良事件（rindopepimut vs 對照）：血小板低下 32（9%）vs 23（6%）、疲倦 6（2%）vs 19（5%）、
  腦水腫 8（2%）vs 11（3%）、癲癇 9（2%）vs 8（2%）、頭痛 6（2%）vs 10（3%）。
  16 例死亡歸因於不良事件（9 vs 7），其中 1 例肺栓塞被評為可能與 rindopepimut 相關[S62]。
- 作者結論：「**Rindopepimut did not increase survival in patients with newly diagnosed glioblastoma.**」[S62]
- → **這是一個設計上幾乎無可挑剔的疫苗試驗（雙盲、中央確認標的、745 人），結果是完全平的。**
  把它和 DCVax-L 並排寫，讀者就會自己看懂「設計嚴謹度」這件事的意義。

### 四、質子

**GBM 的質子證據，三層，全部要標等級**
1. **唯一的隨機資料是 NRG-BN001，而它問的不是「質子好不好」**（完整數字見 B1 D 節）[S7]：
   - 光子中心組加量 vs 標準：**HR 0.95（0.81–1.10），p=0.25**。
   - 質子中心組加量 vs 標準：**HR 0.81（0.67–0.98），p=0.11**。
   - **兩個實驗臂之間（質子 vs 光子）的比較，規約規定只有在兩組都各自打敗自己的對照時才做，
     條件未成立，未執行**[S7]。
   - **必寫的觀察**：質子中心的**兩組**（22.0 與 22.8 個月）都高於光子中心的**兩組**
     （16.3 與 18.8 個月）——**連沒有做質子的對照組都比較高**。這是中心與收案族群的差異，
     不是射線的功勞。**這一段本身就是最好的「怎麼讀試驗」教材。**
   - registry 自陳：質子中心收案比預期慢，因此縮小樣本數、延長追蹤、重算檢定力[S7]。
2. **劑量升高的單一機構經驗（日本，會議摘要層級）**[S66]：
   - 29 位新診斷 GBM，**全部接受超分次同步治療：X 光 50.4 Gy／28 次 + 質子 46.2 Gy(RBE)／28 次
     ＝總量 96.6 Gy(RBE)**，併用 temozolomide。
   - **中位 OS 31.0 個月（95% CI 25.9–36.1）；中位 PFS 11.0 個月（7.8–14.2）**；
     **MGMT 狀態之間看不出存活差異**。
   - 失敗型態：局部復發 17 例、遠端復發 3 例、播散 5 例。
   - **放射性壞死 8 例（含 2 例無症狀）；發生的中位時間為放療後 18.2 個月（10.3–26.2）**。
   - **29 人中有 5 人存活超過 5 年（17.2%），其中 4 人發生了放射性壞死。**
   - 作者結論：「high dose proton beam therapy of 96.6 Gy(RBE) prolonged survival **in selected GBM
     patients**. Particularly in long survivors, **special attention and effective treatment to radiation
     necrosis is a remaining problem.**」[S66]
   - **證據等級標籤（必寫）**：**單一機構、回溯、29 人、會議摘要**——
     **這不是可以據以決定治療的證據**，而且它自己就報出了長期存活者的放射性壞死代價。
3. **沒有其他層級**：Europe PMC 以 `TITLE:"dose-escalated" AND TITLE:"glioblastoma" AND TITLE:"proton"`
   查詢，**命中 0**[FAIL-10]；`TITLE:"proton beam therapy" AND TITLE:"glioblastoma"` 的 10 筆命中
   以個案報告、綜述與會議摘要為主，**沒有第三期隨機試驗**[FAIL-10]。

**台灣的質子現況（這一段查到的東西比預期硬，全部可引）**
- **設備數量**（衛福部醫事司公告附件《全國醫用粒子治療設備設置現況》，**資料截至 113 年 11 月 30 日**）[S74]：
  - **質子治療設備：全國 13 家醫療機構列名，其中「營運中」4 家、「設置中」9 家**
    （北部 5 家、中部 3 家、南部 5 家）。
  - **重粒子治療設備：3 家，其中「營運中」1 家、「設置中」2 家。**
  - **⚠ 該公告逐家列出醫療機構全銜；依 SPEC 固定紅線「不點名機構」，正文只寫家數與地區分布，
    不寫院名。**
- **法規身分**：特管辦法**附表二（特定醫療儀器）**列有「單治療室質子機」「多治療室質子機」與
  「重粒子治療設備」，訂有機構條件（放射腫瘤科專科醫師 5 人以上、醫學物理專業人員 3 人、
  醫事放射師 3 人等）與操作人員資格；其他應遵行事項包含
  「醫療機構應接受中央主管機關所設之**醫用粒子治療設備監督會**督導，建置及運作醫用粒子治療設備；
  並**依中央主管機關規定，收受符合醫用粒子治療適應症之病人、收費及對治療後病人之追蹤管理**」[S72]。
  特管辦法第 35 條：**特定醫療儀器「應符合醫療器材許可證記載之適應症」**[S72]。
- **健保身分**：支付標準全表中質子相關項目為 **N21301–N21308 共八個代碼**
  （3D 電腦斷層模擬、核磁共振模擬攝影含／不含顯影劑、固定模具設計製作、**質子射線治療／次**、
  質子腦部立體定位放射手術、質子身體立體定位放射手術、質子治療電腦治療規劃費），
  **支付點數全部為 0000000、備註欄標示「HTA項目」、生效日 105/12/05**[S71]。
  → **可寫的層次**：「這些項目在健保的表裡有代碼，但**點數是零**、標成 HTA 項目。」
  **不可以**由此推論任何個別醫院的收費金額或給付與否——**費用問醫務課**。
- **衛福部官方同意書範本（衛部醫字第 1101667467A 號公告，110-11-08）**[S73]：
  - 表格的費用欄位標題就是「**各項費用：（單位：新臺幣元）／項目名稱／自費費用**」。
  - **說明書的「處置效益」段落，逐字引用（B5 最有力的台灣端引語）**：
    > 「目前證據顯示相較於傳統放射治療，醫用粒子(質子/重粒子)放射治療對於局限性的腫瘤有較低的
    > 副作用及併發症，提供較好的生活品質。
    > **目前對於治療效果(腫瘤縮小)，僅有間接證據支持醫用粒子(質子/重粒子)放射治療優於傳統放射線治療，
    > 直接證據(前瞻比較性臨床試驗)正在進行中。**
    > 醫用粒子(質子/重粒子)放射治療和傳統放射治療一樣屬於局部治療，仍有遠處器官轉移或未照射部位
    > 發生癌症的可能。
    > **目前世界各國對醫用粒子(質子/重粒子)放射治療的使用上較有共識是適用於治療局限性的腫瘤或
    > 傳統放射治療有效的其他臨床狀況。**」
  - **該範本沒有列出任何適應症清單，也沒有提到膠質母細胞瘤**[S73]。
  - 同一份範本另有兩句可用：「**已告知此處置非屬急迫性質，不於說明當日進行，應經充分時間考慮後
    再決定施作與否**」與「**我瞭解這個治療無法保證一定能改善症狀**」[S73]。
- **「質子用於 GBM 的官方公告」：查不到。** 本次查證未取得任何載明膠質母細胞瘤為
  醫用粒子治療適應症的中央主管機關公告[FAIL-11]。
  → **正文寫：「有沒有一份官方文件說膠質母細胞瘤可以用質子——我查不到。
  我查得到的是：主管機關把它列為需要特別管理的儀器、要求機構依中央規定收案與收費，
  而且在官方的同意書範本上，把療效證據寫成『只有間接證據』。」**

### 五、BNCT

> 站上 `nt-bnct` 已查證台灣端（清華大學 THOR 反應爐、恩慈途徑、官方收費辦法、
> 硼藥在台灣沒有藥證、加速器型中心 2025-08 動工預計 2027 啟用）[S75]，
> **本專題沿用、一句指路、不重寫**；以下只重新確認 **GBM 相關的試驗現況**。

**日本的第二期試驗（GBM 相關證據的主體）**[S68][S69]
- Kawabata 2021（Neuro-Oncology Advances，OA）：加速器型 BNCT（迴旋加速器中子源 BNCT 30 + 硼藥 SPM-011
  500 mg/kg，研究代號 **JG002**），**多中心、開放標籤第二期**；
  2016-02 至 2018-06 收案 **27 位復發惡性膠質瘤，其中 24 位為 glioblastoma**；
  受試者**未曾使用過 bevacizumab**。**主要終點：一年存活率。**
- **結果（復發 GBM）**：**一年存活率 79.2%（95% CI 57.0–90.8）；中位 OS 18.9 個月（12.9–未達）**；
  對照的歷史資料是日本的 bevacizumab 試驗 JO22506：**34.5%（90% CI 20.0–49.0）與 10.5 個月（8.2–12.4）**。
- **⚠ 同一篇論文裡最重要的那個數字**：**依 RANO 判讀的中位 PFS 是 0.9 個月（0.8–1.0）**[S68]。
  → **必寫**：一年存活率 79.2% 與中位 PFS 0.9 個月出現在同一個試驗裡。
  作者的解釋是治療後腦水腫與影像變化讓 RANO 判為惡化；
  **27 人中有 21 人在判定惡化後接受了 bevacizumab**[S68]。
  **這代表存活數字裡混進了後續治療的貢獻，也代表 RANO 在這個情境下量到的東西可能不是真的惡化**
  （這一點與 D1 的假性惡化是同一件事，可一句互相指路）。
- **最主要的不良事件是腦水腫**；作者結論：「AB-BNCT may increase the risk of brain edema due to
  re-irradiation for recurrent MG; however, this appears to be controlled well with bevacizumab.」[S68]
- **延長追蹤（Kawabata 2025，Appl Radiat Isot）**：**一年存活率 79.2%（63.3–88.7）、中位 OS 19.2 個月
  （13.1–24.8）；2 年 33.3%、3 年 20.8%**[S69]。
- **證據等級標籤（必寫）**：**27 人、單臂、對照是歷史資料**——**不是隨機比較**。

**台灣自己的資料（2026 年新發表，可引，但不點名機構）**[S76]
- Chen 等，Neuro-Oncology Advances 2026;8(1):vdag013（OA）：**回溯 171 位復發 GBM 成人**——
  **116 位接受 bevacizumab ±化療（對照組）、55 位接受 BNCT + bevacizumab ±化療**；
  以年齡、體能狀態、復發腫瘤體積、復發到救援治療的間隔、復發次數、再次手術、化療使用做傾向分數配對。
- **配對後世代（n=98）**：
  - **PFS：中位 5.34 vs 3.70 個月；HR 0.54，P=.026（顯著較長）**
  - **OS：HR 0.86，P=.524（沒有差別）**
  - **客觀緩解率：67.4% vs 47.0%，P=.041**
  - 多變項分析：**沒有胼胝體侵犯（OR 0.10，P=.033）與較高的最低吸收劑量（OR 1.09，P=.028）
    與較好的 BNCT 反應獨立相關**。
- 作者結論：「These findings support BNCT as a salvage strategy but **warrant prospective validation**.」[S76]
- → **這是台灣自己的病人資料，而且結果誠實：反應率與 PFS 有差，存活沒有差。**
  **回溯性、傾向分數配對，不是隨機試驗。**

### 六、其他（現況，全部以 2026-09-03 的查證為準）

**regorafenib：從「有希望」走到「被否定」的完整弧線，這是本篇最好的教材**
- **REGOMA（Lombardi 2019，Lancet Oncol）**：義大利 10 個中心、**開放標籤第二期隨機**；
  復發 GBM（手術 + 放療 + TMZ 化放療後惡化）、ECOG 0–1；**n=119（regorafenib 59、lomustine 60）**；
  2015-11-27 至 2017-02-23 收案；中位追蹤 15.4 個月（IQR 13.8–18.1）。
  **主要終點 OS（ITT）：中位 7.4 個月（5.8–12.0）vs 5.6 個月（4.7–7.3）；
  HR 0.50（0.33–0.75），log-rank p=0.0009。**
  grade 3–4 治療相關不良事件 **33/59（56%）vs 24/60（40%）**。
  作者結論用字：「REGOMA showed an **encouraging** overall survival benefit… **should be investigated in
  an adequately powered phase 3 study.**」[S63]
- **GBM AGILE 的第三期驗證（Wen 2026，J Clin Oncol）**[S64]：
  - GBM AGILE（NCT03970447）是**貝氏適應性平台註冊試驗**，多個試驗臂對同一組對照；
    **主要終點 OS**；**regorafenib 是第一個進入的實驗臂**。
  - 納入的次型：**新診斷 MGMT 未甲基化（NDU）與復發（RD）**；對照組為
    「新診斷：TMZ + 放療；復發：lomustine」。
  - 效力判定規則：**當貝氏獲益機率（HR<1.00）≥98% 時判定有效**；
    每月分析，**當所有預設 signature 的貝氏預測檢定力 <25% 時因效力不足停止收案**；
    停收後再追蹤 12 個月。
  - **結果**：因效力不足停止收案。**最終分析在復發與新診斷未甲基化族群都沒有顯示 OS 改善。
    中位 HR：NDU 1.05、RD 1.07、全部 1.07；獲益機率分別為 0.421、0.312、0.296。
    regorafenib 相對於對照有較高的毒性。**
  - 作者結論：「GBM AGILE **did not show superiority of regorafenib** over control in RD (lomustine) or
    NDU (temozolomide + radiotherapy) glioblastoma, **yet caused increased toxicities.**」[S64]
  - **⚠ 該論文的結論最後一句提到某份專業指引已將 regorafenib 移除；
    依 RESEARCH-COMMON 規則本 brief 不引 NCCN，正文亦不得轉述該句。**
  - 另有勘誤一則：J Clin Oncol 2026;44(17):1655[S65]。
- **另一份可引的統合層級證據**：Cochrane 復發 GBM 網絡統合分析（McBain 2021，42 個研究、5,236 人）
  當時的結論是「**REG may improve OS compared with LOM（HR 0.50，0.33–0.76），low-certainty evidence**」
  ——與 REGOMA 同一筆資料，證據確定性標為**低**[S77]。
- → **B5 的寫法**：「有一個第二期試驗說它讓中位存活從 5.6 個月變成 7.4 個月，
  風險比 0.50，看起來很好；**統合分析當時就把它的確定性標成『低』**；
  然後一個更大的、隨機到同一個對照的平台試驗做完了，**沒有做出好處，而且毒性比較高**。
  這就是為什麼第二期的好消息要等第三期。」——**這一段可以當整篇的方法論骨架。**

**paxalisib**
- CT.gov 上 GBM AGILE 的 **「Paxalisib Treatment Arm - Enrollment concluded」**（收案已結束），
  適用族群為新診斷 MGMT 未甲基化 GBM[S16]。
- SNO 2024 有一則 late-breaking 摘要
  （*LTBK-02. Evaluation of paxalisib in GBM AGILE phase 3 registration platform trial for newly diagnosed
  and recurrent glioblastoma*，Neuro-Oncology 2024;26(Suppl 8):viii1）[S78]，
  但 **Europe PMC 上該摘要沒有內文（abstractText 為空），無任何可引用的數字**[FAIL-12]。
- → **正文只能寫：「paxalisib 在這個平台試驗裡的收案已經結束，結果在 2024 年的學會上報告過，
  但我查不到可以引用的完整數字。」不可推論方向。**

**GBM AGILE 平台試驗現況（ClinicalTrials.gov API，2026-09-03）**[S16]
- **NCT03970447**｜狀態 **RECRUITING**；開始 2019-07-30；主要完成 2028-06；預計結案 2030-06；
  **預計收案 2,250 人**；第二／三期；主要終點 OS。
- **試驗臂現況（registry 標籤）**：對照臂；**Regorafenib（收案已結束）**、
  **Paxalisib（收案已結束）**、**VAL-083（收案已結束）**、**VT1021（劑量探索期／強化安全管理期／正式期）**、
  **Troriluzole（劑量探索期）** 等[S16]。
- → **可寫的一句**：「這是一個**還在收案、預計 2030 年才結束**的平台試驗；
  它的設計是讓不同的藥輪流進來、共用同一組對照——**已經有三個藥的收案結束了，
  第一個結束的那個（regorafenib）結果是陰性的。**」
- **怎麼找試驗**指向站上〈sit-trial-how〉，本篇不重寫。

### 反方向的資料（誠實必列）

- **TTFields 是本篇唯一一個第三期隨機正結果**[S59]——負面的東西列了一大堆，
  但**不可以因此把 TTFields 也寫成負的**。同時**必須**並陳：開放標籤、無假裝置對照、
  在完成化放療後才隨機（中位 3.8 個月）、EANO 仍標為 controversial[S13][S59]。
- **BNCT 在台灣自己的資料裡，反應率與 PFS 有差，存活沒有差**[S76]——
  這是「反應不等於守得住」的最直接台灣證據，**要正面寫**。
- **質子在 BN001 的數字看起來好，但那是中心之間的差異**[S7]——
  這是本篇對「新技術」最重要的一個反向提醒。
- **DCVax-L 的 PFS 是反方向的（6.2 vs 7.6 個月）**[S58]。
- **免疫治療的其中一個試驗是顯著較差（HR 1.31）**[S54]，另一個嚴重副作用多了近二十個百分點[S55]。

### Claim ceiling（B5＝紅線 7）

- **可寫**：
  - TTFields：「一個 695 人的第三期隨機試驗，在**已經完成六週同步治療、腫瘤沒有立刻惡化**的病人身上，
    中位存活 16.0 → 20.9 個月，PFS 4.0 → 6.7 個月」[S59]；「一半以上的人會有貼片下方的皮膚問題」[S59]；
    「戴得久的人活得比較久，作者自己用的字是**預後因子**」[S52]；
    「歐洲指引到今天仍然把它標成有爭議」[S13]；「還有一個 981 人、與放療同步的試驗剛做完，
    結果還沒公布」[S53]。
  - 免疫：「三個第三期試驗，**三個都沒有達到主要終點**；其中新診斷未甲基化那一個，
    **用 nivolumab 取代 temozolomide 的那一組顯著較差（HR 1.31，P=.0037）**；
    甲基化那一個加上去之後存活沒變好、嚴重副作用從 33.6% 升到 52.4%；
    復發那一個跟 bevacizumab 打平，但緩解率低很多（7.8% vs 23.1%）」[S54][S55][S56]。
  - 疫苗：「設計最嚴謹的那一個（雙盲、745 人、中央確認 EGFRvIII）結果完全是平的
    （20.1 vs 20.0 個月）」[S62]；「DCVax-L 報出了存活差距，但它在中途換掉主要終點、
    用事後建構的外部對照，而且兩組合計約九成的人最後都用到了那個疫苗；
    最後公布的無惡化存活是反方向的」[S57][S58]。
  - 質子：「唯一的隨機資料問的是**加不加量**，答案是不加量；質子與光子之間的比較**沒有做**」[S7]；
    「日本一個 29 人的單一機構經驗把劑量推到 96.6 Gy(RBE)，中位存活 31 個月，
    但 29 人裡有 8 人出現放射性壞死，長期存活的 5 人裡有 4 人壞死」[S66]；
    「衛福部的官方同意書自己寫著：療效優於傳統放療**只有間接證據**」[S73]。
  - BNCT：「日本 27 人的第二期，一年存活率 79.2%、中位存活 18.9 個月，
    **但同一篇的中位無惡化存活是 0.9 個月**，而且 27 人裡有 21 人之後用了 bevacizumab」[S68]；
    「台灣自己的 171 人回溯配對研究：反應率與無惡化存活較好，**存活沒有差別**」[S76]。
  - 其他：regorafenib 從第二期正結果到平台試驗陰性的完整弧線[S63][S64][S77]；
    GBM AGILE 還在收案、預計 2030 年結束[S16]。
- **不可寫**：
  - **「值得」**（SPEC 紅線 7，硬性）。
  - 任何一個自費金額——**本次查證的自費金額命中為零**（除了站上 nt-bnct 已查證的 BNCT 官方收費辦法，
    本專題**沿用並指路，不在 B5 重寫金額**）→ **寫「問醫務課」**（固定紅線：費用紀律）。
  - 「台灣有／沒有 TTFields 的許可證」——**查不到，不可推論**[FAIL-3]。
  - 「質子可以用在膠質母細胞瘤」的官方背書——**查不到這樣的公告**[FAIL-11]。
  - 「BNCT 對腦瘤有效」——日本試驗是 27 人單臂對歷史對照；台灣資料的存活沒有差別[S68][S76]。
  - 把 BN001 質子組的 22.0／22.8 個月寫成「質子比較好」[S7]。
  - 把 Cloughesy 的 35 人第二期寫成「免疫治療換個時機就有效」[S61]。
  - 把 DCVax-L 的 HR 0.80 當成隨機試驗的效果量[S57][S58]。
  - 把 REGOMA 的 HR 0.50 寫成 regorafenib 有效[S63][S64]。
  - 「本院沒有這台機器」、點名任何醫院（SPEC §一②與固定紅線）。
  - 存活數字當結論——一律一句指向 B4。

### Caveats／safety notes（寫作者必寫）

1. **排擠效應警語照舊**（SPEC §一②）：本篇的治療多數是自費、多在標準治療之外；
   它排擠掉的是還沒用完的標準治療、後線會用到的錢、臨床試驗的資格，以及體能。
2. **TTFields 的家庭負擔要寫**：誰換貼片、頭皮出問題找誰、戴不滿的時候怎麼調整計畫——
   這三題比任何數字實際（沿用站上〈貼片〉的框架）[S75]。
   **戴不滿 18 小時的人沒有害到自己**，這句一定要在。
3. **BNCT 與再照射的腦水腫**：日本試驗最主要的不良事件是腦水腫[S68]；
   腦水腫的警訊症狀歸 C4，一句指路。
4. **質子的放射性壞死**：日本 29 人經驗中 8 例，中位發生時間放療後 18.2 個月[S66]——
   這一條要寫，因為它正好是「活得久才會遇到的代價」。
5. **利益揭露段（SPEC §二逐字）**：作者做的是放療那一段；TTFields 不是他科裡的項目。
6. 本篇不重寫質子物理與 BNCT 法規，一句指路 `nt-proton`／`insight-proton`／`nt-bnct`。

### 台灣端（B5 主場）

| 項目 | 健保代碼 | 特管辦法附表二 | 官方適應症公告 | 本次查證結果 |
|---|---|---|---|---|
| **TTFields（電場）** | **全表搜「電場」零筆**[S71] | **未列**[S72] | 未查到 | 醫療器材許可證**查不到**[FAIL-3]；沿用站上〈貼片〉[S75] |
| **質子** | N21301–N21308，**點數 0、標「HTA項目」**，105/12/05 起[S71] | **列有單／多治療室質子機**[S72] | **查不到載明 GBM 的公告**[FAIL-11] | 全國 13 家、營運中 4 家（113/11/30）[S74]；官方同意書寫「自費費用」「僅有間接證據」[S73] |
| **重粒子** | 全表未見獨立項目[S71] | **列有重粒子治療設備**[S72] | 同上 | 全國 3 家、營運中 1 家（113/11/30）[S74] |
| **BNCT** | **全表搜「中子」「硼」各零筆**[S71] | 未列[S72] | — | 沿用站上 `nt-bnct` 已查證的恩慈途徑與官方收費辦法[S75]，**本篇不重寫金額** |

- **通用的一句（可直接寫進正文）**：「**有代碼不等於有給付，有機器不等於有適應症，
  有許可證不等於這個病可以用。**」——這句在本專題有三個實例撐著：
  質子有代碼但點數是 0[S71]、質子機在特管附表二但沒有 GBM 的適應症公告[S72][FAIL-11]、
  電場治療兩邊都沒有[S71][S72]。指向站上〈核准、給付、有效，是三件不同的事〉。
- **費用**：全文檔搜尋本專題可引用的**官方自費金額為零筆**（BNCT 的官方收費辦法屬 `nt-bnct` 的範圍，
  本篇沿用指路不重寫）→ **依固定紅線，寫「問醫務課」，永不推論、媒體價格不可引。**

### 給繪圖組的數字（B5 若需要圖）

**建議做一張「證據走到哪一格」的對照表，而不是曲線圖。** 每一列標：試驗名／設計／n／主要終點／結果。

| 技術 | 代表試驗 | 設計 | n | 主要終點結果 |
|---|---|---|---|---|
| TTFields | EF-14[S59] | 隨機、**開放標籤**、化放療後才隨機 | 695 | **PFS 6.7 vs 4.0 達標**；OS 20.9 vs 16.0 |
| TTFields（同步） | TRIDENT/EF-32[S53] | 隨機、開放標籤 | 981 | **已完成，結果未公布** |
| 免疫（新診斷未甲基化） | CheckMate-498[S54] | 隨機第三期 | 560 | **未達標，且較差：HR 1.31，P=.0037** |
| 免疫（新診斷甲基化） | CheckMate-548[S55] | 隨機、單盲、安慰劑對照 | 716 | **未達標**：OS HR 1.1；G3/4 AE 52.4% vs 33.6% |
| 免疫（復發） | CheckMate-143[S56] | 隨機第三期，對照 bevacizumab | 369 | **未達標**：OS HR 1.04；ORR 7.8% vs 23.1% |
| 疫苗（胜肽） | ACT IV[S62] | 隨機、**雙盲** | 745 | **未達標**：20.1 vs 20.0 個月；因無效終止 |
| 疫苗（樹突細胞） | DCVax-L[S57][S58] | **非隨機、外部對照**；中途換主要終點 | 331（+外部對照） | OS 19.3 vs 16.5；**PFS 6.2 vs 7.6（反方向）** |
| 質子／劑量升高 | NRG-BN001[S7] | 隨機第二期，**中心組內各自隨機** | 431 可分析 | 光子加量 HR 0.95（p=0.25）；**質子 vs 光子未比較** |
| BNCT | JG002[S68][S69] | **單臂第二期，歷史對照** | 27（24 GBM） | 1 年存活 79.2%；**中位 PFS 0.9 個月** |
| BNCT（台灣） | Chen 2026[S76] | **回溯、傾向分數配對** | 171（配對 98） | PFS HR 0.54（P=.026）；**OS HR 0.86（P=.524）** |
| regorafenib | REGOMA → GBM AGILE[S63][S64] | 第二期隨機 → 貝氏平台第三期 | 119 → 平台 | 第二期 HR 0.50 → **平台試驗陰性，HR 1.05–1.07** |

**這張表的圖說建議**：「**同一個技術，在不同的格子裡是不同的東西。**
看一個新療法，先看它是哪一種設計、收的是哪一群人、主要終點有沒有達標——
再看數字。」

---

## 來源清單（PASS / FAIL 逐條）

**查證路徑代碼**
- `EPMC`＝Europe PMC REST：`https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=<Q>&resultType=core&format=json`
- `EPMC-FT`＝Europe PMC 全文 XML：`https://www.ebi.ac.uk/europepmc/webservices/rest/<PMCID>/fullTextXML`
- `CTG`＝ClinicalTrials.gov API v2：`https://clinicaltrials.gov/api/v2/studies/<NCT>`
- `NHI-PDF` / `MOHW-PDF` / `LAW-PDF`＝官方 PDF 直連 + `pdftotext -layout` 全文搜尋
- 全部查證日期 **2026-09-03**。

### PASS——期刊文獻

**[S1] PASS** — Stupp R, Mason WP, van den Bent MJ, et al. Radiotherapy plus concomitant and adjuvant
temozolomide for glioblastoma. *N Engl J Med.* 2005;352(10):987–996. DOI 10.1056/NEJMoa043330. PMID 15758009.
OA: N（摘要含全部引用數字）。
Route: `EPMC` `EXT_ID:15758009` → hitCount 1，逐欄核對 journal/volume/issue/pages/DOI；
n=573、85 中心、中位年齡 56、84% debulking、60 Gy/2 Gy×30/6 週、TMZ 75 mg/m² 7 天/週、
維持 6 療程 150–200 mg/m² d1–5/28 天、14.6 vs 12.1 個月、HR 0.63（0.52–0.75）、2 年 26.5% vs 10.4%、
同步期 G3/4 血液毒性 7% ——**全部在 abstractText 內可見**。

**[S2] PASS** — Stupp R, Hegi ME, Mason WP, et al. Effects of radiotherapy with concomitant and adjuvant
temozolomide versus radiotherapy alone on survival in glioblastoma in a randomised phase III study:
5-year analysis of the EORTC-NCIC trial. *Lancet Oncol.* 2009;10(5):459–466.
DOI 10.1016/S1470-2045(09)70025-7. PMID 19269895. OA: N。
Route: `EPMC` `EXT_ID:19269895`。2/3/4/5 年存活率與 95% CI、死亡人數 278/286 與 254/287、
HR 0.6、MGMT 僅 206 人可測、「benefit…including patients aged 60–70 years」與
「A few patients in favourable prognostic categories survive longer than 5 years」**皆在摘要內**。

**[S3] PASS** — Bleehen NM, Stenning SP (MRC Brain Tumour Working Party). A Medical Research Council trial
of two radiotherapy doses in the treatment of grades 3 and 4 astrocytoma. *Br J Cancer.* 1991;64(4):769–774.
DOI 10.1038/bjc.1991.396. PMID 1654987. PMCID PMC1977696. **OA: Y**。
Route: `EPMC` `TITLE:"A Medical Research Council trial of two radiotherapy doses…"`。
474 人、2:1（60 Gy 318／45 Gy 156）、9 → 12 個月、HR 0.75、χ²=7.36、P=0.007、
「Over 80%…no morbidity」「**Late morbidity was not assessed**」**皆在摘要內**。

**[S4] PASS（僅書目）／FAIL（數字）** — Walker MD, Strike TA, Sheline GE. An analysis of dose-effect
relationship in the radiotherapy of malignant gliomas. *Int J Radiat Oncol Biol Phys.* 1979;5(10):1725–1731.
DOI 10.1016/0360-3016(79)90553-4. PMID 231022. OA: N。
Route: `EPMC` `TITLE:"An analysis of dose-effect relationship in the radiotherapy of malignant gliomas"`
→ hitCount 1，**abstractText 為空、無 PMCID、全文取不到**。
→ **書目可引，但其劑量反應的任何數字都不可寫入正文。** 需要「劑量有反應」時改用 [S3] 與 [S13]。

**[S5] PASS** — Khan L, Soliman H, Sahgal A, Perry J, Xu W, Tsao MN. External beam radiation dose escalation
for high grade glioma. *Cochrane Database Syst Rev.* 2020;5:CD011475. DOI 10.1002/14651858.CD011475.pub3.
PMID 32437039. PMCID PMC7389526. inEPMC: Y。
Route: `EPMC` `TITLE:"External beam radiation dose escalation for high grade glioma"`。
放療 vs 支持性照護 HR 2.01（1.58–2.55）中等確定性；低分次 vs 常規 HR 0.95（0.78–1.17）**極低**確定性；
≥60 歲 GBM 亞組 HR 1.16（0.92–1.46）**高**確定性；「no randomised trial has compared comfort measures…」
**皆在摘要內**。

**[S6] PASS** — Souhami L, Seiferheld W, Brachman D, et al. Randomized comparison of stereotactic
radiosurgery followed by conventional radiotherapy with carmustine to conventional radiotherapy with
carmustine for patients with glioblastoma multiforme: report of RTOG 93-05 protocol.
*Int J Radiat Oncol Biol Phys.* 2004;60(3):853–860. DOI 10.1016/j.ijrobp.2004.04.011. PMID 15465203. OA: N。
Route: `EPMC` `TITLE:"Randomized comparison of stereotactic radiosurgery followed by conventional
radiotherapy with carmustine"`。n=203、13.5 vs 13.6 個月、p=0.5711、QoL 與認知相當——**摘要內**。

**[S7] PASS** — NRG Oncology. *Dose-Escalated Photon IMRT or Proton Beam Radiation Therapy Versus
Standard-Dose Radiation Therapy and Temozolomide in Treating Patients With Newly Diagnosed Glioblastoma*
(NRG-BN001). ClinicalTrials.gov **NCT02179086**。
Route: `CTG` `https://clinicaltrials.gov/api/v2/studies/NCT02179086`（2026-09-03 讀取）。
取得欄位：overallStatus **ACTIVE_NOT_RECRUITING**、lastUpdatePostDate 2026-08-28、statusVerified 2026-06、
startDate 2014-12-04、primaryCompletion 2025-07-07、completion 2026-12-31、
enrollment 624（ACTUAL）、**hasResults true**；`resultsSection.participantFlowModule`
（FG000 94／FG001 144／FG002 77／FG003 116）、`outcomeMeasuresModule`（主要與次要終點的中位數、95% CI、
Cox HR、log-rank p、規約條件敘述）、`moreInfoModule.limitationsAndCaveats`（收案緩慢、縮小樣本數）。
**⚠ registry 上 Group 2 的 Cox CI（0.67–0.98）與 log-rank p（0.11）並不一致；本 brief 照張貼原樣列出，
正文引用時必須同時寫出兩者，不可只挑其一。**

**[S8] PASS** — Giordano FA, Ganslandt O, Münter MW, et al. Dose escalation with intraoperative radiotherapy
in newly diagnosed glioblastoma (INTRAGO-II): an open-label, multicentre, randomised, controlled, phase 3
trial. *Lancet Oncol.* 2026;27(7):864–878. DOI 10.1016/S1470-2045(26)00235-4. PMID 42372746. OA: N。
Route: `EPMC` `AUTH:"Krex D" AND TITLE:"glioblastoma"` 命中後以 PMID 覆核。
n=314 隨機／298 分析、PFS 11.0 vs 11.4 個月、HR 1.1（0.85–1.44）、p=0.47、
放射性壞死 11（7%）vs 3（2%）p=0.06、結論句——**摘要內**。

**[S9] PASS** — Blumenthal DT, Won M, Mehta MP, et al. Short delay in initiation of radiotherapy may not
affect outcome of patients with glioblastoma: a secondary analysis from the Radiation Therapy Oncology
Group database. *J Clin Oncol.* 2009;27(5):733–739. DOI 10.1200/JCO.2008.18.9035. PMID 19114694.
PMCID PMC2645087. inEPMC: Y。
Route: `EPMC` `TITLE:"Short delay in initiation of radiotherapy may not affect outcome…"`。
2,855 人、四個間隔組、12.5 vs 9.2 個月、P<.0001、結論句「within the relatively narrow constraint of
6 weeks」——**摘要內**。

**[S10] PASS** — Loureiro LV, Pontes LB, Callegaro-Filho D, et al. Waiting time to radiotherapy as a
prognostic factor for glioblastoma patients in a scenario of medical disparities.
*Arq Neuropsiquiatr.* 2015;73(2):104–110. DOI 10.1590/0004-282X20140202. PMID 25742578. OA: N。
Route: `EPMC` `TITLE:"waiting time" AND TITLE:"radiotherapy" AND TITLE:"glioblastoma"`。
n=115、中位等待 6 週、13.5 vs 14.2 個月、HR 1.165（0.770–1.762）p=0.470、
「Although there are no data to ensure that delays to RT are tolerable」——**摘要內**。

**[S11] PASS** — Blumenthal DT, Gorlia T, Gilbert MR, et al. Is more better? The impact of extended adjuvant
temozolomide in newly diagnosed glioblastoma: a secondary analysis of EORTC and NRG Oncology/RTOG.
*Neuro Oncol.* 2017;19(8):1119–1126. DOI 10.1093/neuonc/nox025. PMID 28371907. PMCID PMC5570239. inEPMC: Y。
Route: `EPMC` `TITLE:"Is more better" AND TITLE:"extended adjuvant temozolomide"`。
2,214 → 624 人、291 vs 333、PFS HR 0.80（0.65–0.98）P=.03、甲基化 HR 0.65（0.50–0.85）P<.01、
OS HR 0.92（0.71–1.19）P=.52、甲基化 OS HR 0.89（0.63–1.26）P=.51——**摘要內**。

**[S12] PASS** — Balana C, Vaz MA, Sepúlveda JM, et al. A phase II randomized, multicenter, open-label trial
of continuing adjuvant temozolomide beyond 6 cycles in patients with glioblastoma (GEINO 14-01).
*Neuro Oncol.* 2020;22(12):1851–1861. DOI 10.1093/neuonc/noaa107. PMID 32328662. PMCID PMC7746946. inEPMC: Y。
Route: `EPMC` `TITLE:"A phase II randomized, multicenter, open-label trial of continuing adjuvant
temozolomide"`。20 家醫院、166 篩選／159 納入（79 vs 80）、6 個月 PFS 55.7% vs 61.3%、
淋巴球低下 P<0.001、血小板低下 P<0.001、噁心嘔吐 P=0.001、MGMT 與無可測量病灶為獨立因子——**摘要內**。

**[S13] PASS** — Weller M, van den Bent M, Preusser M, et al. EANO guidelines on the diagnosis and treatment
of diffuse gliomas of adulthood. *Nat Rev Clin Oncol.* 2021;18(3):170–186. DOI 10.1038/s41571-020-00447-z.
PMID 33293629. PMCID PMC7904519. **OA: Y**。
Route: `EPMC` `TITLE:"EANO guidelines on the diagnosis and treatment of diffuse gliomas of adulthood"`
→ `EPMC-FT` `PMC7904519/fullTextXML`（105,622 字元），逐句抓取。
本 brief 引用的每一段（GBM 建議框、MGMT 檢測方法、「Immunocytochemistry is not an adequate method」、
高齡 40 Gy/15 次與 5×5 Gy 的保留、TTFields「remain controversial」、bevacizumab「not been compared with
placebo」、「60 Gy…approximately doubling median OS」、KPS 總則、「This notion has become controversial
again」）**全部來自該全文，字句照原文**。

**[S14] PASS（附屬）** — Weller M, van den Bent M, Preusser M, et al. Author Correction: EANO guidelines on
the diagnosis and treatment of diffuse gliomas of adulthood. *Nat Rev Clin Oncol.* 2022;19(5):357–358.
DOI 10.1038/s41571-022-00623-3. PMID 35322237. PMCID PMC9038523. OA: Y。
Route: `EPMC` 同上查詢。**列出以示已檢查勘誤存在；本 brief 引用的段落不在勘誤範圍。**

**[S15] PASS（會議摘要，僅用於規約措辭）** — Weller M, Lim M, Idbaih A, et al. CTIM-25. A randomized phase 3
study of nivolumab or placebo combined with radiotherapy plus temozolomide in patients with newly diagnosed
glioblastoma with methylated MGMT promoter: CheckMate 548. *Neuro Oncol.* 2021;23(Suppl 6):vi55–vi56.
PMCID PMC8598415. inEPMC: Y。
Route: `EPMC` `TITLE:"CheckMate 548"`。**本 brief 只取其中對標準治療的規約描述**：
「TMZ (75 mg/m² QD during RT, **then 4-week break**, then 150–200 mg/m² QD on days 1–5 of every 28-day
cycle for 6 cycles)」。**療效數字以正式論文 [S55] 為準，不引本摘要的數字。**

**[S16] PASS** — Global Coalition for Adaptive Research. *GBM AGILE: Global Adaptive Trial Master Protocol…*
ClinicalTrials.gov **NCT03970447**。
Route: `CTG`（2026-09-03 讀取）。overallStatus **RECRUITING**、lastUpdatePostDate 2026-07-30、
statusVerified 2026-06、start 2019-07-30、primaryCompletion 2028-06、completion 2030-06、
enrollment 2,250（ESTIMATED）、phases PHASE2/PHASE3、primaryOutcome Overall Survival；
armGroups 標籤（Control Arm；Regorafenib／Paxalisib／VAL-083 皆標 *Enrollment concluded*；
VT1021 三個階段；Troriluzole 劑量探索期）；對照臂敘述含
「Rest Period 2-6 weeks from the last day of radiation…」。

**[S17] PASS** — Hegi ME, Diserens AC, Gorlia T, et al. MGMT gene silencing and benefit from temozolomide in
glioblastoma. *N Engl J Med.* 2005;352(10):997–1003. DOI 10.1056/NEJMoa043331. PMID 15758010. OA: N。
Route: `EPMC` `EXT_ID:15758010`。甲基化 45%/206、HR 0.45（0.32–0.61）P<0.001、
21.7（17.4–30.4）vs 15.3（13.0–20.9）P=0.007、「smaller and statistically insignificant difference」、
結論句——**摘要內**。**未甲基化的具體月數不在本文摘要，改由 [S18] 提供。**

**[S18] PASS** — Alnahhas I, Alsawas M, Rayi A, et al. Characterizing benefit from temozolomide in MGMT
promoter unmethylated and methylated glioblastoma: a systematic review and meta-analysis.
*Neurooncol Adv.* 2020;2(1):vdaa082. DOI 10.1093/noajnl/vdaa082. PMID 33150334. PMCID PMC7596890. **OA: Y**。
（另有勘誤：*Neurooncol Adv.* 2021;3(1):vdab095，DOI 10.1093/noajnl/vdab095，PMID 34258581，已檢視。）
Route: `EPMC` → `EPMC-FT` `PMC7596890/fullTextXML`（29,101 字元），逐句抓取。
本 brief 引用：未甲基化 RT/TMZ N=655 OS 14.11（13.18–15.04）、PFS 4.99（4.25–5.72）；
甲基化 N=753 OS 24.59（22.19–26.99）、N=805 PFS 9.51（7.41–11.61）；高齡未甲基化 RT-only N=223
OS 8.35（6.46–10.25）；**EORTC 26981 未甲基化的分層數字（RT 11.8[9.7–14.1] n=54 / RT+TMZ 12.7
[11.6–14.4] n=60；PFS 5.9[5.3–7.7] n=46 / 10.3[6.5–14] n=46）出自該全文 Discussion 段的轉引**；
以及三句作者原文與其實務立場段落。**⚠ 摘要與全文的未甲基化 OS 95% CI 略有出入
（摘要 13.18–15.04；Discussion 段作 12.85–17.97）；本 brief 採摘要值，正文亦採摘要值。**

**[S19] PASS（僅書目與標題）** — Hegi ME, Stupp R. Withholding temozolomide in glioblastoma patients with
unmethylated MGMT promoter—still a dilemma? *Neuro Oncol.* 2015;17(11):1425–1427. DOI 10.1093/neuonc/nov198.
PMID 26374690. PMCID PMC4648310. OA: N（inEPMC: Y，但 fullTextXML 回傳空）。
Route: `EPMC` `EXT_ID:26374690`；`EPMC-FT` `PMC4648310/fullTextXML` → **空回應**。
→ **只能引標題與其存在（「連 MGMT 檢測的原作者自己都把這題寫成 dilemma」），不可引內文。**

**[S20] PASS** — Hegi ME, Genbrugge E, Gorlia T, et al. MGMT promoter methylation cutoff with safety margin
for selecting glioblastoma patients into trials omitting temozolomide: a pooled analysis of four clinical
trials. *Clin Cancer Res.* 2019;25(6):1809–1816. DOI 10.1158/1078-0432.CCR-18-3181. PMID 30514777.
PMCID PMC8127866. inEPMC: Y。
Route: `EPMC` `EXT_ID:30514777`。4,041 有效結果／1,725 隨機、切點 1.27 與 −0.28（AUC 0.61）、
灰帶約 10%、HR 0.35（0.27–0.45）與 0.58（0.43–0.78）、「more methylation was not related to better
outcome」、重測 R²=0.94、結論句——**摘要內**。

**[S21] PASS** — Brandner S, McAleenan A, Kelly C, et al. MGMT promoter methylation testing to predict overall
survival in people with glioblastoma treated with temozolomide: a comprehensive meta-analysis based on a
Cochrane Systematic Review. *Neuro Oncol.* 2021;23(9):1457–1469. DOI 10.1093/neuonc/noab105. PMID 34467991.
PMCID PMC8408882. **OA: Y**。
Route: `EPMC` `TITLE:"MGMT promoter methylation" AND TITLE:"glioblastoma" AND TITLE:"meta-analysis"`。
32 個世代／3,474 人、MSP 與 PSQ 優於免疫組化、PSQ 略優於 MSP、CpG 位置範圍、
9% vs 28%/29% 切點的比較、「does not provide strong evidence about the best CpG sites or threshold」
——**摘要內**。

**[S22] PASS** — Gilbert MR, Wang M, Aldape KD, et al. Dose-dense temozolomide for newly diagnosed
glioblastoma: a randomized phase III clinical trial (RTOG 0525). *J Clin Oncol.* 2013;31(32):4085–4091.
DOI 10.1200/JCO.2013.49.6968. PMID 24101040. PMCID PMC3816958. inEPMC: Y。
Route: `EPMC` `TITLE:"Dose-dense temozolomide for newly diagnosed glioblastoma"`。
n=833、OS 16.6 vs 14.9 HR 1.03 P=.63、PFS 5.5 vs 6.7 HR 0.87 P=.06、
MGMT 甲基化 OS 21.2 vs 14.0 HR 1.74 P<.001、PFS 8.7 vs 5.7 HR 1.63 P<.001、緩解 P=.012、
G≥3 毒性 34% vs 53% P<.001——**摘要內**。

**[S23] PASS** — Herrlinger U, Tzaridis T, Mack F, et al. Lomustine-temozolomide combination therapy versus
standard temozolomide therapy in patients with newly diagnosed glioblastoma with methylated MGMT promoter
(CeTeG/NOA-09): a randomised, open-label, phase 3 trial. *Lancet.* 2019;393(10172):678–688.
DOI 10.1016/S0140-6736(18)31791-4. PMID 30782343. OA: N。
Route: `EPMC` `EXT_ID:30782343`。17 家德國大學醫院、18–70 歲、KPS ≥70、141 隨機／129 mITT（63 vs 66）、
放療 59–60 Gy、31.4（27.7–47.1）vs 48.1（32.6–未達）個月、HR 0.60（0.35–1.03）p=0.0492、
ITT p=0.0432、G≥3 AE 51% vs 59%、無治療相關死亡、「should be interpreted with caution, owing to the
small size of the trial」——**摘要內**。

**[S24] PASS** — Feldheim J, Kessler AF, Monoranu CM, Ernestus RI, Löhr M, Hagemann C. Changes of
O6-methylguanine DNA methyltransferase (MGMT) promoter methylation in glioblastoma relapse—a meta-analysis
type literature review. *Cancers (Basel).* 2019;11(12):1837. DOI 10.3390/cancers11121837. PMID 31766430.
PMCID PMC6966671. **OA: Y**。
Route: `EPMC` `TITLE:"MGMT promoter methylation" AND TITLE:"glioblastoma" AND TITLE:"meta-analysis"`。
115/476（24%，CI 0.21–0.28）改變、可能原因（技術、異質性、選擇壓力）、
「The clinical implications are still ambiguous and do not yet support a change in clinical practice」
——**摘要內**。

**[S25] PASS** — Roa W, Brasher PM, Bauman G, et al. Abbreviated course of radiation therapy in older patients
with glioblastoma multiforme: a prospective randomized clinical trial. *J Clin Oncol.* 2004;22(9):1583–1588.
DOI 10.1200/JCO.2004.06.082. PMID 15051755. OA: N。
Route: `EPMC` `TITLE:"Abbreviated course of radiation therapy in older patients with glioblastoma multiforme"`。
n=100、≥60 歲、60 Gy/30 vs 40 Gy/15、5.1 vs 5.6 個月 P=.57、6 個月存活 44.7% vs 41.7%、
KPS Wilcoxon P=.63、**類固醇加量 49% vs 23%，χ² P=.02**、FACT-Br 完成率 45%——**摘要內**。

**[S26] PASS** — Roa W, Kepka L, Kumar N, et al. International Atomic Energy Agency randomized phase III study
of radiation therapy in elderly and/or frail patients with newly diagnosed glioblastoma multiforme.
*J Clin Oncol.* 2015;33(35):4145–4150. DOI 10.1200/JCO.2015.62.6606. PMID 26392096. OA: N。
Route: `EPMC` 全標題查詢。98 人、三類收案定義（frail／elderly & frail／elderly 各自的年齡與 KPS 條件）、
25 Gy/5 vs 40 Gy/15、7.9（6.3–9.6）vs 6.4（5.1–7.6）P=.988、PFS 4.2 vs 4.2 P=.716、
中位追蹤 6.3 個月、4 週與 8 週 QoL 無差異——**摘要內**。

**[S27] PASS** — Malmström A, Grønberg BH, Marosi C, et al. Temozolomide versus standard 6-week radiotherapy
versus hypofractionated radiotherapy in patients older than 60 years with glioblastoma: the Nordic
randomised, phase 3 trial. *Lancet Oncol.* 2012;13(9):916–926. DOI 10.1016/S1470-2045(12)70265-6.
PMID 22877848. OA: N。ISRCTN81470623。
Route: `EPMC` `EXT_ID:22877848`。342 收案／291 三組（93/98/100）＋51 兩組（26/25）、
TMZ 200 mg/m² d1–5/28 最多 6 療程、34.0 Gy/3.4 Gy/2 週、60.0 Gy/2.0 Gy/6 週、
8.3（7.1–9.5）vs 6.0（5.1–6.8）HR 0.70（0.52–0.93）p=0.01、7.5（6.5–8.6）HR 0.85（0.64–1.12）p=0.24、
242 人 TMZ vs 低分次 HR 0.82（0.63–1.06）p=0.12、>70 歲 HR 0.35（0.21–0.56）與 0.59（0.37–0.93）、
MGMT 分層（TMZ 組 HR 0.56 p=0.02；放療組 HR 0.97 p=0.81）、毒性人數與 2 例致死性感染——**摘要內**。

**[S28] PASS** — Wick W, Platten M, Meisner C, et al. Temozolomide chemotherapy alone versus radiotherapy
alone for malignant astrocytoma in the elderly: the NOA-08 randomised, phase 3 trial.
*Lancet Oncol.* 2012;13(7):707–715. DOI 10.1016/S1470-2045(12)70164-X. PMID 22578793. OA: N。NCT01502241。
Route: `EPMC` `EXT_ID:22578793`。584 篩選／412 收案／373 分析（195 vs 178）、>65 歲、KPS ≥60、
TMZ 100 mg/m² d1–7 一週開一週停、放療 60.0 Gy/30 次 1.8–2.0 Gy/6–7 週、非劣性 margin 25%、
8.6（7.3–10.2）vs 9.6（8.2–10.8）HR 1.09（0.84–1.42）p(ni)=0.033、EFS 3.3 vs 4.7 HR 1.15 p(ni)=0.043、
MGMT 甲基化 73/209（35%）、11.9 vs 8.2 個月 HR 0.62（0.42–0.91）p=0.014、
EFS 分層（甲基化 8.4 vs 4.6；未甲基化 3.3 vs 4.6）、毒性逐項人數（**淋巴球低下 46 vs 1、
血栓栓塞 24 vs 8**）——**摘要內**。

**[S29] PASS** — Perry JR, Laperriere N, O'Callaghan CJ, et al. Short-course radiation plus temozolomide in
elderly patients with glioblastoma (CCTG CE.6). *N Engl J Med.* 2017;376(11):1027–1037.
DOI 10.1056/NEJMoa1611977. PMID 28296618. OA: N。NCT00482677。
Route: `EPMC` `EXT_ID:28296618`。n=562（各 281）、≥65 歲、中位 73（65–90）、**兩組放療皆 40 Gy/15 次**、
OS 9.3 vs 7.6 HR 0.67（0.56–0.80）P<0.001、PFS 5.3 vs 3.9 HR 0.50（0.41–0.60）P<0.001、
甲基化 n=165 13.5 vs 7.7 HR 0.53（0.38–0.73）P<0.001、未甲基化 n=189 10.0 vs 7.9 HR 0.75（0.56–1.01）
P=0.055、交互作用 P=0.08、「Quality of life was similar in the two trial groups」——**摘要內**。

**[S30] PASS** — Keime-Guibert F, Chinot O, Taillandier L, et al. Radiotherapy for glioblastoma in the elderly.
*N Engl J Med.* 2007;356(15):1527–1535. DOI 10.1056/NEJMoa065901. PMID 17429084. OA: N。NCT00430911。
Route: `EPMC` `EXT_ID:17429084`。≥70 歲、KPS ≥70、10 個中心、85 隨機／81 GBM 分析、
中位 73 歲（70–85）、放療 50 Gy/1.8 Gy 分次、**29.1 週（n=39）vs 16.9 週（n=42）、HR 0.47（0.29–0.76）
P=0.002**、期中分析即停止、「no severe adverse events related to radiotherapy」、
QoL 與認知評估「did not differ significantly」——**摘要內**。

**[S31] PASS** — Hanna C, Lawrie TA, Rogozińska E, et al. Treatment of newly diagnosed glioblastoma in the
elderly: a network meta-analysis. *Cochrane Database Syst Rev.* 2020;3:CD013261.
DOI 10.1002/14651858.CD013261.pub2. PMID 32202316. PMCID PMC7086476. inEPMC: Y。
Route: `EPMC` `DOI:"10.1002/14651858.CD013261.pub2"`。12 個 RCT／約 1,818 人、7 種介入、
CRT vs RT40 HR 0.67（0.56–0.80）高確定性、TMZ vs CRT HR 1.42（1.01–1.98）低確定性、
BEV_CRT vs CRT HR 0.83（95% CrI 0.48–1.44）、排序、
「We could not compare the survival effects of CRT with different radiotherapy fractionation schedules
(60 Gy/30 fractions and 40 Gy/15 fractions) due to a lack of data」、PFS HR 0.50 與 0.28、
QoL 溝通障礙 P=0.002、TMZ vs RT60 血栓 RR 2.74（1.26–5.94）、BEV 加 CRT 血栓 RR 16.63（1.00–275.42）、
TTFields 段落、兩句結論——**摘要內**。

**[S32] PASS** — Curran WJ Jr, Scott CB, Horton J, et al. Recursive partitioning analysis of prognostic
factors in three Radiation Therapy Oncology Group malignant glioma trials.
*J Natl Cancer Inst.* 1993;85(9):704–710. DOI 10.1093/jnci/85.9.704. PMID 8478956. OA: N。
Route: `EPMC` 全標題查詢。1,578 人、1974–1989 年三個試驗、26＋6 個變項、
年齡 50 歲為第一切點、≥50 歲以體能狀態為最重要變項、12 個亞組、中位存活 4.7–58.6 個月、
亞組人數 32–256、目的敘述句——**摘要內**。

**[S33] PASS** — Li J, Wang M, Won M, et al. Validation and simplification of the Radiation Therapy Oncology
Group recursive partitioning analysis classification for glioblastoma.
*Int J Radiat Oncol Biol Phys.* 2011;81(3):623–630. DOI 10.1016/j.ijrobp.2010.06.012. PMID 20888136.
PMCID PMC3783211. inEPMC: Y。
Route: `EPMC` 全標題查詢。1,672 GBM ＋ 488 測試集、42 個基線變項、
原模型 explained variation **20% vs 15%**、簡化版 **18%**、四個變項（年齡、體能狀態、切除程度、神經功能）、
三類中位存活 **17.1／11.2／7.5 個月**——**摘要內**。

**[S34] PASS** — Gorlia T, van den Bent MJ, Hegi ME, et al. Nomograms for predicting survival of patients
with newly diagnosed glioblastoma: prognostic factor analysis of EORTC and NCIC trial 26981-22981/CE.3.
*Lancet Oncol.* 2008;9(1):29–38. DOI 10.1016/S1470-2045(07)70384-4. PMID 18082451. OA: N。
Route: `EPMC` 全標題查詢。573 人三個建模族群（573／287／**103**）、各族群的獨立預後因子
（TMZ、切除範圍、年齡、MMSE ≥27、基線類固醇；體能狀態；MGMT）、
工具網址 http://www.eortc.be/tools/gbmcalculator 、「exploratory subanalysis」——**摘要內**。

**[S35] PASS** — Patil N, Somasundaram E, Waite KA, et al. Independently validated sex-specific nomograms for
predicting survival in patients with newly diagnosed glioblastoma: NRG Oncology RTOG 0525 and 0825.
*J Neurooncol.* 2021;155(3):363–372. DOI 10.1007/s11060-021-03886-5. PMID 34761331. PMCID PMC8651582.
inEPMC: Y。
Route: `EPMC` `TITLE:"Nomograms for predicting survival of patients with newly diagnosed glioblastoma"`。
752 建模／599 驗證、共同顯著因子（年齡、KPS、MGMT、腫瘤位置）、切除程度與類固醇僅男性顯著、
輸出 6/12/24 個月機率——**摘要內**。

**[S36] PASS** — Krex D, Klink B, Hartmann C, et al. Long-term survival with glioblastoma multiforme.
*Brain.* 2007;130(Pt 10):2596–2606. DOI 10.1093/brain/awm204. PMID 17785346. OA: N。
Route: `EPMC` `TITLE:"Long-term survival with glioblastoma multiforme" AND SRC:MED AND PUB_YEAR:2007`。
「3–5% of the patients survives for more than 3 years」、55 位長期存活者、年輕＋KPS 好、
「None of the evaluated socioeconomic, environmental and occupational factors were associated with
long-term survival」、MGMT 28/36（74%）、TP53 9/31（29%）、EGFR 10/38（26%）、1p/19q 2/32（6%）、
與 141 位連續病人比較 MGMT 顯著較常見——**摘要內**。

**[S37] PASS** — Hartmann C, Hentschel B, Simon M, et al. Long-term survival in primary glioblastoma with
versus without isocitrate dehydrogenase mutations. *Clin Cancer Res.* 2013;19(18):5146–5157.
DOI 10.1158/1078-0432.CCR-13-0017. PMID 23918605. OA: N。
Route: `EPMC` 全標題查詢。69 位 LTS-36（含 33 位 LTS-60）vs 257 位對照、
**IDH1/2 突變 34%（23/67）vs 4.3%（11/257）**、IDH 突變 LTS 的特徵、
「IDH1/2 wild-type showed no distinguishing features…except for a higher rate of MGMT promoter
methylation」、11 位 IDH 突變但非長期存活者的比較——**摘要內**。

**[S38] PASS** — Tykocki T, Eltayeb M. Ten-year survival in glioblastoma. A systematic review.
*J Clin Neurosci.* 2018;54:7–13. DOI 10.1016/j.jocn.2018.05.002. PMID 29801989. OA: N。
Route: `EPMC` `TITLE:"Ten-year survival in glioblastoma"`。
36 篇研究／162 例（1950–2014 年發表）、long survivors 比例 **0.76%**、10 年存活率 **0.71%**、
平均診斷年齡 31.1±11.1、OS 15.9±6.3 年、PFS 11.9±5.6 年、全切 82／次全切 58／切片 9、
兩者間 PFS/OS/年齡無統計差異——**摘要內**。
**⚠ 使用限制：世代橫跨 1950–2014 年、多數無 IDH 檢測，正文引用時必須標明分類年代。**

**[S39] PASS** — Briceno N, Vera E, Komlodi-Pasztor E, et al. Long-term survivors of glioblastoma: Tumor
molecular, clinical, and imaging findings. *Neurooncol Adv.* 2024;6(1):vdae019.
DOI 10.1093/noajnl/vdae019. PMID 38420614. PMCID PMC10901543. OA: N（inEPMC: Y，
`EPMC-FT` 回傳空 → **僅用摘要**）。
Route: `EPMC` `TITLE:"long-term survivors" AND TITLE:"glioblastoma" AND TITLE:"molecular"`；
`EPMC-FT PMC10901543` → 空回應。
摘要內可引：分子確認 IDH 野生型、LTS ≥3 年 n=23／STS <3 年 n=75、NGS 23/74、甲基化分析 18/28、
影像 14 vs 28；LTS 較年輕、T1 低訊號較多、**富含 MGMTp 甲基化與 TP53 突變**；
**「Three patients with classic GBM histology were reclassified based on NGS and methylation testing.」**；
**「Additionally, there were LTS with typical poor prognostic molecular markers.」**；
結論句「generalized predictions of prognosis are inaccurate for individual patients」。

**[S40] PASS** — Poon MTC, Sudlow CLM, Figueroa JD, Brennan PM. Longer-term (≥2 years) survival in patients
with glioblastoma in population-based studies pre- and post-2005: a systematic review and meta-analysis.
*Sci Rep.* 2020;10(1):11622. DOI 10.1038/s41598-020-68011-4. PMID 32669604. PMCID PMC7363854. **OA: Y**。
PROSPERO CRD42019130035。
Route: `EPMC` 全標題查詢。23 個族群／63 篇研究、2 年 9%（6–12%，1,488/17,507）→ 18%（14–22%，
5,670/32,390）、3 年 4%（2–6%，325/10,556）→ 11%（9–14%，1,900/16,397）、
5 年 3%（1–5%，401/14,919）→ 4%（2–5%，1,291/28,748）、結論兩句——**摘要內**。

**[S41] PASS** — Johnson DR, Ma DJ, Buckner JC, Hammack JE. Conditional probability of long-term survival in
glioblastoma: a population-based analysis. *Cancer.* 2012;118(22):5608–5613. DOI 10.1002/cncr.27590.
PMID 22569786. OA: N。
Route: `EPMC` `TITLE:"Long-term survival" AND TITLE:"glioblastoma" AND TITLE:"population-based"`。
SEER 1998–2008、含放療方案、n=10,022、中位存活 12.61 個月、
**再活兩年的條件機率 19.8%（診斷當下）→ 65.9%（診斷後 5 年）**、
2005–2008 vs 1998–2004 的多時點比較、只有年齡在三個時點皆顯著（P<.0001）、結論三句——**摘要內**。

**[S42] PASS** — Mueller T, Vasella F, Velz J, et al. Conditional survival in glioblastoma: The evolution of
prognostic factors over time. *Int J Cancer.* 2026;158(10):2571–2580. DOI 10.1002/ijc.70285. PMID 41472359.
PMCID PMC12996738. **OA: Y**。
Route: `EPMC` `TITLE:"conditional survival" AND TITLE:"glioblastoma"`。
315 位 IDH 野生型 GBM 前瞻登記（2008-01–2017-06）、12 個月條件存活於 s=0/6/12/18/24 為
0.51（0.45–0.56）／0.46（0.39–0.52）／0.41（0.33–0.49）／0.43（0.33–0.52）／0.56（0.42–0.67）、
s=0 的顯著因子（年齡 >60、術前腫瘤環狀體積 >20 cm³、無 MGMT 甲基化、術後 KPS ≥70、
術後殘餘 >1 cm³ 或僅切片）、
**「Residual tumor volume mainly influences survival in the initial months following surgery, while MGMT
promoter methylation and age remain significant predictors beyond this period.」**——**摘要內**。

**[S43] PASS** — Kiely BE, Soon YY, Tattersall MH, Stockler MR. How long have I got? Estimating typical,
best-case, and worst-case scenarios for patients starting first-line chemotherapy for metastatic breast
cancer: a systematic review of recent randomized trials. *J Clin Oncol.* 2011;29(4):456–463.
DOI 10.1200/JCO.2010.30.2174. PMID 21189397. OA: N。
Route: `EPMC` `AUTH:"Kiely BE" AND TITLE:"best case"`。36 個試驗／13,083 位女性、
四個百分位數對應四個情境、簡單倍數 0.25／0.5／2／3、準確度 73%／97%／95%／96%、結論句——**摘要內**。
**族群標籤：轉移性乳癌，非膠質瘤。**

**[S44] PASS** — Kiely BE, Alam M, Blinman P, Tattersall MH, Stockler MR. Estimating typical, best-case and
worst-case life expectancy scenarios for patients starting chemotherapy for advanced non-small-cell lung
cancer: a systematic review of contemporary randomized trials. *Lung Cancer.* 2012;77(3):537–544.
DOI 10.1016/j.lungcan.2012.04.017. PMID 22609149. OA: N。
Route: 同上查詢。60 個試驗／29,657 人、各比值（0.26／0.53／1.81／2.84）與可近似的 0.25/0.5/2/3——**摘要內**。
**族群標籤：晚期非小細胞肺癌，非膠質瘤。**

**[S45] PASS** — Kiely BE, McCaughan G, Christodoulou S, et al. Using scenarios to explain life expectancy in
advanced cancer: attitudes of people with a cancer experience. *Support Care Cancer.* 2013;21(2):369–376.
DOI 10.1007/s00520-012-1526-4. PMID 22717918. OA: N。
Route: `EPMC` 全標題查詢。505 位受訪者（門診 251／乳癌病友團體 254）、中位 58 歲、74% 女性、64% 乳癌、
三情境 vs 中位數的五項比較（93/75、93/69、68/44、60/40、24/36，皆 p<0.001）、
應呈現比例（最好 89%、最壞 82%、典型 92%）、**88% 想要三個情境、5% 想要單一中位數**——**摘要內**。
**族群標籤：以乳癌為主的癌症經驗者，非 GBM 病人。**

**[S46] PASS（僅用於發生率與整體惡性腦瘤存活）** — Price M, Ballard CAP, Benedetti JR, Kruchko C,
Barnholtz-Sloan JS, Ostrom QT. CBTRUS Statistical Report: Primary Brain and Other Central Nervous System
Tumors Diagnosed in the United States in 2018–2022. *Neuro Oncol.* 2025;27(Supplement_4):iv1–iv66.
DOI 10.1093/neuonc/noaf194. PMID 41092086. OA: N。
Route: `EPMC` `TITLE:"CBTRUS Statistical Report" AND TITLE:"2018-2022"`。
摘要內：AAAIR 26.05（惡性 6.86／非惡性 19.19）、glioblastoma 佔全部 13.7%、佔惡性 52.2%、男性較多、
**惡性腦與 CNS 腫瘤五年相對存活率 34.8%**（非惡性 91.7%）。
**⚠ GBM 專屬的五年存活率不在摘要內、全文不可取得（見 FAIL-9）；34.8% 若要引用必須明寫它涵蓋
所有惡性腦瘤。本 brief 建議不引。**

**[S47] PASS** — Hagerty RG, Butow PN, Ellis PM, et al. Communicating with realism and hope: incurable cancer
patients' views on the disclosure of prognosis. *J Clin Oncol.* 2005;23(6):1278–1288.
DOI 10.1200/JCO.2005.11.138. PMID 15718326. OA: N。
Route: `EPMC` 全標題查詢。126 位（218 位受邀，58%）、
98% 要求務實／可提問／被當個別的人看、給希望行為（90%／87%／87%）、
**不利希望行為（醫師顯得緊張 91%、先告知家屬 87%、使用委婉語 82%）**、
六種風格與三個希望因子、最被認同的兩種風格——**摘要內**。**族群標籤：無法治癒的轉移性癌症，澳洲。**

**[S48] PASS** — Enzinger AC, Zhang B, Schrag D, Prigerson HG. Outcomes of prognostic disclosure:
associations with prognostic understanding, distress, and relationship with physician among patients with
advanced cancer. *J Clin Oncol.* 2015;33(32):3809–3816. DOI 10.1200/JCO.2015.61.9239. PMID 26438121.
PMCID PMC4737862. inEPMC: Y。
Route: `EPMC` `TITLE:"Outcomes of Prognostic Disclosure" AND TITLE:"Advanced Cancer"`。
590 人、中位存活 5.4 個月、71% 想知道／17.6% 記得被告知、
299 位自估者的中位 12（IQR 6–36）vs 48（IQR 12–180）個月 P<.001、
差 >2 年 30.2% vs 49.2%（OR 0.45，0.14–0.82）、差 >5 年 9.5% vs 35.5%（OR 0.19，0.08–0.47）、
校正後減少 17.2 個月（6.2–28.2）、DNR aOR 0.439（0.296–0.630）、
偏好延長生命 aOR 1.493（1.091–1.939）、結論兩句——**摘要內**。
**族群標籤：化療後仍惡化的轉移性實體癌，非 GBM。**

**[S49] PASS** — Diamond EL, Corner GW, De Rosa A, Breitbart W, Applebaum AJ. Prognostic awareness and
communication of prognostic information in malignant glioma: a systematic review.
*J Neurooncol.* 2014;119(2):227–234. DOI 10.1007/s11060-014-1487-1. PMID 24874468. PMCID PMC5116439.
inEPMC: Y。
Route: `EPMC` 全標題查詢。14 篇研究、定義與測量方式不一、**準確預後認知的盛行率 25–100%**、
「likely a subset of patients who do not desire accurate prognostic information」、
「desire prognostic information communicated in a manner that preserves hope」、
「Systematic investigation…is needed」——**摘要內**。**這是本 brief 唯一一筆膠質瘤專屬的溝通文獻。**

**[S50] PASS（僅書目與身分，不引內文）** — Clark TG, Bradburn MJ, Love SB, Altman DG.
Survival analysis part I: basic concepts and first analyses. *Br J Cancer.* 2003;89(2):232–238.
DOI 10.1038/sj.bjc.6601118. PMID 12865907. PMCID PMC2394262. **OA: Y**。
Route: `EPMC` 全標題查詢（**abstractText 為空**；未抓取全文）。
→ **可作為「存活分析與 Kaplan–Meier 的教學性方法學文獻」引用其存在；
若正文要引任何句子，必須先抓 `EPMC-FT PMC2394262` 逐句核對。本 brief 未做此步。**

**[S51] PASS** — Hagerty RG, Butow PN, Ellis PA, et al. Cancer patient preferences for communication of
prognosis in the metastatic setting. *J Clin Oncol.* 2004;22(9):1721–1730. DOI 10.1200/JCO.2004.04.095.
PMID 15117995. OA: N。
Route: `EPMC` 全標題查詢。126 位、澳洲 12 家門診、30 位腫瘤科醫師、
>95%／85%／80%／81% 的資訊需求、「Words and numbers were preferred over pie charts or graphs」、
59% 於診斷轉移時即想討論、38%／44% 想協商時機、
憂鬱分數與偏好的關聯（P=.047／P=.049／P=.03）、結論句——**摘要內**。
**族群標籤：無法治癒的轉移性癌症，澳洲。**

**[S52] PASS** — Toms SA, Kim CY, Nicholas G, Ram Z. Increased compliance with tumor treating fields therapy
is prognostic for improved survival in the treatment of glioblastoma: a subgroup analysis of the EF-14
phase III trial. *J Neurooncol.* 2019;141(2):467–473. DOI 10.1007/s11060-018-03057-z. PMID 30506499.
PMCID PMC6342854. **OA: Y**。
Route: `EPMC` 全標題查詢。50% 門檻 PFS HR 0.70（0.47–1.05）、OS HR 0.67（0.45–0.99）；
>90% 配戴中位存活 24.9 個月（自診斷 28.7）、5 年 29.3%；≥75% vs <75% HR 0.78 p=0.031；
Cox 模型校正變項清單——**摘要內**。**標題自陳 prognostic。**

**[S53] PASS** — NovoCure. *EF-32: Pivotal, Randomized, Open-Label Study of Optune® (Tumor Treating Fields,
200 kHz) Concomitant With Radiation Therapy and Temozolomide for the Treatment of Newly Diagnosed
Glioblastoma* (TRIDENT). ClinicalTrials.gov **NCT04471844**。
Route: `CTG`（2026-09-03 讀取）。overallStatus **COMPLETED**、lastUpdatePostDate 2026-03-30、
statusVerified 2026-03、start 2020-12-08、primaryCompletion 2026-02-19、completion 2026-02-19、
enrollment **981（ACTUAL）**、primaryOutcome Overall Survival（5 years）、**hasResults false**。
另以 `EPMC` `TITLE:"TRIDENT" AND TITLE:"glioblastoma"` 查詢，僅得試驗設計的會議摘要，
**無正式結果論文**。

**[S54] PASS** — Omuro A, Brandes AA, Carpentier AF, et al. Radiotherapy combined with nivolumab or
temozolomide for newly diagnosed glioblastoma with unmethylated MGMT promoter: An international randomized
phase III trial (CheckMate 498). *Neuro Oncol.* 2023;25(1):123–134. DOI 10.1093/neuonc/noac099.
PMID 35419607. PMCID PMC9825306. **OA: Y**。NCT02617589。
Route: `EPMC` 全標題查詢。560 人（各 280）、劑量與給法、
OS 13.4（12.6–14.3）vs 14.9（13.3–16.1）**HR 1.31（1.09–1.58）P=.0037**、
PFS 6.0 vs 6.2 HR 1.38（1.15–1.65）、緩解率 7.8%（9/116）vs 7.2%（8/111）、
G3/4 TRAE 21.9% vs 25.1%、任何等級嚴重 TRAE 17.3% vs 7.6%、結論句——**摘要內**。

**[S55] PASS** — Lim M, Weller M, Idbaih A, et al. Phase III trial of chemoradiotherapy with temozolomide
plus nivolumab or placebo for newly diagnosed glioblastoma with methylated MGMT promoter (CheckMate 548).
*Neuro Oncol.* 2022;24(11):1935–1949. DOI 10.1093/neuonc/noac116. PMID 35511454. PMCID PMC9629431.
**OA: Y**。NCT02667587。
Route: `EPMC` 全標題查詢。N=716、雙主要終點與兩個評估族群、劑量與給法、
PFS 10.6（8.9–11.8）vs 10.3（9.7–12.5）HR 1.1（0.9–1.3）、OS 28.9（24.4–31.6）vs 32.1（29.4–33.8）
HR 1.1（0.9–1.3）、無類固醇者 31.3 vs 33.0 HR 1.1（0.9–1.4）、
**G3/4 TRAE 52.4% vs 33.6%**、結論句——**摘要內**。

**[S56] PASS** — Reardon DA, Brandes AA, Omuro A, et al. Effect of nivolumab vs bevacizumab in patients with
recurrent glioblastoma: The CheckMate 143 phase 3 randomized clinical trial.
*JAMA Oncol.* 2020;6(7):1003–1010. DOI 10.1001/jamaoncol.2020.1024. PMID 32437507. PMCID PMC7243167.
**OA: Y**。NCT02017717。
Route: `EPMC` 全標題查詢。439 收案／369 隨機（184/185）、57 個中心、2014-09–2015-05、
中位追蹤 9.5 個月、MGMT 分布、OS 9.8（8.2–11.8）vs 10.0（9.0–11.8）HR 1.04（0.83–1.30）P=.76、
**12 個月存活率兩組皆 42%**、ORR 7.8%（4.1–13.3）vs 23.1%（16.7–30.5）、
G3/4 TRAE 33/182（18.1%）vs 25/165（15.2%）、結論句——**摘要內**。

**[S57] PASS** — Liau LM, Ashkan K, Brem S, et al. Association of autologous tumor lysate-loaded dendritic
cell vaccination with extension of survival among patients with newly diagnosed and recurrent glioblastoma:
A phase 3 prospective externally controlled cohort trial. *JAMA Oncol.* 2023;9(1):112–121.
DOI 10.1001/jamaoncol.2022.5370. PMID 36394838. PMCID PMC9673026. **OA: Y**。NCT00045968。
Route: `EPMC` 全標題查詢。94 個中心／4 國／2007-08–2015-11、331 收案（232 vs 99）、
nGBM 19.3（17.5–21.3）自隨機（22.4 自手術）vs 16.5（16.0–17.5）HR 0.80（98% CI 0.00–0.94）P=.002、
48/60 個月 15.7% vs 9.9%、13.0% vs 5.7%；rGBM n=64，13.2（9.7–16.8）vs 7.8（7.2–8.2）
HR 0.58（98% CI 0.00–0.76）P<.001、24/30 個月 20.7% vs 9.6%、11.1% vs 5.1%；
nGBM 甲基化 HR 0.74（98% CI 0.55–1.00）P=.03；**標題即自陳 externally controlled、non-randomized**
——**摘要內**。

**[S58] PASS** — Gatto L, Di Nunno V, Tosoni A, Bartolini S, Ranieri L, Franceschi E. DCVax-L vaccination in
patients with glioblastoma: Real promise or negative trial? The debate is open.
*Cancers (Basel).* 2023;15(12):3251. DOI 10.3390/cancers15123251. PMID 37370860. PMCID PMC10296384.
**OA: Y**。
Route: `EPMC` `TITLE:"DCVax"` → `EPMC-FT PMC10296384/fullTextXML`（41,654 字元），逐句抓取。
本 brief 引用的每一條（原主要終點為 PFS、2018 年期中報告未報 PFS、crossover 使兩組合計約 90% 用到
DCVax-L、主要終點由 PFS 改為 OS、以文獻回顧建構外部對照並用 matching-adjusted indirect comparison、
「this study is configured…as a non-randomized single-arm trial with an external control group」、
**PFS 6.2 vs 7.6 個月 p=0.47**、2007 年開始／2008–2011 中止／約 90% 於 2012–2015 隨機）
**全部出自該全文**。

**[S59] PASS** — Stupp R, Taillibert S, Kanner A, et al. Effect of tumor-treating fields plus maintenance
temozolomide vs maintenance temozolomide alone on survival in patients with glioblastoma: A randomized
clinical trial (EF-14). *JAMA.* 2017;318(23):2306–2316. DOI 10.1001/jama.2017.18718. PMID 29260225.
PMCID PMC5820703. inEPMC: Y。NCT00916409。
Route: `EPMC` `EXT_ID:29260225`。695 人（466/229）、83 個中心、2009-07–2014 收案、追蹤至 2016-12、
**randomized after completing concomitant radiochemotherapy；median time from diagnosis to randomization
3.8 months**、200 kHz／≥18 h/day／4 組貼片、TMZ 150–200 mg/m² 5/28 天 6–12 療程、
PFS 6.7 vs 4.0 HR 0.63（0.52–0.76）P<.001（α=.046）、OS 20.9 vs 16.0 HR 0.63（0.53–0.76）P<.001
（階層式，α=.048）、637/695（92%）完成、中位年齡 56（IQR 48–63）、男性 473（68%）、
全身性 AE 48% vs 44%、**皮膚毒性 52% vs 0%**、開放標籤——**摘要內**。

**[S60] PASS（僅書目與標題）** — Preusser M, van den Bent MJ. Autologous tumor lysate-loaded dendritic cell
vaccination (DCVax-L) in glioblastoma: Breakthrough or fata morgana? *Neuro Oncol.* 2023;25(4):631–634.
DOI 10.1093/neuonc/noac281. PMID 36562460. inEPMC: Y（**fullTextXML 未取得**）。
Route: `EPMC` `TITLE:"DCVax"`。→ **只能引標題與其存在（顯示領域內對 DCVax-L 有正式的質疑聲音），
不可引內文。實質批評內容一律用 [S58]。**

**[S61] PASS** — Cloughesy TF, Mochizuki AY, Orpilla JR, et al. Neoadjuvant anti-PD-1 immunotherapy promotes
a survival benefit with intratumoral and systemic immune responses in recurrent glioblastoma.
*Nat Med.* 2019;25(3):477–486. DOI 10.1038/s41591-018-0337-7. PMID 30742122. PMCID PMC6408961. **OA: Y**。
Route: `EPMC` 全標題查詢。**35 人**、隨機、多機構、neoadjuvant vs adjuvant pembrolizumab、
「significantly extended overall survival」、免疫學次要發現——**摘要內**。
**⚠ 只能寫成「35 人的第二期訊號」。**

**[S62] PASS** — Weller M, Butowski N, Tran DD, et al. Rindopepimut with temozolomide for patients with newly
diagnosed, EGFRvIII-expressing glioblastoma (ACT IV): a randomised, double-blind, international phase 3
trial. *Lancet Oncol.* 2017;18(10):1373–1385. DOI 10.1016/S1470-2045(17)30517-X. PMID 28844499. OA: N。
NCT01480479。
Route: `EPMC` `TITLE:"Rindopepimut with temozolomide for patients with newly diagnosed"`。
165 家醫院／22 國、中央檢測 EGFRvIII、分層因子（EORTC RPA class、MGMT、地區）、
745 人（MRD 405／SRD 338／2 無法評估）、371 vs 374、2012-04-12–2014-12-15、
**因無效終止**、MRD OS 20.1（18.5–22.1）vs 20.0（18.1–21.9）HR 1.01（0.79–1.30）p=0.93、
G3–4 AE 逐項人數、16 例 AE 相關死亡（9 vs 7）、結論句——**摘要內**。

**[S63] PASS** — Lombardi G, De Salvo GL, Brandes AA, et al. Regorafenib compared with lomustine in patients
with relapsed glioblastoma (REGOMA): a multicentre, open-label, randomised, controlled, phase 2 trial.
*Lancet Oncol.* 2019;20(1):110–119. DOI 10.1016/S1470-2045(18)30675-2. PMID 30522967. OA: N。NCT02926222。
Route: `EPMC` `TITLE:"Regorafenib compared with lomustine in patients with relapsed glioblastoma"`。
義大利 10 個中心、ECOG 0–1、124 篩選／119 隨機（59/60）、2015-11-27–2017-02-23、
中位追蹤 15.4 個月（IQR 13.8–18.1）、regorafenib 160 mg/日 每 4 週的前 3 週；
lomustine 110 mg/m² 每 6 週；OS 7.4（5.8–12.0）vs 5.6（4.7–7.3）HR 0.50（0.33–0.75）p=0.0009、
G3–4 治療相關 AE 33/59（56%）vs 24/60（40%）、結論「encouraging…should be investigated in an
adequately powered phase 3 study」——**摘要內**。
（同一試驗的生活品質次要終點：Lombardi G, et al. *Eur J Cancer.* 2021;155:179–190. PMID 34388515；
本 brief 未引用其數字。）

**[S64] PASS** — Wen PY, Berry DA, Buxton MB, et al. Evaluation of regorafenib in newly diagnosed and
recurrent glioblastoma: GBM AGILE phase II/III Bayesian randomized platform trial.
*J Clin Oncol.* 2026;44(18):1676–1686. DOI 10.1200/JCO-25-01137. PMID 41980234. OA: N。NCT03970447。
Route: `EPMC` `TITLE:"GBM AGILE"`。試驗設計（貝氏適應性平台、共同對照、主要終點 OS、
獲益機率 ≥98% 判定有效、預測檢定力 <25% 停收、停收後追蹤 12 個月）、
納入次型 NDU 與 RD、對照臂內容、**中位 HR 1.05（NDU）／1.07（RD）／1.07（全部）、
獲益機率 0.421／0.312／0.296**、毒性較高、結論句——**摘要內**。
**⚠ 該摘要最後一句提及某專業指引已移除 regorafenib；依 RESEARCH-COMMON「不引 NCCN」，
本 brief 不轉述該句，正文亦不得使用。**

**[S65] PASS（附屬）** — Wen PY, Berry DA, Buxton MB, et al. Erratum: Evaluation of regorafenib in newly
diagnosed and recurrent glioblastoma: GBM AGILE phase II/III Bayesian randomized platform trial.
*J Clin Oncol.* 2026;44(17):1655. DOI 10.1200/JCO-26-01027. PMID 42096661. OA: N。
Route: `EPMC` 同上查詢。**列出以示已檢查勘誤存在。**

**[S66] PASS（會議摘要層級，證據等級必須標明）** — Matsuda M, Mizumoto M, Kohzuki H, Sugii N, Ishikawa E.
RT-4: Treatment outcome of proton beam therapy for glioblastoma. *Neurooncol Adv.* 2021;3(Suppl 6):vi15.
PMCID PMC8664621. **OA: Y**。
Route: `EPMC` `TITLE:"proton beam therapy" AND TITLE:"glioblastoma"`。
29 位新診斷 GBM、X 光 50.4 Gy/28 + 質子 46.2 Gy(RBE)/28 = **96.6 Gy(RBE)**、併用 TMZ、
中位 OS 31.0 個月（25.9–36.1）、中位 PFS 11.0（7.8–14.2）、MGMT 無顯著差異、
失敗型態 17/3/5、**放射性壞死 8 例（含 2 例無症狀），中位發生 18.2 個月（10.3–26.2）**、
**5 年以上存活 5/29（17.2%），其中 4 人發生壞死**、結論句——**摘要內**。
**⚠ 單一機構、回溯、n=29、會議摘要。正文引用時必須逐項標明。**

**[S67] PASS（會議摘要，僅用於 BN001 認知次要終點）** — Wefel J, DeMora L, Gondi V, et al.
CTNI-50. Neurocognitive function (NCF) of the photon cohort in NRG-BN001.
*Neuro Oncol.* 2020;22(Suppl 2):ii53–ii54. PMCID PMC7651205. inEPMC: Y。
Route: `EPMC` `TITLE:"BN001"`。229 位可分析（2014-10–2018-07）、
CTB COMP 於 cycle 3（p=0.370，Cohen's d=0.22）與 cycle 12（p=0.977，d=0.01）皆無組間差異、
混合效應模型交互作用 p=0.216、基線完成率 93–94%、cycle 3 為 66–68%、cycle 12 為 51–54%——**摘要內**。
**療效數字以 [S7] 的 registry 張貼結果為準，不引本摘要的存活敘述。**

**[S68] PASS** — Kawabata S, Suzuki M, Hirose K, et al. Accelerator-based BNCT for patients with recurrent
glioblastoma: a multicenter phase II study (JG002). *Neurooncol Adv.* 2021;3(1):vdab067.
DOI 10.1093/noajnl/vdab067. PMID 34151269. PMCID PMC8209606. **OA: Y**。
Route: `EPMC` 全標題查詢。多中心、開放標籤第二期、2016-02–2018-06、27 位復發惡性膠質瘤（24 GB）、
BNCT 30 + SPM-011 500 mg/kg、bevacizumab-naïve、主要終點一年存活率、
**1 年 79.2%（57.0–90.8）、中位 OS 18.9 個月（12.9–未達）**、歷史對照 JO22506 為 34.5%（90% CI 20.0–49.0）
與 10.5（8.2–12.4）、**中位 PFS 0.9 個月（0.8–1.0）（RANO）**、最主要 AE 為腦水腫、
**27 人中 21 人於惡化後接受 bevacizumab**、結論句——**摘要內**。

**[S69] PASS** — Kawabata S, Goto H, Narita Y, et al. Extended follow-up of recurrent glioblastoma patients
treated with boron neutron capture therapy (BNCT): Long-term survival from a phase II trial (JG002) using
cyclotron neutron source and boronophenylalanine. *Appl Radiat Isot.* 2025;226:112118.
DOI 10.1016/j.apradiso.2025.112118. PMID 40865370. OA: N。
Route: `EPMC` `TITLE:"BNCT" AND TITLE:"recurrent" AND TITLE:"glioblastoma" AND SRC:MED`。
**1 年 79.2%（63.3–88.7）、中位 OS 19.2 個月（13.1–24.8）、2 年 33.3%、3 年 20.8%**、
模型外推說明——**摘要內**。

**[S76] PASS** — Chen SF, Lee YY, Liu CY, et al. Boron neutron capture therapy plus bevacizumab versus
bevacizumab alone in recurrent glioblastoma: A propensity score-matched analysis.
*Neurooncol Adv.* 2026;8(1):vdag013. DOI 10.1093/noajnl/vdag013. PMID 42137821. PMCID PMC13168812.
**OA: Y**。
Route: `EPMC` `TITLE:"boron neutron capture therapy" AND TITLE:"glioblastoma"`。
171 位復發 GBM（116 對照／55 BNCT）、配對變項清單、配對後 n=98、
**PFS 5.34 vs 3.70 個月 HR 0.54 P=.026；OS HR 0.86 P=.524；ORR 67.4% vs 47.0% P=.041**；
多變項（無胼胝體侵犯 OR 0.10 P=.033；較高最低吸收劑量 OR 1.09 P=.028）、
結論「warrant prospective validation」——**摘要內**。
**⚠ 台灣族群、回溯、傾向分數配對。正文引用時不點名機構（SPEC 固定紅線）。**

**[S77] PASS（僅用於 regorafenib 的證據確定性標籤）** — McBain C, Lawrie TA, Rogozińska E, Kernohan A,
Robinson T, Jefferies S. Treatment options for progression or recurrence of glioblastoma: a network
meta-analysis. *Cochrane Database Syst Rev.* 2021;5:CD013579. DOI 10.1002/14651858.CD013579.pub2.
PMID 34559423. PMCID PMC8121043. inEPMC: Y。
Route: `EPMC` 全標題查詢。42 個研究／5,236 人、以 lomustine 為參考、
**「Regorafenib (REG): REG may improve OS compared with LOM (HR 0.50, 95% CI 0.33 to 0.76;
low-certainty evidence)」**、bevacizumab 相關結果、
「We found no high-certainty evidence that any treatments tested were better than lomustine」——**摘要內**。
**本 brief 只用其 regorafenib 的確定性標籤；復發治療的完整內容屬 D3，不在 B 組展開。**

**[S78] FAIL（僅存在，無可引用內容）** — *LTBK-02. Evaluation of paxalisib in GBM AGILE phase 3
registration platform trial for newly diagnosed and recurrent glioblastoma.*
*Neuro Oncol.* 2024;26(Suppl 8):viii1. PMCID PMC11583046。
Route: `EPMC` `PMCID:PMC11583046` → **title 有、abstractText 為 None，無任何數字**。
→ **正文只能寫「結果在 2024 年學會上報告過，我查不到可以引用的完整數字」，不可推論方向。**

### PASS——官方文件（台灣）

**[S70] PASS** — 衛生福利部中央健康保險署。《全民健康保險藥品給付規定》**第 9 節 抗癌瘤藥物
Antineoplastics drugs**（最新版分章節檔，頁面標示 115.8.21 更新）。
PDF：`https://www.nhi.gov.tw/ch/dl-55685-99c675b771ab4b2789c891bc8db447ce-1.pdf`（102 頁）。
Route: 先以 WebFetch 取得「最新版藥品給付規定內容(分章節)」頁面
（`https://www.nhi.gov.tw/ch/np-3397-1.html`）上的第 9 節 PDF 連結，
再 `curl -sSL` 直連 PDF（HTTP 200，1,310,289 bytes）→ `pdftotext -layout` 全文（291,445 字元）→
`grep -n Temozolomide` 定位第 437 行。**HTML 頁面直接 curl 會被 Cloudflare 擋（HTTP 403），
PDF 直連可以——與食道癌專題實測一致。**
本 brief 逐字引用：**9.25 Temozolomide（如 Temodal）**（沿革 94/3/1、97/1/1、98/9/1、111/9/1，附表八之二）
全文三款；並核對 **9.35 carmustine 植入劑（如 Gliadel Wafer）**（100/2/1，附表八之四，
「不得與 temozolomide 併用」）與 **bevacizumab 之「2.惡性神經膠質瘤(WHO 第4級)-神經膠母細胞瘤」**
（101/05/1，單獨使用於標準放療與含 TMZ 化療失敗之復發成人患者，事前審查每次 12 週為限）。

**[S71] PASS** — 衛生福利部中央健康保險署。《全民健康保險醫療服務給付項目及支付標準》
**全部診療項目匯出檔（txt）**。
檔案：`https://www.nhi.gov.tw/ch/dl-82681-605f2232ad1448ae82aac171042713c7-1.txt`
（HTTP 200，21,371,491 bytes，5,995 筆診療項目）。
Route: 以 WebFetch 取得「全民健康保險醫療服務給付項目及支付標準」頁面
（`https://www.nhi.gov.tw/ch/cp-5943-f1cce-2821-1.html`）上的檔案清單，再 `curl -sSL` 直連 txt；
以 `grep` 與 Python 逐欄解析（欄位：代碼^支付點數^生效日^截止日^英文名稱^中文名稱^備註）。
**本次查證的關鍵結果（2026-09-03）**：
- `grep -c "電場"` → **0**；`grep -c "中子"` → **0**；`grep -c "硼"` → **0**；
  `grep -c "粒子"` → **0**；`grep -c "重粒子"` → **0**。
- 「質子」→ 8 筆診療項目 **N21301–N21308**，**支付點數欄皆為 `0000000`**，生效日 `20161205`，
  **備註欄皆為「HTA項目」**：質子治療 3D 電腦斷層模擬／核磁共振模擬攝影（不含、含顯影劑）／
  固定模具之設計及製作／**質子射線治療/次**／質子腦部立體定位放射手術（療程約 3 次）／
  質子身體立體定位放射手術（療程約 6 次）／質子治療電腦治療規劃費。
- 放療相關項目核對：36011B–36013B（直線加速器遠隔照射治療，簡單／複雜／緊急照野，
  1,231／1,334／1,601 點）、36015B 電腦治療規劃--複雜 11,483 點、36021C 3D 電腦斷層模擬攝影 8,500 點、
  36018B 模擬定位攝影 3,619 點、37016B／37030B 固定模具 1,943／1,657 點、
  37028B 三度空間立體定位Ｘ光刀 82,000 點、37029B 加馬機立體定位放射手術 153,229 點、
  37047B 身體立體定位放射治療 213,662 點；**低分次放療專屬項目僅 36022B／36023B（乳癌）與
  36024B（直腸癌）**；「強度調控」一詞僅出現於 36015B 的說明文字中，**無獨立項目**。

**[S72] PASS** — 全國法規資料庫。《特定醫療技術檢查檢驗醫療儀器施行或使用管理辦法》
（**修正日期：民國 114 年 12 月 31 日；第 44 條：一百十四年十二月三十一日修正發布之條文，
自一百十五年一月一日施行**）。
法規本文：`https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=L0020075`（HTTP 200）。
附件（`LawGetFile.ashx?FileId=…&lan=C`）：
**附表一** FileId `0000410579`（第三十二條附表一修正規定）、
**附表二** FileId `0000286926`（9 頁）、附表三 `0000286927`、附表四 `0000286928`。
Route: `curl -sSL` 法規本文 HTML → 去標籤後 `count("電場") = 0`；
`curl -sSL` 四份附表 PDF → `pdftotext -layout` → 附表二 `grep -c "電場" = 0`、`grep -c "質子" = 1`
（第八項「多治療室質子機」；同表另列第七項單治療室質子機與第九項「重粒子治療設備」）；
附表一 `grep -c "電場" = 0`。
本 brief 引用：第 34 條「醫療機構施行或設置特定醫療儀器之項目、醫療機構條件、操作人員資格及其他
應遵行事項，規定如附表二」；第 35 條「…**應符合醫療器材許可證記載之適應症**」；
附表二質子機／重粒子條目的機構條件與其他應遵行事項
（含「醫療機構應接受中央主管機關所設之**醫用粒子治療設備監督會**督導…並**依中央主管機關規定，
收受符合醫用粒子治療適應症之病人、收費及對治療後病人之追蹤管理**」）。

**[S73] PASS** — 衛生福利部。**醫用粒子(質子/重粒子)放射治療處置同意書及說明書（範本）**，
附**衛部醫字第 1101667467A 號公告**（醫事司頁面建檔日 110-11-09）。
頁面：`https://dep.mohw.gov.tw/DOMA/cp-3132-63940-106.html`
附件（docx）：`https://www.mohw.gov.tw/dl-72604-33f8a261-4749-4161-b74c-0db86f4f9ef3.html`（HTTP 200，45,155 bytes）
附件（公告 PDF）：`https://www.mohw.gov.tw/dl-72603-4051bd3d-18e2-4e6f-82cf-320f77c2d802.html`
（HTTP 200，437,402 bytes，**1 頁，pdftotext 無文字層＝掃描影像，內容無法擷取**）。
Route: WebFetch 取得附件連結 → `curl -sSL` 下載 docx → Python `zipfile` 解出 `word/document.xml`
→ 去標籤取全文。
本 brief 逐字引用：費用欄「各項費用：（單位：新臺幣元）／編序／項目名稱／**自費費用**」；
說明書「處置效益」四句（含「**僅有間接證據支持…直接證據(前瞻比較性臨床試驗)正在進行中**」與
「**較有共識是適用於治療局限性的腫瘤或傳統放射治療有效的其他臨床狀況**」）；
「已告知此處置非屬急迫性質…應經充分時間考慮後再決定施作與否」；「我瞭解這個治療無法保證一定能改善症狀」。
**該範本未列任何適應症清單，亦未提及膠質母細胞瘤。**

**[S74] PASS** — 衛生福利部醫事司。**《全國醫用粒子治療設備設置現況》（截至 113 年 11 月 30 日）**，
公告頁建檔／更新日 113-12-11。
頁面：`https://dep.mohw.gov.tw/DOMA/fp-3132-80794-106.html`
附件 PDF：`https://www.mohw.gov.tw/dl-92395-6100ce52-602d-4d9c-9483-c542ed59ed19.html`
（HTTP 200，83,433 bytes，1 頁）。
Route: WebFetch 取得附件連結 → `curl -sSL` → `pdftotext -layout`。
內容：**質子治療設備 13 家**（北部 5、中部 3、南部 5；**營運中 4 家、設置中 9 家**）；
**重粒子治療設備 3 家**（北部 1、中部 1、東部 1；**營運中 1 家、設置中 2 家**）。
**⚠ 該表逐家列出醫療機構全銜；依 SPEC 固定紅線「不點名機構」，正文只寫家數與地區分布。**

**[S75] PASS（沿用站上已查證項目，2026-09-03 重新確認）** — 本站既有文章
`sit-ttfields.html`〈貼片〉與 `nt-bnct.html`。
- 〈貼片〉的台灣端結論（原文查證日 2026-08-30）：「健保沒有這個項目…搜過『電場』『TTF』『Optune』，
  沒有任何一筆」「特管辦法附表二列的十二項特定醫療儀器裡，也沒有交流電場類的設備」
  「醫療器材許可證的狀態我沒有查到。查不到不是『沒有』，我也不會反過來寫成『有』」
  「沒有全國統一價，因為自費收費標準是各縣市主管機關逐家核定的；而它的成本形態是只要還在治療
  就持續發生的月費型支出」。
  **→ 本 brief 於 2026-09-03 以 [S71][S72] 獨立重新查證，結論一致，通過重新確認。**
- 〈BNCT〉的台灣端（原文查證日 2026-08 月）：清華大學 THOR 反應爐、恩慈途徑、
  2024-06-13 起生效的官方收費辦法（首次 120 萬元、後續每次 100 萬元）、2017 年起累計 629 人次、
  照射系統器材許可證 2023-06、**硼藥在台灣沒有藥證**、加速器型中心 2025-08 動工預計 2027 啟用。
  **→ 依 SPEC §一③，本專題沿用並一句指路，B5 不重寫金額；本 brief 未重新獨立查證該收費辦法頁面
  （清大網域 TLS 驗證失敗，見 FAIL-13）。**

### FAIL / NOT-CITABLE（保留，讓寫作者知道查過什麼）

**FAIL-1｜Walker 1979 的劑量反應具體數字。**
Route: `EPMC` `TITLE:"An analysis of dose-effect relationship in the radiotherapy of malignant gliomas"`
→ hitCount 1，**abstractText 空、無 PMCID、無 OA 全文**。
→ **書目可引 [S4]，數字不可引。** 需要「劑量有反應」時用 MRC BR2[S3] 與 EANO 的敘述句[S13]。

**FAIL-2｜NRG-BN001 的正式期刊論文。**
Route: `EPMC` `TITLE:"BN001"` → 只得一則 2020 年 SNO 會議摘要（認知次要終點，見 [S67]），
**無主要終點的正式論文**。
→ 主要終點只能引 ClinicalTrials.gov 張貼結果 [S7]，**正文必須寫明「這是試驗登記平台上張貼的結果，
還沒有正式論文」**。

**FAIL-3｜TTFields（Optune／NovoTTF）在台灣的醫療器材許可證。**
Route: 食藥署許可證查詢站 `https://info.fda.gov.tw/MLMS/H0001.aspx` → **連線遭代理伺服器拒絕
（CONNECT tunnel failed, 502 / connect_rejected）**；
`https://data.fda.gov.tw/opendata/exportDataList.do?method=openData&InfoId=36` →
**302 後導向 Swagger UI，未取得資料集**；WebSearch 未得官方許可證頁面。
→ **寫「我查不到可以引用的官方資料」，永不推論有無**（與站上〈貼片〉一致）。

**FAIL-4｜台灣癌症登記的腦瘤／GBM 發生數與存活趨勢。**
Route: 本次未取得可引用的官方原文（Brief A 亦標同一 gap）。
→ **B4 正文寫「我查不到台灣自己的膠質母細胞瘤存活統計」。**

**FAIL-5｜GBM 的放療療程中斷／總療程時間對存活的影響。**
Route: `EPMC` `TITLE:"interruption" AND TITLE:"radiotherapy" AND TITLE:"glioblastoma"` → **hitCount 0**；
`TITLE:"overall treatment time" AND TITLE:"glioblastoma"` → **hitCount 0**。
→ **B1 正文寫「膠質母細胞瘤自己沒有可以引用的資料」，且不可借用其他癌別的資料。**

**FAIL-6｜台灣病人實際完成六個維持療程的比例。** 無可引用資料。→ 不寫。

**FAIL-7｜MGMT 檢測在台灣的健保給付狀態。**
Route: 藥品給付規定不涵蓋檢驗；本次未取得可引用的檢驗給付條文。
（特管辦法附表四「抗癌瘤藥物之伴隨檢測」管的是 LDT 施行程序，**不是給付**[S72]，不可混用。）
→ **寫「檢測費用與給付請問個管師或醫務課」。**

**FAIL-8｜best case／worst case 情境法在膠質瘤的驗證。**
Route: `EPMC` `(TITLE:"scenarios for survival" OR TITLE:"best-case" OR TITLE:"worst-case") AND
ABSTRACT:"glioma"` → **hitCount 0**；`TITLE:"life expectancy" AND TITLE:"glioblastoma" AND
TITLE:"scenarios"` → **hitCount 0**。
→ **B4 可以介紹這個方法的形狀[S43][S44][S45]，但絕不可把 0.25/0.5/2/3 套到 GBM 的中位數上算月數。**

**FAIL-9｜CBTRUS 的 GBM 專屬五年存活率。**
Route: `EPMC-FT PMC11456825`（2017–2021 年版）→ **空回應**；2018–2022 年版無 PMCID。
摘要只有「所有惡性腦與 CNS 腫瘤」的 34.8%[S46]。
→ **不可把 34.8% 寫成 GBM 的數字。B4 用 Poon 2020 的 4%[S40] 取代。**

**FAIL-10｜質子用於 GBM 的第三期隨機試驗。**
Route: `EPMC` `TITLE:"dose-escalated" AND TITLE:"glioblastoma" AND TITLE:"proton"` → **hitCount 0**；
`TITLE:"proton beam therapy" AND TITLE:"glioblastoma"` → 10 筆，以個案報告、綜述、會議摘要為主，
**無第三期隨機試驗**。
→ **B5 寫「質子在膠質母細胞瘤沒有第三期隨機試驗」。**

**FAIL-11｜質子（醫用粒子治療）用於膠質母細胞瘤的中央主管機關適應症公告。**
Route: 醫事司「特定醫療技術及危險性醫療儀器」專區
（`https://dep.mohw.gov.tw/DOMA/lp-3132-106.html`）清單中與醫用粒子相關者僅三則：
設備設置現況[S74]、處置同意書及說明書範本[S73]、設備使用報告書；
**三者皆未列適應症清單，亦未提及膠質母細胞瘤**。特管辦法附表二只寫「依中央主管機關規定，
收受符合醫用粒子治療適應症之病人」，**未於本次查證中取得該「規定」本體**[S72]。
→ **B5 寫「我查不到載明膠質母細胞瘤可以用質子的官方文件」，永不推論。**

**FAIL-12｜paxalisib 在 GBM AGILE 的結果數字。** 見 [S78]。→ 不可推論方向。

**FAIL-13｜清華大學 BNCT 官方收費辦法頁面的獨立重新查證。**
Route: `curl` `https://www.nstdc.nthu.edu.tw/` → **SSL 憑證主體名稱不符（curl error 60），
本環境無法安全連線**（不得停用 TLS 驗證）。
→ **依 SPEC §一③沿用站上 `nt-bnct` 的既有查證並指路，B5 不重寫金額**[S75]。

**NOT-CITABLE-1｜Clark 2003 的內文。** [S50] 的 abstractText 為空，本 brief 未抓全文。
→ 只能引其存在與身分；**要引句子必須先抓 `EPMC-FT PMC2394262`**。

**NOT-CITABLE-2｜Hegi & Stupp 2015 的內文** [S19]、**Preusser & van den Bent 2023 的內文** [S60]。
兩者 fullTextXML 皆取不到。→ **只能引標題與其存在。**

**NOT-CITABLE-3｜NCCN。** 依 RESEARCH-COMMON 規定，全 brief **未查詢、未引用 NCCN**；
[S64] 摘要中提及某指引已移除 regorafenib 的那一句，**本 brief 不轉述，正文不得使用**。

---

## 附：全 brief 的族群標籤速查（寫作者自檢用）

| 來源 | 族群 | 年代／分類 | 設計 |
|---|---|---|---|
| [S1][S2][S17][S34] | 新診斷 GBM，**2000–2002 年收案、組織學診斷、無 IDH 檢測** | 舊分類 | 隨機第三期 |
| [S22] | 新診斷 GBM，18–70 歲，KPS ≥60 | 2013 | 隨機第三期 |
| [S23] | 新診斷 GBM，**僅 MGMT 甲基化**，18–70 歲，KPS ≥70 | 2019 | 隨機第三期，n=129 mITT |
| [S25] | **≥60 歲** GBM | 2004 | 隨機，n=100 |
| [S26] | **≥50 歲 KPS 50–70 或 ≥65 歲**（frail／elderly） | 2015 | 隨機，n=98 |
| [S27] | **≥60 歲** GBM | 2012 | 隨機三組 |
| [S28] | **>65 歲**，AA 或 GBM，KPS ≥60 | 2012 | 隨機非劣性 |
| [S29] | **≥65 歲** GBM，中位 73 歲 | 2017 | 隨機，n=562 |
| [S30] | **≥70 歲** GBM，KPS ≥70 | 2007 | 隨機，n=81 分析 |
| [S36][S37][S38] | 長期存活者，**舊分類、部分為 IDH-mutant** | 2007–2018 | 觀察性 |
| [S39][S42] | **分子確認 IDH-wildtype** | 2024／2026 | 觀察性 |
| [S40][S41] | 族群基礎（真實世界） | 2012／2020 | 系統回顧／SEER |
| [S43][S44][S45][S47][S48][S51] | **非膠質瘤**（乳癌、肺癌、混合晚期癌症） | — | 溝通與方法學研究 |
| [S49] | **惡性膠質瘤**（唯一一筆專屬溝通文獻） | 2014 | 系統回顧 |
| [S54] | 新診斷 GBM，**MGMT 未甲基化** | 2023 | 隨機第三期 |
| [S55] | 新診斷 GBM，**MGMT 甲基化或狀態不明** | 2022 | 隨機、單盲 |
| [S56][S57 部分][S63][S68][S69][S76] | **復發** GBM | — | 見各條設計 |
| [S59][S52] | 新診斷 GBM，**已完成同步化放療後才隨機**（中位 3.8 個月） | 2017／2019 | 隨機開放標籤／事後次族群 |
| [S62] | 新診斷 GBM，**EGFRvIII 陽性、中央確認** | 2017 | 隨機雙盲 |
| [S66] | 新診斷 GBM，**單一機構、n=29** | 2021 | 回溯、會議摘要 |

**寫作者最後一道檢查**：正文每一個數字後面，是否都能回答「這是哪一群人、哪一年、什麼設計」？
答不出來的，就是還沒有標籤，不能寫。
