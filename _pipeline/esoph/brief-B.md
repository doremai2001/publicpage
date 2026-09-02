# Brief B — 食道癌專題「每種治療的實證效益」（B1–B5）

研究員：Group B｜查證日期：2026-09-02｜期刊書目全部經 Europe PMC REST 逐筆核對（title／journal／year／volume(issue)／pages／DOI／PMID／isOpenAccess）；**Key facts 的每一個數字都出自該筆記錄的 abstractText 或可取得的 OA 全文**（JES 2022 指引全文為 OA，經 fullTextXML 抓取）；試驗狀態經 ClinicalTrials.gov API v2；台灣官方條文經直接下載 PDF／ODS 後 pdftotext／解壓全文檢索。
引用規則：**只有標 PASS 的來源可以進正文引用。** FAIL 條目保留，讓寫作者知道哪些話只能寫「查不到可引用的來源」。
沿用 nextgen 專題已查證項目（ASTRO 質子模型政策、健保質子三項公報、高雄長庚收費頁、衛福部粒子設備頁）已於 2026-09-02 重新 curl 確認 HTTP 200 並重新抓取內容。

---

## ⚠ 與 SPEC 假設不同形狀的事（動筆前必讀）

1. **根治性化放療加免疫，三個大型第三期已經讀出，兩個負、一個「主要終點負但單藥臂正」——不是「結果未知」。**
   - KEYNOTE-975（pembrolizumab 同步＋鞏固，n=703，鱗癌＋腺癌）：Merck 2026 年第一季財報（SEC 8-K 附件）原文：「KEYTRUDA plus dCRT did not show a statistically significant improvement in the primary endpoint of EFS」[S32]。ClinicalTrials.gov 狀態 COMPLETED（2026-06-23），無論文[S33]。
   - RATIONALE-311（tislelizumab 同步＋鞏固，中國鱗癌，n=370）：ClinicalTrials.gov 已張貼結果——PFS 中位 29.0 vs 28.9 個月，**HR 0.92（95% CI 0.68–1.25，p=0.30）**；OS HR 1.10（0.83–1.46）[S36]。負的。
   - SKYSCRAPER-07（dCRT 後鞏固，n=760，鱗癌）：Ann Oncol 2026 正式發表——**主要終點（atezolizumab＋tiragolumab vs 安慰劑）未達**（PFS HR 0.82，p=0.095；OS HR 0.91），但 **atezolizumab 單藥臂 vs 安慰劑 OS HR 0.69（0.52–0.91，descriptive p=0.0085）**，作者結論「did not meet the primary endpoint」同時寫「clinically meaningful improvements … with atezolizumab plus placebo」[S34]。這是「statistically 負、但留下一個訊號」的形狀，寫作要兩面都寫。
   - KUNLUN（durvalumab）：AstraZeneca 2026 Q1 臨床試驗附件寫「Data anticipated: 2027」[S39]；ESCORT-CRT（camrelizumab）登錄狀態 UNKNOWN、2021-09 後未更新、無讀出[S37]。
2. **台灣健保對食道鱗癌的免疫給付，形狀跟 SPEC 假設不同：**（a）**nivolumab 術後輔助（CheckMate 577 那格）在現行《藥品給付規定》第 9 節 9.69 條**沒有**對應條文**——查到的是「第二線單用」（113/4/1 起）與「**第一線併化療」（115/2/1 起，2026-02-01 生效，新增）**，兩者 PD-L1 門檻皆為 **TC≧1%**[S43][S44][S45]；（b）**pembrolizumab 在食道鱗癌第一、二線的表格欄位都寫「本藥品尚未給付於此適應症」**[S43]。也就是：SPEC 要查的「pembrolizumab／nivolumab 轉移第一線」——健保只有 nivolumab；「nivolumab 術後輔助」——健保零筆。給付期限：自初次處方起 2 年、事前審查、每次申請 12 週、ECOG≦1[S43]。
3. **CONCORDE／PRODIGE 26 至今只有 2021 年 ASTRO 會議摘要（IJROBP 增刊），Europe PMC 查無 2022–2026 年正式論文**[S5][FAIL-1]。可以引摘要的數字（2 年 LRPFS 42.7% vs 43.8%，OS HR 1.14），但要標「會議摘要層級」。中國 50 對 60 Gy 試驗則有 2022 CCR 主論文＋**2026 年長期追蹤（中位 99.5 個月，8 年 LRPFS 32.7% vs 36.3%，HR 1.06）**[S6][S7]，比 SPEC 預期的更完整。
4. **「放療中斷對鱗癌局部控制的影響」在食道癌自身資料上是兩面的：** 1994 年放療單獨治療時代的日本資料顯示每延長一天局部控制掉 2.3%[S13]；但 2025 年一篇 541 人的同步化放療回溯（中國）顯示總療程延長對 OS／LRFS 沒有影響[S14]。頭頸鱗癌的證據（DAHANCA 6&7 隨機試驗、Bese 綜述「每中斷一天局部控制降 1.4%」）比較硬，但必須標明是類推[S15][S16]。紅線 5 的引用要用「食道癌自身資料在同步化放療時代並不一致＋頭頸鱗癌類推」的寫法，不能寫成「已證明中斷一天就掉幾 %」。
5. **手術術式比較有新的隨機資料**：Ivor Lewis vs McKeown 微創食道切除在鱗癌的單中心 RCT（n=272，2026 Surg Endosc）：吻合口滲漏 8.1% vs 16.9%、狹窄 6.6% vs 22.8%、喉返神經損傷 0 vs 3.7%，PFS 無差異[S61]；荷蘭 ICAN 試驗（胸內 vs 頸部吻合）滲漏 12.3% vs 34.1%[S59]。SPEC 寫的「三種術式與適用位置」可以升級成「同一段食道，接在胸腔裡比接在頸部滲漏少，這有隨機資料」。
6. **CheckMate 577 的整體存活正式論文查不到**：Europe PMC 只查到荷蘭全國真實世界配對研究（2026 IJC），其引言寫 CheckMate 577 是「a significant disease-free and a **non-significant overall survival benefit**」[S22]。OS 最終分析只能用這句轉述，不能寫 HR。
7. **ESD 在台灣健保支付標準裡沒有獨立項目**：現行支付標準全表檢索「黏膜下剝離」零筆；有的是 **72050B「內視鏡黏膜切除術」8,199 點**，適應症含「早期胃腸道癌症（包括食道…）」[S76]。文章不可寫「ESD 有健保」或「沒健保」，寫「內視鏡黏膜切除術有給付項目，ESD 本身的計價方式問你的腸胃科與醫務課」。

---

## B1 `ec-crt-dose`〈化放療那五到六週，劑量為什麼不是越高越好〉【紅線 5 引用主場之一】

### Key facts

**為什麼是「化放療」而不是「放療」——RTOG 85-01**
- Herskovic 1992（NEJM，n=121 隨機，鱗癌＋腺癌，胸段）：5-FU/cisplatin＋**50 Gy** vs **64 Gy 放療單獨**。中位存活 12.5 vs 8.9 個月；2 年存活 38% vs 10%（p<0.001）；合併組局部與遠端復發都較少；代價：嚴重／危及生命副作用 44%／20%（合併）vs 25%／3%（放療單獨）[S1]。
- Cooper 1999（JAMA 長期）：隨機部分 **5 年存活 26%（合併）vs 0%（放療單獨）**；後續非隨機世代 14%。「病灶持續存在」是最常見失敗模式：合併組 26%（34/130）vs 放療單獨 37%（23/62）。化療能照計畫完成者只有 68%（89/130）；危及生命毒性 10% vs 2%[S2]。→ 這裡就已經埋下主題：**放療劑量比較低（50 Gy）的那一臂反而活得久，因為多了化療**。

**劑量升級的五個隨機試驗（全部「加量沒有更好」）——fig-ec-dose-trials 的數據**

| 試驗 | 族群 | 標準臂 | 高劑量臂 | 主要結果 | 來源 |
|---|---|---|---|---|---|
| INT 0123／RTOG 94-05（Minsky 2002） | 218 可分析，鱗癌＋腺癌，T1–4 N0/1，cis/5-FU | 50.4 Gy | 64.8 Gy | 中位存活 18.1 vs 13.0 個月、2 年 40% vs 31%、局部失敗／持續 52% vs 56%，皆無顯著差異；高劑量臂 11 例治療相關死亡 vs 2 例（其中 7 例死於 ≤50.4 Gy 時）；期中分析後停止 | [S3] |
| ARTDECO（Hulshof 2021） | 260 人，荷蘭，鱗癌 61%／腺癌 39%，每週 carboplatin/paclitaxel | 50.4 Gy | 61.6 Gy（原發腫瘤） | 3 年局部 PFS 70% vs 73%（NS）；鱗癌 75% vs 79%、腺癌 61% vs 61%；G4／G5 毒性 12%／5% vs 14%／10%（p=0.15） | [S4] |
| CONCORDE／PRODIGE 26（Crehange 2021，**會議摘要**） | 217 人，法國，鱗癌 88%，FOLFOX | 50 Gy/25 fx | 66 Gy/33 fx | 2 年 LRPFS 42.7% vs 43.8%（HR 1.03）；中位 OS 25.2 vs 23.5 個月（HR 1.14，p=0.44）；毒性死亡 4.6% vs 6.7% | [S5][S20] |
| 中國多中心 50 vs 60 Gy（Xu 2022） | 319 可分析，**全鱗癌**，IIA–IVA，每週 docetaxel/cisplatin | 50 Gy | 60 Gy | 3 年局部區域 PFS 48.4% vs 49.5%（HR 1.00，p=0.98）；3 年 OS 52.7% vs 53.1%（HR 0.99）；**G3+ 放射性肺炎 60 Gy 組較高（p=0.03）** | [S6] |
| 同試驗長期（Cheng 2026） | 同上，中位追蹤 99.5 個月 | | | 5／8 年 LRPFS：50 Gy 43.3%／36.3% vs 60 Gy 41.8%／32.7%（HR 1.06，p=0.70）；OS、PFS、DMFS、失敗型態皆無差異 | [S7] |

- 日本食道學會 2022 指引自己的話（OA 全文）：INT0123「revealed that while the survival was not prolonged any further, higher toxicity was obtained in the 64.8 Gy group」；日本傳統標準是 cisplatin+5-FU＋**60 Gy**（JCOG0303），但 JCOG0909 把劑量改成 1.8 Gy × 28＝**50.4 Gy**，理由原文：「in an attempt to reduce the risk of adverse events and the risk associated with salvage esophagectomy」，完全反應率 59%；指引結論「definitive chemoradiotherapy (≥ 50 Gy) should be considered in patients who are unable to tolerate surgery, refuse surgery, or wish to receive esophagus-preserving therapy」[S18][S19]。→ 日本從 60 走回 50.4 這件事本身是好素材。

**化療組合**
- **FOLFOX vs cisplatin/5-FU**（PRODIGE5/ACCORD17，Conroy 2014，n=267，鱗癌／腺癌／腺鱗癌，50 Gy）：中位 PFS 9.7 vs 9.4 個月（HR 0.93，p=0.64）——**沒有更好**；毒性死亡 1 vs 6（p=0.066）；FOLFOX 組感覺異常 47% vs 2%、神經病變 18% vs 1% 較多；cis/5-FU 組肌酸酐上升 12% vs 3%、黏膜炎 32% vs 27%、掉髮 9% vs 2% 較多。作者：「FOLFOX might be a more convenient option」[S8]。
- **paclitaxel/5-FU vs cisplatin/5-FU**（ESO-Shanghai 1，Chen 2019 JCO，n=436，**全鱗癌**，61.2 Gy）：3 年 OS 55.4% vs 51.8%（HR 0.905，p=0.448）——沒有更好；PF 組 G3+ 貧血、血小板低、食慾差、噁心嘔吐、疲倦較少，但 G3+ 白血球低下、放射性皮膚炎、**放射性肺炎較多**[S9]。
- **carboplatin/paclitaxel vs cisplatin/5-FU 在根治性化放療**：**沒有隨機試驗**。荷蘭多中心回溯（Honing 2014，n=102）：OS 中位 16.1（cis/5-FU）vs 13.8（carbo/pacli）個月，HR 0.97（p=0.879）無差異；**完成率 82% vs 57%（p=0.010）**；G3+ 血液／非血液毒性 4%／18%（carbo/pacli）vs 19%／38%（cis/5-FU）[S10]。ARTDECO 兩臂都用每週 carbo/pacli（CROSS 方案）並完成 94% 放療、85% 至少五次化療[S4]。
- 術前（CROSS 方案 vs FOLFOX）的隨機第二期 PROTECT-1402（n=106）：登錄 COMPLETED（2024-02-09），**hasResults=False、Europe PMC 查無結果論文**，只有 2016 年 protocol[S11][S12][FAIL-2]。不可寫它的結果。
- 奧地利 2026 年全國問卷（OA）：鱗癌根治性化放療 69% 中心首選每週 carbo/pacli；根治性中位處方劑量 57.7 Gy（50.4–66），顯示「指引說 50.4，實務常往上加」的落差是國際現象[S46]。

**放療中斷／總療程時間（紅線 5 的證據面，寫法要誠實）**
- **食道癌自身資料**
  - Nishimura 1994（京都，n=88，**放療單獨**時代，I–III 期）：以總療程時間為橫軸，局部控制的回歸斜率 **−2.3 ± 0.5%／天（p<0.025）**，即每多一天局部控制掉 2.3%；加速超分割組 1 年局部控制 47% vs 常規 22%[S13]。
  - Xiang 2025（西安，n=541，**鱗癌同步化放療**，2008–2024，OA）：中位總療程 43 天、超出理論最短 4 天；多變項分析**總療程延長與等待時間對 OS、LRFS、DMFS、PFS 都沒有影響（p>0.05）**；只有 T1–2 者開始放療前等待 ≥72 天預後較差[S14]。→ 反方向資料，**必列**。
- **頭頸鱗癌類推（標明是類推）**
  - DAHANCA 6&7（Overgaard 2003 Lancet，n=1,476 隨機，放療單獨）：同劑量同次數，每週 6 次 vs 5 次，中位總療程 39 vs 46 天；**5 年局部區域控制 70% vs 60%（p=0.0005）**，原發腫瘤控制 76% vs 64%；疾病特異存活 73% vs 66%，OS 無差異；急性反應較多但短暫[S16]。
  - Bese 2007 綜述（IJROBP）：頭頸癌證據最強，「even a 1-day interruption resulted in a decrease in the local control rate by 1.4%」；建議竭力維持排程，中斷需補償[S15]。
- 寫法：「食道鱗癌跟頭頸鱗癌是同一種細胞，腫瘤在中斷期間會加速再增殖的機轉是一樣的；食道癌自己的資料在放療單獨時代看得到每天 2.3% 的損失，在同步化放療時代有一篇看不到——所以我不會跟你說中斷一天就掉幾個百分點，但我會跟你說沒有任何資料顯示中斷是安全的。」

**IMRT 相對 3D-CRT（「光子 IMRT 已經很好」的證據面，B5 共用）**
- Lin 2012（MD Anderson，n=676，3D-CRT 413／IMRT 263，Ib–IVa，化放療，反機率加權）：OS 校正 HR 0.72（IMRT vs 3D，p<0.001）；死亡 72.6%（3D）vs 52.9%（IMRT）；局部區域復發 3D 較多（p=0.0038）；癌症特異死亡與遠端轉移無差異；**心因性死亡累積發生率 3D 較高（p=0.049）；未記錄原因死亡 5 年 11.7% vs 5.4%（p=0.0029）**——作者解讀為非癌症死亡（心肺）差異[S17]。回溯性、單中心，不可寫成隨機證據。
- Wang 2013（MDACC，n=444，三合一）：肺部併發症 25%、腸胃 23%；3D-CRT vs IMRT 肺部併發症 OR 2.018（1.104–3.688）、腸胃 OR 1.704；**差異可完全由平均肺劑量（MLD）解釋**[S79]。
- Lin 2017（三家學術中心，n=580，術前化放療）：住院天數 3D 13.2 天、IMRT 11.6 天、質子 9.3 天（p<0.0001）；90 天術後死亡 4.2%／4.3%／0.9%（p=0.264，無顯著差異）[S60]。

### 反方向的資料（誠實必列）
- 每一個劑量試驗都是「沒有更好」而非「較差」；ARTDECO 高劑量臂 G5 死亡 10% vs 5% 未達顯著（p=0.15）[S4]；CONCORDE 作者自己寫「66 Gy is not more toxic than 50 Gy」[S5]。不可寫成「加量會害死人」。
- Xiang 2025 對「中斷有害」是反證[S14]。
- ESO-Shanghai 12 正在用 PET 反應分層測 61.2 vs 50.4 Gy（NCT03790553，只有 protocol）——「加量」這題還沒完全關門（protocol 論文 PASS、無結果）[S47b]。

### Claim ceiling
- **可寫**：「五個隨機試驗（INT0123、ARTDECO、CONCORDE、中國 50/60、其長期追蹤），沒有一個顯示加到 60–66 Gy 比 50–50.4 Gy 控制得更好；其中兩個看到高劑量臂較多治療相關死亡或 G3+ 肺炎」；「RTOG 85-01 裡 50 Gy 加化療活得比 64 Gy 純放療久」；「日本自己把標準從 60 Gy 改成 50.4 Gy 的理由是減少副作用與救援手術風險」；「FOLFOX、paclitaxel/5-FU 都沒有打贏 cisplatin/5-FU，差別在副作用種類」；「carbo/pacli 對 cis/5-FU 在根治性化放療沒有隨機比較，回溯資料完成率較高、存活看不出差別」；「總療程拖長在頭頸鱗癌隨機試驗裡局部控制差 10 個百分點；食道癌自己的資料不一致」。
- **不可寫**：「50 Gy 已證明等於 60 Gy」（是「未證明更好」，各試驗 CI 寬）；「中斷一天局部控制掉 X%」寫成食道癌事實（Nishimura 是放療單獨、1994；Bese 是頭頸）；「IMRT 已證明降低心臟死亡」（Lin 2012 回溯，原文說 most deaths were undocumented）；任何暗示可以自己少做幾次或多做幾次的句子。

### Caveats／safety notes
- 中國 50/60 試驗與 ESO-Shanghai 1 用的是 docetaxel/cisplatin 或 paclitaxel/5-FU 週療，跟台灣常見 cis/5-FU 或 carbo/pacli 不同，引用時帶方案名。
- CONCORDE 只有摘要層級，正文要寫「會議摘要」。
- 「什麼情況我會主動幫你停」的臨床規則屬 C2；本篇只提供「為什麼不該自己停」的證據。

### 台灣端
- 健保放療支付標準的 IMRT 相關項目存在於支付標準全表（如 36015B 電腦治療規劃—複雜，說明文字含「強度調控放射治療」）[S76]；**食道癌 IMRT 給付條件的專屬條文本 brief 未逐條查證——gap**，正文不寫「IMRT 有／沒有健保」的具體條件，寫「IMRT 在台灣是常規光子技術，給付細節問醫務課」。
- 台灣鱗癌根治性化放療的處方劑量實務：**無官方資料——gap**。

### 給繪圖組的數字（fig-ec-dose-trials）
五臂對照：INT0123 50.4 vs 64.8（2 年 OS 40% vs 31%）[S3]；ARTDECO 50.4 vs 61.6（3 年 LPFS 70% vs 73%）[S4]；CONCORDE 50 vs 66（2 年 LRPFS 42.7% vs 43.8%，摘要）[S5]；中國 50 vs 60（3 年 LRPFS 48.4% vs 49.5%；8 年 36.3% vs 32.7%）[S6][S7]；起點 RTOG 85-01 50 Gy+化療 vs 64 Gy 放療（5 年 26% vs 0%）[S2]。方向標籤：全部「加量沒有更好」，其中 INT0123 標「高劑量臂治療相關死亡 11 vs 2」、中國試驗標「G3+ 肺炎較多」。

---

## B2 `ec-immunotherapy`〈免疫治療到底幫了誰〉【紅線 2】

### Key facts

**格一：術後（三合一之後仍有殘存腫瘤）——CheckMate 577**
- Kelly 2021 NEJM（n=794，2:1，**R0 切除、II–III 期、術前化放療後有殘存病理病灶**，食道或胃食道接合部，鱗癌＋腺癌）：nivolumab 1 年 vs 安慰劑；**中位 DFS 22.4 vs 11.0 個月，HR 0.69（96.4% CI 0.56–0.86，p<0.001）**；治療相關 G3/4 不良事件 13% vs 6%；因不良事件停藥 9% vs 3%[S21]。**主要終點是 DFS，不是 OS。**
- OS：Europe PMC 查無最終 OS 論文[FAIL-4]。可引的轉述：荷蘭全國真實世界配對研究（Verhoeven 2026 IJC，OA）引言寫「The Checkmate-577 trial showed a significant disease-free and a **non-significant overall survival benefit**」[S22]。同篇真實世界資料（n=311 對 311 配對，2020–2023）：2 年 OS 66.8% vs 58.8%，HR 0.75（0.60–0.97，p=0.024），作者自註「follow-up and the number of events are still limited… interpreted with caution」[S22]。
- 日本食道學會 2022 指引（OA）：對「術前化放療＋根治切除後未達 pCR」者「strong evidence to recommend postoperative nivolumab therapy, regardless of the histologic type or tumor expression level of PD-L1」（共識率 81%，證據 A），並自列四個保留：日本族群療效未報告、術前化療者未建立、**達 pCR 者療效未建立**、（第四點原文截斷）[S18]。
- **台灣健保：術後輔助 nivolumab 零條文**（見台灣端）。

**格二：轉移／無法治癒的第一線——PD-L1 分層**
- KEYNOTE-590（Sun 2021 Lancet，n=749，pembrolizumab＋cis/5-FU，鱗癌＋腺癌；鱗癌比例不在摘要，勿寫）：**鱗癌且 CPS≥10** 中位 OS 13.9 vs 8.8 個月（HR 0.57）；鱗癌全體 12.6 vs 9.8（HR 0.72）；CPS≥10 全體 13.5 vs 9.4（HR 0.62）；全隨機族群 12.4 vs 9.8（HR 0.73）；G3+ 治療相關不良事件 72% vs 68%[S23]。5 年更新（Metges 2025 ESMO Open，OA，中位追蹤 58.8 個月）：全族群 OS HR 0.72（0.62–0.84）、**5 年存活 10.6% vs 3.0%**；PFS HR 0.64；作者結論支持「CPS ≥1」為標準[S24]。
- CheckMate 648（Doki 2022 NEJM，n=970，**全鱗癌**，三臂）：**TPS≥1%**：nivo+化療 OS 15.4 vs 9.1 個月（HR 0.54）、nivo+ipi 13.7 vs 9.1（HR 0.64）；全族群：13.2 vs 10.7（HR 0.74）、12.7 vs 10.7（HR 0.78）；PFS 只有 nivo+化療在 TPS≥1% 顯著（HR 0.65），nivo+ipi 沒有；G3/4 治療相關不良事件 47%／32%／36%[S25]。5 年追蹤（Kato 2026 Ann Oncol）：TPS≥1% OS HR 0.62／0.62；全族群 HR 0.77／0.77；nivo+ipi 的 PFS 仍無差異（HR 1.03）；G3/4 49%／33%／37%[S26]。
- 中國四個鱗癌第一線試驗（全部 OS 顯著，安慰劑對照，paclitaxel/cisplatin 底）：ESCORT-1st（camrelizumab，n=596）OS 15.3 vs 12.0，HR 0.70[S27]；JUPITER-06（toripalimab，n=514）PFS HR 0.58、OS HR 0.58[S28]；ORIENT-15（sintilimab，OA）全體 OS 16.7 vs 12.5，HR 0.63[S29]；RATIONALE-306（tislelizumab，全球）OS 17.2 vs 10.6，HR 0.66[S30]。→ 這四種藥在台灣的給付狀態本 brief 未查到條文（第 9 節 9.69 列出的藥品是 atezolizumab／nivolumab／pembrolizumab／avelumab／ipilimumab／durvalumab／tremelimumab／cemiplimab／dostarlimab）[S43]。
- 第二線單藥：ATTRACTION-3（Kato 2019 Lancet Oncol，n=419，鱗癌，含台灣中心，不分 PD-L1）：nivolumab vs 化療 OS 10.9 vs 8.4 個月，HR 0.77（0.62–0.96，p=0.019）；G3/4 治療相關 18% vs 63%[S31]。→ 對應台灣健保「第二線單用」條文。
- ASCO 指引原文：2023 版「For patients with esophageal squamous cell carcinoma and PD-L1 tumor proportion score ≥ 1%, nivolumab plus CT, or nivolumab plus ipilimumab is recommended; for patients with esophageal squamous cell carcinoma and PD-L1 CPS ≥ 10, pembrolizumab plus CT is recommended」[S41]；2026 更新版：「Immunotherapy with doublet chemotherapy is recommended for patients with pMMR/MSS HER2-negative gastroesophageal adenocarcinoma or squamous cell carcinoma and **PD-L1 expression ≥1; patients with higher PD-L1 expression are more likely to benefit**」；第二線「immunotherapy for PD-L1 ≥1 esophageal squamous cell carcinoma after first-line combination chemotherapy without immunotherapy」[S40]。ESMO 2022 指引存在（Ann Oncol 2022;33:992–1004）但原文措辭取不到[S42][FAIL-5]。

**格三：根治性化放療加免疫——結果照查到的寫**

| 試驗 | 設計 | 狀態／結果 | 來源 |
|---|---|---|---|
| KEYNOTE-975（pembrolizumab 同步 dCRT＋鞏固，n=703，鱗癌＋腺癌，雙盲） | 主要終點 EFS、OS | **負**：Merck SEC 8-K（2026-04-30）「did not show a statistically significant improvement in the primary endpoint of EFS in certain patients with locally advanced unresectable esophageal carcinoma」；CT.gov COMPLETED 2026-06-23，無論文 | [S32][S33] |
| RATIONALE-311（tislelizumab 同步 cis/paclitaxel＋50.4 Gy，再鞏固至 2 年，n=370，中國鱗癌） | 主要終點 PFS（BIRC） | **負**：PFS 中位 29.0 vs 28.9 個月，HR 0.92（0.68–1.25，p=0.3016）；OS 39.2 vs 48.2 個月，HR 1.10（0.83–1.46）；ORR 27.6% vs 38.9%（CT.gov 張貼結果，資料截止 2025-01-08） | [S36] |
| SKYSCRAPER-07（dCRT 後鞏固 atezolizumab±tiragolumab vs 安慰劑，1:1:1，n=760，鱗癌，28 國 166 中心） | 階層檢定：atezo+tira vs 安慰劑 PFS→OS，再 atezo 單藥 OS | **主要終點未達**：atezo+tira PFS HR 0.82（0.65–1.03，p=0.0947）、OS HR 0.91（0.70–1.18）；**atezo 單藥 vs 安慰劑 OS HR 0.69（0.52–0.91，descriptive p=0.0085）、PFS HR 0.74**；治療相關不良事件 74.8%／65.2%／55.4%，治療相關死亡 1.2%／0.8%／1.6% | [S34][S35] |
| KUNLUN（durvalumab 同步 dCRT＋鞏固，n=640，鱗癌） | 主要終點 PFS | **未讀出**：CT.gov ACTIVE_NOT_RECRUITING，主要完成估 2027-06；AZ 2026 Q1 附件「Data anticipated: 2027」 | [S38][S39] |
| ESCORT-CRT（camrelizumab 同步 dCRT，n=396，中國鱗癌） | 主要終點 PFS（IRC） | **未讀出**：CT.gov 狀態 UNKNOWN，最後更新 2021-09-16；Europe PMC 查無結果 | [S37] |

- 2026 年一篇 OA 綜述仍把 KEYNOTE-975／RATIONALE-311／ESCORT-CRT 寫成「results eagerly awaited」並把 SKYSCRAPER-07 寫成「reported positive survival outcomes」[S46b]——這說明連專業文獻都有時間差，正文要以 [S32][S34][S36] 的原始資料為準，**不引該綜述的結論句**。

### 反方向的資料（誠實必列）
- KEYNOTE-590 全族群、CheckMate 648 全族群都顯著（HR 0.72–0.77），「PD-L1 低就沒用」也是超過——正確寫法是「PD-L1 越高獲益越大，低表現族群的獲益較小且信賴區間較寬」（ASCO 2026 原文）[S40][S24][S26]。
- SKYSCRAPER-07 的 atezolizumab 單藥臂 OS HR 0.69 是真的訊號，但它在階層檢定裡排第三、p 值為 descriptive；寫成「鞏固免疫已證明有效」是超過，寫成「全負」也不誠實[S34]。
- 荷蘭真實世界 OS HR 0.75 支持 CheckMate 577，但作者自己說事件數少[S22]。

### Claim ceiling
- **可寫**：「術後 nivolumab 的證據只在『術前化放療＋手術後仍有殘存腫瘤』的人身上，主要終點是無病存活，整體存活到目前為止沒有統計顯著（試驗原文），真實世界看到差 8 個百分點但事件數少」；「轉移第一線加免疫，鱗癌 PD-L1 TPS≥1%（nivolumab）或 CPS≥10／≥1（pembrolizumab）獲益最清楚，5 年存活從 3% 到 10.6%（KEYNOTE-590 全族群）」；「根治性化放療同步加免疫：pembrolizumab（KEYNOTE-975）、tislelizumab（RATIONALE-311）兩個第三期都沒有達到主要終點；化放療後鞏固（SKYSCRAPER-07）主要終點沒達，單用 atezolizumab 那一臂留下一個存活訊號；durvalumab（KUNLUN）2027 才讀出」；「健保目前給付的是 nivolumab 第一線併化療與第二線單用，都要 PD-L1 TC≧1%、事前審查、最多 2 年」。
- **不可寫**：「每個食道癌病人都應該用免疫」；「化放療加免疫是新標準」；「pembrolizumab 有健保」（表格寫「本藥品尚未給付於此適應症」）；「術後免疫有健保」（零條文）；把 SKYSCRAPER-07 寫成陽性試驗；把 CheckMate 577 寫成「延長存活」。
- 中國四藥（camrelizumab／toripalimab／sintilimab／tislelizumab）：可寫「在中國鱗癌試驗都顯示存活延長」，**不可寫台灣可用性或給付**（未查證）。

### Caveats／safety notes
- 免疫相關不良事件（肺炎、肝炎、內分泌）的處置屬 care-fever／C3 一句指路；本 brief 只提供試驗層級的 G3/4 比率。
- CheckMate 577 收案含腺癌與胃食道接合部；鱗癌次族群數字**不在摘要**，不可寫。
- KEYNOTE-590 的鱗癌比例不在摘要，不寫。

### 台灣端（B2 主場，逐字可引）
- 來源：健保署《藥品給付規定》第 9 節抗癌瘤藥物現行合訂本 PDF（102 頁，檔案 ModDate 2026-08-21）[S43]，及 115/2/1 生效修訂對照表[S44]、113/4/1 生效修訂對照表[S45]。
- 9.69 免疫檢查點抑制劑 1.（單獨使用）(10)：「**食道鱗狀細胞癌：限 nivolumab 用於曾接受合併含鉑及 fluoropyrimidine 化學治療之後惡化的無法切除晚期或復發性食道鱗狀細胞癌病人。(113/4/1、113/6/1、115/2/1)**」[S43]
- 9.69 2.（併用其他藥品）(8)：「**食道鱗狀細胞癌：限 nivolumab 與 fluoropyrimidine 及 cisplatin 或 oxaliplatin 併用，用於無法接受化學放射性治療或手術切除等治癒性治療之晚期或轉移性食道鱗狀細胞癌成人病人的第一線治療。(115/2/1)**」[S43][S44]——2026-02-01 生效的新增條文。
- 生物標記表：「食道鱗狀細胞癌第一線用藥（併用化療）P102」與「第二線用藥（單用）P101」，nivolumab 欄 **TC≧1%**（Dako 28-8 或 Ventana SP263），pembrolizumab／atezolizumab／avelumab／durvalumab／cemiplimab／dostarlimab 欄皆「**本藥品尚未給付於此適應症**」[S43]。
- 使用條件：「病人身體狀況良好(ECOG≦1)」；「每位病人每個適應症限給付一種免疫檢查點抑制劑且不得互換」；「**給付時程期限：自初次處方用藥日起算 2 年**」；「需經事前審查核准後使用」；「每次申請以 12 週為限」；「用藥後每 12 週至少評估一次，以 i-RECIST 標準…評定藥物療效反應」；「出現疾病惡化 iCPD (PD)或出現中、重度或危及生命之藥物不良反應者，應停止用藥」；備註「上述影像檢查之給付範圍不包括正子造影(PET)」[S43]。
- **術後輔助 nivolumab（CheckMate 577 情境）：第 9 節全文檢索「食道」共 8 處，無任何術後／輔助條文——gap，正文寫「目前健保沒有這一格的給付條文，問你的醫院藥劑部或個管師（自費或臨床試驗）」。**
- 5-FU/cisplatin 條文 9.x 亦新增「與 nivolumab 及 fluoropyrimidine 併用於…第一線治療，病人需符合免疫檢查點抑制劑之藥品給付規定。(115/2/1)」[S44]。
- 健保署「最新版藥品給付規定內容(分章節)」索引頁 https://www.nhi.gov.tw/ch/np-3397-1.html 本次 curl 回 403（Cloudflare），但 PDF 直連 200[FAIL-6]。

### 給繪圖組的數字（fig-ec-immuno-map）
三格：術後殘存（DFS HR 0.69，22.4 vs 11.0 個月；OS 未顯著）[S21][S22]；轉移第一線（TPS≥1% OS 15.4 vs 9.1，HR 0.54；全族群 13.2 vs 10.7，HR 0.74）[S25]、（CPS≥10 鱗癌 13.9 vs 8.8，HR 0.57；5 年 10.6% vs 3.0%）[S23][S24]；根治性化放療加免疫（KEYNOTE-975 ✗、RATIONALE-311 ✗ HR 0.92、SKYSCRAPER-07 主要終點 ✗／atezo 單藥 OS HR 0.69、KUNLUN 2027、ESCORT-CRT 未讀出）[S32][S36][S34][S39][S37]。台灣給付格：nivolumab 1L＋化療／2L 單藥，TC≧1%，2 年[S43]。

---

## B3 `ec-surgery`〈開刀會拿掉什麼，胃會被拉到哪裡〉

### Key facts

**術式與吻合位置**
- Ivor Lewis（腹＋右胸，胸內吻合）、McKeown（腹＋胸＋頸，頸部吻合）、經橫膈（transhiatal，不開胸）。MIRO 試驗對 hybrid 的定義原文：「a two-field abdominal-thoracic operation (also called an Ivor-Lewis procedure) with laparoscopic gastric mobilization and open right thoracotomy」，適用「middle or lower third of the esophagus」[S48]。
- **經橫膈 vs 經胸擴大清掃**（Hulscher 2002 NEJM，n=220，**腺癌**，中下段／賁門）：經胸併發症較高，住院死亡無差異（p=0.45）；5 年 DFS 27% vs 39%、OS 29% vs 39%，差異未達統計顯著但有趨勢[S50]。
- **胸內 vs 頸部吻合**（ICAN，van Workum 2021 JAMA Surg，荷蘭 9 家高量中心，n=245 可分析，中下段／接合部，微創）：需再介入的吻合口滲漏 **12.3% vs 31.7%**；總滲漏 12.3% vs 34.1%；胸內吻合嚴重併發症少 11.3 個百分點、喉返神經麻痺少 7.3 個百分點、吞嚥困難／嗆咳／說話三個生活品質面向較好；ICU 天數、死亡率無差異[S59]。
- **Ivor Lewis vs McKeown 微創**（Xiu 2026 Surg Endosc，單中心 RCT，n=272，**中下段鱗癌**，OA）：滲漏 8.1% vs 16.9%（p=0.03）、吻合口狹窄 6.6% vs 22.8%（p<0.001）、喉返神經損傷 0 vs 3.7%、手術時間 210 vs 285 分鐘；PFS 無差異（p=0.67）[S61]。

**微創 vs 開胸——三個隨機試驗**
- TIME（Biere 2012 Lancet，n=115，5 中心）：術後 2 週肺部感染 **9% vs 29%**（RR 0.30，p=0.005）；住院期間 12% vs 34%；住院死亡：開胸 1 人（滲漏）、微創 2 人（吸入性肺炎、滲漏後縱膈炎）[S47]。
- MIRO（Mariette 2019 NEJM，n=207，hybrid vs 開）：30 天 Clavien-Dindo ≥II 併發症 **36% vs 64%**（OR 0.31）；主要肺部併發症 18% vs 30%；3 年 OS 67% vs 55%、DFS 57% vs 48%[S48]。
- ROBOT（van der Sluis 2019 Ann Surg，單中心 n=112，機器手臂 vs 開胸）：整體手術相關併發症 **59% vs 80%**（RR 0.74，p=0.02）；肺部 RR 0.54、心臟 RR 0.47；失血 400 vs 568 mL；14 天功能恢復較好；中位追蹤 40 個月腫瘤學結果相當[S49]。→ 注意對照組是**開胸**，不是傳統微創；「機器手臂優於胸腔鏡」沒有隨機證據。

**併發症與死亡率——大型登錄**
- ECCG／ESODATA 基準（Low 2019，24 家高量中心、14 國，n=2,704，2015–16）：任何併發症 59%；肺炎 14.6%、心房顫動 14.5%；**吻合口滲漏 11.4%**、管胃壞死 1.3%、乳糜漏 4.7%、喉返神經損傷 4.2%；Clavien-Dindo ≥IIIb 17.2%；再入院 11.2%；**30 天死亡 2.4%、90 天死亡 4.5%**；R0 93.4%[S51]。
- ESODATA 更新（Kuppusamy 2022，39 中心，n=6,022，2015–18）：30／90 天死亡 **2.0%／4.5%**；再入院 9.7%；出院回家 89.4%；肺炎 15.3%→12.8%；**滲漏率 11.7%→13.1%（仍 >10%）**，需手術的滲漏 3.3%→3.0%[S52]。
- 三個登錄並列（OGAA 2021，BJS Open，OA）：整體併發症 OGAA 63.6%／ECCG 59.0%／DUCA 62.2%（無差異）；**30 天死亡 OGAA 3.2%／ECCG 2.4%／DUCA 1.7%（p=0.013）**；DUCA 微創比例 85.8%、術前治療 93.5%[S53]。
- 日本 NCD（Takeuchi 2014，n=5,354，713 家醫院，2011）：整體併發症 41.9%；**30 天死亡 1.2%、手術死亡 3.4%**；需術前 ADL 協助 OR 4.2、術前一年內吸菸 OR 2.6、**六個月內體重掉 >10% OR 2.4**（30 天死亡）[S54]。→ 與 C1／C4 銜接：體重與戒菸是手術死亡率的變數。
- 住院天數：Lin 2017（美國三中心，術前化放療後）平均 13.2（3D）／11.6（IMRT）／9.3（質子）天[S60]。TIME／MIRO 的住院天數不在摘要，不可引。台灣住院天數：**無官方資料——gap**。

**淋巴結清掃（二野／三野）**
- Li 2020 BJS（中國 RCT，n=400，中下段鱗癌，無術前治療）：三野中位清掃 37 vs 24 顆；三野組 21.5% 有頸部淋巴結轉移、pN3 10.5% vs 5.0%；併發症相當，僅再插管 3.0% vs 0；90 天死亡 0 vs 0.5%[S57]。
- NST 1503（Mao 2025，多中心 RCT，n=829，OA）：以右喉返神經淋巴結冰凍切片分流——陰性者隨機 2FL vs 3FL：**5 年 OS 68.8% vs 72.2%、DFS 62.8% vs 65.1%（皆 NS）**；陽性者直接 3FL，頸部轉移率 28.9% vs 8.3%；結論：右喉返神經淋巴結陰性者可免頸部清掃[S58]。

**手術量與結果**
- Birkmeyer 2002 NEJM（美國 Medicare 1994–99）：食道切除低量 vs 高量醫院校正死亡率絕對差 **>5 個百分點**（同級只有全肺切除）[S55]。Reames 2014（2000–09）：食道切除極低量 vs 極高量醫院死亡 OR 從 2.25 升到 **3.68（2.66–5.11）**，關係在現代**變強**[S56]。台灣手術量與結果：**無可引官方資料——gap**（SPEC 固定紅線：不點名機構）。

### 反方向的資料
- ROBOT 是單中心、對照開胸[S49]；MIRO 的存活差異是次要終點[S48]。
- Hulscher 的擴大清掃存活優勢未達顯著且是腺癌[S50]。
- 日本 NCD 微創組併發症反而較高（44.3% vs 40.8%，p=0.016）——早期學習曲線的訊號[S54]。

### Claim ceiling
- **可寫**：「食道切除在高量中心登錄的 90 天死亡率 4–5%，30 天 2–3%；日本全國 30 天 1.2%」；「吻合口滲漏在國際登錄裡超過一成，並沒有隨技術進步下降」；「微創比開胸肺部併發症少（三個隨機試驗方向一致）」；「接在胸腔比接在頸部滲漏少、聲帶問題少（隨機）」；「二野／三野：右喉返神經淋巴結陰性的中下段鱗癌，隨機試驗顯示免頸部清掃存活不差」；「醫院手術量與死亡率的關係在食道切除特別強」。
- **不可寫**：「機器手臂優於胸腔鏡」（無隨機比較）；「微創存活較好」（MIRO 是次要終點）；任何本院數字或機構名；台灣住院天數、台灣死亡率（無官方資料）。

### Caveats
- 術後人生（吃、傾倒、逆流）指向 D1；開不開刀的完整比較屬 A4，本篇不重比。
- 「胃被拉到哪裡」的解剖敘述與 fig-ec-after-surgery 歸 D1，本篇只交代吻合位置差異。

### 台灣端
- 食道切除術的健保支付項目本 brief 未逐條核對——gap（屬手術給付常規，正文不需要數字）。重大傷病屬 A 組。

### 給繪圖組的數字
若 B3 需要一張「風險刻度」：滲漏 11–13%、肺炎 13–15%、90 天死亡 4.5%、30 天 2–2.4%[S51][S52]；胸內 vs 頸部滲漏 12.3% vs 34.1%[S59]；微創 vs 開胸肺部感染 9% vs 29%[S47]。

---

## B4 `ec-esd`〈早期病灶內視鏡就能解決嗎〉【紅線 7】

### Key facts

**浸潤深度與轉移風險（紅線 7 的核心數字）**
- Yamashina 2013（大阪，n=402 鱗癌 ER 後長期追蹤，平均 50 個月）：**5 年累積轉移率 EP/LPM 0.4%、MM 8.7%、SM1 7.7%、SM2 36.2%**（p<0.001）；相對 EP/LPM 的 HR：MM 13.1、SM1 40.2、SM2 196.3；黏膜癌有／無淋巴血管侵犯 5 年轉移 46.7% vs 0.7%；5 年 OS EP/LPM 90.5%、MM 71.1%、SM 70.8%[S63]。→ SPEC 寫的「m1/m2 <5%，m3/sm1 約 10–20%，sm2/sm3 >30%」在這筆資料是 0.4%／8–9%／36%——**寫作者用這組原始數字，不用 SPEC 的概數**。
- Xu W 2020 系統性回顧（亞洲 20 篇、3,983 人接受手術清掃）：腫瘤大小、巨觀型態、分化、**浸潤深度**、淋巴血管侵犯是淋巴結轉移的危險因子；年齡、性別、位置不是[S64]（摘要無各層百分比，不可引數字）。

**指引原文（可逐字引）**
- ESGE 2022（Pimentel-Nunes，Endoscopy）：「ESGE recommends ESD as the treatment of choice for most superficial esophageal squamous cell … lesions」；治癒性（very low risk）定義：「en bloc R0 resection … histology no more advanced than intramucosal cancer (**no more than m2** in esophageal squamous cell carcinoma), well to moderately differentiated, with no lymphovascular invasion or ulceration … no further staging procedure or treatment is generally recommended」；低風險（仍屬治癒）：「superficial submucosal invasion (**sm1**), well to moderately differentiated, no lymphovascular invasion, **size ≤ 20 mm** for an esophageal squamous cell carcinoma」；高風險（非治癒）：「lymphovascular invasion, or deeper infiltration than sm1, or positive vertical margins, or undifferentiated tumor … complete staging and strong consideration for additional treatments … in a multidisciplinary discussion」；不建議 ER 前常規 EUS／CT／MRI／PET[S62]。
- JES 2022（Kitagawa 2023 part 1，OA 全文）：「In patients classified as having pT1a-EP/LPM disease, follow-up may be scheduled; on the other hand, in patients diagnosed as having **pT1a-MM/pT1b-SM disease, additional treatment (surgery or chemoradiotherapy) should be considered**」；CQ6 建議：「There is evidence to recommend esophagectomy or chemoradiotherapy as an additional treatment in patients identified as having a pT1a-MM lesion with positive vascular invasion or a pT1b-SM lesion after endoscopic treatment」，並註記血管侵犯陽性者「a tendency towards a worse prognosis after chemoradiotherapy than after surgery, suggesting that surgery may be the optimal additional treatment option in these high-risk patients」；狹窄預防：「When the post-resection ulcer is expected to involve **≥ 3/4th of the esophageal circumference**, a preventive measures against stenosis should be considered」；CQ4 強烈建議口服 prednisolone 或黏膜下 triamcinolone；≥3/4 周（非全周）病灶的狹窄率：口服類固醇 8.6–23.1%、局部注射 9.2–36.2%、合併 10.0–13.3%、**無預防 50.0–80.0%**[S18]。cStage I（T1bN0）的手術 vs 化放療：兩者皆「weak evidence」（共識 92.3%，證據 C）[S18]。
- JGES 2020 ESD/EMR 食道癌指引存在（Ishihara，Dig Endosc 2020;32:452–493），措辭取不到[S69]。

**非根治性切除之後——JCOG0508**
- Minashi 2019 Gastroenterology（單臂前瞻，n=176 接受 ER，**cT1b(SM1–2)N0M0 胸段鱗癌**）：依 ER 病理分流——A 組（pT1a、切緣陰性、無 LVI）不加治療 74 人；**B 組（pT1b 切緣陰性，或 pT1a 有 LVI）預防性化放療 41.4 Gy 至局部區域淋巴結** 87 人；C 組（垂直切緣陽性）50.4 Gy＋9 Gy 加強 15 人；化療 5-FU/cisplatin。**B 組 3 年 OS 90.7%（90% CI 84.0–94.7）、全體 92.6%**，超過 80% 門檻；結論「comparable to that of surgery」[S65]。→ 紅線 7 的第二句「非根治性切除之後要加化放療」的證據；注意它是**單臂**、日本、3 年。

**ESD 併發症**
- Tsujii 2015（日本 11 家含市立醫院，n=307／368 病灶）：en bloc 96.7%、完全切除 84.5%；**穿孔（含縱膈氣腫）5.2%**、術後肺炎 1.6%、出血 0%、**狹窄 7.1%**；全部保守治癒、無手術相關死亡；早期年代 OR 4.04、低量機構 OR 3.03 是穿孔的獨立因子；病灶周徑與狹窄相關 OR 32.3[S66]。
- Ono 2009（東京，n=65，HGIN/m2）：狹窄的獨立因子——**周徑 >3/4（OR 44.2）**與深度 m2（OR 14.2）；<3/4 周的 HGIN 無狹窄[S67]。
- Han 2021 統合（22 篇）：ESD 比 EMR en bloc／治癒／R0 較高、局部復發較低，但**較耗時、穿孔較多**；病灶 >20 mm 才顯出 ESD 優勢；≤10 mm EMR 即可[S68]。

**頭頸癌病人的食道第二原發（台灣研究，全部 PASS）**
- Lee 2009 GIE（台灣單中心，n=44 無法經口內視鏡的頭頸癌病人）：經鼻細徑內視鏡＋NBI＋Lugol 序列篩檢；標準白光敏感度 55.6%，加 NBI 88.9%（特異度 97.2%），加 Lugol 88.9%（特異度 72.2%）；序列法估計偽陰性 1.2%[S70]。
- Chung 2016 統合（Head Neck，16 篇 4,918 人）：白光／NBI／Lugol 敏感度 53%／87%／88%，特異度 99%／95%／63%；**NBI 診斷效能最佳**[S71]。
- Chung 2019 Oral Oncol（台灣醫院登錄，1,577 頭頸癌＋501 食道癌，2000–2016）：接受影像強化內視鏡篩檢且陰性的頭頸癌病人 5 年 OS 44%，未篩檢 39%；作者建議常規 IEE 篩檢[S72]。
- Wang WL 2016 Laryngoscope（台灣前瞻世代 100 人）：同步食道鱗癌的獨立危險因子：**飲酒 OR 18.75、喝酒臉紅 OR 2.53**、BMI OR 0.77；有同步食道癌者 5 年 OS 30% vs 70%；HPV 無關[S73]。→ 與 A1／C4 的 ALDH2 敘事銜接。
- Tseng 2020 Sci Rep（台灣健保資料庫，68,131 頭頸癌，OA）：診斷 6 個月內接受食道內視鏡者 9,707 人，同步食道癌 1.0%；首檢陰性者 **5／10 年異時性食道癌累積 1.4%／2.7%**；口咽／下咽癌者 10 年 3.3% vs 口腔／喉癌 0.9%（HR 2.15）；「Metachronous EC continues to develop … even at 10-years」[S74]。
- Wang CC 2024 Head Neck（台灣，717 新診斷頭頸鱗癌接受治療前食道篩檢）：同步食道鱗癌 **14.4%（103/717）**；飲酒 OR 4.19、咽部原發 OR 1.68 為危險因子[S75]。

### 反方向的資料
- JCOG0508 是單臂，沒有與手術直接隨機比較；JES 對 T1b 的手術 vs 化放療只給 weak evidence[S65][S18]。
- Yamashina 的 SM1 轉移 7.7% 與 MM 8.7% 相近，「SM1 就一定比 MM 危險」寫不出來[S63]。
- Tsujii 的穿孔 5.2% 是 2005–2012 含學習曲線的日本資料，現今高量中心可能較低，但沒有可引的台灣數字。

### Claim ceiling
- **可寫**：「深度只到黏膜表層（EP/LPM，ESGE 的 m1–m2），5 年轉移率 0.4%，切乾淨就不需要進一步治療」；「一到黏膜肌層或黏膜下層，轉移率 8–9%，到 SM2 是 36%——這時候 ESD 是『拿到病理答案』的第一步，不是終點」；「非根治性切除之後加化放療，日本前瞻試驗 3 年存活 91%，與手術相當，但這是單臂」；「ESD 穿孔約 5%、狹窄約 7%，超過 3/4 周的病灶狹窄風險大幅上升，要預防」；「頭頸癌病人同步食道癌在台灣篩檢世代達 14%，十年內還會持續出現，喝酒臉紅的人風險更高」。
- **不可寫**：「切掉就沒事」；「ESD 可以取代手術」（對 T1b）；「ESD 有／沒有健保」（見台灣端）；任何具體機構的 ESD 量或成績。

### Caveats／safety notes
- 深度分層術語：ESGE 用 m1/m2/m3/sm1，JES 用 EP/LPM/MM/SM1–3；文章要對照一次（m3＝MM）。
- 篩檢建議的頻率與年限屬 D3，本篇只給「為什麼要篩」。

### 台灣端
- 健保支付標準（現行全表，資料版本「1140501 生效」，2026-09-02 下載）：**72050B「內視鏡黏膜切除術」8,199 點**（2022/03/01 起），適應症「(2)早期胃腸道癌症(包括食道、胃、十二指腸、大腸、直腸)」，含一般材料費，得另加計 63%[S76]。**「黏膜下剝離」「ESD」零筆——gap**，正文寫「內視鏡黏膜切除術有健保項目；ESD 本身如何計價、耗材是否自費，問你的腸胃科醫師與醫務課」。
- 頭頸癌病人食道篩檢在台灣是否有給付碼：未查證——gap。

### 給繪圖組的數字
深度階梯：EP/LPM 0.4% → MM 8.7% → SM1 7.7% → SM2 36.2%（5 年累積轉移，Yamashina）[S63]；ESGE 治癒線畫在 m2（≤sm1、≤20 mm、無 LVI 為低風險）[S62]；狹窄：≥3/4 周無預防 50–80%，有預防 9–23%[S18]。

---

## B5 `ec-proton`〈食道癌的質子治療：升級的理由與試驗的現況〉【紅線 6】

### Key facts

**先把基本款站穩：光子 IMRT 已經很好（紅線 6 要求的完整段落）**
- Lin 2012（n=676，3D vs IMRT）：OS HR 0.72、局部區域復發較少、心因性死亡與不明原因死亡較少（5 年 11.7% vs 5.4%）[S17]。
- Wang 2013（n=444）：3D vs IMRT 術後肺部併發症 OR 2.018；差異可由平均肺劑量解釋[S79]。
- Lin 2017（n=580）：住院 3D 13.2 天→IMRT 11.6 天；90 天死亡 4.2%／4.3%（3D／IMRT）與質子 0.9% **無顯著差異（p=0.264）**[S60]。
- 今天所有劑量試驗（ARTDECO、中國 50/60、CONCORDE 80% IMRT）與 KEYNOTE-975 等都是在 IMRT 時代做的，「50.4 Gy IMRT＋化療」就是被反覆驗證的基本款[S4][S6][S5]。

**升級的理由：劑量學**
- Zhang 2008（MDACC，15 位遠端食道癌，4D-CT）：相對 IMRT，兩束質子計畫肺 V5／V10／V20 減 35.6%／20.5%／5.8%、平均肺劑量減 5.1 Gy；三束質子減 17.4%／8.4%／5%、2.9 Gy；**但兩束質子的心臟 V40 41.8% 比 IMRT 35.7% 高**、三束 27.7% 較低——省肺與省心之間要取捨；橫膈移動與胃內氣體影響劑量[S82]。
- Zhou 2023 統合（JAMA Netw Open，45 篇，OA）：質子顯著降低危及器官劑量；質子顯著減少 **G2+ 放射性肺炎、心包積液、G4+ 淋巴球低下**；OS 統合 HR 1.31（光子較差，I²=11%），PFS 無差異——全部來自非隨機研究[S83]。

**升級的證據 1——隨機第二期（唯一完成的隨機比較）**
- Lin 2020 JCO（MDACC，phase IIB 貝氏設計，n=145 隨機／107 可評估，50.4 Gy，鱗癌＋腺癌、可切除與不可切除分層）：共同主要終點 **總毒性負擔 TTB（11 種不良事件與術後併發症的複合分數）與 PFS**。IMRT 的 TTB 後驗平均 39.9 vs 質子 17.4（**2.3 倍**）；術後併發症分數 19.1 vs 2.5（7.6 倍）；後驗機率 0.9989 超過停止界線；**3 年 PFS 50.8% vs 51.2%、3 年 OS 44.5% vs 44.5%——相同**；**80% 的質子是被動散射**；因 NRG-GI006 啟動而在 67% 期中分析前關閉[S77]。
- → 紅線 6：主要終點是毒性負擔不是存活；「質子活得久」寫不出來。

**升級的證據 2——第三期進行中**
- NRG-GI006（NCT03801876）：質子 vs IMRT 第三期，估 300 人，主要終點 **OS** 與 G3+ 心肺不良事件；狀態 **ACTIVE_NOT_RECRUITING**（2026-08-24 更新），主要完成估 **2031-11**、研究完成估 2036-11[S78]。→ 2026 年的病人等不到這個答案。
- 泰國 HI-SIRI（IMPT 高劑量 vs IMRT 標準劑量，鱗癌，phase II/III，n=232，TCTR20200310006）：只有 2022 年 protocol[S90]。

**升級的證據 3——回溯性**
- Wang 2013：3D vs 質子術後肺部併發症 OR 3.154（1.365–7.289）；腸胃 OR 1.55（0.78–3.08，NS）[S79]。
- Lin 2017：質子住院 9.3 天（vs IMRT 11.6）、90 天死亡 0.9%（vs 4.3%，NS）[S60]。
- Xi 2017（MDACC 根治性化放療，質子 132 vs IMRT 211，2007–2014）：質子 OS（p=0.011）、PFS（p=0.001）較好；多變項 IMRT OS HR 1.454；III 期 5 年 OS 34.6% vs 25.0%；**I/II 期無差異**；毒性無差異；作者「need confirmation by prospective studies」[S81]。
- 淋巴球：Shiraishi 2018（MDACC，136 對 136 傾向配對，術前化放療）：**G4 淋巴球低下 IMRT 40.4% vs 質子 17.6%**（p<0.0001）；質子 OR 0.29[S80]。（淋巴球低下與存活的關聯屬機轉假說，本 brief 未查證存活連結——不可寫成「所以活得久」。）

**日本經驗**
- Ono 2019（四家質子中心，n=202，2009–2013，含 90 位不可手術、49.5% III/IV 期）：3／5 年 OS 66.7%／56.3%；5 年局部控制 64.4%；G3 心包積液 1%、G3 肺炎 0.5%、**無 G4+ 心肺毒性**[S84]。
- Ono 2020（同資料庫 ≥75 歲鱗癌，n=54，70.4% 不可手術）：5 年 OS 56.2%、癌症特異存活 71.7%、5 年局部控制 61.8%；除 3 例 G3 食道潰瘍外無 G3+ 毒性[S85]。→ 單臂回溯、無對照；「不劣於光子」是作者句，不是比較結果。

**政策層級**
- ASTRO 質子模型政策（現行版，文件未標日期）Group 1（常規支持給付）THORACIC 下明列「**Primary cancers of the esophagus**」（ICD-10 C15.3–C15.8）[S86]。

### 反方向的資料（誠實必列）
- Lin 2020 PFS／OS 相同，且 80% 被動散射[S77]；Lin 2017 死亡率差異不顯著[S60]；Xi 2017 早期無差異[S81]；Zhang 2008 兩束質子心臟劑量反而較高[S82]；統合分析的 OS 優勢全來自非隨機資料，質子病人明顯經過選擇[S83]。
- 肺癌的隨機比較（Liao 2018，見 nextgen brief）質子沒有贏——跨癌別的提醒，站上 nt-proton 已有，本篇一句指路即可。

### Claim ceiling（硬上限）
- **可寫**：「光子 IMRT 對 3D 的回溯資料顯示存活、局部控制、非癌症死亡都較好，今天的標準治療就是 IMRT」；「質子在食道的劑量學優勢是肺、心、淋巴球的低劑量區」；「唯一完成的隨機比較（MD Anderson 第二期）：**總毒性負擔 IMRT 是質子的 2.3 倍、術後併發症分數 7.6 倍，PFS 與 OS 相同**」；「第三期 NRG-GI006 以存活為主要終點，預計 2031 年主要完成」；「回溯資料看到住院天數較短、G4 淋巴球低下少一半、術後肺部併發症較少」；「日本四中心 202 人五年存活 56%、無 G4 以上心肺毒性（單臂）」；「ASTRO 模型政策把食道癌列在建議給付的第一組」。
- **不可寫**：「質子存活較好」「質子治癒率較高」（Lin 2020 相同；Xi 2017 回溯）；「值得」；任何把台灣費用寫成全台行情；把 Lin 2020 的 TTB 寫成「副作用少一半以上」而不交代它是複合分數；把兒童給付推到成人。

### Caveats／safety notes
- 質子物理與法規、FLASH 等已在站上 nt-proton／insight-proton，本篇不重複。
- 台灣費用段落必須寫「該院公告、日期、非食道專屬、總價依次數與複雜度而異、其他醫院問醫務課」。

### 台灣端（B5 主場）
- **健保**：質子放射治療三項（36025B／36026B／36027B，676,111／1,030,540／1,266,499 點）自 **115-01-01（2026-01-01）生效，適用範圍均為「年齡未滿十九歲病人」**、事前審查、每人每原發癌終生一次、包裹給付——行政院公報第 031 卷第 245 期 PDF（2026-09-02 重新確認 HTTP 200，388,941 bytes）[S87]。→ **成人食道癌質子＝健保零項目、自費。**
- 支付標準全表中「質子」只見 N21301–N21308 自費參考項（點數 0，標「HTA 項目」：3D 電腦斷層模擬、MRI 模擬、固定模具、質子射線治療/次、腦部立體定位、身體立體定位、電腦治療規劃費）[S76]——這組項目名稱可直接引，說明「健保表裡的質子項目是自費計價名目，不是給付」。
- **醫院自費收費（唯一查到的官方公告頁）**：高雄長庚質子治療中心「收費標準」頁（頁面標示網站更新 2026/03/27；2026-09-02 curl 200）：質子諮詢診察費 1,000；固定模具 1,950；3D 電腦斷層模擬 8,500；電腦治療規劃費 11,483；MRI 模擬 7,500／12,500；**強度調控質子射線治療/次 21,750；中度 26,000；複雜 34,500**；一般／複雜呼吸調控/次 5,000／9,600；腦部立體定位套組 230,234；立體定位放射治療套組 330,000[S88]。**沒有食道癌專屬套組**；食道癌約 25–28 次的總價要自己乘且會因複雜度與呼吸調控而異——正文只可寫「該院公告的每次費用區間」並標日期與網址，不可算總價寫成事實，不可寫成全台行情；其他醫院「向各院醫務課確認」。
- 設備分布：衛福部醫事司「全國醫用粒子治療設備設置現況」（資料日期 113-12-11；2026-09-02 curl 200）：質子 13 家（營運中 4）、重粒子 3 家（營運中 1）——正文不列院名[S89]。

### 給繪圖組的數字（fig-ec-proton-dose）
劑量學示意用 Zhang 2008：IMRT vs 兩束／三束質子的肺 V5 減 35.6%／17.4%、平均肺劑量減 5.1／2.9 Gy；心臟 V40 IMRT 35.7%、兩束質子 41.8%、三束 27.7%[S82]。臨床標籤：TTB 39.9 vs 17.4、3 年 OS 44.5% vs 44.5%[S77]；G4 淋巴球低下 40.4% vs 17.6%[S80]。圖上不可出現「存活優勢」箭頭。

---

## 來源清單（全 brief 唯一編號；PASS＝可引；FAIL＝不可引、保留供查證紀錄）

### B1
- **[S1] PASS** — Herskovic A, Martz K, al-Sarraf M, et al. *Combined chemotherapy and radiotherapy compared with radiotherapy alone in patients with cancer of the esophagus.* N Engl J Med. 1992;326(24):1593–1598. DOI 10.1056/NEJM199206113262403. PMID 1584260. OA:N. https://doi.org/10.1056/NEJM199206113262403 — Route: Europe PMC REST EXT_ID；數字出自摘要。
- **[S2] PASS** — Cooper JS, Guo MD, Herskovic A, et al. *Chemoradiotherapy of locally advanced esophageal cancer: long-term follow-up of a prospective randomized trial (RTOG 85-01).* JAMA. 1999;281(17):1623–1627. DOI 10.1001/jama.281.17.1623. PMID 10235156. OA:N. https://doi.org/10.1001/jama.281.17.1623 — Route: Europe PMC REST。
- **[S3] PASS** — Minsky BD, Pajak TF, Ginsberg RJ, et al. *INT 0123 (RTOG 94-05) phase III trial of combined-modality therapy for esophageal cancer: high-dose versus standard-dose radiation therapy.* J Clin Oncol. 2002;20(5):1167–1174. DOI 10.1200/JCO.2002.20.5.1167. PMID 11870157. OA:N. https://doi.org/10.1200/JCO.2002.20.5.1167 — Route: Europe PMC REST。
- **[S4] PASS** — Hulshof MCCM, Geijsen ED, Rozema T, et al. *Randomized Study on Dose Escalation in Definitive Chemoradiation for Patients With Locally Advanced Esophageal Cancer (ARTDECO Study).* J Clin Oncol. 2021;39(25):2816–2824. DOI 10.1200/JCO.20.03697. PMID 34101496. OA:N. https://doi.org/10.1200/JCO.20.03697 — Route: Europe PMC REST。
- **[S5] PASS（會議摘要層級）** — Crehange G, M'vondo C, Bertaut A, et al. *Exclusive Chemoradiotherapy With or Without Radiation Dose Escalation in Esophageal Cancer: Multicenter Phase 2/3 Randomized Trial CONCORDE (PRODIGE-26).* Int J Radiat Oncol Biol Phys. 2021;111(3S):S5. DOI 10.1016/j.ijrobp.2021.07.045. PMID 34700569. OA:N. https://doi.org/10.1016/j.ijrobp.2021.07.045 — Route: Europe PMC REST（TITLE 檢索）。**引用時標明「ASTRO 2021 摘要」。**
- **[S6] PASS** — Xu Y, Dong B, Zhu W, et al. *A Phase III Multicenter Randomized Clinical Trial of 60 Gy versus 50 Gy Radiation Dose in Concurrent Chemoradiotherapy for Inoperable Esophageal Squamous Cell Carcinoma.* Clin Cancer Res. 2022;28(9):1792–1799. DOI 10.1158/1078-0432.CCR-21-3843. PMID 35190815. OA:N. https://doi.org/10.1158/1078-0432.CCR-21-3843 — Route: Europe PMC REST。（SPEC 寫 JAMA Oncol，實為 Clin Cancer Res。）
- **[S7] PASS** — Cheng Q, Dong B, Zhu W, et al. *Long-term outcomes and exploratory analysis from a randomized phase 3 trial of radiation dose escalation in definitive chemoradiotherapy for locally advanced esophageal squamous cell carcinoma.* Drug Resist Updat. 2026;88:101446. DOI 10.1016/j.drup.2026.101446. PMID 42442129. OA:N. https://doi.org/10.1016/j.drup.2026.101446 — Route: Europe PMC REST。
- **[S8] PASS** — Conroy T, Galais MP, Raoul JL, et al. *Definitive chemoradiotherapy with FOLFOX versus fluorouracil and cisplatin in patients with oesophageal cancer (PRODIGE5/ACCORD17): final results of a randomised, phase 2/3 trial.* Lancet Oncol. 2014;15(3):305–314. DOI 10.1016/S1470-2045(14)70028-2. PMID 24556041. OA:N. https://doi.org/10.1016/S1470-2045(14)70028-2 — Route: Europe PMC REST。
- **[S9] PASS（OA）** — Chen Y, Ye J, Zhu Z, et al. *Comparing Paclitaxel Plus Fluorouracil Versus Cisplatin Plus Fluorouracil in Chemoradiotherapy for Locally Advanced Esophageal Squamous Cell Cancer: A Randomized, Multicenter, Phase III Clinical Trial.* J Clin Oncol. 2019;37(20):1695–1703. DOI 10.1200/JCO.18.02122. PMID 30920880; PMC6638596. OA:Y. https://doi.org/10.1200/JCO.18.02122 — Route: Europe PMC REST。
- **[S10] PASS** — Honing J, Smit JK, Muijs CT, et al. *A comparison of carboplatin and paclitaxel with cisplatinum and 5-fluorouracil in definitive chemoradiation in esophageal cancer patients.* Ann Oncol. 2014;25(3):638–643. DOI 10.1093/annonc/mdt589. PMID 24492674; PMC4433521. OA:N. https://doi.org/10.1093/annonc/mdt589 — Route: Europe PMC REST。
- **[S11] PASS（protocol 論文，無結果）** — Messager M, Mirabel X, Tresch E, et al. *Preoperative chemoradiation with paclitaxel-carboplatin or with fluorouracil-oxaliplatin-folinic acid (FOLFOX) for resectable esophageal and junctional cancer: the PROTECT-1402, randomized phase 2 trial.* BMC Cancer. 2016;16:318. DOI 10.1186/s12885-016-2335-9. PMID 27194176; PMC4872363. OA:Y. — Route: Europe PMC REST。
- **[S12] PASS（登錄狀態）** — ClinicalTrials.gov NCT02359968（PROTECT-1402）：COMPLETED；主要完成 2021-01-08、完成 2024-02-09；n=106；hasResults=False；最後更新 2026-03-18。https://clinicaltrials.gov/study/NCT02359968 — Route: CT.gov API v2（2026-09-02）。
- **[S13] PASS** — Nishimura Y, Ono K, Tsutsui K, et al. *Esophageal cancer treated with radiotherapy: impact of total treatment time and fractionation.* Int J Radiat Oncol Biol Phys. 1994;30(5):1099–1105. DOI 10.1016/0360-3016(94)90315-8. PMID 7961017. OA:N. — Route: Europe PMC REST。
- **[S14] PASS（OA）** — Xiang G, Wang X, Zhang C, et al. *Impact of treatment time and waiting time on outcome for esophageal squamous cell carcinoma receiving definitive chemoradiotherapy.* Radiat Oncol. 2025;20(1):111. DOI 10.1186/s13014-025-02687-8. PMID 40671129; PMC12269214. OA:Y. — Route: Europe PMC REST。
- **[S15] PASS（頭頸類推）** — Bese NS, Hendry J, Jeremic B. *Effects of prolongation of overall treatment time due to unplanned interruptions during radiotherapy of different tumor sites and practical methods for compensation.* Int J Radiat Oncol Biol Phys. 2007;68(3):654–661. DOI 10.1016/j.ijrobp.2007.03.010. PMID 17467926. OA:N. — Route: Europe PMC REST。
- **[S16] PASS（頭頸類推）** — Overgaard J, Hansen HS, Specht L, et al. *Five compared with six fractions per week of conventional radiotherapy of squamous-cell carcinoma of head and neck: DAHANCA 6 and 7 randomised controlled trial.* Lancet. 2003;362(9388):933–940. DOI 10.1016/S0140-6736(03)14361-9. PMID 14511925. OA:N. — Route: Europe PMC REST。
- **[S17] PASS** — Lin SH, Wang L, Myles B, et al. *Propensity score-based comparison of long-term outcomes with 3-dimensional conformal radiotherapy vs intensity-modulated radiotherapy for esophageal cancer.* Int J Radiat Oncol Biol Phys. 2012;84(5):1078–1085. DOI 10.1016/j.ijrobp.2012.02.015. PMID 22867894; PMC3923623. OA:N. — Route: Europe PMC REST。
- **[S18] PASS（OA，全文已抓）** — Kitagawa Y, Ishihara R, Ishikawa H, et al. *Esophageal cancer practice guidelines 2022 edited by the Japan esophageal society: part 1.* Esophagus. 2023;20(3):343–372. DOI 10.1007/s10388-023-00993-2. PMID 36933136; PMC10024303. OA:Y. https://doi.org/10.1007/s10388-023-00993-2 — Route: Europe PMC REST＋fullTextXML（引語逐字核對）。
- **[S19] PASS（OA，全文已抓）** — Kitagawa Y, et al. *Esophageal cancer practice guidelines 2022 edited by the Japan Esophageal Society: part 2.* Esophagus. 2023;20(3):373–389. DOI 10.1007/s10388-023-00994-1. PMID 36995449; PMC10235142. OA:Y. — Route: 同上。
- **[S20] PASS（登錄）** — ClinicalTrials.gov NCT01348217（PRODIGE 26／CONCORDE）：COMPLETED（2018-12-17），n=196（登錄值；摘要為 217），hasResults=False，最後更新 2020-01-27。https://clinicaltrials.gov/study/NCT01348217 — Route: CT.gov API v2。
- **[S46] PASS（OA，實務調查）** — Gerum S, Clemens P, Salinger J, et al. *Practice of radiation therapy for squamous cell esophageal cancer in Austria – a survey on behalf of the ÖGRO-GIT.* Radiat Oncol. 2026;21(1):90. DOI 10.1186/s13014-026-02808-x. PMID 41933377; PMC13295225. OA:Y. — Route: Europe PMC REST。
- **[S47b] PASS（protocol，無結果）** — Zhu H, Liu Q, Xu H, et al. *Dose escalation based on 18F-FDG PET/CT response in definitive chemoradiotherapy of locally advanced esophageal squamous cell carcinoma: a phase III… (ESO-Shanghai 12).* Radiat Oncol. 2022;17(1):134. DOI 10.1186/s13014-022-02099-y. PMID 35906623; PMC9338557. OA:Y. NCT03790553。— Route: Europe PMC REST。只可寫「進行中」。

### B2
- **[S21] PASS** — Kelly RJ, Ajani JA, Kuzdzal J, et al.; CheckMate 577 Investigators. *Adjuvant Nivolumab in Resected Esophageal or Gastroesophageal Junction Cancer.* N Engl J Med. 2021;384(13):1191–1203. DOI 10.1056/NEJMoa2032125. PMID 33789008. OA:N. https://doi.org/10.1056/NEJMoa2032125 — Route: Europe PMC REST。
- **[S22] PASS（OA）** — Verhoeven RHA, Kuijper SC, Slingerland M, et al. *Adjuvant nivolumab after chemoradiotherapy and resection for patients with esophageal cancer: A real-world matched comparison of overall survival.* Int J Cancer. 2026;158(5):1292–1301. DOI 10.1002/ijc.70168. PMID 40985858; PMC12765972. OA:Y. — Route: Europe PMC REST。
- **[S23] PASS** — Sun JM, Shen L, Shah MA, et al.; KEYNOTE-590 Investigators. *Pembrolizumab plus chemotherapy versus chemotherapy alone for first-line treatment of advanced oesophageal cancer (KEYNOTE-590): a randomised, placebo-controlled, phase 3 study.* Lancet. 2021;398(10302):759–771. DOI 10.1016/S0140-6736(21)01234-4. PMID 34454674. OA:N. — Route: Europe PMC REST。
- **[S24] PASS（OA）** — Metges JP, Kato K, Sun JM, et al. *Pembrolizumab plus chemotherapy versus chemotherapy for advanced esophageal cancer: 5-year extended follow-up for the randomized phase III KEYNOTE-590 study.* ESMO Open. 2025;10(12):105854. DOI 10.1016/j.esmoop.2025.105854. PMID 41259897; PMC12670541. OA:Y. — Route: Europe PMC REST。
- **[S25] PASS** — Doki Y, Ajani JA, Kato K, et al.; CheckMate 648 Trial Investigators. *Nivolumab Combination Therapy in Advanced Esophageal Squamous-Cell Carcinoma.* N Engl J Med. 2022;386(5):449–462. DOI 10.1056/NEJMoa2111380. PMID 35108470. OA:N. — Route: Europe PMC REST。
- **[S26] PASS** — Kato K, Ajani J, Doki Y, et al. *Nivolumab plus chemotherapy or ipilimumab versus chemotherapy as first-line treatment for advanced esophageal squamous cell carcinoma: 5-year follow-up results from CheckMate 648.* Ann Oncol. 2026; in press (S0923-7534(26)01455-9). DOI 10.1016/j.annonc.2026.08.001. PMID 42575473. OA:N. — Route: Europe PMC REST。
- **[S27] PASS** — Luo H, Lu J, Bai Y, et al.; ESCORT-1st Investigators. *Effect of Camrelizumab vs Placebo Added to Chemotherapy on Survival and Progression-Free Survival in Patients With Advanced or Metastatic Esophageal Squamous Cell Carcinoma: The ESCORT-1st Randomized Clinical Trial.* JAMA. 2021;326(10):916–925. DOI 10.1001/jama.2021.12836. PMID 34519801; PMC8441593. — Route: Europe PMC REST。
- **[S28] PASS** — Wang ZX, Cui C, Yao J, et al. *Toripalimab plus chemotherapy in treatment-naïve, advanced esophageal squamous cell carcinoma (JUPITER-06): A multi-center phase 3 trial.* Cancer Cell. 2022;40(3):277–288.e3. DOI 10.1016/j.ccell.2022.02.007. PMID 35245446. OA:N. — Route: Europe PMC REST（作者串以 Europe PMC 記錄為準）。
- **[S29] PASS（OA）** — Lu Z, Wang J, Shu Y, et al.; ORIENT-15 study group. *Sintilimab versus placebo in combination with chemotherapy as first line treatment for locally advanced or metastatic oesophageal squamous cell carcinoma (ORIENT-15): multicentre, randomised, double blind, phase 3 trial.* BMJ. 2022;377:e068714. DOI 10.1136/bmj-2021-068714. PMID 35440464; PMC9016493. OA:Y. — Route: Europe PMC REST。
- **[S30] PASS** — Xu J, Kato K, Raymond E, et al. *Tislelizumab plus chemotherapy versus placebo plus chemotherapy as first-line treatment for advanced or metastatic oesophageal squamous cell carcinoma (RATIONALE-306): a global, randomised, placebo-controlled, phase 3 study.* Lancet Oncol. 2023;24(5):483–495. DOI 10.1016/S1470-2045(23)00108-0. PMID 37080222. OA:N. — Route: Europe PMC REST。
- **[S31] PASS** — Kato K, Cho BC, Takahashi M, et al. *Nivolumab versus chemotherapy in patients with advanced oesophageal squamous cell carcinoma refractory or intolerant to previous chemotherapy (ATTRACTION-3): a multicentre, randomised, open-label, phase 3 trial.* Lancet Oncol. 2019;20(11):1506–1517. DOI 10.1016/S1470-2045(19)30626-6. PMID 31582355. OA:N. — Route: Europe PMC REST。
- **[S32] PASS（公司官方文件，SEC 存檔）** — Merck & Co., Inc. *First-Quarter 2026 Financial Results*（Form 8-K Exhibit 99.1，2026-04-30）。原文：「In the Phase 3 KEYNOTE-975 study, compared to placebo plus definitive chemoradiotherapy (dCRT), KEYTRUDA plus dCRT did not show a statistically significant improvement in the primary endpoint of EFS in certain patients with locally advanced unresectable esophageal carcinoma.」 https://www.sec.gov/Archives/edgar/data/310158/000110465926052081/tm2612241d1_ex99-1.htm — Route: WebSearch → curl（HTTP 200，530,575 bytes）→ 全文檢索逐字確認。
- **[S33] PASS（登錄）** — ClinicalTrials.gov NCT04210115（KEYNOTE-975）：COMPLETED；主要完成 2026-01-21、完成 2026-06-23；n=703；主要終點 EFS、OS；hasResults=False；最後更新 2026-07-22。— Route: CT.gov API v2。
- **[S34] PASS** — Xu RH, Cho BC, Chen M, et al. *Atezolizumab with or without tiragolumab in unresectable esophageal squamous cell carcinoma following definitive concurrent chemoradiotherapy (SKYSCRAPER-07): a randomised, phase III study.* Ann Oncol. 2026; in press (S0923-7534(26)01431-6). DOI 10.1016/j.annonc.2026.07.413. PMID 42628839. OA:N. — Route: Europe PMC REST；全部數字出自摘要。
- **[S35] PASS（登錄）** — ClinicalTrials.gov NCT04543617（SKYSCRAPER-07）：ACTIVE_NOT_RECRUITING；n=760；主要完成估 2027-03-31；最後更新 2026-07-23。— Route: CT.gov API v2。
- **[S36] PASS（登錄張貼結果）** — ClinicalTrials.gov NCT03957590（RATIONALE-311）：COMPLETED（2025-03-31）；n=370（185/185）；hasResults=True；PFS 中位 29.0 vs 28.9 個月，HR 0.92（95% CI 0.68–1.25，log-rank p=0.3016）；OS 39.2 vs 48.2 個月，HR 1.10（0.83–1.46）；ORR 27.6% vs 38.9%；最後更新 2026-04-13。https://clinicaltrials.gov/study/NCT03957590 — Route: CT.gov API v2 resultsSection。**Europe PMC 查無論文（只有 2021 protocol：Yu R, et al. Future Oncol 2021;17(31):4081–4089, PMID 34269067）。**
- **[S37] PASS（登錄，UNKNOWN）** — ClinicalTrials.gov NCT04426955（ESCORT-CRT）：狀態 UNKNOWN；主要完成估 2022-12；n=396；最後更新 2021-09-16；hasResults=False。— Route: CT.gov API v2。Europe PMC／WebSearch 查無結果發表。
- **[S38] PASS（登錄）** — ClinicalTrials.gov NCT04550260（KUNLUN）：ACTIVE_NOT_RECRUITING；n=640；主要完成估 2027-06-30；主要終點 PFS（BICR）；最後更新 2026-05-13。— Route: CT.gov API v2。
- **[S39] PASS（公司官方文件）** — AstraZeneca. *Clinical Trials Appendix, Q1 2026 Results Update (29 April 2026)*：「KUNLUN | NCT04550260 | Locally advanced, unresectable ESCC | 640 | … Primary endpoint: PFS | Secondary endpoint: OS | FPCD: Q4 2020 | LPCD: Q3 2023 | **Data anticipated: 2027**」。 https://www.astrazeneca.com/content/dam/az/PDF/2026/eq1/Q1-2026-results-clinical-trials-appendix.pdf — Route: WebSearch → WebFetch（curl 直抓回 403，WebFetch 成功讀出上述列）。
- **[S40] PASS** — Shah MA, Kennedy EB, Deighton D, et al. *Immunotherapy and Targeted Therapy for Advanced Gastroesophageal Cancer: ASCO Guideline Update.* J Clin Oncol. 2026;44(12):1145–1165. DOI 10.1200/JCO-25-02958. PMID 41747202. OA:N. https://doi.org/10.1200/JCO-25-02958 — Route: Europe PMC REST；引語出自摘要。
- **[S41] PASS** — Shah MA, Kennedy EB, Alarcon-Rozas AE, et al. *Immunotherapy and Targeted Therapy for Advanced Gastroesophageal Cancer: ASCO Guideline.* J Clin Oncol. 2023;41(7):1470–1491. DOI 10.1200/JCO.22.02331. PMID 36603169. OA:N. — Route: Europe PMC REST；引語出自摘要。
- **[S42] PASS（書目）／措辭 FAIL** — Obermannová R, Alsina M, Cervantes A, et al. *Oesophageal cancer: ESMO Clinical Practice Guideline for diagnosis, treatment and follow-up.* Ann Oncol. 2022;33(10):992–1004. DOI 10.1016/j.annonc.2022.07.003. PMID 35914638. OA:N；摘要欄空白，內文措辭不可引。
- **[S43] PASS（台灣官方法規）** — 衛生福利部中央健康保險署。《藥品給付規定》第 9 節抗癌瘤藥物 現行合訂本 PDF（102 頁；檔案 ModDate 2026-08-21）。條文 9.69 免疫檢查點抑制劑：1.(10)、2.(8)、3.(1)–(9)、PD-L1 生物標記表 P101／P102。https://www.nhi.gov.tw/ch/dl-55685-99c675b771ab4b2789c891bc8db447ce-1.pdf — Route: curl 200（1,310,289 bytes）→ pdftotext → 全文檢索「食道」8 處逐條抄錄。
- **[S44] PASS（台灣官方法規）** — 健保署。《「藥品給付規定」修訂對照表 第 9 節抗癌瘤藥物（自 115 年 2 月 1 日生效）》：新增 9.69 2.(8) 食道鱗狀細胞癌 nivolumab 第一線併化療；P102 表格 TC≧1%。https://www.nhi.gov.tw/ch/dl-95591-b91a432d0fe34034a353b9e30a4f90d0-1.pdf — Route: curl 200 → pdftotext。
- **[S45] PASS（台灣官方法規）** — 健保署。《「藥品給付規定」修訂對照表 第 9 節抗癌瘤藥物（自 113 年 4 月 1 日生效）》：新增 9.69 1.(10) 食道鱗狀細胞癌 nivolumab 第二線（原限 120mg 規格）；表格 TC≧1%。https://www.nhi.gov.tw/ch/dl-67318-a41026aa220343239d60e75c90ce2ca1-1.pdf — Route: curl 200 → pdftotext。
- **[S46b] PASS（OA 綜述；僅作「文獻時間差」佐證，不引其結論）** — Wang Y, Gu J, Sun X. *Radiotherapy combined with immunotherapy for esophageal cancer: current status and challenge.* J Cancer Res Clin Oncol. 2026;152(5):103. DOI 10.1007/s00432-026-06480-2. PMID 42069985; PMC13135612. OA:Y. — Route: Europe PMC REST＋fullTextXML。

### B3
- **[S47] PASS** — Biere SS, van Berge Henegouwen MI, Maas KW, et al. *Minimally invasive versus open oesophagectomy for patients with oesophageal cancer: a multicentre, open-label, randomised controlled trial.* Lancet. 2012;379(9829):1887–1892. DOI 10.1016/S0140-6736(12)60516-9. PMID 22552194. OA:N. — Route: Europe PMC REST。
- **[S48] PASS** — Mariette C, Markar SR, Dabakuyo-Yonli TS, et al. *Hybrid Minimally Invasive Esophagectomy for Esophageal Cancer.* N Engl J Med. 2019;380(2):152–162. DOI 10.1056/NEJMoa1805101. PMID 30625052. OA:N. — Route: Europe PMC REST（SPEC 給的 PMID 30699875 為誤植，正確為 30625052）。
- **[S49] PASS** — van der Sluis PC, van der Horst S, May AM, et al. *Robot-assisted Minimally Invasive Thoracolaparoscopic Esophagectomy Versus Open Transthoracic Esophagectomy for Resectable Esophageal Cancer: A Randomized Controlled Trial.* Ann Surg. 2019;269(4):621–630. DOI 10.1097/SLA.0000000000003031. PMID 30308612. OA:N. — Route: Europe PMC REST。
- **[S50] PASS** — Hulscher JB, van Sandick JW, de Boer AG, et al. *Extended transthoracic resection compared with limited transhiatal resection for adenocarcinoma of the esophagus.* N Engl J Med. 2002;347(21):1662–1669. DOI 10.1056/NEJMoa022343. PMID 12444180. — Route: Europe PMC REST。
- **[S51] PASS** — Low DE, Kuppusamy MK, Alderson D, et al. *Benchmarking Complications Associated with Esophagectomy.* Ann Surg. 2019;269(2):291–298. DOI 10.1097/SLA.0000000000002611. PMID 29206677. — Route: Europe PMC REST。
- **[S52] PASS** — Kuppusamy MK, Low DE; International Esodata Study Group. *Evaluation of International Contemporary Operative Outcomes and Management Trends Associated With Esophagectomy: A 4-Year Study of >6000 Patients Using ECCG Definitions and the Online Esodata Database.* Ann Surg. 2022;275(3):515–525. DOI 10.1097/SLA.0000000000004309. PMID 33074888. — Route: Europe PMC REST。
- **[S53] PASS（OA）** — Oesophago-Gastric Anastomosis Study Group on behalf of the West Midlands Research Collaborative. *Comparison of short-term outcomes from the International Oesophago-Gastric Anastomosis Audit (OGAA), the Esophagectomy Complications Consensus Group (ECCG), and the Dutch Upper Gastrointestinal Cancer Audit (DUCA).* BJS Open. 2021;5(3):zrab010. DOI 10.1093/bjsopen/zrab010. PMID 35179183; PMC8140199. OA:Y. — Route: Europe PMC REST。
- **[S54] PASS** — Takeuchi H, Miyata H, Gotoh M, et al. *A risk model for esophagectomy using data of 5354 patients included in a Japanese nationwide web-based database.* Ann Surg. 2014;260(2):259–266. DOI 10.1097/SLA.0000000000000644. PMID 24743609. — Route: Europe PMC REST（SPEC 提示之 PMID 24368634 實為 Reames 2014，見 S56）。
- **[S55] PASS** — Birkmeyer JD, Siewers AE, Finlayson EV, et al. *Hospital volume and surgical mortality in the United States.* N Engl J Med. 2002;346(15):1128–1137. DOI 10.1056/NEJMsa012337. PMID 11948273. — Route: Europe PMC REST。
- **[S56] PASS** — Reames BN, Ghaferi AA, Birkmeyer JD, Dimick JB. *Hospital volume and operative mortality in the modern era.* Ann Surg. 2014;260(2):244–251. DOI 10.1097/SLA.0000000000000375. PMID 24368634; PMC4069246. — Route: Europe PMC REST。
- **[S57] PASS** — Li B, Hu H, Zhang Y, et al. *Three-field versus two-field lymphadenectomy in transthoracic oesophagectomy for oesophageal squamous cell carcinoma: short-term outcomes of a randomized clinical trial.* Br J Surg. 2020;107(6):647–654. DOI 10.1002/bjs.11497. PMID 32108326. — Route: Europe PMC REST。
- **[S58] PASS（OA）** — Mao Y, Liu S, Han Y, et al. *Three-field vs two-field lymphadenectomy in thoracic ESCC patients: a multicenter randomized study (NST 1503).* J Natl Cancer Cent. 2025;5(2):203–211. DOI 10.1016/j.jncc.2025.01.002. PMID 40265094; PMC12010381. OA:Y. — Route: Europe PMC REST。
- **[S59] PASS** — van Workum F, Verstegen MHP, Klarenbeek BR, et al. *Intrathoracic vs Cervical Anastomosis After Totally or Hybrid Minimally Invasive Esophagectomy for Esophageal Cancer: A Randomized Clinical Trial (ICAN).* JAMA Surg. 2021;156(7):601–610. DOI 10.1001/jamasurg.2021.1555. PMID 33978698; PMC8117060. — Route: Europe PMC REST。
- **[S60] PASS** — Lin SH, Merrell KW, Shen J, et al. *Multi-institutional analysis of radiation modality use and postoperative outcomes of neoadjuvant chemoradiation for esophageal cancer.* Radiother Oncol. 2017;123(3):376–381. DOI 10.1016/j.radonc.2017.04.013. PMID 28455153. OA:N. — Route: Europe PMC REST。
- **[S61] PASS（OA）** — Xiu R, An R, Shan L, et al. *Ivor Lewis minimally invasive oesophagectomy versus McKeown approach: short-term benefits and mid-term equivalence in a randomized trial for oesophageal squamous cell carcinoma.* Surg Endosc. 2026;40(3):1901–1912. DOI 10.1007/s00464-025-12424-7. PMID 41345532; PMC12971774. OA:Y. — Route: Europe PMC REST。

### B4
- **[S62] PASS** — Pimentel-Nunes P, Libânio D, Bastiaansen BAJ, et al. *Endoscopic submucosal dissection for superficial gastrointestinal lesions: European Society of Gastrointestinal Endoscopy (ESGE) Guideline – Update 2022.* Endoscopy. 2022;54(6):591–622. DOI 10.1055/a-1811-7025. PMID 35523224. OA:N. https://doi.org/10.1055/a-1811-7025 — Route: Europe PMC REST；建議句逐字出自摘要（摘要即建議全文）。
- **[S63] PASS** — Yamashina T, Ishihara R, Nagai K, et al. *Long-term outcome and metastatic risk after endoscopic resection of superficial esophageal squamous cell carcinoma.* Am J Gastroenterol. 2013;108(4):544–551. DOI 10.1038/ajg.2013.8. PMID 23399555. — Route: Europe PMC REST。
- **[S64] PASS（無數字可引）** — Xu W, Liu XB, Li SB, Yang ZH, Tong Q. *Prediction of lymph node metastasis in superficial esophageal squamous cell carcinoma in Asia: a systematic review and meta-analysis.* Dis Esophagus. 2020;33(12):doaa032. DOI 10.1093/dote/doaa032. PMID 32399558. — Route: Europe PMC REST。
- **[S65] PASS** — Minashi K, Nihei K, Mizusawa J, et al. *Efficacy of Endoscopic Resection and Selective Chemoradiotherapy for Stage I Esophageal Squamous Cell Carcinoma (JCOG0508).* Gastroenterology. 2019;157(2):382–390.e3. DOI 10.1053/j.gastro.2019.04.017. PMID 31014996. OA:N. — Route: Europe PMC REST（SPEC 給的 PMID 31136741 為誤植）。
- **[S66] PASS** — Tsujii Y, Nishida T, Nishiyama O, et al. *Clinical outcomes of endoscopic submucosal dissection for superficial esophageal neoplasms: a multicenter retrospective cohort study.* Endoscopy. 2015;47(9):775–783. DOI 10.1055/s-0034-1391844. PMID 25826277. — Route: Europe PMC REST。
- **[S67] PASS** — Ono S, Fujishiro M, Niimi K, et al. *Predictors of postoperative stricture after esophageal endoscopic submucosal dissection for superficial squamous cell neoplasms.* Endoscopy. 2009;41(8):661–665. DOI 10.1055/s-0029-1214867. PMID 19565442. — Route: Europe PMC REST。
- **[S68] PASS** — Han C, Sun Y. *Efficacy and safety of endoscopic submucosal dissection versus endoscopic mucosal resection for superficial esophageal carcinoma: a systematic review and meta-analysis.* Dis Esophagus. 2021;34(4):doaa081. DOI 10.1093/dote/doaa081. PMID 32895709. — Route: Europe PMC REST（摘要無百分比，只可引方向）。
- **[S69] PASS（書目）／措辭 FAIL** — Ishihara R, Arima M, Iizuka T, et al. *Endoscopic submucosal dissection/endoscopic mucosal resection guidelines for esophageal cancer.* Dig Endosc. 2020;32(4):452–493. DOI 10.1111/den.13654. PMID 32072683. OA:N。
- **[S70] PASS** — Lee YC, Wang CP, Chen CC, et al. *Transnasal endoscopy with narrow-band imaging and Lugol staining to screen patients with head and neck cancer whose condition limits oral intubation with standard endoscope (with video).* Gastrointest Endosc. 2009;69(3 Pt 1):408–417. DOI 10.1016/j.gie.2008.05.033. PMID 19019362. — Route: Europe PMC REST。
- **[S71] PASS** — Chung CS, Lo WC, Lee YC, Wu MS, Wang HP, Liao LJ. *Image-enhanced endoscopy for detection of second primary neoplasm in patients with esophageal and head and neck cancer: A systematic review and meta-analysis.* Head Neck. 2016;38 Suppl 1:E2343–E2349. DOI 10.1002/hed.24277. PMID 26595056. — Route: Europe PMC REST。
- **[S72] PASS** — Chung CS, Lo WC, Chen KC, et al. *Clinical benefits from endoscopy screening of esophageal second primary tumor for head and neck cancer patients: Analysis of a hospital-based registry.* Oral Oncol. 2019;96:27–33. DOI 10.1016/j.oraloncology.2019.06.038. PMID 31422210. — Route: Europe PMC REST。（正文不點名醫院。）
- **[S73] PASS** — Wang WL, Wang YC, Chang CY, et al. *Human papillomavirus infection on initiating synchronous esophageal neoplasia in patients with head and neck cancer.* Laryngoscope. 2016;126(5):1097–1102. DOI 10.1002/lary.25728. PMID 27107411. — Route: Europe PMC REST。
- **[S74] PASS（OA）** — Tseng CM, Wang HH, Lee CT, et al. *A nationwide population-based study to access the risk of metachronous esophageal cancers in head and neck cancer survivors.* Sci Rep. 2020;10(1):884. DOI 10.1038/s41598-020-57630-6. PMID 31964952; PMC6972960. OA:Y. — Route: Europe PMC REST。
- **[S75] PASS** — Wang CC, Hsu MH, Lee CT, et al. *Prognostic significances of systemic inflammatory response markers in patients with synchronous esophageal and head and neck cancers.* Head Neck. 2024;46(8):1946–1955. DOI 10.1002/hed.27677. PMID 38344911. — Route: Europe PMC REST。
- **[S76] PASS（台灣官方，版本註記）** — 健保署開放資料「醫療服務給付項目及支付標準——現行給付項目」全表 ODS（資源說明「醫療服務給付項目 1140501 生效」；2026-09-02 下載 565,406 bytes）。檢索：72050B 內視鏡黏膜切除術 8,199 點（2022/03/01），適應症含早期食道癌；「黏膜下剝離」0 筆；「質子」僅 N21301–N21308 自費參考項（0 點，HTA 項目）；36015B 電腦治療規劃—複雜 11,483 點（說明含「強度調控放射治療」）。https://data.gov.tw/dataset/9405 （檔案 https://info.nhi.gov.tw/api/iode0000s01/Dataset?rId=A21030000I-D20003-004 ）— Route: curl → 解壓 content.xml 全文檢索。**注意此版本早於 2026-01-01 生效之質子三項，質子給付以 [S87] 為準。**

### B5
- **[S77] PASS** — Lin SH, Hobbs BP, Verma V, et al. *Randomized Phase IIB Trial of Proton Beam Therapy Versus Intensity-Modulated Radiation Therapy for Locally Advanced Esophageal Cancer.* J Clin Oncol. 2020;38(14):1569–1579. DOI 10.1200/JCO.19.02503. PMID 32160096; PMC7213588. OA:N. — Route: Europe PMC REST。
- **[S78] PASS（登錄）** — ClinicalTrials.gov NCT03801876（NRG-GI006）：ACTIVE_NOT_RECRUITING；估 300 人；主要終點 OS 與 G3+ 心肺不良事件；主要完成估 2031-11-07、完成估 2036-11-07；最後更新 2026-08-24。https://clinicaltrials.gov/study/NCT03801876 — Route: CT.gov API v2。
- **[S79] PASS** — Wang J, Wei C, Tucker SL, et al. *Predictors of postoperative complications after trimodality therapy for esophageal cancer.* Int J Radiat Oncol Biol Phys. 2013;86(5):885–891. DOI 10.1016/j.ijrobp.2013.04.006. PMID 23845841; PMC3786201. — Route: Europe PMC REST。
- **[S80] PASS** — Shiraishi Y, Fang P, Xu C, et al. *Severe lymphopenia during neoadjuvant chemoradiation for esophageal cancer: A propensity matched analysis of the relative risk of proton versus photon-based radiation therapy.* Radiother Oncol. 2018;128(1):154–160. DOI 10.1016/j.radonc.2017.11.028. PMID 29248170; PMC5999560. — Route: Europe PMC REST。
- **[S81] PASS** — Xi M, Xu C, Liao Z, et al. *Comparative Outcomes After Definitive Chemoradiotherapy Using Proton Beam Therapy Versus Intensity Modulated Radiation Therapy for Esophageal Cancer: A Retrospective, Single-Institutional Analysis.* Int J Radiat Oncol Biol Phys. 2017;99(3):667–676. DOI 10.1016/j.ijrobp.2017.06.2450. PMID 29280461. — Route: Europe PMC REST。
- **[S82] PASS** — Zhang X, Zhao KL, Guerrero TM, et al. *Four-dimensional computed tomography-based treatment planning for intensity-modulated radiation therapy and proton therapy for distal esophageal cancer.* Int J Radiat Oncol Biol Phys. 2008;72(1):278–287. DOI 10.1016/j.ijrobp.2008.05.014. PMID 18722278; PMC2610812. — Route: Europe PMC REST。
- **[S83] PASS（OA）** — Zhou P, Du Y, Zhang Y, et al. *Efficacy and Safety in Proton Therapy and Photon Therapy for Patients With Esophageal Cancer: A Meta-Analysis.* JAMA Netw Open. 2023;6(8):e2328136. DOI 10.1001/jamanetworkopen.2023.28136. PMID 37581887; PMC10427943. OA:Y. — Route: Europe PMC REST。
- **[S84] PASS（OA）** — Ono T, Wada H, Ishikawa H, Tamamura H, Tokumaru S. *Clinical Results of Proton Beam Therapy for Esophageal Cancer: Multicenter Retrospective Study in Japan.* Cancers (Basel). 2019;11(7):993. DOI 10.3390/cancers11070993. PMID 31315281; PMC6679064. OA:Y. — Route: Europe PMC REST。
- **[S85] PASS（OA）** — Ono T, Wada H, Ishikawa H, Tamamura H, Tokumaru S. *Proton beam therapy is a safe and effective treatment in elderly patients with esophageal squamous cell carcinoma.* Thorac Cancer. 2020;11(8):2170–2177. DOI 10.1111/1759-7714.13524. PMID 32510875; PMC7396394. OA:Y. — Route: Europe PMC REST。
- **[S86] PASS（官方政策文件，re-list）** — ASTRO. *Model Policies: Proton Beam Therapy (PBT)*（PDF，文件未標日期，內文引用至 2022）。Group 1 THORACIC：「Primary cancers of the esophagus」（C15.3–C15.8）。https://www.astro.org/ASTRO/media/ASTRO/Daily%20Practice/PDFs/ASTROPBTModelPolicy.pdf — Route: curl 200（188,920 bytes，2026-09-02）→ pdftotext 逐字確認。
- **[S87] PASS（台灣官方法規，re-list）** — 行政院公報第 031 卷第 245 期：《全民健康保險醫療服務給付項目及支付標準部分診療項目修正》（114 年第 4 次修正，自 115-01-01 生效）：新增 36025B／36026B／36027B 質子放射治療（676,111／1,030,540／1,266,499 點；限未滿十九歲、事前審查、終生一次、包裹）。https://gazette.nat.gov.tw/EG_FileManager/eguploadpub/eg031245/ch08/type1/gov70/num29/images/AA.pdf （2026-09-02 curl 200，388,941 bytes）；同文件健保署鏡像 https://www.nhi.gov.tw/ch/dl-94480-13813b4e7a0a47f98b006aafaa0584ac-1.pdf （200）— Route: curl（沿用 nextgen [S23]／[S19] 之條文抄錄）。
- **[S88] PASS（機構自行公告，re-list＋重新抓取）** — 高雄長庚紀念醫院質子治療中心「收費標準」頁（頁面標示「網站更新時間 2026/03/27」）：質子諮詢診察費 1,000；固定模具 1,950；3D 電腦斷層模擬 8,500；電腦治療規劃費 11,483；MRI 模擬 7,500／12,500；強度調控質子射線治療/次 21,750；中度 26,000；複雜 34,500；一般／複雜呼吸調控/次 5,000／9,600；腦部立體定位套組 230,234；立體定位放射治療套組 330,000（新台幣）。https://www1.cgmh.org.tw/intr/intr4/C83E10/How/How?id=14 — Route: curl 200（31,787 bytes，2026-09-02）→ HTML 去標籤逐項核對。**非食道專屬；引用須標「該院公告、2026/03/27」。**
- **[S89] PASS（台灣官方頁，re-list）** — 衛生福利部醫事司「全國醫用粒子治療設備設置現況」（資料日期 113-12-11）：質子 13 家（營運中 4）、重粒子 3 家（營運中 1）。https://dep.mohw.gov.tw/DOMA/fp-3132-80794-106.html — Route: curl 200（25,532 bytes，2026-09-02）。正文不列院名。
- **[S90] PASS（protocol，無結果）** — Lertbutsayanukul C, Kitpanit S, Kannarunimit D, et al. *High-dose Intensity-modulated proton therapy versus Standard-dose Intensity-modulated RadIation therapy for esophageal squamous cell carcinoma (HI-SIRI): study protocol for a randomized controlled clinical trial.* Trials. 2022;23(1):897. DOI 10.1186/s13063-022-06822-8. PMID 36273186; PMC9587557. OA:Y. — Route: Europe PMC REST。

### FAIL／NOT-CITABLE（保留紀錄）
- **FAIL-1** — CONCORDE／PRODIGE 26 正式論文：Europe PMC 檢索 AUTH:"Crehange G"＋TITLE CONCORDE／PRODIGE 26（2022–2026）零筆；只有 [S5] 會議摘要。SPEC 寫「2023 發表」，未能證實。
- **FAIL-2** — PROTECT-1402 結果：CT.gov hasResults=False、Europe PMC 零筆（只有 protocol [S11]）。不可寫任何結果。
- **FAIL-3** — 中國「You 等」50 vs 60 Gy 鱗癌隨機試驗（SPEC 提及）：Europe PMC TITLE 檢索未見以 You 為第一作者之另一試驗；查到的是 Xu 2022／Cheng 2026 同一試驗。若作者指的是另一篇，需補查。
- **FAIL-4** — CheckMate 577 整體存活最終分析論文：Europe PMC 檢索（"CheckMate 577" AND overall survival AND Kelly RJ，2024–2026；TITLE:"CheckMate 577" 2024–2026）未見原始論文；只能引 [S22] 的轉述句「non-significant overall survival benefit」，不可寫 OS HR。
- **FAIL-5** — ESMO 2022 食道癌指引內文措辭（付費牆，摘要空白）[S42]。ESMO 對免疫治療的原文建議不可引；ASCO 的可引 [S40][S41]。
- **FAIL-6** — 健保署「最新版藥品給付規定內容(分章節)」索引頁 https://www.nhi.gov.tw/ch/np-3397-1.html curl 回 403（Cloudflare）；但第 9 節 PDF 直連 200 [S43]，內容已取得。
- **FAIL-7** — ESCORT-CRT 結果：CT.gov UNKNOWN、Europe PMC／WebSearch 均無結果發表（2026-09-02）。只可寫「未讀出、登錄未更新」[S37]。
- **FAIL-8** — KEYNOTE-975 論文：Europe PMC 零筆（只有 2021 設計論文與會議 TPS）；結果只能引公司 8-K 一句 [S32]。數字（HR、EFS 中位）**不存在於任何可引來源**，不可寫。
- **FAIL-9** — KUNLUN 結果：無；AZ 附件寫 2027 [S39]。
- **FAIL-10** — 台灣 ESD 專屬支付項目：支付標準全表零筆 [S76]；食道切除術的健保項目、台灣食道切除 30/90 天死亡率與住院天數、台灣醫院手術量資料：未查到可引官方來源——gap。
- **FAIL-11** — 台灣食道癌 IMRT 給付專屬條文：未逐條查證——gap。
- **FAIL-12** — 質子食道癌專屬自費套組：高雄長庚頁面無食道專屬項目 [S88]；其他營運中質子中心的官方收費頁本次未查到可用 URL——寫「向各院醫務課確認」。
- **FAIL-13** — Europe PMC 對 SPEC 提示之 PMID 30699875（MIRO）、31136741（JCOG0508）、24368634（日本 NCD）回傳的是無關文獻；正確 PMID 分別為 30625052 [S48]、31014996 [S65]、24743609 [S54]。寫作者引用時請用本 brief 的 PMID。
