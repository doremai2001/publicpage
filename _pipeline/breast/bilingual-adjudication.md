# 中英漂移最終判讀 / Bilingual drift adjudication

`check_bilingual.py /home/claude/breast/body /home/claude/breast/en`
→ 24 篇，**0 篇硬性不一致**（引用數／引用 URL 逐位置／參考條目／`<h4>` 數），**13 個比例待判讀**。

判讀結論：**13 個全部是誤報**，全部屬於同一類——英文 "percentage points" 被 checker 的
`PCT = (\d+(?:\.\d+)?)\s*(?:%|％|percent|per cent)` 樣式吃進 *percent*age，解析成比例；
中文的「N 個百分點」則完全沒有被 `proportions()` 捕捉，所以只在英文側出現。
**0 個真實漂移，未做任何編輯。**

每一項都逐句對照過中文原句，數字與單位皆完全一致。

---

## endocrine-years（4 項）

### 1. 比例 0.04

> **EN**: "…at a median follow-up of 6.3 years, 5-year disease-free survival was 95% against 91%, **a difference of 4 percentage points** (hazard ratio for recurrence or contralateral breast cancer 0.66, P=0.01…)"

> **ZH**: 「中位追蹤 6.3 年：5 年無病存活 95% 對 91%，**差 4 個百分點**（復發或對側乳癌風險比 0.66，P=0.01……）」

**判定：FALSE POSITIVE — "percentage points"。** 4 個百分點 = 4 percentage points，一致。

### 2. 比例 0.046

> **EN**: "…exemestane plus ovarian function suppression against tamoxifen plus ovarian function suppression gave an absolute improvement in 12-year disease-free survival of **4.6 percentage points** (hazard ratio 0.79, P<0.001)…"

> **ZH**: 「exemestane 加卵巢功能抑制對 tamoxifen 加卵巢功能抑制的 12 年無病存活絕對改善 **4.6 個百分點**（風險比 0.79，P<0.001）」

**判定：FALSE POSITIVE — "percentage points"。**

### 3. 比例 0.027 與 4. 比例 0.045（同一句）

> **EN**: "At a median follow-up of 55.4 months the invasive disease-free survival hazard ratio was 0.716 (0.618 to 0.829), with the absolute difference widening from **2.7 percentage points** at three years to **4.5 percentage points** at five…"

> **ZH**: 「中位追蹤 55.4 個月，無侵犯疾病存活風險比 0.716（0.618 到 0.829），絕對差距由三年的 **2.7 個百分點**擴大到五年的 **4.5 個百分點**」

**判定：兩項皆 FALSE POSITIVE — "percentage points"。** NATALEE 的族群標籤（hormone-receptor-positive、HER2-negative、stage IIA/IIB/III）在英文同段完整保留。

---

## genomic-chemo（2 項）

### 5. 比例 0.05 與 6. 比例 0.002（同一句）

> **EN**: "Within the hormone-receptor-positive/HER2-negative subgroup of 1,358, women aged 50 or under (464) had 8-year distant metastasis-free survival of 93.6% with chemotherapy against 88.6% without, **a difference of 5.0 percentage points** (95% confidence interval −0.5 to 10.4); women over 50 (894) had 90.2% against 90.0%, **a difference of 0.2 percentage points** (−4.0 to 4.4)."

> **ZH**: 「在荷爾蒙受體陽性／HER2 陰性的 1,358 人次群組裡，50 歲以下（464 人）8 年無遠端轉移存活是化療 93.6% 對不化療 88.6%，**差 5.0 個百分點**（95% 信賴區間 −0.5 到 10.4）；超過 50 歲（894 人）是 90.2% 對 90.0%，**差 0.2 個百分點**（−4.0 到 4.4）。」

**判定：兩項皆 FALSE POSITIVE — "percentage points"。** 亞型標籤與年齡分層在英文完整保留。

---

## her2-therapy（1 項）

### 7. 比例 0.018

> **EN**: "…taken apart, the node-positive subgroup was 92.0% against 90.2%, **a difference of 1.8 percentage points** (hazard ratio 0.77, 0.62 to 0.96, P=0.02); the node-negative subgroup was 97.5% against 98.4%…"

> **ZH**: 「拆開看，**淋巴結陽性**次群組是 92.0% 對 90.2%，**差 1.8 個百分點**（風險比 0.77，0.62 到 0.96，P=0.02）；**淋巴結陰性**次群組是 97.5% 對 98.4%……」

**判定：FALSE POSITIVE — "percentage points"。** 淋巴結狀態標籤在英文緊貼數字保留。

---

## neoadjuvant（2 項）

### 8. 比例 0.055

> **EN**: "The cost is on the next line: 15-year local recurrence was 21.4% with preoperative chemotherapy against 15.9% with postoperative chemotherapy, **an absolute increase of 5.5 percentage points** (95% confidence interval 2.4 to 8.6, rate ratio 1.37, 1.17 to 1.61, p=0.0001)."

> **ZH**: 「代價在下一行：15 年局部復發率術前化療 21.4% 對術後化療 15.9%，**絕對增加 5.5 個百分點**（95% 信賴區間 2.4 到 8.6，率比 1.37，1.17 到 1.61，p=0.0001）。」

（同一數字在後段被再次引用：EN "with those **5.5 percentage points** on the table at the same time" ／ ZH「同時要把上面那 **5.5 個百分點**放到桌上一起看」。）

**判定：FALSE POSITIVE — "percentage points"。**

### 9. 比例 0.047

> **EN**: "The final analysis at a median follow-up of 8.4 years: 7-year invasive disease-free survival 80.8% against 67.1% (a difference of 13.7 percentage points, hazard ratio 0.54) and 7-year overall survival 89.1% against 84.4% (**a difference of 4.7 percentage points**, hazard ratio 0.66, 0.51 to 0.87, P=0.003)…"

> **ZH**: 「中位追蹤 8.4 年的最終分析：7 年無侵犯疾病存活 80.8% 對 67.1%（差 13.7 個百分點，風險比 0.54），7 年整體存活 89.1% 對 84.4%（**差 4.7 個百分點**，風險比 0.66，0…）」

**判定：FALSE POSITIVE — "percentage points"。**

---

## rt-hypofx（3 項）

### 10. 比例 0.005

> **EN**: "The Canadian trial enrolled 1,234 women with clear margins and negative axillary nodes who had had breast-conserving surgery: ten-year local recurrence was 6.7% with twenty-five treatments and 6.2% with sixteen, **an absolute difference of 0.5 percentage points** (confidence interval −2.5 to 3.5)…"

> **ZH**: 「加拿大那個試驗收的是切緣乾淨、腋下淋巴結陰性、接受保留手術的女性 1,234 人，十年局部復發二十五次組 6.7%、十六次組 6.2%，**絕對差 0.5 個百分點**（信賴區間 −2.5 到 3.5）」

**判定：FALSE POSITIVE — "percentage points"。**

### 11. 比例 0.002

> **EN**: "The ten-year results published in 2025 covered 2,016 analysable women, median age 63, only 3% node-positive, median follow-up ten years: ipsilateral breast relapse was 2.8% with whole-breast and 3.0% with partial-breast treatment, **an absolute difference of 0.16 percentage points** (−1.28 to 2.89)."

> **ZH**: 「2,016 人可分析、中位年齡 63 歲、只有 3% 淋巴結陽性、中位追蹤十年：同側乳房復發全乳組 2.8%、部分乳房組 3.0%，**絕對差 0.16 個百分點**（−1.28 到 2.89）」

**判定：FALSE POSITIVE — "percentage points"。**（0.16 ÷ 100 四捨五入成 0.002。）

### 12. 比例 0.01

> **EN**: "NSABP B-39 enrolled 4,216 women: ten-year ipsilateral breast relapse was 4.6% with partial-breast and 3.9% with whole-breast treatment, and it did not meet the equivalence criterion set in advance; the authors' own conclusion supports whole-breast irradiation overall, but **the ten-year absolute difference is less than 1 percentage point**."

> **ZH**: 「NSABP B-39 收了 4,216 人，十年同側乳房復發部分乳房 4.6% 對全乳 3.9%，並沒有達到事先設定的等效標準；作者自己的結論是整體支持全乳照射，但**十年的絕對差小於 1 個百分點**。」

**判定：FALSE POSITIVE — "percentage points"。**

---

## rt-omission（1 項）

### 13. 比例 0.08

> **EN**: "CALGB 9343, at a median follow-up of 12.6 years: freedom from locoregional recurrence at ten years was 98% with radiotherapy and 90% with tamoxifen alone, **a difference of about 8 percentage points**."

> **ZH**: 「CALGB 9343 中位追蹤 12.6 年，十年無局部區域復發率放療組 98%、單用 tamoxifen 組 90%，**差約 8 個百分點**。」

**判定：FALSE POSITIVE — "percentage points"。**（同段前一句的「絕對差 8.6 個百分點」／"an absolute difference of 8.6 percentage points" 亦一致。）

---

## 附帶：`--show-numbers` 出現的 6 篇數字差異

這些不是硬性不一致（不加 `--show-numbers` 時全部為 ✓），逐項確認後全部是中英書寫慣例差異，**無一為漂移**：

| 篇 | 差異 | 原因 |
| --- | --- | --- |
| bone-health | en-only `40` | ZH「1.42 代表快了**四成**」→ EN "1.42 means they occurred about **40%** faster"。**「成」正確譯為百分比**（誤報類別 3）。 |
| rt-regional | en-only `30` | ZH「不是『**少了三成**的人復發』」→ EN "not that '**30%** fewer people recurred'"。同上，誤報類別 3。 |
| fertility-young | en-only `70000`/`8000`；zh-only `7`/`8` 等 | ZH「7 萬元」「8 千元」→ EN "NT$70,000"、"NT$8,000"；日期「11 月 6 日」→ "6 November"。 |
| first-month | en-only `2022`/`2025`/`2026`/`40`/`100`；zh-only `4000` 等 | 民國年換算（115 年 → 2026、111 年 → 2022、114 年 → 2025）；「4,000 萬元」→ "NT$40 million"；「每十萬」→ "per 100,000"。 |
| followup-schedule | en-only `80` | ZH「順從度都**超過八成**」→ EN "Compliance … was over **80%**"。誤報類別 3。 |
| self-pay-and-trials | zh-only `11`/`17` | 日期「11 月 28 日」→ "28 November"；「**17 萬**那一筆」→ "the **NT$170,000** entry"。 |

---

# 亞型與族群標籤稽核 / Subtype-and-population label audit

## 方法

不採抽樣，改為全量機械稽核 + 人工判讀，覆蓋範圍遠超過「每篇 5 個數字」的要求：

1. 以 `<h4>`／`<p>`／`<li>`／`<blockquote>` 為單位，把中英兩版逐段對齊（24 篇的段數兩版完全相同）。
2. **標籤稽核**：對每一個含數字的段落，比對 14 組亞型／族群概念在兩版出現的次數——
   `HR+`、`HER2+`、`HER2−`、`triple-negative`、`HER2-low`、`node-positive`、`node-negative`、
   `premenopausal`、`postmenopausal`、`metastatic/advanced`、`early`、`BRCA`、`luminal`、`line of therapy`。
3. **數字稽核**：對每一個對齊段落比對數字多重集合，抓數字被改動、遺漏或搬到別段的情形。
4. 兩項稽核共產生 50 + 45 = 95 個候選差異，**逐一人工開句對照**。

實際受檢的數字遠超過 120（24 篇 × 5）：所有 24 篇中每一個帶數字的段落都進了比對。

## 結果

**掉標籤：0。弱化標籤：0。標籤脫離數字：0。未做任何編輯。**

95 個候選差異全部是正規表示式的字面差異，語意上兩版一致：

* **「停經前／後」寫法**：ZH「停經前後合計」→ EN "pre- and postmenopausal combined"（bone-health [5]）；
  ZH「芳香環轉化酶抑制劑用於停經後（或合併卵巢功能抑制的停經前），tamoxifen 停經前後都可用」→
  EN "aromatase inhibitors are used after the menopause (or before it in combination with ovarian function suppression), and tamoxifen can be used either side of the menopause"（endocrine-side-effects [4]）。語意完全對應。
* **淋巴結標籤的同義表達**：ZH「淋巴結轉移」→ EN "nodal metastasis"／"axillary nodal metastasis"
  （endocrine-years [11]、her2-therapy [20][21]、neoadjuvant [16]、germline-brca [18]）。全部保留。
* **數字寫成英文字**：EN "Two hundred and seven women"（rt-omission [12]）、"Ten days, eighteen days"（germline-brca [12]）、
  "Forty-two is a very small sample"（fertility-young [13]）、"one to three positive nodes"（which-lines-matter [3]、rt-hypofx [2][4]、rt-regional [6]）。
* **日期與金額換算**：民國年 → 西元年、萬／千 → NT$ 數字、中文月份 → 英文月份。

英文在若干處反而比中文更外顯，未見任何一處把標籤壓縮掉。例如：

* rt-hypofx [8]：ZH「這一整段談的都是荷爾蒙受體多為陽性、早期、淋巴結陰性為主的族群，三陰性與 HER2 陽性不在裡面」→
  EN "Everything in this section concerns a population that is mostly hormone-receptor-positive, early and largely node-negative; triple-negative and HER2-positive disease is not in it."
* followup-schedule [17]：EN 保留了「同樣是 ER 陽性，不標 T 和 N 的復發率等於沒有講」這句方法學警語，
  且六格風險的 T1N0 13% / T2N4–9 41% 兩端數字與標籤都貼著。
* metastatic-genomics [6]：依亞型分開的 63%（HR+/HER2−, n=344）、38%（HER2+, n=42）、25%（TNBC, n=95）三組
  在英文全部帶著亞型與 n。
* metastatic-genomics [18]：DESTINY-Breast04 的 494/557（88.7%）hormone-receptor-positive 與 DESTINY-Breast06 的
  chemotherapy-naive 前置條件在英文都在同一句內。
* sentinel-node [11]：SOUND 的 87.8% ER-positive/HER2-negative 保留。
* metastatic-outlook [9]：MONALEESA-2 postmenopausal、MONALEESA-3 first/second line、MONALEESA-7
  premenopausal or perimenopausal 三個族群標籤逐一保留。

---

# 紅線抽查 / Red-line spot-checks

| 項目 | 結果 |
| --- | --- |
| **genomic-chemo**：HR 陽性、HER2 陰性適格句在英文版早段且與中文一樣直白 | **通過。** 第 3 段（第一個 `<h4>`「First, check whether this test was designed for you at all」之下的第一段）："not one of these multigene assays is recommended for treatment decisions in HER2-positive or triple-negative breast cancer. If your report says HER2-positive, or if ER, PR and HER2 are all negative, then none of the numbers below are yours"。下一段接 ASCO 的細部適格（postmenopausal / over 50、early-stage ER-positive/HER2-negative、node-negative or 1–3 positive nodes；premenopausal 只有 Oncotype DX 且限 node-negative；4 顆以上無資料）。與中文逐項對應，無軟化。 |
| **metastatic-genomics**：「這一整篇談的都是轉移性乳癌」在英文靠近開頭 | **通過。** 第 1 段（首段）："One thing has to be settled first: this entire article is about metastatic breast cancer. If your notes say stage I to III and the aim is to cure it, this is not your subject"。位置與中文相同。 |
| **metastatic-genomics**：「驗不到靶」未被寫成壞消息或檢測失敗 | **通過。** "Finding no usable target is a common result. **It is not bad news, and it is not a failed test.** All it means is this: the few positions that a drug can be aimed at happen not to be on your tumour, and treatment carries on along the road it was already following."（對應 ZH「它不是壞消息，也不是檢測失敗」）。文末行動清單再次強化："No usable target on the report makes that a day on which the information is complete, not a day on which something failed"。 |
| **rt-omission**：EUROPA 結果未被軟化 | **通過。** 方向與數字完整："an adjusted between-group difference of 6.39 (0.14–12.65, p=0.045), **with the direction favouring radiotherapy**; treatment-related adverse events were 67% in the radiotherapy group and 85% in the endocrine group"，並保留了緊接其後的反向警告 "This result cannot be turned round and read as 'radiotherapy is better than tablets'" 以及共同主要指標未報告、仍在收案的但書。 |
| **rt-omission**：「每一個省略試驗都預設持續內分泌治療」 | **通過。** 整個 `<h4>`「Every one of these trials rests on the same assumption」小節保留，四個試驗逐一列出（CALGB 9343 both arms、PRIME II all on adjuvant ET、LUMINA required、IDEA 寫進收案條件），並保留 8,769 人 / 49% 的真實世界數字與 "**Every trial of omitting radiotherapy assumes you are one of that 49%.**" |
| **chemo-side-effects**：abemaciclib 靜脈血栓栓塞條目帶當天動作 | **通過。** "swelling and pain in one calf, or sudden chest pain or breathlessness, which is what venous thrombosis and pulmonary embolism look like; abemaciclib's label lists venous thromboembolism among its warnings, and **if any of these appears do not wait for tomorrow's clinic**"。 |
| **chemo-side-effects**：T-DM1 間質性肺病條目帶當天動作 | **通過。** "a new dry cough, breathlessness after walking a short distance, a slight fever — the T-DM1 label lists interstitial lung disease too, and **if these appear do not wait for the next appointment** — this one cannot be told apart from radiation pneumonitis by its symptoms, and **not being able to tell them apart is the reason to phone, not the reason to watch and wait**."（T-DXd 段另有獨立的 "means contacting the treatment team the same day"。） |

---

# 編輯與驗證

**未做任何編輯。** 沒有引用編號、參考條目、作者、年份、期刊、卷期頁、DOI 或 URL 被觸碰；
沒有小節或結構被更動。

```
python3 check_article_html.py en/*.html --lang en --min 1100 --max 2100
→ 24 個檔案，0 個錯誤，0 個提醒。

python3 check_bilingual.py /home/claude/breast/body /home/claude/breast/en
→ 24 篇。0 篇硬性不一致（引用／條目／小節），13 個比例待判讀。
```

13 個比例旗標維持不變是**預期結果**：它們是 checker 樣式本身的假陽性
（`percent` 匹配到 *percent*age points），不是內容問題。修掉它們只能靠改 checker
——在 `PCT` 加上 `(?!age)` 這類負向前瞻——而不是改文章。中文原文為準，英文與其一致。
