# EN-REPORT-D — 良性腦瘤專題 D 組（腦下垂體，4 篇）英文版審閱回報

英文版是這個專題的第三輪對抗式審閱。下面每一條都**沒有在英文裡偷偷修掉**；
英文照中文原樣翻，問題留在兩個語言裡同一個位置，請編輯一次改兩邊。
唯一一處英文多出中文沒有的字，是第 7 條的統計名詞白話解釋（SPEC-EN §5 明文要求）。

嚴重度：**甲＝安全性／事實錯誤，必須改**；乙＝規格與正文互相矛盾，要裁決；丙＝措辭風險，建議改。

---

## 甲1（最嚴重）｜`bt-pit-prolactinoma`：21% 被標成「復發率」，它其實是「維持正常的比例」

**原句（h4「停藥：醫師在評估的是這幾件事」第一段末）**
> 就算三項都成立也不代表停得住——下一段那三份資料的復發率是 21%、54% 與 63%。

**下一段自己寫的（同一篇）**
> 19 篇、743 人的統合分析算出停藥後泌乳素持續正常的合併比例只有 21%，分層是特發性 32%、微泌乳素瘤 21%、大泌乳素瘤 16%。

**問題**：Dekkers 2010（參考資料 [11]）的 21% 是**停藥後泌乳素持續正常的合併比例**，也就是成功率；
對應的復發約是 **79%**，不是 21%。另外兩個數字（Kharlip 2009 整體復發 54%、十八個月估計復發風險 63%）
才是真正的復發率。把三個並稱「復發率」，**會讓三個數字裡最不利的那一個被讀成最輕的那一個**，
而且就發生在紅線 3／修正 12 指定當護欄的那一段。

**證據它是筆誤而不是另一種讀法**：同一組的 `meta/D.json` lead 自己寫對了——
「統合分析裡只有兩成的人泌乳素能一直維持正常」。正文與自己的 lead 互相矛盾。

**連帶**：`SPEC.md` §九 修正 12 與 `SPEC-EN.md` §3 都寫「復發率（21%／54%／63%，各標族群）」，
**規格本身繼承了同一個標籤錯誤**，要一起改，否則下一輪會有人照規格把中文「改回去」。

**英文怎麼處理**：逐字照譯（"the recurrence rates in the three sets of data in the next paragraph
are 21%, 54% and 63%"），下一段也照譯（"a pooled proportion of only 21% in whom prolactin stayed
normal after withdrawal"）。兩個語言現在帶著同一個看得見的矛盾，請一次修兩邊。

---

## 甲2｜`bt-pit-surgery-rt`：38 個月是「平均」還是「中位」，中文與規格不一致

**原句**
> 371 位肢端肥大症的國際多中心資料：……而**達成持久緩解的平均時間是放射手術後 38 個月**。

`SPEC.md` §九 修正 13 與 `SPEC-EN.md` §3 兩處都寫「**中位**落差 38 個月」／"a **median** 38 months"。
中文正文寫的是「平均」。兩者必有一錯，要回 Sheehan 2019（參考資料 [11]）原文核對。
**英文照中文母本寫 "the average time"**，沒有改成 median。

---

## 甲3｜`SPEC-EN.md` §3 把兩個不同世代的垂體功能低下曲線壓成一條

`SPEC-EN.md` §3 寫「5 years 22.4% / 10 years 31.3% / 15 years 45%」，讀起來像同一條累積曲線。
中文正文是對的，而且分得很清楚：
- 22.4%（五年）／31.3%（十年）＝ 17 家機構、1,023 人的多中心資料（參考資料 [14]）；
- 20%（五年）／39%（十年）／45%（十五年）＝ 241 人的單中心資料（參考資料 [15]）。

英文照中文分開標。**請改規格的措辭**，否則下一輪會有人照規格把兩個世代合併。

---

## 乙1｜`bt-pit-apoplexy`：勝算比 0.31 的方向與「開刀較好」對不起來

**原句**
> 眼肌麻痺的恢復開刀明顯較好，勝算比 0.31（95% 信賴區間 0.10 到 0.92）。

勝算比小於 1 而「恢復較好」，只有在**模型的結果變項是「沒有恢復／持續眼肌麻痺」**，
或**參考組是開刀組**時才講得通。原句兩者都沒交代。照現在的寫法，數字與方向互相打架，
而這正是文章自己剛剛才提醒讀者「勝算比不能讀成機率差幾倍」的地方。
要補上結果變項的定義，或把勝算比倒過來寫。**英文照原樣翻。**

---

## 乙2｜`bt-pit-surgery-rt` 開頭「路只有兩條」，把藥物那條路關在門外

**原句（第一段）**
> 腦下垂體腺瘤要動手，路只有兩條：從鼻子進去拿掉，或用放射線照它。

一個泌乳素瘤的讀者從搜尋引擎直接落在這一篇，看到的第一句是「路只有兩條」，
而第一個指向〈泌乳素瘤：先吃藥不是先開刀〉的句子在第三節才出現。
紅線 3 要求「垂體瘤第一線」這件事被框起來的每一個地方，藥物例外都不能漏。
建議在第一段就補一句例外或指路（兩個語言一起補）。**英文照原樣翻，沒有自行補。**

---

## 乙3｜`bt-pit-surgery-rt`：A 到 F 條件的原文講的是「開顱手術」，垂體手術是經蝶竇

**原句（h4「台灣的條文，把放療寫在手術之後」）**
> 條文把放療的官方位置寫得很明白：手術之後，或手術做不了時。

這個結論靠的是條件 A（「曾接受**開顱手術**但有殘餘腫瘤或腫瘤復發者」）與 B
（「**開顱手術**可能造成神經損傷或危險性大者」）。但同一篇下一段自己引的手術代碼是
83057B「**經由蝶竇**之腦下垂體瘤切除」——經蝶竇手術算不算 A、B 款講的「開顱手術」，
條文本身沒有交代。固定紅線禁止推論給付有無，這一句離那條線只差一步，
而且這個推論同時撐著小節標題。建議補一句「條文的 A、B 款寫的是開顱手術，
經蝶竇手術算不算，條文看不出來」。**英文照原樣翻。**

---

## 丙1｜三篇的統計名詞在中文沒有白話解釋（SPEC-EN §5 要求逐篇首次出現就要解釋）

| 檔 | 缺解釋的名詞 | 位置 |
| --- | --- | --- |
| `bt-pit-prolactinoma` | 95% 信賴區間、發生率比、相對風險 | h4 5（瓣膜）、h4 7（懷孕） |
| `bt-pit-surgery-rt` | 95% 信賴區間、精算率／精算發生率 | h4 1、h4 4、h4 5 |
| `bt-pit-apoplexy` | 95% 信賴區間 | h4 3 |

（`bt-pit-function` 的信賴區間有解釋，寫法可以直接沿用。）

**這是全組唯一一處英文帶了中文沒有的字**：英文依 SPEC-EN §5 在上述每個位置補了一句最短的白話解釋
（例如 "a confidence interval is the range the true value plausibly sits in"）。
請把對應的中文也補上，兩版才會齊。

---

## 丙2｜修正 14「不得出現天數」的範圍要裁一次

`SPEC-EN.md` §3 把 `bt-pit-apoplexy` 的禁令寫成「no multiple, no milligram and no number of days
may appear」，**沒有限定段落**。中文母本在腎上腺功能不足那一段之外，實際存在這些數字：

- 「從躺到站收縮壓掉 **20 mmHg** 以上」（腎上腺功能不足症狀清單，指引原文的門檻）
- 「早期手術（**八天內**）視覺結果較好」（垂體中風手術時機，且已標明不是隨機證據）
- 「好發窗口是術後第**三到第十四天**」（術後低血鈉，不同時間軸）
- 追蹤「**四到六週**一次，再拉長到每**六到十二個月**一次」
- 四個問題那一段的「劑量、倍數、要吃**幾天**」——是拿來說「這幾樣要醫師寫給你」，不是給數值

以上沒有一項是類固醇劑量，也沒有一項是自行調整的指示。
我把 修正 14 讀成**只管壓力情境的類固醇那一段**，因此全部保留、照譯。
如果編輯的原意是全篇禁止，**要先從中文拿掉 mmHg 與那幾個天數**，不要只改英文。

---

## 丙3｜`bt-pit-prolactinoma` 第八節標題與 Knosp 0–1 的並列第一線互相抵消

**原標題**：〈治不動的時候，才是走向開刀的時候〉

單獨讀這一句，等於「藥沒效才開刀」，正好是修正 12 要擋掉的那個方向
（Knosp 0–1、界限清楚者，**手術也是第一線之一**）。
整篇是安全的——開頭與第一節都帶了這道護欄，這一節的內文也引了 Knosp 0–1 的手術緩解率——
**但標題單獨被引用時不安全**。建議兩個語言一起把標題的排他性放鬆。
英文照中文寫成 "When the drug stops moving it, that is when surgery comes up"。

---

## 丙4｜`bt-pit-function` 第一段的並列把「藥」排在最前面

**原句**：「分泌什麼決定第一線走哪一條——藥、刀，還是先不動」

這是選項列舉，不是順序主張，而且修正 12 的護欄在第三節完整交代了。
但這是 D 組唯一一句被抽離上下文後可以讀成「垂體瘤先吃藥」的話，而它出現在這一組的**分流篇第一段**。
只回報，兩個語言都沒有動。

---

## 丙5｜`bt-pit-apoplexy` 的重大傷病段落，與修正 6 是兩筆不同的查證結果

中文寫的是：附表一**確實列了**「尿崩症（Diabetes insipidus, E23.2）」、效期永久，
但被放在「七、先天性新陳代謝異常疾病」底下；而「腦下垂體」「垂體」「庫欣」「肢端」逐字搜尋是零筆。

這與修正 6（癌症五個子項全是 C 碼、D32／D33／D35 零筆、唯一沾邊的是脊髓病變那一條）**不衝突**，
但它是**另一筆發現**，而且是全專題唯一一處讀者可能帶走「我這個診斷也許辦得到」的地方。
中文處理得很小心（「附表的文字看不出來……一起問醫務課」），英文維持同樣強度、沒有加強也沒有放寬。
記錄下來，讓編輯決定 `bt-incidental` 的修正 6 段落要不要一起承認 E23.2 這一行。

---

## 丙6｜`bt-pit-function` 的 ICD-O 行為碼 3，與修正 5 的癌症登記論述會互相拉扯

`bt-pit-function` 寫「ICD-O 的行為碼也從代表良性的 0 改成代表原發惡性的 3」（參考資料 [5]）。
修正 5（A 組主場）寫癌症登記長表手冊「ICD-O-3 性態碼為 2、3、6、9 者均需申報」、benign(0) 不申報，
並據此說**台灣沒有良性腦瘤的官方人數**。兩句放在同一個專題裡，讀者可以推出
「那垂體瘤現在是 3，所以有申報、所以有數字」。這一題不在 D 組的權責內，只回報給編輯，
請 A 組與 D 組一起看要不要在其中一邊補一句切割。

---

## 工具誤報

**沒有。** `check_article_html.py --lang en --min 1300 --max 2500` 四篇全部 0 錯誤、0 提醒；
`check_bilingual.py`（把四對檔案放進暫存目錄跑）0 篇硬性不一致、0 個比例待判讀。
加了 `--leads` 之後 lead 與第一段的相似度也全部過關。

---

## 我寫出去的專題內交叉引用（逐句列出，供標題漂移查核）

**`bt-pit-function`**
- The full argument is in "Three tumours, three different logics".
- How position maps onto symptoms is in "Where it sits matters more than how big it is".
- That box is "Prolactinoma: the drug comes first, not the knife".
- …the fact that the measuring method decides the conclusion is in "Watching is a form of treatment".
- How far pituitary deficiency can go, and which situations count as an emergency, is in "Pituitary apoplexy, and not enough hormone".

**`bt-pit-prolactinoma`**
- Which type is which is in "First, find out whether it is secreting".
- The emergency side of all this is in "Pituitary apoplexy, and not enough hormone".
- That side of it is in "Where endonasal surgery and radiotherapy fit".

**`bt-pit-surgery-rt`**
- …when that point is reached is in "Prolactinoma: the drug comes first, not the knife".
- The emergency side of this is in "Pituitary apoplexy, and not enough hormone".
- …that question belongs to "One session, or fractionated".
- …that question is in "Protons: precise. Then what?"
- Whether irradiation grows a second tumour is in "Can radiotherapy grow a second tumour".

**`bt-pit-apoplexy`**
- This whole side of things is in "Where endonasal surgery and radiotherapy fit".

全部逐字對照 `SPEC-EN.md` §4 的正式英文標題，一律雙引號、不加連結。
