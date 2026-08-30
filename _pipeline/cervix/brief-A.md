# A 組研究簡報 — 子宮頸癌專題（階段一：確診之後）

研究日期：2026-08-30。所有期刊來源皆以 Europe PMC REST API（`TITLE`／`AUTH`／`EXT_ID` 查詢，`resultType=core` 取摘要）逐條查證，書目欄位照 API 回傳值抄寫；指引全文以 Europe PMC fullTextXML 取回後 grep 原文（ASCCP 2019＝PMC7147428、ESGO 2023＝PMC10247855、CDC STI 2021＝PMC8344968、FIGO 2021＝PMC9298213）。台灣端以 mohw.gov.tw／dep.mohw.gov.tw 頁面 curl 取原文、nhi.gov.tw 之 PDF／XLS 直接下載後 grep／xlrd 逐列檢索（nhi.gov.tw 的 HTML 頁面遭 Cloudflare 阻擋、hpa.gov.tw SSL 失敗，均記 FAIL 並改用鏡像或附件）。查不到的一律記 FAIL。

**跨組界線提醒（SPEC §五）**
- 「開刀還是放療」的決策本體 → **B1**。A2 只寫「期別決定走哪一條路」的一句話交接（本簡報在 A2 區塊保留 ESGO 的分流句，療效比較與 Landoni 一個字都不寫）。
- LACC／微創 → B2；CCRT 證據 → B3；近接治療 → C1。A 組四篇都不碰。
- **台灣抹片與 HPV 檢測公費政策 → D3 主場，A4 只寫一行**。本簡報把政策事實查證一次放在 A4 的台灣端（S31、S32），標註「D3 主用、A4 一句話」。
- **HPV 疫苗（女兒的公費、治療後接種）→ D3 主場**。A3 只寫「伴侶／成人接種」那一層（ACIP 共同決策＋台灣成人自費），S37 的公費事實供 D3 主用。
- 追蹤排程 → D3；A1 只寫「圓錐切除後的追蹤」（這是 A1 主場，D3 寫的是癌症治療後的追蹤，兩者不同）。
- 生育保存、子宮頸切除術條件 → B4。A1 寫到「錐切發現侵襲癌」為止，radical trachelectomy 只點名不展開。

---

# A1 — 抹片異常、原位癌、侵襲癌，差在哪

**Key facts**

*名詞系統（LAST／Bethesda 與 CIN 的對照）*
- 病理名詞在 2012 年由美國病理學會（CAP）與美國陰道鏡暨子宮頸病理學會（ASCCP）的 LAST 計畫統一：組織學改用兩級制 LSIL／HSIL（低度／高度鱗狀上皮內病變），HSIL 之下仍建議註記 CIN 2 或 CIN 3 [S7]
- ASCCP 2019 指引原文：「Histopathology reports based on Lower Anogenital Squamous Terminology (LAST)/World Health Organization (WHO) recommendations for reporting histologic HSIL should include CIN 2 or CIN 3 qualifiers, i.e., HSIL (CIN 2)…」；並警告 p16 染色不可濫用——「a morphologic CIN 1 on H&E should not be upgraded to histologic HSIL (CIN 2) even if p16 positive」 [S4]
- 「原位癌（carcinoma in situ）」在現行系統裡就是 CIN 3 的舊稱（McCredie 論文原文：「CIN3; also termed stage 0 carcinoma」）[S3]；腺體病變的對應名詞是原位腺癌（AIS）[S4]
- 侵襲癌從哪一格開始：FIGO 2018 分期表原文——IA 期＝「Invasive carcinoma that can be diagnosed only by microscopy, with maximum depth of invasion ≤5 mm」；IA1＝浸潤深度 ≤3 mm、IA2＝>3 且 ≤5 mm；IA1/IA2 的診斷必須靠涵蓋整個病灶的錐切（LEEP 或冷刀）標本、也可由子宮頸切除或子宮切除標本診斷 [S9]

*各級的自然史（fig-cx-cin-ladder 的數據本體，見下方圖表數據）*
- Östör 1993 年的經典文獻回顧（彙整 1950 年以來的自然史研究）：CIN 1 約 60% 消退、30% 持續、10% 進展到 CIN 3、1% 進展到侵襲癌；CIN 2 約 40%／40%／20%／5%；CIN 3 約 33% 消退、>12% 進展到侵襲癌 [S1]
- 現代統合分析（Tainio 2018，36 個研究、3,160 名未立即治療而觀察的 CIN2 患者）：**24 個月**時 50%（95% CI 43–57）消退、32%（23–42）持續、18%（11–27）進展；**30 歲以下**次族群（1,069 人）：60% 消退、23% 持續、11% 進展；前瞻研究的失聯率約 10% [S2]
- **未治療 CIN3 的真實侵襲風險（McCredie 2008，紐西蘭國家婦女醫院 1955–76 未經同意留置不治療的回溯世代，1,063 名經病理覆核的 CIN3）**：只做 punch／wedge 切片、病灶幾乎未處理的 143 人，30 年累積侵襲癌（子宮頸或陰道穹窿）發生率 **31.3%**（95% CI 22.7–42.3）；其中 24 個月內病灶仍在的 92 人為 **50.3%**（37.3–64.9）；相對地，初始治療適當（含之後常規處置）的 593 人 30 年累積風險只有 **0.7%**（0.3–1.9）[S3]

*處置：哪一級要治療、用什麼治療（ASCCP 2019 原文）*
- CIN 1（histologic LSIL）：「Observation is preferred to treatment for CIN 1」；連續兩年以上重複診斷 CIN 1 才「treatment remains acceptable」[S4]
- CIN 3：「treatment is recommended and observation is unacceptable (AII)」——除了懷孕之外沒有觀察這個選項 [S4]
- CIN 2：「treatment is recommended, unless the patient's concerns about the effect of treatment on future pregnancy outweigh concerns about cancer (BII)」；觀察的條件是鱗柱交界可見、且頸管取樣沒有 CIN2+；觀察＝每 6 個月陰道鏡＋HPV 檢測、最多 2 年 [S4]（理由正是 Tainio 的高消退率 [S2]）
- 治療方式：「Excisional treatment is preferred to ablative treatment for histologic HSIL (CIN 2 or CIN 3) in the United States. Excision is recommended for adenocarcinoma in situ (AIS)」[S4]
- AIS（採納 SGO 建議）：切片診斷 AIS 後**一律先做診斷性錐切**（即使已計畫子宮切除）以排除侵襲性腺癌；標本要完整不可分段（LEEP 加 top-hat 不可接受）、長度至少 10 mm（不考慮生育者 18–20 mm）；錐切證實 AIS 且切緣陰性後，**單純子宮切除是首選**，欲保留生育者切緣陰性下保守處理可接受；切緣陽性即使計畫子宮切除也建議先再切一次 [S4]
- 「Expedited treatment」（不經切片直接治療）：HSIL 細胞學＋HPV16 陽性、或幾乎沒篩檢過的 HPV 陽性 HSIL，25 歲以上未懷孕者首選（立即 CIN3+ 風險 ≥60% 時 preferred、25–60% 之間 acceptable）——台灣讀者的意義是「抹片很糟時醫師直接安排 LEEP 不是跳步驟」[S4]

*切緣與治療失敗（「錐切乾不乾淨」那一題）*
- Arbyn 2017 統合分析（97 個研究、44,446 名接受切除治療者）：切緣陽性率整體 23.1%（laser 錐切 17.8%、LLETZ 25.9%）；**治療後殘存／復發 CIN2+ 整體 6.6%**；切緣陽性 vs 陰性的相對風險 4.8（95% CI 3.2–7.2）；但預測治療失敗，**治療後 HPV 檢測（敏感度 91.0%）比切緣狀態（55.8%）準**——治療後 HPV 陰性者殘存風險 0.8%、切緣陰性者 3.7% [S5]
- ESGO 2023：錐切標本切緣應同時無侵襲性與前癌病變（低度病變除外）；若切緣陽性（低度病變除外）應**再做一次錐切**以排除更深的侵襲 [S8]

*錐切後的追蹤（A1 主場；癌症治療後的追蹤歸 D3）*
- ASCCP 2019：治療後 **6 個月做 HPV 檢測（不論切緣狀態）**，陽性就陰道鏡＋切片；之後 HPV 或合併檢測每 3 年一次、**至少 25 年**（新證據顯示風險升高至少持續 25 年，且沒有證據顯示治療過的人風險會回到可以 5 年一篩的水準）[S4]
- 為什麼要追這麼久：Kalliala 2020 統合分析（27 個登記串接研究）：CIN 治療後的子宮頸癌發生率 39/10 萬人年，是一般族群的 3.30 倍（2.57–4.24）；50 歲以上更高、風險升高持續至少 20 年；陰道癌 RR 10.84、外陰癌 3.34、肛門癌 5.11 也升高 [S6]

*錐切發現侵襲癌，路怎麼變（與 A2、B1 交接）*
- T1a（IA）的診斷本身就要靠錐切標本、由專家病理醫師量測浸潤深度、切緣與 LVSI（脈管侵犯）[S8]
- ESGO 2023 原文：T1a1——「**Conization can be considered a definitive treatment as hysterectomy does not improve the outcome** [IV, C]」；radical hysterectomy／trachelectomy／parametrectomy 對 T1a1 是「overtreatment and should not be performed」[IV, D]；LVSI 陰性不需淋巴結分期、LVSI 陽性可考慮 SLN [S8]
- T1a2——「Conization (with clear margins) alone or SH is an adequate treatment」[IV, B]；不需參數切除 [S8]
- 完成生育的 T1a1／T1a2 腺癌患者應提供單純子宮切除 [S8]
- 深度一旦超過 5 mm（IB 起）就換到 A2 的分期與 B1 的治療分流，A1 寫到這裡交棒

**Claim ceiling**

Defensible：
- 「抹片異常不是診斷，是『要進一步看』的信號；診斷靠陰道鏡切片，最後的層級靠病理。」[S4][S7]
- 「CIN 1 多數會自己消退，首選是追蹤不是治療；CIN 2 一半在兩年內消退（30 歲以下六成），在特定條件下可以跟醫師談觀察；CIN 3 沒有觀察這個選項。」[S1][S2][S4]
- 「原位癌（CIN 3）還不是癌——它還沒有突破基底膜——但它是癌的直接前身。不治療的話，30 年內約三分之一會變成侵襲癌；治療得當，這個數字是 0.7%。**『原位癌不可怕』這句話的成立條件是『有治療』。**」[S3]
- 「錐切／LEEP 對 CIN 2–3 和多數 T1a1 就是治療本身，不是檢查的前奏；台灣健保有『子宮頸楔狀切除術』這個支付項目。」[S4][S8][S35]
- 「切緣有病變，風險高 4.8 倍，但下一步通常是再切一次或加密追蹤，不是直接子宮切除；治療後 HPV 檢測比切緣更能預測有沒有殘存。」[S5][S8]
- 「治療過的人不是從此安全：之後得子宮頸癌的風險是一般人的 3.3 倍、持續至少 20 年——所以治療後的追蹤要用年來算，不是用次來算。」[S4][S6]

Would overstate：
- ✗「原位癌不是癌，所以不用緊張、可以慢慢來。」——McCredie 的 31.3%／50.3% 就是不治療的下場；CIN 3「observation is unacceptable」[S3][S4]
- ✗「CIN 2 可以不用管。」——觀察是有條件的（年齡／生育考量、鱗柱交界可見、頸管陰性、能配合每 6 個月回診）[S2][S4]
- ✗「錐切切乾淨就沒事了」或「切緣陽性一定要再手術」——兩個方向都超過：殘存率 6.6%、切緣陽性 RR 4.8，但 HPV 檢測才是更準的哨兵 [S5]
- ✗「LEEP 會影響懷孕所以能不切就不切。」——本簡報未查證早產風險數字（歸 B4 或不展開）；A1 只能寫「切多深要跟生育計畫一起談」，不可給早產率
- ✗ 把 Östör 的百分比寫成個人預測——那是 1950 年代以來研究的合成近似值，Östör 自己說形態學無法預測個別病人 [S1]
- ✗「AIS 跟 CIN 3 一樣處理。」——AIS 的標本要求、子宮切除首選、跳躍性病灶的特性都不同 [S4]

**Caveats / safety notes**

- Östör 的數字是舊年代（含未治療觀察）研究的合成，與 Tainio 的現代統合在 CIN 2 上方向一致但定義不同（Östör 無時間軸、Tainio 是 24 個月）；圖表不要把兩者混成一格，各自帶標籤。
- McCredie 是 1955–76 年的紐西蘭世代（「unfortunate experiment」，經司法調查後重建），族群是已確診 CIN3 者；引用時要帶「未治療」與「30 年」兩個標籤，也要同句給治療組的 0.7%——只給 31.3% 是嚇人，只給 0.7% 是騙人。
- Tainio 的 CIN2 觀察族群有近半研究偏倚風險不低（50% low risk of bias）、異質性高（I² 77–90%）；寫「約一半」不寫精確到小數。
- ASCCP 2019 是美國指引（風險閾值建立在美國 KPNC 資料）；台灣臨床實務由婦產科醫學會與各院遵循，A1 寫「國際指引」即可，不寫成台灣官方規範。
- 「原位癌不是癌」在行政上也成立（不在重大傷病清單，見 A4 台灣端），但**不可以**把「不是重大傷病」寫成「不嚴重」——它是「還來得及用小手術解決」的意思。
- 錐切後懷孕相關風險（早產）本次未查證，不可寫數字。

**Taiwan status**

- 健保「醫療服務給付項目」檔（114.01.01 生效版，官方 XLS，本組獨立重新下載檢索）：**80205C 子宮頸楔狀切除術（Cervical conization）2,810 點**，備註「雷射錐形切除術 Laser conization, CO2 比照申報」「西醫基層院所申報限設置有門診手術室及觀察病床者」；28028C 陰道鏡檢查 605 點；55001C 子宮頸切片（不含病理）430 點；15017C 婦科細胞檢查（抹片 Cytology 部分）245 點，備註：**同一病人 3–6 個月內限做 1 次，但「曾罹患過子宮頸癌或癌前病變之婦女」「最近一次子宮頸抹片檢查結果為異常之婦女」等 6 個月內需重做者為適應症**——即治療後與異常後的追蹤抹片有給付依據 [S35]
- LEEP 的專項與耗材差額：給付項目檔以「conization」涵蓋（laser 比照），**LEEP 專項與自費差額查無獨立條文**→寫「向醫務課或個管師確認」。
- 原位癌／CIN3 不在重大傷病清單（見 A4）；追蹤的公費抹片政策見 A4 台灣端（D3 主用）。

## 圖表數據（fig-cx-cin-ladder）

| 階梯 | 消退 | 持續 | 進展 | 時間軸／族群標籤 | 處置（ASCCP/ESGO） | 來源 |
|---|---|---|---|---|---|---|
| CIN 1（LSIL） | 約 60% | 約 30% | 10% →CIN3；1% →侵襲 | 合成近似值，無統一時間軸 | 觀察為首選；≥2 年持續才考慮治療 | [S1][S4] |
| CIN 2（HSIL 之一） | 50%（<30 歲 60%） | 32% | 18%（<30 歲 11%） | 24 個月，觀察世代 3,160 人 | 建議治療；生育考量下可條件式觀察（6 個月一次、最多 2 年） | [S2][S4] |
| CIN 3／原位癌（HSIL） | 33%（舊合成值） | — | **未治療 30 年 31.3%**（24 個月仍在者 50.3%）；治療得當 0.7% | 紐西蘭 1955–76 世代 1,063 人 | 一律切除治療（錐切/LEEP），無觀察選項 | [S1][S3][S4] |
| AIS | — | — | —（本次無可引用消退率） | — | 先診斷性錐切；子宮切除首選；保留生育需切緣陰性 | [S4] |
| 侵襲癌 IA1（≤3 mm） | — | — | — | — | 錐切切緣陰性即可為根治治療（LVSI 陰性） | [S8][S9] |
| 侵襲癌 IA2（>3–≤5 mm） | — | — | — | — | 錐切（切緣陰性）或單純子宮切除 | [S8][S9] |
| ≥IB（>5 mm 或可見病灶） | — | — | — | — | 進入分期與治療分流 → 見 A2、B1 | [S9] |

圖注建議：「示意圖，各階數據依 Östör 1993、Tainio 2018（BMJ）、McCredie 2008（Lancet Oncol）與 ASCCP 2019 重繪；CIN 2 為 24 個月觀察數據、CIN 3 為未治療世代 30 年數據，時間軸不同。」

---

# A2 — 分期靠內診和影像，不是開刀看

**Key facts**

*FIGO 2018 改了什麼（Bhatla 2019 修訂論文摘要原文）*
- 允許把**影像與病理**納入分期：「allowing incorporation of imaging and/or pathological findings, and clinical assessment of tumor size and disease extent」[S10]
- IA 期取消水平寬度的要求（只看深度）；IB 拆成三個亞期：IB1（深度 ≥5 mm 且 <2 cm）、IB2（2–4 cm）、IB3（≥4 cm）[S10]
- 淋巴結轉移直接進 IIIC：骨盆腔淋巴結＝IIIC1、主動脈旁＝IIIC2；用什麼方法定的要註記——影像＝r、病理＝p [S10]
- 「Routine investigations and other methods (e.g., examination under anesthesia, cystoscopy, proctoscopy, etc.) are **not mandatory** and are to be recommended based on clinical findings and standard of care」——麻醉下內診與膀胱鏡不再是必經流程 [S10]
- 為什麼子宮頸癌是臨床／影像分期而不是開刀分期：修訂的設計原則是「applicable to all resource levels」——這個癌別全球多數病人在不能開刀也不該開刀的期別與環境被診斷，分期系統必須不依賴手術標本 [S10]；FIGO 2021 增補：IB 進一步細分為 ≤2 cm／>2–≤4 cm／>4 cm，微轉移也算 IIIC [S9]
- 完整分期表（IA≤5 mm、IA1≤3 mm、IA2>3–≤5 mm、IIA 上 2/3 陰道、IIB 參數、IIIA 下 1/3 陰道、IIIB 骨盆壁或腎積水、IVA 鄰近器官、IVB 遠端）逐字見 FIGO 2021 開放取用版 Table 1 [S9]

*每種工具各自決定什麼*
- ESGO 2023 原文：「Pelvic magnetic resonance imaging (MRI) is **mandatory** for initial assessment of pelvic tumor extent and to guide treatment options（T1a 錐切切緣陰性者除外）」；訓練有素者的經陰道／經直腸超音波是選項；「Cystoscopy or proctoscopy are not routinely recommended [IV, D]」[S8]
- MRI 看參數侵犯的能力（Woo 2018 統合分析，14 個研究、1,028 人，以手術病理為金標準）：敏感度 76%（95% CI 67–84）、特異度 94%（91–95）——「MRI 說沒侵犯」比「MRI 說有」更可靠，判讀報告時方向要對 [S12]
- 淋巴結：早期以手術病理分期為標準（T1a1/T1a2 無 LVSI 除外）；局部晚期（T1b3 以上或影像可疑）建議 **PET-CT**（沒有就胸腹 CT）評估淋巴結與遠端；「PET-CT is recommended before chemoradiotherapy (CTRT) with curative intent [III, B]」[S8]
- PET 的盲點（ACRIN6671/GOG0233 前瞻多中心試驗，153 名晚期病人、以淋巴結清除病理為金標準）：PET-CT 偵測**主動脈旁／腹部**淋巴結轉移的敏感度只有 **50%**（0.44–0.56）、特異度 85%；骨盆腔敏感度 83%、特異度 63%——**影像乾淨不等於淋巴結乾淨**，小於偵測極限的轉移照不出來 [S13]
- PET-CT vs MRI 找淋巴結（He 2022 統合分析，11 個研究）：PET-CT 敏感度 0.65／特異度 0.93，MRI 敏感度 0.58／特異度 0.91；PET-CT 的 AUC 較高（0.824 vs 0.702）——兩種工具都會漏，PET-CT 略勝 [S14]
- 影像定 N 的後果要註記 r：Wright（NCDB 62,212 人）驗證顯示 IIIC 是極異質的一群（見下）[S11]

*每一期大概是什麼處境（數字給「讀報告」用，治療分流本體 → B1）*
- Wright 2019（美國 NCDB 2004–2015、62,212 人，以 FIGO 2018 重新歸期）：5 年存活 IB1 91.6%、IB2 83.3%、IB3 76.1%——IB 三分法確實把預後分開了 [S11]
- 同一分析的誠實面：**IIIC1（骨盆腔淋巴結陽性）5 年存活 60.8%，比 IIIA（40.7%）和 IIIB（41.4%）都好**；IIIC2 為 37.5%——期別數字變大不再等於預後一定變差，因為 IIIC 混合了局部小腫瘤＋單顆淋巴結到局部大腫瘤＋多顆淋巴結的各種組合 [S11]
- 分流一句話（歸 B1 展開）：ESGO——T1b1/T1b2/T2a1 淋巴結陰性者「Radical surgery by a gynecological oncologist is the preferred treatment modality」；治療策略應**避免手術與放療兩種都做**（高併發症）；T1b3 以上走根治性化放療（證據與選擇 → B1、B3、C1）[S8]

*腫瘤標記的誠實段（SCC-Ag）*
- Charakorn 2018 統合分析（61 個研究）：治療前 SCC-Ag 高 vs 低，復發 RR 2.44（1.91–3.13）、死亡 RR 3.66（2.24–5.98）——它與預後**相關** [S15]
- 但它不能拿來定分期或代替影像：SCC-Ag 預測淋巴結轉移的敏感度 0.70、特異度 0.63（Zhou 2017 統合分析，17 組資料、3,985 人，AUC 0.73，且切點不一、異質性高）[S16]
- ESGO 2023 指引全文（本組以 fullTextXML 逐字檢索「SCC」「tumor marker」）**沒有任何一條**把腫瘤標記列入必要的分期或追蹤項目 [S8]——「SCC-Ag 正常」不能當成「沒有病」的證據，「偏高」也不是一個期別

**Claim ceiling**

Defensible：
- 「子宮頸癌的期別是內診加影像定的，不是開刀開進去看的——這是 FIGO 分期系統的設計，因為它必須在全世界任何資源條件下都能用；2018 年起影像與病理正式可以納入。」[S10]
- 「MRI 是看局部（腫瘤多大、有沒有吃到參數）的必要檢查；PET-CT 是進到局部晚期之前看淋巴結和遠端的建議檢查。」[S8]
- 「影像會漏：PET-CT 找主動脈旁淋巴結轉移，前瞻試驗量出來的敏感度只有五成——所以醫師說『影像上沒看到』而不是『確定沒有』，那不是含糊，是誠實。」[S13][S14]
- 「IB 拆成三級後預後分得很開（5 年 91.6%／83.3%／76.1%）；但 IIIC1 的 5 年存活其實比 IIIA/IIIB 高——**期別是治療的地圖，不是壽命的判決書**。」[S11]
- 「SCC-Ag 高低跟預後相關，但它定不了期、也排除不了病；國際指引沒有把它列為必要檢查。」[S8][S15][S16]
- 「麻醉下內診、膀胱鏡、直腸鏡不再是每個人必做，由臨床發現決定。」[S8][S10]

Would overstate：
- ✗「r 分期（影像）跟 p 分期（病理）一樣準。」——r/p 註記存在的理由正是兩者不等價 [S10][S13]
- ✗「PET 沒照到就是沒轉移。」——敏感度 50–83%，範圍要寫 [S13][S14]
- ✗「MRI 說有參數侵犯就是 IIB。」——特異度 94% 仍有偽陽性，且敏感度 76% 會漏；最終是內診＋影像＋團隊討論的綜合判斷 [S8][S12]
- ✗「IIIC1 存活比 IIIB 好，所以淋巴結轉移沒關係。」——Wright 的解讀是 IIIC 異質，不是淋巴結無害 [S11]
- ✗ 用 SCC-Ag 數值變化下任何治療結論——A2 只建立「它是什麼、不是什麼」；追蹤怎麼用 → D3/D4
- ✗ 寫出「哪一期該開刀哪一期該放療」的完整對照——那是 B1 的紅線 2 主場，A2 只留一句話與指路

**Caveats / safety notes**

- Wright 是美國資料庫、2004–2015 診斷、以當年資料重新歸期的回溯驗證；5 年存活數字帶「美國 NCDB」標籤，不可寫成台灣數字。
- Woo 統合分析以手術病理為金標準→族群偏早期（能開刀的人），外推到局部晚期的參數判讀要保守。
- ACRIN6671/GOG0233 的族群是「晚期、計畫做主動脈旁淋巴結清除」者；50% 敏感度是腹部（主動脈旁／總髂）區域、以病人為單位、平均七位判讀者的結果——標籤要帶。
- He 2022 的統合異質性未完全交代（切點、機型年代不一）；用「兩者都會漏、PET-CT 略優」的方向句，不要精確到小數點比大小。
- 分期名詞由 A2 完整解釋（SPEC §五），A1/B 組引用時不重新定義；IIIC 的 r/p 註記在 B 組寫治療時要沿用。
- 「開刀還是放療」的所有療效數字（含 Landoni）一個都不出現在 A2。

**Taiwan status**

- **正子造影是健保給付項目且適應症明列子宮頸癌**：給付項目檔 26072B 正子造影-全身 36,500 點、26073B 正子造影-局部 26,500 點，備註原文：「…頭頸部癌(不包含腦瘤)、原發性肺癌、黑色素癌、甲狀腺癌及**子宮頸癌之分期及懷疑復發或再分期**」，但有前提：「經電腦斷層、核磁共振、核子醫學掃瞄等檢查仍無法分期者，或認定電腦斷層、核磁共振等檢查不足以提供足夠資訊以供治療所需者，且須於病歷中說明施行正子造影之必要性理由」「不得用於例行之追蹤檢查」[S35]——即**台灣的健保 PET 是「CT/MRI 不夠用時」的條件給付**，自費做 PET 的情境寫「向醫務課確認」。
- MRI：33084B 磁振造影-無造影劑 6,500 點、33085B 有造影劑 11,500 點（「限經保險人同意之醫療院所實施」「申報費用時必須附上報告結果」）；CT：33070B–33072B 3,800–5,035 點 [S35]。
- SCC 腫瘤標記是健保檢驗項目：12080B「SCC腫瘤標記 (EIA/LIA法)」400 點，給付項目檔無附帶限制條文 [S35]——「有給付」可寫，但臨床價值照上面的證據寫。
- 台灣醫院是否常規做麻醉下內診（EUA）：查無可引用的官方或學會文件 → gap，寫「各院做法不同，以你的主治醫師安排為準」。

---

# A3 — HPV：感染很常見，癌變很少見　【紅線 3：不究責】

**Key facts**

*感染有多常見（「~80%」的真正出處）*
- 「一生中八成的人會感染」的可引用來源是 Chesson 2014（美國 CDC 的模型估計，基於終生性伴侶數分布與每段關係的傳染機率，疫苗時代之前）：**有過至少一位異性伴侶者，女性終生感染機率 84.6%（範圍 53.6–95.0）、男性 91.3%（69.5–97.7）；八成以上的人在 45 歲前已感染過** [S17]——注意這是模型推估不是實測世代，但作者指出與世代研究的高累積發生率一致
- 實測：美國大學女生前瞻世代（608 人、每 6 個月採檢）36 個月累積感染發生率 43%（95% CI 36–49）[S18]

*多數清除（timeline 圖的第一個分岔）*
- 新感染的中位持續時間 8 個月（95% CI 7–10）[S18]
- 哥斯大黎加 Guanacaste 世代（599 名女性、800 個致癌型感染）：**12 個月內 67%（63–70）清除** [S19]
- ALTS 世代（4,504 名 ASC-US/LSIL 細胞學異常者）：**24 個月內 91%（90–92）的既有感染清除**；感染已持續越久、再持續的機率越高（新發現的感染再持續 6 個月的機率 37%，已持續 ≥18 個月者 65%）[S20]

*少數持續→癌前病變→癌（timeline 圖的主軸，紅線 3 的證據本體）*
- 持續 ≥12 個月的感染，30 個月內被診斷 CIN2+ 的風險 21%（15–28）；30 歲以下、HPV-16 持續 ≥12 個月者最高，53%（29–76）[S19]
- Schiffman 2007（Lancet 回顧）原文：「Persistent infections and precancer are established, **typically within 5–10 years**, from less than 10% of new infections. **Invasive cancer arises over many years, even decades**, in a minority of women with precancer, with a peak or plateau in risk at about 35–55 years of age」[S21]
- 從 CIN2/3 到侵襲癌的時間（Vink 2013，荷蘭全國登記 2000–2005 的數學模型，雙重設限資料）：**中位數 23.5 年（95% CI 20.8–26.6）；10 年內進展到癌的只有 1.6%**（HPV16 陽性病灶 2.4%、陰性 0.6%）[S22]
- 未治療 CIN3 的 30 年累積侵襲風險 31.3%——即使已經走到癌前病變的最後一格，「變成癌」也還是以十年計的少數 [S3]
- 型別：全球侵襲癌檢體研究（38 國、10,575 例、8,977 例 HPV 陽性）：**HPV 16＋18 佔 71%**（70–72）；16/18/31/33/35/45/52/58 八型合計 91%；腺癌中 16/18/45 佔 94% [S23]

*「是誰傳給我的」為什麼無法回答（CDC 2021 逐字，紅線 3 的直接彈藥）*
- 「Partners tend to share HPV, and **it is not possible to determine which partner transmitted the original infection. Having HPV does not mean that a person or his or her partner is having sex outside the relationship**」[S25]
- 「**Time of HPV acquisition cannot be definitively determined**」[S25]
- 「HPV tests might become positive **many years after initial exposure due to reactivation of latent infections** in both male and female partners. Having an HPV infection should not raise concerns about a male partner's health」[S25]
- 潛伏再活化的實證（Rositch 2012，700 名 35–60 歲女性、兩年追蹤）：**85%（155/183）的新檢出 HPV 發生在無性行為或單一伴侶期間**；只有 13% 可歸因於新伴侶，72% 可歸因於終生 ≥5 位伴侶的既往暴露（HR 4.1，2.0–8.4）——**在中年女性，「驗出 HPV」多半是過去的感染再度可測，不是最近有人帶進來** [S24]

*伴侶要不要驗、要不要打（照證據寫）*
- CDC 2021 逐字：「**Sex partners do not need to be tested for HPV**」「These tests should not be used for male partners of women with HPV」——男性伴侶檢測不被建議，也沒有核准用於男性的 HPV 檢測 [S25]
- 伴侶接種：疫苗對男性本人有效（4 價疫苗第三期試驗，4,065 名 16–26 歲男性：預防疫苗型別外生殖器病灶，per-protocol 效力 90.4%〔69.2–98.1〕）[S27]；美國 ACIP：26 歲以下建議補接種；**27–45 歲不做常規建議、改為共同臨床決策**——因為多數人已暴露過、對已感染的型別沒有治療效果，新獲益隨年齡下降 [S26]
- 保險套：正確且持續使用「might lower the risk」且可能縮短清除時間，但 HPV 可感染未覆蓋的部位，不能完全防護 [S25]

*不是「跟性行為無關」（紅線 3 的反向界線）＋吸菸這個可控因子*
- 感染本身與性行為相關：伴侶數、性頻率等都是感染的危險因子 [S17][S18]——誠實的寫法是「感染與性行為有關，但發病的時間軸讓『用發病推論近期行為』不成立」
- 吸菸是明確的輔因子（IARC 國際合作重分析，23 個研究、13,541 名個案 vs 23,017 名對照）：**目前吸菸者的鱗狀細胞癌風險 RR 1.60（1.48–1.73）**；限 HPV DNA 陽性女性的分析 RR 1.95（1.43–2.65）；有劑量效應（每日支數、起始年齡）；腺癌無關聯 [S28]——「戒菸」是確診後病人自己能動的少數危險因子

**Claim ceiling**

Defensible：
- 「有過性經驗的人，一生感染過 HPV 的機率以模型估計約八到九成——它是『有過性生活』的常態，不是特定行為的印記。」[S17]
- 「九成的感染兩年內自己清掉；持續超過一年的那一小群，才需要盯。」[S19][S20]
- 「從持續感染到癌前病變通常要 5–10 年；從癌前病變到癌，荷蘭全國資料的模型估計中位數是 23.5 年，10 年內就走完的不到 2%。**用今天的診斷去推論伴侶近期的行為，在生物學上不成立。**」[S21][S22]
- 「美國 CDC 的指引寫得很直接：無法判定是誰傳給誰、也無法判定何時感染；驗出 HPV 不代表任何一方有外遇；中年之後驗出陽性，多半是多年前的感染再度可測。」[S24][S25]
- 「伴侶不需要去驗 HPV——指引不建議，市面上也沒有核准給男性用的檢測。」[S25]
- 「伴侶要不要打疫苗：45 歲以下可以跟醫師談，效益主要在他自己還沒感染過的型別；疫苗對已經存在的感染沒有治療效果。」[S26][S27]
- 「吸菸讓鱗癌風險增加約六成，是你自己能改變的輔因子。」[S28]

Would overstate：
- ✗ 任何可以被讀成「可以用發病推論伴侶近期不忠」的句子——紅線 3，直接失敗
- ✗ 反向：「HPV 跟性行為無關」「這是空氣傳染」——感染的危險因子研究清楚指向性接觸 [S17][S18]；紅線 3 條文明定不准這樣寫
- ✗「從感染到癌一定超過十年。」——Vink：10 年內 1.6%（HPV16 陽性 2.4%）非零 [S22]；寫「通常以十年計」不寫「一定」
- ✗「八成」寫成實測數字——它是模型估計，帶「估計」二字 [S17]
- ✗「清除了就永遠沒事。」——潛伏與再活化正是 Rositch 的發現；清除（clearance）在檢測上是「測不到」，不保證病毒徹底離開 [S24][S25]
- ✗「伴侶打疫苗可以保護你（病人本人）。」——本次查證沒有「伴侶接種改善患者預後」的證據；只能寫伴侶自身的保護 [S26][S27]
- ✗「戒菸就不會復發。」——RR 1.60 是發生風險不是復發風險；戒菸寫成「能動的因子」不寫成治療

**Caveats / safety notes**

- 這一篇語氣最軟、事實不軟：每個「不究責」的句子都要掛在可引用的來源上（CDC 逐字、Rositch 的 85%、Vink 的 23.5 年），不要用作者的口吻單獨扛。
- Chesson 是美國、疫苗前時代的模型；Ho 是大學女生；Rodríguez 是哥斯大黎加世代；Plummer 是細胞學異常（ASC-US/LSIL）族群——清除率數字各帶族群標籤，不混用。
- Vink 的 23.5 年是統計模型（雙重設限資料）而非直接觀察，句子裡帶「模型估計」。
- Rositch 的族群是 35–60 歲美國女性；年輕族群的新感染仍以新暴露為主（13% vs 72% 的歸因是這個族群的數字）。
- 「92% 由 HPV 引起」之類的歸因分數本次未查證，型別分布用 de Sanjosé 的 71%／91% [S23]。
- 與 A1 銜接：CIN 的處置一句話指向 A1；與 D3 銜接：治療後要不要打疫苗、女兒的公費疫苗 → D3。
- 吸菸段不可滑向責備（「你抽菸才得病」）——它是輔因子，主因是持續感染；放在「接下來能做什麼」的段落。

**Taiwan status**

- 台灣公費 HPV 疫苗：自 107 年起全國國中女生公費接種（國健署），**114 年起擴大為國中男女生皆可接種**，現行使用 9 價疫苗、9–14 歲兩劑（嘉義市政府衛生局頁面原文，其上游為國健署政策）[S37]——**此事實 D3 主用（女兒的疫苗），A3 只在伴侶段落一句話**：成人／伴侶接種在台灣為自費，適應症至 45 歲 [S37]。
- 成人自費接種的費用：查無全國統一價 → 寫「向醫療院所或藥師確認」。
- HPV 檢測（35／45／65 歲公費）與抹片政策 → 見 A4 台灣端（D3 主用）。
- 台灣曾自 99 年 8 月起提供「HPV 自我採檢套組」給 36 歲以上且 6 年以上未做抹片、及 30 歲以上身心障礙婦女（衛生所索取；當年檢出 HPV 陽性率約 8%）[S36]——**這是 2010 年的公告**；現行（114 年）HPV 檢測服務是否含自採選項，查無官方條文（見 S39 FAIL）→ 寫「自採管道以衛生所與國健署現行公告為準」。

## 圖表數據（fig-cx-hpv-timeline）

| 時間軸節點 | 數字 | 族群／方法標籤 | 來源 |
|---|---|---|---|
| 感染：終生累積 | 女性約 84.6%、男性約 91.3%（模型估計）；45 歲前 >80% | 美國、疫苗前、≥1 位異性伴侶 | [S17] |
| 感染：3 年累積 | 43% | 美國大學女生世代 608 人 | [S18] |
| 清除：中位持續 | 8 個月 | 同上 | [S18] |
| 清除：12 個月 | 67% | Guanacaste 世代 800 個致癌型感染 | [S19] |
| 清除：24 個月 | 91% | ALTS 世代 4,504 人（細胞學異常族群） | [S20] |
| 持續 ≥12 個月 → CIN2+（30 個月內） | 21%；HPV16 且 <30 歲：53% | Guanacaste | [S19] |
| 持續感染 → 癌前病變成形 | 通常 5–10 年內、發生於 <10% 的新感染 | Schiffman 2007 回顧原文 | [S21] |
| CIN2/3 → 侵襲癌 | 中位 23.5 年；10 年內 1.6%（HPV16+ 2.4%） | 荷蘭全國登記模型 | [S22] |
| 未治療 CIN3 → 侵襲癌 | 30 年 31.3%（持續病灶者 50.3%）；治療得當 0.7% | 紐西蘭世代 | [S3] |
| 癌症風險高峰年齡 | 約 35–55 歲 | Schiffman 2007 | [S21] |
| 型別 | HPV16+18 佔侵襲癌 71%；八型合計 91% | 全球 38 國檢體研究 | [S23] |
| 中年新檢出的歸因 | 85% 發生於無性行為或單一伴侶期間；72% 歸因於既往暴露 | 美國 35–60 歲女性 700 人 | [S24] |

圖注建議：「示意圖，依 Chesson 2014、Rodríguez 2008、Plummer 2007、Schiffman 2007、Vink 2013、McCredie 2008 等重繪；各節點族群與方法不同，時間軸為概念性整合。」

---

# A4 — 確診之後的第一個月會怎麼走

**Key facts**

*會遇到哪些人（分工）*
- ESGO 2023：治療計畫應在多專科基礎上制定（「generally at a **tumor board** meeting」）[IV, A]；照護集中到專門中心與轉診網絡 [IV, B]；相關專科含婦科腫瘤、放射腫瘤、腫瘤內科、病理、影像 [S8]
- 台灣的制度面：國民健康署自民國 97 年推動「**癌症診療品質認證**」，通過認證的醫院必須「打破過去各科醫師獨立作戰的模式……集結腫瘤內外科、放射腫瘤科、病理科、影像診斷科及**腫瘤個案管理師**等組成跨科別團隊，藉由多專科之間的定期開會，充分討論並確認每位病人的檢查結果」；113 年公告全臺 67 家醫院通過認證、85% 以上癌症病人於認證醫院接受治療 [S33]——即「你的案子會被一群人看過」在認證醫院是制度要求，不是額外服務
- 個案管理師（個管師）是認證團隊的固定成員 [S33]——病人的單一窗口

*確診到治療前，會做哪些事（對照 A2 的工具）*
- 診斷必要項目：內診＋切片（±陰道鏡）；骨盆 MRI 為必要（T1a 錐切切緣陰性者除外）；局部晚期或影像可疑者加 PET-CT（無則胸腹 CT）；膀胱鏡／直腸鏡不再常規 [S8][S10]；細節與各工具的意義 → A2
- T1a 的「分期」本身就是一次小手術（錐切）＋專家病理判讀 [S8][S9]——「為什麼還要再切一次」的答案在這裡
- 麻醉下內診（EUA）：FIGO 2018 起非強制、依臨床判斷 [S10]；台灣各院做法查無可引用文件（gap）

*排程等待的誠實段（等兩三週會不會出事）*
- 台灣全國性研究（Chen 2019，串接 2004–2010 癌症登記與健保資料，9,693 名新診斷子宮頸癌病人）：**96.37% 在確診後 90 天內開始治療**；調整後，90–180 天才開始者死亡風險 HR 1.33（1.02–1.72）、>180 天 HR 1.36（1.12–1.65）——**傷害出現在拖過三個月之後，資料裡看不到「晚兩週就變差」的訊號** [S29]
- 以色列單中心世代（321 人，1999–2010）：診斷到治療 ≤30 天／30–45 天／>45 天三組的 3 年存活無差異（74.6%／82.2%／80.8%，P=0.38）；作者結論：**病人若需要生育或卵巢保存的程序，在開始治療前留出時間是可接受的** [S30]——與 B4 的時效性紅線同向（要做生育保存就趁這個窗口，見 B4）
- 反向界線：一旦開始放療就不可拖（總治療時間 → C2 主場，此處一句話指路）

*重大傷病證明（行政主場）*
- 依「全民健康保險保險對象免自行負擔費用辦法」第二條附表一（114 年 1 月 1 日以後適用版，官方 PDF）：第一大類「需積極或長期治療之癌症」，其中「**(四) 子宮頸惡性腫瘤第一期（ICD-10 C53.0–C53.9、C55）：證明有效期限三年**」；「(五) 除(一)–(四)之其他惡性腫瘤：**五年**」——即第一期的重大傷病證明效期 3 年、第二期以上 5 年，到期仍符合可申請延長 [S34]
- **原位癌（CIN3／AIS，ICD-10 D06）不在重大傷病清單內**（清單之癌症類以 C 碼定義，全文檢索無原位癌／D06 項目）[S34]——「原位癌不是癌」在行政上的對應：錐切治療原位癌不會有重大傷病證明，但相關診療仍屬健保常規給付（A1 台灣端）
- 重大傷病證明的效果：該辦法名稱所示——就該傷病之相關診療**免自行負擔費用**（部分負擔）[S34]；申請實務（通常由醫院代辦、醫師開立診斷）寫「由個管師或醫院服務台協助」，細節向健保署或醫院確認

*台灣篩檢政策這條線怎麼交（D3 主場、A4 一句話）*
- 【D3 主用】114 年 1 月 1 日起擴大：**增列 25–29 歲女性每 3 年 1 次公費子宮頸抹片**（補助由 430 元調為 630 元）；**新增 35 歲、45 歲、65 歲女性當年度 1 次公費 HPV 檢測**（每案補助 1,400 元）；30 歲以上女性維持每年可做 1 次公費抹片、官方建議至少每 3 年 1 次 [S31][S32]
- 【D3 主用】防治成效脈絡：自民國 84 年提供免費抹片以來，標準化發生率從每十萬 25.2 降至 111 年的 7.6、死亡率從 11 降至 112 年的 2.9（降幅超過七成）；政策對齊 WHO 2030「90-70-90」消除子宮頸癌戰略 [S32]
- 【A4 的一句話版本】「你的診斷不代表篩檢白做了，也與你何時做過抹片無關——但你的女性家人可以用 114 年起放寬的公費篩檢」＋指向 D3

**Claim ceiling**

Defensible：
- 「在通過癌症診療品質認證的醫院，跨科團隊討論與個管師是制度要求；全台 67 家認證醫院涵蓋 85% 以上的癌症病人。」[S33]
- 「第一個月的主要工作是把期別定清楚：內診、切片、MRI，需要時加 PET-CT——每一項各自回答一個治療需要的問題。」[S8][S10]
- 「台灣的全國資料：96% 的病人在確診後 90 天內開始治療；風險升高出現在拖過 90 天之後。**用兩三週把檢查做完、把團隊會議開完，不是在浪費你的時間窗。**」[S29]
- 「需要談生育保存的人，這個檢查期正是唯一的窗口——證據顯示為此留出數週是可接受的（詳見 B4）。」[S30]
- 「子宮頸癌（侵襲癌）屬重大傷病：第一期證明效期 3 年、其他期別 5 年，相關診療免部分負擔；原位癌不在重大傷病清單，因為它還不是癌。」[S34]

Would overstate：
- ✗「等多久都沒關係。」——90–180 天 HR 1.33、>180 天 HR 1.36；「不用急」的上限是「不拖過該做完檢查的時間」[S29]
- ✗「30 天內一定要開始治療，否則會惡化。」——兩個世代研究都不支持這種門檻；不准發明天數 [S29][S30]
- ✗「每家醫院都有 MDT。」——制度要求綁在「通過認證的醫院」；寫認證制度，不寫成全稱句 [S33]
- ✗「重大傷病＝醫療全免費。」——免的是該傷病相關診療的部分負擔；自費項目（部分影像、自費藥材）不在其內；細節向醫務課確認 [S34]
- ✗ 列出「第一個月標準檢查清單」含抽血項目與時程表——本次查證只有影像與病理的指引條文；抽血、麻醉評估等寫「依各院流程」，不可虛構清單
- ✗ 篩檢政策展開超過一句話——D3 主場（SPEC §五收束）

**Caveats / safety notes**

- Chen 2019 的分組是 <90／90–180／>180 天，資料年代 2004–2010、含所有期別與治療方式；不能反推「89 天等於安全」——寫成「資料裡的傷害訊號出現在三個月之後」即可。適應症干擾（拖très久的人常是處境更難的人）與 colon 簡報 B3 的 Biagi 同型，寫法比照：連續的斜率，不是懸崖。
- Perri 2014 是單中心、321 人、以色列，檢定力有限；用來支持「生育保存值得留時間」，不用來支持「等 45 天沒關係」。
- 癌症診療品質認證的「認證基準」全文（含 MDT 的條文編號）本次未取得（S42 FAIL）；引用停在 MOHW 新聞頁的描述層級，不可引用具體基準條號。67 家是 113 年公告數字，會變動，帶年份。
- 重大傷病之 PDF 為 114-01-01 適用版；「第一期效期 3 年」是此版的分類（甲狀腺、口腔口咽下咽第一期、乳房第一期、子宮頸第一期同列 3 年）——舊版是否相同未查，引用時鎖定「114 年起適用」。
- 「排程」的院內實際天數（門診到 MRI、到團隊會議的等待日數）查無可引用資料 → 不寫具體天數，寫「向個管師要時間表」。
- 收尾方向（A 組）：「下次門診問出口的問題」——四篇標題互異，A4 可收在「第一次見團隊時，值得直接問的三件事」之類（與 A1–A3 的收尾句區隔，撰稿時再定）。

**Taiwan status**

- 重大傷病：見 Key facts（S34，官方 PDF 已逐字驗證）。申請流程細節（醫院代辦、審查天數）查無官方逐字 → 寫「由個管師協助、向健保署確認」。
- 癌症診療品質認證與 MDT：S33（MOHW 新聞頁，113-03-19 建檔）。
- 篩檢政策（D3 主用）：S31（113-12-24 建檔）、S32（114-05-08 建檔、114-05-22 更新）。
- 診斷相關健保項目（陰道鏡、切片、錐切、MRI、PET）：見 A1／A2 台灣端（S35）。
- 全台癌症資源中心與免付費專線 0809-010580 已由 C 組查證（C 簡報 S35/S36，2026-08-30 覆核仍在）——A4 需要時引 C 組已驗來源，不重複查證、不重寫。

---

## Sources（單一編號序列；PASS 除非標 FAIL）

- **[S1] PASS** — Ostör AG. (1993). *Natural history of cervical intraepithelial neoplasia: a critical review.* Int J Gynecol Pathol 12(2):186-192. PMID 8463044（無 DOI）. URL: https://europepmc.org/article/MED/8463044 — CIN1 60/30/10/1、CIN2 40/40/20/5、CIN3 消退 33%／進展 >12%；「形態學無法預測個別病人」。Route: Europe PMC REST (TITLE)
- **[S2] PASS** — Tainio K, Athanasiou A, Tikkinen KAO, et al. (2018). *Clinical course of untreated cervical intraepithelial neoplasia grade 2 under active surveillance: systematic review and meta-analysis.* BMJ 360:k499. PMID 29487049, PMC5826010, doi 10.1136/bmj.k499. URL: https://doi.org/10.1136/bmj.k499 — 36 研究 3,160 人；24 個月 50/32/18；<30 歲 60/23/11；失聯約 10%。Route: Europe PMC REST
- **[S3] PASS** — McCredie MR, Sharples KJ, Paul C, et al. (2008). *Natural history of cervical neoplasia and risk of invasive cancer in women with cervical intraepithelial neoplasia 3: a retrospective cohort study.* Lancet Oncol 9(5):425-434. PMID 18407790, doi 10.1016/s1470-2045(08)70103-7. URL: https://doi.org/10.1016/s1470-2045(08)70103-7 — 1,063 名覆核 CIN3；未治療 30 年 31.3%（22.7–42.3）、持續病灶者 50.3%、治療適當者 0.7%；「CIN3; also termed stage 0 carcinoma」。Route: Europe PMC REST
- **[S4] PASS** — Perkins RB, Guido RS, Castle PE, et al.; 2019 ASCCP Risk-Based Management Consensus Guidelines Committee. (2020). *2019 ASCCP Risk-Based Management Consensus Guidelines for Abnormal Cervical Cancer Screening Tests and Cancer Precursors.* J Low Genit Tract Dis 24(2):102-131. PMID 32243307, PMC7147428, doi 10.1097/lgt.0000000000000525. URL: https://doi.org/10.1097/lgt.0000000000000525 — CIN1 觀察首選、CIN3 觀察不可接受、CIN2 條件式觀察、切除優於消融、AIS 全套（SGO 建議採納：診斷性錐切、標本完整 ≥10 mm、子宮切除首選、切緣陽性再切）、expedited treatment 閾值（≥60% preferred／25–60% acceptable）、治療後 6 個月 HPV 檢測＋3 年一次至少 25 年、p16 不可把 CIN1 升級。Route: Europe PMC REST (TITLE) + fullTextXML(PMC7147428) grep 原文（2021 年有 erratum，PMID 34542089，未涉本簡報引用段落）
- **[S5] PASS** — Arbyn M, Redman CWE, Verdoodt F, et al. (2017). *Incomplete excision of cervical precancer as a predictor of treatment failure: a systematic review and meta-analysis.* Lancet Oncol 18(12):1665-1679. PMID 29126708, doi 10.1016/s1470-2045(17)30700-3. URL: https://doi.org/10.1016/s1470-2045(17)30700-3 — 97 研究 44,446 人；切緣陽性 23.1%；殘存/復發 CIN2+ 6.6%；RR 4.8（3.2–7.2）；HPV 檢測敏感度 91.0% vs 切緣 55.8%；HPV 陰性後風險 0.8%、切緣陰性 3.7%。Route: Europe PMC REST（摘要全文分兩次取回）
- **[S6] PASS** — Kalliala I, Athanasiou A, Veroniki AA, et al. (2020). *Incidence and mortality from cervical cancer and other malignancies after treatment of cervical intraepithelial neoplasia: a systematic review and meta-analysis of the literature.* Ann Oncol 31(2):213-227. PMID 31959338, PMC7479506, doi 10.1016/j.annonc.2019.11.004. URL: https://doi.org/10.1016/j.annonc.2019.11.004 — 27 研究；治療後子宮頸癌 39/10 萬人年、RR 3.30（2.57–4.24）、升高持續 ≥20 年；陰道 10.84／外陰 3.34／肛門 5.11。Route: Europe PMC REST
- **[S7] PASS** — Darragh TM, Colgan TJ, Cox JT, et al.; Members of LAST Project Work Groups. (2012). *The Lower Anogenital Squamous Terminology Standardization Project for HPV-Associated Lesions: background and consensus recommendations from the College of American Pathologists and the American Society for Colposcopy and Cervical Pathology.* J Low Genit Tract Dis 16(3):205-242. PMID 22820980, doi 10.1097/lgt.0b013e31825c31dd. URL: https://doi.org/10.1097/lgt.0b013e31825c31dd — LSIL/HSIL 兩級制統一名詞、生物標記使用原則。Route: Europe PMC REST（另有 Int J Gynecol Pathol 2013 同文版本 PMID 23202792）
- **[S8] PASS** — Cibula D, Raspollini MR, Planchamp F, et al. (2023). *ESGO/ESTRO/ESP Guidelines for the management of patients with cervical cancer — Update 2023.* Int J Gynecol Cancer 33(5):649-666. PMID 37127326, PMC10176411, doi 10.1136/ijgc-2023-004429. URL: https://doi.org/10.1136/ijgc-2023-004429 — 本組獨立重驗（與 C 簡報 S7 同來源）：骨盆 MRI 必要、膀胱鏡/直腸鏡非常規、PET-CT 於 LACC 與 CTRT 前建議、T1a 診斷靠錐切、T1a1 錐切即根治（「hysterectomy does not improve the outcome」）、T1a2 錐切或 SH 足夠、切緣陽性再錐切、tumor board [IV, A]、避免手術＋放療雙重治療、T1b1–T2a1 手術首選之分流句；全文檢索 SCC／tumor marker＝0 條建議。Route: Europe PMC REST (TITLE+AUTH+PUB_YEAR) + fullTextXML via PMC10247855（Virchows Arch 同文版，PMID 37145263）grep 原文
- **[S9] PASS** — Bhatla N, Aoki D, Sharma DN, Sankaranarayanan R. (2021). *Cancer of the cervix uteri: 2021 update.* Int J Gynaecol Obstet 155(Suppl 1):28-44. PMID 34669203, PMC9298213, doi 10.1002/ijgo.13865. URL: https://doi.org/10.1002/ijgo.13865 — FIGO 2018 分期表逐字（IA≤5 mm、IA1≤3 mm、IA2>3–≤5 mm、IB1≤2 cm/IB2>2–≤4 cm/IB3>4 cm、IIIC 含微轉移）；IA1/IA2 診斷需涵蓋整個病灶的錐切標本。Route: Europe PMC REST + fullTextXML grep 原文
- **[S10] PASS** — Bhatla N, Berek JS, Cuello Fredes M, et al. (2019). *Revised FIGO staging for carcinoma of the cervix uteri.* Int J Gynaecol Obstet 145(1):129-135. PMID 30656645, doi 10.1002/ijgo.12749. URL: https://doi.org/10.1002/ijgo.12749 — 修訂內容：影像/病理可納入、IA 取消水平寬度、IB 三分、淋巴結→IIIC1/IIIC2、r/p 註記、EUA/膀胱鏡/直腸鏡非強制、「applicable to all resource levels」。Route: Europe PMC REST
- **[S11] PASS** — Wright JD, Matsuo K, Huang Y, et al. (2019). *Prognostic Performance of the 2018 International Federation of Gynecology and Obstetrics Cervical Cancer Staging Guidelines.* Obstet Gynecol 134(1):49-57. PMID 31188324, PMC7641496, doi 10.1097/aog.0000000000003311. URL: https://doi.org/10.1097/aog.0000000000003311 — NCDB 62,212 人；5 年存活 IB1 91.6%/IB2 83.3%/IB3 76.1%；IIIA 40.7%/IIIB 41.4%/IIIC1 60.8%/IIIC2 37.5%；IIIC 異質性結論。Route: Europe PMC REST
- **[S12] PASS** — Woo S, Suh CH, Kim SY, Cho JY, Kim SH. (2018). *Magnetic resonance imaging for detection of parametrial invasion in cervical cancer: An updated systematic review and meta-analysis of the literature between 2012 and 2016.* Eur Radiol 28(2):530-541. PMID 28726120, doi 10.1007/s00330-017-4958-x. URL: https://doi.org/10.1007/s00330-017-4958-x — 14 研究 1,028 人；敏感度 0.76（0.67–0.84）、特異度 0.94（0.91–0.95）；3T 與 DWI 可能改善。Route: Europe PMC REST
- **[S13] PASS** — Atri M, Zhang Z, Dehdashti F, et al. (2016). *Utility of PET-CT to evaluate retroperitoneal lymph node metastasis in advanced cervical cancer: Results of ACRIN6671/GOG0233 trial.* Gynecol Oncol 142(3):413-419. PMID 27178725, PMC4993667, doi 10.1016/j.ygyno.2016.05.002. URL: https://doi.org/10.1016/j.ygyno.2016.05.002 — 153 人、手術病理金標準；PET-DCT 腹部（主動脈旁/總髂）敏感度 0.50（0.44–0.56）／特異度 0.85；骨盆 0.83／0.63。Route: Europe PMC REST
- **[S14] PASS** — He T, Sun J, Wu J, et al. (2022). *PET-CT versus MRI in the diagnosis of lymph node metastasis of cervical cancer: A meta-analysis.* Microsc Res Tech 85(5):1791-1798. PMID 34981608, doi 10.1002/jemt.24039. URL: https://doi.org/10.1002/jemt.24039 — 11 研究；PET-CT 敏感度 0.65／特異度 0.93、MRI 0.58／0.91；PET-CT AUC 0.824 > MRI 0.702。Route: Europe PMC REST
- **[S15] PASS** — Charakorn C, Thadanipon K, Chaijindaratana S, et al. (2018). *The association between serum squamous cell carcinoma antigen and recurrence and survival of patients with cervical squamous cell carcinoma: A systematic review and meta-analysis.* Gynecol Oncol 150(1):190-200. PMID 29606483, doi 10.1016/j.ygyno.2018.03.056. URL: https://doi.org/10.1016/j.ygyno.2018.03.056 — 61 研究；治療前高 SCC-Ag：復發 RR 2.44（1.91–3.13）、死亡 RR 3.66（2.24–5.98）。Route: Europe PMC REST
- **[S16] PASS** — Zhou Z, Li W, Zhang F, Hu K. (2017). *The value of squamous cell carcinoma antigen (SCCa) to determine the lymph nodal metastasis in cervical cancer: A meta-analysis and literature review.* PLoS One 12(12):e0186165. PMID 29227998, PMC5724822, doi 10.1371/journal.pone.0186165. URL: https://doi.org/10.1371/journal.pone.0186165 — 17 組資料 3,985 人；預測淋巴結轉移敏感度 0.70／特異度 0.63／AUC 0.73；切點異質。Route: Europe PMC REST
- **[S17] PASS** — Chesson HW, Dunne EF, Hariri S, Markowitz LE. (2014). *The estimated lifetime probability of acquiring human papillomavirus in the United States.* Sex Transm Dis 41(11):660-664. PMID 25299412, PMC6745688, doi 10.1097/olq.0000000000000193. URL: https://doi.org/10.1097/olq.0000000000000193 — 模型估計：女性 84.6%（53.6–95.0）、男性 91.3%（69.5–97.7）；45 歲前 >80%。Route: Europe PMC REST
- **[S18] PASS** — Ho GY, Bierman R, Beardsley L, Chang CJ, Burk RD. (1998). *Natural history of cervicovaginal papillomavirus infection in young women.* N Engl J Med 338(7):423-428. PMID 9459645, doi 10.1056/nejm199802123380703. URL: https://doi.org/10.1056/nejm199802123380703 — 608 名大學女生；36 個月累積感染 43%（36–49）；中位持續 8 個月（7–10）；持續高危型 → 抹片異常 RR 37.2。Route: Europe PMC REST
- **[S19] PASS** — Rodríguez AC, Schiffman M, Herrero R, et al. (2008). *Rapid clearance of human papillomavirus and implications for clinical focus on persistent infections.* J Natl Cancer Inst 100(7):513-517. PMID 18364507, PMC3705579, doi 10.1093/jnci/djn044. URL: https://doi.org/10.1093/jnci/djn044 — 800 個致癌型感染；12 個月清除 67%（63–70）；持續 ≥12 個月者 30 個月內 CIN2+ 21%（15–28）；<30 歲 HPV16 持續者 53%（29–76）。Route: Europe PMC REST
- **[S20] PASS** — Plummer M, Schiffman M, Castle PE, Maucort-Boulch D, Wheeler CM; ALTS Group. (2007). *A 2-year prospective study of human papillomavirus persistence among women with a cytological diagnosis of atypical squamous cells of undetermined significance or low-grade squamous intraepithelial lesion.* J Infect Dis 195(11):1582-1589. PMID 17471427, doi 10.1086/516784. URL: https://doi.org/10.1086/516784 — 4,504 人；既有感染 24 個月清除 91%（90–92）；持續越久越不易清（37%→65%）。Route: Europe PMC REST
- **[S21] PASS** — Schiffman M, Castle PE, Jeronimo J, Rodriguez AC, Wacholder S. (2007). *Human papillomavirus and cervical cancer.* Lancet 370(9590):890-907. PMID 17826171, doi 10.1016/s0140-6736(07)61416-0. URL: https://doi.org/10.1016/s0140-6736(07)61416-0 — 「typically within 5–10 years, from less than 10% of new infections」「Invasive cancer arises over many years, even decades… peak or plateau in risk at about 35–55 years of age」。Route: Europe PMC REST
- **[S22] PASS** — Vink MA, Bogaards JA, van Kemenade FJ, et al. (2013). *Clinical progression of high-grade cervical intraepithelial neoplasia: estimating the time to preclinical cervical cancer from doubly censored national registry data.* Am J Epidemiol 178(7):1161-1169. PMID 23897645, doi 10.1093/aje/kwt077. URL: https://doi.org/10.1093/aje/kwt077 — 荷蘭 2000–2005 登記模型；CIN2/3→癌中位 23.5 年（20.8–26.6）；10 年內 1.6%（HPV16+ 2.4%／陰性 0.6%）。Route: Europe PMC REST
- **[S23] PASS** — de Sanjose S, Quint WG, Alemany L, et al. (2010). *Human papillomavirus genotype attribution in invasive cervical cancer: a retrospective cross-sectional worldwide study.* Lancet Oncol 11(11):1048-1056. PMID 20952254, doi 10.1016/s1470-2045(10)70230-8. URL: https://doi.org/10.1016/s1470-2045(10)70230-8 — 38 國 10,575 例；HPV16/18 佔 71%（70–72）；八型 91%；腺癌 16/18/45 佔 94%。Route: Europe PMC REST
- **[S24] PASS** — Rositch AF, Burke AE, Viscidi RP, et al. (2012). *Contributions of recent and past sexual partnerships on incident human papillomavirus detection: acquisition and reactivation in older women.* Cancer Res 72(23):6183-6190. PMID 23019223, PMC3513486, doi 10.1158/0008-5472.can-12-2635. URL: https://doi.org/10.1158/0008-5472.can-12-2635 — 700 名 35–60 歲女性；85%（155/183）新檢出發生於無性行為或單一伴侶期間；新伴侶歸因 13%、既往暴露（≥5 位終生伴侶）72%、HR 4.1（2.0–8.4）；支持潛伏–再活化模型。Route: Europe PMC REST
- **[S25] PASS** — Workowski KA, Bachmann LH, Chan PA, et al. (2021). *Sexually Transmitted Infections Treatment Guidelines, 2021.* MMWR Recomm Rep 70(4):1-187. PMID 34292926, PMC8344968, doi 10.15585/mmwr.rr7004a1. URL: https://doi.org/10.15585/mmwr.rr7004a1 — 逐字：「it is not possible to determine which partner transmitted the original infection. Having HPV does not mean that a person or his or her partner is having sex outside the relationship」「Sex partners do not need to be tested for HPV」「These tests should not be used for male partners」「Time of HPV acquisition cannot be definitively determined」「reactivation of latent infections in both male and female partners」；保險套段。Route: Europe PMC REST + fullTextXML(PMC8344968) grep 原文
- **[S26] PASS** — Meites E, Szilagyi PG, Chesson HW, et al. (2019). *Human Papillomavirus Vaccination for Adults: Updated Recommendations of the Advisory Committee on Immunization Practices.* MMWR Morb Mortal Wkly Rep 68(32):698-702. PMID 31415491, PMC6818701, doi 10.15585/mmwr.mm6832a3. URL: https://doi.org/10.15585/mmwr.mm6832a3 — 26 歲以下補接種；27–45 歲不做常規建議、改共同臨床決策。Route: Europe PMC REST
- **[S27] PASS** — Giuliano AR, Palefsky JM, Goldstone S, et al. (2011). *Efficacy of quadrivalent HPV vaccine against HPV infection and disease in males.* N Engl J Med 364(5):401-411. PMID 21288094, PMC3495065, doi 10.1056/nejmoa0909537. URL: https://doi.org/10.1056/nejmoa0909537 — 4,065 名 16–26 歲男性 RCT；per-protocol 對疫苗型別外生殖器病灶效力 90.4%（69.2–98.1）、ITT 65.5%。Route: Europe PMC REST
- **[S28] PASS** — International Collaboration of Epidemiological Studies of Cervical Cancer; Appleby P, Beral V, et al. (2006). *Carcinoma of the cervix and tobacco smoking: collaborative reanalysis of individual data on 13,541 women with carcinoma of the cervix and 23,017 women without carcinoma of the cervix from 23 epidemiological studies.* Int J Cancer 118(6):1481-1495. PMID 16206285, doi 10.1002/ijc.21493. URL: https://doi.org/10.1002/ijc.21493 — 目前吸菸者鱗癌 RR 1.60（1.48–1.73）；HPV 陽性限定 RR 1.95（1.43–2.65）；劑量效應；腺癌無關聯。Route: Europe PMC REST
- **[S29] PASS** — Chen CP, Kung PT, Wang YH, Tsai WC. (2019). *Effect of time interval from diagnosis to treatment for cervical cancer on survival: A nationwide cohort study.* PLoS One 14(9):e0221946. PMID 31483834, PMC6726236, doi 10.1371/journal.pone.0221946. URL: https://doi.org/10.1371/journal.pone.0221946 — 台灣 2004–2010 全國 9,693 人；96.37% 於 90 天內開始治療；90–180 天 HR 1.33（1.02–1.72）、>180 天 HR 1.36（1.12–1.65）。Route: Europe PMC REST
- **[S30] PASS** — Perri T, Issakov G, Ben-Baruch G, et al. (2014). *Effect of treatment delay on survival in patients with cervical cancer: a historical cohort study.* Int J Gynecol Cancer 24(7):1326-1332. PMID 25054445, doi 10.1097/igc.0000000000000211. URL: https://doi.org/10.1097/igc.0000000000000211 — 321 人；≤30／30–45／>45 天三組 3 年存活無差異（74.6/82.2/80.8%，P=0.38）；作者：為生育/卵巢保存留時間可接受。Route: Europe PMC REST
- **[S31] PASS** — 衛生福利部（資料來源：國民健康署）。〈健康臺灣-114年起擴大癌症篩檢 您的健康政府來顧〉，建檔 113-12-24。URL: https://www.mohw.gov.tw/cp-16-80948-1.html — 原文：「(4)增列25-29歲女性每3年1次子宮頸抹片檢查，同時每案補助由430元調整為630元。(5)新增35、45、65歲女性當年度1次人類乳突病毒(HPV)檢測服務，每案補助1,400元」；「30歲以上婦女，建議每3年至少做1次子宮頸抹片檢查」；抹片降低 70% 子宮頸癌死亡率之官方陳述。**篩檢政策 D3 主用、A4 一句話。** Route: WebSearch → curl（--cacert 代理憑證）grep 原文
- **[S32] PASS** — 衛生福利部公共關係室（資料來源：國民健康署）。〈健康台灣！6分鐘護一生，子宮頸癌不來找〉，建檔 114-05-08、更新 114-05-22。URL: https://dep.mohw.gov.tw/pro/fp-2731-82414-120.html — 原文：「自114年起擴大公費篩檢對象，將子宮頸抹片檢查年齡下修至25歲，同時新增35歲、45歲及65歲女性可接受1次免費HPV檢測」「年滿30歲以上女性每年可接受1次免費子宮頸抹片檢查；年滿25歲（含）至29歲以上女性，每3年也享有1次免費抹片服務」；WHO 90-70-90；發生率 25.2→7.6/十萬（111年）、死亡率 11→2.9（112年）；民國 84 年起免費抹片。**D3 主用。** Route: WebSearch → curl grep 原文
- **[S33] PASS** — 衛生福利部（資料來源：國民健康署）。〈癌症就醫好選擇 癌症診療品質認證醫院來相挺〉，建檔 113-03-19、更新 113-03-21。URL: https://www.mohw.gov.tw/cp-16-78073-1.html — 自民國 97 年推動癌症診療品質認證；全臺 67 家通過；85% 以上癌症病人於認證醫院治療；跨科別團隊原文（腫瘤內外科、放射腫瘤科、病理科、影像診斷科及腫瘤個案管理師，多專科定期開會）。Route: WebSearch → curl grep 原文
- **[S34] PASS** — 衛生福利部中央健康保險署。〈全民健康保險保險對象免自行負擔費用辦法第二條附表一：全民健康保險重大傷病項目及其證明有效期限〉（113年9月16日發布修訂、114年1月1日以後適用，官方 PDF）。URL: https://www.nhi.gov.tw/ch/dl-74911-9ea79f859a24431497ef0304ce4b7981-1.pdf （來源頁 https://www.nhi.gov.tw/ch/cp-6086-caf5f-2957-1.html ）— 原文：一、需積極或長期治療之癌症：「(四)子宮頸惡性腫瘤第一期（C53.0-C53.9、C55）…三年」「(五)除(一)-(四)之其他惡性腫瘤（C00.0-C96.9，不含C73、C94.4、C94.6）…五年」；全文檢索無原位癌／D06 項目。Route: WebFetch 取得下載連結（HTML 頁遭 Cloudflare 阻擋 curl，見 S40）→ curl 下載 PDF → pdftotext → grep 原文
- **[S35] PASS** — 衛生福利部中央健康保險署。「醫療服務給付項目」（全民健康保險醫療服務給付項目及支付標準之項目檔，114.01.01 生效版，官方 XLS）。URL: https://www.nhi.gov.tw/ch/dl-82687-cdc462f073354eeb894cfeef692ecb32-1.xls — 本組獨立重新下載、xlrd 逐列檢索（與 C 簡報 S37 同檔）：80205C 子宮頸楔狀切除術 2,810 點（laser conization 比照申報）；28028C 陰道鏡檢查 605 點；55001C 子宮頸切片 430 點；15017C 婦科細胞檢查 245 點（備註：3–6 個月限 1 次；曾罹癌前病變/抹片異常者 6 個月內重做為適應症）；26072B 正子造影-全身 36,500 點／26073B 局部 26,500 點（備註逐字：適應症含「子宮頸癌之分期及懷疑復發或再分期」，限 CT/MRI 無法分期或資訊不足且病歷載明必要性，不得用於例行追蹤）；33084B/33085B MRI 6,500/11,500 點；33070B–33072B CT 3,800–5,035 點；12080B SCC腫瘤標記 400 點（無限制條文）。Route: curl 下載 XLS → xlrd 逐列 grep
- **[S36] PASS** — 衛生福利部。〈久未做抹片婦女感染HPV率達8%，國民健康局提供自我採檢服務〉，建檔 99-10-07。URL: https://www.mohw.gov.tw/cp-3161-26078-1.html — 99 年 8 月起提供 HPV 自我採檢套組（36 歲以上且 6 年未抹片、30 歲以上身心障礙婦女，衛生所索取）；陽性率約 8%；陽性者 6–7 成後續完成抹片。**歷史政策（2010），引用必帶年份；現行自採管道見 S39 FAIL。** Route: WebSearch → curl grep 原文
- **[S37] PASS** — 嘉義市政府衛生局。〈人類乳突病毒(HPV)疫苗（114年擴大公費接種對象，補助國中男女生皆可施打HPV疫苗）〉。URL: https://health.chiayi.gov.tw/cp.aspx?n=6010 — 原文：107 年起國健署提供全國國中女生公費 HPV 疫苗；「衛生福利部國民健康署114年擴大公費HPV疫苗接種對象，補助男女生皆可施打」；現行公費為 9 價、第 1 劑 9–14 歲者 2 劑、滿 15 歲起 3 劑；9 價適應症至 45 歲。**疫苗政策 D3 主用（女兒的疫苗）；A3 僅伴侶／成人一句話。**（國健署 hpa.gov.tw 原始公告無法取得，見 S38。）Route: WebSearch → curl grep 原文
- **[S38] FAIL** — 衛生福利部國民健康署 hpa.gov.tw 全站（例：〈子宮頸癌防治〉 https://www.hpa.gov.tw/Pages/Detail.aspx?nodeid=614&pid=1125 、114 擴大篩檢原始公告 nodeid=4809&pid=18712）。WebFetch 回 ROBOTS_DISALLOWED（robots.txt SSL 驗證失敗）、與 C 簡報 S43／colon 簡報同因。→ 一律改用 mohw.gov.tw／dep.mohw.gov.tw 鏡像 [S31][S32][S33][S36] 與地方衛生局頁面 [S37]
- **[S39] FAIL** — 114 年公費 HPV 檢測（35/45/65 歲）之採檢方式與**現行**自我採檢選項的官方條文。已檢索：S31/S32 原文（僅寫「HPV 檢測服務」未載採檢方式）；WebSearch「自採/自我採檢 site:mohw.gov.tw」僅得 99 年舊公告 [S36]。→ 文章寫「HPV 檢測與自採管道以衛生所或國健署現行公告為準」，不得宣稱現行有或沒有自採
- **[S40] FAIL** — nhi.gov.tw HTML 頁面之 curl 取用（重大傷病專區 cp-6086、cp-6091 等）：回 403 Cloudflare challenge（--cacert 代理憑證無效）。PDF／XLS 直接下載正常 [S34][S35]；頁面內容改以 WebFetch 摘要輔助定位下載連結，引用一律以下載之官方檔案原文為準
- **[S41] FAIL** — 台灣「確診到治療開始」的官方等候時間統計（醫院癌症品質指標之公開版本）。未找到可引用之官方公開數據 → 等待時間段落以學術來源 [S29][S30] 撰寫，院內實際排程天數寫「向個管師確認」
- **[S42] FAIL** — 「癌症診療品質認證基準」條文全文（含多專科團隊會議之基準條號）。hpa.gov.tw 認證專區無法取得（S38）；mohw.gov.tw 僅有新聞稿層級描述 [S33]。→ MDT 敘述停在 S33 的描述層級，不可引用基準條號或宣稱「每位病人都必須經團隊會議」的條文原文
- **[S43] FAIL** — LEEP 專項健保支付碼與自費差額、EUA（麻醉下內診）在台灣的常規性文件。給付項目檔 [S35] 僅 80205C conization（laser 比照）；EUA 無官方/學會文件。→ 均寫「向醫務課／主治醫師確認」
