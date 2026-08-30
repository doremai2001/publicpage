# 乳癌專題 — 修訂清單

兩輪查核（各自獨立、互不知情）已完成，條目本體在：

- `/home/claude/breast/review-safety.md` — 7 條甲級、11 條乙級
- `/home/claude/breast/review-style.md` — 乙級與丙級，共 8 大類

本檔是**執行說明與衝突裁決**。每一條都附了原句與替換句，照替換句貼上。

---

## 零、改完必須維持的不變式

1. 只用 `colon/SPEC.md` 第一節允許的標籤。
2. 內文 `[n]` 依**首次出現順序**連號，不跳號、不重複。
3. 參考資料條目數與內文 href **逐條對應**，沒有未被引用的條目。
4. 全篇一個 `<hr>`、一個 `<h3>`，檔尾 `<p></p>`。
5. 正文 1,600–2,400 個中文字，5–8 個 `<h4>`。
6. **刪掉某個引用的最後一次出現時，要把該條參考資料一併刪除，並把後面全部重新編號
   （內文與清單都要）。**

## 零之二、參考資料的書目資料，只准改一處

241 筆引用已對過 Europe PMC。**39 筆「NOT FOUND」是腳本的 DOI 正規表示式在括號截斷造成的誤報**，
檔案裡的 DOI 是對的。**3 筆「title mismatch」是 Europe PMC 回傳標題含 `<i>` 斜體標記**
（`<i>PALB2</i>`、`<i>PIK3CA</i>`、`<i>BRCA</i>`），文章寫法沒有錯。
**1 筆頁碼差異**（`imaging-extent` 的 `180–187` 對線上 `180-7; quiz 294-5`）是 Europe PMC
把測驗頁併進同欄位，文章沒有錯。

**唯一要改的一筆**：`germline-brca` 的 ASCO/ASTRO/SSO 指引標題被縮寫成
`Management of Hereditary Breast Cancer: ASCO, ASTRO, and SSO Guideline`，
正式標題是
`Management of Hereditary Breast Cancer: American Society of Clinical Oncology, American Society for Radiation Oncology, and Society of Surgical Oncology Guideline`。
**改成全名。其餘任何一條的作者、年份、期刊、卷、期、頁、DOI、URL 都不准動。**

---

## 一、甲級（必須改：安全與法律）

### 甲-1　`chemo-side-effects.html` 漏掉 abemaciclib 的靜脈血栓警訊 —— 全系列最嚴重

brief 的急症警語總表列了 abemaciclib 的「單側腿腫痛、突發胸痛或喘（靜脈血栓栓塞）」，
文章寫了腹瀉、發燒、間質性肺病與黃疸，**唯獨沒有血栓**——而且兩段之後才把同一條
寫給 PARP 抑制劑。abemaciclib 是台灣**唯一**給付於早期乳癌的 CDK4/6 抑制劑，要吃兩年，
而〈抗荷爾蒙藥要吃五年還是十年〉會把讀者送到這一篇。依 `review-safety.md` 甲-1 補上。

### 甲-2　`chemo-side-effects.html` 缺 T-DM1 的間質性肺病症狀

同一段還放了「放射性肺炎 1.8%」，會把咳嗽與喘導向錯誤的原因。依替換段落改。

### 甲-3　**二十一處交叉引用指向不存在的標題**

四位寫作者沿用了 SPEC 第五節的**分節標籤**，而不是 `meta/all.json` 裡真正的標題。
六個目標受影響，**兩篇副作用文章的正確標題在二十四篇裡從來沒有被正確引用過**。
其中兩處同時是安全問題：`breast-conserving` 與 `rt-hypofx` 把 C2 寫成
〈有些人可以不做放療，但不是每個人〉——**那正是紅線 3 禁止的讀法，也正是 C2 自己改標題的原因。**

**下面這張表是全系列唯一正確的標題來源。所有 `〈…〉` 一律照抄，一個字都不要改。**

- `first-month` → 〈確診之後的第一個月會怎麼走〉
- `receptor-report` → 〈ER、PR、HER2 在報告上說了什麼〉
- `three-subtypes` → 〈三種乳癌，三條不一樣的路〉
- `which-lines-matter` → 〈報告哪幾行真的會改變治療〉
- `imaging-extent` → 〈影像上的大小，跟真正的不一樣〉
- `germline-brca` → 〈家族史：現在就該驗 BRCA 嗎〉
- `breast-conserving` → 〈保留乳房還是切除，存活一樣嗎〉
- `sentinel-node` → 〈腋下要不要清乾淨〉
- `neoadjuvant` → 〈先開刀，還是先做化療〉
- **`genomic-chemo` → 〈這份檢測是要證明什麼〉**（見甲-4，標題同時要改）
- `her2-therapy` → 〈HER2 陽性：藥怎麼排〉
- `endocrine-years` → 〈抗荷爾蒙藥要吃五年還是十年〉
- `rt-hypofx` → 〈五次、十五次還是二十五次〉
- **`rt-omission` → 〈省略放療，條件缺一不成立〉**
- `rt-regional` → 〈腋下與鎖骨上要不要一起照〉
- **`chemo-side-effects` → 〈哪些副作用要當天打電話〉**
- **`endocrine-side-effects` → 〈真正讓人停藥的那幾個副作用〉**
- `fertility-young` → 〈年輕病人：生育保存與卵巢功能〉
- `followup-schedule` → 〈追蹤要不要每年做全身檢查〉
- `lymphoedema` → 〈手腫起來：淋巴水腫的真實機率〉
- `bone-health` → 〈骨質、骨轉移用藥與運動〉
- `self-pay-and-trials` → 〈這個檢測要自費，值不值得〉
- `metastatic-genomics` → 〈轉移之後，基因檢測是為了找藥〉
- `metastatic-outlook` → 〈轉移了，接下來會怎麼走〉

### 甲-4　`genomic-chemo` 的標題把「目的」寫成了「結果」

`meta` 裡的 〈這份檢測要證明你可以不做化療〉 掉了一個「是」，在**唯一會被單獨讀到的欄位**
變成對結果的斷言。**標題改成 〈這份檢測是要證明什麼〉**，把「省化療」這件事交給 `dek` 去說，
`dek` 必須同時寫出「只適用於荷爾蒙受體陽性、HER2 陰性」。全系列的交叉引用一併改（見甲-3）。

### 甲-5　`genomic-chemo` 把第二條線與第三條線混在一起

文章把健保給付的 NGS 說成標靶用藥檢測，但 `self-pay-and-trials`、`germline-brca`、
`which-lines-matter` 依公報與支付標準都寫「乳癌唯一給付的是三陰性的**生殖系** BRCA1/2 血液檢測」。
這正是 SPEC 第三節禁止的混線。依 `review-safety.md` 的替換句改，
並把參考 [14] 換成 dl-69964 支付標準 PDF（它是清單最後一條，不需重新編號）。

### 甲-6　`endocrine-years` 的 `note` 少了配重

「如果答案讓你想停，那也要在門診裡停，不要在家裡停。」在**正文裡通過**——
它前一段就寫了「不可以自己停、自己減量、自己『放假幾個月再說』」。
但 `meta` 的 `note` 是被單獨讀的，那裡沒有配重。依替換文字改 `note`。

### 甲-7　其餘甲級

`review-safety.md` 剩下的甲級條目逐條執行。

---

## 二、乙級（數字與歸屬）

`review-safety.md` 的 11 條與 `review-style.md` 的乙級全部執行。優先這六類：

1. **統計術語被寫錯**，這是真正會誤導的：
   - `three-subtypes`「可能性高 6.4 到 20.0 倍」把**勝算比寫成機率倍數**。
   - `metastatic-outlook`「風險降低 68%」把**風險比寫成機率下降**——而 `first-month`
     自己就在警告不要這樣寫。
   - `imaging-extent`（**標題數字，lead 與正文都有**）與 `lymphoedema` 把**百分點寫成百分比**。
   - `sentinel-node` 印出一個**不包含自己點估計的信賴區間**（5.6%［6.1–7.9］）。
   - APHINITY 支持性次族群的風險比沒有信賴區間，虛無的那個卻有——兩個都要給。
2. **「非劣性」在 `genomic-chemo`（紅線 1 那一篇）與 `her2-therapy` 用了但從未解釋。**
   每一篇都要在該篇第一次出現時自己解釋一次——從搜尋引擎落到第 19 篇的讀者沒讀過第 4 篇。
3. **四篇文章用了風險比／勝算比 4–12 次卻完全沒有白話化**，逐篇補。
4. **固定紅線 D**：沒有標亞型與族群的數字要補上。
5. **越界改寫**：`which-lines-matter` 寫了兩段 `germline-brca` 的材料、
   `her2-therapy` 把 `neoadjuvant` 的 KATHERINE 重寫一遍、
   `sentinel-node` 寫了一整節 `lymphoedema` 的資料。依 SPEC 第六節壓成一句並指路。
6. **重複**：EBCTCG 二十年表出現在四篇、8,769 人的服藥順從性研究出現在三篇。
   裁決：SOFT/TEXT 歸 `endocrine-years`，健保 GnRH 5.5.1 歸 `genomic-chemo`，
   兩篇目前都各自寫了兩者，各刪一半。

## 三、丙級（模板味與聲音）

`review-style.md` 的丙級全部執行。這一輪的目標是磨掉四個寫作者的接縫。

- **B 組六篇的第一人稱密度全部低於站上既有文章**（我／千字 1.0–2.4，既有文章 3.4–4.9）。
  `her2-therapy` 只出現一次「你」、零處保留語氣、八個小節有五個以試驗名稱當骨架、
  開場整段是編輯式的路由說明；`sentinel-node` 是二十四篇裡唯一長句比例 0.0% 的一篇。
  依替換文字把這兩篇拉回門診口吻。**不要動它們的內容判斷或紅線處理。**
- **二十四篇有十五篇以「」病人引言開場，十處頻率宣稱**（上限是兩處），
  其中兩處是從 `cc-stage-ii-chemo` 逐字搬來的「幾乎每週被問到」。減到兩處以內。
- **C 組六個收尾標題全部以「今天」開頭，D 組六個全部含「十二個月」。** 各改到彼此不同。
- **指向 `chemo-side-effects` 的七個句子裡有五個是同一句。** 各自帶回自己文章的語境。
- `self-pay-and-trials` 三個 `<li>` 全部用 `<strong>標籤：</strong>` 開頭；
  `metastatic-genomics` 有五段連續的粗體卡片、中間沒有連接的散文。各自打散。
- **十一篇卡在 2,399–2,400 字**，通常代表有東西被壓掉了。
  `metastatic-outlook` 的 `dek` 承諾了治療目標，正文卻沒說目標變成什麼——把那一節補回來；
  它另有三個交叉引用被堆在一個無關的腦轉移段落末尾，要移到各自該去的位置。

---

## 四、執行分工

- **修訂者一**：A 組六篇（`first-month`、`receptor-report`、`three-subtypes`、
  `which-lines-matter`、`imaging-extent`、`germline-brca`）與 B 組六篇
  （`breast-conserving`、`sentinel-node`、`neoadjuvant`、`genomic-chemo`、
  `her2-therapy`、`endocrine-years`），以及 `meta/all.json` 裡對應的十二筆。
- **修訂者二**：C 組六篇（`rt-hypofx`、`rt-omission`、`rt-regional`、
  `chemo-side-effects`、`endocrine-side-effects`、`fertility-young`）與 D 組六篇
  （`followup-schedule`、`lymphoedema`、`bone-health`、`self-pay-and-trials`、
  `metastatic-genomics`、`metastatic-outlook`），以及 `meta/all.json` 裡對應的十二筆。

**甲-3 的標題表兩人共用**，各自負責把自己那十二篇裡寫錯的 `〈…〉` 改成表上的形式。

改完各自跑：

```
python3 /root/.claude/skills/synced/f6500135-c8da-4dc6-93c6-a84bc8f3486b_80aca3b9-b5ee-44df-bbd8-498751f69935/cancer-topic-series/scripts/check_article_html.py <你負責的檔案>
```
