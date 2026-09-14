# Brief D — 膀胱癌專題 轉移與全身治療（D1、D2）

研究員：Group D｜**查證日期：2026-09-13**（本組所有藥證、給付與試驗狀態均以此日為準）
方法：期刊文獻全部經 Europe PMC REST 逐筆核對（title／journal／year／vol(issue)／pages／DOI／PMID／isOpenAccess），
OA 全文走 `/webservices/rest/<PMCID>/fullTextXML`；FDA 仿單走 openFDA `drug/label.json`（每筆記下 `effective_time`）；
試驗狀態走 `clinicaltrials.gov/api/v2/studies/<NCT>`；指引走 uroweb.org 官方章節頁（實際抓取原文）；
台灣藥證走衛福部食藥署開放資料「未註銷藥品許可證資料集」原始 CSV；健保給付走《藥品給付規定》官方 PDF 全文。
引用規則：**只有標 PASS 的來源可以進正文引用。** FAIL 條目保留。

> **這一組的保存期限最短。** 本 brief 的每一個藥證狀態、每一條給付條文都標了 2026-09-13。
> 作者裁決「兩篇寫足，含藥名與試驗數字」，代價就是這兩篇必須在正文顯眼處寫明查證日期，
> 並寫「這一格變動快，看到這篇時請跟主治醫師確認現況」。

---

## ⚠ 與 SPEC 假設不同形狀的事（動筆前必讀）

### 1.（最重要）台灣健保**沒有**給付 EV＋pembrolizumab 第一線；EV 的健保條文是**第三線、單用、一生六個療程**

《藥品給付規定》9.109 Enfortumab vedotin（如 Padcev），生效 113/5/1，逐字[D-S29]：

> 「1.適用於先前接受過含鉑化學治療，後續接受免疫檢查點抑制劑(如 atezolizumab；nivolumab；pembrolizumab；
> avelumab；ipilimumab 製劑)治療失敗後疾病惡化的局部晚期或轉移性泌尿道上皮癌成人病人，須檢附接受過含鉑
> 化學治療之病歷報告。」……「5.每位病人限給付6個療程。」

也就是說：**健保付的 EV，是打完鉑類、又打完免疫治療、再失敗之後的那一格，而且只付六個療程、只付單用。**
同一份規定第 9.69 節的通則還特別把 EV 列為例外：「enfortumab vedotin 用於局部晚期或轉移性泌尿道上皮癌
**第三線用藥**……除外」[D-S29]。**全文檔搜尋 EV＋pembrolizumab 第一線合併用法：零筆。**

對照之下，**食藥署的藥證已經涵蓋這個合併用法**：備思復（衛部菌疫輸字第001212／001213號）2026-05-08 異動後的
適應症第 2 條逐字寫「併用 pembrolizumab 適用於治療局部晚期或轉移性泌尿道上皮癌（mUC）的成人病人」[D-S30]。
**藥證有、健保沒有 —— 這就是 D1 台灣段落的全部重量所在**，而且 SPEC §五把 D1 定位成「轉移之後的第一線變了」，
在台灣的健保現實裡，**變的是藥證與指引，不是給付**。D1 必須把這件事寫清楚，否則會讓病人以為健保付得起。

### 2. EV-302 已有 2.5 年更新，數字**不是** 2024 年 NEJM 的那一組

- 註冊分析（2024 NEJM，追蹤中位 17.2 個月）：OS 31.5 vs 16.1 個月，HR 0.47（95% CI 0.38–0.58）[D-S1]
- **2.5 年更新（2025 Ann Oncol，多追一年）：OS 33.8（95% CI 26.1–39.3）vs 15.9（13.6–18.3）個月，HR 0.51（0.43–0.61）；
  PFS 12.5 vs 6.3 個月，HR 0.48（0.41–0.57）**[D-S2]

**兩組數字都對，但不可混用**，也不可只寫其中一組而不標追蹤時間。寫作者要在同一段裡交代：
追蹤變長之後 OS 中位數往上、HR 往上（0.47→0.51），這是長期追蹤的正常行為，不是效果變差。

### 3. PD-L1「不再是第一線選人依據」這句話，**在台灣是錯的**

SPEC §五給 D2 的題目是「PD-L1 為什麼不再是第一線選人依據……把它寫成一個停止重要的生物標記」。
國際上這句話成立（美國 FDA 的 pembrolizumab 尿路上皮癌適應症現已完全沒有 PD-L1 門檻[D-S6]），
**但台灣健保到今天仍然用 PD-L1 當付錢的門**。《藥品給付規定》9.69 第 3(3) 條的生物標記表現量表格，
尿路上皮癌四列逐字[D-S29]：

| 給付範圍 | 事審代碼 | pembrolizumab（Dako 22C3 或 Ventana SP263） | nivolumab（Dako 28-8 或 Ventana SP263） | atezolizumab（Ventana SP142） | avelumab（Ventana SP263） |
|---|---|---|---|---|---|
| 泌尿道上皮癌**第一線用藥（單用）** | P042 | **CPS≧10** | 本藥品尚未給付於此適應症 | IC≧5%（113 年 8 月 1 日前審核同意符合續用申請條件者） | 本藥品尚未給付於此適應症 |
| 泌尿道上皮癌**第一線用藥（併用化療）** | P044 | 本藥品尚未給付於此適應症 | **TC≥1%** | 本藥品尚未給付於此適應症 | 本藥品尚未給付於此適應症 |
| 泌尿道上皮癌**第二線用藥** | P041 | **CPS≧10** | **TC≧5%** | IC≧5%（113 年 8 月 1 日前審核同意符合續用申請條件者） | 本藥品尚未給付於此適應症 |
| 泌尿道上皮癌**維持療法** | P043 | 本藥品尚未給付於此適應症 | 本藥品尚未給付於此適應症 | 本藥品尚未給付於此適應症 | **不需檢附報告** |

而歐洲 EMA 也仍然把 PD-L1 當 cisplatin 不適合者單用免疫治療的門檻（EAU 指引逐字：
「PD-L1 positivity for use of pembrolizumab is defined by immunohistochemistry as a CPS of ≥ 10 using the
Dako 22C33 platform and, for atezolizumab, as positivity of ≥ 5% tumour-infiltrating immune cells using
Ventana SP142.」[D-S15]）。

→ **D2 的 PD-L1 那一節要從「它停止重要了」改寫成「它在試驗裡失去了選人的角色，卻還留在美國以外的付錢規則裡」。**
這反而是更好的教材：同一個生物標記，在三個地方（美國仿單／歐洲仿單／台灣健保）有三種身分。

### 4. Erdafitinib：台灣**有藥證、沒給付**，而且適應症已從 FGFR2/3 收窄成 **FGFR3 only**

- 台灣藥證：盼樂膜衣錠 3／4／5 毫克，衛部藥輸字第027912／027913／027914號，
  發證 2020/07/10、有效 2030/07/10、**異動 2025/10/20**，適應症逐字[D-S30]：
  > 「治療患有局部晚期或轉移性泌尿道上皮癌(mUC)的成人病人，並且符合以下條件：
  > 1. 帶有敏感性 **FGFR3** 基因變異，以及 2. 先前曾於使用至少一種全身性療法治療期間或治療後出現惡化現象。
  > **使用限制：BALVERSA 不建議用於治療適合使用但先前未曾使用 PD-1 或 PD-L1 抑制劑療法的病人。**」
- 美國 FDA 仿單（effective_time 20251024）用字相同：「susceptible **FGFR3** genetic alterations」＋同一條 Limitations of Use[D-S22]。
- **健保給付：《藥品給付規定》全文檔搜尋「erdafitinib」「Balversa」「盼樂」— 零筆。**
  文中唯二的 FGFR 條文都與尿路上皮癌無關（5.5.8 vosoritide 用於軟骨發育不全症的 FGFR3 基因變異；
  9.x 的 FGFR2 融合條文屬膽道癌）[D-S29]。
  → **依 SPEC §四固定紅線：寫「查不到列項，要問醫務課／個管師申請流程」，不得推論有無給付，也不得推論自費金額。**

SPEC 沒有預期「適應症從 FGFR2/3 縮成 FGFR3」這件事。**D2 不可寫「FGFR2 或 FGFR3 突變就可以用 erdafitinib」**——
帶 FGFR2 變異的病人不在現行台灣與美國仿單的適應症裡（THOR 收案時是 FGFR3/2）。

### 5. Trastuzumab deruxtecan：台灣藥證**有**泛腫瘤 HER2 IHC 3+ 適應症，健保**只付乳癌**

- 台灣藥證：優赫得凍晶注射劑 100 毫克，衛部菌疫輸字第001179號（另有達卓優凍晶注射劑 衛部菌疫輸字第001302號），
  適應症第六項逐字[D-S30]：
  > 「六、其他無法切除或轉移性實體腫瘤(solid tumors)：單獨使用於具有無法切除或轉移性 HER2 陽性(IHC 3+)實體腫瘤，
  > 先前曾接受過全身性治療且無其他適當替代治療選項的成人病人。」
- 健保：《藥品給付規定》9.115 Trastuzumab deruxtecan（生效 114/2/1）**只有乳癌兩段**（HER2 IHC3+/FISH+ 轉移性乳癌二線、
  HER2 弱陽性乳癌），**全文無任何泌尿道上皮癌或實體腫瘤泛適應症條文**[D-S29]。
- 美國 FDA 端這個適應症是**加速核准**（accelerated approval，依 ORR 與 DOR），仿單逐字：
  「This indication is approved under accelerated approval based on objective response rate and duration of response…
  Continued approval for this indication may be contingent upon verification and description of clinical benefit in a
  confirmatory trial.」[D-S25]

### 6. 站上既有文章〈三十年沒變的流程，今年動了〉：台灣藥證的**術前術後**用法比它描述的窄

既有文章寫的是 FDA 2026-07-10 依 KEYNOTE-B15／EV-304（**適合 cisplatin** 的病人）擴大適應症。
但 **台灣藥證的術前術後適應症限定「不適合接受含 cisplatin 化學治療」的 MIBC**（EV-303 那一格），逐字[D-S30]：
> 備思復適應症第 3 條：「與 pembrolizumab 併用，治療**不適合接受含 cisplatin 化學治療的**肌肉侵犯性膀胱癌(MIBC)
> 成人病人，作為其根治性膀胱切除術(radical cystectomy)的前導性治療(neoadjuvant therapy)，並於術後繼續併用
> 作為輔助治療(adjuvant therapy)。」
> 吉舒達（衛部菌疫輸字第001025號）第 6 項尿路上皮癌段落用字相同[D-S30]。

→ **D1／D2 都只作一句指路，不重述那一篇的數字**（依 SPEC §六）。但編輯應把這一點回報給 C 組與上線腳本：
既有文章那句「適用對象也從原本的『不適合 cisplatin』擴大到所有符合條件的病人」在**美國**成立，
在**台灣藥證**（截至 2026-09-13）尚未成立。本組不改既有文章，只列出這個落差。

### 7. Sacituzumab govitecan 的尿路上皮癌適應症**已經被撤回**——這是本專題現成的「加速核准不等於確定有效」教材

FDA 現行 TRODELVY 仿單（effective_time 20260624）的適應症只剩三陰性乳癌與 HR+/HER2− 乳癌，
**完全沒有尿路上皮癌**[D-S32]。EAU 指引章節逐字說明原因[D-S15]：
> 「Sacituzumab govitecan received accelerated FDA approval for mUC with prior platinum and IO pretreatment.
> However, the indication was withdrawn after the TROPiCS-04 trial …because sacituzumab govitecan did not
> significantly improve OS or PFS compared with physician's choice of chemotherapy… In addition, grade 3
> treatment-related AEs (67% vs. 35%) and grade 5 treatment-emergent AEs 7% vs. 2%...were higher」

### 8. THOR cohort 2 是**陰性**的：沒打過免疫治療之前，erdafitinib 並不比 pembrolizumab 好

n=351（erdafitinib 175／pembrolizumab 176），中位追蹤 33 個月：
**OS 10.9 vs 11.1 個月，HR 1.18（95% CI 0.92–1.51，P=0.18）**；PFS 4.4 vs 2.7 個月（HR 0.88）；
ORR 40.0% vs 21.6%，但**反應持續時間 4.3 vs 14.4 個月**[D-S21]。
→ 這是 D2 紅線 7 最好的一根柱子：**反應率較高、存活沒有差別、反應還比較短。**
兩國仿單的 Limitations of Use 就是從這個結果來的[D-S22][D-S30]。

### 9. CheckMate 901 發表的那一組**只收適合 cisplatin 的病人**

EAU 指引章節逐字[D-S15]：「Importantly, both EV-302/KEYNOTE 39A and JAVELIN Bladder 100 included patients fit
for carboplatin, while **CheckMate 901 included patients fit for cisplatin only.**」
台灣健保 9.69 第 3(2)III.i 條也用腎功能把這條線畫出來：「nivolumab 併用化療須符合 eGFR ≥60mL/min/1.73m2」[D-S29]。

### 10. 台灣健保對「不適合化療」的定義，和 Galsky 準則、EAU 措辭**三者不同**

三套並陳（三者都是可引的原文，差異本身就是內容）：

- **Galsky 2011（JCO 29(17):2432–2438）摘要逐字**[D-S11]：
  > 「unfit patients would meet at least one of the following criteria: Eastern Cooperative Oncology Group
  > performance status of 2, creatinine clearance less than 60 mL/min, grade ≥ 2 hearing loss, grade ≥ 2 neuropathy,
  > and/or New York Heart Association Class III heart failure.」
- **EAU 指引章節逐字**[D-S15]：
  > 「At least one of the following criteria must be present: PS > 1; GFR ≤ 60mL/min.; grade ≥ 2 audiometric hearing
  > loss; grade ≥ 2 peripheral neuropathy or New York Heart Association (NYHA) class III heart failure」
- **台灣健保 9.69 第 1(4)I 條逐字**[D-S29]：
  > 「I.不適合接受化學治療之轉移性泌尿道上皮癌成人患者，且需符合下列條件之一：
  > i.CTCAE(the common terminology criteria for adverse events) v4.0 grade≧2 audiometric hearing loss
  > ii.CTCAE v4.0 grade≧2 peripheral neuropathy iii.CIRS(the cumulative illness rating scale) score >6」
  > （腎功能另列於使用條件 3(2)III.i：「單獨使用 pembrolizumab 須符合 eGFR>30mL/min/1.73m2 **且**<60mL/min/1.73m2」）

**健保版沒有 ECOG PS 這一條、也沒有心衰竭這一條，改用 CIRS>6；腎功能是上下兩端都卡的區間。**
C 組亦獨立取得 Galsky 準則（C 組走 [C-S29]／[C-S42] 的轉述路徑，本組走 Europe PMC 摘要原文），
兩組可交叉核對；**兩組的 Galsky 五條內容一致**。

---

## D1 `bl-metastatic`〈轉移之後的第一線變了〉

**本篇最高紀律（紅線 7 上半）：反應率不是治癒率。每一個數字帶試驗名、線別、族群、n、終點、追蹤時間。**

### Key facts

#### A. EV-302／KEYNOTE-A39（第一線，局部晚期或轉移性尿路上皮癌，未曾接受全身治療）

**設計與族群**：全球開放標示隨機第三期，n=886（EV＋P 442／化療 444）；化療組依 cisplatin 適格性給
gemcitabine＋cisplatin 或 carboplatin；EV 1.25 mg/kg D1、D8，pembrolizumab 200 mg D1，每 3 週一次[D-S1]。
**排除條件（要寫，因為它決定誰不在這份數據裡）**：活動性中樞神經轉移、**已存在 ≥2 級感覺或運動神經病變**、
**糖尿病控制不佳（HbA1c ≥8%，或 ≥7% 且有症狀）**、近兩年接受過全身性治療的自體免疫疾病[D-S3][D-S6]。
隨機分層因子：cisplatin 適格性、PD-L1 表現、有無肝轉移[D-S6]。

**效果（兩個追蹤時點都列）**

| 終點 | 註冊分析（中位追蹤 17.2 個月）[D-S1] | 2.5 年更新[D-S2] |
|---|---|---|
| 中位 OS | 31.5 vs 16.1 個月，HR 0.47（95% CI 0.38–0.58），P<0.001 | 33.8（26.1–39.3）vs 15.9（13.6–18.3）個月，HR 0.51（0.43–0.61） |
| 中位 PFS（BICR） | 12.5 vs 6.3 個月，HR 0.45（0.38–0.54），P<0.001 | 12.5（10.4–16.6）vs 6.3（6.2–6.5）個月，HR 0.48（0.41–0.57） |

**反應率（分母要寫出來）**：確認客觀反應率 **67.7%（95% CI 63.1–72.1）vs 44.4%（39.7–49.2）**，
分母是**基準時有可測量病灶者**（EV＋P n=437、化療 n=441），P<0.0001；
**完全反應率 29.1% vs 12.5%**，部分反應 38.7% vs 32.0%[D-S5]。
→ **紅線 7 的操作句：完全反應 29.1% 的那一群，中位總存活仍然是 33.8 個月。影像上看不到腫瘤，不等於治好。**

**依 cisplatin 適格性的次族群**（EV-302 的適格性由試驗主持人依試驗方案判定，不是 Galsky 準則逐條套用）[D-S3]：
- 適合 cisplatin：EV＋P n=244／化療 n=234（94.0% 實際用了 cisplatin）。ORR **70.8% vs 53.0%**
  （絕對差 17.8%，95% CI 9.1–26.2）；完全反應 32.5% vs 15.5%；中位 DOR 未達 vs 8.3 個月。
- 不適合 cisplatin：EV＋P n=198／化療 n=210（97.6% 實際用了 carboplatin）。ORR **63.9% vs 34.9%**
  （絕對差 29.0%，95% CI 19.4–38.0）；完全反應 24.7%；中位 DOR 未達 vs 6.6 個月。
- 作者自己的解釋要一起寫：不適合 cisplatin 那一組的差距比較大，**是因為對照組（carboplatin）的反應率本來就低**，
  不是因為 EV＋P 在這一組特別有效[D-S3]。
- 有肝轉移：OS **19.1 vs 10.1 個月**；無肝轉移：未達 vs 17.9 個月；只有淋巴結轉移：未達 vs 27.5 個月[D-S3]。

**毒性 —— 病人真正要過的日子（全部帶分母）**

EV-302 安全性族群（EV＋P n=440／化療 n=433），FDA 仿單 Table 9 逐筆[D-S5]：

| 不良反應 | EV＋P 全等級 / 3–4 級 | 化療 全等級 / 3–4 級 |
|---|---|---|
| 皮疹（合併多個詞條） | **68% / 15%** | 15% / 0 |
| 周邊神經病變 | **67% / 8%** | 14% / 0 |
| 搔癢 | 41% / 1.1% | 7% / 0 |
| 腹瀉 | 38% / 4.5% | 16% / 1.4% |
| 乾眼 | 24% / 0 | 2.1% / 0 |
| 肺炎／間質性肺病 | 10%（全等級） | — |
| **血糖上升（實驗室值）** | **66% / 14%** | 54% / 5% |

因不良反應**永久停用 EV 者 35%**，其中周邊神經病變單獨就佔 15%、皮疹 4.1%、肺炎／ILD 2.3%；
**暫停給藥 73%**（神經病變 22%、皮疹 16%）；**減量 42%**（皮疹 16%、神經病變 13%）[D-S5]。

**三個「要跟病人講」的長期數字（FDA 仿單 5.1／5.2／5.4 節，la/mUC 合併治療族群 n=564）**[D-S5]：
- **周邊神經病變**：任何等級 67%、2 級 36%、3 級 7%。首次出現 ≥2 級的中位時間 6 個月（範圍 0.3–25 個月）。
  在有結果紀錄的 373 人中，**只有 13% 完全恢復，87% 在最後一次評估時仍有殘留**；殘留者當中 45%（146/326）
  仍是 ≥2 級。**這是本篇最該寫進正文的一句：這個副作用多半不會完全走掉。**
- **皮膚反應**：任何等級 70%、3–4 級 17%（3 級 16%、4 級 1%）。**含史蒂芬強生症候群（SJS）與毒性表皮壞死溶解症（TEN）
  的黑框警語**，且多發生在第一個療程；一人（0.2%）死於大疱性皮膚炎。因皮膚反應停用 EV 者 6%；
  有結果紀錄的 391 人中 59% 完全恢復、41% 仍有殘留。
- **高血糖**：仿單警語明載「Patients with baseline hemoglobin A1C ≥8% were excluded from clinical trials」，
  且高血糖與糖尿病酮酸中毒（含致死案例）在**有沒有糖尿病的人身上都發生過**；EV 單用族群（n=720）任何等級 17%、
  3–4 級 7%；**BMI 越高、基準 A1C 越高，3–4 級高血糖越多**；中位發生時間 0.5 個月；5% 的人因此開始打胰島素，
  其中 66%（23/35）到最後一次評估時已停用胰島素。血糖 >250 mg/dL 時要停藥。

**亞洲族群（含台灣 51 人，最貼近讀者的一份）**[D-S4]：
泛亞洲事後分析 n=176（中國 2、日本 40、新加坡 5、南韓 58、**台灣 51**、泰國 20），EV＋P 94／化療 82；
中位追蹤 28.9／26.6 個月。PFS HR 0.37（0.24–0.57）、OS HR 0.33（0.20–0.54）；**OS 中位數 EV＋P 未達、化療 18.0 個月**；
確認 ORR **72.2%（61.8–81.1）vs 35.0%（24.7–46.5）**，**完全反應 41.1%（37/90）vs 17.5%（14/80）**。
≥3 級治療相關不良事件 66.0% vs 68.4%。
**要寫的那一句**：作者自己指出「grade ≥ 3 skin reactions and hyperglycemia, which were numerically higher in the
pan-Asian subgroup」——亞洲族群的 ≥3 級皮膚反應（28.7%）與高血糖（10.6%）**在數字上比全球族群高**[D-S4]。
其他：周邊感覺神經病變 54.3%（≥3 級 7.4%）、搔癢 53.2%、斑丘疹 27.7%（≥3 級 11.7%）、高血糖 17.0%（≥3 級 10.6%）；
因治療相關不良事件停用 EV 者 28.7%、停用 pembrolizumab 者 19.1%。

#### B. 鉑類化療：三條路，各自的隨機證據

- **GC vs MVAC（第一線，局部晚期或轉移性尿路上皮癌，n=405）**：長期追蹤中位 OS **14.0 vs 15.2 個月**，
  HR 1.09（95% CI 0.88–1.34，P=0.66）；5 年 OS 13.0% vs 15.3%（P=0.53）。
  **有內臟轉移者 5 年 OS 6.8%，無內臟轉移者 20.9%**[D-S13]。→ GC 成為標準是因為毒性較低而非療效較好。
- **高劑量密集 MVAC vs 傳統 MVAC（EORTC 30924，n=263，中位追蹤 7.3 年）**：ORR 64% vs 50%（完全反應 21% vs 9%，P=0.009）；
  中位 PFS 9.5 vs 8.1 個月；**中位 OS 15.1 vs 14.9 個月**；5 年存活 21.8% vs 13.5%；死亡風險比 0.76[D-S14]。
  → **轉移場域的 ddMVAC 隨機證據就只有這一筆，而且對照組是傳統 MVAC，不是 GC。**
  ddMVAC 對 GC 的隨機比較在**轉移場域不存在**；VESPER 那一筆是**術前術後**場域，屬 C 組。
- **不適合 cisplatin 者的 carboplatin（EORTC 30986，第三期部分，n=238，中位追蹤 4.5 年）**：
  收案定義是「GFR <60 但 >30 mL/min 且／或 PS 2」。GC（gemcitabine/carboplatin）vs M-CAVI：
  最佳 ORR 41.2%（確認 36.1%）vs 30.3%（確認 21.0%），P=0.08；**中位 OS 9.3 vs 8.1 個月（P=0.64）**；PFS 無差異；
  嚴重急性毒性 9.3% vs 21.2%[D-S12]。
  → **這是 EV＋P 出現之前，不適合 cisplatin 的病人能拿到的最好數字：中位存活九個月。** 這個對照讓 EV-302 的意義站得住。

**Galsky 準則逐字**（見上方 ⚠ 第 10 點三套並陳）[D-S11][D-S15][D-S29]。
EAU 另有「**連 carboplatin 都不適合**」的一格，逐字[D-S15]：
> 「Patients are unfit for any platinum-based chemotherapy in case of PS > 2, GFR < 30mL/min. or the combination of
> PS 2 and GFR < 60mL/min. as the outcome in this patient population is poor regardless of whether or not
> platinum-based treatment is given」
以及「Approximately 50% of patients with BC are not eligible for cisplatin-based chemotherapy」[D-S15]。

#### C. 維持治療 avelumab（JAVELIN Bladder 100）——**族群是這一段的全部**

隨機第三期，n=700。**收的是「接受四到六個療程第一線 gemcitabine＋cisplatin 或 carboplatin 之後，疾病沒有惡化的人」**；
隨機分到最佳支持療法 ± avelumab 維持[D-S7]。

- 全體族群：**1 年 OS 71.3% vs 58.4%；中位 OS 21.4 vs 14.3 個月，HR 0.69（95% CI 0.56–0.86），P=0.001**
- PD-L1 陽性族群：1 年 OS 79.1% vs 60.4%，HR 0.56（0.40–0.79），P<0.001
- 中位 PFS：全體 3.7 vs 2.0 個月（HR 0.62，0.52–0.75）；PD-L1 陽性 5.7 vs 2.1 個月（HR 0.56，0.43–0.73）
- 任何原因不良事件 98.0% vs 77.7%；**≥3 級 47.4% vs 25.2%**
- EAU 補充的兩年追蹤：OS 仍顯著較長，HR 0.76（0.63–0.91，P=0.0036）；免疫相關不良事件 29%，7% 為 3 級[D-S15]

**誰不適用（必寫）**：第一線化療期間就惡化的人、沒有打滿四到六個療程的人、第一線就用 EV＋P 的人，
這份數據**都套不上去**。台灣健保的維持治療條文更窄，逐字[D-S29]：
> 「III.限 avelumab 用於接受第一線含鉑化學治療 4 至 6 個療程後，疾病未惡化，且達**部分緩解（PR）或疾病呈穩定狀態者(SD)**
> 之無法手術切除局部晚期(stage Ⅲ)或轉移性泌尿上皮癌(stage Ⅳ)成人患者之維持療法。」
→ **試驗收的是「未惡化」（含完全緩解），台灣條文寫的是「達 PR 或 SD」。** 這個措辭差異要照原文並陳，不要替它解釋。

#### D. CheckMate 901（nivolumab＋gemcitabine-cisplatin，第一線）

隨機第三期，n=608（各 304）；**族群是適合 cisplatin 者**[D-S15]。nivolumab 360 mg＋GC 每 3 週最多 6 個療程，
之後 nivolumab 480 mg 每 4 週最多 2 年[D-S9]。中位追蹤 33.6 個月：
- **中位 OS 21.7（18.6–26.4）vs 18.9（14.7–22.4）個月，HR 0.78（95% CI 0.63–0.96），P=0.02**
- **中位 PFS 7.9 vs 7.6 個月，HR 0.72（0.59–0.88），P=0.001**；12 個月 PFS 34.2% vs 21.8%
- 客觀反應 57.6%（完全反應 21.7%）vs 43.1%（完全反應 11.8%）；**完全反應的中位持續 37.1 vs 13.2 個月**
- ≥3 級不良事件 61.8% vs 51.7%
- 注意：EAU 指出**對照組只有 9% 接受了 avelumab 轉換維持治療**[D-S15]——這使它與「GC→avelumab 維持」的比較不對等。

#### E. 第二線以後（簡述，各帶證據等級）

- **EV 單用（EV-301，第三期，n=608）**：族群是打過鉑類**且**在 PD-1/PD-L1 抑制劑期間或之後惡化者。
  中位追蹤 11.1 個月：**中位 OS 12.88 vs 8.97 個月，HR 0.70（0.56–0.89），P=0.001**；
  PFS 5.55 vs 3.71 個月，HR 0.62（0.51–0.75）；≥3 級不良事件 51.4% vs 49.8%[D-S16]。
  → **這正是台灣健保 9.109 條所對應的那一格。**
- **Pembrolizumab 單用（KEYNOTE-045，第三期，n=542，鉑類後）**：
  中位 OS **10.3（8.0–11.8）vs 7.4（6.1–8.3）個月，HR 0.73（0.59–0.91），P=0.002**；
  PD-L1 CPS ≥10 族群 8.0 vs 5.2 個月，HR 0.57（0.37–0.88）；
  **PFS 全體無顯著差異（HR 0.98，0.81–1.19，P=0.42）**；≥3 級治療相關不良事件 15.0% vs 49.4%[D-S17]。
- **Pembrolizumab 單用於不適合任何鉑類者（KEYNOTE-052，單臂，n=370）**：**ORR 29%（95% CI 24–34）、完全反應 10%**，
  中位 DOR 33.4 個月。族群中位年齡 74 歲，**19% 原發於上泌尿道**，85% 有內臟轉移，50% 基準肌酸酐清除率偏低[D-S6]。
  → **單臂試驗、沒有對照組，紅線 7 的第二根柱子：29% 的反應率不能寫成 29% 的治癒率，也不能拿去和隨機試驗比。**
- **Erdafitinib（THOR cohort 1）**：見 D2。
- **Trastuzumab deruxtecan（HER2 IHC 3+）**：見 D2。
- **Sacituzumab govitecan**：**美國適應症已撤回**（見 ⚠ 第 7 點）[D-S15][D-S32]。
- **Disitamab vedotin**：EAU 引兩個第二期試驗合併分析 n=107，ORR 50.5%、中位 PFS 5.9 個月、中位 OS 14.2 個月[D-S15]。
  **台灣藥證資料庫查無此成分（「disitamab」「RC48」零筆）**[D-S30] → 只能寫「中國大陸在用、台灣沒有」，不得多寫。

#### F. 指引怎麼寫（EAU 官方章節原文，附強度）[D-S15]

第一線、適合合併治療者：
> 「Use antibody-drug conjugate enfortumab vedotin (EV) in combination with checkpoint inhibitor (CPI) pembrolizumab.」**Strong**
> 「If contraindications for EV or EV not available: Offer platinum-containing combination chemotherapy (cisplatin or
> carboplatin plus gemcitabine) followed by maintenance treatment with CPI avelumab in patients with at least stable
> disease on chemotherapy.」**Strong**
> 「If contraindications for EV (or EV not available) and cisplatin-eligible: Offer cisplatin/gemcitabine in combination
> with CPI nivolumab.」**Strong**

第一線、不適合合併治療者：
> 「Offer single agent CPI pembrolizumab or atezolizumab in case of high programmed death-ligand 1 (PD-L1)
> expression (for definitions see text).」**Weak**

EAU 對「適合合併治療」的門檻逐字：「Major criteria include ECOG PS 0-2, GFR ≥ 30mL/min. and adequate organ
functions based on eligibility for treatment with EV + P.」[D-S15]

### 反方向的資料（誠實必列）

1. **EV＋P 的代價不是註腳，是主文。** 三分之一的人（35%）因為副作用永久停掉 EV；七成三的人中途暫停過；
   周邊神經病變在最後一次評估時**八成七的人還沒完全恢復**[D-S5]。
   任何一句「新的第一線比化療好」都必須和這些數字同框。
2. **EV-302 的族群是被挑過的。** 已有 ≥2 級神經病變、HbA1c ≥8%、活動性腦轉移的人**不在試驗裡**[D-S3][D-S6]，
   而這三種人在門診並不罕見。
3. **EV-302 的對照組只有約三成接受了 avelumab 轉換維持治療**（EAU 原文：「Thirty percent of the patients in the
   control arm received switch maintenance IO with avelumab.」）[D-S15]——今天的標準化療路徑應該是
   「化療→avelumab 維持」，對照組沒有全部走到那裡，這會讓差距看起來比實務上更大。
4. **CheckMate 901 的對照組只有 9% 用了 avelumab 維持**[D-S15]，同一個問題更嚴重。
5. **EV-103 五年追蹤（n=45，不適合 cisplatin、第一線，中位追蹤 62.1 個月）**：ORR 73.3%、中位 DOR 22.1 個月、
   中位 PFS 12.7 個月、**中位 OS 26.1 個月、五年存活率 41.5%（95% CI 26.5–56.0）**[D-S31]。
   → 這是目前最長的追蹤，**但 n=45、單臂、第 Ib/II 期**。可以寫「有人活過五年」，
   **不可以**寫「五年存活率四成」當成 EV＋P 的通則——EV-302 的追蹤只到 2.5 年，五年數字還沒有。

### Claim ceiling（硬上限）

**可寫**
- 「局部晚期或轉移性尿路上皮癌的第一線，EV＋pembrolizumab 在一個 886 人的第三期隨機試驗裡，
  總存活中位數是化療的兩倍（2.5 年追蹤：33.8 對 15.9 個月，HR 0.51）」——**必帶試驗名、n、追蹤時間**。
- 「反應率 67.7%，其中完全反應 29.1%（分母是有可測量病灶的 437 人）」——**後面必須緊接一句「完全反應不是治癒」**。
- 「不適合 cisplatin 的病人，在 EV＋P 出現之前，carboplatin 方案的中位存活是九個月（EORTC 30986，n=238）」。
- 「打完鉑類、疾病沒有惡化的人，接 avelumab 維持，中位存活 21.4 對 14.3 個月（JAVELIN Bladder 100，n=700）」
  ——**必帶「誰不適用」**。
- 「適合 cisplatin 的人，nivolumab 加上 GC 是另一個隨機試驗證實的第一線選擇（CheckMate 901，n=608，OS 21.7 對 18.9 個月）」。
- 「台灣的健保付的 EV 是第三線、單用、一生六個療程；第一線的 EV＋pembrolizumab 有藥證、沒有給付」——**逐字引條文**。
- 「周邊神經病變在八成七的人身上沒有完全恢復」——這句必寫。

**不可寫**
- 任何把 ORR 或 CR 講成「治好」「清乾淨」「痊癒」的話（紅線 7）。
- 「轉移性膀胱癌現在可以治癒」「有機會長期存活」——**中位存活是 33.8 個月，五年數據只存在於 n=45 的單臂試驗**[D-S31]。
- 「EV＋P 比化療安全」——≥3 級治療相關不良事件 EV＋P 55.9% vs 化療 69.5%[D-S1] 的確較低，
  但**停藥率、神經病變不可逆比例、SJS/TEN 黑框警語**都在 EV 這一邊。只能寫「毒性的形狀不一樣」。
- 把 EV-302 的數字套到**上泌尿道**（E 組）或**肌肉侵犯但未轉移**（C 組）的病人身上。
- 把 2024 年與 2025 年兩組 EV-302 數字混用，或引用其中一組而不標追蹤時間。
- 「不適合 cisplatin 的人用 EV＋P 效果更好」——絕對差較大是因為對照組較差，作者自己說了[D-S3]。
- 任何自費金額。媒體報導的價格一律不可引（SPEC §四固定紅線）。
- 「健保沒給付所以只能自費」這種推論句——條文查得到就引條文，查不到就寫查不到。

### Caveats／safety notes（寫作者必寫）

- **這一篇要在正文顯眼處寫查證日期（2026-09-13）與「這一格變動快」**。
- **副作用的回診訊號要具體**：新出現或加重的手腳麻木無力、皮疹（尤其第一個療程內出現、合併發燒或黏膜破皮）、
  口渴多尿／血糖機數值飆高、走路變喘或乾咳。這些都要「立刻聯絡醫療團隊」，不是「下次回診再說」。
- **不得寫成用藥指南**。劑量、療程數只在說明試驗設計與健保條文時出現，不得寫成「應該怎麼打」。
- **不得建議病人自行停藥或改療程**（沿用既有文章的收尾紀律）。
- 術前術後的 EV＋pembrolizumab **一句指路到站上既有文章**〈三十年沒變的流程，今年動了〉，**不重述其數字**（SPEC §六）。
- 保留膀胱與切除膀胱的比較**不屬本篇**（SPEC §六：C4 專屬）。

### 台灣端（D1）

| 項目 | 狀態（2026-09-13） | 來源 |
|---|---|---|
| Enfortumab vedotin 藥證 | 衛部菌疫輸字第001212號（20mg）／001213號（30mg），發證 2022/12/28、有效 2027/12/28、異動 2026/05/08。適應症含單用三線、**併用 pembrolizumab 治 la/mUC**、併用 pembro 治**不適合 cisplatin 的 MIBC** 術前術後 | [D-S30] |
| Enfortumab vedotin 健保 | **9.109，生效 113/5/1。第三線單用、事前審查、每次 3 個療程、每人限 6 個療程。第一線合併用法：全文零筆** | [D-S29] |
| Pembrolizumab 藥證 | 衛部菌疫輸字第001025號，異動 2026/08/27。尿路上皮癌段含：併用 EV 治 la/mUC；鉑類後單用；**不適合任何含鉑化療者單用**；BCG 無反應高危 NMIBC 併 CIS；併用 EV 治不適合 cisplatin 的 MIBC 術前術後 | [D-S30] |
| Pembrolizumab 健保 | 9.69 第 1(4) 條 I（不適合化療，三選一條件）與 II（鉑類失敗後）。**PD-L1 CPS≧10（P042 一線單用／P041 二線）**；一線單用另需 eGFR>30 且<60 | [D-S29] |
| Avelumab 藥證 | 衛部菌疫輸字第001085號，發證 2018/08/07、有效 2028/08/07、異動 2026/02/10。尿路上皮癌**只有維持療法一項**（台灣藥證未含二線單用） | [D-S30] |
| Avelumab 健保 | 9.69 第 1(4)III（維持療法，4–6 療程後 PR 或 SD）；**PD-L1 不需檢附報告（P043）**；需 eGFR>30 | [D-S29] |
| Nivolumab 藥證 | 衛部菌疫輸字第001013號，發證 2025/06/06、有效 2031/03/04、異動 2025/12/04。尿路上皮癌三項：併 cis＋gem 一線／鉑類後（**加速核准，仿單逐字載明需確認性試驗**）／根治切除後高復發風險輔助 | [D-S30] |
| Nivolumab 健保 | 9.69 第 2(9) 條，生效 115/2/1：「限 nivolumab 與 cisplatin 及 gemcitabine 併用至多 6 個療程，接續限單用 nivolumab，做為無法切除或轉移性泌尿道上皮癌成人病人的第一線治療」。**PD-L1 TC≥1%（P044）**，需 eGFR ≥60 | [D-S29] |
| 重大傷病項次 | **gap**（C 組 law.moj.gov.tw 逐一嘗試失敗，本組未重複；寫「問醫務課／個管師」） | [C-F10] |
| 自費金額 | **gap。查無官方公告可引。媒體報導價格一律不可用**（SPEC §四） | — |

### 給繪圖組的數字（`fig-bl-metastatic`，SPEC §七第 10 張）

決策分岔：**鉑類能不能用**。每一格都必須帶試驗名、n、族群、追蹤時間，並在圖上標**查證日期 2026-09-13**。

- 分岔一「適合合併治療（ECOG 0–2、GFR ≥30）」→ EV＋pembrolizumab：EV-302，n=886，OS 33.8 vs 15.9 個月（2.5 年追蹤）[D-S2]
- 分岔二「不適合 EV」→（a）鉑類＋gemcitabine → avelumab 維持：JAVELIN Bladder 100，n=700，OS 21.4 vs 14.3 個月[D-S7]
  （b）適合 cisplatin 者：nivolumab＋GC，CheckMate 901，n=608，OS 21.7 vs 18.9 個月[D-S9]
- 分岔三「不適合 cisplatin、適合 carboplatin」→ GemCarbo：EORTC 30986，n=238，OS 9.3 個月[D-S12]
- 分岔四「連 carboplatin 都不適合（PS>2 或 GFR<30 或 PS2＋GFR<60）」→ pembrolizumab 單用：KEYNOTE-052，n=370，
  **單臂**，ORR 29%[D-S6][D-S15]
- **圖上必須有的一行警語**：「反應率不是治癒率」＋「台灣健保給付的 EV 是第三線」
- **圖上不可出現**：任何治癒率、五年存活率、自費金額

---

## D2 `bl-biomarker`〈基因檢測與標靶：哪一格真的有藥〉【紅線 7】

**本篇最高紀律：「有基因突變就有藥」必須寫到無法拼湊出來。**
每一格生物標記都要同時寫三件事：**多少人有（帶分母）／測什麼（測法本身的限制）／有藥的那一格有多窄。**

### Key facts

#### A. FGFR 與 erdafitinib

**盛行率（帶分母，並分上泌尿道與膀胱）**

- **真實世界反射性檢測世代（加拿大兩家醫學中心，2021–2025，前瞻性 NGS，n=366）**[D-S26]：
  下泌尿道 239、上泌尿道 72、轉移病灶 55。
  - 任何 FGFR1–4 變異：59 人（**16.1%**）
  - **可用藥（actionable）的 FGFR 變異：49 人（13.4%）**（FGFR3 突變 33、FGFR3 融合 13、FGFR2 突變 3）
  - **上泌尿道 23.8% vs 下泌尿道 13.8%（P=0.007）**
  - 肺轉移 57.1% vs 其他轉移部位 10.4%（P=0.002）
  - 轉移 16.4% vs 原發 12.9%（P=0.482，未達顯著）
  - 收案條件：只做在轉移或 pT3/pT4 的檢體上；**49 人全部 ≥55 歲**
- **日本 C-CAT 全國登記（轉移性尿路上皮癌，FoundationOne，2019/01–2025/06，n=1,014）**[D-S27]：
  - **FGFR3 變異 157 人（15.5%）；ERBB2（HER2）擴增 150 人（14.8%）**
  - 兩者同時出現 13 人（1.3%），在統計獨立假設下預期 2.3%，實際顯著較低（P=0.010，粗 OR 0.47）
  - 多變項分析：**上泌尿道原發與 HER2 擴增機率較低有關（OR 0.57，95% CI 0.39–0.84，P=0.005）**；
    女性亦然（OR 0.58，0.36–0.93，P=0.024）
- **前瞻性 ctDNA／組織對照世代（加拿大 12 中心，2021/01–2024/04，n=208）**[D-S28]：
  **組織或 ctDNA 任一測到 FGFR 變異的比率 26%**。（注意：這個世代是「正在考慮用 erdafitinib」的病人，
  且**已知沒有組織可用的病人根本沒被納入篩選**——分母被挑過，比率不可當成一般盛行率。）

→ **可寫的通則只有：大約每六到七個轉移性尿路上皮癌病人有一個帶可用藥的 FGFR 變異，上泌尿道比膀胱多一些。**
不可寫成「兩成的人有藥可用」。

**THOR cohort 1（erdafitinib vs 化療，第三期）**[D-S18][D-S19]

- 族群：轉移性尿路上皮癌、帶**敏感性 FGFR3/2 變異**、**在一或兩線治療後惡化且其中包含 anti-PD-1/PD-L1**
- n=266（erdafitinib 136／化療 130，化療為醫師選擇的 docetaxel 或 vinflunine）；中位追蹤 15.9 個月
- **中位 OS 12.1 vs 7.8 個月，HR 0.64（95% CI 0.47–0.88），P=0.005**
- **中位 PFS 5.6 vs 2.7 個月，HR 0.58（0.44–0.78），P<0.001**
- **ORR 45.6% vs 11.5%**（數字出自試驗官方 plain language summary[D-S19]，NEJM 摘要不含此數）
- 6 個月存活 85%、12 個月存活 51%[D-S19]
- 3–4 級治療相關不良事件 45.9% vs 46.4%；治療相關致死 0.7% vs 5.4%[D-S18]
- **預先計畫的期中分析顯示 erdafitinib 較好之後，化療組被允許轉換到 erdafitinib**[D-S19]——OS 解讀要帶這一句
- EAU 轉述的 ≥3 級常見項目：手足症候群 9.6%、口腔黏膜炎 8.1%、甲床分離 5.9%、高磷酸鹽血症 5.2%[D-S15]

**THOR cohort 2（陰性）**：見 ⚠ 第 8 點[D-S21]。

**伴隨式診斷到底測什麼（這一段是紅線 7 的核心）**

- 美國核准的伴隨式診斷是 **QIAGEN therascreen® FGFR RGQ RT-PCR Kit**，一個**定性的 RNA/PCR 組織檢測**[D-S22]。
- THOR cohort 1 裡，**75% 的病人由中央實驗室用這個套組判定，其餘 25% 由當地 NGS 判定**[D-S22]。
- 它測的是一份**寫死的清單**：FGFR3 突變 R248C、S249C、G370C、Y373C，以及融合 FGFR3-TACC3、FGFR3-BAIAP2L1、
  FGFR2-BICC1、FGFR2-CASP7[D-S22]。獨立研究對它的描述是「a qualitative RT-PCR tumor tissue test that detects
  **nine recurrent FGFR alterations (4 hotspot mutations and 5 fusions)**」，並指出
  「**no internationally standardized testing approach exists**, contributing to assay-dependent variability in
  patient selection and access to FGFR-targeted therapies」[D-S28]。
- → **「報告上寫 FGFR 有變異」和「這個變異在那份清單上」是兩件事。** 這一句必須進正文。

**Erdafitinib 的特徵毒性（FDA 仿單，pooled safety population）**[D-S22]

- **中心性漿液性視網膜病變／視網膜色素上皮剝離（CSR/RPED）：22%**，中位首次發生時間 **46 天**。
  在 104 位發生 CSR 的病人中：40% 需暫停給藥、56% 需減量、2.9% 永久停藥；
  **暫停後重新開始的 24 人裡，67% 再度發生或惡化**；**最後一次評估時 41% 仍在進行中**。
  乾眼症狀 26%。仿單要求：**前四個月每月一次眼科檢查、之後每三個月一次、有視覺症狀隨時就醫**，
  檢查須含視力、裂隙燈、眼底鏡與光學同調斷層掃描。
- **高磷酸鹽血症**：仿單明載這是**藥理學上的必然效應**（「Increases in phosphate levels are a pharmacodynamic
  effect of BALVERSA」）；24% 的病人在治療期間用了磷結合劑；限制飲食磷攝取 600–800 mg/日；
  血磷 >7.0 mg/dL 時加磷結合劑。血管鈣化見於 0.2%。
- **指甲與皮膚**：指甲疾患、口腔黏膜炎、手足症候群為最常見的減量與暫停原因
  （因不良反應暫停 68%，其中高磷酸鹽血症 24%、口腔黏膜炎 17%、指甲 16%、CSR 9%；
  因不良反應減量 53%，其中指甲 21%、口腔黏膜炎 15%、CSR 14%）。
- 嚴重不良反應 41%；**永久停藥 21%**，最常見原因就是 CSR（4.6%）。
- THOR cohort 1 整體族群（erdafitinib n=135／化療 n=112）[D-S20]：
  高磷酸鹽血症 78.5%（≥3 級 5.2%）、味覺異常 25.2%、甲床分離 23.0%（≥3 級 5.9%）、甲脫落 20.0%、甲溝炎 11.9%；
  **因不良事件減量 68.9%、暫停 71.9%**（化療組分別為 24.1%、31.3%）。
  日本次族群（n=14）最常見治療相關不良事件為味覺異常與高磷酸鹽血症各 71.4%、甲脫落 64.3%[D-S20]。

**真實世界的耐受性**：在前瞻性 ctDNA 世代中，21 位實際用了 erdafitinib 的病人，**6 人（29%）因毒性停藥**，
中位 PFS 7.5 個月；作者自己說這比註冊試驗的 5.6 個月好，可能是因為**43% 是在第二線而非第三線用**[D-S28]。

#### B. HER2 與 trastuzumab deruxtecan

**「HER2 3+」在這裡是什麼意思**

- DESTINY-PanTumor02 的 HER2 判定，仿單與論文都寫明是用**胃癌的 ASCO/CAP 判讀準則**
  （「HER2-overexpressing tumors with IHC 3+/2+ (local or central testing) scored using current ASCO/College of
  American Pathology guidelines for scoring HER2 in **gastric cancer**」）[D-S23]——**不是乳癌那一套**。
- **本地實驗室與中央實驗室的判讀一致率只有 58.6%（IHC 3+）、54.5%（IHC 2+）、合併 73.4%**（事後分析，n=267，
  其中 75.7% 是憑本地檢測收案的）[D-S24]。作者結論逐字：
  > 「The moderate concordance observed between local and central IHC testing in DESTINY-PanTumor02 highlights the
  > need for a **validated diagnostic test and standardized algorithm** for HER2 status assessment in solid tumors」
- **ERBB2 基因擴增 ≠ HER2 IHC 3+**。日本登記研究測的是 ERBB2 擴增（14.8%）[D-S27]，那是另一種檢測、另一個定義。

**膀胱／尿路上皮癌世代的數字（分母很小，要寫出來）**[D-S23]

- DESTINY-PanTumor02 是**第二期、開放標示、單臂、多世代**（七個癌別，共 267 人），族群是
  「先前至少接受過一種全身治療、或沒有其他合適治療選項」的 HER2 表現（IHC 3+/2+）實體腫瘤。
- **膀胱世代（cohort 2）定義逐字**：「metastatic or advanced urothelial carcinoma, including transitional cell or
  predominantly transitional cell carcinoma of the renal pelvis, ureter, urinary bladder, or urethra」
  → **這個世代把上泌尿道包在裡面**，數字不可貼上「膀胱癌」的標籤而不註明。
- **膀胱世代 n=41：試驗主持人評估 ORR 39.0%（95% CI 24.2–55.5）；獨立中央判讀 41.5%（26.3–57.9）**
- **中央確認 IHC 3+ 的膀胱世代：n=16，ORR 56.3%（95% CI 29.9–80.2）** ← **分母十六個人。**
- EAU 補充：膀胱世代中位 PFS 7.0 個月、中位 OS 12.8 個月[D-S15]
- 全體 267 人的安全性：**≥3 級藥物相關不良事件 40.8%；經判定為藥物相關的間質性肺病 10.5%，其中三人死亡**[D-S23]
- FDA 的核准依據是**三個試驗合併的 192 人**（DESTINY-PanTumor02 貢獻 111 位 IHC 3+ 病人，可由本地或中央判讀），
  且是**加速核准**[D-S25]

#### C. PD-L1：一個停止選人、卻沒有停止付錢的生物標記

**為什麼它不再是第一線的選人依據（時間順序）**

1. **KEYNOTE-052（單臂，n=370，不適合任何鉑類）**與同類的 atezolizumab 單臂試驗，是 cisplatin 不適合者
   第一線單用免疫治療的最初依據；歐盟核准時綁上 PD-L1 門檻（pembrolizumab CPS ≥10 Dako 22C3；
   atezolizumab 腫瘤浸潤免疫細胞 ≥5% Ventana SP142）[D-S15]。
2. **KEYNOTE-361（第三期，n=1,010，未曾治療）失敗**。FDA 仿單逐字[D-S6]：
   > 「The study did not meet its major efficacy outcome measures of improved PFS or OS in the intravenous
   > pembrolizumab plus chemotherapy arm compared to the chemotherapy-alone arm. Additional efficacy endpoints,
   > including improvement of OS in the intravenous pembrolizumab monotherapy arm, **could not be formally tested**.」
   > 另載：「The safety and efficacy of intravenous pembrolizumab in combination with platinum-based chemotherapy for
   > previously untreated patients with locally advanced or metastatic urothelial carcinoma **has not been established**.」
3. **美國現行的 pembrolizumab 第一線單用適應症，改成「不適合任何含鉑化學治療」，沒有 PD-L1 條件**，逐字[D-S6]：
   > 「as a single agent for the treatment of adult patients with locally advanced or metastatic urothelial carcinoma who:
   > **are not eligible for any platinum-containing chemotherapy**, or who have disease progression during or following
   > platinum-containing chemotherapy or within 12 months of neoadjuvant or adjuvant treatment with platinum-containing
   > chemotherapy.」
   → **門檻從「生物標記」換成了「身體撐不撐得住鉑類」。這就是這個生物標記退場的方式。**
4. **EV-302 的隨機分層雖然納入 PD-L1，但 EAU 的結論是「All prespecified subgroups benefited equally from EV + P,
   regardless of cisplatin eligibility, PD-L1 expression or presence of liver metastases.」**[D-S15]
5. **atezolizumab 在美國現行仿單已無任何尿路上皮癌適應症**（openFDA TECENTRIQ 仿單全文檢索「urothelial」零筆）[D-S32]。

**但它在付錢的規則裡還活著**：台灣健保四列 PD-L1 門檻見 ⚠ 第 3 點的表[D-S29]；歐盟仍以 PD-L1 綁住
cisplatin 不適合者的單用適應症[D-S15]。

#### D. 檢測的現實（這一節是本篇的落點）

- **什麼時候測**：EAU 把 erdafitinib 放在**後線**（「After prior EV + CPI：If actionable FGFR alterations: offer
  erdafitinib」**Strong**；「After prior platinum-based chemotherapy +/- CPI：If actionable FGFR alterations and prior
  CPI: offer erdafitinib」**Strong**）[D-S15]；T-DXd 更後面（「Further treatment after EV, CPI, platinum-based
  therapy：Offer antibody-drug conjugate Trastuzumab deruxtecan in case of HER2 over expression (IHC 3+) and consider
  in case of HER2 (IHC 2+)」**Weak**）[D-S15]。
  → **這兩格藥都不在第一線。第一線不會因為測到基因變異而改變。** 這一句要寫清楚。
  但檢測本身可以早做——THOR 日本次族群作者的建議逐字：「**early FGFR testing after diagnosis of mUC should be
  considered**」[D-S20]。
- **組織還是抽血**：前瞻多中心研究（加拿大 12 中心，n=208，2021/01–2024/04）[D-S28]：
  - 組織或 ctDNA 任一測到 FGFR 變異 26%
  - 有可判讀 ctDNA 且有配對組織結果的 125 人中，**兩者一致 90%**；
    **ctDNA 對組織測到的變異敏感度 84%**，另外**多找到 7 個案例**
  - 有一名病人的上泌尿道切片測到 FGFR3-TACC3 融合，但**在任何一次 ctDNA 檢體都沒測到**——作者解釋為
    FGFR 的時空異質性
  - 結論逐字：「support clinical uptake of ctDNA FGFR testing **in combination with** tissue-based approaches」
    → **是互補，不是取代。**
  - 重要的分母限制：**「Patients known to have no tissue available were not screened.」**——連這個世代都把
    沒有組織的人排除在外了。
- **測到了，離拿到藥還有多遠**：同一個世代 208 人，**到資料截止時只有 21 人真的用到 erdafitinib**
  （作者說明還有其他 FGFR 陽性病人尚未在目前這一線惡化）[D-S28]。這 21 人裡 6 人（29%）因毒性停藥。
- **周轉時間（turnaround time）**：**gap。** 本組在兩篇前瞻研究的全文中均未找到可引用的檢測周轉天數。
  → **不可寫「大約兩到三週」這類數字**，只能寫「要等報告，時間依實驗室而異，問你的主治醫師或個管師」。
- **台灣端的斷點**：erdafitinib **有藥證、健保零筆**[D-S29][D-S30]；
  T-DXd 的泛腫瘤 HER2 IHC 3+ **有藥證、健保只付乳癌**[D-S29][D-S30]。
  → **「檢測測出來了、藥證也有了、健保不付」是台灣這一格最真實的形狀，也是本篇最該誠實寫出來的一句。**

### 反方向的資料（誠實必列）

1. **THOR cohort 2 是陰性的**：沒用過免疫治療的 FGFR 變異病人，erdafitinib 的 OS 並不優於 pembrolizumab
   （10.9 vs 11.1 個月，HR 1.18）[D-S21]。作者自己寫「Outcomes with pembrolizumab were better than assumed」。
   → **有 FGFR 變異，不代表 FGFR 抑制劑一定是那個人此刻最好的藥。**
2. **T-DXd 在尿路上皮癌的證據是單臂第二期、n=41（IHC 3+ 只有 n=16），且是加速核准**[D-S23][D-S25]。
3. **HER2 IHC 判讀的本地／中央一致率只有 58.6%（3+）**[D-S24]——同一份檢體換一間實驗室可能換一個答案。
4. **FGFR3 變異與 ERBB2 擴增在轉移性尿路上皮癌裡大致互斥**（同時具備者 1.3%，低於獨立假設的 2.3%，P=0.010）[D-S27]
   → 不能寫成「做了全面基因檢測就會有好幾格可以選」。
5. **Sacituzumab govitecan 的前車之鑑**：加速核准拿到過，確認性試驗（TROPiCS-04）失敗後被撤回[D-S15][D-S32]。
   這是寫「加速核准是什麼意思」最好的現成案例。

### Claim ceiling（硬上限）

**可寫**
- 「轉移性尿路上皮癌大約每六到七人有一人帶可用藥的 FGFR 變異，上泌尿道（23.8%）比下泌尿道（13.8%）多」
  ——**帶 n=366、帶反射性檢測世代的條件**[D-S26]。
- 「帶 FGFR3/2 變異、打過免疫治療後惡化的人，erdafitinib 的中位存活 12.1 對 7.8 個月（THOR cohort 1，n=266）」。
- 「erdafitinib 的眼睛副作用（中心性漿液性視網膜病變）發生率兩成二，中位發生在第 46 天，
  兩成一的人最後因副作用永久停藥，所以要定期看眼科」[D-S22]。
- 「HER2 IHC 3+ 的尿路上皮癌，trastuzumab deruxtecan 在一個第二期單臂試驗的 16 人裡有九人（56.3%）縮小」
  ——**分母必須寫出來，且必須註明是加速核准**。
- 「PD-L1 在試驗裡已經不是第一線選人的依據，但在台灣健保仍然是付錢的門檻（pembrolizumab 一線單用 CPS≧10）」
  ——**兩句必須同框**。
- 「台灣：erdafitinib 有藥證、健保給付規定全文搜尋零筆；trastuzumab deruxtecan 的泛腫瘤 HER2 適應症有藥證、
  健保只給付乳癌。要怎麼申請，問醫務課或個管師。」

**不可寫**
- **任何可以拼出「有基因突變就有藥」的句子。** 三個條件必須同時出現：變異在那份清單上、已經走到那個線別、
  台灣拿得到藥。
- 「做基因檢測可以幫你找到最適合的治療」——**第一線不會因為基因檢測而改變**[D-S15]。
- 「FGFR2 或 FGFR3 突變都可以用 erdafitinib」——現行台灣與美國仿單都寫 **FGFR3**[D-S22][D-S30]。
- 把 ORR 寫成治癒率（紅線 7）；把 56.3%（n=16）寫成「HER2 陽性膀胱癌有一半以上會好」。
- 「抽血就可以驗，不用切片」——ctDNA 對組織測到的變異敏感度是 84%，作者結論是**互補**不是取代[D-S28]。
- 任何檢測周轉天數、任何自費檢測金額（本組均為 gap）。
- 「健保沒付所以自費多少錢」——媒體價格一律不可引（SPEC §四固定紅線）。

### Caveats／safety notes（寫作者必寫）

- **正文要標查證日期 2026-09-13**，並寫「藥證與給付是會動的，看到這篇時請跟主治醫師或個管師確認現況」。
- **erdafitinib 的眼科追蹤是硬要求**，要具體寫「視力模糊、視野中央有暗點或扭曲，不要等下次回診」[D-S22]。
- **T-DXd 的間質性肺病要寫**：10.5% 判定為藥物相關，其中三人死亡（全體 267 人）[D-S23]；
  新出現的乾咳、走路變喘、發燒要立刻聯絡醫療團隊。
- 上泌尿道的部分**只作一句指路到 E1**（SPEC §六）；但 FGFR 上下泌尿道盛行率差異屬本篇（因為它決定「誰值得測」），
  **且必須標明這是分子流行病學、不是台灣的發生率資料**。
- 不得寫成檢測指南或建議病人自行去做自費檢測。

### 台灣端（D2）

| 項目 | 狀態（2026-09-13） | 來源 |
|---|---|---|
| Erdafitinib 藥證 | 盼樂膜衣錠 3／4／5 毫克，衛部藥輸字第027912／027913／027914號。發證 2020/07/10、有效 2030/07/10、異動 2025/10/20。適應症：**FGFR3** 敏感性變異＋至少一線全身治療後惡化；含「不建議用於適合但未曾使用 PD-1／PD-L1 抑制劑者」之使用限制 | [D-S30] |
| Erdafitinib 健保 | **《藥品給付規定》（115.8.21 更新）全文搜尋「erdafitinib」「Balversa」「盼樂」— 零筆。** 依 SPEC §四：寫查不到列項，問醫務課／個管師，**不推論有無給付** | [D-S29] |
| Trastuzumab deruxtecan 藥證 | 優赫得凍晶注射劑 100 毫克，衛部菌疫輸字第001179號；達卓優凍晶注射劑 100 毫克，衛部菌疫輸字第001302號。適應症第六項含泛腫瘤 **HER2 陽性（IHC 3+）實體腫瘤** | [D-S30] |
| Trastuzumab deruxtecan 健保 | 9.115（生效 114/2/1）**只有乳癌兩段**；泌尿道上皮癌／實體腫瘤泛適應症零筆 | [D-S29] |
| PD-L1 檢測（健保） | 9.69 第 3(3) 條表格逐字：一線單用 pembrolizumab **CPS≧10**（P042）、一線併化療 nivolumab **TC≥1%**（P044）、二線 pembrolizumab **CPS≧10** 與 nivolumab **TC≧5%**（P041）、維持療法 avelumab **不需檢附報告**（P043）。檢測平台在表頭逐一指定（pembrolizumab：Dako 22C3 或 Ventana SP263；nivolumab：Dako 28-8 或 Ventana SP263；atezolizumab：Ventana SP142；avelumab：Ventana SP263），並註「* Ventana SP263 僅適用於檢測非小細胞肺癌或泌尿道上皮癌維持療法」 | [D-S29] |
| FGFR 檢測的健保給付 | **gap。** 9.69 通則十二（基因檢測的共通要求）在條文中被反覆引用，但本組未取得通則十二的完整條文對照到 FGFR；**不可推論** | [D-S29] |
| Disitamab vedotin | **台灣藥證資料庫零筆**（「disitamab」「RC48」皆 0） | [D-S30] |
| 檢測周轉時間、自費檢測金額 | **gap。查無可引官方或文獻數字** | — |

### 給繪圖組的數字（D2 無指定圖；若要畫，建議「三欄表」而非流程圖）

三欄：**多少人有（帶分母）｜測什麼｜台灣拿不拿得到**

- FGFR3/2：可用藥變異 13.4%（n=366 反射性檢測世代；上泌尿道 23.8%、下泌尿道 13.8%）[D-S26]｜
  美國伴隨式診斷為 RT-PCR，測 4 個熱點突變＋5 個融合的固定清單[D-S22][D-S28]｜**有藥證、健保零筆**[D-S29][D-S30]
- HER2 IHC 3+：DESTINY-PanTumor02 膀胱世代 n=41，中央確認 3+ 只有 n=16[D-S23]｜
  以**胃癌**判讀準則計分；本地與中央一致率 58.6%[D-S23][D-S24]｜**有藥證（泛腫瘤）、健保只付乳癌**[D-S29][D-S30]
- PD-L1：不再是第一線試驗的選人依據[D-S6][D-S15]｜Dako 22C3／28-8、Ventana SP263／SP142，平台各自綁定[D-S29]｜
  **台灣健保仍以它當門檻**[D-S29]
- **圖上必須有的一行**：「這三格藥都不在第一線」＋查證日期
- **圖上不可出現**：治癒率、任何金額、任何「建議去做檢測」的指引語氣

---

## 來源清單

### PASS

- **[D-S1] PASS** Powles T, Valderrama BP, Gupta S, et al.（EV-302 Trial Investigators）.
  *Enfortumab Vedotin and Pembrolizumab in Untreated Advanced Urothelial Cancer.*
  **N Engl J Med. 2024;390(10):875–888.** DOI 10.1056/NEJMoa2312117｜PMID 38446675｜**非 OA**。NCT04223856。
  Route: Europe PMC REST `search?query=EXT_ID:38446675&resultType=core&format=json`，2026-09-13。
  **可引用範圍：摘要內可見者**（n=886、442/444、追蹤 17.2 個月、PFS 12.5 vs 6.3 HR 0.45(0.38–0.54)、
  OS 31.5 vs 16.1 HR 0.47(0.38–0.58)、療程數中位 12 vs 6、≥3 級治療相關不良事件 55.9% vs 69.5%）。
  **ORR 與各項毒性細目不在摘要內，一律改引 [D-S5]（FDA 仿單）或 [D-S3]。**
- **[D-S2] PASS** Powles TB, Van der Heijden MS, Loriot Y, et al.
  *Enfortumab vedotin plus pembrolizumab in untreated locally advanced or metastatic urothelial carcinoma:
  2.5-year median follow-up of the phase III EV-302/KEYNOTE-A39 trial.*
  **Ann Oncol. 2025;36(10):1212–1219.** DOI 10.1016/j.annonc.2025.05.536｜PMID 40460988｜**非 OA**。
  Route: Europe PMC REST（TITLE）。**摘要含全部可引數字**：PFS 12.5(10.4–16.6) vs 6.3(6.2–6.5) HR 0.48(0.41–0.57)；
  OS 33.8(26.1–39.3) vs 15.9(13.6–18.3) HR 0.51(0.43–0.61)。
- **[D-S3] PASS** van der Heijden MS, Powles T, Gupta S, et al.
  *Exploratory subgroup analyses of EV-302: a phase III global study to evaluate enfortumab vedotin in combination
  with pembrolizumab versus chemotherapy in previously untreated locally advanced or metastatic urothelial carcinoma.*
  **ESMO Open. 2025;10(8):105544.** DOI 10.1016/j.esmoop.2025.105544｜PMID 40795788｜PMCID PMC12361773｜**OA**。
  Route: Europe PMC REST ＋ `/webservices/rest/PMC12361773/fullTextXML`。
  用途：cisplatin 適格性次族群（n、ORR、CR、DOR）、肝／內臟／淋巴結轉移次族群 OS、試驗排除條件原文。
- **[D-S4] PASS** Kikuchi E, Van der Heijden MS, Valderrama BP, et al.
  *Pan-Asian subgroup analysis of EV-302/KEYNOTE-A39: a phase 3 study to evaluate enfortumab vedotin and pembrolizumab
  in patients with untreated advanced urothelial carcinoma.*
  **Int J Clin Oncol. 2026;31(3):436–446.** DOI 10.1007/s10147-025-02950-8｜PMID 41563650｜PMCID PMC12932347｜**OA**。
  Route: Europe PMC REST ＋ fullTextXML。用途：亞洲族群（含台灣 51 人）療效與毒性、
  「≥3 級皮膚反應與高血糖在亞洲族群數字上較高」的作者原句、全球 ORR 67.7% vs 44.4% 的轉述。
- **[D-S5] PASS** U.S. FDA. **PADCEV (enfortumab vedotin-ejfv) for injection, prescribing information.**
  Route: openFDA `https://api.fda.gov/drug/label.json?search=openfda.brand_name:"PADCEV"&limit=1`，
  **effective_time 20260804**，set/spl id e8e304ca-8a56-4869-96e2-427ee4a1fe3c，2026-09-13 抓取。
  用途：適應症全文（含 MIBC 術前術後與 la/mUC 合併）、黑框警語、5.1 皮膚反應／5.2 高血糖／5.4 周邊神經病變、
  EV-302 Table 9（不良反應）與 Table 10（實驗室異常）、EV-302 Table 22（療效，ORR 67.7%／CR 29.1%）、
  停藥／暫停／減量比率。
- **[D-S6] PASS** U.S. FDA. **KEYTRUDA (pembrolizumab) prescribing information.**
  Route: openFDA brand_name:"KEYTRUDA"，**effective_time 20260731**，set_id 097d166f-b73b-41d3-9b37-7653cd2a0c41，
  2026-09-13。用途：尿路上皮癌適應症全文（**無 PD-L1 條件**）、KEYNOTE-052（n=370、ORR 29%、CR 10%、
  DOR 33.4 個月、19% 上泌尿道原發）、**KEYNOTE-361 失敗的仿單原文**、KEYNOTE-A39 收案與排除條件。
- **[D-S7] PASS** Powles T, Park SH, Voog E, et al. *Avelumab Maintenance Therapy for Advanced or Metastatic Urothelial Carcinoma.*
  **N Engl J Med. 2020;383(13):1218–1230.** DOI 10.1056/NEJMoa2002788｜PMID 32945632｜**非 OA**。NCT02603432。
  Route: Europe PMC REST（EXT_ID）。**摘要含全部可引數字**（n=700、1 年 OS 71.3%/58.4%、
  中位 OS 21.4/14.3 HR 0.69(0.56–0.86)、PD-L1 陽性 HR 0.56(0.40–0.79)、PFS 3.7/2.0 與 5.7/2.1、
  ≥3 級不良事件 47.4%/25.2%）。
- **[D-S8] PASS** U.S. FDA. **BAVENCIO (avelumab) prescribing information.**
  Route: openFDA brand_name:"BAVENCIO"，**effective_time 20260825**，set_id 5cd725a1-2fa4-408a-a651-57a7b84b2118。
  用途：維持治療適應症逐字（「has not progressed with first-line platinum-containing chemotherapy」，**無 PD-L1 條件**）。
- **[D-S9] PASS** van der Heijden MS, Sonpavde G, Powles T, et al.（CheckMate 901 Trial Investigators）.
  *Nivolumab plus Gemcitabine-Cisplatin in Advanced Urothelial Carcinoma.*
  **N Engl J Med. 2023;389(19):1778–1789.** DOI 10.1056/NEJMoa2309863｜PMID 37870949｜PMCID PMC12314471｜**非 OA**。
  NCT03036098。Route: Europe PMC REST（EXT_ID）；**`/PMC12314471/fullTextXML` 回傳 0 bytes，全文取不到**，
  可引用範圍限摘要（n=608、追蹤 33.6 個月、OS 21.7/18.9 HR 0.78(0.63–0.96) P=0.02、
  PFS 7.9/7.6 HR 0.72(0.59–0.88) P=0.001、12 個月 PFS 34.2%/21.8%、ORR 57.6%(CR 21.7%)/43.1%(CR 11.8%)、
  CR 中位持續 37.1/13.2 個月、≥3 級不良事件 61.8%/51.7%）。
  **「只收適合 cisplatin 者」這一句改引 [D-S15] 的 EAU 原文。**
- **[D-S10] PASS** U.S. FDA. **OPDIVO (nivolumab) prescribing information.**
  Route: openFDA brand_name:"OPDIVO"，**effective_time 20260512**，set_id 7f8c38fa-42f4-4387-9e8c-7a1c66855d8b。
  用途：尿路上皮癌三項適應症（輔助、一線併 cis＋gem、鉑類後）。
- **[D-S11] PASS** Galsky MD, Hahn NM, Rosenberg J, et al.
  *Treatment of patients with metastatic urothelial cancer "unfit" for Cisplatin-based chemotherapy.*
  **J Clin Oncol. 2011;29(17):2432–2438.** DOI 10.1200/JCO.2011.34.8433｜PMID 21555688｜**非 OA**。
  Route: Europe PMC REST（TITLE＋AUTH），**摘要完整可讀，五條準則逐字在摘要內**。
  ⚠ **與 C 組的交叉核對**：C 組把 Galsky 準則記在 Lancet Oncol 2011;12(3):211–214（PMID 21376284，該筆摘要為空、
  標為 [C-F1]）。**兩篇是不同文獻**：C 組那一篇是 consensus definition 的短文，本組這一篇是 JCO 的 review，
  **其摘要本身就載有五條準則的完整文字**，因此本組走的是可直接引用原文的路徑。
  兩組取得的五條內容一致（ECOG PS 2、CrCl <60 mL/min、≥2 級聽力損失、≥2 級神經病變、NYHA Class III 心衰竭）。
- **[D-S12] PASS** De Santis M, Bellmunt J, Mead G, et al.
  *Randomized phase II/III trial assessing gemcitabine/carboplatin and methotrexate/carboplatin/vinblastine in patients
  with advanced urothelial cancer who are unfit for cisplatin-based chemotherapy: EORTC study 30986.*
  **J Clin Oncol. 2012;30(2):191–199.** DOI 10.1200/JCO.2011.37.3571｜PMID 22162575｜**非 OA**。
  Route: Europe PMC REST（TITLE）。摘要含：收案定義（GFR <60 但 >30 且／或 PS 2）、n=238、追蹤中位 4.5 年、
  最佳 ORR 41.2%(確認 36.1%)/30.3%(確認 21.0%) P=0.08、中位 OS 9.3/8.1 個月 P=0.64、
  嚴重急性毒性 9.3%/21.2%。
- **[D-S13] PASS** von der Maase H, Sengelov L, Roberts JT, et al.
  *Long-term survival results of a randomized trial comparing gemcitabine plus cisplatin, with methotrexate,
  vinblastine, doxorubicin, plus cisplatin in patients with bladder cancer.*
  **J Clin Oncol. 2005;23(21):4602–4608.** DOI 10.1200/JCO.2005.07.757｜PMID 16034041｜**非 OA**。
  Route: Europe PMC REST（EXT_ID）。摘要含 n=405、中位 OS 14.0/15.2 個月 HR 1.09(0.88–1.34) P=0.66、
  5 年 OS 13.0%/15.3%、有無內臟轉移 5 年 OS 6.8%/20.9%。
- **[D-S14] PASS** Sternberg CN, de Mulder P, Schornagel JH, et al.（EORTC Genito-Urinary Cancer Group）.
  *Seven year update of an EORTC phase III trial of high-dose intensity M-VAC chemotherapy and G-CSF versus classic
  M-VAC in advanced urothelial tract tumours.*
  **Eur J Cancer. 2006;42(1):50–54.** DOI 10.1016/j.ejca.2005.08.032｜PMID 16330205｜**非 OA**。
  Route: Europe PMC REST（TITLE）。摘要含 n=263、ORR 64%/50%、CR 21%/9% P=0.009、
  中位 PFS 9.5/8.1 個月、中位 OS 15.1/14.9 個月、2 年存活 36.7%/26.2%、5 年 21.8%/13.5%、死亡 HR 0.76。
- **[D-S15] PASS** **European Association of Urology (EAU). Guidelines on Muscle-invasive and Metastatic Bladder Cancer,
  Chapter "Metastatic Disease" (§9).**
  Route: `https://uroweb.org/guidelines/muscle-invasive-and-metastatic-bladder-cancer/chapter/metastatic-disease`，
  **2026-09-13 以 curl 實際抓取整頁 HTML（1,256,381 bytes）並轉純文字（46,288 字元）**，
  本 brief 引用之每一句均出自該純文字檔。
  **⚠ 該頁未標示版本年份**（頁面內文無 edition/year 字串）。→ **正文引用時寫「EAU 指引（uroweb.org 官方章節，
  2026-09-13 查閱）」，不得自行填上年份。** 書目另可並列非 OA 的期刊摘要版：
  van der Heijden AG, Bruins HM, Carrion A, et al. *European Association of Urology Guidelines on Muscle-invasive
  and Metastatic Bladder Cancer: Summary of the 2025 Guidelines.* **Eur Urol. 2025;87(5):582–600.**
  DOI 10.1016/j.eururo.2025.02.019｜PMID 40118736｜**非 OA（內文取不到，見 [D-F9]）**。
  用途：第一線／後線建議表全文與強度、cisplatin 不適合與「不適合任何鉑類」的定義、
  「CheckMate 901 included patients fit for cisplatin only」、「Thirty percent of the patients in the control arm
  received switch maintenance IO with avelumab」、EMA 的 PD-L1 門檻定義、sacituzumab govitecan 撤回的敘述、
  DESTINY-PanTumor02 膀胱世代 PFS/OS、disitamab vedotin 合併分析。
- **[D-S16] PASS** Powles T, Rosenberg JE, Sonpavde GP, et al. *Enfortumab Vedotin in Previously Treated Advanced
  Urothelial Carcinoma (EV-301).* **N Engl J Med. 2021;384(12):1125–1135.** DOI 10.1056/NEJMoa2035807｜PMID 33577729｜
  PMCID PMC8450892｜**非 OA**。NCT03474107。Route: Europe PMC REST（EXT_ID），可引用範圍限摘要。
- **[D-S17] PASS** Bellmunt J, de Wit R, Vaughn DJ, et al.（KEYNOTE-045 Investigators）.
  *Pembrolizumab as Second-Line Therapy for Advanced Urothelial Carcinoma.*
  **N Engl J Med. 2017;376(11):1015–1026.** DOI 10.1056/NEJMoa1613683｜PMID 28212060｜PMCID PMC5635424｜**非 OA**。
  NCT02256436。Route: Europe PMC REST（EXT_ID），可引用範圍限摘要。
- **[D-S18] PASS** Loriot Y, Matsubara N, Park SH, et al.（THOR Cohort 1 Investigators）.
  *Erdafitinib or Chemotherapy in Advanced or Metastatic Urothelial Carcinoma.*
  **N Engl J Med. 2023;389(21):1961–1971.** DOI 10.1056/NEJMoa2308849｜PMID 37870920｜**非 OA**。NCT03390504。
  Route: Europe PMC REST（EXT_ID）。摘要含 n=266、追蹤 15.9 個月、OS 12.1/7.8 HR 0.64(0.47–0.88) P=0.005、
  PFS 5.6/2.7 HR 0.58(0.44–0.78)、3–4 級治療相關不良事件 45.9%/46.4%、治療相關致死 0.7%/5.4%。
  **ORR 不在摘要內 → 改引 [D-S19]。**
- **[D-S19] PASS** Loriot Y, Triantos S, Deprince K, Siefker-Radtke AO.
  *Plain language summary of the THOR Cohort 1 study comparing treatment with erdafitinib or chemotherapy in advanced
  or metastatic urothelial cancer.* **Future Oncol. 2025;21(16):1985–1997.** DOI 10.1080/14796694.2025.2511589｜
  PMID 40539319｜PMCID PMC12218492｜**OA（CC BY-NC-ND）**。
  Route: Europe PMC REST ＋ `/PMC12218492/fullTextXML`，全文 7,377 字元已讀。
  用途：**ORR 45.6% vs 11.5%**、6 個月存活 85%／12 個月 51%、「化療組被允許轉換」的敘述。
- **[D-S20] PASS** Matsubara N, Miura Y, Nishiyama H, et al.
  *Phase 3 THOR Japanese subgroup analysis: erdafitinib in advanced or metastatic urothelial cancer and fibroblast
  growth factor receptor alterations.* **Int J Clin Oncol. 2024;29(10):1516–1527.** DOI 10.1007/s10147-024-02583-3｜
  PMID 39017806｜PMCID PMC11420312｜**OA**。Route: Europe PMC REST ＋ fullTextXML。
  用途：**THOR cohort 1 整體族群安全性表（erdafitinib N=135／化療 N=112）**——高磷酸鹽血症 78.5%(≥3 級 5.2%)、
  甲床分離 23.0%(≥3 級 5.9%)、甲脫落 20.0%、甲溝炎 11.9%、味覺異常 25.2%；
  因不良事件減量 68.9%／暫停 71.9%（化療 24.1%／31.3%）；
  日本次族群 n=27（14/13）之 OS 25.4/12.4、PFS 8.4/2.9、ORR 57.1%/15.4%；
  「early FGFR testing after diagnosis of mUC should be considered」原句；
  日本族群上泌尿道原發較多的敘述。
- **[D-S21] PASS** Siefker-Radtke AO, Matsubara N, Park SH, et al.（THOR cohort 2 investigators）.
  *Erdafitinib versus pembrolizumab in pretreated patients with advanced or metastatic urothelial cancer with select
  FGFR alterations: cohort 2 of the randomized phase III THOR trial.*
  **Ann Oncol. 2024;35(1):107–117.** DOI 10.1016/j.annonc.2023.10.003｜PMID 37871702｜**非 OA**。
  Route: Europe PMC REST（TITLE）。**摘要含全部可引數字**：n=175/176、中位追蹤 33 個月、
  OS 10.9/11.1 HR 1.18(0.92–1.51) P=0.18、PFS 4.4/2.7 HR 0.88(0.70–1.10)、
  ORR 40.0%/21.6%（相對風險 1.85，1.32–2.59）、中位 DOR 4.3/14.4 個月、≥1 個 3–4 級不良事件 64.7%/50.9%、
  不良事件致死 2.9%/6.9%，以及「Outcomes with pembrolizumab were better than assumed」原句。
- **[D-S22] PASS** U.S. FDA. **BALVERSA (erdafitinib) tablets, prescribing information.**
  Route: openFDA brand_name:"BALVERSA"，**effective_time 20251024**，spl id 41ec18e6-999d-f298-e063-6294a90aa2dc。
  用途：適應症（**FGFR3** only）與 Limitations of Use 逐字；5.1 眼部（CSR/RPED 22%、中位 46 天、104 人的處置分布、
  重新開始後 67% 復發、41% 仍在進行中、乾眼 26%、眼科追蹤頻率與檢查項目）；5.2 高磷酸鹽血症（藥理學效應、
  24% 用磷結合劑、飲食限制 600–800 mg/日、>7.0 mg/dL 的處置、血管鈣化 0.2%）；
  BLC3001（THOR）之停藥 21%／暫停 68%／減量 53% 與各別原因；
  **伴隨式診斷 QIAGEN therascreen FGFR RGQ RT-PCR Kit 與其涵蓋的突變／融合清單**；
  THOR 中 75% 由中央 PCR、25% 由當地 NGS 判定。
- **[D-S23] PASS** Meric-Bernstam F, Makker V, Oaknin A, et al.
  *Efficacy and Safety of Trastuzumab Deruxtecan in Patients With HER2-Expressing Solid Tumors: Primary Results From
  the DESTINY-PanTumor02 Phase II Trial.* **J Clin Oncol. 2024;42(1):47–58.** DOI 10.1200/JCO.23.02005｜
  PMID 37870536｜PMCID PMC10730032｜**OA**。NCT04482309。
  Route: Europe PMC REST ＋ `/PMC10730032/fullTextXML`（85,019 字元）。
  用途：全體 n=267、ORR 37.1%、≥3 級藥物相關不良事件 40.8%、判定藥物相關 ILD 10.5%（三死）；
  **膀胱世代 ORR 39.0%（24.2–55.5）試驗主持人評估、41.5%（26.3–57.9）中央判讀**；
  **中央確認 IHC 3+ 之膀胱世代 n=16、ORR 56.3%（29.9–80.2）**；
  **cohort 2 的定義原文（含腎盂、輸尿管、膀胱、尿道）**；
  **HER2 判讀採用胃癌 ASCO/CAP 準則的原文**。
- **[D-S24] PASS** Makker V, Lee JY, Oh DY, et al.
  *Post Hoc Analysis of the Phase II DESTINY-PanTumor02 Study: Local and Central HER2 IHC Concordance and Trastuzumab
  Deruxtecan Efficacy by HER2 IHC Status in HER2-Expressing Solid Tumors.*
  **Clin Cancer Res. 2026;32(13):2628–2636.** DOI 10.1158/1078-0432.CCR-25-4702｜PMID 41954657｜PMCID PMC13320193｜**OA**。
  Route: Europe PMC REST。摘要含：267 人、75.7% 依本地檢測收案、**一致率 IHC 3+ 58.6%、IHC 2+ 54.5%、合併 73.4%**，
  以及結論原句。
- **[D-S25] PASS** U.S. FDA. **ENHERTU (fam-trastuzumab deruxtecan-nxki) prescribing information.**
  Route: openFDA brand_name:"ENHERTU"，**effective_time 20260515**，set_id 7e67e73e-ddf4-4e4d-8b50-09d7514910b6。
  用途：泛腫瘤 HER2 IHC 3+ 適應症逐字＋**加速核准聲明逐字**；14.6 節（合併 192 人、三個試驗、
  DESTINY-PanTumor02 貢獻 111 位 IHC 3+、本地或中央判讀皆可、排除 ILD 病史與 ECOG >1）。
- **[D-S26] PASS** Nguyen NJ, Olkhov-Mitsel E, Craddock KJ, Flood TA, Downes MR.
  *Reflex somatic testing for the detection of FGFR alterations in urinary tract carcinomas: A dual-institutional
  experience.* **Am J Clin Pathol. 2025;164(6):861–869.** DOI 10.1093/ajcp/aqaf108｜PMID 41097827｜PMCID PMC12782305｜**OA**。
  Route: Europe PMC REST ＋ `/PMC12782305/fullTextXML`（47,201 字元）。
  用途：n=366（下泌尿道 239／上泌尿道 72／轉移 55）、任何 FGFR 變異 16.1%、可用藥變異 13.4%（FGFR3 突變 33／
  FGFR3 融合 13／FGFR2 突變 3）、**上 23.8% vs 下 13.8%（P=0.007）**、肺轉移 57.1% vs 其他 10.4%（P=0.002）、
  轉移 16.4% vs 原發 12.9%（P=0.482）、檢測平台（Oncomine Comprehensive Assay v3 DNA 與 OCA Plus RNA）、
  反射性檢測只做在轉移或 pT3/pT4。
- **[D-S27] PASS** Hara T, Tobe T, Ueki H, et al.
  *Prevalence and complementary distribution of FGFR3 alterations and ERBB2 amplification in metastatic urothelial
  carcinoma: a nationwide registry analysis.* **Int J Clin Oncol. 2026;31(9):2025–2032.** DOI 10.1007/s10147-026-03117-9｜
  PMID 42365196｜**非 OA**。Route: Europe PMC REST（EXT_ID），可引用範圍限摘要：
  日本 C-CAT 登記、FoundationOne、2019/01–2025/06、n=1,014；FGFR3 變異 157(15.5%)、ERBB2 擴增 150(14.8%)、
  同時具備 13(1.3%) 對預期 2.3%（P=0.010，粗 OR 0.47）；上泌尿道原發與 HER2 擴增較低相關（OR 0.57，0.39–0.84，P=0.005）。
- **[D-S28] PASS** Müller DC, Murtha AJ, Bacon JVW, et al.
  *Prospective multicenter study of ctDNA versus tumor tissue guiding FGFR-targeted therapy in metastatic urothelial cancer.*
  **Nat Commun. 2026;17(1):3263.** DOI 10.1038/s41467-026-69927-7｜PMID 41760649｜PMCID PMC13066519｜**OA**。
  Route: Europe PMC REST ＋ `/PMC13066519/fullTextXML`（62,652 字元）。
  用途：加拿大 12 中心、2021/01–2024/04、篩選 265／收案 244／可分析 208；FGFR 變異（組織或 ctDNA）26%；
  125 對配對中一致 90%、ctDNA 敏感度 84%、另外找到 7 例；**21 人實際用到 erdafitinib**（中位 PFS 7.5 個月、
  疾病控制率 67%、**6 人(29%) 因毒性停藥**、43% 是在第二線用）；一例組織有 FGFR3-TACC3 而 ctDNA 從未測到；
  **「Patients known to have no tissue available were not screened.」**；
  **「a qualitative RT-PCR tumor tissue test that detects nine recurrent FGFR alterations (4 hotspot mutations and
  5 fusions)」** 與 **「no internationally standardized testing approach exists」** 兩句原文。
- **[D-S29] PASS** **衛生福利部中央健康保險署，《全民健康保險藥品給付規定》（PDF，版眉標示「(115.8.21更新)」）。**
  Route: 2026-09-13 直接下載官方 PDF（6,961,027 bytes）→ `pdftotext -layout` 轉純文字（1,285,264 bytes）逐條比對。
  （另備份一份版眉「(115.4.23更新)」之舊版供對照，內容差異不影響本 brief 引用之條文。）
  **本 brief 引用之條文位置**：9.69 免疫檢查點抑制劑（含第 1(4) 泌尿道上皮癌 I／II／III、第 2(9) nivolumab 併 GC、
  第 3(2)III 腎功能、第 3(3) PD-L1 表格四列與平台註記、第 4 通則中 EV 第三線之例外文字）；
  9.109 Enfortumab vedotin（全條）；9.115 Trastuzumab deruxtecan（全條，乳癌二段）。
  **全文檔搜尋結果（零筆者逐項寫明）**：
  「erdafitinib」**0 筆**、「Balversa」**0 筆**、「盼樂」**0 筆**；
  「尿路上皮」**0 筆**（本規定一律用「**泌尿道上皮癌**」，共 16 筆）；
  「deruxtecan」7 筆（皆為乳癌條文或與其他藥擇一給付之條款，無泌尿道上皮癌）；
  「vedotin」7 筆（brentuximab／polatuzumab／enfortumab）；
  「sacituzumab」1 筆（乳癌，與 T-DXd 擇一給付）；「disitamab」**0 筆**。
- **[D-S30] PASS** **衛生福利部食品藥物管理署，「未註銷藥品許可證資料集」原始 CSV。**
  Route: 政府資料開放平臺 dataset 9123（`https://data.gov.tw/api/v2/rest/dataset/9123`，2026-09-13 取得 metadata，
  平台標示 modifiedDate 2026-08-31 07:41:19）→ 其 `resourceDownloadUrl`
  `https://data.fda.gov.tw/data/opendata/export/37/csv`（zip，3,787,543 bytes）→ 解壓為 `37_2.csv`（16,818,871 bytes，
  25,988 筆許可證），欄位含「許可證字號／中文品名／英文品名／適應症／發證日期／有效日期／註銷狀態／申請商名稱／異動日期」。
  **本 brief 引用之許可證**：
  ｜Padcev 備思復凍晶注射劑 20mg／30mg：**衛部菌疫輸字第001212號／第001213號**，發證 2022/12/28、有效 2027/12/28、
  異動 2026/05/08，申請商 台灣安斯泰來製藥股份有限公司｜
  Keytruda 吉舒達注射劑：**衛部菌疫輸字第001025號**，發證 2024/10/28、有效 2026/10/13、異動 2026/08/27，
  申請商 美商默沙東藥廠股份有限公司台灣分公司｜
  Bavencio 百穩益注射劑 20 毫克/毫升：**衛部菌疫輸字第001085號**，發證 2018/08/07、有效 2028/08/07、異動 2026/02/10，
  申請商 台灣默克股份有限公司｜
  Opdivo 保疾伏：**衛部菌疫輸字第001013號**，發證 2025/06/06、有效 2031/03/04、異動 2025/12/04，
  申請商 台灣小野藥品工業股份有限公司｜
  Balversa 盼樂膜衣錠 3／4／5 毫克：**衛部藥輸字第027912／027913／027914號**，發證 2020/07/10、有效 2030/07/10、
  異動 2025/10/16–20，申請商 嬌生股份有限公司｜
  Enhertu 優赫得凍晶注射劑 100 毫克：**衛部菌疫輸字第001179號**，發證 2026/04/23、有效 2026/12/07、異動 2026/05/20，
  申請商 台灣第一三共股份有限公司；另 達卓優凍晶注射劑 100 毫克 **衛部菌疫輸字第001302號**，發證 2025/11/10、
  有效 2030/11/10。
  **零筆結果**：全檔搜尋「disitamab」**0 筆**、「RC48」**0 筆**。
  ⚠ **註**：此檔僅為「未註銷」許可證快照，**不含適應症的歷次變更紀錄**；「異動日期」只說明最近一次異動，
  **不等於適應症變更的日期**。正文引用時只寫「截至 2026-09-13 的許可證登載適應症」，不得倒推核准時序。
- **[D-S31] PASS** Rosenberg JE, O'Donnell PH, Petrylak DP, et al.
  *EV-103 dose escalation/cohort A: 5-year follow-up of enfortumab vedotin plus pembrolizumab in previously untreated
  locally advanced/metastatic urothelial carcinoma.* **ESMO Open. 2026;11(6):107700.** DOI 10.1016/j.esmoop.2026.107700｜
  PMID 42155320｜PMCID PMC13213747｜**OA**。NCT03288545。Route: Europe PMC REST。
  摘要含 n=45、不適合 cisplatin、84.4% 有內臟疾病、55.6% 腎功能下降（CrCl <60）、中位追蹤 62.1 個月、
  ORR 73.3%、中位 DOR 22.1 個月、中位 PFS 12.7 個月、中位 OS 26.1 個月、**5 年存活率 41.5%（26.5–56.0）**。
- **[D-S32] PASS** U.S. FDA. **TRODELVY (sacituzumab govitecan-hziy) prescribing information.**
  Route: openFDA brand_name:"TRODELVY"，**effective_time 20260624**，set_id 57a597d2-03f0-472e-b148-016d7169169d。
  用途：**現行適應症全文只有三陰性乳癌與 HR+/HER2− 乳癌，無任何尿路上皮癌適應症**
  ——可用來支持「這個適應症已經不在仿單上了」，**但撤回的經過與原因一律引 [D-S15]**。
  **同一路徑另查 TECENTRIQ（atezolizumab）仿單適應症全文：「urothelial」零筆**，
  同樣只能寫「現行美國仿單上沒有這個適應症」，不得自行敘述撤回時序。
- **[D-S33] PASS（僅限台灣藥證適應症之歷史對照）** 財團法人醫藥品查驗中心（CDE）。
  **《備思復凍晶注射劑（Padcev Powder for concentrate for solution for infusion）醫療科技評估報告》，
  報告編號 112BTD06015_Padcev。** 衛生福利部中央健康保險署。
  Route: 2026-09-13 直接下載官方 PDF（1,925,542 bytes，76 頁）→ pdftotext 轉文字。
  用途：當年送審時的「主管機關許可適應症」與「建議健保給付之適應症內容／條件」原文
  （可用來說明健保 9.109 條的由來）。
  ⚠ **這是 2023 年的送審文件，其適應症敘述已被 [D-S30] 的現行許可證取代；引用時必須標明年份與「當時」。**
  站上既有文章〈三十年沒變的流程，今年動了〉的參考文獻 5 即為此報告。
- **[D-S34] PASS** **ClinicalTrials.gov 試驗狀態（全部 2026-09-13 以 `api/v2/studies/<NCT>` 查詢）**：
  ｜**NCT04223856（EV-302）** ACTIVE_NOT_RECRUITING，收案 886（實際），開始 2020-03-30，
  主要完成 2023-08-08，預計全試驗完成 2028-03-01，最後更新 2026-05-29｜
  **NCT02603432（JAVELIN Bladder 100）** COMPLETED，收案 700（實際），開始 2016-04-25，
  主要完成 2019-10-21，完成 2023-03-28，最後更新 2024-03-27｜
  **NCT03390504（THOR）** ACTIVE_NOT_RECRUITING，收案 629（實際，含 cohort 1＋2），開始 2018-03-23，
  主要完成 2024-04-15，預計完成 2026-12-31，最後更新 2026-07-06｜
  **NCT04482309（DESTINY-PanTumor02）** ACTIVE_NOT_RECRUITING，第二期，收案 477（實際），開始 2020-08-18，
  預計完成 2027-03-23，最後更新 2026-07-10｜
  **NCT03036098（CheckMate 901）** ACTIVE_NOT_RECRUITING，收案 1,314（實際，含未發表的 nivo＋ipi 組），
  開始 2017-03-24，主要完成 2024-08-30，完成 2026-05-15，最後更新 2026-03-06。
  ⚠ **CheckMate 901 的註冊收案數 1,314 與 NEJM 論文的 608 不同**——論文報的是
  「nivolumab＋GC vs GC」那一組；正文寫 n 時一律用 608 並註明是該組。

### FAIL / NOT-CITABLE（保留，讓寫作者知道查過什麼）

- **[D-F1] FAIL — nhi.gov.tw 網頁版條文頁。** `https://www.nhi.gov.tw/ch/np-1837-1.html` 回 **HTTP 403（Cloudflare）**，
  與 RESEARCH-COMMON 的預期一致。→ **改走直接 PDF 連結成功**（[D-S29]）；
  另 `info.nhi.gov.tw` 在 15:35 一度 `ws_closed_mid_exchange`，`data.nhi.gov.tw` 回 502（代理政策拒絕）。
- **[D-F2] FAIL — 食藥署「西藥、醫療器材、含藥化粧品許可證查詢」網頁介面。**
  `https://info.fda.gov.tw/MLMS/H0001.aspx` 與 `https://info.fda.gov.tw/` 經代理回 **502 connect_rejected**；
  WebFetch 回 `ROBOTS_DISALLOWED`。→ **改走政府資料開放平臺 dataset 9123 的原始 CSV，成功**（[D-S30]）。
- **[D-F3] FAIL — EV-302 的 NEJM 全文。** [D-S1] 非 OA、無可取得全文；
  **ORR、完全反應率、各項不良反應細目、AESI（皮膚反應／高血糖／周邊神經病變）在摘要裡看不到。**
  → 這些數字一律改引 **[D-S5]（FDA PADCEV 仿單，EV-302 專屬表格 Table 9／10／22）** 或 **[D-S3]／[D-S4]**。
  **不可寫「根據 NEJM 那篇，反應率 67.7%」——該數字不是從那篇摘要裡讀到的。**
- **[D-F4] 零筆 — Erdafitinib 的健保給付條文。**
  Route: [D-S29] 的《藥品給付規定》全文（115.8.21 更新）逐字搜尋
  「erdafitinib」／「Balversa」／「盼樂」／「FGFR」四組關鍵字。
  結果：前三組 **0 筆**；「FGFR」3 筆，逐筆檢視後確認**全部與尿路上皮癌無關**
  （5.5.8 vosoritide 用於軟骨發育不全症之 FGFR3 基因變異 1 筆；FGFR2 融合／重排之膽道癌條文 2 筆）。
  → **依 SPEC §四固定紅線與紅線 7：寫成「健保藥品給付規定全文查不到列項，要問醫務課／個管師」，
  永不推論有無給付，也不得推論自費金額。**
- **[D-F5] 零筆 — Trastuzumab deruxtecan 用於泌尿道上皮癌／泛腫瘤 HER2 的健保條文。**
  Route: [D-S29] 全文搜尋「deruxtecan」7 筆，逐筆檢視：9.115 為乳癌兩段，其餘 5 筆為乳癌條文中與
  trastuzumab emtansine／lapatinib／sacituzumab govitecan 擇一給付之條款。
  **泌尿道上皮癌或實體腫瘤泛適應症：0 筆。** → 同上，寫查不到列項。
- **[D-F6] 零筆 — EV＋pembrolizumab 第一線合併用法的健保條文。**
  Route: [D-S29] 全文搜尋「enfortumab」1 筆（9.69 通則中的第三線例外文字）＋9.109 全條逐字閱讀。
  **第一線、合併 pembrolizumab 的給付條文：0 筆。** → 寫查不到列項。
- **[D-F7] FAIL — 台灣自費金額（EV、pembrolizumab、erdafitinib、T-DXd）。**
  Route: 未取得任何可引之官方公告。→ **gap。依 SPEC §四固定紅線，媒體報導的價格一律不可引，
  自費金額只在查得到官方公告時引用並標日期。本專題 D 組：不寫任何金額。**
- **[D-F8] NOT-CITABLE — NCCN。** 依 SPEC §四與 RESEARCH-COMMON，本專題不引 NCCN。本組未嘗試抓取。
- **[D-F9] FAIL — 期刊版指引原文取不到。**
  ① van der Heijden AG, Bruins HM, Carrion A, et al. *EAU Guidelines on Muscle-invasive and Metastatic Bladder
  Cancer: Summary of the 2025 Guidelines.* **Eur Urol. 2025;87(5):582–600.** DOI 10.1016/j.eururo.2025.02.019｜
  PMID 40118736｜非 OA。
  ② *ESMO Clinical Practice Guideline interim update on first-line therapy in advanced urothelial carcinoma.*
  **Ann Oncol. 2024;35(6):485–490.** DOI 10.1016/j.annonc.2024.03.001｜PMID 38490358｜非 OA。
  Route: Europe PMC REST 皆命中書目但無全文、無 PMCID。
  → **書目可引，內文措辭不可引。指引措辭一律走 [D-S15]（uroweb.org 官方章節實際抓取）；
  ESMO 的措辭本組取不到，D1／D2 不得出現任何「ESMO 說……」的句子。**
- **[D-F10] FAIL — RC48-C016（disitamab vedotin 第三期）原始論文。**
  Route: Europe PMC 以 `TITLE:"disitamab vedotin" OR ABSTRACT:"RC48-C016"` 搜尋，命中者皆為中國的成本效益分析
  （BMJ Open 2026;16:e117595、Hum Vaccin Immunother 2026;22:2717970、Front Pharmacol 2026;16:1809459 等），
  **未命中主試驗報告**。→ disitamab vedotin 一律只引 [D-S15] 的 EAU 轉述（兩個第二期合併分析 n=107），
  並寫明台灣無藥證（[D-S30] 零筆）。**不得引用第三期的任何數字。**
- **[D-F11] FAIL — EMA 產品資訊（Padcev／Keytruda／Bavencio／Balversa／Enhertu 的 EPAR）。** 本組未抓取。
  → 歐洲端的敘述一律走 [D-S15] 的 EAU 原文（其中已含 EMA 核准狀態與 PD-L1 門檻定義），
  **不得自行敘述 EMA 的適應症文字。**
- **[D-F12] FAIL — 基因檢測的周轉時間（turnaround time）與台灣的檢測可及性。**
  Route: [D-S26]、[D-S28] 兩篇 OA 全文逐字搜尋「turnaround」「turn-around」「TAT」——**零筆**；
  健保支付標準檔（C 組 [C-S39]）本組未重複搜尋 FGFR／NGS 項目。
  → **gap。D2 不得寫任何檢測等待天數，寫成「要等報告，時間依實驗室而異，問主治醫師或個管師」。**
- **[D-F13] FAIL — CheckMate 901 全文。** `/webservices/rest/PMC12314471/fullTextXML` 回傳 **0 bytes**
  （該 PMC 紀錄為作者手稿，無 XML 全文）。→ 可引用範圍限 [D-S9] 摘要；
  「只收適合 cisplatin 者」與「對照組僅 9% 接受 avelumab 維持」兩句改引 [D-S15]。
- **[D-F14] FAIL — 台灣癌症登記的轉移性膀胱癌人數／期別分布。** 本組未查（屬 A／E 組範圍）；
  C 組已記錄 hpa.gov.tw TLS 失敗與 data.gov.tw dataset 6399 下載連結同樣失敗（[C-F4]）。
  → **D1／D2 不得出現任何台灣的發生數或期別比例。**
- **[D-F15] FAIL — 重大傷病項次逐字條文。** C 組已於 law.moj.gov.tw 逐一嘗試失敗（[C-F10]），本組未重複。
  → 寫「問醫務課／個管師」。

---

## 給編輯的三點回報（非正文）

1. **SPEC §五對 D1 的標題〈轉移之後的第一線變了〉在台灣健保現實裡需要一句限定。**
   建議在文章開頭或「台灣現況」小節寫明：變的是國際指引與台灣藥證，健保給付的第一線仍是鉑類化療
   （加上符合條件者的 avelumab 維持或 nivolumab 併 GC）。**這不需要改標題，但不能不寫。**
2. **SPEC §五對 D2 的 PD-L1 命題（「一個停止重要的生物標記」）需要改成三地並陳**（見 ⚠ 第 3 點）。
   改寫後它仍是好教材，而且更誠實。
3. **站上既有文章 `insight-bladder-ev-pembro` 有一處與台灣藥證不一致**（見 ⚠ 第 6 點）：
   FDA 2026-07 擴大到適合 cisplatin 的病人，但台灣藥證的術前術後適應症仍限「不適合 cisplatin」。
   本組不修改既有文章，列出供編輯在 §九或上線腳本階段決定要不要處理。
