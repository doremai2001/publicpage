# Brief A — 食道癌專題「治療怎麼決定」群（A1–A4）

研究員：Group A｜查證日期：2026-09-02｜期刊書目資料全部經 Europe PMC REST 逐筆核對（title／journal／year／volume(issue)／pages／DOI／PMID／isOpenAccess）；每個 Key facts 的數字都在該來源的摘要（abstractText）或可取得的全文 XML 裡看得到；指引原文引語出自可取得之 OA 全文；台灣官方頁面經實際抓取（mohw.gov.tw、dep.mohw.gov.tw、law.moj.gov.tw；hpa.gov.tw 與 nhi.gov.tw 全部抓不到，見 FAIL）。
引用規則：**只有標 PASS 的來源可以進正文引用。** FAIL 條目保留，讓作者知道查過什麼、哪些話只能寫「查不到可引用的來源」。
來源編號 [S1]…[S76] 全 brief 唯一；同一篇論文被多篇文章用，同一個編號。

---

## ⚠ 與 SPEC 假設不同形狀的事（動筆前必讀）

1. **CMISG1701 不是「nCRT＋手術 vs 根治性化放療」的試驗。** 它比較的是「術前化放療＋微創食道切除」對「術前化療＋微創食道切除」（中國鱗癌 cT3-4aN0-1M0，n=264）[S45][S46][S47]。3 年 OS 64.1% vs 54.9%，HR 0.82（95% CI 0.58–1.18，p=0.28）——**沒有顯著差異**，pCR 27.7% vs 2.9%[S47]。A4 裡它的位置要改成「化放療比化療多出來的病理反應，沒有換成存活差」的註腳，不能放進「開不開刀」的比較表。SPEC §五 A4 的清單要修。
2. **SANO 已經有主要結果（Lancet Oncol 2025;26:425–436）[S49]，而且是「非劣性成立、但方向不利」的結果。** 2 年 OS 主動監測 74% vs 標準手術 71%，非劣性成立（邊界 15%）；但族群 **腺癌約四分之三、鱗癌只約 21–24%**[S53]；中位追蹤只有 38 個月[S49]；中位 OS 43 vs 53 個月（HR 1.14，95% CI 0.74–1.78，無統計差異）[S52]；作者自己承認遠端轉移率「非顯著差異、方向偏向標準手術」，且「不能排除長期追蹤後出現有意義的差別、進而反映在 OS 上」[S54]。主動監測組 198 人裡，48% 出現局部再生長、17% 出現遠端轉移、35% 維持 cCR[S52]；以更長追蹤（中位 54 個月）計，**只有 25% 維持 cCR**[S51]。2026 年 JAMA Surgery 用 SANO 資料做的決策模型，5 年時手術在 QALY 與生命年數都較好[S55]。→ A4 的敘事不是「試驗還沒讀出」，而是「試驗讀出了 2 年非劣，但族群是荷蘭腺癌、追蹤短、遠端轉移方向不利、長期結果未出」。
3. **「臨床完全反應」與「病理完全反應」在 SANO 裡差很多。** SANO 標準手術組 101 位「臨床完全反應」病人開刀後，只有 36 位（35.6%）是 pT0（此數字出自一篇批評 SANO 的 JTCVS Open 編輯評論，引 SANO 附錄表 S6）[S53]。preSANO 的「漏診率」是針對 TRG3-4（>10% 殘存）算的：一般切片 31%、bite-on-bite 切片＋FNA 10%、EUS 28%、PET-CT 15%[S38]；中國鱗癌 preSINO 的陰性預測值只有 68.7%[S62]。紅線 1 的核心句子有了硬數字。
4. **ESOSTRATE（法國）已終止**：ClinicalTrials.gov NCT02551458 狀態 TERMINATED，原因欄「sub-optimal inclusion rate, additional 9 years to finalize inclusion and follow-up of all patients」，實收 188 人[S58]；查無結果發表。**NEEDS 仍在收案**：NCT04460352 RECRUITING，目標 1,020 人（protocol 原寫 1,200[S56]），主要完成日估 2026-12-31、整體完成估 2031-12-31[S57]——正文要寫「最快也要幾年後才有主要結果」。
5. **ASCO 沒有 2024 年的「局部晚期食道癌」指引更新。** 能查到的是 Shah 2020 JCO（局部晚期）[S32]與 2023／2026 的「晚期胃食道癌免疫與標靶」更新（歸 B2）。SPEC 寫的「Shah 2020/2024」要改成 2020。
6. **ESMO 2025 年 interim update 把腺癌的路寫得比 SPEC 更硬**：「Patients with resectable, locally advanced AC of the oesophagus or OGJ should be treated with perioperative FLOT followed by surgery [I, A]」、「Neoadjuvant CRT may be considered if the patient is not suitable for FLOT [I, C]」[S15]。A1 寫腺癌時可以直接引這兩句，不是「另一條路可選」而是「FLOT 為預設」。
7. **ESMO 對鱗癌「化放療後手術 vs 根治性化放療」的措辭可以逐字引，但出處是 2025 interim update 的演算法註腳，不是 2022 CPG 正文**（2022 CPG 全文抓不到，見 FAIL-1）：「Evidence suggests that neoadjuvant CRT followed by surgery and definitive CRT is equally effective with regard to OS. Oesophageal surgery should be carried out in experienced (high-volume) centres only. For patients not willing to undergo oesophageal surgery or who are medically unfit for major surgery, definitive CRT should be preferred. Even many experienced centres prefer definitive CRT for oesophageal tumours with a very proximal/cervical location.」[S15]
8. **台灣官方能抓到的食道癌「發生數」停在 107 年（2018）：2,778 人**（衛福部 110-11-16 新聞稿）[S4]；111、112 年癌登新聞稿只給名次（男性標準化發生率第 6 位）與性別比（男性為女性 12.5 倍）[S2][S3]。**死亡數有最新的：113 年（2024）食道癌死亡 2,076 人（男 1,926），每十萬人口 8.9、標準化 4.7，死亡年齡中位數 63 歲（十大癌症中最年輕之一）**[S1]。鱗癌比例的官方數字抓不到；可用癌登資料庫研究：2008–2014、40–79 歲，鱗癌 96.6%、男性 94.4%[S5]（注意分母只含鱗癌＋腺癌）。
9. **台灣的觀察性資料方向一致偏向手術**：癌登 2008–2016、7,637 位 cT1b-4N0/+M0 鱗癌，配對後 5 年 OS 根治性化放療 19.8% vs nCRT＋手術 31.2% vs 單純手術 30.5%[S33]。這是傾向分數配對的回溯資料，不是隨機試驗；要與 FFCD 9102／Stahl／Cochrane「加手術不增加 OS」並陳，並說明選擇偏差方向（被送去 dCRT 的人本來就較差）。
10. **JCOG0909（日本）給了「根治性化放療＋救援手術」策略一個前瞻數字**：cStage II/III 鱗癌 n=94，CR 59%，3 年 OS 74.2%[S63]；日本食道學會指引引其最終分析：5 年 OS 64.5%、**5 年食道保留率 54.9%**、救援手術 26%、R0 76%、術後 G3-4 併發症 20%、1 例手術死亡[S30]。

---

## A1 `ec-two-diseases`〈鱗癌和腺癌，其實是兩種病〉

### Key facts

**台灣流行病學（全部官方或癌登資料庫）**

- 死亡：113 年（2024）食道癌死亡 **2,076 人**，每十萬人口 8.9 人、標準化死亡率 4.7；十大癌症死因第 9 位；男性 1,926 人（每十萬 16.7、標準化 9.3）→ 女性約 150 人；**死亡年齡中位數 63 歲**（全癌症 71 歲；口腔癌、食道癌、卵巢癌皆僅 63 歲）[S1]。歷年死亡數：97 年 1,512 → 107 年 2,036 → 113 年 2,076（經轉換比值調整後值）[S1]。
- 發生：107 年（2018）**2,778 人**罹患食道癌，「罹癌者 9 成以上為男性，好發於 50–70 歲，為男性中癌症標準化發生率第 6 位」[S4]。111 年與 112 年癌登：食道癌仍是男性標準化發生率第 6 位；**男性食道癌標準化發生率為女性的 12.5 倍**（111 年）[S2][S3]。
- 組織型態與期別（癌登＋健保資料庫，2008–2014，40–79 歲，n=7,763）：**鱗癌 96.6%、腺癌 3.4%**（分母為鱗癌＋腺癌）、男性 94.4%；鱗癌好發 50–59 歲，腺癌風險隨年齡遞增；**77.1% 確診時為第 III/IV 期**；鱗癌期別分布：0 期 0.9%、I 期 5.3%、II 期 16.5%、III 期 48.5%、IV 期 28.8%；腺癌：I 期 10.0%、II 期 17.8%、III 期 32.4%、IV 期 39.7%[S5]。
- 趨勢（癌登 1985–2019）：男性鱗癌年齡標準化發生率平均年增 4.2%（AAPC 4.2，95% CI 3.1–5.4）、男性腺癌 1.2%、女性鱗癌 1.7%；出生世代效應與 1970–1995 年間危險因子盛行率上升相關[S6]。
- 全球對照：2018 年全球食道癌 57.2 萬例，鱗癌 48.2 萬（ASR 5.3）、腺癌 8.5 萬（ASR 0.9）；東亞鱗癌 ASR 最高（11.1），北歐腺癌最高（3.5）；「rates of OAC exceed those of OSCC in an increasing number of high-income countries」[S13]。日本：鱗癌約 86%、腺癌約 7%[S30]。

**危險因子——台灣本土病例對照研究**

- Lee CH 2005（多中心，鱗癌 513 vs 對照 818）：三種物質都有劑量反應；**酒是最強單一因子**（>900 g/day-year 者 OR 13.9）；「酒的量比年數重要，菸的年數比量重要」；任兩種併用 OR 8.8–19.7，**三種都用 OR 41.2**；酒×菸為相乘交互、酒×檳榔為相加交互；三者合計歸因分率 83.7%[S7]。
- Wu IC 2006（高雄，鱗癌 165 vs 對照 255，全男性）：吸菸 aOR 5.4（PAR 72%）、飲酒 aOR 17.6（PAR 76%）；單純嚼檳榔僅邊緣顯著（aOR 1.7，95% CI 0.8–3.1），但**加荖花者 aOR 4.2、吞檳榔汁者 aOR 3.3**；三者有協同效應；作者推論「檳榔汁與黏膜直接接觸」可能參與致癌[S8]。
- 官方版：國健署引研究「嚼檳榔者罹患上消化道（口腔、咽、喉、食道）癌症風險，較不嚼檳榔者之風險增加 5 倍，若檳榔、菸、酒三者皆有使用習慣，罹患上呼吸消化道癌之風險更高達 10.5 倍」[S2]。

**ALDH2 與喝酒臉紅**

- Lee CH 2008（台灣多中心，鱗癌 406 vs 對照 656）：在相同飲酒量下，風險隨 ADH1B*1 與 ALDH2*2 等位基因數上升；**ALDH2*1/*2（活性不足）與低至中度飲酒（0.1–30 g/day）、重度飲酒（>30 g/day）呈相乘交互，聯合 aOR 分別 14.5 與 102.6**；低中度飲酒者中，ALDH2 變異的效應只在吸菸者顯著[S9]。
- Brooks 2009 PLoS Med：約 **36% 的東亞人**（日、中、韓）有酒後臉紅反應（ALDH2 缺乏）；ALDH2*2 為半顯性，異合子活性不到正常一半、實際降低超過 100 倍；ADH1B 變異與之交互作用[S10]。
- 熱飲：IARC 2016 年將「超過 65°C 的極熱飲品」列為 2A 級可能致癌物（Loomis 2016 Lancet Oncol 為 IARC 專論工作小組摘要，Europe PMC 無摘要文字，只能引書目）[S11]；衛福部新聞稿原文：「世界衛生組織（WHO）將超過攝氏 65 度的熱飲定為食道癌可能的致癌因子」[S4]。官方列出的食道癌致癌因子還包括「含亞硝胺食物（如醃漬、煙燻食物）、食道曾受腐蝕傷害、吞嚥功能疾病、胃食道逆流、肥胖及口腔衛生不良」[S4]。

**腺癌（逆流、巴瑞特食道、肥胖）**

- Lagergren 1999 NEJM（瑞典全國病例對照，食道腺癌 189、賁門腺癌 262、對照 820、鱗癌 167）：反覆逆流症狀者食道腺癌 OR 7.7（95% CI 5.3–11.4），賁門腺癌 OR 2.0；**長期且嚴重逆流者 OR 43.5**（18.3–103.5）；逆流與鱗癌無關（OR 1.1）[S12]。
- 肥胖：官方致癌因子清單列「肥胖」[S4]。專屬統合分析（如 BEACON 合併分析）Europe PMC 查詢失敗，未能核對，**不引數字**（見 FAIL-9）。
- 巴瑞特食道的進展率：本組未查到可 PASS 的數字，A1 只寫「逆流→巴瑞特食道→腺癌」的路徑概念，不寫年進展率（gap）。

**腺癌的治療走另一條路——ESOPEC 與 ESMO 2025 措辭**

- ESOPEC（德國，NEJM 2025，可切除食道腺癌 cT1cN+ / cT2-4a，FLOT 221 vs CROSS 217）：中位追蹤 55 個月，**3 年 OS 57.4% vs 50.7%，HR 0.70（95% CI 0.53–0.92，p=0.01）**；3 年 PFS 51.6% vs 35.0%（HR 0.66）；≥G3 不良事件 58.0% vs 50.0%；**術後 90 天死亡率 3.1%（FLOT）vs 5.6%（CROSS）**[S14]。ESMO interim update 補充：中位 OS 66 vs 37 個月；5 年 OS 50.6% vs 38.7%[S15]。
- ESMO 2025 interim update 建議原文：「Multimodality treatment should be considered in all patients with locally advanced resectable oesophageal cancer [I, A].」「**Patients with resectable, locally advanced AC of the oesophagus or OGJ should be treated with perioperative FLOT followed by surgery [I, A; ESMO-MCBS v1.1 score: A].**」「Neoadjuvant CRT may be considered if the patient is not suitable for FLOT [I, C].」[S15]
- 反方向／背景：Neo-AEGIS（歐洲 24 中心，腺癌 cT2-3N0-3M0，n=362，2020 年因無效性分析提前關閉）：周術期化療 vs CROSS，3 年 OS 55% vs 57%，HR 1.03（0.77–1.38）——**打平**；但化療組 85% 用的是舊的 ECF/EOX 而非 FLOT[S15][S16]；pCR、主要病理反應、R0 均偏向三合一[S16]。SANO 作者也提醒 ESOPEC 化放療組的 pCR 只有 10%、完成率 75%（CROSS 試驗是 23%、91%）[S54]——寫「FLOT 勝出」時把這個註腳放進去。
- 鱗癌在 CROSS 裡的效應比腺癌大：中位 OS 鱗癌 81.6 vs 21.1 個月（HR 0.48，95% CI 0.28–0.83）；腺癌 43.2 vs 27.1 個月（HR 0.73，0.55–0.98）[S17]。pCR：鱗癌 49%、腺癌 23%（此兩數出自 CROSS 全文，可引用的 OA 出處為 preSINO protocol 對 CROSS 的轉述）[S61]。

### 反方向的資料（誠實必列）
- 台灣的「9 成以上是鱗癌」來自 2008–2014 的癌登樣本（且分母排除其他組織型態）[S5]；男性腺癌發生率也在緩升（AAPC 1.2）[S6]——不能寫成「台灣沒有腺癌」。
- 檳榔的獨立效應在 Wu 2006 只有邊緣顯著，效應主要在「加荖花、吞汁」與菸酒協同[S8]；Lee 2005 顯示酒×檳榔是相加不是相乘[S7]。寫「檳榔是食道癌危險因子」時，強度要低於菸酒，不可寫成「檳榔本身致食道癌風險 41 倍」（41.2 是三者合用）。
- Neo-AEGIS 打平（多為 ECF/EOX）[S16]；ESOPEC 化放療組表現偏弱[S54]。

### Claim ceiling
- **可寫**：「台灣食道癌九成以上是鱗癌、九成以上是男性，死亡年齡中位數 63 歲、比全癌症早 8 年」；「菸、酒、檳榔三者都用，風險是都不用的四十倍左右（台灣病例對照）」；「喝酒會臉紅的人（ALDH2 活性不足，東亞約三分之一）即使喝不多，食道鱗癌風險也顯著上升，重度飲酒者聯合勝算比破百」；「腺癌的預設路徑是周術期 FLOT 化療＋手術（ESMO 2025 [I, A]），ESOPEC 顯示 FLOT 的 3 年存活比 CROSS 高 6.7 個百分點」。
- **不可寫**：把勝算比寫成「機率倍數」；「有逆流就會得腺癌」（OR 7.7 是相對於無症狀者、在低基礎發生率的族群）；「腺癌不能做化放療」（ESMO 仍保留 nCRT [I, C] 給不適合 FLOT 者；Neo-AEGIS 打平）；「熱飲致癌已證實」（IARC 2A＝可能致癌）；任何「因為你抽菸喝酒所以…」的責備句式（SPEC §三）。
- 巴瑞特食道進展率、肥胖 OR：**本 brief 沒有 PASS 數字，不寫數字**。

### Caveats／safety notes
- 戒斷寫成治療的一部分：指向 C4；官方資源見台灣端。
- 本篇是鱗癌／腺癌分流的唯一主場；A2–A4 遇到腺癌一句話指回本篇。

### 台灣端
- 死亡與發生數字：見 Key facts [S1][S2][S3][S4][S5]。**gap**：111／112 年食道癌的絕對新發人數與鱗癌比例的官方數字抓不到（hpa.gov.tw TLS 失敗，FAIL-6）。
- 重大傷病：食道癌（C15）屬「一、需積極或長期治療之癌症（五）除（一）～（四）之其他惡性腫瘤（C00.0–C96.9）」，證明有效期限 **五年**；一百十四年一月一日以後適用版亦同[S73]。由醫師開立診斷證明（30 日內有效）、附病歷摘要，可由醫院代辦[S73]。
- 戒菸：國健署免付費戒菸專線 **0800-636363**，週一至週六 09–21 時，Line 官方帳號 @tsh0800636363；官方稱專線個案戒菸成功率約四成[S74]。
- 戒檳榔：衛福部口腔健康司「戒檳諮詢服務醫療機構查詢」（115-08-17 建檔）提供各縣市戒檳諮詢醫療機構名冊與專線[S75]。
- 戒酒：衛福部「115 年度酒癮治療費用補助方案」——補助非健保給付之自費酒癮治療，**每人每年度上限 4 萬元**（其中藥費上限 2 萬元）、限 Naltrexone／Acamprosate／Disulfiram，須至指定酒癮治療機構[S76]。**不可寫成「健保給付戒酒」**——這是衛福部公務預算補助，不是健保。

### 給繪圖組的數字
- 台灣鱗癌 vs 腺癌期別分布長條圖（0/I/II/III/IV：鱗癌 0.9/5.3/16.5/48.5/28.8%；腺癌 0/10.0/17.8/32.4/39.7%）[S5]。
- 三物質 OR 階梯：單一 → 任兩種 8.8–19.7 → 三種 41.2[S7]。
- 兩條路：鱗癌→CROSS（pCR 49%）／腺癌→FLOT（ESOPEC 3 年 OS 57.4 vs 50.7）[S14][S61]。

---

## A2 `ec-workup`〈決定能不能開刀的，是這幾張檢查〉

### Key facts

**三種分期工具各自的長處（統合分析）**

- van Vliet 2008（Br J Cancer，2006 年前文獻）：區域淋巴結轉移——**EUS 敏感度 0.80／特異度 0.70；CT 0.50／0.83；FDG-PET 0.57／0.85**（三者無顯著差異）；EUS 對腹腔幹淋巴結敏感度 0.85、特異度 0.96；遠端轉移——**PET 敏感度 0.71／特異度 0.93 vs CT 0.52／0.91**，PET 顯著優於 CT；結論「EUS 對區域淋巴結最敏感，CT 與 PET 較特異；遠端轉移 PET 敏感度較高；合併使用有臨床價值」[S18]。
- Puli 2008（WJG，49 篇、n=2,558，以手術病理為金標準）：EUS 診斷 T1 敏感度 81.6%／特異度 99.4%；**T4 敏感度 92.4%／特異度 97.4%**；加 FNA 後 N 分期敏感度從 84.7% 升至 96.7%[S19]。
- van Westreenen 2004（JCO，12 篇）：PET 對局部區域轉移敏感度 0.51／特異度 0.84；**遠端轉移敏感度 0.67／特異度 0.97**[S20]。
- Flamen 2000（JCO 前瞻，n=74）：PET 對第 IV 期的準確度 82% vs CT＋EUS 64%（p=0.004）；**PET 改變 22% 病人的分期**（升期 15%、降期 7%）；局部淋巴結 PET 敏感度 33% vs EUS 81%[S22]。
- ACOSOG Z0060（Meyers 2007，前瞻多中心，CT 無轉移之可切除病人 n=189 可分析）：PET 找到並經確認的 M1b **至少 4.8%（95% CI 2.2–8.9%）**；另有 PET 陽性未確認、與 PET 未發現但開刀時發現 M1 各數例；22% 最終未接受食道切除[S21]。
- EUS 在 PET/CT 之後還改變什麼（Hulshoff 2017，回溯 n=279）：EUS 改變 28.7% 病人的處置——放療照野 22.6%、淋巴結清掃範圍 17.2%、可治癒性僅 1.8%[S28]。
- 化放療後再分期 EUS 不可靠（Sun 2015 統合，n=724）：T4 敏感度 43%／特異度 96%；N 分期敏感度 69%／特異度 52%；「Tumors restaged by EUS as T4 should not be assigned to surgery」[S29]。
- 化放療後間隔轉移：preSANO 第二次反應評估的 PET-CT 在 190 人中找到 **18 人（9%）** 組織證實的遠端轉移（1 鱗癌、17 腺癌）[S38]；preSINO（鱗癌）PET-CT 術前找到 13/268（4.9%）[S62]。

**支氣管鏡：上／中段腫瘤與氣道侵犯**

- Riedel 1998（Chest，前瞻 116 人/150 次）：氣管分叉以上腫瘤 32% 有巨觀異常；氣道正常外觀的陰性預測值 98.5%，但巨觀異常的陽性預測值低（放療後尤然）；加多點切片與刷檢後總準確度 95.8%；**9.7% 原本可開刀的病人因支氣管鏡證實氣道侵犯而排除手術**；支氣管鏡與 CT 結果 40% 不一致，支氣管鏡特異度與 PPV 較高[S24]。
- Riedel 2001（Chest，前瞻 166 人/220 次，supracarinal）：57.3% 無異常；正常外觀 NPV 94.4%；證實侵犯者 8.6%；**18.1% 原本可開刀者因此排除手術**，總準確度 93.3%（95% CI 86.7–97.3%）；6 例假陰性皆為新輔助治療後手術者[S23]。
- Nishimura 2002（前瞻 59 人，位於或高於氣管分叉）：診斷氣管支氣管侵犯的準確度——支氣管鏡 78%、支氣管內超音波 91%、EUS 85%、CT 58%[S23 補充來源，見來源清單 S23b]。

**T4 與氣道侵犯的治療方向**

- Lee CC 2022（Acta Oncol，23 篇、n=1,119，93% 鱗癌）：T4 N any M0——化放療＋手術 1/3/5 年 OS 65%／36%／20%；單獨化放療 30%／11%／10%；治療相關廔管 4%（CRT-S）vs 9%（CRT）；治療相關死亡各 3%；作者強調「lack of high-quality evidence」、兩組族群不可比[S27]。
- 日本食道學會 CQ14：「There is only weak evidence to recommend surgical resection for patients with unresectable, locally advanced esophageal cancer (cT4 [e.g., aorta, trachea, bronchus] N0-3M0) that becomes resectable after definitive chemoradiotherapy or induction chemotherapy.」（共識 89.3%、證據等級 C）；CQ12：不可切除 cStage IVA 以根治性化放療為弱建議（共識 100%、C）[S30]。

**AJCC 第 8 版：cTNM／pTNM／ypTNM 是三套**

- Rice 2017（CA Cancer J Clin）：第 8 版新增「臨床（治療決定前）」與「新輔助治療後病理」兩套分期分組，因為它們的存活與純病理分期不對應；**鱗癌與腺癌在 cTNM 與 pTNM 需分開分組，但 ypTNM 分組兩者相同**；來自 Worldwide Esophageal Cancer Collaboration 六大洲資料[S25]。Rice 2017 JTO primer：pT1 細分 pT1a/pT1b；新的食道專用區域淋巴結圖；食道胃接合部定義修訂[S26]。
- 寫給病人的翻譯：「開刀前的期別（c）、只開刀的病理期別（p）、先化放療再開刀的病理期別（yp）是三張不同的表，不能互相換算」——這句話有 [S25] 支撐。

**頸段食道癌以根治性化放療為主——指引原文**

- ESMO 2025 interim update（演算法註腳 c，鱗癌局部晚期）：「Evidence suggests that neoadjuvant CRT followed by surgery and definitive CRT is equally effective with regard to OS. Oesophageal surgery should be carried out in experienced (high-volume) centres only. For patients not willing to undergo oesophageal surgery or who are medically unfit for major surgery, definitive CRT should be preferred. **Even many experienced centres prefer definitive CRT for oesophageal tumours with a very proximal/cervical location.**」；註腳 b：「For patients unable or unwilling to undergo surgery, combined CRT is superior to RT alone.」[S15]
- 日本：頸段食道癌約佔 5%（中段胸部 47%、下段 28%、上段 12%、腹段 8%）[S30]。JES 對「頸段」沒有獨立 CQ 措辭（gap）。

**第一個月的流程——指引措辭**
- JES 總論：cStage II/III「the patient's tolerability to surgical intervention should first be confirmed through evaluation of the patient's general condition after accurate diagnosis of the clinical stage by upper gastrointestinal endoscopy, CT, and PET」[S30]。ESMO 2022 CPG 的分期建議條文抓不到（FAIL-1），本篇的檢查清單以統合分析＋JES 措辭支撐，不引 ESMO 分期條文。

### 反方向的資料
- EUS 對 N 分期的特異度只有 0.70，會有假陽性[S18]；化放療後 EUS 更不可靠[S29]。
- PET 對局部淋巴結敏感度低（33–57%）[S18][S22]；PET 找到「疑似同時性第二原發」約 9.3%，其中真正惡性只佔少數[S22 相關，來源 Malik 2012 未列入 PASS，不引數字]。
- 支氣管鏡巨觀異常 PPV 低，放療後尤其會誤判[S23][S24]。

### Claim ceiling
- **可寫**：「EUS 看深度與鄰近淋巴結最準（T4 敏感度九成以上），PET 抓遠端轉移最準（特異度 0.93–0.97）、可在 CT 乾淨的人裡再找出約 5% 的遠端轉移（Z0060），兩者互補」；「氣管分叉以上的腫瘤要做支氣管鏡＋切片，光看外觀不夠；約一到兩成原本以為可以開的人會因此改變路線（Riedel）」；「侵犯氣管／主動脈（T4b）是不切除的；化放療後若變成可切除，日本指引只給弱建議」；「頸段食道癌多數中心以根治性化放療為主（ESMO 原文）」。
- **不可寫**：「PET 陰性就沒有轉移」（敏感度 0.67–0.71）；「EUS 能判斷化放療後有沒有殘存」（Sun 2015；且 A4 的 preSANO 數據）；「檢查做完就知道能不能開」——體能（JES 的 tolerability）與病人意願是同一層的決定因素。
- T4 統合分析的兩組 OS 不可寫成「加手術把 5 年存活從 10% 提到 20%」——作者自己標注無高品質證據、族群不可比[S27]。

### Caveats
- 檢查的健保給付（PET、EUS）本組未查（非 A 組清單）；正文不寫給付。
- 一句話指向：化放療後的反應評估準確度 → A4；ESD 的深度判斷 → B4。

### 台灣端
- 無食道癌分期檢查的官方指引頁可引（gap）。重大傷病見 A1 台灣端[S73]。

### 給繪圖組的數字
- 三工具雷達圖：區域淋巴結敏感度／特異度 EUS 0.80/0.70、CT 0.50/0.83、PET 0.57/0.85；遠端轉移 PET 0.71/0.93、CT 0.52/0.91[S18]。
- 支氣管鏡改變路線比例：9.7%（1998）／18.1%（2001）[S23][S24]。

---

## A3 `ec-treatment-map`〈食道癌的治療地圖：你在哪一格〉

### Key facts

**台灣病人落在哪一格（癌登資料）**
- 期別分布（2008–2014，40–79 歲）：鱗癌 0/I/II/III/IV ＝ 0.9%／5.3%／16.5%／48.5%／28.8%；**第 III＋IV 期合計 77.3%**（全體 77.1%）[S5]。
- 實際接受的治療（癌登 2008–2016，cT1b-4 N0/+ M0 鱗癌 n=7,637）：**根治性化放療 4,122 人（54%）、nCRT＋手術 1,955 人（26%）、單純手術 1,560 人（20%）**；配對後 5 年 OS 分別 19.77%／31.23%／30.52%（p<0.001）[S33]。另一份（2008–2014，cT1-3N0-3 鱗癌 n=4,931）：dCRT 4,381 vs 手術＋輔助化放療 550；配對後 3 年 OS 23.8% vs 34.0%；**臨床第 I 期兩組無差異**，II/III 期手術組較佳[S34]。→ 台灣一半以上鱗癌病人走的是根治性化放療，這是地圖上人最多的一格。

**各格的指引措辭**

- **早期（cStage 0/I）**：JES CQ5：「There is weak evidence to recommend esophagectomy in patients with cStage I (T1bN0M0) thoracic esophageal cancer, and there is also weak evidence to recommend definitive chemoradiotherapy with adequate follow-up and salvage therapy in patients with cStage I who desire for esophageal preservation.」（共識 92.3%、C）；CQ6：pT1a-MM 脈管侵犯或 pT1b-SM 內視鏡切除後，追加食道切除或化放療皆有證據、無法擇一（89.3%、C）[S30]。→ ESD 細節指向 B4；JES 2022 第 2 部（內視鏡與其他）為 [S35]。
- **局部晚期可切除（cStage II/III）**：
  - JES CQ7：「There is weak evidence to recommend primarily surgery for patients with cStage II or III esophageal cancer.」（共識 100%、C）；CQ8：「there is strong evidence to recommend preoperative triplet chemotherapy with docetaxel + cisplatin + 5-FU」（84%、A）——**日本的標準是術前化療（DCF），不是術前化放療**；JCOG1109：3 年 OS DCF 72.1% vs CF 62.6%（HR 0.68）[S30]。JES 在 CQ7 說明裡也寫：「chemoradiotherapy is a valid treatment option for patients who wish for their esophagus to be preserved」、「both surgery and definitive chemoradiotherapy entail a significant risk of toxicity」[S30]。
  - ASCO 2020：「Multimodality therapy for patients with locally advanced esophageal carcinoma is recommended. For the subgroup of patients with adenocarcinoma, preoperative chemoradiotherapy or perioperative chemotherapy should be offered. **For the subgroup of patients with squamous cell carcinoma, preoperative chemoradiotherapy or chemoradiotherapy without surgery should be offered.**」[S32]
  - ESMO 2025 interim update：多模式治療 [I, A]；腺癌 FLOT [I, A]；鱗癌部分演算法註腳 c（原文見 A2）——nCRT＋手術與 dCRT「equally effective with regard to OS」；不願或不適合手術者「definitive CRT should be preferred」；註腳 f：救援手術「is optional in the case of incomplete response to CRT or local relapse and should only be carried out in selected patients and experienced centres」；註腳 g：術後 nivolumab 限「With residual vital tumour in the resection specimen」[S15]。ESMO 2022 CPG 本體（Ann Oncol 2022;33:992–1004）只能引書目[S31]。
- **不可切除局部晚期（cT4b／cStage IVA）**：JES CQ12 弱建議根治性化放療（100%、C）；CQ14 化放療後轉為可切除者手術為弱建議（89.3%、C）[S30]。
- **化放療後完全反應者**：JES CQ13：完全反應後追加化療只有弱證據（96.4%、C）[S30]。主動監測 → A4。
- **殘存／復發**：JES CQ11：「There is weak evidence to recommend salvage surgery for residual or recurrent lesions after chemoradiotherapy in patients with untreated resectable esophageal cancer.」（96.4%、C）；說明文：「it has a high perioperative mortality rate」[S30]。→ D4。
- **術後**：JES CQ9：術前化放療＋手術後未達 pCR 者，術後 nivolumab 強建議（81%、A），不分組織型態與 PD-L1[S30]。→ B2。
- **轉移**：→ B2／D4（ASCO 2023/2026 免疫指引書目歸 B2）。

**地圖各格的存活錨點（隨機試驗，鱗癌標籤）**
- 單純手術 → 加術前化放療：CROSS 10 年 OS 38% vs 25%[S37]；NEOCRTEC5010 5 年 OS 59.9% vs 49.1%[S41]。
- 化放療後加手術 vs 不加：FFCD 9102 2 年 OS 34% vs 40%[S43]；Stahl 2 年局部 PFS 64.3% vs 40.7% 但 OS 等效、治療死亡 12.8% vs 3.5%[S42]；Cochrane：OS HR 0.99[S44]。詳見 A4。

### 反方向的資料
- 台灣回溯資料偏向手術[S33][S34]，隨機試驗說 OS 等效[S42][S43][S44]——兩者要並陳，並解釋台灣資料裡 dCRT 組佔 54%，包含大量體能差、拒絕手術、腫瘤位置不利者（選擇偏差方向）。
- 日本（術前化療）與歐美（術前化放療）的標準不同[S30][S32][S15]——「地圖」要標注這是「同一格、不同國家不同主流」。

### Claim ceiling
- **可寫**：「台灣四分之三以上的食道鱗癌確診時已是第 III/IV 期」；「台灣一半以上的局部性鱗癌病人接受的是根治性化放療」；「局部晚期鱗癌有三條被指引承認的路：術前化放療＋手術、術前化療＋手術（日本）、根治性化放療（±救援手術）；ASCO 與 ESMO 把前者與後者並列」；「腺癌走 FLOT（ESMO [I, A]）」。
- **不可寫**：「根治性化放療是開不了刀的人的次等選擇」（ESMO／ASCO／JES 措辭皆非如此；紅線 1 反向）；「台灣資料證明手術比較好」（回溯、配對，且 dCRT 組佔一半以上）；任何用本院數字畫的地圖（SPEC 固定紅線）。
- 期別分布數字要標「2008–2014、40–79 歲、癌登＋健保資料庫」[S5]，不寫成「最新」。

### Caveats
- 地圖只畫一次（其他篇不重畫，SPEC §六）。每格一句話指向 B1–D4。
- NCCN 未引用（RESEARCH-COMMON 規定）。

### 台灣端
- 期別與治療分布：[S5][S33][S34]。重大傷病五年：[S73]。**gap**：癌登官方年報的期別分布表（hpa.gov.tw 抓不到）。

### 給繪圖組的數字（fig-ec-treatment-map）
- 期別 × 組織型態 → 路徑；台灣鱗癌三條路的實際人數比例 54／26／20%[S33]；各格指引強度標籤（JES 強／弱、ESMO I,A／I,C）[S30][S15]。

---

## A4 `ec-surgery-or-watch`〈化放療做完，還要不要開刀〉【全系列紅線 1】

### Key facts

**第一層：先化放療再開刀，比只開刀好（這是「開刀」建議的證據基礎）**

- **CROSS**（荷蘭，n=366；腺癌 75%、鱗癌 23%；cT1N1／T2-3N0-1；carboplatin/paclitaxel 週療 ×5 ＋ 41.4 Gy/23 fx）[S36]：R0 92% vs 69%；pCR 29%（47/161）；**院內死亡率兩組皆 4%**；中位 OS 49.4 vs 24.0 個月，HR 0.657（0.495–0.871）[S36]。長期（Shapiro 2015，中位追蹤 84 個月）：HR 0.68；**鱗癌中位 OS 81.6 vs 21.1 個月（HR 0.48，95% CI 0.28–0.83）**；腺癌 43.2 vs 27.1（HR 0.73）[S17]。十年（Eyck 2021，中位追蹤 147 個月）：HR 0.70（0.55–0.89）；**10 年 OS 38% vs 25%**；食道癌死亡 HR 0.60；孤立局部復發 HR 0.40、孤立遠端復發 HR 0.76（0.52–1.13，無差異）[S37]。pCR 依組織型態：**鱗癌 49%、腺癌 23%**（CROSS 全文數字，OA 轉述出處 preSINO protocol）[S61]。
- **NEOCRTEC5010**（中國 8 中心，胸段鱗癌 T1-4N1M0/T4N0M0，n=451；vinorelbine/cisplatin ＋ 40 Gy/20 fx）[S40]：**pCR 43.2%**；R0 98.4% vs 91.2%；中位 OS 100.1 vs 66.5 個月（HR 0.71，0.53–0.96）；治療期間死亡 2.2% vs 0.4%（p=0.212）；心律不整 13% vs 4%。長期（Yang 2021）：中位追蹤 53.5 個月，OS HR 0.74（0.57–0.97）；**5 年 OS 59.9% vs 49.1%**；5 年 DFS 63.6% vs 43.0%[S41]。
- **CMISG1701（修正 SPEC）**：nCRT＋MIE vs nCT＋MIE（中國鱗癌 cT3-4aN0-1M0，n=264）——3 年 OS 64.1% vs 54.9%，HR 0.82（0.58–1.18，p=0.28）無差異；pCR 27.7% vs 2.9%[S47]；術後併發症 47.4% vs 42.6%、**90 天死亡 3.5% vs 2.8%**、R0 97.3% vs 96.2%[S46]。設計文獻[S45]。→ 只能用來說「化放療比化療多出來的 pCR 沒轉成存活差」，不是「開不開刀」的證據。

**第二層：化放療後「加手術」vs「不加手術」——兩個老隨機試驗＋Cochrane**

- **Stahl 2005（德國，鱗癌局部晚期，n=172，誘導化療→40 Gy 化放療→手術 vs 誘導化療→≥65 Gy 化放療）**：OS 等效（log-rank 等效檢定 p<0.05）；**2 年局部 PFS 手術組 64.3% vs 40.7%（HR 2.1，1.3–3.5）**；**治療相關死亡 12.8% vs 3.5%（p=0.03）**；對誘導化療的反應是唯一獨立預後因子（HR 0.30）[S42]。
- **FFCD 9102（法國，T3N0-1M0 胸段，88.8% 鱗癌；化放療有反應者 n=259 隨機：手術 vs 繼續化放療）**：2 年 OS 34% vs 40%（HR 0.90，adjusted p=0.44）；中位 OS 17.7 vs 19.3 個月；2 年局部控制 66.4% vs 57.0%；支架需求 5% vs 32%（p<0.001）；**3 個月死亡率 9.3% vs 0.8%（p=0.002）**；累積住院 68 vs 52 天[S43]。**注意：只有「對化放療有反應者」被隨機**，這是它與主動監測概念相通、也是它不能外推到無反應者的原因。
- **Cochrane 2017（Vellayappan，兩試驗 n=431，93% 鱗癌，≥T3 或 N+）**：加手術對 OS「little or no difference」（**HR 0.99，0.79–1.24**，高品質證據）；免於局部復發改善（HR 0.55，0.39–0.76，中品質）；**治療相關死亡風險 RR 5.11（1.74–15.02，低品質）**；短期 QoL 較差、吞嚥困難的救援處置較少（HR 0.52）[S44]。

**第三層：反應評估有多不準（紅線 1 的核心）**

- **preSANO**（荷蘭 6 中心，n=207，CROSS 方案後，第一次評估 4–6 週、第二次 12–14 週，之後手術）：**一般切片＋FNA 漏掉 31%（8/26）的 TRG3-4**；**bite-on-bite 切片＋FNA 漏掉 10%（4/41）**；EUS 最大厚度漏掉 28%（11/39）；PET-CT 漏掉 15%（6/41）；PET-CT 另找到 9%（18/190）間隔遠端轉移[S38]。漏掉的殘存在哪裡（van der Wilk 2020）：切片陰性但切除標本有殘存者 27/49，其中 18 在黏膜、8 在無腫瘤黏膜下的黏膜下層、1 在肌層[S39]。
- **preSINO**（中國／香港／台灣鱗癌，n=309，同樣兩次評估）：bite-on-bite＋EUS-FNA 對 TRG3-4 或 ypN+ 的**假陰性率 13.5%（18/133）**；偵測任何殘存的敏感度 81.7%、特異度 93.2%、**NPV 68.7%**、PPV 96.5%；PET-CT 術前找到 4.9% 遠端轉移；ctDNA 陽性者 12 個月內全身復發 28.0% vs 陰性 5.3%[S62]。**參與中心含台灣（林口長庚 Chao YK）**[S61][S62]。
- **SANO 標準手術組的「臨床完全反應」有多少是真的完全反應**：101 位開刀者中 pT0 只有 36 位（35.6%），38 位有 T2/T3 殘存（出自批評 SANO 的編輯評論，引 SANO 附錄表 S6）[S53]。SANO 作者回應：preSANO 的 90% 是「>10% 殘存被偵測到」的比例，SANO 本身沒有報告 CRE 的真陽性率，「the results of the accuracy of CREs in the present phase III study inevitably cannot be compared with the preSANO-trial」[S54]。

**第四層：主動監測的隨機試驗——SANO（結果已出）**

- 設計（Noordman 2018 BMC Cancer）：phase III 階梯楔形群集隨機，12 家荷蘭醫院，目標 300 位 cCR，非劣性邊界 15%；CRE-I（4–6 週：內視鏡 bite-on-bite 切片）、CRE-II（再 6–8 週：PET-CT＋內視鏡切片＋EUS-FNA）；監測組在 6/9/12/16/20/24/30/36/48/60 個月重複 CRE-II；只在「高度懷疑或證實局部再生長且無遠端轉移」時開刀；次要終點含不手術比例、cT4b 不可切除率、R0、遠端轉移率[S48]。
- 結果（van der Wilk 2025 Lancet Oncol 26:425–436）：篩選 1,115 人、納入 309 位 cCR（主動監測 198、標準手術 111）；男性 78%；中位追蹤 38 個月（IQR 32–48）；**2 年 OS 74%（69–78）vs 71%（62–78），非劣性成立（單尾 95% 界限低 7%）**；ITT 亦成立；OS 無顯著差異（mITT HR 1.14，95% CI 0.74–1.78；ITT HR 0.83，0.53–1.31）；標準手術與延後手術的併發症與術後死亡率相似；結論：「For the long-term efficacy of active surveillance, extended follow-up is required.」[S49]
- 結果的細部（OA 來源）：中位 OS **43 vs 53 個月**（HR 1.14，p=0.55）；監測組 **48% 局部再生長、17% 遠端轉移、35% 持續 cCR**；腺癌為多數，腺癌 30% 持續 cCR；延後手術的併發症、死亡率、R0 與標準手術相當；標準手術組約四分之一病人拒絕手術改選監測[S52]。SANO 作者 2026 年的回應：**46% 的 cCR 病人最終沒有接受食道切除**（持續 cCR 或早期發現遠端轉移）；遠端轉移率「a non-significant difference … in favor of standard surgery」；「we cannot rule out a possible statistically or clinically relevant difference in distant dissemination after longer follow-up. This may then result in a worse overall survival for patients undergoing active surveillance」；「treatment effects observed in clinical trials often are less favorable in patients outside clinical trials」[S54]。
- 更長追蹤（Gangaram Panday 2026 Ann Surg Oncol，SANO 資料）：750 位接受 nCRT 者中 **37%（274）在 12 週達 cCR**；監測組 198 人中，**中位追蹤 54 個月時只有 25% 維持 cCR**；cN2-3 者較難達 cCR（OR 0.57）也較難維持（HR 2.08）；「Standard clinical parameters poorly predict clinical response after nCRT」[S51]。
- 生活品質（BJS 2025，n=274）：6 個月時監測組吞嚥困難、呼吸困難、疲倦、身體功能顯著較好；**吞嚥困難的優勢維持到 24 個月**；其他面向無差異[S50]。
- 批評方（Housman 2025 JTCVS Open，OA 編輯評論，立場反對主動監測——引用時要標明）：族群鱗癌 24%（監測）vs 21%（手術）；中位追蹤 34 vs 50 個月；**遠端轉移 43% vs 34%**；標準手術組 30 天死亡 3%、90 天 5%（延後手術 1%／4%）、吻合口滲漏 27%；手術時點在化放療後 12 週之後（中位 15 週）；結論主張「esophagectomy should not be abandoned in healthy candidates」[S53]。
- 決策模型（Bondzi-Simpson 2026 JAMA Surg，以 SANO 資料建 Markov 模型，基準 60 歲男性 cT3N1M0 cCR）：**5 年時手術 QALY 1.74 vs 1.34、生命年 3.11 vs 2.41**；2 年時監測略優（約 15 天）；復發機率 <43%、局部可切除復發比例 >94%、或手術 QoL 衝擊很大時，模型轉向監測；結論「esophagectomy remains the preferred strategy for maximizing long-term survival and QALYs」[S55]。
- 後續：SANO-2（前瞻世代，監測 SANO 以外族群的安全性，NCT04886635 RECRUITING，估 360 人）[S59]；SANO-3（cCR 後 nivolumab 維持，NCT05491616 ACTIVE_NOT_RECRUITING，n=77，估 2026-10 完成）[S60]。

**第五層：還沒有結果的、與已經失敗的**

- **NEEDS**（瑞典 Karolinska 主導，多國）：nCRT＋預定手術 vs dCRT＋監測＋必要時救援手術，**限鱗癌**；非劣性邊界 7.5%（CROSS 鱗癌 5 年 OS 60% → 52.5%），protocol 目標 1,200 人／462 事件，HR 對應 1.26；主要次要終點為一年時整體 HRQOL[S56]。ClinicalTrials.gov：RECRUITING，估 1,020 人，開始 2020-11-27，主要完成日估 2026-12-31，完成估 2031-12-31[S57]。
- **ESOSTRATE**（法國 Dijon，NCT02551458，cCR 後系統性手術 vs 監測＋救援）：**TERMINATED**，原因「sub-optimal inclusion rate, additional 9 years to finalize inclusion and follow-up of all patients」，實收 188 人，2016-03 開始、2023-03 主要完成[S58]。查無結果發表。
- **SINO**（中國鱗癌的隨機試驗）：preSINO 已完成並發表[S62]，SINO 本體在 ClinicalTrials.gov 查無登錄（2026-09-02 查詢）。
- **JCOG0909（日本，單臂確認性試驗）**：cStage II/III 鱗癌，cisplatin/5-FU＋50.4 Gy、良好反應者加化療、殘存或復發者救援 ER 或手術；n=94，**CR 59%**；救援 ER 5%、救援手術 27%（R0 76%）；救援手術 G3-4 早期併發症 20%；晚期 G3 毒性 9.6%；**3 年 OS 74.2%（90% CI 65.9–80.8）**[S63]。JES 引最終分析：5 年 OS 64.5%、5 年 RFS 48.3%、**5 年食道保留率 54.9%**（95% CI 44.3–64.4）、1 例手術相關死亡；JES 結論「definitive chemoradiotherapy at the dose of 50.4 Gy is one of the valid treatment options for patients with cStage II or III esophageal cancer who do not wish to undergo surgery as the primary treatment」[S30]。
- 非隨機的「病人自選」世代（愛爾蘭單中心 1998–2019，cCR 80 人，51 選手術、29 選監測；監測組平均年齡 70 vs 59）：年齡校正中位存活 28.1 vs 52.0 個月，p=0.485；監測組 24.1% 局部復發接受救援[S72]——回溯、小樣本、年齡差 11 歲，只能當「有人在做」的紀錄。

**第六層：手術死亡率與救援手術的代價（紅線 1 反向的硬數字）**

- 國際登錄：ECCG／Esodata 2015–2016（24 中心、2,704 例）：任何併發症 59%、吻合口滲漏 11.4%、Clavien-Dindo ≥IIIb 17.2%、**30 天死亡 2.4%、90 天死亡 4.5%**[S68]；2015–2018（39 中心、6,022 例）：**30 天 2.0%、90 天 4.5%**，微創 52.8%，滲漏率 11.7%→13.1%[S69]。
- 日本 NCD 2011（713 院、5,354 例）：併發症 41.9%、**30 天死亡 1.2%、手術死亡 3.4%**；術前需 ADL 協助（OR 4.2）、一年內吸菸（OR 2.6）、六個月內體重減輕 >10%（OR 2.4）是 30 天死亡的危險因子[S70]。
- 荷蘭 DUCA 2011–2018（6,172 例食道切除）：院內／30 天死亡由 4.2% 降至 2.5%；年中位院量 38→53[S71]。
- 隨機試驗內：CROSS 院內死亡 4%[S36]；NEOCRTEC5010 治療期間死亡 2.2%[S40]；ESOPEC CROSS 臂 90 天 5.6%[S14]；CMISG1701 90 天 3.5%[S46]；Stahl 手術臂治療死亡 12.8%[S42]；FFCD 9102 手術臂 3 個月死亡 9.3%[S43]。
- 救援食道切除：Markar 2014 統合（8 篇、n=954）：救援 vs 計畫性手術——**術後死亡 9.50% vs 4.07%（POR 3.02）**、滲漏 23.97% vs 14.47%、肺部併發症 29.75% vs 16.99%、住院多 8.29 天[S65]。Markar 2015（30 個歐洲中心 2000–2010，救援 308 vs 計畫性 540）：**院內死亡 8.4% vs 9.3%（相似）**，滲漏 17.2% vs 10.7%；配對後 3 年 OS 43.3% vs 40.1%；**持續性殘存（persistent）比復發（recurrent）預後差：3 年 OS 40.9% vs 56.2%**[S64]。Kumagai 2016（鱗癌 dCRT 後，4 篇 n=219）：救援手術 vs 二線化放療 OS HR 0.42；救援手術治療相關死亡 10.3%[S66]。T4 鱗癌救援（Sakai 2026 統合，8 篇 208 例）：死亡率 7%、滲漏 18%、R0 72%[S67]。JES CQ11 措辭見 A3[S30]。

**第七層：指引怎麼說**
- ESMO 2025 interim update 註腳 c／f 原文（見 A2／A3）[S15]；ASCO 2020：鱗癌「preoperative chemoradiotherapy or chemoradiotherapy without surgery should be offered」[S32]；JES CQ7 弱建議以手術為主、CQ11 救援手術弱建議、CQ13 CR 後追加化療弱建議[S30]。**沒有任何指引把「cCR 後主動監測」寫成標準選項**（ESMO 2025 interim update 全文未提 SANO／active surveillance；JES 2022 亦無）[S15][S30]。

### 反方向的資料（誠實必列，兩個方向）
- 反「一律開刀」：FFCD 9102／Stahl／Cochrane——化放療有反應者加手術**不增加 OS**、治療死亡風險 5 倍[S42][S43][S44]；JCOG0909 5 年 OS 64.5%、保留食道 54.9%[S30][S63]；SANO 2 年非劣[S49]；HRQoL 優勢[S50]；食道切除 90 天死亡 4.5%[S68][S69]。
- 反「反應好就不開」：cCR 的 pT0 只有 36%[S53]；preSINO NPV 68.7%[S62]；SANO 監測組 48% 局部再生長、17% 遠端轉移、54 個月時只剩 25% 維持 cCR[S51][S52]；遠端轉移方向不利、作者承認長期可能反映在 OS[S54]；5 年 Markov 模型偏向手術[S55]；SANO 族群腺癌為主、追蹤 38 個月[S49][S53]；持續性殘存的救援預後比復發差[S64]；台灣回溯資料 dCRT 5 年 OS 19.8% vs nCRT＋手術 31.2%[S33]。

### Claim ceiling（逐試驗，硬上限）
- **CROSS／NEOCRTEC5010 證明了**：先化放療再開刀比只開刀活得久（鱗癌尤其明顯）。**沒證明**：化放療後開刀比不開刀好（沒有這一臂）。
- **FFCD 9102／Stahl／Cochrane 證明了**：對化放療「有反應」的局部晚期鱗癌，加手術不增加整體存活、改善局部控制、增加治療死亡。**沒證明**：用當代影像／切片可以準確選出誰有反應（兩試驗用的是 2000 年前的評估）；也不涵蓋無反應者。
- **preSANO／preSINO 證明了**：用 bite-on-bite 切片＋EUS-FNA＋PET-CT 可把 >10% 殘存的漏診率壓到約一成（鱗癌 13.5%）。**沒證明**：能排除少量殘存（NPV 68.7%；SANO 手術組 cCR 者 64% 有殘存）。
- **SANO 證明了**：荷蘭、腺癌為主、嚴格兩次評估後判定 cCR 的病人，在**兩年**時主動監測的整體存活不劣於立即手術（邊界 15%），且短期生活品質較好、延後手術的手術風險沒有升高。**沒證明**：五年存活不劣；鱗癌次族群的結果（鱗癌僅約兩成）；遠端轉移不增加（方向偏不利，作者自承）；在試驗嚴格追蹤以外的環境能安全複製（作者自承，SANO-2 正在查）。
- **NEEDS／ESOSTRATE**：NEEDS 還在收案，2026-12 之後才可能有主要結果；ESOSTRATE 已因收案不足終止。**任何把 NEEDS 寫成「已證明」或「快出來了」的句子都超線。**
- **JCOG0909 證明了**：日本鱗癌 cStage II/III 以 50.4 Gy 化放療＋積極救援，可達 3 年 OS 74%、5 年 64.5%、半數以上保留食道（單臂，無對照）。**沒證明**：優於或等於 nCRT＋手術。
- **CMISG1701**：只證明 nCRT 比 nCT 的 pCR 高而 OS 沒差；**與「開不開刀」無關**。
- **可寫的句子**：「化放療後影像和切片都乾淨，仍有大約三分之二的人食道裡還有癌細胞（SANO 手術組）」；「主動監測目前只在一個荷蘭試驗裡成立，追蹤三年多、七成五是腺癌、遠端轉移的方向不利，長期結果還沒有出來」；「這也是為什麼院內在鱗癌化放療後仍建議開刀」；反向：「根治性化放療是有隨機試驗支撐的正當路——對化放療有反應的鱗癌，加手術沒有多活，但多了手術死亡」；「頸段、體能不適合、明確拒絕手術，根治性化放療是指引的首選（ESMO 原文）」。
- **不可寫的句子**：「反應好就可以不開」「現在可以選擇不開刀」「監測和手術一樣安全」（紅線 1 正向）；「不開刀等於放棄治療」「根治性化放療只是給開不了刀的人」（紅線 1 反向）；把 SANO 2 年非劣寫成「存活一樣」；把 Housman 編輯評論的立場句當成事實陳述（要標「批評者認為」）；把 JAMA Surg 模型寫成「試驗證明五年手術較好」（是模型）；把台灣回溯資料寫成「台灣證明手術較好」。

### Caveats／safety notes
- 利益揭露段落（SPEC §二）放本篇第一個 h4 之前，逐字。
- 每個數字帶標籤：鱗癌／腺癌、期別、試驗名、n、追蹤年限。
- 「院內建議」與「國際方向」並排寫，不寫本院療效數字。
- 病人若要問第二意見，給的清單是：SANO 主論文[S49]、Cochrane[S44]、preSANO[S38]、preSINO[S62]、JES CQ7/CQ11[S30]。

### 台灣端
- 台灣鱗癌 nCRT＋手術 vs dCRT：癌登回溯[S33][S34]（見 A3）；**台灣沒有 cCR 後主動監測的試驗或世代研究可引（gap）**；台灣中心（林口長庚）參與 preSINO[S61][S62]。
- 重大傷病[S73]；戒菸／戒檳／戒酒資源[S74][S75][S76]。手術與化放療的健保給付非本組清單，不寫。

### 給繪圖組的數字（fig-ec-three-roads）
- 三條路時間軸：三合一（CROSS：5 週化放療→6–8 週手術；10 年 OS 38%）[S36][S37]；根治性化放療（JCOG0909：50.4 Gy；5 年 OS 64.5%、食道保留 54.9%）[S30][S63]；主動監測（SANO：4–6 週與 12 週兩次評估→cCR 37%→監測；2 年 OS 74%；54 個月維持 cCR 25%；標「試驗中／長期未出」，NEEDS 收案中、ESOSTRATE 終止）[S49][S51][S57][S58]。
- 漏診階梯：一般切片 31% → bite-on-bite＋FNA 10%（鱗癌 13.5%）→ cCR 者 pT0 僅 36%[S38][S62][S53]。
- 手術死亡率尺：計畫性食道切除 90 天 4.5%（Esodata）→ 救援 9.5%（Markar 2014 統合）[S69][S65]。

---

## 來源清單（PASS／FAIL 逐條）

### A1 主用

- **[S1] PASS** 衛生福利部統計處。〈113年死因統計結果－分析〉（PDF，5 頁；含表 4、表 5 歷年主要癌症死亡原因）。發布頁：https://www.mohw.gov.tw/cp-7177-82775-1.html（建檔 114-06-16）；PDF：https://www.mohw.gov.tw/dl-95385-03c74965-e98f-482a-a39f-2a422e38ba13.html。Route: curl 抓取發布頁（200）→ 下載 PDF → pdfplumber 抽字；食道癌 113 年死亡 2,076、每十萬 8.9、標準化 4.7；男性 1,926；死亡年齡中位數 63。
- **[S2] PASS** 衛生福利部（國民健康署）。〈公布111年國人癌症登記資料分析結果 五癌篩檢為健康加值〉新聞稿。https://www.mohw.gov.tw/cp-2704-80902-1.html。Route: curl（200）；抓到「男性…食道癌」第 6 位、「食道癌、口腔癌標準化發生率男性分別為女性的 12.5 倍、9.9 倍」、檳榔 5 倍／三者 10.5 倍。
- **[S3] PASS** 衛生福利部。〈公布112年國人癌症登記資料分析結果 守護健康未來 從癌症篩檢開始〉。https://www.mohw.gov.tw/cp-7171-84987-1.html。Route: curl（200）；112 年新發癌症 138,051 人；男性食道癌第 6 位。
- **[S4] PASS** 衛生福利部（國民健康署）。〈預防食道癌 危險物不入口 有異狀速就醫〉新聞稿，建檔 110-11-16。https://www.mohw.gov.tw/cp-5022-64040-1.html。Route: curl（200）；107 年 2,778 人罹患、109 年 1,954 人死亡；9 成以上男性；50–70 歲；WHO >65°C；致癌因子清單。
- **[S5] PASS** Chen HY, Chen IC, Chen YH, Chen CC, Chuang CY, Lin CH. The Influence of Socioeconomic Status on Esophageal Cancer in Taiwan: A Population-Based Study. *J Pers Med*. 2022;12(4):595. DOI 10.3390/jpm12040595. PMID 35455711. PMC9027796. OA:Y. Route: Europe PMC search + fullTextXML（Table 3 期別分布）。
- **[S6] PASS** Tsai MC, Chou YC, Lee YK, et al. Secular Trends in Incidence of Esophageal Cancer in Taiwan from 1985 to 2019: An Age-Period-Cohort Analysis. *Cancers (Basel)*. 2022;14(23):5844. DOI 10.3390/cancers14235844. PMID 36497327. PMC9741308. OA:Y. Route: Europe PMC 摘要。
- **[S7] PASS** Lee CH, Lee JM, Wu DC, et al. Independent and combined effects of alcohol intake, tobacco smoking and betel quid chewing on the risk of esophageal cancer in Taiwan. *Int J Cancer*. 2005;113(3):475–482. DOI 10.1002/ijc.20619. PMID 15455377. OA:N. Route: Europe PMC 摘要。
- **[S8] PASS** Wu IC, Lu CY, Kuo FC, et al. Interaction between cigarette, alcohol and betel nut use on esophageal cancer risk in Taiwan. *Eur J Clin Invest*. 2006;36(4):236–241. DOI 10.1111/j.1365-2362.2006.01621.x. PMID 16620285. OA:N. Route: Europe PMC 摘要。
- **[S9] PASS** Lee CH, Lee JM, Wu DC, et al. Carcinogenetic impact of ADH1B and ALDH2 genes on squamous cell carcinoma risk of the esophagus with regard to the consumption of alcohol, tobacco and betel quid. *Int J Cancer*. 2008;122(6):1347–1356. DOI 10.1002/ijc.23264. PMID 18033686. OA:N. Route: Europe PMC 摘要。
- **[S10] PASS** Brooks PJ, Enoch MA, Goldman D, Li TK, Yokoyama A. The alcohol flushing response: an unrecognized risk factor for esophageal cancer from alcohol consumption. *PLoS Med*. 2009;6(3):e50. DOI 10.1371/journal.pmed.1000050. PMID 19320537. PMC2659709. OA:Y. Route: fullTextXML（36% 東亞人；ALDH2 半顯性）。
- **[S11] PASS（僅書目）** Loomis D, Guyton KZ, Grosse Y, et al.; IARC Monograph Working Group. Carcinogenicity of drinking coffee, mate, and very hot beverages. *Lancet Oncol*. 2016;17(7):877–878. DOI 10.1016/S1470-2045(16)30239-X. PMID 27318851. OA:N. Route: Europe PMC（無摘要文字）；「>65°C、2A」的措辭以 [S4] 官方轉述為文字依據。
- **[S12] PASS** Lagergren J, Bergström R, Lindgren A, Nyrén O. Symptomatic gastroesophageal reflux as a risk factor for esophageal adenocarcinoma. *N Engl J Med*. 1999;340(11):825–831. DOI 10.1056/NEJM199903183401101. PMID 10080844. OA:N. Route: Europe PMC 摘要。
- **[S13] PASS** Arnold M, Ferlay J, van Berge Henegouwen MI, Soerjomataram I. Global burden of oesophageal and gastric cancer by histology and subsite in 2018. *Gut*. 2020;69(9):1564–1571. DOI 10.1136/gutjnl-2020-321600. PMID 32606208. OA:N. Route: Europe PMC 摘要。
- **[S14] PASS** Hoeppner J, Brunner T, Schmoor C, et al. Perioperative Chemotherapy or Preoperative Chemoradiotherapy in Esophageal Cancer (ESOPEC). *N Engl J Med*. 2025;392(4):323–335. DOI 10.1056/NEJMoa2409408. PMID 39842010. OA:N. Route: Europe PMC 摘要。
- **[S15] PASS** Obermannová RL, Leong T; ESMO Guidelines Committee. ESMO Clinical Practice Guideline interim update on the treatment of locally advanced oesophageal and oesophagogastric junction adenocarcinoma and metastatic squamous-cell carcinoma. *ESMO Open*. 2025;10(2):104134. DOI 10.1016/j.esmoop.2025.104134. PMID 39986705. PMC11889489. OA:Y（CC BY-NC-ND）. Route: fullTextXML 全文（建議條文、Figure 1 註腳 b/c/d/f/g、ESOPEC 與 Neo-AEGIS 段落）。ESMO 官方指引頁 https://www.esmo.org/guidelines/esmo-clinical-practice-guideline-oesophageal-cancer（curl 200，內容需 JS 載入）。
- **[S16] PASS** Reynolds JV, Preston SR, O'Neill B, et al. Trimodality therapy versus perioperative chemotherapy in the management of locally advanced adenocarcinoma of the oesophagus and oesophagogastric junction (Neo-AEGIS): an open-label, randomised, phase 3 trial. *Lancet Gastroenterol Hepatol*. 2023;8(11):1015–1027. DOI 10.1016/S2468-1253(23)00243-1. PMID 37734399. PMC10567579. OA:Y. Route: fullTextXML（Findings）。
- **[S17] PASS** Shapiro J, van Lanschot JJB, Hulshof MCCM, et al.; CROSS study group. Neoadjuvant chemoradiotherapy plus surgery versus surgery alone for oesophageal or junctional cancer (CROSS): long-term results of a randomised controlled trial. *Lancet Oncol*. 2015;16(9):1090–1098. DOI 10.1016/S1470-2045(15)00040-6. PMID 26254683. OA:N. Route: Europe PMC 摘要（鱗癌／腺癌次族群 HR）。

### A2 主用

- **[S18] PASS** van Vliet EP, Heijenbrok-Kal MH, Hunink MG, Kuipers EJ, Siersema PD. Staging investigations for oesophageal cancer: a meta-analysis. *Br J Cancer*. 2008;98(3):547–557. DOI 10.1038/sj.bjc.6604200. PMID 18212745. PMC2243147. OA:Y. Route: Europe PMC 摘要。
- **[S19] PASS** Puli SR, Reddy JB, Bechtold ML, Antillon D, Ibdah JA, Antillon MR. Staging accuracy of esophageal cancer by endoscopic ultrasound: a meta-analysis and systematic review. *World J Gastroenterol*. 2008;14(10):1479–1490. DOI 10.3748/wjg.14.1479. PMID 18330935. PMC2693739. Route: Europe PMC 摘要。
- **[S20] PASS** van Westreenen HL, Westerterp M, Bossuyt PM, et al. Systematic review of the staging performance of 18F-fluorodeoxyglucose positron emission tomography in esophageal cancer. *J Clin Oncol*. 2004;22(18):3805–3812. DOI 10.1200/JCO.2004.01.083. PMID 15365078. OA:N. Route: Europe PMC 摘要。
- **[S21] PASS** Meyers BF, Downey RJ, Decker PA, et al.; ACOSOG Z0060. The utility of positron emission tomography in staging of potentially operable carcinoma of the thoracic esophagus: results of the American College of Surgeons Oncology Group Z0060 trial. *J Thorac Cardiovasc Surg*. 2007;133(3):738–745. DOI 10.1016/j.jtcvs.2006.09.079. PMID 17320575. OA:N. Route: Europe PMC 摘要。
- **[S22] PASS** Flamen P, Lerut A, Van Cutsem E, et al. Utility of positron emission tomography for the staging of patients with potentially operable esophageal carcinoma. *J Clin Oncol*. 2000;18(18):3202–3210. DOI 10.1200/JCO.2000.18.18.3202. PMID 10986052. OA:N. Route: Europe PMC 摘要。
- **[S23] PASS** Riedel M, Stein HJ, Mounyam L, Lembeck R, Siewert JR. Extensive sampling improves preoperative bronchoscopic assessment of airway invasion by supracarinal esophageal cancer: a prospective study in 166 patients. *Chest*. 2001;119(6):1652–1660. DOI 10.1378/chest.119.6.1652. PMID 11399687. OA:N. Route: Europe PMC 摘要。
  - **[S23b] PASS** Nishimura Y, Osugi H, Inoue K, Takada N, Takamura M, Kinosita H. Bronchoscopic ultrasonography in the diagnosis of tracheobronchial invasion of esophageal cancer. *J Ultrasound Med*. 2002;21(1):49–58. DOI 10.7863/jum.2002.21.1.49. PMID 11794402. OA:N. Route: Europe PMC 摘要。
- **[S24] PASS** Riedel M, Hauck RW, Stein HJ, et al. Preoperative bronchoscopic assessment of airway invasion by esophageal cancer: a prospective study. *Chest*. 1998;113(3):687–695. DOI 10.1378/chest.113.3.687. PMID 9515844. OA:N. Route: Europe PMC 摘要。
- **[S25] PASS** Rice TW, Gress DM, Patil DT, Hofstetter WL, Kelsen DP, Blackstone EH. Cancer of the esophagus and esophagogastric junction—Major changes in the American Joint Committee on Cancer eighth edition cancer staging manual. *CA Cancer J Clin*. 2017;67(4):304–317. DOI 10.3322/caac.21399. PMID 28556024. OA:N. Route: Europe PMC 摘要。
- **[S26] PASS** Rice TW, Ishwaran H, Ferguson MK, Blackstone EH, Goldstraw P. Cancer of the Esophagus and Esophagogastric Junction: An Eighth Edition Staging Primer. *J Thorac Oncol*. 2017;12(1):36–42. DOI 10.1016/j.jtho.2016.10.016. PMID 27810391. PMC5591443. Route: Europe PMC 摘要。
- **[S27] PASS** Lee CC, Soon YY, Vellayappan B, Ho F, Tey JCS. Survival rates and safety associated with chemoradiotherapy followed by surgery and chemoradiotherapy alone for patients with T4 esophageal cancer: a systematic review and meta-analysis. *Acta Oncol*. 2022;61(6):738–748. DOI 10.1080/0284186X.2022.2062680. PMID 35450511. OA:N. Route: Europe PMC 摘要。
- **[S28] PASS** Hulshoff JB, Mul VEM, de Boer HEM, et al. Impact of Endoscopic Ultrasonography on 18F-FDG-PET/CT Upfront Towards Patient Specific Esophageal Cancer Treatment. *Ann Surg Oncol*. 2017;24(7):1828–1834. DOI 10.1245/s10434-017-5835-1. PMID 28303427. PMC5486848. OA:Y. Route: Europe PMC 摘要。
- **[S29] PASS** Sun F, Chen T, Han J, Ye P, Hu J. Staging accuracy of endoscopic ultrasound for esophageal cancer after neoadjuvant chemotherapy: a meta-analysis and systematic review. *Dis Esophagus*. 2015;28(8):757–771. DOI 10.1111/dote.12274. PMID 25168285. OA:N. Route: Europe PMC 摘要。
- **[S30] PASS** Kitagawa Y, Ishihara R, Ishikawa H, et al. Esophageal cancer practice guidelines 2022 edited by the Japan Esophageal Society: part 1. *Esophagus*. 2023;20(3):343–372. DOI 10.1007/s10388-023-00993-2. PMID 36933136. PMC10024303. OA:Y. Route: fullTextXML 全文（CQ5–CQ14 建議陳述與說明；JCOG0909 最終分析數字；部位與組織型態分布）。
- （A2 亦用 [S15] ESMO 註腳、[S38] preSANO、[S61][S62] preSINO）

### A3 主用

- **[S31] PASS（書目＋官方頁）** Obermannová R, Alsina M, Cervantes A, et al.; ESMO Guidelines Committee. Oesophageal cancer: ESMO Clinical Practice Guideline for diagnosis, treatment and follow-up. *Ann Oncol*. 2022;33(10):992–1004. DOI 10.1016/j.annonc.2022.07.003. PMID 35914638. OA:N. Route: Europe PMC 書目（無摘要）；ESMO 官方頁 curl 200。**內文措辭不可引**（見 FAIL-1）；措辭以 [S15] 的 2025 interim update 為據。
- **[S32] PASS** Shah MA, Kennedy EB, Catenacci DV, et al. Treatment of Locally Advanced Esophageal Carcinoma: ASCO Guideline. *J Clin Oncol*. 2020;38(23):2677–2694. DOI 10.1200/JCO.20.00866. PMID 32568633. OA:N. Route: Europe PMC 摘要（Recommendations 段）。
- **[S33] PASS** Chen HS, Lin CH, Wu SC, Wang BY. Survival Comparison Among Neoadjuvant Chemoradiotherapy Followed by Esophagectomy, Definitive Chemoradiotherapy, and Esophagectomy Alone for Esophageal Squamous Cell Carcinoma. *Ann Surg Oncol*. 2022;29(6):3617–3627. DOI 10.1245/s10434-021-11210-8. PMID 34994899. OA:N. Route: Europe PMC 摘要。
- **[S34] PASS** Chang YL, Cheng YF, Chen HS, et al. Propensity score analysis comparing survival between definitive chemoradiotherapy and esophagectomy with adjuvant chemoradiotherapy in patients with esophageal squamous cell carcinoma. *PLoS One*. 2022;17(10):e0271338. DOI 10.1371/journal.pone.0271338. PMID 36227954. PMC9560125. OA:Y. Route: Europe PMC 摘要。
- **[S35] PASS（書目，供 B4 交叉）** Kitagawa Y, et al. Esophageal cancer practice guidelines 2022 edited by the Japan Esophageal Society: part 2. *Esophagus*. 2023;20(3):373–389. DOI 10.1007/s10388-023-00994-1. PMID 36995449. PMC10235142. OA:Y. Route: Europe PMC + fullTextXML 可取得。

### A4 主用

- **[S36] PASS** van Hagen P, Hulshof MC, van Lanschot JJ, et al.; CROSS Group. Preoperative chemoradiotherapy for esophageal or junctional cancer. *N Engl J Med*. 2012;366(22):2074–2084. DOI 10.1056/NEJMoa1112088. PMID 22646630. OA:N. Route: Europe PMC 摘要。
- **[S37] PASS** Eyck BM, van Lanschot JJB, Hulshof MCCM, et al. Ten-Year Outcome of Neoadjuvant Chemoradiotherapy Plus Surgery for Esophageal Cancer: The Randomized Controlled CROSS Trial. *J Clin Oncol*. 2021;39(18):1995–2004. DOI 10.1200/JCO.20.03614. PMID 33891478. OA:N. Route: Europe PMC 摘要。
- **[S38] PASS** Noordman BJ, Spaander MCW, Valkema R, et al.; SANO study group. Detection of residual disease after neoadjuvant chemoradiotherapy for oesophageal cancer (preSANO): a prospective multicentre, diagnostic cohort study. *Lancet Oncol*. 2018;19(7):965–974. DOI 10.1016/S1470-2045(18)30201-8. PMID 29861116. OA:N. Route: Europe PMC 完整摘要（四種工具漏診率、9% 間隔轉移）。
- **[S39] PASS** van der Wilk BJ, Eyck BM, Doukas M, et al. Residual disease after neoadjuvant chemoradiotherapy for oesophageal cancer: locations undetected by endoscopic biopsies in the preSANO trial. *Br J Surg*. 2020;107(13):1791–1800. DOI 10.1002/bjs.11760. PMID 32757307. PMC7689829. OA:Y. Route: Europe PMC 摘要。
- **[S40] PASS** Yang H, Liu H, Chen Y, et al. Neoadjuvant Chemoradiotherapy Followed by Surgery Versus Surgery Alone for Locally Advanced Squamous Cell Carcinoma of the Esophagus (NEOCRTEC5010): A Phase III Multicenter, Randomized, Open-Label Clinical Trial. *J Clin Oncol*. 2018;36(27):2796–2803. DOI 10.1200/JCO.2018.79.1483. PMID 30089078. PMC6145832. OA:Y. Route: Europe PMC 摘要。
- **[S41] PASS** Yang H, Liu H, Chen Y, et al. Long-term Efficacy of Neoadjuvant Chemoradiotherapy Plus Surgery for the Treatment of Locally Advanced Esophageal Squamous Cell Carcinoma: The NEOCRTEC5010 Randomized Clinical Trial. *JAMA Surg*. 2021;156(8):721–729. DOI 10.1001/jamasurg.2021.2373. PMID 34160577. PMC8223138. OA:Y. Route: Europe PMC 摘要。
- **[S42] PASS** Stahl M, Stuschke M, Lehmann N, et al. Chemoradiation with and without surgery in patients with locally advanced squamous cell carcinoma of the esophagus. *J Clin Oncol*. 2005;23(10):2310–2317. DOI 10.1200/JCO.2005.00.034. PMID 15800321. OA:N. Route: Europe PMC 摘要。
- **[S43] PASS** Bedenne L, Michel P, Bouché O, et al. Chemoradiation followed by surgery compared with chemoradiation alone in squamous cancer of the esophagus: FFCD 9102. *J Clin Oncol*. 2007;25(10):1160–1168. DOI 10.1200/JCO.2005.04.7118. PMID 17401004. OA:N. Route: Europe PMC 摘要。
- **[S44] PASS** Vellayappan BA, Soon YY, Ku GY, Leong CN, Lu JJ, Tey JC. Chemoradiotherapy versus chemoradiotherapy plus surgery for esophageal cancer. *Cochrane Database Syst Rev*. 2017;8:CD010511. DOI 10.1002/14651858.CD010511.pub2. PMID 28829911. PMC6483706. Route: Europe PMC 摘要。
- **[S45] PASS** Tang H, Tan L, Shen Y, et al. CMISG1701: a multicenter prospective randomized phase III clinical trial comparing neoadjuvant chemoradiotherapy to neoadjuvant chemotherapy followed by minimally invasive esophagectomy in patients with locally advanced resectable esophageal squamous cell carcinoma (cT3-4aN0-1M0) (NCT03001596). *BMC Cancer*. 2017;17(1):450. DOI 10.1186/s12885-017-3446-7. PMID 28659128. PMC5490174. OA:Y. Route: Europe PMC 摘要。
- **[S46] PASS** Wang H, Tang H, Fang Y, et al. Morbidity and Mortality of Patients Who Underwent Minimally Invasive Esophagectomy After Neoadjuvant Chemoradiotherapy vs Neoadjuvant Chemotherapy for Locally Advanced Esophageal Squamous Cell Carcinoma: A Randomized Clinical Trial. *JAMA Surg*. 2021;156(5):444–451. DOI 10.1001/jamasurg.2021.0133. PMID 33729467. PMC7970392. OA:Y. Route: Europe PMC 摘要。
- **[S47] PASS** Tang H, Wang H, Fang Y, et al. Neoadjuvant chemoradiotherapy versus neoadjuvant chemotherapy followed by minimally invasive esophagectomy for locally advanced esophageal squamous cell carcinoma: a prospective multicenter randomized clinical trial. *Ann Oncol*. 2023;34(2):163–172. DOI 10.1016/j.annonc.2022.10.508. PMID 36400384. OA:N. Route: Europe PMC 摘要。
- **[S48] PASS** Noordman BJ, Wijnhoven BPL, Lagarde SM, et al. Neoadjuvant chemoradiotherapy plus surgery versus active surveillance for oesophageal cancer: a stepped-wedge cluster randomised trial (SANO protocol). *BMC Cancer*. 2018;18(1):142. DOI 10.1186/s12885-018-4034-1. PMID 29409469. PMC5801846. OA:Y. Route: Europe PMC 摘要。
- **[S49] PASS** van der Wilk BJ, Eyck BM, Wijnhoven BPL, et al.; SANO Study Group. Neoadjuvant chemoradiotherapy followed by active surveillance versus standard surgery for oesophageal cancer (SANO trial): a multicentre, stepped-wedge, cluster-randomised, non-inferiority, phase 3 trial. *Lancet Oncol*. 2025;26(4):425–436. DOI 10.1016/S1470-2045(25)00027-0. PMID 40112851. OA:N. Route: Europe PMC 完整摘要（2 年 OS、HR、n、追蹤）。**全文抓不到**（FAIL-2）——族群組織型態、遠端轉移率、cCR 維持率等細部數字改引 [S51][S52][S53][S54]。
- **[S50] PASS** Gangaram Panday SSG, van der Wilk BJ, Eyck BM, et al.; SANO Study Group. Health-related quality of life of patients undergoing active surveillance versus standard surgery for oesophageal cancer (SANO trial). *Br J Surg*. 2025;113(1):znaf286. DOI 10.1093/bjs/znaf286. PMID 41591326. OA:N. Route: Europe PMC 摘要。
- **[S51] PASS** Gangaram Panday SSG, van Klaveren D, Lagarde SM, et al. Accuracy of Predicting Residual Disease and Disease Progression During Active Surveillance for Esophageal Cancer. *Ann Surg Oncol*. 2026;33(2):946–954. DOI 10.1245/s10434-025-18531-y. PMID 41128955. PMC12765740. OA:Y. Route: Europe PMC 摘要（37% cCR；25% 維持 cCR at 54 個月）。
- **[S52] PASS** Pittacolo M, Khoma O, Lagarde SM, Mostert B, Wijnhoven BPL. Organ-Sparing Approach after Neoadjuvant Treatment in Oesophageal Cancer. *Dig Surg*. 2025;42(5):247–256. DOI 10.1159/000547632. PMID 40730139. PMC12503578. OA:Y. Route: fullTextXML（SANO 段落：中位 OS 43 vs 53 個月、48%/17%/35%、腺癌 30% 持續 cCR、手術組約四分之一改選監測）。註：作者含 SANO 團隊成員（Lagarde、Mostert、Wijnhoven）。
- **[S53] PASS（立場性編輯評論，引用時須標明為批評方）** Housman BN, Tuminello S, Flores R. Does the Dutch trial prove we should "say no" to active surveillance? An in-depth review of the 2025 study on the treatment of esophageal cancer. *JTCVS Open*. 2025;28:654–656. DOI 10.1016/j.xjon.2025.10.019. PMID 41473087. PMC12745133. OA:Y（CC BY）. Route: fullTextXML 全文；文中引 SANO 正文與附錄表 S4/S6 之數字（pT0 36/101；鱗癌 24%/21%；遠端轉移 43%/34%；30/90 天死亡 3%/5% 與 1%/4%；中位追蹤 34/50 個月）。**這些數字為二手轉述**，正文引用時寫「批評者從 SANO 附錄整理出…」。
- **[S54] PASS** van der Wilk BJ, Wijnhoven BPL, van Lanschot JJB. Active surveillance for esophageal cancer after clinically complete response: relevant considerations of the SANO-trial. *J Thorac Dis*. 2026;18(4):435. DOI 10.21037/jtd-2026-1-0282. PMID 42182714. PMC13190024. OA:Y. Route: fullTextXML 全文（46% 未手術；遠端轉移非顯著差異偏向手術；長期不能排除；試驗外效果較差；ESOPEC 化放療臂 pCR 10%）。
- **[S55] PASS** Bondzi-Simpson A, Gupta V, Ribeiro T, et al. Esophagectomy vs Active Surveillance in Clinical Complete Responders After Neoadjuvant Chemoradiation (decision analytical model). *JAMA Surg*. 2026;161(3):275–282. DOI 10.1001/jamasurg.2025.5890. PMID 41563781. OA:N. Route: Europe PMC 摘要。
- **[S56] PASS** Nilsson M, Olafsdottir H, Alexandersson von Döbeln G, et al. Neoadjuvant Chemoradiotherapy and Surgery for Esophageal Squamous Cell Carcinoma Versus Definitive Chemoradiotherapy With Salvage Surgery as Needed: The Study Protocol for the Randomized Controlled NEEDS Trial. *Front Oncol*. 2022;12:917961. DOI 10.3389/fonc.2022.917961. PMID 35912196. PMC9326032. OA:Y. Route: fullTextXML（非劣性邊界 7.5%、1,200 人、HR 1.26）。
- **[S57] PASS** ClinicalTrials.gov NCT04460352 “Chemoradiotherapy Followed by Planned Surgery or by Surveillance and Surgery Only When Needed for Oesophageal Cancer (NEEDS)”. Karolinska University Hospital. Status RECRUITING；start 2020-11-27；enrollment 1,020 (ESTIMATED)；primary completion 2026-12-31 (EST)；completion 2031-12-31 (EST)；last update 2025-03-06. https://clinicaltrials.gov/study/NCT04460352。Route: API v2（2026-09-02）。
- **[S58] PASS** ClinicalTrials.gov NCT02551458 “Comparison of Systematic Surgery Versus Surveillance and Rescue Surgery in Operable Oesophageal Cancer With a Complete Clinical Response to Radiochemotherapy (Esostrate)”. CHU Dijon. Status TERMINATED；whyStopped「sub-optimal inclusion rate, additional 9 years to finalize inclusion and follow-up of all patients」；enrollment 188 (ACTUAL)；start 2016-03-14；primary completion 2023-03-15；last update 2024-03-07. https://clinicaltrials.gov/study/NCT02551458。Route: API v2。
- **[S59] PASS** ClinicalTrials.gov NCT04886635 “Surgery As Needed for Oesophageal Cancer - 2 (SANO-2)”. Status RECRUITING；enrollment 360 (EST)；start 2021-03-09；last update 2024-02-20. Route: API v2。
- **[S60] PASS** ClinicalTrials.gov NCT05491616 “Nivolumab During Active Surveillance After Neoadjuvant Chemoradiation for Esophageal Cancer: SANO-3 Study”. Erasmus MC. Status ACTIVE_NOT_RECRUITING；enrollment 77 (ACTUAL)；completion est. 2026-10. Route: API v2。
- **[S61] PASS** Zhang X, Eyck BM, Yang Y, et al. Accuracy of detecting residual disease after neoadjuvant chemoradiotherapy for esophageal squamous cell carcinoma (preSINO trial): a prospective multicenter diagnostic cohort study (protocol). *BMC Cancer*. 2020;20(1):194. DOI 10.1186/s12885-020-6669-y. PMID 32143580. PMC7060643. OA:Y. Route: fullTextXML（CROSS pCR 鱗癌 49%／腺癌 23%；NEOCRTEC5010 43.2%；作者含台灣 Chao YK、Hou MM、Hung TM）。
- **[S62] PASS** Yang Y, Liu Z, Wong I, et al. Detecting residual disease after neoadjuvant chemoradiotherapy for oesophageal squamous cell carcinoma: The prospective multicentre preSINO trial. *Br J Surg*. 2025;112(2):znaf004. DOI 10.1093/bjs/znaf004. PMID 39937490. PMC11816269. OA:Y. Route: Europe PMC 摘要。
- **[S63] PASS** Takeuchi H, Ito Y, Machida R, et al. A Single-Arm Confirmatory Study of Definitive Chemoradiation Therapy Including Salvage Treatment for Clinical Stage II/III Esophageal Squamous Cell Carcinoma (JCOG0909 Study). *Int J Radiat Oncol Biol Phys*. 2022;114(3):454–462. DOI 10.1016/j.ijrobp.2022.07.007. PMID 35932949. OA:N. Route: Europe PMC 摘要（5 年數字取自 [S30] JES 全文之轉述）。
- **[S64] PASS** Markar S, Gronnier C, Duhamel A, et al. Salvage Surgery After Chemoradiotherapy in the Management of Esophageal Cancer: Is It a Viable Therapeutic Option? *J Clin Oncol*. 2015;33(33):3866–3873. DOI 10.1200/JCO.2014.59.9092. PMID 26195702. OA:N. Route: Europe PMC 摘要。
- **[S65] PASS** Markar SR, Karthikesalingam A, Penna M, Low DE. Assessment of short-term clinical outcomes following salvage esophagectomy for the treatment of esophageal malignancy: systematic review and pooled analysis. *Ann Surg Oncol*. 2014;21(3):922–931. DOI 10.1245/s10434-013-3364-0. PMID 24212722. OA:N. Route: Europe PMC 摘要。
- **[S66] PASS** Kumagai K, Mariosa D, Tsai JA, et al. Systematic review and meta-analysis on the significance of salvage esophagectomy for persistent or recurrent esophageal squamous cell carcinoma after definitive chemoradiotherapy. *Dis Esophagus*. 2016;29(7):734–739. DOI 10.1111/dote.12399. PMID 26316181. OA:N. Route: Europe PMC 摘要。
- **[S67] PASS** Sakai M, Kuriyama K, Nagai K, Shirabe K, Saeki H. Systematic Review and Meta-Analysis on the Efficacy and Safety of Salvage Esophagectomy for T4 Esophageal Squamous Cell Carcinoma. *Ann Gastroenterol Surg*. 2026; DOI 10.1002/ags3.70233. PMID 42495669. OA:N（卷期頁未定）. Route: Europe PMC 摘要。
- **[S68] PASS** Low DE, Kuppusamy MK, Alderson D, et al. Benchmarking Complications Associated with Esophagectomy. *Ann Surg*. 2019;269(2):291–298. DOI 10.1097/SLA.0000000000002611. PMID 29206677. OA:N. Route: Europe PMC 摘要。
- **[S69] PASS** Kuppusamy MK, Low DE; International Esodata Study Group. Evaluation of International Contemporary Operative Outcomes and Management Trends Associated With Esophagectomy: A 4-Year Study of >6000 Patients Using ECCG Definitions and the Online Esodata Database. *Ann Surg*. 2022;275(3):515–525. DOI 10.1097/SLA.0000000000004309. PMID 33074888. OA:N. Route: Europe PMC 摘要。
- **[S70] PASS** Takeuchi H, Miyata H, Gotoh M, et al. A risk model for esophagectomy using data of 5354 patients included in a Japanese nationwide web-based database. *Ann Surg*. 2014;260(2):259–266. DOI 10.1097/SLA.0000000000000644. PMID 24743609. OA:N. Route: Europe PMC 摘要。
- **[S71] PASS** Voeten DM, Busweiler LAD, van der Werf LR, et al.; DUCA Group. Outcomes of Esophagogastric Cancer Surgery During Eight Years of Surgical Auditing by the Dutch Upper Gastrointestinal Cancer Audit (DUCA). *Ann Surg*. 2021;274(5):866–873. DOI 10.1097/SLA.0000000000005116. PMID 34334633. OA:N. Route: Europe PMC 摘要。
- **[S72] PASS（低階證據，回溯）** Smyth NM, Bass GA, Kharytaniuk N, Sorensen J, Hill ADK, Walsh TN. Long-term outcome of patient choice of surgery or active surveillance following a clinical complete response to neoadjuvant chemoradiotherapy for oesophageal cancer. *Eur J Surg Oncol*. 2026;52(1):111171. DOI 10.1016/j.ejso.2025.111171. PMID 41223456. OA:N. Route: Europe PMC 摘要。

### 台灣行政端

- **[S73] PASS** 全民健康保險保險對象免自行負擔費用辦法 第 2 條 及 附表一「全民健康保險重大傷病項目及其證明有效期限」（含「一百十三年十二月三十一日以前適用」與「一百十四年一月一日以後適用」兩版；「一、需積極或長期治療之癌症（五）除（一）～（四）之其他惡性腫瘤 C00.0–C96.9…五年」）。https://law.moj.gov.tw/LawClass/LawSingle.aspx?Pcode=L0060015&FLNO=2；附表一 PDF：https://law.moj.gov.tw/LawClass/LawGetFile.ashx?FileId=0000375263&lan=C。Route: curl（200）＋ pdfplumber。
- **[S74] PASS** 衛生福利部（國民健康署）。〈撥打0800-636363戒菸專線的五大理由〉新聞稿。https://www.mohw.gov.tw/cp-16-76938-1.html。Route: curl（200）；服務時間、Line 帳號、成功率約四成。
- **[S75] PASS** 衛生福利部口腔健康司。〈戒檳諮詢服務醫療機構查詢〉（建檔 115-08-17、更新 115-08-19，含各縣市醫療機構名冊與專線）。https://dep.mohw.gov.tw/DOOH/cp-7148-87465-124.html；上層頁「口腔癌及檳榔危害防制」https://dep.mohw.gov.tw/DOOH/lp-7148-124.html。Route: curl（200）。
- **[S76] PASS** 衛生福利部（心理健康司）。〈115年度酒癮治療費用補助方案〉說明書（114-11-04 衛部心字第1141762971號函核定；115-03-30 修訂）。PDF：https://www.mohw.gov.tw/dl-97529-a0e4a473-9fc6-41ab-baaf-f0b08d3f5d28.html。Route: 下載 PDF（31 頁）＋ pdfplumber；每人每年上限 4 萬元、藥費上限 2 萬元、限指定機構、補助非健保給付自費項目。

### FAIL／NOT-CITABLE（查過、抓不到或不存在）

- **FAIL-1** ESMO 2022 CPG（Obermannová, Ann Oncol 2022;33:992–1004）全文：annalsofoncology.org 回 403；Europe PMC 無全文；ESMO 官方頁需 JS。→ 書目可引[S31]，**條文措辭不可引**；鱗癌措辭改引 2025 interim update [S15]。
- **FAIL-2** SANO 主論文全文（Lancet Oncol 2025）：thelancet.com 與 sciencedirect 回 403。→ 摘要數字可引[S49]；細部改引 [S51][S52][S53][S54]。
- **FAIL-3** Nierengarten MB. Active surveillance after neoadjuvant chemoradiotherapy for esophageal cancer. *Cancer* 2025 (DOI 10.1002/cncr.35924)：Wiley 403，未讀到內容，不引。
- **FAIL-4** Cancer Therapy Advisor「SANO 5-year QALE」新聞：402；內容對應 [S55]，以 [S55] 取代。
- **FAIL-5** ASCO「Locally Advanced Esophageal Carcinoma」2024 更新：Europe PMC 查無此文；只有 2020 版[S32]。SPEC 需修正。
- **FAIL-6** hpa.gov.tw（癌症登記年報、112 年癌登新聞稿原頁、歷年報告）：TLS handshake 失敗（curl exit 60；WebFetch robots.txt SSL 失敗）。→ 111／112 年食道癌絕對新發人數、官方鱗癌比例、官方期別分布＝gap。
- **FAIL-7** nhi.gov.tw（重大傷病專區、申請須知）：403（Cloudflare）。→ 以法規資料庫 [S73] 取代。
- **FAIL-8** ESOSTRATE 結果論文：Europe PMC TITLE:"ESOSTRATE" 零筆；僅 CT.gov 記錄[S58]。
- **FAIL-9** 肥胖／BMI 與食道腺癌合併分析（Hoyo 2012, Int J Epidemiol）：Europe PMC 查詢時 API 回非 JSON（暫時性錯誤），未完成核對；A1 不引肥胖 OR，只用官方致癌因子清單[S4]。
- **FAIL-10** 台灣「化放療後 cCR 主動監測」之本土研究：Europe PMC 查無；gap。
- **FAIL-11** 台灣癌登 nCRT＋手術 vs dCRT 的官方（非期刊）統計：無；以 [S33][S34] 期刊研究取代。
- **FAIL-12** SINO（中國鱗癌隨機試驗）登錄：ClinicalTrials.gov 查無；只寫「preSINO 完成、SINO 尚未見登錄」。
- **NOT CONSULTED** NCCN（依 RESEARCH-COMMON 規定不引）。
