# Brief D — 肝癌專題「結束之後」（D1–D5）

研究員：Group D｜查證日期：2026-08-30｜期刊書目資料全部經 Europe PMC REST 逐筆核對（EXT_ID／TITLE／AUTH 查詢，含 DOI、卷期頁）；引語出自可取得之全文 XML（Europe PMC / NCBI efetch）；台灣官方頁面經實際抓取（nhi.gov.tw 的 HTML 頁被 Cloudflare 擋、**PDF 直連可用**，詳 FAIL 區）。
引用規則：**只有標 PASS 的來源可以進正文引用。** FAIL / NOT-CITABLE 條目保留。

**跨組界線（依 SPEC §五）**：移植準則與等待制度→B4（D4、D5 引結果數字、不重新解釋 Milan 準則本身）；急症警語→C2（D3、D4 只留與自己直接相關的一兩條並指向 C2）；抗病毒給付「起始條件」→A4（D3 主場是**長期使用與不可自行停藥**——本 brief 已把現行藥品給付規定 10.7.3 全文抓下，A4 寫起始條件時可自行再引同一份 PDF [S19]）；肝功能名詞→A2；三條路比較→B1。

## ⚠ 四件與 SPEC 假設不同形狀的事（動筆前必讀）

1. **brief A 不存在（截至 2026-08-30 只有 B.md）。** SPEC 指示 D3 沿用 A 組的 HBV 再活化查證——無從沿用。本 brief 自行查證了「停用抗病毒藥之後的發作」整條證據鏈（RETRACT-B 三篇 [S9][S10][S11]），可獨立支撐 D3 的【不可自行中斷】；A 組日後若補上「癌症治療期間 HBV 再活化」的來源，屬 A4 主場，D3 一句話指路即可。
2. **健保 B 肝抗病毒給付的「肝癌條款」查到原文，而且有一個對本專題作者極重要的細節**：藥品給付規定 10.7.3.2.(8) 的「根除性治療」定義清單（手術切除、肝臟移植、RFA、酒精注射、微波消融、冷凍治療）**不含 SBRT／放射治療**[S19]。接受 SBRT 作為根治性治療的 B 肝肝癌病人，除非同時符合肝硬化條款 (5)，否則**可能不符合長期用藥給付資格**。這是 D3（與 B2 交叉）最有價值的台灣特有內容，寫法見 D3 節。
3. **修正 8 說「等待名單數字取不到」——現況已部分改變**：登錄中心（現名「器官捐贈移植登錄及病人自主推廣中心」，網域已從 torsc.org.tw 轉址至 **tosrpapc.org.tw**）每月公告「器官等候人數及捐贈案例統計圖」PDF，115 年 7 月 31 日**等候總人數 11,786 人**可安全擷取；但 PDF 是資訊圖，**各器官別的數字與器官名稱在文字層對不上，肝臟等候人數仍不可歸屬**[S33]。正文仍照修正 8 寫「以登錄中心當日公告為準」，不給肝臟別數字。
4. **EASL 2025 版肝癌指引存在（J Hepatol 2025;82:315–374）但全文在付費牆內、Europe PMC 無全文**——追蹤建議的原文措辭取不到，只能寫「EASL 2025 年版指引存在，我取不到可引用的原文」[S5]。D1 的指引錨點落在 AASLD 2023（全文可得、逐字引語見下）[S1]。

---

## D1 `lv-followup`〈追蹤與 AFP：多久照一次〉

### Key facts

**治療後追蹤排程（AASLD 2023，逐字可引）[S1]**

- 手術切除後：「patients should undergo surveillance following surgical resection with cross-sectional imaging of the abdomen and chest plus serum AFP **every 3–6 months**」——腹部＋胸部斷層影像（CT/MRI）加 AFP，每 3–6 個月一次。
- 證據等級自承很弱（**指引自己承認證據薄，逐字引**）：「Routine postoperative surveillance…every 3–6 months for all patients with HCC following liver resection (**Level 3**, Strong Recommendation). **The optimal timing and duration of surveillance after surgical resection is unknown**, although AASLD recommends indefinite surveillance (**Level 5, Weak Recommendation**).」——排程本身是 Level 3、「追多久」是 Level 5（專家意見）。
- 且「current evidence does not support a survival benefit of **more frequent** surveillance」——更密集追蹤沒有存活證據（這句直接對映 colon D1 的誠實結論，可互相呼應但不引 colon 的來源）。
- 消融／TACE 後：熱消融後約 6 週做多期 CT 或 MRI 評估反應；TARE 或 EBRT（放射）後約 12 週再照；確認無存活腫瘤後「repeat imaging **every 3–6 months** is recommended」[S1]。
- 對照：未治療過的肝硬化族群常規監測是每 6 個月一次超音波±AFP；治療後族群風險更高，所以用斷層影像、間隔縮到 3–6 個月——這個「為什麼治療後反而照得更勤」的邏輯差可以寫[S1]。

**AFP 的誠實極限**

- 診斷敏感度：義大利 1,158 人 HCC 世代（Farinati 2006，多中心、以 20 ng/mL 為切點）：**46% 的肝癌病人 AFP 正常（<20 ng/mL）**；36% 在 21–400；只有 18% >400；作者結論「confirm the low sensitivity (54%) of AFP」[S3]。→「AFP 正常不代表沒有復發」的硬數字。
- 監測情境的敏感度（統合分析，Tzartzeva 2018，32 篇、13,367 位肝硬化病人）：超音波單獨偵測**早期** HCC 敏感度僅 **47%**（95% CI 33–61%）；加上 AFP 升到 **63%**（48–75%）；超音波+AFP 對比單獨超音波 RR 0.81（早期偵測），但特異度較差（RR 1.08 反向）[S2]。→ AFP 的角色是「補影像的漏」，不是獨立判準；反之亦然。
- 註：Tzartzeva 是「肝硬化監測找第一顆腫瘤」的資料，不是治療後族群——外推要標明。治療後族群的 AFP 表現沒有等級相當的統合分析（查無，見 FAIL-2）。

**復發的時間形狀（2 年界線，可引的原始出處）**

- Imamura 2003（東京大學，249 位肝切除病人、157 位有肝硬化）：切除後復發精算機率 1 年 30.1%、3 年 62.3%、**5 年 79.0%**；以 **2 年**為界分析，早期復發（2 年內）的危險因子是非解剖性切除、微血管侵犯、AFP≥32——**轉移型**復發；晚期復發（2 年後）的危險因子是肝炎活動度高、多顆腫瘤——**新生型**（de novo）復發。作者明言這提供「metastasis and de novo 兩種機轉」的流行病學證據[S4]。→「2 年界線」概念的原始可引文獻；細節深挖歸 D2，D1 只用「頭兩年最密、之後也不能停」這一層。
- AASLD 2023 同方向：「the highest risk in the first year after resection」[S1]。

**抓到復發買到什麼**

- AASLD 2023：符合 Milan 準則內復發者可走救援移植（salvage LT）；一項 110 人救援移植策略分析 5 年整體存活 69%[S1]。復發若還小、還侷限，再切、再燒、再照都在選項上（數字歸 D2）；追蹤的目的是把復發抓在「還有根治選項」的窗口內。
- 反向誠實：AASLD 也說了更密集追蹤沒有存活證據[S1]——追蹤排程是共識，不是隨機試驗的勝利。這篇的誠實結構可以與 colon 專題 D1 同構。

### Claim ceiling

- **可寫**：「AASLD 2023 建議切除後每 3–6 個月腹部＋胸部斷層影像加 AFP，並無限期追蹤；但指引自己標注：排程是 Level 3、追蹤時長是 Level 5 專家意見，更密集追蹤沒有存活證據」；「近半數肝癌 AFP 正常（Farinati：46%）；肝硬化監測中超音波+AFP 對早期腫瘤的敏感度也只有六成三（Tzartzeva）」；「切除後 5 年約八成會在肝內再長（Imamura：79%），頭兩年風險最高」；「2 年內與 2 年後的復發，危險因子不同（Imamura）」。
- **不可寫**：「AFP 正常就安心」（46% 復發者可能驗不到）；「追蹤照這個排程就能延長存活」（指引自承無證據）；「AFP 沒有用」（加上 AFP 確實把早期偵測敏感度從 47% 拉到 63%）；不可把 Tzartzeva 的肝硬化監測數字寫成治療後族群的數字（要標明外推）。

### Caveats

- 復發率數字（79%、~70%）的完整脈絡歸 D2，D1 提及時一句話＋指向 D2。
- EASL 2025 措辭取不到——如果要寫「各指引排程略有差異」，只能誠實寫「我取不到 EASL 原文」[S5]。
- 追蹤迴圈是自繪圖 5（fig-lv-surveillance）的素材：影像＋AFP＋肝功能、復發→回到治療的循環，數據皆出自本節 PASS 來源。

---

## D2 `lv-recurrence`〈復發不是失敗，是這個病的常態〉

### Key facts

**復發率（每個數字帶治療方式與族群標籤）**

- **切除後：AASLD 2023 指引原文**：「The risk of recurrence following surgical resection remains high, **approaching 50%–70% at 5 years**, with the highest risk in the first year after resection.」——SPEC 問的「~70%」的精確出處就是這句（指引綜述句，背後引 Pinna 2018 Ann Surg 等）；族群＝接受切除的 HCC 全體[S1]。原始世代對照：Imamura 2003 切除後 5 年精算復發 79.0%（日本單中心、249 人、63% 肝硬化）[S4]。
- **RFA 後（東京大學 1,170 人、10 年系列，Shiina 2012）**：**局部**腫瘤惡化 5 年與 10 年都只有 **3.2%**；但**遠處（肝內他處）復發 5 年 74.8%、10 年 80.8%**[S6]。→「燒掉的那顆很少回來，長的是別處的新顆」的最硬數字。
- **SBRT 後（Asan 前瞻二期，n=50、≤5 cm、中位 1.3 cm，Yoon 2020）**：2 年局部控制 100%、**5 年 97.1%**；5 年整體存活 77.6%；無 ≥G3 毒性[S8]。局部控制極高，但這個試驗規模小、腫瘤小——出場外復發（肝內他處）同樣是主要事件形態（試驗主終點是局部控制，全肝復發率數字不在摘要內，不可自行補）。
- 三種局部治療共同的形狀：**局部復發（原位漏網）是少數，肝內新腫瘤是多數**——這正是「復發不是治療失敗，是肝的問題還在」的證據本體。

**局部復發 vs 新生腫瘤（field disease，可引）**

- Imamura 2003 的早期／晚期二分：早期（<2 年）復發與腫瘤因子（微血管侵犯、非解剖切除、AFP）相關＝轉移型；晚期（>2 年）與肝炎活動度、多顆性相關＝**硬化肝的新生癌**（de novo）；作者直接寫這是「metastasis and de novo 兩種機轉」的證據[S4]。→「整片肝都是病田（field disease）」的可引錨點。
- 呼應 Shiina：局部 3.2% 對遠處 80.8% 的巨大落差，就是 field disease 的另一面[S6]。

**再治療的路（誠實版）**

- **復發小肝癌的隨機試驗（Xi 2025，JCO）**：單顆 ≤5 cm **復發性** HCC，SBRT 83 vs RFA 83（中國中山大學、單中心、開放標籤）；主要終點局部無惡化存活 SBRT 顯著較優（HR 0.45，95% CI 0.24–0.87，p=0.014；2 年 92.7% vs 75.8%，作者標明優勢尤其在 ≤2 cm）；PFS（中位 37.6 vs 27.6 月，HR 0.76，p=0.190）、2 年 OS（97.6% vs 93.9%，p=0.830）、急性與晚期不良事件均無差異[S7]。→ D2 用它說「復發後再治療是真的路、而且有隨機證據」；**三條路的初治比較歸 B1，此處不重比**（B1 的 brief 以自己的 S4 收錄同一試驗）。
- **救援移植**：AASLD 2023——Milan 內復發可走救援移植，110 人策略分析 5 年 OS 69%、55% 的世代最終被切除治癒或成功移植；但「**less than 50%** of patients with HCC who develop postresection recurrence are deemed candidates for salvage LT」，主因是肝外復發或超出 Milan；微血管侵犯與衛星病灶是「無法移植的復發」最重要的預測因子[S1]。台灣制度面歸 B4／D5。
- **復發何時改變治療目標**：肝外復發、超出準則、肝功能不允許再局部治療→轉全身治療（細節歸 C3）；AASLD 的救援移植資格句（上引）就是「還在根治窗口內／已出窗口」的分界線素材[S1]。

### Claim ceiling

- **可寫**：「切除後 5 年復發率接近五到七成（AASLD 指引語）、單一世代高到 79%（Imamura）」；「RFA 後 10 年：局部只有 3.2%，肝內他處 80.8%（Shiina）」；「SBRT 前瞻試驗 5 年局部控制 97.1%（Yoon，n=50、中位 1.3 cm）」；「復發的多數不是原位失敗，而是硬化肝長出的新腫瘤（Imamura 的早晚期二分）」；「復發後再治療有一個 166 人的隨機試驗（復發性單顆 ≤5 cm）：SBRT 局部控制優於 RFA、存活與毒性無差異（Xi 2025）」；「Milan 內復發可評估救援移植（110 人分析 5 年存活 69%），但切除後復發者不到一半符合資格」。
- **不可寫**：「復發了也沒關係」（半數以上復發者到不了救援移植）；「SBRT 優於 RFA」的一般句（Xi 只涵蓋復發性單顆 ≤5 cm、單中心；同 B 組修正 1 的紀律）；「復發率 70%」不帶「切除後、5 年」標籤；不可把 Yoon 的 97.1% 寫成「SBRT 治療後 97% 不復發」（那是**局部**控制，肝內他處復發另計）；不可暗示追蹤密一點復發就少一點（D1 已寫無此證據）。

### Caveats

- 這篇的核心情緒工作：把「復發＝我失敗了／醫師失敗了」改寫成「肝還在生病」。Imamura 與 Shiina 的數字結構正好支撐，不需要打氣話術。
- 抗病毒藥降復發（Wu 2012）歸 D3，本篇一句話指路。
- 紅線 4：任何re-treatment 段落不可讓符合準則的年輕病人略過移植評估——救援移植段落必須在再切／再燒／再照之前或並列，不可墊底。

---

## D3 `lv-liver-care`〈治療結束後，肝還要顧一輩子〉【不可自行中斷】

### Key facts

**停藥之後會發生什麼（RETRACT-B 全球世代，含台灣多中心）**

- 主世代（Hirode 2022，Gastroenterology；n=1,552，病毒抑制中、停藥時 HBeAg 陰性）：停藥後 HBsAg 清除率 12 個月 3.2%、48 個月 13.0%——而且明顯偏白人（vs 亞洲人 sHR 6.8）與停藥時 HBsAg <100 IU/mL 者；**亞洲病人要 HBsAg<100 才有較高的功能性治癒機會**。停藥後肝代償不全發生率 0.48/1000 人年，發生者 **19 人中 7 人死亡**[S11]。
- 發作（flare）數字（Dongelmans 2025，J Hepatol；n=1,552）：停藥後 ALT≥5 倍上限的 flare **1 年累積發生率 18.6%**（≥10 倍 10.2%、≥20 倍 3.4%）；350 個 flare 中 70.6% 發生在第一年；**13 人在 flare 後肝代償不全、其中 3 人死亡**；flare 並未換到較高的 HBsAg 清除（aHR 1.42，p=0.28）；年齡較大、男性、停藥時 HBsAg 高（>1,000 IU/mL aHR 2.65）、TDF（vs entecavir，aHR 2.99）是危險因子；停藥後 12 週內 HBV DNA >10⁵ IU/mL 者風險最高（aHR 2.36），作者建議此時回頭治療[S10]。
- 肝代償不全專文（Hirode 2023，Am J Gastroenterol；n=1,557）：停藥後 60 個月肝代償不全累積發生率**全體 1.8%**、非肝硬化＋鞏固治療 ≥12 個月的次組 1.1%；肝硬化者 HR 5.08、起始治療時 HBeAg 陽性者 HR 5.23（次組內 HR 10.5）[S9]。**注意：此文 2024 年刊出更正啟事（Am J Gastroenterol 2024;119(10):2145），更正內容無法取得（FAIL-7）——引用этих數字時下筆前建議再對出版社勘誤頁**。
- 指引層的定錨（AASLD 2018 B 肝指引，逐字）：「**Treatment discontinuation in persons with cirrhosis is not recommended owing to the potential for decompensation and death**」；停藥者應每 3 個月監測至少一年[S12]。失代償肝硬化：無限期治療；肝臟移植後：「Therapy should be continued posttransplant **indefinitely**」[S12]。
- 【不可自行中斷】的寫法：上面全部是「**由醫師評估後、符合條件的停藥**」的結果——即使如此，五分之一的人一年內 flare、少數人失代償死亡。**自行停藥＝沒有監測、沒有再治療的觸發線**，是把同樣的風險裸放。這一段是紅線主場。

**台灣健保給付的張力（現行條文逐字取得）[S19]**

- 來源：《全民健康保險藥品給付規定》第 10 節抗微生物劑（nhi.gov.tw 官方 PDF，內文修訂標記至 **114/6/1**），B 肝口服抗病毒藥條文在 **10.7.3**（lamivudine／entecavir／telbivudine／TDF／TAF）。
- **一般慢性 B 肝（無肝硬化、HBeAg 陰性）有停藥條款**：「治療至少二年，治療期間需檢驗血清 HBV DNA，並於檢驗血清 HBV DNA 連續三次，每次間隔 6 個月，均檢驗不出 HBV DNA 時停藥，**每次療程至多給付 36 個月**」（10.7.3.4）。→ 健保的療程上限與 RETRACT-B 的 flare 數字之間的張力是真的：**依規定停藥的人，正是 RETRACT-B 追蹤的那種人**。
- **可長期使用（不受 36 個月限制）的三個與本專題相關的條款**：
  - (5) **肝硬化病患，可長期使用**（需 HBsAg(+) 且可測到 HBV DNA＋影像／切片／肝彈性檢查等診斷標準，Fibroscan≥12 kPa 等同 F4）；
  - (8) **「確診為肝癌並接受根除性治療且可檢驗到血清 HBV DNA，可長期使用，直至肝癌復發且未能再次接受根除性治療止。」**（108/2/1、110/3/1）
  - (3) 接受肝臟移植者，可預防性使用（D4 相關）。
- **條款 (8) 的兩個精確細節（本篇最重要的台灣內容）**：
  - 註 a（109/1/1）：「根除性治療包括**手術切除、肝臟移植、射頻燒灼、局部酒精注射及微波消融、冷凍治療**。」——**清單裡沒有 SBRT／放射治療**。接受 SBRT 根治的 B 肝肝癌病人，若無肝硬化診斷，依條文字面可能不符長期給付資格（註 b：已符合肝硬化條款者不在此限）。寫法：如實攤開條文＋「這一項在你身上怎麼適用，要請你的醫師與個管師對條文確認」，**不可寫成「健保不給付」的斷言**（實務認定可能不同），也不可假裝沒這件事。
  - 「直至肝癌復發且未能再次接受根除性治療止」——復發而無法再根治時，長期給付的法源就停了；此時是否自費續用是要在門診談的真問題。**這句條文本身就是「復發改變的不只是治療、還有給付」的素材。**
- 給付放寬的方向可引：衛福部新聞稿（112-09-22）：112 年 10 月 1 日起 e 抗原陰性者 ALT 異常次數由 2 次放寬為 1 次、纖維化門檻由 F3 放寬為 F2，估新增 21,000 人受惠[S20]。→「健保給付逐步向國際指引靠攏」的官方句；起始條件的完整版歸 A4。
- **抗病毒藥在肝癌治療後值多少（台灣自己的證據）**：Wu 2012（JAMA，台灣健保資料庫全國世代）：4,569 位 B 肝相關肝癌肝切除病人，有用核苷酸類似物（n=518）對未用（n=4,051），校正競爭死亡後 **6 年復發率 45.6% vs 54.6%**、6 年整體死亡 29.0% vs 42.4%；用藥的校正 HR 0.67（95% CI 0.55–0.81）[S14]。觀察性、健保資料庫——不可寫成隨機證據，但這是「為什麼治療結束後藥更不能停」的台灣本土數字。

**病毒壓下來／清掉之後，肝癌風險還在（數字）**

- C 肝治癒後（Kanwal 2017，美國退伍軍人系統 22,500 人 DAA 世代）：SVR 把 HCC 風險降 72%（aHR 0.28），但**有肝硬化者 SVR 後年發生率仍 1.82/100 人年**——超過監測閾值，「治癒了病毒，沒治癒肝」[S15]。
- B 肝長期抑制下（Papatheodoridis 2017，歐洲 1,951 人 entecavir/TDF 世代）：治療 5 年後 HCC 年發生率從 1.22% 降到 0.73%；肝硬化者由 3.22% 降到 1.57%——**下降但不歸零**；5 年後發生 HCC 者全部超過 50 歲[S16]。高加索族群——外推到台灣要標明。
- 兩個數字合起來的訊息：**抗病毒是降風險，不是除風險；追蹤（D1）與顧肝（本篇）是同一件事的兩半。**

**再代償（recompensation）——Baveno VII 定義逐字[S13]**

- 7.22：「The concept of recompensation implies that there is at least partial regression of the structural and functional changes of cirrhosis after removal of the aetiology of cirrhosis.」
- 7.23（診斷要件，專家共識 C.2）：三條全要——(1) 病因移除／抑制／治癒（C 肝病毒清除、**B 肝持續病毒抑制**、酒精性肝硬化持續戒酒）；(2) 腹水（停利尿劑）、肝性腦病變（停 lactulose/rifaximin）緩解且**至少 12 個月**無再發靜脈曲張出血；(3) 肝功能（白蛋白、INR、膽紅素）穩定改善。
- 7.25：只有腹水消了、沒出血，但病因沒處理、合成功能沒改善——**不算再代償**。
- 用途：給病人一個「肝真的可以部分回來」的可引概念，同時把條件寫死——它的第一條就是抗病毒不能斷、酒要戒到零。

**酒精與代謝**

- 酒精（HBV 族群統合分析，Wu 2025：45 篇、33,272 人）：喝酒者肝硬化 OR 2.61、HCC OR 2.27；**每天每多 12 克酒精（約一罐啤酒），肝硬化風險 +6.2%、HCC 風險 +11.5%**——線性劑量反應、沒有安全下限的訊號[S17]。AASLD 2018 指引句：「the conservative approach is to recommend **abstinence** or minimal alcohol ingestion」＋「Abstinence or only limited use of alcohol is recommended in HBV-infected persons」[S12]。→「零」是保守但有據的建議；證據是觀察性劑量反應，不是隨機試驗——寫「我建議歸零，因為查不到任何安全劑量」而不是「已證明一滴都會致癌」。
- 代謝共病（MASLD 重疊誠實段）：Huang 2021（Nat Rev Gastroenterol Hepatol 綜述）：全球約四分之一人口有脂肪肝；NASH 肝硬化者 HCC 年發生率 0.5–2.6%、無肝硬化 NAFLD 約 0.1–1.3/1000 人年；NAFLD 是美英法成長最快的 HCC 病因[S18]。AASLD 2018 指引句：「Optimization of body weight and treatment of metabolic complications, including control of diabetes and dyslipidemia, are recommended」[S12]。→ 台灣 B 肝病人同時有脂肪肝／糖尿病者，兩個風險是相加的——寫成「病毒之外的第二條戰線」，不給體重數字目標（無可引來源）。
- 疫苗與一般顧肝：AASLD 2018——慢性 B 肝者未具 A 肝免疫力應接種 A 肝疫苗；家戶與性伴侶血清陰性者應接種 B 肝疫苗[S12]。台灣公費成人 A 肝疫苗政策查無可引官方頁（FAIL-6）→寫「向診間或衛生所確認」。

### Claim ceiling

- **可寫**：「符合條件、由醫師執行的停藥，一年內仍有 18.6% 出現 ALT 五倍以上的發作，全球世代裡有人因此失代償、死亡（13 人失代償、3 人死亡）」；「停藥後 60 個月失代償累積 1.8%，肝硬化者風險五倍」；「指引明文：肝硬化者不建議停藥，理由是失代償與死亡」；「健保對一般 B 肝有 36 個月療程上限與停藥條款，但**肝硬化與接受根除性治療的肝癌病人可長期給付**——條文的根除性治療清單不含放射治療，適用要逐案確認」；「台灣全國世代：切除後有用抗病毒藥，6 年復發率 45.6% 對 54.6%（觀察性）」；「SVR 後肝硬化者 HCC 年風險仍 1.82%；B 肝抑制 5 年後肝硬化者仍 1.57%」；「Baveno VII 的再代償定義（三條件並列）」；「每天多 12 克酒精，HCC 風險多 11.5%（HBV 族群統合）」。
- **不可寫**：「條件好就可以停藥」（本專題讀者是肝癌病人——肝癌條款與肝硬化條款都指向長期使用；停藥討論只適用於極少數、且必須由醫師啟動）；「健保不給付 SBRT 病人的抗病毒藥」（條文清單未列≠實務必然拒付——寫「條文如此、請對條文確認」）；「停藥會死」恐嚇句（絕對風險要如實：失代償 1.8%/60 月）；「抗病毒藥防復發」寫成因果定論（Wu 2012 是觀察性）；「戒酒就不會復發」；「再代償=痊癒」。
- 【不可自行中斷】紅線句式：「這顆藥的作用在於**每天都在**。任何『先停兩週看看』都是在沒有監測的情況下重演 RETRACT-B 的曲線。想停、想換、拿不到藥、負擔不起——都是門診當天要說的事，不是自己決定的事。」

### Caveats / safety notes

- RETRACT-B 世代是「停藥時 HBeAg 陰性、病毒抑制中」的**選過的病人**——真實世界自行停藥者風險只會更高，不會更低。這個方向性要寫。
- Hirode 2023 有更正啟事未取得（FAIL-7）——動筆時如引 1.8%/HR 5.08 等數字，先查勘誤。
- flare 的急症症狀（黃疸、茶色尿、極度倦怠）一句話＋指向 C2，不在本篇展開警訊清單。
- C 肝 DAA 治療本身（起始、給付）歸 A4；本篇只寫「治癒後風險仍在」。

### Taiwan status

- **PASS**：藥品給付規定第 10 節全文 PDF（10.7.3 全條文；36 個月上限、肝硬化長期條款、肝癌根除性治療長期條款＋清單無 SBRT）[S19]。
- **PASS**：衛福部 112-10-01 放寬新聞稿[S20]。
- **PASS**：Wu 2012 台灣健保資料庫世代[S14]。
- **gap**：SBRT 病人依條款 (8) 申請長期抗病毒的實務通過率／函釋——查無公開資料；寫成要逐案確認。
- **gap**：成人 A 肝疫苗公費對象官方頁未取得（hpa.gov.tw SSL 失敗，見 FAIL-6）。

---

## D4 `lv-post-transplant`〈換肝之後的日子〉

### Key facts

**免疫抑制與服藥紀律**

- Dew 2007（統合分析，147 篇、跨器官）：移植後**免疫抑制劑不遵囑率每年每百人 19–25 例**（各項醫囑範圍 1–36）；肝移植受者低於腎移植（腎 36/100 人年、其他器官 7–15）；人口學與社會支持幾乎不能預測誰會不遵囑[S23]。→「不是特定哪種人才會漏藥，是每個人都會」的寫法基礎。
- 免疫抑制劑與腫瘤：AASLD 2023——鈣調磷酸酶抑制劑（CNI）暴露與 HCC 復發升高相關；mTOR 抑制劑看似有抗腫瘤性質；SiLVER 第三期試驗整體未證明 sirolimus 改善 5 年後的長期無復發存活，但 **Milan 準則內的次族群**無復發存活改善[S1]。→ 只能寫「藥怎麼配是移植團隊的專業判斷、有試驗在背後」，不可寫成病人可以要求換藥的建議。

**移植後 HCC 復發（帶準則標籤）**

- 原始 Milan（Mazzaferro 1996，n=48，準則內為主）：4 年整體存活 75%、無復發存活 83%、復發 4 人（8%）；病理超出準則者 4 年存活掉到 50%[S21]。
- AASLD 2023 總結句：「Even with adherence to the Milan criteria, **HCC recurs post-LT in 10%–15%** and is the most common cause of death in this population.」復發後預後差：<20% 可切除、免疫檢查點抑制劑不可用（排斥風險）、復發後中位存活約 1 年[S1]。
- 風險分層：RETREAT 分數（AFP、血管侵犯、外植體腫瘤負荷）5 年復發風險由 <3%（RETREAT 0）到 75%（≥5）[S1]。
- 移植後監測（AASLD）：復發最常見部位是**肺（~40%）與肝（33%）**→建議腹部多期 CT/MRI＋**胸部 CT**（不用超音波）；最佳頻率與年限「uncertain」——又一處指引自承證據薄；一項多中心研究顯示掃得多與抓到可根治復發、復發後存活較好相關（觀察性）[S1]。

**新生惡性腫瘤與皮膚癌**

- Engels 2011（美國移植登錄 × 癌症登錄，175,732 件移植、21.6% 為肝）：移植受者整體癌症風險 SIR 2.10（每年每十萬人 1,375 例）；非何杰金氏淋巴瘤 SIR 7.54、肺癌 SIR 1.95（肝受者）、腎癌 SIR 1.80（肝受者）；**黑色素瘤與唇癌也升高**（感染無關癌別）[S22]。→「免疫抑制的帳單包含第二種癌」的硬數字；防曬與皮膚檢查建議可以掛在黑色素瘤/唇癌風險上，不可加碼發明頻率。
- 台灣本土資料存在但取不到數字：高雄長庚 LDLT 世代的皮膚癌 vs 整體新生惡性腫瘤發生率（Br J Dermatol 2026 通訊，NOT-CITABLE，見 FAIL-8）——只能寫「台灣移植中心有本土資料，皮膚癌在亞洲受者相對少見但非零」**不可引數字**；或干脆不提。
- B 肝復發預防：AASLD 2018——移植後抗病毒**無限期**（「Therapy should be continued posttransplant indefinitely, regardless of HBeAg or HBV DNA status」）；HBIG 用法各中心不同[S12]。健保條文：10.7.3.2.(3) 接受肝臟移植者可預防性使用[S19]。

**活體捐贈者安全（一段誠實）**

- A2ALL 世代（Abecassis 2012，n=740 完成捐肝）：**40% 捐贈者出現併發症**（296 人共 557 件），絕大多數 Clavien 1–2 級；3 級（殘留失能）5 件、4 級（導致死亡）3 件；疝氣（7%）與心理併發症（3%）可在捐後一年以上出現；一年內併發症緩解率整體 95%，疝氣 75%、心理 42%[S24]。
- 全球調查（Cheah 2013，71 個計畫、11,553 次捐肝）：**捐贈者死亡率 0.2%**（23/11,553）、平均併發症率 24%、近致命事件 1.1%、中止手術 1.2%；死亡率與中心經驗無關[S25]。
- 寫法：兩個數字並列（0.2% 死亡、24–40% 併發症多為輕度），不粉飾也不嚇阻；「捐贈者有自己的醫療團隊與獨立評估」一句帶過（制度細節歸 B4）。

**台灣端**

- 免疫抑制劑健保給付（現行藥品給付規定第 8 節 PDF，修訂標記至 115/3/1）：**8.2.1 cyclosporin：「器官移植抗排斥藥物」；8.2.2.2 tacrolimus 注射劑及非持續性口服製劑：「肝臟及腎臟移植之第一線用藥」**；tacrolimus 持續性（緩釋）口服製劑為成人肝、腎移植 cyclosporin 無效之第二線[S26]。→ 核心抗排斥藥有健保給付、有明文。
- **gap**：mycophenolate、everolimus、sirolimus 用於肝移植的給付規定條文——第 8 節全文查無專條（可能依藥品許可適應症一般給付）；不可宣稱「全部免疫抑制劑都給付」，寫成「主力藥物有給付、你的組合請與移植團隊及個管師確認」。
- 台灣移植存活（官方、舊）：衛福部（健保局）102-03-22 新聞稿：2001–2011 全國 2,623 例肝移植，術後 3 年存活率約 80%、5 年約 76%、10 年約 70%；資料未校正術前嚴重度[S27]。→ 標明年代與限制後可用一次。
- 重大傷病與部分負擔歸 A5；移植登錄制度歸 B4。

### Claim ceiling

- **可寫**：「Milan 內移植後復發 10–15%（AASLD），復發後中位存活約 1 年、多數無法再根治」；「復發最常在肺與肝，所以追蹤用 CT 而不是超音波——但最佳頻率指引自承不確定」；「移植受者整體癌症風險約兩倍（SIR 2.10），淋巴瘤、肺癌、黑色素瘤、唇癌都升高」；「免疫抑制劑不遵囑率約每年五分之一，肝移植者較低但不是零」；「捐肝者死亡率 0.2%、併發症 24–40% 多為輕度，疝氣與心理併發症可以晚到一年後」；「tacrolimus 是健保給付的肝移植第一線抗排斥藥（條文引錄）」；「移植後 B 肝抗病毒無限期（AASLD）、健保有預防性使用條款」。
- **不可寫**：「換了肝就不會再有肝癌」；「復發率只有 8%」不帶（1996 年、48 人、準則內）標籤；「掃得勤活得久」寫成因果（觀察性）；「sirolimus 防復發」（SiLVER 主終點陰性，只有次族群訊號）；「所有免疫抑制劑健保都有給付」；「捐肝很安全」或「捐肝很危險」的單邊句。

### Caveats

- 排斥的急症症狀（發燒、黃疸、腹痛）一句話指向 C2 格式，但移植病人的警訊由移植團隊個別交代——寫「你的名單以移植團隊給的為準」。
- 免疫檢查點抑制劑在移植後禁忌／高風險（AASLD：ineligibility for ICIs）——與 C3 交叉，一句話即可。
- Milan 準則內容本身歸 B4，本篇用「準則內／外」時不重新定義。

---

## D5 `lv-bridging`〈在等待名單上的日子〉

### Key facts

**橋接治療的證據（誠實：全是觀察性）**

- Kulik 2018（AASLD 委託系統性回顧＋統合，至 2016/4）：**沒有任何隨機試驗**。T2（Milan 內）等待者：橋接治療對「因惡化退出名單」RR 0.32（95% CI 0.06–1.85）、對全因退出 RR 0.38（0.06–2.37）——方向有利但**不顯著、證據品質極低**；移植後存活與復發：5 篇／10 篇比較研究皆無顯著差異。T1：一系列橋接後 6 個月退出 5.3%，另一系列未橋接者中位 2.4 年退出 30%。T3（超出準則）降期後移植：1 年移植後存活 RR 1.11（1.01–1.23）、5 年 RR 1.17（1.03–1.32）——顯著但證據品質極低[S28]。
- AASLD 2023 的實務句：因 MELD 例外需等 6 個月，橋接（TACE、TARE、消融、**EBRT**）常規用於控制腫瘤、降低退出風險；「currently **no one type of LRT is recommended over another** for bridging therapy」；橋接期間腫瘤行為本身是選擇移植候選人的資訊；不建議常規用全身治療當橋接[S1]。→ EBRT 被 AASLD 明文列入橋接選項清單——SBRT 的正當席位是指引原文，不用比較性研究撐。
- 橋接對肝功能的代價：AASLD——LRT 可能造成失代償，建議肝功能足夠者（如 CTP A–B、bilirubin ≤3）才嘗試降期[S1]。→ 紅線 3 的移植版。

**SBRT 作為橋接（可引系列，標回溯）**

- Sapisochin 2017（多倫多，意向治療分析，2004–2014）：379 位等待者，SBRT 36 vs TACE 99 vs RFA 244；**退出率 16.7% vs 20.2% vs 16.8%（p=0.7）**；自列名起 5 年存活 61% vs 56% vs 61%（p=0.4）；自移植起 5 年 75% vs 69% vs 73%（p=0.7）；術後併發症相當；RFA 組外植體壞死較多。結論：SBRT 可以安全作為橋接替代[S29]。**回溯性、單中心、SBRT 組僅 36 人**——寫「打平」要帶這三個標籤；不可寫「SBRT 橋接較好」。

**降期（downstaging）**

- Parikh 2015（系統性回顧＋合併分析，13 篇 950 人）：降到 Milan 內成功率合併 **48%**（前瞻性研究 68% vs 回溯 44%）；降期後移植者移植後 HCC 復發合併 **16%**（12 篇 320 人）——高於一般準則內移植[S30]。
- **XXL 隨機試驗（Mazzaferro 2020，Lancet Oncol，義大利 9 中心）**：Milan 外、無大血管侵犯／肝外轉移、Child-Pugh A–B7，74 人進入降期；**29 人（39%）在隨機分派前就退出**；45 人降期成功且穩定 3 個月後隨機：移植 23 vs 非移植續治 22；5 年腫瘤無事件存活 76.8% vs 18.3%（HR 0.20，p=0.003）、**5 年整體存活 77.5% vs 31.2%**（HR 0.32，95% CI 0.11–0.92，p=0.035）；因分配政策改變提前關閉，作者自己說結果須謹慎解讀[S30→S31 見來源區編號][S31]。→「降期成功且撐過觀察期的人，移植帶來的差距是巨大的」＋「但十個裡近四個到不了隨機那一步」兩句都要寫。
- AASLD 2023 制度句：UNOS-DS 內降到 Milan 內→觀察 3–6 個月後可獲 MELD 例外；**AFP >1000 ng/mL 者須降到 <500** 才算降期成功；放寬降期範圍→成功率更低、退出更多、移植後存活較差[S1]。台灣的登錄與分配制度歸 B4，本篇不重複。

**台灣的現實：活體移植為主**

- 可引（同儕審查、開放取用）：Wen 2018（台灣健保資料庫研究）內文：「in East Asia, including **Taiwan where more than 80% of LT are LDLT**」——台灣八成以上肝移植是活體[S32]。二手陳述（引自其參考文獻）——標「該研究引述」；官方的活體／屍肝分別統計未取得（FAIL-4）。
- 活體移植改寫等待的邏輯：AASLD——LDLT 可縮短等待、降低退出風險，對 HCC 者移植後存活佳[S1]。等待名單上的日子對「有活體捐贈者」與「沒有」的病人是兩種完全不同的時間表——這是本篇的台灣主軸。捐贈者安全數字歸 D4（一句話指向）。
- 等候人數：登錄中心官方頁「器官等候資訊」為動態載入、單月統計圖 PDF 的器官別數字無法安全歸屬（115 年 7 月 31 日**等候總人數 11,786 人**可引，含所有器官）[S33]。**正文照修正 8：肝臟等候人數寫「以登錄中心當日公告為準」並附官方頁指路，不給數字。**

### Claim ceiling

- **可寫**：「橋接治療沒有隨機試驗；系統性回顧顯示方向有利但不顯著、證據品質極低（Kulik）」；「AASLD 明文把 EBRT 列入橋接選項，且不建議任何一種優於另一種」；「多倫多十年系列：SBRT 橋接的退出率與移植後存活跟 TACE/RFA 看不出差別（回溯、n=36）」；「降期成功率約半數（前瞻性研究較高）、降期後移植復發約 16%」；「XXL：降期成功者隨機分派，移植組 5 年存活 77.5% 對 31.2%——但 39% 的人到不了隨機、試驗提前關閉」；「台灣八成以上肝移植是活體（研究引述）」；「等候人數以登錄中心當日公告為準」。
- **不可寫**：「橋接治療已證明降低退出」（RR 不顯著）；「SBRT 是更好的橋接」（打平、回溯、36 人）；「降期就能移植」（一半降不成、成了還要觀察期、AFP 門檻另計）；「XXL 證明超出準則也該移植」（是降期**成功**者的試驗、n=45、提前關閉）；肝臟等候人數的任何具體數字；「活體移植沒有等待問題」（捐贈者評估本身需時間，且捐贈者安全是真實代價——指向 D4）。

### Caveats / safety notes

- 紅線 4 主場之一：本篇任何段落不可讓讀者覺得「先做局部治療、移植以後再說」——橋接的目的是**保住移植資格**，不是取代移植；AASLD 的「LRT 造成失代償反而失格」句要寫。
- 等待期的惡化警訊（腹水、腦病變、出血）指向 C2。
- 降期治療的選擇（TACE/TARE/SBRT 組合）是多專科決定，本篇不給演算法。

---

## Sources（單一序列；只有 PASS 可引用。Route：EPMC=Europe PMC REST 查詢核對書目；NCBI-XML=efetch 全文逐字引語；官方抓取=curl 實際下載）

- [S1] **PASS** Singal AG, Llovet JM, Yarchoan M, et al. (2023). AASLD Practice Guidance on prevention, diagnosis, and treatment of hepatocellular carcinoma. Hepatology, 78(6), 1922–1965. DOI: 10.1097/HEP.0000000000000466. PMID 37199193；PMC10663390。Route: EPMC 書目＋NCBI-XML 全文（引語逐字擷取：切除後 3–6 月追蹤／Level 3+5／50–70%／救援移植 69%、<50%／移植後 10–15%、肺 40% 肝 33%／RETREAT／CNI-mTOR-SiLVER／橋接與降期全段／AFP>1000→<500）。https://doi.org/10.1097/HEP.0000000000000466
- [S2] **PASS** Tzartzeva K, Obi J, Rich NE, et al. (2018). Surveillance Imaging and Alpha Fetoprotein for Early Detection of Hepatocellular Carcinoma in Patients With Cirrhosis: A Meta-analysis. Gastroenterology, 154(6), 1706–1718.e1. DOI: 10.1053/j.gastro.2018.01.064. PMID 29425931。Route: EPMC＋摘要數字核對。https://doi.org/10.1053/j.gastro.2018.01.064
- [S3] **PASS** Farinati F, Marino D, De Giorgio M, et al. (2006). Diagnostic and prognostic role of alpha-fetoprotein in hepatocellular carcinoma: both or neither? Am J Gastroenterol, 101(3), 524–532. DOI: 10.1111/j.1572-0241.2006.00443.x. PMID 16542289。Route: EPMC＋摘要（46%<20 ng/mL；敏感度 54%）。https://doi.org/10.1111/j.1572-0241.2006.00443.x
- [S4] **PASS** Imamura H, Matsuyama Y, Tanaka E, et al. (2003). Risk factors contributing to early and late phase intrahepatic recurrence of hepatocellular carcinoma after hepatectomy. J Hepatol, 38(2), 200–207. DOI: 10.1016/S0168-8278(02)00360-4. PMID 12547409。Route: EPMC＋摘要（1/3/5 年復發 30.1/62.3/79.0%；2 年界線；早晚期危險因子；de novo 結論句）。https://doi.org/10.1016/S0168-8278(02)00360-4
- [S5] **PASS（書目限定）** European Association for the Study of the Liver (2025). EASL Clinical Practice Guidelines on the management of hepatocellular carcinoma. J Hepatol, 82(2), 315–374. DOI: 10.1016/j.jhep.2024.08.028. PMID 39690085。Route: EPMC 書目核對；**全文付費牆、EPMC 無全文——內文措辭不可引用**，正文只能寫「EASL 2025 指引存在、原文我取不到」。https://doi.org/10.1016/j.jhep.2024.08.028
- [S6] **PASS** Shiina S, Tateishi R, Arano T, et al. (2012). Radiofrequency ablation for hepatocellular carcinoma: 10-year outcome and prognostic factors. Am J Gastroenterol, 107(4), 569–577. DOI: 10.1038/ajg.2011.425. PMID 22158026；PMC3321437。Route: EPMC＋摘要（局部 5/10 年 3.2%；遠處 74.8%/80.8%）。https://doi.org/10.1038/ajg.2011.425
- [S7] **PASS** Xi M, Yang Z, Hu L, et al. (2025). Radiofrequency Ablation Versus Stereotactic Body Radiotherapy for Recurrent Small Hepatocellular Carcinoma: A Randomized, Open-Label, Controlled Trial. J Clin Oncol, 43(9), 1073–1082. DOI: 10.1200/JCO-24-01532. PMID 39693584。Route: EPMC＋摘要（LPFS HR 0.45、2 年 92.7% vs 75.8%；PFS/OS/毒性無差異；≤2 cm 註記）。https://doi.org/10.1200/JCO-24-01532
- [S8] **PASS** Yoon SM, Kim SY, Lim YS, et al. (2020). Stereotactic body radiation therapy for small (≤5 cm) hepatocellular carcinoma not amenable to curative treatment: Results of a single-arm, phase II clinical trial. Clin Mol Hepatol, 26(4), 506–515. DOI: 10.3350/cmh.2020.0038. PMID 32646200；PMC7641557。Route: EPMC＋摘要（2 年 LC 100%、5 年 97.1%、5 年 OS 77.6%、無 ≥G3）。https://doi.org/10.3350/cmh.2020.0038
- [S9] **PASS（附更正警示）** Hirode G, Hansen BE, Chen CH, et al.; RETRACT-B study group (2023). Incidence of Hepatic Decompensation After Nucleos(t)ide Analog Withdrawal (RETRACT-B Study). Am J Gastroenterol, 118(9), 1601–1608. DOI: 10.14309/ajg.0000000000002203. PMID 36719174。**2024 年刊出更正（Am J Gastroenterol 2024;119(10):2145，PMID 38457250），更正內容無法取得——引用數字前查勘誤（FAIL-7）**。Route: EPMC＋摘要（60 月失代償 1.8%/1.1%；肝硬化 HR 5.08；HBeAg+ HR 5.23）。https://doi.org/10.14309/ajg.0000000000002203
- [S10] **PASS** Dongelmans EJ, Hirode G, Hansen BE, et al.; RETRACT-B study group (2025). Predictors of hepatic flares after nucleos(t)ide analogue cessation (RETRACT-B study). J Hepatol, 82(3), 446–455. DOI: 10.1016/j.jhep.2024.08.015. PMID 39773379。Route: EPMC＋摘要（1 年 flare ≥5x 18.6%、≥10x 10.2%、≥20x 3.4%；13 失代償 3 死；危險因子；12 週 DNA>5log 建議回治）。https://doi.org/10.1016/j.jhep.2024.08.015
- [S11] **PASS** Hirode G, Choi HSJ, Chen CH, et al.; RETRACT-B Study Group (2022). Off-Therapy Response After Nucleos(t)ide Analogue Withdrawal in Patients With Chronic Hepatitis B (RETRACT-B Study). Gastroenterology, 162(3), 757–771.e4. DOI: 10.1053/j.gastro.2021.11.002. PMID 34762906。Route: EPMC＋摘要（HBsAg 清除 12 月 3.2%、48 月 13.0%；亞洲人須 <100 IU/mL；失代償 0.48/1000 人年、19 人中 7 死）。https://doi.org/10.1053/j.gastro.2021.11.002
- [S12] **PASS** Terrault NA, Lok ASF, McMahon BJ, et al. (2018). Update on prevention, diagnosis, and treatment of chronic hepatitis B: AASLD 2018 hepatitis B guidance. Hepatology, 67(4), 1560–1599. DOI: 10.1002/hep.29800. PMID 29405329；PMC5975958。Route: EPMC＋NCBI-XML 全文（逐字：肝硬化不建議停藥／失代償無限期／移植後 indefinitely／A 肝疫苗／戒酒與代謝句）。https://doi.org/10.1002/hep.29800
- [S13] **PASS** de Franchis R, Bosch J, Garcia-Tsao G, Reiberger T, Ripoll C; Baveno VII Faculty (2022). Baveno VII – Renewing consensus in portal hypertension. J Hepatol, 76(4), 959–974. DOI: 10.1016/j.jhep.2021.12.022. PMID 35120736；PMC11090185（另有勘誤 J Hepatol 2022;77:271）。Route: EPMC＋NCBI-XML 全文（7.22–7.25 再代償定義逐字）。https://doi.org/10.1016/j.jhep.2021.12.022
- [S14] **PASS** Wu CY, Chen YJ, Ho HJ, et al. (2012). Association between nucleoside analogues and risk of hepatitis B virus–related hepatocellular carcinoma recurrence following liver resection. JAMA, 308(18), 1906–1914. DOI: 10.1001/2012.jama.11975. PMID 23162861。Route: EPMC＋摘要（6 年復發 45.6% vs 54.6%；HR 0.67；台灣健保資料庫）。https://doi.org/10.1001/2012.jama.11975
- [S15] **PASS** Kanwal F, Kramer J, Asch SM, et al. (2017). Risk of Hepatocellular Cancer in HCV Patients Treated With Direct-Acting Antiviral Agents. Gastroenterology, 153(4), 996–1005.e1. DOI: 10.1053/j.gastro.2017.06.012. PMID 28642197。Route: EPMC＋摘要（SVR aHR 0.28；SVR 後肝硬化 1.82/100 人年）。https://doi.org/10.1053/j.gastro.2017.06.012
- [S16] **PASS** Papatheodoridis GV, Idilman R, Dalekos GN, et al. (2017). The risk of hepatocellular carcinoma decreases after the first 5 years of entecavir or tenofovir in Caucasians with chronic hepatitis B. Hepatology, 66(5), 1444–1453. DOI: 10.1002/hep.29320. PMID 28622419。Route: EPMC＋摘要（年發生率 1.22%→0.73%；肝硬化 3.22%→1.57%）。https://doi.org/10.1002/hep.29320
- [S17] **PASS** Wu YP, Yang XY, Tian YX, et al. (2025). Dose-dependent Relationship between Alcohol Consumption and the Risks of Hepatitis B Virus-associated Cirrhosis and Hepatocellular Carcinoma: A Meta-analysis and Systematic Review. J Clin Transl Hepatol, 13(3), 179–188. DOI: 10.14218/JCTH.2024.00379. PMID 40078198；PMC11894389（OA）。Route: EPMC＋摘要（OR 2.27；每日 12 g → HCC +11.5%）。https://doi.org/10.14218/JCTH.2024.00379
- [S18] **PASS** Huang DQ, El-Serag HB, Loomba R (2021). Global epidemiology of NAFLD-related HCC: trends, predictions, risk factors and prevention. Nat Rev Gastroenterol Hepatol, 18(4), 223–238. DOI: 10.1038/s41575-020-00381-6. PMID 33349658；PMC8016738。Route: EPMC＋摘要（NASH 肝硬化 HCC 年 0.5–2.6%；非硬化 0.1–1.3/1000 人年）。https://doi.org/10.1038/s41575-020-00381-6
- [S19] **PASS** 衛生福利部中央健康保險署。《全民健康保險藥品給付規定》第 10 節抗微生物劑（官方 PDF，內文修訂標記至 114/6/1；10.7.3 B 肝口服抗病毒藥全條文：HBeAg(-) 停藥條款與 36 個月上限、10.7.3.2(5) 肝硬化長期、(3) 肝移植預防性使用、(8) 肝癌根除性治療長期＋註 a 根除性治療清單【無 SBRT】＋「直至肝癌復發且未能再次接受根除性治療止」）。Route: 官方 PDF 直接下載全文檢索（nhi.gov.tw HTML 頁面被擋、PDF 直連可用）。https://www.nhi.gov.tw/ch/dl-50614-51b47002f99f4ba38f69bb432ca23477-1.pdf
- [S20] **PASS** 衛生福利部新聞稿（112-09-22）。〈112年10月1日起健保放寬口服B肝抗病毒藥物〉（ALT 異常 2 次→1 次；F3→F2；估新增 21,000 人）。Route: 官方網頁直讀。https://www.mohw.gov.tw/cp-16-76025-1.html
- [S21] **PASS** Mazzaferro V, Regalia E, Doci R, et al. (1996). Liver transplantation for the treatment of small hepatocellular carcinomas in patients with cirrhosis. N Engl J Med, 334(11), 693–699. DOI: 10.1056/NEJM199603143341104. PMID 8594428。Route: EPMC＋摘要（4 年 OS 75%、RFS 83%、復發 8%；病理超出者 50%）。https://doi.org/10.1056/NEJM199603143341104
- [S22] **PASS** Engels EA, Pfeiffer RM, Fraumeni JF, et al. (2011). Spectrum of cancer risk among US solid organ transplant recipients. JAMA, 306(17), 1891–1901. DOI: 10.1001/jama.2011.1592. PMID 22045767；PMC3310893。Route: EPMC＋摘要（SIR 2.10；NHL 7.54；肝受者肺癌 1.95、腎癌 1.80；黑色素瘤/唇癌升高）。https://doi.org/10.1001/jama.2011.1592
- [S23] **PASS** Dew MA, DiMartini AF, De Vito Dabbs A, et al. (2007). Rates and risk factors for nonadherence to the medical regimen after adult solid organ transplantation. Transplantation, 83(7), 858–873. DOI: 10.1097/01.tp.0000258599.65257.a6. PMID 17460556。Route: EPMC＋摘要（免疫抑制劑不遵囑 19–25/100 人年；腎 36、其他 7–15）。https://doi.org/10.1097/01.tp.0000258599.65257.a6
- [S24] **PASS** Abecassis MM, Fisher RA, Olthoff KM, et al.; A2ALL Study Group (2012). Complications of living donor hepatic lobectomy—a comprehensive report. Am J Transplant, 12(5), 1208–1217. DOI: 10.1111/j.1600-6143.2011.03972.x. PMID 22335782；PMC3732171。Route: EPMC＋摘要（740 人；40% 併發症；3 死；疝氣 7%、心理 3% 晚發；一年緩解 95/75/42%）。https://doi.org/10.1111/j.1600-6143.2011.03972.x
- [S25] **PASS** Cheah YL, Simpson MA, Pomposelli JJ, Pomfret EA (2013). Incidence of death and potentially life-threatening near-miss events in living donor hepatic lobectomy: a world-wide survey. Liver Transpl, 19(5), 499–506. DOI: 10.1002/lt.23575. PMID 23172840。Route: EPMC＋摘要（11,553 例；死亡率 0.2%；併發症 24%；near-miss 1.1%）。https://doi.org/10.1002/lt.23575
- [S26] **PASS** 衛生福利部中央健康保險署。《全民健康保險藥品給付規定》第 8 節免疫製劑（官方 PDF，內文修訂標記至 115/3/1；8.2.1 cyclosporin「器官移植抗排斥藥物」；8.2.2.2 tacrolimus「肝臟及腎臟移植之第一線用藥」；8.2.2.1 緩釋型為肝腎移植第二線）。Route: 官方 PDF 直接下載全文檢索。https://www.nhi.gov.tw/ch/dl-55682-0edce502618d4d309195db2577c9319b-1.pdf
- [S27] **PASS（2013 年資料，須標年代）** 衛生福利部新聞（102-03-22）。〈新肝寶貝、例例皆珍貴 台灣肝臟移植手術病人存活率享譽國際〉（2001–2011 全國 2,623 例；3 年 ~80%、5 年 ~76%、10 年 ~70%；未校正術前嚴重度——新聞稿自承）。Route: 官方網頁直讀。https://www.mohw.gov.tw/cp-3210-23597-1.html
- [S28] **PASS** Kulik L, Heimbach JK, Zaiem F, et al. (2018). Therapies for patients with hepatocellular carcinoma awaiting liver transplantation: A systematic review and meta-analysis. Hepatology, 67(1), 381–400. DOI: 10.1002/hep.29485. PMID 28859222。Route: EPMC＋摘要（無 RCT；T2 退出 RR 0.32/0.38 不顯著；T3 降期後 1/5 年存活 RR 1.11/1.17；證據品質極低）。https://doi.org/10.1002/hep.29485
- [S29] **PASS** Sapisochin G, Barry A, Doherty M, et al. (2017). Stereotactic body radiotherapy vs. TACE or RFA as a bridge to transplant in patients with hepatocellular carcinoma. An intention-to-treat analysis. J Hepatol, 67(1), 92–99. DOI: 10.1016/j.jhep.2017.02.022. PMID 28257902。Route: EPMC＋摘要（退出 16.7/20.2/16.8%；列名起與移植起存活皆無差異）。https://doi.org/10.1016/j.jhep.2017.02.022
- [S30] **PASS** Parikh ND, Waljee AK, Singal AG (2015). Downstaging hepatocellular carcinoma: A systematic review and pooled analysis. Liver Transpl, 21(9), 1142–1152. DOI: 10.1002/lt.24169. PMID 25981135。Route: EPMC＋摘要（降期成功 48%；前瞻 68% vs 回溯 44%；移植後復發 16%）。https://doi.org/10.1002/lt.24169
- [S31] **PASS** Mazzaferro V, Citterio D, Bhoori S, et al. (2020). Liver transplantation in hepatocellular carcinoma after tumour downstaging (XXL): a randomised, controlled, phase 2b/3 trial. Lancet Oncol, 21(7), 947–956. DOI: 10.1016/S1470-2045(20)30224-2. PMID 32615109。Route: EPMC＋摘要（74 進入、29 隨機前退出、45 隨機；5 年 EFS 76.8% vs 18.3%、OS 77.5% vs 31.2%；提前關閉）。https://doi.org/10.1016/S1470-2045(20)30224-2
- [S32] **PASS** Wen PH, Lu CL, Strong C, et al. (2018). Demographic and Urbanization Disparities of Liver Transplantation in Taiwan. Int J Environ Res Public Health, 15(2), 177. DOI: 10.3390/ijerph15020177. PMID 29360736；PMC5857045（OA）。Route: EPMC＋NCBI-XML 全文（逐字：「Taiwan where more than 80% of LT are LDLT」——內文引述其參考文獻之二手陳述，引用時標明）。https://doi.org/10.3390/ijerph15020177
- [S33] **PASS（指路用；肝臟別數字不可引）** 器官捐贈移植登錄及病人自主推廣中心（TOSRPAPC，原 TORSC，torsc.org.tw 已轉址）。「器官等候資訊」頁（動態數字，文字層抓不到）與「115年每月器官等候人數及捐贈案例統計」公告（每月中旬公告；115 年 7 月 PDF 可抓，**等候總人數 11,786 人（115-07-31）**可引；各器官別數字為圖形排版、無法安全歸屬→肝臟人數不可引）。Route: 官方網頁與 PDF 直接抓取。等候資訊頁：https://www.tosrpapc.org.tw/xmdoc/cont?xsmsid=0P183413005349792009 ；每月統計公告：https://www.tosrpapc.org.tw/xmdoc/cont?xsmsid=0P008623086253508127&sid=0Q098379612297480494

### FAIL / NOT-CITABLE（查過、不能用）

- [FAIL-1] **EASL 2025 指引原文措辭**（追蹤排程、AFP 建議）：付費牆、EPMC 無全文（見 [S5] 書目限定）。
- [FAIL-2] **「治療後族群」的 AFP 表現統合分析**：EPMC 檢索無等級相當的來源——Tzartzeva 是監測情境，外推須標明。
- [FAIL-3] **nhi.gov.tw HTML 頁面**：全部被 Cloudflare 質詢頁擋（403 "Just a moment"，多種 UA/headers 皆同）；**PDF 直連（/ch/dl-…pdf）正常**——本 brief 的健保條文全數走 PDF。data.nhi.gov.tw 連線失敗；data.gov.tw 搜尋 API 無法帶關鍵字（回傳與查詢無關的清單）。
- [FAIL-4] **台灣活體／屍肝移植比例的官方統計**：MOHW 統計處與登錄中心公開頁未取得分別數字；僅 [S32] 的二手 >80% 可用（標註引述）。
- [FAIL-5] **肝臟等候人數**：登錄中心動態頁數字 JS 載入抓不到；月報 PDF 器官別數字無法安全歸屬（詳 [S33]）→ 正文照修正 8 寫「以登錄中心當日公告為準」。
- [FAIL-6] **hpa.gov.tw**（成人 A 肝疫苗公費對象、戒酒資源）：TLS/SSL 失敗（SPEC 已預告）；未找到 mohw 鏡像頁 → gap。
- [FAIL-7] **Hirode 2023 的更正啟事內容**（Am J Gastroenterol 2024;119(10):2145，PMID 38457250）：無摘要、無 OA 全文——不知更正了哪個數字。引用 [S9] 數字前需再查。
- [FAIL-8] **Cheng AY, et al. (2026). Incidence of skin cancer versus overall de novo malignancies among living donor liver transplantation recipients in Taiwan. Br J Dermatol 194(4):788–789**（PMID 41285686）：通訊文章、無摘要、無 OA 全文——台灣本土移植後皮膚癌數字**存在但取不到**，不可引任何數字。
- [FAIL-9] **Hsu YC, et al. (2022). Severe Acute Exacerbation After Cessation of Nucleos(t)ide Analog for Chronic Hepatitis B. Clin Gastroenterol Hepatol 20(6):1413–1415.e3**（PMID 34464721）：台灣真實世界停藥後嚴重急性惡化研究——研究通訊、數字在內文、無 OA 全文——不可引數字（停藥風險數字用 RETRACT-B [S9][S10][S11]，其世代本含台灣多中心：林口長庚、高雄長庚、台大、義大等）。
- [FAIL-10] **mycophenolate／everolimus／sirolimus 用於肝移植的健保給付專條**：第 8 節全文檢索無專條 → gap，寫成「與移植團隊及個管師確認」。
- [FAIL-11] **odtm.mohw.gov.tw（器官捐贈移植整合系統）**：代理連線失敗（與 B 組 FAIL-6 相同）。
