# _pipeline — 專題產生器與底稿（不會被 GitHub Pages 發佈：Jekyll 略過底線目錄）

## 最重要的一條規則

**這是「建題時」的工具，不是重建管線。** 頁面一旦發佈，repo 根目錄的 HTML 就是正本
（作者會直接手改已發佈頁面：配圖、JSON-LD 修正等）。**絕對不要拿產生器重跑舊專題
蓋回去**——那會吃掉手改。產生器只用於：建新專題、或在完全理解差異的前提下做定點修復。

## 佈局

- 本目錄：`topicbuild.py`（共用 build/build_index）＋各專題模組（colon/breast/nextgen/cervix
  ×zh/en）＋ build_*.py 驅動與 verify_*.py 驗證腳本＋圖片插入 staging 腳本
- `colon/`、`breast/`、`nextgen/`、`cervix/`：各專題的 SPEC（含研究修正與紅線）、
  SPEC-EN、查證 brief（含每條來源的 PASS/FAIL 紀錄）、兩輪查核與 FIXES、
  中英 metadata、圖片 manifest。hn 與 rc 兩專題早於本管線，無底稿。
- 正文 fragment 與 SVG 不在此處——它們以成品形式活在 repo 根目錄，可自頁面還原。

## 新 session 的起手式

1. `git clone` 本 repo（工具與底稿隨之而來）
2. 依 cancer-topic-series skill 的流程建新專題（該 skill 另含 verify_refs / check_article_html
   / check_bilingual / check_live 等查核腳本）
3. 各 build_*.py 內的絕對路徑（/home/claude/…、staging 目錄）依當次 session 調整
4. build 前必先 `git pull`——作者會在 session 之間高頻率直接改 repo
5. 上傳落地後把本地 clone reset 對齊 origin

## 已知的路徑注意事項

`cervix.py` 的 `_STAGE` 指向建題當時的 scratchpad 絕對路徑；`stage_cervix_figs.py`
重建該 staging（剝除檔名前綴＋插入圖片標記）。新專題照抄這個模式。
