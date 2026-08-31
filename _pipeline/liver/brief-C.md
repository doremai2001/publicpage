# Brief C — 肝癌專題療程照護群（C1–C5）

研究員：Group C｜查證日期：2026-08-30｜期刊書目資料全部經 Europe PMC REST 逐筆核對（含 DOI、卷期頁、PMID）；指引原文引語出自可取得之全文（NCBI PMC 全文 XML、學會官方網站 PDF）；藥品仿單以 openFDA drug/label.json 取全文、DailyMed 官方頁面確認 HTTP 200；台灣官方文件實際下載全文檢索。
引用規則：**只有標 PASS 的來源可以進正文引用。** FAIL / NOT-CITABLE 條目保留，供作者知道查過什麼、哪些話只能寫「查不到可引用的來源」。
IDSA 發燒定義已於本次**第三度獨立查證**（Europe PMC 書目＋OUP 原文），非沿用。

## ⚠ 五件與 SPEC 假設不同形狀的事（動筆前必讀）

1. **durvalumab+tremelimumab 不是台灣缺口。** 健保藥品給付規定 9.69 的「晚期肝細胞癌第一線用藥」自 114/2/1 起寫成「限 atezolizumab 與 bevacizumab 併用，**或限 durvalumab 與 tremelimumab 併用**」，兩組併用與 sorafenib、lenvatinib 四者**僅得擇一給付，不得互換**[S42]。SPEC §四寫的「durva+treme status (likely gap)」已過期，C3 要照給付現況寫。
2. **紅線 5 的胃鏡要求有台灣官方版本。** 健保 9.69 條文的排除條件原文：「有上消化道出血之疑慮且未接受完全治療 **(須有半年內之內視鏡評估報告)**」[S42]——與 IMbrave150 試驗設計（治療前 6 個月內須評估靜脈瘤）[S15]、AASLD 2023 的強建議（所有考慮 atezo+bev 者都應做胃鏡）[S10] 三者同向。紅線 5 不必只靠國外文獻，健保條文本身就是錨。
3. **cabozantinib 在台灣沒有肝癌給付條文。** 健保 9.74 只有腎細胞癌與甲狀腺癌適應症[S42]。二線風景段落的正確台灣標註：regorafenib 有（9.51）、ramucirumab 有（9.92，AFP≥400）、cabozantinib 查無肝癌條文——寫「這一項要跟醫院確認自費與否」，不可寫成「健保不給付」（只能支持「查無給付條文」）。
4. **C1 標題的「兩週」就是健保包裹的官方定義。** 37047B 支付規範原文：「全療程為二週且分次治療以六次(含)為限，採包裹給付」[S41]；衛福部公告原文：「以一個療程（約1至2週），每1至3天照射1次，總計於6次以內」「透過呼吸調控及影像導航」[S40]。定位到首次治療間隔的天數則**查無可引用來源**（FAIL-1）——時程只能寫到官方定義的療程長度為止，不可自己發明「定位後 X 天開始」。
5. **「栓塞後發燒 vs 感染」查證後的證據形狀：只有量的對比，沒有時間門檻。** 可引的是：安慰劑組僅 10.2% 在 TACE 後 120 小時內完全沒有發燒/食慾不振/噁心嘔吐（等於約九成的人至少中一項）[S19]；對照肝膿瘍合併發生率 0.54%、一旦發生死亡率 7.73%[S20]。「發燒超過第幾天／幾度就是感染」**查無可引用門檻**（FAIL-5）——C2 與 C5 只能寫成質性區分（前幾天的發燒常見且會退；發燒**越來越燒**、合併寒顫、腹痛加劇、超過一週不退，要當天回來），不可編一個數字。

---

## C1 `lv-sbrt-weeks`〈SBRT 的兩週實際長怎樣〉

### Key facts

**分次方案（3–6 次，全部可引）**

- AASLD 2023 原文把 SBRT 定義為「stereotactic body radiation therapy (SBRT) **delivered in five or fewer sessions**」[S10]。
- 前瞻試驗實例：Yoon 2020（≤5 cm、中位 1.3 cm）45 Gy／3 次、連續 3 天[S4]；Bujold 2013（大腫瘤、55% 血管侵犯）24–54 Gy／6 次[S5]；Mendiratta-Lala 系列 24–50 Gy／3–5 次[S7]。
- 台灣官方版：37047B「全療程為二週且分次治療以六次(含)為限」、需事前審查、包裹給付 213,662 點；未完成全療程按比例核扣[S41]。衛福部公告：每 1–3 天照射 1 次、約 1–2 週完成，對照傳統放療 5–6 週約 30 次[S40]。

**呼吸移動管理（各選項的可引描述）**

- AAPM TG-76（2006）是分類學的標準引用，涵蓋五類技術：**涵蓋移動法（motion-encompassing）、呼吸閘控（respiratory gating）、閉氣（breath-hold）、強制淺呼吸（forced shallow-breathing，即腹部加壓）、呼吸同步技術（respiration-synchronized）**；其臨床流程建議：可能時逐病人量測腫瘤移動幅度，**移動大於 5 mm** 且病人可耐受時，使用呼吸移動管理是合適的[S1]。
- 各技術的細部優劣比較（哪家醫院用哪種）不寫——TG-76 之外的單一機構經驗不引。衛福部公告可補一句「健保給付條件即預期以呼吸調控及影像導航執行」[S40]。

**定位標記（fiducial）：程序與風險**

- Kothary 2009（139 次植入，其中肝臟 34 次）：主要併發症 5%、次要併發症 17.3%；6 次（4.3%）標記移位需再處理；結論「風險與傳統經皮器官切片相近」[S2]。氣胸主要發生在肺部植入，肝臟植入不是零風險但低。
- Dutta 2020（前瞻，36 位 HCC 做 CyberKnife，108 顆標記）：置放時間學習曲線後平均 14.3 分鐘（早期 42.2 分鐘）；72% 病人疼痛分數 0–1；14% 需日間留觀（2 例輕微氣胸、3 例疼痛）；**1 例（3%）血胸死亡**——這是差肝功能、廣泛腫瘤族群的真實風險，誠實寫[S3]。Child-Pugh 分數差、體能狀態差者併發症機率較高[S3]。
- 並非每台機器都需要 fiducial；是否植入由治療平台與影像條件決定——這句寫成一般敘述即可，不需引用。

**急性副作用（帶分母）**

- **小腫瘤、好肝功能的形狀（Yoon 2020，n=50，全部 Child-Pugh 5–6 分）**：最常見是輕度疲倦與食慾不振；疲倦 grade 1 佔 4%、噁心 grade 1 佔 4%、AST/ALT 上升 grade 1 32%／grade 2 2%、鹼性磷酸酶上升 14%、膽紅素上升 grade 2 4%；**無任何 grade ≥3**；所有病人完成療程無中斷；Child-Pugh 上升 ≥2 分者 2 位（4%）[S4]。
- **大腫瘤、晚期族群的形狀（Bujold 2013，n=102，中位 GTV 117 mL、55% 血管栓塞）**：grade ≥3 毒性 30%；7 位死亡可能與治療相關[S5]。兩組數字並列時**族群標籤不可省**——同一個治療在兩個族群的毒性差一個數量級。
- 隨機對照下的相對安全性：Xi 2025（復發單顆 ≤5 cm，SBRT 83 vs RFA 83）急性與晚期不良事件發生率兩組相當（p=0.436／0.715）[S6]。
- 晚期反應供 C2 交叉引用：古典 RILD（無黃疸肝腫大＋腹水＋ALP 上升 >2 倍）典型發生在治療後 **2 週到 3 個月**[S9]。

**治療後影像變化不是復發（focal liver reaction／持續顯影的誠實段落）**

- Mendiratta-Lala 2018（10 顆經病理或 AFP 證實治療成功的 HCC）：**4/10 在 SBRT 後 3–12 個月仍有中央動脈相顯影、9/10 仍有 wash-out**；腫瘤旁肝實質早期（3–6 個月）充血、晚期（6–12 個月）包膜回縮與延遲顯影；結論：大小不增加的前提下，持續顯影「may not represent residual viable tumor」[S7]。
- Mendiratta-Lala 2019（67 顆，追蹤至 3 年）：治療後 12 個月內腫瘤縮小 66%、大小不變 34%；**58% 有持續動脈相顯影**；以 mRECIST 在 3–6 個月評估，只有 25% 達「完全反應」、75% 是「疾病穩定」——但這些都是控制住的腫瘤；結論：mRECIST 用在 SBRT 後早期「should be used with caution」[S8]。
- QUANTEC 補充：放療後 2–3 個月 CT 上短暫的組織密度下降是常見且臨床無意義的，「不應與腫瘤惡化或不可逆肝損傷混淆」[S9]。
- 這一段的病人語言：燒灼是「立刻看空洞」、SBRT 是「慢慢看它熄滅」——影像科和放腫科看的是「有沒有變大」，不是「有沒有顯影」。

### Claim ceiling

- 可寫：「肝臟 SBRT 通常 3–6 次、兩週內做完（健保包裹即以二週六次為上限）」；「小腫瘤好肝功能的前瞻試驗中沒有 grade 3 以上副作用，最常見是輕度疲倦、食慾差、短暫肝指數上升（32% grade 1）」；「大腫瘤晚期族群 grade ≥3 毒性 30%」；「fiducial 植入的風險與肝臟切片相近（主要併發症 5%）」；「治療成功的腫瘤半數以上在一年內仍會顯影，顯影不等於復發，看的是大小」。
- **不可寫**：「SBRT 沒有副作用」「做完就知道有沒有效」；不可把 Yoon 的 0% grade ≥3 寫成通則（那是 ≤5 cm、CP 5–6 分的族群）；不可寫「定位後幾天內開始治療」（無來源）；不可寫每次治療躺多久幾分鐘（無來源，FAIL-2）；不可寫成「影像顯影都不用理」——**變大就是另一回事**，且 mRECIST 的猶豫只適用於 SBRT 後早期。
- 肝功能毒性的深度（RILD 機轉、劑量限制、Child-Pugh B 數字）歸 B2，本篇一句話指路；SBRT vs 其他治療的比較歸 B1，本篇不比。

### Caveats

- Dutta 的 1 例死亡要放進 fiducial 風險段，不可只寫「安全」；同時標明該族群全部有門脈癌栓、是高風險群[S3]。
- Yoon 的血清膽紅素、AST/ALT 短暫上升多在 grade 1——「肝指數會小幅波動、多數自行回穩」可寫，但 Child-Pugh 掉 2 分的 4% 也要寫，並指向 C2 的求醫門檻。
- 治療時程「兩週」是台灣健保包裹定義；自費或特殊平台可能不同——寫「以你醫院的治療計畫為準」。

### 台灣現況

- 37047B（肝膽適應症原文：原發性肝膽單一病灶、Child-Pugh A–B、≤5 cm、無法接受或失敗於手術／栓塞／電燒）213,662 點、需事前審查、二週六次包裹[S41]；衛福部 104 年公告全文可引（含「呼吸調控及影像導航」字樣）[S40]。條件外（多顆、>5 cm、再照射）即自費——金額查無官方公告，寫「向醫務課確認」。
- 呼吸調控本身在光子 SBRT 包裹內無獨立收費項目可引；質子的呼吸調控加價屬 B3 範圍，本篇不寫。

---

## C2 `lv-warning-signs`〈哪些狀況要當天回醫院〉【急症警語主場】

### Key facts

**肝性腦病變（可引的分級與早期徵象）**

- AASLD/EASL 2014 指引的 West Haven 分級原文（全文 PDF 經 aasld.org 官方站取得）[S11]：
  - Grade I：**「Trivial lack of awareness／Euphoria or anxiety／Shortened attention span／Impairment of addition or subtraction／Altered sleep rhythm」**（輕微失神、亢奮或焦慮、注意力縮短、簡單加減算不出來、睡眠節律改變）。
  - Grade II：「Lethargy or apathy／**Disorientation for time**／Obvious personality change／Inappropriate behavior／Dyspraxia／**Asterixis**」（嗜睡冷漠、時間定向感喪失、明顯個性改變、不合宜行為、動作失用、撲翼樣顫抖）。
  - Grade III：嗜睡到半昏迷、對刺激仍有反應、明顯混亂；Grade IV：昏迷。
  - 指引原文：早期的個性改變（冷漠、易怒、失抑制）**常是家屬先注意到**（"personality changes...may be reported by the patient's relatives"）；日夜顛倒的過度白天嗜睡常見；ISHEN 共識以「**時間定向感喪失或撲翼樣顫抖出現**」為顯性腦病變的起點[S11]。
- 病人語言的門檻：睡眠日夜顛倒、算不出簡單的數字、家人說「他怪怪的」→ 提前回診；**搞不清楚今天星期幾、手抖成撲翼樣、叫不太醒 → 當天回醫院**[S11]。

**黑便嘔血（立刻行動）**

- AASLD 2024 門脈高壓與靜脈瘤指引原文：「**AVH remains an emergent complication of cirrhosis and requires timely and effective management to prevent short-term mortality. Even with therapeutic advancements for AVH, 6-week mortality still ranges from 10% to 15%.**」（急性靜脈瘤出血仍是肝硬化的急症，即使治療進步，6 週死亡率仍 10–15%）[S12]。大顆靜脈瘤年出血率約 15%[S12]。
- 寫法：黑便（柏油樣）、嘔血或嘔咖啡渣——**不是掛號問題，是叫救護車問題**。死亡多發生在 Child-Pugh C；肝功能好的人死亡率低[S12]——這句用來說明「快就有用」，不是用來安撫。

**發燒合併腹水（自發性細菌性腹膜炎）**

- EASL 2018 失代償肝硬化指引（easl.eu 官方 PDF）[S13]：
  - 診斷門檻：腹水嗜中性球 **>250 cells/µl**。
  - 症狀清單原文：局部症狀（腹痛、腹部壓痛、嘔吐、腹瀉、腸阻塞）；全身發炎徵象（**發燒或低體溫、寒顫**、白血球異常、心搏過速、呼吸過速）；肝功能惡化；肝性腦病變；休克；腎衰竭；腸胃道出血。
  - **「SBP may be asymptomatic, particularly in outpatients」**——可以完全沒症狀，所以「有腹水的人發燒」本身就夠格。
  - 延遲診斷性腹水穿刺（入院 >12 小時）死亡率增加 **2.7 倍**；「Empirical antibiotic therapy must be initiated immediately after the diagnosis of SBP」[S13]。
- 病人門檻：**有腹水（或最近才抽過腹水）＋發燒或發冷或新的腹痛 → 當天回醫院，並預期會被抽腹水**[S13]。

**黃疸急升**

- EASL 2018 對失代償的定義原文：「decompensated phase, marked by the development of overt clinical signs, the most frequent of which are **ascites, bleeding, encephalopathy, and jaundice**」[S13]——黃疸與腹水、出血、腦病變並列為四大失代償訊號。皮膚眼白在幾天內明顯變黃、茶色尿＋腹圍變大或變昏沉 → 當天回醫院。

**發燒的通用定義（IDSA，本次第三度獨立查證）**

- IDSA 2010 嗜中性球低下發燒指引原文：發燒＝「a single oral temperature measurement of **≥38.3°C** (101°F) or a temperature of **≥38.0°C** (100.4°F) **sustained over a 1-h period**」；嗜中性球低下＝ANC <500/mm³ 或預期 48 小時內降到 <500[S14]。
- 肝癌全身治療不以骨髓抑制為主，但免疫治療＋標靶的病人發燒同樣不可輕忽；引用時標明這是 IDSA 對癌症病人發燒的指引定義，**不要把 38 度寫成無出處的通用門檻**。

**藥物列（每列具體症狀＋來源）**

*Atezolizumab + bevacizumab（Tecentriq 仿單 IMbrave150 安全性章）*
- 致死不良反應 4.6%；**最常見死因是腸胃道與食道靜脈瘤出血（1.2%）**與感染（1.2%）；嚴重不良反應 38%，最常見為**腸胃道出血 7%**、感染 6%、發燒 2.1%[S15]。
- 試驗設計原文：「Patients were required to be evaluated for the presence of varices within 6 months prior to treatment, and were excluded if they had variceal bleeding within 6 months...untreated or incompletely treated varices with bleeding, or high risk of bleeding」[S15]——治療前胃鏡是這個組合的內建前提（完整論述歸 C3）。
- Bevacizumab 端（Avastin 仿單）：**腸胃道穿孔 0.3–3%**，多數在第一劑後 50 天內，表現為腹痛（可合併發燒、腹部僵硬）→ 永久停藥[S16]；嚴重出血較化療高至 5 倍，近期咳血者不得使用[S16]；傷口癒合併發症——擇期手術前後各至少停 28 天，**任何手術（含拔牙）排程要主動告知腫瘤科**[S16]；高血壓危象與 PRES（劇烈頭痛、視力改變、抽搐）→ 停藥[S16]。
- Atezolizumab 端（免疫相關不良反應，仿單單獨用藥數據）：免疫性肺炎 3%（呼吸喘、咳嗽加劇）；免疫性大腸炎 1%（腹瀉、腹痛、血便）；免疫性肝炎 1.8%；腎上腺功能不全 0.4%（極度倦怠、噁心、低血壓）；腦下垂體炎（頭痛、視野缺損）；甲狀腺功能異常——仿單要求治療期間定期驗肝功能、肌酸酐與甲狀腺功能[S15]。門檻寫法：**新的喘咳、一天多次的水便或血便、皮疹起水疱、眼白變黃、極度倦怠站不起來 → 當天聯絡治療團隊**，不要自己吃止瀉藥或退燒藥撐過去[S15]。

*Lenvatinib（Lenvima 仿單，REFLECT/HCC 數據）*
- 高血壓 45%（grade 3 24%），**新高血壓或惡化的中位發生時間是開始吃藥後 26 天**——前幾週在家量血壓不是儀式[S17]。
- 出血事件 23%（G3–4 4%）；REFLECT 中 grade 3–5 出血 5%、含 **7 例致死出血**[S17]。
- 肝性腦病變 8%（sorafenib 組 3%）；grade 3–5 腦病變 5%[S17]——TKI 也會把腦病變催出來，症狀同上面 West Haven 段。
- 手足症候群（PPE）27%；瘻管或腸胃道穿孔 2%（任何等級穿孔即永久停藥）[S17]。
- 門檻寫法：血壓量到藥物壓不住、任何黑便/血尿/咳血、手腳破皮到走不了路、突然變得昏沉 → 當天聯絡[S17]。

*Sorafenib（Nexavar 仿單，SHARP/HCC 數據）*
- 手足皮膚反應 21%（grade 3 8%；安慰劑組 3%）；**通常出現在開始治療的前六週**[S18]。
- 高血壓 9.4%（安慰劑 4.3%）；仿單要求**前 6 週每週量血壓**[S18]。
- 食道靜脈瘤出血 2.4%（安慰劑組 4%——SHARP 中相近；出血風險是肝硬化本身的，不因吃藥消失）[S18]；腸胃道穿孔 <1%[S18]。
- 門檻寫法：手腳紅腫痛到影響走路或破皮、血壓失控、黑便嘔血 → 當天聯絡；破皮前的減量時機是回診要主動講的事[S18]。

*TACE 後（栓塞後症候群 vs 感染——質性區分，無可引時間門檻）*
- 發燒、食慾不振、噁心嘔吐是 TACE 後「最常見的不良反應」；安慰劑組只有 10.2% 在 120 小時內完全沒有這三項[S19]——**前幾天的發燒常見、多會自己退**（完整照護歸 C5）。
- 肝膿瘍合併發生率 0.54%（32 篇、254,408 人次），**一旦發生死亡率 7.73%**[S20]。
- 區分寫法（不發明數字）：發燒**越來越高**、合併寒顫、腹痛不減反增、黃疸出現、或返家後**又燒回來** → 當天回醫院；平順下降的低燒＋照常進步的食慾 → 照 C5 的路徑觀察。

*SBRT 後*
- 急性期（兩週內）看 C1；**晚反應的窗口是治療後 2 週到 3 個月**：古典 RILD 的樣子是「無黃疸的肝腫大＋腹水＋鹼性磷酸酶上升」；非古典 RILD 是 Child-Pugh 掉 ≥2 分或転氨酶 >5 倍[S9]。小腫瘤前瞻試驗中 Child-Pugh 掉 ≥2 分者 4%[S4]。
- 門檻寫法：SBRT 結束後三個月內，肚子變大、褲頭變緊、體重莫名增加（腹水）、或人變昏沉 → 提前回診，不要等下次排程[S9][S11]。

### 急症警語總表

> 供全系列交叉引用。每一列「狀況 → 門檻 → 來源」。其他篇引用時只保留與自己直接相關的一兩列並指向本篇。

| # | 狀況 | 當天行動門檻 | 來源 |
|---|---|---|---|
| 1 | 肝性腦病變 | 搞不清楚時間（星期幾/月份）、手撲翼樣抖動、叫不太醒 → 當天回醫院；睡眠日夜顛倒、家人覺得個性變了 → 提前回診 | [S11] |
| 2 | 靜脈瘤出血 | 黑便（柏油樣）、嘔血、嘔咖啡渣 → 立刻急診（急性靜脈瘤出血 6 週死亡率 10–15%） | [S12] |
| 3 | 自發性細菌性腹膜炎 | 有腹水＋發燒或發冷或新腹痛 → 當天回醫院（可無症狀；延遲穿刺 >12 小時死亡率 2.7 倍） | [S13] |
| 4 | 黃疸急升 | 數天內眼白皮膚明顯變黃＋茶色尿，尤其合併腹水或昏沉 → 當天回醫院（失代償四訊號之一） | [S13] |
| 5 | 發燒（治療中通用） | 單次口溫 ≥38.3°C，或 ≥38.0°C 持續 1 小時（IDSA 指引定義，出處要標明） | [S14] |
| 6 | atezo+bev：出血 | 任何黑便、嘔血、咳血、大片瘀青 → 立刻急診（IMbrave150 死亡原因第一位是靜脈瘤出血 1.2%；嚴重腸胃道出血 7%） | [S15] |
| 7 | atezo+bev：穿孔 | 腹痛合併發燒或腹部僵硬 → 當天（bevacizumab 腸胃道穿孔 0.3–3%，多在第一劑後 50 天內） | [S16] |
| 8 | atezo+bev：免疫事件 | 新的喘咳（肺炎 3%）、一天多次水便或血便（大腸炎 1%）、眼白變黃（肝炎 1.8%）、極度倦怠低血壓（腎上腺 0.4%）、劇烈頭痛視野缺損 → 當天聯絡，勿自行吃止瀉/退燒藥 | [S15] |
| 9 | atezo+bev：手術與拔牙 | 任何手術或拔牙排程 → 主動告知腫瘤科（擇期手術前後各停藥至少 28 天） | [S16] |
| 10 | lenvatinib | 血壓藥物壓不住（高血壓 45%、中位 26 天出現）、黑便/血尿/咳血（出血 23%、REFLECT 7 例致死）、突然昏沉（腦病變 8%）、手腳破皮走不了路（PPE 27%） → 當天聯絡 | [S17] |
| 11 | sorafenib | 手腳紅腫破皮（HFSR 21%、前六週）、血壓失控（前 6 週每週量）、黑便嘔血（靜脈瘤出血 2.4%）、劇烈腹痛（穿孔 <1%） → 當天聯絡 | [S18] |
| 12 | TACE 後 | 發燒越燒越高、寒顫、腹痛加劇、黃疸、退了又燒 → 當天回醫院（膿瘍 0.54%、死亡率 7.73%）；前幾天遞減的燒與倦怠常見（約九成至少一項症狀） | [S19][S20] |
| 13 | SBRT 後 | 治療後 2 週–3 個月：腹圍變大、體重莫名增加、人變昏沉 → 提前回診（古典 RILD 窗口） | [S9][S4] |

### Claim ceiling

- 可寫：上表每一列（帶數字帶出處）；「SBP 可以完全沒有症狀，所以腹水＋發燒本身就夠格」；「黑便是急診等級，不是門診等級」；「atezo+bev 最需要記住的一個數字：死亡原因第一位是靜脈瘤出血」。
- **不可寫**：「如有不適請就醫」式的無藥名警語；把 38 度寫成無出處門檻；把 TACE 後發燒寫成「都正常」或發明「第 X 天還燒就是感染」；把免疫副作用寫成「很少見不用擔心」（單獨用藥的個別發生率低，但**任何器官都可能**、且會致命——仿單原文）；不可暗示自行停藥（停藥決定歸團隊；本篇的動作動詞只有「當天聯絡／當天回醫院／立刻急診」）。
- 抗病毒藥不可自行停（爆發性肝炎）是 D 組主場——本篇表中不列，正文一句話指向 D3/A4。

### Caveats

- 本篇是全系列急症警語主場：C1、C3、C4、C5 與 B、D 組各篇提到症狀時，只保留與自己直接相關的列並指向本篇（SPEC §五）。
- West Haven 分級表在指引中同時標注「Grade I 的臨床發現通常不可重現」[S11]——寫早期徵象時要誠實說「這一級連醫師都難以客觀確認，所以家屬的直覺值得被講出來」。
- Kaplan 2024 引語出自 OA 接受稿（SDU 機構典藏），與正式版頁碼不同；引用時用 DOI 連結。
- 免疫相關不良反應的處置細節（類固醇等）不寫——那是團隊的事，病人端只需要「什麼要當天講」。

### 台灣現況

- 健保 9.69 條文的內視鏡要求（半年內評估報告）是 C3 主場，本篇一句話帶過[S42]。
- 台灣官方的「癌症病人急診就醫指引」類頁面：未檢索到可引用的專屬頁面——警語門檻全部以國際指引與仿單為出處，不假造官方來源。

---

## C3 `lv-systemic-days`〈標靶與免疫治療的日子〉【紅線 5】

### Key facts

**IMbrave150（atezolizumab + bevacizumab）——效益與風險同段**

- 初次分析（Finn 2020，n=501，2:1）：死亡 HR **0.58**（95% CI 0.42–0.79）；12 個月 OS **67.2% vs 54.6%**；中位 PFS 6.8 vs 4.3 個月（HR 0.59）；G3–4 不良事件 56.5% vs 55.1%；G3–4 高血壓 15.2%[S22]。
- 更新分析（Cheng 2022，中位追蹤 15.6 個月）：中位 OS **19.2 vs 13.4 個月**（HR 0.66，95% CI 0.52–0.85）；治療相關 G3/4 43% vs 46%；治療相關 G5 2% vs <1%[S23]。
- **族群標籤每次都帶**：全身治療初治、幾乎全為 Child-Pugh A、排除高出血風險者[S15][S22]。
- **紅線 5 的三層錨（全部逐字可引）**：
  1. 試驗設計（仿單轉述）：「required to be evaluated for the presence of varices within 6 months prior to treatment」、排除未治療或未完全治療之出血靜脈瘤與高出血風險者[S15]。
  2. 指引（AASLD 2023 原文）：「**all patients considered for atezolizumab plus bevacizumab should undergo an esophagogastroduodenoscopy (EGD)**」（Level 5, Strong Recommendation）；大顆靜脈瘤建議至少一次結紮；「patients who had incompletely treated varices or who were at high risk for bleeding were excluded...underscoring the importance of appropriate endoscopic evaluation before atezolizumab plus bevacizumab is initiated」；高出血風險者「may instead be considered for durvalumab plus tremelimumab」[S10]。
  3. 台灣健保條文：排除「有上消化道出血之疑慮且未接受完全治療 **(須有半年內之內視鏡評估報告)**」[S42]。
- 風險數字（仿單）：致死不良反應 4.6%、死因第一位靜脈瘤出血 1.2%、嚴重腸胃道出血 7%[S15]——效益（HR 0.58）與這組數字**必須同段出現**。

**HIMALAYA（durvalumab + tremelimumab，STRIDE）——誠實版**

- 主分析（Abou-Alfa 2022，n=1,171）：中位 OS **16.43 vs 13.77 個月**（sorafenib）；OS HR **0.78**（96.02% CI 0.65–0.93）；36 個月 OS 30.7% vs 20.2%；G3/4 治療引發不良事件 50.5% vs 52.4%；durvalumab 單用非劣於 sorafenib（HR 0.86）[S24]。
- 5 年更新（Rimassa 2025）：OS HR 0.76；**60 個月存活 19.6% vs 9.4%**——「五個人有一個活過五年」是可引句，但要註明是晚期試驗族群[S25]。
- 亞洲次族群（Lau 2025，含台灣；n=479）：OS HR 0.68；港台次族群（n=141）HR 0.44（95% CI 0.26–0.77）——**探索性、樣本小、CI 寬**，只能寫「方向一致」，不可寫成「對台灣人效果加倍」[S26]。G3/4 治療相關不良事件亞洲組 19.9% vs sorafenib 30.5%[S26]。
- 與 atezo+bev 的差異寫法：STRIDE 不含抗血管新生藥，出血風險結構不同，AASLD 把它列為高出血風險者的替代選項[S10]——但**兩組合從未頭對頭比較**，不可寫誰優。CTLA-4 加入使免疫副作用機率升高（AASLD 原文：兩種 ICI 併用 irAE 風險較高）[S10]。

**REFLECT（lenvatinib）**

- 非劣性試驗（n=954）：中位 OS 13.6 vs 12.3 個月（HR 0.92，95% CI 0.79–1.06，達非劣性）；lenvatinib 最常見不良事件：高血壓 42%、腹瀉 39%、食慾下降 34%、體重下降 31%；sorafenib：PPE 52%、腹瀉 46%[S27]。**證明的是不劣於，寫成優於就是超過**。

**二線風景（一段誠實話）**

- Regorafenib（RESORCE，sorafenib 耐受且惡化者）：OS 10.6 vs 7.8 個月（HR 0.63）；G3/4 高血壓 15%、手足 13%[S28]。
- Cabozantinib（CELESTIAL，sorafenib 後）：OS 10.2 vs 8.0 個月（HR 0.76）；G3/4 事件 68%（安慰劑的近兩倍）[S29]。
- Ramucirumab（REACH-2，**AFP≥400 ng/mL** 限定）：OS 8.5 vs 7.3 個月（HR 0.710）——第一個生物標記選族群的陽性第三期[S30]。
- 誠實句：二線的絕對獲益以「月」計、都是 Child-Pugh A 族群的數字；**一線用了免疫組合之後的最佳二線順序，隨機證據還沒跟上**（此句可由台灣條文的「治療失敗後不得申請 regorafenib/ramucirumab」側寫制度端的空白[S42]）。
- 免疫相關副作用細節與求醫門檻→指向 C2（表列 8）。

### Claim ceiling

- 可寫：上述每個數字（帶試驗名、帶族群標籤）；「atezo+bev 治療前胃鏡是試驗設計、國際指引強建議、台灣健保條文三位一體的硬要求」；「HIMALAYA 五年還有近兩成的人活著，同期 sorafenib 組不到一成」；「lenvatinib 證明的是不輸」；「二線每一條都有隨機證據，但獲益以月計」。
- **不可寫**：「免疫治療優於標靶」的無標籤句（各試驗對照組都是 sorafenib，彼此沒有頭對頭）；港台 HR 0.44 不可寫成主結論；「durva+treme 不用做胃鏡」（AASLD 只說高風險者可**考慮**它作替代，胃鏡評估本身仍是判斷風險的前提[S10]）；不可給任何用法用量（STRIDE 的單次 priming 劑量寫法只能當背景）；Child-Pugh B 的全身治療數據本組未查證——寫「試驗幾乎都是 Child-Pugh A，B 的人要跟醫師個別談」。
- 效益數字與出血/irAE 風險不可拆段（好處與代價同段）。

### Caveats

- IMbrave150 主論文（NEJM）與更新（J Hepatol）皆付費牆——數字以摘要（Europe PMC 核對）與仿單第 14 節為據，引語不超出摘要與仿單範圍。
- HIMALAYA 發表於 NEJM Evidence（付費牆）；書目與摘要數字經 Europe PMC 核對可引。
- irAE 的「任何器官、可致命」與監測要求引仿單與 AASLD[S15][S10]；細節歸 C2。
- 與 B5 的邊界：TACE 失敗後轉全身治療的策略歸 B5；本篇只寫「日子怎麼過」（多久打一次、回診驗什麼、什麼要當天講）。

### 台灣現況

- **一線（健保 9.69，需事前審查）**：atezo+bev 自 112/8/1、durva+treme 自 114/2/1 納入；適用條件：Child-Pugh A、未曾全身治療、且符合肝外轉移／大血管侵犯／TACE 12 個月內 ≥3 次失敗三者之一；排除：曾器官移植、正用免疫抑制劑、**「有上消化道出血之疑慮且未接受完全治療(須有半年內之內視鏡評估報告)」**；sorafenib、lenvatinib、atezo+bev、durva+treme **僅得擇一給付，不得互換**；atezo+bev 或 durva+treme 治療失敗後**不得申請 regorafenib 或 ramucirumab**[S42]。
- **標靶條文**：sorafenib 9.34（101/8/1 起，條件同上三擇一，事前審查、首次 3 個月、每 3 個月附影像評估，每日至多 4 粒）[S42]；lenvatinib 9.63（109/1/1 起，同構條件；治療失敗後不得申請 regorafenib/ramucirumab）[S42]。
- **二線條文**：regorafenib 9.51（限 sorafenib 失敗後、CP-A；首次 12 週、每 8 週評估；與 ramucirumab/nivolumab 擇一）[S42]；ramucirumab 9.92（限 sorafenib 失敗後、**AFP≥400**、CP-A）[S42]；**cabozantinib 9.74 無肝癌適應症**（僅腎癌、甲狀腺癌）→ 肝癌使用為自費，金額寫「向醫務課確認」[S42]。nivolumab 肝癌條文（9.69(1)(8)）限 109/4/1 前已核准者續用——歷史條款，新病人已不適用[S42]。
- 擇一給付的白話翻譯是 C3 的台灣主段：**健保只買一張一線門票**——這正是「治療前把胃鏡做完、把條件湊齊」值得慎重的制度理由。

---

## C4 `lv-nutrition`〈白蛋白、肌肉與飲食〉

### Key facts

**肌少症的預後數據（HCC）**

- Jiang 2022 統合分析（42 篇、8,445 人）：HCC 病人肌少症盛行率 **39%**（95% CI 33–45%）；肌少症者整體存活較差，**校正後 HR 1.84**（95% CI 1.62–2.09）；無惡化存活 HR 1.33[S33]。
- Guo 2023 統合分析（57 篇、9,790 人）：盛行率 41.7%；OS HR **1.93**（95% CI 1.73–2.17）；復發風險 HR 1.75；藥物不良事件 OR 2.23；次族群顯示**早期腫瘤、有肝硬化、Child-Pugh B 者受肌少症影響更大**[S34]。
- 全部是觀察性資料——肌少症「與較差存活相關」，不可寫成「練肌肉就會活比較久」（介入試驗不在本組查證範圍）。

**蛋白質——過時慣例 vs 現行指引（本篇的誠實脊椎）**

- 舊慣例的正式葬禮，兩份指引原文：
  - AASLD/EASL 2014（建議 31，GRADE I, A, 1）：「**Daily protein intake should be 1.2-1.5 g/kg/day**」；內文：「**Chronic protein restriction is detrimental**」「There is consensus that **low-protein nutrition should be avoided** for patients with HE. Some degree of protein restriction may be inevitable in the first few days of OHE treatment, **but should not be prolonged**」[S11]。
  - ESPEN 2019（建議 54，Grade B，100% 共識）：「**Protein intake should not be restricted in cirrhotic patients with HE as it increases protein catabolism**」；內文直接說 Córdoba 試驗之後「the dogma of prescribing protein restriction for LC patients with HE was **definitively abandoned**」[S31]。建議 52/53：無營養不良的代償性肝硬化 1.2 g/kg/day、營養不良或肌少症者 **1.5 g/kg/day**[S31]。
- 翻案的原始試驗（Córdoba 2004，n=30 隨機）：肝性腦病變住院病人隨機吃低蛋白漸增 vs 正常蛋白 14 天——**腦病變病程無差異**，低蛋白組**蛋白分解反而較高**[S32]。
- 熱量：AASLD/EASL 2014 建議 30：35–40 kcal/kg/day（GRADE I, A, 1）[S11]；ESPEN：30–35 kcal/kg/day[S31]。兩份指引數字略異，並陳出處。

**睡前點心（late evening snack）**

- 指引等級：AASLD/EASL 2014 建議 32（GRADE I, A, 1）：「Small meals or liquid nutritional supplements evenly distributed throughout the day and **a late-night snack should be offered**」[S11]；ESPEN 建議 24：口服營養補充品「should be given as a **late evening or nocturnal supplement**」[S31]。機轉句可引 ESPEN 內文：肝硬化病人一夜空腹後肝醣即耗盡、代謝狀態等同健康人長期飢餓[S31]。
- 統合分析（Chen 2019，8 篇 341 人）：LES 改善白蛋白（效應量 0.233）、血氨（−0.425）、凝血酶原時間（−0.589）；腹水與肝性腦病變發生率較對照低；**Child-Pugh 總分無顯著差異**[S35]——寫「肝功能檢驗指標改善、分數不動」的誠實版。

**鈉與腹水**

- EASL 2018 建議原文：「A moderate restriction of sodium intake (**80–120 mmol/day, corresponding to 4.6–6.9 g of salt**) is recommended in patients with moderate, uncomplicated ascites」≒不另外加鹽的飲食[S13]。
- ESPEN 的平衡句（建議 61）：開低鈉飲食時，**要把「更難吃導致吃得更少」的風險跟腹水治療的中等好處放在天平上**；極端限鈉反而犧牲熱量與蛋白攝取[S31]——「限鈉不是越嚴越好」是可引的指引立場。

**酒精**

- EASL 2018 建議原文：失代償肝硬化病人「the aetiological factor should be removed, **particularly alcohol consumption**」；內文：戒酒與肝硬化的漸進「再代償」及極佳長期預後相關[S13]。本篇寫到「零酒精」為止；再代償與長期肝照護歸 D3。

### Claim ceiling

- 可寫：「四成 HCC 病人有肌少症，肌少症者死亡風險約 1.8–1.9 倍（統合分析、觀察性）」；「腦病變限蛋白是被兩大指引正式拋棄的過時慣例，現行建議反而是 1.2–1.5 g/kg/day」；「睡前點心是 A 級建議，統合分析看得到白蛋白與血氨改善」；「限鹽限到 4.6–6.9 克鹽就好，更嚴的代價是吃不下」。
- **不可寫**：「補蛋白／練肌肉可以延長存活」（觀察性資料＋無介入試驗查證）；「白蛋白低就打白蛋白」（輸注白蛋白適應症完全未查證，不碰）；任何營養品品牌或 BCAA 產品推薦（ESPEN 對 BCAA 有條件建議，但台灣端多自費且本組未查證品項——寫「跟營養師談」）；「腦病變病人隨便吃蛋白都沒關係」（急性發作最初幾天的暫時調整仍由團隊決定[S11]）。
- 蛋白質 1.2–1.5 g/kg 可以寫（這是攝取建議不是藥物用量），但換算成食物的示範要保守、並導向營養師。

### Caveats

- 肌少症統合分析的異質性高、肌肉量測法不一——寫趨勢不寫精確倍數比較。
- Chen 2019 非 OA，數字以摘要為據；效應量（effect size）翻成白話時不要寫成「改善 X%」。
- 「兩個病」的框架（肝癌＋肝硬化）是 A2 地基；本篇不重新解釋 Child-Pugh 與白蛋白的意義，一句話指路。
- 糖尿病共存者的夜間點心含糖問題：ESPEN 有提及個別化（腎衰竭、糖尿病者需調整）[S31]——寫「有糖尿病要跟營養師調整內容」，不展開。

### 台灣現況

- **健保藥品給付規定第 3 節（代謝及營養劑）查證結果**：靜脈營養輸液限嚴重燒傷、全靜脈營養等特定情境；維生素依附表適應症；多處條文明載「不得做為一般營養補充劑」[S43]。**市售口服營養品（安素類、蛋白粉）屬食品、不在藥品給付規定內；癌症營養諮詢的健保給付條文未查得** → 寫「口服營養品多為自費；醫院的營養師諮詢管道與費用，請個管師協助安排」，不要寫「健保有給付營養品」也不要寫「不貴」。（FAIL-8）
- 台灣本土的 HCC 肌少症資料未取得可引來源（FAIL-9）——不寫「台灣研究顯示」。

---

## C5 `lv-tace-days`〈TACE 前後那幾天〉

### Key facts

**栓塞後症候群（發生率、正常的樣子）**

- 定義句可引 Leung 2001：「Postembolization syndrome (PES) occurs in the majority of patients undergoing hepatic chemoembolization, and is **the major reason for hospitalization after the procedure**」[S21]。膽囊被栓到與藥量較大者風險較高；**同一區域再次栓塞者 PES 風險反而較低**（OR 0.5）——「第二次通常比第一次好過」有出處[S21]。
- 帶分母的發生率：
  - 安慰劑組（Ogasawara 2018 隨機試驗，n=120，CP A/B）：只有 **10.2%** 在 TACE 後 **120 小時**內完全沒有發燒、食慾不振、噁心嘔吐三者之一（複合「完全反應」定義）——即約九成至少中一項[S19]。類固醇預防可把「完全沒症狀」提高到 47.5%（該試驗排除糖尿病控制不良者；用不用是團隊的事，不寫成病人可要求的用藥）[S19]。
  - 泰國雙盲試驗（Koonsiripaiboon 2025，n=56，92.9% CP-A，中期 HCC）：**48 小時內 PES 48.2%**[S36]。
- 症狀組成：發燒、腹痛、噁心嘔吐、食慾不振——預防性統合分析以此四項為結局[S19][S36]。

**肝功能的下沉與回升**

- Koonsiripaiboon：**51.8% 在 TACE 後 48 小時內 ALBI 分數變差**；但整個世代只有 **3.6% 出現肝功能失代償**[S36]——「檢驗數字幾乎都會先沉一下、真正沉下去的是少數」的可引版本。追蹤更長的回升軌跡數據未查得（見 FAIL-4 的鄰接說明）——寫「多數在數週內回到基線」須避免，改寫「回診驗血就是在確認它回來了」。

**住院長度**

- 台灣的典型住院天數**查無可引來源**（FAIL-3）。可引的間接材料：美國單中心 8 年系列（521 次 cTACE）採「觀察 3 小時、不需靜脈止痛即當日出院」策略，30 天再入院率當日出院組 4.8% vs 留院觀察組 4.2%（無差異）；Child-Pugh B/C 是再入院的獨立預測因子（OR 2.1）[S37]——用來說明「留院幾天不是治療品質的指標，而是觀察策略」，台灣天數寫「各院不同，問你的團隊」。

**返家警訊（餵給 C2）**

- 本篇只保留：發燒越燒越高／寒顫／腹痛加劇／黃疸／退了又燒 → 當天回醫院（肝膿瘍 0.54%、死亡率 7.73%[S20]），其餘完整表格指向 C2。

**重複 TACE 的節奏與「不能再栓了」的交接**

- 節奏的可引錨（Lo 2002 隨機試驗設計）：「Chemoembolization was **repeated every 2 to 3 months** unless there was evidence of contraindications or progressive disease」；中位每人 4.5 個療程[S39]——「隔 2–3 個月評估一次、看影像決定要不要再做」是有出處的節奏描述（現代做法多為 on-demand，TLCA 亦以 on-demand 為當代框架[S38]）。
- 交接時刻的可引定義（TLCA 2025 中期肝癌共識，OA）：TACE 難治（refractory）＝多次治療後腫瘤反應不佳或持續惡化；**「兩次以上療程後仍有超過 50% 病灶存活」即屬反應不足**；聲明 5：難治者建議轉全身治療（immunotherapy 第一線，lenvatinib/sorafenib 替代；共識 100%）；共識內文直言「**TACE is frequently overused**...can lead to deterioration in liver function」、反覆 TACE 於難治者常導致肝功能惡化與不良預後[S38]。
- **策略深度歸 B5**：為什麼換、換成什麼、Y-90 的位置——本篇只寫「病人端會經歷什麼」：每次栓塞前後的驗血、影像追蹤的節奏、以及「醫師說不再栓了」不是放棄而是換武器，指向 B5 與 C3。

### Claim ceiling

- 可寫：「九成的人在 TACE 後五天內至少有發燒／食慾差／噁心其中一項——這是被栓塞的腫瘤在壞死，不是治療失敗」；「一半的人 48 小時內肝功能指數會先變差，但真正失代償的是 3.6%（Child-Pugh A 為主的族群）」；「第二次通常比第一次好過（OR 0.5）」；「膿瘍不到 1%，但一旦發生死亡率 7.73%——所以警訊要背」；「兩次栓不熟就該談下一步（TLCA 定義）」。
- **不可寫**：「栓塞後住院 X 天」（無來源）；「發燒第 X 天沒退就是感染」（無門檻來源）；「PES 會持續 3–5 天」這類天數（無直接來源——只能寫試驗觀察窗：48 小時內近半、120 小時內九成至少一項）；類固醇/NAC 預防寫成病人可以要求的常規（試驗背景可述，決定歸團隊）；TACE-refractory 之後「該選哪個治療」的比較（歸 B5）。
- 分母標籤：PES 與失代償數字多來自 Child-Pugh A 為主的試驗族群，肝功能差者風險更高——每次引用帶標籤。

### Caveats

- Ogasawara 是日本試驗、Koonsiripaiboon 是泰國試驗；台灣病人組成相近但非台灣數據，敘述用「亞洲的隨機試驗」。
- Leung 2001 是 29 人 70 次的老系列（含轉移瘤）——只用它的定義句與風險方向，不用其百分比。
- TACE 適應症與 Y-90、與 SBRT 的銜接歸 B5；C5 開頭一句話標定「這篇講的是你會怎麼度過那幾天」。
- 「發燒是腫瘤壞死」的機轉句寫成通俗解釋即可，避免絕對化（感染永遠在鑑別清單上——正是 C2 那列存在的理由）。

### 台灣現況

- TACE 健保給付：33144B「血管阻塞術-Lipiodol」28,591 點，適應症原文「(1)HCC conventional TACE…」，含一般材料費及 Lipiodol[S41]。載藥微球（DEB-TACE）之特材給付未查證（沿 B 組結論：查無官方可引頁面）→「自費與否向醫院確認」。
- 住院天數、術前禁食、鼠蹊部加壓時數等實務細節：查無官方可引來源——寫成「以你醫院的術前說明單為準」，不發明數字（FAIL-3）。

---

## 給 B／D 組的協調備註

- 急症警語總表歸 C2；B3（質子）、B5（TACE 策略）、D3（復發與再代償）引用警訊時只留相關列＋指向 C2。
- C2 表 13（SBRT 後 RILD 窗口）與 B2 的紅線 3 同源（QUANTEC[S9]）——B2 寫機轉與劑量，C2 只寫「什麼時候該回來」。
- C3 的台灣給付更正（durva+treme 已給付、cabozantinib 無肝癌條文）如與 B 組 brief 的假設衝突，以本篇 9.69/9.74 條文原文為準[S42]。
- 抗病毒不可自行停藥（爆發性肝炎）：C2 表中未列，D3/A4 主場；C2 正文以一句話指路。

---

## Sources（單一序列；PASS 才可入正文）

**C1 期刊（Europe PMC REST 核對）**

- [S1] **PASS（摘要層級引用；非 OA）** Keall PJ, Mageras GS, Balter JM, et al. The management of respiratory motion in radiation oncology report of AAPM Task Group 76. *Med Phys*. 2006;33(10):3874–3900. DOI: 10.1118/1.2349696. PMID 17089851. https://doi.org/10.1118/1.2349696 ——五類技術名稱與「>5 mm 即適用移動管理」皆出自摘要，可引；內文表格數字不可引。
- [S2] **PASS** Kothary N, Heit JJ, Louie JD, et al. Safety and efficacy of percutaneous fiducial marker implantation for image-guided radiation therapy. *J Vasc Interv Radiol*. 2009;20(2):235–239. DOI: 10.1016/j.jvir.2008.09.026. PMID 19019700. https://doi.org/10.1016/j.jvir.2008.09.026
- [S3] **PASS（OA）** Dutta D, Kataki KJ, George S, et al. Prospective evaluation of fiducial marker placement quality and toxicity in liver CyberKnife stereotactic body radiotherapy. *Radiat Oncol J*. 2020;38(4):253–261. DOI: 10.3857/roj.2020.00472. PMID 33249803. PMC7785839. https://doi.org/10.3857/roj.2020.00472
- [S4] **PASS（OA，全文毒性表經 Europe PMC fullTextXML 核對）** Yoon SM, Kim SY, Lim YS, et al. Stereotactic body radiation therapy for small (≤5 cm) hepatocellular carcinoma not amenable to curative treatment: Results of a single-arm, phase II clinical trial. *Clin Mol Hepatol*. 2020;26(4):506–515. DOI: 10.3350/cmh.2020.0038. PMID 32646200. PMC7641557. https://doi.org/10.3350/cmh.2020.0038
- [S5] **PASS** Bujold A, Massey CA, Kim JJ, et al. Sequential phase I and II trials of stereotactic body radiotherapy for locally advanced hepatocellular carcinoma. *J Clin Oncol*. 2013;31(13):1631–1639. DOI: 10.1200/JCO.2012.44.1659. PMID 23547075. https://doi.org/10.1200/JCO.2012.44.1659
- [S6] **PASS** Xi M, Yang Z, Hu L, et al. Radiofrequency Ablation Versus Stereotactic Body Radiotherapy for Recurrent Small Hepatocellular Carcinoma: A Randomized, Open-Label, Controlled Trial. *J Clin Oncol*. 2025;43(9):1073–1082. DOI: 10.1200/JCO-24-01532. PMID 39693584. https://doi.org/10.1200/JCO-24-01532 ——AE 相當（p=0.436/0.715）出自摘要，本組獨立核對。
- [S7] **PASS** Mendiratta-Lala M, Gu E, Owen D, et al. Imaging Findings Within the First 12 Months of Hepatocellular Carcinoma Treated With Stereotactic Body Radiation Therapy. *Int J Radiat Oncol Biol Phys*. 2018;102(4):1063–1069. DOI: 10.1016/j.ijrobp.2017.08.022. PMID 29029891. PMC5826807. https://doi.org/10.1016/j.ijrobp.2017.08.022
- [S8] **PASS** Mendiratta-Lala M, Masch W, Shankar PR, et al. Magnetic Resonance Imaging Evaluation of Hepatocellular Carcinoma Treated With Stereotactic Body Radiation Therapy: Long Term Imaging Follow-Up. *Int J Radiat Oncol Biol Phys*. 2019;103(1):169–179. DOI: 10.1016/j.ijrobp.2018.09.004. PMID 30213751. PMC6301102. https://doi.org/10.1016/j.ijrobp.2018.09.004
- [S9] **PASS（引語經 NCBI PMC 作者稿全文核對，PMC4388033）** Pan CC, Kavanagh BD, Dawson LA, et al. Radiation-associated liver injury. *Int J Radiat Oncol Biol Phys*. 2010;76(3 Suppl):S94–S100. DOI: 10.1016/j.ijrobp.2009.06.092. PMID 20171524. https://doi.org/10.1016/j.ijrobp.2009.06.092
- [S10] **PASS（全文引語經 NCBI PMC 全文核對，PMC10663390）** Singal AG, Llovet JM, Yarchoan M, et al. AASLD Practice Guidance on prevention, diagnosis, and treatment of hepatocellular carcinoma. *Hepatology*. 2023;78(6):1922–1965. DOI: 10.1097/HEP.0000000000000466. PMID 37199193. https://doi.org/10.1097/HEP.0000000000000466

**C2 指引與仿單**

- [S11] **PASS（全文 PDF 經 AASLD 官方網站取得並逐字核對）** Vilstrup H, Amodio P, Bajaj J, et al. Hepatic encephalopathy in chronic liver disease: 2014 Practice Guideline by the American Association for the Study of Liver Diseases and the European Association for the Study of the Liver. *Hepatology*. 2014;60(2):715–735. DOI: 10.1002/hep.27210. PMID 25042402. 官方 PDF：https://www.aasld.org/sites/default/files/2022-07/Hepatic%20Encephalopathy%20in%20Chronic%20Liver%20Disease%202014.pdf
- [S12] **PASS（OA 接受稿經機構典藏取得並逐字核對；引用連結用 DOI）** Kaplan DE, Ripoll C, Thiele M, et al. AASLD Practice Guidance on risk stratification and management of portal hypertension and varices in cirrhosis. *Hepatology*. 2024;79(5):1180–1211. DOI: 10.1097/HEP.0000000000000647. PMID 37870298. https://doi.org/10.1097/HEP.0000000000000647
- [S13] **PASS（全文 PDF 經 easl.eu 官方網站取得並逐字核對）** European Association for the Study of the Liver. EASL Clinical Practice Guidelines for the management of patients with decompensated cirrhosis. *J Hepatol*. 2018;69(2):406–460. DOI: 10.1016/j.jhep.2018.03.024. PMID 29653741. 官方 PDF：https://easl.eu/wp-content/uploads/2018/10/decompensated-cirrhosis-English-report.pdf
- [S14] **PASS（本次第三度獨立查證：Europe PMC 書目＋OUP 原文定義句）** Freifeld AG, Bow EJ, Sepkowitz KA, et al. Clinical practice guideline for the use of antimicrobial agents in neutropenic patients with cancer: 2010 update by the Infectious Diseases Society of America. *Clin Infect Dis*. 2011;52(4):e56–e93. DOI: 10.1093/cid/cir073. PMID 21258094. https://academic.oup.com/cid/article/52/4/e56/382256
- [S15] **PASS** TECENTRIQ (atezolizumab) injection — FDA prescribing information，BLA761034，Genentech, Inc.，label effective 2026-05-20。URL: https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=6fa682c9-a312-4932-9831-f286908660ee ——建立：IMbrave150 安全性（致死 AE 4.6%；死因最常見為腸胃道及食道靜脈瘤出血 1.2%、感染 1.2%；嚴重 AE 38%，含腸胃道出血 7%）；試驗要求 6 個月內評估靜脈瘤與排除條件原文；免疫性肺炎 3%、大腸炎 1%、肝炎 1.8%、腎上腺不全 0.4%、腦下垂體炎；肝功能/肌酸酐/甲狀腺監測要求；HCC AE 表（高血壓 30%/G3–4 15%）。Route: openFDA drug/label.json（openfda.brand_name:"TECENTRIQ"），DailyMed HTTP 200
- [S16] **PASS** Avastin (bevacizumab) injection — FDA prescribing information，BLA125085，Genentech, Inc.，label effective 2025-01-06。URL: https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=939b5d1f-9fb2-4499-80ef-0607aa6b114e ——建立：腸胃道穿孔 0.3–3%、多在第一劑後 50 天內；擇期手術前後各至少停 28 天；嚴重出血高至 5 倍、近期咳血禁用；高血壓危象/PRES。Route: openFDA drug/label.json，DailyMed HTTP 200
- [S17] **PASS** Lenvima (lenvatinib) capsules — FDA prescribing information，NDA206947，Eisai Inc.，label effective 2026-06-30。URL: https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=f4bedd21-efde-44c6-9d9c-b48b78d7ed1e ——建立：REFLECT 高血壓 45%（G3 24%、中位發生 26 天）；G3–5 出血 5% 含 7 例致死；肝性腦病變 8%（G3–5 5%）；瘻管/腸胃道穿孔 2%；HCC AE 表（PPE 27% vs sorafenib 52%；出血事件 23%/G3–4 4%）。Route: openFDA drug/label.json，DailyMed HTTP 200
- [S18] **PASS** Nexavar (sorafenib) tablets — FDA prescribing information，NDA021923，Bayer HealthCare Pharmaceuticals Inc.，label effective 2023-08-28。URL: https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=b50667e4-5ebc-4968-a646-d605058dbef0 ——建立：HFSR/皮疹多在前六週；SHARP HFSR 21%（G3 8%）vs 安慰劑 3%；高血壓 9.4% vs 4.3%、前 6 週每週量血壓；食道靜脈瘤出血 2.4% vs 4%；腸胃道穿孔 <1%。Route: openFDA drug/label.json，DailyMed HTTP 200
- [S19] **PASS** Ogasawara S, Chiba T, Ooka Y, et al. A randomized placebo-controlled trial of prophylactic dexamethasone for transcatheter arterial chemoembolization. *Hepatology*. 2018;67(2):575–585. DOI: 10.1002/hep.29403. PMID 28746788. https://doi.org/10.1002/hep.29403 ——安慰劑組 120 小時內完全無發燒/食慾不振/噁心嘔吐者僅 10.2%（95% CI 3.8–20.8）。
- [S20] **PASS（OA）** Wang Y, Wang H, Liu Z, Chang Z. Evolution of transarterial chemoembolization-related liver abscess over time: a systematic review and meta-analysis. *Quant Imaging Med Surg*. 2025;15(4):2707–2721. DOI: 10.21037/qims-24-1166. PMID 40235776. PMC11994569. https://doi.org/10.21037/qims-24-1166 ——合併發生率 0.54%（32 篇、254,408 人次）；直接相關死亡率 7.73%。
- [S21] **PASS（僅引定義句與風險方向；29 人老系列，百分比不引）** Leung DA, Goin JE, Sickles C, et al. Determinants of postembolization syndrome after hepatic chemoembolization. *J Vasc Interv Radiol*. 2001;12(3):321–326. DOI: 10.1016/S1051-0443(07)61911-3. PMID 11287509. https://doi.org/10.1016/S1051-0443(07)61911-3

**C3 期刊（Europe PMC REST 核對；數字以摘要為據）**

- [S22] **PASS** Finn RS, Qin S, Ikeda M, et al. Atezolizumab plus Bevacizumab in Unresectable Hepatocellular Carcinoma. *N Engl J Med*. 2020;382(20):1894–1905. DOI: 10.1056/NEJMoa1915745. PMID 32402160.（NCT03434379）https://doi.org/10.1056/NEJMoa1915745
- [S23] **PASS** Cheng AL, Qin S, Ikeda M, et al. Updated efficacy and safety data from IMbrave150: Atezolizumab plus bevacizumab vs. sorafenib for unresectable hepatocellular carcinoma. *J Hepatol*. 2022;76(4):862–873. DOI: 10.1016/j.jhep.2021.11.030. PMID 34902530. https://doi.org/10.1016/j.jhep.2021.11.030
- [S24] **PASS** Abou-Alfa GK, Lau G, Kudo M, et al. Tremelimumab plus Durvalumab in Unresectable Hepatocellular Carcinoma. *NEJM Evid*. 2022;1(8):EVIDoa2100070. DOI: 10.1056/EVIDoa2100070. PMID 38319892.（NCT03298451）https://doi.org/10.1056/EVIDoa2100070
- [S25] **PASS** Rimassa L, Chan SL, Sangro B, et al. Five-year overall survival update from the HIMALAYA study of tremelimumab plus durvalumab in unresectable HCC. *J Hepatol*. 2025;83(4):899–908. DOI: 10.1016/j.jhep.2025.03.033. PMID 40222621. https://doi.org/10.1016/j.jhep.2025.03.033
- [S26] **PASS** Lau G, Abou-Alfa GK, Cheng AL, et al. Outcomes in the Asian subgroup of the phase III randomised HIMALAYA study of tremelimumab plus durvalumab in unresectable hepatocellular carcinoma. *J Hepatol*. 2025;82(2):258–267. DOI: 10.1016/j.jhep.2024.07.017. PMID 39089633. https://doi.org/10.1016/j.jhep.2024.07.017
- [S27] **PASS** Kudo M, Finn RS, Qin S, et al. Lenvatinib versus sorafenib in first-line treatment of patients with unresectable hepatocellular carcinoma: a randomised phase 3 non-inferiority trial. *Lancet*. 2018;391(10126):1163–1173. DOI: 10.1016/S0140-6736(18)30207-1. PMID 29433850. https://doi.org/10.1016/S0140-6736(18)30207-1
- [S28] **PASS** Bruix J, Qin S, Merle P, et al. Regorafenib for patients with hepatocellular carcinoma who progressed on sorafenib treatment (RESORCE): a randomised, double-blind, placebo-controlled, phase 3 trial. *Lancet*. 2017;389(10064):56–66. DOI: 10.1016/S0140-6736(16)32453-9. PMID 27932229. https://doi.org/10.1016/S0140-6736(16)32453-9
- [S29] **PASS** Abou-Alfa GK, Meyer T, Cheng AL, et al. Cabozantinib in Patients with Advanced and Progressing Hepatocellular Carcinoma. *N Engl J Med*. 2018;379(1):54–63. DOI: 10.1056/NEJMoa1717002. PMID 29972759. https://doi.org/10.1056/NEJMoa1717002
- [S30] **PASS** Zhu AX, Kang YK, Yen CJ, et al. Ramucirumab after sorafenib in patients with advanced hepatocellular carcinoma and increased α-fetoprotein concentrations (REACH-2): a randomised, double-blind, placebo-controlled, phase 3 trial. *Lancet Oncol*. 2019;20(2):282–296. DOI: 10.1016/S1470-2045(18)30937-9. PMID 30665869. https://doi.org/10.1016/S1470-2045(18)30937-9

**C4 期刊與指引**

- [S31] **PASS（全文引語經 NCBI PMC 全文核對，PMC6686849）** Plauth M, Bernal W, Dasarathy S, et al. ESPEN guideline on clinical nutrition in liver disease. *Clin Nutr*. 2019;38(2):485–521. DOI: 10.1016/j.clnu.2018.12.022. PMID 30712783. https://doi.org/10.1016/j.clnu.2018.12.022
- [S32] **PASS** Córdoba J, López-Hellín J, Planas M, et al. Normal protein diet for episodic hepatic encephalopathy: results of a randomized study. *J Hepatol*. 2004;41(1):38–43. DOI: 10.1016/j.jhep.2004.03.023. PMID 15246205. https://doi.org/10.1016/j.jhep.2004.03.023
- [S33] **PASS（OA）** Jiang C, Wang Y, Fu W, et al. Association between sarcopenia and prognosis of hepatocellular carcinoma: A systematic review and meta-analysis. *Front Nutr*. 2022;9:978110. DOI: 10.3389/fnut.2022.978110. PMID 36590214. PMC9794869. https://doi.org/10.3389/fnut.2022.978110
- [S34] **PASS（OA）** Guo Y, Ren Y, Zhu L, et al. Association between sarcopenia and clinical outcomes in patients with hepatocellular carcinoma: an updated meta-analysis. *Sci Rep*. 2023;13(1):934. DOI: 10.1038/s41598-022-27238-z. PMID 36650190. PMC9845331. https://doi.org/10.1038/s41598-022-27238-z
- [S35] **PASS** Chen CJ, Wang LC, Kuo HT, et al. Significant effects of late evening snack on liver functions in patients with liver cirrhosis: A meta-analysis of randomized controlled trials. *J Gastroenterol Hepatol*. 2019;34(7):1143–1152. DOI: 10.1111/jgh.14665. PMID 30883904. https://doi.org/10.1111/jgh.14665

**C5 期刊**

- [S36] **PASS（OA）** Koonsiripaiboon P, Ruamtawee W, Simasingha N, et al. Efficacy of N-acetylcysteine vs dexamethasone in preventing postembolization syndrome post-transarterial chemoembolization in hepatocellular carcinoma: A randomized controlled trial. *World J Gastroenterol*. 2025;31(31):109630. DOI: 10.3748/wjg.v31.i31.109630. PMID 40901687. PMC12400246. https://doi.org/10.3748/wjg.v31.i31.109630
- [S37] **PASS** Hund HC, Frantz SK, Wu H, et al. Six-Year Evaluation of Same-Day Discharge following Conventional Transarterial Chemoembolization of Hepatocellular Carcinoma. *J Vasc Interv Radiol*. 2023;34(3):378–385. DOI: 10.1016/j.jvir.2022.11.029. PMID 36481322. https://doi.org/10.1016/j.jvir.2022.11.029
- [S38] **PASS（OA，全文引語經 NCBI PMC 全文核對，PMC12538147）** Lee IC, Wang HW, Teng W, et al. Taiwan liver cancer association management consensus guidelines for intermediate-stage hepatocellular carcinoma. *Clin Mol Hepatol*. 2025;31(4):1213–1232. DOI: 10.3350/cmh.2025.0724. PMID 40755008. https://doi.org/10.3350/cmh.2025.0724
- [S39] **PASS** Lo CM, Ngan H, Tso WK, et al. Randomized controlled trial of transarterial lipiodol chemoembolization for unresectable hepatocellular carcinoma. *Hepatology*. 2002;35(5):1164–1171. DOI: 10.1053/jhep.2002.33156. PMID 11981766. https://doi.org/10.1053/jhep.2002.33156 ——「每 2–3 個月重複、除非禁忌或惡化」與中位 4.5 個療程出自摘要。

**官方頁面／文件（實際抓取，取得日 2026-08-30）**

- [S40] **PASS** 衛生福利部新聞稿（104-01-13）：「104年2月起『身體立體定位放射治療』將納入健保給付，可縮短癌症病患治療療程。」——全文含「以一個療程（約1至2週），每1至3天照射1次，總計於6次以內」「透過呼吸調控及影像導航」「肝功能為Child-Pugh A至B級…≦5公分且無法接受手術切除、血管栓塞治療及電燒灼治療」。https://www.mohw.gov.tw/cp-2636-21129-1.html （HTTP 200）
- [S41] **PASS** 全民健康保險醫療服務給付項目及支付標準（開放資料 ODS 全表，6,013 項；本組獨立下載逐列檢索）：**37047B** 身體立體定位放射治療 213,662 點（適應症與「全療程為二週且分次治療以六次(含)為限，採包裹給付」原文如上引錄；需事前審查）；**33144B** 血管阻塞術-Lipiodol 28,591 點（適應症 (1) HCC conventional TACE，含一般材料費及 Lipiodol）。資料集頁：https://data.gov.tw/dataset/9405 ；檔案：https://info.nhi.gov.tw/api/iode0000s01/Dataset?rId=A21030000I-D20003-004
- [S42] **PASS** 衛生福利部中央健康保險署《全民健康保險藥品給付規定》第 9 節抗癌瘤藥物（現行版全文 102 頁，條文日期至 115/8/1；curl 下載 → pdftotext → 逐條檢索）。URL: https://www.nhi.gov.tw/ch/dl-55685-99c675b771ab4b2789c891bc8db447ce-1.pdf ——建立：9.69 晚期肝細胞癌第一線（atezo+bev 112/8/1、durva+treme 114/2/1；條件、內視鏡評估報告要求、擇一給付、失敗後不得申請 regorafenib/ramucirumab）；9.34 sorafenib；9.63 lenvatinib；9.51 regorafenib（HCC 108/6/1）；9.92 ramucirumab（AFP≥400，110/5/1）；9.74 cabozantinib（**無肝癌適應症**）；9.69(1)(8) nivolumab 歷史條款。
- [S43] **PASS** 衛生福利部中央健康保險署《全民健康保險藥品給付規定》第 3 節代謝及營養劑（現行版；curl 下載 → pdftotext → 檢索）。URL: https://www.nhi.gov.tw/ch/dl-50601-a3baf9dd4cd44fbb93b4d62a01cdf1df-1.pdf ——建立：靜脈營養輸液限特定情境；「不得做為一般營養補充劑」措辭；**口服營養品與癌症營養諮詢均無給付條文可引**。

**FAIL ／ NOT-CITABLE（保留紀錄，不得入正文引用）**

- [FAIL-1] **定位（模擬攝影）到第一次治療的典型間隔天數**：Europe PMC 與官方頁面均查無可引來源。C1 時程寫到「療程本身約二週、六次以內」為止[S40][S41]，準備期寫「依醫院排程，通常以週計」不帶數字。
- [FAIL-2] **單次 SBRT 治療在治療床上的分鐘數**：查無可引來源（Dutta [S3] 的時間是 fiducial 置放程序，不可挪用）。寫質性描述（擺位比照射久、全程不痛）不帶分鐘數。
- [FAIL-3] **台灣 TACE 典型住院天數**：查無官方或可引學術來源。美國當日出院系列[S37]只能用來說明「觀察策略各院不同」。
- [FAIL-4] **栓塞後症候群的持續天數**：無直接來源；僅能寫試驗觀察窗（48 小時內 48.2%[S36]；120 小時內約九成至少一項[S19]）。「3–5 天會退」這類句子不可寫。
- [FAIL-5] **PES 發燒 vs 感染的時間/溫度門檻**：查無任何指引或試驗給出「第幾天、幾度」的分界。C2 表 12 與 C5 只寫質性區分（趨勢向上、寒顫、退了又燒、腹痛加劇）。
- [FAIL-6] **Garcia-Tsao 2017 與 Biggins 2021（AASLD 門脈高壓/腹水指引）全文**：付費牆、無 OA 副本可下載（openaccessrepository.it 記錄失效 400/302）。以 Kaplan 2024（OA 接受稿）[S12]與 EASL 2018（easl.eu 官方 PDF）[S13]替代，兩者涵蓋所需引語。
- [FAIL-7] **EASL 2022 肝性腦病變指引全文**：付費牆。分級與早期徵象改引 AASLD/EASL 2014（aasld.org 官方 PDF）[S11]——引用時標明為 2014 年文件。
- [FAIL-8] **台灣口服營養品／癌症營養諮詢的健保給付條文**：第 3 節全文檢索無對應品項（多屬食品不在藥品給付規定範圍）[S43]；亦未查得其他官方文件。→ C4 寫「自費為主、請個管師協助安排營養師」，不得憑空宣稱有給付或沒給付。
- [FAIL-9] **台灣本土 HCC 肌少症預後資料**：未取得可引來源；C4 用國際統合分析[S33][S34]，不寫「台灣研究顯示」。
- [FAIL-10] **肝膿瘍發生的典型時間點（TACE 後第幾天到第幾週）**：統合分析[S20]未提供；不寫時間窗。
- [FAIL-11] **「durva+treme 在台灣是給付缺口」這句話**：查證後不成立（見開頭警示 1）。9.69 條文自 114/2/1 已納入[S42]。

---

## 給撰稿人的一句話總結

C 組查證後最大的驚喜有兩個：一是**紅線 5 在台灣有官方本體**——健保 9.69 條文自己就要求「半年內之內視鏡評估報告」，胃鏡要求可以寫成試驗設計、AASLD 強建議、健保條文三位一體，而且 durva+treme 已同條給付（SPEC 的 gap 假設過期）；二是 **C1 標題的「兩週」就是 37047B 的法定療程定義**，官方文字比任何文獻都適合當骨架。最誠實的兩段內容都有紮實出處：SBRT 後持續顯影不是復發（Mendiratta-Lala 兩篇：治療成功者 58% 仍顯影、早期 mRECIST 只判得出 25% 完全反應）、腦病變限蛋白是被兩大指引「definitively abandoned」的過時慣例（Rec 54 原文＋Córdoba 翻案試驗）。C2 的十三列警語全部有來源，其中 SBP「可以無症狀＋延遲穿刺死亡率 2.7 倍」與 atezo+bev「死因第一位是靜脈瘤出血 1.2%」是最值得放大的兩列。缺口誠實列了十一條：時程與住院天數類的數字（定位到治療的間隔、單次治療分鐘數、台灣 TACE 住院天數、PES 持續天數、發燒分界門檻）全部查無來源——這五個 FAIL 是 C 組文章最容易憑印象補數字的地方，動筆時寧可寫「問你的團隊」。
