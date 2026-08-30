# B 組研究簡報 — 子宮頸癌專題（階段二：治療怎麼決定）

研究日期：2026-08-30。所有期刊來源皆以 Europe PMC REST API（`EXT_ID`／`TITLE`／`AUTH` 查詢，`resultType=core` 取摘要）逐條查證，書目欄位照 API 回傳值抄寫；ESGO/ESTRO/ESP 2023 指引另以 Europe PMC fullTextXML（PMC10247855）下載後 grep 原文。台灣端以 nhi.gov.tw／mohw.gov.tw 原始檔案（PDF／XLS／HTML）下載後 grep 原文（2026-08-30 覆核）。查不到＝FAIL，照列不藏。每個數字帶期別與族群標籤。

**跨組界線提醒（SPEC §五）**
- 「開刀還是放療」的決策與雙重毒性 → **B1 主場**；LACC 與微創 → **B2 主場**（紅線 4 標籤不外溢）；CCRT 療效證據與 OUTBACK／INTERLACE／KEYNOTE-A18 → **B3 主場**。
- **cisplatin 毒性與當天實務 → C 組**（C 組簡報已涵蓋；本簡報只寫療效，毒性僅保留試驗回報的整體 G3+ 率供對照，不展開個別器官毒性）。
- 近接治療的證據與流程 → **C1**；B1 只寫「局部晚期的根治性放療含近接」一句並指路。
- 總治療時間數字 → **C2**；B 組不重複。
- 卵巢移位的劑量資料（8 Gy）→ 站上 `insight-cervix-ovary`；冷凍生育機制、成功率、台灣 114/9 補助 → 站上 `care-fertility`。**B4 只寫子宮頸專屬**：子宮頸切除術條件、時間窗、放療後的子宮。兩篇站上文章的內容清單見本檔「站上既有文章的內容清單」節。
- **共用註（D4 可重用）**：bevacizumab 復發轉移子宮頸癌健保條文（9.37.4）與 pembrolizumab 子宮頸適應症「查無條文」的查證結果，見 B3 的 Taiwan status 與 [S39][S41]，D4 寫復發時直接引用，不必重查。

---

# B1 — 開刀還是放療：不開刀不是放棄　【紅線 2 雙向】

**Key facts**

*早期（IB–IIA）兩者存活等效（Landoni 隨機試驗）*
- Landoni 1997（義大利單中心隨機試驗，1986–1991 收案，343 名 FIGO IB–IIA 隨機分派：手術 172／根治性放療 171）：中位追蹤 87 個月，**5 年整體存活兩組皆 83%、無病存活兩組皆 74%**；復發 25%（手術組）vs 26%（放療組）。**嚴重併發症：手術組 28% vs 放療組 12%（p=0.0004）**，作者原文：「There is no treatment of choice for early-stage cervical carcinoma in terms of overall or disease-free survival. **The combination of surgery and radiotherapy has the worst morbidity**, especially urological complications」 [S1]
- 手術組術後接受輔助放療的比例（同試驗、依原訂病理條件 pT2b+／安全緣 <3 mm／切緣陽性／淋巴結陽性）：**腫瘤 ≤4 cm 者 62/114（54%）、>4 cm 者 46/55（84%）** [S1] ——「先開刀」在這個隨機試驗裡，超過一半的人最後兩種治療都做了
- **20 年更新版存在（已驗證）**：Landoni 2017（J Gynecol Oncol），最短追蹤 19 年；**20 年整體存活 手術組 72% vs 放療組 77%（p=0.280，無差異）**；全組復發 94 例（28%）；多變項的存活因子是組織型態（p=0.020）、腫瘤直徑（p=0.008）、淋巴結（p<0.001），不是治療方式；結論重申「no treatment of choice」 [S2]

*「避免兩種都做」是指引寫進去的原則（ESGO/ESTRO/ESP 2023 原文）*
- 早期（T1b1、T1b2、T2a1）總則原文：「Treatment strategy should aim to **avoid combining radical surgery and radiotherapy because of the high morbidity induced by the combined treatment** [IV, A]」 [S3]
- 同指引：「**If a combination of risk factors is known at diagnosis, which would require an adjuvant treatment, definitive CTRT and brachytherapy (BT) should be considered without previous radical pelvic surgery** [IV, A]」——術前就看得出來會需要術後放療的人，指引叫你直接做根治性化放療，不要先開 [S3]
- 早期也可以選根治性化放療：「Definitive CTRT and image-guided brachytherapy (IGBT) represent an alternative treatment option [IV, B]」；NACT 或化放療後再開刀「are not recommended [IV, D]」 [S3]
- 術中發現淋巴結陽性：「If any LN involvement is detected intraoperatively, further PLND and radical hysterectomy **should be avoided**. Patients should be referred for definitive CTRT [III, A]」 [S3]

*為什麼「先開刀」常收在雙重治療（Sedlis／Peters 這兩組條件就是機制）*
- **中風險（Sedlis，GOG 92）**：277 名 IB、淋巴結陰性、根治性子宮切除後，具備至少兩項危險因子（>1/3 基質侵犯、脈管侵犯 LVSI、腫瘤大）者隨機分派輔助骨盆放療 vs 觀察：復發 15% vs 28%，**復發風險下降 47%（RR 0.53，p=0.008）**；2 年無復發 88% vs 79%；代價是 G3/4 不良事件 6% vs 2.1% [S4]。2006 年長期追蹤：復發或死亡 HR 0.58（90% CI 0.40–0.85，p=0.009）；**整體存活 HR 0.70（90% CI 0.45–1.05，p=0.074）未達統計顯著** [S5]
- **高風險（Peters，GOG 109/SWOG 8797/Intergroup 0107）**：243 名 IA2/IB/IIA 根治性子宮切除後淋巴結陽性、切緣陽性或子宮旁組織侵犯者，輔助放療 vs 輔助化放療（cisplatin＋5-FU）：**4 年無惡化存活 80% vs 63%、整體存活 81% vs 71%**（單做放療的惡化與死亡 HR 各為 2.01 與 1.96）——病理高風險的人術後不只補放療，還要補化放療 [S6]
- ESGO 2023 把這兩層寫成現行規則：中風險（腫瘤大小＋LVSI＋基質侵犯深度的組合）「adjuvant radiotherapy should be considered [IV, A]」（由做過完整型別根治性子宮切除的團隊觀察是替代選項 [IV, B]）；高風險（淋巴結轉移 pN1／切緣陽性／子宮旁侵犯）「Adjuvant CTRT is indicated [IV, A]」 [S3]
- 實際發生率（現代世代，帶標籤）：SUCCOR 世代（歐洲多中心回溯，FIGO 2009 IB1、**最終病理淋巴結陰性** 572 人）：**40.6% 術後接受了輔助放療**；而且執行很亂——接受放療者有 56.9% 其實不符 Sedlis 條件、符合條件者有 13.2% 沒被治療 [S7]。FIGO 2018 IB2（2–4 cm）接受根治性子宮切除的 675 人（SUCCOR＋LATAM＋MD Anderson 三個資料庫）：**51% 術後接受輔助治療**（其中 54% 是化放療、44% 是放療）；最終病理 ≥3 cm 者 **61%** 接受輔助治療 [S8]

*局部晚期（T1b3–T4a）的標準是根治性化放療（含近接），而且是根治意圖*
- ESGO 2023 原文：「Management of Locally Advanced Cervical Cancer (T1b3-T4a)：**Definitive radiotherapy should include concomitant chemotherapy whenever possible [I, A]. IGBT is an essential component of definitive radiotherapy** and should not be replaced with an external boost…」（近接的完整證據與流程 → C1） [S3]
- T1b3/T2a2 淋巴結陰性這一格是唯二「手術 vs 化放療都可談」的灰色地帶：指引原文「There is limited evidence to guide the choice…應由多專科團隊討論、告知兩種選項的利弊 [IV, A]」，且因個案數 <10% 建議轉診高度專業中心；「For surgery, avoidance of the combination of radical surgery and post-operative external radiotherapy requires acceptance for modifications of the traditional selection criteria for adjuvant treatment [IV, B]」 [S3]

*「不開刀不是放棄」要有數字（根治性化放療做得到什麼）*
- retroEMBRACE（12 中心、731 名接受影像導引近接的局部晚期病人，IIB 佔 50.4%，77.4% 有同步化療）：**3／5 年整體存活 74%／65%、癌症特異存活 79%／73%**；5 年局部控制依期別：**IB 98%、IIB 91%、IIIB 75%** [S9]
- EMBRACE-I（24 中心前瞻世代、1,341 名 IB–IVA）：CCRT＋MRI 導引近接，**5 年精算局部控制 92%**（95% CI 90–93）；各器官 G3–5 晚期毒性 3.2–8.5% [S10]
- 當代隨機試驗的「標準治療臂」也是同一級數：INTERLACE 的化放療單獨臂 **5 年整體存活 72%**（FIGO 2008 IB1 淋巴結陽性至 IVA，70% 為 IIB）[S26]；KEYNOTE-A18 安慰劑＋化放療臂 **36 個月整體存活 74.8%**（高風險族群含 III–IVA）[S30]。（兩試驗的比較結果歸 B3；B1 只用其對照臂數字說明「根治性化放療不是安慰性治療」）

*化放療之後再補子宮切除：沒有好處（驗證過的證據）*
- GOG 71（Keys 2003，256 名 bulky IB ≥4 cm 隨機：放療 vs 減量放療＋筋膜外子宮切除）：**「Overall, there was no clinically important benefit with the use of extrafascial hysterectomy」**；局部復發累積發生率 27% vs 14%（5 年）但存活無統計差異（惡化 URR 0.77，p=0.07；死亡 p=0.26）；G3/4 不良事件兩組皆 10% [S11]
- Cochrane 2022（11 個 RCT、2,683 人）：放療後加子宮切除 vs 放療單獨（GOG 71 的資料）死亡或惡化 HR 0.89（95% CI 0.61–1.29，無差異）；**NACT＋子宮切除 vs 化放療單獨（2 個 RCT、1,253 人統合）：整體存活 HR 0.94（0.76–1.16，無差異），且兩試驗中 NACT＋手術組的 5 年無病存活反而較差（57% vs 65.6%，以 IIB 為主）** [S12]
- ESGO 2023：化放療後追加手術不建議（「NACT or CTRT followed by surgery are not recommended [IV, D]」；殘留腫瘤是另一回事，3–6 個月後仍有殘留者轉專業中心評估救援手術 [IV, B]） [S3]

**Claim ceiling**

Defensible：
- 「早期子宮頸癌開刀和放療，隨機試驗追了 5 年和 20 年，存活都沒有差別（5 年皆 83%；20 年 72% 對 77%，統計上無差異）。」[S1][S2]
- 「真正有差的是副作用的組合方式：先開刀的那組有超過一半（≤4 cm 者 54%、>4 cm 者 84%）最後又做了放療，而嚴重併發症在手術組是 28%、放療組是 12%——歐洲指引因此把『避免兩種都做』寫成治療策略的原則。」[S1][S3]
- 「會不會需要術後放療，開刀前常常就估得出來：腫瘤 2–4 公分的病人開完刀有五成一最後接受輔助治療；病理上有淋巴結轉移、切緣陽性或子宮旁侵犯，標準是術後化放療。指引說：如果診斷時就看得出會走到這一步，應該直接做根治性化放療，不要先開。」[S3][S6][S8]
- 「局部晚期（IB3 以上）的標準治療是同步化放療加近接治療，意圖是根治：現代影像導引近接的世代 5 年整體存活 65%、IIB 期 5 年局部控制 91%；當代試驗的化放療標準臂 5 年整體存活 72%。這不是安慰性治療。」[S3][S9][S26]
- 「化放療做完再『順便把子宮拿掉』並不會多活：隨機試驗與 Cochrane 統合都是陰性，指引明確不建議。」[S11][S12][S3]
- 「哪一種比較好？隨機試驗的答案是：看你的腫瘤條件（大小、組織型態、淋巴結），不是看哪一科。」[S2][S3]

Would overstate：
- ✗ 任何讀起來像「放療比手術好」或「手術比放療好」的句子——**紅線 2，雙向失敗**。也不准出現對任一科別的貶抑（禁醫療法 §84/§86 用語）
- ✗「所有期別都等效。」——Landoni 只randomize了 IB–IIA；IB3/II–IVA 的標準是化放療，不是「都可以」[S1][S3]
- ✗「先開刀＝一定要做兩種治療。」——是「機率高且可預估」（54–84%、40.6%、51%、61%，各帶族群標籤），不是必然 [S1][S7][S8]
- ✗「Landoni 證明現在的放療和現在的手術等效。」——那是 1986–1991 的放療技術與手術；兩邊今天都更好，等效的結論是方向性的，引用時帶年代 [S1][S2]
- ✗ 把 Sedlis 準則的細項組合表（invasion 深度 × 腫瘤大小 × LVSI 的具體切點）寫出來——本次只驗證到「至少兩項：>1/3 基質侵犯、LVSI、腫瘤大」的摘要層級，細項表未驗證，不可憑記憶列表 [S4]
- ✗「輔助放療讓中風險病人活得比較久。」——GOG 92 顯著的是復發與無惡化存活；**整體存活 HR 0.70 未達顯著（p=0.074）**，要照寫 [S5]
- ✗「化放療後子宮切除完全沒有角色。」——GOG 71 的次族群（4–6 cm）作者自己說可能受益（URR 0.58/0.60），且殘留腫瘤的救援手術是另一條路；寫「常規追加沒有好處」即可 [S11][S3]

**Caveats / safety notes**

- Landoni 的「等效」部分是靠手術組大量輔助放療撐出來的（手術組 64%〔108/169〕實際上接受了合併治療）——這正是「雙重治療」論點的一部分，寫的時候可以用，但不要反過來寫成「手術本身不行」。
- 期別標籤要小心：Landoni／SUCCOR 用 FIGO 2009（IB1=4 cm 以下），Pan 2024 用 FIGO 2018（IB2=2–4 cm），ESGO 用 TNM（T1b3≈IB3）。**每個數字寫出處的分期版本，不可互相換算後混用。**
- SUCCOR 與三資料庫的輔助治療率是手術資料庫的回溯資料，有選擇偏差；當作「量級」引用，不當作精確預測值。
- 「跟你的放腫醫師與婦癌醫師都談過再決定」是這一篇的行為結論；ESGO 原文本身就要求多專科討論與雙向告知 [S3]，寫的時候不點名機構、不寫「本院」。
- B 組收尾方向是「帶哪幾份資料去談」：病理／影像報告上決定這題的欄位（腫瘤大小、LVSI、基質侵犯深度、淋巴結、組織型態）在 [S3][S4][S6] 都有依據。

**Taiwan status**

- 健保「醫療服務給付項目」檔（114.01.01 生效版 XLS，官方下載，2026-08-30 覆核）明列：**80413B 子宮頸癌根除性子宮切除（Radical hysterectomy for cervical cancer）42,640 點**；80412B 擴大性子宮切除 28,841 點。放療端的近接治療給付項目（37007B/37008B/37018B/37019B 等）→ C 組簡報已載，B1 指路即可 [S42]。給付的臨床條件與住院自付額不在此檔 → 寫「向醫務課或個管師確認」。
- IMRT/VMAT 無專項（按照野計費）與 cisplatin 給付條文 gap → C 組簡報已查證，B1 不重寫。

## 圖表數據（fig-cx-treatment-map）

| 期別（依來源之分期系統標註） | 主要治療（來源原文層級） | 附註／存活錨點 | 來源 |
|---|---|---|---|
| T1a1（FIGO IA1） | 圓錐切除即可為根治性治療；根治性子宮切除／子宮頸切除屬過度治療 [IV, D] | LVSI 陽性可考慮 SLN | [S3] |
| T1a2（IA2） | 圓錐切除（切緣乾淨）或單純子宮切除即足夠 | | [S3] |
| T1b1/T1b2/T2a1（IB1–IB2/IIA1） | 根治性手術（開腹為標準）**或**根治性化放療＋近接（替代選項 [IV, B]）；原則＝避免兩種都做 [IV, A] | Landoni：5 年 OS 兩臂皆 83%；20 年 72/77% 無差異 | [S1][S2][S3] |
| 術後病理中風險（Sedlis 因子） | 考慮輔助放療 [IV, A] | 復發 RR 0.53；OS 未顯著 | [S4][S5][S3] |
| 術後病理高風險（淋巴結＋/切緣＋/子宮旁＋） | 輔助化放療 [IV, A] | 4 年 OS 81 vs 71%（化放療 vs 放療） | [S6][S3] |
| T1b3/T2a2 淋巴結陰性（IB3/IIA2） | 灰色地帶：手術 vs 化放療皆可談，建議轉專業中心；證據有限 [IV, B] | 選手術須接受調整輔助治療門檻 | [S3] |
| T1b3–T4a（IB3–IVA，含淋巴結陽性早期） | **根治性同步化放療 [I, A]＋影像導引近接（必要組成）** | retroEMBRACE 5 年 OS 65%、IIB 5 年 LC 91%；INTERLACE 化放療臂 5 年 OS 72% | [S3][S9][S26] |
| 化放療之後 | 不追加常規子宮切除 [IV, D]；殘留者轉專業中心評估 | GOG 71／Cochrane 皆無存活好處 | [S3][S11][S12] |

圖注建議：「示意圖，依 ESGO/ESTRO/ESP 2023 指引重繪；存活數字出處見各篇內文。」（近接的劑量邏輯圖歸 C1 的 fig-cx-brachy-dose，不重畫。）

---

# B2 — 微創手術在這個癌別踩了煞車　【紅線 4：族群與術式標籤每次都帶，不外溢】

**Key facts**

*LACC 隨機試驗（族群標籤：早期〔FIGO 2009 IA1 有 LVSI／IA2／IB1〕、術式標籤：根治性子宮切除）*
- Ramirez 2018（NEJM，631 名隨機：微創 319／開腹 312；微創組 84.4% 腹腔鏡、15.6% 達文西；91.9% 為 IB1；兩組的組織型態、LVSI、淋巴結、腫瘤大小、輔助治療使用率相似）：**4.5 年無病存活 86.0% vs 96.5%（差 −10.6 個百分點，95% CI −16.4 至 −4.7，未達非劣性）；3 年無病存活 91.2% vs 97.1%，復發或死亡 HR 3.74（1.63–8.58）；3 年整體存活 93.8% vs 99.0%，死亡 HR 6.00（1.77–20.30）** [S13]
- **最終分析（已驗證存在）**：Ramirez 2024（J Clin Oncol，追蹤 4.5 年完整）：4.5 年 DFS 85.0% vs 96.0%（差 −11.1，95% CI −15.8 至 −6.3）、**DFS HR 3.91（2.02–7.58）；4.5 年整體存活 90.6% vs 96.2%，死亡 HR 2.71（1.32–5.59，p=0.007）**；作者結論原文：「an open approach should be standard of care」 [S15]
- 量級的白話翻譯素材：復發或死亡的風險約 3–4 倍，但**絕對值**是 4.5 年少了約 11 個百分點的無病存活——兩個層次都要寫，只寫倍數會嚇人、只寫絕對值會失真。

*流行病學驗證（Melamed，同方向）*
- Melamed 2018（NEJM；美國 Commission on Cancer 醫院 2010–2013 的 2,461 名 IA2/IB1 根治性子宮切除，傾向分數加權）：**4 年死亡率 微創 9.1% vs 開腹 5.3%（HR 1.65，1.22–2.22）**；另以 SEER 做中斷時間序列：微創普及前（2000–2006）4 年相對存活穩定，**2006 年微創開始普及後每年下降 0.8%（95% CI 0.3–1.4，p=0.01）** [S14]

*指引回應（哪些指引把開腹寫回標準）*
- ESGO/ESTRO/ESP 2023 原文：「**Laparotomy is the standard approach for all procedures which include radical parametrectomy [I, A]**. Minimally invasive approach may be considered **only in low risk tumors (<2 cm and free margins after conization)**, in high-volume centers…if the patient agrees after comprehensive discussion about current evidence [IV, C]」 [S3]
- 同指引：**微創做淋巴結分期是可接受的**（「Minimally invasive surgery is an acceptable approach for LN staging [IV, B]」）——「踩煞車的是根治性子宮切除這個術式，不是腹腔鏡這個工具」的指引級佐證 [S3]
- LACC 最終分析作者結論「open approach should be standard of care」 [S15]。（NCCN 依本專題規則不引用；ESMO 現行版見 FAIL [S43]）

*機制（假說層級，標籤要帶）*
- SUCCOR（歐洲 126 中心回溯世代，1,272→加權 693 名 FIGO 2009 IB1 根治性子宮切除，2013–2014）：微創組復發 HR 2.07（1.35–3.15）、死亡 HR 2.45（1.30–4.60）；**用了舉宮器（uterine manipulator）的微創復發 HR 2.76（1.75–4.33）；沒用舉宮器的微創與開腹無顯著差異（HR 1.58，0.79–3.15，P=0.20）；有做保護性陰道縫合（把腫瘤封起來再切開陰道）的微創與開腹相近（HR 0.63，0.15–2.59）** [S16]
- 但反向證據也存在：2023 年 BJOG 統合分析（6 個觀察性研究、2,150 人）：**即使不用舉宮器，微創根治性子宮切除的無復發存活仍比開腹差（HR 1.55，1.15–2.10）**——「只要避開舉宮器就安全」目前不成立 [S17]
- CO2 氣腹促進腫瘤擴散的假說：**本次查無可引用的臨床證據**（見 FAIL [S44]）。機制段落只能寫「舉宮器與陰道切開時的腫瘤暴露是觀察資料指向的可能環節、CO2 是假說」，全部帶「假說／觀察性」標籤。

*已經開過微創的讀者（出口段的素材）*
- SUCCOR 10 年更新（556 名 FIGO 2009 IB1、2013–2014 手術、完成 10 年追蹤）：**全組 5 年整體存活 97%、10 年 89%；10 年累積復發 9%；復發中 78% 發生在術後前 5 年**；這個世代 10 年 DFS 微創 92% vs 開腹 88%（p=0.12，無差異）——觀察性資料、有選擇偏差，不可寫成「其實沒差」，但「復發風險集中在前幾年、之後逐年下降」的形狀可用 [S18]
- 一般性（非微創專屬）的條件存活資料：SEER 65 歲以下 18,511 名子宮頸癌（2004–2019）：**已無病存活超過 5–6 年者，之後 10–15 年死於子宮頸癌的風險低於 5%** [S19]
- **微創專屬的「以某時點無病為條件」的存活分析：查無**（FAIL [S45]）。誠實寫法：已手術且目前無復發的人，資料能說的是「時間站在你這邊」（[S18][S19] 的一般形狀），該做的是把追蹤排程做好，不是重開一次刀；LACC/SUCCOR 都沒有任何資料支持「開過微創要補做什麼治療」。

**Claim ceiling**

Defensible：
- 「在早期子宮頸癌的**根治性子宮切除**這一個術式上，隨機試驗發現微創的復發風險是開腹的三到四倍，4.5 年無病存活少了約 11 個百分點；美國的全國資料也在微創普及後看到同方向的存活下滑。」[S13][S14][S15]
- 「歐洲指引因此把開腹寫回標準路徑（証據等級 I, A）；微創只保留給極低風險（錐切後小於 2 公分且切緣乾淨）、在符合品質條件的大量中心、且病人充分知情同意的情況。」[S3]
- 「這個煞車踩在『根治性子宮切除』上，不是腹腔鏡這個工具上：同一份指引照樣接受用微創做淋巴結分期；其他癌別、其他婦科手術不在這個結論裡。」[S3]
- 「為什麼微創會比較差？目前只有線索：歐洲的回溯資料指向舉宮器與切開陰道時腫瘤暴露這兩個環節，但後續統合分析發現不用舉宮器的微創仍然比較差——老實說，機制還沒有定論。」[S16][S17]
- 「已經開過微創的人：復發大多集中在術後前幾年（一個歐洲十年世代裡 78% 在前 5 年），無病時間越長、風險越低；該做的是照排程回診，讓醫師知道你當年的術式，而不是恐慌。」[S18][S19]

Would overstate：
- ✗「微創手術不安全」「腹腔鏡有問題」——**紅線 4 外溢，直接失敗**。每一次都要帶「早期子宮頸癌的根治性子宮切除」全標籤
- ✗「開過微創的人完蛋了／要趕快做什麼補救。」——**紅線 4**；沒有任何證據支持補救性介入，出口是追蹤 [S18]
- ✗「不用舉宮器的微創就跟開腹一樣安全。」——SUCCOR 的次族群無顯著差異，但 BJOG 統合是 HR 1.55 仍較差；兩個都要寫 [S16][S17]
- ✗「SUCCOR 十年資料證明微創其實沒差。」——觀察性、選擇偏差、與隨機試驗方向相反時以隨機試驗為準；只可用它的「復發時間分布」形狀 [S18]
- ✗「CO2 氣腹會把癌細胞吹散。」——查無可引用臨床證據，只能寫「有人提出的假說」[S44]
- ✗ 把 Melamed 的 HR 1.65 寫成因果——觀察性研究，寫「相關」與「時間序列同步下滑」[S14]
- ✗「達文西（機器人）比較安全／比較危險。」——LACC 微創組僅 15.6% 是機器人，無法分開下結論；查無足以引用的機器人專屬隨機證據，不寫

**Caveats / safety notes**

- LACC 收案是 FIGO 2009 分期（IB1＝4 cm 以下）；對照 FIGO 2018 讀者需知 IB1/IB2 定義已改，寫文時帶清楚。
- 「3 年 OS 99% vs 93.8%」這種高存活數字同時是「早期預後很好」的證據——寫 B2 時順手固定讀者的絕對風險感（兩組都在九成以上），避免嚇到早期病人。
- 台灣自己的族群資料本次未查證（未搜尋台灣健保資料庫的 MIS 世代研究）→ 不寫「台灣的情況是…」。
- 已開過微創者的追蹤**排程本身**歸 D3（追蹤怎麼排），B2 只給「回診討論、告知術式」的行為出口，不開追蹤處方。
- 這篇必須寫「如果你正要開刀」的行動句：問醫師「我的手術會用哪種途徑、為什麼」是正當問題（ESGO 要求 comprehensive discussion [S3]）；不准寫成質疑特定醫院或醫師。

**Taiwan status**

- 健保「醫療服務給付項目」檔（114.01.01 生效版 XLS，2026-08-30 覆核）中，**80429B 腹腔鏡子宮頸癌根除性子宮切除（Laparoscopic radical hysterectomy for cervical cancer）48,183 點的支付項目仍然存在**（80413B 開腹版 42,640 點）[S42]——支付項目存在≠臨床建議，這正好是「制度跟不上證據」的中性寫法素材；不點名機構。
- 機器人手術的自費差額：本次未查得公開條文 → 寫「向醫務課確認」。

---

# B3 — 為什麼放療期間每週還要打化療　【OUTBACK 陰性是主旨不是註腳】

**Key facts**

*1999 年的證據地震（同步化療 vs 沒有同步化療；療效數字本篇主場）*
- GOG 120（Rose 1999，526 名 IIB–IVA、主動脈旁淋巴結陰性，放療＋三種化療方案隨機）：含 cisplatin 的兩組對 hydroxyurea 組，**惡化或死亡 RR 0.57（0.42–0.78）與 0.55（0.40–0.75）；死亡 RR 0.61（0.44–0.85）與 0.58（0.41–0.81）**；每週 cisplatin 40 mg/m²×6 是其中最簡單的方案 [S20]
- GOG 123（Keys 1999，369 名 bulky IB ≥4 cm，放療±每週 cisplatin，之後皆行輔助子宮切除）：**惡化 RR 0.51（0.34–0.75）、死亡 RR 0.54（0.34–0.86）**，4 年無惡化與整體存活皆顯著較好 [S21]
- RTOG 90-01（Morris 1999，403 名 IB–IIA ≥5 cm 或淋巴結陽性、IIB–IVA）：骨盆放療＋cisplatin/5-FU vs 骨盆＋主動脈旁放療：**5 年整體存活 73% vs 58%（p=0.004）、無病存活 67% vs 40%（p<0.001）**；遠端轉移與局部復發皆較少 [S22]
- GOG 85（Whitney 1999，368 名 IIB–IVA）：放療＋cisplatin/5-FU vs 放療＋hydroxyurea：無惡化存活 p=0.033、整體存活 p=0.018，且嚴重白血球毒性反而較低（4% vs 24%） [S23]
- 這一波證據促成 1999 年美國 NCI 臨床警訊（CCCMAC 摘要背景原句可引） [S24]

*把不確定性收攏的統合分析（絕對獲益的錨點）*
- CCCMAC 2008（18 個隨機試驗的個別病人資料統合）：13 個「化放療 vs 同樣的放療」試驗：**5 年存活絕對提升 6%（HR 0.81，p<0.001）**；非鉑類化放療也有效（HR 0.77）；化放療同時減少局部與遠端復發、改善無病存活；**獲益大小隨期別有異的訊號存在**（分母：18 trials 的 IPD；毒性句歸 C 組） [S24]
- 每週 cisplatin 40 mg/m² 是現行標準：ESGO 2023 原文「Concomitant chemotherapy should be based on single-agent radiosensitizing chemotherapy, **preferably cisplatin (weekly 40 mg/m²)**. If cisplatin is not applicable, alternative treatment options are **weekly carboplatin (AUC=2)** or hyperthermia」；也允許病況不適合者單獨放療 [S3]（carboplatin 對上健保 9.2 條文，見 Taiwan status；當天實務歸 C3）

*OUTBACK：化放療之後再補四個療程化療——陰性（主旨）*
- OUTBACK（Mileshkin 2023，Lancet Oncol；919 名可分析，FIGO 2008 IB1 淋巴結陽性／IB2／II／IIIB／IVA；標準化放療 vs 化放療後加 carboplatin AUC5＋paclitaxel 155 mg/m² 四個療程）：**5 年整體存活 72% vs 71%（差 1%，95% CI −6 至 7；HR 0.90，0.70–1.17，p=0.81）**；代價：G3–4 嗜中性球低下 20% vs 8%、貧血 18% vs 8%、嚴重不良事件 30% vs 22%；作者結論原文：「increased short-term toxicity and **did not improve overall survival; therefore, it should not be given in this setting**」 [S25]
- 這順便回頭解釋 CCCMAC 當年「加輔助化療的兩個試驗獲益較大」的暗示 [S24]——被隨機試驗正面檢驗後**不成立**。「更多化療≠更好」是這篇的尷尬結論，要當主旨寫。

*INTERLACE：化放療之前的六週誘導化療——陽性，但帶著實作但書*
- INTERLACE（McCormack 2024，Lancet；500 名，FIGO 2008 IB1 淋巴結陽性／IB2／IIA／IIB／IIIB／IVA；**70% 是 IIB、43% 淋巴結陽性**；2012–2022 收案）：每週 carboplatin AUC2＋paclitaxel 80 mg/m²×6 週→標準化放療 vs 直接化放療。**5 年無惡化存活 72% vs 64%（HR 0.65，0.46–0.91，p=0.013）；5 年整體存活 80% vs 72%（HR 0.60，0.40–0.91，p=0.015）**；G3+ 不良事件 59% vs 48%；誘導組 92% 完成至少 5 個週期，誘導與化放療的中位間隔僅 7 天；全組 92% 完成外照＋近接、中位總治療時間 45 天 [S26]
- 生活品質分析：誘導化療期間整體 QoL 略降、周邊神經症狀略多，但組間差異小於臨床意義門檻、12–18 個月內消失；任何等級不良事件 99% vs 95%、G3/4 59% vs 48% [S28]
- **實作但書（要照寫）**：(1) 收案跨 11 年、以 IIB 鱗癌為主的族群；(2) 試驗內的化放療品質很高（92% 完成近接、45 天完成）——誘導化療是「加在高品質化放療之上」的結果，不是替代品；(3) 誘導與化放療只隔 7 天，臨床上排程若拖長就不是這個試驗證明的東西；(4) 2025 年 Lancet 通訊由 EMBRACE 團隊具名質疑「不是新標準」（標題層級立場：〈INTERLACE: not a new standard for cervical cancer chemoradiation〉，作者群 Petric、Pötter 等；原文與作者回覆皆無摘要，引用停在「爭論存在」層級） [S27]
- 白話定位素材：INTERLACE 改變的是「化放療之前」；它沒有動搖「同步化放療＋近接」這個底座 [S26][S27]

*KEYNOTE-A18：化放療加免疫治療——族群限定高風險，2026 年的證據狀態*
- KEYNOTE-A18／ENGOT-cx11／GOG-3047（1,060 名，**高風險族群限定：FIGO 2014 IB2–IIB 且淋巴結陽性，或 III–IVA 不論淋巴結**；pembrolizumab 5 個週期同步＋15 個週期維持 vs 安慰劑，皆加標準化放療）：
  - 第一次期中分析（Lorusso 2024，Lancet 403 期）：**24 個月無惡化存活 68% vs 57%，HR 0.70（0.55–0.89，p=0.0020）**；G3+ 不良事件 75% vs 69% [S29]
  - 第二次期中分析（Lorusso 2024，Lancet 404 期）：**36 個月整體存活 82.6% vs 74.8%，死亡 HR 0.67（0.50–0.90，p=0.0040）**；G3+ 78% vs 70%；**免疫相關不良事件 39% vs 17%** [S30]
  - 病人自報結果（Randall 2025，Gynecol Oncol）：預先設定的 QoL 量表皆無組間有意義差異——加了 pembrolizumab 沒有讓生活品質變差 [S47]
  - 誠實的另一面（已發表的具名質疑，Cancer 2025）：對照組惡化的 193 人中只有 51 人後續接受過免疫治療——OS 差距可能部分反映對照組後線治療不足；90 週的治療長度與費用是可近性問題 [S31]
  - 美國 FDA 2024 年 1 月核准的適應症**限 FIGO 2014 III–IVA**（比試驗全體更窄；引自 2026 年成本效益論文的背景敘述） [S32]
  - **截至 2026-08-30，最終分析尚無同儕審查論文可引**（已有論文引用其 patient-level data，但主報告未見於 Europe PMC）[S32][S46]
- 台灣可近性：**健保藥品給付規定 9.69（免疫檢查點抑制劑）查無子宮頸癌適應症**（見 Taiwan status）——文章必須寫「在台灣此適應症目前需自費，是否適用與費用向團隊確認」，不可寫成人人可得的新標準

**Claim ceiling**

Defensible：
- 「1999 年連續四個隨機試驗同方向：放療期間加 cisplatin，死亡風險降三到五成（各試驗 RR 0.51–0.61，族群各異）；統合 18 個試驗的個別病人資料後，5 年存活的絕對提升是 6 個百分點（HR 0.81）。每週一次、低劑量，角色是放射增敏。」[S20][S21][S22][S23][S24][S3]
- 「化放療**之後**再補四個療程化療，隨機試驗（919 人）的答案是零：5 年存活 72% 對 71%，嚴重不良事件反而多——作者直接寫『不應該這樣給』。更多化療不等於更好。」[S25]
- 「化放療**之前**先打六週較溫和的化療（INTERLACE），5 年存活 80% 對 72%——但這是加在近乎滿分的化放療（92% 完成近接、45 天完成療程）之上、間隔只有 7 天的結果，而且學界對它是否該成為新標準仍有具名爭論。」[S26][S27]
- 「化放療加 pembrolizumab（KEYNOTE-A18）：**限定高風險族群**，36 個月存活 82.6% 對 74.8%（HR 0.67）；代價是免疫相關不良事件 39% 對 17%。美國核准的範圍比試驗更窄（III–IVA）；在台灣，健保給付規定目前查無子宮頸癌這一項，此適應症屬自費，費用與適用性要跟團隊確認。」[S29][S30][S31][S32][S39][S41]
- 「腎功能不好不能打 cisplatin 的人，指引的替代是每週 carboplatin（AUC2）——台灣健保 9.2 條文恰好允許 CCr<60 的惡性腫瘤病人使用 carboplatin。」[S3][S39]

Would overstate：
- ✗ 把 OUTBACK 寫成註腳或「補充說明」——**固定紅線：尷尬結論當主旨**
- ✗「INTERLACE 已是新標準／每個人都該先打誘導化療。」——爭論中、族群與實作條件要帶 [S26][S27]
- ✗「免疫治療是局部晚期的新標準。」——族群限定（IB2–IIB 淋巴結陽性或 III–IVA）；台灣給付查無；最終分析未見刊。三個限制都要同段出現 [S29][S30][S41][S46]
- ✗「OS HR 0.67＝死亡風險降 33%，所以每個人多活…」——寫絕對值（36 個月 82.6 vs 74.8%）為主，倍數為輔 [S30]
- ✗ 寫出 OUTBACK 的 PFS／無病存活數字——本次只驗證到 OS 與不良事件，PFS 不在摘要內，不可憑記憶補 [S25]
- ✗「6% 很小，所以化療可有可無。」——6% 是**全族群平均**的絕對存活提升，且同步化療同時減少局部與遠端復發；反向失真 [S24]
- ✗ cisplatin 個別毒性數字（腎、聽力、血球的百分比）——**C 組主場**，B3 只保留試驗回報的整體率
- ✗「carboplatin 跟 cisplatin 一樣有效。」——ESGO 寫的是「cisplatin 不適用時的替代」；效力證據較弱（C 組簡報 S30 已載其統合分析），B3 不得寫成等效 [S3]

**Caveats / safety notes**

- 期別標籤地雷：OUTBACK／INTERLACE 用 FIGO 2008、KEYNOTE-A18 用 FIGO 2014、ESGO 用 TNM。逐數字帶標籤，不換算。
- KEYNOTE-A18 的免疫相關不良事件（39%）寫進正文時，要與 HR 0.67 同段（好處與代價同段是本專題慣例）。
- INTERLACE 的誘導化療會用到 paclitaxel（神經毒性）——症狀層歸 C 組；B3 只寫「較溫和但不是沒有代價，G3+ 59% vs 48%」。
- 「為什麼不能只做放療」的劑量生物學（總治療時間、加速再增殖）歸 C2；B3 用一句話指路。
- 費用紀律：pembrolizumab 自費金額本次查無台灣公定數字 → 不寫金額，寫「向醫務課／個管師確認」。

**Taiwan status**

- **Pembrolizumab（含所有免疫檢查點抑制劑）：健保藥品給付規定第 9 節（115.8.21 更新版 PDF，2026-08-30 下載 grep）9.69 條列適應症中無子宮頸癌**；全檔「子宮頸」僅出現 4 次：3 次在 bevacizumab 9.37.4、1 次在 CAR-T 排除條件。→ KEYNOTE-A18（局部晚期）與 KEYNOTE-826（復發轉移第一線）情境在台灣皆屬自費 gap [S39][S41]
- **Bevacizumab：9.37.4 有明確條文（109/6/1 生效、113/3/1 修訂）**：「(1) Bevacizumab 與 cisplatin 及 paclitaxel 合併使用，可用於持續性、復發性或轉移性之子宮頸癌。(2) 與 paclitaxel 及 topotecan 合併使用，作為無法接受含鉑類藥物治療患者之持續性、復發性或轉移性之子宮頸癌。(3) 須經事前審查核准後使用，每次申請之療程以 15 週為限，再次申請必須提出客觀證據（如影像學）證實無惡化」 [S39] ——**此條與 pembrolizumab 的 gap 為共用註，D4 寫復發轉移時直接重用**
- **Carboplatin：9.2 條文原文「限 1.卵巢癌患者。2.腎功能不佳(CCr<60)或曾作單側或以上腎切除之惡性腫瘤患者使用」**（115/8/1 版有效）——與 ESGO「cisplatin 不適用改 carboplatin」銜接 [S39][S3]
- Cisplatin：第 9 節無 cisplatin 專屬給付條文（僅出現在其他藥品的併用條文中；與 C 組簡報結論一致，本次重新 grep 確認）→ 給付細節寫「向醫務課確認」 [S39]

---

# B4 — 年輕病人：生育與卵巢還保得住嗎　【時效性：治療開始前】

**Key facts**

*誰可以考慮保留生育的手術（ESGO 2023 的嚴格條件，原文層級）*
- 適用門檻：「Fertility sparing treatment can be considered in patients with cervical cancer **<2 cm (squamous cell carcinoma and HPV-related adenocarcinoma)** who want to preserve the option to have children. Before initiating fertility sparing therapy, **consultation at an onco-fertility center and discussion in a multidisciplinary tumor board is recommended** [III, B]」；諮詢必須涵蓋腫瘤學與產科風險、以及若切緣或淋巴結陽性將**放棄**保留生育治療的可能 [III, A] [S3]
- 淋巴結是第一關：「In case of intraoperatively proven PLN involvement, **fertility-sparing surgery should be abandoned** and patients should be referred for CTRT and BT [IV, B]」 [S3]
- 術式對應（摘要層級）：T1a1/T1a2 →圓錐切除或單純子宮頸切除即足夠（不論 LVSI）；T1b1 LVSI 陰性→圓錐切除或單純子宮頸切除亦可，根治性子宮頸切除仍是選項；**T1b1 LVSI 陽性→根治性（type B）子宮頸切除**；術中同時放永久性子宮頸環紮 [IV, B] [S3]
- **腫瘤 >2 cm 不是標準**：「Fertility sparing therapy for patients with tumors greater than 2 cm is significantly associated with a higher risk of recurrence and **should not be considered as a standard treatment**」；>2 cm 想保留生育的 NACT＋保守手術路線存在文獻但療程與範圍「still a matter of debate」，且必須先確認淋巴結陰性 [S3]
- 孕產規則：「Any pregnancy following fertility sparing therapy should be considered as a **high-risk pregnancy**」；做過環紮者**只能剖腹產**；完成生育後不強制切除子宮（[V, D]） [S3]

*保留生育手術的腫瘤學結果（誠實的兩面）*
- Smith 2020 系統性回顧（47 篇、2,566 名接受根治性子宮頸切除＋淋巴結評估者；74.8% IB1、69.2% ≤2 cm）：**中位復發率 3.3%（範圍 0–25%）**、5 年無復發存活中位 94.6%、5 年整體存活中位 97.4%；**計畫做子宮頸切除的人有 9% 術中臨時改成子宮切除**（切緣或淋巴結不過關）；術後懷孕率 23.9%、懷孕者活產率 75.1% [S33]
- 適用者是少數（「誠實的多數」素材）：門檻本身（<2 cm、淋巴結陰性、非高風險組織型態、想生育）已排除多數病人 [S3][S35]；加上 9% 術中轉換 [S33]——寫法：這是一條為少數人保留的窄路，不是「年輕就可以選」的選項

*產科結果（保住子宮 ≠ 平安足月）*
- Bentivegna 2016（Fertil Steril 系統性回顧，2,777 名保留生育手術、944 次懷孕）：整體生育率 55%、活產率 70%、**早產率 38%**；第二孕期流產與早產大多與早期破水（PPROM）有關；單純子宮頸切除／圓錐切除者早產率顯著較低（術式越大、早產越多） [S34]
- 同團隊 Lancet Oncol 回顧：保留生育只適用於預後良好、無需輔助治療者（IB <4 cm、淋巴結陰性、非侵襲性組織型態）；≤2 cm 與 LVSI 是選術式的兩大軸 [S35]

*放療這一側：子宮的傷害是不可逆的（為什麼「卵巢保住了」≠「能自己懷孕」）*
- Teh 2014（文獻回顧）：子宮受照後生育力下降、懷孕併發症增加；**成人期子宮劑量 >45 Gy 建議告知避免自行懷孕**；<4 Gy 未見子宮功能受損；成人全身照射（約 12 Gy）懷孕仍可能但流產與併發症多 [S36]
- Wo & Viswanathan 2009（回顧）：腹部骨盆放療後的子宮功能異常表現為**流產、早產、低出生體重、胎盤異常**；卵巢劑量與提早停經呈劑量依存 [S37]
- 對接子宮頸癌的實際劑量：根治性化放療的骨盆外照就是 45–50 Gy、近接再往上加（劑量細節歸 C1）[S3]——子宮整個在照野裡。**卵巢移位保的是荷爾蒙（避免提早停經），保不了「用自己的子宮懷孕」**；這句是 B4 的核心誠實句 [S36][S37][S3]
- 因此順序有兩層：(1) 還想「懷孕」→ 治療策略本身要在保留生育手術可行性上先談（見上）；(2) 只能做放療者 → 能保的是卵巢功能（移位）與卵子／胚胎（冷凍），子宮功能保不住 [S3][S36]

*時間窗（時效性紅線的證據）*
- ASCO 2025 生育保存指引更新：**「FP approaches should be discussed before cancer-directed therapy」**；女性的已確立方法包括胚胎、卵子、卵巢組織冷凍、**卵巢移位**與保守性婦科手術；GnRHa 不可取代已確立方法 [S38]
- ESGO：卵巢移位「should be discussed **upfront** with the patient [IV, A]」；淋巴結陽性者不建議移位 [IV, D] [S3]
- 站上 `insight-cervix-ovary` 的醫師的話已寫：「移位必須趕在放療開始前完成…等療程排好再問就來不及」，並提醒不要為了移位延後放療——B4 指路即可，不重寫（內容清單見下節）

*指路（一句話＋清單，不重複）*
- 卵巢移位的劑量資料（8 Gy 分水嶺、71% POI、17 人回溯）→ **站上 `insight-cervix-ovary`**，B4 一句話：「移位之後保不保得住、劑量壓到多低才有意義，我在另一篇寫了完整數字」
- 冷凍卵子／胚胎的機制、成功率（43% 累積活產）、台灣 114/9 補助（限乳癌與血液癌）→ **站上 `care-fertility`**，B4 一句話：「冷凍留下的是機會不是小孩、補助涵蓋誰，見那一篇」

**Claim ceiling**

Defensible：
- 「保留子宮的手術（子宮頸切除術）有嚴格門檻：腫瘤小於 2 公分、淋巴結陰性、鱗癌或 HPV 相關腺癌、而且要在腫瘤與生殖醫學團隊共同評估之下——大於 2 公分做保留生育治療，復發風險顯著較高，指引明說不是標準治療。」[S3]
- 「符合條件的人結果不差：系統性回顧裡復發率中位 3.3%、5 年存活九成七；但有 9% 的人在手術台上因為切緣或淋巴結不合格，臨時改成了子宮切除——這個可能性術前就要知道。」[S33]
- 「保住子宮不等於平安足月：術後懷孕的早產率約 38%，大多跟早期破水有關；懷孕一律當高風險妊娠管理，做過環紮只能剖腹產。」[S34][S3]
- 「如果治療是根治性化放療，骨盆的照射劑量遠超過子宮能承受的範圍——回顧文獻建議成人子宮劑量超過 45 Gy 就應告知避免自行懷孕。所以卵巢移位保的是荷爾蒙、不是懷孕能力；想留下血緣後代的機會，靠的是治療前冷凍卵子或胚胎。」[S36][S37][S3]
- 「這一題全部有時效：保留生育的可行性、卵巢移位、冷凍，都必須在治療開始前談定——ASCO 指引原文就是『在癌症治療之前討論』。」[S38][S3]
- 「淋巴結有轉移，保留生育的路就要停：這不是誰狠心，是指引寫的安全底線。」[S3]

Would overstate：
- ✗「年輕就可以選保留生育。」——門檻是腫瘤條件不是年齡；「誠實的多數」不符合條件，要寫
- ✗「子宮頸切除術跟子宮切除一樣安全。」——沒有隨機比較；Smith 是案例系列的系統性回顧、追蹤長短不一，作者自己說缺高層級證據 [S33]
- ✗「>2 cm 也有辦法（NACT）。」——ESGO 寫的是「文獻中有描述、仍在辯論」；只能寫成研究性選項且須先淋巴結分期 [S3]
- ✗「放療後絕對不可能懷孕。」——Teh 的寫法是「>45 Gy 建議避免嘗試」；有 TBI 12 Gy 後懷孕的資料。寫「子宮的傷害不可逆、劑量遠超過建議上限、不建議嘗試」，不寫「絕對不可能」 [S36]
- ✗ 重複 8 Gy、43% 活產、7 萬元補助等站上已有數字——**歸屬違規**（見下節清單）
- ✗「凍了卵就等於保住生育。」——care-fertility 的主旨句（「冷凍是把機會保留下來，不是把小孩保留下來」），B4 指路即可，不改寫成承諾
- ✗ 為了保生育延後或改變腫瘤治療的任何暗示——反向紅線；ESGO/ASCO 都是「並行討論、不增加腫瘤學風險」 [S3][S38]

**Caveats / safety notes**

- 【時效性】這篇的行動句必須在最前面就出現：「確診後第一次門診就說出『我還想生』」——錯過治療開始，多數選項消失（固定紅線）。
- 分期標籤：ESGO 用 TNM（T1b1≈FIGO 2018 IB1 ≤2 cm…注意 FIGO 2018 的 IB1 定義即 ≤2 cm，與 FIGO 2009 不同）；Smith/Bentivegna 世代多為舊分期。寫「2 公分」這個實體門檻比寫期別代號安全。
- Smith 的懷孕率 23.9% 分母是全部接受手術者（不是全部嘗試懷孕者）——不可寫成「四分之三懷不了」。
- 早產 38% 是「保留生育手術後懷孕」的整體值，各術式差很大（術式越小越低）[S34]——引用帶術式。
- SHAPE 試驗（低風險改單純子宮切除）與本篇無直接關係，本次未查證 → 不寫。
- 男性伴侶、AMH、GnRHa、卵巢組織冷凍細節 → care-fertility 已寫（見下節），B4 一律指路。
- 收尾（B 組方向「帶哪幾份資料去談」）：病理報告（腫瘤大小、組織型態、LVSI）、影像（MRI 大小與淋巴結）、生殖醫學科的轉介單——三份都有出處支撐 [S3]。

**Taiwan status**

- **生育保存補助（2026-08-30 覆核 mohw.gov.tw 原頁）**：「醫療性生育保存補助試辦方案」自 114 年 9 月 1 日實施，補助對象原文「罹患**乳癌或血液癌**具我國國籍之 18 歲至 40 歲民眾」；女性取卵每次上限 7 萬元、男性取精每次上限 8 千元、每人一生至多 2 個療程、限特約人工生殖機構 [S40]。**子宮頸癌不在補助對象內**——這句 care-fertility 與 insight-cervix-ovary 都已寫，B4 指路並保留一句「各縣市另有補助、向衛生局或個管師確認」（care-fertility 已載，出處在該文）。
- 健保「醫療服務給付項目」檔（114.01.01 版 XLS）：**80211C Radical trachelectomy（根治性子宮頸切除）42,638 點**、80210C Abdominal trachelectomy 13,871 點、80205C 圓錐切除 2,810 點——支付項目存在；給付條件與自付細節不在檔內 → 「向醫務課確認」 [S42]。
- 凍卵療程本身的自費金額：不查、不寫（care-fertility 亦未給數字）；一律「向生殖醫學科與醫務課確認」。

---

## 站上既有文章的內容清單（B4 指路不重複；寫 B4 前必讀）

### `insight-cervix-ovary.html`〈把卵巢搬離照野，8 Gy 是分水嶺〉（醫學新知，2026-08-25 上線）已寫的內容——B4 不得重複：
1. 卵巢是對輻射最敏感的器官之一；散射個位數 Gy 即可使其永久停工；提早停經的後果（熱潮紅、骨質、心血管、性功能與情緒）。
2. 卵巢移位（oophoropexy）的定義（放療前腹腔鏡把卵巢上移固定至照野外）；ASCO 2025 指引將其與胚胎／卵子／卵巢組織冷凍並列為已確立方法（引 Su 2025，PMID 40106739）。
3. **8 Gy／16 Gy 分水嶺的全部數字**：2026 Practical Radiation Oncology 單機構回溯 17 人（Shogan，PMID 42409314）——71% POI；平均劑量 >8 Gy 全數 POI、<8 Gy 為 50%（P=.03）；最高劑量 16 Gy 同型結果；POI 者受照較少側卵巢平均劑量中位 12.0 Gy vs 未 POI 4.4 Gy。
4. 2019 Radiation Oncology 105 人研究（Yin，doi 10.1186/s13014-019-1312-2）：39% 保住卵巢功能；建議平均 <5.32 Gy、最高 <9.985 Gy。
5. 手術到放療中位間隔 40 天、最快一週內開始放療無急性併發症。
6. 台灣端：光子放療（IMRT/IGRT/VMAT）屬健保給付範疇、質子重粒子自費（引秀傳衛教頁）；**114/9 生育保存補助限乳癌與血液癌、婦癌尚未納入**（引 mohw cp-16-83501）。
7. 醫師的話：移位要趕在放療前、第一次門診就開口、但不要為移位延後放療。
→ **B4 的寫法**：一句話「卵巢移位能不能保住功能、劑量要壓到多低，我把數字寫在〈把卵巢搬離照野，8 Gy 是分水嶺〉」；B4 自己只保留「移位保荷爾蒙、保不了懷孕」的分工句（用 [S36][S37] 支撐）。

### `care-fertility.html`〈有些選項，治療開始就消失了〉（病人衛教）已寫的內容——B4 不得重複：
1. 「治療開始前處理、開始之後選項消失」的總論；ASCO 2018 指引（Oktay，PMID 29620997）：盡早討論、記錄、轉介；精卵胚冷凍是標準作法。
2. 癌症本身可能先損傷生殖力（韓國精子研究）。
3. 傷害依方案分級：烷化劑 90–100% 男性無精症／30 歲以下女性 5–25% 卵巢早衰 vs 非烷化劑 <10%（何杰金資料）；年齡是女性關鍵變數。
4. 男性凍精門檻低（8 千元補助）、睪丸癌問卷（33% 冷凍、11% 用到）。
5. **「凍了就會有小孩嗎：累積活產率 43%」**（Cascante 2024，PMID 38955888）；冷凍當下年齡決定成敗（墨爾本 3,164 人，癌症組平均 31.3 歲）；主旨句「冷凍是把機會保留下來，不是把小孩保留下來」。
6. GnRHa 不可取代冷凍（ASCO 立場＋Lambertini IPD 統合：POI 14.1% vs 30.9%、懷孕 10.3% vs 5.5%、存活無差）。
7. 卵巢組織冷凍：適用對象（來不及刺激者、青春期前）、婦癌僅佔 7.5%、78.1% 恢復內分泌、移植物中位存活 32 個月；惡性細胞帶回的安全疑慮。
8. AMH 不等於「還能不能生」。
9. **台灣 114/9/1 補助全細節**（乳癌 0–3 期或血液癌、18–40 歲、7 萬／8 千、一生 2 療程、特約機構、2 個月內施術、6 個月內申請；縣市補助另查）；試管嬰兒補助 3.0 是另一回事；人工生殖法第 2/11/21 條（受術夫妻定義、十年銷毀）。
10. 「下次門診就可以問的四句」與治療期間仍要避孕的提醒。
→ **B4 的寫法**：一句話「冷凍的機制、成功率、台灣補助涵蓋誰，站上〈有些選項，治療開始就消失了〉整篇在寫這個」；B4 只寫子宮頸專屬的三件事（子宮頸切除術、時間窗、放療後的子宮）。

---

## Sources（單一編號序列；PASS 除非標 FAIL）

- **[S1] PASS** — Landoni F, Maneo A, Colombo A, et al. (1997). *Randomised study of radical surgery versus radiotherapy for stage Ib-IIa cervical cancer.* Lancet 350(9077):535-540. PMID 9284774, doi 10.1016/s0140-6736(97)02250-2. URL: https://doi.org/10.1016/s0140-6736(97)02250-2 — 343 人；5 年 OS/DFS 兩組 83%/74%；嚴重併發症 28% vs 12%；輔助放療 62/114 與 46/55；「no treatment of choice」「combination…worst morbidity」原文。Route: Europe PMC REST (TITLE) + abstract (resultType=core)
- **[S2] PASS** — Landoni F, Colombo A, Milani R, Placa F, Zanagnolo V, Mangioni C. (2017). *Randomized study between radical surgery and radiotherapy for the treatment of stage IB-IIA cervical cancer: 20-year update.* J Gynecol Oncol 28(3):e34. PMID 28382797, PMC5391393, doi 10.3802/jgo.2017.28.e34. URL: https://doi.org/10.3802/jgo.2017.28.e34 — 最短追蹤 19 年；20 年 OS 72% vs 77%（p=0.280）；復發 94 例（28%）；多變項因子。Route: Europe PMC REST
- **[S3] PASS** — Cibula D, Raspollini MR, Planchamp F, et al. (2023). *ESGO/ESTRO/ESP Guidelines for the management of patients with cervical cancer — Update 2023.* Int J Gynecol Cancer 33(5):649-666. PMID 37127326, PMC10176411, doi 10.1136/ijgc-2023-004429. URL: https://doi.org/10.1136/ijgc-2023-004429 — 本組引用之原文（全部由 fullTextXML grep 取得）：avoid combining radical surgery and radiotherapy [IV,A]；risk factors known at diagnosis → definitive CTRT without radical surgery [IV,A]；laparotomy is the standard approach [I,A]／MIS 僅限 <2 cm 低風險；術中 LN 陽性→棄手術轉 CTRT [III,A]；中風險輔助放療／高風險輔助 CTRT 條件；T1b3–T4a definitive RT＋concomitant chemo [I,A]；T1b3/T2a2 灰色地帶；NACT or CTRT followed by surgery not recommended [IV,D]；weekly cisplatin 40 mg/m² 標準、carboplatin AUC2 替代；fertility sparing <2 cm 條件全套、>2 cm 非標準、cerclage 與剖腹產、ovarian transposition upfront [IV,A]／N1 不建議 [IV,D]。Route: Europe PMC REST (EXT_ID) + fullTextXML via PMC10247855（Virchows Arch 同文版本）grep 原文
- **[S4] PASS** — Sedlis A, Bundy BN, Rotman MZ, Lentz SS, Muderspach LI, Zaino RJ. (1999). *A randomized trial of pelvic radiation therapy versus no further therapy in selected patients with stage IB carcinoma of the cervix after radical hysterectomy and pelvic lymphadenectomy: A Gynecologic Oncology Group Study.* Gynecol Oncol 73(2):177-183. PMID 10329031, doi 10.1006/gyno.1999.5387. URL: https://doi.org/10.1006/gyno.1999.5387 — GOG 92；277 人；RR 0.53；復發 15% vs 28%；G3/4 6% vs 2.1%。**Sedlis 細項組合表不在摘要，未驗證。** Route: Europe PMC REST
- **[S5] PASS** — Rotman M, Sedlis A, Piedmonte MR, et al. (2006). *A phase III randomized trial of postoperative pelvic irradiation in Stage IB cervical carcinoma with poor prognostic features: follow-up of a gynecologic oncology group study.* Int J Radiat Oncol Biol Phys 65(1):169-176. PMID 16427212, doi 10.1016/j.ijrobp.2005.10.019. URL: https://doi.org/10.1016/j.ijrobp.2005.10.019 — 復發 HR 0.54；惡化或死亡 HR 0.58；OS HR 0.70（p=0.074 未顯著）；腺癌次族群訊號。Route: Europe PMC REST
- **[S6] PASS** — Peters WA 3rd, Liu PY, Barrett RJ 2nd, et al. (2000). *Concurrent chemotherapy and pelvic radiation therapy compared with pelvic radiation therapy alone as adjuvant therapy after radical surgery in high-risk early-stage cancer of the cervix.* J Clin Oncol 18(8):1606-1613. PMID 10764420, doi 10.1200/jco.2000.18.8.1606. URL: https://doi.org/10.1200/jco.2000.18.8.1606 — 243 人；淋巴結＋/切緣＋/子宮旁＋；4 年 PFS 80 vs 63%、OS 81 vs 71%；RT 單獨 HR 2.01/1.96。（2023 年 JCO 重刊版 PMID 37797409 同數字，引原版。）Route: Europe PMC REST
- **[S7] PASS** — Casarin J, Meschini T, Schivardi G, et al. (2026). *Determinants of adjuvant radiotherapy in early-stage cervical cancer: a retrospective analysis of the SUCCOR cohort.* Int J Gynecol Cancer 36(2):104448. PMID 41534444, doi 10.1016/j.ijgc.2025.104448. URL: https://doi.org/10.1016/j.ijgc.2025.104448 — FIGO 2009 IB1 淋巴結陰性 572 人；40.6% 接受輔助放療；其中 56.9% 不符 Sedlis；符合者 13.2% 未治療；符合 Sedlis OR 4.44。Route: Europe PMC REST
- **[S8] PASS** — Pan TL, Pareja R, Chiva L, et al. (2024). *Accuracy of pre-operative tumor size assessment compared to final pathology and frequency of adjuvant treatment in patients with FIGO 2018 stage IB2 cervical cancer.* Int J Gynecol Cancer 34(12):1861-1866. PMID 39448083, doi 10.1136/ijgc-2024-005986. URL: https://doi.org/10.1136/ijgc-2024-005986 — 675 名 FIGO 2018 IB2 根治性子宮切除；51% 輔助治療（54% CCRT／44% RT）；病理 ≥3 cm 者 61%；淋巴結陽性率隨腫瘤增大（13%→21%）。Route: Europe PMC REST
- **[S9] PASS** — Sturdza A, Pötter R, Fokdal LU, et al. (2016). *Image guided brachytherapy in locally advanced cervical cancer: Improved pelvic control and survival in RetroEMBRACE, a multicenter cohort study.* Radiother Oncol 120(3):428-433. PMID 27134181, doi 10.1016/j.radonc.2016.03.011. URL: https://doi.org/10.1016/j.radonc.2016.03.011 — 731 人（IIB 50.4%、77.4% 同步化療）；3/5 年 OS 74%/65%、CSS 79%/73%；5 年 LC：IB 98%、IIB 91%、IIIB 75%。Route: Europe PMC REST
- **[S10] PASS** — Pötter R, Tanderup K, Schmid MP, et al.; EMBRACE Collaborative Group. (2021). *MRI-guided adaptive brachytherapy in locally advanced cervical cancer (EMBRACE-I): a multicentre prospective cohort study.* Lancet Oncol 22(4):538-547. PMID 33794207, doi 10.1016/S1470-2045(20)30753-1. URL: https://doi.org/10.1016/s1470-2045(20)30753-1 — 1,341 人；5 年局部控制 92%；G3–5 各器官 3.2–8.5%。Route: Europe PMC REST
- **[S11] PASS** — Keys HM, Bundy BN, Stehman FB, et al. (2003). *Radiation therapy with and without extrafascial hysterectomy for bulky stage IB cervical carcinoma: a randomized trial of the Gynecologic Oncology Group.* Gynecol Oncol 89(3):343-353. PMID 12798694, doi 10.1016/s0090-8258(03)00173-2. URL: https://doi.org/10.1016/s0090-8258(03)00173-2 — GOG 71；256 名 bulky IB；「no clinically important benefit」；局部復發 27%→14% 但存活無差（URR 0.77，p=0.07）；4–6 cm 次族群訊號（URR 0.58/0.60）。Route: Europe PMC REST
- **[S12] PASS** — Kokka F, Bryant A, Olaitan A, Brockbank E, Powell M, Oram D. (2022). *Hysterectomy with radiotherapy or chemotherapy or both for women with locally advanced cervical cancer.* Cochrane Database Syst Rev 8:CD010260. PMID 35994243, PMC9394583, doi 10.1002/14651858.cd010260.pub3. URL: https://doi.org/10.1002/14651858.cd010260.pub3 — 11 RCT、2,683 人；NACT＋子宮切除 vs CCRT：OS HR 0.94（0.76–1.16）、5 年 DFS 57% vs 65.6%（NACT+手術較差，IIB 為主）；RT＋子宮切除 vs RT：HR 0.89（0.61–1.29）（2015 版摘要載明，同一試驗＝GOG 71）。Route: Europe PMC REST（2022 版＋2015 版摘要皆驗）
- **[S13] PASS** — Ramirez PT, Frumovitz M, Pareja R, et al. (2018). *Minimally Invasive versus Abdominal Radical Hysterectomy for Cervical Cancer.* N Engl J Med 379(20):1895-1904. PMID 30380365, doi 10.1056/NEJMoa1806395. URL: https://doi.org/10.1056/nejmoa1806395 — LACC；631 人（IA1 LVSI/IA2/IB1，91.9% IB1；84.4% 腹腔鏡/15.6% 機器人）；4.5 年 DFS 86.0 vs 96.5%（−10.6）；3 年 DFS HR 3.74；3 年 OS 93.8 vs 99.0%、HR 6.00。Route: Europe PMC REST
- **[S14] PASS** — Melamed A, Margul DJ, Chen L, et al. (2018). *Survival after Minimally Invasive Radical Hysterectomy for Early-Stage Cervical Cancer.* N Engl J Med 379(20):1905-1914. PMID 30379613, PMC6464372, doi 10.1056/NEJMoa1804923. URL: https://doi.org/10.1056/nejmoa1804923 — 2,461 名 IA2/IB1（2010–2013 NCDB，傾向分數加權）：4 年死亡 9.1 vs 5.3%（HR 1.65，1.22–2.22）；SEER 中斷時間序列：2006 後 4 年相對存活每年 −0.8%。Route: Europe PMC REST
- **[S15] PASS** — Ramirez PT, Robledo KP, Frumovitz M, et al. (2024). *LACC Trial: Final Analysis on Overall Survival Comparing Open Versus Minimally Invasive Radical Hysterectomy for Early-Stage Cervical Cancer.* J Clin Oncol 42(23):2741-2746. PMID 38810208, doi 10.1200/jco.23.02335. URL: https://doi.org/10.1200/jco.23.02335 — 4.5 年 DFS 85.0 vs 96.0%（HR 3.91，2.02–7.58）；4.5 年 OS 90.6 vs 96.2%（HR 2.71，1.32–5.59，p=0.007）；「an open approach should be standard of care」原文。Route: Europe PMC REST
- **[S16] PASS** — Chiva L, Zanagnolo V, Querleu D, et al. (2020). *SUCCOR study: an international European cohort observational study comparing minimally invasive surgery versus open abdominal radical hysterectomy in patients with stage IB1 cervical cancer.* Int J Gynecol Cancer 30(9):1269-1277. PMID 32788262, doi 10.1136/ijgc-2020-001506. URL: https://doi.org/10.1136/ijgc-2020-001506 — 加權 693 名 FIGO 2009 IB1；MIS 復發 HR 2.07、死亡 HR 2.45；舉宮器 HR 2.76；無舉宮器 HR 1.58（NS）；保護性陰道縫合 HR 0.63（NS）。Route: Europe PMC REST
- **[S17] PASS** — Li RZ, Sun LF, Li R, Wang HJ. (2023). *Survival after minimally invasive radical hysterectomy without using uterine manipulator for early-stage cervical cancer: A systematic review and meta-analysis.* BJOG 130(2):176-183. PMID 36331008, doi 10.1111/1471-0528.17339. URL: https://doi.org/10.1111/1471-0528.17339 — 6 個觀察性研究、2,150 人；不用舉宮器的 MIS 復發風險仍高（HR 1.55，1.15–2.10）。Route: Europe PMC REST
- **[S18] PASS** — Manzour N, Chiva L, Zanagnolo V, et al. (2025). *SUCCOR 10 years: a decade's perspective on radical hysterectomy outcomes in cervical cancer.* Int J Gynecol Cancer 35(5):101690. PMID 40055121, doi 10.1016/j.ijgc.2025.101690. URL: https://doi.org/10.1016/j.ijgc.2025.101690 — 556 人完成 10 年追蹤；5/10 年 OS 97%/89%；10 年復發 9%，其中 78% 在前 5 年；10 年 DFS/OS 依術式無顯著差異（p=0.12，觀察性）。Route: Europe PMC REST
- **[S19] PASS** — Meng X, Jiang Y, Chang X, Zhang Y, Guo Y. (2022). *Conditional survival analysis and real-time prognosis prediction for cervical cancer patients below the age of 65 years.* Front Oncol 12:1049531. PMID 36698403, PMC9868950, doi 10.3389/fonc.2022.1049531. URL: https://doi.org/10.3389/fonc.2022.1049531 — SEER 18,511 名 <65 歲（2004–2019）；已存活 5–6 年者，其後 10–15 年死於子宮頸癌風險 <5%（一般族群條件存活，非微創專屬）。Route: Europe PMC REST
- **[S20] PASS** — Rose PG, Bundy BN, Watkins EB, et al. (1999). *Concurrent cisplatin-based radiotherapy and chemotherapy for locally advanced cervical cancer.* N Engl J Med 340(15):1144-1153. PMID 10202165, doi 10.1056/NEJM199904153401502. URL: https://doi.org/10.1056/nejm199904153401502 — GOG 120；526 名 IIB–IVA；cisplatin 組 PFS RR 0.57/0.55、OS RR 0.61/0.58（vs hydroxyurea）；每週 cisplatin 40 mg/m²×6 方案原文。Route: Europe PMC REST
- **[S21] PASS** — Keys HM, Bundy BN, Stehman FB, et al. (1999). *Cisplatin, radiation, and adjuvant hysterectomy compared with radiation and adjuvant hysterectomy for bulky stage IB cervical carcinoma.* N Engl J Med 340(15):1154-1161. PMID 10202166, doi 10.1056/NEJM199904153401503. URL: https://doi.org/10.1056/nejm199904153401503 — GOG 123；369 名 bulky IB；惡化 RR 0.51、死亡 RR 0.54。（毒性數字歸 C 組。）Route: Europe PMC REST
- **[S22] PASS** — Morris M, Eifel PJ, Lu J, et al. (1999). *Pelvic radiation with concurrent chemotherapy compared with pelvic and para-aortic radiation for high-risk cervical cancer.* N Engl J Med 340(15):1137-1143. PMID 10202164, doi 10.1056/NEJM199904153401501. URL: https://doi.org/10.1056/nejm199904153401501 — RTOG 90-01；403 人；5 年 OS 73 vs 58%、DFS 67 vs 40%。Route: Europe PMC REST
- **[S23] PASS** — Whitney CW, Sause W, Bundy BN, et al. (1999). *Randomized comparison of fluorouracil plus cisplatin versus hydroxyurea as an adjunct to radiation therapy in stage IIB-IVA carcinoma of the cervix with negative para-aortic lymph nodes: a Gynecologic Oncology Group and Southwest Oncology Group study.* J Clin Oncol 17(5):1339-1348. PMID 10334517, doi 10.1200/jco.1999.17.5.1339. URL: https://doi.org/10.1200/jco.1999.17.5.1339 — GOG 85；368 名可評估；CF 組 PFS p=.033、OS p=.018；嚴重白血球毒性 4% vs 24%。Route: Europe PMC REST
- **[S24] PASS** — Chemoradiotherapy for Cervical Cancer Meta-Analysis Collaboration (CCCMAC). (2008). *Reducing uncertainties about the effects of chemoradiotherapy for cervical cancer: a systematic review and meta-analysis of individual patient data from 18 randomized trials.* J Clin Oncol 26(35):5802-5812. PMID 19001332, PMC2645100, doi 10.1200/jco.2008.16.4368. URL: https://doi.org/10.1200/jco.2008.16.4368 — 13 個試驗（CRT vs 同樣 RT）：5 年存活 +6%（HR 0.81，p<.001）；非鉑類亦有效（HR 0.77）；期別間獲益大小有訊號；1999 NCI alert 背景句。Route: Europe PMC REST
- **[S25] PASS** — Mileshkin LR, Moore KN, Barnes EH, et al. (2023). *Adjuvant chemotherapy following chemoradiotherapy as primary treatment for locally advanced cervical cancer versus chemoradiotherapy alone (OUTBACK): an international, open-label, randomised, phase 3 trial.* Lancet Oncol 24(5):468-482. PMID 37080223, PMC11075114, doi 10.1016/s1470-2045(23)00147-x. URL: https://doi.org/10.1016/s1470-2045(23)00147-x — 919 名（FIGO 2008 IB1N+/IB2/II/IIIB/IVA）；5 年 OS 72% vs 71%（HR 0.90，0.70–1.17，p=0.81）；G3–4 嗜中性球 20 vs 8%、貧血 18 vs 8%、SAE 30 vs 22%；「should not be given in this setting」原文。**PFS 數字不在摘要，未驗證。** Route: Europe PMC REST
- **[S26] PASS** — McCormack M, Eminowicz G, Gallardo D, et al. (2024). *Induction chemotherapy followed by standard chemoradiotherapy versus standard chemoradiotherapy alone in patients with locally advanced cervical cancer (GCIG INTERLACE): an international, multicentre, randomised phase 3 trial.* Lancet 404(10462):1525-1535. PMID 39419054, doi 10.1016/s0140-6736(24)01438-7. URL: https://doi.org/10.1016/s0140-6736(24)01438-7 — 500 人（70% IIB、43% N+；2012–2022）；誘導 carboplatin AUC2＋paclitaxel 80 週×6；5 年 PFS 72 vs 64%（HR 0.65）；5 年 OS 80 vs 72%（HR 0.60）；G3+ 59 vs 48%；間隔中位 7 天；92% 完成 EBRT+BT、OTT 中位 45 天。Route: Europe PMC REST
- **[S27] PASS（標題層級）** — Petric P, Lindegaard JC, Schmid MP, Jürgenliemk-Schulz I, Mahantshetty U, Kirisits C, Pötter R. (2025). *INTERLACE: not a new standard for cervical cancer chemoradiation.* Lancet 406(10505):806-807. PMID 40849130, doi 10.1016/s0140-6736(25)01114-6. URL: https://doi.org/10.1016/s0140-6736(25)01114-6 — 通訊無摘要；引用限於「EMBRACE 團隊具名質疑其為新標準」的立場陳述（作者回覆 PMID 40849132 同期）。Route: Europe PMC REST
- **[S28] PASS** — Eminowicz G, Vaja S, Gallardo D, et al. (2025). *Induction chemotherapy followed by chemoradiation in locally advanced cervical cancer: Quality of life outcomes of the GCIG INTERLACE trial.* Eur J Cancer 220:115375. PMID 40139003, doi 10.1016/j.ejca.2025.115375. URL: https://doi.org/10.1016/j.ejca.2025.115375 — 任何等級 AE 99% vs 95%、G3/4 59% vs 48%；QoL 組間差異小於臨床意義門檻、12–18 個月內回復。Route: Europe PMC REST
- **[S29] PASS** — Lorusso D, Xiang Y, Hasegawa K, et al. (2024). *Pembrolizumab or placebo with chemoradiotherapy followed by pembrolizumab or placebo for newly diagnosed, high-risk, locally advanced cervical cancer (ENGOT-cx11/GOG-3047/KEYNOTE-A18): a randomised, double-blind, phase 3 clinical trial.* Lancet 403(10434):1341-1350. PMID 38521086, doi 10.1016/s0140-6736(24)00317-9. URL: https://doi.org/10.1016/s0140-6736(24)00317-9 — 1,060 人（FIGO 2014 IB2–IIB 淋巴結陽性或 III–IVA）；24 個月 PFS 68% vs 57%（HR 0.70，0.55–0.89，p=0.0020）；G3+ 75% vs 69%。Route: Europe PMC REST
- **[S30] PASS** — Lorusso D, Xiang Y, Hasegawa K, et al. (2024). *Pembrolizumab or placebo with chemoradiotherapy followed by pembrolizumab or placebo for newly diagnosed, high-risk, locally advanced cervical cancer (ENGOT-cx11/GOG-3047/KEYNOTE-A18): overall survival results from a randomised, double-blind, placebo-controlled, phase 3 trial.* Lancet 404(10460):1321-1332. PMID 39288779, doi 10.1016/s0140-6736(24)01808-7. URL: https://doi.org/10.1016/s0140-6736(24)01808-7 — 第二次期中：36 個月 OS 82.6% vs 74.8%、HR 0.67（0.50–0.90，p=0.0040）；G3+ 78% vs 70%；免疫相關 AE 39% vs 17%。Route: Europe PMC REST
- **[S31] PASS** — Penninx BMF, Samson MJ, Schnog JB. (2025). *Pembrolizumab with chemoradiotherapy followed by pembrolizumab for stage III-IVa cervical cancer: is the ENGOT-cx11/GOG-3047/KEYNOTE-A18 trial practice changing?* Cancer 131(4):e35749. PMID 39913282, doi 10.1002/cncr.35749. URL: https://doi.org/10.1002/cncr.35749 — 對照組惡化 193 人僅 51 人後續接受免疫治療；90 週療程長度與成本的具名質疑。Route: Europe PMC REST
- **[S32] PASS（僅用於 FDA 核准範圍與最終分析存在之背景事實）** — Brand-Wiita S, Tsai CJ, Liu YH, et al. (2026). *Cost-effectiveness of pembrolizumab as a treatment for FIGO 2014 stage III-IVA cervical cancer in the United States.* Gynecol Oncol 210:1-9. PMID 42150374, doi 10.1016/j.ygyno.2026.05.001. URL: https://doi.org/10.1016/j.ygyno.2026.05.001 — 「FDA approved pembrolizumab in combination with CRT for…FIGO 2014 Stage III-IVA cervical cancer in January 2024」；模型使用 KEYNOTE-A18 final analysis 的 patient-level data（該最終分析本身未見刊，見 [S46]）。Route: Europe PMC REST
- **[S33] PASS** — Smith ES, Moon AS, O'Hanlon R, et al. (2020). *Radical Trachelectomy for the Treatment of Early-Stage Cervical Cancer: A Systematic Review.* Obstet Gynecol 136(3):533-542. PMID 32769648, PMC7528402, doi 10.1097/aog.0000000000003952. URL: https://doi.org/10.1097/aog.0000000000003952 — 47 篇、2,566 人；9% 術中轉子宮切除；中位復發 3.3%；5 年 RFS 94.6%、OS 97.4%；懷孕率 23.9%、活產率 75.1%；證據層級限制原文。Route: Europe PMC REST
- **[S34] PASS** — Bentivegna E, Maulard A, Pautier P, Chargari C, Gouy S, Morice P. (2016). *Fertility results and pregnancy outcomes after conservative treatment of cervical cancer: a systematic review of the literature.* Fertil Steril 106(5):1195-1211.e5. PMID 27430207, doi 10.1016/j.fertnstert.2016.06.032. URL: https://doi.org/10.1016/j.fertnstert.2016.06.032 — 2,777 人／944 次懷孕；生育率 55%、活產 70%、**早產 38%**；PPROM 主因；小術式早產較低。Route: Europe PMC REST
- **[S35] PASS** — Bentivegna E, Gouy S, Maulard A, Chargari C, Leary A, Morice P. (2016). *Oncological outcomes after fertility-sparing surgery for cervical cancer: a systematic review.* Lancet Oncol 17(6):e240-e253. PMID 27299280, doi 10.1016/s1470-2045(16)30032-8. URL: https://doi.org/10.1016/s1470-2045(16)30032-8 — 適用限預後良好（IB <4 cm、淋巴結陰性、非侵襲性組織型態）；≤2 cm 與 LVSI 為選術式主軸；六種術式比較框架。Route: Europe PMC REST
- **[S36] PASS** — Teh WT, Stern C, Chander S, Hickey M. (2014). *The impact of uterine radiation on subsequent fertility and pregnancy outcomes.* Biomed Res Int 2014:482968. PMID 25165706, PMC4140124, doi 10.1155/2014/482968. URL: https://doi.org/10.1155/2014/482968 — 成人子宮 >45 Gy 建議告知避免嘗試懷孕；<4 Gy 未見損害；TBI 12 Gy 懷孕可能但併發症多。Route: Europe PMC REST
- **[S37] PASS** — Wo JY, Viswanathan AN. (2009). *Impact of radiotherapy on fertility, pregnancy, and neonatal outcomes in female cancer patients.* Int J Radiat Oncol Biol Phys 73(5):1304-1312. PMID 19306747, PMC2865903, doi 10.1016/j.ijrobp.2008.12.016. URL: https://doi.org/10.1016/j.ijrobp.2008.12.016 — 腹骨盆放療後子宮功能異常：流產、早產、低出生體重、胎盤異常；卵巢劑量與提早停經劑量依存。Route: Europe PMC REST
- **[S38] PASS** — Su HI, Lacchetti C, Letourneau J, et al. (2025). *Fertility Preservation in People With Cancer: ASCO Guideline Update.* J Clin Oncol 43(12):1488-1515. PMID 40106739, doi 10.1200/jco-24-02782. URL: https://doi.org/10.1200/jco-24-02782 — 「FP approaches should be discussed before cancer-directed therapy」；女性已確立方法含 embryo/oocyte/OTC、ovarian transposition、conservative gynecologic surgery；GnRHa 不可取代。（站上 insight-cervix-ovary 亦引同文。）Route: Europe PMC REST
- **[S39] PASS** — 衛生福利部中央健康保險署。《全民健康保險藥品給付規定》第 9 節 抗癌瘤藥物（115.8.21 更新版 PDF，2026-08-30 下載、pdftotext 後 grep）。URL: https://www.nhi.gov.tw/ch/dl-55685-99c675b771ab4b2789c891bc8db447ce-1.pdf — **9.37.4 bevacizumab 子宮頸癌條文原文**（與 cisplatin+paclitaxel 併用於持續性/復發性/轉移性；或與 paclitaxel+topotecan 用於不能含鉑者；事前審查、每次 15 週）；**9.2 carboplatin**「限 1.卵巢癌患者。2.腎功能不佳(CCr<60)…」；**9.69 免疫檢查點抑制劑條列適應症無子宮頸癌**（全檔「子宮頸」共 4 處：3 處在 9.37.4、1 處在 CAR-T 排除條件）；第 9 節無 cisplatin 專屬條文。Route: nhi.gov.tw 直接下載 → pdftotext → grep 原文
- **[S40] PASS** — 衛生福利部（2025）。〈114年起癌友生育保存補助 最高7萬元〉。URL: https://www.mohw.gov.tw/cp-16-83501-1.html — 原文：「醫療性生育保存補助試辦方案」114/9/1 起；對象「罹患乳癌或血液癌具我國國籍之18歲至40歲民眾」；女性取卵每次上限 7 萬、男性取精 8 千；一生至多 2 療程；限特約機構。（2026-08-30 curl 下載 grep 覆核，頁面仍在。）Route: curl（--cacert 代理憑證）→ grep 原文
- **[S41] FAIL（記錄為查證過的 gap）** — Pembrolizumab（或任何免疫檢查點抑制劑）用於子宮頸癌之健保給付條文。已檢索：藥品給付規定第 9 節全文（S39，9.69 逐條適應症、全檔「子宮頸」關鍵字）→ **零筆**。→ 文章寫「此適應症目前健保未給付、屬自費，費用向醫務課／個管師確認」；**D4（復發轉移之 KEYNOTE-826 情境）可直接重用此查證結果**
- **[S42] PASS** — 衛生福利部中央健康保險署。「醫療服務給付項目」檔（114.01.01 生效版 XLS，2026-08-30 下載、xlrd 逐列 grep）。URL: https://www.nhi.gov.tw/ch/dl-82687-cdc462f073354eeb894cfeef692ecb32-1.xls （來源頁 https://www.nhi.gov.tw/ch/cp-5943-f1cce-2821-1.html ）— 80413B Radical hysterectomy for cervical cancer 42,640 點；**80429B Laparoscopic radical hysterectomy for cervical cancer 48,183 點（項目仍存在）**；80412B Extended hysterectomy 28,841 點；**80211C Radical trachelectomy 42,638 點**；80210C Abdominal trachelectomy 13,871 點；80205C Cervical conization 2,810 點。臨床給付條件不在檔內。Route: curl 下載 XLS → xlrd 逐列 grep
- **[S43] FAIL** — ESMO 子宮頸癌現行指引之官方 landing page 內容。esmo.org 指引頁為 JS 渲染，curl 取得之 HTML 無正文可 grep；Europe PMC 可查得的最新 ESMO 子宮頸癌 CPG 為 2017 年版（Marth，PMID 28881916，**早於 LACC 與 KEYNOTE-A18**，不適合當現行標準引用）。→ B1/B2 的指引級敘述一律以 ESGO/ESTRO/ESP 2023 [S3] 為準
- **[S44] FAIL** — CO2 氣腹（pneumoperitoneum）促進子宮頸癌擴散之可引用臨床證據。Europe PMC 檢索（CO2/carbon dioxide × cervical × spillage/metastasis/mechanism 等組合）無相關臨床研究。→ 機制段 CO2 只能寫「假說」，不可引數字
- **[S45] FAIL** — 微創術後「以某時點無病為條件」的條件存活分析（conditional survival given disease-free at interval, MIS-specific）。Europe PMC 檢索零筆。→ 已開過微創者的段落改用 [S18]（復發時間分布）＋[S19]（一般族群條件存活，帶「非微創專屬」標籤）
- **[S46] FAIL** — KEYNOTE-A18 最終分析（final analysis）之同儕審查論文。截至 2026-08-30，Europe PMC 檢索（"KEYNOTE-A18" × Lorusso × 2025–2026；final analysis／third interim）僅得引用其 patient-level data 的成本效益論文 [S32]，主報告未見刊。→ OS 的可引用上限是第二次期中分析 [S30]；文章寫「最終分析尚未正式發表」
- **[S47] PASS** — Randall L, Xiang Y, Matsumoto T, et al. (2025). *Patient-reported outcomes from the phase 3, randomized, double-blind, placebo-controlled ENGOT-cx11/GOG-3047/KEYNOTE-A18 study of pembrolizumab plus concurrent chemoradiotherapy in participants with high-risk locally advanced cervical cancer.* Gynecol Oncol 199:88-95. PMID 40592026, doi 10.1016/j.ygyno.2025.06.003. URL: https://doi.org/10.1016/j.ygyno.2025.06.003 — 1,008/1,060 人納入 PRO 分析；QLQ-C30 GHS/QoL、physical functioning、QLQ-CX24 symptom experience、EQ-5D-5L VAS 皆無組間有意義差異。Route: Europe PMC REST
