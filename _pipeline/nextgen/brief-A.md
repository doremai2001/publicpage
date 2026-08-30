# A 組研究簡報 — 次世代治療專題（N1 總論尺、N2 法規身分）

查證日期：2026-08-29。所有期刊來源均以 Europe PMC REST API（`https://www.ebi.ac.uk/europepmc/webservices/rest/search`）逐條核對標題、作者、卷、期、頁、年、DOI 與 OA 狀態；官方文件以 curl / WebFetch 實際取得頁面或 PDF 原文，並記錄取得日期與版本日期。負面宣稱（「沒有核准」「沒有給付項目」「沒有試驗」）一律附上檢索路徑。**依規格，各技術的臨床證據細節（N3–N6）不在本簡報**；N2 是全專題法規身分的唯一真相來源，四技術的身分事實集中寫在這裡。

---

# N1 — 〈新，不等於比較好〉

## Key facts

**「劑量學／機轉上的優勢」在隨機試驗裡消失或反轉的放射腫瘤學實例**

- **RTOG 0617（劑量增加反而害命）**：III 期不可手術非小細胞肺癌的隨機第三期試驗（美加 185 家機構，2×2 設計，544 人隨機分派：標準劑量 60 Gy 組 166＋147 人、高劑量 74 Gy 組 121＋110 人）。「劑量更高應該殺死更多腫瘤」在物理與機轉上完全合理，結果是**高劑量組中位存活 20.3 個月、標準劑量組 28.7 個月（HR 1.38，95% CI 1.09–1.76，p=0.004）**——多給的劑量讓病人活得更短。第 3 級以上食道炎 21%（43/207）對 7%（16/217）；治療相關死亡 8 對 3 人。[S1]
- RTOG 0617 長期追蹤（中位 5.1 年）確認：5 年整體存活 32.1%（60 Gy）對 23%（74 Gy）；第 5 級不良事件 3 對 9 件；結論明寫 60 Gy 併用化療「應維持標準治療」。[S2]
- **RTOG 0126（替代終點改善、存活沒變、副作用變多）**：中風險攝護腺癌 1,532 人隨機分派 79.2 Gy 對 70.2 Gy（分析 1,499 人：751 對 748）。高劑量組生化失敗率明顯較低（8 年 20% 對 35%，Phoenix 定義，HR 0.54），但 **8 年整體存活 76% 對 75%（HR 1.00，95% CI 0.83–1.20，p=0.98）完全沒有差別**；晚期第 2 級以上腸胃道毒性 21% 對 15%、泌尿道毒性 12% 對 7%，都是高劑量組較差。「指標變好」不等於「人活得更久」的教科書例子。[S4]
- **質子對光子的隨機比較（劑量分布佔優、臨床終點沒贏）**：MD Anderson 的貝氏適應性隨機試驗，局部晚期非小細胞肺癌同步化放療，被動散射質子（57 人）對 IMRT（92 人），只有兩種計畫都能通過同樣劑量限制的病人才隨機分派。質子組心臟劑量在 5–80 Gy(RBE) 全段都較低，但主要終點：第 3 級以上放射性肺炎 IMRT 6.5% 對質子 10.5%、局部失敗率 10.9% 對 10.5%——**沒有觀察到臨床好處**。[S3]（此為單一試驗、被動散射技術、特定癌別；不可外推成「質子沒效」，見 Claim ceiling。）

**排擠效應（警語一）的證據底座**

- 財務毒性的定義與框架：Carrera 等在 CA: A Cancer Journal for Clinicians 的回顧將財務毒性定義為病人因治療產生的「客觀財務負擔＋主觀財務困擾」，並指出不當的財務因應（如為了省錢少拿藥、跳過回診）會連帶惡化健康結果。[S9]
- 美國全國代表性樣本（2011 MEPS「Experiences With Cancer」問卷，1,202 位成年癌症存活者）：18–64 歲組 **28.4%** 曾因癌症借錢、破產、付不出醫療費或做出其他重大財務犧牲（≥65 歲組 13.8%，p<0.001）；曾為醫療帳單擔憂的心理財務困擾 18–64 歲 31.9%、≥65 歲 14.7%。[S7]
- 財務崩潰與死亡的關聯：西華盛頓 SEER 癌症登記串接聯邦破產紀錄（1995–2009 年 231,596 位癌症病人，4,728 人申請破產），傾向分數配對後，**申請破產者的死亡風險比 1.79（95% CI 1.64–1.96）**。這是觀察性資料，只能寫成「嚴重財務困境與較高死亡風險相關」，不可寫成因果。[S8]
- **臨床試驗常排除近期接受過實驗性治療的人**——兩層證據：
  1. 共識文件：ASCO 與 Friends of Cancer Research 的「先前治療工作小組」建議（Clin Cancer Res 2021）開宗明義承認「以先前治療作為排除條件的限制很常見」，並建議除非有科學理由，不應以先前治療的次數或種類排除病人——這份建議之所以存在，正因為現行慣例普遍如此。[S10]
  2. 具體條文：KEYNOTE-048（復發／轉移性頭頸癌第三期試驗，NCT02358031）排除條件原文：「Currently participating and receiving study therapy, or participated in a study of an investigational agent and received study therapy, or used an investigational device **within 4 weeks** of the first dose of study medication」。[S11]
- 台灣的藥品臨床試驗法規本身要求利益風險衡量：藥品優良臨床試驗作業準則第 4 條——執行臨床試驗應符合赫爾辛基宣言；預期利益應超過可能風險始得進行；受試者權利安全福祉勝於科學及社會利益。[S16]

**怎麼找臨床試驗（台灣）**

- 國際註冊庫：ClinicalTrials.gov（美國國家醫學圖書館），可依癌別、國家（Taiwan）、收案狀態檢索；本簡報多筆查證即以其公開 API v2 完成。[S13]
- 台灣官方入口 **2026 年的正確答案**：衛生福利部食品藥物管理署「**台灣藥品臨床試驗資訊網**」，網址 `https://e-sub.fda.gov.tw/ClinicalTrialInfo`（頁面標題「台灣藥品臨床試驗資訊網｜衛生福利部食品藥物管理署」，設有公開的案件查詢功能）。[S14]
- 舊的「台灣藥物臨床試驗資訊網」（醫藥品查驗中心 CDE，www1.cde.org.tw/ct_taiwan/）**已關閉**，原站現掛公告：「為配合衛生福利部『台灣藥品臨床試驗網』功能上線，本系統功能即日起關閉」，並導向上述新站。寫文章時不要再給 CDE 舊網址。[S15]
- 誠實框架（試驗給什麼、不給什麼）：美國國家癌症研究所（NCI）病人頁面（2024-11-18 更新）同時列出：可能的好處（接觸到試驗外拿不到的治療、較密集的追蹤照護、幫助未來的病人）與可能的壞處——原文直譯：「**研究中的治療可能不比標準治療好，甚至可能不如標準治療**」、可能有更差的副作用、更多回診與檢查、交通住宿等額外花費。[S12]

**早期安寧緩和照護（紅線 8「什麼時候該談安寧」的證據）**

- Temel 2010（NEJM，單一機構隨機試驗，151 位新診斷轉移性非小細胞肺癌）：確診後早期整合安寧緩和照護組 12 週生活品質較佳（FACT-L 98.0 對 91.5，p=0.03）、憂鬱症狀較少（16% 對 38%，p=0.01）、生命末期接受激進治療較少（33% 對 54%，p=0.05），且中位存活較長（11.6 對 8.9 個月，p=0.02）。**存活差異來自單一試驗的次要觀察，不可寫成「安寧會延長壽命」**。[S5]
- Cochrane 2017（Haun 等，7 個隨機／叢集隨機試驗、1,614 位晚期癌症成人）：早期安寧緩和照護改善健康相關生活品質，效果量小（**SMD 0.27，95% CI 0.15–0.38**；治療後分析 1,028 人；低確定性證據），換算 FACT-G 平均多 4.59 分（95% CI 2.55–6.46）；症狀強度略低（SMD −0.23，95% CI −0.35 到 −0.10）；**存活（4 試驗、800 人）沒有顯示差異（死亡 HR 0.85，95% CI 0.56–1.28，極低確定性）**；憂鬱無顯著差異。[S6]

## Claim ceiling

Defensible：
- 「在放射腫瘤學裡，『物理上更合理』被隨機試驗推翻過不只一次：RTOG 0617 裡劑量更高的那組活得更短（中位 20.3 對 28.7 個月）；RTOG 0126 裡高劑量把生化失敗率壓低了一半，整體存活卻一模一樣（8 年 76% 對 75%），副作用還更多；質子與 IMRT 在肺癌的隨機比較裡，質子的心臟劑量確實比較低，但肺炎與局部失敗都沒有比較少。所以『劑量圖比較漂亮』『機轉比較聰明』是假說的起點，不是療效的證明。」
- 「自費新療法排擠的是三樣有價值的東西：還沒用完的標準治療、後線的錢（癌症病人的財務困境是有數字的：美國 18–64 歲存活者 28.4% 有具體財務損害；申請破產者死亡風險高 79%——相關性）、以及臨床試驗資格（大型試驗常明文排除四週內用過實驗性藥物或器材的人，KEYNOTE-048 的條文就是這樣寫的）。」
- 「臨床試驗是真實選項但不是後門：官方入口是 ClinicalTrials.gov 與衛福部食藥署的台灣藥品臨床試驗資訊網；NCI 自己的病人頁面明寫研究中的治療『可能不比標準治療好，甚至可能更差』。」
- 「早期安寧緩和照護有隨機試驗與統合分析支持：生活品質改善（效果量小但方向一致），而且沒有證據顯示會讓人走得比較快。」

Would overstate：
- ✗「新技術都沒有用」「質子被證明無效」——Liao 試驗是單一試驗、被動散射技術、肺癌一個癌別，且以劑量限制可同時滿足者為收案條件 [S3]。只能寫「在這個試驗裡沒有看到好處」。
- ✗「劑量學優勢毫無意義」——0126 的高劑量確實減少生化失敗與挽救治療 [S4]；問題是那不等於存活。
- ✗「參加臨床試驗就能拿到更好的治療」——NCI 頁面明確反對這個讀法 [S12]。
- ✗「安寧照護可以延長壽命」——Temel 是單一試驗的觀察 [S5]，Cochrane 統合的死亡 HR 0.85（0.56–1.28）沒有顯示差異、極低確定性 [S6]。可以寫「不會讓人走得比較快」。
- ✗「自費治療會害你更早死」——Ramsey 的 HR 1.79 是破產與死亡的觀察性關聯 [S8]，不可寫成「花錢買自費＝提高死亡率」。
- ✗ 用「做了實驗性治療就永遠不能進試驗」嚇人——排除條款多為時間窗（如四週）與特定情形 [S10][S11]，誠實寫法是「很多試驗會排除近期接受過實驗性治療的人，等於把一扇門暫時關上」。

## Caveats / safety notes

- RTOG 0617 的教訓是「未經隨機驗證的合理假設可能有害」，不是「放療劑量都不該提高」；文章不可讓讀者對自己正在接受的處方劑量產生懷疑。
- 財務數字全部來自美國健保環境（自付結構與台灣不同），引用時必須註明「美國資料」；台灣的癌症財務毒性本土數據**本次檢索未找到可引用的代表性研究**（檢索路徑見 [S7] 條目後注），不要編造台灣數字。
- 「排除近期實驗性治療」要寫成「每個試驗的條文不同、時間窗不同，報名前要把先前治療清單交給試驗團隊判斷」，不可寫死一個週數。
- 臨床試驗段落必須同時寫「技術料免費／由試驗支付的部分」與「不是所有費用都免」——本簡報未查證台灣試驗費用分攤的通則條文，寫成「哪些費用由試驗吸收，要在同意書裡逐條確認」。
- 安寧段落引用 Cochrane 時要一併寫出「低／極低確定性」與「效果量小」——這是作者自陳，照抄才誠實。
- 紅線 7 的句子（決定結果的是期別、亞型、與有沒有把療程做完）在本簡報沒有單獨引用來源；它是全站一貫立場的總結句，寫作時不要掛引用編號在它身上。

## Taiwan status

- 找試驗的官方入口已查證：[S13][S14]，舊站關閉公告 [S15]。
- 台灣藥品臨床試驗的法源與倫理要求已查證：藥品優良臨床試驗作業準則（**注意正式名稱有「作業」二字**，修正日期民國 109-08-28）[S16]。
- 台灣本土財務毒性數據：**gap**（未找到可引用的代表性研究）。
- 安寧緩和照護在台灣的給付與轉介路徑：**gap**（本次未查證；正文寫「安寧共同照護與門診、居家安寧的轉介做法各院不同，請問你的個管師」，不得宣稱給付狀態）。

---

# N2 — 〈核准、給付、有效，是三件不同的事〉

## Key facts — 台灣的五種身分（全部查自現行法規原文）

- **1. 臨床試驗**：法源為藥事法第 42 條第 2 項授權訂定之「**藥品優良臨床試驗作業準則**」（修正日期民國 109-08-28）。第 3 條定義臨床試驗為「以發現或證明藥品在臨床、藥理或其他藥學上之作用為目的，而於人體執行之研究」；受試者同意書、人體試驗委員會（保護受試者權利安全福祉）皆在同條定義；第 4 條要求符合赫爾辛基宣言、預期利益應超過可能風險。[S16]
- **2. 特管辦法**：正式名稱「**特定醫療技術檢查檢驗醫療儀器施行或使用管理辦法**」，依醫療法第 62 條第 2 項訂定，**現行版本修正日期民國 114-12-31（2025-12-31）**，2026-08-29 取得之現行條文仍含細胞治療技術專節。核心結構：
  - 第 3 條：醫療機構施行**非人體試驗**之細胞治療技術，應檢附操作醫師資格證明、細胞製備場所證明、施行計畫，**向中央主管機關申請核准**後經地方主管機關登記始得為之。[S17]
  - 第 13 條：施行計畫應載明機構名稱、細胞治療項目、**適應症**、專任操作醫師、施行方式、療效評估與追蹤方式、**費用及其收取方式**、**已發表之國內外相關文獻報告**、同意書範本、細胞製備場所、細胞成分製程管控、不良反應救濟措施。[S17]
  - 第 18 條：非預期嚴重不良反應應於得知後七日內通報；第 20 條：每年提出施行結果報告（案例數、治療效果、不良反應）；第 21 條：不良事件數或嚴重度顯有異常者，中央主管機關得停止或終止其施行。[S17]
  - **可據此寫的定性**：特管核准的是「哪家醫院、哪個技術、哪些適應症、收多少錢」的施行計畫，附帶安全通報與年度成果報告義務；申請時交的是「已發表文獻」而非自家的隨機試驗結果——**它是管理與安全框架，不是療效認證**。
  - 附表三所列六類細胞治療技術含「自體免疫細胞治療（CIK、NK、DC、DC-CIK、TIL、gamma-delta T）」，適應症為「血液惡性腫瘤經標準治療無效」「第一期至第三期實體癌經標準治療無效」「實體癌第四期」。[S17]
- **3. 恩慈使用／專案核准**：藥事法第 **48-2** 條——「為預防、診治危及生命或嚴重失能之疾病，且國內尚無適當藥品或合適替代療法」或「因應緊急或重大影響公共衛生情事」，中央衛生主管機關得**專案核准**特定藥品之製造或輸入，不受第 39 條（查驗登記）限制；已有許可證藥品或合適替代療法出現時得廢止核准。[S18]
- **4. 醫材許可證**：醫療器材管理法（公布民國 109-01-15）第 25 條——製造、輸入醫療器材應向中央主管機關申請**查驗登記**，經核准發給**醫療器材許可證**後始得為之（公告品項改採登錄制）。[S19]
- **5. 再生醫療雙法——2026 年的狀態是「已施行」**：
  - **再生醫療法**：民國 113-06-19（2024-06-19）總統令制定公布全文 35 條，施行日期由行政院定之；**行政院 114-12-30（2025-12-30）院臺衛字第 1141035478 號令發布定自 115-01-01（2026-01-01）施行**。[S20]
  - **再生醫療製劑條例**：同日（2024-06-19）公布全文 23 條，**同一紙行政院令定自 2026-01-01 施行**。[S21]
  - 再生醫療法第 8 條：醫療機構執行再生技術原則上應完成人體試驗，但「治療危及生命或嚴重失能之疾病，且國內尚無適當之藥品、醫療器材或醫療技術」或「本法施行前經中央主管機關核准執行之再生技術」得**免完成人體試驗**——後者就是特管辦法已核准案件的過渡條款。[S20]
  - **Gap**：2026-01-01 之後新申請的細胞治療案件由再生醫療法或特管辦法何者受理、兩制如何併行，本次未取得衛福部的說明文件；特管辦法 114-12-31 該次修正的修正內容對照表也未取得。正文寫到這裡時停在「2026 年起再生醫療雙法已上路、舊特管核准案有過渡條款」即可，不要展開兩制分工。

## Key facts — 美國 FDA

- **器材是「列級＋上市前程序」，不是逐癌別核准**：質子治療機在美國的法規身分是 21 CFR 892.5050「medical charged-particle radiation therapy system」（醫用帶電粒子放射治療系統），**Class II（第二級）醫材**。[S25]
- Class II 走 **510(k) premarket notification（上市前通知，通稱 clearance「核可／許可」）**：申請者證明新器材與已合法上市的「述詞器材」（predicate）**實質等同**（substantially equivalent）即可上市；FDA 明文區分 510(k) clearance 與 PMA（premarket approval）的 approval 是不同程序。[S26]
- openFDA 510(k) 資料庫檢索（2026-08-29）：產品代碼 LHN 共 **92 筆核可紀錄**，全部為「Substantially Equivalent」，最近如 2026-06-11、2026-04-23、2026-03-25 各家質子系統；**同一產品代碼下 PMA 資料庫為零筆**——佐證「質子機用的是與既有機器實質等同的 510(k) 路徑，FDA 從未按癌別『批准』質子治療」。[S27]
- **未上市器材做人體研究的身分**：IDE（investigational device exemption）——FDA 官方定義「允許研究用器材在臨床研究中使用，以蒐集安全性與有效性資料」。[S29]
- **藥品核准的標準（對照組）**：FDA 藥品審查（CDER）要求「藥品提供的效益超過其已知與潛在風險（對目標族群）」始得核准。[S30]
- **FLASH 與 BNCT 在美國的身分（負面查證，2026-08-29）**：openFDA drugs@FDA 檢索 generic name／active ingredient「borofalan」→ **零筆**；510(k) 資料庫檢索 device_name 含「FLASH」且產品代碼 LHN → 零筆；device_name「carbon ion」→ **零筆**。[S28] FLASH 人體使用目前見於臨床試驗（FAST-01，NCT04592887，見 [S44]）。
- **美國重粒子（碳離子）**：零家臨床運轉中心。2026 年 IJPT「Hadrontherapy for Life」白皮書：全球碳離子中心分布於日本、歐洲（HIT、CNAO、MedAustron 等）、中國（蘭州、上海）、台灣（台北）、南韓；**「In the USA, Mayo Clinic is building a CIRT facility in Jacksonville, Florida」——興建中，尚未治療病人**；全球累計治療已逾 50,000 人。[S40]（PTCOG 官方設施統計頁本次無法取得，見 [S50] FAIL。）

## Key facts — 歐盟

- **CE 標章證明的是什麼**：歐盟醫療器材規則 MDR（Regulation (EU) 2017/745，取得 2025-01-10 合併版全文）第 20 條——「被認為**符合本規則要求**之器材應附 CE 合格標章」；第 5 條——器材應符合附件一之一般安全與性能要求，符合性證明**包含臨床評估**（第 61 條）。[S31]
- 可據此寫的定性：CE 標章是「符合安全與性能要求」的合格認證，由公告機構審查，**不是**「對某個癌別優於標準治療」的療效判定，也沒有逐癌別的適應症核准清單。給付則由各會員國各自決定（見下）。
- 歐洲碳離子中心的給付現實（來源同白皮書）：歐洲的健保給付系統「通常要求與標準放療比較的隨機臨床試驗高階證據，才可能核予給付」，且各國制度差異大。[S40]
- **歐盟 BNCT**：EMA 藥品資料庫檢索 borofalan 無法完成（網站阻擋自動化工具，[S51] FAIL）；PMDA 審查報告記載至 2019-11 borofalan 未在任何國家或地區核准 [S32]；本次未查得任何歐盟上市許可存在的跡象，但「不存在」無法以官方資料庫直接證明——正文寫「查無歐盟核准紀錄（查證日 2026-08）」。

## Key facts — 日本（藥證＋保險給付是兩關）

- **BNCT——目前全球唯一「有藥證＋有給付」的司法管轄區**：
  - 藥證：厚生勞動省藥事審議會 2020-02-26 通過、審議結果報告書 2020-03-03——Steboronine 9000 mg/300 mL（borofalan (10B)，Stella Pharma）；**核准適應症原文：「Unresectable, locally advanced or locally recurrent head and neck cancer」（無法切除之局部晚期或局部復發頭頸癌）**——注意不是只有「復發」，也含局部晚期；附帶條件：風險管理計畫＋**全數用藥病人的使用成績調查**（因日本臨床試驗病人數有限）。[S32]
  - 器材：同期核准 Sumitomo Heavy Industries 的 **NeuCure BNCT System（加速器中子源）與 NeuCure BNCT Dose Engine**（審議結果 2020-02-19；指定 8 年使用成績調查）。[S33]
  - 給付：全國性上市後調查論文（Cancers 2024，開放取用）明載「PMDA approvals in March 2020」且「**included for coverage by the national health insurance system in Japan in June 2020**」；PMS 于 2020 年 5 月啟動、收入 162 位病人（144 位頭頸鱗癌），復發鱗癌 1 年整體存活 78.8%、2 年 60.7%。[S34]
  - 藥證依據的第二期試驗：JHN002（Hirose 等，Radiother Oncol 2021;155:182-187）。[S35]
- **粒子線治療（質子＋碳離子）的保險收載清單（JASTRO 官方頁，2026-06 更新）**：
  - 陽子線（質子）保險適用：頭頸部惡性腫瘤（口腔咽喉之鱗癌除外）、早期肺癌（I–IIA 期）＊、肝細胞癌＊（≥4cm）、肝內膽管癌＊、局部進行性胰癌＊、局部大腸癌＊（術後復發）、限局性及局部進行性攝護腺癌、限局性骨軟部腫瘤＊、**小兒腫瘤（限局性固形惡性腫瘤）**、大腸癌肺轉移（≤3 個、原發已切除、無局部復發且肺外轉移受控）＊。
  - 重粒子線（碳離子）保險適用：頭頸部惡性腫瘤（同上例外）、早期肺癌（I–IIA 期）＊、肝細胞癌＊（≥4cm）、肝內膽管癌＊、局部進行性胰癌＊、局部大腸癌＊（術後復發）、局部進行性子宮頸腺癌＊、局部進行性子宮頸鱗癌（≥6cm）＊、婦科惡性黑色素瘤＊、限局性及局部進行性攝護腺癌、限局性骨軟部腫瘤＊、大腸癌肺轉移（同上條件）＊。
  - ＊號規則原文：「**手術による根治的な治療が困難であるものに限る**」（限手術難以根治者）。[S36]
- 給付的金額感（QST 病院官方頁，2026-04-01 更新）：保險診療下重粒子線技術費攝護腺 160 萬日圓、頭頸部與骨軟部等 237.5 萬日圓，病人依健保負擔 1–3 成並適用高額療養費制度；先進醫療的技術料 344 萬日圓全額自付；自由診療技術料 **385 萬日圓（含稅）**。[S37]
- 給付範圍擴大的時間點（QST 官方公告頁）：**令和 6 年 6 月 1 日（2024-06-01）**起，原屬先進醫療的肝（肝細胞癌、肝內膽管癌）、局部進行性胰癌、大腸癌術後復發、局部進行性子宮頸腺癌，在「手術難以根治」條件下納入保險。[S38]（更早各適應症的收載年份本次未逐一查證原始公告——**gap**；QST 費用頁僅有「2022 年 4 月現在」的清單快照 [S37]。）
- **醫療觀光的關鍵事實（官方機構頁）**：QST 病院「海外からの受診について」（2026-04-17 更新）明載：**「日本の公的医療保険に加入していない外国人患者さん」**（未加入日本公的醫療保險之外國病人）費用（含稅）：適應判斷 22,000 円、初診 55,000 円、**重粒子線治療 5,786,000 円**、追蹤 22,000 円；須經身元保證機關（醫療協調者或旅行社）接洽。即：**日本健保給付適用於日本被保險人；外國病人全額自費，且費率高於日本自由診療價**。[S39]
- 同頁的規模數字（1994-06 至 2025-03 累計治療人數）：攝護腺 5,429 人、頭頸 1,551 人、骨軟部 1,549 人、I 期肺癌 1,317 人、胰 1,082 人、肝 986 人、大腸術後復發 887 人。[S39]

## Key facts — 台灣的四技術現況

- **質子——健保給付已從草案變成現行條文（重大更新）**：「全民健康保險醫療服務給付項目及支付標準」114 年第 4 次修正，**自 115-01-01（2026-01-01）生效**，新增三項：
  - 36025B 低度生物等效劑量質子放射治療（676,111 點）
  - 36026B 中度生物等效劑量質子放射治療（1,030,540 點）
  - 36027B 高度生物等效劑量質子放射治療（1,266,499 點）
  - 三項第一條註記皆為「**適用範圍：年齡未滿十九歲病人**」且符合各自條件（36025B：威爾姆氏腫瘤、何杰金氏淋巴瘤或神經母細胞瘤接受治癒性劑量，或 BED<40 GyE；36026B：惡性軟組織肉瘤（骨肉瘤除外）、非何杰金氏淋巴瘤或生殖胚芽瘤，或 40≤BED<72 GyE；36027B：中樞神經腫瘤全顱脊髓照射、眼部腫瘤、骨肉瘤，或 BED≥72 GyE）；皆須**事前審查**、每人每原發性癌症**終生限給付一次**、療程包裹給付。[S23]
  - 即：**成人質子治療不在健保給付範圍**，實務上自費；兒童青少年（<19 歲）自 2026-01-01 起有條件給付。
- 質子與重粒子設備分布（衛福部醫事司「全國醫用粒子治療設備設置現況」頁，資料建檔／更新 113-12-11，頁面最後更新 115-08-28）：質子設備 13 家——**營運中 4 家**（臺北醫學大學附設醫院、林口長庚、中國醫藥大學附設醫院、高雄長庚），設置中 9 家；重粒子設備 3 家——**營運中 1 家（臺北榮民總醫院）**，設置中 2 家（中國醫藥大學附設醫院、花蓮慈濟）。**注意資料時間戳是 2024-12-11**，寫作時標註「衛福部頁面資料日期」。[S22]
- **重粒子——健保零給付項目**：健保署開放資料「醫療服務給付項目及支付標準現行給付項目」全表（資源版本標記 1140501 生效，2026-08-29 下載）檢索「重粒子」→ **0 筆**；114 年第 4 次修正全文亦無任何重粒子項目 [S23][S24]。臺北榮總重粒子中心的**官方公告自費價格：未查得**（院方「常見問題」頁無費用資訊，[S52] FAIL）；退輔會頁面（112-10-26）僅載明重粒子治療「非屬醫療必須健保不給付醫療項目補助範疇」，須簽自費同意書 [S54]。→ 費用寫法依紅線 4：「向該院醫務課確認」。
- **BNCT**：台灣的身分是**臨床試驗＋恩慈（專案）使用**，不是常規醫療：
  - 試驗：ClinicalTrials.gov 檢索（boron neutron capture＋Taiwan，2026-08-29）現有招募中試驗 NCT06952868（復發頭頸癌）、NCT07003139（惡性腦瘤），另有已完成之 NCT01173172（復發頭頸癌）等。[S42]
  - 恩慈：Wang 等（J Chin Med Assoc 2026;89(2):109-115，開放取用）回溯報告 2020–2024 年在清華大學開放水池式反應器（THOR）**於臨床試驗之外**以恩慈方式治療 10 位復發鼻咽癌病人（1 年整體存活 44.4%）；文中並載明 THOR「至 2024 年為止是全國唯一用於 BNCT 的超熱中子源」，及台灣自 2010 年起的頭頸癌 BNCT 試驗歷史。[S41]
  - 台灣**沒有**BNCT 硼藥物之藥品許可證（本簡報未檢索台灣藥證資料庫——藥證細節與清大加速器／醫材許可證屬 N6 主場，由 C 組查證；此處僅需「試驗＋恩慈」的身分定位）。
- **FLASH**：台灣**連臨床試驗都沒有**——ClinicalTrials.gov 檢索（FLASH radiotherapy＋地點 Taiwan，2026-08-29）僅回傳 2 筆與 FLASH 放療無關的藥物試驗，**零筆 FLASH 放療試驗**。[S43] 全球人體資料仍在可行性階段：FAST-01（首個人體 FLASH 試驗，10 人、骨轉移緩和照射 8 Gy 單次、≥40 Gy/s）[S44]；2026 年的回顧仍寫「目前多數質子 FLASH 研究仍限於可行性與前臨床」[S49]。

## Claim ceiling（N2）

Defensible：
- 「『核准』在不同體系指不同的事：美國的質子機是以『與既有機器實質等同』的 510(k) 程序核可的第二級醫材（21 CFR 892.5050），FDA 的資料庫裡有 92 筆這類核可、零筆 PMA——所以『FDA 核准質子治療某癌症』這句話在制度上不存在。歐盟的 CE 標章證明符合安全與性能要求，也不是按癌別發的。台灣的醫材許可證（醫療器材管理法第 25 條）是查驗登記，同樣是器材身分。」
- 「『給付』是另一關：日本把 BNCT（2020 年 6 月起，限無法切除之局部晚期或局部復發頭頸癌）與多個質子／碳離子適應症納入健保，但同一份官方清單的多數項目都掛著『限手術難以根治者』；台灣健保 2026 年 1 月 1 日起給付質子，但限未滿十九歲、事前審查、終生一次；重粒子在台灣健保是零項目。」
- 「『有效』是第三關：給付與核准都不等於『優於標準治療』——日本 BNCT 的藥證是拿第二期單臂試驗（JHN002）加上市後全數登錄調查換來的；特管辦法的核准要件是文獻報告與安全管理，不是隨機試驗。」
- 「同一個技術在四個地方可以有四種身分：BNCT 在日本有藥證有給付、在台灣是試驗與恩慈、在美國查無核准藥證、在歐盟查無核准紀錄。所以『在國外已經核准』這句話，永遠要問：哪一國？核准的是什麼？給付了沒有？」
- 醫療觀光段：「日本的健保價目表適用於日本的被保險人。QST 病院官方網頁對未加入日本公的醫療保險的外國病人開出的重粒子治療費是 5,786,000 日圓（含稅、不含身元保證機關費用）——同一台機器，身分不同，價錢不同。」

Would overstate：
- ✗「特管辦法＝政府認證有效」——條文內容是施行計畫、安全通報與年度報告 [S17]。
- ✗「日本給付＝日本認為它比標準治療好」——給付清單掛著「限手術難以根治者」的但書 [S36]，且歐洲同儕的白皮書明言日本的給付路徑接受出版紀錄而非隨機試驗 [S40]。
- ✗「美國 FDA 沒核准＝美國認為無效」——器材本來就不走逐癌別核准；不可把制度差寫成否定。
- ✗「台灣健保給付質子＝質子在兒癌優於光子已被證明」——給付條文是政策決定；本簡報未查證兒癌比較證據（屬 N3 主場）。
- ✗「重粒子在台灣沒給付＝以後也不會給付」——只能寫查證日的狀態。
- ✗ 把 MOHW 設備清單（資料日 2024-12-11）寫成「現在共有 X 家營運中」而不標日期。
- ✗「外國人在日本治療都是 578.6 萬日圓」——那是 QST 一家的公告價；其他院所各自定價，不可外推。

## Caveats / safety notes（N2）

- **紅線 5**：本簡報為查證需要記錄了具體醫院與廠商名（臺北榮總、QST、Stella Pharma、Sumitomo、Mayo、各質子廠牌）。**正文除法規文件與官方公告之機構名（衛福部、健保署、FDA、EMA/歐盟、厚勞省/PMDA）外，一律不得點名**；台灣設備現況寫「衛福部公告全國質子設備 13 家（4 家營運中）、重粒子 3 家（1 家營運中）」即可，不列院名。QST 的數字寫「日本國立量子科學技術研究開發機構所屬醫院之公告」（政府機構，屬官方公告可引）——但仍避免把它寫成推薦。
- 恩慈／專案不是「後門」：藥事法 48-2 的前提是「危及生命或嚴重失能且國內尚無適當藥品或合適替代療法」，且主管機關可隨時廢止 [S18]。寫作時不可暗示讀者「去申請恩慈就拿得到」。
- 日本保險收載清單會變動（2026-06 更新的清單已比 2024 年多出早期肺癌與大腸癌肺轉移）；所有日本給付敘述必須帶「2026 年 6 月更新的學會清單」這類時間戳。
- 台灣質子給付三項的適應症分層（BED 三檔）技術性很強，正文只需寫「未滿十九歲、特定條件、事前審查、終生一次」；不要抄 BED 門檻，避免讀者自行對號入座。
- FLASH 段落（紅線 2）：台灣零試驗這件事必須寫成「目前在台灣沒有任何臨床可及路徑，包括試驗」，並接「這代表：有人向你推銷 FLASH，就跨過了本專題的收錄門檻」。
- 「四地對照表」中所有 unknown 格，正文處理方式是不寫或明寫查無，**不可**用「應該也是」補格。

## Taiwan status（N2 彙整）

- 五種身分的法源全部取得現行條文：[S16][S17][S18][S19][S20][S21]。
- 質子健保三項：已生效（2026-01-01），條文全文在手 [S23]。
- 重粒子：健保零項目 [S23][S24]；官方公告自費價：gap [S52]；補助範疇外之公文 [S54]。
- BNCT：試驗＋恩慈 [S41][S42]；藥證資料庫檢索：gap（N6 主場）。
- FLASH：零試驗 [S43]。
- 再生雙法：2026-01-01 施行 [S20][S21]；與特管辦法的分工細節：gap。
- 特管辦法 114-12-31 修正的修正內容對照表：gap（僅有現行整併條文）。

---

## 四地對照表（每格＝法規身分／給付身分，as-of 日期＝查證所得之來源日期）

**質子（proton）**

| | 法規身分 | 給付身分 |
|---|---|---|
| 台灣 | 醫療器材（醫療器材管理法 §25 查驗登記制）[S19]；全國設備 13 家、營運中 4 家（衛福部頁，資料日 2024-12-11）[S22] | 健保 36025B–36027B 三項，**限未滿 19 歲**、事前審查、終生一次，2026-01-01 生效；成人自費 [S23] |
| 美國 | Class II 醫材（21 CFR 892.5050），510(k) 實質等同核可，92 筆、零 PMA（openFDA，2026-08-29）[S25][S26][S27] | **unknown／gap**——美國保險給付因保險人而異，本次未取得可引用之統一官方來源 |
| 歐盟 | CE 標章＝符合 MDR 安全與性能要求（MDR Art. 5、20，合併版 2025-01-10）[S31] | 各會員國各自決定；**gap**（無單一官方清單） |
| 日本 | 醫療器材（PMDA 體系）；**本次未逐一查證質子系統藥機法核准文件——gap** | 保險收載適應症清單（JASTRO，2026-06 更新）：小兒腫瘤、攝護腺、頭頸（部分）、早期肺癌＊、肝＊胰＊大腸術後復發＊等，＊限手術難根治 [S36] |

**碳離子／重粒子（carbon）**

| | 法規身分 | 給付身分 |
|---|---|---|
| 台灣 | 醫療器材；設備 3 家、營運中 1 家（衛福部頁，資料日 2024-12-11）[S22]；台北有臨床運轉中心（2026 白皮書）[S40] | **健保零項目**（現行給付項目全表檢索 0 筆，2026-08-29）[S23][S24]；官方公告自費價未查得 [S52]；非屬健保不給付項目補助範疇（退輔會，2023-10-26）[S54] |
| 美國 | **零家臨床運轉中心**；第一家興建中（2026 白皮書）[S40]；510(k) 資料庫「carbon ion」0 筆（2026-08-29）[S28] | 不適用（無中心可給付） |
| 歐盟 | 臨床運轉中心存在（德、義、奧等，2026 白皮書）[S40]；CE 制度同上 [S31] | 各國不同；白皮書：歐洲給付體系通常要求隨機試驗等級證據 [S40] |
| 日本 | 運轉中（QST 等；1994 年起）[S39][S40] | 保險收載多項（JASTRO 2026-06 清單；技術費攝護腺 160 萬、頭頸骨軟部 237.5 萬日圓）[S36][S37]；2024-06-01 擴大（肝胰大腸術後復發子宮頸腺癌，限手術難根治）[S38]；清單外：先進醫療（技術料 344 萬自付）或自由診療（385 萬）[S37]；外國無日本健保者全額自費（一機構公告價 5,786,000 円）[S39] |

**FLASH**

| | 法規身分 | 給付身分 |
|---|---|---|
| 台灣 | **零臨床路徑：連註冊試驗都沒有**（ClinicalTrials.gov 檢索 0 筆，2026-08-29）[S43] | 無 |
| 美國 | 臨床試驗階段（FAST-01，NCT04592887，10 人可行性）[S44]；無任何 FLASH 器材核可（openFDA 0 筆，2026-08-29）[S28]；試驗用器材身分＝IDE [S29] | 無（試驗） |
| 歐盟 | 臨床試驗階段（2026 回顧：多數研究仍在可行性與前臨床）[S49]；**CE 標章 FLASH 臨床產品：unknown**（EUDAMED 未能查詢——gap） | 無可引用來源——**unknown** |
| 日本 | **unknown**（本次未查得日本 FLASH 臨床試驗或核准；JASTRO 保險與先進醫療清單皆無 FLASH [S36]） | 無（清單內查無）[S36] |

**BNCT**

| | 法規身分 | 給付身分 |
|---|---|---|
| 台灣 | 臨床試驗（NCT06952868、NCT07003139 招募中等）[S42]＋恩慈使用（2020–2024 THOR 10 例文獻紀錄）[S41]；法源＝藥事法 48-2 [S18]；藥證：查無（詳細由 N6 查證——gap） | 無健保項目（未檢索到；試驗／恩慈之費用結構——gap） |
| 美國 | **無核准硼藥**（drugs@FDA「borofalan」0 筆，2026-08-29）[S28] | 無 |
| 歐盟 | **查無核准紀錄**；EMA 資料庫無法自動查詢（[S51] FAIL）；PMDA 報告載至 2019-11 未在任何國家核准 [S32] | 無可引用來源——**unknown** |
| 日本 | **藥證＋器材證齊備（2020-03）**：Steboronine（borofalan (10B)）適應症「無法切除之局部晚期或局部復發頭頸癌」＋NeuCure BNCT System [S32][S33] | **2020-06 起健保給付**（同適應症）；上市後全數登錄調查 162 人 [S34] |

---

## 圖表數據（自繪圖的開放取用參考與數值錨點）

**可參考版式的 CC-BY 開放取用論文**（自繪，不取用原圖；圖注寫「示意圖，依〔來源〕重繪」）：

- `fig-nt-depth-dose`（深度劑量曲線）：Tinganelli & Durante, *Carbon Ion Radiobiology*, Cancers 2020（MDPI，CC-BY）[S46] — 其 Figure 1A 為 X 光、質子、氦、碳的深度劑量分布（同射程之布拉格峰、重離子碎裂尾）；正文並描述碳離子在布拉格峰後有輕碎片尾巴（tail of light fragments beyond the Bragg peak）——重繪時**碳的曲線峰後不可畫成歸零**，要畫碎裂尾。
- `fig-nt-bnct`（BNCT 兩步驟機轉）：Malouff 等, *Boron Neutron Capture Therapy: A Review of Clinical Applications*, Front Oncol 2021（Frontiers，CC-BY）[S47] — 其 Figure 1 為「注射硼藥→腫瘤細胞攝取→熱中子照射→核反應」流程。
- `fig-nt-flash-time`（時間壓縮）與 `fig-nt-ladder`（證據階梯）：無需外部圖式；數值錨點見下。

**數值錨點（全部有 PASS 來源）**：

- 質子射程：治療上關心的射程區間約 1 mm 至約 30 cm（成人骨盆中線深度），對應質子能量約 11–220 MeV（Newhauser & Zhang 2015, Phys Med Biol 60(8):R155-209）[S48]。→ 深度劑量圖的橫軸畫到 30 cm 上下即有依據。
- 光子曲線形狀：淺處建量後隨深度遞減；質子／碳離子於射程末端形成布拉格峰（[S46] Fig 1 的定性形狀；[S48] 的物理敘述）。
- BNCT 反應：¹⁰B＋熱中子（<0.025 eV）→ α＋⁷Li＋2.38 MeV；高 LET 粒子能量沉積範圍 **<10 μm，約一個細胞的直徑**（[S47]）。→ 兩步驟圖的「只殺吃了硼的細胞」半徑標注用這組數字。
- FLASH 時間軸：FLASH 定義為 ≥40 Gy/s 的超高劑量率、脈衝 ≤500 ms；對照的傳統劑量率 ≤0.03 Gy/s（小鼠實驗原始定義，Favaudon 2014）[S45]。人體端：FAST-01 以 ≥40 Gy/s 給 8 Gy 單次（與標準緩和照射同處方；傳統系統約 0.03 Gy/s）[S44]。傳統分次的對照錨點：RTOG 0617 標準臂為 60 Gy、每日 2 Gy 分次（共 30 次、約 6 週）[S1]。→ 時間壓縮圖可畫「約 6 週（30 次）對比 <1 秒（劑量給完的時間尺度）」，但**不可**寫成「FLASH 治療全程不到一秒」——擺位與療程仍要時間，FAST-01 病人在治療床上的平均時間是 18.9 分鐘 [S44]。
- 證據階梯圖（`fig-nt-ladder`）各技術目前落點的支撐：FLASH＝首個人體可行性試驗 10 人 [S44]；BNCT＝日本藥證（單臂第二期＋上市後登錄）[S32][S34][S35]；質子＝隨機比較已有（肺癌一例為陰性）[S3]＋各國常規使用 [S27][S36]；碳離子＝大量單臂系列、全球 >50,000 人、隨機比較缺乏（正式引用碳離子證據結構屬 N4 主場，此圖僅標位置）[S40]。

---

## Sources

**期刊（Europe PMC REST 查證；PASS＝標題／作者／卷期頁／年／DOI 全部由 API 回傳值抄錄）**

- **[S1] PASS** — Bradley JD, Paulus R, Komaki R, Masters G, Blumenschein G, Schild S, Bogart J, Hu C, Forster K, Magliocco A, Kavadi V, et al. *Standard-dose versus high-dose conformal radiotherapy with concurrent and consolidation carboplatin plus paclitaxel with or without cetuximab for patients with stage IIIA or IIIB non-small-cell lung cancer (RTOG 0617): a randomised, two-by-two factorial phase 3 study.* The Lancet. Oncology, 16(2), 187-199 (2015). DOI: 10.1016/s1470-2045(14)71207-0。PMID 25601342；PMCID PMC4419359；isOpenAccess=N。URL: https://doi.org/10.1016/S1470-2045(14)71207-0 — Route: Europe PMC REST (EXT_ID)
- **[S2] PASS** — Bradley JD, Hu C, Komaki RR, Masters GA, Blumenschein GR, Schild SE, Bogart JA, et al. *Long-Term Results of NRG Oncology RTOG 0617: Standard- Versus High-Dose Chemoradiotherapy With or Without Cetuximab for Unresectable Stage III Non-Small-Cell Lung Cancer.* Journal of Clinical Oncology, 38(7), 706-714 (2020). DOI: 10.1200/jco.19.01162。PMID 31841363；PMCID PMC7048161；isOpenAccess=N。URL: https://doi.org/10.1200/JCO.19.01162 — Route: Europe PMC REST (EXT_ID)
- **[S3] PASS** — Liao Z, Lee JJ, Komaki R, Gomez DR, O'Reilly MS, Fossella FV, Blumenschein GR, Heymach JV, et al. *Bayesian Adaptive Randomization Trial of Passive Scattering Proton Therapy and Intensity-Modulated Photon Radiotherapy for Locally Advanced Non-Small-Cell Lung Cancer.* Journal of Clinical Oncology, 36(18), 1813-1822 (2018). DOI: 10.1200/jco.2017.74.0720。PMID 29293386；PMCID PMC6008104；isOpenAccess=N。URL: https://doi.org/10.1200/JCO.2017.74.0720 — Route: Europe PMC REST (EXT_ID)
- **[S4] PASS** — Michalski JM, Moughan J, Purdy J, Bosch W, Bruner DW, Bahary JP, Lau H, Duclos M, Parliament M, Morton G, Hamstra D, et al. *Effect of Standard vs Dose-Escalated Radiation Therapy for Patients With Intermediate-Risk Prostate Cancer: The NRG Oncology RTOG 0126 Randomized Clinical Trial.* JAMA Oncology, 4(6), e180039 (2018). DOI: 10.1001/jamaoncol.2018.0039。PMID 29543933；PMCID PMC5885160；isOpenAccess=N。URL: https://doi.org/10.1001/jamaoncol.2018.0039 — Route: Europe PMC REST (EXT_ID)
- **[S5] PASS** — Temel JS, Greer JA, Muzikansky A, Gallagher ER, Admane S, Jackson VA, Dahlin CM, Blinderman CD, Jacobsen J, Pirl WF, et al. *Early palliative care for patients with metastatic non-small-cell lung cancer.* The New England Journal of Medicine, 363(8), 733-742 (2010). DOI: 10.1056/nejmoa1000678。PMID 20818875；isOpenAccess=N。URL: https://doi.org/10.1056/NEJMoa1000678 — Route: Europe PMC REST (EXT_ID)
- **[S6] PASS** — Haun MW, Estel S, Rücker G, Friederich HC, Villalobos M, Thomas M, Hartmann M. *Early palliative care for adults with advanced cancer.* Cochrane Database of Systematic Reviews, (6), CD011129 (2017). DOI: 10.1002/14651858.cd011129.pub2。PMID 28603881；PMCID PMC6481832；isOpenAccess=N。URL: https://doi.org/10.1002/14651858.CD011129.pub2 — Route: Europe PMC REST (EXT_ID)。與乳癌專題 D 簡報使用之同一來源，本次獨立重查，SMD 0.27（0.15–0.38）等數字一致
- **[S7] PASS** — Yabroff KR, Dowling EC, Guy GP Jr, Banegas MP, Davidoff A, Han X, Virgo KS, McNeel TS, Chawla N, Blanch-Hartigan D, Kent EE, et al. *Financial Hardship Associated With Cancer in the United States: Findings From a Population-Based Sample of Adult Cancer Survivors.* Journal of Clinical Oncology, 34(3), 259-267 (2016). DOI: 10.1200/jco.2015.62.0468。PMID 26644532；PMCID PMC4872019；isOpenAccess=N。URL: https://doi.org/10.1200/JCO.2015.62.0468 — Route: Europe PMC REST (EXT_ID)。（台灣本土財務毒性研究另以 `"financial toxicity" AND Taiwan AND cancer` 及 TITLE/ABSTRACT 限縮各檢索一次，無可用之代表性研究——gap）
- **[S8] PASS** — Ramsey SD, Bansal A, Fedorenko CR, Blough DK, Overstreet KA, Shankaran V, Newcomb P. *Financial Insolvency as a Risk Factor for Early Mortality Among Patients With Cancer.* Journal of Clinical Oncology, 34(9), 980-986 (2016). DOI: 10.1200/jco.2015.64.6620。PMID 26811521；PMCID PMC4933128；isOpenAccess=N。URL: https://doi.org/10.1200/JCO.2015.64.6620 — Route: Europe PMC REST（標題檢索 → EXT_ID）
- **[S9] PASS** — Carrera PM, Kantarjian HM, Blinder VS. *The financial burden and distress of patients with cancer: Understanding and stepping-up action on the financial toxicity of cancer treatment.* CA: A Cancer Journal for Clinicians, 68(2), 153-165 (2018). DOI: 10.3322/caac.21443。PMID 29338071；PMCID PMC6652174；isOpenAccess=N。URL: https://doi.org/10.3322/caac.21443 — Route: Europe PMC REST (EXT_ID)
- **[S10] PASS** — Osarogiagbon RU, Vega DM, Fashoyin-Aje L, Wedam S, Ison G, Atienza S, De Porre P, Biswas T, Holloway JN, Hong DS, et al. *Modernizing Clinical Trial Eligibility Criteria: Recommendations of the ASCO-Friends of Cancer Research Prior Therapies Work Group.* Clinical Cancer Research, 27(9), 2408-2415 (2021). DOI: 10.1158/1078-0432.ccr-20-3854。PMID 33563637；PMCID PMC8170959；isOpenAccess=N。URL: https://doi.org/10.1158/1078-0432.CCR-20-3854 — Route: Europe PMC REST（標題檢索）
- **[S34] PASS（OA）** — Sato M, Hirose K, Takeno S, Aihara T, Nihei K, Takai Y, Hayashi T, Bando K, Kimura H, Tsurumi K, Ono K. *Safety of Boron Neutron Capture Therapy with Borofalan(10B) and Its Efficacy on Recurrent Head and Neck Cancer: Real-World Outcomes from Nationwide Post-Marketing Surveillance.* Cancers, 16(5), 869 (2024). DOI: 10.3390/cancers16050869。PMID 38473231；PMCID PMC10931064；isOpenAccess=Y。URL: https://doi.org/10.3390/cancers16050869 — Route: Europe PMC REST（關鍵字 borofalan）＋全文 XML（PMC10931064）確認「PMDA approvals in March 2020」「included for coverage by the national health insurance system in Japan in June 2020」原文。注意：2024 年有勘誤（Cancers 16(19):3297，PMID 39410052），引用時以勘誤後版本為準
- **[S35] PASS** — Hirose K, Konno A, Hiratsuka J, Yoshimoto S, Kato T, Ono K, Otsuki N, Hatazawa J, Tanaka H, Takayama K, Wada H, Suzuki M, et al. *Boron neutron capture therapy using cyclotron-based epithermal neutron source and borofalan (10B) for recurrent or locally advanced head and neck cancer (JHN002): An open-label phase II trial.* Radiotherapy and Oncology, 155, 182-187 (2021). DOI: 10.1016/j.radonc.2020.11.001。PMID 33186684；isOpenAccess=N。URL: https://doi.org/10.1016/j.radonc.2020.11.001 — Route: Europe PMC REST（作者＋關鍵字檢索）
- **[S40] PASS（OA）** — Thariat J, Letellier V, Ohno T, Yamada S, Fossati P, Orlandi E, Harrabi S, Balosso J, Gaubert G, Haghdoost S, Habrand JL, et al. *Clinical White Paper From the "Hadrontherapy for Life" Symposium—Clinical Expansion of Carbon Ion Facilities Worldwide.* International Journal of Particle Therapy, 19, 101290 (2026). DOI: 10.1016/j.ijpt.2025.101290。PMID 41510222；PMCID PMC12774709；isOpenAccess=Y。URL: https://doi.org/10.1016/j.ijpt.2025.101290 — Route: Europe PMC REST（關鍵字檢索）＋全文 XML 確認「In the USA, Mayo Clinic is building a CIRT facility in Jacksonville, Florida」「Over 50,000 patients」與歐洲給付要求隨機證據之敘述
- **[S41] PASS（OA）** — Wang LW, Hsueh Liu YW, Peir JJ, Lin KH, Lee JC, Shueng PW, Yen SH, Yang MH. *Compassionate boron neutron capture therapy for locally recurrent nasopharyngeal cancer: A retrospective study.* Journal of the Chinese Medical Association, 89(2), 109-115 (2026). DOI: 10.1097/jcma.0000000000001339。PMID 41501971；PMCID PMC12900212；isOpenAccess=Y。URL: https://doi.org/10.1097/JCMA.0000000000001339 — Route: Europe PMC REST（關鍵字 BNCT+Taiwan+compassionate）＋全文 XML（THOR 為至 2024 年全國唯一 BNCT 超熱中子源等敘述）
- **[S44] PASS** — Mascia AE, Daugherty EC, Zhang Y, Lee E, Xiao Z, Sertorio M, Woo J, Backus LR, McDonald JM, McCann C, Russell K, et al. *Proton FLASH Radiotherapy for the Treatment of Symptomatic Bone Metastases: The FAST-01 Nonrandomized Trial.* JAMA Oncology, 9(1), 62-69 (2023). DOI: 10.1001/jamaoncol.2022.5843。PMID 36273324；PMCID PMC9589460；isOpenAccess=N。ClinicalTrials.gov: NCT04592887。URL: https://doi.org/10.1001/jamaoncol.2022.5843 — Route: Europe PMC REST (EXT_ID)
- **[S45] PASS** — Favaudon V, Caplier L, Monceau V, Pouzoulet F, Sayarath M, Fouillade C, Poupon MF, Brito I, Hupé P, Bourhis J, Hall J, et al. *Ultrahigh dose-rate FLASH irradiation increases the differential response between normal and tumor tissue in mice.* Science Translational Medicine, 6(245), 245ra93 (2014). DOI: 10.1126/scitranslmed.3008973。PMID 25031268；isOpenAccess=N。URL: https://doi.org/10.1126/scitranslmed.3008973 — Route: Europe PMC REST (EXT_ID)
- **[S46] PASS（OA，CC-BY）** — Tinganelli W, Durante M. *Carbon Ion Radiobiology.* Cancers, 12(10), 3022 (2020). DOI: 10.3390/cancers12103022。PMID 33080914；PMCID PMC7603235；isOpenAccess=Y。URL: https://doi.org/10.3390/cancers12103022 — Route: Europe PMC REST（標題檢索）＋全文 XML（Figure 1 深度劑量分布、碎裂尾敘述）
- **[S47] PASS（OA，CC-BY）** — Malouff TD, Seneviratne DS, Ebner DK, Stross WC, Waddle MR, Trifiletti DM, Krishnan S. *Boron Neutron Capture Therapy: A Review of Clinical Applications.* Frontiers in Oncology, 11, 601820 (2021). DOI: 10.3389/fonc.2021.601820。PMID 33718149；PMCID PMC7952987；isOpenAccess=Y。URL: https://doi.org/10.3389/fonc.2021.601820 — Route: Europe PMC REST（標題檢索）＋全文 XML（¹⁰B(n,α)⁷Li＋2.38 MeV、<10 μm≈一個細胞直徑）
- **[S48] PASS** — Newhauser WD, Zhang R. *The physics of proton therapy.* Physics in Medicine and Biology, 60(8), R155-209 (2015). DOI: 10.1088/0031-9155/60/8/r155。PMID 25803097；PMCID PMC4407514；isOpenAccess=N（PMC 有免費全文）。URL: https://doi.org/10.1088/0031-9155/60/8/R155 — Route: Europe PMC REST（標題檢索）＋PMC HTML 全文（「range of interest typically extends from 1 mm … to about 30 cm … correspond to 11 MeV and 220 MeV」原文確認）
- **[S49] PASS（OA）** — Wang X, Zhang Y, Zhang X, Xiong Z, Xu K, Yue NJ, Ma C. *Current Advances in Proton FLASH Radiotherapy in Abdominal Cancers.* Cancers, 18(5), 758 (2026). DOI: 10.3390/cancers18050758。PMID 41827694；PMCID PMC12984422；isOpenAccess=Y。URL: https://doi.org/10.3390/cancers18050758 — Route: Europe PMC REST（關鍵字檢索）＋全文 XML（「most proton FLASH studies are limited to feasibility and pre-clinical…」）

**官方／註冊庫來源（curl 或 WebFetch 實際取得）**

- **[S11] PASS** — ClinicalTrials.gov 試驗紀錄 NCT02358031（KEYNOTE-048），eligibility criteria 原文（排除四週內接受實驗性藥物／器材者）。URL: https://clinicaltrials.gov/study/NCT02358031 — Route: ClinicalTrials.gov API v2（`/api/v2/studies/NCT02358031`，2026-08-29）
- **[S12] PASS** — National Cancer Institute. *Why Participate in a Clinical Trial?*（頁面更新 2024-11-18）。URL: https://www.cancer.gov/research/participate/clinical-trials/why-participate — Route: curl（HTTP 200）＋WebFetch 摘讀（「The study treatment may not be better than, or even as good as, the standard treatment」等原文）
- **[S13] PASS** — ClinicalTrials.gov（美國國家醫學圖書館臨床試驗註冊庫）。URL: https://clinicaltrials.gov/ — Route: 本簡報多筆檢索以其公開 API v2 完成（2026-08-29）
- **[S14] PASS（僅入口與標題）** — 衛生福利部食品藥物管理署「台灣藥品臨床試驗資訊網」。URL: https://e-sub.fda.gov.tw/ClinicalTrialInfo — Route: curl（HTTP 200；HTML `<title>` 為「台灣藥品臨床試驗資訊網 | 衛生福利部食品藥物管理署」；另確認 `…/ClinicalTrialInfo/case-search/` 公開案件頁存在）。**頁面主體為 JavaScript 渲染，選單與功能說明無法機械抽取**——正文僅寫網站名稱與網址，不描述其介面細節
- **[S15] PASS** — 醫藥品查驗中心（CDE）舊「台灣藥物臨床試驗資訊網」關站公告：「為配合衛生福利部『台灣藥品臨床試驗網』功能上線，本系統功能即日起關閉」。URL: https://www1.cde.org.tw/ct_taiwan/ — Route: curl（HTTP 200，Big5 編碼，iconv 轉碼後抄錄原文；2026-08-29）
- **[S16] PASS** — 全國法規資料庫：**藥品優良臨床試驗作業準則**（修正日期民國 109-08-28；第 1、3、4 條原文抄錄）。URL: https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=L0030056 — Route: curl（HTTP 200）。**注意：規格中「藥品優良臨床試驗準則」非正式名稱，正式名稱含「作業」二字**
- **[S17] PASS** — 全國法規資料庫：**特定醫療技術檢查檢驗醫療儀器施行或使用管理辦法**（修正日期民國 114-12-31；第 2、3、12–21、32 條與附表三原文抄錄；附表 PDF 亦下載核對）。URL: https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=L0020075 — Route: curl（HTTP 200；附表經 LawGetFile.ashx 下載 pdftotext）
- **[S18] PASS** — 全國法規資料庫：**藥事法第 48-2 條**（專案核准；條文全文抄錄）。URL: https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=L0030001&flno=48-2 — Route: curl（HTTP 200）
- **[S19] PASS** — 全國法規資料庫：**醫療器材管理法**（公布民國 109-01-15；第 25 條原文抄錄）。URL: https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=L0030106 — Route: curl（HTTP 200）
- **[S20] PASS** — 全國法規資料庫：**再生醫療法**（公布民國 113-06-19）全文＋沿革頁（行政院 114-12-30 院臺衛字第 1141035478 號令**發布定自 115-01-01 施行**）。URL: https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=L0020238 ；沿革 https://law.moj.gov.tw/LawClass/LawHistory.aspx?pcode=L0020238 — Route: curl（HTTP 200）
- **[S21] PASS** — 全國法規資料庫：**再生醫療製劑條例**（公布民國 113-06-19）全文＋沿革頁（同一行政院令定自 115-01-01 施行）。URL: https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=L0030142 ；沿革 https://law.moj.gov.tw/LawClass/LawHistory.aspx?pcode=L0030142 — Route: curl（HTTP 200）
- **[S22] PASS** — 衛生福利部醫事司「全國醫用粒子治療設備設置現況」（建檔／更新日期 113-12-11；頁面最後更新 115-08-28）。質子 13 家（營運中 4）、重粒子 3 家（營運中 1），完整院名表已抄錄於工作檔。URL: https://dep.mohw.gov.tw/DOMA/fp-3132-80794-106.html — Route: curl（HTTP 200，2026-08-29）
- **[S23] PASS** — 行政院公報（第 031 卷第 245 期）：**全民健康保險醫療服務給付項目及支付標準部分診療項目修正**（114 年第 4 次修正，自 115-01-01 生效）總說明＋修正對照表 PDF：新增 36025B／36026B／36027B 三項質子放射治療（676,111／1,030,540／1,266,499 點；限未滿十九歲、事前審查、終生一次、包裹給付；三檔適應症原文抄錄）。URL: https://gazette.nat.gov.tw/EG_FileManager/eguploadpub/eg031245/ch08/type1/gov70/num29/images/AA.pdf （HTTP 200，388,941 bytes）；同文件另掛於健保署 https://www.nhi.gov.tw/ch/dl-94480-13813b4e7a0a47f98b006aafaa0584ac-1.pdf — Route: WebSearch → curl 下載 → pdftotext → grep 原文。**乳癌 C 簡報 [S39] 之草案（2025-10-29）已由本件確認定案生效**
- **[S24] PASS（版本註記）** — 健保署開放資料「醫療服務給付項目及支付標準——現行給付項目」全表（ODS；資源說明「醫療服務給付項目1140501生效」，資料集 metadata 更新 2026-08-12；2026-08-29 下載）。檢索「重粒子」0 筆、「硼中子」0 筆；「質子」僅見自費參考項 N21301–N21308（點數 0，註記 HTA 項目）與質子幫浦抑制劑等無關條目。URL: https://data.gov.tw/dataset/9405 （檔案 https://info.nhi.gov.tw/api/iode0000s01/Dataset?rId=A21030000I-D20003-004 ）— Route: data.gov.tw API → curl 下載 ODS → 解壓 content.xml 全文檢索。**注意：此資料版本早於 2026-01-01 生效之 36025B–36027B，故其中未含該三項；質子給付以 [S23] 為準，此件僅用於證明「重粒子零項目」**
- **[S25] PASS** — 美國 eCFR（官方 API）：21 CFR 892.5050 *Medical charged-particle radiation therapy system*（Class II）。URL: https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-892/subpart-F/section-892.5050 — Route: eCFR versioner API（2026-08-01 版全文，2026-08-29 取得）
- **[S26] PASS** — U.S. FDA. *Premarket Notification 510(k)*（「demonstrate that the device to be marketed is as safe and effective, that is, substantially equivalent, to a legally marketed device」）。URL: https://www.fda.gov/medical-devices/premarket-submissions-selecting-and-preparing-correct-submission/premarket-notification-510k — Route: WebFetch（fda.gov 對 curl 回 401，WebFetch 成功）
- **[S27] PASS** — openFDA 510(k) 資料庫檢索：product_code=LHN → total 92，全部 decision「Substantially Equivalent」（最新三筆 2026-06-11／2026-04-23／2026-03-25）。URL: https://api.fda.gov/device/510k.json?search=product_code:LHN — Route: curl（2026-08-29）
- **[S28] PASS（負面查證）** — openFDA 檢索四則（2026-08-29，皆回 NOT_FOUND／0 筆）：drugs@FDA `openfda.generic_name:"borofalan"` 與 `products.active_ingredients.name:"borofalan"`；device/510k `device_name:"carbon ion"`；device/510k `device_name:"FLASH" AND product_code:LHN`；device/pma `product_code:LHN`。URL: https://api.fda.gov/ — Route: curl，查詢字串已列
- **[S29] PASS** — U.S. FDA. *Investigational Device Exemption (IDE)*（「allows the investigational device to be used in a clinical study in order to collect safety and effectiveness data」）。URL: https://www.fda.gov/medical-devices/premarket-submissions-selecting-and-preparing-correct-submission/investigational-device-exemption-ide — Route: WebFetch
- **[S30] PASS** — U.S. FDA. *Development & Approval Process | Drugs*（CDER 審查；「benefits that outweigh its known and potential risks for the intended population」）。URL: https://www.fda.gov/drugs/development-approval-process-drugs — Route: WebFetch
- **[S31] PASS** — EUR-Lex：Regulation (EU) 2017/745（MDR）合併版 02017R0745-20250110，第 5 條（上市條件、臨床評估）與第 20 條（CE marking of conformity）原文抄錄。URL: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02017R0745-20250110 — Route: curl（HTTP 200，1.6 MB HTML）
- **[S32] PASS** — 日本厚生勞動省／PMDA：*Report on the Deliberation Results — Steboronine 9000 mg/300 mL for Infusion（borofalan (10B)，Stella Pharma）*（審議結果 2020-03-03；審查報告 2020-02-06；英文官方譯本）。適應症「Unresectable, locally advanced or locally recurrent head and neck cancer」；核准條件（RMP＋全數病人使用成績調查）；SAKIGAKE 指定（2017-04）；「As of November 2019, borofalan is not approved in any country or region」。URL: https://www.pmda.go.jp/files/000237990.pdf — Route: WebSearch → curl 下載 PDF（1,364,027 bytes）→ pdftotext
- **[S33] PASS** — 日本厚生勞動省／PMDA：*Report on the Deliberation Results — NeuCure BNCT System／NeuCure BNCT Dose Engine（Sumitomo Heavy Industries）*（審議結果 2020-02-19；含兩品項之合併審查報告；8 年使用成績調查）。URL: https://www.pmda.go.jp/files/000237993.pdf — Route: curl 下載 PDF（2,420,080 bytes）→ pdftotext
- **[S36] PASS** — 公益社団法人日本放射線腫瘍学会（JASTRO）：「粒子線治療（陽子線治療，重粒子線治療）の保険適用となる疾患」（**2026 年 06 月更新**；陽子線 10 項、重粒子線 12 項清單與「限手術難根治」但書原文抄錄）。URL: https://www.jastro.or.jp/medicalpersonnel/particle_beam/2022/07/post-10.html — Route: curl（HTTP 200）
- **[S37] PASS** — 国立研究開発法人量子科学技術研究開発機構（QST）QST 病院「費用について」（掲載日 2026-04-01 更新）：保險診療技術費（前立腺 160 萬円、頭頸部・骨軟部等 237.5 萬円、1–3 割負担＋高額療養費）；先進醫療技術料 344 萬円；自由診療 385 萬円（稅込）＋保險點數×11 円；「2022 年 4 月現在」之保險適用清單快照。URL: https://www.qst.go.jp/site/hospital/patients-cost.html — Route: curl（HTTP 200；舊網址 hospital.qst.go.jp/patients/cost.html 為轉址殼頁）
- **[S38] PASS** — QST 病院「令和 6 年 6 月より新たに保険適用となる疾患について」：2024-06-01 起，肝（肝細胞癌・肝內膽管癌）、局部進行性膵癌、大腸癌術後復發、局部進行性子宮頸腺癌之重粒子線治療（限手術難根治）由先進醫療納入保險。URL: https://hospital.qst.go.jp/tekiyoukakudai.html — Route: curl（HTTP 200）
- **[S39] PASS** — QST 病院「海外からの受診について」（掲載日 2026-04-17 更新）：未加入日本公的醫療保險之外國病人費用（稅込）——適應判斷 22,000 円、初診 55,000 円、**重粒子線治療 5,786,000 円**、經過觀察 22,000 円（2025-07-01 改訂）；須經身元保證機關；並附 1994-06〜2025-03 累計治療人數表。URL: https://www.qst.go.jp/site/hospital/patients-abroad.html — Route: curl（HTTP 200）
- **[S42] PASS** — ClinicalTrials.gov API v2 檢索：query.term=boron neutron capture＋query.locn=Taiwan（2026-08-29）→ NCT06952868（RECRUITING，復發頭頸癌）、NCT07003139（RECRUITING，惡性腦瘤）、NCT06668987（COMPLETED，復發腦膜瘤）、NCT01173172（COMPLETED）、NCT02004795（UNKNOWN）。URL: https://clinicaltrials.gov/search?locn=Taiwan&term=boron%20neutron%20capture — Route: API v2
- **[S43] PASS（負面查證）** — ClinicalTrials.gov API v2 檢索：query.term=FLASH radiotherapy＋query.locn=Taiwan（2026-08-29）→ 僅 2 筆與 FLASH 放療無關之藥物試驗，**FLASH 放射治療試驗 0 筆**。URL: https://clinicaltrials.gov/search?locn=Taiwan&term=FLASH%20radiotherapy — Route: API v2
- **[S54] PASS** — 國軍退除役官兵輔導委員會：「臺北榮民總醫院重粒子癌症治療中心啟用……可否有醫療補助？」（發布 112-10-26）：重粒子治療「非屬醫療必須健保不給付醫療項目補助範疇」，未納補助、須簽自費同意書。URL: https://www.vac.gov.tw/cp-2137-154207-1.html — Route: WebFetch。（無金額資訊）

**FAIL（保留，寫作時視為查無）**

- **[S50] FAIL** — PTCOG 官方設施統計（Facilities in Operation）。已嘗試：`https://www.ptcog.site/index.php/facilities-in-operation-public`（多次 curl，皆 HTTP 503）；新站 `https://ptcog.online/facilities-in-clinical-operation/`（HTTP 200 但表格內容需登入，WP REST API 回「Please log in」）。→ 全球與美國設施數改以 [S40]（2026 年白皮書）支撐；**不可**引用 PTCOG 數字
- **[S51] FAIL** — EMA 藥品資料庫檢索 borofalan（`https://www.ema.europa.eu/en/medicines?search_api_fulltext=borofalan`）：curl 得 JS 殼頁（antibot），WebFetch 只回搜尋首頁說明。→ 歐盟 BNCT 藥證狀態寫「查無核准紀錄（2026-08）」並以 [S32] 之 2019-11 敘述輔助，不可寫成「EMA 已確認未核准」
- **[S52] FAIL** — 臺北榮總重粒子治療之**官方公告自費金額**。已檢索：院方重粒子及放射腫瘤部「常見問題」頁（wd.vghtpe.gov.tw/CIRO/Fpage.action?muid=18038&fid=16201，WebFetch：無任何費用資訊，頁面更新 2023-04-24）、退輔會頁（[S54]，無金額）、site:vghtpe.gov.tw 搜尋。媒體報導之「4 次療程約 90 萬元」**不可引用**（非官方）。→ 依紅線 4 寫「向該院醫務課確認」
- **[S53] FAIL** — 健保署「支付標準壓縮檔」現行整併全文（`https://www.nhi.gov.tw/ch/dl-99892-…-1.zip`，115-08-01 生效版）：curl 帶 UA／Referer 皆 HTTP 403；info.nhi.gov.tw 開放資料頁為 JS 渲染無法取檔連結。→ 36025B–36027B 之現行生效以 [S23]（公報定案全文）為據；「重粒子零項目」以 [S24] 佐證。**現行整併版全文未取得**，正文避免宣稱「現行條文第 X 頁」層級的細節

---

## 工作檔

原始抓取檔（法規 HTML、公報 PDF、pdftotext 輸出、API 回應）存於
`/tmp/claude-0/-home-claude/4bc50b06-d4e4-5989-80b2-34f0f02eed26/scratchpad/nt/`（session 結束即失效；關鍵原文均已抄錄於本簡報）。
