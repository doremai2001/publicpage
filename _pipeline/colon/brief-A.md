# A 組研究簡報 — 結腸癌專題（階段一：確診之後）

查證日期：2026-08-27。所有期刊來源均以 Europe PMC REST API（`https://www.ebi.ac.uk/europepmc/webservices/rest/search`）逐條核對卷、期、頁、年、DOI；官方文件以 WebFetch / curl 實際取得。
**本簡報只提供 A 組（A1–A4）主場的材料。** 依規格第十節，屬於 B/C/D 主場的內容（手術範圍與術式比較、第二期化療決策、IDEA 的療程長度數字、oxaliplatin 神經毒性發生率、ctDNA 的任何數字與試驗名稱、dMMR 的治療意涵、追蹤期間 CEA 與電腦斷層的排程、寡轉移與肝轉移治療、運動與飲食介入）**一律不在此簡報內**，也請 A 組不要自行補。

---

# A1 — 息肉切掉了，為什麼還要開刀

**Key facts**

- 在 67 篇研究、21,238 名 T1 大腸直腸癌病人的統合分析中，整體淋巴結轉移率為 11.2%。[S2]
- 同一份統合分析中，把深部黏膜下侵犯（deep submucosal invasion, DSI）與其他危險因子一起放進多變量模型後，DSI **不是**淋巴結轉移的獨立預測因子（8 篇研究、3,621 人，OR 1.73，95% CI 0.96–3.12）；而分化不良（OR 2.14，95% CI 1.39–3.28）、高度腫瘤出芽（OR 2.83，95% CI 2.06–3.88）、淋巴血管侵犯（OR 3.16，95% CI 1.88–5.33）都是。[S2]
- 在同一份統合分析裡，**只有**深部黏膜下侵犯、沒有其他組織學危險因子的 T1 病人（8 篇研究、1,146 人），淋巴結轉移的絕對風險是 2.6%（合併發生率 2.83，95% CI 1.66–4.78）。[S2]
- 較早的系統性回顧（17 篇研究、3,621 名有淋巴結狀態資料的 pT1 病人）算出的相對風險：淋巴管侵犯 RR 5.2（95% CI 4.0–6.8）、黏膜下侵犯 ≥1 mm RR 5.2（95% CI 1.8–15.4）、腫瘤出芽 RR 5.1（95% CI 3.6–7.3）、分化不良 RR 4.8（95% CI 3.3–6.9）。這份回顧的作者自己註明納入研究以亞洲人為主，需要在西方族群驗證。[S1]
- 腫瘤出芽的判讀方式在 2016 年才有國際共識（ITBCC 2016）：以 H&E 切片、在侵襲前緣挑一個熱點、0.785 mm² 的視野內數出芽數目，Bd1 為 0–4 個、Bd2 為 5–9 個、Bd3 為 10 個以上，並且報告要寫出絕對數字。[S3]
- 切緣的意義有數字可講：荷蘭 11 家醫院、局部切除的 T1 大腸直腸癌，在沒有淋巴血管侵犯與分化不良的前提下，切緣 0.1–1 mm 者局部殘留癌（local intramural residual cancer）為 2.9%（5/171，95% CI 1.0–6.7%），切緣 >1 mm 者為 0.6%（2/351，95% CI 0.1–2.1%）；若切緣 0.1–1 mm 且沒有 Bd2-3，殘留只出現 1 例（0.8%，95% CI 0.1–4.4%）。[S8]
- 切緣陽性或無法判讀（R1/Rx）、且沒有淋巴血管侵犯與分化不良的 434 名病人中，334 人接受追加腸段切除、100 人接受疤痕全層切除；中位追蹤 64 個月，復發率分別為 2.2%（95% CI 0.9–4.6%）與 9.0%（95% CI 3.9–17.7%），但無轉移存活（96.8% vs 92.1%，P = 0.10）與總存活（95.6% vs 94.4%，P = 0.55）沒有統計上的差別，而且 8 例疤痕切除組的復發有 5 例可以用挽救手術處理。[S7]
- 「先做內視鏡切除、發現是癌再追加手術」不會比「一開始就開刀」差：日本 27 家高量中心 6,105 名 T1 大腸直腸癌病人，傾向分數配對後兩組各 1,219 人，5 年總存活 97.1% vs 96.0%（HR 0.72，95% CI 0.49–1.08），復發 2.6% vs 2.0%（OR 1.34，95% CI 0.76–2.40，P = 0.344）。[S5]
- 對高齡病人，追加手術的淨效益會被競爭風險吃掉：2026 年的回顧指出，高風險 T1 大腸直腸癌的世代研究中，追加手術與不追加手術的 5 年癌症專一存活只差一點點，未手術組的死亡多數來自癌症以外的原因，而統合分析顯示存活優勢要到 10 年後才顯現；相對地，圍手術期併發症與短期死亡率隨年齡上升且立即發生。[S6]
- 歐洲內視鏡學會 2024 年更新版指引建議：當懷疑是表淺侵襲癌、又無法用一般息肉切除或 EMR 完整整塊切下時，應優先採用整塊切除的技術（en bloc EMR、ESD、內視鏡肌層間剝離、內視鏡全層切除或手術）。[S4]

**Claim ceiling**

Defensible：「一顆已經切下來的 pT1 癌息肉，要不要再開一次刀，取決於病理報告上的幾項特徵——淋巴血管侵犯、分化程度、腫瘤出芽、切緣，以及侵犯深度；在完全沒有這些特徵的情形下，追加手術要清掉的淋巴結轉移機率是個位數，而手術本身的代價是立刻發生的。這是一個把兩邊機率攤開來談的決定，不是一個標準答案。」

Would overstate：
- 「只要切乾淨就不用再開刀」——切緣乾淨只排除局部殘留，不處理淋巴結轉移。[S8]
- 「侵犯太深就一定要開刀」——最新的統合分析明確指出深部侵犯單獨存在時不是獨立危險因子。[S2]
- 「追加手術可以把復發風險降到零」——沒有任何一份資料支持這句。
- 「內視鏡切完再開刀會比較差 / 會擴散」——[S5] 反駁了這個常見的擔心，但它是日本高量中心的觀察性資料，也不能反過來寫成「一定不會比較差」。

**Caveats / safety notes**

- 這篇最危險的誤讀是「我的息肉切掉了，所以我沒事」。必須寫清楚：pT1 的意思是癌細胞已經穿過黏膜肌層進到黏膜下層，這已經是侵襲癌，不是原位癌。[S12]
- 第二個危險誤讀是「醫師叫我開刀是因為沒切乾淨」。要說明追加手術主要處理的是看不見的淋巴結，不是切緣。
- 不要把「多數追加手術找不到殘留腫瘤」寫成「所以追加手術是多餘的」。要同時寫出這件事的另一面：正因為事前無法確定是哪一部分人有淋巴結轉移，所以才會有一部分人白開了一刀，這是這個決定的本質，不是誰的疏失。
- 高齡與共病的病人，追加手術的取捨不一樣。[S6] 這一段不可以寫成「年紀大就不用開」，要寫成「年紀與共病會改變這個計算，這是要跟醫師談的變數」。
- **手術範圍、腹腔鏡與開腹的比較屬 B1 主場**，A1 只寫「要不要追加」，不比較術式。
- 直腸癌的局部切除邏輯與結腸癌不同，本專題不處理；碰到時一句話帶過。

**Taiwan status**

- 內視鏡切除（息肉切除術、EMR）與腸段切除的健保給付項目確實存在於「全民健康保險醫療服務給付項目及支付標準」，但**我沒有逐項核對到與惡性息肉追加手術直接對應的條文**，因此這一項寫成 gap：文章要寫「追加手術的住院、術式與自費項目（例如止血夾、能量器械）要跟你的個管師或醫院醫務課確認」。
- ESD 在台灣部分情境為自費，**我查不到可以引用的正式給付條文**，一律不要提費用。

---

# A2 — 報告上的 T3N1 是怎麼算出來的

**Key facts**

- **版本問題（2026 年的答案）**：UICC 的 TNM 第 9 版已於 2025 年 7 月 3 日發行，UICC 建議自 2026 年 1 月 1 日起適用；但官方公告列出的改版部位是鼻咽、HPV 相關口咽、肺、胸腺、間皮瘤、闌尾、肛管、子宮頸、外陰與攝護腺，**大腸與直腸不在改版之列**。[S14][S13]
- AJCC 方面，Version 9 是逐個部位分批發行的：2024 年發行的是神經內分泌腫瘤（含結腸與直腸 NET）與外陰，2023 年是闌尾、肛門、腦與脊髓，2025 年是肺、胸腺、間皮瘤、鼻咽，2026 年是唾液腺與 HPV 相關口咽；官方頁面寫明「第 8 版的所有部位在被 Version 9 取代前仍然現行」。**結腸與直腸的腺癌尚未改版。**[S15]
- 直接證據：美國病理學會（CAP）「結腸與／或直腸原發癌切除檢體」報告範本 4.4.0.1 版（2025 年 9 月張貼、2026 年 3 月起為認證必用版本）在文件開頭寫「Standard(s): AJCC 8」，pTNM 欄位標題也寫「pTNM CLASSIFICATION (AJCC 8th Edition)」。[S12]
- 文獻上確實有人在驗證「AJCC 第 9 版結腸癌分期」的提案（北京協和 1,222 例，79.9% 的病人期別會改變，58.4% 上升、21.4% 下降），腫瘤沉積（tumor deposits）的定義也已由 AJCC/UICC 專家以 Delphi 共識重寫；但這些是**改版過程**，不是現行報告使用的版本。[S17][S16]
- **T 的定義（AJCC 第 8 版）**：pTis 為原位癌／黏膜內癌（侵犯固有層但未穿過黏膜肌層）；pT1 侵犯黏膜下層（穿過黏膜肌層但未進入固有肌層）；pT2 侵犯固有肌層；pT3 穿過固有肌層進入結腸直腸周圍組織；pT4a 穿透臟層腹膜；pT4b 直接侵犯或沾黏到鄰近器官或構造。[S12]
- **N 的定義**：pN0 無區域淋巴結轉移；pN1a 一顆陽性、pN1b 二至三顆陽性、pN1c 淋巴結都沒有但在漿膜下／腸繫膜／非腹膜化的結腸直腸周圍組織有腫瘤沉積；pN2a 四至六顆、pN2b 七顆以上。轉移的定義是淋巴結內腫瘤 ≥0.2 mm。[S12]
- **M 的定義**：pM1a 單一部位或器官轉移且無腹膜轉移；pM1b 兩個以上部位或器官且無腹膜轉移；pM1c 腹膜表面轉移（單獨或合併其他）。[S12]
- **期別怎麼組出來（AJCC 第 8 版，美國國家癌症研究所 PDQ 版本）**：IIA = T3 N0 M0；IIB = T4a N0 M0；IIC = T4b N0 M0；IIIA = T1–2 N1/N1c M0 或 T1 N2a M0；IIIB = T1–2 N2b M0、T2–3 N2a M0、或 T3–T4a N1/N1c M0；IIIC = T3–T4a N2b M0、T4a N2a M0、或 T4b N1–N2 M0。**因此 T3N1M0 是第 IIIB 期。**[S20]
- **≥12 顆淋巴結為什麼是品質指標**：CAP 報告範本直接寫「美國國家品質論壇（National Quality Forum）把手術檢體中至少 12 顆淋巴結列為美國結腸癌照護的關鍵品質指標之一」，並寫「偵測到轉移的機率隨檢查的淋巴結數目增加，因此 12 顆應視為最低目標，但應盡可能取出並檢查所有淋巴結」。[S12]
- 這個數字的原始證據來自 INT-0089 試驗的次級分析（3,411 名第 II、III 期結腸癌病人，中位追蹤 8.4 年）：檢出淋巴結數目愈多，存活愈好，而且這個關聯在 N0、N1、N2 各組內都成立。[S10]
- 但把「數目」當成醫院品質指標的作法，2025 年被兩個大型資料庫的分析質疑：英格蘭 CORECT-R（n = 84,116，2010–2020）與美國 SEER（n = 287,974，2000–2020）顯示，淋巴結陽性率在檢出 9 顆之後就不再有臨床意義的增加，但存活在 9 顆之後仍持續改善（每多一顆，總死亡風險降低約 1%）；作者發現英格蘭有十家醫院的檢出數高於或低於預期，卻**對總存活沒有影響**，因而主張淋巴結檢出數目應被當成腫瘤生物學與預後的替代指標，而不是醫院的品質指標。[S11]
- **CEA 能告訴你什麼**：SEER 中 2004 年確診、有 CEA 資料的 9,083 名結腸腺癌病人，術前 CEA 升高（C1）與總死亡風險增加 60% 獨立相關（HR 1.60，95% CI 1.46–1.76，P < .001）；而且 CEA 升高的低期別病人存活比 CEA 正常的高期別病人更差（例如第 I 期 C1 差於第 IIA 期 C0 與第 IIIA 期 C0，P < .001）。[S18]
- **CEA 不能告訴你什麼**：CEA 會被抽菸拉高。韓國 750 名成年男性的橫斷面研究（各 250 名紙菸使用者、加熱菸使用者、戒菸者）中，CEA 中位數分別為 2.4、2.0、1.6，紙菸使用者顯著高於另外兩組。[S19]

**Claim ceiling**

Defensible：「T 講的是腫瘤往腸壁裡鑽了多深，N 講的是拿掉的淋巴結裡有幾顆有癌細胞，兩個合起來才是期別。你手上這份報告用的是 AJCC 第 8 版；第 9 版正在改，但結腸腺癌還沒輪到。至少 12 顆淋巴結是一個被寫進病理報告範本的最低目標，理由是拿得愈少，把有轉移的病人誤判成沒轉移的機會愈高。CEA 是一個預後指標，不是一個診斷或安心的指標。」

Would overstate：
- 「2026 年起結腸癌改用第 9 版 TNM」——**錯**。[S12][S15]
- 「拿不到 12 顆就是手術做得不好」——[S11] 明確反對這個推論。
- 「CEA 正常代表沒事」「CEA 正常代表期別低」——[S18] 的資料只支持「CEA 高比較差」，不支持反面。這也是規格固定紅線 C。
- 「淋巴結拿愈多存活愈好，所以要求醫師多拿」——這是關聯，不是因果，而且 [S11] 顯示醫院層級的檢出數高低與存活無關。

**Caveats / safety notes**

- 期別的說明最容易被讀成宣判。要寫清楚期別是描述「現在知道多少」，不是「還剩多久」。
- **不可暗示 CEA 正常就沒事**（固定紅線 C）。抽菸者、良性肝病與其他狀況都會讓 CEA 偏高，而相當一部分結腸癌病人 CEA 是正常的。[S19]
- **CEA 在追蹤期間的排程與判讀屬 D1 主場**，A2 只建立「意義與限制」，不寫追蹤要多久驗一次、也不寫追蹤期間 CEA 上升該怎麼辦。
- **手術端怎麼做才拿得到足夠的淋巴結屬 B1；數目不足會如何影響第二期的判斷屬 B2。** A2 只解釋名詞與品質指標本身的意義，不給臨床決策建議。
- 腫瘤沉積（tumor deposits）的定義本身仍在改，這件事要誠實寫出來：目前的判定「相當依賴病理醫師的裁量」。[S16]
- 病理報告上「哪幾行會改變處置」可以寫，但每一行的下游決策要指向對應的篇章，不要在 A2 展開。

**Taiwan status**

- 台灣的病理報告普遍採用 AJCC/UICC 的 TNM，**我沒有找到衛福部或健保署對「結腸癌病理報告必須採用哪一版 TNM」的正式規範文件**，因此這一項寫成 gap：文章只寫「你手上的報告寫的是第幾版，報告本身通常會註明；不確定就問」。
- 淋巴結檢出數目在台灣是否為癌症診療品質認證的指標之一，**國民健康署網站（www.hpa.gov.tw）在本次查證的環境下 TLS 憑證驗證失敗，curl 與 WebFetch 都無法取得**（見 [S49] FAIL），因此寫成 gap。
- CEA 檢驗的健保給付條件**我沒有核對到正式支付標準條文**，寫成 gap。

---

# A3 — 確診之後的第一個月會發生什麼

**Key facts**

- **全大腸評估為什麼要做完**：荷蘭鹿特丹癌症登記 1995–2006 年的 13,683 名大腸直腸癌病人中，534 人（3.9%）有同時性（synchronous）大腸直腸癌，也就是每 25 個人有 1 個；其中 34%（184/534）的兩顆腫瘤位在不同的手術切除節段。作者的結論就是：這強調了在手術前完成全大腸檢查的重要性。[S21]
- 男性（OR 1.54，95% CI 1.29–1.84）與 70 歲以上（OR 1.83，95% CI 1.39–2.40）的同時性癌風險較高；同時性癌病人出現遠端轉移的機率也較高（OR 1.69，95% CI 1.27–2.26）。[S21]
- **鏡子過不去怎麼辦**：統合分析比較「有做電腦斷層大腸攝影（CT colonography）」與「沒做」的研究，同時性大腸直腸癌的合併盛行率分別為 5.7%（95% CI 4.7–7.1%，21 篇、1,673 人）與 3.9%（95% CI 3.3–4.4%，27 篇、111,873 人），差異顯著（P = 0.004）——也就是說，不做完整評估會漏掉一部分。[S22]
- **PET 什麼時候不該做**：加拿大安大略 9 家醫院、21 位外科醫師的隨機試驗，收 2005–2013 年、影像判定可切除的大腸直腸癌肝轉移病人，術前加做 PET-CT 的 263 人中只有 21 人（8.0%，95% CI 5.0–11.9%）改變了手術計畫；兩組的存活沒有差別（HR 0.86，95% CI 0.60–1.21，P = .38）。作者的結論是這些發現「對 PET-CT 在這個情境的價值提出質疑」。[S23]
- **多專科團隊（MDT）的證據品質要誠實講**：這一題沒有隨機試驗。英格蘭單一高量中心 2003–2016 年共 4,617 名經 MDT 討論的大腸直腸癌病人，比較三個時期後，急診切除從 15.5% 降到 9.0%（P < 0.0001）、90 天死亡率從 14.8% 降到 10.7%（P < 0.001）、2 年存活從 58.6% 升到 65%（P < 0.001）；80 歲以上者的擇期切除後 90 天死亡率從 10.0%（18/180）降到 3.3%（5/151，P = 0.013）。這是同一機構跨時期的比較，不能歸因於 MDT 單一因素。[S24]
- 義大利北部（Reggio Emilia）以人口為基礎的第 I–III 期大腸直腸癌研究，比較有無 MDT 管理的存活與復發，是另一份支持性的觀察資料。[S25]
- **手術時程**：美國 National Cancer Data Base 1998–2012 年 514,103 名非轉移性結腸癌病人，以「確診到手術 7–30 天」為對照，31–60 天（HR 1.13）、61–90 天（HR 1.49）、91–120 天（HR 2.28）、121–180 天（HR 2.46）死亡風險上升；**但小於 7 天者也上升（HR 1.56）**。這是觀察性資料，太快與太慢各自帶著不同的混擾因素（太快的多半是急症）。[S26]
- 35.4% 的病人在 7 天內開刀、45% 在 7–30 天、15.1% 在 31–60 天。[S26]

**Claim ceiling**

Defensible：「確診後的第一個月，你會被排一連串檢查：胸腹骨盆電腦斷層、把大腸鏡沒看完的部分補完、抽血。這些不是拖延，是因為期別會決定治療的順序，而不做完全大腸評估，每 25 個人裡會有 1 個漏掉第二顆腫瘤。PET 不是每個人都需要，而且在台灣它的給付條件寫得很清楚：要先用電腦斷層或核磁共振做過，而且要在病歷上寫明為什麼還需要它。」

Would overstate：
- 「多專科團隊會議可以提高存活」——只有觀察性與跨時期比較資料，寫成「和比較好的結果有關」而不是「會提高」。[S24]
- 「等愈久愈危險，所以要催醫院快點開」——[S26] 的資料同時顯示 7 天內開刀的死亡風險也較高，這是一份無法區分因果的觀察性資料。這一段要寫得非常克制。
- 「PET 沒有用」——[S23] 是限定在「影像判定可切除的肝轉移、術前」這個情境，不能外推到所有情境。

**Caveats / safety notes**

- 這篇最容易被讀成「檢查愈多愈安心」，進而去自費做 PET 或全身健檢式的影像。健保署的衛教文件自己寫：民眾以正子造影來篩檢癌症必須自費，而且「正子造影並非對所有癌症診斷率都很高」，一次檢查的游離輻射劑量約 6–10 毫西弗，相當於 100–160 張胸部 X 光。[S31]
- 也不要寫成「檢查排得慢沒關係」。要給讀者一個可以問出口的問題：「我的手術／治療預計什麼時候開始？如果排不進去，有沒有其他安排？」
- 重大傷病證明的段落不要寫成「申請了就會過」或「申請了就免費」。免自行負擔的範圍是有條文界線的（見下）。
- **暫時性造口屬 C3、術式比較屬 B1**，A3 一律不展開。

**Taiwan status**

- **重大傷病證明的法源與流程（已查到正式條文）**：依《全民健康保險保險對象免自行負擔費用辦法》（修正日期：民國 113 年 09 月 16 日；全國法規資料庫法規整編資料截止日 115 年 08 月 21 日）第 2 條，重大傷病項目及證明有效期限規定於附表一；保險對象經特約醫院、診所醫師診斷為重大傷病者，得檢具申請書、診斷證明書（診斷病名欄應加填國際疾病分類碼）及病歷摘要或檢查報告等佐證資料、身分證明文件影本，**由本人或委託他人、醫院、診所為代理人**向保險人申請。診斷證明書自開立日起 **30 日內有效，逾期不予受理**。[S27]
- 第 3 條：保險人應自收受申請文件之日起 **14 日內（不包括例假日）** 核定並通知申請人或代理人；需補件者，補件時間得予扣除。重大傷病證明註記於健保卡。[S27]
- 第 5 條：重大傷病證明**以提出申請之日為生效日**；有效期間為二年以上者，得於效期屆滿三個月前重新申請，於期限內重新申請並經核定者效期得予銜接。[S27]
- 第 6 條：免自行負擔費用的範圍為——(1) 重大傷病證明所載傷病，或經診治醫師認定與該傷病相關之治療；(2) 因重大傷病門診，當次由同一醫師併行其他治療；(3) 因重大傷病住院須併行他科治療；住院期間申請獲准者，當次住院自第一日起免自行負擔。[S27][S30]
- **結腸癌的重大傷病有效期限是 5 年**：依附表一（114 年 1 月 1 日以後適用版本），「一、需積極或長期治療之癌症」項下，甲狀腺惡性腫瘤、口腔／口咽／下咽第一期、乳房第一期、子宮頸第一期為三年，「(五) 除(一)–(四)之其他惡性腫瘤」（ICD-10-CM C00.0–C96.9，不含 C73、C94.4、C94.6）為 **五年**。結腸惡性腫瘤（C18）屬於這一類。[S28]
- 申請可由院所線上或造冊送件，也可郵寄、親送或向健保署分區業務組提出。[S29]
- **PET（正子造影）的健保給付條件（已查到正式支付標準條文）**：支付標準項目 26072B「正子造影－全身」支付 36,500 點、26073B「正子造影－局部」支付 26,500 點。腫瘤適應症明列「大腸癌、直腸癌…之分期及懷疑復發或再分期」，但附有規範：「以上各階段須符合：經電腦斷層、核磁共振、核子醫學掃瞄等檢查仍無法分期者，或認定電腦斷層、核磁共振等檢查不足以提供足夠資訊以供治療所需者，且須於病歷中說明施行正子造影之必要性理由」，並且「配合腫瘤治療計畫者方得以正子造影作為療效評估項目，未有後續積極處置之計畫者，不得施行」；「懷疑復發或再分期」不得用於例行之追蹤檢查。[S30]（點數不等於金額，每點金額依總額支付制度結算點值計算。[S31]）
- **gap — 電腦斷層與核磁共振的給付條件**：我在「全民健康保險醫療服務給付項目及支付標準」的品項檔中沒有核對到與結腸癌分期直接對應的 CT／MRI 條文。文章要寫「分期用的電腦斷層與核磁共振的給付條件與是否需事前審查，要跟你的個管師或醫院醫務課確認」，**不得宣稱有給付或沒給付**。
- **gap — 台灣的排程節奏**：我查不到衛福部或健保署對「確診到手術」等候時間的官方統計或標準。文章只能寫成「這個時間各院差很多，你可以直接問你的個管師」，不可以給天數。
- **gap — 多專科團隊會議在台灣的制度位置**：國民健康署的「癌症診療品質認證」相關頁面在本次環境下無法取得（[S49] FAIL）。健保署 NGS 支付標準條文中確實出現「主管機關公告通過『癌症診療品質認證醫院』」與「分子腫瘤委員會（MTB）」作為資格條件 [S43]，可以據此說明這個制度存在，但**不得**據此描述 MDT 會議的運作細節或涵蓋率。

---

# A4 — 基因報告決定的不只是治療

**Key facts**

- **為什麼是「每一個人都驗」**：4 個大型世代、10,206 名新診斷大腸直腸癌先證者的合併分析中，312 人（3.1%）帶有 MMR 基因致病變異（Lynch 症候群）。以人口為基礎的次族群（n = 3,671）比較各種篩選策略：全面腫瘤 MMR 檢測（universal screening）的敏感度 100%（95% CI 99.3–100%）、特異度 93.0%、診斷率 2.2%；Bethesda 準則敏感度 87.8%（95% CI 78.9–93.2%）；Jerusalem 建議 85.4%；「70 歲以下全驗 + 70 歲以上符合 Bethesda 才驗」的選擇性策略敏感度 95.1%，會漏掉 4.9% 的 Lynch 病人，但可少做 34.8% 的腫瘤檢測。[S32]
- 更早的俄亥俄州 1,066 名新診斷大腸腺癌病人中，208 人（19.5%）有微衛星不穩定，其中 23 人（2.2%）帶有致病的 MMR 生殖系變異；這 23 人裡有 10 人年齡超過 50 歲、5 人不符合 Amsterdam 準則或 Bethesda 指引。單用 MSI 基因型分析與單用免疫組織化學染色，**各自都漏掉 2 名**先證者。[S33]
- **家族的部分才是重點**：在 [S33] 的 21 個先證者家族中，117 名有風險的親屬接受檢測，其中 **52 人帶有 Lynch 變異、65 人沒有**——也就是說，找出一個病人，平均會找出兩個以上原本不知情的帶因親屬。[S33]
- **轉移性的盛行率完全不同**：CAIRO、CAIRO2、COIN、FOCUS 四個第三期試驗合併 3,063 名轉移性大腸直腸癌病人的原發腫瘤，dMMR 只有 153 人（5.0%），BRAF 突變 250 人（8.2%）；dMMR 腫瘤中 BRAF 突變佔 34.6%（53/153），pMMR 中只佔 6.8%（197/2,910，P < 0.001）。[S34]
- 在同一份合併分析中，dMMR 與較差的預後相關（PFS HR 1.33，95% CI 1.12–1.57；OS HR 1.35，95% CI 1.13–1.61），BRAF 突變也是（PFS HR 1.34，95% CI 1.17–1.54；OS HR 1.91，95% CI 1.66–2.19）；作者的結論是 dMMR 的不良預後主要是由 BRAF 突變帶動的。[S34]
- **RAS 的盛行率**：12 個真實世界資料來源、4,431 個做過 RAS 檢測的腫瘤檢體，合併 RAS 突變盛行率 43.6%（95% CI 38.8–48.5%），各來源之間從 33.7% 到 54.1% 不等，作者自己說原因不明。[S35]
- KRAS、NRAS、BRAF 突變在統合分析中都與較差的總存活相關（9 個研究、3,096 人，合併 HR 均 > 1，P < .05），其中 BRAF 的影響最大；但作者也註明漏斗圖有輕度不對稱、可能有發表偏誤。[S36]
- **Lynch 症候群親屬的篩檢建議（EHTG／ESCP 第三版 Mallorca 指引，2021）**：大腸鏡監測建議 **path_MLH1 與 path_MSH2 帶因者自 25 歲開始、path_MSH6 與 path_PMS2 帶因者自 35 歲開始**；監測間隔為 **path_MLH1、path_MSH2、path_MSH6 每 2 或 3 年一次**（若曾罹患大腸直腸癌則改為每 2 年），path_PMS2 帶因者可考慮每 5 年一次；監測起始年齡與間隔**不因性別而異**。[S37]
- 為什麼不是「愈密愈好」：比較德國（每年）、荷蘭（1–2 年）、芬蘭（2–3 年）三國、2,747 名 Lynch 病人、16,327 次大腸鏡、23,309 人年的資料，**三國之間的累積大腸直腸癌發生率與診斷時的期別沒有顯著差異**；10 年累積發生率依風險族群從 4.1% 到 18.4% 不等，受年齡、性別、基因與先前病灶影響。[S38]
- 各學會的建議並不一致：2025 年比較各國指引的回顧指出，多數指引建議大腸鏡間隔 1–2 年，但**開始年齡的建議互相矛盾**（依 MLH1/MSH2 或 MSH6/PMS2 而不同），在大腸直腸癌病人該做局部或擴大切除上也有明顯分歧。[S39]
- 歐洲腫瘤內科學會（ESMO）的遺傳性消化道癌症指引是另一份可引用的正式文件。[S40]
- **台灣的資料**：台灣精準醫療計畫（TPMI）一家醫學中心 42,828 名參與者中，89 人帶有致病的 MMR 變異（MLH1 22 人 25%、MSH2 47 人 53%、MSH6 20 人 22%），盛行率約 **481 分之 1**；帶因者的累積癌症發生率 MLH1 40.9%、MSH2 29.8%、MSH6 40%。作者直接指出台灣的 Lynch 症候群明顯診斷不足。[S41]

**Claim ceiling**

Defensible：「MMR／MSI 這一項檢驗，不是只為了決定你的治療。它同時是找出 Lynch 症候群的入口，而 Lynch 症候群一旦確定，改變的是你兄弟姊妹、子女、父母要從幾歲開始、多久做一次大腸鏡——那個時程和一般人的糞便潛血篩檢不是同一回事。這是這份報告上最容易被忽略、但影響最多人的一行。」

Would overstate：
- 「基因報告正常就代表家人不用擔心」——MSI 與 IHC 各自都會漏掉少數 Lynch 病人。[S33]
- 「有 Lynch 就一定會得癌症」——[S41] 的累積發生率是 30–41%，不是 100%。
- 「大腸鏡做愈密愈安全」——[S38] 明確顯示三國不同間隔的結果沒有顯著差異。
- 「RAS／BRAF 有突變就代表預後很差、治不好」——這些是族群層級的風險比，不是個人的命運；而且 **BRAF/RAS 的治療意涵屬 B4 與 D3，A4 不寫**。
- 「MSI-H 代表免疫治療有效」——**這是 B4 的主場與紅線 2**。A4 只寫「這項檢驗會不會影響治療，屬於另一篇」，不給任何療效敘述。

**Caveats / safety notes**

- 這篇最危險的誤讀是「基因報告 = 遺傳」。要說清楚：腫瘤上的 KRAS／NRAS／BRAF 是**腫瘤細胞後天發生的**變異，不會遺傳給小孩；只有生殖系（germline）的 MMR 變異才是會遺傳的 Lynch 症候群。這兩件事在同一份報告上經常並列，病人分不清。
- 家族篩檢是**固定紅線 B** 的三件時效性事項之一，必須寫出具體的起始年齡與間隔，不可以寫成「建議家人也去檢查」。
- 建議家屬去做的是**大腸鏡監測**，不是糞便潛血。要明確寫出這個差別，否則讀者會把家人送去做公費 FIT 就以為做完了。
- 遺傳諮詢與生殖系檢測要經過知情同意，也牽涉保險與家族關係。文章不要把「去驗」寫成理所當然的下一步，要寫成「這是一個可以在門診提出、由遺傳諮詢人員說明後再決定的選項」。
- **台灣糞便潛血篩檢政策由 A4 寫完整；D1 只寫「已確診病人的大腸鏡追蹤不等於一般人的篩檢」。**

**Taiwan status**

- **糞便潛血篩檢政策（已查到官方文件）**：衛生福利部官網頁面（建檔／更新日期 114 年 1 月 16 日，政策自 114 年 1 月 1 日起生效）載明大腸癌篩檢補助對象「擴大至 **45 至 74 歲**民眾及 **40 至 44 歲有家族病史者（父母、子女或兄弟姊妹經診斷為大腸癌者）**」，提供「**每 2 年 1 次免費糞便潛血檢查**」。[S42]
- 衛生福利部 114 年 5 月 15 日的另一則官網內容重述同一組數字：「建議 40 歲至 44 歲具大腸癌家族史的民眾與 45 歲至 74 歲民眾，每 2 年 1 次接受糞便潛血檢查。」[S43]
- 115 年（2026）起國民健康署另有擴大癌症篩檢（新增胃癌篩檢等），但我核對到的官方頁面**未顯示大腸癌篩檢的年齡帶或間隔有再變動**。國民健康署網站本身無法取得（[S49] FAIL），所以文章寫「以國民健康署公告為準」，並附上衛福部頁面連結。
- **台灣 FIT 篩檢的效果（同儕審查證據）**：台灣百萬人篩檢計畫 2004–2009 年、約 500 萬人追蹤的世代研究中，1,160,895 名 50–69 歲民眾參加雙年一次的全國篩檢；受篩者相對未受篩者的大腸直腸癌死亡率下降 62%（RR 0.38，95% CI 0.35–0.42，最長追蹤 6 年）；校正自我選擇偏差後，21.4% 的涵蓋率帶來全人口 10% 的死亡率下降（RR 0.90，95% CI 0.84–0.95）。[S44]
- **FIT 不是萬無一失**：台灣篩檢計畫 2004–2012 年的資料中，15,386 例大腸直腸癌裡有 4,018 例（26.2%）是間隔癌，其中 2,782 例（18.1%）發生在 FIT 陰性之後、1,236 例（8.1%）發生在 FIT 陽性後大腸鏡未診斷出癌之後；後者的發生率（每千人年 0.75 vs 0.09）與死亡率（0.12 vs 0.02）都高得多（AHR 分別為 7.06 與 5.04）。醫院層級的腺瘤偵測率愈高，大腸鏡後間隔癌愈少（高 vs 低 ADR，AHR 0.26，95% CI 0.20–0.36）。[S45]
- **RAS／BRAF 檢驗的健保給付（已查到正式支付標準條文，項目自 113 年 12 月 1 日生效）**：
  - 30104B「All-RAS 及 BRAF 基因突變分析實驗室開發檢測（LDTs）」11,878 點、30106B 同名之 IVD 版本 11,878 點。**適應症限「符合藥品給付規定第九節 9.27 Cetuximab 及 9.53 Panitumumab 之轉移性直腸結腸癌病人」**；檢測應包含 KRAS（exon 2、3、4）、NRAS（exon 2、3、4）與 BRAF V600E；限用藥前之伴隨式檢測，**每人終生限給付一次**。[S46]
  - 30107B「BRAF 基因突變分析（LDTs）」3,006 點，用於轉移性結直腸癌時限「KRAS 及 NRAS 為 wild type 者」；同樣限用藥前伴隨式檢測、每人每癌別終生一次。[S46]
  - **這代表：健保給付的 RAS/BRAF 檢測綁在轉移性病人的標靶藥物適應症上，不是給所有結腸癌病人在確診時做的。** 文章要照這個界線寫，不可以寫成「確診就會驗」。
- **gap — MMR／MSI 檢驗的給付**：我在支付標準品項檔中**找不到任何 MMR 或 MSI 專屬的項目代碼**（關鍵字「微衛星」「錯配修復」「MSI」「MLH1」「MSH2」皆為 0 筆）。免疫組織化學染色只有通用項目 25012B「免疫組織化學染色（每一抗體）」1,354 點，註明每例以申報五種抗體為限（淋巴瘤、雙側乳癌、不明原發、骨與軟組織腫瘤才放寬到十種），條文中沒有提到 MMR 或大腸癌。因此**是否給付、以什麼名目給付，本簡報無法確認**：文章一律寫「MMR／MSI 檢驗的給付條件要跟你的個管師或醫院醫務課確認」，**不得宣稱有給付或沒給付**。
- **NGS 的部分**：健保自 113 年 5 月 1 日起給付實體腫瘤／血癌次世代基因定序（30301B BRCA1/2 定額 10,000 點、30302B 小套組 ≦100 基因 20,000 點、30303B 大套組 >100 基因 30,000 點；每人每癌別限擇一申報且終生一次；醫院須為區域級以上或通過「癌症診療品質認證」，並須設立或聯合組成分子腫瘤委員會 MTB）。[S46][S47]
- 但**大腸直腸癌不在 NGS 給付的癌別內**：健保署「次世代基因定序（NGS）支付標準問答輯」（113.08.05 第二版）明載，7 大類癌症（**大腸直腸癌**、泌尿道上皮癌、黑色素瘤、胃癌、B 細胞淋巴癌及 T 或 NK 細胞血癌與淋巴癌）「專家共識建議採『單基因檢測』，相關醫學會已陸續提出新增修訂診療項目之申請，本署將依程序研議」。[S48]
- **時效性提醒**：[S48] 是 113 年（2024）8 月的文件，2025–2026 年可能已有異動；文章寫的時候要標明「以健保署公告為準」，或直接寫成要確認。
- **gap — 生殖系（germline）基因檢測與遺傳諮詢的給付**：我查不到正式條文，寫成 gap。

---

# Sources

## 期刊來源（全部經 Europe PMC REST API 核對）

- **[S1] PASS** — Bosch SL, Teerenstra S, de Wilt JH, Cunningham C, Nagtegaal ID (2013). *Predicting lymph node metastasis in pT1 colorectal cancer: a systematic review of risk factors providing rationale for therapy decisions*. Endoscopy, 45(10), 827–834. PMID 23884793, doi 10.1055/s-0033-1344238 — 建立四項組織學高風險特徵與淋巴結轉移的相對風險。Route: Europe PMC REST（TITLE 檢索 → EXT_ID 核對）。連結：https://doi.org/10.1055/s-0033-1344238

- **[S2] PASS** — Zwager LW, Bastiaansen BAJ, Montazeri NSM, et al. (2022). *Deep Submucosal Invasion Is Not an Independent Risk Factor for Lymph Node Metastasis in T1 Colorectal Cancer: A Meta-Analysis*. Gastroenterology, 163(1), 174–189. PMID 35436498, doi 10.1053/j.gastro.2022.04.010 — 提供 T1 整體淋巴結轉移率 11.2%、單獨深部侵犯的絕對風險 2.6%，並推翻「侵犯深度可單獨決定要不要開刀」。Route: Europe PMC REST（TITLE 檢索）。連結：https://doi.org/10.1053/j.gastro.2022.04.010

- **[S3] PASS** — Lugli A, Kirsch R, Ajioka Y, et al. (2017). *Recommendations for reporting tumor budding in colorectal cancer based on the International Tumor Budding Consensus Conference (ITBCC) 2016*. Modern Pathology, 30(9), 1299–1311. PMID 28548122, doi 10.1038/modpathol.2017.46 — 腫瘤出芽的判讀方法與 Bd1/2/3 分級的來源。Route: Europe PMC REST（TITLE 檢索）。連結：https://doi.org/10.1038/modpathol.2017.46

- **[S4] PASS** — Ferlitsch M, Hassan C, Bisschops R, et al. (2024). *Colorectal polypectomy and endoscopic mucosal resection: European Society of Gastrointestinal Endoscopy (ESGE) Guideline – Update 2024*. Endoscopy, 56(7), 516–545. PMID 38670139, doi 10.1055/a-2304-3219 — 懷疑表淺侵襲癌時應採整塊切除技術的正式建議。Route: Europe PMC REST（TITLE 檢索）。連結：https://doi.org/10.1055/a-2304-3219

- **[S5] PASS** — Tamaru Y, Kuwai T, Kajiwara Y, et al. (2024). *Long-Term Outcomes of Additional Surgery After Endoscopic Resection Versus Primary Surgery for T1 Colorectal Cancer*. The American Journal of Gastroenterology, 119(12), 2418–2425. PMID 38864517, PMCID PMC11608620（open access）, doi 10.14309/ajg.0000000000002879 — 6,105 人、傾向分數配對，先內視鏡切除再追加手術不劣於一開始就手術。Route: Europe PMC REST（TITLE 檢索）。連結：https://doi.org/10.14309/ajg.0000000000002879

- **[S6] PASS** — Ichimasa K, Kudo SE, Kouyama Y, et al. (2026). *Competing Mortality Redefines the Net Benefit of Additional Surgery After Endoscopic Resection for T1 Colorectal Cancer in Older Adults*. Digestive Endoscopy, 38(7), e70222. PMID 42400343, doi 10.1111/den.70222 — 高齡病人追加手術的延遲效益 vs 立即風險。Route: Europe PMC REST（TITLE 檢索）。連結：https://doi.org/10.1111/den.70222

- **[S7] PASS** — Gijsbers KM, Laclé MM, Elias SG, et al. (2022). *Full-Thickness Scar Resection After R1/Rx Excised T1 Colorectal Cancers as an Alternative to Completion Surgery*. The American Journal of Gastroenterology, 117(4), 647–653. PMID 35029166, doi 10.14309/ajg.0000000000001621 — 434 人，追加腸段切除 vs 疤痕全層切除的復發、無轉移存活與總存活比較。Route: Europe PMC REST（TITLE 檢索）。連結：https://doi.org/10.14309/ajg.0000000000001621

- **[S8] PASS** — Gijsbers KM, van der Schee L, van Veen T, et al. (2022). *Impact of ≥ 0.1-mm free resection margins on local intramural residual cancer after local excision of T1 colorectal cancer*. Endoscopy International Open, 10(4), E282–E290. PMID 35836740, PMCID PMC9274442（open access）, doi 10.1055/a-1736-6960 — 切緣 0.1–1 mm 與 >1 mm 的局部殘留癌風險（2.9% vs 0.6%）。Route: Europe PMC REST（TITLE 檢索）。連結：https://doi.org/10.1055/a-1736-6960

- **[S9] PASS（僅供引用「有這份指引」，不得引用未經核對的內文數字）** — Vogel JD, Felder SI, Bhama AR, et al. (2022). *The American Society of Colon and Rectal Surgeons Clinical Practice Guidelines for the Management of Colon Cancer*. Diseases of the Colon and Rectum, 65(2), 148–177. PMID 34775402, doi 10.1097/DCR.0000000000002323 — 美國結直腸外科醫學會的結腸癌臨床指引。**Europe PMC 未提供摘要，我沒有取得全文**，因此只能用於「有這份 2022 年的指引」，不得引述其中任何具體建議或數字。Route: Europe PMC REST（TITLE 檢索）。連結：https://doi.org/10.1097/DCR.0000000000002323

- **[S10] PASS** — Le Voyer TE, Sigurdson ER, Hanlon AL, et al. (2003). *Colon cancer survival is associated with increasing number of lymph nodes analyzed: a secondary survey of intergroup trial INT-0089*. Journal of Clinical Oncology, 21(15), 2912–2919. PMID 12885809, doi 10.1200/JCO.2003.05.062 — ≥12 顆淋巴結這個門檻的原始證據。Route: Europe PMC REST（TITLE 檢索）。連結：https://doi.org/10.1200/JCO.2003.05.062

- **[S11] PASS** — Bundred J, Lal N, Chan DKH, Buczacki SJA (2025). *Lymph node yield as a surrogate marker for tumour biology and prognosis in colon cancer*. British Journal of Cancer, 132(7), 643–651. PMID 39953281, PMCID PMC11961567（open access）, doi 10.1038/s41416-025-02949-y — CORECT-R（n=84,116）與 SEER（n=287,974），主張淋巴結檢出數目是預後替代指標而非醫院品質指標。Route: Europe PMC REST（TITLE 檢索）。連結：https://doi.org/10.1038/s41416-025-02949-y

- **[S13] PASS** — Brierley JD, Van Eycken LJ, Giuliani ME, et al. (2026). *The 9th Edition of the UICC TNM Classification of Malignant Tumours: Updates and Rationale for Change*. International Journal of Cancer, 159(7), 1588–1601. PMID 42261202, doi 10.1002/ijc.70561 — TNM 第 9 版的改版摘要（重點在頭頸與肺）。Route: Europe PMC REST（DOI 檢索）。連結：https://doi.org/10.1002/ijc.70561

- **[S16] PASS** — Nagtegaal ID, Washington K, Brierley JD, et al. (2026). *Tumor Deposits in Colorectal Cancer: Definitions for Ninth Edition of the Tumor Node Metastasis Staging System*. Modern Pathology, 39(1), 100924. PMID 41591951, doi 10.1016/j.modpat.2025.100924 — 腫瘤沉積定義的重寫過程與「現行判定高度依賴病理醫師裁量」的說明。Route: Europe PMC REST（TITLE 檢索）。連結：https://doi.org/10.1016/j.modpat.2025.100924

- **[S17] PASS（弱證據，單中心、中文期刊）** — Song JQ, Li KX, Sun Z, et al. (2026). *[Clinical utility of the newly revised AJCC 9th edition colon cancer staging: a single-center retrospective study]*. Zhonghua Wei Chang Wai Ke Za Zhi, 29(3), 338–346. PMID 41856645, doi 10.3760/cma.j.cn441530-20250926-00361 — 北京協和 1,222 例，第 9 版提案下 79.9% 病人期別改變。**單中心、非台灣族群，只能用來說明「改版正在進行」，不可用於任何期別對應的敘述。** Route: Europe PMC REST（TITLE 檢索）。連結：https://doi.org/10.3760/cma.j.cn441530-20250926-00361

- **[S18] PASS** — Thirunavukarasu P, Sukumar S, Sathaiah M, et al. (2011). *C-stage in colon cancer: implications of carcinoembryonic antigen biomarker in staging, prognosis, and management*. Journal of the National Cancer Institute, 103(8), 689–697. PMID 21421861, doi 10.1093/jnci/djr078 — 術前 CEA 升高的獨立預後意義（HR 1.60）。Route: Europe PMC REST（AUTH+TITLE 檢索）。連結：https://doi.org/10.1093/jnci/djr078

- **[S19] PASS（族群限制大：韓國成年男性）** — Kim DH, Hong SW, Park N (2025). *Comparative analysis of alpha-fetoprotein, carbohydrate antigen 19-9, carcinoembryonic antigen, and prostate-specific antigen among conventional cigarette smokers, heated tobacco product users and quitters*. Tobacco Induced Diseases, 23. PMID 40078230, PMCID PMC11897907（open access）, doi 10.18332/tid/200890 — CEA 中位數：紙菸 2.4、加熱菸 2.0、戒菸者 1.6。**橫斷面、僅男性、韓國健檢族群**，只能用來說明「抽菸會把 CEA 拉高」，不可外推出切點。Route: Europe PMC REST（TITLE 檢索）。連結：https://doi.org/10.18332/tid/200890

- **[S21] PASS** — Mulder SA, Kranse R, Damhuis RA, et al. (2011). *Prevalence and prognosis of synchronous colorectal cancer: a Dutch population-based study*. Cancer Epidemiology, 35(5), 442–447. PMID 21470938, doi 10.1016/j.canep.2010.12.007 — 同時性大腸直腸癌 3.9%（每 25 人 1 人），34% 位於不同手術節段。Route: Europe PMC REST（TITLE 檢索）。連結：https://doi.org/10.1016/j.canep.2010.12.007

- **[S22] PASS** — Flor N, Zanchetta E, Di Leo G, et al. (2018). *Synchronous colorectal cancer using CT colonography vs. other means: a systematic review and meta-analysis*. Abdominal Radiology (New York), 43(12), 3241–3249. PMID 29948053, doi 10.1007/s00261-018-1658-1 — 有做 CT colonography 者同時性癌盛行率 5.7% vs 未做者 3.9%。Route: Europe PMC REST（TITLE 檢索）。連結：https://doi.org/10.1007/s00261-018-1658-1

- **[S23] PASS** — Moulton CA, Gu CS, Law CH, et al. (2014). *Effect of PET before liver resection on surgical management for colorectal adenocarcinoma metastases: a randomized clinical trial*. JAMA, 311(18), 1863–1869. PMID 24825641, doi 10.1001/jama.2014.3740 — 術前 PET-CT 只改變 8.0% 的手術計畫，存活無差別。Route: Europe PMC REST（EXT_ID）。連結：https://doi.org/10.1001/jama.2014.3740

- **[S24] PASS（觀察性、單中心跨時期比較）** — Layfield DM, Flashman KG, Benitez Majano S, et al. (2022). *Changing patterns of multidisciplinary team treatment, early mortality, and survival in colorectal cancer*. BJS Open, 6(5), zrac098. PMID 36254731, PMCID PMC9577547（open access）, doi 10.1093/bjsopen/zrac098 — 4,617 名經 MDT 討論的病人 14 年間的 90 天死亡率與 2 年存活變化。Route: Europe PMC REST（TITLE 檢索）。連結：https://doi.org/10.1093/bjsopen/zrac098

- **[S25] PASS（觀察性）** — Mangone L, Zizzo M, Nardecchia M, et al. (2024). *Impact of Multidisciplinary Team Management on Survival and Recurrence in Stage I-III Colorectal Cancer: A Population-Based Study in Northern Italy*. Biology, 13(11), 928. PMID 39596883, PMCID PMC11592292（open access）, doi 10.3390/biology13110928 — 以人口為基礎的 MDT 支持性資料。Route: Europe PMC REST（TITLE 檢索）。連結：https://doi.org/10.3390/biology13110928

- **[S26] PASS（觀察性，雙向關聯）** — Kaltenmeier C, Shen C, Medich DS, et al. (2021). *Time to Surgery and Colon Cancer Survival in the United States*. Annals of Surgery, 274(6), 1025–1031. PMID 31850985, doi 10.1097/SLA.0000000000003745 — 514,103 人，確診到手術 >30 天與 <7 天的死亡風險均上升。Route: Europe PMC REST（TITLE 檢索）。連結：https://doi.org/10.1097/SLA.0000000000003745

- **[S32] PASS** — Moreira L, Balaguer F, Lindor N, et al. (2012). *Identification of Lynch syndrome among patients with colorectal cancer*. JAMA, 308(15), 1555–1565. PMID 23073952, PMCID PMC3873721, doi 10.1001/jama.2012.13088 — 10,206 名先證者中 3.1% 帶有 MMR 致病變異；全面檢測 vs 各種選擇性策略的敏感度。Route: Europe PMC REST（EXT_ID）。連結：https://doi.org/10.1001/jama.2012.13088

- **[S33] PASS** — Hampel H, Frankel WL, Martin E, et al. (2005). *Screening for the Lynch syndrome (hereditary nonpolyposis colorectal cancer)*. The New England Journal of Medicine, 352(18), 1851–1860. PMID 15872200, doi 10.1056/NEJMoa043146 — 1,066 名未經篩選的大腸腺癌病人中 19.5% MSI、2.2% Lynch；21 個家族中 117 名親屬受檢、52 人帶因；MSI 與 IHC 各漏掉 2 名先證者。Route: Europe PMC REST（EXT_ID）。連結：https://doi.org/10.1056/NEJMoa043146

- **[S34] PASS** — Venderbosch S, Nagtegaal ID, Maughan TS, et al. (2014). *Mismatch repair status and BRAF mutation status in metastatic colorectal cancer patients: a pooled analysis of the CAIRO, CAIRO2, COIN, and FOCUS studies*. Clinical Cancer Research, 20(20), 5322–5330. PMID 25139339, PMCID PMC4201568, doi 10.1158/1078-0432.CCR-14-0332 — 轉移性族群 dMMR 5.0%、BRAF 突變 8.2% 與各自的預後 HR。Route: Europe PMC REST（TITLE 檢索）。連結：https://doi.org/10.1158/1078-0432.CCR-14-0332

- **[S35] PASS** — Kafatos G, Niepel D, Lowe K, et al. (2017). *RAS mutation prevalence among patients with metastatic colorectal cancer: a meta-analysis of real-world data*. Biomarkers in Medicine, 11(9), 751–760. PMID 28747067, PMCID PMC6367778（open access）, doi 10.2217/bmm-2016-0358 — 合併 RAS 突變盛行率 43.6%（95% CI 38.8–48.5%）。Route: Europe PMC REST（TITLE 檢索）。連結：https://doi.org/10.2217/bmm-2016-0358

- **[S36] PASS（樣本小、作者自陳可能有發表偏誤）** — Oyelami M, Mgbeke O, Obadiah AA, Egbeyemi A, Marshall E (2026). *The Prognostic Significance of KRAS, NRAS, and BRAF Mutations in Colorectal Cancer: A Systematic Review and Meta-Analysis*. Clinical Medicine Insights: Oncology, 20, 11795549261417367. PMID 41647651, PMCID PMC12868589（open access）, doi 10.1177/11795549261417367 — 9 個研究、3,096 人，三種突變均與較差總存活相關，BRAF 影響最大。**只有 9 個研究，敘述要保守。** Route: Europe PMC REST（TITLE 檢索）。連結：https://doi.org/10.1177/11795549261417367

- **[S37] PASS** — Seppälä TT, Latchford A, Negoi I, et al. (2021). *European guidelines from the EHTG and ESCP for Lynch syndrome: an updated third edition of the Mallorca guidelines based on gene and gender*. British Journal of Surgery, 108(5), 484–498. PMID 34043773, PMCID PMC10364896（open access）, doi 10.1002/bjs.11902 — **家族篩檢起始年齡與間隔的主要來源**（MLH1/MSH2 自 25 歲、MSH6/PMS2 自 35 歲；MLH1/MSH2/MSH6 每 2–3 年，曾罹癌者每 2 年，PMS2 可考慮每 5 年）。Route: Europe PMC REST（TITLE 檢索）＋ Europe PMC fullTextXML（PMC10364896）核對建議原文。連結：https://doi.org/10.1002/bjs.11902

- **[S38] PASS** — Engel C, Vasen HF, Seppälä T, et al. (2018). *No Difference in Colorectal Cancer Incidence or Stage at Detection by Colonoscopy Among 3 Countries With Different Lynch Syndrome Surveillance Policies*. Gastroenterology, 155(5), 1400–1409.e2. PMID 30063918, doi 10.1053/j.gastro.2018.07.030 — 德／荷／芬三國不同監測間隔，累積發生率與診斷期別無顯著差異。Route: Europe PMC REST（TITLE 檢索）。連結：https://doi.org/10.1053/j.gastro.2018.07.030

- **[S39] PASS** — Abu-Freha N, Hozaeel W, Weissmann S, et al. (2025). *Lynch Syndrome: Similarities and Differences of Recommendations in Published Guidelines*. Journal of Gastroenterology and Hepatology, 40(3), 564–573. PMID 39797698, doi 10.1111/jgh.16881 — 各學會 Lynch 指引之間的分歧（間隔多為 1–2 年，起始年齡不一致）。Route: Europe PMC REST（TITLE 檢索）。連結：https://doi.org/10.1111/jgh.16881

- **[S40] PASS** — Stjepanovic N, Moreira L, Carneiro F, et al. (2019). *Hereditary gastrointestinal cancers: ESMO Clinical Practice Guidelines for diagnosis, treatment and follow-up*. Annals of Oncology, 30(10), 1558–1571. PMID 31378807, doi 10.1093/annonc/mdz233 — ESMO 的遺傳性消化道癌症指引。對應的 ESMO 官方指引頁面：https://www.esmo.org/guidelines/esmo-clinical-practice-guideline-hereditary-gastrointestinal-cancers （WebFetch 回應 200，但頁面內容由 JavaScript 載入，抓不到條文；引用時請以期刊原文為準）。Route: Europe PMC REST（TITLE 檢索）。連結：https://doi.org/10.1093/annonc/mdz233

- **[S41] PASS（單一醫學中心生物資料庫）** — Chen YP, Hsiao TH, Lin WT, et al. (2024). *Characteristics of Cancer in Subjects Carrying Lynch Syndrome-Associated Gene Variants in Taiwanese Population: A Hospital-Based Study in Taiwan*. Cancers, 16(21), 3682. PMID 39518119, PMCID PMC11544957（open access）, doi 10.3390/cancers16213682 — 台灣 42,828 名參與者中 MMR 致病變異盛行率約 1/481；帶因者累積癌症發生率 MLH1 40.9%、MSH2 29.8%、MSH6 40%。**單一醫學中心的生物資料庫族群，不是全國盛行率。** Route: Europe PMC REST（TITLE 檢索）。連結：https://doi.org/10.3390/cancers16213682

- **[S44] PASS** — Chiu HM, Chen SL, Yen AM, et al. (2015). *Effectiveness of fecal immunochemical testing in reducing colorectal cancer mortality from the One Million Taiwanese Screening Program*. Cancer, 121(18), 3221–3229. PMID 25995082, PMCID PMC4676309（open access）, doi 10.1002/cncr.29462 — 台灣百萬人篩檢：受篩者死亡率下降 62%（RR 0.38），校正後全人口下降 10%（RR 0.90）。Route: Europe PMC REST（TITLE/ABSTRACT 檢索）。連結：https://doi.org/10.1002/cncr.29462

- **[S45] PASS** — Hsu WF, Ladabaum U, Su CW, et al. (2025). *Interval Colorectal Cancers in a Fecal Immunochemical Test-Based Screening Program*. JAMA Network Open, 8(7), e2523441. PMID 40720124, PMCID PMC12305388（open access）, doi 10.1001/jamanetworkopen.2025.23441 — 台灣篩檢計畫的間隔癌負擔（26.2%）與大腸鏡品質（ADR）的關係。Route: Europe PMC REST（TITLE/ABSTRACT 檢索）。連結：https://doi.org/10.1001/jamanetworkopen.2025.23441

## 官方文件來源

- **[S12] PASS** — College of American Pathologists. *Protocol for the Examination of Resection Specimens from Patients with Primary Carcinoma of the Colon and / or Rectum*, Version 4.4.0.1, Protocol Posting Date: September 2025, CAP Laboratory Accreditation Program Protocol Required Use Date: March 2026. — 文件內明載「Standard(s): AJCC 8」與「pTNM CLASSIFICATION (AJCC 8th Edition)」，並提供 pT／pN／pM 的完整定義與「至少 12 顆淋巴結」的 National Quality Forum 品質指標說明。Route: curl 直接下載 PDF（HTTP 200）並以 pdftotext 逐段核對。連結：https://www.cap.org/protocols-and-guidelines/cancer-reporting-tools/cancer-protocol-templates

- **[S14] PASS** — Union for International Cancer Control (UICC). *9th Edition of the UICC TNM classification of Malignant Tumours now available!* — 第 9 版於 2025 年 7 月 3 日發行，UICC 建議自 2026 年 1 月 1 日起適用；改版部位為鼻咽、HPV 相關口咽、肺、胸腺、間皮瘤、闌尾、肛管、子宮頸、外陰與攝護腺（**不含結腸直腸**）。Route: WebFetch（HTTP 200）。連結：https://www.uicc.org/news-and-updates/25-7-announcements/9th-edition-uicc-tnm-classification-malignant-tumours-now-available

- **[S15] PASS** — American College of Surgeons / American Joint Committee on Cancer. *AJCC Version 9 Cancer Staging System*. — 逐部位分批發行清單（2021 子宮頸；2023 闌尾、肛門、腦與脊髓；2024 各 NET 部位含結腸與直腸 NET、外陰；2025 肺、胸腺、間皮瘤、鼻咽；2026 唾液腺、HPV 相關口咽），並載明第 8 版所有部位在被 Version 9 取代前仍然現行。Route: WebFetch（HTTP 200）。連結：https://www.facs.org/quality-programs/cancer-programs/american-joint-committee-on-cancer/version-9/

- **[S20] PASS** — National Cancer Institute（美國國家癌症研究所）. *Colon Cancer Treatment (PDQ®) – Health Professional Version*. — AJCC 第 8 版結腸癌期別組合表（IIA = T3N0M0；IIB = T4aN0M0；IIC = T4bN0M0；IIIA、IIIB、IIIC 的組合；**T3N1M0 = 第 IIIB 期**）。Route: WebFetch（HTTP 200）。連結：https://www.cancer.gov/types/colorectal/hp/colon-treatment-pdq

- **[S27] PASS** — 法務部全國法規資料庫。《全民健康保險保險對象免自行負擔費用辦法》，修正日期：民國 113 年 09 月 16 日（本次查證時全國法規資料庫法規整編資料截止日為民國 115 年 08 月 21 日）。— 第 2 條（申請文件、診斷證明書 30 日效期、代理人）、第 3 條（14 日內核定，不含例假日）、第 5 條（以申請之日為生效日、效期屆滿三個月前得重新申請）、第 6 條（免自行負擔費用範圍）。Route: curl 直接取得 HTML（HTTP 200）並解析條文全文。連結：https://law.moj.gov.tw/LawClass/LawAll.aspx?PCode=L0060015

- **[S28] PASS** — 衛生福利部中央健康保險署。《全民健康保險保險對象免自行負擔費用辦法第二條附表一修正規定：全民健康保險重大傷病項目及其證明有效期限》（一百十四年一月一日以後適用，ICD-10-CM/PCS 2023 年版）。— 「一、需積極或長期治療之癌症」項下「(五) 除(一)–(四)之其他惡性腫瘤（C00.0–C96.9，不含 C73、C94.4、C94.6）」證明有效期限為**五年**；結腸惡性腫瘤（C18）屬此類。Route: curl 直接下載 PDF（HTTP 200）並以 pdftotext 核對；同時比對 111.12.19 舊版確認為現行版本。連結：https://www.nhi.gov.tw/ch/dl-74911-9ea79f859a24431497ef0304ce4b7981-1.pdf

- **[S29] PASS** — 衛生福利部中央健康保險署。〈重大傷病專區—申請須知及文件下載〉。— 申請所需文件與三種送件方式（本人／委託代理人郵寄或親送、院所透過健保資訊服務網線上申請、向分區業務組提出）。Route: WebFetch（HTTP 200；curl 直連得 403，改用 WebFetch）。連結：https://www.nhi.gov.tw/ch/cp-6091-08ad9-2957-1.html

- **[S30] PASS** — 衛生福利部中央健康保險署。《全民健康保險醫療服務給付項目及支付標準》品項檔（檔案版本 114.03.13）。— 項目 26072B「正子造影－全身」36,500 點、26073B「正子造影－局部」26,500 點，腫瘤適應症含「大腸癌、直腸癌…之分期及懷疑復發或再分期」，並附「須經電腦斷層、核磁共振、核子醫學掃瞄等檢查仍無法分期，或認定該等檢查不足以提供足夠資訊，且須於病歷中說明必要性理由」等規範；「懷疑復發或再分期」不得用於例行追蹤檢查。另同一檔案的第 6089 號頁面說明重大傷病免自行負擔費用範圍之法令依據為全民健康保險法第 48 條與本辦法。Route: curl 下載官方 txt 檔（HTTP 200，21.4 MB）逐行檢索項目代碼與備註原文；支付標準頁面 WebFetch（HTTP 200）。連結（支付標準頁面）：https://www.nhi.gov.tw/ch/cp-5943-f1cce-2821-1.html ；連結（免自行負擔範圍頁面）：https://www.nhi.gov.tw/ch/cp-6089-0c619-2957-1.html

- **[S31] PASS** — 衛生福利部中央健康保險署。〈常見醫療院所要求自費之醫療項目－正子斷層造影〉（民眾版說明文件）。— 全身 36,500 點、局部 26,500 點；腫瘤與非腫瘤適應症清單；「民眾以正子造影來篩檢癌症是必須自費」；每次檢查游離輻射劑量約 6–10 毫西弗，相當於 100–160 張胸部 X 光。**此文件未標示發布或修訂日期**，引用時請以 [S30] 的支付標準條文為準，本文件只用於民眾版的說明語氣與輻射劑量。Route: curl 直接下載 PDF（HTTP 200）並以 pdftotext 讀取全文。連結：https://www.nhi.gov.tw/ch/dl-18965-4379120973164be98add7d9c5a511d96-1.pdf

- **[S42] PASS** — 衛生福利部。〈健康台灣–擴展腸癌防護網 「腸」常篩檢護健康〉（建檔／更新日期：民國 114 年 1 月 16 日；政策自 114 年 1 月 1 日起生效）。— 大腸癌篩檢補助對象「擴大至 45 至 74 歲民眾及 40 至 44 歲有家族病史者（父母、子女或兄弟姊妹經診斷為大腸癌者）」，「每 2 年 1 次免費糞便潛血檢查」。Route: WebFetch（HTTP 200）。連結：https://www.mohw.gov.tw/cp-16-81256-1.html

- **[S43] PASS** — 衛生福利部。〈擴大推動五癌篩檢 攜手共創你我健康〉（民國 114 年 5 月 15 日）。— 重述「建議 40 歲至 44 歲具大腸癌家族史的民眾與 45 歲至 74 歲民眾，每 2 年 1 次接受糞便潛血檢查」。Route: WebFetch（HTTP 200）。連結：https://www.mohw.gov.tw/cp-16-82502-1.html

- **[S46] PASS** — 衛生福利部中央健康保險署。《全民健康保險醫療服務給付項目及支付標準》品項檔（檔案版本 114.03.13）中的基因檢測項目。— 30104B / 30106B「All-RAS 及 BRAF 基因突變分析（LDTs / IVD）」各 11,878 點，適應症限符合藥品給付規定 9.27 Cetuximab 及 9.53 Panitumumab 之轉移性直腸結腸癌病人，檢測須含 KRAS exon 2/3/4、NRAS exon 2/3/4 與 BRAF V600E，限用藥前伴隨式檢測、每人終生一次；30107B「BRAF 基因突變分析（LDTs）」3,006 點；30301B/30302B/30303B 實體腫瘤 NGS 分別 10,000 / 20,000 / 30,000 點，醫院須為區域級以上或通過「癌症診療品質認證醫院」且設立或聯合組成分子腫瘤委員會（MTB），每人每癌別擇一申報且終生一次；25012B「免疫組織化學染色（每一抗體）」1,354 點，每例限五種抗體（特定四類腫瘤放寬至十種，不含大腸癌）。Route: curl 下載官方 txt 檔（HTTP 200）逐行檢索並列印完整備註欄。連結：https://www.nhi.gov.tw/ch/cp-5943-f1cce-2821-1.html

- **[S47] PASS** — 衛生福利部。〈健保5月1日起給付癌症精準醫療「實體癌/血癌次世代基因定序檢測(NGS)」2萬多名癌友受惠〉（113 年 5 月 1 日起實施）。— NGS 給付起始日、定額給付級距（BRCA 1 萬點、小套組 ≦100 基因 2 萬點、大套組 >100 基因 3 萬點）、每人每癌別終生一次；文中並載明大腸直腸癌等癌別「將採單基因檢測」。Route: WebFetch（HTTP 200）。連結：https://www.mohw.gov.tw/cp-16-78416-1.html

- **[S48] PASS（文件日期為 113.08.05，2026 年可能已異動）** — 衛生福利部中央健康保險署。〈「次世代基因定序(NGS)支付標準」問答輯〉第二版，113.08.05。— 「7 大類癌症（大腸直腸癌、泌尿道上皮癌、黑色素瘤、胃癌、B 細胞淋巴癌及 T 或 NK 細胞血癌與淋巴癌）專家共識建議採『單基因檢測』，相關醫學會已陸續提出新增修訂診療項目之申請，本署將依程序研議。」Route: curl 直接下載 PDF（HTTP 200）並以 pdftotext 檢索原文。連結：https://www.nhi.gov.tw/ch/dl-69957-04acdb972dc54e4ebb47fa3fab24b0fd-1.pdf ；NGS 專區頁面：https://www.nhi.gov.tw/ch/np-3636-1.html

## FAIL（保留紀錄，說明試過哪些路徑）

- **[S49] FAIL** — 衛生福利部國民健康署（www.hpa.gov.tw）。目標頁面包含〈大腸癌篩檢簡介〉（nodeid=621&pid=1136）、〈健康臺灣-114年起擴大癌症篩檢〉（nodeid=4809&pid=18712）、〈大腸癌擴大篩檢 半年突破103萬人〉（nodeid=4878&pid=19212）。**curl 與 curl --cacert /root/.ccr/ca-bundle.crt 皆回傳 HTTP 000（TLS 無法建立安全連線）；WebFetch 回傳 ROBOTS_DISALLOWED（robots.txt 抓取時 SSL CERTIFICATE_VERIFY_FAILED）。** 改以衛生福利部（www.mohw.gov.tw）的兩則官方頁面 [S42][S43] 取代，篩檢政策的年齡與間隔已由這兩則交叉確認。**但「115 年（2026）起是否再調整大腸癌篩檢年齡帶」無法從國民健康署第一手頁面確認**，文章請寫「以國民健康署公告為準」。

- **[S50] FAIL** — NCCN Clinical Practice Guidelines in Oncology: Colon Cancer（https://www.nccn.org/guidelines/guidelines-detail?category=1&id=1428）。WebFetch 回傳 **HTTP 403**（需登入）。無法確認版本與內容，**本專題 A 組不引用 NCCN**。

- **[S51] FAIL** — ESMO 指引頁面 https://www.esmo.org/guidelines/gastrointestinal-cancers/localised-colon-cancer 回傳 **HTTP 404**。正確的頁面為 https://www.esmo.org/guidelines/esmo-clinical-practice-guideline-localised-colon-cancer （由 WebSearch 於 esmo.org 內找到），但該頁內容由 JavaScript 載入，WebFetch 取不到條文。對應的期刊原文為 Argilés G, et al. (2020). *Localised colon cancer: ESMO Clinical Practice Guidelines for diagnosis, treatment and follow-up*. Annals of Oncology, 31(10), 1291–1305. PMID 32702383, doi 10.1016/j.annonc.2020.06.022（此筆已經 Europe PMC REST 核對，但**內容未取得**，故不列為 PASS，A 組請勿引用其內文）。

- **[S52] FAIL** — RCPA *Pathology*〈Validation of the proposed AJCC 9th edition colon cancer staging system in a large single-centre cohort〉（https://www.pathologyjournal.rcpa.edu.au/article/S0031-3025(26)00011-5/fulltext）。WebFetch 回傳 **HTTP 403**。無法取得書目與內容，不引用。

- **[S53] FAIL** — 台北區醫療網／衛福部所屬單位頁面〈115年國民健康署擴大健檢與癌篩〉（https://www.taic.mohw.gov.tw/...iid=6502）。WebFetch 回傳 **HTTP 403**。115 年癌篩擴大的細節無法從此路徑取得。

- **[S54] FAIL（查無其物，非連線失敗）** — MMR／MSI 專屬的健保支付標準項目代碼。以「微衛星」「微衛星不穩定」「錯配修復」「不匹配修復」「MSI」「MSI-H」「MLH1」「MSH2」等關鍵字檢索《全民健康保險醫療服務給付項目及支付標準》品項檔（114.03.13 版，21.4 MB）**全部 0 筆**。因此無法確認 MMR/MSI 檢驗在台灣的給付狀態，A4 一律寫成「要跟個管師或醫院醫務課確認」。

- **[S55] FAIL** — 分期用電腦斷層（CT）與核磁共振（MRI）對應結腸癌的健保給付條文。已下載並檢索支付標準品項檔，但未能定位到與結腸癌分期直接對應、可引用的條文；不宣稱有無給付，寫成 gap。
