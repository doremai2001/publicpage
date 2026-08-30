# C 組研究簡報 — 子宮頸癌專題（階段三：療程中的照護）

研究日期：2026-08-30。所有期刊來源皆以 Europe PMC REST API（`EXT_ID`／`TITLE`／`AUTH` 查詢，`resultType=core` 取摘要）逐條查證，書目欄位照 API 回傳值抄寫。指引全文另以 Europe PMC fullTextXML（ESGO 2023＝PMC10247855、EMBRACE-II＝PMC5862686）或官方 landing page 驗證原文。仿單以 openFDA `drug/label.json` 取全文。台灣端以 nhi.gov.tw／mohw.gov.tw 原始檔案（PDF／XLS）下載後 grep 原文；查不到的一律記 FAIL。

**跨組界線提醒（SPEC §五）**
- CCRT 的療效數字（CCCMAC 的 6%、HR 0.81；GOG 各試驗的 PFS/OS 相對風險；OUTBACK／INTERLACE／KEYNOTE-A18）**全部屬 B3**。本簡報保留 GOG 試驗的「療程設計」與「毒性率」（第十節把急性毒性給 C2、cisplatin 當天實務給 C3），療效數字一個都不寫。
- 近接治療的證據與流程 → C1 完整寫；C2、B1 一句話指路。
- **總治療時間的數字（幾 %／天、HR、7 週／50 天／56 天）→ C2 主場**；C1 只留一句「拖長會輸掉局部控制，數字見 C2」。
- 急症警語總表 → C2；其他篇只留與自己直接相關的一兩條並指向 C2。
- 擴張器的協定（何時開始、頻率、多久）與狹窄發生率 → **D2**；C4 只寫「變化已經開始＋為什麼銜接要在放療結束時就發生」。
- 提早停經與 HRT 的數據 → D1；C4 一句話。
- 性生活一般層（治療中可不可以、體液、慾望）→ 站上 `care-sex`；C4 列出該文已寫內容（見 C4 區塊的清單），指路不重寫。

---

# C1 — 近接治療：名字最可怕，那幾天最關鍵　【紅線 1：全系列風險最高的一篇】

**Key facts**

*不做近接，存活真的變差（資料庫證據）*
- Han 等人的 SEER 分析（美國，1988–2009，7,359 名接受體外放療的 IB2–IVA 期病人）：63% 合併近接治療、37% 只做體外放療。傾向分數配對後，做近接者 4 年癌症特異存活 64.3% vs 51.5%（P<.001）、整體存活 58.2% vs 46.2%（P<.001）；近接與較佳存活獨立相關（CSS HR 0.64，95% CI 0.57–0.71；OS HR 0.66，0.60–0.74）。同一分析發現近接使用率從 1988 年 83% 掉到 2009 年 58%，2003 年更一度掉到 43% [S1]
- **同一團隊 2024 年的更新版**（SEER 2000–2020，8,500 名 FIGO 2009 IB2–IVA 接受體外放療者）：64% 合併近接；使用率在 2003/04 觸底（2003 年 44%）後**回升，2018–2020 已達 76%**。配對後做近接者 4 年癌症死亡累積發生率 32.1% vs 43.4%、整體存活 64.0% vs 51.4%（皆 P<.001）；癌症特異死亡 HR 0.70（0.64–0.76）、全因死亡 HR 0.72（0.67–0.78）。結論原文：近接是局部晚期子宮頸癌「an essential component of treatment」 [S2]
- Gill 等人的 NCDB 分析（美國，2004–2011，7,654 名 IIB–IVA、有加強照射資料者）：90.3% 用近接；期間近接使用率 96.7%→86.1%，IMRT/SBRT 加強從 3.3%→13.9%。控制其他因子後，**用 IMRT 或 SBRT 加強取代近接，整體存活較差（HR 1.86，95% CI 1.35–2.55，P<.01）——這個傷害比不做化療的傷害（HR 1.61）還大** [S3]
- Tanderup、Eifel、Pötter 等人在 IJROBP 的專文標題就是〈Curative radiation therapy for locally advanced cervical cancer: brachytherapy is NOT optional〉（2014）——「近接不是可選項」是這個領域自己說出口的話 [S4]

*做好近接，局部控制可以到多高（IGABT 前瞻資料）*
- EMBRACE-I（24 個中心的前瞻世代研究，1,341 名可分析、1,251 名可評估毒性；IB–IVA 或僅 L1-L2 以下主動脈旁轉移的 IVB）：治療為每週 cisplatin 40 mg/m²（5–6 次）＋體外放療 45–50 Gy（1.8–2 Gy/次）＋MRI 導引的影像導引適應性近接治療；CTV-HR D90 中位數 90 Gy EQD2（IQR 85–94）。中位追蹤 51 個月，**5 年精算局部控制 92%（95% CI 90–93）**；5 年 G3–5 毒性累積發生率：泌尿 6.8%、腸胃 8.5%、陰道 5.7%、瘻管 3.2% [S5]
- retroEMBRACE（12 個中心、731 名接受影像導引近接者）：3／5 年局部控制 91%／89%；**分期別 5 年局部控制：IB 98%、IIB 91%、IIIB 75%**；5 年 G3–5 毒性：膀胱 5%、腸胃道 7%、陰道 5% [S6]
- retroEMBRACE 的劑量效應（EMBRACE-II 論文轉述）：CTV-HR D90 ≥85 Gy（EQD2）**且在 7 週內完成**，3 年局部控制在小腫瘤（<20 cm³）≥94%、中等（20–30 cm³）>93%、大腫瘤（至 70 cm³）>86% [S8]

*「體外加強取代不了」的指引原文（這篇的地基）*
- ESGO/ESTRO/ESP 2023 更新版指引原文：「**IGBT is an essential component of definitive radiotherapy and should not be replaced with an external boost (photon or proton). If BT is not available, patients should be referred to a center where this can be done** [III, B]」 [S7]
- 同指引：對腫瘤相關標的「不建議用體外放療補加強劑量（如子宮頸加強、參數加強），**即使用的是立體定位放療或粒子治療等先進技術**」；用中線擋塊做參數加強也不建議 [S7]
- 美國近接治療學會（ABS）2012 共識 Part I：「The ABS recommends the use of brachytherapy as a component of the definitive treatment」，根治性治療的累積劑量約 80–90 Gy [S9]；Part II 原文：「The ABS **affirms the essential curative role** of tandem-based brachytherapy」 [S10]

*劑量邏輯（圖 fig-cx-brachy-dose 的數據，見下方圖表數據區）*
- ESGO 2023：體外放療 45 Gy/25 次（或 46 Gy/23 次）；近接要在這之上**再加 40–45 Gy EQD2**，把 CTV-HR 的 D90 推到 **85–95 Gy EQD2** [S7]
- EMBRACE-II 計畫書的規劃目標：CTV-HR D90 目標 90–95 Gy（處方下限 85 Gy）；同時膀胱 D2cm³ 目標 <80 Gy（上限 <90）、直腸 <65（<75）、直腸陰道參考點 <65（<75）、乙狀結腸／腸 <70（<75）——腫瘤要 85–95、緊貼著的直腸膀胱只准 65–90，**這個劑量落差正是近接「從裡面照、劑量急遽下降」才做得到的** [S8]

*流程逐步（拆解恐懼的素材）*
- 置入物：子宮腔內管（tandem）＋陰道端（卵圓體 ovoids／環 ring／模具），必要時加組織間插針（IC/IS）；ESGO 原文：「**Intracavitary and combined intracavitary/interstitial BT implants should be performed under anesthesia**」，並要求「Care should be taken to optimize patient comfort during (fractionated) BT，最好有多專科參與」 [S7]
- 影像：建議 MRI（放著置入器照）；也可用 CT 或超音波；每次置入後都要重新做劑量計算才治療（ABS：dosimetry must be performed after each insertion）[S7][S10]
- 次數與間隔：HDR 通常 **3–4 次**、每次至少間隔 6–8 小時；或 PDR 一次置入 50–60 個每小時脈衝（等於置入約兩天）[S7]。美國 ABS 最常用的是 5 次 ×5.5 Gy（腫瘤 >4 cm 用 5×6 Gy），另列 4×7、6×5 等 [S10]。時程：大腫瘤的近接安排在化放療**接近尾聲或結束後的 1–2 週內**完成 [S7]
- 病人端的美國癌症協會（ACS）說法可引用：HDR 是門診療程、「放射源置入幾分鐘後就取出」；LDR 則需住院數天臥床。（**HDR 治療結束後體內沒有任何放射性物質留著**——這一句要寫，站上 care-sex 講的「體內有放射線種子」是攝護腺永久植入，不是這裡的遙控後荷式）[S13]

*不適是真的（本篇承諾不粉飾的素材）*
- Kirchheiner 等人的前瞻研究（單一機構、50 名局部晚期病人；**該院做法是一次置入、留置過夜、打兩個分次，脊椎／硬脊膜外麻醉**）：治療後 1 週 30% 有急性壓力症狀，3 個月後 41% 有創傷後壓力症狀（PTSD symptoms）。壓力來源分析：**不是置入本身，而是兩個分次之間帶著置入器不能動的那段時間**；有幫助的因素是團隊支持、心理支持、事前說明；壓力因素是疼痛、流程混亂、置入期間不能動 [S11]
- Humphrey 等人的系統性回顧（19 篇研究）：10 篇心理層面研究有 9 篇把近接描述為造成焦慮與痛苦（distressing）的經驗；**止痛與麻醉的做法各院差異很大**；結論是需要更好的疼痛管理、病人資訊與支持性介入 [S12]

*總治療時間（一句話，數字歸 C2）*
- ESGO 2023：含近接在內的總治療時間不超過 7 週 [S7]。為什麼、拖一天輸多少 → 見 C2。

**Claim ceiling**

Defensible：
- 「在美國的全國資料庫裡，該做近接而沒做的病人，4 年存活差了 10 個百分點以上；用『高精準』體外放療代替近接的病人，死亡風險將近兩倍——這個傷害比不做化療還大。」[S1][S2][S3]
- 「歐洲三個學會 2023 年的指引寫得很直接：近接是根治性放療的必要組成，不能用體外加強取代——光子不行，質子也不行；如果這家醫院做不了，應該轉去做得了的醫院。」[S7]
- 「體外放療安全給到 45 Gy 左右就得停手，因為直腸膀胱就貼在旁邊；根治需要的是 85–95 Gy。那多出來的 40–45 Gy，只有從腫瘤裡面照、劑量隨距離急遽下降的近接做得到。」[S7][S8]
- 「現代影像導引近接治療的前瞻資料：5 年局部控制 92%，各器官的嚴重併發症各在一成以下。」[S5]
- 「置入應該在麻醉下做，這是指引的原文，不是我的個人做法。」[S7]
- 「有研究誠實量過：在一次置入留置過夜打兩次的做法下，三個月後四成的人有創傷後壓力症狀。壓力主要來自置入器留在身上不能動的那段時間——所以事前知道流程、疼痛有人管，真的有差。」[S11][S12]
- 「HDR 每次治療放射源只進來幾分鐘，出來之後你身上沒有任何放射性。」[S13]

Would overstate：
- ✗ 任何讀起來像「近接可以不做」「體外加強可以代替」「只是加分」的句子——**紅線 1，直接失敗**
- ✗「美國醫師越來越不做近接了。」——2013 年的下滑（2009 年 58%）在 2024 年更新版已回升到 76%（2018–2020）[S2]。要講歷史教訓可以，不可寫成現在進行式
- ✗「做了近接就一定控制得住。」——大腫瘤（CTV-HR 至 70 cm³）3 年局部控制 >86%，不是 100% [S8]
- ✗「過程不會痛、不用怕。」——反向紅線。Kirchheiner 與 Humphrey 的資料都要寫 [S11][S12]
- ✗ 把 Kirchheiner 的 41% PTSD 寫成所有近接的通例——那是「一次置入、留置過夜、兩分次」的單一機構做法；各院流程與麻醉差異很大 [S11][S12]
- ✗「5 次是標準次數。」——ABS 美國常用 5 次、ESGO 寫 HDR 通常 3–4 次；次數依各院與劑量分割而定 [S7][S10]
- ✗ 寫出「體外放療最多只能給 XX Gy」的單一數字——本次查證只有「EBRT 45–50 Gy＋近接推到 85–95」的指引寫法，沒有「體外單獨安全上限」的可引用數字。用相對邏輯寫，不要發明數字

**Caveats / safety notes**

- SEER／NCDB 是觀察性資料庫，傾向分數配對仍可能殘留干擾（沒做近接的人可能本來就更虛弱）；但方向與 IGABT 前瞻資料、劑量效應資料一致，且指引已經把話說死。寫的時候用「資料庫分析」自稱，不寫成隨機試驗。
- Gill 的 HR 1.86 族群是 IIB–IVA、2004–2011、以 OS 為終點；標籤要帶。
- EMBRACE-I 的 92% 是「局部控制」不是存活；5 年 OS 74%（retroEMBRACE 世代）。兩者不可混用 [S5][S6]。
- Kirchheiner PTSD 研究：一定要同時寫「壓力來源不是近接本身」與該院特殊做法，否則這篇會自己製造恐懼——但也不可以因此把數字藏起來。
- 「如果這家醫院做不了近接應轉院」是指引原文，但寫法要小心不點名機構（固定紅線）：寫「跟你的放腫醫師確認近接的安排」即可，指引原文可引。
- 麻醉方式（全身／半身／鎮靜）各院不同；本次查證只有「應在麻醉下執行」的指引句與 Kirchheiner 用脊椎/硬脊膜外的描述，沒有各選項比例的可引用資料——作者可用自己門診的做法描述，但不要冠上「標準」二字。

**Taiwan status**

- **近接治療是健保支付項目**——健保署「醫療服務給付項目」檔（114.01.01 生效版，官方 XLS）明列：37007B 安裝近接治療器（複雜）每次 3,236 點、37008B（簡單）每次 1,650 點、37010B 組織插種治療 5,611 點、**37018B 遙控後荷式近距治療（簡單）每次 4,126 點、37019B（複雜）每次 6,600 點** [S37]。給付的臨床條件與審查細節不在此檔內→費用相關細節寫「向醫務課或個管師確認」。
- SBRT（身體立體定位放射治療 37047B）健保給付範圍是**原發性早期肺部及肝膽單一病灶**（104 年納入時的公告）——**不含子宮頸癌**；「用 SBRT 代替近接」在台灣既無實證也不在給付範圍 [S37][S40]。
- 全台設有「癌症資源中心」的醫院（2023 年公告為 104 家），免付費諮詢專線 0809-010580 [S35][S36]。

## 圖表數據（fig-cx-brachy-dose）

| 項目 | 數值 | 來源 |
|---|---|---|
| 體外放療（骨盆） | 45 Gy／25 次（或 46 Gy／23 次），IMRT/VMAT | [S7] |
| 近接治療要再加 | 40–45 Gy EQD2 | [S7] |
| 腫瘤（CTV-HR D90）合併目標 | 85–95 Gy EQD2（EMBRACE-II 目標 90–95、下限 85） | [S7][S8] |
| ABS 的說法 | 累積約 80–90 Gy | [S9][S10] |
| 同時膀胱 D2cm³ 必須 | 目標 <80 Gy（上限 <90） | [S8] |
| 同時直腸 D2cm³ 必須 | 目標 <65 Gy（上限 <75） | [S8] |
| 直腸陰道參考點 | 目標 <65 Gy（上限 <75） | [S8] |
| 乙狀結腸／腸 D2cm³ | 目標 <70 Gy（上限 <75） | [S8] |
| 劑量效應（≥85 Gy、7 週內完成） | 3 年局部控制：<20 cm³ ≥94%；20–30 cm³ >93%；大腫瘤 >86% | [S8] |
| 不做近接的代價 | 4 年 OS 64.0% vs 51.4%（SEER 配對）；IMRT/SBRT 加強取代 HR 1.86 | [S2][S3] |

圖注建議：「示意圖，依 ESGO/ESTRO/ESP 2023 指引與 EMBRACE-II 計畫書之劑量目標重繪」。

---

# C2 — 骨盆放療的五、六週怎麼過　【急症警語主場｜紅線 6：不可自行中斷】

**Key facts**

*療程的形狀（fig-cx-treatment-weeks 的骨架，見下方圖表數據）*
- ESGO 2023：體外放療 45 Gy/25 次（或 46 Gy/23 次）＝**每週 5 次、約 5 週**，用 IMRT/VMAT＋每日影像導引；影像上有病理性淋巴結另用同步整合加強（合併近接估算約 60 Gy EQD2）[S7]
- 每週化療：cisplatin 40 mg/m²，每週一次（詳見 C3）[S5][S7]
- 近接：大腫瘤在化放療**接近尾聲或結束後 1–2 週內**完成，HDR 通常 3–4 次（每次間隔至少 6–8 小時）[S7]
- **總治療時間（含近接）不超過 7 週**——ESGO 原文有兩處：「Delay of treatment and/or treatment interruptions have to be prevented to avoid tumor progression and **accelerated repopulation**. The overall treatment time including both EBRT and BT should therefore not exceed 7 weeks」 [S7]；EMBRACE-II 把上限訂在 **50 天**，並揭露 EMBRACE-I 有 21% 的病人超過 50 天——所以這不是理所當然做得到的事，要整個團隊排程去搶 [S8]

*拖長會輸掉什麼（紅線 6 的證據本體）*
- Girinsky 等人（386 名 IIB–III 期、只做放療的年代，1973–1983）：總治療時間與輸血是多變項分析裡最顯著的兩個因子；**超過 52 天之後，局部控制與整體存活各約每天損失 1%** [S14]
- Petereit 等人（209 名 IB–IIIB、體外＋LDR 腔內）：<55 天 vs ≥55 天，5 年存活 65% vs 54%（p=0.03）、骨盆控制 87% vs 72%（p=0.006）；**超過 55 天後每多一天，存活掉 0.6%／骨盆控制掉 0.7%**；晚期併發症沒有因為治療快而增加 [S15]
- Song 等人（CCRT 年代的回溯，113 名 IB2–IIIB）：**近接完成時間 >56 天者骨盆復發風險 HR 3.8（95% CI 1.2–16）**，3 年骨盆復發 26% vs 9%（P=.04）；拖長的原因主要是近接延後開始與急性 G3/4 毒性；作者建議 8 週內完成全部放療 [S16]
- 標籤要誠實：Girinsky／Petereit 是「放療單獨」年代的資料，Song 是 CCRT 年代、樣本小；指引取其一致方向訂出 7 週（ESGO）／50 天（EMBRACE-II）。「每天 1%」引用時要帶「舊年代、只做放療的世代」標籤。

*急性副作用有多常見（帶分母）*
- Kirwan 等人的系統性回顧（19 個隨機試驗、4,580 名隨機、毒性資料 1,766 名）：化放療 vs 放療單獨，**G3–4 白血球毒性 OR 2.15（1.57–2.95）、血小板毒性 OR 3.04（1.08–8.51）、腸胃毒性 OR 1.92（1.26–2.92）**；G1–2 血液毒性也較高；長期毒性只有 8 個試驗有報告，其中 7 個無統計差異（＝資料不足，不是證明安全）[S18]
- 絕對數字（單一試驗、族群標籤 bulky IB）：GOG/Keys 試驗，放療＋每週 cisplatin 組（183 人）**暫時性 G3–4 血液毒性 21%（放療單獨組 2%）、G3–4 腸胃毒性 14%（vs 5%）** [S19]
- CCCMAC 個別病人資料統合分析（18 個試驗）：急性血液與腸胃毒性隨化放療增加；晚期毒性資料太稀疏無法分析（**療效數字歸 B3，此處只用毒性句**）[S17]
- 疲倦、膀胱炎、皮膚反應：ACS 病人端頁面可引用其定性描述（放射性膀胱炎——頻尿、解尿不適；皮膚由紅到脫皮；疲倦；貧血）[S13]。**急性頻率的分母級數字本次沒有查到可引用的來源→寫定性，不發明百分比**。台灣端：健保支付標準有「放射治療之皮膚處理（一個療程）」37026B 這個項目 [S37]。

*腹瀉的處理與「低渣飲食」的誠實版*
- ESMO 2018 癌症病人腹瀉臨床實務指引存在、可引用為指引級來源 [S23]——但本環境無法取得全文逐字（見 FAIL S45），**loperamide 劑量與「複雜性腹瀉」的逐字定義不可寫**；文章寫到藥物時停在「第一線止瀉藥、由團隊指示使用」層級。
- 飲食證據是兩面的：Cochrane 回顧（4 個試驗、413 人）發現「調整脂肪／乳糖／纖維」的飲食介入減少放療結束時的腹瀉（RR 0.66，95% CI 0.51–0.87，中等品質、老技術年代）[S24]；但 2017 年的隨機試驗（166 名骨盆放療病人分低纖／習慣／高纖三組）發現**高纖組急性與 1 年後的腸道症狀都比習慣組好**，作者原文：「Restrictive, non-evidence-based advice to reduce fiber intake in this setting should be abandoned」[S25]。→「一律低渣」不是有證據的建議；乳糖與高脂的調整比較有依據。
- 補水與脫水辨識：無法進食飲水、尿量變少、站起來頭暈——這組症狀合併腹瀉屬當天聯絡（見總表；來源為臨床常識級，標示為「無單一可引用門檻」）。

*發燒（與 C3 共用，定義在這裡）*
- IDSA 2010 指引原文（已於本次獨立重新驗證）：發燒＝「a single oral temperature measurement of ≥38.3°C (101°F) or a temperature of ≥38.0°C (100.4°F) sustained over a 1-h period」；嗜中性球低下＝「ANC <500 cells/mm³ or expected to decrease to <500 during the next 48 h」；ANC <100 稱 profound [S21]
- ESMO 發熱性嗜中性球低下指引可作為歐洲的指引級來源 [S22]
- Cisplatin 仿單：骨髓抑制發生於 25–30%；**嗜中性球低下病人的發燒與感染有致死報告** [S26]

**Claim ceiling**

Defensible：
- 「指引把總治療時間的上限寫成 7 週，EMBRACE-II 訂 50 天——不是行政方便，是因為腫瘤在治療中會加速再增殖；只做放療年代的資料，超過 52–55 天後每拖一天，局部控制掉約 1%。」[S7][S8][S14][S15]
- 「化放療年代的資料：近接沒有在 56 天內完成的人，骨盆復發率是完成者的近三倍（26% vs 9%）。」[S16]
- 「第四、五週最難受的時候請假一週，輸掉的不是舒適，是控制率。難受要說，讓團隊處理症狀，而不是自己按暫停。」[S7][S14][S15][S16]
- 「加上每週化療之後，嚴重腸胃毒性大約是放療單獨的兩倍、白血球毒性也約兩倍——以 bulky IB 的試驗為例，G3–4 血液毒性 21%、腸胃 14%。」[S18][S19]
- 「『放療就要吃低渣』其實證據很弱；2017 年的隨機試驗甚至發現高纖組比較好，作者直接說這種限制性建議該被放棄。乳糖和脂肪的調整比較有依據。個別情況跟營養師談。」[S24][S25]
- 「正在化放療的人，量到 38.3°C 一次、或 38°C 持續一小時，就當急症處理，不要先吃退燒藥觀察一晚。」[S21][S26]

Would overstate：
- ✗「撐不下去可以休息一兩週再繼續。」——**紅線 6，直接失敗**
- ✗ 把「每天損失 1%」寫成現代化放療的精確數字——那是 1970–80 年代放療單獨的世代 [S14]
- ✗「7 週內做完是醫院的責任，跟你無關。」——EMBRACE-I 有 21% 超過 50 天，排程、回診、副作用回報都會影響 [S8]
- ✗「低渣飲食可以預防腹瀉。」——證據兩面，見上 [S24][S25]
- ✗ 寫出腹瀉「一天幾次以上」的通用數字門檻——CTCAE 與 ESMO 指引逐字內容本次取不到（S44、S45），不可憑記憶給分級數字
- ✗ 給 loperamide 用法用量——藥物劑量不可寫成用法用量（colon SPEC §四），且逐字來源缺
- ✗「IMRT 比較貴所以比較好」或任何設備別優劣的行銷句——醫療法紅線

**Caveats / safety notes**

- 「不可自行中斷」與「有症狀要回報」必須同時成立：中斷的決定只能由團隊做（例如血球太低時本來就會由醫師喊停），病人的工作是回報，不是硬撐著隱瞞。這與 colon C1 的「講」和「決定」分開的寫法同構。
- 治療時間的三個數字（7 週指引、50 天 EMBRACE-II、56 天 Song）不要混寫成一個；建議主句用指引的 7 週，證據句各帶自己的標籤。
- Kirwan 的 OR 不是發生率；勝算比第一次出現要翻白話（colon SPEC §三），有絕對數字（Keys 的 21%、14%）就放絕對數字。
- 疲倦與膀胱炎沒拿到分母數字——是本篇最薄的一塊，寫定性即可，不要為了對稱去發明數字。
- 陰道出血：ESGO 只有在**晚期／緩和照護脈絡**寫了大量陰道出血的處置（填塞、栓塞、緩和放療）[S7]；治療中出血的急症門檻沒有可引用數字→總表用症狀描述並標示為臨床常識級。
- 站上 `care-sex` 的引言框已寫「性行為之後發燒或畏寒發抖、會陰或肛門劇痛、出血止不住，這幾項不能等到隔天」——C2 的總表要涵蓋同方向，避免兩處門檻互相矛盾。

**Taiwan status**

- **IMRT/VMAT 沒有健保專屬支付項目**：健保「醫療服務給付項目」檔（114.01.01 版，5,996 項）逐項檢索「強度調控／IMRT／modulated／arc」，放射治療章節內**查無 IMRT/VMAT 專項**（僅 36024B 直腸癌術前低分次含 intensity-modulated 字樣、36022B/36023B 乳癌低分次為包裹項目）；體外放療以「直線加速器遠隔照射治療」按照野計費（36011B 簡單 1,231 點／36012B 複雜 1,334 點）[S37]。→ 指引建議的 IMRT/VMAT（ESGO [S7]）在台灣如何申報、有無自費差額，**各院不同，寫「向醫務課與個管師確認」**，不得宣稱健保有給付或沒給付 IMRT 差額。
- 癌症資源中心：2021 年公告 82 家＋免付費專線 **0809-010580**（頁面日期 110-08-18，引用要標年份）[S35]；2023 年公告已達 **104 家**（更新時間 113-03-21）[S36]。hpa.gov.tw 的對應頁面本環境 SSL 失敗，改引衛福部本部頁（同 colon 系列的處理）[S43]。

## 急症警語總表（症狀 → 門檻 → 來源）

| # | 症狀 | 門檻／行動 | 來源 |
|---|---|---|---|
| 1 | 發燒（化放療期間全程適用） | 單次口溫 ≥38.3°C，或 ≥38.0°C 持續 1 小時 → 立即聯絡、當急症；不要先退燒觀察過夜 | [S21]（IDSA 定義，OUP 原文已驗）；[S26]（仿單：嗜中性球低下之感染有致死報告） |
| 2 | 腹瀉合併脫水 | 水瀉不止＋喝不下、尿量少、站起來頭暈，或腹瀉合併發燒／血便 → 當天聯絡 | 指引級方向 [S23]；**逐字分級門檻取不到（S44/S45），此列為症狀描述、臨床常識級** |
| 3 | 輸注中或輸注後數分鐘的過敏樣反應 | 臉腫、胸悶氣喘、心跳快、頭暈（低血壓）→ 當場喊人／立即回院 | [S26]（cisplatin 仿單 boxed warning：anaphylactic-like reactions within minutes） |
| 4 | 尿量明顯變少 | 化療後幾天內尿量明顯下降、下肢水腫 → 當天聯絡（cisplatin 腎毒性自第二週顯現） | [S26] |
| 5 | 大量陰道出血 | 出血止不住（衛生棉短時間內濕透、頭暈）→ 當天就醫 | 症狀級；ESGO 對大量陰道出血列有填塞／栓塞／放療等處置（原文脈絡為晚期照護，標籤要帶）[S7] |
| 6 | 解尿問題 | 完全解不出尿、或整泡肉眼血尿 → 當天聯絡 | **無可引用門檻來源——臨床常識級，寫作時不掛引用** |
| 7 | 性行為後 | 發燒／畏寒發抖、會陰或肛門劇痛、出血不止 → 不能等隔天 | 與站上 care-sex 引言框一致（指路，不重寫） |
| 8 | 聽力改變、耳鳴（非急症但必報） | 下次回診主動講；不是急診，但別自己吞 | [S26][S29]（詳見 C3） |

## 圖表數據（fig-cx-treatment-weeks，C2/C3 共用）

| 元素 | 數據 | 來源 |
|---|---|---|
| 體外放療 | 45 Gy/25 次（每週 5 次 ×5 週）或 46 Gy/23 次；IMRT/VMAT＋每日影像導引 | [S7][S8] |
| 每週化療 | cisplatin 40 mg/m²，每週 1 天，共 5–6 次（EMBRACE-I 描述）；單週上限 70 mg（GOG/Keys） | [S5][S7][S19] |
| 近接治療 | HDR 通常 3–4 次（間隔 ≥6–8 小時）；大腫瘤排在療程尾聲或結束後 1–2 週內 | [S7] |
| 淋巴結加強 | 同步整合加強至約 60 Gy EQD2（含近接貢獻估算） | [S7] |
| 總時鐘 | 全部（含近接）≤7 週；EMBRACE-II 上限 50 天；EMBRACE-I 21% 超過 50 天 | [S7][S8] |

---

# C3 — 每週化療那一天

**Key facts**

*方案本身（療效證據歸 B3，這裡只放「是什麼」）*
- ESGO 2023 原文：同步化療應為單一藥物放射增敏化療，「preferably cisplatin (weekly 40 mg/m²)」；**cisplatin 不能用時，替代選項是每週 carboplatin（AUC=2）或熱治療（有設備才有）**；完全不能化療的病人可單做放療 [S7]
- EMBRACE-I 的治療描述：每週靜脈 cisplatin 40 mg/m²，5–6 個週期、每週期 1 天 [S5]
- GOG/Keys 試驗的設計：40 mg/m² 每週一次、最多 6 次、**單週最高 70 mg** [S19]；GOG-120 同為 40 mg/m² ×6 週 [S20]

*腎臟（這一天喝水／輸液的理由）*
- Cisplatin 仿單（openFDA，2024/01 版）：**累積性腎毒性是主要的劑量限制毒性**；單次 50 mg/m² 後 28–36% 出現腎毒性，於給藥後**第二週**開始顯現；重複療程會更嚴重、更持久；**腎功能未回到正常前不可再給下一劑**；每次給藥前要驗 BUN／肌酸酐／肌酸酐清除率與鎂鈉鉀鈣 [S26]
- 仿單的水化寫法（注意：仿單針對的是每 3–4 週 50–100 mg/m² 的傳統劑量）：給藥前 8–12 小時輸液 1–2 公升，之後 24 小時維持水分與尿量 [S26]。**每週 40 mg/m² 的當天水化流程各院不同，本次沒有查到台灣通用的可引用協定→「當天總共幾小時」寫作者自己門診的實際流程（作者本人執業描述，不掛文獻），不要冠「標準」**
- 仿單：不可用含鋁的針具與輸液套件（鋁會與 cisplatin 反應）[S26]——可當「為什麼化療室有些器材規定」的小知識

*聽力（誠實版：風險存在，但每週低劑量的實測結果比想像溫和）*
- 仿單：單次 50 mg/m² 後聽毒性最高 31%，表現為耳鳴與 4,000–8,000 Hz 高頻聽損，可單側可雙側、隨累積劑量變頻繁變嚴重，是否可逆不明確；建議治療前與每劑前做聽力檢查 [S26]
- 但每週 40 mg/m² 的化放療實測（Marnitz 等，51 名病人，累積劑量 115–400 mg，中位 342 mg）：62% 在治療後有 ≥20 dB 的閾值變化（55% 在 ≥6,000 Hz），**經年齡與時間校正後沒有統計上顯著的聽力損失**，主觀聽力與日常活動無人受影響；作者結論：這個族群不需常規聽力檢查 [S29]
- 寫法：耳鳴、聽不清楚要主動回報（仿單層級的警語），但不要把 31% 的傳統劑量數字直接套在每週 40 mg/m² 上——兩個劑量脈絡都要標

*血球與時間點*
- 仿單：骨髓抑制 25–30%；白血球與血小板**最低點在第 18–23 天**（範圍 7.5–45），多數在第 39 天前恢復；貧血發生頻率與時間類似；下一劑條件：血小板 ≥100,000/mm³、WBC ≥4,000/mm³ [S26]（此為傳統劑量寫法；每週給藥時是每週抽血把關）
- 發燒門檻與行動 → C2 總表 [S21]

*止吐（打 cisplatin 那天為什麼要吃這麼多顆藥）*
- ASCO 止吐指引：cisplatin 屬高致吐風險；2017 年版把 **olanzapine 加入高致吐化療的止吐組合**、NK1 受體拮抗劑角色擴大；2020 年更新維持成人建議不變 [S27][S28]。寫作用「NK1＋5-HT3＋類固醇（±olanzapine）的組合」層級即可，不寫個別劑量
- 延遲性噁心（第 2–5 天）正是 NK1／olanzapine 要蓋的時段——「回家後兩三天比當天更想吐」是預期內，不是藥沒效 [S27]

*Cisplatin 不能打的時候（誠實寫弱）*
- Bacorro 等人的系統性回顧與統合分析（20 篇研究、對 cisplatin 有相對或絕對禁忌的局部晚期病人）：相對禁忌者用 cisplatin CRT 仍有效且耐受可；**carboplatin CRT 化療完成率較好（86%）但 5 年 OS 較低（44%），作者結論是「效果不明確」（unclear effectiveness）**；多為間接比較、異質性高 [S30]
- ESGO 也只把 carboplatin 列為「not suitable for cisplatin」時的替代 [S7]。→ 主旨句：換 carboplatin 不是「比較溫和的同等選擇」，是腎功能等條件不允許時的次佳解

**Claim ceiling**

Defensible：
- 「每週那一天的順序是有道理的：先抽血看腎功能與血球，過關才給止吐藥、輸液，然後才是化療，後面再補水。因為 cisplatin 傷腎是累積性的，而且仿單規定腎功能沒回來就不能給下一劑。」[S26]
- 「打 cisplatin 那天拿到一整袋止吐藥不是過度醫療——cisplatin 是最會讓人吐的一級，指引建議多種機轉的藥一起上，包括蓋住第二到第五天的延遲性噁心。」[S27][S28]
- 「耳鳴或聽不清楚要講。不過也說句公道話：每週 40 的劑量下，有研究做完整聽力檢查，校正年齡後沒有測到顯著的聽力損失——風險是真的，但不是傳統高劑量的那個數字。」[S26][S29]
- 「腎功能不行的時候換 carboplatin，化療比較打得完，但效果的證據明顯比 cisplatin 弱——這是一個誠實的取捨，不是升級。」[S7][S30]

Would overstate：
- ✗ 寫出任何療效數字（HR、存活%）——歸 B3
- ✗ 給水化的量與時數當「標準流程」——仿單是傳統劑量的寫法，每週劑量各院不同；作者可描述自己的做法但不掛文獻
- ✗「打了會聾。」／「每週劑量完全不傷聽力。」——兩個方向都超過 [S26][S29]
- ✗「carboplatin 效果一樣只是比較不傷腎。」——Bacorro 的結論相反 [S30]
- ✗「最低點固定在第 18–23 天。」——那是傳統劑量仿單值；每週給藥用每週抽血把關，不要教病人自己算日子 [S26]

**Caveats / safety notes**

- 仿單所有數字都來自較高單次劑量（50–100 mg/m² q3–4w）的年代資料；引用時逐項標「單次 50 mg/m² 後」。每週 40 mg/m² 的毒性率用 Keys（G3–4 血液 21%、腸胃 14%，bulky IB 族群）比較貼近 [S19]。
- 「聽力檢查要不要做」兩個來源方向不同（仿單：每劑前；Marnitz：這個族群不需常規做）——照實寫成「各院做法不同、有症狀必查」，這正是這個專題「誠實勝過乾淨」的示範點。
- 提醒病人自備清單（食物、水、消磨時間的東西、記錄副作用的紙）屬經驗層，不掛引用。
- 避孕與生育：不在 C3 展開，指向 B4 與站上 care-fertility。

**Taiwan status**

- **Cisplatin**：健保「藥品給付規定」第 9 節（抗癌瘤藥物，115.8.21 版）**沒有 cisplatin 專屬的限制條文**（逐頁檢索無 9.x Cisplatin 條目；它只出現在其他藥的併用條文裡）——老藥無特別限制通常代表依適應症常規使用，但**「有給付」的正式條文本次拿不到**（健保用藥品項檔 data.nhi.gov.tw 遭本環境阻擋，見 S42）→ 文章寫「cisplatin 是化放療的健保常規用藥這件事請放心，但費用細節以醫院醫務課為準」，不引條文 [S39][S42]
- **Carboplatin**：第 9 節 9.2 有明文——「限 1. 卵巢癌患者。2. **腎功能不佳(CCr<60)或曾作單側或以上腎切除之惡性腫瘤患者使用**。…」[S39]。→ 台灣的給付條件正好對應「cisplatin 腎功能禁忌時的替代」這個臨床邏輯，可以寫、要照原文範圍寫
- **止吐藥**：第 7 節 7.2 止吐劑有完整條文：致吐風險分級「依 NCCN 最新版治療指引內容」；5-HT3（ondansetron 等）於高／中致吐化療可預防性使用（原則不超過 5 日）；**NK1 拮抗劑（aprepitant／fosaprepitant）給付於高致吐化療之急性與延遲性噁心嘔吐，口服限 3 天、每日 1 顆，注射限第一天**；palonosetron 限中高致吐；NEPA 複方（Akynzeo）每次化療限 1 粒、3 天內不得併用其他同類藥 [S38]。→「那一袋止吐藥每顆都有健保的使用規則」是可寫的台灣段
- **Olanzapine 用於止吐**：第 7 節止吐劑條文中**無 olanzapine**；其給付歸精神科用藥章節、止吐用途查無條文 → gap，寫「若醫師處方 olanzapine 止吐，給付或自費請問藥師」[S38][S46]
- 癌症資源中心與 0809-010580 [S35][S36]

---

# C4 — 治療期間，陰道與荷爾蒙已經在變化

**Key facts**

*變化在治療中／結束時就開始（本篇的核心論證）*
- EMBRACE 陰道morbidity分析（Kirchheiner 等，588 名、中位追蹤 15 個月）：2 年時 G≥3 嚴重陰道併發症的精算機率只有 3.6%，**但 G≥1 高達 89%、G≥2 29%，而且大多數在 6 個月內就出現**；最常見是狹窄、其次乾澀；陰道黏膜炎與出血多為輕度 [S31]（**狹窄的專屬發生率與劑量效應 → D2，本篇不展開**）
- EMBRACE 陰道morbidity子研究（Suvaal 等，113 名、陰道侵犯 ≤5 mm 的族群）：醫師評估的陰道變化**在基線與第一次追蹤之間就有顯著差異，之後不再顯著變化**——變化發生在最早期；追蹤中約 20%（範圍 11–37%）有多為輕度的陰道變化；2 年時 47% 沒有性活動 [S32]
- ACS 病人端頁面：近接治療會刺激陰道，「可能變紅、變痛、有分泌物」；乾澀與性交疼痛可為長期副作用 [S13]

*為什麼銜接（dilator counselling）要在放療結束時就發生（D2 的門口）*
- ESGO 2023 原文：「**After CTRT and BT, patients should be counseled about sexual rehabilitation measures including the use of vaginal dilators. Topical estrogens are indicated** [IV, B]」[S7]——指引把衛教時點放在「治療完成後」，不是幾個月後的回診
- Cochrane 回顧（Miles & Johnson 2014）：**沒有可靠證據支持「放療期間」常規擴張**；放療後的觀察性資料顯示規律擴張與較低的自述狹窄率相關，但因果與偏誤無法排除（健康的陰道本來就比較做得下去）[S33]
- EMBRACE-I 的擴張器使用與陰道morbidity關聯報告（2025）存在 [S34]——**數字歸 D2**，C4 只用一句「規律使用與較輕的陰道變化相關的資料，見〈擴張器〉那一篇」
- 荷爾蒙：ESGO 原文「Hormone replacement therapy is indicated to cervical cancer survivors with premature menopause and should be consistent with standard menopausal recommendation [IV, B]」[S7]——C4 只放一句並指向 D1

*治療期間的清潔與感染照護*
- **本次沒有查到可引用的官方「放療期間陰道清潔」指引**（ACS 頁面無此段；ESGO 的陰道沖洗＋metronidazole 條文是**晚期疾病惡臭分泌物的緩和照護**，族群不同，不可挪用）→ 這一段寫作者門診的一般原則（溫水、不灌洗、有異味或發燒就回報），不掛引用，或標明「以下是我門診的做法」

*站上 care-sex 已經寫掉的內容（C4 指路清單——不可重寫）*
`/home/claude/repo/care-sex.html`〈治療中的性生活，誰來開這個口〉已涵蓋：
1. 引言框的急症句：性行為後發燒／畏寒發抖、會陰或肛門劇痛、出血止不住 → 不能等隔天
2. 「治療期間到底可不可以」：血球正常、無出血、無活動性感染、黏膜完好時治療期間不是禁忌；要避開的狀況清單（含**骨盆腔與會陰正在照射的那幾週**）；並明言查不到任何學會給的血球數值門檻
3. ASCO 2018 性議題指引：應由醫療團隊主動開口
4. 慾望與性功能障礙的盛行率統合數字（乳癌 70%、婦癌單中心 94.5% 等）
5. 化療藥經體液殘留的證據與「48 小時保險套」的出處考證（廢棄物規範，不是試驗）
6. **「身體裡有放射線種子的人可以親近人嗎」——這一段講的是攝護腺癌碘-125／鈀-103 永久植入（ICRP 98）**，不是子宮頸的遙控後荷式；C1/C4 要補的一句是「HDR 近接治療結束後體內沒有放射性」[S13]，然後指向 care-sex 的該段講「留在體內的種子」是另一回事
7. 「陰道乾澀與狹窄不是心理問題，不處理它不會自己好」整段（60–90 Gy 造成纖維化、擴張器「持續使用時有效」但會痛做不下去、ASCO 先潤滑保濕再考慮低劑量陰道雌激素、乳癌觀察性資料）——**C4 與 D2 都不得重寫此一般論述**，只寫子宮頸放療的專屬時序
8. 台灣單中心 RCT：63 名子宮頸癌病人單次性健康衛教課即提升知識與自我效能——C4 可指路（「這件事可以被教」）

**Claim ceiling**

Defensible：
- 「陰道的變化不是治療結束幾個月後才開始的——前瞻資料裡，醫師評估的變化在第一次追蹤就已經跟治療前不同，之後反而不再明顯變化；輕中度的變化在 6 個月內就出現在大多數人身上。」[S31][S32]
- 「嚴重的陰道併發症其實少（2 年 3.6%），但輕度變化幾乎人人有（G≥1 89%）——『不嚴重』和『沒感覺』是兩回事。」[S31]
- 「歐洲指引把性復健衛教（包括擴張器）的時間點寫在化放療與近接**完成後**就開始，外用雌激素是有適應症的（indicated），不是偷偷摸摸的自費偏方。」[S7]
- 「放療『期間』要不要用擴張器？目前沒有可靠證據支持，實務也多半等急性期過。什麼時候開始、怎麼用，寫在〈擴張器〉那一篇。」[S33]
- 「提早停經與荷爾蒙補充是下一階段的題目，先記住一句：荷爾蒙補充在子宮頸癌不是禁忌，指引有明文。」[S7]

Would overstate：
- ✗ 展開狹窄發生率、劑量效應、擴張器頻率協定——D2 主場
- ✗ 展開 HRT 配方與適用條件——D1 主場（紅線 5 在那邊）
- ✗ 重寫 care-sex 的「乾澀狹窄不是心理問題」論證或體液殘留段——只指路
- ✗「治療期間絕對不能有性行為。」——care-sex 已寫「多數時候可以，要看的是幾個具體條件」，其中之一是骨盆正在照射的那幾週要避開；C4 不得寫出比 care-sex 更嚴的絕對禁令，也不得放鬆
- ✗ 給「每天沖洗」之類的清潔指示掛上指引——查無來源；ESGO 的沖洗條文是晚期緩和照護
- ✗ 把 Suvaal 的族群（陰道侵犯 ≤5 mm）的溫和數字推到所有病人——族群標籤要帶

**Caveats / safety notes**

- 這篇最容易犯的錯是「時序錯置」：把 D2 的內容提前寫完，或把急性期寫成永久。結構上建議：急性變化（現在）→ 為什麼結束時就要接住（銜接）→ 指向 D2/D1/care-sex（出口）。
- 89%／29%／3.6% 三個數字並列時要講清楚是「兩年內、含追蹤期」的數字，不是「治療當下」的即時盛行率 [S31]。
- 「陰道出血」在治療期間可能是腫瘤本身、黏膜炎、或急症——出血不止歸 C2 總表，這裡一句話指路。
- 性活動與擴張器在 EMBRACE 分析裡是合併討論的（regular dilation and/or sexual activity）——寫的時候不要把「有性生活」寫成醫囑，也不要寫成禁忌；細節歸 D2。

**Taiwan status**

- 外用（陰道）雌激素在台灣的健保給付狀態：**本次未取得可引用條文**（藥品給付規定第 15 節婦產科製劑未逐條檢索到對應品項條文；未確認）→ gap，寫「向婦產科醫師與藥師確認品項與給付」[S47]
- 擴張器在台灣的取得（醫材、自費）→ D2 的台灣段處理，C4 不展開
- 癌症資源中心與 0809-010580 [S35][S36]

---

## Sources（單一編號序列；PASS 除非標 FAIL）

- **[S1] PASS** — Han K, Milosevic M, Fyles A, Pintilie M, Viswanathan AN. (2013). *Trends in the utilization of brachytherapy in cervical cancer in the United States.* Int J Radiat Oncol Biol Phys 87(1):111-119. PMID 23849695, doi 10.1016/j.ijrobp.2013.05.033. URL: https://doi.org/10.1016/j.ijrobp.2013.05.033 — SEER 7,359 人、使用率下滑、4 年 CSS/OS 配對差異、HR 0.64/0.66。Route: Europe PMC REST (TITLE) + abstract (resultType=core)
- **[S2] PASS** — Han K, Colson-Fearon D, Liu ZA, Viswanathan AN. (2024). *Updated Trends in the Utilization of Brachytherapy in Cervical Cancer in the United States: A Surveillance, Epidemiology, and End-Results Study.* Int J Radiat Oncol Biol Phys 119(1):143-153. PMID 37951548, PMC11023766, doi 10.1016/j.ijrobp.2023.11.007. URL: https://doi.org/10.1016/j.ijrobp.2023.11.007 — SEER 2000–2020、使用率回升至 76%、4 年 OS 64.0 vs 51.4%、HR 0.70/0.72、「essential component」原文。Route: Europe PMC REST
- **[S3] PASS** — Gill BS, Lin JF, Krivak TC, et al. (2014). *National Cancer Data Base analysis of radiation therapy consolidation modality for cervical cancer: the impact of new technological advancements.* Int J Radiat Oncol Biol Phys 90(5):1083-1090. PMID 25216857, doi 10.1016/j.ijrobp.2014.07.017. URL: https://doi.org/10.1016/j.ijrobp.2014.07.017 — NCDB 7,654 人、IMRT/SBRT 加強 HR 1.86、比不做化療（HR 1.61）更傷。Route: Europe PMC REST
- **[S4] PASS** — Tanderup K, Eifel PJ, Yashar CM, Pötter R, Grigsby PW. (2014). *Curative radiation therapy for locally advanced cervical cancer: brachytherapy is NOT optional.* Int J Radiat Oncol Biol Phys 88(3):537-539. PMID 24411631, doi 10.1016/j.ijrobp.2013.11.011. URL: https://doi.org/10.1016/j.ijrobp.2013.11.011 — 書目與標題已驗；全文未取得，引用限於標題層級的立場陳述。Route: Europe PMC REST (TITLE+AUTH)
- **[S5] PASS** — Pötter R, Tanderup K, Schmid MP, et al.; EMBRACE Collaborative Group. (2021). *MRI-guided adaptive brachytherapy in locally advanced cervical cancer (EMBRACE-I): a multicentre prospective cohort study.* Lancet Oncol 22(4):538-547. PMID 33794207, doi 10.1016/S1470-2045(20)30753-1. URL: https://doi.org/10.1016/s1470-2045(20)30753-1 — 1,341 人、D90 中位 90 Gy、5 年局部控制 92%、G3–5 各器官毒性、每週 cisplatin 40 mg/m² 5–6 次的療程描述。**分期別局部控制不在摘要內，未驗證→用 retroEMBRACE 的分期數字替代。** Route: Europe PMC REST
- **[S6] PASS** — Sturdza A, Pötter R, Fokdal LU, et al. (2016). *Image guided brachytherapy in locally advanced cervical cancer: Improved pelvic control and survival in RetroEMBRACE, a multicenter cohort study.* Radiother Oncol 120(3):428-433. PMID 27134181, doi 10.1016/j.radonc.2016.03.011. URL: https://doi.org/10.1016/j.radonc.2016.03.011 — 731 人、3/5 年 LC 91%/89%、IB 98%/IIB 91%/IIIB 75%（5 年）、5 年 OS 65%、G3–5 毒性。Route: Europe PMC REST
- **[S7] PASS** — Cibula D, Raspollini MR, Planchamp F, et al. (2023). *ESGO/ESTRO/ESP Guidelines for the management of patients with cervical cancer — Update 2023.* Int J Gynecol Cancer 33(5):649-666. PMID 37127326, doi 10.1136/ijgc-2023-004429. URL: https://doi.org/10.1136/ijgc-2023-004429 — 「IGBT is an essential component… should not be replaced with an external boost (photon or proton)」「not exceed 7 weeks」「performed under anesthesia」「HDR 3–4 次、間隔 6–8 小時」「BT 40–45 Gy EQD2 → 85–95 Gy D90」「weekly cisplatin 40 mg/m²、carboplatin AUC2 替代」「After CTRT and BT… vaginal dilators; topical estrogens are indicated; HRT is indicated」等原文。Route: Europe PMC REST (TITLE) + fullTextXML via PMC10247855（Virchows Arch 同文版本）grep 原文
- **[S8] PASS** — Pötter R, Tanderup K, Kirisits C, et al.; EMBRACE Collaborative Group. (2018). *The EMBRACE II study: The outcome and prospect of two decades of evolution within the GEC-ESTRO GYN working group and the EMBRACE studies.* Clin Transl Radiat Oncol 9:48-60. PMID 29594251, PMC5862686, doi 10.1016/j.ctro.2018.01.001. URL: https://doi.org/10.1016/j.ctro.2018.01.001 — OTT 上限 50 天、EMBRACE-I 21% 超過 50 天、EBRT 45 Gy/25 fx IMRT/VMAT＋每日 IGRT、D90 目標 90–95（下限 85）、OAR 目標（膀胱<80、直腸<65、乙狀結腸/腸<70）、≥85 Gy＋7 週內 → 3 年 LC ≥94/93/86%。Route: Europe PMC REST + fullTextXML grep 原文
- **[S9] PASS** — Viswanathan AN, Thomadsen B; ABS Cervical Cancer Recommendations Committee. (2012). *American Brachytherapy Society consensus guidelines for locally advanced carcinoma of the cervix. Part I: general principles.* Brachytherapy 11(1):33-46. PMID 22265436, doi 10.1016/j.brachy.2011.07.003. URL: https://doi.org/10.1016/j.brachy.2011.07.003 — 「recommends the use of brachytherapy as a component of the definitive treatment」、累積 80–90 Gy。Route: Europe PMC REST
- **[S10] PASS** — Viswanathan AN, Beriwal S, De Los Santos JF, et al. (2012). *American Brachytherapy Society consensus guidelines for locally advanced carcinoma of the cervix. Part II: high-dose-rate brachytherapy.* Brachytherapy 11(1):47-52. PMID 22265437, PMC3489267, doi 10.1016/j.brachy.2011.07.002. URL: https://doi.org/10.1016/j.brachy.2011.07.002 — 「affirms the essential curative role of tandem-based brachytherapy」、每次置入後必做劑量計算、美國常用 5×5.5 Gy（>4 cm 用 5×6）；全文含分割表（4×7、6×5 等）。Route: Europe PMC REST + PMC 網頁全文（WebFetch）
- **[S11] PASS** — Kirchheiner K, Czajka-Pepl A, Ponocny-Seliger E, et al. (2014). *Posttraumatic stress disorder after high-dose-rate brachytherapy for cervical cancer with 2 fractions in 1 application under spinal/epidural anesthesia: incidence and risk factors.* Int J Radiat Oncol Biol Phys 89(2):260-267. PMID 24721589, doi 10.1016/j.ijrobp.2014.02.018. URL: https://doi.org/10.1016/j.ijrobp.2014.02.018 — 50 人、1 週後 ASD 30%、3 個月 PTSD 症狀 41%、壓力來源是分次間留置不能動、有幫助/有害因素。Route: Europe PMC REST
- **[S12] PASS** — Humphrey P, Bennett C, Cramp F. (2018). *The experiences of women receiving brachytherapy for cervical cancer: A systematic literature review.* Radiography (Lond) 24(4):396-403. PMID 30292512, doi 10.1016/j.radi.2018.06.002. URL: https://doi.org/10.1016/j.radi.2018.06.002 — 19 篇；9/10 心理研究描述為 distressing；止痛管理各院差異大；需要更好的疼痛管理與資訊。Route: Europe PMC REST
- **[S13] PASS** — American Cancer Society. *Radiation Therapy for Cervical Cancer.* URL: https://www.cancer.org/cancer/types/cervical-cancer/treating/radiation.html — tandem+ovoids/ring 描述、LDR 住院數天 vs HDR 門診「放射源置入幾分鐘後移除」、急性副作用定性清單（腹瀉、放射性膀胱炎、皮膚、疲倦、血球低）、陰道刺激（紅、痛、分泌物）與長期乾澀。Route: WebFetch（cancer.org）
- **[S14] PASS** — Girinsky T, Rey A, Roche B, et al. (1993). *Overall treatment time in advanced cervical carcinomas: a critical parameter in treatment outcome.* Int J Radiat Oncol Biol Phys 27(5):1051-1056. PMID 8262826, doi 10.1016/0360-3016(93)90522-W. URL: https://doi.org/10.1016/0360-3016(93)90522-w — 386 名 IIB/III、放療單獨；>52 天後 LC 與 OS 各約每天 −1%。Route: Europe PMC REST
- **[S15] PASS** — Petereit DG, Sarkaria JN, Chappell R, et al. (1995). *The adverse effect of treatment prolongation in cervical carcinoma.* Int J Radiat Oncol Biol Phys 32(5):1301-1307. PMID 7635769, doi 10.1016/0360-3016(94)00635-X. URL: https://doi.org/10.1016/0360-3016(94)00635-x — 209 人；<55 vs ≥55 天：5 年 OS 65/54%、骨盆控制 87/72%；>55 天每天 −0.6%（OS）／−0.7%（PC）。Route: Europe PMC REST
- **[S16] PASS** — Song S, Rudra S, Hasselle MD, et al. (2013). *The effect of treatment time in locally advanced cervical cancer in the era of concurrent chemoradiotherapy.* Cancer 119(2):325-331. PMID 22806897, doi 10.1002/cncr.27652. URL: https://doi.org/10.1002/cncr.27652 — 113 名 IB2–IIIB CCRT；近接完成 >56 天 → 骨盆復發 HR 3.8（1.2–16）、3 年 PF 26% vs 9%；建議 8 週內完成。Route: Europe PMC REST
- **[S17] PASS** — Chemoradiotherapy for Cervical Cancer Meta-Analysis Collaboration (CCCMAC). (2008). *Reducing uncertainties about the effects of chemoradiotherapy for cervical cancer: a systematic review and meta-analysis of individual patient data from 18 randomized trials.* J Clin Oncol 26(35):5802-5812. PMID 19001332, PMC2645100, doi 10.1200/jco.2008.16.4368. URL: https://doi.org/10.1200/jco.2008.16.4368 — 本組僅用「急性血液與腸胃毒性隨化放療增加；晚期毒性資料稀疏」一句；**療效數字（6%、HR 0.81）歸 B3**。Route: Europe PMC REST
- **[S18] PASS** — Kirwan JM, Symonds P, Green JA, et al. (2003). *A systematic review of acute and late toxicity of concomitant chemoradiation for cervical cancer.* Radiother Oncol 68(3):217-226. PMID 13129628, doi 10.1016/s0167-8140(03)00197-x. URL: https://doi.org/10.1016/s0167-8140(03)00197-x — 19 個試驗、4,580 隨機、毒性資料 1,766 人；G3–4 白血球 OR 2.15、血小板 OR 3.04、腸胃 OR 1.92。Route: Europe PMC REST
- **[S19] PASS** — Keys HM, Bundy BN, Stehman FB, et al. (1999). *Cisplatin, radiation, and adjuvant hysterectomy compared with radiation and adjuvant hysterectomy for bulky stage IB cervical carcinoma.* N Engl J Med 340(15):1154-1161. PMID 10202166, doi 10.1056/NEJM199904153401503. URL: https://doi.org/10.1056/nejm199904153401503 — 每週 40 mg/m²、至多 6 次、單週上限 70 mg；G3–4 血液 21% vs 2%、腸胃 14% vs 5%（n=183/186，bulky IB）。**療效 RR 歸 B3。** Route: Europe PMC REST
- **[S20] PASS** — Rose PG, Bundy BN, Watkins EB, et al. (1999). *Concurrent cisplatin-based radiotherapy and chemotherapy for locally advanced cervical cancer.* N Engl J Med 340(15):1144-1153. PMID 10202165, doi 10.1056/NEJM199904153401502. URL: https://doi.org/10.1056/nejm199904153401502 — GOG-120 的方案描述（cisplatin 40 mg/m²/週 ×6 週；納入條件 WBC≥3000、血小板≥10 萬、Cr≤2）。**療效數字歸 B3。** Route: Europe PMC REST
- **[S21] PASS** — Freifeld AG, Bow EJ, Sepkowitz KA, et al.; IDSA. (2011). *Clinical practice guideline for the use of antimicrobial agents in neutropenic patients with cancer: 2010 update by the Infectious Diseases Society of America.* Clin Infect Dis 52(4):e56-e93. PMID 21258094, doi 10.1093/cid/cir073. URL: https://academic.oup.com/cid/article/52/4/e56/382256 — 發燒與嗜中性球低下定義原文（≥38.3°C 單次口溫或 ≥38.0°C 持續 1 小時；ANC<500 或預期 48 小時內 <500；<100=profound）。Route: Europe PMC REST (TITLE) + WebFetch OUP 全文驗證原文（本次獨立重驗，非沿用 colon 簡報）。注意：academic.oup.com 對 curl 回 403，WebFetch 正常；IDSA 官方 landing page https://www.idsociety.org/practice-guideline/neutropenic-patients-with-cancer/ 僅載摘要
- **[S22] PASS** — Klastersky J, de Naurois J, Rolston K, et al. (2016). *Management of febrile neutropaenia: ESMO Clinical Practice Guidelines.* Ann Oncol 27(suppl 5):v111-v118. PMID 27664247, doi 10.1093/annonc/mdw325. URL: https://doi.org/10.1093/annonc/mdw325 — 指引級來源（書目已驗；無摘要）。Route: Europe PMC REST (TITLE)
- **[S23] PASS（僅書目層級）** — Bossi P, Antonuzzo A, Cherny NI, et al. (2018). *Diarrhoea in adult cancer patients: ESMO Clinical Practice Guidelines.* Ann Oncol 29(Suppl 4):iv126-iv142. PMID 29931177, doi 10.1093/annonc/mdy145. URL: https://doi.org/10.1093/annonc/mdy145 — 書目經 Europe PMC 驗證；**全文逐字（複雜性腹瀉定義、loperamide 劑量）在本環境取不到（見 S45）→ 文章只能引為「指引存在」，不得寫其中的數字門檻**。Route: Europe PMC REST
- **[S24] PASS** — Henson CC, Burden S, Davidson SE, Lal S. (2013). *Nutritional interventions for reducing gastrointestinal toxicity in adults undergoing radical pelvic radiotherapy.* Cochrane Database Syst Rev (11):CD009896. PMID 24282062, doi 10.1002/14651858.CD009896.pub2. URL: https://doi.org/10.1002/14651858.cd009896.pub2 — 飲食調整（脂肪/乳糖/纖維）減少放療末腹瀉 RR 0.66（0.51–0.87；4 試驗 413 人，中等品質）；老技術年代需謹慎解讀；元素飲食耐受差。Route: Europe PMC REST
- **[S25] PASS** — Wedlake L, Shaw C, McNair H, et al. (2017). *Randomized controlled trial of dietary fiber for the prevention of radiation-induced gastrointestinal toxicity during pelvic radiotherapy.* Am J Clin Nutr 106(3):849-857. PMID 28679552, doi 10.3945/ajcn.116.150565. URL: https://doi.org/10.3945/ajcn.116.150565 — 低纖 55／習慣 55／高纖 56；高纖組急性（療程末）與 1 年腸道症狀較好；原文「Restrictive, non-evidence-based advice to reduce fiber intake in this setting should be abandoned」。Route: Europe PMC REST
- **[S26] PASS** — Cisplatin injection 美國仿單（openFDA drug/label.json，SPL id bf489cd3-17a3-4398-ba7e-2cb9e87b9c13，set id 00396546-6a80-4b9f-a5f8-c22c1d1bb173，effective 2024-01-20）。DailyMed URL: https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=00396546-6a80-4b9f-a5f8-c22c1d1bb173 — boxed warning（累積腎毒性、骨髓抑制、噁心嘔吐、聽毒性、過敏樣反應）；腎毒性 28–36%（單次 50 mg/m²）、第二週顯現、腎功能未恢復不得再給；聽毒性至 31%（4,000–8,000 Hz）、每劑前聽力檢查建議；骨髓抑制 25–30%、nadir 第 18–23 天、多數第 39 天前恢復；水化 1–2 L／8–12 小時（傳統劑量脈絡）；不可用含鋁器材。**注意：仿單劑量脈絡是 50–100 mg/m² q3–4w，引用時逐項標註。** Route: openFDA API + DailyMed
- **[S27] PASS** — Hesketh PJ, Kris MG, Basch E, et al. (2017). *Antiemetics: American Society of Clinical Oncology Clinical Practice Guideline Update.* J Clin Oncol 35(28):3240-3261. PMID 28759346, doi 10.1200/JCO.2017.74.4789. URL: https://doi.org/10.1200/jco.2017.74.4789 — olanzapine 加入高致吐化療止吐組合、NK1 角色擴大。Route: Europe PMC REST
- **[S28] PASS** — Hesketh PJ, Kris MG, Basch E, et al. (2020). *Antiemetics: ASCO Guideline Update.* J Clin Oncol 38(24):2782-2797. PMID 32658626, doi 10.1200/jco.20.01296. URL: https://doi.org/10.1200/jco.20.01296 — 成人建議大致維持；olanzapine 5 mg 選項等。Route: Europe PMC REST
- **[S29] PASS** — Marnitz S, Schermeyer L, Dommerich S, et al. (2018). *Age-corrected hearing loss after chemoradiation in cervical cancer patients.* Strahlenther Onkol 194(11):1039-1048. PMID 30120496, doi 10.1007/s00066-018-1347-6. URL: https://doi.org/10.1007/s00066-018-1347-6 — 51 名、每週 cisplatin（累積至 400 mg）：62% 有 ≥20 dB 閾值變化（多在 ≥6,000 Hz），**年齡校正後無顯著聽損**、主觀聽力未受影響；作者：此族群不需常規聽力檢查。Route: Europe PMC REST
- **[S30] PASS** — Bacorro W, Baldivia K, Yu KK, et al. (2022). *Outcomes with definitive radiotherapy among patients with locally advanced cervical cancer with relative or absolute contraindications to cisplatin: A systematic review and meta-analysis.* Gynecol Oncol 166(3):614-630. PMID 35760651, doi 10.1016/j.ygyno.2022.06.018. URL: https://doi.org/10.1016/j.ygyno.2022.06.018 — 20 篇；carboplatin CRT 化療完成率 86% 但 5 年 OS 44%、效果不明確；相對禁忌者 cisplatin CRT 仍有效耐受可；多為間接比較。Route: Europe PMC REST
- **[S31] PASS** — Kirchheiner K, Nout RA, Tanderup K, et al. (2014). *Manifestation pattern of early-late vaginal morbidity after definitive radiation (chemo)therapy and image-guided adaptive brachytherapy for locally advanced cervical cancer: an analysis from the EMBRACE study.* Int J Radiat Oncol Biol Phys 89(1):88-95. PMID 24725693, doi 10.1016/j.ijrobp.2014.01.032. URL: https://doi.org/10.1016/j.ijrobp.2014.01.032 — 588 人；2 年 G≥3 3.6%、G≥1 89%、G≥2 29%、多數 6 個月內出現；狹窄最常見、其次乾澀。**狹窄專屬數字的使用權歸 D2。** Route: Europe PMC REST
- **[S32] PASS** — Suvaal I, Kirchheiner K, Nout RA, et al. (2023). *Vaginal changes, sexual functioning and distress of women with locally advanced cervical cancer treated in the EMBRACE vaginal morbidity substudy.* Gynecol Oncol 170:123-132. PMID 36682090, doi 10.1016/j.ygyno.2023.01.005. URL: https://doi.org/10.1016/j.ygyno.2023.01.005 — 113 名（陰道侵犯 ≤5 mm）；醫師評估變化在基線→第一次追蹤即顯著、之後不再顯著變化；多為輕度（約 20%，範圍 11–37%）；2 年 47% 無性活動。Route: Europe PMC REST
- **[S33] PASS** — Miles T, Johnson N. (2014). *Vaginal dilator therapy for women receiving pelvic radiotherapy.* Cochrane Database Syst Rev (9):CD007291. PMID 25198150, PMC6513398, doi 10.1002/14651858.CD007291.pub3. URL: https://doi.org/10.1002/14651858.cd007291.pub3 — 無可靠證據支持放療期間常規擴張；放療後觀察性資料顯示規律擴張與較低自述狹窄相關（因果未定）。Route: Europe PMC REST
- **[S34] PASS** — Kirchheiner K, Zaharie A, Smet S, et al. (2025). *Association Between the Regular Use of Vaginal Dilators and/or Sexual Activity and Vaginal Morbidity in Locally Advanced Cervical Cancer Survivors: An EMBRACE-I Study Report.* Int J Radiat Oncol Biol Phys 121(2):452-464. PMID 39278418, doi 10.1016/j.ijrobp.2024.09.011. URL: https://doi.org/10.1016/j.ijrobp.2024.09.011 — 存在性已驗（書目層級）；**內容數字歸 D2 使用，C4 僅指路**。Route: Europe PMC REST
- **[S35] PASS** — 衛生福利部（發布單位：國民健康署）。〈癌友抗癌不孤單 癌症資源中心與您相伴〉，建檔日期 110-08-18。URL: https://mohw.gov.tw/cp-5019-62797-1.html — 全國 82 家醫院設癌症資源中心；癌症希望基金會免付費諮詢專線 **0809-010580**（頁面原文已 grep 確認仍在）。**頁面日期 2021 年，引用時標年份。** Route: WebSearch → curl（--cacert 代理憑證）grep 原文
- **[S36] PASS** — 衛生福利部（國民健康署）。〈癌症資源中心 實體與網路服務並進 癌症照護新時代 抗癌路上不孤單〉，建檔 112-04-06、更新 113-03-21。URL: https://www.mohw.gov.tw/cp-6565-74177-1.html — 104 家醫院設癌症資源中心；台灣癌症資源網 https://www.crm.org.tw/ 。Route: WebSearch → curl grep 原文
- **[S37] PASS** — 衛生福利部中央健康保險署。「醫療服務給付項目」（全民健康保險醫療服務給付項目及支付標準之項目檔，114.01.01 生效、114.03.13 更新，XLS，5,996 項）。URL: https://www.nhi.gov.tw/ch/dl-82687-cdc462f073354eeb894cfeef692ecb32-1.xls （來源頁 https://www.nhi.gov.tw/ch/cp-5943-f1cce-2821-1.html ）— 近接治療項目原文：37007B 安裝近接治療器(複雜)每次 3,236 點、37008B(簡單) 1,650 點、37010B 組織插種治療 5,611 點、37018B 遙控後荷式近距治療(簡單)每次 4,126 點、37019B(複雜)每次 6,600 點；直線加速器 36011B/36012B 按照野計費；37047B 身體立體定位放射治療 213,662 點；37026B 放射治療之皮膚處理(一療程) 244 點；**全檔逐項檢索「強度調控／IMRT／modulated／arc／tomo」→ 放療章節無 IMRT/VMAT 專項**。Route: WebFetch 取得下載連結 → curl 下載 XLS → xlrd 逐列 grep
- **[S38] PASS** — 衛生福利部中央健康保險署。《全民健康保險藥品給付規定》第 7 節 消化系統藥物（114.07.24 更新版）。URL: https://www.nhi.gov.tw/ch/dl-42517-ca9cb4fbbf6646a183b01f8e021c7b06-1.pdf （章節索引頁 https://www.nhi.gov.tw/ch/np-3397-1.html ）— 7.2 止吐劑原文：致吐風險依 NCCN 最新版指引；7.2.1 serotonin antagonists 使用規範；7.2.2 NK1 拮抗劑（aprepitant/fosaprepitant）限高致吐化療、口服限 3 天每日 1 顆、注射限第一天；7.2.3 Akynzeo 規範。**全文 grep olanzapine＝0 筆。** Route: WebFetch 索引 → curl 下載 PDF → pdftotext → grep 原文
- **[S39] PASS** — 衛生福利部中央健康保險署。《全民健康保險藥品給付規定》第 9 節 抗癌瘤藥物（115.8.21 更新版）。URL: https://www.nhi.gov.tw/ch/dl-55685-99c675b771ab4b2789c891bc8db447ce-1.pdf — 9.2 Carboplatin 原文：「限 1.卵巢癌患者。2.腎功能不佳(CCr<60)或曾作單側或以上腎切除之惡性腫瘤患者使用。…」；**全節無 cisplatin 專屬條文（僅出現於其他藥之併用條文）**。Route: curl 下載 PDF → pdftotext → grep 原文
- **[S40] PASS** — 衛生福利部。〈104年2月起「身體立體定位放射治療」將納入健保給付，可縮短癌症病患治療療程。〉URL: https://www.mohw.gov.tw/cp-2636-21129-1.html — SBRT 健保給付範圍為原發性早期肺部及肝膽單一病灶、包裹給付 2 週 6 次內、約 21 萬點。Route: WebSearch → curl grep 原文
- **[S41] FAIL** — 台灣 IMRT/VMAT 用於子宮頸癌的健保給付／自費差額正式條文。已檢索：醫療服務給付項目 XLS 全檔（S37，無 IMRT/VMAT 專項）；支付標準頁 https://www.nhi.gov.tw/ch/lp-3778-1.html 與 https://www.nhi.gov.tw/ch/cp-5943-f1cce-2821-1.html （支付標準壓縮檔 zip 遭 Cloudflare challenge，curl 無法取得）；癌症低分次放療問答集 PDF（無 IMRT 內容）；行政院公報 110/111 年修正案 PDF（僅載修正項目）。**查無可引用條文，無論給付或自費**→ 文章寫「IMRT/VMAT 的申報與差額，向醫務課與個管師確認」
- **[S42] FAIL** — Cisplatin 在健保的「有給付」正式條文。藥品給付規定第 9 節無專屬條文（S39）；健保用藥品項檔（data.nhi.gov.tw）遭本環境 egress 政策阻擋；info.nhi.gov.tw 開放資料頁為 SPA 無法取得直接下載連結。→ 文章不得宣稱「健保給付 cisplatin」的條文細節；費用面寫「向醫務課確認」
- **[S43] FAIL** — 衛生福利部國民健康署 hpa.gov.tw 頁面（例：〈癌症資源中心 是癌友最堅強的後盾〉 https://www.hpa.gov.tw/Pages/Detail.aspx?nodeid=4809&pid=18609 ）。WebFetch 回 ROBOTS_DISALLOWED（robots.txt SSL 驗證失敗）；curl（含 --cacert 代理憑證）exit 60。與 colon 簡報 S73 同因，改以 mohw.gov.tw 頁面替代 [S35][S36]
- **[S44] FAIL** — CTCAE v5.0 官方 PDF（ctep.cancer.gov：Quick Reference 5x7 回應 0 byte；CTCAE_v5.0.pdf 回 HTML 錯誤頁）。→ 腹瀉／血尿等 CTCAE 分級門檻**不可憑記憶寫**；急症總表相關列以症狀描述呈現
- **[S45] FAIL** — ESMO 腹瀉指引（S23）全文逐字。annalsofoncology.org 對 curl 回 challenge、WebFetch 回 403；linkinghub 轉址後內容為空；esmo.org landing page 未找到對應 PDF。→ loperamide 劑量與複雜性腹瀉逐字定義不可寫
- **[S46] FAIL** — Olanzapine 用於化療止吐的台灣健保給付狀態。第 7 節止吐劑無此品項（S38）；第 1 節（神經系統藥物）未逐條檢索其止吐適應症條文。→ gap，寫「處方時向藥師確認給付或自費」
- **[S47] FAIL** — 陰道（外用）雌激素在台灣的健保給付條文。藥品給付規定第 15 節（婦產科製劑，114.07.24 版）已知存在（索引頁 S38 route），但本次未逐條下載檢索到 estriol/estradiol 陰道製劑之給付條文。→ gap，C4 寫「向婦產科醫師與藥師確認」
