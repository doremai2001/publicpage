# Brief B — 乳房放療專題主張核心組（B1 心臟劑量／B2 TOMO／B3 質子）

研究員：Group B｜查證日期：2026-08-31｜期刊書目全部經 Europe PMC REST 逐筆核對（PMID、DOI、卷期頁）；引語層級的句子出自可取得之全文（Europe PMC / NCBI XML）；registry 經 ClinicalTrials.gov API v2 實抓；官方頁面與健保支付標準開放資料全表（ODS，6,013 項）經實際下載檢索。
引用規則：**只有標 PASS 的來源可以進正文引用。** FAIL / NOT-CITABLE 條目保留，供作者知道查過什麼、哪些話只能寫「查不到可引用的來源」。
沿用先前專題已查證項目（Newhauser & Zhang、高雄長庚收費頁、兒童質子公告）已於 2026-08-31 重新確認連結與內容。

## ⚠ 與 SPEC 假設不同形狀的事（動筆前必讀，即 §八修正建議）

1. **DIBH 降幅「常見 40–50% 級」要改寫成「約 20–70%、個別差異大」。** 可引的統合分析都用標準化平均差（SMD）呈現，不給單一百分比[S7][S8][S9]；給百分比區間的是 OA 綜述 Bergom 2022：「約 20–70%」[S6]，與一篇 MCO 規劃研究的「DIBH 後心臟劑量約為自由呼吸的 70–74%（即降約 26–30%）」[S22]。40–50% 這個中間數查無單一可引出處——寫區間、標「因人而異」，比寫一個查無出處的中位數安全。
2. **「基本款站得住」比 SPEC 預期的更有數字可撐。** 現代（2014 後）左乳平均心臟劑量的文獻平均已降到 3.6 Gy、2017 年發表者平均 2.6 Gy[S4]；荷蘭 910 人世代（3D-CRT 為主、未特別做 DIBH）中位數 2.37 Gy[S2]；單機構 4,687 人實測左側傳統分次中位 2.16 Gy、低分次 1.47 Gy[S5b]。紅線 1 的「不自費也顧得到心臟」可以直接用這串數字寫成段。
3. **TOMO「不是全面較優」的反向證據比預期強，而且有台灣資料。** 台灣單中心 108 人比較（左乳＋區域淋巴，含內乳次族群）：**VMAT 的平均心臟劑量比 TOMO 低（3.82 vs 5.13 Gy，p<0.001）**，肺、對側乳房、食道亦然[S13]。B2 不能寫成「TOMO 對心臟比較好」；要寫成「旋轉調控技術（TOMO／VMAT）對複雜標靶較優，TOMO 與 VMAT 之間互有勝負、看情境與規劃」。
4. **TOMO 的隨機比較不是零，但唯一一個（TomoBreast，n=121–123）比的是「TOMO 低分次影像導引」對「傳統分次傳統技術」，分次與技術混在一起**，且 QOL 主分析經校正後兩組無顯著差異[S19]；12 年的肺心功能複合終點偏 TOMO 組，作者自己說是 proof-of-concept[S20]。**「TOMO vs 一般 IMRT」的隨機療效比較查無**（檢索紀錄見 FAIL-6）。
5. **RADCOMP 已收案完成但主要終點離讀出很遠：registry 的主要完成日估在 2036-11。** 2026-08-31 實查 ClinicalTrials.gov（NCT02603341）：ACTIVE_NOT_RECRUITING、收案 1,238、最後更新 2025-11-06、**hasResults: false**[S27]。2026 年的回顧文章轉述：收案 2024 年完成（n=1,239）、2025 年生活品質分析兩臂同樣好、主要終點（局部控制與重大心臟事件）未讀出[S36]。「未讀出」不是「快讀出」——這格會空很多年，B3 要照 SPEC 寫「未讀出」。
6. **質子的皮膚故事是兩面的，都有 2026 年資料**：一個隨機 phase II 期中分析（26 Gy/5 fx）質子組急性皮膚炎顯著較多（97.2% vs 75%，多為輕度）[S33]；但另一個 176 人的術後胸壁比較顯示，IMPT 用皮膚限制條件規劃後 ≥G2 皮膚炎與光子相同（47% vs 48%）[S34]。寫「質子皮膚反應比較重」或「一樣」都是超過——正確寫法是「入射端沒有光子的皮膚保護效應，皮膚劑量取決於規劃，早期經驗偏多、用限制條件可以壓回來」。
7. **台灣端最重要的官方事實**：健保支付標準全表（114-05-01 版）中，**乳癌低分次包裹碼 36022B／36023B 存在且適應症明文「不含鎖骨上、腋下或內乳淋巴結」**；放射治療章節**沒有 IMRT 專屬治療碼、沒有 TOMO 專屬碼、沒有任何呼吸調控／DIBH 項目**（IMRT 出現在 36015B「電腦治療規劃—複雜」的文字裡；治療本身以直線加速器照野碼計費）[S38]。質子在全表只有 N21301–N21308 八個標註「HTA項目」、點數 0 的登錄項[S38]；健保給付的質子三碼（36025B–36027B，115-01-01 生效）全部「限年齡未滿十九歲」[S40][S41]。**TOMO 與光子 DIBH 的自費／差額金額查無任何官方公告＝gap（問醫務課）**；質子端唯一可引的官方價是高雄長庚收費頁[S42]。

---

## B1 `brt-heart`〈心臟劑量：左側的核心課題〉【主張核心｜紅線 1】

### Key facts

**Darby 2013——全專題的錨（逐欄核對，全部與原文一致）[S1]**

- 設計：**族群式病例對照研究**（population-based case-control），1958–2001 年在**瑞典與丹麥**接受乳癌放療的 2,168 名女性；963 名發生「主要冠狀動脈事件」（心肌梗塞、冠狀動脈血管重建、缺血性心臟病死亡）、1,205 名對照。逐人由放療紀錄重建全心與左前降支（LAD）平均劑量。
- 全心平均劑量的平均值 **4.9 Gy**（範圍 0.03–27.72）。
- 主要冠狀動脈事件發生率**隨平均心臟劑量線性上升，每 Gy 增加 7.4%**（95% CI 2.9–14.5，p<0.001）；**無明顯閾值**（no apparent threshold）。
- **風險上升自放療後五年內開始，持續到第三個十年。**
- 每 Gy 的「比例上升」在有無心血管風險因子者相似——但**基線風險高的人，同樣的比例乘上去，絕對增量比較大**（原文結論句）。寫法沿 bc-rt-regional 已定調的「相對比例、不是每 Gy 多 7.4 個人」句式。
- 年代註記要寫：這是 1958–2001 年的技術（平均 4.9 Gy 是那個年代的劑量）；現代劑量見下。

**驗證研究——Darby 的斜率被獨立世代重現[S2]**

- van den Bogaard 2017（荷蘭，910 名乳房保留手術後放療、3D 劑量資料）：中位平均心臟劑量 **2.37 Gy**（0.51–15.25）；中位追蹤 7.6 年、30 例急性冠狀動脈事件；**累積發生率每 Gy 上升 16.5%**（95% CI 0.6–35.0，p=.042），作者明言以平均心臟劑量計算的每 Gy 相對增幅**與 Darby 相似**；左心室 V5 是比平均心臟劑量更好的預測子。→「劑量—事件關係在現代劑量範圍也成立」的引用。

**現代劑量水準——紅線 1 的地基（「基本款本身站得住」的數字）**

- 系統性回顧（2003–2013 發表，149 篇、398 種療程）：左乳平均心臟劑量平均 **5.4 Gy**；不含內乳者 4.2 Gy；**切線照野＋呼吸控制 1.3 Gy**；質子 0.5 Gy[S3]。
- 更新回顧（2014–2017 發表，99 篇）：左乳平均降到 **3.6 Gy**；**有呼吸控制 1.7 Gy vs 無 4.5 Gy（p<.0001）**；發表年 2014 的 4.6 Gy 一路降到 2017 的 2.6 Gy；LAD 平均劑量 12.4 Gy[S4]。
- 單機構 4,687 人實測（2011–2018）：左側傳統分次（50 Gy/25 fx）中位平均心臟劑量 **2.16 Gy**、低分次（42.6 Gy/16 fx）**1.47 Gy**；2015 年後因寬切線（含內乳）使用增加而略回升[S5b]。
- 絕對風險的天花板句（給「把 7.4% 翻成白話」用）[S5]：EBCTCG 個別病人資料統合（40,781 人、75 個試驗）＋現代劑量（2010–2015 平均全心 4.4 Gy）推估：**現代放療造成的心臟死亡絕對風險，不吸菸者約 0.3%、長期吸菸者約 1%**；肺癌部分吸菸者約 4%、不吸菸者 0.3%——「戒菸能改變放療的淨效益」是原文結論。此為模型推估，標籤要寫。

**DIBH——機轉、降幅、LAD、臨床證據現況**

- 機轉（可直接引的句子）：DIBH「利用呼吸週期的自然生理，在整個療程中**拉開心臟與治療標靶的距離**」；使全心與 LAD 平均劑量**降低約 20–70%**[S6]。
- 統合分析（左側，12 篇觀察性研究、n=1,019）：DIBH 對比自由呼吸，心臟劑量 SMD −1.36（95% CI −1.64～−1.09）、**LAD SMD −1.45**、左肺 SMD −0.52，**標靶涵蓋無差異**[S8]。
- VMAT 情境的統合（11 篇）：心臟 Dmean、LAD、同側肺、對側肺、對側乳房全部較低；各次族群（全乳、含瘤床加強、含淋巴照射）方向一致[S7]。
- 早期系統性回顧的換算句（把 Gy 翻成風險的現成句）：DIBH 最多可降平均心臟劑量 3.4 Gy，「以目前對放療心臟毒性的估計，相當於把預期增加的心臟病風險降低 13.6%」[S12]。
- **臨床事件證據現況（誠實段，紅線 1 反向）**：以上全部是**劑量學終點**。DIBH 降低「心臟事件」的直接證據，查無任何已讀出的隨機或大型世代比較（檢索紀錄 FAIL-5）；鏈條寫法照 SPEC §一：「劑量降低量得到（統合分析）＋劑量與事件的關係是世代級證據（Darby、van den Bogaard）」，兩截分開標。
- **適用性（不是每個人都閉得住氣）[S6]**：Bergom 綜述引述——一項研究中 72 名經過預選與訓練的病人仍有 **29% 無法完成 DIBH 定位掃描**；另一研究 112 人中 20 人無法耐受 ABC（主動呼吸控制）系統；估計約 75% 做 DIBH 的病人有劑量學獲益——「逐案評估、不是人人都需要或都做得到」是綜述原句方向。定位時做得起來是療程能完成的正向預測子。

**左側 vs 右側**

- 左側平均心臟劑量本質較高：同一系統性回顧，**左側 5.4 Gy vs 右側 3.3 Gy**（2003–2013 文獻平均）[S3]。
- **內乳照射把心臟劑量翻倍**：左側含內乳者平均約 8 Gy、不含者 4.2 Gy——「Inclusion of the IMC doubled typical heart dose」是原文結論句[S3]。→ 右側何時也要心臟考量：照內乳時。
- 臨床事件的側別數字（前瞻世代，非隨機）：丹麥 DBCG IMN2 以側別分配內乳照射（右側照、左側不照，**設計理由就是避開左側心臟劑量**），4,541 人中位追蹤 13.7 年：**15 年缺血性或瓣膜性心臟病死亡累積發生率右側 0.2% vs 左側 0.7%**[S11]。此數字 bc-rt-regional 已引過，本專題引用時指路該篇、不重複 IMN 效益論證（SPEC §五）。

### Claim ceiling（硬上限）

- 可寫：「平均心臟劑量每多 1 Gy，主要冠狀動脈事件率相對上升 7.4%，無明顯安全下限，五年內就開始」（帶族群標籤：瑞典丹麥 1958–2001 世代）；「這條劑量—風險線在現代劑量的荷蘭世代被重現（每 Gy 約 16.5%）」；「現代技術下左乳平均心臟劑量文獻平均約 2–4 Gy、呼吸控制下 1.3–1.7 Gy」；「DIBH 把心臟與 LAD 劑量降低約 20–70%（劑量學）」；「不吸菸者現代放療的心臟死亡絕對風險估約 0.3%（模型推估）」。
- **不可寫**：「每 Gy 多 7.4% 的人出事」（相對 vs 絕對混淆——bc-rt-regional 的括號句照搬）；「DIBH 已證明減少心臟病發作」（零事件級證據）；「不做 DIBH 心臟就顧不到」（紅線 1 正向——基本款數字段必須在 DIBH 段之前或同段存在）；反向「現在技術進步所以 Darby 不重要了」也超線（van den Bogaard 就是在 2.37 Gy 的中位劑量看到斜率；無閾值）。
- 右側不可寫成「不用管心臟」——照內乳時劑量翻倍[S3]；也不可寫成與左側等同（0.2% vs 0.7% 的世代數字擺著）。

### Caveats

- Darby 的「無閾值」是統計上「看不到明顯閾值」，不是「證明了任何劑量都有害」；寫「研究沒有看到明顯的安全下限」（bc-rt-regional 已用此句式）。
- van den Bogaard 只有 30 個事件、CI 很寬（0.6–35.0）——引用時給 CI。
- DIBH 統合分析全部是規劃研究層級（同一病人兩套計畫或前後對照），不是隨機分派。

### 台灣現況（B1 的健保與自費段）

- **基本款健保有付**：乳癌放療以直線加速器照野碼（36011B/36012B 等）＋電腦治療規劃計費；「電腦治療規劃—複雜」（36015B，11,483 點）明文包含「順形放射治療、**強度調控放射治療**、立體定位放射治療等技術」之設計[S38]。保留手術後全乳低分次另有包裹碼 36022B（含瘤床加強，279,986 點）／36023B（不含，246,960 點），適應症明文不含區域淋巴（詳 A2 主場，本篇一句話）[S38][S39]。
- **DIBH／呼吸調控：健保支付標準全表查無任何呼吸調控或閉氣相關項目**[S38]；光子 DIBH 的自費收費也**查無任何醫院官方公告**（FAIL-3）→ 正文照慣例寫「請向醫院醫務課確認」。可引的唯一官方呼吸調控價格是高雄長庚**質子**呼吸調控（每次 5,000／9,600 元），引用時必須標明是質子項目、單一機構公告[S42]。

---

## B2 `brt-tomo`〈TOMO 與一般 IMRT 差在哪〉【紅線 1】

### Key facts

**TOMO 是什麼（一句話，骨架歸 A3）**：螺旋斷層放射治療（helical tomotherapy）是旋轉式強度調控的一種——與 VMAT 同屬「旋轉調控」，與固定野 IMRT 同屬強度調控家族；技術骨架圖歸 A3，本篇只寫差異。

**有意義的差——TOMO（或旋轉調控）佔優的情境**

- **複雜標靶／困難解剖**：法國 Institut Curie 系列明言 TOMO 用於「解剖困難的個案」（anatomically challenging cases）——複雜標靶與特殊解剖時提供高順形度[S16]；「complex target volumes and specific anatomic considerations」同句出現在另一法國系列[S15]。
- **胸壁＋區域淋巴（含內乳）的照野**：TD／HT／VMAT 三方比較（30 名 PMRT 病人）：**含區域淋巴的複雜標靶，HT 與 VMAT 的涵蓋與危及器官保護整體優於固定野式 TomoDirect**；HT 的均勻度、順形度、涵蓋在所有情境最好[S14]。左側 PMRT＋內乳的 HT 規劃研究（26 人）：HT（加方向性阻擋）平均心臟劑量 4.79 Gy vs 固定野 IMRT 6.39 Gy，內乳 D95 涵蓋較佳[S22]。
- **重建後胸壁**：120 名立即重建後低分次 PMRT 用 HT 的前瞻分析：七成計畫同時達成胸壁＋淋巴涵蓋與危及器官保護之最適標準，急性毒性最高 G2（36.7%）——可行性與劑量學可引，無比較組[S21]。
- **雙側乳癌**（特殊情境）：HT 在雙側同時照射的比較中平均心臟劑量最低（HT 3.53 vs VMAT 5.6、IMRT 3.80、FIF 4.84 Gy），肺與 LAD 亦最低；代價是治療時間最長（11.0 vs VMAT 3.9 分鐘）[S18]。

**差異小或反向的情境——「TOMO 不是全面較優」（紅線 1 反向，有源）**

- **低劑量浴是 TOMO 的內建代價**（可直接引的句子）：螺旋 TOMO「對複雜標靶提供順形照射與有效的危及器官保護，**但增加非標靶體積的『低劑量浴』（low-dose bath）**」[S15]。
- **台灣 108 人比較（左乳＋區域淋巴，2017–2020）：VMAT 全面優於 HT**——平均心臟劑量 3.82 vs 5.13 Gy（p<0.001）、心臟 V5–V20、全肺平均、**對側乳房**與食道平均劑量皆較低；**含內乳的次族群 VMAT 優勢持續**；HT 只在甲狀腺平均劑量佔優；不含內乳時兩者心肺與對側乳房平均劑量相近[S13]。
- TD/HT/VMAT 比較同方向：**VMAT 的對側乳房與心臟低劑量區比 HT 好**；只照胸壁（不含淋巴）時固定野 TomoDirect 反而對側器官保護最好[S14]。
- 單純全乳或部分乳房：HT 的 APBI 系列平均心臟劑量 0.82 Gy——好，但這種情境切線／固定野技術本來就低（見 B1 現代劑量段），差異小[S16b 不設，逕用 B1 數字對照]。

**臨床結果比較的證據現況（誠實段）**

- **TOMO vs 一般 IMRT 的隨機療效比較：查無**（FAIL-6）。唯一含 TOMO 的隨機試驗是 TomoBreast（比利時單中心，n=121–123）：**TOMO 低分次影像導引 vs 傳統分次傳統放療**——分次與技術綁在一起比。QOL 主分析：Bonferroni 校正後**兩組所有面向無顯著差異**[S19]；12 年追蹤的肺心功能複合終點（病人回報＋臨床＋心臟超音波＋肺功能任一惡化 10%）偏 TOMO 組（受限平均存活時間多 1.46 年，p=0.041），總存活與無病存活兩組相同；作者定位為 proof-of-concept、「低分次的優勢以使用進階技術為條件」[S20]。
- 回溯比較（中國，315 人，追蹤僅 3 個月）：TOMO 組放射性肺炎較少（0% vs 4.3%）但 **G3–4 皮膚毒性較多（16.2% vs 7.6%，p=0.017）**——回溯、短期、基線用藥不均[S17]。
- 長期單臂系列：Curie 179 人（TOMO 用於困難解剖，中位平均心臟劑量 7.04 Gy——因為都是複雜個案）中位 9.1 年心血管事件 4.5%、全部發生在原有風險因子或肥胖者、無心因性死亡；作者提出 3D 時代的劑量—毒性關係在 IMRT 劑量分布下可能高估——**假說層級，不可寫成「TOMO 打破 Darby 曲線」**[S16]。

### Claim ceiling

- 可寫：「胸壁＋區域淋巴（尤其含內乳）、重建後胸壁、雙側等複雜情境，TOMO（與 VMAT 同屬旋轉調控）能同時把涵蓋與均勻度做好——這是劑量學結論」；「單純全乳等簡單情境，各技術差異小」；「TOMO 的代價是低劑量浴——大體積的低劑量，對側乳房與肺的低劑量區可能比固定野大」；「台灣一個 108 人的比較裡，VMAT 的心臟與對側乳房劑量反而比 TOMO 低」；「TOMO 對一般 IMRT 沒有隨機的療效或毒性比較；唯一的隨機試驗比的是低分次 TOMO 對傳統分次傳統技術」。
- **不可寫**：「TOMO 比較好／先進」（無條件式）；「TOMO 對心臟比較好」（台灣資料反向[S13]）；「差異只是機器不同、都一樣」（複雜標靶的劑量學差異有源[S14][S22]）；不可把 TomoBreast 的肺心功能訊號寫成「TOMO 證明減少心肺毒性」（混雜分次、單中心、複合終點）；不可把 Curie 的「未見劑量—事件相關」寫成「IMRT 時代心臟劑量不重要」。技術選擇句式照紅線 1：「適應症決定，不是預算決定」。

### Caveats

- 規劃比較研究的結果高度依賴各院的規劃目標與功力（Cancers 2021 的 HT 未用完整方向性阻擋；OABD 研究顯示阻擋策略可大幅改變 HT 的心臟劑量[S22]）——寫「同一台機器在不同醫院做出來的劑量分布可以差很多」是誠實且有源的。
- DIBH 可疊加在 TOMO 之外的光子技術；TOMO 平台的閉氣實作各院不同，本篇不展開（C1 的 DIBH 流程自查來源）。

### 台灣現況（費用誠實段）

- **健保支付標準全表（114-05-01 版，6,013 項）查無 TOMO 專屬項目**；螺旋斷層放療在健保端沒有自己的代碼——IMRT 技術的規劃已含在 36015B「電腦治療規劃—複雜」的文字中，治療以直線加速器照野碼申報[S38]。
- **TOMO 的自費差額金額：查無任何全國性官方公告或可引的醫院官方收費頁**（FAIL-2）→ 正文寫「各院收費方式不同，請向醫務課確認」；**媒體流通的 TOMO 價格絕不可引**（固定紅線）。
- 對照句可用：「同一療程，健保申報的部分與自費差額的部分怎麼算，是各院行政面的事——這篇能告訴你的是劑量學上什麼情境值得問，錢的部分請拿著這篇去問醫務課。」（符合紅線 1 句式）

---

## B3 `brt-proton`〈質子在乳房：證據走到哪一格〉【紅線 1】

### Key facts

**劑量學（機轉一句話指路 nt-proton／insight-proton，不重寫物理）**

- 布拉格峰、幾乎無出射劑量：物理總說[S23]。
- 乳房情境的心臟數字：系統性回顧（2003–2013）——**質子平均心臟劑量 0.5 Gy（範圍 0.1–0.8，不含內乳）；含內乳 2.6 Gy（1.0–6.0），是所有含內乳技術中最低**[S3]。前瞻 70 人系列實測：**全心平均 0.44 Gy、左心室 0.12 Gy**（91% 左側、含區域淋巴照射）[S29]。
- 質子＋DIBH 的疊加有限（有趣的反直覺，有源）：9 篇比較的系統性回顧——質子本身自由呼吸的平均心臟劑量已 0.48 Gy，DIBH 再降到 0.31 Gy、LAD 近似最大劑量 8.74→6.49 Gy，「以現有文獻，DIBH 對多數接受質子的乳癌病人**沒有明顯額外劑量學好處**，個別病人不排除」[S30]。→「DIBH 是姿勢、可疊加任何光子技術」的骨架句（SPEC §一 4）在質子這格的正確寫法是「質子的心臟劑量已近零，閉氣的邊際效益小」。
- 心臟功能佐證：70 人前瞻系列，質子放療前後 GLS、troponin、NT-proBNP 皆無變化[S29]。肩胛與胸壁肌肉骨骼結構劑量也顯著較低（IMPT vs VMAT 規劃比較，30 人）[S37]。

**主要前瞻資料**

- **MGH 單臂 phase II（Jimenez 2019，n=70）**：需要區域淋巴照射、被認為不適合常規放療者；91% 左側、94% II–III 期、72% 立即重建；胸壁中位 49.7 Gy(RBE)、內乳 48.8 Gy(RBE)（完整涵蓋）。**5 年局部區域失敗 1.5%、總存活 91%**；G2 放射性肺炎 1 例、無 G3 肺炎、無 G4 毒性；放療後心臟超音波與生物標記無早期變化。**5 年非計畫性再次手術（重建相關）33%**——重建族群引用時要帶這個數字[S25]。
- **RADCOMP（NCT02603341，質子 vs 光子、實務型隨機、主要終點＝重大心血管事件 MACE）——2026-08-31 實查**：ACTIVE_NOT_RECRUITING、收案 1,238、最後更新 2025-11-06、**主要完成日「估計 2036-11」、hasResults: false**；Europe PMC 查無主要結果論文[S27]。試驗計畫書可引（設計、n=1,278 規劃、終點定義）[S26]。2026 年回顧文章轉述：2024 年收案完成（n=1,239）、2025 年健康相關生活品質分析「兩臂都同樣極佳」、**主要終點（局部區域控制與重大心臟事件）未讀出**[S36]——QOL 那句只能以「回顧文章轉述」的形式引（FAIL-5）。**結論句照 SPEC：未讀出就寫未讀出。**
- 試驗內相關性子研究（單機構，71 人）：區域淋巴照射後 3 年臨床甲狀腺低下累積發生率 13%；**質子 16% vs 光子 9%（p=.14，無統計差異）**——「質子不是每個副作用都自動比較少」的可引數字[S35]。

**質子特有 trade-off（誠實段）**

- **肋骨骨折**：一個前瞻試驗世代的肋骨骨折率 **7%**，高於光子文獻預期；機轉分析指向**射程末端 LET／RBE 上升**（原文：「increased RBE at the distal edge of proton beams」）[S31]。較大的 225 人系列：3 年照野內肋骨骨折累積發生率 **3.7%、有症狀者 0.4%**（多為影像偶見）[S32]。
- **皮膚反應**：隨機 phase II 期中分析（26 Gy/5 fx，n=72 可評估）：急性皮膚炎質子 97.2% vs 光子 75%（p=0.006，最高僅 G2 一例）；期中的美容與滿意度偏光子[S33]。反向：176 人 PMRT 比較（IMPT 有皮膚限制條件）：≥G2 皮膚炎 47% vs 48%、G3 3% vs 7%，皆無差異；12 個月時光子組膚色改變反而較多（26% vs 6%）[S34]。→ 寫成「入射端沒有光子的皮膚保護效應；皮膚劑量取決於規劃」。
- 適應症框架（「誰值得考慮」的疊加條件）：PTCOG 乳癌小組共識——質子降低非標靶劑量是共識，但「**研究尚未證明質子改善光子放療達成的治療結果**」（consensus statement 摘要原句方向）；共識建議的角色集中在區域淋巴照射（尤其含內乳）、心臟風險高、解剖困難、再照射等情境[S28]。SPEC 的疊加條件（年輕＋左側＋內乳＋心臟病史）與此一致，可用共識當錨。

**「基本款已經很好」（紅線 1 對應段）**

- 直接用 B1 的現代劑量數字（呼吸控制下 1.3–1.7 Gy[S3][S4]）與 B2 的旋轉調控數字；質子把 1.5 Gy 級再壓到 0.5 Gy 級——差距是真的[S3][S29]，但這段差距對事件率的影響正是 RADCOMP 要回答、還沒回答的問題[S26][S27]。

### Claim ceiling（硬上限）

- 可寫：「質子在含內乳的區域淋巴照射，平均心臟劑量是各技術最低（文獻平均 2.6 Gy；單純乳房 0.5 Gy 級；前瞻系列實測 0.44 Gy）」；「一個 70 人的前瞻試驗：5 年局部區域失敗 1.5%、無 G3 肺炎」；「質子 vs 光子的隨機試驗（RADCOMP）已收案完成（約 1,240 人），主要終點是心血管事件，尚未讀出——registry 的主要完成日估在 2036 年」；「質子的肋骨骨折與皮膚反應有自己的機轉（射程末端 RBE），前瞻世代 7%、大系列 3 年 3.7%（有症狀 0.4%）」。
- **不可寫**：「質子對乳癌比較安全／較少心臟病」（RADCOMP 未讀出；bc-rt-regional 已寫下「這句話沒有可以引用的證據，所以我不說它」——本篇不可倒退）；「質子沒有副作用」（肋骨、皮膚、甲狀腺數字都在）；「未讀出＝沒效」也超線（劑量學差距是量得到的[S3][S29]）；**絕不寫「值得」「不貴」**；重建族群不可略過 33% 再手術率的脈絡（那是重建本身＋放療的複合結果，Jimenez 資料照實引）。
- 質子物理與台灣法規細節指向 nt-proton／insight-proton，一句話帶過（SPEC §五）。

### 台灣現況（自費身分與官方公告價）

- **健保**：115-01-01 生效新增之質子三碼 36025B／36026B／36027B（676,111／1,030,540／1,266,499 點）**適用範圍均限「年齡未滿十九歲病人」**、需事前審查、每人每原發癌終生一次[S40]；衛福部新聞稿估年約 100 名兒童受惠[S41]。**成人乳癌質子＝全自費。** 健保支付標準全表另有 N21301–N21308 質子相關項目，標註「HTA項目」、點數 0——支持「自費特殊項目登錄」的身分描述，不可寫成「健保公告不給付」[S38]。
- **官方可查的價格（單一機構公告，2026-08-31 重新抓取，頁面更新日 2026/03/27）**：高雄長庚質子治療中心收費標準頁——強度調控質子每次 NT$21,750／26,000／34,500，質子呼吸調控每次加收 5,000（一般）／9,600（複雜），另有諮詢診察費 1,000、模具 1,950、3D 斷層模擬 8,500、電腦治療規劃 11,483、MRI 模擬 7,500／12,500、質子立體定位套組 330,000 等[S42]。**該頁沒有「乳癌」專屬項目**——乳房療程總價取決於分次數（一般 15–25+ 次）與呼吸調控與否，引用時標明「該院公告、非乳癌專屬報價；不同醫院不同」；其他醫院查無官方公告→「向各院醫務課確認」。
- 對照句（與 B1/B2 呼應）：光子放療健保有付（照野碼＋36022B/36023B 包裹）、質子全自費——兩句在同一篇可對照，但不評價。

---

## 圖表數據（自繪圖的 PASS 數據錨點）

### fig-brt-heart-dibh（DIBH 吸氣把心臟拉離照野＋降幅數字）

- 機轉示意：吸氣→橫膈下移、胸廓擴張→**心臟與胸壁／照野的距離拉開**（Bergom 原句：increase the distance between the heart and the therapeutic target）[S6]。示意圖自繪，不取論文圖。
- 數字錨（帶標籤）：全心與 LAD 平均劑量降低**約 20–70%**（綜述）[S6]；呼吸控制 1.7 Gy vs 無 4.5 Gy（2014–2017 文獻平均，左側）[S4]；切線＋呼吸控制 1.3 Gy（2003–2013）[S3]；統合分析心臟 SMD −1.36、LAD −1.45、標靶涵蓋不變[S8]。
- 圖注的證據等級句：「以上為劑量學數字；心臟事件的劑量—風險關係來自世代研究（每 Gy +7.4%[S1]）」——把鏈條印在圖上，紅線 1 安全閥。

### fig-brt-technique-map（IMRT／TOMO／質子 × DIBH 適用地圖——「基本款那格要真實」）

- 「一般 IMRT/VMAT＋心臟閃避」格：現代左乳平均心臟劑量 2.16–3.6 Gy、低分次 1.47 Gy、加呼吸控制 1.3–1.7 Gy[S3][S4][S5b]——這格填真實數字，不填「陽春」。
- 「TOMO/旋轉調控」格：複雜標靶（胸壁＋淋巴＋內乳、重建、雙側、困難解剖）[S14][S16][S18][S21][S22]；代價註記「低劑量浴」[S15]、「與 VMAT 互有勝負」[S13]。
- 「質子」格：含內乳平均心臟 2.6 Gy→前瞻實測 0.44 Gy[S3][S29]；註記「隨機試驗未讀出[S27]、全自費[S40]」。
- 「DIBH」列：可疊加任何光子技術；質子格標「邊際效益小[S30]」；適用性註記「預選後仍約三成無法完成定位閉氣[S6]」。
- 側別軸：左 5.4 vs 右 3.3 Gy；內乳照射把心臟劑量翻倍（右側照內乳也要心臟考量）[S3]。

---

## 給 A 組與 C 組的協調備註

- A3 技術骨架圖用 fig-brt-technique-map 的同一組數據；A3 不重列 B 組數字，指路即可。
- A2 引 36022B/36023B 適應症原文時用 [S38]（開放資料全表）優於 bc-rt-regional 舊 PDF 連結；「不含區域淋巴」條文與計費差異 bc-rt-regional 已寫過，A2 指路。
- C1 的 DIBH 練習流程需要自己的來源；本 brief 只確認：支付標準無呼吸調控項目[S38]、高雄長庚質子呼吸調控價存在[S42]、「約三成預選病人無法完成閉氣定位」[S6]可供 C1 引用。
- C2 意外收穫：支付標準有 **37026B「放射治療之皮膚處理」244 點／週療程**[S38]——「放療期間皮膚護理健保有給付項目」這句 C2 可用，SPEC §七的「傷口護理給付」查證有部分著落。
- 心臟劑量完整論證歸 B1；B2/B3 引用 Darby 時一句話＋指向 B1（SPEC §五）。

---

## Sources（單一序列；PASS 才可入正文）

> **作者欄補查紀錄（2026-08-31）**：本表原有 14 筆期刊條目未載作者，已以 Europe PMC REST（`search?query=DOI:"…"&resultType=core` 之 `authorList`）逐筆實查補上——S14／S15／S16／S17／S18／S21／S22／S29／S30／S32／S33／S34／S35／S36，全數查得，DOI、PMID、年、卷（期）、頁碼與原表逐欄相符，未作任何更動。作者格式沿 A 組慣例：四位以內全列（末位以 & 連接），五位以上列前三位加 et al.。機構型來源（S27、S38–S42）無作者欄，以機構名代之，已於各條標註。

**B1 期刊（Europe PMC REST 核對，2026-08-31）**

- [S1] **PASS** Darby SC, Ewertz M, McGale P, et al. Risk of ischemic heart disease in women after radiotherapy for breast cancer. *N Engl J Med*. 2013;368(11):987–998. DOI: 10.1056/NEJMoa1209825. PMID 23484825.（摘要逐欄核對：2,168 人、瑞典丹麥 1958–2001、病例對照 963/1,205、平均 4.9 Gy、7.4%/Gy（95% CI 2.9–14.5）、無明顯閾值、五年內開始、持續至第三個十年、風險因子者絕對增量較大）https://doi.org/10.1056/NEJMoa1209825
- [S2] **PASS（OA，PMC5455600）** van den Bogaard VAB, Ta BDP, van der Schaaf A, et al. Validation and Modification of a Prediction Model for Acute Cardiac Events in Patients With Breast Cancer Treated With Radiotherapy Based on Three-Dimensional Dose Distributions to Cardiac Substructures. *J Clin Oncol*. 2017;35(11):1171–1178. DOI: 10.1200/JCO.2016.69.8480. PMID 28095159. https://doi.org/10.1200/JCO.2016.69.8480
- [S3] **PASS** Taylor CW, Wang Z, Macaulay E, et al. Exposure of the Heart in Breast Cancer Radiation Therapy: A Systematic Review of Heart Doses Published During 2003 to 2013. *Int J Radiat Oncol Biol Phys*. 2015;93(4):845–853. DOI: 10.1016/j.ijrobp.2015.07.2292. PMID 26530753. https://doi.org/10.1016/j.ijrobp.2015.07.2292
- [S4] **PASS** Drost L, Yee C, Lam H, et al. A Systematic Review of Heart Dose in Breast Radiotherapy. *Clin Breast Cancer*. 2018;18(5):e819–e824. DOI: 10.1016/j.clbc.2018.05.010. PMID 29980429. https://doi.org/10.1016/j.clbc.2018.05.010
- [S5] **PASS（OA，PMC5548226）** Taylor C, Correa C, Duane FK, et al. Estimating the Risks of Breast Cancer Radiotherapy: Evidence From Modern Radiation Doses to the Lungs and Heart and From Previous Randomized Trials. *J Clin Oncol*. 2017;35(15):1641–1649. DOI: 10.1200/JCO.2016.72.0722. PMID 28319436. https://doi.org/10.1200/JCO.2016.72.0722
- [S5b] **PASS** Trivedi SJ 等（單機構 4,687 人 MHD 實測）Factors Affecting Mean Heart Dose in Patients Receiving Breast Radiotherapy from 2011 to 2018 in a Single Institution. *J Med Imaging Radiat Sci*. 2020;51(3):379–393. DOI: 10.1016/j.jmir.2020.03.003. PMID 32362536.（左側傳統中位 2.16 Gy、低分次 1.47 Gy；2015 後寬切線使用增加）https://doi.org/10.1016/j.jmir.2020.03.003
- [S6] **PASS（OA 全文引語核對，PMC9309321）** Lai J, Hu S, Luo Y, et al.（Bergom 團隊）Heart Sparing Radiotherapy Techniques in Breast Cancer: A Focus on Deep Inspiration Breath Hold. *Breast Cancer (Dove Med Press)*. 2022;14:175–186. DOI: 10.2147/BCTT.S282799. PMID 35899145.（「20–70%」「29%/72 無法完成 DIBH 定位」「20/112 無法耐受 ABC」「約 75% 有劑量學獲益」皆經全文核對）https://doi.org/10.2147/BCTT.S282799
- [S7] **PASS（OA，PMC13035160）** Chiang PY, Huang PJ, Hung CH, et al. Deep inspiration breath hold versus free breathing in postoperative radiotherapy strategy for patients with left-sided breast cancer treated with volumetric modulated arc therapy: A meta-analysis and systematic review. *PLoS One*. 2026;21(3):e0345614. DOI: 10.1371/journal.pone.0345614. PMID 41911243.（bc-rt-regional 引過，重新核對成立）https://doi.org/10.1371/journal.pone.0345614
- [S8] **PASS** Lu Y, Yang D, Zhang X, et al. Meta-analysis of deep inspiration breath hold (DIBH) versus free breathing (FB) in postoperative radiotherapy for left-side breast cancer. *Breast Cancer (Tokyo)*. 2020;27(2):299–307. DOI: 10.1007/s12282-019-01023-9. PMID 31707586. https://doi.org/10.1007/s12282-019-01023-9
- [S9] **PASS（OA，PMC11460020）** （右側 DIBH 統合）Clinical benefits of deep inspiration breath-hold in postoperative radiotherapy for right-sided breast cancer: a meta-analysis. *BMC Cancer*. 2024;24(1):1238. DOI: 10.1186/s12885-024-12992-2. PMID 39379827.（右側 DIBH 也降心／肝／肺劑量——右側段備用）https://doi.org/10.1186/s12885-024-12992-2
- [S10]（編號保留給統合分析集合，未單獨使用）
- [S11] **PASS（OA，PMC11732476）** Thorsen LBJ, et al.; DBCG. Internal mammary node irradiation in 4541 node-positive breast cancer patients treated with newer systemic therapies and 3D-based radiotherapy (DBCG IMN2): a prospective, nationwide, population-based cohort study. *Lancet Reg Health Eur*. 2025;49:101160. DOI: 10.1016/j.lanepe.2024.101160. PMID 39810969.（15 年心臟死亡右 0.2% vs 左 0.7%；右照內乳、左不照的設計理由）https://doi.org/10.1016/j.lanepe.2024.101160
- [S12] **PASS（OA，PMC4364808）** Smyth LM, Knight KA, Aarons YK, Wasiak J. The cardiac dose-sparing benefits of deep inspiration breath-hold in left breast irradiation: a systematic review. *J Med Radiat Sci*. 2015;62(1):66–73. DOI: 10.1002/jmrs.89. PMID 26229669.（最多降 3.4 Gy ≈ 預期增加風險降 13.6%）https://doi.org/10.1002/jmrs.89

**B2 期刊**

- [S13] **PASS（OA，PMC8534109）** Lin YC 等（台灣，108 人）Modern Rotational Radiation Techniques with Volumetric Modulated Arc Therapy or Helical Tomotherapy for Optimal Sparing of the Lung and Heart in Left-Breast Cancer Radiotherapy Plus Regional Nodal Irradiation: A Comparative Dosimetric Analysis. *Cancers (Basel)*. 2021;13(20):5043. DOI: 10.3390/cancers13205043. PMID 34680189.（VMAT MHD 3.82 vs HT 5.13 Gy；含內乳次族群 VMAT 優勢持續）https://doi.org/10.3390/cancers13205043
- [S14] **PASS（OA，PMC7497934）** Nobnop W, Phakoetsuk P, Chitapanarux I, et al. Dosimetric comparison of TomoDirect, helical tomotherapy, and volumetric modulated arc therapy for postmastectomy treatment. *J Appl Clin Med Phys*. 2020;21(9):155–162. DOI: 10.1002/acm2.12989. PMID 32715634. https://doi.org/10.1002/acm2.12989
- [S15] **PASS** Quintin K, Loap P, Fourquet A, Kirova Y. Late hepatic toxicity after breast cancer intensity-modulated radiotherapy using helicoidal tomotherapy. *Cancer Radiother*. 2023;27(4):267–272. DOI: 10.1016/j.canrad.2023.03.001. PMID 37179220.（「increases the low-dose bath to non-target volumes」原句所在）https://doi.org/10.1016/j.canrad.2023.03.001
- [S16] **PASS** Loap P, Uakkas A, Bouziane J, et al.（Institut Curie，179 人，9.1 年）Long-term cardiac outcomes in breast cancer patients treated with helical tomotherapy: Evaluating the applicability of 3D-based dose constraints for intensity modulated radiation therapy. *Int J Cancer*. 2025;157(7):1386–1394. DOI: 10.1002/ijc.35474. PMID 40405829. https://doi.org/10.1002/ijc.35474
- [S17] **PASS（OA，PMC12582959）** Xia Y, Yang YC, Ren HQ, et al. Comparison of adverse events between intensity-modulated radiation therapy and tomotherapy for early stage breast cancer: a retrospective cohort study. *Front Oncol*. 2025;15:1654609. DOI: 10.3389/fonc.2025.1654609. PMID 41195267.（TOMO G3-4 皮膚 16.2% vs 7.6%；肺炎 0% vs 4.3%；回溯、3 個月）https://doi.org/10.3389/fonc.2025.1654609
- [S18] **PASS** Cheng HW, Chang CC, Shiau AC, et al. Dosimetric comparison of helical tomotherapy, volumetric-modulated arc therapy, intensity-modulated radiotherapy, and field-in-field technique for synchronous bilateral breast cancer. *Med Dosim*. 2020;45(3):271–277. DOI: 10.1016/j.meddos.2020.01.006. PMID 32122694. https://doi.org/10.1016/j.meddos.2020.01.006
- [S19] **PASS（OA，PMC3492203）** Versmessen H, Vinh-Hung V, et al. Health-related quality of life in survivors of stage I-II breast cancer: randomized trial of post-operative conventional radiotherapy and hypofractionated tomotherapy (TomoBreast). *BMC Cancer*. 2012;12:495. DOI: 10.1186/1471-2407-12-495. PMID 23098579. https://doi.org/10.1186/1471-2407-12-495
- [S20] **PASS（OA，PMC10694354）** Vinh-Hung V, et al. Lung-heart toxicity in a randomized clinical trial of hypofractionated image guided radiation therapy for breast cancer. *Front Oncol*. 2023;13:1211544. DOI: 10.3389/fonc.2023.1211544. PMID 38053657.（TomoBreast 12 年；NCT00459628）https://doi.org/10.3389/fonc.2023.1211544
- [S21] **PASS** Orecchia R, Rojas DP, Cattani F, et al. Hypofractionated postmastectomy radiotherapy with helical tomotherapy in patients with immediate breast reconstruction: dosimetric results and acute/intermediate toxicity evaluation. *Med Oncol*. 2018;35(3):39. DOI: 10.1007/s12032-018-1095-6. PMID 29442173. https://doi.org/10.1007/s12032-018-1095-6
- [S22] **PASS（OA，PMC12304599）** Fang Y, Yu W, Qiao J, et al. Optimizing Helical Tomotherapy for Left-Sided Breast Cancer: A Retrospective Dosimetric Study of a Novel Virtual Organ-Arc Block. *Technol Cancer Res Treat*. 2025;24:15330338251363288. DOI: 10.1177/15330338251363288. PMID 40708434.（左側 PMRT＋內乳：HT+阻擋 MHD 4.79 vs 固定野 IMRT 6.39 Gy）https://doi.org/10.1177/15330338251363288

**B3 期刊與 registry**

- [S23] **PASS（沿用 nextgen/liver brief 查證，2026-08-31 再確認書目）** Newhauser WD, Zhang R. The physics of proton therapy. *Phys Med Biol*. 2015;60(8):R155–R209. DOI: 10.1088/0031-9155/60/8/R155. PMID 25803097. https://doi.org/10.1088/0031-9155/60/8/R155
- [S25] **PASS（摘要層級；全文不可取得，見 FAIL-4）** Jimenez RB, Hickey S, DePauw N, et al. Phase II Study of Proton Beam Radiation Therapy for Patients With Breast Cancer Requiring Regional Nodal Irradiation. *J Clin Oncol*. 2019;37(30):2778–2785. DOI: 10.1200/JCO.18.02366. PMID 31449469. https://doi.org/10.1200/JCO.18.02366
- [S26] **PASS（OA，PMC6797426）** Bekelman JE, Lu H, Pugh S, et al. Pragmatic randomised clinical trial of proton versus photon therapy for patients with non-metastatic breast cancer: the Radiotherapy Comparative Effectiveness (RadComp) Consortium trial protocol. *BMJ Open*. 2019;9(10):e025556. DOI: 10.1136/bmjopen-2018-025556. PMID 31619413.（bc-rt-regional 引過，重新核對成立）https://doi.org/10.1136/bmjopen-2018-025556
- [S27] **PASS（registry，2026-08-31 實查 ClinicalTrials.gov API v2）** 【機構型來源，無作者欄】ClinicalTrials.gov。NCT02603341（RADCOMP）：ACTIVE_NOT_RECRUITING、Enrollment 1,238、最後更新 2025-11-06、**主要完成日 ESTIMATED 2036-11、hasResults: false**；Europe PMC 查無主要結果論文。https://clinicaltrials.gov/study/NCT02603341
- [S28] **PASS** Mutter RW, Choi JI, Jimenez RB, et al. Proton Therapy for Breast Cancer: A Consensus Statement From the Particle Therapy Cooperative Group Breast Cancer Subcommittee. *Int J Radiat Oncol Biol Phys*. 2021;111(2):337–359. DOI: 10.1016/j.ijrobp.2021.05.110. PMID 34048815.（摘要原句：「studies have yet to demonstrate that protons improve upon the treatment outcomes achieved with photon radiation therapy」）https://doi.org/10.1016/j.ijrobp.2021.05.110
- [S29] **PASS** Hassan MZO, Awadalla M, Tan TC, et al. Serial Measurement of Global Longitudinal Strain Among Women With Breast Cancer Treated With Proton Radiation Therapy: A Prospective Trial for 70 Patients. *Int J Radiat Oncol Biol Phys*. 2023;115(2):398–406. DOI: 10.1016/j.ijrobp.2022.08.036. PMID 36028065.（全心 0.44 Gy、左心室 0.12 Gy；GLS/生物標記無變化）https://doi.org/10.1016/j.ijrobp.2022.08.036
- [S30] **PASS** Wilson F, Gupta P, Halvorsen H, et al. A Systematic Review of Deep Inspiration Breath Hold and Free Breathing in Proton Beam Therapy Plans for Breast Cancer Radiotherapy. *Clin Oncol (R Coll Radiol)*. 2025;40:103782. DOI: 10.1016/j.clon.2025.103782. PMID 39999640.（質子 MHD FB 0.48 vs DIBH 0.31 Gy；DIBH 對多數質子病人無明顯額外劑量學好處）https://doi.org/10.1016/j.clon.2025.103782
- [S31] **PASS（OA，PMC7293563）** Wang CC, McNamara AL, Shin J, et al. End-of-Range Radiobiological Effect on Rib Fractures in Patients Receiving Proton Therapy for Breast Cancer. *Int J Radiat Oncol Biol Phys*. 2020;107(3):449–454. DOI: 10.1016/j.ijrobp.2020.03.012. PMID 32240774.（前瞻試驗世代肋骨骨折 7%；射程末端 RBE 機轉）https://doi.org/10.1016/j.ijrobp.2020.03.012
- [S32] **PASS（OA，PMC10166011）** Bradley JA, Liang X, Mailhot Vega RB, et al. Incidence of Rib Fracture following Treatment with Proton Therapy for Breast Cancer. *Int J Part Ther*. 2023;9(4):269–278. DOI: 10.14338/IJPT-22-00034.1. PMID 37169006.（225 人；3 年照野內 3.7%、有症狀 0.4%）https://doi.org/10.14338/IJPT-22-00034.1
- [S33] **PASS** Sarsitthithum T, Nantavithya C, Lertbutsayanukul C, Saksornchai K. Acute skin toxicity and cosmesis outcome in non-metastatic breast cancer patients treated with ultrahypofractionated radiotherapy: a randomized controlled phase II clinical trial comparing proton versus photon radiotherapy. *J Radiat Res*. 2026;67(4):609–617. DOI: 10.1093/jrr/rrag037. PMID 42183732.（期中分析 n=72；皮膚炎 97.2% vs 75%，最高 G2；追蹤中位 9 個月——引用須標「期中、短期」）https://doi.org/10.1093/jrr/rrag037
- [S34] **PASS** Gergelis KR, Afzal A, Mullikin TC, et al. Comparative Analysis of Acute Skin Reactions After Postmastectomy Photon and Intensity Modulated Proton Therapy. *Int J Radiat Oncol Biol Phys*. 2026 (online). DOI: 10.1016/j.ijrobp.2026.05.052. PMID 42269789.（176 人；≥G2 皮膚炎 47% vs 48%；皮膚限制條件規劃）https://doi.org/10.1016/j.ijrobp.2026.05.052
- [S35] **PASS** Neibart SS, Taylor M, Depauw N, et al. Clinical Hypothyroidism After Proton Versus Photon Regional Nodal Irradiation: A Prospective Correlative Study Within the RADCOMP Randomized Trial. *Int J Radiat Oncol Biol Phys*. 2026;125(5):1338–1347. DOI: 10.1016/j.ijrobp.2026.02.199. PMID 41692352.（3 年 13%；質子 16% vs 光子 9%，p=.14；單機構子研究）https://doi.org/10.1016/j.ijrobp.2026.02.199
- [S36] **PASS（回顧文章；RADCOMP 收案完成與 QOL 之轉述僅能以此形式引，見 FAIL-5）** MacDonald SM, Kirova Y, Campbell L, et al. Proton Radiation for Locally Advanced Breast Cancer: Evolution and Techniques. *Int J Radiat Oncol Biol Phys*. 2026 (online). DOI: 10.1016/j.ijrobp.2026.08.017. PMID 42617887. https://doi.org/10.1016/j.ijrobp.2026.08.017
- [S37] **PASS（OA，PMC11538476）** Intensity-modulated proton radiotherapy spares musculoskeletal structures in regional nodal irradiation for breast cancer: a dosimetric comparison. *Acta Oncol*. 2024;63:755–762. DOI: 10.2340/1651-226X.2024.40084. PMID 39354810. https://doi.org/10.2340/1651-226X.2024.40084

**官方頁面／文件（實際抓取，取得日 2026-08-31）**

- [S38] **PASS** 【機構型來源，無作者欄】衛生福利部中央健康保險署。全民健康保險醫療服務給付項目及支付標準（開放資料，114-05-01 生效版 ODS 全表，6,013 項；經逐項下載檢索）：**36022B** 乳癌術後低分次全乳照射合併局部加強 279,986 點／**36023B** 不含加強 246,960 點（適應症原文：「早期乳癌或原位癌接受乳房腫瘤局部切除…治療範圍包含全乳房（**不包含鎖骨上淋巴結、腋下淋巴結或內乳淋巴結**）」；禁忌症含淋巴結轉移；包裹給付 20／16 次）；**36011B/36012B** 直線加速器照野碼；**36015B** 電腦治療規劃—複雜 11,483 點（明文含「強度調控放射治療」之設計）；**37026B** 放射治療之皮膚處理 244 點/週療程；**N21301–N21308** 質子治療相關項目標註「HTA項目」點數 0；全表**查無** TOMO／螺旋斷層專屬項目、查無呼吸調控／閉氣項目、查無 IMRT 專屬治療碼。資料集頁：https://data.gov.tw/dataset/9405 ；檔案：https://info.nhi.gov.tw/api/iode0000s01/Dataset?rId=A21030000I-D20003-004
- [S39] **PASS（nhi.gov.tw 直接 PDF，2026-08-31 確認 200 可下載）** 【機構型來源，無作者欄】衛生福利部中央健康保險署。健保署《癌症低分次放射治療相關診療項目之問答集及申報範例》PDF（36022B/36023B 乳癌低分次之申報說明）。https://www.nhi.gov.tw/ch/dl-42468-1634a5de2b1a4295a94838b69a98e712-1.pdf
- [S40] **PASS（沿用 liver brief S62，2026-08-31 確認連結有效）** 【機構型來源，無作者欄】行政院公報：114 年第 4 次支付標準修正公告（114-12-11 健保醫字第 1140126650 號，自 115-01-01 生效；36025B/36026B/36027B 質子三項全文，適用範圍均為「年齡未滿十九歲病人」）。https://gazette.nat.gov.tw/EG_FileManager/eguploadpub/eg031245/ch08/type1/gov70/num29/images/AA.pdf
- [S41] **PASS（2026-08-31 確認連結有效）** 【機構型來源，無作者欄】衛生福利部新聞稿（2026-01-12）：「健保115年1月起新增高血脂及兒童癌症質子治療等醫療服務」（年約 100 名兒童受惠）。https://www.mohw.gov.tw/cp-16-85076-1.html
- [S42] **PASS（機構自行公告；2026-08-31 重新抓取全文，頁面更新日 2026/03/27）** 【機構型來源，無作者欄】高雄長庚紀念醫院質子治療中心「收費標準」頁（質子諮詢診察費 1,000；模具 1,950；3D 斷層模擬 8,500；電腦治療規劃 11,483；MRI 模擬 7,500／12,500；強度調控質子每次 21,750／26,000／34,500；呼吸調控每次 5,000／9,600；腦部立體定位套組 230,234；立體定位套組 330,000；**無乳癌專屬項目**）。https://www1.cgmh.org.tw/intr/intr4/C83E10/How/How?id=14

**FAIL ／ NOT-CITABLE（保留紀錄，不得入正文引用）**

- [FAIL-1] **NCCN 指引**：nccn.org 403（依 SPEC 已知），未再嘗試。乳癌放療技術之指引措辭不引 NCCN；本 brief 以 PTCOG 共識[S28]補指引位。
- [FAIL-2] **TOMO 台灣自費／差額金額**：健保支付標準全表無 TOMO 專屬項目[S38]；查無全國性官方公告，亦查無醫院官方網頁之可引 TOMO 收費表。正文寫「各院收費不同，請向醫務課確認」；**媒體流通之 TOMO 價格（每次數千至上萬元等說法）依規格絕不可引**。
- [FAIL-3] **光子 DIBH／呼吸調控收費**：支付標準全表查無項目[S38]；查無醫院官方公告之光子呼吸調控價格（唯一官方價是高雄長庚「質子」呼吸調控[S42]，不可移作光子引用）。正文寫「請向醫務課確認」。
- [FAIL-4] **Jimenez 2019 全文**：出版社不允許全文下載（PMC author manuscript 亦被鎖）。**全文層級數字（如平均心臟劑量 0.5 Gy(RBE)、各器官 DVH、皮膚炎分級明細）不可引**；只可用摘要層級數字（5 年 LRF 1.5%、OS 91%、無 G3 肺炎、再手術 33%）。質子心臟劑量改引 [S3][S29][S30]。
- [FAIL-5] **RADCOMP 2025 生活品質分析**：僅見於回顧文章之轉述[S36]（可能為會議層級發表）；Europe PMC 查無同行評審之 QOL 主論文。引用時只能寫「2026 年回顧文章轉述兩臂生活品質同樣好」，不可寫成「RADCOMP 已發表 QOL 結果」。同理 DIBH 的「臨床心臟事件」比較：查無任何已讀出研究——正文寫「劑量降低是量得到的，事件層級的長期資料還在累積」。
- [FAIL-6] **「TOMO vs 一般 IMRT/VMAT 的隨機療效比較」**：Europe PMC 以 tomotherapy＋randomized＋breast 檢索，查無此設計之試驗；唯一隨機試驗 TomoBreast[S19][S20] 比較的是「低分次 TOMO-IGRT vs 傳統分次傳統放療」，分次混雜。正文寫法：「TOMO 與一般 IMRT 之間，沒有隨機的臨床結果比較；能比的都是劑量分布與回溯資料。」
- [FAIL-7] **N21301–N21308 之給付性質**：全表僅標「HTA項目」點數 0，未附說明文件；不可寫成「健保署公告質子不給付成人」——只能寫「支付標準中查無成人質子給付項目；質子相關 N 碼為點數 0 之 HTA 登錄項」[S38]。

---

## 給撰稿人的一句話總結

B1 的錨穩得不能再穩：Darby 逐欄核對全中（7.4%/Gy、無閾值、五年內開始、瑞典丹麥世代），還有荷蘭世代在現代劑量重現斜率（16.5%/Gy）＋Taylor 2017 把絕對風險翻成白話（不吸菸者約 0.3%）——紅線 1 的「基本款站得住」有一整串數字（現代左乳 2–4 Gy、呼吸控制 1.3–1.7 Gy、低分次中位 1.47 Gy）。DIBH 降幅寫「約 20–70%、LAD 同降、涵蓋不變」，別寫 40–50%（查無出處）；三成預選病人閉不住氣、臨床事件零直接證據，都要照實寫。B2 最大的發現是反向證據比預期硬：台灣自己的 108 人資料 VMAT 心臟劑量比 TOMO 低，「TOMO 不是全面較優」不但有源、還有台灣源；TOMO 的格是複雜標靶（內乳、重建、雙側、困難解剖），代價是低劑量浴（原句可引）。B3 照 SPEC 框架剛好：劑量學明確（含內乳 2.6 Gy vs 光子約 8 Gy 級；前瞻實測 0.44 Gy）、RADCOMP 收案完成但主要完成日估 2036-11、hasResults false（2026-08-31 實查）——未讀出就寫未讀出；肋骨 7%／3.7%、皮膚兩面資料、甲狀腺無差異，trade-off 段材料齊全。台灣端：36022B/36023B 適應症原文在手（不含區域淋巴）、TOMO 與光子 DIBH 全部查無官方價格（gap→醫務課）、質子成人全自費、唯一官方價是高雄長庚（無乳癌專屬項目）。意外收穫給 C2：37026B 放療皮膚處理健保有付。
