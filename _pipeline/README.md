# _pipeline — 專題產生器與底稿（不會被 GitHub Pages 發佈：Jekyll 略過底線目錄）

## 最重要的一條規則

**這是「建題時」的工具，不是重建管線。** 頁面一旦發佈，repo 根目錄的 HTML 就是正本
（作者會直接手改已發佈頁面：配圖、JSON-LD 修正等）。**絕對不要拿產生器重跑舊專題
蓋回去**——那會吃掉手改。產生器只用於：建新專題、或在完全理解差異的前提下做定點修復。

## 佈局

- 本目錄：`topicbuild.py`（共用 build/build_index，**不要改**）＋各專題模組
  （`colon` `breast` `nextgen` `cervix` `liver` `brt` `pel` `esoph` `gbm` `endo`，各 ×zh/en）
  ＋ `build_*.py` 驅動、`verify_*.py` 驗證、`stage_*_figs.py` 圖片插入
- 各專題底稿目錄：SPEC（含 §九 研究修正與紅線）、SPEC-EN、查證 brief（每條來源標 PASS/FAIL
  與查證路徑）、兩輪對抗式查核與 FIXES、中英 metadata、圖片 manifest、figwish。
  目前有：`colon/` `breast/` `nextgen/` `cervix/` `liver/` `brt/` `pel/` `esoph/` `gbm/` `endo/`
  `nextgen-ht/` `nextgen-bn/`。**hn 與 rc 兩專題早於本管線，無底稿。**
- 各專題的前綴與 hub（建新題前先確認不撞）：
  hn／rc／cc（colon）／bc（breast）／nt（nextgen，含 `nt-ht-` 熱治療與 `nt-bn-` BNCT 兩個分組，
  子目錄頁 `nt-ht.html`／`nt-bn.html`）／cx（cervix）／lv（liver，**hub 是 `liver.html`，
  前綴與 hub 不同名，用 `topicbuild._hub_name` 覆寫**）／brt／pel／ec（esoph，**hub 是 `ec.html`**）／
  gb（gbm，**hub 是 `gbm.html`，同樣要覆寫**）／em（endo，hub `em.html`，前綴與 hub 同名、不必覆寫）。
  **`en-` 這個前綴永遠不可用**——會與全站的 `-en.html` 英文版後綴相撞。
- 正文 fragment 與 SVG 不在此處——它們以成品形式活在 repo 根目錄，可自頁面還原。

## 新 session 的起手式

1. `git clone` 本 repo（工具與底稿隨之而來）
2. 依 cancer-topic-series skill 的流程建新專題（該 skill 另含 verify_refs / check_article_html
   / check_bilingual / check_live 等查核腳本）
3. 各 build_*.py 內的絕對路徑（/home/claude/…、staging 目錄）依當次 session 調整
4. build 前必先 `git pull`——作者會在 session 之間高頻率直接改 repo
5. 上傳落地後把本地 clone reset 對齊 origin

## 待上線草稿（`pending/`）

寫完但作者還沒決定上線的成品放在 `pending/<slug>/`，每個資料夾內含成品 HTML、
查證 brief，以及一份 README 寫明狀態、文章支點、紅線、以及「上線前還要做的事」。
**這些不是廢稿**——是等時機的稿子，每次新 session 起手時值得掃一眼。

目前：

- `pending/insight-jp-advanced/` —〈自費，但不能各做各的〉，日本先進醫療A 制度下的
  粒子線治療（醫學新知）。**中英文都已完稿、仍未上線**（2026-09-10 補上英文版並重查了
  兩件會過期的事：JASTRO 兩張清單仍是 2026 年 6 月版、厚労省実績報告仍是令和 7 年度版，
  下一版約 2026 年 12 月）。英文譯者以 report-don't-fix 抓出 12 條中文缺陷，記在同資料夾的
  `EN-REPORT.md`；**上線前要先處理其中的 D1、D2、D6、D7 四條**（見該檔）。

## 已知的路徑注意事項

`cervix.py` 的 `_STAGE` 指向建題當時的 scratchpad 絕對路徑；`stage_cervix_figs.py`
重建該 staging（剝除檔名前綴＋插入圖片標記）。新專題照抄這個模式。

`build_*.py` 對 `topics*.html`／`sitemap.xml`／既有頁的修改**不是冪等的**（卡片與 sitemap
區塊是 append）。專題上線後若只要補一張圖或改一句話，**不要重跑 build**——直接對 repo 根目錄
的成品頁做定點修改，圖片區塊照既有頁的 `<figure class="article-figure">`＋`<picture>` 版式手動插入
（`em-chemo-rt` 的第 12 張圖就是這樣補的）。
