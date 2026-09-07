# Brief D — GBM 專題「之後」群（D1–D3）＋全專題台灣端總掃

研究員：Group D｜查證日期：**2026-09-03**
期刊書目資料全部經 Europe PMC REST 逐筆核對（title／journal／year／volume(issue)／pages／DOI／PMID／isOpenAccess）；
可取得全文者（Europe PMC fullTextXML）已抓下逐句核對，引語為原文。
台灣端：健保署 `info.nhi.gov.tw` 藥品給付規定 API（逐條 PDF）、健保署支付標準全表 TXT（21 MB，全文檢索）、
全國法規資料庫 `law.moj.gov.tw` 原文、台灣癌症登記中心資料檔——**全部為本次實際抓取，非二手轉述**。**未引用 NCCN。**

**引用規則：只有標 PASS 的來源可以進正文。** FAIL / NOT-CITABLE 條目保留在最後。所有 D[Sn] 編號全 brief 唯一。

---

## ⚠ 與 SPEC 假設不同形狀的事（動筆前必讀，共 14 條）

**1.（最重要）紅線 8 有一個算術陷阱：GBM 化放療後的假性惡化比例，比站上〈影像變壞，不一定是病變壞〉的 6% 高得多，方向是反的。**
`sit-pseudo.html` 的「往好處想的機率是個位數」是**免疫治療**的合併發生率 6.0%[站上出處 Park 2020]，
而且該篇自己就寫了「膠質母細胞瘤……放療後 3 個月的假性惡化比例是 19.4%、6 個月是 7.0%，比免疫治療的數字高得多」。
GBM 的數字更高：Brandes 2008 的世代裡，化放療後**第一次** MRI 顯示病灶變大的 50 人中，**32 人（64%）事後判定是假性惡化**，
MGMT 甲基化者更高達 21/23（91%）[D[S4]]。
→ **「往好處想的機率是個位數」這句話不可以搬進 D1**，搬進去就是引用錯誤的族群。
→ 但「不得更寬鬆」要靠**別的方式**守住，見 D1 的 Claim ceiling：
  (a) 用**正確的分母**——Blakstad 三個月那張片子，53 人假性惡化、113 人真惡化、104 人穩定；
      **在「片子看起來變壞」的 166 人裡，回頭重判是假性惡化的約三分之一（53/166 = 31.9%，本 brief 由原文數字換算），
      真的惡化的約三分之二**[D[S3]]。這句話與 sit-pseudo 的「往好處想的機率並不比往壞處想高」**方向一致、且不更寬鬆**。
  (b) 判讀規則（只能回頭看、四到八週是判讀規則不是自己領走的等待期、判斷臨床穩定的是醫師）**逐字沿用**，一個字都不放寬。

**2. 「四到八週」在 GBM 有官方原文，而且 RANO 2.0 把窗口改寫成「放療後十二週」。**
EANO 2021 原文：「in the event of suspected disease progression, **short-term control MRI within 4–8 weeks** might be reasonable
to confirm progression」；同段並寫「Pseudoprogression … and pseudoresponse … are **most likely to occur during the first 3 months
of treatment but can also occur later**」[D[S5]]。
RANO 2.0（2023）另立一條**更硬的規則**：「Since the incidence of pseudoprogression is high **in the 12 weeks after radiotherapy**,
**continuation of treatment and confirmation of progression during this period with a repeat MRI, or histopathologic evidence of
unequivocal recurrent tumor, are required to define tumor progression**」[D[S2]]。
→ D1 要同時寫這兩個數字，而且要點明**它們都是「試驗判讀規則」，不是回診間隔**——這正好是 sit-pseudo 已經立過的線。

**3. RANO 2.0 把「基準線」從術後 MRI 改成放療後 MRI，而且把 GBM 的非增強病灶踢出評估。**
原文：「In the newly diagnosed setting, **the postradiotherapy magnetic resonance imaging (MRI), rather than the postsurgical MRI,
will be used as the baseline**」；「For IDH wild-type glioblastoma, **the nonenhancing disease will no longer be evaluated except
when assessing response to antiangiogenic agents**」[D[S2]]。
→ 第二句就是**假性反應**寫進判讀標準的證據：只有在用抗血管新生藥（bevacizumab）時才回頭看 T2/FLAIR。
→ SPEC 只寫「RANO 與 RANO 2.0 判讀標準的原文」，沒有預期到「基準線換了」這件事——但這件事對病人很有用：
  **你那張「術後片子」不是後面拿來比的那一張。**

**4. 追蹤間隔的「證據等級」比 SPEC 假設的低很多，而且唯一一個大型資料是**觀察性**、有 immortal-time bias。**
EANO 2021 對療程結束後的措辭是「**an initial interval between scans of 2–6 months is common practice**」——
用的是「common practice（慣例）」，不是建議等級[D[S5]]。
INTERVAL-GB（英愛 26 中心、754 位 WHO grade 4 病人）記錄了兩套建議：NICE（術後 <72 小時；此後每 3–6 個月 MRI）
與 EANO（術後 <48 小時；每 3 個月 MRI）；**實際遵從率只有 52.8% 與 24.9%**；
多變項 Cox 顯示「符合建議追蹤的時間愈長，OS 愈長」（NICE HR 0.56、EANO HR 0.54，皆 p<0.001），**但 PFS 沒有差別**[D[S10]]。
→ **PFS 沒差、OS 有差**，這個組合是典型的「活得久的人才有機會照更多次片」（immortal time / guarantee-time bias）。
  作者自己的結論句就是「**Prospective trials are needed to determine whether regular or symptom-directed MRI influences outcomes**」。
→ **D1 不可寫「照得越勤活得越久」。** 這條要當成寫作教材：一個看起來很誘人的關聯，為什麼不能拿來當理由。

**5. 灌注影像與 MR spectroscopy 的準確度數字，比 SPEC 語氣裡的「有限制」還要好看——所以限制要另外寫。**
van Dijken 2017 統合分析（高惡性度膠質瘤治療反應判讀）：一般 MRI 敏感度 68%／特異度 77%；
DSC 灌注 87%／86%；DCE 灌注 92%／85%；**MR spectroscopy 91%／95%（九篇、203 人）**[D[S6]]。
→ 數字漂亮，但**特異度 95% 的信賴區間是 65–99%**（原文），而且每格研究數都很少。
→ 真正的限制在別處：RANO/EANO 2025 年的 PET 更新自己寫「**the scarcity of class 1 evidence showing that incorporating PET
  imaging into clinical workflows improves patient outcomes**」[D[S8]]——**準確度高 ≠ 改變結果**。這句要進 D1。

**6. D3 的「復發後怎麼辦」有一件事比 SPEC 假設的更硬：EANO 對再開刀的時間點寫了一條明確的話。**
「Second surgery is an option for ~20–30% of patients, commonly with symptomatic but circumscribed relapses diagnosed
**not earlier than 6 months after initial surgery**. **Second surgery earlier than 6 months after initial surgery increases the risk
of unnecessary intervention on the basis of pseudoprogression**」[D[S5]]。
→ **D1 與 D3 在這裡接上了**：假性惡化不是一個影像學上的趣聞，它會讓人白挨一刀。這是兩篇之間最好的接點。

**7. bevacizumab 的「不延長生命但改善症狀」這個框架，EANO 有一句可以逐字引的原文。**
「**The main value of this agent in routine clinical practice is transient symptom control and the option for sparing treatment
with steroids in symptomatic patients with large tumours.**」[D[S5]]
同一份文件另寫：「Bevacizumab … is approved … in the USA, Canada, Switzerland and several other countries outside the European
Union, but **no OS benefit has been demonstrated from its use**」[D[S5]]。
→ 這兩句比自己組裝的說法安全得多。**但注意：「省類固醇」在隨機試驗裡沒有被當主要終點量過**——
  BRAIN 試驗只寫「**There was a trend for patients who were taking corticosteroids at baseline to take stable or decreasing doses
  over time**」（趨勢，非統計檢定）[D[S40]]。所以「改善類固醇用量」只能寫到**趨勢**這一格，不可以寫成「證實可以減類固醇」。

**8. 台灣端翻盤了三次：A 組標為 gap 的四項，我用另外兩條路全部查到原文。**
- **temozolomide 給付規定第 9.25 條**逐字取得（同步期與維持期都在條文裡，且需事前審查）[D[S60]]；
  **bevacizumab 給付規定第 9.37 條第 2 項**逐字取得（限復發 GBM、單獨使用、每次事前審查 12 週）[D[S61]]。
  兩者本日（2026-09-03）以健保署藥品給付規定 API 重新抓取 PDF 覆核，內容與 A 組轉述一致。
- **vorasidenib 的台灣藥證查到了**：食藥署「未註銷藥品許可證資料集」中，**VORANIGO 瓦拉固膜衣錠 10 mg／40 mg，
  衛部藥輸字第 029063／029064 號，發證日 2025/12/23、有效日期 2030/12/23**，適應症逐字可引[D[S68]]。
  A 組因 `info.fda.gov.tw` DNS／TLS 失敗而標 gap；**改走政府資料開放平臺的食藥署 API（data.fda.gov.tw）就通了**。
- **5-ALA 的台灣藥證也查到了**：**Gliolan 格麗藍口服溶液用粉劑，衛署藥輸字第 025524 號，發證 2012/04/20、
  有效日期 2027/04/20**，適應症「用於成人患者進行惡性神經膠質瘤(WHO 分級 III 及 IV)手術期間的惡性組織顯影」[D[S68]]。
- **但兩者在健保藥品給付項目查詢都是 0 筆**（以成分名 vorasidenib、aminolevulinic acid 查詢）[D[S63]]。
  → **正確寫法：「有藥證、我在健保藥品給付項目查不到品項」，不可寫成「健保沒有給付」。**
- 另外撿到 SPEC 沒列的三樣：**carmustine 植入劑（Gliadel）給付規定第 9.35 條**（限復發性 GBM 手術輔助、
  **不得與 temozolomide 併用**、需事前審查）[D[S62]]；**lomustine（CCNU）現行仍有四個健保品項、但沒有對應的
  「藥品給付規定」條文編號**[D[S63]]；**regorafenib 給付規定第 9.51 條只寫大腸直腸癌、胃腸道間質瘤、肝細胞癌
  ——沒有膠質母細胞瘤**[D[S65]]，食藥署仿單的適應症也一樣只有這三個癌別[D[S68]]。
- **台灣的腦癌發生數查到了**（A 組因 hpa.gov.tw TLS 失敗而 gap）：台灣癌症登記中心長期趨勢資料檔，
  **2023 年腦癌新發個案 742 人（男 410、女 332），年齡標準化發生率 2.41／10 萬**[D[S69]]。
  **但「GBM 佔多少比例」仍然是 gap**——癌症登記公開資料只到「腦癌」這一層，沒有組織型態別；
  衛福部 112 年癌症登記報告新聞稿只公布十大癌症，腦不在內[D[S70]]。
- **癲癇與駕照的法規原文也取得了**（屬 C 組主場，這裡只登錄查證結果）：全國法規資料庫《道路交通安全規則》
  （修正日期 **民國 115 年 6 月 26 日**）第 64 條第一項第一款第六目之 1「**癲癇。但檢具醫療院所醫師出具最近二年以上
  未發作診斷證明書者，不在此限。**」、第 52-3 條（換照與診斷證明書規定）[D[S64]]。

**9. D2 最後一節有比 SPEC 預期更強的實證，而且是亞洲資料。**
SPEC 問「有沒有研究測過 GBM 病人簽署預立醫療文件的時機與比例」——有，而且是韓國單一醫學中心、串接國民健康保險資料庫：
惡性膠質瘤 229 人 vs 五大實體癌 4,283 人，**預立醫療照護諮商（ACP）文件記載率 20.1% vs 58.0%（aOR 0.13）**；
**維生醫療決定「由病人本人決定」者只有 21.4%，實體癌是 67.1%（aOR 0.07）**[D[S29]]。
再加上 Triebel 2009：惡性膠質瘤病人**確診後不久**，就有**超過 50%** 在標準化醫療決定能力量表上出現能力受損（marginally capable / incapable）[D[S27]]。
→ 「腦瘤病人的文件要比別的癌別早談」不再是常識論述，是**有數字的論述**。

**10.（D3 最重要的一條）REGOMA 沒有被確認：regorafenib 在 GBM AGILE 第三期平台試驗裡輸了，而且已被移出指引。**
SPEC 寫「regorafenib REGOMA 的結果與其限制」，預期的是「第二期正向、要等第三期」。第三期出來了，是**負的**：
GBM AGILE（NCT03970447）的 regorafenib 臂結論原文——「GBM AGILE **did not show superiority of regorafenib over control**
in RD (lomustine) or NDU (temozolomide + radiotherapy) glioblastoma, **yet caused increased toxicities**.
Regorafenib **has been removed from National Comprehensive Cancer Network guidelines** as a treatment option for RD.」
（JCO 2026;44(18):1676–1686）[D[S35]]。同期 Neuro-Oncology 的社論標題就叫
「Gods do play dice: **the activity of regorafenib in glioblastoma not confirmed**」[D[S36]]。
→ **D3 不可把 REGOMA 的「7.4 vs 5.6 個月、HR 0.50」單獨拿出來當希望。** 兩個試驗要並排寫，
  而且這正好是全專題最好用的一堂課：**一個漂亮的第二期，被第三期推翻了**。
→ 台灣端剛好對得起來：健保 regorafenib 第 9.51 條與食藥署仿單的適應症**都沒有膠質母細胞瘤**[D[S65]][D[S68]]。

**11. 「早期緩和照護對腦瘤有幫助」現在有第三期隨機試驗了，而它的主要終點是陰性的。**
EPCOG（六家德國大學醫學中心、GBM 病人 217 人隨機、介入 12 個月）：**六個月時的生活品質主要終點未達統計顯著**
（平均差 4.1，95%CI −4.4 到 12.6，P=.34）；作者另以「死亡時間校正」的事後分析才得到顯著（P=.041），
而那個校正之所以要做，是因為**兩組存活有顯著差異、而且是對照組比較長（P=.018）**[D[S42]]。
作者的結論句寫得很誠實：「EPCIC sustainably improves '**how to live**' but **not 'length of life**'」。
→ **D3 不可寫「早點介入緩和照護會活得比較久」。** 可寫的是：主要終點沒過、心情與緩和照護問題有改善、
  而**存活方向是相反的**（且該差異的解釋作者自己沒有給）。這一條比任何鼓勵句都更有說服力。

**12. 再手術的「好處」在方法學上被翻過一次，形狀跟 D1 的追蹤影像一模一樣。**
21 篇、8,630 人的統合分析：把再手術當**固定共變數**時 OS 有好處（HR 0.66，95%CI 0.61–0.71）；
把它當**時間相依共變數**時，好處不但消失，**方向還反過來（HR 2.19，95%CI 1.47–3.27）**[D[S38]]。
作者結論原文：「survival benefits of reoperation in recurrent GBM **may be overestimated when analyzed as fixed covariates**」。
2025 年 36 篇、10,738 人的更新統合分析也只敢寫「**The role of reoperation in rGBM remains uncertain**」[D[S41]]。
→ **D1 的 INTERVAL-GB（照得勤→活得久）與 D3 的再手術（開了刀→活得久），是同一個統計陷阱的兩個面貌。**
  兩篇可以互相指路，這是本組最好的一條內在線索。

**13. bevacizumab 治療放射性壞死的那個隨機試驗，收的不是 GBM。**
Levin 2011 是唯一一個安慰劑對照隨機試驗，**總共只有 14 人**，而且收案條件明寫是
「patients had undergone irradiation for **head-and-neck carcinoma, meningioma, or low- to mid-grade glioma**」[D[S37]]——
**高惡性度膠質瘤被排除在外。** 結果本身很漂亮（bevacizumab 組 5/5 有反應、安慰劑 0/7），作者也自稱 Class I evidence，
但**族群不是 GBM**。→ D1／D3 引用時**必須把族群寫出來**，不可寫成「GBM 的放射性壞死可以打 bevacizumab（有隨機試驗）」。

**14. D2 有一個引用地雷：那篇最好用的「病人與家屬評分落差」論文，2022 年版已被撤稿。**
Caramanna 等人 2022 年在 Quality of Life Research 的 patient–proxy agreement 論文**已於 2024 年撤稿**，
撤稿聲明寫明原因是「an **honest error** occurred while exporting data from the original EORTC dataset ... **significantly affecting
the results and conclusions**」[D[S55]]。**更正後的版本 2025 年重新發表**[D[S54]]。
→ **只能引 2025 年那一版**（EORTC 26101／26091，500 對病人—代理人配對）。它給出 D2 最重的一個數字：
  **復發高惡性度膠質瘤的病人裡，神經認知「完好」的只有 18.8%。**

---

## D1 `gb-followup`〈追蹤 MRI 怎麼排，變大不一定是惡化〉【紅線 8】

### 先讀站上那一篇（本節是硬性前置）

`/home/claude/repo/sit-pseudo.html`〈影像變壞，不一定是病變壞〉。本次逐字讀過，抄下它已經立的線：

| 站上原句（逐字） | D1 的處理 |
|---|---|
| 「試驗裡那個『四到八週』不是回診的間隔，是判讀病灶的規則，而且那段期間治療是持續的、監測也是持續的。它不是一段可以自己領走的緩衝。」 | **逐字沿用**，並補上 GBM 專屬的官方出處 EANO 2021[D[S5]] 與 RANO 2.0 的 12 週規則[D[S2]] |
| 「往好處想的機率是個位數，往壞處想至少一樣高」 | **不可搬用**（那是免疫治療的 6.0%）。改用同方向但正確族群的說法，見 Claim ceiling |
| 「假性進展只能回溯性地診斷，因為它在影像與臨床上都缺乏特異性」 | **同義沿用**；GBM 版的官方出處是 EANO 2021 的「Particular attention is needed when interpreting scans during this period; in case of doubt, rescanning after shorter intervals (4–8 weeks) is a pragmatic approach」[D[S5]] |
| 「把『沒有不舒服』當成證據，是這一題最常見的誤讀……那是回頭重新判讀之後在族群層次算出來的關聯，不是個人層次的判準」 | **逐字沿用邏輯**；它引的正是本 brief 的 [D[S3]]（Blakstad，p=0.029） |
| 「多做一個檢查不會把這個問題變簡單」 | 沿用，但 GBM 要改寫：**胺基酸 PET 確實比 FDG 好**（見下），所以不能照抄「更難分辨」；正確的限制是「準確度高 ≠ 改變結果」[D[S8]] |
| 「電腦斷層、磁振造影與正子造影在支付標準裡都是既有的診療項目……至於短期內重複照同一個部位有沒有頻次限制，我查不到對應的條文」 | **重新確認仍成立**（本次以 114.01.01 生效／114.03.13 更新之支付標準全表重新全文檢索，見台灣端）[D[S66]] |

**站上那篇引的 10 條連結今天仍有效**：10 篇期刊文獻的 DOI 於 2026-09-03 逐條以 Europe PMC REST 覆核，**10/10 命中且書目相符**（見 FAIL/驗證段落末尾的「連結重驗清單」）。第 10 條（健保支付標準全表）本次改以官方 TXT 全表重新下載成功。

### Key facts

#### A. 判讀標準的原文（RANO 2010 → RANO 2.0 2023）

- **RANO 2010（Wen et al., JCO 2010;28:1963–1972）**[D[S1]]，摘要原文可引：
  - 「chemoradiotherapy for newly diagnosed glioblastomas results in **transient increase in tumor enhancement (pseudoprogression) in 20% to 30% of patients**, which is difficult to differentiate from true tumor progression.」
    → **這是 RANO 之所以存在的理由，也是「20–30%」這個常被引用的數字的原始出處。族群標籤：新診斷 GBM、接受同步化放療。**
  - 「**Antiangiogenic agents produce high radiographic response rates, as defined by a rapid decrease in contrast enhancement on CT/MRI that occurs within days of initiation of treatment and that is partly a result of reduced vascular permeability to contrast agents rather than a true antitumor effect.**」
    → **這一句就是「假性反應」的定義原文，SPEC 要的就是它。關鍵字：within days（幾天內）、reduced vascular permeability（血管通透性下降）、not a true antitumor effect。**
  - 「In addition, **a subset of patients treated with antiangiogenic agents develop tumor recurrence characterized by an increase in the nonenhancing component depicted on T2-weighted/FLAIR sequences.**」
    → 假性反應的另一半：增強打掉了，**非增強的部分卻在長**。
- **RANO 2.0（Wen et al., JCO 2023;41(33):5187–5199）**[D[S2]]，摘要原文可引：
  - **基準線改了**：「In the newly diagnosed setting, **the postradiotherapy MRI, rather than the postsurgical MRI, will be used as the baseline for comparison with subsequent scans.**」
  - **12 週規則**：「Since the incidence of pseudoprogression is high in the **12 weeks after radiotherapy**, **continuation of treatment and confirmation of progression during this period with a repeat MRI, or histopathologic evidence of unequivocal recurrent tumor, are required to define tumor progression.** However, **confirmation scans are not mandatory after this period** nor for the evaluation of treatment for recurrent tumors. For treatments with a high likelihood of pseudoprogression, mandatory confirmation of progression with a repeat MRI is highly recommended.」
  - **非增強病灶**：「For IDH wild-type glioblastoma, **the nonenhancing disease will no longer be evaluated except when assessing response to antiangiogenic agents.**」
  - 主要量測仍是二維最大截面積，體積量測列為選項。
- **標準化影像協定**：Ellingson 2015 的 Brain Tumor Imaging Protocol（BTIP）定義了臨床試驗的最低序列組合（對比前後 3D T1、注射對比劑後的 2D T2、FLAIR、擴散加權）[D[S13]]。
  → 給病人的白話：**「同一台機器、同一套序列」不是龜毛，是判讀能不能成立的前提。**

#### B. 假性惡化——GBM 專屬的數字（每個都帶族群與分母）

- **Blakstad 2024（挪威東南區全人口世代，n=284，2015–2018 連續收案，全部接受放療且有追蹤 MRI）**[D[S3]]：
  - 放療後**三個月**（平均距放療結束 3.1 個月）重新判讀：**假性惡化 53 人（19.4%）、真惡化 113 人（41.4%）、穩定 104 人（38.1%）**，3 人無法評估。
  - 放療後**六個月**（平均 6.1 個月，242 人可評估）：**假性惡化 17 人（7.0%）**、真惡化 120 人（49.6%）、穩定 104 人（43.0%）。
    其中 8 人在三個月時也被判為假性惡化；**扣掉這 8 人，六個月的新發假性惡化只有 3.8%**。
  - **本 brief 的換算（必須標明是換算）**：三個月那一次，「片子看起來不是穩定」的共 166 人（53+113），
    **其中假性惡化 53 人＝31.9%，真惡化 113 人＝68.1%。**
    → **這就是 D1 要給讀者的分母。** 與 sit-pseudo 的「往好處想的機率並不比往壞處想高」方向一致，且不更寬鬆。
  - **與 MGMT 的關聯**：校正後分析中，**MGMT 啟動子甲基化**與假性惡化相關（三個月 p<0.001、六個月 p=0.045）。
  - **與症狀的關聯**：**沒有神經功能惡化**與假性惡化相關（三個月 p=0.029、六個月 p=0.034）。
    → **但這是族群層次的關聯，不是個人層次的判準**（sit-pseudo 已立此線，逐字沿用）。
  - **假性惡化組的形態**：53 人中 22 人（41.5%）只有 T1 增強變化、2 人（3.8%）只有 T2/FLAIR 上升、**29 人（54.7%）兩者都有**。
  - **關鍵的治療決策資料**：三個月時被即時懷疑、且回頭也確認是真惡化的病人中，只有 17 人（15.0%）改了抗腫瘤治療；
    **改治療者中位 OS 12.1 個月 vs 沒改者 11.8 個月，p=0.838（看不出差別）**。
    假性惡化組中只有 2 人（3.8%）因影像被改治療，**兩人都接受了第二次手術，病理只見反應性組織／壞死，沒有活性腫瘤**。
    → 作者結論原文：「we recommend **continuing adjuvant temozolomide courses in case of inconclusive MRI findings**」。
    → **這是 D1 全篇最有力的一段：不確定的時候把療程做完，在這份資料裡沒有讓人吃虧；而急著開刀確認的兩個人，開出來是壞死。**
  - 存活數字（**屬 B4，D1 若引用須一句指向 B4**）：三個月假性惡化組中位 OS 24.5 個月；六個月時假性惡化 31.8、真惡化 13.0、穩定 23.7 個月。
- **Brandes 2008（義大利波隆那，n=103，新診斷 GBM，第一次 MRI 在化放療結束後一個月）**[D[S4]]：
  - **第一次 MRI 顯示病灶變大者 50/103**；事後分類：**假性惡化 32 人、早期真惡化 18 人**。
  - **MGMT 分層（本題最強的數字）**：**甲基化組 21/23（91%）是假性惡化；未甲基化組 11/27（41%）**，p=0.0002。
  - MGMT 狀態（p=0.001）與偵測到假性惡化（p=0.045）都顯著影響存活。
  - **年代與方法標籤必寫**：2008 年、單中心、**RANO 之前**（用的是舊判讀）、第一次 MRI 距化放療結束僅一個月。
  - → **Brandes 的 64%（32/50）與 Blakstad 的 31.9%（53/166）不衝突，是不同時間點與不同分母**：
    離放療越近、越早那一張片子，假性惡化占的比重越高。這件事本身就是 D1 要教的東西。

#### C. 假性反應（bevacizumab）

- 定義原文見 [D[S1]]（上引三句）。
- RANO 2.0 的實作後果：GBM 平常不評估非增強病灶，**只有在評估抗血管新生藥的反應時才回頭看 T2/FLAIR**[D[S2]]。
- 臨床上的規模感（**反應率不是存活**，屬 D3 主場，D1 只需一句）：BRAIN 試驗中 bevacizumab 單用的
  客觀反應率 **28.2%**、bevacizumab+irinotecan **37.8%**[D[S40]]；而隨機試驗顯示加上 bevacizumab **不延長總存活**[D[S39]]。
  → **一個「片子變好了三成」與「活得沒有比較久」並存的例子。**

#### D. 放射性壞死與復發的鑑別——工具、準確度、限制

- **常規 MRI 本身就不夠**：van Dijken 2017 統合分析[D[S6]]，anatomical MRI（5 篇、166 人）**敏感度 68%（95%CI 51–81）、特異度 77%（45–93）**。
- **進階 MRI**（同一篇）[D[S6]]：
  - ADC（擴散，7 篇、204 人）：敏感度 71%（60–80）、特異度 87%（77–93）
  - **DSC 灌注（18 篇、708 人）：敏感度 87%（82–91）、特異度 86%（77–91）**
  - DCE 灌注（5 篇、207 人）：敏感度 92%（73–98）、特異度 85%（76–92）
  - **MR spectroscopy（9 篇、203 人）：敏感度 91%（79–97）、特異度 95%（65–99）**
  - 作者結論：進階技術準確度高於一般 MRI，**最高的是 spectroscopy**。
  - **誠實註記（必寫）**：spectroscopy 的特異度信賴區間下界只有 **65%**，且只有 9 篇 203 人——「95%」不是一個穩定的數字。
- **DSC 灌注的專篇統合分析（限 GBM）**：Wo 2025[D[S11]]，13 篇、487 個病灶（318 真復發、178 假性惡化），
  rCBV 合併**敏感度 87%（0.82–0.91）、特異度 83%（0.75–0.89）、AUC 0.92（0.89–0.94）**，異質性低（I²=18.9%）。
  高惡性度膠質瘤版（Gu 2024，21 篇、879 人、888 病灶）：rCBV 敏感度 86%、特異度 83%、AUC 0.91[D[S12]]。
- **胺基酸 PET**：de Zwart 2020 統合分析（39 篇、11 種示蹤劑，高惡性度膠質瘤）[D[S7]]：
  - **¹⁸F-FDG（12 篇、171 病灶）：敏感度 84%（72–92）、特異度 84%（69–93）**
  - **¹⁸F-FET（7 篇、172 病灶）：敏感度 90%（81–95）、特異度 85%（71–93）**
  - **¹¹C-MET（8 篇、151 病灶）：敏感度 93%（80–98）、特異度 82%（68–91）**
  - ¹⁸F-FDOPA：敏感度 85–100%、特異度 72–100%（研究數不足以合併）
  - 作者結論：**FET 與 MET 這兩個胺基酸示蹤劑敏感度高於 FDG，有得用就優先用胺基酸 PET。**
- **指引原文**：RANO/EANO 2025 年的更新（Lancet Oncol 2025;26(8):e436–e447）在摘要裡逐字寫著
  「This guideline further underscores the previously reported clinical value of PET imaging and the **superiority of amino acid PET
  over glucose PET**」[D[S8]]（初版是 2016 年，2025 版自述為其更新；同一份更新另有一篇 Neuro-Oncology 的開放取用導讀[D[S9]]）；
  同一段摘要並加上**本篇最重要的一句限制**：
  「**the scarcity of class 1 evidence showing that incorporating PET imaging into clinical workflows improves patient outcomes,
  highlighting priority areas for future clinical studies designed to address this gap**」[D[S8]]。
  → **準確度 90% 不等於做了會活得比較好。這句話是 D1 對抗「那我自費做個 PET」最誠實的回答。**
- **切片也不是萬靈丹**：EANO 2021 原文——「**Biopsy sampling is not always informative because viable tumour cells are regularly detected
  but their presence does not rule out pseudoprogression.**」[D[S5]]
  → 對照 Blakstad 那兩位被開刀確認、結果只見壞死的病人[D[S3]]：**兩個方向的錯都存在。**

#### E. 追蹤間隔的建議與其證據等級

- **EANO 2021 原文（唯一可引的指引措辭）**[D[S5]]：
  - 未經病理證實而採觀察策略者：「require **initial intervals of only 2–3 months** between scans」
  - 「In addition to clinical examination, **MRI is the standard diagnostic measure** for the evaluation of disease status or treatment
    response, using RANO criteria and **identical MRI protocols according to published recommendations**」
  - 「After the completion of therapy, **an initial interval between scans of 2–6 months is common practice for most patients depending
    on the disease histology**, but longer intervals might be appropriate in ca[ses] …」
    → **注意用詞是「common practice（慣例）」，不是建議等級。**
  - 「Conversely, in the event of suspected disease progression, **short-term control MRI within 4–8 weeks might be reasonable to
    confirm progression**.」
  - 「**Pseudoprogression (typically after chemoradiotherapy or immunotherapy) and pseudoresponse (for example, after anti-angiogenic
    therapy) are most likely to occur during the first 3 months of treatment but can also occur later.** Particular attention is needed
    when interpreting scans during this period; **in case of doubt, rescanning after shorter intervals (4–8 weeks) is a pragmatic
    approach.** **Perfusion MRI and amino acid PET might help to distinguish** pseudoprogression from true disease progression.」
- **實務端的兩套建議與遵從率**：INTERVAL-GB（Journal of Neuro-Oncology 2024;169(3):517–529，26 中心、754 人、10,100 人月追蹤）[D[S10]]：
  - **NICE**：術後 MRI <72 小時，此後每 3–6 個月一次；**EANO**：術後 <48 小時，此後每 3 個月一次。
  - 有做減積手術者，術後 72 小時內完成 MRI 者 **78.0%（407/522）**、48 小時內 **64.2%（335/522）**。
  - **後續追蹤 MRI 的中位次數只有 1 次（IQR 0–4）。**
  - 遵從率：NICE **52.8%（398/754）**、EANO **24.9%（188/754）**。
  - 多變項 Cox：處在建議追蹤區間內的時間越長，**OS 越長**（NICE HR 0.56，95%CI 0.46–0.66，p<0.001；EANO HR 0.54，0.45–0.63，p<0.001），
    **但 PFS 沒有差別**（HR 0.93，p=0.349／HR 0.99，p=0.874）。
  - 作者結論原文：「Regular surveillance follow-up for glioblastoma **is associated with** longer OS. **Prospective trials are needed to
    determine whether regular or symptom-directed MRI influences outcomes.**」

### 反方向的資料（誠實必列）

1. **「照得勤 → 活得久」這個關聯極可能是假的。** INTERVAL-GB 的 OS 有差、PFS 沒差[D[S10]]——
   如果追蹤真的靠早期發現而改善結果，PFS 應該先動；PFS 不動而 OS 動，最常見的解釋是**活得久的人才有機會累積更多「符合建議」的追蹤時間**
   （immortal time bias）。原作者自己只寫 "associated with"，並要求前瞻試驗。
2. **假性惡化的比例會隨著判讀時間點與判讀標準劇烈變動。** Brandes 2008 是 64%（第一次 MRI，化放療後一個月，RANO 之前）[D[S4]]；
   Blakstad 2024 是 31.9%（放療後三個月、RANO 判讀、以「非穩定」為分母）[D[S3]]；RANO 2010 引用的常見說法是 20–30%（以全體病人為分母）[D[S1]]。
   **三個數字互相不矛盾，但任何一個單獨拿出來都會誤導。**
3. **進階影像的統合分析都有明顯的方法學弱點。** 每一格的研究數少（spectroscopy 只有 9 篇 203 人）[D[S6]]，
   且各研究的參考標準不一致（有的病理、有的臨床追蹤）。統合分析的敏感度／特異度**不能當成個別醫院的表現保證**。
4. **PET 沒有第一級證據顯示改善病人結果**[D[S8]]。
5. **切片會給假的安心也會給假的警報**[D[S5]][D[S3]]。

### Claim ceiling（D1，紅線 8 的硬上限）

**可寫：**
- 「化放療後三個月那張片子，回頭重判會發現：**看起來變壞的人裡面，大約三分之一其實是假性惡化，三分之二是真的惡化**」
  （Blakstad，n=284，53/166 vs 113/166；**必須標明這是本 brief 由原文人數換算，原文報的是 19.4%／41.4%／38.1%**）[D[S3]]
- 「新診斷 GBM 接受同步化放療，**兩到三成**的人會出現暫時性的增強變強，這就是 RANO 判讀標準誕生的理由」[D[S1]]
- 「MGMT 甲基化的人，假性惡化的比例明顯較高（Brandes：甲基化 21/23 vs 未甲基化 11/27，p=0.0002）」[D[S4]]，
  以及「校正後分析中甲基化與假性惡化相關（p<0.001）」[D[S3]]
- 「假性惡化最常出現在治療開始後的頭三個月，但也可能更晚」[D[S5]]
- 「RANO 2.0 規定：**放療後十二週內**懷疑惡化，必須在**繼續治療**的前提下用重複 MRI 或病理證據來確認」[D[S2]]
- 「懷疑惡化時，四到八週後再照一次是合理的作法——**這是判讀規則，不是回診間隔，也不是你可以自己領走的等待期**」[D[S5]]＋沿用 sit-pseudo
- 「療程結束後每 2–6 個月照一次是**慣例**（EANO 原文用的是 common practice）」[D[S5]]；
  「NICE 的版本是每 3–6 個月、EANO 的版本是每 3 個月；在英國愛爾蘭 26 個中心的實際資料裡，**遵從率只有 52.8% 與 24.9%**」[D[S10]]
- 「灌注影像與 MR spectroscopy 的準確度高於一般 MRI（DSC 敏感度 87%／特異度 86%；spectroscopy 91%／95%），
  **但 spectroscopy 特異度的信賴區間下界只有 65%**」[D[S6]]
- 「胺基酸 PET（FET、MET）的敏感度高於 FDG（90%、93% vs 84%）」[D[S7]]；
  「**但目前沒有第一級證據顯示把 PET 放進流程能改善病人的結果**——這是 RANO/EANO 2025 年更新自己寫的」[D[S8]]
- 「切片查到活的腫瘤細胞，**不能排除**假性惡化」[D[S5]]
- 「在挪威那份資料裡，**影像不確定時把 temozolomide 療程做完，並沒有讓存活變差**；而三個月時被判真惡化的人，改治療與不改治療的中位存活是 12.1 對 11.8 個月，看不出差別」[D[S3]]
- 「RANO 2.0 之後，用來比較的基準線是**放療後**那張 MRI，不是術後那張」[D[S2]]
- 「bevacizumab 會在**幾天內**讓增強變淡，這一部分是血管通透性下降造成的，不是真的抗腫瘤效果」[D[S1]]

**不可寫（超線）：**
- ❌ **「往好處想的機率是個位數」**——那是 sit-pseudo 的免疫治療數字（6.0%），族群不對，搬過來是引用錯誤。
- ❌ 「變大多半沒事」「大部分是假性惡化」——即使 Brandes 的 64% 也不能這樣寫（單中心、2008、RANO 之前、第一次 MRI）。
  **凡引用 Brandes 的 32/50，同一段必須寫出 18/50 是早期真惡化，並帶上年代與方法標籤。**
- ❌ 任何讓「再等一等」讀起來像是**病人可以自己決定**的句子。四到八週／十二週都是**在治療持續、監測持續、醫師判定臨床穩定**之下的安排。
- ❌ 「沒有症狀就是假性惡化」——[D[S3]] 的 p=0.029 是族群層次關聯，sit-pseudo 已立此線。
- ❌ 「照得越勤活得越久」——INTERVAL-GB 是觀察性、PFS 沒差、作者自己說要前瞻試驗[D[S10]]。
- ❌ 「做個 PET 就能分辨」——準確度 ≠ 改變結果[D[S8]]；也不可反過來抄 sit-pseudo 的「更難分辨」（那是 FDG 在免疫治療下的情形，GBM 的胺基酸 PET 不適用）。
- ❌ 「切片就能確定」[D[S5]]。
- ❌ 任何存活月數當結論——屬 B4，要用一句指向〈那個數字，我要怎麼跟你講〉。
- ❌ 給讀者一個可以自己對照的「追蹤時程表」口吻。EANO 自己用的詞是 common practice。

### Caveats／safety notes（寫作者必寫）

1. **本篇的主警語（放在第一個 h4 之前或第一段）**：這一題的原理就是回頭看才成立的。任何一段都不可以被讀成「所以我可以再等等」。
   **不要更動回診日期。**
2. **急症出口（每篇都要有，指向 C4）**：新出現的劇烈頭痛、清晨頭痛合併噴射性嘔吐、意識改變、單側無力、瞳孔不等大、癲癇發作——
   **這些不必等到原訂那一天**，見〈哪些狀況要當天回來〉。
3. **這一篇不寫存活數字當結論**；需要時一句指向 B4。
4. **不點名機構、不寫本院的判讀流程或設備**；台灣的假性惡化判讀官方文件本次同樣查不到（見台灣端）。
5. **胺基酸 PET 在台灣的可及性未查證**——不可寫「台灣有／沒有」，只能寫「有沒有、要不要自費，問你的團隊與醫務課」。
6. 引用任何統合分析的敏感度／特異度時，**同段必須帶研究數與人數**。

### 台灣端（D1）

| 項目 | 結果 | 路徑 |
|---|---|---|
| MRI／CT／PET 是否為既有支付項目 | **查到**：支付標準全表中有「磁振造影－無造影劑」（代碼 33084B，6,500 點）等既有診療項目[D[S66]] | 健保署支付標準全表 TXT（114.01.01 生效、114.03.13 更新）直接下載後全文檢索，2026-09-03 |
| 短期內重複照同一部位的頻次限制條文 | **gap**——與 sit-pseudo 的結論一致，本次仍未檢出可引用條文 | 同上 |
| 台灣官方的假性惡化判讀流程文件 | **gap** | 未檢出 |
| 「電場」在支付標準全表 | **零筆**（重新確認，見全專題台灣端總掃第 8 項）[D[S66]] | 同上 |

**文章寫法**：沿用 sit-pseudo 的措辭——「實際申報方式請向個管師或醫務課確認」；**不推論有無給付**。

### 給繪圖組的數字（D1，`fig-gb-mri`）

- 時間軸節點：手術 → **術後 48／72 小時 MRI**（EANO／NICE 兩套建議）[D[S10]] → 六週同步化放療 →
  **放療後 MRI＝RANO 2.0 的基準線**[D[S2]] → **放療後 12 週為假性惡化高風險窗**[D[S2]] →
  療程結束後**每 2–6 個月**（EANO 稱 common practice）[D[S5]]。
- 假性惡化窗：**放療後 3 個月 19.4%、6 個月 7.0%（新發 3.8%）**[D[S3]]；EANO：**頭三個月最可能，但也可能更晚**[D[S5]]。
- **圖上最重要的一格（取代「往好處想的機率是個位數」）**：
  三個月那張片子，284 人中 **假性惡化 53／真惡化 113／穩定 104**；
  → 「看起來變壞的 166 人裡，**53 人（約三分之一）是假性惡化，113 人（約三分之二）是真的惡化**」[D[S3]]（標明為換算值）。
- 懷疑惡化時的確認窗：**4–8 週**[D[S5]]；RANO 2.0 的十二週內強制確認[D[S2]]。
- 工具準確度小方塊（可做橫條）：一般 MRI 68/77；DSC 87/86；DCE 92/85；MRS 91/95[D[S6]]；FDG-PET 84/84、FET 90/85、MET 93/82[D[S7]]。
  **每一條旁邊要有研究數與人數，圖說要有一句「準確度高不等於做了會活得比較好」[D[S8]]。**


---

## D2 `gb-cognition`〈記憶、專注與人格改變〉

### 這一篇的骨架（SPEC 指定，本節逐項給來源）

SPEC 要求把**腫瘤本身 vs 放療 vs 藥物 vs 癲癇 vs 類固醇**的相對貢獻分開講。
查證結果是：**這五者裡，只有「腫瘤本身 vs 放療」有可以拿來分開的對照資料**（Klein 2002／Douw 2009），
**抗癲癇藥有一份校正後的橫斷面資料（結論是「沒有獨立相關」）**，
**類固醇對認知的直接證據在腦瘤族群裡我查不到可引用的原始研究**。
→ **這一節不能寫成五等分的圓餅圖。** 正確的寫法是：兩件事有資料、一件事有反面資料、兩件事沒有資料。

### Key facts

#### A. 診斷時就已經有——比大多數人以為的高很多

- **Tucha 2000（額葉或顳葉腦瘤，n=139，治療前、剛診斷完就測）**[D[S20]]：
  以「低於第 10 百分位＝受損」判定，**超過 90% 的病人至少一個認知面向受損**；
  **執行功能受損 78%**、**記憶與注意力受損超過 60%**。
  **本篇最重要的一句在方法段之外**：「Analysis of the correlation between the patients' **own reports** and the
  neuropsychological assessment results revealed **only a weak relationship**.」
  → **病人自己講的「還好」，跟測出來的結果只有很弱的相關。** 這一句就是 D2「家屬看到的與病人自覺的落差」那一節的地基。
  同一篇也寫「**No effects of anticonvulsant drugs on cognition were observed**」——抗癲癇藥在這份資料裡看不出影響。
- **Sekely 2023（新診斷 GBM，n=45，診斷後中位 4 週、化放療之前測）**[D[S21]]：
  **76%（34/45）有神經認知損害**；分項：**記憶保留 53%、執行功能 51%、立即回想 42%、語詞流暢 41%、注意力 24%**。
  同時：**睡眠障礙 70%、疲倦 57%、神經行為症狀 27%、憂鬱症狀 16%**。
  多變項回歸顯示**憂鬱症狀與認知損害顯著相關**。
  → **這是「還沒開始治療就已經這樣」最乾淨的 GBM 專屬數字（n 小，要標）。**
- **Moiyadi 2023（印度單中心、內生性腦瘤連續收案 n=142，術前測五個面向）**[D[S22]]：
  **嚴重認知缺損 90%**，其中 **70% 至少兩個面向受影響**；最常受影響的是注意力—執行功能、記憶、視動速度。
  多變項：**年齡較大、教育程度較低、腫瘤體積較大**與較差的認知相關；
  **只有語言障礙與位置有關（顳葉），而且與左右側無關**。
- **與「能不能自理」直接掛勾**：Noll 2018（新診斷顳葉膠質瘤 n=103，其中左側 73 人 49% 是 GBM、右側 30 人 57% 是 GBM）[D[S71]]：
  語文學習、執行功能、語言理解三項測驗**共同解釋了臨床醫師評定的功能獨立性（FIM）40% 的變異**。
  → 可以用來反駁「認知測驗只是紙上作業」。

#### B. 放療的貢獻——最乾淨的對照資料在低惡性度膠質瘤，不在 GBM

- **Klein 2002（Lancet，n=195 低惡性度膠質瘤，其中 104 人在 1–22 年前接受過放療；對照組是 100 位低惡性度血液疾病病人與 195 位健康人）**[D[S23]]：
  - 膠質瘤病人在**所有**認知面向都比血液疾病對照差，比健康對照更差。
  - 用過放療與較差的認知功能相關；**但記憶面向的認知失能只出現在「單次分次劑量超過 2 Gy」的人身上。**
  - **抗癲癇藥的使用與注意力及執行功能的失能有強烈相關。**
  - 作者結論原文：「**the tumour itself has the most deleterious effect on cognitive function**, and that radiotherapy mainly results
    in additional long-term cognitive disability **when high fraction doses are used**」。
  → **這是 D2 骨架第一句的官方出處：貢獻最大的是腫瘤本身。**
- **Douw 2009（Lancet Neurology，同一個世代追到平均 12 年，n=65 完成第二次評估，其中 32 人（49%）曾接受放療，只有 3 人分次劑量 >2 Gy）**[D[S24]]：
  - 接受過放療者在第二次評估時**注意力**較差（−1.6 vs −0.1，p=0.003）、**執行功能**（p=0.03）與**訊息處理速度**（p=0.05）也較差。
  - **17/32（53%）接受過放療者出現認知失能，未接受放療者 4/15（27%）。**
  - 作者結論：未放療的長期存活者影像與認知**穩定**；接受放療者出現**進行性的注意力退化，即使分次劑量在被認為安全的範圍內**。
  - **族群標籤必寫：低惡性度膠質瘤、長期存活者、平均 12 年、n 很小（65 人）。這不是 GBM 的資料。**
- **GBM 自己的長期存活者資料（2026 年新出）**：EORTC 1419 ETERNITY[D[S52]]，
  存活 ≥5 年的 grade 4 病人（GBM IDH-wildtype 與 astrocytoma IDH-mutant），**基線平均在診斷後 9 年（範圍 5–21 年）**：
  **185 人中 145 人（78%）至少一項測驗受損**；各項受損率介於 **17.4%（HVLT-R 延遲再認）到 58.7%（TMT B）**；
  **縱貫來看認知大致穩定**，只有延遲記憶有小幅下降；左側與顳葉腫瘤與較差的認知相關。
  → **這一段可以同時回答兩個問題：長期存活者多數有認知損害，但它不是一路往下掉。**
- **放射性腦白質病變（late）**：Terziev 2021（高惡性度膠質瘤長期存活者 n=81，18 位 grade 4／63 位 grade 3，
  無惡化存活 >30 個月，放療後中位追蹤 79 個月）[D[S51]]：
  **54.3%（44/81）出現放射性腦白質病變**；其中 29 人有相應症狀（**皮質下失智 28 人、步態障礙 12 人、尿失禁 9 人**）。
  **累積發生率：12 個月 21%、36 個月 42%、60 個月 48%。** 危險因子：**年齡 >60 歲、吸菸**、與一個基因多型性。
  → **這是 D2 唯一一份「時間軸上的量化風險」，也是給繪圖組的主要數字。族群標籤：長期存活者、多數是 grade 3。**

#### C. 藥物、癲癇與類固醇——這三格裡有兩格是空的

- **抗癲癇藥**：van der Meer 2021（多中心橫斷面、膠質瘤病人 n=272）[D[S56]]：
  未用藥者憂鬱盛行率 10%、用藥者 21%（未校正 OR 2.29，95%CI 1.05–4.97，p=0.037），
  **但校正混淆因子後不再顯著（校正 OR 1.94，95%CI 0.83–4.50，p=0.125）**；
  焦慮（校正 OR 1.17，p=0.659）與**主觀認知障礙（校正 OR 0.83，95%CI 0.34–2.04，p=0.684）**都沒有差別。
  作者結論：「AED use was **not independently associated** with concurrent depression, anxiety, or subjective cognitive impairment」。
  → **與 Klein 2002 的「抗癲癇藥與注意力／執行功能失能強烈相關」方向相反。兩個都要寫。**
    差異可能來自：Klein 用的是**客觀神經心理測驗**、2002 年的舊藥；van der Meer 用的是**自填問卷**、2021 年的用藥組合。
    **這個不一致本身就是內容**——「藥有沒有影響」目前沒有一致的答案。
- **癲癇發作本身**：本次未檢出可引用的「發作對 GBM 病人認知的獨立貢獻」原始研究。**gap。**
- **類固醇**：本次以 Europe PMC 檢索 corticosteroid／dexamethasone × cognitive，**檢出的全部是非腦瘤族群
  （氣喘、心臟手術、早產兒、動物模型）**；**在膠質瘤族群裡沒有檢出可引用的原始研究。gap。**
  → **D2 只能寫「臨床上常見的抱怨（失眠、情緒起伏、坐立難安）在 C2 有完整處理」，並一句指向 C2；
    不可寫成「類固醇會讓你記性變差，這有研究」。**
- EANO 2021 的官方立場只寫到這裡：建議用標準化測驗組合做神經認知評估，MMSE／MoCA 是篩檢工具、有其限制[D[S5]]。

#### D. 海馬迴保護——證據在腦轉移，不在 GBM

- **NRG Oncology CC001（Brown 2020，JCO 2020;38(10):1019–1029，n=518 腦轉移病人）**[D[S25]]：
  海馬迴保護全腦放療＋memantine vs 全腦放療＋memantine。
  - **主要終點「認知功能失敗的時間」顯著較佳：校正後 HR 0.74（95%CI 0.58–0.95），P=.02。**
  - 差異來自 **4 個月時的執行功能（23.3% vs 40.4%，P=.01）**與 **6 個月時的學習與記憶（11.5% vs 24.7%，P=.049；16.4% vs 33.3%，P=.02）**。
  - **總存活、顱內無惡化存活、毒性三組都沒有差別。**
  - 作者結論限定得很死：「should be considered a standard of care for patients with **good performance status** who plan to receive
    **WBRT for brain metastases** with **no metastases in the HA region**」。
- **在 GBM 適不適用——誠實的答案是「沒有隨機試驗，只有劑量學可行性研究」**：
  Thippu Jayaprakash 2017（Clin Oncol 2017;29(11):748–752）是一份**回溯性計畫研究**，
  目的是量化 GBM 接受根治性化放療時海馬迴實際吃到多少劑量、與已知會造成認知損害的劑量比較、
  並評估用螺旋斷層治療能不能有臨床意義的減量[D[S50]]。
  **這是可行性層級的證據（retrospective planning study），不是療效試驗。**
  **本篇摘要在 Europe PMC 只有目的段，沒有數字**——所以 **brief 不提供任何海馬迴劑量數字，寫作者也不得自行補**。
- **為什麼 GBM 難做**：SPEC 的假設（腫瘤常在附近、劑量分布限制）本次**沒有找到可引用的量化來源**。
  → **只能寫成「這件事在腦轉移證明過，在膠質母細胞瘤沒有；原因請問你的放腫科醫師」，不可自己補理由。**
- **memantine（RTOG 0614，Brown 2013，Neuro-Oncology 2013;15(10):1429–1437，n=554 收案／508 可評估，腦轉移病人）**[D[S26]]：
  - **主要終點（24 週延遲回想）沒有達到統計顯著（P=.059）**，作者自己說可能是因為 24 週只剩 149 人可分析、**檢定力只有 35%**。
  - **次要終點：認知退化的時間顯著較長（HR 0.78，95%CI 0.62–0.99，P=.01）**；
    24 週時認知功能失敗的機率 **memantine 53.8% vs 安慰劑 64.9%**。
  - 執行功能（8 週 P=.008、16 週 P=.0041）、處理速度（24 週 P=.0137）、延遲再認（24 週 P=.0149）較佳。
  - **毒性與安慰劑相當。**
  → **正確措辭：主要終點沒過（而且作者說是檢定力不夠），次要終點方向一致。族群是腦轉移的全腦放療，不是 GBM。**

#### E. 認知復健與職能治療——有隨機試驗，效果是「延後才出現」

- **Gehring 2009（JCO 2009;27(22):3712–3722，隨機對照，荷蘭 11 家醫院，n=140）**[D[S48]]：
  族群是**低惡性度與退行性膠質瘤、預後因子良好、而且同時有主觀認知抱怨與客觀認知缺損**的病人；
  介入是電腦化注意力再訓練＋注意力／記憶／執行功能的代償策略訓練。
  - **療程剛結束時：只有「主觀認知功能」與「主觀負擔」顯著改善，客觀神經心理測驗與其他自填量表都沒有。**
  - **六個月追蹤時：介入組在注意力與語文記憶的客觀測驗上顯著較好，並且心理疲倦較少。**
  - 作者結論：短期改善主觀抱怨，長期改善客觀表現與心理疲倦；**還需要研究釐清哪個成分有效。**
  → **族群標籤必寫：不是 GBM，是預後好的低惡性度／退行性膠質瘤，而且是「已經有抱怨也測得出缺損」的人。**
- **Tariq 2025 系統性回顧（15 篇）**[D[S49]]：
  神經心理師指導的訓練對記憶、注意力、執行功能有效，**年輕、教育程度較高者獲益最大**；
  **整體性記憶術訓練與神經回饋沒有顯示對整體認知有效**；有氧運動改善執行功能；瑜伽與合併有氧＋肌力訓練改善整體認知；
  主動式電玩可能改善動作與流程技巧，**對認知功能沒有效果**。
  作者結論原文：「Given the **limited trials and methodological variations**, **a standardized CR program cannot be established at present**.」
  → **D2 可以寫「有東西可以做」，但不可以寫成一套療程。**
- EANO 2021 的一句官方立場可以直接引：「**The need for occupational, speech and physical therapy as well as for counselling for
  social support should be assessed**」[D[S5]]。→ **「要被評估」是指引寫的；「一定會改善」不是。**

#### F. 人格與行為改變、以及「他覺得沒事」這件事

- **落差的主證據是 Tucha 2000 的那一句**（自述與測驗結果只有弱相關）[D[S20]]。
- **代理人評分與病人自評的一致性——只能引 2025 年的更正版**[D[S54]]（2022 年版已撤稿[D[S55]]）：
  EORTC 26101／26091 的 **500 對病人—代理人配對**，復發高惡性度膠質瘤：
  - **全體的一致性（Lin's CCC）介於 0.399–0.743**；
  - **認知受損者 0.231–0.811、認知完好者 0.376–0.732**；
  - **最重的一個數字：全體 500 人裡，神經認知「完好」的只有 18.8%。**
  - 作者結論：整體的中等一致性**足以在研究裡採用代理人報告**，但**做臨床決定時必須把病人的神經認知狀態與心智能力納入考量**。
- **代理人評的情緒準不準——另一份系統性回顧說要小心**[D[S67]]（Sannes 2023，6 篇）：
  結果分歧；**憂鬱的代理人評分比焦慮準**；作者明寫「proxy ratings of depression and anxiety **should be interpreted with caution**」，
  並指出樣本小、代理人定義不一。
- **長期存活者的家庭視角**[D[S53]]（Spoor 2024，n=21 存活 ≥5 年的高惡性度膠質瘤、15 位照顧者，
  平均存活 grade III 12 年、grade IV 8 年）：
  **認知顯著受損但個別差異很大**；病人整體生活品質沒有受損、但**所有功能量表都偏離常模**；
  **多數生活品質次量表上病人與代理人一致**；**三分之一的照顧者回報高度照顧負荷或高度負擔**；
  **照顧者負擔與病人的認知缺損沒有相關。**
  → **這一句很反直覺，要寫：照顧者累不累，跟病人認知壞到什麼程度沒有對應關係。**
- **關於「anosognosia（病覺缺失）」這個詞**：本次以 Europe PMC 檢索
  anosognosia／unawareness／impaired awareness × glioma／brain tumour，
  **沒有檢出以成人膠質瘤為族群的原始研究**；唯一相關的自評—他評一致性研究（FrSBe）族群是**兒童腦瘤的成年存活者**[D[S72]]，
  結果是各次量表一致性弱到中等（ICC：冷漠 .583、去抑制 .420、執行功能失調 .373），**只有去抑制那一項與評分者角色有關**。
  → **D2 不可使用「anosognosia」這個診斷名詞來描述 GBM 病人**，也不可引兒童腦瘤存活者的數字當成人資料。
    可寫的是 Tucha 的「自述與測驗只有弱相關」＋ Caramanna 的一致性係數，**用白話寫「落差」，不掛病名**。
- **額葉病灶的表現**：本次未檢出以成人膠質瘤為族群、可引用的量化研究。ETERNITY 反而報告
  **額葉腫瘤與較高的心理動作速度與認知彈性相關**（方向與直覺相反）[D[S52]]。
  → **不可寫「長在額葉就會人格改變」。** 可寫的是 ETERNITY 的位置關聯（左側／顳葉較差），並註明是長期存活者世代。

#### G. 照顧者負荷的實證

- **Chen 2025 系統性回顧與統合分析（15 篇、974 位腦瘤病人的家庭照顧者，文獻搜尋到 2022 年 2 月）**[D[S57]]：
  **憂鬱合併盛行率 37.15%（95%CI 22.00–52.30）**；
  **焦慮 49.47%（95%CI 35.81–63.12）**；
  **64%（95%CI 54–74）回報 distress／負擔。**
  → **信賴區間都很寬（憂鬱從 22% 到 52%），引用時必須把區間一起寫。**
- **EPCOG 的照顧者結果是陰性的**[D[S42]]：介入組**照顧者並未獲益**（"caregivers did not seem to benefit"）。
  → **誠實必列：目前最大的那個隨機試驗，沒有讓照顧者比較輕鬆。**

#### H. 最後一節的素材——「文件要比別的癌別早談」

**這一節指向站上 `sit-decide-for`〈他不能決定的時候，誰決定〉與 `sit-documents`〈三份文件，不是同一件事〉，
法律內容一律不重寫。D2 只提供「為什麼腦瘤要更早」的數字。**

1. **確診後不久，決定能力就已經受影響**：Triebel 2009（Neurology 2009;73(24):2086–2092，惡性膠質瘤 26 人 vs 健康對照 22 人，
   標準化醫療決定能力量表 CCTI）[D[S27]]：
   病人在「理解」與「推理」兩個同意標準上顯著低於對照，「賞識」呈趨勢；
   **相對於對照組，超過 50% 的惡性膠質瘤病人出現能力受損（marginally capable 或 incapable）。**
   作者結論原文：「**Soon after diagnosis**, patients with malignant glioma have impaired capacity to make treatment decisions」；
   受損主要與**短期語文記憶**缺損有關；並建議**持續評估**決定能力。
2. **體能狀態看起來很好，不代表決定能力沒問題**：Martin 2015（惡性腦瘤 71 人，26 人原發、45 人轉移）[D[S28]]：
   **KPS 90–100 的人，在所有 CCTI 標準上都被判定「有能力」的只有 46%**；KPS 70–80 是 23%；**KPS 50–60 是 0%**。
   作者結論：**只有極輕度失能的腦瘤病人，仍有相當比例在標準化測量上出現決定能力損害。**
   → **這一句是本節最關鍵的一句：「他看起來好好的」不是證據。**
3. **到了復發，認知完好的只剩不到兩成**：Caramanna 2025，n=500，**18.8%**[D[S54]]。
4. **結果就是文件寫不成、也不是病人自己寫的**：
   - **韓國單中心＋國民健康保險資料庫串接（2018–2022，安寧照會病人）**[D[S29]]：
     惡性膠質瘤 **229 人** vs 五大實體癌（肺、大腸直腸、胃、肝、胰膽）**4,283 人**：
     **預立醫療照護諮商（ACP）文件記載率 20.1% vs 58.0%（校正 OR 0.13，95%CI 0.09–0.19）**；
     **維生醫療決定被記載為「由病人本人決定」者只有 21.4%，實體癌是 67.1%（校正 OR 0.07，95%CI 0.04–0.12）**；
     急診次數較少（29.3% vs 48.7%）、化療較少（29.7% vs 42.0%），**但安寧使用率較低（62.0% vs 73.1%，校正 OR 0.57）**，
     **死在護理之家的比例較高（20.5% vs 6.8%）**。
   - **另一份韓國單中心世代（GBM 205 人，2017–2022，159 人死亡，中位 OS 20.3 個月）**[D[S58]]：
     **有預立醫療指示者 11 人（6.9%）**、有維生醫療計畫者 63 人（39.6%）、**兩者皆無 85 人（53.5%）**；
     63 位有計畫者中，**由本人完成的只有 10 人（15.9%），由家屬決定的 53 人（84.1%）**；
     **接受安寧照會者 102 人（64.2%，中位從首次照會到死亡 44 天）**；侵略性末期照護 78 人（49.1%），
     **接受過安寧照會者較少接受侵略性末期照護。**
     作者結論原文：「The right to self-determination remains poorly protected among patients with glioblastoma,
     with **nearly 90% not self-completing AD or LST plan**.」
   - **系統性回顧的一般性結論**：Sizoo 2014（17 篇）[D[S45]]：「**Cognitive deficits increase as the disease progresses,
     hampering communication and decision making.**」
   - **跨國比較**：Koekkoek 2014（荷 83／奧 72／英 52 位已故高惡性度膠質瘤病人的家屬問卷）[D[S46]]：
     **預立指示的比例：荷蘭 46%、英國 36%、奧地利 6%（p<0.001）**；死亡前三個月有 75% 在家；
     **只有 53% 的病人被認為得到良好的照護品質。**
5. **指引自己承認這一塊還沒有建議**：EANO 2021 原文——「**Firm recommendations on when and how to involve family members and
   caregivers and how to assess the medical decision-making capacity in patients with brain tumours remain to be developed**」[D[S5]]。
   → **這句話對這一節極有用：不是「醫界已經有一套流程你沒照做」，是「這一塊連指引都說還沒訂好」，所以更要自己早一點談。**

### 反方向的資料（誠實必列）

1. **認知損害不等於生活品質差。** Spoor 2024：長期存活者「認知顯著受損」但整體生活品質未受損[D[S53]]；
   ETERNITY：78% 受損，但**縱貫看是穩定的**[D[S52]]。
2. **抗癲癇藥的證據互相矛盾**（Klein 2002 有關聯 vs van der Meer 2021 校正後無關聯）[D[S23]][D[S56]]；
   Tucha 2000 在治療前也沒有看到抗癲癇藥的影響[D[S20]]。
3. **memantine 與海馬迴保護的主要終點各有問題**：memantine 主要終點沒過（P=.059，檢定力 35%）[D[S26]]；
   CC001 主要終點過了但**族群是腦轉移**，且 OS 與顱內 PFS 都沒有差別[D[S25]]。
4. **認知復健沒有標準療程**，而且效果在療程剛結束時**只出現在主觀指標**[D[S48]][D[S49]]。
5. **照顧者的介入試驗是陰性的**[D[S42]]；**照顧者負擔與病人認知缺損沒有相關**[D[S53]]。
6. **代理人評分要小心**[D[S67]]；而且它最好用的那份資料曾經因資料匯出錯誤而撤稿[D[S55]]。

### Claim ceiling（D2）

**可寫：**
- 「還沒開始治療，就已經有 76% 的新診斷 GBM 病人在測驗上有認知損害（n=45）」[D[S21]]；
  「額葉或顳葉腦瘤的病人，診斷當下超過九成至少一個面向受損，執行功能 78%」[D[S20]]
- 「**病人自己講的狀況，跟測出來的結果只有很弱的相關**」[D[S20]]
- 「貢獻最大的是腫瘤本身；放療主要是在**單次分次劑量超過 2 Gy** 的情況下再加上長期的認知失能」[D[S23]]
  ——**必須標明族群是低惡性度膠質瘤**
- 「追到平均 12 年，接受過放療的低惡性度膠質瘤存活者注意力持續退化，即使分次劑量在被認為安全的範圍內；
  53% 出現認知失能，未放療者 27%（n=65）」[D[S24]]
- 「存活五年以上的 grade 4 病人，78% 至少一項測驗受損，但整體看是**穩定**的（n=185，平均診斷後 9 年）」[D[S52]]
- 「高惡性度膠質瘤長期存活者中，54.3% 出現放射性腦白質病變；累積發生率 12 個月 21%、36 個月 42%、60 個月 48%（n=81）」[D[S51]]
- 「抗癲癇藥與憂鬱／焦慮／主觀認知障礙**校正後沒有獨立相關**（n=272）」[D[S56]]，
  **並列**「2002 年那份用客觀測驗的研究則看到抗癲癇藥與注意力及執行功能失能有強烈相關」[D[S23]]
- 「海馬迴保護＋memantine 讓認知功能失敗的風險下降（HR 0.74，P=.02），**但那是腦轉移病人的全腦放療試驗**，
  而且**存活沒有差別**」[D[S25]]；「在膠質母細胞瘤，這件事只有劑量學可行性研究，**沒有隨機試驗**」[D[S50]]
- 「memantine 的主要終點沒有達到統計顯著（P=.059，作者說檢定力只有 35%），次要終點方向一致」[D[S26]]
- 「認知復健有一個隨機試驗：療程剛結束時只有主觀指標改善，**六個月後客觀測驗才出現差別**（n=140，族群不是 GBM）」[D[S48]]；
  「系統性回顧的結論是**目前無法訂出標準療程**」[D[S49]]
- 「指引寫的是**職能、語言與物理治療的需求應被評估**」[D[S5]]
- 「腦瘤家屬的憂鬱合併盛行率 37%（22–52%）、焦慮 49%（36–63%）、64% 回報負擔（15 篇、974 人）」[D[S57]]
- 「確診後不久，超過一半的惡性膠質瘤病人在標準化量表上已經出現決定能力受損（n=26）」[D[S27]]
- 「KPS 90–100 的腦瘤病人，各項標準都判定有能力的只有 46%」[D[S28]]
- 「到了復發，神經認知完好的只剩 18.8%（n=500）」[D[S54]]
- 「韓國的資料：惡性膠質瘤病人的預立醫療照護諮商記載率 20.1%，五大實體癌是 58.0%；
  維生醫療決定是本人做的只有 21.4%，實體癌是 67.1%」[D[S29]]
- 「另一份韓國 GBM 世代：近九成沒有自己完成預立醫療指示或維生醫療計畫」[D[S58]]
- 「連指引都寫著：什麼時候、怎麼讓家屬參與、怎麼評估決定能力，**還沒有明確的建議**」[D[S5]]

**不可寫（超線）：**
- ❌ **把腫瘤／放療／藥物／癲癇／類固醇畫成一張比例圖。** 只有前兩者有對照資料。
- ❌ 「類固醇會影響記憶／注意力，研究這樣說」——**膠質瘤族群沒有可引用的原始研究，這是 gap。**
- ❌ 「癲癇發作會讓認知變差」當成有證據的因果句——**未檢出可引用來源。**
- ❌ 把 Klein 2002／Douw 2009 的數字寫成 GBM 的數字。**那是低惡性度膠質瘤。**
- ❌ 把 CC001 或 RTOG 0614 寫成「GBM 放療可以保護海馬迴／可以吃 memantine」。**族群是腦轉移的全腦放療。**
- ❌ 給任何海馬迴劑量數字。**本 brief 沒有取得可引用的數值。**
- ❌ 使用「anosognosia／病覺缺失」這個診斷名詞描述 GBM 病人；也不可引兒童腦瘤存活者的自評—他評數字[D[S72]]。
- ❌ 「長在額葉就會人格改變」——未檢出可引用的量化來源，而且 ETERNITY 的方向相反[D[S52]]。
- ❌ 「認知復健可以改善 GBM 病人的認知」——Gehring 的族群不是 GBM，而且系統性回顧說訂不出標準療程[D[S48]][D[S49]]。
- ❌ 「早點簽文件可以活得比較久／過得比較好」——**EPCOG 的主要終點是陰性的**[D[S42]]。
  這一節能說的是「**能不能由他自己決定**」，不是「會不會比較好」。
- ❌ 任何存活數字當結論——屬 B4。
- ❌ 重寫 `sit-decide-for` 與 `sit-documents` 的法律內容。**只指路。**

### Caveats／safety notes（寫作者必寫）

1. **這一篇最容易被讀成「他變了個人，是不是不愛我們了」。** 開頭要把「這是病灶與治療造成的」講清楚，
   而且要寫「病人自己常常感覺不到」——用 Tucha 的弱相關[D[S20]]，不用病名。
2. **不可自行調整任何藥物**（抗癲癇藥、類固醇）。類固醇的減量規則在 C2，一句指路。
3. **急症出口**（指向 C4）：**突然的意識改變、新出現的混亂、講不出話、單側無力**——
   這些不是「認知副作用」，**要當天回來**。這一句一定要在人格改變那一節裡出現，
   否則「他最近怪怪的」會被家屬當成慢性變化而延誤。
4. **每一個數字都要帶族群標籤**：低惡性度膠質瘤／腦轉移／長期存活者／兒童腦瘤存活者，是四種不同的人。
5. **不寫存活數字當結論**（B4）；不點名機構；認知復健的可及性寫「問復健科與個管師」。
6. **文件那一節不給法律建議**，只給「為什麼早」的數字＋兩篇指路。

### 台灣端（D2）

| 項目 | 結果 | 路徑 |
|---|---|---|
| 職能治療評估 | **查到**：**43026C 職能治療評估 240 點**（同一病患治療期間一個月限申報一次；同一治療期間超過三個月不予支付）[D[S66]] | 政府資料開放平臺 dataset 174451 → 健保署 `info.nhi.gov.tw/api/iode0000s01/Dataset?rId=A21030000I-D20020-002` 全表 TXT，2026-09-03 重新下載 |
| 一般／特殊職能治療 | **查到**：**45031C 一般職能治療（次）299 點**（一般治療項目 1–2 項、合計 40 分鐘）；**45095C 特殊職能治療（次）325 點**，特殊治療項目明列 **「(3) 知覺認知訓練 (4) 執行功能訓練」**[D[S66]] | 同上 |
| **複雜職能治療（本篇最相關）** | **查到**：**43031C 複雜 500 點**，適應症第一項「成人中樞神經系統疾患」的 ICD-10-CM 清單**明確含 C71、C72**（腦及其他中樞神經系統惡性腫瘤）；**限因上述診斷住院期間及出院後六個月內**，治療項目三項以上、合計 30 分鐘以上，且須含 OT 1／3／4／5／7／8／9／10／11／**12（知覺認知訓練 Cognitive training）**中的兩項以上；並限復健專科醫師開立處方[D[S66]] | 同上 |
| 心理治療項目 | **查到**：45010C 支持性心理治療 97 點、45013C 深度心理治療（每四十分鐘）－成人 1,203 點、45087C 特殊心理治療－成人 344 點[D[S66]] | 同上 |
| 「認知復健」作為獨立支付項目 | **查無此名稱的獨立項目**——全表檢索「認知功能」「認知治療」「神經心理」「心理衡鑑」皆 0 筆；認知訓練是**包在職能治療項目底下的治療項目**（OT 12、45095C 特殊治療項目第 3 項）[D[S66]] | 同上 |
| 實際申報條件（次數、療程） | **不推論**。條文只寫到上述限制，個別病人能不能申報、申報幾次，**寫「問復健科與個管師」** | — |

**文章寫法**：可以寫「**腦惡性腫瘤（C71）確實列在複雜職能治療的適應症診斷碼裡，而且治療項目裡就有『知覺認知訓練』**」，
並立刻接上「**但條文限住院期間與出院後六個月內，實際能不能申報請問復健科與個管師**」。
**不可寫成「健保有給付認知復健」**——沒有這個名稱的項目。

### 給繪圖組的數字（D2）

- **診斷時的認知損害**：新診斷 GBM **76%**（n=45，分項：記憶保留 53%／執行 51%／立即回想 42%／流暢 41%／注意力 24%）[D[S21]]；
  額顳葉腦瘤治療前 **>90%**（執行功能 78%、記憶與注意力 >60%，n=139）[D[S20]]。
- **長期存活者**：≥5 年 grade 4，**78% 至少一項受損**（n=185）；各項介於 17.4%–58.7%[D[S52]]。
- **放射性腦白質病變累積發生率曲線**：**12 個月 21%、36 個月 42%、60 個月 48%**（n=81 高惡性度膠質瘤長期存活者）[D[S51]]。
- **決定能力的三個時間點（強烈建議做成一條時間軸）**：
  **確診後不久 >50% 能力受損**（n=26）[D[S27]] → **KPS 90–100 仍只有 46% 全項有能力**（n=71）[D[S28]] →
  **復發時神經認知完好只剩 18.8%**（n=500）[D[S54]]。
- **文件落差長條圖**：ACP 記載率 **膠質瘤 20.1% vs 五大實體癌 58.0%**；
  「由病人本人決定」**21.4% vs 67.1%**（n=229 vs 4,283）[D[S29]]。
- **照顧者**：憂鬱 **37.15%（22.00–52.30）**、焦慮 **49.47%（35.81–63.12）**、負擔 **64%（54–74）**（15 篇、974 人）[D[S57]]。
- **每一格都要標族群**，尤其腦轉移（CC001／RTOG 0614）與低惡性度膠質瘤（Klein／Douw）不可混進 GBM 的格子。

---

## D3 `gb-recurrence`〈復發之後，還有哪些路〉

### 這一篇的地基：EANO 2021 的復發 GBM 整段（逐字可引，最安全）

「Standard-of-care treatments for patients with recurrent glioblastoma **are not well defined**; treatment is selected on the basis of
prior therapy, age, KPS, MGMT promoter methylation status and patterns of disease progression.」[D[S5]]
→ **這句話應該是 D3 的第一段**：不是「還有很多路」，是「沒有標準答案，所以是逐案挑」。

### Key facts

#### A. 復發的定義與時間點

- **判讀規則屬 D1**：RANO 2.0 規定放療後 12 週內懷疑惡化必須確認[D[S2]]；EANO 的 4–8 週複查[D[S5]]。
  **D3 只需一句指向 D1。**
- **「什麼時候算復發」在臨床上最實用的一條界線是 EANO 的六個月**：
  「Second surgery is an option for ~20–30% of patients, commonly with **symptomatic but circumscribed relapses diagnosed
  not earlier than 6 months after initial surgery**. **Second surgery earlier than 6 months after initial surgery increases the risk of
  unnecessary intervention on the basis of pseudoprogression** and is unlikely to provide durable benefit if the initial surgery
  followed by radiotherapy did not provide tumour control for more than a few months.」[D[S5]]
  → **D1 與 D3 在這裡接上：假性惡化不是影像學上的趣聞，它會讓人白挨一刀。**
- **無惡化存活的數字屬 B1／B4**，D3 一句指路，不重寫。
- **RTOG 1205 的收案條件可以當「什麼樣的復發才進得了試驗」的具體例子**：
  「imaging evidence of tumor progression **≥ 6 months from completion of prior chemo-RT**」[D[S31]]。

#### B. 再手術——全部是觀察性資料，而且它的「好處」被方法學翻過一次

- **誰適合**：EANO 原文——**約 20–30% 的病人是再手術的候選人**，典型是「**有症狀、但界限清楚**」的復發，
  且**距第一次手術不早於六個月**[D[S5]]。另補一句：早期惡化且原本手術可能不夠徹底的有症狀病人也可考慮；
  「This procedure **might** improve post-recurrence survival in patients who are candidates for **gross total resection of enhancing tumour**」[D[S5]]。
- **最重要的一件事（紅線等級）**：Zhao 2019 統合分析（21 篇、8,630 人）[D[S38]]：
  - 把再手術當**固定共變數**：OS **HR 0.66（95%CI 0.61–0.71）**、post-progression survival **HR 0.70（0.57–0.88）**。
  - 把再手術當**時間相依共變數**：好處消失且方向反轉，**OS HR 2.19（95%CI 1.47–3.27）**；PPS 也不顯著（p=0.51）。
  - 作者結論原文：「survival benefits of reoperation in recurrent GBM **may be overestimated when analyzed as fixed covariates**.
    **Proper analysis methodology should be used in future work to confirm the clinical benefits of reoperation.**」
  → **白話：活得久的人才有機會等到「再開一次刀」這個事件。把它算成「開刀讓人活久」，是把因果接反了。**
- **2025 年的更新統合分析（36 篇、10,738 人，其中 2,806 人接受再手術；9 篇傾向分數配對、1 個臨床試驗）**[D[S41]]：
  再手術組平均 OS **19.66 個月** vs 化療±放療 **12.56 個月**；多變項 OS **HR 0.62（95%CI 0.50–0.76）**；
  **達到「增強腫瘤完全切除（CRET）」與較佳的復發後存活相關（HR 0.54，95%CI 0.39–0.73，p=0.04）**。
  作者結論原文：「**The role of reoperation in rGBM remains uncertain.** While it may improve survival in selected cases,
  **limited high-quality data hinder definitive conclusions.**」
- **再開刀開出來是什麼**：Blakstad 世代裡放療後 3 個月與 6 個月 MRI 之後共 16 人接受再切除，
  病理**只見反應性組織 2 人、腫瘤組織 9 人、兩者都有 5 人**；這 16 人**從第一次手術算起中位 OS 15.3 個月、
  從第二次手術算起 7.6 個月**[D[S3]]。
  另外，該世代中因影像被判假性惡化而仍被改治療的 2 人**都接受了第二次手術，病理只見反應性組織／壞死，沒有活性腫瘤**[D[S3]]。
  → **這兩段合起來，就是「六個月那條線」在真實世界的樣子。**

#### C. 再照射——GBM 專屬的隨機證據只有一個，而且主要終點是陰性的

**一般邏輯（正常組織修復、逐案評估、劑量不可自我換算）已在站上 `sit-reirradiation` 寫過，D3 不重寫，只寫 GBM 專屬的。**

- **NRG Oncology／RTOG 1205（Tsien 2023，JCO 2023;41(6):1285–1295）**[D[S31]]——
  **這是第一個用現代放療技術評估復發 GBM 再照射的前瞻隨機多中心試驗**（作者自述 "To our knowledge... the first"）：
  - 設計：**第二期隨機**，再照射 **35 Gy／10 次** ＋ 同步 bevacizumab 10 mg/kg 每兩週 **vs** bevacizumab 單用直到惡化。
    2012 年 12 月至 2016 年 4 月隨機 182 人，**170 人合格**。分層因子：年齡、切除、KPS。
  - **主要終點 OS：沒有改善。HR 0.98（80%CI 0.79–1.23），P=.46；中位存活 10.1 vs 9.7 個月。**
  - **PFS：中位 7.1 vs 3.8 個月（HR 0.73，95%CI 0.53–1.0，P=.05）；
    6 個月無惡化率由 29.1%（19.1–39.1）提升到 54.3%（43.5–65.1），P=.001。**
  - **安全性：急性 3 級以上治療相關不良事件 5%，「no delayed high-grade AEs」。**
  - 作者結論原文：「re-RT was shown to be **safe and well tolerated**. BEV + RT demonstrated a **clinically meaningful improvement
    in PFS**, specifically the 6-month PFS rate **but no difference in OS**.」
  → **D3 的正確措辭：再照射（在這個劑量與這個組合下）是安全的、把惡化往後推了，但沒有讓人活得比較久。**
- **分次方案的官方描述（EANO 2021，逐字）**[D[S5]]：
  「The efficacy of re-irradiation and the value of amino acid PET for target delineation **remain debated**.
  **Radiation fractionation depends on tumour size. Larger lesions require smaller single fraction sizes** to improve the safety and
  tolerability. Doses of conventional or near conventional fractionation have been tested as well as higher doses per fraction (5–6 Gy)
  using stereotactic hypofractionated radiotherapy to a total dose of **30–36 Gy** or even radiosurgery with a single dose of
  **15–20 Gy**, all with **acceptable toxicity profiles**.」
  → **可以引這一段，但必須照站上 `sit-reirradiation` 的規矩：這些是計畫參數，不是讀者可以拿來自我評估的東西。**
    建議寫法：只寫「**腫瘤越大，每次的劑量就要越低**」這個原則，數字放在指引原文的引號裡並標明是計畫參數。
- **放射性壞死的風險**：RTOG 1205 沒有觀察到延遲的高等級不良事件[D[S31]]；
  一般性的再照射壞死風險（含「治療體積越小、累積劑量可以越高」「間隔月數與壞死發生率無相關」）
  **已在站上 `sit-reirradiation` 寫過，D3 一句指路，不重寫**。

#### D. bevacizumab——把「改善什麼」和「不改善什麼」徹底分開

**(1) 復發情境**

- **EORTC 26101（Wick 2017，NEJM 2017;377(20):1954–1963，n=437，第一次惡化的 GBM，2:1 隨機）**[D[S39]]：
  - **主要終點是 OS，結果是陰性**：lomustine＋bevacizumab **9.1 個月**（95%CI 8.1–10.1）vs lomustine 單用 **8.6 個月**
    （95%CI 7.6–10.4），**死亡 HR 0.95（95%CI 0.74–1.21），P=0.65**。
  - **PFS 是正向的**：**4.2 vs 1.5 個月**（HR 0.49，95%CI 0.39–0.61，P<0.001），差 2.7 個月。
  - **3–5 級不良事件：合併組 63.6% vs 單用組 38.1%。**
  - **生活品質與神經認知功能：加上 bevacizumab 兩者都沒有影響**（"affected neither health-related quality of life nor
    neurocognitive function"）。**MGMT 狀態具預後意義。**
  - **這一句是 D3 全篇最需要被正確轉述的一句：PFS 好看、OS 沒動、副作用翻倍、生活品質沒變。**
- **BELOB（Taal 2014，Lancet Oncol 2014;15(9):943–953，n=153，隨機第二期，三組）**[D[S30]]：
  - 主要終點是**九個月存活率**：lomustine 單用 **43%**（29–57）、bevacizumab 單用 **38%**（25–51）、
    bevacizumab＋lomustine 90 mg/m² **59%**（43–72）、合併兩個劑量組 **63%**（49–75）。
  - **安全性事件改變了試驗**：前八人出現血液毒性（3 人 3 級、2 人 4 級血小板低下），**lomustine 劑量由 110 降到 90 mg/m²**。
  - 作者結論原文：「The combination... met prespecified criteria for assessment... in further phase 3 studies.
    However, **the results in the bevacizumab alone group do not justify further studies of this treatment.**」
  → **BELOB 是「第二期看起來可以、第三期沒過」的另一個例子**（EORTC 26101 就是那個第三期）。
- **反應率不是存活**：BRAIN 試驗（Friedman 2009，n=167，第二期非比較性）[D[S40]]：
  bevacizumab 單用**客觀反應率 28.2%**、bevacizumab＋irinotecan **37.8%**；
  中位總存活 9.2 與 8.7 個月；6 個月無惡化率 42.6% 與 50.3%。
  **類固醇那一句必須逐字引，不可加碼**：「**There was a trend** for patients who were taking corticosteroids at baseline to take
  stable or decreasing doses over time.」——**是趨勢，沒有統計檢定，不是「證實可以減類固醇」。**
- **EANO 對它的定位（逐字，最安全的寫法）**[D[S5]]：
  - 「Bevacizumab... is approved for the treatment of recurrent glioblastoma in the USA, Canada, Switzerland and several other
    countries outside the European Union, **but no OS benefit has been demonstrated from its use**」
  - 「**The main value of this agent in routine clinical practice is transient symptom control and the option for sparing treatment
    with steroids in symptomatic patients with large tumours.**」
  - 「Bevacizumab is **not approved** for patients with recurrent glioblastoma **in the European Union**, although it has been approved
    for this indication in other countries on the basis of **objective response rates of ~30% in two uncontrolled** [trials]」
  → **「省類固醇」只能寫到 EANO 這個「option」的層級＋BRAIN 的「趨勢」；不可寫成試驗證實。**

**(2) 新診斷情境（兩個第三期，OS 都是陰性）——D3 只需一段，主場在 B5**

- **AVAglio（Chinot 2014，NEJM 2014;370(8):709–722，n=921）**[D[S32]]：
  PFS **10.6 vs 6.2 個月**（HR 0.64，95%CI 0.55–0.74）；**「The addition of bevacizumab to radiotherapy-temozolomide
  did not improve survival」**；觀察到基線生活品質與體能狀態的維持，**但不良事件比率較高**。
- **RTOG 0825（Gilbert 2014，NEJM 2014;370(8):699–708，637 人隨機）**[D[S33]]：
  中位 OS **15.7 vs 16.1 個月**（死亡 HR 1.13，**沒有差異**）；PFS **10.7 vs 7.3 個月**（HR 0.79，**未達預設目標**）；
  **「Over time, an increased symptom burden, a worse quality of life, and a decline in neurocognitive function were more frequent
  in the bevacizumab group.」**
  → **兩個試驗對生活品質的結論方向相反（AVAglio 較好、RTOG 0825 較差）。這件事本身要寫出來，不可只挑一邊。**

**(3) bevacizumab 用於放射性壞死——證據等級高、族群不對**

- Levin 2011（IJROBP 2011;79(5):1487–1495）[D[S37]]：**安慰劑對照、雙盲、隨機，但 n 只有 14**。
  收案要求影像或病理證實的中樞神經放射性壞死＋進行性神經症狀，
  **且曾接受放療的原疾病是「head-and-neck carcinoma, meningioma, or low- to mid-grade glioma」**。
  結果：安慰劑組 0/7 有反應，**bevacizumab 組 5/5（隨機）與 7/7（交叉）全部在 T2/FLAIR 與 T1 增強體積上縮小**，
  **且全部出現神經症狀或徵象的改善**；作者稱其為 Class I evidence。
  → **引用時必須寫「這個試驗收的不是高惡性度膠質瘤，而且只有 14 個人」。**
- **台灣端**：健保 bevacizumab 給付規定第 9.37 條**沒有放射性壞死這個適應症**[D[S61]]（見台灣端）。

#### E. lomustine 與 nitrosourea——它是對照臂，不是勝出者

- **EANO 原文（逐字，最重要的一句）**[D[S5]]：
  「**Lomustine (90–110 mg/m²) has never been shown to have superiority over another agent in an RCT** but is increasingly considered
  as **the most appropriate standard of care on the basis of its activity as the control arm of several RCTs** and is also used in the
  AGILE trial, with **6-month PFS rates of ~20%**.」
  → **這是一個很好的教材句：一個藥成為「標準」，可以是因為它一直被拿來當對照組，而不是因為它贏過誰。**
- 毒性的形狀不一樣（EANO 逐字）[D[S5]]：nitrosourea 類（lomustine、carmustine、nimustine、fotemustine）造成的是
  **延遲（4–6 週）而非早期（2–3 週）的、而且更常是累積性的**白血球與血小板低下，
  可能導致療程中斷、減量甚至停藥；**肺纖維化主要見於 carmustine，lomustine 罕見**。
- **temozolomide 再挑戰**：EANO 寫「Similar results have been reported with alternative dosing schedules of temozolomide but
  **activity is probably limited to patients with tumours with MGMT promoter methylation**」；
  且「**No data from RCTs support the view that dose-intensified schedules are superior to standard-dose temozolomide**」[D[S5]]。
- **carmustine 植入劑（Gliadel）**：EANO 寫「provided a **modest** OS benefit in patients with newly diagnosed WHO grade 3 or 4
  gliomas **or recurrent glioblastoma**; however, in the pivotal trial... patient outcomes were **not statistically significantly different**
  after patients with WHO grade 3 tumours... 」[D[S5]]。**台灣有給付條文（第 9.35 條），見台灣端。**

#### F. regorafenib——第二期正向、第三期推翻，這是本篇最重要的一課

- **REGOMA（Lombardi 2019，Lancet Oncol 2019;20(1):110–119）**[D[S34]]：
  隨機、開放標籤、**第二期**，義大利 10 中心，n=119（regorafenib 59／lomustine 60）。
  中位追蹤 15.4 個月時 99/119（83%）死亡。
  **主要終點 OS：7.4 個月（95%CI 5.8–12.0）vs 5.6 個月（4.7–7.3），HR 0.50（95%CI 0.33–0.75），log-rank p=0.0009。**
  3–4 級治療相關不良事件 **56%（33/59）vs 40%（24/60）**。
  作者自己的結論就寫著「should be investigated in an **adequately powered phase 3 study**」。
- **GBM AGILE（Wen 2026，JCO 2026;44(18):1676–1686，NCT03970447）**[D[S35]]：
  貝氏適應性平台第二／三期註冊試驗，regorafenib 是第一個進場的實驗臂，
  族群是**新診斷未甲基化（NDU）**與**復發（RD）**；對照臂是 temozolomide＋放療（新診斷）或 **lomustine（復發）**。
  **結論原文：「GBM AGILE did not show superiority of regorafenib over control in RD (lomustine) or NDU
  (temozolomide + radiotherapy) glioblastoma, yet caused increased toxicities. Regorafenib has been removed from
  National Comprehensive Cancer Network guidelines as a treatment option for RD.」**
  （**這句話裡出現的指引名稱是原文引述的一部分；本專題不引用該指引本身，也不轉述其內容。**）
- 同期 Neuro-Oncology 社論的標題本身就可以當一句話總結：
  「**Gods do play dice: The activity of regorafenib in glioblastoma not confirmed**」[D[S36]]。
- **台灣端對得起來**：健保給付規定第 9.51 條與食藥署仿單，**適應症都只有大腸直腸癌、胃腸道間質瘤、肝細胞癌**[D[S65]][D[S68]]。

#### G. TTFields 在復發——陰性，主場在 B5

- **EF-11（Stupp 2012，Eur J Cancer 2012;48(14):2192–2202，n=237）**[D[S73]]：
  TTFields 單用（每天 20–24 小時）vs 醫師選擇的化療。
  **主要終點 OS 沒有改善：中位 6.6 vs 6.0 個月（HR 0.86，95%CI 0.66–1.12，p=0.27）；一年存活率都是 20%。**
  6 個月無惡化率 21.4% vs 15.1%（p=0.13）；反應率 14% vs 9.6%（p=0.19）。
  **嚴重不良事件 6% vs 16%（p=0.022）；生活品質多數面向偏向 TTFields。**
- EANO 一句話總結：「**tumour-treating fields were not superior to physician's choice of best treatment**」[D[S5]]。
- **D3 只寫這一段，其餘（台灣法規身分、可及性、排擠效應）一句指向 B5 與站上 `sit-ttfields`。**

#### H. 免疫治療在復發——一句話，指向 B5

EANO 逐字：「**nivolumab was not superior to bevacizumab**」[D[S5]]；「So far, **only a limited role for targeted therapy in
recurrent glioblastoma** has been shown」[D[S5]]。**其餘屬 B5。**

#### I. 臨床試驗——指向站上 `sit-trial-how`，不重寫

- 可以用的一句事實：**lomustine「也被用在 AGILE 試驗裡」當對照臂**[D[S5]]；GBM AGILE 是貝氏適應性平台試驗[D[S35]]。
  → 這可以順便解釋「為什麼參加試驗不等於一定拿到新藥」——平台試驗有對照臂。
- **怎麼查、收案條件怎麼讀、退出是權利、同意書該問什麼**：站上〈臨床試驗，怎麼找怎麼看〉已經寫完，**一句指路**。

#### J. 什麼時候談安寧——有第三期隨機試驗了，而且要誠實地寫

- **EPCOG（Golla 2026，Neuro-Oncology 2026;28(1):226–240）**[D[S42]]——**GBM 專屬的早期緩和照護第三期隨機試驗**：
  - 設計：六家德國大學醫學中心，**診斷後四週內**（初診或復發）收案的 GBM 病人與其照顧者，
    隨機到標準照護（對照 n=108）或標準照護＋早期整合緩和照護（介入 n=109），介入持續 12 個月，評估者盲性。
  - **主要終點（六個月時 FACT-Br trial outcome index 的生活品質變化）：沒有達到統計顯著**
    ——平均差 4.1（95%CI −4.4 到 12.6），**P=.34**。
  - 因為**兩組存活有顯著差異、而且是對照組較長（P=.018）**，作者做了以死亡時間校正的分析，**校正後生活品質較佳（P=.041）**。
  - 次要終點：**緩和照護問題與情緒顯著獲益，尤其在介入結束之後**；**照顧者沒有獲益**。
  - 結論原文：「Provided that the survival difference is included in the analysis, EIPC improves QoL in glioblastoma patients.
    This... demonstrates that EIPC sustainably improves '**how to live**' but **not 'length of life**'.」
- **EANO 緩和照護指引（Pace 2017，Lancet Oncol 2017;18(6):e330–e340）**[D[S43]]：
  「The life-limiting nature of gliomas and the presence of specific symptoms related to neurological deterioration necessitate an
  appropriate and **early palliative care approach**.」並自陳目前缺乏證據、需要研究的領域包括
  **疲倦、行為與情緒障礙、照顧者需求的介入，以及預立醫療照護諮商的時機**。
- **2023 年的更新回顧（Koekkoek 2023，140 篇）**[D[S44]]：
  「**Early palliative care interventions are essential to define goals of care and minimize symptom burden in a timely fashion.**」
  同時誠實寫著「**No pharmacological agents have been shown in randomized controlled trials to significantly improve fatigue or
  neurocognition.**」
- **為什麼腦瘤要更早**：Sizoo 2014 系統性回顧（17 篇）——「**Cognitive deficits increase as the disease progresses, hampering
  communication and decision making**」，且腦瘤病人使用緩和照護服務比其他癌症病人更密集[D[S45]]。
- **實際發生了什麼**：韓國 GBM 世代中，接受安寧照會者中位**從首次照會到死亡只有 44 天**；
  **接受照會者較少接受侵略性末期照護**[D[S58]]；跨歐三國資料中**只有 53% 的病人被家屬認為得到良好的照護品質**[D[S46]]。
- **「最後那幾週會發生什麼」屬站上 `sit-last-weeks`，D3 一句指路，不重寫。**

### 反方向的資料（誠實必列）

1. **再手術的存活好處在時間相依分析裡消失、甚至反轉**[D[S38]]；2025 年的更新統合分析自陳「**remains uncertain**」[D[S41]]。
2. **再照射沒有改善總存活**（RTOG 1205，主要終點陰性）[D[S31]]。
3. **bevacizumab 在復發沒有改善總存活**（EORTC 26101，P=0.65），而且**3–5 級不良事件由 38.1% 升到 63.6%**[D[S39]]；
   **生活品質與神經認知也沒有改善**[D[S39]]。
4. **bevacizumab 在新診斷的兩個第三期，OS 都是陰性**；而且兩試驗對生活品質的結論**方向相反**[D[S32]][D[S33]]。
5. **regorafenib 的第二期被第三期推翻**[D[S34]][D[S35]][D[S36]]。
6. **TTFields 在復發是陰性的**[D[S73]][D[S5]]。
7. **lomustine 從來沒有在隨機試驗裡贏過別的藥**[D[S5]]。
8. **早期緩和照護的第三期主要終點沒過，照顧者沒有獲益，而且存活方向是對照組較長**[D[S42]]。
9. **bevacizumab 治放射性壞死的隨機試驗收的不是高惡性度膠質瘤，n=14**[D[S37]]。

### Claim ceiling（D3）

**可寫：**
- 「復發 GBM 沒有標準治療；要選哪一條，看的是先前治療、年齡、體能狀態、MGMT 與惡化的樣子」[D[S5]]（逐字引最安全）
- 「再手術大約適用兩到三成的人，典型是有症狀、界限清楚、而且**距第一次手術不早於六個月**的復發；
  太早開刀，會因為假性惡化而白挨一刀」[D[S5]]
- 「再手術與存活的關聯**全部是觀察性資料**；把手術當成時間相依事件重新分析，好處會消失（HR 由 0.66 變成 2.19）」[D[S38]]
- 「如果要開，能不能把增強的部分完全切掉，跟復發後存活有關（HR 0.54）——但這仍是觀察性的」[D[S41]]
- 「再照射（35 Gy／10 次＋bevacizumab）在唯一一個隨機試驗裡**是安全的、把惡化往後推了（6 個月無惡化率 29.1%→54.3%），
  但沒有讓人活得比較久（10.1 vs 9.7 個月，P=.46）**」[D[S31]]
- 「腫瘤越大，每次的劑量要越低」[D[S5]]（原則可寫；劑量數字放在指引引號內並標明是計畫參數，其餘指向 `sit-reirradiation`）
- 「bevacizumab 在復發 GBM：**惡化的時間從 1.5 個月延到 4.2 個月，但總存活 9.1 對 8.6 個月、看不出差別**；
  代價是 3 級以上不良事件從 38.1% 升到 63.6%」[D[S39]]
- 「它在臨床上的主要價值是**暫時的症狀控制**，以及**對腫瘤大、有症狀的病人省下類固醇的選項**」[D[S5]]（逐字引）
  ——**同段必須加註：省類固醇這件事在隨機試驗裡沒有被當主要終點量過，BRAIN 只寫了「趨勢」**[D[S40]]
- 「片子可以變好三成，人不會因此活得比較久」[D[S40]][D[S39]]
- 「lomustine 從來沒有在隨機試驗裡證明贏過別的藥；它之所以被當成標準，是因為它一直是別人的對照組，6 個月無惡化率大約 20%」[D[S5]]
- 「temozolomide 再挑戰的活性**大概只在 MGMT 甲基化的人身上**；加大劑量沒有隨機試驗支持」[D[S5]]
- 「regorafenib 的第二期（REGOMA）中位存活 7.4 對 5.6 個月、HR 0.50；**但第三期平台試驗 GBM AGILE 沒有證明它優於對照，
  而且毒性更高**」[D[S34]][D[S35]]
- 「電場治療在**復發**這個情境的隨機試驗是陰性的（6.6 對 6.0 個月，p=0.27），但嚴重不良事件比化療少（6% 對 16%）」[D[S73]]
- 「早期緩和照護的第三期試驗：**主要終點沒過**；情緒與緩和照護問題有改善；**照顧者沒有獲益**；
  作者自己的話是『改善的是怎麼活，不是活多久』」[D[S42]]
- 「指引寫的是：腦瘤病人因為神經功能會退化，需要**早一點**的緩和照護取向」[D[S43]][D[S44]]
- 「隨著病程進展，認知缺損會加重，溝通與做決定會變困難」[D[S45]]——接到 D2 的文件那一節

**不可寫（超線）：**
- ❌ **「再開一次刀可以多活半年」**——時間相依分析裡好處反轉[D[S38]]。
  凡引用 19.66 vs 12.56 個月，**同段必須寫「這是觀察性資料，而且選擇偏差很大：能被挑去開刀的人本來就比較好」**。
- ❌ 「再照射可以延長存活」[D[S31]]。
- ❌ 「bevacizumab 可以減少類固醇用量（有證據）」——只能寫到 EANO 的「option」與 BRAIN 的「趨勢」[D[S5]][D[S40]]。
- ❌ 「bevacizumab 讓生活品質變好」——EORTC 26101 說沒有影響[D[S39]]；新診斷的兩個試驗結論相反[D[S32]][D[S33]]。
- ❌ 只寫 REGOMA 不寫 GBM AGILE[D[S35]]。
- ❌ 把 EF-11 寫成「電場在復發有效」[D[S73]]。
- ❌ 「早點接受安寧會活得比較久／比較好」——EPCOG 主要終點陰性，且存活方向相反[D[S42]]。
- ❌ 任何具體的再照射劑量／間隔，被寫成讀者可以自我評估的形式（沿用 `sit-reirradiation` 的紀律）。
- ❌ 存活月數當結論（屬 B4）；**復發情境的中位存活數字只能用在「試驗結果的比較」脈絡裡，並一句指向 B4。**
- ❌ 引用 NCCN 或轉述其內容（GBM AGILE 摘要中的那句話只能整句引述為「該試驗結論原文」）。
- ❌ 重寫 `sit-reirradiation`、`sit-trial-how`、`sit-last-weeks`、`sit-ttfields` 的內容。

### Caveats／safety notes（寫作者必寫）

1. **這一篇最危險的讀法是「還有這麼多路，所以不用急」，以及反過來的「都沒用，那就算了」。**
   兩邊都要擋：每一條路都要同時寫「它改善什麼」「它不改善什麼」「代價是什麼」。
2. **開頭建議直接用 EANO 的那句「沒有明確的標準治療」**[D[S5]]，把「為什麼每個人的建議都不一樣」講清楚。
3. **急症出口（指向 C4）**：復發期新出現的劇烈頭痛、清晨頭痛合併噴射性嘔吐、意識改變、單側無力、癲癇發作、
   **以及腿腫或突然喘（GBM 是深部靜脈栓塞與肺栓塞的高風險族群）**——**當天回來**。
4. **不寫本院順位**（SPEC §一⑤③ 尚未由作者拍板）。措辭寫成「這幾條路怎麼排順序，各家團隊不一樣，
   要在多專科會議上依你的狀況決定」，**不點名機構、不寫本院有沒有**。
5. **利益揭露**：SPEC 規定只放在 A3、B1、B4、B5；**D3 不放**，但寫再照射那一段時語氣要更保守
   （作者自己做這一段，站上 `sit-reirradiation` 已經自我揭露過，一句指路）。
6. **費用紀律**：全文檔搜尋到的健保條文逐字引；查不到的寫「問醫務課」；**永不推論有無給付**。

### 台灣端（D3）

| 項目 | 結果 | 路徑 |
|---|---|---|
| **bevacizumab 用於復發 GBM 的給付條文（逐字）** | **查到**：藥品給付規定 **第 9.37 條第 2 項「惡性神經膠質瘤(WHO 第4級)-神經膠母細胞瘤」**：「(1) **單獨使用**可用於治療**曾接受標準放射線治療且含 temozolomide 在內之化學藥物治療失敗**之多型性神經膠母細胞瘤(Glioblastoma multiforme)**復發**之成人患者。(101/05/1)(2) **須經事前審查核准後使用，每次申請事前審查之療程以 12 週為限**，再次申請必須提出客觀證據（如：影像學）證實無惡化，才可繼續使用。」條文版本日期含 114/10/1[D[S61]] | 健保署藥品給付規定 API（`info.nhi.gov.tw/api/INAE3000/INAE3000S01/SQL0001`，DRUG_ING=bevacizumab）取得規定碼 9.37.，再以 `getPDF?DurgFileName=9.37._20251001.pdf` 直接下載 PDF 後 pdftotext，2026-09-03 重新抓取 |
| **temozolomide 給付條文（逐字，與 B 組交叉核對）** | **查到**：**第 9.25 條**「限用於 1.經手術或放射線治療後**復發**之下列病人：(1) 退行性星狀細胞瘤(AA) (2) **多形神經膠母細胞瘤(GBM)** (3) 退行性寡樹突膠質細胞瘤(98/9/1)。2.**新診斷的多形神經膠母細胞瘤，與放射線治療同步進行，然後作為輔助性治療**。(97/1/1) 3.**需經事前審查核准後使用**。4.若用於退行性寡樹突膠質細胞瘤，每日最大劑量 200 mg/m²，每次申請事前審查之療程以三個月為限……若復發之惡性膠質細胞瘤有惡化之證據，則必須停止使用。(98/9/1)」——現行 temozolomide 品項連結的正是這一版（檔名 9.25._20090901_000.pdf）[D[S60]] | 同上（DRUG_ING=temozolomide） |
| carmustine 植入劑（Gliadel） | **查到**：**第 9.35 條**「1.作為**復發性多形神經膠母細胞瘤病人的手術輔助**，且**不得與 temozolomide 併用**。2.需經事前審查核准後使用。」現行品項 B0247772BG 格立得植入劑（起 102.10.01，迄今）[D[S62]] | 同上（DRUG_ING=carmustine） |
| lomustine（CCNU） | **查到**：現行仍有四個健保品項（治先優膠囊 10／40 公絲、希恩優膠囊 10／40 公絲），**「藥品給付規定」欄位為空**（沒有對應的條文編號）[D[S63]] | 同上（DRUG_ING=lomustine） |
| **regorafenib 是否可用於 GBM** | **查到（重要陰性）**：給付規定**第 9.51 條只列轉移性大腸直腸癌、胃腸道間質瘤、肝細胞癌**，**沒有膠質母細胞瘤**[D[S65]]；食藥署仿單（癌瑞格膜衣錠 40 毫克，衛部藥輸字第 026168 號）適應症同樣只有這三個癌別[D[S68]] | 給付規定 PDF `9.51._20240601.pdf`；食藥署未註銷藥品許可證資料集 |
| bevacizumab 用於**放射性壞死** | **條文中未列此適應症**（第 9.37 條的六個適應症群組中沒有放射性壞死）[D[S61]]。**不推論可否申請**，寫「問醫務課」 | 同上 |
| 再照射有無獨立支付項目 | **gap**——沿用站上 `sit-reirradiation` 的查證結論（支付標準全表中查不到「再照射」項目）；本次以 2026-09-03 重新下載的全表覆核，仍未檢出[D[S66]] | 支付標準全表 TXT 全文檢索 |
| 「電場」在支付標準全表 | **零筆**（2026-09-03 重新確認）[D[S66]] | 同上 |
| 復發 GBM 的台灣治療指引 | **gap**——未檢出可引用的官方文件 | — |

### 給繪圖組的數字（D3）

- **「改善什麼／不改善什麼」對照表（本篇最該做的一張圖，不必是曲線）**：
  | 做法 | PFS／反應 | OS | 代價 |
  |---|---|---|---|
  | 再照射＋bev（RTOG 1205，n=170） | 6 個月無惡化 29.1%→54.3%；中位 PFS 3.8→7.1 月 | **10.1 vs 9.7 月，P=.46** | 急性 3 級以上 5%，無延遲高等級毒性[D[S31]] |
  | lomustine＋bev（EORTC 26101，n=437） | 中位 PFS 1.5→4.2 月（HR 0.49） | **9.1 vs 8.6 月，P=0.65** | 3–5 級 38.1%→63.6%[D[S39]] |
  | bev 單用（BRAIN，n=167，非比較性） | 反應率 28.2% | 9.2 月（單臂） | 3 級以上 46.4%[D[S40]] |
  | regorafenib（REGOMA 第二期 → GBM AGILE 第三期） | REGOMA OS HR 0.50 | **GBM AGILE：未優於對照** | 3–4 級 56% vs 40%；AGILE 毒性更高[D[S34]][D[S35]] |
  | TTFields（EF-11，n=237） | 6 個月無惡化 21.4% vs 15.1%（p=0.13） | **6.6 vs 6.0 月，p=0.27** | 嚴重不良事件 6% vs 16%[D[S73]] |
  | 早期緩和照護（EPCOG，n=217） | — | 主要終點是生活品質，**P=.34 未達顯著** | 對照組存活較長（P=.018）[D[S42]] |
- **再手術的「同一份資料、兩種算法」對照（可做成兩根對比的長條）**：
  固定共變數 **HR 0.66（0.61–0.71）** vs 時間相依共變數 **HR 2.19（1.47–3.27）**（21 篇、8,630 人）[D[S38]]。
  **圖說必須寫：這不是兩份資料，是同一份資料換一種算法。**
- **六個月那條線**（接 D1 的時間軸）：EANO——再手術通常用在**距第一次手術不早於六個月**的復發；
  更早開刀會因假性惡化而白挨一刀[D[S5]]；Blakstad 世代裡因影像被改治療的兩位假性惡化病人，
  **開出來只有反應性組織／壞死**[D[S3]]。

---

## 全專題台灣端總掃（Group D 負責，2026-09-03）

**方法紀律**：所有結果都是本日實際抓取的官方檔案內容。
**「查無」一律寫成「我在某某官方查詢裡查不到」，不寫「沒有給付／沒有核准」。**
媒體報導的價格與適應症一律不採用。

### 兩條本次打通的新路（給其他組沿用）

1. **健保藥品給付規定，走 API 不走網頁**（nhi.gov.tw 的 HTML 會被擋，這條不會）：
   - 查品項與規定碼：`POST https://info.nhi.gov.tw/api/INAE3000/INAE3000S01/SQL0001`，
     body `{"CURPAGE":1,"PAGESIZE":500,"DRUG_ING":"<成分英文名>"}`，
     header 需 `Content-Type: application/json` 與 `Referer: https://info.nhi.gov.tw/INAE3000/INAE3000S02`。
     **注意：只有 `DRUG_ING`（成分名）這個參數有效；傳 `DRUG_ENAME`／`DRUG_CNAME` 會被忽略並回傳全資料庫（total=224811）。**
     回傳欄位 `paY_CODE_LIST` 是給付規定條號、`druG_UFILE_NAME_LIST` 是對應 PDF 檔名、`paY_END_DATE` 空白或「迄今」表示現行。
     **民國年字串不可直接比大小**（"89.03.31" 字串大於 "115.09.03"），要先轉西元再比。
   - 抓條文 PDF：`GET https://info.nhi.gov.tw/api/INAE3000/INAE3000S01/getPDF?DurgFileName=<檔名>&appType=true`，再 `pdftotext -layout`。
2. **食藥署藥證，走政府資料開放平臺的 TFDA API，不走 `info.fda.gov.tw`**（後者本日仍 DNS／TLS 失敗）：
   - `GET https://data.fda.gov.tw/data/opendata/export/37/csv` →
     回傳的是 **ZIP**（內含 `37_2.csv`，UTF-8 with BOM，約 16.8 MB、26,027 筆），資料集名稱
     **【9123】未註銷藥品許可證資料集**（每週與藥證業務管理系統同步）。
     欄位含：許可證字號、註銷狀態、有效日期、發證日期、中文品名、英文品名、**適應症**、劑型、主成分略述、申請商、製造廠。
   - 資料集清單在 `https://data.fda.gov.tw/data/dataset/oas/classification/a5c2c11b-2cbd-4917-a1f3-2d6eee97c057`（藥品分類的 OpenAPI 文件）。
3. **健保支付標準全表**：政府資料開放平臺 dataset 174451 →
   `https://info.nhi.gov.tw/api/iode0000s01/Dataset?rId=A21030000I-D20020-002`（約 22 MB TXT，UTF-8 BOM、CRLF、`^` 分欄，6,186 筆）。
4. **全國法規資料庫**可直接 curl：`https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=<代碼>`。
5. **仍然打不通的**：`info.fda.gov.tw`（DNS/連線失敗）、`www.hpa.gov.tw`（TLS 失敗，連 data.gov.tw 指向它的檔案連結也一起失敗）、
   `cris.hpa.gov.tw`（連線失敗）、`data.nhi.gov.tw`（連線失敗）。**hpa.gov.tw 的替代路徑是 `twcr.tw` 與 `www.mohw.gov.tw`。**

### 逐項結果

| # | 項目 | 結果 | 出處 |
|---|---|---|---|
| 1 | **bevacizumab 用於復發 GBM 的健保給付條文（逐字）** | **查到**。第 9.37 條第 2 項，見 D3 台灣端表格逐字內容。限單獨使用、限標準放療且含 temozolomide 化療失敗後之復發成人 GBM、須事前審查、每次 12 週 | [D[S61]] |
| 2 | **temozolomide 給付條文** | **查到**。第 9.25 條，同步期與維持期都在條文裡（第 2 項），復發用途在第 1 項，均須事前審查。**與 B 組交叉核對用**：現行所有 temozolomide 品項（含 115.04.01 新增的特莫斯膠囊）連結的都是同一版 9.25._20090901_000.pdf | [D[S60]] |
| 3 | **vorasidenib 的台灣藥證** | **查到（A 組 gap 已補上）**。**VORANIGO 瓦拉固膜衣錠 10 mg：衛部藥輸字第 029063 號；40 mg：第 029064 號**；製劑、**發證日 2025/12/23、有效日期 2030/12/23**；適應症逐字：「適用於治療罹患帶有 IDH1 或 IDH2 易感突變(susceptible IDH1 or IDH2 mutation)之**第 2 級**星狀細胞瘤或寡樹突神經膠質瘤，**已接受手術(包括切片、次全切除或完全切除)，且目前不須立即接受放射或化學治療**之 **12 歲以上**病人。」 | [D[S68]] |
| 3b | **vorasidenib 的健保給付** | **健保藥品給付項目查詢以成分名 vorasidenib 查詢為 0 筆。** 寫法：「有藥證；我在健保藥品給付項目裡查不到品項」，**不寫「健保不給付」** | [D[S63]] |
| 4 | **5-ALA（Gliolan）的台灣藥證** | **查到（A 組 gap 已補上）**。**格麗藍口服溶液用粉劑 / Gliolan Powder for Oral Solution，衛署藥輸字第 025524 號**；**發證 2012/04/20、有效日期 2027/04/20**；適應症逐字：「**用於成人患者進行惡性神經膠質瘤(WHO 分級 III 及 IV)手術期間的惡性組織顯影。**」 | [D[S68]] |
| 4b | **5-ALA 的健保給付** | **以成分名 5-aminolevulinic acid／aminolevulinic acid／aminolevulinic 查詢皆 0 筆。** 同上寫法 | [D[S63]] |
| 5 | **台灣癌症登記的腦瘤發生數** | **查到（A 組 gap 部分補上）**。台灣癌症登記中心長期趨勢資料檔（Year_Nervous_2023.xlsx）：**2023 年「腦癌」新發個案 742 人（男 410、女 332），粗發生率 3.18／10 萬，年齡標準化發生率 2.41／10 萬（男 2.81、女 2.01）**；2021 年 785 人、2022 年 742 人。另有「其他神經系統癌」2023 年 83 人。註明：僅含侵襲癌、以年中人口計算、年齡標準化採 2000 年世界標準人口。**資料檔中 2022 與 2023 兩列的個案數完全相同（742／410／332）而年齡標準化率不同，引用時建議只用 2023 年那一列並註明資料來源年度** | [D[S69]] |
| 5b | **GBM 佔腦瘤的比例** | **仍是 gap。** 癌症登記公開資料只到「腦癌」這一層，沒有組織型態別；衛福部 112 年癌症登記報告新聞稿只公布十大癌症（腦不在內）；`hpa.gov.tw`、`cris.hpa.gov.tw` 本日皆無法連線。**A1 的比例數字只能用 CBTRUS（美國），並標明是美國資料** | [D[S70]] |
| 6 | **認知復健／職能治療的給付項目** | **查到**。43026C 職能治療評估 240 點；45031C 一般職能治療 299 點；45095C 特殊職能治療 325 點（特殊項目含「知覺認知訓練」「執行功能訓練」）；**43031C 複雜職能治療 500 點，適應症的 ICD-10-CM 清單含 C71、C72，限住院期間與出院後六個月內，須含 OT 12 知覺認知訓練等項目中的兩項以上，限復健專科醫師開處方**。**全表中沒有名為「認知復健」的獨立支付項目**（檢索「認知功能」「認知治療」「神經心理」「心理衡鑑」皆 0 筆） | [D[S66]] |
| 7 | **regorafenib 可否用於 GBM（本次新增）** | **查到（重要陰性）**。健保第 9.51 條與食藥署仿單適應症皆只有 mCRC／GIST／HCC，**沒有膠質母細胞瘤** | [D[S65]][D[S68]] |
| 8 | **carmustine 植入劑（Gliadel）給付（本次新增）** | **查到**。第 9.35 條：限復發性 GBM 手術輔助、**不得與 temozolomide 併用**、須事前審查。現行品項 B0247772BG（起 102.10.01） | [D[S62]] |
| 9 | **lomustine（CCNU）健保身分（本次新增）** | **查到**。現行四個品項（B006293100／B006294100／B015116100／B015117100），**給付規定欄位為空** | [D[S63]] |
| 10 | **「電場」在支付標準全表** | **零筆**（以 2026-09-03 重新下載的全表覆核）。沿用站上〈貼片〉的結論，B5 一句指路 | [D[S66]] |
| 11 | **MRI／PET 的既有支付項目** | **查到**：33084B 磁振造影－無造影劑 6,500 點；33085B 有造影劑 11,500 點；26072B 正子造影－全身 36,500 點；26073B 局部 26,500 點。**短期內重複照同一部位的頻次限制條文仍查不到（gap）** | [D[S66]] |
| 12 | **心理治療項目（D2 相關）** | **查到**：45010C 支持性心理治療 97 點；45013C 深度心理治療（每四十分鐘）－成人 1,203 點；45087C 特殊心理治療－成人 344 點 | [D[S66]] |
| 13 | **癲癇與駕照法規原文（C 組項目，順手取得）** | **查到**。《道路交通安全規則》（**修正日期 民國 115 年 6 月 26 日**）第 64 條第一項第一款第六目之 1：「**癲癇。但檢具醫療院所醫師出具最近二年以上未發作診斷證明書者，不在此限。**」；第 52-3 條：符合上開但書者得申請機車或普通小型車駕照考驗，**駕照自發照日起每滿二年換發一次**，換發時須檢具最近三個月內由神經內科、神經外科或兒科（且曾參加神經相關專業訓練）醫師出具**最近二年內未癲癇發作**並加註專科醫師證照號碼之診斷證明書。**C 組應自行覆核後再用** | [D[S64]] |
| 14 | **再照射的支付項目** | **gap**（與 `sit-reirradiation` 的結論一致，本次重新覆核仍未檢出） | [D[S66]] |
| 15 | **bevacizumab 用於放射性壞死的給付** | **條文未列此適應症**；**不推論可否申請**，文章寫「問醫務課」 | [D[S61]] |
| 16 | **台灣的復發 GBM 治療指引／假性惡化判讀流程文件** | **gap**，未檢出可引用的官方文件 | — |

---

## 來源清單（PASS／FAIL 逐條，含查證路徑）

**共同路徑說明**：所有期刊條目均於 **2026-09-03** 以 Europe PMC REST
`https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=...&resultType=core&format=json` 逐筆抓取，
書目欄位（title／journal／year／volume(issue)／pages／DOI／PMID／isOpenAccess）與所引數字**全部出自本次抓到的 abstractText**；
標「全文核對」者另以 `https://www.ebi.ac.uk/europepmc/webservices/rest/<PMCID>/fullTextXML` 取得全文後逐句比對。
**未引用 NCCN。**

### PASS — 判讀標準與影像（D1）

- **[D[S1]] PASS** — Wen PY, Macdonald DR, Reardon DA, et al. *Updated response assessment criteria for high-grade gliomas:
  response assessment in neuro-oncology working group.* **J Clin Oncol 2010;28(11):1963–1972.** DOI 10.1200/JCO.2009.26.3541；
  PMID 20231676；OA=N。
  Route: Europe PMC `DOI:"10.1200/JCO.2009.26.3541"` → hitCount 1。摘要含「20% to 30%」、假性反應三句原文，逐字核對通過。
- **[D[S2]] PASS** — Wen PY, van den Bent M, Youssef G, et al. *RANO 2.0: Update to the Response Assessment in Neuro-Oncology
  Criteria for High- and Low-Grade Gliomas in Adults.* **J Clin Oncol 2023;41(33):5187–5199.** DOI 10.1200/JCO.23.01059；
  PMID 37774317；PMC10860967；OA=N（PMC 全文本次取回為空檔）。
  Route: Europe PMC `TITLE:"RANO 2.0: Update to the Response Assessment in Neuro-Oncology Criteria"`。
  「postradiotherapy MRI... as the baseline」「12 weeks after radiotherapy」「nonenhancing disease will no longer be evaluated」
  三句均在摘要中逐字核對通過。
- **[D[S3]] PASS（全文核對）** — Blakstad H, Mendoza Mireles EE, Heggebø LC, et al. *Incidence and outcome of pseudoprogression
  after radiation therapy in glioblastoma patients: A cohort study.* **Neuro-Oncol Pract 2024;11(1):36–45.**
  DOI 10.1093/nop/npad063；PMID 38222046；PMC10785573；**OA=Y**。
  Route: Europe PMC 檢索＋`PMC10785573/fullTextXML`。逐句核對通過的數字：
  53(19.4%)／113(41.4%)／104(38.1%)；6 個月 17(7.0%)、扣除重複後 3.8%；22(41.5%)／2(3.8%)／29(54.7%)；
  中位 OS 24.5 vs 11.4 vs 18.4（3 個月）與 31.8 vs 13.0 vs 23.7（6 個月）；
  改治療 17(15.0%)、改與不改 12.1 vs 11.8 個月 p=.838；假性惡化組 2(3.8%) 被改治療、二次手術病理只見反應性組織／壞死；
  再切除 16 人的病理分布與 15.3／7.6 個月；p<.001／p=.029／p=.045／p=.034。
- **[D[S4]] PASS** — Brandes AA, Franceschi E, Tosoni A, et al. *MGMT promoter methylation status can predict the incidence and
  outcome of pseudoprogression after concomitant radiochemotherapy in newly diagnosed glioblastoma patients.*
  **J Clin Oncol 2008;26(13):2192–2197.** DOI 10.1200/JCO.2007.14.8163；PMID 18445844；OA=N。
  Route: Europe PMC `AUTH:"Brandes AA" AND TITLE:"MGMT promoter methylation status can predict..."`。
  摘要核對通過：50/103 病灶變大、psPD 32／早期惡化 18、甲基化 21/23(91%) vs 未甲基化 11/27(41%) P=.0002、
  MGMT P=.001、psPD P=.045、第一次 MRI 在化放療結束後一個月。
- **[D[S5]] PASS（全文核對）** — Weller M, van den Bent M, Preusser M, et al. *EANO guidelines on the diagnosis and treatment of
  diffuse gliomas of adulthood.* **Nat Rev Clin Oncol 2021;18(3):170–186.** DOI 10.1038/s41571-020-00447-z；PMID 33293629；
  PMC7904519；**OA=Y**（另有 2022 年 Author Correction，PMID 35322237）。
  Route: Europe PMC 檢索＋ PMC7904519 全文。本 brief 引用的每一句（追蹤間隔 2–3／2–6 個月 common practice、4–8 週、
  假性惡化與假性反應「first 3 months but can also occur later」、切片不足以排除、再手術 20–30% 與六個月、
  再照射分次原則與 30–36 Gy／15–20 Gy、bevacizumab 的 main value 與 no OS benefit 與 EU 未核准、
  lomustine never shown superiority／6 個月 PFS ~20%、temozolomide 再挑戰限 MGMT 甲基化、Gliadel modest、
  nivolumab 與 TTFields 陰性、職能／語言／物理治療需求應被評估、決定能力的建議「remain to be developed」）
  皆已在全文中逐字定位。
- **[D[S6]] PASS** — van Dijken BRJ, van Laar PJ, Holtman GA, van der Hoorn A. *Diagnostic accuracy of magnetic resonance imaging
  techniques for treatment response evaluation in patients with high-grade glioma, a systematic review and meta-analysis.*
  **Eur Radiol 2017;27(10):4129–4144.** DOI 10.1007/s00330-017-4789-9；PMID 28332014；PMC5579204；**OA=Y**。
  Route: Europe PMC。摘要核對通過：anatomical 5 篇/166 人 68%(51–81)/77%(45–93)；ADC 7/204 71%(60–80)/87%(77–93)；
  DSC 18/708 87%(82–91)/86%(77–91)；DCE 5/207 92%(73–98)/85%(76–92)；MRS 9/203 91%(79–97)/**95%(65–99)**。
- **[D[S7]] PASS** — de Zwart PL, van Dijken BRJ, Holtman GA, et al. *Diagnostic Accuracy of PET Tracers for the Differentiation of
  Tumor Progression from Treatment-Related Changes in High-Grade Glioma: A Systematic Review and Metaanalysis.*
  **J Nucl Med 2020;61(4):498–504.** DOI 10.2967/jnumed.119.233809；PMID 31541032；OA=N。
  Route: Europe PMC。摘要核對通過：39 篇 11 種示蹤劑；FDG 12 篇/171 病灶 84%(72–92)/84%(69–93)；
  FET 7/172 90%(81–95)/85%(71–93)；MET 8/151 93%(80–98)/82%(68–91)；FDOPA 85–100%/72–100%；
  結論「**18F-FET and 11C-MET, both amino-acid tracers, showed a comparably higher sensitivity than 18F-FDG**」。
- **[D[S8]] PASS** — Galldiks N, Lohmann P, Aboian M, et al. *Update to the RANO working group and EANO recommendations for the
  clinical use of PET imaging in gliomas.* **Lancet Oncol 2025;26(8):e436–e447.** DOI 10.1016/S1470-2045(25)00193-7；
  PMID 40744043；OA=N。
  Route: Europe PMC `EXT_ID:40744043`。摘要逐字核對通過：「the **superiority of amino acid PET over glucose PET**」與
  「the **scarcity of class 1 evidence showing that incorporating PET imaging into clinical workflows improves patient outcomes**,
  highlighting priority areas for future clinical studies designed to address this gap」。初版為 2016 年（本更新自述）。
- **[D[S9]] PASS（全文核對）** — Galldiks N, Tonn JC, Preusser M, Albert NL. *Update to the RANO Working Group and EANO
  recommendations for the clinical use of PET imaging in gliomas.* **Neuro Oncol 2025;27(10):2492–2493.**
  DOI 10.1093/neuonc/noaf170；PMID 40717220；PMC12833539；**OA=Y**。
  Route: `PMC12833539/fullTextXML`。這是同一份更新的開放取用導讀，可供寫作者查證脈絡；**數字仍以 [D[S8]] 為準**。
- **[D[S10]] PASS** — INTERVAL-GB Collaborative, NANSIG, BNTRC. *Imaging timing after surgery for glioblastoma: an evaluation of
  practice in Great Britain and Ireland (INTERVAL-GB) — a multi-centre, cohort study.*
  **J Neurooncol 2024;169(3):517–529.** DOI 10.1007/s11060-024-04705-3；PMID 39105956；PMC11341661；**OA=Y**
  （另有 2025 年 Correction，PMID 39976898）。
  Route: Europe PMC `TITLE:"INTERVAL-GB"`。摘要核對通過：754 人／26 中心／10,100 人月；72 小時內 78.0%(407/522)、
  48 小時內 64.2%(335/522)；後續追蹤 MRI 中位 1 次(IQR 0–4)；NICE 遵從 52.8%(398/754)、EANO 24.9%(188/754)；
  NICE HR 0.56(0.46–0.66)；結論句「Regular surveillance follow-up... **is associated with** longer OS.
  **Prospective trials are needed**...」。
  **註**：EANO HR 0.54 與兩個 PFS HR（0.93 p=0.349／0.99 p=0.874）在 Europe PMC 回傳的摘要中被截斷；
  **寫作者引用 EANO HR 與 PFS 數字前，須自行開啟 PMC11341661 全文覆核**，或只引 NICE 的 HR 0.56 與「PFS 沒有差別」這個方向性描述。
- **[D[S11]] PASS** — Wo XW, Zhu HF, Xu N. *Dynamic susceptibility contrast perfusion in differentiation between recurrence and
  pseudoprogression in glioblastoma: a systematic review and meta-analysis.*
  **Quant Imaging Med Surg 2025;15(12):12336–12345.** DOI 10.21037/qims-2025-245；PMID 41367751；PMC12682496；**OA=Y**。
  Route: Europe PMC。摘要核對通過：13 篇 487 人（318 復發／178 假性惡化）；rCBV 敏感度 87%(0.82–0.91)、
  特異度 83%(0.75–0.89)、AUC 0.92(0.89–0.94)、I²=18.92%。
- **[D[S12]] PASS** — Gu X, He X, Wang H, et al. *Dynamic Susceptibility Contrast-Enhanced Perfusion-Weighted Imaging in
  Differentiation Between Recurrence and Pseudoprogression in High-Grade Glioma: A Meta-analysis.*
  **J Comput Assist Tomogr 2024;48(2):303–310.** DOI 10.1097/RCT.0000000000001543；PMID 37654056；OA=N。
  Route: Europe PMC `EXT_ID:37654056`。摘要核對通過：21 篇、879 人、888 病灶；CBV 於其中 20 篇報告，
  敏感度 86%(0.81–0.89)、特異度 83%(0.77–0.87)、AUC 0.91(0.88–0.93)。
- **[D[S13]] PASS** — Ellingson BM, Bendszus M, Boxerman J, et al. *Consensus recommendations for a standardized Brain Tumor
  Imaging Protocol in clinical trials.* **Neuro Oncol 2015;17(9):1188–1198.** DOI 10.1093/neuonc/nov095；PMID 26250565；
  PMC4588759；OA=N。
  Route: Europe PMC。摘要核對通過：最低序列組合（對比前後 3D T1、注射對比劑後的 2D T2、FLAIR、三方向擴散加權）。

### PASS — 認知與文件（D2）

- **[D[S20]] PASS** — Tucha O, Smely C, Preier M, Lange KW. *Cognitive deficits before treatment among patients with brain tumors.*
  **Neurosurgery 2000;47(2):324–333; discussion 333–334.** DOI 10.1097/00006123-200008000-00011；PMID 10942005；OA=N。
  Route: Europe PMC `TITLE:"Cognitive deficits before treatment among patients with brain tumors"`
  （**注意：常被引用的 DOI 10.1097/00006123-200002000-00015 是別篇文章，本次查證已排除**）。
  摘要核對通過：n=139、>90% 至少一面向受損、執行功能 78%、記憶與注意力 >60%、
  自述與測驗「only a weak relationship」、抗癲癇藥無影響。
- **[D[S21]] PASS** — Sekely A, Bernstein LJ, Campbell KL, et al. *Neurocognitive impairment, neurobehavioral symptoms, fatigue,
  sleep disturbance, and depressive symptoms in patients with newly diagnosed glioblastoma.*
  **Neuro-Oncol Pract 2023;10(1):89–96.** DOI 10.1093/nop/npac068；PMID 36659968；PMC9837779；OA=N。
  摘要核對通過：n=45、診斷後中位 4 週、76%(34/45)、記憶保留 53%／執行 51%／立即回想 42%／流暢 41%／注意力 24%、
  睡眠 70%／疲倦 57%／憂鬱 16%／神經行為 27%。
- **[D[S22]] PASS** — Moiyadi A, Jain K, Shetty P, et al. *Baseline neurocognitive dysfunction is ubiquitous in intrinsic brain tumors —
  results from a large Indian cohort of patients and analysis of factors associated with domain-specific dysfunction.*
  **World Neurosurg X 2023;19:100210.** DOI 10.1016/j.wnsx.2023.100210；PMID 37251242；PMC10209697；**OA=Y**。
  摘要核對通過：n=142、嚴重缺損 90%、70% 至少兩面向、年齡／教育／腫瘤體積、語言與顳葉。
- **[D[S23]] PASS** — Klein M, Heimans JJ, Aaronson NK, et al. *Effect of radiotherapy and other treatment-related factors on
  mid-term to long-term cognitive sequelae in low-grade gliomas: a comparative study.*
  **Lancet 2002;360(9343):1361–1368.** DOI 10.1016/S0140-6736(02)11398-5；PMID 12423981；OA=N。
  Route: Europe PMC 以完整標題檢索（**常見的 DOI …(02)11213-X 查無，正確者為 …(02)11398-5**）。
  摘要核對通過：n=195（104 人曾放療）＋100 血液疾病對照＋195 健康對照；「fraction doses exceeding 2 Gy」；
  抗癲癇藥與注意力／執行功能失能強烈相關；結論句「the tumour itself has the most deleterious effect」。
- **[D[S24]] PASS** — Douw L, Klein M, Fagel SS, et al. *Cognitive and radiological effects of radiotherapy in patients with low-grade
  glioma: long-term follow-up.* **Lancet Neurol 2009;8(9):810–818.** DOI 10.1016/S1474-4422(09)70204-2；PMID 19665931；OA=N。
  摘要核對通過：n=65、平均 12 年（6–28）、32(49%) 曾放療（3 人 >2 Gy）、注意力 −1.6 vs −0.1 p=0.003、
  執行 p=0.03、處理速度 p=0.05、17(53%) vs 4(27%)。
- **[D[S25]] PASS** — Brown PD, Gondi V, Pugh S, et al. *Hippocampal Avoidance During Whole-Brain Radiotherapy Plus Memantine
  for Patients With Brain Metastases: Phase III Trial NRG Oncology CC001.*
  **J Clin Oncol 2020;38(10):1019–1029.** DOI 10.1200/JCO.19.02767；PMID 32058845；PMC7106984；OA=N。
  摘要核對通過：n=518、校正 HR 0.74(0.58–0.95) P=.02、執行功能 4 個月 23.3% vs 40.4% P=.01、
  學習與記憶 6 個月 11.5% vs 24.7% P=.049 與 16.4% vs 33.3% P=.02、OS／顱內 PFS／毒性無差異、
  結論限定於腦轉移且海馬迴區無轉移者。
- **[D[S26]] PASS** — Brown PD, Pugh S, Laack NN, et al. *Memantine for the prevention of cognitive dysfunction in patients receiving
  whole-brain radiotherapy: a randomized, double-blind, placebo-controlled trial (RTOG 0614).*
  **Neuro Oncol 2013;15(10):1429–1437.** DOI 10.1093/neuonc/not114；PMID 23956241；PMC3779047；OA=N。
  摘要核對通過：554 收案／508 可評估、24 週延遲回想 P=.059（149 人可分析、檢定力 35%）、
  認知退化時間 HR 0.78(0.62–0.99) P=.01、24 週失敗率 53.8% vs 64.9%、執行 8 週 P=.008／16 週 P=.0041、
  處理速度 P=.0137、延遲再認 P=.0149。
- **[D[S27]] PASS** — Triebel KL, Martin RC, Nabors LB, Marson DC. *Medical decision-making capacity in patients with malignant
  glioma.* **Neurology 2009;73(24):2086–2092.** DOI 10.1212/WNL.0b013e3181c67bce；PMID 20018637；PMC2833103；OA=N。
  Route: Europe PMC 標題檢索（**常見 DOI …3181bd1153 查無，正確者為 …3181c67bce**）。
  摘要核對通過：26 位惡性膠質瘤 vs 22 位健康對照、**>50% 出現 marginally capable 或 incapable**、
  「Soon after diagnosis」、短期語文記憶為主要預測因子。
- **[D[S28]] PASS** — Martin RC, Gerstenecker A, Nabors LB, Marson DC, Triebel KL. *Impairment of medical decisional capacity in
  relation to Karnofsky Performance Status in adults with malignant brain tumor.*
  **Neuro-Oncol Pract 2015;2(1):13–19.** DOI 10.1093/nop/npu030；PMID 26034637；PMC4369704；OA=N。
  摘要核對通過：n=71（原發 26／轉移 45）、KPS 90–100 全項有能力 46%、KPS 70–80 為 23%、KPS 50–60 為 0%。
- **[D[S29]] PASS** — Jeung YS, Lee WT, Kim Y, et al. *Documented advance care planning elements and end-of-life care patterns in
  malignant glioma vs. major solid tumors: a single-center retrospective study.*
  **J Neurooncol 2025;176(2):142.** DOI 10.1007/s11060-025-05396-0；PMID 41460550；OA=N。
  摘要核對通過：韓國單中心 2018–2022、串接 National Health Insurance Service；惡性膠質瘤 229 vs 五大實體癌 4,283；
  ACP 記載 20.1% vs 58.0%（aOR 0.13，0.09–0.19）；本人決定 21.4% vs 67.1%（aOR 0.07，0.04–0.12）；
  急診 29.3% vs 48.7%；化療 29.7% vs 42.0%；安寧 62.0% vs 73.1%（aOR 0.57，0.43–0.77）；
  死於護理之家 20.5% vs 6.8%。
- **[D[S48]] PASS** — Gehring K, Sitskoorn MM, Gundy CM, et al. *Cognitive rehabilitation in patients with gliomas: a randomized,
  controlled trial.* **J Clin Oncol 2009;27(22):3712–3722.** DOI 10.1200/JCO.2008.20.5765；PMID 19470928；OA=N。
  摘要核對通過：n=140、荷蘭 11 家醫院、低惡性度與退行性膠質瘤且同時有主觀抱怨與客觀缺損、
  療程後只有主觀指標顯著、六個月後注意力與語文記憶客觀測驗顯著且心理疲倦較少。
- **[D[S49]] PASS** — Tariq R, Aziz HF, Paracha S, et al. *Cognitive Rehabilitation of Brain Tumor Survivors: A Systematic Review.*
  **Brain Tumor Res Treat 2025;13(1):1–16.** DOI 10.14791/btrt.2024.0033；PMID 39924711；PMC11813561；**OA=Y**。
  摘要核對通過：15 篇；神經心理師指導訓練有效、年輕與教育程度高者獲益最大；整體性記憶術與神經回饋無效；
  有氧運動、瑜伽、合併訓練有效；主動式電玩對認知無效；「**a standardized CR program cannot be established at present**」。
- **[D[S50]] PASS（受限）** — Thippu Jayaprakash K, Wildschut K, Jena R. *Feasibility of Hippocampal Avoidance Radiotherapy for
  Glioblastoma.* **Clin Oncol (R Coll Radiol) 2017;29(11):748–752.** DOI 10.1016/j.clon.2017.06.010；PMID 28693823；OA=N。
  Route: Europe PMC `EXT_ID:28693823`。**Europe PMC 回傳的摘要只有目的段（retrospective planning study），沒有任何數值結果。**
  → **可引用的只有「這是一份回溯性計畫研究、目的是量化海馬迴劑量並評估減量可行性」這件事，
    不可引用任何劑量或比例數字。**
- **[D[S51]] PASS** — Terziev R, Psimaras D, Marie Y, et al. *Cumulative incidence and risk factors for radiation induced
  leukoencephalopathy in high grade glioma long term survivors.*
  **Sci Rep 2021;11(1):10176.** DOI 10.1038/s41598-021-89216-1；PMID 33986314；PMC8119685；**OA=Y**。
  摘要核對通過：n=81（18 grade IV／63 grade III）、無惡化存活 >30 個月、放療後中位追蹤 79 個月；
  44/81(54.3%)；症狀：皮質下失智 28／步態 12／尿失禁 9；累積發生率 12 個月 21%、36 個月 42%、60 個月 48%；
  危險因子 >60 歲、吸菸、rs2120825。
- **[D[S52]] PASS** — Drijver AJ, Butterbrod E, Hertler C, et al. *Neurocognitive functioning in long-term survivors of glioblastoma,
  IDH-wildtype and astrocytoma, IDH-mutant, CNS WHO grade 4: A report from EORTC 1419 (ETERNITY).*
  **Eur J Cancer 2026;246:116985.** DOI 10.1016/j.ejca.2026.116985；PMID 42607618；OA=N。
  摘要核對通過：基線平均診斷後 9 年（5–21）、145/185(78%) 至少一項受損、17.4%（HVLT-R 延遲再認）–58.7%（TMT B）、
  縱貫穩定、左側與顳葉較差、額葉與較高的心理動作速度與認知彈性相關。
- **[D[S53]] PASS** — Spoor JKH, Donders-Kamphuis M, Veenstra WS, et al. *Cognition and health-related quality of life in long-term
  survivors of high-grade glioma: an interactive perspective from patient and caregiver.*
  **Acta Neurochir (Wien) 2024;166(1):166.** DOI 10.1007/s00701-024-06037-7；PMID 38565800；PMC10987343；**OA=Y**。
  摘要核對通過：21 位存活 ≥5 年（8 grade III／13 grade IV）＋15 位照顧者；平均存活 12 年／8 年；
  認知顯著受損但個別差異大；整體 HRQoL 未受損但所有功能量表偏離；多數次量表病人與代理人一致；
  3 人（14%）有焦慮或憂鬱指標；**三分之一照顧者高負荷或高負擔**；**照顧者負擔與認知缺損無相關**。
- **[D[S54]] PASS** — Caramanna I, Klein M, van den Bent M, et al. *Neurocognitive impairment and patient-proxy agreement on
  health-related quality of life evaluations in recurrent high-grade glioma patients.*
  **Qual Life Res 2025;34(8):2405–2418.** DOI 10.1007/s11136-025-03984-1；PMID 40471413；PMC12274216；**OA=Y**。
  摘要核對通過：EORTC 26101／26091、**500 對配對**、Lin's CCC 全體 0.399–0.743、受損者 0.231–0.811、
  完好者 0.376–0.732、**只有 18.8% 神經認知完好**。**這是撤稿後的更正版，只可引這一版。**
- **[D[S55]] PASS（撤稿聲明，供警示用）** — Caramanna I, Klein M, van den Bent M, et al.
  *Retraction Note: Neurocognitive impairment and patient-proxy agreement on health-related quality of life evaluations in
  recurrent high-grade glioma patients.* **Qual Life Res 2024;33(8):2297.** DOI 10.1007/s11136-024-03696-y；PMID 38819763；
  PMC11286618；**OA=Y**。
  Route: `PMC11286618/fullTextXML`。全文逐字核對通過：撤稿的是 Qual Life Res 2022;31:3253–3266，
  原因為「an **honest error** occurred while exporting data from the original EORTC dataset ... **significantly affecting the results
  and conclusions**」，作者請求撤稿並將提交更正稿。**原 2022 年版一律不得引用。**
- **[D[S56]] PASS** — van der Meer PB, Koekkoek JAF, van den Bent MJ, Dirven L, Taphoorn MJB.
  *Effect of antiepileptic drugs in glioma patients on self-reported depression, anxiety, and cognitive complaints.*
  **J Neurooncol 2021;153(1):89–98.** DOI 10.1007/s11060-021-03747-1；PMID 33822293；PMC8131297；**OA=Y**。
  摘要核對通過：n=272；憂鬱 10% vs 21%（uOR 2.29，1.05–4.97，p=0.037；aOR 1.94，0.83–4.50，p=0.125）；
  焦慮 19% vs 26%（aOR 1.17，p=0.659）；主觀認知障礙 16% vs 21%（aOR 0.83，0.34–2.04，p=0.684）。
- **[D[S57]] PASS** — Chen H, Zou T, Teng Z, et al. *A systematic review and meta-analysis of psychological burden in family
  caregivers of patients with brain tumors.* **Sci Rep 2025;15(1):39694.** DOI 10.1038/s41598-025-23331-1；PMID 41224961；
  PMC12612171；**OA=Y**。
  摘要核對通過：15 篇、974 位家庭照顧者、文獻搜尋至 2022 年 2 月；憂鬱 37.15%(22.00–52.30)、
  焦慮 49.47%(35.81–63.12)、distress 64%(54–74)。
- **[D[S58]] PASS** — Suh KJ, Jung EH, Seo J, et al. *Current status of advance care planning, palliative care consultation, and
  end-of-life care in patients with glioblastoma in South Korea.*
  **Oncologist 2024;29(11):e1586–e1592.** DOI 10.1093/oncolo/oyae159；PMID 38940449；PMC11546624；**OA=Y**。
  摘要核對通過：205 人（2017–2022）、159 人死亡、中位 OS 20.3 個月；AD 11(6.9%)、LST 計畫 63(39.6%)、
  兩者皆無 85(53.5%)；63 人中本人完成 10(15.9%)／家屬 53(84.1%)；安寧照會 102(64.2%)、中位 44 天；
  侵略性末期照護 78(49.1%)；結論「nearly 90% not self-completing AD or LST plan」。
- **[D[S67]] PASS** — Sannes TS, Yusufov M, Amonoo HL, et al. *Proxy ratings of psychological well-being in patients with primary
  brain tumors: A systematic review.* **Psychooncology 2023;32(2):203–213.** DOI 10.1002/pon.6063；PMID 36371618；
  PMC10373343；OA=N。摘要核對通過：6 篇、結果分歧、憂鬱的代理人評分比焦慮準、「should be interpreted with caution」。
- **[D[S71]] PASS** — Noll KR, Bradshaw ME, Weinberg JS, Wefel JS. *Neurocognitive functioning is associated with functional
  independence in newly diagnosed patients with temporal lobe glioma.*
  **Neuro-Oncol Pract 2018;5(3):184–193.** DOI 10.1093/nop/npx028；PMID 30094046；PMC6075221；OA=N。
  摘要核對通過：左側 n=73（49% GBM）／右側 n=30（57% GBM）；語文學習、執行功能、語言理解共同解釋 FIM 40% 變異。
- **[D[S72]] PASS（族群不同，僅供警示）** — Haller OC, Tighe EL, King TZ. *Concordance of informant and self-reported ratings on
  the Frontal Systems Behavior Scale in adult survivors of pediatric brain tumor.*
  **Clin Neuropsychol 2024;38(1):135–149.** DOI 10.1080/13854046.2023.2192417；PMID 36987932；OA=N。
  摘要核對通過：73 對成年（兒童腦瘤）存活者與知情者；ICC 冷漠 .583／去抑制 .420／執行功能失調 .373；
  只有去抑制與評分者角色相關。**族群是兒童腦瘤的成年存活者，不可當成人 GBM 資料使用。**

### PASS — 復發（D3）

- **[D[S30]] PASS** — Taal W, Oosterkamp HM, Walenkamp AM, et al. *Single-agent bevacizumab or lomustine versus a combination
  of bevacizumab plus lomustine in patients with recurrent glioblastoma (BELOB trial): a randomised controlled phase 2 trial.*
  **Lancet Oncol 2014;15(9):943–953.** DOI 10.1016/S1470-2045(14)70314-6；PMID 25035291；OA=N。
  摘要核對通過：n=153（可分析 50／46／44）；9 個月存活率 43%(29–57)／38%(25–51)／59%(43–72)／
  110 mg/m² 組 87%(39–98)／合併 63%(49–75)；安全性分析後 lomustine 由 110 降為 90 mg/m²；
  結論「the results in the bevacizumab alone group **do not justify further studies**」。
- **[D[S31]] PASS** — Tsien CI, Pugh SL, Dicker AP, et al. *NRG Oncology/RTOG1205: A Randomized Phase II Trial of Concurrent
  Bevacizumab and Reirradiation Versus Bevacizumab Alone as Treatment for Recurrent Glioblastoma.*
  **J Clin Oncol 2023;41(6):1285–1295.** DOI 10.1200/JCO.22.00164；PMID 36260832；PMC9940937；OA=N。
  Route: Europe PMC `AUTH:"Tsien CI"`（**SPEC／常見引用的 DOI 10.1200/JCO.22.01542 指向另一篇文章，本次已排除**）。
  摘要核對通過：35 Gy／10 次、bevacizumab 10 mg/kg q2w；隨機 182、合格 170；
  OS HR 0.98（80%CI 0.79–1.23）P=.46、中位 10.1 vs 9.7 個月；PFS 7.1 vs 3.8 個月 HR 0.73(0.53–1.0) P=.05；
  6 個月 PFS 29.1%(19.1–39.1)→54.3%(43.5–65.1) P=.001；急性 3 級以上 5%、無延遲高等級不良事件；
  收案條件「≥ 6 months from completion of prior chemo-RT」。
- **[D[S32]] PASS** — Chinot OL, Wick W, Mason W, et al. *Bevacizumab plus radiotherapy-temozolomide for newly diagnosed
  glioblastoma (AVAglio).* **N Engl J Med 2014;370(8):709–722.** DOI 10.1056/NEJMoa1308345；PMID 24552318；OA=N。
  摘要核對通過：458 vs 463；PFS 10.6 vs 6.2 個月、分層 HR 0.64(0.55–0.74)；
  「did not improve survival」；生活品質與體能狀態維持；不良事件較高。
- **[D[S33]] PASS** — Gilbert MR, Dignam JJ, Armstrong TS, et al. *A randomized trial of bevacizumab for newly diagnosed
  glioblastoma (RTOG 0825).* **N Engl J Med 2014;370(8):699–708.** DOI 10.1056/NEJMoa1308573；PMID 24552317；
  PMC4201043；OA=N。
  摘要核對通過：978 登錄／637 隨機；OS 15.7 vs 16.1 個月、HR 1.13；PFS 10.7 vs 7.3 個月、HR 0.79（未達預設目標）；
  「increased symptom burden, a worse quality of life, and a decline in neurocognitive function were more frequent in the
  bevacizumab group」。
- **[D[S34]] PASS** — Lombardi G, De Salvo GL, Brandes AA, et al. *Regorafenib compared with lomustine in patients with relapsed
  glioblastoma (REGOMA): a multicentre, open-label, randomised, controlled, phase 2 trial.*
  **Lancet Oncol 2019;20(1):110–119.** DOI 10.1016/S1470-2045(18)30675-2；PMID 30522967；OA=N。
  摘要核對通過：n=119（59／60）、10 中心、中位追蹤 15.4 個月、99/119(83%) 死亡；
  OS 7.4(5.8–12.0) vs 5.6(4.7–7.3) 個月、HR 0.50(0.33–0.75)、p=0.0009；3–4 級 33(56%) vs 24(40%)；
  作者自陳需 adequately powered phase 3。
- **[D[S35]] PASS** — Wen PY, Berry DA, Buxton MB, et al. *Evaluation of Regorafenib in Newly Diagnosed and Recurrent
  Glioblastoma: GBM AGILE Phase II/III Bayesian Randomized Platform Trial.*
  **J Clin Oncol 2026;44(18):1676–1686.** DOI 10.1200/JCO-25-01137；PMID 41980234；OA=N。
  （另有 Erratum，PMID 42096661。）
  摘要核對通過：NCT03970447；族群 NDU 與 RD；對照臂為 temozolomide＋放療或 lomustine；
  結論原文「did not show superiority of regorafenib over control... yet caused increased toxicities」。
  **註：摘要的 Results 段在 Europe PMC 被截斷，未取得 HR 數值；本 brief 只引用結論段的定性敘述，
  寫作者不得補上任何 HR 或存活數字。**
- **[D[S36]] PASS（社論，供一句話總結用）** — *Gods do play dice: The activity of regorafenib in glioblastoma not confirmed.*
  **Neuro Oncol 2026**（PMID 42124532；OA=N）。Route: Europe PMC `EXT_ID:42124532`。
  **只用標題，不引其內文（本次未取得全文）。**
- **[D[S37]] PASS** — Levin VA, Bidaut L, Hou P, et al. *Randomized double-blind placebo-controlled trial of bevacizumab therapy for
  radiation necrosis of the central nervous system.* **Int J Radiat Oncol Biol Phys 2011;79(5):1487–1495.**
  DOI 10.1016/j.ijrobp.2009.12.061；PMID 20399573；PMC2908725；OA=N。
  摘要核對通過：**n=14**；收案的原疾病為「head-and-neck carcinoma, meningioma, or **low- to mid-grade glioma**」；
  安慰劑 0/7、bevacizumab 5/5 隨機與 7/7 交叉均有影像反應且神經症狀改善；作者自稱 Class I evidence。
- **[D[S38]] PASS** — Zhao YH, Wang ZF, Pan ZY, et al. *A Meta-Analysis of Survival Outcomes Following Reoperation in Recurrent
  Glioblastoma: Time to Consider the Timing of Reoperation.* **Front Neurol 2019;10:286.** DOI 10.3389/fneur.2019.00286；
  PMID 30984099；PMC6448034；**OA=Y**。
  摘要核對通過：21 篇、8,630 人；固定共變數 OS HR 0.66(0.61–0.71)、PPS HR 0.70(0.57–0.88)；
  時間相依共變數 OS **HR 2.19(1.47–3.27)**、PPS p=0.51；結論「may be overestimated when analyzed as fixed covariates」。
- **[D[S39]] PASS** — Wick W, Gorlia T, Bendszus M, et al. *Lomustine and Bevacizumab in Progressive Glioblastoma (EORTC 26101).*
  **N Engl J Med 2017;377(20):1954–1963.** DOI 10.1056/NEJMoa1707358；PMID 29141164；OA=N。
  摘要核對通過：2:1 隨機（288／149）、共 437 人、329 次死亡事件(75.3%)；
  OS 9.1(8.1–10.1) vs 8.6(7.6–10.4) 個月、HR 0.95(0.74–1.21)、**P=0.65**；
  PFS 4.2 vs 1.5 個月、HR 0.49(0.39–0.61)、P<0.001；3–5 級 63.6% vs 38.1%；
  「affected neither health-related quality of life nor neurocognitive function」；MGMT 具預後意義；NCT01290939。
- **[D[S40]] PASS** — Friedman HS, Prados MD, Wen PY, et al. *Bevacizumab alone and in combination with irinotecan in recurrent
  glioblastoma (BRAIN).* **J Clin Oncol 2009;27(28):4733–4740.** DOI 10.1200/JCO.2008.19.8721；PMID 19720927；OA=N。
  摘要核對通過：n=167；6 個月 PFS 42.6%／50.3%；反應率 28.2%／37.8%；中位 OS 9.2／8.7 個月；
  「**There was a trend** for patients who were taking corticosteroids at baseline to take stable or decreasing doses over time.」；
  3 級以上不良事件 46.4%／65.8%；顱內出血 2.4%／3.8%。
- **[D[S41]] PASS** — Pichardo-Rojas PS, Garcia-Torrico F, Espinosa-Cantú CB, et al. *Current trends in reoperation for recurrent
  glioblastoma: a meta-analysis (2007–2023).* **J Neurooncol 2025;174(2):271–301.** DOI 10.1007/s11060-025-05058-1；
  PMID 40314867；OA=N。
  摘要核對通過：36 篇、10,738 人、2,806 人再手術、9 篇傾向分數配對＋1 個臨床試驗；
  平均 OS 19.66 vs 12.56 個月；多變項 OS HR 0.62(0.50–0.76)；CRET 之 PRS HR 0.54(0.39–0.73) p=0.04；
  結論「The role of reoperation in rGBM **remains uncertain**」。
- **[D[S42]] PASS** — Golla H, Nettekoven C, Hellmich M, et al. *Early palliative care for patients with glioblastoma: A randomized
  phase III clinical trial (EPCOG).* **Neuro Oncol 2026;28(1):226–240.** DOI 10.1093/neuonc/noaf230；PMID 41071052；
  PMC12962646；**OA=Y**。
  摘要核對通過：六家德國大學醫學中心、診斷後四週內收案、介入 12 個月、評估者盲性；介入 109／對照 108；
  六個月生活品質平均差 4.1（95%CI −4.4 到 12.6）**P=.34**；存活差異（對照較長）**P=.018**；
  校正後 P=.041；緩和照護問題與情緒獲益；**照顧者未獲益**；
  結論「improves '**how to live**' but **not 'length of life**'」。
- **[D[S43]] PASS** — Pace A, Dirven L, Koekkoek JAF, et al. *European Association for Neuro-Oncology (EANO) guidelines for
  palliative care in adults with glioma.* **Lancet Oncol 2017;18(6):e330–e340.** DOI 10.1016/S1470-2045(17)30345-5；
  PMID 28593859；OA=N。摘要核對通過：「necessitate an appropriate and **early palliative care approach**」；
  缺乏證據的領域包含疲倦、行為與情緒障礙、照顧者需求、**預立醫療照護諮商的時機**。
- **[D[S44]] PASS** — Koekkoek JAF, van der Meer PB, Pace A, et al. *Palliative care and end-of-life care in adults with malignant
  brain tumors.* **Neuro Oncol 2023;25(3):447–456.** DOI 10.1093/neuonc/noac216；PMID 36271873；PMC10013651；OA=N。
  （另有 Corrigendum，PMID 36610983。）
  摘要核對通過：2016–2021、140 篇；「Early palliative care interventions are essential...」；
  「**No pharmacological agents have been shown in randomized controlled trials to significantly improve fatigue or
  neurocognition.**」；levetiracetam 優於 valproic acid 作為第一線單藥（**此句屬 C3，D 組不使用**）。
- **[D[S45]] PASS** — Sizoo EM, Pasman HR, Dirven L, et al. *The end-of-life phase of high-grade glioma patients: a systematic
  review.* **Support Care Cancer 2014;22(3):847–857.** DOI 10.1007/s00520-013-2088-9；PMID 24337718；OA=N。
  摘要核對通過：695 篇篩出 17 篇、幾乎全為觀察性（僅 2 個非隨機介入研究）；
  「**Cognitive deficits increase as the disease progresses, hampering communication and decision making.**」；
  緩和照護服務使用較其他癌症病人密集。
- **[D[S46]] PASS** — Koekkoek JA, Dirven L, Reijneveld JC, et al. *End of life care in high-grade glioma patients in three European
  countries: a comparative study.* **J Neurooncol 2014;120(2):303–310.** DOI 10.1007/s11060-014-1548-5；PMID 25038849；OA=N。
  摘要核對通過：207 份家屬問卷（荷 83／奧 72／英 52）；死亡前三個月 75% 在家；
  預立指示 荷 46%／英 36%／奧 6%（p<0.001）；**53% 被認為得到良好照護品質**。
- **[D[S47]] PASS（可用、本 brief 未引用）** — Walbert T, Pace A. *End-of-life care in patients with primary malignant brain tumors:
  early is better.* **Neuro Oncol 2016;18(1):7–8.** DOI 10.1093/neuonc/nov241；PMID 26423092；PMC4677419；OA=N。
  Route: Europe PMC `EXT_ID:26423092`。**這是一篇編者評論，Europe PMC 無摘要內容**；
  → **只能引標題與其為 editorial 的事實，不可引任何內容。建議不用。**
- **[D[S73]] PASS** — Stupp R, Wong ET, Kanner AA, et al. *NovoTTF-100A versus physician's choice chemotherapy in recurrent
  glioblastoma: a randomised phase III trial of a novel treatment modality (EF-11).*
  **Eur J Cancer 2012;48(14):2192–2202.** DOI 10.1016/j.ejca.2012.04.011；PMID 22608262；OA=N。
  摘要核對通過：n=237（TTFields 120／對照 117）、每天 20–24 小時；
  中位存活 6.6 vs 6.0 個月、HR 0.86(0.66–1.12)、p=0.27；一年存活率 20% vs 20%；
  6 個月 PFS 21.4% vs 15.1%（p=0.13）；反應率 14% vs 9.6%（p=0.19）；
  嚴重不良事件 6% vs 16%（p=0.022）；TTFields 相關不良事件為輕度(14%)至中度(2%)的皮膚疹。

### PASS — 台灣官方文件

- **[D[S60]] PASS** — 衛生福利部中央健康保險署。**全民健康保險藥品給付規定 第 9.25 條 Temozolomide（如 Temodal）**
  （條文標註日期 94/3/1、97/1/1、98/9/1；附表八之二）。檔名 `9.25._20090901_000.pdf`。
  Route: `POST https://info.nhi.gov.tw/api/INAE3000/INAE3000S01/SQL0001`（DRUG_ING=temozolomide）取得規定碼 9.25.
  與檔名，再 `GET .../getPDF?DurgFileName=9.25._20090901_000.pdf&appType=true` 下載 PDF、`pdftotext -layout` 全文，
  2026-09-03 重新抓取並逐字核對。
- **[D[S61]] PASS** — 同署。**藥品給付規定 第 9.37 條 Bevacizumab（如 Avastin）**
  （條文標註日期含 100/6/1 … 114/10/1）。檔名 `9.37._20251001.pdf`。第 2 項為「惡性神經膠質瘤(WHO 第4級)-神經膠母細胞瘤」。
  Route 同上（DRUG_ING=bevacizumab），2026-09-03 重新抓取並逐字核對。現行連結此規定的品項共 12 筆（含多家生物相似藥）。
- **[D[S62]] PASS** — 同署。**藥品給付規定 第 9.35 條 carmustine 植入劑（如 Gliadel Wafer）**（100/2/1；附表八之四）。
  檔名 `9.35._20110201_000.pdf`。Route 同上（DRUG_ING=carmustine）。
- **[D[S63]] PASS（查詢結果，非條文）** — 同署。**藥品給付項目查詢結果**（2026-09-03）：
  DRUG_ING=lomustine → total 16 筆，現行 4 筆（B006293100、B006294100、B015116100、B015117100），給付規定欄位皆空；
  DRUG_ING=vorasidenib → **total 0**；DRUG_ING=5-aminolevulinic acid／aminolevulinic acid／aminolevulinic → **total 0**。
  Route 同上。**注意：本 API 僅 `DRUG_ING` 參數有效；以品名查詢會回傳全庫。**
  **本條只證明「以成分名查詢的結果為 0 筆」，不得據以宣稱有無給付。**
- **[D[S64]] PASS** — 全國法規資料庫。**《道路交通安全規則》**（修正日期 民國 115 年 6 月 26 日），
  第 64 條第一項第一款第六目之 1、第 52-3 條。
  Route: `curl https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=K0040013`，2026-09-03 取得全文並逐字核對。
  **屬 C 組項目，C 組應自行覆核。**
- **[D[S65]] PASS** — 中央健康保險署。**藥品給付規定 第 9.51 條 Regorafenib（如 Stivarga）**
  （104/9/1、105/8/1、107/12/1、108/6/1、110/5/1、110/6/1、113/6/1）。檔名 `9.51._20240601.pdf`。
  適應症僅列 mCRC、GIST、HCC。Route 同 [D[S60]]（DRUG_ING=regorafenib）。
- **[D[S66]] PASS** — 中央健康保險署。**全民健康保險醫療服務給付項目及支付標準（現行給付項目全表，TXT）**。
  Route: 政府資料開放平臺 dataset 174451（`https://data.gov.tw/api/v2/rest/dataset/174451`）取得下載連結
  `https://info.nhi.gov.tw/api/iode0000s01/Dataset?rId=A21030000I-D20020-002`，
  2026-09-03 重新下載（22,040,780 bytes、UTF-8 BOM、6,186 筆）並全文檢索。
  本 brief 引用的代碼：43026C(240)、45031C(299)、45095C(325)、43031C(500，適應症含 C71／C72)、
  33084B(6,500)、33085B(11,500)、26072B(36,500)、26073B(26,500)、45010C(97)、45013C(1,203)、45087C(344)。
  檢索為 0 筆者：「電場」「認知功能」「認知治療」「神經心理」「心理衡鑑」「再照射」。
- **[D[S68]] PASS** — 衛生福利部食品藥物管理署。**【9123】未註銷藥品許可證資料集**（每週與藥證業務管理系統同步）。
  Route: `GET https://data.fda.gov.tw/data/opendata/export/37/csv`（回傳 ZIP，內含 `37_2.csv`，UTF-8 BOM，26,027 筆），
  2026-09-03 下載並以許可證字號逐筆核對。本 brief 引用的四筆：
  ① 瓦拉固膜衣錠 10 毫克／VORANIGO film-coated tablets 10 mg，**衛部藥輸字第 029063 號**，發證 2025/12/23、有效 2030/12/23；
  ② 瓦拉固膜衣錠 40 毫克，**衛部藥輸字第 029064 號**，同日期；
  ③ 格麗藍口服溶液用粉劑／Gliolan Powder for Oral Solution，**衛署藥輸字第 025524 號**，發證 2012/04/20、有效 2027/04/20；
  ④ 癌瑞格膜衣錠 40 毫克／Stivarga，**衛部藥輸字第 026168 號**，適應症僅 mCRC／GIST／HCC。
  （temozolomide 亦有 30 筆現行許可證，適應症含新診斷 GBM 同步＋輔助與復發惡性膠質瘤。）
- **[D[S69]] PASS** — 台灣癌症登記中心（twcr.tw）。**長期趨勢資料檔 `Year_Nervous_2023.xlsx`**
  （工作表 191_YEAR_data「腦癌」、192_YEAR_data「其他神經系統癌」，1980–2023）。
  Route: `https://twcr.tw/?page_id=1657` 取得檔案清單 →
  `https://twcr.tw/wp-content/uploads/2026/01/Year_Nervous_2023.xlsx`，2026-09-03 重新下載（MD5 與先前一致）。
  引用值：2023 年腦癌 742 人（男 410／女 332）、粗發生率 3.18、年齡標準化 2.41（男 2.81／女 2.01）；
  2021 年 785 人、2022 年 742 人；其他神經系統癌 2023 年 83 人。
  檔內註記：僅含侵襲癌、採年中人口數、年齡標準化採 2000 年世界標準人口。
  **已知瑕疵：2022 與 2023 兩列的個案數完全相同，引用時請只用單一年度並註明。**
- **[D[S70]] PASS** — 衛生福利部。**〈公布 112 年國人癌症登記資料分析結果 守護健康未來 從癌症篩檢開始〉**
  （建檔日期 114-12-30、更新 115-01-05，資料來源：國民健康署）。
  Route: `curl https://www.mohw.gov.tw/cp-7171-84987-1.html`，2026-09-03 取得全文。
  內容：112 年新發生癌症 138,051 人、全癌症標準化發生率每 10 萬人口 331.3、發生年齡中位數 65 歲；
  十大癌症名單中**沒有腦（中樞神經系統）**。**本條只用來證明「官方十大癌症統計不含腦瘤」。**

### FAIL／NOT-CITABLE（保留，讓寫作者知道查過什麼）

- **FAIL-D1** — `info.fda.gov.tw`（食藥署西藥許可證查詢／`https://info.fda.gov.tw/mlms/H0001.aspx`）：
  **2026-09-03 連線失敗（HTTP 000，DNS／TLS 層即失敗）**，與 A 組所遇一致。
  → **已由 [D[S68]] 的 TFDA 開放資料 API 取代，vorasidenib 與 5-ALA 的藥證資料因此取得。**
- **FAIL-D2** — `www.hpa.gov.tw`（國民健康署）：**2026-09-03 TLS 連線失敗**。
  連 `data.gov.tw` 資料集 6399「癌症發生統計」所指向的下載連結
  （`https://www.hpa.gov.tw/Pages/ashx/GetFile.ashx?lang=c&type=1&sid=9e08758933474930a69e2946e17d63ea`）
  也因同一原因失敗。→ 以 `twcr.tw`[D[S69]] 與 `www.mohw.gov.tw`[D[S70]] 取代。
- **FAIL-D3** — `cris.hpa.gov.tw`（癌症登記線上互動查詢系統）：**2026-09-03 連線失敗（HTTP 000）**。
  → **這是「GBM 佔台灣腦瘤多少比例」仍然是 gap 的直接原因**：公開資料只到「腦癌」這一層，沒有組織型態別。
- **FAIL-D4** — `data.nhi.gov.tw`（健保署資料開放服務）：**2026-09-03 連線失敗（HTTP 000）**。
  → 以政府資料開放平臺 `data.gov.tw` ＋ `info.nhi.gov.tw` API 取代[D[S66]]。
- **NOT-CITABLE-D5** — **Caramanna 2022（Qual Life Res 2022;31:3253–3266）已撤稿**，
  撤稿聲明見 [D[S55]]。**任何情況下不得引用**；改引 2025 年更正版 [D[S54]]。
- **NOT-CITABLE-D6** — **類固醇對膠質瘤病人認知的影響**：以 Europe PMC 檢索
  `(TITLE:"corticosteroid" OR TITLE:"dexamethasone") AND TITLE:"cognitive"`（56 筆）
  逐筆檢視，**全部為非腦瘤族群**（氣喘、冠狀動脈繞道術後、早產兒、動物模型等）。
  → **膠質瘤族群無可引用的原始研究，D2 必須寫成 gap。**
- **NOT-CITABLE-D7** — **癲癇發作本身對 GBM 病人認知的獨立貢獻**：未檢出可引用的原始研究。**gap。**
- **NOT-CITABLE-D8** — **成人膠質瘤的 anosognosia／病覺缺失**：以
  `("self-awareness" OR "anosognosia" OR "impaired awareness") AND (glioma OR "brain tumour" OR "brain tumor")`
  等多組檢索（1,032 筆、32 筆等），**未檢出以成人膠質瘤為族群的原始研究**；
  最接近者為兒童腦瘤成年存活者的 FrSBe 一致性研究[D[S72]]。→ **D2 不得使用此診斷名詞。**
- **NOT-CITABLE-D9** — **額葉病灶與人格／行為改變的量化研究（成人膠質瘤）**：
  以 `TITLE:"frontal" AND (glioma OR tumour OR tumor) AND (behaviour OR behavior OR apathy OR personality OR executive)`
  檢索（10 筆），命中的是影像連結性、術中監測、單一病例報告，**沒有可引用的族群層次量化資料**。**gap。**
- **NOT-CITABLE-D10** — **GBM 的海馬迴劑量數值**：[D[S50]] 在 Europe PMC 只有目的段、無數值結果，
  且該文非開放取用、本次未取得全文。→ **brief 不提供任何海馬迴劑量數字。**
- **NOT-CITABLE-D11** — **GBM AGILE 的 HR 與存活數值**：[D[S35]] 摘要 Results 段在 Europe PMC 被截斷，
  本次未取得完整數值。→ **只可引用結論段的定性敘述。**
- **NOT-CITABLE-D12** — **INTERVAL-GB 的 EANO HR 與兩個 PFS HR**：摘要被截斷（見 [D[S10]] 註）。
  → 寫作者若要用，須自行開啟 PMC11341661 全文覆核。
- **NOT-CITABLE-D13** — **台灣的復發 GBM 治療指引、假性惡化判讀流程文件、再照射支付項目、
  短期內重複影像的頻次限制條文**：本次以支付標準全表全文檢索與一般網路檢索均未檢出可引用的官方文件。**全部為 gap。**
- **NOT-CITABLE-D14** — **NCCN**：依 RESEARCH-COMMON.md 規定不引用，本 brief 未抓取、未引用。
  D3 中出現的「已從某指引移除」一句，是 [D[S35]] 試驗結論的**整句引述**，非對該指引的引用或轉述。

### 站上既有頁面（本次逐字讀過，用於措辭對齊，非文獻來源）

- `/home/claude/repo/sit-pseudo.html`〈影像變壞，不一定是病變壞〉——D1 的措辭母版（見 D1 首節對照表）。
- `/home/claude/repo/sit-decide-for.html`〈他不能決定的時候，誰決定〉——四件事：醫療委任代理人（病主法第 3 條第 5 款、第 10 條）、
  預立醫療決定（第 8、9、14、15 條）、家屬同意順位（**只在安寧緩和醫療條例第 7 條、只管末期病人的維生醫療**）、
  決定能力（臨床在醫師、法律在法院）。**D2 只指路，不重寫。**
- `/home/claude/repo/sit-documents.html`〈三份文件，不是同一件事〉——安寧緩和醫療意願書／預立醫療決定／DNR 三者的
  法源、見證人限制、生效關卡；**分野在人工營養及流體餵養**；癌症病人走的是「末期病人」那一款。**D2 只指路，不重寫。**
- `/home/claude/repo/sit-reirradiation.html`〈照過的地方，能不能再照〉——再照射的一般邏輯與劑量紀律。**D3 只指路。**
- `/home/claude/repo/sit-trial-how.html`〈臨床試驗，怎麼找怎麼看〉——**D3 只指路。**
- `/home/claude/repo/sit-last-weeks.html`〈最後那幾週，會發生什麼〉——**D3 只指路。**

---

**Brief D 結束。** 寫作者請注意：本 brief 共 14 條「與 SPEC 不同形狀的事」，
其中第 1、2、4（D1）、第 10、11、12（D3）、第 14（D2 引用地雷）是動筆前必須先讀完的。
所有 PASS 條目的書目與數字均於 **2026-09-03** 由 Europe PMC REST 或官方檔案本次實際抓取，
FAIL／NOT-CITABLE 條目已逐項寫明試過哪些路徑。
