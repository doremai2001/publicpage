# B 組研究查證 brief — 乳癌專題（階段二：治療怎麼決定）

查證日期：2026-08-29（任務書寫 2026-08-27，以系統日期為準；差兩天，不影響任何結論）
查證路徑：期刊文獻一律經 Europe PMC REST（`EXT_ID:` / `DOI:` 查詢）；
指引以官方頁面或 Europe PMC 書目確認；台灣以 `www.nhi.gov.tw`「藥品給付規定」現行合訂本
（第 5 節、第 9 節，網站標示 115.8.21 更新）與「修訂對照表」原始 PDF 為準。

**寫作前必讀（會改變 SPEC 假設的三件事，詳見文末「給 SPEC 的修正建議」）：**
1. B1 的「保留 vs 全切等效」證據**只來自 1970 年代開始收案的兩個試驗**，而 2020 年代的
   大型世代研究反而顯示保留＋放療**優於**全切；紅線 4 目前寫成「等效」，方向是安全的，
   但「保留不會比較差」比「兩者一樣」更貼近現在的證據。
2. B2 的 INSEMA 第二次隨機分派（前哨淋巴結巨轉移者省略腋清）**數字方向是不利的**
   （5 年 iDFS 86.6% vs 93.8%，HR 1.69，p=0.058），不能寫成「腋清可以省」。
3. B4 的 RxPONDER「停經前有化療效益」在 2026 年被 AMH 分析改寫成
   「卵巢儲備正常者才有效益」——這強化紅線 1，但也讓「年齡／停經狀態」這句話需要更精確。

---

# B1 — 保留乳房還是切除，存活一樣嗎 【紅線 4】

**Key facts**

- Veronesi 試驗（義大利，1973–1980 收案，n=701，腫瘤 ≤2 cm 的可手術乳癌，未分亞型；
  當年無 ER/HER2 分型）：象限切除＋患側乳房放療 vs Halsted 根除性乳房切除，
  中位追蹤 20 年，全死因死亡率 41.7%（保留組）vs 41.2%（根除組），P=1.0；
  乳癌死亡率 26.1% vs 24.3%，P=0.8 [S1]
- 同一試驗：20 年同側乳房內復發累積發生率 8.8%（保留組，30/352）vs 2.3%（根除組，8/349），
  P<0.001——**局部復發不一樣，存活一樣** [S1]
- NSABP B-06（美國，1976 年起收案，n=1,851，第 I/II 期侵犯性乳癌，未分亞型）：
  20 年追蹤，腫瘤切除＋放療 vs 全乳房切除的死亡風險比 HR 0.97（95% CI 0.83–1.14，P=0.74）；
  腫瘤切除**未加放療** vs 全乳房切除 HR 1.05（95% CI 0.90–1.23，P=0.51） [S2]
- 同一試驗：20 年同側乳房內復發 14.3%（腫瘤切除＋放療）vs **39.2%**（腫瘤切除未放療），
  P<0.001 [S2]
- EBCTCG 個別病人資料統合分析（17 個隨機試驗、10,801 名接受保留手術的女性，
  多數為 1980–1990 年代、未分子分型）：放療把 10 年任何首次復發從 35.0% 降到 19.3%
  （絕對降低 15.7%，95% CI 13.7–17.7），15 年乳癌死亡從 25.2% 降到 21.4%
  （絕對降低 3.8%，95% CI 1.6–6.0） [S3]
- 同一統合分析，淋巴結陰性（pN0，n=7,287）：10 年復發 31.0%→15.6%；
  15 年乳癌死亡 20.5%→17.2%（絕對降低 3.3%，95% CI 0.8–5.8）。
  淋巴結陽性（pN+，n=1,050）：10 年復發 63.7%→42.5%；15 年乳癌死亡 51.3%→42.8% [S3]
- 切緣共識（SSO–ASTRO，2014；系統性回顧 33 篇研究、28,162 名第 I/II 期侵犯性乳癌
  且接受全乳放療者）：切緣陽性（墨水碰到侵犯癌或原位癌）使同側乳房腫瘤復發風險增為兩倍；
  **切得更寬並不會再降低復發率**，故以「no ink on tumour（墨水未染到腫瘤）」為足夠切緣 [S4]
- 同一共識明確指出：這個兩倍風險**不會**因為腫瘤生物特性好、有內分泌治療或有放療 boost 而消失 [S4]
- 瑞典全國世代（2008–2017 手術，n=48,986，T1-2 N0-2 原發侵犯性乳癌，未分亞型呈現）：
  校正共病與社經地位後，全切未放療 vs 保留＋放療的全因死亡 HR 1.79（95% CI 1.66–1.92）、
  乳癌死亡 HR 1.66（1.45–1.90）；全切＋放療 vs 保留＋放療全因死亡 HR 1.24（1.13–1.37）。
  中位追蹤僅 6.28 年，**這是觀察性資料，不是隨機分派** [S5]
- 對側預防性乳房切除（CPM）使用率：SEER 1998–2012，496,488 名單側第 I–III 期侵犯性乳癌女性，
  CPM 比例由 2002 年 3.9% 上升到 2012 年 12.7%（P<0.001）；同期 CPM 病人接受重建的比例
  由 35.3% 升到 55.4% [S6]
- 同一資料：以保留手術＋放療為對照，CPM 未改善乳癌特異存活（HR 1.08，95% CI 1.01–1.16）
  或整體存活（HR 1.08，95% CI 1.03–1.14），**不因荷爾蒙受體狀態或年齡而異** [S6]
- SEER 2000–2019，661,270 名單側乳癌（第 0–III 期，含原位癌）女性，
  以 1:1:1 配對成三組各 36,028 人，追蹤 20 年：20 年對側乳癌風險在
  腫瘤切除／單側全切組為 6.9%（95% CI 6.1–7.9），雙側全切組僅 97 例（vs 766、728 例）；
  但 20 年乳癌死亡數為 3,077（8.54%，腫瘤切除）、3,269（9.07%，單側全切）、
  3,062（8.50%，雙側全切）——**對側乳癌幾乎被消滅，乳癌死亡率沒有差別** [S7]
- 同一研究解釋了為什麼：發生對側乳癌者，其後 15 年累積乳癌死亡率 32.1%，
  未發生者 14.5%（以對側乳癌為時間相依共變數，HR 4.00，95% CI 3.52–4.54）——
  對側乳癌**標記**了高風險體質，切掉第二個乳房並不能改變已經播散出去的風險 [S7]

**Claim ceiling**

Defensible：「在腫瘤大小與切緣條件符合的情況下，**保留手術加上全乳房放療**與乳房切除的
長期存活結果沒有差別；差別在同側乳房的局部復發率，保留組較高。近十年的大型世代研究
甚至顯示保留＋放療的存活比全切好，但那是觀察性資料，殘餘的選擇偏差無法排除。
對側預防性乳房切除可以大幅減少對側乳癌的發生，但在沒有已知遺傳性基因變異的人身上，
**沒有被證實能降低乳癌死亡率**。」

Would overstate：
- 「保留手術跟全切一樣，所以選保留就好」——漏掉放療這個必要條件，也漏掉切緣與腫瘤大小條件。
- 「保留手術的復發率跟全切一樣」——**不一樣**，同側乳房復發率明確較高（20 年 8.8% vs 2.3%）[S1]。
- 「新的研究證明保留比全切活得久」——瑞典研究是觀察性的，作者自己把它寫成
  「若兩者都是可行選項，不應把全切視為與保留等值」，不是因果宣稱 [S5]。
- 「切掉對側乳房比較安心也比較安全」——對側乳癌會少，乳癌死亡不會少 [S7]。
- 「切掉乳房就不用放療」——本篇不展開，但不可暗示；乳房切除後放療的適應症在 C3。

**Caveats / safety notes**

- **最容易造成不可逆錯誤決定的一句**：把「保留＋放療 ≈ 全切」讀成「保留＝不用放療」。
  NSABP B-06 的腫瘤切除未放療組 20 年同側復發率 39.2%，是加了放療那組的近三倍 [S2]。
  文章裡「保留」二字後面**每一次**都要跟著「加放療」。
- 這兩個奠基試驗都是 1970 年代收案，**當年沒有 HER2 標靶、沒有現代化療、沒有分子分型**，
  病人族群與今天不同。這一點要誠實寫出來，不要假裝它們是當代證據 [S1][S2]。
- CPM 的討論要同時給出兩個數字：對側乳癌**確實**變少（20 年 6.9% → 幾乎為零），
  乳癌死亡**確實**沒變（8.5% vs 8.54%）[S7]。只給其中一個都是誤導。
- SEER 沒有 BRCA 狀態資料，[S7] 的族群「絕大多數是非帶因者」是推論而非測量。
  帶因者的預防性手術決策**屬於 A6**，本篇一句話帶過並指過去。
- 不要把「沒有存活好處」寫成「不該做」。焦慮、影像追蹤困難、對稱性考量都是合理的理由；
  文章的任務是把「這件事買到什麼、沒買到什麼」講清楚，讓病人自己決定。
- 淋巴水腫、腋下手術範圍 → B2；放療分次 → C1；省略放療 → C2；重建時序 → C3。

**Taiwan status**

- 保留手術、乳房切除、術後全乳放療皆為健保給付之常規診療項目；**本 brief 未逐項核到
  個別手術與放療的支付標準條文**（支付標準壓縮檔下載被 Cloudflare 阻擋，見 [S41]），
  因此文中不得引用任何點數或項目代碼。寫成「這幾項是健保常規給付，細節請問個管師」即可。
- **對側預防性乳房切除（非帶因者）的健保給付狀態：查不到正式條文（gap）。**
  以 `nhi.gov.tw` 搜尋「預防性乳房切除／對側／BRCA 帶因者」未取得任何給付規定或支付標準文件 [S41]。
  文中一律寫成「這一項要跟你的個管師或醫院醫務課確認」，**不得宣稱有給付或沒給付**。

**Sources**

- **[S1] PASS** — Veronesi U, Cascinelli N, Mariani L, et al. (2002). *Twenty-year follow-up of a randomized study comparing breast-conserving surgery with radical mastectomy for early breast cancer*. N Engl J Med 347(16):1227-1232. PMID 12393819, doi 10.1056/nejmoa020989 — 象限切除＋放療 vs Halsted 根除術，20 年存活無差異、局部復發有差異。Route: Europe PMC REST (EXT_ID). https://europepmc.org/article/MED/12393819
- **[S2] PASS** — Fisher B, Anderson S, Bryant J, et al. (2002). *Twenty-year follow-up of a randomized trial comparing total mastectomy, lumpectomy, and lumpectomy plus irradiation for the treatment of invasive breast cancer*. N Engl J Med 347(16):1233-1241. PMID 12393820, doi 10.1056/nejmoa022152 — NSABP B-06 三臂，證明放療是保留手術等效性的前提。Route: Europe PMC REST (EXT_ID). https://europepmc.org/article/MED/12393820
- **[S3] PASS** — Early Breast Cancer Trialists' Collaborative Group (EBCTCG), Darby S, McGale P, et al. (2011). *Effect of radiotherapy after breast-conserving surgery on 10-year recurrence and 15-year breast cancer death: meta-analysis of individual patient data for 10,801 women in 17 randomised trials*. Lancet 378(9804):1707-1716. PMID 22019144, PMC3254252, doi 10.1016/s0140-6736(11)61629-2, Open Access — 保留手術後放療的絕對效益，含 pN0/pN+ 分層。Route: Europe PMC REST (EXT_ID). https://europepmc.org/article/MED/22019144
- **[S4] PASS** — Moran MS, Schnitt SJ, Giuliano AE, et al. (2014). *Society of Surgical Oncology-American Society for Radiation Oncology consensus guideline on margins for breast-conserving surgery with whole-breast irradiation in stages I and II invasive breast cancer*. J Clin Oncol 32(14):1507-1515. PMID 24516019, doi 10.1200/jco.2013.53.3935 — 「no ink on tumour」共識的原始文件。Route: Europe PMC REST (TITLE)。同一份共識另刊於 Ann Surg Oncol 21(3):704-716（PMID 24515565）與 Int J Radiat Oncol Biol Phys 88(3):553-564（PMID 24521674）。截至 2026-08-29，Europe PMC 查無 2023–2026 年之侵犯性乳癌切緣指引更新。https://europepmc.org/article/MED/24516019
- **[S5] PASS** — de Boniface J, Szulkin R, Johansson ALV. (2021). *Survival After Breast Conservation vs Mastectomy Adjusted for Comorbidity and Socioeconomic Status: A Swedish National 6-Year Follow-up of 48 986 Women*. JAMA Surg 156(7):628-637. PMID 33950173, PMC8100916, doi 10.1001/jamasurg.2021.1438, Open Access — 觀察性資料顯示保留＋放療存活較佳，作者自陳為關聯而非因果。Route: Europe PMC REST (TITLE). https://europepmc.org/article/MED/33950173
- **[S6] PASS** — Wong SM, Freedman RA, Sagara Y, et al. (2017). *Growing Use of Contralateral Prophylactic Mastectomy Despite no Improvement in Long-term Survival for Invasive Breast Cancer*. Ann Surg 265(3):581-589. PMID 28169929, doi 10.1097/sla.0000000000001698 — CPM 使用率趨勢與無存活益處。Route: Europe PMC REST (TITLE). https://europepmc.org/article/MED/28169929
- **[S7] PASS** — Giannakeas V, Lim DW, Narod SA. (2024). *Bilateral Mastectomy and Breast Cancer Mortality*. JAMA Oncol 10(9):1228-1236. PMID 39052262, PMC11273285, doi 10.1001/jamaoncol.2024.2212 — 66 萬人 SEER 配對世代，20 年對側乳癌大減但乳癌死亡不變。Route: Europe PMC REST (AUTH+TITLE). https://europepmc.org/article/MED/39052262
- **[S8] FAIL** — NCCN Clinical Practice Guidelines in Oncology: Breast Cancer 版本字串。目標頁 https://www.nccn.org/guidelines/guidelines-detail?category=1&id=1419 回傳 HTTP 403（登入牆＋機器人阻擋），**連版本號都無法確認**。全系列不得引用 NCCN 的任何內容或版本。

---

# B2 — 腋下要不要清乾淨

**Key facts**

- NSABP B-32（1999–2004 收案，n=5,611，臨床腋下淋巴結陰性之侵犯性乳癌，未分亞型）：
  前哨淋巴結陰性者（n=3,989）比較「前哨＋腋下淋巴結廓清」與「僅做前哨」，
  平均追蹤 95.6 個月，整體存活 HR 1.20（95% CI 0.96–1.50，p=0.12）；
  8 年整體存活 91.8% vs 90.3%，8 年無病存活 82.4% vs 81.5%（HR 1.05，0.90–1.22，p=0.54） [S9]
- 同一試驗的併發症資料（n=1,975 腋清組 vs 2,008 僅前哨組，均為前哨陰性）：
  36 個月時患側／對側手臂體積差 ≥10% 者，腋清組 14%、僅前哨組 8%；
  6 個月時麻木感 49% vs 15%、刺痛感 23% vs 10% [S10]
- ALMANAC（英國，n=1,031，臨床淋巴結陰性侵犯性乳癌）：12 個月時任何淋巴水腫的
  絕對發生率 5%（前哨組，n=515）vs 13%（標準腋下處置組，n=516），RR 0.37（95% CI 0.23–0.60）；
  感覺喪失 11% vs 31%，RR 0.37（0.27–0.50） [S18]
- ACOSOG Z0011（n=891，臨床 T1/T2、腋下無可觸及淋巴結、**1–2 顆前哨淋巴結有轉移**、
  全部接受腫瘤切除＋正切線全乳放療＋全身輔助治療；中位年齡 55 歲）：
  中位追蹤 9.3 年，10 年整體存活 86.3%（僅前哨）vs 83.6%（加腋清），
  HR 0.85（單側 95% CI 0–1.16），非劣性 P=0.02；10 年無病存活 80.2% vs 78.2%
  （HR 0.85，95% CI 0.62–1.17，P=0.32）。**第三照野放療是被禁止的** [S11]
- AMAROS（EORTC 10981-22023；4,806 人做前哨，其中 1,425 名前哨陽性者隨機分派：
  腋清 n=744 vs 腋下放療 n=681；cT1-2、臨床淋巴結陰性）：
  10 年腋下復發累積發生率 0.93%（95% CI 0.18–1.68，7 例，腋清）vs 1.82%（0.74–2.94，11 例，腋下放療），
  HR 1.71（95% CI 0.67–4.39）；整體存活 HR 1.17（0.89–1.52）、無病存活 HR 1.19（0.97–1.46），
  皆無差異 [S12]
- 同一試驗的淋巴水腫（5 年更新分析）：**腋清 24.5% vs 腋下放療 11.9%，P<0.001**。
  另一方面，10 年第二原發癌累積發生率為腋下放療 12.1%（95% CI 9.6–14.9）
  vs 腋清 8.3%（6.3–10.7）——好處與代價各在一邊 [S12]
- SINODAR-ONE（義大利，2015–2020，n=889，T1-2 且 **1–2 顆巨轉移前哨淋巴結**，
  保留手術或全乳切除皆可）：中位追蹤 34 個月，5 年整體存活 98.9%（腋清）vs 98.8%（僅前哨），
  p=0.936；5 年累積復發 6.9% vs 3.3%，p=0.444；兩組各僅 1 例腋下復發 [S13]
- SOUND（義大利／瑞士／西班牙／智利，n=1,405 意向分析；腫瘤 ≤2 cm 且**術前腋下超音波陰性**；
  中位年齡 60 歲，87.8% 為 ER 陽性／HER2 陰性）：前哨切片組 708 人中 97 人（13.7%）淋巴結陽性；
  中位追蹤 5.7 年，5 年無遠端疾病存活 97.7%（前哨組）vs 98.0%（完全不做腋下手術組），
  HR 0.84（90% CI 0.45–1.54），非劣性 P=0.02 [S14]
- INSEMA 主要結果（德國等，n=5,502 隨機分派，per-protocol 4,858；臨床淋巴結陰性、
  T1/T2 ≤5 cm、**接受保留手術者**；90% 為臨床 T1、79% 為病理 T1）：
  中位追蹤 73.6 個月，5 年無侵犯疾病存活 91.9%（不做腋下手術，n=962）
  vs 91.7%（做前哨，n=3,896），HR 0.91（95% CI 0.73–1.14），低於非劣性上限 1.271。
  腋下復發 1.0% vs 0.3%；死亡 1.4% vs 2.4%。不做腋下手術者淋巴水腫較少、肩臂活動較好 [S15]
- **INSEMA 第二次隨機分派（n=485 收案、per-protocol 386；cN0、T1/T2、**1–3 顆前哨淋巴結
  巨轉移**、先手術之保留手術病人）：中位追蹤 74.2 個月，5 年無侵犯疾病存活
  86.6%（95% CI 81.0–90.7，僅前哨，n=217）vs 93.8%（88.7–96.6，加腋清，n=169），
  HR 1.69（95% CI 0.98–2.94），P=0.058；5 年整體存活 94.9% vs 96.2%（P=0.663）；
  5 年局部區域復發 1.1% vs 0%（P=0.405）。作者結論是「未觀察到顯著差異」，
  但**點估計方向不利於省略腋清，且樣本數遠不足以下結論** [S16]
- 淋巴水腫發生率的統合分析（72 篇研究）：整體合併發生率 16.6%（95% CI 13.6–20.2）；
  僅取前瞻性世代研究（30 篇）為 21.4%（14.9–29.8）；
  **腋下淋巴結廓清者 19.9%（13.5–28.2，18 篇）vs 前哨切片者 5.6%（6.1–7.9，18 篇）**。
  證據等級最強的風險因子為手術範圍大（腋清、摘除淋巴結數多、乳房切除）與過重／肥胖 [S17]
- 指引現況：Ontario Health（Cancer Care Ontario）與 ASCO 2021 共同指引仍是英語系
  「腋下處置」的主要參考文件，涵蓋誰需要腋下分期、前哨陰性者是否需進一步處置、
  前哨陽性者的策略、以及**術前化療情境下的腋下處置與時機** [S19]
- 2025 St Gallen 共識把「在許多低風險、ER 陽性的病人身上避免前哨淋巴結手術」
  列為當年的重要更新之一 [S27]

**Claim ceiling**

Defensible：「前哨淋巴結陰性時，不需要再做腋下淋巴結廓清，存活與局部控制相同而手臂
併發症明顯較少。前哨有 1–2 顆轉移、又接受保留手術加全乳放療的病人，多數不需要腋清。
腫瘤小、術前腋下超音波陰性、且不做腋下手術不會改變後續全身治療決定的人，甚至可以
完全不做腋下手術。**但腋下處置仍有明確需要廓清的情境，這是外科與腫瘤團隊逐案判斷的事。**」

Would overstate：
- 「現在都不用清腋下了」——SOUND 與 INSEMA 的族群非常窄（腫瘤小、超音波陰性、
  多為 ER 陽性 HER2 陰性、接受保留手術者），把結論外推到全部病人是錯的 [S14][S15]。
- 「前哨有轉移也不用清」——INSEMA 第二次隨機分派的 5 年 iDFS 差了 7.2 個百分點
  且 HR 1.69，方向不利；SINODAR-ONE 追蹤僅 34 個月 [S16][S13]。
- 「不清腋下就不會淋巴水腫」——前哨切片仍有 5.6% 的淋巴水腫發生率 [S17]，
  NSABP B-32 的僅前哨組 36 個月時仍有 8% 手臂體積差 ≥10% [S10]（固定紅線 C）。
- 「腋下放療可以完全取代腋清」——AMAROS 顯示腋下控制與存活相當、淋巴水腫較少，
  但第二原發癌 10 年累積發生率較高（12.1% vs 8.3%），要一起講 [S12]。
- Z0011 的結論不可脫離它的前提：**保留手術＋正切線全乳放療＋全身輔助治療、禁止第三照野** [S11]。

**Caveats / safety notes**

- 這篇最容易被讀成「我可以要求醫師不要清腋下」。要明確寫出：省略腋清的試驗族群條件
  （腫瘤大小、臨床與超音波腋下狀態、手術方式、有沒有做放療、是不是先手術）
  幾乎每一項都會改變答案。
- **術前化療後才發現淋巴結有殘餘轉移**的情境，不在 Z0011／SOUND／INSEMA 的族群裡；
  這一類仍以腋清為標準處置 [S19]。B3 會談術前治療，兩篇要互相指路。
- 淋巴水腫的完整內容 → **D2**；本篇只用一句話帶過「手術與放療都是風險因子」並指過去。
- 「哪些人要照區域淋巴、乳房切除後要不要放療」→ **C3**，本篇不寫。
- INSEMA 第二次隨機分派是 2026 年才刊出的次要結果，寫的時候要標明它是
  **未達統計顯著、但點估計不利、且明顯檢定力不足**——不可寫成「證明可以省略」，
  也不可寫成「證明不能省略」。

**Taiwan status**

- 前哨淋巴結切片與腋下淋巴結廓清均為健保給付之常規手術項目；
  **本 brief 未核到具體支付標準條文**（下載受阻，見 [S41]），文中不得寫出點數或項目代碼，
  一律寫成「請跟個管師或醫院醫務課確認」。
- 前哨淋巴結定位所用的染劑／同位素／磁性追蹤劑之給付與自費狀態：**查不到正式條文（gap）**。

**Sources**

- **[S9] PASS** — Krag DN, Anderson SJ, Julian TB, et al. (2010). *Sentinel-lymph-node resection compared with conventional axillary-lymph-node dissection in clinically node-negative patients with breast cancer: overall survival findings from the NSABP B-32 randomised phase 3 trial*. Lancet Oncol 11(10):927-933. PMID 20863759, PMC3041644, doi 10.1016/s1470-2045(10)70207-2 — 前哨陰性者省略腋清的存活等效性。Route: Europe PMC REST (TITLE). https://europepmc.org/article/MED/20863759
- **[S10] PASS** — Ashikaga T, Krag DN, Land SR, et al. (2010). *Morbidity results from the NSABP B-32 trial comparing sentinel lymph node dissection versus axillary dissection*. J Surg Oncol 102(2):111-118. PMID 20648579, PMC3072246, doi 10.1002/jso.21535 — B-32 的手臂體積、肩關節活動與感覺異常，附分母。Route: Europe PMC REST (AUTH+TITLE). https://europepmc.org/article/MED/20648579
- **[S11] PASS** — Giuliano AE, Ballman KV, McCall L, et al. (2017). *Effect of Axillary Dissection vs No Axillary Dissection on 10-Year Overall Survival Among Women With Invasive Breast Cancer and Sentinel Node Metastasis: The ACOSOG Z0011 (Alliance) Randomized Clinical Trial*. JAMA 318(10):918-926. PMID 28898379, PMC5672806, doi 10.1001/jama.2017.11470 — Z0011 十年結果與其嚴格前提。Route: Europe PMC REST (TITLE). https://europepmc.org/article/MED/28898379
- **[S12] PASS** — Bartels SAL, Donker M, Poncet C, et al. (2023). *Radiotherapy or Surgery of the Axilla After a Positive Sentinel Node in Breast Cancer: 10-Year Results of the Randomized Controlled EORTC 10981-22023 AMAROS Trial*. J Clin Oncol 41(12):2159-2165. PMID 36383926, doi 10.1200/jco.22.01565 — 腋下放療 vs 腋清十年結果，含淋巴水腫 24.5% vs 11.9% 與第二原發癌。Route: Europe PMC REST (TITLE). https://europepmc.org/article/MED/36383926
- **[S13] PASS** — Tinterri C, Gentile D, Gatzemeier W, et al. (2022). *Preservation of Axillary Lymph Nodes Compared with Complete Dissection in T1-2 Breast Cancer Patients Presenting One or Two Metastatic Sentinel Lymph Nodes: The SINODAR-ONE Multicenter Randomized Clinical Trial*. Ann Surg Oncol 29(9):5732-5744. PMID 35552930, doi 10.1245/s10434-022-11866-w — 中位追蹤僅 34 個月，須標明。Route: Europe PMC REST (TITLE). https://europepmc.org/article/MED/35552930
- **[S14] PASS** — Gentilini OD, Botteri E, Sangalli C, et al. (2023). *Sentinel Lymph Node Biopsy vs No Axillary Surgery in Patients With Small Breast Cancer and Negative Results on Ultrasonography of Axillary Lymph Nodes: The SOUND Randomized Clinical Trial*. JAMA Oncol 9(11):1557-1564. PMID 37733364, PMC10514873, doi 10.1001/jamaoncol.2023.3759, Open Access — 完全省略腋下手術的非劣性試驗。Route: Europe PMC REST (TITLE). https://europepmc.org/article/MED/37733364
- **[S15] PASS** — Reimer T, Stachs A, Veselinovic K, et al. (2025). *Axillary Surgery in Breast Cancer — Primary Results of the INSEMA Trial*. N Engl J Med 392(11):1051-1064. PMID 39665649, doi 10.1056/nejmoa2412063 — 保留手術族群省略腋下分期的非劣性。Route: Europe PMC REST (TITLE). https://europepmc.org/article/MED/39665649
- **[S16] PASS** — Reimer T, Stachs A, Veselinovic K, et al. (2026). *Axillary surgery in patients with sentinel node macrometastases: secondary results of the randomized INSEMA trial*. NPJ Breast Cancer 12(1):19. PMID 41593108, PMC12855813, doi 10.1038/s41523-026-00902-7, Open Access — 前哨巨轉移者省略腋清的次要結果，5 年 iDFS 86.6% vs 93.8%，HR 1.69。Route: Europe PMC REST (TITLE). https://europepmc.org/article/MED/41593108
- **[S17] PASS** — DiSipio T, Rye S, Newman B, Hayes S. (2013). *Incidence of unilateral arm lymphoedema after breast cancer: a systematic review and meta-analysis*. Lancet Oncol 14(6):500-515. PMID 23540561, doi 10.1016/s1470-2045(13)70076-7 — 腋清 19.9% vs 前哨 5.6%。Route: Europe PMC REST (TITLE). https://europepmc.org/article/MED/23540561
- **[S18] PASS** — Mansel RE, Fallowfield L, Kissin M, et al. (2006). *Randomized multicenter trial of sentinel node biopsy versus standard axillary treatment in operable breast cancer: the ALMANAC Trial*. J Natl Cancer Inst 98(9):599-609. PMID 16670385, doi 10.1093/jnci/djj158 — 隨機試驗中的淋巴水腫 5% vs 13%。Route: Europe PMC REST (TITLE). https://europepmc.org/article/MED/16670385
- **[S19] PASS** — Brackstone M, Baldassarre FG, Perera FE, et al. (2021). *Management of the Axilla in Early-Stage Breast Cancer: Ontario Health (Cancer Care Ontario) and ASCO Guideline*. J Clin Oncol 39(27):3056-3082. PMID 34279999, doi 10.1200/jco.21.00934 — 腋下處置指引，含術前化療後的腋下策略。Route: Europe PMC REST (TITLE). https://europepmc.org/article/MED/34279999

---

# B3 — 先開刀，還是先做化療

**Key facts**

- NSABP B-18（n=1,493 可分析；可手術乳癌，未分子分型）：術前 AC 四療程 vs 術後 AC 四療程，
  無病存活與整體存活**無統計顯著差異**；<50 歲次群組有偏向術前的趨勢
  （無病存活 HR 0.85，P=0.09；整體存活 HR 0.81，P=0.06） [S21]
- NSABP B-27（n=2,344）：術前 AC 之後再加 docetaxel，病理完全緩解率由 13% 提高到 26%
  （P<0.0001），但**無病存活與整體存活沒有因此改善**。兩個試驗中達到 pCR 的病人，
  其無病存活與整體存活都顯著較佳 [S21]
- EBCTCG 統合分析（10 個隨機試驗、4,756 名女性，1983–2002 收案，81% 用 anthracycline 為主）：
  術前化療組接受保留手術的比例 65%（1,504/2,320）vs 術後化療組 49%（1,135/2,318）；
  1,947 名接受術前化療者中 69%（1,349 人）有完全或部分臨床反應 [S22]
- 同一統合分析（中位追蹤 9 年）：**15 年局部復發率術前化療 21.4% vs 術後化療 15.9%**
  （絕對增加 5.5%，95% CI 2.4–8.6；rate ratio 1.37，95% CI 1.17–1.61，p=0.0001）；
  遠端復發 38.2% vs 38.0%（RR 1.02，0.92–1.14，p=0.66）、乳癌死亡 34.4% vs 33.7%
  （RR 1.06，0.95–1.18，p=0.31）、全因死亡 40.9% vs 41.2%（RR 1.04，0.94–1.15，p=0.45） [S22]
- CTNeoBC 合併分析（12 個國際試驗、11,955 名病人）：達到 pCR（定義為 ypT0/is ypN0）者
  無事件存活 HR 0.48（95% CI 0.43–0.54）、整體存活 HR 0.36（0.31–0.42）。
  乳房與淋巴結都清空（ypT0 ypN0 或 ypT0/is ypN0）的關聯性優於僅乳房清空（ypT0/is，EFS HR 0.60） [S20]
- 同一分析的**亞型差異**：pCR 與長期預後的關聯在三陰性乳癌最強（EFS HR 0.24，95% CI 0.18–0.33；
  OS HR 0.16，0.11–0.25）與 HER2 陽性／荷爾蒙受體陰性且接受 trastuzumab 者最強
  （EFS HR 0.15，0.09–0.27；OS HR 0.08，0.03–0.22） [S20]
- **同一分析的試驗層級分析：pCR 率的提升與 EFS 改善的相關性極弱（R²=0.03，95% CI 0.00–0.25），
  與 OS 的相關性 R²=0.24（0.00–0.70）——作者明白寫出「本合併分析無法驗證 pCR 為
  EFS 或 OS 的替代終點」** [S20]
- 獨立驗證（54 個隨機試驗、32,611 名早期乳癌病人）：log(pCR 相對風險) 與 log(HR) 的
  試驗層級相關性，無病存活 R²=0.14（95% CI 0.00–0.29）、整體存活 R²=0.08（0.00–0.22）；
  在各亞群（含 HER2 陽性、三陰性）與各種 pCR 定義下結果一致。
  作者結論：pCR **不應**作為法規用途之術前治療試驗的主要終點 [S23]
- KATHERINE（n=1,486，HER2 陽性早期乳癌、含 taxane 與 trastuzumab 之術前治療後
  乳房或腋下仍有殘餘侵犯性病灶）：術後 T-DM1 14 個療程 vs trastuzumab，
  3 年無侵犯疾病存活 88.3% vs 77.0%，HR 0.50（95% CI 0.39–0.64，P<0.001） [S24]
- KATHERINE 最終分析（中位追蹤 8.4 年）：7 年無侵犯疾病存活 80.8%（T-DM1）vs 67.1%
  （trastuzumab），差 13.7 個百分點，HR 0.54（95% CI 0.44–0.66）；
  7 年整體存活 89.1% vs 84.4%（差 4.7 個百分點），死亡 HR 0.66（95% CI 0.51–0.87，P=0.003）；
  ≥3 級不良事件 26.1% vs 15.7% [S25]
- CREATE-X（日本／韓國，n=910，**HER2 陰性**、術前化療（含 anthracycline／taxane）
  後仍有殘餘侵犯性病灶）：術後加 capecitabine vs 不加，
  5 年無病存活 74.1% vs 67.6%（HR 0.70，95% CI 0.53–0.92，P=0.01）；
  5 年整體存活 89.2% vs 83.6%（HR 0.59，95% CI 0.39–0.90，P=0.01） [S26]
- CREATE-X 的**三陰性次群組**：5 年無病存活 69.8% vs 56.1%（HR 0.58，95% CI 0.39–0.87）；
  5 年整體存活 78.8% vs 70.3%（HR 0.52，0.30–0.90）。手足症候群發生率 73.4% [S26]

**Claim ceiling**

Defensible：「把同樣的化療放在手術前或手術後，遠端復發、乳癌死亡與整體存活沒有差別；
術前做的好處是腫瘤縮小後比較有機會保留乳房，而且可以直接看到腫瘤對藥物的反應。
代價是保留手術後的局部復發率略高（15 年 21.4% vs 15.9%）。
**手術後有沒有殘餘病灶，會改變接下來的治療**——HER2 陽性有殘餘病灶者換成 T-DM1，
HER2 陰性（尤其三陰性）有殘餘病灶者加 capecitabine，都有隨機試驗支持。」

Would overstate：
- 「先化療效果比較好」——存活沒有比較好 [S21][S22]。
- 「化療反應好就可以從全切改成局部切除」——本 brief **不支持**這種寫法（固定紅線 C）。
  可以說「有機會把原本需要全切的腫瘤縮到可以保留」，但必須同時寫出局部復發率上升 [S22]，
  且是否可行由外科團隊逐案判斷。
- 「達到 pCR 就等於治好了」——pCR 是**個人層級的預後標記**，不是治癒保證；
  而且在**試驗層級**，把 pCR 率拉高並不可靠地轉換成存活改善（R²=0.03–0.24）[S20][S23]。
- 「沒有達到 pCR 就沒救了」——KATHERINE 與 CREATE-X 正是為這群人設計的，
  而且效果是實質的（7 年 OS 89.1% vs 84.4%）[S25][S26]。
- 「capecitabine 對每一種乳癌的殘餘病灶都有效」——CREATE-X 只收 **HER2 陰性**，
  效益最明確的是三陰性 [S26]。

**Caveats / safety notes**

- 這篇的高風險讀法是「先化療＝可以不用開刀」與「pCR＝不用再治療」。兩個都要正面否定。
- **亞型標示是這篇的命門**：pCR 的意義在三陰性與 HER2 陽性／HR 陰性最大，
  在 HR 陽性／HER2 陰性小很多；同一句「達到 pCR 的人預後比較好」在三種亞型之間
  意義差距數倍 [S20]。任何 pCR 數字都必須帶亞型。
- CREATE-X 是東亞族群試驗（日本、韓國），這對台灣讀者是加分，但 73.4% 的手足症候群
  也必須寫出來——好處與代價同一段。
- 提到 anthracycline、taxane、cyclophosphamide、capecitabine、trastuzumab、T-DM1
  就觸發**固定紅線 A**：本篇只留一兩條與自己藥物相關的當天聯絡警語（發熱性嗜中性球低下、
  T-DM1 相關的心臟功能下降與肝功能異常、capecitabine 的手足症候群破皮與嚴重腹瀉），
  完整清單指向 **C4**。
- 生育保存必須在第一次化療之前 → 一句話帶過並指向 **C6**（固定紅線 B）。
- 術前 MRI 的爭議 → **A5**，本篇不重複。
- 腋下處置在術前治療情境的差異 → **B2**（並見 [S19]）。
- HER2 藥物本身的排列 → **B5**；本篇只寫「殘餘病灶要換藥」這個決策點。

**Taiwan status**

- T-DM1 用於早期乳癌殘餘病灶：**有健保給付，條件明確**（藥品給付規定 9.87.1）。
  必須是 HER2 過度表現（IHC 3+ 或 FISH+）、術前已接受至少 6 個療程（每 3 週一療程、
  至少 16 週）化療（其中至少 3 個療程／9 週的 taxane）與至少 3 個療程（9 週）trastuzumab
  之術前輔助治療後**仍有殘餘病灶**，且需符合下列之一：
  (I) 有腋下淋巴結轉移但無遠處臟器轉移；(II) 無腋下淋巴結轉移，但 **ER 陰性且腫瘤 >2 公分**。
  須事前審查，每 24 週檢附療效評估再申請，**每人上限 14 個療程**；
  且與 trastuzumab 在手術前後合計以 18 個療程為上限 [S51]
- T-DM1 的排除條件（同條文）：未於**術後 12 週內**開始治療或提出申請、
  左心室射出分率 <45% 或有症狀心衰竭、不得與其他抗 HER2 藥物併用 [S51]。
  「術後 12 週內」是一個時效性條件，值得在文中點出。
- 術後輔助 capecitabine 用於 HER2 陰性殘餘病灶（CREATE-X 適應症）之健保給付狀態：
  **本 brief 未在第 9 節查到對應之獨立條文（gap）**，請寫成「要跟個管師或醫院醫務課確認」。

**Sources**

- **[S20] PASS** — Cortazar P, Zhang L, Untch M, et al. (2014). *Pathological complete response and long-term clinical benefit in breast cancer: the CTNeoBC pooled analysis*. Lancet 384(9938):164-172. PMID 24529560, doi 10.1016/s0140-6736(13)62422-8 — pCR 的個人層級預後價值與試驗層級替代終點失敗（R²=0.03）。Route: Europe PMC REST (TITLE). https://europepmc.org/article/MED/24529560
- **[S21] PASS** — Rastogi P, Anderson SJ, Bear HD, et al. (2008). *Preoperative chemotherapy: updates of National Surgical Adjuvant Breast and Bowel Project Protocols B-18 and B-27*. J Clin Oncol 26(5):778-785. PMID 18258986, doi 10.1200/jco.2007.15.0235 — 術前 vs 術後化療的長期等效性。Route: Europe PMC REST (AUTH+TITLE). https://europepmc.org/article/MED/18258986
- **[S22] PASS** — Early Breast Cancer Trialists' Collaborative Group (EBCTCG). (2018). *Long-term outcomes for neoadjuvant versus adjuvant chemotherapy in early breast cancer: meta-analysis of individual patient data from ten randomised trials*. Lancet Oncol 19(1):27-39. PMID 29242041, PMC5757427, doi 10.1016/s1470-2045(17)30777-5, Open Access — 保留手術率上升、局部復發率上升、存活無差異。Route: Europe PMC REST (TITLE). https://europepmc.org/article/MED/29242041
- **[S23] PASS** — Conforti F, Pala L, Sala I, et al. (2021). *Evaluation of pathological complete response as surrogate endpoint in neoadjuvant randomised clinical trials of early stage breast cancer: systematic review and meta-analysis*. BMJ 375:e066381. PMID 34933868, PMC8689398, doi 10.1136/bmj-2021-066381, Open Access — 54 試驗、32,611 人，pCR 試驗層級替代性不成立。Route: Europe PMC REST (AUTH+TITLE). https://europepmc.org/article/MED/34933868
- **[S24] PASS** — von Minckwitz G, Huang CS, Mano MS, et al. (2019). *Trastuzumab Emtansine for Residual Invasive HER2-Positive Breast Cancer*. N Engl J Med 380(7):617-628. PMID 30516102, doi 10.1056/nejmoa1814017 — KATHERINE 主要分析。Route: Europe PMC REST (TITLE). https://europepmc.org/article/MED/30516102
- **[S25] PASS** — Geyer CE, Untch M, Huang CS, et al. (2025). *Survival with Trastuzumab Emtansine in Residual HER2-Positive Breast Cancer*. N Engl J Med 392(3):249-257. PMID 39813643, doi 10.1056/nejmoa2406070 — KATHERINE 8.4 年追蹤，整體存活顯著改善。Route: Europe PMC REST (TITLE). https://europepmc.org/article/MED/39813643
- **[S26] PASS** — Masuda N, Lee SJ, Ohtani S, et al. (2017). *Adjuvant Capecitabine for Breast Cancer after Preoperative Chemotherapy*. N Engl J Med 376(22):2147-2159. PMID 28564564, doi 10.1056/nejmoa1612645 — CREATE-X，HER2 陰性殘餘病灶，含三陰性次群組與手足症候群 73.4%。Route: Europe PMC REST (TITLE). https://europepmc.org/article/MED/28564564
- **[S27] PASS** — Burstein HJ, Curigliano G, Gnant M, et al. (2025). *Tailoring treatment to cancer risk and patient preference: the 2025 St Gallen International Breast Cancer Consensus Statement on individualizing therapy for patients with early breast cancer*. Ann Oncol 36(12):1433-1446. PMID 41072918, doi 10.1016/j.annonc.2025.09.007 — 現行最新一版 St Gallen 早期乳癌共識（2025）。Route: Europe PMC REST (TITLE). https://europepmc.org/article/MED/41072918
- **[S28] PASS（書目已核，內容未取得）** — Loibl S, André F, Bachelot T, et al. (2024). *Early breast cancer: ESMO Clinical Practice Guideline for diagnosis, treatment and follow-up*. Ann Oncol 35(2):159-182. PMID 38101773, doi 10.1016/j.annonc.2023.11.016 — 截至 2026-08-29，Europe PMC 查無更新版之 ESMO 早期乳癌指引（2026 年更新的是**轉移性**指引，Ann Oncol 37(9):1203-1219，PMID 42217581）。**ESMO 官方著陸頁 https://www.esmo.org/guidelines/esmo-clinical-practice-guideline-early-breast-cancer 為 JS 動態載入，抓不到內容，Europe PMC 亦無摘要**；因此本文只能引用「這是現行版本」，**不得引用其中任何具體建議文字或數字**。Route: Europe PMC REST (AUTH+TITLE). https://europepmc.org/article/MED/38101773

---

# B4 — 這份檢測是要證明你可以不做化療 【紅線 1｜全系列風險最高】

> **開頭必須有的一句**（見 SPEC 第六節）：這一篇談的是三條基因檢測線裡的**第一條**——
> 從腫瘤看化療加下去有沒有好處，結論常常是「不用做」。三條線的分別在 **A4**；
> 遺傳性 BRCA 在 **A6**；轉移後找藥在 **D5**。

**Key facts — 適用範圍（這是本篇最重要的一組事實）**

- ASCO 2022 生物標記指引（現行版；2026-08-29 於 Europe PMC 未查到更新版）明文：
  **這些檢測沒有一項被建議用於 HER2 陽性或三陰性乳癌的治療決策** [S37]
- 同一指引的適用界線：Oncotype DX、MammaPrint、Breast Cancer Index、EndoPredict
  可用於**停經後或 >50 歲**、早期 ER 陽性／HER2 陰性、淋巴結陰性或 1–3 顆陽性者；
  Prosigna 與 BCI 用於停經後、淋巴結陰性者；
  **停經前病人只有 Oncotype DX 可用於淋巴結陰性者**；
  現有資料顯示**停經前、1–3 顆淋巴結陽性者不論分數為何都能從化療得到好處**；
  **≥4 顆淋巴結陽性者沒有任何以基因檢測指導化療的資料** [S37]
- 台大醫院的自費同意書（2024 年 7 月版）所列 Oncotype DX 適應症與此一致：
  ER 或 PR 陽性、HER2 陰性、淋巴結陰性或陽性之新診斷早期浸潤性乳癌 [S40]

**Key facts — 21 基因復發分數（Oncotype DX）：TAILORx**

- TAILORx 收案 10,273 名 **荷爾蒙受體陽性、HER2 陰性、腋下淋巴結陰性**女性；
  分數區間 0–100，分成 **0–10（低）、11–25（中）、26–100（高）** 三帶 [S29][S30]
- 分數 0–10（1,626 人，占 15.9%）僅接受內分泌治療：5 年無侵犯疾病存活 93.8%
  （95% CI 92.4–94.9）、5 年無遠端復發 99.3%（98.7–99.6）、5 年整體存活 98.0%（97.1–98.6） [S29]
- 分數 11–25（6,711 人，占符合追蹤條件者的 69%）隨機分派：單用內分泌治療對
  化療＋內分泌治療為非劣性，無侵犯疾病存活 HR 1.08（95% CI 0.94–1.24，P=0.26）。
  9 年時：無侵犯疾病存活 83.3%（內分泌）vs 84.3%（化療＋內分泌）；
  無遠端復發 94.5% vs 95.0%；整體存活 93.9% vs 93.8% [S30]
- **年齡交互作用（紅線 1 的核心）**：化療對無侵犯疾病存活的效益隨「復發分數×年齡」而變化
  （交互作用 P=0.004）；**≤50 歲、分數 16–25 的女性可看到化療的效益** [S30]
- 加入臨床風險（以腫瘤大小與分級定義）後（n=9,427）：
  在 **≤50 歲、僅接受內分泌治療**者，9 年遠端復發率為
  分數 0–10 者 ≤1.8±0.9%（不論臨床風險）；
  分數 11–25 且臨床低風險者 4.7±1.0%；
  **分數 11–25 且臨床高風險者 12.3±2.4%**；
  分數 26–100（全部接受化療＋內分泌）者 15.2±3.3% [S31]
- 臨床風險本身在中分數帶仍具預後價值：內分泌治療組高 vs 低臨床風險的遠端復發
  HR 2.73（95% CI 1.93–3.87）；化療＋內分泌組 HR 2.41（1.66–3.48） [S31]

**Key facts — 淋巴結 1–3 顆陽性：RxPONDER**

- RxPONDER 收案 5,083 名 **荷爾蒙受體陽性、HER2 陰性、1–3 顆腋下淋巴結陽性、
  復發分數 ≤25** 的女性（33.2% 停經前、66.8% 停經後） [S32]
- **化療效益隨停經狀態而異**（交互作用 P=0.008），因此分開分析：
  **停經後**女性 5 年無侵犯疾病存活 91.9%（僅內分泌）vs 91.3%（化療＋內分泌），
  HR 1.02（95% CI 0.82–1.26，P=0.89）——**沒有化療效益**；
  **停經前**女性 89.0% vs 93.9%，HR 0.60（95% CI 0.43–0.83，P=0.002），
  無遠端復發存活 HR 0.58（0.39–0.87，P=0.009) [S32]
- **關鍵反直覺點**：在停經前族群，**相對化療效益並不隨復發分數升高而增加** [S32]
- 2026 年的生物標記次分析（1,556 名 <55 歲之受試者，測治療前血清）：
  抗穆勒氏管荷爾蒙（AMH）與化療效益有顯著交互作用（校正後 P=0.0034）。
  AMH ≥10 pg/mL（卵巢儲備正常，占 64%）者化療＋內分泌優於單用內分泌
  （無侵犯疾病存活 HR 0.46，95% CI 0.33–0.65，校正後 P=0.00012）；
  AMH <10 pg/mL（占 36%）者**沒有化療效益**（HR 1.27，95% CI 0.81–1.99，校正後 P=0.47）。
  作者明白寫出：**AMH 比停經狀態、年齡或其他荷爾蒙更能指出誰會從化療得到好處**，
  且 RxPONDER 的停經前受試者**大多沒有接受卵巢功能抑制** [S33]

**Key facts — 70 基因訊號（MammaPrint）：MINDACT**

- MINDACT 收案 6,693 名早期乳癌女性（T1/T2 或可手術 T3、**最多 3 顆淋巴結陽性**、
  年齡 18–70 歲）；同時評估臨床風險（改良版 Adjuvant! Online）與基因風險（70 基因） [S34][S35]
- 主要族群「**臨床高風險、基因低風險**」（1,550 人，占 23.2%）：不做化療者
  5 年無遠端轉移存活 94.7%（95% CI 92.5–96.2），高於預設非劣性下界 92%；
  與做化療者的絕對差為 1.5 個百分點（不做化療較低） [S34]
- 更新分析（中位追蹤 8.7 年，2020 年 2 月資料）：主要檢定族群（n=644）5 年無遠端轉移存活
  95.1%（95% CI 93.1–96.6）；意向治療族群（化療 n=749 vs 不化療 n=748）
  8 年無遠端轉移存活 92.0%（89.6–93.8）vs 89.4%（86.8–91.5），HR 0.66（95% CI 0.48–0.92） [S35]
- **同樣的年齡分歧**（探索性、檢定力不足）：在 HR 陽性／HER2 陰性次群組（1,358 人）中，
  **≤50 歲**者（n=464）8 年無遠端轉移存活 93.6%（化療）vs 88.6%（不化療），
  絕對差 5.0 個百分點（SE 2.8，95% CI −0.5 至 10.4）；
  **>50 歲**者（n=894）90.2% vs 90.0%，絕對差 0.2 個百分點（SE 2.1，−4.0 至 4.4）。
  作者自己寫「這可能來自化療造成的卵巢功能抑制」 [S35]
- 依淋巴結分層（同族群）：淋巴結陰性者（n=699）8 年無遠端轉移存活差 2.5 個百分點
  （SE 2.3，−2.1 至 7.2）；1–3 顆陽性者（n=658）差 1.3 個百分點（SE 2.4，−3.5 至 6.1）——
  **效益並不因淋巴結陽性而變大** [S35]

**Key facts — 不同平台的分數不能互換**

- OPTIMA prelim（英國，313 名早期乳癌女性，**同一批腫瘤同時做五種檢測**）：
  被判為低／中風險的比例，Oncotype DX 82.1%（95% CI 77.8–86.4）、Prosigna 65.5%（60.1–70.9）、
  IHC4 72.0%（66.5–77.5）、MammaPrint 61.4%（55.9–66.9）、NexCourse Breast 61.6%（55.8–67.4） [S36]
- 同一批腫瘤：**只有 119 顆（39.4%）被五種檢測一致歸為低／中風險或一致歸為高風險；
  183 顆（60.6%）被不同檢測歸到不同風險類別**。三種可做分子亞型分類的檢測中，
  只有 121 顆（40.1%）被三者一致判為 luminal A，123 顆（40.7%）分型不一致 [S36]
- 作者結論：這些檢測在**族群層級**提供大致等值的預後資訊，但**對個別病人可能給出
  不同的風險分類與不同的亞型** [S36]

**Key facts — 分數低不等於零風險**

- EBCTCG（88 個試驗、62,923 名 ER 陽性、完成 5 年內分泌治療且 5 年時無病之女性）：
  **從第 5 年到第 20 年，復發是以穩定的速率持續發生的**。遠端復發風險與原始 T/N 狀態
  密切相關：T1N0 13%、T1N1-3 20%、T1N4-9 34%、T2N0 19%、T2N1-3 26%、T2N4-9 41% [S38]
- 即使是最低風險的 T1N0：第 5–20 年遠端復發風險為低分化 10%、中分化 13%、高分化 17% [S38]
- TAILORx 分數 11–25、僅接受內分泌治療者，9 年無侵犯疾病存活 83.3%——
  換句話說**約六分之一在 9 年內發生了事件** [S30]

**Claim ceiling**

Defensible：「這一類多基因檢測的用途，是在**荷爾蒙受體陽性、HER2 陰性**、
且符合試驗淋巴結與期別條件的病人身上，找出化療加上去也帶不來額外好處的人。
它的答案取決於**你的年齡與停經狀態**：同一個中間分數，在停經後可能代表化療沒有用，
在停經前（或卵巢功能仍正常）可能代表化療有用。分數低代表復發機率低，**不代表零**。
不同平台的分數不能互相換算。這是一個要帶著病理報告去門診談的決定。」

Would overstate / **本篇一律不准出現**：
- **任何一般性建議**——不准寫「分數低就可以不做化療」，也不准寫「還是做化療比較保險」。
  這篇的結論只能是「這是一個要一起談的決定，而且你有權要求對方說出他看的是哪幾項」。
- 「做了基因檢測就可以不用化療」——這是紅線 1 的失敗定義。
- 「分數低就不會復發」——T1N0 在第 5–20 年仍有 10–17% 的遠端復發風險 [S38]；
  TAILORx 中分數帶單用內分泌者 9 年有約 17% 發生事件 [S30]（固定紅線 C）。
- 「HER2 陽性／三陰性也可以做這個檢測來決定要不要化療」——ASCO 明確不建議 [S37]。
- 「Oncotype 的 18 分等於 MammaPrint 的低風險」——同一批腫瘤有 60.6% 被不同檢測
  分到不同類別 [S36]。
- 「停經前的人做這個檢測沒有意義」——過度反向；ASCO 允許用於停經前、淋巴結陰性者 [S37]，
  TAILORx 中 ≤50 歲、分數 0–10 者 9 年遠端復發 ≤1.8% [S31]。
- 「RxPONDER 證明停經前都要化療」——它證明的是在 1–3 顆淋巴結陽性、分數 ≤25 的
  停經前族群有效益，而 2026 年的 AMH 分析顯示**這個效益集中在卵巢儲備正常者** [S32][S33]。

**Caveats / safety notes**

- **這是全系列最可能造成不可逆傷害的一篇。** 兩個方向都要防：
  (a) 一個 ≤50 歲、中分數、臨床高風險的病人讀完決定不做化療——她 9 年遠端復發風險是
  12.3%，不是低風險 [S31]；
  (b) 一個停經後、1–3 顆淋巴結陽性、分數 ≤25 的病人被嚇去做化療——那組人 5 年
  無侵犯疾病存活 91.9% vs 91.3%，化療沒有帶來好處，只帶來神經病變、心臟毒性與
  次發性白血病風險 [S32]。
- **年齡／停經狀態的解釋要小心**：TAILORx 與 MINDACT 的作者都指出，年輕族群看到的
  化療效益**可能有一部分其實是化療造成的卵巢功能抑制**，而不是化療殺死癌細胞 [S35]；
  RxPONDER 的 2026 年 AMH 分析支持這個方向，而且該試驗的停經前受試者**大多沒有接受
  卵巢功能抑制** [S33]。這件事要寫成「所以你的醫師可能會跟你討論用卵巢功能抑制
  取代化療的選項」，而**不是**寫成「所以化療其實沒有用」。卵巢功能抑制的療程細節 → **B6**。
- 台灣的健保**不給付卵巢功能抑制作為一般輔助治療**（見下方 Taiwan status 與 [S69]），
  因此「用卵巢抑制取代化療」在台灣不是一個免費選項——這件事必須誠實寫出來，
  否則會給假的安心。
- 檢測本身也會出錯：台大的自費同意書把兩個方向的風險都列出來——
  檢測錯誤可能讓高復發風險者被判為低風險而**治療不足**，或讓低風險者被判為高風險而
  **治療過度** [S40]。這是一個很好的、來自台灣醫院官方文件的平衡素材。
- MINDACT 的年齡分析與 TAILORx 的年齡交互作用都是**探索性、檢定力不足**的分析 [S35]，
  誠實寫出來比寫得乾淨重要。
- 「這個檢測要自費、值不值得」的完整決策邏輯 → **D4**；本篇只寫適用範圍與試驗數字。
- A4 不得給任何分數或試驗數字；本篇是主場（SPEC 第六節）。

**Taiwan status**

- **多基因表現分析（Oncotype DX、MammaPrint 等）：健保不給付，屬自費。**
  查證路徑：`nhi.gov.tw`「全民健康保險醫療服務給付項目及支付標準」頁面
  （https://www.nhi.gov.tw/ch/lp-3778-1.html）之支付標準壓縮檔下載被 Cloudflare 攔截，
  改以站內搜尋「21 基因／多基因／復發風險評估／Oncotype／MammaPrint」，
  **零筆給付項目命中** [S41]。同時，健保於 2024 年 5 月 1 日起給付的
  「次世代基因定序（NGS）」是**為了選標靶藥**、且乳癌只涵蓋**三陰性乳癌**，
  與本篇談的省化療用途完全是另一條線 [S41]。
- 台大醫院官方說明暨同意書（文件編號 01400-4-602763，版次 2，2024 年 7 月核定）載明：
  Oncotype DX **需自費，自費價格為新臺幣 170,000 元**；檢體送往美國 Genomic Health Inc
  Laboratory 檢測；若因檢測限制無法出報告則不需負擔費用 [S40]。
  **寫作提醒**：這是單一醫院、2024 年 7 月的版本，價格會隨醫院與時間變動，
  文中要標明來源與版本，並寫「實際金額請跟你的個管師或醫院醫務課確認」。
- 同一份同意書列出的替代檢測：MammaPrint、EndoPredict、PAM50、Breast Cancer Index [S40]。

**Sources**

- **[S29] PASS** — Sparano JA, Gray RJ, Makower DF, et al. (2015). *Prospective Validation of a 21-Gene Expression Assay in Breast Cancer*. N Engl J Med 373(21):2005-2014. PMID 26412349, PMC4701034, doi 10.1056/nejmoa1510764 — TAILORx 低分數帶（RS 0–10）單用內分泌治療的結果。Route: Europe PMC REST (TITLE). https://europepmc.org/article/MED/26412349
- **[S30] PASS** — Sparano JA, Gray RJ, Makower DF, et al. (2018). *Adjuvant Chemotherapy Guided by a 21-Gene Expression Assay in Breast Cancer*. N Engl J Med 379(2):111-121. PMID 29860917, PMC6172658, doi 10.1056/nejmoa1804710 — TAILORx 主要結果與年齡×分數交互作用（P=0.004）。Route: Europe PMC REST (TITLE). https://europepmc.org/article/MED/29860917
- **[S31] PASS** — Sparano JA, Gray RJ, Ravdin PM, et al. (2019). *Clinical and Genomic Risk to Guide the Use of Adjuvant Therapy for Breast Cancer*. N Engl J Med 380(25):2395-2405. PMID 31157962, PMC6709671, doi 10.1056/nejmoa1904819 — 臨床風險＋基因分數的 9 年遠端復發率，含 ≤50 歲的 12.3% 那組。Route: Europe PMC REST (TITLE). https://europepmc.org/article/MED/31157962
- **[S32] PASS** — Kalinsky K, Barlow WE, Gralow JR, et al. (2021). *21-Gene Assay to Inform Chemotherapy Benefit in Node-Positive Breast Cancer*. N Engl J Med 385(25):2336-2347. PMID 34914339, PMC9096864, doi 10.1056/nejmoa2108873 — RxPONDER，停經前 vs 停經後的分歧。Route: Europe PMC REST (TITLE). https://europepmc.org/article/MED/34914339
- **[S33] PASS** — Kalinsky K, Barlow WE, Pathak HB, et al. (2026). *Ovarian reserve as a measure of adjuvant chemotherapy benefit in hormone receptor positive (HR-positive), HER2-negative, node-positive breast cancer in SWOG S1007 (RxPONDER)*. Ann Oncol 37(9):1220-1229. PMID 42613139, doi 10.1016/j.annonc.2026.05.697 — AMH ≥10 pg/mL 者才有化療效益（HR 0.46 vs 1.27）。Route: Europe PMC REST (AUTH+TITLE). https://europepmc.org/article/MED/42613139
- **[S34] PASS** — Cardoso F, van't Veer LJ, Bogaerts J, et al. (2016). *70-Gene Signature as an Aid to Treatment Decisions in Early-Stage Breast Cancer*. N Engl J Med 375(8):717-729. PMID 27557300, doi 10.1056/nejmoa1602253 — MINDACT 主要結果。Route: Europe PMC REST (TITLE). https://europepmc.org/article/MED/27557300
- **[S35] PASS** — Piccart M, van 't Veer LJ, Poncet C, et al. (2021). *70-gene signature as an aid for treatment decisions in early breast cancer: updated results of the phase 3 randomised MINDACT trial with an exploratory analysis by age*. Lancet Oncol 22(4):476-488. PMID 33721561, doi 10.1016/s1470-2045(21)00007-3 — 8.7 年追蹤與依年齡／淋巴結的探索性分析。Route: Europe PMC REST (AUTH+TITLE). https://europepmc.org/article/MED/33721561
- **[S36] PASS** — Bartlett JM, Bayani J, Marshall A, et al. (2016). *Comparing Breast Cancer Multiparameter Tests in the OPTIMA Prelim Trial: No Test Is More Equal Than the Others*. J Natl Cancer Inst 108(9):djw050. PMID 27130929, PMC5939629, doi 10.1093/jnci/djw050 — 同一批腫瘤上五種檢測的不一致率 60.6%。Route: Europe PMC REST (TITLE). https://europepmc.org/article/MED/27130929
- **[S37] PASS** — Andre F, Ismaila N, Allison KH, et al. (2022). *Biomarkers for Adjuvant Endocrine and Chemotherapy in Early-Stage Breast Cancer: ASCO Guideline Update*. J Clin Oncol 40(16):1816-1837. PMID 35439025, doi 10.1200/jco.22.00069 — 適用族群界線；明文不建議用於 HER2 陽性或三陰性。截至 2026-08-29，Europe PMC 未查到更新版。Route: Europe PMC REST (TITLE). https://europepmc.org/article/MED/35439025
- **[S38] PASS** — Pan H, Gray R, Braybrooke J, et al.; EBCTCG. (2017). *20-Year Risks of Breast-Cancer Recurrence after Stopping Endocrine Therapy at 5 Years*. N Engl J Med 377(19):1836-1846. PMID 29117498, PMC5734609, doi 10.1056/nejmoa1701830 — 依 T/N 分層的第 5–20 年遠端復發風險（10–41%）。Route: Europe PMC REST (TITLE). https://europepmc.org/article/MED/29117498
- **[S39] FAIL（並非查證失敗，而是「東西不存在」）** — OPTIMA 主試驗（英國，以 Oncotype DX 指導化療的大型隨機試驗）**截至 2026-08-29 沒有主要結果的期刊發表**。Europe PMC 以 `TITLE:"OPTIMA" AND TITLE:"breast"` 與 `AUTH:"Stein RC" AND TITLE:"OPTIMA"` 查詢，只回傳 OPTIMA prelim 的可行性研究、招募方法學、價值分析與檢測比較（[S36]）。**文中不得暗示 OPTIMA 有結果。**
- **[S40] PASS（台灣機構文件）** — 國立臺灣大學醫學院附設醫院。《Oncotype DX 安可待乳癌腫瘤基因檢測（Oncotype DX Breast Recurrence Score）說明暨同意書》（文件編號 01400-4-602763，版次 2；2024 年 7 月 15 日品質暨病人安全委員會審核通過、2024 年 7 月 23 日病歷委員會修正通過）。載明適應症（ER+ 或 PR+、HER2−、N− 或 N+）、檢測錯誤的雙向風險、替代檢測，以及「此項檢測需自費，檢測自費價格為 170,000 元」。https://www.ntuh.gov.tw/ckfinder_file/path/files/2763(1005%E8%99%9F)Oncotype_DX%E5%AE%89%E5%8F%AF%E5%BE%85%E4%B9%B3%E7%99%8C%E8%85%AB%E7%98%A4%E5%9F%BA%E5%9B%A0%E6%AA%A2%E6%B8%AC(Oncotype_DX_Breast_Recurrence_Score)%E8%AA%AA%E6%98%8E%E6%9A%A8%E5%90%8C%E6%84%8F%E6%9B%B8%E9%9B%BB%E5%AD%90%E7%97%85%E6%AD%B7%E7%89%88%E6%9C%AC(%E7%B4%99%E6%9C%AC%E7%89%88%E6%9C%AC)(%E7%89%882)20240730.pdf
- **[S41] PARTIAL / 零命中（如實記錄）** — 台灣健保之多基因表現分析給付狀態。查證路徑：(1)「全民健康保險醫療服務給付項目及支付標準」頁面 https://www.nhi.gov.tw/ch/lp-3778-1.html 之支付標準壓縮檔（115.08.01 生效、115.08.13 更新）與開放資料平台 CSV，兩者下載均遭 Cloudflare challenge 阻擋，**無法逐條全文檢索**；(2) 改以站內搜尋「21 基因」「多基因」「復發風險評估」「Oncotype」「MammaPrint」，**未命中任何給付項目或項目代碼（零筆）**；(3) 健保署新聞稿〈健保 5 月 1 日起給付癌症精準醫療「實體癌/血癌次世代基因定序檢測(NGS)」〉https://www.nhi.gov.tw/ch/cp-14565-e02e0-3255-1.html 顯示 113/5/1 起給付之 NGS 涵蓋 9 種實體癌，乳癌僅限**三陰性乳癌**，用途為選擇標靶藥物，分三級支付（BRCA 檢測 10,000 點、≤100 基因 20,000 點、>100 基因 30,000 點），每人每癌別終生一次。**結論：查無多基因表現分析之健保給付項目；文中一律寫「這一項目前要自費，實際費用與是否有其他方案，請跟你的個管師或醫院醫務課確認」。**

---

# B5 — HER2 陽性：藥怎麼排

**Key facts**

- NSABP B-31 與 NCCTG N9831 聯合分析（n=4,046，HER2 陽性可手術乳癌；
  AC → paclitaxel ± trastuzumab；中位追蹤 8.4 年）：加 trastuzumab 使整體存活相對改善 37%
  （HR 0.63，95% CI 0.54–0.73，P<0.001），**10 年整體存活由 75.2% 提高到 84.0%**；
  無病存活相對改善 40%（HR 0.60，0.53–0.68，P<0.001），10 年無病存活由 62.2% 提高到 73.7% [S42]
- HERA（BIG 1-01，n=5,099 意向治療；HER2 陽性早期乳癌；觀察 vs trastuzumab 1 年 vs 2 年）：
  中位追蹤 11 年，1 年 trastuzumab vs 觀察的無病存活 HR 0.76（95% CI 0.68–0.86）、
  死亡 HR 0.74（0.64–0.86）；10 年無病存活 63%（觀察）、69%（1 年）、69%（2 年）。
  **2 年並不優於 1 年**（HR 1.02，95% CI 0.89–1.17）。
  觀察組有 884 人（52%）後來交叉接受 trastuzumab [S43]
- HERA 的心臟事件（次要心臟終點，附分母）：2 年組 122/1,700（7.3%）、
  1 年組 74/1,702（4.4%）、觀察組 15/1,697（0.9%）；多數發生在治療期間 [S43]
- Cochrane 系統性回顧（8 個試驗、11,991 名 HER2 陽性早期或局部晚期乳癌病人）：
  含 trastuzumab 之療程的整體存活 HR 0.66（95% CI 0.57–0.77）、無病存活 HR 0.60（0.50–0.71）；
  **鬱血性心衰竭風險比 RR 5.11（90% CI 3.00–8.72）、左心室射出分率下降 RR 1.83（1.36–2.47）** [S50]
- APHINITY（n=4,805；HER2 陽性、淋巴結陽性或高風險淋巴結陰性之可手術乳癌；
  63% 淋巴結陽性、36% 荷爾蒙受體陰性）：在化療＋1 年 trastuzumab 之外加 pertuzumab，
  3 年無侵犯疾病存活 94.1% vs 93.2%，HR 0.81（95% CI 0.66–1.00，P=0.045）。
  **淋巴結陽性次群組** 92.0% vs 90.2%（HR 0.77，0.62–0.96，P=0.02）；
  **淋巴結陰性次群組** 97.5% vs 98.4%（HR 1.13，0.68–1.86，P=0.64） [S44]
- APHINITY 第三次期中分析（中位追蹤 8.4 年，n=4,804）：
  8 年整體存活 92.7%（pertuzumab）vs 92.0%（安慰劑），HR 0.83（95% CI 0.68–1.02，P=0.078），
  **未達 0.006 的顯著性門檻**；淋巴結陽性者 HR 0.80（0.63–1.00）、淋巴結陰性者 HR 0.99（0.64–1.55）。
  8 年無侵犯疾病存活在淋巴結陽性族群絕對改善 4.9 個百分點（86.1% vs 81.2%，HR 0.72，0.60–0.87）；
  **淋巴結陰性族群不加 pertuzumab 也表現很好**（安慰劑組 8 年 iDFS 93.3%、OS 96.4%） [S45]
- APHINITY 的心臟安全性（n=4,769 安全族群，中位追蹤 74 個月）：
  心臟事件 159 人（3.3%）——pertuzumab＋trastuzumab 組 83/2,400（3.5%）、
  trastuzumab 組 76/2,405（3.2%）；77.4%（123 例）發生於抗 HER2 治療期間，
  83.6%（133 例）為無症狀或輕微症狀的射出分率下降；心因性死亡各組各 2 例（0.1%）；
  155 例中有 127 例（81.9%）急性恢復。心臟風險因子為 >65 歲、BMI ≥25、
  基線射出分率 55%–<60%、以及使用含 anthracycline 之化療 [S46]
- PERSEPHONE（英國，n=4,088，HER2 陽性早期乳癌且有化療適應症）：
  6 個月 vs 12 個月 trastuzumab，中位追蹤 5.4 年，4 年無病存活 89.4% vs 89.8%，
  HR 1.07（90% CI 0.93–1.24），**非劣性 p=0.011（達成非劣性）**；
  6 個月組嚴重不良事件較少（373/1,939，19% vs 459/1,894，24%，p=0.0002），
  因心臟毒性停藥者較少（61/1,939，3% vs 146/1,894，8%，p<0.0001） [S47]
- PHARE（法國，n=3,380 意向治療，HER2 陽性非轉移性乳癌）：
  6 個月 vs 12 個月，中位追蹤 7.5 年，無病存活的校正 HR 為 1.08（95% CI 0.93–1.25，p=0.39），
  **95% CI 上界超過非劣性界限 1.15，故未能證明非劣性**；
  作者結論：輔助 trastuzumab 的標準療程仍應為 12 個月 [S48]
- **兩個試驗方向相反**：PERSEPHONE 達成非劣性、PHARE 未達成 [S47][S48]
- APT（單臂第二期，n=406 接受治療；**腫瘤 ≤3 cm、淋巴結陰性**之 HER2 陽性乳癌；
  平均年齡 55 歲、67.0% 荷爾蒙受體陽性）：weekly paclitaxel 12 週＋trastuzumab 共 1 年，
  中位追蹤 10.8 年，10 年無侵犯疾病存活 91.3%（95% CI 88.3–94.4）、
  10 年無復發間期 96.3%（94.3–98.3）、10 年整體存活 94.3%（91.8–96.8）、
  10 年乳癌特異存活 98.8%（97.6–100）。31 件 iDFS 事件中，9 件（29.0%）是
  **對側新發乳癌**、10 件（32.3%）是任何原因死亡，僅 6 件（19.4%）是遠端復發 [S49]
- 術前治療後有殘餘病灶者換 T-DM1（KATHERINE）：7 年無侵犯疾病存活 80.8% vs 67.1%
  （HR 0.54，95% CI 0.44–0.66），7 年整體存活 89.1% vs 84.4%（HR 0.66，0.51–0.87，P=0.003）；
  ≥3 級不良事件 26.1% vs 15.7% [S25]（完整背景見 B3）

**Claim ceiling**

Defensible：「HER2 陽性早期乳癌加上 trastuzumab，10 年整體存活由約 75% 提高到約 84%，
這是整個乳癌治療史上少見的大幅度改變。1 年是標準療程，2 年沒有更好。
雙標靶（加 pertuzumab）的額外好處**集中在淋巴結陽性的人身上**，
淋巴結陰性者幾乎看不到，而且到目前為止**整體存活的改善仍未達統計顯著**。
腫瘤小、淋巴結陰性的人有減量療程（12 週 paclitaxel＋1 年 trastuzumab）可選。
術前治療後仍有殘餘病灶，換成 T-DM1 是有隨機試驗支持的升階治療。」

Would overstate：
- 「雙標靶比單標靶好，大家都該用」——APHINITY 的 8 年整體存活 HR 0.83（P=0.078）
  未達顯著門檻，淋巴結陰性者 HR 0.99 [S45]。
- 「trastuzumab 打半年就夠了」——PERSEPHONE 與 PHARE 結論相反 [S47][S48]，
  而且兩者都是**族群層級的平均**，不等於任何一位病人可以自行縮短。
- 「trastuzumab 對心臟很安全」——HERA 的次要心臟終點 1 年組 4.4% vs 觀察組 0.9%；
  Cochrane 的鬱血性心衰竭 RR 5.11（90% CI 3.00–8.72）[S43][S50]。
  正確的說法是「大多數是無症狀的射出分率下降、多數可恢復，但風險確實升高，
  所以治療期間要定期做心臟超音波」。
- 「APT 的 10 年存活 94.3% 代表小腫瘤幾乎不會有事」——APT 是**單臂**試驗，沒有對照組 [S49]。
- 「殘餘病灶＝失敗」→ 見 B3 的 caveats。

**Caveats / safety notes**

- **固定紅線 A（急症警語）**：本篇提到 trastuzumab、pertuzumab、T-DM1、taxane，
  必須有一段寫出**藥名＋具體症狀＋當天聯絡治療團隊**：
  trastuzumab／pertuzumab／T-DM1 的**心臟功能下降**（走路或平躺時喘、腳腫、明顯心跳快）、
  taxane 的**過敏反應與手腳麻木**、化療期間的**發熱性嗜中性球低下**（發燒 ≥38°C）。
  完整清單 → **C4**，本篇只留這幾條並指過去。
- 心臟毒性要給分母，不要只寫「可能影響心臟」：HERA 1 年組 74/1,702（4.4%）[S43]；
  APHINITY 雙標靶組 83/2,400（3.5%），其中 83.6% 是無症狀或輕微的射出分率下降、
  81.9% 有恢復 [S46]。
- 心臟風險因子（>65 歲、BMI ≥25、基線射出分率 55%–<60%、含 anthracycline 的化療）
  是可以在門診談的具體項目 [S46]——這是本篇最好的「下次門診可以問出口的問題」。
- **不可暗示病人可以自行縮短療程**。PERSEPHONE 的 6 個月是隨機分派下的族群結果，
  而 PHARE 沒能證明非劣性；療程長度是要由團隊決定的。
- pCR 的意義與殘餘病灶的判讀 → **B3**；本篇只寫「殘餘病灶就換 T-DM1」這個藥物排列。
- HER2 判讀與再檢驗 → **A2**；亞型如何決定整條路線 → **A3**。

**Taiwan status**（依健保署「藥品給付規定」第 9 節現行合訂本，網站標示 115.8.21 更新）

- **Trastuzumab（9.18）早期乳癌**：限 HER2 過度表現（IHC 3+ 或 FISH+）。
  - **有腋下淋巴結轉移但無遠處臟器轉移者**（事審代碼 C50P2）：若用於術前輔助治療，
    術後達 pCR 者，本藥品／pertuzumab＋trastuzumab／Phesgo 三者手術前後合計
    **以 18 個療程為上限**；術後 non-pCR 者，本藥品與 T-DM1 合計 18 個療程為上限，
    其中 T-DM1 上限 14 個療程。若未做術前治療而先手術，須接受至少 4 個療程化療，
    上限 18 個療程 [S51]
  - **無腋下淋巴結轉移者**：條件較細，且**依 ER 狀態與藥品品項而異**。
    先手術者須符合「ER 陰性且腫瘤 >0.5 公分（C50P4）」或「ER 陽性且腫瘤 >1 公分（C50P5）」，
    並限用 Eirgasun vial 420 mg、Herzuma、Ogivri，上限 18 個療程；
    術前治療且 ER 陰性、術後達 pCR 者，Herceptin 為 9 個療程上限、
    上述三個品項為 18 個療程上限（115/7/1、115/8/1 新修訂） [S51]
  - 須事前審查；早期乳癌每 24 週檢附療效評估再申請 [S51]
- **Pertuzumab（9.70）早期乳癌**：與 trastuzumab 及化療併用，
  限 HER2 過度表現（IHC 3+ 或 FISH+）**且具腋下淋巴結轉移、無遠處臟器轉移**者。
  用於術前輔助治療者，須**術後達 pCR** 才可續用至 18 個療程；
  未做術前治療而先手術者，可用於術後輔助治療，上限 18 個療程。須事前審查，每 24 週再申請 [S51]
  - **這條和 APHINITY 的證據方向一致**：健保把 pertuzumab 限在淋巴結陽性族群，
    而 APHINITY 的效益也集中在該族群 [S45][S51]。這一點值得在文中點出來。
  - Pertuzumab 用於早期乳癌是 **113/12/1（2024 年 12 月 1 日）**才納入給付的新規定 [S52]
- **Pertuzumab 與 trastuzumab 皮下注射複方製劑（Phesgo，9.112）**：早期乳癌亦有給付規定，
  與上述療程上限合併計算 [S51]
- **T-DM1（9.87）早期乳癌**：條件見 B3 的 Taiwan status（殘餘病灶、ER 與腫瘤大小條件、
  **術後 12 週內**須開始或提出申請、射出分率 <45% 或有症狀心衰竭者排除、
  上限 14 個療程、與 trastuzumab 合計 18 個療程） [S51]
- **共同的行政現實**：以上全部**須事前審查**，且療程上限是手術前後合併計算的。
  這代表「術前用掉幾個療程」會影響術後還剩幾個療程——這是門診值得問清楚的一件事。
- **gap**：本 brief 未查到 trastuzumab 生物相似藥各品項之間可否互換的完整條文
  （現行條文中多處以「限使用 Eirgasun、Herzuma、Ogivri」限定品項，但未見完整互換規則）；
  請寫成「哪一個廠牌、能不能換，要跟你的個管師或醫院醫務課確認」。

**Sources**

- **[S42] PASS** — Perez EA, Romond EH, Suman VJ, et al. (2014). *Trastuzumab plus adjuvant chemotherapy for human epidermal growth factor receptor 2-positive breast cancer: planned joint analysis of overall survival from NSABP B-31 and NCCTG N9831*. J Clin Oncol 32(33):3744-3752. PMID 25332249, PMC4226805, doi 10.1200/jco.2014.55.5730 — 10 年整體存活 75.2% → 84.0%。Route: Europe PMC REST (AUTH+TITLE). https://europepmc.org/article/MED/25332249
- **[S43] PASS** — Cameron D, Piccart-Gebhart MJ, Gelber RD, et al. (2017). *11 years' follow-up of trastuzumab after adjuvant chemotherapy in HER2-positive early breast cancer: final analysis of the HERceptin Adjuvant (HERA) trial*. Lancet 389(10075):1195-1205. PMID 28215665, PMC5465633, doi 10.1016/s0140-6736(16)32616-2 — 1 年為標準、2 年無額外效益；心臟事件附分母。Route: Europe PMC REST (TITLE). https://europepmc.org/article/MED/28215665
- **[S44] PASS** — von Minckwitz G, Procter M, de Azambuja E, et al. (2017). *Adjuvant Pertuzumab and Trastuzumab in Early HER2-Positive Breast Cancer*. N Engl J Med 377(2):122-131. PMID 28581356, PMC5538020, doi 10.1056/nejmoa1703643 — APHINITY 主要分析，含淋巴結陽性／陰性次群組。Route: Europe PMC REST (TITLE). https://europepmc.org/article/MED/28581356
- **[S45] PASS** — Loibl S, Jassem J, Sonnenblick A, et al. (2024). *Adjuvant Pertuzumab and Trastuzumab in Early Human Epidermal Growth Factor Receptor 2-Positive Breast Cancer in the APHINITY Trial: Third Interim Overall Survival Analysis With Efficacy Update*. J Clin Oncol 42(31):3643-3651. PMID 39259927, doi 10.1200/jco.23.02505 — 8.4 年追蹤，整體存活未達顯著（P=0.078）。Route: Europe PMC REST (AUTH+TITLE). https://europepmc.org/article/MED/39259927
- **[S46] PASS** — de Azambuja E, Agostinetto E, Procter M, et al. (2023). *Cardiac safety of dual anti-HER2 blockade with pertuzumab plus trastuzumab in early HER2-positive breast cancer in the APHINITY trial*. ESMO Open 8(1):100772. PMID 36681013, PMC10044361, doi 10.1016/j.esmoop.2022.100772, Open Access — 心臟事件率、可恢復比例與風險因子，附分母。Route: Europe PMC REST (TITLE). https://europepmc.org/article/MED/36681013
- **[S47] PASS** — Earl HM, Hiller L, Vallier AL, et al. (2019). *6 versus 12 months of adjuvant trastuzumab for HER2-positive early breast cancer (PERSEPHONE): 4-year disease-free survival results of a randomised phase 3 non-inferiority trial*. Lancet 393(10191):2599-2612. PMID 31178152, PMC6615016, doi 10.1016/s0140-6736(19)30650-6, Open Access — 達成非劣性。Route: Europe PMC REST (TITLE). https://europepmc.org/article/MED/31178152
- **[S48] PASS** — Pivot X, Romieu G, Debled M, et al. (2019). *6 months versus 12 months of adjuvant trastuzumab in early breast cancer (PHARE): final analysis of a multicentre, open-label, phase 3 randomised trial*. Lancet 393(10191):2591-2598. PMID 31178155, doi 10.1016/s0140-6736(19)30653-1 — **未**達成非劣性，結論維持 12 個月。Route: Europe PMC REST (TITLE). https://europepmc.org/article/MED/31178155
- **[S49] PASS** — Tolaney SM, Tarantino P, Graham N, et al. (2023). *Adjuvant paclitaxel and trastuzumab for node-negative, HER2-positive breast cancer: final 10-year analysis of the open-label, single-arm, phase 2 APT trial*. Lancet Oncol 24(3):273-285. PMID 36858723, doi 10.1016/s1470-2045(23)00051-7 — 小腫瘤減量療程的 10 年結果；**單臂、無對照組**。Route: Europe PMC REST (TITLE). https://europepmc.org/article/MED/36858723
- **[S50] PASS** — Moja L, Tagliabue L, Balduzzi S, et al. (2012). *Trastuzumab containing regimens for early breast cancer*. Cochrane Database Syst Rev (4):CD006243. PMID 22513938, PMC6718210, doi 10.1002/14651858.cd006243.pub2 — 8 試驗、11,991 人；鬱血性心衰竭 RR 5.11、射出分率下降 RR 1.83。Route: Europe PMC REST (TITLE). https://europepmc.org/article/MED/22513938
- **[S51] PASS（台灣官方法規）** — 衛生福利部中央健康保險署。《藥品給付規定》第 9 節 抗癌瘤藥物（現行合訂本，網站標示 115.8.21 更新；共 102 頁）。條文 9.1 Aromatase Inhibitors、9.18 Trastuzumab、9.70 Pertuzumab、9.72 CDK4/6 抑制劑、9.87 Trastuzumab emtansine、9.107 Abemaciclib、9.112 Phesgo。取得方式：健保署「最新版藥品給付規定內容(分章節)」頁 https://www.nhi.gov.tw/ch/np-3397-1.html → 第九節 PDF https://www.nhi.gov.tw/ch/dl-55685-99c675b771ab4b2789c891bc8db447ce-1.pdf
- **[S52] PASS（台灣官方法規）** — 衛生福利部中央健康保險署。《「藥品給付規定」修訂對照表 第 9 節 抗癌瘤藥物（自 113 年 12 月 1 日生效）》。內含 pertuzumab（9.70）首度納入早期乳癌給付、Phesgo（9.112）新增、以及 trastuzumab（9.18）早期乳癌條文之對照修訂。https://www.nhi.gov.tw/ch/dl-76370-ffd2512e78c84b55b3c37bbef7b1beee-1.pdf

---

# B6 — 抗荷爾蒙藥要吃五年還是十年 【紅線 5】

**Key facts — 五年的基礎效果**

- EBCTCG 個別病人資料統合分析（20 個試驗、21,457 人；約 5 年 tamoxifen vs 不用）：
  在 **ER 陽性**族群（n=10,645），復發率比 RR 0.53（SE 0.03）於第 0–4 年、
  0.68（0.06）於第 5–9 年（皆 2p<0.00001），第 10–14 年 0.97（0.10）——
  **停藥後保護仍延續約十年**。乳癌死亡率在前 15 年降低約三分之一
  （RR 0.71／0.66／0.68 於三個時段）。**在 ER 陰性族群，tamoxifen 對復發與死亡幾乎沒有作用** [S53]
- EBCTCG（31,920 名停經後 ER 陽性早期乳癌女性）：5 年芳香環酶抑制劑（AI）vs 5 年 tamoxifen，
  10 年乳癌死亡 12.1% vs 14.2%（RR 0.85，95% CI 0.75–0.96，2p=0.009）。
  代價：**5 年骨折風險 8.2%（AI）vs 5.5%（tamoxifen），RR 1.42（95% CI 1.28–1.57）**；
  子宮內膜癌則較少（10 年 0.4% vs 1.2%，RR 0.33，0.21–0.51） [S55]

**Key facts — 停在五年之後，風險還在**

- EBCTCG（88 個試驗、62,923 名 ER 陽性、完成 5 年內分泌治療且第 5 年時無病之女性）：
  **第 5 年到第 20 年，復發以穩定速率持續發生**。遠端復發風險依原始 T/N：
  T1N0 13%、T1N1-3 20%、T1N4-9 34%；T2N0 19%、T2N1-3 26%、T2N4-9 41%。
  T1N0 依分化度：低 10%、中 13%、高 17%（同期任何復發或對側乳癌則為 17%、22%、26%）。
  分化度與 Ki-67 在已知 T/N 之後只有中等的獨立預測力；PR 與 HER2 狀態則無預測力 [S38]

**Key facts — 延長到十年：tamoxifen**

- ATLAS（n=12,894 完成 5 年 tamoxifen 者隨機分派；本段數字為其中 6,846 名 **ER 陽性**者）：
  續用到 10 年 vs 停在 5 年——復發 617/3,428 vs 711/3,418（p=0.002）；
  乳癌死亡 331 vs 397（p=0.01）；全因死亡 639 vs 722（p=0.01） [S54]
- **效益出現得很晚**：復發率比第 5–9 年 0.90（95% CI 0.79–1.02）、第 10 年之後 0.75（0.62–0.90）；
  乳癌死亡率比第 5–9 年 0.97（0.79–1.18）、第 10 年之後 0.71（0.58–0.88）。
  第 5–14 年累積復發 21.4% vs 25.1%；第 5–14 年乳癌死亡 12.2% vs 15.0%
  （**絕對死亡率降低 2.8 個百分點**） [S54]
- 代價（全部 12,894 人）：肺栓塞 RR 1.87（95% CI 1.13–3.07，p=0.01；兩組死亡率皆 0.2%）；
  子宮內膜癌 RR 1.74（1.30–2.34，p=0.0002），第 5–14 年累積風險 3.1%（死亡 0.4%）
  vs 1.6%（死亡 0.2%），**絕對死亡增加 0.2 個百分點**；
  缺血性心臟病反而較少 RR 0.76（0.60–0.95，p=0.02）；中風 RR 1.06（0.83–1.36） [S54]

**Key facts — 延長到十年：芳香環酶抑制劑**

- MA.17R（n=1,918 停經後、荷爾蒙受體陽性、已完成含 AI 之 5 年治療者）：
  再加 letrozole 5 年 vs 安慰劑，中位追蹤 6.3 年——
  5 年無病存活 95%（95% CI 93–96）vs 91%（89–93），復發或對側乳癌 HR 0.66（P=0.01）；
  **5 年整體存活 93% vs 94%，HR 0.97（P=0.83，沒有差別）**；
  對側乳癌年發生率 0.21%（letrozole）vs 0.49%（安慰劑），HR 0.42（P=0.007）。
  letrozole 組骨痛、骨折與新發生骨質疏鬆較多 [S56]
- ABCSG-16／SALSA（n=3,484，停經後、荷爾蒙受體陽性，已完成 5 年內分泌治療）：
  再用 anastrozole **2 年 vs 5 年**（總計 7 年 vs 10 年）——
  主要分析族群（n=3,208）8 年時兩組各 335 件無病存活事件，
  HR 0.99（95% CI 0.85–1.15，P=0.90）；多數次要終點亦無差異。
  **5 年組的臨床骨折風險較高，HR 1.35（95% CI 1.00–1.84）** [S57]

**Key facts — 卵巢功能抑制（OFS）**

- SOFT／TEXT 8 年更新（停經前、ER／PR 陽性早期乳癌；SOFT 三臂：tamoxifen、
  tamoxifen＋OFS、exemestane＋OFS）：SOFT 的 8 年無病存活 78.9%（tamoxifen 單用）、
  83.2%（tamoxifen＋OFS）、85.9%（exemestane＋OFS）（tamoxifen 單用 vs 加 OFS，P=0.009）；
  8 年整體存活 91.5%、93.3%、92.1%（tamoxifen 單用 vs 加 OFS，P=0.01）。
  **在化療後仍維持停經前狀態者**，三組 8 年整體存活為 85.1%、89.4%、87.2% [S58]
- 同一報告的代價：≥3 級不良事件在 tamoxifen 單用 24.6%、tamoxifen＋OFS 31.0%、
  exemestane＋OFS 32.3% [S58]
- SOFT＋TEXT 合併長期追蹤（n=4,690，中位追蹤 13 年）：exemestane＋OFS vs tamoxifen＋OFS，
  12 年無病存活絕對改善 4.6 個百分點（HR 0.79，95% CI 0.70–0.90，P<0.001）、
  無遠端復發間期絕對改善 1.8 個百分點（HR 0.83，0.70–0.98，P=0.03）；
  **12 年整體存活 90.1% vs 89.1%，HR 0.93（95% CI 0.78–1.11），無顯著差異**。
  HER2 陰性次群組（占 86.0%）12 年整體存活絕對改善 2.0 個百分點（HR 0.85，0.70–1.04），
  接受化療者（占 45.9%）改善 3.3 個百分點；<35 歲者 4.0、腫瘤 >2 cm 者 4.5、
  第 3 級分化者 5.5 個百分點 [S59]

**Key facts — 中斷與不規則服藥的代價（紅線 5 的核心）**

- Kaiser Permanente 北加州世代（n=8,769，第 I–III 期荷爾蒙敏感性乳癌，1996–2007 診斷）：
  到第 4.5 年時 **32% 已停藥**；在持續服藥者當中 **72% 達到完全遵從**（藥物持有率 ≥80%）；
  合計**只有 49% 的病人以最佳方式吃完整個療程**。
  **<40 歲者停藥風險最高（HR 1.51，95% CI 1.23–1.85）** [S60]
- 同一世代的死亡率分析：8,769 人中 2,761 人（31%）提早停藥；在繼續服藥者中
  1,684 人（28%）未達遵從。中位追蹤 4.4 年、813 人死亡。
  10 年估計存活率：持續服藥者 80.7% vs 停藥者 73.6%（P<0.001）；
  在持續服藥者中，遵從者 81.7% vs 不遵從者 77.8%（P<0.001）。
  校正臨床與人口學變項後，**提早停藥 HR 1.26（95% CI 1.09–1.46）、
  不遵從 HR 1.49（1.23–1.81）**，皆為全因死亡的獨立預測因子 [S61]
- BIG 1-98 隨機試驗內的遵從度分析（n=6,144 停經後荷爾蒙受體陽性早期乳癌）：
  提早停用 letrozole 與無病存活變差有關（多變項 HR 1.45，95% CI 1.09–1.93，P=0.01）；
  遵從分數 <90% 亦然（HR 1.61，95% CI 1.08–2.38，P=0.02）。
  **提早停藥的原因中 82.7% 是不良事件**；換藥序貫組的不持續率較高
  （tamoxifen→letrozole 20.8%、letrozole→tamoxifen 20.3% vs 單用 tamoxifen 16.9%、
  單用 letrozole 17.6%） [S62]
- **台灣本土資料**：健保資料庫世代（2003–2010 新診斷、接受手術並使用輔助內分泌治療
  至少 12 個月者，n=30,573，平均診斷年齡 52.1±11.6 歲）——
  **中斷（連續兩張處方間隔 >180 天）者 4,565 人（14.9%）**；
  **不遵從（藥物持有率 <80%）者 6,942 人（22.7%）**。
  校正後，中斷與全因死亡相關（HR 1.32，95% CI 1.20–1.46，P<0.0001）、
  不遵從亦然（HR 1.45，95% CI 1.32–1.59，P<0.0001）。
  **中斷與不遵從對死亡率的影響在較年輕族群更明顯**；敏感度分析顯示中斷次數越多、
  遵從門檻越高，死亡風險越高（劑量—反應趨勢） [S63]

**Key facts — CDK4/6 抑制劑加在內分泌治療上（追蹤仍短）**

- monarchE（n=5,637；**HR 陽性、HER2 陰性、淋巴結陽性、高復發風險**早期乳癌）：
  內分泌治療加 abemaciclib 2 年。中位追蹤 54 個月時，
  無侵犯疾病存活 HR 0.680（95% CI 0.599–0.772）、無遠端復發存活 HR 0.675（0.588–0.774）；
  **5 年絕對改善 iDFS 7.6、DRFS 6.7 個百分點**（4 年時為 6.0／5.3，3 年時為 4.8／4.1）；
  該次期中分析**整體存活未達統計顯著** [S65]
- monarchE 主要整體存活分析（中位追蹤 76.2 個月，2026 年發表）：
  死亡風險降低 15.8%（661 件死亡；HR 0.842，95% CI 0.722–0.981，P=0.027），
  **達到預設顯著性界限**；**7 年整體存活 86.8% vs 85.0%（絕對差 1.8 個百分點）**。
  7 年 iDFS 77.4% vs 70.9%（絕對差 6.5 個百分點，HR 0.734，0.657–0.820）；
  7 年 DRFS 80.0% vs 74.9%（絕對差 5.1 個百分點，HR 0.746，0.662–0.840）。
  仍存活但帶有轉移性疾病者 6.4%（abemaciclib）vs 9.4%（單用內分泌） [S64]
- **對 monarchE 的公開批評**（Lancet Oncology，2023）：一群方法學研究者發表
  〈Review of the monarchE trial suggests no evidence to support use of adjuvant abemaciclib
  in women with breast cancer〉，主張當時的資料不足以支持常規使用 [S68]。
  這篇批評早於 2026 年的整體存活結果，寫的時候要標明時序。
- NATALEE（n 依報告；**HR 陽性、HER2 陰性、解剖分期 IIA（N1 或具高風險因子之 N0）、
  IIB 或 III** 之早期乳癌；停經前女性與男性另加 goserelin）：
  ribociclib 400 mg/日（3 週用 1 週停）3 年＋非固醇類 AI vs 單用 AI。
  期中分析（截止 2023-01-11，426 件事件）：**3 年無侵犯疾病存活 90.4% vs 87.1%**
  （HR 0.75，95% CI 0.62–0.91，P=0.003） [S66]
- NATALEE 5 年追蹤（中位 iDFS 追蹤 55.4 個月）：HR 0.716（95% CI 0.618–0.829）；
  **絕對 iDFS 差距由 3 年的 2.7 個百分點擴大到 5 年的 4.5 個百分點**；
  N0 次群組 HR 0.606（95% CI 0.372–0.986）；
  **整體存活仍在成熟中：HR 0.800（95% CI 0.637–1.003），名目單側 log-rank P=0.026** [S67]

**Claim ceiling**

Defensible：「五年的內分泌治療已經把復發與死亡風險降低了一大截，而且停藥之後保護
還會延續一段時間。但 ER 陽性乳癌的復發是**在停藥後的第 5 到 20 年持續發生的**，
所以『要不要吃到十年』是一個真實的問題。延長治療能再減少一些復發，
但**絕對獲益不大、而且很晚才出現**，同時帶來明確的骨頭與（tamoxifen 的）子宮內膜與
血栓代價。適合誰要看原本的期別、淋巴結數目與分化度，以及你自己的骨質狀況。
**中斷與不規則服藥有明確的死亡代價，包括在台灣的資料裡。** 有副作用要講出來，
因為換藥、加藥物處理、調整方式都做得到；但不可以自己停。」

Would overstate：
- 「十年一定比五年好」——ABCSG-16 顯示 7 年與 10 年沒有差別，而且 10 年組骨折更多
  （HR 1.35）[S57]；MA.17R 的整體存活沒有改善（HR 0.97，P=0.83）[S56]。
- 「延長治療能救命」——ATLAS 的第 5–14 年乳癌死亡絕對降低 2.8 個百分點 [S54]；
  MA.17R 的整體存活無差異 [S56]。要給絕對數字，不要只給相對風險。
- 「加 CDK4/6 抑制劑可以取代把藥吃完」——monarchE 與 NATALEE 都是**加在**
  內分泌治療之上，不是取代 [S64][S66]。
- 「monarchE 證明可以延長存活很多」——7 年整體存活絕對差 1.8 個百分點 [S64]。
- 「NATALEE 也證明能延長存活」——**還沒有**；整體存活 HR 0.800，95% CI 上界 1.003，
  仍在成熟中 [S67]。
- **「受不了可以先停一陣子」「先停幾個月再說」「反正吃五年就夠了自己停也還好」
  ——這三句任何一句出現就是失敗（紅線 5）。**

**Caveats / safety notes**

- **紅線 5 的兩件相反的事，要在同一段裡做到**：
  (a) **叫她把副作用講出來**——BIG 1-98 顯示提早停藥的原因中 82.7% 是不良事件 [S62]，
  而換藥（tamoxifen ↔ AI）、加藥物處理、調整服藥時間都是門診做得到的事；
  (b) **不准自己停**——並且要說明為什麼：療程長度本身就是療效的一部分。
  台灣健保資料庫的 30,573 人資料顯示，中斷者全因死亡 HR 1.32、不遵從者 HR 1.45，
  而且中斷次數越多、風險越高 [S63]。這是本地的、有分母的、可以直接引用的數字。
- **年輕病人是最高風險族群**：<40 歲停藥風險 HR 1.51 [S60]；台灣資料也顯示
  中斷與不遵從對死亡率的影響在較年輕族群更明顯 [S63]。文中要對這一群多說一句。
- 骨頭的代價要寫出來、而且要寫成「可以處理」而不是「所以別吃」：
  AI 的 5 年骨折風險 8.2% vs tamoxifen 5.5%（RR 1.42）[S55]；
  延長 AI 到 10 年的骨折 HR 1.35 [S57]。骨密度追蹤與骨保護藥物 → **D3**。
- **副作用的完整內容與處理方式 → C5**，本篇只寫療程長度的決定；兩篇互相指路，不重疊
  （SPEC 第六節）。C5 也要有「不可自行中斷」這句話。
- 提到 CDK4/6 抑制劑就觸發**固定紅線 A**：本篇只留一兩條與 abemaciclib／ribociclib
  相關的當天聯絡警語（血球下降造成的發燒或異常出血、嚴重腹瀉合併脫水、
  肝功能異常的黃疸或深色尿、ribociclib 的心律問題如暈厥或心悸），完整清單 → **C4**。
- **生育保存與治療期間的避孕 → C6**；OFS 對生育的影響在本篇一句話帶過即可。
- monarchE 與 NATALEE 的追蹤仍短（中位 76.2 與 55.4 個月）[S64][S67]，
  而且兩者的高風險族群定義不同（monarchE 限淋巴結陽性且高風險；NATALEE 涵蓋部分 N0），
  **不可把兩個試驗的數字混在一起講**。

**Taiwan status**

- **Tamoxifen**：健保給付之常規用藥。**本 brief 未在第 9 節查到獨立的 tamoxifen 給付規定條文**
  （第 9 節的 aromatase inhibitor 條文中多次以「使用 tamoxifen 五年證明」為前提），
  給付細節請寫成「跟個管師或醫院醫務課確認」。
- **芳香環酶抑制劑（藥品給付規定 9.1）——這一節與國際指引的落差很大，必須寫清楚**：
  - **Letrozole（9.1.3）**：第 3 款給付「停經後且荷爾蒙接受體陽性之早期乳癌病人，
    經外科手術切除後之輔助治療」，**每日最大劑量 2.5 mg、使用不得超過 5 年**；
    若由 tamoxifen 轉換，兩者合計亦不得超過 5 年 [S51]
  - **Letrozole 的延伸治療（9.1.3 第 2 款）**：限「停經後、荷爾蒙接受體陽性、
    **有淋巴結轉移**之乳癌病人，作為 tamoxifen 治療 **五年後**的延伸治療」，
    且**手術後 ≥11 年且無復發者不得使用**、**使用不得超過 4 年**、
    不得與其他 AI 併用；病歷須留存 tamoxifen 使用五年之證明 [S51]
  - **Exemestane（9.1.1 第 2 款）**：限「雌激素受體陽性之停經婦女，使用 tamoxifen
    **至少兩年**之高危險早期侵犯性乳癌的輔助治療」，**使用不得超過 3 年**，
    不得與 tamoxifen 或其他 AI 併用 [S51]
  - **Anastrozole（9.1.2 第 3 款）**：早期侵犯性乳癌的給付**限於「有血栓栓塞症或
    子宮內膜異常增生的高危險群，而無法使用 tamoxifen 治療者」**，
    並列出三種具體情形（腦血管梗塞病史、靜脈血栓栓塞症病史、
    經陰道超音波判定為子宮內膜異常增生高危險群）；備註「療程期間以不超過五年為原則」 [S51]
  - **寫作要點**：台灣的給付路徑與國際「停經後首選 AI」的建議並不完全一致，
    而且**延長到十年的路徑受到明確的條文限制**（letrozole 延伸限淋巴結陽性、
    須先吃滿五年 tamoxifen、術後 11 年以上不給付、延伸不超過 4 年）。
    這是門診真實會遇到的落差，要誠實寫出來，但**不要寫成批評特定醫院或醫師**，
    批評的對象只能是「規則跟證據之間還有距離」。
- **卵巢功能抑制（GnRH analogue；藥品給付規定 5.5.1）——這是本篇最大的台灣落差**：
  - 早期乳癌的給付（5.5.1 第 2 項第 (3) 款）須**完全符合以下六點**：
    (I) **與 tamoxifen 合併使用，作為手術後取代化學治療之輔助療法**；
    (II) 荷爾蒙接受體強陽性（ER/PR 為 2+ 或 3+）；
    (III) HER2 FISH 陰性或 IHC 1+；
    (IV) **淋巴結轉移數目 ≤3 個**；
    (V) 使用期限：leuprorelin、goserelin 或 triptorelin **使用 3 年**，tamoxifen 使用 5 年；
    (VI) **須事前審查，並於申請時說明無法接受化學治療的原因** [S69]
  - 轉移性的給付（第 (2) 款）另有規定：荷爾蒙接受體陽性、停經前婦女有轉移性乳癌 [S69]
  - **這代表**：SOFT／TEXT 支持的「化療之外再加卵巢功能抑制」，以及 B4 提到的
    「用卵巢功能抑制取代化療」這個選項，在台灣健保的條文下**都不是直接可及的**——
    現行條文把 OFS 定位成「**取代**化療」而非「**加在**化療之上」，
    而且與 exemestane 併用的組合（SOFT／TEXT 的最佳臂）**不在條文允許的組合裡**。
    這一點必須誠實寫出來，並寫成「這是要跟你的醫師與個管師確認自費與申請可能性的事」。
- **Abemaciclib（9.107）**：**有給付**，但條件很窄。
  併用內分泌療法（tamoxifen 或 AI），限 **HR 陽性（ER 或 PR >30%）、HER2 陰性、
  淋巴結陽性、高復發風險**之早期乳癌成年女性，須符合下列之一：
  (1) 陽性腋下淋巴結 ≥4 顆；(2) 陽性腋下淋巴結 1–3 顆且腫瘤 ≥5 cm；
  (3) 陽性腋下淋巴結 1–3 顆且腫瘤細胞分化第 3 級。
  使用前須已接受標準化學及放射輔助治療；使用前**最多只能接受 12 週的內分泌治療**，
  且應於**手術切除後 16 個月內**開始；須事前審查、每 24 週再申請；
  **每日至多 2 錠、使用不得超過 2 年**；使用中若疾病惡化須停用且不得再用其他 CDK4/6 抑制劑 [S51]
- **Ribociclib 用於早期乳癌（NATALEE 適應症）：健保不給付。**
  第 9 節 9.72「CDK4/6 抑制劑（如 ribociclib；palbociclib）」的全部給付條件都限於
  **遠端轉移後**的全身性藥物治療；早期乳癌的 CDK4/6 給付只有 abemaciclib（9.107）一條 [S51]。
  同一條文並規定「若先前於早期乳癌使用 abemaciclib 無效後……不得再申請
  ribociclib、palbociclib」，以及晚期使用終生給付上限 24 個月 [S51]。
- **gap**：本 brief 未查到「延長內分泌治療期間之骨密度檢查與骨保護藥物」的給付條文
  （屬 D3 範圍）；亦未查到 Breast Cancer Index 等「要不要延長」預測工具的給付項目
  （[S41] 的零命中同樣適用）。兩者一律寫成「要跟個管師或醫院醫務課確認」。

**Sources**

- **[S53] PASS** — Early Breast Cancer Trialists' Collaborative Group (EBCTCG), Davies C, Godwin J, et al. (2011). *Relevance of breast cancer hormone receptors and other factors to the efficacy of adjuvant tamoxifen: patient-level meta-analysis of randomised trials*. Lancet 378(9793):771-784. PMID 21802721, PMC3163848, doi 10.1016/s0140-6736(11)60993-8, Open Access — 5 年 tamoxifen 的效果與其 ER 依賴性。Route: Europe PMC REST (TITLE). https://europepmc.org/article/MED/21802721
- **[S54] PASS** — Davies C, Pan H, Godwin J, et al. (2013). *Long-term effects of continuing adjuvant tamoxifen to 10 years versus stopping at 5 years after diagnosis of oestrogen receptor-positive breast cancer: ATLAS, a randomised trial*. Lancet 381(9869):805-816. PMID 23219286, PMC3596060, doi 10.1016/s0140-6736(12)61963-1, Open Access — 十年 tamoxifen 的絕對效益與絕對代價。Route: Europe PMC REST (TITLE). https://europepmc.org/article/MED/23219286
- **[S55] PASS** — Early Breast Cancer Trialists' Collaborative Group (EBCTCG). (2015). *Aromatase inhibitors versus tamoxifen in early breast cancer: patient-level meta-analysis of the randomised trials*. Lancet 386(10001):1341-1352. PMID 26211827, doi 10.1016/s0140-6736(15)61074-1 — 31,920 名停經後 ER 陽性者；骨折 8.2% vs 5.5%。Route: Europe PMC REST (TITLE). https://europepmc.org/article/MED/26211827
- **[S56] PASS** — Goss PE, Ingle JN, Pritchard KI, et al. (2016). *Extending Aromatase-Inhibitor Adjuvant Therapy to 10 Years*. N Engl J Med 375(3):209-219. PMID 27264120, PMC5024713, doi 10.1056/nejmoa1604700 — MA.17R；無病存活改善但整體存活無差異、骨頭代價明確。Route: Europe PMC REST (TITLE). https://europepmc.org/article/MED/27264120
- **[S57] PASS** — Gnant M, Fitzal F, Rinnerthaler G, et al. (2021). *Duration of Adjuvant Aromatase-Inhibitor Therapy in Postmenopausal Breast Cancer*. N Engl J Med 385(5):395-405. PMID 34320285, doi 10.1056/nejmoa2104162 — ABCSG-16／SALSA；7 年與 10 年無差異，10 年組骨折較多。Route: Europe PMC REST (TITLE). https://europepmc.org/article/MED/34320285
- **[S58] PASS** — Francis PA, Pagani O, Fleming GF, et al. (2018). *Tailoring Adjuvant Endocrine Therapy for Premenopausal Breast Cancer*. N Engl J Med 379(2):122-137. PMID 29863451, PMC6193457, doi 10.1056/nejmoa1803164 — SOFT／TEXT 8 年更新，含化療後仍停經前者的次群組。Route: Europe PMC REST (TITLE). https://europepmc.org/article/MED/29863451
- **[S59] PASS** — Pagani O, Walley BA, Fleming GF, et al. (2023). *Adjuvant Exemestane With Ovarian Suppression in Premenopausal Breast Cancer: Long-Term Follow-Up of the Combined TEXT and SOFT Trials*. J Clin Oncol 41(7):1376-1382. PMID 36521078, PMC10419413, doi 10.1200/jco.22.01064 — 中位追蹤 13 年；12 年整體存活無顯著差異。Route: Europe PMC REST (AUTH+TITLE). https://europepmc.org/article/MED/36521078
- **[S60] PASS** — Hershman DL, Kushi LH, Shao T, et al. (2010). *Early discontinuation and nonadherence to adjuvant hormonal therapy in a cohort of 8,769 early-stage breast cancer patients*. J Clin Oncol 28(27):4120-4128. PMID 20585090, PMC2953970, doi 10.1200/jco.2009.25.9655 — 4.5 年停藥 32%、僅 49% 完整最佳服藥；<40 歲風險最高。Route: Europe PMC REST (TITLE). https://europepmc.org/article/MED/20585090
- **[S61] PASS** — Hershman DL, Shao T, Kushi LH, et al. (2011). *Early discontinuation and non-adherence to adjuvant hormonal therapy are associated with increased mortality in women with breast cancer*. Breast Cancer Res Treat 126(2):529-537. PMID 20803066, PMC3462663, doi 10.1007/s10549-010-1132-4 — 停藥 HR 1.26、不遵從 HR 1.49。Route: Europe PMC REST (TITLE). https://europepmc.org/article/MED/20803066
- **[S62] PASS** — Chirgwin JH, Giobbie-Hurder A, Coates AS, et al. (2016). *Treatment Adherence and Its Impact on Disease-Free Survival in the Breast International Group 1-98 Trial of Tamoxifen and Letrozole, Alone and in Sequence*. J Clin Oncol 34(21):2452-2459. PMID 27217455, PMC4962733, doi 10.1200/jco.2015.63.8619 — 隨機試驗內的遵從度與無病存活；停藥原因 82.7% 為不良事件。Route: Europe PMC REST (TITLE). https://europepmc.org/article/MED/27217455
- **[S63] PASS（台灣本土資料）** — Hsieh KP, Chen LC, Cheung KL, Chang CS, Yang YH. (2014). *Interruption and non-adherence to long-term adjuvant hormone therapy is associated with adverse survival outcome of breast cancer women — an Asian population-based study*. PLoS One 9(2):e87027. PMID 24586261, PMC3931619, doi 10.1371/journal.pone.0087027, Open Access — 台灣健保資料庫 30,573 人；中斷 14.9%、不遵從 22.7%；死亡 HR 1.32 / 1.45。Route: Europe PMC REST (ABSTRACT+TITLE)，分母與比例取自 Europe PMC 全文（PMC3931619）Results 段與 Table 2。https://europepmc.org/article/MED/24586261
- **[S64] PASS** — Johnston S, Martin M, O'Shaughnessy J, et al. (2026). *Overall survival with abemaciclib in early breast cancer*. Ann Oncol 37(2):155-165. PMID 41110697, doi 10.1016/j.annonc.2025.10.005 — monarchE 主要整體存活分析；7 年 OS 86.8% vs 85.0%（絕對差 1.8 個百分點）。Route: Europe PMC REST (AUTH+TITLE). https://europepmc.org/article/MED/41110697
- **[S65] PASS** — Rastogi P, O'Shaughnessy J, Martin M, et al. (2024). *Adjuvant Abemaciclib Plus Endocrine Therapy for Hormone Receptor-Positive, Human Epidermal Growth Factor Receptor 2-Negative, High-Risk Early Breast Cancer: Results From a Preplanned monarchE Overall Survival Interim Analysis, Including 5-Year Efficacy Outcomes*. J Clin Oncol 42(9):987-993. PMID 38194616, PMC10950161, doi 10.1200/jco.23.01994 — 5 年 iDFS 絕對改善 7.6 個百分點；該次期中分析 OS 未達顯著。Route: Europe PMC REST (AUTH+TITLE). https://europepmc.org/article/MED/38194616
- **[S66] PASS** — Slamon D, Lipatov O, Nowecki Z, et al. (2024). *Ribociclib plus Endocrine Therapy in Early Breast Cancer*. N Engl J Med 390(12):1080-1091. PMID 38507751, doi 10.1056/nejmoa2305488 — NATALEE 期中分析；3 年 iDFS 90.4% vs 87.1%。Route: Europe PMC REST (AUTH+TITLE). https://europepmc.org/article/MED/38507751
- **[S67] PASS** — Crown J, Stroyakovskii D, Yardley DA, et al. (2025). *Adjuvant ribociclib plus nonsteroidal aromatase inhibitor therapy in patients with HR-positive/HER2-negative early breast cancer: 5-year follow-up of NATALEE efficacy outcomes and updated overall survival*. ESMO Open 10(11):105858. PMID 41320342, PMC12684762, doi 10.1016/j.esmoop.2025.105858, Open Access — 5 年追蹤；整體存活 HR 0.800（95% CI 0.637–1.003），尚未成熟。Route: Europe PMC REST (AUTH+TITLE). https://europepmc.org/article/MED/41320342
- **[S68] PASS** — Meirson T, Goldstein DA, Gyawali B, Tannock IF. (2023). *Review of the monarchE trial suggests no evidence to support use of adjuvant abemaciclib in women with breast cancer*. Lancet Oncol 24(6):589-593. PMID 37146621, doi 10.1016/s1470-2045(23)00165-1 — 對 monarchE 的方法學批評（發表於整體存活結果之前）。作者回覆見 Lancet Oncol 24(6):e238（PMID 37146620）。Route: Europe PMC REST (TITLE). https://europepmc.org/article/MED/37146621
- **[S69] PASS（台灣官方法規）** — 衛生福利部中央健康保險署。《藥品給付規定》第 5 節 荷爾蒙及影響內分泌機轉藥物，條文 5.5.1 Gn-RH analogue（如 Buserelin；Goserelin；Leuprorelin；Triptorelin；Nafarelin），第 2 項第 (2)(3) 款（停經前乳癌之給付條件）。取得方式：健保署「最新版藥品給付規定內容(分章節)」頁 https://www.nhi.gov.tw/ch/np-3397-1.html → 第五節 PDF https://www.nhi.gov.tw/ch/dl-42511-66ac909b574f4f5c9c1c96042873cab4-1.pdf
- **[S70] FAIL（東西不存在，不是查證失敗）** — aTTom 試驗（英國，tamoxifen 10 年 vs 5 年）**沒有主要結果的完整期刊發表**，僅有 2013 年 ASCO 會議摘要。Europe PMC 以 `TITLE:"aTTom" AND TITLE:"tamoxifen"` 查詢，回傳的是 Trans-aTTom 的 Breast Cancer Index 生物標記研究（Clin Cancer Res 2022;28(9):1871-1880，PMID 35144966；Ann Oncol 2019;30(11):1776-1783，PMID 31504126）、一篇評論與兩篇試驗招募相關通訊，**沒有主要療效結果的原始論文**。**文中不得引用 aTTom 的任何數字**；十年 tamoxifen 的證據一律以 ATLAS [S54] 為準，並可誠實寫出「另一個英國試驗只發表過會議摘要，沒有完整論文」。

---

## 給 SPEC 的修正建議（研究階段發現的、與紅線假設不一致之處）

1. **紅線 4（B1）的「等效」用詞**：SPEC 寫「保留手術加放療 vs 全乳房切除的等效證據」。
   隨機證據（Veronesi、NSABP B-06）確實是等效 [S1][S2]，但兩者都是 1970 年代收案；
   而 2021 年的瑞典全國世代（n=48,986）在校正共病與社經地位後顯示**保留＋放療優於全切**
   （全切未放療 vs 保留＋放療全因死亡 HR 1.79）[S5]。
   建議把紅線 4 的必寫項改成「**保留＋放療的長期存活不比全切差；近年觀察性資料甚至顯示更好，
   但那不是隨機證據**」，並明確要求寫出兩個奠基試驗的年代限制。

2. **紅線 4 的 CPM 句子可以更強、也更精確**：SPEC 寫「對側預防性乳房切除對非帶因者
   沒有被證實的存活好處」。2024 年 JAMA Oncology 的 66 萬人 SEER 配對世代提供了
   更好的講法：**對側乳癌幾乎被消滅（20 年 6.9% → 極少），乳癌死亡率完全沒有差別
   （8.50% vs 8.54%）**，原因是對側乳癌是高風險體質的**標記**而非死亡的**原因** [S7]。
   建議把這個「標記 vs 原因」的機制寫進紅線，因為它同時解釋了為什麼手術有效、
   卻救不了命——這比單純說「沒有好處」更能讓焦慮的人讀下去。
   另需補一句：SEER 沒有 BRCA 狀態，這是推論而非測量。

3. **B2 需要一條新的紅線或至少一條必寫警語**：SPEC 對 B2 沒有設紅線，但
   **INSEMA 第二次隨機分派（2026）在前哨淋巴結巨轉移者省略腋清的 5 年 iDFS 是
   86.6% vs 93.8%，HR 1.69，P=0.058** [S16]。這與「腋下去階梯是安全的」的一般印象方向相反。
   建議在 B2 加一句必寫：「**在前哨淋巴結有巨轉移的情況下，省略腋下廓清目前只有
   檢定力不足的資料，而且點估計方向不利；這不是病人可以自己要求的事。**」

4. **紅線 1（B4）的「年齡與停經狀態」需要更新為「卵巢功能」**：SPEC 寫
   「年齡與停經狀態會改變同一個分數的意義」。這仍然正確，但 2026 年 RxPONDER 的
   AMH 分析把它精確化了——化療效益集中在**卵巢儲備正常（AMH ≥10 pg/mL）**者
   （HR 0.46 vs 低儲備者 HR 1.27）[S33]，而 MINDACT 作者也把年輕族群的化療效益
   歸因於「可能是化療造成的卵巢功能抑制」[S35]。
   建議把紅線 1 的必寫項擴充成「**年齡、停經狀態與卵巢功能**會改變同一個分數的意義，
   而且年輕族群看到的化療效益可能有一部分來自化療造成的卵巢功能抑制」。

5. **紅線 1 需要補一個台灣特有的陷阱**：承上，B4 若寫「可以用卵巢功能抑制取代化療」，
   在台灣會給假的安心——健保的 GnRH analogue 早期乳癌給付把 OFS 定位成
   「**取代**化學治療」、限**與 tamoxifen 併用**、ER/PR 2+ 或 3+、HER2 陰性、
   **淋巴結 ≤3 顆**、GnRH 只給 3 年，且須事前審查並說明無法化療的原因 [S69]。
   SOFT／TEXT 最有效的組合（exemestane＋OFS）**不在條文允許的組合裡**。
   建議在紅線 1 與紅線 5 各加一句：**談 OFS 時必須同時寫出台灣的給付條文限制**。

6. **紅線 5（B6）可以用台灣本土數字，比國外資料更有力**：SPEC 說「中斷率極高，
   而中斷有明確的復發代價」。台灣健保資料庫 30,573 人的研究給了在地數字：
   中斷 14.9%、不遵從 22.7%、全因死亡 HR 1.32 / 1.45，且年輕族群影響更大 [S63]。
   建議把「引用台灣本土資料」寫進紅線 5 的必寫項。
   另外，**「中斷」的操作型定義是「連續兩張處方間隔超過 180 天」**，
   這比「自己停一陣子」聽起來更具體，適合直接寫進文章。

7. **B6 的 CDK4/6 段落需要標明「兩個試驗不可混談」**：monarchE 已在 2026 年拿到
   顯著的整體存活（7 年 86.8% vs 85.0%，絕對差 1.8 個百分點）[S64]，
   而 NATALEE 的整體存活仍未成熟（HR 0.800，95% CI 0.637–1.003）[S67]，
   且兩者的高風險族群定義不同（monarchE 限淋巴結陽性；NATALEE 涵蓋部分 N0）。
   台灣只給付 abemaciclib（且條件比 monarchE 的收案條件更窄），**ribociclib 早期乳癌不給付** [S51]。
   建議在 B6 加一句必寫：**不可把 monarchE 與 NATALEE 的數字混在一起講。**

8. **B5 的「HERA/joint analysis 長期」在 SPEC 中被列為「trastuzumab adjuvant benefit」——
   實際上這兩篇是不同的東西**：HERA 是「trastuzumab vs 觀察」且有 52% 交叉 [S43]，
   聯合分析是 NSABP B-31／N9831 的「化療±trastuzumab」[S42]。
   10 年整體存活 75.2%→84.0% 這個最有力的數字來自**聯合分析**，不是 HERA。
   建議 SPEC 把兩者分開列，避免撰稿時把數字掛錯試驗。

9. **B5 的「duration questions（PERSEPHONE/PHARE）」在 SPEC 中被寫成
   「什麼showed 及其限制」——但兩者的結論是相反的**：PERSEPHONE 達成非劣性 [S47]，
   PHARE **未**達成非劣性且明確主張維持 12 個月 [S48]。
   建議 SPEC 明確要求「必須寫出兩個試驗結論相反」，否則很容易被寫成「半年就夠了」。

10. **全系列的 NCCN 引用要拿掉**：NCCN 的指引頁在本次查證中回傳 HTTP 403，
    **連版本字串都無法確認** [S8]。建議 SPEC 明確禁止全系列引用 NCCN，
    改以 ASCO [S37][S19]、ESMO [S28]、St Gallen [S27] 為指引來源。
    另請注意 ESMO 早期乳癌指引雖書目可查（Ann Oncol 2024;35(2):159-182），
    但**官方著陸頁與 Europe PMC 都取不到內容**，因此只能引用「這是現行版本」，
    不得引用其中任何具體建議 [S28]。

11. **日期**：任務書寫「今天是 2026-08-27」，系統日期為 2026-08-29。
    所有「截至今日查無更新」的判斷以 **2026-08-29** 為準。
