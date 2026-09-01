# Brief C — 骨盆腔放射治療專題．療程中與之後（C1–C4）

研究員：Group C｜查證日期：2026-09-01
方法：期刊書目全部經 Europe PMC REST API（`EXT_ID:`／`DOI:"…"`／`TITLE:` 檢索，`resultType=core`）逐筆核對標題、作者、期刊、年卷期頁、PMID、PMCID、DOI、OA 狀態；凡標「全文逐字」者出自 Europe PMC `fullTextXML`（HTTP 200 實抓）或官方 PDF（`pdftotext -layout` 全文檢索）。PubMed 網頁有 CAPTCHA、NCCN 回 403 ——**兩條路徑一律未用**；照護指引改採 ESTRO／MASCC／BC Cancer／BSG／Cochrane 等可取得全文者。台灣端經 data.gov.tw dataset 9405 健保支付標準開放資料**全表實下載**（curl HTTP 200，565,406 bytes，ODS → odfpy 解析 6,012 個項目）、健保署 PDF 與行政院公報 PDF 全文檢索。
引用規則：**只有標 PASS 的來源可以進正文。** FAIL 條目保留紀錄，讓撰稿人知道查過什麼、哪些話只能寫「查不到可引用的來源」。

---

## ⚠ 動筆前必讀：七件與 SPEC 假設不同形狀的事

1. **紅線 4 的核心句有官方原文可抄，而且來自 2025 年的指引。** 英國腸胃學會（BSG）2025 年癌症治療腸胃副作用指引原文：「Once there is a clinical suspicion of a fistula it is crucial to **rule out disease recurrence before assuming that it is secondary to radiation injury**.」[S8] ——「廔管先當復發查，不要一開始就歸給放療」不是本專題自創的立場，是指引的話。C4 的紅線段不必自己立規矩。

2. **「腫瘤侵犯 vs 治療造成」的數字對比是現成的，而且差了一個數量級。** 同樣是子宮頸癌現代影像導引近接治療：
   - **全體世代**（含有器官侵犯者）5 年 G≥3 廔管 **3.2%**（95% CI 2.2–4.5，EMBRACE-I，n=1,251）[S16]
   - **排除膀胱侵犯者**之後，G≥2 膀胱廔管粗發生率 **0.7%**（EMBRACE-I，n=1,153）[S14]
   - **有膀胱侵犯者**膀胱陰道廔管 **12.8%**（5/43），且膀胱壁受侵高度 ≥20.3 mm 時 25%、≥31.1 mm 時 50%、≥41 mm 時 75%[S17]
   這三個數字放在同一段，紅線 4 的兩個方向就同時守住了：既不是「不用擔心」（3.2%／12.8% 都不是零），也不是「換技術就能避免」（**EMBRACE-I 用的就是最現代的 MRI 導引調控技術，3.2% 是那個技術下的數字**）。

3. **抽菸是本組最硬的可行動風險因子，而且在三個終點上都出現。** 廔管：現行抽菸 OR **5.14**（多變項，子宮頸癌化放療＋近接，n=150）[S18]；晚期腹瀉：抽菸與糖尿病 HR 1.4–7.3（EMBRACE-I，n=1,199）[S10]；急性毒性：BSG 原文「Smoking and low body mass index both increase the risk of toxicity and **should be addressed if possible before radiotherapy is given**」[S8]。C4 的收尾與 C2 的預告都可以扣在這裡。

4. **高壓氧的證據不是「有效／無效」二選一，是「兩個隨機試驗方向相反」。** 陽性：HORTIS-IV（Clarke 2008，n=120 可評估，雙盲假治療對照交叉）SOMA-LENT 改善 5.00 vs 2.61（p=0.0019）、臨床有反應 88.9% vs 62.5%、絕對風險降低 32%、NNT 3[S23]；RICH-ART（n=87 隨機，開放標籤）EPIC 泌尿總分改善差 10.1 分（95% CI 2.2–18.1，p=0.013）、NNT 3、五年仍維持[S25][S26]。陰性：HOT2（n=84，雙盲假治療對照，第三期）**主要終點兩項全部無差異**（腸道分數 p=0.50、直腸出血分數 p=0.092），作者原文「We found **no evidence** that patients … benefit from hyperbaric oxygen therapy」[S24]。Cochrane 2016 的結論原文只寫到「**may be justified** … in selected participants and tissues」[S27]。**寫成「有效」與寫成「沒用」都會被原文打臉。**

5. **飲食那格的證據方向，跨癌別版本比 rc-diarrhoea 更反直覺。** BSG 2025 的臨床指引第 29 條逐字：「29.1 Dietary counselling and/or protein supplementation may reduce the risk of toxicity during pelvic radiotherapy. 29.2 Lactobacilli±bifidobacteria containing probiotics may reduce acute RT-related diarrhoea. 29.3 **A high-fibre diet may reduce the risk of toxicity during pelvic radiotherapy.**」而同一份文件在正文裡對整批飲食介入（含低乳糖、低脂、要素飲食、纖維調整）下的判詞是：「There is sound scientific rationale for many of these interventions, but there are inadequate data to say which of them make a useful difference. They are all potentially burdensome and **should not be used outside the context of clinical trials**.」[S8] ——**指引點名的方向是高纖不是低渣**，但整體證據不足以推薦任何一種。這句要小心地寫（見 Claim ceiling）。

6. **C1 的「好發位置」有兩層可引來源，但都不是「鼠蹊、臀溝、會陰」這三個詞。** 可引的是：(a) CTCAE v5 grade 2 原文「patchy moist desquamation, mostly **confined to skin folds and creases**」（BC Cancer 分級表逐字）[S1]；(b) ESTRO 2025 原文：因照野淺，皮膚反應常見於「breast, head and neck, **anal, and vulvar cancer**」，且「obesity leading to skin folds will also increase the dose to the skin in the folds, exacerbating RID risk in the area」[S2]；(c) 直腸肛門癌統合分析：**腫瘤距肛門口 ≤5 cm** OR 2.86、**腫瘤侵犯皮膚** OR 36.0[S3]。**「臀溝」「鼠蹊皺摺」這兩個具體部位名，查無逐字可引的來源（FAIL-3）**——寫「皺摺處」「摩擦處」「照野越靠近肛門口越重」，不點名解剖構造清單。

7. **BC Cancer 指引裡有一條專門寫給骨盆腔病人的自我照顧句，而且在 grade 1 與 grade 2–3 都出現。** 原文逐字：「Patients receiving RT for **perineal/rectal cancer should use a sitz bath daily once RT begins**」[S1]。**注意：這與 rc-diarrhoea 已寫過的「沒有指引等級的證據支持坐浴能治療急性放射性直腸炎」不衝突——那句講的是治療直腸炎，這句講的是照顧皮膚**。C1 用這句時必須帶「這是皮膚照護的建議」的限定語，否則兩篇文章會被讀成互相打架（見 Caveats）。

---

## C1 `pel-skin`〈皮膚反應：會長在哪、怎麼顧〉

### Key facts

**發生率與分級（帶癌別／技術標籤，全部跨癌別）**

- 全放療族群量級（ESTRO 指引開篇句，原文逐字）：「Up to **95%** of cancer patients receiving radiotherapy will develop acute radiation-induced dermatitis (RID) in the treated area, either during or after the treatment course」[S2]。**這是全部位、全癌別的上限式敘述，不是骨盆腔專屬數字**，標籤不可省。
- **直腸／肛門癌（骨盆腔最可比的族群）**：系統性回顧與統合分析，50 篇、**n=4,892**——放射性皮膚炎總發生率 **58.7%**（95% CI 55.2–62.1）；**G≥3 為 12.3%**；**濕性脫屑 34.5%**[S3]。
- **肛門癌化放療（劑量最高的一格，隨機／前瞻對照）**：RTOG 0529 劑量繪製 IMRT，急性 **G3+ 皮膚 23%**，對照 RTOG 9811 的傳統技術 **49%**（p<0.0001）[S4]。**注意 RTOG 0529 的主要終點沒有達成**（G2+ 急性 GI/GU 兩者都是 77%）——引用皮膚那格時不可暗示「IMRT 全面較好」（與紅線 1 同向）。
- **單中心隨機試驗（肛管與直腸癌，n=63，護理門診追蹤）**：放射性皮膚炎**總發生率 100%**、**嚴重者 36.5%**、**17.5% 因皮膚炎中斷放療**[S6]。——這個 100% 是密集護理評估下的數字，與 58.7% 的差別是「看得多勤」，並列時必須解釋（見 Caveats）。

**時間軸（可引的錨只有三個，比 SPEC 預期的少）**

- 出現：BC Cancer 定義句逐字——「Reactions are evident **one to four weeks after beginning treatment** and can **persist for several weeks post treatment**」[S1]。
- 療程長度會拖長恢復：ESTRO 原文「Prolonged fractionation schedules **longer than 4–5 weeks will also delay the onset of RID recovery**」[S2]——骨盆腔多數是 5–6 週療程，這句正好用來預告「照完之後還要一段時間」。
- **比這更細的「第幾週會紅、第幾週會破、幾週後退乾淨」：查無骨盆腔專屬來源（FAIL-1）。** 乳房專題的「結束後約 2 週達峰」出自乳癌前瞻研究，**不可移用到骨盆腔**。

**好發位置（可引的三層，見「必讀」第 6 點）**

- CTCAE v5 grade 2 逐字：「patchy moist desquamation, mostly confined to **skin folds and creases**」；grade 3 逐字：「Moist desquamation in areas **other than skin folds and creases**」[S1]。→ **CTCAE 的分級本身就把「皺摺處」當成比較輕的那一級**，這件事對病人很有用：破在皺摺裡是 grade 2，破到皺摺以外才是 grade 3。
- ESTRO：肛門癌與外陰癌被點名為皮膚反應高風險癌別；肥胖造成的皮膚皺摺會增加該處皮膚劑量[S2]。
- 直腸肛門癌統合分析的風險因子（全部 p<0.05）：**腫瘤距肛門口 ≤5 cm OR 2.86；未做造口 OR 3.12；總劑量 >50 Gy OR 2.59；同步化療 OR 2.73；HIV 感染 OR 5.82；3D-CRT 相對 IMRT OR 8.76；腫瘤侵犯皮膚 OR 36.0**。劑量轉折點在 **50 Gy**，超過之後**每多 5 Gy，嚴重皮膚炎風險增加 29%**[S3]。

**照護的實證（逐項標等級）**

- **可以洗（指引層級已翻案）**：ESTRO 一般照護（Grade 0）原文：「Ensure good hygiene by **washing the skin daily**, preferably with lukewarm water and gentle drying of the treatment area」**QoE L1、Strong recommendation**；「The use of **deodorant is allowed unless the skin is broken**」**QoE L1、Strong recommendation**[S2]。BC Cancer 具體做法：溫水＋手掌輕洗、溫和無香精 pH 平衡皂、**不用毛巾搓**、軟毛巾拍乾[S1]。
  - 乳癌隨機試驗本體（洗澡 33%→14% 濕性脫屑）已在 rc-perineum 寫過並標明「做的是乳房與胸壁，搬到會陰是推論」——**本篇一句指路 rc-perineum，不重複舉證**。
- **骨盆腔專屬的一條**：BC Cancer 逐字「Patients receiving RT for **perineal/rectal cancer should use a sitz bath daily once RT begins**」[S1]（grade 1 與 grade 2–3 段落各出現一次）。
- **保濕**：ESTRO 逐字「Encourage the use of a **basic moisturiser from pre-treatment**」**QoE L4、Strong recommendation**[S2]。
- **敷料（grade 2 起）**：ESTRO grade 2 原文「Apply **self-adhesive soft silicone dressings** on the irradiated skin」**QoE L1、Strong recommendation**；grade 3「Apply soft silicone or other appropriate dressings on broken skin」**QoE L1**[S2]。**這是醫療端的處置，不是病人自己去買**（見紅線段）。
- **類固醇藥膏**：BC Cancer 逐字「Corticosteroid creams may be used sparingly for inflammation **as ordered by the physician**」[S1]；MASCC 2023 推薦 mometasone 與 betamethasone 用於**預防**[S5]。→ **處方決定，寫「可以跟你的放腫醫師討論」，不寫成病人自行購藥。**
- **MASCC 2023 的推薦清單（原文層級）**：達 75% 共識而獲推薦的**預防**介入只有六項——光生物調節（限乳癌）、Mepitel film（限乳癌）、Hydrofilm、mometasone、betamethasone、橄欖油；**處理**只推薦 Mepilex Lite 敷料；其餘「多數介入因證據不足、證據衝突或缺乏共識而不推薦」[S5]。**注意：Mepitel film 與光生物調節的共識僅限乳癌，骨盆腔不在推薦範圍**——這一條 rc-perineum 已寫過，本篇一句帶過並指路。
- **噴霧式皮膚保護膜（骨盆腔專屬的隨機證據）**：肛管與直腸癌 n=63 單盲隨機——使用噴霧式非灼燒性保護膜者，**出現「合併濕性脫屑」的機率較低、無濕性脫屑的時間較長**；但**兩組在嚴重度與中斷放療人數上沒有差異**[S6]。直腸肛門癌統合分析的網絡分析也把噴霧式保護劑排在第一（SUCRA 92.3%）、VMAT 相對 3D-CRT OR 0.29[S3]。→ 寫成「有一類產品在骨盆腔有隨機證據，但只贏在濕性脫屑那個終點」。

**濕性脫屑的分界（紅線段的本體，可逐字抄）**

- BC Cancer 的分級—行動對照原文：**GRADE 2 – GRADE 3 標為「URGENT: Requires medical attention within 24 hours」**[S1]。
- 臨床感染徵象四項逐字：「**fever／foul odour／purulent drainage／pain and swelling extending outside the treatment area**」[S1]。
- ESTRO grade 2 起：「Prevent and be aware of infections, **infections should be overseen by skin/wound care specialist**」QoE L4；「Use topical antiseptics and/or antibiotics **at any sign of infections**」QoE L3；「Prescribe adequate analgesia if required」QoE L4[S2]。

### Claim ceiling（C1）

- **可寫**：直腸肛門癌 58.7%／G≥3 12.3%／濕性脫屑 34.5%（帶「直腸與肛門癌、50 篇統合」標籤）[S3]；肛門癌 IMRT G3+ 皮膚 23% vs 傳統 49%[S4]；「一到四週出現、結束後可持續數週」[S1]；「CTCAE 把皺摺內的濕性脫屑列為 grade 2、皺摺以外才是 grade 3」[S1]；「腫瘤越靠近肛門口、劑量越高、同步化療，皮膚越難顧」（帶 OR）[S3]；「50 Gy 之後每多 5 Gy 風險 +29%」[S3]；「每天洗、可以用體香劑（乾燥完整皮膚上）」是指引 QoE L1 強推薦[S2]；「會陰／直腸放療每天坐浴」是 BC Cancer 的皮膚照護建議[S1]；「破皮＝24 小時內要讓醫療端看到」[S1]；感染四徵象逐字[S1]。
- **不可寫**：
  - 「第 X 週開始紅／第 Y 週最嚴重／照完 Z 週退乾淨」——骨盆腔的逐週劇本查無來源（FAIL-1）。**乳癌的「結束後 2 週達峰」不可挪用。**
  - 「臀溝與鼠蹊皺摺是最常破的兩個位置」——這兩個部位名查無逐字來源（FAIL-3）；只能寫「皺摺與摩擦處」。
  - 「用 XX 就不會破皮」——噴霧式保護膜那個隨機試驗裡**總發生率仍是 100%、嚴重者仍有 36.5%**[S6]。
  - 把 95% 寫成骨盆腔的數字（那是全部位敘述[S2]）；把 100% 寫成一般值（那是密集護理評估下的單中心數字[S6]）。
  - 把 Mepitel film／光生物調節寫成骨盆腔可用——MASCC 的共識**限乳癌**[S5]。
  - 類固醇藥膏寫成自行購用；敷料寫成病人自己貼（ESTRO 的 L1 推薦對象是醫療端）[S2]。
  - 任何一句可讀成「破皮自己敷就好」的話（紅線）。
- 會陰皮膚的深度（為什麼這裡最難顧、洗澡禁令的隨機試驗本體、MASCC 共識清單的完整討論）→ **一句指路 rc-perineum，不重寫**。

### Caveats（C1）

- 58.7%[S3] 與 100%[S6] 不是矛盾，是分母與評估密度不同（統合分析涵蓋各種通報方式 vs 單中心每次護理門診評估）。並列時必須寫出這句，否則讀者以為文獻在打架。
- BC Cancer 的坐浴建議是**皮膚照護**脈絡；rc-diarrhoea 已寫「查不到指引等級證據支持坐浴治療急性放射性直腸炎」。兩者相容但極易被讀成矛盾——C1 寫這一條時**必須明說「這是照顧皮膚的建議，不是治療腸子的方法」**，並在指路句裡把腸道那一半交給 C2／rc-diarrhoea。
- RTOG 0529 的皮膚數字亮眼，但**主要終點沒達成**[S4]；引用時要帶這一句，否則違反紅線 1 的反向（不可把技術差異寫大）。
- He 2026 統合分析中「3D-CRT vs IMRT OR 8.76」的 OR 極大，且統合來源異質性高——寫成「舊技術的皮膚反應明顯較重」的方向陳述，**不要把 8.76 當成個人風險倍數講**。
- ESTRO 文件本身在結論裡承認「identified a lack of high-level evidence, especially for agent-specific recommendations」[S2]——引用其 QoE 標籤時照抄等級即可，不要說「指引證實」。

### 台灣現況（C1）

- **健保有對應項目（2026-09-01 全表重新下載核對，備註逐字比 B 組版本更完整）**：**37026B「放射治療之皮膚處理（一個療程）」244 點**，生效 2004/07/01；備註原文「**1.以每週為一個療程（含括一週之治療次數）。2.申報時須註明所照部位範圍、劑量、次數。**」[S36]
  → **可寫**：「放療期間的皮膚處理在健保的診療項目表裡有自己的項目，是**以週計**的。」**不可推論成「所以敷料不用錢」或「所以自我照顧都有給付」。**
- **47047C「坐浴」53 點**（備註「泡盆（soaking）比照申報」）[S36]——與 BC Cancer 的坐浴建議可相互呼應，但**不可寫成「健保鼓勵坐浴」**（支付項目存在不等於臨床推薦）。
- **特殊功能敷料在放射性皮膚炎的給付身分：查無（FAIL-9）**。全表檢索「敷料」相關項目未見放射性皮膚炎適應症條文。寫法：「敷料的種類與費用各院不同，由醫療端評估後決定，費用問醫務課或放腫護理師。」

---

## C2 `pel-colitis`〈腸道反應：什麼時候來、怎麼過〉

### Key facts

**時間形狀（本篇最有價值的一段，指引原文逐字）**

- BSG 2025 逐字：「Acute GI symptoms usually **begin in the second week after starting radiotherapy**, tend to **peak in the last week of treatment** and **continue for at least 1–2 weeks after completion**.」[S8]
- 大分次的時間差（同段逐字）：「Treatment with **hypofractionated regimens means that acute symptoms may not start before treatment is completed**.」[S8] ——直腸癌短程五次的人，照完那天沒事、一週後才開始，這是**有指引原文可引的**。（rc-diarrhoea 已寫過此點；本篇是跨癌別版本，引同一份 2025 指引，論述角度改為「同一個骨盆腔、不同分次，難受出現在不同時間點」。）

**發生率與嚴重度（分癌別）**

- **子宮頸癌（現代影像導引，前瞻多中心 EMBRACE-I，n=1,199，中位追蹤 48 個月）**：晚期腹瀉粗發生率 **G≥2 8.3%、G≥3 1.5%**；**持續性 G≥1 佔 16%**、病人自評「相當困擾以上」持續者 7%[S10]。
- **子宮頸癌整體腸胃道（EMBRACE-I，n=1,199）**：**G≥3 肛門／直腸 2.8%、乙狀結腸 1.8%、結腸／小腸 2.3%**；G≥2 症狀中**腹瀉 8.5%、脹氣 9.9%** 最常見[S9]。
- **直腸癌的急性腹瀉逐週曲線**（rc-diarrhoea 已完整寫過：G≥2 腹瀉女性第一週 1.4%→第五週 33.3%、V45 劑量體積關係、IMRT 10.8% vs 3D-CRT 32.3%）——**本篇不重複，一句指路 rc-diarrhoea**。
- **攝護腺癌的急性與晚期腸道數字**（PACE-B、CHHiP、累積發生率 vs 盛行率的分辨）——**pc-bowel-urinary 已完整寫過，一句指路，不重建數字**。

**風險因子（帶出處）**

- EMBRACE-I 晚期腹瀉：病人端因子為**基線腹瀉、抽菸、糖尿病，HR 1.4–7.3**；治療端為處方劑量、V43 Gy、V57 Gy（淋巴結加強）與腹主動脈旁照射[S10]。
- 劑量的具體落差（同研究）：3 年 G≥2 腹瀉，處方 **45 Gy 為 9.5%、50 Gy 為 19.9%**；V43 Gy <2,500 cm³ 為 8.7%、>3,000 cm³ 為 14.0%；V57 Gy <165 cm³ 為 9.4%、≥165 cm³ 為 19.0%[S10]。
- EMBRACE-I 整體腸胃道：基線症狀、年齡增加、抽菸、低 BMI 都與症狀相關；治療端 rectum D2cm³、ICRU 直腸陰道參考點、bowel D2cm³ 與嚴重事件相關[S9]。
- BSG 逐字：「**Smoking and low body mass index both increase the risk of toxicity and should be addressed if possible before radiotherapy is given.**」[S8]

**飲食（見「必讀」第 5 點；這是本篇最容易寫錯的一段）**

- BSG 2025 臨床指引 29 條逐字：「29.1 **Dietary counselling and/or protein supplementation** may reduce the risk of toxicity during pelvic radiotherapy. 29.2 **Lactobacilli±bifidobacteria containing probiotics** may reduce acute RT-related diarrhoea. 29.3 **A high-fibre diet may reduce the risk of toxicity during pelvic radiotherapy.**」[S8]
- 同文件對整批飲食介入的判詞逐字：「Dietary modifications trialled include partial or complete replacement of normal nutritional intake with elemental diet, modified fat …, low lactose diets and modified fibre intake. **High fibre diets may be beneficial possibly by enhancing production of anti-inflammatory short chain fatty acids.** There is sound scientific rationale for many of these interventions, but **there are inadequate data to say which of them make a useful difference. They are all potentially burdensome and should not be used outside the context of clinical trials.**」[S8]
- **益生菌的安全但書**：rc-diarrhoea 已寫（免疫低下者的菌血症風險、白血球低下時先停）——**本篇一句指路，但不可省略但書**（BSG 的 29.2 沒有寫安全性，直接引 29.2 而不帶但書會變成鼓勵病人自行服用）。

**藥物與處置（急性期）**

- 止瀉藥：BSG 逐字「In patients developing acute diarrhoea, **stool analysis for infection should be performed; however, it is generally safe to start loperamide while awaiting the results. Reassess the patient regularly to exclude the development of toxic dilatation of the colon.**」[S8]
- 化療端的分界（逐字）：「**Grade 3 or 4 diarrhoea mandates chemotherapy to be stopped** with subsequent dose reduction if restarted.」[S8]
- 治療期間出現血便：BSG 逐字「Clinical experience suggests that it is prudent to **investigate rectal bleeding occurring during radiotherapy 6 weeks after treatment completion with flexible sigmoidoscopy** if no recent lower GI endoscopic or virtual colonoscopy has been performed.」[S8]
- 「把腸子推開」的物理手段：BSG 逐字「New approaches aimed at limiting toxicity through attempting to exclude the GI tract from the radiation field（**endorectal spacers, balloons, rectal emptying**）**have not improved GI outcomes**.」[S8]——**這一條要交叉給 A 組 A4（SpaceOAR）**，見〈給 SPEC 的修正建議〉第 4 點。
- 個人化介入的正向證據（同段）：單中心可行性隨機試驗，化放療期間由嵌入腫瘤科的多專科團隊快速檢查乳糖不耐、小腸細菌過度生長、膽鹽吸收不良並個別化飲食支持，**結果較佳**[S8]。

**感染性腹瀉的鑑別（C2 警訊段）**

- BSG 對放療族群明寫的是「先驗糞便、等結果期間可先用 loperamide、定期重評以排除毒性巨結腸」[S8]。
- **C. difficile 在放療（非移植）族群的頻率：BSG 的生理異常表格中 During radiotherapy／After radiotherapy 兩欄的 C. difficile 格填的是「?」，原文註明「'?' indicates that there are no published data and no clinical experience」**[S8]。→ **「放療病人有多少比例是 C. difficile」查無數字（FAIL-4）**，只能寫「腹瀉不一定都是放療造成的，糞便檢查是必要的一步」，**不可給比例**。
- 造血幹細胞移植族群才有明確句：「**Stool cultures should be obtained to exclude C. difficile infection before institution of antidiarrhoeal medications.**」[S8]——族群標籤不可省，**不可直接搬到放療病人身上當規則**。

### Claim ceiling（C2）

- **可寫**：「第二週開始、最後一週最難、照完至少再一到兩週」＋「大分次的人症狀可能到照完才開始」（兩句都是 BSG 原文）[S8]；子宮頸癌 EMBRACE-I 的 G≥2 腹瀉 8.3%／G≥3 1.5%／持續性 G≥1 16%[S10]；G≥3 依部位 2.8%／1.8%／2.3%[S9]；「45 Gy 與 50 Gy 差一倍」的劑量對照[S10]；抽菸與糖尿病是風險因子（HR 1.4–7.3）[S10]；「拉肚子先驗糞便、等結果時可以先吃止瀉藥、但要定期回來評估」[S8]；「第 3–4 級腹瀉時化療必須停」[S8]。
- **飲食那段的唯一安全寫法**：「指引裡對飲食下的判斷有兩層：**方向上點名的是高纖不是低渣**，但整體證據**不足以推薦任何一種飲食法，而且指引明說這些做法在臨床試驗之外不應使用**。所以最務實的一句是——你的飲食問你的營養師與治療團隊，不要照網路上的低渣清單自己執行到營養不良。」[S8]
- **不可寫**：
  - 「低渣飲食沒有用／低渣飲食有害」——指引沒有這樣寫，它寫的是證據不足以分辨哪一種有用[S8]。
  - 「多吃纖維可以減輕副作用」當成建議句——29.3 的措辭是 **may** reduce，而且同文件說不應在試驗外使用[S8]。這一格**必須把兩句並陳**。
  - 「X% 的放療腹瀉其實是 C. difficile」（FAIL-4）。
  - 把移植族群的「用止瀉藥前先驗 C. difficile」寫成放療族群的規則[S8]。
  - 直腸癌逐週曲線與 V45 的數字（rc-diarrhoea 主場，重複＝違反 SPEC §五）；攝護腺的累積發生率／盛行率討論（pc-bowel-urinary 主場）。
  - 「益生菌可以吃」不帶安全但書。
- 裡急後重、黏液便的**獨立頻率數字**：EMBRACE-I 是把 proctitis／bleeding／diarrhoea 分項報 G≥2，**「裡急後重」與「黏液便」沒有單獨的百分比（FAIL-5）**——寫症狀清單可以，不給比例。

### Caveats（C2）

- EMBRACE-I 是**子宮頸癌、化放療＋影像導引近接治療**的族群，數字不可當成「骨盆腔放療的通則」；每次引用都要帶癌別標籤[S9][S10]。
- 「第二週開始、最後一週達峰」是 BSG 的**臨床實務陳述**（practice guidance），不是統合分析的量化結果——證據等級標籤寫「指引的臨床實務陳述」。
- BSG 全文中對急性期處置的總評逐字是「The management of toxicity **remains empirical as evidence is lacking**」[S8]——寫任何一種急性期做法時都要在同段附近保留這句的意思。
- 「endorectal spacers/balloons 沒有改善腸胃道結果」這句是 BSG 對**急性毒性預防**脈絡下的敘述[S8]；A4 若引用，**不可讀成「SpaceOAR 對晚期直腸毒性也無效」**（那是不同終點、不同文獻，本組未查證）。

### 台灣現況（C2）

- 健保支付標準全表（6,012 項，2026-09-01 實下載）逐欄檢索：「**益生菌」0 筆、「止瀉」0 筆、「硫醣鋁／sucralfate」0 筆**[S36]。灌腸類項目有 47003C 大量灌腸、47004C 甘油球灌腸、**47006C 小量或留置灌腸 123 點**、47011C 清潔灌腸[S36]——**這些是處置碼，不是「類固醇灌腸／sucralfate 灌腸有給付」的證據，不可如此推論。**
- 下消化道內視鏡：**28013C S 狀結腸鏡檢查 1,069 點；28017C 大腸鏡檢查 2,363 點**（備註限消化內科、消化外科、大腸直腸外科、兒科消化學及小兒外科專科醫師執行）[S36]。
- 藥品給付（loperamide 等）不在本表範圍，**本組未查證，正文不碰**。

---

## C3 `pel-urinary`〈膀胱與解尿的那幾週〉

### Key facts

**急性期會有多少人不舒服、什麼時候來**

- **前瞻世代（骨盆腔跨癌別，巴西單中心，n=72；癌別組成：攝護腺 36%、直腸 31%、子宮頸 23%、子宮內膜 6%、肛管 4%）**：療程中**33%（24/72）出現新的或惡化的泌尿症狀**[S12]。
- **同一研究的「什麼時候來」（以累積劑量表示，非週數）**：症狀出現／惡化時的骨盆腔累積劑量分布——**<5 Gy 0%、6–15 Gy 8%、16–25 Gy 25%、26–35 Gy 25%、36–45 Gy 25%、46–55 Gy 4%、56–65 Gy 8%、>65 Gy 4%**[S12]。→ **四分之三的症狀出現在累積 16–45 Gy 之間**。
- 症狀組成（24 位有症狀者）：**解尿疼痛 83%（20/24）、夜尿 16%（4/24）、急尿 0%、血尿 0%**；治療前就有症狀者佔 49%，其中急尿 63%、夜尿 37%[S12]。
- **子宮頸癌晚期泌尿（EMBRACE-I，n=1,153，排除膀胱侵犯者，中位追蹤 48 個月）**：G≥2 **膀胱炎 8.8%、出血 2.7%、廔管 0.7%**[S14]；另一篇同世代：G≥2 **頻尿 13%、尿失禁 11%**；ICRU 膀胱點劑量 >75 Gy 者 5 年 G≥2 尿失禁由 11% 升到 20%[S14b]。
- 攝護腺癌的急性與晚期泌尿數字（PACE-B 12 週內 G≥2 GU 27% vs 23%、CHHiP 五年累積發生率、夜尿十二年 48%）——**pc-bowel-urinary 已完整寫過，一句指路，不重建**。

**放射性膀胱炎 vs 泌尿道感染（C3 的主場，兩個方向都有來源，而且互相拉扯）**

- **方向一（症狀多半不是感染）**：Xavier 2019 前瞻世代——24 位在療程中出現症狀者，**只有 1 位（全體 1.4%、症狀者中 4%）尿液培養陽性**；作者結論原文：「The incidence of UTI was **much lower than expected**, suggesting that **asymptomatic bacteriuria develops symptoms due to radiotherapy**.」該研究因感染率遠低於樣本數估計而**提前中止收案**[S12]。同研究的引言把問題講得最清楚：放療造成的頻尿、解尿疼痛、血尿「**may mimic the secondary symptoms of urinary tract infection**」，而社區女性常用的「有症狀就先給經驗性抗生素」做法「probably cannot be applied in individuals undergoing pelvic radiotherapy」[S12]。
- **方向二（不能因此就不驗）**：Shuford 2016（婦癌骨盆腔放療女性 n=134、241 份檢體，回溯）——**34.9%（84/241）的尿液培養有菌生長**；試紙的亞硝酸鹽或白血球酯酶任一陽性敏感度最高（91.7%）、兩者皆陽性特異度最高（95.5%）；**大腸桿菌只佔 22.6%**，且 **23.8% 對 TMP-SMX、16.7% 對 ciprofloxacin、11.1% 對 nitrofurantoin 抗藥**；作者結論：尿液分析在這個族群**準確度低於一般人群但仍有用**，強調必須做培養與藥敏[S13]。
- **兩篇不是矛盾，是分母不同**（Xavier 是前瞻、症狀觸發、排除已在用抗生素與有導尿管者；Shuford 是回溯、只納入「臨床已決定送檢」的檢體）——並列時必須寫這句。
- **可以寫給病人的結論**：療程中出現的頻尿、急尿、解尿痛，**大多數不是感染**；但**分辨的方法不是靠感覺，是驗尿加培養**；而且**經驗性抗生素在這個族群不是安全的預設**（抗藥比例不低）[S12][S13]。

**什麼情況要當天回來**

- 可引的支撐點：Dejonckheere 2026 對放射性膀胱炎的標準處置順序原文「standard measures such as **bladder irrigation, intravesical coagulation, or instillation**」[S15]——**沖洗與內視鏡電燒排在最前面，意味著血塊阻塞是要當場處理的事**。
- **「發燒＋解尿痛」「解不出尿」「血尿合併下腹脹痛」這三條逐字的病人端就醫指示：查無可直接引用的指引原文（FAIL-6）。** 寫法：以症狀邏輯陳述（血塊會塞住尿道、發燒代表可能有感染而放療期間常合併化療），**並明說這是臨床常識性的分界而非某份指引的條列**；或沿用 pc-bowel-urinary 已寫過的警訊清單並指路。
- **導尿與尿滯留的處置細節：本組未取得可引來源（FAIL-6 併記）**，正文不展開具體做法，寫「解不出來就當天回來，不要自己憋著等下次回診」。

### Claim ceiling（C3）

- **可寫**：「骨盆腔放療的病人裡，約三分之一在療程中會出現新的或變嚴重的泌尿症狀」（帶「跨癌別前瞻世代 n=72」標籤）[S12]；「四分之三的症狀出現在累積劑量 16–45 Gy 之間」[S12]；「有症狀的人裡，最多的是解尿疼痛（83%）」[S12]；子宮頸癌晚期 G≥2 膀胱炎 8.8%／出血 2.7%／廔管 0.7%[S14]、頻尿 13%／尿失禁 11%[S14b]；「症狀很像感染，但前瞻研究裡真的驗出感染的只有 1.4%」[S12]；「所以要驗尿；而且這個族群的抗藥比例不低，經驗性抗生素不是安全的預設」[S13]。
- **不可寫**：
  - **把 16–45 Gy 直接換算成「第 X 週」**——原文用的是累積劑量不是週數（FAIL-2）。可寫「大約落在療程的中段」，**不可給週次**。
  - 「放療期間的泌尿症狀都不是感染，不用驗尿」——這是把 Xavier 讀反了；同一份研究的方法就是**驗**出來的[S12]，而 Shuford 的 34.9% 陽性培養在另一個方向[S13]。
  - 「尿液試紙陰性就可以排除感染」——最高的陰性預測值是「無白血球」的 87.0%，不是 100%[S13]。
  - 「大腸桿菌是主因」——在這個族群只佔 22.6%[S13]。
  - 攝護腺癌的分次比較、IPSS 與晚期毒性的預測因子（pc-bowel-urinary 主場）。
  - 任何具體的導尿、尿滯留自我處置做法（FAIL-6）。
- 「血尿要當天回來」可寫，但**要標明這是依症狀邏輯（血塊會阻塞）給的分界，不是引自某份指引的條文**。

### Caveats（C3）

- Xavier 2019 樣本小（n=72）、單中心、**因結果與預期不符而提前中止**，作者自己也因此無法做預測因子分析[S12]——引用 1.4% 時必須帶這三個標籤，否則會被讀成「放療病人不會泌尿道感染」。
- Xavier 的族群六成是男性、以攝護腺與直腸癌為主[S12]；女性骨盆腔放療者的感染風險不能直接套用（Shuford 的族群才是婦癌女性）[S13]。
- EMBRACE-I 的膀胱數字**是在排除膀胱侵犯者之後算的**[S14]——這一點在 C4 是紅線 4 的關鍵，在 C3 也要標明，否則「0.7% 廔管」會被讀成所有子宮頸癌病人的數字（全體是 3.2%[S16]）。
- 「急尿 0%」是該研究 24 位有症狀者中的新發生率，且**該族群治療前就有急尿者已佔 63%**[S12]——不可寫成「放療不會造成急尿」。

### 台灣現況（C3）

- **28019C 膀胱鏡檢查 1,800 點**（1995/03/01 生效）；**50011C 膀胱灌注 260 點**（1995/03/01 生效，無備註條文）[S36]。
- **膀胱灌注液（特殊材料 D113-2）在出血性膀胱炎的事前審查條文**已由 pc-bowel-urinary 引用過（須「在傳統清血塊、電燒無效後，檢附照片及病歷經事前審查核准後使用」，每療程以六個月為限）——**本組未重新取得該附件全文，C3／C4 一句指路 pc-bowel-urinary，並提醒讀者現行版本問醫務課**（FAIL-10）。
- 尿液檢查與培養的健保身分：本組未逐項查證，正文不碰。

---

## C4 `pel-late`〈晚期出血與廔管：有哪些解方〉【紅線 4】

### Key facts — 晚期直腸出血

**發生率與時間窗（跨癌別，指引原文逐字）**

- BSG 2025 逐字：「**Rectal bleeding occurs in up to half of all patients treated with radiotherapy for a pelvic tumour.** It is often occasional and minor. **Severe bleeding which affects about 1% of patients after radical pelvic irradiation** may result in repeated need for hospitalisation, transfusion and severely affects quality of life.」[S8]
- 時間窗逐字：「People usually **start to notice intermittent bleeding a few months after the end of radiotherapy**. It usually **reaches a peak within 3 years**, sometimes then **persisting for 10 or more years**.」[S8]
- 機轉與劑量關係逐字：「The risk of bleeding is **directly related to the dose of radiotherapy delivered to the bowel wall**. Increased risks may occur in patients treated with **contact brachytherapy for early rectal cancers or brachytherapy for prostate cancer**. **Brachytherapy for cervix and endometrial cancers may move the site of maximum damage from the rectum to the sigmoid, or rarely, the small bowel.**」[S8]
- 分癌別的嚴重端數字：**子宮頸癌（EMBRACE-I，n=1,199）G≥3 肛門／直腸 2.8%、乙狀結腸 1.8%、結腸／小腸 2.3%**[S9]；**5 年 G≥3 腸胃道整體 8.5%**（95% CI 6.9–10.6）[S16]。**攝護腺癌的五年累積發生率／盛行率**→指路 pc-bowel-urinary。

**處置選項與各自的證據等級（逐條）**

| 處置 | 最高等級證據 | 結論原文／數字 | 已知傷害 |
|---|---|---|---|
| **先不處置＋衛教** | BSG 指引陳述 | 「If bleeding is not affecting quality of life and assessment has excluded underlying malignancy, the patient should be **reassured and the natural history of radiation-induced bleeding explained; intervention is not required**.」[S8] | — |
| **先排除復發、先做內視鏡** | BSG 指引陳述 | 「it **cannot be assumed that rectal bleeding after radiotherapy is caused by radiation-induced telangiectasia**」；診斷靠典型外觀，**「biopsy confirmation should not be performed」**[S8] | 切片本身是缺血組織上的傷口 |
| **調整排便、停抗凝血劑（若可停）** | BSG 指引陳述 | 「optimising irregular bowel function will often reduce bleeding」「Stopping anticoagulants/antiplatelet agents **if possible**」[S8] | — |
| **Sucralfate 灌腸** | BSG 指引陳述；Cochrane 收錄的隨機比較為**極低至低品質** | BSG：「Sucralfate enemas can be useful as a **temporary** treatment … or for long-term use in those with problematic bleeding unsuitable for disease-modifying therapy」[S8]；Cochrane：APC 後併用口服 sucralfate **反而**在內視鏡評分上不如 APC 加安慰劑（RR 2.26，95% CI 1.12–4.55，n=122，低至中品質）[S28] | — |
| **氬氣電漿凝固（APC）** | 無安慰劑對照隨機試驗；Cochrane 只收到 APC±sucralfate 的比較[S28] | BSG：「Argon plasma coagulation is **widely used** for bleeding radiation proctopathy.」[S8] | **BSG 逐字：「it carries a serious complication rate of up to 26%, including stricture formation, rectal pain, perforation and fistula formation」；且「Its use is absolutely contraindicated on the anterior rectal wall after prostate brachytherapy because of the high risk of fistula formation, which invariably then requires diversion of the bowel」**[S8] |
| **任何熱凝固治療（含射頻消融、雷射、band ligation）** | 觀察性 | BSG 逐字：「**Any thermal therapy risks causing deep, progressive or non-healing injury, because radiation proctopathy is an ischaemic condition.**」射頻消融「Initial data suggested a good response rate and no significant complications, but **no new data have been published … since 2015**」[S8] | 同上 |
| **Formalin（福馬林）** | **無安慰劑對照隨機試驗** | BSG 逐字：「Formalin has been used in **many observational single-arm studies and retrospective series with apparent effect**. However, there are **few long-term data, no placebo-controlled randomised trials** and a variety of techniques（濃度 3.6–15%）」[S8]；Cochrane：4% formalin 對 sucralfate-類固醇灌腸的比較有利於 formalin，但評為**極低至低品質**（n=102）[S28] | BSG 逐字：「Complications include **colitis, which can be prolonged and severe especially if formalin enters the submucosa, stricturing, perforation and pain**」[S8] |
| **Purastat（自組裝胜肽止血劑）** | 單一 21 人前瞻研究 | BSG 逐字：「In a **21 patient prospective study, the only published data**, Purastat led to significantly reduced bleeding in **three-quarters of patients at 1 year**」[S8] | 「has no recorded side effects」[S8] |
| **高壓氧（HBOT）** | **有隨機試驗，方向相反**——見下節 | Cochrane 2016 對放射性直腸炎的單一研究：改善或治癒 **RR 1.72（95% CI 1.0–2.9，p=0.04，NNTB 5）**[S27]；Cochrane 2016 late proctopathy 評 HBOT 那筆為**中等品質**（n=150，SOMA-LENT 改善 p=0.0019）[S28] | 見「高壓氧的傷害」段 |
| **腸胃科／護理師主導的演算法式照護** | 隨機（n=218），**低品質** | Cochrane：相對於自助手冊，腸胃科醫師主導 IBDQ-B 6 個月改善 MD 5.47（95% CI 1.14–9.81）、護理師主導 MD 4.12（0.04–8.19）[S28] | — |
| **Almagate 灌腸** | 單臂 59 人 | 90%（53/59）出血明顯減少、平均反應時間 12 天、長期成功率 69%[S32] | 「No adverse effects were found」（單臂、無對照）[S32] |

### Key facts — 晚期出血性膀胱炎

- **量級與時間窗**：Dejonckheere 2026（CA Cancer J Clin，OA 全文逐字）——放射性膀胱炎「currently affects an **estimated 5%–15% of patients**」；「Symptoms **typically emerge 2 years after primary treatment**, and the risk **increases significantly with radiation doses >60 grays**」[S15]。RICH-ART 論文的引言則寫「affecting approximately **5–10%** of patients」[S26]。→ **兩個區間並存，寫成「文獻的估計落在 5% 到 15% 之間」是誠實寫法。**
- **子宮頸癌現代技術的分項數字**：EMBRACE-I（排除膀胱侵犯者）G≥2 **出血 2.7%、膀胱炎 8.8%**；膀胱 D2cm³ 與三個終點都相關；D2cm³ 由 75 Gy 增到 80 Gy，4 年 G≥2 膀胱炎由 **8% 升到 13%**[S14]。全體 5 年 G≥3 泌尿 **6.8%**（95% CI 5.4–8.6）[S16]。
- **處置順序（原文）**：「standard measures such as **bladder irrigation, intravesical coagulation, or instillation（e.g., with hyaluronic acid）**」，難治者再考慮 HBOT[S15]。
- **內視鏡能量凝固（narrative review，10 篇、n=137–139）**：**84.7%（116/137）單次治療後血尿緩解**，無血尿中位／平均間隔 **11–16 個月**；**4.4%（6 人）無反應而接受膀胱切除或尿路改道**；**總不良事件 21.6%（30/139）**，含儲尿期症狀、再出血、膀胱結石、尿滯留[S30]。
- **整體評價**：BJU 2023 回顧原文——「**There is no standard of care** for patients with HC, although existing strategies including fulguration, hyperbaric oxygen therapy, botulinum toxin A, and other intravesical therapies have demonstrated **short-term efficacy in cohort studies**」[S31]。
- **HBOT 在膀胱那格的定位（原文）**：Dejonckheere 逐字——「HBOT **can be offered** to patients with late radiation-induced cystitis and **should be preferred over urinary diversion, bladder embolization, or cystectomy**, both of which potentially could lead to further deterioration of quality of life. Early referral and initiation seem beneficial because there are signs of improved efficacy with **short intervals（i.e., within 6 months）between hematuria onset and HBOT**.」；並註明「HBOT is **approved by the US FDA** in patients with **radiation-related** hemorrhagic cystitis, but **not** in those with chemotherapy-related hemorrhagic cystitis」[S15]。→ **栓塞在這份回顧裡是被排在高壓氧之後的選項，不是首選。**

### Key facts — 高壓氧：隨機試驗逐條核對（紅線 4 的第二個重點）

| 試驗 | 年 | 對象 | 設計 | n | 介入 | 結果 |
|---|---|---|---|---|---|---|
| **HORTIS-IV**（Clarke 2008） | 2008 | 難治性放射性直腸炎（醫療與內視鏡處置皆失敗） | 隨機、**假治療對照、雙盲、交叉** | 226 評估／150 納入／**120 可評估** | 2.0 ATA vs 1.1 ATA 空氣，30–40 次、每次 90 分 | SOMA-LENT 改善 **5.00 vs 2.61（p=0.0019）**；臨床有反應 **88.9% vs 62.5%（p=0.0009）**；**絕對風險降低 32%、NNT 3**；交叉之後差異消失[S23] |
| **HOT2**（Glover 2016） | 2016 | 骨盆腔放療後 ≥12 個月、且經 ≥3 個月最佳藥物治療仍持續的慢性腸道功能障礙 | 隨機 2:1、**假治療對照、雙盲、第三期** | 84 | 2.4 ATA vs 1.3 ATA，40 次、每次 90 分、8 週 | **兩個主要終點皆無差異**：IBDQ 腸道分數中位改變 4 vs 4（p=0.50）；直腸出血分數 3 vs 1（p=0.092）。結論原文：「**We found no evidence that patients … benefit from hyperbaric oxygen therapy. These findings contrast with evidence used to justify current practices, and more level 1 evidence is urgently needed.**」[S24] |
| **RICH-ART**（Oscarsson 2019） | 2019 | 骨盆腔放療 ≥6 個月前完成、EPIC 泌尿分數 <80 的慢性放射性膀胱炎 | 隨機 1:1、**開放標籤（無盲）**、phase 2–3 | 87 隨機／79 ITT | 240–250 kPa，30–40 次、每次 80–90 分 vs 標準照護 | EPIC 泌尿總分改善差 **10.1 分（95% CI 2.2–18.1，p=0.013）**；**NNT 3（95% CI 2–5）**；EPIC 腸道分數也改善（差 8.3 分，p=0.024）；**41%（17/41）出現暫時性 grade 1–2 視覺與聽覺不良事件**[S25][S15] |
| **RICH-ART 五年追蹤**（Oscarsson 2025） | 2025 | 同上（對照組後續可交叉接受 HBOT） | 次要終點 | 70 可追蹤 | 同上 | 全體 EPIC 泌尿總分改善 18.0 分（6 個月）→ **19.1 分（5 年）維持**；**有反應者 48/70（68.6%）**，五年仍維持 +22.9 分；**無反應者 22/70（31.4%）從頭到尾沒有改善**；**12.8%（9/70）因症狀復發需再做一輪**；因經費不足**提前 6 個月終止追蹤**[S26] |
| **HORTIS-III**（放射性膀胱炎） | — | — | 隨機 | — | — | **提前結束、無結果可引**（Dejonckheere 原文：「the HORTIS-III trial（investigating radiation cystitis; ISRCTN19501634）**closed early**」）[S15] |

**回顧與統合層級**

- **Cochrane 2016（Bennett，14 試驗、753 人）結論原文**：「These small trials suggest that for people with LRTI affecting **tissues of the head, neck, anus and rectum, HBOT is associated with improved outcome**. … There was **no such evidence of any important clinical effect on neurological tissues**. **The application of HBOT to selected participants and tissues may be justified. Further research is required to establish the optimum participant selection and timing of any therapy. An economic evaluation should be undertaken.**」；放射性直腸炎那一格為單一研究：改善或治癒 **RR 1.72（95% CI 1.0–2.9，p=0.04，NNTB 5）**；並註明「These trials **did not report adverse events**」[S27]
- **Cochrane 2016（van de Wetering，16 試驗、993 人）**：把 HBOT 那筆評為**中等品質（moderate-quality）**，是整份回顧裡等級最高的幾筆之一；作者結論原文：「Although some interventions … look promising（including rectal sucralfate, metronidazole added to an anti-inflammatory regimen, and hyperbaric oxygen therapy），**single small studies provide limited evidence**.」[S28]
- **BSG 2025 對兩個相反結果的判詞（逐字）**：「A meta-analysis and a separate Cochrane review suggest significant benefit of treatment with hyperbaric oxygen (HBO). **Data from randomised trials are contradictory.** The underpowered HOT2 study showed no statistically significant benefit (p=0.09) compared with sham treatment in rectal bleeding, while the HORTIS IV study demonstrated greater healing in patients receiving HBO versus sham therapy. **Clinical experience suggests that little benefit is seen until patients have completed at least 30 sessions of HBO. Lower-pressure HBO as used in chambers treating people with multiple sclerosis is probably ineffective to treat radiation-induced injury.**」[S8]
- **Dejonckheere 2026 對 HOT2 與 HORTIS-IV 差異的解釋（逐字）**：「The reason for this discrepancy is thought to be related to **patient selection（overall milder symptoms and longer intervals after radiotherapy）and choice of the end point（an unvalidated instrument）in HOT2**.」並指出「Based on a large body of equivocal, retrospective evidence in addition to the well designed RICH-ART and HORTIS-IV trials, the **Multinational Association for Supportive Care in Cancer guideline currently recommends the use of HBOT as an effective way to treat radiation-induced proctitis** in patients with pelvic malignancies.」[S15]（**MASCC 該條指引原文本組未直接取得，見 FAIL-8——只可寫成「有回顧文章轉述 MASCC 有此推薦」，不可寫成「MASCC 指引指出」**。）
- **單臂統合（證據等級最低的一格）**：Yuan 2020（骨盆腔癌症，改善率為單臂彙總）——直腸出血改善率 **0.81（95% CI 0.74–0.89）**、腹瀉 **0.75（0.61–0.90）**、疼痛 **0.58（0.38–0.79）**；結論原文「HBO treatment **might have the potential** to alleviate … but **more data are needed for further conclusions**」[S29]。

**高壓氧的傷害與實務條件（誠實段，全部 Dejonckheere 2026 全文逐字）**[S15]

- 副作用發生率表：**近視（多為暫時性）25%–100%**（依定義而異，約每週 0.25 屈光度、停止後可完全恢復但**可能要到 12 個月**）；**中耳氣壓傷 2%–3%**；肺氣壓傷罕見；**氧中毒（可表現為癲癇）約每 2,000–3,000 次治療 1 次**；幽閉恐懼、低血糖、高血壓、急性肺水腫皆罕見（<0.5%）。「The probability of developing adverse reactions is **higher with an increasing number of treatment sessions（usually >10）and pressures above 2.0 ATA**.」
- 絕對禁忌：未處理的氣胸、眼內氣體（非緊急適應症）。相對禁忌：氣喘、慢性阻塞性肺病、嚴重幽閉恐懼；植入式裝置需向廠商確認相容性。
- **與抗癌藥的交互作用**：bleomycin（肺毒性，需無明顯肺毒性且間隔 3–4 個月）、doxorubicin（心毒性，間隔 3 天）、cisplatin（不與 HBOT 並行，尤其在傷口癒合適應症）；「There is a **lack of experience** when combining newer antineoplastic agents（e.g., immunotherapies, targeted therapies）with HBOT.」
- **可近性的誠實句（逐字）**：「HBOT does remain **unevenly available** across regions and health care systems; the need for specialized equipment, trained personnel, and multiple treatment sessions poses logistical and financial barriers … **In many health care settings, HBOT is not routinely reimbursed or remains restricted to very specific indications only, further limiting accessibility.**」
- 療程規模（可寫給病人的「要花多少時間」）：各試驗皆為 **30–40 次、每次 80–120 分鐘、通常每週五天**[S15][S23][S24][S25]。

### Key facts — 廔管（紅線 4 的核心）

**發生率：三組數字必須並陳**

| 族群 | 數字 | 出處 |
|---|---|---|
| 子宮頸癌，現代化放療＋MRI 導引調控近接治療，**全體**（n=1,251，中位追蹤足以算 5 年） | **5 年 G≥3 廔管 3.2%（95% CI 2.2–4.5）**；同世代 5 年 G≥3 腸胃 8.5%、泌尿 6.8%、陰道 5.7%；**器官相關 G≥3 合計 18.4%**、全終點合計 26.6%；**13 位治療相關死亡（8 位與腸胃道相關）** | EMBRACE-I[S16] |
| 同世代但**排除膀胱侵犯者**（n=1,153） | **G≥2 膀胱廔管粗發生率 0.7%** | EMBRACE-I[S14] |
| 子宮頸癌**有膀胱侵犯者**（n=43，1999–2015，中位追蹤 67.4 個月） | **膀胱陰道廔管 12.8%（5/43）**；5 例中 3 例在治療後 1 年內、2 例在 16.7 與 64.5 個月；多變項中唯一顯著預測因子是**MRI 上膀胱壁受侵高度**：**≥20.3 mm 時 25%、≥31.1 mm 時 50%、≥41 mm 時 75%** | Kim 2025[S17] |
| 子宮頸癌化放療＋近接治療單中心（n=150，2013–2022，中位追蹤 20 個月） | **廔管 13/150＝9%**；13 人中 **8 人（62%）症狀後來緩解**；2 年整體存活 72.0%、無廔管存活 91.6% | Ali 2025[S18] |
| 攝護腺癌放療後的泌尿廔管（外照射 30%／近接 30%／併用 40%，n=20 符合納入條件） | **80% 是直腸到泌尿道的廔管**、平均直徑 3.2 cm；**所有達到症狀緩解的直腸尿道廔管病人都需要尿路與糞便雙改道** | Chrouser 2005[S22] |

**風險因子（每條帶出處與效應量）**

- **腫瘤本身侵犯／期別**：FIGO **IVA 期 OR 6.87（95% CI 1.99–23.75，p=0.002）**、腫瘤體積較大 OR 3.29（1.53–7.08）[S19]；疾病侵入膀胱 OR 3.99（1.27–12.53，單變項）[S18]；膀胱壁受侵高度是唯一的多變項預測因子[S17]。
- **抽菸**：現行抽菸**單變項 OR 8.37（2.58–27.22，p<0.001）、多變項 OR 5.14（1.43–18.48，p=0.012）——是該研究多變項中唯一顯著者**[S18]。
- **低 BMI／營養**：BMI <20 kg/m² OR 4.33（1.11–16.90）[S19]；BMI 較高與廔管風險較低相關（OR 0.90，0.82–1.00）[S18]。
- **免疫功能低下**：OR 5.84（1.32–25.91）[S19]。
- **中重度貧血**（慢性放射性直腸炎族群，n=59，93.1% 為婦癌）：與後續發生**直腸深潰瘍或廔管**顯著相關（p=0.015）[S32]。
- **抗血管新生藥物（bevacizumab）**：
  - 統合分析（4 個世代研究、597 位曾接受骨盆腔放療的子宮頸癌病人）：**腸胃道廔管／穿孔 OR 4.03（95% CI 1.76–9.20）、泌尿道廔管／穿孔 OR 4.71（1.51–14.70）**[S21]。
  - 日本上市後監測（n=142，其中 64.1% 曾接受放療）：**6 位病人發生 7 處骨盆腔廔管＝4.2%（95% CI 1.56–8.96），六位全部有骨盆腔照射史**，其中 5 位還做過骨盆腔手術；3 位膀胱與直腸累積劑量高、**其中 2 位曾為骨盆腔復發接受救援性再照射**[S20]。
- **再照射**：僅在上述上市後監測的病例系列中被點名（2/6）[S20]；**未取得可引的再照射廔管發生率（FAIL-7）**。
- **手術史**：上市後監測 6 位中 5 位有骨盆腔手術史[S20]；系統性回顧原文「**higher complication rates and diminished healing in irradiated patients compared to non-irradiated counterparts**」[S34]。
- **放療後的器械操作（本組最被低估的一條）**：Chrouser 2005——**發生直腸廔管者 81% 有以下病史之一：直腸狹窄、尿道狹窄、直腸切片、直腸氬氣光束治療或放療後經尿道攝護腺刮除**[S22]；BSG 逐字：APC「absolutely contraindicated on the anterior rectal wall after prostate brachytherapy because of the high risk of fistula formation」[S8]；BSG 對放射性直腸炎的診斷原則逐字：「**biopsy confirmation should not be performed**」[S8]。
- **糖尿病**：在 EMBRACE-I 中是**晚期腹瀉**的風險因子（HR 1.4–7.3）[S10]；**廔管終點的糖尿病效應量：本組未取得可引來源（FAIL-7 併記）**——**不可把腹瀉的 HR 挪用到廔管**。

**「腫瘤造成的」與「治療造成的」怎麼分（紅線 4 的靈魂）**

- **BSG 2025 逐字（最重要的一句）**：「**Once there is a clinical suspicion of a fistula it is crucial to rule out disease recurrence before assuming that it is secondary to radiation injury.**」[S8]
- BSG 對整體頻率與趨勢的逐字判斷：「Gastrointestinal fistulae are a **relatively rare complication of radiotherapy and their incidence is probably decreasing owing to changes in its delivery**. They may occur in **any part of the GI tract** … They can present **acutely or many years later**.」[S8]
- **可據此建立的「兩條路」寫法（每一格都有出處）**：
  - **腫瘤本身走出來的洞**：腫瘤原本就長在器官壁上（IVA 期、侵犯膀胱或直腸），治療讓腫瘤退掉之後，原來被腫瘤佔住的地方就是一個洞。證據：有膀胱侵犯者 12.8% vs 排除侵犯者 0.7%[S17][S14]；侵犯高度愈高、機率愈高[S17]；IVA 期 OR 6.87[S19]。
  - **治療造成的洞**：現代技術下仍有 3.2%（5 年 G≥3，全體）[S16]；風險因子是抽菸、營養、免疫、抗血管新生藥物、放療後的器械操作[S18][S19][S21][S22]。
  - **第三種可能，而且必須先排除**：復發[S8]。
- **BSG 的處置原則（可寫成「這件事怎麼被處理」，不寫成「怎麼治好」）逐字**：(a) 積極處理敗血症（放射線或手術引流＋抗生素）；(b) 治療前必須先弄清楚廔管的解剖（哪些腸段與器官被牽連）；(c) **手術前必須先把營養狀態調整好**；(d) 矯正手術的目標是斷開廔管、恢復腸道完整並盡量少切腸子，「**Multiple operations and the judicious use of stomas may be required. The use of normal, non-irradiated tissue to fashion repairs helps to ensure an adequate blood supply. These often complex operations require multidisciplinary surgical expertise and carry a high risk of prolonged morbidity.**」；「**Rarely, there may be a role for non-operative therapies such as hyperbaric oxygen therapy.**」[S8]
- 修補成績的誠實數字：直腸尿道廔管系統性回顧（10 篇、>500 人）原文——**「higher complication rates and diminished healing in irradiated patients … irradiated individuals frequently required additional surgeries or definitive urinary diversion」**[S34]；多中心世代（n=72）：**晚發型廔管的最終完全癒合率 42.9%，明顯低於早發型的 83.8%（p<0.005）；30% 的病人最後需要永久性結腸造口，晚發型組更高（48.5% vs 13.5%，p=0.001）**[S35]。

**追蹤的理由（可接 C4 收尾）**

- BSG 逐字：「There is an **increased risk of a radiation-induced gastrointestinal tract cancer** in patients, **starting 5–10 years after pelvic radiotherapy**. Patients should be encouraged to take part in screening programmes, if fit enough, **every 5 years after their radiotherapy**.」[S8]

### Claim ceiling（C4）

- **可寫（出血）**：「骨盆腔放療後**最多一半的人會有直腸出血，多半偶發且量少；嚴重出血約佔 1%**」（帶「BSG 2025 指引陳述」標籤）[S8]；「通常在結束後幾個月開始注意到、三年內達到高峰、有時持續十年以上」[S8]；子宮頸癌 G≥3 依部位 2.8%／1.8%／2.3%[S9]、5 年 G≥3 腸胃 8.5%[S16]；「近接治療會把最容易受傷的位置從直腸移到乙狀結腸」[S8]。
- **可寫（膀胱）**：「文獻估計 5%–15%（另一份寫 5%–10%）」[S15][S26]；「症狀通常在治療後兩年左右浮現，>60 Gy 風險明顯上升」[S15]；EMBRACE-I 的 2.7%／8.8%／劑量對照[S14]；內視鏡能量凝固 84.7% 單次緩解、11–16 個月不再血尿、**但不良事件 21.6%、4.4% 最後仍要切膀胱或改道**[S30]；「這一格**沒有標準治療**」（BJU 回顧原文）[S31]。
- **可寫（高壓氧）**：上表五個試驗逐條（含 HOT2 的陰性結論原文）[S23][S24][S25][S26][S15]；Cochrane 兩份的結論原文與品質評等[S27][S28]；BSG 的「隨機試驗結果互相矛盾」「至少要做滿 30 次才看得到效果」「低壓艙大概無效」三句[S8]；副作用表全部[S15]；「30–40 次、每次 80–120 分鐘、通常每週五天」的療程規模[S15]；美國 FDA 對放射相關出血性膀胱炎的核准／對化療相關者未核准[S15]。
- **可寫（廔管，紅線 4）**：上表四列發生率（每一列都帶族群標籤）；抽菸 OR 5.14／8.37[S18]；IVA 期 OR 6.87、BMI<20 OR 4.33、免疫低下 OR 5.84[S19]；膀胱壁受侵高度的三個門檻[S17]；bevacizumab 的 OR 4.03／4.71[S21] 與 4.2% 上市後監測[S20]；放療後器械操作 81%[S22]；APC 在攝護腺近接治療後前壁「絕對禁忌」[S8]；「先排除復發」原文[S8]；晚發型廔管癒合 42.9%、30% 需永久造口[S35]。
- **不可寫（紅線 4 的兩個方向）**：
  - **「用了 IMRT／影像導引／質子就不會有廔管」——EMBRACE-I 就是最現代的技術，5 年 G≥3 廔管仍是 3.2%[S16]。** 技術能寫的最大限度是 BSG 那句「incidence is **probably** decreasing owing to changes in its delivery」[S8]，**要照抄 probably**。
  - **「廔管很罕見，不用擔心」**——3.2%[S16]、9%[S18]、有器官侵犯者 12.8%[S17]，且 EMBRACE-I 有 13 位治療相關死亡[S16]。
  - 「高壓氧可以治好放射性直腸炎／膀胱炎」——HOT2 是雙盲假治療對照的第三期陰性試驗[S24]；RICH-ART 是**開放標籤無盲**[S25]；RICH-ART 五年裡**31.4% 從頭到尾沒有反應**[S26]；Cochrane 的措辭只到 **may be justified**[S27]。
  - 「MASCC 指引推薦高壓氧治療放射性直腸炎」——**本組未取得該指引原文（FAIL-8）**；只能寫「有 2026 年的回顧文章轉述 MASCC 有此推薦」並標明是轉述。
  - 「氬氣電漿凝固是標準做法」——無安慰劑對照隨機試驗，且 BSG 明寫嚴重併發症率**高達 26%**、在攝護腺近接治療後的前壁是**絕對禁忌**[S8]。
  - 「福馬林很有效」——BSG 明寫**沒有安慰劑對照隨機試驗**、併發症含腸炎、狹窄、穿孔[S8]。
  - 「栓塞是選項之一」寫成中性並列——Dejonckheere 把 HBOT 放在膀胱切除與**栓塞之前**[S15]；栓塞要寫成後線。
  - 把糖尿病寫成廔管的風險因子並附數字（本組只有腹瀉終點的 HR[S10]，FAIL-7）。
  - 再照射給具體的廔管發生率（FAIL-7）。
  - 攝護腺癌放療後直腸尿道廔管的**發生率百分比**——最接近的一篇摘要中的數字有明顯排版損毀（「their prevalence ranges from 0.03 in various series」，區間下限缺失），**不可引用該數字**（FAIL-5）。
  - 推薦任何特定院所或高壓氧中心（SPEC 紅線）。
- **收尾的可行動句（有出處、且是紅線 4 允許的方向）**：抽菸是廔管多變項裡唯一顯著的因子[S18]，也是急性毒性應在放療前處理的兩件事之一[S8]；營養與 BMI 同樣在兩端出現[S18][S19]；放療後任何要在照射過的腸子或膀胱上動刀動燒的處置，都要讓做的人知道你照過放療[S8][S22]。

### Caveats（C4）

- **EMBRACE-I 的 3.2% 與 0.7% 分母不同**：3.2% 是全體（含器官侵犯者）的 5 年 actuarial G≥3 廔管[S16]；0.7% 是**排除膀胱侵犯者**後的 G≥2 膀胱廔管**粗發生率**（crude），不是 actuarial，也只算膀胱那一種[S14]。並列時**必須說明是不同分母與不同計算方式**，否則會被讀成矛盾。
- Ali 2025 的 9% 是單中心、中位追蹤只有 20 個月[S18]；Kim 2025 的 12.8% 是 43 人、1999–2015 的舊技術年代[S17]——兩者都不能當成「現在的機率」。
- Clarke 2008 的假治療組用的是 1.1 ATA 空氣，**假治療組本身也有顯著改善**（Dejonckheere 原文：「in some trials（e.g., HORTIS-IV），the sham effect resulted in a **significant improvement** of symptoms」[S15]）——寫 88.9% vs 62.5% 時，62.5% 那個數字也要出現。
- HOT2 的作者自己標註為 underpowered（BSG 用詞）[S8]；Dejonckheere 認為差異來自病人選擇與未經驗證的評估工具[S15]。**兩種解釋都要寫，不可只寫對高壓氧有利的那一種。**
- Yuan 2020 的「改善率 0.81」是**單臂彙總比率，不是與對照的比較**[S29]——證據等級標籤絕不可省，且不建議在正文使用（容易被讀成八成有效）。
- 內視鏡能量凝固的 84.7% 出自 narrative review 彙總的 10 篇小型研究（n=137）[S30]，非隨機。
- Chrouser 2005 是 51 人中篩出 20 人的病例系列，**沒有分母、不能算發生率**[S22]；它的價值在「81% 有放療後器械操作史」這個關聯，不在比例。
- 「廔管發生率可能在下降」是 BSG 的**推測性陳述（probably）**，非量化結論[S8]。

### 台灣現況（C4）——本組查證的重點

**（一）高壓氧治療的健保身分：項目存在，但支付標準本文沒有適應症條文**

- **健保支付標準全表（2026-09-01 實下載，6,012 項，逐欄字串檢索）**：「高壓氧」共 **4 筆**[S36]：
  - **47054C「一般高壓氧治療」720 點**（英文名 General hyperbaric oxygen therapy, general；生效 2023/10/01）；**備註全文只有兩句：「1.包括氧氣費在內。2.提升兒童加成項目。」——沒有適應症、沒有事前審查、沒有次數上限、沒有任何「放射」字樣。**
  - 59014B／59015B／59016B **潛水病（減壓病）或急性氣栓塞症之高壓氧治療** 30,836／14,886／3,236 點，備註明文**限第一型／第二型潛水減壓病與空氣栓塞症**。
- **健保署官方 PDF 交叉核對（HTTP 200，472,858 bytes，35 頁，`pdftotext -layout` 全文）**：修正對照表中 47054C 的註逐字為「**1.包括氧氣費在內。2.提升兒童加成項目。3.屬西醫基層總額部門院所，本項以原支付點數 600 點申報。**」[S37]——**與開放資料一致，仍無適應症條文。**
- **行政院公報 026 卷 072 期（2020-04-21，衛生福利部中央健康保險署令）審查注意事項（HTTP 200，128,969 bytes，全文檢索）**[S38]：其中關於高壓氧的審查原則**只涵蓋潛水病／減壓病、一氧化碳與毒化物中毒、氣壞疽**三類，逐字內容包括「高壓氧治療執行頻率最多 1 天 2 次…治療共計約 10 次為宜」「慢性潛水病如異壓性骨壞死可執行 20 次治療，最多延長至 40 次」。**全文查無「放射」「放射線」「放射性膀胱炎」「放射性大腸炎」等字樣。**
- **結論與寫法（FAIL-11，這是 C4 台灣端最重要的一格）**：
  - **可寫的事實**：「健保的診療項目表裡**有**一個『一般高壓氧治療』的項目（47054C，720 點）；另外三個高壓氧代碼的備註明文限潛水減壓病與空氣栓塞症。」
  - **不可寫**：「健保給付放射性組織損傷的高壓氧治療」**或**「健保不給付」——**兩個方向都超過本組取得的官方文件。** 支付標準本文與可取得的公報審查注意事項都沒有放射性組織損傷這一條；坊間（含多家醫院的高壓氧中心網頁）流傳的「健保核定適應症含放射性組織壞死（骨壞死、放射性膀胱炎、放射性大腸炎）」清單，**本組查無對應的健保署官方公告可引**（SPEC 固定紅線：不點名機構、非官方公告不引）。
  - **正文寫法**：「高壓氧在台灣有健保的診療項目代碼，但**放射線造成的組織損傷是不是在給付範圍、要不要事前審查、能做幾次，我查到的官方文件沒有寫**。要做之前，請個管師或醫務課幫你核對現行的給付規定與自付金額——這一格我不替你猜。」

**（二）內視鏡與局部處置的健保項目（全表實查，逐字）**[S36]

| 代碼 | 名稱 | 點數 | 生效 | 備註原文 |
|---|---|---|---|---|
| 28013C | S 狀結腸鏡檢查 | 1,069 | 2023/10/01 | — |
| 28017C | 大腸鏡檢查 | 2,363 | 2023/10/01 | 限消化內科、消化外科、大腸直腸外科、兒科消化學及小兒外科專科醫師執行 |
| 28019C | 膀胱鏡檢查 | 1,800 | 1995/03/01 | — |
| **49023C** | **直腸內視鏡止血術** | **2,392** | 2023/10/01 | 含內視鏡使用費 |
| **49026C** | **經大腸鏡結腸止血術** | **8,044** | 2023/10/01 | 含一般材料費及特殊材料費 |
| **50011C** | **膀胱灌注** | **260** | 1995/03/01 | （無備註） |
| **33105B** | **腸胃道出血栓塞治療** | **10,800** | 2003/12/01 | 包括選擇性血管造影術、血管阻塞術、器材材料費及局部麻醉費，同時不可加報其他血管攝影費用 |
| 47006C | 小量或留置灌腸 | 123 | 2004/07/01 | — |
| 47047C | 坐浴 | 53 | 2013/01/01 | 泡盆（soaking）比照申報 |

- **零筆的檢索**（全表 6,012 項逐欄）：**「氬離子」0 筆、「電漿」0 筆、「福馬林」0 筆、「甲醛」0 筆、「硫醣鋁／sucralfate」0 筆、「益生菌」0 筆、「止瀉」0 筆**[S36]。（「氬」僅 1 筆：62019B 氬氣雷射治療 3,030 點，是**眼科的雷射項目**，與內視鏡氬氣電漿凝固無關，**不可誤引**。）
- **寫法**：「內視鏡止血在健保的診療項目表裡有自己的代碼（直腸 49023C、大腸 49026C），出血栓塞也有（33105B）。**但氬氣電漿凝固與福馬林灌注在表裡查不到專屬項目**——這不等於不能做、也不等於要自費，只是表上沒有那個名字；實際怎麼申報、要不要自付，問醫務課。」**不可從「查無代碼」推論任何費用方向（SPEC 固定紅線）。**
- **膀胱灌注液（特材 D113-2）的事前審查條文**（須在傳統清血塊、電燒無效後，檢附照片與病歷經事前審查核准，原則上每療程六個月為限）→ **pc-bowel-urinary 已引用過，本組未重新取得該附件全文（FAIL-10）；C4 一句指路並提醒核對現行版本。**

**（三）台灣本土的發生率資料**：本組未取得可引的台灣骨盆腔放療晚期出血／廔管／高壓氧使用量資料（FAIL-12）——**不寫「台灣研究顯示」、不引媒體數字。**

---

## 數字形狀的洞（writer 不可回填——每一條都已實際檢索確認查無）

| # | 洞 | 已確認查無的範圍 | 正文寫法 |
|---|---|---|---|
| **H1** | 骨盆腔皮膚反應的**逐週劇本**（第幾週紅、第幾週破、幾週退乾淨） | Europe PMC 檢索到的骨盆腔皮膚文獻只給總發生率與風險因子；唯一可引的時間句是 BC Cancer「一到四週出現、結束後可持續數週」[S1]與 ESTRO「療程 >4–5 週會延後恢復」[S2] | 只用這兩個錨。**乳癌的「結束後 2 週達峰」不可挪用到骨盆腔** |
| **H2** | 急性泌尿症狀的**週次**時間窗 | 唯一的量化來源用的是**累積劑量**（16–45 Gy 佔 75%）[S12]，不是週數 | 寫「大約在療程中段」＋可寫劑量區間；**不可換算成第幾週** |
| **H3** | 「鼠蹊皺摺」「臀溝」作為好發位置的**逐字來源** | CTCAE 與 ESTRO 只寫 skin folds and creases；點名這兩個部位的來源未尋得 | 寫「皺摺與摩擦處」「照野越靠近肛門口越重（距肛門口 ≤5 cm OR 2.86[S3]）」 |
| **H4** | 放療（非移植）族群中 **C. difficile 佔腹瀉的比例** | BSG 表格該格原文即為「?」，並註明「no published data and no clinical experience」[S8] | 寫「拉肚子不一定都是放療造成的，糞便檢查是必要的一步」，**不給比例** |
| **H5** | 攝護腺癌放療後**直腸尿道廔管的發生率百分比** | 檢索到的回顧摘要數字排版損毀（「0.03 in various series」下限缺失）[S35b]；其餘皆為手術系列無分母 | 寫「這是低頻但後果嚴重的併發症」＋引 Chrouser 的關聯（81% 有放療後器械操作史[S22]），**不給百分比** |
| **H6** | 泌尿端「當天回診」的**指引原文條列** | 未尋得可直接引用的病人端指引條文 | 以症狀邏輯寫（血塊會塞、發燒可能是感染），**明說這是臨床分界不是指引條文**；或指路 pc-bowel-urinary 的既有清單 |
| **H7** | **再照射**與**糖尿病**對廔管的效應量 | 再照射只在 6 例病例系列中被點名 2 例[S20]；糖尿病只有腹瀉終點的 HR[S10] | 兩者都可寫成「已知的風險方向」，**不給數字**；不可把腹瀉的 HR 挪用到廔管 |
| **H8** | **直腸癌／膀胱癌**各自的放射性廔管發生率 | 檢索到的直腸癌廔管文獻多為吻合口廔管（手術併發症）而非放射性廔管；膀胱癌未取得 | 廔管數字一律標「子宮頸癌」族群；其他癌別寫「同一個解剖區、風險因子相同，但各癌別的分項數字我查不到」 |
| **H9** | **台灣：高壓氧用於放射性組織損傷的給付條文** | 健保支付標準開放資料全表 6,012 項＋健保署修正對照表 PDF 35 頁＋行政院公報 026 卷 072 期審查注意事項全文，**「放射」相關字樣 0 筆**；坊間清單無官方出處可引 | 「有代碼（47054C，720 點），但放射性組織損傷是否在給付範圍**查不到官方文件**，問醫務課」——**不可寫成給付，也不可寫成不給付** |
| **H10** | **台灣：氬氣電漿凝固、福馬林灌注的健保項目** | 全表「氬離子」「電漿」「福馬林」「甲醛」各 **0 筆** | 「表上沒有這個名字」是可寫的事實；**不可推論費用方向** |
| **H11** | **台灣本土**的骨盆腔放療晚期出血／廔管發生率、高壓氧使用量 | 未取得可引本土資料 | 不寫「台灣研究顯示」；媒體數字絕不引 |
| **H12** | 裡急後重、黏液便的**獨立頻率** | EMBRACE-I 只分項報 proctitis／bleeding／diarrhoea 的 G≥2 | 症狀清單可寫，**不給比例** |
| **H13** | HORTIS-I／II／III 的**個別結果** | Europe PMC 檢索「HORTIS」無獨立試驗條目；HORTIS-III（放射性膀胱炎）**提前結束**[S15] | 只寫 HORTIS-IV（＝Clarke 2008）；提到系列時寫「其中研究膀胱炎的那一個提前結束、沒有結果」 |
| **H14** | Purastat、Mepitel film 等產品在**台灣的可近性與收費** | 未查證 | 「有沒有、怎麼算，問你的團隊與醫務課」 |

---

## Sources（單一序列；**只有 PASS 可以進正文**）

> 編號說明：S7、S11、S33 在查證過程中被併入他條或棄用，序號**刻意留空不遞補**，以免與已寫好的內文引註錯位。S14b、S35b 為同組來源之第二筆。

### C1

- **[S1] PASS（官方 PDF，2026-09-01 重新下載，HTTP 200，376,402 bytes，12 頁，`pdftotext -layout` 全文逐字核對）** 【機構型來源，無作者欄】BC Cancer. *Symptom Management Guidelines: Radiation Dermatitis*（NCI CTCAE v.5 update）. https://www.bccancer.bc.ca/nursing-site/Documents/Radiation%20Dermatitis%20NCI%20v.5%20Update.pdf ——逐字核對內容：定義句「Reactions are evident one to four weeks after beginning treatment and can persist for several weeks post treatment」；CTCAE v5 分級表（G2「patchy moist desquamation, mostly confined to skin folds and creases」／G3「Moist desquamation in areas other than skin folds and creases」）；**「GRADE 2 – GRADE 3 URGENT: Requires medical attention within 24 hours」**；感染徵象四項「fever／foul odour／purulent drainage／pain and swelling extending outside the treatment area」；**「Patients receiving RT for perineal/rectal cancer should use a sitz bath daily once RT begins」（G1 與 G2–3 段各出現一次）**；Appendix B 一般建議（每天溫水洗＋溫和無香精 pH 平衡皂、不用毛巾搓、乾燥完整皮膚上可續用止汗劑／體香劑、電動刮鬍刀、氯水泳池後沖洗＋保濕、破皮後停游、避免膠帶／冰敷／電熱墊、寬鬆棉質衣物）；「Corticosteroid creams may be used sparingly for inflammation as ordered by the physician」。
- **[S2] PASS（OA，Europe PMC fullTextXML HTTP 200，233,944 bytes，全文逐字核對）** Forde E, Van den Berghe L, Buijs M, Cardone A, Daly J, Franco P, Julka-Anderson N, Lechner W, Marignol L, Marvaso G, Nisbet H, O'Donovan A, Russell NS, Scherer P. Practical recommendations for the management of radiodermatitis: on behalf of the ESTRO RTT committee. *Radiat Oncol*. 2025;20(1):46. DOI: 10.1186/s13014-025-02624-9. PMID 40158149. PMC11954187. ——「Up to 95% of cancer patients receiving radiotherapy will develop acute RID」；高風險癌別「breast, head and neck, anal, and vulvar cancer」；「obesity leading to skin folds will also increase the dose to the skin in the folds」；「Prolonged fractionation schedules longer than 4–5 weeks will also delay the onset of RID recovery」；分級管理表（G0 每日清洗 QoE L1 強推薦、體香劑 QoE L1 強推薦、G2 自黏軟矽膠敷料 QoE L1 強推薦、感染由傷口專科照護 QoE L4、感染徵象即用局部抗菌劑 QoE L3）；結論自陳「identified a lack of high-level evidence」。
- **[S3] PASS（摘要層級；全文非 OA）** He Y, Wang M, Gao C, Hao Y, He S, Li L. Incidence, Risk Factors, and Management of Radiotherapy-Related Skin Toxicity in Rectoanal Cancer Patients: a Systematic Review and Meta-Analysis. *J Gastrointest Cancer*. 2026;57(1):16. DOI: 10.1007/s12029-025-01387-6. PMID 41538092. ——50 篇、n=4,892；總發生率 58.7%（95% CI 55.2–62.1）、G≥3 12.3%、濕性脫屑 34.5%；風險因子 OR（距肛門口 ≤5 cm 2.86／無造口 3.12／>50 Gy 2.59／同步化療 2.73／HIV 5.82／3D-CRT vs IMRT 8.76／腫瘤侵犯皮膚 36.0）；50 Gy 轉折點、每多 5 Gy +29%；噴霧式保護劑 SUCRA 92.3%、VMAT OR 0.29。
- **[S4] PASS（書目與數字沿 B 組 brief 已核對之 [S10]，本組重新核對書目一致）** Kachnic LA, Winter K, Myerson RJ, et al. RTOG 0529: a phase 2 evaluation of dose-painted IMRT … carcinoma of the anal canal. *Int J Radiat Oncol Biol Phys*. 2013;86(1):27–33. DOI: 10.1016/j.ijrobp.2012.09.023. PMID 23154075. PMC3619011. ——**主要終點未達成**（G2+ 急性 GI/GU 77% vs 77%）；G3+ 皮膚 23% vs 49%（p<.0001）。
- **[S5] PASS（摘要層級；全文付費牆）** Behroozian T, Bonomo P, Patel P, et al.; MASCC Oncodermatology Study Group Radiation Dermatitis Guidelines Working Group. MASCC clinical practice guidelines for the prevention and management of acute radiation dermatitis: international Delphi consensus-based recommendations. *Lancet Oncol*. 2023;24(4):e172–e185. DOI: 10.1016/S1470-2045(23)00067-0. PMID 36990615. ——42 位專家、四輪德爾菲、共識門檻 75%；**預防獲推薦六項**（光生物調節與 Mepitel film **限乳癌**、Hydrofilm、mometasone、betamethasone、橄欖油）；**處理獲推薦僅 Mepilex Lite**；其餘「not recommended due to insufficient evidence, conflicting evidence, or lack of consensus」。
- **[S6] PASS（OA，摘要逐字核對）** Simões FV, da Silva E Silva T, Pires AA, França CRM, Velasco NS, Santos VO, Moreira K, da Silva MM, Brandão MAG, de Oliveira BGRB, da Silva RC. Spray skin protectant versus standard moisturiser in the prevention of radiodermatitis in patients with anal canal and rectal cancer: A randomised clinical trial. *Int Wound J*. 2024;21(8):e70030. DOI: 10.1111/iwj.70030. PMID 39171868. PMC11339855. ——n=63 單盲隨機（肛管與直腸癌，巴西）；噴霧式保護膜組出現「合併濕性脫屑之皮膚炎」機率較低、無此結果之時間較長；**總發生率 100%、嚴重 36.5%、17.5% 因皮膚炎中斷放療；兩組在嚴重度與中斷人數上無差異**。

### C2

- **[S8] PASS（OA，Europe PMC fullTextXML HTTP 200，373,412 bytes，166,313 字全文逐字核對）** Andreyev J, Adams R, Bornschein J, Chapman M, Chuter D, Darnborough S, Davies A, Dignan F, Donnellan C, Fernandes D, Flavel R, Giebner G, Gilbert A, Huddy F, Khan MSS, Leonard P, Mehta S, Minton O, Norton C, Payton L, et al. British Society of Gastroenterology practice guidance on the management of acute and chronic gastrointestinal symptoms and complications as a result of treatment for cancer. *Gut*. 2025;74(7):1040–1067. DOI: 10.1136/gutjnl-2024-333812. PMID 40068855. PMC12322484. ——103 條建議。**本 brief 引用之逐字段落**：急性時間形狀（second week／peak in the last week／at least 1–2 weeks after／hypofractionated may not start before treatment is completed）；急性放療預防指引 29.1–29.3（飲食諮詢與蛋白質補充、Lactobacilli±bifidobacteria 益生菌、**高纖飲食**）；飲食介入總判詞（「inadequate data … should not be used outside the context of clinical trials」）；「endorectal spacers, balloons, rectal emptying … have not improved GI outcomes」；抽菸與低 BMI 應於放療前處理；急性腹瀉先驗糞便、可先用 loperamide、定期重評以排除毒性巨結腸；G3–4 腹瀉須停化療；療程中血便建議結束後 6 週做軟式乙狀結腸鏡；晚期直腸出血（up to half／severe ~1%／幾個月後開始、三年內達峰、可持續十年以上／劑量關係／近接治療移轉受損部位）；不可假設出血來自放射性微血管擴張、**不做切片**；sucralfate 灌腸定位；APC（widely used／**serious complication rate of up to 26%**／攝護腺近接治療後前壁**絕對禁忌**）；任何熱凝固在缺血組織上的風險；formalin（無安慰劑對照隨機試驗、併發症）；Purastat（21 人、1 年四分之三改善）；HBO（隨機試驗結果矛盾、HOT2 p=0.09、HORTIS IV 較佳、至少 30 次、低壓艙大概無效）；**廔管段全文**（rare／incidence probably decreasing／可急性或多年後表現／**先排除復發**／四項處理原則／罕見情況下高壓氧有角色）；放療後 5–10 年起腸道二次癌症風險、每 5 年參與篩檢；生理異常表格中放療期間與放療後的 C. difficile 格為「?」＝無發表資料亦無臨床經驗；移植族群「用止瀉藥前先驗 C. difficile」。
- **[S9] PASS（摘要層級）** Spampinato S, Jensen NBK, Pötter R, Fokdal LU, Chargari C, Lindegaard JC, Schmid MP, Sturdza A, Jürgenliemk-Schulz IM, Mahantshetty U, Hoskin P, Segedin B, Rai B, Bruheim K, Wiebe E, Van der Steen-Banasik E, Cooper R, et al. Severity and Persistency of Late Gastrointestinal Morbidity in Locally Advanced Cervical Cancer: Lessons Learned From EMBRACE-I and Implications for the Future. *Int J Radiat Oncol Biol Phys*. 2022;112(3):681–693. DOI: 10.1016/j.ijrobp.2021.09.055. PMID 34678431. ——n=1,199（CTCAE）／1,002（EORTC）；G≥3 肛門／直腸 2.8%、乙狀結腸 1.8%、結腸／小腸 2.3%；G≥2 腹瀉 8.5%、脹氣 9.9%；風險因子含基線症狀、年齡、抽菸、低 BMI、rectum D2cm³、ICRU RV-RP、bowel D2cm³、EBRT 處方劑量、V57Gy。
- **[S10] PASS（摘要層級）** K Jensen NB, Pötter R, Spampinato S, Fokdal LU, Chargari C, Lindegaard JC, Schmid MP, Sturdza A, Jürgenliemk-Schulz IM, Mahantshetty U, Segedin B, Bruheim K, Hoskin P, Rai B, Wiebe E, Cooper R, Van der Steen-Banasik E, et al. Dose-Volume Effects and Risk Factors for Late Diarrhea in Cervix Cancer Patients After Radiochemotherapy With Image Guided Adaptive Brachytherapy in the EMBRACE I Study. *Int J Radiat Oncol Biol Phys*. 2021;109(3):688–700. DOI: 10.1016/j.ijrobp.2020.10.006. PMID 33068689. ——n=1,199，中位追蹤 48 個月；粗發生率 G≥2 8.3%、G≥3 1.5%；EORTC「very much」腹瀉 8%；持續性 G≥1 16%、≥「quite a bit」7%；病人端風險因子基線腹瀉、抽菸、糖尿病（HR 1.4–7.3）；3 年 G≥2 腹瀉 45 Gy 9.5% vs 50 Gy 19.9%、V43Gy <2,500 vs >3,000 cm³ 為 8.7% vs 14.0%、V57Gy <165 vs ≥165 cm³ 為 9.4% vs 19.0%。

### C3

- **[S12] PASS（OA，Europe PMC fullTextXML HTTP 200，全文逐字核對）** Xavier VF, Gabrielli FCG, Ibrahim KY, Gomes MVS, Guimarães RGR, Abdala E, Carvalho HA. Urinary infection or radiation cystitis? A prospective evaluation of urinary symptoms in patients submitted to pelvic radiotherapy. *Clinics (Sao Paulo)*. 2019;74:e1388. DOI: 10.6061/clinics/2019/1388. PMID 31778433. PMC6862710. ——n=72（癌別：攝護腺 27、直腸 22、子宮頸 16、子宮內膜 4、肛管 3）；療程中 24（33%）出現新的或惡化症狀，**其中僅 1 例（全體 1.4%）尿液培養陽性**；**因結果遠低於樣本估計而提前中止收案、預定的預測因子回歸分析取消**；症狀出現時累積劑量分布（<5 Gy 0%／6–15 Gy 8%／16–25 Gy 25%／26–35 Gy 25%／36–45 Gy 25%／46–55 Gy 4%／56–65 Gy 8%／>65 Gy 4%）；症狀組成（解尿疼痛 20/24＝83%、夜尿 4/24＝16%）；治療前已有症狀者 49%；引言原文「may mimic the secondary symptoms of urinary tract infection」與「probably cannot be applied in individuals undergoing pelvic radiotherapy」。
- **[S13] PASS（摘要層級）** Shuford RA, Dulaney CR, Burnett OL, Byram KW, McDonald AM. Evaluating the Role of Urinalysis for Suspected Cystitis in Women Undergoing Pelvic Radiotherapy. *Int J Gynecol Cancer*. 2016. DOI: 10.1097/IGC.0000000000000714. PMID 27101588. PMC5074921. ——134 位婦癌骨盆腔放療女性、241 份檢體；**84 份（34.9%）培養陽性**；亞硝酸鹽或白血球酯酶任一陽性敏感度 91.7%；白血球＋亞硝酸鹽皆陽性特異度 95.5%、PPV 75.0%、DOR 7.21（2.92–17.83）；無白血球之 NPV 87.0%；**E. coli 僅 22.6%**；抗藥率 TMP-SMX 23.8%、ciprofloxacin 16.7%、nitrofurantoin 11.1%。
- **[S14] PASS（摘要層級）** Spampinato S, Fokdal LU, Pötter R, Haie-Meder C, Lindegaard JC, Schmid MP, Sturdza A, Jürgenliemk-Schulz IM, Mahantshetty U, Segedin B, Bruheim K, Hoskin P, Rai B, Huang F, Cooper R, van der Steen-Banasik E, Van Limbergen E, et al. Risk factors and dose-effects for bladder fistula, bleeding and cystitis after radiotherapy with imaged-guided adaptive brachytherapy for cervical cancer: An EMBRACE analysis. *Radiother Oncol*. 2021;158:312–320. DOI: 10.1016/j.radonc.2021.01.019. PMID 33545254. ——1,416 收案；**風險因子分析在無膀胱侵犯者中進行**（CTCAE n=1,153、EORTC n=884）；中位追蹤 48 個月；**G≥2 廔管 0.7%、出血 2.7%、膀胱炎 8.8%**；EORTC「quite a bit or worse」疼痛 16%、解尿困難 14%；膀胱 D2cm³ 與三者相關；D2cm³ 75→80 Gy 使 4 年 G≥2 膀胱炎由 8% 升至 13%。
- **[S14b] PASS（摘要層級）** Spampinato S, Fokdal LU, Pötter R, et al. Importance of the ICRU bladder point dose on incidence and persistence of urinary frequency and incontinence in locally advanced cervical cancer: An EMBRACE analysis. *Radiother Oncol*. 2021;158:300–308. DOI: 10.1016/j.radonc.2020.10.003. PMID 33065183. ——同世代；**G≥2 頻尿 13%、尿失禁 11%**；ICRU 膀胱點劑量 >75 Gy 相對 ≤65 Gy，5 年 G≥2 尿失禁由 11% 升至 20%。
- **[S15] PASS（OA，Europe PMC fullTextXML HTTP 200，183,762 bytes，全文逐字核對）** Dejonckheere CS, Käsmann L, Schmeel LC, Walter S, Anzböck T, Dreyer S, Sarria GR, Gkika E, Layer JP. Hyperbaric oxygen therapy for chronic radiotherapy-related adverse effects: A clinically focused review. *CA Cancer J Clin*. 2026;76(1):e70058. DOI: 10.3322/caac.70058. PMID 41385271. PMC12700310. ——放射性膀胱炎 5%–15%、症狀典型於治療後 2 年、>60 Gy 風險顯著上升；標準處置順序（bladder irrigation／intravesical coagulation／instillation）；**Table 3 隨機試驗對照表（HONEY／HOPON／DAHANCA-21＋NWHHT2009-1／RICH-ART／HORTIS-IV／HOT2）**；RICH-ART 詳述（NNT 3、95% CI 2–5；EPIC 腸道分數亦改善 13.2 vs 4.9，差 8.3，p=.024；41% 暫時性 G1–2 不良事件）；五年追蹤詳述（13% 症狀復發再治療、多數原只做 30 次）；「HBOT can be offered … should be preferred over urinary diversion, bladder embolization, or cystectomy」；「Early referral … short intervals（within 6 months）」；FDA 核准放射相關而非化療相關出血性膀胱炎；HOT2 與 HORTIS-IV 差異的解釋（病人選擇、未經驗證的終點工具）；**HORTIS-III（放射性膀胱炎，ISRCTN19501634）closed early**；轉述 MASCC 指引推薦 HBOT 治療放射性直腸炎；**Table 1 副作用表**（近視 25%–100%、中耳氣壓傷 2%–3%、肺氣壓傷罕見、氧中毒每 2,000–3,000 次 1 次、幽閉恐懼／低血糖／高血壓／急性肺水腫罕見 <0.5%）；「higher with an increasing number of treatment sessions（usually >10）and pressures above 2.0 ATA」；絕對／相對禁忌；**Table 2 藥物交互作用**（bleomycin／doxorubicin／cisplatin／disulfiram／mafenide）；「lack of experience when combining newer antineoplastic agents」；可近性與給付不均的段落全文；2017 European Consensus Conference on Hyperbaric Medicine 22 項適應症中 6 項（27%）與放療相關；HBOT 給氧規格 1.9–6.0 ATA（常用 2.0–2.5）、每次 90–120 分、每週五天。

### C4

- **[S16] PASS（摘要層級）** Vittrup AS, Kirchheiner K, Pötter R, Fokdal LU, Jensen NBK, Spampinato S, Haie-Meder C, Schmid MP, Sturdza AE, Mahantshetty U, Hoskin P, Segedin B, Bruheim K, Rai B, Wiebe E, van der Steen-Banasik E, Cooper R, Van Limbergen E, Sundset M, Pieters BR, Kirisits C, Lindegaard JC, Jürgenliemk-Schulz IM, Nout R, Tanderup K; EMBRACE Collaborative Group. Overall Severe Morbidity After Chemo-Radiation Therapy and Magnetic Resonance Imaging-Guided Adaptive Brachytherapy in Locally Advanced Cervical Cancer: Results From the EMBRACE-I Study. *Int J Radiat Oncol Biol Phys*. 2023;116(4):807–824. DOI: 10.1016/j.ijrobp.2023.01.002. PMID 36641039. ——1,416 收案、1,251 有晚期追蹤；534 件嚴重事件發生於 270 人（429 件 G3、105 件 G4）；**5 年 actuarial G≥3：腸胃 8.5%（6.9–10.6）、泌尿 6.8%（5.4–8.6）、陰道 5.7%（4.3–7.6）、廔管 3.2%（2.2–4.5）**；器官相關合計 18.4%（16.0–21.2）、全終點合計 26.6%（23.8–29.6）；**13 位治療相關死亡，其中 8 位與腸胃道相關**。
- **[S17] PASS（摘要層級）** Kim YJ, Lee J, Park S, Kim YM, Park KJ, Kim YS. The value of magnetic resonance imaging in predicting vesicovaginal fistula in cervical cancer with bladder invasion treated with definitive chemoradiotherapy. *Gynecol Oncol*. 2025;193:136–140. DOI: 10.1016/j.ygyno.2025.01.009. PMID 39864258. ——n=43（1999–2015，MRI 評分 ≥3 或膀胱鏡確認之膀胱侵犯）；中位追蹤 67.4 個月；**膀胱陰道廔管 5 例（12.8%）**，3 例於治療後 1 年內、2 例於 16.7 與 64.5 個月；多變項中唯一顯著預測因子為 MRI 上膀胱壁受侵高度（p=0.041）：**≥20.3 mm 25%、≥31.1 mm 50%、≥41 mm 75%**。
- **[S18] PASS（OA）** Ali N, Sykes Martin KD, Tobillo R, Meiyappan K, McCook-Veal A, Switchenko J, Dresser S, Dilley S, Starbuck KD, Khanna N, Shelton J, Patel A, Eng T, Manning-Geist B, Remick JS. Risk factors and clinical outcomes of radiation-induced fistula after chemoradiation and image-guided brachytherapy for locally advanced cervical cancer. *Gynecol Oncol Rep*. 2025;62:101977. DOI: 10.1016/j.gore.2025.101977. PMID 41282280. PMC12637236. ——FIGO IB2–IV，2013–2022 單中心，n=150；中位追蹤 20 個月；**廔管 13 例（9%）**；13 人中 8 人（62%）症狀緩解；2 年整體存活 72.0%、無廔管存活 91.6%；單變項：BMI 較高 OR 0.90（0.82–1.00，p=0.048）、**現行抽菸 OR 8.37（2.58–27.22，p<0.001）**、未用 MRI 導引 OR 4.77（1.42–15.97，p=0.011）、疾病侵入膀胱 OR 3.99（1.27–12.53，p=0.018）；**多變項僅現行抽菸顯著 OR 5.14（1.43–18.48，p=0.012）**。
- **[S19] PASS（摘要層級；全文非 OA）** Landman Y, De Sousa Smith C, Ke S, Roumeliotis M, Rezaee M, Lee J, Schmidt EJ, Hu C, Viswanathan AN. Image-guided brachytherapy for locally advanced cervical cancer: clinical outcomes and fistula risk in stage IVA disease. *Int J Gynecol Cancer*. 2026;36(9):104848. DOI: 10.1016/j.ijgc.2026.104848. PMID 42531776. ——n=151，中位追蹤 2.9 年，其中 IVA 期 22 人（14.6%）；任何廔管之多變項預後因子：**BMI <20 kg/m² OR 4.33（1.11–16.90，p=.035）、免疫功能低下 OR 5.84（1.32–25.91，p=.020）、IVA 期 OR 6.87（1.99–23.75，p=.002）、原發腫瘤體積較大 OR 3.29（1.53–7.08，p=.002）**；IVA 期病人的膀胱與直腸 D2cc 較高「due to organ invasion」。
- **[S20] PASS（OA）** Sugiyama T, Katsumata N, Toita T, Ura M, Shimizu A, Kamijima S, Aoki D. Incidence of fistula occurrence in patients with cervical cancer treated with bevacizumab: data from real-world clinical practice. *Int J Clin Oncol*. 2022;27(9):1517–1528. DOI: 10.1007/s10147-022-02196-8. PMID 35760943. PMC9393147. ——日本上市後監測 n=142（中位年齡 51、鱗癌 66.9%、復發性 66.2%、**曾放療 64.1%**）；中位 7 劑；**6 位發生 7 處骨盆腔廔管＝4.2%（95% CI 1.56–8.96），6 位全部有骨盆腔照射史**，其中 5 位另有骨盆腔手術史；3 位膀胱與直腸累積劑量高，其中 2 位曾為骨盆腔復發接受**救援性再照射**；作者結論：95% CI 上限未超過 GOG 240 通報之發生率。
- **[S21] PASS（摘要層級；全文非 OA）** Yang ST, Liu HH, Liu CH, Wang LW, Wang PH. Bevacizumab is associated with a higher gastrointestinal/genitourinary fistula or perforation risk in cervical cancer patients undergoing pelvic radiotherapy. *Int J Gynaecol Obstet*. 2024;167(1):80–87. DOI: 10.1002/ijgo.15609. PMID 38746971. ——統合分析，4 個世代研究、597 位；**腸胃道廔管／穿孔 OR 4.03（95% CI 1.76–9.20）、泌尿道廔管／穿孔 OR 4.71（95% CI 1.51–14.70）**。
- **[S22] PASS（摘要層級）** Chrouser KL, Leibovich BC, Sweat SD, Larson DW, Davis BJ, Tran NV, Zincke H, Blute ML. Urinary fistulas following external radiation or permanent brachytherapy for the treatment of prostate cancer. *J Urol*. 2005;173(6):1953–1957. DOI: 10.1097/01.ju.0000158041.77063.ff. PMID 15879789. ——1977–2002 期間 51 位攝護腺癌放療後泌尿廔管者，符合納入條件 20 位（外照射 30%／近接 30%／併用 40%）；**80% 為直腸至泌尿道之廔管、平均直徑 3.2 cm**；**直腸廔管者 81% 有以下病史之一：直腸狹窄、尿道狹窄、直腸切片、直腸氬氣光束治療或放療後 TURP**；所有達症狀緩解之直腸尿道廔管病人皆需尿路與糞便雙改道。**（病例系列，無分母，不可算發生率。）**
- **[S23] PASS（摘要層級；即 HORTIS-IV，試驗代號由 [S15] 之 Table 3 確認）** Clarke RE, Tenorio LM, Hussey JR, Toklu AS, Cone DL, Hinojosa JG, Desai SP, Dominguez Parra L, Rodrigues SD, Long RJ, Walker MB. Hyperbaric oxygen treatment of chronic refractory radiation proctitis: a randomized and controlled double-blind crossover trial with long-term follow-up. *Int J Radiat Oncol Biol Phys*. 2008;72(1):134–143. DOI: 10.1016/j.ijrobp.2007.12.048. PMID 18342453. ——226 評估／150 納入／120 可評估；2.0 ATA vs 1.1 ATA 空氣；SOMA-LENT 改善 5.00 vs 2.61（p=0.0019）、組間平均較低（p=0.0150）、臨床有反應 88.9% vs 62.5%（p=0.0009）、ITT 分析 p=0.0006；**絕對風險降低 32%、NNT 3**；交叉後差異消失；腸道特異生活品質較佳。
- **[S24] PASS（OA，摘要逐字核對）** Glover M, Smerdon GR, Andreyev HJ, Benton BE, Bothma P, Firth O, Gothard L, Harrison J, Ignatescu M, Laden G, Martin S, Maynard L, McCann D, Penny CEL, Phillips S, Sharp G, Yarnold J. Hyperbaric oxygen for patients with chronic bowel dysfunction after pelvic radiotherapy (HOT2): a randomised, double-blind, sham-controlled phase 3 trial. *Lancet Oncol*. 2016;17(2):224–233. DOI: 10.1016/S1470-2045(15)00461-1. PMID 26703894. PMC4737893. ISRCTN86894066. ——n=84（55 HBOT／29 假治療），2.4 ATA vs 1.3 ATA、90 分鐘、每週 5 天、8 週共 40 次；**共同主要終點皆無差異**：IBDQ 腸道分數中位改變 4（IQR −3 到 11）vs 4（−6 到 9），p=0.50；直腸出血分數 3（1–3）vs 1（1–2），p=0.092；常見不良事件（治療組 vs 對照組）屈光改變 30% vs 11%、耳痛 28% vs 21%；8 件嚴重不良事件皆判定與治療無關；**結論原文「We found no evidence that patients … benefit from hyperbaric oxygen therapy. These findings contrast with evidence used to justify current practices, and more level 1 evidence is urgently needed.」**
- **[S25] PASS（摘要逐字核對；全文非 OA）** Oscarsson N, Müller B, Rosén A, Lodding P, Mölne J, Giglio D, Hjelle KM, Vaagbø G, Hyldegaard O, Vangedal M, Salling L, Kjellberg A, Lind F, Ettala O, Arola O, Seeman-Lodding H. Radiation-induced cystitis treated with hyperbaric oxygen therapy (RICH-ART): a randomised, controlled, phase 2-3 trial. *Lancet Oncol*. 2019;20(11):1602–1614. DOI: 10.1016/S1470-2045(19)30494-2. PMID 31537473. NCT01659723；EudraCT 2012-001381-15. ——五家北歐大學醫院；納入條件含骨盆腔放療 ≥6 個月前完成、EPIC 泌尿分數 <80；**排除條件含「fistula in the urinary bladder」**；87 隨機／79 ITT；HBOT 30–40 次、240–250 kPa、80–90 分鐘；**EPIC 泌尿總分改變之組間差 10.1 分（95% CI 2.2–18.1，p=0.013；17.8 分 [SD 18.4] vs 7.7 分 [15.5]）**；**41%（17/41）出現暫時性 grade 1–2 視聽相關不良事件**；**無盲（No masking was applied）**。
- **[S26] PASS（OA）** Oscarsson N, Rosén A, Müller B, Koskela LR, Giglio D, Kjellberg A, Ettala O, Seeman-Lodding H. Radiation-induced cystitis treated with hyperbaric oxygen therapy (RICH-ART): long-term follow-up of a randomised controlled, phase 2-3 trial. *EClinicalMedicine*. 2025;83:103214. DOI: 10.1016/j.eclinm.2025.103214. PMID 40291346. PMC12033922. ——引言句「affecting approximately 5-10% of patients」；70 位可追蹤；EPIC 泌尿總分由 46.6（SD 18.4）改善 18.0 分（95% CI 14.2–21.8）至 6 個月的 64.6（SD 24.1），**5 年仍為 +19.1 分（95% CI 13.3–24.9）**；**有反應者（≥9 分改善）48 人（68.6%）5 年 +22.9 分（16.2–29.6，p<0.0001）；無反應者 22 人（31.4%）自始至終無改善（43.5→44.6）**；**9/70（12.8%）因症狀復發追加 HBOT**；**因經費不足提前 6 個月終止追蹤（2022 年 5 月）**。
- **[S27] PASS（摘要逐字核對；全文非 OA，inEPMC）** Bennett MH, Feldmeier J, Hampson NB, Smee R, Milross C. Hyperbaric oxygen therapy for late radiation tissue injury. *Cochrane Database Syst Rev*. 2016;4:CD005005. DOI: 10.1002/14651858.CD005005.pub4. PMID 27123955. PMC6457778. ——14 試驗、753 人；**放射性直腸炎（單一研究）改善或治癒 RR 1.72（95% CI 1.0–2.9，p=0.04，NNTB 5）**；下頜骨壞死黏膜覆蓋 RR 1.3（1.1–1.6，NNTB 5，中等品質）；神經組織無效；**「These trials did not report adverse events」**；結論原文「The application of HBOT to selected participants and tissues **may be justified**. Further research is required … An economic evaluation should be undertaken.」
- **[S28] PASS（摘要逐字核對；全文非 OA）** van de Wetering FT, Verleye L, Andreyev HJ, Maher J, Vlayen J, Pieters BR, van Tienhoven G, Scholten RJ. Non-surgical interventions for late rectal problems (proctopathy) of radiotherapy in people who have received radiotherapy to the pelvis. *Cochrane Database Syst Rev*. 2016;4:CD003455. DOI: 10.1002/14651858.CD003455.pub2. PMID 27111831. PMC7173735. ——16 研究、993 人，**未做統合**；出血終點 9 篇皆不明或高偏差風險；APC 加安慰劑優於 APC 加口服 sucralfate（內視鏡評分 RR 2.26，95% CI 1.12–4.55，n=122，**低至中品質**）；4% formalin 塗抹優於 sucralfate-類固醇留置灌腸（p=0.001，n=102，**極低至低品質**）；結腸灌洗＋ciprofloxacin＋metronidazole 優於 4% formalin（n=50，低品質）；腸胃科醫師主導演算法 IBDQ-B 6 個月 MD 5.47（1.14–9.81）、護理師主導 MD 4.12（0.04–8.19）（n=218，低品質）；**HBOT（2.0 ATA）優於安慰劑之 SOMA-LENT 改善 p=0.0019（n=150，中等品質）**；結論原文「single small studies provide limited evidence」。
- **[S29] PASS（OA；證據等級最低，建議正文不用）** Yuan JH, Song LM, Liu Y, Li MW, Lin Q, Wang R, Zhang CS, Dong J. The Effects of Hyperbaric Oxygen Therapy on Pelvic Radiation Induced Gastrointestinal Complications (Rectal Bleeding, Diarrhea, and Pain): A Meta-Analysis. *Front Oncol*. 2020;10:390. DOI: 10.3389/fonc.2020.00390. PMID 32328454. PMC7160697. ——**單臂改善率彙總**：直腸出血 0.81（95% CI 0.74–0.89）、腹瀉 0.75（0.61–0.90）、疼痛 0.58（0.38–0.79）；結論「might have the potential … more data are needed」。
- **[S30] PASS（OA）** Khern WC, Rajandram R, Raja Ram NK, Kuppusamy S. Comparative efficacy and safety of energy coagulation in radiation-induced hemorrhagic cystitis: A narrative review. *Investig Clin Urol*. 2025;66(2):97–105. DOI: 10.4111/icu.20240288. PMID 40047122. PMC11885922. ——10 篇、n=137–139（Nd:YAG、氬氣電漿凝固、980-nm 二極體雷射、KTP 雷射）；**116/137（84.7%）單次治療後血尿緩解**；無血尿之平均／中位間隔 **11–16 個月**；**6 人（4.4%）無反應而接受膀胱切除／尿路改道**；**總不良事件 30/139（21.6%）**（儲尿期症狀、再出血、膀胱結石、尿滯留等）。
- **[S31] PASS（摘要層級；全文非 OA）** Li KD, Jones CP, Hakam N, Erickson BA, Vanni AJ, Chancellor MB, Breyer BN. Haemorrhagic cystitis: a review of management strategies and emerging treatments. *BJU Int*. 2023;132(6):631–637. DOI: 10.1111/bju.16140. PMID 37501638. ——**「There is no standard of care for patients with HC」**；現有策略（電燒、高壓氧、肉毒桿菌素 A、其他膀胱內灌注療法）僅於世代研究顯示**短期**療效。
- **[S32] PASS（摘要層級；單臂，證據等級低）** Yuan ZX, Ma TH, Zhong QH, Wang HM, Yu XH, Qin QY, Chu LL, Wang L, Wang JP. Novel and Effective Almagate Enema for Hemorrhagic Chronic Radiation Proctitis and Risk Factors for Fistula Development. *Asian Pac J Cancer Prev*. 2016;17(2):631–638. DOI: 10.7314/APJCP.2016.17.2.631. PMID 26925655. ——n=59（婦癌佔 93.1%）；90%（53/59）出血明顯減少、平均反應時間 12 天、長期控制成功率 69%；**中重度貧血與後續發生直腸深潰瘍或廔管顯著相關（p=0.015）**。
- **[S34] PASS（摘要層級；全文非 OA）** Lo Re M, Pezzoli M, Garcia Rojo E, Alonso Isa M, Manfredi C, Cocci A, Sessa F, Minervini A, Fraile Poblador A, Romero-Otero J. A systematic review on the surgical management of acquired rectourethral fistula. *Int J Impot Res*. 2026;38(3):214–225. DOI: 10.1038/s41443-025-01100-y. PMID 40579441. ——10 篇、>500 人；最常見術式為經會陰＋股薄肌皮瓣；**「higher complication rates and diminished healing in irradiated patients compared to non-irradiated counterparts」**；照射過的病人常需追加手術或永久尿路改道。
- **[S35] PASS（OA）** Jeannot P, Roussel E, Dutoit A, Collard M, Christou N, Lefevre JH, Souadka A, Arnaud A, Castaldi A, Bertrand M, Michot N, d'Arcier BF, Tuech JJ, Bruyère F, Giger-Pabst U, Ouaïssi M. Comparative outcomes of early and late rectourethral fistula: insights from a multicentric retrospective study on multidisciplinary management strategies. *Ann Coloproctol*. 2026;42(1):103–114. DOI: 10.3393/ac.2025.00696.0099. PMID 41802311. PMC12971167. ——2010-01 至 2023-06，n=72（早發 37／晚發 35，以術後 31 天為界）；**最終完全癒合：早發 83.8% vs 晚發 42.9%（p<0.005）**；第二次治療後治癒率 83.8% vs 40.0%（p<0.001）；**約 30% 的病人最後需要永久性結腸造口，晚發組 48.5% vs 早發組 13.5%（p=0.001）**。
- **[S35b] NOT-CITABLE（摘要數字排版損毀，僅存紀錄）** Poitevin M, Ferragu M, Bigot P, Culty T, Venara A. Rectourethral fistulas after treatment for prostate carcinoma: Update and new management algorithm. *J Visc Surg*. 2025;162(3):199–208. DOI: 10.1016/j.jviscsurg.2025.01.010. PMID 39952891. ——摘要原文「their prevalence ranges from **0.03 in various series**」，**區間上限缺失、單位不明**，**不可引用該數字**；可引的僅其定性陳述（多數為醫源性、放療病史決定處置策略、無最佳術式共識）。

### 台灣端

- **[S36] PASS（開放資料全表，2026-09-01 實下載並解析；curl HTTP 200，565,406 bytes，application/ods → odfpy 解析 6,012 列 → 逐欄字串檢索）** 【機構型來源，無作者欄】衛生福利部中央健康保險署。《全民健康保險醫療服務給付項目及支付標準》開放資料（「生效起日」最新值 2025-05-01，即 114-05-01 生效版）。資料集頁：https://data.gov.tw/dataset/9405 ；檔案：https://info.nhi.gov.tw/api/iode0000s01/Dataset?rId=A21030000I-D20003-004
  ——本 brief 逐欄核對之項目：**47054C 一般高壓氧治療 720 點（2023/10/01 生效；備註「1.包括氧氣費在內。2.提升兒童加成項目。」）**；59014B／59015B／59016B 潛水病或急性氣栓塞症之高壓氧治療 30,836／14,886／3,236 點（備註明文限第一型／第二型潛水減壓病與空氣栓塞症）；**37026B 放射治療之皮膚處理（一個療程）244 點（備註「1.以每週為一個療程（含括一週之治療次數）。2.申報時須註明所照部位範圍、劑量、次數。」）**；28013C S 狀結腸鏡檢查 1,069 點；28017C 大腸鏡檢查 2,363 點；28019C 膀胱鏡檢查 1,800 點；**49023C 直腸內視鏡止血術 2,392 點（含內視鏡使用費）**；**49026C 經大腸鏡結腸止血術 8,044 點（含一般材料費及特殊材料費）**；**50011C 膀胱灌注 260 點**；**33105B 腸胃道出血栓塞治療 10,800 點**；47006C 小量或留置灌腸 123 點；47047C 坐浴 53 點；62019B 氬氣雷射治療 3,030 點（**眼科雷射，與內視鏡氬氣電漿凝固無關**）。**零筆檢索（全表 6,012 項逐欄）：「氬離子」0、「電漿」0、「福馬林」0、「甲醛」0、「sucralfate／硫醣鋁」0、「益生菌」0、「止瀉」0。**
- **[S37] PASS（官方 PDF，2026-09-01 實下載；HTTP 200，472,858 bytes，35 頁，`pdftotext -layout` 全文檢索）** 【機構型來源，無作者欄】衛生福利部中央健康保險署。《全民健康保險醫療服務給付項目及支付標準部分診療項目修正對照表》。https://www.nhi.gov.tw/ch/dl-42784-106c2884f650466f9e9e63b18b3db16c-1.pdf ——**47054C 一般高壓氧治療 720 點之註逐字：「1.包括氧氣費在內。2.提升兒童加成項目。3.屬西醫基層總額部門院所，本項以原支付點數 600 點申報。」全篇查無適應症條文、查無「放射」字樣。**
- **[S38] PASS（行政院公報 PDF，2026-09-01 實下載；HTTP 200，128,969 bytes，`pdftotext -layout` 全文檢索）** 【機構型來源，無作者欄】行政院公報第 026 卷第 072 期（2020-04-21）衛生勞動篇：衛生福利部中央健康保險署令——全民健康保險非住院診斷關聯群（Tw-DRGs）案件審查注意事項。https://gazette.nat.gov.tw/EG_FileManager/eguploadpub/eg026072/ch08/type2/gov70/num32/Eg.pdf ——高壓氧相關審查原則逐字**僅涵蓋潛水病／減壓病（59002B、59014B、59015B）、一氧化碳與其他毒化物中毒、氣壞疽**三類（含「執行頻率最多 1 天 2 次…治療共計約 10 次為宜」「慢性潛水病如異壓性骨壞死可執行 20 次治療，最多延長至 40 次」）；**全文查無「放射」「放射線」「放射性膀胱炎」「放射性大腸炎」字樣。**

### FAIL ／ NOT-CITABLE（保留紀錄，不得入正文引用）

- **[FAIL-1] 骨盆腔皮膚反應的逐週時間軸。** 檢索紀錄：Europe PMC 以 `TITLE:("radiation dermatitis" OR "skin toxicity") AND ("anal cancer" OR "vulvar" OR "perineum" OR "pelvic")` 與 `("gluteal cleft" OR "intergluteal" OR "inguinal fold") AND ("radiation dermatitis" …)` 檢索；ESTRO 指引全文檢索 `weeks`／`onset`／`resolve`；BC Cancer PDF 全文檢索。**可引的時間句只有兩句**（[S1] 一到四週出現、持續數週；[S2] 療程 >4–5 週延後恢復）。**怎麼寫**：只用這兩個錨，不寫逐週劇本；**乳癌專題的「結束後 2 週達峰」不可移用**。（＝洞 H1）
- **[FAIL-2] 急性泌尿症狀的週次時間窗。** 唯一量化來源 [S12] 用的是累積劑量分布。**怎麼寫**：可寫「累積劑量 16–45 Gy 之間出現的佔四分之三」與「大約落在療程中段」，**不可換算成第幾週**。（＝洞 H2）
- **[FAIL-3] 「鼠蹊皺摺」「臀溝」作為好發位置的逐字來源。** CTCAE 與 ESTRO 只寫 skin folds and creases[S1][S2]。**怎麼寫**：「皺摺與摩擦處」＋「距肛門口越近越重（OR 2.86[S3]）」。（＝洞 H3）
- **[FAIL-4] 放療（非移植）族群中 C. difficile 的比例。** BSG 表格該格原文為「?」＋「no published data and no clinical experience」[S8]。**怎麼寫**：「糞便檢查是必要的一步」，不給比例。（＝洞 H4）
- **[FAIL-5] 攝護腺癌放療後直腸尿道廔管的發生率百分比。** 檢索紀錄：`TITLE:"rectourethral fistula" AND ("radiation" OR "prostate")`（92 筆）、`TITLE:"fistula" AND "prostate cancer" AND (SEER/Medicare/population-based/national)`——回傳者皆為手術系列或無分母之病例系列；唯一提到 prevalence 的回顧摘要數字排版損毀（[S35b]）。**怎麼寫**：寫「低頻但後果嚴重」＋ Chrouser 的關聯[S22]，不給百分比。（＝洞 H5）
- **[FAIL-6] 泌尿端「當天回診」的指引原文；尿滯留與導尿的處置細節。** 未尋得可直接引用之病人端指引條文。**怎麼寫**：以症狀邏輯陳述並明說這是臨床分界；或指路 pc-bowel-urinary 既有的警訊清單。（＝洞 H6）
- **[FAIL-7] 再照射與糖尿病對「廔管」終點的效應量。** 再照射僅在 6 例病例系列中被點名 2 例[S20]；糖尿病只有 EMBRACE-I 的**腹瀉**終點 HR[S10]。**怎麼寫**：兩者寫成「已知的風險方向」，不給數字；**不可把腹瀉的 HR 挪用到廔管**。（＝洞 H7）
- **[FAIL-8] MASCC 對高壓氧治療放射性直腸炎的指引原文。** 僅由 [S15] 轉述；本組未取得該指引本體（未列於 Europe PMC 可取得全文之範圍內，且非 OA）。**怎麼寫**：只可寫「有 2026 年的回顧文章轉述 MASCC 有此推薦」，**不可寫成「MASCC 指引指出」**。
- **[FAIL-9] 台灣：特殊功能敷料於放射性皮膚炎的給付身分。** 健保支付標準全表逐欄檢索未見對應適應症條文[S36]；健保署 HTML 對 curl 為已知 403 行為。**怎麼寫**：「敷料的種類與費用各院不同，由醫療端評估決定，問醫務課或放腫護理師」，不寫有給付也不寫要自費。（與 A／B 組結論一致）
- **[FAIL-10] 台灣：特材 D113-2 膀胱灌注液給付規定之現行版本全文。** 本組未重新取得該附件（pc-bowel-urinary 曾引用 2016 年建檔之行政院公報附件）。**怎麼寫**：一句指路 pc-bowel-urinary，並提醒「現行版本請個管師或醫務課核對」。
- **[FAIL-11] 台灣：高壓氧治療用於放射性組織損傷的健保給付條文。** 檢索紀錄：(a) 健保支付標準開放資料全表 6,012 項逐欄，「高壓氧」4 筆，**47054C 備註無適應症、無「放射」字樣**[S36]；(b) 健保署官方修正對照表 PDF 35 頁全文，47054C 註同上、**全篇無「放射」相關條文**[S37]；(c) 行政院公報 026 卷 072 期審查注意事項全文，高壓氧審查原則**僅涵蓋潛水病、一氧化碳／毒化物中毒、氣壞疽**，**查無「放射」字樣**[S38]；(d) WebSearch 三輪（含 gazette.nat.gov.tw 限定）未回傳可引之健保署官方公告；(e) 多家醫院高壓氧中心網頁列有「健保核定適應症含放射性組織壞死（骨壞死、放射性膀胱炎、放射性大腸炎）」，**但頁面未載公告文號、日期或法規出處，屬機構型二手來源，依 SPEC 固定紅線不引、不點名**。**怎麼寫**：「有代碼（47054C，一般高壓氧治療 720 點），但**放射線造成的組織損傷是否在給付範圍、要不要事前審查、能做幾次，我查到的官方文件沒有寫**——請個管師或醫務課幫你核對現行規定與自付金額。」**兩個方向都不可下結論。**（＝洞 H9）
- **[FAIL-12] 台灣本土的骨盆腔放療晚期出血／廔管發生率、高壓氧使用量。** 未取得可引本土資料。**怎麼寫**：不寫「台灣研究顯示」；媒體數字絕不引。（＝洞 H11）
- **[FAIL-13] HORTIS-I／II／III 的個別結果。** Europe PMC 以 `"HORTIS"` 檢索無獨立試驗條目（回傳多為不相關領域）；HORTIS-IV 之代號由 [S15] 之 Table 3 確認即 Clarke 2008；**HORTIS-III（放射性膀胱炎，ISRCTN19501634）提前結束**[S15]。**怎麼寫**：只寫 HORTIS-IV；提到系列時寫「研究膀胱炎的那一個提前結束、沒有結果可看」。（＝洞 H13）
- **[FAIL-14] NCCN（403，未使用）；PubMed 網頁（CAPTCHA，未使用）。** 照護指引全部改採 ESTRO[S2]／MASCC[S5]／BC Cancer[S1]／BSG[S8]／Cochrane[S27][S28]（符合 SPEC 指定之替代路徑）。
- **[FAIL-15] 直腸癌與膀胱癌各自的放射性廔管發生率。** 檢索紀錄：`TITLE:"fistula" AND ("rectal cancer" AND ("chemoradiotherapy" OR "radiotherapy"))`——回傳者多為吻合口廔管（手術併發症）而非放射性廔管；膀胱癌未取得。**怎麼寫**：廔管數字一律標「子宮頸癌」族群，其他癌別寫「同一個解剖區、風險因子相同，但各癌別的分項數字我查不到」。（＝洞 H8）

---

## 給 SPEC 的修正建議（§八）

1. **紅線 4 建議升級成「有指引原文可抄的三段式」。** 現行 SPEC 寫「寫真實機率與風險因子，不可寫成換技術就能避免、也不可寫成不用擔心」——查證後這三件事都有現成的、可逐字核對的錨：
   （a）**真實機率**＝EMBRACE-I 5 年 G≥3 廔管 3.2%[S16]（而且那就是最現代的技術，直接堵住「換技術就能避免」）；
   （b）**風險因子**＝抽菸 OR 5.14[S18]、IVA 期 OR 6.87[S19]、bevacizumab OR 4.03／4.71[S21]、放療後器械操作 81%[S22]；
   （c）**「腫瘤造成 vs 治療造成」**＝BSG 原文「rule out disease recurrence before assuming that it is secondary to radiation injury」[S8]＋膀胱侵犯者 12.8% 對排除侵犯者 0.7% 的對照[S17][S14]。
   建議 SPEC §三紅線 4 明列這三個錨，審稿時可逐字核對。
2. **C1 的「好發位置」建議修訂措辭。** SPEC §四與 §六（fig-pel-skin-sites）寫「鼠蹊、臀溝、會陰」——**可引證據只到「皺摺與摩擦處」**（CTCAE 原文[S1]）＋「腫瘤距肛門口 ≤5 cm 風險 OR 2.86」[S3]＋「肛門癌與外陰癌是高風險癌別」[S2]。建議 `fig-pel-skin-sites` 的位置標注改為「皺摺與摩擦處」並以「離肛門口的距離」作為風險軸，**不逐一點名三個解剖構造**（FAIL-3）。
3. **`fig-pel-timeline` 的四條時間軸，只有兩條有可引來源。** 腸道：BSG 的「第二週開始／最後一週達峰／照完至少再 1–2 週／大分次可能照完才開始」[S8]——**四段全部有原文**；晚期出血：「幾個月後開始／三年內達峰／可持續十年以上」[S8]。皮膚只有「一到四週出現、持續數週」[S1]；泌尿**只有累積劑量**沒有週數[S12]。建議圖上把皮膚與泌尿兩條畫成**不標刻度的區間帶**，腸道與晚期出血兩條才標節點（與 FAIL-1／FAIL-2 一致）。
4. **一條要交叉給 A 組 A4 的原文。** BSG 2025 逐字：「New approaches aimed at limiting toxicity through attempting to exclude the GI tract from the radiation field（**endorectal spacers**, balloons, rectal emptying）**have not improved GI outcomes**」[S8]。這與 SPEC 紅線 3「SpaceOAR 不是本科項目、不可寫成人人該做」同向，且是**指引層級**的句子，比 A 組現有材料更硬。建議 §三紅線 3 補一句：**間隔物的好處寫「劑量學」那一格，臨床腸胃道結果那一格有指引原文說沒有改善**——但務必標明這是**急性毒性預防**脈絡，不可外推到晚期直腸毒性（本組未查證該終點）。
5. **C2 的飲食段建議在 SPEC 裡先定好措辭。** 這是全 C 組最容易被讀反的一格：指引點名的方向是**高纖**（29.3），但同一份文件說整批飲食介入**證據不足、在臨床試驗之外不應使用**[S8]。建議 SPEC 明訂 C2 的飲食段必須「兩句並陳」，且結論句落在「問你的營養師與治療團隊」，避免寫成「該吃高纖」或「低渣沒用」。
6. **建議在 §五交叉引用歸屬中補一條「坐浴」的邊界。** BC Cancer 對會陰／直腸放療病人的每日坐浴建議是**皮膚照護**[S1]；rc-diarrhoea 已寫「查無指引等級證據支持坐浴治療急性放射性直腸炎」。兩者相容但極易被讀成矛盾——建議 SPEC 明訂：**坐浴寫在 C1（皮膚），C2 不重寫；C1 寫時必須加「這是照顧皮膚的做法，不是治療腸子的方法」。**
7. **§七台灣端查證清單建議更新「高壓氧」那一格的結案狀態。** 已結案為 **FAIL**：健保支付標準有 47054C（720 點）但**無適應症條文**[S36][S37]，可取得的公報審查注意事項**只涵蓋潛水病／中毒／氣壞疽**[S38]。建議 SPEC 直接寫明「這一格的答案是『查不到官方文件』，正文一律導向醫務課，兩個方向都不下結論」。同時建議補入本組新查到、C4 可用的四個健保項目：**49023C（直腸內視鏡止血 2,392 點）、49026C（經大腸鏡結腸止血 8,044 點）、50011C（膀胱灌注 260 點）、33105B（腸胃道出血栓塞 10,800 點）**[S36]，以及「氬離子／電漿／福馬林在全表 0 筆」這個可寫的事實。
8. **建議 §四把 C4 的收尾方向定在「可行動的那三件事」。** 抽菸在 C4（廔管多變項唯一顯著因子[S18]）與 C2（BSG 明列為放療前應處理者[S8]）兩篇都出現；營養與 BMI 同樣橫跨兩端[S18][S19]；第三件是「放療後任何要在照射過的腸子或膀胱上動刀動燒的處置，都要讓做的人知道你照過放療」[S8][S22]。這樣 C4 不會停在「有哪些解方」的清單感，而且完全不越過紅線 4。

---

## 給撰稿人的一句話總結

C 組查證後最大的三個收穫：一是**紅線 4 有現成的三段式錨**——3.2%（現代技術下的 5 年 G≥3 廔管[S16]）堵住「換技術就能避免」，12.8% vs 0.7%（有無膀胱侵犯[S17][S14]）把「腫瘤造成的」與「治療造成的」分開，而 BSG 那句「先排除復發再說是放療造成的」[S8] 讓 C4 不必自己立規矩；二是**高壓氧不能寫成有效或無效，只能寫成「兩個隨機試驗方向相反」**——HORTIS-IV 的 NNT 3[S23] 與 HOT2 的「no evidence」[S24] 必須同段出現，Cochrane 只寫到 may be justified[S27]，BSG 只寫到「randomised data are contradictory」[S8]，而副作用那張表（近視 25–100%、每 2,000–3,000 次一次氧中毒、30–40 次 × 90 分鐘的時間成本[S15]）是這一段最誠實的部分；三是**飲食那格的方向與大家以為的相反**——BSG 點名的是高纖不是低渣，但同一份文件說整批飲食介入證據不足、試驗外不應使用[S8]，兩句必須並陳。時間軸方面，腸道是唯一四段全有原文的（第二週開始、最後一週達峰、照完至少再 1–2 週、大分次可能照完才開始[S8]），皮膚只有「一到四週」[S1]，泌尿**只有累積劑量沒有週數**[S12]——洞列了十四條，台灣端最重要的一條是**高壓氧用於放射性組織損傷的給付條文查無官方文件**（支付標準全表、健保署 PDF、行政院公報三路皆 0 筆），寫的時候兩個方向都不要猜，直接導向醫務課。
