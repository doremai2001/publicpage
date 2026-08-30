# B 組查證 brief — 結腸癌專題（B1–B4）

查證日期：2026-08-27　｜　查證人：B 組 research agent
期刊來源一律經 Europe PMC REST API（`search?query=EXT_ID:…` 或 `DOI:"…"`，`resultType=core`）逐條核對。
**卷期頁、DOI、PMID 一律照 API 回傳值抄寫，沒有回傳的欄位就不寫。**
每個來源的連結一律用 `https://europepmc.org/article/MED/<PMID>`（已逐條測到 HTTP 200；出版社網站對機器人回 403，人用瀏覽器可開）。
指引與台灣官方文件另附各自的官方連結。

> **寫稿人請先讀這三條**
> 1. 只能引用標記 **PASS** 的來源。FAIL 條目保留在最後一節，是給下一輪查證看的，不准引用。
> 2. 交叉引用歸屬：本 brief **刻意不提供** ctDNA/MRD 的任何試驗數字（屬 D2）、oxaliplatin 神經毒性的發生率數字（屬 C1）、運動介入試驗數字（屬 D4，CHALLENGE 試驗數據已從本 brief 移除）、TNM 名詞解釋與 ≥12 顆的意義（屬 A2）、MMR/MSI 檢驗本身（屬 A4）、暫時性造口（屬 C3）、急症警語完整清單（屬 C2）。這些主題在本 brief 出現時只寫成「指向哪一篇」。
> 3. **B2 不得引用 IDEA 的任何數字**（第十節明訂 IDEA 歸 B3）。B2 需要談療程長度時只寫一句「療程要三個月還是六個月，見〈三個月還是六個月〉」。

---

# B1 — 拿幾顆淋巴結，決定的是什麼

## Key facts

### 切除範圍與腸繫膜淋巴結廓清（CME / D3 vs 傳統 D2）——**這一題是有爭議的，證據不站在 CME 那一邊**

- RELARC 是目前唯一一個比較「完整腸繫膜切除（CME）」與標準 D2 廓清的大型隨機試驗：中國 17 家醫院、2016-01-11 至 2019-12-26 收案、1,072 人隨機分派（CME 536、D2 536），主要分析納入 995 人（CME 495、D2 500），對象是右側結腸癌 [S1]。
- RELARC 主要終點 3 年無病存活期（DFS，指手術後到復發、出現新的原發癌或死亡之間的時間）**沒有達到顯著差異**：CME 組 86.1%、D2 組 81.9%，風險比（HR，兩組事件發生速度的比值）0.74（95% 信賴區間 0.54–1.02，P = 0.06）；3 年整體存活率 CME 94.7%、D2 92.6%（HR 0.70，95% CI 0.43–1.16，P = 0.17）[S1]。
- RELARC 作者自己的結論是：「這個試驗未能找到 CME 優於標準 D2 的無病存活證據，標準 D2 廓清應為這些病人的常規術式（Standard D2 dissection should be the routine procedure）；CME 只在腸繫膜淋巴結明顯侵犯的病人才需考慮」[S1]。
- RELARC 5 年追蹤（995 人）同樣沒有整體存活差異：5 年 OS HR 0.74（95% CI 0.51–1.07，P = 0.105）、癌症特異存活 HR 0.72（95% CI 0.49–1.06，P = 0.091）。只有在第三期（OS HR 0.58，95% CI 0.37–0.93，P = 0.023）、特別是 pN2（OS HR 0.25，95% CI 0.11–0.57，P = 0.001）與有淋巴血管侵犯的次族群出現有利於 CME 的訊號，且交互作用檢定顯著 [S2]。**次族群分析不是主要終點，不能寫成「第三期就該做 CME」。**
- 支持 CME 的主要證據是**回溯性、族群資料**而非隨機試驗：丹麥哥本哈根首都區 2008-06-01 至 2011-12-31 的族群研究，CME 組 364 人 vs 非 CME 組 1,031 人，4 年 DFS 85.8%（95% CI 81.4–90.1）vs 75.9%（72.2–79.7），多變項校正後 HR 0.59（95% CI 0.42–0.83）[S3]。這是觀察性資料，**兩組來自不同醫院**，作者自己寫的是「associated with」。

### 腹腔鏡與開腹的長期腫瘤學結果（四個隨機試驗，逐一查證）

- **COST（美國，NEJM 2004）**：48 家機構、872 人隨機分派，中位追蹤 4.4 年。3 年復發率腹腔鏡 16% vs 開腹 18%（HR 0.86，95% CI 0.63–1.17，P = 0.32）；3 年整體存活 86% vs 85%（HR 0.91，95% CI 0.68–1.21，P = 0.51）；傷口部位復發兩組都 <1%（P = 0.50）。住院天數 5 天 vs 6 天（P < 0.001）[S4]。
- **COST 5 年更新（Ann Surg 2007）**：確認腹腔鏡不劣於開腹 [S5]。
- **COLOR（歐洲，Lancet Oncol 2009）**：29 家歐洲醫院、1,248 人隨機分派，1,076 人納入分析（腹腔鏡 534、開腹 542），中位追蹤 53 個月。3 年 DFS 腹腔鏡 74.2%（95% CI 70.4–78.0）vs 開腹 76.2%（72.6–79.8）（P = 0.70）；差值 2.0%（95% CI −3.2 到 7.2）。**兩組切下的淋巴結數目相近**。作者自己寫：因為 95% 信賴區間上限「剛好超過」預設的 7% 非劣性界線，這個試驗**無法完全排除**開腹較好的可能 [S6]。這是誠實寫法的好材料。
- **CLASICC（英國，Lancet 2005；長期追蹤 Br J Surg 2013）**：27 家英國中心、794 人以 2:1 隨機分派 [S7]。中位追蹤 62.9 個月，整體存活與 DFS 兩組沒有統計顯著差異 [S8]。**關鍵發現：結腸癌病人術中由腹腔鏡轉開腹（conversion）者整體存活較差（HR 2.28，95% CI 1.47–3.53，P < 0.001）、DFS 也較差（HR 2.20，95% CI 1.31–3.67，P = 0.007）**[S8]。這是「腹腔鏡不等於一定做得完」的最好證據。
- **Barcelona 單中心試驗（Lancet 2002；長期 Ann Surg 2008）**：219 人（腹腔鏡 111、開腹 108），中位追蹤 95 個月，報告腹腔鏡組復發風險較低（HR 0.47，95% CI 0.23–0.94）、癌症相關死亡較低（0.44，0.21–0.92）、全死因死亡較低（0.59，0.35–0.98）[S9][S10]。**單一中心、219 人，結論比其他三個大型多中心試驗都樂觀，不可以拿它當代表性結果。**

### 取樣數目不足時會發生什麼

- 系統性回顧納入 9 個國家 17 篇研究、共 61,371 名病人：儘管方法學異質性大、各研究採用的門檻從 6 顆到 40 顆不等，**17 篇中有 16 篇報告第二期結腸癌檢出淋巴結數目越多、存活越好**；6 篇有第三期資料的研究中有 4 篇也呈現同方向 [S11]。
- INT-0089 試驗的次級分析：第三期結腸癌病人，分析的淋巴結數目越多，存活越好 [S12]。
- ≥12 顆的定義與名詞解釋歸 A2。**B1 只寫手術端怎麼做才拿得到足夠的淋巴結，以及數目不足代表的是「這份報告的資訊量不夠」而不是「癌症比較輕」。**

### 急症（阻塞、穿孔）手術的不同處境

- 台灣長庚單一機構、1995-01 至 2005-12、1,492 名右側結腸癌開腹切除病人：306 人（20.5%）以腸阻塞表現。阻塞組手術併發症率 22.2% vs 非阻塞 14.1%（P = 0.0005）、手術死亡率 3.9% vs 1.9%（P = 0.041）[S13]。
- 同一研究：阻塞在**第二期**是獨立的預後不良因子（598 人，log-rank P = 0.001；Cox 迴歸 P = 0.012），但在**第三期不是**（424 人，P = 0.116 / 0.108）[S13]。這一條同時是 B1 與 B2 的橋樑。
- 暫時性造口何時會出現，**由 C3 寫完整，B1 只用一句話帶過並指向 C3**。

## Claim ceiling

**Defensible**：
「以目前唯一的大型隨機試驗（RELARC）來看，標準 D2 廓清在右側結腸癌的三年與五年結果，並沒有輸給更大範圍的 CME；支持 CME 的資料主要來自回溯性的族群研究。腹腔鏡與開腹在四個隨機試驗裡的長期腫瘤學結果相當，選哪一種取決於腫瘤位置、腹內沾黏、體型與這家醫院的經驗，而不是哪一種比較『先進』。真正跟長期結果有關的，是能不能完成一個乾淨的切除——CLASICC 顯示術中被迫轉開腹的病人，長期結果明顯比較差。淋巴結檢出數目不足，改變的是**你手上這份報告能提供多少資訊**，不是癌症的嚴重度。」

**Would overstate（越線句）**：
- ✗「完整腸繫膜切除（CME／D3）可以提高存活率，應該優先選擇這種術式。」——RELARC 主要終點是**陰性**的。
- ✗「腹腔鏡手術的長期結果比開腹好。」——只有 219 人的單中心 Barcelona 試驗這樣講，三個大型試驗都是「相當」。
- ✗「淋巴結拿不到 12 顆，代表手術沒做好。」——檢出數目受腫瘤位置、切除長度、病人體型、病理科取材方式、術前有無治療影響，不是單一術者品質指標。
- ✗ 任何暗示「選腹腔鏡就不會有造口」的寫法（固定紅線 C）。
- ✗ 拿 RELARC 的 pN2 次族群（HR 0.25）當作結論。那是次族群分析。

## Caveats / safety notes（必寫）

- **讀者最容易誤讀成「我的醫師沒有幫我做最好的手術」。** 一定要寫清楚：D2 是隨機試驗支持的常規做法，不是「比較簡單的版本」。
- **淋巴結數目不足時，正確的下一步是回頭問病理與外科，不是自行決定要不要化療。** 數目不足會把第二期的風險評估往「資訊不足」推（見 B2），不是自動升級成需要化療。
- **不要把「轉開腹」寫成手術失敗。** CLASICC 的 HR 2.28 反映的是這群病人本來腫瘤或腹內狀況就比較複雜（選擇偏誤），不是「因為轉開腹所以變差」。這一點寫錯會讓已經轉開腹的病人恐慌。
- **急診手術的病人讀到這一段會覺得自己輸在起跑點。** 要同時寫：阻塞在第二期是預後因子之一，但它是「評估時要一起看的一項」，不是判決。
- 不可以出現「本院」的術式成績或淋巴結平均檢出數；不可點名批評其他醫院或外科團隊（醫療法 §84、§86）。可以批評的對象只有「整個領域的慣例還沒跟上證據」。

## Taiwan status

- **gap**：CME/D3 與傳統廓清、腹腔鏡與開腹在台灣健保的**手術給付、自付差額或特材差額**，本輪查證**未取得任何官方條文**（健保署「藥品給付規定」只涵蓋藥品，不含手術術式）。文章一律寫成「這一項的費用與給付條件要跟你的個管師或醫院醫務課確認」，**不得**宣稱有給付、不得宣稱沒給付、不得寫「不貴」或「負擔得起」（規格第四節、固定紅線 C）。
- **gap**：機械手臂（robotic）結腸切除的給付狀態同上，未查證，不寫。
- B1 不觸及藥品，因此不需要固定紅線 A 的急症警語段落；若行文提到任何化療藥名，一句話帶過並指向 C2。

---

# B2 — 第二期到底要不要化療　**【紅線 1】**

## Key facts

### 絕對獲益有多小（帶分母）

- **QUASAR**（Lancet 2007）：1994-05 至 2003-12、19 個國家 150 家中心、3,239 名「復發風險低、是否該做輔助化療不明確」的大腸直腸癌病人隨機分派為化療（5-FU + folinic acid，n = 1,622）或觀察（n = 1,617）。其中 **2,963 人（91%）是第二期（淋巴結陰性）**，2,291 人（71%）是結腸癌，中位年齡 63 歲 [S14]。
- QUASAR 結果：中位追蹤 5.5 年，化療組 311 人死亡、觀察組 370 人死亡，全死因死亡相對風險 0.82（95% CI 0.70–0.95，P = 0.008）；復發 293 vs 359，相對風險 0.78（0.67–0.91，P = 0.001）[S14]。
- **QUASAR 作者自己換算的絕對數字**：「假設不化療的 5 年死亡率是 20%，本研究觀察到的相對風險換算成**絕對存活改善為 3.6%（95% CI 1.0–6.0）**」[S14]。**這是本篇最重要的一個數字，一定要帶著信賴區間寫，而且要說明它是在「5 年死亡率 20%」這個假設下算出來的。**
- QUASAR 同時報告：化療組 8 人（0.5%）、觀察組 4 人（0.25%）在隨機分派後 30 週內死於非大腸直腸癌原因，其中 1 例被判定「可能與化療相關」[S14]。**好處與代價要放在同一段。**
- **SACURA**（EJC 2018，日本）：1,982 名第二期結腸癌病人隨機分派為單純手術（997）或術後 1 年口服 tegafur-uracil（UFT，985），中位追蹤 69.5 個月，中位年齡 66 歲，IIA/IIB/IIC 分佈 84%/13%/3%。5 年 DFS 78.4% vs 80.2%，**HR 0.91（95% CI 0.75–1.10，P = 0.31），未能證明 UFT 較優**；5 年整體存活 94.3% vs 94.5%（HR 0.93，95% CI 0.66–1.31）[S15]。
- SACURA 的次族群分析：**有復發風險因子的病人也沒有從 UFT 得到好處**（作者原句：Patients with risk factors for recurrence did not benefit from UFT）[S15]。
- SACURA 另一個對讀者很重要的數字：約 9% 的病人發生第二種癌症，這些第二癌**佔了 DFS 事件的 40.7%**[S15]。也就是說第二期病人的「復發風險」裡有一大塊其實不是原本那顆大腸癌。

### 「高風險第二期」的定義，各家指引不一致——**逐字比對**

- **ESMO（Argilés 等，Ann Oncol 2020；2026-02 的 Express Update 明文確認這份 2020 CPG 仍是母版指引）**[S20][S21]，其分層與建議為：
  - 低風險第二期：「For patients with low-risk stage II colon cancer, follow-up is recommended [I, A].」（追蹤即可）
  - 中度風險：「For patients with intermediate risk (non-MMR/MSI + any risk factor except pT4 or <12 lymph nodes assessed), 6 months of fluoropyrimidines should be recommended [I, B].」
  - 高風險：「Patients with high-risk stage II (pT4 or <12 lymph nodes or multiple intermediate risk factors, regardless of MSI) may be considered for the addition of oxaliplatin [I, C].」
  - **注意 ESMO 把「檢出淋巴結 < 12 顆」直接列為高風險特徵之一，且把 pT4 與 <12 顆單獨拉出來、與其他中度風險因子分開處理。**
- **ESMO 2026-02 Express Update 的第二期治療流程圖（Figure 1）附註 a 逐字寫**：「For pT4 MSI: pT4 is a major risk factor but adjuvant ChT benefit in the presence of MSI is uncertain.」（pT4 是主要風險因子，但在 MSI 存在的情況下輔助化療的效益並不確定）[S21]。**這是 2026 年 ESMO 自己承認「這一格沒有答案」的原文，是本篇最有力的誠實材料。**
- **ASCO（Baxter 等，JCO 2022，Adjuvant Therapy for Stage II Colon Cancer: ASCO Guideline Update）**[S19]，逐字：
  - 「Adjuvant chemotherapy (ACT) is not routinely recommended for patients with stage II colon cancer who are not in a high-risk subgroup.」
  - 「Patients with **T4 tumors** are at higher risk of recurrence and **should be offered** ACT, whereas patients with **other high-risk factors, including sampling of fewer than 12 lymph nodes in the surgical specimen, perineural or lymphovascular invasion, poorly or undifferentiated tumor grade, intestinal obstruction, tumor perforation, or grade BD3 tumor budding, may be offered** ACT.」
  - **ASCO 把 T4 的動詞寫成 should be offered，其他所有高風險特徵寫成 may be offered——這是與 ESMO 最可比對的一處措辭差異。**
  - 「The addition of oxaliplatin to fluoropyrimidine-based ACT is not routinely recommended, but may be offered as a result of shared decision making.」
  - 「Patients with mismatch repair deficiency/microsatellite instability tumors **should not be routinely offered ACT**; if the combination of MMR deficiency/MSI and high-risk factors results in a decision to offer ACT, **oxaliplatin-containing chemotherapy is recommended**.」
- **NCCN**：現行版本為 **NCCN Guidelines for Colon Cancer, Version 2.2026（2026-04-07）**（此版本號與日期取自 NCCN 官方公開的 NCCN Guidelines for Patients®: Colon Cancer, 2026 版 PDF，該 PDF 逐字寫「NCCN Guidelines® for Colon Cancer, Version 2.2026 —April 7, 2026.」）[S22]。該病人版對第二期的敘述是：「Your doctor may (or may not) recommend chemotherapy. They will consider the cancer sub-stage (2A, 2B, or 2C), the mismatch repair status, and any high-risk features found in the tumor.」[S22]
  - ⚠️ **NCCN 專業版演算法（含完整高風險特徵條列）需登入，本輪未能取得原文（見 [S45] FAIL）。文章可以指出「NCCN 現行版本是 2.2026（2026 年 4 月 7 日）」並引用上面這句病人版原文，但不得逐條列出 NCCN 的高風險特徵清單，也不得宣稱 NCCN 與 ESMO / ASCO 在某一項上「相同」或「不同」。**
- **可以據實寫的分歧本身**：ESMO 把「<12 顆」列進**高風險**（可考慮加 oxaliplatin），ASCO 把「<12 顆」列進 **may be offered** 那一組（與 T4 的 should be offered 分開）。ASCO 額外把「grade BD3 tumor budding」「intestinal obstruction」「tumor perforation」寫進條列，ESMO 2020 的第二期條文則沒有把 tumor budding 單獨列名。

### dMMR / MSI-H 第二期的特殊性——**這是紅線 1 的核心**

- **Ribic 等（NEJM 2003）**：最早報告高度微衛星不穩定（MSI-H）／錯誤配對修復缺損（dMMR）的結腸癌病人預後較好，且**不從 5-FU 為基礎的輔助化療得到好處** [S16]。
- **Sargent 等（JCO 2010）**：457 名第二、三期病人（隨機分派到 5-FU 為基礎治療 229 人 vs 術後不治療 228 人），其中 70 人（15%）為 dMMR。
  - 錯誤配對修復功能正常（pMMR）者，輔助化療顯著改善 DFS：HR 0.67（95% CI 0.48–0.93，P = 0.02）。
  - **dMMR 者接受 5-FU 沒有改善 DFS：HR 1.10（95% CI 0.42–2.91，P = 0.85）。**
  - 併入先前分析後的 1,027 人資料集（其中 165 人 dMMR）中，**「在第二期且 dMMR 的病人，接受治療與較差的整體存活相關：HR 2.95（95% CI 1.02–8.54，P = 0.04）」**[S17]。
  - ⚠️ **這個 HR 2.95 的 95% 信賴區間下界是 1.02，幾乎貼著 1；它來自一個次族群、樣本數小。寫的時候必須寫成「有一個訊號顯示可能更差，但這個估計很不精確」，不可以寫成「單用 5-FU 會害死 dMMR 的第二期病人」。**（見下方 Caveats）
- **MOSAIC 10 年更新（André 等，JCO 2015）**：2,246 名第二、三期切除後病人，中位追蹤 9.5 年。
  - **第二期：10 年整體存活率 LV5FU2 組 79.5% vs FOLFOX4 組 78.4%，HR 1.00，P = 0.980——在第二期，加上 oxaliplatin 對 10 年整體存活沒有任何幫助。**
  - 對照組：第三期 59.0% vs 67.1%（HR 0.80，P = 0.016）；全體 67.1% vs 71.7%（HR 0.85，P = 0.043）。
  - 1,008 份檢體中 95 人（9.4%）為 dMMR、94 人（10.4%）帶 BRAF 突變。dMMR 是獨立的預後因子（HR 2.02，95% CI 1.15–3.55，P = 0.014）[S18]。
  - **「MOSAIC 第二期加 oxaliplatin 的 10 年 OS HR 恰好等於 1.00」是本篇最乾淨的一句話。**
- MMR / MSI 檢驗本身怎麼做、代表什麼 → **由 A4 寫完整，B2 不重新解釋**（第十節）。B2 只寫「這一格報告如果是 dMMR，第二期的化療討論會整個換一套邏輯」。

### 淋巴結取樣數目與第二期判斷的關係

- 17 篇研究、61,371 人的系統性回顧中，**16 篇報告第二期結腸癌檢出淋巴結數目越多、存活越好**[S11]。這條同時支撐 B1 與 B2，但 B2 只寫「數目不足會如何影響第二期的判斷」（第十節），不重新解釋 ≥12 顆的意義（歸 A2）。
- ESMO 把 <12 顆列為高風險特徵、ASCO 把它列為 may be offered 的其中一項 [S19][S20]。**兩家指引都把「取樣不足」當成一個需要納入討論的變數，而不是一個自動觸發化療的開關。**

### T4 / pT4 這個特殊處境

- ASCO：T4 是唯一被寫成 **should be offered** 的第二期特徵 [S19]。
- ESMO：pT4 與 <12 顆一起被歸入**高風險**，可考慮加 oxaliplatin [S20]。
- ESMO 2026 Express Update 附註：**pT4 合併 MSI 時，輔助化療的效益「uncertain」**[S21]。
- 台灣長庚 1,492 人資料：**腸阻塞在第二期是獨立的預後不良因子**（598 名第二期病人，Cox 迴歸 P = 0.012），但在第三期不是 [S13]。急診以阻塞表現的第二期病人，是「這份病理報告以外還要加看的一項」。

### ctDNA

- **只能寫這一句、不得給任何數字或試驗結論**：「目前有以 ctDNA（血中循環腫瘤 DNA）來決定第二期要不要做化療的臨床試驗，這件事完整寫在〈ctDNA 驗不到，代表什麼〉那一篇。」（第十節硬性規定）

## Claim ceiling　**【紅線 1，最高風險】**

**Defensible（可以寫到這裡為止）**：
「第二期輔助化療的絕對獲益很小——QUASAR 在假設不化療的 5 年死亡率為 20% 的前提下，算出的絕對存活改善是 3.6%（95% 信賴區間 1.0% 到 6.0%）。而『誰算高風險』這件事，ESMO、ASCO 兩家指引的條列與措辞就已經不一樣：ASCO 只有 T4 用『應該提供』，其他特徵都是『可以提供』；ESMO 則把 pT4 和淋巴結取樣不足 12 顆一起放進高風險。如果你的報告是 dMMR／MSI-H，單用 fluoropyrimidine 這條路在現有資料裡看不到好處，甚至有一個不精確的訊號顯示第二期可能更差；而在第二期加上 oxaliplatin，MOSAIC 追蹤十年後的整體存活風險比是 1.00。所以這不是一個能在文章裡替你決定的題目——**這是一個要帶著你的病理報告去門診談的決定，而且你有權要求對方說出他評估的是哪幾項。**」

**Would overstate（任一句出現即失敗）**：
- ✗「第二期通常不需要化療。」／「第二期不用化療。」
- ✗「有高風險特徵的第二期病人應該接受化療。」／「第二期都應該化療。」
- ✗「絕對獲益只有 3.6%，所以做不做差別不大。」——3.6% 對某些人是決定性的，這句話等於替讀者做了決定。
- ✗「MSI-H 的第二期病人做化療會更糟。」——證據是一個 95% CI 下界 1.02 的次族群估計，只能寫成「有訊號、不精確」。
- ✗「加 oxaliplatin 對第二期沒用。」——MOSAIC 第二期 10 年 OS 的 HR 是 1.00，但那是一個試驗的次族群分析，而且指引仍為特定高風險族群保留了這個選項。寫成「在 MOSAIC 追蹤十年後，第二期加 oxaliplatin 的整體存活風險比是 1.00」而不是一句斷語。
- ✗ 引用 IDEA 的任何數字（歸 B3）。
- ✗ 給任何 ctDNA 的數字或試驗結論（歸 D2）。
- ✗ 給 oxaliplatin 神經毒性的發生率（歸 C1）。
- ✗ 逐條列出 NCCN 的高風險特徵清單（本輪未取得原文，見 [S45]）。

**結論的形狀（硬性）**：本篇不得出現對任何一邊的一般性建議。結尾必須落在「帶哪幾份資料去門診、可以問出口的哪幾個問題」（B 組收尾方向）。

## Caveats / safety notes（必寫，不是參考）

- **兩個方向都是傷害。** 一個讀完決定不做化療的第二期高風險病人，可能死於一個原本可能被治癒的癌症；一個讀完硬要做化療的低風險病人，可能承受終身的神經病變換不到任何存活好處。這句判斷必須在文章前段就出現，不能藏在文末。
- **QUASAR 的 3.6% 有一個前提句。** 它是在「假設不化療的 5 年死亡率是 20%」下換算出來的。不寫這個前提，讀者會以為 3.6% 是所有第二期病人的固定值。
- **Sargent 的 HR 2.95 是本 brief 裡最脆弱的一個數字**（95% CI 1.02–8.54，次族群，樣本小）。規格紅線 1 寫的是「甚至可能更差」——證據**剛好只夠支撐「可能」這兩個字**，不夠支撐「會」。這一點請寫作規格照著調整。
- **不可暗示「化療做完就結束了」**（固定紅線 C）。
- **不可在最脆弱的段落寫「費用不是問題」**（固定紅線 C）。第二期的健保給付狀況見下方 Taiwan status，本身就是這個決定的一部分。
- **淋巴結數目不足不是「自動要化療」的開關。** 讀者最容易誤讀成「我只有 8 顆，所以我一定要化療」。正確的讀法是：資訊不足會讓風險估計變得不可靠，這件事本身要在門診被講出來。
- **這篇若提到 5-FU / capecitabine / oxaliplatin 的藥名，需依固定紅線 A 保留與自己直接相關的一兩條急症警語並指向 C2**；完整清單歸 C2。
- 藥物劑量只能當背景（例如「六個月是八個療程」），**不可寫成用法用量**（規格第四節）。

## Taiwan status

**以下三條取自健保署官方 PDF 原文，逐字可查：**

- **oxaliplatin（藥品給付規定 9.10）逐字**：「1.和 5-FU 和 folinic acid 併用 …（2）**作為第三期結腸癌(Duke's C) 原發腫瘤完全切除手術後的輔助療法。(98/2/1)**」[S40][S41]
  → **健保給付的輔助性 oxaliplatin 限第三期結腸癌。第二期不在條文之內。**
- **capecitabine（藥品給付規定 9.17）逐字**：「4.**第三期結腸癌患者手術後的輔助性療法，以八個療程為限。（96/9/1）**」[S41]
  → **健保給付的輔助性 capecitabine 同樣限第三期，且上限八個療程。第二期不在條文之內。**
- **時效性確認**：健保署第 9 節（抗癌瘤藥物）自 113/6/1 之後的各次修訂對照表中，114/2/1、114/6/1、114/7/1、114/8/1、114/10/1、115/1/1、115/2/1、115/8/1 各版**均未修改 9.10 或 9.17 的結腸癌輔助治療條文**（逐份下載後以「結腸／大腸／直腸」關鍵字比對）[S42][S43][S44]。截至 2026-08-27，上述兩條為現行條文。

**寫法要求**：
- 可以寫「健保對輔助性 oxaliplatin 與 capecitabine 的給付條文寫的是第三期」，並附上健保署 PDF 連結。
- **不可以**由此推論「第二期做化療要自費」或「第二期沒有任何健保給付的化療選項」——單方 5-FU/leucovorin 注射劑、UFUR 等品項的給付條文本輪**未逐條查證**，屬 **gap**。
- **gap**：第二期病人若經醫師判斷需要輔助化療，實際上哪些藥品、在什麼條件下由健保支付，本輪無法從官方條文完整還原。文章一律寫成「第二期的給付條件要跟你的個管師或醫院醫務課確認」。
- **gap**：MMR/MSI 檢驗本身的給付狀態未在 B 組查證（該題歸 A4）。B2 不得宣稱該檢驗有給付或需自費。

---

# B3 — 三個月還是六個月

## Key facts

### IDEA 合作計畫的全部數字

- **IDEA 是六個同時進行的隨機第三期試驗（CALGB/SWOG 80702、IDEA France、SCOT、ACHIEVE、TOSCA、HORG）的前瞻性、預先規劃的合併分析**，收案期間 2007-06-20 至 2015-12-31，跨 12 個國家，對象是第三期結腸癌、ECOG 體能狀態 0–1、年滿 18 歲的病人；隨機分派到 3 個月或 6 個月的 FOLFOX（每 2 週）或 CAPOX（每 3 週），**用哪個處方由主治醫師決定，不是隨機分派的**[S23][S24]。
- **主要終點（NEJM 2018）**：在 12,834 名病人發生 3,263 個復發或死亡事件後，**非劣性未被確認**：整體族群 HR 1.07（95% CI 1.00–1.15）。非劣性的門檻是「雙側 95% 信賴區間上限不超過 1.12」——1.15 超過了，所以**形式上失敗**[S23]。
- **CAPOX 與 FOLFOX 的差異（NEJM 2018）**：
  - CAPOX：3 個月對 6 個月 **達到非劣性**，HR 0.95（95% CI 0.85–1.06）。
  - FOLFOX：3 個月對 6 個月 **未達非劣性**，HR 1.16（95% CI 1.06–1.26）[S23]。
- **風險分層（NEJM 2018，探索性分析）**：
  - **低風險（T1–T3 且 N1）**：3 個月不劣於 6 個月，3 年 DFS **83.1% vs 83.3%**，HR 1.01（95% CI 0.90–1.12）。
  - **高風險（T4 或 N2 或兩者）**：6 個月優於 3 個月，3 年 DFS **64.4%（6 個月）vs 62.7%（3 個月）**，合併處方 HR 1.12（95% CI 1.03–1.23，P = 0.01 for superiority）[S23]。
  - **高風險組的絕對差距是 1.7 個百分點。** 這個數字一定要寫出來。
- **最終整體存活（Lancet Oncol 2020）**：中位追蹤 72.3 個月（IQR 72.2–72.5），12,835 人中觀察到 2,584 例死亡；5,064 人（39.5%）接受 CAPOX、7,771 人（60.5%）接受 FOLFOX。
  - 全體：5 年 OS **3 個月 82.4%（95% CI 81.4–83.3）vs 6 個月 82.8%（81.8–83.8）**，HR 1.02（95% CI 0.95–1.11），非劣性 FDR 校正 p = 0.058 → **整體存活的非劣性同樣未被確認**。
  - CAPOX：5 年 OS 82.1%（80.5–83.6）vs 81.2%（79.2–82.9），HR 0.96（0.85–1.08），非劣性 FDRadj p = 0.033。
  - FOLFOX：5 年 OS 82.6%（81.3–83.8）vs 83.8%（82.6–85.0），HR 1.07（0.97–1.18），非劣性 FDRadj p = 0.34。
  - 更新後的 DFS：HR 1.08（95% CI 1.02–1.15），非劣性 FDRadj p = 0.25 [S24]。
- **IDEA 作者自己的結論原句（Lancet Oncol 2020）**：「非劣性未被確認，但 5 年整體存活 **0.4%** 的絕對差距應該放在臨床脈絡裡看；整體存活結果支持大多數第三期結腸癌病人使用 3 個月的輔助 CAPOX。這個結論因為較短療程大幅降低毒性、不便與費用而更加成立。」[S24]
- **SCOT（IDEA 六個試驗之一，Lancet Oncol 2018）**：獨立發表的「3 個月 vs 6 個月 oxaliplatin-fluoropyrimidine 輔助治療」國際隨機第三期非劣性試驗，開放取用 [S25]。
- **ESMO 對 IDEA 分層的警告（2026-02 Express Update 第三期流程圖附註 a，逐字）**：「Stage III risk subgroups are based on a post hoc analysis from the IDEA collaboration and should be applied with caution. Levels of evidence and grades of recommendation for ChT regimens are lower for low-risk and high-risk subgroups compared with the overall population due to the exploratory nature of the analyses.」[S21]　**指引自己說這個分層要「小心使用」，這是誠實勝過乾淨的最佳材料。**
- **ASCO 2022 對療程長度的敘述（逐字）**：「Duration of oxaliplatin-containing chemotherapy is also addressed, with recommendations for 3 or 6 months of treatment with capecitabine and oxaliplatin or fluorouracil, leucovorin, and oxaliplatin, with decision making informed by key evidence of 5-year disease-free survival in each treatment subgroup and the rate of adverse events, including peripheral neuropathy.」[S19]（注意：這句在 ASCO 是第二期指引的脈絡下寫的。）

### 輔助化療的起始時間窗　**【固定紅線 B 的主場】**

- **Biagi 等（JAMA 2011）系統性回顧與統合分析**：納入 10 項研究、15,410 名切除後的大腸直腸癌病人（7 篇正式論文、3 篇摘要）。**10 項中有 9 項是世代或族群研究，只有 1 項是隨機試驗的次級分析。**
  - **每延遲 4 週開始輔助化療，整體存活的風險比是 1.14（95% CI 1.10–1.17）、無病存活的風險比是 1.14（95% CI 1.10–1.18）。**
  - 各研究之間沒有顯著異質性；校正潛在發表偏誤後、以及排除權重最大的研究後，結果仍然顯著 [S26]。
  - ⚠️ **這是觀察性資料的統合分析，存在適應症混淆（開始得晚的人往往是術後恢復比較差、併發症比較多的人）。作者自己寫的是「associated with」。**
- **ACCENT/IDEA 合併分析（Gallois 等，JCO 2023）**：11 個輔助試驗、第三期結腸癌病人。
  - **提早中止全部治療（ETD，指在完成計畫療程的 75% 之前把所有藥都停掉）：10,447 人納入分析，20.9% 屬於 ETD。ETD 與較差的 DFS（HR 1.61，P < 0.001）與較差的整體存活（HR 1.73，P < 0.001）相關。**
  - **只停 oxaliplatin、繼續用 fluoropyrimidine（EOD）：7,243 人納入分析，18.8% 屬於 EOD。EOD 與 DFS（HR 1.07，P = 0.3）或整體存活（HR 1.13，P = 0.1）沒有顯著相關。**
  - **但是：接受不到計畫 oxaliplatin 療程 50% 的病人結果較差。**
  - 作者結論原句：「這些資料支持在已接受超過 50% 計畫療程、且有明顯神經毒性的病人，停掉 oxaliplatin 而繼續使用 fluoropyrimidine。」[S27]
  - **這一條是 B3 與 C1（紅線 5）的接點：療程長度本身是療效的一部分，把全部停掉（ETD）和只調整 oxaliplatin（EOD）在資料上是兩件完全不同的事。**
- **生育保存的時間窗**（必須在第一次化療之前）→ 主場在 C4，**B3 只用一句話帶過並指向 C4**（固定紅線 B）。

## Claim ceiling

**Defensible**：
「IDEA 合作計畫的正式結論是：三個月**沒有**被證明不劣於六個月——無論是無病存活（HR 1.07，95% CI 1.00–1.15，上限超過預設的 1.12）還是整體存活（HR 1.02，95% CI 0.95–1.11）。但同一批資料同時顯示：五年整體存活的絕對差距只有 0.4 個百分點；用 CAPOX 的人，三個月的整體存活風險比是 0.96；T1–T3 且 N1 的低風險族群，三年無病存活是 83.1% 對 83.3%；而 T4 或 N2 的高風險族群，六個月比三個月多了 1.7 個百分點。所以『三個月還是六個月』不是一個對錯題，是一個把處方（CAPOX 還是 FOLFOX）、期別細節（T 幾、N 幾）和你能承受多少毒性一起放上桌的討論——而且 ESMO 自己在指引裡註明，這個風險分層來自事後分析，要小心使用。至於什麼時候開始：統合分析顯示每晚四週開始，死亡風險上升約 14%，但那是觀察性資料，開始得晚的人本來術後狀況就比較差。」

**Would overstate（越線句）**：
- ✗「三個月和六個月效果一樣。」——非劣性**在形式上失敗了兩次**（DFS 與 OS）。
- ✗「現在標準已經改成三個月了。」——IDEA 的結論是「支持大多數病人使用 3 個月的 **CAPOX**」，處方是條件的一部分。
- ✗「高風險族群一定要做滿六個月。」——絕對差距是 1.7 個百分點，而且分層是探索性分析。
- ✗「術後超過 8 週（或任何一個具體週數）開始化療就沒有效果了。」——Biagi 給的是**每 4 週的連續斜率**，不是一個懸崖式的截止點。不可以造一個 brief 裡沒有的門檻數字。
- ✗「副作用太大可以少做幾次。」／「太難受可以自己停。」（紅線 5，即使 C1 是主場，B3 也不准出現這種讀法）
- ✗ 給 oxaliplatin 神經毒性的**發生率數字**（歸 C1）。B3 只寫「療程長度與神經毒性的取捨」這一層。

## Caveats / safety notes（必寫）

- **這篇最危險的誤讀是「反正三個月和六個月差不多，我做三個月就好」，而讀者其實是 T4N2 用 FOLFOX 的人。** 處方與期別必須和月數綁在一起寫。
- **第二危險的誤讀是把「起始時間窗」讀成「我已經超過了，所以做了也沒用」。** 一定要寫清楚 Biagi 是連續斜率、是觀察性資料，而且晚開始不等於不該開始。
- **ETD vs EOD 的區別必須寫出來，而且要寫成「這是要由醫師調整的，不是你自己減量」**（紅線 5 的精神）。ACCENT/IDEA 顯示「全部停掉」與明顯較差的結果相關（DFS HR 1.61、OS HR 1.73），而「只停 oxaliplatin、繼續口服藥」則沒有。**這一段寫錯會直接造成病人自行跳過療程。**
- **不可寫成用法用量。** 「三個月是四個週期的 CAPOX」可以當背景；具體劑量、體表面積換算、減量幅度一律不寫（規格第四節）。
- **固定紅線 A**：本篇提到 5-FU、capecitabine、oxaliplatin，必須保留與這幾個藥直接相關的一兩條急症警語（寫出藥名與具體症狀，例如 oxaliplatin 的冷誘發喉頭緊縮感），並一句話指向 C2；完整清單歸 C2。
- **固定紅線 B**：年輕病人的生育保存必須在第一次化療之前——一句話帶過並指向 C4。
- 不可暗示「化療做完就結束了」（固定紅線 C）。

## Taiwan status

- **capecitabine 輔助療程上限（官方條文，逐字）**：「4.第三期結腸癌患者手術後的輔助性療法，**以八個療程為限**。（96/9/1）」[S41]
  → 三週一個療程、八個療程，對應的正是「六個月」那一端。**這條條文本身就是台灣讀者在門診會遇到的現實約束，位置要跟數據一樣顯眼（規格第四節）。**
- **oxaliplatin 輔助給付（官方條文，逐字）**：「（2）作為第三期結腸癌(Duke's C) 原發腫瘤完全切除手術後的輔助療法。(98/2/1)」[S40][S41]。**條文中未見療程數上限。**
- **時效性**：健保署第 9 節自 113/6/1 之後的 114/2/1、114/6/1、114/7/1、114/8/1、114/10/1、115/1/1、115/2/1、115/8/1 各次修訂對照表均未變動上述兩條 [S42][S43][S44]。截至 2026-08-27 為現行條文。
- **gap**：三個月（四個療程 CAPOX）與六個月（八個療程）在健保申報、事前審查或療程認定上是否有差別，**本輪未取得官方文件**。文章寫成「療程要做幾次、健保怎麼認，要跟你的個管師或醫院醫務課確認」。
- **gap**：術後多久內開始輔助化療在台灣有無任何行政或給付上的時限，**查不到正式條文**，不得推測。

---

# B4 — 免疫治療不是每個人的選項　**【紅線 2】**

> ⚠️ **2026 年的重大變動，寫稿前務必先看**：本題在 2025–2026 之間發生了實質改變。ATOMIC 試驗（NEJM 2026）證明在**第三期 dMMR 結腸癌**的輔助治療加上 atezolizumab 可改善無病存活，而 NCCN Colon Cancer v2.2026（2026-04-07）已把它寫進第三期的治療敘述。**「免疫治療只用在轉移性病人」這種 2023–2024 年的寫法現在是錯的。**

## Key facts

### dMMR / MSI-H 有多少人（帶分母）

- **轉移性**：CAIRO、CAIRO2、COIN、FOCUS 四個第三期試驗的合併分析，3,063 名轉移性大腸直腸癌病人的原發腫瘤檢體中，**153 人（5.0%）為 dMMR**；250 人（8.2%）帶 BRAF 突變 [S28]。
  → **這就是紅線 2 的「大約每 20 個轉移性結腸癌病人裡只有 1 個」的出處。**
- 同一分析：dMMR 的轉移性病人**預後較差**（PFS HR 1.33，95% CI 1.12–1.57；OS HR 1.35，95% CI 1.13–1.61），而作者的解讀是這個較差的預後主要由 BRAF 突變驅動（dMMR 中有 53/153，34.6% 帶 BRAF 突變，pMMR 中只有 197/2,910，6.8%，P < 0.001）[S28]。
- **非轉移（早期）**：NICHE-2 論文開頭逐字寫「dMMR tumors can be found in **10 to 15%** of patients with nonmetastatic colon cancer」[S31]。
- 其他早期族群的實測分母：Sargent 的 457 名第二、三期病人中 **70 人（15%）為 dMMR**[S17]；MOSAIC 的 1,008 份第二、三期檢體中 **95 人（9.4%）為 dMMR**[S18]。
- **早期比轉移性高出一截，是因為 dMMR 的腫瘤本來就比較不容易轉移。** 這個對比是本篇最重要的一組數字，因為讀者常把「10–15%」誤套到自己的轉移性情境。
- MMR / MSI 檢驗本身怎麼做、報告怎麼看 → **歸 A4，B4 不重新解釋**（第十節）。

### KEYNOTE-177（第一線轉移性 dMMR/MSI-H）

- **設計**：第三期、開放標籤，307 名未曾治療的轉移性 MSI-H/dMMR 大腸直腸癌病人以 1:1 隨機分派，接受 pembrolizumab 每 3 週一次（n = 153）或化療（以 5-FU 為基礎，可加 bevacizumab 或 cetuximab）（n = 154）。**化療組在中央確認疾病惡化後可以跨組（crossover）接受 pembrolizumab。** 雙主要終點是無惡化存活（PFS）與整體存活（OS）[S29]。
- **首次報告（NEJM 2020，第二次期中分析，中位追蹤 32.4 個月）**：中位 PFS **16.5 個月 vs 8.2 個月**，HR 0.60（95% CI 0.45–0.80，P = 0.0002）。客觀反應率 43.8% vs 33.1%。有反應的病人中，24 個月時仍持續有反應者為 83% vs 35%。**當時整體存活資料尚未成熟（僅達所需事件數的 66%），維持盲性**[S29]。
- **5 年追蹤（Ann Oncol 2025，資料截止 2023-07-17，中位追蹤 73.3 個月，範圍 64.9–89.2）**：
  - **中位整體存活 77.5 個月 vs 36.7 個月，HR 0.73（95% CI 0.53–0.99）；5 年整體存活率 54.8% vs 44.2%。**
  - 中位 PFS 16.5 個月 vs 8.2 個月，HR 0.60（95% CI 0.45–0.79）。
  - 中位反應持續時間 75.4 個月 vs 10.6 個月。
  - **跨組（crossover）警告——這是本篇必寫的方法學限制**：化療組 154 人中，**57 人（37.0%）依照試驗計畫跨組接受 pembrolizumab，另有 39 人（25.3%）在試驗外接受 PD-(L)1 抑制劑，實際跨組率 62%**。也就是說，「化療組」的中位存活 36.7 個月裡，有超過六成的人後來也用到了免疫治療 [S30]。
  - **不良事件**：pembrolizumab 組 80% vs 化療組 99% 發生不良事件；**第 3–5 級：22% vs 67%**[S30]。首次報告的治療相關第 3 級以上不良事件同樣是 22% vs 66%（化療組有 1 人死亡）[S29]。

### 局部（未轉移）dMMR 結腸癌的術前免疫治療

- **NICHE-2（NEJM 2024）**：第二期（phase 2）**單臂**研究，115 名未轉移、局部侵犯較廣、未曾治療的 dMMR 結腸癌病人接受術前 nivolumab + ipilimumab。
  - 兩個主要終點是（一）安全性，定義為手術如期進行（因治療相關毒性延後手術不超過 2 週）；（二）3 年無病存活。
  - 113/115（98%，97.5% CI 93–100）如期手術；2 人手術延後超過 2 週。
  - **第 3 或 4 級免疫相關不良事件發生在 5 人（4%）**；沒有人因不良事件停藥。
  - 111 人納入療效分析：**109 人（98%，95% CI 94–100）有病理反應**，其中 105 人（95%）為主要病理反應（殘存活性腫瘤 ≤10%）、**75 人（68%）為病理完全反應（0% 殘存活性腫瘤）**。
  - **中位追蹤 26 個月（範圍 9–65），無人復發。**[S31]
  - ⚠️ **NICHE-2 的第二個主要終點是 3 年無病存活，但這篇 NEJM 論文報告時中位追蹤只有 26 個月，論文的結論句只寫到「安全性可接受、高比例達到病理反應」，並未宣告 3 年 DFS 結果。本輪在 Europe PMC 檢索 Chalabi 於 2025–2026 年的著作，未找到 NICHE-2 的 3 年 DFS 正式論文（見 [S46] FAIL）。**
  - **NICHE-2 沒有對照組。「無人復發」是 115 人、中位追蹤 26 個月的單臂觀察，不是與手術＋標準治療比較的結果。**
- **ATOMIC（Sinicrope 等，NEJM 2026）——這是這個主題目前唯一的第三期隨機證據**：
  - 712 名**切除後第三期 dMMR** 結腸癌病人 1:1 隨機分派：atezolizumab + mFOLFOX6 六個月、之後 atezolizumab 單用（合計 12 個月療程）（n = 355）vs 單用 mFOLFOX6 六個月（n = 357）。
  - 中位年齡 64 歲，55.1% 為女性，**53.9% 屬 T4、N2 或兩者（高風險）**。
  - **中位追蹤 40.9 個月時，3 年無病存活 86.3%（95% CI 81.8–89.8）vs 76.2%（95% CI 70.9–80.6），HR 0.50（95% CI 0.35–0.73，P < 0.001）。**
  - **代價：第 3 或 4 級不良事件發生率 84.1% vs 71.9%。**[S32]
  - **好處與代價在同一段：DFS 絕對差 10.1 個百分點，換來第 3–4 級不良事件多 12.2 個百分點。這正是紅線 2 要求的「好處與代價不可分割」的最佳範例。**
- **指引已出現分歧（可以據實寫）**：NCCN Colon Cancer **v2.2026（2026-04-07）** 的病人版逐字寫「For dMMR or MSI-H cancers, an immunotherapy drug called atezolizumab (Tecentriq) may be given with chemotherapy」於第三期 [S22]；而 ESMO 在 **2026-02** 的 Express Update 中，第三期治療流程圖仍只列 FOLFOX/CAPOX 相關選項與 IDEA 的療程長度 [S21]。**兩份 2026 年的指引在同一題上進度不同——這是誠實、可查證、而且對台灣讀者有實際意義的分歧。**

### 微衛星穩定（MSS）／pMMR 的轉移性結腸癌：檢查點抑制劑沒有站得住的療效證據

- **Le 等（NEJM 2015）**：第二期研究，41 名病人接受 pembrolizumab。
  - **錯誤配對修復正常（pMMR）的大腸直腸癌：免疫相關客觀反應率 0%（0/18）**，20 週免疫相關無惡化存活率 11%（2/18）。
  - dMMR 的大腸直腸癌：反應率 40%（4/10），20 週 PFS 率 78%（7/9）。
  - pMMR 組中位 PFS 2.2 個月、中位 OS 5.0 個月；dMMR 組兩者皆未達到（疾病惡化或死亡的 HR 0.10，P < 0.001；死亡 HR 0.22，P = 0.05）。
  - 全外顯子定序：dMMR 腫瘤平均每個腫瘤 1,782 個體細胞突變，pMMR 為 73 個（P = 0.007）[S33]。
- **IMblaze370（Lancet Oncol 2019）——第三期隨機試驗，這是最硬的一條**：
  - 11 個國家 73 個中心，363 名先前至少兩線化療失敗的轉移性大腸直腸癌病人以 2:1:1 隨機分派為 atezolizumab + cobimetinib（183）、atezolizumab 單用（90）或 regorafenib（90）。**高微衛星不穩定病人的收案上限被設定為 5%**（也就是說這是一個以 MSS 為主的族群）。
  - **中位整體存活：atezolizumab + cobimetinib 8.87 個月（95% CI 7.00–10.61）、atezolizumab 單用 7.10 個月（6.05–10.05）、regorafenib 8.51 個月（6.41–10.71）。合併對 regorafenib 的 HR 1.00（95% CI 0.73–1.38，P = 0.99）；atezolizumab 單用對 regorafenib 的 HR 1.19（0.83–1.71，P = 0.34）。主要終點未達成。**
  - 作者結論原句：「這些結果凸顯了要把免疫治療的好處擴展到基礎免疫發炎程度較低的腫瘤（例如微衛星穩定的轉移性大腸直腸癌）有多困難。」[S34]
- ⚠️ **一個必須知道、但不可誤用的 2025 年新資料**：NICHE 研究的 pMMR 世代（Nature 2025）中，31 名**早期（未轉移）** pMMR 結腸癌病人接受術前 nivolumab + ipilimumab，反應率 26%，其中 6 人達主要病理反應（殘存活性腫瘤 ≤10%）[S35]。
  → **這是早期、術前、雙藥合併、第二期單臂研究，不是轉移性、不是單藥。它不推翻「MSS 轉移性大腸直腸癌單用檢查點抑制劑沒有站得住的療效證據」這句話，但它使得「免疫治療對 MSS 完全無效」變成一句不精確的話。** 寫作時請把限定語完整寫出來：「**轉移性**的微衛星穩定大腸直腸癌，**單用**檢查點抑制劑」。

### 免疫相關不良反應（irAE）：發生率與「可能不會好」的那幾種

- **KEYNOTE-177 的第 3 級以上不良事件是 22%**（對照化療組 67%）[S30]。**這是本篇最貼近讀者情境的一個數字。**
- **ATOMIC 的第 3 或 4 級不良事件是 84.1%**（合併化療），對照單用化療 71.9%[S32]。
- **NICHE-2 的第 3 或 4 級免疫相關不良事件是 5/115（4%）**（雙藥、術前、短療程）[S31]。
- **致死性 irAE（Wang 等，JAMA Oncol 2018）**：112 個試驗、19,217 名病人的統合分析中，毒性相關死亡率為 **anti-PD-1 0.36%、anti-PD-L1 0.38%、anti-CTLA-4 1.08%、PD-1/PD-L1 併用 CTLA-4 1.23%**；7 個學術中心 3,545 名接受 ICI 治療病人的回溯資料顯示死亡率 0.6%。WHO 藥物警戒資料庫 2009 至 2018-01 共 613 例致死事件；心肌炎的致死比例最高（131 例通報中 52 例死亡，39.7%），而**內分泌事件與腸炎的通報致死率只有 2% 到 5%**。從症狀出現到死亡的中位時間 32 天 [S36]。
- **內分泌不良反應的發生率（Barroso-Sousa 等，JAMA Oncol 2018）**：38 個隨機試驗、7,551 名病人的統合分析，評估全等級的甲狀腺功能低下、甲狀腺功能亢進、腦下垂體炎、原發性腎上腺功能不全、胰島素缺乏型糖尿病。
  - 甲狀腺功能低下與亢進的發生率在 PD-1 + CTLA-4 併用組最高；相對 ipilimumab，併用組發生甲狀腺低下的勝算比（OR，**不是機率倍數**）3.81（95% CI 2.10–6.91，P < 0.001）、甲狀腺亢進 OR 4.27（2.05–8.90，P = 0.001）。
  - PD-1 抑制劑相對 ipilimumab，甲狀腺低下 OR 1.89（1.17–3.05，P = 0.03）。
  - 腦下垂體炎：PD-1 抑制劑相對 ipilimumab 較少（OR 0.29，0.18–0.49，P < 0.001）；併用組較多（OR 2.2，1.39–3.60，P = 0.001）。
  - **原發性腎上腺功能不全與胰島素缺乏型糖尿病因事件數太少，作者未做統計推論。**[S37]
  - ⚠️ **這篇是勝算比，不是絕對機率。規格第三節要求「勝算比不是機率倍數」，而且要求有絕對數字就寫絕對數字——本 brief 沒有可靠的絕對發生率百分比可供引用（該統合分析的 log-odds 隨機效果模型未提供可直接引用的合併百分比），所以文章請寫「哪一類藥比較容易出現」而不要編造百分比。**
- **免疫治療引起的第 1 型糖尿病（統合分析，Diabetes Res Clin Pract 2026）**：納入 2020 年 1 月以後發表的 10 項研究、65,925 名接受 ICI 治療的病人。**合併發生率 0.58%（95% CI 0.35–0.92%）；其中約 37% 以糖尿病酮酸中毒（DKA）表現。** 雙免疫藥物併用顯著增加風險；原本就有糖尿病與是否發生 ICI-T1DM 無顯著相關 [S38]。
  → **0.58%、其中 37% 以酮酸中毒表現——這是「罕見但可能是急症、而且是終身的」最好的一組數字。**
- **腦下垂體炎的不可逆性（Nguyen 等，Endocr Relat Cancer 2021，開放取用）**：MD Anderson 2003-05 至 2017-08 的回溯研究，83 名疑似免疫相關腦下垂體炎病人，中位追蹤 1.75 年（範圍 0.6–3）。62 名確診者中最常見的表現為疲倦 66%、頭痛 60%、中樞性甲狀腺功能低下 94%、中樞性腎上腺功能不全 69%、MRI 變化 77%。
  - **各內分泌軸的恢復比例：甲狀腺軸 24%、性腺軸 58%、腎上腺軸 0%。**
  - **高劑量類固醇或停用免疫治療，與內分泌功能恢復無關。**
  - 非腦下垂體炎組 19 人中，1 人為單獨中樞性甲狀腺低下、6 人為單獨中樞性腎上腺功能不全，**全部在最後一次追蹤時仍在使用荷爾蒙補充。**[S39]
  → **「腎上腺軸恢復比例 0%」是本篇最有份量的一個數字。它把「終身」這兩個字變成可查證的。**
- irAE 的處理指引：ASCO Management of Immune-Related Adverse Events: ASCO Guideline Update（JCO 2021，39(36):4073–4126）為現行版；本輪檢索未找到 2024–2026 的 ASCO 更新版 [S40b]。

## Claim ceiling　**【紅線 2】**

**Defensible（可以寫到這裡為止）**：
「這個選項的前提是一份特定的檢驗結果。轉移性結腸直腸癌裡，四個第三期試驗合併的 3,063 名病人中，只有 153 人（5.0%）是 dMMR——大約每二十個人裡一個。如果你在這一類，KEYNOTE-177 追蹤超過五年後的中位整體存活是 77.5 個月對化療的 36.7 個月，而且這個比較裡有六成的化療組病人後來也用到了免疫治療；同時，這個療法的第 3 級以上不良事件是 22%，其中有幾種——腦下垂體炎造成的腎上腺功能不全（一項 62 人的追蹤中恢復比例是 0%）、免疫治療引起的第 1 型糖尿病（發生率 0.58%，其中約 37% 以酮酸中毒發病）、甲狀腺功能失調——一旦發生就可能要補充荷爾蒙一輩子。**如果你不在這一類，目前沒有可以站得住的證據支持你用它：IMblaze370 這個以微衛星穩定病人為主的第三期隨機試驗，單用 atezolizumab 對 regorafenib 的整體存活風險比是 1.19，主要終點沒有達成。**另外，2026 年有一個新的變化：ATOMIC 試驗顯示第三期 dMMR 的病人在輔助化療上加 atezolizumab，三年無病存活從 76.2% 提高到 86.3%，代價是第 3–4 級不良事件從 71.9% 上升到 84.1%——這件事在台灣的給付狀態要跟你的個管師確認。」

**Would overstate（任一句出現即失敗）**：
- ✗「免疫治療是比化療更好的新一代療法。」（紅線 2 明訂）
- ✗「免疫治療副作用比化療小。」——KEYNOTE-177 的第 3 級以上事件確實是 22% 對 67%，但 irAE 的**性質**不同（可能終身、可能致命），不是同一個量尺。要寫成「不良事件的**種類**不一樣」。
- ✗「MSI-H 的病人做免疫治療就會好。」——5 年整體存活率是 54.8%。
- ✗「免疫治療對 MSS 完全無效。」——限定語必須寫全：**轉移性、單用**。NICHE 的 pMMR 早期世代（Nature 2025）反應率 26%，是研究中的做法，不是臨床選項。
- ✗「NICHE-2 顯示術前免疫治療可以取代手術／可以免開刀。」——NICHE-2 的主要終點之一就是「手術如期進行」，所有病人都開了刀。
- ✗「NICHE-2 顯示術前免疫治療的病人不會復發。」——115 人、單臂、中位追蹤 26 個月，3 年 DFS 尚未正式發表（[S46]）。
- ✗「第三期 dMMR 現在都應該加 atezolizumab。」——ATOMIC 是一個試驗；ESMO 的 2026-02 版第三期流程圖尚未納入；台灣給付狀態未查到（見下）。
- ✗ 把好處寫一段、代價放文末（紅線 2 明訂**必須在同一段**）。
- ✗ 重新解釋 MMR/MSI 檢驗本身（歸 A4）。

## Caveats / safety notes（必寫）

- **這篇的失敗模式是一個 MSS 病人讀完去要求免疫治療。** 開頭第一段就要把分母寫出來（5.0%，153/3,063），不可以放到中段。
- **好處與代價必須寫在同一段**（紅線 2 硬性要求）。不可以「療效一段、副作用放文末」。
- **「終身」這兩個字要有出處。** 腎上腺軸恢復比例 0%（62 人）、ICI-T1DM 0.58% 且 37% 以酮酸中毒發病——這兩個數字讓「可能是終身的」不再是恐嚇。
- **不可暗示「免疫治療沒有化療那麼傷身」。** ATOMIC 組合療法的第 3–4 級不良事件是 84.1%。
- **KEYNOTE-177 的跨組必須寫出來。** 62% 的實際跨組率會讓「77.5 個月對 36.7 個月」這個對比被低估或高估的方向難以直覺判斷——誠實寫法是：這個比較不是「免疫治療 vs 完全沒有免疫治療」。
- **固定紅線 A**：本篇若提到 bevacizumab、cetuximab、5-FU（KEYNOTE-177 的對照組處方），需保留與之直接相關的一兩條急症警語並指向 C2。**另外必須加一條 irAE 專屬的當天聯絡條件**：新出現的持續腹瀉、呼吸喘、異常疲倦合併低血壓、莫名口渴與多尿（可能是 ICI 引起的第 1 型糖尿病、可能以酮酸中毒發病）——這幾條在 C2 沒有涵蓋（C2 的主場是化療藥），B4 必須自己寫。
- **不可寫「費用不是問題」**（固定紅線 C）。
- **不可引用個案故事當作代表性結果**（紅線 4 的精神同樣適用）。

## Taiwan status

**已取得官方條文（健保署藥品給付規定 9.69 免疫檢查點抑制劑）：**

- **pembrolizumab 用於 MSI-H/dMMR 大腸直腸癌——逐字**：「(11)大腸直腸癌：限 pembrolizumab 做為**無法切除或轉移性**高微衛星不穩定性(MSI-H)或錯誤配對修復功能不足性(dMMR)大腸直腸癌(CRC)之成年病人**第一線治療**。(114/6/1)」[S43]
  → 生效日 **民國 114 年 6 月 1 日（2025-06-01）**。
- 同節其他限制（逐字）：「(5) 給付時程期限：自初次處方用藥日**起算 2 年**」；「(7)每次申請以 **12 週**為限」[S43]。
- 同節的生物標記表現對照表中，「大腸直腸癌(單用)」在 pembrolizumab 欄位標示「**不需檢附報告**」（即不需檢附 PD-L1 表現量報告）[S43]。
- **時效性**：健保署第 9 節自 114/6/1 之後的 114/7/1、114/8/1、114/10/1、115/1/1、115/2/1、115/8/1 各次修訂對照表中，**未再變動大腸直腸癌的免疫檢查點抑制劑條文**（115/2/1 版本涉及大腸直腸癌的是 9.66 trifluridine/tipiracil，與本篇無關）[S42][S44]。截至 2026-08-27，上述條文為現行。

**gap（查不到官方文件，文章必須寫成要確認）：**

- **gap — atezolizumab 用於第三期 dMMR 結腸癌的輔助治療（ATOMIC 的做法）**：本輪逐份檢視健保署第 9 節自 113/6/1 至 115/8/1 的修訂對照表，**未見任何將免疫檢查點抑制劑用於早期／輔助性結腸癌的給付條文**。**文章一律寫成「這一項的給付條件要跟你的個管師或醫院醫務課確認」，不得宣稱有給付、也不得宣稱沒有給付。**
- **gap — nivolumab + ipilimumab 用於術前（NICHE-2 的做法）**：同上，未見條文。屬臨床試驗／未給付情境，寫成要確認。
- **gap — pembrolizumab 兩年上限之後怎麼辦**：條文寫「自初次處方用藥日起算 2 年」，但**續用、再治療（re-treatment）的條件本輪未查到官方說明**。寫成要確認。
- **gap — MMR/MSI 檢驗本身的健保給付**：屬 A4 主場，B 組未查證，**B4 不得提及檢驗費用或給付**。

---

# Sources（全 brief 單一編號序列）

> 期刊來源一律經 **Europe PMC REST（`search?query=EXT_ID:<PMID> AND SRC:MED`，`resultType=core&format=json`）** 查核；DOI 依 API 回傳值原樣抄寫（DOI 解析不分大小寫）。
> **連結一律使用下列 `https://europepmc.org/article/MED/<PMID>` 網址**（已逐條測到 HTTP 200）。出版社網站對自動抓取回 403，但人用瀏覽器可正常開啟。

## B1 可用

- **[S1] PASS** — Lu J, Xing J, Zang L, et al.; RELARC Study Group (2024). *Extent of Lymphadenectomy for Surgical Management of Right-Sided Colon Cancer: The Randomized Phase III RELARC Trial*. Journal of Clinical Oncology 42(33):3957–3966. PMID 39190853, doi 10.1200/jco.24.00393 — 目前唯一比較 CME 與 D2 的大型隨機試驗，主要終點 3 年 DFS 未達顯著差異，作者建議 D2 為常規術式。Route: Europe PMC REST (EXT_ID)
  URL：`https://europepmc.org/article/MED/39190853`
- **[S2] PASS** — Li K, Li H, Wu A, et al.; RELARC Study Group (2025). *Long-Term Survival on Extent of Lymphadenectomy for Right-Sided Colon Cancer: Five-Year Follow-up Results of a Randomized Controlled Trial (RELARC Trial)*. Annals of Surgery. PMID 40938728, doi 10.1097/sla.0000000000006941 — RELARC 五年追蹤，OS/CSS 仍無顯著差異，只在第三期與 pN2 次族群出現有利訊號。（API 未回傳 volume / issue / pageInfo，故不填。）Route: Europe PMC REST (EXT_ID)
  URL：`https://europepmc.org/article/MED/40938728`
- **[S3] PASS** — Bertelsen CA, Neuenschwander AU, Jansen JE, et al.; Danish Colorectal Cancer Group (2015). *Disease-free survival after complete mesocolic excision compared with conventional colon cancer surgery: a retrospective, population-based study*. The Lancet Oncology 16(2):161–168. PMID 25555421, doi 10.1016/s1470-2045(14)71168-4 — 支持 CME 的主要證據，但為回溯性族群研究、兩組來自不同醫院。Route: Europe PMC REST (EXT_ID)
  URL：`https://europepmc.org/article/MED/25555421`
- **[S4] PASS** — Clinical Outcomes of Surgical Therapy Study Group; Nelson H, Sargent DJ, Wieand HS, et al. (2004). *A comparison of laparoscopically assisted and open colectomy for colon cancer*. The New England Journal of Medicine 350(20):2050–2059. PMID 15141043, doi 10.1056/nejmoa032651 — COST 試驗主報告：3 年復發率與整體存活兩組相當。Route: Europe PMC REST (EXT_ID)
  URL：`https://europepmc.org/article/MED/15141043`
- **[S5] PASS** — Fleshman J, Sargent DJ, Green E, et al.; Clinical Outcomes of Surgical Therapy Study Group (2007). *Laparoscopic colectomy for cancer is not inferior to open surgery based on 5-year data from the COST Study Group trial*. Annals of Surgery 246(4):655–62; discussion 662–4. PMID 17893502, doi 10.1097/sla.0b013e318155a762 — COST 五年資料確認非劣性。Route: Europe PMC REST (EXT_ID)
  URL：`https://europepmc.org/article/MED/17893502`
- **[S6] PASS** — Colon Cancer Laparoscopic or Open Resection Study Group; Buunen M, Veldkamp R, Hop WC, et al. (2009). *Survival after laparoscopic surgery versus open surgery for colon cancer: long-term outcome of a randomised clinical trial*. The Lancet Oncology 10(1):44–52. PMID 19071061, doi 10.1016/s1470-2045(08)70310-3 — COLOR 長期結果；作者自承 95% CI 上限剛好超過 7% 非劣性界線。Route: Europe PMC REST (EXT_ID)
  URL：`https://europepmc.org/article/MED/19071061`
- **[S7] PASS** — Guillou PJ, Quirke P, Thorpe H, et al.; MRC CLASICC trial group (2005). *Short-term endpoints of conventional versus laparoscopic-assisted surgery in patients with colorectal cancer (MRC CLASICC trial): multicentre, randomised controlled trial*. Lancet 365(9472):1718–1726. PMID 15894098, doi 10.1016/s0140-6736(05)66545-2 — CLASICC 主報告與試驗設計（794 人、2:1 隨機分派）。Route: Europe PMC REST (EXT_ID)
  URL：`https://europepmc.org/article/MED/15894098`
- **[S8] PASS** — Green BL, Marshall HC, Collinson F, et al. (2013). *Long-term follow-up of the Medical Research Council CLASICC trial of conventional versus laparoscopically assisted resection in colorectal cancer*. The British Journal of Surgery 100(1):75–82. PMID 23132548, doi 10.1002/bjs.8945 — CLASICC 長期追蹤；術中轉開腹與較差存活相關（OS HR 2.28）。Route: Europe PMC REST (EXT_ID)
  URL：`https://europepmc.org/article/MED/23132548`
- **[S9] PASS** — Lacy AM, García-Valdecasas JC, Delgado S, et al. (2002). *Laparoscopy-assisted colectomy versus open colectomy for treatment of non-metastatic colon cancer: a randomised trial*. Lancet 359(9325):2224–2229. PMID 12103285, doi 10.1016/s0140-6736(02)09290-5 — Barcelona 單中心試驗主報告。Route: Europe PMC REST (EXT_ID)
  URL：`https://europepmc.org/article/MED/12103285`
- **[S10] PASS** — Lacy AM, Delgado S, Castells A, et al. (2008). *The long-term results of a randomized clinical trial of laparoscopy-assisted versus open surgery for colon cancer*. Annals of Surgery 248(1):1–7. PMID 18580199, doi 10.1097/sla.0b013e31816a9d65 — Barcelona 長期結果（219 人，單中心，結論比其他三個大型試驗樂觀）。Route: Europe PMC REST (EXT_ID)
  URL：`https://europepmc.org/article/MED/18580199`
- **[S11] PASS** — Chang GJ, Rodriguez-Bigas MA, Skibber JM, Moyer VA (2007). *Lymph node evaluation and survival after curative resection of colon cancer: systematic review*. Journal of the National Cancer Institute 99(6):433–441. PMID 17374833, doi 10.1093/jnci/djk092 — 17 篇研究、61,371 人；16/17 篇報告第二期檢出淋巴結越多存活越好。B1 與 B2 共用。Route: Europe PMC REST (EXT_ID)
  URL：`https://europepmc.org/article/MED/17374833`
- **[S12] PASS** — Le Voyer TE, Sigurdson ER, Hanlon AL, et al. (2003). *Colon cancer survival is associated with increasing number of lymph nodes analyzed: a secondary survey of intergroup trial INT-0089*. Journal of Clinical Oncology 21(15):2912–2919. PMID 12885809, doi 10.1200/jco.2003.05.062 — 第三期病人中，分析的淋巴結數目與存活的關聯。Route: Europe PMC REST (EXT_ID)
  URL：`https://europepmc.org/article/MED/12885809`
- **[S13] PASS** — Chin CC, Wang JY, Changchien CR, Huang WS, Tang R (2010). *Carcinoma obstruction of the proximal colon cancer and long-term prognosis—obstruction is a predictor of worse outcome in TNM stage II tumor*. International Journal of Colorectal Disease 25(7):817–822. PMID 20135321, doi 10.1007/s00384-010-0904-y — 台灣 1,492 人單一機構資料；阻塞在第二期是獨立預後不良因子、在第三期不是。B1 與 B2 共用。Route: Europe PMC REST (EXT_ID)
  URL：`https://europepmc.org/article/MED/20135321`

## B2 可用（另加 [S11]、[S13]）

- **[S14] PASS** — Quasar Collaborative Group; Gray R, Barnwell J, McConkey C, Hills RK, Williams NS, Kerr DJ (2007). *Adjuvant chemotherapy versus observation in patients with colorectal cancer: a randomised study*. Lancet 370(9604):2020–2029. PMID 18083404, doi 10.1016/s0140-6736(07)61866-2 — 第二期輔助化療絕對獲益的來源：3,239 人（91% 第二期），絕對存活改善 3.6%（95% CI 1.0–6.0）。Route: Europe PMC REST (EXT_ID)
  URL：`https://europepmc.org/article/MED/18083404`
- **[S15] PASS** — Matsuda C, Ishiguro M, Teramukai S, et al. (2018). *A randomised-controlled trial of 1-year adjuvant chemotherapy with oral tegafur-uracil versus surgery alone in stage II colon cancer: SACURA trial*. European Journal of Cancer 96:54–63. PMID 29677641, doi 10.1016/j.ejca.2018.03.009 — 1,982 名第二期病人，UFT 未證明優於單純手術（DFS HR 0.91，95% CI 0.75–1.10）；有風險因子者亦無獲益。Route: Europe PMC REST (EXT_ID)
  URL：`https://europepmc.org/article/MED/29677641`
- **[S16] PASS** — Ribic CM, Sargent DJ, Moore MJ, et al. (2003). *Tumor microsatellite-instability status as a predictor of benefit from fluorouracil-based adjuvant chemotherapy for colon cancer*. The New England Journal of Medicine 349(3):247–257. PMID 12867608, PMCID PMC3584639, doi 10.1056/nejmoa022289 — MSI-H 病人不從 5-FU 為基礎輔助化療得到好處的原始報告。Route: Europe PMC REST (EXT_ID)
  URL：`https://europepmc.org/article/MED/12867608`
- **[S17] PASS** — Sargent DJ, Marsoni S, Monges G, et al. (2010). *Defective mismatch repair as a predictive marker for lack of efficacy of fluorouracil-based adjuvant therapy in colon cancer*. Journal of Clinical Oncology 28(20):3219–3226. PMID 20498393, PMCID PMC2903323, doi 10.1200/jco.2009.27.1825 — dMMR 者 5-FU 無 DFS 好處（HR 1.10）；併入 1,027 人資料集後，第二期且 dMMR 者接受治療與較差 OS 相關（HR 2.95，95% CI 1.02–8.54）。**開放取用（PMC）。** Route: Europe PMC REST (EXT_ID)
  URL：`https://europepmc.org/article/MED/20498393`
- **[S18] PASS** — André T, de Gramont A, Vernerey D, et al. (2015). *Adjuvant Fluorouracil, Leucovorin, and Oxaliplatin in Stage II to III Colon Cancer: Updated 10-Year Survival and Outcomes According to BRAF Mutation and Mismatch Repair Status of the MOSAIC Study*. Journal of Clinical Oncology 33(35):4176–4187. PMID 26527776, doi 10.1200/jco.2015.63.4238 — 第二期加 oxaliplatin 的 10 年 OS：79.5% vs 78.4%，HR 1.00，P = 0.980。Route: Europe PMC REST (EXT_ID)
  URL：`https://europepmc.org/article/MED/26527776`
- **[S19] PASS** — Baxter NN, Kennedy EB, Bergsland E, et al. (2022). *Adjuvant Therapy for Stage II Colon Cancer: ASCO Guideline Update*. Journal of Clinical Oncology 40(8):892–910. PMID 34936379, doi 10.1200/jco.21.02538 — ASCO 現行第二期指引；T4「should be offered」、其他高風險特徵「may be offered」、dMMR/MSI「should not be routinely offered ACT」。ASCO 官方期刊平台頁面為 `https://ascopubs.org/doi/10.1200/JCO.21.02538`（人用瀏覽器可開，自動抓取回 403）。Route: Europe PMC REST (EXT_ID)
  URL（供文章使用）：`https://europepmc.org/article/MED/34936379`
- **[S20] PASS** — Argilés G, Tabernero J, Labianca R, et al.; ESMO Guidelines Committee (2020). *Localised colon cancer: ESMO Clinical Practice Guidelines for diagnosis, treatment and follow-up*. Annals of Oncology 31(10):1291–1305. PMID 32702383, doi 10.1016/j.annonc.2020.06.022 — ESMO 母版指引；第二期低／中／高風險三分層與各自建議條文。Route: Europe PMC REST (EXT_ID)
  ESMO 官方指引頁（已測 HTTP 200，供文章連結）：`https://www.esmo.org/guidelines/guidelines-by-topic/esmo-clinical-practice-guidelines-gastrointestinal-cancers/localised-colon-cancer`
  Europe PMC：`https://europepmc.org/article/MED/32702383`
- **[S21] PASS** — Pentheroudakis G, Argilés G, Arnold D, Smyth E, Ducreux M; ESMO Guidelines Committee (2026). *ESMO Clinical Practice Guideline Express Update on the adoption of physical exercise in patients with localised colon cancer*. ESMO Open 11(2):106019. PMID 41741110, PMCID PMC12947638, doi 10.1016/j.esmoop.2025.106019 — **開放取用**。用途有三：(一) 逐字確認 2020 年 Argilés CPG 仍為母版指引（原文：「This Express Update provides new recommendations for the following ESMO Clinical Practice Guideline (CPG): Localised colon cancer…」）；(二) 第二期流程圖附註 a「For pT4 MSI: pT4 is a major risk factor but adjuvant ChT benefit in the presence of MSI is uncertain.」；(三) 第三期流程圖附註 a 對 IDEA 風險分層的警告。**⚠️ 這篇的主題（運動介入與 CHALLENGE 試驗數據）歸 D4，B 組不得引用其運動相關數字。** Route: Europe PMC REST (EXT_ID) + fullTextXML (PMC12947638)
  URL：`https://europepmc.org/article/MED/41741110`
- **[S22] PASS** — National Comprehensive Cancer Network (2026). *NCCN Guidelines for Patients®: Colon Cancer, 2026*（基於 NCCN Guidelines® for Colon Cancer, **Version 2.2026 — April 7, 2026**）。官方 PDF，49 頁，已下載並逐頁比對版本字串。用途：確認 NCCN 現行版本號與日期；引用其第二期敘述（「Your doctor may (or may not) recommend chemotherapy…」）與第三期 dMMR 加 atezolizumab 的敘述。**這是病人版，不是專業版演算法；不得據此逐條列出 NCCN 的高風險特徵清單。** Route: 官方 nccn.org PDF 直接下載（HTTP 200）
  URL：`https://www.nccn.org/patients/guidelines/content/PDF/colon-patient.pdf`

## B3 可用（另加 [S19]、[S21]）

- **[S23] PASS** — Grothey A, Sobrero AF, Shields AF, et al. (2018). *Duration of Adjuvant Chemotherapy for Stage III Colon Cancer*. The New England Journal of Medicine 378(13):1177–1188. PMID 29590544, PMCID PMC6426127, doi 10.1056/nejmoa1713709 — IDEA 主要終點：整體非劣性未確認（HR 1.07，95% CI 1.00–1.15）；CAPOX vs FOLFOX 差異；低風險 T1–3N1 與高風險 T4/N2 的分層數字。Route: Europe PMC REST (EXT_ID)
  URL：`https://europepmc.org/article/MED/29590544`
- **[S24] PASS** — André T, Meyerhardt J, Iveson T, et al. (2020). *Effect of duration of adjuvant chemotherapy for patients with stage III colon cancer (IDEA collaboration): final results from a prospective, pooled analysis of six randomised, phase 3 trials*. The Lancet Oncology 21(12):1620–1629. PMID 33271092, PMCID PMC7786835, doi 10.1016/s1470-2045(20)30527-1 — IDEA 最終整體存活：5 年 OS 82.4% vs 82.8%（HR 1.02，95% CI 0.95–1.11），非劣性未確認；CAPOX / FOLFOX 分層；作者對 0.4% 絕對差距的解讀原句。Route: Europe PMC REST (EXT_ID) + DOI
  URL：`https://europepmc.org/article/MED/33271092`
- **[S25] PASS** — Iveson TJ, Kerr RS, Saunders MP, et al. (2018). *3 versus 6 months of adjuvant oxaliplatin-fluoropyrimidine combination therapy for colorectal cancer (SCOT): an international, randomised, phase 3, non-inferiority trial*. The Lancet Oncology 19(4):562–578. PMID 29611518, PMCID PMC5883334, doi 10.1016/s1470-2045(18)30093-7 — IDEA 六個組成試驗之一，**開放取用**。Route: Europe PMC REST (EXT_ID)
  URL：`https://europepmc.org/article/MED/29611518`
- **[S26] PASS** — Biagi JJ, Raphael MJ, Mackillop WJ, Kong W, King WD, Booth CM (2011). *Association between time to initiation of adjuvant chemotherapy and survival in colorectal cancer: a systematic review and meta-analysis*. JAMA 305(22):2335–2342. PMID 21642686, doi 10.1001/jama.2011.749 — 10 項研究、15,410 人；每延遲 4 週開始，OS HR 1.14（95% CI 1.10–1.17）、DFS HR 1.14（1.10–1.18）。**10 項中 9 項為世代／族群研究。** Route: Europe PMC REST (EXT_ID)
  URL：`https://europepmc.org/article/MED/21642686`
- **[S27] PASS** — Gallois C, Shi Q, Meyers JP, et al. (2023). *Prognostic Impact of Early Treatment and Oxaliplatin Discontinuation in Patients With Stage III Colon Cancer: An ACCENT/IDEA Pooled Analysis of 11 Adjuvant Trials*. Journal of Clinical Oncology 41(4):803–815. PMID 36306483, doi 10.1200/jco.21.02726 — 提早中止全部治療（ETD，10,447 人、20.9%）與較差 DFS（HR 1.61）、OS（HR 1.73）相關；只停 oxaliplatin（EOD，7,243 人、18.8%）則無顯著相關；但接受不到 50% oxaliplatin 療程者結果較差。Route: Europe PMC REST (DOI)
  URL：`https://europepmc.org/article/MED/36306483`

## B4 可用

- **[S28] PASS** — Venderbosch S, Nagtegaal ID, Maughan TS, et al. (2014). *Mismatch repair status and BRAF mutation status in metastatic colorectal cancer patients: a pooled analysis of the CAIRO, CAIRO2, COIN, and FOCUS studies*. Clinical Cancer Research 20(20):5322–5330. PMID 25139339, PMCID PMC4201568, doi 10.1158/1078-0432.ccr-14-0332 — **轉移性 dMMR 盛行率 5.0%（153/3,063）**，即紅線 2 的「每 20 人一個」；同時報告 dMMR 在轉移性情境預後較差。Route: Europe PMC REST (EXT_ID)
  URL：`https://europepmc.org/article/MED/25139339`
- **[S29] PASS** — André T, Shiu KK, Kim TW, et al. (2020). *Pembrolizumab in Microsatellite-Instability-High Advanced Colorectal Cancer*. The New England Journal of Medicine 383(23):2207–2218. PMID 33264544, doi 10.1056/nejmoa2017699 — KEYNOTE-177 首次報告：中位 PFS 16.5 vs 8.2 個月（HR 0.60，95% CI 0.45–0.80）；OS 當時尚未成熟；治療相關第 3 級以上不良事件 22% vs 66%。Route: Europe PMC REST (EXT_ID)
  URL：`https://europepmc.org/article/MED/33264544`
- **[S30] PASS** — André T, Shiu KK, Kim TW, et al. (2025). *Pembrolizumab versus chemotherapy in microsatellite instability-high or mismatch repair-deficient metastatic colorectal cancer: 5-year follow-up from the randomized phase III KEYNOTE-177 study*. Annals of Oncology 36(3):277–284. PMID 39631622, doi 10.1016/j.annonc.2024.11.012 — **取代 2020 年的 OS 空缺**：中位 OS 77.5 vs 36.7 個月（HR 0.73，95% CI 0.53–0.99）、5 年 OS 54.8% vs 44.2%、**實際跨組率 62%**、不良事件第 3–5 級 22% vs 67%。Route: Europe PMC REST (EXT_ID)
  URL：`https://europepmc.org/article/MED/39631622`
- **[S31] PASS** — Chalabi M, Verschoor YL, Tan PB, et al. (2024). *Neoadjuvant Immunotherapy in Locally Advanced Mismatch Repair-Deficient Colon Cancer*. The New England Journal of Medicine 390(21):1949–1958. PMID 38838311, doi 10.1056/nejmoa2400634 — NICHE-2：115 人單臂第二期；98% 如期手術；病理反應 109/111（98%）、病理完全反應 75（68%）；第 3–4 級 irAE 5 人（4%）；中位追蹤 26 個月無人復發。**單臂、無對照組、3 年 DFS 尚未正式發表。** Route: Europe PMC REST (EXT_ID)
  URL：`https://europepmc.org/article/MED/38838311`
- **[S32] PASS** — Sinicrope FA, Ou FS, Arnold D, et al. (2026). *Atezolizumab plus FOLFOX for Stage III Mismatch Repair-Deficient Colon Cancer*. The New England Journal of Medicine 394(12):1155–1166. PMID 41880612, PMCID PMC13020640, doi 10.1056/nejmoa2507874. **開放取用。** — ATOMIC 第三期隨機試驗：712 人，3 年 DFS 86.3% vs 76.2%（HR 0.50，95% CI 0.35–0.73，P < 0.001）；第 3–4 級不良事件 84.1% vs 71.9%。**這是 2026 年最重要的變動，必須寫進 B4。** Route: Europe PMC REST (EXT_ID)
  URL：`https://europepmc.org/article/MED/41880612`
- **[S33] PASS** — Le DT, Uram JN, Wang H, et al. (2015). *PD-1 Blockade in Tumors with Mismatch-Repair Deficiency*. The New England Journal of Medicine 372(26):2509–2520. PMID 26028255, PMCID PMC4481136, doi 10.1056/nejmoa1500596 — pMMR 大腸直腸癌免疫相關客觀反應率 **0%（0/18）**；dMMR 40%（4/10）。Route: Europe PMC REST (EXT_ID)
  URL：`https://europepmc.org/article/MED/26028255`
- **[S34] PASS** — Eng C, Kim TW, Bendell J, et al.; IMblaze370 Investigators (2019). *Atezolizumab with or without cobimetinib versus regorafenib in previously treated metastatic colorectal cancer (IMblaze370): a multicentre, open-label, phase 3, randomised, controlled trial*. The Lancet Oncology 20(6):849–861. PMID 31003911, doi 10.1016/s1470-2045(19)30027-0 — **MSS 轉移性大腸直腸癌最硬的陰性隨機證據**：atezolizumab 單用對 regorafenib 的 OS HR 1.19（95% CI 0.83–1.71，P = 0.34），主要終點未達成；MSI-H 收案上限 5%。Route: Europe PMC REST (EXT_ID)
  URL：`https://europepmc.org/article/MED/31003911`
- **[S35] PASS（限定用途）** — Tan PB, Verschoor YL, van den Berg JG, et al. (2025). *Neoadjuvant immunotherapy in mismatch-repair-proficient colon cancers*. Nature 648(8094):726–735. PMID 41115454, PMCID PMC12711568, doi 10.1038/s41586-025-09679-4. **開放取用。** — NICHE 的 pMMR 世代：31 名**早期**pMMR 結腸癌病人接受術前 nivolumab + ipilimumab，反應率 26%，6 人達主要病理反應。**只可用來說明「必須寫全限定語：轉移性、單用」，不可用來暗示 MSS 病人有免疫治療選項。** Route: Europe PMC REST (EXT_ID)
  URL：`https://europepmc.org/article/MED/41115454`
- **[S36] PASS** — Wang DY, Salem JE, Cohen JV, et al. (2018). *Fatal Toxic Effects Associated With Immune Checkpoint Inhibitors: A Systematic Review and Meta-analysis*. JAMA Oncology 4(12):1721–1728. PMID 30242316, PMCID PMC6440712, doi 10.1001/jamaoncol.2018.3923 — 112 個試驗、19,217 人：毒性相關死亡率 anti-PD-1 0.36%、anti-PD-L1 0.38%、anti-CTLA-4 1.08%、併用 1.23%；心肌炎致死比例最高（39.7%）；症狀到死亡中位 32 天。Route: Europe PMC REST (EXT_ID)
  URL：`https://europepmc.org/article/MED/30242316`
- **[S37] PASS（用途受限）** — Barroso-Sousa R, Barry WT, Garrido-Castro AC, et al. (2018). *Incidence of Endocrine Dysfunction Following the Use of Different Immune Checkpoint Inhibitor Regimens: A Systematic Review and Meta-analysis*. JAMA Oncology 4(2):173–182. PMID 28973656, PMCID PMC5838579, doi 10.1001/jamaoncol.2017.3064 — 38 個隨機試驗、7,551 人。**只提供勝算比（OR），不提供可直接引用的合併絕對百分比；原發性腎上腺功能不全與胰島素缺乏型糖尿病因事件數太少未做推論。** 用來說明「哪一類藥比較容易出現哪一種內分泌損傷」，**不得由此推出百分比。** Route: Europe PMC REST (EXT_ID)
  URL：`https://europepmc.org/article/MED/28973656`
- **[S38] PASS** — Alharbi TH, Alzahrani HA, Alromaihi RA, Alzahrani S, Alromaihi M, Kamrul-Hasan ABM (2026). *Immune checkpoint inhibitor-induced type 1 diabetes mellitus: incidence, risk factors, and prognostic implications - a systematic review and meta-analysis*. Diabetes Research and Clinical Practice 239:113439. PMID 42456777, doi 10.1016/j.diabres.2026.113439 — 10 項研究、65,925 人：ICI 引起的第 1 型糖尿病合併發生率 **0.58%（95% CI 0.35–0.92%）**，其中約 **37% 以糖尿病酮酸中毒表現**；雙免疫藥物併用風險較高。Route: Europe PMC REST (EXT_ID)
  URL：`https://europepmc.org/article/MED/42456777`
- **[S39] PASS** — Nguyen H, Shah K, Waguespack SG, et al. (2021). *Immune checkpoint inhibitor related hypophysitis: diagnostic criteria and recovery patterns*. Endocrine-Related Cancer 28(7):419–431. PMID 33890870, PMCID PMC8183642, doi 10.1530/erc-20-0513. **開放取用。** — 83 人（62 人確診）、中位追蹤 1.75 年：**甲狀腺軸恢復 24%、性腺軸 58%、腎上腺軸 0%**；高劑量類固醇或停藥與恢復無關。**「終身」這個詞的出處。** Route: Europe PMC REST (EXT_ID)
  URL：`https://europepmc.org/article/MED/33890870`
- **[S40b] PASS（背景用）** — Schneider BJ, Naidoo J, Santomasso BD, et al. (2021). *Management of Immune-Related Adverse Events in Patients Treated With Immune Checkpoint Inhibitor Therapy: ASCO Guideline Update*. Journal of Clinical Oncology 39(36):4073–4126. PMID 34724392, doi 10.1200/jco.21.01440 — irAE 處理的現行 ASCO 指引；本輪於 Europe PMC 檢索 2024–2026 未見更新版。Route: Europe PMC REST (EXT_ID)
  URL：`https://europepmc.org/article/MED/34724392`

## 台灣官方文件

- **[S40] PASS** — 衛生福利部中央健康保險署。《全民健康保險藥品給付規定》**9.10. Oxaliplatin**（條文修訂沿革列至 111/11/1）。官方 PDF，已下載並逐字擷取。逐字內容：「1.和 5-FU 和 folinic acid 併用（1）治療轉移性結腸直腸癌，惟若再加用 irinotecan (如 Campto)則不予給付。(91/10/1)（2）作為第三期結腸癌(Duke's C) 原發腫瘤完全切除手術後的輔助療法。(98/2/1)」Route: 健保署藥品給付規定查詢系統官方 PDF 端點（HTTP 200）
  URL：`https://info.nhi.gov.tw/api/INAE3000/INAE3000S01/getPDF?DurgFileName=9.10._20221101.pdf`
- **[S41] PASS** — 衛生福利部中央健康保險署。《「藥品給付規定」修訂對照表　第 9 節　抗癌瘤藥物 Antineoplastics drugs（113 年 6 月 1 日生效）》。官方 PDF，已下載並逐字擷取。用途：同時取得 **9.10 Oxaliplatin** 與 **9.17 Capecitabine** 的完整條文（含 9.17 第 4 項「第三期結腸癌患者手術後的輔助性療法，以八個療程為限。（96/9/1）」），且修訂後／原條文兩欄一致，證明結腸癌輔助條文未被該次修訂變動。Route: nhi.gov.tw 官方 PDF（HTTP 200）
  URL：`https://www.nhi.gov.tw/ch/dl-69883-b86f808f024b4f51b803adf5ea4e5a71-1.pdf`
- **[S42] PASS** — 衛生福利部中央健康保險署。《「藥品給付規定」修訂對照表　第 9 節　抗癌瘤藥物（自 115 年 8 月 1 日生效）》。官方 PDF，已下載並全文比對：**內容為 9.138 Aumolertinib 等項目，未涉及結腸／大腸／直腸癌**。用途：確認截至 2026-08-27 的最新一次第 9 節修訂未變動本 brief 引用的三條結腸癌條文。Route: nhi.gov.tw 官方 PDF（HTTP 200）
  URL：`https://www.nhi.gov.tw/ch/dl-100554-4be16d1317d547a8a2db6ccec9ab6596-1.pdf`
- **[S43] PASS** — 衛生福利部中央健康保險署。《「藥品給付規定」修訂對照表　第 9 節　抗癌瘤藥物（自 114 年 6 月 1 日生效）》。官方 PDF，已下載並逐字擷取。逐字內容：「9.69.免疫檢查點抑制劑…(11)大腸直腸癌：限 pembrolizumab 做為無法切除或轉移性高微衛星不穩定性(MSI-H)或錯誤配對修復功能不足性(dMMR)大腸直腸癌(CRC)之成年病人第一線治療。(114/6/1)」；並含「(5) 給付時程期限：自初次處方用藥日起算 2 年」「(7)每次申請以 12 週為限」及生物標記對照表中「大腸直腸癌(單用)…不需檢附報告」。Route: nhi.gov.tw 官方 PDF（HTTP 200）
  URL：`https://www.nhi.gov.tw/ch/dl-84779-755e9fb705df4d639017935b1cc26fc5-1.pdf`
- **[S44] PASS（時效性佐證，不必出現在文章參考清單）** — 衛生福利部中央健康保險署，第 9 節修訂對照表 114/2/1、114/7/1、114/8/1、114/10/1、115/1/1、115/2/1 各版官方 PDF。已逐份下載並以「結腸／大腸／直腸／Oxaliplatin／Capecitabine」比對：僅 115/2/1 版涉及大腸直腸癌（9.66 trifluridine/tipiracil，與 B 組四篇無關），其餘各版**均未變動** 9.10、9.17、9.69 的結腸癌條文。Route: nhi.gov.tw 官方 PDF（皆 HTTP 200）
  代表性 URL（115/2/1）：`https://www.nhi.gov.tw/ch/dl-95585-dd98d905607c4c8a8c03a2dd9a36a487-1.pdf`

## FAIL（保留，不得引用）

- **[S45] FAIL** — NCCN Clinical Practice Guidelines in Oncology: Colon Cancer（專業版演算法，含完整高風險特徵條列）。官方登陸頁 `https://www.nccn.org/guidelines/guidelines-detail?category=1&id=1428` 以 curl 追蹤重導向可得 HTTP 200，但 WebFetch 取回 403 / 無實質內容；PDF 需註冊登入。**因此未能取得 NCCN 對「高風險第二期」的官方條列原文。** 版本號與日期改由 NCCN 官方公開的病人版 PDF 確認（見 [S22]）。**寫稿人不得逐條列出 NCCN 的高風險特徵，也不得宣稱 NCCN 與 ESMO / ASCO 在某一項上相同或不同。**
- **[S46] FAIL** — NICHE-2 的 3 年無病存活（該試驗的第二個主要終點）正式論文。以 Europe PMC 檢索 `AUTH:"Chalabi M" AND (PUB_YEAR:2025 OR PUB_YEAR:2026) AND TITLE:"colon"` 僅得一則 Nature Medicine 新聞短文（PMID 41495400）與 NICHE pMMR 世代論文（[S35]），**未找到 NICHE-2 3 年 DFS 的正式發表**。**文章不得宣稱 NICHE-2 已證明長期無復發。**
- **[S47] FAIL** — ESMO Express Update 官方登陸頁 `https://www.esmo.org/guidelines/express-update-localised-colon-cancer`（HTTP 200）與 ESMO 指引主題頁：兩者皆為前端渲染，WebFetch 取回的內容只有導覽列與頁尾，**無法直接讀出版本日期**。所需資訊改由 ESMO Open 全文（[S21]，經 Europe PMC fullTextXML 取得）確認，該全文逐字聲明所更新的母版 CPG 為 2020 年 Argilés 版。
- **[S48] FAIL** — ASCO 官方指引登陸頁：`https://www.asco.org/guidelines/GUIDELINEASCO168761`、`https://www.asco.org/practice-patients/guidelines/gastrointestinal-cancer`、`https://society.asco.org/practice-patients/guidelines/gastrointestinal-cancer` 三個候選網址分別回 403 / 404 / 連線失敗，**未能從 ASCO 官網確認 2022 年第二期指引的「現行／已改版」狀態**。指引內容本身已由 JCO 正式論文查證（[S19]）。**文章可以寫「2022 年 ASCO 的第二期結腸癌輔助治療指引」，不得寫「最新版」或「現行版」。**
- **[S49] FAIL** — 憑記憶輸入的下列 PMID 經 Europe PMC 查核後**均為完全不同的文章**，已全部作廢，未進入本 brief：17954709（實為 2007 年 ASCO 乳癌腫瘤標記指引）、12049860（實為 fondaparinux 髖關節置換試驗）、29580319（實為肝臟與胰臟胚胎發育綜述）。**保留此條作為「絕不從記憶寫書目資料」的證據。**
- **[S50] FAIL** — 「IDEA 整體存活結果（Sobrero 等，JCO 2022）」此一憑記憶的引用**在 Europe PMC 查無此文**。IDEA 的最終整體存活結果實際發表於 Lancet Oncology 2020（見 [S24]）。**不得引用任何 JCO 2022 版的 IDEA OS 論文。**
- **[S51] FAIL** — 台灣健保對 CME/D3、腹腔鏡與開腹結腸切除、機械手臂手術的**手術給付／自付差額**：健保署「藥品給付規定」不涵蓋手術術式，本輪未找到對應的官方條文或公告。**文章一律寫成要向個管師或醫務課確認。**
- **[S52] FAIL** — 台灣健保對**第二期**結腸癌輔助化療（單方 5-FU/leucovorin 注射劑、UFUR 等）的完整給付條文：本輪僅完整取得 9.10 與 9.17 兩項，未逐條還原其餘 fluoropyrimidine 品項。**不得由「9.10 與 9.17 寫的是第三期」推論「第二期一律自費」。**
- **[S53] FAIL** — 台灣健保對 **atezolizumab 用於第三期 dMMR 結腸癌輔助治療**（ATOMIC 的做法）、以及 **nivolumab + ipilimumab 術前使用**（NICHE-2 的做法）的給付條文：逐份比對健保署第 9 節 113/6/1 至 115/8/1 各版修訂對照表，**未見任何早期／輔助性結腸癌的免疫檢查點抑制劑條文**。因無法確認是「明文不給付」還是「條文中另有他處規範」，**一律寫成 gap：要跟個管師或醫務課確認，不得宣稱有給付、也不得宣稱沒給付。**
- **[S54] FAIL** — 台灣健保對 **pembrolizumab 滿 2 年後續用／再治療（re-treatment）** 的條件：條文只寫「自初次處方用藥日起算 2 年」，未找到後續處理的官方說明。**寫成要確認。**
