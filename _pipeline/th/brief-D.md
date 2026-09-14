# D 組查證 brief（D1 th-tsh／D2 th-followup／D3 th-recurrence／D4 th-rai-refractory／D5 th-ebrt）

查證日：2026-09-14
主要路徑：Europe PMC REST（search／fullTextXML）、`pmc.ncbi.nlm.nih.gov` 全文 HTML、clinicaltrials.gov API v2、law.moj.gov.tw（全民健康保險藥物給付項目及支付標準＋其附件 PDF）、data.fda.gov.tw 開放資料（西藥許可證）。**全程未引用 NCCN。**

已由 A／B／C 組確立、本組沿用未重推的事：ATA 2025 為現行版；四級復發風險（low <10%／low-intermediate 10–15%／intermediate-high ≥16–30%／high >30%）；GRADE＋Good Practice Statement 併行；ATA 2025 內文參考文獻編號有錯置；ATA 2025 已把甲狀腺結節移出範圍。

---

## ⚠ 與 SPEC 假設不同形狀的事

### ⚠D-1　ATA 2025 已經把「TSH 目標值的數字區間」整個拿掉了——SPEC 與一般記憶中的 0.1／0.5／2.0 三段式是 2015 版
- **SPEC 怎麼假設**：SPEC §四 D1 寫「TSH 抑制的目標依風險組而變」，暗示現行指引仍給一組可對照的數字。
- **實際是什麼**：ATA 2025 的 TSH 目標只剩下 Table 9 最右欄的**四個文字格**，沒有任何數字：Excellent →「TSH within normal reference range」；Indeterminate →「TSH within normal reference range」（附註 b：「Data on optimal TSH target range are inconclusive.」）；Biochemically incomplete →「TSH below normal reference range」（附註 c）；Structurally incomplete →「TSH below normal reference range」（附註 c）。附註 c 逐字：「Data on optimal TSH target range are inconclusive and/or conflicting. If there is progression of residual disease or development of new recurrence, targeting a TSH below normal reference range may be reasonable. However, comorbidities such as atrial fibrillation and osteoporosis should be factored into the decision making process.」
  且 Table 9 的 TSH 目標欄是**依「治療反應分類」給的，不是依「初始復發風險組」給的**——這與 SPEC 的措辭（依風險組而變）形狀不同。ATA 2025 Recommendation 45 只說「recognizing that patients with high-risk disease may be more likely to benefit from a TSH in the subnormal range than those with low-risk disease」。
- **對照組（2015 版，已被取代）**：ATA 2015 Recommendation 70 有明確數字：(A) structural incomplete → TSH <0.1 mU/L；(B) biochemical incomplete → 0.1–0.5 mU/L；(C) 高風險但 excellent／indeterminate → 0.1–0.5 mU/L 維持至多 5 年；(D)(E) excellent／indeterminate → 0.5–2 mU/L。
- **證據**：[D-S1] ATA 2025 全文 Table 9 與 Recommendation 45／46；[D-S3] ATA 2015 全文 Recommendation 70。
- **建議怎麼裁決**：**D1 全篇禁止出現 0.1／0.5／2.0 這三個數字作為「現行目標」。** 只能寫「現在的指引不給你一個可以對號入座的數字，只給四格文字」，並把 2015→2025 的這個改變本身寫成文章的骨幹。若要提 2015 的數字，必須明寫「這是舊版、已被取代」。

### ⚠D-2　ATA 2025 明文「不建議」低風險與中風險病人長期抑制——這是這一篇真正的新聞
- **實際是什麼**：Recommendation 46A 逐字：「Long-term TSH suppression is not suggested for patients with low- or intermediate-risk disease who have no evidence of biochemical or structural recurrence. (Conditional recommendation, Low certainty evidence)」；46B 逐字：「Risks versus benefits of TSH suppression and TSH goals should be re-evaluated over time. (Good Practice Statement)」。
- **注意用詞**：46A 寫的是 low- or **intermediate**-risk，用的是**舊的三級講法**，不是 ATA 2025 自己新訂的四級（low／low-intermediate／intermediate-high／high）。**指引內部用詞不一致**，寫作時不可以自行把它翻成四級中的哪兩格。
- **建議怎麼裁決**：D1 引用 46A 時逐字抄英文並加註「原文用的是 low-／intermediate-risk 這種舊講法，與同一份指引的四級分層沒有對應說明」。

### ⚠D-3　「低風險抑制 TSH 有沒有好處」的隨機證據：有，只有一個，而且是陰性的非劣性試驗
- **實際是什麼**：唯一的 RCT 是 Sugitani & Fujimoto 2010（[D-S4]），單中心開放標籤、**用 AMES 風險分類而非 ATA 分層**、218 vs 215 人、乳突癌、終點是 disease-free survival。結論：不抑制組的 DFS 不劣於抑制組（HR 的 95% CI 0.85–1.27，落在預設的 2.12 非劣性界限內）。**摘要沒有給 HR 點估計值，只給 CI。**
- 另：2024 年的系統性回顧與統合分析（[D-S6] Gubbi 2024，限中／高風險）在 PFS／DFS／RLFS 合成終點 HR 0.75（95% CI 0.48–1.17）、DSS／OS 合成終點 HR 0.69（95% CI 0.31–1.52），皆不顯著；不良事件合成終點 HR 1.82（95% CI 1.30–2.55）顯著較高。
- **建議怎麼裁決**：D1 可以明寫「隨機試驗只有一個，而且它問的是『不抑制會不會比較差』，答案是沒有比較差」。**不可以寫成「已證實抑制無效」**（非劣性試驗不能證明無效），也不可以寫成「指引建議大家都抑制」。

### ⚠D-4　ATA 2025 內文對原始論文的轉述有可查證的算術錯誤——本組實測到三處
- **(a) 參考文獻 1194 指錯篇**：ATA 2025 用 ref 1194 支撐 SELECT 試驗的敘述，但參考文獻表第 1194 條是「Schlumberger M, Tahara M, Wirth LJ. Lenvatinib in radioiodine-refractory thyroid cancer. N Engl J Med 2015;372(19):1868」——那是 NEJM 的**通信／回覆**（單頁 1868），不是 SELECT 原著（NEJM 2015;372(7):621–630，PMID 25671254）。
- **(b) Recommendation 53 內文轉述 Hirsch 2018 的數字互相矛盾**：ATA 寫「Three of 47 (17.6%) patients had resolution of their nodes」——3/47 = 6.4%，不是 17.6%；接著寫「Of the remaining 44 patients, 10 (22.7%) … 2 (4.5%) … and 26 (59.0%)」——10+2+26 = 38，不是 44。原著（[D-S29]）的對應敘述是「At 1 to 2 years after RAI retreatment, 10 of the 41 patients with sufficient data had structural progression, 5 resolution/shrinkage, and 26 stable disease」。
- **(c) Recommendation 62 內文把 DECISION 的「serious adverse events」寫成「Grade 3 or higher serious adverse events」**：原著（[D-S30]）逐字是「Serious AEs occurred in 77 (37·2%) patients receiving sorafenib and 55 (26·3%) patients receiving placebo」，並未限定 grade ≥3。
- **建議怎麼裁決**：沿用既有裁決並加強——**D 組五篇一律不得透過 ATA 2025 轉引原始論文的任何數字**；本 brief 已把每一個要用的數字都回到原文重抄，未能回到原文的已個別標示「ATA 轉述、未獨立驗證」，那些數字**寫作組不得使用**。

### ⚠D-5　多個關鍵試驗的信賴區間不是 95%——照抄會出錯
- SELECT（[D-S31]）的 PFS HR 0.21 是 **99% CI 0.14–0.31**（NEJM 摘要逐字「hazard ratio for progression or death, 0.21; 99% confidence interval, 0.14 to 0.31」）。ATA 2025 寫成「HR 0.21 [CI 0.14–0.31]」沒有標明是 99%。
- COSMIC-311（[D-S32]）主要分析的 ORR 是 **99% CI**（10/67，15%，99% CI 5.8–29.3），PFS HR 0.22 是 **96% CI 0.13–0.36**；延長追蹤版（[D-S33]）的 median PFS 11.0 個月是 **96% CI 7.4–13.8**，HR 0.22 是 **96% CI 0.15–0.32**。
- **建議怎麼裁決**：D4 若寫 CI，必須連同「99%／96%」一起寫，或乾脆不寫 CI 只寫點估計值與樣本數。**不得預設是 95%。**

### ⚠D-6　COSMIC-311 的「中位 PFS 未達到」已經過期了——ATA 2025 只引了期中分析
- **實際是什麼**：ATA 2025 Recommendation 66 內文寫「median progression-free survival was not reached [CI 5.7 months—not estimable] compared with … 1.9 months」，那是 2021 年 Lancet Oncol 的期中分析（187 人、中位追蹤 6.2 個月）。2022 年 Cancer 的延長追蹤（[D-S33]，258 人隨機、中位追蹤 10.1 個月）已讀出**中位 PFS 11.0 個月 vs 1.9 個月，HR 0.22（96% CI 0.15–0.32）**，ORR 11.0%（95% CI 6.9–16.9）。
- **建議怎麼裁決**：D4 用 2022 年的延長追蹤數字，並註明期中分析的 ORR 未達預設顯著門檻（α=0.01）。

### ⚠D-7　BRAF V600E 的第三期試驗已經讀出來了，比 ATA 2025 晚
- **SPEC／ATA 假設**：ATA 2025 寫「a global randomized, placebo-controlled phase III study … is underway (NCT04940052)」。
- **實際是什麼**：已於 Lancet Oncol 2026;27(8):994–1003 發表（[D-S39]，PMID 42442381）。153 人（dabrafenib+trametinib 101／安慰劑 52），中位追蹤 17.4 個月，**中位 PFS 12.8 個月（95% CI 10.2–21.2）vs 3.7 個月（2.3–7.5），分層 HR 0.38（95% CI 0.25–0.57）**；ORR 57%（58/101）vs 4%（2/52）；**OS 期中分析未達顯著（分層 HR 0.66，95% CI 0.36–1.19；p=0.083）**。受試者 86% 為亞洲人。
- **建議怎麼裁決**：D4 必須寫這個新結果，並明講「這是二線的證據，不是一線」（該試驗納入的是 previously treated 病人）。

### ⚠D-8　任務書要求的 LIBRETTO-531 是**髓質癌**試驗，不屬於 D4 的分化型甲狀腺癌範圍
- **實際是什麼**：LIBRETTO-531（[D-S36]，NEJM 2023;389(20):1851–1861）比較的是 selpercatinib vs cabozantinib／vandetanib，對象是 **RET 突變型髓質癌（MTC）**、第一線、291 人。分化型甲狀腺癌（RET **融合**）的 selpercatinib 證據是 LIBRETTO-001 的第 3 世代（[D-S34]，19 人）。
- **建議怎麼裁決**：D4 **不得**把 LIBRETTO-531 的 PFS 數字寫在分化型甲狀腺癌段落。髓質癌那一段屬於 E1（th-mtc）。若 D4 要提，只能寫一句「髓質癌那邊是另一個試驗、另一種基因變化（點突變而非融合），請看那一篇」。

### ⚠D-9　台灣端：食藥署**查得到**（走 data.fda.gov.tw 開放資料），健保藥品給付規定**也查得到全文**——任務書預設的「查詢管道不可用」在本次不成立
- **任務書怎麼假設**：「TFDA's info.fda.gov.tw may be unreachable from here (502)」。
- **實際是什麼**：`info.fda.gov.tw` 確實被代理端以 502 阻擋（與 A 組相同），但 **`data.fda.gov.tw` 的開放資料集（西藥許可證，InfoId=36／37，ZIP→JSON）可用**，且欄位含「適應症」全文。健保端 `www.nhi.gov.tw` 被 Cloudflare 擋（403）、`data.nhi.gov.tw` 502，但**全國法規資料庫 `law.moj.gov.tw` 的「全民健康保險藥物給付項目及支付標準」（pcode=L0060035）附有「附件六　藥品給付規定.PDF」與「附件二　藥品給付項目暨支付標準表.PDF」，兩份都下載成功並轉成全文可搜**。
- **查到的結果**（詳見 [D-S55]～[D-S57]）：
  - 藥證有甲狀腺適應症：lenvatinib、sorafenib、selpercatinib、cabozantinib、pralsetinib；larotrectinib／entrectinib 是不分癌別的 NTRK 適應症。
  - 健保**藥品給付規定**有列項：sorafenib（9.34 第 3 項）、lenvatinib（9.63 第 1 項）、cabozantinib（9.74 第 2 項，114/8/1 起）。
  - 健保**藥品給付規定 zero hits**：selpercatinib、pralsetinib、larotrectinib、entrectinib、dabrafenib、trametinib；全文亦查無「NTRK」「基因融合」「不分癌別」等字串。
  - 健保**藥品給付項目暨支付標準表**（附件二）**有收載**：Lenvima 4/10mg、Nexavar 與數家 sorafenib、Cabometyx 20/40/60mg、VITRAKVI（larotrectinib）四品項、Rozlytrek 200mg；**查無**：RETSEVMO（selpercatinib）、GAVRETO（pralsetinib）。
- **建議怎麼裁決**：這是 SPEC §六 第 4 點（「台灣健保對 lenvatinib／sorafenib／selpercatinib 用於甲狀腺癌的給付狀態」）的正式答案，請寫進 §九。**注意兩件事**：(1) 藥證 ≠ 健保給付，兩者必須分開寫；(2) 「在藥品給付規定查無列項」不等於「不給付」——附件二證明 larotrectinib／entrectinib 有收載卻無給付規定條文，所以**對 selpercatinib／pralsetinib 只能寫「附件二與附件六都查無列項」，對 larotrectinib／entrectinib 只能寫「附件二有收載、附件六查無限制條文，實際能不能用要問醫務課」**。

### ⚠D-10　D5 的「有沒有隨機證據」：有一個，但它自己垮了；另有兩個正在進行、都還沒讀出
- **實際是什麼**：ATA 2025 Recommendation 44 內文寫「Only one multicenter randomized trial has been launched … This study closed in 2003 due to slow accrual after only 45 patients were enrolled.」——這句**與原文形狀不同**。MSDS 原著（[D-S46]）逐字：「In 4/2003 the trial became a prospective cohort study after only 45 of then 311 patients had consented to randomization. 351 of 422 patients met the trial's inclusion criteria. … Of 47 patients randomized or allocated to RTx, 26 actually received RTx.」——不是「只收了 45 人」，而是「311 人裡只有 45 人同意被隨機分配，於是改成世代研究」。
- 另外本組在 clinicaltrials.gov 查到**兩個仍在進行的隨機試驗**：NCT06558981（復旦大學，第三期，1:1 隨機，預計 124 人，主要終點 5 年 LRFS，預計主要完成 2031-06，招募中）與 NCT03669432（Tata Memorial，隨機第二期，實際 72 人，狀態 UNKNOWN，預計主要完成 2026-07）。
- **建議怎麼裁決**：D5 可以、也應該明寫「到今天為止，分化型甲狀腺癌的術後體外放射治療沒有任何一個完成並讀出的隨機對照試驗」，並用 MSDS 的真實形狀（311 人裡 45 人同意隨機）當作「為什麼做不出來」的例子，同時寫出那兩個正在進行的試驗。**不得寫成「有隨機試驗支持」或「永遠不會有隨機試驗」。**

### ⚠D-11　D5 最強的一個數字是**負向**的，但它有嚴重的期別版本問題
- **實際是什麼**：[D-S47] Megwalu 2019（SEER 1988–2013、870 例 **T4 乳突癌**、傾向分數分析）：輔助性 EBRT 與**較差**的 overall survival（HR 1.60，95% CI 1.18–2.16）與 disease-specific survival（HR 1.58，95% CI 1.09–2.30）相關。
- **問題**：1988–2013 跨越 AJCC 第五～第七版，摘要未說明 T4 的定義版本；且是回溯性、有指定偏誤（做放療的本來就比較嚴重）。
- **建議怎麼裁決**：D5 可以用這個數字，但**必須同時寫**：(1) 這是 SEER 回溯資料不是試驗；(2) T4 的定義版本不明（跨 1988–2013）；(3) 方向上最可能的解釋是「病情較重的人才被送去放療」，不是「放療把人害死」。**不可以寫成「放療會降低存活率」。**

### ⚠D-12　Table 9 的「治療反應分類」數值切點，依手術範圍與有無放射碘分成三欄，而且**半切那一欄是 N/A**
- **實際是什麼**（[D-S1] Table 9 逐字，單位 ng/mL）：
  - 全切±頸廓清＋RAI：Excellent「Nonstimulated Tg <0.2 or stimulated Tg <1 and negative imaging」；Indeterminate「nonstimulated Tg 0.2–1 or stimulated Tg 1–10 or stable/declining TgAb levels」；Biochemically incomplete「Non-stimulated Tg >1 or stimulated Tg >10 or increasing TgAb levels and negative imaging」。
  - 全切±頸廓清**無 RAI**：Excellent「Nonstimulated Tg <2.5」；Indeterminate「nonstimulated Tg 2.5–5, or stable/declining TgAb levels」；Biochemically incomplete「Nonstimulated Tg >5 or increasing TgAb levels and negative imaging」。
  - **半切（Post hemithyroidectomy）**：Excellent 那一格根本不用 Tg，寫的是「Normal or low-risk nodules in the contralateral lobe, or contralateral lobe nodules with benign biopsy AND no abnormal lymph nodes on imaging」；Indeterminate 與 Biochemically incomplete 兩格都是 **N/A**。
- **這與 2016 年最常被引用的那組半切切點不同**：Momesso 2016（[D-S22]）當年提的是「lobectomy 非刺激 Tg <30 ng/mL 為 excellent、>30 為 biochemical incomplete」。**ATA 2025 沒有採用它**，而且全切無 RAI 那一欄的 excellent 也從 Momesso 的 <0.2 改成 **<2.5**。
- **建議怎麼裁決**：D2 一律用 ATA 2025 Table 9 的三欄，並明寫「半切之後沒有 Tg 的判讀格」。**不得引用 30 ng/mL 這個數字當作現行標準**（若要提，須標明它是 2016 年單中心研究、ATA 2025 未採納）。

### ⚠D-13　ATA 2025 對「監測可以停」給了明確年限——這件事 SPEC 只寫「什麼時候可以放鬆」，比實際保守
- **實際是什麼**：Recommendation 48 給的是可以**停掉**：低風險＋全切＋RAI、持續 excellent response 者，5–8 年後可停常規超音波、之後只驗生化指標每 1–2 年（Conditional, Low certainty）；**10–15 年持續 excellent 者不需要再繼續常規生化監測，應視為已達 complete remission（Good Practice Statement）**。全切無 RAI 者同樣兩條。半切者「if initial ultrasound is negative, subsequent ultrasounds should be performed every 1–3 years for 5–8 years after initial therapy」（GPS）。
- ATA 2025 並首次把「complete remission」寫進甲狀腺癌指引（過去各版都沒有）。
- **建議怎麼裁決**：D2 可以寫「有一天會被正式宣告結束追蹤」，並逐字引 48-2／48-4。但**必須同時寫出 48 的前提是「low-risk DTC ＋ sustained excellent response」，且指引自己說「Data are more limited for patients treated with lobectomy」。**

### ⚠D-14　ATA 2025 明文反對「Tg 上升就開始吃標靶」
- **實際是什麼**：Recommendation 60 內文逐字：「While biomarker monitoring of serum Tg can be undertaken at 3- to 12-month intervals, increasing Tg levels alone in the absence of structural disease progression should not be considered a criterion warranting the initiation of systemic therapy. Rather, increasing or accelerating Tg levels should lead to consideration of more frequent and/or comprehensive imaging in an effort to identify structural correlates.」
- **建議怎麼裁決**：這是 D3 與 D4 之間的接縫，兩篇都要寫，且要一致。

### ⚠D-15　再分化治療的證據階段：有前瞻第二期、**沒有任何隨機試驗**，而且唯一的第三期（ASTRA）是陰性的
- **實際是什麼**：[D-S44] ITOG 2025 statement 逐字：「The iodine uptake restoration ranges from 33% to 95%, and tumour response rates from 11% to 80%. There is substantial variability between trials … **Randomised studies are missing to clearly establish the effectiveness and applicability of redifferentiation.**」
- 唯一的第三期是 ASTRA（[D-S43]），但它問的不是再分化救援，而是**高風險病人術後輔助 RAI 加不加 selumetinib**：233 人隨機 2:1，18 個月完全緩解率 selumetinib 62/154（40%）vs 安慰劑 30/79（38%），OR 1.07（95% CI 0.61–1.87），p=0.8205 → 陰性。ATA 2025 Recommendation 74B 因此寫「Redifferentiation approaches in adjuvant RAI treatment for patients with high-risk, non-gene selected DTC are not recommended. (Strong recommendation, Moderate certainty evidence)」。
- **建議怎麼裁決**：D4 的再分化段落要寫成「還在試驗階段、而且在『非基因篩選的輔助治療』這個用法上已經被一個第三期試驗否定」。**不得寫成「再分化可以讓放射碘重新有效」這種完成式。**

### ⚠D-16　D5 的兩個「支持段落」都不是甲狀腺癌的資料
- 疼痛性骨轉移的放療證據（單次 vs 多次分割）來自 25 個隨機試驗的統合分析（[D-S50]），**混合各種原發癌**；脊髓壓迫的手術＋放療 vs 單獨放療隨機試驗（[D-S51]，Patchell 2005）也是**混合癌別**（101 人）。甲狀腺癌本身在這兩個領域只有回溯性單中心系列（[D-S1] Recommendation 77 內文所引的 53 人系列）。
- **建議怎麼裁決**：D5 寫這兩段時必須逐句標明「這些試驗不是只做甲狀腺癌的」。這正好也支撐該篇的結論：**連「真的需要放療」的那幾個處境，甲狀腺癌自己的證據也很薄。**

### ⚠D-17　抗甲狀腺球蛋白抗體（TgAb）不是「干擾一下」而已——ATA 2025 把它升級成「這群人主要靠影像追蹤」
- **實際是什麼**：Recommendation 47E 逐字：「In patients with circulating anti-Tg antibodies, trends of serial TgAb levels using the same assay may be useful to monitor disease. Current Tg immunometric assays (IMA) and radioimmunoassays (RIA) are often affected by TgAb, and Tg liquid chromatography-tandem mass spectrometry (LC-MS/MS) has low sensitivity. These should not be solely relied upon to monitor patients with circulating TgAb levels. **Imaging is the primary modality for monitoring in this population.** (Conditional recommendation, Low certainty evidence)」
- 內文另有一句必須抄給讀者：「in clinical series, it is not clear that any Tg assay system is fully accurate in monitoring patients with circulating TgAb」；以及「TgAb are present in about 20% of patients with DTC」。
- **建議怎麼裁決**：D2 要把 TgAb 寫成「換一種追蹤方式」，不是「數字要打折」。

### ⚠D-18　ATA 2025 沒有給「心房顫動／骨折」的量化風險——所有數字都必須自己去原始世代取，而且多數不是甲狀腺癌世代
- **實際是什麼**：ATA 2025 Recommendation 45–46 的討論段只寫了一句定性（「increased risk for atrial fibrillation and stroke (especially in older patients), increased risk for cardiovascular mortality, and increased risk of osteoporosis and possibly fracture in postmenopausal women」），並自承「Some of the recognized adverse effects of TSH suppression are derived from studies of endogenous subclinical hyperthyroidism or from studies of exogenous subclinical hyperthyroidism that exclude patients with thyroid cancer.」
- **建議怎麼裁決**：D1 每一個代價數字都必須標明它是「甲狀腺癌世代」還是「內生性亞臨床甲亢世代」還是「所有吃甲狀腺素的人」——本 brief 的 [D-S9]～[D-S19] 已逐條標。

### ⚠D-19　ATA 2025 對放射碘無效（RAIR）的定義，「強判準」與「輔助判準」是分開的兩層，而且本身寫著會再改
- 見 [D-S1] Recommendation 59 段的逐字全文（下方來源清單）。要注意 Recommendation 59 本身的兩條都是 **Good Practice Statement（沒有 GRADE 等級）**；真正的判準寫在它下面的討論段，**不帶任何建議強度**。
- **建議怎麼裁決**：D4 引用定義時，必須寫「這一段在指引裡沒有給證據等級」。依既有裁決，**不得替 GPS 捏造等級。**

### ⚠D-20　健保給付規定的版本日期與法規修正日期不一致，抄的時候要抄原字串
- 全國法規資料庫顯示「全民健康保險藥物給付項目及支付標準　修正日期：民國 115 年 08 月 24 日」，但其附件六 PDF 第一行寫的是：「第八十三條附件六　藥品給付規定修正規定」「說明：本規定係依本標準第四條第四項規定公告一百十五年一月份之內容；如有異動，以保險人最新公告為主。」附件二亦同（「公告一百十五年一月份之給付項目及支付價格」）。
- **建議怎麼裁決**：引用時一律連同「一百十五年一月份」這個原字串一起寫，並保留「如有異動，以保險人最新公告為主」這句。

---
## 來源清單

### 指引與共識

**[D-S1] 2025 American Thyroid Association Management Guidelines for Adult Patients with Differentiated Thyroid Cancer.** Thyroid : official journal of the American Thyroid Association 2025;35(8):841-985. PMID 40844370；DOI `10.1177/10507256251363120`；PMCID PMC13090833
- 狀態：**PASS**（書目＋全文皆取得）
- 查證路徑：Europe PMC `EXT_ID:40844370&resultType=core` 取書目；`https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13090833/fullTextXML` **回 404**（非 OA 子集）；`https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=13090833&retmode=xml` 回 200 但內含「The publisher of this article does not allow downloading of the full text in XML form.」只有 front matter；最後以瀏覽器 UA 打 `https://pmc.ncbi.nlm.nih.gov/articles/PMC13090833/` → HTTP 200、590,437 bytes（**第一次以預設 UA 取回的是 Google reCAPTCHA 挑戰頁，需重試**），去標籤後正文 988,291 字元、參考文獻 1,458 筆，84 條 RECOMMENDATION 全數可逐字抄。
- 可用的逐字條文（D 組會用到的全部）：
  - **Recommendation 29**（分化型／反應分類）：「The ATA Response Criteria should be used to categorize response to surgery prior to determining intensity of additional therapy or monitoring in combination with the ATA Risk of Recurrence Estimates. (Strong Recommendation, Moderate certainty evidence)」；四類定義逐字：「A. Excellent response: no clinical, biochemical or structural evidence of disease. B. Indeterminate response: nonspecific biochemical or structural findings, which cannot be confidently classified as either benign or malignant. This includes patients with stable or declining TgAb levels without definitive structural evidence of disease. C. Biochemical incomplete response: abnormal Tg or rising TgAb levels in the absence of localizable disease. D. Structural incomplete response: persistent or newly identified locoregional or distant metastases on imaging.」
  - **Recommendation 30**（Tg 何時驗，分化型）：「A. Measuring a postoperative serum Tg level 6–12 weeks after total thyroidectomy while on thyroid hormone therapy or after TSH stimulation is recommended. Such measurements may guide additional decision-making regarding clinical management. (Strong recommendation, Low certainty evidence)」「B. Measurement of serum Tg on one occasion 6–12 weeks after thyroid lobectomy with a normal TSH may be helpful to ensure that it is not unexpectedly elevated; however, a specific cutoff value is uncertain. (Good Practice Statement)」
  - **Recommendation 31**（超音波與影像，分化型）：A「Ultrasound to evaluate the thyroid bed and central and lateral cervical lymph node compartments is the preferred method of imaging surveillance for most DTC. (Strong recommendation, Moderate certainty evidence)」；C「Six to 12 months following completion of initial therapy, cervical ultrasound to evaluate the thyroid bed and central and lateral cervical lymph node compartments should be performed. Timing and frequency thereafter are informed by the patient's risk for residual or recurrent disease and response to therapy. (Good Practice Statement)」；D「Suspicious lymph nodes or lesions <8–10 mm in shortest dimension may be followed without FNA unless they grow or threaten vital structures (such as the recurrent laryngeal nerve, trachea, esophagus, or great vessels). (Conditional recommendation, Low certainty evidence)」；F「When Tg (or TgAb) levels rise following total thyroidectomy for DTC, and cervical ultrasound demonstrates no structural disease or only minimal tumor burden, additional cross-sectional imaging to evaluate common metastatic sites (e.g. lungs and bone) should be performed. (Good Practice Statement)」；G「When Tg (or TgAb) levels rise following total thyroidectomy for OTC and PDTC, and cervical ultrasound demonstrates no structural disease or shows only minimal tumor burden, 18FDG-PET/CT may be considered. (Conditional recommendation, Low certainty of evidence)」
  - **Recommendation 45**（TSH 抑制程度）：「Individualization of decisions to initiate TSH suppression to below the reference range is recommended based on potential benefits and risks; recognizing that patients with high-risk disease may be more likely to benefit from a TSH in the subnormal range than those with low-risk disease (see Table 9). (Conditional recommendation, Low certainty evidence)」
  - **Recommendation 46**（要抑制多久）：「A. Long-term TSH suppression is not suggested for patients with low- or intermediate-risk disease who have no evidence of biochemical or structural recurrence. (Conditional recommendation, Low certainty evidence)」「B. Risks versus benefits of TSH suppression and TSH goals should be re-evaluated over time. (Good Practice Statement)」
  - **Recommendation 47**（Tg／TgAb 測量）：A「Serum Tg should be measured by an assay that is calibrated against the BCR457 standard. Tg antibodies should be quantitatively assessed with every measurement of serum Tg. (Good Practice Statement)」；B「Measure serum Tg (on thyroid hormone therapy) after total thyroidectomy, with or without RAI, to monitor for response to therapy and to determine recurrence (although the predictive value is greater after RAI). (Strong recommendation, Moderate certainty of evidence)」；C「Measurement of serum Tg during initial follow-up while receiving thyroxine therapy should be undertaken every 6–12 months. More frequent serum Tg measurements may be appropriate for ATA intermediate-high or high-risk patients. (Good Practice Statement)」；D「Measurement of serum Tg on thyroid hormone in patients after lobectomy during initial follow-up is not recommended routinely (see Recommendation 30). (Conditional recommendation, Very low certainty evidence)」；E 見 ⚠D-17。
  - **Recommendation 48**（可否降階／停止監測）：六條全文見 ⚠D-13；逐字關鍵兩條——48-2「Patients with low-risk DTC treated with total thyroidectomy and RAI and sustained excellent response for 10–15 years do not require continued routine biochemical monitoring for thyroid cancer and should be considered to have achieved a complete remission. (Good Practice Statement)」；48-5「For patients with low-risk DTC treated with lobectomy, if initial ultrasound is negative, subsequent ultrasounds should be performed every 1–3 years for 5–8 years after initial therapy. Nodules in the residual lobe should be monitored as per ATA thyroid nodule guidelines. (Good Practice Statement)」
  - **Recommendation 49**（診斷性全身掃描）：A「Patients who have undergone lobectomy or total thyroidectomy without RAI should not undergo surveillance radioiodine WBS. (Good Practice Statement)」；B「Patients with DTC who are at low- and low-intermediate risk of recurrence and who have excellent response to therapy do not require routine diagnostic radioiodine WBS during follow-up. (Conditional recommendation, Low certainty evidence)」；C「Patients with DTC who are at intermediate-high and high risk of recurrence can be evaluated with diagnostic radioiodine WBS to evaluate for iodine-avid disease if there is clinical suspicion for recurrence. WBS, if undertaken, can be performed with 123I or low activity 131I. (Conditional recommendation, Low certainty evidence)」；D「SPECT-CT radioiodine imaging may be performed in addition to planar imaging to anatomically localize the radioiodine uptake and distinguish between likely cancer and nonspecific uptake. (Conditional recommendation, Low certainty evidence)」
  - **Recommendation 50**（FDG-PET/CT）：A「Imaging using 18FDG-PET/CT scanning may be performed in patients with DTC at high risk of recurrence with elevated serum Tg levels, particularly in patients with OTC or aggressive histologies and in patients who have a history of negative RAI imaging. (Conditional recommendation, Moderate certainty evidence)」；B「Imaging with 18FDG-PET/CT scanning may also be employed: (i) as a prognostic tool in patients at highest risk for rapid disease progression and disease-specific mortality and (ii) as an evaluation of post-treatment response following systemic or local therapy of invasive disease. (Conditional recommendation, Low certainty evidence)」；內文另有「In patients with high-risk DTC with elevated serum Tg levels (generally >10 ng/mL)」與「The frequency of false positive lesions varies from 0% to 39% between series, even with TSH stimulation.」與「18FDG-PET is insensitive for detecting brain metastases and that standard imaging stops in the mid-thigh.」
  - **Recommendation 58**（Tg 陽性、掃描陰性）：A「In the absence of structurally demonstrable disease, patients with stimulated serum Tg <10 ng/mL after thyroid hormone withdrawal or <5 ng/mL with rhTSH (indeterminate response) can be followed with thyroid hormone therapy alone, reserving additional treatment for emergence of rising serum Tg levels over time or other evidence of structural disease progression. (Conditional recommendation, Low certainty evidence)」；B「Empiric (3.7–7.4 GBq, 100–200 mCi) or dosimetrically determined RAI therapy may be considered in patients with more significantly elevated or rapidly rising serum Tg levels where imaging (e.g. cross sectional imaging and/or 18FDG-PET/CT) has failed to reveal tumor amenable to directed therapy. (Conditional recommendation, Low certainty evidence)」；內文逐字「more than half of patients with negative diagnostic WBS experience a fall in serum Tg levels after empirical RAI therapy, but improved survival has not been shown with empirical therapy in this setting」「This approach may disclose the location of persistent disease in up to 50% of patients. However, the reported range of success is wide.」
  - **Recommendation 59（RAIR 定義）**：A「RAIR DTC (including OTC) cannot be diagnosed in patients who have not received an ablative or treatment dose of RAI. Patients who meet criteria for RAI should receive ablative or treatment administrations of RAI to determine status. (Good Practice Statement)」；B「Patients who have RAIR DTC should not receive additional empiric RAI therapy. Other treatments should be considered. (Good Practice Statement)」。判準（**無等級**）逐字：「Strong criteria suggesting iodine-refractory DTC include (i) absence of 131I uptake on a post-therapy scan (Recommendation 37) in the setting of confirmed disease visible on structural or 18FDG-PET imaging. This may occur at the time of initial treatment of metastatic DTC or at the time of a subsequent RAI, and/or (ii) progression of disease less than 6 months after a treatment appropriate administration of therapeutic RAI demonstrated uptake on post-therapy scans.」；再逐字：「We propose the following criteria which may suggest an iodine-refractory state in patients with metastatic DTC: When a patient does not have uptake on post-therapy scans in the setting of structurally apparent disease on imaging, and/or when there is progression of disease fewer than 6 months after treatment, such a patient is unlikely to receive benefit from additional RAI administration.」；**Supplemental criteria suggesting less RAI sensitivity** 逐字：「A. No uptake present on a diagnostic 123I or 131I WBS in the presence of otherwise detectable disease. This criterion is known to predict less favorable response to RAI, but some fraction of patients in this category will have a positive post-therapy scan and may still derive some clinical benefit from RAI. B. Uptake is present in some (but not all) tumor foci on post-therapy WBS. This criterion does not preclude use of RAI but instead suggests that a multimodal treatment approach could be appropriate depending on therapeutic response. RAI alone is not adequate treatment for this subgroup of patients.」；另一句 D4 很需要：「while some of these patients die within 3–5 years, there are also long-term survivors with stable or very slowly progressive disease」；以及「About two-thirds of patients with metastases demonstrate 131I uptake in them, and only half of such individuals will be cured with repeated courses of RAI.」
  - **Recommendation 60**（哪些人可以只觀察）：A「Patients with RAIR metastatic DTC that is asymptomatic, stable, or minimally progressive, or who have clinically significant comorbidities, can be monitored on TSH-suppressive thyroid hormone therapy with serial radiographic imaging every 3–12 months. (Conditional recommendation, Low certainty evidence)」；B「In the absence of planned systemic treatment or redifferentiation therapy, molecular testing is not routinely recommended in patients with RAIR residual DTC. (Conditional recommendation, Moderate certainty evidence)」；並見 ⚠D-14 的逐字句。
  - **Recommendation 61**：「Tissue-based biomarker testing to identify actionable oncogenic driver alterations in RAIR DTC should be performed prior to initiating systemic therapy for progressive disease. (Strong recommendation, Moderate certainty evidence)」
  - **Recommendation 62**：「For patients with progressive RAIR DTC without an actionable biomarker-linked FDA-approved first-line therapy, MKI therapy with either lenvatinib or sorafenib is recommended. In most cases, lenvatinib is the preferred first-line MKI. (Strong recommendation, High certainty evidence)」
  - **Recommendation 63（什麼時候開始吃藥）**：A「Lenvatinib or other therapy should be initiated without delay in patients with symptomatic RAIR DTC for whom local therapy, such as radiation or surgery, is not appropriate. (Strong recommendation, Moderate certainty evidence)」；B「For patients with asymptomatic RAIR DTC that has progressed over the prior 12–14 months and local therapy is not appropriate, if efficacy outcomes are the most important goal of treatment, earlier initiation of lenvatinib may be considered. For patients with asymptomatic progressive RAIR DTC for whom QoL is a major priority, delaying the initiation of lenvatinib and continuing disease monitoring may be most appropriate. (Good Practice Statement)」
  - **Recommendation 64**：A「For most patients with progressive RAI-refractory DTC initiating lenvatinib, 24 mg once daily is the recommended starting dose; a lower starting dose may be indicated in selected patients. (Strong recommendation, High certainty evidence)」
  - **Recommendation 66**：「Cabozantinib should be offered as second-line therapy for patients with RAIR DTC without an actionable oncogenic driver alteration who have progressed on or did not tolerate, prior MKI therapy, if they desire ongoing treatment, and do not have a contraindication to therapy. (Strong recommendation, High certainty evidence)」
  - **Recommendation 67**：「In patients with progressive RAIR DTC harboring an oncogenic NTRK fusion, NTRK-targeted therapy is recommended in the first line. (Strong recommendation, Moderate certainty evidence)」；內文「The prevalence of NTRK gene fusion in PTC is approximately 7%.」「NTRK fusions occur more frequently in PTCs diagnosed in children and young adults, at approximately 25%.」
  - **Recommendation 68**：「In patients with progressive RAIR DTC harboring an oncogenic RET fusion, RET-targeted therapy is recommended in the first line. (Strong recommendation, Moderate certainty evidence)」；內文「RET fusions occur in approximately 10–15% of PTCs but are more common in pediatric and young cases and in radiation-induced thyroid cancers.」
  - **Recommendation 70**（BRAF）：a「In patients with progressive RAIR DTC harboring an oncogenic BRAF V600E mutation, BRAF V600E-directed therapy may be considered in the first line for patients who are poor candidates for lenvatinib. (Conditional recommendation, Moderate certainty evidence)」；b「BRAF-directed treatment is recommended in patients with BRAF V600E mutation-positive RAIR DTC who have progressed on or did not tolerate one or more prior MKI therapies. (Strong recommendation, Moderate certainty evidence)」；c「Currently approved BRAF-directed therapies are not recommended in DTCs harboring non-V600 BRAF alterations. (Strong recommendation, Moderate certainty evidence)」
  - **Recommendation 74（再分化）**：A「Redifferentiation by MAPK pathway blockade in patients with progressive RAIR DTC harboring targetable mutations may be considered in selected patients. Clinical trial participation is encouraged. (Conditional recommendation, Low certainty evidence)」；B「Redifferentiation approaches in adjuvant RAI treatment for patients with high-risk, non-gene selected DTC are not recommended. (Strong recommendation, Moderate certainty evidence)」；內文結語「Currently, redifferentiation therapy is only considered for individuals with tumors harboring BRAF or RAS-mutations.」
  - **Recommendation 44（EBRT，D5 主條文）**：A「Adjuvant external beam radiotherapy (EBRT) for patients with DTC with high-risk features for locoregional disease progression (such as aggressive histologic subtype, gross extrathyroidal extension, positive margins, and visceral or soft tissue invasion) may be considered in select cases, especially if the expected disease progression would not be amenable to salvage surgery. The potential benefit of improving locoregional relapse-free survival must be weighed against the absence of data demonstrating improvement in overall survival and the known risks of clinically meaningful toxicity. (Conditional recommendation, Low certainty evidence)」；B「EBRT with or without concurrent chemotherapy in patients with DTC with gross residual disease in the postoperative setting or with locally advanced unresectable disease may be considered in select patients who may benefit from improved locoregional control. EBRT with or without concurrent chemotherapy may increase locoregional control but also causes acute- and long-term treatment-related toxicity. (Conditional recommendation, Low certainty evidence)」
  - **Recommendation 44 討論段（D5 需要的頸部放療警告，逐字）**：「results available to date do not support the adoption of adjuvant EBRT as a standard of care in patients with high-risk locally advanced DTC, particularly in light of the risks of acute and long-term treatment-related adverse effects that may impact patient QoL and **make future revision neck surgery for recurrent disease still more challenging**.」；劑量描述「The range of radiation dose administered is primarily 6000–6600 cGy」與「In treating gross disease, IMRT administered to 7000 cGy was most common, with evidence indicating that locoregional control is improved with doses higher than 5000 cGy.」；單中心回溯系列的存活區間「locoregional relapse-free, disease-specific, and overall survival rates were reported at varying time periods spanning 4–10 years and ranged from 79% to 95%, 71% to 76%, and 65% to 93%, respectively.」（**回溯性、非隨機、混合風險族群**）
  - **Recommendation 54（頸部復發的 EBRT）**：「EBRT using modern techniques such as IMRT and stereotactic radiation may be considered for locoregional recurrences that are not surgically resectable or when there is extranodal extension or involvement of soft tissues. (Conditional recommendation, Low certainty evidence)」
  - **Recommendation 77（症狀性 RAIR 的局部治療）**：「For patients with symptomatic RAIR DTC, local treatment is suggested. Surgery, radiotherapy, and percutaneous thermo-ablative approaches are available to treat individual symptomatic sites of disease. (Conditional recommendation, Moderate certainty evidence)」；內文逐字「While prospective controlled trials are lacking, palliative radiotherapy is well tolerated and effective at producing durable local control in many cases.」；骨轉移逐字「Bone metastases in DTC are typically osteolytic and highly destructive to bone structural integrity and cause frequent skeletal-related events (including pathological fracture, spinal cord compression, and pain), impairing QoL and survival.」；脊椎逐字「Indications for palliative surgery include vertebral metastases associated with spinal cord compression or impending compression and risk of fracture in weight-bearing long-bone metastases.」「Postoperative radiotherapy is typically administered to reduce the risk of local recurrence.」
  - **Recommendation 78（骨骼保護劑）**：A「In patients with RAIR DTC with symptomatic and/or multiple bone metastases, treatment with a bone modifying agent is recommended to decrease the risk of skeletal-related events. (Strong recommendation, Low certainty evidence)」；內文自承「large-scale clinical trials have not been carried out in DTC」。
  - **Recommendation 79（腦轉移）**：A「Resection and/or SBRT are the mainstays of therapy for central nervous system metastases. (Conditional recommendation, Low-certainty evidence)」；B「RAI can be considered if central nervous system metastases concentrate RAI. If RAI is planned, SBRT and concomitant glucocorticoid therapy are recommended prior to RAI therapy to minimize the effects of a potential TSH induced increase in tumor size and RAI induced inflammatory response. (Good Practice Statement)」
  - **Recommendation 55C 討論段（脊髓／腦附近病灶要先放療再放射碘）**逐字：「If brain or spinal canal metastases are detected, EBRT prior to RAI and high-dose corticosteroid therapy are recommended to limit the risk of acute tumor swelling (see Recommendation 79).」
  - **Table 9 全文**見 ⚠D-1／⚠D-12。**Table 11**（低風險＋excellent response 的降階表）逐字三列：「Hemithyroidectomy｜Once postoperatively (see Recommendation 48)｜Normal｜Every 1–3 years for 5–8 years」「Total thyroidectomy, no RAI Excellent response｜<2.5 ng/mL with undetectable TgAb｜Normal｜Every 1–3 years for 5–8 years, then discontinue unless Tg level rises or TgAb becomes newly detectable」「Total thyroidectomy + RAI Excellent response｜<0.2 ng/mL with undetectable TgAb｜Normal｜Every 1–3 years for 5–8 years and then discontinue unless Tg level rises or TgAb becomes newly detectable」
  - **動態風險分層的復發率（分化型、全切＋RAI，終點為 structural recurrence）**逐字：「those who achieved an excellent response to therapy had recurrence rates of 1–4%」「When specifically evaluating low-risk patients who achieved an excellent response, risk of recurrence was 0.2–2%」「When evaluating intermediate-risk patients, 1–12% developed a structural recurrence」「Patients with high risk at initial assignment who achieved an excellent response experienced recurrences 3–15% of the time」「For those with an indeterminate response to therapy, recurrence rates range from 5% to 15–20%」「Patients with biochemically incomplete responses to therapy experienced recurrences 20−53% of the time」
  - **全切無 RAI 者**逐字：「Those with excellent responses had recurrence rates of 0–1.6% in all studies except Lee et al., where a recurrence rate of 7.4% was observed.」「Those with indeterminate responses experienced a 0–5.6% recurrence rate. Biochemically incomplete response to therapy was associated with a 0–31.6% rate of recurrence. All those categorized as structurally incomplete responses experienced continued presence of disease.」
  - **半切後 TSH 目標的臨床意涵**逐字：「The TSH goal for those patients with low or intermediate risk for recurrence of thyroid cancer (after a total thyroidectomy or after a thyroid lobectomy) is in the normal reference range (Table 9). Prior studies suggest that if the TSH goal is within the normal range, about 70–80% of patients who undergo lobectomy can avoid thyroid hormone supplementation. In contrast, if the goal TSH level is 0.5–2.0 mIU/L, only 20–30% of patients who undergo lobectomy can avoid thyroid hormone supplementation. If TSH is above the normal reference range (after total thyroidectomy or after thyroid lobectomy), then thyroid hormone therapy should be initiated. Thyroid hormone replacement therapy is most frequently started in the first 2 years after thyroid lobectomy, but for up to a quarter of patients, it is started later.」
  - **真實世界達標率**逐字：「with use of target TSH levels per the 2015 ATA guidelines, of 1125 patients with DTC who were treated at 21 medical centers, only 29% had TSH levels at target normal reference range despite 82.8% having good or moderate adherence to therapy. Approximately 50% of the patients were overtreated, and 20% were undertreated.」（原始出處為 ref 950 Yavuz 2022，**本組未回原文驗證，屬 ATA 轉述，寫作組僅可用「大多數人其實沒有停在醫師想要的那一格」這樣的定性說法，不得引用 29%／50%／20% 這三個數字**）
- 四條線標籤：全部為**分化型甲狀腺癌（乳突／濾泡／嗜酸性）**；終點為 **structural recurrence／response-to-therapy 分類**，不是 OS；**不適用於髓質癌與未分化癌**。

**[D-S2] Corrigendum to: 2025 American Thyroid Association Management Guidelines for Adult Patients with Differentiated Thyroid Cancer.** Thyroid 2025;35(11):1350. PMID 41182278；DOI `10.1177/10507256251387671`；PMCID PMC13521431（OA）
- 狀態：**PASS**
- 查證路徑：`https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13521431/fullTextXML` HTTP 200, 6,970 bytes，全文逐字讀完。
- 可用的內容：更正三項——兩位作者的機構、一位作者姓名中間縮寫、**Table 8 的列標題「Follicular Carcinoma」應為「Follicular Carcinoma and IEFVPTC」**。**與 D 組五篇無關**（Table 8 屬 A 組範圍）。可用來說明「這份指引出版後有勘誤，但沒有動到追蹤與進階治療的條文」。

**[D-S3] 2015 American Thyroid Association Management Guidelines for Adult Patients with Thyroid Nodules and Differentiated Thyroid Cancer: The American Thyroid Association Guidelines Task Force on Thyroid Nodules and Differentiated Thyroid Cancer.** Thyroid 2016;26(1):1-133. PMID 26462967；DOI `10.1089/thy.2015.0020`；PMCID PMC4739132
- 狀態：**PASS（僅作為「已被取代的舊版」對照用）**
- 查證路徑：Europe PMC `EXT_ID:26462967&resultType=core`（注意 Europe PMC 回傳的年份是 **2016**、卷期 26(1):1-133，不是 2015）；全文以瀏覽器 UA 打 `https://pmc.ncbi.nlm.nih.gov/articles/PMC4739132/` HTTP 200、534,068 bytes 取得。
- 可用的逐字條文（**只能用在「以前是這樣、現在改了」的對照句**）：Recommendation 70(A)「In patients with a structural incomplete response to therapy, the serum TSH should be maintained below 0.1 mU/L indefinitely in the absence of specific contraindications. (Strong recommendation, Moderate-quality evidence)」；70(B)「…maintained between 0.1 and 0.5 mU/L…(Weak recommendation, Low-quality evidence)」；70(D)「…the serum TSH may be kept within the low reference range (0.5–2 mU/L). (Strong recommendation, Moderate-quality evidence)」。另 Recommendation 62(B)「During initial follow-up, serum Tg on thyroxine therapy should be measured every 6–12 months. More frequent Tg measurements may be appropriate for ATA high-risk patients.」（**2025 版把「high-risk」改成「intermediate-high or high-risk」，且建議強度從 Strong 降為 Good Practice Statement**）
- 四條線標籤：分化型；復發風險為**2015 三級**分層，**不可與 2025 四級互譯**。

### D1 專用：TSH 抑制的效益側

**[D-S4] Does postoperative thyrotropin suppression therapy truly decrease recurrence in papillary thyroid carcinoma? A randomized controlled trial.** The Journal of clinical endocrinology and metabolism 2010;95(10):4576-4583. PMID 20660039；DOI（EPMC 回傳）`10.1210/jc.2010-0161`
- 狀態：**PASS**（僅摘要；非 OA、無 PMCID）
- 查證路徑：Europe PMC `TITLE:"Does postoperative thyrotropin suppression therapy truly decrease recurrence in papillary thyroid carcinoma"` hitCount 1 → `resultType=core` 取全摘要。
- 可用的數字（**組織型：乳突癌**；**風險分層：AMES，不是 ATA**；**終點：disease-free survival**；**手術範圍：文中稱「thyroid-conserving surgery」為主，未統一全切**；**放射碘：未規定**）：
  - 收案 1996–2005；**抑制組 218 人、不抑制組 215 人**，意向治療分析。
  - 抑制組目標「serum TSH 低於 0.01 μU/ml」；對照組「TSH 維持在正常範圍」。
  - 結論逐字：「DFS did not differ significantly between groups. The 95% confidence interval of the hazard ratio for recurrence was 0.85-1.27 according to Cox proportional hazard modeling, within the margin of 2.12 required to declare 10% noninferiority.」——**摘要只給 CI，未給 HR 點估計值**；幾何中心約 1.04，與 CI 一致（無標錯）。
  - 結論逐字：「Thyroid-conserving surgery without TSH suppression should be considered for patients with low-risk PTC to avoid potential adverse effects of TSH suppression.」
- **使用限制**：這是**非劣性**設計，只能說「不抑制沒有比較差」，**不能說「抑制無效」**。ATA 2025 內文另補了兩個排除條件（逐字）：「Patients with T1a PTC, distant metastases, age ≥80 years, Graves' disease, ischemic heart disease/arrhythmia, or severe osteoporosis were not eligible for the trial.」以及「Most of the patients in this study did not undergo total thyroidectomy or RAI, and Tg levels were not monitored or reported.」

**[D-S5] Effects of thyroid hormone suppression therapy on adverse clinical outcomes in thyroid cancer.** Annals of medicine 2002;34(7-8):554-564. PMID 12553495；DOI `10.1080/078538902321117760`
- 狀態：**PASS**（僅摘要）
- 查證路徑：Europe PMC `TITLE:"Effects of thyroid hormone suppression therapy on adverse clinical outcomes in thyroid cancer"` hitCount 1。
- 可用的數字（**組織型：乳突＋濾泡**；**終點：major adverse clinical events＝disease progression／recurrence／death 的合成**；**手術與放射碘：1934–2001 年的研究，未標準化**）：
  - 納入 28 篇、可統合者 10 篇；**4,174 人中 2,880 人（69%）接受抑制治療**。
  - **RR = 0.73（CI 0.60–0.88；P<0.05）**。（幾何檢查：√(0.60×0.88)=0.727，與 0.73 一致。**摘要未標明是 95% 還是其他水準，引用時寫「CI 0.60–0.88」不加百分比。**）
- **使用限制**：這是 D1 唯一「支持抑制」的量化證據，年代 1934–2001、合成終點混合了復發與死亡，**不得寫成「抑制可以降低死亡」**。

**[D-S6] The Effect of Thyrotropin Suppression on Survival Outcomes in Patients with Differentiated Thyroid Cancer: A Systematic Review and Meta-Analysis.** Thyroid 2024;34(6):674-686. PMID 38717947；DOI `10.1089/thy.2023.0711`；PMCID PMC11295840
- 狀態：**PASS**（摘要完整）
- 查證路徑：Europe PMC `TITLE:"The Effect of Thyrotropin Suppression on Survival Outcomes in Patients with Differentiated Thyroid Cancer"` hitCount 1。
- 可用的數字（**組織型：分化型**；**風險組：僅中／高風險（intermediate- and high-risk），≥18 歲，追蹤 5 年**；**抑制定義：below normal reference range，或已知時 <0.5 mIU/L**）：
  - PROSPERO #252396；篩 6,369 篇，最終 9 篇。
  - **PFS／DFS／RLFS 合成（7 篇、3,591 人）：HR 0.75（95% CI 0.48–1.17；I²=76%）→ 不顯著。**（幾何檢查 √(0.48×1.17)=0.749 ✓）
  - **DSS／OS 合成（4 篇、3,616 人）：HR 0.69（95% CI 0.31–1.52；I²=88%）→ 不顯著。**（√(0.31×1.52)=0.686 ✓）
  - **心臟或骨骼不良事件合成（2 篇、1,294 人）：HR 1.82（95% CI 1.30–2.55；I²=0%）→ 抑制組顯著較高。**（√(1.30×2.55)=1.821 ✓）
- **使用限制**：**這是中／高風險族群的結果，不可外推到低風險**（低風險族群的隨機證據只有 [D-S4]）。異質性極高（I² 76%／88%）。

**[D-S7] Association of Thyrotropin Suppression With Survival Outcomes in Patients With Intermediate- and High-Risk Differentiated Thyroid Cancer.** JAMA network open 2019;2(2):e187754. PMID 30707227；DOI `10.1001/jamanetworkopen.2018.7754`；PMCID PMC6484595（OA）
- 狀態：**PASS**
- 查證路徑：Europe PMC 標題精確查詢 hitCount 1。
- 可用的數字（**組織型：分化型**；**風險組：ATA 中／高風險**；**手術：全部全切**；**放射碘：全部接受，中位累積 151 mCi（範圍 30–1600）**；**終點：PFS 與 OS**）：
  - 1979-01-01～2015-03-01 收案，1,012 人中排除 145 人無縱向 TSH 值 → **分析 867 人**（女性 557 人 64.2%，平均年齡 48.5±16.5 歲），平均追蹤 7.2±5.8 年。
  - **疾病進展 293 人（33.8%），死亡 34 人（3.9%）——作者自承「the study was underpowered in death events」。**
  - **TSH 抑制與 PFS 改善無關**：landmark 1.5 年 P=0.41、3.0 年 P=0.51、5.0 年 P=0.64。
  - 作者結論逐字：「Patients with intermediate- and high-risk DTC might not benefit from thyrotropin suppression. This study provides the justification for a randomized trial.」
- **使用限制**：回溯世代；死亡事件太少。

**[D-S8] Thyrotropin suppression increases the risk of osteoporosis without decreasing recurrence in ATA low- and intermediate-risk patients with differentiated thyroid carcinoma.** Thyroid 2015;25(3):300-307. PMID 25386760；DOI `10.1089/thy.2014.0287`；PMCID PMC6916125
- 狀態：**PASS**
- 查證路徑：Europe PMC `TITLE:"Thyrotropin suppression increases the risk of osteoporosis without decreasing recurrence"` hitCount 3（本篇＋一篇 Letter 回覆）。
- 可用的數字（**組織型：分化型**；**風險組：ATA 低／中風險（2009 版分層）**；**手術：全部全切**；**放射碘：未限定**；**終點：structural recurrence／術後心房顫動／術後骨質疏鬆**）：
  - **771 人**（女性 569 人），平均年齡 48±14 歲，2000–2006 年於單一三級中心全切，中位追蹤 6.5 年。
  - 依中位 TSH 分兩組：**≤0.4 mIU/L（抑制）vs >0.4 mIU/L（未抑制）**。
  - **結構性復發 43/771（5.6%）；術後骨質疏鬆 29/739（3.9%，僅計女性）；術後心房顫動 17/756（2.3%）。**
  - **復發風險兩組相同：HR 1.02（p=0.956；CI 0.54–1.91）。**（√(0.54×1.91)=1.016 ✓）
  - **心房顫動＋骨質疏鬆的合成終點：HR 2.1（p=0.05；CI 1.001–4.3）。**（√(1.001×4.3)=2.075 ✓）
  - **單看心房顫動：HR 0.78（p=0.63；CI 0.3–2.1）→ 未偵測到差別。**
  - **女性術後骨質疏鬆：HR 3.5（p=0.023；CI 1.2–10.2）。**（√(1.2×10.2)=3.50 ✓）
  - 作者逐字：「The increased risk of postoperative osteoporosis disappeared when the patient's median TSH was maintained around 1 mIU/L.」
- **這是 D1 最好用的一篇**：同一個世代、同時給了「好處（沒有）」與「代價（有）」，而且分母都寫清楚。注意 CI 未標百分比水準，引用時照抄「CI 1.2–10.2」。

### D1 專用：心房顫動

**[D-S9] Low serum thyrotropin concentrations as a risk factor for atrial fibrillation in older persons.** The New England journal of medicine 1994;331(19):1249-1252. PMID 7935681；DOI（EPMC 回傳）`10.1056/nejm199411103311901`
- 狀態：**PASS**
- 查證路徑：Europe PMC 標題精確查詢 hitCount 1。（**注意：依記憶用 PMID 7969281 會抓到完全無關的古柯鹼與 HIV 論文——本組實測到這個陷阱，PMID 一律以標題查詢回抄。**）
- 可用的數字（**族群：社區長者，不是甲狀腺癌病人**；**TSH 為內生性低下，非外源性甲狀腺素造成**；**終點：新發心房顫動**）：
  - **2,007 人（男 814、女 1,193），年齡 ≥60 歲，追蹤 10 年**。依 TSH 分四組：≤0.1 mU/L（61 人）、>0.1–0.4（187 人）、>0.4–5.0（1,576 人）、>5.0（183 人）。
  - **10 年累積發生率：TSH ≤0.1 組 28%，正常組 11%**；年齡校正後發生率 28 vs 10／1,000 人年（P=0.005）。
  - **校正其他危險因子後，TSH ≤0.1 相對於正常：相對風險 3.1（95% CI 1.7–5.5；P<0.001）。**（√(1.7×5.5)=3.06 ✓）
  - **TSH >0.1–0.4 的「輕度偏低」組與正常組沒有顯著差別。**
- **使用限制（重要）**：這是 Framingham 世代的長者研究，**不是甲狀腺癌病人、不是吃甲狀腺素造成的低 TSH**。D1 引用時必須明說。同時它給了 D1 一個很有用的細節：**風險主要出現在 ≤0.1 這一格，0.1–0.4 那一格沒看到。**

**[D-S10] The spectrum of thyroid disease and risk of new onset atrial fibrillation: a large population cohort study.** BMJ (Clinical research ed.) 2012;345:e7895. PMID 23186910；DOI `10.1136/bmj.e7895`；PMCID PMC3508199（**OA**）
- 狀態：**PASS**
- 查證路徑：Europe PMC 標題精確查詢 hitCount 1。
- 可用的數字（**族群：丹麥哥本哈根基層醫療全人口，非甲狀腺癌**；**終點：新發心房顫動**）：
  - **586,460 名成人**（平均年齡 50.2±16.9 歲，男性 39%），2000–2010 年首次驗甲狀腺功能、先前無甲狀腺疾病或心房顫動。
  - 分布：甲狀腺功能正常 562,461（96.0%）、明顯甲狀腺低下 1,670（0.3%）、亞臨床低下 12,087（2.0%）、明顯甲狀腺亢進 3,966（0.7%）、亞臨床亢進 6,276（1.0%）。
  - **相對於正常組的發生率比（incidence rate ratio）：正常偏高 TSH 1.12（95% CI 1.03–1.21）；亞臨床亢進／TSH 偏低 1.16（0.99–1.36）；亞臨床亢進／TSH 受抑制 1.41（95% CI 1.25–1.59）。**（√(1.25×1.59)=1.41 ✓）
  - **明顯與亞臨床甲狀腺低下反而與較低的心房顫動風險相關。**
- **使用限制**：內生性甲狀腺疾病，非甲狀腺癌病人的外源性抑制。

**[D-S11] Risk of atrial fibrillation in patients with differentiated thyroid cancer: a nationwide population-based analysis.** The Korean journal of internal medicine 2026;41(2):286-295. PMID 41850220；DOI `10.3904/kjim.2025.129`；PMCID PMC12999249（**OA**）
- 狀態：**PASS**
- 查證路徑：Europe PMC `TITLE:"atrial fibrillation" AND TITLE:"thyroid cancer"` hitCount 5 → `EXT_ID:41850220&resultType=core`。
- 可用的數字（**組織型：分化型**；**族群：韓國 National Health Information Database 全民資料，2006–2019**；**終點：新發心房顫動**；**依手術範圍與有無放射碘分層——正好對上第六條分界線**）：
  - **113,791 名分化型甲狀腺癌病人 vs 455,188 名年齡性別配對對照**。
  - **整體：HR 2.07（95% CI 1.98–2.17）。**（√(1.98×2.17)=2.073 ✓）
  - **全切未做放射碘：HR 2.20（95% CI 2.06–2.34）。**
  - **全切＋放射碘：HR 2.07（95% CI 1.95–2.20）。**
  - **單葉切除：HR 1.93（95% CI 1.72–2.15）。**
- **使用限制（非常重要）**：這是「有沒有得甲狀腺癌」的比較，**不是「有沒有抑制 TSH」的比較**；連只做單葉切除的人 HR 也有 1.93，所以**不能把整個 2.07 歸因於 TSH 抑制**。D1 若用這個數字，必須連同單葉那一格一起寫，否則會誤導。

**[D-S12] Incident atrial fibrillation in patients with differentiated thyroid cancer: a meta-analysis.** Endocrine-related cancer 2021;28(5):325-335. PMID 33794503；DOI `10.1530/erc-20-0496`；PMCID PMC8111325（**OA**）
- 狀態：**PASS**
- 查證路徑：同上一筆的查詢結果。
- 可用的數字（**組織型：分化型**；**終點：新發心房顫動**）：
  - 6 篇觀察性研究，**共 187,754 名分化型甲狀腺癌病人與 199,770 名健康對照**，中位追蹤 4.3–18.8 年。
  - **心房顫動發生率 4.86／1,000 人年（95% CI 3.29–7.17；I²=96%）。**
  - **發生率比（incidence rate ratio）1.54（95% CI 1.44–1.65；I²=0%；95% 預測區間 1.33–1.78）。**（√(1.44×1.65)=1.54 ✓）
- **使用限制**：作者把它歸因於長期 TSH 抑制造成的醫源性甲狀腺亢進，但納入研究並未直接比較抑制與不抑制。

### D1 專用：骨質與骨折

**[D-S13] Subclinical thyroid dysfunction and fracture risk: a meta-analysis.** JAMA 2015;313(20):2055-2065. PMID 26010634；DOI `10.1001/jama.2015.5161`；PMCID PMC4729304
- 狀態：**PASS**（摘要完整，數字含分子分母）
- 查證路徑：Europe PMC `TITLE:"Subclinical thyroid dysfunction and fracture risk"` hitCount 2 → 取 JAMA 2015 那一筆。
- 可用的數字（**族群：13 個前瞻世代的個別參與者資料（美、歐、澳、日），一般人口，非甲狀腺癌**；**亞臨床甲亢定義 TSH <0.45 mIU/L**；**終點：骨折**）：
  - **70,298 人**，其中亞臨床甲狀腺低下 4,092（5.8%）、**亞臨床甲亢 2,219（3.2%）**；762,401 人年追蹤。
  - 事件：髖骨骨折 2,975 人（4.6%，12 篇）、任一骨折 2,528 人（9.0%，8 篇）、非脊椎骨折 2,018 人（8.4%，8 篇）、臨床脊椎骨折 296 人（1.3%，6 篇）。
  - **亞臨床甲亢 vs 正常（年齡性別校正）：髖骨骨折 HR 1.36（95% CI 1.13–1.64；2,082 人中 146 事件 vs 56,471 人中 2,534 事件）；任一骨折 HR 1.28（1.06–1.53）；非脊椎骨折 HR 1.16（0.95–1.41）；脊椎骨折 HR 1.51（0.93–2.45）。**
  - **TSH <0.10 mIU/L 這一格：髖骨骨折 HR 1.61（95% CI 1.21–2.15；510 人中 47 事件）；任一骨折 HR 1.98（1.41–2.78；212 人中 44 事件）；非脊椎骨折 HR 1.61（0.96–2.71）；脊椎骨折 HR 3.57（95% CI 1.88–6.78；162 人中 8 事件）。**
  - **內生性亞臨床甲亢（排除吃甲狀腺藥的人）：髖骨 HR 1.52（1.19–1.93）、任一骨折 1.42（1.16–1.74）、脊椎 1.74（1.01–2.99）。**
  - 亞臨床甲狀腺低下與骨折無關。
- **使用限制**：非甲狀腺癌族群；**脊椎骨折那個 3.57 只建立在 8 個事件上**，D1 若要寫必須連同分母一起寫。幾何檢查全部通過（例：√(1.88×6.78)=3.57 ✓）。

**[D-S14] Association Between Subclinical Thyroid Dysfunction and Fracture Risk.** JAMA network open 2022;5(11):e2240823. PMID 36346629；DOI `10.1001/jamanetworkopen.2022.40823`；PMCID PMC9644261（**OA**）
- 狀態：**PASS**
- 查證路徑：同 [D-S13] 的查詢結果第一筆。
- 可用的數字（**族群：ARIC 社區世代，未服用甲狀腺藥物、無骨折史**；**非甲狀腺癌**）：
  - **10,946 人**（女性 54.3%，平均年齡 57±5.7 歲），1987–1989 收案，追蹤至 2019；亞臨床甲亢定義 TSH <0.56 mIU/L。
  - 分布：正常 93.0%、亞臨床甲亢 2.6%、亞臨床低下 4.4%。中位追蹤 21 年，**3,556 件骨折（167.1／10,000 人年）**。
  - **亞臨床甲亢 vs 正常：校正 HR 1.34（95% CI 1.09–1.65）；亞臨床低下 HR 0.90（0.77–1.05）。**
- **使用限制**：同樣是內生性、非甲狀腺癌。

**[D-S15] Effect of TSH Suppression Therapy on Bone Mineral Density in Differentiated Thyroid Cancer: A Systematic Review and Meta-analysis.** The Journal of clinical endocrinology and metabolism 2021;106(12):3655-3667. PMID 34302730；DOI `10.1210/clinem/dgab539`
- 狀態：**PASS**
- 查證路徑：Europe PMC 標題精確查詢 hitCount 1。
- 可用的數字（**組織型：分化型**；**手術：全切後**；**終點：骨密度，不是骨折**）：
  - **17 篇觀察性研究，739 名病人與 1,085 名對照**。
  - **停經後女性：腰椎骨密度顯著下降，加權平均差 −0.03（−0.05, −0.02）**（單位為 g/cm²；全髖有相同趨勢）。
  - **停經前女性：腰椎 +0.04（0.02, 0.06）、股骨頸 +0.02（0.01, 0.04）——方向相反。**
  - **男性：各部位皆無顯著關聯。**
  - 結論逐字：「Evidence from observational studies suggests that postmenopausal women treated with TSH suppression therapy are at risk for lower BMD.」
- **注意**：這是**加權平均差（迴歸型、算術對稱）**，不是 HR/OR，CI 檢查用算術中點：(−0.05+−0.02)/2 = −0.035 ≈ −0.03 ✓。

**[D-S16] High Prevalence of Radiological Vertebral Fractures in Women on Thyroid-Stimulating Hormone-Suppressive Therapy for Thyroid Carcinoma.** The Journal of clinical endocrinology and metabolism 2018;103(3):956-964. PMID 29121201；DOI `10.1210/jc.2017-01986`
- 狀態：**PASS**
- 查證路徑：Europe PMC 標題精確查詢 hitCount 1。
- 可用的數字（**組織型：分化型**；**族群：179 名接受甲狀腺切除後長期服用左旋甲狀腺素的女性，中位年齡 59 歲，其中 178 人已停經**；**終點：影像學脊椎骨折**；**設計：橫斷面**）：
  - 依 TSH 目標分三組：**<0.5 mU/L（第 1 組，83 人）、0.5–1.0（第 2 組，50 人）、>1.0（第 3 組，46 人）**。
  - **整體脊椎骨折 51/179（28.5%）；第 1 組 44.6%、第 2 組 24.0%、第 3 組 4.3%（P<0.001）。**
  - 逐字：「VF prevalence was not significantly different among patients in group 1 with normal BMD, osteopenia, or osteoporosis」——**在 TSH <0.5 這一組，骨密度正常的人一樣會裂**。
  - 多變項獨立相關因子：TSH <1.0 mU/L、腰椎／股骨頸／全髖的骨質疏鬆診斷、年齡、左旋甲狀腺素使用期間。
- **這是 D1 最有畫面的一個數字**，但**只有女性、幾乎全為停經後、橫斷面**，不能講成「吃藥就會骨折」。

**[D-S17] Risk of Osteoporosis and Fractures in Patients with Thyroid Cancer: A Case-Control Study in U.S. Veterans.** The oncologist 2019;24(9):1166-1173. PMID 31164453；DOI `10.1634/theoncologist.2019-0234`；PMCID PMC6738319（**OA**）
- 狀態：**PASS**
- 查證路徑：Europe PMC 標題精確查詢 hitCount 1。
- 可用的數字（**族群：美國退伍軍人，以男性為主**；**組織型：甲狀腺癌，摘要未分型**；**終點：骨質疏鬆與骨折**）：
  - **甲狀腺癌 10,370 人 vs 配對對照 10,370 人**（依年齡、性別、體重、類固醇使用配對），2004–2013。
  - **骨質疏鬆：7.3% vs 5.3%，OR 1.33（95% CI 1.18–1.49）；骨折：未較多。**
  - 病人次群分析：**較低的 TSH 與骨質疏鬆相關（OR 0.93，95% CI 0.90–0.97，即 TSH 每上升一單位風險下降）**；女性 OR 4.24（3.53–5.10）；年齡 ≥85 歲 vs <50 歲 OR 17.18（11.12–26.54）；雄性素使用 OR 1.63（1.18–2.23）。
  - **血清 TSH 與骨折無關：OR 1.01（95% CI 0.96–1.07）。**
  - 作者結論逐字：「Osteoporosis, but not fractures, was more common in U.S. veterans with thyroid cancer than controls. Multiple factors may be contributory, with low TSH playing a small role.」
- **這一篇是 D1 誠實度的關鍵**：它告訴讀者「骨密度掉」與「真的骨折」不是同一件事，而且在以男性為主的族群裡 TSH 的角色很小。

### D1 專用：心血管死亡

**[D-S18] Long-term cardiovascular mortality in patients with differentiated thyroid carcinoma: an observational study.** Journal of clinical oncology 2013;31(32):4046-4053. PMID 24101052；DOI `10.1200/jco.2013.49.1043`
- 狀態：**PASS**
- 查證路徑：Europe PMC 標題精確查詢 hitCount 1。
- 可用的數字（**組織型：分化型**；**終點：心血管死亡與全因死亡**）：
  - **524 名分化型甲狀腺癌病人 vs 1,572 名同地區性別年齡配對對照**，平均年齡 49±14 歲；病人中位追蹤 8.5 年（IQR 4.1–15.9），對照 10.5 年。
  - 病人死亡 100 人（19.1%）：心血管 22（4.2%）、甲狀腺癌 39（7.4%）、其他／不明 39（7.4%）。對照死亡 85 人（5.4%）：心血管 24（1.5%）。
  - **校正年齡、性別、心血管危險因子後：心血管死亡 HR 3.35（95% CI 1.66–6.74）；全因死亡 HR 4.40（95% CI 3.15–6.14）。**（√(1.66×6.74)=3.34 ✓；√(3.15×6.14)=4.40 ✓）
  - **病人組內：每 TSH 幾何平均值下降 10 倍，心血管死亡的校正 HR 3.08（95% CI 1.32–7.21）。**（√(1.32×7.21)=3.09 ✓）
  - 作者結論逐字提到「supporting the current European Thyroid Association and the American Thyroid Association guidelines of tempering TSH suppression in patients with low risk of cancer recurrence」。
- **注意**：ATA 2025 內文把這一篇轉述成「survival in the patients was lower when the serum TSH was <0.02 mIU/L」——**摘要沒有這個 0.02 的切點**，該數字在本組可取得的範圍內無法驗證，**寫作組不得使用 <0.02 這個數字**，只能用「每下降 10 倍」的 HR 3.08。

**[D-S19] Association of Thyroid Hormone Treatment Intensity With Cardiovascular Mortality Among US Veterans.** JAMA network open 2022;5(5):e2211863. PMID 35552725；DOI `10.1001/jamanetworkopen.2022.11863`；PMCID PMC9099430（**OA**）
- 狀態：**PASS**
- 查證路徑：Europe PMC 標題精確查詢 hitCount 1。
- 可用的數字（**族群：所有接受甲狀腺素治療的退伍軍人，絕大多數不是甲狀腺癌**；**終點：心血管死亡**）：
  - **705,307 人**（男性 625,444 人，88.7%；中位年齡 67 歲），2004-01-01～2017-12-31，中位追蹤 4 年（IQR 2–9）。
  - **75,963 人（10.8%）死於心血管原因。**
  - **外源性甲狀腺亢進（TSH <0.1 mIU/L）：校正 HR 1.39（95% CI 1.32–1.47）；游離 T4 >1.9 ng/dL：HR 1.29（1.20–1.40）。**
  - **外源性甲狀腺低下也有害：TSH >20 mIU/L 的 HR 2.67（2.55–2.80）；游離 T4 <0.7 的 HR 1.56（1.50–1.63）。**
- **這篇對 D1 的價值在於後半**：吃太少的風險比吃太多還高。**但它不是甲狀腺癌族群**，引用時必須明說。

### D1 專用：半切病人的「補充 vs 抑制」

**[D-S20] Frequency of Thyroid Hormone Replacement After Lobectomy for Differentiated Thyroid Cancer.** Endocrine practice 2021;27(7):691-697. PMID 33642257；DOI `10.1016/j.eprac.2021.01.004`
- 狀態：**PASS**
- 查證路徑：Europe PMC 標題精確查詢 hitCount 1。
- 可用的數字（**組織型：分化型，低風險**；**手術：治療性單葉切除**；**放射碘：未做**）：
  - 單一機構 2016-01～2020-05，**115 人（91%）有術後 TSH 值**；其中 **97 人（84%）術後 TSH >2 mU/L**。
  - 中位追蹤 2.6 年；術後 TSH >2 的獨立預測因子只有術前 TSH（HR 1.53，P=0.003）。
  - **TSH >2 的 97 人中，66 人（68%）開始服用左旋甲狀腺素，中位於術後 74 天（IQR 41–126）；其中 51 人（77%）至少調整過一次劑量。**
- **使用限制**：這是「TSH 目標設在 0.5–2.0」的年代的資料，因此吃藥比例高；ATA 2025 現在把半切的目標改成「正常參考範圍」，所以 D1 要寫的是「目標訂在哪裡，決定你會不會需要吃藥」。ATA 2025 的 70–80% vs 20–30% 那一句（見 [D-S1]）可以搭配使用，但**那是指引自己的綜述，不是本篇的數字**。

### D2／D3 專用：甲狀腺球蛋白、抗體、治療反應與追蹤

**[D-S21] Serum Thyroglobulin Measurement Following Surgery Without Radioactive Iodine for Differentiated Thyroid Cancer: A Systematic Review.** Thyroid 2022;32(6):613-639. PMID 35412871；DOI `10.1089/thy.2021.0666`；PMCID PMC11265617
- 狀態：**PASS**
- 查證路徑：Europe PMC 標題精確查詢 hitCount 1。**這是 ATA 2025 參考文獻第 16 條，也是 Table 9「全切無 RAI」那一欄切點的直接來源。**
- 可用的數字（**依手術範圍與有無放射碘分層——正是第五、六條分界線**）：
  - **37 篇納入。分三種情境：單葉切除後 4 篇（N=561）；全切／近全切但未做放射碘 5 篇（N=751）；全切／近全切但在放射碘之前 28 篇（N=7,618）。**
  - **單葉切除後**逐字：「Following partial thyroidectomy, Tg measurement was not accurate for diagnosing recurrence or metastasis, or estimates were imprecise.」
  - **全切無放射碘**逐字：「evidence was limited due to few studies with very low rates of recurrence or metastasis, but indicated that Tg levels were usually stable and low.」
  - **切點**逐字：「Following total/near-total thyroidectomy, Tg levels using a cutoff of 1-2.5 ng/mL might identify patients at low risk for persistent or metastatic disease.」並自承「applicability to patients who do not undergo RAI is uncertain because patients selected for RAI are likely to represent a higher risk group」。
  - **證據品質**逐字：「The evidence was very low quality for all scenarios.」
- **D2 的核心支點**：可以直接寫「為什麼半切之後那個數字沒有一條線可以對」，而且有官方系統性回顧背書。

**[D-S22] Dynamic Risk Stratification in Patients with Differentiated Thyroid Cancer Treated Without Radioactive Iodine.** The Journal of clinical endocrinology and metabolism 2016;101(7):2692-2700. PMID 27023446；DOI `10.1210/jc.2015-4290`；PMCID PMC6287503
- 狀態：**PASS**
- 查證路徑：Europe PMC 標題精確查詢 hitCount 1。
- 可用的數字（**組織型：分化型**；**手術：單葉切除 187 人、全切 320 人**；**放射碘：全部未做**；**風險：低風險 85.4%、中風險 14.6%**；**終點：復發／持續性結構性疾病**）：
  - **507 人**，中位年齡 43.7 歲，88% 女性，中位追蹤 100.5 個月（24–510）。
  - **Excellent response（全切非刺激 Tg <0.2 ng/mL；單葉 <30 ng/mL，且 TgAb 陰性、影像陰性，n=326）→ 結構性疾病 0%。**
  - **Indeterminate（全切非刺激 Tg 0.2–5 ng/mL，TgAb 穩定或下降／影像非特異，n=152）→ 1.3%（2/152）。**
  - **Biochemical incomplete（全切 Tg >5 ng/mL；單葉 >30 ng/mL，或 Tg／TgAb 上升且影像陰性，n=19）→ 31.6%（6/19）。**
  - **Structural incomplete（n=10）→ 100%（10/10）。**
- **使用限制（見 ⚠D-12）**：**ATA 2025 沒有採用這一篇的切點**——2025 把全切無 RAI 的 excellent 改成 <2.5 ng/mL，並把單葉那兩格改成 N/A。D2 引用時必須標明「這是 2016 年單中心的提案版本」，**不可當作現行標準**。另注意 biochemical incomplete 那一格只有 19 人。

**[D-S23] Estimating risk of recurrence in differentiated thyroid cancer after total thyroidectomy and radioactive iodine remnant ablation: using response to therapy variables to modify the initial risk estimates predicted by the new American Thyroid Association staging system.** Thyroid 2010;20(12):1341-1349. PMID 21034228；DOI `10.1089/thy.2010.0178`；PMCID PMC4845674
- 狀態：**PASS**
- 查證路徑：Europe PMC 標題精確查詢 hitCount 1。
- 可用的數字（**組織型：濾泡細胞來源（分化型）**；**手術：全部全切**；**放射碘：全部做了殘存組織消融**；**風險分層：2009 版 ATA 三級**；**終點：persistent structural disease or recurrence**）：
  - **588 名成人，中位追蹤 7 年（1–15 年）**。
  - **初始分層：低風險 3%、中風險 21%、高風險 68% 有持續性結構疾病或復發。**
  - **前 2 年達 excellent response（stimulated Tg <1 ng/mL 且無結構性疾病）後重新分層：低風險 2%、中風險 2%、高風險 14%。**
  - **前 2 年為 incomplete response（suppressed Tg >1 ng/mL、stimulated Tg >10 ng/mL、Tg 上升，或前 2 年內找到結構性疾病）：低風險 13%、中風險 41%、高風險 79%。**
- **這是「反應分類」這整套系統的原始論文**，D2／D3 皆可引。注意它用的是 **2009 三級分層**與**刺激型 Tg**。

**[D-S24] Spontaneous remission in thyroid cancer patients after biochemical incomplete response to initial therapy.** Clinical endocrinology 2012;77(1):132-138. PMID 22248037；DOI `10.1111/j.1365-2265.2012.04342.x`
- 狀態：**PASS**
- 查證路徑：Europe PMC 標題精確查詢 hitCount 1。
- 可用的數字（**組織型：分化型**；**手術：全部全切**；**放射碘：全部做了消融**；**地點：巴西單一癌症中心**；**終點：復發／持續性疾病與重新分類為 NED**）：
  - **506 人，中位追蹤 10 年。**
  - ATA 分層驗證：低風險 13%、中風險 36%、高風險 68% 有復發／持續性疾病；達 excellent response 者降到 1.4%。
  - **最關鍵的一句（逐字）：「At the time of final follow-up, 34% of the biochemical incomplete response patients had been re-classified as having no evidence of disease (NED) without having received any additional therapy beyond continue levothyroxine suppression.」**
  - **對照（逐字）：「Conversely, even after additional therapies, only 9% of the patients with an incomplete structural response were eventually re-classified as NED.」**
- **D3 的主支點**：34% vs 9%，同一個世代、同一段追蹤、分母清楚。

**[D-S25] Even without additional therapy, serum thyroglobulin concentrations often decline for years after total thyroidectomy and radioactive remnant ablation in patients with differentiated thyroid cancer.** Thyroid 2012;22(8):778-783. PMID 22780333；DOI `10.1089/thy.2011.0522`
- 狀態：**PASS**
- 查證路徑：Europe PMC 標題精確查詢 hitCount 1。
- 可用的數字（**組織型：分化型**；**手術：全部全切**；**放射碘：全部做了消融**；**Tg 型態：抑制狀態下的非刺激 Tg**；**只納入「除了全切＋消融＋左旋甲狀腺素之外沒有再接受其他治療」的人**）：
  - **299 人**（69% 女性，中位年齡 46 歲，中位追蹤 7 年）。
  - **達到 Tg 谷值的時間：6 個月 58%、12 個月 75%；其餘 25% 需要 18 個月以上。**
  - 最終能降到 Tg <1 ng/mL 的 **223 人**之中：6 個月達標 81%、12 個月 91%、18 個月 94%。
  - **最關鍵：「In patients with a 6-month suppressed serum Tg of 1-5 ng/mL, 54% eventually developed a suppressed serum Tg of <1 ng/mL without additional therapy.」**
  - 作者結論逐字：「strong consideration should be given to continued observation without additional therapy in patients with well-differentiated thyroid cancer who have 6-month suppressed serum Tg values of 1-5 ng/mL without a structurally identifiable disease.」
- **D3 的第二支點**：「等」這件事本身是有證據的處置。

**[D-S26] Long-term consequence of elevated thyroglobulin in differentiated thyroid cancer.** Thyroid 2013;23(1):58-63. PMID 22973946；DOI `10.1089/thy.2011.0487`；PMCID PMC3539255
- 狀態：**PASS**（Europe PMC 摘要在 Results 段被截斷；已改由 `https://pmc.ncbi.nlm.nih.gov/articles/PMC3539255/` HTTP 200、38,410 bytes 取得全文，Results 與 Discussion 逐字讀完）
- 可用的數字（**組織型：分化型**；**手術：雙側甲狀腺切除**；**放射碘：全部做了殘存消融**；**Tg 型態：停藥刺激後的 stimulated Tg**；**族群：韓國，1995–2004**；**納入條件：消融後 1 年 sTg ≥2 ng/mL 且影像無結構性疾病（NSED）**）：
  - **186 人**（已排除 66 人有遠端轉移或甲狀腺床外攝取、76 人 1 年時已有結構性復發、6 人接受經驗性放射碘、21 人無後續 sTg）。
  - 依 1 年 sTg（sTg1）分三組：**A 組 2–4.9 ng/mL、B 組 5–19.9、C 組 ≥20。**
  - **自發生化緩解（BR，定義為 sTg <1 ng/mL）：A 組 41%、B 組 17%、C 組 1%。A 組達到 BR 的中位時間 69 個月。**
  - **結構性復發：A 組 19 人（24%）、B 組 20 人（30%）、C 組 20 人（50%）（log-rank 10.8, df=2, p=0.005）；C 組的中位復發時間 84 個月。全體 32% 出現結構性復發。**
  - 依 sTg 斜率分：**≥50% 下降（第 1 組）者達 BR 的中位時間 63 個月；<50% 下降或上升（第 2 組）中位約 117 個月**（log-rank 28.0, df=1, p<0.001）。復發率兩組亦顯著不同（log-rank 18.7, df=1, p<0.001）。
  - 引言中的文獻回顧逐字：「About 30%–68% of patients with elevated sTg 1 year after RRA have a subsequent decline in sTg concentration or an undetectable sTg.」
- **D3 的第三支點，也是最完整的一篇**：同時給了「自己會好」的比例與「會長出東西」的比例，且依起始 Tg 高低分層。**注意這是刺激型 Tg，不是現在常用的高敏感非刺激 Tg。**

**[D-S27] Unstimulated high-sensitive thyroglobulin is a powerful prognostic predictor in patients with thyroid cancer.** Clinical chemistry and laboratory medicine 2019;58(1):130-137. PMID 31444962；DOI `10.1515/cclm-2019-0654`
- 狀態：**PASS**
- 查證路徑：Europe PMC 標題精確查詢 hitCount 1。（**注意 Europe PMC 回傳的年份為 2019，卷期為 58(1)——跨年出版，引用時照抄。**）
- 可用的數字（**組織型：分化型**；**手術：近全切或全切**；**放射碘：有或無皆納入**；**終點：structural evidence of disease**）：
  - PROSPERO CRD42019125092；**10 篇、1,796 人**。
  - **服用左旋甲狀腺素下的高敏感 Tg（ON-T4 hs-Tg）測不到時，排除結構性疾病的陰性預測值：診斷情境 99.4%（95% CI 98.9–99.9；I²=13%）；預後情境 99.4%（95% CI 98.8–100；I²=0%）。**
  - 作者結論逐字：「A high level of evidence is provided to decrease the intensity and frequency of follow-up in those DTC patients having undetectable high-sensitive Tg.」
- **D2 的支點**：解釋「為什麼可以不必再打針刺激、也可以把追蹤拉長」。

**[D-S28] Diagnostic performance of 18F-FDG-PET/CT in DTC patients with thyroglobulin elevation and negative iodine scintigraphy: a meta-analysis.** European journal of endocrinology 2019;181(2):93-102. PMID 31117054；DOI `10.1530/eje-19-0261`
- 狀態：**PASS**
- 查證路徑：Europe PMC 標題精確查詢 hitCount 1。**這是 ATA 2025 參考文獻第 1024 條。**
- 可用的數字（**組織型：分化型**；**情境：Tg 上升但碘掃描陰性（TENIS）**；**終點：偵測復發／轉移**）：
  - 2001-01～2018-12，**17 篇、1,195 人**。
  - **以病人為單位：合併敏感度 0.86（95% CI 0.79–0.91）、特異度 0.84（95% CI 0.72–0.91）、診斷勝算比 31.00（95% CI 12.00–80.00）、AUC 0.91（95% CI 0.88–0.93）。**
  - **異質性高（敏感度 I²=80%、特異度 I²=82%）且可能有發表偏誤（P=0.01）。**
  - **有無 TSH 刺激沒有差別**（Z 檢定各項 P>0.05）。
- **注意**：診斷勝算比 31.00 的 CI 12.00–80.00，幾何中心 √(12×80)=30.98 ✓。

**[D-S29] Second Radioiodine Treatment: Limited Benefit for Differentiated Thyroid Cancer With Locoregional Persistent Disease.** The Journal of clinical endocrinology and metabolism 2018;103(2):469-476. PMID 29126111；DOI `10.1210/jc.2017-01790`
- 狀態：**PASS**
- 查證路徑：Europe PMC 標題精確查詢 hitCount 1。
- 可用的數字（**組織型：分化型**；**手術：全切**；**放射碘：至少兩次**；**排除有遠端轉移者**；**Tg 型態：stimulated Tg**）：
  - **164 人**（女性 103 人，平均年齡 46.6±17 歲），20 年間單一三級醫院。
  - **未先再手術就再次放射碘的 114 人中，53 人有結構性疾病**：1–2 年後資料足夠的 41 人裡，**10 人結構性惡化、5 人縮小／消失、26 人穩定**；刺激型 Tg 由 93.7±108 降到 102.2±124 ng/mL（無統計意義）。
  - **僅生化性持續者 61 人：刺激型 Tg 由 41.9±56 降到 24.6±54 ng/mL（P=0.003）。**
  - **先再手術再放射碘的 50 人：刺激型 Tg 無明顯變化，21 人（42%）1–2 年後影像上仍有病灶。**
  - **最終追蹤：164 人中有 63 人（38.4%）接受了額外治療，最後只有 56/164（34.1%）達到無疾病狀態。**
- **見 ⚠D-4(b)**：ATA 2025 對這一篇的轉述有兩處算術不一致，**本 brief 的數字是回原文重抄的**。

### D4 專用：放射碘無效之後的藥

**[D-S30] Sorafenib in radioactive iodine-refractory, locally advanced or metastatic differentiated thyroid cancer: a randomised, double-blind, phase 3 trial.（DECISION）** Lancet (London, England) 2014;384(9940):319-328. PMID 24768112；DOI（EPMC 回傳）`10.1016/s0140-6736(14)60421-9`；PMCID PMC4366116
- 狀態：**PASS（含全文）**
- 查證路徑：Europe PMC `EXT_ID:24768112&resultType=core` 取摘要；`https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4366116/fullTextXML` 回 **404**；改以瀏覽器 UA 打 `https://pmc.ncbi.nlm.nih.gov/articles/PMC4366116/`，**第一次回 reCAPTCHA 挑戰頁，等待後重試 HTTP 200、51,501 bytes**，Results 與 Table 2 逐字讀完。另打 `https://clinicaltrials.gov/api/v2/studies/NCT00984282?format=json` → PHASE3、COMPLETED、實際 417 人、主要完成 2012-08-31。
- 可用的數字（**組織型：分化型（中央判讀：乳突 57.0%／56.7%、濾泡 24.2%／26.7%、低分化 11.6%／7.6%、嗜酸性 1.0%／0——兩組分別）**；**RAI-refractory；96.6% 有遠端轉移**；**終點：PFS 為主**）：
  - 18 國 77 中心；意向治療 **417 人（sorafenib 207／安慰劑 210）**；安全性族群 416 人。納入條件含「serum thyroid-stimulating hormone concentration lower than 0.5 mIU/L」、過去 14 個月內 RECIST 惡化。
  - **中位 PFS 10.8 vs 5.8 個月，HR 0.59（95% CI 0.45–0.76；p<0.0001）。**（√(0.45×0.76)=0.585 ✓）
  - **總存活無顯著差異：HR 0.80（95% CI 0.54–1.19；P=0.14）；兩組中位 OS 皆未達到。**
  - **安慰劑組 150 人（71.4%）在惡化後轉換為 sorafenib。** 另 sorafenib 組 42 人（20.3%）、安慰劑組 18 人（8.6%）在試驗後接受其他抗癌治療。
  - **客觀反應率 12.2%（24/196）vs 0.5%（1/201），全部是部分反應；反應的中位持續時間 10.2 個月（95% CI 7.4–16.6）。**
  - **毒性**：任何不良事件 204/207（98.6%）vs 183/209（87.6%）。手足皮膚反應 76.3%（其中 grade 3 為 42 人／20.3%）、腹瀉 68.6%、落髮 67.1%、皮疹脫屑 50.2%。
  - **劑量中斷 66.2%（137/207）、減量 64.3%（133/207）、因不良事件停藥 18.8%（39/207）**；安慰劑組分別為 25.8%、9.1%、3.8%。**手足皮膚反應是停藥最常見的原因（5.3%，11/207）。**
  - **嚴重不良事件 77 人（37.2%）vs 55 人（26.3%）**——見 ⚠D-4(c)，**不是「grade 3 以上」**。
  - 另有一句 D4 可用：TSH 上升超過 0.5 mIU/L 者占 33.3%（69/207）——**吃這個藥會把甲狀腺素的劑量弄亂。**

**[D-S31] Lenvatinib versus placebo in radioiodine-refractory thyroid cancer.（SELECT）** The New England journal of medicine 2015;372(7):621-630. PMID 25671254；DOI（EPMC 回傳）`10.1056/nejmoa1406470`
- 狀態：**PASS（僅摘要；無 PMCID）**
- 查證路徑：Europe PMC `TITLE:"Lenvatinib versus placebo in radioiodine-refractory thyroid cancer"` hitCount 1。另打 `https://clinicaltrials.gov/api/v2/studies/NCT01321554?format=json` → PHASE3、COMPLETED、實際 392 人、主要完成 2013-11-15。
- 可用的數字（**組織型：分化型**；**RAI-refractory、進展性**；**終點：PFS 為主**）：
  - **392 人隨機（lenvatinib 261／安慰劑 131，2:1）**；lenvatinib 24 mg/日、28 天一週期。
  - **中位 PFS 18.3 vs 3.6 個月，HR 0.21，99% CI 0.14–0.31（p<0.001）。**（**見 ⚠D-5：是 99% 不是 95%。**）
  - **反應率 64.8%（4 個完全反應、165 個部分反應）vs 1.5%（p<0.001）。**
  - **兩組中位總存活皆未達到。**
  - 任一等級的治療相關不良事件中超過 40% 者：高血壓 67.8%、腹瀉 59.4%、疲倦或無力 59.0%、食慾下降 50.2%、體重下降 46.4%、噁心 41.0%。
  - **因不良事件停藥：lenvatinib 37 人（14.2%）vs 安慰劑 3 人（2.3%）。**
  - **治療期間 20 例死亡中，6 例被判定與藥物有關。**
- **ATA 2025 另轉述但本組未能回原文驗證的數字（寫作組不得使用）**：安慰劑組 83% 交叉、交叉後中位 PFS 10.1 個月與 ORR 52.3%、劑量中斷 82.4%、減量 67.8%、嚴重不良事件 49.8%、PFS 更新為 19.4 vs 3.7 個月。**這幾個數字分別出自 SELECT 原文正文與 Gianoukakis 2018（ATA ref 1195），本組僅取得書目未取得內文。**

**[D-S32] Cabozantinib for radioiodine-refractory differentiated thyroid cancer (COSMIC-311): a randomised, double-blind, placebo-controlled, phase 3 trial.** The Lancet. Oncology 2021;22(8):1126-1138. PMID 34237250；DOI `10.1016/s1470-2045(21)00332-6`
- 狀態：**PASS（僅摘要）**
- 查證路徑：Europe PMC 標題精確查詢 hitCount 1；`https://clinicaltrials.gov/api/v2/studies/NCT03690388?format=json` → PHASE3、ACTIVE_NOT_RECRUITING、實際 187 人、主要完成 2020-08-19。
- 可用的數字（**組織型：分化型（乳突／濾泡及其亞型）**；**≥16 歲；曾用 lenvatinib 或 sorafenib 並惡化，最多兩線 VEGFR TKI**）：
  - 25 國 164 中心，2019-02-27～2020-08-18，**187 人（cabozantinib 125／安慰劑 62，2:1）**。資料截止時 ITT 中位追蹤 6.2 個月。
  - **ORR（前 100 名隨機者）：10/67（15%，99% CI 5.8–29.3）vs 0/33（0%，0–14.8），p=0.028——未達預設顯著水準（α=0.01）。**
  - **中位 PFS 未達到（96% CI 5.7–無法估計）vs 1.9 個月（1.8–3.6），HR 0.22（96% CI 0.13–0.36；p<0.0001）。**
  - **Grade 3 或 4 不良事件 71/125（57%）vs 16/62（26%）**；最常見手足症候群 13（10%）vs 0、高血壓 11（9%）vs 2（3%）、疲倦 10（8%）vs 0。嚴重治療相關不良事件 20（16%）vs 1（2%）。**無治療相關死亡。**

**[D-S33] Cabozantinib for previously treated radioiodine-refractory differentiated thyroid cancer: Updated results from the phase 3 COSMIC-311 trial.** Cancer 2022;128(24):4203-4212. PMID 36259380；DOI `10.1002/cncr.34493`；PMCID PMC10092751（**OA**）
- 狀態：**PASS**（另有 Erratum：Cancer 2023;129(5):807，PMID 36637398，DOI `10.1002/cncr.34638`，**本組未取得其內容，僅確認存在**）
- 查證路徑：Europe PMC `TITLE:"COSMIC-311"` hitCount 7 → `EXT_ID:36259380&resultType=core`。
- 可用的數字（同上族群）：
  - 資料截止 2021-02-08，**258 人隨機（cabozantinib 170／安慰劑 88），中位追蹤 10.1 個月**。
  - **中位 PFS 11.0 個月（96% CI 7.4–13.8）vs 1.9 個月（96% CI 1.9–3.7），HR 0.22（96% CI 0.15–0.32；p<0.0001）。**
  - **ORR 11.0%（95% CI 6.9–16.9）vs 0%（0.0–4.1），p=0.0003；cabozantinib 組有 1 例完全反應。**
  - **40 名安慰劑病人轉換為 cabozantinib。**
  - **Grade 3/4 治療中出現的不良事件 62% vs 28%**；最常見高血壓 12% vs 2%、手足症候群 10% vs 0%、疲倦 9% vs 0%。**無 grade 5 治療相關事件。**
- **D4 用這一筆取代 [D-S32] 的「中位 PFS 未達到」。** ATA 2025 轉述的「劑量減量 56%、5% 因不耐受停藥」本組未能在可取得的摘要中驗證，**寫作組不得使用**。

**[D-S34] Efficacy of Selpercatinib in RET-Altered Thyroid Cancers.（LIBRETTO-001）** The New England journal of medicine 2020;383(9):825-835. PMID 32846061；DOI `10.1056/nejmoa2005651`；PMCID PMC10777663
- 狀態：**PASS（僅摘要）**
- 查證路徑：Europe PMC `TITLE:"Efficacy of Selpercatinib in RET-Altered Thyroid Cancers"` hitCount 1。（Europe PMC 回傳的 title 含 `<i>` 標籤，逐字標題應為「Efficacy of Selpercatinib in RET-Altered Thyroid Cancers.」）
- 可用的數字（**分兩種完全不同的病：RET 點突變的髓質癌 vs RET 融合的非髓質甲狀腺癌**）：
  - **RET 融合陽性甲狀腺癌（曾治療過）19 人：反應率 79%（95% CI 54–94）；1 年無惡化存活 64%（95% CI 37–82）。**
  - 對照（**髓質癌，不屬 D4**）：曾用 vandetanib／cabozantinib 的 RET 突變髓質癌前 55 人反應率 69%（95% CI 55–81），1 年 PFS 82%（69–90）；未曾用者 88 人反應率 73%（62–82），1 年 PFS 92%（82–97）。
  - **全部 531 名受試者中，12 人（2%）因藥物相關不良事件停藥。** Grade ≥3 最常見：高血壓 21%、ALT 上升 11%、AST 上升 9%、低血鈉 8%、腹瀉 6%。
  - ATA 2025 補述該 19 人的組成（**ATA 轉述，本組未在摘要中驗證**）：13 例乳突癌、3 例低分化癌、1 例嗜酸性癌，另有 2 例未分化癌；6 人（32%）有腦轉移。**寫作組若要寫組成，須寫成「不到二十個人」而不給細項。**
- **使用限制**：**n=19，單臂，非隨機。** D4 必須把這件事寫出來。

**[D-S35] Pralsetinib for patients with advanced or metastatic RET-altered thyroid cancer (ARROW): a multi-cohort, open-label, registrational, phase 1/2 study.** The lancet. Diabetes & endocrinology 2021;9(8):491-501. PMID 34118198；DOI `10.1016/s2213-8587(21)00120-0`；PMCID PMC13224057
- 狀態：**PASS**
- 查證路徑：Europe PMC 標題精確查詢 hitCount 1。
- 可用的數字：
  - 13 國 71 中心，2017-03-17～2020-05-22；**RET 突變髓質癌 122 人、RET 融合陽性甲狀腺癌 20 人**。
  - **RET 融合陽性甲狀腺癌中有可測量病灶者 9 人：反應率 8/9＝89%（95% CI 52–100）。**
  - （髓質癌對照，不屬 D4：未曾治療者 15/21＝71%（95% CI 48–89）；曾用 cabozantinib／vandetanib 者 33/55＝60%（46–73）。）
  - **全部 142 名 RET 異常甲狀腺癌病人的 grade ≥3 治療相關不良事件（≥10%）：高血壓 24 人（17%）、嗜中性球低下 19（13%）、淋巴球低下 17（12%）、貧血 14（10%）。嚴重治療相關不良事件 21 人（15%），最常見肺炎 5 人（4%）。5 人（4%）因治療相關事件停藥。1 人（1%）死於治療相關不良事件。**
- **使用限制**：**分母是 9 人。** 另 ATA 2025 提到 pralsetinib 原本對髓質癌的加速核准後來被撤回（逐字：「its approval was subsequently withdrawn because a required confirmatory phase study would not be feasible」）——**這一點只能引 ATA 的敘述，本組未取得 FDA 原始公告。**

**[D-S36] Phase 3 Trial of Selpercatinib in Advanced RET-Mutant Medullary Thyroid Cancer.（LIBRETTO-531）** The New England journal of medicine 2023;389(20):1851-1861. PMID 37870969；DOI `10.1056/nejmoa2309719`
- 狀態：**PASS，但依 ⚠D-8「不屬於 D4 的病」**
- 查證路徑：Europe PMC `TITLE:"selpercatinib" AND JOURNAL:"The New England journal of medicine"` hitCount 11 → `EXT_ID:37870969`。另有試驗設計論文（Future Oncol 2022;18(28):3143-3150，PMID 35969032）與病人回報耐受性次要分析（Thyroid 2025;35(10):1162-1172，PMID 40828665）。
- 可用的數字（**組織型：髓質癌（MTC），RET 點突變，第一線**）：291 人隨機；中位追蹤 12 個月；**中位 PFS 未達到 vs 16.8 個月（95% CI 12.2–25.1），HR 0.28（95% CI 0.16–0.48；P<0.001）**；12 個月 PFS 86.8% vs 65.7%；反應率 69.4% vs 38.8%；因不良事件停藥 4.7% vs 26.8%。
- **使用限制**：**D4（分化型）不得引用這些數字。** 保留給 E1。

**[D-S37] Efficacy and safety of larotrectinib in patients with TRK fusion-positive thyroid carcinoma.** European journal of endocrinology 2022;186(6):631-643. PMID 35333737；DOI `10.1530/eje-21-1259`；PMCID PMC9066591（**OA**）
- 狀態：**PASS**
- 查證路徑：Europe PMC 標題精確查詢 hitCount 1。
- 可用的數字（**組織型混合，且已分開報告——正好符合第一條分界線**）：
  - 三個 1/2 期試驗（NCT02576431、NCT02122913、NCT02637687）的合併資料，資料截止 2020-07。
  - **29 人**（中位年齡 60 歲，範圍 6–80）：**乳突癌 20 人（69%）、濾泡癌 2 人（7%）、未分化癌 7 人（24%）。**
  - **28 名可評估者整體反應率 71%（95% CI 51–87）**：完全反應 2 人（7%）、部分反應 18 人（64%）、疾病穩定 4 人（14%）、疾病惡化 3 人（11%）、1 人（4%）未定。
  - **分開報：乳突／濾泡癌 86%（95% CI 64–97）；未分化癌 29%（95% CI 4–71）。**
  - 中位反應時間 1.87 個月（1.64–3.68）。**24 個月的反應持續率 81%、PFS 率 69%、OS 率 76%。**
  - 治療相關不良事件主要為 grade 1–2。
- **注意**：ATA 2025 說「In the 21 patients with evaluable DTC, the objective response rate was 86%」——與原文的 86%（95% CI 64–97）一致，但原文分母為乳突＋濾泡，**未分化癌那 7 人必須另外算**。

**[D-S38] Entrectinib in patients with advanced or metastatic NTRK fusion-positive solid tumours: integrated analysis of three phase 1-2 trials.** The Lancet. Oncology 2020;21(2):271-282. PMID 31838007；DOI `10.1016/s1470-2045(19)30691-6`；PMCID PMC7461630
- 狀態：**PASS（僅摘要）**
- 查證路徑：Europe PMC 標題精確查詢 hitCount 1。（**注意：ATA 2025 參考文獻第 1245 條印的 DOI 與 Europe PMC 回傳不同；以 Europe PMC 為準。**）
- 可用的數字（**不分癌別的籃子試驗，甲狀腺癌只是其中一格**）：
  - ALKA-372-001、STARTRK-1、STARTRK-2 合併；資料截止 2018-05-31；**療效可評估族群 54 名成人，涵蓋 10 種腫瘤型別、19 種組織學**。
  - **31/54（57%，95% CI 43.2–70.8）有客觀反應**：完全反應 4 人（7%）、部分反應 27 人（50%）。**中位反應持續 10 個月（95% CI 7.1–無法估計）。** 中位追蹤 12.9 個月。
  - Grade 3/4 治療相關不良事件最常見：體重增加（NTRK 融合安全性族群 68 人中 7 人／10%）、貧血（8 人／12%）。無治療相關死亡。
- **ATA 2025 轉述但本組無法在摘要中驗證（寫作組不得使用）**：「五名甲狀腺癌受試者中一人達部分反應」、以及 2022 年 ASCO 摘要（ATA ref 1246）的 61.3% 反應率與 16 名甲狀腺癌中 10 人反應。**後者只有會議摘要，依鐵則不引用。**

**[D-S39] Efficacy and safety of dabrafenib plus trametinib in adults with differentiated thyroid cancer: a randomised, double-blind, placebo-controlled, phase 3 trial.** The Lancet. Oncology 2026;27(8):994-1003. PMID 42442381；DOI `10.1016/s1470-2045(26)00133-6`
- 狀態：**PASS（僅摘要，非 OA）**
- 查證路徑：Europe PMC `TITLE:"dabrafenib" AND TITLE:"trametinib" AND TITLE:"thyroid"` hitCount 48 → 命中本篇；`https://clinicaltrials.gov/api/v2/studies/NCT04940052?format=json` → PHASE3、ACTIVE_NOT_RECRUITING、實際 153 人、主要完成 2025-01-22（ACTUAL）、hasResults=true。
- 可用的數字（**組織型：分化型**；**BRAF V600E 陽性、RAI-refractory、曾接受治療（previously treated）**；**終點：PFS 為主**）：
  - 11 國 42 中心，2021-12-10～2024-05-09；**153 人（dabrafenib+trametinib 101／安慰劑 52，2:1）**；男 73（48%）女 80（52%）；平均年齡 62.6±10.2 歲；**白人 18（12%）、亞洲人 131（86%）、黑人 3（2%）、多重族裔 1（1%）**。
  - 中位追蹤 17.4 個月（IQR 10.5–25.2）。
  - **中位 PFS 12.8 個月（95% CI 10.2–21.2）vs 3.7 個月（2.3–7.5），分層 HR 0.38（95% CI 0.25–0.57；p<0.0001）。**（√(0.25×0.57)=0.377 ✓）
  - **客觀反應率 58/101（57%）vs 2/52（4%），分層差值 53%（95% CI 42–64，p<0.0001）。**
  - **總存活期中分析未達顯著：分層 HR 0.66（95% CI 0.36–1.19；p=0.083）。**
  - **毒性**：最常見 grade ≥3 事件為肺炎（8/101，8% vs 1/52，2%）；任一等級嚴重不良事件 43（43%）vs 13（25%）；**因不良事件停藥 8（8%）vs 3（6%）**；最常見不良事件為發燒（48 人，48%）；漿液性視網膜病變 7（7%）vs 0。**Grade 5 事件：肺炎 2、心搏過緩 1、腦血管意外 1、敗血性休克 1、鱗狀細胞癌 1（皆在試驗組）；安慰劑組心包積液與多重器官衰竭各 1。試驗組有 1 例（1%）治療中死亡（腦血管意外）被判定與試驗藥有關。**
  - 作者結論逐字：「These findings support the **second-line** use of dabrafenib plus trametinib in patients with radioactive iodine-refractory BRAFV600E-positive differentiated thyroid cancer.」
- **注意族裔組成 86% 亞洲人**——這一點對台灣讀者反而是好消息，但不能寫成「特別適合台灣人」。

### D4 專用：再分化

**[D-S40] A Phase II Redifferentiation Trial with Dabrafenib-Trametinib and 131I in Metastatic Radioactive Iodine Refractory BRAF p.V600E-Mutated Differentiated Thyroid Cancer.（MERAIODE，BRAF 世代）** Clinical cancer research 2023;29(13):2401-2409. PMID 37074727；DOI `10.1158/1078-0432.ccr-23-0046`
- 狀態：**PASS**
- 查證路徑：Europe PMC `(AUTH:"Leboulleux S") AND TITLE:"Redifferentiation"` hitCount 6 → `EXT_ID:37074727&resultType=core`。**注意：ATA 2025 用單一參考文獻（第 1340 條，即 RAS 世代那篇）同時支撐 BRAF 與 RAS 兩個世代的敘述；BRAF 世代另有本篇獨立論文。**
- 可用的數字（**組織型：分化型**；**BRAF p.V600E**；**RAI-refractory 且 18 個月內 RECIST 惡化、無 >3 cm 病灶**；**單臂第二期**）：
  - **收 24 人，21 人可於 6 個月評估。** 給 dabrafenib＋trametinib 42 天，第 28 天做 rhTSH 刺激的診斷性全身掃描，第 35 天給 **5.5 GBq（150 mCi）** 放射碘。
  - **異常碘攝取比例：治療前掃描 5%、用藥 4 週後掃描 65%、治療後掃描 95%。**
  - **6 個月：部分反應 38%、疾病穩定 52%、疾病惡化 10%。**
  - 10 人接受第二個療程，6 個月時觀察到 1 個完全反應與 6 個部分反應。
  - **中位 PFS 未達到；12 個月 PFS 82%、24 個月 68%。24 個月時 1 人因疾病惡化死亡。**
  - **96% 的病人出現不良事件，7 人出現 10 件 grade 3–4 事件。**

**[D-S41] MERAIODE: A Phase II Redifferentiation Trial with Trametinib and 131I in Metastatic Radioactive Iodine Refractory RAS Mutated Differentiated Thyroid Cancer.** Thyroid 2023;33(9):1124-1129. PMID 37350119；DOI `10.1089/thy.2023.0240`
- 狀態：**FAIL（僅書目，內容一字未取得）**
- 理由：Europe PMC 回傳的 `abstractText` 為空、非 OA、無 PMCID；`pmc.ncbi.nlm.nih.gov` 無對應頁。
- 可寫的只有：這篇論文存在，是 MERAIODE 的 RAS 世代。**ATA 2025 轉述「10 名可於 6 個月評估者中 2 人達部分反應」——屬 ATA 轉述，寫作組不得使用。**

**[D-S42] Results of the SEL-I-METRY Phase II Trial on Resensitization of Advanced Iodine Refractory Differentiated Thyroid Cancer to Radioiodine Therapy.** Thyroid 2023;33(9):1119-1123. PMID 37565288；DOI `10.1089/thy.2022.0707`；PMCID PMC10516223（**OA，CC-BY**）
- 狀態：**PASS（含全文）**
- 查證路徑：Europe PMC `TITLE:"Results of the SEL-I-METRY Phase II Trial"` hitCount 2（本篇＋更正啟事）；Europe PMC 的 `abstractText` 為空、`fullTextXML` 回傳的是更正啟事的 metadata；改以瀏覽器 UA 打 `https://pmc.ncbi.nlm.nih.gov/articles/PMC10516223/`（**第一次回 reCAPTCHA，等待 20 秒後重試 HTTP 200、36,414 bytes**）取得正文與 Table 1。**更正啟事**（Thyroid 2023;33(11):1385，PMID 37856079，PMCID PMC11074422）已逐字讀完，**內容僅為改為開放取用與加註 CC-BY 授權，未更動任何數據**。
- 可用的數字（**組織型：乳突癌 11 人（39.3%）、濾泡癌 17 人（60.7%）**；**RAI-refractory 且 12 個月內 RECIST 惡化**；**單臂多中心第二期，英國，ISRCTN17468602**）：
  - 設計需要 **38 名接受碘治療者**才能偵測 12 個月 PFS 由 25% 提升到 44%（HR 0.6），假設 60% 攝碘率 → 需收 60 人。
  - **2017-03-28 開始收案；獨立資料監測委員會在第 26 人時發現攝碘率只有約 40%，加上收案太慢，2019-08-15 提早關閉，共登錄 30 人，分析 28 人。**
  - **11/28（39.3%，CI 21.5–59.4）有足夠的 123I 攝取增加；10 人被建議進一步放射碘，1 人因與治療無關的嚴重不良事件未接受；最終 9/28（32.1%）真的接受了 5.5 GBq 放射碘。**
  - **主要終點（只算這 9 人）：12 個月 PFS 64.8%（CI 25.3–87.2；80% CI 39.8–81.5）。** 分析時 7 人（77.8%）已惡化。
  - **9 名碘治療者中只有 4 人（44.4%）吃完全部 selumetinib 劑量**；非碘治療組 19 人中只有 1 人（5.3%）吃完。**減量或漏服有 79.3% 是因為不良事件或毒性。**
  - 7 件嚴重不良事件發生於 7 人（碘治療組 1、非碘治療組 6），3 件與 selumetinib 有關。**無治療相關死亡。**
- **這是 D4 最誠實的一筆**：主要終點的分母只有 9 個人，信賴區間 25.3–87.2。**寫作組若要寫 64.8%，必須同時寫出 9 這個分母與那個區間。**

**[D-S43] Selumetinib Plus Adjuvant Radioactive Iodine in Patients With High-Risk Differentiated Thyroid Cancer: A Phase III, Randomized, Placebo-Controlled Trial (ASTRA).** Journal of clinical oncology 2022;40(17):1870-1878. PMID 35192411；DOI `10.1200/jco.21.00714`；PMCID PMC9851689
- 狀態：**PASS**
- 查證路徑：Europe PMC 標題精確查詢 hitCount 1。
- 可用的數字（**組織型：分化型**；**族群：術後初次治療失敗高風險（原發 >4 cm；或明顯甲狀腺外侵犯 T4；或 N1a/N1b 且至少一顆 ≥1 cm 或 ≥5 顆任意大小的轉移淋巴結）**；**未依基因篩選**；**終點：18 個月完全緩解率**）：
  - 國際、第三期、隨機（2:1）、雙盲、安慰劑對照；selumetinib 75 mg 一天兩次約 5 週，第 29–31 天給 rhTSH 後放射碘。
  - **完全緩解率：selumetinib 62/154（40%）vs 安慰劑 30/79（38%）；勝算比 1.07（95% CI 0.61–1.87）；P=0.8205 → 陰性。**（√(0.61×1.87)=1.068 ✓）
  - **治療相關 grade ≥3 不良事件：selumetinib 25/154（16%），安慰劑 0；最常見為痤瘡樣皮膚炎 11 人（7%）。無治療相關死亡。**
- **這是再分化領域唯一完成的第三期試驗，結果是陰性的。**

**[D-S44] Redifferentiation therapy in unresectable or metastatic radioactive iodine refractory thyroid cancer: an International Thyroid Oncology Group statement.** The lancet. Diabetes & endocrinology 2025;13(6):516-527. PMID 40318680；DOI `10.1016/s2213-8587(25)00064-6`；PMCID PMC13011886（**OA**）
- 狀態：**PASS**
- 查證路徑：Europe PMC `(AUTH:"Leboulleux S") AND TITLE:"Redifferentiation"` hitCount 6 → `EXT_ID:40318680&resultType=core`。
- 可用的逐字句（**組織型：濾泡細胞來源的甲狀腺癌**）：
  - 「The iodine uptake restoration ranges from 33% to 95%, and tumour response rates from 11% to 80%.」
  - 「There is substantial variability between trials with regards to inclusion criteria, duration of redifferentiation drug therapy, activity of radioactive iodine, and use of dosimetry.」
  - **「Randomised studies are missing to clearly establish the effectiveness and applicability of redifferentiation. Thus, long-term studies are needed to establish the most effective redifferentiation protocols.」**
- **D4 再分化段落的定位句就用這三句。**

**[D-S45] Selumetinib-enhanced radioiodine uptake in advanced thyroid cancer.** The New England journal of medicine 2013;368(7):623-632. PMID 23406027；DOI `10.1056/nejmoa1209288`；PMCID PMC3615415
- 狀態：**PASS（僅摘要）**
- 查證路徑：Europe PMC 標題精確查詢 hitCount 1。
- 可用的數字（**組織型：轉移性甲狀腺癌**；**單臂、單中心、20 人可評估**）：
  - 篩 24 人，**20 人可評估**，中位年齡 61 歲（44–77），男性 11 人；**9 人 BRAF 突變、5 人 NRAS 突變**。
  - **selumetinib 提高 20 人中 12 人的 124I 攝取（BRAF 9 人中 4 人、NRAS 5 人中 5 人）。**
  - **12 人中有 8 人達到可以給治療劑量的劑量計量門檻（≥2,000 cGy），其中包括全部 5 名 NRAS 突變者。**
  - **接受放射碘的 8 人：5 人確認部分反應、3 人疾病穩定；全部病人的甲狀腺球蛋白下降（平均下降 89%）。**
  - **無 grade ≥3 被判定與 selumetinib 有關的毒性。1 人在放射碘治療 51 週後被診斷為骨髓化生不良症候群，並進展為急性白血病。**
- **最後那一句必須寫。** 這是 D4「再分化還在試驗階段」最具體的安全性提醒。

### D5 專用：體外放射線治療

**[D-S46] Clinical outcomes of adjuvant external-beam radiotherapy for differentiated thyroid cancer - results after 874 patient-years of follow-up in the MSDS-trial.** Nuklearmedizin. Nuclear medicine 2009;48(3):89-98; quiz N15. PMID 19322503；DOI `10.3413/nukmed-0221`
- 狀態：**PASS（僅摘要）**
- 查證路徑：Europe PMC `TITLE:"Clinical outcomes of adjuvant external-beam radiotherapy for differentiated thyroid cancer"` hitCount 1。另打 `https://clinicaltrials.gov/api/v2/studies/NCT00144079?format=json` → 官方標題「Phase 3 Trial of Adjuvant External Beam Radiotherapy for Locally Invasive Differentiated Thyroid Carcinoma」、PHASE3、COMPLETED、預計 500 人、2000-01 開始、主辦 University Hospital Muenster、地點德國與奧地利、主要終點為 time to local or distant failure 與 cancer-related mortality。
- 可用的數字（**組織型：乳突 90%、濾泡 10%**；**期別：pT4，UICC 1997 版——⚠ 這是很舊的版本，不可與 AJCC 第八版互譯**；**無已知遠端轉移**；**全部接受甲狀腺切除＋131I＋TSH 抑制**）：
  - **原設計為前瞻多中心隨機試驗；2003 年 4 月，在當時 311 人中只有 45 人同意被隨機分配之後，改為前瞻性世代研究。**
  - **422 人中 351 人符合納入條件。** 平均年齡 48±12 歲，男性 25%。
  - **被隨機分配或被指派到放療組的 47 人中，只有 26 人真的接受了放療。**
  - 平均追蹤 930 天。**依實際治療分析：放療組 25/26（96%）達完全緩解，未放療組 86%。復發率 0% vs 3%。**
  - **嚴重慢性放療毒性 1/26。**
  - 作者結論逐字：「The MSDS trial showed low mortality and recurrence rates and a weak benefit of RTx in terms of local control that did however not reach statistical significance. **Routine RTx in locally invasive DTC can no longer be recommended.**」
- **這是 D5 的核心**：唯一啟動過的隨機試驗，而它失敗的原因是**病人不願意被隨機分配**。⚠D-10 已記錄 ATA 2025 對這一段的轉述與原文形狀不同。

**[D-S47] Adjuvant external beam radiotherapy for locally invasive papillary thyroid cancer.** Head & neck 2019;41(6):1719-1724. PMID 30620424；DOI `10.1002/hed.25639`
- 狀態：**PASS（僅摘要）**
- 查證路徑：Europe PMC 標題精確查詢 hitCount 1。
- 可用的數字（**組織型：乳突癌**；**期別：T4，SEER 1988–2013，⚠ 摘要未說明用第幾版 AJCC**；**終點：OS 與 DSS**；**設計：傾向分數分析，回溯**）：
  - **870 例已手術切除的 T4 乳突癌。**
  - **輔助性 EBRT 與較差的總存活相關：HR 1.60（95% CI 1.18–2.16）；與較差的疾病特異性存活相關：HR 1.58（95% CI 1.09–2.30）。**（√(1.18×2.16)=1.596 ✓；√(1.09×2.30)=1.583 ✓）
  - **僅限有明顯甲狀腺外侵犯者的次群：OS HR 1.53（95% CI 1.04–2.25）；DSS HR 1.57（95% CI 0.99–2.50，不顯著）。**
  - 作者結論逐字：「Adjuvant EBRT, in the initial management of locally invasive papillary thyroid cancer, was not associated with a survival benefit.」
- **使用限制見 ⚠D-11。** 這個數字的方向最可能反映的是「被送去放療的人本來就比較嚴重」，**不可以寫成「放療會害死人」。**

**[D-S48] Intensity-modulated radiation therapy and doxorubicin in thyroid cancer: A prospective phase 2 trial.** Cancer 2021;127(22):4161-4170. PMID 34293201；DOI `10.1002/cncr.33804`；PMCID PMC9455581
- 狀態：**PASS**
- 查證路徑：Europe PMC 標題精確查詢 hitCount 1。
- 可用的數字（**組織型：非未分化癌、非髓質癌的甲狀腺癌**；**情境：肉眼殘存或無法切除**；**單中心、非隨機第二期，NCT01882816**）：
  - **27 人**：無法切除 12 人（44.4%）、肉眼殘存 15 人（55.6%）。中位追蹤 45.6 個月（IQR 42.0–51.6）。
  - **2 年局部區域 PFS 79.7%、2 年 OS 77.3%。**
  - **grade ≥3 的急性與晚期毒性合計 33.4%。**
  - 治療後 12 個月客觀吞嚥功能（改良鋇劑吞嚥檢查）無顯著差異；生活品質先下降、6 個月回到基準、之後改善。
  - **事後分析：合併化療的 IMRT 2 年局部區域失敗率為 0，單獨 IMRT 為 50%（P=.001）**；合併化療組 grade ≥2 的急性皮膚炎、黏膜炎、吞嚥困難較多，長期毒性、功能與生活品質無差異。
- **注意**：前 8 人是單用 IMRT，之後修改計畫才加上每週 doxorubicin（19 人）——**兩組不是隨機分派的**。

**[D-S49] Postoperative simultaneous integrated boost-intensity modulated radiation therapy for patients with locoregionally advanced papillary thyroid carcinoma: preliminary results of a phase II trial and propensity score analysis.** The Journal of clinical endocrinology and metabolism 2015;100(3):1009-1017. PMID 25581596；DOI `10.1210/jc.2014-3242`
- 狀態：**PASS（僅摘要）**
- 查證路徑：Europe PMC 標題精確查詢 hitCount 1。
- 可用的數字（**組織型：乳突癌**；**期別：pT4 或 N1b，⚠ 摘要未說明 AJCC 版本**；**全部先手術＋放射碘消融**；**終點：locoregional relapse-free survival**）：
  - 單中心；放療組來自一個第二期試驗，對照組為同期未放療者；**全部 201 人，傾向分數配對後 118 人。**
  - **配對後 4 年局部區域無復發存活：放療組 100% vs 未放療組 84.6%（P=.002）。**
  - **無 grade ≥3 毒性，所有病人都照計畫完成。**
  - ATA 2025 另述「4-year overall survival was 100% in both」（**ATA 轉述，本組未在摘要中驗證**）。
- **使用限制**：**不是隨機試驗**，是單臂第二期＋傾向分數配對的歷史對照。D5 引用時必須明講。

**[D-S50] Update on the systematic review of palliative radiotherapy trials for bone metastases.** Clinical oncology (Royal College of Radiologists (Great Britain)) 2012;24(2):112-124. PMID 22130630；DOI `10.1016/j.clon.2011.11.004`
- 狀態：**PASS（僅摘要）**
- 查證路徑：Europe PMC 標題精確查詢 hitCount 1。
- 可用的數字（**⚠ 混合原發癌別，不是甲狀腺癌專屬**；**情境：無併發症的骨轉移疼痛**；**終點：疼痛反應**）：
  - **25 個隨機對照試驗**，比較單次分割與多次分割。
  - **意向治療：整體反應率單次 1,696/2,818（60%）vs 多次 1,711/2,799（61%）；完全反應 620/2,641（23%）vs 634/2,622（24%）——皆無顯著差異。**
  - 病理性骨折兩組相當；脊髓壓迫傾向多次分割較佳但不顯著（P=0.72 與 P=0.13）。
  - **重新照射的需求：單次分割組是多次分割組的 2.6 倍（95% CI 1.92–3.47；P<0.00001）。**（√(1.92×3.47)=2.58 ✓）
  - 急性毒性無顯著差異。
- **D5 用它說「痛的骨頭，放療是有用的、而且可以很短」，但必須標明這是混合癌別的資料。**

**[D-S51] Direct decompressive surgical resection in the treatment of spinal cord compression caused by metastatic cancer: a randomised trial.** Lancet (London, England) 2005;366(9486):643-648. PMID 16112300；DOI `10.1016/s0140-6736(05)66954-1`
- 狀態：**PASS（僅摘要）**
- 查證路徑：Europe PMC `TITLE:"Direct decompressive surgical resection in the treatment of spinal cord compression caused by metastatic cancer"` hitCount 2（本篇與一篇 2008 年的 British Journal of Neurosurgery 轉載評論）。
- 可用的數字（**⚠ 混合原發癌別**；**情境：轉移造成的脊髓壓迫**；**終點：能不能走路**）：
  - 隨機、多中心、非盲；**手術後放療 50 人 vs 單獨放療 51 人**；兩組放療皆為 10 次 × 3 Gy。
  - 期中分析達到預設提前停止準則而中止；篩 123 人、隨機 101 人。
  - **治療後能走路：手術組 42/50（84%）vs 放療組 29/51（57%），勝算比 6.2（95% CI 2.0–19.8；p=0.001）。**（√(2.0×19.8)=6.29 ✓）
  - **維持行走能力的中位時間 122 天 vs 13 天（p=0.003）。**
  - **入組時已不能走路的 32 人中，重新能走：手術組 10/16（62%）vs 放療組 3/16（19%）（p=0.01）。**
  - 手術組對類固醇與鴉片類止痛藥的需求顯著較低。
- **D5 用它說「脊髓被壓到的時候，這是急事，而且要外科一起決定」，必須標明非甲狀腺癌專屬。**

**[D-S52] NCT06558981 — The Role of Adjuvant Radiotherapy in High Risk Locally Advanced Differentiated Thyroid Cancer：a 1:1 Randomized Phase III Clinical Trial**
- 狀態：**PASS（試驗登錄資料，非結果）**
- 查證路徑：`https://clinicaltrials.gov/api/v2/studies?query.cond=thyroid cancer&query.intr=radiotherapy OR radiation&filter.advanced=AREA[DesignAllocation]RANDOMIZED` 命中，再打 `https://clinicaltrials.gov/api/v2/studies/NCT06558981?format=json`。
- 可用的內容：第三期、1:1 隨機、**RECRUITING**、2024-07-11 開始、**預計 124 人**、主辦 Fudan University、地點中國、**主要終點為手術後 5 年的 local-regional recurrence free survival（LRFS）**、**預計主要完成 2031-06（ESTIMATED）**。
- **D5 用它說「這個問題到 2031 年之前都不會有答案」。**

**[D-S53] NCT03669432 — Phase II Randomized Controlled Trial Of Postoperative Intensity Modulated Radiotherapy (IMRT) in Locally Advanced Thyroid Cancers.**
- 狀態：**PASS（試驗登錄資料，非結果）**
- 查證路徑：同上查詢，再打 `https://clinicaltrials.gov/api/v2/studies/NCT03669432?format=json`。
- 可用的內容：隨機、主辦 Tata Memorial Hospital（印度）、2013-07 開始、**實際收案 72 人**、主要終點 locoregional recurrence（治療後至 5 年）、**狀態 UNKNOWN**、預計主要完成 2026-07。
- **本組在 Europe PMC 未找到其結果論文。**

### 台灣端

**[D-S55] 衛生福利部食品藥物管理署　西藥許可證開放資料（西藥、醫療器材、化粧品許可證資料集）**
- 網址：`https://data.fda.gov.tw/opendata/exportDataList.do?method=ExportData&InfoId=36&logType=3&type=json`（同一查詢另比對 InfoId=37）
- 狀態：**PASS**
- 查證路徑：`info.fda.gov.tw` 經代理端 **502 CONNECT**（與 A 組相同，管道不可用）；改打 `data.fda.gov.tw` 的開放資料匯出端點，InfoId=36 回 HTTP 200、11,988,794 bytes（ZIP），解開後為 `36_3.json`、83,237,858 bytes、**72,043 筆**；InfoId=37 為 25,988 筆（兩者結果一致）。以成分名與英文品名逐筆比對，並抄回「適應症」欄全文。
- **查到的許可證（逐字回抄「適應症」中與甲狀腺相關的段落）**：
  - **Lenvatinib｜衛部藥輸字第026933號 Lenvima Capsules 4 mg 樂衛瑪膠囊4毫克；衛部藥輸字第026934號 Lenvima Capsules 10 mg 樂衛瑪膠囊10毫克**（申請商：衛采製藥股份有限公司；發證 2016/09/07；有效 2031/09/07；未註銷）。適應症第 1 項逐字：「分化型甲狀腺癌(Differentiated thyroid cancer, DTC)：適用於放射性碘治療無效之進行性，且為局部晚期或轉移性之分化型甲狀腺癌之成人病人。」（另有腎細胞癌、肝細胞癌、子宮內膜癌三項）
  - **Sorafenib｜衛署藥輸字第024727號 Nexavar film-coated tablets 200mg 蕾莎瓦膜衣錠 200 毫克**（台灣拜耳；發證 2017/10/06；有效 2027/10/23）。適應症第三段逐字：「放射性碘治療無效之局部晚期或轉移性的進行性(progressive)分化型甲狀腺癌(DTC)。」另查到同成分學名藥五張製劑許可證，適應症文字相同：衛部藥輸字第028614號（索拿癌膜衣錠200毫克）、衛部藥輸字第028536號（易芬妮膜衣錠200毫克）、衛部藥輸字第028192號（索福耐膜衣錠200毫克）、衛部藥製字第061955號（鎖癌飛膜衣錠200毫克）。
  - **Selpercatinib｜衛部藥輸字第028331號 RETSEVMO hard capsules 40mg 銳癌寧膠囊40毫克；衛部藥輸字第028332號 80mg**（台灣禮來；發證 2022/07/11；有效 2027/07/11）。適應症第 (2)(3) 項逐字：「(2)適用於治療需要接受全身性療法之晚期或轉移性 RET 基因突變甲狀腺髓質癌(MTC)的成人病人。(3)適用於治療需要接受全身性療法且以放射性碘治療無效(若適合接受放射性碘)之晚期或轉移性 RET 基因融合陽性甲狀腺癌的成人病人。」
  - **Cabozantinib｜衛部藥輸字第027511／027512／027513號 CABOMETYX film-coated tablet 20／40／60mg 癌必定膜衣錠**（法商益普生股份有限公司台灣分公司；發證 2018/10/12；有效 2028/10/12）。適應症第 3 項逐字：「分化型甲狀腺癌：適用於12歲以上曾接受VEGFR標靶治療後惡化、放射碘治療無效或不適用放射碘治療的局部晚期或轉移性分化型甲狀腺癌病人。」
  - **Pralsetinib｜衛部藥輸字第028393號 GAVRETO Capsules 100 mg 普吉華膠囊100毫克**（臺灣基石藥業有限公司；發證 2022/12/20；有效 2027/12/20）。適應症第 2 項逐字：「適用於需接受全身性治療且經放射性碘治療無效(如適用放射性碘治療)的晚期或轉移的RET融合陽性甲狀腺癌成人病人。」
  - **Larotrectinib｜衛部藥輸字第027746／027747／027748號 VITRAKVI 20mg/ml oral solution／25mg capsule／100mg capsule 維泰凱**（台灣拜耳；發證 2019/12/03；有效 2029/12/03）。適應症逐字：「適用於有NTRK 基因融合的實體腫瘤之成人和兒童病人，並應符合以下三項條件: 1、具NTRK基因融合且無已知的後天阻抗性突變(acquired resistance mutation)；2、為轉移性實體腫瘤，或手術切除極可能造成嚴重病症(severe morbidity)；3、沒有合適的替代治療選項，或於治療後發生疾病惡化。」**——不分癌別，未指名甲狀腺。**
  - **Entrectinib｜衛部藥輸字第027864／027865號 Rozlytrek 100／200mg hard capsules 羅思克膠囊**（羅氏大藥廠；發證 2020/05/21；有效 2030/05/21）。適應症第 2 項為 NTRK 基因融合陽性實體腫瘤（1 個月大以上），**同樣不分癌別、未指名甲狀腺**。
- **使用限制（紅線 4 與紅線 7）**：**藥證只證明「可以合法賣、標示上寫了這個適應症」，不證明有健保給付、不證明有人在用、不證明哪家醫院有。** 寫作時不得由此推論台灣的臨床實務或普及程度。

**[D-S56] 全民健康保險藥物給付項目及支付標準　第八十三條附件六「藥品給付規定」**
- 網址（法規本體）：`https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=L0060035`；附件檔：`https://law.moj.gov.tw/LawClass/LawGetFile.ashx?FileId=0000423552&lan=C`
- 狀態：**PASS**
- 查證路徑：`www.nhi.gov.tw` 各頁以瀏覽器 UA 打皆回 **403（Cloudflare「Just a moment...」挑戰頁）**；`data.nhi.gov.tw` 代理端 **502**；`https://data.gov.tw/api/v2/rest/dataset` 需 Authorization Key，未取得。改走全國法規資料庫：整合查詢「藥物給付項目及支付標準」→ 命中 pcode=L0060035「全民健康保險藥物給付項目及支付標準（民國 115 年 08 月 24 日）」，頁面「附檔」欄列出附件一至附件七，其中**附件六 藥品給付規定.PDF** 下載成功（HTTP 200、757,362 bytes、136 頁），以 `pdftotext -layout` 轉出 443,641 字元全文後全文檢索。
- **版本字串逐字回抄**：「第八十三條附件六　　藥品給付規定修正規定」「說明：本規定係依本標準第四條第四項規定公告一百十五年一月份之內容；如有異動，以保險人最新公告為主。」
- **查到的列項（逐字回抄）**：
  - **9.34.Sorafenib(如 Nexavar)：(98/10/1、100/6/1、101/8/1、104/12/1、105/11/1、106/1/1、107/7/1、108/6/1、108/12/1、109/1/1、112/8/1、114/2/1、114/6/1)** 第 3 項：「3.用於放射性碘治療無效之局部晚期或轉移性的進行性(progressive)分化型甲狀腺癌(RAI-RDTC)：(106/1/1) (1)放射性碘治療無效之局部晚期或轉移性的進行性(progressive)分化型甲狀腺癌。(2)需經事前審查核准後使用，每次申請之療程以3個月為限，送審時需檢送影像資料，每3個月評估一次。(3)Sorafenib 與 lenvatinib 不得合併使用。(107/7/1)」
  - **9.63. Lenvatinib(如 Lenvima)：(107/7/1、109/1/1、109/8/1、112/8/1、114/2/1、114/6/1)** 第 1 項：「1.用於放射性碘治療無效之局部晚期或轉移性的進行性(progressive)分化型甲狀腺癌(RAI-RDTC)：(1)需經事前審查核准後使用，每次申請之療程以3個月為限，送審時需檢送影像資料，每3個月評估一次。(2)Lenvatinib 與 sorafenib 不得合併使用。(109/8/1)」
  - **9.74.Cabozantinib (如 Cabometyx)： (108/12/1、110/12/1、114/8/1)** 第 2 項：「2.甲狀腺癌(114/8/1) (1)適用於治療成人及12歲以上兒童曾接受 VEGFR 標靶治療後惡化、放射碘治療無效或不適用放射碘治療的局部晚期或轉移性分化型甲狀腺癌病人。(2)須經事前審查核准後使用，每次申請療程以3個月為限，送審時需檢送影像資料，每3個月評估一次，無疾病惡化方可繼續使用。 3.每日限用1粒。」
- **查無列項（全文檢索命中 0 次）**：**Selpercatinib／Retsevmo／銳癌寧；Pralsetinib／Gavreto／普吉華；Larotrectinib／Vitrakvi／維泰凱；Entrectinib／Rozlytrek／羅思克；Dabrafenib；Trametinib。** 另以「NTRK」「基因融合」「不分癌別」「腫瘤不分部位」「泛癌」逐一全文檢索，**皆為 0 筆**；以正規式 `[A-Za-z]*RET[A-Za-z]*` 掃描，命中的全部是 retinal／secretory／acitretin／Ripretinib 等無關字詞，**沒有任何以 RET 基因為條件的給付條文**。
- **依鐵則寫法**：「在民國一百十五年一月份公告的健保藥品給付規定全文中查無列項，要問醫務課或個管師」。**不得推論有或沒有給付。**

**[D-S57] 全民健康保險藥物給付項目及支付標準　第七十九條附件二「藥品給付項目暨支付標準表」**
- 網址：`https://law.moj.gov.tw/LawClass/LawGetFile.ashx?FileId=0000423548&lan=C`
- 狀態：**PASS**
- 查證路徑：同 [D-S56] 的法規頁附檔；下載 HTTP 200、686,475 bytes、275 頁；`pdftotext -layout` 後共 13,705 筆藥品代碼行。
- **版本字串逐字回抄**：「第七十九條附件二　　　藥品給付項目暨支付標準表修正規定」「通則：本表係依本標準第四條第四項規定公告一百十五年一月份之給付項目及支付價格；如有異動，以保險人最新公告為主。」
- **查到的收載品項（藥品代碼／英文名稱／支付價（115年1月），逐字回抄）**：
  - `BC26933100 Lenvima Capsules 4 mg 967.00`
  - `BC26934100 Lenvima Capsules 10 mg 967.00`
  - `BC24727100 Nexavar film-coated tablets 200mg 856.00`
  - `BC28192100 Sorafenat film-coated Tablets 200mg 684.00`／`BC28614100 Sorafenib Sandoz Film-coated Tablets 200mg 690.00`／`AC61955100 Sorafenib F.C. Tablets 200 mg "C.C.P.C." 770.00`
  - `BC27511100 CABOMETYX film-coated tablet 20mg 4175.00`／`BC27512100 40mg 4175.00`／`BC27513100 60mg 4175.00`
  - `BC27746148 VITRAKVI 20mg/ml oral solution 26798.00`／`BC27746155 同品項 53597.00`／`BC27747100 VITRAKVI 25mg capsule 669.00`／`BC27748100 VITRAKVI 100mg capsule 2679.00`
  - `BC27865100 Rozlytrek 200mg hard capsules 1530.00`（**100mg 膠囊未列**）
- **查無（全文檢索 0 筆）**：**RETSEVMO（selpercatinib）、GAVRETO（pralsetinib）。**
- **這一筆的作用**：證明「在附件六查無列項」**不等於**「不給付」——larotrectinib 與 entrectinib 在附件二有收載、支付價也列了，但附件六沒有任何限制條文。**因此 D4 的台灣段落必須把「有藥證」「有收載並列了支付價」「有沒有給付規定條文」三件事分開寫，且對 selpercatinib／pralsetinib 只能寫「附件二與附件六都查無列項」。**
- **⚠ 媒體報價一律不引用**；上列支付價是法規附件的原始數字，**但那是健保的支付點數，不是病人自費價**，寫進文章會違反紅線 7（不寫任何自費金額）。**建議：這些金額只留在 brief 供編輯判斷，文章不得出現。**

**[D-S54] NCT04940052 — A Randomized, Double-blind, Placebo-controlled Phase III Study to Evaluate the Efficacy and Safety of Dabrafenib Plus Trametinib in Previously Treated Patients With Locally Advanced or Metastatic, Radio-active Iodine Refractory BRAFV600E Mutation-positive Differentiated Thyroid Cancer (DTC)**
- 狀態：**PASS（試驗登錄資料）**
- 查證路徑：`https://clinicaltrials.gov/api/v2/studies/NCT04940052?format=json`。
- 可用的內容：PHASE3、**ACTIVE_NOT_RECRUITING**、2021-11-15 開始、**實際收案 153 人**、**主要完成 2025-01-22（ACTUAL）**、`hasResults` 為 true（登錄端已有結果區段）。結果論文為 [D-S39]。
- **用途**：證明 ATA 2025 寫的「is underway」在本次查證時已經不成立（⚠D-7）。

---

## 本組各篇可以寫的東西

### D1 `th-tsh`〈吃一輩子的那顆藥，要吃到多少〉

**能站住的支點**

1. **這一篇的骨幹就是「指引把數字拿掉了」這件事。** ATA 2025 Table 9 的 TSH 目標只有四格文字，附註 b 與 c 都直說「data are inconclusive」；Recommendation 45 的等級是 Conditional／Low certainty。可以逐字引英文＋自己的中文翻譯。這讓文章可以誠實地說：**你的醫師給你一個數字，那個數字現在不是從指引抄來的，是他替你權衡出來的。**
2. **決定目標的是「治療反應分類」，不是「當初被歸在哪一格風險」。** Table 9 的 TSH 欄掛在 excellent／indeterminate／biochemically incomplete／structurally incomplete 底下。這件事對讀者很重要，因為它意味著**這個目標會隨時間變**，而 Recommendation 46B（GPS）明文要求定期重新評估。
3. **明文的「不建議長期抑制」**：Recommendation 46A 逐字（注意 ⚠D-2 的用詞問題）。
4. **效益側的證據長什麼樣，可以完整攤開**：唯一的 RCT [D-S4]（218 vs 215，非劣性，DFS 沒有比較差）；支持抑制的 2002 年統合分析 [D-S5]（4,174 人中 2,880 人抑制，RR 0.73，CI 0.60–0.88，但年代 1934–2001、合成終點）；2024 年中／高風險統合分析 [D-S6] 三個合成終點全部不顯著、不良事件顯著較高；867 人的中／高風險世代 [D-S7] PFS 無差異且自承死亡事件不足。
5. **代價側可以給真正的分母**：
   - **骨**：[D-S16] 179 名幾乎全為停經後的女性，TSH<0.5 那一組脊椎骨折 44.6%、0.5–1.0 組 24.0%、>1.0 組 4.3%；[D-S15] 17 篇統合，停經後女性腰椎骨密度 −0.03 g/cm²、停經前反而 +0.04、男性無差別；[D-S13] 70,298 人的個別參與者資料，TSH<0.10 這一格髖骨骨折 HR 1.61（510 人中 47 事件）；[D-S17] 退伍軍人 10,370 對，骨質疏鬆 7.3% vs 5.3%（OR 1.33），**但骨折沒有比較多，TSH 與骨折 OR 1.01**。
   - **心房顫動**：[D-S9] Framingham 系列 2,007 名長者，TSH ≤0.1 者 10 年累積 28% vs 正常 11%，RR 3.1（95% CI 1.7–5.5），**而 0.1–0.4 那一格沒看到差別**；[D-S10] 哥本哈根 586,460 人，受抑制的亞臨床甲亢 IRR 1.41（1.25–1.59）；[D-S11] 韓國健保 113,791 人 vs 455,188 對照，整體 HR 2.07（1.98–2.17），**但單葉切除也有 1.93**；[D-S12] 統合 187,754 人，IRR 1.54（1.44–1.65）。
   - **心血管死亡**：[D-S18] 524 人 vs 1,572 對照，心血管死亡 HR 3.35（1.66–6.74），組內每 TSH 下降 10 倍 HR 3.08（1.32–7.21）；[D-S19] 705,307 名吃甲狀腺素的退伍軍人，TSH<0.1 的 HR 1.39（1.32–1.47），**但 TSH>20 的 HR 2.67——吃太少更糟**。
   - **同一個世代裡的好處與代價**：[D-S8] 771 人低／中風險全切世代，復發 5.6%、骨質疏鬆 3.9%、心房顫動 2.3%；抑制沒有降低復發（HR 1.02），但女性骨質疏鬆 HR 3.5（CI 1.2–10.2）。**這一篇最適合當文章的收束段。**
6. **半切病人的「補充 vs 抑制」**：ATA 2025 逐字——目標訂在正常參考範圍時約 70–80% 的半切病人可以不吃藥；目標訂在 0.5–2.0 時只剩 20–30%。搭配 [D-S20]（84% 的半切病人術後 TSH >2，其中 68% 開始吃藥，77% 至少調整過一次劑量）。**這一段直接回答「為什麼有人半切之後還是要吃」。**

**哪幾句話寫不了**

- ❌ 不能寫「目標是 0.1」「目標是 0.5–2.0」等任何具體數字作為現行標準（⚠D-1）。
- ❌ 不能寫「已證實抑制沒有用」——[D-S4] 是非劣性設計（⚠D-3）。
- ❌ 不能把 [D-S9]／[D-S10]／[D-S13]／[D-S14]／[D-S19] 的數字講成「甲狀腺癌病人吃藥的風險」——它們分別是社區長者、丹麥基層人口、13 個一般人口世代、ARIC 世代、全體甲狀腺素使用者（⚠D-18）。
- ❌ 不能把 [D-S11] 的 HR 2.07 歸因於 TSH 抑制（單葉組也有 1.93）。
- ❌ 不能寫 Klein Hesselink 的「TSH <0.02」這個切點（本組無法驗證）。
- ❌ 不能寫 ATA 轉述的 29%／50%／20% 達標率（本組未回原文）。
- ❌ 不能寫「大多數台灣醫師怎麼設目標」——紅線 4。

---

### D2 `th-followup`〈追蹤看的是超音波和一個數字〉

**能站住的支點**

1. **「那個數字的意義完全取決於你被切掉多少、有沒有做放射碘」——這一句有官方系統性回顧背書。** [D-S21] 把三種情境（半切／全切無 RAI／全切放射碘前）分開報，並逐字寫「Following partial thyroidectomy, Tg measurement was not accurate for diagnosing recurrence or metastasis」，而且**全部情境的證據品質都是 very low**。
2. **Table 9 三欄可以整表照抄**（⚠D-12），包括半切那一欄的兩個 N/A。這是全文最重要的一張表。
3. **反應分類的四個定義可以逐字引**（Recommendation 29 的 A–D），並搭配 ATA 2025 給的各類復發率區間（excellent 1–4%，低風險 excellent 0.2–2%，indeterminate 5% 到 15–20%，biochemical incomplete 20–53%）。
4. **抗體那一段可以寫成「換一種追蹤方式」**：Recommendation 47E 逐字（⚠D-17）；ATA 內文「TgAb are present in about 20% of patients with DTC」與「it is not clear that any Tg assay system is fully accurate in monitoring patients with circulating TgAb」。可以解釋機轉：免疫計量法在抗體存在時**傾向低估**（falsely low），所以「數字漂亮」反而可能是假的。
5. **為什麼不用再打針刺激**：[D-S27] 服藥狀態下高敏感 Tg 測不到時，排除結構性疾病的陰性預測值 99.4%（1,796 人、10 篇）。
6. **超音波的間隔與「什麼時候可以停」**：Recommendation 31C（初次治療完成後 6–12 個月做一次，之後看風險與反應）、Recommendation 31D（<8–10 mm 的可疑淋巴結可以先追不扎）、Table 11 三列的「每 1–3 年、做 5–8 年」與 Recommendation 48 的 5–8 年停超音波、10–15 年停生化監測。
7. **「照太多會出事」也有數字**（ATA 2025 內文，屬指引自己的綜述，可用定性寫法）：excellent response 的低風險病人做超音波「has not been found to identify clinically significant disease, but it can increase the number of interventions undertaken based on false positive findings」。
8. **全身碘掃描與 FDG-PET 在追蹤中的位置**：Recommendation 49A（沒做過放射碘的人不該做監測性全身掃描）、49B（低與低-中風險且 excellent response 不需要例行做）、49C（中-高與高風險且臨床懷疑復發時可做）；Recommendation 50A/B 與內文「generally >10 ng/mL」、偽陽性 0–39%、「18FDG-PET is insensitive for detecting brain metastases and that standard imaging stops in the mid-thigh」；量化表現用 [D-S28]（17 篇、1,195 人，敏感度 0.86、特異度 0.84，但 I²≈80%、可能有發表偏誤）。

**哪幾句話寫不了**

- ❌ 不能給半切之後的 Tg 切點（含 30 ng/mL）當作現行標準（⚠D-12）。
- ❌ 不能寫「Tg 正常就是沒事」——TgAb 陽性那 20% 的人不適用。
- ❌ 不能把 Table 11 的「每 1–3 年」寫成所有人的追蹤頻率——那一表的前提是**低風險＋持續 excellent response**。
- ❌ 不能寫「10 年之後就不用再看醫師了」——Recommendation 48 講的是**甲狀腺癌的例行監測**可以停，甲狀腺素劑量與 TSH 的追蹤是另一回事（ATA 2015 Recommendation 62D 要求至少每 12 個月驗一次 TSH；2025 版本組未查到對應條文，**不得自行推論**）。
- ❌ 不能寫台灣的健保追蹤頻率或給付（本組未查，屬 E4）。

---

### D3 `th-recurrence`〈Tg 上升，不一定找得到東西〉

**能站住的支點**

1. **「生化性反應不完全」的正式定義**（Recommendation 29C 與 Table 9）與「它不等於復發」這件事。
2. **自己會好的比例，有三組互相獨立的數字**：
   - [D-S24] 506 人、中位追蹤 10 年：**34% 的生化性反應不完全病人在完全沒有額外治療下被重新分類為無疾病證據**；對照組是結構性反應不完全者即使治療後也只有 9% 變成無疾病證據。
   - [D-S25] 299 人：**6 個月時抑制狀態下 Tg 在 1–5 ng/mL 的人，54% 最後在沒有額外治療下降到 <1 ng/mL**；且 25% 的人要 18 個月以上才到谷值。
   - [D-S26] 186 人（刺激型 Tg）：**sTg1 2–4.9 的人 41% 自發生化緩解（中位 69 個月）、5–19.9 的 17%、≥20 的 1%。**
3. **會變壞的比例，同一批資料也有**：[D-S26] 結構性復發 A 組 24%、B 組 30%、C 組 50%，全體 32%；ATA 2025 的區間是 20–53%（全切＋RAI）與 0–31.6%（全切無 RAI）。**兩個方向都要寫，而且要標明是哪一種手術／有沒有放射碘。**
4. **「找不到東西的時候要做什麼」**：Recommendation 31F（先做橫斷面影像找肺與骨）、31G（嗜酸性癌與低分化癌可考慮 FDG-PET/CT）、Recommendation 49C 與 D（診斷性全身掃描與 SPECT-CT 的位置）、Recommendation 50A、[D-S28] 的量化表現。
5. **「不要做什麼」有明確條文**：
   - Recommendation 58A：刺激型 Tg <10（停藥）或 <5（rhTSH）且無結構性疾病者，**可以只用甲狀腺素治療繼續追蹤**。
   - Recommendation 60 內文（⚠D-14）：**Tg 上升本身不是開始全身性治療的理由。**
   - Recommendation 58 內文：經驗性放射碘「more than half of patients with negative diagnostic WBS experience a fall in serum Tg levels after empirical RAI therapy, but improved survival has not been shown」。
   - [D-S29]：再一次放射碘的效益有限——164 人中最後只有 34.1% 無疾病；生化性持續者的刺激型 Tg 雖從 41.9 降到 24.6 ng/mL（P=0.003），結構性持續者則毫無變化。
6. **Tg 倍增時間**：ATA 2025 內文說 Tg 倍增時間短與 FDG-PET 陽性有關，**但明講「the "cut-points" vary across reports」**。可以寫「醫師看的是趨勢不是單一次的數字」，**不給切點**。

**哪幾句話寫不了**

- ❌ 不能寫「Tg 升高就是復發」，也不能寫「Tg 升高大多沒事」——兩個方向的數字都要給。
- ❌ 不能用 ATA 轉述的 Hirsch 數字（3/47、17.6%、44 人；⚠D-4b）。
- ❌ 不能把 [D-S26] 的刺激型 Tg 切點（2／5／20 ng/mL）講成現在門診抽的那個非刺激 Tg 的切點。
- ❌ 不能寫「再做一次放射碘就好了」。
- ❌ 不能給 Tg 倍增時間的切點。

---

### D4 `th-rai-refractory`〈放射碘無效之後〉

**能站住的支點**

1. **定義可以逐字給**（Recommendation 59 的兩層：Strong criteria 兩條、Supplemental criteria 兩條），並誠實寫出兩件事：(a) Recommendation 59 本身是 Good Practice Statement、判準段落沒有證據等級（⚠D-19）；(b) 指引自己寫「RAIR criteria will continue to evolve」。
2. **「無效」不等於「來日無多」**：Recommendation 59 內文逐字「while some of these patients die within 3–5 years, there are also long-term survivors with stable or very slowly progressive disease」；Recommendation 60A 明文允許無症狀、穩定或極緩慢進展者**只做 3–12 個月一次的影像追蹤**。
3. **兩個第三期試驗可以完整寫**：
   - **DECISION（sorafenib）**：417 人（207/210），PFS 10.8 vs 5.8 個月，HR 0.59（95% CI 0.45–0.76）；**OS 無差異（HR 0.80，95% CI 0.54–1.19），71.4% 的安慰劑組交叉**；ORR 12.2%（24/196）全為部分反應，中位持續 10.2 個月；**劑量中斷 66.2%、減量 64.3%、停藥 18.8%**；嚴重不良事件 37.2% vs 26.3%。
   - **SELECT（lenvatinib）**：392 人（261/131），PFS 18.3 vs 3.6 個月，HR 0.21（**99%** CI 0.14–0.31）；反應率 64.8%（4 個完全反應）；**兩組中位 OS 皆未達到**；**因不良事件停藥 14.2%**；**治療期間 20 例死亡中 6 例判定與藥物有關**。
   - 指引的取捨：Recommendation 62 逐字（lenvatinib 為多數人的首選，Strong／High certainty），並逐字承認「no randomized controlled trial has been conducted directly comparing sorafenib to lenvatinib」。
4. **二線**：Recommendation 66（Strong／High certainty）＋ COSMIC-311 延長追蹤 [D-S33]（258 人，PFS 11.0 vs 1.9 個月，HR 0.22，96% CI 0.15–0.32；ORR 11.0%；grade 3/4 62% vs 28%），並寫出期中分析的 ORR 未達預設顯著門檻（[D-S32]）。
5. **基因導向的藥，可以老實寫「證據規模很小」**：
   - RET 融合：Recommendation 68（Strong／Moderate），但原始資料是 [D-S34] 的 **19 人**（反應率 79%，95% CI 54–94）與 [D-S35] 的 **9 人**（8/9，89%，95% CI 52–100）。
   - NTRK 融合：Recommendation 67（Strong／Moderate），[D-S37] **29 人**（乳突／濾泡 86%、未分化 29%）；[D-S38] 是 54 人的不分癌別籃子試驗（整體 57%）。盛行率：乳突癌約 7%，兒童與年輕人約 25%（ATA 2025 內文）。
   - BRAF V600E：Recommendation 70a/b/c，加上**新的第三期結果** [D-S39]（153 人，PFS 12.8 vs 3.7 個月，HR 0.38；ORR 57% vs 4%；**OS 期中未達顯著**；二線定位）。
6. **再分化**：ITOG 2025 的三句定位（[D-S44]）＋ ASTRA 陰性（[D-S43]）＋ MERAIODE BRAF 世代（[D-S40]，24 人收案 21 人可評估，6 個月部分反應 38%）＋ SEL-I-METRY（[D-S42]，**主要終點分母只有 9 人、12 個月 PFS 64.8%，CI 25.3–87.2**，且因攝碘率只有約 40% 與收案太慢提早關閉）＋ Ho 2013（[D-S45]，20 人，8 人達劑量門檻，5 人部分反應；**1 人事後發生骨髓化生不良症候群並進展為急性白血病**）。Recommendation 74A/B 逐字。
7. **什麼時候開始吃藥**：Recommendation 63A（有症狀且不適合局部治療 → 不要拖，Strong／Moderate）與 63B（無症狀者要看病人重視療效還是生活品質，GPS）；Recommendation 60 內文「increasing Tg levels alone … should not be considered a criterion warranting the initiation of systemic therapy」。
8. **台灣端可以寫得很具體**（見 [D-S55]～[D-S57]，並嚴守三層分開）：
   - **藥證**：lenvatinib、sorafenib、cabozantinib 的仿單裡直接寫了「放射性碘治療無效之……分化型甲狀腺癌」；selpercatinib 與 pralsetinib 的仿單寫的是「RET 基因融合陽性甲狀腺癌」；larotrectinib 與 entrectinib 的仿單是**不分癌別的 NTRK 適應症、沒有指名甲狀腺**。
   - **健保藥品給付規定**：sorafenib（9.34 第 3 項）、lenvatinib（9.63 第 1 項）、cabozantinib（9.74 第 2 項，114/8/1 起）**有列項，而且三者都寫「需經事前審查核准後使用，每次申請療程以 3 個月為限，送審時需檢送影像資料，每 3 個月評估一次」；sorafenib 與 lenvatinib 明文不得合併使用。**
   - **查無列項**：selpercatinib、pralsetinib、larotrectinib、entrectinib、dabrafenib、trametinib 在給付規定全文中 0 筆；全文亦無任何以 NTRK 或 RET 基因為條件的條文。
   - **但**：larotrectinib 與 entrectinib 在附件二（給付項目暨支付標準表）**有收載**，selpercatinib 與 pralsetinib **沒有**。所以文章的寫法是：「這幾個藥在台灣有藥證；健保的藥品給付規定裡，只有三個藥寫了甲狀腺癌這一條，而且都要事前審查、三個月一審。其他幾個查不到列項——**查不到列項不等於不給付，也不等於給付**，要問你的醫務課或個管師。」

**哪幾句話寫不了**

- ❌ 不能把 LIBRETTO-531 的數字寫進分化型甲狀腺癌（⚠D-8）。
- ❌ 不能寫任何 95% 以外的 CI 卻標成 95%（⚠D-5）。
- ❌ 不能用 ATA 轉述而本組未驗證的數字：SELECT 的 83% 交叉／交叉後 PFS 10.1／ORR 52.3／中斷 82.4／減量 67.8／嚴重不良事件 49.8、COSMIC-311 的減量 56%／停藥 5%、entrectinib 的甲狀腺次群、MERAIODE RAS 世代的 2/10。
- ❌ 不能寫「有藥證就是健保有給付」或反過來。
- ❌ 不能寫任何自費金額或健保支付點數（紅線 7）。
- ❌ 不能寫「台灣有多少人在用」「哪家醫院做得到基因檢測」（紅線 4、7）。
- ❌ 不能把再分化寫成已經可用的常規治療（⚠D-15）。

---

### D5 `th-ebrt`〈體外放射線治療在這個病的位置〉

**固定利益揭露**：依 SPEC §二 逐字放置，中英各一版，**只出現在本篇**。

**能站住的支點（負向的證據要跟正向的一樣硬）**

1. **「有沒有隨機證據」這一題可以正面回答，而且答案很乾淨**：
   - 唯一啟動過的隨機試驗是 MSDS（[D-S46]／NCT00144079）。它**不是收不到人，是收得到人但病人不肯被隨機分配**——311 人中只有 45 人同意；最後改成世代研究，被指派到放療的 47 人裡只有 26 人真的接受。作者自己的結論是「Routine RTx in locally invasive DTC can no longer be recommended.」
   - **今天仍有兩個隨機試驗在跑，都還沒讀出**：NCT06558981（第三期，預計 124 人，5 年 LRFS，預計 2031-06 主要完成）、NCT03669432（隨機第二期，實際 72 人，狀態 UNKNOWN）。
   - ATA 2025 自己逐字承認「Prospective data from clinical trials evaluating the benefits of EBRT weighed against its toxicities are limited.」
2. **所有「支持」的資料都是回溯性單中心系列或傾向分數配對**：ATA 2025 內文列出的存活區間是 4–10 年、局部無復發 79–95%、疾病特異性 71–76%、總存活 65–93%——**區間大到幾乎不能用**，正好可以拿來說明「這種資料能告訴你什麼、不能告訴你什麼」。[D-S49] 是其中最漂亮的一筆（4 年 LRFS 100% vs 84.6%，P=.002），但**是單臂第二期＋傾向分數配對，而且總存活兩組都是 100%**。
3. **最強的量化證據是負向的**：[D-S47] SEER 870 例 T4 乳突癌，EBRT 與較差的 OS（HR 1.60）與 DSS（HR 1.58）相關。**必須同時寫出三個限制（⚠D-11）。**
4. **ATA 2025 的條文可以逐字給，而且它自己就是保留的**：Recommendation 44A 逐字含「must be weighed against the absence of data demonstrating improvement in overall survival and the known risks of clinically meaningful toxicity」；44B 逐字；兩條都是 **Conditional／Low certainty**。Recommendation 54（不可切除的頸部復發）也是 Conditional／Low certainty。
5. **少數真的需要的處境，可以列得很清楚**：
   - **肉眼殘存或無法切除**：Recommendation 44B；[D-S48] 27 人前瞻第二期，2 年局部區域 PFS 79.7%、OS 77.3%、grade ≥3 毒性 33.4%；事後比較顯示合併化療的局部控制較好但**皮膚炎、黏膜炎、吞嚥困難也較多**，**而且那兩組不是隨機分的**。
   - **不可切除的頸部復發／結外侵犯／軟組織受侵**：Recommendation 54。
   - **會痛的骨轉移**：Recommendation 77（Conditional／Moderate）＋ ATA 內文「While prospective controlled trials are lacking, palliative radiotherapy is well tolerated and effective at producing durable local control in many cases.」＋ [D-S50]（25 個隨機試驗、混合癌別：單次與多次分割的疼痛反應率相同，60% vs 61%；但單次分割需要重照的機率是 2.6 倍）。
   - **脊髓壓迫**：Recommendation 77 內文（「Indications for palliative surgery include vertebral metastases associated with spinal cord compression or impending compression」「Postoperative radiotherapy is typically administered to reduce the risk of local recurrence」）＋ [D-S51]（101 人、混合癌別：手術加放療 84% 能走 vs 單獨放療 57%，OR 6.2，95% CI 2.0–19.8；維持行走中位 122 天 vs 13 天）。**這一段的重點是「要外科一起決定，不是放腫科自己決定」，正好呼應揭露段最後一句。**
   - **腦轉移／脊髓旁病灶要先放療再放射碘**：Recommendation 79A/B 與 Recommendation 55C 內文（「If brain or spinal canal metastases are detected, EBRT prior to RAI and high-dose corticosteroid therapy are recommended to limit the risk of acute tumor swelling」）。
6. **頸部放療的具體代價，指引自己寫了兩層**：
   - 急性與長期毒性：ATA 內文「grade 2 or less acute mucositis, esophagitis, xerostomia, dysphagia, dermatitis, and fatigue are quite common, grade 3 or higher acute and long-term toxicities, including dysphagia, gastrostomy tube-dependance, and tracheostomy, are rare」。
   - **最關鍵、也最少被講的那一句**：「make future revision neck surgery for recurrent disease still more challenging」——**照過的脖子，以後要再開會更難開。** 這一句是 D5 全篇的道德重心。
   - [D-S48] 的具體事件：兩名合併化療者因喉頭水腫需氣切、兩名需胃造口、兩名單獨 IMRT 者在局部復發後需氣切（**此三項為 ATA 2025 轉述，本組未在該論文摘要中驗證，僅可寫成「會用到氣切與胃造口的情況存在但少見」**）。
7. **站外指路**：頸部放療後的甲狀腺低下 → `hn-late-effects`／`hn-followup`（SPEC §五已指定，本篇不重寫）。

**哪幾句話寫不了**

- ❌ 不能寫「有隨機試驗支持放療」，也不能寫「永遠不會有隨機試驗」（兩個正在跑）。
- ❌ 不能寫「放療會降低存活率」（⚠D-11）。
- ❌ 不能把 MSDS 寫成「只收了 45 人就關了」（⚠D-10）。
- ❌ 不能把 [D-S50]／[D-S51] 寫成甲狀腺癌的資料（⚠D-16）。
- ❌ 不能寫劑量數字給讀者對照（ATA 內文的 6000–6600 cGy／7000 cGy 只供編輯理解；紅線 6 的精神同樣適用於放療劑量與分次）。
- ❌ 不能寫任何機器型號、哪家醫院有什麼（紅線 7）。
- ❌ 不能寫台灣健保對 IMRT／SBRT 的給付（本組未查，屬 E4）。

---

## 查不到的東西（明寫查無，不補空）

1. **ATA 2025 的 Executive Summary 版本**——本組未另行取得，所有逐字條文皆取自全文版（PMC13090833）。若寫作組需要較短的官方摘要版，須另查。
2. **MERAIODE RAS 世代（Thyroid 2023;33(9):1124-1129，PMID 37350119）的任何內容**——Europe PMC 回傳 `abstractText` 為空、非 OA、無 PMCID，`pmc.ncbi.nlm.nih.gov` 無對應頁。**只確認論文存在。**
3. **COSMIC-311 的 Erratum（Cancer 2023;129(5):807，PMID 36637398）內容**——僅確認存在，未取得更正了什麼。引用 [D-S33] 的數字時請編輯留意此風險。
4. **SELECT 原著正文**（NEJM 2015;372(7):621-630，無 PMCID、非 OA）——只取得摘要。劑量中斷率、減量率、交叉後療效、更新版 PFS 皆**未能獨立驗證**。
5. **COSMIC-311 的劑量減量率與停藥率**——兩篇論文的摘要皆未提供，全文非 OA。
6. **entrectinib 試驗中甲狀腺癌次群的結果**——[D-S38] 摘要未分癌別報告；ATA 引用的 2022 年更新只有**會議摘要**（J Clin Oncol 2022;40(16_suppl):3099），依鐵則不引用。
7. **Yavuz 2022（ATA ref 950，1,125 人 21 中心的 TSH 達標率）**——本組未查證原文，**29%／50%／20% 三個數字不得使用**。
8. **Klein Hesselink 2013 的「TSH <0.02」切點**——摘要無此數字，全文非 OA，**不得使用**。
9. **ATA 2025 Recommendation 47／48 是否保留了「至少每 12 個月驗一次 TSH」這一條**——本組在取得的全文中未找到對應條文（2015 版 Recommendation 62D 有）。**D2 不得寫「指引要求每年至少驗一次 TSH」。**
10. **台灣健保對頸部 IMRT／SBRT、對甲狀腺癌追蹤影像頻率的給付規定**——本組未查（屬 E4 範圍）。**D2 與 D5 不得寫任何台灣給付內容。**
11. **台灣有多少甲狀腺癌病人在用標靶藥、事前審查的實際核准率**——**查無可引用的官方來源**，且依紅線 4 不得由給付條文推論。
12. **`info.fda.gov.tw` 的許可證查詢介面**——代理端 502 CONNECT，**管道不可用**（與 A 組相同）。本組改走 `data.fda.gov.tw` 開放資料取得等價資料，因此 **D4 的藥證段落是「查到了」，不是「查不到」**。
13. **`www.nhi.gov.tw` 本站**——Cloudflare 403；`data.nhi.gov.tw` 502；`data.gov.tw` API 需授權金鑰。本組改走全國法規資料庫的法規附件 PDF 取得等價全文，因此 **D4 的健保段落是「查到了全文並檢索」，不是「管道不可用」**。但**該附件的版本是「公告一百十五年一月份之內容」，比法規本體的修正日期（115/08/24）舊**，引用時必須連同版本字串一起寫。
14. **ISRCTN17468602（SEL-I-METRY）登錄端資料**——本組未另行查詢，試驗細節取自論文正文。
15. **NCT03669432 的結果**——狀態 UNKNOWN，Europe PMC 查無結果論文。
