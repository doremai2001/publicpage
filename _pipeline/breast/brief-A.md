# A 組研究簡報 — 乳癌專題（階段一：確診之後）

查證日期：**2026-08-27**。所有期刊來源均以 Europe PMC REST API
（`https://www.ebi.ac.uk/europepmc/webservices/rest/search`）逐條核對標題、期刊、卷、期、頁、年、DOI；
官方文件以 WebFetch / curl 實際取得並逐句抄錄。**只有標記 PASS 的來源可以被引用。**

**本簡報只提供 A1–A6 主場的材料。** 依 `breast/SPEC.md` 第三節與第六節，
以下內容**不在此簡報內**，A 組也不得自行補：多基因表現分析的任何分數或試驗數字（TAILORx、
RxPONDER、MINDACT → **B4**）、轉移性的標靶藥物資料（PARP／PIK3CA／ESR1／HER2-low 用藥 → **D5**）、
保留手術 vs 全乳切除的等效證據（**B1**）、前哨淋巴結（**B2**）、pCR 與殘餘病灶（**B3**）、
HER2 藥物排序（**B5**）、內分泌療程長度（**B6**）、放療分次與省略（**C1**、**C2**）、
急症警語總表（**C4**）、追蹤排程（**D1**）、跨項目自費決策（**D4**）。

**亞型標示是硬規則。** 本簡報每一個數字後面都寫了它出自哪一個亞型與哪一個族群；
沒有標族群的數字在乳癌專題裡等同於錯誤。

---

# A1 — 確診之後的第一個月會怎麼走

**Key facts**

- 粗針切片（core-needle biopsy）與開刀切片（open surgical biopsy）在區分良惡性上的準確度接近：
  立體定位真空輔助粗針切片與開刀切片準確度相當（證據強度被評為 low），超音波導引粗針切片也很準確；
  嚴重併發症的風險，粗針切片 <1%、開刀切片 2%–10%。以粗針切片確診的乳癌病人，
  比以開刀切片確診者更可能只需要一次手術（隨機效應勝算比 13.7，95% CI 5.5–34.6）。
  這是一份 AHRQ 委託、涵蓋 1990–2009 年文獻的系統性回顧，族群為「疑似乳癌的一般風險女性」，未分亞型。[S1]
- 新診斷乳癌做全身分期影像的產出很低：22 篇研究、14,824 名接受分期影像的乳癌病人（年齡中位數 53 歲），
  遠端轉移的**盛行率中位數為 7.0%（範圍 1.2%–48.8%），且隨期別上升；第一、二期的盛行率低，
  越晚期越高**。同一份回顧的敏感度／特異度中位數：合併常規影像 78.0%／91.4%、骨骼掃描 98.0%／93.5%、
  胸部 X 光 100%／97.9%、肝臟超音波 100%／96.7%、胸腹部電腦斷層 100%／93.1%、
  FDG-PET 100%／96.5%、FDG-PET/CT 100%／98.1%。作者自己註明 PET 類研究偵測到的無症狀轉移比例高，
  部分反映選樣偏差。**未分亞型。**[S2]
- 多專科團隊（MDT）與存活的關聯有一份大型自然實驗：蘇格蘭西部 13,722 名 1990–2000 年診斷的
  症狀性侵襲性乳癌女性。1995 年前，介入區（大格拉斯哥）的乳癌死亡率比非介入區高 11%
  （調整後 HR 1.11，95% CI 1.00–1.20）；1995 年 10 月導入多專科團隊之後，介入區反而低 18%
  （HR 0.82，95% CI 0.74–0.91），全死因死亡率低 11%（HR 0.89，95% CI 0.82–0.97）。
  這是回溯性、非隨機的介入型世代研究，**未分亞型**。[S3]
- 「從確診到手術要多久」有兩個大型資料庫的答案：SEER-Medicare 94,544 名 66 歲以上、
  1992–2009 年診斷的非發炎性非轉移性侵襲性乳癌病人，每往後一個時間區間（≤30、31–60、61–90、
  91–120、121–180 天）整體存活下降（HR 1.09，95% CI 1.06–1.13），第一期（HR 1.13，95% CI 1.08–1.18）
  與第二期（HR 1.06，95% CI 1.01–1.11）達顯著；乳癌專一死亡率每 60 天區間上升（sHR 1.26，95% CI 1.02–1.54）。
  NCDB 115,790 名 2003–2005 年診斷、18 歲以上病人，每一區間整體死亡 HR 1.10（95% CI 1.07–1.13），
  同樣只在第一期（HR 1.16）與第二期（HR 1.09）達顯著。**這是觀察性資料，未分亞型，
  作者明講「術前評估與重建考量本來就需要時間」。**[S4]
- ESMO 早期乳癌臨床指引現行版為 2024 年（Ann Oncol 35(2):159-182）。**注意：Europe PMC 沒有本文摘要，
  我沒有取得全文，因此只能引用「這份指引存在、版本為 2024 年」，不得引述其中任何條文。**[S10]

**Claim ceiling**

Defensible：「第一個月做的事情是把三件事釘死——組織診斷（粗針切片，不是先開刀）、受體與 HER2 的判讀、
以及期別。全身分期影像不是每個人都要做：早期乳癌找到無症狀遠端轉移的機率低，
指引普遍不建議常規做，這一點在門診值得直接問出口。多專科團隊的討論不是行政流程，
有大型世代資料顯示它與存活相關。從確診到手術的等待時間，和存活有統計上的關聯，但需要的評估時間也是真的。」

Would overstate：
- 「早期乳癌不需要做任何分期檢查」——[S2] 說的是**盛行率低、指引不建議常規做**，不是「不必做」；
  有症狀或期別較高時另當別論。
- 「多專科團隊會讓存活率提高 18%」——[S3] 是回溯性非隨機比較，而且 0.82 是**風險比**不是存活率差；
  必須寫成「與較低的乳癌死亡率有關聯」。
- 「拖越久越危險，所以要立刻開刀」——[S4] 是觀察性資料，作者自己說術前評估與重建考量需要時間；
  不可以把它寫成催促病人跳過評估。
- 「粗針切片一定不會錯」——[S1] 的證據強度被作者評為 low，而且準確度不是 100%。

**Caveats / safety notes**

- 最危險的誤讀是「醫師沒幫我做全身檢查，是不是不夠仔細」。要把 [S2] 的邏輯講清楚：
  早期做全身影像，找到真東西的機率低、找到假陽性再去追一輪的機率不低，而追那一輪要花的時間
  正好是 [S4] 在談的時間。
- 第二個危險誤讀是「先開刀拿下來化驗比較準」。[S1] 的重點是粗針切片準確度接近、併發症明顯較低，
  而且**先有完整的粗針切片報告，才有可能討論術前治療與手術範圍**。
- 不要把「時間與存活有關聯」寫成「每拖一天就少一分存活」。[S4] 的區間是 30 天級距，不是天數線性關係。
- **術前 MRI 的爭議屬 A5 主場**，A1 只寫「排程上可能會多一個檢查」，不展開。
- **生殖系 BRCA 檢測要在手術前談**（固定紅線 B）→ 一句話帶過並指向 A6。
- 男性乳癌、懷孕期乳癌不在本專題；碰到寫一句帶過。

**Taiwan status**

- **重大傷病證明（已查到正式條文）**：依《全民健康保險保險對象免自行負擔費用辦法》第二條附表一
  「全民健康保險重大傷病項目及其證明有效期限」（114 年 1 月 1 日以後適用），
  重大傷病第一項為「需積極或長期治療之癌症」，其中
  **「(三)乳房惡性腫瘤第一期」（ICD-10-CM C50.011–C50.929）證明有效期限為「三年」；
  「(五)除(一)-(四)之其他惡性腫瘤」（C00.0–C96.9）有效期限為「五年」**。
  也就是說，**第一期乳癌是三年，第二期以上走「其他惡性腫瘤」的五年**。[S5]
- **申請與生效**：可郵寄、親自到分區業務組送件，或由醫院診所透過健保資訊網服務系統（VPN）代送。
  法源為《全民健康保險法》第 48 條與上述辦法。**生效日期為「保險人受理日期」**；
  住院期間提出申請者，自當次住院第一日起免自行負擔；若以住院期間檢驗報告在出院後才確定診斷，
  施行該確定診斷檢驗之當次住院及出院後之相關門診亦免自行負擔。展延申請時程依效期長短規定
  （二年以上者於效期屆滿前三個月、一年或六個月者於屆滿前一個月、三個月以下者於屆滿前 14 日）。
  **健保署頁面上沒有寫「幾個工作天內核定」，這一項是 gap**，文章要寫「核定要多久請跟個管師或
  醫院醫務課確認」。[S6]
- **診斷影像的健保給付（已查到支付標準條文）**：
  「33145B 診斷性乳房攝影（Diagnostic Mammography）」適應症為乳房攝影報告 BIRADS 0、3、4、5，
  且同時符合「乳房診斷性影像發現微鈣化／鈣化」或「乳房攝影影像發現不對稱、結構扭曲及腫塊」之一；
  限放射診斷科專科醫師執行；**每人每年限執行二次**。
  「19014C 乳房超音波」為給付項目。
  「12195B 第二型人類表皮生長因子受體(Her-2/neu)原位雜合檢驗（ISH）」限 HER2 IHC score 為 2+ 的乳癌使用，
  且明訂「本法為 IHC 染色結果之輔助檢查方法，不可單獨使用」。
  「25012B 免疫組織化學染色（每一抗體）」每例以五種抗體為限，雙側乳癌病理檢體放寬到十種。[S7]
- **乳癌照護品質提升方案（2026 年）**：健保署 115 年 2 月 13 日新聞稿說明，
  自 113 年 11 月成立乳癌專家小組研議，方案涵蓋**所有期別新診斷及首次復發的乳癌個案（含男性）**，
  目標納入全國 80% 新確診病人；由乳房外科、放射診斷科醫師及個案管理師組成診療團隊，
  提供單一窗口諮詢及護理指導；核發「新收個案整合照護」獎勵，以及每年一次的「追蹤照護」獎勵
  （追蹤至滿五年且無病狀態）；挹注約新臺幣 4,000 萬元。**這是 A1「台灣行政現實」段落的骨幹：
  台灣的乳癌病人有個管師這個窗口，是有給付設計在後面撐的。**[S8]
- **台灣的流行病學**：衛福部公布 111 年癌症登記資料，女性乳房癌新診斷 17,366 人，
  標準化發生率每十萬女性人口 92.0 人（110 年為 82.5），**診斷年齡中位數 57 歲**，
  為女性癌症發生第 3 位；112 年資料的女性乳癌在全癌症新發生人數排名第 3、
  女性標準化發生率排名第 1，發生年齡中位數 57 歲，比全癌症中位數 65 歲早 8 歲。[S9][S11]
- **gap（查不到正式文件，文章一律寫成「要跟你的個管師或醫院醫務課確認」）**：
  ①重大傷病申請的**核定工作天數**；②**乳房磁振造影**在乳癌診斷／分期情境的健保給付條文
  （支付標準內沒有乳房專屬的 MRI 項目名稱可對應）；③PET/CT 用於乳癌初次分期的給付條件；
  ④國健署癌症登記報告的乳癌**期別分布**原始檔（`www.hpa.gov.tw` 在本環境 TLS 驗證失敗，無法取得）。

**Sources**

- **[S1] PASS** — Bruening W, Fontanarosa J, Tipton K, et al. (2010). *Systematic review: comparative effectiveness of core-needle and open surgical biopsy to diagnose breast lesions.* Ann Intern Med 152(4):238-246. PMID 20008742, doi 10.7326/0003-4819-152-1-201001050-00190 — 建立粗針切片 vs 開刀切片的準確度、併發症率與「一次手術完成」的勝算比。Route: Europe PMC REST (EXT_ID). URL: https://doi.org/10.7326/0003-4819-152-1-201001050-00190
- **[S2] PASS** — Brennan ME, Houssami N. (2012). *Evaluation of the evidence on staging imaging for detection of asymptomatic distant metastases in newly diagnosed breast cancer.* Breast 21(2):112-123. PMID 22094116, doi 10.1016/j.breast.2011.10.005 — 建立「早期乳癌全身分期影像產出低、盛行率隨期別上升」與各項影像的敏感度/特異度。Route: Europe PMC REST (title+author). URL: https://doi.org/10.1016/j.breast.2011.10.005
- **[S3] PASS** — Kesson EM, Allardice GM, George WD, Burns HJ, Morrison DS. (2012). *Effects of multidisciplinary team working on breast cancer survival: retrospective, comparative, interventional cohort study of 13 722 women.* BMJ 344:e2718. PMID 22539013, doi 10.1136/bmj.e2718 — 建立多專科團隊導入與乳癌死亡率下降的關聯。開放取用。Route: Europe PMC REST (AUTH). URL: https://doi.org/10.1136/bmj.e2718
- **[S4] PASS** — Bleicher RJ, Ruth K, Sigurdson ER, et al. (2016). *Time to Surgery and Breast Cancer Survival in the United States.* JAMA Oncol 2(3):330-339. PMID 26659430, doi 10.1001/jamaoncol.2015.4508 — 建立確診到手術的時間與存活的關聯（兩個獨立資料庫）。Route: Europe PMC REST (AUTH+TITLE). URL: https://doi.org/10.1001/jamaoncol.2015.4508
- **[S5] PASS** — 衛生福利部中央健康保險署。《全民健康保險保險對象免自行負擔費用辦法》第二條附表一
  「全民健康保險重大傷病項目及其證明有效期限」（114 年 1 月 1 日以後適用，113 年 9 月 16 日修訂）。
  PDF 實際下載並逐字核對：乳房惡性腫瘤第一期三年、其他惡性腫瘤五年。Route: curl（HTTP 200，466,471 bytes）+ pdftotext。
  URL（頁面）: https://www.nhi.gov.tw/ch/cp-6086-caf5f-2957-1.html
  URL（PDF）: https://www.nhi.gov.tw/ch/dl-74911-9ea79f859a24431497ef0304ce4b7981-1.pdf
- **[S6] PASS** — 衛生福利部中央健康保險署。〈法令規定與免自行負擔費用範圍〉／〈申請須知及文件下載〉。
  建立法源（全民健康保險法第 48 條）、免自行負擔範圍四款、生效日為保險人受理日、住院期間申請的起算、
  以及展延申請的時程。Route: WebFetch。
  URL: https://www.nhi.gov.tw/ch/cp-6089-0c619-2957-1.html ；https://www.nhi.gov.tw/ch/cp-6091-08ad9-2957-1.html
- **[S7] PASS** — 衛生福利部中央健康保險署。《全民健康保險醫療服務給付項目及支付標準》
  （115.08.01 生效版）診療項目 33145B、19014C、12195B、25012B、33125C 條文與支付規範。
  Route: 支付標準全文檔逐項比對（項目代碼、生效日、支付規範欄位）。
  URL: https://www.nhi.gov.tw/ch/lp-3778-1.html
- **[S8] PASS** — 衛生福利部中央健康保險署（115 年 2 月 13 日）。〈健保啟動乳癌照護品質提升方案 守護國人健康新里程〉。
  建立方案涵蓋對象、團隊組成、個管師角色、獎勵項目與五年追蹤、預算金額。Route: WebFetch。
  URL: https://www.nhi.gov.tw/ch/cp-19662-fec7d-3255-1.html
- **[S9] PASS** — 衛生福利部。〈公布 111 年國人癌症登記資料分析結果 五癌篩檢為健康加值〉。
  女性乳房癌 17,366 人、標準化發生率 92.0／十萬、診斷年齡中位數 57 歲、發生第 3 位。Route: WebFetch。
  URL: https://www.mohw.gov.tw/cp-2704-80902-1.html
- **[S10] PASS（僅書目，內容未取得）** — Loibl S, André F, Bachelot T, et al. (2024).
  *Early breast cancer: ESMO Clinical Practice Guideline for diagnosis, treatment and follow-up.*
  Ann Oncol 35(2):159-182. PMID 38101773, doi 10.1016/j.annonc.2023.11.016。
  **Europe PMC 無摘要、全文未取得。只能引用「現行版為 2024 年」，不得引述任何條文內容。**
  Route: Europe PMC REST (TITLE)。URL: https://doi.org/10.1016/j.annonc.2023.11.016
- **[S11] PASS** — 衛生福利部。〈公布 112 年國人癌症登記資料分析結果 守護健康未來 從癌症篩檢開始〉。
  女性乳癌全癌症新發生人數第 3 位、女性標準化發生率第 1 位、發生年齡中位數 57 歲（全癌症 65 歲）。Route: WebFetch。
  URL: https://www.mohw.gov.tw/cp-7171-84987-1.html

---

# A2 — ER、PR、HER2 在報告上說了什麼

**Key facts**

- **ER／PR 判讀的現行標準（ASCO/CAP 2020）**：ER 以經確效的免疫組織化學染色（IHC）判讀，
  是預測誰能從內分泌治療獲益的標準方法，**沒有其他檢驗被建議用於這個目的**；
  **腫瘤細胞核 1%–100% 陽性判為 ER 陽性**；**<1% 或 0% 判為 ER 陰性**。
  指引明白承認「1%–10% 染色的癌症，內分泌治療獲益的資料有限」，因此**另設一個新的報告分類
  「ER Low Positive」並附建議註記**。0%–10% 染色的案例必須報告對照組（controls）狀態，
  實驗室要有標準作業程序去確認／裁決這類結果。PR 主要用於 ER 陽性癌症的預後判斷。
  原位癌（DCIS）建議測 ER 以評估降低未來乳癌風險的內分泌治療效益，測 PR 為選項。[S13]
- **ER 1%–9% 的分子本質**：465 例原發乳癌，以 IHC 與 Affymetrix U133A 基因晶片比對。
  ER 陰性、1%–9%（n=25）、10%（n=6）、>10%（n=251）四組中，
  **ESR1 mRNA 陽性的比例分別為 24%、67%、92%（1%–9% 組只有 24%）**；
  1%–9% 組的 ER 相關基因表現分數與 ER 陰性組相近，顯著低於 ≥10% 組；
  **1%–9% 組中 48% 屬 basal-like、只有 8% 屬 luminal B**；整體存活介於 ≥10% ER 陽性與 ER 陰性之間。
  作者結論：多數 1%–9% ER 陽性腫瘤的分子特徵像 ER 陰性、basal-like。[S14]
- **ER-low 的臨床行為（HR 亞型內部差異）**：韓國單一機構 5,930 名接受根治手術的侵襲性乳癌
  （中位追蹤 80.9 個月），**ER-low（1%–10%，以 Allred proportion score 定義）只佔 2.0%（117 人）**，
  其中 53.8% 為 HER2 陰性、46.2% 為 HER2 陽性。
  五年無病存活／總存活：**ER-high/HER2− 94.0%／98.6%（最好）；ER-low/HER2− 85.7%／92.1%；
  三陰性 81.3%／90.1%（最差）**。作者結論：ER-low/HER2− 的臨床病理特徵、治療與結果與三陰性相近。[S15]
- **ER-low 仍不該把內分泌治療當成沒用**：美國國家癌症資料庫（NCDB）7,018 名第 I–III 期、
  ER 1%–10%、且接受（前導性或輔助性）化療的高風險病人，中位追蹤 3 年、586 例死亡。
  **12 個月時有 42% 沒有開始內分泌治療**；多變量分析中省略內分泌治療與較高死亡風險相關
  （HR 1.23，95% CI 1.04–1.46，P=.02），且 ER 6%–10% 者影響較大（HR 1.42，95% CI 1.00–2.02，P=.048），
  ER 1%–5% 者未達顯著（HR 1.15，95% CI 0.91–1.45，P=.24）。
  前導性化療後**有殘餘病灶者**省略內分泌治療與較差總存活相關（HR 1.26，95% CI 1.00–1.57，P=.046），
  達病理完全緩解者則否（HR 1.06，95% CI 0.62–1.80，P=.84）。這是觀察性資料。[S16]
- **HER2 判讀的現行標準（ASCO/CAP 2018，2023 年更新確認沿用）**：
  IHC 2+ 定義為侵襲性乳癌有 >10% 腫瘤細胞呈現弱到中度的完整細胞膜染色。
  若粗針切片的初次 HER2 結果為陰性，依特定臨床條件**「可以（may）」而非「必須（must）」**
  在手術檢體上重做一次 HER2。
  雙探針 ISH 的少見型態（約佔 5% 的案例）另立處理流程：
  **ISH group 2**（HER2/CEP17 比值 ≥2.0、平均 HER2 拷貝數 <4.0／細胞）、
  **ISH group 3**（比值 <2.0、平均拷貝數 ≥6.0）、
  **ISH group 4**（比值 <2.0、平均拷貝數 ≥4.0 且 <6.0）；
  **group 2–4 都必須同時回看 IHC**，才能得到「陽性或陰性」的最終判定；
  使用單探針 ISH 的實驗室，所有結果都必須併同 IHC 判讀。[S17]
- **2023 年的 ASCO-CAP 更新做了什麼、沒做什麼**：系統性回顧檢出 173 篇摘要、審閱 5 篇，
  **沒有任何一篇構成修改建議的訊號，因此 2018 年的建議「予以確認（affirmed）」**。
  更新承認 trastuzumab deruxtecan 在 HER2 未過度表現／未擴增但 IHC 1+ 或 IHC 2+/ISH 未擴增的腫瘤有新適應症；
  但明講 **「現在就建立 HER2-Low、HER2-Ultra-Low 這類新的結果分類還太早（premature）」**，
  也明講目前資料不支持 IHC 0 vs 1+ 是新的預後或預測門檻——只是因為試驗納入條件而變得臨床相關。
  更新新增的是一段**報告註記**，提醒 IHC 0 與 1+ 的區分現在有臨床意義，並給出區分兩者的最佳實務建議。[S18]
  **→ 這一點直接修正了「2026 年 ASCO/CAP 已經有 HER2-low／ultralow 報告分類」的假設：沒有。
  現行版仍是 ER/PR 2020 與 HER2 2018（2023 確認）。**[S19]
- **IHC 0 與 1+ 分不清楚，是有量化證據的**：CAP 能力試驗調查（1,391–1,452 個實驗室、
  每個實驗室每年判讀 40 個 HER2 core、兩年共 80 個）顯示，**19% 的案例在 IHC 0 vs 1+ 上
  實驗室間一致性 ≤70%**；耶魯的研究讓 18 位病理醫師以四分法判讀 170 個乳癌切片，
  **0 與 1+ 之間的一致性只有 26%，而 2+ 與 3+ 之間是 58%**。作者結論：低區間（0 與 1+）的判讀準確度差。[S20]
- **Ki-67 的立場（國際 Ki67 工作小組 IKWG 2021 共識）**：
  Ki-67 IHC「因為分析效度可疑，對治療決策的價值有限」。共識為：
  ①前分析處理與 ER、HER2 一樣關鍵；②已建立標準化的目視計分方法並建議採用；
  ③應參加並評估品保／品管方案以維持分析效度；
  ④**IKWG 接受 Ki-67 IHC 作為預後標記有臨床效度，但結論是「臨床實用性只明確存在於
  解剖上條件良好的 ER 陽性、HER2 陰性病人，用來辨認不需要輔助化療的人」**。
  在 **T1-2、N0-1** 這一族群，共識是 **Ki-67 ≤5% 或 ≥30% 可用來估計預後**（言下之意：中間地帶無法）。
  結語再寫一次：目前 Ki-67 IHC 在乳癌照護中的臨床實用性仍侷限於第一、二期的預後評估。[S21]
- **Ki-67 的實驗室間變異有量化證據**：30 家歐洲病理實驗室以各自的院內流程染同一套組織微陣列，
  70 個配對樣本由一位觀察者中央判讀。**各實驗室 Ki-67 標記指數中位數從 0.65% 到 33.0%（P<0.0001）；
  同一批腫瘤被分類為 luminal A 的比例從 17% 到 57%（P<0.0001）**。
  即使只分析使用相同抗體（MIB-1、SP6 或 30-9）的實驗室，或排除未參加外部品保方案的實驗室，
  差異依然顯著。作者結論：使用 Ki-67 做治療決策時必須充分知道該實驗室的參考值。[S22]
- **組織分級（grade）的原始依據**：Nottingham/Tenovus 研究把 Bloom-Richardson 法改良為
  半定量評估三項形態特徵——**腺管形成的百分比、細胞核多形性程度、以定義視野面積計算的有絲分裂數**，
  三項各自評分後加總得出分級，分三級。1973 年起收案 2,200 名以上原發可手術乳癌病人，
  其中 1,831 人可評分級：**第一級的存活顯著優於第二、三級（P<0.0001）**。
  分級與腫瘤大小、淋巴結期別共同組成 Nottingham 預後指數。[S23]
- **報告格式已經國際統一化**：ICCR（International Collaboration on Cancer Reporting）已產出
  國際通用的乳癌病理報告資料集（含侵襲癌與 DCIS 的切除檢體），區分 core（必填）與 noncore（選填）欄位，
  每個欄位附說明解釋為何納入、臨床相關性、以及證據不足或有爭議之處。
  該文以**組織分級、腫瘤大小、雌激素受體狀態**三項作為示範。開放取用。[S24]
- **各亞型的盛行率（美國 SEER，2010 年起登記 HER2）**：在有 HR/HER2 狀態的病人中，
  **HR+/HER2− 佔 72.7%（36,810 人）、三陰性（HR−/HER2−）佔 12.2%（6,193 人）、
  HR+/HER2+ 佔 10.3%（5,240 人）、HR−/HER2+ 佔 4.6%（2,328 人）**；另有 12%（6,912 人）狀態不明。
  非西班牙裔白人女性 HR+/HER2− 發生率最高，非西班牙裔黑人女性三陰性發生率最高。
  三陰性、HR+/HER2+、HR−/HER2+ 相較 HR+/HER2−，出現高分級疾病的可能性高 6.4 到 20.0 倍。[S25]

**Claim ceiling**

Defensible：「這份報告上真正會改變治療的是 ER、PR、HER2 三行，加上分級與大小。
ER 只要 1% 就算陽性，但 1%–10% 這一段指引自己標成『ER Low Positive』並承認資料有限——
它的分子特徵多數更像 ER 陰性，可是省掉內分泌治療在觀察性資料裡對應到較差的存活，
所以這一段是要拿去門診談、不是自己下結論的。HER2 的判讀有一套明確流程，
IHC 2+ 一定要加做 ISH，少數 ISH 型態還必須回頭配 IHC 一起看，
所以『HER2 要等比較久』或『HER2 要再驗一次』通常是流程正常，不是出了錯。
Ki-67 的實驗室間差異大到會改變亞型分類，工作小組自己說它的臨床用途很窄。」

Would overstate：
- 「ER 1% 跟 ER 90% 意義一樣」——[S13][S14][S15] 都反對這句。
- 「ER-low 就等於三陰性，可以不用吃抗荷爾蒙藥」——**這是本篇最危險的誤讀**。[S15] 說結果相近，
  但 [S16] 顯示省略內分泌治療與較差存活相關。兩件事要寫在同一段。
- 「2026 年 ASCO/CAP 已經有 HER2-low 或 HER2-ultralow 這個正式分類」——**沒有**。[S18] 明講太早。
- 「Ki-67 高就要化療、低就不用化療」——[S21] 只支持在 T1-2 N0-1 的 ER+/HER2− 族群用 ≤5% 或 ≥30% 估計預後。
- 「不同醫院的 Ki-67 可以互相比較」——[S22] 直接反駁。
- 「HER2 要重驗代表第一次驗錯了」——[S17] 寫的是 may，不是 must，而且是流程設計。

**Caveats / safety notes**

- 這一篇最容易被 ER-low 的病人讀成「我不用吃藥」。必須把 [S15] 與 [S16] 放在同一段，
  並明講這是觀察性資料、目前**沒有前瞻性試驗**回答這題。
- 不可以把 Ki-67 講成「腫瘤活躍度分數」然後給一個門檻。[S22] 的 0.65%–33.0% 是同一批腫瘤。
- HER2 IHC 0 與 1+ 的區分不可靠（[S20]），但**本篇不得延伸到 T-DXd 的用藥**——那是 D5 主場，
  這裡只寫「這條界線現在為什麼被重新在意，細節看 D5」。
- **多基因表現分析的分數與試驗數字一律不寫**（B4 主場）。A2 只解釋受體與分級這幾行。
- 亞型盛行率一律標明來源族群為美國 SEER（[S25]），不可寫成台灣的比例。

**Taiwan status**

- HER2 ISH（12195B）在健保支付標準中明訂**限 HER2 IHC score 為 2+ 的乳癌使用，且不可單獨使用**；
  IHC 染色（25012B）每例以五種抗體為限、雙側乳癌檢體放寬至十種。[S7]
- **gap**：ER/PR/HER2 判讀**報告的作業時效**（例如幾個工作天出報告）在健保或衛福部文件中查不到規範，
  文章要寫成「報告要等多久、要不要加做，請跟你的個管師確認」。
- **gap**：台灣本地的三種亞型盛行率，我沒有查到可引用的官方或期刊來源；
  文章中的亞型比例一律標明「美國 SEER 資料」，不得寫成台灣數字。

**Sources**

- **[S13] PASS** — Allison KH, Hammond MEH, Dowsett M, et al. (2020). *Estrogen and Progesterone Receptor Testing in Breast Cancer: ASCO/CAP Guideline Update.* J Clin Oncol 38(12):1346-1366. PMID 31928404, doi 10.1200/JCO.19.02309 — 建立 ER 1% 門檻、ER Low Positive 分類、對照組報告要求與 DCIS 的建議。Route: Europe PMC REST (EXT_ID)。URL: https://doi.org/10.1200/JCO.19.02309
- **[S14] PASS** — Iwamoto T, Booser D, Valero V, et al. (2012). *Estrogen receptor (ER) mRNA and ER-related gene expression in breast cancers that are 1% to 10% ER-positive by immunohistochemistry.* J Clin Oncol 30(7):729-734. PMID 22291085, doi 10.1200/JCO.2011.36.2574 — 建立 1%–9% ER 陽性的分子本質多數像 ER 陰性/basal-like。Route: Europe PMC REST (TITLE)。URL: https://doi.org/10.1200/JCO.2011.36.2574
- **[S15] PASS** — Park YH, Karantza V, Calhoun SR, et al. (2021). *Prevalence, treatment patterns, and prognosis of low estrogen receptor-positive (1% to 10%) breast cancer: a single institution's experience in Korea.* Breast Cancer Res Treat 189(3):653-663. PMID 34487293, doi 10.1007/s10549-021-06309-1 — 建立 ER-low 的盛行率（2.0%）與五年 DFS/OS 分層數字。Route: Europe PMC REST (TITLE)。URL: https://doi.org/10.1007/s10549-021-06309-1
- **[S16] PASS** — Choong GM, Hoskin TL, Boughey JC, Ingle JN, Goetz MP. (2025). *Endocrine Therapy Omission in Estrogen Receptor-Low (1%-10%) Early-Stage Breast Cancer.* J Clin Oncol 43(16):1875-1885. PMID 40215443, doi 10.1200/JCO-24-02263 — 建立 ER-low 省略內分泌治療與較差總存活的關聯（NCDB 觀察性）。Route: Europe PMC REST (TITLE)。URL: https://doi.org/10.1200/JCO-24-02263
- **[S17] PASS** — Wolff AC, Hammond MEH, Allison KH, et al. (2018). *Human Epidermal Growth Factor Receptor 2 Testing in Breast Cancer: ASCO/CAP Clinical Practice Guideline Focused Update.* J Clin Oncol 36(20):2105-2122. PMID 29846122, doi 10.1200/JCO.2018.77.8738 — 建立 IHC 2+ 定義、重驗的 may/must 用語、ISH group 2/3/4 的處理流程與必須併看 IHC。Route: Europe PMC REST (EXT_ID)。URL: https://doi.org/10.1200/JCO.2018.77.8738
- **[S18] PASS** — Wolff AC, Somerfield MR, Dowsett M, et al. (2023). *Human Epidermal Growth Factor Receptor 2 Testing in Breast Cancer: ASCO-College of American Pathologists Guideline Update.* J Clin Oncol 41(22):3867-3872. PMID 37284804, doi 10.1200/JCO.22.02864 — 建立「2018 建議予以確認」「建立 HER2-Low／Ultra-Low 分類為時過早」「新增 IHC 0 vs 1+ 的報告註記」。Route: Europe PMC REST (TITLE)。URL: https://doi.org/10.1200/JCO.22.02864
  （同內容之 Arch Pathol Lab Med 版：Wolff AC, et al. 2023;147(9):993-1000, PMID 37303228, doi 10.5858/arpa.2023-0950-SA）
- **[S19] PASS** — College of American Pathologists。〈Current CAP Guidelines〉頁面（2026-08-27 取得）。
  現行乳癌相關指引列為「HER2 Testing in Breast Cancer – 2023 Guideline Update」與
  「Immunohistochemical Testing of Estrogen and Progesterone Receptors in Breast Cancer – Update」；
  **頁面上沒有 2025 或 2026 年的新版**。用於佐證「2026 年的現行版本就是這兩份」。Route: WebFetch。
  URL: https://www.cap.org/protocols-and-guidelines/cap-guidelines/current-cap-guidelines
- **[S20] PASS** — Fernandez AI, Liu M, Bellizzi A, et al. (2022). *Examination of Low ERBB2 Protein Expression in Breast Cancer Tissue.* JAMA Oncol 8(4):1-4. PMID 35113160, doi 10.1001/jamaoncol.2021.7239 — 建立 IHC 0 vs 1+ 判讀一致性差（CAP 調查 19% 案例 ≤70% 一致；18 位病理醫師 0 vs 1+ 僅 26% 一致，2+ vs 3+ 為 58%）。Route: Europe PMC REST (AUTH+TITLE)。URL: https://doi.org/10.1001/jamaoncol.2021.7239
- **[S21] PASS** — Nielsen TO, Leung SCY, Rimm DL, et al. (2021). *Assessment of Ki67 in Breast Cancer: Updated Recommendations From the International Ki67 in Breast Cancer Working Group.* J Natl Cancer Inst 113(7):808-819. PMID 33369635, PMC8487652（開放取用）, doi 10.1093/jnci/djaa201 — 建立 Ki-67 的臨床實用性僅限 ER+/HER2−、T1-2 N0-1 的預後估計，且門檻為 ≤5% 或 ≥30%。Route: Europe PMC REST (EXT_ID)。URL: https://doi.org/10.1093/jnci/djaa201
- **[S22] PASS** — Focke CM, Bürger H, van Diest PJ, et al. (2017). *Interlaboratory variability of Ki67 staining in breast cancer.* Eur J Cancer 84:219-227. PMID 28829990, doi 10.1016/j.ejca.2017.07.041 — 建立 30 家實驗室的 Ki-67 中位數 0.65%–33.0%、luminal A 分類比例 17%–57%。Route: Europe PMC REST (TITLE)。URL: https://doi.org/10.1016/j.ejca.2017.07.041
- **[S23] PASS** — Elston CW, Ellis IO. (1991). *Pathological prognostic factors in breast cancer. I. The value of histological grade in breast cancer: experience from a large study with long-term follow-up.* Histopathology 19(5):403-410. PMID 1757079, doi 10.1111/j.1365-2559.1991.tb00229.x — 建立分級的三項組成與第一級存活顯著較佳（n=1,831，P<0.0001）。Route: Europe PMC REST (AUTH+TITLE)。URL: https://doi.org/10.1111/j.1365-2559.1991.tb00229.x
- **[S24] PASS** — Ellis IO, Rakha EA, Tse GM, Tan PH. (2023). *An international unified approach to reporting and grading invasive breast cancer. An overview of the International Collaboration on Cancer Reporting (ICCR) initiative.* Histopathology 82(1):189-197. PMID 36482273（開放取用）, doi 10.1111/his.14802 — 建立乳癌病理報告的 core/noncore 欄位架構與國際統一化。Route: Europe PMC REST (AUTH+TITLE)。URL: https://doi.org/10.1111/his.14802
- **[S25] PASS** — Howlader N, Altekruse SF, Li CI, et al. (2014). *US incidence of breast cancer subtypes defined by joint hormone receptor and HER2 status.* J Natl Cancer Inst 106(5):dju055. PMID 24777111, doi 10.1093/jnci/dju055 — 建立四個亞型的盛行率與分母（美國 SEER，涵蓋約 28% 美國人口）。Route: Europe PMC REST (AUTH+TITLE)。URL: https://doi.org/10.1093/jnci/dju055

---

# A3 — 三種乳癌，三條不一樣的路

**Key facts**

- **盛行率（美國 SEER，2010 年起）**：HR+/HER2− 72.7%、三陰性 12.2%、HR+/HER2+ 10.3%、HR−/HER2+ 4.6%
  （在 HR/HER2 狀態已知者中；另有 12% 狀態不明）。**HER2 陽性合計約 14.9%。**[S25]
- **依亞型的乳癌專一存活（美國 SEER，2010–2013 年診斷、追蹤至 2014 年底，四年）**：
  **HR+/HER2− 92.5%（最佳）、HR+/HER2+ 90.3%、HR−/HER2+ 82.7%、三陰性 77.0%（最差）**。
  作者以多重插補處理受體狀態不明者，並指出**不做插補會高估存活**，因為狀態不明者的預後特徵較差。
  依期別差異極大；**在初診即為第四期者，HR+/HER2+ 的存活（45.5%）優於 HR+/HER2−（35.9%）**，
  作者歸因於 HER2 標靶治療的進展。[S26]
- **復發風險曲線的形狀，三種亞型不一樣——這是本篇最有用的一段。**
  ①**ER 陽性 vs ER 陰性的長期對照（IBCSG I–V 試驗，4,105 名 1978–1985 年隨機分派的可手術乳癌病人，
  中位追蹤 24 年）**：全體的年化復發風險在頭五年最高（10.4%），**第 1–2 年之間達到高峰（15.2%）**。
  頭五年，ER 陽性的年化風險低於 ER 陰性（9.9% vs 11.5%，P=.01）；
  **五年之後反過來——5–10 年 5.4% vs 3.3%、10–15 年 2.9% vs 1.3%、15–20 年 2.8% vs 1.2%、
  20–25 年 1.3% vs 1.4%（P<.001）**。
  ER 陽性即使腋下淋巴結陰性，10–15、15–20、20–25 年的年化風險仍為 2.0%、2.1%、1.1%；
  1–3 顆淋巴結陽性者為 3.0%、3.5%、1.5%。[S27]
- ②**三陰性的早期高峰**：多倫多 Women's College Hospital 1987–1997 年診斷的 1,601 名乳癌病人，
  中位追蹤 8.1 年，**其中 180 人（11.2%）為三陰性**。三陰性在**診斷後五年內**遠端復發
  （HR 2.6，95% CI 2.0–3.5，P<0.0001）與死亡（HR 3.2，95% CI 2.3–4.5，P<0.001）的風險較高，
  **五年之後則否**；**遠端復發風險在大約第 3 年達到高峰、隨後迅速下降**，
  而「其他」組的復發風險在追蹤期內大致恆定。作者結論：三陰性的病程較侵襲，但這個不利影響是暫時的。[S28]
- ③**四種內在亞型各自的曲線形狀**：1,249 名早期乳癌、統一處置的世代，以組織微陣列判定 ER、PR、
  Ki-67、HER2、EGFR、CK5/6。**Luminal A**（ER+/PR+、HER2−、Ki-67 <14）風險緩慢上升，
  約三年達最大值後維持平穩；**Luminal B**（同上但 Ki-67 ≥14）多數復發發生在前五年；
  **HER2-enriched** 在術後約 20 個月出現高峰（Ki-67 ≥14 者風險較大），
  但在第 72 個月出現第二個高峰（此時 Ki-67 <14 者風險反而較大）；
  **三陰性**在 Ki-67 低者呈平緩曲線，Ki-67 ≥14 者則在約 18 個月出現尖銳高峰。[S29]
- ④**ER 陽性停藥後的 20 年絕對風險（EBCTCG，88 個試驗、62,923 名 ER 陽性、完成五年內分泌治療
  且五年時無病的女性）**：5 至 20 年間復發以穩定速率持續發生。**遠端復發的絕對風險
  ——T1N0 13%、T1N1-3 20%、T1N4-9 34%、T2N0 19%、T2N1-3 26%、T2N4-9 41%**。
  在給定 TN 狀態後，分級（43,590 人有資料）與 Ki-67（7,692 人）只有中等的獨立預測價值，
  **PR 狀態（54,115 人）與 HER2 狀態（15,418 人，取自未使用 trastuzumab 的試驗）沒有預測價值**。
  T1N0 的 5–20 年遠端復發絕對風險依分級為低分級 10%、中分級 13%、高分級 17%；
  任何復發或對側乳癌則為 17%、22%、26%。[S30]
- **三條路線各自的大致治療順序（不展開個別療法）**：
  ASCO 前導性治療指引（2021）明確寫出各亞型的分流——
  **三陰性**：臨床淋巴結陽性且／或至少 T1c 者應給含 anthracycline 與 taxane 的療程；
  **cT1a 或 cT1bN0 的三陰性不應常規給予前導性治療**；carboplatin 可用於提高病理完全緩解率；
  當時的證據不足以支持在標準化療上加免疫檢查點抑制劑。
  **HR+/HER2−**：可在「不需要手術資訊就能做出治療決定」時使用前導性化療；
  停經後者可用荷爾蒙治療降期。
  **HER2 陽性**：淋巴結陽性或高風險淋巴結陰性者，應給前導性治療併用抗 HER2 治療；
  T1aN0 與 T1bN0 者不應常規給予前導性治療。
  指引同時寫明：接受前導性治療的病人應由多專科團隊照護；
  **除了組織型態、分級、期別與 ER/PR/HER2 之外，證據不足以支持用其他標記或基因表現圖譜做臨床決策**。[S31]
- ASCO 輔助治療指引 2021 年更新的唯一新建議與 HER2 陽性有關：
  標準前導性化療加抗 HER2 治療後仍有病理侵襲性殘餘病灶者，應接受 14 個週期的輔助 T-DM1
  （KATHERINE 試驗，n=743 vs 743，侵襲性無病存活 HR 0.50，95% CI 0.39–0.64，P<.001；
  遠端復發風險 HR 0.60，95% CI 0.45–0.79；三級以上不良事件 25.7% vs 15.4%）。
  **這個數字只能用一句話帶過並指向 B5 與 B3，A3 不得展開。**[S32]

**Claim ceiling**

Defensible：「三種亞型不是三個標籤，是三條時間軸不一樣的路。三陰性的復發風險在頭三年壓得很滿，
過了五年反而比荷爾蒙陽性低；荷爾蒙受體陽性的風險曲線是拉長的，
五年到二十年之間仍以穩定速率持續發生，而且絕對風險取決於當初的腫瘤大小與淋巴結。
這件事會改變的不是恐懼的總量，而是恐懼的分配方式——以及為什麼抗荷爾蒙藥要吃那麼久。」

Would overstate：
- 「三陰性五年後就安全了」——[S28] 說的是**超過五年後的相對風險不再顯著高於其他型**，
  不是零風險，而且是 1987–1997 年的世代。
- 「荷爾蒙陽性比較好，所以不用太擔心」——[S30] 的 T2N4-9 遠端復發 41%（5–20 年）直接反駁。
- 「HER2 陽性預後差」——[S26] 顯示 HR+/HER2+ 四年乳癌專一存活 90.3%，
  而在第四期甚至優於 HR+/HER2−。這一句必須標明是現代標靶治療年代的資料。
- 把 [S27]（1978–1985 年隨機分派）或 [S28]（1987–1997 年）的曲線直接說成「你今天的復發率」——
  **不行**。這些世代大多在 trastuzumab、現代輔助治療與現代內分泌治療之前，
  文章必須寫出這一句誠實的限制。
- 「Ki-67 決定你屬於 luminal A 還是 B」——[S29] 用的是 14% 門檻，但 [S22] 顯示同一批腫瘤在不同實驗室
  被分為 luminal A 的比例是 17%–57%。A3 引用 [S29] 時必須同時帶這個限制。

**Caveats / safety notes**

- 這一篇最容易被讀成「我的亞型決定了我的命運」。必須寫清楚：亞型決定的是**治療路線的順序與內容**，
  不是一個個人的結局；同一個亞型內部的絕對風險，被腫瘤大小與淋巴結拉開好幾倍（[S30]）。
- 復發風險曲線的三個歷史世代（[S27][S28][S29]）都要標明年代與治療背景，
  否則會讓現代病人用過時的數字自我判刑。
- 不可以把 [S26] 的「四年乳癌專一存活」寫成「五年存活率」。年數要照抄。
- **各療法的細節、pCR 的意義、T-DM1 的排列一律不展開**（B3、B5 主場），只留一句指路。
- **急症警語**：本篇如果提到 anthracycline、taxane、carboplatin、trastuzumab，
  依固定紅線 A 必須有一段具體症狀的當天聯絡指引，並指向 C4。

**Taiwan status**

- **gap**：台灣本地的亞型別存活資料，我以 Europe PMC 檢索（`TITLE:"Taiwan" AND TITLE:"breast cancer"
  AND TITLE:"subtype" AND (TITLE:"survival" OR TITLE:"registry")`）**沒有找到可引用的來源**。
  文章中的亞型別存活數字一律標明「美國 SEER 資料」。
- 台灣的整體流行病學可用 [S9]／[S11]：女性乳癌新診斷 17,366 人（111 年）、診斷年齡中位數 57 歲、
  比全癌症中位數（65 歲）早 8 歲。

**Sources**

- **[S25]**（見 A2）— 亞型盛行率。
- **[S26] PASS** — Howlader N, Cronin KA, Kurian AW, Andridge R. (2018). *Differences in Breast Cancer Survival by Molecular Subtypes in the United States.* Cancer Epidemiol Biomarkers Prev 27(6):619-626. PMID 29593010, doi 10.1158/1055-9965.EPI-17-0627 — 建立四亞型的四年乳癌專一存活與第四期的反轉。Route: Europe PMC REST (AUTH+TITLE)。URL: https://doi.org/10.1158/1055-9965.EPI-17-0627
- **[S27] PASS** — Colleoni M, Sun Z, Price KN, et al. (2016). *Annual Hazard Rates of Recurrence for Breast Cancer During 24 Years of Follow-Up: Results From the International Breast Cancer Study Group Trials I to V.* J Clin Oncol 34(9):927-935. PMID 26786933, doi 10.1200/JCO.2015.62.3504 — 建立 ER 陽性與 ER 陰性年化復發風險曲線的交叉。Route: Europe PMC REST (TITLE)。URL: https://doi.org/10.1200/JCO.2015.62.3504
- **[S28] PASS** — Dent R, Trudeau M, Pritchard KI, et al. (2007). *Triple-negative breast cancer: clinical features and patterns of recurrence.* Clin Cancer Res 13(15 Pt 1):4429-4434. PMID 17671126, doi 10.1158/1078-0432.CCR-06-3045 — 建立三陰性的早期高峰（約第 3 年）與五年後不利影響消失。Route: Europe PMC REST (EXT_ID)。URL: https://doi.org/10.1158/1078-0432.CCR-06-3045
- **[S29] PASS** — Ribelles N, Perez-Villa L, Jerez JM, et al. (2013). *Pattern of recurrence of early breast cancer is different according to intrinsic subtype and proliferation index.* Breast Cancer Res 15(5):R98. PMID 24148581（開放取用）, doi 10.1186/bcr3559 — 建立四種內在亞型各自的復發風險曲線形狀與高峰時點。Route: Europe PMC REST (TITLE)。URL: https://doi.org/10.1186/bcr3559
- **[S30] PASS** — Pan H, Gray R, Braybrooke J, et al.（EBCTCG）(2017). *20-Year Risks of Breast-Cancer Recurrence after Stopping Endocrine Therapy at 5 Years.* N Engl J Med 377(19):1836-1846. PMID 29117498, doi 10.1056/NEJMoa1701830 — 建立 ER 陽性 5–20 年遠端復發的絕對風險（依 T 與 N 分層）與 PR/HER2 無獨立預測價值。Route: Europe PMC REST (EXT_ID)。URL: https://doi.org/10.1056/NEJMoa1701830
- **[S31] PASS** — Korde LA, Somerfield MR, Carey LA, et al. (2021). *Neoadjuvant Chemotherapy, Endocrine Therapy, and Targeted Therapy for Breast Cancer: ASCO Guideline.* J Clin Oncol 39(13):1485-1505. PMID 33507815, doi 10.1200/JCO.20.03399 — 建立三亞型各自的前導性治療分流與「多專科團隊」「其他標記證據不足」的立場。Route: Europe PMC REST (TITLE)。URL: https://doi.org/10.1200/JCO.20.03399
- **[S32] PASS** — Denduluri N, Somerfield MR, Chavez-MacGregor M, et al. (2021). *Selection of Optimal Adjuvant Chemotherapy and Targeted Therapy for Early Breast Cancer: ASCO Guideline Update.* J Clin Oncol 39(6):685-693. PMID 33079579, doi 10.1200/JCO.20.02510 — 建立 HER2 陽性殘餘病灶後的輔助 T-DM1 建議（**A3 只能一句話帶過，主場在 B5／B3**）。Route: Europe PMC REST (TITLE)。URL: https://doi.org/10.1200/JCO.20.02510

---

# A4 — 報告哪幾行真的會改變治療

> **這一篇的任務是把三條線分開，不是講細節。** 依 SPEC 第三節與第六節：
> 第一條線的試驗與分數 → **B4**；第二條線的轉移性用藥 → **D5**；
> 第三條線的完整內容 → **A6**；台灣的自費決策邏輯 → **D4**。
> **A4 不得出現任何多基因表現分析的分數或試驗名稱，也不得出現任何轉移性標靶藥物的療效數字。**

**Key facts**

- **第一條線（多基因表現分析，目的是證明可以少做化療）的邊界，指引寫得很死**：
  ASCO 2022 年生物標記指引更新明訂——
  Oncotype DX、MammaPrint、Breast Cancer Index（BCI）、EndoPredict
  **可用於停經後或 50 歲以上、早期 ER 陽性且 HER2 陰性、淋巴結陰性或 1–3 顆陽性**的病人；
  Prosigna 與 BCI **可用於停經後、淋巴結陰性的 ER+/HER2−**；
  停經前病人，臨床醫師**只能**對淋巴結陰性的 ER+/HER2− 使用 Oncotype；
  **目前資料顯示停經前、1–3 顆淋巴結陽性的病人，不論基因檢測結果都能從化療獲益**；
  **≥4 顆淋巴結陽性者沒有資料**支持用基因檢測指導輔助化療。
  最關鍵的一句：**「這些檢測沒有一個被建議用於 HER2 陽性或三陰性乳癌的治療指引」**。
  BCI 另可用於 0–3 顆淋巴結陽性、已完成五年內分泌治療且無復發者，協助決定是否延長內分泌治療。
  指引同時說明：無法取得基因檢測時，停經後病人可用 Ki-67 併同其他參數或 IHC4 分數輔助決策。
  治療決定仍應考量期別、共病與病人偏好。[S33]
- **第二條線（腫瘤基因體檢測，目的是找藥）的邊界，也寫得很死**：
  ESMO 精準醫療工作小組 2024 年更新的建議中，
  **常規實務裡建議做腫瘤 NGS 的癌別為晚期非鱗狀非小細胞肺癌、攝護腺癌、大腸直腸癌、
  膽管癌與卵巢癌**；2024 年這一版把建議**擴大到晚期乳癌**與少數罕見腫瘤
  （胃腸道基質瘤、肉瘤、甲狀腺癌、原發部位不明癌）。
  另建議在臨床研究中心、以及與病人討論過的特定情況下執行；
  當可及配對治療時，建議對轉移性癌症執行 NGS 以偵測不分癌別（tumour-agnostic）的變異。
  **整份建議的適用對象是「advanced cancer／metastatic」，不是早期乳癌。**[S34]
- **第三條線（生殖系檢測，測的是與生俱來的風險）的邊界**：
  ASCO-SSO 2024 年指引建議 **BRCA1/2 檢測應提供給所有 65 歲以下新診斷的乳癌病人**，
  65 歲以上則依個人病史、家族史、族裔或是否符合 PARP 抑制劑治療資格選擇性提供；
  所有適合 PARP 抑制劑治療的復發乳癌病人不論家族史都應提供 BRCA1/2 檢測；
  同側或對側出現第二個原發乳癌的女性應提供檢測。
  BRCA1/2 以外的**高穿透度**基因，應提供給家族史支持者；**中穿透度**基因在需要據以說明個人與家人風險時可提供。
  病人應獲得足夠的檢測前資訊以完成知情同意；**帶有致病性變異者應接受個別化的檢測後諮詢**。
  最重要的一句：**「意義未明的變異（variants of uncertain significance, VUS）不應影響治療處置」**，
  帶有 VUS 者應持續追蹤變異的重新分類。[S35]
- **哪些欄位不會改變你現在的治療**：
  ① **VUS**——[S35] 明講不應影響處置。
  ② **Ki-67 的中間地帶**——IKWG 只支持在 ER+/HER2−、T1-2 N0-1 用 ≤5% 或 ≥30% 估計預後，
     且不同實驗室的同一批腫瘤標記指數中位數可從 0.65% 到 33.0%。[S21][S22]
  ③ **HER2-Low／HER2-Ultra-Low**——ASCO/CAP 2023 明講建立這類新結果分類「為時過早」，
     現行報告仍只有陽性／陰性，加上一段 IHC 0 vs 1+ 的註記。[S18]
  ④ **前導性治療的決策**——ASCO 2021 指引明講，除組織型態、分級、期別與 ER/PR/HER2 外，
     **證據不足以支持使用其他標記或基因表現圖譜**做臨床決策。[S31]
  ⑤ **五年之後的長期復發風險**——EBCTCG 顯示在給定 T 與 N 之後，PR 與 HER2 狀態沒有預測價值。[S30]
- **NCCN 的版本現況（僅能確認版本字串）**：NCCN
  Genetic/Familial High-Risk Assessment: Breast, Ovarian, Pancreatic, and Prostate 的現行版本為
  **Version 2.2026**。**NCCN 的專業版演算法需登入，我只能確認版本字串，
  不得列舉其內容。** NCCN 乳癌治療指引的版本字串我沒有取得（見 [S37] FAIL）。[S36]

**Claim ceiling**

Defensible：「病人聽到『基因檢測』時腦子裡是一件事，臨床上是三件目的不同的事。
第一份報告在問『化療加下去有沒有好處』，它的結論常常是不用做，而且只適用於特定族群——
HER2 陽性與三陰性完全不適用。第二份報告在問『有沒有一個可以打的靶』，
它的建議對象是晚期／轉移性，不是剛確診的早期病人。第三份報告在問『這是不是遺傳來的』，
它同時影響手術決定與家人。搞清楚手上這份是哪一份，比報告上任何一個數字都重要。」

Would overstate：
- 「做了基因檢測就可以不用化療」——**這是全系列最高風險的誤讀**（SPEC 紅線 1）。
  A4 只寫「第一條線的問題是化療加下去有沒有好處」，**不得給任何分數或結論**。
- 「做了基因檢測就會有藥」——**紅線 2**。[S34] 的適用對象是晚期，而且 ESMO 是以可及配對治療為前提。
- 「三陰性也可以做基因檢測來決定要不要化療」——[S33] 明確說沒有一個檢測被建議用於 HER2 陽性或三陰性。
- 「停經前淋巴結陽性的人可以用檢測分數決定不做化療」——[S33] 明確說目前資料顯示這一群不論檢測結果都獲益。
- 「NCCN 說……」+ 具體內容——除非另有可查證來源，否則只能寫版本字串。

**Caveats / safety notes**

- 這篇的最大風險不是講錯數字，而是**讓讀者拿錯報告去做決定**。開頭就要把三條線分開，
  每一條後面都寫「這一條的細節在哪一篇」。
- **不得出現任何試驗名稱或分數**（TAILORx、RxPONDER、MINDACT 一律不寫）——那是 B4 的主場。
- **不得出現任何轉移性標靶藥物的療效數字**——那是 D5 的主場。
- VUS 這一段要寫得溫和但明確：拿到「意義未明」不是壞消息也不是好消息，
  指引直接說它不應該改變處置，而且分類可能會隨時間改變（[S35]）。
- 費用與給付的**跨項目決策邏輯**屬 D4 主場；A4 只寫「哪一條線在台灣有健保、哪一條沒有」的一句話，
  細節指向 D4 與 A6。

**Taiwan status**

- **第三條線在台灣有明確的健保條文，但範圍很窄**（詳見 A6 的 [S51]）：健保支付標準
  「30301B BRCA1/2 基因檢測（BRCA testing, germline or somatic）」在乳癌只給付**三陰性乳癌**，
  且限特定情境；**HR+/HER2− 與 HER2 陽性乳癌的生殖系 BRCA 檢測不在健保 NGS 給付範圍內**。
- **第一條線（多基因表現分析）的台灣給付狀態不在本簡報範圍**，屬 **D4** 主場；A4 只寫一句指路。
- **第二條線的其餘癌別給付內容**屬 D5／D4；A4 不展開。

**Sources**

- **[S33] PASS** — Andre F, Ismaila N, Allison KH, et al. (2022). *Biomarkers for Adjuvant Endocrine and Chemotherapy in Early-Stage Breast Cancer: ASCO Guideline Update.* J Clin Oncol 40(16):1816-1837. PMID 35439025, doi 10.1200/JCO.22.00069 — 建立第一條線的適用族群邊界，以及「HER2 陽性與三陰性不適用」。Route: Europe PMC REST (EXT_ID)。URL: https://doi.org/10.1200/JCO.22.00069
- **[S34] PASS** — Mosele MF, Westphalen CB, Stenzinger A, et al. (2024). *Recommendations for the use of next-generation sequencing (NGS) for patients with advanced cancer in 2024: a report from the ESMO Precision Medicine Working Group.* Ann Oncol 35(7):588-606. PMID 38834388, doi 10.1016/j.annonc.2024.04.005 — 建立第二條線的適用對象為晚期／轉移性，2024 年擴及晚期乳癌。（勘誤：Ann Oncol 2025;36(4):472, PMID 39984357）Route: Europe PMC REST (AUTH+TITLE)。URL: https://doi.org/10.1016/j.annonc.2024.04.005
- **[S35] PASS** — Bedrosian I, Somerfield MR, Achatz MI, et al. (2024). *Germline Testing in Patients With Breast Cancer: ASCO-Society of Surgical Oncology Guideline.* J Clin Oncol 42(5):584-604. PMID 38175972, doi 10.1200/JCO.23.02225 — 建立第三條線的檢測門檻（≤65 歲全體提供）與「VUS 不應影響處置」。Route: Europe PMC REST (AUTH+TITLE)。URL: https://doi.org/10.1200/JCO.23.02225
- **[S36] PASS（僅版本字串）** — NCCN. *NCCN Guidelines Insights: Genetic/Familial High-Risk Assessment: Breast, Ovarian, Pancreatic, and Prostate, Version 2.2026*（NCCN Continuing Education 活動頁，開課日 2026-02-10）。**只可引用版本字串，不得列舉內容（專業版演算法需登入）。** Route: WebFetch。URL: https://education.nccn.org/Feb2026 ；指引頁 https://www.nccn.org/guidelines/guidelines-detail?category=2&id=1545
- **[S37] FAIL** — NCCN 乳癌治療指引的版本字串：`https://www.nccn.org/guidelines/guidelines-detail?category=1&id=1419` WebFetch 回 403；`category_1` 列表頁以 curl 取得 HTTP 200 但 WebFetch 回 403，未能取得版本字串。**文章不得提及 NCCN 乳癌治療指引的版本或內容。**

---

# A5 — 影像上的大小，跟真正的不一樣

**Key facts**

- **COMICE（隨機對照試驗）**：英國 45 個中心、1,623 名 18 歲以上、經切片確診、
  在三重評估後預計接受廣泛局部切除的原發乳癌女性，隨機分派做 MRI（n=816）或不再做影像（n=807）。
  主要終點為隨機分派後六個月內再次手術／進一步乳房切除，或初次手術時病理上「本可避免的」乳房切除。
  **結果：MRI 組 153 人（19%）需再次手術，對照組 156 人（19%），勝算比 0.96（95% CI 0.75–1.24），P=0.77。**
  作者結論：在這個族群，MRI 對降低再次手術率可能是不必要的。[S38]
- **MONET（隨機對照試驗）**：418 名有不可觸診 BIRADS 3–5 病灶的病人，隨機分派為常規照護
  （乳房攝影、超音波、粗針切片）或在切片前加做 MRI（MRI 組 207 人、對照組 211 人）。
  MRI 組 74 人有 83 個惡性病灶，對照組 75 人有 80 個。
  **初次乳房保留手術率兩組相近（68% vs 66%）；但初次保留手術後因切緣陽性而再次切除的比例，
  MRI 組 18/53（34%）高於對照組 6/50（12%），P=0.008**；轉為乳房切除的人數兩組無顯著差異；
  初次保留手術後任何額外手術介入的比例為 45%（24/53）vs 28%（14/50），P=0.069。
  作者結論：**在不可觸診乳癌的常規照護中加做 MRI，反常地與較高的再切除率相關；
  不應常規用於術前評估。**[S39]
- **統合分析（9 篇研究：2 篇隨機試驗、7 篇對照世代，3,112 名任何組織型態的乳癌病人）**：
  MRI 組 vs 無 MRI 組——
  **初次乳房切除 16.4% vs 8.1%（OR 2.22，P<0.001；校正後 OR 3.06，P<0.001）；
  初次保留手術後再切除 11.6% vs 11.4%（OR 1.02，P=0.87；校正後 OR 0.95，P=0.71）；
  整體乳房切除 25.5% vs 18.2%（OR 1.54，P<0.001；校正後 OR 1.51，P<0.001）**。
  在 766 名**侵襲性小葉癌（ILC）**病人中：初次乳房切除 31.1% vs 24.9%（OR 1.36，P=0.056；校正後 OR 2.12，P=0.008）；
  初次保留手術後再切除 **10.9% vs 18.0%（OR 0.56，P=0.031；校正後 OR 0.56，P=0.09）**；
  整體乳房切除 43.0% vs 40.2%（OR 1.12，P=0.45；校正後 OR 1.64，P=0.034）。
  作者結論：MRI 顯著提高乳房切除率，常規使用的利害比不利；**在 ILC 減少再切除的證據薄弱，
  而且代價是更多乳房切除，整體病人獲益並不明朗。**[S40]
- **個人資料統合分析（IPD，4 篇符合條件的研究、3,169 名病人、3,180 個受影響乳房，年齡中位數 56.2 歲）**：
  **八年局部復發無事件存活 MRI 組 97% vs 無 MRI 組 95%（P=.87）；
  多變量模型中 MRI 對局部復發無事件存活無顯著影響（HR 0.88，95% CI 0.52–1.51，P=.65）**，
  而年齡、切緣狀態與腫瘤分級都與局部復發無事件存活相關（皆 P<.05）。
  限於接受保留手術加放療者的敏感度分析 HR 為 0.96（95% CI 0.52–1.77，P=.90）。
  **八年遠端復發無事件存活 MRI 組 89% vs 無 MRI 組 93%（P=.37）**；多變量 HR 1.18（95% CI 0.76–2.27，P=.48），
  敏感度分析 1.31（95% CI 0.76–2.27，P=.34）。
  **結論：術前 MRI 對患側乳房分期並未降低局部或遠端復發風險。**[S41]
- **MIPA（前瞻觀察性、27 個中心、5,896 名 18–80 歲經切片確診的乳癌病人）**：
  2,763 人（46.9%）只做常規影像，3,133 人（53.1%）做了 MRI（其中 2,441 人是術前用意）。
  做 MRI 的病人較年輕、乳房較緻密、腫瘤 ≥20 mm 較多、侵襲性小葉癌比例較高（各項 p<0.001）。
  **依常規影像即計畫乳房切除者 MRI 組 22.4% vs 無 MRI 組 14.4%（p<0.001）；
  MRI 組因 MRI 而額外計畫乳房切除的比例為 11.3%；
  第一線加第二線實際執行的整體乳房切除率 36.3% vs 18.0%（p<0.001）。
  在接受保留手術者中，MRI 組的再次手術率較低（8.5% vs 11.7%，p<0.001）。**
  作者自己的結論句：MRI 帶來多 11.3% 的乳房切除，換來保留手術族群少 3.2% 的再次手術。開放取用。[S42]
- **MIPA 的小葉癌配對分析（唯一支持 MRI 的一組數字，但不是隨機試驗）**：
  547 名以粗針切片診斷的單側侵襲性小葉癌，依九項干擾因子 1:1 配對後各留 103 人。
  **第一線乳房切除率 MRI 組 21.4%（22/103）vs 無 MRI 組 18.4%（19/103），p=0.727，OR 1.20（95% CI 0.61–2.38），無顯著差異；
  再次手術率 MRI 組 1.9%（2/103）vs 無 MRI 組 12.6%（13/103），p=0.007，避免再次手術的 OR 7.29（95% CI 1.60–33.21）；
  整體乳房切除率 23.3% vs 21.4%，p=0.867，無顯著差異。**
  作者明講：**目前沒有針對粗針切片診斷之 ILC 的術前 MRI 隨機對照試驗**，本研究以配對緩解干擾。[S43]
- **MRI 對「另一側乳房」的偵測率（ACRIN 6667）**：969 名新診斷單側乳癌、
  對側乳房在臨床檢查與乳房攝影上均無異常的女性接受 MRI。
  **MRI 在對側乳房偵測到臨床與影像上隱匿的乳癌 30 人（3.1%）**；敏感度 91%、特異度 88%、陰性預測值 99%。
  **121 人（12.5%）因 MRI 陽性而接受切片，其中 30 人（24.8%）為癌症**——
  也就是**四個因 MRI 而切片的人裡有三個不是癌**；30 例中 18 例為侵襲癌，侵襲癌平均直徑 10.9 mm。
  偵測到的額外癌症數不受乳房緻密度、停經狀態或原發腫瘤組織特徵影響。[S44]
- **MRI 會延後手術**：多專科乳癌門診 577 名病人，130 人做了術前 MRI。
  **MRI 與術前評估延後 22.4 天相關（p=0.011）**；控制 T 大小與期別後，
  **做 MRI 者接受乳房切除的勝算比為 1.80（p=0.024）**；
  做 MRI 者的切緣陽性率（21.6% vs 13.8%，p=0.20）與由保留轉為切除的比例（9.8% vs 5.9%，p=0.35）都沒有比較好。
  這是單一機構的回溯性資料。[S45]
- **乳房斷層攝影（tomosynthesis, DBT）——證據在篩檢而不在術前範圍評估**：
  MAITA 聯盟兩個隨機試驗的合併資料（基期 100,743 名女性、664 例癌症；次輪追蹤 82,938 名女性、550 例癌症）。
  **第一輪 DBT 組的偵測率比單用數位乳房攝影高 50%；兩組間隔癌整體發生率相近（IRR 0.95，95% CI 0.69–1.32）；
  下一輪 DBT 組的偵測率低 14%，但整體仍殘留 16% 的癌症超額（IRR 1.16，95% CI 1.04–1.30）。**
  第一輪偵測增加在多數腫瘤型別一致，**但在 ≥20 mm 的大腫瘤、第三級、HER2 陽性與三陰性癌症上不成立**；
  次輪偵測下降在大腫瘤與淋巴結陽性疾病明顯，**但在侵襲性亞型（受體陰性、HER2 陽性、Ki-67 陽性、三陰性）上不明顯**。
  作者結論：DBT 較可能偵測到本來會在後續篩檢輪次以更大腫瘤現身、且預後特徵較佳的腫瘤。[S46]
- TMIST 的先導試驗（A4705，加拿大四個中心、2014–2017 年收案）中，
  因年齡不符全試驗資格（40–44 歲或 ≥75 歲）的 271 名參與者的非計畫分析：
  DM 組 389 次、DBT 組 482 次篩檢，共 8 例癌症（7 例篩檢發現：DM 1 例、DBT 6 例；DBT 組 1 例間隔癌）。
  **樣本極小，作者本人標明為「unplanned analysis」。TMIST 主試驗（EA1151）的主要結果
  截至 2026 年 8 月我在 Europe PMC 檢索不到已發表版本（見 [S48] FAIL）。**[S47]

**Claim ceiling**

Defensible：「術前磁振造影看得到更多東西，這件事沒有爭議。有爭議的是看到之後會發生什麼。
兩個隨機試驗顯示它沒有降低再次手術率，其中一個甚至再切除更多；統合分析顯示它把乳房切除率
從 8.1% 推到 16.4%；個人資料統合分析顯示八年局部與遠端復發都沒有比較少。
最大的一份前瞻觀察研究算出的交換比是：多 11.3% 的乳房切除，換來保留手術族群少 3.2% 的再次手術。
唯一比較站得住腳的例外是侵襲性小葉癌——但那是配對分析，不是隨機試驗，作者自己說沒有隨機試驗。」

Would overstate：
- 「術前 MRI 沒有用」——**不行**。[S43] 的小葉癌配對分析顯示再次手術降低六倍以上；
  [S44] 顯示對側偵測率 3.1%。要寫成「常規做沒有改善結果，特定情況下有它的位置」。
- 「MRI 會害你被切掉乳房」——[S42] 的作者明講是「臨床醫師替本來就比較可能接受乳房切除的人開 MRI」，
  這是**適應症偏差**，不是 MRI 造成的因果。這一句一定要寫進去。
- 「MRI 可以早點抓到轉移所以比較安全」——[S41] 直接反駁（八年局部與遠端復發無差異）。
- 「乳房緻密的人術前一定要做 MRI」——[S44] 明講額外偵測的癌症數**不受乳房緻密度影響**。
  緻密乳房的 MRI 證據在**篩檢**（不同族群、不同問題），不可挪用到已確診病人的範圍評估。
- 「斷層攝影比較準所以可以看清楚腫瘤範圍」——[S46] 的資料是**篩檢偵測率與間隔癌**，
  不是術前範圍評估。不可挪用。
- 「植入物、隱匿性原發癌 MRI 一定要做」——**這兩個情境我沒有查到可引用的隨機或統合證據**（見 gap），
  只能寫成「這幾種情況臨床上會考慮做，理由是常規影像看不到，但這一點我查不到高品質的比較性證據」。

**Caveats / safety notes**

- 這一篇最危險的誤讀是**病人自己去要求 MRI**，然後在一個沒有其他理由的情況下走向乳房切除。
  必須把 [S42] 的 11.3% / 3.2% 交換寫在同一段，而且把適應症偏差說清楚。
- 第二個危險誤讀是**把「MRI 沒有改善存活」讀成「醫師開 MRI 是多餘的」**。
  文章不可以寫成鼓勵病人拒絕醫師建議的檢查；要寫成「這是一個可以問理由的檢查——
  問『這次 MRI 如果看到東西，會改變你的手術計畫嗎』」。
- [S44] 的 121 人切片、30 人是癌，要寫成「四個裡三個不是癌」，讓讀者理解偽陽性的代價。
- [S45] 的 22.4 天延後，要跟 A1 的 [S4]（時間與存活的關聯）連起來看，但**不可以寫成「MRI 會害你死」**——
  兩份都是觀察性資料，效應方向不能相乘。
- **切緣的意義、保留 vs 切除的等效證據屬 B1 主場**；**前導性治療後的影像判讀屬 B3 主場**。A5 都不展開。

**Taiwan status**

- **gap**：乳房磁振造影用於乳癌術前分期的健保給付條文，我在健保支付標準中**查不到乳房專屬的 MRI 項目**，
  也查不到相關的事前審查規定。文章一律寫成「術前 MRI 是不是給付、需不需要自費，
  要跟你的個管師或醫院醫務課確認」，**不得宣稱有給付或沒給付**。
- 已查到的相關給付條文：「33145B 診斷性乳房攝影」（BIRADS 0/3/4/5 且符合特定影像發現，
  限放射診斷科專科醫師執行，**每人每年限二次**）、「19014C 乳房超音波」、
  「33125C 乳房攝影立體定位組織切片術（含乳房攝影）」。[S7]
- **gap**：乳房斷層攝影（DBT）在台灣的給付狀態，我在支付標準中查不到對應項目名稱。

**Sources**

- **[S38] PASS** — Turnbull L, Brown S, Harvey I, et al. (2010). *Comparative effectiveness of MRI in breast cancer (COMICE) trial: a randomised controlled trial.* Lancet 375(9714):563-571. PMID 20159292, doi 10.1016/S0140-6736(09)62070-5 — 建立 MRI 未降低再次手術率（19% vs 19%，OR 0.96）。Route: Europe PMC REST (EXT_ID)。URL: https://doi.org/10.1016/S0140-6736(09)62070-5
  （同試驗的 HTA 全報告：Health Technol Assess 2010;14(1):1-182, PMID 20025837, doi 10.3310/hta14010）
- **[S39] PASS** — Peters NH, van Esser S, van den Bosch MA, et al. (2011). *Preoperative MRI and surgical management in patients with nonpalpable breast cancer: the MONET - randomised controlled trial.* Eur J Cancer 47(6):879-886. PMID 21195605, doi 10.1016/j.ejca.2010.11.035 — 建立加做 MRI 反而提高再切除率（34% vs 12%，p=0.008）。Route: Europe PMC REST (AUTH+TITLE)。URL: https://doi.org/10.1016/j.ejca.2010.11.035
- **[S40] PASS** — Houssami N, Turner R, Morrow M. (2013). *Preoperative magnetic resonance imaging in breast cancer: meta-analysis of surgical outcomes.* Ann Surg 257(2):249-255. PMID 23187751, doi 10.1097/SLA.0b013e31827a8d17 — 建立初次與整體乳房切除率上升、再切除率無差異，以及 ILC 次族群的數字。Route: Europe PMC REST (AUTH+TITLE)。URL: https://doi.org/10.1097/SLA.0b013e31827a8d17
- **[S41] PASS** — Houssami N, Turner R, Macaskill P, Turnbull LW, McCready DR, Tuttle TM, Vapiwala N, Solin LJ. (2014). *An individual person data meta-analysis of preoperative magnetic resonance imaging and breast cancer recurrence.* J Clin Oncol 32(5):392-401. PMID 24395846, doi 10.1200/JCO.2013.52.7515 — 建立八年局部與遠端復發無差異。Route: Europe PMC REST (AUTH+TITLE)。URL: https://doi.org/10.1200/JCO.2013.52.7515
- **[S42] PASS** — Sardanelli F, Trimboli RM, Houssami N, et al. (2022). *Magnetic resonance imaging before breast cancer surgery: results of an observational multicenter international prospective analysis (MIPA).* Eur Radiol 32(3):1611-1623. PMID 34643778（開放取用）, doi 10.1007/s00330-021-08240-x — 建立「多 11.3% 乳房切除、少 3.2% 再次手術」與適應症偏差。Route: Europe PMC REST (AUTH+TITLE)。URL: https://doi.org/10.1007/s00330-021-08240-x
- **[S43] PASS** — Cozzi A, Di Leo G, Houssami N, et al. (2025). *Preoperative breast MRI reduces reoperations for unilateral invasive lobular carcinoma: a patient-matched analysis from the MIPA study.* Eur Radiol 35(7):3990-4000. PMID 40016317, doi 10.1007/s00330-024-11338-7 — 建立 ILC 的再次手術降低（1.9% vs 12.6%）與乳房切除率無差異；作者自陳無隨機試驗。Route: Europe PMC REST (TITLE)。URL: https://doi.org/10.1007/s00330-024-11338-7
- **[S44] PASS** — Lehman CD, Gatsonis C, Kuhl CK, et al.（ACRIN Trial 6667）(2007). *MRI evaluation of the contralateral breast in women with recently diagnosed breast cancer.* N Engl J Med 356(13):1295-1303. PMID 17392300, doi 10.1056/NEJMoa065447 — 建立對側偵測率 3.1%、切片後癌症比例 24.8%、與乳房緻密度無關。Route: Europe PMC REST (AUTH+TITLE)。URL: https://doi.org/10.1056/NEJMoa065447
- **[S45] PASS** — Bleicher RJ, Ciocca RM, Egleston BL, et al. (2009). *Association of routine pretreatment magnetic resonance imaging with time to surgery, mastectomy rate, and margin status.* J Am Coll Surg 209(2):180-187. PMID 19632594, doi 10.1016/j.jamcollsurg.2009.04.010 — 建立 MRI 與 22.4 天延後、乳房切除勝算比 1.80、切緣未改善。Route: Europe PMC REST (AUTH+TITLE)。URL: https://doi.org/10.1016/j.jamcollsurg.2009.04.010
- **[S46] PASS** — Mancuso P, Ragazzi M, Castellano I, et al. (2026). *Histological subtype and receptor characteristics of cancers detected or missed by digital mammography and tomosynthesis: Results from MAITA randomized trials.* Eur J Cancer 238:116687. PMID 41895001, doi 10.1016/j.ejca.2026.116687 — 建立 DBT 在**篩檢**中的偵測率與間隔癌數字，以及對侵襲性亞型效果不佳。Route: Europe PMC REST (TITLE)。URL: https://doi.org/10.1016/j.ejca.2026.116687
- **[S47] PASS（樣本極小，只可作為背景）** — Seely JM, Yaffe MJ, Warren L, et al. (2026). *TMIST Lead-In Randomized Trial of Breast Tomosynthesis Versus Digital Mammography: Results in Women Ineligible for the Full TMIST Trial Due to Age (40-44 or ≥ 75 Years Old).* AJR Am J Roentgenol 226(5):e2534244. PMID 41603806, doi 10.2214/AJR.25.34244 — 271 人、8 例癌症的非計畫分析。**不得用來下任何一般性結論。** Route: Europe PMC REST (TITLE)。URL: https://doi.org/10.2214/AJR.25.34244
- **[S48] FAIL** — TMIST 主試驗（EA1151）的主要結果：Europe PMC 以 `TMIST` 檢索 2025–2026 年沒有主要結果論文；
  WebSearch 也只找到 lead-in 與招募新聞。**截至 2026-08-27，TMIST 主要結果尚未發表，文章不得提及其結論。**
- **[S49] FAIL** — 隱匿性原發乳癌（occult primary）與乳房植入物情境下術前 MRI 的證據：
  Europe PMC 檢索 `TITLE:"occult primary breast" AND TITLE:"MRI"` 只回到 1999 年一篇單中心小型研究
  （Breast J 5(4):230-234, doi 10.1046/j.1524-4741.1999.99004.x）；
  `TITLE:"breast implant" AND TITLE:"MRI" AND TITLE:"cancer" AND TITLE:"staging"` 無結果。
  **這兩個「MRI 真的有幫助」的情境，我查不到可引用的高品質比較性證據，文章必須誠實說「這一點我查不到好的證據」。**

---

# A6 — 家族史：現在就該驗 BRCA 嗎

> **這一篇談的是三條線裡的第三條：生殖系（遺傳性）檢測。** 開頭要有這一句並指向 A4。
> 腫瘤檢測與轉移性用藥屬 **D5**；多基因表現分析屬 **B4**；跨項目自費決策屬 **D4**。

**Key facts**

- **在乳癌病人裡的盛行率（族群基礎的病例對照，CARRIERS 聯盟）**：
  32,247 名乳癌女性與 32,544 名未罹病女性，以 28 個癌症易感基因的自訂套組定序。
  **12 個已確立的乳癌易感基因中，致病性變異出現在 5.03% 的乳癌病人與 1.63% 的對照組。**
  勝算比：**BRCA1 為 7.62（95% CI 5.33–11.27）、BRCA2 為 5.23（95% CI 4.09–6.77）
  —— 這兩個屬高風險；PALB2 為 3.83（95% CI 2.68–5.63）—— 屬中度風險。**
  依亞型分：**BARD1、RAD51C、RAD51D 的致病性變異與 ER 陰性乳癌及三陰性乳癌的風險上升相關；
  ATM、CDH1、CHEK2 則與 ER 陽性乳癌的風險上升相關。**
  另有 16 個候選基因（含 NBN 的 c.657_661del5 創始變異）未與乳癌風險上升相關。[S50]
- **更大的獨立驗證（BRIDGES）**：60,466 名乳癌女性與 53,461 名對照，34 個候選基因。
  **蛋白質截短變異在 ATM、BRCA1、BRCA2、CHEK2、PALB2 五個基因與整體乳癌風險相關（P<0.0001）；
  BARD1、RAD51C、RAD51D、TP53 四個基因 P<0.05 且 Bayesian false-discovery probability <0.05；
  其餘 25 個基因中有 19 個，其勝算比 95% 信賴區間上限低於 2.0。**
  亞型方向：ATM 與 CHEK2 的勝算比在 **ER 陽性**較高；
  BARD1、BRCA1、BRCA2、PALB2、RAD51C、RAD51D 的勝算比在 **ER 陰性**較高。[S51]
- **帶因者的終生風險（前瞻性世代，6,036 名 BRCA1 與 3,820 名 BRCA2 女性帶因者；
  1997–2011 年收案，追蹤至 2013 年底，中位追蹤 5 年）**：
  乳癌分析納入 3,886 名女性（年齡中位數 38 歲），卵巢癌分析 5,066 名，對側乳癌分析 2,213 名（年齡中位數 47 歲）；
  追蹤期間 426 人診斷乳癌、109 人卵巢癌、245 人對側乳癌。
  **至 80 歲的累積乳癌風險：BRCA1 為 72%（95% CI 65%–79%）、BRCA2 為 69%（95% CI 61%–77%）。
  至 80 歲的累積卵巢癌風險：BRCA1 為 44%（95% CI 36%–53%）、BRCA2 為 17%（95% CI 11%–25%）。
  乳癌診斷後 20 年的對側乳癌累積風險：BRCA1 為 40%（95% CI 35%–45%）、BRCA2 為 26%（95% CI 20%–33%）；
  BRCA2 相對 BRCA1 的 HR 為 0.62（95% CI 0.47–0.82，P=.001）。**
  BRCA1 的發生率在成年早期快速上升至 30–40 歲、BRCA2 至 40–50 歲，之後維持在每 1,000 人年 20–30 例的固定水準直到 80 歲。
  風險隨一等與二等親罹患乳癌人數增加而上升（BRCA1：≥2 人 vs 0 人 HR 1.99，95% CI 1.41–2.82；
  BRCA2：HR 1.91，95% CI 1.08–3.37）。**注意：94% 經家族門診轉介、僅 6% 來自族群研究。**[S52]
- **PALB2 的風險（21 國、524 個家族的國際研究，複雜分離分析）**：
  相對風險——**女性乳癌 7.18（95% CI 5.82–8.85）、卵巢癌 2.91（95% CI 1.40–6.04）、
  胰臟癌 2.37（95% CI 1.24–4.50）、男性乳癌 7.34（95% CI 1.28–42.18）；攝護腺癌與大腸直腸癌無證據。**
  **至 80 歲的絕對風險：女性乳癌 53%（95% CI 44%–63%）、卵巢癌 5%（95% CI 2%–10%）、
  胰臟癌 2%–3%、男性乳癌 1%。** 乳癌相對風險隨年齡下降（趨勢 P=2.0×10⁻³）。[S53]
- **檢測時機會改變手術決定，這件事有三份獨立的數字**：
  ① 多倫多四個學術中心 1,007 名同意接受「快速基因檢測」（RGT）的乳癌女性（平均年齡 46.3 歲），
  **結果揭露的中位時間為 10 天；6% 的女性帶有 BRCA 變異**；帶因者選擇雙側乳房切除的比例顯著較高（p<0.0001）；
  **BRCA 陽性者中 95.7% 表示自己用這份結果做了手術決定。**[S54]
  ② 美國單一醫療系統 220 名帶有致病性 BRCA 變異的乳癌病人，其中 208 人為單側乳癌；
  106 人（51.0%）在指標手術前已知自己的帶因狀態、102 人（49%）不知道。
  **手術前已知者接受對側預防性乳房切除的比例為 76.4%，未知者為 14.7%（p<0.05）。**[S55]
  ③ 英國「主流化基因檢測」（mainstream testing，由非遺傳專科醫師在治療規劃時提供）
  580 名乳癌女性（首次診斷 474 人，年齡中位數 46 歲，IQR 38–57）。
  檢測適應症：≤45 歲 233 人（49%）、三陰性 192 人（40.5%）、<60 歲雙側乳癌 39 人（8%）、其他 72 人（14%）。
  **從啟動檢測到結果的中位時間為 18 天（IQR 15–21）；302 人（64%）在手術前拿到結果。
  手術前得知帶有 BRCA 變異者，88% 選擇雙側乳房切除；BRCA 野生型者為 5%。**[S56]
  ④ 佛州與田納西州癌症登記招募的 633 名 ≤50 歲黑人女性侵襲性乳癌世代中，
  帶有 BRCA 致病性變異且**手術前**檢測者（n=29）接受雙側乳房切除的比例為 82.8%，
  **手術後**才檢測者為 40%（P<0.0001）。開放取用。[S57]
- **降低風險手術的結果（前瞻多中心世代，2,482 名 BRCA1/2 女性帶因者，
  1974–2008 年收案於歐洲與北美 22 個中心，追蹤至 2009 年底）**：
  **接受降低風險乳房切除的 247 名女性中沒有人被診斷乳癌**；未接受者 1,372 人中有 98 人診斷乳癌。
  **接受降低風險輸卵管卵巢切除（RRSO）者的卵巢癌風險較低**——有乳癌病史者 1% vs 6%（HR 0.14，95% CI 0.04–0.59），
  無乳癌病史者 2% vs 6%（HR 0.28，95% CI 0.12–0.69）；
  首次乳癌診斷風險也較低——BRCA1 帶因者 14% vs 20%（HR 0.63，95% CI 0.41–0.96）、
  BRCA2 帶因者 7% vs 23%（HR 0.36，95% CI 0.16–0.82）。
  **RRSO 與較低的全死因死亡率（3% vs 10%，HR 0.40，95% CI 0.26–0.61）、
  乳癌專一死亡率（2% vs 6%，HR 0.44，95% CI 0.26–0.76）與卵巢癌專一死亡率
  （0.4% vs 3%，HR 0.21，95% CI 0.06–0.80）相關。**[S58]
- **RRSO 的統合分析（10 篇研究，1999–2007 年發表）**：
  RRSO 與 BRCA1/2 帶因者乳癌風險下降相關（**HR 0.49，95% CI 0.37–0.65**；
  BRCA1 HR 0.47，95% CI 0.35–0.64；BRCA2 HR 0.47，95% CI 0.26–0.84），
  以及 BRCA1/2 相關卵巢或輸卵管癌風險下降（**HR 0.21，95% CI 0.12–0.39**）。開放取用。[S59]
- **對側乳房切除與存活（回溯性分析，12 家癌症遺傳門診）**：390 名有家族史、第一或第二期乳癌、
  BRCA1/2 帶因、初次以單側或雙側乳房切除治療的女性，其中 181 人接受對側乳房切除；追蹤至診斷後 20 年
  （中位追蹤 14.3 年，範圍 0.1–20.0 年）；79 人死於乳癌（雙側組 18 人、單側組 61 人）。
  **20 年存活率：對側乳房切除組 88%（95% CI 83%–93%）、未做者 66%（95% CI 59%–73%）；
  多變量分析中對側乳房切除與乳癌死亡下降 48% 相關（HR 0.52，95% CI 0.29–0.93，P=0.03）；
  但在 79 對傾向分數配對的分析中，這個關聯未達統計顯著（HR 0.60，95% CI 0.34–1.06，P=0.08）。**
  作者自己的結論句寫得很保守：「事件數少，需要進一步研究確認」。[S60]
- **帶因者的乳癌局部治療（ASCO-ASTRO-SSO 2020 指引）**：
  新診斷、帶有 BRCA1/2 變異的病人**可以考慮接受乳房保留治療，指標癌症的局部控制與非帶因者相近**；
  但對側乳癌的顯著風險（尤其年輕女性）與同側乳房新發癌的較高風險，
  使得**討論雙側乳房切除是必要的**。中度風險基因變異者應提供乳房保留治療。
  符合乳房切除條件的 BRCA1/2 或中度穿透度基因變異者，**保留乳頭的乳房切除是合理選擇**。
  **沒有證據顯示 BRCA1/2 帶因者的放射線暴露會增加毒性或對側乳癌事件；ATM 帶因者不應被拒絕放療；
  生殖系 TP53 變異者建議乳房切除，除非局部區域復發風險顯著否則放療為禁忌。**[S61]
- **家人的檢測（cascade testing）落差有量化證據**：30 篇研究的統合分析，
  **遺傳性乳癌卵巢癌症候群家族中，親屬接受串聯基因檢測的比例為 33%（95% CI 25%–42%）**；
  女性親屬高於男性親屬、一等親高於二等親。作者結論：接受率遠低於理想，是癌症預防與早期偵測的錯失機會。[S62]
- **帶因親屬需要什麼樣的監測（ACR 2023 更新建議）**：
  **基因相關風險上升者、終生風險計算值 ≥20% 者、以及年輕時曾接受胸部放射線者，
  建議在 25 至 30 歲開始每年一次乳房 MRI 監測，並每年乳房攝影（起始年齡依風險類型在 25 至 40 歲之間）。
  帶因者若已依建議接受每年乳房 MRI，乳房攝影可延到 40 歲開始。**
  50 歲前診斷乳癌或有乳癌病史且乳房緻密者，應每年接受補充性乳房 MRI。
  **所有女性應在 25 歲前完成風險評估**，尤其黑人女性與德系猶太裔女性。
  無法接受 MRI 者，可考慮對比增強乳房攝影或超音波。[S63]
- **ASCO-SSO 2024 對檢測門檻的建議**（同 [S35]）：**所有 65 歲以下新診斷乳癌病人都應被提供 BRCA1/2 檢測**；
  65 歲以上依個人史、家族史、族裔或 PARP 抑制劑資格選擇性提供；
  同側或對側第二原發乳癌者應提供；有乳癌病史但目前無活動性疾病者，
  診斷時 ≤65 歲者應提供、>65 歲者在能說明個人與家人風險時選擇性提供；
  轉介給有臨床癌症遺傳學經驗的提供者，有助於病人選擇、擴大檢測結果的判讀與諮詢。[S35]

**Claim ceiling**

Defensible：「生殖系檢測回答的是『這是不是與生俱來的』，它會同時改變兩件事——你的手術決定，
以及你家人的篩檢起始年齡。它必須在手術前談，因為有四份獨立資料顯示：
知道結果的時間點不同，最後接受的手術就不同。指引現在的門檻已經放寬到
『65 歲以下新診斷的乳癌病人都應該被提供檢測』，這比多數人以為的『要有家族史才驗』寬得多。
但驗出帶因不等於必須切除——同一份指引說帶因者的乳房保留治療局部控制與非帶因者相近，
雙側乳房切除是一個要談、不是一個被指定的選項。」

Would overstate：
- 「BRCA 帶因就一定要雙側乳房切除」——[S61] 明確反對這種寫法。
- 「切掉對側可以延長壽命」——[S60] 的多變量分析顯著、**但傾向分數配對後不顯著（P=0.08）**，
  作者自己說事件數少。**必須把兩個結果寫在同一句裡**，而且這一段要與 B1 的紅線 4 對齊
  （對側預防性乳房切除對非帶因者沒有被證實的存活好處）。
- 「BRCA 帶因的乳癌風險是 72%，所以我一定會得」——[S52] 的世代 94% 來自家族門診，
  是**已知有家族聚集**的族群；[S50] 的族群基礎勝算比是不同的東西，兩者不可混用。
- 「PALB2 跟 BRCA 一樣危險」——[S50] 說 PALB2 是中度風險（OR 3.83），
  [S53] 說至 80 歲乳癌絕對風險 53%，都低於 BRCA1/2 的 72%/69%。
- 「切除卵巢可以降低死亡率一半」——[S58] 是觀察性世代，而且 HR 0.40 的比較組是「沒有做」，
  存在明顯的選擇偏差。要寫成「與較低的死亡率相關」。
- 「驗完就知道會不會復發」——生殖系檢測回答的不是這個問題（見 A4 的三條線）。

**Caveats / safety notes**

- **時效性紅線（固定紅線 B）**：這一段是本篇的核心。要寫清楚「手術前」的意義：
  [S54] 中位 10 天、[S56] 中位 18 天、64% 在手術前拿到結果——**這是做得到的**，
  所以病人有理由在第一次手術討論時就問「我需不需要驗、驗得來得及嗎」。
- 但**不可以把它寫成「等驗完再開刀」**。[S4]（A1）顯示時間與存活有關聯；
  正確的寫法是「這是一個要在同一次門診同時談的事，不是一個要求延後手術的理由」。
- **VUS 不應影響處置**（[S35]），這一句一定要寫，因為拿到 VUS 的病人最容易被嚇到。
- 家人的部分要寫得具體：串聯檢測的實際接受率只有 33%（[S62]），
  而帶因親屬的監測是 25–30 歲開始每年 MRI（[S63]）——**這與一般女性 45 歲開始的乳房攝影完全不同**，
  這個落差就是為什麼要主動告訴家人。
- **不得展開 PARP 抑制劑的療效數字**——那是 D5 主場；A6 只寫「檢測結果也可能影響某些藥物的資格，
  細節看 D5」。
- 男性親屬也要提（[S53] 男性乳癌 RR 7.34、[S62] 男性親屬接受率更低），但一句話帶過。

**Taiwan status**

- **健保給付生殖系 BRCA1/2 檢測——有條文，但只給三陰性乳癌（已查到正式支付標準）**：
  《全民健康保險醫療服務給付項目及支付標準》第二部第二章第一節第二十五項「次世代基因定序」
  診療項目 **30301B「BRCA1/2 基因檢測 BRCA testing (germline or somatic)」，支付 10,000 點**。
  支付規範明訂：**「除 Germline BRCA1/2 基因檢測使用血液檢體外，其他檢測限使用已確診之腫瘤病理組織」**；
  醫院資格限「區域級以上醫院或主管機關公告通過『癌症診療品質認證醫院』」，
  且須院內設立或跨院聯合組成分子腫瘤委員會（MTB），並限主管機關核定之實驗室開發檢測施行計畫表列醫療機構；
  **每人各癌別限 30301B、30302B 或 30303B 擇一申報且終生給付一次。**
  附表 2.2.1「實體腫瘤次世代基因定序給付癌別列表」中，乳癌**只列出「三陰性乳癌」**，適應症為：
  ①**局部晚期或轉移性三陰性乳癌**，檢測時機為曾接受前導性、術後輔助性或轉移性化療者，或無法接受化療者；
  ②**早期三陰性乳癌**，且須符合以下任一：（a）未接受前導性化療、若腫瘤大於二公分或具腋下淋巴結轉移者；
  （b）接受前導性化療後未完全病理緩解者。
  應先執行之檢測：ER、PR、HER2 的 IHC（25012B）均呈現陰性始得申報；若 HER2 IHC 為 2+ 應加做 HER2 FISH（12195B）。
  必須包含之檢測基因：**Germline BRCA1 及 BRCA2（全外顯子分析，含 SNV 與 indels），限使用血液檢體**。
  **→ 也就是說：HR+/HER2− 與 HER2 陽性乳癌病人的生殖系 BRCA 檢測，不在健保 NGS 給付範圍內。
  這是台灣與 ASCO-SSO 2024「65 歲以下全體提供」之間最大的落差，A6 必須寫清楚。**[S64]
- **NGS 給付上路日期與其他癌別**：健保自 **2024 年 5 月 1 日**起給付實體腫瘤／血液腫瘤次世代基因定序，
  涵蓋 19 類癌症；BRCA 基因檢測 10,000 點、小套組（≤100 個基因）20,000 點、大套組（>100 個基因）30,000 點；
  每人每癌別終生給付一次；限區域級以上醫院或癌症診療品質認證醫院、須有分子腫瘤委員會。[S65]
- **gap — 遺傳諮詢的健保給付**：我在健保支付標準中**查不到「遺傳諮詢」的獨立診療項目**。
  唯一相關的是「25021B 染色體檢查（特殊）」，其支付規範寫「限衛生福利部認證之遺傳諮詢中心申請實施」，
  但這是檢查費而非諮詢費，且「每一個案限給付一次」、「如做為一般性篩檢者，非屬本保險給付範圍」。
  **文章一律寫成「遺傳諮詢要不要另外收費、在哪裡做，要跟你的個管師或醫院醫務課確認」，
  不得宣稱遺傳諮詢有健保給付。**[S7]
- **gap — 未罹病親屬的檢測給付**：健保 NGS 給付的對象是**已確診的癌症病人**，
  我查不到未罹病親屬做 BRCA 檢測的給付條文。文章要寫成「家人的檢測費用怎麼算，要問遺傳諮詢門診」。
- **gap — 台灣乳癌病人的 BRCA 帶因率**：我沒有查到可引用的台灣本土盛行率資料。
  文章中的 5.03%、6% 等數字一律標明來源族群（美國 CARRIERS、加拿大多倫多），不得寫成台灣的比例。

**Sources**

- **[S50] PASS** — Hu C, Hart SN, Gnanaolivu R, et al. (2021). *A Population-Based Study of Genes Previously Implicated in Breast Cancer.*（CARRIERS）N Engl J Med 384(5):440-451. PMID 33471974, doi 10.1056/NEJMoa2005936 — 建立乳癌病人中致病性變異 5.03% 與各基因的勝算比及亞型方向。Route: Europe PMC REST (EXT_ID)。URL: https://doi.org/10.1056/NEJMoa2005936
- **[S51] PASS** — Breast Cancer Association Consortium; Dorling L, Carvalho S, Allen J, et al.（BRIDGES）(2021). *Breast Cancer Risk Genes - Association Analysis in More than 113,000 Women.* N Engl J Med 384(5):428-439. PMID 33471991, doi 10.1056/NEJMoa1913948 — 建立哪些基因值得放進套組，以及 ER 陽性／陰性的方向差異。Route: Europe PMC REST (EXT_ID)。URL: https://doi.org/10.1056/NEJMoa1913948
- **[S52] PASS** — Kuchenbaecker KB, Hopper JL, Barnes DR, et al. (2017). *Risks of Breast, Ovarian, and Contralateral Breast Cancer for BRCA1 and BRCA2 Mutation Carriers.* JAMA 317(23):2402-2416. PMID 28632866, doi 10.1001/jama.2017.7112 — 建立累積風險（乳癌 72%/69%、卵巢癌 44%/17%、對側 40%/26%）與分母、追蹤年數、家族門診轉介比例。Route: Europe PMC REST (EXT_ID)。URL: https://doi.org/10.1001/jama.2017.7112
- **[S53] PASS** — Yang X, Leslie G, Doroszuk A, et al. (2020). *Cancer Risks Associated With Germline PALB2 Pathogenic Variants: An International Study of 524 Families.* J Clin Oncol 38(7):674-685. PMID 31841383, doi 10.1200/JCO.19.01907 — 建立 PALB2 的相對風險與至 80 歲的絕對風險。Route: Europe PMC REST (EXT_ID)。URL: https://doi.org/10.1200/JCO.19.01907
- **[S54] PASS** — Metcalfe KA, Eisen A, Poll A, et al. (2021). *Rapid Genetic Testing for BRCA1 and BRCA2 Mutations at the Time of Breast Cancer Diagnosis: An Observational Study.* Ann Surg Oncol 28(4):2219-2226. PMID 32989658, doi 10.1245/s10434-020-09160-8 — 建立中位 10 天出結果、6% 帶因、95.7% 用結果做手術決定。Route: Europe PMC REST (TITLE)。URL: https://doi.org/10.1245/s10434-020-09160-8
- **[S55] PASS** — Yadav S, Reeves A, Campian S, Sufka A, Zakalik D. (2017). *Preoperative genetic testing impacts surgical decision making in BRCA mutation carriers with breast cancer: a retrospective cohort analysis.* Hered Cancer Clin Pract 15:11. PMID 28770017（開放取用）, doi 10.1186/s13053-017-0071-z — 建立手術前已知 vs 未知的對側預防性乳房切除比例（76.4% vs 14.7%）。Route: Europe PMC REST (TITLE)。URL: https://doi.org/10.1186/s13053-017-0071-z
- **[S56] PASS** — Ain Q, Richardson C, Mutebi M, George A, Kemp Z, Rusby JE. (2023). *Does mainstream BRCA testing affect surgical decision-making in newly-diagnosed breast cancer patients?* Breast 67:30-35. PMID 36577271（開放取用）, doi 10.1016/j.breast.2022.12.001 — 建立主流化檢測的中位 18 天、64% 手術前拿到結果、88% vs 5% 的雙側乳房切除率。Route: Europe PMC REST (TITLE)。URL: https://doi.org/10.1016/j.breast.2022.12.001
- **[S57] PASS** — Roberson ML, Reid S, Brown JA, et al. (2025). *Timing of BRCA Genetic Testing and Surgical Decision-Making Among Young Black Women With Breast Cancer.* Cancer Control 32:10732748251407739. PMID 41360000（開放取用）, doi 10.1177/10732748251407739 — 建立手術前 vs 手術後檢測的雙側乳房切除率（82.8% vs 40%，P<0.0001）。Route: Europe PMC REST (TITLE)。URL: https://doi.org/10.1177/10732748251407739
- **[S58] PASS** — Domchek SM, Friebel TM, Singer CF, et al. (2010). *Association of risk-reducing surgery in BRCA1 or BRCA2 mutation carriers with cancer risk and mortality.* JAMA 304(9):967-975. PMID 20810374, doi 10.1001/jama.2010.1237 — 建立降低風險乳房切除與 RRSO 的癌症風險與死亡率關聯（含分母）。Route: Europe PMC REST (EXT_ID)。URL: https://doi.org/10.1001/jama.2010.1237
- **[S59] PASS** — Rebbeck TR, Kauff ND, Domchek SM. (2009). *Meta-analysis of risk reduction estimates associated with risk-reducing salpingo-oophorectomy in BRCA1 or BRCA2 mutation carriers.* J Natl Cancer Inst 101(2):80-87. PMID 19141781（開放取用）, doi 10.1093/jnci/djn442 — 建立 RRSO 的合併 HR（乳癌 0.49、卵巢/輸卵管癌 0.21）。Route: Europe PMC REST (AUTH+TITLE)。URL: https://doi.org/10.1093/jnci/djn442
- **[S60] PASS** — Metcalfe K, Gershman S, Ghadirian P, et al. (2014). *Contralateral mastectomy and survival after breast cancer in carriers of BRCA1 and BRCA2 mutations: retrospective analysis.* BMJ 348:g226. PMID 24519767（開放取用）, doi 10.1136/bmj.g226 — 建立 20 年存活 88% vs 66%、多變量 HR 0.52（顯著）**與傾向分數配對後 HR 0.60（不顯著）**。Route: Europe PMC REST (AUTH+TITLE)。URL: https://doi.org/10.1136/bmj.g226
- **[S61] PASS** — Tung NM, Boughey JC, Pierce LJ, et al. (2020). *Management of Hereditary Breast Cancer: ASCO, ASTRO, and SSO Guideline.* J Clin Oncol 38(18):2080-2106. PMID 32243226, doi 10.1200/JCO.20.00299 — 建立帶因者可考慮乳房保留治療、必須討論雙側乳房切除、保留乳頭乳房切除為合理選擇、BRCA1/2 帶因者放療無額外毒性、ATM 不應拒絕放療、TP53 建議乳房切除且放療為禁忌。Route: Europe PMC REST (EXT_ID)。URL: https://doi.org/10.1200/JCO.20.00299
- **[S62] PASS** — Ahsan MD, Chandler IR, Min S, et al. (2024). *Uptake of Cascade Genetic Testing for Hereditary Breast and Ovarian Cancer: A Systematic Review and Meta-Analysis.* Clin Obstet Gynecol 67(4):702-710. PMID 39431491, doi 10.1097/GRF.0000000000000895 — 建立串聯檢測接受率 33%（95% CI 25%–42%，30 篇研究）。Route: Europe PMC REST (TITLE)。URL: https://doi.org/10.1097/GRF.0000000000000895
- **[S63] PASS** — Monticciolo DL, Newell MS, Moy L, Lee CS, Destounis SV. (2023). *Breast Cancer Screening for Women at Higher-Than-Average Risk: Updated Recommendations From the ACR.* J Am Coll Radiol 20(9):902-914. PMID 37150275, doi 10.1016/j.jacr.2023.04.002 — 建立高風險親屬的監測起始年齡（MRI 25–30 歲）、模式與頻率、以及 25 歲前完成風險評估。Route: Europe PMC REST (AUTH+TITLE)。URL: https://doi.org/10.1016/j.jacr.2023.04.002
- **[S64] PASS** — 衛生福利部中央健康保險署。《全民健康保險醫療服務給付項目及支付標準》
  第二部第二章第一節第二十五項「次世代基因定序（30301-30307）」及附表 2.2.1「實體腫瘤次世代基因定序
  （30301B-30303B）給付癌別列表」。逐字核對 30301B 的品項名稱、支付點數、支付規範五款，
  以及三陰性乳癌的兩組適應症與應先執行之檢測。Route: curl 下載官方 PDF（HTTP 200，179,327 bytes）+ pdftotext -layout 逐行核對。
  URL（專區）: https://www.nhi.gov.tw/ch/np-3636-1.html
  URL（PDF）: https://www.nhi.gov.tw/ch/dl-69964-7ec3041734cb428b922563a52f86f155-1.pdf
- **[S65] PASS** — 衛生福利部中央健康保險署（2024）。〈健保 5 月 1 日起給付癌症精準醫療「實體癌／血癌次世代基因定序檢測(NGS)」2 萬多名癌友受惠〉。
  建立生效日 2024-05-01、涵蓋癌別、三種檢測層級的點數、每人每癌別終生一次、醫院資格。Route: WebFetch。
  URL: https://www.nhi.gov.tw/ch/cp-14565-e02e0-3255-1.html
  （衛福部同稿：https://www.mohw.gov.tw/cp-16-78416-1.html）
- **[S66] FAIL** — 「乳房植入物」「隱匿性原發癌」情境的 MRI 證據（見 A5 的 [S49]），以及
  ESMO《Risk reduction and screening of cancer in hereditary breast-ovarian cancer syndromes: ESMO Clinical Practice Guideline》
  （Ann Oncol 2023;34(1):33-47, PMID 36307055, doi 10.1016/j.annonc.2022.10.004）：
  **書目資料已查證通過，但 Europe PMC 無摘要、全文未取得，ESMO 官方指引頁 WebFetch 只回到導覽骨架。
  因此只能引用「這份指引存在、版本為 2023 年」，不得引述其中任何監測起始年齡或條文。**
  親屬監測的具體建議請一律引用 [S63]（ACR 2023）。

---

## 全簡報共用的失敗紀錄（保留，不得刪除）

- **[S67] FAIL** — ASCO 指引專區 `https://www.asco.org/practice-patients/guidelines/breast-cancer`
  與 `https://www.asco.org/guidelines/breast-cancer`：curl 回 403、WebFetch 兩個網址都回 404 頁面。
  **ASCO 的官方 landing page 在本環境取不到**，因此本簡報中的 ASCO 指引一律以 DOI 連結引用，
  版本現行性另以 CAP 官方指引頁（[S19]）佐證。
- **[S68] FAIL** — 國民健康署 `www.hpa.gov.tw`：TLS 憑證驗證失敗（`CERTIFICATE_VERIFY_FAILED`），
  curl 與 WebFetch 皆無法取得。癌症登記報告的**乳癌期別分布原始資料因此未取得**，寫成 gap。

---

## 全簡報統計

- **編號說明：S12 為空號**（整理時原 A1 的兩則 FAIL 併入文末共用失敗紀錄 S67、S68）。
- **PASS：60**（S1–S11、S13–S36、S38–S47、S50–S65；其中 S10、S36、S47 為受限 PASS，
  限制條件寫在各自條目內）
- **FAIL：6**（S67 ASCO landing page、S68 國健署 TLS、S37 NCCN 乳癌治療指引版本、
  S48 TMIST 主要結果、S49 隱匿性原發癌／植入物 MRI 證據、S66 ESMO 遺傳指引全文）
- 每篇可用的 PASS 來源數：A1 = 10；A2 = 13；A3 = 8；A4 = 8（含跨篇共用）；A5 = 11；A6 = 17。
  **六篇皆達 ≥6 PASS 的門檻。**
