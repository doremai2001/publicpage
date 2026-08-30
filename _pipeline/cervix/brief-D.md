# D 組研究簡報 — 子宮頸癌專題（階段四：結束之後）

研究日期：2026-08-30。所有期刊來源皆以 Europe PMC REST API（`EXT_ID`／`TITLE`／`AUTH` 查詢，`resultType=core` 取摘要）逐條查證，書目欄位照 API 回傳值抄寫；開放取用全文另以 Europe PMC fullTextXML grep 原文（ESGO 2023＝PMC10247855、POI 2024 指引＝PMC11631070、JJCO 2025 回顧＝PMC12529068、愛爾蘭回顧＝PMC9892117、Medicina 2021 回顧＝PMC8066324、JAMA Netw Open 2026＝PMC13080543）。台灣端以 mohw.gov.tw 頁面與 nhi.gov.tw 原始 PDF（curl --cacert 下載後 pdftotext + grep 原文）查證；查不到的一律記 FAIL。零筆就寫零筆。

**撰寫時的重要前提**：本簡報完成時 `cervix/brief/A.md` 與 `cervix/brief/B.md` **尚不存在**。SPEC 指示 D3 重用 A4 的台灣篩檢來源、D4 重用 B 組的 pembrolizumab 條文查證——都做不到，因此 D3 的台灣篩檢政策與 D4 的健保條文**由本簡報自行完整查證**（含原文 grep）。A、B 組完成後請比對；若相同主題有出入，以各自的原始檔案下載日期新者為準。

**跨組界線提醒（SPEC §五）**
- 狹窄發生率與擴張器協定的所有數字 → **D2 主場**（C4 已依約定讓出 [C-S31] 的狹窄專屬數字與 [C-S34] 的內容數字）。
- HRT 的數據 → **D1 主場**；C4 只留一句「不是禁忌」。
- 卵巢移位的劑量資料 → 站上 `insight-cervix-ovary`；D1 只寫「沒做移位、骨盆照野內的卵巢」這一情境，不展開移位。
- 性生活一般層（治療中可不可以、慾望盛行率、體液殘留、「乾澀狹窄不是心理問題」論證）→ 站上 `care-sex`；D2 只寫骨盆放療後的專屬協定。care-sex 的八項清單已由 C 簡報 C4 區塊列出（C.md 第 278–287 行），本簡報不重複查證，見 D2 區塊的分工表。
- KEYNOTE-A18（同步化放療加 pembrolizumab）→ **B3**。D4 只寫復發轉移後的全身治療。
- 追蹤「在抓什麼」歸 D3；抓到之後的處置全部歸 D4。D3 不展開治療。
- 急症警語總表 → C2；D 組各篇只在相關處一句話指回。

---

# D1 — 提早停經：荷爾蒙補充不是禁忌　【紅線 5】

**Key facts**

*為什麼會提早停經（不做卵巢移位、卵巢在骨盆照野內的情境）*
- 人類卵母細胞的放射敏感度：Wallace 等人以自然卵泡衰減模型估計，**摧毀一半卵母細胞的劑量（LD50）不到 2 Gy** [S2]
- 同團隊的預測模型：治療後立即造成 97.5% 病人卵巢衰竭的「有效絕育劑量」（ESD）隨年齡下降——出生時 20.3 Gy、10 歲 18.4、20 歲 16.5、**30 歲 14.3 Gy** [S3]。根治性骨盆放療的處方是 45–50 Gy [S1]——遠超過任何年齡的 ESD。愛爾蘭回顧的說法可直接引用：以骨盆放療為主要治療的病人，「menopause is inevitable」（停經無可避免）[S4]
- 瑞典全國資料：45 歲以下子宮頸癌病人中，31%（257/837）因雙側卵巢切除及／或放療而急性喪失卵巢功能 [S11]

*「不是禁忌」的證據鏈（紅線 5 的地基——由弱到強排好）*
- 直接證據其實只有一個 1987 年的前瞻研究：Ploch（波蘭，120 名 I–II 期、手術及／或放療後），80 人用 HRT、40 人對照，追蹤至少 5 年：5 年無癌存活 80% vs 65%、復發 20% vs 32%，**皆無統計差異**；HRT 組症狀控制與放療後直腸膀胱陰道併發症較好 [S7]。此後**再沒有任何隨機試驗**——這件事要照實寫
- Vargiu 等人的系統性回顧（2021，篩 2,805 篇、納入 10 篇）：**沒有證據顯示 HRT 傷害子宮頸癌的腫瘤學結果**；並結論 HRT「應該提供給」年輕子宮頸癌倖存者 [S8]
- 2020 年 EMAS／IGCS 立場聲明原文：「There is no evidence to contraindicate the use of systemic or topical menopausal hormone therapy by women with cervical, vaginal, or vulvar cancer, as these tumors are not considered to be hormone dependent」 [S6]
- ESGO/ESTRO/ESP 2023 指引原文：「Hormone replacement therapy is indicated to cervical cancer survivors with premature menopause and should be consistent with standard menopausal recommendation [IV, B]」——注意證據等級是 IV [S1]
- 2024 年 ESHRE/ASRM/IMS 等四學會 POI 指引（分級建議）：「HT does not increase the risk of recurrence of squamous cell carcinoma of the cervix and **is recommended** for women with iatrogenic POI due to the treatment of squamous cell carcinoma.（STRONG，⊕⊕⊕◯）」 [S5]
- 2025 年日本婦癌背景的回顧（JJCO）：「For cervical cancer, HRT is not contraindicated in either squamous cell carcinoma or adenocarcinoma, regardless of stage」；同時誠實註明**神經內分泌癌等罕見組織型態的安全性資料有限** [S10]

*組織型態的細節（腺癌——訊號存在，但要分清楚「發生」與「復發」）*
- 芬蘭全國登記研究（Jaakkola，243,857 名用雌激素加黃體素治療 ≥6 個月的停經婦女）：**發生**鱗癌的標準化發生比 0.41（0.28–0.58）、**發生**腺癌 1.31（1.01–1.67）；用滿 5 年後分別為 0.34 與 1.83。作者的絕對數字：若為因果，每萬人用 5 年追蹤 10 年約少 2–3 例鱗癌、多約 2 例腺癌 [S9]——這是**一般族群的發生率**資料，不是倖存者的復發資料
- **復發**端：JJCO 回顧明言「no studies have demonstrated an increased risk of recurrence」（腺癌倖存者用 HRT 增加復發的研究不存在）[S10]；Vargiu 同方向 [S8]
- 但 2024 年 POI 指引把腺癌單獨分級：「HT **may be associated with a slightly increased risk of recurrence** of cervical adenocarcinoma and a personalized approach considering individualized HT risk and benefits is recommended（STRONG，⊕⊕◯◯）」 [S5]——指引之間不完全一致（EMAS/IGCS 與 ESGO 不分組織型態、POI 指引把腺癌另立一條）。這正是紅線 5 說「組織型態決定配方」的查證結果：**方向是個別化，不是禁忌**
- 愛爾蘭回顧則寫「For the purposes of MHT use, cervical adenocarcinoma and squamous cell carcinoma should be treated the same」[S4]——立場光譜的另一端，可用來呈現「專家之間也沒完全談攏」

*子宮還在的人：為什麼是雌加黃體素，不是雌激素單方*
- 2024 年 POI 指引（一般原則，非子宮頸專屬）：「A progestogen should be given in combination with estrogen therapy to **all women with an intact uterus** to prevent endometrial hyperplasia/cancer（STRONG，⊕⊕◯◯）」 [S5]
- 放療後子宮還在算不算「intact uterus」？愛爾蘭回顧寫得最直白：「It is important to remember that those with an intact uterus, **even after radiotherapy** do require combined MHT with estrogen and progesterone to avoid the risk of endometrial hyperplasia and malignancy」[S4]——這是回顧級論述，不是指引原文，標籤要帶
- 實務端佐證（美國調查，SGO 與 ABS 會員、178 名有效問卷）：婦癌科醫師 99.3%（135/136）願意在化放療後開 HRT、放腫科 73.8%；願意開的人裡，婦癌科 91.2% 選**雌加黃體素合併**配方（放腫科 70.0%）；選雌激素單方（口服或經皮）者只有約四分之一 [S14]——這是「態度調查」，不是療效資料

*不治療的代價（「不是禁忌」論證的另一半）*
- Muka 等人統合分析（32 篇、310,329 名女性）：45 歲前停經 vs 45 歲以上，冠心病 RR 1.50（1.28–1.76）、心血管死亡 RR 1.19（1.08–1.31）、全因死亡 RR 1.12（1.03–1.21）[S15]（觀察性資料）
- POI 2024 指引：未用 HT 的 POI 與**壽命縮短**相關（主因心血管疾病）（STRONG，⊕⊕◯◯）；「HT is recommended for women with POI **until the usual age of menopause** for primary prevention…whether there are estrogen deficiency symptoms or not（STRONG）」；骨骼端：POI 與骨微結構異常及骨密度下降相關，HT 建議用於維持骨密度、預防骨質疏鬆（STRONG）[S5]
- ESGO 2023 也有配套句：早停經病人應**定期評估骨骼狀態** [V, B] [S1]

*誰不適用／個別化的界線（紅線 5「不准寫成都可以放心吃」的素材）*
- POI 2024 指引：**有乳癌病史者一般不建議 HT**（STRONG，⊕⊕⊕◯）[S5]——子宮頸癌倖存者若同時有乳癌病史，走非荷爾蒙路線
- 腺癌：個別化（見上）[S5]；神經內分泌癌等罕見型態：資料有限 [S10]
- 有子宮者需合併黃體素；HT 中不明原因出血需要評估（POI 指引 GPP）[S5]

*沒人開、開了也太短（underuse——三個國家三份資料）*
- 瑞典（2005–2009 診斷、≤45 歲、837 人）：急性卵巢衰竭的 257 人中，診斷後 0.5–1 年有領過 HRT 者 67%，但領到建議劑量 75% 以上者只有 46%；4.5–5 年時使用率掉到 39%（足量者 21%）[S11]
- 美國保險資料庫（Suzuki 2023，1,826 名 <50 歲）：24 個月內用過 HRT 者僅 39.0%；放療組更低（36.6% vs 手術組 49.4%）；**中位使用時間只有 60 天**（放療組 35 天）[S12]
- 美國單一機構（Rauh 2017，202 名醫源性停經）：48.0% 得到 HRT 諮詢或處方；DEXA 骨密度檢查只有 8.6% 做過 [S13]
- JJCO 回顧的總結句可引用：「fewer than half of patients with iatrogenic menopause receive HRT and the duration of HRT use is shorter than recommended」 [S10]

**Claim ceiling**

Defensible：
- 「HRT 在子宮頸癌不是禁忌——歐洲三學會指引、EMAS/IGCS 立場聲明、2024 年四學會 POI 指引都有明文；鱗癌那一條的建議強度是 STRONG。」[S1][S5][S6]
- 「但我要誠實說：直接證據很薄。唯一的前瞻比較研究是 1987 年、120 人，結果是復發沒有差；之後快四十年沒有人做過隨機試驗。指引寫『不是禁忌』的底氣，一半來自這類小型資料，一半來自『子宮頸癌不是荷爾蒙依賴腫瘤』的生物學。」[S5][S6][S7][S8]
- 「腺癌的細節：一般族群的登記資料看到用雌加黃體素者腺癌發生率略高（用滿五年 SIR 1.83）；但在已治療的倖存者身上，沒有研究顯示 HRT 增加復發。2024 年 POI 指引因此對腺癌寫『可能略增復發風險、採個別化』——不是不能用，是要談過再用。」[S5][S9][S10]
- 「子宮還在（放療而沒開刀的人多數如此）就要用雌加黃體素合併配方，不是雌激素單方——照射過的子宮內膜仍可能有殘存功能。美國的調查裡，九成婦癌科醫師開的正是合併配方。」[S4][S5][S14]
- 「不吃的代價有數字：45 歲前停經者冠心病風險高五成、全因死亡高 12%（觀察性統合分析）；POI 指引建議 HT 用到自然停經年齡，且不論有沒有症狀。骨頭要定期評估。」[S1][S5][S15]
- 「現實是多數人根本沒拿到：瑞典足量使用者不到一半、美國資料庫中位只用了 60 天。這一篇存在的理由就是這個缺口。」[S10][S11][S12][S13]
- 「有乳癌病史是另一回事——那時 HT 一般不建議，要走非荷爾蒙選項。」[S5]

Would overstate：
- ✗「HRT 對子宮頸癌病人絕對安全／都可以放心吃。」——**紅線 5 直接失敗**；證據等級 ESGO [IV, B]、直接比較只有 Ploch 一篇 [S1][S7]
- ✗「癌症病人不能碰荷爾蒙。」——紅線 5 的另一側，同樣失敗 [S5][S6]
- ✗ 把 Jaakkola 的腺癌 SIR 寫成「用 HRT 會讓腺癌復發」——那是一般族群發生率，不是倖存者復發 [S9][S10]
- ✗「指引都同意腺癌照用就好。」——POI 2024 明文寫個別化；指引間不一致要寫出來 [S4][S5]
- ✗「雌激素單方也可以。」——子宮在就要合併黃體素（POI 指引 STRONG）[S5]
- ✗「HRT 會保護心臟所以每個人都該吃」──Muka 是觀察性資料，寫成「不治療的風險」可以，寫成 HT 的療效承諾不行 [S15]
- ✗ 寫出具體品名、劑量當處方（colon SPEC §四：不可寫成用法用量）。POI 指引的骨密度最低有效劑量（≥2 mg 口服或 100 µg 經皮 estradiol）可當背景知識引用，不可寫成醫囑 [S5]

**Caveats / safety notes**

- 全部安全性資料是觀察性或小型前瞻；寫作時句型固定為「沒有證據顯示有害」，不寫「已證明安全」。
- 三份指引對腺癌的分歧（ESGO/EMAS 不分、POI 2024 個別化、愛爾蘭回顧視同鱗癌）是本篇「誠實勝過乾淨」的示範點——攤開寫，結論落在「跟你的婦癌／放腫醫師談配方」。
- 陰道（外用）雌激素歸 D2／C4 的脈絡（ESGO：topical estrogens are indicated [IV, B] [S1]）；D1 寫全身性 HRT，一句話互指即可。
- 45 歲這個年齡切點是 Muka 分析的定義；POI 定義是 40 歲前。引用時帶各自定義，不混用。
- 血栓、偏頭痛等一般 HT 注意事項：POI 指引有相應條文（偏頭痛不是禁忌、有風險者考慮經皮途徑等）——寫到個別化那段時點到為止，不展開成 HT 教科書。

**Taiwan status**

- **健保藥品給付規定第 5 節（激素及影響內分泌機轉藥物，115.08.21 版，官方 PDF 已下載 grep）**：5.3「動情激素、黃體激素及治療不孕症藥物」節內，僅有兩條 estradiol **經皮貼片**的限制條文——Estraderm TTS「限不能口服本品患者使用，申報費用時應具體說明不能口服之理由」、Climara 50「限每週一片」；**全節查無任何把癌症病人排除在 HRT 給付之外的條文**，也無 estriol／conjugated estrogens／tibolone／黃體素製劑的專屬限制條文 [S16]。→ 可寫：「健保的給付規定裡沒有『癌症病人不能用荷爾蒙』這種條文；貼片有『限不能口服者』的規定」。**個別品項有沒有健保價、有沒有適應症限制，屬藥品品項檔層級（本環境取不到，同 C 簡報 S42 的阻擋），寫『請藥師或個管師查你的處方品項』** [S16][C-S42]
- 陰道雌激素給付：C 簡報已記 gap（C-S47），D1/D2 沿用，不重複查證
- 骨密度檢查（DXA）給付條件：**未查證**（本次未下載相應支付標準段落）→ gap，寫「向醫院確認自費或給付條件」
- 癌症資源中心與免付費專線 0809-010580 → 沿用 C 簡報 [C-S35][C-S36]

---

# D2 — 擴張器、性生活——沒人願意先開口的那題

**Key facts**

*狹窄有多常見（分母與分級——D2 主場，C4 已讓出）*
- EMBRACE 前瞻資料（Kirchheiner 2016，630 名局部晚期、化放療＋影像導引近接，中位追蹤 24 個月）：**2 年 G≥2 陰道狹窄的精算發生率 21%**；風險因子為直腸陰道參考點劑量、EBRT >45 Gy/25 次、腫瘤侵犯陰道；模型推估直腸陰道參考點 65 Gy 時風險 20%、75 Gy 27%、85 Gy 34%——因此提出 ≤65 Gy 的規劃目標 [S17]
- EMBRACE-I 六中心子研究（Westerveld 2022，301 人，中位追蹤 49 個月）：追蹤期間狹窄 G0 25%、**G1 52%、G2 20%、G3 3%**——輕度幾乎過半，重度（G3）個位數 [S18]
- 整體陰道併發症的背景數字（2 年 G≥1 89%、G≥2 29%、G≥3 3.6%，多在 6 個月內出現；狹窄是最常見項目）→ 已在 C4 用過，D2 可再引 [C-S31=S19]
- 各文獻報告的狹窄發生率範圍極寬：1.2%–88%（依評估方法、族群、治療而異；近年估計子宮頸癌骨盆放療後三年內約 60%）——評估方法不標準化是主因 [S24]

*擴張器的證據，誠實版（比「人人都該用」的通用建議弱，但不是零）*
- Cochrane（Miles & Johnson 2014）：**沒有可靠證據支持「放療期間」常規擴張**；放療後的觀察性資料顯示規律擴張與較低自述狹窄率相關，但因果與偏誤無法排除 [C-S33=S20]
- 目前最大的前瞻資料（EMBRACE-I 擴張器報告，Kirchheiner 2025，882 名可分析、中位追蹤 60 個月）：64% 規律「擴張」（定義：擴張器使用及／或性活動出現在 ≥50% 的追蹤紀錄）；規律者 **5 年 G≥2 狹窄 23% vs 37%**（多變項 HR 0.630，P=.001）；代價是輕度（G≥1）乾澀（72% vs 67%）與出血（61% vs 34%）較多，**G≥2 不增加** [S21]——仍是觀察性關聯（做得下去的人陰道本來就比較健康），寫作時要帶這個保留
- 唯一的子宮頸癌隨機試驗（Martins 2021，巴西單中心、開放式、195 人分四組：外用雌激素 66／外用睪固酮 34／潤滑劑 66／擴張器 29）：一年後**四組陰道體積都縮小約 25%、組間無差異**；但以 CTCAE 評的狹窄嚴重度，只有擴張器組沒有顯著惡化（p=0.37，其他組 p<0.01）[S23]——組數不均、開放式、回溯註冊；寫的時候標「品質有限的單一試驗」
- 專業建議的實際內容與證據等級：ESGO 2023 原文「After CTRT and BT, patients should be counseled about sexual rehabilitation measures including the use of vaginal dilators. **Topical estrogens are indicated** [IV, B]」——證據等級 IV（專家共識層級），時間點寫在「治療完成後」[S1]
- 具體協定只有共識可引（Medicina 2021 回顧整理）：英國（國際臨床指引小組）共識——**放療結束後 4 週開始、每週 2–3 次、每次 1–3 分鐘、持續 9–12 個月**；巴西 2019 共識——每次 5–10 分鐘、每週 2–3 次、**期限無共識**（且對何時開始未達成一致）；**沒有證據支持放療期間就開始** [S24]。各院衛教單的差異來自這裡——協定本身就是共識而非試驗

*依從性（低——而且隨時間掉）*
- 前瞻依從性研究（Law 2015，MSKCC，109 名骨盆放療後、含婦癌 46 名；該院建議每週 3 次、共 52 週）：12 個月平均依從性 **42%**（95% CI 36–48%）；第一季 56%、第四季只剩 **25%**；82% 在 12 個月時維持治療前的擴張器尺寸 [S22]
- 依從性低的原因（系統性回顧）：疼痛、甚至受傷、缺乏標準化評估與指導 [care-sex 已載 Torigoe 2026 的同方向結論——歸 care-sex，D2 引 Law 的數字即可] [S22]

*長期性功能（EMBRACE 資料）*
- EMBRACE 陰道morbidity子研究（Suvaal 2023，113 名陰道侵犯 ≤5 mm 的溫和族群）：**2 年時 47% 沒有性活動**；醫師評估的陰道變化在第一次追蹤即與基線不同 [C-S32=S25]
- 規律擴張／性活動與較低狹窄的關聯 → S21；「性活動」與「擴張器」在 EMBRACE 是合併定義，寫作時不可把「有性生活」寫成醫囑（C 簡報 C4 已同樣提醒）

*與站上 care-sex 的分工（不可重寫清單——C 簡報 C4 區塊第 278–287 行已列全，此處只標 D2 相關三項）*
- care-sex 已寫：「陰道乾澀與狹窄不是心理問題」整段（60–90 Gy 纖維化、擴張器「持續使用時有效」但會痛做不下去、ASCO 先潤滑保濕再考慮低劑量陰道雌激素、乳癌觀察性資料）→ **D2 不重寫一般論證，只寫骨盆放療後的時序、頻率、數字**
- care-sex 已寫：治療期間可不可以、避開的狀況（含骨盆照射那幾週）、性行為後的急症句 → D2 指路
- care-sex 已寫：台灣單中心 RCT（63 名子宮頸癌病人，單次性健康衛教課提升知識與自我效能）→ D2 可一句話引用「這件事可以被教」，出處在 care-sex
- HDR 近接後體內沒有放射性的澄清 → C1/C4 主場（SPEC §八修正 8），D2 不重複

**Claim ceiling**

Defensible：
- 「輕度的陰道變窄變短幾乎是常態（前瞻資料裡 G1 過半），需要處置的中重度約兩成，最嚴重的 G3 是個位數。」[S17][S18]
- 「擴張器的證據我照實講：隨機試驗幾乎沒有，Cochrane 說『放療期間』沒有可靠證據；但放療後的前瞻觀察資料——882 人追蹤五年——規律使用（或有規律性生活）的人 G≥2 狹窄 23% 對 37%。關聯不等於因果，但這是目前最好的資料，而且方向一致。」[S20][S21]
- 「巴西唯一的隨機試驗結果很誠實：不管用什麼，一年後陰道體積平均都縮了四分之一；差別在嚴重度——擴張器組是唯一沒有顯著惡化的一組。」[S23]
- 「什麼時候開始、多久做一次？指引層級只有共識：英國版是結束後約 4 週開始、每週 2–3 次、持續 9–12 個月；巴西版連何時開始都沒共識。所以各醫院衛教單不一樣是正常的，以你的治療團隊為準。」[S1][S24]
- 「堅持很難是有數字的：前瞻研究裡 12 個月平均依從性 42%，到第四季只剩四分之一。會痛、沒人教、覺得尷尬都是真的——這些都可以跟放腫護理師調整。」[S22]
- 「規律擴張的代價也要說：輕度乾澀和出血會比較常見（重度不增加）——出一點血不代表做錯了，但出血不止要回報。」[S21]
- 「外用雌激素不是偷偷摸摸的自費偏方——ESGO 指引寫的是 indicated。」[S1]

Would overstate：
- ✗「每天用擴張器就不會狹窄。」——觀察性關聯＋巴西試驗四組體積都縮 [S21][S23]
- ✗「不用擴張器一定會閉鎖。」——G3 是 3% [S18]
- ✗ 把英國共識的 4 週／2–3 次寫成「標準」或掛上試驗證據——它是共識，證據等級 IV [S1][S24]
- ✗「放療期間就要開始用。」——Cochrane 與回顧都說無證據 [S20][S24]
- ✗ 重寫 care-sex 的「不是心理問題」論證、體液殘留、慾望盛行率——分工紅線
- ✗ 把 Suvaal 的 47% 無性活動（陰道侵犯 ≤5 mm 的溫和族群）推到所有病人 [S25]
- ✗「有性生活可以取代擴張器」寫成醫囑——EMBRACE 是合併定義，不是處方 [S21]

**Caveats / safety notes**

- 本篇的結構性風險是「數字嚇人」與「數字騙人」並存：89%／21%／3% 三層要每次帶分級標籤，否則讀者不是嚇跑就是輕忽。
- 依從性 42% 的分母是「該院建議每週 3 次 × 52 週」——那是 MSKCC 的院內協定，不是普世標準；引用時帶機構標籤。
- Martins 試驗的擴張器組只有 29 人且開放式——「唯一 RCT」不等於「高品質 RCT」，兩句都要寫。
- 出血是規律擴張的已知輕度副作用 [S21]，但**大量出血不止**屬急症 → 一句話指回 C2 總表。
- 擴張器尺寸遞增、搭配潤滑等操作細節屬實作層——作者可用門診經驗寫，不掛文獻；不寫成醫材廣告（醫療法紅線）。

**Taiwan status**

- **陰道擴張器的健保給付：查無任何官方條文或公告**（WebSearch「陰道擴張器 健保給付」無官方結果；醫療服務給付項目檔為處置項目、不含此類居家醫材）→ **gap**：擴張器屬自購醫材，各院輔具室／醫療器材行管道與價格不一，寫「向放腫護理師或個管師確認購買管道與費用」[S26-FAIL]
- 陰道雌激素給付條文 → C 簡報已記 gap [C-S47]，沿用
- 癌症資源中心 0809-010580 [C-S35][C-S36]

---

# D3 — 追蹤怎麼排；疫苗和抹片現在還要不要

**Key facts**

*追蹤排程（兩份指引，一致的骨架）*
- 加拿大 CCO 系統性回顧＋指引更新（Elit 2016）：**前 2 年每 3–4 個月一次、第 3–5 年每 6–12 個月一次**；每次含病史（主動問症狀）與完整身體檢查；**陰道穹窿抹片不應做得比一年一次更密**；**PET-CT、其他影像、腫瘤標記都不建議常規做**；HPV DNA 檢測「可能是放療後偵測復發較敏感的方法」；5 年後回歸一般婦科照護 [S27]
- ESGO 2023：追蹤策略**個別化**（依風險）；每次回診＝病史（含症狀與副作用）＋身體檢查（含鴨嘴與雙合診）；**影像與抽血只在有症狀或懷疑復發時做** [IV, A]；**陰道穹窿抹片不建議 [IV, D]**；放療後「Cytology is not recommended in detecting disease recurrence after radiotherapy [IV, D]」；治療後影像評估反應**不早於 3 個月**；保留生育治療後（子宮頸還在）追蹤**要含 HPV 檢測（6–12 與 24 個月）[V, A]**；早停經者定期評估骨骼 [S1]
- 2026 年 SGO 臨床實務聲明（Salani）：坦承**追蹤建議的證據薄弱、多為回溯性**、實務差異大；「symptom review and physical examination are reportedly the most effective methods to detect recurrence」；陰道抹片「negligible benefit」卻仍被常規使用；常規影像「without proven benefit」（特定情境例外）；ctDNA 等新工具還需要研究 [S28]

*抹片與 HPV 檢測在「治療後」的角色（誠實的分歧）*
- 分機關寫清楚三種身體狀態：(1) 放療後子宮頸還在——細胞學不建議（放射變化讓判讀不可靠，ESGO [IV, D]）[S1]；(2) 手術後只剩陰道穹窿——穹窿抹片 ESGO 不建議 [IV, D]、CCO 說最多一年一次 [S1][S27]；(3) 圓錐切除／保留生育——HPV 檢測是正式建議 [S1]
- HPV 檢測抓復發：CCO 2016 說「可能較敏感」[S27]，但實測潑冷水——單一機構回溯（Aryasomayajula 2022，262 名倖存者、169 名做過 hrHPV）：24% 至少一次陽性；**復發者與未復發者的陽性率沒有差異（21% vs 24%，p=0.67）、沒有任何一例復發是靠 hrHPV 驗出的**，陽性反而帶來額外檢查；作者結論不支持常規使用 [S29]——兩個來源方向相反，照實並列
- 復發怎麼被發現：SGO 2026——症狀回顧與身體檢查是最有效的方法 [S28]。**本次沒有取得「幾 % 復發以症狀呈現」的單一可引用分母**——寫定性（「大多數復發是因為症狀或內診異常被抓到」掛 S28），不發明百分比

*治療後打 HPV 疫苗（證據所在的位置要標清楚）*
- 證據在「圓錐切除後的 CIN 族群」：BMJ 系統性回顧＋統合分析（Kechagias 2022，22 篇、統合 18 篇）：局部切除後有接種者 CIN2+ 復發風險 **RR 0.43（0.30–0.60）**（11 篇、19,909 人、中位追蹤 36 個月）；HPV16/18 相關 CIN2+ 更低（RR 0.26）；**GRADE 評為 very low 到 moderate**，作者明言資料「inconclusive」、需要大型隨機試驗 [S30]——多數納入研究是觀察性或事後分析，接種時機（術前／術後）不一
- **侵襲癌治療後接種：直接證據為零。** Europe PMC 標題檢索（vaccination + cervical cancer + after/survivors + treatment/treated）**0 筆**臨床結果研究 [S31-note]。寫法：「對已經得過侵襲癌的人，疫苗防復發的證據不存在；上面那些數字是癌前病變族群的」——不可外推
- 年齡的誠實面（給「我自己現在打還有用嗎」這題）：美國 ACIP 2019——**26 歲以下建議補接種；27–45 歲不做常規建議**，改為「共同臨床決策」，因為多數人已暴露過、群體層次獲益小 [S32]

*女兒／家人的疫苗（台灣公費現況——官方原文已驗，見 Taiwan status）*

*自己的抹片（台灣政策——見 Taiwan status；文章要把「治療後追蹤」與「一般人篩檢」分開：已治療者照上面的追蹤協定走，公費篩檢是給沒得過病的人與追蹤畢業者的框架）*

**Claim ceiling**

Defensible：
- 「追蹤的骨架很簡單：前兩年每三到四個月、之後每半年到一年，重點是問症狀加內診——不是排一堆檢查。影像和抽血留給有症狀或檢查有異常的時候，這是指引原文，不是省成本。」[S1][S27][S28]
- 「我要誠實說：追蹤要多密才對，其實從來沒有好的隨機試驗證明過。連 2026 年美國婦癌學會的聲明都承認證據薄弱。所以個別化排程不是敷衍，是誠實。」[S28]
- 「放療後的子宮頸做抹片，指引寫的是『不建議』——放射變化會讓判讀不可靠，陽性嚇人、陰性也不保證。穹窿抹片同樣不建議。」[S1][S27]
- 「HPV 驗復發聽起來合理，但實測讓人清醒：一家醫院的資料裡，沒有任何一次復發是 HPV 檢測抓到的，陽性只帶來更多檢查。有一份指引說它可能有用、有一份實測說沒用——這題還沒有答案。」[S27][S29]
- 「切完癌前病變後打疫苗，統合分析看到復發風險減半左右——但證據品質被評為低到中等，作者自己說還不能下結論。至於已經得過侵襲癌的人，防復發的證據是零，我查過，就是零。」[S30]
- 「27 到 45 歲補打是『可以談』不是『建議打』——年紀越大、多半已經暴露過，效益遞減。這句對病人自己、也對她的成年姊妹適用。」[S32]
- 「女兒的疫苗不用自費：台灣從 2025 年 9 月起，公費九價 HPV 疫苗涵蓋全體國中生，男生也打。」[S33]

Would overstate：
- ✗「追蹤照這個表做就不會漏。」——證據薄弱是主旨之一，不可反向寫成保證 [S28]
- ✗「治療後打疫苗可以防止復發。」——CIN 族群、觀察性為主、GRADE 低；侵襲癌族群零證據 [S30]
- ✗「HPV 檢測比抹片準，追蹤都應該改用它。」——S29 實測相反；保留生育族群才有正式建議 [S1][S29]
- ✗「45 歲以上打疫苗沒有用。」——是「效益遞減、共同決策」，不是無效 [S32]
- ✗ 展開復發後的治療選項——D4 主場
- ✗ 把台灣公費篩檢年齡寫成「治療後追蹤的排程」——兩個制度，分開寫

**Caveats / safety notes**

- 「不建議常規影像」不等於「有症狀也不照」——症狀觸發的影像是 [IV, A] 建議 [S1]。這兩句必須同段出現，否則會被讀成「醫院不幫我照」。
- Kechagias 的 RR 0.43 很好記也很好被濫用；引用時 GRADE 標籤與「CIN 族群」標籤缺一不可 [S30]。
- ACIP 是美國建議；台灣成人自費補接種的官方年齡建議本次未另行查證（gap）——寫「跟婦產科或家醫科談」，不援引台灣不存在的條文。
- 「追蹤在抓什麼」與「抓到之後怎麼辦」分屬 D3/D4——本篇對復發治療只留一句「還有路，見下一篇」。
- 死亡率／發生率下降七成等篩檢成效數字是政策宣導數字（官方頁面原文），引用時標「國健署公布」[S34]。

**Taiwan status**（本組自行查證；A4 簡報完成後請交叉比對）

- **HPV 疫苗公費對象（已驗官方原文）**：衛福部新聞稿（資料來源：國民健康署，建檔 114-08-12）——「自114年9月起，擴大HPV疫苗公費接種對象，由原先的國中女生擴大至國中男生」；對象為「113年入學的全體國中生（包含男女）」，校園集中接種；**現行公費疫苗為九價**；15 歲以下 2 劑、間隔 ≥6 個月；錯過校園場次可持補接種通知單到合約院所公費補接種 [S33]
- **子宮頸癌篩檢公費政策（已驗官方原文，114/1/1 起）**：25–29 歲**每 3 年 1 次**公費抹片（新增，補助 630 元）；**30 歲以上每年可做 1 次免費抹片**（政策自民國 84 年起；同頁另有「建議每 3 年至少 1 次」的建議句——資格是每年、建議底線是三年，兩句都是官方原文）；**新增 35、45、65 歲女性各 1 次公費 HPV 檢測**（補助 1,400 元，國健署明言 35/45 依國際指引、65 歲是台灣因高齡感染率加開）[S34][S35]
- **HPV 自採檢體政策：查無官方公告**。mohw.gov.tw 兩頁均未提及自採；hpa.gov.tw 本環境無法存取（SSL 失敗，同 C 簡報 S43）→ **gap**：公費 HPV 檢測的採檢方式（醫師採檢或自採）寫「以合作院所現場說明為準」，不宣稱有或沒有自採選項 [S36-FAIL]
- 2018 年起國中女生公費接種、2018–2021 入學世代兩劑完成率 75.2%→91.7%：出自中央社報導（媒體層級，引用時標「據媒體報導」或不用）[S37-媒體]
- 追蹤期間回診的部分負擔、抹片在「已有症狀／追蹤」時走健保而非公費篩檢等行政細節：未逐項查證 → 寫「向個管師確認」

---

# D4 — 復發之後，還有哪些路

**Key facts**

*先分兩張地圖：骨盆內（可能還有根治意圖）vs 遠端（以控制為主、少數寡轉移例外）*
- ESGO 2023 的門檻句：多發淋巴結／遠端轉移（非寡轉移）或廣泛骨盆壁侵犯的多灶性局部病灶，**不應視為根治性治療的對象 [IV, D]**；**寡轉移／寡復發應考慮根治性、有治癒潛力的治療 [IV, B]**；復發應盡可能取得病理證實 [IV, B]；復發治療需集中在多專科團隊 [S1]

*骨盆內復發（放療後）*
- ESGO：**中央型骨盆復發（未及骨盆壁、無骨盆外病灶）建議骨盆臟器摘除術（pelvic exenteration）[IV, B]**；再程放療（IGABT）用於選擇性中央復發病人、「只能在專門中心做」[IV, C] [S1]
- 摘除術的現代成績（COREPEX 回溯多中心國際研究，862 名婦癌病人，2005–2023）：完整切除（切緣陰性）78.4%；預後分數分四組，**5 年整體存活最好一組 54.3%、其次 40.4%、24.0%、最差 4.3%**；全摘除、切緣陽性、淋巴血管侵犯、「持續性（而非復發）疾病時開」都是壞因子；最常見的失敗是遠端復發（32.1%）[S38]——「高度選擇下約四到五成」的說法成立，但**要同時寫另一端的 4.3%**
- 手術本身的代價（統合分析，46 篇、4,417 人、多數為子宮頸癌）：**30 天死亡率 5.1%**（敗血症為首因 27.2%）；圍術期死亡率逐年下降；骨盆壁侵犯與全摘除增加風險 [S39]
- 再程放療的證據狀態（回顧原文）：毒性高（尤其短期內的照野內復發）、各研究異質性大、**缺乏大型前瞻研究、無法下確定結論**——是前緣不是標準 [S40]

*遠端／無法根治的復發——第一線*
- GOG-240（452 人，復發／持續／轉移）：化療加 bevacizumab，OS 17.0 vs 13.3 個月（HR 0.71）；最終分析 16.8 vs 13.3（HR 0.77，p=0.007）；代價：≥G2 高血壓 25% vs 2%、≥G3 血栓 8% vs 1%、瘻管（任何級，均為照射過的病人）15% vs 1% [S41][S42]
- KEYNOTE-826（617 人，雙盲第三期）：化療（±bev）加 pembrolizumab vs 加安慰劑。**族群標籤不可省**：最終 OS——**CPS≥1（548 人）28.6 vs 16.5 個月（HR 0.60）；全體 26.4 vs 16.8（HR 0.63）；CPS≥10（317 人）29.6 vs 17.4（HR 0.58）**；G≥3 不良事件 82.4% vs 75.4% [S43][S44]。注意：全體人群的數字被 CPS≥1 佔 89% 的組成拉動；**CPS<1 的次族群獲益未確立**（主要分析族群就是 CPS≥1/全體/CPS≥10 三層）——寫作只用這三個帶標籤的數字
- ESGO 2023 的定位：鉑類化療±bev 為第一線 [I, A]；**pembrolizumab 加入限 CPS≥1 [I, A]** [S1]

*第二線之後*
- Cemiplimab（EMPOWER-Cervical 1，608 人、鉑類後進展、不限 PD-L1）：OS 12.0 vs 8.5 個月（HR 0.69）；ORR 16.4% vs 6.3%；G≥3 45.0% vs 53.4% [S45]；ESGO：未用過免疫治療者第二線建議 [I, A] [S1]
- Tisotumab vedotin（innovaTV 301，502 人、第二／三線）：OS **11.5 vs 9.5 個月（HR 0.70）**；PFS 4.2 vs 2.9；ORR 17.8% vs 5.2%；G≥3 治療期不良事件 52.0% vs 62.3%；14.8% 因毒性停藥 [S46]——中位數差 2 個月、反應率不到兩成，寫的時候不可膨脹成「新救星」；眼部毒性等細節本次未取得可引用原文，不寫具體百分比
- 免疫治療用過 pembrolizumab 之後還能不能用 cemiplimab：EMPOWER 排除了先前免疫治療者 [S45]——這個序列問題沒有答案，照實寫

*寡轉移的誠實（鏡像乳癌系列的保守）*
- **子宮頸癌專屬的隨機資料是零**：Europe PMC 檢索「oligometastatic + cervical cancer + randomized/phase 3」**0 筆**、「oligometastatic + cervical + review」標題檢索亦 0 筆 [S47-note]
- 可引用的只有指引共識層級：ESGO 對照野外的局部性主動脈旁／縱膈／鎖骨上復發可行根治性 EBRT±化療 [IV, C]；「oligo」器官轉移（肺、肝等）的局部處理（切除、熱消融、介入性近接、SBRT）[IV, B]——證據等級全是 IV，即專家共識 [S1]

*什麼時候談試驗與安寧*
- ESGO：復發／轉移病人**強烈建議納入臨床試驗 [V, A]**；**晚期病人應由臨床團隊提供與腫瘤治療整合的早期安寧緩和照護 [IV, A]**（含疼痛階梯、腎衰竭的引流決策、大量出血的處置等章節）[S1]——「談安寧不是放棄治療」有指引位階可引

**Claim ceiling**

Defensible：
- 「骨盆內單一中央復發和多處遠端轉移是兩條完全不同的路：前者還存在根治意圖的選項，後者的目標是控制與生活品質——把這兩張地圖攤開，是這篇存在的目的。」[S1]
- 「骨盆臟器摘除術是大手術：現代國際資料裡，選得最好的一群 5 年存活過半，但選錯對象的那一組不到 5%，而且 30 天內死亡率 5%。所以『能不能開』必須由專門中心的多專科團隊來選。」[S38][S39]
- 「再程放療是前緣不是標準——回顧文獻自己說無法下結論，只能在專門中心做。」[S1][S40]
- 「第一線加 pembrolizumab 的數字要帶標籤：PD-L1 CPS≥1 的病人中位存活 28.6 對 16.5 個月——差了一年；CPS 分數是用藥前提，這是指引原文。」[S1][S43][S44]
- 「bevacizumab 平均多爭取三個多月，代價是高血壓、血栓，照射過的病人瘻管風險 15%。」[S41][S42]
- 「第二線之後還有藥：cemiplimab（多活約 3.5 個月）、tisotumab vedotin（多活約 2 個月、反應率不到兩成）——是真實的選項，不是奇蹟。」[S45][S46]
- 「寡轉移拿掉／燒掉／照掉能不能延命？子宮頸癌自己的隨機證據是零，指引建議的證據等級是專家共識。可以考慮，前提是多專科評估加上誠實的期待。」[S1]
- 「臨床試驗與安寧緩和都寫在指引裡：試驗是強烈建議，早期安寧照護是 [IV, A]——它們是路，不是終點宣告。」[S1]

Would overstate：
- ✗ 任何不帶 CPS／族群標籤的免疫治療存活數字——**族群標籤不可協商**（SPEC）[S43][S44]
- ✗「摘除術 5 年存活五成」不帶「高度選擇、最好的風險組」標籤 [S38]
- ✗「寡轉移積極處理可以治癒」——零隨機證據、指引 [IV] 級 [S1]
- ✗「tisotumab／cemiplimab 台灣就用得到」——健保零條文（見 Taiwan status），費用句要照固定紅線寫
- ✗「復發等於末期」或「總有辦法」——雙向都是失敗；COREPEX 的 4.3% 那組和 54.3% 那組都要在場
- ✗ 引個案故事當代表性結果（colon SPEC 紅線精神沿用）

**Caveats / safety notes**

- KEYNOTE-826 各層人群互相重疊（CPS≥10 ⊂ CPS≥1 ⊂ 全體），不可寫成三組獨立病人比較。
- GOG-240 的瘻管 15% 全部發生在照射過的病人——本專題讀者幾乎都照射過，這個數字必須寫，不可藏進「副作用略多」。
- innovaTV 301 的對照組是單藥化療（topotecan 等），不是安慰劑——「贏過化療」的參照系要寫清楚。
- 摘除術資料是回溯性、跨 18 年（2005–2023）、多癌別（子宮頸為大宗）——標籤要帶。
- 「先用過 pembrolizumab 的人第二線免疫治療有沒有用」無證據（EMPOWER 排除）——診間常見問題，照實寫「沒有答案」。
- 安寧那段禁用「放棄」二字框架；ESGO 的「早期、與腫瘤治療整合」是原文依據。

**Taiwan status**（B 簡報不存在，本組自行查證；B 組完成後請比對）

- **健保藥品給付規定第 9 節（抗癌瘤藥物，115.8.21 版，官方 PDF 已下載、pdftotext 全文 grep「子宮頸」）**：
  - **Bevacizumab 有明確條文——9.37.4**（109/6/1 生效、113/3/1 修訂）：「持續性、復發性或轉移性之子宮頸癌」，(1) 與 cisplatin 及 paclitaxel 合併使用；(2) 與 paclitaxel 及 topotecan 合併使用（無法接受含鉑類藥物治療者）；(3) 需事前審查、每次申請以 15 週為限，續用需影像佐證無惡化 [S48]——條文組合正是 GOG-240 的兩個化療臂
  - **Pembrolizumab 用於子宮頸癌：零條文。** 9.69（免疫檢查點抑制劑）全文列出之給付癌別**不含子宮頸癌**；「子宮頸」在第 9 節全文僅出現於 9.37.4（bevacizumab）與附表的原位癌註記，共 4 處 [S48]。→ **SPEC「9.69?」的假設不成立**：截至 115.8.21 版，KEYNOTE-826 的組合在台灣屬自費 pembrolizumab（或未來增修條文），文章寫「pembrolizumab 在子宮頸癌目前查無健保給付條文，費用與最新給付狀態向醫務課與個管師確認」，不寫死「健保不給付」（條文隨時增修）
  - **Cemiplimab 用於子宮頸癌：零條文**（9.69 列名藥品含 cemiplimab，但其給付癌別不含子宮頸癌）[S48]
  - **Tisotumab vedotin：全文 grep 零筆**——一如預期 [S48]
- 重大傷病、癌症資源中心 0809-010580 → 沿用 C 簡報 [C-S35][C-S36]
- 臨床試驗查詢管道（台灣藥物臨床試驗資訊網等）：未查證現行網址 → gap，寫「請主治醫師或個管師協助查詢」

---

## Sources（單一編號序列；PASS 除非標 FAIL。「＝C-Sxx」表示與 C 簡報同一來源，URL 重列）

- **[S1] PASS（＝C-S7）** — Cibula D, Raspollini MR, Planchamp F, et al. (2023). *ESGO/ESTRO/ESP Guidelines for the management of patients with cervical cancer — Update 2023.* Int J Gynecol Cancer 33(5):649-666. PMID 37127326, doi 10.1136/ijgc-2023-004429. URL: https://doi.org/10.1136/ijgc-2023-004429 — 本組自行以 fullTextXML（PMC10247855，Virchows Arch 同文版）重新 grep 下列原文：HRT indicated [IV, B]；bone status assessed regularly [V, B]；追蹤個別化、每次回診內容、影像限症狀者 [IV, A]；vault cytology not recommended [IV, D]；放療後 cytology not recommended [IV, D]；影像不早於 3 個月；保留生育後 HPV 檢測 [V, A]；復發章（exenteration [IV, B]、reirradiation IGABT [IV, C] 限專門中心、寡轉移根治意圖 [IV, B]、非寡轉移不做根治 [IV, D]、鉑類±bev [I, A]、pembrolizumab 限 CPS≥1 [I, A]、cemiplimab 第二線 [I, A]、試驗 [V, A]、早期安寧 [IV, A]）；「After CTRT and BT… vaginal dilators; Topical estrogens are indicated [IV, B]」。Route: Europe PMC fullTextXML grep
- **[S2] PASS** — Wallace WH, Thomson AB, Kelsey TW. (2003). *The radiosensitivity of the human oocyte.* Hum Reprod 18(1):117-121. PMID 12525451, doi 10.1093/humrep/deg016. URL: https://doi.org/10.1093/humrep/deg016 — LD50 <2 Gy。Route: Europe PMC REST
- **[S3] PASS** — Wallace WH, Thomson AB, Saran F, Kelsey TW. (2005). *Predicting age of ovarian failure after radiation to a field that includes the ovaries.* Int J Radiat Oncol Biol Phys 62(3):738-744. PMID 15936554, doi 10.1016/j.ijrobp.2004.11.038. URL: https://doi.org/10.1016/j.ijrobp.2004.11.038 — ESD：出生 20.3／10 歲 18.4／20 歲 16.5／30 歲 14.3 Gy（97.5% 立即卵巢衰竭）。Route: Europe PMC REST
- **[S4] PASS** — Donohoe F, O'Meara Y, Roberts A, et al. (2023). *Using menopausal hormone therapy after a cancer diagnosis in Ireland.* Ir J Med Sci 192(1):45-55. PMID 35141870, PMC9892117, doi 10.1007/s11845-022-02947-6. URL: https://doi.org/10.1007/s11845-022-02947-6 — 開放取用全文 grep：骨盆放療「menopause is inevitable」；「those with an intact uterus, even after radiotherapy do require combined MHT…to avoid the risk of endometrial hyperplasia and malignancy」；腺癌與鱗癌同等對待（回顧級立場）。Route: Europe PMC REST + fullTextXML grep
- **[S5] PASS** — ESHRE, ASRM, CREWHIRL and IMS Guideline Group on POI; Panay N, Anderson RA, Bennie A, et al. (2024). *Evidence-based guideline: premature ovarian insufficiency.* Hum Reprod Open 2024(4):hoae065. PMID 39660328, PMC11631070, doi 10.1093/hropen/hoae065. URL: https://doi.org/10.1093/hropen/hoae065 — 全文 grep 分級建議原文：鱗癌 HT recommended（STRONG ⊕⊕⊕◯）；腺癌 slightly increased risk of recurrence、personalized approach（STRONG ⊕⊕◯◯）；intact uterus 需合併 progestogen（STRONG）；HT until the usual age of menopause（STRONG）；POI 無 HT 壽命縮短（主因 CVD）；HT 維持骨密度（STRONG）；乳癌病史 generally not recommended（STRONG ⊕⊕⊕◯）；偏頭痛非禁忌。Route: Europe PMC REST + fullTextXML grep
- **[S6] PASS** — Rees M, Angioli R, Coleman RL, et al. (2020). *EMAS and IGCS position statement on managing the menopause after gynecological cancer: focus on menopausal symptoms and osteoporosis.* Int J Gynecol Cancer 30(4):428-433. PMID 32046979, doi 10.1136/ijgc-2020-001217. URL: https://doi.org/10.1136/ijgc-2020-001217 — 摘要原文「There is no evidence to contraindicate…cervical, vaginal, or vulvar cancer, as these tumors are not considered to be hormone dependent」。（同文另刊 Maturitas 2020;134:56-61, PMID 32059825。）Route: Europe PMC REST
- **[S7] PASS** — Ploch E. (1987). *Hormonal replacement therapy in patients after cervical cancer treatment.* Gynecol Oncol 26(2):169-177. PMID 2433195, doi 10.1016/0090-8258(87)90270-8. URL: https://doi.org/10.1016/0090-8258(87)90270-8 — 120 人（80 HRT／40 對照）、I–II 期、≥5 年：5 年無癌存活 80/65%、復發 20/32%，皆無統計差異。Route: Europe PMC REST
- **[S8] PASS** — Vargiu V, Amar ID, Rosati A, et al. (2021). *Hormone replacement therapy and cervical cancer: a systematic review of the literature.* Climacteric 24(2):120-127. PMID 33236658, doi 10.1080/13697137.2020.1826426. URL: https://doi.org/10.1080/13697137.2020.1826426 — 10 篇；無 HRT 傷害腫瘤學結果的證據；鱗癌發生率降低、腺癌弱增加；結論 HRT should be offered。Route: Europe PMC REST
- **[S9] PASS** — Jaakkola S, Pukkala E, Lyytinen HK, Ylikorkala O. (2012). *Postmenopausal estradiol-progestagen therapy and risk for uterine cervical cancer.* Int J Cancer 131(4):E537-43. PMID 22024969, doi 10.1002/ijc.27321. URL: https://doi.org/10.1002/ijc.27321 — 243,857 名 EPT 使用者：鱗癌 SIR 0.41（0.28–0.58）、腺癌 1.31（1.01–1.67）；≥5 年 0.34／1.83；絕對數字每萬人 10 年 −2~3 鱗癌／+2 腺癌。**發生率資料，非復發。** Route: Europe PMC REST
- **[S10] PASS** — Yoshihama T, Yokota M, Aoki D, Yamagami W. (2025). *Hormone replacement therapy in female-specific cancer survivors: considerations beyond cancer cure.* Jpn J Clin Oncol 55(9):1000-1004. PMID 40459199, PMC12529068, doi 10.1093/jjco/hyaf092. URL: https://doi.org/10.1093/jjco/hyaf092 — 全文 grep：「not contraindicated in either squamous cell carcinoma or adenocarcinoma, regardless of stage」；神經內分泌癌等罕見型態資料有限；「no studies have demonstrated an increased risk of recurrence」（腺癌）；underuse 總結句。Route: Europe PMC REST + fullTextXML grep
- **[S11] PASS** — Everhov ÅH, Nyberg T, Bergmark K, et al. (2015). *Hormone therapy after uterine cervical cancer treatment: a Swedish population-based study.* Menopause 22(6):633-639. PMID 25405572, doi 10.1097/GME.0000000000000357. URL: https://doi.org/10.1097/gme.0000000000000357 — 837 名 ≤45 歲；31% 急性卵巢衰竭；0.5–1 年 HRT 使用 67%（足量 46%）；4.5–5 年 39%（足量 21%）；不因組織型態而異。Route: Europe PMC REST
- **[S12] PASS** — Suzuki Y, Huang Y, Ferris J, Kulkarni A, Hershman D, Wright JD. (2023). *Prescription of hormone replacement therapy among cervical cancer patients with treatment-induced premature menopause.* Int J Gynecol Cancer 33(1):26-34. PMID 36543392, doi 10.1136/ijgc-2022-003861. URL: https://doi.org/10.1136/ijgc-2022-003861 — 1,826 名 <50 歲；24 個月內 HRT 39.0%（放療組 36.6%、手術組 49.4%）；中位使用 60 天（放療組 35 天）。Route: Europe PMC REST
- **[S13] PASS** — Rauh LA, Pannone AF, Cantrell LA. (2017). *Hormone replacement therapy after treatment for cervical cancer: Are we adhering to standard of care?* Gynecol Oncol 147(3):597-600. PMID 28923411, doi 10.1016/j.ygyno.2017.09.009. URL: https://doi.org/10.1016/j.ygyno.2017.09.009 — 202 名醫源性停經；48.0% 得到 HRT 諮詢／處方；DEXA 8.6%；無保險與較高年齡為負因子。Route: Europe PMC REST
- **[S14] PASS** — Levy MS, Huang M, Dietrich CS, Fabian D. (2026). *Oncology Clinicians' Attitudes on Hormonal Therapy After Chemoradiotherapy for Cervical Cancer.* JAMA Netw Open 9(4):e266862. PMID 41979882, PMC13080543, doi 10.1001/jamanetworkopen.2026.6862. URL: https://doi.org/10.1001/jamanetworkopen.2026.6862 — 178 名有效問卷（SGO/ABS）；GYO 99.3% 願意開 HRT（RO 73.8%）；願意者中 GYO 91.2% 選合併 E+P（RO 70.0%）；雌激素單方僅約 25–27%。態度調查，非療效資料。Route: Europe PMC REST + fullTextXML grep
- **[S15] PASS** — Muka T, Oliver-Williams C, Kunutsor S, et al. (2016). *Association of Age at Onset of Menopause…With Cardiovascular Outcomes…and All-Cause Mortality: A Systematic Review and Meta-analysis.* JAMA Cardiol 1(7):767-776. PMID 27627190, doi 10.1001/jamacardio.2016.2415. URL: https://doi.org/10.1001/jamacardio.2016.2415 — <45 歲停經：CHD RR 1.50（1.28–1.76）、CVD 死亡 1.19（1.08–1.31）、全因死亡 1.12（1.03–1.21）；32 篇、310,329 人。Route: Europe PMC REST
- **[S16] PASS（含限制）** — 衛生福利部中央健康保險署。《全民健康保險藥品給付規定》第 5 節 激素及影響內分泌機轉藥物（115.08.21 更新版）。URL: https://www.nhi.gov.tw/ch/dl-42511-66ac909b574f4f5c9c1c96042873cab4-1.pdf （章節索引頁 https://www.nhi.gov.tw/ch/np-3397-1.html ）— 5.3.1 Estradiol 經皮製劑兩條限制條文（Estraderm TTS 限不能口服者；Climara 50 限每週一片）；全節 grep estriol／conjugated／tibolone／progest 之專屬給付限制＝0 筆；**無排除癌症病人之條文**。限制：個別品項之收載與健保價屬品項檔層級，本環境取不到（同 C-S42），不得據此宣稱「有給付」。Route: WebFetch 索引 → curl --cacert 下載 PDF → pdftotext → grep
- **[S17] PASS** — Kirchheiner K, Nout RA, Lindegaard JC, et al.; EMBRACE Collaborative Group. (2016). *Dose-effect relationship and risk factors for vaginal stenosis after definitive radio(chemo)therapy with image-guided brachytherapy for locally advanced cervical cancer in the EMBRACE study.* Radiother Oncol 118(1):160-166. PMID 26780997, doi 10.1016/j.radonc.2015.12.025. URL: https://doi.org/10.1016/j.radonc.2015.12.025 — 630 人；2 年 G≥2 狹窄 21%；風險 20%@65 Gy／27%@75／34%@85（直腸陰道參考點）；提出 ≤65 Gy 規劃目標。Route: Europe PMC REST
- **[S18] PASS** — Westerveld H, Kirchheiner K, Nout RA, et al. (2022). *Dose-effect relationship between vaginal dose points and vaginal stenosis in cervical cancer: An EMBRACE-I sub-study.* Radiother Oncol 168:8-15. PMID 35063582, doi 10.1016/j.radonc.2021.12.034. URL: https://doi.org/10.1016/j.radonc.2021.12.034 — 301 人、中位追蹤 49 個月：狹窄 G0 25%／G1 52%／G2 20%／G3 3%。Route: Europe PMC REST
- **[S19] PASS（＝C-S31）** — Kirchheiner K, Nout RA, Tanderup K, et al. (2014). *Manifestation pattern of early-late vaginal morbidity…: an analysis from the EMBRACE study.* Int J Radiat Oncol Biol Phys 89(1):88-95. PMID 24725693, doi 10.1016/j.ijrobp.2014.01.032. URL: https://doi.org/10.1016/j.ijrobp.2014.01.032 — 588 人；2 年 G≥1 89%／G≥2 29%／G≥3 3.6%；狹窄最常見。狹窄專屬數字使用權在 D2（C 簡報已讓渡）。Route: Europe PMC REST（C 組已驗，本組沿用書目）
- **[S20] PASS（＝C-S33）** — Miles T, Johnson N. (2014). *Vaginal dilator therapy for women receiving pelvic radiotherapy.* Cochrane Database Syst Rev (9):CD007291. PMID 25198150, PMC6513398, doi 10.1002/14651858.CD007291.pub3. URL: https://doi.org/10.1002/14651858.cd007291.pub3 — 放療期間常規擴張無可靠證據；放療後觀察性關聯、因果未定。Route: Europe PMC REST（C 組已驗，本組沿用書目）
- **[S21] PASS（＝C-S34，內容數字本組取得）** — Kirchheiner K, Zaharie A, Smet S, et al.; EMBRACE Collaborative Group. (2025). *Association Between the Regular Use of Vaginal Dilators and/or Sexual Activity and Vaginal Morbidity in Locally Advanced Cervical Cancer Survivors: An EMBRACE-I Study Report.* Int J Radiat Oncol Biol Phys 121(2):452-464. PMID 39278418, doi 10.1016/j.ijrobp.2024.09.011. URL: https://doi.org/10.1016/j.ijrobp.2024.09.011 — 882 名可分析、中位追蹤 60 個月；64% 規律擴張（定義：≥50% 追蹤回報擴張器及／或性活動）；5 年 G≥2 狹窄 23% vs 37%（多變項 HR 0.630，P=.001）；G≥1 乾澀 72 vs 67%、G≥1 出血 61 vs 34%（G≥2 不增）。Route: Europe PMC REST（resultType=core 摘要全文）
- **[S22] PASS** — Law E, Kelvin JF, Thom B, et al. (2015). *Prospective study of vaginal dilator use adherence and efficacy following radiotherapy.* Radiother Oncol 116(1):149-155. PMID 26164775, PMC5028178, doi 10.1016/j.radonc.2015.06.018. URL: https://doi.org/10.1016/j.radonc.2015.06.018 — 109 人（婦癌 46）；院方建議每週 3 次 ×52 週；12 個月平均依從 42%（36–48%）、第一季 56%→第四季 25%；82% 維持治療前尺寸。Route: Europe PMC REST
- **[S23] PASS** — Martins J, Vaz AF, Grion RC, Costa-Paiva L, Baccaro LF. (2021). *Topical estrogen, testosterone, and vaginal dilator in the prevention of vaginal stenosis after radiotherapy in women with cervical cancer: a randomized clinical trial.* BMC Cancer 21(1):682. PMID 34112100, PMC8191143, doi 10.1186/s12885-021-08274-w. URL: https://doi.org/10.1186/s12885-021-08274-w — 195 人四組（雌激素 66／睪固酮 34／潤滑劑 66／擴張器 29）；一年陰道體積平均 −25.47%、組間無差異；CTCAE 狹窄僅擴張器組未顯著惡化（p=0.37）。開放式、組數不均、回溯註冊。Route: Europe PMC REST
- **[S24] PASS** — Varytė G, Bartkevičienė D. (2021). *Pelvic Radiation Therapy Induced Vaginal Stenosis: A Review of Current Modalities and Recent Treatment Advances.* Medicina (Kaunas) 57(4):336. PMID 33915994, PMC8066324, doi 10.3390/medicina57040336. URL: https://doi.org/10.3390/medicina57040336 — 全文 grep：英國共識「start VDT four weeks after completing RT, perform VDT 2–3 times per week for 1–3 min…continue 9 to 12 months」；巴西 2019 共識 5–10 分鐘、2–3 次／週、期限與起始時點無共識；發生率範圍 1.2–88%、近年子宮頸約 60%（3 年內）；無證據支持放療期間開始。Route: Europe PMC REST + fullTextXML grep
- **[S25] PASS（＝C-S32）** — Suvaal I, Kirchheiner K, Nout RA, et al. (2023). *Vaginal changes, sexual functioning and distress of women with locally advanced cervical cancer treated in the EMBRACE vaginal morbidity substudy.* Gynecol Oncol 170:123-132. PMID 36682090, doi 10.1016/j.ygyno.2023.01.005. URL: https://doi.org/10.1016/j.ygyno.2023.01.005 — 113 名（陰道侵犯 ≤5 mm）；2 年 47% 無性活動。Route: Europe PMC REST（C 組已驗，本組沿用書目）
- **[S26] FAIL** — 陰道擴張器在台灣的健保給付／官方採購指引。WebSearch（「陰道擴張器 健保給付 放射治療後 自費 台灣」）無任何官方（nhi/mohw/hpa）結果；醫療服務給付項目檔（C-S37）為處置支付項目、不含居家醫材。→ gap：寫「自購醫材，管道與費用向放腫護理師或個管師確認」
- **[S27] PASS** — Elit L, Kennedy EB, Fyles A, Metser U. (2016). *Follow-up for cervical cancer: a Program in Evidence-Based Care systematic review and clinical practice guideline update.* Curr Oncol 23(2):109-118. PMID 27122975, PMC4835009, doi 10.3747/co.23.2742. URL: https://doi.org/10.3747/co.23.2742 — 前 2 年 q3–4 月、3–5 年 q6–12 月；病史＋完整身體檢查；穹窿抹片≤每年一次；PET/CT、影像、標記不建議常規；HPV DNA 可能較敏感（放療後）；5 年後回歸一般照護。Route: Europe PMC REST
- **[S28] PASS** — Salani R, Atallah D, Fader AN, Frimer M, Obermair A, Pareja R, Huang M. (2026). *Updates to post-treatment surveillance after curative intent treatment for patients with gynecologic cancers: A Society of Gynecologic Oncology clinical practice statement.* Gynecol Oncol 204:109-117. PMID 41308226, doi 10.1016/j.ygyno.2025.11.014. URL: https://doi.org/10.1016/j.ygyno.2025.11.014 — 摘要原文：追蹤證據薄弱、多回溯性；症狀回顧＋身體檢查最有效；陰道細胞學「negligible benefit」仍被常用；常規影像未證實益處；ctDNA 需更多研究。Route: Europe PMC REST
- **[S29] PASS** — Aryasomayajula C, Chanana A, Tandel M, et al. (2022). *The role of high-risk HPV testing in cervical cancer surveillance.* Gynecol Oncol 164(2):357-361. PMID 34836678, doi 10.1016/j.ygyno.2021.11.014. URL: https://doi.org/10.1016/j.ygyno.2021.11.014 — 262 名倖存者（169 名做 hrHPV）：陽性與復發無關（21% vs 24%，p=0.67）；無任何復發由 hrHPV 檢出；作者不支持常規使用。單一機構回溯。Route: Europe PMC REST
- **[S30] PASS** — Kechagias KS, Kalliala I, Bowden SJ, et al. (2022). *Role of human papillomavirus (HPV) vaccination on HPV infection and recurrence of HPV related disease after local surgical treatment: systematic review and meta-analysis.* BMJ 378:e070135. PMID 35922074, PMC9347010, doi 10.1136/bmj-2022-070135. URL: https://doi.org/10.1136/bmj-2022-070135 — 22 篇（統合 18）；CIN2+ 復發 RR 0.43（0.30–0.60；11 篇、19,909 人、中位追蹤 36 個月）；HPV16/18 相關 RR 0.26（0.16–0.43）；GRADE very low–moderate；作者：inconclusive、需大型 RCT。Route: Europe PMC REST
- **[S31-note] 零筆紀錄** — 侵襲性子宮頸癌治療後接種 HPV 疫苗之臨床結果研究：Europe PMC `TITLE:vaccination AND TITLE:"cervical cancer" AND TITLE:(after OR survivors) AND TITLE:(treatment OR treated)` ＝ **0 筆**（2026-08-30）。D3 據此寫「侵襲癌族群無直接證據」
- **[S32] PASS** — Meites E, Szilagyi PG, Chesson HW, Unger ER, Romero JR, Markowitz LE. (2019). *Human Papillomavirus Vaccination for Adults: Updated Recommendations of the Advisory Committee on Immunization Practices.* MMWR Morb Mortal Wkly Rep 68(32):698-702. PMID 31415491, PMC6818701, doi 10.15585/mmwr.mm6832a3. URL: https://doi.org/10.15585/mmwr.mm6832a3 — 26 歲以下補接種；27–45 歲非常規建議、採共同臨床決策。Route: Europe PMC REST
- **[S33] PASS** — 衛生福利部（資料來源：國民健康署）。〈男孩女孩齊接種　HPV遠離我 公費人類乳突病毒（HPV）疫苗擴大施打〉，建檔／更新 114-08-12。URL: https://mohw.gov.tw/cp-2704-83470-1.html — 原文已 grep：114 年 9 月起公費對象由國中女生擴大至國中男生（113 年入學全體國中生）；公費九價；15 歲以下 2 劑、間隔 ≥6 個月；校園集中接種＋合約院所補接種。Route: WebSearch → curl --cacert grep 原文
- **[S34] PASS** — 衛生福利部（國民健康署）。〈健康臺灣-114年起擴大癌症篩檢 您的健康政府來顧〉，建檔 113-12-24。URL: https://www.mohw.gov.tw/cp-16-80948-1.html — 原文已 grep：114/1/1 起增列 25–29 歲每 3 年 1 次抹片（補助 630 元）；新增 35、45、65 歲女性各 1 次 HPV 檢測（1,400 元）；30 歲以上「建議每3年至少做1次」句。Route: WebSearch → curl --cacert grep 原文
- **[S35] PASS** — 衛生福利部（國民健康署）。〈健康台灣！6分鐘護一生，子宮頸癌不來找〉，建檔 114-05-08、更新 114-05-22。URL: https://www.mohw.gov.tw/cp-2704-82414-1.html — 原文已 grep：「年滿30歲以上女性每年可接受1次免費子宮頸抹片檢查；年滿25歲（含）至29歲以上女性，每3年也享有1次免費抹片」；WHO 90-70-90 框架；發生率 25.2→7.6／10 萬（111 年）、死亡率 11→2.9（112 年）之官方數字。Route: WebSearch → curl --cacert grep 原文
- **[S36] FAIL** — 台灣 HPV **自採檢體**之公費政策官方公告。mohw.gov.tw 兩頁（S34、S35）均未提及自採；hpa.gov.tw 本環境 SSL 失敗無法存取（同 C-S43）；WebSearch 未見國健署自採公告。→ gap：公費 HPV 檢測之採檢方式寫「以合作院所說明為準」，不宣稱有無自採選項
- **[S37] PASS（媒體層級，僅供背景）** — 中央社。〈子宮頸癌篩檢升級 公費HPV檢測2025年開放3年齡適用〉2024-12-01（2025-04-18 更新）。URL: https://www.cna.com.tw/news/ahel/202412010095.aspx — 2018 年起國中女生公費接種；2018–2021 入學世代兩劑完成率 75.2%／86%／86.1%／91.7%（國健署統計、經媒體轉述）。**引用時標媒體來源或不用於正文數字**。Route: curl grep 原文
- **[S38] PASS** — Bizzarri N, Querleu D, Ricotta G, et al. (2025). *Complications and Recurrence After Pelvic Exenteration for Gynecologic Malignancies: Survival Analysis From the COREPEX Study.* Obstet Gynecol 146(5):737-749. PMID 40934517, PMC12520032, doi 10.1097/aog.0000000000006051. URL: https://doi.org/10.1097/aog.0000000000006051 — 862 人（2005–2023，多中心國際回溯）；切緣陰性 78.4%；預後四組 5 年 OS 54.3／40.4／24.0／4.3%；DFS 43.7／24.9／22.2／8.0%；遠端復發最常見（32.1%）。Route: Europe PMC REST
- **[S39] PASS** — Di Donato V, Kontopantelis E, De Angelis E, et al.; Pelvic Exenteration Study Group. (2025). *Evaluation of survival and mortality in pelvic exenteration for gynecologic malignancies: a systematic review, meta-analyses, and meta-regression study.* Int J Gynecol Cancer 35(6):101829. PMID 40373347, PMC12751357, doi 10.1016/j.ijgc.2025.101829. URL: https://doi.org/10.1016/j.ijgc.2025.101829 — 46 篇、4,417 人（子宮頸 3,183）；30 天死亡率 5.1%（敗血症 27.2% 為首因）；骨盆壁侵犯、淋巴結陽性為壞因子；圍術期死亡率逐年下降。（合併 5 年 OS 之單一數字不在摘要內、全文本環境取不到——引用限摘要層級。）Route: Europe PMC REST
- **[S40] PASS** — Shen Z, Qu A, Jiang P, Jiang Y, Sun H, Wang J. (2022). *Re-Irradiation for Recurrent Cervical Cancer: A State-of-the-Art Review.* Curr Oncol 29(8):5262-5277. PMID 35892987, PMC9331513, doi 10.3390/curroncol29080418. URL: https://doi.org/10.3390/curroncol29080418 — 再程放療毒性高（尤其照野內短期復發）；SBRT／HDR-ISBT 有初步成果；異質性大、缺大型前瞻研究、無法下確定結論。Route: Europe PMC REST
- **[S41] PASS** — Tewari KS, Sill MW, Long HJ 3rd, et al. (2014). *Improved survival with bevacizumab in advanced cervical cancer.* N Engl J Med 370(8):734-743. PMID 24552320, PMC4010094, doi 10.1056/NEJMoa1309748. URL: https://doi.org/10.1056/nejmoa1309748 — GOG-240，452 人；OS 17.0 vs 13.3 個月（HR 0.71）；ORR 48 vs 36%；≥G2 高血壓 25 vs 2%、≥G3 血栓 8 vs 1%、≥G3 腸胃瘻管 3 vs 0%。Route: Europe PMC REST
- **[S42] PASS** — Tewari KS, Sill MW, Penson RT, et al. (2017). *Bevacizumab for advanced cervical cancer: final overall survival and adverse event analysis…(Gynecologic Oncology Group 240).* Lancet 390(10103):1654-1663. PMID 28756902, PMC5714293, doi 10.1016/s0140-6736(17)31607-0. URL: https://doi.org/10.1016/s0140-6736(17)31607-0 — 最終 OS 16.8 vs 13.3 個月（HR 0.77，p=0.007）；瘻管（任何級）15% vs 1%，全部發生於照射過的病人；G3 瘻管 6%，無手術急症或死亡。Route: Europe PMC REST
- **[S43] PASS** — Colombo N, Dubot C, Lorusso D, et al.; KEYNOTE-826 Investigators. (2021). *Pembrolizumab for Persistent, Recurrent, or Metastatic Cervical Cancer.* N Engl J Med 385(20):1856-1867. PMID 34534429, doi 10.1056/NEJMoa2112435. URL: https://doi.org/10.1056/nejmoa2112435 — 三層人群設計（CPS≥1／全體／CPS≥10）；PFS 10.4 vs 8.2（HR 0.62／0.65／0.58）；24 個月 OS 53.0 vs 41.7% 等。Route: Europe PMC REST
- **[S44] PASS** — Monk BJ, Colombo N, Tewari KS, et al. (2023). *First-Line Pembrolizumab + Chemotherapy…: Final Overall Survival Results of KEYNOTE-826.* J Clin Oncol 41(36):5505-5511. PMID 37910822, doi 10.1200/jco.23.00914. URL: https://doi.org/10.1200/jco.23.00914 — 最終 OS：CPS≥1 28.6 vs 16.5（HR 0.60）；全體 26.4 vs 16.8（HR 0.63）；CPS≥10 29.6 vs 17.4（HR 0.58）；G≥3 AE 82.4 vs 75.4%。Route: Europe PMC REST
- **[S45] PASS** — Tewari KS, Monk BJ, Vergote I, et al. (2022). *Survival with Cemiplimab in Recurrent Cervical Cancer.* N Engl J Med 386(6):544-555. PMID 35139273, doi 10.1056/NEJMoa2112187. URL: https://doi.org/10.1056/nejmoa2112187 — EMPOWER-Cervical 1，608 人、鉑類後進展、不限 PD-L1、排除先前免疫治療：OS 12.0 vs 8.5（HR 0.69）；ORR 16.4 vs 6.3%；G≥3 45.0 vs 53.4%。Route: Europe PMC REST
- **[S46] PASS** — Vergote I, González-Martín A, Fujiwara K, et al.; innovaTV 301/ENGOT-cx12/GOG-3057 Collaborators. (2024). *Tisotumab Vedotin as Second- or Third-Line Therapy for Recurrent Cervical Cancer.* N Engl J Med 391(1):44-55. PMID 38959480, doi 10.1056/NEJMoa2313811. URL: https://doi.org/10.1056/nejmoa2313811 — 502 人；OS 11.5 vs 9.5（HR 0.70，p=0.004）；PFS 4.2 vs 2.9；ORR 17.8 vs 5.2%；G≥3 治療期 AE 52.0 vs 62.3%；14.8% 因毒性停藥。Route: Europe PMC REST
- **[S47-note] 零筆紀錄** — 子宮頸癌寡轉移之隨機證據：Europe PMC `TITLE:oligometastatic AND TITLE:"cervical cancer" AND TITLE:(randomized OR randomised OR "phase 3" OR "phase III")` ＝ **0 筆**；`TITLE:oligometastatic AND TITLE:cervical AND TITLE:review` ＝ 0 筆（2026-08-30）。D4 據此寫「無子宮頸專屬隨機資料」，僅引 ESGO 共識級建議 [S1]
- **[S48] PASS（含明確陰性結果）** — 衛生福利部中央健康保險署。《全民健康保險藥品給付規定》第 9 節 抗癌瘤藥物（115.8.21 更新版，官方 PDF 已下載、pdftotext 全文 grep）。URL: https://www.nhi.gov.tw/ch/dl-55685-99c675b771ab4b2789c891bc8db447ce-1.pdf （章節索引頁 https://www.nhi.gov.tw/ch/np-3397-1.html ）— **9.37.4 Bevacizumab**：「持續性、復發性或轉移性之子宮頸癌」與 cisplatin+paclitaxel 或（無法用鉑類者）paclitaxel+topotecan 合併；事前審查、每次 15 週、續用需影像無惡化（109/6/1、113/3/1）。**陰性查證**：全文「子宮頸」僅 4 處（均為 9.37.4 及附表原位癌註記）；**9.69 免疫檢查點抑制劑之給付癌別不含子宮頸癌（pembrolizumab、cemiplimab 均無）；tisotumab 全文 0 筆**。Route: curl --cacert 下載 → pdftotext → grep
- **[C-S35]／[C-S36]／[C-S37]／[C-S42]／[C-S43]／[C-S47]** — 沿用 C 簡報之來源與 FAIL 紀錄（癌症資源中心 82→104 家與 0809-010580；醫療服務給付項目 XLS；cisplatin 品項檔阻擋；hpa.gov.tw SSL 失敗；陰道雌激素給付 gap）。URL 見 `/home/claude/cervix/brief/C.md` 來源清單。
