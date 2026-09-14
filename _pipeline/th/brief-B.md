# B 組（低風險那一格：要不要那麼積極）查證 brief

範圍：B1 `th-active-surveillance`／B2 `th-lobectomy`／B3 `th-neck-dissection`／B4 `th-surgery-risks`
查證日：2026-09-14　　主要路徑：Europe PMC REST、PMC 全文、clinicaltrials.gov API v2、thyroid.org
本 brief 一律不觸碰台灣使用率／普及程度（依編輯裁決與紅線 4）。

---

## ⚠ 與 SPEC 假設不同形狀的事

### ⚠1（最重要，跨全專題）ATA 指引已改版：2025 版存在，且範圍與評等系統都變了
- SPEC §六 問「ATA 指引是否已有 2015 之後的新版（本 SPEC 暫以 2015 版為準，必須查證）」。**有。**
- 實際：**〈2025 American Thyroid Association Management Guidelines for Adult Patients with Differentiated Thyroid Cancer〉**, *Thyroid* 2025;35(8):841–985, PMID 40844370, DOI 10.1177/10507256251363120。ATA 官網 `https://www.thyroid.org/professionals/ata-professional-guidelines/` 逐字列出這一條，且不再把 2015 版列為現行 DTC 指引。
- **三件形狀上的改變**：
  1. **標題不再含「Thyroid Nodules」**。2025 版摘要自述：「The practice guidelines of the American Thyroid Association (ATA) for DTC management in adult patients (**previously combined with thyroid nodules**) were published initially in 1996…」→ **結節評估（A1／A2 那一格）已不在 ATA 2025 的範圍內**，A 組若寫「ATA 建議什麼大小扎針」必須引 2015 版並標明它是 2015 版，或改引 ETA 2023／K-TIRADS。
  2. **評等系統從「Strong/Weak + quality of evidence」改成 modified GRADE：`Strong recommendation` / `Conditional recommendation` + `High/Moderate/Low certainty evidence`，另有 `Good Practice Statement`（無等級）。** 2015 版的「Weak recommendation, Low-quality evidence」在 2025 版不存在。抄等級時不可混用兩套字串。
  3. 文獻檢索截止日 **2024-07-01**；另有勘誤 *Thyroid* 2025;35(11):1350（PMID 41182278）——內容只有作者單位、作者中間名、Table 8 列名改為「Follicular Carcinoma and IEFVPTC」，**不影響任何本組引用的建議條文**。
- **建議裁決**：SPEC §九 明訂「本專題以 ATA 2025 為現行版；凡引 2015 版一律加註『2015 版』並說明它已被取代」。B2、B3 的整段骨架要改寫。

### ⚠2 B2 的題目前提（「2015 ATA 鬆綁 1–4 公分」）已經是歷史，2025 版把切點移到 2 公分且語氣加強
- SPEC／任務書寫「2015 ATA change that allowed lobectomy for 1–4 cm low-risk tumours」。這對 2015 版是正確的（Rec 35B：「>1 cm and <4 cm」，`Strong recommendation, Moderate-quality evidence`，措辭是 *can be either* / *may be sufficient*）。
- 但 **2025 版 Rec 15 把這一格拆成兩段**：≤2 公分（cT1）cN0M0 **「should be a thyroid lobectomy」**，等級是 `Strong recommendation, Moderate certainty evidence`；>2–4 公分（cT2N0M0）才是 `Conditional recommendation, Low-moderate certainty evidence` 的「may be the preferred initial surgical treatment」。
- **這是語氣從「可以半切」變成「≤2 公分應該半切」**。B2 若照 SPEC 原樣寫「1–4 公分都是可以半切的灰帶」，會低估 ≤2 公分那一格的建議強度，也會高估 2–4 公分那一格的確定性。
- 建議裁決：B2 的主軸改成「**2 公分這條線**」，並明寫 2015→2025 的語氣變化。

### ⚠3 B3 的題目前提（「找找看有沒有隨機試驗，沒有就回報」）錯了——**隨機試驗存在，而且已有隨機試驗的統合分析**
- 任務書寫「whether any randomised trial exists (look for it — report if none)」。**不是沒有，是至少 5 個已發表 RCT 加 1 個 RCT 統合分析，外加 1 個正在進行的第三期多中心試驗。**
- 已發表 RCT：Viola 2015（JCEM, n=181）、Kim BY 2020（Eur Arch ORL, n=164）、Sippel 2020（Ann Surg, n=60）、Ahn 2022（Surgery, n=101）。
- RCT 統合分析：Sanabria 2022（Ann Surg 2022;276(1):66–73），**5 個 RCT、763 人**，結構性復發風險差 0%（95% CI −2% 到 2%），NNT = 500；永久副甲狀腺低下風險差 **+3%（95% CI 0%–6%）**。
- 進行中：**NCT03570021（ESTIMABL-CND，法國）**，`ACTIVE_NOT_RECRUITING`，實際收案 352 人（原設計 598 人），主要完成預估 2026-12。另有 NCT06899347（2–4 公分 PTC 的 pCND 隨機試驗，`NOT_YET_RECRUITING`，預估 392 人，估計 2026-04 開始）。
- 建議裁決：B3 必須寫成「**有隨機證據，而且隨機證據比觀察性統合分析更保守**」——觀察性統合分析（Chen 2018、Zhao 2017）看到復發下降，RCT 統合分析看不到。這是這一篇的真正支點。

### ⚠4 B2：**沒有任何有效力的「半切 vs 全切」隨機試驗**——唯一登記過的隨機嘗試只隨機了 2 個人
- ATA 2025 自述：「In view of the generally favorable outcomes of low-risk DTC and **lack of randomized controlled trials**, large database studies were deemed necessary…」
- 我另外查到 2026 年新出的〈Thyroid Lobectomy vs Total Thyroidectomy in Indeterminate Molecular Risk Thyroid Cancer: A Randomized Clinical Trial.〉*JAMA Otolaryngol Head Neck Surg* 2026, PMID 42623052。**但它對應的試驗 NCT06235814（MAPS pilot, UCLA）在 clinicaltrials.gov 上的紀錄是：主要終點＝「Rate of eligible patients who enroll」（可行性），實際收案數 `{'count': 2, 'type': 'ACTUAL'}`，狀態 COMPLETED（2026-01-30）。**
- → B2 可以寫、也**應該**寫：「這一格到今天為止沒有隨機試驗可以依靠；唯一一次試著做隨機的，隨機到的人數是個位數。」這比含混地說「證據等級不高」誠實得多。

### ⚠5 B2：「半切就不用吃藥」比想像中弱很多——這是本組最值得進 ⚠ 的臨床落差
- 常被複述的數字是 Verloop 2012 統合分析的 **22%**（半切後甲狀腺低下，95% CI 19–27；其中 subclinical 12%、clinical 4%——但 12/4 的拆分只來自 32 篇中的 4 篇）。
- 但那是「全部半切（含良性）」的甲狀腺低下率，**不是癌症病人為了把 TSH 壓進目標而吃藥的比例**：
  - Cox 2018（Surgery, n=555）：478 位術前沒吃藥的人中，**350 人（73%）一年內 TSH 升到 >2 mIU/L**。
  - Schumm 2021（Endocr Pract，低風險 DTC 半切）：115 人中 **97 人（84%）術後 TSH >2 mU/L**；其中 **66 人（68%）開始吃 LT4**（≈全體 57%）。
  - Hu 2024（Surgery，MarketScan 全美理賠，33,756 例半切）：**因惡性而半切者 59.3% 用了甲狀腺素**，良性 39.4%（aOR 2.34，95% CI 2.20–2.48）。
  - KTA 2025 指引本文亦寫：癌症病人半切後甲狀腺低下率「around 60%」，且「thyroid hormone therapy is required in **more than 73%** of patients to maintain target TSH levels (≤2 mIU/L)」。
- **ATA 2025 內文把 Verloop 的 22% 標成「biochemical hypothyroidism」、4% 標成「clinical or overt」——與 Verloop 原文（22% 是整體、12% 才是 subclinical）不一致。** 依鐵則回報為「指引自己轉述有誤」，不照抄；要用就引 Verloop 原文。
- 建議裁決：B2 必須寫「半切不等於不吃藥」，並且把「甲狀腺低下」與「為了 TSH 目標而吃藥」分成兩個不同的數字講。

### ⚠6 B1：「主動監測＝幾乎不會有事」對年輕人不成立，而且 Kuma 的終身進展機率有兩組互相打架的數字
- Kuma 依年齡分層（Ito 2014, n=1235，平均追蹤 75 個月）：10 年進展率 **<40 歲 22.5%／40–59 歲 4.9%／≥60 歲 2.5%**（此組數字由 JAES 2021 共識引述 Ito 2014）。
- **數字打架**：Miyauchi 2018（*Surgery* 2018;163(1):48–52）摘要原文給的終身（至 85 歲）進展機率是 **60.3%（20 多歲）／37.1%／27.3%／14.9%／9.9%／3.5%**；但 **JAES 2021 共識引用同一篇**時寫成 **48.6%／25.3%／20.9%／10.3%／8.2%／3.5%**。兩者不是同一組數。依鐵則回報「來源之間不一致」，**寫作組請引 Europe PMC 取得的原始摘要那一組（60.3%…），並且不要把任何一組寫成「日本的定論」**。
- 韓國 MAeSTro 前瞻世代（Lee 2022, n=706 可分析）：複合進展 5 年 **14.2%**（2 年 5.3%）。比日本高。
- 建議裁決：B1 不可以出現「幾乎不會長大」這種句子；必須帶年齡。

### ⚠7 B1：「拖到後來才開刀，結果一樣」比常被複述的版本弱——三份來源給出不同方向
- Kuma（Sasaki 2023, *Thyroid* 33(2):186–191，4635 人）：轉換手術組（CS, n=242）與立即手術組（IS, n=1739）之間，**不良事件發生率沒有差**；CS 組無人永久聲帶麻痺。
- 但 **KTA 2025 指引自己做的 6 篇統合**：延遲手術的**暫時性**副甲狀腺低下較高（OR 1.705, 95% CI 1.188–2.448）、**暫時性**聲帶麻痺較高（OR 1.519, 95% CI 1.038–2.222）；**永久性**副甲狀腺低下（OR 1.304, 0.583–2.915）與永久性聲帶麻痺（OR 0.842, 0.198–3.799）**沒有差**。另 MAeSTro：延遲手術組中央／側頸廓清比例較高（95% vs 89%, p=0.02）。
- **Nguyen 2025**（Eur Arch ORL, 21 篇 9,397 人統合）結論更保守：「**Overall complication and recurrence rates were higher in the delayed surgery group than in the IS group.**」
- 建議裁決：B1 只能寫到「**永久性併發症沒有增加；暫時性併發症與手術範圍可能增加；有一篇統合分析連復發率都看到較高**」。不可以寫「晚開刀完全沒有代價」。

### ⚠8 B1：主動監測的「退出」主要不是因為腫瘤變化，而是病人（與醫師）改變主意——這件事指引自己寫明了
- ATA 2025 原文：「Rates of later surgery varied and were **driven more by patient choice than signs of progression**.」
- Kuma（Sasaki 2021, n=2288）：162 人（7.1%）在開始監測 12 個月後轉手術，原因為疾病進展 57 人、病人意願 43 人、**醫師意願 31 人**、其他甲狀腺／副甲狀腺疾病 24 人、其他 7 人。
- 韓國（Oh 2018, n=370）：58 人（15.7%）延遲手術，原因為**焦慮 37.9%**、腫瘤變大 32.8%、出現淋巴結轉移 8.6%。
- 建議裁決：這正是紅線 3 要的材料——主動監測不是「先觀察看看」，它有明文的退出條件，而現實中最大宗的退出原因是心理與醫病關係，不是腫瘤。要寫進去，且不可寫成「病人自己撐不住就是失敗」。

### ⚠9 B1：主動監測期間**不驗甲狀腺球蛋白（Tg）**——這與讀者（與 D2 那篇）的直覺相反
- ATA 2025 **RECOMMENDATION 13**：「For patients undergoing active surveillance, routine measurement of serum Tg and/or TgAb levels is not recommended.（Good Practice Statement）」
- 理由：甲狀腺完整時 Tg 沒有判讀基準。這一條同時支援共同規範第 7 條（Tg 數字必須標手術範圍）。
- 建議裁決：B1 要有一句「監測看的是超音波，不是抽血驗 Tg」，並指路 D2。

### ⚠10 B1：主動監測的納入上限，**在 ATA 2025 仍然是 cT1a（≤1 公分）**，>1 公分只有零星資料
- ATA 2025 **RECOMMENDATION 11A** 只寫 cT1aN0M0。內文明言「There are limited data on the role of active surveillance in cancers >1 cm」。
- >1 公分的資料就只有：Sakai 2019（T1bN0M0，**只有 61 人選監測**，平均 7.4 年）、Ho 2022（≤2 公分 Bethesda V/VI，監測組 112 人，平均 37.1 個月）、Tuttle 2017（納入條件是 **intrathyroidal ≤1.5 cm**，291 人，中位 25 個月）。
- 建議裁決：B1 不可以寫「1.5 公分、2 公分也可以看著」。要寫「目前站得住的是 1 公分以內；再大一點的只有少數中心、少數人、短追蹤的資料」。

### ⚠11 B1：**主動監測在 ATA／ESMO／NCCN 以外「有」其他指引明文納入**（SPEC §六 的待確認）——而且是三份，其中兩份是專門寫主動監測的
- 〈2025 Korean Thyroid Association Clinical Management Guideline on Active Surveillance for Low-Risk Papillary Thyroid Carcinoma〉*Endocrinol Metab (Seoul)* 2025;40(3):307–341（OA，全文可讀）——**整本專門寫主動監測**，含納入定義、追蹤間隔、退出條件、Recommendation level 1/2/3。
- 〈Standardized Ultrasound Evaluation for Active Surveillance of Low-Risk Thyroid Microcarcinoma in Adults: 2024 Korean Society of Thyroid Radiology Consensus Statement〉*Korean J Radiol* 2024;25(11):942–958（OA）——**專門寫超音波怎麼做**。
- 〈Indications and Strategy for Active Surveillance of Adult Low-Risk Papillary Thyroid Microcarcinoma: Consensus Statements from the Japan Association of Endocrine Surgery Task Force…〉*Thyroid* 2021;31(2):183–192（OA）——日本內分泌外科學會；文中自述「**Grading of evidence was not considered suitable for the present consensus statements**」（即這份沒有證據等級，引用時必須說明）。
- ESMO：現行實體癌指引是 2019 年（*Ann Oncol* 30(12):1856–1883），2022 年只更新了晚期全身性治療那一段。**我沒有取得 ESMO 全文或摘要中關於主動監測的段落 → 標 FAIL，寫作組不得引用 ESMO 對主動監測的立場。**

### ⚠12 B1／A 組交界：韓國兩份指引允許**不扎針**就進主動監測，這會改變 A1／A2 的「先扎針才知道」框架
- KSThR 2024 建議 1-3：「…**AS can also be considered for highly suspicious (K-TIRADS 5) thyroid nodules on US without biopsy**, taking patient preference into account.」
- KTA 2025 亦寫：小於 1 公分、無不良預後特徵的高度懷疑結節，可以「monitoring with neck US rather than immediate pathologic examination」。
- ATA 2015 本來就不建議對 ≤1 公分結節常規扎針。
- 建議裁決：這是 A 組的事，但 B1 若寫「先有細針報告才談監測」會與國際指引不一致；請 §九 統一裁決 A2 與 B1 的接口。

### ⚠13 B4：**「併發症率」根本沒有單一分母——分母取決於「怎麼查」與「怎麼定義」**，這件事本身就是 B4 的主軸
- 喉返神經：Jeannon 2009（27 篇、25,000 人）——平均暫時性 9.8%、永久性 2.3%；**但依喉部檢查方式不同，報告率從 2.3% 一路到 26%**。Bergenfelz 2008（斯堪地那維亞 3,660 例）亦顯示「**routine laryngoscopy**」本身就是單側麻痺的獨立關聯因子（OR 1.92, p=0.0002）。
- 副甲狀腺低下：Koimtzis 2021（45 篇、23,164 人）——文獻報告率 **0.5% 到 65%**，主因是定義與「暫時／永久」的時間切點（6 個月 vs 12 個月）不同；以 6 個月切點的永久性為 4.11%，12 個月為 4.08%（p=0.92）。
- ATA 2025 自己的區間：**暫時性副甲狀腺低下 14–43%，永久性 1–25%。**
- 建議裁決：B4 的第一段就要寫「你在網路上看到的那個數字，取決於那家醫院有沒有每個人都照喉鏡、以及他們把幾個月算成永久」。這比給一個數字有用。

### ⚠14 B4：被廣泛引用的 Hsiao 2022 統合分析**有已發表的資料勘誤**
- 〈Complication Rates of Total Thyroidectomy vs Hemithyroidectomy for Treatment of Papillary Thyroid Microcarcinoma: A Systematic Review and Meta-analysis〉*JAMA Otolaryngol Head Neck Surg* 2022;148(6):531–539。
- 勘誤：〈Errors in Data Reported in Meta-analysis…〉*JAMA Otolaryngol Head Neck Surg* 2023;149(2):189，PMID 36547950。勘誤原文：「the authors reported several errors for the studies included in the meta-analysis… which affect the text, Table, Figures, and Supplement, and indicate that **none of the direction of the statistical findings, interpretations, or conclusions are affected**. The article has been corrected.」
- **KTA 2025 指引引用的 0.9%／1.8%／0.2% 就是出自這一篇。** 可用，但引用時必須知道有勘誤、且我無法確認 Europe PMC 上的摘要是勘誤前還是勘誤後版本 → 本 brief 把 Hsiao 的數字標為 **PASS（附勘誤警告）**，建議 B4 的頭條數字改用登錄資料（Bergenfelz 2008、Aspinall 2019）與 ATA 2025 的區間，Hsiao 只作為「半切 vs 全切相對差距」的佐證。

### ⚠15 B4：永久性副甲狀腺低下不是「補鈣就沒事」——但可引的死亡率／腎功能資料來自**良性疾病**世代，不可外推到癌症
- Almquist 2018（BJS，瑞典 SQRTPA，4,899 人，**全部是良性甲狀腺疾病的全切**）：永久性副甲狀腺低下 246 人（5.2%），校正後死亡 HR **2.09（95% CI 1.04–4.20）**。
- Bergenfelz 2020（Surgery，同一登錄，4,828 人，**良性**）：腎功能不全 HR 4.88（2.00–11.95）；本來就有心血管疾病者，心血管事件 HR 1.88（1.02–3.47）。
- **這兩篇的世代是良性疾病、且以「使用活性維生素 D 超過 6 個月」定義永久性低下。** 依四條分界線，不得寫成「甲狀腺癌開完刀副甲狀腺壞掉會早死」。
- 建議裁決：B4 可以寫「副甲狀腺永久受損在登錄資料裡與長期腎臟與心血管風險有關（該資料來自良性疾病手術）」，必須帶括號。

### ⚠16 B4：手術量門檻**不是一個數字**
- ATA 2025 **RECOMMENDATION 6** 原文寫 **「>25–50 thyroidectomies/year」**，`Strong recommendation, Moderate certainty evidence`。
- Adam 2017（Ann Surg，HCUP-NIS 16,954 例全切）：門檻 **>25 例/年**；1 例/年者併發症勝算增加 87%、2–5 例 68%、6–10 例 42%、11–15 例 22%、16–20 例 10%、21–25 例 3%。
- Aspinall 2019（UKRETS，10,313 例雙側手術／25,038 例甲狀腺切除）：**要到 >50 例/年才開始下降**，最高量組（>100 例/年）永久副甲狀腺低下 3%、喉返神經麻痺 2.6%；作者自承「limited by a high proportion of missing data」。
- 建議裁決：B4 引量效關係時必須同時說「不同資料庫算出來的門檻不一樣（25 到 50 到 100）」，並且**絕對不可以**把它轉成任何台灣的敘述（紅線 4、紅線 7）。

### ⚠17 B3：2025 版把「不做預防性中央區廓清」的措辭**加強**了
- 2015 Rec 36C：「Thyroidectomy **without** prophylactic central neck dissection **is appropriate** for small (T1 or T2), noninvasive, clinically node-negative PTC (cN0) and for most follicular cancers.（Strong recommendation, Moderate-quality evidence）」
- 2025 Rec 19A：「Prophylactic central-compartment lymph node dissection **should not be performed** for most small, noninvasive, clinically node-negative PTC (cT1-T2, cN0) and for most FTCs.（Strong recommendation, Moderate certainty evidence）」
- 另：2015 Rec 36B 把 **cN1b（側頸有轉移）** 列為可考慮預防性中央區廓清的情境之一；**2025 Rec 19B 把 cN1b 拿掉了**，只剩 T3/T4 與「for whom the information will be used to plan further steps in therapy」。
- 建議裁決：B3 要把這兩處措辭變化寫出來——「從『不做也可以』變成『不應該做』」。

### ⚠18 B4（給寫作組的紀律提醒）：術後補鈣不可以給讀者一組數字
- ATA 2018 聲明給的是臨床閾值（術後 iPTH **<15 pg/mL** 提示急性副甲狀腺低下風險升高），ATA 2025 Rec 24B 只說「parathyroid hormone-directed calcium and vitamin D supplementation (regular or selective) should be provided」，沒有給劑量。
- 建議裁決：比照紅線 6 的精神，B4 寫「為什麼要一直抽血驗鈣、在管什麼」，**不給鈣片與活性維生素 D 的劑量或天數**，寫成「依你手術醫院的術後補鈣流程」。

---

## 來源清單

> PASS＝我實際取得並讀到內容（摘要或全文）。FAIL＝只在別的文件裡看到被引用、或取不到內容。
> 每個數字後括號內為四條分界線＋三個必帶標籤（組織型／風險組或期別／年齡切點與 AJCC 版本／終點／腫瘤大小／手術範圍／有無放射碘）。

### 指引與共識

**[B-G1]** 2025 American Thyroid Association Management Guidelines for Adult Patients with Differentiated Thyroid Cancer. *Thyroid* 2025;35(8):841-985. PMID 40844370; DOI 10.1177/10507256251363120
  狀態：**PASS**
  查證路徑：Europe PMC `search?query=EXT_ID:40844370&resultType=core` 取得書目；Europe PMC `PMC13090833/fullTextXML` 回 404，改抓 `https://pmc.ncbi.nlm.nih.gov/articles/PMC13090833/`（HTTP 200，2.4 MB），轉純文字 983,598 字元，內含全部 84 條 RECOMMENDATION 與 1,458 筆參考文獻。另於 `https://www.thyroid.org/professionals/ata-professional-guidelines/` 逐字看到「2025 American Thyroid Association Management Guidelines for Adult Patients with Differentiated Thyroid Cancer / Matthew D. Ringel, Julie Ann Sosa, et al., Thyroid.Aug 2025. 841-985.」
  可用的逐字條文：
  - **RECOMMENDATION 6**（外科量效）：「Due to lower complication rates and improved outcomes on average associated with high volume thyroid surgeons (>25–50 thyroidectomies/year), patients with thyroid cancer should be offered referral to a high-volume surgeon, particularly for tumors requiring more extensive surgery.」`(Strong recommendation, Moderate certainty evidence)`
  - **RECOMMENDATION 11 A**：「Active surveillance may be offered as an appropriate management option for some patients with **cT1aN0M0 PTCs**. Shared clinical decision-making between the patient and clinical team regarding risks and benefits of this approach is essential.」`(Conditional recommendation, Low certainty evidence)`
  - **RECOMMENDATION 11 B**：「Ultrasound-guided percutaneous ablation may be considered as an alternative to active surveillance or resection for cT1aN0M0 PTC in selected patients…」`(Conditional recommendation, Low certainty evidence)`
  - **RECOMMENDATION 12**：「For patients undergoing active surveillance, neck ultrasound should be used to monitor disease progression.」`(Good Practice Statement)` 內文：「neck ultrasound should be performed **every 6 months for 1–2 years and then annually**. The length of necessary follow-up remains unknown. **None of the prior studies on active surveillance used neck CT for routine follow-up.**」
  - **RECOMMENDATION 13**：「For patients undergoing active surveillance, routine measurement of serum Tg and/or TgAb levels is not recommended.」`(Good Practice Statement)`
  - **RECOMMENDATION 14**：「In patients undergoing active surveillance, surgical resection is indicated if there is evidence of new biopsy-proven lymph node metastases, **growth of the primary tumor by ≥3 mm**, distant metastases, evidence of extrathyroidal extension, **posterior growth**, when there is **patient anxiety**, **inability to follow-up**, and/or expressed preference for surgery.」`(Good Practice Statement)`
  - **RECOMMENDATION 15 A**：「When resection is performed for patients with thyroid cancer **≤2 cm** without gross extra-thyroidal extension (cT1) and without metastases (cN0M0), the initial surgical procedure **should be a thyroid lobectomy** unless there are bilateral cancers or other indications to remove the contralateral lobe.」`(Strong recommendation, Moderate certainty evidence)`
  - **RECOMMENDATION 15 B**：「For patients with low risk, unilateral thyroid cancer **>2 and ≤4 cm (cT2N0M0)**, thyroid lobectomy may be the preferred initial surgical treatment due to significantly lower risk and side effects. However, the patient and treatment team may adopt total thyroidectomy to enable RAI administration and/or enhance follow-up… When thyroid lobectomy is offered as initial treatment, counsel the patient about the possibility of conversion to total thyroidectomy or need for subsequent completion thyroidectomy if higher-risk factors emerge intraoperatively or postoperatively.」`(Conditional recommendation, Low-moderate certainty evidence)`
  - **RECOMMENDATION 15 C**：「For patients with thyroid cancer >4 cm (cT3a), cancer of any size with gross extra-thyroidal extension (cT3b or cT4), or clinically apparent metastatic disease to lymph nodes (cN1) or distant sites (cM1), the initial surgical procedure should include a total thyroidectomy…」`(Strong recommendation, Moderate certainty evidence)`
  - **RECOMMENDATION 16 A**（補全切）：「Completion thyroidectomy for cancer following initial lobectomy may be considered to address persistent primary malignancy, facilitate RAI administration, and/or enhance follow-up based upon higher estimated risk of recurrence identified postoperatively, accounting for recurrent laryngeal nerve function.」`(Conditional recommendation, Low-moderate certainty evidence)`
  - **RECOMMENDATION 19 A**：「Prophylactic central-compartment lymph node dissection **should not be performed** for most small, noninvasive, clinically node-negative PTC (cT1-T2, cN0) and for most FTCs.」`(Strong recommendation, Moderate certainty evidence)`
  - **RECOMMENDATION 19 B**：「Prophylactic central-compartment neck dissection may be considered in patients with PTC and clinically uninvolved lymph nodes (cN0) who have advanced primary tumors (T3 or T4) or for whom the information will be used to plan further steps in therapy, but this approach should be weighed against the risks as they evolve during thyroidectomy.」`(Conditional recommendation, Low certainty evidence)`
  - **RECOMMENDATION 20 A**（治療性）：「Therapeutic central-compartment (Level VI and upper Level VII) neck dissection for patients with clinically involved central nodes (cN1a) should accompany thyroidectomy to clear disease from the central neck.」`(Strong recommendation, Moderate certainty evidence)`
  - **RECOMMENDATION 20 B**：「Therapeutic CLND with dissection of the ipsilateral central compartment lymph nodes is recommended to accompany lateral-compartment neck dissection and thyroidectomy for patients with clinically involved lateral neck lymph nodes (cN1b).」`(Conditional recommendation, Low certainty evidence)`
  - **RECOMMENDATION 22 A**（術前聲音）：「All patients undergoing thyroid surgery should undergo voice assessment as part of their preoperative physical examination…」`(Strong recommendation, Moderate certainty evidence)`
  - **RECOMMENDATION 23 A/B**：「Visual identification of the recurrent laryngeal nerve(s) (RLN) should be performed during thyroidectomy and/or para-tracheal node dissection…」`(Good Practice Statement)`；「Intraoperative neurophysiological monitoring of the RLN **may be performed**…particularly during total or re-operative thyroidectomy.」`(Conditional recommendation, Low-moderate certainty evidence)`
  - **RECOMMENDATION 24 A/B**（副甲狀腺）：「The parathyroid glands and their blood supply should be preserved during thyroid surgery… auto-transplanted into nearby muscle after frozen section (of a portion) confirms benign parathyroid tissue.」`(Good Practice Statement)`；「After total thyroidectomy and/or central lymph node dissection, or after unilateral operations that follow prior contralateral thyroid resections, parathyroid hormone-directed calcium and vitamin D supplementation (regular or selective) should be provided to reduce rates of hypocalcemia and shorten hospital stays compared with observation with serial calcium measurement alone.」`(Strong recommendation, Moderate certainty evidence)`
  - **RECOMMENDATION 46 A**（TSH，供 B2 交界用）：「Long-term TSH suppression is not suggested for patients with low- or intermediate-risk disease who have no evidence of biochemical or structural recurrence.」`(Conditional recommendation, Low certainty evidence)`
  可用的數字（來自本指引內文）：
  - 高量外科醫師（≥30 例/年）癌症全切併發症率 **7.5% vs 中量 13.4% vs 低量 18.9%（p<0.001）**（分化型；終點＝住院併發症；手術範圍＝全切；HCUP-NIS）
  - 高量醫師：半切 **7.6%** vs 全切 **14.5%**；低量醫師：半切 **11.8%** vs 全切 **24.1%**（同上）
  - 全切 vs 半切相對風險：喉返神經傷害暫時 RR 1.7／永久 RR 1.9；低血鈣暫時 RR 10.7／永久 RR 3.2；出血血腫 RR 2.6（引自 Kandil 2013，見 [B-S22]）
  - 半切後補全切的估計比例：**5%–43%**（回溯研究區間）、統合分析 **11%–34%**；另兩篇研究：術中因高風險發現轉全切 **21%**、依最終病理補全切 **27%–30%**（分化型；cT1-2N0M0 低風險；終點＝再手術）
  - ATA 2015 上路前後：全切佔比 61%→31%，補全切 74%→20%（另一組 50%→25%）；但全切**仍是**最常做的起始手術（**70%–88%**，即使是 cT1-2N0M0）
  - 「patients must be aware of a **≥20% possibility** of conversion to total thyroidectomy intraoperatively, or subsequent completion thyroidectomy」
  - 長期併發症段落：無神經傷害者長期聲音改變 **>30%**；副甲狀腺低下 **暫時 14–43%、永久 1–25%**
  - pCND 觀察性統合（Chen 2018）：pCND 組局部區域復發 **280/11,098（2.52%）** vs 非 pCND **254/5,583（4.59%）**；OR 0.65（0.48–0.88）；暫時性喉返神經傷害 OR 2.03（1.32–3.13）、暫時性低血鈣 OR 2.23（1.84–2.70）、**永久性低血鈣 OR 2.22（1.58–3.13）**

**[B-G2]** 2015 American Thyroid Association Management Guidelines for Adult Patients with Thyroid Nodules and Differentiated Thyroid Cancer: The American Thyroid Association Guidelines Task Force on Thyroid Nodules and Differentiated Thyroid Cancer. *Thyroid* 2016;26(1):1-133. PMID 26462967; DOI 10.1089/thy.2015.0020
  狀態：**PASS（但為已被取代的版本，引用時必須標明）**
  查證路徑：`https://pmc.ncbi.nlm.nih.gov/articles/PMC4739132/`（HTTP 200，2.07 MB），轉文字 846,207 字元。
  可用的逐字條文：
  - **RECOMMENDATION 12** 內文：「an active surveillance management approach **can be considered** as an alternative to immediate surgery in (A) patients with very low risk tumors (e.g., papillary microcarcinomas without clinically evident metastases or local invasion, and no convincing cytologic evidence of aggressive disease), (B) patients at high surgical risk because of comorbid conditions, (C) patients expected to have a relatively short remaining life span…, or (D) patients with concurrent medical or surgical issues that need to be addressed prior to thyroid surgery.」
  - **RECOMMENDATION 35 B**：「For patients with thyroid cancer >1 cm and <4 cm without extrathyroidal extension, and without clinical evidence of any lymph node metastases (cN0), the initial surgical procedure can be either a bilateral procedure (near-total or total thyroidectomy) or a unilateral procedure (lobectomy). Thyroid lobectomy alone **may be sufficient** initial treatment for low-risk papillary and follicular carcinomas…」`(Strong recommendation, Moderate-quality evidence)`
  - **RECOMMENDATION 35 C**：「If surgery is chosen for patients with thyroid cancer <1 cm without extrathyroidal extension and cN0, the initial surgical procedure should be a thyroid lobectomy…」`(Strong recommendation, Moderate-quality evidence)`
  - **RECOMMENDATION 36 B**：「Prophylactic central-compartment neck dissection (ipsilateral or bilateral) **should be considered** in patients with papillary thyroid carcinoma with clinically uninvolved central neck lymph nodes (cN0) who have advanced primary tumors (T3 or T4) **or clinically involved lateral neck nodes (cN1b)**, or if the information will be used to plan further steps in therapy.」`(Weak recommendation, Low-quality evidence)`
  - **RECOMMENDATION 36 C**：「Thyroidectomy without prophylactic central neck dissection **is appropriate** for small (T1 or T2), noninvasive, clinically node-negative PTC (cN0) and for most follicular cancers.」`(Strong recommendation, Moderate-quality evidence)`
  - 2015 版對 PTMC 術後的數字：「disease-specific mortality rates have been reported to be **<1%**, loco-regional recurrence rates are **2%–6%**, and distant recurrence rates are **1%–2%**」（乳突微小癌 ≤1 cm；手術後；終點分別為疾病特異性死亡與結構性復發；未標 RAI 狀態）

**[B-G3]** Indications and Strategy for Active Surveillance of Adult Low-Risk Papillary Thyroid Microcarcinoma: Consensus Statements from the Japan Association of Endocrine Surgery Task Force on Management for Papillary Thyroid Microcarcinoma. *Thyroid* 2021;31(2):183-192. PMID 33023426; PMC7891203; DOI 10.1089/thy.2020.0330
  狀態：**PASS**（全文 OA）
  查證路徑：`europepmc.../PMC7891203/fullTextXML`（HTTP 200，135,323 bytes）。
  重要自述：「…identified **no randomized studies** comparing outcomes between immediate surgery and AS. …**Grading of evidence was not considered suitable** for the present consensus statements.」（→ 這份沒有等級，不可假裝有）
  **Table 2. Indication for Immediate Surgery in Papillary Thyroid Microcarcinoma Without Active Surveillance（逐字，7 條）**
  1. Presence of clinical lymph node metastasis or distant metastasis (rare)
  2. Clinically apparent invasion into the RLN or trachea
  3. Diagnosis of aggressive subtype of papillary thyroid carcinoma on cytology (rare)
  4. Tumors adherent to the trachea, possibly invading
  5. Tumors located along the course of the RLN
  6. Associated with other thyroid or parathyroid disease requiring surgery
  7. Age <20 years (no current evidence)
  **Table 3. Indications for Surgery After Active Surveillance for PTMC（逐字，4 條）**
  1. Tumor diameter reaches 13 mm
  2. Appearance of new lymph node metastasis
  3. Change in patient preference
  4. Appearance of other thyroid disease or parathyroid disease requiring surgery
  其他可用內容：
  - 團隊要求：「**A multidisciplinary team including US specialists highly experienced in imaging of the neck region is mandatory** for conducting AS…」；2018 年 JAES 結節指引要求 AS 應由「an appropriate medical care team」執行。
  - 影像頻率（Key point 逐字）：「US evaluations of PTMCs by experienced examiners are recommended **every 6 months for 1–2 years** after initiation of AS and **once a year thereafter** if no disease progression is detected.」
  - 增大的定義：「**increase in maximal diameter by ≥3 mm**」（Ito 2007 起）；並明確反對用體積 >50% 作為主要判準（理由：6×6×6→7×7×7 mm 的體積成長率就是 59%，且超音波體積外推有觀察者變異）
  - 氣管／喉返神經的判準（Kuma 的原始觀察）：腫瘤與氣管呈**鈍角**者侵犯風險高；腫瘤與喉返神經路徑之間**沒有正常甲狀腺組織薄緣**者有風險。「**No PTMCs <7 mm showed invasion into the trachea or RLN during surgery.**」；≥7 mm 且與氣管呈鈍角者，**51 例中 12 例（24%）** 需刮除軟骨或全層切除氣管；≥7 mm 且無正常薄緣者，**98 例中 9 例（9%）** 需刮除／部分切除／切除重建喉返神經。
  - 不構成排除條件者（逐條有 Key point）：多發、家族史、有生育計畫／懷孕、鈣化程度、血流豐富程度、合併 Graves 病或良性結節。
  - 年齡（引 Ito 2014）：10 年進展率 **≥60 歲 2.5%／40–59 歲 4.9%／<40 歲 22.5%**；多變項分析年輕（≤40 歲）為獨立危險因子 OR 4.348（95% CI 2.293–8.196, p<0.0001）（乳突微小癌 T1aN0M0；終點＝「進展」＝腫瘤達 ≥12 mm 或新出現淋巴結轉移；未手術、未做 RAI）
  - **本文引用 Miyauchi 2018 終身進展機率為 48.6%／25.3%／20.9%／10.3%／8.2%／3.5%，與原著摘要不符（見 ⚠6）。**
  - 持續多久：「**AS throughout life is therefore recommended.**」「There is no evidence regarding after how many years AS can be discontinued.」

**[B-G4]** Standardized Ultrasound Evaluation for Active Surveillance of Low-Risk Thyroid Microcarcinoma in Adults: 2024 Korean Society of Thyroid Radiology Consensus Statement. *Korean J Radiol* 2024;25(11):942-958. PMID 39473087; PMC11524690; DOI 10.3348/kjr.2024.0871
  狀態：**PASS**（全文 OA；另有勘誤 *Korean J Radiol* 2024;25(12):1104, PMID 39608376，與本 brief 引用內容無關）
  查證路徑：`europepmc.../PMC11524690/fullTextXML`（HTTP 200，201,631 bytes）。
  可用的逐字建議：
  - **2-1**：「Prior to the initiation of AS for thyroid cancer, **high-quality US of the thyroid and neck should be performed by experts in thyroid and neck US imaging**」
  - **1-3**：「AS is primarily considered for Bethesda V or VI thyroid nodules on FNA or CNB, without suspicious imaging features of gross ETE (particularly the trachea and RLN), LNM, and distant metastasis. However, taking patient preference into account, **AS can also be considered for highly suspicious (K-TIRADS 5) thyroid nodules on US without biopsy**」
  - **4-1**：「We recommend using consistent measurement methods throughout the initial and follow-up examinations during AS」（採 ACR TI-RADS 三軸測量；體積＝橫徑×前後徑×上下徑×0.524）
  - **6**：「US evaluations of changes in tumor size and the appearance of novel potential gross ETE and LNM are recommended **every 6 months for the first 1–2 years** after the initiation of AS and **once a year thereafter** if no tumor progression is detected」
  - 增大定義：「an increase of **≥3 mm in one dimension or ≥2 mm in two dimensions**」；並且「We recommend surgery when this criterion is met **at least twice on consecutive observations within at least 6 months**, considering the inter- and intra-observer variability in measuring tumor size using US.」
  - 氣管：「we recommend that **paratracheal tumors with right- or wide-angle abutments are inappropriate** for initiating or pursuing AS」
  - **三分類（承 Brito 2016）逐字**：
    - Ideal：「probable or proven **solitary** PTMC that is **not adjacent to the thyroid capsule** and is **confined to the thyroid parenchyma**」
    - Appropriate：「specific characteristics that render observations **more technically difficult to follow-up** (e.g., ill-defined nodule margin, US-diffuse thyroid disease) or have a subcapsular tumor without definite evidence of gross ETE… **when followed by an experienced management team**」
    - Inappropriate：「an observational approach is **contraindicated**… locoregional or distant metastasis or potential gross ETE… identified at the initial presentation, [or] when the tumor presents with new features of potential gross ETE to the trachea or RLN, or locoregional or distant metastasis during US surveillance」
  - 「The US-based appropriateness category… **should be determined by the operator performing the real-time US scan and should be included in the US report.**」

**[B-G5]** 2025 Korean Thyroid Association Clinical Management Guideline on Active Surveillance for Low-Risk Papillary Thyroid Carcinoma. *Endocrinol Metab (Seoul)* 2025;40(3):307-341. PMID 40598902; PMC12230268; DOI 10.3803/enm.2025.2461
  狀態：**PASS**（全文 OA）
  查證路徑：`europepmc.../PMC12230268/fullTextXML`（HTTP 200，378,159 bytes）。
  等級定義（Table 1 逐字）：Level 1「Strongly recommend for/against」；Level 2「Conditionally recommend for/against」；Level 3「Expert consensus recommendation」；Level 4「Inconclusive」。
  可用的逐字建議：
  - **1.2.B**：「Adult patients (**aged ≥19 years**) diagnosed with low-risk PTMC may be considered for AS.」[Level 2]；臨床考量：「For patients under the age of 19 with PTMC, **surgery is recommended** regardless of whether the tumor is classified as low-risk.」
  - **2.1.A（納入定義，逐字四條）**：「Thyroid nodules ≤1 cm diagnosed as Bethesda category V… or VI… provided all the following criteria: (1) No clinical evidence of LN metastasis or distant metastasis (2) No evident imaging features of gross ETE into strap muscles, trachea, or RLN (3) No suspicious imaging features suggestive of tracheal or RLN invasion (4) Absence of aggressive histologic subtypes of papillary thyroid carcinoma (e.g., **tall cell, columnar cell, hobnail, solid, or diffuse sclerosing** subtypes)」[Level 1]
  - **2.2.B**：「High-quality US examinations of the thyroid and neck **should be conducted by physicians experienced** in thyroid and neck US imaging.」[Level 1]
  - **2.2.E**：「Routine chest CT for evaluating lung metastasis in PTMC patients is **not** recommended.」[Level 3]
  - **4.1.A**：「To evaluate disease progression, US should be performed **every 6 months for the first 1–2 years** following diagnosis. If no progression is observed, **annual US** is recommended thereafter.」[Level 1]
  - **5.1.A 進展定義**：「(1) Tumor enlargement: An increase in maximal tumor diameter of **≥3 mm** or an increase of **≥2 mm in at least two dimensions**. [Level 3] (2) Newly detected clinical evidence of ETE, LN metastasis, or distant metastasis. [Level 1]」
  - **5.2.A 退出條件**：「(1) The tumor's maximal diameter reaches **≥13 mm**, or at least two dimensions measure ≥12 mm. [Level 3] (2) A new US finding… inappropriate for AS… [Level 1] (3) New LN or distant metastasis is confirmed or suspected. [Level 1] (4) **The patient elects to undergo surgery.** [Level 1]」
  - **3.3.A**：「delayed surgery following AS **may be associated with a higher risk of temporary surgical complications** compared to immediate surgery; however, delayed surgery **does not increase the risk of permanent complications or disease recurrence**.」[Level 2]
  可用的數字：
  - 委員會自行統合（6 篇）：延遲手術 vs 立即手術——暫時性副甲狀腺低下 **OR 1.705（95% CI 1.188–2.448）**；暫時性聲帶麻痺 **OR 1.519（1.038–2.222）**；永久性副甲狀腺低下 OR 1.304（0.583–2.915）；永久性聲帶麻痺 OR 0.842（0.198–3.799）（乳突微小癌 T1aN0M0；終點＝手術併發症；手術範圍混合）
  - 委員會自行統合（6 篇）：復發 **OR 0.749（0.424–1.321）**（無差）
  - 自然史（引 Yoon 2024 統合，≤2 cm 低風險 PTC，追蹤 1.5–7.6 年）：最大徑 ≥3 mm 成長 **2.2%–10.8%**；體積 ≥50% 增加 **16.0%–28.8%**；新淋巴結轉移 **0%–4.5%**（10 年內）
  - 自然史（引 Nguyen 2025 統合，17 篇）：整體疾病進展 **14.5%**；只看 ≤1 cm 者進展 **8.86%**、≥3 mm 成長 4.51%、新淋巴結轉移 1.55%、體積 ≥50% 增加 17.48%；含 >1 cm 者進展 **19.85%**
  - 「2% to 24% of patients undergoing AS eventually chose to undergo conversion surgery **despite the absence of disease progression**」
  - 手術後果（引 Hsiao 2022，見 ⚠14）：PTMC 全切後永久喉返神經麻痺 **約 0.9%**、永久副甲狀腺低下 **約 1.8%**；半切後喉返神經麻痺 **約 0.2%**、副甲狀腺低下罕見
  - 半切後甲狀腺低下：全體（含良性）約 30%；**只看癌症病人約 60%**；為維持 TSH ≤2 mIU/L 需要藥物者 **>73%**

**[B-G6]** American Thyroid Association Statement on Postoperative Hypoparathyroidism: Diagnosis, Prevention, and Management in Adults. *Thyroid* 2018;28(7):830-841. PMID 29848235; DOI 10.1089/thy.2017.0309
  狀態：**PASS（僅摘要；非 OA，未取得全文）**
  查證路徑：Europe PMC `DOI:"10.1089/thy.2017.0309"` core 查詢，取得逐字摘要。
  可用內容：「HypoPT occurs when a low intact parathyroid hormone (PTH) level is accompanied by hypocalcemia.」風險因子逐字：「bilateral thyroid operations, autoimmune thyroid disease, **central neck dissection**, substernal goiter, **surgeon inexperience**, and malabsorptive conditions.」閾值：「In general, a postoperative **PTH level <15 pg/mL** indicates increased risk for acute hypoPT.」處置策略三選一：「empiric/prophylactic oral calcium and vitamin D, selective oral calcium and vitamin D based on rapid postoperative PTH level(s), or serial serum calcium levels as a guide.」並提醒「Monitoring for **rebound hypercalcemia** is necessary」。

**[B-G7]** *Corrigendum to:* 2025 American Thyroid Association Management Guidelines for Adult Patients with Differentiated Thyroid Cancer. *Thyroid* 2025;35(11):1350. PMID 41182278; PMC13521431; DOI 10.1177/10507256251387671
  狀態：**PASS**
  查證路徑：`europepmc.../PMC13521431/fullTextXML`（HTTP 200）。內容僅涉作者單位、作者中間名、Table 8 列名（改為「Follicular Carcinoma and IEFVPTC」）與若干拼字；**不影響本組引用的任何建議條文**。

**[B-G8]** Thyroid cancer: ESMO Clinical Practice Guidelines for diagnosis, treatment and follow-up†. *Ann Oncol* 2019;30(12):1856-1883. PMID 31549998; DOI 10.1093/annonc/mdz400
  狀態：**FAIL（取不到內容）**
  查證路徑：Europe PMC 標題檢索取得書目；非 OA，無摘要全文可讀。
  → **寫作組不得引用 ESMO 對主動監測／半切／預防性廓清的任何立場。** 2022 年的 ESMO 更新（*Ann Oncol* 2022;33(7):674-684, PMID 35491008）標題自述只涵蓋「systemic therapy in advanced thyroid cancer」，與本組四篇無關。

**[B-G9]** Executive Summary of the 2025 American Thyroid Association Management Guidelines for Adult Patients with Differentiated Thyroid Cancer. *Thyroid* 2025;35(11):1214-1220. PMID 41173539; DOI 10.1177/10507256251390877
  狀態：**書目 PASS／內容 FAIL**（Europe PMC 無摘要，非 OA）。列此條僅供寫作組知道有一份執行摘要存在；引用內容一律回到 [B-G1]。

---

### B1 主動監測：世代資料

**[B-S1]** An observation trial without surgical treatment in patients with papillary microcarcinoma of the thyroid. *Thyroid* 2003;13(4):381-387. PMID 12804106; DOI 10.1089/105072503321669875
  狀態：**PASS**（摘要）
  查證路徑：Europe PMC `DOI:"10.1089/105072503321669875"`。
  可用的數字：1993–2001 年 732 位診斷 PTMC 者中，**162 人選擇觀察**；追蹤期間「more than 70% of tumors either did not change or decreased in size」；**增大超過 10 mm 者 10.2%**；**側頸淋巴結轉移新出現 1.2%**。同期 626 位手術者中，做淋巴結廓清的 594 人，**組織學證實轉移 50.5%**；多發 42.8%；術後復發 5 年 2.7%、8 年 5.0%。（乳突微小癌 ≤10 mm；風險分層＝Kuma 自訂低風險；終點＝結構性進展／術後復發；未做 RAI；手術範圍未分層）

**[B-S2]** An observational trial for papillary thyroid microcarcinoma in Japanese patients. *World J Surg* 2010;34(1):28-35. PMID 20020290; DOI 10.1007/s00268-009-0303-0
  狀態：**PASS**（摘要）
  可用的數字：1993–2004，**觀察 340 人／立即手術 1,055 人**；觀察期 18–187 個月（平均 74 個月）。**增大 ≥3 mm：5 年 6.4%、10 年 15.9%**；**新出現淋巴結轉移：5 年 1.4%、10 年 3.4%**。觀察組中 **109/340** 後續接受手術，「none of those patients showed carcinoma recurrence」。
  排除條件（摘要逐字）：「unless the lesion shows unfavorable features, such as **location adjacent to the trachea or on the dorsal surface of the thyroid possibly invading the recurrent laryngeal nerve, clinically apparent nodal metastasis, or high-grade malignancy on FNAB findings**」
  （乳突微小癌 ≤1 cm；Kuma 低風險；終點＝結構性進展；未做 RAI）

**[B-S3]** Patient age is significantly related to the progression of papillary microcarcinoma of the thyroid under observation. *Thyroid* 2014;24(1):27-34. PMID 24001104; PMC3887422; DOI 10.1089/thy.2013.0367
  狀態：**PASS**（摘要）
  可用的數字：1993–2011，**1,235 人**觀察，期間 18–227 個月（平均 75 個月）。進展定義三項：尺寸增大、新出現淋巴結轉移、進展為臨床疾病（**腫瘤達 12 mm 以上，或新出現淋巴結轉移**）。年輕為獨立預測因子。**「none of the 1235 patients showed distant metastasis or died of PTC during observation」**。**191 人**後續手術，「None showed recurrence except for one in the residual thyroid, and none died of PTC after surgery」。只有 51 人（4%）做過 TSH 抑制。
  （乳突微小癌 ≤1 cm；Kuma 低風險；終點＝結構性進展／疾病特異性死亡；未做 RAI）

**[B-S4]** Incidences of Unfavorable Events in the Management of Low-Risk Papillary Microcarcinoma of the Thyroid by Active Surveillance Versus Immediate Surgery. *Thyroid* 2016;26(1):150-155. PMID 26426735; PMC4739129; DOI 10.1089/thy.2015.0313
  狀態：**PASS**（摘要）
  可用的數字：2005-02 至 2013-08，2,153 人低風險 PTMC；**主動監測 1,179／立即手術 974**。監測組 94 人後續手術，其中因**腫瘤增大 27 人（2.3%）**、因**新出現淋巴結轉移 6 人（0.5%）**。
  **不良事件（立即手術 vs 主動監測）**：暫時性聲帶麻痺 **4.1% vs 0.6%**（p<0.0001）；暫時性副甲狀腺低下 **16.7% vs 2.8%**（p<0.0001）；**永久性副甲狀腺低下 1.6% vs 0.08%**（p<0.0001）；永久性聲帶麻痺僅立即手術組 2 人（0.2%）；**使用 L-thyroxine（補充或抑制）66.1% vs 20.7%**（p<0.0001）；術後血腫 0.5% vs 0%；頸部疤痕 100% vs 0%（原文寫成「8.0% vs 100%」係其自身排版錯誤，方向以「手術組有疤」為準——**依鐵則回報為來源自身標錯，勿照抄該行**）。
  「None of the patients had distant metastases, and none died of the disease.」
  （乳突微小癌 ≤1 cm；Kuma 低風險；終點＝不良事件與結構性復發；手術組範圍混合；未標 RAI）

**[B-S5]** Natural History and Tumor Volume Kinetics of Papillary Thyroid Cancers During Active Surveillance. *JAMA Otolaryngol Head Neck Surg* 2017;143(10):1015-1020. PMID 28859191; PMC5710258; DOI 10.1001/jamaoto.2017.1442
  狀態：**PASS**（摘要）——**這是 MSKCC 世代**
  可用的數字：**291 人**，納入條件為「**intrathyroidal tumors ≤1.5 cm**」；中位監測 **25 個月（範圍 6–166）**；女性 219（75.3%），平均年齡 52（SD 15）。
  **直徑增大 ≥3 mm：11/291（3.8%）**；累積發生率 **2 年 2.5%、5 年 12.1%**。**「No regional or distant metastases developed during active surveillance.」**
  體積量測比直徑早偵測到成長，中位早 **8.2 個月**（範圍 3–46）。成長者呈指數成長，**中位倍增時間 2.2 年**（0.5–4.8）。年輕（HR per year 0.92, 95% CI 0.87–0.98, p=0.006）與「inappropriate」分類（HR 55.17, 95% CI 9.4–323.19, p<0.001）獨立相關。
  （乳突癌；≤1.5 cm 腺內；MSKCC 自訂；終點＝結構性進展；未手術、未做 RAI）

**[B-S6]** Estimation of the lifetime probability of disease progression of papillary microcarcinoma of the thyroid during active surveillance. *Surgery* 2018;163(1):48-52. PMID 29103582; DOI 10.1016/j.surg.2017.03.028
  狀態：**PASS**（摘要）
  可用的數字：1993–2013，Kuma，**1,211 人，20–79 歲**。**10 年進展率（依十歲年齡層）：20 多歲 36.9%／30 多歲 13.5%／40 多歲 14.5%／50 多歲 5.6%／60 多歲 6.6%／70 多歲 3.5%**；**推估終身（至平均 85 歲）進展機率：60.3%／37.1%／27.3%／14.9%／9.9%／3.5%**。
  **⚠ 與 [B-G3] 引述的數字不符（見 ⚠6）。以本摘要為準並註明存在不一致。**
  （乳突微小癌 ≤1 cm；Kuma 低風險；終點＝疾病進展，非死亡；未做 RAI）

**[B-S7]** Insights into the Management of Papillary Microcarcinoma of the Thyroid. *Thyroid* 2018;28(1):23-31. PMID 28629253; PMC5770127; DOI 10.1089/thy.2017.0227
  狀態：**PASS**（摘要）
  可用的數字：Kuma 1,235 人 10 年觀察，**增大 ≥3 mm 者 8%、新出現淋巴結轉移 3.8%**。東京癌研有明（Cancer Institute Hospital）世代 **230 人 300 病灶：增大 7%、新出現淋巴結轉移 1%**；且「macroscopic or rim calcification and poor vascularity were correlated with non-progressing disease」。懷孕期間 51 人中 **8% 增大**，產後補救手術成功。成本：立即手術 10 年總成本為主動監測的 **4.1 倍**（日本醫療體系）。
  「In both series, none of the patients who underwent rescue surgery after progression signs were detected showed significant recurrence or died of PTC.」

**[B-S8]** Active Surveillance of Low-Risk Papillary Thyroid Microcarcinoma: A Multi-Center Cohort Study in Korea. *Thyroid* 2018;28(12):1587-1594. PMID 30226447; DOI 10.1089/thy.2018.0263
  狀態：**PASS**（摘要）
  可用的數字：**370 人**，年齡 51±12 歲，30% <45 歲；起始最大徑 5.9±1.7 mm、體積 81.0±77.7 mm³；中位追蹤 **32.5 個月**。**體積增加 86 人（23.2%）；最大徑增加 13 人（3.5%）**。體積增加累積發生率 2 年 6.9%、3 年 17.3%、4 年 28.2%、**5 年 36.2%**。<45 歲者體積增加風險為年長者 2 倍（p=0.002）。**58 人（15.7%）延遲手術，原因：焦慮 37.9%、腫瘤增大 32.8%、出現頸部淋巴結轉移 8.6%**；病理上 **29.3% 有淋巴結轉移**。
  （乳突微小癌 ≤1 cm；韓國多中心；終點＝影像進展與延遲手術；未做 RAI）

**[B-S9]** Active Surveillance for T1bN0M0 Papillary Thyroid Carcinoma. *Thyroid* 2019;29(1):59-63. PMID 30560718; DOI 10.1089/thy.2018.0462
  狀態：**PASS**（摘要）
  可用的數字：東京癌研有明。T1aN0M0 監測 360 人；**T1bN0M0 共 392 人，其中只有 61 人（約 16%）選擇監測**，其餘 331 人手術。平均監測 **7.4 年**：T1a **29 人（8%）**、T1b **4 人（7%）** 增大（p=0.69）；新出現淋巴結轉移 T1a **3 人（0.8%）**、T1b **2 人（3%）**（p=0.10）。選手術的 T1b 起始腫瘤較大（14.5±2.8 mm vs 11.7±1.1 mm, p<0.0001）。「**No postoperative recurrence was seen in patients with tumor <15 mm in diameter.**」
  （乳突癌 T1b 11–16 mm；終點＝結構性進展／術後復發；未做 RAI）

**[B-S10]** Marked Decrease Over Time in Conversion Surgery After Active Surveillance of Low-Risk Papillary Thyroid Microcarcinoma. *Thyroid* 2021;31(2):217-223. PMID 32664805; PMC7891222; DOI 10.1089/thy.2020.0319
  狀態：**PASS**（摘要）
  可用的數字：**2,288 人**接受主動監測；**162 人（7.1%）在開始監測 12 個月後轉手術**。原因分布：**疾病進展 57、病人意願 43、醫師意願 31、其他甲狀腺或副甲狀腺疾病 24、其他 7**。前半期（2005-02 至 2011-11，561 人）與後半期（2011-12 至 2017-06，1,727 人）相比，後半期各項原因的轉手術率**都顯著較低**。

**[B-S11]** Progression of Low-Risk Papillary Thyroid Microcarcinoma During Active Surveillance: Interim Analysis of a Multicenter Prospective Cohort Study of Active Surveillance on Papillary Thyroid Microcarcinoma in Korea. *Thyroid* 2022;32(11):1328-1336. PMID 36205563; PMC9700369; DOI 10.1089/thy.2021.0614
  狀態：**PASS**（摘要）；試驗註冊 NCT02938702（MAeSTro）
  可用的數字：3 家韓國轉診醫院，**1,177 人**（女 919, 78.1%），中位年齡 48 歲（19–87）。**755 人（64.1%）選監測、422 人（35.9%）選手術**；可分析 706 人，追蹤 41.4 個月（SD 16.0）。**163 人（23.1%）後續手術。**
  **複合進展 68/706（9.6%）；2 年 5.3%、5 年 14.2%。** 各判準：≥3 mm 增大 41/706（5.8%）；2×2 mm 增大 38/706（5.4%）；**新淋巴結轉移 9/706（1.3%）**；新甲狀腺外侵犯 3/706（0.4%）。**「No distant metastases developed during AS.」**
  進展的獨立因子：**診斷年齡 <30 歲 OR 2.86（95% CI 1.10–7.45）、男性 OR 2.48（1.47–4.20）、腫瘤 ≥6 mm OR 1.89（1.09–3.27）**。作者自述「slightly higher than previously reported in other populations」。

**[B-S12]** Expanded Parameters in Active Surveillance for Low-risk Papillary Thyroid Carcinoma: A Nonrandomized Controlled Trial. *JAMA Oncol* 2022;8(11):1588-1596. PMID 36107411; PMC9478884; DOI 10.1001/jamaoncol.2022.3875
  狀態：**PASS**（摘要）
  可用的數字：美國單一學術中心，2014–2021，平均追蹤 37.1（SD 23.3）個月。257 位 **≤20 mm 的 Bethesda 5–6 結節**中 222 人（86.3%）入組；**112 人（50.5%）選主動監測**，中位腫瘤 11.0 mm（IQR 9–15），**10.1–20.0 mm 者佔 59.8%**。
  監測組：**101 人（90.1%）持續監測**；**46 人（41.0%）腫瘤縮小**；**0 人發生局部或遠端轉移**。**>5 mm 成長 3.6%**（累積 2 年 1.2%、5 年 10.8%）；**體積 >100% 成長 7.1%**（2 年 2.2%、5 年 13.7%）。立即手術的 110 人中 **21 人（19.1%）最終病理有 equivocal-risk 特徵**，但全部仍為第 I 期。**兩組疾病特異性存活與整體存活皆 100%。**
  焦慮：立即手術組基線焦慮顯著較高（差 0.39, 95% CI 0.22–0.55, p<0.001），且 4 年後仍在（差 0.50, 95% CI 0.21–0.79, p=0.001）。
  （乳突癌 ≤2 cm；非隨機；終點＝結構性進展與存活；AJCC 第八版「stage I」）

**[B-S13]** Comparison of Postoperative Unfavorable Events in Patients with Low-Risk Papillary Thyroid Carcinoma: Immediate Surgery Versus Conversion Surgery Following Active Surveillance. *Thyroid* 2023;33(2):186-191. PMID 36205580; PMC9986002; DOI 10.1089/thy.2022.0444
  狀態：**PASS**（摘要）
  可用的數字：Kuma 2005–2019，**4,635 人**；主動監測 2,896、立即手術 1,739；**242 人（原文寫 0.8%，此百分比與分子不合——依鐵則回報為來源自身標錯，請以「242 人」為準，勿照抄 0.8%）** 轉換手術。
  「The incidence of unfavorable events… **did not differ between the CS and IS groups**.」CS 組 **無人**永久聲帶麻痺；IS 組 15 人（0.9%）永久聲帶麻痺（其中意外損傷 4 人、癌侵犯 11 人）。IS 組各項不良事件顯著高於 AS 組（p<0.001）。**兩組淋巴結復發率與整體死亡率無差；無人遠端轉移、無人死於甲狀腺癌。**

**[B-S14]** Long-Term Outcomes of Active Surveillance and Immediate Surgery for Adult Patients with Low-Risk Papillary Thyroid Microcarcinoma: 30-Year Experience. *Thyroid* 2023;33(7):817-825. PMID 37166389; PMC10354707; DOI 10.1089/thy.2023.0076
  狀態：**PASS**（摘要）——**這是 Kuma 目前最新、最大的一組**
  可用的數字：1993–2019，**5,646 人**；**主動監測 3,222／立即手術 2,424**。
  監測組：**124 人（3.8%）增大 ≥3 mm**，10 年 **4.7%**、20 年 **6.6%**；**新出現淋巴結轉移 27 人（0.8%）**，10 年 **1.0%**、20 年 **1.6%**。
  手術組：13 人（0.5%）術後淋巴結復發，10 年 0.4%、20 年 0.7%；**1,327 位接受單葉切除者中 18 人（1.4%）殘餘甲狀腺復發**。
  兩組淋巴結轉移率差異：10 年 1.1% vs 0.4%、20 年 1.7% vs 0.7%（p=0.009），「but the differences were small」。
  **接受過 ≥1 次手術者：立即手術 100% vs 主動監測 12.3%；≥2 次：1.07% vs 0.09%（p<0.01）。**
  遠端轉移復發：監測後轉換手術者 1 人、立即手術者 1 人，均存活（診斷後 18.4 與 18.8 年）。**「None of the patients in this study died of thyroid carcinoma.」**

**[B-S15]** A Clinical Framework to Facilitate Risk Stratification When Considering an Active Surveillance Alternative to Immediate Biopsy and Surgery in Papillary Microcarcinoma. *Thyroid* 2016;26(1):144-149. PMID 26414743; PMC4842944; DOI 10.1089/thy.2015.0178
  狀態：**PASS**（全文，經 `https://pmc.ncbi.nlm.nih.gov/articles/PMC4842944/` 取得）
  **這是「主動監測對執行的中心有什麼要求」的原始出處。Table 1 第三欄逐字：**
  - **Medical team characteristics — Ideal**：「Experienced multidisciplinary management team／High-quality neck ultrasonography／**Prospective data collection**／**Tracking/reminder program to ensure proper follow-up**」
  - **Medical team characteristics — Appropriate**：「Experienced endocrinologist or thyroid surgeon／Neck ultrasonography routinely available」
  - **Medical team characteristics — Inappropriate**：「**Reliable neck ultrasonography not available**／**Little experience with thyroid cancer management**」
  - Patient — Inappropriate：「Young patients (<18 years)／**Unlikely to be compliant with follow-up plans**／Not willing to accept an observation approach」
  - Tumor/neck US — Inappropriate：「Evidence of aggressive cytology on FNA (rare)／**Subcapsular locations adjacent to RLN**／Evidence of extrathyroidal extension／Clinical evidence of invasion of RLN or trachea (rare)／N1 disease at initial evaluation or identified during follow-up／M1 disease (rare)／**Documented increase in size of ≥3 mm** in a confirmed papillary thyroid cancer tumor」
  - Tumor/neck US — Ideal：「Solitary thyroid nodule／Well-defined margins／**Surrounded by ≥2 mm normal thyroid parenchyma**／No evidence of extrathyroidal extension／Previous US documenting stability／cN0／cM0」
  另一句可直接翻譯的：「There is little doubt that the excellent outcomes associated with the observation approach at the Kuma Hospital are the result of **careful patient selection by an experienced thyroid cancer management team with access to state-of-the-art cytology and US facilities**.」
  以及「Data from Kuma Hospital convincingly show that patients who are **ideal candidates** for active surveillance will demonstrate a **<1–2% rate of disease progression**.」

**[B-S16]** Outcomes and effectiveness of active surveillance for low-risk papillary thyroid carcinoma: a systematic review and meta-analysis. *Eur Arch Otorhinolaryngol* 2025;282(5):2239-2252. PMID 39668225; DOI 10.1007/s00405-024-09141-7
  狀態：**PASS**（摘要）
  可用的數字：14 篇比較性研究 + 7 篇非比較性，共 **9,397 人**。**AS 期間疾病進展率 14.53%（95% CI 9.59–21.43%）**；**延遲手術率 14.91%（95% CI 8.35–25.21%）**；**兩組皆無甲狀腺癌相關死亡**。
  結論逐字（本組最重要的一句反面證據）：「**Overall complication and recurrence rates were higher in the delayed surgery group than in the IS group.**」以及「AS should be undertaken with caution」。

**[B-S17]** Active Surveillance Versus Thyroid Surgery for Differentiated Thyroid Cancer: A Systematic Review. *Thyroid* 2022;32(4):351-367. PMID 35081743; PMC11265616; DOI 10.1089/thy.2021.0539
  狀態：**PASS**（摘要）——**這是 ATA 2025 委託的系統性回顧，Rec 11 的證據基礎**
  可用的數字：7 篇比較性研究（5 篇世代 N=5,432；2 篇橫斷 N=538）＋7 篇非對照治療系列（N=1,219）。**品質：1 篇 fair，其餘全部 poor。**
  結論逐字：「In patients with low risk (primarily papillary), small (primarily ≤1 cm) DTC, active surveillance and immediate surgery were associated with **similar, low risk of all-cause or cancer-specific mortality, distant metastasis, and recurrence after surgery**.」「rates of subsequent surgery varied and **primarily occurred due to patient preference rather than tumor progression**.」「Four cohort studies (N=88,654) found that surgery associated with improved all-cause or thyroid cancer mortality compared with nonsurgical management, but findings were **potentially influenced by patient age and tumor risk category and highly susceptible to confounding by indication**…」「**methodological limitations preclude strong conclusions**」「Research is needed to clarify… outcomes in **nonpapillary DTC, larger (>1 cm) cancers, and older patients**.」

---

### B2 半切還是全切

**[B-S18]** Extent of surgery affects survival for papillary thyroid cancer. *Ann Surg* 2007;246(3):375-81; discussion 381-4. PMID 17717441; DOI 10.1097/sla.0b013e31814697d9
  狀態：**PASS**（摘要）
  可用的數字：NCDB 1985–1998，**52,173 人**；全切 43,227（82.9%）、單葉 8,946（17.1%）。**PTC <1 cm：手術範圍不影響復發或存活（p=0.24／p=0.83）。≥1 cm：單葉切除復發與死亡風險較高（p=0.04／p=0.009）；只看 1–2 cm 亦然（p=0.04／p=0.04）。**
  （乳突癌；未標 AJCC 版本，時代為第五／六版；終點＝復發與整體存活；未標 RAI）
  → 這是 2015 年前「≥1 公分要全切」的代表性證據。

**[B-S19]** Extent of surgery for papillary thyroid cancer is not associated with survival: an analysis of 61,775 patients. *Ann Surg* 2014;260(4):601-5; discussion 605-7. PMID 25203876; PMC4532384; DOI 10.1097/sla.0000000000000925
  狀態：**PASS**（摘要）——**這就是 SPEC 說的「Adam/Sosa NCDB reanalysis」**
  可用的數字：NCDB 1998–2006，**腫瘤 1.0–4.0 cm 的 PTC 共 61,775 人**；全切 54,926、單葉 6,849。中位追蹤 **82 個月**（60–179）。
  校正後**整體存活**無差：全部 1.0–4.0 cm **HR 0.96（95% CI 0.84–1.09, p=0.54）**；1.0–2.0 cm **HR 1.05（0.88–1.26, p=0.61）**；2.1–4.0 cm **HR 0.89（0.73–1.07, p=0.21）**。
  **重要的選擇偏誤提示（要寫進文章）**：全切組的淋巴結轉移（27% vs 7%）、甲狀腺外侵犯（16% vs 5%）、多發（44% vs 29%）都顯著較多（皆 p<0.001）。
  （乳突癌 1–4 cm；終點＝**整體存活**，非疾病特異性存活；未標 AJCC 版本；RAI 有納入校正）

**[B-S20]** Impact of extent of surgery on survival for papillary thyroid cancer patients younger than 45 years. *J Clin Endocrinol Metab* 2015;100(1):115-121. PMID 25337927; PMC5399499; DOI 10.1210/jc.2014-3039
  狀態：**PASS**（摘要）
  可用的數字：**<45 歲、第 I 期（AJCC 第七版年齡切點）PTC 1.1–4.0 cm**；NCDB 1998–2006（29,522 人）與 SEER 1988–2006（13,510 人）。14 年未校正整體存活兩組相當；校正後 NCDB HR 1.45（0.88–2.51, p=0.19）、SEER HR 0.95（0.70–1.29, p=0.75）；分層後亦無差。
  **⚠ 這篇的「第 I 期」用的是 AJCC 第七版（45 歲切點），與第八版（55 歲）不可互換。**

**[B-S21]** Risk of hypothyroidism following hemithyroidectomy: systematic review and meta-analysis of prognostic studies. *J Clin Endocrinol Metab* 2012;97(7):2243-2255. PMID 22511795; DOI 10.1210/jc.2012-1063
  狀態：**PASS**（摘要）
  可用的數字：**32 篇**。「The overall risk of hypothyroidism after hemithyroidectomy was **22% (95% confidence interval, 19-27)**.」清楚區分臨床／亞臨床者**只有 4 篇**，其估計為**亞臨床 12%、臨床 4%**。抗甲狀腺過氧化酶陽性為術前指標。
  （混合良性與惡性；手術範圍＝單葉切除；終點＝生化與臨床甲狀腺低下；未做 RAI）
  **⚠ ATA 2025 把 22% 轉述為「biochemical hypothyroidism」，與本文不符（見 ⚠5）。**

**[B-S22]** Hemithyroidectomy: a meta-analysis of postoperative need for hormone replacement and complications. *ORL J Otorhinolaryngol Relat Spec* 2013;75(1):6-17. PMID 23486083; DOI 10.1159/000345498
  狀態：**PASS**（摘要）
  可用的數字：**50,445 人**，其中 15,412（30.6%）單葉切除。術後甲狀腺低下發生率報告區間 **10.9%–48.8%**。術前 TSH >2.5 µIU/l 者術後甲狀腺低下 RR **3.16（2.03–4.90）**；甲狀腺抗體 RR 3.52（2.55–4.86）；病理甲狀腺炎 RR 3.30（2.49–4.36）。
  **全切 vs 單葉的併發症合併 RR**：暫時性低血鈣 **10.67（5.75–19.31）**；永久性低血鈣 **3.17（1.72–5.83）**；暫時性喉返神經傷害 **1.69（1.30–2.20）**；永久性喉返神經傷害 **1.85（1.28–2.69）**；出血 **2.58（1.69–3.93）**。

**[B-S23]** Lobectomy for treatment of differentiated thyroid cancer: can patients avoid postoperative thyroid hormone supplementation and be compliant with the American Thyroid Association guidelines? *Surgery* 2018;163(1):75-80. PMID 29122328; DOI 10.1016/j.surg.2017.04.039
  狀態：**PASS**（摘要）
  可用的數字：連續 **555 位單葉切除**；478 人（86%）術前沒吃甲狀腺素。術後 7–10 天有 TSH 值者 394 人，其中 **218 人（55%）TSH >2 mIU/L**；術後 2–12 個月仍未服藥的 225 人中 **132 人（59%）TSH 升到 >2 mIU/L**；**合計 350/478（73%）在一年內 TSH >2 mIU/L**。
  （分化型；手術範圍＝單葉切除；終點＝TSH 目標達成，非甲狀腺低下診斷；未做 RAI）

**[B-S24]** Frequency of Thyroid Hormone Replacement After Lobectomy for Differentiated Thyroid Cancer. *Endocr Pract* 2021;27(7):691-697. PMID 33642257; DOI 10.1016/j.eprac.2021.01.004
  狀態：**PASS**（摘要）
  可用的數字：單一機構 2016-01 至 2020-05，**低風險分化型甲狀腺癌**治療性單葉切除。115 人（91%）有術後 TSH，其中 **97 人（84%）TSH >2 mU/L**；中位追蹤 2.6 年。TSH >2 的 97 人中 **66 人（68%）開始服用 LT4**，中位於術後 **74 天**（IQR 41–126）；其中 **51 人（77%）至少調整過一次劑量**。獨立預測因子只有術前 TSH（HR 1.53, p=0.003）。

**[B-S25]** A national study of postoperative thyroid hormone supplementation rates after thyroid lobectomy. *Surgery* 2024;175(4):1029-1033. PMID 38097483; DOI 10.1016/j.surg.2023.11.016
  狀態：**PASS**（摘要）
  可用的數字：Merative MarketScan，**81,926 人**；單葉切除 33,756（41.2%）、全切 45,104（55.1%）、補全切 3,066（3.7%）。
  **因惡性而單葉切除者用藥比例 59.3%，良性 39.4%**（p<0.001；校正後 aOR **2.34, 95% CI 2.20–2.48**）。
  2015 指引前後（2008–2015 vs 2016–2019）：癌症單葉切除比例 30.3%→**34.3%**（p<0.001）；**補全切 29.8%→25.6%**（p<0.001）；甲狀腺素補充 60.1%→**56.9%**（p=0.04）。

**[B-S26]** Postoperative hypoparathyroidism after completion thyroidectomy for well-differentiated thyroid cancer. *Eur J Endocrinol* 2021;185(3):413-419. PMID 34232122; DOI 10.1530/eje-21-0353
  狀態：**PASS**（摘要）
  可用的數字：單一機構 1990–2015，**786 人**；一次全切 637（81.04%）vs 先單葉再補全切 149（18.96%）。**暫時性副甲狀腺低下：一次全切組高於補全切組（p=0.0057）**（以術後 6 個月評估區分暫時／永久）。
  → 這是「補全切不必然比一次全切更危險」的主要支點，但**是單一機構回溯研究**。

**[B-S27]** A National Comparison of Postoperative Outcomes in Completion Thyroidectomy and Total Thyroidectomy. *Otolaryngol Head Neck Surg* 2021;164(3):566-573. PMID 32838642; DOI 10.1177/0194599820951165
  狀態：**PASS**（摘要）
  可用的數字：NSQIP 2005–2017，**70,638 人**（全切 64,763、補全切 5,875）。30 天死亡率兩者皆 **0.1%**（p>0.05）。至少一項併發症 1.7%（全切）vs 1.4%（補全切）（p>0.05）；術後內科併發症 1.2% vs 0.9%（p=0.0186）。全切者較易回手術室（OR 1.36, 1.04–1.80, p=0.027）與再入院（OR 1.45, 1.16–1.81, p=0.001）。
  **⚠ NSQIP 不收錄甲狀腺專屬併發症（副甲狀腺低下、喉返神經麻痺），所以這篇的「安全」不能拿來談聲音與鈣。**

**[B-S28]** Thyroid Lobectomy vs Total Thyroidectomy in Indeterminate Molecular Risk Thyroid Cancer: A Randomized Clinical Trial. *JAMA Otolaryngol Head Neck Surg* 2026. PMID 42623052; DOI 10.1001/jamaoto.2026.2258
  狀態：**書目 PASS／數字 FAIL**
  查證路徑：Europe PMC `EXT_ID:42623052&resultType=core` 回傳完整書目與作者（Seo YJ, Hughes EG, Wu JX, Yeh MW, Livhits MJ；UCLA），但 `abstractText` 為空，非 OA。
  → 只能引用「有這樣一篇隨機試驗報告存在」，不可引用任何數字。其對應試驗見 [B-S29]。

**[B-S29]** ClinicalTrials.gov NCT06235814 — Molecular Analysis for Precision Surgery in Thyroid Cancer (MAPS) Trial
  狀態：**PASS**
  查證路徑：`https://clinicaltrials.gov/api/v2/studies/NCT06235814`
  可用的內容：`studyType: INTERVENTIONAL`、`allocation: RANDOMIZED`、`phases: ["NA"]`、`overallStatus: COMPLETED`、開始 2024-02-19（ACTUAL）、完成 2026-01-30（ACTUAL）、**`enrollmentInfo: {count: 2, type: ACTUAL}`**、`hasResults: False`、最後更新 2026-02-04。
  主要終點逐字：「**Rate of eligible patients who enroll**… Endpoints are related to **feasibility of a future trial**.」研究摘要逐字：「This is a **pilot feasibility study**… This will be a pilot study for a **future randomized controlled trial (RTC)** to compare between the two surgical approaches…」
  → **「半切 vs 全切至今沒有可用的隨機證據」這句話成立。**

**[B-S30]** Complication Rates of Total Thyroidectomy vs Hemithyroidectomy for Treatment of Papillary Thyroid Microcarcinoma: A Systematic Review and Meta-analysis. *JAMA Otolaryngol Head Neck Surg* 2022;148(6):531-539. PMID 35511129; PMC9073663; DOI 10.1001/jamaoto.2022.0621
  勘誤：Errors in Data Reported in Meta-analysis of Complication Rates of Total Thyroidectomy vs Hemithyroidectomy for Treatment of Papillary Thyroid Microcarcinoma. *JAMA Otolaryngol Head Neck Surg* 2023;149(2):189. PMID 36547950; PMC9912126; DOI 10.1001/jamaoto.2022.4225
  狀態：**PASS（附勘誤警告，見 ⚠14）**
  可用的數字（分母明確）：**17 篇；單葉 1,416 人、全切 2,411 人**（單葉組平均 47.0 歲、84.6% 女；全切組 48.8 歲、77.4% 女）。
  單葉 vs 全切：**暫時性聲帶麻痺 3.3% vs 4.5%**（加權 RR 0.4, 95% CI 0.2–0.7）；**暫時性副甲狀腺低下 2.2% vs 21.3%**（RR 0.1, 0.0–0.4）；**永久性副甲狀腺低下 0% vs 1.8%**（RR 0.2, 0.0–0.8）。
  **對側葉惡性復發：單葉 2.3%，全切 0%。整體復發：單葉 3.8% vs 全切 1.0%（RR 2.6, 1.3–5.4）；但甲狀腺床與頸部復發無差。**
  （乳突微小癌 ≤1 cm；終點＝手術併發症與結構性復發；RAI 狀態未分層）

---

### B3 淋巴結要不要一起清

**[B-S31]** Prophylactic central compartment lymph node dissection in papillary thyroid carcinoma: clinical implications derived from the first prospective randomized controlled single institution study. *J Clin Endocrinol Metab* 2015;100(4):1316-1324. PMID 25590215; DOI 10.1210/jc.2014-3825
  狀態：**PASS**（摘要）——**第一個 RCT**
  可用的數字：**181 人 cN0 PTC**隨機分為 A 組（全切，n=88）與 B 組（全切＋pCCND，n=93）。**追蹤 5 年，兩組結果無差。** A 組接受較多次 ¹³¹I 療程（p=0.002）；**B 組永久性副甲狀腺低下較多（p=0.02）**。「Almost 50% of patients with PTC had micrometastatic lymph nodes in the central compartment, but **none of the presurgical features analyzed, including BRAF mutation, was able to predict their presence**; moreover, to be aware of their presence does not seem to have any effect on the outcome.」只有 3 人被升期、僅 1 人治療策略改變。

**[B-S32]** Randomized trial of prophylactic ipsilateral central lymph node dissection in patients with clinically node negative papillary thyroid microcarcinoma. *Eur Arch Otorhinolaryngol* 2020;277(2):569-576. PMID 31664515; DOI 10.1007/s00405-019-05702-3
  狀態：**PASS**（摘要）（另有作者針對 ITT vs per-protocol 的補充：*Eur Arch Otorhinolaryngol* 2022;279(11):5457, PMID 34708281）
  可用的數字：**164 人**雙盲隨機，單葉切除＋同側 pCND（n=82）vs 不做（n=82）。手術時間、住院天數、術後併發症**均無顯著差異**。pCND 組**隱匿性淋巴結轉移率 50.0%**，淋巴結比 45.2%；**10 人因中央區轉移或切緣陽性改／補做全切**。平均追蹤 73.4 個月：不做組區域復發 1 人、做的那組 3 人；**5 年無復發存活相當**。結論逐字：「it **failed to provide any oncological benefit** for cN0 PTMC patients.」

**[B-S33]** A Randomized Controlled Clinical Trial: No Clear Benefit to Prophylactic Central Neck Dissection in Patients With Clinically Node Negative Papillary Thyroid Cancer. *Ann Surg* 2020;272(3):496-503. PMID 33759836; PMC8496479; DOI 10.1097/sla.0000000000004345
  狀態：**PASS**（摘要）
  可用的數字：**60 人 cN0 PTC** 隨機，全切 vs 全切＋pCND；全部接受術後喉鏡與標準化放射碘。腫瘤平均 2.2±0.2 cm，11.9% 有甲狀腺外侵犯。pCND 組 30 人中 **27.6% 有陽性淋巴結（全部 ≤6 mm）**。
  術後 PTH <10 的比例 33.3% vs 24.1%（p=0.57）；暫時性神經功能異常 13.3% vs 10.3%（p=1.00）——**皆無顯著差**。術後 6 週 Tg<0.2 達成率 54.5% vs 66.7%（p=0.54）；1 年 Tg<0.2 為 88.9% vs 90.0%（p=1.00）；1 年頸部超音波正常比例 85.7% vs 85.1%（p=1.00）。
  （乳突癌；手術範圍＝全切；**有做 RAI**；終點＝生化反應與影像，不是存活）

**[B-S34]** A prospective randomized controlled trial to assess the efficacy and safety of prophylactic central compartment lymph node dissection in papillary thyroid carcinoma. *Surgery* 2022;171(1):182-189. PMID 34391573; DOI 10.1016/j.surg.2021.03.071
  狀態：**PASS**（摘要）
  可用的數字：**101 人**（20–70 歲，小型／非侵犯性 PTC，無臨床轉移），隨機分為全切（50）與全切＋pCND（51）；隨機期間 2015-04 至 2017-11。**追蹤 46.6±9.1 個月，無人結構性復發。** 手術完整度、消融成功率、併發症發生率兩組相同；**pCND 組較多被升期為 pN1a（p<0.05）**。

**[B-S35]** Prophylactic Central Neck Lymph Node Dissection in Low-risk Thyroid Carcinoma Patients Does Not Decrease the Incidence of Locoregional Recurrence: A Meta-analysis of Randomized Trials. *Ann Surg* 2022;276(1):66-73. PMID 35129470; DOI 10.1097/sla.0000000000005388
  狀態：**PASS**（摘要）——**B3 的核心支點**
  可用的數字：**5 個 RCT、763 人**（單純全切 354／全切＋pCND 409）。多數研究偏誤風險低，無發表偏誤。
  **結構性復發：pCND 組 11/409（2.7%）vs 對照 9/354（2.5%），風險差 0%（95% CI −2% 到 2%）。生化復發風險差 0%（−5% 到 4%）。NNT = 500。**
  **永久性副甲狀腺低下：pCND 組較高，風險差 +3%（95% CI 0%–6%）。**
  結論逐字：「We did not find a beneficial effect of prophylactic CND… but did **confirm a higher risk of permanent hypoparathyroidism** associated with this procedure.」

**[B-S36]** ESTIMation of the ABiLity of prophylactic central compartment neck dissection to modify outcomes in low-risk differentiated thyroid cancer: a prospective randomized trial. *Trials* 2023;24(1):298. PMID 37118818; PMC10142499; DOI 10.1186/s13063-023-07294-0（另有 Correction: *Trials* 2023;24(1):452, PMID 37434205）
  搭配：ClinicalTrials.gov **NCT03570021**
  狀態：**PASS**
  查證路徑：Europe PMC 摘要；`https://clinicaltrials.gov/api/v2/studies/NCT03570021`。
  可用的內容：開放標籤多中心第三期，納入 **11–40 mm 乳突癌（Bethesda VI，或 Bethesta V 經術中冰凍確認）**、術前專科超音波無可疑淋巴結。1:1 隨機分為全切＋雙側預防性中央區廓清 vs 單純全切；**兩組皆給 30 mCi 放射碘（rTSH 刺激）**。主要終點：**術後 1 年 excellent response 比例**（未刺激 Tg ≤0.2 ng/mL、無抗 Tg 抗體、頸部超音波正常、治療後掃描無異位攝取）；非劣性界值 5%，單側 α=0.025、power 80%，需 **598 人（每組 299）**。
  試驗登記狀態（2026-03-05 最後更新）：`overallStatus: ACTIVE_NOT_RECRUITING`；開始 2018-08-08（ACTUAL）；**實際收案 352 人（ACTUAL）**；主要完成預估 **2026-12**；整體完成預估 2027-12。
  → **實際收案 352 < 設計 598，寫作時不可暗示它一定能給出定論。**

**[B-S37]** ClinicalTrials.gov NCT06899347 — Impact of PROphylactic Central cOMpArtment Neck Dissection for 2-4 cm Papillary Thyroid Carcinoma
  狀態：**PASS**
  可用的內容：`RANDOMIZED`；`overallStatus: NOT_YET_RECRUITING`；預估開始 2026-04-28；預估收案 **392 人**；主要完成預估 2027-04。

**[B-S38]** Prophylactic Central Neck Dissection for Papillary Thyroid Carcinoma with Clinically Uninvolved Central Neck Lymph Nodes: A Systematic Review and Meta-analysis. *World J Surg* 2018;42(9):2846-2857. PMID 29488066; DOI 10.1007/s00268-018-4547-4
  狀態：**PASS**（摘要）
  可用的數字：**23 篇回溯與前瞻世代、18,376 人**（**全部非隨機**）。pCND 組局部區域復發顯著較低 **OR 0.65（95% CI 0.48–0.88）**；但**暫時性喉返神經傷害 OR 2.03（1.32–3.13）**、**暫時性低血鈣 OR 2.23（1.84–2.70）**、**永久性低血鈣 OR 2.22（1.58–3.13）** 皆顯著較高。

**[B-S39]** The Effect of Prophylactic Central Neck Dissection on Locoregional Recurrence in Papillary Thyroid Cancer After Total Thyroidectomy: A Systematic Review and Meta-Analysis. *Ann Surg Oncol* 2017;24(8):2189-2198. PMID 27913945; DOI 10.1245/s10434-016-5691-4
  狀態：**PASS**（摘要）
  可用的數字：**17 篇、4,437 人**。pCND 組局部區域復發風險比 **RR 0.66（95% CI 0.49–0.90, p=0.008）**；**中央區**復發顯著較低（RR 0.35, 0.18–0.68, p=0.002），**側頸區無差**。pCND 組接受放射碘比例較高（**74.6% vs 59.9%**）；暫時性低血鈣 OR 2.37（1.89–2.96, p<0.00001）、**永久性低血鈣 OR 1.93（1.05–3.57, p=0.03）**、整體併發症 OR 2.56（1.75–3.74, p<0.00001）。作者自述「the evidence is limited and **randomized, controlled trials are needed**」。

**[B-S40]** A meta-analysis of the effect of prophylactic central compartment neck dissection on locoregional recurrence rates in patients with papillary thyroid cancer. *Ann Surg Oncol* 2013;20(11):3477-3483. PMID 23846784; DOI 10.1245/s10434-013-3125-0
  狀態：**PASS**（摘要）
  可用的數字：11 篇、2,318 人。全切＋pCCND 復發率 **3.8%（95% CI 2.3–5.8）**。6 篇比較性研究（1,740 人：全切 995／全切＋pCCND 745）整體復發 7.6%（全切 7.9% vs 加 pCCND 4.7%）；**RR 0.59（95% CI 0.33–1.07，未達顯著）**；**NNT = 31**。永久性低血鈣 RR 1.82（0.51–6.5）；永久性喉返神經傷害 RR 1.14（0.46–2.83）。
  → 注意：**同一群作者（Sosa 團隊）的 NNT 31 與 Sanabria 2022 的 NNT 500 差了一個數量級，差別就在「納入觀察性研究」與「只納入 RCT」。這個對比本身就是 B3 最好的敘事。**

---

### B4 開完刀會少掉什麼

**[B-S41]** The importance of surgeon experience for clinical and economic outcomes from thyroidectomy. *Ann Surg* 1998;228(3):320-330. PMID 9742915; DOI 10.1097/00000658-199809000-00005
  狀態：**PASS**（摘要）
  可用的數字：馬里蘭州 1991–1996 全州出院資料，**5,860 次出院**。外科醫師依 6 年總量分 A（1–9 例）、B（10–29）、C（30–100）、D（>100）。校正後 **最高量組住院併發症率 5.1% vs B、C 組 6.1% vs A 組 8.6%**；住院天數 1.4 天 vs 1.7 vs 1.9。「Length of stay and complications were **more determined by surgeon experience than hospital volume**, which had no consistent association with outcomes.」

**[B-S42]** Is There a Minimum Number of Thyroidectomies a Surgeon Should Perform to Optimize Patient Outcomes? *Ann Surg* 2017;265(2):402-407. PMID 28059969; DOI 10.1097/sla.0000000000001688
  狀態：**PASS**（摘要）
  可用的數字：HCUP-NIS 1998–2009，**16,954 位全切**（47% 癌症）。**外科醫師年手術量中位數 7 例；51% 的醫師 1 年只做 1 例。** 整體併發症 6%。校正後併發症風險隨手術量上升而下降，**直到每年 26 例**（p<0.01）。**81% 的病人由低量醫師（≤25 例/年）開刀**；由低量醫師開刀者併發症 **OR 1.51（p=0.002）**、住院延長 12%（p=0.006）。
  **併發症勝算增加幅度：1 例/年 +87%；2–5 例 +68%；6–10 例 +42%；11–15 例 +22%；16–20 例 +10%；21–25 例 +3%。**

**[B-S43]** Total thyroidectomy is associated with increased risk of complications for low- and high-volume surgeons. *Ann Surg Oncol* 2014;21(12):3844-3852. PMID 24943236; DOI 10.1245/s10434-014-3846-8
  狀態：**PASS**（摘要）
  可用的數字：NIS 2003–2009，**62,722 例**。**全切併發症 20.4% vs 單側 10.8%（p<0.0001）**。高量定義 >99 例/年、低量 <10 例/年；**高量醫師只做了 5.0% 的手術**。低量醫師做全切的併發症勝算 OR 1.53（95% CI 1.12–2.11, p=0.0083）。
  **⚠ 這篇的 20.4%/10.8% 與 ATA 2025 引述的 14.5%/7.6%（高量）、24.1%/11.8%（低量）是同一篇的不同分層，寫作時不可混用。**

**[B-S44]** Effect of surgeons' annual operative volume on the risk of permanent Hypoparathyroidism, recurrent laryngeal nerve palsy and Haematoma following thyroidectomy: analysis of United Kingdom registry of endocrine and thyroid surgery (UKRETS). *Langenbecks Arch Surg* 2019;404(4):421-430. PMID 31254103; DOI 10.1007/s00423-019-01798-7
  狀態：**PASS**（摘要）
  可用的數字：UKRETS 2010-09-01 至 2016-08-31。永久性副甲狀腺低下分析納入 **10,313 例雙側手術**；喉返神經麻痺與血腫分析納入 **25,038 例**。
  「Categorisation of AR showed that PH and RLN palsy rates **declined in surgeons performing >50 cases/year** to a minimum of **3%** and **2.6%** respectively in highest volume AR group (**>100 cases/year**).」血腫與手術量**無**顯著相關。與喉返神經麻痺顯著相關者包括年齡、胸骨後甲狀腺腫、**常規喉鏡**、再手術、淋巴結廓清、雙側手術、神經監測、外科醫師手術量。
  作者自述限制：「limited by a **high proportion of missing data**, which could potentially bias the outcome」；建議下限「tentatively suggests the minimum recommended number of thyroid operations / year should be **50 cases**」。

**[B-S45]** Complications to thyroid surgery: results as reported in a database from a multicenter audit comprising 3,660 patients. *Langenbecks Arch Surg* 2008;393(5):667-673. PMID 18633639; DOI 10.1007/s00423-008-0366-7
  狀態：**PASS**（摘要）
  可用的數字（斯堪地那維亞 26 個科、2004–2006、**3,660 次手術**；良性與惡性混合）：
  - **術後出血 2.1%**（年齡 OR 1.04/歲, p<0.0001；男性 OR 1.90, p=0.014）
  - **術後感染 1.6%**（淋巴結手術 OR 8.18, p<0.0001）
  - **單側喉返神經麻痺 3.9%、雙側 0.2%**；**「Unilateral paresis was associated with… if routine laryngoscopy was practiced (OR 1.92; p=0.0002)」**（← 這句就是 ⚠13 的直接證據）
  - **6 個月後神經麻痺 0.97%**
  - **雙側手術者（n=1,648）：以活性維生素 D 治療的低血鈣 首次回診 9.9%、6 個月後 4.4%**

**[B-S46]** Mortality in patients with permanent hypoparathyroidism after total thyroidectomy. *Br J Surg* 2018;105(10):1313-1318. PMID 29663312; DOI 10.1002/bjs.10843
  狀態：**PASS**（摘要）
  可用的數字：SQRTPA 連結瑞典處方與住院登錄，2005-07-01 至 2014-06-30 **因良性甲狀腺疾病**全切者 **4,899 人**（平均 46.3±15.8 歲，83.1% 女，59.8% 甲狀腺毒症）。**以「術後使用活性維生素 D ≥6 個月」定義永久性副甲狀腺低下：246 人（5.2%）。** 平均追蹤 4.4±2.4 年，109 人（2.2%）死亡。**校正後死亡 HR 2.09（95% CI 1.04–4.20）。**
  **⚠ 良性疾病世代，不可外推至甲狀腺癌。**

**[B-S47]** Morbidity in patients with permanent hypoparathyroidism after total thyroidectomy. *Surgery* 2020;167(1):124-128. PMID 31570150; DOI 10.1016/j.surg.2019.06.056
  狀態：**PASS**（摘要）
  可用的數字：同一登錄，**4,828 人（良性）**，平均追蹤 4.5±2.4 年；**239 人（5.0%）**用藥治療永久性副甲狀腺低下。**腎功能不全 HR 4.88（2.00–11.95）**；任何惡性腫瘤 HR 2.15（1.08–4.27）；**術前已有心血管疾病者，心血管事件 HR 1.88（1.02–3.47）**。作者結語逐字：「These results are a cause of **great concern**.」
  **⚠ 良性疾病世代。**

**[B-S48]** Diagnosis of recurrent laryngeal nerve palsy after thyroidectomy: a systematic review. *Int J Clin Pract* 2009;63(4):624-629. PMID 19335706; DOI 10.1111/j.1742-1241.2008.01875.x
  狀態：**PASS**（摘要）——**B4「怎麼查決定數字」的核心支點**
  可用的數字：**27 篇、25,000 人**。**平均暫時性喉返神經麻痺 9.8%、永久性 2.3%。**「The RLNP rate **varied according to the method of examining the larynx and ranged from 26% to 2.3%**.」多數研究建議追蹤至 1 年才判定。作者主張需要建立「gold standard」以減少報告偏誤。

**[B-S49]** What are the real rates of temporary hypoparathyroidism following thyroidectomy? It is a matter of definition: a systematic review. *Endocrine* 2021;73(1):1-7. PMID 33651345; DOI 10.1007/s12020-021-02663-8
  狀態：**PASS**（摘要）——**B4「定義決定數字」的核心支點**
  可用的數字：**45 篇、23,164 人**。開場逐字：「its incidence varies greatly in the literature **ranging from 0.5% to 65%**. This can be mainly attributed to the **different definition of hypoparathyroidism** used in each study and especially to the **different time cutoff** applied to distinguish temporary from permanent hypoparathyroidism.」
  **以 6 個月為切點的永久性副甲狀腺低下 4.11%，以 12 個月為切點 4.08%（p=0.92）。**

**[B-S50]** The incidence of vocal fold motion impairment after primary thyroid and parathyroid surgery for a single high-volume academic surgeon determined by pre- and immediate post-operative fiberoptic laryngoscopy. *Int J Surg* 2018;56:73-78. PMID 29908329; DOI 10.1016/j.ijsu.2018.06.014
  狀態：**PASS**（摘要）
  可用的數字：單一高量外科醫師，1,547 人、1,580 次手術、**2,527 條有風險的喉返神經**（已排除術前即有異常的 27 條）。全部病人術前與術後立即接受纖維喉鏡。
  **術後聲帶活動受損 2.9%（73/2,527）**；**永久性 9 例（0.4%），其中 3 例為因惡性而刻意切斷神經**（→ 可保留神經者的永久率約 0.24%，這就是 ATA 2025 引述的「0.2%」）。術後立即喉鏡的敏感度 92%、陰性預測值 99.8%。
  **與 B3 直接相關：中央區頸部廓清會提高聲帶活動受損的勝算，aOR 2.4（95% CI 1.0–5.9）**；惡性者 T 期愈高風險愈高（adjusted p-trend<0.001）。

**[B-S51]** Long-term voice changes after thyroidectomy: Results from a validated survey. *Surgery* 2021;170(6):1687-1691. PMID 34344524; DOI 10.1016/j.surg.2021.04.060
  狀態：**PASS**（摘要）
  可用的數字：單一機構 1990–2018 手術者，**電話完成 VHI-10 者 308 人**（平均 51±14 歲，78% 女）；**已排除有記錄神經損傷者**；距手術中位 10.7 年（IQR 2.3–17.5）。
  平均 VHI-10 為 2.6±5.2。**113 人（37%）自述有聲音問題**（該群平均 VHI-10 為 7.1±6.5）；**但 VHI-10 超過常模切點 11 者只有 22 人（7.1%）**（平均 17.6±6.8）。最常見抱怨：「The clarity of my voice is unpredictable」71 人（23%）、「People have difficulty understanding me in a noisy room」70 人（23%）、「I feel as though I have to strain to produce voice」65 人（21%）。
  **⚠ ATA 2025 只引述「over 30%」，沒有帶「只有 7.1% 超過異常切點」。寫作時兩個數字要一起給，否則會嚇到讀者。**

---

## 本組各篇可以寫的東西

### B1〈不開刀，先看著——這是真的，但有條件〉
**站得住的支點**
1. **它是被指引明文寫進去的選項，不是民間偏方**：ATA 2025 Rec 11A（cT1aN0M0，Conditional/Low certainty）、KTA 2025 整本指引、KSThR 2024 超音波共識、JAES 2021 共識。四份文件可以逐字引。
2. **世代規模夠大、終點夠硬**：Kuma 30 年 3,222 位監測者（[B-S14]）——增大 ≥3 mm 3.8%（10 年 4.7%、20 年 6.6%）、新淋巴結轉移 0.8%（10 年 1.0%、20 年 1.6%）、**無人死於甲狀腺癌**；MSKCC 291 人（[B-S5]）——≥3 mm 增大 3.8%，5 年累積 12.1%，**無區域或遠端轉移**；韓國 MAeSTro 706 人（[B-S11]）——5 年複合進展 14.2%。
3. **「有條件」這件事可以逐條列出來**：JAES Table 2 的 7 條立即手術適應症、Brito 2016 的三分類（腫瘤／病人／**醫療團隊**）、KTA 2025 的 4 條納入定義。這三份一起用，就能把紅線 3 撐滿。
4. **「對中心的要求」有明文**：Brito 2016「Inappropriate：Reliable neck ultrasonography not available／Little experience with thyroid cancer management」；KSThR「high-quality US… by experts」；JAES「A multidisciplinary team including US specialists highly experienced in imaging of the neck region is **mandatory**」；ATA 2025「**non-compliance with such follow-up invalidates claims for safety of this approach**」。
5. **影像頻率三份指引一致**：**前 1–2 年每 6 個月，其後每年一次**（ATA 2025 Rec 12／JAES／KSThR 建議 6／KTA 4.1.A）。
6. **退出條件可以逐條寫**：ATA 2025 Rec 14（≥3 mm 增大、新的切片證實淋巴結轉移、遠端轉移、甲狀腺外侵犯、**往後長**、**病人焦慮**、**無法規律回診**、病人選擇手術）；JAES Table 3（直徑達 13 mm 等四條）；KTA 5.2.A。
7. **年齡是真正的分岔**：Kuma 10 年進展率 <40 歲 22.5%／40–59 歲 4.9%／≥60 歲 2.5%；MAeSTro 的 <30 歲 OR 2.86。
8. **監測期間不驗 Tg**（ATA 2025 Rec 13）。
9. **「晚一點開刀」有代價、但不是致命的代價**：永久性併發症不增加（KTA 3.3.A、Sasaki 2023），但暫時性副甲狀腺低下 OR 1.705、暫時性聲帶麻痺 OR 1.519，且手術範圍可能變大；**另有一篇統合分析（Nguyen 2025）報告延遲手術組整體併發症與復發率都較高**。

**寫不了的句子**
- ✗「日本人都這樣做／這是日本的做法」——JAES 自己說沒有隨機研究、也沒有證據等級；且韓國、美國、義大利、哥倫比亞都有世代。
- ✗「只要是小於 1.5 公分（或 2 公分）都可以看著」——ATA 2025 只建議到 cT1a（≤1 cm）；>1 cm 的資料是 Sakai 的 61 人與 Ho 的 112 人。
- ✗「幾乎不會進展」——對 20–30 多歲不成立。
- ✗「你可以自己決定要不要觀察」——三份指引都要求共享決策＋團隊能力評估。
- ✗ 任何「台灣有沒有在做／做得夠不夠」的句子（編輯裁決 + 紅線 4）。
- ✗ 引用 ESMO 的立場（[B-G8] FAIL）。
- ✗ 引用 Miyauchi 終身進展機率而不說明兩個來源數字不一致。

### B2〈半切還是全切〉
**站得住的支點**
1. **逐字引 2015 Rec 35B（Strong, Moderate-quality）與 2025 Rec 15A/B/C**，並寫出「切點從 1–4 公分一整格，變成 2 公分這條線」。
2. **底下的證據是資料庫，不是隨機試驗**：Bilimoria 2007（52,173 人，≥1 cm 全切較好）→ Adam 2014（61,775 人，1–4 cm 整體存活 HR 0.96，無差）→ Adam 2015（<45 歲亦無差）。**必須同時寫 Adam 2014 的選擇偏誤**（全切組淋巴結轉移 27% vs 7%）。
3. **「有沒有隨機試驗」有明確答案：沒有。** ATA 2025 自述「lack of randomized controlled trials」；唯一登記的隨機嘗試 NCT06235814 是可行性 pilot，實際隨機 2 人。
4. **補全切的比例與代價**：ATA 2025 給的區間 5%–43%（統合 11%–34%）、術中轉全切 21%、依病理補全切 27%–30%、「≥20% possibility」；指引前後的實際變化（全切 61%→31%、補全切 74%→20%；另一組 50%→25%；MarketScan 29.8%→25.6%）。代價方面：兩階段手術的風險「similar to… initial near-total/total thyroidectomy」，且暫時性副甲狀腺低下可能**更少**（Giordano 2021）；NSQIP 70,638 人顯示補全切的非甲狀腺專屬併發症不高於一次全切（Brauer 2021）——但要註明 NSQIP 不收錄副甲狀腺與神經併發症。
5. **甲狀腺素這件事（本篇最有用的一段）**：Verloop 22%（19–27）→ 但癌症半切者術後 TSH >2 mIU/L 一年內達 73%（Cox）、84%（Schumm，其中 68% 開藥）、全美理賠 59.3% 用藥（Hu）。並接 ATA 2025 Rec 46A（低／中風險不建議長期抑制）指路 D1。
6. **併發症的相對差距**：Kandil 2013 的 RR 組（暫時性低血鈣 RR 10.7、永久 3.2；喉返神經暫時 1.7、永久 1.9；出血 2.6）；Hsiao 2022 的絕對率（附勘誤警告）。
7. **復發的位置**：ATA 2025「Most recurrences following lobectomy alone appear to occur in the **contralateral lobe** and are successfully salvaged with completion thyroidectomy」；Hsiao：對側葉復發 單葉 2.3% vs 全切 0%，但甲狀腺床與頸部復發無差；Kuma 30 年：1,327 位單葉切除者 18 人（1.4%）殘餘葉復發。

**寫不了的句子**
- ✗「研究證明半切和全切一樣好」——那是**整體存活**（OS），而且是資料庫回溯；ATA 2025 自己說有大約一半的統合分析看到全切復發較低。
- ✗「半切就不用吃一輩子的藥」。
- ✗ 把 Adam 2015 的「第 I 期」當成 AJCC 第八版。
- ✗ 任何「在台灣通常怎麼開」的推論。

### B3〈淋巴結要不要一起清〉
**站得住的支點**
1. **兩件事要先分開**：**治療性**（cN1a／cN1b，摸得到、看得到）與**預防性**（cN0）。ATA 2025 Rec 20A 逐字（Strong, Moderate）＋ Rec 19A/B 逐字。2015 Rec 36A/B/C 作對照。
2. **爭議的形狀**：隱匿性轉移非常常見（Viola 2015 約 50%、Kim 2020 同側 50.0%、Sippel 2020 27.6%，全部 ≤6 mm），**但把它們清掉不會改變結局**。
3. **隨機證據存在，而且比觀察性資料保守**：Sanabria 2022（5 RCT、763 人，復發風險差 0%、NNT 500、永久副甲狀腺低下風險差 +3%）vs 觀察性統合（Chen 2018 OR 0.65；Zhao 2017 RR 0.66；Wang 2013 NNT 31）。**NNT 31 → NNT 500** 是這篇最有力的一句。
4. **併發症差距有數字**：Chen 2018（暫時神經 OR 2.03、暫時低血鈣 OR 2.23、**永久低血鈣 OR 2.22**）；Zhao 2017（暫時 OR 2.37、永久 OR 1.93、整體 OR 2.56，且 pCND 組放射碘用得更多 74.6% vs 59.9%）；Dhillon 2018（中央區廓清使聲帶活動受損 aOR 2.4）。
5. **復發 vs 存活要分開講**：所有來源的終點都是**局部區域復發**或**生化反應**，**沒有任何一份顯示 pCND 改善存活**。Sippel 2020 的終點是 1 年 Tg 與超音波，不是存活。
6. **還沒讀出來的**：NCT03570021（實際 352 人，主要完成 2026-12）、NCT06899347（尚未開始）。

**寫不了的句子**
- ✗「目前沒有隨機試驗」——錯（⚠3）。
- ✗「清淋巴結可以活比較久」。
- ✗ 把 pCND 的併發症數字用在治療性廓清上（後者的基準風險更高）。
- ✗ 把「隱匿性轉移 50%」寫成「一半的人其實已經轉移了，很危險」——三個 RCT 都顯示知道它的存在不改變結局。

### B4〈開完刀會少掉什麼〉
**站得住的支點**
1. **開場就寫「數字取決於怎麼查、怎麼定義」**：Jeannon 2009（喉返神經麻痺報告率 2.3%–26%，視喉部檢查方式）＋ Bergenfelz 2008（常規喉鏡本身 OR 1.92）＋ Koimtzis 2021（副甲狀腺低下文獻 0.5%–65%，6 個月 vs 12 個月切點）。
2. **給「有分母」的數字，並標明世代性質**：
   - 登錄資料（良性＋惡性混合，3,660 例）：單側喉返神經麻痺 3.9%、雙側 0.2%、6 個月後 0.97%；雙側手術者活性維生素 D 治療的低血鈣 首次 9.9%、6 個月 4.4%。
   - 單一高量醫師＋全員喉鏡（2,527 條神經）：受損 2.9%、永久 0.4%（含刻意切斷）。
   - PTMC 統合（單葉 1,416／全切 2,411，附勘誤）：暫時性副甲狀腺低下 2.2% vs 21.3%；永久 0% vs 1.8%；暫時性聲帶麻痺 3.3% vs 4.5%。
   - ATA 2025 的整體區間：暫時性副甲狀腺低下 14–43%、永久 1–25%。
3. **「暫時」與「永久」的界線是人為訂的**：6 個月 vs 12 個月，兩者算出來的永久率其實沒差（4.11% vs 4.08%），但研究之間不可直接比較。
4. **手術量**：ATA 2025 Rec 6 逐字（>25–50 例/年，Strong/Moderate）＋ Sosa 1998（5.1% vs 8.6%）＋ Adam 2017（門檻 26 例；1 例/年 +87% 勝算；81% 病人由 ≤25 例/年的醫師開刀）＋ Aspinall 2019（>50 才下降，>100 時 3%／2.6%；作者自承資料缺失多）。**三個資料庫給三個門檻，要照實寫。**
5. **術後補鈣在管什麼**：ATA 2018 聲明（低 iPTH＋低血鈣才算；術後 PTH <15 pg/mL 提示風險；三種給藥策略；要注意反彈性高血鈣）＋ ATA 2025 Rec 24B（Strong/Moderate）。**不給劑量**。
6. **副甲狀腺永久受損不是小事**（但標好世代）：瑞典登錄良性全切，永久性 5.2%，死亡 HR 2.09（1.04–4.20）、腎功能不全 HR 4.88、心血管事件 HR 1.88（限本來就有心血管疾病者）。
7. **聲音不等於神經受傷**：Li 2021——**排除神經損傷者**後仍有 37% 自述聲音問題，但只有 7.1% 超過 VHI-10 異常切點；ATA 2025 也寫長期聲音改變 >30%。
8. **其他**：術後出血 2.1%、感染 1.6%（淋巴結手術 OR 8.18）；頸部緊繃／吞嚥不適多在術後 3 個月內最明顯、2–3 個月回到基準（ATA 2025 內文）。

**寫不了的句子**
- ✗ 給單一數字說「聲帶麻痺的機率是 X%」。
- ✗ 把良性疾病登錄的死亡 HR 說成癌症病人的風險。
- ✗ 給鈣片與活性維生素 D 的劑量、療程、天數。
- ✗ 把手術量門檻轉成任何台灣的敘述，或暗示讀者去比較醫師（紅線 4、紅線 7）。
- ✗ 把 Hsiao 2022 的數字當成無爭議的定論而不提勘誤。

---

## 查不到的東西（明寫查無）

1. **ESMO 對主動監測／半切／預防性中央區廓清的立場**：ESMO 現行實體癌指引為 2019 年（*Ann Oncol* 30(12):1856-1883, PMID 31549998），非 OA，Europe PMC 無摘要全文，**查無可引用內容**。2022 年更新（PMID 35491008）標題自述只涵蓋晚期全身性治療。→ 寫作組不得引用 ESMO。
2. **2025 ATA 指引的 PDF／原始出版方全文**：Sage（`journals.sagepub.com/doi/10.1177/10507256251363120`）回 **HTTP 403（Cloudflare 挑戰頁）**；Europe PMC `PMC13090833/fullTextXML` 回 **404**。全文係經 `pmc.ncbi.nlm.nih.gov/articles/PMC13090833/` 的 HTML 版取得（HTTP 200）。所有逐字條文均出自該版本。
3. **2025 ATA 執行摘要（PMID 41173539）的內容**：Europe PMC 無摘要，非 OA，**查無**。
4. **〈Thyroid Lobectomy vs Total Thyroidectomy in Indeterminate Molecular Risk Thyroid Cancer: A Randomized Clinical Trial.〉（PMID 42623052）的任何數字**：Europe PMC `abstractText` 為空，非 OA，**查無**。只能引其存在與對應試驗登記（NCT06235814）。
5. **Hsiao 2022 勘誤的具體更動內容**：勘誤本文（PMID 36547950）只說「several errors for the studies included in the meta-analysis… affect the text, Table, Figures, and Supplement」，並指向另一封回覆信（DOI 10.1001/jamaoto.2022.4217）；該回覆信非 OA，**查無逐項更動**。也因此**無法確認 Europe PMC 上的摘要是勘誤前或勘誤後版本**。
6. **BTA（British Thyroid Association）對主動監測的現行條文**：本輪未取得（未查）。若 §九 認為需要非 ATA／非亞洲的第三方指引背書，請指派補查。
7. **主動監測應持續幾年、幾歲可以停**：三份指引一致寫「無證據」。JAES 逐字：「There is no evidence regarding after how many years AS can be discontinued. **AS throughout life is therefore recommended.**」ATA 2025：「The length of necessary follow-up **remains unknown**.」→ 這是「查無」，不是疏漏，文章要照實寫。
8. **主動監測期間 TSH 要不要壓**：無隨機試驗；JAES 與 ATA 2025 都列出互相矛盾的觀察性研究（Kuma 傾向有益、Sugitani 無關、韓國研究顯示高 TSH 與進展相關）。**查無定論**，B1 不可給建議，指路 D1。
9. **分子檢測能否用來篩選主動監測對象**：ATA 2025 逐字「Several retrospective studies… have **conflicting results**」；JAES「Currently, **reliable molecular markers of PTMCs behavior are lacking**」。**查無定論。**
10. **台灣端一切**：依編輯裁決與紅線 4，本組**完全未查**台灣的使用率、分佈、健保列項或臨床實務，brief 內亦無任何可被讀成台灣敘述的句子。E4 若需要健保列項，請依共同規範以全文檔搜尋處理，零筆就寫零筆。
