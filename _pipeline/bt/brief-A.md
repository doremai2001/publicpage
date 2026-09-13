# Brief A — 良性腦瘤專題「共同的起點」（A1–A4）

研究員：Group A｜查證日期：2026-09-13
期刊書目資料全部經 **Europe PMC REST**（`/webservices/rest/search?query=EXT_ID:<PMID>&resultType=core&format=json`）逐筆核對（title、journal、year、vol(iss)、pages、DOI、PMID、isOpenAccess）；
OA 全文走 `/webservices/rest/<PMCID>/fullTextXML`；非 OA 但 inEPMC 者改走 `https://www.ncbi.nlm.nih.gov/pmc/articles/<PMCID>/`（HTML，實際抓到才標 PASS）。
台灣端法規走 `law.moj.gov.tw`（curl 成功）；健保支付標準走開放資料 ODS 全表；`nhi.gov.tw` HTML 回 403 → 改抓 PDF；`hpa.gov.tw` 連線失敗 → 改 `mohw.gov.tw`／`twcr.tw`。
**PubMed MCP 本次不可用，未使用。NCCN 未引用。**

引用規則：**只有標 PASS 的來源可以進正文引用。** FAIL 條目保留，讓寫作者知道哪些話只能寫「我查不到可以引用的來源」。
**本 brief 每一個數字都帶「哪一種瘤」的標籤**（腦膜瘤／聽神經瘤＝前庭神經鞘瘤／腦下垂體腺瘤／其他），寫作者不得把任一種瘤的數字寫成三種通用。

---

## ⚠ 與 SPEC 假設不同形狀的事（動筆前必讀，七條）

### 1.「大多數偶然發現的腦膜瘤在追蹤期間沒有長大」——**這句話在不同量法下會得到相反的答案，不能照 SPEC §四紅線 1 的措辭直接寫**

- **體積量法（volumetric）**：Behbahani 2019 前瞻 5 年世代，64 位偶然發現腦膜瘤，用 GammaPlan 做體積分析，**48 顆（75%）體積增加 >15%**，只有 13 顆（20.3%）不變、3 顆（4.7%）縮小[A-S11]。
- **複合「疾病惡化」終點**：IMPACT 工具的國際外部驗證（JAMA Oncol 2026，33 中心、15 國、1,248 人、1,010 顆未治療腦膜瘤，中位追蹤 61 個月），**5 年無惡化存活 88.1%、10 年 85.7%**——也就是十年內約 14% 惡化[A-S10]。
- 兩個數字不衝突，衝突的是**「長大」的定義**：一個是「體積比基線多 15%」，一個是「長到會影響臨床決策（生長＋症狀＋腦膜瘤相關死亡＋失去可治癒時機）」。
- 而且 Behbahani 自己的結論是「**沒有任何一位病人在 5 年內出現腫瘤相關症狀**，超過 60% 呈現自限性生長型態」[A-S11]。
- **正確寫法**：不要寫「大多數不會長大」。寫「**大多數不會因此出事**」——並且在同一段講清楚是用哪一種量法測的（SPEC §四紅線 2 本來就要求標明最大徑對體積，本 brief 把這條提升成 A1 也要遵守）。
- 佐證這件事本身是領域級問題：Millward 2024 系統性回顧（33 篇、32 個世代研究）發現偶然發現／未治療腦膜瘤的結果測量**極度不一致**，268 個逐字結果、只有 77 個有定義，因此無法做有意義的跨研究合併[A-S37]；Islim 2019 統合分析也明講「meningioma growth 的定義與追蹤方案差異極大，妨礙了相關的統合分析」[A-S7]。

### 2. 偶然發現的分母有三個不同的數字，取決於掃了什麼、掃誰、用什麼機器——不可以只寫一個

- Vernooij 2007（Rotterdam Scan Study，NEJM）：2,000 人、平均 63.3 歲（45.7–96.7）、**1.5 T 高解析結構性腦 MRI**；**良性原發腫瘤 1.6%（以腦膜瘤為主）**、腦動脈瘤 1.8%、無症狀腦梗塞 7.2%[A-S1]。
- Bos 2016（同一個世代擴大，Radiology）：**5,800 人、平均 64.9 歲**；偶然發現 **9.5%**（549/5,800），其中**腦膜瘤 2.5%（143/5,800）**、腦動脈瘤 2.3%[A-S2]。
- Morris 2009（BMJ 統合分析，19,559 人、16 篇）：**腫瘤性偶然發現 0.70%（95% CI 0.47–0.98）**，隨年齡上升；**高解析序列 4.3% vs 標準解析 1.7%（p<0.001）**；每掃 37 個無症狀的人會找到 1 個偶然發現[A-S3]。
- EANO 2021 指引自己的講法：「Incidental meningiomas are present on brain MRI of **0.9% to 1.0%** of the general population.」[A-S12]
- 腦下垂體是另一個分母，**而且用的不是腦 MRI**：Hall 1994（Ann Intern Med）100 位正常志願者做**專做腦下垂體的高解析 MRI ＋ 釓對比**，**10%（女 7/70、男 3/30）有 3–6 mm 的局部低訊號病灶被至少兩位判讀者診斷為腦下垂體腺瘤**[A-S4]。Ezzat 2004（Cancer 系統性回顧）：腦下垂體腺瘤整體盛行率 **16.7%（解剖 14.4%、影像 22.5%）**[A-S5]。
- **SPEC §七 圖 1 若只畫一個分母，就是錯的。圖 1 要畫成「同一個問題，三種掃法三個答案」。**

### 3.「腦下垂體腺瘤」的改名是**雙軌並列**，不是單方面改掉——而且反對方的論點正好是本專題的編輯立場

- 2022 年 WHO 內分泌與神經內分泌腫瘤分類第 5 版把分化良好的腺垂體腫瘤「now classified as **pituitary neuroendocrine tumors (PitNETs; formerly known as pituitary adenomas)**」[A-S28]。
- 但實際出版的分類用的是**雙重命名**：Ho 等人（Pituitary Society）逐字寫「Most striking, however, is the use of **dual nomenclature of "pituitary adenoma/pituitary neuroendocrine tumor (NET)"**」[A-S29]。
- 反對方的核心數字（可直接引）：「The overall population prevalence of pituitary neoplasms is **10% or more**. **Local invasiveness occurs only in 1 in 2000 and malignancy in 1 in 100,000** such neoplasms.」——因此「NET」這個標籤「grossly mislabelling the overwhelming majority」[A-S29]。
- 反對方還寫了一段**幾乎就是本專題 §一編輯立場的原文版**：疾病標籤會影響病人的決策與焦慮，低風險疾病的病人「less likely to benefit from treatments and more likely to experience detrimental adverse effects of interventions, **anxiety caused by the disease label**, and financial harm arising from additional and often unnecessary tests and treatments」；並引一個隨機試驗：把「papillary thyroid carcinoma」換成「papillary lesion」會改變治療決策與焦慮程度[A-S29]。
- **這段是 A1 的理論支柱，可以直接寫進去。** A2 必須把爭議兩邊並陳，不可以只寫「現在改叫 PitNET 了」。

### 4. 台灣的癌症登記**確定不收良性腦瘤**，而且有逐字的法源與作業手冊可引——這題查得到，不必寫 gap

- 癌症防治法第 3 條：「癌症：係指經由病理切片證實，或經其他檢查、檢驗有效推定診斷，在臨床上具有再發或轉移現象之**惡性腫瘤**。」第 11 條要求提報的是「新發生之癌症個案」[A-S40]。
- 《台灣癌症登記長表摘錄手冊》（114 年 12 月正式版）逐字：「收案對象為中華民國國籍（外籍人士不收案），第一次經醫師診斷為癌症之個案，亦即 **ICD-O-3 性態碼為 2、3、6、9 者**（若為 6、9 者，需申報原發部位，性態碼改為 3），均需申報。」同手冊「性態碼」欄位說明：「病理醫師常使用 **benign(0)**、**borderline(1)**、in situ(2)、malignant, primary site(3)…其中性態碼為 2、3、6 或 9…的個案必須申報至癌症登記中心。」欄位編碼範圍逐字寫「**2, 3**」[A-S41]。
- **這跟美國相反**：CBTRUS 收惡性與非惡性兩種，非惡性佔多數（2018–2022 非惡性 AAAIR 19.19 vs 惡性 6.86／10 萬）[A-S14]——所以本專題所有「發生率」數字都來自美國登記，台灣沒有對應數字。**這件事本身要寫進 A2。**

### 5. 重大傷病：**良性腦瘤不在項次內**，這題也查得到逐字條文，不是 gap

- 《全民健康保險保險對象免自行負擔費用辦法》第 2 條：「本法第四十八條所稱重大傷病，其項目及證明有效期限如附表一。」[A-S42]
- 附表一「一、需積極或長期治療之癌症」全部 5 個子項的 ICD-10-CM 碼是 **C73／C00.0-C06.9、C09.0-C10.9、C12-C14.8／C50.011-C50.929／C53.0-C53.9、C55／C00.0-C96.9（不含 C73、C94.4、C94.6）**——**全部是 C 碼（惡性腫瘤）**。113-12-31 以前適用版與 114-01-01 以後適用版皆同[A-S42]。
- 全表逐字檢索：**D32（腦膜良性腫瘤）、D33（腦及中樞神經系統其他部位良性腫瘤）、D35（腦下垂體良性腫瘤）零筆**[A-S42]。
- 唯一可能沾到邊的是「十八、脊髓損傷或病變所引起之神經、肌肉、皮膚、骨骼、心肺、泌尿及腸胃等之併發症者（**其身心障礙等級在中度以上者**）」之「(三)其他脊髓病變 Other disease of spinal cord（G32.0、G95.0、G95.11-G95.89、G95.9、G99.2）」[A-S42]——**這是脊髓端的併發症項次，不是「良性腫瘤」項次，而且有身心障礙等級門檻**。正文只能寫成「附表一裡與良性腦瘤沾到邊的只有這一條，條件是脊髓病變造成的併發症且身心障礙中度以上，能不能適用由保險人核定，要問醫務課」。另有「三十、經中央主管機關依罕見疾病防治及藥物法公告之罕見疾病」，NF2 是否在公告名單內本組**未查**（E5 的題）。
- **SPEC §一.5.③ 說「良性腦瘤多數不在癌症項次內，這件事要查證後如實寫」——查證結果是「完全不在癌症項次內」，比「多數不在」更硬。**

### 6. 台灣健保給的立體定位放射手術，**適應症條文本身就寫了三種瘤，但加了一道「開刀不行」的門**——這直接改變台灣讀者的「觀察 vs 處置」處境

- 37028B 三度空間立體定位Ｘ光刀照射治療（82,000 點）、37029B 加馬機立體定位放射手術（153,229 點），適應症逐字含「**聽神經瘤、腦膜瘤、腦下垂體瘤、顱咽管瘤**」，但**必須同時符合以下條件之一**：「A.曾接受開顱手術，但有殘餘腫瘤或腫瘤復發者。B.開顱手術可能造成神經損傷或危險性大者。C.有嚴重心肺疾病或其他內科疾病，不適合侵入性手術或全身麻醉者。…F.顱內單側小腦橋腦角聽神經瘤寬度小於 2.5 公分（不含內耳道）者。」且「**全部個案須事前專案向保險人申請**」[A-S43]。
- **A1／A4 需要知道這件事**（「在台灣，第一線就做放射手術不是預設路徑」），但**單次對分次的比較、平台選擇一律歸 B3／C2，A 組不得自行比較**（SPEC §六、§一.5.①）。

### 7. 台灣官方唯一拆得出來的良性腦瘤數字是 **D33，而且它不含腦膜瘤、不含腦下垂體瘤**

- 113 年度全民健康保險醫療統計年報：西醫門診（含急診）「大腦及中樞神經系統其他部位之良性腫瘤 D33」**就診人數 23,027 人（男 8,700、女 14,327）**、就診率 98.36／10 萬；出院件數 **652 件**、住院費用 132,096,723 點[A-S45]。
- **同一份年報的疾病別分類裡沒有 D32（腦膜）、沒有 D35.2（腦下垂體）**，它們被歸進「其他腫瘤 remainder of C00-D49」（門診 1,065,794 人）[A-S45]。
- 所以：**台灣沒有官方的腦膜瘤人數，也沒有官方的腦下垂體腺瘤人數。** 聽神經瘤有一筆學術的健保資料庫研究（見台灣端）。

---

## A1 `bt-incidental`〈影像上發現一顆東西〉【紅線 1，全專題最高風險，雙向】

### Key facts

**分母（每一筆都帶研究族群、年齡、影像條件——見上面「不同形狀 2」）**

| 來源 | 族群與影像 | 數字 |
|---|---|---|
| Vernooij 2007[A-S1] | 2,000 人，平均 63.3 歲（45.7–96.7），族群為本的 Rotterdam Study，**1.5 T 標準化高解析結構性腦 MRI**，無病理確認 | **良性原發腫瘤 1.6%（以腦膜瘤為主）**；腦動脈瘤 1.8%；無症狀腦梗塞 7.2%。腦梗塞與腦膜瘤盛行率隨年齡上升，動脈瘤不隨年齡上升 |
| Bos 2016[A-S2] | 同世代擴大，**5,800 人，平均 64.9 歲，女性 55.1%**，前瞻族群為本 | 偶然發現 **9.5%（549/5,800；95% CI 8.7–10.3）**；**腦膜瘤 2.5%（143/5,800；95% CI 2.1–2.9）**；腦動脈瘤 2.3%（134/5,800） |
| Morris 2009[A-S3] | 16 篇、19,559 人，無神經症狀者的研究／職業／臨床／商業篩檢 MRI | **腫瘤性偶然發現 0.70%（95% CI 0.47–0.98）**，隨年齡上升（p=0.003）；非腫瘤性 2.0%；**高解析 4.3% vs 標準解析 1.7%（p<0.001）**；「需掃描的無症狀人數」= 37 |
| EANO 2021[A-S12] | 指引敘述句 | 「Incidental meningiomas are present on brain MRI of **0.9% to 1.0%** of the general population.」 |
| Hall 1994[A-S4] | 100 位正常志願者（女 70、男 30，18–60 歲），**專做腦下垂體的高解析 MRI＋Gd-DTPA**，三位判讀者盲讀 | **10%（女 10%、男 10%）有 3–6 mm 局部病灶，經至少兩位判讀者診斷為腦下垂體腺瘤** |
| Ezzat 2004[A-S5] | 系統性回顧／統合分析，解剖＋影像研究 | **腦下垂體腺瘤整體盛行率 16.7%（解剖 14.4%、影像 22.5%）** |
| Marinelli 2022[A-S21] | 系統性回顧，丹麥／荷蘭／台灣／美國 4 個族群 | **散發性聽神經瘤最新發生率 3.0–5.2／10 萬人年**（≥70 歲最高、峰值 20.6／10 萬人年）；**美國一篇報告「無症狀、偶然診斷」的聽神經瘤發生率 1.3／10 萬人年（2012–2016）**；作者估終生盛行率「likely exceeds 1 per 500 persons」 |

**Bos 2016 的「後來怎麼了」——A1 最重要的一段**[A-S2]
- 5,800 人裡 **188 人（3.2%，95% CI 2.8–3.7）**因偶然發現被轉介給專科醫師。
- 這 188 人裡 **144 人（76.6%，95% CI 70.1–82.1）不是被採取「觀察（wait-and-see）」就是初診後即結案**。
- 「The **majority of meningiomas** and **virtually all aneurysms** not referred or referred but untreated **remained stable in size** during follow-up.」（追蹤最長 9 年）
- 作者結論逐字：偶然發現「occur in over 3% of the general middle-aged and elderly population, but are **mostly without direct clinical consequences**」。

**「發現了不等於要開刀」的世代證據（腦膜瘤）**[A-S7][A-S8][A-S9][A-S10]
- Islim 2019 統合分析（20 篇、2,130 位偶然發現腦膜瘤）：初診時的處置分布是**手術 27.3%、立體定位放射手術 22.0%、主動監測 50.7%**，加權平均追蹤 49.5 個月（SD 29.3）。主動監測者**出現症狀的合併風險 8.1%（95% CI 2.7–16.1）**；勘誤後更新為 **8.4%（95% CI 2.8–16.7），n=575，69 人出現症狀，I²=88.9%**[A-S8]。監測一段時間後接受介入的合併比例 **24.8%（95% CI 7.5–48.0）**，加權平均到介入的時間 24.8 個月（SD 18.2）。**開刀後病理是 WHO grade 1 的合併比例 94.0%（95% CI 88.2–97.9）**。作者結論逐字：「**Intervention at diagnosis may lead to unnecessary overtreatment.**」
- IMPACT 外部驗證（JAMA Oncol 2026，n=1,248，33 中心 15 國，中位年齡 66 歲、女性 80%，中位追蹤 61 個月）[A-S10]：1,010 顆未治療腦膜瘤中 **114 顆（11.3%）惡化**、132 顆（13.1%）接受介入；**383 人（40.5%）在沒有惡化也沒有介入的情況下死於與腦膜瘤無關的原因**。5 年無惡化 88.1%、10 年 85.7%。低／中／高風險組的惡化風險 **3.9% / 24.2% / 51.6%**。

**哪些情況「不是觀察題」——三種瘤各自的可引來源（圖 1 右半邊）**

- **腦下垂體腺瘤（最明確，指引直接列清單）**：Endocrine Society 2011 指引逐字建議轉手術的情形——「if they have a **visual field deficit**; signs of compression by the tumor leading to other visual abnormalities, such as **ophthalmoplegia**, or **neurological compromise** due to compression by the lesion; **a lesion abutting the optic nerves or chiasm**; **pituitary apoplexy with visual disturbance**; or if the incidentaloma is **a hypersecreting tumor other than a prolactinoma**」[A-S25]。同指引也規定：病灶若貼到或壓到視神經／視交叉，要做視野檢查[A-S25]。
- **腦膜瘤**：EANO 2021 逐字——「The primary treatment for the majority of **symptomatic or enlarging** meningiomas is surgery.」[A-S12]；Islim 2019 指出主動監測期間出現症狀的相關因子是**腫瘤周圍水腫（OR 8.72，95% CI 0.35–14.90）與腦膜瘤直徑 ≥3 cm（OR 34.90，95% CI 5.17–160.40）**[A-S7]（注意兩個 CI 都非常寬，不可寫成精確倍數）。
- **聽神經瘤**：CNS 2018 聽力保存指引明載，觀察組在**第 10 年**維持可用聽力的機率只剩「moderately low（>25%–50%）」[A-S24]；Kirchmann 2017 的實測見 A4。**「已造成聽損」不等於「必須治療」，而是「不能當成沒事，要進入有時程的聽力追蹤」**——寫法見 Claim ceiling。
- **反向的紅線：什麼情況不需要急**：Bos 2016 的 76.6% 觀察／結案[A-S2]、Islim 2019 的「診斷當下介入可能造成過度治療」[A-S7]、IMPACT 的「低風險組 5 年惡化 3.9%」與「可安全從門診結案（safe discharge from outpatient care）」[A-S10]。

**「良性／惡性」在顱內是什麼意思**
- 登記層面：CBTRUS 2018–2022，全部原發腦與其他中樞神經腫瘤 AAAIR **26.05／10 萬（惡性 6.86、非惡性 19.19）**；**非惡性腫瘤的 5 年相對存活 91.7%，惡性 34.8%**[A-S14]。**非惡性 ≠ 100%，這個落差要寫出來，但不可以拿它嚇人**（相對存活率的分子分母含多種死因，本 brief 不提供拆分）。
- 腦膜瘤的「惡性」是罕見的一小塊：CBTRUS 2017–2021，全體腦膜瘤 195,297 例、AAAIR **10.15**；其中**惡性腦膜瘤 1,608 例、AAAIR 0.08**（佔全部腦瘤 0.3%）[A-S15]。
- 腦下垂體：「local invasiveness occurs only in **1 in 2000** and malignancy in **1 in 100,000**」[A-S29]。
- 位置才是風險的來源：腦膜瘤的症狀組成完全由位置決定（見 A3 的整段）[A-S13]；EANO 指出 grade 1 腦膜瘤仍可能早期復發、grade 2 完全切除者也可能長期無事，「**分級與臨床病程之間有相當的個體差異**」[A-S12]。

**診斷延遲的證據（只有腦下垂體這一種瘤查得到，其他兩種是 gap）**
- 腦下垂體腺瘤：Forsgren 2025（BMJ Open，瑞典 7 家大學醫院、654 人：非功能性腺瘤 314、泌乳素瘤 118、肢端肥大症 164、庫欣氏病 58）——**從症狀到診斷 <1 年 66%、1–5 年 12%、5–9 年 13%、>10 年 9%**；最長的延遲在庫欣氏病與肢端肥大症；**女性比男性延遲更久（p<0.001）**；首次就醫多半是家醫科[A-S32]。
- 聽神經瘤：**沒有「延遲」的直接數字，但有反方向的可引數字**——丹麥 40 年全國世代顯示診斷時的平均外耳道外腫瘤大小從 1976 年的 26 mm 降到 2015 年的 13.4 mm，診斷年齡中位數從 49.2 歲升到 60 歲，發生率從 3／百萬／年升到 34／百萬／年，作者歸因於「easier access to improved diagnostics」[A-S19]。**這是「找得更早、找到更多」，不是「延遲」。不可以互換。**
- 腦膜瘤：**gap。本次未找到可引用的診斷延遲數據，不可推論。**

### 反方向的資料（誠實必列）

1. **偶然發現本身有代價**：Morris 2009 的結論句逐字——這些發現「deserve to be mentioned when obtaining informed consent for brain MRI…**but are not sufficient to justify screening healthy asymptomatic people**」[A-S3]。**不可以把本篇寫成鼓勵健檢做腦 MRI。**
2. **體積量法下絕大多數腦膜瘤會長大**：Behbahani 75%[A-S11]（見「不同形狀 1」）。只寫「多數不會長大」就是選擇性引用。
3. **有一群人是真的需要處理的**：IMPACT 高風險組 5 年惡化 51.6%[A-S10]；Islim 2019 監測中 24.8% 最終接受介入[A-S7]。
4. **標籤本身會造成傷害**：Ho 2022 引用的隨機試驗顯示改個病名就會改變治療決策與焦慮[A-S29]——這是雙向的：既支持「不要用『腦瘤』兩個字嚇人」，也提醒「不要用『良性』兩個字讓人安心到不回診」。

### Claim ceiling（硬上限）

**可寫**
- 「在 5,800 位平均 65 歲的一般民眾做研究用腦 MRI，9.5% 有偶然發現，其中腦膜瘤 2.5%、腦動脈瘤 2.3%」[A-S2]（要標明族群與年齡）。
- 「高解析序列找到的偶然發現比標準序列多（4.3% 對 1.7%）——機器越好，找到的越多」[A-S3]。
- 「腦下垂體是特例：拿高解析的腦下垂體專用 MRI 去掃 100 個正常人，10 個看得到 3–6 mm 的東西」[A-S4]；「解剖與影像研究合起來，腦下垂體腺瘤的盛行率約 16.7%」[A-S5]。
- 「這 5,800 人裡真正被轉介的是 3.2%，而被轉介的人有四分之三是繼續觀察或第一次門診就結案」[A-S2]。
- 「一個 1,248 人、33 中心 15 國的世代顯示，偶然發現的腦膜瘤 10 年無惡化 85.7%；同一群人裡有 40.5% 在腦膜瘤還沒動靜之前就先死於別的原因」[A-S10]——**這一句是全篇最好用的一句，因為它同時防兩個方向。**
- 「診斷當下就介入，可能造成過度治療」——這是 Islim 2019 的原話，可直接引[A-S7]。
- 「哪些情況不是觀察題」：腦下垂體照 Endocrine Society 2011 的清單逐條寫[A-S25]；腦膜瘤照 EANO「有症狀或正在長大」寫[A-S12]；聽神經瘤照 CNS 指引寫成「聽力要有時程地追」[A-S24]。
- 「良性不等於零風險，但顱內的風險來自位置，不是單看組織學」——用 CBTRUS 非惡性 5 年相對存活 91.7%[A-S14]＋惡性腦膜瘤發生率 0.08 對全體 10.15[A-S15]＋腦下垂體侵襲 1/2000、惡性 1/100,000[A-S29]。

**不可寫**
- ❌「大多數偶然發現的腦膜瘤不會長大」（未標量法即為誤導，見「不同形狀 1」）。
- ❌「良性所以可以放心」「不用回診」——IMPACT 低風險組也有 3.9% 的 5 年惡化率，而且「安全從門診結案」是**用工具分層之後**的結論，不是預設[A-S10]。
- ❌「腦瘤＝腦癌」的反向誤讀，也不可以用「所以不是癌症」收尾。
- ❌ 任何一句讓讀者自己判斷該不該治療。本篇給的是**要問醫師的問題清單**（SPEC §四紅線 1）。
- ❌ 把 Hall 1994 的 10% 寫成「做腦 MRI 有 10% 會發現腦下垂體瘤」——那是**專做腦下垂體的序列**，不是一般腦 MRI[A-S4]。
- ❌ 把聽神經瘤診斷時腫瘤變小、年齡變大寫成「診斷延遲改善了」或「延遲很嚴重」[A-S19]。
- ❌ 鼓勵無症狀者去做腦 MRI 健檢[A-S3]。
- ❌ 用診斷延遲的瑞典腦下垂體數字去講腦膜瘤或聽神經瘤[A-S32]。

### Caveats／safety notes（寫作者必寫）

- Vernooij 2007 與 Bos 2016 的全部診斷都是**影像診斷，沒有病理確認**（Vernooij 摘要逐字：「All diagnoses were based on MRI findings, and additional histologic confirmation was not obtained.」）[A-S1]。
- 三個分母的世代都是**中老年白人為主的歐洲族群**，年輕人與亞洲族群的數字本 brief 查不到，不可外推。
- Islim 2019 的兩個 OR（水腫 8.72、直徑 ≥3 cm 34.90）信賴區間極寬，**只能寫方向，不可寫倍數**；且 2019 年的勘誤把「T2 訊號」與「腫瘤周圍訊號」從預後因子名單裡拿掉了[A-S8]（但 IMPACT 模型裡「meningioma hyperintensity」HR 10.6 仍在[A-S9]——兩者並陳，不可只寫一邊）。
- 「不是觀察題」的三份清單來自三個不同專科的指引，**不可以合併成一張通用清單**（紅線 9）。

### 台灣端（A1）

- **癌症登記**：良性腦瘤不收（逐字見「不同形狀 4」）[A-S40][A-S41]。
- **重大傷病**：不在項次內（逐字見「不同形狀 5」）[A-S42]。
- **腦 MRI 的健保身分**：支付標準 **33084B 磁振造影－無造影劑 6,500 點**、**33085B 磁振造影－有造影劑 11,500 點**；備註只有兩句：「1.本項須限**經保險人同意之醫療院所**實施。2.申報費用時必須**附上報告結果**。」**支付標準本文沒有任何腫瘤別的適應症或頻次限制**[A-S43]。
- 頻次與適應症的規範在另一份文件——《全民健康保險醫療費用審查注意事項》「(十八)其他注意事項 1.電腦斷層及磁振造影檢查審查原則」逐字重點[A-S44]：
  - 「『電腦斷層造影』及『磁振造影』診療項目均以『**次**』為單位…病患可同次施作，僅能申報 1 次，不得以不同部位為理由分次執行或拆分申報多次。」
  - 「**須附檢查申請書、報告及影像，否則不予給付。**」申請書或報告須含臨床診斷、檢查目的、相關病史、理學檢查（神經系統檢查需附詳細神經學理學檢查）、其他相關檢查結果。
  - 「如**短期內（如十二週）再次執行**電腦斷層或磁振造影檢查，應敘明病情及必要性，應詳加審查。」
  - 「磁振造影檢查之選擇應用，須在公認有明顯優於其他檢查（procedure of choice），或其他檢查無法提供足夠資料以輔助臨床治療時，方可申請。」
  - 「**癌症患者**檢查須有癌病史或確切病理診斷、有確切臨床需要且同時其他檢查無法輔助診斷時…方得申請磁振造影檢查。」（注意：這條寫的是「癌症患者」，良性腦瘤不在此列，正文不可推論）
- **gap（要寫成 gap）**：健保沒有針對腦膜瘤／聽神經瘤／腦下垂體腺瘤的 MRI **追蹤頻次**條文。《審查注意事項》全文檢索：「腦膜瘤」「腦下垂體」「聽神經瘤」**零筆**；「腦瘤」2 筆，都是腦電圖診斷價值的段落，與 MRI 追蹤無關[A-S44]。**正文寫「查不到列項，追蹤頻率怎麼排請問你的主治醫師與醫務課」，永不推論有無給付。**

### 給繪圖組的數字（圖 1 `fig-bt-incidental`）

**左半：分母（每一格都必須標族群／年齡／影像條件）**
- 一般人做研究用腦 MRI（5,800 人、平均 64.9 歲）：偶然發現 9.5%；腦膜瘤 2.5%；動脈瘤 2.3%[A-S2]
- 統合分析（19,559 人）：腫瘤性偶然發現 0.70%；高解析 4.3% vs 標準解析 1.7%[A-S3]
- 腦下垂體專用高解析 MRI（100 位正常志願者）：10%（3–6 mm）[A-S4]
- 聽神經瘤：偶然發現的發生率 1.3／10 萬人年（美國 2012–2016）[A-S21]

**中段：被轉介之後**
- 3.2% 被轉介 → 其中 76.6% 觀察或結案[A-S2]
- 偶然發現腦膜瘤 10 年無惡化 85.7%；40.5% 死於非腦膜瘤原因[A-S10]

**右半：不是觀察題（三欄，各自標瘤別，不可合併）**
- 腦下垂體腺瘤：視野缺損／眼肌麻痺等壓迫性視覺異常／神經受壓／病灶貼到或壓到視神經或視交叉／垂體中風合併視覺障礙／泌乳素瘤以外的功能性腺瘤[A-S25]
- 腦膜瘤：有症狀或正在長大[A-S12]
- 聽神經瘤：已有聽損者需進入有時程的聽力追蹤（觀察組第 10 年可用聽力只剩 >25%–50%）[A-S24]

**禁止入圖**：任何「良性所以安全」的視覺收尾；任何把三種瘤合併的分流箭頭。

---

## A2 `bt-three-kinds`〈腦膜瘤、聽神經瘤、腦下垂體瘤：三種病，三套邏輯〉【紅線 9，地基篇】

### Key facts

**發生率與佔比（全部來自美國 CBTRUS；台灣沒有對應數字，見台灣端）**

站上 `gb-what-it-is` 已引的「腦膜瘤佔全部腦瘤 42.6%」出自 CBTRUS 2018–2022（Price 2025）。**本次重新核對：正確，不需更正。** 該報告摘要逐字：「the most common non-malignant histopathology was meningioma (**42.6% of all tumors** [includes malignant meningioma] and **57.4% of all non-malignant tumors**)」[A-S14]。

| | CBTRUS 2018–2022[A-S14] | CBTRUS 2017–2021 明細[A-S15] |
|---|---|---|
| 全部原發腦與其他 CNS 腫瘤 | AAAIR **26.05**／10 萬（惡性 6.86、非惡性 19.19）；女 29.67 > 男 22.23 | AAAIR 25.34；女 28.77 > 男 21.78 |
| **腦膜瘤** | **42.6% 全部腫瘤、57.4% 非惡性**；女多於男 | 41.7% 全部腫瘤、56.8% 非惡性；195,297 例；**AAAIR 10.15（男 6.02、女 13.90）**；其中惡性 1,608 例、AAAIR 0.08 |
| **腦下垂體腫瘤（histology grouping「Tumors of the pituitary」）** | 摘要未拆 | **17.4% 全部腫瘤**；81,187 例；**AAAIR 4.67（男 4.03、女 5.41）**；非惡性佔 99.8%（男）／99.9%（女） |
| **神經鞘瘤（nerve sheath tumors，聽神經瘤屬之）** | 摘要未拆 | **8.0% 全部腫瘤**；37,436 例；**AAAIR 2.02**（非惡性 2.01、惡性 0.01） |
| 顱咽管瘤 | 摘要未拆 | 0.7% 全部腫瘤；3,096 例；AAAIR 0.18；非惡性 99.8–99.9% |
| 存活 | 非惡性 5 年相對存活 **91.7%**；惡性 34.8% | 非惡性 92.0%；惡性 35.7% |

- 三者合計：CBTRUS 自己寫「Tumors of the pituitary (17.4%) and nerve sheath tumors (8.0%) combined accounted for slightly more than one-fourth of all tumors (**25.4%**)」[A-S15]；加上腦膜瘤 41.7%，**三種病合起來就是美國全部原發腦瘤登記的三分之二。這是本專題成立的根據，可以寫。**
- **注意標籤**：CBTRUS 的「腦膜瘤 42.6%」的分母是**全部原發腦與其他中樞神經腫瘤（含非惡性）**，不是「腦癌」。CBTRUS 的定義與 NPCR/SEER/NAACCR 不同——CBTRUS 收 pituitary 與非惡性，後者通常只出惡性，報告自己寫「These differences in definition therefore influence the direct comparison of published rates.」[A-S15]

**性別分布（可引，帶發生率比）**[A-S15]
- 非惡性腦膜瘤 男:女 IRR **0.43（p<0.0001）**——女性明顯較多。
- 腦下垂體腫瘤 男:女 IRR **0.75（p<0.0001）**——女性較多。
- 神經鞘瘤：CBTRUS 未把它列在「女性較多」的名單裡；本 brief **不提供聽神經瘤的性別比**（gap）。

**典型年齡**
- 腦膜瘤：CBTRUS「The most diagnosed histopathologies in older ages were glioblastoma, meningiomas, and lymphoma (median age of 66, **68**, and 69 years, respectively)」[A-S15]。
- 聽神經瘤：丹麥全國世代，診斷年齡中位數 1976 年 49.2 歲 → 2015 年 **60 歲**[A-S19]；美國／丹麥／荷蘭／台灣合看，**≥70 歲發生率最高（峰值 20.6／10 萬人年）**[A-S21]。台灣：發生率最高的年齡層是 **60–69 歲（4.86／10 萬）**[A-S35]。
- 腦下垂體腺瘤：比利時 Liège 人口普查式研究（68 位臨床相關腺瘤／71,972 人），**診斷時平均年齡 40.3 歲、女性 67.6%、42.6% 是大腺瘤**[A-S6]。**（CBTRUS 的腦下垂體中位年齡本次未取得 → gap）**
- **這三個年齡不可以合併成一句「中老年人的病」**：腦下垂體腺瘤的臨床相關族群明顯年輕。

**細胞來源（各一句，不可混寫）**
- **腦膜瘤**：來自腦膜上皮細胞（meningothelial cells）／蛛網膜帽細胞（arachnoid cap cells）——「Arachnoid cap cells make up the outer layer of the arachnoid mater and arachnoid villi and with cytological similarities to meningiomas cells, it is likely their cell of origin」；而且**顱底與大腦凸面的腦膜上皮細胞胚胎來源不同（中胚層 vs 神經嵴），這個差異影響各部位好發的組織亞型與體細胞突變分布**[A-S13]。
- **腦下垂體腺瘤／PitNET**：來自**腺垂體（前葉）**的內分泌細胞，2022 WHO 明確把前葉（adenohypophyseal）腫瘤與後葉（neurohypophyseal）及下視丘腫瘤分開，並以細胞譜系（PIT1、TPIT、SF1、GATA3、ERα 轉錄因子免疫染色）分型[A-S28]。
- **聽神經瘤（前庭神經鞘瘤）**：屬於 CBTRUS 的「nerve sheath tumors」組（ICD-O 9540, 9541, 9550, 9560, 9561, 9570, 9571）[A-S15]；解剖上分為**內耳道內（intrameatal／intracanalicular）**與**延伸到小腦橋腦角（extrameatal）**兩種，丹麥全國資料就是照這個二分法統計生長[A-S16]。**「起源於前庭神經的許旺細胞」這句話本次未找到可直接引用的原文出處 → 寫成「神經鞘瘤」這個分類即可，或由 B/C 組補來源。**

**三套決策邏輯的骨架（每一條都有指引或綜述來源）**

| | 第一個要問的問題 | 可引來源 |
|---|---|---|
| **腦膜瘤** | **分級與位置**。定性診斷靠影像即可（「A provisional diagnosis of meningioma is typically made by neuroimaging, mostly MRI」），**但 WHO 分級必須靠手術取得組織**（「A surgical intervention with tissue…is required for the definitive diagnosis according to the WHO classification」）；所以無症狀、年長者「may be managed by a **watch-and-scan** strategy」[A-S12]。位置決定可切除性：「EOR is determined by tumor location, consistency, size, and proximity or involvement of critical neurovascular structures」[A-S12]；顱底腦膜瘤多為 grade 1、凸面／矢狀竇旁／大腦鐮／竇匯／腦室內較多高分級[A-S13] |
| **聽神經瘤** | **聽力**。CNS 2018 用整整一份指引（9 個問題）處理「三條路各自的可用聽力保存率」，且明訂觀察組 2／5／10 年的機率級距[A-S24]；診斷的入口也是聽力——不對稱感音神經性聽損的 MRI 篩檢門檻寫在另一份指引裡[A-S23] |
| **腦下垂體腺瘤** | **它有沒有在分泌**。Endocrine Society 2011 第一句建議就是完整病史與理學檢查＋**篩檢荷爾蒙過度分泌與腦下垂體功能低下的實驗室檢查**＋（病灶貼到視神經／視交叉時）視野檢查；而轉手術的條件裡明白寫著「if the incidentaloma is a **hypersecreting tumor other than a prolactinoma**」——**泌乳素瘤被單獨挑出來，因為它是唯一藥物優先的**[A-S25]。**藥物細節一律歸 D2，A2 只寫這個分流點。** |

**其他良性顱內腫瘤（各一句的事實依據，**不可暗示「都差不多」**）**
- **血管母細胞瘤（hemangioblastoma）**：SEER 分析，中樞神經系統血管母細胞瘤**整體發生率 0.141／10 萬人年**；多變項分析顯示**多發腫瘤是較差存活的獨立因子（HR 1.715，p<0.001）**、曾接受手術者較好（HR 0.638，p=0.013）；作者結論手術是最常用也建議的處置[A-S33]。（**多發 → 想到 von Hippel-Lindau**，這條線指向 E5。）
- **顱咽管瘤**：CBTRUS 2017–2021，3,096 例、**AAAIR 0.18／10 萬、佔全部腦瘤 0.7%**，99.8–99.9% 為非惡性[A-S15]。健保 37028B／37029B 的立體定位放射手術適應症把它與三種主角並列[A-S43]。
- **表皮樣囊腫（epidermoid cyst）**：小腦橋腦角表皮樣囊腫 17 例手術世代（平均追蹤 126 個月）——**全切除只有 5 例，12 例是不完全切除（把貼在血管、神經或腦幹上的殘留留下）**；**切除程度與復發風險無關**；症狀性復發平均發生在 **9 年以上之後**；作者結論「it may be acceptable to leave tumor capsule fragments adhering closely to nerves, vessels, or brainstem」[A-S34]。（n=17 的單中心系列，**只能寫成「一個小型長期追蹤系列顯示…」**）

**「腦下垂體腺瘤」的命名變動與爭議（必須並陳）**
- **改名方**：2022 年 WHO 內分泌與神經內分泌腫瘤分類第 5 版，分化良好的腺垂體腫瘤「are now classified as **pituitary neuroendocrine tumors (PitNETs; formerly known as pituitary adenomas)**」；同時把「pituitary carcinoma」改成「**metastatic PitNET**」，理由是避免與神經內分泌癌混淆[A-S28]。
- **實際採用的是雙軌**：「the use of **dual nomenclature of "pituitary adenoma/pituitary neuroendocrine tumor (NET)"**」[A-S29]。
- **反對方（Pituitary Society，Ho／Gadelha／Kaiser／Reincke／Melmed）**逐字論點[A-S29]：
  - 生物學：「A 'NET' label is a misrepresentation of the overwhelmingly benign clinical biology of pituitary neoplasms…**Local invasiveness occurs only in 1 in 2000 and malignancy in 1 in 100,000**」。
  - 分類學：突觸素、NSE、體抑素受體「are not specific to NE cells; they are also expressed in **thyroid and adrenal neoplasms**」——照同樣的推理，甲狀腺腺瘤與腎上腺腺瘤是不是也要改叫 NET？
  - 預後：「There is simply **no clinically relevant grading system** available for pituitary neoplasms that is based on histology and which determines clinical outcome.」
  - 臨床後果：NET 這個字在病人端連結到「metastases occurring in 50% of these patients at late diagnosis」（引北美神經內分泌腫瘤學會的衛教）與 Mayo Clinic 衛教頁上的「cancers」。
  - 程序：「the **patient perspective** in such a relevant nomenclature shift has not been considered, that patient advocacy groups have not been counseled, nor have patient and public involvement representation been sought」；Pituitary Society 為此在 2019 年召開國際工作坊，「**The IARC/WHO was unable to attend.**」
- 更早的立場聲明：Ho KKY 等，「A tale of pituitary adenomas: to NET or not to NET: Pituitary Society position statement」，*Pituitary* 2019;22(6):569–573[A-S30]（**書目經核對，摘要不可取得 → 只能當「這場爭論有正式立場聲明」的指路，不可引其內文**）。
- 站上 `gb-what-it-is` 現行寫法「腦下垂體腫瘤在 CNS5 改稱 pituitary adenoma／PitNET」與雙軌命名一致，**不需更正**；A2 要把爭議補上。

### 反方向的資料（誠實必列）

- 「腦膜瘤佔 42.6%」不代表「腦瘤有四成是腦膜瘤」對台灣成立——**CBTRUS 是美國登記，而台灣的癌症登記根本不收非惡性腫瘤**[A-S40][A-S41]，所以台灣無法產生同樣的分母。這句話必須在同一段講。
- 「非惡性」不等於「不會死」：CBTRUS 非惡性腦瘤 5 年相對存活 91.7%[A-S14]。
- 分級不是命運：EANO 明講 grade 1 有一部分意外早復發、grade 2 完全切除者也可能長期無事[A-S12]（細節歸 B1）。

### Claim ceiling

**可寫**
- 三種瘤在美國登記的佔比與發生率（每筆帶 CBTRUS 年份與分母定義）[A-S14][A-S15]。
- 「三種病合起來佔美國原發腦瘤登記的三分之二」[A-S15]。
- 三種瘤各自的性別傾向（腦膜瘤與腦下垂體女多於男，帶 IRR）[A-S15]、各自的典型年齡（腦膜瘤中位 68 歲[A-S15]；聽神經瘤診斷中位年齡已升到 60 歲[A-S19]、台灣高峰 60–69 歲[A-S35]；腦下垂體腺瘤臨床相關者平均 40.3 歲[A-S6]）。
- 三套決策邏輯的骨架，每一條引自己的指引[A-S12][A-S24][A-S25]。
- 命名爭議兩邊並陳[A-S28][A-S29]。
- 其他良性顱內腫瘤各一句，**各自帶自己的數字**[A-S33][A-S15][A-S34]。

**不可寫**
- ❌ 把三種瘤的預後、治療門檻或追蹤時程寫成共用的一套（紅線 9）。
- ❌ 把「其他良性顱內腫瘤」寫成「都差不多」——血管母細胞瘤多發時預後較差[A-S33]、表皮樣囊腫切不乾淨也不影響復發風險[A-S34]，這兩件事跟腦膜瘤的邏輯完全不同。
- ❌ 用美國佔比去推台灣人數（無分母，見台灣端）。
- ❌ 寫「WHO 已經把腦下垂體腺瘤改名為 PitNET」而不寫雙軌與爭議[A-S29]。
- ❌ 寫聽神經瘤的性別比（本 brief 查不到可引來源）。
- ❌ 在 A2 講任何治療細節（歸 B／C／D）。

### Caveats

- CBTRUS 的 histology grouping 與部位 grouping 是兩套數字（部位「Pituitary C75.1-C75.2」18.2% vs 組織「Tumors of the pituitary」17.4%），**引用時要說是哪一套**[A-S15]。
- CBTRUS 2018–2022 報告在 Europe PMC 無 PMCID、無 OA 全文（本次只能取摘要）；三種瘤的細項拆分來自 **2017–2021 版**的全文表格。**正文並列時要標年份，不可混成一年。**[A-S14][A-S15]
- Daly 2006 的 40.3 歲是「**臨床相關**（clinically relevant）」腦下垂體腺瘤的平均診斷年齡，不是所有影像上看得到的病灶[A-S6]。

### 台灣端（A2）

- **癌症登記不收良性腦瘤**（法源與作業手冊逐字，見「不同形狀 4」）[A-S40][A-S41]。台灣癌症登記中心自述其法源即癌症防治法第 11 條[A-S46]。
- **衛福部有沒有良性腦瘤的官方統計**：**部分有，但拆不到瘤別**。113 年度全民健康保險醫療統計年報：
  - 西醫門診（含急診）「大腦及中樞神經系統其他部位之良性腫瘤 **D33**」**就診人數 23,027 人**（男 8,700、女 14,327）、就診率 98.36／10 萬[A-S45]。
  - 出院患者 **D33 652 件**、住院費用 132,096,723 點；同表「腦惡性腫瘤 C71」3,422 件[A-S45]。
  - **D32（腦膜良性腫瘤）與 D35.2（腦下垂體良性腫瘤）在這份年報的疾病別分類裡沒有獨立列項**，被歸入「其他腫瘤 remainder of C00-D49」[A-S45]。→ **台灣沒有官方的腦膜瘤人數，也沒有官方的腦下垂體腺瘤人數（gap）。**
- **聽神經瘤台灣有一筆學術數字**：Koo 2018（Ann Otol Rhinol Laryngol），用健保資料庫 LHID2000，ICD-9-CM 225.1、且診斷前有做過 MRI 者才算確定個案，20 歲以上，2001–2012 共 206 例；**年發生率 2.66／10 萬（95% CI 2.32–3.05）**，年間波動 1.74–3.72；**60–69 歲最高，4.86／10 萬**[A-S35]。（學術研究，不是官方統計，要標清楚。）
- **健保給付的立體定位放射手術條文把三種瘤寫在一起**（37028B／37029B，見「不同形狀 6」）[A-S43]——A2 可以用它當「台灣的制度也把這三種病放在同一格」的一句話，**但不得比較單次與分次、不得比較平台**（歸 B3／C2）。

### 給繪圖組的數字（圖 2 `fig-bt-three-kinds`）

三欄分流樹，每欄獨立，**不共用箭頭**：

| | 腦膜瘤 | 聽神經瘤（前庭神經鞘瘤） | 腦下垂體腺瘤／PitNET |
|---|---|---|---|
| 長在哪 | 腦膜（蛛網膜帽細胞）[A-S13] | 內耳道內／小腦橋腦角[A-S16] | 腺垂體（前葉）[A-S28] |
| 美國登記佔比 | 42.6%（2018–2022）[A-S14] | 神經鞘瘤 8.0%（2017–2021）[A-S15] | 17.4%（2017–2021）[A-S15] |
| 發生率（／10 萬） | 10.15（男 6.02／女 13.90）[A-S15] | 2.02[A-S15]；台灣 2.66[A-S35] | 4.67（男 4.03／女 5.41）[A-S15] |
| 典型年齡 | 中位 68 歲[A-S15] | 中位 60 歲（丹麥 2015）[A-S19]；台灣高峰 60–69 歲[A-S35] | 臨床相關者平均 40.3 歲[A-S6] |
| 第一個問題 | 分級與位置[A-S12] | 聽力[A-S24] | 有沒有在分泌[A-S25] |

圖腳註必寫：**各研究族群、登記定義與年份不同，數點不可直接互比；台灣的癌症登記不收非惡性腫瘤，因此無對應的台灣發生率。**

---

## A3 `bt-where`〈位置比大小重要〉

**本節所有症狀—位置對應都有來源。寫作者不得憑解剖推理自行補症狀。**

### Key facts

**腦膜瘤各部位的分布比例（帶分母說明）**[A-S13]

Ogasawara 2021（Biomedicines 綜述，OA）彙整三篇來源後給出的區間——**是區間不是單一數字，正文要照抄區間**：

| 部位 | 比例 |
|---|---|
| 凸面（convexity，大腦外側面） | **20–37%** |
| 矢狀竇旁（parasagittal，半球內側） | **13–22%**（其中大腦鐮 falcine 5%） |
| 脊髓 | **7–12%** |
| **顱底合計** | **43–51%** |
| ・前顱底（frontobasal） | 10–20% |
| ・蝶骨嵴與中顱窩 | **9–36%** |
| ・後顱窩 | 6–15% |
| 　○小腦天幕 | 2–4% |
| 　○小腦凸面 | 5% |
| 　○**小腦橋腦角** | **2–11%** |
| 　○枕骨大孔 | 3% |
| 　○岩斜區（petroclival） | <1–9% |
| 腦室內 | 1–5% |
| 眼眶 | <1–2% |
| 異位 | <1% |

- 同一篇：「**Grade I meningiomas are more likely to be found at the skull base**, whereas **higher grade meningiomas are more likely to be found at the convexity, parasagittal, falcine, torcular, and intraventricular regions**」[A-S13]。
- 另一筆佐證（大型病理世代，n=2,608，德國兩家大學醫院）：「**Skull base meningiomas had significantly lower global Ki-67 PI compared to convexity meningiomas**, also when stratified for WHO grade.」[A-S38]

**整體症狀組成（腦膜瘤，帶百分比）**[A-S13]
頭痛 33.3–36.7%；局部顱神經缺損 28.8–31.3%；癲癇 16.9–24.6%；認知改變 14.4%；無力 11.1%；眩暈／頭暈 9.8%；步態失調 6.3%；疼痛／感覺改變 5.6%；眼球突出 2.1%；昏厥 1.0%；**無症狀 9.4%**。
70 歲以上另有：感覺運動缺損 38.3%、認知障礙 28.8%[A-S13]。
「Skull base meningiomas present more often with neurological deficits and **non-skull base meningiomas are more likely to present with seizures**」[A-S13]。

**位置 → 症狀（腦膜瘤，逐條可引，全部出自 [A-S13]）**

- **前顱窩（前大腦鐮、嗅溝、眶額）**：診斷時常已很大；**視力受損 54%、頭痛 48%、嗅覺喪失（anosmia）40%、癲癇 20%**，加上精神運動症狀與「behavioral disturbance with personality disintegration」。
- **前大腦鐮**：漸進性人格改變伴淡漠與失智，常有長期頭痛史與視神經萎縮。
- **矢狀竇旁**：可以長到相當大才出現症狀；多以**下肢的傑克遜癲癇（Jacksonian seizures）**或頭痛表現；進展期的前矢狀竇旁腦膜瘤特徵性地出現**視乳突水腫與同向性偏盲**。
- **鞍結節（tuberculum sellae）**：「usually present with **insidious unilateral visual loss**, followed by **scotomatous defects in the other eye**」——**注意：是先單眼慢慢視力下降、再另一眼出現暗點，不是典型的雙顳側偏盲**。
- **鞍上（suprasellar）**：可能只表現輕微的荷爾蒙異常。
- **外側蝶骨嵴**：「often present with **painless unilateral exophthalmos**（無痛的單側眼球突出），followed by unilateral loss of vision」。
- **顳葉**：常以癲癇表現。
- **岩斜區**：步態失調與顱神經病變，例如**三叉神經受損**。
- **前床突（clinoidal）**：各式視覺障礙、顱神經麻痺、眼球突出。
- **後顱窩**：可造成阻塞性水腦，表現為**視乳突水腫與清晨頭痛**。
- **竇匯周圍（peritorcular）**：枕葉或小腦受壓——枕部局部疼痛的頭痛、視乳突水腫、同向性視野缺損，以及失調、辨距不良、肌張力低下、眼球震顫。
- **脊髓**：最常在**胸椎**，表現為**緩慢進展的痙攣性輕癱**，可伴或不伴神經根痛或夜間痛；**頸椎與顱頸交界**是第二常見，表現為痙攣性四肢輕癱，可伴低位延髓症狀。
- **貼近骨頭者**：局部骨質增生（hyperostosis）——「almost invariably a sign of bone invasion by meningioma cells」，可造成骨頭隆起與局部疼痛。
- **自發性出血**：罕見，<30 歲與 >70 歲較多；整體死亡率 21%，手術修補前無法恢復意識者死亡率 75%。

**聽神經瘤：內耳道與小腦橋腦角**
- 解剖二分法本身就是分類基礎：丹麥全國世代把腫瘤分成 **intrameatal（內耳道內）** 與 **extrameatal（延伸到小腦橋腦角）**，兩者的生長機率完全不同（見 A4）[A-S16]。
- 症狀入口：CNS 2018 指引處理的三種臨床狀況是**不對稱感音神經性聽損、不對稱耳鳴、突發性感音神經性聽損**[A-S23]。
- 診斷門檻（**逐字**）：「On the basis of an audiogram, it is recommended that MRI screening on patients with **≥10 dB of interaural difference at 2 or more contiguous frequencies or ≥15 dB at 1 frequency** be pursued to minimize the incidence of undiagnosed vestibular schwannomas. However, selectively screening patients with **≥15 dB of interaural difference at 3000 Hz alone** may minimize the incidence of MRIs performed that do not diagnose a vestibular schwannoma.」（Level 3）[A-S23]
- **產出率的誠實面**：不對稱耳鳴做 MRI「is low yielding in terms of vestibular schwannoma diagnosis (**<1%**)」；突發性感音神經性聽損做 MRI「**<3%**」[A-S23]。**這兩個數字要寫——它們同時支持「該查」與「查到的機率其實不高」。**
- 內耳道外側受侵犯的程度會影響顏面神經與聽力結果，「should be emphasized when interpreting imaging for preoperative planning」[A-S22]。
- 小腦橋腦角不是只有聽神經瘤：腦膜瘤 2–11% 長在小腦橋腦角[A-S13]，表皮樣囊腫也長在那裡[A-S34]——**A3 要講「同一個位置，好幾種瘤」**。

**腦下垂體腺瘤：視交叉壓迫與海綿竇侵犯**[A-S39]
- 生長方向與後果（Melmed 2022, *Endocrine Reviews*，OA 全文，逐條）：
  - 「**Superior growth is the most common**, as the diaphragm sella and its opening are a weak barrier to expansion. **Tumors may compress and damage the optic nerves and chiasm**; with a **postfixed chiasm**, the tumor may grow forward to the subfrontal area, whereas with a **prefixed chiasm**, growth is backward to the third ventricle and hypothalamus.」
  - 「**Inferior growth** produces sellar remodeling, enlargement, and bone resorption, leaving a free path for sphenoid sinus spread.」可再延伸到鼻咽或鼻腔。
  - 「**Anterior growth** encroaches the planum sphenoidale, inferior surfaces of the frontal lobes, and ethmoid sinuses. **Posterior growth** produces expansion to the interpeduncular cistern and brainstem. **Lateral growth** may be either by expansion into or infiltration of the **cavernous sinuses**.」
  - 侵襲的比例：「**Up to 35% of adenoma types exhibit gross invasion**, with macroadenomas showing higher rates.」
  - 海綿竇內側壁「varies in structural thickness or defects」，所以腫瘤可能侵入、內陷或延伸進海綿竇。
- **「雙顳側偏盲」這四個字本次未在可取得的全文裡逐字找到** → 寫作者**只能寫「向上長會壓到視神經與視交叉、造成視野缺損」並引 [A-S39]，不可以自行補上「雙顳側偏盲」這個專有名詞的機轉解釋**，或由 D 組另找來源。（記為 gap-A3-1）
- 病人端最常報告的症狀（瑞典 654 人）：**非功能性腺瘤是頭痛與視覺障礙；泌乳素瘤是月經不規則與頭痛；肢端肥大症是外觀改變與打鼾；庫欣氏病是體重增加與疲倦**[A-S32]。
- Endocrine Society 2011：病灶**貼到或壓到視神經／視交叉**時要做視野檢查，追蹤期間每 6 個月與每年各做一次[A-S25]。

### 反方向的資料（誠實必列）

- **位置不是唯一決定因素**：同一部位的腦膜瘤可以是不同分級，顱底以 grade 1 為主但不是全部[A-S13]；EANO 明講分級與臨床病程有相當的個體落差[A-S12]。
- **「不對稱聽損就有聽神經瘤」是錯的**：不對稱耳鳴的產出率 <1%，突發性聽損 <3%[A-S23]。
- 腦膜瘤有 9.4% 在診斷時是無症狀的[A-S13]——位置再典型，也有人什麼感覺都沒有。

### Claim ceiling

**可寫**
- 腦膜瘤的部位分布區間（照抄區間，標明是綜述彙整的區間）[A-S13]。
- 上表每一條位置 → 症狀的對應，**逐條引 [A-S13]**；腦下垂體的生長方向與後果逐條引 [A-S39]。
- 「顱底以 grade 1 為主，凸面／矢狀竇旁／大腦鐮／竇匯／腦室內較多高分級」[A-S13]；「顱底腦膜瘤的 Ki-67 顯著低於凸面，且在同一 WHO 分級下仍成立」[A-S38]。
- 「不對稱聽損要不要做 MRI」的聽力圖門檻逐字引[A-S23]，**同時寫產出率**。
- 「小腦橋腦角這個位置不是只有聽神經瘤」[A-S13][A-S34]。

**不可寫**
- ❌ 任何沒有來源、由解剖推導出來的症狀對應（例如自行寫「長在運動區就會手腳無力」）。
- ❌ 「雙顳側偏盲」作為腦下垂體瘤的典型表現（gap-A3-1，本 brief 無逐字來源）。
- ❌ 把腦膜瘤的部位—症狀對應套到聽神經瘤或腦下垂體瘤上。
- ❌ 把區間寫成單一數字（例如把「凸面 20–37%」寫成「約三成」）。
- ❌ 用「位置比大小重要」推導出「所以大小不用管」——Islim 2019 的資料裡直徑 ≥3 cm 是出現症狀的相關因子[A-S7]，IMPACT 模型裡腫瘤體積增加是預後參數（HR 2.17，95% CI 1.53–3.09）[A-S9]。**標題是修辭，不是結論。**

### Caveats

- Ogasawara 2021 是**綜述**，其部位比例與症狀百分比是彙整自更早的來源（綜述自己標為 [2,96,97,98,101,102] 等）。正文可以引，但要寫成「一篇彙整多個系列的綜述」，不可寫成單一研究[A-S13]。
- 前顱窩腦膜瘤的「視力受損 54%、嗅覺喪失 40%」來自診斷時已經很大的族群——**不可外推到偶然發現的小腦膜瘤**[A-S13]。
- 脊髓腦膜瘤在 CBTRUS 是另一個部位碼（脊膜 C70.1，AAAIR 0.40）[A-S15]，本篇提到脊髓時要標明。

### 台灣端（A3）

- 「單側聽力變差什麼時候該安排影像」在台灣有逐字的審查條文可引。《全民健康保險醫療費用審查注意事項》編號 **100901030「耳科病人有下列臨床狀況時，可予以適度安排 CT 或 MRI Study」**（106/8/1）[A-S44]，逐字十項：
  1. ABR 懷疑耳蝸後病變 retrocochlear lesion。
  2. **單側聽損 PTA 2-4k loss 大於 65 dB。**
  3. Poor SDS (not compatible with SRT)，或有 rollover 現象者。
  4. Neurological focal sign present, trigeminal neuralgia, facial numbness, or hemi-facial spasm。
  5. 先天性聽損懷疑有 cochlear nerve deficiency。
  6. **脈動性耳鳴 Pulsatile tinnitus。**
  7. Any unusual vertigo pattern or central nystagmus pattern。
  8. 懷疑乳突、內耳迷路、岩骨部或顱內感染者。
  9. 懷疑其他耳內良性、惡性腫瘤，如 ear cancer, **facial nerve schwannoma**, glomus tumor, cholesterol granuloma etc。
  10. Suggestion from referring neurologist/neurosurgeon。
- **這一條非常有用**：它是台灣制度上「什麼樣的單側聽力問題，醫師可以幫你安排影像」的官方文字。**但要注意它的門檻（PTA 2-4k 單側損失 >65 dB）比 CNS 指引的 ≥10–15 dB 差值寬鬆得多——兩者並陳，不可混用，也不可寫成「台灣比較嚴」或「台灣比較鬆」的評價。**
- 腦部 MRI 的一般審查原則見 A1 台灣端[A-S44]；支付項目 33084B／33085B[A-S43]。
- gap：本 brief 未查台灣的聽力檢查（純音聽力檢查、ABR）給付項目與助聽器補助（SPEC §八 有列，但屬 C 組）。

### 給繪圖組的數字（圖 3 `fig-bt-where`）

一張解剖示意，三種瘤共用，**但每個標註都要帶瘤別**：
- 腦膜瘤部位分布：凸面 20–37%、矢狀竇旁 13–22%（大腦鐮 5%）、顱底 43–51%（前顱底 10–20%、蝶骨嵴與中顱窩 9–36%、後顱窩 6–15%、小腦橋腦角 2–11%）、脊髓 7–12%、腦室內 1–5%[A-S13]
- 每個位置掛一句症狀（逐條照上表，引 [A-S13]）
- 聽神經瘤：內耳道內 vs 延伸到小腦橋腦角（兩個框，因為 A4 的生長機率不同）[A-S16]
- 腦下垂體：向上（壓視神經與視交叉）、向下（蝶竇）、向前（蝶骨平台／額葉下方／篩竇）、向後（腳間池／腦幹）、向側（海綿竇）；「Up to 35% 有肉眼可見的侵襲」[A-S39]
- 圖腳註必寫：**這是位置與症狀的對應，不是診斷工具；同一個位置可以長不同的瘤（例如小腦橋腦角有腦膜瘤、聽神經瘤、表皮樣囊腫）。**

---

## A4 `bt-watch`〈先觀察也是一種處置〉【紅線 2，雙向】

### Key facts

#### 一、腦膜瘤

**指引的追蹤時程（逐字）**[A-S12]
> 「Currently, by consensus, **annual MRI scans are recommended in suspected meningiomas or meningiomas of WHO grade 1 for 5 years. Thereafter, intervals can be doubled** (good practice point).」

EANO 同段也寫：「A significant proportion of meningiomas, notably in patients that are **asymptomatic or elderly or both**, may be managed by a **watch-and-scan** strategy.」[A-S12]

**生長速率與量法（紅線 2 的核心，每一筆都標量法）**

| 研究 | 設計與 n | **量法** | 結果 |
|---|---|---|---|
| Behbahani 2019[A-S11] | 前瞻，64/70 連續個案，偶然發現腦膜瘤，0／0.5／1／1.5／2／3／4／5 年定點評估 | **體積（GammaPlan 體積分析＋混合線性回歸）；「生長」＝體積變化 >15%** | **48 顆（75%）增大、13 顆（20.3%）不變、3 顆（4.7%）縮小**；平均到生長的時間 2.2 年（0.5–5.0 年）；生長型態：quasi-exponential 26%、linear 17%、**sigmoidal 35%**、parabolic 17%、continuous reduction 5%；**>60% 呈自限性生長**；**5 年內沒有任何人出現腫瘤相關症狀**；生長速率與較大的基線體積（p<0.001）及年齡相關（<55 歲 0.10 cm³/年、55–75 歲 0.24、>75 歲 **0.85**） |
| IMPACT 外部驗證 2026[A-S10] | 回溯世代，33 中心 15 國，1,248 人／1,010 顆未治療腦膜瘤，中位追蹤 61 個月 | 複合終點：**生長＋症狀發生＋腦膜瘤相關死亡＋失去可治癒時機** | **5 年無惡化 88.1%（85.8–90.5）、10 年 85.7%（83.2–88.2）**；114 顆（11.3%）惡化、132 顆（13.1%）接受介入；**383 人（40.5%）死於非腦膜瘤原因且未惡化未介入** |
| Islim 2019 統合分析[A-S7][A-S8] | 20 篇、2,130 人，加權平均追蹤 49.5 個月 | **各研究量法不一致，作者明講無法合併生長數據** | 主動監測者出現症狀 **8.4%（2.8–16.7）**（勘誤後）；監測後接受介入 **24.8%（7.5–48.0）**，到介入的加權平均時間 24.8 個月；「**Most patients who clinically or radiologically progressed did so within 5 years of diagnosis.**」 |

**預測生長的因子——兩套彼此不完全一致的答案，必須並陳**

- **IMPACT 預後模型（Islim 2020，441 人／459 顆，中位追蹤 55 個月）**[A-S9]：模型參數為
  - **腫瘤體積增加 HR 2.17（95% CI 1.53–3.09）**
  - **腦膜瘤（T2）高訊號 HR 10.6（95% CI 5.39–21.0）**
  - 腫瘤周圍訊號變化 HR 1.58（95% CI 0.65–3.85）→ **CI 跨 1**
  - 鄰近重要神經血管構造 HR 1.38（95% CI 0.74–2.56）→ **CI 跨 1**
  - 分成低／中／高風險，**5 年疾病惡化率 3%／28%／75%**；「**After 5 years of follow-up, the risk of disease progression plateaued in all groups.**」
  - 計算器網址（EANO 指引內載明）：`https://www.impact-meningioma.com`[A-S12]
- **Islim 2019 統合分析的勘誤把 T2 拿掉了**：「**T2 and peritumoral signal are no longer prognostic factors** on simple pooled and IPD analyses respectively.」[A-S8]
- **EANO 引述的另一個世代（Lee 等，232 人，1997–2013 前瞻追蹤未治療）**[A-S12]：59 顆（25.4%）**快速生長**；預測因子為腫瘤大小（**OR per cm³ 1.07，P=.000**）、**沒有鈣化（OR 3.87，P=.004）**、**腫瘤周圍水腫（OR 2.74，P=.025）**、**T2 高訊號或等訊號（OR 3.76，P=.049）**。（**這筆是透過 EANO 指引全文取得的二手轉述，引用時要標「EANO 指引轉述的一個 232 人世代」，本 brief 未直接核對其原始論文 → 見 FAIL-3**）
- **正確寫法**：「鈣化、T2 訊號這些影像特徵被用來預測會不會長，但不同研究給的答案不一樣——一個 441 人的模型裡 T2 高訊號的風險比高達 10.6，同一批作者的統合分析勘誤卻把 T2 從預後因子裡拿掉了。這是一個還在動的題目。」

**什麼情況停止觀察（改為處置）**
- EANO：「The primary treatment for the majority of **symptomatic or enlarging** meningiomas is surgery.」[A-S12]
- Islim 2019：主動監測期間出現症狀的相關因子是腫瘤周圍水腫與直徑 ≥3 cm（CI 極寬）[A-S7]。

**什麼情況停止追蹤（這題查得到，不是 gap）**
- **時程**：EANO 的 5 年年度掃描、之後間隔可加倍[A-S12]；Islim 2019「多數惡化發生在診斷後 5 年內」[A-S7]；IMPACT「5 年之後所有風險組的惡化風險都進入平台」[A-S9]。
- **年齡與共病（可直接引的兩句）**：
  - Islim 2020：「Patients with an **age-adjusted Charlson comorbidity index ≥6**（例：一位 80 歲合併慢性腎病的病人）**were 15 times more likely to die of other causes than to receive intervention at 5 years** following diagnosis, regardless of risk group.」結論句：「the model shows that **there is little benefit to rigorous monitoring in low-risk and older patients with comorbidities**. Risk-stratified follow-up has the potential to **reduce patient anxiety** and associated health care costs.」[A-S9]
  - IMPACT 外部驗證 2026：「Patients with an **age-adjusted Charlson Comorbidity Index score of 6 or higher**（例：80 歲、第 2 型糖尿病、曾心肌梗塞）**and a performance status of 2 to 4**（無法從事任何工作活動，或一天有一半以上時間臥床或坐著）were more likely to die of other causes than to receive intervention following diagnosis.」結論：IMPACT 工具可用來把病人分流為**早期介入、連續監測、或安全從門診結案（safe discharge from outpatient care）**[A-S10]。
- **「連續幾年無變化就可以停」的明確年數**：**gap**。指引只寫「5 年後間隔可加倍」，沒有寫停止年限[A-S12]。**正文不可自行訂年數。**

#### 二、聽神經瘤（前庭神經鞘瘤）

**指引的追蹤時程（逐字）**[A-S22]
> Question 3：What is the expected growth rate of vestibular schwannomas on MRI, and how often should they be imaged if a "watch and wait" philosophy is pursued?
> **Recommendation Level 3: MRIs should be obtained annually for 5 yr, with interval lengthening thereafter with tumor stability.**

同指引另兩條可引：追蹤用的序列應為「contrast-enhanced 3-D T1 MPRAGE 或 high-resolution T2（CISS／FIESTA）」（Level 3）；**囊性聽神經瘤**要被告知「may more often be associated with **rapid growth**, lower rates of complete resection」（Level 3）[A-S22]。

**wait-and-scan 的世代資料（量法：線性最大徑，>2 mm 算生長）**[A-S16]
- 丹麥全國、前瞻、未經選擇的世代，1976–2015，3,637 例散發性聽神經瘤；其中 **2,312 人接受觀察**，平均追蹤 7.33 年。
- **生長定義逐字**：「>2 mm by **linear measurement**, in accordance with the **Tokyo 2001 consensus-meeting** recommendations」。
- **434 人（19%）**在觀察期間因腫瘤生長轉為積極治療（內耳道內 102 人、外耳道外 332 人）。
- **診斷後 5 年：內耳道內腫瘤 21% 曾生長，外耳道外 37%；10 年：內耳道內 25%、外耳道外 42%。**
- 「Tumor growth occurred **mainly within the first 5 years** post diagnosis.」
- 生長之後：內耳道內腫瘤多半**繼續觀察**，外耳道外多半接受手術。

**「長了」不等於「會一直長」**[A-S18]
- Marinelli 2021，4 個轉診中心（美國與丹麥），3,402 位觀察中的病人裡 592 位符合條件（已有兩次 MRI 顯示線性生長 ≥2 mm 且仍繼續觀察）。
- 內耳道內（n=65）：初次偵測到生長之後的 1／2／3／4／5 年**無後續生長（再 ≥2 mm）存活率 77%／53%／46%／34%／32%**。
- 延伸到小腦橋腦角（n=527）：**72%／47%／32%／26%／22%**。
- 初次生長的幅度每多 1 mm，後續再生長的 HR：內耳道內 1.64（1.25–2.15，p<0.001）、小腦橋腦角 1.08（1.01–1.15，p=0.02）。
- 作者結論逐字：「**Growth detected during observation does not necessarily portend future growth**, especially for slowly growing tumors. Because early treatment does not confer improved long-term quality of life outcomes, **toleration of some growth during observation is justifiable in appropriately selected cases.**」

**觀察期間聽力會下降——紅線 5 與紅線 2 都要求不可省的一段**

- **Kirchmann 2017（Neurosurgery，156 位內耳道內聽神經瘤、保守處置、平均追蹤 9.5 年）**[A-S17]：
  - 腫瘤生長 37%；長入小腦橋腦角 23%；**保守處置失敗 15%**。
  - **純音平均聽閾（PTA）從 51 dB HL 上升到 72 dB HL；語音辨識分數（SDS）從 60% 下降到 34%。**
  - **好聽力（SDS >70%）的人從 52% 降到 22%；AAO-HNS A 級聽力從 19% 降到 3%。**
  - **同一群人、兩種定義、兩個答案**：可用聽力（serviceable hearing）保存率 **AAO-HNS（A–B 級）34%**，**word recognition score（I–II 級）58%**。
  - 診斷時 SDS 100% 者聽力保存明顯較好；**腫瘤有生長者聽力下降較快**。
- **Reznitsky & Cayé-Thomasen 2019 系統性回顧（15 篇、2,142 人，AAO-HNS 分級）**[A-S20]：**平均 5 年觀察後，診斷時有好聽力者 50% 仍保有好聽力；可用聽力保存率 54%**；診斷時語音辨識正常者保存得非常好。
- **CNS 2018 聽力保存指引（Level 3，觀察組）**[A-S24]：
  - Q7（所有觀察者）：2 年 **>75%–100%**、5 年 **>50%–75%**、10 年 **>25%–50%**。
  - Q8（基線 AAO-HNS A 級或 Gardner-Robertson I 級者）：2 年 >75%–100%、5 年 >50%–75%；**10 年資料不足**。
  - Q9：觀察期間維持可用聽力最一致的預測因子是「good preoperative word recognition and/or pure tone thresholds…as well as **nongrowth of the tumor**」；**診斷時的腫瘤大小、年齡、性別都不能預測**。

#### 三、腦下垂體腺瘤

**指引的追蹤時程（逐字）**[A-S25]
> 「We recommend that patients with incidentalomas **not meeting criteria for surgical removal** be followed with clinical assessments, neuroimaging (**magnetic resonance imaging at 6 months for macroincidentalomas, 1 yr for a microincidentaloma, and thereafter progressively less frequently if unchanged in size**), **visual field examinations for incidentalomas that abut or compress the optic nerve and chiasm (6 months and yearly)**, and **endocrine testing for macroincidentalomas (6 months and yearly)** after the initial evaluations.」

**自然病程（非功能性腺瘤與偶然瘤，量法：各研究定義的「病灶進展」，以人年為分母）**[A-S27]
- Fernández-Balsells 2011（JCEM 系統性回顧與統合分析，11 篇單世代研究，追蹤 3–15 年）：
  - **大腺瘤生長 12.5／100 人年（95% CI 7.9–17.2）**
  - **實質性病灶 5.7／100 人年（2.3–9.2）**
  - **微腺瘤 3.3／100 人年（2.1–4.5）**
  - **囊性病灶 0.05／100 人年（0.0–0.2）**
  - **垂體中風與視野缺損惡化都很罕見**；新發生內分泌功能異常整體 **2.4／100 人年（0.0–6.4）**。
  - 作者自己的限制：「The majority of these analyses were associated with **significant heterogeneity**…The quality of the evidence (risk of bias) was **very low**.」結論句：「PIs/NFPAs seem to have fairly rare complications that **may be more common when lesions are large (>10 mm) and solid**.」
- **停止追蹤的條件**：指引只寫「如果大小沒變，之後逐步拉長間隔（progressively less frequently if unchanged in size）」，**沒有給停止年限**[A-S25] → **gap，正文不可自行訂。**

### 反方向的資料（誠實必列）

1. **觀察不是零成本（聽神經瘤）**：Kirchmann 的 PTA 51→72 dB、SDS 60%→34%、AAO-HNS A 級 19%→3%[A-S17]；CNS 指引觀察組 10 年可用聽力只剩 >25%–50%[A-S24]。**這一段不可省（紅線 5），否則「先觀察」會被讀成免費。**
2. **體積量法下腦膜瘤多數會長大**：Behbahani 75%[A-S11]。
3. **年紀越大長得越快（腦膜瘤，體積速率）**：>75 歲 0.85 cm³/年 vs <55 歲 0.10 cm³/年[A-S11]——**但同一批高齡病人也最可能死於別的原因**[A-S9][A-S10]。兩件事要放同一段。
4. **觀察期間會有人轉治療**：腦膜瘤 24.8%[A-S7]；聽神經瘤丹麥世代 19%[A-S16]；內耳道內聽神經瘤 10 年保守處置失敗 15%[A-S17]。
5. **「長了」也未必要立刻動**：Marinelli 的後續生長率[A-S18]——但那是在**適當選擇的病人**身上，原文寫的是「in appropriately selected cases」，不可去掉這個限定。

### Claim ceiling

**可寫**
- 三種瘤各自的指引追蹤時程，**逐字引、分開寫**：腦膜瘤「年度 MRI 5 年、之後間隔可加倍」[A-S12]；聽神經瘤「年度 MRI 5 年、之後在穩定的前提下拉長間隔」[A-S22]；腦下垂體「大腺瘤 6 個月、微腺瘤 1 年，之後若大小不變逐步拉長；貼到或壓到視路者另做視野檢查（6 個月與每年）；大腺瘤另做內分泌檢查（6 個月與每年）」[A-S25]。
- 腦膜瘤的生長數據，**每一筆都標量法**[A-S11][A-S10][A-S7]。
- 聽神經瘤的生長機率**分內耳道內與外耳道外**，並標明「生長＝線性最大徑增加 >2 mm（Tokyo 2001 共識）」[A-S16]。
- 聽神經瘤觀察期間的聽力下降數字，**標明用哪一種聽力定義**（AAO-HNS 34% vs word recognition 58%，同一群人）[A-S17]。
- 腦下垂體的生長率**分大腺瘤／微腺瘤／實質／囊性**，單位是每 100 人年[A-S27]。
- 「什麼情況停止觀察」：腦膜瘤有症狀或正在長大[A-S12]；聽神經瘤生長後多數外耳道外者接受手術、內耳道內者多繼續觀察[A-S16]；腦下垂體照 Endocrine Society 的手術清單[A-S25]。
- 「什麼情況可以放鬆或停止追蹤」：5 年後風險進入平台[A-S9]；年齡校正 Charlson ≥6 者死於其他原因的機率是接受介入的 15 倍[A-S9]；Charlson ≥6 且體能狀態 2–4 者可考慮從門診結案[A-S10]。**寫的時候一定要加「這是醫師用工具分層之後的決定，不是你自己可以決定的事」。**

**不可寫**
- ❌「觀察＝什麼都不做」（紅線 2）。
- ❌「反正都會觀察」——三種瘤的時程與門檻不同，上面三行指引就是證據[A-S12][A-S22][A-S25]。
- ❌ 生長速率寫成保證（例如「腦膜瘤一年長 0.24 cm³」）。Behbahani 的生長型態有五種，其中 35% 是 S 型、17% 是拋物線型[A-S11]——**線性外推是錯的**。
- ❌ 沒標量法的生長比例（紅線 2 明文）。
- ❌ 把聽神經瘤觀察組的聽力保存率寫成單一數字而不標定義（34% 還是 58% 取決於用哪一把尺）[A-S17]。
- ❌ 自行訂「幾年沒變就可以不用追」——指引沒寫（gap）。
- ❌ 任何可以被讀成「你可以自己決定不回診」的句子。

### Caveats／safety notes

- **CNS 2018 指引的所有相關建議都是 Level 3**（最低證據等級），指引自己在執行摘要寫「a number of well-designed questions and subsequent searches did not yield information that allowed creation of a meaningful and justifiable recommendation」[A-S36]。EANO 的追蹤間隔是 **good practice point（共識），不是試驗結果**[A-S12]。**這兩件事要寫出來。**
- CNS 2026 的影像指引更新版已經出版（Neurosurgery 2026;98(2):283–287），但**其具體建議內文在摘要中取不到（見 FAIL-2）**，所以正文引的是 2018 版，並應加一句「這份指引在 2026 年有更新版，我引的是我能取得原文的 2018 版」。
- Fernández-Balsells 的證據品質作者自評「very low」[A-S27]；IMPACT 的外部驗證是**回溯性**世代[A-S10]。
- Behbahani 只有 64 人、單中心、且作者自己標為 level-2 evidence[A-S11]。

### 台灣端（A4）

- **腦部 MRI 追蹤的健保條文**：支付標準本文無腫瘤別條件（33084B／33085B）[A-S43]；《審查注意事項》有「十二週內再次執行須敘明必要性」等一般原則，但**沒有任何腦膜瘤／聽神經瘤／腦下垂體腺瘤的追蹤頻次條文（全文檢索零筆）**[A-S44] → **gap，正文寫「查不到列項，問醫務課／個管師」，永不推論。**
- **台灣的「觀察 vs 處置」受給付條文影響**：37028B／37029B 的立體定位放射手術，適應症雖含腦膜瘤、聽神經瘤、腦下垂體瘤、顱咽管瘤，但**必須同時符合「曾開顱有殘餘或復發／開顱風險大／內科條件不適合侵入性手術或全身麻醉」等條件之一，且全部個案須事前專案向保險人申請**[A-S43]。**A4 可以寫這一句事實（它解釋了「為什麼台灣的第一步常常是觀察或手術，而不是直接放射手術」），但不得比較單次與分次、不得比較平台、不得評價這個給付條件好壞**（SPEC §一.4、§一.5.①、§六）。
- 良性腦瘤不在重大傷病項次、不在癌症登記（見 A1／A2 台灣端）[A-S40][A-S41][A-S42] → **「觀察期的門診與影像費用怎麼算」是讀者會問的實際問題，本篇只能寫「要問醫務課」，不可推論。**

### 給繪圖組的數字（圖 4 `fig-bt-watch`）

三條平行時間軸（**絕對不可合併**），每條標自己的量法：

**腦膜瘤**（量法：見各格）
- 指引：年度 MRI × 5 年 → 之後間隔可加倍（共識）[A-S12]
- 5 年疾病惡化率（IMPACT 風險分層）：低 3%／中 28%／高 75%[A-S9]；外部驗證 3.9%／24.2%／51.6%[A-S10]
- 5 年之後風險進入平台[A-S9]
- 體積量法：5 年內 75% 體積增加 >15%，但 >60% 是自限性，5 年內 0 人出現症狀[A-S11]
- 什麼情況改變決定：有症狀或正在長大[A-S12]

**聽神經瘤**（量法：線性最大徑 >2 mm，Tokyo 2001）
- 指引：年度 MRI × 5 年 → 穩定則拉長間隔（Level 3）[A-S22]
- 曾生長比例：5 年 內耳道內 21%／外耳道外 37%；10 年 25%／42%[A-S16]
- 觀察中轉治療：19%（丹麥全國 2,312 人）[A-S16]
- **聽力（同一群人、兩把尺）**：9.5 年後可用聽力保存 AAO-HNS 34%／word recognition 58%；PTA 51→72 dB；SDS 60%→34%；AAO-HNS A 級 19%→3%[A-S17]
- 生長之後不一定會繼續長：內耳道內 5 年無後續生長 32%、小腦橋腦角 22%[A-S18]

**腦下垂體腺瘤**（量法：各研究定義之病灶進展，每 100 人年）
- 指引：大腺瘤 MRI 6 個月、微腺瘤 1 年 → 大小不變則逐步拉長；貼／壓視路者視野檢查 6 個月與每年；大腺瘤內分泌檢查 6 個月與每年[A-S25]
- 生長率：大腺瘤 12.5／實質 5.7／微腺瘤 3.3／囊性 0.05（每 100 人年）[A-S27]
- 新發內分泌功能異常 2.4／100 人年；垂體中風與視野惡化罕見[A-S27]

**共用腳註（必寫）**：三種瘤的量法不同（體積 vs 最大徑 vs 每人年事件率），**數值不可互比**；追蹤間隔是專家共識或 Level 3 建議，不是隨機試驗結果。

---

## 來源清單

### PASS — 期刊與指引

- **[A-S1] PASS** Vernooij MW, Ikram MA, Tanghe HL, et al. **Incidental findings on brain MRI in the general population.** *N Engl J Med*. 2007;357(18):1821–1828. DOI 10.1056/nejmoa070972. PMID 17978290. isOpenAccess: N。
  Route: Europe PMC REST `EXT_ID:17978290`&resultType=core → 摘要含 n=2000、平均 63.3 歲、1.5 T、良性原發腫瘤 1.6%、動脈瘤 1.8%、無症狀梗塞 7.2%、無病理確認。
  **限制：全文非 OA，腦膜瘤與垂體腺瘤的個別百分比取不到（見 FAIL-1）。**
- **[A-S2] PASS** Bos D, Poels MM, Adams HH, et al. **Prevalence, Clinical Management, and Natural Course of Incidental Findings on Brain MR Images: The Population-based Rotterdam Scan Study.** *Radiology*. 2016;281(2):507–515. DOI 10.1148/radiol.2016160218. PMID 27337027. isOpenAccess: N。
  Route: Europe PMC REST `TITLE:"Incidental Findings on Brain MR Images" AND TITLE:"Rotterdam"` → 摘要含 n=5800、平均 64.9 歲、9.5%、腦膜瘤 2.5%（143/5800）、動脈瘤 2.3%、轉介 3.2%、其中 76.6% 觀察或結案、追蹤最長 9 年。
- **[A-S3] PASS** Morris Z, Whiteley WN, Longstreth WT, et al. **Incidental findings on brain magnetic resonance imaging: systematic review and meta-analysis.** *BMJ*. 2009;339:b3016. DOI 10.1136/bmj.b3016. PMID 19687093. PMCID PMC2728201. **isOpenAccess: Y**。
  Route: Europe PMC REST TITLE 檢索 → 摘要含 16 篇/19,559 人、腫瘤性 0.70%（0.47–0.98）、非腫瘤性 2.0%、NNS=37、高解析 4.3% vs 標準 1.7%（p<0.001）、結論句「not sufficient to justify screening healthy asymptomatic people」。
- **[A-S4] PASS** Hall WA, Luciano MG, Doppman JL, Patronas NJ, Oldfield EH. **Pituitary magnetic resonance imaging in normal human volunteers: occult adenomas in the general population.** *Ann Intern Med*. 1994;120(10):817–820. DOI 10.7326/0003-4819-120-10-199405150-00001. PMID 8154641. isOpenAccess: N。
  Route: Europe PMC REST TITLE 檢索 → 摘要含 100 位志願者（女 70/男 30，18–60 歲）、Gd-DTPA 高解析腦下垂體 MRI、10%/10%、病灶 3–6 mm、Cushing 對照組 PPV 86%。
- **[A-S5] PASS** Ezzat S, Asa SL, Couldwell WT, et al. **The prevalence of pituitary adenomas: a systematic review.** *Cancer*. 2004;101(3):613–619. DOI 10.1002/cncr.20412. PMID 15274075. isOpenAccess: N。
  Route: Europe PMC REST TITLE 檢索 → 摘要含整體 16.7%、解剖 14.4%、影像 22.5%。
- **[A-S6] PASS** Daly AF, Rixhon M, Adam C, et al. **High prevalence of pituitary adenomas: a cross-sectional study in the province of Liege, Belgium.** *J Clin Endocrinol Metab*. 2006;91(12):4769–4775. DOI 10.1210/jc.2006-1668. PMID 16968795. isOpenAccess: N。
  Route: Europe PMC REST TITLE 檢索 → 摘要含 68 例/71,972 人、94±19.3／10 萬（95% CI 72.2–115.8）、女 67.6%、平均診斷年齡 40.3 歲、大腺瘤 42.6%、泌乳素瘤 66%、非分泌 14.7%、生長激素瘤 13.2%、庫欣氏病 5.9%、hypopituitarism 20.6%、1/1064。
- **[A-S7] PASS** Islim AI, Mohan M, Moon RDC, et al. **Incidental intracranial meningiomas: a systematic review and meta-analysis of prognostic factors and outcomes.** *J Neurooncol*. 2019;142(2):211–221. DOI 10.1007/s11060-019-03104-3. PMID 30656531. PMCID PMC6449307. **isOpenAccess: Y**。
  Route: Europe PMC REST `TITLE:"incidental intracranial meningiomas"` → 摘要含 20 篇/2,130 人、手術 27.3%/SRS 22.0%/主動監測 50.7%、追蹤 49.5 月（SD 29.3）、症狀 8.1%（2.7–16.1）、水腫 OR 8.72、直徑 ≥3 cm OR 34.90、介入 24.8%（7.5–48.0）、到介入 24.8 月、grade I 94.0%、「Intervention at diagnosis may lead to unnecessary overtreatment」。
- **[A-S8] PASS（勘誤，必須與 [A-S7] 一起引）** Islim AI, Mohan M, Moon RDC, et al. **Correction to: Incidental intracranial meningiomas: a systematic review and meta-analysis of prognostic factors and outcomes.** *J Neurooncol*. 2019;144(2):427–429. DOI 10.1007/s11060-019-03237-5. PMID 31368055. PMCID PMC6700050. **isOpenAccess: Y**。
  Route: 同上 → 逐字：「**T2 and peritumoral signal are no longer prognostic factors**」；症狀發生更新為 575 人中 69 人、**8.4%（2.8–16.7）**、I²=88.9%；介入之分母 947。
- **[A-S9] PASS** Islim AI, Kolamunnage-Dona R, Mohan M, et al. **A prognostic model to personalize monitoring regimes for patients with incidental asymptomatic meningiomas.** *Neuro Oncol*. 2020;22(2):278–289. DOI 10.1093/neuonc/noz160. PMID 31603516. PMCID PMC7032634. **isOpenAccess: Y**。
  Route: Europe PMC REST TITLE 檢索 → 摘要含 441 人/459 顆、中位 55 月（IQR 37–80）、44 人惡化、57 人非腦膜瘤死亡、HR（體積 2.17、高訊號 10.6、周圍訊號 1.58、鄰近神經血管 1.38）、5 年惡化 3%/28%/75%、5 年後風險平台、Charlson ≥6 者 15 倍。
- **[A-S10] PASS** Islim AI, Millward CP, Zakaria R, et al.; IMPACT Study Investigators, ICOM, BNTRC. **A Clinical Tool to Identify Incidental Meningioma for Early Outpatient Management.** *JAMA Oncol*. 2026;12(1):66–74. DOI 10.1001/jamaoncol.2025.4821. PMID 41264316. isOpenAccess: N。
  Route: Europe PMC REST `EXT_ID:41264316` → 摘要含 33 中心/15 國、n=1,248、中位年齡 66（IQR 55–77）、女 80%、945 人/1,010 顆未治療、中位追蹤 61 月（IQR 17–108）、惡化 114 顆（11.3%）、介入 132 顆（13.1%）、非腦膜瘤死亡 383 人（40.5%）、5 年 PFS 88.1%（85.8–90.5）、10 年 85.7%（83.2–88.2）、風險組 3.9%/24.2%/51.6%、Brier 0.12、C-statistic 0.80、Charlson ≥6 且 PS 2–4。
- **[A-S11] PASS** Behbahani M, Skeie GO, Eide GE, Hausken A, Lund-Johansen M, Skeie BS. **A prospective study of the natural history of incidental meningioma—Hold your horses!** *Neurooncol Pract*. 2019;6(6):438–450. DOI 10.1093/nop/npz011. PMID 31832214. PMCID PMC6899048. inEPMC: Y（isOpenAccess: N）。
  Route: Europe PMC REST TITLE 檢索 → 摘要含 64/70 人、0–5 年定點、GammaPlan 體積分析、48 顆（75%）>15% 增大／13 顆（20.3%）不變／3 顆（4.7%）縮小、平均 2.2 年（0.5–5.0）、生長型態五分類、年齡分層速率、無人出現症狀、level-2 evidence。
- **[A-S12] PASS** Goldbrunner R, Stavrinou P, Jenkinson MD, et al. **EANO guideline on the diagnosis and management of meningiomas.** *Neuro Oncol*. 2021;23(11):1821–1834. DOI 10.1093/neuonc/noab150. PMID 34181733. PMCID PMC8563316. isOpenAccess: N，inEPMC: Y。
  Route: Europe PMC REST 取書目 → **全文自 `https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8563316/` 實際抓取（HTTP 200，301,816 bytes）**，本 brief 引用之逐字句（「Incidental meningiomas are present on brain MRI of 0.9% to 1.0%…」、Behbahani 轉述、Lee 232 人世代轉述、「annual MRI scans…for 5 years. Thereafter, intervals can be doubled」、「symptomatic or enlarging」、impact-meningioma.com、NCDB grade 2/3 存活）皆出自該全文。
  人類可讀頁：https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8563316/
- **[A-S13] PASS** Ogasawara C, Philbrick BD, Adamson DC. **Meningioma: A Review of Epidemiology, Pathology, Diagnosis, Treatment, and Future Directions.** *Biomedicines*. 2021;9(3):319. DOI 10.3390/biomedicines9030319. PMID 33801089. PMCID PMC8004084. **isOpenAccess: Y**。
  Route: Europe PMC REST → fullTextXML（243,356 chars）。本 brief 的部位分布表（Table 4）、整體症狀百分比、逐條位置→症狀、蛛網膜帽細胞起源、顱底 vs 凸面胚胎來源、grade 與部位關係、dural tail 72% 等皆出自該全文。
- **[A-S14] PASS** Price M, Ballard CAP, Benedetti JR, Kruchko C, Barnholtz-Sloan JS, Ostrom QT. **CBTRUS Statistical Report: Primary Brain and Other Central Nervous System Tumors Diagnosed in the United States in 2018-2022.** *Neuro Oncol*. 2025;27(Supplement_4):iv1–iv66. DOI 10.1093/neuonc/noaf194. PMID 41092086. isOpenAccess: N，**無 PMCID**。
  Route: Europe PMC REST `EXT_ID:41092086` → 摘要含 AAAIR 26.05（惡性 6.86／非惡性 19.19）、女 29.67 vs 男 22.23、gliomas 22.2%、GBM 13.7%/52.2%、**meningioma 42.6% of all tumors（含惡性腦膜瘤）與 57.4% of all non-malignant**、兒少 5.99、5 年相對存活惡性 34.8%／非惡性 91.7%。
  **與站上 `gb-what-it-is` 引用的 42.6% 一致，不需更正。**
- **[A-S15] PASS** Price M, Ballard C, Benedetti J, et al. **CBTRUS Statistical Report: Primary Brain and Other Central Nervous System Tumors Diagnosed in the United States in 2017-2021.** *Neuro Oncol*. 2024;26(Supplement_6):vi1–vi85. DOI 10.1093/neuonc/noae145. PMID 39371035. PMCID PMC11456825. isOpenAccess: N，inEPMC: Y。
  Route: 書目經 Europe PMC REST 核對；**全文表格自 `https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11456825/` 實際抓取（HTTP 200，1,023,221 bytes）**，本 brief 之腦膜瘤／腦下垂體／神經鞘瘤／顱咽管瘤細項、AAAIR、男女別、IRR、中位年齡 68、Table 1 的 ICD-O 碼對應、CBTRUS 與 NPCR/SEER 定義差異段落皆出自該全文。
  人類可讀頁：https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11456825/
- **[A-S16] PASS** Reznitsky M, Petersen MMBS, West N, Stangerup SE, Cayé-Thomasen P. **The natural history of vestibular schwannoma growth—prospective 40-year data from an unselected national cohort.** *Neuro Oncol*. 2021;23(5):827–836. DOI 10.1093/neuonc/noaa230. PMID 33068429. PMCID PMC8099466. inEPMC: Y。
  Route: Europe PMC REST `EXT_ID:33068429` → 摘要含 1976–2015、3,637 例、手術 1,304／放療 21／觀察 2,312（平均追蹤 7.33 年）、434 人（19%）轉治療（內耳道內 102／外耳道外 332）、**生長定義「>2 mm by linear measurement, Tokyo 2001 consensus」**、5 年 21%/37%、10 年 25%/42%、「growth occurred mainly within the first 5 years」。
- **[A-S17] PASS** Kirchmann M, Karnov K, Hansen S, Dethloff T, Stangerup SE, Caye-Thomasen P. **Ten-Year Follow-up on Tumor Growth and Hearing in Patients Observed With an Intracanalicular Vestibular Schwannoma.** *Neurosurgery*. 2017;80(1):49–56. DOI 10.1227/neu.0000000000001414. PMID 27571523. isOpenAccess: N。
  Route: Europe PMC REST `EXT_ID:27571523` → 摘要含 n=156、平均追蹤 9.5 年、生長 37%、長入 CPA 23%、保守失敗 15%、PTA 51→72 dB HL、SDS 60%→34%、SDS>70% 52%→22%、AAO-HNS A 級 19%→3%、可用聽力 AAO-HNS(A–B) 34% vs word recognition(I–II) 58%、生長者聽力下降較快。
- **[A-S18] PASS** Marinelli JP, Carlson ML, Hunter JB, et al. **Natural History of Growing Sporadic Vestibular Schwannomas During Observation: An International Multi-Institutional Study.** *Otol Neurotol*. 2021;42(8):e1118–e1124. DOI 10.1097/mao.0000000000003224. PMID 34121081. isOpenAccess: N。
  Route: Europe PMC REST `EXT_ID:34121081` → 摘要含 4 中心、3,402 觀察者中 592 符合、內耳道內 65／CPA 527、初次生長中位年齡 66/62 歲、後續無生長存活率（IC 77/53/46/34/32%；CPA 72/47/32/26/22%）、HR 1.64／1.08、結論「Growth detected during observation does not necessarily portend future growth…in appropriately selected cases」。
- **[A-S19] PASS** Reznitsky M, Petersen MMBS, West N, Stangerup SE, Cayé-Thomasen P. **Epidemiology Of Vestibular Schwannomas — Prospective 40-Year Data From An Unselected National Cohort.** *Clin Epidemiol*. 2019;11:981–986. DOI 10.2147/clep.s218670. PMID 31807080. PMCID PMC6850685. **isOpenAccess: Y**。
  Route: Europe PMC REST＋fullTextXML → 摘要含 3,637 例、年診斷數 14（1976）→193（2015）、平均外耳道外大小 26 mm→13.4 mm、診斷年齡中位 49.2→60 歲、發生率 3→34／百萬／年。
- **[A-S20] PASS** Reznitsky M, Cayé-Thomasen P. **Systematic Review of Hearing Preservation in Observed Vestibular Schwannoma.** *J Neurol Surg B Skull Base*. 2019;80(2):165–168. DOI 10.1055/s-0039-1679894. PMID 30931224. PMCID PMC6438797. inEPMC: Y。
  Route: Europe PMC REST `EXT_ID:30931224` → 摘要含 15 篇/2,142 人、AAO-HNS 分級、平均 5 年觀察後好聽力保存 50%、可用聽力保存 54%、診斷時語音辨識正常者保存最好。
- **[A-S21] PASS** Marinelli JP, Beeler CJ, Carlson ML, Caye-Thomasen P, Spear SA, Erbele ID. **Global Incidence of Sporadic Vestibular Schwannoma: A Systematic Review.** *Otolaryngol Head Neck Surg*. 2022;167(2):209–214. DOI 10.1177/01945998211042006. PMID 34464224. isOpenAccess: N。
  Route: Europe PMC REST `EXT_ID:34464224` → 摘要含 6 篇/4 個族群（丹麥、荷蘭、台灣、美國）、最新發生率 3.0–5.2／10 萬人年、≥70 歲峰值 20.6、**美國「無症狀、偶然診斷」1.3／10 萬人年（2012–2016）**、終生盛行率 >1/500、PROSPERO CRD42021228208。
- **[A-S22] PASS** Dunn IF, Bi WL, Mukundan S, et al. **Congress of Neurological Surgeons Systematic Review and Evidence-Based Guidelines on the Role of Imaging in the Diagnosis and Management of Patients With Vestibular Schwannomas.** *Neurosurgery*. 2018;82(2):E32–E34. DOI 10.1093/neuros/nyx510. PMID 29309686. isOpenAccess: N。
  Route: Europe PMC REST TITLE 檢索 → **摘要即為指引建議全文**，含 Q3 逐字「Level 3: MRIs should be obtained annually for 5 yr, with interval lengthening thereafter with tumor stability.」、追蹤序列（3-D T1 MPRAGE 或 CISS/FIESTA）、囊性腫瘤、內耳道外側受侵犯、NF2 影像、術後追蹤。
  指引官方頁：https://www.cns.org/guidelines/guidelines-management-patients-vestibular-schwannoma/chapter_5
- **[A-S23] PASS** Sweeney AD, Carlson ML, Shepard NT, McCracken DJ, Vivas EX, Neff BA, Olson JJ. **Congress of Neurological Surgeons Systematic Review and Evidence-Based Guidelines on Otologic and Audiologic Screening for Patients With Vestibular Schwannomas.** *Neurosurgery*. 2018;82(2):E29–E31. DOI 10.1093/neuros/nyx509. PMID 29309699. isOpenAccess: N。
  Route: Europe PMC REST `EXT_ID:29309699` → 摘要即建議全文，含 ≥10 dB/2 個相鄰頻率或 ≥15 dB/1 個頻率、3000 Hz 單頻 ≥15 dB、不對稱耳鳴 <1%、突發性感音神經性聽損 <3%。
  指引官方頁：https://www.cns.org/guidelines/guidelines-management-patients-vestibular-schwannoma/chapter_2
- **[A-S24] PASS** Carlson ML, Vivas EX, McCracken DJ, Sweeney AD, Neff BA, Shepard NT, Olson JJ. **Congress of Neurological Surgeons Systematic Review and Evidence-Based Guidelines on Hearing Preservation Outcomes in Patients With Sporadic Vestibular Schwannomas.** *Neurosurgery*. 2018;82(2):E35–E39. DOI 10.1093/neuros/nyx511. PMID 29309683. isOpenAccess: N。
  Route: Europe PMC REST TITLE 檢索 → 摘要即建議全文（Q1–Q9）。**A 組只用 Q7／Q8／Q9（觀察組）；Q1–Q6（放射手術與顯微手術的聽力保存）歸 C2，A 組不得引用比較。**
  指引官方頁：https://www.cns.org/guidelines/guidelines-manage-ment-patients-vestibular-schwannoma/chapter_3
- **[A-S25] PASS** Freda PU, Beckers AM, Katznelson L, et al.; Endocrine Society. **Pituitary incidentaloma: an endocrine society clinical practice guideline.** *J Clin Endocrinol Metab*. 2011;96(4):894–904. DOI 10.1210/jc.2010-1048. PMID 21474686. PMCID PMC5393422. **isOpenAccess: Y**。
  Route: Europe PMC REST TITLE 檢索 → 摘要即建議全文，含初評（病史／理學／荷爾蒙過度分泌與功能低下篩檢／視野）、追蹤間隔（大腺瘤 6 月、微腺瘤 1 年、之後逐步拉長；視野 6 月與每年；大腺瘤內分泌 6 月與每年）、轉手術清單（視野缺損／壓迫性視覺異常如眼肌麻痺／神經受壓／病灶貼到或壓到視神經與視交叉／垂體中風合併視覺障礙／泌乳素瘤以外的功能性腺瘤）。
- **[A-S27] PASS** Fernández-Balsells MM, Murad MH, Barwise A, et al. **Natural history of nonfunctioning pituitary adenomas and incidentalomas: a systematic review and metaanalysis.** *J Clin Endocrinol Metab*. 2011;96(4):905–912. DOI 10.1210/jc.2010-1054. PMID 21474687. isOpenAccess: N。
  Route: Europe PMC REST `DOI:"10.1210/jc.2010-1054"` → 摘要含 11 篇單世代、追蹤 3–15 年、大腺瘤 12.5／100 人年（7.9–17.2）、實質 5.7（2.3–9.2）、微腺瘤 3.3（2.1–4.5）、囊性 0.05（0.0–0.2）、新發內分泌異常 2.4（0.0–6.4）、垂體中風與視野惡化罕見、證據品質 very low。
- **[A-S28] PASS** Asa SL, Mete O, Perry A, Osamura RY. **Overview of the 2022 WHO Classification of Pituitary Tumors.** *Endocr Pathol*. 2022;33(1):6–26. DOI 10.1007/s12022-022-09703-7. PMID 35291028. isOpenAccess: N。
  Route: Europe PMC REST TITLE 檢索 → 摘要含「now classified as pituitary neuroendocrine tumors (PitNETs; formerly known as pituitary adenomas)」、前後葉分開、PIT1/TPIT/SF1/GATA3/ERα 轉錄因子、null cell 為排除性診斷、「metastatic PitNET」取代「pituitary carcinoma」。
- **[A-S29] PASS** Ho KKY, Gadelha M, Kaiser UB, Reincke M, Melmed S. **The NETting of pituitary adenoma: a gland illusion.** *Pituitary*. 2022;25(3):349–351. DOI 10.1007/s11102-022-01235-x. PMID 35616761. PMCID PMC9170656. **isOpenAccess: Y（CC BY 4.0）**。
  Route: Europe PMC REST → fullTextXML（28,565 chars）。逐字引語（dual nomenclature、1 in 2000／1 in 100,000、NE markers 非專一、無臨床相關組織分級、NANETS/Mayo 衛教連結、疾病標籤對決策與焦慮的影響、甲狀腺乳突癌改名的隨機試驗、Pituitary Society 2019 工作坊與「The IARC/WHO was unable to attend」）皆出自該全文。
- **[A-S30] PASS（僅書目，內文不可引）** Ho KKY, Fleseriu M, Wass J, et al. **A tale of pituitary adenomas: to NET or not to NET: Pituitary Society position statement.** *Pituitary*. 2019;22(6):569–573. DOI 10.1007/s11102-019-00988-2. PMID 31571098. isOpenAccess: N，摘要為 none。
  Route: Europe PMC REST `TITLE:"pituitary adenomas" AND TITLE:"NET"` → 書目核對通過，**摘要不存在，內文取不到 → 只能當「有一份正式立場聲明」的指路，不可引其內容。**
- **[A-S32] PASS** Forsgren M, Dahlgren C, Alkebro C, et al. **Estimating diagnostic delay in patients with pituitary adenomas in Sweden: a cross-sectional study.** *BMJ Open*. 2025;15(6):e097804. DOI 10.1136/bmjopen-2024-097804. PMID 40550723. PMCID PMC12186051. **isOpenAccess: Y**。
  Route: Europe PMC REST `EXT_ID:40550723` → 摘要含 7 家大學醫院、654 人（NFPA 314／泌乳素瘤 118／肢端肥大 164／庫欣氏病 58）、<1 年 66%／1–5 年 12%／5–9 年 13%／>10 年 9%、CD 與肢端肥大延遲最久、女性延遲較久（p<0.001）、各病別最常見的病人自述症狀、視覺障礙與月經不規則的 kappa。
- **[A-S33] PASS** Yin X, Duan H, Yi Z, Li C, Lu R, Li L. **Incidence, Prognostic Factors and Survival for Hemangioblastoma of the Central Nervous System: Analysis Based on the Surveillance, Epidemiology, and End Results Database.** *Front Oncol*. 2020;10:570103. DOI 10.3389/fonc.2020.570103. PMID 33014882. PMCID PMC7509109. **isOpenAccess: Y**。
  Route: Europe PMC REST `EXT_ID:33014882` → 摘要含整體發生率 0.141／10 萬人年、多變項 HR（60–79 歲 3.697、≥80 歲 12.318、多發腫瘤 1.715、曾手術 0.638）、手術組存活較佳。
- **[A-S34] PASS** Czernicki T, Kunert P, Nowak A, Wojciechowski J, Marchel A. **Epidermoid cysts of the cerebellopontine angle: Clinical features and treatment outcomes.** *Neurol Neurochir Pol*. 2016;50(2):75–82. DOI 10.1016/j.pjnns.2015.11.008. PMID 26969562. isOpenAccess: N。
  Route: Europe PMC REST `EXT_ID:26969562` → 摘要含 1994–2013、17 例、平均追蹤 126 個月、全切 5／不全切 12、切除程度與復發無關、症狀性復發平均 >9 年後（5 例）、結論「acceptable to leave tumor capsule fragments adhering closely to nerves, vessels, or brainstem」。
- **[A-S35] PASS（台灣）** Koo M, Lai JT, Yang EY, Liu TC, Hwang JH. **Incidence of Vestibular Schwannoma in Taiwan from 2001 to 2012: A Population-Based National Health Insurance Study.** *Ann Otol Rhinol Laryngol*. 2018;127(10):694–697. DOI 10.1177/0003489418788385. PMID 30032646. isOpenAccess: N。
  Route: Europe PMC REST `EXT_ID:30032646` → 摘要含 LHID2000、ICD-9-CM 225.1、須診斷前做過 MRI、≥20 歲、206 例、年發生率 2.66／10 萬（95% CI 2.32–3.05）、年間 1.74–3.72、60–69 歲最高 4.86。
- **[A-S36] PASS（僅用於「證據等級低」這一件事）** Olson JJ, Kalkanis SN, Ryken TC. **Congress of Neurological Surgeons Systematic Review and Evidence-Based Guidelines on the Treatment of Adults With Vestibular Schwannomas: Executive Summary.** *Neurosurgery*. 2018;82(2):129–134. DOI 10.1093/neuros/nyx586. PMID 29309649. isOpenAccess: N。
  Route: Europe PMC REST TITLE 檢索 → 摘要逐字「some level 2 recommendations and a greater number of level 3 recommendations」「a number of well-designed questions and subsequent searches did not yield information that allowed creation of a meaningful and justifiable recommendation」。
- **[A-S37] PASS** Millward CP, Islim AI, Armstrong TS, et al. **The outcomes measured and reported in observational studies of incidental and untreated intracranial meningioma: A systematic review.** *Neurooncol Adv*. 2024;6(1):vdae042. DOI 10.1093/noajnl/vdae042. PMID 38596715. PMCID PMC11003528. **isOpenAccess: Y**。
  Route: Europe PMC REST TITLE 檢索 → 摘要含 33 篇＋1 進行中 = 32 個獨立研究（回溯 27／前瞻 5）、268 個逐字結果、僅 77 個有定義、去重後 178 個、歸併為 53 個標準化詞、COMET 分類 9 個 domain／3 個 core area、結論「Outcome measurement…is heterogeneous」。
- **[A-S38] PASS** Broechner A, Maier AD, Mirian C, et al. **Analysis of anatomical location, mitoses, and Ki-67 in 2608 meningiomas.** *J Neuropathol Exp Neurol*. 2026;85(3):253–266. DOI 10.1093/jnen/nlaf131. PMID 41267161. isOpenAccess: N。
  Route: Europe PMC REST `EXT_ID:41267161` → 摘要含 n=2,608（Heidelberg 與 Mannheim）、「Skull base meningiomas had significantly lower global Ki-67 PI compared to convexity meningiomas also when stratified for WHO grade」、transitional 亞型增殖指數較高、hotspot 在高分級較常見。
- **[A-S39] PASS** Melmed S, Kaiser UB, Lopes MB, et al. **Clinical Biology of the Pituitary Adenoma.** *Endocr Rev*. 2022;43(6):1003–1037. DOI 10.1210/endrev/bnac010. PMID 35395078. PMCID PMC9695123. **isOpenAccess: Y**。
  Route: Europe PMC REST → fullTextXML（204,982 chars）。本 brief 的生長方向段落（superior/inferior/anterior/posterior/lateral、prefixed 與 postfixed chiasm、Up to 35% gross invasion、海綿竇內側壁厚度不一）、null cell 從 ~20% 降到 1–2%、侵襲性腺瘤約佔大腺瘤 2% 等皆出自該全文。

### PASS — 台灣官方

- **[A-S40] PASS** **癌症防治法**（民國 112 年 04 月 26 日修正）。第 3 條第 1 款：「癌症：係指經由病理切片證實，或經其他檢查、檢驗有效推定診斷，在臨床上具有再發或轉移現象之**惡性腫瘤**。」第 11 條：「為建立癌症防治相關資料庫，癌症防治醫療機構應向中央主管機關所委託之學術研究機構，提報下列資料：一、新發生之癌症個案與期別等相關診斷及治療資料…」
  Route: `curl https://law.moj.gov.tw/Law/LawSearchResult.aspx?ty=ONEBAR&kw=癌症防治法` → pcode **L0070008** → `curl https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=L0070008`（HTTP 200，54,711 bytes），逐字取自條文本文。
  人類可讀頁：https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=L0070008
- **[A-S41] PASS** **台灣癌症登記長表摘錄手冊（114 年 12 月正式版）**，台灣癌症登記中心（國民健康署委託）。
  逐字（個案的選擇／申報個案條件）：「收案對象為中華民國國籍（外籍人士不收案），第一次經醫師診斷為癌症之個案，亦即 **ICD-O-3 性態碼為 2、3、6、9 者**（若為 6、9 者，需申報原發部位，性態碼改為 3），均需申報。」
  逐字（「性態碼」欄位，欄位長度 1、**編碼範圍：2, 3**）：「病理醫師常使用 **benign(0)、borderline(1)**、in situ(2)、malignant, primary site(3)、malignant, metastatic site(6)、或 malignant, uncertain whether primary or metastatic site(9) 來描述腫瘤的性態。其中性態碼為 2、3、6 或 9（若為 6 或 9 者，須申報原發部位，且性態碼改為 3）的個案必須申報至癌症登記中心。」
  另（卵巢 borderline 表）：「無 intraepithelial carcinoma 亦無 microinvasive carcinoma｜性態碼 1｜是否申報：**否**」。
  Route: `curl https://twcr.tw/?page_id=1809` → PDF `https://twcr.tw/wp-content/uploads/2025/12/Longform-Manual_Official-version_20251224_W-1.pdf`（HTTP 200，5,120,704 bytes）→ `pdftotext -enc UTF-8`（736,459 bytes 文字）→ 逐字檢索。
  人類可讀頁（資料下載）：https://twcr.tw/?page_id=1809
- **[A-S42] PASS** **全民健康保險保險對象免自行負擔費用辦法**（民國 113 年 09 月 16 日修正）第 2 條＋**附表一「全民健康保險重大傷病項目及其證明有效期限」**。
  附表一「一、需積極或長期治療之癌症」子項與 ICD-10-CM 碼：(一)甲狀腺惡性腫瘤 C73（3 年）；(二)口腔、口咽及下咽惡性腫瘤第一期 C00.0-C06.9、C09.0-C10.9、C12-C14.8（3 年）；(三)乳房惡性腫瘤第一期 C50.011-C50.929（3 年）；(四)子宮頸惡性腫瘤第一期 C53.0-C53.9、C55（3 年）；(五)除(一)~(四)之其他惡性腫瘤 **C00.0-C96.9（不含 C73、C94.4、C94.6）**（5 年）。**113-12-31 以前適用版與 114-01-01 以後適用版皆同。**
  全表逐字檢索：**D32／D33／D35 零筆**。唯一相關項次為「十八、脊髓損傷或病變所引起之神經、肌肉、皮膚、骨骼、心肺、泌尿及腸胃等之併發症者（其身心障礙等級在中度以上者）」之「(三)其他脊髓病變 Other disease of spinal cord（G32.0、G95.0、G95.11-G95.89、G95.9、G99.2）」。另有「三十、經中央主管機關依罕見疾病防治及藥物法…公告之罕見疾病」（罕病名單本組未查）。
  Route: `curl https://law.moj.gov.tw/Law/LawSearchResult.aspx?ty=ONEBAR&kw=免自行負擔費用辦法` → pcode **L0060015** → `curl https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=L0060015`（HTTP 200）→ 附檔 `LawGetFile.ashx?FileId=0000375263&lan=C`（HTTP 200，433,100 bytes，application/pdf）→ pdftotext（2,424 行）→ 逐字檢索。
  人類可讀頁：https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=L0060015
- **[A-S43] PASS** **全民健康保險醫療服務給付項目及支付標準**（開放資料 ODS 全表，6,013 項，經逐項檢索）。
  - **33084B 磁振造影－無造影劑 6,500 點**（2010/01/01 生效）；備註全文：「1.本項須限經保險人同意之醫療院所實施。2.申報費用時必須附上報告結果。」
  - **33085B 磁振造影－有造影劑 11,500 點**（2010/01/01 生效）；備註同上。
  - **37028B 三度空間立體定位Ｘ光刀照射治療 82,000 點**（2023/03/01 生效）；適應症逐字含「顱內病灶直徑小於三公分或容積十五立方公分以下之病灶數目小於或等於三處之動靜脈畸型（含腦膜動靜脈瘻管）、**聽神經瘤、腦膜瘤、腦下垂體瘤、顱咽管瘤**或其他腫瘤…**且須符合以下條件之一：A.曾接受開顱手術，但有殘餘腫瘤或腫瘤復發者。B.開顱手術可能造成神經損傷或危險性大者。C.有嚴重心肺疾病或其他內科疾病，不適合侵入性手術或全身麻醉者。…F.顱內單側小腦橋腦角聽神經瘤寬度小於 2.5 公分（不含內耳道）者。**」＋「3.全部個案須事前專案向保險人申請。」
  - **37029B 加馬機立體定位放射手術 153,229 點**（2023/03/01 生效）；適應症同構（大小門檻為 3.5×3.5×3.5 公分或容積二十立方公分），另載「3.電腦刀影像導引立體定位放射手術（Cyber Knife Image Guided Stereotactic radiosurgery）項目比照申報。」「4.全部個案須事前專案向保險人申請。」
  Route（機器介面）：`curl https://info.nhi.gov.tw/api/iode0000s01/Dataset?rId=A21030000I-D20003-004`（HTTP 200，565,406 bytes，application/ods）→ odfpy 解析 6,013 列 → 逐項檢索。
  對應的人類可讀頁：政府資料開放平臺資料集 https://data.gov.tw/dataset/9405 ；健保署醫療服務給付項目及支付標準 https://www.nhi.gov.tw/ch/np-1631-1.html （**該 HTML 對抓取回 403，僅列為人類可讀對照，非本 brief 的取得路徑**）。
- **[A-S44] PASS** **全民健康保險醫療費用審查注意事項**（衛生福利部中央健康保險署編訂，452 頁 PDF）。
  本 brief 引用之逐字段落：（十八）其他注意事項 1.電腦斷層及磁振造影檢查審查原則 (1)–(9)（以「次」為單位、須附申請書報告影像、申請書內容五項、十二週內再次執行須敘明必要性、procedure of choice、癌症患者條件、骨與肌肉關節系統）；編號 **100901030「耳科病人有下列臨床狀況時，可予以適度安排 CT 或 MRI Study」十項（106/8/1）**；編號 100901040（人工耳蝸植入前）。
  逐字檢索結果（用於標 gap）：「腦膜瘤」「腦下垂體」「聽神經瘤」**零筆**；「腦瘤」2 筆（皆為腦電圖診斷價值段落，與 MRI 追蹤無關）。
  Route: `curl https://www.nhi.gov.tw/ch/dl-55608-2f847b0977dd49a4ad968bf8f3258800-1.pdf`（HTTP 200，3,637,766 bytes，452 頁）→ pdftotext（527,588 bytes）→ 逐字檢索。
  人類可讀頁：https://www.nhi.gov.tw/ch/cp-3937-e0cfb-2911-1.html
- **[A-S45] PASS** **113 年度全民健康保險醫療統計年報**（衛生福利部統計處）。
  - 表 4（西醫門診含急診・人數統計－按疾病別、性別及年齡別分）：「大腦及中樞神經系統其他部位之良性腫瘤 Benign neoplasm of brain and other parts of central nervous system **D33**」**23,027 人（男 8,700、女 14,327）**；表 1 就診率 **98.36／10 萬**。
  - 表一（出院患者件數及費用統計）：D33 **652 件**、費用 **132,096,723 點**；對照「腦惡性腫瘤 C71」3,422 件、525,747,108 點；「中樞神經系統其他部位惡性腫瘤 C70,C72」394 件。
  - **該年報的疾病別分類中沒有 D32、沒有 D35.2 的獨立列項**；歸入「其他腫瘤 remainder of C00-D49」（門診人數 1,065,794、出院 55,967 件）。
  Route: `curl https://dep.mohw.gov.tw/dos/lp-5103-113.html`（HTTP 200）→ 下載 `https://www.mohw.gov.tw/dl-98350-9e88b779-7618-4bed-a359-b1d1af838048.html`（HTTP 200，7,424,998 bytes，application/zip）→ unzip → 以 pandas 讀 `.xls` 統計表 → 逐列檢索。
  人類可讀頁：https://dep.mohw.gov.tw/dos/lp-5103-113.html
- **[A-S46] PASS（背景，不含可引數字）** **台灣癌症登記中心・簡介**：自述癌症登記的法源為癌症防治法第 11 條；資料處理流程（醫院於新診斷後 1 年內收案申報→雙重審核→戶政比對→多重原發歸併→年報），並說明「最新的癌症登記報告約晚 2 年」。
  Route: `curl https://twcr.tw/?page_id=1822`（HTTP 200）。
  人類可讀頁：https://twcr.tw/?page_id=1822

### FAIL／NOT-CITABLE（保留，說明為什麼）

- **[FAIL-1] Vernooij 2007 的腦膜瘤／垂體腺瘤個別百分比。** isOpenAccess: N、無 PMCID，Europe PMC fullTextXML 不可用。摘要只寫「benign primary tumors (1.6%), mainly meningiomas」。→ **正文只能引 1.6% 這個合併數字，不可寫「腦膜瘤 0.9%」之類的拆分**（若要用 0.9–1.0%，引 EANO [A-S12]，那是指引的敘述句，不是 Vernooij 的拆分）。
- **[FAIL-2] CNS 2026 影像指引更新版的具體建議。** Graffeo CS, Sivakumar W, Tavakol SA, et al. *Neurosurgery*. 2026;98(2):283–287. DOI 10.1227/neu.0000000000003419. PMID 40470931。Route: Europe PMC REST `EXT_ID:40470931` → 書目核對通過，**但摘要只有方法學與結論（7 個問題、6 個有更新建議、57 篇納入、多為 level III），沒有任何具體的追蹤間隔文字**；isOpenAccess: N、無 PMCID。→ **正文引 2018 版 [A-S22]，並註明 2026 年有更新版但原文措辭取不到。** 指引官方頁：https://www.cns.org/guidelines/treatment-adults-vestibular-schwannoma/5-role-of-imaging-in-management-of-patients-with-v
- **[FAIL-3] EANO 轉述的 Lee 等 232 人腦膜瘤生長世代。** 數字（25.4% 快速生長、OR per cm³ 1.07、無鈣化 3.87、水腫 2.74、T2 高／等訊號 3.76）是**透過 EANO 指引全文取得的二手轉述**[A-S12]，本 brief **未直接核對原始論文的書目與摘要**（Europe PMC TITLE/AUTH 檢索未命中）。→ 正文若使用，必須寫成「EANO 指引轉述的一個 232 人世代」，不可標成獨立文獻。
- **[FAIL-4] Fleseriu M, Gurnell M, McCormack A, et al. Pituitary incidentaloma: a Pituitary Society international consensus guideline statement.** *Nat Rev Endocrinol*. 2025;21(10):638–655. DOI 10.1038/s41574-025-01134-8. PMID 40555795。Route: Europe PMC REST TITLE 檢索 → 書目核對通過，isOpenAccess: N、無 PMCID，**摘要只有範疇敘述（對大腺瘤、微腺瘤、囊性病灶、空蝶鞍分別給建議；特殊族群），沒有任何可引用的門檻、間隔或數字**。→ **正文可以寫「2025 年有一份新的國際共識」，但門檻與間隔一律引 Endocrine Society 2011 [A-S25]。**
- **[FAIL-5] Carlson ML, Link MJ. Vestibular Schwannomas.** *N Engl J Med*. 2021;384(14):1335–1348. DOI 10.1056/nejmra2020394. PMID 33826821。Route: Europe PMC REST `AUTH:"Carlson ML" AND AUTH:"Link MJ" AND JOURNAL:"The New England journal of medicine"` → **abstractText 為 none**，isOpenAccess: N。→ **書目正確但無任何可引內容，不可引。**（聽神經瘤的細胞來源與症狀百分比因此成為 gap，見下。）
- **[FAIL-6] Ho KKY 等 2019 Pituitary Society 立場聲明的內文**（見 [A-S30]）：摘要不存在。
- **[FAIL-7] Ho KKY, Melmed S 等 2023 *Nat Rev Endocrinol* 19(11):671–678「Pituitary adenoma or neuroendocrine tumour: the need for an integrated prognostic classification」（PMID 37592077，PMCID PMC12519436，isOpenAccess: N）。** 本次未取得全文，不引。
- **[FAIL-8] 國民健康署（hpa.gov.tw）** 各頁面：`curl https://www.hpa.gov.tw/Pages/List.aspx?nodeid=269` 回 **000（連線失敗）**，與 RESEARCH-COMMON 所述之 TLS 問題一致。→ 已改走 mohw.gov.tw 與 twcr.tw（成功，見 [A-S45][A-S41][A-S46]）。
- **[FAIL-9] 健保署官網 HTML（nhi.gov.tw）**：`https://www.nhi.gov.tw/` 與 `https://www.nhi.gov.tw/ch/np-1631-1.html` 皆回 **403**（Cloudflare）。→ 已改走開放資料 ODS（[A-S43]）與直接 PDF（[A-S44]），兩者皆成功。
- **[FAIL-10] 政府資料開放平臺「國人全民健康保險就醫疾病資訊」（dataset 9403）**：`https://data.gov.tw/api/v2/rest/dataset/9403` 回 `{"success":false,"error":{"error_type":"Not Found"}}`；`https://data.gov.tw/dataset/9403` 為 SPA、HTML 中無資源連結；WebFetch 回 ROBOTS_DISALLOWED；試 `info.nhi.gov.tw/api/iode0000s01/Dataset?rId=` 之多個候選 rId 皆回 400「查無資料」。→ **ICD-10 三碼層級的健保就醫人數（含 D32、D35.2）未能取得。已改用 113 年度醫療統計年報（[A-S45]），但該年報只拆到 D33。**
- **[FAIL-11] 台灣官方的腦膜瘤與腦下垂體腺瘤人數**：癌症登記不收（[A-S40][A-S41]）、重大傷病無此項次（[A-S42]）、醫療統計年報未拆出 D32／D35.2（[A-S45]）、開放資料路徑失敗（FAIL-10）。→ **標 gap。正文寫「台灣沒有官方的腦膜瘤／腦下垂體腺瘤人數」，不可用美國佔比推算台灣人數。**

### 本 brief 明確的 gap 清單（正文必須寫成「查不到」，不可推論）

1. **gap-A1-1** 腦膜瘤與聽神經瘤的診斷延遲：無可引數據（腦下垂體有 [A-S32]）。
2. **gap-A2-1** 聽神經瘤的性別發生率比：CBTRUS 未列入「女多於男」名單，本 brief 不提供數字。
3. **gap-A2-2** 腦下垂體腫瘤與神經鞘瘤的診斷中位年齡（CBTRUS Figure 16 為圖檔，文字未載）。
4. **gap-A2-3** 「聽神經瘤起源於前庭神經的許旺細胞」的逐字文獻出處（[FAIL-5] 之故）。
5. **gap-A3-1** 「雙顳側偏盲」作為腦下垂體瘤壓迫視交叉的典型表現：本 brief 取得的全文只寫「壓迫並傷害視神經與視交叉」[A-S39]，無此逐字名詞。
6. **gap-A4-1** 「連續幾年無變化就可以停止追蹤」的明確年數：三份指引都沒有寫[A-S12][A-S22][A-S25]。
7. **gap-TW-1** 台灣的腦膜瘤與腦下垂體腺瘤官方人數（見 FAIL-11）。
8. **gap-TW-2** 健保對腦膜瘤／聽神經瘤／腦下垂體腺瘤的 MRI **追蹤頻次**條文：全文檢索零筆[A-S44]。
9. **gap-TW-3** NF2 是否在中央主管機關公告之罕見疾病名單內（重大傷病項次三十的入口）：本組未查，歸 E5。
