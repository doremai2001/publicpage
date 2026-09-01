# Brief A — 骨盆腔放射治療專題「誰會被照、怎麼準備」群（A1–A4）

研究員：Group A｜查證日期：2026-09-01｜期刊書目全部經 Europe PMC REST API（`DOI:"..."` 引號查詢／TITLE 關鍵字→DOI 回查）逐筆核對：標題、作者、期刊、卷期頁、年份、PMID、PMCID、DOI、OA 狀態一律照 API 回傳值抄寫；abstract 內的數字逐一比對，凡標「原文逐字」者出自 Europe PMC 回傳之 abstractText。台灣端經實際下載健保署開放資料全表（curl HTTP 200 → odfpy 解析 → 逐欄檢索），抓取路徑逐條註明。
引用規則：**只有標 PASS 的來源可以進正文引用。** FAIL 條目保留並附「這個洞怎麼寫」。每個數字帶癌別／劑量／技術／族群標籤。
起點聲明：候選清單參考了 `_pipeline/cervix/brief-A|B|C.md`、`_pipeline/liver/brief-C.md`（fiducial 段）、`_pipeline/brt/brief-A|B|C.md`（定位、健保全表路徑），但**每一條都在本日重新跑過 Europe PMC／健保開放資料核對**，未沿用任何舊 PASS 標記；其中兩條舊結論被本次查證推翻（見 ⚠1、⚠6）。

---

## ⚠ 七件與 SPEC／既有 brief 假設不同形狀的事（動筆前必讀）

1. **SPEC §一2 的「膀胱準備不是一律憋尿」不只成立，而且證據強度比預期高得多——「全膀胱照射常要空膀胱」有直接的對照研究可引。**
   Guel 2024（格拉斯哥，40 位肌肉侵犯型膀胱癌，55 Gy/20 次，空膀胱組 20 人 vs 滿膀胱組 20 人，plan-of-the-day 適應性放療）[S18]：**滿膀胱組的膀胱體積在模擬 CT 與治療當天 CBCT 之間有顯著差異（p<0.05），空膀胱組沒有（p=0.11）**；接受 25.0–45.8 Gy 的身體體積在空膀胱組顯著較小（p<0.05）；作者結論原文逐字：「This work provides evidence in favour of a BE protocol compared to a BF protocol for radical radiotherapy for MIBC.」
   反向那一邊——直腸癌的 MESORECT 前瞻研究（48 人，同一批病人做滿膀胱與空膀胱兩套流程、各 7 次 CBCT）[S17]：**滿膀胱的膀胱體積平均 243 cm³、SD 高達 164 cm³；空膀胱指令下平均 73 cm³、SD 58 cm³**——「憋出來的體積本身極不可複製」有實測數字。同一份資料裡，中段與下段直腸的前緣位移變異在空膀胱下較小（中段 4.60 vs 5.36 mm；下段 3.03 vs 3.45 mm），上段幾乎不受影響（6.48 vs 5.19 mm）。
   → A3 的框架句「**滿或空由你的計畫決定，主題是複製當初那個狀態**」不只是安全閥，是**有數字撐得住的技術事實**。

2. **「憋越多越好」在婦癌側有兩筆直接反證，而且是臨床終點不是劑量學。** Wu 2026（142 位子宮頸癌術後放療，依模擬時膀胱容積分三組，中位追蹤 48 個月）[S20]：**A 組（≤300 mL）膀胱 V30／V40 最高、小腸 V40 最高；C 組（>500 mL）膀胱與直腸的 D2cm³ 最高（57.85 Gy／51.35 Gy）；B 組（300–500 mL）放射性膀胱炎發生率顯著最低（p=0.0396）**。Wang 2025（71 位子宮頸癌根除術後 VMAT，中位追蹤 33 個月）[S21]：**A 組（<300 mL）晚期放射性膀胱炎最多、C 組（≥500 mL）晚期放射性直腸炎最多**（兩者組間差異皆 p<0.05）。兩篇都收在「300–500 mL 是甜蜜點」。
   → 紅線 2(b)「憋過頭同樣會壞事」**不是常識推論，是可引的臨床數字**。但兩篇都是單中心回溯世代、族群是子宮頸癌術後，標籤不可省。

3. **A2 想寫的兩個時間數字（定位到第一次治療隔幾天、單次治療幾分鐘）確認查無**，與 liver brief 的 FAIL-1／FAIL-2 結論一致（本次重新檢索仍為零）。但**意外撿到兩個「在治療室裡多久」的替代數字**，可帶標籤使用：膀胱癌線上適應性放療（Ethos，8 人 496 次分次）平均治療時長 **14.8 分鐘（範圍 7–49）**[S27]；子宮頸癌 EBRT 治療前後 MRI 之間平均 **27.82±7.12 分鐘（IMRT）／24.14±5.86 分鐘（VMAT）**[S16]。兩者都是特殊流程，**不可寫成「一般骨盆腔放療一次幾分鐘」**。

4. **A3 的直腸段有一個「證據在往回走」的重大轉折，不寫進去就是不誠實。** 經典地標 de Crevoisier 2005（MD Anderson，127 人，78 Gy 3D-CRT，**沒有每日影像導引**）[S29]：模擬 CT 直腸橫切面積 >11.2 cm² 者生化失敗顯著較高（p=0.0009），多變項 HR **3.89（1.58–9.56）**；兩年切片殘存腫瘤機率隨直腸擴張上升（p=0.010）——原文結論句逐字：「an empty rectum is warranted at the time of simulation」。
   **但**同一批英國團隊在現代每日影像導引下重做：Alexander 2023（40 人，5 次或 20 次）[S30] 找不到直腸體積與 intrafraction 位移的相關性，結論原文逐字：「**Findings support the relaxation of strict rectal diameter tolerances and do not support the need for rectal preparation when delivering contemporary IGRT to the prostate.**」Alexander 2026（255＋40 人）[S31] 更進一步：**灌腸只把「大直腸」的比例壓低 10–15%**；大直腸只讓 interfraction 位移「modestly」增加、對 intrafraction 位移沒影響；結論「rectal preparation is not universally required with contemporary IGRT」。
   → A3 直腸段的正確口徑：**「排空的要求是有歷史來源的，但在每日影像導引的今天它正在被鬆綁；你的醫院要求你做什麼，照做，但不必把它當成成敗關鍵。」** 不可寫成「排不乾淨會治療失敗」（那是 2005 年無 IGRT 世代的資料）。

5. **排空手段的證據等級全部偏低，而且系統性回顧明講「沒有一個方法勝出」。** McNair 2014 系統性回顧（18 篇、5 類策略：排便技巧、飲食、瀉劑、灌腸及其組合）原文逐字：「**There is no robust evidence to recommend one rectal emptying strategy over another.**」[S32] 唯一的隨機試驗級證據是 SPoRT（30 人隨機、264 次 CBCT，simethicone 消脹氣）[S33]：**直腸體積與氣體體積整體都沒有顯著下降**（平均降 10%／21%，p>0.05）；只有「第 3 週起直腸體積的變異度」在 simethicone 組內顯著下降（p=0.012）。
   → 甘油球／飲食／排氣藥一律標「證據等級低、無單一方法勝出」，**不可寫成有效的處置**。

6. **【推翻既有 brief 的舊結論】健保 36024B 不是乳癌五次的碼，是「直腸癌術前低分次放射治療」。**
   `brt/brief-A.md` FAIL-4 與 `brt/brief-B.md` 依 2025 年問答集推測 36024B 屬乳癌低分次系列（「20/16/5 次」）。本次直接下載健保支付標準全表（114-05-01 生效版，6,010 項）逐項比對：**36024B「直腸癌術前低分次放射治療」204,966 點，2023-07-01 生效**，適應症原文逐字：「(1)AJCC臨床分期大於等於T3、骨盆腔淋巴結陽性（N+）之直腸惡性腫瘤（C20）或直腸乙狀結腸連接處惡性腫瘤（C19）。(2)AJCC臨床分期T1N0或T2N0之下段直腸（距肛緣5cm以內）惡性腫瘤。」支付規範原文：「本療程採包裹給付，如未執行完全療程，依療程次數**五次**，按等比例核減點數」「執行頻率：**每人終生限給付一次**」「手術後復發之病人如須再次salvage骨盆腔放射治療，不得執行本項」[S59]。
   → 這是本專題台灣端最硬的一塊事實，A1 直腸癌那一格可以直接用；同時**必須回頭修正 brt 專題的 FAIL-4 寫法**（見文末〈給 SPEC 的修正建議〉第 5 條）。

7. **A4 的兩個植入物，證據形狀完全不同，不可寫成同一種東西。**
   fiducial：**沒有隨機試驗**，但有大樣本安全性資料（795 人：敗血症 1%、暫時性尿滯留 1.6%、僅 2 人置放後短期移位、療程中零移位[S41]）與一個「它到底幫到什麼」的量化數字（132 人 2,659 次分次，**17% 的分次因 fiducial 影像發現偏移而中斷做修正、77% 的人整個療程至少被修正過一次**[S34]）。
   間隔物：**有隨機試驗**（Mariados 2015 樞紐 RCT 222 人 2:1[S44]、Hamstra 2017 三年最終結果[S45]），但兩篇 2025/2026 的統合分析在**嚴重毒性那一格都是「沒差」**（Kwon 2026：grade ≥2 的急性與晚期腸胃道毒性皆無顯著差異[S47]；Wong 2025：grade ≥2 晚期直腸毒性顯著較低 RR 0.25，但 **grade ≥3 無差異**[S48]）。
   → A4 的兩段要寫成：「金標是**幫機器看見**，沒有隨機證據但有明確的量化貢獻與已知風險率」vs「間隔物是**把直腸推開**，有隨機證據但獲益集中在輕度終點、嚴重毒性那一格兩份統合都說沒差」。

---

## A1 `pel-who`〈骨盆腔放療用在哪些癌症〉

> 本篇是「一句話級」的地圖。五癌別的治療決定深度一律指路既有專題（SPEC §五）。以下每一格只提供**一句話所需的最小證據錨**。

### Key facts（逐癌別，一格一錨）

**膀胱癌｜保膀胱三聯療法（TURBT ＋ 同步化放療）**

- **同步化療加上去有隨機證據**：BC2001（英國多中心第三期，360 位肌肉侵犯型膀胱癌隨機分配放療±同步 fluorouracil＋mitomycin C）[S2]：**2 年無局部區域疾病存活 67%（59–74）vs 54%（46–62）**，中位追蹤 69.9 個月時 HR **0.68（0.48–0.96，P=0.03）**；5 年總存活 48% vs 35%（HR 0.82，0.63–1.09，P=0.16，**未達顯著**）；治療中 grade 3–4 不良事件 36.0% vs 27.5%（P=0.07）。
- **三聯療法 vs 膀胱全切除**：Zlotta 2023（美加三家大學中心，2005–2017，722 位 cT2-4N0M0、單一病灶 <7 cm、無或單側水腎、無廣泛原位癌，因此**兩種治療都做得到**的病人；440 全切除 vs 282 三聯；傾向分數配對後 1,119 人）[S1]：**5 年無轉移存活 74%（70–78）vs 75%（70–80）（IPTW），SHR 0.89（0.67–1.20，p=0.40）**；5 年癌症特異存活 81%（77–85）vs 84%（79–89）。原文開宗明義：先前比較保膀胱與全切除的隨機試驗**因收案不足而關閉**，「no further trials are foreseen」——這句要寫進去，讀者才知道為什麼證據等級停在傾向分數配對。
- 指引錨：EAU 2025 肌肉侵犯與轉移性膀胱癌指引[S3]，abstract 逐字提到 2025 年新增之建議包括「**for the management of all patients who are candidates for trimodality bladder-preserving treatment in a multidisciplinary team setting using a shared decision-making process**」與「salvage cystectomy after trimodality therapy」的新建議。
- 台灣端：TURBT 對應健保 78008C「膀胱腫瘤之切除－內視鏡下--含膀胱鏡檢」8,027 點／78049C 含輸尿管鏡 8,886 點[S59]。

**子宮頸癌｜根治性同步化放療（＋近接治療）**

- CCCMAC 2008 個別病人資料統合（18 個隨機試驗；其中 13 個比較「化放療 vs 同劑量單獨放療」）[S4]：**5 年存活改善 6 個百分點，HR 0.81（P<.001）**；含鉑（HR 0.83，P=.017）與不含鉑（HR 0.77，P=.009）都有存活益處；急性血液與腸胃毒性上升，**晚期毒性資料太稀疏無法分析**（這一句要誠實帶）。
- 指引錨：ESGO/ESTRO/ESP 子宮頸癌 2023 更新[S5]（本組重新核對書目；逐字條文本次取不到全文，見 FAIL-3）。近接治療的完整證據歸 cx 專題與 cervix brief。
- 深度指路：cx-surgery-or-rt／cx-why-chemo／cx-pelvic-rt-weeks／cx-brachytherapy。

**子宮內膜癌｜術後放療的分層（PORTEC 系列）**

- **PORTEC-1**（715 位 FIGO I 期，全子宮切除＋雙側輸卵管卵巢切除、未做淋巴廓清，隨機骨盆腔放療 46 Gy vs 不治療；中位追蹤 52 個月）[S6]：**5 年局部區域復發 4% vs 14%（p<0.001）；5 年總存活 81% vs 85%（p=0.31，無差異）**；治療相關併發症 25% vs 6%（p<0.0001），grade 3–4 併發症放療組 2%。原文結論逐字：「Postoperative radiotherapy in stage-1 endometrial carcinoma **reduces locoregional recurrence but has no impact on overall survival**」。
- **PORTEC-2**（427 位「高中度風險」I／IIA 期，隨機骨盆腔外照 46 Gy/23 次 vs 陰道近接 21 Gy/3 次 HDR；中位追蹤 45 個月）[S7]：**5 年陰道復發 1.8% vs 1.6%（HR 0.78，p=0.74，非劣性成立）**；5 年局部區域復發 5.1%（近接）vs 2.1%（外照）（HR 2.08，0.71–6.09，p=0.17）；**急性 grade 1–2 腸胃毒性 12.6% vs 53.8%**。結論逐字：「VBT should be the adjuvant treatment of choice for patients with endometrial carcinoma of high-intermediate risk.」
- **PORTEC-3 十年**（660 位高風險，骨盆腔放療 48.6 Gy vs 同樣放療＋化療；中位追蹤 10.1 年）[S8，OA]：**10 年總存活 74.4%（69.8–79.4）vs 67.3%（62.3–72.7），校正後 HR 0.73（0.54–0.97，p=0.032）**；10 年無復發存活 72.8% vs 67.4%（HR 0.74，0.56–0.98，p=0.034）。
- 指引錨：ESGO-ESTRO-ESP 子宮內膜癌 2025 更新[S9]（書目錨；逐字條文取不到，見 FAIL-3）。
- **SPEC §一5：子宮內膜癌與膀胱癌站上尚無專題** → A1 兩格都要註明「另有專題規劃中」，本篇不代寫疾病介紹。

**直腸癌｜術前放療**

- **短程 5×5 Gy（Dutch TME 12 年）**[S10]：1,861 人隨機（5×5 Gy＋TME vs 單獨 TME），**10 年局部復發累積發生率 5% vs 11%（p<0.0001）**；總存活兩組無差；環狀切緣陰性且 TNM III 期者 10 年存活 50% vs 40%（p=0.032）。
- **長程術前化放療（德國 CAO/ARO/AIO-94）**[S11]：823 人隨機（術前 50.4 Gy＋5-FU vs 術後同方案），**5 年局部復發 6% vs 13%（P=0.006）**；5 年總存活 76% vs 74%（P=0.80，無差）；急性 grade 3–4 毒性 27% vs 40%（P=0.001）、長期毒性 14% vs 24%（P=0.01）。
- 台灣端（**本專題最硬的制度事實**）：健保 **36024B「直腸癌術前低分次放射治療」204,966 點**，2023-07-01 生效，適應症與「療程五次、每人終生限給付一次」原文見 ⚠6[S59]。
- 深度指路：rc-five-or-twentyfive（五次 vs 二十五次的完整論證）、rc-diarrhoea、rc-lars。

**攝護腺癌｜根治性放療與術後放療**

- **根治（ProtecT 十五年）**[S12]：1,643 位 PSA 篩檢發現之侷限性攝護腺癌隨機分為主動監測（545）／根除術（553）／放療（545），中位追蹤 15 年、追蹤完整度 98%：**攝護腺癌死亡 3.1% vs 2.2% vs 2.9%（整體比較 P=0.53）**；轉移 9.4% vs 4.7% vs 5.0%；臨床惡化 25.9% vs 10.5% vs 11.0%。原文結論逐字：「prostate cancer-specific mortality was low regardless of the treatment assigned. Thus, **the choice of therapy involves weighing trade-offs between benefits and harms**」。
- **術後（ARTISTIC 統合）**[S13]：三個隨機試驗、2,153 人（1,075 立即輔助放療 vs 1,078 早期救援放療），中位追蹤 60–78 個月；以統一定義之無事件存活比較——**立即輔助放療未顯示優於早期救援**（詳細 HR 見原文；A1 只需一句「立即照 vs 等 PSA 上升再照，隨機證據沒有分出勝負」）。
- 深度指路：pc-rt-how／pc-rp-vs-rt／pc-bowel-urinary。

### Claim ceiling

- **可寫**：「膀胱癌有一條不切除膀胱的路：先做內視鏡刮除，再合併化療與放療；加化療是有隨機證據的（2 年無局部區域疾病 67% vs 54%），而三聯療法與全切除在條件相當的病人身上，5 年無轉移存活 74% vs 75%——但這個比較來自傾向分數配對，不是隨機試驗，因為當年的隨機試驗收不到人而關掉了」；「子宮頸癌的根治性化放療，比單獨放療多 6 個百分點的 5 年存活」；「子宮內膜癌術後照不照、照哪裡，是按風險分層決定的：PORTEC-1 顯示照了局部復發從 14% 降到 4%、但總存活沒有變；PORTEC-2 顯示高中度風險的人用陰道近接就夠，腸胃副作用少很多（12.6% vs 53.8%）；高風險的人加化療十年總存活 74.4% vs 67.3%」；「直腸癌術前放療把 10 年局部復發減半（5% vs 11%，短程）／從 13% 降到 6%（長程化放療），但總存活沒有差」；「攝護腺癌根治：十五年的隨機資料顯示手術與放療的癌症死亡率一樣低（2.2% vs 2.9%），選擇是在權衡副作用；術後要立即照還是等 PSA 上升再照，統合三個隨機試驗沒有分出勝負」。
- **不可寫**：「保膀胱跟切膀胱一樣好」（Zlotta 是配對分析、族群限定在「單一病灶 <7 cm、無廣泛原位癌、無雙側水腎」——條件不符的人不在這份資料裡）；「化放療能治好子宮頸癌」（統合是 6 個百分點的存活改善，不是治癒率宣稱）；「子宮內膜癌術後放療能延長壽命」（PORTEC-1 原文明講 no impact on overall survival；只有高風險加化療那一格有十年存活差異）；「直腸癌照了就不會復發」（照了仍 5%）；「攝護腺癌放療比手術好／手術比放療好」（ProtecT 主要終點 P=0.53）；任何一格展開治療決定的細節（一律指路，SPEC 固定紅線）。
- **必寫**：膀胱癌與子宮內膜癌兩格加「另有專題規劃中」（SPEC §一5）。

### Caveats

- Zlotta 的 440 例全切除只佔同期該三家中心所有全切除的 **29%**——被選進來的是「兩種治療都適用」的那群人，外推要保守[S1]。
- PORTEC-1 的族群沒做淋巴廓清、是 1990 年代收案；PORTEC-2 的中位追蹤只有 45 個月[S6][S7]。PORTEC-3 的分子分型分析是 **post-hoc**，只有 62% 的人有分子資料[S8]。
- Dutch TME 與德國試驗都是 TME 手術品質受控的隨機試驗，且是化療與影像分期都不同的年代[S10][S11]。
- ProtecT 的族群是 PSA 篩檢發現、超過三分之一在診斷時是中高風險；「15 年癌症死亡率低」不等於「不用治療」[S12]。
- CCCMAC 原文自承晚期毒性資料太稀疏無法分析[S4]——A1 不可用它談長期副作用（歸 C 組）。

### 台灣現況（A1 相關）

- 健保支付標準全表（114-05-01 生效版，6,010 項）中與本篇直接相關者[S59]：**36024B 直腸癌術前低分次放射治療 204,966 點**（適應症、五次包裹、終生一次原文見 ⚠6）；**78008C 膀胱腫瘤之切除－內視鏡下--含膀胱鏡檢 8,027 點**；**36011B/36012B 直線加速器遠隔照射治療（每一簡單／複雜照野）1,231／1,334 點**；**36015B 電腦治療規劃--複雜 11,483 點**（備註原文：「指使用三度空間電腦軟體做放射治療之設計，包括順形放射治療、**強度調控放射治療**、立體定位放射治療等技術，以至近接治療之規劃等」）。
- 「誰需要照」本身無給付爭點；技術與影像導引的給付現況見下方〈台灣端總表〉，是 B 組主場。

---

## A2 `pel-sim-day`〈定位那一天會發生什麼〉

### Key facts

**CT 模擬定位（台灣端有明確的制度形狀，比文獻更好用）**

- 健保支付標準全表原文[S59]：**36021C「3D電腦斷層模擬攝影」8,500 點**，備註逐字：「1.**適應症：放射治療前所實施之必要檢查及治療設計**。2.含電腦斷層攝影費用。」另有 **36018B「模擬定位攝影」3,619 點**、**36019B「劑量計算」301 點**、**36001B/36015B 電腦治療規劃（簡單 3,309／複雜 11,483 點）**。
- → A2 可以直接寫：「定位那一天做的事，在健保的分類裡叫做『放射治療前所實施之必要檢查及治療設計』——它不是額外的檢查，是療程的第一步。」這句有官方文字撐著，比任何文獻都貼近讀者。

**固定具（台灣端同樣有制度形狀）**

- 健保[S59]：**37016B「固定模具之設計及製作（大）」1,943 點**，備註逐字：「1.**胸腔、腹腔、骨盆腔及四肢使用**。2.包括技術費及材料費在內。」另 **37030B（小）1,657 點**，備註「頭、頸部使用」。→ 骨盆腔用的是「大」的那一款；材料費已包在裡面（**這一點對費用紀律有用：固定具不是自費項目**）。
- 固定具真的有差嗎（婦癌，可引數字）：Prasad 2024（16 位婦癌病人回溯，BodyFIX 8 人 vs Butterfly Board 8 人）[S35]：骨盆傾斜角度多數落在 BodyFIX ±2°、Butterfly Board ±4°；**因骨盆傾斜而需要重新影像的分次比例 39.1%（BB）→ 19.4%（BodyFIX），約減半**。單中心、樣本 16 人，證據等級低，只能寫成「固定具的差別是真的存在的、量級大概是這樣」。

**俯臥、仰臥與 belly board（SPEC 點名要查，結果比預期分歧）**

- **支持 belly board 的一側**：Wiesendanger-Wittmer 2012 系統性回顧（33 篇符合條件）[S36] 結論原文逐字：「The irradiated SB-V can be **maximally reduced by the use of a prone treatment position combined with a BB** for both 3D-CRT and IMRT, which **might** individually result in a reduction of GI-morbidity.」——注意 might，這是劑量學推論不是臨床終點。Nijkamp 2012（11 位志願者、4 套 MRI、25×2 Gy IMRT 計畫）[S28]：某一款 belly board 相對俯臥平地讓**腸道體積在各劑量層減少 20–30%**；**俯臥與仰臥之間本身沒有差別**；且「**膀胱體積每多 100 cc，腸道 V15 顯著下降 16%**」（後面這句是 A3 的重要素材）。
- **不支持的一側**：Mantello 2026 直腸癌擺位系統性回顧（32 篇）[S38] 原文逐字：「Setup uncertainty was reported to be **very different for prone (w/o belly board) vs supine position, in favour of supine position**」；且「Setup errors can largely be minimized with daily (2D or 3D) IGRT, whereas TV shape variations—particularly in the mesorectum—needs to be assessed daily with 3D imaging and requires anisotropic margins」。Xiao 2025（168 位子宮頸癌術後 VMAT，傾向分數 2:1 配對後俯臥 70／仰臥 42）[S39]：擺位誤差**各軸皆無差異（p>0.05）**；俯臥組腸袋與直腸的低劑量區（V5–V15）反而較高（V10 差 −9.84%，adjusted p=0.040）；**仰臥組白血球下降較多（92.9% vs 71.4%，p=0.0073），俯臥組腹瀉較多（44.3% vs 26.2%，p=0.070）**。
- → A2 的姿勢段正確口徑：「趴著（加 belly board）是為了把小腸推出照野，這件事在劑量分布上是真的；但它同時讓擺位比躺著難一點，而且不同癌別、不同終點的取捨方向不一樣——所以姿勢是**你的計畫決定的**，不是哪個姿勢比較好。」

**皮膚標記與紋身**

- 可引的只有「替代方案存在」這個層級：Lastrucci 2024 範疇回顧（383 篇篩出 21 篇：無紋身法 14、UV 墨水 4、其他 3）[S40] 結論原文逐字：「Tattoo-less techniques are a **promising alternative** to traditional tattoo-based methods」；且明講**乳癌是最常見的應用部位**、多數（13 篇）靠表面導引（SGRT）。→ 骨盆腔的無紋身資料**幾乎不存在**，A2 只能寫「有些醫院已經在用不刺青的方式，但目前多數研究在乳房」。
- 「幾個點、洗澡會不會掉、掉了怎麼辦」等實務細節**無文獻**——寫「以你醫院的說明為準」（沿用 brt/brief-C 的處理方式）。

**兩個確認查無的時間數字（見 ⚠3）**

- 「定位到第一次治療隔幾天」：Europe PMC 檢索（`"time from simulation to" AND "first radiotherapy fraction" AND days` 命中 0；`interval between CT simulation and start of radiotherapy days pelvic` 命中 761 但無任何一篇以此為終點）→ **FAIL-1**。
- 「單次治療躺在床上幾分鐘」：無一般骨盆腔數字（`TITLE:"treatment time" AND (VMAT OR IMRT) AND pelvic AND minutes` 僅 5 筆、皆為特殊流程）→ **FAIL-2**。可帶標籤使用的替代數字見 ⚠3（[S27] 14.8 分鐘＝膀胱癌線上適應性；[S16] 24–28 分鐘＝子宮頸癌治療前後 MRI 之間）。

### Claim ceiling

- **可寫**：「定位那天做的是一次專門為了治療設計的電腦斷層——在健保的分類裡，它的適應症就寫著『放射治療前所實施之必要檢查及治療設計』」；「骨盆腔用的固定模具，健保有專屬項目、材料費含在裡面」；「換一種固定具，因為骨盆傾斜而要重照影像的次數可以少一半（39% → 19%，16 人的單中心資料）」；「趴著加 belly board 可以把腸道受照體積在各劑量層降 20–30%（志願者的計畫比較）」；「但趴著的擺位誤差在直腸癌的系統性回顧裡是比仰臥差的，而且在子宮頸癌術後的配對世代裡，趴著白血球比較保得住、腹瀉卻比較多——姿勢是你的計畫決定的」；「膀胱多裝 100 cc，腸道 V15 少 16%——這就是為什麼很多骨盆腔計畫要你憋尿（但不是全部，見 A3）」；「有些醫院已經改用不刺青的定位方式，目前的研究大多在乳房」。
- **不可寫**：「定位後 X 天開始治療」「一次治療 X 分鐘」（FAIL-1／FAIL-2，**不可挪用 [S27][S16] 的數字充當一般值**）；「趴著比躺著好」或反向（[S36][S38][S39] 方向不一致）；「belly board 能減少腸胃副作用」（原文用 might，是劑量學推論）；「紋身可以不用做了」（骨盆腔幾乎無資料）。

### Caveats

- Prasad 2024 只有 16 人、單中心、回溯[S35]。
- Nijkamp 2012 用的是 11 位**健康志願者**的 MRI，不是病人，也沒有臨床終點[S28]。
- Wiesendanger-Wittmer 2012 是 2012 年的回顧，年代早於現行 IMRT／每日 CBCT 常規化[S36]。
- Xiao 2025 的白血球差異 OR 高達 14.40（95% CI 1.60–129.74）——信賴區間極寬，**不可當成穩健結論**，只能寫成「有這樣的觀察」[S39]。
- 36021C／36018B／37016B 的點數是「表定點數」，不等於病人自付金額；**任何金額換算一律不做**（SPEC 固定紅線）。

---

## A3 `pel-bladder-bowel`〈膀胱與腸道的準備：每天複製同一個狀態〉【核心｜紅線 2】

### Key facts

**（一）滿或空由計畫決定——兩邊都有可引來源**

- **滿膀胱這一邊（婦癌／直腸癌）**：
  - Buchali 1999（29 位子宮頸癌或子宮內膜癌，同一批人各照一套「膀胱直腸皆空」與「皆滿」的計畫 CT）[S14]：**滿膀胱把膀胱的整體劑量負擔壓下來**——D50 由中位 94% 降到 87%（p<0.05）、D66 由 78% 降到 61%（p<0.005）、全膀胱平均 42%→39%（p<0.005）；**直腸的充盈狀態對直腸自身的整體劑量沒有顯著貢獻**。原文結論逐字：「**A full bladder is the prerequisite for an integral dose reduction.**」
  - Nijkamp 2012（直腸癌 IMRT 計畫，滿膀胱流程）[S28]：**膀胱體積每多 100 cc，腸道 V15 顯著下降 16%**。
  - 兩篇 2025/2026 的臨床終點資料把「滿」的甜蜜點釘在 **300–500 mL**（見 ⚠2）[S20][S21]。
- **空膀胱這一邊（全膀胱照射）**：
  - Guel 2024（40 位肌肉侵犯型膀胱癌，55 Gy/20 次，空 vs 滿各 20 人）[S18]：**空膀胱組模擬 CT 與治療 CBCT 之間的膀胱體積無顯著差異（p=0.11），滿膀胱組有（p<0.05）**；空膀胱組偏好選中「中型」計畫、滿膀胱組偏好「小型」；PTV 覆蓋率無差的前提下，**接受 25.0–45.8 Gy 的身體體積在空膀胱組顯著較小（p<0.05）**；兩組的膀胱體積都在療程中從第一次到最後一次顯著縮小（p<0.05）。作者結論偏向空膀胱流程（原文逐字見 ⚠1）。
  - Khalifa 2021（法國兩學會合作、34 個議題的共識建議，15 位放腫、3 位泌尿、1 位腫瘤內科）[S19]：34 項中 30 項達成共識；**未達成共識的四項之一，正是「PTV margins definition for empty bladder and full bladder protocols」**——這句本身就是「兩種流程都存在、專家還沒統一」的最好證據。
- → **A3 的框架句可以寫得比 SPEC 更硬**：「同一個骨盆腔，子宮頸癌／子宮內膜癌／直腸癌的計畫多半要你把膀胱裝到 300–500 mL，因為裝滿的膀胱會把小腸頂出照野；但如果照的是**整顆膀胱**，很多醫院反而要你排空——因為一顆空的膀胱體積比較穩定，照野也比較小。**主題從頭到尾是複製當初的那個狀態，不是憋越多越好。**」

**（二）再現性有多差——實測數字（A3 的心臟）**

| 情境 | 數字 | 來源 |
|---|---|---|
| 直腸癌，滿膀胱流程 | 膀胱體積平均 **243 cm³、SD 164 cm³**（變異幾乎與平均值同量級） | [S17] |
| 直腸癌，空膀胱指令 | 膀胱體積平均 **73 cm³、SD 58 cm³** | [S17] |
| 攝護腺癌 SBRT（要求滿膀胱、空直腸） | 第 5 次分次時膀胱體積平均比模擬 CT 少 **86.9 mL（19.0%）**、直腸少 6.4 mL（8.7%），皆 p<0.01；**模擬時膀胱裝越大的人，療程中掉得越多（ρ=−0.69，p<0.01）** | [S26] |
| 子宮頸癌 EBRT（喝 500 mL、超音波確認後才開始） | 膀胱體積的**分次間變異顯著（p<0.0001）**；單次治療中平均再增加 **30 cc**（p<0.001）；平均充盈速率 **3.43 mL/分鐘** | [S16] |
| 子宮頸癌，膀胱充盈度變化造成的目標位移 | 單一方向位移**最大到 65 mm**；子宮底（tip of uterus）平均 3D 位置變化 **26.1±10.8 mm**（治療前）、**26.8±15.8 mm**（40 Gy 後） | [S15] |
| 子宮／子宮頸本身對膀胱＋直腸充盈的敏感度 | 子宮體：頭尾向中位 **7 mm（95% CI 3–15）**、前後向 4 mm（0–9）；子宮頸：頭尾向 4 mm（−1–6） | [S14] |
| 攝護腺癌，每日 fiducial 影像抓到的治療中位移 | 2,659 次分次中 **17% 的分次需要中斷做修正**；**77% 的男性整個療程至少被修正過一次**；直腸寬度 >3.6 cm 者需要頻繁修正的比例 47% vs 18%（p=0.0016） | [S34] |

- 「**憋出來的體積本身就是最不可複製的那個變數**」這句話，[S17] 的 SD 164 vs 58 是最直接的證據。
- Ahmad 2011 的原文結論句是這一段最誠實的注腳（逐字）：「**For highly conformal (IMRT) treatments, the use of a full bladder drinking protocol results in unacceptably large systematic set-up errors.**」[S15]——A3 要引用它來說明「為什麼還要每天做影像對位」，**不可用它去說『所以憋尿沒用』**（同一篇也顯示膀胱體積與位移之間有可預測的線性關係，殘差僅 2.2±1.7 mm）。

**（三）喝水方案（drinking protocol）的證據**

- Europe PMC 以 `TITLE:"drinking protocol" AND radiotherapy` 檢索命中 **0**——**沒有以喝水方案本身為主題的隨機試驗**（FAIL-4）。可引的只有「方案被寫在流程裡」這個層級：Li 2021 的流程原文逐字「each patient was instructed to **empty the bladder and drink 500 ml water 1 h before** CT simulation and each treatment」，且以超音波確認達到模擬時的體積才開始治療[S16]。
- **有隨機／對照資料的是「有沒有把方案管起來」，不是「喝多少水」**：Yoon 2015（直腸癌化放療，20 人前瞻「教育＋訓練＋以膀胱掃描器持續生理回饋」的方案化維持，對照 20 人自我控管）[S22]：膀胱掃描與模擬 CT 的體積相關性 R=0.87（p<0.001）；**病人內相對體積變化的四分位距中位 32.56% vs 42.19%（p=0.058，未達顯著）**；但邏輯迴歸顯示方案化維持與較小的 IQR 顯著相關（RR 1.045，1.004–1.087，p=0.033），且「IQR<37%」的人數顯著較多（p=0.025）。
- → 「喝多少、什麼時候喝」寫成「照你醫院給的方案做」；**不可自行寫出任何 mL 數或時間**（那是各院的臨床規定，不是可引證據）。唯一可帶的具體數字是 **300–500 mL 這個劑量學／臨床終點的甜蜜點**[S20][S21]，且必須標「子宮頸癌、單中心回溯」。

**（四）超音波量膀胱容積的證據（比想像中分歧）**

- **支持**：Ohira 2022（30 位攝護腺癌中度低分次 VMAT，15 人用 A-mode 攜帶式膀胱掃描器 Lilium）[S23]：CBCT 與掃描器測值相關 r=0.796（p<0.05）；**未用掃描器時「治療當天／模擬」體積比 <0.5 的分次佔 10.3%、>2 的佔 12.7%；用了以後降到 1% 與 2.8%**；膀胱 V30–V40 的平均絕對差異顯著較小（p<0.05）。
- **支持（護理介入版）**：Shimada 2026（60 位攝護腺癌 51.6 Gy/12 次；20 人由放射腫瘤專科護理師以手持膀胱超音波指導＋脫水風險評估）[S25]：**膀胱體積再現性 96.5±12.0% vs 86.9±14.2%（P=0.022）**；**第一次 CBCT 就能開始治療的比例 95.4%（229/240）vs 80.0%（384/480），P<0.001**。
- **限制**：Bai 2024（165 位骨盆腔腫瘤病人前瞻，國產 PBSV3.2）[S24]：與 CT 相關 r=0.874（p<0.001），平均差 −0.14±50.17 mL；但**膀胱容積 >400 mL 時相關係數掉到 0.473**（<400 mL 為 0.868）；男性平均差 12.87 mL 大於女性 3.27 mL；建議「男性與 ≥65 歲者至少重複量兩次」，且「建議在計畫膀胱容積 200–400 mL 時使用」。
- **反例**：Li 2021 明講「The portable US scanner provides a **quick but unreliable** measurement of the bladder volume. There is a significant statistical difference between the results of ultrasonic scanning and that of image scanning.」[S16]
- → A3 口徑：「有些醫院會在治療前用超音波幫你量一下膀胱，這件事在幾份研究裡確實讓再現性變好（96.5% vs 86.9%）；但它是個粗略的量測，體積很大的時候尤其不準——**它是輔助，不是判準，真正的判準是治療前的影像對位。**」

**（五）直腸與腸道準備**

- **歷史來源（為什麼有人要你排空）**：de Crevoisier 2005[S29]（數字與逐字結論見 ⚠4）。**族群標籤絕不可省：78 Gy 3D-CRT、無每日影像導引的攝護腺癌病人。**
- **現代反轉**：Alexander 2023[S30]（中位直腸體積：診斷 MRI 74 cm³、計畫 CT 64 cm³、治療影像 65 cm³；直腸體積與 intrafraction 位移無顯著相關；直腸體積 ≥90 cm³ 的分次位移沒有比較大）；Alexander 2026[S31]（255 人，96 人用微型灌腸、159 人不做任何準備：**灌腸只把「計畫 CT 上直腸 ≥90 cm³」的比例從 28% 壓到 18%，即 10–15 個百分點**；大直腸「modestly」增加 interfraction 的後方位移，但對 intrafraction 位移無影響）。
- **排空手段的證據強度**：McNair 2014 系統性回顧[S32]（逐字結論見 ⚠5）；SPoRT 隨機試驗（simethicone）[S33]（結果見 ⚠5）。**甘油球／灌腸、飲食調整、排氣藥三者都沒有勝出的證據。**
- **「嚴不嚴格」到底影不影響結果**：Byun 2020（85 位攝護腺癌 SBRT 40 Gy/5 次、510 套 CT）[S26]：儘管治療時的膀胱與直腸都比計畫時小，**劑量學影響很小**（膀胱平均劑量 +4.5±12.8%、D2cc 無顯著變化；直腸平均劑量 +7.0±12.9%、D2cc 反而 −2.2±10.1%）；**膀胱體積相對變化、膀胱三角區位移、直腸體積變化，與泌尿或直腸毒性發生率皆無顯著相關**。作者原文：「These results **cast doubt on the need for excessively strict** bladder filling and rectal emptying protocols in the context of image guided prostate SBRT」。
- **腸道與脹氣**：Wu 2026（子宮頸癌近接治療前排除直腸氣體，21 人）[S60]：排氣後直腸體積下降 40.1%、膀胱體積上升 18.2%，直腸 D0.1cc–D5cc 與 Dmax 皆顯著下降（P<0.001）；**但排氣本身讓施體尖端位移 5.86±3.64 mm、子宮頸擋板位移 4.23±3.30 mm**——「處理脹氣本身也會動到東西」。（近接情境，A3 只能一句話帶，深度歸 cx-brachytherapy。）

**（六）療程中會被調整（紅線 2(c) 的證據）**

- 膀胱體積在療程中**系統性地變小**：Guel 2024 兩種流程都是（p<0.05）[S18]；Byun 2020 第 5 次時平均少 19.0%[S26]；Li 2021 觀察到「充盈速率沒有隨療程改變，但**膀胱變得比較不耐受**」[S16]。
- 團隊怎麼接住：plan-of-the-day 適應性放療（Guel 2024 的小／中／大三套計畫[S18]；Varga 2025，8 位膀胱癌、496 次 CBCT，線上適應把 PTV 從平均 416.5 cm³ 降到 296.8 cm³，**減少 30%**，不必要照到的正常組織體積平均減少 43.9%，幾何脫靶次數 13 → 7[S27]）。
- → 紅線 2(c) 可以寫成有名有姓的事實：「**你的膀胱在療程後段會變得比較裝不住，這是被量到的常態，不是你退步了。**團隊看到影像上的偏差就會調整——調整準備方式、甚至換一套當天的計畫——被調整不是你做錯。」

### Claim ceiling

- **可寫（滿或空）**：「有的計畫要滿、有的要空。子宮頸癌、子宮內膜癌、直腸癌的計畫多半要膀胱裝著，因為裝滿的膀胱會把小腸頂開（膀胱每多 100 cc，腸道 V15 少 16%）；**但如果照的是整顆膀胱，很多醫院用的是空膀胱流程**——因為空膀胱的體積比較穩定（滿膀胱的體積 SD 164 cm³ vs 空膀胱 58 cm³），照野也比較小。連專家共識都還沒統一這兩種流程的邊界該怎麼畫。」
- **可寫（不是憋越多越好）**：「300 到 500 毫升是子宮頸癌那兩份回溯資料指出來的甜蜜點：低於 300，膀胱自己被照得多、晚期膀胱炎多；高於 500，直腸與乙狀結腸被照得多、晚期直腸炎多。」「模擬那天憋得越大的人，療程中掉得越多（相關係數 −0.69）——一開始就衝到極限，反而最難複製。」
- **可寫（再現性）**：「同一個人，同樣的指令，膀胱容積在不同天的落差可以跟平均值一樣大」；「膀胱充盈度的改變可以把子宮推動到 65 毫米，子宮底的平均位移是 26 毫米」；「攝護腺癌病人裝了金標之後，17% 的分次會因為看到偏移而中斷修正，77% 的人整個療程至少被修正過一次」。
- **可寫（腸道）**：「要你排空直腸的做法，來源是 2005 年一份沒有每日影像導引的資料——那時候直腸脹著會讓照野打偏，生化失敗風險是 3.9 倍。但在每日影像導引的今天，同一個問題被重新檢查：灌腸只把『大直腸』的比例壓低一成到一成五，而且大直腸並沒有讓治療中的位移變大。」「排空的方法——甘油球、飲食、排氣藥——系統性回顧的結論是沒有任何一種勝出；唯一的隨機試驗（消脹氣藥）連直腸體積都沒有真的降下來。」
- **可寫（療程中調整，紅線 2c）**：「你的膀胱在後面幾週會變得比較裝不住——這被量到過，是常態。」「有些醫院會準備大中小三套計畫，當天看影像挑一套。」
- **不可寫（紅線 2 的兩個方向）**：
  - ✗「憋尿是骨盆腔放療的標準準備」「憋越滿越好」——[S18][S19][S20][S21] 四路推翻。
  - ✗「憋不憋其實沒差」——[S14][S17][S20][S21][S28] 顯示膀胱狀態實質改變劑量分布與晚期毒性。
  - ✗「排不乾淨會讓治療失敗」——[S30][S31] 在現代 IGRT 下已不支持；de Crevoisier 的族群標籤不可省。
  - ✗ 任何具體的「喝幾毫升、幾點喝、憋幾分鐘」——FAIL-4，這是各院臨床規定。
  - ✗「用超音波量就準了」——[S16][S24] 都有明確限制。
  - ✗ 把 [S17] 的直腸癌數字、[S26] 的攝護腺癌數字、[S16] 的子宮頸癌數字互相搬用——族群與流程都不同。
- **必寫（紅線 2 的三件事）**：(a) 憋不住、解不乾淨要說出來，不要硬撐——文中要有一句明確的「說出來的門檻」；(b) 憋過頭同樣會壞事（[S20][S21] 的 >500 mL 那一格 ＋ [S26] 的「起點越大掉越多」）；(c) 團隊會依影像調整（[S18][S27] 的 plan-of-the-day）。

### Caveats

- [S20][S21] 都是單中心回溯世代（142 人／71 人）、族群是子宮頸癌術後放療、以「模擬時的膀胱容積」分組——**不是隨機試驗，也不能外推到根治性化放療或其他癌別**。
- [S18] 是 40 人的回溯稽核、比較的是兩個不同時期的流程（非隨機），且其優勢終點是劑量學（身體受照體積）不是臨床事件。
- [S17] 的作者欄由 Europe PMC 回傳為「Alexandre J, Audrey BL, Camille L, …」——疑為名／姓欄位順序異常，撰稿人若需列作者請照本表抄，或僅寫「MESORECT 研究」。
- [S15] 只有 13 人；[S16] 43 人；[S23] 30 人；[S25] 60 人回溯——全部是小樣本，數字寫成「量級」而非精確值。
- [S30][S31] 的族群是攝護腺癌、每日 3D 影像導引；**不可外推成「所有骨盆腔癌別都不必做腸道準備」**。
- [S29] 的年代（2005）與技術（78 Gy 3D-CRT、無每日 IGRT）是這條 claim 的全部前提。
- **證據等級標籤對照**（SPEC §一1「劑量學較優」與「臨床結果證實較優」永遠分開寫）：
  - 劑量學／幾何終點：[S14][S17][S18][S23][S26][S27][S28][S60]
  - 臨床事件終點（毒性發生率）：[S20][S21]（皆回溯世代）
  - 隨機試驗：**只有 [S33]（simethicone，陰性結果）**——A3 全篇沒有一個「準備方式改善臨床結果」的隨機證據，這件事要在文中誠實出現。

### 台灣現況（A3 相關）

- 健保支付標準全表逐欄檢索[S59]：**查無「影像導引放射治療／IGRT」獨立診療項目**（「影像導引」四字在全表 9 筆命中中，放射治療章節只出現在 37029B 加馬機立體定位放射手術，其餘為插管、乳房穿刺、脊椎／腦機械手臂系統）；**查無膀胱超音波掃描於放射治療流程的專屬項目**；**查無任何準備衛教／護理指導的獨立項目**。→ 這三件事在健保端沒有價格形狀，A3 的費用段只寫「這些準備本身不是額外收費的項目，如果你被告知有任何費用，請向醫務課確認」。
- 骨盆腔放療本體以 36011B/36012B 照野碼＋36015B 電腦治療規劃（複雜）申報[S59]；直腸癌術前五次者走 36024B 包裹（見 ⚠6），且 36024B 備註明訂**不得同時申報 36011B–36013B、36015B、36018B–36020B、36021C、37013B–37016B、37030B 等**[S59]。

---

## A4 `pel-implants`〈金標與間隔物：兩種植入物，兩種目的〉【紅線 3】

### Key facts

**（一）Fiducial marker（金標）——攝護腺**

- **怎麼放**：經直腸超音波導引下、以 18G 針置入 3 顆金標（3×0.6 mm）是最大宗的可引描述[S41]（795 人、2018–2023 單中心）。經會陰 vs 經直腸兩條路徑的比較：Hong 2024 系統性回顧與統合分析（13 篇觀察性研究）[S42]：**經會陰的泌尿道感染與直腸出血風險顯著較低**；結論原文逐字：「The use of both TP and TR techniques for placing gold seed fiducial markers has proven to be an **effective, safe, and well-tolerated** method…A significant benefit of the TP technique is its ability to **avoid rectal puncture**」。
- **併發症率（帶分母）**[S41]：795 人全部技術成功；**術後敗血症 1%、暫時性尿滯留 1.6%**；**僅 2 人在置放後短期發生標記移位，療程中無任何移位**；無其他重大併發症。
- **跨器官對照（不可與攝護腺混用）**：Kothary 2009（139 次經皮置放：肺 44、胰 61、肝 34）[S43]：**主要併發症 5%、次要併發症 17.3%**；氣胸主要出現在肺（44 次中 20 次、45%，其中 7 次需胸管）；**6 次（4.3%）標記移位需再處理**；結論「風險與傳統經皮器官切片相近」。→ 這是既有 liver brief 的來源，**本專題若引用必須標明「這是經皮肺／胰／肝的資料，不是攝護腺經直腸的資料」**。
- **它到底幫到什麼（量化貢獻）**：Serra 2025（132 位攝護腺癌 VMAT、2,659 次分次，每 15 秒觸發 kV 影像，任兩顆金標超出 3 mm 容許度即修正）[S34]：**582 次修正發生在 463 次分次（17%）；77% 的男性整個療程至少被修正一次**；多變項分析中**只有直腸體積與直腸寬度與位移相關**（直腸寬 >3.6 cm 者「需頻繁修正」比例 47% vs 18%，p=0.0016）。→ 這一個數字同時服務 A3（直腸大小是有後果的）與 A4（金標的貢獻是「讓看不見的偏移被看見」）。

**（二）Fiducial——其他癌別的現況（SPEC 要求查「子宮頸／直腸的使用現況」）**

- **膀胱癌**：有前瞻試驗級資料。Greer 2022（15 人，TURBT 時在腫瘤床周圍注射可吸收顯影水膠 TraceIT）[S55]：94%（90–98）的注射點在放療開始時仍可見、放療結束時 71%（62–81）；中位可見天數 106 天；**以標記對位可讓初期照野的 PTV 邊界從 1.56 cm 降到 0.67 cm**（但 boost 階段沒有好處：1.01 vs 0.96 cm）；中位追蹤 22 個月**無任何可歸因於置放的急性或晚期併發症**。
- **子宮內膜癌（陰道殘端）**：只到單中心初步經驗。Titone 2025（6 人，3 顆 0.40×10 mm 金標）[S56]：全部完成治療、**無任何急慢性毒性、無標記脫落**；20 套 CBCT 分析，Dice 中位 0.90；**僅 2 位病人出現 >5 mm 的分次內位移，且與直腸體積變化有關**。
- **直腸癌**：只到可行性研究。Rigter 2019（20 人前瞻多中心，內視鏡超音波導引，4 種標記、2 種置放策略，共 64 顆）[S57]：無嚴重不良事件；**3 位病人有 1 顆誤置（2 顆進攝護腺、1 顆進腹腔內），無臨床後果**；中位 17 天後**僅 42/64（66%）仍在位——腫瘤內 55% vs 直腸繫膜內 90%（P=0.009）**。
- **子宮頸癌**：Europe PMC 檢索未找到可引的置放併發症或成效系列（多為 MRI 標記線、近接施體或裝置開發）→ **FAIL-5**。
- → A4 可寫：「金標不是每個癌別都在用。攝護腺癌是它的主場（大樣本安全性資料、明確的量化貢獻）；膀胱癌有前瞻試驗、子宮內膜癌與直腸癌還停在單中心經驗與可行性研究的階段，直腸癌的標記甚至有三分之一在兩三週內就掉了；子宮頸癌我查不到可引用的臨床系列。**它視病情，不是流程必備。**」（呼應 SPEC §一4 與紅線 3。）

**（三）SpaceOAR／直腸間隔物——隨機證據那一半**

- **樞紐 RCT（Mariados 2015，222 人 2:1 隨機；IG-IMRT 79.2 Gy/1.8 Gy；所有人都先放了 fiducial）**[S44]：置放成功率 99%；**攝護腺與直腸之間的間距 12.6±3.9 mm vs 對照 1.6±2.0 mm**；**直腸 V70 由 12.4% 降到 3.3%（P<.0001）**；**試驗中無裝置相關不良事件、無直腸穿孔、無嚴重出血或感染**；急性直腸不良事件整體率相近（間隔物組直腸疼痛較少，P=.02）；**3–15 個月晚期直腸毒性嚴重度顯著較低（P=.04），發生率 2.0% vs 7.0%，間隔物組無任何 grade 1 以上晚期直腸毒性**；15 個月時腸道生活品質下降 10 分以上者 11.6% vs 21.4%；**12 個月 MRI 確認水膠已被吸收**。
- **三年最終結果（Hamstra 2017）**[S45]：**3 年 grade ≥1 直腸毒性 9.2% vs 2.0%（P=.028）、grade ≥2 為 5.7% vs 0%（P=.012）**（皆為對照 vs 間隔物）；grade ≥1 尿失禁 15% vs 4%（P=.046），**grade ≥2 泌尿毒性無差（7% vs 7%，P=0.7）**；3 年腸道生活品質差 5.8 分（P<.05，達最小重要差異）；3 年時腸道 QOL 出現最小重要差異下降者 41% vs 14%（P=.002）、泌尿 30% vs 17%（P=.04）。
- **統合分析（兩份，2025/2026）**：
  - Kwon 2026（35 篇、4,664 人；OA）[S47]：**直腸 V50 減少 51.8%、V70 減少 56.8%**（體積制）／54.5% 與 62.2%（百分比制）；**急性泌尿毒性（任何級與 grade ≥2）無差**；晚期泌尿毒性（任何級）較低、**grade ≥2 無差**；急性腸胃毒性（任何級）顯著較低（低分次更明顯）、**grade ≥2 無差**；晚期腸胃毒性（任何級）較低、**grade ≥2 無差**。結論原文逐字：「their **limited impact on severe toxicity** highlights the need for further research」。
  - Wong 2025（17 篇：3 個 RCT、3 個前瞻世代、11 個回溯；3,200 人）[S48]：**晚期 grade ≥2 直腸毒性 1.62% vs 9.35%（RR 0.25，0.15–0.42，P<0.001）**；早期 grade ≥2 為 3.07% vs 6.05%（RR 0.53，0.33–0.86，P<0.001）；**grade ≥3 腸胃事件（急性或晚期）無差異**；腸道生活品質無統計差異（risk difference −0.16，−0.38–0.06，P=0.15）。
- → **兩份統合的共同交集：嚴重毒性（grade ≥3）那一格沒有差別。** 這是 A4 唯一不可省略的句子。

**（四）間隔物的併發症與失敗案例（紅線 3「誠實寫」）**

- **上市後通報資料庫（MAUDE）三份分析，數字方向一致但詮釋不同——三份都要引，讓讀者看見分歧**：
  - Hathout 2025（廠商提供銷售資料為分母；2015-01-01 至 2023-12-31，**1,005 份通報／251,836 套售出**；OA）[S49]：**通報率整體 0.40%**（2015 年 0.00% → 2023 年 0.57%）；**死亡 5 例，佔售出量的 0.002%**；最常見裝置端事件為置放／定位問題（0.295%）；最常見病人端事件為「無臨床症狀」（0.175%）、疼痛不適（0.110%）、**感染（0.052%）、廔管（0.037%）、出血（0.033%）**。結論：整體都在 1% 以下、多數無臨床後果。
  - Fernandez 2024（2015-06 至 2022-10，574 例納入）[S50]：**死亡 3 例（佔所有不良事件 0.5%）**；CTCAE **grade 4 佔 1.6%、grade 3 佔 15.9%、grade 2 佔 24.2%、grade 1 佔 57%**；**29 例（9%）做了腸道改道**。原文列舉的併發症種類逐字：「Death, **gel embolization, anaphylaxis, rectal ulcerations, and infections requiring bowel or urinary diversions**」。
  - Millot 2024（2015-01 至 2023-05，981 份通報／990 件事件；同期售出 206,619 套）[S51]：故障 626 件、病人傷害 350 件、**死亡 5 件**；**膿瘍與廔管各 91 件**；**22.4% 的相關不良事件發生在放療開始之前**（作者指出「是裝置而非放射線造成的」）；**CTCAE grade ≥3 佔 13.1%**。原文結論逐字：「many of which are **more serious than have been reported in clinical trials**…these data highlight the need for continued postmarket surveillance.」
  - → **正確寫法**：「這些是自願通報的資料庫，分母是賣出去的套數不是實際植入數，通報率整體在 1% 以下；但通報進去的案子裡，有 13% 是 CTCAE 三級以上，也有膿瘍、廔管、凝膠栓塞、過敏性休克與死亡的紀錄，而且有超過兩成的事件發生在放療還沒開始之前。**這不是罕見到不用提的事，也不是常見到不該做的事——它是一個你該問清楚的取捨。**」
- **個案報告（可具名的失敗形狀）**：
  - 過敏性休克：Nesi 2024，SpaceOAR Vue 置放過程中發生 anaphylactic shock[S53]。
  - 感染／敗血：Markey 2025，近接治療前置放後發生**急性攝護腺炎與敗血性休克**[S54]。
  - **凝膠栓塞（gel embolization）** 與腸道／泌尿改道：由 MAUDE 分析列名[S50]。
- **直腸壁內注射（rectal wall infiltration）——結果與直覺相反，要誠實寫**：Grossman 2024（樞紐 RCT 中 149 位間隔物組的植入後 T2 MRI 判讀）[S52]：**62.4% 完全無直腸壁訊號異常，24% 有影像上的直腸壁內浸潤（部分浸潤 20.1%、全層 4.0%）**；然而**浸潤程度與手術當下、急性、晚期直腸毒性皆無相關（P=.64／.64／.85）**；全層浸潤的 6 人在 15 個月內無人發生晚期直腸毒性。→ 「影像上看到凝膠跑進直腸壁，在這份隨機試驗的資料裡並沒有轉成更多的直腸副作用」——**這句要寫，因為它防止把 MAUDE 的嚴重案例誤讀成常態**。

**（五）誰不需要／誰不適合（紅線 3 要求成段）**

- **「誰不會受益」的隨機試驗次分析結果，是一個反直覺的空答案**：Quinn 2020（樞紐試驗 222 人的次級分析）[S46]：**跨年齡、BMI、既往手術、標的體積、放療計畫品質等預後分組，間隔物降低腸道生活品質下降風險的相對益處沒有統計上的異質性**；即使在 >95% 已達成 QUANTEC 直腸劑量限制的計畫中，間隔物仍帶來可能有意義的益處；攝護腺體積與直腸 V70 無相關（r=0.077）。→ **不能寫「攝護腺大的人比較需要」或「計畫做得好就不用」——這兩個直覺都被這份次分析否掉了。**
- **可具名的「不適合」只有一個，而且來自失敗經驗**：Yates 2025（8 位**曾接受骨盆腔放射線治療**、因再照射而置放 SpaceOAR 的連續病例）[S58]：併發症從骨盆疼痛到**直腸穿孔、膿瘍、廔管**，**8 人中 2 人發生嚴重併發症**。原文結論逐字：「**We urge caution when using SpaceOAR in this patient group.**」
- **制度層面的「不需要」**：SPEC §一4 已定案——**間隔物不是本科提供的項目**；A4 寫成「一個你可以去問的選項」，費用與執行單位導向該科與醫務課。
- → 「誰不需要」那一段的可寫內容：(1) 它只有攝護腺癌的隨機證據，其他四個癌別沒有；(2) 曾照過骨盆腔的人風險明顯較高，有團隊明講要謹慎；(3) 兩份統合在嚴重毒性那一格都是沒差——**如果你最擔心的是嚴重的晚期直腸副作用，目前的證據沒辦法保證它會幫上忙**；(4) 它不是本科提供的項目。

### Claim ceiling

- **可寫（金標）**：「金標是三顆比米粒還小的金屬點，用超音波導引、細針放進攝護腺裡，目的只有一個：讓每天的影像看得見攝護腺在哪裡」；「795 人的單中心資料裡，術後敗血症 1%、暫時性解不出尿 1.6%，只有 2 人在置放後短期發生移位，療程中沒有再移位」；「經會陰放比經直腸放，泌尿道感染與直腸出血都比較少」；「它的貢獻可以量化：一份 2,659 次分次的研究裡，17% 的分次因為金標影像看到偏移而中斷修正，77% 的人整個療程至少被修正過一次」；「不是每個癌別都在做——攝護腺是主場，膀胱癌有前瞻試驗，子宮內膜癌與直腸癌還在單中心經驗的階段，直腸癌的標記甚至有三分之一在兩三週內掉掉了」。
- **可寫（間隔物）**：「間隔物是一團會被身體吸收的水膠，注射在攝護腺與直腸之間，把直腸推開大約一公分（12.6 mm vs 對照 1.6 mm），一年後 MRI 上就吸收掉了」；「隨機試驗裡直腸 V70 從 12.4% 降到 3.3%，三年的 grade ≥2 直腸毒性 5.7%（不放）vs 0%（放）」；「兩份 2025、2026 年的統合分析都同意：輕度的腸胃副作用有減少，**但嚴重（三級以上）的那一格，兩份都是沒有差別**」；「上市後通報資料庫裡，通報率整體不到 1%，但通報進去的案子有 13% 是三級以上，也有膿瘍、廔管、凝膠栓塞、過敏性休克與死亡的紀錄，而且超過兩成的事件發生在放療開始之前」；「影像上看到凝膠跑進直腸壁的比例有 24%，但在隨機試驗的追蹤裡，它並沒有轉成更多的直腸副作用」；「曾經照過骨盆腔的人再放間隔物，有一個 8 人的系列裡 2 人出現嚴重併發症，作者明講要謹慎」。
- **不可寫**：「金標／間隔物人人該做」（紅線 3）；「間隔物能減少嚴重的直腸副作用」（[S47][S48] 在 grade ≥3 皆無差）；「間隔物很安全，臨床試驗裡沒有併發症」（[S44] 的零併發症是 222 人的試驗族群，[S50][S51] 的上市後資料形狀不同——**兩者必須並陳**）；「攝護腺大的人／計畫做不好的人才需要」（[S46] 否定）；把 Kothary 2009 的 5% 主要併發症率當成攝護腺金標的風險（那是肺／胰／肝經皮置放）；任何金額、任何「值得」「不貴」的措辭（SPEC 固定紅線）；點名執行機構。
- **必寫**：SpaceOAR 不是本科項目（SPEC §一4、紅線 3）；「誰不需要」成段；fiducial 寫成視病情。

### Caveats

- Mariados 2015 與 Hamstra 2017 是**同一個試驗**的不同時間點（222 人、2:1、單盲、廠商贊助的樞紐試驗），且**對照組也全部放了 fiducial**——所以這份試驗比較的是「有沒有間隔物」，不是「有沒有植入物」[S44][S45]。
- MAUDE 是**自願通報**資料庫：分母（售出套數）不是實際植入數，分子受通報意願影響；三份分析對同一批資料給出「都在 1% 以下」[S49] 與「比臨床試驗報告的更嚴重」[S51] 兩種語氣——**兩種都要出現在文中**。
- Hathout 2025 的作者群含廠商方作者（Rojanasarot、Vannan 等），Millot 2024 與 Fernandez 2024 為學術端分析——**利益關係的差異要在心裡有數，但正文不點名指控，只並陳兩組數字**。
- [S58] 只有 8 人；[S53][S54] 是單一個案報告——證據等級標「個案／小型系列」。
- [S52] 的追蹤只到 15 個月，且是常規分次（79.2 Gy）——不涵蓋 SBRT 與更長期。
- 金標與間隔物的證據**全部集中在攝護腺癌**；其他四個癌別的 A4 內容只能寫「現況」與「還在研究階段」。

### 台灣現況（A4 相關）

- 健保支付標準全表（114-05-01 生效版，6,010 項）逐欄檢索[S59]：
  - 「金標」「標記物」「fiducial」→ **各 0 筆**。
  - 「間隔物」「水膠」「hydrogel」「spacer」→ **各 0 筆**。
  - 「IGRT」「IMRT」→ **各 0 筆**（IMRT 僅以「強度調控放射治療」六字出現在 36015B 的備註文字中，且是**規劃**項目而非治療項目）。
  - 「攝護腺／前列腺」相關術式與處置共 29／20 筆，其中與植入物相關者 **0 筆**；一般性的「19007C 超音波導引（為組織切片，抽吸、注射等）1,500 點」存在，**但無任何公開文件說明 fiducial 置放是否以此申報——不推論，寫成 gap**。
- 台灣端 SpaceOAR 的**核准狀態**：食藥署醫療器材許可證查詢（info.fda.gov.tw）本次 curl 回 502（CONNECT tunnel failed），開放資料端點（data.fda.gov.tw/opendata/exportDataList.do）回傳的是 Swagger UI 外殼而非資料 → **FAIL-6，寫成零筆**。
- **A4 台灣端的唯一可寫法**：「金標的置放、直腸間隔物在健保的診療項目表裡都查不到專屬項目；它們在台灣的核准狀態與收費身分，我查不到可以引用的官方公告。**這一格請直接問該科與醫務課，不要用網路上的價格去推算。**」（符合 SPEC §三固定紅線與 §一4。）

---

## 來源表（PASS／FAIL＋完整書目＋URL）

> 全部經 Europe PMC REST API（https://www.ebi.ac.uk/europepmc/webservices/rest/search，`resultType=core`）於 2026-09-01 逐筆核對；OA／inEPMC 欄位照 API 回傳值標記。台灣端經 curl 實際下載。
> 編號說明：共 59 條，編號連號但**跳過 S37**（原擬給 Nijkamp 2012，該條已編為 [S28]，跨 A2／A3 共用）。撰稿人不會看到 [S37]，這是預期行為。

### A1 適應症

- [S1] **PASS** Zlotta AR, Ballas LK, Niemierko A, et al. Radical cystectomy versus trimodality therapy for muscle-invasive bladder cancer: a multi-institutional propensity score matched and weighted analysis. *Lancet Oncol*. 2023;24(6):669–681. DOI: 10.1016/S1470-2045(23)00170-5. PMID 37187202. https://doi.org/10.1016/S1470-2045(23)00170-5 — Route: Europe PMC REST（DOI 引號查詢，abstract 數字逐一核對）。非 OA。
- [S2] **PASS** James ND, Hussain SA, Hall E, et al.; BC2001 Investigators. Radiotherapy with or without chemotherapy in muscle-invasive bladder cancer. *N Engl J Med*. 2012;366(16):1477–1488. DOI: 10.1056/NEJMoa1106106. PMID 22512481. https://doi.org/10.1056/NEJMoa1106106 — Route: Europe PMC REST（DOI）
- [S3] **PASS（書目＋abstract；完整建議條文不可引，見 FAIL-3）** van der Heijden AG, Bruins HM, Carrion A, et al. European Association of Urology Guidelines on Muscle-invasive and Metastatic Bladder Cancer: Summary of the 2025 Guidelines. *Eur Urol*. 2025;87(5):582–600. DOI: 10.1016/j.eururo.2025.02.019. PMID 40118736. https://doi.org/10.1016/j.eururo.2025.02.019 — Route: Europe PMC REST（TITLE 關鍵字 → DOI 核對）
- [S4] **PASS** Chemoradiotherapy for Cervical Cancer Meta-Analysis Collaboration. Reducing uncertainties about the effects of chemoradiotherapy for cervical cancer: a systematic review and meta-analysis of individual patient data from 18 randomized trials. *J Clin Oncol*. 2008;26(35):5802–5812. DOI: 10.1200/JCO.2008.16.4368. PMID 19001332. PMCID PMC2645100. https://doi.org/10.1200/JCO.2008.16.4368 — Route: Europe PMC REST（DOI）
- [S5] **PASS（書目錨；全文本次取不到，見 FAIL-3）** Cibula D, Raspollini MR, Planchamp F, et al. ESGO/ESTRO/ESP Guidelines for the management of patients with cervical cancer — Update 2023. *Int J Gynecol Cancer*. 2023;33(5):649–666. DOI: 10.1136/ijgc-2023-004429. PMID 37127326. PMCID PMC10176411. https://doi.org/10.1136/ijgc-2023-004429 — Route: Europe PMC REST（DOI）；fullTextXML 請求回傳 0 bytes
- [S6] **PASS** Creutzberg CL, van Putten WL, Koper PC, et al.; PORTEC Study Group. Surgery and postoperative radiotherapy versus surgery alone for patients with stage-1 endometrial carcinoma: multicentre randomised trial. *Lancet*. 2000;355(9213):1404–1411. DOI: 10.1016/S0140-6736(00)02139-5. PMID 10791524. https://doi.org/10.1016/S0140-6736(00)02139-5 — Route: Europe PMC REST（TITLE 全稱 → DOI 核對）
- [S7] **PASS** Nout RA, Smit VT, Putter H, et al.; PORTEC Study Group. Vaginal brachytherapy versus pelvic external beam radiotherapy for patients with endometrial cancer of high-intermediate risk (PORTEC-2): an open-label, non-inferiority, randomised trial. *Lancet*. 2010;375(9717):816–823. DOI: 10.1016/S0140-6736(09)62163-2. PMID 20206777. https://doi.org/10.1016/S0140-6736(09)62163-2 — Route: Europe PMC REST（TITLE 全稱 → DOI 核對）
- [S8] **PASS（OA；PMCID PMC12479390）** Post CCB, de Boer SM, Powell ME, et al. Adjuvant chemoradiotherapy versus radiotherapy alone in women with high-risk endometrial cancer (PORTEC-3): 10-year clinical outcomes and post-hoc analysis by molecular classification from a randomised phase 3 trial. *Lancet Oncol*. 2025;26(10):1370–1381. DOI: 10.1016/S1470-2045(25)00379-1. PMID 40921169. https://doi.org/10.1016/S1470-2045(25)00379-1 — Route: Europe PMC REST（DOI 引號查詢）
- [S9] **PASS（書目錨；逐字條文不可引，見 FAIL-3）** Concin N, Matias-Guiu X, Cibula D, et al. ESGO-ESTRO-ESP guidelines for the management of patients with endometrial carcinoma: update 2025. *Lancet Oncol*. 2025;26(8):e423–e435. DOI: 10.1016/S1470-2045(25)00167-6. PMID 40744042. https://doi.org/10.1016/S1470-2045(25)00167-6 — Route: Europe PMC REST（DOI 引號查詢）
- [S10] **PASS** van Gijn W, Marijnen CA, Nagtegaal ID, et al.; Dutch Colorectal Cancer Group. Preoperative radiotherapy combined with total mesorectal excision for resectable rectal cancer: 12-year follow-up of the multicentre, randomised controlled TME trial. *Lancet Oncol*. 2011;12(6):575–582. DOI: 10.1016/S1470-2045(11)70097-3. PMID 21596621. https://doi.org/10.1016/S1470-2045(11)70097-3 — Route: Europe PMC REST（TITLE 全稱 → DOI 核對）
- [S11] **PASS** Sauer R, Becker H, Hohenberger W, et al.; German Rectal Cancer Study Group. Preoperative versus postoperative chemoradiotherapy for rectal cancer. *N Engl J Med*. 2004;351(17):1731–1740. DOI: 10.1056/NEJMoa040694. PMID 15496622. https://doi.org/10.1056/NEJMoa040694 — Route: Europe PMC REST（DOI）
- [S12] **PASS** Hamdy FC, Donovan JL, Lane JA, et al. Fifteen-Year Outcomes after Monitoring, Surgery, or Radiotherapy for Prostate Cancer. *N Engl J Med*. 2023;388(17):1547–1558. DOI: 10.1056/NEJMoa2214122. PMID 36912538. https://doi.org/10.1056/NEJMoa2214122 — Route: Europe PMC REST（DOI）
- [S13] **PASS（inEPMC；PMCID PMC7611137）** Vale CL, Fisher D, Kneebone A, et al.; ARTISTIC Meta-analysis Group. Adjuvant or early salvage radiotherapy for the treatment of localised and locally advanced prostate cancer: a prospectively planned systematic review and meta-analysis of aggregate data. *Lancet*. 2020;396(10260):1422–1431. DOI: 10.1016/S0140-6736(20)31952-8. PMID 33002431. https://doi.org/10.1016/S0140-6736(20)31952-8 — Route: Europe PMC REST（DOI 引號查詢）

### A3 膀胱與腸道

- [S14] **PASS** Buchali A, Koswig S, Dinges S, et al. Impact of the filling status of the bladder and rectum on their integral dose distribution and the movement of the uterus in the treatment planning of gynaecological cancer. *Radiother Oncol*. 1999;52(1):29–34. DOI: 10.1016/s0167-8140(99)00068-7. PMID 10577683. https://doi.org/10.1016/s0167-8140(99)00068-7 — Route: Europe PMC REST（AUTH＋關鍵字 → DOI 核對）
- [S15] **PASS** Ahmad R, Hoogeman MS, Bondar M, et al. Increasing treatment accuracy for cervical cancer patients using correlations between bladder-filling change and cervix-uterus displacements: proof of principle. *Radiother Oncol*. 2011;98(3):340–346. DOI: 10.1016/j.radonc.2010.11.010. PMID 21295877. https://doi.org/10.1016/j.radonc.2010.11.010 — Route: Europe PMC REST（DOI 引號查詢）
- [S16] **PASS（OA；PMCID PMC8447532）** Li X, Wang L, Cui Z, et al. Online MR evaluation of inter- and intra-fraction uterus motions and bladder volume changes during cervical cancer external beam radiotherapy. *Radiat Oncol*. 2021;16(1):179. DOI: 10.1186/s13014-021-01907-1. PMID 34535161. https://doi.org/10.1186/s13014-021-01907-1 — Route: Europe PMC REST（DOI 引號查詢）
- [S17] **PASS（OA；PMCID PMC13234591）（MESORECT）** Alexandre J, Audrey BL, Camille L, Dominique LD, Valentine G, Emmanuel R, Vincent L. MESORECT: Influence of bladder depletion on mesorectal movements during radiation therapy of locally advanced rectal cancers: a prospective comparative study. *Clin Transl Radiat Oncol*. 2026;59:101194. DOI: 10.1016/j.ctro.2026.101194. PMID 42255982. https://doi.org/10.1016/j.ctro.2026.101194 — Route: Europe PMC REST（關鍵字 → DOI 核對）。**作者欄由 API 回傳為此順序（疑名／姓欄位異常），引用時照抄或僅寫「MESORECT 研究」**
- [S18] **PASS（OA；PMCID PMC11264890）** Guel DNB, Laverick N, MacLaren L, et al. Adaptive radiotherapy for muscle invasive bladder cancer: a retrospective audit of two bladder filling protocols. *Radiat Oncol*. 2024;19(1):92. DOI: 10.1186/s13014-024-02484-9. PMID 39030548. https://doi.org/10.1186/s13014-024-02484-9 — Route: Europe PMC REST（DOI 引號查詢，abstract 數字逐一核對）
- [S19] **PASS（僅 abstract 層級；全文非 OA）** Khalifa J, Supiot S, Pignot G, et al. Recommendations for planning and delivery of radical radiotherapy for localized urothelial carcinoma of the bladder. *Radiother Oncol*. 2021;161:95–114. DOI: 10.1016/j.radonc.2021.06.011. PMID 34118357. https://doi.org/10.1016/j.radonc.2021.06.011 — Route: Europe PMC REST（DOI 引號查詢）。可引之逐字僅限 abstract 中「The group did not obtain an agreement on…PTV margins definition for empty bladder and full bladder protocols」
- [S20] **PASS（OA；PMCID PMC13047064；回溯世代）** Wu Y, Xue X, Su L, Liu Y. Effect of bladder volume on dose of exposure to dangerous organs and incidence of cystitis and enteritis in patients with cervical cancer after external radiotherapy. *Front Oncol*. 2026;16:1760076. DOI: 10.3389/fonc.2026.1760076. PMID 41939472. https://doi.org/10.3389/fonc.2026.1760076 — Route: Europe PMC REST（DOI 引號查詢）
- [S21] **PASS（OA；PMCID PMC12226321；回溯世代）** Wang Y, Wang M, Zhu L. The impact of bladder volume on dosimetric outcomes in VMAT for cervical cancer patients after surgery. *J Gynecol Oncol*. 2025;36(4):e65. DOI: 10.3802/jgo.2025.36.e65. PMID 40223551. https://doi.org/10.3802/jgo.2025.36.e65 — Route: Europe PMC REST（DOI 引號查詢）
- [S22] **PASS（OA；PMCID PMC4454439）** Yoon HI, Chung Y, Chang JS, Lee JY, Park SJ, Koom WS. Evaluating Variations of Bladder Volume Using an Ultrasound Scanner in Rectal Cancer Patients during Chemoradiation: Is Protocol-Based Full Bladder Maintenance Using a Bladder Scanner Useful to Maintain the Bladder Volume? *PLoS One*. 2015;10(6):e0128791. DOI: 10.1371/journal.pone.0128791. PMID 26039198. https://doi.org/10.1371/journal.pone.0128791 — Route: Europe PMC REST（DOI 引號查詢）
- [S23] **PASS（OA；PMCID PMC8992960）** Ohira S, Komiyama R, Kanayama N, et al. Improvement in bladder volume reproducibility using A-mode portable ultrasound bladder scanner in moderate-hypofractionated volumetric modulated arc therapy for prostate cancer patients. *J Appl Clin Med Phys*. 2022;23(4):e13546. DOI: 10.1002/acm2.13546. PMID 35112479. https://doi.org/10.1002/acm2.13546 — Route: Europe PMC REST（DOI 引號查詢）
- [S24] **PASS（OA；PMCID PMC10963561）** Bai F, Hu Q, Yao X, Cheng M, Zhao L, Xu L. A prospective comparative study on bladder volume measurement with portable ultrasound scanner and CT simulator in pelvic tumor radiotherapy. *Phys Eng Sci Med*. 2024;47(1):87–97. DOI: 10.1007/s13246-023-01344-2. PMID 38019446. https://doi.org/10.1007/s13246-023-01344-2 — Route: Europe PMC REST（DOI 引號查詢）
- [S25] **PASS（OA；PMCID PMC13202308）** Shimada C, Ishii K, Koorita Y, et al. Ensuring bladder volume reproducibility and reducing cone-beam computed tomography-related radiation exposure in prostate hypofractionated radiotherapy by a Certified Nurse in Radiation Oncology nursing. *J Radiat Res*. 2026;67(3):395–401. DOI: 10.1093/jrr/rrag015. PMID 41853985. https://doi.org/10.1093/jrr/rrag015 — Route: Europe PMC REST（DOI 引號查詢）
- [S26] **PASS（OA；PMCID PMC7565753）** Byun DJ, Gorovets DJ, Jacobs LM, et al. Strict bladder filling and rectal emptying during prostate SBRT: Does it make a dosimetric or clinical difference? *Radiat Oncol*. 2020;15(1):239. DOI: 10.1186/s13014-020-01681-6. PMID 33066781. https://doi.org/10.1186/s13014-020-01681-6 — Route: Europe PMC REST（DOI 引號查詢）
- [S27] **PASS（OA；PMCID PMC12546546；n=8，極小樣本）** Varga L, Gáldi Á, Szegedi D, et al. Reduction of the planning target volume with daily online adaptive radiotherapy in bladder cancer. *Strahlenther Onkol*. 2025;201(11):1162–1169. DOI: 10.1007/s00066-025-02397-w. PMID 40232382. https://doi.org/10.1007/s00066-025-02397-w — Route: Europe PMC REST（關鍵字 → DOI 核對）
- [S28] **PASS（志願者計畫研究，非病人）** Nijkamp J, Doodeman B, Marijnen C, Vincent A, van Vliet-Vroegindeweij C. Bowel exposure in rectal cancer IMRT using prone, supine, or a belly board. *Radiother Oncol*. 2012;102(1):22–29. DOI: 10.1016/j.radonc.2011.05.076. PMID 21723637. https://doi.org/10.1016/j.radonc.2011.05.076 — Route: Europe PMC REST（DOI 引號查詢）
- [S29] **PASS（1990s–2000s 3D-CRT、無每日 IGRT——族群標籤不可省）** de Crevoisier R, Tucker SL, Dong L, et al. Increased risk of biochemical and local failure in patients with distended rectum on the planning CT for prostate cancer radiotherapy. *Int J Radiat Oncol Biol Phys*. 2005;62(4):965–973. DOI: 10.1016/j.ijrobp.2004.11.032. PMID 15989996. https://doi.org/10.1016/j.ijrobp.2004.11.032 — Route: Europe PMC REST（AUTH＋關鍵字 → DOI 核對）
- [S30] **PASS（OA；PMCID PMC10570575）** Alexander SE, Oelfke U, Westley R, McNair HA, Tree AC. Prostate cancer image guided radiotherapy: Why the commotion over rectal volume and motion? *Clin Transl Radiat Oncol*. 2023;43:100685. DOI: 10.1016/j.ctro.2023.100685. PMID 37842073. https://doi.org/10.1016/j.ctro.2023.100685 — Route: Europe PMC REST（DOI 引號查詢）
- [S31] **PASS（OA；PMCID PMC13276509）** Alexander SE, Booth L, Delacroix L, et al. Is rectal preparation necessary in contemporary image-guided prostate radiotherapy? *Clin Transl Radiat Oncol*. 2026;60:101207. DOI: 10.1016/j.ctro.2026.101207. PMID 42327916. https://doi.org/10.1016/j.ctro.2026.101207 — Route: Europe PMC REST（DOI 引號查詢，abstract 數字逐一核對）
- [S32] **PASS（僅 abstract；全文非 OA）** McNair HA, Wedlake L, Lips IM, Andreyev J, Van Vulpen M, Dearnaley D. A systematic review: effectiveness of rectal emptying preparation in prostate cancer patients. *Pract Radiat Oncol*. 2014;4(6):437–447. DOI: 10.1016/j.prro.2014.06.005. PMID 25407867. https://doi.org/10.1016/j.prro.2014.06.005 — Route: Europe PMC REST（DOI 引號查詢）。逐字可引：「There is no robust evidence to recommend one rectal emptying strategy over another.」
- [S33] **PASS（隨機試驗，n=30；非 OA）** Ward J, Gill S, Armstrong K, et al. Randomised controlled trial on the effect of simethicone bowel preparation on rectal variability during image-guided radiation therapy for prostate cancer (SPoRT study). *J Med Imaging Radiat Oncol*. 2022;66(6):866–873. DOI: 10.1111/1754-9485.13404. PMID 35322563. https://doi.org/10.1111/1754-9485.13404 — Route: Europe PMC REST（DOI 引號查詢）
- [S34] **PASS（OA；PMCID PMC11969104）** Serra LM, Wu T, Korpics MC, Yenice K, Liauw SL. Online correction of intrafraction motion during volumetric modulated arc therapy for prostate radiotherapy using fiducial-based kV imaging: A cohort study quantifying the frequency of shifts and analysis of men at highest risk. *J Appl Clin Med Phys*. 2025;26(4):e14603. DOI: 10.1002/acm2.14603. PMID 39824507. https://doi.org/10.1002/acm2.14603 — Route: Europe PMC REST（DOI 引號查詢）
- [S60] **PASS（OA；PMCID PMC12885748；近接治療情境，A3 只能一句話帶）** Wu H, He C, Liu M, Zhao X. Impact of rectal gas evacuation on dosimetry and applicator displacement in cervical cancer brachytherapy. *J Appl Clin Med Phys*. 2026;27(2):e70490. DOI: 10.1002/acm2.70490. PMID 41663311. https://doi.org/10.1002/acm2.70490 — Route: Europe PMC REST（關鍵字 → DOI 核對）

### A2 定位

- [S35] **PASS（OA；PMCID PMC11638372；n=16 回溯）** Prasad S, Bell LJ, Zwan B, et al. Comparing immobilisation devices in gynaecological external beam radiotherapy: improving inter-fraction reproducibility of pelvic tilt. *J Med Radiat Sci*. 2024;71(4):529–539. DOI: 10.1002/jmrs.804. PMID 38894671. https://doi.org/10.1002/jmrs.804 — Route: Europe PMC REST（DOI 引號查詢）
- [S36] **PASS（僅 abstract；全文非 OA）** Wiesendanger-Wittmer EM, Sijtsema NM, Muijs CT, Beukema JC. Systematic review of the role of a belly board device in radiotherapy delivery in patients with pelvic malignancies. *Radiother Oncol*. 2012;102(3):325–334. DOI: 10.1016/j.radonc.2012.02.004. PMID 22364650. https://doi.org/10.1016/j.radonc.2012.02.004 — Route: Europe PMC REST（DOI 引號查詢）
- [S38] **PASS（OA；PMCID PMC12974187）** Mantello G, Galofaro E, Gani C, et al. Setup and target volume shape variation in rectal cancer radiotherapy: a systematic literature review. *Tech Innov Patient Support Radiat Oncol*. 2026;37:100359. DOI: 10.1016/j.tipsro.2025.100359. PMID 41815276. https://doi.org/10.1016/j.tipsro.2025.100359 — Route: Europe PMC REST（DOI 引號查詢）
- [S39] **PASS（OA；PMCID PMC12585954；傾向分數配對之回溯世代）** Xiao N, Yuan C, Zhao T, et al. Comparative impact of supine vs prone positioning on dose distribution, acute toxicity, and setup error in postoperative radiotherapy for cervical cancer: a multidimensional propensity-matched cohort study. *Front Oncol*. 2025;15:1637443. DOI: 10.3389/fonc.2025.1637443. PMID 41199826. https://doi.org/10.3389/fonc.2025.1637443 — Route: Europe PMC REST（關鍵字 → DOI 核對）
- [S40] **PASS（僅 abstract；全文非 OA；族群以乳癌為主）** Lastrucci A, Marrazzo L, Meattini I, et al. Advancing patient setup: A comprehensive scoping review of tattoo-less techniques in radiation therapy. *Crit Rev Oncol Hematol*. 2024;204:104518. DOI: 10.1016/j.critrevonc.2024.104518. PMID 39299409. https://doi.org/10.1016/j.critrevonc.2024.104518 — Route: Europe PMC REST（DOI 引號查詢）

### A4 植入物

- [S41] **PASS（OA；PMCID PMC10262562）** Mahdavi A, Mofid B, Taghizadeh-Hesary F. Intra-prostatic gold fiducial marker insertion for image-guided radiotherapy (IGRT): five-year experience on 795 patients. *BMC Med Imaging*. 2023;23(1):79. DOI: 10.1186/s12880-023-01036-z. PMID 37308834. https://doi.org/10.1186/s12880-023-01036-z — Route: Europe PMC REST（DOI 引號查詢）
- [S42] **PASS（OA；PMCID PMC11222131）** Hong SS, Bae SH, Hwang J, Lee EJ. Transperineal versus transrectal prostate fiducial insertion in radiation treatment of prostate cancer: a systematic review and meta-analysis. *Ultrasonography*. 2024;43(4):229–237. DOI: 10.14366/usg.23229. PMID 38898635. https://doi.org/10.14366/usg.23229 — Route: Europe PMC REST（DOI 引號查詢）
- [S43] **PASS（族群為經皮肺／胰／肝，不可挪用為攝護腺數字；沿用 liver brief S2，本日重新核對）** Kothary N, Heit JJ, Louie JD, et al. Safety and efficacy of percutaneous fiducial marker implantation for image-guided radiation therapy. *J Vasc Interv Radiol*. 2009;20(2):235–239. DOI: 10.1016/j.jvir.2008.09.026. PMID 19019700. https://doi.org/10.1016/j.jvir.2008.09.026 — Route: Europe PMC REST（DOI 引號查詢）
- [S44] **PASS（樞紐 RCT；廠商贊助；非 OA）** Mariados N, Sylvester J, Shah D, et al. Hydrogel Spacer Prospective Multicenter Randomized Controlled Pivotal Trial: Dosimetric and Clinical Effects of Perirectal Spacer Application in Men Undergoing Prostate Image Guided Intensity Modulated Radiation Therapy. *Int J Radiat Oncol Biol Phys*. 2015;92(5):971–977. DOI: 10.1016/j.ijrobp.2015.04.030. PMID 26054865. https://doi.org/10.1016/j.ijrobp.2015.04.030 — Route: Europe PMC REST（DOI 引號查詢）
- [S45] **PASS（同一試驗之 3 年最終結果）** Hamstra DA, Mariados N, Sylvester J, et al. Continued Benefit to Rectal Separation for Prostate Radiation Therapy: Final Results of a Phase III Trial. *Int J Radiat Oncol Biol Phys*. 2017;97(5):976–985. DOI: 10.1016/j.ijrobp.2016.12.024. PMID 28209443. https://doi.org/10.1016/j.ijrobp.2016.12.024 — Route: Europe PMC REST（DOI 引號查詢）
- [S46] **PASS（同一試驗之次級分析）** Quinn TJ, Daignault-Newton S, Bosch W, et al. Who Benefits From a Prostate Rectal Spacer? Secondary Analysis of a Phase III Trial. *Pract Radiat Oncol*. 2020;10(3):186–194. DOI: 10.1016/j.prro.2019.12.011. PMID 31978591. https://doi.org/10.1016/j.prro.2019.12.011 — Route: Europe PMC REST（DOI 引號查詢）
- [S47] **PASS（OA；PMCID PMC13036257）** Kwon JK, Jeon J, Bang S, Koo KC, Cho KS, Kim DK. Association of Perirectal Hydrogel Spacer Placement with Clinical Outcomes in Patients with Prostate Cancer Undergoing Radiotherapy: A Systematic Review and Meta-Analysis. *World J Mens Health*. 2026;44(2):301–321. DOI: 10.5534/wjmh.250043. PMID 40676889. https://doi.org/10.5534/wjmh.250043 — Route: Europe PMC REST（DOI 引號查詢）
- [S48] **PASS（非 OA）** Wong CH, Ko IC, Leung DK, et al. Does biodegradable peri-rectal spacer mitigate treatment toxicities in radiation therapy for localised prostate cancer—a systematic review and meta-analysis. *Prostate Cancer Prostatic Dis*. 2025;28(4):927–937. DOI: 10.1038/s41391-025-00961-0. PMID 40148672. https://doi.org/10.1038/s41391-025-00961-0 — Route: Europe PMC REST（DOI 引號查詢）
- [S49] **PASS（OA；PMCID PMC12661999；作者群含廠商方）** Hathout L, Shin YE, Rojanasarot S, Ezekekwu E, Vannan D, Folkert MR. Real-World Medical Device Reports of SpaceOAR Hydrogel Spacer: Analysis of the Food and Drug Administration Manufacturer and User Facility Device Experience (MAUDE) Database. *Adv Radiat Oncol*. 2025;10(12):101824. DOI: 10.1016/j.adro.2025.101824. PMID 41321862. https://doi.org/10.1016/j.adro.2025.101824 — Route: Europe PMC REST（DOI 引號查詢）
- [S50] **PASS（非 OA）** Fernandez AM, Jones CP, Patel HV, et al. Real-World Complications of the SpaceOAR Hydrogel Spacer: A Review of the Manufacturer and User Facility Device Experience Database. *Urology*. 2024;183:157–162. DOI: 10.1016/j.urology.2023.09.016. PMID 37774851. https://doi.org/10.1016/j.urology.2023.09.016 — Route: Europe PMC REST（DOI 引號查詢）
- [S51] **PASS（非 OA）** Millot JC, Arenas-Gallo C, Silver E, et al. Major Complications and Adverse Events Related to Use of SpaceOAR Hydrogel for Prostate Cancer Radiotherapy. *Urology*. 2024;188:94–100. DOI: 10.1016/j.urology.2023.12.034. PMID 38458325. https://doi.org/10.1016/j.urology.2023.12.034 — Route: Europe PMC REST（DOI 引號查詢）
- [S52] **PASS（OA；PMCID PMC11602978；樞紐 RCT 之影像次分析）** Grossman CE, Akin O, Damato AL, Nunez DA, Zelefsky MJ. Depth of Hydrogel Spacer Rectal Wall Infiltration Was Not Associated With Rectal Toxicity: Results From a Randomized Prospective Trial. *Adv Radiat Oncol*. 2024;9(12):101624. DOI: 10.1016/j.adro.2024.101624. PMID 39610659. https://doi.org/10.1016/j.adro.2024.101624 — Route: Europe PMC REST（DOI 引號查詢）
- [S53] **PASS（OA；PMCID PMC11550147；個案報告）** Nesi L, Gogia P, Navalpakam A, Vaishampayan N, Maitland C. Anaphylactic shock during SpaceOAR Vue hydrogel procedure. *Urol Case Rep*. 2024;57:102870. DOI: 10.1016/j.eucr.2024.102870. PMID 39525407. https://doi.org/10.1016/j.eucr.2024.102870 — Route: Europe PMC REST（關鍵字 → DOI 核對）
- [S54] **PASS（OA；PMCID PMC12206518；個案報告）** Markey GE, Razdan P, Jaipalli S, Rozzell DM. Acute Prostatitis and Septic Shock Following Rectal Spacer Placement: A Case Report of a Pre-brachytherapy Complication. *Cureus*. 2025;17(5):e85099. DOI: 10.7759/cureus.85099. PMID 40585687. https://doi.org/10.7759/cureus.85099 — Route: Europe PMC REST（關鍵字 → DOI 核對）
- [S55] **PASS（OA；PMCID PMC8977855；n=15 前瞻試驗）** Greer MD, Schaub SK, Bowen SR, et al. A Prospective Study of a Resorbable Intravesical Fiducial Marker for Bladder Cancer Radiation Therapy. *Adv Radiat Oncol*. 2022;7(2):100858. DOI: 10.1016/j.adro.2021.100858. PMID 35387424. https://doi.org/10.1016/j.adro.2021.100858 — Route: Europe PMC REST（DOI 引號查詢）
- [S56] **PASS（OA；PMCID PMC12387298；n=6 單中心初步經驗）** Titone F, Moretti E, Poli A, et al. Single-Center Preliminary Experience Treating Endometrial Cancer Patients with Fiducial Markers. *Life (Basel)*. 2025;15(8):1218. DOI: 10.3390/life15081218. PMID 40868866. https://doi.org/10.3390/life15081218 — Route: Europe PMC REST（DOI 引號查詢）
- [S57] **PASS（OA；PMCID PMC6805181；n=20 可行性研究）** Rigter LS, Rijkmans EC, Inderson A, et al. EUS-guided fiducial marker placement for radiotherapy in rectal cancer: feasibility of two placement strategies and four fiducial types. *Endosc Int Open*. 2019;7(11):E1357–E1364. DOI: 10.1055/a-0958-2148. PMID 31673605. https://doi.org/10.1055/a-0958-2148 — Route: Europe PMC REST（DOI 引號查詢）
- [S58] **PASS（OA；PMCID PMC12041414；n=8 連續病例系列）** Yates AH, Dempsey PJ, Power JW, et al. Rectal complications following SpaceOAR insertion after prior pelvic radiation. *BJR Case Rep*. 2025;11(2):uaaf013. DOI: 10.1093/bjrcr/uaaf013. PMID 40309031. https://doi.org/10.1093/bjrcr/uaaf013 — Route: Europe PMC REST（DOI 引號查詢）

### 台灣官方文件

- [S59] **PASS（2026-09-01 實際下載並逐項解析；curl HTTP 200，565,406 bytes，content-type application/ods；解析後 6,010 項；欄位「生效起日」最新值 2025-05-01，即 114-05-01 生效版）** 【機構型來源，無作者欄】衛生福利部中央健康保險署。《全民健康保險醫療服務給付項目及支付標準》開放資料全表。經逐欄檢索確認：
  - **36024B「直腸癌術前低分次放射治療」204,966 點，2023-07-01 生效**；適應症與支付規範原文（含「療程次數五次」「每人終生限給付一次」「手術後復發之病人如須再次salvage骨盆腔放射治療，不得執行本項」）見 ⚠6。
  - **36021C「3D電腦斷層模擬攝影」8,500 點**（備註原文：「1.適應症：放射治療前所實施之必要檢查及治療設計。2.含電腦斷層攝影費用。」）；**36018B「模擬定位攝影」3,619 點**；**36019B「劑量計算」301 點**；**36001B「電腦治療規劃--簡單」3,309 點**；**36015B「電腦治療規劃--複雜」11,483 點**（備註原文含「強度調控放射治療」）。
  - **37016B「固定模具之設計及製作（大）」1,943 點**（備註原文：「1.胸腔、腹腔、骨盆腔及四肢使用。2.包括技術費及材料費在內。」）；**37030B（小）1,657 點**（頭、頸部）。
  - **36011B/36012B/36013B 直線加速器遠隔照射治療（簡單／複雜／緊急照野）1,231／1,334／1,601 點**；**37047B 身體立體定位放射治療 213,662 點**（適應症限肺與肝膽，骨盆腔不在內）；**36022B/36023B 乳癌低分次包裹碼**；**78008C 膀胱腫瘤之切除－內視鏡下--含膀胱鏡檢 8,027 點**。
  - **零筆確認**：「金標」「標記物」「fiducial」「間隔物」「水膠」「hydrogel」「spacer」「IGRT」「IMRT」「重粒子」「斷層放射」全表各 0 筆；「影像導引」全表 9 筆中放射治療章節僅 37029B 加馬機立體定位放射手術；質子相關僅 N21301–N21308 八項，全部點數 0。
  資料集頁：https://data.gov.tw/dataset/9405 ；檔案：https://info.nhi.gov.tw/api/iode0000s01/Dataset?rId=A21030000I-D20003-004 — Route: curl 下載 ODS → python odfpy 解析 6,010 列 → 逐欄字串檢索

---

## FAIL 清單（含「這個洞怎麼寫」）

- **FAIL-1 — 「定位到第一次治療隔幾天」。** 檢索紀錄：Europe PMC `"time from simulation to" AND "first radiotherapy fraction" AND days` → **hitCount 0**；`interval between CT simulation and start of radiotherapy days pelvic` → 761 筆，逐筆檢視前列無任何以此為終點者。與 `liver/brief-C.md` FAIL-1 結論一致。**怎麼寫**：A2 只寫「定位之後要做計畫設計與品質驗證，這段時間各院不同，你的個管師會告訴你哪一天開始」——**不帶任何天數**。
- **FAIL-2 — 「單次治療躺在治療床上幾分鐘」。** 檢索紀錄：`TITLE:"treatment time" AND (VMAT OR IMRT) AND pelvic AND minutes` → 5 筆，皆為特殊流程（MR-Linac 工作流程、單次 SABR、直腸氣球等）。與 `liver/brief-C.md` FAIL-2 一致。**怎麼寫**：寫質性描述——「擺位比照射久、照射本身不痛、可以隨時舉手」。**不可挪用 [S27] 的 14.8 分鐘或 [S16] 的 24–28 分鐘充當一般值**；若真要用，必須整句帶標籤（「在膀胱癌用線上適應性放療的一份 8 人研究裡……」）。
- **FAIL-3 — 三份指引（EAU 2025 MIBC、ESGO/ESTRO/ESP 子宮頸 2023、ESGO-ESTRO-ESP 子宮內膜 2025）的逐字建議條文。** EAU 與 ESGO 子宮內膜為非 OA（Eur Urol／Lancet Oncol）；ESGO 子宮頸 2023 雖標 OA、PMCID PMC10176411，但 fullTextXML 請求回傳 **0 bytes**。**怎麼寫**：三者一律當書目錨，只寫「歐洲泌尿科學會／歐洲婦癌與放腫學會的指引同此方向」，**不加引號、不寫「指引建議」的具體措辭**；A1 的證據主體改用試驗與統合（[S1][S2][S4][S6][S7][S8][S10][S11][S12][S13]）。
- **FAIL-4 — 喝水方案（drinking protocol）本身的隨機證據。** 檢索紀錄：`TITLE:"drinking protocol" AND radiotherapy` → **hitCount 0**。可得的最高等級只到「有無方案化管理」的對照研究（[S22]，主要比較未達顯著 p=0.058）與流程描述（[S16]）。**怎麼寫**：A3 一律「照你醫院給的方案做」，**不寫任何 mL 數與時間點**；唯一可帶的具體數字是 [S20][S21] 的 300–500 mL 甜蜜點，且必須整句帶「子宮頸癌、單中心回溯」標籤。
- **FAIL-5 — 子宮頸癌 fiducial 的置放併發症與成效系列。** 檢索紀錄：`fiducial markers cervical cancer image-guided radiotherapy implantation` → 147 筆，前列皆為 MRI 標記線、近接施體、裝置開發或非婦癌主題；無可引之臨床系列。**怎麼寫**：A4 寫「子宮頸癌方面，我沒有找到可以引用的臨床系列」，或直接不提子宮頸癌那一格，改列膀胱癌[S55]、子宮內膜癌[S56]、直腸癌[S57] 三格。
- **FAIL-6 — SpaceOAR／直腸間隔物在台灣的核准狀態與收費身分；fiducial 置放在台灣的給付身分。** 檢索紀錄：(a) 健保支付標準全表 6,010 項逐欄檢索，「間隔物」「水膠」「hydrogel」「spacer」「金標」「fiducial」**各 0 筆**[S59]；(b) 食藥署醫療器材許可證查詢 info.fda.gov.tw/MLMS/H0001.aspx → curl **502（CONNECT tunnel failed）**；(c) data.fda.gov.tw/opendata/exportDataList.do?method=openData&InfoId=36 → HTTP 200 但回傳 734 bytes 的 Swagger UI 外殼，非資料。**怎麼寫**：「健保的診療項目表裡查不到金標置放與直腸間隔物的專屬項目；它們在台灣的核准與收費身分，我查不到可以引用的官方公告。請直接向該科與醫務課確認，**不要用網路上流傳的價格去推算**。」（符合 SPEC §一4、§三固定紅線。）
- **FAIL-7 — 骨盆腔 IGRT（影像導引）在健保是否有獨立給付項目。** 檢索紀錄：全表「IGRT」「影像導引」「影像導航」「導航」→ 放射治療章節 0 筆（「影像導引」9 筆全在插管、乳房穿刺、脊椎／腦機械手臂與 37029B）[S59]。**怎麼寫**：「影像導引在健保的診療項目表裡沒有自己的代碼」是可寫的事實陳述；**不可推論成「所以不用錢」或「所以要自費」**——寫「這一格請問醫務課」。（此條與 `brt/brief-B.md` S38 的結論一致，本日重新驗證仍成立；正式歸屬 B 組，本 brief 只作交接。）
- **FAIL-8 — NCCN 指引。** 依任務指示不引（專業版 403）。**怎麼寫**：全文任何地方不出現「NCCN 建議」；指引錨一律用 EAU／ESGO／ESTRO／ESP 書目替代。

---

## 「數字形狀的洞」清單（撰稿人請直接視為禁區）

> 以下每一格都是「讀者會問、文章結構會想放一個數字、但目前沒有可引來源」的位置。**一律寫成質性描述或明白的『我查不到』，不得由臨近數字推算或改寫。**

| # | 洞的位置 | 讀者會問的問題 | 目前可得的最接近物（**不可當答案用**） | 撰稿人該怎麼填 |
|---|---|---|---|---|
| 1 | A2 開場 | 「定位完幾天開始照？」 | 無（FAIL-1） | 「各院不同，個管師會告訴你」——不帶天數 |
| 2 | A2 流程 | 「一次治療要躺多久？」 | [S27] 14.8 分（膀胱癌線上適應）、[S16] 24–28 分（子宮頸癌前後 MRI 之間） | 質性：「擺位比照射久」；若用數字必須整句帶流程標籤 |
| 3 | A2 流程 | 「定位那一天總共要待多久？」 | 無 | 不寫 |
| 4 | A2 標記 | 「要點幾個刺青點？會不會洗掉？」 | 無（[S40] 只到「替代方案存在」且以乳癌為主） | 「以你醫院的說明為準」 |
| 5 | A3 喝水 | 「要喝幾 c.c.？提前多久喝？」 | [S16] 流程描述「治療前 1 小時喝 500 mL」（單一研究的流程，非建議） | **絕對不寫數字**；只寫「照你醫院的方案」。若要給範圍，只能引 [S20][S21] 的 300–500 mL 並標「子宮頸癌、單中心回溯、是模擬時的膀胱容積不是喝水量」 |
| 6 | A3 憋尿 | 「憋不住的話可以撐多久？」 | 無 | 「憋不住就說，不要硬撐」——紅線 2(a)，寫成行為指引不是時間指引 |
| 7 | A3 腸道 | 「甘油球要提前多久用？多少人需要用？」 | 無（[S31] 只給「灌腸把大直腸比例壓低 10–15 個百分點」） | 「用不用、怎麼用照醫囑」；可寫 10–15 個百分點但要標「攝護腺癌、現代 IGRT」 |
| 8 | A3 腸道 | 「排氣藥有效嗎？」 | [S33] SPoRT：整體無效（陰性隨機結果） | **可以寫「唯一的隨機試驗沒有做出效果」**——這不是洞，是可引的陰性結果，要寫 |
| 9 | A3 微調 | 「療程中大概第幾週會被要求改準備方式？」 | 無（只知道膀胱體積在療程中系統性變小[S18][S26]） | 「後段會變得比較裝不住，這是常態」——不寫週數 |
| 10 | A4 金標 | 「放金標要幾分鐘？痛不痛？」 | 無攝護腺資料（liver brief 的 14.3 分鐘是**肝臟 CyberKnife** 的置放時間，不可挪用） | 質性描述；不帶分鐘數 |
| 11 | A4 金標 | 「金標會不會掉？」 | [S41] 攝護腺：795 人中 2 人短期移位、療程中 0；[S57] 直腸：17 天後僅 66% 在位 | **兩個數字都可寫，但器官標籤絕不可混** |
| 12 | A4 間隔物 | 「台灣做一次多少錢？」 | 無（FAIL-6） | 「問該科與醫務課」——**媒體價格一律不引**（SPEC 固定紅線） |
| 13 | A4 間隔物 | 「台灣有沒有核准？」 | 無（FAIL-6，食藥署查詢 502） | 「我查不到可以引用的官方公告」 |
| 14 | A4 間隔物 | 「多少人做了會出事？」 | MAUDE 通報率 0.40%[S49]／通報案中 grade ≥3 佔 13.1%[S51] | **兩個都要寫，並說明「這是通報資料庫，分母是售出套數不是實際植入數」**——不可只寫其中一個 |
| 15 | A4 間隔物 | 「哪些人不適合？」 | 只有「曾照過骨盆腔」有具名證據（8 人中 2 人嚴重併發症[S58]） | 只寫這一格＋「它只有攝護腺癌的隨機證據」＋「不是本科項目」；**不可自行列出其他禁忌症** |
| 16 | A1 各格 | 「五年存活率是多少？」 | 各試驗有各自的數字，但族群邊界完全不同 | A1 是一句話級地圖，**只用本 brief 已列的、帶族群標籤的數字**；不做跨癌別存活率並列 |
| 17 | 全篇 | 「骨盆腔放療的總療程幾週？」 | 屬 cx-pelvic-rt-weeks 主場 | 指路，不重寫（SPEC §五） |
| 18 | A3／A4 | 「健保有沒有給付 IGRT／膀胱超音波／衛教指導？」 | 全表 0 筆（FAIL-7） | 「診療項目表裡沒有這些代碼」是事實；**不可推論費用方向** |

---

## 給 SPEC 的修正建議（查證結果與 SPEC 假設不符處，逐條）

1. **§一2（全專題最重要的框架）建議升級為「有數字撐著的技術事實」，而不只是編輯立場。** 目前 SPEC 寫「有的計畫要滿、有的要空（全膀胱照射常要空）」；查證結果是這句話兩邊都有可引來源，而且**空膀胱那一邊的證據比預期硬**（[S18] 的對照稽核＋[S19] 專家共識明講「滿／空兩種流程的 PTV 邊界至今未達共識」）。建議 §一2 加註「A3 必須把 [S17] 的 SD 164 vs 58 cm³ 這組對照寫進去——它是『憋出來的體積本身最不可複製』的直接證據」。

2. **§三紅線 2(b)「憋過頭同樣會壞事」建議從『不適與擺位變差』升級為『有臨床終點的劑量與毒性代價』。** 現行 SPEC 的理由是主觀感受與擺位；查證找到兩筆帶臨床終點的回溯資料（[S20][S21]）：>500 mL 那一格直腸與乙狀結腸劑量最高、晚期直腸炎最多。建議紅線 2(b) 明文要求文中出現「300–500 mL 是甜蜜點，低於與高於各自付出不同的代價」這個雙向結構（並帶「子宮頸癌、單中心回溯」標籤）。

3. **§四 A3 的內容清單建議新增一項：「排空直腸的要求正在被鬆綁」。** 現行清單有「排便與脹氣準備」，但沒有反映 [S30][S31] 這條「現代 IGRT 下不再普遍需要腸道準備」的證據轉折。這一條對紅線 2 極重要——**若只寫「要排空」，會讓做不到的病人承受不必要的自責**，正好違反紅線 2 的立意。建議 SPEC §四 A3 加一格：「排空要求的歷史來源與它現在的鬆綁」。

4. **§六圖 1 `fig-pel-bladder-repro` 的資料本體已備齊，建議在 SPEC 註明來源編號。** 「滿膀胱與空膀胱兩種計畫並陳」那一格的數字：滿 243±164 cm³ vs 空 73±58 cm³[S17]；「不可畫成憋越多越好」那一格：300–500 mL 甜蜜點與 >500 mL 的直腸代價[S20][S21]；「同一個膀胱如何推動子宮與腸」那一格：子宮體位移中位 7 mm（95% CI 3–15）[S14]、子宮底平均 3D 位移 26.1 mm[S15]、膀胱每多 100 cc 腸道 V15 −16%[S28]。

5. **【跨專題修正】`brt/brief-A.md` FAIL-4 與 `brt/brief-B.md` 對 36024B 的推測需更正。** 兩份 brief 依 2025 年問答集的「20/16/5 次」推測 36024B 屬乳癌低分次系列；本次直接解析健保全表確認 **36024B 是「直腸癌術前低分次放射治療」（204,966 點，2023-07-01 生效，五次包裹，每人終生一次）**[S59]。建議：(a) 本專題 A1 直腸癌那一格直接使用；(b) 若 brt 專題尚未出版，回頭修正其 FAIL-4 的敘述；若已出版，列入 FIXES。

6. **§七台灣端查證清單的三條結果回報**：(a) 「IGRT 有無獨立項目」→ **零筆確認**（FAIL-7），這一條可以從「待查」改成「已確認為零，寫成事實不推論費用」；(b) 「SpaceOAR 在台灣的核准與收費身分」→ **零筆，且食藥署查詢管道本日不可用**（FAIL-6），建議 SPEC 直接寫死「A4 此格一律導向醫務課」；(c) 「fiducial 置放的給付」→ **零筆**，同上。另補一條 §七未列但查到的正面事實：**骨盆腔的固定模具（37016B，1,943 點）與 3D 電腦斷層模擬攝影（36021C，8,500 點）在健保都有專屬項目且材料費內含**——這對 A2 的費用安全閥很有用，建議加入 §七清單。

7. **A4 的證據形狀建議在 SPEC §一4 補一句。** 現行 §一4 寫「SpaceOAR 不是本科提供的項目……fiducial 視病情」，方向正確；但查證顯示兩者的**證據等級剛好相反**（fiducial 無隨機證據但有大樣本安全數字與量化貢獻；間隔物有隨機證據但嚴重毒性那一格兩份統合都說沒差[S47][S48]）。建議 §一4 加註：「A4 必須寫出『間隔物在嚴重副作用那一格，統合分析是沒有差別的』——這句是紅線 3『不可寫成人人該做』的證據本體。」

8. **A2 的姿勢段建議 SPEC 調整措辭。** §四 A2 現寫「俯臥 vs 仰臥（belly board 對小腸劑量的證據）」，暗示 belly board 較優；查證顯示這是**劑量學較優、臨床終點未證實**（[S36] 原文用 might），且擺位精準度在直腸癌系統性回顧中反而**偏向仰臥**[S38]，在子宮頸癌術後配對世代中兩種姿勢**各有各的代價**[S39]。建議把該項改寫為「俯臥 vs 仰臥：劑量學與擺位精準度的取捨，姿勢是計畫決定不是優劣」，以符合 §一1「劑量學較優與臨床結果證實較優永遠分開寫」。
