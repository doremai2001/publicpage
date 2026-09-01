# Brief A — 乳房放射治療專題「為什麼照、怎麼決定」群（A1–A3）

研究員：Group A｜查證日期：2026-08-31｜期刊書目全部經 Europe PMC REST API（`DOI:"..."` / TITLE 查詢，含括號之 Elsevier DOI 一律加引號）逐筆核對：標題、作者、期刊、卷期頁、年份、PMID、OA 狀態照 API 回傳值抄寫；指引措辭凡標「逐字」者出自 Europe PMC 回傳之 abstract 或 fullTextXML（PMC OA 全文），非二手轉述。台灣官方文件經實際下載（curl HTTP 200 → pdftotext → grep 原文），抓取路徑逐條註明。
引用規則：**只有標 PASS 的來源可以進正文引用。** FAIL 條目保留並附「這個洞怎麼寫」。每個數字帶族群標籤（手術型式、淋巴結狀態、分次、追蹤年數）。
起點聲明：候選清單參考了 `_pipeline/breast/brief-C.md` 與已發布之 bc-rt-regional／bc-rt-hypofx／bc-rt-omission 參考清單，但**每一條都在本日重新跑過 Europe PMC／官方文件核對**，未沿用任何舊 PASS 標記。

## ⚠ 六件與 SPEC 假設不同形狀的事（動筆前必讀）

1. **A2 並陳的國際側已經不只是「指引放寬」，是「隨機試驗讀出＋指引原文」雙層。** SPEC §一3 寫「START 十年、近年 ASTRO/ESTRO 對低分次的擴張」；查證結果是 2026 年已有兩個大型 N+ 區域淋巴低分次隨機試驗發表：**HypoG-01**（Lancet 2026；1,265 人，40 Gy/15 次 vs 50 Gy/25 次之區域淋巴照射，主要終點手臂淋巴水腫非劣性成立，p<0.001）[S17] 與 **SKAGEN-1**（JCO 2026；2,908 人，3 年淋巴水腫 8.0% vs 9.4%，8 年內局部區域復發 HR 0.96）[S16]，加上中國 **Wang 2019** PMRT 試驗（820 人，5 年局部區域復發 8.3% vs 8.1%，非劣性 p<0.0001）[S15]。院內對 N+ 維持傳統分次仍站得住（理由見 A2 Caveats），但文章**不可把國際側寫成「還在等證據」**——要寫成「證據已到、各地採納速度不同、我們的保守有具體理由」。
2. **健保條文本身就是院內做法的第三隻腳，而且條文正在動。** 現行可查到的 36022B／36023B 適應症逐字是「早期乳癌或原位癌接受乳房腫瘤局部切除（+/-前哨或腋下淋巴結清除）後加上術後放射線治療，治療範圍包含全乳房（**不包含鎖骨上淋巴結、腋下淋巴結或內乳淋巴結**）」，禁忌症第一條就是「**淋巴結轉移**」[S26]——即「保留手術＋N0 → 低分次給付碼；N+ → 不在低分次包裹碼內」，與院內「PM 且 pT1–2N0 → 低分次」形狀完全一致。**但** 2025-10-29 行政院公報之修正草案明列「修正 36022B『乳癌術後低分次照射合併局部加強照射放射治療』等二項診療項目，**刪除禁忌症以符合國際臨床指引**」[S28]——健保自己也在往國際方向走。現行生效版是否已刪，查不到整合後條文（FAIL-2）。A2 寫法：並陳三隻腳（國際證據、院內政策、健保條文），並加一句「條文這幾年在調整，實際適用問醫務課」。
3. **兩份國際指引的原文措辭都拿到了（abstract 層級逐字），A2 並陳的兩邊原文都在手上。** ASTRO 2018：「the preferred dose-fractionation scheme is hypofractionated WBI to a dose of 4000 cGy in 15 fractions or 4250 cGy in 16 fractions」[S13]；ESTRO-ACROP 2022：「moderately hypofractionated radiotherapy can be offered to any patient for whole breast, chest wall (with or without reconstruction), and nodal volumes. Ultrafractionation (five fractions) can also be offered for non-nodal breast or chest wall (without reconstruction) radiotherapy either as standard of care or within a randomised trial or prospective cohort」[S14]。ESMO 2024 的逐字建議條文取不到（FAIL-1），只能當書目錨點。
4. **A1 的「MRM 後 N+ 建議 PMRT」在 1–3 顆這格不是鐵律，是有張力的地帶。** EBCTCG 2014：1–3 顆陽性者 PMRT 降乳癌死亡率 RR 0.80（0.67–0.95）[S3]；但 SUPREMO（NEJM 2025）用現代全身治療重做中風險族群（含 pT1-2N1）：10 年總存活 81.4% vs 81.9%（HR 1.04，p=0.80），胸壁復發 1.1% vs 2.5%（HR 0.45）[S7]。bc-rt-regional 已把這個並陳寫過——A1 一句話帶出張力＋指路，不重寫證據深度；但**不可寫成「N+ 一定要照」**。≥4 顆這格沒有爭議（RR 0.87，且無人在 SUPREMO 型試驗裡挑戰它）。
5. **重大傷病證明：乳癌第一期效期三年，其餘乳癌五年——跟肝癌專題的「一律五年」不同。** 法規原文（〈全民健康保險保險對象免自行負擔費用辦法〉第二條附表一，114-01-01 起適用版）：「C50.011–C50.929 (三)乳房惡性腫瘤第一期……**三年**」；「C00.0–C96.9 (五)除(一)-(四)之其他惡性腫瘤……**五年**」[S29][S30]。A 組文章若提重大傷病，必須分期別寫。
6. **A3 的「基本款那格要真實」有臨床數據，但方向跟直覺相反的部分要小心。** IMRT 對 2D 的優勢有隨機試驗三連：急性濕性脫屑 31.2% vs 47.8%（加拿大，雙盲）[S18]、5 年外觀變化 40% vs 58%（英國 Royal Marsden）[S19]、5 年整體外觀不佳 OR 0.68（劍橋）[S20]——「一般 IMRT 本身就有作為」這段有本錢寫。反向，一筆 TOMO vs IMRT 的回溯世代（315 人、追蹤僅 3 個月）顯示 TOMO 的 3–4 級皮膚毒性反而較高（16.2% vs 7.6%）、放射性肺炎較低（0% vs 4.3%）[S25]——TOMO 不是全面升級，A3 的一句話定位要寫成「劑量分布的再進一步、適應症決定」，深度與費用歸 B2。

---

## A1 `brt-who-needs`〈誰需要術後放射治療〉

### Key facts

**保留手術（PM）後全乳照射是配套（證據本體）**

- **EBCTCG 2011 統合**（17 個隨機試驗、10,801 位保留手術後照 vs 不照的女性；OA 全文）[S1]：照射把 **10 年任何首次復發（局部區域＋遠端）從 35.0% 降到 19.3%**（絕對降 15.7%，95% CI 13.7–17.7，2p<0.00001），**15 年乳癌死亡從 25.2% 降到 21.4%**（絕對降 3.8%，1.6–6.0，2p=0.00005）。
- 分淋巴結狀態（同一統合）[S1]：**pN0（n=7,287）**：10 年復發 31.0%→15.6%（絕對降 15.4%）、15 年乳癌死亡 20.5%→17.2%（絕對降 3.3%）；**pN+（n=1,050）**：10 年復發 63.7%→42.5%（絕對降 21.2%）、15 年乳癌死亡 51.3%→42.8%（絕對降 8.5%）。
- 比例效應的原文句（abstract 逐字）[S1]：「radiotherapy to the conserved breast **halves the rate** at which the disease recurs and **reduces the breast cancer death rate by about a sixth**」；換算關係：「about **one breast cancer death was avoided by year 15 for every four recurrences avoided by year 10**」。絕對獲益依個人風險而變、比例獲益各族群差不多——這是「配套但個人化」的數學骨架。
- **NSABP B-06 二十年**（1,851 人隨機：全切除 vs 單純腫瘤切除 vs 腫瘤切除＋照射）[S2]：同側乳房復發累積發生率**照射 14.3% vs 不照 39.2%**（P<0.001）；三組總存活無差（腫瘤切除＋照射 vs 全切除之死亡 HR 0.97，0.83–1.14）。地標可引其本體，「保留手術＋放療 vs 全切除等效」的完整論證屬 bc 專題，A1 一句話。

**MRM 後 N+ 建議 PMRT（證據本體＋2025 年的張力）**

- **EBCTCG 2014 PMRT 統合**（22 個試驗、8,135 位 1964–86 年隨機的女性；乳房切除＋腋下手術，照胸壁＋區域淋巴 vs 不照；OA）[S3]：
  - **腋下廓清＋1–3 顆陽性（n=1,314）**：局部區域復發 2p<0.00001、整體復發 RR 0.68（0.57–0.82）、**乳癌死亡 RR 0.80（0.67–0.95，2p=0.01）**；其中 1,133 人兩組都有全身治療（CMF 或 tamoxifen），結論不變（乳癌死亡 RR 0.78）。
  - **≥4 顆陽性（n=1,772）**：整體復發 RR 0.79（0.69–0.90）、**乳癌死亡 RR 0.87（0.77–0.99，2p=0.04）**。
  - **腋下廓清＋0 顆陽性（n=700）**：復發 RR 1.06、乳癌死亡 RR 1.18——**皆不顯著，N0 的 MRM 後不是常規適應症**。
  - EBCTCG 自己的但書（abstract 逐字）：「For today's women, who in many countries are at lower risk of recurrence, **absolute gains might be smaller** but proportional gains might be larger because of more effective radiotherapy.」
- 地標試驗由統合承載，書目已各自核對可列：**Danish 82b**（1,708 位停經前高風險，CMF±RT：10 年總存活 54% vs 45%，p<0.001）[S4]、**Danish 82c**（1,375 位停經後高風險，tamoxifen±RT：10 年存活 45% vs 36%，p=0.03）[S5]、**British Columbia 20 年**（318 位停經前 N+，16 次分次之區域照射：20 年總存活 47% vs 37%，RR 0.73，p=0.03）[S6]。注意 BC 試驗用的就是 **37.5 Gy/16 次**——「低分次照 N+」其實是這個 1970 年代試驗的原始設計，A2 可回收這個彩蛋。
- **SUPREMO（NEJM 2025，OA）**[S7]：國際隨機試驗，「中風險」＝pT1N1、pT2N1、pT3N0、或 pT2N0＋grade 3 或 LVI，乳房切除＋腋下手術＋現代全身治療後，胸壁照射（808 人）vs 不照（799 人），中位追蹤 9.6 年：**10 年總存活 81.4% vs 81.9%（HR 1.04，0.82–1.30，p=0.80）**；胸壁復發 9/808（1.1%）vs 20/799（2.5%），HR 0.45（0.20–0.99）。→ 1–3 顆這格的當代張力，深度歸 bc-rt-regional，A1 誠實帶到。
- 指引錨點：ESMO 2024 早期乳癌指引[S8]為書目錨（逐字條文取不到，FAIL-1）。

### Claim ceiling

- 可寫：「保留手術＋全乳照射是一套設計：手術把看得見的拿掉，照射處理殘存的顯微病灶——不照的話十年內約三分之一會再出事（35.0%→19.3%，17 個試驗統合）」；「每避免 4 個十年內的復發，十五年就少 1 個乳癌死亡（統合原句）」；「B-06 二十年：不照的同側復發 39.2%、照的 14.3%」；「乳房全切除後 1–3 顆淋巴結陽性：老統合顯示放療降乳癌死亡（RR 0.80），但用現代藥物重做的 SUPREMO 十年總存活沒差（81.4% vs 81.9%）、胸壁復發有差（1.1% vs 2.5%）——這格要跟醫師談，不是自動要或自動不要」；「≥4 顆陽性建議照（RR 0.87）且無現代試驗挑戰這格」；「全切除且淋巴結陰性，統合顯示照了沒好處（RR 1.06/1.18，不顯著）」。
- **不可寫**：「不照一定會復發」（不照者 10 年 65% 沒事）；「照了就不會復發」（照了仍 19.3%）；「放療延長所有人的壽命」（絕對獲益依風險層而變：pN0 低風險預測組 15 年死亡絕對降幅 0.1%，高風險組 7.8%[S1]）；「MRM 後 N+ 一定要照」（SUPREMO 張力，紅線意識）；「保留手術比全切除安全／全切除就不用放療」（前者是 bc 專題主場；後者被 N+ 條件推翻）。
- 深度指路：省略放療的高齡低風險族群 → bc-rt-omission；區域淋巴範圍與 SUPREMO 完整論證 → bc-rt-regional。本篇是診間地圖（PM／MRM × N 狀態，即 fig-brt-decision 的資料本體），不重複證據細節。

### Caveats

- EBCTCG 2011/2014 的族群是 1960–80 年代收案：絕對數字對今日病人偏高，寫的時候一律帶「統合、老年代、比例效應較可信」標籤；EBCTCG 2014 的但書原句就是給這件事用的[S3]。
- SUPREMO 的族群是「中風險」混合體（含 pT2N0 grade3/LVI 與 pT3N0），不等於「所有 1–3 顆」；且只照胸壁、不含區域淋巴——與 EBCTCG 2014 試驗（胸壁＋鎖骨上／腋下＋內乳都照）不是同一個介入。並陳時兩個標籤都要帶。
- pN+ 保留手術族群在 EBCTCG 2011 裡只有 1,050 人，數字信賴區間寬。
- fig-brt-decision 的四格（PM×N0、PM×N+、MRM×N0、MRM×N+）每格都有上面對應的數字可標；MRM×N+ 格內要再分 1–3 vs ≥4。

### 台灣現況

- 重大傷病：**乳房惡性腫瘤第一期（C50.011–C50.929）證明效期三年；其他乳癌（落在 C00.0–C96.9 其他惡性腫瘤類）五年**[S29][S30]。申請程序（診斷證明 30 日內有效、保險人 14 日內核定、免部分負擔範圍為「證明所載傷病及經診治醫師認定相關之治療」）法規原文都在[S29]。放療屬該傷病相關治療、適用免部分負擔——這句是辦法第 6 條的直接推論，寫成「依辦法規定，經醫師認定與乳癌相關的治療免部分負擔」即可，不要寫成「放療全部免費」。
- 「誰需要照」本身無給付爭點；分次與技術的給付歸 A2／B 組。

---

## A2 `brt-fractionation`〈幾次：療程長短怎麼定〉【紅線 2：並陳不裁贏家】

### Key facts

**院內做法（作者定案，寫成診間實況，不需文獻）**

- PM（保留手術）且 pT1–2N0 → 低分次（對應健保 36022B/36023B 的族群）；其餘（N+、MRM 後 PMRT、需照區域淋巴）→ 傳統分次。此段落以作者第一人稱寫，證據標籤標「院內政策」。

**低分次的證據本體（全乳／不含淋巴——院內低分次族群的靠山）**

- **START A/B 十年**（英國；pT1-3a pN0-1 M0，含保留手術與乳房切除）[S9]：START-B 40 Gy/15 次 vs 50 Gy/25 次：10 年局部區域復發 4.3% vs 5.5%（HR 0.77，0.51–1.16，p=0.21）；乳房縮小、微血管擴張、乳房水腫**40 Gy 組顯著較少**。START-A 41.6 Gy/13 次 vs 50 Gy：6.3% vs 7.4%（HR 0.91，p=0.65）。原文結論（abstract 逐字）：「appropriately dosed hypofractionated radiotherapy is safe and effective…The results support the continued use of 40 Gy in 15 fractions」。
- **加拿大 Whelan 試驗十年**（1,234 位保留手術、切緣乾淨、**腋下淋巴結陰性**）[S10]：10 年局部復發 42.5 Gy/16 次 6.2% vs 50 Gy/25 次 6.7%（絕對差 0.5 個百分點，95% CI −2.5 到 3.5）；外觀良好以上 69.8% vs 71.3%。
- **FAST-Forward**（英國；pT1-3 pN0-1，保留手術或乳房切除，**不含需腋下照射者**）：5 年[S11]與 10 年[S12]：26 Gy/5 次 10 年同側乳房復發 2.1%（1.5–3.1）vs 40 Gy/15 次 3.6%（2.7–4.9）；10 年中度／明顯乳房或胸壁變化 26 Gy 14.4% vs 40 Gy 13.1%（27 Gy 19.3%——劑量細節不是小事）。結論句（abstract 逐字）：「26 Gy in five fractions over 1 week is safe and efficacious…supporting its use as a standard of care.」腋下子研究 466 人、中位追蹤 7 年、32 例局部區域復發，原文自承「sample size limits precision of estima[tes]」[S12]。

**指引原文（並陳的國際側，逐字在手）**

- **ASTRO 2018 全乳照射指引**（abstract 逐字）[S13]：「For women with invasive breast cancer receiving WBI with or without inclusion of the low axilla, **the preferred dose-fractionation scheme is hypofractionated WBI to a dose of 4000 cGy in 15 fractions or 4250 cGy in 16 fractions.**」（注意適用範圍：全乳±低位腋下，不含區域淋巴。）
- **ESTRO-ACROP 2022 共識**（abstract 逐字）[S14]：「**moderately hypofractionated radiotherapy can be offered to any patient for whole breast, chest wall (with or without reconstruction), and nodal volumes.** Ultrafractionation (five fractions) can also be offered for non-nodal breast or chest wall (without reconstruction) radiotherapy either as standard of care or within a randomised trial or prospective cohort.」——歐洲已把中度低分次開到「任何病人、含胸壁重建與淋巴」，五次則限「非淋巴」。
- ESMO 2024 指引：書目錨[S8]，逐字取不到（FAIL-1）——寫「ESMO 同方向，原文我取不到可逐字引用的版本」或乾脆不引。

**PMRT／區域淋巴低分次的隨機試驗（國際側的第二層）**

- **Wang 2019**（中國醫科院腫瘤醫院單中心；820 位乳房切除後高風險：≥4 顆陽性或 T3-4；43.5 Gy/15 次 vs 50 Gy/25 次照胸壁＋淋巴）[S15]：5 年局部區域復發 8.3% vs 8.1%（HR 1.10，90% CI 0.72–1.69，非劣性 p<0.0001）；3 級急性皮膚毒性低分次組反而較少（3% vs 8%，p<0.0001）。標籤：單中心、中國、大多未做重建。
- **SKAGEN-1**（丹麥等 17 中心；2,908 位高風險 N+ 需區域照射；40 Gy/15 次 vs 50 Gy/25 次）[S16]：3 年手臂淋巴水腫 8.0% vs 9.4%（OR 0.84，0.62–1.14），在 +5% 非劣性邊界內；8 年內局部區域復發 HR 0.96（0.62–1.51）、乳癌死亡 HR 1.25（0.93–1.66，不顯著）、總死亡 HR 1.08。中位腫瘤學追蹤 5.25 年。
- **HypoG-01**（法國 29 中心；1,265 位需淋巴照射者；40 Gy/15 次 vs 50 Gy/25 次）[S17]：主要終點手臂淋巴水腫非劣性成立（HR 1.02，0.79–1.31，非劣性 p<0.001）；3 年累積發生率 23.4% vs 22.2%（測量定義敏感、數字高，與 SKAGEN 的 8–9% 定義不同，不可互比）；grade ≥3 不良事件 8% vs 13%。中位追蹤 4.8 年。

**院內保守的理由（並陳的另一邊，寫成「有名有姓的理由」不是「習慣」）**

- 三個可引用的理由：(1) N+／區域淋巴的低分次隨機資料**追蹤年限仍短**（SKAGEN 腫瘤學中位 5.25 年[S16]、HypoG-01 4.8 年[S17]，對照 START/Whelan 的十年）；(2) FAST-Forward 五次在腋下照射族群原文自承精確度不足[S12]；(3) 晚期正常組織效應（心臟、臂神經叢、纖維化）的時間尺度是十年以上——EBCTCG 2014 的乳癌死亡獲益也是 20 年尺度才完整顯現[S3]。另有本地制度事實：健保低分次包裹碼的適應症本來就排除淋巴照射[S26]。
- BC 試驗彩蛋（可作收尾梗）：1970 年代的 British Columbia 試驗照 N+ 用的就是 16 次（37.5 Gy/16 fx），20 年存活獲益成立[S6]——「低分次照淋巴」不是新發明，是繞了一圈回來。

### Claim ceiling

- 可寫：「全乳低分次十年資料成熟：15–16 次與 25 次復發無差、晚期外觀還較好（START-B、加拿大試驗）」；「一週五次 26 Gy 十年復發 2.1%，英國已寫成 standard of care（原文），但腋下照射族群原文自承樣本不足」；「美國指引 2018 年起把 15–16 次寫成全乳照射的『preferred』（原文）」；「歐洲共識 2022 年把 15 次開到含淋巴與重建後胸壁（原文）」；「N+ 的低分次隨機試驗已有三個（中國、丹麥、法國），復發與淋巴水腫都沒有更差」；「我們醫院對 N+ 與乳房切除後仍用 25 次：因為這些試驗追蹤還在 5 年上下、五次方案在淋巴族群證據不足、而且晚期副作用是十年尺度的事——這是保守，不是落後」；「健保的低分次包裹給付碼，適應症寫的正是保留手術後、不含淋巴照射的族群（條文原文）」。
- **不可寫**（紅線 2 兩個方向都要守）：「25 次是舊時代、15 次才對」／「N+ 用 15 次還不安全」——兩邊都不可判死；「五次適合所有人」（FAST-Forward 腋下族群＋27 Gy 的正常組織教訓[S12]）；「健保不給付低分次」（有專屬碼，是族群限定[S26]）；「國際指引要求 N+ 也要低分次」（ESTRO 用語是 can be offered，ASTRO 2018 範圍只到低位腋下——措辭等級要照抄，不升級）；不可把 HypoG-01 的 23.4% 淋巴水腫與 SKAGEN 的 8.0% 並列比較（定義不同）；不可展開「省略放療」（bc-rt-omission 主場）與 boost 取捨細節（bc-rt-hypofx 主場）。
- 病人拿著這篇問「為什麼我不是低分次」必須問得出口，答案在文中已鋪好：你的淋巴結狀態／手術型式／是否照淋巴決定分組；如果你是 N+，院內選 25 次的三個理由如上；你可以問醫師「我的情況適不適用新的 15 次資料」——這句要真的寫進文章。

### Caveats

- START 含乳房切除後胸壁照射、Whelan 只有保留手術 N0、FAST-Forward 不含需腋下照射者——三個試驗的族群邊界不同，引用時逐一標。
- Wang 2019 的分次是 43.5 Gy/15 次（不是 40 Gy）、族群是 ≥4 顆或 T3-4——不能直接搬到 1–3 顆。
- SKAGEN-1 乳癌死亡 HR 1.25（0.93–1.66）雖不顯著，寫的時候不可只寫「無差」三個字了事——誠實寫「點估計偏高、信賴區間跨 1、追蹤仍在延長」。
- 「次數少＝輕鬆」的暗示要避免：單次劑量較高、皮膚反應高峰常在療程結束後（C2 主場，一句指路）。
- 分次深度證據（26 vs 27 Gy、boost、APBI）→ bc-rt-hypofx 指路，不重列。

### 台灣現況

- **健保低分次包裹碼（條文原文，2022-10-12 建檔版 PDF）**[S26]：36022B「乳癌術後低分次全乳照射合併局部加強照射放射治療」279,986 點、療程 20 次；36023B「無合併局部加強照射」246,960 點、療程 16 次。適應症與禁忌症逐字見 ⚠2。包裹給付、未完成按比例核扣；原則限國健署「通過癌症診療品質認證醫院名單」申報，否則須乳房醫學會＋放射腫瘤醫學會共同訪視認證[S26][S28]。
- 健保問答集（第四版 1140211）[S27]：36022B/36023B/**36024B** 支付標準所訂次數為「20/16/5 次」——**五次的申報架構存在**；但 36024B 的完整品項名稱與適應症條文未取得（FAIL-4），只能寫「五次的給付條件要跟醫院確認」。
- **2025-10-29 修正草案**[S28]：刪除 36022B/36023B 禁忌症「以符合國際臨床指引」；同份草案新增 36025B–36027B 質子放射治療三項（**限未滿十九歲**、事前審查、每人每次原發癌一生一次——B3 的台灣端素材，轉交 B 組）。現行生效版未確認（FAIL-2）：文章寫「條文正在往國際方向修，實際適用以就醫當時規定為準，可問醫務課」。
- 傳統分次（25 次）走一般放射治療診療項目申報，無單獨爭點；DIBH／TOMO／質子的收費身分歸 B 組查證清單。

---

## A3 `brt-technique-map`〈IMRT、TOMO、質子、DIBH 是什麼關係〉【骨架篇】

### Key facts

**IMRT 是現行標準（隨機證據：對 2D/楔形板的優勢）**

- **加拿大多中心雙盲隨機試驗**（Pignol 2008；358 人隨機、331 人分析）[S18]：乳房 IMRT vs 楔形板標準照射：**濕性脫屑 31.2% vs 47.8%（P=0.002）**；多變項中 IMRT（P=0.003）與較小乳房（P<0.001）獨立降低濕性脫屑風險；濕性脫屑與疼痛（P=0.002）、生活品質下降（P=0.003）相關。
- **英國 Royal Marsden 隨機試驗**（Donovan 2007；306 人，5 年照片評估）[S19]：2D 組 58% 出現乳房外觀改變 vs IMRT 組 40%；2D 組風險 1.7 倍（95% CI 1.2–2.5，p=0.008）；IMRT 組可觸摸硬結顯著較少。
- **劍橋隨機試驗 5 年**（Mukesh 2013；1,145 人分析，劑量不均者隨機）[S20]：簡單 IMRT vs 標準：整體外觀不佳 OR 0.68（0.48–0.96，p=0.027）、皮膚微血管擴張 OR 0.58（p=0.021）。原文結論：「These results are practice changing and should encourage centres still using two-dimensional RT to implement simple breast IMRT.」
- 三個試驗共同的機轉句：IMRT 的好處來自**劑量均勻度**（消掉熱點），這是「基本款 IMRT 本身就有作為」的證據本體——紅線 1 的安全閥在 A3 就要立起來，B1/B2 引用不重立。

**DIBH 是「姿勢／技術疊加」不是「機器」（定義逐字，OA 全文）**

- Bergom 2018（Front Oncol 綜述，PMC 全文逐字）[S21]：「**Deep inspiration breath hold (DIBH) is a technique that takes advantage of a more favorable position of the heart during inspiration to minimize heart doses** over a course of radiation therapy.」機轉句：「during inspiration, **the flattening of the diaphragm and expansion of the lungs pulls the heart away from the [chest wall]**. During both simulation and treatment, the patient takes a deep breath and then holds it for a period of time during which radiation is administered.」另有可用細節：自由呼吸下的呼吸調控（gating）對心臟閃避通常無效（心臟在正常呼吸週期中不會大幅離開胸壁）；vDIBH 與 ABC 兩種做法效果相當（UK HeartSpare）。
- 台灣族群相關統合（左側乳癌、VMAT，劑量學終點）[S22]：DIBH 相對自由呼吸降低平均心臟劑量（SMD −1.40）、左前降支（−1.65）、同側肺（−0.57）。**標籤：劑量學，不是臨床事件**——證據等級標籤照 SPEC §一1 的鏈條寫法，臨床端接 Darby 2013（每 Gy 冠心事件率 +7.4%，無閾值）[S24]，完整論證歸 B1。
- 骨架句：DIBH 可疊加在 2D/3D/IMRT/VMAT/TOMO 任何光子技術上（機器不同、姿勢同一件事）——fig-brt-technique-map 的縱軸。

**TOMO 與質子（一句話定位，深度歸 B2/B3）**

- TOMO：螺旋斷層方式執行的強度調控治療，屬 IMRT 家族的進階給法；現有小型回溯比較（315 人、追蹤 3 個月）顯示其急性不良事件並非全面較優：放射性肺炎較低（0% vs 4.3%，p=0.016）、3–4 級皮膚毒性反而較高（16.2% vs 7.6%，p=0.017）[S25]——A3 只用來支撐「差異在特定情境、適應症決定」的一句話，數字本身留給 B2 決定是否使用。
- 質子：比較質子與光子的實務型隨機試驗 RadComp 正在進行，主要終點是主要心血管事件[S23]；**主要終點截至 2026-08-31 未發表**（本日再查 Europe PMC，僅有計畫書與 PRO 驗證、甲狀腺、劑量-生活品質等附屬研究，FAIL-3）→ A3 的質子句只能寫「劑量學上更集中、臨床優勢的隨機答案還沒讀出、需轉診」，物理與法規指路 nt-proton／insight-proton。

### Claim ceiling

- 可寫：「IMRT 對舊式照法的優勢是隨機試驗等級：濕性脫屑 31% vs 48%、五年外觀變化 40% vs 58%、外觀不佳 OR 0.68——所以健保給付的一般 IMRT 不是陽春款，是把熱點消掉的現行標準」；「DIBH 是深吸氣讓橫膈下降、把心臟拉離胸壁的技術（綜述原文），可以疊加在任何光子機器上——它是姿勢，不是機器」；「DIBH 的降幅目前是劑量學證據（統合），心臟劑量與臨床事件的關係是世代級證據（Darby），兩層分開標」；「TOMO 是 IMRT 的螺旋式進階給法，差異出現在特定情境（詳見 B2）」；「質子的隨機試驗還沒讀出主要結果」。
- **不可寫**（紅線 1 雙向）：「不自費就顧不到心臟」（一般 IMRT 的心臟閃避作為要成段存在——用 [S18][S19][S20] 的均勻度邏輯＋B1 的心臟段落鋪）；「TOMO/質子跟一般 IMRT 都一樣」（劑量學差異不可寫小——但 A3 只立骨架，數字歸 B 組）；「DIBH 可以降低心臟病風險」（臨床事件未證，只能寫劑量學＋Darby 鏈條）；「質子比較安全／比較好」（RadComp 未讀出，作者本人是放腫醫師這條特別要守）；「IMRT 試驗證明現在每個人都該用 IMRT」（試驗對照組是 2D/楔形板，今日已無人用 2D——優勢是對「舊式」，不是對 3D 適形的全面碾壓，Mukesh 試驗只隨機了劑量不均者[S20]）。
- 技術選擇的句式固定為「適應症決定，不是預算決定」；費用一律留給 B 組的誠實段。

### Caveats

- 三個 IMRT 試驗用的「標準組」是楔形板／2D 時代技術；引用時標年代（2003–2007 收案），避免讀者以為對照的是今日的 3D。
- [S25] 追蹤僅 3 個月、回溯、單中心（中國陸軍軍醫大學）——A3 若引用只能當「不是全面升級」的反例，不可反過來寫成「TOMO 比較傷皮膚」的定論。
- fig-brt-technique-map 的資料本體：橫軸（3D→IMRT→TOMO／質子＝劑量分布逐步精細）、縱軸（DIBH 可疊加）、每格標「健保／自費／轉診」的欄位資料要等 B 組台灣端查證回來才能填——A3 文章先用文字骨架，圖的費用欄位與 B 組對稿。

### 台灣現況

- IMRT／弧形／TOMO 的健保與自費身分、DIBH 收費身分：SPEC §七歸 B 組查證，A3 不重查；本組僅確認 2025-10-29 草案新增之質子診療項目 36025B–36027B **限未滿十九歲**［S28］——成人乳癌質子在健保架構內沒有位置，自費與轉診現況歸 B3。A3 文章對費用只寫一句「各技術的健保與自費身分見本專題 B 組各篇」。

---

## 給 B/C 組的協調備註

- A3 立技術骨架與 IMRT 隨機證據本體（[S18][S19][S20]）＋DIBH 定義（[S21]）；B1 寫心臟深度（Darby [S24] 的完整論證、DIBH 降幅數字）、B2 寫 TOMO 差異情境、B3 寫質子——不重立骨架，引 A3 的來源 ID 即可。
- [S28] 草案的質子三項（36025B–36027B 限未滿十九歲、事前審查、一生一次）是 B3 的台灣端現成素材；B3 仍須查 KCGMH 等自費公告。
- A2 擁有分次並陳的證據本體與健保 36022B/36023B/36024B 條文（[S26][S27][S28]）；C1 寫療程時間感時引 A2 結論句，不重列試驗數字。
- 重大傷病（乳癌第一期三年／其餘五年，[S29][S30]）由 A1 寫完整，其他篇一句話。
- SKAGEN-1 的 3 年淋巴水腫數字（8.0%/9.4%）與 HypoG-01（23.4%/22.2%）定義不同——若 C3/D 組要引淋巴水腫數字，注意不可跨試驗互比。

---

## Sources（單一序列；PASS 才可入正文）

**A1 誰需要（統合與地標）**

- [S1] **PASS（OA，abstract 逐字核對；PMCID PMC3254252）** Early Breast Cancer Trialists' Collaborative Group (EBCTCG), Darby S, McGale P, et al. Effect of radiotherapy after breast-conserving surgery on 10-year recurrence and 15-year breast cancer death: meta-analysis of individual patient data for 10,801 women in 17 randomised trials. *Lancet*. 2011;378(9804):1707–1716. DOI: 10.1016/S0140-6736(11)61629-2. PMID 22019144. https://doi.org/10.1016/S0140-6736(11)61629-2 — Route: Europe PMC REST（DOI 引號查詢）
- [S2] **PASS** Fisher B, Anderson S, Bryant J, et al. Twenty-year follow-up of a randomized trial comparing total mastectomy, lumpectomy, and lumpectomy plus irradiation for the treatment of invasive breast cancer. *N Engl J Med*. 2002;347(16):1233–1241. DOI: 10.1056/NEJMoa022152. PMID 12393820. https://doi.org/10.1056/NEJMoa022152 — Route: Europe PMC REST（DOI）
- [S3] **PASS（OA；PMCID PMC5015598）** EBCTCG (Early Breast Cancer Trialists' Collaborative Group), McGale P, Taylor C, et al. Effect of radiotherapy after mastectomy and axillary surgery on 10-year recurrence and 20-year breast cancer mortality: meta-analysis of individual patient data for 8135 women in 22 randomised trials. *Lancet*. 2014;383(9935):2127–2135. DOI: 10.1016/S0140-6736(14)60488-8. PMID 24656685. https://doi.org/10.1016/S0140-6736(14)60488-8 — Route: Europe PMC REST（DOI 引號查詢）
- [S4] **PASS** Overgaard M, Hansen PS, Overgaard J, et al. Postoperative radiotherapy in high-risk premenopausal women with breast cancer who receive adjuvant chemotherapy. Danish Breast Cancer Cooperative Group 82b Trial. *N Engl J Med*. 1997;337(14):949–955. DOI: 10.1056/NEJM199710023371401. PMID 9395428. https://doi.org/10.1056/NEJM199710023371401 — Route: Europe PMC REST（DOI）
- [S5] **PASS** Overgaard M, Jensen MB, Overgaard J, et al. Postoperative radiotherapy in high-risk postmenopausal breast-cancer patients given adjuvant tamoxifen: Danish Breast Cancer Cooperative Group DBCG 82c randomised trial. *Lancet*. 1999;353(9165):1641–1648. DOI: 10.1016/S0140-6736(98)09201-0. PMID 10335782. https://doi.org/10.1016/S0140-6736(98)09201-0 — Route: Europe PMC REST（TITLE → DOI 核對）
- [S6] **PASS** Ragaz J, Olivotto IA, Spinelli JJ, et al. Locoregional radiation therapy in patients with high-risk breast cancer receiving adjuvant chemotherapy: 20-year results of the British Columbia randomized trial. *J Natl Cancer Inst*. 2005;97(2):116–126. DOI: 10.1093/jnci/djh297. PMID 15657341. https://doi.org/10.1093/jnci/djh297 — Route: Europe PMC REST（TITLE → DOI 核對）。**注意：網路上流傳的 DOI dji021 是錯的（那是另一篇統合），正確為 djh297——撰稿人引用時照本表抄**
- [S7] **PASS（OA；PMCID PMC7618363）** Kunkler IH, Russell NS, Anderson N, et al. Ten-Year Survival after Postmastectomy Chest-Wall Irradiation in Breast Cancer. *N Engl J Med*. 2025;393(18):1771–1783. DOI: 10.1056/NEJMoa2412225. PMID 41191939. https://doi.org/10.1056/NEJMoa2412225 — Route: Europe PMC REST（DOI）。（SUPREMO）
- [S8] **PASS（僅書目；逐字條文不可引，見 FAIL-1）** Loibl S, André F, Bachelot T, et al. Early breast cancer: ESMO Clinical Practice Guideline for diagnosis, treatment and follow-up. *Ann Oncol*. 2024;35(2):159–182. DOI: 10.1016/j.annonc.2023.11.016. PMID 38101773. https://doi.org/10.1016/j.annonc.2023.11.016 — Route: Europe PMC REST（DOI）

**A2 分次**

- [S9] **PASS** Haviland JS, Owen JR, Dewar JA, et al. The UK Standardisation of Breast Radiotherapy (START) trials of radiotherapy hypofractionation for treatment of early breast cancer: 10-year follow-up results of two randomised controlled trials. *Lancet Oncol*. 2013;14(11):1086–1094. DOI: 10.1016/S1470-2045(13)70386-3. PMID 24055415. https://doi.org/10.1016/S1470-2045(13)70386-3 — Route: Europe PMC REST（DOI 引號查詢，abstract 數字逐一核對）
- [S10] **PASS** Whelan TJ, Pignol JP, Levine MN, et al. Long-term results of hypofractionated radiation therapy for breast cancer. *N Engl J Med*. 2010;362(6):513–520. DOI: 10.1056/NEJMoa0906260. PMID 20147717. https://doi.org/10.1056/NEJMoa0906260 — Route: Europe PMC REST（DOI）
- [S11] **PASS（OA；PMCID PMC7262592）** Murray Brunt A, Haviland JS, Wheatley DA, et al. Hypofractionated breast radiotherapy for 1 week versus 3 weeks (FAST-Forward): 5-year efficacy and late normal tissue effects results from a multicentre, non-inferiority, randomised, phase 3 trial. *Lancet*. 2020;395(10237):1613–1626. DOI: 10.1016/S0140-6736(20)30932-6. PMID 32580883. https://doi.org/10.1016/S0140-6736(20)30932-6 — Route: Europe PMC REST（DOI 引號查詢）
- [S12] **PASS** Brunt AM, Cafferty FH, Kirby AM, et al. Hypofractionated breast radiotherapy for 1 week versus 3 weeks (FAST-Forward): 10-year efficacy and late normal tissue effects from a multicentre, open-label, non-inferiority, phase 3, randomised controlled trial and 5-year efficacy results from a randomised axillary substudy. *Lancet Oncol*. 2026;27(6):686–698. DOI: 10.1016/S1470-2045(26)00076-8. PMID 42134381. https://doi.org/10.1016/S1470-2045(26)00076-8 — Route: Europe PMC REST（DOI 引號查詢，abstract 數字逐一核對）
- [S13] **PASS（「preferred…4000 cGy in 15 fractions or 4250 cGy in 16 fractions」為 abstract 逐字）** Smith BD, Bellon JR, Blitzblau R, et al. Radiation therapy for the whole breast: Executive summary of an American Society for Radiation Oncology (ASTRO) evidence-based guideline. *Pract Radiat Oncol*. 2018;8(3):145–152. DOI: 10.1016/j.prro.2018.01.012. PMID 29545124. https://doi.org/10.1016/j.prro.2018.01.012 — Route: Europe PMC REST（DOI，resultType=core 取 abstract）
- [S14] **PASS（「can be offered to any patient for whole breast, chest wall…and nodal volumes」等為 abstract 逐字）** Meattini I, Becherini C, Boersma L, et al. European Society for Radiotherapy and Oncology Advisory Committee in Radiation Oncology Practice consensus recommendations on patient selection and dose and fractionation for external beam radiotherapy in early breast cancer. *Lancet Oncol*. 2022;23(1):e21–e31. DOI: 10.1016/S1470-2045(21)00539-8. PMID 34973228. https://doi.org/10.1016/S1470-2045(21)00539-8 — Route: Europe PMC REST（DOI 引號查詢，resultType=core 取 abstract）
- [S15] **PASS** Wang SL, Fang H, Song YW, et al. Hypofractionated versus conventional fractionated postmastectomy radiotherapy for patients with high-risk breast cancer: a randomised, non-inferiority, open-label, phase 3 trial. *Lancet Oncol*. 2019;20(3):352–360. DOI: 10.1016/S1470-2045(18)30813-1. PMID 30711522. https://doi.org/10.1016/S1470-2045(18)30813-1 — Route: Europe PMC REST（DOI 引號查詢）。**出版年為 2019，任務單寫的「Wang 2020」應更正**
- [S16] **PASS** Offersen BV, Alsner J, Høgsbjerg K, et al.; DBCG RT Committee. Hypo- Versus Standard Fractionated Locoregional Radiotherapy of Patients With High-Risk Breast Cancer in the Randomized Phase III Trial: The Danish Breast Cancer Group Skagen Trial 1. *J Clin Oncol*. 2026;44(24):2278–2289. DOI: 10.1200/JCO-25-02705. PMID 42492022. https://doi.org/10.1200/JCO-25-02705 — Route: Europe PMC REST（"Skagen Trial 1" 關鍵字 → DOI 核對，abstract 數字逐一核對）
- [S17] **PASS** Rivera S, Ghodssighassemabadi R, Auzac G, et al.; HypoG-01 trialists. 5-year results of hypofractionated locoregional radiotherapy in early breast cancer HypoG-01 (UNICANCER): a French multicentre, randomised, non-inferiority, phase 3, open-label, controlled trial. *Lancet*. 2026;407(10532):976–987. DOI: 10.1016/S0140-6736(25)02597-8. PMID 41794436. https://doi.org/10.1016/S0140-6736(25)02597-8 — Route: Europe PMC REST（"HypoG-01" 關鍵字 → DOI 核對，abstract 數字逐一核對）

**A3 技術**

- [S18] **PASS** Pignol JP, Olivotto I, Rakovitch E, et al. A multicenter randomized trial of breast intensity-modulated radiation therapy to reduce acute radiation dermatitis. *J Clin Oncol*. 2008;26(13):2085–2092. DOI: 10.1200/JCO.2007.15.2488. PMID 18285602. https://doi.org/10.1200/JCO.2007.15.2488 — Route: Europe PMC REST（DOI）
- [S19] **PASS** Donovan E, Bleakley N, Denholm E, et al.; Breast Technology Group. Randomised trial of standard 2D radiotherapy (RT) versus intensity modulated radiotherapy (IMRT) in patients prescribed breast radiotherapy. *Radiother Oncol*. 2007;82(3):254–264. DOI: 10.1016/j.radonc.2006.12.008. PMID 17224195. https://doi.org/10.1016/j.radonc.2006.12.008 — Route: Europe PMC REST（DOI）
- [S20] **PASS** Mukesh MB, Barnett GC, Wilkinson JS, et al. Randomized controlled trial of intensity-modulated radiotherapy for early breast cancer: 5-year results confirm superior overall cosmesis. *J Clin Oncol*. 2013;31(36):4488–4495. DOI: 10.1200/JCO.2013.49.7842. PMID 24043742. https://doi.org/10.1200/JCO.2013.49.7842 — Route: Europe PMC REST（DOI）。（劍橋乳房 IMRT 試驗）
- [S21] **PASS（OA，定義句經 fullTextXML 逐字擷取；PMCID PMC5893752）** Bergom C, Currey A, Desai N, Tai A, Strauss JB. Deep Inspiration Breath Hold: Techniques and Advantages for Cardiac Sparing During Breast Cancer Irradiation. *Front Oncol*. 2018;8:87. DOI: 10.3389/fonc.2018.00087. PMID 29670854. https://doi.org/10.3389/fonc.2018.00087 — Route: Europe PMC REST（DOI）→ PMC5893752 fullTextXML
- [S22] **PASS（OA；劑量學終點，非臨床事件；PMCID PMC13035160）** Chiang PY, Huang PJ, Hung CH, Lin CP, Chang CC. Deep inspiration breath hold versus free breathing in postoperative radiotherapy strategy for patients with left-sided breast cancer treated with volumetric modulated arc therapy: A meta-analysis and systematic review. *PLoS One*. 2026;21(3):e0345614. DOI: 10.1371/journal.pone.0345614. PMID 41911243. https://doi.org/10.1371/journal.pone.0345614 — Route: Europe PMC REST（DOI）
- [S23] **PASS（僅計畫書；主要終點未發表，見 FAIL-3）** Bekelman JE, Lu H, Pugh S, et al. Pragmatic randomised clinical trial of proton versus photon therapy for patients with non-metastatic breast cancer: the Radiotherapy Comparative Effectiveness (RadComp) Consortium trial protocol. *BMJ Open*. 2019;9(10):e025556. DOI: 10.1136/bmjopen-2018-025556. PMID 31619413. PMCID PMC6797426. https://doi.org/10.1136/bmjopen-2018-025556 — Route: Europe PMC REST（DOI）
- [S24] **PASS** Darby SC, Ewertz M, McGale P, et al. Risk of ischemic heart disease in women after radiotherapy for breast cancer. *N Engl J Med*. 2013;368(11):987–998. DOI: 10.1056/NEJMoa1209825. PMID 23484825. https://doi.org/10.1056/NEJMoa1209825 — Route: Europe PMC REST（DOI）。（每 Gy +7.4%、無閾值；完整論證歸 B1）
- [S25] **PASS（OA；回溯世代、追蹤 3 個月、單中心——引用限「非全面優勢」一句話等級；PMCID PMC12582959）** [作者群見 API] Comparison of adverse events between intensity-modulated radiation therapy and tomotherapy for early stage breast cancer: a retrospective cohort study. *Front Oncol*. 2025;15:1654609. DOI: 10.3389/fonc.2025.1654609. PMID 41195267. https://doi.org/10.3389/fonc.2025.1654609 — Route: Europe PMC REST（TITLE 關鍵字 → DOI 核對）

**台灣官方文件**

- [S26] **PASS（2026-08-31 重新下載核對；curl HTTP 200，216,940 bytes；PDF 建檔 2022-10-12）** 衛生福利部中央健康保險署。《全民健康保險醫療服務給付項目及支付標準》中含適應症且表定點數≧10萬點之項目一覽——36022B（279,986 點、20 次）、36023B（246,960 點、16 次）之完整適應症、禁忌症、包裹給付與認證醫院條件原文。URL: https://www.nhi.gov.tw/ch/dl-12586-80c56ca7db574cc9bd9d567537efd169-1.pdf — Route: curl 下載 → pdftotext -layout → grep 原文。**建檔於 2022 年，禁忌症是否仍為現行生效版須以 [S28]／FAIL-2 對照，文章寫「條文調整中」**
- [S27] **PASS（2026-08-31 重新下載核對；curl HTTP 200，225,836 bytes）** 衛生福利部中央健康保險署。《全民健康保險醫療服務給付項目及支付標準癌症低分次放射治療相關診療項目之問答集及申報範例》第四版 1140211——36022B/36023B/36024B 採包裹給付、未完成療程按比例核扣、支付標準所訂次數「20/16/5 次」原文。URL: https://www.nhi.gov.tw/ch/dl-42468-1634a5de2b1a4295a94838b69a98e712-1.pdf — Route: curl 下載 → pdftotext -layout → grep 原文
- [S28] **PASS（草案文件本身；2026-08-31 重新下載核對；curl HTTP 200，605,976 bytes）** 行政院公報第 031 卷第 203 期（2025-10-29）衛生勞動篇：《全民健康保險醫療服務給付項目及支付標準部分診療項目修正草案》。已 grep 原文確認：(a)「修正 36022B『乳癌術後低分次照射合併局部加強照射放射治療』等二項診療項目，刪除禁忌症以符合國際臨床指引」；(b) 修正對照表中新版 36022B/36023B 之「註」已無禁忌症段；(c) 新增 36025B（676,111 點）／36026B（1,030,540 點）／36027B（1,266,499 點）質子放射治療，皆「限未滿十九歲者申報」、須事前審查、每人每次原發性癌症一生限執行一次。URL: https://gazette.nat.gov.tw/EG_FileManager/eguploadpub/eg031203/ch08/type3/gov70/num57/images/Eg01.pdf — Route: curl 下載 → pdftotext -layout → grep 原文。**草案≠現行生效條文（FAIL-2）**
- [S29] **PASS（2026-08-31 重新抓取；curl HTTP 200，54,084 bytes）** 〈全民健康保險保險對象免自行負擔費用辦法〉全文（重大傷病申請文件、診斷證明書 30 日內有效、保險人 14 日內〔不含例假日〕核定、第 6 條免部分負擔範圍）。法務部全國法規資料庫，pcode=L0060015。https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=L0060015 — Route: curl 直接 GET → 去標籤 grep 原文
- [S30] **PASS（2026-08-31 重新下載；curl HTTP 200，433,100 bytes，pdftotext 核對）** 同辦法第二條附表一「全民健康保險重大傷病項目及其證明有效期限」（含 113-12-31 前與 114-01-01 起兩版）：114 版「C50.011–C50.929 (三)乳房惡性腫瘤第一期……三年」「C00.0–C96.9 (五)除(一)-(四)之其他惡性腫瘤……五年」。https://law.moj.gov.tw/LawClass/LawGetFile.ashx?FileId=0000375263&lan=C — Route: curl 下載附件 PDF → pdftotext → grep 原文

---

## FAIL 清單（含「這個洞怎麼寫」）

- **FAIL-1 — ESMO 2024 早期乳癌指引之逐字建議條文。** annonc 全文非 OA，Europe PMC 無 fullTextXML；書目已核對（[S8]）。**怎麼寫**：A2 的指引段以 ASTRO［S13］與 ESTRO-ACROP［S14］的逐字為主體，ESMO 只寫「歐洲腫瘤內科學會的指引同此方向」不加引號；或乾脆不提 ESMO。
- **FAIL-2 — 36022B/36023B 現行生效版禁忌症條文（2025-10-29 草案是否已公告生效）與 36024B 完整品項名稱／適應症。** 已檢索：nhi.gov.tw HTML 對 curl 403（Cloudflare）；已下載可得之 2022 建檔版支付標準摘錄 PDF（[S26]）、問答集（[S27]）、行政院公報草案（[S28]）——三者皆到手，但「整合後現行生效條文」無法取得。**怎麼寫**：不寫死禁忌症現況；寫「給付條文這幾年在往國際指引方向修（公報原文可引），你就醫當時適用哪一版，請問醫務課或個管師」。**出版前若 nhi.gov.tw 放出新版 PDF，值得再查一次。**
- **FAIL-3 — RadComp 主要臨床終點（主要心血管事件）結果。** 2026-08-31 再查 Europe PMC（"RADCOMP" AND proton，2024–2026）：僅有計畫書[S23]、PRO 驗證（PMID 38739047）、甲狀腺附屬研究（PMID 41692352）、心臟劑量與生活品質關聯（PMID 42479004）。**怎麼寫**：A3/B3 一律「隨機答案還沒讀出」；不得寫「質子比較好／比較安全」。
- **FAIL-4 — 台灣 DIBH、TOMO、成人質子之健保／自費身分。** 屬 SPEC §七 B 組查證範圍，本組未查（僅意外取得 36025B–36027B 限未滿十九歲之草案原文，已轉交）。**怎麼寫**：A3 對費用只寫指路句。
- **FAIL-5 — NCCN 乳癌指引。** 專業版 403，依任務指示不引。**怎麼寫**：指引錨點用 ASTRO/ESTRO/EBCTCG/ESMO 書目替代，全文任何地方不出現「NCCN 建議」。

---

## 給 SPEC 的修正建議（查證結果與 SPEC 假設不符處，逐條）

1. **SPEC §一3「國際指引已放寬的方向」建議升級措辭**：國際側現在是「隨機試驗讀出（Wang 2019、SKAGEN-1 2026、HypoG-01 2026）＋指引原文（ASTRO 2018、ESTRO-ACROP 2022）」雙層。A2 的並陳若只寫「指引放寬」會低估對面；院內保守理由建議照本 brief A2 Caveats 的三條寫（追蹤年限、五次在淋巴族群證據不足、晚期效應時間尺度），這樣兩邊都立得住，紅線 2 才守得住。
2. **SPEC §四 A1 的「MRM 後 N+ 建議 PMRT」**：1–3 顆這格因 SUPREMO（2025 讀出）已是張力地帶，建議 SPEC 註記「1–3 顆寫成『要談的決定』、≥4 顆寫成『建議』」，與已發布的 bc-rt-regional 口徑一致。
3. **任務單「Wang 2020」應為 Wang 2019**（Lancet Oncol 2019;20:352–360）[S15]。
4. **台灣端新事實**：(a) 重大傷病乳癌第一期效期**三年**（非五年）[S30]——C 組／行政段落引用時要分期別；(b) 健保 36022B/36023B 禁忌症刪除草案已刊行政院公報[S28]——出版前需重查生效狀態（FAIL-2）；(c) 草案內質子診療項目限未滿十九歲[S28]——B3 可直接引用，成人乳癌質子在健保無位置這件事有官方文件形狀。
5. **SPEC §六 fig-brt-technique-map**：「基本款那格要真實」的數據本體是 [S18][S19][S20]（IMRT 隨機三連）；TOMO 格不可預設「全面較優」（[S25] 反例）——圖說建議寫「差異出現在特定情境」，與 B2 對稿後定案。
