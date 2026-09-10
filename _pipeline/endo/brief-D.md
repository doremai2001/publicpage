# Brief D — 子宮內膜癌專題「結束之後」群（D1–D4）

研究員：Group D｜查證日期：2026-09-10
期刊書目資料全部經 Europe PMC REST（`/webservices/rest/search?query=EXT_ID:<PMID>&resultType=core`）逐筆核對，含 DOI、卷期頁、isOpenAccess；
指引原文引語出自 ESGO 官方 PDF（guidelines.esgo.org，實際 curl 下載 + `pdftotext -layout`）與 Europe PMC 全文 XML；台灣官方條文全部實際下載原始檔逐字檢索。
引用規則：**只有標 PASS 的來源可以進正文。** FAIL / NOT-CITABLE 條目保留不刪。
本 brief 來源編號 **[D-S1]…[D-S77]**，與 A/B/C 組編號空間分開。

站上指路檔名已 `ls` 確認存在（含現行標題）：
`bc-lymphoedema.html`〈手腫起來：淋巴水腫的真實機率〉、`sit-markers.html`〈指標上升，不等於病在長〉、
`cx-dilator-sex.html`〈擴張器、性生活——沒人願意先開口的那題〉、`care-fear.html`〈療程結束了，為什麼更怕了〉、
`sit-oligomet.html`〈打掉那兩三顆，然後呢〉、`sit-reirradiation.html`〈照過的地方，能不能再照〉、
`sit-paperwork.html`〈重大傷病之外還能辦什麼〉、`care-thrombosis.html`〈小腿腫起來，可以等到明天嗎〉、
`care-fever.html`〈這一種發燒，不能等到天亮〉。

---

## ⚠ 與 SPEC 假設不同形狀的事（動筆前必讀，八條）

1. **SPEC 要「追蹤頻次的指引原文（ESGO/ESTRO/ESP、SGO、ESMO）依風險分組的間隔」——最新的 ESGO 指引根本不給間隔表。**
   ESGO-ESTRO-ESP **2025 更新版**（Lancet Oncol 2025;26:e423–e435）的 Follow-up 段落只有四句建議，全部是 **V, A**（最低證據等級），
   逐字包含這一句：「**there is no evidence that follow-up visits improve overall survival (V, A)**」，並要求
   「**A personalised follow-up approach to individual factors … is recommended (V, A)**」[D-S1]。
   附錄的證據摘要更直接：「**The only randomised data on follow-up in EC patients are derived from the TOTEM trial, which showed that
   an intensified follow-up does not improve OS, not even in high-risk patients. Gynecological examination including vaginal ultrasound
   can be considered to detect local recurrence. Other imaging techniques are not indicated in asymptomatic patients.**」[D-S2]
   → **D1 的骨架不能是「幾個月回診一次」的表格**，要寫成「這件事目前沒有證據支持任何一種頻次比另一種好；有數字的那個指引（SEOM-GEICO 2025）
   自己把等級標成 V, C」。有明確間隔可引的是 **SEOM-GEICO 2025**[D-S3]（低風險：前 2 年每 6 個月、之後每年到滿 5 年，**V, C**；
   高風險：前 2 年每 3 個月、之後每 6 個月到滿 5 年，**V, C**）。NCCN 依規則不引。

2. **「例行影像與腫瘤標記的證據等級（弱）」比 SPEC 寫的還要弱——SEOM-GEICO 2025 給的是最強等級的「不建議」。**
   逐字：「**Serum biomarkers are not recommended, and vaginal cytology is not routinely recommended, as most vaginal recurrences are
   detected with clinical examination alone [I, A]. There is very little evidence on the benefit of imaging tests as part of EC follow-up.**」[D-S3]
   注意這個 **[I, A]** 是「不要做」方向的強建議，不是「證據弱所以隨便」。寫作者不可把它稀釋成「證據不足，看醫師決定」。

3. **紅線 9 的正面數字，主力不是 PORTEC-1，是 GOG-0238。**
   PORTEC-1 的救援結果[D-S21] 分母很小（39 位孤立陰道復發、35 位以根治意圖治療），且它的「3 年存活 73%／5 年 65%」是
   **1990 年代、無影像導引近接治療**的年代數字。真正可以拿來給病人的當代分母是 **GOG-0238（Klopp 2024 JCO，n=165 隨機，86% 復發侷限於陰道、
   82% 低惡性度類內膜）：3 年無惡化存活單純放療 73%、化放療 62%，HR 1.25（95% CI 0.75–2.07），加化療不但沒有更好、急性毒性更高**[D-S22]。
   → **fig-em-recurrence 的「陰道頂端」格子應該用 GOG-0238 的 73%，PORTEC-1 當歷史對照。**
   而且 GOG-0238 附帶一個 SPEC 沒預期的訊息：**這個情境「加化療」是失敗的介入**，D2 要寫。

4. **「陰道頂端復發可以救」的分母比想像中更小，因為孤立陰道復發本身很少見。**
   MSK＋MD Anderson 兩中心、2009–2017、**2009 FIGO 第 1 期 n=2,815**：總復發 278 人（10%），其中**孤立陰道復發只有 61 人（佔全體 2%）**，
   42 人（69%）在陰道頂端；陰道外復發 217 人（8%）。做過輔助陰道近接治療的 960 人中，孤立陰道復發 19 人（2%）[D-S14]。
   → 「復發＝末期」要破，但「陰道頂端復發是可救的那一種」也**只佔第 1 期病人的 2%**——兩個方向的分母都要給。

5. **下肢淋巴水腫的發生率不是一個數字，是一個 1.3% 到 49% 的區間，而區間的寬度主要來自「怎麼定義」不是「做了什麼」。**
   同一件事：Geppert 2018（ICG 前哨 vs 全面廓清，臨床判定）**1.3% vs 18.1%**[D-S38]；
   Leitao 2020（MSK，13 題自填問卷，n=599）**27% vs 41%**[D-S36]；Glaser 2021（Mayo，同一份問卷，n=378）**26.0% vs 49.4%**[D-S37]；
   Casarin 2025（n=239）**21.4% vs 44.6%**[D-S39]；Bjørnholt 2025（丹麥全國，n=486，EORTC QLQ-EN24 分數差）**低惡性度做前哨者
   12 個月平均分數只上升 5.0 分，低於 8 分的臨床顯著門檻**[D-S40]。
   最關鍵的一篇是 Wedin 2021（瑞典 14 院前瞻，n=235，**同一批人同時用四種方法判定**）：
   **「Apparent risk factors for lymphedema differed considerably depending on the method used to determine lymphedema.」**
   ——淋巴廓清在「BMI 標準化體積」下 aOR 14.42、在「臨床分級」下只有 2.11、在「原始體積」下**完全看不出來**；
   輔助放療只有在 BMI 標準化體積這一種方法下才是風險因子（aOR 15.02）[D-S43]。
   → **D3 不可以寫成「機率是 X%」。要先寫「這個數字取決於誰在量、怎麼量」，再給區間與各自的定義。**
   （與 A 組 [A-Sn] 若有數字差異：本組獨立重查，取的是同一批原文，**Leitao/Glaser/Geppert 三筆數字若 A 組不同，以各自標註的判定方法為準，不要求一致**。）

6. **台灣健保確實有一個「徒手淋巴引流」的診療項目，但它的適應症把治癒後的病人排除在外——這是 D3 台灣段的主場。**
   **47091B「淋巴水腫照護-徒手淋巴引流(須達四十分鐘)」，450 點**，備註逐字：
   「**1.適應症：癌症末期淋巴水腫病人 2.執行人員：須接受淋巴照護相關訓練。執行完成後需有適應症、執行過程及執行時間的紀錄。3.提升兒童加成項目。**」[D-S72]
   → 一個第 1 期內膜癌、手術做完、腿腫的人，**依這條條文的字面適應症不在給付範圍內**。
   文章只能逐字引條文並寫「這一條寫的是癌症末期，實際能不能申報請問醫務課／個管師」，**不可推論**。
   同一份全表（6,013 項，1140501 生效版）**逐字檢索「壓力衣」「彈性襪」「氣壓」（僅見最大吸氣壓、氣壓式眼壓測定兩項無關項目）
   「淋巴水腫」除 47091B 外零筆**[D-S72]。

7. **壓力衣／彈性襪在「身心障礙者輔具費用補助基準表」裡也查不到。**
   《身心障礙者輔具費用補助辦法》附表（法規名稱與附表全文皆自全國法規資料庫下載，751,186 bytes、4,584 行）
   **逐字檢索「壓力衣」「彈性衣」「彈性襪」「淋巴」「水腫」全部零筆**[D-S77]。
   → 「壓力衣有沒有補助」這題的正確寫法是「這兩份官方文件裡我查不到列項」，**不是「沒有給付」**。

8. **心血管與代謝共病確實是這個族群的主要死因之一，但「內膜癌病人的心血管死亡率比一般人高」這句話有反方向資料，不能直接寫。**
   SEER 135,831 人：追蹤期間 46,604 人死亡（34.3%），死因分布 **內膜癌 42.9%、其他癌症 15.6%、非癌症 41.5%**；
   非癌症死因以心臟病、腦血管疾病、糖尿病為首；對比美國一般人口的標準化死亡比 **心臟病 SMR 1.06（1.03–1.09）、糖尿病 1.56（1.47–1.65）、
   敗血症 1.40（1.28–1.52）**[D-S57]。**罹病端**（不是死亡端）的訊號更強：SEER-Medicare 44,386 人 vs 221,219 對照，
   缺血性心臟病 HR 1.73、肺源性心臟病 HR 1.95、**靜脈與淋巴系統疾病 HR 2.71**[D-S58]；猶他州 2,648 人 vs 10,503 對照，
   1–5 年血栓性靜脈炎與栓塞 HR 2.07[D-S59]。
   **反方向**：Iowa Women's Health Study 以年齡與 BMI 配對，內膜癌組的**心血管死亡率反而較低**（HR 0.75，95% CI 0.56–0.99），
   全因死亡率則較高（HR 1.50）[D-S60]。
   → D4 可寫「非癌症死因佔了一半」「心血管與代謝共病是要顧的」，**不可寫「內膜癌讓你更容易死於心臟病」**。

---

## D1 `em-followup`〈追蹤怎麼排，該注意什麼〉

### Key facts

**(a) 指引怎麼寫追蹤（原文並陳，注意證據等級）**

- **ESGO-ESTRO-ESP 2025**[D-S1]（Lancet Oncol 2025;26:e423–e435）Follow-up 全段只有這些，逐字：
  > 「Patients with endometrial carcinoma should be actively informed and counselled about their follow-up (including programmes for
  > long-term survivorship; **V, A**). Patients should be informed about the signs and symptoms of endometrial carcinoma recurrence and
  > long-term side-effects of medical interventions (**V, A**). Patients with endometrial carcinoma should be informed that the primary
  > objectives of follow-up include psychosocial assistance and the detection of health problems, but that **there is no evidence that
  > follow-up visits improve overall survival (V, A)**. A personalised follow-up approach to individual factors, such as prognostic factors
  > (eg, molecular classification), applied treatment modalities, potential acute and long-term side-effects, comorbidities, and the
  > patients' needs is recommended (**V, A**). Follow-up should include assessment of physical (eg, **cardiovascular comorbidities and
  > secondary cancers**) and mental health (**V, A**).」
  → **這一段沒有任何一個月份數字。** 這件事本身就是 D1 最誠實的開場。
- **ESGO 2025 附錄**[D-S2]逐字：「The only randomised data on follow-up in EC patients are derived from the TOTEM trial, which showed that
  an intensified follow-up does not improve OS, not even in high-risk patients. Gynecological examination including vaginal ultrasound can be
  considered to detect local recurrence. **Other imaging techniques are not indicated in asymptomatic patients.**」
- **SEOM-GEICO 2025**[D-S3]（Clin Transl Oncol 2025;27:4368–4380，OA）給了唯一可引的具體間隔，逐字：
  > 「In low-risk patients, surveillance with physical and gynecological examinations is recommended **every 6 months for the first 2 years,
  > and then annually until completing 5 years** of recurrence-free follow-up **V, C**」
  > 「For high-risk groups, surveillance with physical and gynecological examinations are recommended **every 3 months for the first 2 years,
  > and then every 6 months until completing 5 years** of recurrence-free follow-up **V, C**」
  > 「A CT scan or PET-CT may be considered for the evaluation of a suspected recurrence **V, C**」
  正文另有一句：「**Serum biomarkers are not recommended, and vaginal cytology is not routinely recommended, as most vaginal recurrences are
  detected with clinical examination alone [I, A].**」與「There is very little evidence on the benefit of imaging tests as part of EC follow-up.」
  以及例外條款：「in high-risk non-endometrioid or FIGO III-IV tumors, imaging may be helpful, with **chest/abdominal/pelvic CT recommended
  every 6 months during the first 3 years, and every 6 to 12 months for 2 additional years [IV, A]**」；
  滿 5 年之後：「It seems reasonable for patients to return to annual population-based general physical and pelvic examinations after five years
  of recurrence-free follow-up [V, B]」。
- **SGO 2026 臨床實務聲明**[D-S4]（Salani, Gynecol Oncol 2026;204:109–117；**只有摘要可取得**）逐字可引：
  「the evidence for surveillance recommendations is weak and often based on retrospective studies, resulting in wide variability in clinical
  practice」「**symptom review and physical examination are reportedly the most effective methods to detect recurrence across gynecologic
  tumor types**」「tests such as **vaginal cytology, which have negligible benefit in recurrence detection, are still frequently utilized**」
  「**imaging is often routinely used without proven benefit; however … imaging may play a role in specific settings**」
  「incorporating novel serum biomarkers and emerging tests, such as **ctDNA, requires additional studies**」。
  2017 版[D-S5]同方向：「**There is very little evidence that routine cytology or imaging improves the ability to detect gynecologic cancer
  recurrence that will impact cure or response rates to salvage therapy.**」

**(b) 唯一的隨機證據：TOTEM**[D-S7]（Zola 2022, J Clin Oncol 40:3817–3827）

- 42 家醫院（義大利＋法國），**n=1,871 隨機、1,847 可分析（98.7%），60% 低風險**，FIGO I–IV 手術後完全緩解者，1:1 分派密集追蹤 vs 極簡追蹤。
- 中位追蹤 69 個月。**5 年總存活：密集 90.6% vs 極簡 91.9%（HR 1.13，95% CI 0.86–1.50，P=.380）**。
- 年齡、治療方式、復發風險、中心遵從度的次族群分析**都看不出差別**。
- 偵測到復發的機率**密集組略高但無統計意義**（HR 1.17，95% CI 0.92–1.48，P=.194）。
- 作者結論逐字：「An INT follow-up in endometrial cancer-treated patients does not improve OS, even in high-risk patients. According to
  available evidence, **there is no need to routinely add vaginal cytology, laboratory, or imaging investigations to the MIN regimens used in this trial.**」
- 兩組實際內容（由 SEOM-GEICO 轉述[D-S3]）：低風險組＝每 6 個月臨床檢查 vs 每年臨床檢查＋每年陰道細胞學＋CT；
  高風險組＝每 4 個月臨床檢查＋每年 CT vs 每 4 個月臨床檢查與超音波＋每年陰道細胞學＋CT。**整體復發率 12.3%。**

**(c) 復發多在何時、多少比例是「有症狀」被發現的（每一筆帶分母，方向不一致，必須並列）**

| 研究 | 族群與分母 | 復發率 | 時間分布 | 偵測方式 |
|---|---|---|---|---|
| Lubrano 2021[D-S9]（西班牙，2005–2014） | 全期別，復發 81 人（佔 10.04%） | 10.04% | **2 年內 66.7%、3 年內 80.2%** | **症狀＋理學檢查 54.3%**、血清標記 29.6%、CT 9.9%、陰道細胞學 6.2%；**42% 有症狀**；有症狀 vs 無症狀**總存活無差異** |
| Nakamura 2022[D-S10]（日本，n=847，密集追蹤：前 2 年每 1–3 個月抹片＋腫瘤標記、每 6–12 個月影像） | 復發 88 人 | 10.4% | — | **75% 的復發者是無症狀被查出來的**；多變項分析只有「局部復發」與存活相關；遠端轉移者有無症狀對存活**無差異**。作者結論：「an intensive surveillance protocol did not benefit patients」 |
| Knox 2025[D-S11]（澳洲兩中心，接受**輔助放療**者 n=264，中位追蹤 34 個月） | 復發 41 人（15.5%） | 15.5% | — | **只有 4 人是孤立局部復發**；**只有 3 人（佔全體 1.1%）是無症狀在內診時被發現**，其中**只有 1 人（0.4%）進到救援治療**。作者主張放療後族群可省略例行內診 |
| Ulusoy 2025[D-S12]（土耳其，第 1–2 期類內膜，n=303，追蹤 ≥2 年） | 復發 17 人（5.61%） | 5.61% | **前 23 個月累積 3.06%，前 33 個月 7.52%；25 個月後上升** | 理學檢查敏感度 50.00%、特異度 99.52%、PPV 88.89%、NPV 96.30% |
| Sadeghi 2025[D-S13]（英國，**低惡性度**，FIGO 2009 I–IV，n=238，近 10 年追蹤） | 復發 14 人（5.88%），其中 11 人（78.5%）原本是第 1 期 | 5.88% | **中位 30 個月** | 復發部位：**陰道頂端 42%**，其次骨盆淋巴結與遠端 |
| Rios-Doria 2023[D-S14]（MSK＋MDACC，2009 FIGO 第 1 期，n=2,815） | 復發 278 人（10%）；**孤立陰道復發 61 人（2%）**、陰道外 217 人（8%） | 10% | **孤立陰道復發中位 11 個月（1–68）；陰道外中位 20 個月（1–98），P<.004** | 孤立陰道復發 69% 在陰道頂端；曾做輔助陰道近接治療者（n=960）孤立陰道復發 19 人（2%），84% 在頂端 |
| Lantsman 2024[D-S15]（單一學術中心，**高風險**內膜癌 n=229） | 復發 63 人（28%） | 28% | — | **例行影像先發現 31 人（49.2%）**、症狀追蹤 24 人（38.15%）；最常見復發部位是**肺**；復發後平均存活影像組 2.0 年 vs 非影像組 1.6 年，**無統計差異** |

> **寫法要求**：這張表的方向**不一致**（Nakamura 75% 無症狀、Lubrano 42% 有症狀、Knox 只有 1.1% 靠內診抓到）。
> 差異來自**追蹤有多密集**（做愈多檢查，愈多人被「無症狀」發現）與**族群風險**（Lantsman 是高風險，影像先發現的比例最高）。
> 這件事本身就是要寫的內容：**「無症狀被查出來」的比例是追蹤強度製造出來的，不是疾病本身的性質**——而 TOTEM 證明多查出來的那些人並沒有活比較久。

**(d) 陰道細胞學在追蹤的角色**

- **Watanabe 2025**[D-S8]（大阪單一醫院，2010–2019，**n=759**，日本仍普遍例行做）：復發 85 人（**11.2%**），其中含陰道成分者 20 人（23.5%）；
  單一部位復發最常見是**陰道 12 人（14.1%）與肺 11 人（12.9%）**。20 例陰道復發中，**14 例是靠症狀與婦科內診診斷；只有 1 例單靠陰道細胞學診斷**，
  而那一例在細胞學異常後 2 個月就出現肉眼可見病灶。作者結論：「monitoring critical symptoms and conducting careful gynecological examinations
  has been shown to be more important than cytological examinations」。
- 指引端：SEOM-GEICO 2025 **[I, A]** 不建議常規做[D-S3]；SGO 2026 說它「negligible benefit … still frequently utilized」[D-S4]；TOTEM 說不需要加[D-S7]。
- 現實端：677 位婦癌長期存活者（≥5 年）的國際調查中，**內膜癌存活者有 50.5% 回報仍在做 Pap 追蹤、28.9% 仍在驗 CA-125**[D-S71]
  （作者結論逐字：「Follow-up procedures that do not follow guidelines should be avoided.」）。

**(e) 例行 CT／PET 與 CA-125 在無症狀追蹤**

- 指引：ESGO 2025 附錄「Other imaging techniques are not indicated in asymptomatic patients」[D-S2]；
  SEOM「Serum biomarkers are not recommended … [I, A]」「very little evidence on the benefit of imaging tests」[D-S3]；
  SGO 2026「imaging is often routinely used without proven benefit」[D-S4]。
- 唯一有條件的例外（SEOM，等級 **IV, A**）：高風險非類內膜或 FIGO III–IV，胸腹骨盆 CT 前 3 年每 6 個月、再 2 年每 6–12 個月[D-S3]。
- 支持影像的最強觀察資料也只到這裡：Lantsman 2024 高風險族群中影像先發現 49.2% 的復發，但**復發後存活無統計差異**[D-S15]。
- **ctDNA**：SGO 2026 明說「requires additional studies」[D-S4]。**D1 不寫 ctDNA 的效能數字。**
- 腫瘤標記本身怎麼讀 → 一句指向站上 `sit-markers`〈指標上升，不等於病在長〉。

**(f) 第二原發癌（Lynch 族群另計，指向 C3）**

- **Kokts-Porietis 2024**[D-S16]（Alberta Endometrial Cancer Cohort，**n=533** 前瞻世代，中位追蹤 **16.7 年**，IQR 12.2–17.9）：
  **89 人（17%）發生第二原發癌**——「With **1 in 6 survivors** developing an SPC」。
  部位分布：**乳房 29%、大腸直腸 13%、肺 12%**。
  可修正因子：診斷前飲食升糖負荷（≥90.4 vs <90.4 g/day，sHR 1.71，95% CI 1.09–2.69）、存活早期年齡 ≥60（sHR 2.48）、
  **存活早期每週飲酒 ≥2 杯（sHR 3.81，95% CI 1.55–9.31）**；診斷前到存活早期**減少飲酒者風險下降（sHR 0.34，95% CI 0.14–0.82）**。
- **放療與第二原發癌**：Wang & Cai 2024[D-S17]（SEER 8 registry，**n=62,108**，放療 16,846 vs 未放療 45,262，30 年追蹤）：
  第二原發癌累積發生率 **20.9% vs 19.7%**；輔助放療與**大腸直腸癌 aHR 1.29（1.12–1.50）、肺與支氣管 1.27、外陰 1.72、膀胱 1.86、
  非何杰金氏淋巴瘤 1.37** 相關；**乳癌風險反而略低 aHR 0.89（0.80–0.98）**。大腸直腸與膀胱的相對風險**隨距診斷時間拉長而上升**。
- **反方向／規模感**：SEER 17 registry 匯總分析（女性 20–79 歲，2000–2022，1,537,182 人年）算出**非婦科第二原發癌整體標準化發生比僅 SIR 1.038
  （95% CI 1.023–1.053）**，超額絕對風險 4.31/10,000 人年；**≥120 個月後 SIR 0.960（0.935–0.986）**；作者自己說
  「These population-level estimates support age-specific burden reporting **but not individual risk prediction or surveillance thresholds**」——
  但**這是 preprint（Research Square, DOI 10.21203/rs.3.rs-10744519/v1），標 FAIL-3，不可引**。
- **可寫的結論形狀**：「第二原發癌不罕見（16.7 年追蹤下六個人有一個），最常見是乳房與大腸直腸；所以**該做的是回去做全國一般族群的癌症篩檢**，
  不是額外多做內膜癌的檢查。」ESGO 2025 逐字支持這個寫法：「**Cancer screening, medical follow-up, and vaccination programmes according to
  local guidelines should be recommended to all patients (V, A)**」[D-S1]。**Lynch 族群的篩檢建議一律指向 C3，D1 不重寫。**

### 反方向的資料（誠實必列）

- Lantsman 2024[D-S15]：高風險族群近半數復發是例行影像先抓到的，且復發後存活有偏向影像組的**非顯著**趨勢（2.0 vs 1.6 年）。這是目前「例行影像可能有用」最好的一筆，等級是回溯性單中心。
- Nakamura 2022[D-S10]：密集追蹤下 75% 復發者無症狀——「多做真的會多抓到」是事實，TOTEM 反駁的是「多抓到不等於活比較久」。
- 患者端偏好：風險分層／病人自主啟動追蹤（PIFU）在英國推行中，臨床端訪談顯示 COVID 加速了轉型，但**非英語族群與溝通困難者是障礙**[D-S20 相關文獻未取全文，不引具體數字]。

### Claim ceiling（D1）

- **可寫**：「唯一的隨機試驗（TOTEM，1,847 人）比較密集與極簡追蹤，5 年存活 90.6% vs 91.9%，看不出差別，高風險族群也一樣」；
  「最新的 ESGO 指引在追蹤這一段的所有建議都標 V（專家意見），並且明著寫『沒有證據顯示回診會延長總存活』」；
  「有數字的間隔建議（SEOM-GEICO 2025：低風險前 2 年每 6 個月、高風險前 2 年每 3 個月，都到 5 年）本身是 V, C」；
  「陰道細胞學不建議常規做，這是 [I, A] 等級的『不要做』」；「例行 CT／PET／腫瘤標記在無症狀追蹤不被建議」；
  「復發大多在 3 年內（2 年內約 2/3、3 年內約 4/5）」；「多數陰道復發是靠症狀與內診發現的（759 人的世代中 20 例陰道復發只有 1 例單靠細胞學）」；
  「16.7 年追蹤下約六分之一的存活者會有第二原發癌，最常見乳房與大腸直腸——所以要回去做一般族群的癌症篩檢」。
- **不可寫**：
  - 「追蹤要每 X 個月一次」寫成事實或指令——只能寫「某某指引建議 X，等級是專家意見，實際排程由你的婦癌科醫師定」。
  - 「不用追蹤了」——ESGO 的四句建議都是 V, A **建議要做**，理由是心理社會支持、症狀教育、共病與第二原發癌，不是延長存活。
  - 「做 CT／驗 CA-125 比較保險」或「醫師沒幫我排 CT 是漏掉了」——這一句是本篇最大的傷害來源。
  - 「無症狀被查出來比較好」——Nakamura[D-S10]、Lubrano[D-S9] 都顯示有無症狀與存活無差異。
  - 任何 ctDNA 的效能數字。
  - Lynch 族群的篩檢頻次（歸 C3）。
  - 免疫治療、化療、分子分型的療效數字（歸 B5／B3／B4）。

### Caveats／safety notes（寫作者必寫）

- **症狀清單要具體且要寫「不用等回診」**。SEOM-GEICO 2025 的病人衛教清單逐字[D-S3]：
  「unexplained vaginal bleeding, detection of a mass, abdominal distension, persistent pain, fatigue, diarrhea, nausea or vomiting,
  persistent cough, **leg swelling**, or weight loss」。**陰道出血**是最重要的一項（多數陰道復發靠它與內診發現[D-S8]）。
- 「腿腫」同時是復發訊號、淋巴水腫訊號與深部靜脈栓塞訊號——**這裡一定要一句指向 `care-thrombosis`〈小腿腫起來，可以等到明天嗎〉**，
  並寫「單側、突然、痛，不能等」。
- 追蹤的門檻是現實問題：870 人的回溯顯示未達建議追蹤頻次者住得離癌症中心更遠（39.2 vs 20.7 英里，P=.026）、家戶所得中位數更低
  （$74,015 vs $80,435，P=.027）[D-S19]。這是拿來鼓勵「排不出時間就講出來、換一種追蹤方式」的素材，不是責備。

### 台灣端（D1）

- **PET 的健保條文明著把子宮體癌排除在腫瘤適應症之外，也明著禁止例行追蹤**。26072B 正子造影-全身 36,500 點／26073B 局部 26,500 點，
  備註逐字[D-S72]：腫瘤適應症清單為「(1)乳癌、淋巴癌之分期、治療及懷疑復發或再分期。(2)大腸癌、直腸癌、食道癌、頭頸部癌(不包含腦瘤)、
  原發性肺癌、黑色素癌、甲狀腺癌及**子宮頸癌**之分期及懷疑復發或再分期。」——**婦癌只列子宮頸癌，全表查無「子宮體癌」在 PET 適應症內**。
  同一備註逐字：「C.懷疑復發或再分期：使用於患者已接受一階段之正統治療後，偵測疑似有復發或轉移及評估復發之程度(**不得用於例行之追蹤檢查**)。」
- **CT**：33070B 無造影劑 3,800 點／33071B 有造影劑 4,560 點／33072B 有／無造影劑 5,035 點，備註只有「申報費用時應檢附報告。」
  **全表查無任何依癌別或追蹤頻次的限制條文**[D-S72]。
- **陰道／子宮頸細胞學**：15017C 婦科細胞檢查 245 點，備註逐字：「1.子宮頸或陰道抹片同一病人3~6個月內限做1次。
  2.6個月內需重新施做之適應症：(1)曾罹患過子宮頸癌或癌前病變之婦女(2)最近一次子宮頸抹片檢查結果為異常之婦女(3)免疫功能受抑制的高危險群婦。」[D-S72]
  → **有給付、有頻次上限（3–6 個月 1 次），但這與「指引不建議常規做」是兩回事**，文章要把兩件事分開講。
- **CA-125**：12077C／27053C「ＣＡ–１２５腫瘤標記」各 400 點，**備註欄空白，全表查無追蹤頻次限制條文**[D-S72]。
  → 寫法：「健保表列有 CA-125 這個項目、條文沒有寫追蹤頻次限制；但國際指引在無症狀追蹤是不建議做的。要不要驗，問你的醫師。」**不推論。**
- **重大傷病證明**（子宮體癌 C54 落在附表一第一項「(五)除(一)-(四)之其他惡性腫瘤」）：**證明有效期限 5 年**（113-12-31 前與 114-01-01 後兩版皆同）[D-S73]。
  重新申請的期限，《全民健康保險保險對象免自行負擔費用辦法》第 5 條逐字[D-S73]：
  「重大傷病證明有效期間屆滿，申請人得於下列期限內，依第二條規定重新申請：**一、有效期間為二年以上者：效期屆滿三個月前。**
  二、有效期間為一年或六個月者：效期屆滿一個月前。三、有效期間為三個月以下者：效期屆滿十四日前。
  於前項期限內重新申請，經保險人核定繼續取得重大傷病證明者，**其效期得予銜接**。逾前項期限始重新申請……以保險對象提出申請之日為生效日。
  原疾病經重新審查結果，確認不符重大傷病規定者，不再發給重大傷病證明。」
  → **實用結論：五年到期前三個月要重新申請，逾期會斷保障且不溯及。** 其他文件（身心障礙、保險理賠等）一句指向站上 `sit-paperwork`。
- **子宮體癌在台灣的位置**：衛福部 112 年癌症登記報告[D-S74]——112 年女性標準化發生率順位「依序為乳癌、肺癌、大腸癌、甲狀腺癌、**子宮體癌**、
  肝癌、卵巢癌、皮膚癌、胃癌、子宮頸癌」（**女性第 5 位**）；男女合計新發生人數第 10 位；**發生年齡中位數 57 歲**（全癌症中位數 65 歲）。
- **官方明說子宮體癌沒有篩檢，只有症狀警訊**：衛福部 110 年癌症登記新聞稿逐字[D-S75]：
  「目前國際間尚無實證建議對攝護腺癌、胰臟癌、非何杰金氏淋巴瘤及**子宮體癌**的無症狀者進行篩檢……子宮體癌：**不正常的出血，包括：
  月經週期紊亂、長期持續性出血、月經長久不來後突然大量出血或者停經後的出血。**」
  → 這段可以直接用在 D1 的症狀教育段（也是 A1 的素材，D1 用時一句帶過並指向 A1）。
- **gap（查不到，不推論）**：
  - **子宮體癌依期別的五年存活率**：國健署癌症登記報告的期別存活表在 `hpa.gov.tw`，本 session **TLS 憑證鏈驗證失敗（curl 60，
    加 `--cacert /root/.ccr/ca-bundle.crt` 亦同；WebFetch 回 robots.txt 取得失敗）**；`tcr.cph.ntu.edu.tw` 連線被重置。
    衛福部鏡像的新聞稿只有發生數與順位，**沒有期別存活率**。→ 文章寫「台灣官方的期別存活數字我查不到可引用的版本」，**不得用國外數字冒充台灣數字**。
  - 健保**追蹤影像的頻次限制條文**：除 PET 的「不得用於例行之追蹤檢查」外，CT／MRI／腫瘤標記**查無頻次限制列項**。

### 給繪圖組的數字（D1）

- TOTEM 兩臂 5 年 OS：**90.6% vs 91.9%**（n=1,847，HR 1.13）[D-S7]；整體復發率 12.3%[D-S3]。
- 復發時間分布：**2 年內 66.7%、3 年內 80.2%**（n=81 復發）[D-S9]；孤立陰道復發中位 11 個月 vs 陰道外 20 個月[D-S14]。
- 第 1 期分母樹：**2,815 人 → 復發 278（10%）→ 孤立陰道 61（2%）→ 陰道頂端 42（69% of 61）**[D-S14]。
- 陰道復發的偵測方式：**20 例中 14 例靠症狀＋內診，1 例單靠細胞學**[D-S8]。
- 第二原發癌：**533 人 / 16.7 年 → 89 人（17%）；乳房 29%、大腸直腸 13%、肺 12%**[D-S16]。

---

## D2 `em-recurrence`〈復發之後，還有哪些路〉【紅線 9，雙向】

### 分類骨架（依 ESGO 2025，逐字）

ESGO-ESTRO-ESP 2025 把復發分成三塊：**Locoregional recurrent disease（再分成「未照過放療」與「照過放療」）／Oligometastatic recurrent disease／
Disseminated recurrent disease**[D-S1]。這個切法就是 D2 的章節結構，也是 `fig-em-recurrence` 的三格。

---

### ① 陰道／陰道頂端孤立復發、**先前未接受過放療**者

**指引原文**[D-S1]（Radiotherapy-naive patients）逐字：
> 「For locoregional recurrence, the preferred primary therapy should be **external beam radiotherapy with or without image-guided
> brachytherapy and with or without chemotherapy (IV, A)**. For vaginal cuff recurrence, **pelvic external beam radiotherapy plus
> intracavitary image-guided brachytherapy (with or without intrauterine image-guided brachytherapy) is recommended (IV, A)**.
> In cases of superficial tumours, **intracavitary image-guided brachytherapy alone can be considered (IV, A)**.
> An easily accessible, superficial vaginal tumour can be resected vaginally before radiotherapy (IV, C).」

附錄的證據摘要逐字[D-S2]：
> 「with the advent of modern image-guided radiation therapy, including IMRT and image-guided adaptive brachytherapy, **radiotherapy has
> become the treatment of choice in previously not-irradiated patients with isolated vaginal recurrence or locoregional recurrence**.
> … In patients with vaginal-only recurrences of grade 1 or 2 endometrioid endometrial cancer, **EBRT + image-guided brachytherapy (IGBT)
> (without addition of chemotherapy) results in excellent outcome (DFS 73% at 3 years)**.」

**主力證據——GOG-0238（唯一的隨機試驗）**[D-S22]（Klopp AH et al., J Clin Oncol 2024;42(20):2425–2435）
- 2008-02 至 2020-08，**n=165 隨機 1:1**：單純放療 vs 放療＋每週 cisplatin 40 mg/m²。
- 族群標籤（必須跟著數字寫）：**82% 是低惡性度（grade 1 或 2）類內膜組織型；86% 復發侷限於陰道。**
- 外照射（3D 或 IMRT）後以近接治療或外照射加強。
- **主要結果：3 年時單純放療組 73%、化放療組 62% 存活且無疾病惡化。** 中位 PFS：單純放療**未達到** vs 化放療 73 個月，**HR 1.25（95% CI 0.75–2.07）**。
- **加化療的急性毒性更高。**
- 作者結論逐字：「**Excellent outcomes can be achieved for women with localized recurrences of endometrial cancer when treated with radiation
  therapy. The addition of chemotherapy does not improve PFS** for patients treated with definitive radiation therapy for recurrent endometrial
  cancer and increases acute toxicity. **Patients with low-grade and vaginal recurrences who constituted the majority of those enrolled are
  best treated with radiation therapy alone.**」

**歷史對照——PORTEC-1 的救援結果**[D-S21]（Creutzberg CL et al., Gynecol Oncol 2003;89(2):201–209）
- PORTEC-1 收 715 人（第 1 期，G1–2 深肌層侵犯或 G2–3 淺肌層侵犯；全部腹式子宮切除、**未做淋巴廓清**），隨機骨盆放療 46 Gy vs 不治療；714 人可分析。
- 中位追蹤 73 個月。**8 年局部區域復發：放療組 4% vs 對照組 15%（P<0.0001）；8 年總存活 71% vs 77%（P=0.18）；8 年遠端轉移 10% vs 6%（P=0.20）。**
- **救援的分母**：局部區域復發多數在陰道、主要在陰道頂端。**39 位孤立陰道復發者中，35 位（87%）以根治意圖治療**（通常外照射＋近接治療，部分加手術）。
  **35 人中 31 人（89%）達到完全緩解；其中 24 人（77%）在後續追蹤時仍維持完全緩解**。5 人後來出現遠端轉移、2 人二度陰道復發。
- **關鍵的分層數字（紅線 9 的兩個方向都在這一句裡）**：
  - 依復發部位：**3 年存活——陰道復發 73%、骨盆復發 8%、遠端復發 14%（P<0.001）。**
  - 依是否照過放療：**首次復發後 3 年存活——對照組（未照過放療）51% vs 放療組（照過）19%（P=0.004）。**
  - **5 年陰道復發後存活：對照組 65% vs 放療組 43%。**
- 作者結論逐字：「Treatment for vaginal relapse was effective, with **89% CR and 65% 5-year survival in the control group**, while there was
  **no difference in survival between patients with pelvic relapse and those with distant metastases**.」

**當代單中心系列（分母小，但補上「影像導引時代」的局部控制與毒性）**
- **Alban 2021**[D-S23]（IJGC 2021;31:1007–1013；Brigham/Dana-Farber）：**n=62**，第 1–2 期內膜癌、陰道復發、**先前皆未做輔助放療**，
  外照射＋影像導引近接治療根治意圖。89% 類內膜、85% G1–2、89% 陰道單獨復發。中位追蹤 39 個月。
  **3 年／5 年：陰道控制 86%／82%，無復發存活 69%／55%，總存活 80%／61%。**
  多變項：**非類內膜組織型 HR 12.5（P<0.01）復發風險**、死亡風險高 4.5 倍（P=0.02）。
  **MMR 分層（僅 20 人有資料，全為 G1–2 類內膜，10 人 MMR 缺損）：3 年無復發存活 MMR 完整 100% vs MMR 缺損 52%（P=0.03）。**
  晚期毒性：G2／G3 腸胃道 27%／3%、泌尿道 15%／2%、陰道 16%／2%。
- **Maina 2026**[D-S28]（Brachytherapy 2026;25:107–114；Princess Margaret）：**n=56** 接受救援 MRI 導引腔內／組織插種近接治療；94% 類內膜。
  HR-CTV D90 中位 82 Gy。中位追蹤 39.5 個月：**2 年局部失敗 5.9%（95% CI 1.5–15.9）、2 年 DFS 83%（73–94）、2 年 OS 94%（87–100）**；
  最高晚期毒性只到 grade 2（腸胃道 0 例、泌尿道 1 例、陰道 6 例）。
- **Baek 2016**[D-S26]（Brachytherapy 2016;15:812–816，日本，1997–2012，**n=43**，79% 組織插種、40% 併外照射；中位追蹤 58 個月）：
  **5 年 OS 84%、PFS 52%、局部控制 78%。** 原發手術時的分化度是強預後因子：**G1–2 vs G3 的 5 年 OS 96% vs 40%（P<0.01）、5 年 PFS 58% vs 0%（P<0.01）。**
  併外照射者無淋巴結復發（0/17），單純近接治療者 23%（6/26）有淋巴結復發（P=0.047）。
- **Sekii 2017**[D-S27]（J Contemp Brachytherapy 2017;9:209–215，日本，1992–2014，**n=37**）：**4 年 OS 81.0%、局部控制 77.9%、PFS 56.8%**；
  **從診斷復發到開始放療 <3 個月 vs ≥3 個月是局部控制與 PFS 的顯著預測因子**；無 grade 3 以上晚期併發症。

> **紅線 9 正面段的可寫上限**：「低惡性度、類內膜、只在陰道、而且之前沒照過放療的復發，
> 用外照射加上影像導引近接治療，隨機試驗裡 **3 年有 73% 的人活著而且沒有再惡化**；單中心系列的 5 年陰道控制超過 80%。」
> **同一段必須接上**：這個分母是「82% 低惡性度、86% 陰道侷限」的族群；非類內膜組織型在同一個治療下復發風險是 12.5 倍[D-S23]、
> 原發 G3 者 5 年無惡化存活是 0%[D-S26]。

---

### ② 骨盆內／淋巴結復發，以及**先前照過放療**者

**指引原文**[D-S1]（Radiotherapy-pretreated patients）逐字：
> 「After previous adjuvant brachytherapy only, an **external beam radiotherapy and image-guided brachytherapy boost is recommended (IV, C)**.
> After previous external beam radiotherapy (with or without brachytherapy), the **molecular subtype should be considered in the decision
> making about radical surgery (IV, A) or chemotherapy and immune checkpoint inhibitors, followed by immune checkpoint inhibitors in patients
> with MMRd tumours who are immune checkpoint inhibitor-naive (II, B)**. Radical surgery should only be done **if complete resection with
> clear margins in a curative intent seems feasible with acceptable morbidity (IV, A)**. If radical surgery is not feasible, primary systemic
> therapy should be considered … **Re-irradiation with curative intent could be considered in a specialised centre for patients with previous
> external beam radiotherapy for whom surgery is not feasible (IV, C)**.」

殘存淋巴結／骨盆病灶（非復發、是初次手術後殘留）另有一段[D-S1]：不可切除者「primary systemic therapy accounting for the molecular profile,
external beam radiotherapy, or both should be used (**I, A**)」；外照射「should be delivered to pelvic nodes with or without para-aortic nodes,
with dose escalation to involved nodes using an integrated boost (IV, B)」。

**骨盆復發的預後基準線（要跟陰道復發並排寫）**
- PORTEC-1[D-S21]：**3 年存活——骨盆復發 8%、遠端復發 14%、陰道復發 73%（P<0.001）**；作者明說骨盆復發與遠端轉移的存活**沒有差別**。
- Rios-Doria 2023[D-S14]：第 1 期復發 278 人中，**陰道外復發 217 人（78% 的復發者）**。
- Knox 2025[D-S11]（接受過輔助放療者 n=264）：復發 41 人中**只有 4 人是孤立局部復發，其餘偵測到時多半已合併遠端病灶**。

**再照射（先前照過外照射者）——分母小、控制率中等、毒性明顯上升**
- **Ling 2019**[D-S24]（Gynecol Oncol 2019;152:581–586，匹茲堡，**n=22**，根治意圖再照射近接治療±外照射）：
  先前放療為陰道近接 54.5%、骨盆外照射 22.7%、兩者 22.7%；中位再照射間隔 26.6 個月；累積 D2cc 限制膀胱 <90 Gy、直腸乙狀結腸 <75 Gy。
  中位追蹤 27.6 個月：**3 年局部控制 65.8%、區域控制 76.6%、無疾病存活 40.8%、總存活 68.1%**；**無 grade ≥3 急性或晚期直腸乙狀結腸／膀胱毒性**。
  作者結論逐字：「offers a chance to potentially **salvage 40% of patients** presenting with vaginal recurrence in the setting of prior pelvic radiation」。
- **Lee 2022**[D-S25]（Brachytherapy 2022;21:263–272，Brigham，**n=32**，2003–2017）：先前放療為陰道近接 19 人（59%）、骨盆外照射 7 人（22%）、兩者 6 人（19%）。
  中位追蹤 47 個月：**3 年／5 年陰道控制 64%／56%、無復發存活 47%／41%、總存活 68%／42%**；6 人（19%）在 85–155 個月時仍無疾病證據。
  **晚期 grade 2／grade 3 毒性：腸胃道 13%／16%、泌尿道 19%／13%、陰道 9%／16%。**
  累積直腸 D2cc（前次＋救援）可預測 grade 2+ 與 grade 3 腸胃道毒性；**估計 10% 晚期 grade 2+／grade 3 風險對應累積直腸 D2cc 86 Gy／92 Gy**。
- ESGO 附錄的補充[D-S2]：「Interstitial brachytherapy as sole modality of treatment or combined with EBRT can result in **high and durable
  local control**」「In general, **a longer time interval between the first and second course of radiation and recurrence with lesions <4 cm in
  diameter tend to have a better outcome**. Multidisciplinary management is critical … and to communicate clearly to patients the potential
  side effects and expected treatment outcome.」
- **再照射的通則、風險與怎麼問 → 一句指向站上 `sit-reirradiation`〈照過的地方，能不能再照〉。D2 不重寫再照射的一般原則。**

**手術：骨盆廓清術（pelvic exenteration）——適應與代價**
- 指引門檻[D-S2]逐字：「**Pelvic exenteration for central local relapse should only be performed if clear margins can be achieved, and in the
  absence of extrapelvic disease in an curative intent.**」
- **COREPEX 國際多中心登錄**（20 家歐洲三級中心，2005-01 至 2023-03；子宮頸／陰道／外陰／**子宮內膜**癌；前位或全骨盆廓清）：
  - 存活面[D-S29]（Bizzarri N et al., Obstet Gynecol 2025;146:737–749）：**n=862**；**676 人（78.4%）切緣無腫瘤**。
    預後分數把根治意圖者分成四組，**5 年無疾病存活 43.7%／24.9%／22.2%／8.0%（P<.001）；5 年總存活 54.3%／40.4%／24.0%／4.3%（P<.001）**。
    最常見復發部位是**遠端（166 人，32.1%）**。全骨盆廓清、切緣陽性、有淋巴血管腔侵犯獨立預測較差 DFS 與 OS；
    **在「持續性疾病」（非復發）時做廓清，總存活較差。** 主動脈旁淋巴結轉移者的 5 年 DFS 與癌症特異存活顯著較差。
  - 併發症面[D-S30]（Bizzarri N et al., Int J Gynecol Cancer 2026;36:102820）：同一批 **n=862**；
    **嚴重術中併發症 7 人（0.8%）、術中死亡 0**；**嚴重早期術後併發症 225 人（26.1%）、30 天內死亡 27 人（3.1%）**；
    **嚴重晚期術後併發症 87 人（10.1%）、31–180 天死亡 16 人（1.8%）**。
    最常見的嚴重早期併發症是骨盆膿瘍／積液（23.4%）與尿路造口漏／廔管（13.4%）；晚期是骨盆膿瘍／積液（21.6%）與良性輸尿管狹窄（13.5%）。
  - **內膜癌在 COREPEX 中的佔比**：另一份同世代分析顯示外陰癌佔 9.2%（79/861）[參見 D-S29 系列]；**單一中心系列**（英國，2004–2024，n=47）中
    **內膜癌 17 人（36%）是最大宗**，主要併發症（Clavien-Dindo ≥3）32%，術後死亡 1 人，中位住院 17 天、加護 4 天，中位失血 1.5 L、手術時間 391 分鐘[D-S30 系列，n=47 之數字標為單中心]。
- **寫法**：骨盆廓清術是「切緣乾淨才做、沒有骨盆外病灶才做」的手術；代價是**四分之一的人有嚴重早期併發症、3.1% 在 30 天內死亡**，
  換到的是**分成四個風險組後 5 年無疾病存活 43.7% 到 8.0%** 的區間。**不可以只寫存活不寫代價，也不可以只寫代價不寫那 43.7%。**

---

### ③ 遠端轉移／播散性復發

**指引原文**[D-S1]（Disseminated recurrent disease）逐字：
> 「In recurrent disseminated disease (including peritoneal and lymph node relapse), **surgery should only be considered if complete
> macroscopic resection is feasible with acceptable morbidity and quality of life**. Systemic therapy or radiotherapy should be considered
> postoperatively, depending on the extent and pattern of relapse and the amount of residual disease (IV, B). … **Palliative surgery can be
> done in selected cases to alleviate symptoms (eg, bleeding, fistula, or bowel obstruction; IV, B). Palliative radiotherapy is indicated for
> symptoms related to pelvic or systemic disease (IV, A).**」
> 復發組織的重驗：「If feasible, **repeated mismatch repair testing should be considered on a relapsed tissue sample to guide treatment (IV, B)**.」

**寡轉移**[D-S1]逐字：
> 「Patients with oligometastatic disease (**between one and five metastases in up to three regions**) should be considered for local therapy.
> Treatment options include (IV, B) **surgery, radical radiotherapy—including stereotactic radiotherapy—and local ablating techniques**.
> Following local treatment, systemic therapy could be considered (IV, C).」
> → **寡轉移的一般原則、SBRT 的證據強度與怎麼問，一句指向站上 `sit-oligomet`〈打掉那兩三顆，然後呢〉。D2 只寫「內膜癌的指引把它定義成 1–5 顆、≤3 個部位，等級 IV, B」。**

**系統性治療在復發情境的「位置」（療效數字全部歸 B5／B3，這裡只寫位置與一句指路）**
- 指引把第一線分成 MMR 狀態兩條路[D-S1]：MMRd 者「should be offered an immune checkpoint inhibitor … in combination with carboplatin–paclitaxel
  chemotherapy, followed by immune checkpoint inhibitors as maintenance therapy (**I, A**)」；非 MMRd 且快速進展／有症狀者「should be offered
  carboplatin–paclitaxel chemotherapy (**I, A**)」，加免疫檢查點抑制劑（±PARP 抑制劑）維持「can be considered (**I, B**)」。
  標準化療是「**six cycles of carboplatin–paclitaxel (I, A)**」。
- 第二線[D-S1]：未曾用過免疫檢查點抑制劑者，MMRd「preferred option should be an immune checkpoint inhibitor monotherapy … (**III, A**)」，
  pembrolizumab＋lenvatinib「could be considered (**I, B**)」；非 MMRd「should be offered pembrolizumab and lenvatinib (**I, A**)」。
  HER2 過度表現者可考慮 HER2 標靶策略（II, B／III, B）。
- 多線之後[D-S1]逐字：「The use of multiple lines of systemic therapy, particularly in platinum-pretreated and immune checkpoint
  inhibitor-pretreated patients, **should be carefully evaluated for individuals, considering the low efficacy and weighed against best
  supportive care (IV, B)**.」——**這一句要寫進去**，它是「什麼時候該談停手」的指引原文依據。
- → **免疫治療誰有效、有多有效，一句指向 B5；化療的三個試驗歸 B3；分子分型改治療歸 B4。D2 一個療效數字都不放。**

**荷爾蒙治療在低惡性度、荷爾蒙受體陽性復發的角色與反應率（帶分母）**
- 指引原文[D-S1]逐字：「In **low-grade oestrogen receptor-positive, low volume or asymptomatic, advanced or slowly growing recurrent tumours,
  endocrine therapy is the preferred systemic therapy**. In these instances, **progestins (medroxyprogesterone or megestrol) are recommended
  (III, A)**. Alternatives include **aromatase inhibitors and tamoxifen (IV, C)**.」
- **GOG-81（Thigpen 1999）**[D-S31]（J Clin Oncol 1999;17:1736–1744）：**n=299** 晚期或復發內膜癌，隨機口服 medroxyprogesterone acetate
  **200 mg/日 vs 1,000 mg/日**。
  - **低劑量組（n=145）：完全緩解 25 人（17%）＋部分緩解 11 人（8%）＝總反應率 25%**；中位無惡化存活 3.2 個月、中位存活 11.1 個月。
  - **高劑量組（n=154）：完全緩解 14 人（9%）＋部分緩解 10 人（6%）＝總反應率 15%**；中位無惡化存活 2.5 個月、中位存活 7.0 個月。
  - 校正後高劑量相對低劑量的反應勝算比 0.61（90% CI 0.36–1.04）——**高劑量沒有比較好，趨勢反而相反。**
  - **關鍵的族群分層**：反應與**分化良好的組織型、黃體素受體陽性**相關；
    **「Patients with poorly differentiated and/or progesterone receptor levels less than 50 fmol/mg cytosol protein had only an 8% to 9% response rate.」**
- **GOG（Fiorica 2004）**[D-S32]（Gynecol Oncol 2004;92:10–14）：megestrol acetate 80 mg BID × 3 週與 tamoxifen 20 mg BID × 3 週**交替**，
  未曾接受細胞毒或荷爾蒙治療者；61 人入組、**56 人可評估**。
  - **15 人有反應（12 完全＋3 部分），總反應率 27%（90% CI 17–38%）**；**15 位反應者中 8 人（53%）反應持續超過 20 個月**。
  - 依分化度：**G1（n=16）38%、G2（n=17）24%、G3（n=23）22%**。依年齡：≤60 歲（n=16）44% vs >60 歲（n=40）20%。
    依部位：骨盆外病灶（n=42）31% vs 侷限骨盆／陰道（n=14）14%。
  - 中位無惡化存活 **2.7 個月**、中位總存活 **14.0 個月**。**2 人發生 grade 4 血栓栓塞事件。**
- **寫法**：荷爾蒙治療的價值是「**副作用小、少數人反應可以很久（53% 的反應者超過 20 個月）**」，不是「反應率高」——
  總反應率 25–27%、中位無惡化存活只有 2.5–3.2 個月。**必須寫黃體素受體陰性／低分化者只有 8–9% 反應率**，
  以及**血栓栓塞風險**（並一句指向 `care-thrombosis`）。

**復發後的預後依組織型與分子型的差異**
- **組織型**：Alban 2021[D-S23]，陰道復發根治性放療後，**非類內膜組織型復發 HR 12.5（P<0.01）、死亡風險高 4.5 倍（P=0.02）**。
  Baek 2016[D-S26]，原發手術時 G1–2 vs G3 的 5 年 OS **96% vs 40%**、5 年 PFS **58% vs 0%**。
- **分子型（診斷時 vs 復發時都適用）**：McHenry 2024[D-S33]（Histopathology 2024;85:614–626）——**n=141** 診斷即轉移或後續復發／轉移的
  子宮內膜樣癌，TCGA 分類：**POLE 突變 9 例（6%）、MSI 45 例（32%）、p53 異常 16 例（11%）、NSMP 71 例（50%）**。
  **從高期別（III–IV）診斷時起算、或從低期別（I–II）復發時起算的疾病特異存活，都與 TCGA 分類強相關（高期別 P=0.02、低期別 P=0.017）。**
  原發與轉移／復發腫瘤的分類**不一致者 4/105（3.8%）**（2 例 PMS2/MSH6 IHC、2 例 p53 IHC）——作者因此建議在復發／轉移組織上重做分類。
- **真實世界的反方向**：Lindemann 2025[D-S34]（IJGC 2025;35:101618；挪威 Radium Hospital，2006–2017，接受含鉑化療者）
  ——晚期組 264 人、**復發組 96 人**。分子分類在**晚期病人**是顯著預後因子（復發時間與癌症特異存活皆 P<.0001），
  但**「the outcome did not differ significantly by molecular groups in recurrent patients」**。
  p53 異常最差：晚期 III/IV 期復發時間 HR 1.57（1.07–2.30）、癌症特異存活 HR 1.78（1.19–2.65）；
  **復發族群中同方向但未達顯著**（HR 1.45，0.83–2.52；HR 1.60，0.99–2.68）。POLE 突變者即使已復發，結果仍佳（人數很少）。
- **真實世界的整體基準線（免疫治療進場前）**：ENDOVIE[D-S35]（BMJ Open 2025;15:e096837，法國，2019 年接受第一或第二線化療者 **n=200**）：
  第一線 127 人、第二線 73 人；類內膜 62.0%；第一線 78.0% 用 carboplatin＋paclitaxel。
  **中位真實世界無惡化存活與總存活：第一線 8.5 與 13.2 個月；第二線 4.0 與 9.4 個月。**
  癌肉瘤、肝轉移、FIGO IVB 與較差結果相關。**這是 PD-1 抑制劑上市前的法國真實世界基準，引用時必須標「免疫治療進場前」。**

### 反方向的資料（誠實必列）

- **加化療在陰道復發不但沒好處、毒性更高**（GOG-0238[D-S22]）——這是「多做一點比較保險」直覺的直接反例。
- **照過放療的人，復發之後的存活差很多**：PORTEC-1 首次復發後 3 年存活 **對照組 51% vs 放療組 19%（P=0.004）**[D-S21]。
  這句話**不是**「不要做輔助放療」——PORTEC-1 的輔助放療把 8 年局部區域復發從 15% 壓到 4%，代價是復發者的救援餘地變小。
  **這個取捨屬於 B1，D2 只寫「如果你之前照過，救援的路會比較窄」並指向 B1。**
- **分子分型在復發後的預後價值**：McHenry[D-S33] 說有、Lindemann[D-S34] 在復發族群說看不出來。**兩篇都要寫。**
- 骨盆廓清術的 5 年無疾病存活在最差的預後組只有 **8.0%**，30 天死亡率 3.1%[D-S29][D-S30]。

### Claim ceiling（D2，紅線 9 的硬邊界）

- **可寫（正方向，必須寫足）**：
  - 「復發不等於末期。復發的位置決定了完全不同的路。」
  - 「陰道／陰道頂端的孤立復發、而且之前沒有照過放療的人，用外照射加影像導引近接治療，**隨機試驗（n=165，82% 低惡性度、86% 陰道侷限）
    3 年有 73% 的人活著且沒有再惡化**」[D-S22]；「當代單中心系列的 5 年陰道控制超過 80%、5 年總存活 61%」[D-S23]。
  - 「PORTEC-1 裡 39 位孤立陰道復發、35 位以根治意圖治療，**89% 達到完全緩解、對照組 5 年存活 65%**」[D-S21]。
  - 「同一個試驗裡，陰道復發、骨盆復發、遠端復發的 3 年存活是 **73%、8%、14%**——差別不在『復發』兩個字，在位置。」[D-S21]
  - 「低惡性度、荷爾蒙受體陽性、量少或無症狀的復發，指引把荷爾蒙治療列為**首選**（III, A）」[D-S1]；反應率 25–27%、少數人反應很久[D-S31][D-S32]。
  - 「寡轉移（1–5 顆、≤3 個部位）可以考慮局部治療（IV, B）」[D-S1]，細節指向 `sit-oligomet`。
- **不可寫**：
  - 「復發之後大多可以救回來」——GOG-0238 的 73% 是**特定族群**（低惡性度、陰道侷限、未照過放療）；骨盆與遠端復發的 3 年存活是 8% 與 14%[D-S21]。
  - 「照過放療也一樣可以救」——再照射的 3 年局部控制 65.8%[D-S24]／3 年陰道控制 64%[D-S25]，晚期 grade 3 毒性 13–16%，而且分母只有 22 與 32 人。
  - 「非類內膜／高惡性度的陰道復發一樣有效」——HR 12.5[D-S23]、G3 的 5 年 PFS 0%[D-S26]。
  - **任何免疫治療、化療、lenvatinib＋pembrolizumab 的療效數字**（歸 B5／B3）。只寫「在復發情境的位置」＋一句指路。
  - 「分子分型會決定你復發後能不能救」——[D-S33] 與 [D-S34] 方向不一致。
  - 「骨盆廓清術可以治癒」——只能寫「在切緣可以乾淨、沒有骨盆外病灶的人身上是根治意圖的手術」＋四個風險組的 5 年 DFS 區間＋併發症與 30 天死亡率。
  - 任何一句讓讀者自己判斷「我這種復發屬於哪一類」——**分類是婦癌科＋放腫科＋影像做的**，文章給的是問題清單。
  - 復發後決定要不要繼續治療：ESGO 的「low efficacy … weighed against best supportive care (IV, B)」[D-S1] 可引，
    但**不可寫成「該放棄了」**，寫成「這是一個要跟醫療團隊一起評估的問題，指引自己寫了要權衡」。

### Caveats／safety notes（D2）

- **復發的第一個訊號常常是陰道出血**——復發後回頭看，多數陰道復發是靠症狀與內診發現的[D-S8]。**不要等下次回診。**
- **時間**：Sekii 2017[D-S27] 顯示從診斷復發到開始放療 **<3 個月** 者的局部控制與 PFS 顯著較好。這是「別拖」的證據，但分母只有 37 人，寫成「有一筆資料指向早一點開始比較好」。
- **復發組織要不要重新切片／重做 MMR**：ESGO「If feasible, repeated mismatch repair testing should be considered on a relapsed tissue sample (IV, B)」[D-S1]；
  McHenry 顯示 3.8% 的人分類會改變[D-S33]。這是可以在門診問的具體問題。
- **荷爾蒙治療的血栓風險**：GOG 交替療法試驗中 2 人 grade 4 血栓栓塞[D-S32]。指向 `care-thrombosis`。
- **多專科討論**：ESGO 附錄逐字「Multidisciplinary management is critical to develop individualised plans」[D-S2]——一句指向 `sit-mdt`；
  想聽第二意見 → `sit-second-opinion`。

### 台灣端（D2）

- **PET 在子宮體癌的復發評估查無給付適應症**：26072B／26073B 的腫瘤適應症清單婦癌只列子宮頸癌，**未列子宮體癌**；
  且「懷疑復發或再分期」欄逐字寫「**不得用於例行之追蹤檢查**」[D-S72]。→ 文章可寫「PET 這一項的健保條文沒有把子宮體癌列進去，
  要不要做、怎麼申請，問醫務課／個管師」，**不推論自費金額**。
- **近接治療的支付項目**（給 D2 提到救援近接治療時用；實務細節歸 B2）：37018B 遙控後荷式近距治療（簡單）每次 4,126 點、37019B（複雜）每次 6,600 點、
  37010B 組織插種治療 5,611 點、37007B 安裝近接治療器（複雜）每次 3,236 點、37008B（簡單）1,650 點；37047B 身體立體定位放射治療 213,662 點[D-S72]。
  **D2 只在需要時提一句，點數與適應症的完整討論歸 B2／`sit-oligomet`。**
- **化療藥、免疫治療藥的健保條文歸 B5／B3，D2 不查不寫。**
- **gap**：台灣本土的內膜癌復發後救援結果（陰道復發救援成功率、骨盆廓清術例數與結果）**查無可引用的官方或期刊來源**。

### 給繪圖組的數字（`fig-em-recurrence`，D2 主圖）

三格結構，每格都要有分母標籤：

1. **陰道／陰道頂端（未照過放療）**
   - GOG-0238：n=165 隨機，**3 年無惡化存活 73%（單純放療）vs 62%（加化療）**，HR 1.25[D-S22]。標籤：82% G1–2 類內膜、86% 陰道侷限。
   - PORTEC-1：39 位孤立陰道復發 → 35 位根治意圖 → **31 位（89%）完全緩解 → 24 位（77%）維持**；**3 年存活 73%**[D-S21]。
   - Alban 2021：n=62，**5 年陰道控制 82%、5 年總存活 61%**[D-S23]。
2. **骨盆／淋巴結（含照過放療者）**
   - PORTEC-1：**骨盆復發 3 年存活 8%**[D-S21]。
   - 再照射：Ling n=22 **3 年局部控制 65.8%、3 年 OS 68.1%**[D-S24]；Lee n=32 **3 年陰道控制 64%、5 年 56%**，晚期 G3 毒性 13–16%[D-S25]。
   - 骨盆廓清術：n=862，**5 年 DFS 43.7%→8.0%（四個風險組）**，嚴重早期併發症 26.1%、30 天死亡 3.1%[D-S29][D-S30]。
3. **遠端／播散**
   - PORTEC-1：**遠端復發 3 年存活 14%**[D-S21]。
   - 寡轉移定義：**1–5 顆、≤3 個部位**（ESGO 2025，IV, B）→ 箭頭指向 `sit-oligomet`[D-S1]。
   - 系統性治療：只畫「MMRd／非 MMRd 兩條路」的**方向箭頭**，**不放任何療效數字**，箭頭標「數字見 B5」[D-S1]。
   - 荷爾蒙治療（低惡性度、ER 陽性、量少）：**反應率 25–27%**[D-S31][D-S32]，標籤「PR 陰性／低分化只有 8–9%」[D-S31]。

---

## D3 `em-lymphedema`〈下肢淋巴水腫：機率、預防與處理〉

> **本篇的定位**：淋巴水腫的一般原則（什麼是淋巴系統、為什麼會腫、壓力衣的基本概念、日常保養通則）
> **一句指向站上 `bc-lymphoedema`〈手腫起來：淋巴水腫的真實機率〉，不重寫**。
> D3 只寫**下肢與骨盆的特殊處**：分層機率、判定方法的爭議、蜂窩性組織炎的急症面、以及下肢在功能／鞋襪／旅行上的不同。

### Key facts

**(a) 發生率：一個 1.3% 到 49.4% 的區間，先寫「為什麼是區間」再寫數字**

**必須先寫的那一句**——Wedin 2021[D-S43]（IJGC 2021;31:1416–1427；瑞典 14 家醫院前瞻縱貫，**n=235** 內膜癌，116 人做淋巴廓清、119 人沒做；
術前與術後 1 年，**同一批人同時用四種方法判定**：①下肢周徑推算的原始體積 ②BMI 標準化體積 ③臨床分級 ④病人自覺腫脹；體積法以增加 ≥10% 為水腫）：

> 「**Risk factors varied substantially, depending on the method of determining lymphedema.**」
> - 淋巴廓清作為風險因子：**BMI 標準化體積 aOR 14.42（95% CI 3.49–59.62）／臨床分級 aOR 2.11（1.04–4.29）／病人自覺 aOR 2.51（1.33–4.73）
>   ／原始體積：看不出來（非顯著）**。
> - **輔助放療只有在「BMI 標準化體積」這一種方法下才是風險因子（aOR 15.02，95% CI 2.34–96.57）。**
> - 年齡只有在 BMI 標準化體積（aOR 1.07）與病人自覺（aOR 1.06）下顯著；BMI 上升只有在原始體積（aOR 1.92）與病人自覺（aOR 1.36）下顯著。
> - 淋巴廓清的**範圍**在 BMI 標準化體積與病人自覺下強烈預測水腫，在原始體積與臨床分級下則否。
> - 作者結論逐字：「This highlights the **need for a 'gold standard' method** when addressing lymphedema for determining risk factors.」

**分層數字（每筆都帶 n 與判定方式）**

| 研究 | 設計與 n | 判定方式 | 前哨淋巴結 | 全面淋巴廓清 | 只做子宮切除 |
|---|---|---|---|---|---|
| Geppert 2018[D-S38]（瑞典，前瞻，機器人手術，ICG） | n=188 計畫收案 | 臨床判定 | **1.3%** | **18.1%**（骨盆＋腎下主動脈旁） | — |
| Leitao 2020[D-S36]（MSK，2006–2012 手術者郵寄問卷，回覆 623/1275=49%，可分析 599） | SLN 180／LND 352／單純子宮切除 67 | **13 題自填 LEL 篩檢問卷** | **27%（49/180）** | **41%（144/352）** | （另計 67 人） |
| Glaser 2021[D-S37]（Mayo，2009-01–2016-06 微創手術，n=378） | SLN 127／LND 251 | 同一份 13 題問卷 | **26.0%（33/127）** | **49.4%（124/251）** | — |
| Casarin 2025[D-S39]（義大利單中心，2020-01–2023-08，腹腔鏡 NCCN SLN 演算法，n=239，問卷回覆率 85.4%） | SLN 54.8%／系統性骨盆廓清 27.2%／單純子宮切除 18% | 驗證過的問卷 | **21.4%** | **44.6%** | （18% 未報分項） |
| Torrent 2025[D-S55]（西班牙單中心前瞻，n=97） | SLN 47／SLN＋完整廓清 50 | 自填 LELQ | **7.0%**（有症狀水腫） | **34.4%** | — |
| Bjørnholt 2025[D-S40]（丹麥全國前瞻世代，2017-03–2022-02，**低惡性度、推定第 1 期**；486/617=79% 完成術前與 12 個月 PROM） | 全部做 SLN | **EORTC QLQ-EN24 腿部淋巴水腫分數**（0–100，8 分為臨床顯著門檻） | **12 個月平均分數比術前上升 5.0 分（95% CI 3.3–6.8），低於 8 分門檻** | — | — |

**校正後的效應量（跨研究方向一致）**
- Leitao 2020[D-S36]：校正外照射與 BMI 後，**淋巴廓清 vs 前哨的 OR 1.8（95% CI 1.22–2.69，P=0.003）**。
- Glaser 2021[D-S37]：校正 BMI、外照射、糖尿病、心衰竭、FIGO 分化度後，**OR 2.75（95% CI 1.69–4.47，P<0.001）**；
  **只看前哨引進之後的同期病人，仍是 39.0%（41/105）vs 26.0%（33/127），P=0.03**（這一筆很重要——排除了「年代不同」的解釋）。
- Casarin 2025[D-S39]：**OR 3.11（95% CI 1.47–6.58）**；且**沒有其他病人或腫瘤特徵與水腫相關**。
- Accorsi 2020[D-S42]（巴西單中心，n=250，四組：單純子宮切除／＋SLN／＋淋巴廓清／＋兩者）：
  做淋巴廓清者 30 天併發症 HR 3.11（1.62–5.98）、術中併發症 HR 14.25（1.85–19.63）、**下肢淋巴水腫 HR 8.14（1.01–65.27）**；
  **子宮切除＋SLN 相對於單純子宮切除，術中與 30 天併發症都沒有增加**（手術時間多約 20 分鐘，P=.016）。
- 統合分析 Helgers 2020[D-S41]（J Clin Med 2021;10:120，7 篇、**共 3,046 人**）：只有 3 篇報了下肢水腫的勝算比，分別是
  **OR 0.05（0.01–0.37）、0.07（0.00–1.21）、0.54（0.37–0.80）**——**離散很大、其中一筆未達顯著**；
  合併的「任何術後併發症」OR 0.52（0.36–0.73，I²=48%，P<0.001）、「嚴重術後併發症」OR 0.52（0.28–0.96，I²=0%，P=0.04）。
  作者結論逐字：「There are **strong indications** that SLN results in a lower incidence of lower-extremity lymphedema … **In spite of the
  paucity and heterogeneity of studies**, direction of results was similar in all studies.」

**放療與 BMI 的獨立效應**
- Leitao 2020[D-S36]：**接受外照射者水腫盛行率 51%（23/45）vs 未接受者 35%（170/487），OR 1.95（95% CI 1.06–3.6，P=0.03）**；
  **BMI 每升 1 單位 OR 1.04（1.02–1.06，P=0.001）**。（注意：該世代外照射使用率很低，SLN 組 5.5%、LND 組 10%。）
- Wedin 2021[D-S43]：輔助放療只有在 BMI 標準化體積法下顯著（aOR 15.02）。
- Bjørnholt 2025[D-S40]：術前的腿部水腫分數與 BMI 預測 12 個月的分數；**3 個月時的分數預測 12 個月的分數**。

**(b) 發生的時間分布**
- **Utsugi 2025（5 年前瞻）**[D-S45]（Sci Rep 2025;15:26371；2011–2012 接受含骨盆淋巴廓清的婦癌手術者 **n=190**，追蹤 5 年；
  水腫定義為 **ISL 第 I 期以上**）：
  **5 年累積發生率 39.6%**；**第一年發生率最高**。
  多變項風險因子：**輔助化療含 docetaxel 或 paclitaxel（5 年累積 51.6%）**、**摘除淋巴結數 ≥60 顆（5 年累積 49.1%）**。
  作者結論逐字：「the incidence of lower limb lymphedema was **highest in the first year**」「**close monitoring of lower limbs is crucial in
  the first year** after lymphadenectomy for patients with these risk factors」。
- Bjørnholt 2025[D-S40]：**3 個月時就有的水腫預測 12 個月仍持續**。
- Cibula 2021（子宮頸癌 SLN 前瞻，n=150，**族群不同，標籤要寫清楚**）：24 個月累積輕度水腫（體積增加 10–19%）17.3%、中度（20–39%）9.2%、
  重度（>40%）僅 1 人（0.7%）；**中位發生時間 9 個月**；另有 22% 的人出現 6 個月內自行緩解的暫時性水腫。
  作者結論：以 SLN 取代骨盆淋巴廓清**不能消除**輕中度水腫的風險。→ **這一筆是子宮頸癌，D3 只能拿來講「暫時性腫脹會自己好」的概念，
  且必須標明是子宮頸癌世代。**
- **亞臨床期**：Tsuchiya 2026[D-S54]（PRS Glob Open 2026;14:e7998；婦癌術後無症狀下肢 **80 肢**，ICG 淋巴造影，中位追蹤 24 個月）：
  26 肢屬亞臨床（無症狀但 ICG 異常，stage ≥1）。**追蹤期間出現客觀水腫：亞臨床組 50% vs 非亞臨床組 5.6%（P<0.001）**，
  **HR 8.57（95% CI 2.36–31.2，P=0.0011）**。作者同時說：「**not all subclinical cases progress**, which supports the need for
  risk-based surveillance.」→ 可寫成「腫之前身體就有訊號，但有訊號不一定會腫」。

**(c) 預防與早期偵測——方向與強度要誠實，這一段目前是「幾乎沒有有效介入」**
- **Utsugi 2025（5 年前瞻，簡易淋巴引流 SLD）**[D-S46]（Sci Rep 2025;15:42805）：同一世代中未接受輔助治療的 87 人，依**病人自己的意願**
  分成 SLD 組 24 人與對照組 63 人；SLD 組每天自行做 SLD 一年，追蹤 5 年。
  **下肢周徑變化率與細胞外水／全身水比值皆無顯著差異；5 年累積水腫發生率 SLD 組 37.5% vs 對照組 23.5%，無顯著差異。**
  作者結論逐字：「**SLD does not contribute to the prevention of LLE** following gynecological cancer surgery with pelvic lymphadenectomy.」
- **反方向（品質較低）**：Wu L 2026[D-S56]（PeerJ 2026;14:e21275；廣西單一醫院，2025-01-03 至 2025-02-15 婦癌根治手術 342 人，
  **依病人自己選擇**分成術後早期徒手淋巴引流組與對照組，1:1 傾向分數配對後 111 對，術後 ≥6 個月以 GLQ 問卷評估）：
  **水腫發生率 10.81% vs 21.62%（P=0.04），RR 0.50（95% CI 0.263–0.949，P=0.034）**。
  **但**：非隨機、由病人自選、預防行為執行率也差很多（介入組 38.9% vs 對照組 15.6%，P<0.001）——**混淆嚴重，只能寫成「有一筆傾向分數配對的觀察資料
  指向這個方向，但不是隨機分派」。**
- **護理主導的衛教方案（隨機但很小）**：Tümkaya 2026[D-S 未列，僅摘要層級]（Oncol Nurs Forum，土耳其，**n=27** 試驗性隨機，介入 14／對照 13）：
  可行性佳（參與率 93.3%、完成率 96.4%、滿意度 4.54/5）；介入組在生活品質、整體健康、自我效能與水腫症狀顯著改善，
  **但「No significant short-term changes in leg circumference measurements were observed」**。
  → **這是「教育有用、但沒有量到腿變細」的典型結果**，可用來說明「早期偵測與自我管理」與「預防水腫本身」是兩件事。
- **前哨淋巴結本身是目前唯一有跨研究一致證據的「預防」**：見上表與 Helgers 統合分析[D-S41]。
  **注意用詞**：這是「少切一點淋巴結 → 少一點水腫」，不是「有一種預防治療」。
  **前哨 vs 廓清的手術決策歸 A4，D3 只寫水腫端的數字並一句指向 A4。**
- **體重**：BMI 是多篇研究裡的獨立風險因子[D-S36][D-S40][D-S43]，但**沒有任何一筆資料顯示「減重可以預防或治療已發生的下肢淋巴水腫」**。
  體重與這個癌的關係歸 C2，D3 只寫「BMI 高的人水腫比例較高，這是相關，不是介入證據」。
- **運動**：橫斷面研究顯示身體活動量與下肢水腫的關聯[D-S 見 D4 段之 Engh 2025，僅橫斷面]，**不可寫成運動能預防水腫**。

**(d) 治療——證據等級逐項標明**
- **完整消腫治療（CDT／complex decongestive therapy）與徒手淋巴引流（MLD）**：
  最高等級的證據來自**乳癌手臂水腫**的 Cochrane 回顧（Ezzo 2015）[D-S47]（Cochrane Database Syst Rev 2015;(5):CD003475，**6 個試驗**）：
  - MLD ＋壓力繃帶 vs 單純壓力繃帶（2 試驗、83 人）：**單純壓力繃帶本身就減少 30% 到 38.6% 的多餘體積；加上 MLD 再多減 7.11%
    （MD 7.11%，95% CI 1.75–12.47）**；體積減少量的差異接近顯著（P=0.06），殘餘水腫體積無顯著差異。
  - 次族群：**輕到中度水腫者從 MLD 得到的好處比中到重度者大。**
  - 作者結論逐字：「**MLD is safe and may offer additional benefit to compression bandaging for swelling reduction.**」
  - 疼痛與沉重感：「**60% to 80% of participants reported feeling better regardless of which treatment they received.**」
  - 一年追蹤：「once swelling had been reduced, participants were likely to **keep their swelling down if they continued to use a custom-made sleeve**.」
  - **關鍵讀法：壓力（bandaging／garment）是主力，MLD 是加分項；維持靠持續穿壓力衣。** 這是乳癌手臂的資料，**外推到下肢要標明**。
- **下肢專屬的物理治療證據**：Wu Y 2026[D-S48]（Front Oncol 2026;16:1792931，系統性回顧，PROSPERO CRD420251274284；
  **只有 6 個隨機試驗、共 289 人**）：物理治療介入顯著減少下肢體積或周徑，並改善疼痛、沉重感、肌力、步態與生活品質；
  **多模式物理治療優於單一模式**；所有不良事件皆為輕度、無嚴重不良事件；**沒有一篇被判為高偏誤風險**。
  → **可寫成「有，但只有 6 個小型隨機試驗、共 289 人」。**
- **氣壓治療（間歇性氣壓壓縮）**：**本 brief 未找到下肢婦癌族群的獨立隨機證據可引**。Cochrane[D-S47] 中有一個試驗比較
  「壓力袖套＋MLD」與「壓力袖套＋氣壓幫浦」，**體積減少量顯著偏向 MLD（MD 47.00 mL，95% CI 15.25–78.75；1 試驗、24 人）**，
  但這是乳癌手臂、n=24。→ **D3 寫「氣壓治療的證據在這個族群我查不到可引用的隨機資料」，不寫有效也不寫無效。**
- **外科（淋巴靜脈吻合 LVA／血管化淋巴結移植 VLNT）——全部是統合分析**單臂或觀察性研究**，沒有隨機試驗**：
  - Hahn 2025[D-S 見清單]（Microsurgery 2025;45:e70050，52 篇）：**下肢水腫的合併臨床改善 34.16%（95% CI 23.93–44.40）**；
    分項 LVA 31.87%（18.60–45.14）、VLNT 39.53%（19.37–59.69）。上肢 36.46%。
  - Shah 2026[D-S51]（JPRAS 2026;116:131–147，**25 篇、395 位下肢水腫病人**）：膝上／膝下周徑縮小率 **24.79%／29.50%**，
    肢體體積減少 **25.32%**，蜂窩性組織炎發生率顯著下降（P<0.001），不良事件 12.22%。
  - Jungbauer 2025[D-S49]（Ann Plast Surg 2025;95:522–530，23 篇、648 肢，追蹤 ≥24 個月）：
    **年蜂窩性組織炎次數的合併平均減少——LVA 下肢 −1.32（95% CI −2.08 至 −0.55）、VLNT 下肢 −1.38（−2.11 至 −0.65）**；
    VLNT 使下肢周徑減少 21.98%（19.8–24.4）。
  - **預防性（手術當下同時做）LVA**：Hinson 2025[D-S50]（J Surg Oncol 2025;132:717–726，39 篇、3,697 人；17 篇進統合分析）：
    合併續發性淋巴水腫發生率 **LVA 組 7.1% vs 對照 35.0%，RR 0.31**；乳癌次族群 RR 0.28。
    **但這 39 篇以乳癌為主，婦癌族群的資料很少。**
  - 婦癌專屬的預防性淋巴結對靜脈吻合：Jeong 2026[D-S 見清單]（Plast Reconstr Surg，**前瞻介入 26 人 vs 回溯對照 88 人**）：
    1 年水腫發生率 **8% vs 49%（P<0.001）**。**回溯對照、單中心、n 小，只能寫成「有一筆小型的對照研究」。**
  - **證據等級的誠實標法**：這一整塊**沒有隨機試驗**；統合分析合併的是單臂前後比較，異質性極高（I² 常 84–94%）。
    可寫「手術有一條路，回報的效果是周徑縮小兩到三成、蜂窩性組織炎次數每年少一到兩次；但這些數字全部來自沒有對照組的前後比較」。
- **抽脂（liposuction）＋控制性壓力治療**：Karlsson 2022[D-S52]（PRS Glob Open 2022;10:e4314，**n=124** 下肢淋巴水腫，
  術前中位追蹤 11 年、術後 5 年）：
  **術前 1,680 人年中 64 人共發生 335 次丹毒，發生率 0.20 次/人/年、期間盛行率 52%；術後 763 人年中 28 人共 53 次，
  發生率 0.07 次/人/年、期間盛行率 23%——丹毒發生率下降 65%（P<0.001）**；術前中位多餘體積 3,158 mL，中位減少 100%（P<0.0001）。
  **注意：這是晚期／脂肪化的水腫，且術後必須終身穿壓力衣。**

**(e) 蜂窩性組織炎／丹毒——急症面，要具體**
- **這是 D3 唯一「不能等到明天」的段落。**
- 風險的量級（**乳癌手臂資料，標籤必寫**）：Wagner 2026[D-S53]（Ann Surg Oncol 2026;33:1180–1188；單一機構 2000–2024，
  **2,920 位乳癌相關淋巴水腫病人**）：**231 人發生過蜂窩性組織炎（盛行率 7.9%），共 418 次；發生過的人中 39.0%（90/231）會再發**。
  血液培養 255 次中 33 次（12.9%）陽性，最常見菌種為 **無乳鏈球菌 Streptococcus agalactiae（8/33，24.2%）**。
  再發的獨立風險因子：**任何放療 HR 2.15（1.24–3.72）、腋下淋巴結廓清 HR 1.96（1.05–3.68）、從水腫診斷到第一次蜂窩性組織炎的時間愈短 HR 0.99（P<0.01）**。
- **下肢的量級**：Karlsson 2022[D-S52] 的術前基準線（下肢淋巴水腫、晚期）**期間盛行率 52%、0.20 次/人/年**——
  這是**晚期**族群，不可拿來代表一般術後病人。
- **丹毒會讓水腫本身變壞**：Li 2025[D-S 見清單]（Sci Rep 2025;15:5518，n=1,016 癌症相關續發性淋巴水腫抽脂後）：
  **既往丹毒是抽脂後復發最強的獨立風險因子（OR 3.98，95% CI 2.81–5.69）**。
- **可以寫的警訊清單（要具體）**：腿部突然出現界線不清的紅、熱、脹、痛，可能合併發燒與畏寒；範圍在數小時內擴大。
  **這種時候要當天就醫，不是等回診。** 一句指向 `care-fever`〈這一種發燒，不能等到天亮〉。
- **鑑別診斷的紅線**：**單側、突然、痛的腿腫，也可能是深部靜脈栓塞**——而內膜癌存活者的靜脈與淋巴系統疾病風險本來就高
  （SEER-Medicare：HR 2.71[D-S58]；猶他州世代 1–5 年血栓性靜脈炎與栓塞 HR 2.07[D-S59]）。
  **這一段必須一句指向 `care-thrombosis`〈小腿腫起來，可以等到明天嗎〉，並寫清楚「淋巴水腫是慢慢來的、雙側或單側都可能；
  突然一夜之間腫起來又痛，先當栓塞處理」。**

**(f) 與乳癌手臂水腫的差別（本篇的存在理由）**
- **一般原則不重寫，指向 `bc-lymphoedema`。** D3 只寫下肢特有的：
  1. **功能面**：手臂水腫影響的是提、抓、穿衣；下肢水腫影響的是**站、走、上下樓、久坐後起身**，直接影響工作與外出。
     677 位婦癌長期存活者（≥5 年，其中內膜癌 32.9%）的國際調查中，**仍有症狀者 36.9%，最常見的就是淋巴水腫 36.2%**[D-S71]。
  2. **生活品質的量化**：Leitao 2020[D-S36] 與 Glaser 2021[D-S37] 都顯示自述水腫者生活品質顯著較差；
     Bjørnholt 2025[D-S40] 進一步指出 12 個月時分數高者「negatively associated with the women's **daily activities, appearance, emotional
     functioning, and global quality of life**」。
  3. **壓力衣的實務差別（下肢特有）**：下肢壓力衣要靠手的握力穿脫。Tsukagoshi 2026[D-S 見清單]（Ann Vasc Dis 2026;19:26–30，
     婦癌術後續發性下肢淋巴水腫、ISL 晚期 II 期、**≥65 歲 71 人**）：
     **使用平織（flat-knit）襪者的握力顯著高於圓織（circular-knit）者（21.1 kg vs 19.1 kg，P=0.004）**；
     作者結論：只要握力維持，即使 75 歲以上仍能繼續使用平織襪。→ **「穿不上去」是真實且可以量到的障礙，要寫，而且要寫「穿不上就講，有輔助工具與不同織法」。**
  4. **鞋襪與旅行**：腳背與腳趾受累會改變鞋子尺寸；長途久坐（飛機、長途車）與下肢水腫的關係在文獻上**沒有內膜癌族群的隨機資料**，
     **不可寫「搭飛機一定要穿壓力衣」**，只能寫「長時間不動時多起來走、把腿墊高，這是通則不是證據」。
  5. **自我管理的落差是真的**：16 位婦癌下肢水腫病人的質性研究歸納出五個主題，包括「醫療資源分布不均」「支持不足」「居家自我管理技巧不足」
     「居家管理期間心理壓力大」[D-S 見清單，質性研究，不給數字]。

### 反方向的資料（誠實必列）

- **前哨淋巴結不能消除水腫**：Cibula 2021（子宮頸癌 n=150）在**只做前哨、不做骨盆廓清**的族群中，24 個月累積輕度水腫仍有 17.3%、中度 9.2%；
  作者結論逐字「The replacement of standard PLND by bilateral SLN biopsy … **does not eliminate the risk of mild to moderate LLL**」。
  Leitao[D-S36] 與 Glaser[D-S37] 的前哨組自述水腫也有 26–27%。
- **統合分析自己承認證據薄**：Helgers 2020[D-S41] 的三筆勝算比從 0.05 到 0.54，其中一筆 95% CI 跨過 1。
- **自我淋巴引流（SLD）預防無效**：Utsugi 2025[D-S46]，5 年累積發生率 SLD 組 37.5% vs 對照 23.5%（**方向甚至相反**，但非隨機且無顯著差異）。
- **衛教方案量不到腿變細**：Tümkaya 2026 隨機試驗（n=27）症狀與自我效能改善，**腿圍無顯著變化**。
- **外科的效果數字全部沒有對照組**（LVA／VLNT 統合分析，I² 84–94%）[D-S49][D-S51]。

### Claim ceiling（D3）

- **可寫**：
  - 「這個數字取決於怎麼量。同一批 235 個人用四種方法判定，得到的風險因子完全不同（淋巴廓清的勝算比從『看不出來』到 14.42）。」[D-S43]
  - 「做前哨淋巴結的人比做全面淋巴廓清的人少腫：MSK 27% vs 41%、Mayo 26% vs 49%、義大利 21% vs 45%、瑞典臨床判定 1.3% vs 18%。
    校正 BMI 與放療後，勝算比約 1.8 到 3.1 倍。」[D-S36][D-S37][D-S38][D-S39]
  - 「做過骨盆淋巴廓清的人，5 年累積發生率約四成（190 人前瞻、ISL 第 I 期以上），**第一年最多**。」[D-S45]
  - 「加做骨盆腔放療，自述水腫比例從 35% 上到 51%（OR 1.95）。」[D-S36]
  - 「壓力（繃帶／壓力衣）是主力；徒手淋巴引流是加分項，Cochrane 的合併效果是多減 7.11% 的多餘體積。」[D-S47]（標籤：乳癌手臂）
  - 「下肢專屬的物理治療只有 6 個隨機試驗、289 人，方向是有效、多模式優於單一模式、不良事件都是輕度。」[D-S48]
  - 「蜂窩性組織炎會再發（乳癌相關淋巴水腫世代中 39% 的人再發），而且會讓水腫本身變壞。突然的紅熱脹痛要當天就醫。」[D-S53][D-S 見清單]
- **不可寫**：
  - **「下肢淋巴水腫的機率是 X%」**——沒有那個數字。必須帶「誰、怎麼量、做了什麼手術、有沒有放療」四個標籤。
  - 「做前哨就不會腫」——前哨組仍有 21–27% 自述水腫[D-S36][D-S37][D-S39]。
  - 「自己做淋巴按摩可以預防」——5 年前瞻的隨機以外資料是**無效**[D-S46]；唯一正向的是非隨機自選世代[D-S56]。
  - 「減重可以治好淋巴水腫」——BMI 是相關因子，**沒有介入證據**。
  - 「氣壓治療有效／無效」——**查無可引用的下肢婦癌隨機資料**，寫「查不到」。
  - 「開刀可以治好」——LVA／VLNT 的數字全部來自無對照的前後比較。
  - **任何一句讓讀者自己判斷「我這個腫要不要看醫師」**——腿腫的鑑別診斷（復發、栓塞、蜂窩性組織炎、淋巴水腫）不是病人的工作。
  - 前哨 vs 廓清該不該做（歸 A4）；體重管理的健康效益（歸 C2）；放療技術與副作用（歸 `pel-*` 專題）。
- **與 SPEC 不同形狀的事已在開頭第 5、6、7 條標註。**

### Caveats／safety notes（D3，寫作者必寫）

1. **急症段要獨立成一個小節，不能藏在文字中間**：突然的單側紅腫熱痛 → 當天就醫（蜂窩性組織炎／丹毒）；
   突然的單側腫脹合併疼痛 → 先排除深部靜脈栓塞。指向 `care-fever` 與 `care-thrombosis`。
2. **第一年是關鍵窗口**[D-S45]，而 3 個月時的腫脹預測 12 個月仍在腫[D-S40]——所以「早一點講出來」是有依據的行動建議。
3. **量的方式要跟醫療團隊講好**：因為「量法決定結論」[D-S43]，病人自己在家用捲尺量會得到跟醫院不同的答案。
4. **壓力衣穿不上去是常見且可量化的問題**（握力）[D-S 見清單]——要寫「穿不上就講」，不要寫成病人不配合。
5. **不要把水腫寫成「一定會惡化」**：亞臨床異常者 24 個月內 50% 進展、但**另外一半沒有**[D-S54]；子宮頸癌世代中另有 22% 的暫時性腫脹在 6 個月內自行緩解。

### 台灣端（D3，這是本篇最重要的台灣段）

- **健保有「徒手淋巴引流」這一項，但條文寫的適應症是癌症末期。**
  《全民健康保險醫療服務給付項目及支付標準》現行給付項目全表（**1140501 生效版，6,013 項**，自政府資料開放平臺資料集 9405 下載官方 ODS
  並解壓 `content.xml` 逐列檢索）[D-S72]：
  > **47091B　淋巴水腫照護-徒手淋巴引流(須達四十分鐘)　450 點　（生效 2022/03/01）**
  > 備註逐字：「**1.適應症：癌症末期淋巴水腫病人　2.執行人員：須接受淋巴照護相關訓練。執行完成後需有適應症、執行過程及執行時間的紀錄。
  > 3.提升兒童加成項目。**」
  → **寫法（不可推論）**：「健保表上確實有一項『淋巴水腫照護－徒手淋巴引流』，450 點，條文寫的適應症是『癌症末期淋巴水腫病人』。
  一個手術做完、腫起來的早期病人算不算，這一條字面上沒有寫。**要不要申報、能不能申報，問醫務課或個管師。**」
- **同一份全表的其他檢索結果（全部是逐字檢索的負面發現，可以寫「查不到列項」）**[D-S72]：
  - 「壓力衣」「彈性衣」「彈性襪」：**零筆**。
  - 「氣壓」：只有 17002B 最大吸氣壓及最大吐氣壓、23305C 氣壓式眼壓測定，**與淋巴水腫無關**。
  - 「淋巴水腫」：除 47091B 外**零筆**。
  - **復健治療的既有項目**（可寫，但要說清楚它們不是為淋巴水腫設的）：
    42016C 物理治療評估 240 點（同一病患治療期間一個月限申報一次；同一治療期間超過三個月者不予支付）；
    42017C 中度治療－中度 265 點、42018C 中度治療－複雜 400 點——其治療內容代碼列表逐字包含「**PTM 11.按摩 Massage**」與水療、牽拉、運動治療等，
    **但整份條文沒有出現「淋巴引流」或「淋巴水腫」字樣**；42019C 複雜治療 500 點（PTC 1–7，無淋巴相關項目）。
    43026C 職能治療評估 240 點、45031C 一般職能治療 299 點、45095C 特殊職能治療 325 點。
    → **可寫**：「復健科有物理治療的給付項目，其治療內容代碼裡有『按摩』，但條文裡沒有『淋巴引流』這四個字。實際怎麼申報，問你的復健科與醫務課。」
- **壓力衣／彈性襪在身心障礙輔具補助也查不到。**
  《身心障礙者輔具費用補助辦法》（法規代碼 D0050060，全國法規資料庫）第 2 條列的補助類別逐字為
  「一、個人行動輔具。二、溝通及資訊輔具。三、身體、生理與生化試驗設備及材料。四、身體、肌力及平衡訓練輔具。五、預防壓瘡輔具。
  六、住家家具及改裝組件。七、個人照顧及保護輔具。八、居家生活相關輔具。九、矯具及義具。十、其他輔具。」；
  補助比率「一、低收入戶：最高補助金額之全額。二、中低收入戶：最高補助金額之百分之七十五。三、前二款以外之一般戶：最高補助金額之百分之五十。」；
  「輔具補助，每人每二年度以補助四項為原則。」
  其**附表〈身心障礙者輔具費用補助基準表〉PDF（751,186 bytes，`pdftotext -layout` 後 4,584 行）逐字檢索
  「壓力衣」「彈性衣」「彈性襪」「淋巴」「水腫」——全部零筆**[D-S77]。
  → **寫法**：「壓力衣有沒有補助？我把健保支付標準全表和身心障礙輔具補助基準表都下載下來逐字搜過，這兩份文件裡查不到列項。
  各縣市另有自訂的加碼項目（辦法第 7 條明訂『直轄市、縣（市）主管機關得考量財務狀況，增列補助項目，或調高最高補助金額』），
  **要問你戶籍地的社會局與醫院社工**。」**永不推論有無給付。**
- **重大傷病**：子宮體癌（C54）屬附表一第一項第(五)款「除(一)-(四)之其他惡性腫瘤」，**證明有效期限 5 年**；
  效期屆滿**三個月前**重新申請可銜接效期，逾期則以提出申請之日為生效日[D-S73]。其他可辦的證明一句指向 `sit-paperwork`。
- **gap**：
  - 台灣本土的**下肢淋巴水腫發生率**（婦癌術後）**查無可引用的官方統計**。
  - **氣壓治療（間歇性氣壓壓縮）在健保表中查無列項**，也查不到自費公告價格——**不寫價格**。
  - 淋巴靜脈吻合／淋巴結移植在台灣的**給付狀態查不到列項**（全表無相關項目名稱）；自費金額不查不寫（費用紀律；想問怎麼問 → `care-self-pay`）。

### 給繪圖組的數字（D3）

- **一張「同一件事、四種量法」的圖**（本篇最有價值的圖）：Wedin 2021 的淋巴廓清 aOR——
  **原始體積：看不出來｜臨床分級 2.11｜病人自覺 2.51｜BMI 標準化體積 14.42**[D-S43]。
- **前哨 vs 全面廓清的四組對照條**（每組標判定方式）：
  1.3% vs 18.1%（臨床判定，n=188）[D-S38]｜26.0% vs 49.4%（13 題問卷，n=378）[D-S37]｜27% vs 41%（13 題問卷，n=599）[D-S36]｜
  21.4% vs 44.6%（問卷，n=239）[D-S39]｜7.0% vs 34.4%（LELQ，n=97）[D-S55]。
- **時間軸**：5 年累積 39.6%，**第一年最高**；taxane 化療 51.6%、摘除 ≥60 顆淋巴結 49.1%（n=190）[D-S45]。
- **放療加成**：外照射 51%（23/45）vs 無 35%（170/487），OR 1.95[D-S36]。
- **治療的效果量**：壓力繃帶單獨 30–38.6% 體積減少，＋MLD 再 +7.11%[D-S47]（標籤：乳癌手臂）。
- **蜂窩性組織炎**：乳癌相關淋巴水腫 2,920 人中盛行率 7.9%、再發 39.0%[D-S53]；晚期下肢淋巴水腫抽脂前 0.20 次/人/年、期間盛行率 52%[D-S52]。

---

## D4 `em-daily`〈治療結束之後的日常〉

> **這一篇的結構是「一站式轉診台」**：每一塊都給一段可引的證據＋一句指路。
> 荷爾蒙→C4；體重與代謝的病因學→C2；性生活與擴張器→`cx-dilator-sex`；心理與復發恐懼→`care-fear`；
> 骨質→C4；淋巴水腫→D3；追蹤→D1；免疫／化療→B5／B3。**D4 不重寫任何一塊。**

### Key facts

**(a) 這個族群的死因分布——D4 的立論基礎**

- **Xue 2023**[D-S57]（Cancer Med 2023;12:10917–10930；SEER 2000–2015，**n=135,831**）：
  追蹤期間 **46,604 人死亡（34.3%）**；死因分布 **內膜癌 42.9%、其他癌症 15.6%、非癌症死因 41.5%**。
  「As the diagnosis time increased, **the number of EC-associated mortalities gradually decreased**.」
  最常見的非癌症死因：**心臟病、腦血管疾病、糖尿病**。
  對比美國一般人口的標準化死亡比（有統計意義者）：**心臟病 SMR 1.06（95% CI 1.03–1.09）、糖尿病 1.56（1.47–1.65）、敗血症 1.40（1.28–1.52）**。
  作者結論逐字：「For patients with EC, **the number of deaths from non-cancer causes (mainly heart disease, cerebrovascular disease and
  diabetes mellitus) is equivalent to that of EC.**」
- **罹病端（不是死亡端）的訊號更強**：
  - Anderson 2022[D-S58]（Gynecol Oncol 2022;167:51–57；SEER-Medicare，66 歲以上，2004–2017，**內膜癌 44,386 人 vs 配對無癌 221,219 人**）：
    指標日時內膜癌組的心血管疾病盛行率就比較高；從指標日後 1 年開始追蹤，**缺血性心臟病 HR 1.73（95% CI 1.69–1.78）、
    肺源性心臟病 HR 1.95（1.88–2.02）、靜脈與淋巴系統疾病 HR 2.71（2.64–2.78）**。
  - Soisson 2018[D-S59]（J Natl Cancer Inst 2018;110:1342–1351；猶他州，1997–2012，**2,648 人 vs 10,503 配對**）：
    **1–5 年：靜脈炎／血栓性靜脈炎／栓塞 HR 2.07（99% CI 1.57–2.72）、肺源性心臟病 HR 1.74（1.26–2.40）、心房顫動 HR 1.50（1.07–2.11）**；
    5–10 年仍有部分風險殘留。相對於只開刀者，**再加放療和／或化療者在 1–5 年心臟與循環系統疾病風險增加**。
    作者結論：「increased monitoring for cardiovascular diseases may be necessary for endometrial cancer patients **for 10 years after cancer diagnosis**」。
- **反方向（必列）**：Felix 2017[D-S60]（Cancer Causes Control 2017;28:1043–1051；Iowa Women's Health Study 1986–2011，
  **552 位內膜癌 vs 2,352 位年齡與 BMI 配對的無癌對照**）：
  **內膜癌組的心血管死亡率反而較低（HR 0.75，95% CI 0.56–0.99）**，全因死亡率較高（HR 1.50，1.30–1.74）。
  作者自己說需要更多校正良好的大型研究。
  → **D4 的寫法**：「不是『得過內膜癌讓你更容易死於心臟病』（有反方向資料）。是『這個病和心臟病、糖尿病共用同一批風險因子，
  所以治療結束之後，真正該回去顧的常常是這些』。」ESGO 2025 的原文直接支持這個框架：
  「Follow-up should include assessment of physical (eg, **cardiovascular comorbidities and secondary cancers**) and mental health (V, A)」[D-S1]。
- **病人自己怎麼看**：DeMari 2023[D-S 見清單]（Gynecol Oncol 2023;174:208–212；NCORP WF-1804CD 試驗基線，**n=55**）：
  **87% 同意心臟病對自己的健康是風險、76% 同意腫瘤科醫師應該談心臟健康、84% 表示準備好採取行動**；
  但實測 AHA Simple 7 的成績是 **血壓 95%、BMI 93%、空腹血糖/A1c 60%、飲食 60%、運動 47%、總膽固醇 53% 落在中／差**；
  **16% 過去一年沒看過家醫科，而這些人比較常回報經濟困難（22% vs 0%，P=0.02）**。
  → 這一段可以直接用：**「這件事你們自己都知道，缺的是有人幫你把它排進行程」**，並自然接到「回去看家醫科／代謝科」的行動建議。

**(b) 運動與存活／復發——方向清楚、強度只到觀察性**

- **最強的一筆（前瞻世代，但仍是觀察性）**：Friedenreich 2020[D-S61]（J Clin Oncol 2020;38:4107–4117；
  Alberta，2002–2006 診斷的**侵襲性內膜癌 425 人**，追蹤到 2019，中位追蹤 **14.5 年**；訪員施測 Lifetime Total Physical Activity Questionnaire，
  診斷前活動於診斷後中位 4.4 個月訪談、診斷後活動於中位 3.4 年訪談；校正年齡、期別、分化度、治療、BMI、停經狀態、荷爾蒙治療、家族史、共病）：
  - 事件數：**60 人死亡（其中內膜癌死亡 18 人）、80 個無病存活事件**。
  - **診斷後**休閒身體活動（>13 vs ≤5 MET-小時/週/年）：**無病存活 HR 0.33（95% CI 0.17–0.64，P_trend=.001）；總存活 HR 0.33（0.15–0.75，P_trend=.007）**。
  - **診斷前**（>14 vs ≤8）：無病存活 HR 0.54（0.30–0.96，P_trend=.04）；總存活 HR 0.56（0.29–1.07，P_trend=.06，**未達顯著**）。
  - 從診斷前到診斷後**都維持高活動量**者：無病存活 HR 0.35（0.18–0.69）、總存活 HR 0.43（0.20–0.94）。
  - **注意分母**：60 個死亡、80 個事件——**這是小樣本的觀察性資料，效應量看起來很大正是小樣本的特徵。**
- **同一個世代、更長追蹤、方向變複雜（必列的反方向）**：Oh 2026[D-S62]（Int J Cancer 2026;159:345–358；
  同一個 Alberta 世代擴大到 **n=527**，追蹤 16.7 年，128 人死亡、194 個無病存活事件；依主要治療分層：**單純手術 333 人 vs 手術＋輔助治療 194 人**）：
  - **交互作用顯著（P=.035）**：診斷前達到活動指引在**單純手術**組與較少事件相關，在**手術＋輔助治療**組卻與**較多**事件相關。
  - 作者結論逐字：「Associations between PA and survival may differ by primary treatment, with **generally protective associations in the
    surgery alone group, but harmful associations in the surgery plus adjuvant therapy** group.」
  - → **這一筆必須寫。** 它不是「運動有害」——最可能的解釋是**混淆與反向因果**（需要輔助治療者本來就期別高、活動能力也不同）；
    但它把「運動延長存活」這句話從「證據明確」拉回「觀察性、且在不同族群方向不一致」。
- **另一筆前瞻世代（方向弱）**：Bates-Fraser 2025[D-S63]（Cancer Causes Control 2025;36:1743–1752；Cancer Prevention Study-II，
  **n=1,016** 內膜癌存活者，平均診斷年齡 72 歲、平均追蹤 13.5 年、511 人死亡）：
  相對於零中高強度活動，**達到指引兩倍者的全因死亡 HR 0.71（95% CI 0.50–1.00）——剛好觸及顯著邊界**，總癌症死亡無關聯；
  奇怪的是「每週步行 <2 小時」相對「完全不走」的全因死亡 HR 1.45（1.08–1.96）（作者未解釋，很可能是反向因果）；
  久坐時間與存活無關。作者結論：「further research is needed in larger/pooled cohorts with more cancer deaths」。
- **更早的一筆（BMI 有關、運動無關）**：Arem 2016[D-S 見清單]（Cancer Causes Control 2016;27:1403–1409；NIH-AARP，**n=580**，
  中位追蹤 7.1 年、91 人死亡）：診斷後 BMI 與死亡率正相關（校正腫瘤與人口學後）；
  **中高強度活動（15+ vs 0 MET-小時/週）HR 0.72（95% CI 0.43–1.21，非顯著）**；
  進一步校正生活型態與健康狀態後 BMI 的關聯被削弱（HR 1.47，0.71–3.07），而**看電視 5+ vs <3 小時/天 HR 2.28（1.05–4.95）變強**。
- **隨機介入試驗只到「可行性」與「行為改變」，沒有一個以存活為終點**：
  - **Zamorano 2021（隨機、陰性）**[D-S64]（Gynecol Oncol 2021;162:770–777；肥胖（BMI ≥30）的內膜癌存活者 **n=80** 隨機，
    個人化簡訊行為減重介入 vs 加強版常規照護；主要終點 6 個月體重）：
    **兩組體重變化無差異（P=0.08）**；生活品質、身體活動、身體形象亦無差異。
    更重要的是：**參加試驗的人與沒參加的 278 人體重變化也一樣（P=0.85）；6 個月時參加者 47.7% vs 未參加者 44.4% 體重反而增加，
    減掉至少 5% 體重的分別只有 9.2% 與 11.2%。**
    作者結論逐字：「This text-message-based intervention **did not increase weight loss** among endometrial cancer survivors with obesity,
    nor did participation in the trial.」
  - **Maxwell-Smith 2019（隨機、陽性但終點是行為）**[D-S 見清單]（Psychooncology 2019;28:1420–1429；有心血管風險且活動不足的
    **大腸直腸癌與內膜癌存活者 n=68** 隨機，穿戴裝置＋行動計畫 12 週）：
    **介入組中高強度活動每週增加 45 分鐘，對照組減少 21 分鐘（組別×時間交互作用 F₁,₁₂₆=5.14，P=0.025）**；
    有舒張期高血壓者介入組淨降 9.89 mmHg（F₁,₆₆=4.89，P=0.031）。
  - **Koutoukidis 2019（隨機試驗性）**[D-S67]（IJGC 2019;29:531–540；英國 2 家醫院，第 I–IVA 期無病內膜癌存活者，
    篩 296 人收 60 人、隨機 54 人（介入 29／常規 31），8 週團體健康飲食＋身體活動）：
    8 週時**飲食品質改善（Alternative Healthy Eating Index 2010 差異 7.5，95% CI 0.1–14.9，P=0.046）**，
    **身體活動無差異（0.1 MET-小時/日，95% CI −1.6 至 1.8，P=0.879）**、整體生活品質無差異；**24 週時整體生活品質改善（差異 8.9，0.9–16.8，P=0.029）**。
    介入遵從率 77%，無介入相關不良事件。
  - **Smits 2022（單臂可行性）**[D-S66]（Cancers 2022;14:5579；英國，術後 6 週起 10 週個人教練課程；54 人符合、**22 人（41%）同意**）：
    出席率 86%、無不良事件；角色功能（P=0.02）、情緒功能（P=0.02）、認知功能（P=0.04）、內臟脂肪百分比（P=0.039）、
    六分鐘走路測試（P<0.001）皆顯著改善；**最大減重 3 個月 6.0 kg、6 個月 8.4 kg**。
- **減重與存活／復發：目前是陰性**：Santana 2024[D-S65]（Oncol Lett 2024;27:44；西班牙，2007–2019，
  **早期第 I 型內膜癌、過重或肥胖 n=526**，過重 152（28.90%）／肥胖 374（71.10%），中位追蹤 76.17 個月、77 人（14.64%）死亡）：
  存活者診斷時體重 86.4±17.9 kg → 治療後 1 年 84.6±16.4 kg（平均減 1.47 kg，P<0.001）；非存活者 84.7±15.7 → 84.7±14.6（減 0.63 kg，P=0.180）。
  比較「維持或增加 ≥5%」與「減少 ≥5%」：**全世代與全追蹤期間沒有顯著差異**；只有在**校正到 32–98 個月這個區間**時減重 ≥5% 者存活較高（P=0.025，log-rank）。
  **多變項：12 個月的體重變化不是總存活的顯著因子，校正後 HR 1.01（95% CI 0.97–1.05，P=0.723）。**
- **→ D4 對運動與體重的 claim ceiling（見下）：方向可以寫、強度只到觀察性、隨機介入試驗連「讓人減重成功」都還沒做到。**

**(c) 性功能與陰道狹窄——擴張器的證據等級是「Cochrane 找不到任何一個可納入的試驗」**

- **Cochrane（Miles & Johnson 2014）**[D-S68]（Cochrane Database Syst Rev 2014;(9):CD007291）：
  搜尋 CENTRAL 2013 Issue 5、MEDLINE 1950–2013、EMBASE 1980–2013、CINAHL 1982–2013。
  > 「**We found no trials and therefore analysed no data.**」「We identified **no studies for inclusion** in the original review or for this update.」
  被排除但作者認為值得討論的研究包括：一個隨機試驗顯示**鼓勵婦女做擴張器治療並沒有改善性功能分數**；一個小型隨機試驗顯示放療期間擴張與震動治療沒有差別；
  「Three recent studies showed **less stenosis associated with prophylactic dilation after radiotherapy**.」
  > 作者結論逐字：「**There is no reliable evidence to show that routine, regular vaginal dilation during radiotherapy treatment prevents
  > stenosis or improves quality of life.** Several observational studies have examined the effect of dilation therapy after radiotherapy.
  > They suggest that **frequent dilation practice is associated with lower rates of self reported stenosis. This could be because dilation is
  > effective or because women with a healthy vagina are more likely to comply with dilation therapy instructions** compared to women with
  > strictures. We would normally suggest that a RCT is needed to distinguish between a casual and causative link, but pilot studies highlight
  > many reasons why RCT methodology is challenging in this area.」
  2010 版[D-S68 同條目 pub2]另有安全警語逐字：「**Dilation during or immediately after radiotherapy can, in rare cases, cause damage**」
  「Routine dilation during or soon after cancer treatment **may be harmful**」「Gentle vaginal exploration might separate the vaginal walls
  before they can stick together and some women may benefit from dilation therapy **once inflammation has settled**」。
- **內膜癌專屬、且是本專題可用的一筆**：Noorian 2024[D-S69]（J Pers Med 2024;14:838；術後內膜癌、外照射後接陰道殘端近接治療，**n=131**，
  中位追蹤 60 個月；Group-1 65 人單次 7 Gy、Group-2 66 人在 68 Gy EQD2(α/β=3) 的 2 cm³ 劑量限制下給 5.5–7.0 Gy）：
  **陰道殘端復發率 1/131（0.8%）**；晚期陰道併發症 **Group-1 55.4%（36/65）vs Group-2 25.8%（17/66），P=0.003**；
  **多變項：屬於 Group-1（HR 1.99，P=0.021）與「擴張器使用少於 9 個月」（HR 3.07，P=0.010）是晚期陰道併發症的獨立預後因子。**
  → **可寫**：「有一筆 131 人的內膜癌資料顯示，擴張器用滿 9 個月以上的人，晚期陰道副作用比較少（風險約差三倍）。**這是回溯性的關聯，
  不是隨機試驗。**」
- **遵從率的現實**：Tahseen 2023[D-S70]（Ecancermedicalscience 2023;17:1545；巴基斯坦單一機構，內膜癌 24 人／子宮頸癌 30 人，共 **n=54**；
  放療結束 1 個月後開始衛教、3 個月後評估）：
  **整體遵從率 36/54（66.6%）**；每週 2–3 次 22 人（40.7%）、每週 <2 次 8 人（14.8%）、每月 1 次 6 人（11.9%）、**完全沒用 18 人（33.3%）**；
  內診發現黏膜正常 32 人（59.3%）、有沾黏 20 人（37.0%）、2 人（3.7%）因沾黏緊密無法檢查。
  **36 位有使用者中 29 人（80.6%）判定有效；照處方每週 2–3 次者的有效比例 72.4%（21/29）。**
- **一句指路**：擴張器怎麼用、什麼時候開始、性生活怎麼談 → **`cx-dilator-sex`〈擴張器、性生活——沒人願意先開口的那題〉。D4 不重寫。**
- **荷爾蒙（含局部雌激素）→ C4，D4 一個字都不展開。**

**(d) 長期存活者實際還在困擾什麼（給讀者「不是只有我」的量化）**

- **Woopen 2026**[D-S71]（Cancers 2026;18:1647；NOGGO／ENGOT／GCIG 國際調查，2019–2025，四國，**n=677** 婦癌長期存活者，
  定義為診斷後存活 ≥5 年；中位年齡 64 歲、中位存活 7 年；**內膜癌佔 32.9%**、子宮頸癌 46.6%、卵巢癌 4.4%、其他 16.1%）：
  - **36.9% 仍有身體或心理症狀**，最常見依序：**淋巴水腫 36.2%、熱潮紅 22.4%、注意力困難 21.1%、疲倦 20.9%、陰道乾澀 20.1%、尿失禁 18.9%**。
  - 整體健康自評（1 很好–5 很差）中位數 2；**13.5% 自評為差或很差**。目前有症狀與較差健康自評（P<0.001）及有過復發（P=0.001）相關。
  - **13.6% 回報完全沒有接受追蹤照護。**
  - 追蹤內容偏離指引：內膜癌存活者 **28.9% 仍在驗 CA-125、50.5% 仍在做 Pap 追蹤**。
  - 生活型態：**33.7% 完全不運動或每週運動不到 1 小時、13.4% 抽菸、51.2% 每月飲酒超過一次。**
  - 作者結論逐字：「Our findings highlight the need for patient-centred follow-up care, addressing both long-term side effects and education on
    lifestyle and prevention. **Follow-up procedures that do not follow guidelines should be avoided.**」

**(e) 回工作／照護模式**

- **可引的只有一筆間接資料**：Johnson & Choy 2022[D-S 見清單]（Arch Gynecol Obstet 2022;305:431–437；英國單中心服務評估，
  **n=98** 低風險類內膜第 1 期內膜癌轉入病人自主啟動追蹤（PIFU）；中位追蹤 54 個月）：
  **追蹤期間無復發證據**；病人回饋顯示運動課程幫助降低 BMI，超過三分之一覺得比較快樂、五分之一覺得更有自信也更能應付壓力；
  **91% 願意推薦這種追蹤模式**；成本相對傳統醫院追蹤**節省約 96.5%**。
  → **只能寫成「英國有醫院把低風險病人轉成病人自主啟動追蹤、把省下來的門診換成運動課程，服務評估顯示病人接受度高」**，
  **不可寫成「台灣也可以這樣」或「這樣比較安全」**（n=98、無對照、服務評估）。
- **「回工作」本身**：**本 brief 查無內膜癌族群的回工作率／時間的可引用量化資料 → gap。**
  文章只能寫「這一塊沒有好的數字」，並把重點放在具體障礙：下肢水腫影響久站與久坐[D-S71]、疲倦 20.9%、注意力困難 21.1%[D-S71]。
- **心理與復發恐懼 → 一句指向 `care-fear`〈療程結束了，為什麼更怕了〉。D4 不重寫。**
  可用的量化錨點只有一句：長期存活者中 21.1% 有注意力困難、20.9% 疲倦，且有症狀者健康自評顯著較差（P<0.001）[D-S71]。

### 反方向的資料（誠實必列）

- **運動**：Oh 2026[D-S62] 在同一個世代、更長追蹤下發現**手術＋輔助治療組的方向相反**（交互作用 P=.035）；
  Bates-Fraser 2025[D-S63] 的效果只到 HR 0.71（95% CI 0.50–1.00，觸邊）；Arem 2016 的運動關聯**非顯著**。
- **減重**：Santana 2024[D-S65] 多變項下 12 個月體重變化與總存活**無關**（HR 1.01）；
  Zamorano 2021[D-S64] 的隨機介入**沒有讓人減重成功**，而且**半數的人在 6 個月時體重是增加的**。
- **心血管**：Felix 2017[D-S60] 顯示以 BMI 配對後內膜癌組的心血管死亡率**較低**。
- **擴張器**：Cochrane **一個可納入的試驗都沒有**[D-S68]，且明說放療期間或剛結束就開始擴張**可能有害**。

### Claim ceiling（D4）

- **可寫**：
  - 「這個癌別的死亡，非癌症死因佔了約四成（SEER 135,831 人中 41.5%），其中最多的是心臟病、腦血管疾病、糖尿病。」[D-S57]
  - 「治療結束之後真正要顧的常常是血壓、血糖、血脂——而且病人自己也知道（87% 同意心臟病是風險），缺的是有人幫忙排進行程。」[D-S57][D-S 見清單 DeMari]
  - 「診斷後有規律休閒運動的人，長期追蹤下的無病存活與總存活比較好（HR 約 0.33）——**這是 425 人、60 個死亡的觀察性資料，不是隨機試驗**；
    同一個世代追蹤更久之後，在做過輔助治療的那一組方向甚至相反。」[D-S61][D-S62]
  - 「減重跟『不再復發』之間，目前沒有證據撐得起因果——多變項下 12 個月的體重變化與存活無關；而唯一的隨機減重介入試驗連讓人瘦下來都沒做到。」[D-S65][D-S64]
  - 「運動介入試驗做得出來的是：活動量增加（每週多 45 分鐘）、舒張壓下降、生活品質改善、內臟脂肪下降、六分鐘走路變好。**終點不是存活。**」
    [D-S 見清單 Maxwell-Smith][D-S66][D-S67]
  - 「擴張器：Cochrane 找不到任何一個可納入的隨機試驗；觀察性研究顯示常做的人自述狹窄比較少，但那也可能是因為陰道狀況好的人才做得下去。」[D-S68]
  - 「有一筆 131 人的內膜癌資料顯示擴張器用滿 9 個月以上，晚期陰道副作用較少（HR 3.07）——回溯性。」[D-S69]
  - 「五年以上的長期存活者裡，還有 36.9% 有症狀，最多的是淋巴水腫（36.2%）、熱潮紅、注意力困難、疲倦、陰道乾澀、尿失禁。」[D-S71]
- **不可寫**：
  - **「運動可以降低復發／延長存活」**（只能寫「觀察性資料指向這個方向，強度到此為止，而且有一筆反方向」）。
  - **「瘦下來就不會復發」**——這是紅線 8 的鏡像，D4 一樣不可越線；發生率端與復發／存活端是兩件事，且**復發／存活端目前是陰性**。
  - **「一定要用擴張器」或「不用擴張器會狹窄」**——Cochrane 是零試驗，且警告太早開始可能有害。
  - **任何劑量式的運動處方**（每週幾分鐘、什麼強度）寫成醫囑——只能引「ESGO：Lifestyle counselling in physical activity, a well-balanced diet,
    healthy weight, and smoking cessation should be routinely offered (V, A)」[D-S1]，並寫「怎麼開始，問你的醫療團隊」。
  - **荷爾蒙補充的任何一句**（歸 C4）；**骨質的數字**（歸 C4）；**局部雌激素**（歸 C4）。
  - **免疫治療／化療的療效數字**（歸 B5／B3）。
  - 台灣的自費金額、保險理賠金額（費用紀律；怎麼問自費 → `care-self-pay`）。

### Caveats／safety notes（D4）

- **擴張器不要在放療期間或剛結束時開始**：Cochrane 2010 版逐字「Dilation during or immediately after radiotherapy **can, in rare cases,
  cause damage**」「Routine dilation during or soon after cancer treatment **may be harmful**」「some women may benefit from dilation therapy
  **once inflammation has settled**」[D-S68]。**開始的時機一定要問放腫科醫師**，然後指向 `cx-dilator-sex`。
- **「多做運動」不可寫成對還在治療中或有共病者的通用建議**——Oh 2026 的交互作用[D-S62] 提醒不同族群方向可能不同；
  文章要寫「開始之前先跟你的醫師確認可以做到哪裡」。
- **13.6% 的長期存活者根本沒在追蹤**[D-S71]——這是 D4 收尾要回頭扣住 D1 的地方：追蹤的價值不是延長存活，是**共病、第二原發癌與心理**（ESGO V, A）[D-S1]。
- 出現新症狀（尤其陰道出血、單側腿腫、持續咳嗽、體重下降）→ 不要等下次回診，指向 D1 的症狀清單與 `care-thrombosis`／`care-fever`。

### 台灣端（D4）

- **重大傷病證明**：子宮體癌（C54）屬附表一第一項第(五)款，**效期 5 年**；**效期屆滿三個月前**重新申請可銜接，逾期則以申請日為生效日；
  原疾病經重新審查不符者不再發給[D-S73]。
  免自行負擔的範圍（第 6 條）逐字：「一、重大傷病證明所載傷病，或經診治醫師認定與該傷病相關之治療。二、因重大傷病門診，當次由同一醫師併行其他治療。
  三、因重大傷病住院須併行他科治療，或住院期間依病情需要，併行重大傷病之診療。」[D-S73]
  **其他可以辦的（身心障礙、經濟補助、保險）→ 一句指向站上 `sit-paperwork`〈重大傷病之外還能辦什麼〉。**
- **官方的社會資源入口（抓得到官方頁）**：衛生福利部焦點新聞〈癌症資源中心 實體與網路服務並進 癌症照護新時代 抗癌路上不孤單〉逐字[D-S76]：
  「**國民健康署補助癌症希望基金會共同協助推動 104 家醫院成立「癌症資源中心」**，讓癌友及其家人能夠獲得**資訊提供、心理支持及資源取得**等
  3 大重要因素之相關服務，透過實體與網路雙管齊下方式，**迄今共服務 150 萬人次**。」
  同頁提供的官方連結：**台灣癌症資源網 https://www.crm.org.tw/**（本 session 實測 HTTP 200，站名「台灣癌症資源網」）[D-S76]；
  另附「癌症資源中心名單」與「線上諮詢」短網址（短網址為第三方轉址，**引用時只寫官方新聞稿與 crm.org.tw**）。
  同一篇新聞稿另可引的數字：「國人癌症 5 年存活率已從民國 92-96 年的 50%，提升到民國 105-109 年的 **61.5%**」（**全癌症，不是子宮體癌**，
  引用時務必標明）[D-S76]。
- **子宮體癌在台灣的位置**：112 年女性標準化發生率**第 5 位**，男女合計新發生人數**第 10 位**，**發生年齡中位數 57 歲**[D-S74]。
- **淋巴水腫相關給付與壓力衣**：見 D3 台灣端（47091B 適應症為癌症末期；壓力衣／彈性襪在健保表與輔具補助基準表**皆查無列項**）[D-S72][D-S77]。
- **gap（查不到，一律標 gap，不推論）**：
  - **台灣子宮體癌依期別的五年存活率**：`hpa.gov.tw` TLS 憑證鏈驗證失敗、`tcr.cph.ntu.edu.tw` 連線重置，衛福部鏡像新聞稿無期別存活表。
  - **回工作率／病假期間的官方統計**：查無。
  - **癌症希望基金會官方網站**（`www.ecancer.org.tw`）本 session 直接抓取回 **HTTP 403**；
    → 可引用的官方路徑改走衛福部新聞稿[D-S76] 與台灣癌症資源網 crm.org.tw。
  - **商業保險理賠**：不在官方文件範圍，**不寫**。

### 給繪圖組的數字（D4）

- **死因圓餅（SEER n=135,831，死亡 46,604）**：**內膜癌 42.9%／其他癌症 15.6%／非癌症 41.5%**；
  非癌症前三：心臟病、腦血管疾病、糖尿病；SMR 心臟病 1.06、糖尿病 1.56、敗血症 1.40[D-S57]。
- **長期存活者仍有的症狀（n=677，內膜癌佔 32.9%）**：**淋巴水腫 36.2%、熱潮紅 22.4%、注意力困難 21.1%、疲倦 20.9%、
  陰道乾澀 20.1%、尿失禁 18.9%**；**36.9% 仍有症狀、13.6% 沒有在追蹤**[D-S71]。
- **運動的證據階梯（一張「證據強度」圖）**：
  觀察性（n=425，14.5 年，60 死）**HR 0.33**[D-S61] → 同世代更長追蹤**方向依治療分層而異（交互作用 P=.035）**[D-S62] →
  隨機介入試驗的終點只到**每週多 45 分鐘活動、舒張壓降 9.89 mmHg**[D-S 見清單 Maxwell-Smith]、**飲食分數 +7.5**[D-S67] →
  **沒有任何一個以存活為終點的隨機試驗**。
- **減重的證據**：多變項 HR **1.01（0.97–1.05）**[D-S65]；隨機簡訊介入 6 個月**兩組無差異**、減重 ≥5% 者僅 9.2% vs 11.2%[D-S64]。
- **擴張器**：Cochrane **納入試驗數 = 0**[D-S68]；內膜癌回溯 n=131，**使用 <9 個月的晚期陰道併發症 HR 3.07（P=0.010）**、
  兩組晚期併發症 55.4% vs 25.8%（P=0.003）[D-S69]；實務遵從率 66.6%、完全沒用 33.3%[D-S70]。

---

## 來源清單（PASS / FAIL 逐條，含完整書目與查證路徑）

**共同查證路徑（期刊文獻）**：`curl https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:<PMID>&resultType=core&format=json`
→ 逐筆核對 title／journal／year／volume(issue)／pages／DOI／PMID／isOpenAccess，並自 `abstractText`（或 OA 全文 XML）逐字抄出所引用的每一個數字。
**引用進正文的每一個數字都在摘要或已取得的全文裡看得到。**

**編號慣例**：正文中出現的 **[D-S 見清單]** 指向下方「【D3 補充來源】」「【D4 補充來源】」兩個區塊裡的具名條目
（Hahn 2025、Jeong 2026、Tsukagoshi 2026、Li 2025、Cibula 2021、Tümkaya 2026、Zalawadia 2026、DeMari 2023、Maxwell-Smith 2019、
Arem 2016、Johnson & Choy 2022）——**這些同樣是 PASS，可以引用，書目在該區塊逐條列出**；
只有 **[D-S 未列]** 一處（Wedin 2025 淋巴腹水，即 [D-S44]）本 brief 未取用其數字。

### 一、指引（PASS）

- **[D-S1] PASS（官方 PDF 全文，2026-09-10 實下載；HTTP 200，2,817,386 bytes；`pdftotext -layout` 全文檢索）**
  Concin N, Matias-Guiu X, Cibula D, Colombo N, Creutzberg CL, Ledermann J, Mirza MR, Vergote I, Abu-Rustum NR, Bosse T, Chargari C,
  Espenel S, Fagotti A, Fotopoulou C, Gatius S, González-Martin A, Lax S, et al.
  **ESGO-ESTRO-ESP guidelines for the management of patients with endometrial carcinoma: update 2025.**
  *Lancet Oncol.* 2025;26(8):e423–e435. DOI: 10.1016/S1470-2045(25)00167-6. PMID: 40744042. OA: N（**但官方 PDF 公開掛在 ESGO 指引網站**）。
  官方 PDF: https://guidelines.esgo.org/media/2025/09/ESGO-ESTRO-ESP-Guidelines-for-EC_-LO-July-2025.pdf
  人類可讀頁面: https://guidelines.esgo.org/endometrial-cancer/guidelines/recommendations/
  Route: WebSearch → curl 指引頁 HTML → 取 PDF href → curl 下載 → pdftotext → grep Follow-up／Recurrent disease／Systemic therapy 原文逐字。
  引用內容：Follow-up 四句 V, A 建議（含「no evidence that follow-up visits improve overall survival」）；復發三分類與各自建議等級；
  寡轉移定義（1–5 顆、≤3 個部位，IV, B）；荷爾蒙治療在低惡性度 ER 陽性復發為首選（III, A）；多線治療的權衡句（IV, B）；
  病人賦權段（癌症篩檢、生活型態諮商 V, A）。

- **[D-S2] PASS（官方附錄 PDF 全文，2026-09-10 實下載；HTTP 200，`pdftotext -layout` 後 267,956 bytes 文字）**
  同上，**Appendix**（ESGO-ESTRO-ESP Guidelines for EC — Appendix, July 2025）。
  URL: https://guidelines.esgo.org/media/2025/09/Appendix-ESTO-ESTRO-ESP-Guideline-for-EC_-LO-July-2025-.pdf
  Route: 同 [D-S1]。引用內容：§5.11 Follow-up 證據摘要全段逐字；§5.9 Recurrent disease（含「DFS 73% at 3 years」的轉述、
  骨盆廓清術門檻句、再照射「longer time interval … lesions <4 cm … better outcome」）。

- **[D-S3] PASS（Europe PMC 全文 XML，OA）**
  Ramírez SP, Fidalgo AP, Ginesta MPB, De Juan Ferré A, Madrid LF, Martínez AG, Montosa FG, Madariaga A, Gómez TM, Gil-Martin M.
  **SEOM-GEICO clinical guidelines on endometrial cancer (2025).**
  *Clin Transl Oncol.* 2025;27(12):4368–4380. DOI: 10.1007/s12094-025-04046-1. PMID: 40986254. PMCID: PMC12630260. **OA: Y**
  Route: Europe PMC REST 檢索 → `curl https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12630260/fullTextXML` → 去標籤後檢索 "Follow-up"。
  引用內容：Table 1 的低／高風險追蹤間隔（皆 V, C）；「Serum biomarkers are not recommended, and vaginal cytology is not routinely
  recommended … [I, A]」；高風險非類內膜／III–IV 期影像建議（IV, A）；TOTEM 兩臂的實際內容與 12.3% 復發率；復發部位比例（約 50% 局部區域、
  25% 遠端、25% 兩者）；5 年後回歸一般族群檢查（V, B）。

- **[D-S4] PASS（僅摘要層級，引用限於摘要逐字）**
  Salani R, Atallah D, Fader AN, Frimer M, Obermair A, Pareja R, Huang M.
  **Updates to post-treatment surveillance after curative intent treatment for patients with gynecologic cancers: A Society of Gynecologic
  Oncology clinical practice statement.** *Gynecol Oncol.* 2026;204:109–117. DOI: 10.1016/j.ygyno.2025.11.014. PMID: 41308226. OA: N
  Route: Europe PMC REST（`TITLE:` 檢索 → EXT_ID 核對）。**全文未取得；只引摘要中的措辭，不引任何間隔數字。**

- **[D-S5] PASS（僅摘要層級）**
  Salani R, Khanna N, Frimer M, Bristow RE, Chen LM.
  **An update on post-treatment surveillance and diagnosis of recurrence in women with gynecologic malignancies: Society of Gynecologic
  Oncology (SGO) recommendations.** *Gynecol Oncol.* 2017;146(1):3–10. DOI: 10.1016/j.ygyno.2017.03.022. PMID: 28372871. OA: N
  Route: 同上。引用限摘要：「There is very little evidence that routine cytology or imaging improves the ability to detect gynecologic cancer
  recurrence that will impact cure or response rates to salvage therapy.」

- **[D-S6] PASS（書目層級）／措辭 FAIL**
  Salani R, Backes FJ, Fung MF, Holschneider CH, Parker LP, Bristow RE, Goff BA.
  **Posttreatment surveillance and diagnosis of recurrence in women with gynecologic malignancies: Society of Gynecologic Oncologists
  recommendations.** *Am J Obstet Gynecol.* 2011;204(6):466–478. DOI: 10.1016/j.ajog.2011.03.008. PMID: 21752752. OA: N
  → 已被 [D-S4][D-S5] 取代，**正文不引 2011 版**。

### 二、D1 追蹤（PASS）

- **[D-S7] PASS** Zola P, Ciccone G, Piovano E, Fuso L, Di Cuonzo D, Castiglione A, Pagano E, Peirano E, Landoni F, Sartori E, Narducci F,
  Bertetto O, Ferrero A, TOTEM Collaborative Group.
  **Effectiveness of Intensive Versus Minimalist Follow-Up Regimen on Survival in Patients With Endometrial Cancer (TOTEM Study):
  A Randomized, Pragmatic, Parallel Group, Multicenter Trial.** *J Clin Oncol.* 2022;40(33):3817–3827. DOI: 10.1200/JCO.22.00471. PMID: 35858170. OA: N
  引用：n=1,871 隨機／1,847 分析（60% 低風險）、42 院、中位追蹤 69 個月、**5 年 OS 90.6% vs 91.9%（HR 1.13，95% CI 0.86–1.50，P=.380）**、
  偵測復發 HR 1.17（0.92–1.48，P=.194）、結論句逐字。

- **[D-S8] PASS** Watanabe Y, Kobayashi E, Masuda T, Kakuda M, Nakagawa S, Hiramatsu K, Iwamiya T, Matsuzaki S, Nakatani E, Ueda Y.
  **The value of vaginal cytology for postoperative surveillance of endometrial cancer.** *Int J Clin Oncol.* 2025;30(10):2138–2147.
  DOI: 10.1007/s10147-025-02843-w. PMID: 40742697. OA: N
  引用：n=759、復發 85（11.2%）、含陰道成分 20（23.5%）、單一部位陰道 12（14.1%）／肺 11（12.9%）、**20 例陰道復發中 14 例靠症狀＋內診、
  僅 1 例單靠細胞學（2 個月後出現肉眼病灶）**、結論句逐字。

- **[D-S9] PASS（OA）** Lubrano A, Benito V, Pinar B, Molano F, Leon L.
  **Efficacy of Endometrial Cancer Follow-up Protocols: Time to Change?** *Rev Bras Ginecol Obstet.* 2021;43(1):41–45.
  DOI: 10.1055/s-0040-1721352. PMID: 33513635. PMCID: PMC10183951. **OA: Y**
  引用：復發 81 人（10.04%）、**2 年內 66.7%／3 年內 80.2%**、遠端 41.9%／局部區域 40.7%／淋巴 17.4%、**42% 有症狀**、
  偵測方式 症狀＋理學 54.3%／血清標記 29.6%／CT 9.9%／細胞學 6.2%、有無症狀存活無差異。

- **[D-S10] PASS（OA）** Nakamura K, Kitahara Y, Yamashita S, Kigure K, Ito I, Nishimura T, Azuma A, Kanuma T.
  **Reassessment of intensive surveillance practices adopted for endometrial cancer survivors.** *BMC Womens Health.* 2022;22(1):355.
  DOI: 10.1186/s12905-022-01937-1. PMID: 35999573. PMCID: PMC9396785. **OA: Y**
  引用：n=847、復發 88、**75% 無症狀**、密集追蹤協定內容、局部復發是多變項中唯一顯著因子、遠端轉移者有無症狀存活無差異、結論句。

- **[D-S11] PASS（OA）** Knox MC, Salkeld A, Brand A, Herbst U, Chard J, Thiruthaneeswaran N.
  **Value of Routine Pelvic Examination in the Follow-Up of Patients Receiving Adjuvant Radiation Therapy for Endometrial Cancer:
  An Australian Tertiary-Centre Experience.** *J Med Imaging Radiat Oncol.* 2025;69(4):531–539. DOI: 10.1111/1754-9485.13864.
  PMID: 40334278. PMCID: PMC12175206. **OA: Y**
  引用：264/395 納入、中位追蹤 34 個月、復發 41（15.5%）、**孤立局部復發僅 4 人**、**無症狀在內診發現 3 人（1.1%）、進到救援 1 人（0.4%）**、
  類內膜 76.5%、FIGO 2023 第 II 期 48.5%、ESGO/ESTRO 高風險 36.7%。

- **[D-S12] PASS（OA）** Ulusoy CO, Varlı B, Gökçe A, Altın D, Baydemir ŞK, Ortaç UF, Taşkın S.
  **Determining the optimal follow-up protocol after primary surgery in patients with early-stage endometrial cancer.**
  *J Turk Ger Gynecol Assoc.* 2025;26(2):82–89. DOI: 10.4274/jtgga.galenos.2025.2025-2-4. PMID: 40495516. PMCID: PMC12152776. **OA: Y**
  引用：n=303、復發 17（5.61%）、**23 個月累積 3.06%／33 個月 7.52%**、理學檢查敏感度 50.00%／特異度 99.52%／PPV 88.89%／NPV 96.30%、
  分化度每升一級 OR 2.549（1.078–6.027，p=0.033）、期別每升一級 OR 2.943（1.270–6.820，p=0.012）。

- **[D-S13] PASS（OA）** Sadeghi N, Conforti J, Zouridis A, Kashif A, Darwish A, Smyth SL, Sattar A, Addley S, Pappa C, Damato S, Abdalla M,
  Kehoe S, Ferrari F, Soleymani Majd H.
  **Prognostic characteristics and recurrence patterns of grade 1 endometrial carcinoma: a large retrospective analysis of a tertiary center.**
  *Transl Cancer Res.* 2025;14(11):7611–7620. DOI: 10.21037/tcr-2025-1635. PMID: 41378031. PMCID: PMC12686162. **OA: Y**
  引用：n=238、復發 14（5.88%）、其中 11（78.5%）原為第 1 期、**中位復發時間 30 個月**、**陰道頂端 42%**、
  深肌層侵犯（P=0.049）與漿膜侵犯（P=0.01）為顯著預測因子。

- **[D-S14] PASS** Rios-Doria E, Cun HT, Filippova OT, Mueller JJ, Alektiar KM, Ellenson LH, Makker V, Lakhman Y, Leitao MM, Jhingran A,
  Soliman PT, Abu-Rustum NR.
  **Isolated vaginal recurrence in women with stage I endometrial cancer.** *Gynecol Oncol.* 2023;179:9–15. DOI: 10.1016/j.ygyno.2023.10.011.
  PMID: 37864854. PMCID: PMC11215939. OA: N
  引用：**n=2,815（2009 FIGO 第 1 期）、復發 278（10%）、孤立陰道 61（2%，其中頂端 42 人＝69%）、陰道外 217（8%）**、
  中位復發時間 11 vs 20 個月（P<.004）、輔助陰道近接治療 960 人中孤立陰道復發 19（2%，84% 在頂端）、結論句「Adjuvant VBT … carries a
  1%–2% risk of isolated vaginal apex recurrence」。

- **[D-S15] PASS（僅摘要層級）** Lantsman T, Jansen C, Larson E, Esselen K, Shea M.
  **An evaluation of the utility of computed tomography in high-risk endometrial cancer surveillance.** *Cancer Treat Res Commun.*
  2024;39:100812. DOI: 10.1016/j.ctarc.2024.100812. PMID: 38582032. OA: N
  引用：n=229 高風險、復發 63（28%）、**例行影像先發現 31（49.2%）／症狀 24（38.15%）**、最常見復發部位為肺、
  復發後平均存活 2.0 vs 1.6 年**無統計差異**。

- **[D-S16] PASS（僅摘要層級）** Kokts-Porietis RL, O'Sullivan DE, Nelson G, Courneya KS, Cook LS, Friedenreich CM.
  **Risk factors for second primary cancer in a prospective cohort of endometrial cancer survivors: an Alberta Endometrial Cancer Cohort
  Study.** *Am J Epidemiol.* 2024;193(12):1701–1711. DOI: 10.1093/aje/kwae140. PMID: 38918029. OA: N
  引用：n=533、中位追蹤 16.7 年（IQR 12.2–17.9）、**89 人（17%）第二原發癌**、乳房 29%／大腸直腸 13%／肺 12%、
  飲食升糖負荷 sHR 1.71（1.09–2.69）、存活早期年齡 ≥60 sHR 2.48（1.34–4.62）、飲酒 ≥2 杯/週 sHR 3.81（1.55–9.31）、
  減少飲酒 sHR 0.34（0.14–0.82）、「With 1 in 6 survivors developing an SPC」。

- **[D-S17] PASS（OA）** Wang Y, Cai Y.
  **Association between radiation therapy for primary endometrial cancer and risk of second primary malignancies: a retrospective cohort
  study.** *Sci Rep.* 2024;14(1):24623. DOI: 10.1038/s41598-024-74840-4. PMID: 39427001. PMCID: PMC11490500. **OA: Y**
  引用：n=62,108（放療 16,846＝27.12%／未放療 45,262）、30 年累積第二原發癌 20.9% vs 19.7%、
  大腸直腸 aHR 1.29（1.12–1.50）、肺與支氣管 1.27（1.08–1.50）、外陰 1.72（1.04–2.85）、膀胱 1.86（1.41–2.46）、
  非何杰金氏淋巴瘤 1.37（1.06–1.77）、**乳癌 aHR 0.89（0.80–0.98）**。

- **[D-S19] PASS（OA，次要）** Zhang N, Marshall L, Thappa S, Morell A, Samborski A, Moore R, Wilbur M.
  **Patient Surveillance Adherence After Treatment for Endometrial Cancer.** *O&G Open.* 2024;1(2):10. DOI: 10.1097/OG9.0000000000000010.
  PMID: 41000582. PMCID: PMC12456480. **OA: Y**
  引用：n=870、遵從 761（87.5%）、未遵從者距癌症中心較遠（39.2 vs 20.7 英里，P=.026）、家戶所得中位數較低（$74,015 vs $80,435，P=.027）。

- **[D-S20] PASS（僅供框架，不取數字）** Szatkowski W, Glanowska-Nawrat I.
  **Toward Biology-Driven Surveillance After Endometrial Cancer Treatment: A Molecular-Clinical Framework Integrating Recurrence Phenotype.**
  *Cancers.* 2026;18(9):1443. DOI: 10.3390/cancers18091443. PMID: 42122239. PMCID: PMC13163091. **OA: Y**
  **這是敘事型回顧＋概念架構，不是原始資料。正文只可用來說明「有人在提議依分子型分層追蹤，但這是提案不是實證」，不得引用任何數字。**

### 三、D2 復發（PASS）

- **[D-S21] PASS** Creutzberg CL, van Putten WLJ, Koper PC, Lybeert MLM, Jobsen JJ, Wárlám-Rodenhuis CC, De Winter KA, Lutgens LCHW,
  van den Bergh ACM, van der Steen-Banasik E, Beerman H, van Lent M, PORTEC Study Group.
  **Survival after relapse in patients with endometrial cancer: results from a randomized trial.** *Gynecol Oncol.* 2003;89(2):201–209.
  DOI: 10.1016/S0090-8258(03)00126-4. PMID: 12713981. OA: N
  引用：n=715 收案／714 分析、中位追蹤 73 個月、**8 年局部區域復發 4% vs 15%（P<0.0001）、8 年 OS 71% vs 77%（P=0.18）、
  8 年遠端轉移 10% vs 6%（P=0.20）**；**39 位孤立陰道復發 → 35 位（87%）根治意圖 → 31 位（89%）完全緩解 → 24 位（77%）維持**；
  **首次復發後 3 年存活 對照 51% vs 放療 19%（P=0.004）**；**依部位 3 年存活 陰道 73%／骨盆 8%／遠端 14%（P<0.001）**；
  **5 年陰道復發後存活 對照 65% vs 放療 43%**；結論句逐字。

- **[D-S22] PASS** Klopp AH, Enserro D, Powell M, Randall M, Schink JC, Mannel RS, Holman L, Bender D, Kushnir CL, Backes F, Zweizig SL,
  Waggoner S, Bradley KA, Lawrence LD, Hanjani P, Darus CJ, Small W, Cardenes HR, et al.
  **Radiation Therapy With or Without Cisplatin for Local Recurrences of Endometrial Cancer: Results From an NRG Oncology/GOG Prospective
  Randomized Multicenter Clinical Trial.** *J Clin Oncol.* 2024;42(20):2425–2435. DOI: 10.1200/JCO.23.01279. PMID: 38662968. PMCID: PMC11681946. OA: N
  引用：2008-02–2020-08、**n=165 隨機 1:1**、**82% 低惡性度類內膜、86% 陰道侷限**、每週 cisplatin 40 mg/m²、
  **3 年 73%（單純放療）vs 62%（化放療）存活且無惡化**、中位 PFS 未達到 vs 73 個月、**HR 1.25（95% CI 0.75–2.07）**、
  化放療急性毒性較高、結論句逐字。

- **[D-S23] PASS（僅摘要層級）** Alban G, Cheng T, Adleman J, Buzurovic I, Pretz J, Singer L, King M, Lee L.
  **Definitive radiotherapy for vaginal recurrence of early-stage endometrial cancer: survival outcomes and effect of mismatch repair status.**
  *Int J Gynecol Cancer.* 2021;31(7):1007–1013. DOI: 10.1136/ijgc-2021-002536. PMID: 33858956. OA: N
  引用：n=62（第 1–2 期、**皆無輔助放療**）、89% 類內膜／85% G1–2／89% 陰道單獨、中位追蹤 39 個月、
  **3 年／5 年 陰道控制 86%／82%、無復發存活 69%／55%、總存活 80%／61%**、
  非類內膜 復發 HR 12.5（P<0.01）、死亡風險 4.5 倍（P=0.02）、
  **MMR 亞組（n=20，10 例缺損）3 年無復發存活 100% vs 52%（P=0.03）**、
  晚期 G2／G3 毒性 腸胃道 27%／3%、泌尿道 15%／2%、陰道 16%／2%。

- **[D-S24] PASS** Ling DC, Vargo JA, Glaser SM, Kim H, Beriwal S.
  **Outcomes after definitive re-irradiation with 3D brachytherapy with or without external beam radiation therapy for vaginal recurrence of
  endometrial cancer.** *Gynecol Oncol.* 2019;152(3):581–586. DOI: 10.1016/j.ygyno.2018.12.022. PMID: 30600093. PMCID: PMC7422921. OA: N
  引用：n=22、先前放療分布（陰道近接 54.5%／骨盆外照射 22.7%／兩者 22.7%）、中位再照射間隔 26.6 個月、
  累積 D2cc 限制（直腸乙狀 <75 Gy、膀胱 <90 Gy）、中位 HR-CTV D90 64.5 Gy（IQR 49.6–75.8）、中位追蹤 27.6 個月、
  **3 年 局部控制 65.8%／區域控制 76.6%／無疾病存活 40.8%／總存活 68.1%**、**無 G≥3 急性或晚期直腸乙狀／膀胱毒性**、結論句「salvage 40%」。

- **[D-S25] PASS（僅摘要層級）** Lee LJ, Alban GM, Cheng T, Buzurovic I, Pretz J, Singer L, King MT.
  **Clinical outcomes and dosimetric predictors of toxicity for re-irradiation of vaginal recurrence of endometrial cancer.**
  *Brachytherapy.* 2022;21(3):263–272. DOI: 10.1016/j.brachy.2021.12.010. PMID: 35078717. OA: N
  引用：n=32（2003-06–2017-12）、先前放療分布（陰道近接 19＝59%／骨盆 7＝22%／兩者 6＝19%）、中位追蹤 47 個月、
  **3/5 年 陰道控制 64%／56%、無復發存活 47%／41%、總存活 68%／42%**、6 人（19%）在 85–155 個月無疾病、
  **晚期 G2／G3 毒性 腸胃道 13%／16%、泌尿道 19%／13%、陰道 9%／16%**、
  累積直腸 D2cc 對應 10% 晚期 G2+／G3 腸胃道毒性風險為 **86 Gy／92 Gy**。

- **[D-S26] PASS（僅摘要層級）** Baek S, Isohashi F, Yamaguchi H, Mabuchi S, Yoshida K, Kotsuma T, et al.
  **Salvage high-dose-rate brachytherapy for isolated vaginal recurrence of endometrial cancer.** *Brachytherapy.* 2016;15(6):812–816.
  DOI: 10.1016/j.brachy.2016.08.005. PMID: 27614661. OA: N
  引用：1997–2012、n=43（組織插種 34＝79%／腔內 9＝21%；17 人＝40% 併外照射）、中位年齡 64 歲、中位追蹤 58 個月、
  **5 年 OS 84%／PFS 52%／局部控制 78%**、併外照射者淋巴結復發 0/17 vs 單純近接 6/26（23%），p=0.047、
  **G1–2 vs G3：5 年 OS 96% vs 40%（p<0.01）、5 年 PFS 58% vs 0%（p<0.01）**、
  年齡（≥60 vs <60）5 年局部控制 74% vs 100%（p=0.020）、組織插種 vs 腔內 85% vs 56%（p=0.035）。

- **[D-S27] PASS（OA）** Sekii S, Murakami N, Kato T, Harada K, Kitaguchi M, Takahashi K, et al.
  **Outcomes of salvage high-dose-rate brachytherapy with or without external beam radiotherapy for isolated vaginal recurrence of
  endometrial cancer.** *J Contemp Brachytherapy.* 2017;9(3):209–215. DOI: 10.5114/jcb.2017.67755. PMID: 28725243. PMCID: PMC5509978. **OA: Y**
  引用：1992–2014、n=37（腔內 23／組織插種 14；26 人併外照射）、中位追蹤 48 個月、
  **4 年 OS 81.0%／局部控制 77.9%／PFS 56.8%**、**診斷復發到放療 <3 vs ≥3 個月是局部控制與 PFS 的顯著預測因子**、
  2 例 G2 直腸出血、4 例 G2 血尿、**無 G3 以上晚期併發症**。

- **[D-S28] PASS（僅摘要層級）** Maina J, Liu ZA, Milosevic M, Croke J, Lukovic J, Malik N, Rink A, Beiki-Ardakani A, Weersink RA, Serban M,
  Skliarenko J, Rauth S, Conway JL, Han K.
  **MRI-guided brachytherapy for vaginal recurrence of endometrial cancer.** *Brachytherapy.* 2026;25(1):107–114.
  DOI: 10.1016/j.brachy.2025.10.007. PMID: 41274827. OA: N
  引用：2015–2023、n=56（腔內多管 17＝30%／組織插種 Syed-Neblett 39＝70%）、53（94%）類內膜、中位 HR-CTV D90 82 Gy、中位追蹤 39.5 個月、
  復發 11 人（20%）、**2 年局部失敗 5.9%（95% CI 1.5–15.9）、2 年 DFS 83%（73–94）、2 年 OS 94%（87–100）**、
  最高晚期毒性 grade 2（腸胃道 0／泌尿道 1／陰道 6）。

- **[D-S29] PASS（OA）** Bizzarri N, Querleu D, Ricotta G, Giannarelli D, Cãpîlna ME, Domingo S, Chiantera V, Akıllı H, Cibula D, Novák Z,
  Zach D, Miranda A, Korompelis P, Chiva L, Zapardiel I, Lampe B, Svintsitskyi V, Matylevich O, et al.
  **Complications and Recurrence After Pelvic Exenteration for Gynecologic Malignancies: Survival Analysis From the COREPEX Study.**
  *Obstet Gynecol.* 2025;146(5):737–749. DOI: 10.1097/AOG.0000000000006051. PMID: 40934517. PMCID: PMC12520032. **OA: Y**
  引用：n=862（2005-01–2023-03，20 家歐洲三級中心；子宮頸／陰道／外陰／**子宮內膜**癌；前位或全骨盆廓清）、
  **切緣無腫瘤 676（78.4%）**、預後分數四組 **5 年 DFS 43.7%／24.9%／22.2%／8.0%（P<.001）、5 年 OS 54.3%／40.4%／24.0%／4.3%（P<.001）**、
  最常見復發部位遠端 166（32.1%）、全骨盆廓清／切緣陽性／LVSI 獨立預測較差 DFS 與 OS、持續性疾病時手術 OS 較差、
  主動脈旁淋巴結轉移者 5 年 DFS 與癌症特異存活顯著較差（P=.002、P<.001）。

- **[D-S30] PASS（僅摘要層級）** Bizzarri N, Querleu D, Ricotta G, Giannarelli D, Cãpîlna ME, Domingo S, Chiantera V, Akıllı H, Cibula D,
  Novák Z, Zach D, Miranda A, Korompelis P, Chiva L, Zapardiel I, Lampe B, Svintsitskyi V, Matylevich O, et al.
  **Complications and recurrence after pelvic exenteration for gynecologic malignancies: Analysis of surgical complications from the COREPEX
  study.** *Int J Gynecol Cancer.* 2026;36(2):102820. DOI: 10.1016/j.ijgc.2025.102820. PMID: 41505868. OA: N
  引用：n=862、**嚴重術中併發症 7（0.8%）、術中死亡 0**、**嚴重早期術後併發症 225（26.1%）、30 天內死亡 27（3.1%）**、
  **嚴重晚期術後併發症 87（10.1%）、31–180 天死亡 16（1.8%）**、
  早期最常見骨盆膿瘍／積液 23.4%、尿路造口漏／廔管 13.4%；晚期骨盆膿瘍／積液 21.6%、良性輸尿管狹窄 13.5%。
  **同世代的單中心對照（英國，n=47，內膜癌 17 人＝36%；Clavien-Dindo ≥3 為 32%、術後死亡 1、中位住院 17 天、中位失血 1.5 L、
  中位手術 391 分鐘）出自 Zalawadia S, et al. J Clin Med. 2026;15(10):3957（DOI 10.3390/jcm15103957，PMID 42194919，PMCID PMC13207788，OA: Y）
  ——引用該組數字時請標為「單一中心 n=47」，勿與 COREPEX 混寫。**

- **[D-S31] PASS** Thigpen JT, Brady MF, Alvarez RD, Adelson MD, Homesley HD, Manetta A, Soper JT, Given FT.
  **Oral medroxyprogesterone acetate in the treatment of advanced or recurrent endometrial carcinoma: a dose-response study by the
  Gynecologic Oncology Group.** *J Clin Oncol.* 1999;17(6):1736–1744. DOI: 10.1200/JCO.1999.17.6.1736. PMID: 10561210. OA: N
  引用：n=299 隨機（MPA 200 mg/日 vs 1,000 mg/日）、
  **低劑量 n=145：CR 25（17%）＋PR 11（8%）＝25%；PFS 3.2 個月；OS 11.1 個月**；
  **高劑量 n=154：CR 14（9%）＋PR 10（6%）＝15%；PFS 2.5 個月；OS 7.0 個月**；校正勝算比 0.61（90% CI 0.36–1.04）；
  預後因子（PS、年齡、分化度、黃體素受體）；**「Patients with poorly differentiated and/or progesterone receptor levels less than
  50 fmol/mg cytosol protein had only an 8% to 9% response rate.」**

- **[D-S32] PASS** Fiorica JV, Brunetto VL, Hanjani P, Lentz SS, Mannel R, Andersen W, Gynecologic Oncology Group.
  **Phase II trial of alternating courses of megestrol acetate and tamoxifen in advanced endometrial carcinoma: a Gynecologic Oncology Group
  study.** *Gynecol Oncol.* 2004;92(1):10–14. DOI: 10.1016/j.ygyno.2003.11.008. PMID: 14751131. OA: N
  引用：61 人入組／**56 人可評估**、MA 80 mg BID×3 週交替 T 20 mg BID×3 週、
  **15 人反應（12 CR＋3 PR）＝27%（90% CI 17–38%）**、**8/15（53%）反應持續 >20 個月**、
  依分化度 G1 38%（n=16）／G2 24%（n=17）／G3 22%（n=23）、≤60 歲 44%（n=16）vs >60 歲 20%（n=40）、
  骨盆外病灶 31%（n=42）vs 侷限骨盆／陰道 14%（n=14）、**中位 PFS 2.7 個月／中位 OS 14.0 個月**、**2 例 grade 4 血栓栓塞**。

- **[D-S33] PASS（僅摘要層級）** McHenry A, Devereaux K, Ryan E, Chow S, Allard G, Ho CC, Suarez CJ, Folkins A, Yang E, Longacre TA, Charu V,
  Howitt BE.
  **Molecular classification of metastatic and recurrent endometrial endometrioid carcinoma: prognostic relevance among low- and high-stage
  tumours.** *Histopathology.* 2024;85(4):614–626. DOI: 10.1111/his.15232. PMID: 38859768. OA: N
  引用：n=141（診斷即轉移或後續復發／轉移的子宮內膜樣癌）、**POLE 突變 9（6%）／MSI 45（32%）／p53 異常 16（11%）／NSMP 71（50%）**、
  **疾病特異存活與 TCGA 分類相關：高期別 P=0.02、低期別（自復發時起算）P=0.017**、
  **原發與轉移／復發分類不一致 4/105（3.8%）**（2 例 PMS2/MSH6 IHC、2 例 p53 IHC）。

- **[D-S34] PASS（僅摘要層級）** Lindemann K, Kildal W, Kleppe A, Tobin KAR, Pradhan M, Mascialino B, Schneider D, Edvardsen H, Sørlie T,
  Kristensen GB, Askautrud HA.
  **Real-world outcomes in molecular subgroups for patients with advanced or recurrent endometrial cancer treated with platinum-based
  chemotherapy.** *Int J Gynecol Cancer.* 2025;35(5):101618. DOI: 10.1016/j.ijgc.2024.101618. PMID: 40189984. OA: N
  引用：挪威 Radium Hospital 2006-01–2017-12、**晚期 264 人／復發 96 人**、
  分子分類在晚期病人對復發時間與癌症特異存活皆 P<.0001、**「the outcome did not differ significantly by molecular groups in recurrent patients」**、
  p53 異常 晚期 HR 1.57（1.07–2.30）／1.78（1.19–2.65）；復發族群 HR 1.45（0.83–2.52）／1.60（0.99–2.68）；POLE 突變者結果佳（人數少）。

- **[D-S35] PASS（OA）** Alexandre J, Boudier P, Lavit E, Asselain B, Emambux S, Berton D, Babin G, Lescure C, Heudel PE, Salaun H, Delanoy N,
  Dawood H, Combe P, Duliège D, Selle F, Hakmé A, Cagnan L, Offner N, Niogret J, et al.
  **Clinical outcome of advanced or recurrent endometrial carcinoma treated with chemotherapy: a French observational retrospective cohort:
  the ENDOVIE study.** *BMJ Open.* 2025;15(9):e096837. DOI: 10.1136/bmjopen-2024-096837. PMID: 40908005. PMCID: PMC12414171. **OA: Y**
  引用：2019 年接受第一或第二線化療者 n=200（第一線 127／第二線 73）、類內膜 62.0%、第一線 carboplatin＋paclitaxel 78.0%、
  **中位 rwPFS／OS：第一線 8.5／13.2 個月；第二線 4.0／9.4 個月**、癌肉瘤／肝轉移／FIGO IVB 與較差結果相關。
  **引用時必須標「PD-1 抑制劑上市前的法國真實世界」。**

### 四、D3 下肢淋巴水腫（PASS）

- **[D-S36] PASS** Leitao MM, Zhou QC, Gomez-Hidalgo NR, Iasonos A, Baser R, Mezzancello M, Chang K, Ward J, Chi DS, Long Roche K, Sonoda Y,
  Brown CL, Mueller JJ, Gardner GJ, Jewell EL, Broach V, Zivanovic O, Dowdy SC, et al.
  **Patient-reported outcomes after surgery for endometrial carcinoma: Prevalence of lower-extremity lymphedema after sentinel lymph node
  mapping versus lymphadenectomy.** *Gynecol Oncol.* 2020;156(1):147–153. DOI: 10.1016/j.ygyno.2019.11.003. PMID: 31780238. PMCID: PMC6980687. OA: N
  引用：2006-01–2012-12 手術者、2016-08 郵寄問卷、1,275 人中 623（49%）回覆、**599 可分析（SLN 180／LND 352／單純子宮切除 67）**、
  **自述 LEL 27%（49/180）vs 41%（144/352），OR 1.85（95% CI 1.25–2.74，P=0.002）**、
  **外照射者 51%（23/45）vs 未接受 35%（170/487），OR 1.95（1.06–3.6，P=0.03）**、
  **BMI 每升 1 單位 OR 1.04（1.02–1.06，P=0.001）**、校正後 LND vs SLN **OR 1.8（1.22–2.69，P=0.003）**、
  自述 LEL 者生活品質顯著較差。外照射使用率 SLN 5.5% vs LND 10%（P=0.1）。

- **[D-S37] PASS（僅摘要層級）** Glaser G, Dinoi G, Multinu F, Yost K, Al Hilli M, Larish A, Kumar A, McGree M, Weaver AL, Cheville A, Dowdy S,
  Mariani A.
  **Reduced lymphedema after sentinel lymph node biopsy versus lymphadenectomy for endometrial cancer.** *Int J Gynecol Cancer.*
  2021;31(1):85–91. DOI: 10.1136/ijgc-2020-001924. PMID: 33243776. OA: N
  引用：2009-01–2016-06 微創手術、**n=378（SLN 127／LND 251）**、13 題篩檢問卷、
  **整體 LEL 盛行率 41.5%（157/378）**（69 人＝18.3% 自報曾被診斷，中位 54.3 個月，IQR 31.2–70.1；另 88 人＝23.3% 由問卷篩出）、
  **26.0%（33/127）vs 49.4%（124/251），P<0.001**；**限 SLN 引進後同期：26.0%（33/127）vs 39.0%（41/105），P=0.03**；
  校正 BMI／外照射／糖尿病／心衰竭／FIGO 分化度後 **OR 2.75（95% CI 1.69–4.47，P<0.001）**。

- **[D-S38] PASS（僅摘要層級）** Geppert B, Lönnerfors C, Bollino M, Persson J.
  **Sentinel lymph node biopsy in endometrial cancer—Feasibility, safety and lymphatic complications.** *Gynecol Oncol.* 2018;148(3):491–498.
  DOI: 10.1016/j.ygyno.2017.12.017. PMID: 29273307. OA: N
  引用：前瞻 n=188 計畫機器人手術、ICG 子宮頸注射雙側偵測率 96%、SLN 本身無術中併發症、
  相對單純子宮切除多 33 分鐘、相對全骨盆＋腎下主動脈旁廓清省 91 分鐘、
  **僅摘除前哨者腿部淋巴水腫 1.3% vs 腎下主動脈旁＋骨盆廓清 18.1%（p=0.0003）**。

- **[D-S39] PASS（僅摘要層級）** Casarin J, Schivardi G, Artuso V, Giudici A, Meschini T, De Vitis L, Granato V, Lembo A, Cromi A, Mariani A,
  Bogani G, Multinu F, Ghezzi F.
  **Laparoscopic treatment of early-stage endometrial cancer: benefits of sentinel lymph node mapping and impact on lower extremity
  lymphedema.** *Int J Gynecol Cancer.* 2025;35(8):101857. DOI: 10.1136/ijgc-2024-005670. PMID: 39313300. OA: N
  引用：2020-01–2023-08 單中心、n=239、問卷回覆率 85.4%、
  分組：子宮切除＋SLN 54.8%／＋系統性骨盆廓清 27.2%／單純子宮切除 18%、
  **LEL 盛行率 21.4% vs 44.6%（p=0.003）**、多變項 **OR 3.11（95% CI 1.47–6.58）**、
  **無其他病人或腫瘤特徵與 LEL 相關**。

- **[D-S40] PASS（僅摘要層級）** Bjørnholt SM, Groenvold M, Petersen MA, Mogensen O, Bouchelouche K, Sponholtz SE, Neumann G, Bjørn SF,
  Hamid BH, Dahl K, Jensen PT.
  **Patient-reported lymphedema after sentinel lymph node mapping in women with low-grade endometrial cancer.** *Am J Obstet Gynecol.*
  2025;232(3):306.e1–306.e11. DOI: 10.1016/j.ajog.2024.09.001. PMID: 39245429. OA: N
  引用：丹麥全國前瞻世代 2017-03–2022-02、推定第 1 期低惡性度、**486/617（79%）完成術前與 12 個月 PROM**、
  主要終點 EORTC QLQ-EN24 腿部淋巴水腫分數（0–100，**8 分為臨床顯著門檻**）、
  **12 個月平均差 5.0（95% CI 3.3–6.8），低於門檻**、術前腿部分數與 BMI 為預測因子、**3 個月分數預測 12 個月分數**、
  12 個月高分者與日常活動、外觀、情緒功能與整體生活品質負相關。

- **[D-S41] PASS（OA）** Helgers RJA, Winkens B, Slangen BFM, Werner HMJ.
  **Lymphedema and Post-Operative Complications after Sentinel Lymph Node Biopsy versus Lymphadenectomy in Endometrial Carcinomas—A
  Systematic Review and Meta-Analysis.** *J Clin Med.* 2020;10(1):120. DOI: 10.3390/jcm10010120. PMID: 33396373. PMCID: PMC7795280. **OA: Y**
  引用：7 篇（回溯與前瞻）、**共 3,046 人**、
  **僅 3 篇報下肢水腫勝算比：OR 0.05（0.01–0.37；p=0.067）、0.07（0.00–1.21；p=0.007）、0.54（0.37–0.80；p=0.002）**、
  合併任何術後併發症 OR 0.52（0.36–0.73，I²=48%，p<0.001）、嚴重術後併發症 OR 0.52（0.28–0.96，I²=0%，p=0.04）、
  結論句「strong indications … In spite of the paucity and heterogeneity of studies」。

- **[D-S42] PASS（僅摘要層級）** Accorsi GS, Paiva LL, Schmidt R, Vieira M, Reis R, Andrade C.
  **Sentinel Lymph Node Mapping vs Systematic Lymphadenectomy for Endometrial Cancer: Surgical Morbidity and Lymphatic Complications.**
  *J Minim Invasive Gynecol.* 2020;27(4):938–945.e2. DOI: 10.1016/j.jmig.2019.07.030. PMID: 31421249. OA: N
  引用：2013-04–2018-03、n=250、四組（HT／HT+SLN／HT+LND／HT+SLN+LND）、
  **HT+SLN 相對 HT 無術中（0 vs 1，p=1.0）與 30 天併發症（8 vs 7，p=.782）增加，手術時間多約 20 分鐘（p=.016）**；
  **執行 LND 者 30 天併發症 HR 3.11（1.62–5.98）、術中併發症 HR 14.25（1.85–19.63）、下肢淋巴水腫 HR 8.14（1.01–65.27）**。

- **[D-S43] PASS（僅摘要層級）** Wedin M, Stalberg K, Marcickiewicz J, Ahlner E, Ottander U, Åkesson Å, Lindahl G, Wodlin NB, Kjølhede P,
  LASEC study group.
  **Risk factors for lymphedema and method of assessment in endometrial cancer: a prospective longitudinal multicenter study.**
  *Int J Gynecol Cancer.* 2021;31(11):1416–1427. DOI: 10.1136/ijgc-2021-002890. PMID: 34610970. OA: N
  引用：瑞典 14 院、**n=235（廓清 116／未廓清 119）**、術前與術後 1 年、四種判定法（原始體積／BMI 標準化體積／臨床分級／病人自覺；體積法 ≥10%）、
  **淋巴廓清 aOR：BMI 標準化體積 14.42（3.49–59.62）、臨床分級 2.11（1.04–4.29）、病人自覺 2.51（1.33–4.73）、原始體積非顯著**、
  **輔助放療僅 BMI 標準化體積 aOR 15.02（2.34–96.57）**、年齡 aOR 1.07／1.06、BMI aOR 1.92／1.36、
  結論句「Apparent risk factors … differed considerably depending on the method used … need for a 'gold standard' method」。

- **[D-S44] PASS（OA，次要）** Wedin M, Stålberg KG, Ottander U, Åkesson Å, Lindahl G, Wodlin NB, Kjølhede P.
  **Risk factors for lymph ascites after surgery for endometrial cancer and impact on lymphedema of the legs. A prospective longitudinal
  Swedish multicenter study.** *Acta Obstet Gynecol Scand.* 2025;104(5):976–987. DOI: 10.1111/aogs.15077. PMID: 40035366. PMCID: PMC11981105. **OA: Y**
  **本 brief 未取用其數字；列出供寫作者知道同一個瑞典世代還有淋巴腹水這條線。正文若要用，需自行回查摘要。**

- **[D-S45] PASS（OA）** Utsugi K, Ishizuka N, Nomura H, Fusegi A, Kanao H.
  **A 5-year prospective assessment of risk factors for lower limb lymphedema after gynecologic cancer surgery.** *Sci Rep.* 2025;15(1):26371.
  DOI: 10.1038/s41598-025-11732-1. PMID: 40691210. PMCID: PMC12280194. **OA: Y**
  引用：2011–2012 含骨盆淋巴廓清手術者 n=190、追蹤 5 年、水腫定義 ISL 第 I 期以上、
  **5 年累積發生率 39.6%**、含 taxane（docetaxel／paclitaxel）輔助化療 51.6%、摘除淋巴結 ≥60 顆 49.1%、
  **「The incidence of lower limb lymphedema was highest in the first year.」**

- **[D-S46] PASS（OA）** Utsugi K, Ishizuka N, Seki Y, Nomura H, Fusegi A, Kanao H.
  **A prospective assessment of simple lymphatic drainage to prevent lower limb lymphedema in gynecological malignancies.** *Sci Rep.*
  2025;15(1):42805. DOI: 10.1038/s41598-025-26967-1. PMID: 41315504. PMCID: PMC12663189. **OA: Y**
  引用：2011-04–2012-05 收 224 人、排除後 190 人、**其中未接受輔助治療的 87 人依意願分為 SLD 組 24／對照 63**、SLD 每日執行一年、追蹤 5 年、
  **下肢周徑變化率與細胞外水／全身水比值皆無顯著差異**、**5 年累積水腫發生率 37.5% vs 23.5%，無顯著差異**、
  結論句「SLD does not contribute to the prevention of LLE」。

- **[D-S47] PASS** Ezzo J, Manheimer E, McNeely ML, Howell DM, Weiss R, Johansson KI, Bao T, Bily L, Tuppo CM, Williams AF, Karadibak D.
  **Manual lymphatic drainage for lymphedema following breast cancer treatment.** *Cochrane Database Syst Rev.* 2015;(5):CD003475.
  DOI: 10.1002/14651858.CD003475.pub2. PMID: 25994425. PMCID: PMC4966288. OA: N
  引用：**6 個試驗**、MLD＋壓力繃帶 vs 壓力繃帶（2 試驗、83 人）：**壓力繃帶單獨減少 30%–38.6% 多餘體積，加 MLD 再多 7.11%
  （MD 7.11%，95% CI 1.75–12.47）**、體積減少量 P=0.06、殘餘水腫體積無顯著；
  輕到中度水腫者受益較多；MLD＋袖套 vs 氣壓幫浦＋袖套：體積減少 MD 47.00 mL（15.25–78.75；1 試驗、24 人）；
  MLD＋袖套 vs 自我簡易淋巴引流＋袖套：殘餘水腫體積 MD −230.00 mL（−450.84 至 −9.16；1 試驗、31 人）；
  疼痛與沉重感「60% to 80% of participants reported feeling better regardless of which treatment they received」；
  一年追蹤「keep their swelling down if they continued to use a custom-made sleeve」；結論句「MLD is safe and may offer additional benefit
  to compression bandaging for swelling reduction」。**族群是乳癌手臂，外推到下肢必須標明。**

- **[D-S48] PASS（OA）** Wu Y, Li X, Shao P, Wang T.
  **Effectiveness of physical therapy for lower limb lymphedema in gynecological cancer survivors: a systematic review of randomized
  controlled trials.** *Front Oncol.* 2026;16:1792931. DOI: 10.3389/fonc.2026.1792931. PMID: 41939456. PMCID: PMC13047141. **OA: Y**
  引用：檢索至 2025-12-27、PROSPERO CRD420251274284、**6 個 RCT、共 289 人**、
  **無一被判高偏誤風險**、顯著減少下肢體積或周徑、改善疼痛與沉重感、肌力與步態、生活品質、
  **多模式優於單一模式**、不良事件皆為輕度、無嚴重不良事件。

- **[D-S49] PASS（僅摘要層級）** Nicholas Jungbauer W, Solomon S, Verhey EM, Jeger JL, Chang YH, Rhee DH, Rebecca AM, Saint-Cyr M, Reece EM,
  Casey WJ.
  **Lymphovenous Anastomosis and Vascularized Lymph Node Transfer Reduce Long-term Cellulitis Events in Patients With Secondary Lymphedema:
  A Systematic Review and Meta-analysis.** *Ann Plast Surg.* 2025;95(5):522–530. DOI: 10.1097/SAP.0000000000004508. PMID: 41071856. OA: N
  引用：23 篇、**648 肢（LVA 216／VLNT 432）**、追蹤 ≥24 個月、
  **年蜂窩性組織炎次數合併平均減少：LVA 上肢 −1.13（−1.70 至 −0.57）、LVA 下肢 −1.32（−2.08 至 −0.55）、
  VLNT 上肢 −2.43（−3.36 至 −1.50）、VLNT 下肢 −1.38（−2.11 至 −0.65）**；VLNT 周徑減少 上肢 42.7%（36.7–49.7）／下肢 21.98%（19.8–24.4）。

- **[D-S50] PASS（OA）** Hinson C, Sink M, Henn D, Sammer D, Zhang AY, Billig JI, Chang E, Odobescu A.
  **Preventing Secondary Lymphedema: A Systematic Review and Meta-Analysis on the Efficacy of Immediate Lymphovenous Anastomosis.**
  *J Surg Oncol.* 2025;132(4):717–726. DOI: 10.1002/jso.70046. PMID: 40673745. PMCID: PMC12455550. **OA: Y**
  引用：39 篇、**3,697 人（LVA 1,722／對照 1,975）**、17 篇進統合分析、
  **合併續發性淋巴水腫發生率 LVA 7.1% vs 對照 35.0%；RR 0.31**；乳癌次族群 RR 0.28、皮膚惡性腫瘤 RR 0.35。
  **注意：以乳癌為主，婦癌資料少。**

- **[D-S51] PASS（OA）** Shah P, Pillari B, Margiotta N, Devisetti N, Wong AK.
  **Efficacy of vascularized lymph node transfer for lower extremity lymphedema: A systematic review and meta-analysis of 395 patients from
  25 peer-reviewed studies.** *J Plast Reconstr Aesthet Surg.* 2026;116:131–147. DOI: 10.1016/j.bjps.2026.03.005. PMID: 41950607.
  PMCID: PMC13384956. **OA: Y**
  引用：25 篇、**395 人（70.28% 女性）**、PROSPERO CRD420251243270、
  **膝上／膝下周徑縮小率 24.79%／29.50%**（胃網膜供區顯著較佳，p=0.002／p<0.001）、**肢體體積減少 25.32%**、
  **蜂窩性組織炎發生率術後顯著下降（p<0.001）**、不良事件 12.22%。

- **[D-S52] PASS（OA）** Karlsson T, Hoffner M, Brorson H.
  **Liposuction and Controlled Compression Therapy Reduce the Erysipelas Incidence in Primary and Secondary Lymphedema.**
  *Plast Reconstr Surg Glob Open.* 2022;10(5):e4314. DOI: 10.1097/GOX.0000000000004314. PMID: 35539287. PMCID: PMC9076442. **OA: Y**
  引用：n=124 下肢淋巴水腫、中位年齡 49 歲、術前中位追蹤 11 年／術後 5 年、
  **術前 1,680 人年、64 人共 335 次丹毒 → 發生率 0.20 次/人/年、期間盛行率 52%**；
  **術後 763 人年、28 人共 53 次 → 0.07 次/人/年、期間盛行率 23%**；**發生率下降 65%（P<0.001）**；
  術前中位多餘體積 3,158 mL，中位減少 100%（P<0.0001）。

- **[D-S53] PASS（僅摘要層級；族群為乳癌，標籤必寫）** Wagner BD, Rubin J, Lin IH, Raina J, Abul M, Pollack BL, Roberts AN, Barrio AV,
  Kataru RP, Mehrara BJ, Kaltsas A.
  **Clinical Features, Microbial Epidemiology, and Recurrence Risk of Cellulitis in Breast Cancer-Related Lymphedema.**
  *Ann Surg Oncol.* 2026;33(2):1180–1188. DOI: 10.1245/s10434-025-18598-7. PMID: 41110022. PMCID: PMC13256347. OA: N
  引用：單一機構 2000–2024、**2,920 位乳癌相關淋巴水腫**、**231 人（7.9%）發生共 418 次蜂窩性組織炎、再發率 39.0%（90/231）**、
  血液培養 255 次中 33 次（12.9%）陽性、最常見 *Streptococcus agalactiae*（8/33，24.2%）、
  再發風險：任何放療 HR 2.15（1.24–3.72）、腋下淋巴結廓清 HR 1.96（1.05–3.68）、水腫診斷到首次蜂窩性組織炎時間 HR 0.99（P<0.01）。

- **[D-S54] PASS（OA）** Tsuchiya M, Yasutake I, Ishihara Y, Matsuno K, Futami H, Kubo S, Azuma R.
  **Natural History of Subclinical Lower Limb Lymphedema After Gynecologic Cancer Surgery Using Indocyanine Green Lymphography.**
  *Plast Reconstr Surg Glob Open.* 2026;14(8):e7998. DOI: 10.1097/GOX.0000000000007998. PMID: 42559312. PMCID: PMC13441149. **OA: Y**
  引用：2021-04–2024-06、**80 條無症狀下肢**（26 條屬亞臨床，ICG stage ≥1）、中位追蹤 24 個月、
  **出現客觀水腫 50% vs 5.6%（P<0.001）、HR 8.57（95% CI 2.36–31.2，P=0.0011）**、主觀症狀也較早出現（P=0.021）、
  結論句「**not all subclinical cases progress**, which supports the need for risk-based surveillance」。

- **[D-S55] PASS（OA）** Torrent A, Amengual J, Ruiz A, Serra A, Fuertes L, Sampol CM, Ruiz M, Rioja J, Roca P, Cordoba O.
  **Impact of lymph node staging techniques on lymphedema and quality of life in early-stage endometrial cancer: A prospective cohort study.**
  *Gynecol Oncol Rep.* 2025;60:101919. DOI: 10.1016/j.gore.2025.101919. PMID: 40799683. PMCID: PMC12341510. **OA: Y**
  引用（**數字取自同一研究群的預印本摘要 DOI 10.21203/rs.3.rs-6477370/v1，正式期刊版摘要未逐項列出；引用時以「西班牙單中心前瞻 n=97」
  並註明數字來源版本**）：SLN 47／SLN＋完整廓清 50、**有症狀水腫 7.0% vs 34.4%（p=0.002）**、
  整體健康自評中位 85 vs 70（p=0.001）、EQ-5D-3L 中位 5 vs 7（p=0.001）、術中與術後併發症無差異。
  → **正文若要用 7.0% vs 34.4%，必須標「數字出自該研究的預印本版本」；若寫作者不願承擔，改用 [D-S36][D-S37][D-S39] 三筆即可。**

- **[D-S56] PASS（OA，但設計弱）** Wu L, Chen X, Mo D, Duan C, Wu X, Chang X.
  **Does the effect of early manual lymphatic drainage during postoperative hospital stay prevent the development of lower limb lymphedema
  after gynecologic cancer surgery? A real-world cohort study.** *PeerJ.* 2026;14:e21275. DOI: 10.7717/peerj.21275. PMID: 42180605.
  PMCID: PMC13192460. **OA: Y**
  引用：廣西單一醫院、2025-01-03 至 2025-02-15、342 人、**依病人自己選擇分組**、1:1 傾向分數配對後 **111 對**、術後 ≥6 個月 GLQ 問卷、
  **LLL 發生率 10.81% vs 21.62%（P=0.04）、RR 0.50（95% CI 0.263–0.949，P=0.034）**、
  預防行為執行率 38.9% vs 15.6%（P<0.001）。**非隨機、自選分組、行為混淆嚴重——引用時必須全部標出來。**

### 五、D4 日常（PASS）

- **[D-S57] PASS（OA）** Xue Q, Che W, Xue L, Zhang X, Wang X, Lyu J.
  **Causes of death in endometrial cancer survivors: A Surveillance, Epidemiology, and End Result-based analysis.** *Cancer Med.*
  2023;12(9):10917–10930. DOI: 10.1002/cam4.5804. PMID: 36924355. PMCID: PMC10225232. **OA: Y**
  引用：SEER 2000–2015、**n=135,831**、死亡 46,604（34.3%）、**內膜癌 42.9%／其他癌症 15.6%／非癌症 41.5%**、
  非癌症前三：心臟病、腦血管疾病、糖尿病、
  **SMR 心臟病 1.06（1.03–1.09）、糖尿病 1.56（1.47–1.65）、敗血症 1.40（1.28–1.52）**、結論句逐字。

- **[D-S58] PASS（僅摘要層級）** Anderson C, Olshan AF, Bae-Jump VL, Brewster WR, Lund JL, Nichols HB.
  **Cardiovascular disease diagnoses among older women with endometrial cancer.** *Gynecol Oncol.* 2022;167(1):51–57.
  DOI: 10.1016/j.ygyno.2022.08.014. PMID: 36008183. OA: N
  引用：SEER-Medicare、66 歲以上、2004–2017、**內膜癌 44,386 vs 配對無癌 221,219**、指標日起算 1 年後追蹤、
  **缺血性心臟病 HR 1.73（1.69–1.78）、肺源性心臟病 HR 1.95（1.88–2.02）、靜脈與淋巴系統疾病 HR 2.71（2.64–2.78）**。

- **[D-S59] PASS（僅摘要層級）** Soisson S, Ganz PA, Gaffney D, Rowe K, Snyder J, Wan Y, Deshmukh V, Newman M, Fraser A, Smith K, Herget K,
  Hanson HA, Wu YP, Stanford J, Al-Sarray A, Werner TL, Setiawan VW, Hashibe M.
  **Long-term Cardiovascular Outcomes Among Endometrial Cancer Survivors in a Large, Population-Based Cohort Study.** *J Natl Cancer Inst.*
  2018;110(12):1342–1351. DOI: 10.1016/j.ygyno.2017.12.025. PMID: 29741696. PMCID: PMC6292788. OA: N
  引用：猶他州 1997–2012、**2,648 位存活者 vs 10,503 位配對**、
  **1–5 年：靜脈炎／血栓性靜脈炎／栓塞 HR 2.07（99% CI 1.57–2.72）、肺源性心臟病 HR 1.74（1.26–2.40）、心房顫動 HR 1.50（1.07–2.11）**、
  5–10 年部分風險殘留、相較單純手術者，加放療和／或化療者 1–5 年心臟與循環系統疾病風險增加、
  結論句「increased monitoring for cardiovascular diseases may be necessary … for 10 years after cancer diagnosis」。

- **[D-S60] PASS（僅摘要層級；反方向，必列）** Felix AS, Blair CK, Lehman A, Bower JK, Raman SV, Lazovich D, Cohn DE, Prizment AE.
  **Cardiovascular disease mortality among women with endometrial cancer in the Iowa Women's Health Study.** *Cancer Causes Control.*
  2017;28(10):1043–1051. DOI: 10.1007/s10552-017-0953-4. PMID: 28864924. PMCID: PMC6943911. OA: N
  引用：1986–2011、**552 位內膜癌 vs 2,352 位年齡與 BMI 配對對照**、
  **心血管死亡率 HR 0.75（95% CI 0.56–0.99）、全因死亡率 HR 1.50（1.30–1.74）**。

- **[D-S61] PASS（OA）** Friedenreich CM, Cook LS, Wang Q, Kokts-Porietis RL, McNeil J, Ryder-Burbidge C, Courneya KS.
  **Prospective Cohort Study of Pre- and Postdiagnosis Physical Activity and Endometrial Cancer Survival.** *J Clin Oncol.*
  2020;38(34):4107–4117. DOI: 10.1200/JCO.20.01336. PMID: 33026939. PMCID: PMC7768343. **OA: Y**
  引用：Alberta、2002–2006 診斷、**n=425**、追蹤至 2019、中位追蹤 14.5 年、**60 人死亡（內膜癌死亡 18）、80 個 DFS 事件**、
  診斷後休閒活動 >13 vs ≤5 MET-小時/週/年：**DFS HR 0.33（0.17–0.64，P_trend=.001）、OS HR 0.33（0.15–0.75，P_trend=.007）**；
  診斷前 >14 vs ≤8：DFS HR 0.54（0.30–0.96，P_trend=.04）、**OS HR 0.56（0.29–1.07，P_trend=.06，非顯著）**；
  維持高活動者 DFS HR 0.35（0.18–0.69）、OS HR 0.43（0.20–0.94）；校正變項清單見摘要。

- **[D-S62] PASS（OA；反方向，必列）** Oh M, An KY, Lee DH, Kokts-Porietis RL, Cook LS, Friedenreich CM, Jeon JY, Courneya KS.
  **Long-term association of physical activity with survival by primary cancer treatment in endometrial cancer: The Alberta Endometrial
  Cancer Cohort Study.** *Int J Cancer.* 2026;159(2):345–358. DOI: 10.1002/ijc.70369. PMID: 41665306. PMCID: PMC13193435. **OA: Y**
  引用：**n=527**（單純手術 333／手術＋輔助治療 194）、追蹤 16.7 年、**128 人死亡、194 個 DFS 事件**、
  **診斷前達到活動指引的交互作用 p=.035：單純手術組事件較少、手術＋輔助治療組事件較多**、
  結論句「generally protective associations in the surgery alone group, but harmful associations in the surgery plus adjuvant therapy group」。

- **[D-S63] PASS（僅摘要層級）** Bates-Fraser LC, Masters M, Bodelon C, McCullough LE, Shams-White MM, Patel AV, Rees-Punia E.
  **Every move matters: physical activity, walking, sedentary behavior, and endometrial cancer survival.** *Cancer Causes Control.*
  2025;36(12):1743–1752. DOI: 10.1007/s10552-025-02060-w. PMID: 40859087. OA: N
  引用：Cancer Prevention Study-II、**n=1,016**、平均診斷年齡 72 歲、平均追蹤 13.5 年、**511 人死亡（232 任何癌症、60 內膜癌）**、
  **達指引兩倍者全因死亡 HR 0.71（95% CI 0.50–1.00）**、總癌症死亡無顯著、
  每週步行 <2 小時 vs 完全不走 HR 1.45（1.08–1.96）、久坐與存活無關。

- **[D-S64] PASS（僅摘要層級；隨機、陰性）** Zamorano AS, Wilson EM, Liu J, Leon A, Kuroki LM, Thaker PH, McCourt CK, Fuh KC, Powell MA,
  Mutch DG, Evanoff BA, Colditz GA, Hagemann AR.
  **Text-message-based behavioral weight loss for endometrial cancer survivors with obesity: A randomized controlled trial.**
  *Gynecol Oncol.* 2021;162(3):770–777. DOI: 10.1016/j.ygyno.2021.06.007. PMID: 34140179. OA: N｜NCT03169023
  引用：2017-05-18 至 2017-12-31、BMI ≥30 的內膜癌存活者 **n=80 隨機**、主要終點 6 個月體重、
  **兩組體重變化無差異（P=0.08）**、生活品質／身體活動／身體形象無差異、
  **參加者 vs 未參加者（278 人）體重變化亦無差異（P=0.85）**、
  **6 個月時體重增加者 47.7% vs 44.4%；減重 ≥5% 者 9.2% vs 11.2%**、結論句逐字。

- **[D-S65] PASS（僅摘要層級；陰性）** Santana BN, Soriano JV, Arencibia O, Petousis S, Margioula-Siarkou C, González D, Laseca M, Rave A,
  Martínez AM.
  **Impact of weight loss after treatment on survival outcomes of overweight and obese patients with early-stage endometrial cancer.**
  *Oncol Lett.* 2024;27(2):44. DOI: 10.3892/ol.2023.14177. PMID: 38106524. PMCID: PMC10722546. OA: N
  引用：2007-01–2019-12、**n=526**（過重 152＝28.90%／肥胖 374＝71.10%）、中位追蹤 76.17 個月、77 人（14.64%）死亡、
  存活者體重 86.4±17.9 → 84.6±16.4 kg（減 1.47 kg，P<0.001）；非存活者 84.7±15.7 → 84.7±14.6（減 0.63 kg，P=0.180）；
  **維持／增加 ≥5% vs 減少 ≥5%：全世代無顯著差異；僅 32–98 個月區間 P=0.025（log-rank）**；
  **多變項 12 個月體重變化 adjusted HR 1.01（95% CI 0.97–1.05，P=0.723）**。

- **[D-S66] PASS（OA；單臂可行性）** Smits A, Galaal K, Winnan S, Lopes A, Bekkers RLM.
  **Feasibility and Effectiveness of the Exercise Program in Endometrial Cancer; Feasibility and Acceptability Survivorship Trial
  (EPEC-FAST).** *Cancers.* 2022;14(22):5579. DOI: 10.3390/cancers14225579. PMID: 36428675. PMCID: PMC9688636. **OA: Y**｜NCT02367950
  引用：術後 6 週起 10 週個人教練課、符合 54 人、**同意 22 人（41%）**、出席率 86%、無不良事件、
  角色功能 P=0.02／情緒功能 P=0.02／認知功能 P=0.04／內臟脂肪百分比 P=0.039／六分鐘走路 P<0.001 顯著改善、
  **最大減重 3 個月 6.0 kg、6 個月 8.4 kg**。

- **[D-S67] PASS（僅摘要層級；隨機試驗性）** Koutoukidis DA, Beeken RJ, Manchanda R, Burnell M, Ziauddeen N, Michalopoulou M, Knobf MT,
  Lanceley A.
  **Diet, physical activity, and health-related outcomes of endometrial cancer survivors in a behavioral lifestyle program: the Diet and
  Exercise in Uterine Cancer Survivors (DEUS) parallel randomized controlled pilot trial.** *Int J Gynecol Cancer.* 2019;29(3):531–540.
  DOI: 10.1136/ijgc-2018-000039. PMID: 30723098. OA: N｜NCT02433080
  引用：英國 2 家醫院、2015-05–2015-12、篩 296 人收 60、**隨機 54（介入 29／常規 31）**、8 週團體介入、
  **8 週：飲食分數差異 7.5（95% CI 0.1–14.9，P=0.046）；身體活動 0.1 MET-小時/日（−1.6 至 1.8，P=0.879）；整體生活品質 5.0（−3.4 至 13.3，P=0.236）**；
  **24 週整體生活品質差異 8.9（0.9–16.8，P=0.029）**；遵從率 77%、無介入相關不良事件。

- **[D-S68] PASS** Miles T, Johnson N.
  **Vaginal dilator therapy for women receiving pelvic radiotherapy.** *Cochrane Database Syst Rev.* 2014;(9):CD007291.
  DOI: 10.1002/14651858.CD007291.pub3. PMID: 25198150. PMCID: PMC6513398. OA: N
  （前一版：*Cochrane Database Syst Rev.* 2010;(9):CD007291. DOI: 10.1002/14651858.CD007291.pub2. PMID: 20824858. PMCID: PMC4171967.）
  引用（2014 版）：檢索範圍逐字、**「We found no trials and therefore analysed no data.」「We identified no studies for inclusion」**、
  被排除但討論的研究（一個 RCT 顯示鼓勵擴張未改善性功能分數；小型 RCT 擴張 vs 震動治療無差異；「Three recent studies showed less stenosis
  associated with prophylactic dilation after radiotherapy」）、結論全段逐字。
  引用（2010 版）：**「Dilation during or immediately after radiotherapy can, in rare cases, cause damage」「Routine dilation during or soon
  after cancer treatment may be harmful」「some women may benefit from dilation therapy once inflammation has settled」**。

- **[D-S69] PASS（OA）** Noorian F, Abellana R, Zhang Y, Herreros A, Lancellotta V, Tagliaferri L, Sabater S, Torne A, Agusti-Camprubi E,
  Rovirosa A.
  **Impact of Vaginal Dilator Use and 68 Gy EQD2(α/β=3) Dose Constraint on Vaginal Complications in External Beam Irradiation Followed by
  Brachytherapy in Post-Operative Endometrial Cancer.** *J Pers Med.* 2024;14(8):838. DOI: 10.3390/jpm14080838. PMID: 39202029.
  PMCID: PMC11355937. **OA: Y**
  引用：**n=131**（Group-1 65 人單次 7 Gy／Group-2 66 人 5.5–7.0 Gy 在 68 Gy EQD2 限制下）、中位追蹤 60 個月、
  **陰道殘端復發 1/131（0.8%）**、**晚期陰道併發症 55.4%（36/65）vs 25.8%（17/66），p=0.003**、
  **多變項：Group-1 HR 1.99（p=0.021）、擴張器使用 <9 個月 HR 3.07（p=0.010）**。

- **[D-S70] PASS（OA）** Tahseen R, Ahmed Y, Tariq M, Abrar S, Ali N.
  **Compliance and clinical efficacy of vaginal dilator after radiotherapy for cervical and endometrial malignancies.**
  *Ecancermedicalscience.* 2023;17:1545. DOI: 10.3332/ecancer.2023.1545. PMID: 37377680. PMCID: PMC10292859. **OA: Y**
  引用：**n=54**（內膜癌 24＝44.4%／子宮頸癌 30＝55.6%）、放療後 1 個月開始衛教、3 個月評估、
  **遵從 36（66.6%）**：每週 2–3 次 22（40.7%）／每週 <2 次 8（14.8%）／每月 1 次 6（11.9%）／**完全沒用 18（33.3%）**；
  內診黏膜正常 32（59.3%）／有沾黏 20（37.0%）／密沾黏無法檢查 2（3.7%）；
  **36 位使用者中 29（80.6%）判定有效；每週 2–3 次者有效比例 72.4%（21/29）**。

- **[D-S71] PASS（OA）** Woopen H, Zwimpfer T, Brenner L, Liebrich C, Leitner K, Henry S, Müller C, Saner FAM, Ebner C, Dimitrova D, Mang C,
  Himsl I, Hell-Teutsch J, Van Gorp T, Braun C, Nurhayat Y, Müller M, Hanker L, Heinzelmann-Schwarz V, et al.
  **Patients' Perception of Follow-Up Care and Personal Health Status of 677 Long-Term Survivors of Gynecological Cancer from the Study
  "Expression IX-Long-Term Survival with Gynecological Cancer": The International NOGGO, ENGOT and GCIG Survey.** *Cancers.* 2026;18(10):1647.
  DOI: 10.3390/cancers18101647. PMID: 42193006. PMCID: PMC13204237. **OA: Y**
  引用：2019–2025、四國、**n=677**（診斷後 ≥5 年）、中位年齡 64 歲（26–92）、中位存活 7 年（5–38）、
  **子宮頸癌 46.6%／內膜癌 32.9%／卵巢癌 4.4%／其他 16.1%**、
  **36.9% 仍有身體或心理症狀：淋巴水腫 36.2%、熱潮紅 22.4%、注意力困難 21.1%、疲倦 20.9%、陰道乾澀 20.1%、尿失禁 18.9%**、
  健康自評（1–5）中位 2、**13.5% 差／很差**、有症狀與較差健康自評（p<0.001）及曾復發（p=0.001）相關、
  **13.6% 未接受追蹤照護**、**內膜癌存活者 CA-125 28.9%、Pap 50.5%**、
  **33.7% 完全不運動或每週 <1 小時、13.4% 抽菸、51.2% 每月飲酒 >1 次**、結論句逐字。

- **【D4 補充來源（PASS，僅摘要層級；正文引用時請按此書目）】**
  - **DeMari JA, Dressler EV, Foraker RE, Wells BJ, Smith S, Klepin H, Hundley WG, Lesser GJ, Shalowitz DI, Nightingale CL, Hernandez M,
    Weaver KE. Endometrial cancer survivors' perceptions of their cardiovascular disease risk (results from WF-1804CD AH-HA).**
    *Gynecol Oncol.* 2023;174:208–212. DOI: 10.1016/j.ygyno.2023.05.009. PMID: 37224793. PMCID: PMC10330616. OA: N｜NCT03935282
    （n=55；87%／76%／84% 三個比例；AHA Simple 7 各項中／差比例；16% 一年未看家醫科且較常回報經濟困難 22% vs 0%，p=0.02）
  - **Maxwell-Smith C, Hince D, Cohen PA, Bulsara MK, Boyle T, Platell C, Tan P, Levitt M, Salama P, Tan J, Salfinger S, Makin G,
    Mohan GRKA, Jiménez-Castuera R, Hardcastle SJ. A randomized controlled trial of WATAAP to promote physical activity in colorectal and
    endometrial cancer survivors.** *Psychooncology.* 2019;28(7):1420–1429. DOI: 10.1002/pon.5090. PMID: 30980691. OA: N
    （n=68 隨機；MVPA 介入 +45 分/週 vs 對照 −21 分/週，F₁,₁₂₆=5.14，P=0.025；舒張期高血壓者淨降 9.89 mmHg，F₁,₆₆=4.89，P=0.031）
  - **Arem H, Pfeiffer RM, Moore SC, Brinton LA, Matthews CE. Body mass index, physical activity, and television time in relation to
    mortality risk among endometrial cancer survivors in the NIH-AARP Diet and Health Study cohort.** *Cancer Causes Control.*
    2016;27(11):1403–1409. DOI: 10.1007/s10552-016-0813-7. PMID: 27730319. PMCID: PMC5738914. OA: N
    （n=580；中位追蹤 7.1 年、91 死；MVPA 15+ vs 0 HR 0.72，95% CI 0.43–1.21 非顯著；看電視 5+ vs <3 小時/日 HR 2.28，1.05–4.95）
  - **Johnson RL, Choy C. Patient-initiated follow-up of early endometrial cancer: a potential to improve post-treatment cardiovascular
    risk?** *Arch Gynecol Obstet.* 2022;305(2):431–437. DOI: 10.1007/s00404-021-06166-9. PMID: 34363114. PMCID: PMC8840909. **OA: Y**
    （n=98 服務評估；中位追蹤 54 個月無復發；91% 願推薦；成本節省約 96.5%。**無對照組，只能寫成服務評估**）

- **【D3 補充來源（PASS，僅摘要層級）】**
  - **Hahn BA, Kleeven A, Richir MC, Witkamp AJ, Kuijpers AMJ, de Jong T, Qiu S, Coert JH, Krijgh DD. Objectifying Clinical Outcomes After
    Lymphaticovenous Anastomosis and Vascularized Lymph Node Transfer in the Treatment of Extremity Lymphedema: A Systematic Review and
    Meta-Analysis.** *Microsurgery.* 2025;45(3):e70050. DOI: 10.1002/micr.70050. PMID: 40066947. PMCID: PMC11895410. **OA: Y**
    （52 篇；**下肢合併臨床改善 34.16%（95% CI 23.93–44.40）**；LVA 31.87%（18.60–45.14）、VLNT 39.53%（19.37–59.69）；上肢 36.46%）
  - **Jeong HH, Kwon JG, Kim TH, Suh HP, Pak CJ, Kim D, Hong JP. Prophylactic Surgery for Gynecologic Cancer-Related Lower Extremity
    Lymphedema.** *Plast Reconstr Surg.* 2026 [Epub]. DOI: 10.1097/PRS.0000000000013163. PMID: 42085589. OA: N
    （前瞻介入 26 人 vs **回溯**對照 88 人；1 年水腫發生率 **8% vs 49%，p<0.001**。**回溯對照、單中心、n 小，只能寫成「有一筆小型對照研究」**）
  - **Tsukagoshi M, Maegawa J. Compression Therapy in Patients Aged 65 and Older with Late Stage II Secondary Lower Limb Lymphedema.**
    *Ann Vasc Dis.* 2026;19(1):26–30. DOI: 10.3400/avd.oa.26-00030. PMID: 42609764. PMCID: PMC13478886. **OA: Y**
    （婦癌術後續發性下肢淋巴水腫、ISL 晚期 II 期、**≥65 歲 n=71**；平織 51／圓織 20；**握力 21.1 kg vs 19.1 kg，p=0.004**）
  - **Li P, Zhao Z, Sun Y, Xia S, Shen W. The prognostic effect and mechanism of erysipelas in cancer-associated lymphedema.** *Sci Rep.*
    2025;15(1):5518. DOI: 10.1038/s41598-025-90200-2. PMID: 39953144. PMCID: PMC11828868. **OA: Y**
    （n=1,016 抽脂後；**既往丹毒是復發最強獨立風險因子 OR 3.98，95% CI 2.81–5.69**；nomogram C-index 0.757）
  - **Cibula D, Borčinová M, Marnitz S, Jarkovský J, Klát J, Pilka R, Torné A, Zapardiel I, Petiz A, Lay L, Sehnal B, Ponce J, Felsinger M,
    Arencibia-Sánchez O, Kaščák P, Zalewski K, Presl J, Palop-Moscardó A, et al. Lower-Limb Lymphedema after Sentinel Lymph Node Biopsy in
    Cervical Cancer Patients.** *Cancers.* 2021;13(10):2360. DOI: 10.3390/cancers13102360. PMID: 34068399. PMCID: PMC8153612. **OA: Y**
    （**子宮頸癌 n=150，族群標籤必寫**；24 個月累積輕度 17.3%／中度 9.2%／重度 0.7%；**中位發生 9 個月**；另 22% 暫時性水腫 6 個月內自行緩解；
    主觀自述 10.7%，與客觀量測僅弱相關；結論「does not eliminate the risk of mild to moderate LLL」）
  - **Tümkaya MN, Şimşek E, Seven M. Lower Extremity Lymphedema Prevention Program for Women Undergoing Gynecologic Cancer Surgery:
    A Pilot Randomized Controlled Study.** *Oncol Nurs Forum.* 2026;53(5):1–15. DOI: 10.1188/26.ONF.E26535375. PMID: 42690377. OA: N
    （**n=27 試驗性隨機**（介入 14／對照 13）；參與率 93.3%、完成率 96.4%、滿意度 4.54/5；生活品質、整體健康、自我效能、水腫症狀顯著改善；
    **「No significant short-term changes in leg circumference measurements were observed」**）
  - **Zalawadia S, Lekka S, Al-Jumaili Z, Brockbank E, Manchanda R, Jeyarajah A, Phadnis S, Sideris M. Morbidity, Recurrence and Survival
    Following Pelvic Exenteration for Gynaecological Malignancies: A Retrospective, Single-Centre Study.** *J Clin Med.* 2026;15(10):3957.
    DOI: 10.3390/jcm15103957. PMID: 42194919. PMCID: PMC13207788. **OA: Y**（見 [D-S30] 註）

### 六、台灣官方（PASS）

- **[D-S72] PASS（官方開放資料原始檔，2026-09-10 實下載；HTTP 200，565,406 bytes；OpenDocument Spreadsheet；解壓 `content.xml` 逐列解析，
  共 6,013 列項目）**
  【機構型來源，無作者欄】衛生福利部中央健康保險署。**《全民健康保險醫療服務給付項目及支付標準》現行給付項目全表**
  （資源說明：醫療服務給付項目 **1140501 生效**）。
  資料集頁面（人類可讀）: https://data.gov.tw/dataset/9405
  官方檔案（機器介面）: https://info.nhi.gov.tw/api/iode0000s01/Dataset?rId=A21030000I-D20003-004
  健保署支付標準頁面（人類可讀）: https://www.nhi.gov.tw/ch/cp-17728-d8596-3848-1.html
  Route: curl 下載 ODS → `unzip content.xml` → 以正則逐 `table:table-row` / `table:table-cell` 解析（**注意：非貪婪比對 `/>` 會被
  儲存格內的 `<text:s/>` 截斷，必須用 `<table:table-cell\b[^>]*/>|<table:table-cell\b.*?</table:table-cell>` 兩式擇一**）→ 欄位為
  〔診療項目代碼｜健保支付點數｜生效起日｜生效迄日｜英文項目名稱｜中文項目名稱｜備註〕→ 逐列關鍵字檢索並列印完整備註欄原文。
  **本 brief 引用的逐字條文與檢索結果**：
  - **47091B　淋巴水腫照護-徒手淋巴引流(須達四十分鐘)　450 點　生效 2022/03/01**；備註逐字：
    「1.適應症：**癌症末期淋巴水腫病人** 2.執行人員：須接受淋巴照護相關訓練。執行完成後需有適應症、執行過程及執行時間的紀錄。3.提升兒童加成項目。」
  - **全表逐字檢索負面結果**：「壓力衣」0 筆、「彈性衣」0 筆、「彈性襪」0 筆；
    「氣壓」僅 17002B（最大吸氣壓及最大吐氣壓，85 點）與 23305C（氣壓式眼壓測定，135 點）兩項無關項目；
    「淋巴水腫」除 47091B 外 0 筆。
  - 復健相關項目：42016C 物理治療評估 240 點（備註逐字含「同一病患治療期間一個月限申報一次」「同一治療期間超過三個月者，不予支付」）；
    42017C 中度治療-中度 265 點、42018C 中度治療-複雜 400 點（PTM 1–14 清單逐字，含「PTM 11.按摩 Massage」，**無淋巴引流字樣**）；
    42019C 複雜治療 500 點（PTC 1–7，無淋巴相關）；43026C 職能治療評估 240 點；45031C 一般職能治療 299 點；45095C 特殊職能治療 325 點。
  - **26072B 正子造影-全身 36,500 點／26073B 正子造影-局部 26,500 點**：備註腫瘤適應症逐字「(1)乳癌、淋巴癌之分期、治療及懷疑復發或再分期。
    (2)大腸癌、直腸癌、食道癌、頭頸部癌(不包含腦瘤)、原發性肺癌、黑色素癌、甲狀腺癌及**子宮頸癌**之分期及懷疑復發或再分期。」
    ——**全表無「子宮體癌」列於 PET 適應症**；並含「C.懷疑復發或再分期：……(**不得用於例行之追蹤檢查**)」與「D.……須於病歷中說明施行正子造影之
    必要性理由。」「E.配合腫瘤治療計畫者方得以正子造影作為療效評估項目，未有後續積極處置之計畫者，不得施行。」
  - **15017C 婦科細胞檢查 245 點**：備註逐字「1.子宮頸或陰道抹片同一病人3~6個月內限做1次。2.6個月內需重新施做之適應症：(1)曾罹患過子宮頸癌或
    癌前病變之婦女(2)最近一次子宮頸抹片檢查結果為異常之婦女(3)免疫功能受抑制的高危險群婦。」
  - **12077C／27053C ＣＡ–１２５腫瘤標記 各 400 點**：**備註欄空白**；12021C 癌胚胎抗原檢驗 400 點備註空白；12080B SCC 腫瘤標記 400 點備註空白。
  - **33070B 電腦斷層造影－無造影劑 3,800 點／33071B 有造影劑 4,560 點／33072B 有/無造影劑 5,035 點**：備註僅「申報費用時應檢附報告。」
  - 近接治療相關（供 D2 一句帶過，完整討論歸 B2）：37007B 3,236 點／37008B 1,650 點／37010B 5,611 點／37018B 4,126 點／37019B 6,600 點／
    37047B 213,662 點。
  **版本註記**：此為 1140501 生效版；引用時請標明版本，且**永不推論條文以外的給付與否**。

- **[D-S73] PASS（法規全文＋官方附表 PDF，2026-09-10 實下載）**
  【機構型來源】**《全民健康保險保險對象免自行負擔費用辦法》**（法規代碼 L0060015），全國法規資料庫。
  法規頁（人類可讀）: https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=L0060015
  **附表一 PDF**（〈全民健康保險重大傷病項目及其證明有效期限〉）: https://law.moj.gov.tw/LawClass/LawGetFile.ashx?FileId=0000375263&lan=C
  （HTTP 200，433,100 bytes；`pdftotext -layout` 全文檢索）
  Route: 法規檢索 → 取 pcode → curl 取條文 HTML 去標籤 → 逐條抄錄；附表一另 curl 下載 PDF → pdftotext → grep 癌症段。
  **引用逐字**：
  - 附表一（**113-12-31 以前適用**與**114-01-01 以後適用**兩版皆同）第一項「需積極或長期治療之癌症」：
    (一) C73 甲狀腺惡性腫瘤 **三年**；(二) 口腔、口咽及下咽惡性腫瘤第一期 **三年**；(三) C50.011-C50.929 乳房惡性腫瘤第一期 **三年**；
    (四) C53.0-C53.9、C55 子宮頸惡性腫瘤第一期 **三年**；**(五) C00.0-C96.9（不含 C73、C94.4、C94.6）除(一)-(四)之其他惡性腫瘤　五年**。
    → **子宮體癌 C54 落在第(五)款，效期 5 年。**
  - 第 5 條逐字（重新申請期限與效期銜接）：見 D1／D4 台灣端引文。
  - 第 6 條逐字（免自行負擔費用範圍三款）：見 D4 台灣端引文。
  - 第 2 條逐字（申請文件；「診斷證明書自開立日起三十日內有效，逾期不予受理。」）、第 3 條（保險人 14 日內核定、註記於健保憑證）。

- **[D-S74] PASS（衛福部官方新聞稿，2026-09-10 實抓；HTTP 200）**
  【機構型來源】衛生福利部。〈**公布112年國人癌症登記資料分析結果 守護健康未來 從癌症篩檢開始**〉（建檔 114-12-30、更新 115-01-05；資料來源：國民健康署）。
  URL: https://www.mohw.gov.tw/cp-7171-84987-1.html
  Route: WebSearch 找 mohw 鏡像 → curl 下載 HTML → 去標籤取內文（**hpa.gov.tw 原始頁 TLS 失敗，見 FAIL-1**）。
  引用逐字：112 年新發生癌症 138,051 人；**女性標準化發生率順位「依序為乳癌、肺癌、大腸癌、甲狀腺癌、子宮體癌、肝癌、卵巢癌、皮膚癌、胃癌、
  子宮頸癌」（子宮體癌女性第 5 位）**；男女合計新發生人數第 10 位為子宮體癌；「**子宮體癌及乳癌為57歲**」（發生年齡中位數，全癌症中位數 65 歲）。

- **[D-S75] PASS（衛福部官方新聞稿，2026-09-10 實抓；HTTP 200）**
  【機構型來源】衛生福利部。〈**公布110年國人癌症登記資料分析結果 五癌篩檢定期做 早發現早治療**〉（建檔／更新 112-11-10；資料來源：國民健康署）。
  URL: https://www.mohw.gov.tw/cp-16-76564-1.html
  引用逐字：「**目前國際間尚無實證建議對攝護腺癌、胰臟癌、非何杰金氏淋巴瘤及子宮體癌的無症狀者進行篩檢**，若民眾察覺自身有以下異常症狀，
  請務必就醫並遵循醫師指示，及早診治。……**子宮體癌：不正常的出血，包括：月經週期紊亂、長期持續性出血、月經長久不來後突然大量出血或者
  停經後的出血。**」（110 年女性標準化發生率順位中子宮體癌亦為第 5 位。）
  **版本註記：110 年資料，發生數與順位以 [D-S74]（112 年）為準；本件只用於「無篩檢建議＋症狀清單」的官方措辭。**

- **[D-S76] PASS（衛福部官方新聞稿＋官方轉介網站，2026-09-10 實抓）**
  【機構型來源】衛生福利部。〈**癌症資源中心 實體與網路服務並進 癌症照護新時代 抗癌路上不孤單**〉（建檔 112-04-06、更新 113-03-21；資料來源：國民健康署）。
  URL: https://www.mohw.gov.tw/cp-6565-74177-1.html
  引用逐字：「**國民健康署補助癌症希望基金會共同協助推動104家醫院成立「癌症資源中心」**，讓癌友及其家人能夠獲得**資訊提供、心理支持及資源取得**
  等3大重要因素之相關服務，透過實體與網路雙管齊下方式，**迄今共服務150萬人次**。」；
  「國人癌症5年存活率已從民國92-96年的50%，提升到民國105-109年的**61.5%**」（**全癌症，非子宮體癌，引用必須標明**）。
  官方頁提供之轉介連結：**台灣癌症資源網 https://www.crm.org.tw/**（2026-09-10 curl HTTP 200，`<title>台灣癌症資源網</title>`）。
  Route: WebSearch → curl 新聞稿 HTML 去標籤 → 逐字抄錄 → 另 curl 驗證 crm.org.tw 可達。

- **[D-S77] PASS（法規全文＋官方附表 PDF，2026-09-10 實下載；HTTP 200，751,186 bytes；`pdftotext -layout` 後 4,584 行）**
  【機構型來源】衛生福利部。**《身心障礙者輔具費用補助辦法》**（法規代碼 D0050060）及其**附表〈身心障礙者輔具費用補助基準表〉**。
  法規頁（人類可讀）: https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=D0050060
  附表 PDF: https://law.moj.gov.tw/LawClass/LawGetFile.ashx?FileId=0000326887&lan=C
  Route: 法規檢索 → curl 條文 HTML 去標籤 → 逐條抄錄；附表 curl → pdftotext → grep。
  引用逐字：第 2 條十類輔具清單；第 3 條補助比率（低收入戶全額／中低收入戶 75%／一般戶 50%）；
  第 7 條「直轄市、縣（市）主管機關**得考量財務狀況，增列補助項目，或調高最高補助金額**。」「輔具補助，每人每二年度以補助四項為原則。」
  **附表逐字檢索負面結果：「壓力衣」0 筆、「彈性衣」0 筆、「彈性襪」0 筆、「淋巴」0 筆、「水腫」0 筆。**

### 七、FAIL / NOT-CITABLE（保留，寫明原因）

- **FAIL-1（台灣，重要 gap）** 國民健康署《癌症登記報告》歷年報告頁與**子宮體癌依期別之五年存活率**：
  `https://www.hpa.gov.tw/Pages/List.aspx?nodeid=269`、`https://www.hpa.gov.tw/Pages/Detail.aspx?nodeid=4878&pid=19734`、
  `https://www.hpa.gov.tw/Pages/List.aspx?nodeid=119`
  → **curl 回 SSL error 60（unable to get local issuer certificate），加 `--cacert /root/.ccr/ca-bundle.crt` 仍同**（伺服器端未送中繼憑證，
  非代理政策問題；`curl $HTTPS_PROXY/__agentproxy/status` 顯示 `bundleCoversEveryHost: true`）；
  WebFetch 回 `ROBOTS_DISALLOWED`（robots.txt 取得時同一 TLS 錯誤）。
  台灣癌症登記中心 `https://tcr.cph.ntu.edu.tw/main.php?Page=N2` → **connection reset（ws_closed_mid_exchange）**。
  → **正文寫「台灣官方的子宮體癌期別存活數字，我查不到可引用的版本」，不得以國外數字代替。**

- **FAIL-2（台灣）** 健保署 HTML 頁面 `https://www.nhi.gov.tw/ch/cp-6089-0c619-2957-1.html`（重大傷病免自行負擔範圍）與
  `https://www.nhi.gov.tw/ch/cp-6091-08ad9-2957-1.html`（申請須知）→ **HTTP 403（Cloudflare）**。
  → 重大傷病的條文改以全國法規資料庫原文為據（[D-S73]），內容完整、且是法規本文，證據力更強。

- **FAIL-3（文獻，preprint）** Tang R, Li G, Duan Z, Zhu Y. *Age-specific relative and absolute burden of subsequent primary non-gynecologic
  cancers after endometrial cancer: a population-based SEER study.* Research Square preprint. DOI: 10.21203/rs.3.rs-10744519/v1（無 PMID、無 PMCID）。
  → **預印本、未經同儕審查，且作者自陳結果「not for individual risk prediction or surveillance thresholds」。不可引。**
  其 SIR 1.038（1.023–1.053）等數字**不得進正文**；第二原發癌一律用 [D-S16][D-S17]。

- **FAIL-4（指引措辭）** Oaknin A, Bosse TJ, Creutzberg CL, Giornelli G, Harter P, Joly F, Lorusso D, Marth C, Makker V, Mirza MR,
  Ledermann JA, Colombo N, ESMO Guidelines Committee. *Endometrial cancer: ESMO Clinical Practice Guideline for diagnosis, treatment and
  follow-up.* **Ann Oncol.** 2022;33(9):860–877. DOI: 10.1016/j.annonc.2022.05.009. PMID: 35690222. OA: N。
  → Europe PMC **abstractText 為空**，全文付費牆內，**追蹤間隔的原文措辭無法取得**。
  **正文不得引用 ESMO 2022 的任何追蹤措辭或間隔。** 需要指引間隔時用 [D-S3]（SEOM-GEICO 2025，OA，且自標 V, C）。

- **FAIL-5（依規則不引）** NCCN Guidelines（Uterine Neoplasms）：依 RESEARCH-COMMON 硬規則，**NCCN 專業版對抓取回 403，本專題不引 NCCN**。
  [D-S15] 的摘要中轉述了 NCCN 立場（「NCCN recommends symptom and exam-based surveillance for all endometrial cancers after remission,
  regardless of cancer stage and histology」）——**這是第三方轉述，不可當成 NCCN 原文引用**；正文若要表達同方向，用 [D-S1][D-S3][D-S4]。

- **FAIL-6（台灣，gap）** 台灣本土的**下肢淋巴水腫發生率**、**婦癌術後回工作率**、**內膜癌復發後救援結果**、
  **氣壓治療／淋巴靜脈吻合／淋巴結移植的健保或自費列項**：全部**查無可引用的官方或期刊來源**。
  健保支付標準全表[D-S72]中相關關鍵字為 0 筆——**「查不到列項」可以寫，「沒有給付」不可以寫**。

- **FAIL-7（官方頁不可達）** 癌症希望基金會官方網站 `https://www.ecancer.org.tw/` → **HTTP 403**（2026-09-10）。
  社家署輔具資源入口網 `https://newrepat.sfaa.gov.tw/home/gov-repat-service/wlfrIntro3` → WebFetch **ConnectTimeout**。
  → 社會資源一律走 [D-S76]（衛福部新聞稿）＋ **crm.org.tw**（實測可達）；**不引任何第三方短網址與媒體整理頁**。

- **NOT-CITABLE-1（設計問題，非查證失敗）** 質性研究：Liu G, Liu Y, Hu J, Deng S, Fan J. *Home self-management experience of gynaecological
  tumour patients with lower limb lymphoedema: a qualitative study.* Prim Health Care Res Dev. 2025;26:e81. DOI: 10.1017/S1463423625100406.
  PMID: 41077997. PMCID: PMC12555075. OA: Y（n=16，Colaizzi 七步法）。
  → **可用來描述「病人普遍反映資源不均、居家自我管理技巧不足、心理壓力大」這種質性主題，但不得引用任何比例或數字。**

---

## 附：寫作者的交叉引用檢查表（D 組四篇）

| 主題 | 歸屬 | D 組怎麼處理 |
|---|---|---|
| 分子分型與組織型名詞 | A2 | 第一次出現一句帶過，指向 A2 |
| FIGO 分期版本 | A3 | **本組凡提期別一律標「2009 版」或「2023 版」**（[D-S14] 是 2009 版、[D-S11] 同時標了兩版） |
| 手術與前哨淋巴結該不該做 | A4 | D3 只寫水腫端數字，決策指向 A4 |
| 風險分組（ESGO/ESTRO/ESP） | B1 | **D1 不得自列分組表**；提到「低風險／高風險」時一句指向 B1 |
| 輔助放療的取捨（PORTEC-1 兩個結論） | B1 | D2 引用 PORTEC-1 救援結果時，**必須一句指向 B1** 並不得重述輔助治療的決策 |
| 陰道近接治療實務 | B2 | D2 提到救援近接治療時一句帶過 |
| 化療（PORTEC-3／GOG-258／GOG-249） | B3 | D2 不引 |
| 分子分型改治療 | B4 | D2 引 [D-S33][D-S34] 只談「復發後的預後」，不談治療降階／升階 |
| 免疫治療療效數字 | B5 | **D2 一個數字都不放**，只寫位置＋指路 |
| 生育保留 | C1 | 不涉及 |
| 體重與代謝的病因學 | C2 | D4 只寫「治療後」端，病因學指向 C2 |
| Lynch 與遺傳 | C3 | **D1 的第二原發癌段必須寫「Lynch 族群另計，見 C3」** |
| 荷爾蒙、骨質、停經症狀 | C4 | **D4 一句指向 C4，不展開** |
| 追蹤 | D1 | 本組 |
| 復發 | D2 | 本組 |
| 淋巴水腫 | D3 | 一般原則指向 `bc-lymphoedema` |
| 日常 | D4 | 本組 |
| 腫瘤標記怎麼讀 | 站上 `sit-markers` | D1 一句指路 |
| 再照射一般原則 | 站上 `sit-reirradiation` | D2 一句指路 |
| 寡轉移 | 站上 `sit-oligomet` | D2 一句指路 |
| 擴張器與性生活 | 站上 `cx-dilator-sex` | D4 一句指路 |
| 復發恐懼 | 站上 `care-fear` | D4 一句指路 |
| 腿腫／發燒的急症判斷 | 站上 `care-thrombosis`／`care-fever` | **D1、D3 各一句，且必須寫「不能等」** |
| 重大傷病以外的文書 | 站上 `sit-paperwork` | D4 一句指路 |
| 自費怎麼問 | 站上 `care-self-pay` | D3、D4 各一句（**不寫任何金額**） |
| 骨盆腔放療技術與副作用 | 站上 `pel-*` 專題 | D3 提到放療與水腫時一句指路 |
