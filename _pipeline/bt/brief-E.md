# Brief E — 良性腦瘤專題「共同的之後」（E1–E5）

研究員：Group E｜查證日期：**2026-09-13**
期刊書目一律經 **Europe PMC REST** 逐筆核對（title／journal／year／volume(issue)／pages／DOI／PMID／isOpenAccess），
引用的每一個數字都出自摘要或可取得之 OA 全文；指引原文引語出自可實際抓取的官方頁面或 OA 全文。
台灣端：全國法規資料庫（law.moj.gov.tw）、健保署 `info.nhi.gov.tw` API（藥品給付規定 PDF、支付標準全表 TXT）實際下載後全文檢索。
**PubMed MCP 本次不可用**；**NCCN 不查不引**（專題規則）。

引用規則：**只有標 PASS 的來源可以進正文。** FAIL／NOT-CITABLE 條目保留，讓寫作者知道哪些話只能寫「我查不到可以引用的來源」。
每一個數字都帶「哪一種瘤」的標籤；跨瘤別借用的對照資料（例如腦轉移的類固醇試驗）在該筆逐條標明。

**站上指路檔名已確認存在**（`ls` 檢查）：
`gb-seizure.html`、`gb-steroid.html`、`gb-recurrence.html`、`gb-followup.html`、`gbm.html`、
`sit-pseudo.html`、`sit-reirradiation.html`、`nt-bn-meningioma.html`、`nt-proton.html`、`insight-proton.html`、
`sit-mdt.html`、`sit-second-opinion.html`、`sit-elderly.html`、`care-fear.html`、`sit-paperwork.html`、`lc-brainmet.html`。

---

## ⚠ 與 SPEC 假設不同形狀的事（動筆前必讀，共 8 條）

1. **E1 最關鍵的一份指引存在，而且比 SPEC 想像的更硬。**
   AAN 2000 practice parameter 確實已退休（**AAN 官網逐字：「This guideline is retired.… Retired by the AAN Institute Board of Directors on June 4, 2012.」**；
   Europe PMC 的標題本身就帶 `[RETIRED]`）[E-S2][E-S3]。
   **取代它的是 SNO／EANO 2021 practice guideline update**（Neuro-Oncology 2021;23(11):1835–1844），
   AAN 官網標示「Affirmed by the AAN Institute Board of Directors on November 18, 2020.」[E-S2]。
   它的建議是**等級 A 的否定建議**：「In patients with newly diagnosed brain tumors who have not had a seizure,
   clinicians **should not prescribe** antiepileptic drugs (AEDs) to reduce the risk of seizures (**level A**).」[E-S1]
   →E1 不是「沒有證據支持常規給」這種軟寫法（那是 GBM 專題當時的寫法），而是**有一份現行指引明著說不要給**。
   但**手術周邊那一段仍然是 level C「證據不足」**，而且**「用腫瘤位置、組織型、分級、分子／影像特徵來決定要不要給」是 level U**[E-S1]
   ——所以**不可以寫「腦膜瘤因為位置／分級所以是例外」**。

2. **E2「什麼時候可以停止追蹤」不是一個 gap，而是三種瘤三個不同的答案，其中兩個可以引。**
   - 腦膜瘤：**NICE NG99 有明文的停止條件**——第 9 年之後「**Consider discharge**」；
     無症狀偶然發現的腦膜瘤「**scan at 12 months and if no change, consider discharge or scan at 5 years**」[E-S15]。
   - 非功能性腦下垂體腺瘤：**CNS 2016 指引明著寫「證據不足以就監測的期間與頻次做出建議」**
     （"There is insufficient evidence to make a recommendation on the duration of time of surveillance and its frequency."）[E-S18]；
     而一份 148 人的 GTR 世代結論是「**patients require life-long periodic imaging**」[E-S24]。
   - 聽神經瘤：CNS 2026 更新只寫到「觀察者前 3 年每年、之後至少每 3–5 年一次」，**沒有給停止點**[E-S17]。
   →**三種瘤並列的這一篇，正確的形狀是「停不停得掉，三種瘤的答案不一樣，而且其中一種的官方答案是『不知道』」**，
   不是 SPEC 假設的「找得到就引、找不到標 gap」的二分法。

3. **E4 的「另一個方向」有一條可以直接引的指引句，比任何研究都好用。**
   CNS 2026 立體定位放射手術指引的四條新 level III 建議之一，逐字是：
   「adult patients with sporadic VS undergoing SRS **should be informed that SRS does not result in an increased number of
   secondary malignancies compared with the rate expected in the overall population**」[E-S51]。
   這句話把「第二腫瘤風險」與「告知義務」綁在同一句裡，正是紅線 7 要的材料。

4. **E3 的「沒有藥」要改寫成「有藥，但每一個都只是 PFS-6 的單臂訊號，唯一的隨機第三期是陰性的」。**
   腦膜瘤系統性藥物不是空白：sunitinib（PFS-6 42%，達標）[E-S32]、bevacizumab（PFS-6 第1級 87%／第2級 77%／第3級 46%）[E-S33]、
   everolimus+octreotide（PFS-6 55%）[E-S36]、Alliance A071401 的 FAK 抑制劑（第1級 PFS-6 83%、第2/3級 33%，兩組都達標）[E-S34]。
   **反方向更重要**：mifepristone 的**隨機雙盲第三期 SWOG S9005（n=164）是陰性**[E-S38]；
   trabectedin 的**隨機第二期 EORTC-1320（n=90）不但沒有改善、PFS 數字還比標準照護差**（中位 2.43 vs 4.17 個月）且毒性更高[E-S35]；
   octreotide 單用（n=9）**零個部分反應**[E-S37]；pembrolizumab（n=18）**PFS-6 11.1%，因無效與收案慢提前終止**[E-S39]。
   →**「沒有標準藥」是對的，「沒有藥」是錯的**；而且**唯一的兩個隨機資料都指向沒有效**，這比「沒資料」更有力。

5. **腦膜瘤術後的瘤周水腫多半不會消失——這件事跟病人的直覺相反，而且跟癲癇直接相關。**
   279 位術前有瘤周水腫、做到 GTR 的病人，**術後至少一年的 MRI 上 96.8%（270/279）水腫變化仍然存在**；
   只有 35.8% 的人水腫體積消退超過九成[E-S7]。作者的解釋是那多半是**膠質增生（gliosis）**，不是還在漏水。
   同一組 218 人的資料顯示，**殘留水腫體積最高三分位的人新發癲癇的勝算是最低三分位的 4.7 倍**，
   而且有腦電圖的 23 人裡 10 人（43.5%）的致癇病灶就在殘留水腫的位置[E-S6]。
   →E1 不可以寫成「開完刀水腫就會退、藥就可以停」。

6. **E5 的名稱改版比 SPEC 寫的更徹底：不只是「改名」，是「NF2 這個詞被退掉了」。**
   2022 年的國際共識原文寫的是：「In the revised nomenclature, **the term "neurofibromatosis 2" has been retired**
   to improve diagnostic specificity.」[E-S53]；而且**新準則本身就把鑲嵌型寫進條文**（VAF 明顯 <50% 即診斷為 mosaic NF2-SWN）[E-S54]。
   另外**「多發腦膜瘤就是 NF2」是錯的**：LZTR1、SMARCB1 相關的 schwannomatosis、BAP1、SUFU、SMARCE1（家族性透明細胞腦膜瘤），
   以及**過去的放射線暴露**，都要放在同一張鑑別診斷表裡[E-S54]。

7. **台灣端最大的意外：健保立體定位放射手術的條文在 115.04.01 換版了，而且「復發」是明列的適應條件。**
   支付標準全表（本次下載版）中 **37028B／37029B 的生效日是 20260401**，條文逐字含
   「**聽神經瘤、腦膜瘤、腦下垂體瘤**」與條件「**A.曾接受開顱手術，但有殘餘腫瘤或腫瘤復發者**」，
   且 37029B 第 3 點寫明「**加馬機立體定位放射手術（Stereotactic radiosurgery with γ-knife）項目比照申報**」[E-S64]。
   站上 `sit-reirradiation` 引的是 114.03.13 版，**E3／E1 提到代碼時必須用這一版並標日期**。

8. **bevacizumab 在台灣的健保條文，逐字查完是零筆涵蓋本專題三種瘤。**
   藥品給付規定第 9.37 條（檔名 `9.37._20251001.pdf`）共 7 個適應症群組，
   以「腦膜瘤／神經鞘瘤／聽神經／神經纖維瘤／NF2／schwannoma／meningioma」逐字檢索**全部 0 筆**[E-S62]。
   →E3、E5 只能寫「條文裡沒有這個適應症，怎麼申請問醫務課」，**不可推論有無給付**。

---

## E1 `bt-seizure-steroid`〈癲癇、水腫、類固醇，還有開車〉【紅線 10】

> **寫作者先讀**：類固醇的副作用逐項、以及「減量為什麼要慢」，站上 `gb-steroid`〈類固醇：救命的藥，也要減掉〉
> 已經寫完（含 Vecht 試驗、肌病變、潰瘍、失眠、血糖、情緒、感染）。**這一篇不重寫那一段，一句指路。**
> E1 要自己扛的是**腦膜瘤專屬的三件事**：癲癇盛行率（帶分母）、瘤周水腫為什麼在腦膜瘤特別常見且術後不退、
> 以及**預防性抗癲癇藥現在有指引明說不要給**。駕照條文沿用 `gb-seizure` 的寫法（已重新確認版本）。

### Key facts

**一、腦膜瘤的癲癇盛行率（全部是幕上腦膜瘤；帶分母）**

- **術前癲癇：29.2%（4,709 位幕上腦膜瘤）**（39 個觀察性世代的系統性回顧與統合分析，**沒有任何對照試驗**）[E-S4]。
  預測因子（統合分析）：男性 OR 1.74（95% CI 1.30–2.34）、**沒有頭痛** OR 1.77（1.04–3.25）、
  **瘤周水腫 OR 7.48（6.13–9.47）**、非顱底位置 OR 1.77（1.04–3.25）[E-S4]。
- **手術後**：術前有癲癇的 703 人中 **69.3% 達到無發作**；
  **術前沒有癲癇的 1,085 人中，12.3% 出現新的術後癲癇**[E-S4]。
- **術前有瘤周水腫這個次族群（218 人，全部做到 GTR）**：術前癲癇 94/218（43.1%）；
  其中 27/94（28.7%）術後仍在發作（首次術後發作平均 8.4 個月）；
  術前沒發作過的 124 人中 **18 人（14.5%）新發癲癇**（平均 7.6 個月）[E-S6]。
- **早期術後癲癇（術後第一週）**：單中心 517 位幕上凸面／矢狀竇旁腦膜瘤、術前無癲癇者，**30/517（5.8%）**；
  多變項分析中**唯一的獨立預測因子是手術／內科併發症**（OR 16.33，95% CI 7.07–37.7，P<0.001）[E-S5]。

**二、預防性抗癲癇藥：現行指引怎麼寫（E1 的核心）**

- **SNO／EANO 2021 practice guideline update**（取代 AAN 2000）逐字建議[E-S1]：
  - 「In patients with newly diagnosed brain tumors who have not had a seizure, clinicians **should not prescribe**
    antiepileptic drugs (AEDs) to reduce the risk of seizures (**level A**).」
  - 「In brain tumor patients undergoing surgery, there is **insufficient evidence** to recommend prescribing AEDs
    to reduce the risk of seizures in the peri- or postoperative period (**level C**).」
  - 「There is insufficient evidence to support prescribing valproic acid or levetiracetam with the intent to
    prolong progression-free or overall survival (**level C**).」
  - 「Physicians **may consider** the use of levetiracetam over older AEDs to reduce side effects (**level C**).」
  - 「There is insufficient evidence to support using **tumor location, histology, grade, molecular/imaging features**
    when deciding whether or not to prescribe prophylactic AEDs (**level U**).」
- **退休狀態的官方證據**：AAN 官網 GuidelineDetail/30 逐字「This guideline is retired.」「Guideline, May 2000」
  「**Retired by the AAN Institute Board of Directors on June 4, 2012.**」[E-S2]；
  Europe PMC 書目標題即 `Practice parameter: anticonvulsant prophylaxis in patients with newly diagnosed brain tumors [RETIRED]`[E-S3]。
- **腦膜瘤專屬的統合分析結論（可與指引並陳）**：「No difference in the rate of new postoperative seizures was observed
  with or without perioperative prophylactic anticonvulsants.」「evidence does not support routine use of prophylactic
  anticonvulsants in patients without seizures」[E-S4]。
- **反方向的資料（誠實必列）**：同一篇單中心研究的文獻回顧（2011–2021，10 篇）得出
  「術前無癲癇的幕上腦膜瘤，早期術後癲癇發生率**用藥組 3.7%（47/1,282）、未用藥組 6.2%（95/1,525）**；
  其中凸面／矢狀竇旁、未用藥者 **9.0%（19/209）**」，作者結論是「AED 預防可以降低凸面與矢狀竇旁腦膜瘤的早期術後癲癇」[E-S5]。
  **這是回溯性單中心＋非隨機文獻彙整，證據等級遠低於 [E-S1]，但方向相反，必須一起寫。**
- **現行的腦瘤癲癇總說**：SNO 2024 consensus review（Neuro-Oncology 2024;26(1):7–24）可作為「這一題現在怎麼看」的錨點；
  **本次只取得摘要，全文取不到，不可引用其內文措辭**[E-S13]。

**三、瘤周水腫：機轉、影響因子、術後會怎樣**

- **機轉（腦膜瘤專屬資料）**：79 位 WHO 第 1 級腦膜瘤的免疫組化＋術中血管觀察，
  VEGF **只表現在腦膜瘤腫瘤細胞**；**只有「同時有軟腦膜供血血管＋腫瘤表現 VEGF」這一組與瘤周水腫相關（P<.002）**；
  性別、年齡、腫瘤大小、位置、組織型都不足以解釋水腫形成[E-S8]。
- **術後不會消失**：279 位術前有水腫、做到 GTR、術後至少一年有 MRI 的病人，
  **96.8%（270/279）水腫變化持續存在**；只有 **35.8%（102/279）** 在中位 5.0 年（IQR 2.3–6.5）追蹤中消退超過九成。
  較高的 edema index（P<.001）與顳葉位置（P=.018）與較高的消退比例相關。作者判讀為**膠質增生**[E-S7]。
- **殘留水腫與癲癇**：殘留水腫體積最高三分位（中位 12.8 cm³）對最低三分位（中位 0.5 cm³），
  **新發癲癇 OR 4.7（P=0.03）**；術後水腫體積增加者，新發癲癇 OR 6.7（P=0.008）、持續癲癇 OR 4.4（P=0.004）；
  殘留水腫越大，術後 KPS 越差（每增加 1 cm³ OR 1.03，P=0.04）[E-S6]。

**四、類固醇（**這一段寫短，指路 `gb-steroid`**；E1 只保留下面三個可直接引的錨點）**

- **劑量與副作用的隨機證據（族群：腦轉移，不是腦膜瘤，必須標）**：89 人可評估的兩個雙盲隨機試驗，
  dexamethasone 4 mg/日與 16 mg/日在第 7 天的 Karnofsky 改善相當（6.7±11.3 vs 9.1±12.4 分），
  **毒性在 16 mg 組明顯較多（P<0.03）**；作者結論是沒有腦疝徵象者 4 mg/日即可[E-S9]。
- **類固醇肌病變（族群：原發性腦瘤，含腦膜瘤以外的診斷）**：216 位連續使用 dexamethasone ≥2 週的成人原發腦瘤病人，
  **有臨床意義的肌病變 23 人（10.6%）**，**三分之二發生在連續治療的第 9 到第 12 週**[E-S10]。
- **「為什麼減量要慢」的兩層**：
  ① **腎上腺功能不全**——74 篇、3,753 人的統合分析：停用後腎上腺功能不全的比例依途徑 4.2%（鼻用）到 52.2%（關節內注射）；
     依劑量 2.4%（低劑量）到 21.5%（高劑量）；依療程長度 1.4%（<28 天）到 27.4%（>1 年，氣喘族群）；
     血液惡性腫瘤族群 60.0%。作者結論逐字：「**there is no administration form, dosing, treatment duration, or underlying
     disease for which adrenal insufficiency can be excluded with certainty**」[E-S11]。**這是全族群資料，不是腦瘤族群，要標。**
  ② **神經腫瘤科實務**：一份 4 年單中心回顧指出 **1% 的神經腫瘤科類固醇使用者出現續發性腎上腺功能不全**，
     而且其症狀**會被誤認成顱內壓升高或化放療副作用**[E-S12]。**n 只有 5 例，是病例系列，寫的時候要說清楚。**
- **紅線 10 要求的那句**：類固醇不可自行加減量——`gb-steroid` 已有完整寫法，沿用。

### 反方向的資料（誠實必列）

- 預防性抗癲癇藥：指引是 level A 的「不要給」[E-S1]，但**手術周邊那一格是 level C「證據不足」**，
  而且有回溯性資料顯示凸面／矢狀竇旁腦膜瘤未用藥者早期術後癲癇 9.0%[E-S5]。
  **寫法必須是「這一題在開刀前後那幾天仍未定，是醫師依你的狀況決定」，不是「不需要吃」。**
- 腦膜瘤手術對癲癇是有效的（術前有癲癇者 69.3% 無發作）[E-S4]，**但這不是開刀的理由**
  ——[E-S4] 是觀察性世代的彙整，沒有對照組。

### Claim ceiling（E1）

- **可寫**：「幕上腦膜瘤的病人，**大約三成在手術前就發作過**（4,709 人的彙整）」；
  「**術前沒發作過的人，術後新發癲癇約一成二**（1,085 人）」；
  「**瘤周水腫是最強的關聯因子**（勝算比約 7.5）——勝算比不是機率的幾倍」；
  「**現行指引寫的是：新診斷腦瘤、從沒發作過的人，不應該為了預防癲癇而開抗癲癇藥（等級 A）**」；
  「**指引同時說：不能用腫瘤的位置、組織型、分級來決定要不要預防性給藥（等級 U）**」；
  「開完刀水腫多半不會完全退，那多半是膠質增生，而且殘留越多、新發癲癇越多」；
  「dexamethasone 的副作用隨劑量與時間增加，腦轉移的隨機試驗裡 4 mg 與 16 mg 的短期效果相當、毒性 16 mg 較多」（標族群）。
- **不可寫**：
  - 「發作一次沒關係」（紅線 10）；
  - 「腦膜瘤不用預防性吃藥」這種**指令式**寫法——指引是對「新診斷腦瘤、未發作者」說的，
    **且手術周邊那一段明著寫證據不足**；正確寫法是「指引怎麼寫」＋「這一題回去問誰」；
  - 「AAN 說……」——**AAN 2000 已退休，引它就是錯**[E-S2][E-S3]；
  - 任何劑量、任何減量速度的具體數字寫成可以照做的說明（`gb-steroid` 的紀律沿用：出現的 mg 數都是研究分組）；
  - 「水腫退了就可以停藥」；
  - 把 [E-S5] 的 9.0% 寫成「所以要吃」——那是回溯性資料，與 level A 建議方向相反，必須並陳而非取代。

### Caveats／safety notes（寫作者必寫）

- **[E-S4] 是 1980–2014 的 39 個觀察性世代**，沒有隨機資料；所有比例都是彙整值，不是個人機率。
- **[E-S9][E-S10][E-S11][E-S12] 都不是腦膜瘤族群**（分別是腦轉移、混合原發腦瘤、全族群、神經腫瘤科混合），
  每一筆在正文都要帶族群標籤。
- 類固醇減量、停藥、加量一律是開藥醫師的決定；本文不給任何可照做的減量表。
- 癲癇急救與「五分鐘是行動線」已在 `gb-seizure` 寫完，E1 一句指路，不重寫。

### 台灣端（E1）

| 項目 | 結果 | 路徑 |
|---|---|---|
| **癲癇與駕照條文** | **重新確認現行版本**：《道路交通安全規則》**修正日期 民國 115 年 06 月 26 日**、法規整編資料截止日 **民國 115 年 09 月 04 日**（查證日 2026-09-13）。第 64 條第一項第一款第六目之 1 逐字：「**癲癇。但檢具醫療院所醫師出具最近二年以上未發作診斷證明書者，不在此限。**」同目之 2、之 3 為兩個開放條款。第 52 條之 3：符合前述但書者「**得申請機車或普通小型車駕駛執照考驗，其駕駛執照並自發照之日起每滿二年換發一次**」，換照須於有效期限**屆滿前後一個月內**檢具最近三個月內、由神經內科／神經外科／兒科且曾參加神經相關專業訓練醫師出具、加註專科醫師證照號碼之「最近二年內未癲癇發作」診斷證明書。第 76 條第一項第五款、第八款與第二項：體格變化不合格、或「**有癲癇發作情形或未依該規定辦理定期換照**」者應迅速繳回駕照且不得駕駛汽車。第 65 條：繳回後「**最近二年以上未有癲癇發作，經醫療院所醫師出具診斷證明書**」者得免考驗逕予核發新照。第 64 條之 1：年滿 60 歲職業駕駛人每年體檢，「**患有癲癇、腦中風、眩暈症、重症肌無力等身體障礙致不堪勝任工作**」為不合格 | law.moj.gov.tw `LawSingle.aspx?pcode=K0040013&flno=64／52-3／64-1／65／76` 與 `LawAll.aspx?pcode=K0040013`，2026-09-13 逐條抓取並與 `gb-seizure` 逐字比對，**一字不差** [E-S14] |
| 未滿 60 歲職業駕照怎麼認定 | **gap（沿用 `gb-seizure` 的寫法）**：條文只寫到第 52 條之 3 的機車與普通小型車；**我查不到可以引用的明文，請向監理單位確認** | 同上 |
| 「診斷了腦瘤但從沒發作過」 | **條文沒有專門規定**，落點只能是第 64 條那兩個開放條款的專科醫師認定——**不推論** | 同上 |
| **levetiracetam 給付條文** | **查到（逐字）**：藥品給付規定 **1.3.2.4 Levetiracetam**（101/6/1、102/10/1、108/5/1、111/2/1）：「1.一般錠劑膠囊劑…**(1)限用於其他抗癲癇藥物無法有效控制之局部癲癇發作之輔助性治療 (add on therapy) 或作為第二線之單一藥物治療。**(2)12歲以上病患之肌抽躍性癲癇發作之輔助治療(111/2/1)。2.緩釋錠劑膠囊劑…限使用於16歲以上病患之局部癲癇發作之輔助治療(111/2/1)。3.口服液劑…限用於其他抗癲癇藥物無法有效控制之局部癲癇發作之輔助性治療。4.注射劑…限癲癇症病患使用，且符合以下其中之一項者使用：(1)對 phenytoin 注射劑無效或無法忍受 phenytoin 副作用且無法口服 levetiracetam 之病患。(2)癲癇連續發作 (Seizure clusters) 之病患。(3)癲癇重積狀態(Status epilepticus) 之病患。」現行連結此規定的品項 **56 項** | `POST info.nhi.gov.tw/api/INAE3000/INAE3000S01/SQL0001`（DRUG_ING=levetiracetam）→ 規定碼 1.3.2.4.、檔名 `1.3.2.4._20220201.pdf` → `getPDF` → pdftotext，2026-09-13 [E-S63] |
| carbamazepine／lacosamide | **查到規定碼**：carbamazepine **1.3.2.6.**（檔名 `1.3.2.6._20110801_000.pdf`，現行 35 個品項）；lacosamide **1.3.2.9.**（`1.3.2.9._20180801_000.pdf`，現行 15 個品項）。**條文內文本次未逐字抓取，正文若要引須先抓** | 同上 [E-S67] |
| **valproic acid／phenytoin 的給付規定欄位** | **查詢結果**：以成分名查詢，現行品項的「藥品給付規定」欄位**全部為空**（valproic acid 17 項、phenytoin 41 項，皆無對應條號） | 同上，全頁擷取後篩選 `paY_END_DATE` 為空或「迄今」[E-S67]。**本條只證明查詢結果，不得據以宣稱有無給付** |
| **類固醇（dexamethasone／prednisolone）給付** | **查詢結果**：dexamethasone 現行 483 筆中 **480 個品項的「藥品給付規定」欄位為空**，另 2 項屬 14.3.、1 項屬 14.9.4.（皆為眼科相關條號）；prednisolone 現行 377 個品項**全部為空** | 同上 [E-S67]。寫法：「**條文上我查不到針對腦瘤水腫的特別限制**，怎麼開、怎麼減是醫師的判斷；有疑問問醫務課」 |

### 給繪圖組（E1）

SPEC §七 沒有分配圖給 E1。若要補一張，可用的 **PASS 數字**只有這一組（全部標「幕上腦膜瘤」）：
術前癲癇 29.2%（n=4,709）／術後無發作 69.3%（n=703）／術前無癲癇者新發 12.3%（n=1,085）[E-S4]；
水腫的勝算比 7.48（6.13–9.47）[E-S4]；術後水腫持續 96.8%（n=279）[E-S7]。
**不要畫類固醇減量曲線。**

---

## E2 `bt-followup`〈追蹤怎麼排，追到什麼時候停〉——三種瘤並列

> **寫作者先讀** `sit-pseudo`〈影像變壞，不一定是病變壞〉。本篇談放射手術後的暫時性膨脹時，
> **措辭不得比 sit-pseudo 更寬鬆**：那一頁的立場是「只能回頭看才成立」「沒有一個影像特徵或症狀能在當下把它跟真的惡化分開」
> 「四到八週是試驗判讀病灶的規則，不是你可以自己領走的等待期」。E2 沿用同一個立場。

### Key facts

**一、腦膜瘤：治療後與觀察中的兩種情境（唯一有明文時程表且有停止條件的一種）**

NICE NG99《Brain tumours (primary) and brain metastases in over 16s》（**Published 11 July 2018；Last updated 29 January 2021**）
第 1.5 節，表 7「**Possible regular clinical review schedule by years after end of treatment for people with meningioma
depending on grade of tumour**」逐字[E-S15]：

| 治療後年數 | 第1級·無殘餘 | 第1級·有殘餘 | 第1級·放療後 | 第2級 | 第3級 |
|---|---|---|---|---|---|
| 0–1 年 | 3 個月時掃描 | 3 個月時掃描 | 放療後 6 個月掃描 | 3 個月時掃描，之後 6–12 個月再一次 | 每 3–6 個月 |
| 1–2 年 | 每年 | 每年 | 每年 | 每年 | 每 3–6 個月 |
| 2–3 年 | 每年 | 每年 | 每年 | 每年 | 每 6–12 個月 |
| 3–4 年 | 每 2 年 | 每年 | 每 2 年 | 每年 | 每 6–12 個月 |
| 4–5 年 | 每 2 年 | 每年 | 每 2 年 | 每年 | 每 6–12 個月 |
| 5–9 年 | 每 2 年 | 每 2 年 | 每 2 年 | 每 2 年 | 每年 |
| **>9 年（終其一生）** | **Consider discharge** | **Consider discharge** | **Consider discharge** | **Consider discharge** | **每年** |

- **觀察中（偶然發現、無症狀）的停止條件（逐字）**：「For asymptomatic incidental meningioma:
  **scan at 12 months and if no change, consider discharge or scan at 5 years.**」[E-S15]
- **表下註（重要）**：「the presence of any residual tumour **can only be established after the first scan at 3 months**」[E-S15]
  ——這句解釋了為什麼第一次追蹤影像是 3 個月而不是出院前。
- **NICE 自己把「多做影像」的代價寫進表 6**（可直接引，對抗「追越密越好」的直覺）：
  「**There is no definitive evidence that identifying recurrent disease early improves outcomes**」；
  「May increase anxiety if changes of uncertain significance are detected on imaging」；
  「Some people can find more frequent imaging and hospital contact burdensome and disruptive –
  **they feel their life revolves around their latest scan**」[E-S15]。
- **隨時回診的條件（逐字）**：「Arrange a clinical review, including appropriate imaging, for people with meningioma
  (**including incidental meningioma**) who develop new or changing neurological symptoms or signs **at any time**.」[E-S15]
- **NICE NG99 涵蓋 glioma、meningioma、brain metastases——不涵蓋聽神經瘤與腦下垂體瘤**。這件事要寫出來。
- **國際共識的位置**：ICOM 2024 共識綜述（Neuro-Oncology 2024;26(10):1742–1780，OA）在「未來方向」一節明著寫
  「**Defining the appropriate interval and type of surveillance needed for each meningioma subgroup**」仍是待解的事[E-S40]
  ——所以 NICE 的表是「一份國家指引的建議」，不是國際定論。

**二、聽神經瘤：三種情境（觀察／手術後／放射手術後）都有 level III 建議，但沒有停止點**

CNS（Congress of Neurological Surgeons）2026 影像指引更新，**官方全文頁逐字**（`cns.org` 可抓取）[E-S17]：

- **觀察中**：「It is suggested that **close early imaging follow-up, with annual studies for at least 3 years after
  diagnosis, followed by interval imaging at least every 3-5 years**, with specific plans tailored to the patient-specific
  parameters (e.g., age, tumor size, prior growth), and the comfort levels of the patient and multidisciplinary treatment
  team be used in patients with sporadic VS undergoing initial observation.」（Level III）
- **手術後**：「it is suggested that **initial imaging at ≥ 3 months after surgery**, with follow-up imaging at closer
  intervals for STR/NTR (e.g., **3, 12, and 24 months**), and longer intervals after GTR (e.g., **6, 18, and 36 months**)
  is reasonable.」（Level III）
- **放射手術後（這一條是 2026 新增，直接對應紅線與 `sit-pseudo`）**：「**Post-radiosurgery imaging is suggested at
  12, 24, and 36 months, and deferral of retreatment is suggested until progression is noted on 3 consecutive imaging
  studies, absent concerning parallel changes in clinical symptoms.**」（Level III）
- **序列影像可以不用打顯影劑**：「The use of high-resolution T2 imaging without enhanced T1 imaging in follow-up of
  observed VS is suggested, with enhanced T1 studies considered for instances of equivocal growth…」（Level III）[E-S17]
- **2018 舊版的對應建議（仍可引，措辭不同）**：「MRIs should be obtained **annually for 5 yr**, with interval lengthening
  thereafter with tumor stability.」；GTR 者「a postoperative MRI **may occur as late as 1 yr after surgery**」，
  非 GTR 者「**annual MRI scans may be reasonable for 5 yr**」[E-S16]。
  →**兩版措辭不同（5 年 vs 3 年＋3–5 年），照原文並陳，不要自己折衷。**
- **CNS 對整個證據基礎的自評（可直接引，很好用）**：「The current evidence base for imaging protocols in VS clinical
  management is **broad, diverse, low certainty, and low quality**.」[E-S17]

**三、腦下垂體瘤：功能性與非功能性不同，而且「停」這件事沒有答案**

- **偶然發現的腦下垂體病灶（Endocrine Society 2011 clinical practice guideline，OA 全文逐字）**[E-S19]：
  - 「**MRI scan of the pituitary 6 months after the initial scan if the incidentaloma is a macroincidentaloma
    and 1 yr after the initial scan if it is a microincidentaloma (1|⊕⊕○○).**」
  - 「In patients whose incidentaloma does not change in size, we suggest **repeating the MRI every year for
    macroincidentalomas and every 1–2 yr in microincidentalomas for the following 3 yr, and gradually less frequently
    thereafter (2|⊕⊕○○).**」——**注意：是「逐漸拉長」，沒有寫停。**
  - **視野**：「**VF testing in patients with a pituitary incidentaloma that enlarges to abut or compress the optic
    nerves or chiasm on a follow-up imaging study (1|⊕⊕⊕⊕).**」；反過來「we suggest that clinicians **do not need to
    test VF** in patients whose incidentalomas are not close to the chiasm and who have no new symptoms and are being
    followed closely by MRI (2|⊕○○○)」。
  - **荷爾蒙**：「**Clinical and biochemical evaluations for hypopituitarism 6 months after the initial testing and
    yearly thereafter in patients with a pituitary macroincidentaloma**…(1|⊕⊕○○)」；
    微腺瘤若臨床、病史與 MRI 都沒變化，「**do not need to test for hypopituitarism** (2|⊕⊕○○)」。
  - 括號裡的 `1|⊕⊕○○` 是 GRADE：`1`＝強建議、`2`＝弱建議；`⊕` 數量＝證據品質。**正文要解釋一次。**
- **治療後的非功能性腺瘤（CNS 2016 指引，摘要逐字）**[E-S18]：
  - 「**Long-term radiologic, endocrinologic, and ophthalmologic surveillance monitoring after surgical and/or radiation
    therapy treatment of NFPAs to evaluate for tumor recurrence or regrowth, as well as pituitary and visual status,
    is recommended.**」
  - 「**There is insufficient evidence to make a recommendation on the duration of time of surveillance and its frequency.**」
  - 「It is recommended that **the first radiologic study to evaluate the extent of resection of the NFPA be performed
    ≥3 months after surgical intervention.**」
- **為什麼停不掉（實證面）**：148 位 NFPA 做到 GTR 的單一術者世代，中位追蹤 91 個月，復發 12 人（8.1%），
  **中位復發時間 80 個月（範圍 36–156 個月）**；在已經有 12／36／60／84／120 個月無復發影像之後，
  180 個月仍無復發的機率分別是 84%／86%／88%／93%（全體 82%）；**逐年復發勝算線性上升 1.07%**。
  作者結論逐字：「Increased intervals of recurrence-free imaging were **not** associated with a decrease in risk of
  recurrence, which suggests that **patients require life-long periodic imaging**.」[E-S24]
- **另一個分母（同為非功能性腺瘤）**：491 位初治 NFPA 手術世代，術後殘餘 173/491（36.4%）；
  有至少兩次追蹤影像的 436 人中**復發 83 人（19.0%）**，中位追蹤 53 個月[E-S25]。
- **功能性腺瘤的追蹤主軸是生化不是影像**——D 組主場。E2 只寫「功能性看的是荷爾蒙數值，非功能性只能看影像與視野，
  所以兩者的追蹤節奏不一樣」，**不重寫泌乳素瘤的停藥條件**（紅線 3 歸 D2）。

**四、追蹤看的不只是影像**

- **視野**：見上方 Endocrine Society 兩條建議（有分「要測」與「不需要例行測」兩個方向）[E-S19]；
  NFPA 治療後的眼科監測列在 CNS 的長期監測建議裡，**但頻次無建議**[E-S18]。
- **荷爾蒙**：巨腺瘤 6 個月一次然後每年；微腺瘤若無變化不需要[E-S19]；NFPA 治療後「長期」但**頻次無建議**[E-S18]。
- **聽力**：**gap**——本次以 Europe PMC 檢索，**查不到任何一份給出「聽神經瘤觀察中該多久做一次純音聽力檢查」的指引建議**。
  可引的只有**結果面**：CNS 2026 聽力保存指引的彙整估計值（同側診斷時仍有 serviceable hearing 者）——
  **觀察：2 年 78%、5 年 59%、10 年 47%；放射手術：2 年 71%、5 年 59%、10 年 38%；顯微手術：2 年 48%、5 年 40%、10 年 32%**，
  結論逐字「**Regardless of treatment modality, fewer than half of patients with sporadic vestibular schwannoma who
  present with serviceable hearing will maintain useful hearing by 10 years.**」[E-S23]
  →**這一組數字的主場是 C2（紅線 5），E2 只借來說明「聽力會隨時間往下走，所以聽力追蹤跟影像追蹤是兩件事」，
  且必須帶「觀察組也會掉」這個方向。**

**五、放射手術後的暫時性膨脹（與 `sit-pseudo` 一致）**

- **前瞻世代（聽神經瘤，n=100，加馬刀，邊緣劑量平均 12.2 Gy，平均觀察 65 個月）**：
  **腫瘤體積在 3 個月時平均增加 23%、6 個月時 27%**，平均在 12 個月時縮回原來大小。
  最大體積增幅：<10% 26 人、10–30% 23 人、30–50% 22 人、50–100% 16 人、**>100% 13 人**；
  峰值膨脹平均 47%（範圍 0–613%）。**暫時性顏面神經麻痺與顏面感覺異常與膨脹強烈相關；
  聽力下降只有一半與此現象同時發生**[E-S20]。
- **體積分析世代（聽神經瘤，n=259，單次 SRS，中位邊緣劑量 12 Gy，序列 MRI ≥24 個月）**：
  四種生長軌跡——**早期假性進展 35.5%、晚期假性進展 11.2%、穩定 41.3%、真正進展 12%**；
  作者訂的規則（PP＝12 個月內體積上升 >20% 且 24 個月內回落 ≥10%）敏感度 86%、特異度 93%（AUC 0.92）。
  假性進展或穩定者 serviceable hearing 保存 ≥86%，真正進展者只有 61%（p<0.01）[E-S21]。
- **哪一種比較會發生（聽神經瘤，n=330，加馬刀）**：**實質型 55% 對囊性型 31%（P<.001）**[E-S22]。
- **指引怎麼處理**：CNS 2026 的作法是「12、24、36 個月照，**在連續三次影像都顯示惡化之前先不要再治療**，
  除非臨床症狀同時出現令人擔心的變化」[E-S17]——**這句話就是 `sit-pseudo` 那一頁的專科版本，直接引，不要改寫得更寬鬆。**

### 反方向的資料（誠實必列）

- 追蹤影像本身有代價：NICE 把「不確定意義的變化會增加焦慮」「病人覺得人生繞著下一次掃描轉」寫進指引表格[E-S15]；
  ICOM 也寫「Even surveillance imaging may be associated with significant anxiety and negative effects on HRQoL」[E-S40]。
- **「早一點發現復發會比較好」沒有被證明**——NICE 逐字：「There is no definitive evidence that identifying recurrent
  disease early improves outcomes」[E-S15]。這句話必須寫，否則 E2 會變成鼓勵密集追蹤。
- 停止條件在腦膜瘤有（NICE）、在聽神經瘤沒有、在腦下垂體瘤是「證據不足」＋「可能要一輩子」[E-S15][E-S17][E-S18][E-S24]。

### Claim ceiling（E2）

- **可寫**：三張表照抄（腦膜瘤 NICE 表 7；聽神經瘤 CNS 三種情境；腦下垂體偶然瘤 Endocrine Society 的 6 個月／1 年／每年／1–2 年），
  **每一張都標明是哪一國、哪個學會、哪一年、涵蓋哪一種瘤**；
  「腦膜瘤第 9 年之後，NICE 寫的是『考慮結案』；無症狀偶然發現的腦膜瘤，12 個月沒變化就可以考慮結案或第 5 年再照一次」；
  「非功能性腦下垂體腺瘤的追蹤要多久、多密，**現行指引明說證據不足**；而一份 148 人的資料顯示復發中位在 80 個月、
  逐年風險不會下降，作者主張要終身定期影像」；
  「放射手術之後的腫瘤變大，**在聽神經瘤是常見現象**（前瞻世代 3 個月平均漲 23%；另一個 259 人世代早期假性進展 35.5%），
  而指引的作法是連續三次影像都在長之前先不要再治療」。
- **不可寫**：
  - 把 NICE 的表寫成「你的追蹤表」——那是英國的國家指引，**台灣的排法由主治醫師決定**；
  - 把「Consider discharge」寫成「就可以不用再追蹤了」——原文是「考慮」，而且同一節同時寫著
    「任何時候出現新的或改變的神經症狀，隨時安排回診與影像」[E-S15]；
  - 把聽神經瘤或腦下垂體瘤套用腦膜瘤的停止條件（紅線 9 的延伸）；
  - **任何比 `sit-pseudo` 更寬鬆的假性進展措辭**——不可寫「所以變大不用緊張」「可以再等等看」；
    可寫的是「這件事存在、有分母、判讀是醫師與連續影像的事」；
  - 把 CNS 的「12、24、36 個月」寫成病人可以自己延後回診的依據；
  - 用聽力保存率去比較三條路的優劣（那是 C2 的主場，紅線 5）。

### Caveats／safety notes

- NICE NG99 的表 7 標題是「**Possible** regular clinical review schedule」，條文動詞是「**Consider**」，不是「Offer」——照抄時要保留這個語氣。
- CNS 指引全部是 **level III**（作者自評 low certainty, low quality）[E-S17]。
- Endocrine Society 2011 是**十五年前的文件**，寫的時候要標年份；本次未檢出更新版。
- 聽力追蹤頻次是明確的 **gap**。

### 台灣端（E2）

| 項目 | 結果 | 路徑 |
|---|---|---|
| **追蹤影像（MRI）有沒有頻次限制條文** | **查到項目，查不到頻次限制**：支付標準全表中 **33084B「磁振造影－無造影劑」6,500 點**、**33085B「磁振造影－有造影劑」11,500 點**，兩者的規範欄逐字只有「1.本項須限經保險人同意之醫療院所實施。2.申報費用時必須附上報告結果。」——**條文裡沒有任何關於間隔或次數的限制**。另有 33146B（Primovist 造影劑加計）、P2102C／P2104C（跨院影像提供費） | 健保署支付標準全表 TXT（政府資料開放平臺 dataset，`info.nhi.gov.tw/api/iode0000s01/Dataset?rId=A21030000I-D20020-002`，22 MB、6,163 筆），2026-09-13 下載後全文檢索 [E-S64] |
| **聽力檢查給付項目** | **查到**：22001C 純音聽力檢查 405 點、22011B 語言分辨聽力檢查 279 點、22013B 語言聽力檢查 300 點、22014B 誘發反應聽力檢查 706 點、22023B 耳蝸誘發聽力檢查 2,012 點、22008B 聲場聽力檢查 2,270 點、20031B 穩定狀態聽性誘發反應 1,000 點、54045B 人工電子耳術後調圖（單耳）1,311 點 | 同上 [E-S64]。**頻次限制未逐項抓取規範欄，正文若要寫「多久可以做一次」必須先抓；本 brief 不背書** |
| 追蹤的荷爾蒙檢驗項目 | **未查**（歸 D 組） | — |
| 「良性腦瘤在不在癌症登記內」 | **未查**（歸 A 組台灣端） | — |

### 給繪圖組（E2）

SPEC §七 沒有分配圖給 E2。若要做一張三欄並列的追蹤時程表，**只能用上面三段的 PASS 原文數字**，
而且三欄必須各自標學會與年份（NICE 2018/2021｜CNS 2026｜Endocrine Society 2011），
**並在圖上標出「停止條件：腦膜瘤有／聽神經瘤無／腦下垂體瘤＝證據不足」**。

---

## E3 `bt-recurrence`〈復發之後：再開刀、再照射，以及沒有藥這件事〉

> **寫作者先讀** `sit-reirradiation`〈照過的地方，能不能再照〉。那一頁的立場是：
> 「這件事沒有通則，必須逐案評估」「歐洲共識自己寫著再照射的前瞻證據稀少」
> 「我沒有在這一篇印任何劑量或間隔月數，那是刻意的」。**E3 的再照射段落沿用同一個紀律：不印劑量、不印間隔。**
> 高分級復發腦膜瘤的 BNCT **一句指向 `nt-bn-meningioma`〈腦膜瘤：等不到的那個大型試驗〉，不重寫**。

### Key facts

**一、復發的定義與時機（三種瘤各自，不可互相套用）**

- **腦膜瘤**：復發風險由 WHO 分級與切除程度決定（Simpson 的細節歸 B2）；ICOM 逐字「higher grades associated with
  higher rates of recurrence」，但同時寫明 Simpson 分級在現代手術中「has become somewhat controversial」[E-S40]。
  **預後的量級**：登記資料中的「malignant」meningioma 分類並非純 WHO 第 3 級（含 grade 1 20.4%、grade 2 15%），
  而**純 WHO 第 3 級的非登記世代，5 年總存活 66%、估計 10 年總存活僅 14–24%**[E-S40]。
  **再手術的時間點（間接證據）**：顱底腦膜瘤世代中，**初次切除到第一次再手術的中位時間 4.4 年，
  第一次到第二次再手術 4.1 年**[E-S28]。
- **聽神經瘤**：SRS 失敗後走到補救手術的中位間隔 **48 個月（範圍 24–120）**（28 人，六家歐洲中心）[E-S30]。
- **腦下垂體瘤（非功能性）**：GTR 之後**中位復發時間 80 個月（範圍 36–156 個月）**，8.1%（12/148）[E-S24]；
  另一世代 436 人中復發 19.0%（中位追蹤 53 個月），術後殘餘者 36.4%[E-S25]。
  **關鍵形狀**：無復發影像累積越久，**逐年復發風險並沒有下降**（年增 1.07%）[E-S24]。

**二、再手術：結果與併發症（每一筆都帶分母）**

- **腦膜瘤·非顱底（UCSF，67 位病人、111 次再手術，中位追蹤 9.8 年）**[E-S27]：
  最後一次再手術的 WHO 分級 第1級 22%、第2級 51%、第3級 27%；**22% 的病例在再手術時分級升高**。
  **111 次再手術中發生 48 件併發症，分布在 32 位病人（48%）**；其中 26 件（54%）需要再一次手術處理。
  細項：神經功能缺損 14%（**永久性 8%**）、傷口裂開／感染 14%、腦脊髓液漏／假性腦膜膨出／水腦 9%。
  **無圍手術期死亡**。第一次再手術後中位存活 11.5 年，2／5／10 年存活 91.0%／68.8%／50.0%。
  併發症的獨立風險因子：腫瘤跨越矢狀面中三分之一（OR 6.97，95% CI 1.5–32.0，p=0.006）、
  以認知改變表現（OR 20.7，95% CI 2.3–182.7，p=0.001）。
- **腦膜瘤·顱底（同院，78 位病人、100 次再手術，中位追蹤 8.5 年）**[E-S28]：
  WHO 第1級 72%、第2級 22%、第3級 6%；44%（44 顆）在第一次再手術時最大徑 ≥3 cm。
  **100 次再手術中 60 件併發症發生在 30 個病例**，其中 20 件（33%）需要手術處理：
  水腦 12、腦脊髓液漏／假性腦膜膨出 11、傷口感染 9、術後血腫 4、靜脈梗塞 1、氣腦 1；
  新增或惡化的顱神經缺損 10、偏癱 3。**無圍手術期死亡**。多變項分析：後顱窩位置與併發症顯著相關（OR 3.45）。
- **聽神經瘤·再次顯微手術（10 篇、359 人的統合分析）**[E-S31]：
  **彙整 GTR 率 0.71（95% CI 0.46–0.87）**；4 篇 49 人報告 PFS，**沒有再復發**（彙整比例 1.00）；
  **術後顏面神經功能惡化 43%（95% CI 0.29–0.58）**；腦脊髓液漏 11%（0.05–0.21）。
  作者結論逐字：「Repeat microsurgery for recurrent VS provides good tumor control but carries **higher risks of
  facial nerve deterioration and other complications compared with primary surgery**.」
- **聽神經瘤·放射手術失敗後的補救手術（28 人，六家中心，2012–2022）**[E-S30]：
  手術指徵 27/28 是影像上再長大；軸向徑由 SRS 前中位 18.5 mm 增到手術前 25 mm。
  **GTR 13/28（46.4%）**；**併發症 3/28（10.7%）**；
  **聽力：SRS 前 serviceable hearing 10/20（50.0%）→ 術前 4/24（16.7%）→ 術後有追蹤的 14/28 全部 AAO-HNS D 級**；
  顏面神經：術前 HB I 級 25/28（89.3%），出院時 HB I–II 14/27（51.9%），12 個月時 11/15（73.3%），
  **3/15（20.0%）停在 HB V–VI 級**。作者結論：**「hearing preservation is not a realistic goal in this setting」**。
- **腦下垂體瘤·再次經鼻內視鏡手術（211 次初次 vs 57 次再次，非功能性腺瘤）**[E-S29]：
  手術併發症率**相當**、無死亡；但再次手術者
  **新發全垂體功能低下 7.1% 對 0.5%（P=.011）**、**GTR 率 26.3% 對 59.2%（P=.001）**、
  術後再做放射手術的比例 36.8% 對 24.2%（P=.009）；**2 年 MRI 無惡化存活兩組相當（95.4% 對 97.9%，P=.807）**。

**三、再照射：可行性、劑量限制、併發症（與 `sit-reirradiation` 一致）**

- **總則沿用站上那一頁**：歐洲放射腫瘤學會與 EORTC 2022 共識自己寫「再照射的前瞻性證據稀少」；
  七位專家看同一個病例、五位願意再治療，**分次方式與劑量上限沒有一個相同**。**E3 一句指路，不重寫。**
- **腦部再照射的既有結論（站上已引，E3 可沿用其結論但不重印數字）**：治療體積越小、可給的累積劑量越高；
  同一份回顧**沒有發現兩次治療的間隔與壞死發生率相關**——所以「隔幾個月就安全了」的說法站不住。
- **腦膜瘤專屬的再照射資料（本次新查到，可引書目與方向，但分母小）**：
  - 「Re-irradiation of anaplastic meningioma: higher dose and concomitant Bevacizumab may improve progression-free
    survival」Radiation Oncology 2024;19(1):135（OA；PMID 39358739，DOI 10.1186/s13014-024-02486-7）——**本次只取得書目，內文數字未取得，不可引用其數值**（FAIL-7）。
  - 「Proton therapy re-irradiation provides promising clinical results in recurrent brain meningioma」
    Acta Oncologica 2023;62(9):1096–1101（PMID 37526998，DOI 10.1080/0284186x.2023.2241994）——同上，只有書目（FAIL-8）。
  - →**E3 對腦膜瘤再照射只能寫「有系列報告、方向偏可行、但沒有隨機資料，而且我這次拿不到可以引用的數字」，
    並把細節推回 `sit-reirradiation` 與主治醫師。**
- **與 B3 的分工**：**E3 不得自行比較單次與分次**（SPEC §六），也不比較質子與光子。

**四、系統性藥物在腦膜瘤——逐筆帶證據等級與是否達到主要終點**

| 藥／試驗 | 設計 | n（族群） | 主要終點 | 結果 | 達標？ |
|---|---|---|---|---|---|
| **Sunitinib**（Kaley 2015）[E-S32] | 前瞻、多中心、研究者發起、**單臂第二期** | 36（復發 WHO 2–3 級，中位已復發 5 次，範圍 2–10） | PFS-6 | **42%**；中位 PFS 5.2 個月（95% CI 2.8–8.3）、中位 OS 24.6 個月（16.5–38.4） | **達標**。**但毒性要並列**：1 例第 5 級（致死）瘤內出血、2 例第 3 級與 1 例第 4 級中樞／瘤內出血、1 例第 3 級與 1 例第 4 級血栓性微血管病變、1 例第 3 級腸胃道穿孔。作者結論：「A randomized trial should be performed.」 |
| **Bevacizumab**（Kumthekar 2022）[E-S33] | 多機構**單臂第二期** | 50 人收案（42 人為進展性腦膜瘤：第1級 10、第2級 20、第3級 12；另含 4 例前庭神經鞘瘤、4 例血管外皮細胞瘤，併入同級分析） | PFS-6 | **第1級 87%、第2級 77%、第3級 46%**；中位 PFS 22／23／8 個月；中位 OS 35／41／12 個月。最佳影像反應以穩定疾病為主（第1級 100%、第2級 85%、第3級 82%），部分反應僅第2級 5% | **作者判定為 promising**。常見毒性：高血壓 42.2%、蛋白尿 35.6%、疲倦 31.1%。**注意：ICOM 表列的第1級數字是 90%，與原文的 87% 不符；另有 2023 年勘誤（Neuro-Oncol Adv 2023;5(1):vdad103）。以原文 87/77/46 為準**[E-S33][E-S69] |
| **Alliance A071401（FAK 抑制劑 GSK2256098）**（Brastianos 2023 JCO）[E-S34] | **第一個以基因分型驅動的第二期籃式試驗**；本臂限體細胞 *NF2* 突變 | 篩檢 322 人 → 36 人入組（第1級 12、第2/3級 24） | 共同主要終點：PFS-6（依分級分層）＋反應率 | **第1級 PFS-6 83%（10/12，95% CI 52–98）；第2/3級 33%（8/24，95% CI 16–55）**；全體 1 人部分反應、24 人穩定疾病 | **兩個分級族群都達到 PFS-6 效力門檻**。7 人有第 3 級相關不良事件，無第 4／5 級。作者結論：「FAK inhibition **warrants further evaluation**」——**不是可用的治療** |
| **Everolimus＋octreotide（CEVOREM）**（Graillon 2020）[E-S36] | **單臂第二期** | 20（第1級 2、第2級 10、第3級 8；4 人帶 *NF2* 生殖系突變） | PFS-6 | **55%（95% CI 31.3–73.5）**；6／12 個月存活 90%／75%；78% 的腫瘤生長速率下降 >50%（中位由 16.6%／3 個月降到 0.02%／3 個月，P<0.0002） | **達標**；作者結論「warrants further studies」 |
| **Octreotide 單用**（Simó 2014）[E-S37] | 前瞻兩階段第二期 | **9**（第2級 5、第3級 4，全部 octreotide SPECT 陽性） | 影像部分反應（RPR） | **0 例 RPR**；最佳反應為穩定疾病 33.3%（3/9）；PFS-6 44.4%；中位至惡化 4.23 個月；10 個月時全部惡化 | **未達標**。作者結論：不支持每月長效 SSA 用於復發高分級腦膜瘤 |
| **Hydroxyurea** | **沒有單獨的前瞻試驗可引**。可引的是兩個含 HU 的組合單臂第二期：Reardon 2011（imatinib＋HU，n=21，PFS-6 **61.9%**，第1級 87.5%／第2-3級 46.2%，判定達標）與 Jensen 2016（HU＋verapamil，**n=7**，PFS-6 85%，判定未達標）[E-S40 表 3] | — | — | — | **E3 的寫法：「hydroxyurea 沒有自己的隨機資料，能引的只有把它當搭檔的小型單臂試驗，其中一個 n 只有 7」** |
| **Mifepristone（抗黃體素）SWOG S9005**（Ji 2015 JCO）[E-S38] | **雙盲、隨機、安慰劑對照第三期** | **164**（80 mifepristone / 84 安慰劑；無法切除之腦膜瘤） | 至治療失敗時間、總存活 | 完成 2 年而未惡化者 mifepristone 30%（24/80）、安慰劑 33%（28/84）；**兩組的 failure-free 與 overall survival 均無統計差異** | **陰性**。作者結論：「Long-term administration of mifepristone was well tolerated but **had no impact** on patients with unresectable meningioma.」**這是本專題唯一一個第三期隨機試驗，必須寫** |
| **Trabectedin EORTC-1320-BTG**（Preusser 2022）[E-S35] | **隨機（2:1）、多中心、開放標籤第二期**，對照組為 local standard of care | **90**（61 trabectedin / 29 LOC；復發 WHO 2–3 級） | PFS | **中位 PFS：LOC 4.17 個月 vs trabectedin 2.43 個月（HR 1.42，80% CI 1.00–2.03，P=.294）**；PFS-6 29.1% vs 21.1%；中位 OS 10.61 vs 11.37 個月（HR 0.98，P=.94）；**≥3 級不良事件 44.4% vs 59.0%** | **陰性且方向不利**。作者結論：「Trabectedin **did not improve PFS and OS and was associated with higher toxicity** than LOC」 |
| **Pembrolizumab**（Limon 2024）[E-S39] | 前瞻**單臂第二期**，單一機構 | **18**（15 復發腦膜瘤＋3 退行性孤立性纖維瘤） | PFS-6 | **PFS-6 與 PFS-12 皆 11.1%**；中位 PFS 2.6 個月；整體反應率 11%（2 人穩定、2 人部分反應）；第 3 級毒性 16.7% | **未達標；試驗因無效與收案緩慢終止** |
| **Nivolumab**（Reardon 2021，經 ICOM 表列）[E-S40] | 單臂第二期 | 25（復發 WHO 2–3 級） | PFS-6 | **42.4%** | **未達標**（ICOM 標記為「−」）。2 位高腫瘤突變負荷者為長期存活者 |

- **指引的定調（可直接引）**：EANO 2021 腦膜瘤指引摘要逐字——「**all approaches of systemic pharmacotherapy** [are experimental].
  The best albeit modest results with pharmacotherapy have been obtained with bevacizumab or multikinase inhibitors
  targeting vascular endothelial growth factor receptor, but **no standard of care systemic treatment has been yet defined.**」[E-S41]
- **ICOM 2024 的定調（OA 全文，可直接引）**：「novel systemic agents have emerged as a possible option for recurrent or
  aggressive subtypes, **all of which remain under investigation**」；
  「Cytotoxic and hormonal agents, including trabectedin, somatostatin agonists, and progesterone antagonists,
  have demonstrated **less clinical efficacy**」[E-S40]。
- **ICOM 對 PFS-6 這個終點本身的批評（非常好用）**：「Given the **poor reliability of historical benchmarks such as PFS-6**,
  ideally randomized trials should be conducted whenever possible.」[E-S40]
  →**這句話是 E3 整節的骨架：上面所有「達標」的試驗，達的都是一個歷史對照的門檻，不是跟另一組人比出來的。**
- **進行中的（一律寫「進行中」）**：NCT02523014（A071401 的 vismodegib／capivasertib／abemaciclib 臂）、
  NCT02648997（nivolumab＋ipilimumab）、NCT02847559（bevacizumab＋電場）、NCT03971461（177Lu-DOTATATE）、
  NCT03267836（avelumab＋質子）、POPLAR-NF2（REC-2282，HDAC 抑制劑，*NF2* 突變腦膜瘤）[E-S40]。

**五、聽神經瘤的 bevacizumab（與 E5 交叉；此處只放一句，數字在 E5）**

- 用於 **NF2 相關**的前庭神經鞘瘤，**不是偶發型**。EANO 2020 聽神經瘤指引摘要逐字：
  「**Except for bevacizumab in neurofibromatosis type 2, there is no role for pharmacotherapy.**」[E-S42]
- 偶發型聽神經瘤只有極小的個案級資料（Kumthekar 的 42+8 人試驗裡含 4 例前庭神經鞘瘤，**併入腦膜瘤分級分析，無法單獨解讀**）[E-S33]。
  →**E3 一句：「藥物這條路在聽神經瘤幾乎只對 NF2 相關的人開，細節在 E5」。**

**六、高分級復發腦膜瘤的 BNCT**

**一句指路 `nt-bn-meningioma`，不重寫。** 那一頁已寫明：44 人的病例系列、無對照組、
BNCT 後中位總存活 29.6 個月、第2級放射性壞死 34.1%／第3級 13.6%。**E3 不得複製這些數字。**

### 反方向的資料（誠實必列）

- 再手術不是沒有代價：非顱底 48% 的病人至少發生一件併發症、8% 永久神經功能缺損[E-S27]；
  顱底 100 次手術 60 件併發症[E-S28]；聽神經瘤再次手術顏面神經惡化 43%[E-S31]。
- 但**兩個腦膜瘤再手術世代都沒有圍手術期死亡，而且長期存活可觀**（非顱底第一次再手術後中位 11.5 年）[E-S27]。
  **兩邊都要寫**，否則這一篇不是嚇人就是鼓勵。
- 系統性藥物的「達標」都是單臂對歷史門檻；**唯二的隨機資料（mifepristone 第三期、trabectedin 隨機第二期）都是陰性**[E-S38][E-S35]。

### Claim ceiling（E3）

- **可寫**：三種瘤各自的復發時機（帶分母與中位數）；
  再手術的併發症率（**每一筆帶「哪一種瘤、顱底或非顱底、幾個病人幾次手術」**）；
  「聽神經瘤在放射手術失敗之後還能開，但**保住聽力不是這個手術的目標**——28 人的系列裡術後全部落在最差的聽力等級」；
  「非功能性腦下垂體腺瘤再開一次，併發症率與第一次相當，**但全垂體功能低下的機率從 0.5% 升到 7.1%、全切除率從 59% 降到 26%**」；
  「腦膜瘤沒有標準的系統性治療——這是 EANO 2021 指引的原話」；
  「試過的藥很多：sunitinib、bevacizumab、somatostatin 類似物、hydroxyurea、trabectedin、mifepristone、免疫治療；
  **達標的都是單臂試驗對歷史門檻，唯二做出隨機比較的兩個都是陰性**」；
  「Alliance A071401 是第一個依照腫瘤基因分型分配治療的腦膜瘤第二期試驗，*NF2* 突變臂兩個分級都達到門檻，
  **作者的結論是值得進一步研究，不是可以拿來用**」。
- **不可寫**：
  - 「腦膜瘤沒有藥」（過頭了）或「已經有藥了」（也過頭）；正確是「**沒有標準治療；有幾個訊號；唯二的隨機資料是陰性**」；
  - 把 PFS-6 說成「有效率」或「存活率」；
  - 把單臂試驗寫成「比不治療好」；
  - 自行比較單次與分次放射治療、或比較質子與光子（歸 B3）；
  - **印任何再照射的劑量或間隔月數**（沿用 `sit-reirradiation` 的刻意省略）；
  - 重寫 BNCT 的數字（歸 `nt-bn-meningioma`）；
  - 把 bevacizumab 在 NF2 的資料外推到偶發型聽神經瘤或腦膜瘤病人；
  - 任何一句可以讀成「復發了就一定要再開／一定要再照」的話。

### Caveats／safety notes

- 所有再手術世代都是**單一或少數醫學中心的回溯資料**，選擇偏差明顯（能被再開的人本來就被挑過）。
- [E-S30] n=28、[E-S37] n=9、[E-S39] n=18、Jensen 2016 n=7——**小分母必須寫在數字旁邊**。
- 復發之後的決定要走多專科討論：一句指向 `sit-mdt`；想聽第二意見指向 `sit-second-opinion`；
  高齡者的取捨指向 `sit-elderly`；找試驗的方法指向 `sit-trial-how`（檔案已確認存在）。

### 台灣端（E3）

| 項目 | 結果 | 路徑 |
|---|---|---|
| **立體定位放射手術的支付項目與適應症（逐字）** | **查到，且版本更新**：**37028B「三度空間Ｘ光刀立體定位放射手術」82,000 點**、**37029B「影像導引強度調控X光刀立體定位放射手術」153,229 點**，**兩者生效日皆為 20260401**。37028B 規範逐字：「1.含括一般及特殊材料費。2.須符合適用範圍：(1)以顱內病灶直徑小於三公分或容積十五立方公分以下之病灶數目小於或等於三處之動靜脈畸型（含腦膜動靜脈廔管）、**聽神經瘤、腦膜瘤、腦下垂體瘤**、顱咽管瘤或其他腫瘤(應附相關療效文獻佐證)…且須符合下列條件之一：**A.曾接受開顱手術，但有殘餘腫瘤或腫瘤復發者。** B.開顱手術可能造成神經損傷或危險性大者。C.有嚴重心肺疾病或其他內科疾病，不適合侵入性手術或全身麻醉者。…**F.顱內單側小腦橋腦角聽神經瘤寬度小於2.5公分（不含內耳道）者。**(2)不適用手術或其他傳統治療方式之三叉神經痛。**3.全部個案須事前專案向保險人申請。**4.須有專任放射線治療醫師與專任輻射劑量計算人員，並向保險人申請核可實施。」37029B 的大小門檻為「三度空間直徑不大於3.5×3.5×3.5公分或容積二十立方公分」，並多一條「**3.加馬機立體定位放射手術（Stereotactic radiosurgery with γ-knife）項目比照申報。**」 | 支付標準全表 TXT，2026-09-13 下載後以代碼比對 [E-S64] |
| **再照射有沒有獨立支付項目** | **零筆（重新確認）**：以「**再照射**」「**再次放射**」全文檢索支付標準全表，**各 0 筆**。沿用 `sit-reirradiation` 的結論，但**版本要更新**：本次檢索的是 2026-09-13 下載的全表（含 115.04.01 生效條目），不是站上那一頁引的 114.03.13 版 | 同上 [E-S64]。寫法：「**條文上沒有這個項目；你的療程怎麼申報，問醫務課**」，**不推論** |
| bevacizumab 有沒有涵蓋腦膜瘤／聽神經瘤／NF2 | **零筆（逐字）**：藥品給付規定第 9.37 條（`9.37._20251001.pdf`，條文標註日期含 100/6/1…114/10/1）共 7 個適應症群組：轉移性大腸或直腸癌、**惡性神經膠質瘤(WHO 第4級)-神經膠母細胞瘤**、卵巢上皮細胞／輸卵管／原發性腹膜癌、持續性復發性或轉移性子宮頸癌、晚期轉移性或復發性非鱗狀非小細胞肺癌、與 atezolizumab 併用之肝細胞癌、第 7 群組。以「腦膜瘤／神經鞘瘤／聽神經／神經纖維瘤／NF2／schwannoma／meningioma／良性」逐字檢索**全部 0 筆** | NHI 藥品給付規定 API（DRUG_ING=bevacizumab）→ 規定碼 9.37.、14.9.7.（後者為早產兒視網膜病變，與本專題無關）→ getPDF → pdftotext 全文檢索，2026-09-13 [E-S62] |
| sunitinib／everolimus／octreotide 等在腦膜瘤的給付 | **未逐一查證**（本次優先查 bevacizumab）。**正文不得提及這幾個藥的台灣給付狀態**，只能寫「這些藥在腦膜瘤都還在研究階段，台灣怎麼算，問醫務課」 | — |
| 重大傷病：良性腦瘤在不在項次內 | **未查**（SPEC §八 列為全專題最實際的一題，歸 A 組／C 組台灣端）。E3 一句指向 `sit-paperwork` 與個管師 | — |


#### 〈與 B／C／D 組的版本差異（已由編輯裁定以本節為準）〉

**跨組裁決**：B／C／D 三組引用的是 **20230301 生效**版；本節查到的是 **20260401 生效**版。
**項目名稱與「比照申報」的對象在新版對調了**，四點釘死如下（查證日 **2026-09-13**）。

**① 20260401 版就是現行版，且同代碼沒有多版並存。**
本次下載的支付標準全表共 **6,163 筆**，`37028B`、`37029B` **各只出現 1 筆**，
生效日皆為 **20260401**、截止日 **29101231**（＝現行有效）。
全表中 **37 開頭代碼的最大生效日就是 20260401**；全表整體最大生效日為 20260901（屬 30301B–30303B 等基因檢測項目，非放療）。
→**沒有比 20260401 更新的放療版本，也沒有 20230301 版並列存在於現行全表中**（舊版已被取代，不在此資料集）。

**② 兩個代碼的現行版逐字全文**

> **37028B｜支付點數 82,000 點｜生效日 20260401｜截止日 29101231**
> **診療項目名稱：三度空間Ｘ光刀立體定位放射手術**
> **規範／備註全文**：
> 「1.含括一般及特殊材料費。2.須符合適用範圍：(1)以顱內病灶直徑小於三公分或容積十五立方公分以下之病灶數目小於或等於三處之動靜脈畸型（含腦膜動靜脈廔管）、聽神經瘤、腦膜瘤、腦下垂體瘤、顱咽管瘤或其他腫瘤(應附相關療效文獻佐證)，或顱內病灶(大小限制同前)數目小於或等於五處之轉移性腦瘤，惟轉移性腎臟細胞瘤及黑色素瘤不受病灶數目限制。且須符合下列條件之一：A.曾接受開顱手術，但有殘餘腫瘤或腫瘤復發者。B.開顱手術可能造成神經損傷或危險性大者。C.有嚴重心肺疾病或其他內科疾病，不適合侵入性手術或全身麻醉者。D.轉移性腦瘤，限Karnofsky Performance Scale(KPS) ≧70或ECOG 0-1者，且含其他病灶部位屬少部分惡化者(oligoprogression/惡化病灶總數不超過五個且惡化器官不超過三處）。E.海綿狀血管瘤限病灶位於深部腦核或腦幹，曾有出血病史者。F.顱內單側小腦橋腦角聽神經瘤寬度小於2.5公分（不含內耳道）者。(2)不適用手術或其他傳統治療方式之三叉神經痛。**3.全部個案須事前專案向保險人申請。**4.須有專任放射線治療醫師與專任輻射劑量計算人員，並向保險人申請核可實施。」
> **→ 37028B 的備註只有 4 點，沒有任何「比照申報」條款。**

> **37029B｜支付點數 153,229 點｜生效日 20260401｜截止日 29101231**
> **診療項目名稱：影像導引強度調控X光刀立體定位放射手術**
> **規範／備註全文**：
> 「1.含括手術技術費、定位技術費、一般材料費及特殊材料費等。2.須符合適用範圍：(1)以顱內病灶之三度空間直徑不大於3.5×3.5×3.5公分或容積二十立方公分，病灶數目小於或等於三處之動靜脈畸型（含腦膜動靜脈廔管）、聽神經瘤、腦膜瘤、腦下垂體瘤、顱咽管瘤或其他腫瘤(應附相關療效文獻佐證)、或顱內病灶(大小限制同前)數目小於或等於五處之轉移性腦瘤，惟轉移性腎臟細胞瘤及黑色素瘤不受病灶數目限制。且須符合下列條件之一：A.曾接受開顱手術，但有殘餘腫瘤或腫瘤復發者。B.開顱手術可能造成神經損傷或危險性大者。C.有嚴重心肺疾病或其他內科疾病，不適合侵入性手術或全身麻醉者。D.轉移性腦瘤，限Karnofsky Performance Scale(KPS) ≧70或ECOG 0-1者，且含其他病灶部位屬少部分惡化者(oligoprogression/惡化病灶總數不超過五個且惡化器官不超過三處）。E.海綿狀血管瘤限病灶位於深部腦核或腦幹，曾有出血病史者。F.顱內單側小腦橋腦角之聽神經瘤寬度小於2.5公分（不含內耳道）者。(2)不適用手術或其他傳統治療方式之三叉神經痛。**3.加馬機立體定位放射手術（Stereotactic radiosurgery with γ-knife）項目比照申報。** 4.全部個案須事前專案向保險人申請。5.須有專任放射線治療醫師與專任輻射劑量計算人員，並向保險人申請核可實施。」

> **抄錄註記**：全表 TXT 中「腦膜動靜脈**廔**管」的「廔」字被以替代字元輸出（顯示為 `?`），
> 本節已按上下文還原為「廔」。**正文若要逐字引用這一句，請標明此處為還原字**，或避開這四個字。

**③ 現行版的備註裡「電腦刀」三個字不在了——零筆。**
以「**電腦刀**」對全表**所有欄位**做原始字串檢索：**0 次**；
`CyberKnife`／`Cyberknife`／`cyberknife` 亦**各 0 次**。
反過來，「**加馬機**」在全表中**只出現 1 次**，就在 **37029B 的備註第 3 點**（上引逐字）；
「Stereotactic」與「γ-knife」同樣只出現在這一句。
→**B／C／D 組引用的「電腦刀……項目比照申報」那一句，在現行版全表中已檢索不到；
凡是寫出「電腦刀」的段落都必須改寫或刪除。**
（提醒：SPEC §一之 5① 本來就規定**不寫加馬刀／電腦刀／直線加速器的廠牌**，
所以正文本來就不該出現這些字；本節只用來解決跨組引用的版本一致性。）

**④ 現行版沒有「分次立體定位」或 fractionated stereotactic 的獨立項目——零筆（與 B 組在 20230301 版的結論一致）。**
檢索結果：「**分次立體定位**」0 筆；`fractionated`／`Fractionated` 各 0 筆；
`stereotactic`（小寫）0 筆、`Stereotactic`（大寫）1 筆（即 37029B 備註那一句）。
含「**立體定位**」字樣的診療項目共 17 筆，其中放療相關者只有
**37028B、37029B、37047B（身體立體定位放射治療，213,662 點，生效 20260401——身體部位，非顱內）**，
其餘為心導管（33091B、33139B、33140B）、乳房攝影切片（33125C）、副鼻竇手術（65080B、65081B）、
腦部立體定位切片／抽吸（83081B、83082B）與電腦治療規劃（36015B）等，皆非分次立體定位放射治療項目。
另可佐證的是質子項目自成一組（N21301–N21308，生效 20161205；及 36025B–36027B 生物等效劑量質子放射治療，生效 20260101），
**其中 N21306 的名稱是「質子腦部立體定位放射手術（療程約3次)」——這是全表中唯一把「療程次數」寫進名稱的立體定位項目。**
→**結論：現行版中，顱內立體定位「單次對分次」的分界在支付標準上沒有對應的獨立代碼；
寫作者不得以代碼推論健保如何區分單次與分次**（單次對分次的臨床分界歸 B3，且只談證據、不談代碼）。

**下載路徑與檢索方式（可覆核）**
- `GET https://info.nhi.gov.tw/api/iode0000s01/Dataset?rId=A21030000I-D20020-002`
  （HTTP 200，22,040,997 bytes，UTF-8 BOM、CRLF、`^` 分欄；解析後 6,163 筆）。
  人類可讀頁面：`https://www.nhi.gov.tw/ch/cp-18621-7e20c-4002-1.html`。
- 下載兩次（2026-09-13）內容 **md5 相同**（`9f4626701e39b19d3108c7346fa0f9d0`），排除單次下載失真。
- 欄位對應：`[0]`診療項目代碼、`[1]`支付點數、`[2]`生效日、`[3]`截止日、`[5]`診療項目名稱、`[6]`規範／備註。
- 檢索方式：以 Python 讀入後對 `[5]`／`[6]` 欄做子字串比對；「電腦刀」等關鍵字另對**整份原始檔字串**再做一次 `str.count()`，
  兩種方式結果一致。
- **本節以 [E-S64] 計，不另開新來源編號。**


##### 跨組補查第二批（2026-09-13，同一份現行版全表；仍計入 [E-S64]）

**① 37028B／37029B 現行版的大小與病灶數門檻——三個門檻全部還在，數字沒有變。**
逐字（取自兩條規範第 2 點「須符合適用範圍：(1)」開頭）：

> **37028B（三度空間Ｘ光刀立體定位放射手術，82,000 點，生效 20260401）**：
> 「以顱內病灶**直徑小於三公分或容積十五立方公分以下**之**病灶數目小於或等於三處**之動靜脈畸型（含腦膜動靜脈廔管）、
> 聽神經瘤、腦膜瘤、腦下垂體瘤、顱咽管瘤或其他腫瘤(應附相關療效文獻佐證)，
> 或顱內病灶(**大小限制同前**)**數目小於或等於五處之轉移性腦瘤**，惟轉移性腎臟細胞瘤及黑色素瘤不受病灶數目限制。」

> **37029B（影像導引強度調控X光刀立體定位放射手術，153,229 點，生效 20260401）**：
> 「以顱內病灶之**三度空間直徑不大於3.5×3.5×3.5公分或容積二十立方公分**，
> **病灶數目小於或等於三處**之動靜脈畸型（含腦膜動靜脈廔管）、聽神經瘤、腦膜瘤、腦下垂體瘤、顱咽管瘤或其他腫瘤(應附相關療效文獻佐證)、
> 或顱內病灶(**大小限制同前**)**數目小於或等於五處之轉移性腦瘤**，惟轉移性腎臟細胞瘤及黑色素瘤不受病灶數目限制。」

**→ 裁定**：B 組從舊版抄來的三個門檻（37028B <3 cm／≤15 cc；37029B 3.5×3.5×3.5 cm／20 cc；病灶數 ≤3）
**在 20260401 現行版逐字相同，不需要改**。**變的只有項目名稱與備註第 3 點的「比照申報」對象**（見上一節①–③）。
另兩個容易漏抄的細節：轉移性腦瘤是 **≤5 處**（且腎細胞癌與黑色素瘤不受數目限制）；
兩條各自的 F 款都寫著「顱內單側小腦橋腦角（之）聽神經瘤**寬度小於2.5公分（不含內耳道）**」——**這是聽神經瘤專屬的第二層門檻，C 組若要寫大小分界必須連這一句一起引**（紅線 5：不可把大小分界寫成硬規則，照條文原文引）。
（「廔」字在全表 TXT 中被輸出為替代字元，此處已還原；逐字引用時比照上一節的抄錄註記。）

**② 83057B 在現行版沒有變，而且條文確實沒有內視鏡／顯微鏡分項——D3 那句話成立。**

> **83057B｜支付點數 30,571 點｜生效日 20220301｜截止日 29101231**
> **診療項目名稱：經由蝶竇之腦下垂體瘤切除**
> **規範全文**：「1.限神經外科專科醫師施行。 2.一般材料費及特殊材料費，得另加計百分之八十六。 3.上開特殊材料為單一使用之拋棄式特殊材料。」

- **全表中與腦下垂體手術有關的診療項目只有這一個**：品名含「腦下垂體」1 筆、含「垂體」1 筆、含「經蝶竇」**0 筆**、含「蝶竇」2 筆（另一筆為 65052B 蝶竇手術 5,379 點，耳鼻喉科項目）。
- **沒有任何「內視鏡下」／「顯微鏡下」的腦下垂體手術分項**：品名含「內視鏡」49 筆、含「顯微鏡」12 筆，
  逐筆檢視**沒有一筆是腦下垂體或經蝶竇手術**（內視鏡多為消化道、鼻竇、支氣管、耳；顯微鏡多為眼科、耳科、檢驗）。
- **最接近「器械差異」的是兩個獨立的儀器使用費，不是術式分項**：
  **28037B 腦內視鏡 2,000 點（生效 20040701，規範：「限神經外科專科醫師施行。」）**；
  **56019B 腦神經及脊椎手術中特殊儀器使用費－精密手術顯微鏡 2,000 點（生效 20140801，規範欄為空）**；
  同組另有 **56018B 誘發電位手術監視機 4,000 點**。
- **→ 裁定**：D3 正文「條文沒有區分內視鏡與顯微鏡」**正確，可維持**；
  但建議補一句更精確的說法：「**手術項目本身沒有分，分的是手術中用到的儀器有沒有另外計費**」，並註明 83057B 的生效日是 **20220301**（不是 114.01.01——那是 D 組引用的全表版本日期，不是這一條項目的生效日）。
  **仍不得寫本院有沒有、也不得比較內視鏡與顯微鏡孰優**（SPEC §一之 5②）。

**③ 20007B 與 20031B 是兩個不同的項目，兩個在現行版都還在，點數剛好都是 1,000 點。**

| 代碼 | 診療項目名稱 | 點數 | 生效日 | 規範欄 |
|---|---|---|---|---|
| **20007B** | **腦幹聽覺誘發電位檢查** | 1,000 點 | 19950301 | 空 |
| **20031B** | **穩定狀態聽性誘發反應** | 1,000 點 | 20031201 | 空 |

- **→ 裁定：C 組的 20007B 與本 brief 的 20031B 都對，不是同一個代碼抄錯，而是兩個不同項目。**
  兩份 brief 都應同時列出這兩碼，避免讀者以為其中一份抄錯。
- 同一系列的相鄰項目（供交叉核對）：**20008B 中程聽覺誘發電位檢查 720 點**、**20009B 長程聽覺誘發電位檢查 720 點**；
  聽力科那一組另有 **22014B 誘發反應聽力檢查 706 點**、**22018B 腦幹反應檢查 1,792 點**、**22033B 幼兒聽力篩檢(腦幹聽反射) 800 點**。
  **品名含「誘發電位」共 9 筆、含「誘發反應」2 筆、含「腦幹」3 筆。**
  →**C 組若要寫「聽神經瘤會做哪些聽力檢查」，這一整組代碼要一起看，不能只挑一個。**

**④ 在現行版重跑的零筆／命中檢索（B 組在舊版做的結論，本次逐詞覆核）**

| 檢索詞 | 品名＋規範欄命中 | 全檔原始字串出現 | 結論 |
|---|---|---|---|
| `CDKN2A` | **0 筆** | 0 次 | **零筆，沿用成立** |
| `TERT` | **0 筆** | 0 次 | **零筆，沿用成立** |
| `甲基化` | **0 筆** | 0 次 | **零筆，沿用成立**（`methylation` 亦 0 次） |
| `Ki-67` | **0 筆** | 0 次 | **零筆，沿用成立**（`Ki67` 亦 0 次） |
| `MGMT` | **0 筆** | 0 次 | **零筆，沿用成立** |
| `前庭復健` | **0 筆** | 0 次 | **零筆，沿用成立** |
| `聽能復健` | **0 筆** | 0 次 | **零筆，沿用成立** |
| `淋巴` | **199 筆** | 227 次 | **不是零筆**。命中集中在 P1（78 筆，論病例計酬／給付組合）、70 與 78（外科淋巴結相關術式）、12 與 25（免疫與細胞學檢驗）等，**與腦膜瘤／聽神經瘤／腦下垂體瘤的追蹤或復健無關**。→**這個詞在本專題沒有可用的結論，不要寫。** |

**順帶查的顏面神經與前庭相關（B 組未查，補上）**

- **顏面神經**：品名含「顏面神經」**只有 1 筆**——**83087B 顏面神經減壓術 10,900 點（生效 20220301；規範：一般與特殊材料費得另加計 144%，特殊材料限單次使用拋棄式）**。
  另有 **83035B 顏面舌下神經吻合術 12,333 點（生效 20260901；規範：「限神經外科或整形外科專科醫師施行」）**。
  **品名含「顏面神經復健」或專屬的顏面神經復健項目：0 筆**（復健是走 42／43 開頭的通用治療項目，不分部位）。
- **前庭**：品名含「前庭」8 筆，其中與本專題相關者為
  **22017C 前庭平衡檢查 450 點（生效 20211101）**、**22037B 前庭誘發肌電位－頸性或眼性 720 點**、**22040B 前庭誘發肌電位－頸性及眼性 1,188 點**（後二者生效 20180601）；其餘為耳鼻喉局部治療與婦科項目（同名字元巧合）。
- **復健／平衡訓練**：「復健」欄位命中 82 筆、「平衡訓練」21 筆，**全部落在 42（物理治療）與 43（職能治療）的通用治療強度分級項目**
  （簡單／中度／複雜，以治療項目數與時間計），**沒有任何前庭或聽能專屬的復健代碼**。
  →**C3 若要寫「治療之後的平衡與顏面神經復健」，可引的只有這幾個通用項目，不可寫成有專屬給付。**
- **英文字 `face`**：欄位命中 0 筆；全檔出現 59 次全部是英文品名中的其他字（`surface`、`surfaces`、`Except face`、`contracture, face, neck` 等），**與顏面神經無關**。

**檢索方式（與上一節同一份檔）**
同一份 2026-09-13 下載的支付標準全表（md5 `9f4626701e39b19d3108c7346fa0f9d0`，6,163 筆）。
以 Python 解析 `^` 分欄後，對**診療項目名稱 `[5]` 與規範／備註 `[6]` 兩欄**做子字串比對；
每個關鍵字**另對整份原始檔字串再做一次 `str.count()`**（會掃到所有欄位，含英文品名欄），兩種結果並列於上表。
代碼精確查詢則以 `[0]` 欄完全相等比對，並列出該代碼的**所有**列，用以確認同代碼是否有多版並存。

### 給繪圖組（E3）

SPEC §七 沒有分配圖給 E3。若要一張「腦膜瘤系統性治療的成績單」，
**只能用上表的 PASS 數字**，而且每一列必須同時標：**設計（單臂／隨機）、n、主要終點、是否達標**。
**陰性的兩筆（SWOG S9005、EORTC-1320）必須與陽性的並排在同一張圖裡，不可分開。**

---

## E4 `bt-radiation-induced`〈放射線引起的腦膜瘤與第二腫瘤〉【紅線 7，雙向】

> **紅線 7 的兩個方向，本 brief 兩邊都備齊了材料。**
> 方向一（**童年接受過頭部放療的人讀完要知道自己該做什麼**）：見「A. 放射線引起的腦膜瘤」。
> 方向二（**一個正在考慮放射手術的人不可以讀成「照了會長第二個瘤，所以別照」**）：見「B. 放射手術之後的第二腫瘤」。
> **兩段必須同篇、且 B 段的絕對風險與益處放在同一段**（見下方 Claim ceiling 的硬要求）。

### A. 放射線引起的腦膜瘤（RIM）

**一、診斷準則（Cahan 準則的現行用法，逐字）**

一份 2026 年的系統性回顧把**修正版 Cahan 準則**寫成四條，逐字[E-S43]：
> (1) the tumor developed **within a previously irradiated field**;
> (2) there was a **sufficient latency period** between irradiation and tumor appearance;
> (3) the **histology of the secondary tumor differed from that of the primary lesion**; and
> (4) the patient had **no predisposing conditions such as neurofibromatosis type 2, Li–Fraumeni syndrome, or Gorlin syndrome**.

同一篇明白寫出這套準則的鬆處：「**the minimum duration of a sufficient latency period remains undefined**,
and reported intervals vary widely across published studies」（該研究自訂 >6 個月）[E-S43]。
原始準則出自 Cahan WG 等 1948 年《Cancer》的 11 例放射後骨肉瘤報告（1998 年在同刊重印）[E-S52]。

**二、族群與分母（每一筆都標清楚是哪一個世代）**

- **以色列頭癬放療世代（低劑量、童年暴露）**[E-S44]：
  **10,834 位 1950 年代因頭癬接受 X 光治療者**＋兩個配對未照射對照組（人口對照與手足對照）。
  **腦部平均估計劑量 1.5 Gy**。中位追蹤 **40 年**。
  **良性腦膜瘤：ERR/Gy 4.63（95% CI 2.43–9.12）；EAR/Gy 每 10⁴ 人年 0.48（0.28–0.73）。**
  惡性腦瘤：ERR/Gy 1.98（0.73–4.69）；EAR/Gy 0.31（0.12–0.53）。
  惡性腦瘤的 ERR/Gy 隨照射時年齡增加而下降（3.56→0.47，P=0.037）；**良性腦膜瘤看不出年齡趨勢**。
  **兩者的 ERR 在暴露後 30 年以上仍然升高。**
- **同一個以色列世代的臨床描述（253 例 RIM）**[E-S45]：與 41 位無放射史的腦膜瘤對照相比，
  RIM 病人**診斷年齡較低、顱蓋部腫瘤比例較高、多發腦膜瘤比例較高**，復發率較高但未達統計顯著；
  **從暴露到腦膜瘤的平均潛伏期約 36 年**。
- **童年癌症存活者世代 CCSS（高劑量、含顱腦放療）**[E-S47]：
  **4,221 位接受過顱腦放療的存活者**中，169 人共 199 顆腦膜瘤。
  **從原發癌到腦膜瘤的中位間隔 22 年（5–37 年）**；
  **到 40 歲時的累積發生率 5.6%（95% CI 4.7–6.7%）**。
  **劑量反應**：以 1.5–19.9 Gy 為參考，20–29.9 Gy 的 HR 1.6（95% CI 1.0–2.6）、**≥30 Gy 的 HR 2.6（1.6–4.2）**，P<.001。
  **神經後果（這一段是「要知道自己該做什麼」的理由）**：診斷腦膜瘤前後六個月內，
  **20%（30/149）至少出現一項新的神經症狀**——癲癇 8.3%、聽覺／前庭／視覺缺損 6%、局部神經功能障礙 7.1%、嚴重頭痛 5.3%。
  與未發生腦膜瘤者相比，原發癌診斷 5 年後的風險：癲癇 HR 10.0（7.0–15.3）、
  聽覺／前庭／視覺感官缺損 HR 2.3（1.3–4.0）、局部神經功能障礙 HR 4.9（3.2–7.5）、嚴重頭痛 HR 3.2（1.9–5.4）。
  腦膜瘤診斷後中位追蹤 72 個月，**22 人（13%）死亡，其中 6 人死因歸因於腦膜瘤**。
- **CCSS 的劑量反應（巢式病例對照）**[E-S46]：14,361 位童年癌症 5 年存活者中，116 人出現續發中樞神經系統腫瘤
  （膠質瘤 40 例、**腦膜瘤 66 例**）。**腦膜瘤的中位發生時間為原診斷後 17 年**（膠質瘤 9 年）。
  放射暴露與續發腦膜瘤相關 **OR 9.94（95% CI 2.17–45.6）**；
  **ERR 的劑量反應為線性：腦膜瘤每 Gy 斜率 1.06（95% CI 0.21–8.15）**（膠質瘤 0.33，0.07–1.71）。
  校正劑量後，原發癌別與化療皆與風險無關。
- **彙整分析（1,809 位 RIM 病人，237 篇研究，1953–2025）**[E-S43]：
  - 原發放療原因：**頭部皮膚疾病（含頭癬）530 例（48.1%）**、急性白血病 378 例（34.3%）、
    髓母細胞瘤 137 例（12.4%）、低惡性度膠質瘤 98 例（8.9%）、鞍區／鞍上腫瘤 62 例（5.6%）、核災暴露 204 例（18.5%）。
  - **潛伏期（1,303 例有資料）：中位 22.7 年（範圍 0.6–63 年），平均 24.2±10.9 年。**
    依劑量分層（1,130 例）：**低劑量 <20 Gy 中位 36.3 年（n=458）；中劑量 20–40 Gy 中位 21.1 年（n=165）；
    高劑量 >40 Gy 中位 21.0 年（n=507）**，P<0.001。
  - **照射時年齡（980 例）：中位 8.3 歲（範圍 0.3–79 歲）**；年齡越大、潛伏期越長（Spearman ρ=0.405，P<0.001）。
  - **WHO 分級（1,017 例）：第 1 級 702 例（69%）、第 2 級 255 例（25.1%）、第 3 級 60 例（5.9%）**；
    高分級 RIM **85.0% 發生在高劑量組**（P<0.001）。
  - **多發性（1,047 例）：單顆 866 例（82.7%）、多顆 181 例（17.3%）**；高劑量組多發比例較高（P<0.001）。
  - **復發（440 例）：24.8%（109/440）**；依分級（241 例有資料）**高分級 51.5% vs 低分級 18.3%（P<0.001）**；
    **與放射劑量無關**（P=0.46）。
- **RIM 佔所有腦膜瘤的比例與生物學（ICOM 2024 逐字）**[E-S40]：
  「RIMs are biologically and clinically distinct from their sporadic counterparts and **while rare
  (making up only 1–2% of all meningiomas)**, present significant clinical challenges due to their
  **increased biological aggressiveness, multiplicity, and resistance to standard therapies.**」
  分子面：1p 缺失超過 50%、9p／19q／18q／10p／22q 缺失頻繁；
  **NF2 點突變與 22q 缺失反而比偶發型少，但 NF2 基因融合事件較多**（推測來自放射造成的雙股斷裂誤修復）；
  AKT1、SMO、TRAF7、KLF4 等非 *NF2* 突變在 RIM 基本上不出現[E-S40]。

**三、追蹤建議（「該做什麼」的可引來源）**

- **ICOM 2024 逐字（最接近建議的一句）**[E-S40]：
  「Given that RIMs in childhood cancer survivors may be diagnosed **40 years after their initial treatment**,
  **imaging follow-up at fixed intervals, with more frequent follow-up for those who received high-intensity treatment,
  may be warranted.**」——注意動詞是 **may be warranted**，不是 should。
- **ICOM 對「要不要篩」的保留（必須並列，防止 E4 變成鼓勵全面篩檢）**[E-S40]：
  「There is currently **insufficient evidence to support a standardized screening approach** such as germline genetic
  testing or routine neuroimaging, **even in higher risk cohorts**」。
- **NICE NG99 第 1.11 節「Surveillance for the late-onset side effects of treatment」（可直接引，這是最實用的一段）**[E-S15]：
  - 1.11.1 逐字列出可能在治療後數月到數年才出現的副作用，其中包含「**secondary tumours**」，
    同列的還有白內障、海綿狀血管瘤、認知退化、癲癇、聽力喪失、腦下垂體功能低下、不孕、神經病變、放射性壞死、SMART、中風。
  - 1.11.2「**Assess the person's individual risk of developing late effects when they finish treatment.
    Record these in their written treatment summary and explain them to the person**（and their relatives and carers, as appropriate）.」
  - 1.11.3 鼓勵接受過顱腦放療者維持健康生活型態（運動、飲食、戒菸）以降低中風風險；
    1.11.4 有中風風險者「consider checking their blood pressure, HbA1c level and cholesterol profile regularly」；
    1.11.5 認知退化風險者考慮持續神經心理評估；
    1.11.6「**If a person has had a radiotherapy dose that might affect pituitary function,
    consider checking their endocrine function regularly after the end of treatment.**」；
    1.11.7／1.11.8 有視力／聽力風險者分別轉眼科與聽力檢查。
- **RIM 的處置（ICOM 逐字）**[E-S40]：「Standard treatment guidelines for RIMs **do not currently differ from sporadic
  meningiomas**, with surgical resection as first line therapy for symptomatic cases. When multiple RIMs are present in
  the same patient, surgery should target the largest and/or symptomatic tumors first. Otherwise, **active surveillance
  remains a safe initial strategy** for these tumors, with a low rate of neurologic morbidity.」
  同段也寫了限制：「even CNS WHO grade 1 RIMs can demonstrate aggressive behavior and many of these cases are RT-resistant.
  SRS in select cases however appears to be safe and well tolerated… **Overall, tumor control rates following SRS are
  lower for RIMs than for sporadic meningiomas**, and larger treatment volume is associated with worse PFS.」

### B. 另一個方向：立體定位放射手術之後的第二腫瘤／惡性轉化

**一、絕對風險與分母（這一題的數字很小但常被放大，逐筆精確）**

- **五中心國際世代（Wolf 2019，Lancet Oncology）**[E-S48]：
  1987-08-14 至 2011-12-31 間接受加馬刀放射手術的 **14,168 人中，4,905 人符合分析條件**
  （**至少 5 年追蹤、且先前未接受過放射治療**）。
  診斷分布：前庭神經鞘瘤 1,011（20.6%）、**腦膜瘤 1,490（30.4%）**、動靜脈畸形 1,089（22.2%）、
  三叉神經痛 565（11.5%）、**腦下垂體腺瘤 641（13.1%）**、血管母細胞瘤 29（0.6%）、其他神經鞘瘤 80（1.6%）。
  **中位追蹤 8.1 年（IQR 6.0–10.6）。**
  結果：**3,251 位良性腫瘤病人中 2 人（0.0006%）被判為疑似惡性轉化**；
  **4,905 人中 1 人（0.0002%）被判為放射手術相關的顱內惡性腫瘤**（定義為發生在 2 Gy 等劑量線內）。
  發生率：**惡性轉化 6.87／10 萬人年（95% CI 1.15–22.71）；放射手術相關顱內惡性腫瘤 2.26／10 萬人年（0.11–11.17）**。
  另有 2 人（0.0004%）發生的顱內惡性腫瘤被判定與照射野無關。
  **整體放射手術相關惡性腫瘤發生率 6.80／10 萬人年（95% CI 1.73–18.50），10 年累積發生率 0.00045%（95% CI 0.00–0.0034）。**
  作者結論逐字：「the estimated risk… **remains low at long-term follow-up, and is similar to the risk of the general
  population to have a primary CNS tumour**」；並寫明「**prospective cohort studies with longer follow-up are warranted**」。
- **英國 Sheffield 世代（Rowe 2007）**[E-S49]：約 **5,000 位病人、30,000 人年追蹤**，
  **超過 1,200 人追蹤超過 10 年**，與全國死亡與癌症登記對比：
  **只出現 1 例新的星形細胞瘤，而依全國發生率預期為 2.47 例**。結論：未偵測到惡性風險上升。
- **單中心長期世代（Sherry 2020）**[E-S50]：1990–2014 年因良性中樞神經病灶接受加馬刀或直線加速器放射手術、
  且至少 5 年臨床追蹤者 **273 人**，中位追蹤 **11 年（範圍 5–27）**，共 **3,216 人年**：
  **放射相關惡性腫瘤 0 例；放射相關惡性轉化 2 例**，粗發生率 0.73%，即 **0.62／1,000 人年**；
  **Kaplan-Meier 5／10／15 年惡性轉化風險皆為 0.4%（95% CI 0.05–2.6%）**。
- **指引層級的一句（最適合放進紅線 7 的那一段）**[E-S51]：
  CNS 2026 立體定位放射手術指引更新的四條新 **level III** 建議之一逐字：
  「adult patients with sporadic VS undergoing SRS **should be informed that SRS does not result in an increased number
  of secondary malignancies compared with the rate expected in the overall population**」。

**二、把益處放進同一段的材料（紅線 7 的硬要求）**

同一份 CNS 2026 指引在同一批新建議裡還寫了三條，**寫作者應把它們與上面那一條放在同一段**[E-S51]：
- 「In adult patients with sporadic intracanalicular or <2 cm VS, **SRS should not be recommended as superior to
  observation alone for hearing preservation.**」（——**這一條是反方向的，也必須寫**；主場在 C2）
- 「In adult patients with sporadic VS treated with SRS, **cochlear dose constraint should be considered** because it
  provides better hearing preservation than no constraint.」
- 「single fraction SRS should be recommended rather than hypofractionated SRS (>1 and ≤5 fractions) because it results
  in decreased cranial nerve dysfunction」（**這一條屬 B3／C2 的分次比較，E4 不得引用來做單次對分次的比較**）

另可用的益處面錨點（**不要展開，一句帶過並指路**）：
台灣健保 37028B／37029B 的適應症條文本身把「曾接受開顱手術但有殘餘或復發」「開顱手術可能造成神經損傷或危險性大者」
「有嚴重心肺疾病不適合手術或全身麻醉者」列為放射手術的適用情境[E-S64]
——**這是「為什麼有人會走這條路」的官方版說明，比任何療效數字都適合放在風險那一段旁邊。**

### 反方向的資料（誠實必列）

- **A 段的風險是真的**：以色列頭癬世代的 ERR/Gy 4.63、CCSS 到 40 歲累積 5.6%、劑量反應線性——這些不能淡化[E-S44][E-S47][E-S46]。
- **B 段的風險非常小，但不是零**：Wolf 世代裡確實有 2 例惡性轉化與 1 例照射野內惡性腫瘤[E-S48]；
  Sherry 世代 2 例惡性轉化[E-S50]。**不可寫成「完全沒有風險」。**
- **兩段的可比性有限**：A 段是**童年、大範圍、幾十年前的技術**；B 段是**成人、小體積、單次高劑量、中位追蹤只有 8–11 年**。
  **這件事必須明寫**，否則兩段會互相抵銷成一句「所以不用擔心」或「所以都很可怕」。
- Wolf 自己寫追蹤時間仍不夠長，需要前瞻世代[E-S48]；Sherry 的 n 只有 273[E-S50]。

### Claim ceiling（E4）

- **可寫（A 段）**：
  「童年因頭癬接受低劑量頭部放療（腦部平均 1.5 Gy）的一萬多人，中位追蹤 40 年後，**良性腦膜瘤的超額相對風險是每格雷 4.63 倍**
  ——超額相對風險說的是相對於未照射者多出來的比例，不是你個人的機率」；
  「童年癌症存活者中接受過顱腦放療的 4,221 人，**到 40 歲時得到腦膜瘤的累積機率是 5.6%**，
  從原發癌到腦膜瘤的中位間隔 22 年，劑量 ≥30 Gy 者風險是 1.5–19.9 Gy 者的 2.6 倍」；
  「1,809 位病例的彙整：**中位潛伏期 22.7 年；劑量越低、潛伏期越長（<20 Gy 中位 36.3 年）**；
  照射時年齡中位 8.3 歲；**69% 是第 1 級，17.3% 是多顆**」；
  「放射線引起的腦膜瘤只佔所有腦膜瘤的 1–2%，但它比偶發型更常多發、更常復發、也更難治」；
  「該做什麼：**把治療摘要留著、把當年的放療部位與劑量問清楚、按 NICE 那一節列的晚期副作用項目定期追蹤**；
  國際共識的措辭是『固定間隔的影像追蹤可能是合理的』，**同一份文件也說目前證據不足以支持標準化的篩檢方案**」。
- **可寫（B 段）**：
  「四千九百多位接受過加馬刀、追蹤至少五年的病人（其中腦膜瘤 1,490 人、聽神經瘤 1,011 人、腦下垂體瘤 641 人），
  **十年累積發生放射手術相關惡性腫瘤的機率是 0.00045%**，發生率 6.8／10 萬人年，
  **與一般人口自己長出原發中樞神經惡性腫瘤的機率相當**」；
  「英國五千人、三萬人年的世代只出現 1 例新的星形細胞瘤，而依全國發生率預期是 2.47 例」；
  「指引寫的是：**接受放射手術的偶發型聽神經瘤病人應被告知，放射手術不會讓第二惡性腫瘤比一般人口多**」。
- **不可寫**：
  - **A 段結束後不給任何行動**（紅線 7 方向一的失敗定義）——必須有「該做什麼」的段落；
  - 把 B 段寫成「所以別照」或把 A 段的數字套到 B 段的病人身上（**這是紅線 7 方向二的失敗**）；
  - 把 B 段寫成「零風險」「完全安全」；
  - **把 B 段的絕對風險與治療的益處分開寫在不同段落**（SPEC 明文要求同段）；
  - 用 ERR/Gy 或 EAR 當成個人機率；
  - 把「1–2% 的腦膜瘤是放射線引起的」寫成「照過的人有 1–2% 會長」（分母完全不同）；
  - 建議任何人去做基因檢測或全面影像篩檢（ICOM 明說證據不足）；
  - 用 Cahan 準則讓讀者自我判定「我這顆是不是放射線引起的」——那是病理與病史的事。

### Caveats／safety notes

- Cahan 準則的第 2 條「足夠的潛伏期」**沒有公認的下限**，各研究自訂[E-S43]——引用時要說。
- 以色列世代的暴露是 1950 年代的技術與適應症（頭癬），**今天不會再有人因此照射**。
- CCSS 的 4,221 人是**接受過顱腦放療的童年癌症存活者**，不是一般民眾，也不是成人放射手術病人。
- Wolf 世代排除了先前接受過放射治療者，**所以它不能回答「已經照過一次的人再照一次會怎樣」**——那一題指向 `sit-reirradiation`。
- 本篇涉及兩個高焦慮族群；情緒面一句指向 `care-fear`。

### 台灣端（E4）

| 項目 | 結果 | 路徑 |
|---|---|---|
| 放射手術的支付條文（作為「為什麼有人走這條路」的官方說明） | 見 E3 台灣端 37028B／37029B 逐字 | [E-S64] |
| 「第二腫瘤」在台灣有沒有官方追蹤建議 | **gap**：本次未檢出任何台灣官方針對童年放療存活者或放射手術後第二腫瘤的追蹤文件 | hpa.gov.tw 本次連線失敗（見 FAIL 清單）；寫法：「我查不到台灣的官方追蹤建議，請把治療摘要帶去問主治醫師」 |
| 童年癌症存活者的長期追蹤資源 | **未查**（不在 SPEC §八 E 組清單內） | — |

### 給繪圖組（E4）

SPEC §七 沒有分配圖給 E4。若要一張「兩個方向同框」的圖（**這正是紅線 7 的形狀**），
可用的 PASS 數字只有：
左半（童年高劑量顱腦放療）：到 40 歲累積 5.6%（n=4,221）[E-S47]；中位潛伏 22 年[E-S47]／22.7 年（n=1,303）[E-S43]。
右半（成人立體定位放射手術）：10 年累積 0.00045%、6.8／10 萬人年（n=4,905，中位追蹤 8.1 年）[E-S48]；
Sheffield 1 例對預期 2.47 例（約 5,000 人、30,000 人年）[E-S49]。
**兩半必須標明族群、年代、劑量與追蹤時間；不可把兩個數字直接並列成同一把尺。**

---

## E5 `bt-nf2`〈多發性、NF2 與遺傳〉——合併專題真正的紅利

### Key facts

**一、名稱與診斷準則（2022 起的正式名稱）**

- **改名**：2022 年的國際共識（Children's Tumor Foundation 統籌，Delphi 流程）把
  **neurofibromatosis type 2 改為 NF2-related schwannomatosis（NF2-SWN）**。
  原文逐字：「In the revised nomenclature, **the term "neurofibromatosis 2" has been retired to improve diagnostic
  specificity.**」；改名的理由是「to emphasize their phenotypic overlap and **to minimize misdiagnosis with
  neurofibromatosis type 1**」，而且新準則「**incorporate mosaic forms of these conditions**」[E-S53]。
- **診斷準則全文（由一份 OA 綜述逐字重印，可引）**[E-S54]：
  > A diagnosis of NF2-related schwannomatosis can be made when an individual has one of the following:
  > **1. Bilateral vestibular schwannomas (VS)**
  > **2.** An identical *NF2* pathogenic variant in **at least 2 anatomically distinct NF2-related tumors**
  > (schwannoma, meningioma, and/or ependymoma). (Note: if the variant allele fraction (VAF) in unaffected tissues
  > such as blood is clearly **<50%**, the diagnosis is **mosaic** NF2-related schwannomatosis)
  > **3.** Either **2 major** or **1 major and 2 minor** criteria:
  > **Major criteria**: Unilateral VS；First-degree relative other than sibling with NF2-related schwannomatosis；
  > **2 or more meningiomas**（單一顆腦膜瘤只算 minor）；*NF2* pathogenic variant in an unaffected tissue such as blood
  > （VAF 明顯 <50% 則為 mosaic）。
  > **Minor criteria**（同一類可計 >1 次）：ependymoma、meningioma（多顆腦膜瘤則升為 major）、schwannoma
  > （若 major 是單側 VS，則至少一顆 schwannoma 須為皮內）；**只能計一次者**：juvenile subcapsular or cortical cataract、
  > retinal hamartoma、**epiretinal membrane in a person aged <40 years**、meningioma。
- **兩個容易寫錯的地方**：
  ① **雙側前庭神經鞘瘤沒有年齡上限**——2019 年曾提議加 70 歲的切點，**共識決定不加**，
     理由逐字是「the consensus was to retain all those with bilateral VS as possible NF2-SWN
     **to dissuade clinicians from not investigating older patients**」[E-S54]。
  ② **膠質瘤已從準則中移除**（因為 NF2-SWN 的髓內腫瘤以脊髓室管膜瘤為主、且沒有高惡性度膠質瘤）[E-S54]。
- **LZTR1 的鑑別（寫作者常漏）**：單側 VS 加上兩顆以上非前庭神經鞘瘤的人，
  「**LZTR1 variants must ideally be ruled out before confirming a diagnosis of NF2-SWN**」[E-S54]。

**二、流行病學、發病年齡與自然病程（帶分母）**

- **盛行率與發生率**[E-S54]：
  - 曼徹斯特地區（人口 480 萬）**診斷盛行率 1／50,500**，推算**出生盛行率 1／27,956**；
  - 2024 年全英格蘭（人口 5,500 萬）**盛行率至少 1／58,000**（三個最高完整度地區為 1／55,000）；
  - 曼徹斯特 2010–24 年 15 年間新診斷 97 例（人口 500 萬），**年發生率 1／773,000**；
  - 1992 年的舊估計：出生盛行率 1／33,000–40,000，但當時**診斷點盛行率只有 1／200,000**（因為多數人 30 歲後才出現症狀、且早逝）。
- **遺傳來源的三分法（最新英國流行病學研究）**[E-S54]：
  現存 NF2-SWN 病人中**約 25% 由受影響的父母遺傳而來、30% 為新生的異型合子（de novo heterozygotes）、45% 為鑲嵌型**；
  另一處寫「de novo 率現估為 **73%**」。
- **臨床表現的比例**[E-S54]：
  - **皮膚神經鞘瘤約 70% 的 NF2-SWN 病人有，但只有 10% 的人有 10 顆以上**；
  - **仔細的專科眼科評估下，60–80% 的病人有白內障**（多為幼年型後囊下混濁，少需手術）；
  - NF2-SWN「usually presents with bilateral vestibular schwannoma, **but can present with meningioma or spinal tumour
    or ophthalmic features before a VS diagnosis**, or with a unilateral VS and other tumours and rarely with a
    unilateral VS alone」。
- **腦膜瘤在 NF2-SWN 的比例與行為**：
  - **「Meningiomas affect up to 80% of patients with *NF2*-related schwannomatosis during their lifetime.」**
    （15 篇研究、937 位病人、3,637 顆腦膜瘤的系統性回顧與統合分析）[E-S61]
  - 同一份統合分析：女性佔 59.6%（95% CI 55.4–63.7）；
    **監測中的 2,082 顆腫瘤（平均追蹤 5.55–9.18 年）加權平均生長速率 0.508 cm³/年（95% CI 0.0244–0.992）**（748 顆有資料）；
    **監測期間出現新生腦膜瘤的病人比例 24.6%（95% CI 2.73–58.7，3 篇研究）**；
    手術切除 203 顆，**彙整復發風險 12.5%（95% CI 7.98–17.9）**；
    **立體定位放射手術 665 顆，彙整治療後腫瘤惡化風險 6.29%（95% CI 4.57–8.25）**，
    中位追蹤 3.58–9.25 年，**3 年與 5 年局部控制 97.1%（94.7–98.8）與 91.2%（88.4–93.6）**。
  - **ICOM 2024 的補充（另一組分母）**[E-S40]：「approximately **10%** of these meningiomas will grow rapidly
    (defined as **≥2 cm³/year** by one study) while the remainder will demonstrate no or very slow growth.
    **New meningiomas will develop in 20% of NF2-SWN patients.**」
    以及「patients with NF2-SWN who have a meningioma have been found to have a **significantly increased risk of death**
    compared to those who do not」；「management of patients with NF2-SWN by **multidisciplinary teams at high-volume
    centers** has been demonstrated to improve [outcomes]」。
- **存活**[E-S54]：1990 年以前，臨床診斷後平均存活僅 15 年、平均精算存活年齡約 60 歲；
  近 30 年改善，但 2012 年的資料顯示**仍顯著低於一般人口**；英格蘭自 2009 年起指定四家治療中心集中照護後再有改善。

**三、同一個基因怎麼同時解釋多發腦膜瘤與雙側聽神經瘤（本篇的核心段落）**

可引的三層：
1. **同一個抑癌基因，兩種細胞都會用到它**：NF2-SWN 是體染色體顯性的腫瘤易感症候群，
   「predisposing affected individuals to the development of **schwannomas, meningiomas and ependymomas**
   as well as specific ophthalmologic manifestations」[E-S54]。
2. **偶發型腦膜瘤最常見的驅動事件也是 *NF2***——ICOM 的表述是 *NF2* 突變在腦膜瘤中佔優勢
   （Alliance A071401 的設計理由逐字：「Given the **predominance of *NF2* mutations in meningiomas**」）[E-S34]。
   →**所以「一個基因同時解釋兩件事」不是巧合：它本來就是這兩種腫瘤共同的主要抑癌基因。**
3. **第三層證據（放射線引起的腦膜瘤）**：RIM 的 *NF2* 點突變比偶發型少，**但 *NF2* 基因融合事件較多**，
   推測是放射造成的雙股斷裂誤修復——**同一個基因，被不同的機制打壞**[E-S40]。
   這一層把 E4 與 E5 接起來，是本專題合併寫作的具體紅利。
4. **可引的臨床表述**：「Compared to patients with sporadic meningiomas, patients with NF2-SWN typically
   **develop meningiomas at a younger age and are at higher risk for developing multiple meningiomas.**
   Therefore patients with these phenotypes **should be screened for germline *NF2* and *SMARCE1* mutations.**」[E-S40]

**四、bevacizumab 在 NF2 相關前庭神經鞘瘤的聽力反應（帶分母與反應定義）**

- **反應的定義先寫清楚**：三個前瞻試驗的主要終點都是**以字詞辨識分數（word recognition score, WRS）定義的聽力反應**，
  不是「病人覺得有沒有比較好聽」[E-S57][E-S58][E-S59]。
- **Blakeley 2016（JCO）**[E-S57]：14 位 NF2、目標耳有進展性聽力喪失（中位基線 WRS 60%，範圍 13–82%），
  bevacizumab 7.5 mg/kg 每 3 週、共 46 週，之後 24 週監測。
  **主要終點「確認的聽力反應」（改善維持 ≥3 個月）＝5/14（36%，95% CI 13–65%，P<.001）**；
  另有 8/14（57%）出現超過 WRS 95% 信賴區間的**短暫**改善；**沒有病人聽力變差**；
  目標腫瘤影像反應 6/14（43%）。第 3 級不良事件 3 件（高血壓 2、免疫性血小板減少性紫斑 1）。
  **⚠ 本篇有 2026 年的 Erratum（JCO 2026;44(8):723，PMID 41666344）；本次未能取得勘誤內容
  （摘要為空、原文取不到）——寫作者引用上述數字前，請先確認勘誤內容（見 FAIL-6）。**
- **Plotkin 2019（JCO，高劑量）**[E-S58]：22 位 NF2（中位 23 歲，中位基線 WRS 53%），
  bevacizumab 10 mg/kg 每 2 週共 6 個月，之後 5 mg/kg 每 3 週共 18 個月。
  **6 個月時聽力反應 9/22（41%）——成人 8/15、兒童 1/7（P=.08）**；
  **影像反應 7/22（32%）——成人 7/15、兒童 0/7（P=.05）**。
  作者結論逐字：「**High-dose bevacizumab seems to be no more effective than standard-dose bevacizumab**」。
  同文開頭也寫下標準劑量的既有成績：「Bevacizumab treatment at 7.5 mg/kg every 3 weeks results in improved hearing in
  **approximately 35%-40%** of patients with NF2 and progressive VSs」。
  常見不良事件：高血壓、疲倦、頭痛、月經不規則；30% 報告 NF2 相關生活品質改善、60% 耳鳴困擾減輕。
- **Plotkin 2023（Neuro-Oncology，維持治療，OA）**[E-S59]：20 位 NF2-SWN（中位 23.5 歲，範圍 12.5–62.5；
  目標耳中位 WRS 70%，範圍 2–94%），誘導後以 5 mg/kg 每 3 週維持 18 個月。
  **目標耳免於聽力惡化：48 週 95%、72 週 89%、98 週 70%**；
  **目標腫瘤免於生長（生長定義為體積較基線增加 >20%）：48 週 94%、72 週 89%、98 週 89%**；
  NF2 相關生活品質維持穩定、耳鳴困擾下降；**3/20（15%）因不良事件停藥**。
- **系統性回顧（9 篇、176 位病人）**[E-S60]：**腫瘤體積部分縮小（≥20%）40%、穩定 50%、惡化 10%**；
  **聽力改善 36%、穩定 46%、惡化 18%**；**嚴重不良反應（含高血壓與血栓栓塞）13%**，18% 無任何副作用。
  作者特別點出：**停藥後有病人腫瘤再長，需要長期監測。**
- **指引位置**：EANO 2020 聽神經瘤指引摘要逐字——
  「**Except for bevacizumab in neurofibromatosis type 2, there is no role for pharmacotherapy.**」[E-S42]

**五、多發性腦膜瘤（非 NF2 的情況）**

- **鑑別診斷清單（逐字可引）**[E-S54]：
  「multiple intracranial meningiomas can be seen in the chromosome 22 condition **SMARCB1-SWN**.
  In the absence of schwannomas, there are additional genetic associations with multiple meningiomas such as
  **BAP1 tumour predisposition syndrome** and **SUFU familial meningioma predisposition** as well as
  **familial clear cell meningioma caused by SMARCE1**, and these can be assessed via commercially available
  **multiple meningioma next generation sequencing panels**. Finally, **past medical history should be interrogated for
  prior radiation exposure** and a common secondary neoplasm after remote radiation exposure is meningioma.」
- **ICOM 的篩檢句**（同上第三節第 4 點）：年輕發病或多發者「should be screened for germline *NF2* and *SMARCE1* mutations」[E-S40]。
- **放射線引起的多發性**：RIM 的多發比例 17.3%（181/1,047），高劑量組更多[E-S43]；
  以色列世代中 RIM 比非 RIM 更常多發[E-S45]。**→ 這是 E4 與 E5 的第二個接點。**

**六、鑲嵌型（mosaic）NF2 對家屬風險的意義**

- **有多常見**：1,055 位沒有上一代受影響家族史的 de novo 個案中，
  **確診或推定的鑲嵌型 232/1,055（22.0%）**；但由於非鑲嵌型的變異偵測率只有 387/1,055（36.7%），
  作者推算**整體可能的鑲嵌率為 59.7%**。
  **這個比例隨發病年齡變化極大**：**20 歲前以雙側 VS 表現者 21.7%，60 歲以上者 80.7%**[E-S55]。
  作者結論逐字：「**Risks to offspring are small and probably correlate with variant allele frequency detected in blood.**」
- **檢測怎麼做**（給遺傳諮詢段落用的可引描述）[E-S54]：
  「need to test blood and ideally **≥2 potentially associated tumours** (i.e. schwannoma, meningioma, ependymoma)
  from distinct regions of the nervous system. If a shared *NF2* variant is seen across the unique tumour samples and
  not found (or at low level) in blood, this confirms mosaic NF2-SWN.」
- **對病人本人與對家屬的意義不同（這一句是本段的重點，逐字可引）**[E-S54]：
  「People with mosaic NF2-SWN **may still have severe clinical course and require appropriate clinical surveillance and
  intervention**, but there is an implication of **lower risk of transmission to children** versus germline involvement.」
- **NF2-SWN 病人的影像追蹤怎麼調整（與 E2 交叉）**[E-S16]：
  CNS 指引 level III：「vestibular schwannomas associated with NF2 should be imaged (similar to sporadic schwannomas)
  with the following caveats: 1. **More frequent imaging may be adopted in NF2 patients because of a more variable
  growth rate** for vestibular schwannomas, and annual imaging may ensue once the growth rate is established.
  2. In NF2 patients with **bilateral** vestibular schwannomas, **growth rate of a vestibular schwannoma may increase
  after resection of the contralateral tumor**, and therefore, more frequent imaging may be indicated…
  3. Careful consideration should be given to whether contrast is necessary in follow-up studies…」
  （2026 更新版把這一條列為「未更動、沿用」的建議）[E-S17]

### 反方向的資料（誠實必列）

- **多發腦膜瘤不等於 NF2**：非 NF2 的基因（SMARCB1、BAP1、SUFU、SMARCE1）與**放射線暴露史**都要先排[E-S54][E-S43]。
- **bevacizumab 不是治癒**：系統性回顧中 18% 的人聽力仍惡化、10% 腫瘤仍惡化，13% 有嚴重不良反應，
  而且**停藥後有人腫瘤再長**[E-S60]；維持治療到 98 週時免於聽力惡化的比例已降到 70%[E-S59]。
- **高劑量沒有比較好**[E-S58]，**兒童的影像反應在該試驗中是 0/7**[E-S58]。
- 鑲嵌型的家屬風險「較低」不等於「零」，而且**鑲嵌型的病人本人可以病得很重**[E-S54][E-S55]。

### Claim ceiling（E5）

- **可寫**：「2022 年起正式名稱是 **NF2 相關神經鞘瘤病（NF2-related schwannomatosis）**，
  共識文件寫的是『neurofibromatosis 2 這個詞已經退場』」；
  「**雙側前庭神經鞘瘤本身就足以診斷**，而**兩顆以上的腦膜瘤是主要條件之一**（單一顆只算次要條件）」；
  「**一輩子當中最多八成的 NF2-SWN 病人會長腦膜瘤**（937 人、3,637 顆的統合分析）；
  監測中約四分之一的人會長出新的腦膜瘤」；
  「**同一個 *NF2* 基因同時是神經鞘瘤與腦膜瘤最常見的抑癌基因**，所以一個人同時有這兩種瘤不是巧合」；
  「bevacizumab 在 **NF2 相關**的前庭神經鞘瘤，用字詞辨識分數定義的**聽力反應約三成五到四成**
  （14 人 36%、22 人 41%；176 人的系統性回顧 36%），**高劑量沒有比較好**，**停藥後有人會再長**」；
  「英格蘭 2024 年的盛行率約 1／58,000；現存病人裡**約四分之一遺傳自父母、約三成是新生突變、約四成五是鑲嵌型**」；
  「**鑲嵌型的意思是變異只出現在身體一部分細胞**：對病人本人病情不一定比較輕，但**傳給子女的風險比生殖系變異低**，
  而且風險大致與血液中的變異等位基因頻率相關——**實際數字要由遺傳諮詢師依你的檢驗結果說明**」；
  「多發腦膜瘤不等於 NF2：還要想到 SMARCB1、BAP1、SUFU、SMARCE1，以及**過去的放射線暴露史**」。
- **不可寫**：
  - 把「最多八成會長腦膜瘤」寫成「八成的人會需要治療」（統合分析裡 SRS 與手術是少數，多數在監測）[E-S61]；
  - 把 bevacizumab 的聽力反應寫成「聽力會恢復」——**反應的定義是 WRS 的改善並維持三個月，不是回到正常**；
  - 把 NF2 的 bevacizumab 資料外推到**偶發型**聽神經瘤或腦膜瘤病人[E-S42]；
  - 給任何具體的家屬再發風險百分比（**除了可引的「≈50% 生殖系顯性遺傳」這個教科書層級的陳述外，
    鑲嵌型的個別風險不可自行推算**）；
  - 建議讀者自行安排基因檢測——可寫的是「這件事要透過遺傳諮詢做」；
  - 把 NF2-SWN 的追蹤時程寫成與偶發型相同（CNS 明文說可能要更密）[E-S16]；
  - 把「存活較差」寫成預後宣告（[E-S54] 的資料跨越 30 年、且明確記錄集中照護後有改善）。

### Caveats／safety notes

- 遺傳檢測與家屬檢測涉及未成年人、保險與工作，**文章只寫「這一題要找誰談」**：遺傳諮詢門診／遺傳諮詢中心。
- [E-S61] 的部分信賴區間極寬（新生腦膜瘤 24.6%，95% CI 2.73–58.7），**寫的時候要把區間帶上**。
- [E-S57] 有 2026 年勘誤未取得（FAIL-6），引用 36% 這個數字時建議同時寫出 [E-S58] 的 41% 與 [E-S60] 的 36%，
  讓三個獨立來源互相支撐。
- 聽力輔具、人工電子耳、身心障礙鑑定的細節歸 C 組；E5 只寫 NF2 相關的部分並指路。

### 台灣端（E5）

| 項目 | 結果 | 路徑 |
|---|---|---|
| **NF2 基因檢測有沒有健保支付項目** | **查不到（零筆）**：支付標準全表（6,163 筆）以「**神經纖維瘤**」查詢 **0 筆**、「**次世代定序**」在品名欄 0 筆（相關項目名稱為「實體腫瘤次世代基因定序」，見下列）。**全表中沒有任何以 NF2／神經纖維瘤命名的檢測項目** | 支付標準全表 TXT 全文檢索，2026-09-13 [E-S64]。**只證明「查不到列項」，不得推論有無給付** |
| 腫瘤次世代基因定序項目 | **查到項目，但適應症附表未取得**：**30301B** 實體腫瘤 NGS－BRCA1/2 基因檢測 10,000 點、**30302B** 小套組（≦100 個基因）20,000 點、**30303B** 大套組（>100 個基因）30,000 點（三者生效日 20260901）；**30304B／30305B** 為血液腫瘤。30302B 規範逐字：「**1.適應症：如附表2.2.1。**2.支付規範：(1)醫院資格…A.限區域級以上醫院或主管機關公告通過「癌症診療品質認證醫院」者。B.須院內設立或跨院聯合組成分子腫瘤委員會(Molecular Tumor Board, MTB)…(3)**除 Germline BRCA1/2 基因檢測使用血液檢體外，其他檢測限使用已確診之腫瘤病理組織**…(4)**每人各癌別限 30301B、30302B 或 30303B 擇一申報且終生給付一次**…」 | 同上 [E-S64]。**附表 2.2.1 的癌別清單本次未取得（見 FAIL-5）→ 不能說腦膜瘤或聽神經瘤在不在名單內** |
| **遺傳諮詢相關條文** | **查到一筆**：**25021B「染色體檢查(特殊)」4,067 點**，規範逐字：「**1.限衛生福利部認證之遺傳諮詢中心申請實施。2.人員資格依遺傳諮詢中心相關規定辦理。3.本項目如已申請衛生福利部補助者，本保險不另支付該次檢查費用。4.如做為一般性篩檢者，非屬本保險給付範圍。5.每一個案限給付一次。**」另有 25007B「細胞遺傳學檢查」11,871 點 | 同上 [E-S64]。→**可寫的一句：「健保條文裡確實有『遺傳諮詢中心』這個角色，而且明文寫著一般性篩檢不給付、已申請衛福部補助者不重複支付」** |
| **罕見疾病相關規定** | **查到法源，查不到名單**：《罕見疾病防治及藥物法》（**修正日期 民國 104 年 01 月 14 日**）第 3 條：「本法所稱罕見疾病，指**疾病盛行率在中央主管機關公告基準以下**或因情況特殊，經第四條所定審議會審議認定，**並經中央主管機關指定公告者**」；第 7 條：醫事人員發現罹患罕見疾病之病人應向中央主管機關報告；第 8 條：中央主管機關「發現具有罕見遺傳疾病缺陷者，經病人或其法定代理人同意，應派遣專業人員訪視，告知相關疾病之影響，並**提供病人及家屬心理支持、生育關懷、照護諮詢等服務**」；第 13 條：得申請補助至國外進行國際醫療合作，「**前項醫療合作為代行檢驗項目者，得由第十條規定之醫療或研究機構申請補助**」 | law.moj.gov.tw `LawAll.aspx?pcode=L0030003`，2026-09-13 [E-S65] |
| **NF2-SWN 在不在台灣公告的罕見疾病名單內** | **gap**：**國民健康署網站（hpa.gov.tw）本次連線失敗**，未能取得公告名單；data.gov.tw 的 API 回 405。**不推論**。寫法：「NF2 在不在台灣公告的罕見疾病名單裡，我這次查不到可以引用的官方名單，請向遺傳諮詢中心或罕見疾病基金會確認」 | 見 FAIL-4 |
| **身心障礙鑑定（NF2 相關部分）** | **查到法源與現行版本**：《**身心障礙者鑑定作業辦法**》**修正日期 民國 115 年 06 月 29 日**，附有「附表一甲 身體系統構造或功能之鑑定人員資格條件及鑑定方法與鑑定工具」等多份附表 PDF。**附表內容本次未展開**（聽力、平衡、顏面神經的鑑定基準歸 C 組） | law.moj.gov.tw `LawAll.aspx?pcode=L0020020`，2026-09-13 [E-S66] |
| 助聽器／人工電子耳補助 | **未查**（歸 C 組）。全表中可見 **54045B 人工電子耳術後調圖（單耳）1,311 點** | [E-S64] |
| bevacizumab 給付是否涵蓋 NF2 | **零筆（逐字）**——見 E3 台灣端 [E-S62] | — |

### 給繪圖組（E5）——**SPEC §七 圖 12 `fig-bt-nf2` 的唯一資料來源**

圖的任務（SPEC 原文）：「**NF2 怎麼同時解釋多發腦膜瘤與雙側聽神經瘤**」。

可用的 **PASS 數字與可引敘述**（不要放任何不在此清單裡的數字）：
1. **中心節點**：*NF2* 抑癌基因（第 22 號染色體）。可標的事實：
   - 它是**偶發型腦膜瘤最常見的驅動突變**（A071401 的設計理由逐字「the predominance of *NF2* mutations in meningiomas」）[E-S34]；
   - 雙側前庭神經鞘瘤是 NF2-SWN 的**單一充分診斷條件**[E-S54]。
2. **左分支：腦膜瘤**——一生中最多 **80%** 的 NF2-SWN 病人會長[E-S61]；
   監測中出現**新生**腦膜瘤者 **24.6%（95% CI 2.73–58.7）**[E-S61]；
   約 **10%** 長得快（≥2 cm³/年）[E-S40]；
   監測腫瘤加權平均生長 **0.508 cm³/年**[E-S61]；
   手術後復發 **12.5%（7.98–17.9）**、SRS 後惡化 **6.29%（4.57–8.25）**，SRS 後 3／5 年局部控制 **97.1%／91.2%**[E-S61]。
3. **右分支：前庭神經鞘瘤**——雙側；bevacizumab 的**聽力反應 36%（5/14）／41%（9/22）／36%（176 人回顧）**[E-S57][E-S58][E-S60]；
   維持治療 98 週免於聽力惡化 **70%**[E-S59]。
4. **第三分支（把 E4 接進來）**：放射線引起的腦膜瘤中，*NF2* **點突變較少但基因融合較多**[E-S40]
   ——同一個基因、不同的打壞方式。
5. **底部的鑑別框**：多發腦膜瘤 ≠ NF2 → SMARCB1-SWN、BAP1、SUFU、SMARCE1（家族性透明細胞腦膜瘤）、**過去的放射線暴露**[E-S54]。
6. **鑲嵌型的角落**：de novo 個案中確診／推定鑲嵌 **22.0%（232/1,055）**，推算整體可能達 **59.7%**；
   **20 歲前雙側 VS 發病者 21.7%，60 歲以上者 80.7%**[E-S55]；
   現存病人組成：**遺傳 25%／de novo 異型合子 30%／鑲嵌 45%**[E-S54]。

**圖上不可出現**：任何家屬再發風險的百分比、任何療效比較箭頭、任何「所以要做基因檢測」的指令。

---

## 來源清單

**共同查證路徑**
- 期刊書目：`GET https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:<PMID>&resultType=core&format=json`
  （或 `TITLE:"..."`），逐筆核對 title／journal／year／volume(issue)／pages／DOI／PMID／isOpenAccess 與 abstractText。
- OA 全文：`GET https://www.ebi.ac.uk/europepmc/webservices/rest/<PMCID>/fullTextXML`。
- 全國法規資料庫：`GET https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=<代碼>&flno=<條號>` 與 `LawAll.aspx?pcode=<代碼>`。
- 健保藥品給付規定：`POST https://info.nhi.gov.tw/api/INAE3000/INAE3000S01/SQL0001`
  （header `Content-Type: application/json`＋`Referer: https://info.nhi.gov.tw/INAE3000/INAE3000S02`，body `{"CURPAGE":n,"PAGESIZE":500,"DRUG_ING":"<成分英文名>"}`）
  → `GET .../getPDF?DurgFileName=<檔名>&appType=true` → `pdftotext -layout`。
  **人類可讀頁面：`https://info.nhi.gov.tw/INAE3000/INAE3000S02`**。
- 健保支付標準全表：`GET https://info.nhi.gov.tw/api/iode0000s01/Dataset?rId=A21030000I-D20020-002`（22 MB TXT，UTF-8 BOM，`^` 分欄，6,163 筆）。
  **人類可讀頁面：`https://www.nhi.gov.tw/ch/cp-18621-7e20c-4002-1.html`（醫療服務給付項目及支付標準）**。
- 全部查證日期：**2026-09-13**。

### PASS

- **[E-S1] PASS** — Walbert T, Harrison RA, Schiff D, Avila EK, Chen M, Kandula P, Lee JW, Le Rhun E, Stevens GHJ,
  Vogelbaum MA, Wick W, Weller M, Wen PY, Gerstner ER. (2021). **SNO and EANO practice guideline update:
  Anticonvulsant prophylaxis in patients with newly diagnosed brain tumors.** *Neuro-Oncology*, 23(11), 1835–1844.
  DOI: 10.1093/neuonc/noab152｜PMID: 34174071｜PMCID: PMC8563323｜OA: N。
  Route: Europe PMC REST（`TITLE:"Anticonvulsant prophylaxis in patients with newly diagnosed brain tumors"`）。
  **五條建議逐字出自 abstractText 的 Recommendations 欄；全文未取得，只可引用摘要中的建議原文。**
- **[E-S2] PASS** — American Academy of Neurology. **Guideline Detail** 頁面兩筆：
  ① `https://www.aan.com/Guidelines/home/GuidelineDetail/30`「Anticonvulsant Prophylaxis in Patients with Newly
  Diagnosed Brain Tumors」，頁面逐字「**This guideline is retired.**」「Guideline, May 2000」
  「**Retired by the AAN Institute Board of Directors on June 4, 2012.**」
  ② `https://www.aan.com/Guidelines/Home/GuidelineDetail/1042`「SNO and EANO practice guideline update: Anticonvulsant
  prophylaxis in patients with newly diagnosed brain tumors」，頁面逐字「Guideline developed by the Society of
  Neuro-Oncology and the European Association of Neuro-Oncology.」「Guideline, August 2021」
  「**Affirmed by the AAN Institute Board of Directors on November 18, 2020.**」
  Route: `curl` 直取（HTTP 200），2026-09-13。
- **[E-S3] NOT-CITABLE（保留紀錄）** — Glantz MJ, Cole BF, Forsyth PA, Recht LD, Wen PY, Chamberlain MC, Grossman SA,
  Cairncross JG. (2000). **Practice parameter: anticonvulsant prophylaxis in patients with newly diagnosed brain tumors
  [RETIRED].** *Neurology*, 54(10), 1886–1893. DOI: 10.1212/wnl.54.10.1886｜PMID: 10822423。
  Europe PMC 的標題欄本身即帶 `[RETIRED]`。**不可引用其建議內容**；只可用來說明「這份 2000 年的文件已經退休」。
- **[E-S4] PASS** — Englot DJ, Magill ST, Han SJ, Chang EF, Berger MS, McDermott MW. (2016). **Seizures in supratentorial
  meningioma: a systematic review and meta-analysis.** *Journal of Neurosurgery*, 124(6), 1552–1561.
  DOI: 10.3171/2015.4.jns142742｜PMID: 26636386｜PMCID: PMC4889504｜OA: N。數字全部出自摘要。
- **[E-S5] PASS** — Cai Q, Wu Y, Wang S, Huang T, Tian Q, Wang J, Qin H, Feng D. (2022). **Preoperative antiepileptic drug
  prophylaxis for early postoperative seizures in supratentorial meningioma: a single-center experience.**
  *Journal of Neuro-Oncology*, 158(1), 59–67. DOI: 10.1007/s11060-022-04009-4｜PMID: 35434765｜OA: N。
- **[E-S6] PASS** — Laajava J, Niemelä M, Korja M. (2026). **Association between persisting peritumoral brain edema and
  seizures as well as worse functional outcome after meningioma surgery: a retrospective study of 218 patients.**
  *Journal of Neurosurgery*, 145(3), 613–622. DOI: 10.3171/2026.1.jns252864｜PMID: 42320065｜OA: N。
- **[E-S7] PASS** — Laajava J, Niemelä M, Korja M. (2025). **Peritumoral edema resolves infrequently in surgically treated
  patients with intracranial meningioma — a retrospective study of 279 meningioma patients.**
  *Journal of Neuro-Oncology*, 173(1), 83–94. DOI: 10.1007/s11060-025-04964-8｜PMID: 40048039｜PMCID: PMC12040978｜**OA: Y**。
- **[E-S8] PASS** — Schmid S, Aboul-Enein F, Pfisterer W, Birkner T, Stadek C, Knosp E. (2010). **Vascular endothelial
  growth factor: the major factor for tumor neovascularization and edema formation in meningioma patients.**
  *Neurosurgery*, 67(6), 1703–1708; discussion 1708. DOI: 10.1227/neu.0b013e3181fb801b｜PMID: 21107201｜OA: N。
- **[E-S9] PASS** — Vecht CJ, Hovestadt A, Verbiest HB, van Vliet JJ, van Putten WL. (1994). **Dose-effect relationship of
  dexamethasone on Karnofsky performance in metastatic brain tumors: a randomized study of doses of 4, 8, and 16 mg
  per day.** *Neurology*, 44(4), 675–680. DOI: 10.1212/wnl.44.4.675｜PMID: 8164824｜OA: N。**族群：腦轉移，非腦膜瘤。**
  註：摘要在 250 字處被截斷（"ABSTRACT TRUNCATED AT 250 WORDS"），可引用的只有截斷前出現的數字。
- **[E-S10] PASS** — Dropcho EJ, Soong SJ. (1991). **Steroid-induced weakness in patients with primary brain tumors.**
  *Neurology*, 41(8), 1235–1239. DOI: 10.1212/wnl.41.8.1235｜PMID: 1866012｜OA: N。**族群：混合原發腦瘤。**
- **[E-S11] PASS** — Broersen LH, Pereira AM, Jørgensen JO, Dekkers OM. (2015). **Adrenal Insufficiency in Corticosteroids
  Use: Systematic Review and Meta-Analysis.** *The Journal of Clinical Endocrinology and Metabolism*, 100(6), 2171–2180.
  DOI: 10.1210/jc.2015-1218｜PMID: 25844620｜OA: N。**族群：全體類固醇使用者（74 篇、3,753 人），非腦瘤族群。**
- **[E-S12] PASS** — Da Silva AN, Schiff D. (2007). **Adrenal insufficiency secondary to glucocorticoid withdrawal in
  patients with brain tumor.** *Surgical Neurology*, 67(5), 508–510. DOI: 10.1016/j.surneu.2006.07.018｜PMID: 17445619｜OA: N。
  **n=5 的病例系列＋單中心比例（1%）。**
- **[E-S13] PASS（僅書目與摘要）** — Avila EK, Tobochnik S, Inati SK, Koekkoek JAF, McKhann GM, Riviello JJ, Rudà R,
  Schiff D, Tatum WO, Templer JW, Weller M, Wen PY. (2024). **Brain tumor-related epilepsy management: A Society for
  Neuro-oncology (SNO) consensus review on current management.** *Neuro-Oncology*, 26(1), 7–24.
  DOI: 10.1093/neuonc/noad154｜PMID: 37699031｜PMCID: PMC10768995｜OA: N。
  **全文兩條路徑（Europe PMC fullTextXML、NCBI efetch）皆未取得正文，只可引書目，不可引內文措辭。**
- **[E-S14] PASS** — 全國法規資料庫。**道路交通安全規則**（**修正日期：民國 115 年 06 月 26 日**；
  法規整編資料截止日：民國 115 年 09 月 04 日）。所引條文：**第 52 條之 3、第 64 條、第 64 條之 1、第 65 條、第 76 條**。
  Route: `https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=K0040013&flno=64`（及 `flno=52-3／64-1／65／76`）與
  `https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=K0040013`，2026-09-13 逐條抓取；
  與站上 `gb-seizure.html` 已引之條文逐字比對，**完全一致**。
- **[E-S15] PASS** — National Institute for Health and Care Excellence (NICE). **Brain tumours (primary) and brain
  metastases in over 16s. NICE guideline [NG99].** Published: 11 July 2018; **Last updated: 29 January 2021.**
  所引章節：1.4（meningioma 的調查與治療，含 table 4、table 5）、**1.5 Follow-up for meningioma（含 table 6、table 7）**、
  **1.11 Surveillance for the late-onset side effects of treatment**。
  Route: `https://www.nice.org.uk/guidance/ng99/chapter/Recommendations`（HTTP 200），2026-09-13 全文擷取。
  **注意：NG99 涵蓋 glioma、meningioma、brain metastases，不涵蓋前庭神經鞘瘤與腦下垂體腺瘤。**
- **[E-S16] PASS** — Dunn IF, Bi WL, Mukundan S, Delman BN, Parish J, Atkins T, Asher AL, Olson JJ. (2018).
  **Congress of Neurological Surgeons Systematic Review and Evidence-Based Guidelines on the Role of Imaging in the
  Diagnosis and Management of Patients With Vestibular Schwannomas.** *Neurosurgery*, 82(2), E32–E34.
  DOI: 10.1093/neuros/nyx510｜PMID: 29309686｜OA: N。**七個問題的建議全文出現在 abstractText 中，可逐字引用。**
- **[E-S17] PASS** — Graffeo CS, Sivakumar W, Tavakol SA, Carlstrom LP, Van Gompel JJ, Dunn IF, Olson JJ. (2026).
  **Congress of Neurological Surgeons Systematic Review and Evidence-Based Guidelines Update for the Role of Imaging in
  the Management of Patients With Vestibular Schwannomas.** *Neurosurgery*, 98(2), 283–287.
  DOI: 10.1227/neu.0000000000003419｜PMID: 40470931｜OA: N。
  **建議原文取自 CNS 官方全文頁：`https://www.cns.org/guidelines/treatment-adults-vestibular-schwannoma/5-role-of-imaging-in-management-of-patients-with-v`（HTTP 200，2026-09-13）**，
  含「Questions and Recommendations from the Prior Version… Without Change」與 New Question 1–7 的逐字建議。
- **[E-S18] PASS** — Ziu M, Dunn IF, Hess C, Fleseriu M, Bodach ME, Tumialan LM, Oyesiku NM, Patel KS, Wang R, Carter BS,
  Chen JY, Chen CC, Patil CG, Litvack Z, Zada G, Aghi MK. (2016). **Congress of Neurological Surgeons Systematic Review
  and Evidence-Based Guideline on Posttreatment Follow-up Evaluation of Patients With Nonfunctioning Pituitary Adenomas.**
  *Neurosurgery*, 79(4), E541–E543. DOI: 10.1227/neu.0000000000001392｜PMID: 27635964｜OA: N。
  結論段逐字可引。官方全文頁（本次未抓）：`https://www.cns.org/guidelines/guidelines-management-patients-non-functioning-pituitary-adenomas/Chapter_8`。
- **[E-S19] PASS** — Freda PU, Beckers AM, Katznelson L, Molitch ME, Montori VM, Post KD, Vance ML; Endocrine Society.
  (2011). **Pituitary incidentaloma: an Endocrine Society clinical practice guideline.**
  *The Journal of Clinical Endocrinology and Metabolism*, 96(4), 894–904.
  DOI: 10.1210/jc.2010-1048｜PMID: 21474686｜PMCID: PMC5393422｜**OA: Y**。
  Route: Europe PMC `PMC5393422/fullTextXML`，第 1.1、**2.0–2.2**、3.0 節逐字取得。
- **[E-S20] PASS** — Nagano O, Higuchi Y, Serizawa T, Ono J, Matsuda S, Yamakami I, Saeki N. (2008). **Transient expansion
  of vestibular schwannoma following stereotactic radiosurgery.** *Journal of Neurosurgery*, 109(5), 811–816.
  DOI: 10.3171/jns/2008/109/11/0811｜PMID: 18976069｜OA: N。
- **[E-S21] PASS** — Inggas MAM, Apriani S, Hendriansyah L, Wijaya JH. (2025). **Distinguishing pseudoprogression from
  true tumor growth after stereotactic surgery in vestibular schwannoma: a volumetric and clinical trajectory analysis.**
  *Radiation Oncology (London, England)*, 20(1), 185. DOI: 10.1186/s13014-025-02753-1｜PMID: 41382184｜PMCID: PMC12696888｜**OA: Y**。
- **[E-S22] PASS** — Huang CY, Peng SJ, Yang HC, Wu HM, Chen CJ, Wang MC, Hu YS, Lin CJ, Shiau CY, Guo WY, Chung WY, Pan DH,
  Lee CC. (2023). **Association Between Pseudoprogression of Vestibular Schwannoma After Radiosurgery and Radiological
  Features of Solid and Cystic Components.** *Neurosurgery*, 93(6), 1383–1392.
  DOI: 10.1227/neu.0000000000002599｜PMID: 37432016｜OA: N。（另有 2024 年 Letter 與 In Reply 各一，PMID 38529998／38529995。）
- **[E-S23] PASS** — Daher GS, Marinelli JP, Van Gompel JJ, Patel NS, Olson JJ, Carlson ML. (2026). **Congress of
  Neurological Surgeons Systematic Review and Evidence-Based Guideline on Hearing Preservation Outcomes in Patients With
  Sporadic Vestibular Schwannoma: Update.** *Neurosurgery*, 98(2), 298–302.
  DOI: 10.1227/neu.0000000000003551｜PMID: 40470934｜OA: N。**這一組數字的主場是 C 組 C2；E2 只借用「觀察組也會掉」這個方向。**
- **[E-S24] PASS** — McClure JJ, Chatrath A, Robison TR, Jane JA. (2024). **Conditioned recurrence-free survival following
  gross-total resection of nonfunctioning pituitary adenoma: a single-surgeon, single-center retrospective study.**
  *Journal of Neurosurgery*, 140(6), 1614–1619. DOI: 10.3171/2023.10.jns23754｜PMID: 38064693｜OA: N。
- **[E-S25] PASS** — Losa M, Mortini P, Barzaghi R, Ribotto P, Terreni MR, Marzoli SB, Pieralli S, Giovanelli M. (2008).
  **Early results of surgery in patients with nonfunctioning pituitary adenoma and analysis of the risk of tumor
  recurrence.** *Journal of Neurosurgery*, 108(3), 525–532. DOI: 10.3171/jns/2008/108/3/0525｜PMID: 18312100｜OA: N。
- **[E-S26] PASS** — Sheehan J, Lee CC, Bodach ME, Tumialan LM, Oyesiku NM, Patil CG, Litvack Z, Zada G, Aghi MK. (2016).
  **Congress of Neurological Surgeons Systematic Review and Evidence-Based Guideline for the Management of Patients With
  Residual or Recurrent Nonfunctioning Pituitary Adenomas.** *Neurosurgery*, 79(4), E539–E540.
  DOI: 10.1227/neu.0000000000001385｜PMID: 27635963｜OA: N。
  可引結論：49 篇納入、**無 class I 證據**；5 篇 class II 的統合分析顯示術後放射治療相對於觀察可降低復發
  （**OR 0.04，95% CI 0.01–0.20，P<.001**），但**異質性極高（χ²=20.70，P=.003，I²=81%）**；
  結論句「Repeat resection, SRS, SRT, and XRT play a role…」。
- **[E-S27] PASS** — Magill ST, Dalle Ore CL, Diaz MA, Jalili DD, Raleigh DR, Aghi MK, Theodosopoulos PV, McDermott MW.
  (2019). **Surgical outcomes after reoperation for recurrent non-skull base meningiomas.**
  *Journal of Neurosurgery*, 131(4), 1179–1187. DOI: 10.3171/2018.6.jns18118｜PMID: 30544357｜OA: N。
- **[E-S28] PASS** — Magill ST, Lee DS, Yen AJ, Lucas CG, Raleigh DR, Aghi MK, Theodosopoulos PV, McDermott MW. (2019).
  **Surgical outcomes after reoperation for recurrent skull base meningiomas.**
  *Journal of Neurosurgery*, 130(3), 876–883. DOI: 10.3171/2017.11.jns172278｜PMID: 29726777｜OA: N。
- **[E-S29] PASS** — Bakhsheshian J, Wheeler S, Strickland BA, Pham MH, Rennert RC, Carmichael J, Weiss M, Zada G. (2019).
  **Surgical Outcomes Following Repeat Transsphenoidal Surgery for Nonfunctional Pituitary Adenomas: A Retrospective
  Comparative Study.** *Operative Neurosurgery (Hagerstown)*, 16(2), 127–135.
  DOI: 10.1093/ons/opy078｜PMID: 29767762｜OA: N。（另有 Commentary，PMID 30010871。）
- **[E-S30] PASS** — Friso F, Ben Dor N, Conti A, Decio Fabbri A, Calvaruso F, Dallari V, De Cecco F, Bochicchio FF,
  La Corte E, Wojciechowski T, Niemczyk K, Drożdż A, Turek G, Anschuetz L, Soloperto D, et al. (2026).
  **Salvage microsurgery for vestibular schwannoma after failed stereotactic radiosurgery: a multi-institutional
  retrospective study.** *Journal of Neuro-Oncology*, 178(1), 11.
  DOI: 10.1007/s11060-026-05598-0｜PMID: 42159832｜PMCID: PMC13190541｜**OA: Y**。
- **[E-S31] PASS** — Haddad L, Arlt F, Güresir E, Wach J. (2026). **Salvage surgery following primary treatment in
  recurrent vestibular schwannoma: surgical outcomes and progression-free survival — a meta-analysis.**
  *Journal of Neuro-Oncology*, 178(1), 34. DOI: 10.1007/s11060-026-05629-w｜PMID: 42215714｜PMCID: PMC13221319｜**OA: Y**。
- **[E-S32] PASS** — Kaley TJ, Wen P, Schiff D, Ligon K, Haidar S, Karimi S, Lassman AB, Nolan CP, DeAngelis LM,
  Gavrilovic I, Norden A, Drappatz J, Lee EQ, Purow B, Plotkin SR, Batchelor T, Abrey LE, et al. (2015).
  **Phase II trial of sunitinib for recurrent and progressive atypical and anaplastic meningioma.**
  *Neuro-Oncology*, 17(1), 116–121. DOI: 10.1093/neuonc/nou148｜PMID: 25100872｜PMCID: PMC4483051｜OA: N。
  **註：ICOM 表 3 把此試驗標為「Kaley 2014」（線上先行）；正式書目為 2015 年第 17 卷第 1 期。**
- **[E-S33] PASS** — Kumthekar P, Grimm SA, Aleman RT, Chamberlain MC, Schiff D, Wen PY, Iwamoto FM, Gursel DB,
  Reardon DA, Purow B, Kocherginski M, Helenowski I, Raizer JJ. (2022). **A multi-institutional phase II trial of
  bevacizumab for recurrent and refractory meningioma.** *Neuro-Oncology Advances*, 4(1), vdac123.
  DOI: 10.1093/noajnl/vdac123｜PMID: 36225651｜PMCID: PMC9549880｜**OA: Y**。
  **⚠ 與 [E-S40] 的表 3 數字不符**：ICOM 表列第 1 級 PFS-6 90%、且把 n 寫成 42（10/20/12），
  原文摘要則為 **PFS-6 87%／77%／46%**、收案 50 人（42 人為腦膜瘤）。**以原文為準。**
- **[E-S69] 補充紀錄** — Erratum/Corrigendum to Kumthekar et al. *Neuro-Oncology Advances*, 2023, 5(1), vdad103.
  DOI: 10.1093/noajnl/vdad103｜PMID: 37664526。**摘要只有「[This corrects the article DOI: 10.1093/noajnl/vdac123.]」，
  勘誤內容未取得**——引用 [E-S33] 的數字前建議註明有勘誤存在。
- **[E-S34] PASS** — Brastianos PK, Twohy EL, Gerstner ER, Kaufmann TJ, Iafrate AJ, Lennerz J, Jeyapalan S, Piccioni DE,
  Monga V, Fadul CE, Schiff D, Taylor JW, Chowdhary SA, Bettegowda C, Ansstas G, et al. (2023).
  **Alliance A071401: Phase II Trial of Focal Adhesion Kinase Inhibition in Meningiomas With Somatic *NF2* Mutations.**
  *Journal of Clinical Oncology*, 41(3), 618–628. DOI: 10.1200/jco.21.02371｜PMID: 36288512｜PMCID: PMC9870228｜OA: N。
  （同期社論：Focal Adhesion Kinase as a Therapeutic Target for Meningiomas With Somatic NF2 Mutations,
  *JCO* 2023;41(3):675–677，DOI 10.1200/jco.22.01914，PMID 36288506。）
- **[E-S35] PASS** — Preusser M, Silvani A, Le Rhun E, Soffietti R, Lombardi G, Sepulveda JM, Brandal P, Brazil L,
  Bonneville-Levard A, Lorgis V, Vauleon E, Bromberg J, Erridge S, Cameron A, Lefranc F, et al. (2022).
  **Trabectedin for recurrent WHO grade 2 or 3 meningioma: A randomized phase II study of the EORTC Brain Tumor Group
  (EORTC-1320-BTG).** *Neuro-Oncology*, 24(5), 755–767. DOI: 10.1093/neuonc/noab243｜PMID: 34672349｜PMCID: PMC9071312｜OA: N。
- **[E-S36] PASS** — Graillon T, Sanson M, Campello C, Idbaih A, Peyre M, Peyrière H, Basset N, Autran D, Roche C,
  Kalamarides M, Roche PH, Fuentes S, Tabouret E, Barrie M, Cohen A, Honoré S, Boucekine M, et al. (2020).
  **Everolimus and Octreotide for Patients with Recurrent Meningioma: Results from the Phase II CEVOREM Trial.**
  *Clinical Cancer Research*, 26(3), 552–557. DOI: 10.1158/1078-0432.ccr-19-2109｜PMID: 31969329｜OA: N。
- **[E-S37] PASS** — Simó M, Argyriou AA, Macià M, Plans G, Majós C, Vidal N, Gil M, Bruna J. (2014).
  **Recurrent high-grade meningioma: a phase II trial with somatostatin analogue therapy.**
  *Cancer Chemotherapy and Pharmacology*, 73(5), 919–923. DOI: 10.1007/s00280-014-2422-z｜PMID: 24619496｜OA: N。
- **[E-S38] PASS** — Ji Y, Rankin C, Grunberg S, Sherrod AE, Ahmadi J, Townsend JJ, Feun LG, Fredericks RK, Russell CA,
  Kabbinavar FF, Stelzer KJ, Schott A, Verschraegen C. (2015). **Double-Blind Phase III Randomized Trial of the
  Antiprogestin Agent Mifepristone in the Treatment of Unresectable Meningioma: SWOG S9005.**
  *Journal of Clinical Oncology*, 33(34), 4093–4098. DOI: 10.1200/jco.2015.61.6490｜PMID: 26527781｜PMCID: PMC4669593｜OA: N。
  **註：ICOM 表 3 標為「Verschraegen 2015」；Europe PMC 的第一作者為 Ji Y。**
- **[E-S39] PASS** — Limon D, Amiel A, Even Haim S, Gordon N, Tschernichovsky R, Stemmer S, Gal O, Laviv Y, Kanner A,
  Siegal T, Yust-Katz S. (2024). **A phase II, open-label, single-arm trial of pembrolizumab for recurrent meningioma
  and solitary fibrous tumor.** *Neuro-Oncology Advances*, 6(1), vdae154.
  DOI: 10.1093/noajnl/vdae154｜PMID: 39429970｜PMCID: PMC11487343｜**OA: Y**。
- **[E-S40] PASS** — Nassiri F, Wang JZ, et al.（International Consortium on Meningiomas）. (2024).
  **Meningioma: International Consortium on Meningiomas consensus review on scientific advances and treatment paradigms
  for clinicians, researchers, and patients.** *Neuro-Oncology*, 26(10), 1742–1780.
  DOI: 10.1093/neuonc/noae082｜PMID: 38695575｜PMCID: PMC11449035｜**OA: Y**。
  Route: Europe PMC `PMC11449035/fullTextXML`（621 KB XML，純文字 219,008 字元）全文取得；
  所引段落：Systemic Therapies for Meningiomas（含 **Table 3 已完成試驗**、Table 4 進行中試驗）、
  **Radiation-Induced Meningiomas**、NF2-SWN 段、Surgical Management（Simpson）、流行病學與存活段、未來方向段。
  **註：作者欄以 Europe PMC 的 authorString 為準，正文引用時建議寫「International Consortium on Meningiomas (ICOM) 2024 共識綜述」。**
- **[E-S41] PASS（僅書目與摘要）** — Goldbrunner R, Stavrinou P, Jenkinson MD, Sahm F, Mawrin C, Weber DC, Preusser M,
  Minniti G, Lund-Johansen M, Lefranc F, Houdart E, Sallabanda K, Le Rhun E, Nieuwenhuizen D, Tabatabai G, et al. (2021).
  **EANO guideline on the diagnosis and management of meningiomas.** *Neuro-Oncology*, 23(11), 1821–1834.
  DOI: 10.1093/neuonc/noab150｜PMID: 34181733｜PMCID: PMC8563316｜OA: N。
  **全文三條路徑皆失敗（見 FAIL-1）**：Europe PMC fullTextXML 回 0 byte；NCBI efetch 回「The publisher of this article
  does not allow downloading」；academic.oup.com 回 403；pmc.ncbi.nlm.nih.gov 回 reCAPTCHA 擋頁。
  **只可引用摘要中的措辭**（本 brief 引用的那一句出自 abstractText）。
- **[E-S42] PASS（僅書目與摘要）** — Goldbrunner R, Weller M, Regis J, Lund-Johansen M, Stavrinou P, Reuss D, Evans DG,
  Lefranc F, Sallabanda K, Falini A, Axon P, Sterkers O, Fariselli L, Wick W, Tonn JC. (2020).
  **EANO guideline on the diagnosis and treatment of vestibular schwannoma.** *Neuro-Oncology*, 22(1), 31–45.
  DOI: 10.1093/neuonc/noz153｜PMID: 31504802｜PMCID: PMC6954440｜OA: N。
  **全文未取得（fullTextXML 回 0 byte，見 FAIL-2）**；只可引摘要中的那一句
  「Except for bevacizumab in neurofibromatosis type 2, there is no role for pharmacotherapy.」
- **[E-S43] PASS** — Krzemińska A, Więcław J, Koźba-Gosztyła M, Czapiga B. (2026). **Radiation-Induced Meningiomas:
  Systematic Review with Pooled Case Analysis and Case Series of Long Latency, Aggressive Behavior, and Clinical
  Outcomes.** *Journal of Clinical Medicine*, 15(6), 2356. DOI: 10.3390/jcm15062356｜PMID: 41899280｜PMCID: PMC13027033｜**OA: Y**。
  Route: Europe PMC `PMC13027033/fullTextXML`，**修正版 Cahan 準則四條與 Results 全節逐字取得**。
  **設計限制必須寫：這是 237 篇（1953–2025）個案／病例系列的彙整（pooled case analysis），不是 study-level meta-analysis；
  多數變項只有部分病例有資料（分母各不相同，已在 Key facts 逐一標註）。**
- **[E-S44] PASS** — Sadetzki S, Chetrit A, Freedman L, Stovall M, Modan B, Novikov I. (2005). **Long-term follow-up for
  brain tumor development after childhood exposure to ionizing radiation for tinea capitis.**
  *Radiation Research*, 163(4), 424–432. DOI: 10.1667/rr3329｜PMID: 15799699｜OA: N。
- **[E-S45] PASS** — Sadetzki S, Flint-Richter P, Ben-Tal T, Nass D. (2002). **Radiation-induced meningioma: a descriptive
  study of 253 cases.** *Journal of Neurosurgery*, 97(5), 1078–1082. DOI: 10.3171/jns.2002.97.5.1078｜PMID: 12450029｜OA: N。
- **[E-S46] PASS** — Neglia JP, Robison LL, Stovall M, Liu Y, Packer RJ, Hammond S, Yasui Y, Kasper CE, Mertens AC,
  Donaldson SS, Meadows AT, Inskip PD. (2006). **New primary neoplasms of the central nervous system in survivors of
  childhood cancer: a report from the Childhood Cancer Survivor Study.**
  *Journal of the National Cancer Institute*, 98(21), 1528–1537. DOI: 10.1093/jnci/djj411｜PMID: 17077355｜OA: N。
- **[E-S47] PASS** — Bowers DC, Moskowitz CS, Chou JF, Mazewski CM, Neglia JP, Armstrong GT, Leisenring WM, Robison LL,
  Oeffinger KC. (2017). **Morbidity and Mortality Associated With Meningioma After Cranial Radiotherapy: A Report From
  the Childhood Cancer Survivor Study.** *Journal of Clinical Oncology*, 35(14), 1570–1576.
  DOI: 10.1200/jco.2016.70.1896｜PMID: 28339329｜PMCID: PMC5455703｜OA: N。
- **[E-S48] PASS** — Wolf A, Naylor K, Tam M, Habibi A, Novotny J, Liščák R, Martinez-Moreno N, Martinez-Alvarez R,
  Sisterson N, Golfinos JG, Silverman J, Kano H, Sheehan J, Lunsford LD, Kondziolka D. (2019).
  **Risk of radiation-associated intracranial malignancy after stereotactic radiosurgery: a retrospective, multicentre,
  cohort study.** *The Lancet Oncology*, 20(1), 159–164. DOI: 10.1016/s1470-2045(18)30659-4｜PMID: 30473468｜OA: N。
- **[E-S49] PASS** — Rowe J, Grainger A, Walton L, Silcocks P, Radatz M, Kemeny A. (2007). **Risk of malignancy after
  gamma knife stereotactic radiosurgery.** *Neurosurgery*, 60(1), 60–65; discussion 65–66.
  DOI: 10.1227/01.neu.0000255492.34063.32｜PMID: 17228253｜OA: N。
- **[E-S50] PASS** — Sherry AD, Bingham B, Kim E, Monsour M, Luo G, Attia A, Chambless LB, Cmelak AJ. (2020).
  **Secondary malignancy following stereotactic radiosurgery for benign neurologic disease: A cohort study and review of
  the literature.** *Journal of Radiosurgery and SBRT*, 6(4), 287–294. PMID: 32185088｜PMCID: PMC7065897｜OA: N｜**無 DOI**。
- **[E-S51] PASS** — Germano IM, Green S, Lehrer EJ, Ziu M, Olson JJ. (2026). **Congress of Neurological Surgeons
  Systematic Review and Evidence-Based Guideline on the Role of Radiosurgery (Stereotactic Radiosurgery) and Radiation
  Therapy in the Management of Patients With Vestibular Schwannomas: Updates.** *Neurosurgery*, 98(2), 293–297.
  DOI: 10.1227/neu.0000000000003416｜PMID: 40470956｜OA: N。**四條新 level III 建議全文出現在 abstractText 中，可逐字引用。**
  官方全文頁（本次未抓）：`https://www.cns.org/guidelines/treatment-adults-vestibular-schwannoma/6-role-of-radiosurgery-srs-radiation-therapy-in-ma`。
- **[E-S52] PASS（僅書目）** — Cahan WG, Woodard HQ, Higinbotham NL, Stewart FW, Coley BL. (1948).
  **Sarcoma arising in irradiated bone; report of 11 cases.** *Cancer*, 1(1), 3–29.
  DOI: 10.1002/1097-0142(194805)1:1<3::aid-cncr2820010103>3.0.co;2-7｜PMID: 18867438。
  1998 年重印本：*Cancer*, 82(1), 8–34，DOI: 10.1002/(sici)1097-0142(19980101)82:1<8::aid-cncr3>3.0.co;2-w，PMID: 9428476。
  **摘要為空，內文未取得；只可作為「準則的出處」引用，準則條文本身用 [E-S43]。**
- **[E-S53] PASS（僅書目與摘要）** — Plotkin SR, Messiaen L, Legius E, Pancza P, Avery RA, Blakeley JO,
  Babovic-Vuksanovic D, Ferner R, Fisher MJ, Friedman JM, Giovannini M, Gutmann DH, Hanemann CO, Kalamarides M,
  Kehrer-Sawatzki H, et al. (2022). **Updated diagnostic criteria and nomenclature for neurofibromatosis type 2 and
  schwannomatosis: An international consensus recommendation.** *Genetics in Medicine*, 24(9), 1967–1977.
  DOI: 10.1016/j.gim.2022.05.007｜PMID: 35674741｜OA: N。
  **全文未取得**；摘要中的「the term "neurofibromatosis 2" has been retired to improve diagnostic specificity」可逐字引；
  **準則條文本身透過 [E-S54] 的逐字重印取得。**
- **[E-S54] PASS** — Evans DG, Blakeley J, et al. (2025). **History and clinical epidemiology of NF2-related
  schwannomatosis.** *Familial Cancer*, 24(4), 79. DOI: 10.1007/s10689-025-00504-5｜PMID: 41160189｜PMCID: PMC12572065｜**OA: Y**。
  Route: Europe PMC `PMC12572065/fullTextXML`（94 KB XML）全文取得；
  含 **2022 年修訂診斷準則全文重印**、原始與修訂 Manchester 準則兩表、盛行率／出生盛行率／發生率、
  遺傳來源三分法、皮膚與眼科表現比例、鑲嵌型檢測方式與家屬意涵、多發腦膜瘤的非 NF2 鑑別清單、存活段。
- **[E-S55] PASS** — Evans DG, Hartley CL, Smith PT, King AT, Bowers NL, Tobi S, Wallace AJ, Perry M, Anup R, Lloyd SKW,
  Rutherford SA, Hammerbeck-Ward C, Pathmanaban ON, Stapleton E, Freeman SR, et al. (2020).
  **Incidence of mosaicism in 1055 de novo NF2 cases: much higher than previous estimates with high utility of
  next-generation sequencing.** *Genetics in Medicine*, 22(1), 53–59.
  DOI: 10.1038/s41436-019-0598-7｜PMID: 31273341｜OA: N。
- **[E-S57] PASS（附勘誤警告）** — Blakeley JO, Ye X, Duda DG, Halpin CF, Bergner AL, Muzikansky A, Merker VL,
  Gerstner ER, Fayad LM, Ahlawat S, Jacobs MA, Jain RK, Zalewski C, Dombi E, Widemann BC, Plotkin SR. (2016).
  **Efficacy and Biomarker Study of Bevacizumab for Hearing Loss Resulting From Neurofibromatosis Type 2-Associated
  Vestibular Schwannomas.** *Journal of Clinical Oncology*, 34(14), 1669–1675.
  DOI: 10.1200/jco.2015.64.3817｜PMID: 26976425｜PMCID: PMC4872317｜OA: N。
  **⚠ 有 2026 年勘誤（*JCO* 2026;44(8):723，DOI 10.1200/jco-26-00231，PMID 41666344），勘誤內容本次未取得（FAIL-6）。**
- **[E-S58] PASS** — Plotkin SR, Duda DG, Muzikansky A, Allen J, Blakeley J, Rosser T, Campian JL, Clapp DW, Fisher MJ,
  Tonsgard J, Ullrich N, Thomas C, Cutter G, Korf B, Packer R, Karajannis MA. (2019). **Multicenter, Prospective,
  Phase II and Biomarker Study of High-Dose Bevacizumab as Induction Therapy in Patients With Neurofibromatosis Type 2
  and Progressive Vestibular Schwannoma.** *Journal of Clinical Oncology*, 37(35), 3446–3454.
  DOI: 10.1200/jco.19.01367｜PMID: 31626572｜PMCID: PMC7098833｜OA: N。
- **[E-S59] PASS** — Plotkin SR, Allen J, Dhall G, Campian JL, Clapp DW, Fisher MJ, Jain RK, Tonsgard J, Ullrich NJ,
  Thomas C, Edwards LJ, Korf B, Packer R, Karajannis MA, Blakeley JO. (2023). **Multicenter, prospective, phase II study
  of maintenance bevacizumab for children and adults with NF2-related schwannomatosis and progressive vestibular
  schwannoma.** *Neuro-Oncology*, 25(8), 1498–1506.
  DOI: 10.1093/neuonc/noad066｜PMID: 37010875｜PMCID: PMC10398799｜**OA: Y**。
- **[E-S60] PASS** — Screnci M, Puechmaille M, Berton Q, Khalil T, Mom T, Coll G. (2024). **Bevacizumab for Vestibular
  Schwannomas in Neurofibromatosis Type 2: A Systematic Review of Tumor Control and Hearing Preservation.**
  *Journal of Clinical Medicine*, 13(23), 7488. DOI: 10.3390/jcm13237488｜PMID: 39685944｜PMCID: PMC11642482｜**OA: Y**。
- **[E-S61] PASS** — Sheppard J, Kannan S, Halliday J, Rutherford S, Lavin T, Forde C, Smith MJ, Evans G, King AT,
  Islim AI, Pathmanaban ON. (2026). **A systematic review and meta-analysis of outcomes following active surveillance,
  surgery and radiotherapy of meningiomas in NF2-related schwannomatosis.** *Neuro-Oncology Advances*, 8(1), vdag022.
  DOI: 10.1093/noajnl/vdag022｜PMID: 41853812｜PMCID: PMC12994695｜**OA: Y**。

### 台灣端來源

- **[E-S62] PASS** — 衛生福利部中央健康保險署。**全民健康保險藥品給付規定 第 9.37 條 Bevacizumab（如 Avastin）**
  （條文標註日期：100/6/1、101/05/1、106/4/1、108/3/1、109/6/1、112/8/1、113/3/1、113/6/1、113/9/1、114/3/1、114/4/1、114/6/1、114/8/1、**114/10/1**）。檔名 `9.37._20251001.pdf`。
  現行連結此規定的品項 14 筆（其中 10 筆同時連結 14.9.7.，該條為早產兒視網膜病變，檔名 `14.9.7._20250501.pdf`）。
  **七個適應症群組逐字檢視，以「腦膜瘤／神經鞘瘤／聽神經／神經纖維瘤／NF2／schwannoma／meningioma／良性」檢索皆 0 筆。**
  Route: `POST https://info.nhi.gov.tw/api/INAE3000/INAE3000S01/SQL0001`（DRUG_ING=bevacizumab）→
  `GET .../getPDF?DurgFileName=9.37._20251001.pdf&appType=true` → `pdftotext -layout`，2026-09-13。
  人類可讀頁面：`https://info.nhi.gov.tw/INAE3000/INAE3000S02`。
- **[E-S63] PASS** — 同署。**藥品給付規定 第 1.3.2.4 條 Levetiracetam**（101/6/1、102/10/1、108/5/1、111/2/1）。
  檔名 `1.3.2.4._20220201.pdf`。現行連結此規定的品項 56 個藥品代碼。Route 同上（DRUG_ING=levetiracetam），2026-09-13。
- **[E-S64] PASS** — 同署。**全民健康保險醫療服務給付項目及支付標準（全表）**，本次下載檔 22,040,997 bytes、6,163 筆有效紀錄，
  含生效日 **20260401** 與 **20260901** 之條目（即含 115.04.01 與 115.09.01 生效版）。
  Route: `GET https://info.nhi.gov.tw/api/iode0000s01/Dataset?rId=A21030000I-D20020-002`（HTTP 200），2026-09-13 下載後全文檢索。
  人類可讀頁面：`https://www.nhi.gov.tw/ch/cp-18621-7e20c-4002-1.html`。
  **本 brief 引用的條目**：
  - 37028B 三度空間Ｘ光刀立體定位放射手術（82,000 點，生效 20260401）；
  - 37029B 影像導引強度調控X光刀立體定位放射手術（153,229 點，生效 20260401）；
  - 37047B 身體立體定位放射治療（213,662 點，生效 20260401）——**身體部位，與本專題無關，僅記錄以免誤用**；
  - 33084B 磁振造影－無造影劑（6,500 點）／33085B 磁振造影－有造影劑（11,500 點）／33146B Primovist 加計（5,686 點）；
  - 22001C 純音聽力檢查 405／22008B 聲場聽力檢查 2,270／22011B 語言分辨聽力檢查 279／22013B 語言聽力檢查 300／
    22014B 誘發反應聽力檢查 706／22015B 詐聾聽力檢查 800／22023B 耳蝸誘發聽力檢查 2,012／22025B 自記聽力檢查 300／
    22033B 幼兒聽力篩檢（腦幹聽反射）800／22041C 遊戲式聽力檢查 671／20031B 穩定狀態聽性誘發反應 1,000／
    54045B 人工電子耳術後調圖（單耳）1,311；
  - 25021B 染色體檢查(特殊) 4,067／25007B 細胞遺傳學檢查 11,871；
  - 30301B／30302B／30303B 實體腫瘤次世代基因定序（10,000／20,000／30,000 點，生效 20260901）。
  **檢索為零筆者（只證明查詢結果，不得推論有無給付）**：「再照射」0、「再次放射」0、「神經纖維瘤」0、「次世代定序」（品名欄）0。
- **[E-S65] PASS** — 全國法規資料庫。**罕見疾病防治及藥物法**（**修正日期：民國 104 年 01 月 14 日**；
  法規類別：行政＞衛生福利部＞國民健康目）。所引條文：第 1、2、3、4、6、7、8、9、10、11、13 條。
  Route: `https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=L0030003`，2026-09-13。
  同時取得《罕見疾病防治及藥物法施行細則》（修正日期：民國 104 年 12 月 07 日，pcode=L0030004）之書目。
- **[E-S66] PASS（書目與版本日期）** — 全國法規資料庫。**身心障礙者鑑定作業辦法**（**修正日期：民國 115 年 06 月 29 日**；
  法規類別：行政＞衛生福利部＞護理及健康照護目），附「附表一甲 身體系統構造或功能之鑑定人員資格條件及鑑定方法與鑑定工具」等附表 PDF。
  Route: `https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=L0020020`，2026-09-13。**附表內容本次未展開。**
- **[E-S67] PASS（查詢結果，非條文）** — 同署。**健保藥品給付項目查詢結果**（2026-09-13，全頁擷取後以
  `paY_END_DATE` 為空或含「迄今」篩出現行品項）：
  - dexamethasone：total 2,335 筆、現行 483 筆，其中 **480 個藥品代碼的「藥品給付規定」欄位為空**，
    2 筆連結 14.3.（`14.3._19950301_000.pdf`）、1 筆連結 14.9.4.（`14.9.4._20260601.pdf`）；
  - prednisolone：total 1,663 筆、現行 377 筆，**給付規定欄位全部為空**；
  - valproic acid：total 126 筆、現行 17 筆，**全部為空**；
  - phenytoin：total 129 筆、現行 41 筆，**全部為空**；
  - carbamazepine：現行 35 筆連結規定碼 **1.3.2.6.**（`1.3.2.6._20110801_000.pdf`）；
  - lacosamide：現行 15 筆連結規定碼 **1.3.2.9.**（`1.3.2.9._20180801_000.pdf`）。
  Route 同 [E-S62]。**本條只證明「以成分名查詢的結果」，不得據以宣稱有無給付。**
  **注意（沿用 GBM 專題已知陷阱）：本 API 僅 `DRUG_ING` 參數有效，以品名查詢會回傳全庫；民國年字串不可直接比大小。**

### FAIL／未取得（保留，供寫作者知道查過什麼）

- **FAIL-1** — **EANO 2021 腦膜瘤指引全文**（[E-S41]）。三條路徑皆失敗：
  Europe PMC `PMC8563316/fullTextXML` 回 **0 byte**；NCBI efetch 回 XML 但內含
  「The publisher of this article does not allow downloading…」；`academic.oup.com/neuro-oncology/article/23/11/1821/6310110` **HTTP 403**；
  `pmc.ncbi.nlm.nih.gov/articles/PMC8563316/` 回 **reCAPTCHA 擋頁**。
  →**指引原文的追蹤時程、輔助治療條文等內文措辭不可引用**；本 brief 以 NICE NG99[E-S15] 與 ICOM 2024[E-S40] 替代。
- **FAIL-2** — **EANO 2020 聽神經瘤指引全文**（[E-S42]）。`PMC6954440/fullTextXML` 回 0 byte。
  →只能引摘要那一句；追蹤時程改用 CNS 2018／2026[E-S16][E-S17]。
- **FAIL-3** — **SNO 2024 腦瘤癲癇共識綜述全文**（[E-S13]）。Europe PMC fullTextXML 回 0 byte；NCBI efetch 只回到 front matter。
  →**不可引用其內文措辭**。
- **FAIL-4** — **台灣公告的罕見疾病名單（NF2-SWN 在不在裡面）**。
  `www.hpa.gov.tw`（國民健康署）**連線失敗（curl 回 000，零 byte）**；`data.gov.tw` 的 REST API 回 **HTTP 405**。
  →**標 gap，不推論**。寫法：「請向遺傳諮詢中心或罕見疾病相關單位確認」。
- **FAIL-5** — **健保實體腫瘤 NGS 的適應症附表 2.2.1**。支付標準全表 TXT 只含條文正文，**附表不在此資料集內**，
  本次未另行取得。→**不能說腦膜瘤、聽神經瘤或 NF2 在不在 NGS 給付的癌別名單內。**
- **FAIL-6** — **Blakeley 2016 的 2026 年勘誤內容**（*JCO* 2026;44(8):723，PMID 41666344）。
  Europe PMC 的 abstractText 為空，原文未取得。→引用 [E-S57] 的 36% 時要註明有勘誤存在。
- **FAIL-7** — Kessel KA 等？（作者欄未取得）**Re-irradiation of anaplastic meningioma: higher dose and concomitant
  Bevacizumab may improve progression-free survival.** *Radiation Oncology*, 2024;19(1):135.
  DOI: 10.1186/s13014-024-02486-7｜PMID: 39358739｜PMCID: PMC11447990｜OA: Y。
  **本次只取得書目（作者與內文數字未擷取），不可引用其數值。**
- **FAIL-8** — **Proton therapy re-irradiation provides promising clinical results in recurrent brain meningioma.**
  *Acta Oncologica*, 2023;62(9):1096–1101. DOI: 10.1080/0284186x.2023.2241994｜PMID: 37526998｜OA: N。
  **只有書目，不可引用其數值。**
- **FAIL-9** — **聽神經瘤觀察期間的聽力檢查頻次建議**。以 Europe PMC 多組檢索（`"vestibular schwannoma" AND audiometric`、
  `hearing preservation AND evidence-based` 等）**未檢出任何給出頻次建議的指引**。→**標 gap。**
- **FAIL-10** — **NCCN**：依專題規則（抓取回 403）**不查、不引**。
- **FAIL-11** — **PubMed 網頁與 PubMed MCP**：本 session 不可用，全部走 Europe PMC REST（RESEARCH-COMMON 已載明）。
- **FAIL-12** — **腦膜瘤追蹤的國際（非英國）明文時程**。ICOM 2024 明說「Defining the appropriate interval and type of
  surveillance needed for each meningioma subgroup」仍待解[E-S40]；EANO 全文取不到（FAIL-1）。
  →**E2 的腦膜瘤時程表只有 NICE 一個可引來源，寫的時候要標明這件事。**

---

## 附錄：本 brief 打通、可供其他組沿用的三條新路

1. **CNS（Congress of Neurological Surgeons）指引的「全文」可以直接抓**：
   `https://www.cns.org/guidelines/<系列>/<章節 slug>` 回 HTTP 200 且含完整建議文字（本次取得聽神經瘤影像章節）。
   期刊版（Neurosurgery）多半付費牆，但 **CNS 官網版可用**；章節 slug 就寫在各篇摘要的末句。
2. **AAN 指引的退休狀態可以直接查證**：`https://www.aan.com/Guidelines/home/GuidelineDetail/<id>` 回 HTTP 200，
   頁面上有「This guideline is retired.」與退休日期，以及新版指引的「Affirmed by the AAN Institute Board of Directors on …」。
   **索引頁是 JS 驅動、抓不到清單**，要先用搜尋找到 id（本次：AED prophylaxis 舊版 id=30、新版 id=1042）。
3. **NICE 指引全文可以直接抓**：`https://www.nice.org.uk/guidance/<代碼>/chapter/Recommendations` 回 HTTP 200，
   含完整條文與表格，頁面上同時有 Published／Last updated 日期。**pmc.ncbi.nlm.nih.gov 則被 reCAPTCHA 擋，不要浪費時間。**
