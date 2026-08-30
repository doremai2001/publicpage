# C 組研究簡報 — 次世代治療專題（N5 FLASH／N6 BNCT）

研究日期：2026-08-29。所有期刊來源皆以 Europe PMC REST API（`EXT_ID` / `TITLE` / `AUTH` 查詢）逐條查證，
書目欄位一律照 API 回傳值抄寫，API 沒回傳的欄位就留白。官方頁面（PMDA、清華大學、臺北榮總、ChiCTR、
ClinicalTrials.gov）皆實際抓取並記錄網址與查證日期。媒體來源逐條標示「媒體」。
臨床試驗註冊查詢使用 ClinicalTrials.gov API v2 與 chictr.org.cn，查詢日期 2026-08-29。

**跨組界線提醒**
- 法規身分的完整敘述（藥證、給付、特管、恩慈與專案的制度說明、四技術 × 四地對照）屬 **N2**。
  本簡報只保留「一行帶過」所需的最小事實：日本 BNCT 藥證（2020-03-25）與健保收載（2020 年 6 月）、
  台灣清大醫材許可證（2023 年 6 月）。制度層面的解釋不在本組展開。
- 質子的深度劑量與適應症屬 N3；本簡報僅在 FLASH 的「穿透式質子束」脈絡下提到質子，不展開。
- 證據階梯的方法論說明屬 N1；本組只提供各試驗「在哪一格」的事實。

**兩篇的紅線對應（SPEC 第六節紅線 2）**
N5、N6 每一段興奮內容必須同段接上「這目前代表什麼、不代表什麼」。本簡報的 Key facts 已把
每個試驗的 n、族群、終點寫死，撰稿時不可脫離這些分母。

---

# N5 — FLASH：一秒打完的放療，還在第一期

**Key facts**

*FLASH 效應的奠基動物證據（真的、而且有趣）*
- Favaudon 等人 2014 年發表於 Science Translational Medicine 的奠基研究：C57BL/6J 小鼠胸腔照射，
  比較超高劑量率（≥40 Gy/s，FLASH，脈衝 ≤500 ms）與傳統劑量率（≤0.03 Gy/s）單次照射。
  傳統劑量率 15 Gy 引發肺纖維化（TGF-β 路徑活化）；FLASH 在 20 Gy 以下、追蹤超過 36 週
  未出現肺部併發症。同時，在人類腫瘤異種移植（HBCx-12A、HEp-2）與小鼠原位肺腫瘤（TC-1 Luc+）模型中，
  **FLASH 抑制腫瘤生長的效果與傳統照射相同**——正常組織受保護、腫瘤控制不打折，這就是「FLASH 效應」 [S1]
- 「≥40 Gy/s」這個門檻就是從這篇來的，後續文獻普遍沿用「>40 Gy/s」為 FLASH 的操作型定義 [S1][S3]
- 對照的量級感：傳統放療的劑量率約 0.03 Gy/s，FLASH 至少 40 Gy/s，相差超過一千倍 [S1][S6]

*機轉：提出了很多，還沒有定論*
- 2025 年 Frontiers in Oncology 的機轉回顧（開放取用）直接寫明：FLASH 效應已在許多臨床前研究
  （與少數臨床研究）中被確認，但「**機轉與影響因素仍不明確**（the mechanism and the influencing
  factors of FLASH effect remain ambiguous）」；文中整理氧耗竭（oxygen depletion）等主要假說 [S2]
- Vozenin、Bourhis、Durante 2022 年 Nature Reviews Clinical Oncology 的觀點文章：FLASH 站在
  技術、物理、化學、生物的交叉口，臨床轉譯的障礙包括**對生物機轉的理解不足、參數最佳化、
  與技術挑戰**（含超高劑量率下的劑量測定） [S3]
- 2019 年 Frontiers in Oncology 的批判性回顧（標題就叫「Silver Bullet or Fool's Gold?」，開放取用）：
  在證據熱潮中對 FLASH 的限制提出系統性質疑，可用來支撐「這個領域自己也知道還沒定案」的寫法 [S4]

*人體試驗全清單（截至 2026-08-29 已發表或已註冊者）——沒有任何一個是療效比較*
- **CHUV 單一病人（2019，洛桑）**：75 歲多重抗藥性 CD30+ T 細胞皮膚淋巴瘤病人，用專為 FLASH 設計的
  5.6 MeV 電子直線加速器，對一顆 3.5 公分皮膚腫瘤給 15 Gy、**90 毫秒內打完**。3 週時皮膚反應僅
  grade 1；腫瘤快速完全反應，追蹤 5 個月。**n=1，可行性觀察，不是試驗** [S5]
- **FAST-01（美國，質子 FLASH 首次人體試驗）**：非隨機試驗，10 位成人（中位 63 歲）四肢疼痛性骨轉移，
  共 12 個病灶，用 FLASH 化的質子治療系統以**單一穿透式（transmission）質子束**給 8 Gy 單次
  （≥40 Gy/s）——處方與傳統緩和放療相同，差別只在劑量率（傳統約 0.03 Gy/s）。主要指標是
  **工作流程可行性、治療相關毒性、疼痛緩解**；中位追蹤 4.8 個月，不良事件輕微、與傳統放療相當，
  治療床上平均 15.8 分鐘／部位。發表於 JAMA Oncology 2023 [S6]。註：n=10 是納入分析人數，
  11 位同意者中 1 位不符資格被排除 [S6]
- **FAST-02（美國，第二個質子 FLASH 試驗）——2026 年已讀出**：前瞻單臂試驗（FDA IDE G220086），
  胸腔非脊椎骨轉移（肋骨、肩胛骨），收案 12 位、實際治療 10 位，8 Gy 單次（≥40 Gy/s）。
  共同主要目標是**病人回報毒性與止痛效果**；中位追蹤 189 天，無 ≥grade 2 急性或晚期不良事件，
  8 位有 3 個月疼痛資料者中 6 位完全緩解、3 位部分緩解、1 位穩定（原文如此併計）；3 位在第 11 天前
  出現疼痛突發（pain flare）。發表於 Radiotherapy and Oncology 2026 [S7]。
  ClinicalTrials.gov NCT05524064 顯示狀態為 Active, not recruiting、收案數 10（API 查詢 2026-08-29） [S13]
- **IMPulse（洛桑，電子 FLASH 第一期劑量爬升）——2026 年發表**：黑色素瘤皮膚轉移、全身治療無效
  的病人，3+3 劑量爬升，單次 22→28 Gy（每 2 Gy 一階），9 MeV Mobetron，劑量率 >200 Gy/s、
  10 個脈衝共 90 毫秒。2021-06 至 2024-09 收案 **11 位、10 位實際治療、15 個病灶**。
  主要指標是**劑量限制毒性（DLT）**：各劑量階皆無 DLT，最大耐受劑量未達到；
  原計畫爬到 34 Gy，**因收案緩慢在 28 Gy 完成後提前中止**。發表於 Radiotherapy and Oncology 2026 [S8]
- **e-FLASH 首次人體（蘇黎世，改裝傳統 C 臂直線加速器）**：把一台傳統 Varian TrueBeam 在研究情境下
  改裝成可輸出 9 MeV 超高劑量率電子束；第一期試驗（NCT06549439）的第一位病人：黑色素瘤（皮下）病灶，
  3×9 Gy，前兩次用 e-FLASH、第三次用傳統電子束，追蹤 6 週無嚴重或非預期毒性。
  發表於 Clinical and Translational Radiation Oncology 2026（DOI 為 10.1016/j.ctro.2025.101047）。
  **n=1 的技術可行性報告** [S9]
- **中國表淺皮膚腫瘤第一期（ChiCTR2400080935）**：鄭州大學附屬河南省腫瘤醫院發起，單臂、
  預計收案 12 位，表淺皮膚腫瘤，電子束 FLASH **24–40 Gy 分 3–5 次**（注意：這是 FLASH 首見的
  分次設計之一），主要指標為 90 天內急性皮膚毒性（CTCAE v5.0）。註冊資訊經 chictr.org.cn 原頁查證：
  預註冊、招募中（Recruiting）；試驗方案論文發表於 Precision Radiation Oncology 2025（開放取用） [S10][S11]
- 把上面全部加起來：**已發表的人體經驗合計約 30 位病人**，全部是可行性、安全性、劑量爬升或
  緩和性止痛終點；**沒有任何一個人體試驗以「FLASH 是否優於傳統放療」為問題**，也沒有任何
  隨機比較存在 [S5][S6][S7][S8][S9]

*從這裡到臨床，中間隔著什麼（可引用的清單）*
- 2025 年國際多學科 Delphi 共識（21 位臨床、物理、生物專家，兩輪投票，回覆率 100%）為「下一批
  質子 FLASH 試驗」訂前提：進入特定部位的臨床試驗前，必須先有該部位的活體動物 FLASH 效應證據；
  建議只收成人、緩和情境預期存活 ≥1 年或消融情境以寡轉移為佳；主要終點應是**毒性減少**；
  並要求劑量率的準確度與治療前驗證。**「多射束、多分次、單次劑量」三題沒有達成共識**——
  分次邏輯是公開的未解問題 [S12]
- Vozenin 2022 回顧列出的轉譯障礙：機轉不明、超高劑量率下的劑量測定（偵測器在此劑量率下的
  飽和與校正）、技術參數最佳化；深部腫瘤是質子 FLASH 的領域，而 FAST-01/02 用的是**穿透式質子束**
  （不停在腫瘤、直接穿過去），這放棄了質子原本的布拉格峰優勢——目前的人體 FLASH 全部是
  淺層或緩和情境 [S3][S6][S7]

**Claim ceiling**

Defensible（可以寫到這裡為止）：
- 「FLASH 效應在動物實驗是真的、可重複的：同樣的腫瘤控制、正常組織傷害較少。」[S1]
- 「機轉有好幾個假說（氧耗竭是最有名的一個），但領域自己承認還沒有定論。」[S2][S3]
- 「到 2026 年 8 月為止，發表過的人體經驗合計約 30 人，全部在第一期或可行性階段；
  問的問題是『打得出來嗎、安全嗎』，不是『比較好嗎』。」[S5][S6][S7][S8][S9]
- 「FAST-01/02 的止痛處方跟傳統緩和放療一模一樣（8 Gy 單次），差別只在劑量率——
  它們證明的是可行，不是更好。」[S6][S7]
- 「連 FLASH 專家自己開的共識會議，都對『要不要分次、怎麼分次』沒有共識。」[S12]
- 「IMPulse 因為收案太慢提前中止爬升——連第一期都收不滿，離常規還很遠。」[S8]

Would overstate（**紅線：N5 不可出現任何人體療效宣稱**）：
- ✗「FLASH 治癒了／控制了病人的腫瘤」當成療效證據——FAST-01/02 的疼痛緩解率是緩和終點，
  與傳統 8 Gy 的歷史表現無對照設計，**不可比較、不可推論優劣** [S6][S7]
- ✗「FLASH 副作用比較少（人體）」——沒有任何人體對照。動物證據不可直接寫成人體結論 [S1][S3]
- ✗「一秒鐘打完，所以病人不用來三十次」——分次邏輯未解，Delphi 連這題都無共識 [S12]
- ✗「FLASH 很快就會進入臨床」——深部腫瘤、劑量測定、分次三關都沒過 [S3][S12]
- ✗ 暗示台灣病人有任何管道——見 Taiwan status，**沒有** [S13 查詢紀錄]

**Caveats / safety notes**

- 本篇的主旨是「新聞聲量與證據量成反比」：FLASH 的媒體聲量極大，但人體證據只有約 30 人的
  第一期／可行性資料。每一段興奮內容（動物證據、90 毫秒、改裝加速器）都必須同段落接上
  「這目前代表什麼、不代表什麼」（紅線 2）。
- FAST-01 有 2 位病人在 2 個月追蹤後、3 個月評估前死亡 [S6]——這不是治療相關，而是骨轉移
  族群本身的預後；寫進去可以誠實呈現這是什麼樣的病人族群。
- 「≥40 Gy/s」是操作型慣例不是物理常數；不同裝置（質子穿透束、電子 Mobetron >200 Gy/s、
  改裝 C 臂）的時間結構不同，不可寫成「FLASH 是一種機器」。
- 穿透式質子束是為了達到超高劑量率而放棄布拉格峰——寫 N5 時不可讓讀者以為「質子的準」與
  「FLASH 的快」目前可以同時擁有；這正是深部腫瘤未解的原因 [S3][S6]。
- 排擠內容（第五問素材）：FLASH 在台灣沒有任何可及路徑，所以它的排擠風險不是花錢做 FLASH，
  而是**為了等一個還不存在的東西而延誤現在有效的治療**，或為了出國尋求「更先進的放療」
  而中斷標準療程。

**Taiwan status**

- **台灣沒有 FLASH 臨床試驗、也沒有任何臨床可及路徑。** 查證方式：ClinicalTrials.gov API v2，
  查詢「"FLASH radiotherapy"」全球共 6 筆註冊，**位於台灣者 0 筆**；另以 query.intr=FLASH、
  query.locn=Taiwan 與 "ultra-high dose rate"＋Taiwan 交叉查詢，回傳結果皆為無關試驗
  （閃爍熱潮紅藥物等字串誤中）。查詢日期 2026-08-29 [S13 同一 API]
- 未查得任何台灣醫院或機構宣布 FLASH 臨床計畫的官方公告。此為**查證過的空白**，
  文章應明寫「我查不到台灣有任何 FLASH 的臨床試驗或治療管道」，並以此支撐紅線 2。

---

# N6 — BNCT：不是用瞄準的放療

**Key facts**

*機轉：選擇性不在射束，在硼的分布*
- 硼-10（非放射性）捕獲低能熱中子（<0.025 eV）後分裂：¹⁰B + n(th) → α（⁴He）+ ⁷Li + 2.38 MeV。
  α 粒子是高 LET 粒子，能量沉積範圍 **<10 μm，約等於一顆細胞的直徑**——殺傷力被鎖在
  含硼的那顆細胞裡，這就是「細胞層級選擇性」的物理基礎 [S14]
- 所以 BNCT 的「瞄準」不是幾何的（射束對準腫瘤），而是生物的（哪顆細胞吃進硼藥）。
  中子照野本身涵蓋腫瘤與周邊正常組織；選擇性完全依賴腫瘤與正常組織的硼濃度比 [S14]
- 硼藥 boronophenylalanine（BPA，藥證名 borofalan）經 **LAT1（L 型胺基酸轉運蛋白 1）**進入細胞；
  LAT1 在多種侵襲性腫瘤（膠質瘤、部分肺癌與乳癌亞型）上調，是 BPA 腫瘤選擇性的來源；
  2025 年的 LAT1 回顧（開放取用）同時把「需要更有選擇性的硼化合物、抗性機轉、off-target」
  列為未解挑戰 [S15]
- **硼攝取不均是真實的限制**：台灣 THOR 第一期／二期試驗以 ¹⁸F-BPA-PET 逐人測腫瘤／正常組織比
  （T/N ratio），第一次照射中位 3.4、第二次降到 2.5——同一個病人、隔 28 天，攝取就變了；
  攝取低的腫瘤，劑量學上根本拿不到處方劑量 [S24]

*日本的註冊試驗與藥證（N6 只寫一行身分，完整制度屬 N2）*
- **JHN002（頭頸癌註冊試驗）**：開放性第二期，加速器（cyclotron-based epithermal neutron source,
  C-BENS）＋ borofalan(¹⁰B) 400 mg/kg 靜脈輸注後照射中子。收案 **21 位**：8 位復發鱗癌（R-SCC，
  全部曾接受中位 65.5 Gy 放療）＋ 13 位復發／局部晚期非鱗癌（R/LA-nSCC）。主要終點 **ORR＝71%**；
  R-SCC 的 CR/PR 為 50%/25%，2 年 OS 58%；R-SCC 中位局部區域無惡化存活 11.5 個月。
  常見不良事件：落髮 95%、高澱粉酶血症 86%、噁心 81%。發表於 Radiotherapy and Oncology 2021 [S16]
- **藥證與給付（一行）**：PMDA 官方核准清單載明 Steboronine 9000 mg/300 mL for infusion
  （Stella Pharma）於 **2020 年 3 月 25 日**核准，適應症「unresectable, locally recurrent or
  unresectable advanced head and neck cancer」，SAKIGAKE 指定 [S17]；日本全國健保於
  **2020 年 6 月**收載此適應症的 BNCT [S18][S19]。完整法規與醫療觀光段屬 N2。
- **上市後全登錄監測（真實世界，2020-05 至 2023-03）**：日本僅有的兩家商轉設施（NeuCure 系統）
  全數病人登錄，分析 162 位（144 位頭頸鱗癌）：急性治療相關不良事件以高澱粉酶血症 84.0%、
  口腔炎 51.2%、唾液腺炎 50.6%、落髮 49.4% 為主；復發鱗癌 1 年／2 年 OS 為 78.8%／60.7%。
  發表於 Cancers 2024（開放取用） [S18]
- **健保時代的單中心結果（2020-06 至 2022-05，Kansai BNCT Medical Center）**：69 位病人
  （72 次治療），ORR 80.5%，1 年局部區域控制 57.1%、PFS 42.2%、OS 75.4%；作者結論是
  「若手術與根治性放療都不可行，BNCT 可考慮」——**它的位置是救援，不是取代標準治療**。
  發表於 Cancer Medicine 2024（開放取用） [S19]
- **2024 年適應症內次族群讀出**：下咽喉癌／喉癌（全部曾接受中位 70 Gy 頭頸放療）36 位：
  CR 72%、ORR 84%、1 年局部控制 63.1%、中位存活 15.5 個月；急性 grade 3 以口腔／咽黏膜炎為主，
  無 grade 4–5（高澱粉酶血症除外）。發表於 Radiotherapy and Oncology 2024 [S20]

*膠質瘤：誠實版*
- **JG002（復發惡性膠質瘤，日本加速器第二期）**：多中心單臂，27 位復發惡性膠質瘤（24 位 GBM），
  borofalan 500 mg/kg。主要終點 1 年存活率 **79.2%**、中位 OS 18.9 個月——對照是**歷史對照**
  （日本國內 bevacizumab 試驗 JO22506 的 34.5%／10.5 個月），不是隨機比較。
  **RANO 判定的中位 PFS 只有 0.9 個月**（腦水腫與影像變化使判讀複雜，27 位中 21 位惡化後用了
  bevacizumab）。最主要不良事件是腦水腫。發表於 Neuro-Oncology Advances 2021（開放取用） [S21]
- 延長追蹤（2025）：GBM 病人中位 OS 19.2 個月，2 年／3 年存活率 33.3%／20.8% [S22]
- **膠質瘤至今沒有藥證**：PMDA 核准清單（收錄至 2026 年 2 月）中 borofalan 僅出現一次，
  即 2020-03-25 的頭頸癌適應症 [S17]。日媒報導 Stella Pharma 的復發 GBM 已改走第三期
  （媒體來源，未在 jRCT 檢索中獨立驗證，見 FAIL [S42]） [S38：媒體]
- 台灣端的膠質瘤資料是 THOR 緊急治療的最大宗（腦瘤 402 人次），但**全部在試驗外**，
  沒有published 的前瞻性台灣腦瘤試驗讀出可引用（THOR 網站列有「腦瘤臨床試驗-第1期」頁面） [S32][S33]

*加速器 vs 反應器：為什麼 BNCT 走得進醫院*
- BNCT 數十年來只能在研究用核子反應爐做；**加速器中子源的開發把 BNCT 從研究帶進實際臨床**
  ——這是 2023 年日本官方回顧（開放取用）的核心敘事：「The development of accelerators for BNCT
  resulted in a paradigm shift from research to real clinical applications」；日本 2020 年將 BNCT
  納入國家健保 [S23]
- JHN002 原文：因為 cyclotron-based epithermal neutron source（C-BENS）的開發，
  「BNCT can be performed without reactors」 [S16]
- 對照：台灣現行做 BNCT 的中子源是**清華大學水池式反應器（THOR）**——研究用反應爐，
  不是醫院裡的加速器 [S24][S25]

*台灣：THOR 的完整時間線（全部經官方頁面或期刊查證）*
- **2010–2013**：第一個試驗「A phase I/II trial of BNCT for recurrent head and neck cancer at THOR」，
  17 位曾接受 63–165 Gy photon 放療的復發頭頸癌病人（23 顆腫瘤），L-BPA-fructose 400 mg/kg、
  間隔 28 天兩次照射：6 CR ＋ 6 PR，2 年 OS 47%、**2 年局部區域控制 28%**；grade 3 黏膜炎 5 位、
  grade 4 喉水腫與頸動脈出血 1 位。發表於 IJROBP 2016 [S24]；THOR 試驗史的開放取用總結
  發表於 Cancer Communications 2018 [S25]
- **2014 起**：第二個試驗 BNCT（單次）＋影像導引 IMRT：14 位收案、12 位完成合併治療，
  5 CR ＋ 4 PR（回應率 64%），但 1 年局部無惡化存活僅 21%，1 位 grade 4 喉水腫、1 位 grade 4 出血；
  作者自己的結論是「in-field 與邊緣復發率高，未來要改與放療以外的方式合併」。
  發表於 Cancers 2023（開放取用） [S26]
- **2017-01-24 起**：「緊急治療」（THOR 官方頁面用語）開始。THOR 官方統計（頁面標示統計至
  2026 年，查證日 2026-08-29）：**總治療 629 人次**——腦瘤 402、頭頸癌 207、
  其他（肝癌、外陰黑色素瘤、乳癌等）20；頁面載整體 ORR 70.2%、頭頸癌 ORR 80.0% [S32]
- **恩慈途徑的期刊證據**：2020–2024 年在 THOR「於臨床試驗之外」接受 BNCT 的復發鼻咽癌 10 位
  （北榮團隊，發表於 Journal of the Chinese Medical Association 2026，開放取用；作者自稱
  compassionate-use）：8 位可評估中 1 CR ＋ 1 PR（回應率 25%），1 年 OS 44.4%、1 年 PFS 33%；
  1 位（接受兩次 BNCT）發生顳葉壞死。**注意：這個 25% 與頭頸鱗癌系列的高回應率差距很大
  ——族群不同，不可混用** [S27]
- **2023 年 6 月**：「清大中子放射照射系統」取得衛福部**醫療器材許可證**（清華官方新聞稿
  2023-08-16：全國唯一；審議歷時 3 年；新聞稿同時載明至 2023-08-15 已治療 293 位腦癌、
  頭頸癌、黑色素瘤病人，緊急醫療自 2017 年開始、臨床試驗自 2010 年開始）。
  **許可證涵蓋的是照射系統這個器材，新聞稿未載明核准適應症範圍**；硼藥在台灣沒有藥證 [S29]
- **2024-06-13 起**：清華公告「使用 THOR 進行 BNCT 醫療服務收費辦法」：**首次治療新台幣 120 萬元、
  計畫性後續照射每次 100 萬元**（涵蓋射束 QA/QC、反應器運轉與照射、治療計畫計算、定位、
  血硼濃度分析、劑量即時監測等）；國外病人按 2 倍收費；「如為雙方合作進行 BNCT 癌症治療
  臨床試驗，費用另訂之」；病症評估由台北榮總醫師執行 [S31]
- **今天病人怎麼進得去（本篇最重要的台灣事實）**：THOR 官方「BNCT 緊急治療相關事宜」頁面：
  「如有 BNCT 治療的需求，請洽臺北榮民總醫院、台北亞東醫院、新竹馬偕醫院、台中榮民總醫院」，
  病症能否適用由醫師判斷 [S33]。合起來的可查證事實是：**途徑（1）學術臨床試驗**（THOR 網站列有
  頭頸癌第 1、2 期／腦瘤第 1 期／肝癌第 1 期試驗頁面）；**途徑（2）「緊急治療」（官方頁面用語；
  期刊論文稱 compassionate use／恩慈）經上述四家合作醫院轉介、依公告收費辦法收費**。
  它**不是**健保給付項目，也不是一般醫院掛號就有的常規自費項目。
  「緊急治療」在藥事法／醫療法下的確切法規類別（恩慈專案？專案核准？），
  官方頁面沒有寫，**列為 gap（見 FAIL [S40]），文章不得自行命名法條** [S31][S32][S33][S27]
- **北榮加速器 BNCT**：臺北榮總官方新聞（2025-08-18）：硼中子捕獲治療中心動工典禮，
  「國產國造全系統設計加速器型硼中子捕獲治療設備」（禾榮科技建置；漢民科技創辦人黃民奇
  透過陽明交大捐資 12 億元），**預計民國 116 年（2027）完工啟用**；新聞稿明寫期待未來成為
  「衛福部許可的正式治療項目」——**換句話說，現在還不是** [S34]。北榮重粒子及放射腫瘤部的
  BNCT 介紹頁（最後更新 2023-05-04）僅描述與清華合作的臨床試驗脈絡 [S35]

*「BNCT 攻克乳癌」媒體事件（2026-08-27）——查證後的事實*
- **官方源頭**：清華大學官方新聞稿（2026-08-27）〈全台第一！清華以 BNCT 治療乳癌　患者腫瘤明顯縮小〉：
  「已完成 **5 名復發三陰性乳癌患者**的 BNCT **恩慈治療**」；「在前期追蹤的 **437 緊急恩慈治療人次**中，
  整體客觀緩解率為 70.2%……頭頸癌患者的客觀緩解率更高達八成」（此 70.2%／80% 是**全部癌別的
  緊急治療統計，不是乳癌的數字**）；「團隊期盼在累積足夠病例與追蹤資料後，進一步推動乳癌 BNCT
  人體臨床試驗」——官方新聞稿自己承認**還沒有臨床試驗**；新聞稿全文沒有「攻克」二字，
  用語是「提供病患控制病情的新選擇」 [S30]
- **背後的論文**：Liao 等，Advances in Radiation Oncology 2026（開放取用；北榮＋清華團隊）：
  **4 位病人的病例系列**——2 位復發乳癌＋2 位乳癌腦轉移，全部是三陰性、多線治療後；
  論文自述「limited by its small sample size, retrospective design, and short follow-up.
  These results should therefore be considered preliminary, and further prospective validation
  is required」 [S28]
- **媒體版**：科技媒體標題〈清大 BNCT 全台首度**攻克**乳癌細胞！核級標靶「中子射線」狙擊腫瘤縮小〉
  （2026-08-27）；產業媒體標題〈三陰性乳癌新曙光　清大 BNCT 治療成效顯著〉（2026-08-27）。
  兩篇內文的事實與官方新聞稿一致（5 位恩慈治療、70.2% 為整體統計），
  **落差發生在標題**：4–5 位病人的回溯性恩慈病例系列，被寫成「攻克」「新曙光」 [S36：媒體][S37：媒體]
- **給撰稿的精確定位（處理說法、不點名機構——紅線 5）**：這個案例**不是** SPEC 原設想的
  「細胞實驗被寫成快能治療」——它是「**個位數病例的恩慈治療系列，被標題寫成攻克**」。
  批評要對準的說法是「攻克」與「新曙光」這類標題語言 vs 論文自己寫的 preliminary、
  官方稿自己寫的「還要推動臨床試驗」；批評不可否認事實本身（那 4 位病人的腫瘤反應是真的、
  發表是真的）。媒體數字 437 人次與 THOR 官方頁面的 629 人次分母不同（統計時點與納入範圍不同），
  引用時以官方頁面 [S32] 為準並註明查證日。

**Claim ceiling**

Defensible（可以寫到這裡為止）：
- 「BNCT 的選擇性來自硼藥在細胞層級的分布，α 粒子射程不到 10 微米、約一顆細胞——
  這是它跟所有『瞄準式』放療在原理上的不同。」[S14]
- 「日本以一個 21 人、ORR 71% 的第二期試驗，在 2020 年 3 月核准 borofalan 用於不可切除的
  局部晚期／復發頭頸癌，同年 6 月納入健保；上市後 162 人的真實世界登錄大致重現了安全性。」
  [S16][S17][S18]
- 「**在日本、對一個特定適應症，BNCT 是核准且有給付的治療；在台灣，它不是**——台灣的現況是
  研究用反應爐、學術試驗加上恩慈性質的『緊急治療』途徑，收費辦法由校方公告（首次 120 萬元，
  2024-06-13 起適用）。」[S17][S18][S29][S31][S32][S33]
- 「復發膠質瘤的第二期單臂資料存活數字亮眼，但對照是歷史資料，RANO 中位 PFS 只有 0.9 個月，
  而且膠質瘤至今沒有任何藥證。」[S21][S17]
- 「台灣自己的前瞻試驗誠實地告訴我們限制在哪：回應率高、但局部再復發常見
  （2 年局部區域控制 28%；合併 IMRT 後 1 年局部無惡化存活 21%）。」[S24][S26]
- 「硼攝取不均是機轉層面的真實限制——同一個病人兩次照射的腫瘤／正常組織比可以從 3.4 掉到 2.5。」[S24]

Would overstate（硬上限）：
- ✗「BNCT 是已確立的治療選項」（不加地區與適應症限定）——**「日本核准且給付的一個適應症」
  跟「在台灣是既有選項」是兩回事，每次出現都要限定**，這是本篇的 claim ceiling 主軸
- ✗「BNCT 對乳癌有效」——4–5 位恩慈病例，論文自稱 preliminary [S28][S30]
- ✗「BNCT 治好復發膠質瘤」——單臂＋歷史對照，無藥證 [S21][S17]
- ✗「不用瞄準，所以不傷正常組織」——毒性表就在那裡：高澱粉酶血症 84–86%、黏膜炎、落髮、
  腦水腫、顳葉壞死、grade 4 喉水腫與頸動脈出血各有案例 [S16][S18][S21][S24][S26][S27]
- ✗「70.2% 的病人有效」不加註「這是跨癌別的緊急治療統計、以人次計、非前瞻試驗」 [S30][S32]
- ✗ 以 JHN002 的 71% 或日本健保資料推論台灣緊急治療病人的預期結果——族群與選擇不同；
  台灣復發鼻咽癌恩慈系列的回應率是 25% [S27]
- ✗ 寫出「恩慈專案」「專案核准」等具體法條名稱——官方頁面只說「緊急治療」，法規類別未查得 [S40]

**Caveats / safety notes**

- 讀 N6 的人很可能是復發頭頸癌或腦瘤病人家屬，正在 Google「BNCT 台灣」。本篇必須同時給他
  兩件事：真實的入口（四家合作醫院的評估轉介、以及那是恩慈性質而非常規）與真實的價格
  （官方收費辦法，120 萬／次起，此數字有官方出處與日期，可寫）——**但不可寫「值得」與否**
  （紅線 4）。也要寫清楚：適不適合做，由醫師評估硼攝取（¹⁸F-BPA-PET）與病灶條件決定，
  不是付得起就能做 [S24][S31][S33]。
- 高回應率 ≠ 治癒：台灣兩個前瞻試驗都是「反應快、復發也快」的型態（2 年 LRC 28%、
  1 年 LPFS 21%）[S24][S26]；日本健保時代資料 1 年 PFS 42.2% [S19]。寫療效時回應率與
  控制率必須並列。
- 膠質瘤段落要處理「PFS 0.9 個月但 OS 18.9 個月」的矛盾：影像判讀（腦水腫、假性惡化）與
  後續 bevacizumab 使用讓單臂資料更難解讀 [S21]——這是「單臂系列為什麼不夠」的好教材。
- 乳癌媒體事件的批評要公平：事實層（5 位恩慈病例、論文 preliminary、官方稿無「攻克」）
  已查證，錯的是標題的量級，不是研究者造假。針對說法、不點名媒體與機構（紅線 5）。
- 排擠內容（第五問素材）：120 萬元起的單次費用 vs 後線標靶自費與試驗資格；以及恩慈治療
  通常要求「標準治療已用盡或不適用」——反過來說，**還有標準治療沒走完的人，不是它的對象**。

**Taiwan status**

- 途徑總結（查證日 2026-08-29）：**臨床試驗（學術性，THOR 網站列有頭頸癌、腦瘤、肝癌試驗頁）＋
  「緊急治療」（恩慈性質，2017-01-24 起，經北榮／亞東／新竹馬偕／台中榮總評估轉介，
  依 2024-06-13 公告收費辦法自費，首次 120 萬元）**。不是健保項目、不是常規醫療 [S31][S32][S33]
- 清大醫材許可證（2023 年 6 月）涵蓋「清大中子放射照射系統」這個**器材**；適應症範圍與
  許可證字號未在官方新聞稿載明，TFDA 資料庫未能檢索到（FAIL [S39]）；硼藥在台灣無藥證 [S29]
- 北榮加速器中心：2025-08-18 動工、預計 2027 啟用；官方新聞稿明寫期待未來成為衛福部許可的
  正式治療項目 [S34]
- gap：緊急治療的法規類別（見 FAIL [S40]）；緊急治療的整體療效資料只有官方網頁統計
  （70.2%，人次計）與個別癌別的期刊系列，無前瞻整體發表 [S32]

---

## 圖表數據（自繪圖的數字錨點，全部出自 PASS 來源）

### 圖 1　`fig-nt-flash-time` — 時間壓縮：傳統劑量率 vs FLASH

- 劑量率慣例門檻：FLASH **≥40 Gy/s**；傳統 **≤0.03 Gy/s**（兩個數字同出自 Favaudon 2014 的
  實驗定義 [S1]；FAST-01 沿用「≥40 Gy/sec」與「approximately 0.03 Gy/sec」 [S6]）→ 相差 >1,000 倍
- 同處方對照（圖的主軸，數字全部可引）：8 Gy 單次緩和處方——
  傳統光子系統約 0.03 Gy/s → 純出束時間約 267 秒（≈4.5 分鐘）；
  FLASH ≥40 Gy/s → **≤0.2 秒**（此兩值由 [S6] 的劑量率直接換算，圖注寫「依 FAST-01 之
  劑量率換算」）
- 實測時間點（可標在時間軸上）：
  - CHUV 首例：15 Gy／**90 毫秒** [S5]
  - IMPulse：22–28 Gy／10 個脈衝共 **90 毫秒**（>200 Gy/s） [S8]
  - FAST-01：病人在治療床上的總時間仍是 15.8 分鐘／部位（擺位與影像佔掉全部時間）[S6]
    ——圖要傳達「快的是出束，不是整個療程流程」，避免「一秒進出醫院」誤讀
- 分次對照：傳統緩和骨轉移 8 Gy×1（FAST-01/02 同處方 [S6][S7]）；中國皮膚腫瘤 FLASH 試驗
  用 24–40 Gy 分 3–5 次 [S10]——證明 FLASH 的分次邏輯未定，圖注可引 Delphi 無共識 [S12]
- 圖注：「示意圖，依 Favaudon 2014、Mascia 2023 重繪」

### 圖 2　`fig-nt-bnct` — BNCT 兩步驟機轉

- 步驟一：靜脈輸注含硼藥物 borofalan／BPA（JHN002 用 **400 mg/kg** [S16]；經 **LAT1** 進入
  腫瘤細胞 [S15]）；步驟二：熱中子（<0.025 eV）照射 [S14]
- 捕獲反應（畫在圖中央）：**¹⁰B + n(th) → ⁴He（α）+ ⁷Li + 2.38 MeV** [S14]
- 射程（圖的關鍵尺度）：α 粒子能量沉積範圍 **<10 μm ≈ 一顆細胞的直徑** [S14]
  →畫兩顆相鄰細胞：含硼細胞被 α／⁷Li 破壞，隔壁不含硼的細胞倖免
- 選擇性的量化錨點（可作圖側註）：腫瘤／正常組織硼濃度比（T/N ratio）中位 3.4（第一次照射）
  → 2.5（第二次），出自 THOR 試驗的 ¹⁸F-BPA-PET 實測 [S24]——同一張圖可順帶表達
  「比值會變、攝取不均」的限制
- 圖注：「示意圖，依 Malouff 2021 重繪」

---

# Sources

## N5 期刊文獻（全部經 Europe PMC REST API 查證）

- **[S1] PASS** — Favaudon V, Caplier L, Monceau V, et al. (2014). *Ultrahigh dose-rate FLASH irradiation increases the differential response between normal and tumor tissue in mice.* Sci Transl Med 6(245):245ra93. PMID 25031268, doi 10.1126/scitranslmed.3008973. OA: N. URL: https://doi.org/10.1126/scitranslmed.3008973 — 奠基動物研究；建立 ≥40 Gy/s vs ≤0.03 Gy/s 的定義、肺纖維化 sparing、iso-tumour control。Route: Europe PMC REST (AUTH+TITLE)
- **[S2] PASS** — Feng T, He T, Ye W, Xiang L. (2025). *Influence factor and mechanism of FLASH effect.* Front Oncol 15:1669228. PMID 41040510, doi 10.3389/fonc.2025.1669228. OA: Y. URL: https://doi.org/10.3389/fonc.2025.1669228 — 機轉回顧；原文明言 mechanism「remain ambiguous」。（另有 2025 年更正 PMID 41473430，引用時以原文為準）Route: Europe PMC REST (TITLE)
- **[S3] PASS** — Vozenin MC, Bourhis J, Durante M. (2022). *Towards clinical translation of FLASH radiotherapy.* Nat Rev Clin Oncol 19(12):791-803. PMID 36303024, doi 10.1038/s41571-022-00697-z. OA: N. URL: https://doi.org/10.1038/s41571-022-00697-z — 轉譯障礙（機轉、參數、劑量測定、技術）之引用來源。Route: Europe PMC REST (TITLE+AUTH)
- **[S4] PASS** — Wilson JD, Hammond EM, Higgins GS, Petersson K. (2019). *Ultra-High Dose Rate (FLASH) Radiotherapy: Silver Bullet or Fool's Gold?* Front Oncol 9:1563. PMID 32010633, doi 10.3389/fonc.2019.01563. OA: Y. URL: https://doi.org/10.3389/fonc.2019.01563 — 批判性回顧；作者欄經 EXT_ID 查詢逐字核對。Route: Europe PMC REST (TITLE＋EXT_ID)
- **[S5] PASS** — Bourhis J, Sozzi WJ, Jorge PG, et al. (2019). *Treatment of a first patient with FLASH-radiotherapy.* Radiother Oncol 139:18-22. PMID 31303340, doi 10.1016/j.radonc.2019.06.019. OA: N. URL: https://doi.org/10.1016/j.radonc.2019.06.019 — 洛桑 CHUV 單一病人：CD30+ T 細胞皮膚淋巴瘤、15 Gy／90 ms、grade 1 皮膚反應。Route: Europe PMC REST (TITLE)
- **[S6] PASS** — Mascia AE, Daugherty EC, Zhang Y, et al. (2023). *Proton FLASH Radiotherapy for the Treatment of Symptomatic Bone Metastases: The FAST-01 Nonrandomized Trial.* JAMA Oncol 9(1):62-69. PMID 36273324, doi 10.1001/jamaoncol.2022.5843. OA: N. URL: https://doi.org/10.1001/jamaoncol.2022.5843 — n=10、四肢骨轉移、8 Gy 單次、單一穿透式質子束、可行性＋毒性＋疼痛終點。Route: Europe PMC REST (TITLE)
- **[S7] PASS** — Daugherty EC, Zhang Y, Xiao Z, et al. (2026). *FAST-02: Results from the second in-human prospective evaluation of single-fraction proton FLASH for symptomatic thoracic bone metastases.* Radiother Oncol 222:111671. PMID 42342043, doi 10.1016/j.radonc.2026.111671. OA: N. URL: https://doi.org/10.1016/j.radonc.2026.111671 — 收案 12、治療 10、肋骨／肩胛骨、無 ≥G2 相關不良事件。Route: Europe PMC REST (TITLE)
- **[S8] PASS** — Kinj R, Schiappacasse L, Grilj V, et al. (2026). *A phase I dose escalation of FLASH radiotherapy in patients with cutaneous metastases from melanoma: The IMPulse trial.* Radiother Oncol 221:111414. PMID 41628698, doi 10.1016/j.radonc.2026.111414. OA: N. URL: https://doi.org/10.1016/j.radonc.2026.111414 — 11 位收案、10 位治療、15 病灶、22–28 Gy、無 DLT、因收案緩慢中止爬升。Route: Europe PMC REST (TITLE)
- **[S9] PASS** — von der Grün J, Dal Bello R, Psoroulas S, et al. (2026). *First-in-human e-Flash radiotherapy using a modified conventional C-arm linear accelerator.* Clin Transl Radiat Oncol 56:101047. PMID 41080989, doi 10.1016/j.ctro.2025.101047. OA: Y. URL: https://doi.org/10.1016/j.ctro.2025.101047 — 改裝 TrueBeam、9 MeV UHDR 電子束、第一位病人 3×9 Gy（前兩次 FLASH）。**Europe PMC 標示出版年 2026**（SPEC 原寫 2025，以 API 為準）。Route: Europe PMC REST (TITLE)
- **[S10] PASS** — Yang C, Luo H, Leijie M, et al. (2025). *A safety study of ultra-high dose rate FLASH radiotherapy in the treatment of superficial skin tumors: study protocol of a phase I trial.* Precis Radiat Oncol 9(2):72-76. PMID 41164421, doi 10.1002/pro6.70010. OA: Y. URL: https://doi.org/10.1002/pro6.70010 — 中國表淺皮膚腫瘤第一期方案論文：24–40 Gy／3–5 次、主要終點 90 天急性皮膚毒性。Route: Europe PMC REST (ABSTRACT:"ChiCTR2400080935")
- **[S12] PASS** — Klaver YLB, Hoogeman MS, Lu QR, et al. (2025). *Requirements and Study Design for the Next Proton FLASH Clinical Trials: an International Multidisciplinary Delphi Consensus.* Int J Radiat Oncol Biol Phys 123(1):296-305. PMID 40174648, doi 10.1016/j.ijrobp.2025.03.047. OA: N. URL: https://doi.org/10.1016/j.ijrobp.2025.03.047 — 21 位專家 Delphi；毒性為主要終點；多射束／多分次／單次劑量無共識。Route: Europe PMC REST (TITLE)

## N5 官方註冊資料（實際抓取）

- **[S11] PASS** — 中国临床试验注册中心（ChiCTR）。*ChiCTR2400080935：电子束超高剂量率放疗在表浅皮肤肿瘤中的应用（Application of electron ultra-high dose rate radiotherapy in superficial skin tumors）*。URL: https://www.chictr.org.cn/showproj.html?proj=220336 — 直接抓取原頁（HTTP 200，2026-08-29）：預註冊、單臂、樣本量 12、Recruiting、主辦單位 Henan Cancer Hospital, The Affiliated Cancer Hospital of Zhengzhou University
- **[S13] PASS** — ClinicalTrials.gov API v2。*NCT05524064：FLASH Radiotherapy for the Treatment of Symptomatic Bone Metastases in the Thorax（FAST-02）*。URL: https://clinicaltrials.gov/study/NCT05524064 — API 查詢（2026-08-29）：OverallStatus＝ACTIVE_NOT_RECRUITING、Enrollment＝10。台灣檢索亦用同一 API（見 Taiwan status 與 FAIL [S41]）

## N6 期刊文獻（全部經 Europe PMC REST API 查證）

- **[S14] PASS** — Malouff TD, Seneviratne DS, Ebner DK, et al. (2021). *Boron Neutron Capture Therapy: A Review of Clinical Applications.* Front Oncol 11:601820. PMID 33718149, doi 10.3389/fonc.2021.601820. OA: Y (PMC7952987). URL: https://doi.org/10.3389/fonc.2021.601820 — 建立捕獲反應式（¹⁰B+n(th)→α+⁷Li+2.38 MeV）、熱中子 <0.025 eV、α 射程 <10 μm ≈ 一顆細胞直徑（全文逐字查證）。Route: Europe PMC REST (TITLE+AUTH)＋fullTextXML
- **[S15] PASS** — Zheng X, Pan J, Lin D, Shao W. (2025). *L‑type amino acid transporter 1 in enhancing boron neutron capture therapy: Mechanisms, challenges and future directions (Review).* Int J Mol Med 56(5):170. PMID 40849804, doi 10.3892/ijmm.2025.5611. OA: Y. URL: https://doi.org/10.3892/ijmm.2025.5611 — BPA/LAT1 攝取邏輯與其挑戰（選擇性、抗性、off-target）。Route: Europe PMC REST (ABSTRACT:LAT1)
- **[S16] PASS** — Hirose K, Konno A, Hiratsuka J, et al. (2021). *Boron neutron capture therapy using cyclotron-based epithermal neutron source and borofalan (¹⁰B) for recurrent or locally advanced head and neck cancer (JHN002).* Radiother Oncol 155:182-187. PMID 33186684, doi 10.1016/j.radonc.2020.11.001. OA: N. URL: https://doi.org/10.1016/j.radonc.2020.11.001 — 註冊試驗：n=21（8 R-SCC＋13 R/LA-nSCC）、borofalan 400 mg/kg、主要終點 ORR＝71%、R-SCC 2 年 OS 58%、mLRPFS 11.5 月；「BNCT can be performed without reactors」。Route: Europe PMC REST (AUTH+TITLE)
- **[S17] PASS** — PMDA（獨立行政法人醫藥品醫療機器總合機構）官方文件。*List of Approved Products — New Drugs Approved in Japan (April 2004 to February 2026)*（PDF, 3.06 MB）。URL: https://www.pmda.go.jp/files/000281190.pdf — 直接下載並全文檢索（2026-08-29）：第 79 頁載 Steboronine 9000 mg/300 mL for infusion（Stella Pharma Corporation）、Approval、Borofalan (10B)、2020-03-25、「indicated for the treatment of locally unresectable recurrent or unresectable advanced head and neck cancer」、SAKIGAKE designation；**全 PDF 中 borofalan 僅此一筆——至 2026 年 2 月無適應症擴增**
- **[S18] PASS** — Sato M, Hirose K, Takeno S, et al. (2024). *Safety of Boron Neutron Capture Therapy with Borofalan(¹⁰B) and Its Efficacy on Recurrent Head and Neck Cancer: Real-World Outcomes from Nationwide Post-Marketing Surveillance.* Cancers (Basel) 16(5):869. PMID 38473231, doi 10.3390/cancers16050869. OA: Y (PMC10931064). URL: https://doi.org/10.3390/cancers16050869 — 上市後全登錄 n=162；全文載明「PMDA approvals in March 2020…included for coverage by the national health insurance system in Japan in June 2020」；當時日本僅兩家設施（NeuCure）。（2024 年另有更正 PMID 39410052，引用以原文＋更正並存為準）Route: Europe PMC REST (AUTH+TITLE)＋fullTextXML
- **[S19] PASS** — Takeno S, Yoshino Y, Aihara T, et al. (2024). *Preliminary outcomes of boron neutron capture therapy for head and neck cancers as a treatment covered by public health insurance system in Japan.* Cancer Med 13(11):e7250. PMID 38826090, doi 10.1002/cam4.7250. OA: Y. URL: https://doi.org/10.1002/cam4.7250 — 健保時代單中心 n=69（72 次）：ORR 80.5%、1 年 LRC 57.1%／PFS 42.2%／OS 75.4%。Route: Europe PMC REST (TITLE)
- **[S20] PASS** — Sato M, Hirose K. (2024). *Efficacy and safety of boron neutron capture therapy for Hypopharyngeal/Laryngeal cancer patients with previous head and neck irradiation.* Radiother Oncol 198:110382. PMID 38880413, doi 10.1016/j.radonc.2024.110382. OA: N. URL: https://doi.org/10.1016/j.radonc.2024.110382 — 2024 讀出：n=36（HPC 25＋LCA 11）、CR 72%、ORR 84%、1 年 LC 63.1%、MST 15.5 月。（2026 年有更正 PMID 41172915）Route: Europe PMC REST (AUTH+PUB_YEAR)
- **[S21] PASS** — Kawabata S, Suzuki M, Hirose K, et al. (2021). *Accelerator-based BNCT for patients with recurrent glioblastoma: a multicenter phase II study (JG002).* Neurooncol Adv 3(1):vdab067. PMID 34151269, doi 10.1093/noajnl/vdab067. OA: Y. URL: https://doi.org/10.1093/noajnl/vdab067 — n=27（24 GBM）、SPM-011 500 mg/kg、1 年存活 79.2%、mOS 18.9 月 vs 歷史對照 JO22506（34.5%／10.5 月）、**RANO mPFS 0.9 月**、腦水腫為主要不良事件、21/27 惡化後用 bevacizumab。Route: Europe PMC REST (AUTH+TITLE)
- **[S22] PASS** — Kawabata S, Goto H, Narita Y, et al. (2025). *Extended follow-up of recurrent glioblastoma patients treated with boron neutron capture therapy (BNCT): Long-term survival from a Phase II trial.* Appl Radiat Isot 226:112118. PMID 40865370, doi 10.1016/j.apradiso.2025.112118. OA: N. URL: https://doi.org/10.1016/j.apradiso.2025.112118 — JG002 延長追蹤：mOS 19.2 月、2 年 33.3%、3 年 20.8%。Route: Europe PMC REST (ABSTRACT:"JG002")
- **[S23] PASS** — Matsumura A, Asano T, Hirose K, et al. (2023). *Initiatives Toward Clinical Boron Neutron Capture Therapy in Japan.* Cancer Biother Radiopharm 38(3):201-207. PMID 36374236, doi 10.1089/cbr.2022.0056. OA: Y. URL: https://doi.org/10.1089/cbr.2022.0056 — 「加速器使 BNCT 從研究走向臨床」的官方級敘事＋2020 年納入日本國家健保。（2023 年有更正 PMID 37172293）Route: Europe PMC REST (TITLE)
- **[S24] PASS** — Wang LW, Chen YW, Ho CY, et al. (2016). *Fractionated Boron Neutron Capture Therapy in Locally Recurrent Head and Neck Cancer: A Prospective Phase I/II Trial.* Int J Radiat Oncol Biol Phys 95(1):396-403. PMID 27084657, doi 10.1016/j.ijrobp.2016.02.028. OA: N. URL: https://doi.org/10.1016/j.ijrobp.2016.02.028 — THOR 第一個試驗：n=17、L-BPA 400 mg/kg 兩次照射、6 CR＋6 PR、2 年 OS 47%、2 年 LRC 28%、T/N ratio 3.4→2.5、grade 4 喉水腫＋頸動脈出血 1 位。Route: Europe PMC REST (AUTH+TITLE)
- **[S25] PASS** — Wang LW, Liu YH, Chou FI, Jiang SH. (2018). *Clinical trials for treating recurrent head and neck cancer with boron neutron capture therapy using the Tsing-Hua Open Pool Reactor.* Cancer Commun (Lond) 38(1):37. PMID 29914577, doi 10.1186/s40880-018-0295-y. OA: Y. URL: https://doi.org/10.1186/s40880-018-0295-y — THOR 試驗史（2010–2013 第一試驗；2014 起 BNCT＋IG-IMRT 試驗）之開放取用總結。Route: Europe PMC REST (AUTH+ABSTRACT)
- **[S26] PASS** — Wang LW, Liu YH, Chu PY, et al. (2023). *Boron Neutron Capture Therapy Followed by Image-Guided Intensity-Modulated Radiotherapy for Locally Recurrent Head and Neck Cancer: A Prospective Phase I/II Trial.* Cancers (Basel) 15(10):2762. PMID 37345099, doi 10.3390/cancers15102762. OA: Y. URL: https://doi.org/10.3390/cancers15102762 — n=14 收案／12 完成：回應率 64%（5 CR＋4 PR）、1 年 OS 56%、1 年 LPFS 21%、in-field／邊緣復發為主要失敗型態。Route: Europe PMC REST (AUTH+TITLE)
- **[S27] PASS** — Wang LW, Hsueh Liu YW, Peir JJ, et al. (2026). *Compassionate boron neutron capture therapy for locally recurrent nasopharyngeal cancer: A retrospective study.* J Chin Med Assoc 89(2):109-115. PMID 41501971, doi 10.1097/jcma.0000000000001339. OA: Y. URL: https://doi.org/10.1097/jcma.0000000000001339 — **台灣恩慈途徑的期刊證據**：2020–2024 於 THOR 試驗外治療之復發鼻咽癌 n=10：回應率 25%（1 CR＋1 PR/8 可評估）、1 年 OS 44.4%、1 位顳葉壞死。第一作者單位：臺北榮總重粒子及放射腫瘤部。Route: Europe PMC REST (AUTH+TITLE)
- **[S28] PASS** — Liao HR, Chen YW, Hsieh CH, et al. (2026). *Exploring the Use of Boron Neutron Capture Therapy for Recurrent Breast Cancer and Brain Metastases: A Case Series.* Adv Radiat Oncol 11(5):101998. PMID 41757386, doi 10.1016/j.adro.2026.101998. OA: Y (PMC12934234). URL: https://doi.org/10.1016/j.adro.2026.101998 — 媒體事件背後的論文：**4 位病人**（2 復發乳癌＋2 乳癌腦轉移，三陰性）；全文自述 preliminary、需前瞻驗證（fullTextXML 逐字查證）。Route: Europe PMC REST (JOURNAL+TITLE)＋fullTextXML

## N6 官方頁面（實際抓取，含日期）

- **[S29] PASS** — 國立清華大學（官方新聞，2023-08-16）。*清華BNCT獲醫材許可證 治療瑞士名作家腦癌*。URL: https://www.nthu.edu.tw/hotNews/content/1141 — 抓取日 2026-08-29：「清大中子放射照射系統」2023 年 6 月取得衛福部醫療器材許可證（審議 3 年）；至 2023-08-15 已治療 293 位腦癌、頭頸癌、黑色素瘤病人；緊急醫療自 2017 年、臨床試驗自 2010 年開始。新聞稿未載許可證字號與適應症範圍
- **[S30] PASS** — 國立清華大學（官方新聞，2026-08-27）。*全台第一！清華以BNCT治療乳癌　患者腫瘤明顯縮小*。URL: https://www.nthu.edu.tw/hotNews/content/1258 — 抓取日 2026-08-29：5 名復發三陰性乳癌恩慈治療；437 緊急恩慈治療人次整體 ORR 70.2%、頭頸癌約八成；論文刊於 Advances in Radiation Oncology；「期盼……進一步推動乳癌 BNCT 人體臨床試驗」；全文無「攻克」字眼
- **[S31] PASS** — 國立清華大學原子科學技術發展中心。*國立清華大學使用THOR進行硼中子捕獲治療(BNCT)醫療服務收費辦法*。URL: https://thor.site.nthu.edu.tw/p/406-1192-88861,r115.php?Lang=zh-tw — 抓取日 2026-08-29：首次治療 120 萬元、計畫性後續照射每次 100 萬元、國外病人 2 倍、臨床試驗費用另訂、由台北榮總醫師評估；「本收費辦法自2024年6月13日起適用」
- **[S32] PASS** — 國立清華大學原子科學技術發展中心。*緊急治療（THOR 執行 BNCT 治療統計）*。URL: https://thor.site.nthu.edu.tw/p/406-1192-278370,r11030.php?Lang=zh-tw — 抓取日 2026-08-29：時程 2017.01.24 起；總治療 629 人次（腦瘤 402、頭頸癌 207、其他含肝癌／外陰黑色素瘤／乳癌 20）；整體 ORR 70.2%、頭頸癌 80.0%。頁面聲明數據屬 THOR，引用須註明出處
- **[S33] PASS** — 國立清華大學原子科學技術發展中心。*BNCT緊急治療相關事宜（BNCT Treatment Information）*。URL: https://thor.site.nthu.edu.tw/p/406-1192-292935,r11030.php?Lang=zh-tw — 抓取日 2026-08-29：「如有BNCT治療的需求，請洽臺北榮民總醫院，台北亞東醫院, 新竹馬偕醫院, 台中榮民總醫院」；病症適用由醫師判斷；未載法規依據
- **[S34] PASS** — 臺北榮民總醫院（官方新聞，2025-08-18）。*北榮硼中子捕獲治療中心動工　臺灣癌症治療邁向國際頂尖*。URL: https://www.vghtpe.gov.tw/News!one.action?nid=15088 — 抓取日 2026-08-29：2025-08-18 動工、預計民國 116 年（2027）完工啟用；國產加速器型設備（禾榮科技建置、捐資 12 億元經陽明交大）；「期待成為衛福部許可的正式治療項目」
- **[S35] PASS** — 臺北榮民總醫院重粒子及放射腫瘤部。*硼中子捕獲治療*（頁面最後更新 2023-05-04）。URL: https://wd.vghtpe.gov.tw/CIRO/Fpage.action?muid=18032&fid=16192 — 抓取日 2026-08-29：與清華合作之臨床試驗脈絡（至民國 104 年 5 月已有 20 位以上病人在評估不適合一線治療後接受 BNCT）；無費用資訊

## 媒體來源（僅供「媒體事件」段落查證用，文章不點名——紅線 5）

- **[S36] PASS（媒體）** — TechNews 科技新報（2026-08-27）。*清大 BNCT 全台首度攻克乳癌細胞！核級標靶「中子射線」狙擊腫瘤縮小*。URL: https://technews.tw/2026/08/27/bnct-her2 （經 cdn.technews.tw 轉址抓取）— 內文事實與官方稿一致（5 位恩慈、437 人次 70.2%）；「攻克」「核級標靶」「狙擊」為標題語言。**僅作為被批評說法的存證，不得在文章中點名**
- **[S37] PASS（媒體）** — 產業人物 Wa-People（2026-08-27）。*三陰性乳癌新曙光 清大BNCT治療成效顯著*。URL: https://wa-people.com/nthu20260827 — 同上，存證用
- **[S38] PASS（媒體，未經註冊庫獨立驗證）** — Pharma Japan（Jiho）。*Stella Begins Japan PIII of BNCT for Recurrent Glioblastoma*。URL: https://pj.jiho.jp/article/255423 — 僅用於「膠質瘤在日本仍在試驗中」的狀態描述；jRCT 檢索未能定位對應註冊（見 [S42]）。**引用時標示為媒體報導**

## FAIL（保留紀錄，不得引用為事實）

- **[S39] FAIL** — 「清大中子放射照射系統」的 TFDA 醫療器材許可證**字號與核准適應症範圍**。已檢索：web 搜尋（"清大中子放射照射系統" 許可證 衛部醫器製字）無官方資料庫結果；TFDA 許可證查詢系統為 JS 動態頁面，無法以本環境驗證。→ 許可證的存在與 2023 年 6 月時點以清華官方新聞稿 [S29] 為準；**字號與適應症範圍寫成 gap，不得杜撰**
- **[S40] FAIL** — THOR「緊急治療」在台灣法規下的**確切類別**（恩慈療法？專案核准？依哪一條）。THOR 官方頁面 [S32][S33] 僅用「緊急治療」，清華新聞稿 [S29][S30] 用「緊急醫療救治」「恩慈治療」，期刊論文 [S27] 用 compassionate use；**未查得衛福部核准文件或法規依據的官方頁面** → 文章寫「官方頁面稱為緊急治療、性質上屬恩慈性質的試驗外治療」即止，**不得自行標註法條名稱**
- **[S41] FAIL（查證過的空白，本身是 N5 的重要事實）** — 台灣的 FLASH 臨床試驗或臨床計畫。ClinicalTrials.gov API v2（2026-08-29）："FLASH radiotherapy" 全球 6 筆、台灣 0 筆；query.intr=FLASH＋Taiwan、"ultra-high dose rate"＋Taiwan 均無相關結果；未查得任何台灣機構的 FLASH 臨床官方公告 → N5 的 Taiwan status 寫「查無」，此為 PASS 級的陰性發現，但列於此以示查證路徑
- **[S42] FAIL** — Stella Pharma 復發 GBM 第三期試驗的 jRCT 註冊條目。jRCT 搜尋僅定位到無關試驗（jRCT2031240090 為 64Cu-ATSM 試驗）→ 膠質瘤「進行中的第三期」只能以媒體 [S38] 標示媒體身分帶過，或乾脆只寫「膠質瘤至今無藥證 [S17]」
- **[S43] FAIL** — 日本健保收載（2020 年 6 月）的 MHLW 官方頁面。未另行抓取厚勞省中醫協文件；June 2020 的收載事實以開放取用論文 [S18][S19][S23] 的原文敘述為準。N2 若需官方文件，由 N2 組自行補查
- **[S44] FAIL** — 清華大學秘書處新聞稿列表頁（https://secretary.site.nthu.edu.tw/p/404-1070-172220.php）抓取後僅得導航頁、無新聞稿內容 → 改用 [S30]（hotNews/content/1258）為官方新聞稿來源。此條保留為 FAIL 紀錄
