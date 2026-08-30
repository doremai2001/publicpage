# 中英比例漂移判讀（bilingual proportion adjudication）

檢查指令：

    python3 /root/.claude/skills/synced/cancer-topic-series/scripts/check_bilingual.py \
        /home/claude/colon/body /home/claude/colon/en --show-numbers

硬性項目（引用數、逐位置 URL、參考資料條目、`<h4>` 數）全部通過：0 篇硬性不一致。
以下逐條處理 15 個「比例待判讀」旗標。

**結論：15 個全部是誤報，沒有一條是真的事實漂移。因此沒有修改任何檔案。**

誤報分成三類：

- **A 類「percentage points」**：腳本的 `percent` 正則會咬進英文的 *percentage* 這個字，
  於是 "12.2 percentage points" 被讀成比例 0.122；中文的「12.2 個百分點」則完全沒有被抓到。
  兩邊的數字其實一模一樣。共 10 條。
- **B 類「成」的解析誤差**：`ZH_CHENG` 只吃單一漢數字＋「成」，複合的「一成三」只被讀到「一成」＝0.1，
  英文寫的是 13%。共 1 條。
- **C 類 half／分之 的字面誤配**：英文 `\bhalf\b` 會抓到「後半段」「半張紙」「一倍半」這種
  非比例的用法；`ZH_FRAC` 只吃漢數字，所以「481 分之 1」沒被抓到而英文 "1 in 481" 被抓到。共 4 條。

---

## 1. biomarkers-and-family — 比例 0.002（僅英文）

- **EN**：“Among the 42,828 participants at one medical centre in Taiwan's precision medicine programme, 89 carried a pathogenic MMR variant, **a prevalence of about 1 in 481**; …”
- **ZH**：「台灣精準醫療計畫在一家醫學中心的 42,828 名參與者中，89 人帶有致病的 MMR 變異，**盛行率約 481 分之 1**；…」

**判定：誤報（C 類）。** 兩邊都是 1/481。英文的 "1 in 481" 被 `EN_IN` 折算成 0.002，
中文的「481 分之 1」用的是阿拉伯數字，`ZH_FRAC` 只認漢數字所以沒抓到，因此看起來只在英文版出現。
數字一致，不動。

## 2. bowel-recovery — 比例 0.5（僅英文）

- **EN**（`<h4>`）：“Will there be a bag, and when does it come down? **The second half** I can't answer”
- **ZH**（`<h4>`）：「袋子會不會裝？什麼時候關？**後面這一題**我答不出來」

**判定：誤報（C 類）。** 這裡的 "half" 指的是「兩個問句裡的後面那一個」，不是比例。
中文寫「後面這一題」，語意相同。不動。

## 3. ctdna-mrd — 比例 0.011（僅英文）

- **EN**：“Chemotherapy use in the ctDNA-guided arm fell from 28% to 15%, two-year recurrence-free survival was 93.5% against 92.4%, **an absolute difference of 1.1 percentage points** (95% CI −4.1 to 6.2), inside the tolerance, so non-inferiority was met [4].”
- **ZH**：「結果 ctDNA 導向組的化療使用率從 28% 降到 15%，兩年無復發存活 93.5% 對 92.4%，**絕對差 1.1 個百分點**（95% CI −4.1 到 6.2），落在容忍範圍內，達到非劣性 [4]。」

**判定：誤報（A 類）。** 兩邊都是 1.1 個百分點。不動。

## 4. exercise-recurrence — 比例 0.064（僅英文）

- **EN**：“In absolute terms: five-year disease-free survival 80.3% against 73.9%, **a difference of 6.4 percentage points** (0.6–12.2) [1].”
- **ZH**：「換成絕對數字：五年無病存活 80.3% 對 73.9%，**相差 6.4 個百分點**（0.6–12.2） [1]。」

**判定：誤報（A 類）。** 不動。

## 5. exercise-recurrence — 比例 0.071（僅英文）

- **EN**：“The hazard ratio for death was 0.63 (0.43–0.94), and eight-year overall survival 90.3% against 83.2%, **a difference of 7.1 percentage points** (1.8–12.3) [1].”
- **ZH**：「死亡的風險比是 0.63（0.43–0.94），八年整體存活 90.3% 對 83.2%，**相差 7.1 個百分點**（1.8–12.3） [1]。」

**判定：誤報（A 類）。** 不動。

## 6. first-month — 比例 0.13（僅英文）

- **EN**：“A hazard ratio is the ratio of the rates at which events occur in two groups: **1.13 means 13% faster**, 2.46 means about one and a half times faster.”
- **ZH**：「風險比是兩組事件發生速度的比值，**1.13 代表快一成三**，2.46 代表快一倍半。」

**判定：誤報（B 類）。** 「一成三」＝13%，與英文相同。腳本的 `ZH_CHENG` 只吃到「一成」＝0.1，
所以中文那一版被折算成 0.1、英文被折算成 0.13。數字一致，不動。

## 7. first-month — 比例 0.5（僅英文）

- **EN**：“…1.13 means 13% faster, **2.46 means about one and a half times faster**.”
- **ZH**：「…1.13 代表快一成三，**2.46 代表快一倍半**。」

**判定：誤報（C 類）。** "one and a half times" 對「一倍半」，是同一個說法；
`EN_HALF` 咬到片語裡的 "half" 才折算成 0.5。不動。

## 8. immunotherapy-dmmr — 比例 0.122（僅英文）

- **EN**：“**The extra 10.1 percentage points of disease-free survival is bought with an extra 12.2 percentage points of serious adverse events**, and those two numbers have to be read together.”
- **ZH**：「**多出來的 10.1 個百分點無病存活，換的是多出來的 12.2 個百分點嚴重不良事件**——這兩個數字要一起看。」

**判定：誤報（A 類）。** 兩邊都是 10.1 與 12.2 個百分點。不動。

## 9. lymph-node-yield — 比例 0.07（僅英文）

- **EN**：“The authors write honestly that COLOR used a non-inferiority design — you agree a boundary first (**"laparoscopy being up to 7 percentage points worse is still acceptable"**), then check whether the upper limit of the confidence interval around the difference goes past it.”
- **ZH**：「作者很誠實地寫下，COLOR 用的是非劣性設計——先講定**「腹腔鏡最多差到 7 個百分點還算可以接受」**這條界線，再看差異的信賴區間上限有沒有超過它。」

**判定：誤報（A 類）。** 不動。

## 10. malignant-polyp — 比例 0.068（僅英文）

- **EN**：“**An absolute difference of 6.8 percentage points in recurrence**, and no difference at all in survival: an awkward result like that deserves saying as it stands, rather than half of it quoted.”
- **ZH**：「復發率一邊 2.2%、一邊 9.0%，**絕對差是 6.8 個百分點**；可是無轉移存活與總存活都看不出差別。這種尷尬的結果值得原樣講出來，而不是挑一半講。」

**判定：誤報（A 類）。** 不動。

## 11. reading-stage-report — 比例 0.5（僅英文）

- **EN**：“"Doctor, what stage am I?" The question usually comes with **half a sheet of paper** behind it, printed with something like pT3 N1b (2/16) M0…”
- **ZH**：「「醫師，我是第幾期？」這句話後面通常還跟著**半張紙**，上面印著 pT3 N1b (2/16) M0…」

**判定：誤報（C 類）。** 「半張紙」對 "half a sheet of paper"，是實物不是比例。不動。

（本篇 `--show-numbers` 另有 en-only=['60']：英文寫 "1.60 means deaths happen 60% faster,
not that 60% more people die"，中文寫「1.60 的意思是死亡『發生得快 6 成』，不是『多死六成的人』」，
6 成＝60%，同樣是慣例差異。）

## 12. stage-ii-chemo — 比例 0.036（僅英文）

- **EN**（`<h4>`）：“**Three point six percentage points**”；內文：“The authors converted it themselves: assuming a five-year mortality of 20% without chemotherapy, **an absolute survival improvement of 3.6 percentage points**, 95% confidence interval 1.0 to 6.0 percentage points [1].”
- **ZH**（`<h4>`）：「**QUASAR 算出來的是三點六個百分點**」；內文：「作者自己換算過：在「不化療的五年死亡率是 20%」這個假設下，這相當於**絕對存活改善 3.6 個百分點**，95% 信賴區間 1.0 到 6.0 個百分點 [1]。」

**判定：誤報（A 類）。** 不動。

## 13. stage-ii-chemo — 比例 0.06（僅英文）

- **EN**：“…an absolute survival improvement of 3.6 percentage points, **95% confidence interval 1.0 to 6.0 percentage points** [1].”
- **ZH**：「…這相當於絕對存活改善 3.6 個百分點，**95% 信賴區間 1.0 到 6.0 個百分點** [1]。」

**判定：誤報（A 類）。** `PCT` 咬到 "6.0 percentage" 才生出 0.06。不動。

## 14. surveillance-intensity — 比例 0.05（僅英文）

- **EN**：“A microsimulation analysis recomputed FACS, GILDA and COLOFOL: … **the mortality reduction those trials could have expected to see was under 5 percentage points** and their statistical power below 10% …[5]”
- **ZH**：「一份微模擬分析把 FACS、GILDA 與 COLOFOL 重算了一遍：在合理的轉移切除療效假設下，這三個試驗預期能看到的**死亡率下降幅度不到 5 個百分點**，統計檢定力都低於 10%……[5]」

**判定：誤報（A 類）。** 不動。

## 15. three-or-six-months — 比例 0.017（僅英文）

- **EN**（`<h4>`）：“**T4 or N2: three more months buys 1.7 percentage points**”；內文：“**What three extra months buys a high-risk patient is 1.7 percentage points.**”
- **ZH**（`<h4>`）：「**T4 或 N2 的人，多做三個月換到 1.7 個百分點**」；內文：「高風險的人多做三個月，換到的是 **1.7 個百分點**。」

**判定：誤報（A 類）。** 不動。

---

## 附：獨立數字抽查（腳本看得到、但只做集合比對的那些數字）

方法比要求的「每篇五個」更嚴：把兩版逐個 `<p>` / `<h4>` / `<li>` 區塊對齊（16 篇的區塊數兩邊完全相同），
再逐區塊比對阿拉伯數字 token 的多重集合。共比對 **1,549 個中文版數字 token**
（biomarkers 120、bowel-recovery 44、capecitabine 95、ctdna 89、exercise 142、first-month 67、
immunotherapy 135、lymph-node 76、malignant-polyp 105、metastatic-cure 136、oxaliplatin 56、
reading-stage 121、stage-ii 89、supplements 65、surveillance 127、three-or-six 82）。

33 個區塊出現多重集合差異，逐一看過後**全部是已知的良性轉換**，沒有任何一個是數值不同：

- **民國年 → 西元年**：113→2024、114→2025、115→2026（biomarkers blk18/23、ctdna blk18、
  first-month blk13、immunotherapy blk7/15、surveillance blk18）。
- **月份寫成英文字**：「2025 年 7 月 3 日」→ "3 July 2025"、「2026 年 1 月 27 日」→ "27 January 2026"、
  「2020 年 4 月」→ "April 2020"、「2026 年 2 月」→ "February 2026"、「113 年 8 月」→ "August 2024" 等。
- **「成」↔ 百分比**：「大約四成」→ "roughly 40%"（ctdna blk14）、「三成到四成」→ "30% to 40%"
  （biomarkers blk12）、「快 6 成／六成」→ "60% faster"（reading-stage blk22）、
  「五成」→ "50%"（three-or-six blk22）、「六成」→ "six-tenths"（exercise blk17）。
- **小整數寫成英文字**：「10 人…5 人」→ "ten … five"、「4 到 6 次」→ "four to six"、「0 筆」→ "zero hits"、
  「2 倍到 9 倍」→ "two-fold to nine-fold"、「四倍多」→ "a little over four times"、
  「一百五十家中心」→ "150 centres"、「二年以上／三個月前」→ "two years or more / three months"、
  「1 例」→ "a single case"。
- **同一數字在一句裡被覆述的次數不同**（純文體差異，數值相同）：malignant-polyp blk18 中文把
  2.2% 與 9.0% 再唸一次、英文只留絕對差；lymph-node blk8 中文兩次 pN2、英文一次。
- **級別／期別寫法**：中文「第三級」「第三期」不含阿拉伯數字，英文寫 "grade 3" / "phase 3"
  （oxaliplatin blk5/blk8）。
- **區塊內語序不同**（token 集合相同，只是先後不一），約半數的差異屬於此類。

另外也把兩版「用字寫出來的比例」逐區塊對齊比過一次（一半／半數／N 分之 M／N 成／N 倍
對 half／a third／one in N／six-tenths…），沒有任何一個區塊出現兩語言講不同量的情形。
特別確認過幾個容易出事的：
「三分之一」↔ "a third"（biomarkers blk7）、「二十分之一」↔ "one-in-twenty"（immunotherapy blk1）、
「六分之一」↔ "one-in-six"（metastatic-cure blk5）、「八分之一」↔ "one in eight"（metastatic-cure blk12）、
「四分之一」↔ "a quarter"（exercise blk2）、「大約每十個…有一個」↔ "roughly one in ten"（malignant-polyp blk6）、
「一成」↔ "one in ten"（bowel-recovery blk4/5）、「十六倍」↔ "sixteen times"（supplements blk8）。

## 結果

沒有修改任何檔案。引用編號、參考資料條目、作者、年份、期刊、卷期頁、DOI、URL 全部未動。
複查（不加 `--show-numbers`）：16 篇、**0 篇硬性不一致**、15 個比例待判讀，即上列 15 個已判定的誤報。
