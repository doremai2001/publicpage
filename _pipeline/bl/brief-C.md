# Brief C — 膀胱癌專題 肌肉侵犯型：兩條路（C1–C5）

研究員：Group C｜查證日期：2026-09-13
期刊文獻全部經 Europe PMC REST（`search?query=EXT_ID/DOI/TITLE&resultType=core`）逐筆核對書目與摘要數字；
OA 全文經 `/webservices/rest/<PMCID>/fullTextXML` 取得；指引原文為官方 landing page（uroweb.org、nice.org.uk）
與官方 PDF（auanet.org）實際抓取；試驗狀態經 `clinicaltrials.gov/api/v2/studies/<NCT>`；
健保條文出自政府資料開放平臺 dataset 174451 指向的健保署官方 txt 檔實際下載後全文檔搜尋。
**NCCN 依 SPEC §四不引。**

引用規則：**只有標 PASS 的來源可以進正文。** FAIL 條目保留，讓寫作者知道查過什麼、哪些話只能寫「查不到可引用的來源」。

---

## ⚠ 與 SPEC 假設不同形狀的事（動筆前必讀）

### 1. BC2001 沒有「想做而收不到」的那個比較——收案不足收掉的只有 SPARE 一個

SPEC §一.3 寫「SPARE 與 BC2001 想做的那個比較都因收案不足收掉」。**查不到任何支持後半句的紀錄。**
BC2001（ISRCTN68324339 / NCT00024349）是**完成的**第 3 期試驗，收了 458 人、其中 360 人進入「放療 vs 同步化放療」
的隨機比較，做完了，而且是陽性結果[C-S4][C-S5]。它從來不是一個比較膀胱切除的試驗。

真正因收案不足關掉的是 **SPARE（CRUK/07/011，ISRCTN61126465）**：2007-07-20 收第一位、**2010-02-12 依 IDMC 與 TSC
建議關閉收案，累計 45 人（RC 25、SBP 20），30 個月**[C-S2]。Zlotta 2023 的摘要用複數「Previous randomised controlled
trials comparing bladder preservation with radical cystectomy … closed due to insufficient accrual」[C-S1]，
但**可查證被點名的只有 SPARE**：EAU 2026 指引[C-S19] 與 CA Cancer J Clin 2025 的回顧[C-S40] 都只寫 SPARE 一個。

**→ 正文修正**：寫「這一題只有一個現代的隨機試驗真的開起來過，叫 SPARE，收案收不到而在 2010 年關掉」。
不可寫「SPARE 與 BC2001 都收掉了」。

### 2. 而且，「完全沒有隨機試驗」這句話要再修一次——有一個 1991 年的完成試驗

**Sell 1991（DAVECA protocol 8201，丹麥，n=183，T2–T4a）**[C-S36]：隨機分成「術前放療 40 Gy＋膀胱切除」
對「根治性放療 60 Gy＋有殘存腫瘤時挽救性切除」。結果是「合併治療組存活率有較高的趨勢，但未達統計顯著」。
1983–1986 收案，**沒有同步化療，不是今天的三聯療法**。AUA 2024 指引把它當成「the RCT」在引[C-S20]。

**→ 正文最誠實的那一句應該是**：「**膀胱全切除對現代三聯療法（刮除＋同步化放療），沒有完成的隨機試驗**」——
EAU 2026 自己的措辭可直接引：「**No successfully completed RCTs are available comparing the outcomes of TMT with RC.**」[C-S19]。
**不可**寫成「這一題完全沒有隨機試驗」（1991 年那個存在），也不可寫成「只有配對世代」（BC2001、BCON、RTOG 0712 都是隨機試驗，
只是它們比較的是放療內部的問題，不是兩條路）。

### 3. BC2001 的「第 3–4 級不良事件上升」沒有達顯著，作者的結論句是反向的

SPEC §四紅線 2 要求 BC2001 的三個數字同框，第三個寫成「第 3 到 4 級不良事件上升」。原始數字是：
**治療期間 36.0%（化放療）vs 27.5%（單純放療），p=0.07；追蹤期間 8.3% vs 15.7%，p=0.07（化放療組反而較低）**，
NEJM 的結論句是「**with no significant increase in adverse events**」[C-S4]。

**→ 正文修正**：第三個數字要寫成「急性期第 3–4 級不良事件從 27.5% 升到 36.0%，但這個差距沒有達到統計顯著（p=0.07）」。
寫成「上升」而不標 p 值，會超過資料。**紅線 2 的精神（不可把化療寫成「只是加強」）仍然成立**，
因為真正撐得住的代價數字在別處：RTOG 0712 的治療相關第 3–4 級毒性 FCT 組 64%、GD 組 55%[C-S9]；
配對世代統合分析的急性 ≥3 級毒性彙總 11.4%[C-S33]。

### 4. 「選擇偏差往三聯療法好看的方向倒」——實際上是三個不同方向，不能只寫一個

- **配對／單中心世代：往三聯療法好看倒。** Zlotta 的 440 位膀胱切除病人「**represent 29% of all radical cystectomies
  performed during the study period**」——也就是同期每 10 個切膀胱的人裡，只有約 3 個在腫瘤條件上本來就兩條路都能走[C-S1]。
  三聯療法那一組是被挑過的、有動機的、腫瘤條件好的人。
- **登記資料：往三聯療法難看倒。** NCDB 2004–2013（n=32,300，AJCC II–III 期）配對後，
  同步化放療對膀胱切除的死亡風險比 **HR 1.406（95% CI 1.235–1.601）**，方向偏切除[C-S30]；
  SEER 2010–2022（T2N0M0，n=10,495）配對後 5 年 OS **62.6%（RC）vs 36.7%（TMT）**[C-S31]。
  這些資料庫裡的三聯療法病人本來就比較老、體況比較差、共病比較多（RISC 國際世代直接量過：p<0.01）[C-S32]。
- **統計層面第三個方向：informative censoring，往膀胱切除好看倒。** Robesti 2025（6 篇、8,594 人，重建 KM 曲線）
  發現 12 個報告終點裡有 10 個存在追蹤中斷的不平衡，整體在 OS／MFS／DFS 上**偏向膀胱切除**（log-rank 皆 p<0.01）；
  **但校正後膀胱切除仍然較優（5 年 OS 42% vs 30%，p<0.001）**，作者的結論句是
  「challenge the acceptance of TMT based on retrospective comparison in spite of randomization」[C-S34]。

**→ 正文修正**：C1 不能只寫「偏差往保留膀胱好看的方向倒」。要寫三格：單中心配對世代往保留倒、
全國登記資料往切除倒、而且有人論證統計方法本身也往切除倒。**三格都寫，才是誠實。**

### 5. 「約兩到三成最後仍要切除膀胱」——偏高，正確的中心值是約兩成

| 來源 | 族群／設計 | 挽救性膀胱切除比率 |
|---|---|---|
| Schuettfort 2021 統合分析[C-S14] | 73 篇、9,110 人，追蹤 >5 年的研究 | **19.2%** |
| EAU 2026[C-S19] | 現代三聯療法系列彙總 | 10–30% |
| Zlotta 2023[C-S1] | 配對世代，282 位三聯療法 | 13%（38/282） |
| BC2001 10 年[C-S5] | 隨機試驗，T2–T4a | 5 年切除率 **化放療 14%（95% CI 9–21）vs 單純放療 22%（16–31）** |
| RISC 國際真實世界[C-S32] | 265 位保留膀胱 | 4%（10/265）——但這個世代只有 45% 真的用了同步化療 |

**→ 正文修正**：寫「**大約每五個人有一個，最後還是要切掉膀胱**」，並把 10–30% 這個區間與它為什麼這麼寬
（選人條件、追蹤密度、有沒有做同步化療）寫在同一段。「兩到三成」只能當上界寫。

### 6. 「台灣的保留膀胱做得太少」——我查不到任何台灣端的分母，而且國際數字比 SPEC 預期的更複雜

- **台灣端：零。** 健保「醫療服務給付項目及支付標準」全文檔搜尋「**膀胱癌**」**零筆**；「低分次」僅三筆
  （36022B、36023B 乳癌，36024B 直腸癌），**沒有膀胱癌的低分次或強度調控放療獨立項目**[C-S39]。
  癌症登記的膀胱癌期別分布：hpa.gov.tw **TLS 連線失敗**（見 FAIL-4），mohw.gov.tw 對應頁面只到統計處目錄層。
  **沒有任何可引的台灣三聯療法使用率。**
- **國際端：使用率已經接近指引說的「適合比例」。** SEER 2010–2022，T2N0M0：三聯療法從 **11.9% 升到 26.2%**[C-S31]；
  EAU 2026 說「**In contemporary series, approximately 25-30% of cystectomy candidates may be appropriate for
  bladder preservation**」[C-S19]。兩個數字的分母不一樣（前者是全部 T2N0M0，後者是膀胱切除候選人），
  不能直接相減，但**「國際上保留膀胱明顯做得太少」這個說法，用 2026 年的美國登記資料已經支撐不住了**。

**→ 給作者的話（這一段是本節的重點）**：主張「台灣的保留膀胱做得太少」**在台灣可能仍然成立**，
但這份 brief 給不出任何台灣的數字去證明它。**可引的只有三樣**：
① 指引自己怎麼寫該不該討論兩條路（EAU「**For all suitable candidates, both bladder-preserving techniques and RC
should be discussed**」、「**should be offered to all suitable candidates … and not only to patients with significant
comorbidities**」[C-S19][C-S1]；NICE「**Offer a choice of radical cystectomy or radiotherapy with a radiosensitiser**」[C-S21]）；
② 台灣健保確實把兩條路的每一個構件都給付了（見各篇台灣端）；
③ 作者自己的門診觀察，**必須寫成觀察、標明是他的看法、放在利益揭露之後**。
**不可寫**「台灣比國際低」「台灣的使用率只有 X%」——沒有這個數字。
**不可寫**任何歸因句（SPEC §一.2 第二道護欄）。

### 7. 兩個小的校正

- **EAU 與 AUA 的三聯療法選人條件真的不一樣，NICE 根本不給腫瘤條件。** 這對紅線 2 是好消息（可以並陳），
  但也意味著「選人條件」不能寫成一張統一的表。詳見 C4。
- **CA Cancer J Clin 2025 的回顧把 SWOG S1011 的 90 天死亡數字轉錯了**（寫成 16/292 vs 9/300）。
  NEJM 原文是 **19 人（7%）vs 7 人（2%）**[C-S43]。**一律以 NEJM 原文為準。**

---

## C1 `bl-two-roads`〈切掉膀胱，還是保留膀胱〉【紅線 1，全專題最高風險，雙向】【利益揭露】

### Key facts

**A. 這一題的證據地基：沒有完成的隨機比較（可直接引的四句）**

1. EAU 2026 指引原文：「**No successfully completed RCTs are available comparing the outcomes of TMT with RC.**」[C-S19]
2. Zlotta 2023 摘要第一句：「Previous randomised controlled trials comparing bladder preservation with radical
   cystectomy for muscle-invasive bladder cancer closed due to insufficient accrual. **Given that no further trials
   are foreseen**, we aimed to use propensity scores…」[C-S1]
3. SPARE 為什麼關掉，作者自己的話（OA 全文）[C-S2]：
   - 「SPARE closed due to failure to meet the predefined minimum target recruitment rate, **even though there had been
     extensive efforts and qualitative research to support recruitment**.」
   - 「**Low randomisation rates and frequent deviations from allocated treatment suggest patients have a reluctance to
     allow randomisation to determine which of two contrasting treatment strategies they should receive.**」
   - 「An additional contributor to early closure of the study was the smaller than anticipated number of patients eligible
     for all treatment modalities. This, in addition to **a lack of equipoise amongst clinicians**, had a major impact.」
   - 結論句：「Randomising patients with MIBC between RC and SBP based on response to neoadjuvant chemotherapy **was not
     feasible in the UK health system. Strong clinician and patient preferences for treatments impacted willingness to
     undergo randomisation and acceptance of treatment allocation.**」
4. SPARE 的招募數字（全部帶分母，寫「為什麼做不起來」用）[C-S2]：篩檢登記 T2–3 N0 M0 共 **796 人**→
   **490 人不合格（多數是體況撐不住化療＋切除＋放療三種治療）**→另 141 人雖可能合格但沒被詢問（轉診路徑複雜）→
   **165 人被詢問、45 人同意（27%）**。**拒絕的 120 人中，51 人自己偏好放療、25 人偏好手術、44 人不明。**
   分到膀胱切除組的 25 人中有 **6 人（24%）最後接受了放療**；整體 36/45（80.0%，95% CI 65.4–90.4）照分組接受了根治治療。

**B. 唯一完成的隨機試驗（1991，不是三聯療法）**

Sell 1991，DAVECA 8201，丹麥，1983–1986，**n=183**（T2–T4a，尿路上皮癌）[C-S36]：
術前放療 40 Gy＋計畫性膀胱切除（88 人）對 根治性放療 60 Gy＋殘存腫瘤時挽救性切除（95 人）。
計畫執行率 66/88（75%）vs 88/95（92%），**放療組 27 人（28%）接受了挽救性切除**。
結果：「a trend to a higher survival rate following the combined treatment … **but a statistical significant difference
could not be demonstrated**」。手術併發症在計畫性與挽救性切除之間沒有差別，沒有術後死亡。
**男性病人在膀胱切除後全部發生勃起功能喪失。**
→ **標籤必須寫足**：1980 年代、沒有同步化療、放療劑量與技術都不是今天的做法。

**C. 最好的配對世代：Zlotta 2023（本篇的錨）**[C-S1]

- 設計：**回溯性、多中心（美加三家大學中心）、傾向分數配對（3:1 with replacement）＋逆機率加權**，**不是隨機試驗**。
- 族群：臨床期別 **T2–T4 N0 M0 肌肉侵犯型尿路上皮癌**，2005-01-01 至 2017-12-31，**n=722**（膀胱切除 440、三聯療法 282）。
- **收案的腫瘤條件（這就是「誰能被比較」的定義，必須跟數字一起寫）**：
  「All patients had **solitary tumours less than 7 cm, no or unilateral hydronephrosis, and no extensive or multifocal
  carcinoma in situ**.」——也就是兩條路都走得通的人。
- 配對後 n=1,119（RC 837、TMT 282）。配對變數包含年齡、性別、cT2 比例、水腎、有沒有接受術前或術後化療。
  配對後：年齡中位 71.4 vs 71.6 歲；cT2 90% vs 90%；有水腎 12% vs 10%；接受術前／術後化療 59% vs 56%。
- 中位追蹤 **4.38 年（RC）／4.88 年（TMT）**。
- **主要終點 5 年無轉移存活：74%（RC）vs 75%（TMT）**（IPTW）；配對法 74% vs 74%。無差異
  （IPTW SHR 0.89，95% CI 0.67–1.20，p=0.40；PSM SHR 0.93，0.71–1.24，p=0.64）。
- 5 年癌症專一存活 81% vs 84%（IPTW）／83% vs 85%（PSM），**無統計差異**（p=0.071／p=0.057）。
- 5 年無病存活 73% vs 74%／76% vs 76%，無差異。
- **總存活偏向三聯療法**：IPTW 66% vs 73%（HR 0.70，0.53–0.92，p=0.010）；PSM 72% vs 77%（HR 0.75，0.58–0.97，p=0.0078）。
- **挽救性膀胱切除 38 人（13%）。**
- **膀胱切除那 440 人的病理期別（這一段是誠實必列，見下）**：pT2 124 人（28%）、**pT3–4 194 人（44%）、
  淋巴結陽性 114 人（26%）**；中位取出淋巴結 39 顆；軟組織切緣陽性 1%（n=5）；**圍術期死亡率 2.5%（n=11）**。
- 作者自己的結論句（可直接引）：「This multi-institutional study provides **the best evidence to date** showing similar
  oncological outcomes between radical cystectomy and trimodality therapy **for select patients**…
  These results support that trimodality therapy, **in the setting of multidisciplinary shared decision making**,
  should be offered to all suitable candidates with muscle-invasive bladder cancer and **not only to patients with
  significant comorbidities for whom surgery is not an option**.」

**D. 配對世代的統合層級**

- Matsukawa 2025（Eur Urol Focus，**只收配對世代研究以減少選擇偏差**，87 篇、n=28,218）[C-S33]：
  **OS 無差異（HR 1.05，95% CI 0.78–1.40）、CSS 無差異（HR 1.05，0.69–1.58）**。
  三聯療法端：完全反應率 **74.4%（69.1–79.1）**、**膀胱內復發率 23.1%（19.0–27.7）**、急性 ≥3 級毒性 **11.4%（4.0–28.4）**。
  作者結論仍寫「**However, evidence from high-volume controlled trials is needed.**」
- Ditonno 2024（BJU Int，cT2–4 任何 N M0）[C-S35]：OS HR 1.07（0.81–1.4，p=0.6）；
  只看 ≥60 Gy 的放療方案 HR 1.02（0.69–1.52，p=0.9）；CSS HR 1.12（0.79–1.57）；MFS HR 0.88（0.66–1.16）。
  **三聯療法平均成本顯著較高（US$289,142 vs US$148,757，p<0.001）**，但每品質調整生命年成本較佳。

**E. 反方向的資料（誠實必列，這一節不得刪）**

1. **全國登記資料方向偏切除。** Cahn 2017（NCDB 2004–2013，AJCC II–III 期，n=32,300：RC 22,680、保留膀胱 9,620；
   其中根治劑量放療 2,540 人（26.4%）、同步化放療 1,489 人（15.5%））[C-S30]：
   每一組都是膀胱切除的總存活較好；隨著統計方法愈嚴格、保留膀胱的定義愈嚴格，差距縮小但沒有消失——
   多變項：任何放療 HR 2.115、根治劑量放療 HR 1.870、**同步化放療 HR 1.578（1.474–1.691）**；
   傾向分數：**同步化放療 HR 1.406（1.235–1.601）**。
2. **SEER 2010–2022（T2N0M0，n=10,495）**[C-S31]：配對後 **5 年 OS 膀胱切除 62.6% vs 三聯療法 36.7%（p<0.001）**。
   作者的結論句：「**The inferior survival of TMT in real-world practice underscores the critical importance of
   stringent patient selection for bladder preservation strategies.**」
3. **EAU 引用的系統性回顧（57 篇、n=30,293）**[C-S19]：10 年 OS 三聯療法 30.9% vs 膀胱切除 35.1%（p=0.32）；
   平均疾病專一存活 50.9% vs 57.8%（p=0.26）；**T2 的 10 年疾病專一存活 69%（TMT）vs 78.9%（RC）**；
   T3/T4 則 43.5% vs 43.1%。→ **在最早期的 T2 這一格，數字方向是偏切除的，只是差距未達顯著。**
4. **統計方法層面的反駁：Robesti 2025** [C-S34]（見上 ⚠ 第 4 點）：校正 informative censoring 後
   **5 年 OS 42%（RC）vs 30%（TMT），p<0.001**。
5. **三聯療法系列的病人本來就比較老。** EAU 2026：手術系列的年齡中位在 60 多歲中後段，**放療系列在 70 多歲中段**[C-S19]。
   RISC 國際世代（29 個學術中心，2005–2013，cT2–T4a N0M0）[C-S32]：265 位保留膀胱 vs 1,447 位膀胱切除，
   保留膀胱者**較老、體能狀態較差、共病較多（三項 p 皆 <0.01）**；用根治劑量放療者的中位總存活
   **41 個月 vs 46 個月（p=0.33）**。
6. **兩邊的比較永遠不對等：分期基礎不同。** Zlotta 的膀胱切除組拿到的是**病理**期別（44% 是 pT3–4、26% 淋巴結陽性），
   三聯療法組只有**臨床**期別，沒有人知道他們的真實期別[C-S1]。SPARE 的作者也點出同一件事：
   膀胱鏡下看起來正常的膀胱，實際上會被**低估期別**（understage）[C-S2]。

**F. 「不用開刀＝比較輕鬆」要被打掉的三根柱子**

1. **療程長度與急性毒性。** 同步化放療的標準劑量是 64 Gy／32 次／6.5 週或 55 Gy／20 次／4 週[C-S6][C-S19][C-S21]；
   RTOG 0712 的治療相關第 3–4 級毒性 **FCT 組 21/33（64%）、GD 組 18/33（55%）**，以血液學毒性為主（55%／42%）[C-S9]。
2. **一輩子的膀胱鏡追蹤。** 三個指引都沒有給停止點：EAU「每 3 個月照兩年、每 6 個月照到第五年、**之後每年一次**」[C-S19]；
   AUA「第一年每 3 個月、第二年每 4–6 個月、**之後每 6–12 個月**」[C-S20]；
   NICE「放療結束後 3 個月硬式膀胱鏡，之後每 3 個月照兩年、每 6 個月照兩年、**之後每年一次**」[C-S21]。詳見 C5。
3. **挽救性膀胱切除。** 約五分之一（見 ⚠ 第 5 點），而且它的併發症比第一次就開刀更重（見 C5）。

**G. 生活品質：唯一的比較資料是回溯性的**

Mak 2016（兩院、橫斷面、**回溯性**，226 位 cT2–cT4 非轉移、兩條路都適合、無病存活 ≥2 年者，回覆率 77%，n=173；
三聯療法 64 人、膀胱切除 109 人；中位追蹤 5.6 年；從診斷到填問卷中位 9 年（TMT）vs 7 年（RC），p=0.009）[C-S12]：
傾向分數校正後，三聯療法組的整體生活品質高 **9.7 分（滿分 100，p=0.001）**，
身體／角色／社會／情緒／認知功能高 6.6–9.9 分（p≤0.04），腸道功能好 4.5 分（p=0.02），
**性功能好 8.7–32.1 分（p≤0.02）、身體形象好 14.8 分（p<0.001）**，**排尿症狀分數兩組相似**。
作者結論：「**Both TMT and RC result in good long-term QOL outcomes** … **Whether TMT leads to superior QOL requires
prospective validation.**」EAU 2026 的評語同樣保守：「a retrospective study showed QoL to be good after TMT and in most
domains better than after cystectomy, **although prospective validations are needed**」[C-S19]。

### Claim ceiling（硬上限）

**可寫：**
- 「**膀胱全切除對現代三聯療法，沒有完成的隨機試驗**」——並引 EAU 原文那一句。
- 「一個 1980 年代的隨機試驗比較過『術前放療＋切除』與『放療＋需要時再切』，看不出存活差別，但那不是今天的三聯療法」。
- 「唯一一個現代的隨機試驗（SPARE）因為收不到人在 2010 年關掉；作者寫的原因是病人與醫師都有強烈偏好、不願意讓抽籤決定」。
- 「在**腫瘤條件兩條路都走得通**的人身上（單一腫瘤 <7 公分、沒有或只有單側水腎、沒有廣泛或多發 CIS），
  最好的配對世代看不出無轉移存活、癌症專一存活、無病存活的差別」——**每次都要帶這串條件**。
- 「同一份資料裡，總存活偏向三聯療法（HR 0.70），但那是回溯性配對，不是隨機」。
- 「全國登記資料的方向是反過來的，偏向切除」——並寫出為什麼（病人條件不同、資料庫看不到腫瘤條件）。
- 「約每五個人有一個，最後還是要切掉膀胱」。
- 「三聯療法的生活品質在回溯性比較裡多數面向較好，但那是回溯性的，作者自己說需要前瞻驗證」。

**不可寫：**
- 「保留膀胱＝次等選擇」。
- 「保留膀胱＝一樣好」「效果相同」「沒有差別」——**只能寫「在這一群被挑過的病人裡，這些研究看不出差別」**，
  且必須標明配對世代不是隨機試驗。
- 「不用開刀＝比較輕鬆」。
- 任何**不帶選人條件**的「兩條路一樣」——EAU 引的系統性回顧在 T2 這一格，10 年疾病專一存活是 69% vs 78.9%。
- 把「總存活偏向三聯療法（HR 0.70）」寫成「保留膀胱活得比較久」——那是回溯性資料裡的非癌症死因差異最可能的解釋，
  作者自己沒有這樣宣稱。
- 把台灣的使用率寫成任何數字（沒有）。
- 任何讓讀者自己判斷該走哪一條的句子。**本篇給的是要問醫師的問題清單與選擇條件。**

### Caveats／safety notes（寫作者必寫）

- **利益揭露逐字放在第一個 h4 之前**（SPEC §二）。
- 每一個比較都要標：研究設計（隨機／配對／登記）、族群（cT2–T4 N0M0 肌肉侵犯型尿路上皮癌）、n、追蹤時間、
  **以及三聯療法那一組是不是被挑過的**。
- 分期不對等這件事要寫進去：切除的人拿到病理期別，保留的人只有臨床期別。
- 兩條路的比較**只在本篇做**（SPEC §六）；C2、C3、C4、C5 不得自行比較療效。
- 非肌肉侵犯型的數字一律不得進本篇。

### 台灣端

- **兩條路的每一個構件健保都有給付項目**（見 C3、C4 的逐條），但**「膀胱癌」三個字在支付標準全文檔裡零筆**[C-S39]——
  也就是沒有任何以膀胱癌為適應症的獨立給付項目。可寫「兩條路的構件都在給付範圍內，
  但要問醫務課／個管師實際申報與事前審查怎麼走」，**不可推論有沒有給付某個特定療程**。
- **台灣三聯療法使用率：查不到（gap）。** 路徑：hpa.gov.tw TLS 失敗；
  data.gov.tw dataset 6399「癌症發生統計」的下載連結指向 hpa.gov.tw，同樣 TLS 失敗（FAIL-4）。
- **重大傷病項次：本組未取得逐字條文（gap）**，law.moj.gov.tw 三個候選 PCode 都不是該辦法。交由 A 組或寫成「問醫務課」。

### 給繪圖組的數字（`fig-bl-two-roads`）

兩欄對照，每一格帶研究設計／族群／n／追蹤：
- 同框最上方必須標：**「沒有完成的隨機試驗（比較膀胱全切除與現代三聯療法）」**[C-S19]
- 配對世代欄（Zlotta 2023，回溯性配對，cT2–T4N0M0、單一腫瘤 <7cm、無／單側水腎、無廣泛 CIS，n=722，中位追蹤 4.4／4.9 年）：
  5 年無轉移存活 74% vs 75%；5 年癌症專一存活 83% vs 85%（PSM）；挽救性切除 13%
- 登記資料欄（NCDB 2004–2013，n=32,300，配對後）：同步化放療 vs 切除 死亡 HR 1.406
- 登記資料欄（SEER 2010–2022，T2N0M0，n=10,495，配對後）：5 年 OS 62.6% vs 36.7%
- 代價欄：膀胱切除 90 天死亡率 3.4–8.0%[C-S19]／4.7%（彙總）[C-S17]；三聯療法急性 ≥3 級毒性 11.4%[C-S33]
- 追蹤欄：三聯療法後膀胱鏡「沒有停止點」[C-S19][C-S20][C-S21]
- **不可**畫成「哪一條比較好」的結論圖。

---

## C2 `bl-neoadjuvant`〈開刀前先化療，為什麼是標準〉

### Key facts

**A. 術前含鉑化療的隨機證據（三層）**

1. **SWOG 8710（Grossman 2003，NEJM）**[C-S22]：T2–T4a 肌肉侵犯型，11 年收了 317 人、307 人可評估
   （單獨手術 154、MVAC×3 後手術 153）。意圖治療分析：中位存活 **46 個月 vs 77 個月（p=0.06，雙側分層 log-rank，
   未達傳統顯著水準）**。**手術檢體看不到殘餘癌的比例 38% vs 15%（p<0.001）。**
2. **BA06 30894（國際合作，JCO 2011 長期結果）**[C-S24]：1989–1995 收 **976 人**，中位追蹤 8.0 年。
   CMV×3 對不給。**死亡風險降低 16%（HR 0.84，95% CI 0.72–0.99，p=0.037），
   相當於 10 年存活從 30% 升到 36%。** 注意：這個試驗的局部治療是**膀胱切除和／或放療**，由醫師選擇。
3. **ABC 個別病人資料統合分析（2005 更新版，Eur Urol）**[C-S23]：**11 個試驗、3,005 人**（涵蓋已知合格試驗 98% 的病人）。
   **含鉑複方化療的存活益處 HR 0.86（95% CI 0.77–0.95，p=0.003），等於 5 年絕對存活提高 5%；
   無病存活 HR 0.78（0.71–0.86，p<0.0001），等於 5 年絕對提高 9%。**
   → **這就是「絕對益處有多大」那個數字：5 年 5 個百分點。**
4. EAU 2026 的證據摘要寫法（可直接引）：「Neoadjuvant cisplatin-containing combination chemotherapy improves OS
   (**8% at five years**). LE 1a」[C-S19]。**→ 5% 與 8% 是兩個不同來源的數字**（ABC 2005 vs EAU 2026 引的較新版），
   正文要嘛引 ABC 原文的 5%（帶年份與 n），要嘛引 EAU 的 8%（帶「指引寫的」），**不可把兩個混寫成一個範圍**。

**B. ddMVAC 對 gemcitabine–cisplatin：VESPER**

VESPER（GETUG-AFU V05，法國 28 家中心，開放標籤隨機第 3 期，2013-02-25 至 2018-03-01，n=500，
最終意圖治療 **493**：GC 245、ddMVAC 248；**437 人（89%）是術前給**）[C-S25]：
- **主要終點是 3 年無惡化存活**（本論文報的是 5 年次要終點）。中位追蹤 5.3 年，190 例死亡。
- **整個圍術期族群：5 年總存活 64%（ddMVAC）vs 56%（GC），HR 0.79（95% CI 0.59–1.05）——未達顯著。**
- **術前次族群：5 年總存活 66% vs 57%，HR 0.71（0.52–0.97）——達顯著；
  5 年膀胱癌死亡累積發生率 24% vs 38%，HR 0.55（0.39–0.78）。**
- 作者結論：「We found no evidence of improved overall survival with dd-MVAC over GC in the perioperative setting,
  **but the data support the use of six cycles of dd-MVAC over four cycles of GC in the neoadjuvant setting.**」
- **誠實必列的標籤**：VESPER 用的是 **6 個療程的 ddMVAC**，超過臨床上常用的 4 個療程，
  這會影響毒性與外推性（Ther Adv Urol 2026 回顧明寫這一點）[C-S29]。

**C. 誰是「不適合 cisplatin」——Galsky 準則（逐字）**

Galsky 2011 的共識定義（Lancet Oncol 2011;12:211–214）**本身在 Europe PMC 沒有摘要也拿不到全文（見 [C-F1]，書目可引、內容不可引）**。
可引的逐字轉述有兩個 OA 來源：

- Ther Adv Urol 2026（OA 全文）[C-S29]：「**The Galsky criteria define cisplatin ineligibility as the presence of any
  of the following: ECOG performance status ≥2, creatinine clearance <60 mL/min, hearing loss (≥grade 2),
  peripheral neuropathy (≥grade 2), or New York Heart Association class III heart failure.**」
- Investig Clin Urol 2025（OA 全文）[C-S42]：「The panel's recommended criteria include: (1) ECOG performance status of 2,
  and/or (2) creatinine clearance <60 mL/min, and/or (3) Common Terminology Criteria for Adverse Events (CTCAE)
  grade ≥2 hearing impairment, and/or (4) CTCAE grade ≥2 peripheral neuropathy.」
  並說明來源：由泌尿腫瘤內科醫師小組回顧文獻、向 120 位國際內科腫瘤醫師徵詢、**回收 65 份**後形成的共識定義。
  同一篇也寫：「**The definition of cisplatin ineligibility, which is often based on the Galsky criteria,
  lacks robust scientific validation**」。

**→ 寫法**：五條逐條寫（引 [C-S29] 的完整五條），並寫明「這是 2011 年一份**專家共識**、是 65 份問卷的結果，
不是試驗驗證出來的門檻，文獻裡至今有人質疑它」。
**約一半的肌肉侵犯型病人不適合 cisplatin**（Ther Adv Urol 2026：「up to 50%」[C-S29]；
Investig Clin Urol 2025：「nearly 50%」[C-S42]）。

EAU 2026 對腎功能的實際門檻（可並陳，措辭不同）：圍術期化學免疫治療的建議條件寫成
「eligible for cisplatin-based chemotherapy (**glomerular filtration rate ≥ 40mL/min. allowed**)」[C-S19]；
腎功能在 eGFR 40–60 mL/min 的人，臨床上有**分次給藥（split-dose cisplatin）**的做法[C-S29]。
**EAU 的強建議：「Do not offer neoadjuvant carboplatin-containing combination chemotherapy to patients who are
ineligible for cisplatin-based combination chemotherapy.」**[C-S19]——carboplatin 不是 cisplatin 的替身。

**D. 圍術期免疫治療：兩個試驗，兩個族群**

1. **NIAGARA（Powles 2024，NEJM 391:1773–1786）**[C-S26]——**適合 cisplatin 的人**：
   第 3 期開放標籤，**n=1,063**（durvalumab 組 533、對照 530）。術前 durvalumab＋GC×4 →膀胱切除→術後 durvalumab×8
   對 術前 GC×4 →膀胱切除。
   **24 個月無事件存活 67.8% vs 59.8%（HR 0.68，95% CI 0.56–0.82，p<0.001）；
   24 個月總存活 82.2% vs 75.2%（HR 0.75，0.59–0.93，p=0.01）。**
   第 3–4 級治療相關不良事件 40.6% vs 40.9%；治療相關死亡各 0.6%。**接受膀胱切除者 88.0% vs 83.2%。**
2. **EV-303／KEYNOTE-905（Vulsteke 2026，NEJM 394:1257–1269）**[C-S27]——**不適合或拒絕 cisplatin 的人**：
   第 3 期開放標籤，**n=344**（EV＋pembrolizumab 170、單純手術 174）。中位追蹤 25.6 個月。
   **2 年無事件存活 74.7% vs 39.4%（HR 0.40，0.28–0.57，p<0.001）；
   2 年總存活 79.7% vs 63.1%（HR 0.50，0.33–0.74，p<0.001）；
   病理完全反應 57.1% vs 8.6%（差 48.3 個百分點）。**
   接受手術者 87.6% vs 89.7%。**不良事件：EV＋pembro 組 100% 發生任何不良事件，≥3 級 71.3%、
   ≥3 級藥物相關 45.5%；對照組 64.8% 發生不良事件、≥3 級 45.9%。**
   → 注意對照組是**單純手術、不給任何術前治療**，因為這是 cisplatin 不適用的族群。

EAU 2026 的建議措辭（可直接引，兩條並列）[C-S19]：
- 「**Offer perioperative chemoimmunotherapy with cisplatin/gemcitabine and durvalumab** to patients with muscle-invasive
  bladder cancer (MIBC) (T2-T4a, cN0-1 M0) who are eligible for cisplatin-based chemotherapy (glomerular filtration rate
  ≥ 40mL/min. allowed) and immunotherapy. **Strong**」
- 「**Offer perioperative enfortumab vedotin plus pembrolizumab** to patients with MIBC who are ineligible for
  cisplatin-based chemotherapy. **Strong**」
- 「**Offer neoadjuvant cisplatin-based combination chemotherapy** to patients with MIBC (T2-T4a, cN0-1 M0) who are
  eligible for cisplatin-based chemotherapy. **Strong**」

**E. 站上既有文章 `insight-bladder-ev-pembro`：可以指向什麼、不可以重寫什麼**

該文（現行標題〈三十年沒變的流程，今年動了〉）寫的是 **KEYNOTE-B15／EV-304，也就是「適合 cisplatin」那一格**：
n=808，2 年無事件存活 79.4% vs 66.2%，2 年總存活 86.9% vs 81.3%，病理完全反應 55.8% vs 32.5%，
≥3 級不良事件 75.7% vs 67.2%，因副作用中途停藥 35.2% vs 11.1%；並引 2026-07-10 的 FDA 核准。
我已獨立核對該試驗的原始文獻：Galsky 2026, NEJM 395:338–348，**摘要數字與站上所寫一致**[C-S41]
（n=405 vs 403 共 808；中位追蹤 33.6 個月；EFS HR 0.53，0.41–0.70；OS HR 0.65，0.48–0.89；pCR 55.8% vs 32.5%；
≥3 級不良事件 75.7% vs 67.2%）。**站上那篇沒有寫到停藥率的原始出處欄位——它引的是 ASCO Post 轉述**；
NEJM 摘要裡**看不到** 35.2%／11.1% 這兩個數字，所以 **C2 不得重述停藥率**（見 FAIL-9）。

**→ C2 的安全寫法**：
- 「適合 cisplatin 的人，術前術後改用 EV＋pembrolizumab 這件事，站上已經寫過一篇，
  用它現行標題〈三十年沒變的流程，今年動了〉指路，**一句帶過，不重述數字**。」
- C2 自己寫的是：**古典的術前含鉑化療為什麼是標準（ABC／BA06／SWOG 8710）**、
  **ddMVAC 對 GC（VESPER）**、**誰不適合 cisplatin（Galsky 五條）**、
  **以及 cisplatin 不適用那一格的新證據（EV-303／KEYNOTE-905）與適合 cisplatin 那一格的 NIAGARA**。

### 反方向的資料（誠實必列）

- 術前化療的絕對益處**是 5 個百分點（5 年）**，不是「顯著延長存活」的大字。ABC 的 HR 0.86 與 BA06 的 HR 0.84
  都貼近 1，BA06 的 p=0.037[C-S23][C-S24]。
- SWOG 8710 的**主要存活比較 p=0.06，沒有達到傳統顯著水準**[C-S22]——不可寫成「隨機試驗證明存活延長 31 個月」。
- 真實世界的術前化療使用率低：Osanto 2020 回顧寫「real-world adherence to NAC is low as ~40-50% of patients are
  unfit for cisplatin」[C-S44]。
- VESPER 整個圍術期族群的總存活**沒有達顯著**（HR 0.79，0.59–1.05）；只有術前次族群達顯著[C-S25]。
- NIAGARA 與 EV-303 的追蹤都只有 2 年多（NIAGARA 主要報 24 個月；EV-303 中位 25.6 個月）[C-S26][C-S27]。
- EV＋pembrolizumab 的代價很實在：EV-303 的 ≥3 級藥物相關不良事件 45.5%[C-S27]。

### Claim ceiling

**可寫**：「術前含鉑化療是標準，因為 11 個隨機試驗 3,005 人的個別病人資料統合分析顯示 5 年絕對存活提高 5 個百分點」；
「BA06 976 人的長期結果是 10 年存活從 30% 升到 36%」；「手術檢體看不到殘餘癌的比例從 15% 升到 38%」；
「6 個療程的 ddMVAC 在術前這一格的 5 年總存活優於 4 個療程的 GC（66% vs 57%），但整個圍術期族群沒有達顯著」；
「Galsky 的五條（逐條），以及它是 2011 年的專家共識、不是驗證出來的門檻」；
「約一半的病人用不了 cisplatin」；「carboplatin 不是 cisplatin 的替身（引 EAU 的強建議原文）」；
NIAGARA 與 EV-303 的數字（帶試驗名、族群、n、終點、追蹤長度）。

**不可寫**：把 SWOG 8710 的中位存活差寫成證明（p=0.06）；把 5% 與 8% 混成一個範圍；
把 ddMVAC 寫成「比較好的化療」而不標 6 vs 4 個療程與整體未達顯著；
把 Galsky 準則寫成讀者可以自己打勾的表（紅線 3 的精神在這裡同樣適用）；
重述站上 EV-pembro 那篇的停藥率數字（原始摘要看不到）；
把免疫治療的無事件存活寫成治癒率。

### 台灣端

- **健保藥品給付規定的逐字條文本組未查（屬 D 組範圍）。** 站上既有文章〈三十年沒變的流程，今年動了〉
  寫「健保給付 enfortumab vedotin 仍限於局部晚期或轉移性尿路上皮癌，術前後這個用法尚未納入」，
  **本組未獨立核對該條文**（nhi.gov.tw HTML 403，見 FAIL-5）。**C2 若要寫給付，必須等 D 組的逐字條文，
  或寫「查不到列項，問醫務課／個管師」，永不推論。**
- 化學治療注射的健保項目存在（37038B 靜脈血管內化學藥物注射一小時內 1,031 點、37039B 一至四小時 1,234 點，
  註「藥費另計」）[C-S39]——可寫「施打的處置有給付項目，藥費另計」，不可推論特定藥物有沒有給付。

---

## C3 `bl-cystectomy`〈膀胱切除與尿路改道：三種做法的日子〉【紅線 6，雙向】

### Key facts

**A. 這個手術為什麼是標準治療（紅線 6 反方向那一半，要先寫）**

- EAU 2026 的建議原文：「**Offer radical cystectomy to patients with T2-T4a N0M0 disease. Strong**」[C-S19]；
  適應症還包含極高風險非肌肉侵犯型、卡介苗無效等（那一格歸 B 組）。
- 為什麼要切乾淨：**單靠膀胱切除，五年存活約 50%**（EAU 2026：「RC only provides five-year survival in about 50% of
  patients」）[C-S19]——這句同時解釋了為什麼要加術前化療（C2）。
- 拖不得：19 篇研究的統合分析顯示**延遲超過三個月對總存活有負面影響（HR 1.34，95% CI 1.18–1.53）**[C-S19]。
- 手術品質的兩個硬數字（Zlotta 的膀胱切除組，n=440）[C-S1]：中位取出淋巴結 **39 顆**、軟組織切緣陽性 **1%（n=5）**。

**B. 90 天併發症、死亡率、再住院率（全部帶分母與世代型態）**

| 數字 | 來源與世代 |
|---|---|
| **90 天併發症 58.5%（範圍 36.1–80.5）**；30 天 39.0%（27.3–80.0）；住院期間 34.9%（28.8–68.8） | Maibom 2021 系統性回顧，66 篇、**全部是回溯性、沒有隨機試驗**，證據品質「poor to good」[C-S17] |
| **90 天死亡率 4.7%（範圍 0.0–7.0）**；30 天 2.1%（0.0–3.7）；住院期間 2.4%（0.9–4.7） | 同上[C-S17] |
| 30 天死亡 **2.1–3.2%**；**90 天死亡 3.4–8.0%** | EAU 2026 引四篇回溯研究＋一篇人口基礎世代[C-S19] |
| Clavien-Dindo 併發症 **50–88%（I–IV）**、**嚴重併發症（≥III）30–42%** | EAU 2026[C-S19] |
| **再住院率約 25%（出院後 30 天內）** | EAU 2026 引大型全國資料庫與機構系列[C-S19] |
| 30 天死亡 **2.2%（208/9,287）**、**90 天死亡 5.6%（518/9,287）** | Richters 2021，荷蘭癌症登記 2008–2018 全國世代，n=9,287（OA）[C-S18] |
| **90 天死亡 7%（19/292，擴大淋巴廓清）vs 2%（7/300，標準廓清）**；第 3–5 級不良事件 54% vs 44% | **SWOG S1011，隨機試驗**，cT2–T4a、≤2 顆陽性淋巴結，658 人入組、**592 人隨機**，36 位外科醫師、27 個中心，中位追蹤 6.1 年[C-S43] |
| 圍術期死亡率 **2.5%（11/440）** | Zlotta 2023 的膀胱切除世代（大學中心、被挑過的族群）[C-S1] |

**→ 寫法**：這串數字的範圍非常寬（90 天死亡 2.5% 到 8%），**原因就是世代型態不同**：
大學中心被挑過的族群在低端，全國登記在中段，隨機試驗裡做擴大淋巴廓清的在高端。**範圍與原因要同段寫。**

**C. 擴大淋巴廓清沒有比較好（隨機證據，寫「不是切得愈多愈好」）**

SWOG S1011[C-S43]：擴大廓清（切到總髂、坐骨前、薦骨前）對標準廓清，**5 年無病存活 56% vs 60%（HR 1.10，0.86–1.40，p=0.45）、
5 年總存活 59% vs 63%（HR 1.13，0.88–1.45）**，**併發症與死亡率反而較高**。
作者結論：「extended lymphadenectomy **did not result in improved** disease-free or overall survival … and **was
associated with higher perioperative morbidity and mortality**」。

**D. 三種尿路改道：日子長什麼樣（三種都不得寫成有高下）**

**指引自己的兩句話，先引，它們就是「不畫高下」的授權**[C-S19]：
- 「**Randomised controlled trials comparing conduit diversion with neobladder or continent cutaneous diversion
  have not been performed.**」
- 「**Currently, it is not possible to recommend a particular type of urinary diversion.** However, based on clinical
  experience, most institutions prefer ileal orthotopic neobladders and ileal conduits. In select patients, such as
  patients with a single kidney, ureterocutaneostomy is surgically the simplest.」
- NICE 的措辭（並陳用）[C-S21]：「Offer adults who have chosen radical cystectomy **a urinary stoma, or a continent
  urinary diversion** (bladder substitution or a catheterisable reservoir) **if there are no strong contraindications
  to continent urinary diversion such as cognitive impairment, impaired renal function or significant bowel disease**.」

**① 迴腸導管（ileal conduit，肚皮上的造口＋尿袋）**[C-S19]
- 「an established option with **well-known/predictable results**」。
- **早期（30 天）併發症 48%**：泌尿道感染、腎盂腎炎、輸尿管—迴腸接合處漏與狹窄。
- 長期：**造口相關併發症最高到 24%**、**上泌尿道功能或形態變化最高到 30%**；
  與禁尿型腹腔內貯尿囊或原位新膀胱相比，**迴腸導管的晚期併發症較少**。

**② 原位新膀胱（orthotopic neobladder，接回尿道，用腹壓＋放鬆括約肌排尿）**[C-S19]
- 使用率：荷蘭、德國、西班牙的膀胱癌登記資料顯示，男女各約 **10–20%** 的病人做這個。
- **早期與晚期併發症最高到 22%**；EAU 表 6.3 的標題寫「Management of neobladder morbidity (**30-64%**)」，
  其中接合處狹窄 7%。
- **連續性（男性，前瞻性評估）**[C-S19]：**日間禁尿從術後 3 個月內的 59% 升到 12–18 個月時的 92%；
  夜間禁尿從 28% 升到 18–36 個月時的 51%。**
- **女性**（56 位新膀胱病人）：**日間禁尿 70.4%、夜間 64.8%；排空困難在女性特別常見——
  約三分之二需要自行導尿、將近 45% 完全無法自行排尿。** 保留雙側自律神經可把導尿需求降到 3.4–18.7%（66 位女性）。
- 尿道復發：合併估計 **4.6%**（範圍 0.8–13.7%，男性明顯較高）；**新膀胱不會犧牲腫瘤控制**
  （校正病理期別後癌症專一存活與迴腸導管無差異）。
- 禁忌：尿道有侵犯性腫瘤（EAU 強建議不做）；相對禁忌為高劑量術前放療、複雜尿道狹窄、嚴重括約肌型失禁。
  年齡 >80 歲常被當門檻，但 EAU 明寫「there is **no exact age for a strict contraindication**」。

**③ 輸尿管皮膚吻合（ureterocutaneostomy，輸尿管直接接到肚皮）**[C-S19]
- 「the **simplest** form of cutaneous diversion」。
- 相對迴腸導管：**手術時間、併發症率、失血、輸血率、加護病房停留與住院天數都較低**。
- 代價：**輸尿管口徑較小，造口狹窄與上行性泌尿道感染的發生率高於用小腸或大腸做的腸道造口。**
- 適應對象：**體弱者、或只有一顆腎而需要上尿路改道者，是首選做法。**

**④ 禁尿型皮膚改道與輸尿管乙狀結腸吻合**[C-S19]：「nowadays … **rarely used** because of high complication rates」
（造口狹窄與失禁；輸尿管乙狀結腸吻合則是上尿路感染與結石）。

**E. 選改道的過程比選哪一種更重要（可直接引，紅線 6 的核心）**[C-S19]
- 「Ensuring that patients make a well-informed decision about the type of urinary diversion is associated with
  **less decision regret postoperatively, independent of the method selected**.」
- 證據摘要：「Ensuring that patients are well informed about the various urinary diversion options prior to making a
  decision may help prevent or reduce decision regret, **independent of the method of diversion selected**. LE 3」
- 「**The type of urinary diversion does not affect oncological outcome. LE 3**」
- NICE：造口護理師要在手術前後都能談[C-S21]。

**F. 腎功能與代謝：長期的帳**

- **迴腸導管與原位新膀胱在腎絲球過濾率下降的風險上沒有顯著差異**（回溯性，n=1,383，術前慢性腎病第 2 期
  eGFR 60–89 或 3a 期 45–59 者）；**只有年齡與接合處狹窄與 eGFR 下降相關**[C-S19]。
- **3,360 位因肌肉侵犯型膀胱癌接受膀胱切除者，29% 在 12 個月內進展到晚期慢性腎病**[C-S19]。
- 良性輸尿管—腸道接合處狹窄**最高 20%**；腸道改道者**維生素 B12 偏低 17%**（EAU 建議每年驗一次）；
  SEER 資料顯示膀胱切除與**骨折風險上升 21%** 相關（慢性代謝性酸中毒與長期骨質流失）[C-S19]。
- 改道相關併發症在追蹤**前五年偵測到 45%**；131 人的系列裡，**存活超過 15 年者升到 94%**；
  15 年追蹤時 **50% 出現上泌尿道變化、38% 出現尿路結石**[C-S19]。
- 迴腸皮膚改道的單側／雙側輸尿管皮膚吻合各有健保項目（見台灣端）。

**G. 性功能**[C-S19]

- **傳統膀胱切除**：男性標準術式切除膀胱、攝護腺、儲精囊、遠端輸尿管與區域淋巴結；
  女性歷史上的標準術式切除膀胱、**整段尿道、鄰接陰道、子宮、遠端輸尿管與區域淋巴結**，
  「Pelvic floor disorders, along with sexual and voiding dysfunction in female patients are **prevalent** after RC」。
  EAU 要求術前問婦科病史並告知對性功能與陰道脫垂的潛在負面影響。
- **保留性功能術式（12 篇、n=1,098，多為開放手術＋原位新膀胱；9 篇中位追蹤 >3 年、3 篇 >5 年；
  多數收的是術前有性功能、器官侷限、膀胱頸與攝護腺尿道無侵犯者）**：
  術後性功能（potency）**顯著高於傳統術式（p<0.05）**：保留攝護腺 80–90%、保留攝護腺被膜 50–100%、
  保留神經血管束 29–78%。**腫瘤結果在所有有比較的研究中沒有差別。**
  保留攝護腺者的禁尿（定義為不用護墊）：**日間 88–100%、夜間 31–96%**。
  **證據摘要明寫：「None of the sexual-preserving techniques … have shown to be superior, and no particular technique
  can be recommended. LE 3」**；建議只提供給**高度希望保留性功能且經過篩選**的男性。
- 1991 年的隨機試驗裡，**所有接受膀胱切除的男性都出現勃起功能喪失**[C-S36]——年代久遠，當標尺不當現況。

**H. 手術量與結果的關係**[C-S19][C-S18]

- EAU 2026 的建議：「**Perform at least 20 radical cystectomies (RCs) per hospital/per year. Strong**」。
- EAU 的敘述：「lower morbidity and (perioperative) mortality have been observed by surgeons and in hospitals with a
  higher case load」；瑞典全國資料（**n=4,638**）顯示把膀胱切除從 24 家集中到 10 家後，**90 天死亡率與再手術率顯著下降**，
  但**被提供手術的病人平均年齡與共病也隨之上升**。
- **反過來的細節（誠實必列）**：Richters 2021（荷蘭全國，n=9,287，中位年手術量 19 例，範圍 1–75）[C-S18]
  在校正年齡、TNM 期別與術前治療後發現，**術後死亡風險在年手術量 0 到 25 例之間其實略為上升，
  從 30 例起才穩定下降**，最低風險出現在手術量最高的醫院。作者的結論句是
  「the volume criterion of 20 RCs annually, as recently recommended by the European Association of Urology Guideline
  Panel, **might therefore be reconsidered**」。
- **SPEC §一.5：不寫任何院內配置、不點名醫院。** 手術量這一段只能寫成「國際指引與全國資料顯示手術量與結果有關」，
  以及「這是可以問你的主治醫師的問題之一」，**不得寫成任何醫院的評比或暗示**。

**I. 加速術後康復（ERAS）與血栓預防**[C-S19]

- ERAS：不做術前腸道準備、不禁食；術後強調減少嗎啡類止痛。**ERAS 組的疼痛評分反而較高
  （VAS 3.1 vs 1.1，p<0.001），但術後腸阻塞從 22% 降到 7.3%（p=0.003）。**
- EAU 強建議：「**Offer pharmacological venous thromboembolism prophylaxis, such as low-molecular-weight heparin,
  to RC patients, starting the first day post-surgery for a period of at least four weeks.**」
- 安大略癌症登記（n=4,205，其中 1,084 人接受術前化療）：**術前化療者的靜脈血栓栓塞率較高（12% vs 8%，p=0.002）。**

### 反方向的資料（誠實必列）

- 上面每一個「代價」數字都要配一句「這個手術為什麼仍是 T2–T4a N0M0 的標準治療」（EAU 強建議原文）。
- 90 天死亡率的範圍（2.5–8%）**不是因為手術愈來愈危險**，而是世代不同：大學中心被挑過的族群 2.5%[C-S1]，
  全國登記 5.6%[C-S18]，隨機試驗裡做擴大廓清的 7%[C-S43]。
- 迴腸導管**晚期併發症最少**[C-S19]——不要因為它「最不像原本的膀胱」就寫成次等。
- 輸尿管皮膚吻合在體弱者與單腎者是**首選**[C-S19]——不要因為它「最簡單」就寫成將就。
- 原位新膀胱的夜間禁尿，男性在 18–36 個月時只有 51%[C-S19]——不要因為它「最像原本的膀胱」就寫成最好。

### Claim ceiling

**可寫**：上表所有數字，**每一個都帶分母與世代型態**；三種改道各自的優點與代價（引 EAU 原文）；
「沒有任何比較三種改道的隨機試驗」「目前無法建議哪一種改道」（引原文）；
「把選擇過程做好，比選到哪一種更能減少事後的後悔——而且與選了哪一種無關」；
「擴大淋巴廓清在隨機試驗裡沒有比較好，併發症與死亡率反而比較高」；
「手術量與結果有關，國際指引的門檻是每年至少 20 例，而荷蘭全國資料認為這個門檻可能該再提高」。

**不可寫**：任何一種改道比另一種好；把併發症數字寫成勸退（同段必須有「為什麼這是標準治療」）；
把任何一個數字寫成「膀胱癌手術的死亡率是 X%」而不標世代；點名任何醫院或暗示院內量能（SPEC §一.5、§四固定紅線）；
把手術步驟寫進去（SPEC §一.6 ②）；用非肌肉侵犯型的資料。

### 台灣端（逐字，全部出自健保署官方檔）[C-S39]

以下為「全民健康保險醫療服務給付項目及支付標準」現行給付項目檔（政府資料開放平臺 dataset 174451 指向之
健保署 API 檔，2026-09-13 下載）中的逐字項目與點數：

| 代碼 | 中文項目名稱 | 點數 | 生效起日 |
|---|---|---|---|
| 78011B | 膀胱全切除術 | 13,799 | 2020-01-01 |
| 78013B | 膀胱全切除術合併骨盆腔淋巴切除術 | 21,450 | 2020-01-01 |
| 78012B | 膀胱全切除術合併原位新膀胱重建術 | 27,464 | 2020-01-01 |
| 78014B | 膀胱全切除術及骨盆腔淋巴切除術合併原位新膀胱重建術 | 34,992 | 2020-01-01 |
| 78041B | 膀胱攝護腺根除術合併原位新膀胱重建術 | 28,778 | 2020-01-01 |
| 78045B | 膀胱攝護腺根除術及骨盆腔淋巴切除術合併原位新膀胱重建術 | 35,531 | 2020-01-01 |
| 78046B | 膀胱全切除術及骨盆腔淋巴切除術及尿道全切除術合併禁尿膀胱重建術 | 60,063 | 2017-10-01 |
| 77032B | 輸尿管迴腸經皮分流術（單側） | 12,960 | 2020-01-01 |
| 77033B | 輸尿管迴腸經皮分流術（雙側） | 17,040 | 2020-01-01 |
| 77018B | 輸尿管皮膚吻合術－單側 | 8,231 | 2020-01-01 |
| 77019B | 輸尿管皮膚吻合術－雙側 | 10,148 | 2020-01-01 |
| 78050B | 腹腔鏡膀胱全切除術合併骨盆腔淋巴切除術合併正位新膀胱重建 | 65,785 | 2025-05-01 |
| 78051B | 腹腔鏡膀胱全切除術及骨盆腔淋巴切除術合併雙側輸尿管迴腸經皮分流術 | 65,785 | 2025-05-01 |
| 49022B | 迴腸膀胱永久裝具裝置 | 282 | 2020-01-01 |
| 49021B | 迴腸造口永久裝具裝置 | 235 | — |

**78050B／78051B 的備註逐字**（與機械手臂輔助手術有關，涉及可及性，寫法要小心）：
「執行『機械手臂輔助膀胱全切除術……』，須符合下列規範：1.醫師資格：(1)具機械手臂輔助手術系統『泌尿科』認證學會認證醫師資格。
(2)前述核發認證單位應檢附認證計畫書（須檢附訓練課程、認證方式及認證培訓機構證明）予保險人審核通過。
2.執行手術之醫師名單應報經保險人核定。3.其手術費按保險人規範之未列項申報方式辦理，比照本項申報……」
**→ 可寫的只有：三種改道在健保裡都有獨立的給付項目；機械手臂輔助的做法對執行醫師有認證與報備規範。
不可寫任何醫院有沒有、不可寫自費金額（SPEC §一.5）。**

**gap（要寫成「查不到列項，問醫務課／個管師」）：**
- **造口用品（尿袋、底座等耗材）的補助**：支付標準全文檔搜尋「造口」得 48 筆，但全部是**處置項目**
  （如 49021B 迴腸造口永久裝具裝置 235 點、49024B 人工肛門造口袋置換術 95 點、56004C 換造口器 210 點），
  **沒有任何耗材補助項目**；搜尋「尿袋」僅 2 筆（47013C 一般導尿、47014C 留置導尿），均非補助。
  → 寫「健保支付標準裡我查不到造口耗材的補助列項，這要問醫務課或個管師」，**永不推論有沒有補助**。
- **身心障礙鑑定與輔具補助**：屬社政系統（非健保支付標準），本組未取得逐字條文。
- **重大傷病項次逐字條文**：本組未取得（見 C1 台灣端）。

### 給繪圖組的數字（`fig-bl-diversion`）

三欄並列，**不畫高下、不排順序、不打勾**：
- 迴腸導管：30 天併發症 48%；長期造口併發症 ≤24%；上泌尿道變化 ≤30%；**晚期併發症在三者中最少**[C-S19]
- 原位新膀胱：使用率 10–20%；併發症 30–64%（EAU 表 6.3 標題）；男性日間禁尿 59%→92%（3 個月→12–18 個月）、
  夜間 28%→51%（3 個月→18–36 個月）；女性日間 70.4%／夜間 64.8%、約 2/3 需自行導尿[C-S19]
- 輸尿管皮膚吻合：手術時間／失血／輸血／加護病房／住院天數皆較低；造口狹窄與上行感染較多；
  體弱者與單腎者的首選[C-S19]
- 三欄共用的底線字：「**沒有任何比較三種改道的隨機試驗；目前無法建議哪一種**」[C-S19]
- 另一張可用：90 天死亡率的四個世代點（2.5% 大學中心[C-S1]／4.7% 系統性回顧彙總[C-S17]／
  5.6% 荷蘭全國[C-S18]／7% 隨機試驗擴大廓清組[C-S43]），標題寫「同一個手術，不同的人群」

---

## C4 `bl-tmt`〈三聯療法實際上怎麼做，誰適合〉【紅線 2】【利益揭露】

### Key facts

**A. 選人條件：三個指引，三種措辭，必須並陳（紅線 2 的核心）**

**① EAU 2026（最具體的腫瘤條件）**[C-S19] —— 6.8.1.a 逐字：
> 「Trimodality therapy is best suited for patients with **solitary, unifocal cT2-T3a tumours, absence of extensive or
> multifocal CIS, no or unilateral hydronephrosis, and good baseline bladder function.** Patient selection is critical
> in achieving good outcomes. **In contemporary series, approximately 25-30% of cystectomy candidates may be appropriate
> for bladder preservation.** Trimodality therapy should also be considered for patients **medically unfit or unwilling
> to undergo RC.** During TURBT, **as much visible tumour as possible should be resected**; a repeat transurethral
> resection may reveal residual disease in **> 50% of cases**. Pelvic node dissection before TMT is not routinely performed.」

EAU 的建議欄逐字：
> 「**Offer radical cystectomy or bladder-preserving trimodality treatment (TMT) as primary curative option for eligible
> patients** since they are more effective than radiotherapy alone. **Strong**」
> 「**Advise patients who are candidates for TMT that bladder monitoring post-treatment is essential. Strong**」
> 「**Manage all patients who are candidates for trimodality therapy in a multidisciplinary team setting.
> The choice of treatment modality should be made through a shared decision-making process. Strong**」

**② AUA／ASCO／SUO 2024（措辭不同：沒有「單側水腎可以」，CIS 直接寫「no CIS」）**[C-S20] —— 逐字：
> 「**Patients with large tumors unable to be resected by TURBT, multifocal CIS, T3/T4 tumors, and/or hydronephrosis
> are not ideal candidates for any type of bladder preserving therapy.** Random biopsies may help ensure that there is
> no associated CIS. Although patients with these characteristics may be cured by a multi-modal treatment … **that
> likelihood is low, and the probability for the need of salvage cystectomy is significant.**」
> 「**Additionally, ideal patients for tri-modality therapy include those in whom complete resection is feasible and who
> have no hydronephrosis and no CIS.**」
> 建議條文 21：「For patients with newly diagnosed non-metastatic muscle-invasive bladder cancer **who desire to retain
> their bladder**, and for those with significant comorbidities for whom radical cystectomy is not a treatment option,
> clinicians **should offer bladder preserving therapy when clinically appropriate**. (Clinical Principle)」
> 建議條文 22：「In patients under consideration for bladder preserving therapy, **maximal debulking TURBT and assessment
> of multifocal disease/carcinoma in situ (CIS) should be performed**. (Strong Recommendation; Evidence Level: Grade C)」
> 建議條文 25：「…clinicians should offer maximal TURBT followed by chemotherapy combined with external beam radiation
> therapy (EBRT). **Planned cystoscopic surveillance per high-risk NMIBC schedule should be performed.**
> (Strong Recommendation; Evidence Level: Grade B)」
> 建議條文 24（反面）：「For patients with muscle-invasive bladder cancer, **clinicians should not offer radiation therapy
> alone as a curative treatment.** (Strong Recommendation; Evidence Level: Grade C)」
> 病理型態：「Patients with **adenocarcinomas, sarcomas, and squamous cell carcinomas** have not been included in
> prospective studies of radiation-based bladder preservation and thus **should not receive this therapy unless medically
> unfit for cystectomy**.」
> AUA 的整體立場句（可直接引，對本專題立場有利但要原文照引）：「currently the Panel believes that **multi-modal bladder
> preserving therapy is the preferred treatment in those patients who desire bladder preservation and understand the
> unique risks associated with this approach** or those who are medically unfit for surgery.」

**③ NICE NG2（2015-02-25 發布；根本不給腫瘤條件，改成「兩條路都要提供」）**[C-S21] —— 逐字：
> 1.5.5「**Offer a choice of radical cystectomy or radiotherapy with a radiosensitiser** to adults with muscle-invasive
> urothelial bladder cancer for whom radical therapy is suitable.」
> 1.5.6「Involve **a urologist who performs radical cystectomy, a clinical oncologist and a clinical nurse specialist**
> in discussions with the person about the choice of treatment.」
> 1.5.7「When discussing the choice of treatment, cover the: prognosis with or without treatment；
> **limited evidence about whether surgery or radiotherapy with a radiosensitiser is the most effective cancer treatment**；
> benefits and risks of surgery and radiotherapy with a radiosensitiser, **including the impact on sexual and bowel
> function and the risk of death as a result of the treatment**.」

**→ 三者的差異本身就是內容，逐條並陳：**
| | 腫瘤數目／期別 | CIS | 水腎 | 刮除 | 膀胱功能 |
|---|---|---|---|---|---|
| EAU 2026 | 單一、單灶、cT2–T3a | 沒有**廣泛或多發**的 CIS | **沒有、或只有單側**水腎 | 盡量刮乾淨 | 基礎膀胱功能良好 |
| AUA 2024 | 不寫「單一」；T3/T4 不是理想人選 | **沒有** CIS（並建議隨機切片確認） | **沒有**水腎 | 完全刮除可行 | 未單獨列出 |
| NICE NG2 | **不給腫瘤條件** | — | — | — | — |
| 三者共同 | 都要多專科討論、都要共同決策、都不得只給放療 | | | | |

**→ SPEC §四紅線 2 要求的「選人條件逐條」在這裡全部有了，而且措辭差異可以原文並陳。**
腎功能那一條：三個指引都沒有寫死一個數字給放射增敏化療；可寫的是
「能不能用 cisplatin 當增敏劑，看的是同一套 Galsky 條件（見 C2）；用不了 cisplatin 的人有
5-FU＋mitomycin-C 或低劑量 gemcitabine 這兩條路」（EAU 原文：「good chemotherapy options are available for
non-cisplatin candidates, such as **5-FU/mitomycin-C or low-dose gemcitabine**」[C-S19]；
AUA：「**Carboplatin should not be used as a radiosensitizer unless there are contraindications to cisplatin, 5-FU,
and gemcitabine.**」[C-S20]）。

**B. 同步化放療的證據：BC2001（三個數字必須同框）**

**BC2001（James 2012，NEJM 366:1477–1488）**[C-S4]：多中心第 3 期，**360 人**隨機分到放療 ± 同步化療
（5-FU 500 mg/m²/日於第 1–5 與第 16–20 次分次期間＋mitomycin C 12 mg/m² 第 1 天）；
另有部分 2×2 因子設計的放療體積隨機（結果另報）。中位追蹤 69.9 個月。
1. **主要終點・無局部區域疾病存活（2 年）：67%（95% CI 59–74）vs 54%（46–62），HR 0.68（0.48–0.96），p=0.03。**
2. **總存活（5 年）：48%（40–55）vs 35%（28–43），HR 0.82（0.63–1.09），p=0.16——沒有達顯著。**
3. **第 3–4 級不良事件：治療期間 36.0% vs 27.5%（p=0.07）；追蹤期間 8.3% vs 15.7%（p=0.07）。**
   NEJM 的結論句逐字：「Synchronous chemotherapy with fluorouracil and mitomycin C combined with radiotherapy
   significantly improved locoregional control of bladder cancer, as compared with radiotherapy alone,
   **with no significant increase in adverse events.**」
   → **見 ⚠ 第 3 點：第三個數字要標 p 值，不可只寫「上升」。**

**BC2001 十年追蹤（Hall 2022，Eur Urol 82:273–279）**[C-S5]：458 人入組（360 人進化療隨機、218 人進放療體積隨機），
**中位追蹤 9.9 年**。局部區域控制 HR 0.61（0.43–0.86，p=0.004）、侵襲性局部區域控制 HR 0.55（0.36–0.84，p=0.006）；
無病存活 HR 0.78（0.60–1.02，p=0.069）、無轉移存活 HR 0.78（0.58–1.05，p=0.089）、
總存活 HR 0.88（0.69–1.13，p=0.3）、膀胱癌專一存活 HR 0.79（0.59–1.06，p=0.11)——**四個都沒有達顯著**。
**5 年膀胱切除率：化放療 14%（95% CI 9–21）vs 單純放療 22%（16–31），HR 0.54（0.31–0.95），p=0.034。**
放療標準體積與縮小高劑量體積之間**沒有差別**。

**C. BCON（缺氧修飾，第二條增敏路線）**

Hoskin 2010（JCO 28:4912–4918）[C-S7]：**333 人**局部晚期膀胱癌隨機分到單純放療 vs 放療＋carbogen 與 nicotinamide（CON）；
劑量為 55 Gy/20 次/4 週 或 64 Gy/32 次/6.5 週。
- **主要終點・6 個月膀胱鏡控制：81%（RT+CON）vs 76%（RT），p=0.3——沒有達顯著**（而且只有略多於一半的病人在該時間點做了膀胱鏡）。
- **3 年總存活 59% vs 46%（p=0.04）；3 年無局部復發存活 54% vs 43%（p=0.06）；死亡風險降低 14%（p=0.04）。**
- 多變項分析中 RT+CON 顯著降低復發（p=0.05）與死亡（p=0.03）風險。**晚期泌尿道與腸胃道併發症兩組相似。**
- 作者結論逐字：「RT + CON produced **a small nonsignificant improvement** in CC(6m). Differences in OS, risk of death,
  and local relapse were significantly in favor of RT + CON.」

**D. RTOG 的前瞻世代（沒有比較組，但這是長期追蹤的來源）**

Mak 2014（JCO 32:3801–3809，六個 RTOG 試驗的彙總：8802、8903、9506、9706、9906、0233，五個第 2 期＋一個第 3 期）[C-S8]：
**468 位肌肉侵犯型病人**，中位年齡 66 歲（34–93），**臨床期別 T2 61%、T3 35%、T4a 4%**。
- **對同步化放療的完全反應 69%。**
- 中位追蹤 4.3 年（存活者 7.8 年，n=205）：**5 年／10 年總存活 57%／36%；5 年／10 年疾病專一存活 71%／65%。**
- **5 年／10 年累積發生率：肌肉侵犯型局部失敗 13%／14%；非肌肉侵犯型局部失敗 31%／36%；遠端轉移 31%／35%。**
- AUA 2024 轉述同一世代時補了一句：「Mak et al. have reported a 5-year survival of 57% for all study patients,
  **of whom, 80% did have an intact bladder**」[C-S20]。
- 作者結論：「long-term DSS **comparable to modern immediate cystectomy studies**, for patients with **similarly staged**
  MIBC … CMT can be considered as an alternative to radical cystectomy, **especially in elderly patients not well
  suited for surgery**.」→ **這句的後半段要照引，不可只引前半段。**

**E. 增敏劑怎麼選：RTOG 0712（隨機第 2 期，但沒有 power 做組間比較）**

Coen 2019（JCO 37:44–51）[C-S9]：cT2–4a，**70 人入組、66 人可分析（每組 33）**。
先做經尿道刮除＋誘導化放療到 40 Gy；完全反應者鞏固到 64 Gy，其餘做膀胱切除；之後給輔助 gemcitabine/cisplatin。
- **主要終點是 3 年無遠端轉移率（基準 75%）。試驗「not statistically powered to compare regimens」。**
- **3 年無遠端轉移：FCT（5-FU＋cisplatin＋每日兩次放療）78%；GD（gemcitabine＋每日一次放療）84%。**
- 3 年膀胱完整且無遠端轉移存活：67% vs 72%。誘導後完全反應率 88% vs 78%。
- **治療相關第 3–4 級毒性：FCT 21/33（64%）、GD 18/33（55%）**；血液學毒性 18（55%）vs 14（42%）、
  腸胃道 2（6%）vs 3（9%）、泌尿生殖道各 2（6%）。
- 作者結論：「Both regimens demonstrated DMF3 greater than 75%. **There were fewer toxicities observed in the GD arm.**」

**F. 分次方式：55 Gy/20 對 64 Gy/32（個別病人資料統合分析）**

Choudhury 2021（Lancet Oncol 22:246–255，OA）[C-S6]：**BC2001 與 BCON 兩個英國隨機試驗的個別病人資料**，
**782 人**（BC2001 456、BCON 326；64 Gy/32 共 376 人（48%）、55 Gy/20 共 406 人（52%）），**中位追蹤 120 個月（IQR 99–159）**。
- **族群標籤要寫清楚：T1G3（高惡性度非肌肉侵犯型）或 T2–T4、N0M0** ——**這個世代混有高風險 NMIBC**，不是純 MIBC。
- 共同主要終點：侵襲性局部區域控制（非劣性界限 HR=1.25）與晚期膀胱／直腸毒性（絕對風險差非劣性界限 10%）。
- **結果：55 Gy/20 的侵襲性局部區域復發風險較低——校正後 HR 0.71（95% CI 0.52–0.96），即非劣性成立且達優越；
  毒性相當（校正後風險差 −3.37%，95% CI −11.85 到 5.10）。**
- 作者結論：「**55 Gy in 20 fractions should be adopted as a standard of care for bladder preservation in patients with
  locally advanced bladder cancer.**」
- NICE 的措辭（並陳）[C-S21]：「Use a radiosensitiser (such as **mitomycin in combination with fluorouracil [5-FU] or
  carbogen in combination with nicotinamide**) when giving radical radiotherapy (**for example, 64 Gy in 32 fractions over
  6.5 weeks or 55 Gy in 20 fractions over 4 weeks**)」，並註明 2015 年 2 月時這兩種組合都是仿單外使用。
- EAU 2026 的劑量描述[C-S19]：常規為全骨盆／膀胱 40–45 Gy 起始、加強到全膀胱或腫瘤床 60–66 Gy；
  只照膀胱時，中度低分次 55 Gy/20 次是被接受的替代方案。

**G. 進行中的試驗（一律寫「進行中」，帶狀態與預計主要完成日）**

| 試驗 | NCT | 狀態（查詢日 2026-09-13） | 設計與 n | 主要終點 | 預計主要完成 |
|---|---|---|---|---|---|
| **SWOG/NRG S1806** | NCT03775265 | **ACTIVE_NOT_RECRUITING**（最後更新 2026-08-27） | 第 3 期隨機、同步化放療 ± atezolizumab，預計 n=475，2019-06-03 開始 | **膀胱完整無事件存活（BI-EFS）** | **2027-06-01（估計）**[C-S37] |
| **KEYNOTE-992** | NCT04241185 | **ACTIVE_NOT_RECRUITING**（最後更新 2026-04-29） | 第 3 期隨機、同步化放療 ± pembrolizumab，預計 n=520，2020-05-19 開始 | **膀胱完整無事件存活（BI-EFS）** | **2027-01-31（估計）**；全試驗完成估 2031-11-01[C-S38] |

EAU 2026 的措辭（可直接引）：「The integration of IO with TMT is **under investigation**. Future studies may clarify
sequencing of IO with bladder-preserving chemoradiation. **Outside of trials, combined use remains investigational.**」[C-S19]

**H. 毒性（長期）**

Efstathiou 2009（JCO 27:4055–4061，RTOG 8903／9506／9706／9906 的彙總）[C-S10]：285 位合格病人中
**157 人接受完整同步化放療、治療開始後存活 ≥2 年且膀胱完整**，中位追蹤 5.4 年（2.0–13.2）。
- **7% 出現晚期第 3 級以上骨盆毒性：泌尿生殖道 5.7%、腸胃道 1.9%。**
- **9 位發生第 3 級以上泌尿道毒性的人中，只有 1 位持續不緩解。**
- **沒有任何晚期第 4 級毒性，沒有治療相關死亡。**
- 年齡、性別、期別、有無 CIS、刮除是否完全都**不能預測**晚期第 3 級以上骨盆毒性。
- EAU 2026 引同一組資料並補一句：現代影像導引強度調控與適應性規劃可能進一步降低骨盆毒性[C-S19]。

**I. 變異型組織（SPEC §零：一句指路，不獨立成篇）**[C-S19][C-S20]

- EAU 2026：鱗狀、腺狀或微乳頭**亞型的尿路上皮癌**，其完全反應、存活與挽救性切除率**與純尿路上皮癌相近**，可考慮三聯療法；
  但**純鱗狀細胞癌或腺癌**在三聯療法後存活較差，「should be counselled for upfront RC」。
- AUA 2024：腺癌、肉瘤與鱗狀細胞癌**沒有被納入放射線保留膀胱的前瞻研究**，除非不適合手術，否則不應接受這種治療。

### 反方向的資料（誠實必列）

- **BC2001 的總存活沒有達顯著**（5 年 48% vs 35%，p=0.16；10 年 HR 0.88，p=0.3）[C-S4][C-S5]。
- **BCON 的主要終點（6 個月膀胱鏡控制）沒有達顯著**（81% vs 76%，p=0.3），而且只有略多於一半的人真的做了那次膀胱鏡[C-S7]。
- **RTOG 0712 沒有 power 做兩組比較**，不能寫成「gemcitabine 比較好」[C-S9]。
- **RTOG 彙總世代的 10 年非肌肉侵犯型局部失敗 36%**——保留下來的膀胱會一直長新的腫瘤[C-S8]。
- **hypofractionation 的統合分析混有 T1G3 高風險非肌肉侵犯型病人**[C-S6]——不是純 MIBC 世代。
- AUA 2024 對「誰適合」寫得比 EAU 保守，而且明說 T3/T4、多發 CIS、水腎「不是任何保留膀胱做法的理想人選」[C-S20]。
- **重新刮除會在超過一半的病例發現殘餘病灶**[C-S19]——「刮乾淨了」這件事沒有想像中可靠（並指路 A2）。

### Claim ceiling

**可寫**：三個指引的選人條件**逐字並陳**（並寫明它們不一樣）；BC2001 的三個數字**同框並各帶 p 值**；
BCON 的「主要終點沒達顯著、存活達顯著」兩句一起寫；RTOG 彙總世代的 5/10 年數字（帶 n=468、期別分布、追蹤長度）；
55 Gy/20 對 64 Gy/32 的非劣性＋侵襲性局部控制較優（帶 n=782、混有 T1G3、中位追蹤 120 個月）；
晚期第 3 級以上骨盆毒性 5.7% 泌尿／1.9% 腸胃（帶 n=157、存活 ≥2 年且膀胱完整、中位追蹤 5.4 年）；
S1806 與 KEYNOTE-992 **一律寫「進行中」，帶狀態與預計主要完成日期**。

**不可寫**：「只要不想開刀就可以做」；把三個指引的條件合併成一張統一的表；
把 BC2001 的化療益處寫成「延長存活」；把 BC2001 的毒性寫成「上升」而不帶 p=0.07；
把 BCON 寫成「有效」而不寫主要終點沒達顯著；把 RTOG 0712 寫成兩種增敏劑的優劣比較；
把進行中試驗寫成已知結果；把 hypofractionation 的結果外推到純 MIBC 而不標那個世代混有 T1G3；
拿本篇的數字去跟膀胱切除比（兩條路的比較**只在 C1**，SPEC §六）。

### Caveats／safety notes

- **利益揭露逐字放在第一個 h4 之前**（SPEC §二）。
- 放療的技術與自我照顧全部指向 `pel-*`（SPEC §一.1、§六）：`pel-sim-day`、`pel-igrt`、
  `pel-urinary`〈膀胱與解尿的那幾週〉、`pel-bladder-bowel`、`pel-toxicity`、`pel-late`。**本篇不重寫那一塊。**
- 熱治療合併灌注化療（含 HIVEC-1 陰性結果）一句指路 `nt-ht-bladder`〈膀胱癌〉。
- 「三聯療法不是每家醫院都有，要問你的主治醫師轉去哪裡」——SPEC §一.5 的固定寫法，**不寫院內配置**。

### 台灣端

- **健保支付標準全文檔搜尋「膀胱癌」＝零筆**[C-S39]。
  搜尋「低分次」僅三筆：36022B（乳癌術後低分次全乳照射合併局部加強照射，279,986 點）、
  36023B（乳癌術後低分次全乳照射無合併局部加強照射，246,960 點）、
  36024B（直腸癌術前低分次放射治療，204,966 點）。
  **→ 沒有以膀胱癌為適應症的低分次或包裹式放療項目。寫成「查不到列項，問醫務課／個管師」，永不推論。**
- **構件層級的項目存在**（可逐條寫，帶點數與生效日）[C-S39]：
  36001B 電腦治療規劃－簡單 3,309 點；**36015B 電腦治療規劃－複雜 11,483 點**
  （備註逐字：「指使用三度空間電腦軟體做放射治療之設計，包括順形放射治療、強度調控放射治療、立體定位放射治療等技術……」）；
  36018B 模擬定位攝影 3,619 點；36011B 直線加速器遠隔照射治療每一簡單照野 1,231 點；
  36012B 每一複雜照野 1,334 點；36019B 劑量計算 301 點（每週最多一次）；
  37026B 放射治療之皮膚處理（一個療程）244 點。
  刮除端：**78008C 膀胱腫瘤之切除－內視鏡下－含膀胱鏡檢 8,027 點（2023-11-01 生效）**；
  78049C 含膀胱鏡檢及輸尿管鏡檢查 8,886 點。膀胱鏡：**28019C 膀胱鏡檢查 1,800 點**。
  **→ 可寫：三聯療法的每一個構件在健保裡都有項目；但「三聯療法」本身不是一個包裹給付項目。**
- **gap**：台灣的三聯療法使用率、膀胱癌期別分布——查不到（hpa.gov.tw TLS 失敗，見 FAIL-4）。

### 給繪圖組的數字（`fig-bl-tmt-eligible`）

- 三欄（EAU 2026／AUA 2024／NICE NG2）× 五列（腫瘤數目與期別／CIS／水腎／刮除／膀胱功能）的並陳表，
  **每一格用該指引的原文用語**，空白處明寫「該指引不給這一條」（NICE 整欄都是）。
- 底線字：「三個指引的措辭不一樣，這不是筆誤；決定要在多專科團隊裡跟你一起做。」
- **不可**畫成可自行打勾的資格檢核表（沿用 SPEC 紅線 3 與紅線 5 對計分表的禁令）。

---

## C5 `bl-tmt-after`〈保留下來的膀胱，之後要顧什麼〉【紅線 10】【利益揭露】

### Key facts

**A. 追蹤時程：三個指引，都沒有停止點（逐字並陳）**

**EAU 2026（7.3 Follow-up after trimodality therapy）**[C-S19] 逐字：
> 「Most recurrences occur **within the first two to five years** after treatment. Patients with muscle-invasive
> intravesical recurrence should be **evaluated promptly for salvage cystectomy** when feasible. There is general expert
> consensus that **cystoscopy should be performed every three months during the first two years, every six months until
> year five, and annually thereafter.** Urine cytology and **cross-sectional imaging of the chest, abdomen, and pelvis
> (CT or MRI, including upper-tract imaging) is recommended every six to twelve months for the first three to five years,
> and then as clinically indicated.** … Evidence is available indicating that **close cystoscopic monitoring and early
> salvage cystectomy are critical to long-term bladder preservation and DSS.** **Post-radiation cystoscopic and cytologic
> interpretation can be challenging due to post-RT mucosal changes.** Surveillance should also include **assessment of
> bladder function and late toxicity**.」

**AUA/ASCO/SUO 2024**[C-S20]：建議條文 25 要求「planned cystoscopic surveillance **per high-risk NMIBC schedule**」；
建議條文 27：「Following completion of bladder preserving therapy, clinicians should perform regular surveillance with
**computed tomography (CT) scans, cystoscopy, and urine cytology**. (Strong Recommendation; Evidence Level: Grade C)」。
內文逐字：「**Published protocols recommend every 3 month cystoscopy during the first year, every 4-6 months in the
second, and every 6-12 months thereafter.** In addition, the Panel recommends cross-sectional imaging of the abdomen and
pelvis and chest imaging **every six months for the first two years**, although, again, **there is no published data
showing that this improves survival.**」
還有一句要一起寫：「Those who are **biopsy-proven complete responders** to bladder preserving protocols **remain at risk
for both invasive and non-invasive recurrences as well as new tumors in the upper tracts.**」

**NICE NG2（1.6.2）**[C-S21] 逐字：
> 「After radical radiotherapy consider using a follow-up protocol that includes all of the following: **rigid cystoscopy
> 3 months after radiotherapy has been completed**, followed by either rigid or flexible cystoscopy: **every 3 months for
> the first 2 years then every 6 months for the next 2 years then every year thereafter, according to clinical judgement
> and the person's preference**；**upper-tract imaging every year for 5 years**；monitoring for local and distant recurrence
> using CT of the abdomen, pelvis and chest … **6, 12 and 24 months** after radical radiotherapy has finished.」

**→ 紅線 10 的寫法**：三個指引的間隔不一樣（EAU 前兩年 q3m、AUA 第一年 q3m 第二年 q4–6m、NICE 前兩年 q3m），
**但三個都沒有給停止點**，最後一段都寫成「之後每年一次」。**照原文引，不要合成一個時程表，也不要寫「照幾年就可以停」。**
上泌尿道：EAU 要求影像含上泌尿道、NICE 明寫「每年一次照五年」。

**B. 保留下來的膀胱裡會發生什麼：復發的比率與時間**

- **RTOG 六個前瞻試驗的彙總（Mak 2014，n=468，cT2 61%／T3 35%／T4a 4%，中位追蹤 4.3 年、存活者 7.8 年）**[C-S8]：
  **非肌肉侵犯型局部失敗 5 年 31%／10 年 36%；肌肉侵犯型局部失敗 5 年 13%／10 年 14%；遠端轉移 5 年 31%／10 年 35%。**
  → **兩個訊息：① 復發以非肌肉侵犯型為主，而且是肌肉侵犯型復發的兩倍以上；
  ② 5 年到 10 年之間新增得很少（31%→36%、13%→14%），也就是晚期復發少見。**
- **配對世代統合分析（Matsukawa 2025，87 篇、n=28,218）**[C-S33]：
  三聯療法後**膀胱內復發彙總估計 23.1%（95% CI 19.0–27.7）**；完全反應率 74.4%。
- **SPARE 的觀察（作者自己的話）**[C-S2]：「Loco-regional recurrence-free survival was worse after RT,
  **mainly due to the incidence of NMIBC, which was more frequent than invasive recurrence.** …
  suggests **the bladder remains at high risk of developing second primary disease**. …
  **Many cases of NMIBC can be salvaged with local treatment, thus the bladder preservation rate remained high**.」
- **非肌肉侵犯型復發怎麼處理**（AUA 建議條文 29）[C-S20]：「In patients who have a **non-muscle invasive recurrence**
  after bladder preserving therapy, clinicians may offer **either local measures, such as TURBT with intravesical therapy,
  or radical cystectomy** with bilateral pelvic lymphadenectomy. (Moderate Recommendation; Evidence Level: Grade C)」
  並補：「The presence of an NMIBC relapse, however, **predicts an increased likelihood for further future relapses**,
  including both NMIBC and MIBC recurrences.」
- **肌肉侵犯型復發怎麼處理**（AUA 建議條文 28）[C-S20]：「In patients who are medically fit and have **residual or
  recurrent muscle-invasive disease** following bladder preserving therapy, clinicians **should offer radical cystectomy
  with bilateral pelvic lymphadenectomy**. (Strong Recommendation; Evidence Level: Grade C)」
  EAU 同義：「Salvage cystectomy is indicated in **non-responders to bladder-sparing therapy**, that is,
  non-metastatic muscle invasive recurrence after TMT.」[C-S19]

**C. 挽救性膀胱切除：比率、併發症、結果**

- **比率**（見 ⚠ 第 5 點的表）：彙總 **19.2%**（73 篇、9,110 人、追蹤 >5 年的研究）[C-S14]；
  Schuettfort 同時給出兩個理由的彙總比率：**對保留膀胱治療無反應 15.5%、保留後局部復發 28.7%**。
- **併發症**[C-S14]：「Only three studies provided a thorough report of complication rates after SV-RC.
  **The overall complication rate ranged between 67 and 72% with a 30-day mortality rate of 0-8.8%.**」
  作者結論：「This procedure carries a **proportionally high rate of complications** and is usually accompanied by
  **an incontinent urinary diversion**.」→ **也就是說，挽救性切除後通常做不成新膀胱。**
- **與初次切除的比較（單中心，n=265，2003–2013，cT1–T4，中位追蹤 65.5 個月）**[C-S15]：
  三聯療法後的挽救性切除與初次切除相比，**術中與早期（≤90 天）併發症沒有差別**；
  **晚期（>90 天）併發症較多**（任何晚期併發症 HR 2.3，p=0.02；主要晚期併發症 HR 2.1，p<0.05）；
  **疾病專一存活與總存活沒有差別**（p=0.8／p=0.9）。
- **多國配對分析（Pyrgidis 2026，13 個高量中心，1:1 傾向分數配對，n=118（每組 59），中位年齡 73 歲）**[C-S16]：
  **7 人（11%）發生嚴重的第 4 或 5 級圍術期併發症；30 天與 90 天存活率分別為 93% 與 91%**
  （即 90 天死亡約 9%——**這是高量中心的挽救性手術數字，必須帶這個標籤**）。
  挽救性切除的失血多 297 mL（95% CI 73–520，p=0.010）、進加護病房的勝算高（OR 2.8，1.2–6.7，p=0.017）。
  中位追蹤只有 10 個月（IQR 5–34）時已有 29 例死亡；**總存活比初次切除差（HR 1.9，1.2–4.1，p=0.032）**，
  作者的解釋是「**likely reflecting tumor biology**」。
- **AUA 的兩句實務提醒**[C-S20]：「Pelvic surgery is **more difficult after prior full-dose EBRT** with a possible higher
  rate of complications, and **radiation may limit the choice of urinary diversions and the ability to perform
  nerve-sparing surgery.**」以及「In addition, the options for urinary diversion **may be more limited**.」

**D. 保留下來的膀胱功能到底怎麼樣（有真資料）**

**Zietman 2003（麻省總醫院，J Urol 170:1772–1776）**[C-S11]——**這是這一題最直接的資料**：
1986–2000 年 **221 位 cT2–4a** 接受三聯療法者中，2001 年時有 **71 人存活、保有原生膀胱且無病**；
**69% 參與了部分或全部研究**，距治療**中位 6.3 年（範圍 1.6–14.9 年）**。
- **尿路動力學（n=32）：24 人膀胱功能正常；7 人膀胱順應性下降；2 位女性有膀胱過度敏感、不自主逼尿肌收縮與失禁。**
- **問卷：解尿流速症狀 6%、急尿感 15%、控制問題 19%；女性中 11% 使用護墊。
  因泌尿症狀而感到困擾的比例約為症狀盛行率的一半。**
- **腸道症狀 22%，其中 14% 有任何程度的困擾。**
- **多數男性保有性功能。整體健康相關生活品質高。**
- 作者結論逐字：「**The majority of patients treated with trimodality therapy retain good bladder function.
  A fifth have evidence of bowel dysfunction.**」

**BC2001 的病人自填生活品質（Huddart 2020，Eur Urol 77:260–268，OA）**[C-S13]：
458 位 T2–T4a N0M0 病人，在基線、治療結束、與放療後 6/12/24/36/48/60 個月填 FACT-BL。
- 基線回覆率 92%／93%；**12 個月時只剩 54%／52%**（這個掉落率本身要寫）。
- **治療結束時生活品質顯著下降**（膀胱癌次量表 −5.06，99% CI −6.12 到 −4.00，p<0.001；FACT-B 總分 −8.22，
  −10.76 到 −5.68，p<0.01），**6 個月時回到基線，之後維持**。
- **加化療對生活品質沒有影響**（任何時間點兩組都沒有顯著差異）。
- 作者結論：「**Two-thirds of patients report stable or improved HRQoL on long-term follow-up.**」
- **反過來讀（誠實必列）**：EAU 2026 引同一組資料時寫的是「**Approximately 33% of patients reported persistent lower
  BLCS scores after five years.**」[C-S19]——**三分之一的人五年後膀胱症狀分數仍然比治療前差。**
- EAU 同段補充的性別差異[C-S19]：治療後 2 年女性的生活品質比男性多掉一截（看來與泌尿功能惡化有關），
  但五年時男女大致都回到基線。

**晚期毒性**（同 C4 的 [C-S10]，C5 也要寫）：157 位存活 ≥2 年且膀胱完整者，中位追蹤 5.4 年，
**晚期第 3 級以上骨盆毒性 7%（泌尿生殖道 5.7%、腸胃道 1.9%）；沒有第 4 級，沒有治療相關死亡；
9 位第 3 級以上泌尿道毒性中只有 1 位持續不緩解**[C-S10]。

**E. 膀胱鏡本身是這個病最真實的長期負擔（紅線 10 的另一半）**

可引的事實面：
- 三個指引都沒有停止點（見 A）[C-S19][C-S20][C-S21]。
- EAU 明寫**放療後的膀胱鏡與細胞學判讀會因黏膜變化而困難**[C-S19]——也就是會有更多「再看一次」與切片。
- AUA 明寫**沒有任何發表資料證明這個影像追蹤頻率能改善存活**[C-S20]。
- 追蹤本身是三聯療法之所以成立的條件：AUA「The overall survival rates achieved in bladder preserving series that
  appear comparable to those obtained with immediate cystectomy are likely, **in part, due to the use of close
  surveillance with early salvage cystectomy** in patients with residual/recurrent disease as well as careful patient
  selection.」[C-S20]；EAU「**close cystoscopic monitoring and early salvage cystectomy are critical to long-term bladder
  preservation and DSS**」[C-S19]。
- **不適感本身沒有可引的量化數字在本 brief 裡**（B4 那組可能有）。**C5 只能寫成「這是要照一輩子的檢查」
  與「指引沒有給停止點」，不可自行加上任何不適感的百分比。**

### 反方向的資料（誠實必列）

- 保留下來的膀胱**一直在長新的東西**：10 年非肌肉侵犯型局部失敗 36%[C-S8]、膀胱內復發彙總 23.1%[C-S33]。
- **三分之一的人五年後膀胱症狀分數仍低於治療前**[C-S19][C-S13]。
- **五分之一的人最後還是要切除膀胱**，而且那次手術的晚期併發症比第一次就開刀多（HR 2.1–2.3）[C-S14][C-S15]，
  在高量中心的配對資料裡 90 天死亡約 9%[C-S16]，而且**通常做不成新膀胱**[C-S14][C-S20]。
- Zietman 那個世代是**存活、無病、保有膀胱的人**（71/221），**本來就是結果最好的那一群**，
  而且只有 69% 參與、只有 32 人做了尿路動力學——**這個標籤不可省**[C-S11]。
- BC2001 生活品質的 12 個月回覆率只剩約一半[C-S13]。

### Claim ceiling

**可寫**：三個指引的追蹤時程**逐字並陳**，並明寫**沒有停止點**；
復發的比率與時間（帶 n、追蹤長度、以及「非肌肉侵犯型多於肌肉侵犯型」）；
非肌肉侵犯型復發多數仍可用局部處理救回（引 SPARE 與 AUA 條文 29 的原文）；
挽救性切除的比率（約五分之一）、併發症（67–72%）、30 天死亡（0–8.8%）、晚期併發症較多（HR 2.1–2.3）、
以及**挽救後通常是不禁尿型改道**；
Zietman 的膀胱功能數字（帶「這是存活且保有膀胱者」的標籤）；
「三分之一的人五年後膀胱症狀仍較差」；晚期第 3 級以上骨盆毒性 5.7%／1.9%。

**不可寫**：「照幾年就可以停」；「照完五年就沒事」；把膀胱鏡的不舒服寫成不重要；
把 Zietman 的「多數人膀胱功能良好」寫成「三聯療法不影響膀胱功能」（分母是最好的那一群）；
把挽救性切除寫成「保險」（它的晚期併發症較多、改道選擇受限、總存活較差）；
用 B 組的非肌肉侵犯型追蹤數字代替本篇（兩者的族群不同，SPEC §六：NMIBC 追蹤歸 B4）。

### Caveats／safety notes

- **利益揭露逐字放在第一個 h4 之前**（SPEC §二）。
- 放療的晚期影響與自我照顧指向 `pel-late`、`pel-toxicity`、`pel-colitis`、`pel-urinary`（SPEC §六）。
- 「要立刻回診」的訊號：肉眼血尿、新出現或惡化的解尿困難、發燒合併排尿痛——**這幾句要寫成具體症狀，
  但本 brief 沒有可引的量化來源，只能寫成「出現這些就回診」的臨床指引式敘述，不加數字。**

### 台灣端

- **28019C 膀胱鏡檢查 1,800 點**（1995-03-01 生效）[C-S39]——追蹤用的膀胱鏡在健保裡有項目。
- **50011C 膀胱灌注 260 點**[C-S39]——非肌肉侵犯型復發時的局部處理有項目（灌注藥物本身歸 B 組）。
- **78008C 膀胱腫瘤之切除－內視鏡下－含膀胱鏡檢 8,027 點**[C-S39]——復發時再刮有項目。
- **gap**：追蹤頻率有沒有次數限制、事前審查怎麼走——支付標準檔的備註欄在這幾個項目均**未載頻率限制**，
  但**不得因此推論「照多少次都給付」**。寫「問醫務課／個管師」。

### 給繪圖組的數字（`fig-bl-followup` 的三聯療法那一半，與 B4 共用一張）

- 時間軸三條（EAU 2026／AUA 2024／NICE NG2），每條標出膀胱鏡間隔，**末端都標「沒有停止點」**
- 復發那一格：5 年／10 年非肌肉侵犯型局部失敗 31%／36%；肌肉侵犯型 13%／14%（RTOG 彙總，n=468）[C-S8]
- 挽救性切除那一格：約 19.2%（彙總，追蹤 >5 年）[C-S14]；併發症 67–72%[C-S14]
- 膀胱功能那一格：中位 6.3 年後，尿路動力學正常 24/32；急尿感 15%、控制問題 19%、腸道症狀 22%[C-S11]；
  五年時仍有約三分之一膀胱症狀分數低於治療前[C-S19][C-S13]

---

## 來源清單

（編號 C-S3 與 C-S28 在查證過程中改列 FAIL，見 [C-F2] 與 [C-F1]；編號不重複使用。）

### PASS

- **[C-S1] PASS** Zlotta AR, Ballas LK, Niemierko A, et al. *Radical cystectomy versus trimodality therapy for
  muscle-invasive bladder cancer: a multi-institutional propensity score matched and weighted analysis.*
  **Lancet Oncol. 2023;24(6):669–681.** DOI 10.1016/S1470-2045(23)00170-5｜PMID 37187202｜非 OA。
  Route: Europe PMC REST `search?query=DOI:"10.1016/S1470-2045(23)00170-5"&resultType=core`。摘要含全部引用數字。
- **[C-S2] PASS** Huddart RA, Birtle A, Maynard L, et al. *Clinical and patient-reported outcomes of SPARE — a randomised
  feasibility study of selective bladder preservation versus radical cystectomy.* **BJU Int. 2017;120(5):639–650.**
  DOI 10.1111/bju.13900｜PMID 28453896｜PMCID PMC5655733｜**OA**。
  Route: Europe PMC REST ＋ `/webservices/rest/PMC5655733/fullTextXML`。招募流程、Discussion 引語出自全文。
- **[C-S4] PASS** James ND, Hussain SA, Hall E, et al. *Radiotherapy with or without chemotherapy in muscle-invasive
  bladder cancer.* **N Engl J Med. 2012;366(16):1477–1488.** DOI 10.1056/NEJMoa1106106｜PMID 22512481｜非 OA。
  Route: Europe PMC REST `DOI:"10.1056/NEJMoa1106106"`。三個數字與結論句全在摘要。
- **[C-S5] PASS** Hall E, Hussain SA, Porta N, et al. *Chemoradiotherapy in Muscle-invasive Bladder Cancer: 10-yr
  Follow-up of the Phase 3 Randomised Controlled BC2001 Trial.* **Eur Urol. 2022;82(3):273–279.**
  DOI 10.1016/j.eururo.2022.04.017｜PMID 35577644｜非 OA。Route: Europe PMC REST（DOI）。
- **[C-S6] PASS** Choudhury A, Porta N, Hall E, et al. *Hypofractionated radiotherapy in locally advanced bladder cancer:
  an individual patient data meta-analysis of the BC2001 and BCON trials.* **Lancet Oncol. 2021;22(2):246–255.**
  DOI 10.1016/S1470-2045(20)30607-0｜PMID 33539743｜PMCID PMC7851111｜**OA**。Route: Europe PMC REST（DOI）。
- **[C-S7] PASS** Hoskin PJ, Rojas AM, Bentzen SM, Saunders MI. *Radiotherapy with concurrent carbogen and nicotinamide
  in bladder carcinoma.* **J Clin Oncol. 2010;28(33):4912–4918.** DOI 10.1200/JCO.2010.28.4950｜PMID 20956620｜非 OA。
  Route: Europe PMC REST（DOI）。
- **[C-S8] PASS** Mak RH, Hunt D, Shipley WU, et al. *Long-term outcomes in patients with muscle-invasive bladder cancer
  after selective bladder-preserving combined-modality therapy: a pooled analysis of RTOG protocols 8802, 8903, 9506,
  9706, 9906, and 0233.* **J Clin Oncol. 2014;32(34):3801–3809.** DOI 10.1200/JCO.2014.57.5548｜PMID 25366678｜
  PMCID PMC4239302｜非 OA（摘要可取得）。Route: Europe PMC REST（DOI）。
- **[C-S9] PASS** Coen JJ, Zhang P, Saylor PJ, et al. *Bladder Preservation With Twice-a-Day Radiation Plus
  Fluorouracil/Cisplatin or Once Daily Radiation Plus Gemcitabine for Muscle-Invasive Bladder Cancer: NRG/RTOG 0712 —
  A Randomized Phase II Trial.* **J Clin Oncol. 2019;37(1):44–51.** DOI 10.1200/JCO.18.00537｜PMID 30433852｜
  PMCID PMC6354769。Route: Europe PMC REST（DOI）。
- **[C-S10] PASS** Efstathiou JA, Bae K, Shipley WU, et al. *Late pelvic toxicity after bladder-sparing therapy in
  patients with invasive bladder cancer: RTOG 89-03, 95-06, 97-06, 99-06.* **J Clin Oncol. 2009;27(25):4055–4061.**
  DOI 10.1200/JCO.2008.19.5776｜PMID 19636019｜PMCID PMC2734419。Route: Europe PMC REST（TITLE）。
- **[C-S11] PASS** Zietman AL, Sacco D, Skowronski U, et al. *Organ conservation in invasive bladder cancer by
  transurethral resection, chemotherapy and radiation: results of a urodynamic and quality of life study on long-term
  survivors.* **J Urol. 2003;170(5):1772–1776.** DOI 10.1097/01.ju.0000093721.23249.c3｜PMID 14532773｜非 OA。
  Route: Europe PMC REST（TITLE）。
- **[C-S12] PASS** Mak KS, Smith AB, Eidelman A, et al. *Quality of Life in Long-term Survivors of Muscle-Invasive
  Bladder Cancer.* **Int J Radiat Oncol Biol Phys. 2016;96(5):1028–1036.** DOI 10.1016/j.ijrobp.2016.08.023｜
  PMID 27727064｜非 OA。Route: Europe PMC REST（TITLE）。
- **[C-S13] PASS** Huddart RA, Hall E, Lewis R, et al. *Patient-reported Quality of Life Outcomes in Patients Treated for
  Muscle-invasive Bladder Cancer with Radiotherapy ± Chemotherapy in the BC2001 Phase III Randomised Controlled Trial.*
  **Eur Urol. 2020;77(2):260–268.** DOI 10.1016/j.eururo.2019.11.001｜PMID 31843338｜PMCID PMC6983941｜**OA**。
  Route: Europe PMC REST（DOI）。
- **[C-S14] PASS** Schuettfort VM, Pradere B, Quhal F, et al. *Incidence and outcome of salvage cystectomy after bladder
  sparing therapy for muscle invasive bladder cancer: a systematic review and meta-analysis.*
  **World J Urol. 2021;39(6):1757–1768.** DOI 10.1007/s00345-020-03436-0｜PMID 32995918｜PMCID PMC8217031｜**OA**。
  Route: Europe PMC REST（DOI）。
- **[C-S15] PASS** Pieretti A, Krasnow R, Drumm M, et al. *Complications and Outcomes of Salvage Cystectomy after
  Trimodality Therapy.* **J Urol. 2021;206(1):29–36.** DOI 10.1097/JU.0000000000001696｜PMID 33617327｜非 OA。
  Route: Europe PMC REST（DOI）。
- **[C-S16] PASS** Pyrgidis N, Schulz GB, Scilipoti P, et al. *The Role of Salvage Cystectomy After Prior Trimodality
  Therapy: A Multinational Match-paired Analysis.* **Eur Urol Focus. 2026;12(1):88–95.**
  DOI 10.1016/j.euf.2025.04.028｜PMID 40300977｜非 OA。Route: Europe PMC REST（DOI）。
- **[C-S17] PASS** Maibom SL, Joensen UN, Poulsen AM, Kehlet H, Brasso K, Røder MA. *Short-term morbidity and mortality
  following radical cystectomy: a systematic review.* **BMJ Open. 2021;11(4):e043266.**
  DOI 10.1136/bmjopen-2020-043266｜PMID 33853799｜PMCID PMC8054090｜**OA**。Route: Europe PMC REST（DOI）。
- **[C-S18] PASS** Richters A, Ripping TM, Kiemeney LA, et al. *Hospital volume is associated with postoperative
  mortality after radical cystectomy for treatment of bladder cancer.* **BJU Int. 2021;128(4):511–518.**
  DOI 10.1111/bju.15334｜PMID 33404154｜PMCID PMC8519083｜**OA**。Route: Europe PMC REST（DOI）。
- **[C-S19] PASS** **EAU Guidelines on Muscle-invasive and Metastatic Bladder Cancer.** EAU Guidelines, edn. presented at
  the EAU Annual Congress **London 2026**. ISBN 978-94-92671-32-5. EAU Guidelines Office, Arnhem, The Netherlands.
  Route: 官方 landing page 實際抓取，2026-09-13：
  `https://uroweb.org/guidelines/muscle-invasive-and-metastatic-bladder-cancer/chapter/disease-management`（6.1、6.5、6.7、6.8、6.9）、
  `…/chapter/followup`（7.2、7.3、7.4）、`…/chapter/quality-of-life-and-palliative-care`（10.5）、
  `…/chapter/citation-information`（版本與 ISBN）。全部引語逐字出自這些頁面。
- **[C-S20] PASS** Chang SS, Bochner BH, Chou R, et al. **Treatment of Non-Metastatic Muscle-Invasive Bladder Cancer:
  AUA/ASCO/SUO Guideline (2017; Amended 2020, 2024).** American Urological Association；2024 年 4 月經 AUA 理事會核准。
  Route: 官方 PDF 實際下載，2026-09-13：`https://www.auanet.org/documents/Guidelines/PDF/2024%20Guidelines/MIBC%20Unabridged.pdf`
  （54 頁），以 pdftotext 取文。**註**：2017 原始版由 AUA／ASCO／ASTRO／SUO 四學會共同制定，
  2024 修訂版封面標題寫 AUA/ASCO/SUO——正文引用時照封面寫法。
- **[C-S21] PASS** **NICE. Bladder cancer: diagnosis and management. NICE guideline NG2. Published 25 February 2015.**
  Route: `https://www.nice.org.uk/guidance/ng2/chapter/Recommendations` 與 `https://www.nice.org.uk/guidance/ng2`
  實際抓取，2026-09-13。引語為 1.5.5、1.5.6、1.5.7、1.5.8、1.5.15、1.6.1、1.6.2 逐字。
- **[C-S22] PASS** Grossman HB, Natale RB, Tangen CM, et al. *Neoadjuvant chemotherapy plus cystectomy compared with
  cystectomy alone for locally advanced bladder cancer.* **N Engl J Med. 2003;349(9):859–866.**
  DOI 10.1056/NEJMoa022148｜PMID 12944571｜非 OA。Route: Europe PMC REST（DOI）。
- **[C-S23] PASS** Advanced Bladder Cancer (ABC) Meta-analysis Collaboration. *Neoadjuvant chemotherapy in invasive
  bladder cancer: update of a systematic review and meta-analysis of individual patient data.*
  **Eur Urol. 2005;48(2):202–205; discussion 205–206.** DOI 10.1016/j.eururo.2005.04.006｜PMID 15939524｜非 OA。
  Route: Europe PMC REST（DOI）。
- **[C-S24] PASS** International Collaboration of Trialists; MRC Advanced Bladder Cancer Working Party; EORTC, et al.
  *International phase III trial assessing neoadjuvant cisplatin, methotrexate, and vinblastine chemotherapy for
  muscle-invasive bladder cancer: long-term results of the BA06 30894 trial.* **J Clin Oncol. 2011;29(16):2171–2177.**
  DOI 10.1200/JCO.2010.32.3139｜PMID 21502557｜PMCID PMC3107740。Route: Europe PMC REST（DOI）。
- **[C-S25] PASS** Pfister C, Gravis G, Flechon A, et al. *Perioperative dose-dense methotrexate, vinblastine,
  doxorubicin, and cisplatin in muscle-invasive bladder cancer (VESPER): survival endpoints at 5 years in an open-label,
  randomised, phase 3 study.* **Lancet Oncol. 2024;25(2):255–264.** DOI 10.1016/S1470-2045(23)00587-9｜PMID 38142702｜
  非 OA。Route: Europe PMC REST（DOI）。
- **[C-S26] PASS** Powles T, Catto JWF, Galsky MD, et al. *Perioperative Durvalumab with Neoadjuvant Chemotherapy in
  Operable Bladder Cancer (NIAGARA).* **N Engl J Med. 2024;391(19):1773–1786.** DOI 10.1056/NEJMoa2408154｜
  PMID 39282910｜非 OA。NCT03732677。Route: Europe PMC REST（DOI）。
- **[C-S27] PASS** Vulsteke C, Adra N, Danchaivijitr P, et al. *Perioperative Enfortumab Vedotin and Pembrolizumab in
  Bladder Cancer (EV-303／KEYNOTE-905).* **N Engl J Med. 2026;394(13):1257–1269.** DOI 10.1056/NEJMoa2511674｜
  PMID 41707170｜非 OA。NCT03924895。Route: Europe PMC REST（DOI）。
- **[C-S29] PASS** *Perioperative treatment for muscle invasive bladder cancer in the era of immunotherapy.*
  **Ther Adv Urol. 2026;18:17562872261481954.** DOI 10.1177/17562872261481954｜PMID 42666617｜PMCID PMC13522676｜**OA**。
  Route: Europe PMC REST ＋ `/webservices/rest/PMC13522676/fullTextXML`。
  **用途：Galsky 五條準則的逐字轉述（原文 FAIL-1 拿不到）＋「up to 50% 不適合 cisplatin」＋VESPER 6 vs 4 療程的評語。**
- **[C-S30] PASS** Cahn DB, Handorf EA, Ghiraldi EM, et al. *Contemporary use trends and survival outcomes in patients
  undergoing radical cystectomy or bladder-preservation therapy for muscle-invasive bladder cancer.*
  **Cancer. 2017;123(22):4337–4345.** DOI 10.1002/cncr.30900｜PMID 28743162｜非 OA。Route: Europe PMC REST（DOI）。
- **[C-S31] PASS** He Q, Jiang Z, Jiang C, Tu X, Huang J. *Bladder preservation vs. radical cystectomy for T2N0M0:
  trends and survival outcomes from SEER.* **World J Urol. 2026;44(1):575.** DOI 10.1007/s00345-026-06683-9｜
  PMID 42606609｜非 OA。Route: Europe PMC REST（DOI）。
- **[C-S32] PASS** Rose TL, Deal AM, Ladoire S, et al. *Patterns of Bladder Preservation Therapy Utilization for
  Muscle-Invasive Bladder Cancer.* **Bladder Cancer. 2016;2(4):405–413.** DOI 10.3233/BLC-160072｜PMID 28035321｜
  PMCID PMC5181658｜**OA**。Route: Europe PMC REST（DOI）。
- **[C-S33] PASS** Matsukawa A, Yanagisawa T, Miszczyk M, et al. *Trimodality Therapy Versus Radical Cystectomy for
  Muscle-invasive Bladder Cancer: A Systematic Review and Meta-analysis of Matched Cohort Studies.*
  **Eur Urol Focus. 2025;11(2):374–385.** DOI 10.1016/j.euf.2024.11.003｜PMID 39578213｜非 OA。
  Route: Europe PMC REST（DOI）。
- **[C-S34] PASS** Robesti D, Micheli F, Rai SN, et al. *Trimodal treatment vs radical cystectomy for muscle-invasive
  bladder cancer: The neglected impact of informative censoring. A systematic review and meta-analysis.*
  **Crit Rev Oncol Hematol. 2025;214:104815.** DOI 10.1016/j.critrevonc.2025.104815｜PMID 40545069｜非 OA。
  Route: Europe PMC REST（DOI）。
- **[C-S35] PASS** Ditonno F, Veccia A, Montanaro F, et al. *Trimodal therapy vs radical cystectomy in patients with
  muscle-invasive bladder cancer: a systematic review and meta-analysis of comparative studies.*
  **BJU Int. 2024;134(5):684–695.** DOI 10.1111/bju.16366｜PMID 38622957｜非 OA。Route: Europe PMC REST（DOI）。
- **[C-S36] PASS** Sell A, Jakobsen A, Nerstrøm B, Sørensen BL, Steven K, Barlebo H. *Treatment of advanced bladder
  cancer category T2 T3 and T4a. A randomized multicenter study of preoperative irradiation and cystectomy versus radical
  irradiation and early salvage cystectomy for residual tumor. DAVECA protocol 8201. Danish Vesical Cancer Group.*
  **Scand J Urol Nephrol Suppl. 1991;138:193–201.** PMID 1785004｜無 DOI｜非 OA。Route: Europe PMC REST（TITLE）。
  **註：摘要在 250 字處被截斷（原始資料庫如此），可引用的只有截斷前的內容。**
- **[C-S37] PASS** **NCT03775265（SWOG/NRG S1806）**。官方名稱：*Phase III Randomized Trial of Concurrent
  Chemoradiotherapy With or Without Atezolizumab in Localized Muscle Invasive Bladder Cancer*。
  次要識別碼：S1806（SWOG／CTEP）、NCI-2018-03264。狀態 **ACTIVE_NOT_RECRUITING**，最後更新 2026-08-27；
  開始 2019-06-03；預計收案 475；主要終點 bladder intact event-free survival；**預計主要完成 2027-06-01**。
  Route: `https://clinicaltrials.gov/api/v2/studies/NCT03775265`，查詢日 2026-09-13。
- **[C-S38] PASS** **NCT04241185（MK-3475-992／KEYNOTE-992）**。狀態 **ACTIVE_NOT_RECRUITING**，最後更新 2026-04-29；
  開始 2020-05-19；預計收案 520；主要終點 bladder intact event-free survival；
  **預計主要完成 2027-01-31**、全試驗完成 2031-11-01。
  Route: `https://clinicaltrials.gov/api/v2/studies/NCT04241185`，查詢日 2026-09-13。
- **[C-S39] PASS** **衛生福利部中央健康保險署，《全民健康保險醫療服務給付項目及支付標準》現行給付項目（txt 檔）。**
  Route: 政府資料開放平臺 dataset 174451（`https://data.gov.tw/dataset/174451`）→ 其
  `resourceDownloadUrl`：`https://info.nhi.gov.tw/api/iode0000s01/Dataset?rId=A21030000I-D20020-002`，
  2026-09-13 實際下載（22,040,997 bytes，UTF-8），以 `^` 分隔欄位解析。
  本 brief 引用的每一個代碼、中文名稱、點數與生效起日皆由該檔逐筆比對。
  **全文檔搜尋結果（零筆者必須寫成零筆）：「膀胱癌」0 筆；「低分次」3 筆（36022B、36023B 乳癌，36024B 直腸癌）；
  「造口」48 筆但皆為處置項目、無耗材補助；「尿袋」2 筆且皆非補助。**
- **[C-S40] PASS** *Urothelial carcinoma: Perioperative considerations from top to bottom.*
  **CA Cancer J Clin. 2025;75(6):528–551.** DOI 10.3322/caac.70019｜PMID 40478748｜PMCID PMC12593283｜**OA**。
  Route: Europe PMC REST ＋ `/webservices/rest/PMC12593283/fullTextXML`。
  **用途僅限「SPARE 是唯一嘗試隨機化的試驗」這一句的佐證。
  ⚠ 該文轉述 SWOG S1011 的 90 天死亡數字有誤（見 ⚠ 第 7 點），該段一律改引 [C-S43]。**
- **[C-S41] PASS** Galsky MD, Valderrama BP, Maruzzo M, et al. *Enfortumab Vedotin and Pembrolizumab in Cisplatin-Eligible
  Bladder Cancer (KEYNOTE-B15/EV-304).* **N Engl J Med. 2026;395(4):338–348.** DOI 10.1056/NEJMoa2601486｜
  PMID 42485627｜非 OA。NCT04700124。Route: Europe PMC REST（DOI）。
  **用途：核對站上既有文章 `insight-bladder-ev-pembro` 的數字（已核對一致）。C2 只指路、不重述。**
- **[C-S42] PASS** *Treatment strategies for cisplatin-ineligible metastatic bladder cancer: Emerging therapies and
  future perspectives.* **Investig Clin Urol. 2025;66(6):471–481.** DOI 10.4111/icu.20250316｜PMID 41184140｜
  PMCID PMC12599474｜**OA**。Route: Europe PMC REST ＋ `/webservices/rest/PMC12599474/fullTextXML`。
  **用途：Galsky 準則的四條逐字轉述、其產生過程（120 位徵詢、65 份回收）、以及「lacks robust scientific validation」這一句。**
- **[C-S43] PASS** Lerner SP, Tangen C, Svatek RS, et al. *Standard or Extended Lymphadenectomy for Muscle-Invasive
  Bladder Cancer (SWOG S1011).* **N Engl J Med. 2024;391(13):1206–1216.** DOI 10.1056/NEJMoa2401497｜PMID 39589370｜
  PMCID PMC11599768｜**OA**。NCT01224665。Route: Europe PMC REST（ABSTRACT:"S1011"）。
- **[C-S44] PASS（僅限背景句）** Osanto S, Álvarez Gómez de Segura C. *Neoadjuvant and adjuvant treatments in
  muscle-invasive bladder cancer: Where are we?* **Arch Esp Urol. 2020;73(10):971–985.** PMID 33269716｜無 DOI｜非 OA。
  Route: Europe PMC REST（全文檢索）。**用途僅限「real-world adherence to NAC is low as ~40-50% of patients are unfit
  for cisplatin」這一句；其餘數字另有更好來源，不由本篇引。**

### FAIL / NOT-CITABLE（保留，讓寫作者知道查過什麼）

- **[C-F1] FAIL — Galsky 2011 原文拿不到。** Galsky MD, Hahn NM, Rosenberg J, et al. *A consensus definition of patients
  with metastatic urothelial carcinoma who are unfit for cisplatin-based chemotherapy.*
  **Lancet Oncol. 2011;12(3):211–214.** DOI 10.1016/S1470-2045(10)70275-8｜PMID 21376284。
  Route: Europe PMC REST 命中 1 筆，**`abstractText` 為空、非 OA、無 PMCID**，全文取不到。
  → **書目可引，五條準則的文字必須引 [C-S29]（五條完整）或 [C-S42]（四條），不可假裝讀過原文。**
- **[C-F2] FAIL — SPARE 關閉當時那篇反思文拿不到。** Huddart RA, Hall E, Lewis R, Birtle A, SPARE Trial Management Group.
  *Life and death of SPARE (selective bladder preservation against radical excision): reflections on why the SPARE trial
  closed.* **BJU Int. 2010;106(6):753–755.** DOI 10.1111/j.1464-410X.2010.09537.x｜PMID 20707796。
  Route: Europe PMC REST 命中 1 筆，**無摘要、非 OA、無 PMCID**。
  → **SPARE 為什麼關掉，一律引 [C-S2] 的 2017 年全文（Discussion 段可直接引），不可引這一篇的內容。**
- **[C-F3] FAIL — Zlotta 論文的公開批評與回覆，內容取不到。**
  ① Seisen T, Rouprêt M, Blanchard P. *Re: Zlotta et al.* **Eur Urol. 2024;85(1):e24.** DOI 10.1016/j.eururo.2023.07.019｜
  PMID 37659960。② Zlotta AR, Lajkosz K, Efstathiou JA. *Reply to Seisen et al.* **Eur Urol. 2024;85(1):e25–e26.**
  DOI 10.1016/j.eururo.2023.08.011｜PMID 37661552。③ Cigliola A, Mercinelli C, Patanè D, et al. *Re: Zlotta et al.*
  **Eur Urol. 2023;84(6):602–603.** DOI 10.1016/j.eururo.2023.06.026｜PMID 37451897。
  Route: Europe PMC REST 三筆皆**無摘要、非 OA**。
  → **可寫「這篇論文發表後在期刊上有公開的批評與作者回覆」並附書目，但不可轉述任何論點。**
- **[C-F4] FAIL — 台灣癌症登記（膀胱癌發生數、期別分布、性別年齡）。**
  Route:（a）`https://www.hpa.gov.tw/` 與 `https://www.hpa.gov.tw/Pages/ashx/GetFile.ashx?...`
  **curl 回傳 HTTP 000（TLS 連線失敗）**，與 RESEARCH-COMMON 的預期一致；
  （b）改走 data.gov.tw dataset 6399「癌症發生統計」，其唯一下載連結仍指向 hpa.gov.tw，**同樣失敗**；
  （c）mohw.gov.tw 統計處頁面只到目錄層，無膀胱癌期別資料。
  → **gap。文章寫「查不到」或交由 A／E 組；不可用媒體轉述的數字。**
- **[C-F5] FAIL — nhi.gov.tw 網頁版條文。** `https://www.nhi.gov.tw/ch/cp-1649-...` 與 `/ch/np-1649-1.html`
  皆回 **HTTP 403（Cloudflare）**。→ 改走 [C-S39] 的官方開放資料 API 檔，已成功。
- **[C-F6] NOT-CITABLE — NCCN。** 依 SPEC §四與 RESEARCH-COMMON：專業版抓取回 403，**本專題不引 NCCN**。本組未嘗試。
- **[C-F7] FAIL — 獨立的 ASTRO 膀胱癌臨床指引。** Europe PMC 以 `TITLE:"bladder" AND TITLE:"ASTRO" AND TITLE:"Guideline"`
  搜尋僅命中 AUA/ASCO/ASTRO/SUO 2017 聯合指引一筆；`astro.org` 的臨床指引頁回 **HTTP 403**。
  → **沒有可引的獨立 ASTRO 膀胱指引。C4 的第三個指引用 NICE NG2。**
- **[C-F8] FAIL — 台灣的三聯療法使用率／膀胱保留率。** Europe PMC 未命中任何台灣族群的三聯療法使用率研究；
  健保支付標準檔「膀胱癌」零筆。→ **gap。「台灣做得太少」不可帶任何數字，見 ⚠ 第 6 點。**
- **[C-F9] FAIL — KEYNOTE-B15/EV-304 的「因副作用中途停藥 35.2% vs 11.1%」。**
  站上既有文章引的是 ASCO Post 的轉述；**NEJM 摘要（[C-S41]）裡看不到這兩個數字**，全文非 OA 取不到。
  → **C2 不得重述停藥率。要寫 EV＋pembro 的代價，改用 EV-303 摘要裡看得到的
  「≥3 級藥物相關不良事件 45.5%」[C-S27]，或 KEYNOTE-B15 摘要裡的「≥3 級不良事件 75.7% vs 67.2%」[C-S41]。**
- **[C-F10] FAIL — 重大傷病項次逐字條文。** law.moj.gov.tw 以 PCode L0060004／L0060005／L0060012／L0060023／L0060008
  逐一嘗試，均非「全民健康保險保險對象免自行負擔費用辦法」。
  → **gap。寫「問醫務課／個管師」，或由 A 組補。**
- **[C-F11] FAIL — 造口耗材補助與身心障礙輔具補助的逐字條文。** 健保支付標準檔內僅有處置項目（見 [C-S39] 搜尋結果），
  補助屬社政系統，本組未取得官方條文。→ **gap，寫「問醫務課／個管師／社工」。**
- **[C-F12] 註記（非來源）** — CA Cancer J Clin 2025 [C-S40] 對 SWOG S1011 的 90 天死亡數字轉述有誤
  （該文寫 16/292 vs 9/300；NEJM 原文 [C-S43] 為 19 人 7% vs 7 人 2%）。**一律以 NEJM 原文為準。**

---

## 附：本 brief 未涵蓋、但 C 組文章會碰到而應由他組提供的項目

- 非肌肉侵犯型的風險分層、卡介苗、NMIBC 追蹤時程（B 組；C5 不得代寫）
- 名詞與兩條分界線的解釋（A3；C 組各篇不重解釋）
- 第一次刮除的品質指標與再刮除（A2；C4 只引「重新刮除在 >50% 會發現殘餘病灶」並指路）
- 影像分期（A4）
- 轉移性第一線與基因檢測、健保藥品給付逐字條文（D 組；C2 的給付段落須等 D 組）
- 上泌尿道（E1；本 brief 所有數字**皆為膀胱**，不得外推）
- 造口與日常生活（E3；C3 只寫三種改道的日子輪廓與併發症量級，不寫照護教學）
