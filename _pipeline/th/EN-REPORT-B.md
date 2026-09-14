# EN-REPORT-B — 英文版第三輪對抗式查核（B 組）

英文版寫作期間逐句重述中文時發現的問題。**一律 report-don't-fix**：以下全部照中文原樣寫進英文版，未在英文版裡修正，也未改動中文檔。

查核範圍：`body/th-active-surveillance.html`、`body/th-lobectomy.html`、`body/th-neck-dissection.html`、`body/th-surgery-risks.html`、`meta/B.json`，對照 `brief/B.md`（僅 PASS 條目）、`SPEC.md` §三／§九、`FIXES.md`。

機械項全部通過：四篇的 `<h4>` 數與順序、引用序列、參考條目數與 URL 順序中英完全相同；字數比 0.715–0.786；`<strong>` 密度 2.1–3.6／千字；無 `<h1>`／`<table>`／`<figure>`；結尾皆為 `</ol>` 後一個空 `<p></p>`；四篇中英皆未出現台灣。

---

## 嚴重（2 條）

### B-EN-1｜`th-neck-dissection.html`：需治療人數 500 的白話解釋，方向與同一句印出來的數字相反

**中文原文（〈需治療人數，從 31 變成 500〉第一段）**

> 結構性復發是 11/409（2.7%）對 9/354（2.5%），風險差 0%（95% 信賴區間負 2% 到 2%）；生化復發的風險差同樣是 0%。它算出來的需治療人數是 **500**——意思是要對 500 個人做預防性廓清，才可能換到其中 1 個人少一次復發

**來源實際說的是什麼（Sanabria 2022，[B-S35]，DOI 10.1097/sla.0000000000005388）**

5 個 RCT、763 人；結構性復發 pCND 組 11/409（2.7%）、對照組 9/354（2.5%）；風險差 0%（−2% 到 2%）；NNT = 500；結論逐字「We did not find a beneficial effect of prophylactic CND」。

**問題**

印出來的兩個比例，加做廓清那一組比較**高**（2.7% > 2.5%，差 0.15 個百分點）。緊接著把 NNT 500 解釋成「換到其中 1 個人**少**一次復發」，等於替一個原著明說「找不到好處」的結果指定了一個有利方向。讀者只要把 11/409 和 9/354 相減，就會得到與那句白話相反的正負號。這個數字是全篇的軸心，`meta/B.json` 的 dek（「只收隨機試驗的統合分析算出的需治療人數是 500」）也建在它上面，是最容易被單獨截圖的一句。

**建議裁決方向（不在本輪執行）**：NNT 500 只寫成「它把這個差距換算成需治療人數，得到 500」，並明寫原著結論是找不到好處、兩組復發率實際上一樣（加做的那組還略高一點點）。

**嚴重度：高**

---

### B-EN-2｜`th-neck-dissection.html`：2025 Rec 19A 的 "most" 被吃掉，禁令因此讀成全面禁令

**中文原文（〈2025 年的措辭變嚴了，還刪掉一個情境〉第一段）**

> 2015 年版第 36C 條寫的是：對小型（T1 或 T2）、非侵犯性、臨床上淋巴結陰性的乳突癌與大多數濾泡癌，不做預防性中央區廓清「是適當的」。……2025 年版第 19A 條改成：**這些人**不應該做預防性中央區廓清。

**來源實際說的是什麼（[B-G1] ATA 2025 逐字）**

> RECOMMENDATION 19 A：「Prophylactic central-compartment lymph node dissection should not be performed for **most** small, noninvasive, clinically node-negative PTC (cT1-T2, cN0) and for **most** FTCs.」(Strong recommendation, Moderate certainty evidence)

對照 2015 Rec 36C 逐字：「Thyroidectomy without prophylactic central neck dissection is appropriate for small (T1 or T2), noninvasive, clinically node-negative PTC (cN0) and for **most** follicular cancers.」——2015 在乳突癌前面**沒有** most，2025 **加上了** most。

**問題**

中文用「這些人」把 2015 條文的族群（乳突癌那一格無限定詞）整個搬進 2025 的建議句，於是 2025 新增的那個 most 消失了。結果是：一條指引自己留了餘地的強烈建議，在文章裡讀成對所有 cT1–T2、cN0 乳突癌的全面禁令。這正好是修正 21 要求精確傳達的那一句，而且方向是把建議講得比原文更絕對。英文版照中文寫成 "in these people"，未加 most。

**嚴重度：高**

---

## 中（2 條）

### B-EN-3｜`th-lobectomy.html`：`enrollmentInfo.count = 2` 被寫成「實際隨機的人數是 2 人」

**中文原文（〈這條線底下，沒有隨機試驗〉第二段）**

> 試驗登記上實際隨機的人數是 2 人，2026 年 1 月結案

**來源實際說的是什麼（[B-S29] NCT06235814）**

`enrollmentInfo: {count: 2, type: ACTUAL}`；brief 逐字記為「**實際收案** 2 人（ACTUAL）」。登記表的這個欄位是**收案人數**，不是隨機分派人數；ClinicalTrials.gov 沒有另外給隨機人數。

**問題**

收案與隨機在可行性試驗裡不必然相等（主要終點本身就是「有多少符合資格的人願意入組」）。把它寫成「實際隨機 2 人」，是替登記表補了一個它沒說的欄位。結論（半切 vs 全切至今無可用隨機證據）不受影響，但這是本篇用來撐住整段「沒有隨機試驗」的唯一具體數字。

**嚴重度：中**

### B-EN-4｜`th-active-surveillance.html`：品質評等被綁在「七篇比較性研究」上，來源沒有這樣分

**中文原文（〈它是條文，不是某個醫師的個人風格〉第三段）**

> 美國甲狀腺學會為這一版委託的系統性回顧裡，七篇比較主動監測與立即手術的研究，品質評等只有一篇「尚可」，其餘全是「差」

**來源實際說的是什麼（[B-S17]，DOI 10.1089/thy.2021.0539）**

7 篇比較性研究（5 篇世代 N=5,432、2 篇橫斷 N=538）**＋7 篇非對照治療系列（N=1,219）**；brief 記錄的是「品質：1 篇 fair，其餘全部 poor」，**沒有說這個評等只涵蓋比較性那 7 篇**，也可能是 14 篇全部。

**問題**

把「1 fair / 其餘 poor」指名安在比較性研究那一組，是比來源更精確的敘述。方向上不會誤導（無論怎麼分組，結論都是證據弱），但它替來源決定了一個分母。

**嚴重度：中**

---

## 輕（4 條）

### B-EN-5｜`th-surgery-risks.html`：開場的「2% 到 20%」沒有任何標籤，也沒有來源

第二段「你如果回去上網查，會看到從 2% 到 20% 都有人寫」。這是修辭用的範圍，不是查證過的數字，但它出現在全篇第一個百分比的位置，緊接著就是兩組有來源的區間（2.3–26%、0.5–65%）。HOUSE-STYLE §三要求每一個數字都帶族群標籤；這一個既無標籤也無來源，且與下文兩個真實區間的上下緣都不相同，容易被讀成第三個文獻區間。英文版照寫 "anything from 2% to 20%"。

### B-EN-6｜`th-neck-dissection.html`：Sippel 試驗的「30 人中 27.6%」算術不自洽

「接受廓清的 30 人中 27.6% 有陽性淋巴結」。27.6% × 30 = 8.28，不是整數（27.6% ≈ 8/29）。brief [B-S33] 本身就是這樣記的，屬來源自身的分子分母不合。依 RESEARCH-COMMON §三的判準（算術自洽）應歸入「來源自己標錯」一類，但修正 52 列的六件不含這一件。目前中英文皆照抄。

### B-EN-7｜`th-active-surveillance.html`：「日本的尺寸門檻是 13 毫米」寫成日本獨有

該句只掛 JAES 2021（Table 3 第 1 條「Tumor diameter reaches 13 mm」）。但 KTA 2025 的 5.2.A(1) 同樣是「maximal diameter reaches ≥13 mm」[Level 3]。兩份指引共用同一個門檻，寫成「日本的」會讓讀者以為韓國用的是別的數字。

### B-EN-8｜`th-active-surveillance.html`：「韓國 2021 年那份影像共識」不在本篇的參考清單裡

該句（〈納入的上限〉第二段）沒有引註，而本篇的參考 [3] 是 2024 年那份 KSThR 超音波共識，不是 2021 年的 K-TIRADS（PMID 34719893）。依 FIXES F8 這是刻意把出處收斂到〈照到一顆結節，然後呢〉的結果，**不是缺陷**，此處僅記錄：單看這一頁的讀者查不到那份文件。同理記錄 `th-lobectomy.html` 參考第 3 條的標題含 "A Randomized Clinical Trial"，而小標寫「這條線底下，沒有隨機試驗」——正文已說明那是隨機 2 人的可行性先導，書目標題逐字抄不改（比照 F20 的處理）。

---

## 查核通過、特別確認過的項目

- **修正 19**：2025 Rec 15A 的 `should be a thyroid lobectomy`（Strong / Moderate certainty）在英文版逐字寫出；15B 的 `may be the preferred initial surgical treatment`（Conditional / Low-moderate）與 15C 的 `should include a total thyroidectomy` 情態詞分別對應，未互相滲透。2 公分這條線與「可以半切 → 應該半切」的語氣轉變完整保留。
- **F1**：〈半切之後要不要吃藥〉整段第一句即為 ATA 2025 自己的對照（正常參考範圍下七到八成可以不必補充甲狀腺素，舊版那個偏低區間只剩兩到三成），已核對 brief D 第 157 行的逐字原句。73%／84%／59.3% 三個舊數字各自掛著自己的門檻（TSH > 2 mIU/L）與終點（達標／被診斷／實際用藥），英文版未出現任何「反正都要吃藥」的合併句。依修正 36 與 F12，英文版未印出舊目標的數字區間，只寫 "that older, lower band"。
- **修正 20**：Verloop 22% 以原文（整體甲狀腺低下）呈現，並寫明 ATA 2025 把它標成 biochemical 與原文不符。
- **修正 21**：四個 RCT（181／164／60／101）＋只收 RCT 的統合分析（5 試驗、763 人）、NNT 500、永久副甲狀腺低下 +3%（0%–6%）、`should not be performed`、19B 刪掉 cN1b，六項全數在英文版出現。（其中 NNT 的白話解釋見 B-EN-1、19A 的族群見 B-EN-2。）
- **修正 22–26**：Kuma 原著終身進展機率六個數字以原著摘要為準並註明與日本共識不符；年齡梯度 22.5%／4.9%／2.5% 與 Kuma 30 年那組數字在同一段（F19）；延遲手術兩個 OR 與 Nguyen 2025 的反面結論齊備；退出主因（進展 57／病人 43／醫師 31）與焦慮 37.9% 齊備；監測期間不驗甲狀腺球蛋白（Rec 13，Good Practice Statement，英文加 "which the guideline does not grade"）；納入上限仍寫死 cT1a ≤1 公分，61 人／112 人／291 人三筆都標了中心數與追蹤長度。
- **修正 27**：2.3%–26% 與 0.5%–65% 在英文版都與「怎麼查」「怎麼定義」綁在同一句，未塌縮成單一百分比；常規喉鏡 OR 1.92 保留；瑞典 SQRTPA 兩篇的良性世代標籤在同段內外各出現一次；手術量三個門檻（26／50／100）以區間呈現；Hsiao 2022 的數字四篇皆未使用。
- **F10**：`hazard ratio` 只用在 Adam 2014 的三個 OS 風險比與瑞典登錄的死亡／腎功能／心血管風險比；Kandil、Wang、Zhao 一律 `relative risk`。`th-lobectomy-en` 在 relative risk 第一次出現處加了與 hazard ratio 的差別（「一個是比例相除，一個是比事件到達的速度」）。
- **統計名詞擁有權（SPEC-EN §3）**：`odds ratio` 在 `th-active-surveillance-en` 白話化一次；`relative risk`（含與 hazard ratio 的差別）在 `th-lobectomy-en`；`non-inferiority` 在 `th-neck-dissection-en`。三篇之外未重複解釋，`hazard ratio` 未在 B 組重新解釋（擁有權在 `th-pathology-en`）。
- **紅線 3／6／7**：主動監測寫成有納入退出條件與團隊要求的計畫，未寫成病人可自行決定；未給鈣片與活性維生素 D 的劑量或天數，收在「你手術醫院的術後補鈣流程」；未寫任何院內配置、自費金額或機器型號。
- **紅線 4**：四篇皆未出現台灣，也未從指引條文推論任何地區的臨床實務或普及程度。
