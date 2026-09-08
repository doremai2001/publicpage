# nextgen-bn — 狀態（2026-09-08）

## 已完成
- SPEC.md（17 篇、8 條紅線、6 張圖、第八節為查證後的規格修正）
- brief/A.md、B.md、C.md（PASS/FAIL 逐條標記，含 FAIL 專區）
- articles_a/b/d/e.py：**17 篇中文正文，27,150 字**（不含圖）
- parts.py：雙警語、本組專屬利益揭露（作者醫院沒有 BNCT）、**每篇專屬的排擠句 DISPLACE**
- 兩輪對抗式查核（安全 15 條、文風 38 條）已套用 → FIXES.md、fixes_safety.py、fixes_style.py、fixes_style2.py
- verify_refs 對 Europe PMC：第一輪 16 筆不符全部修好；剩下的是已知誤報（三本期刊 EPMC 未收、無期號期刊）
- **figs.py：六張自繪圖，中英 × 桌機/手機 = 24 檔**，manifest 在 figs-manifest.json
  - fig-bn-reaction／dose／depth／pathway／gbm／evidence
  - 自動換行（`wrap()` 估算 CJK 與拉丁字寬）、標題過長自動縮字級
  - 分類色只用 #A98722／#5C77C4／#00806B；尚無療效結果與非同期對照一律加斜線並附文字標籤
  - shoot.py 用 Chromium 把 24 檔轉 PNG 供目視檢查（figs/png/）
- figplace.py：六張圖在正文的插入點、圖說與 alt（中英）
- build_review.py：組裝審閱稿，含 renumber 與圖片內嵌

- **英文版 17 篇完成**：`en_a.py`／`en_b.py`／`en_c.py`，共用區塊在 `parts_en.py`，
  參考條目的中文敘述以 `refs_en.py` 轉英文；`build_en.py` 產出 `body/` 與 `en/` 兩側 fragment，
  `build_review_en.py` 產出 review-en.html（含英文圖）
- 三項機械查核全過：check_article_html 中英各 0 錯誤、check_bilingual 0 篇硬性不一致
- 英文譯者回頭抓到 10 處中文缺陷（E1-E10），兩邊一起改，記在 FIXES.md

## 尚未做
- [ ] 併入層：nt.html 改成卡片式、新增 nt-bn.html 與 nt-ht.html 子目錄頁（中英各一）、sitemap
- [ ] nt-ht-* 20 篇與 nt-bnct 的 backlink／tagchip 改指向各自的子目錄頁
- [ ] 上線時把 24 個 SVG 複製到 repo 根目錄
- [ ] 打包交付（他用 GitHub 網頁上傳）

## 等作者裁示
- 第 5 篇（pet）出現「台北榮總」——兩位審閱者都建議保留（是 NCT01173172 的主辦單位，
  刪掉收案條件就沒出處）。作者尚未回覆。
- 已上線的 nt-bnct.html 提到北榮 2027 加速器中心；新的 17 篇一個字都沒寫。要不要一併拿掉。

## 另案已交付
- nt-bnct.html／-en.html 的十倍價格錯誤 → 避開金額版，在他電腦
  `C:\Users\dorem\Downloads\Claude outputs\bnct-price-fix\`，等他上傳
