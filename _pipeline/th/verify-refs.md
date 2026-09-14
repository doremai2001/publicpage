# 甲狀腺癌專題 — 參考資料查核報告

查核日期：2026-09-14　·　範圍：`/home/claude/th/body/*.html`（20 篇）　·　**僅回報，未修改任何檔案**

## 摘要

| 項目 | 數字 |
|---|---|
| 文章數 | 20 |
| 參考文獻總數 | 246 |
| 唯一 URL 數 | 196 |
| 經 Europe PMC 比對（標題／作者／年／期刊／卷／期／頁） | 217 |
| 經 DOI Handle API 驗證註冊狀態 | 160 |
| 經 ClinicalTrials.gov API 驗證 | 5 |
| 經 Crossref 補驗 | 3 |
| 判定 OK | 205 |
| 判定 DEFECT | 40 |
| 本環境無法驗證 | 1 |

### 查核方法

- **書目正確性**：217 筆有 PMID/DOI 者全部以 `EXT_ID:` 或 `DOI:"…"` 查詢 Europe PMC REST（`resultType=core`），逐欄比對標題、作者、年份、期刊、卷、期、頁。
- **連結可用性**：196 個唯一 URL 全部以 `curl -L` 抓取；另對 160 個 DOI 另行呼叫 `doi.org/api/handles/` 確認 handle 是否註冊（此法不受出版社擋爬蟲影響）。
- **已知誤報**：依指示不列為缺陷者，包括含 `(` 的 DOI 遭正則截斷、Europe PMC 併入 discussion/quiz 頁碼、無期號期刊、Europe PMC 回傳含 `<sub>`／`<i>` 標記的標題、以及 *Thyroid* 於 2025 年改由 SAGE 出版而 DOI 前綴由 `10.1089` 變為 `10.1177/1050725…`。

## 各項檢查結果

### 1. 書目正確性 — 通過

217 筆比對中，**標題、作者、年份、期刊、卷、期、頁全部相符**，無捏造文獻、無張冠李戴。

- **標題**：217/217 相符。工具回報的 4 筆差異全為已知誤報（`BRAF<sup>V600E</sup>`、`<i>Corrigendum to:</i>`×2、`<i>RET</i>`）。第 5 筆見缺陷 D2。
- **作者**：63 筆有列出作者者全數相符。2 筆看似不符者為法人／團體掛名（Korean Thyroid Association、Japan Association of Endocrine Surgery Task Force），屬正當寫法。
- **期刊名**：工具回報 30 筆差異，**全為正規化誤報**——Europe PMC 存的是含副標的全名（如 `Annals of oncology : official journal of the European Society for Medical Oncology`），文章寫的是通用刊名（`Annals of Oncology`）。無一筆指向錯誤期刊。
- **卷／期／頁**：214／207／214 筆比對全數相符。10 筆無期號者屬已知誤報。
- **識別碼**：DOI 與 PMID 互相一致；23 筆同時標註 PMID 與 DOI 者，兩者指向同一篇。PMCID 全數相符。

> 補充：`th-active-surveillance.html#7`（JAMA Oncology 2022;8(11):1588–1596）在 Europe PMC 無卷期頁資料，已另以 Crossref 補驗，文章所載 **8(11), 1588** 正確，是 Europe PMC 紀錄不全。`th-daily.html#16`、`th-lobectomy.html#3` 為線上先行，正確地未標卷期。

### 2. 連結可用性 — 1 項缺陷

| 結果 | 數量 | 說明 |
|---|---|---|
| HTTP 200／202／203 | 85 | 正常 |
| HTTP 403 | 109 | **非缺陷**：SAGE、OUP、Wiley、JAMA、NEJM、LWW、ASCO 等出版社擋 `curl` 的 UA。這 109 個 DOI 全數經 Handle API 確認已註冊且指向正確出版社網域。 |
| HTTP 404 | 1 | **缺陷 D1** |
| 連線失敗（000） | 2 | 本環境 egress gateway 對 `www.hpa.gov.tw` 的 TLS 無法建立信任鏈；同為 `*.gov.tw` 的 `law.moj.gov.tw` 正常。屬沙箱限制，非連結失效。 |

160 個 DOI 中 **159 個 handle 註冊正常**，解析目標全部落在合法出版社網域（sagepub、elsevier、oup、springer、wiley、nejm、lww、jama…），**無任何導向不相關頁面**。

5 筆 ClinicalTrials.gov 連結全部可用，且 NCT 編號與所述試驗名稱（officialTitle）逐字相符。4 筆全國法規資料庫連結標題正確對應所引法規。

### 3. `.pdf` / `/full` 結尾 — 通過

196 個 URL 中**無任何一個**以 `.pdf` 或 `/full` 結尾。

### 4. 內文標記 ↔ 清單對應 — 通過

20 篇全數通過：

- 每篇 `<sup class="cit">[n]</sup>` 依首次出現順序恰為 1..N；
- `<ol>` 順序一致；
- **每個 `<sup>` 外層 anchor 的 href 與對應 `<ol>` 條目的 href 完全相同**（246/246）；
- 無未被引用的條目、無超出範圍的編號；
- 每個 `<sup>` 都包在 anchor 內（各篇 sup 數 = anchor 數），且全部具備 `target="_blank" rel="noopener"`。

### 5. 重複 URL — 符合預期，非錯誤

全 20 篇中僅 `th-taiwan.html` 一篇出現同篇內重複 URL：條目 **3、4、5、6** 共用 `https://info.nhi.gov.tw/INAE3000/INAE3000S01`。

逐條檢視內容，四者確為**不同文件**：

| # | 內容 |
|---|---|
| 3 | 健保用藥品項網路查詢服務（成分名查詢結果） |
| 4 | 藥品給付規定 9.86 Vandetanib（109/11/1 生效條文） |
| 5 | 藥品給付規定 9.74 Cabozantinib（甲狀腺癌段 114/8/1 生效條文） |
| 6 | 藥品給付規定 9.63 Lenvatinib 與 9.34 Sorafenib（甲狀腺癌段條文） |

因各條文的直接端點以 `.pdf` 結尾（受檢查 3 限制），共用同一 landing URL 屬既定且可接受的作法。**非缺陷。**

### 6. 跨文章一致性 — 主要問題所在

25 個被兩篇以上引用的來源中，**7 個渲染不一致**。根因是全書存在兩套並行的引用格式：

| 格式 | 樣式 | 篇數 |
|---|---|---|
| A（Vancouver，含 PMID） | `Title. Journal YYYY;Vol(Iss):pp. PMID nnnn. DOI: x` | 5（fna, nodule, overdiagnosis, pathology, staging） |
| B（APA，不含 PMID） | `Author, et al. (YYYY). Title. Journal, Vol(Iss), pp. DOI: x` | 14 |
| — | 純中文官方來源 | 1（taiwan） |

## 缺陷清單

### 會改變讀者認知者

**D1 — `th-atc.html` 條目 1：DOI 未註冊，連結對讀者是死連結（404）**

```
DOI: 10.20945/2359-4292-2026-0100
href: https://doi.org/10.20945/2359-4292-2026-0100  → HTTP 404（重試 3 次一致）
doi.org Handle API → {"responseCode":100}  = handle not found
api.crossref.org → 404
```

書目資料本身**完全正確**（經 Europe PMC 核對：Latin American Thyroid Society expert panel consensus on anaplastic thyroid cancer；Arch Endocrinol Metab 2026;70(5):e260100；作者 Califano I 等），問題純在連結——該 DOI 尚未在 DOI 系統註冊（2026 年新刊常見）。這是唯一一個讀者點下去會落空的連結，且它是該篇的第 1 號引用。

可用替代端點：PMID **42721060**／PMCID **PMC13560782**。

### 書目體例問題（不影響事實認知）

**D2 — `th-neck-dissection.html` 條目 9：標題與 Europe PMC 回傳不逐字相同**

Europe PMC 回傳：

```
The Effect of Prophylactic Central Neck Dissection on Locoregional Recurrence in
Papillary Thyroid Cancer After Total Thyroidectomy: A Systematic Review and
Meta-Analysis : pCND for the Locoregional Recurrence of Papillary Thyroid Cancer.
```

文章寫到 `…A Systematic Review and Meta-Analysis` 為止，未含後綴。

依「標題逐字照抄 Europe PMC」的體例，這構成截短；但冒號前的空格（`Meta-Analysis : pCND…`）顯示該後綴是 Springer 的 running title 被 Europe PMC 併進 title 欄的產物，與已知誤報中「頁碼併入 discussion」同類。**建議交由人工判斷是否補上**，本報告不主張逕行修改。其餘欄位（Ann Surg Oncol 2017;24(8):2189–2198、作者 Zhao W 等、DOI、PMID 27913945）全部正確。

**D3 — ATA 2025 分化型甲狀腺癌指引：16 篇引用，4 種寫法**

同一份文獻（DOI `10.1177/10507256251363120`）在 16 篇中有 4 種渲染：

| 寫法 | 篇數 | 檔案 |
|---|---|---|
| `Ringel, M.D., Sosa, J.A., et al. (2025). …Thyroid, 35(8), 841–985.` | 4 | active-surveillance#1, lobectomy#2, neck-dissection#1, surgery-risks#4 |
| `(2025). …Thyroid, 35(8), 841–985.` | 5 | ebrt#4, followup#1, rai-refractory#1, recurrence#1, tsh#2 |
| `…Thyroid 2025;35(8):841–985. PMID 40844370.` | 5 | fna#11, nodule#6, overdiagnosis#3, pathology#4, staging#1 |
| `… 2025. Thyroid, 35(8), 841–985.` | 2 | rai-days#1, rai-whether#1 |

四種寫法的書目內容都正確，差別在作者是否具名、年份位置、卷期標點、以及是否保留 PMID。這是全書最大的一致性落差。

**D4 — ATA 2015 指引：6 篇引用，2 種寫法**

DOI `10.1089/thy.2015.0020`：APA 式（lobectomy#1, neck-dissection#11, tsh#1）對上 Vancouver 式（nodule#3, pathology#6, staging#2）。後者保留 `PMID 26462967`，前者未保留。

**D5 — ATA 2025 勘誤：2 篇引用，2 種寫法**

DOI `10.1177/10507256251387671`：`followup#8` 用 APA 式、`pathology#5` 用 Vancouver 式（並保留 PMID 41182278）。

**D6 — ARROW pralsetinib 試驗：2 篇引用，HTML escaping 不一致**

DOI `10.1016/s2213-8587(21)00120-0`：`th-mtc.html#12` 寫 `The Lancet. Diabetes & Endocrinology`（裸 `&`），`th-rai-refractory.html#7` 寫 `The Lancet. Diabetes &amp; Endocrinology`。瀏覽器渲染相同，但原始碼不一致。

**D7 — 3 處裸 `&` 未跳脫為 `&amp;`（HTML 有效性）**

| 檔案 | # | 位置 |
|---|---|---|
| th-atc.html | 6 | `JAMA Otolaryngology-- Head & Neck Surgery` |
| th-daily.html | 4 | `Head & Neck` |
| th-mtc.html | 12 | `The Lancet. Diabetes & Endocrinology` |

全書其餘位置一律使用 `&amp;`。

**D8 — 同一期刊名兩種寫法**

*JAMA Otolaryngology–Head & Neck Surgery*：

- `th-atc.html#6` → `JAMA Otolaryngology-- Head & Neck Surgery`（Medline 雙連字號 + 裸 `&`）
- `th-active-surveillance.html#8`、`th-lobectomy.html#3` → `JAMA Otolaryngology–Head &amp; Neck Surgery`（連接號 + 跳脫）

同理 *Head & Neck* 在 `th-daily.html#4` 為裸 `&`、在 `th-ebrt.html#6` 為 `&amp;`。

**D9 — `th-atc.html#13` 多出一個全形空格**

與 `th-taiwan.html#7` 引用同一頁面，但 atc 版在「支付標準」與「第二部」之間多了 U+3000 IDEOGRAPHIC SPACE，taiwan 版沒有。

**D10 — 國健署癌症登記報告：6 篇引用，4 種寫法**

`https://www.hpa.gov.tw/Pages/List.aspx?nodeid=269` 在 6 處的描述不一：

| 檔案 | # | 寫法 |
|---|---|---|
| th-atc.html | 12 | 甲狀腺 C73，第 100–101 頁；查證日 2026-09-14 |
| th-mtc.html | 1 | （同上） |
| th-overdiagnosis.html | 1 | 甲狀腺，ICD-O-3 C73；表十「…」 |
| th-pathology.html | 3 | 甲狀腺，ICD-O-3 C73 |
| th-staging.html | 8 | （同上） |
| th-taiwan.html | 8 | 甲狀腺 C73，第 100–101 頁；期別統計涵蓋範圍見第貳部；查證日 2026-09-14 |

引用不同頁次／表次本身合理，但基礎描述在「甲狀腺 C73」與「甲狀腺，ICD-O-3 C73」之間搖擺，且查證日有無不一。

## 本環境無法驗證

**U1 — `www.hpa.gov.tw` 兩個 URL（涉及 7 筆引用）**

`Pages/List.aspx?nodeid=269`（6 筆）與 `nodeid=211`（1 筆）在本容器均因 TLS 信任鏈無法建立而連線失敗（`curl: (60)`）。改用 `--cacert /root/.ccr/ca-bundle.crt` 與 `agent-proxy-ca.crt` 皆無效；同屬 `*.gov.tw` 的 `law.moj.gov.tw`、`info.nhi.gov.tw`、`erss.nusc.gov.tw` 則正常。判為 egress gateway 對該主機的限制，**非連結失效**，但本次無法確認頁面內容。建議由可直連的環境補查。

## 逐筆對照表

判定說明：`OK` = 所有適用檢查通過；`DEFECT Dn` = 對應上方缺陷編號；`UNVERIFIED Un` = 本環境無法驗證。

「驗證來源」欄：`EuropePMC` = 書目逐欄比對；`DOI-handle` = 經 Handle API 確認註冊；`URL-only` = 僅檢查連結可用性與內容相符。

| 檔案 | # | 判定 | HTTP | 驗證來源 |
|---|---|---|---|---|
| th-active-surveillance.html | 1 | DEFECT D3 | 403 | EuropePMC |
| th-active-surveillance.html | 2 | OK | 200 | EuropePMC |
| th-active-surveillance.html | 3 | OK | 200 | EuropePMC |
| th-active-surveillance.html | 4 | OK | 403 | EuropePMC |
| th-active-surveillance.html | 5 | OK | 403 | EuropePMC |
| th-active-surveillance.html | 6 | OK | 403 | EuropePMC |
| th-active-surveillance.html | 7 | OK | 403 | EuropePMC |
| th-active-surveillance.html | 8 | DEFECT D8 | 403 | EuropePMC |
| th-active-surveillance.html | 9 | OK | 403 | EuropePMC |
| th-active-surveillance.html | 10 | OK | 403 | EuropePMC |
| th-active-surveillance.html | 11 | OK | 403 | EuropePMC |
| th-active-surveillance.html | 12 | OK | 200 | EuropePMC |
| th-active-surveillance.html | 13 | OK | 403 | EuropePMC |
| th-active-surveillance.html | 14 | OK | 200 | EuropePMC |
| th-active-surveillance.html | 15 | OK | 403 | EuropePMC |
| th-active-surveillance.html | 16 | OK | 403 | EuropePMC |
| th-atc.html | 1 | DEFECT D1 | 404 | EuropePMC |
| th-atc.html | 2 | OK | 403 | DOI-handle |
| th-atc.html | 3 | OK | 403 | EuropePMC |
| th-atc.html | 4 | OK | 403 | EuropePMC |
| th-atc.html | 5 | OK | 200 | EuropePMC |
| th-atc.html | 6 | DEFECT D7,D8 | 403 | EuropePMC |
| th-atc.html | 7 | OK | 200 | EuropePMC |
| th-atc.html | 8 | OK | 200 | EuropePMC |
| th-atc.html | 9 | OK | 200 | EuropePMC |
| th-atc.html | 10 | OK | 403 | EuropePMC |
| th-atc.html | 11 | OK | 403 | EuropePMC |
| th-atc.html | 12 | DEFECT D10 | 000 | URL-only |
| th-atc.html | 13 | DEFECT D9 | 403 | URL-only |
| th-atc.html | 14 | OK | 200 | URL-only |
| th-daily.html | 1 | OK | 403 | EuropePMC |
| th-daily.html | 2 | OK | 403 | EuropePMC |
| th-daily.html | 3 | OK | 403 | EuropePMC |
| th-daily.html | 4 | DEFECT D7 | 403 | EuropePMC |
| th-daily.html | 5 | OK | 200 | EuropePMC |
| th-daily.html | 6 | OK | 200 | EuropePMC |
| th-daily.html | 7 | OK | 403 | EuropePMC |
| th-daily.html | 8 | OK | 403 | EuropePMC |
| th-daily.html | 9 | OK | 200 | EuropePMC |
| th-daily.html | 10 | OK | 403 | EuropePMC |
| th-daily.html | 11 | OK | 403 | EuropePMC |
| th-daily.html | 12 | OK | 403 | EuropePMC |
| th-daily.html | 13 | OK | 403 | EuropePMC |
| th-daily.html | 14 | OK | 403 | EuropePMC |
| th-daily.html | 15 | OK | 403 | EuropePMC |
| th-daily.html | 16 | OK | 200 | EuropePMC |
| th-daily.html | 17 | OK | 200 | EuropePMC |
| th-ebrt.html | 1 | OK | 200 | EuropePMC |
| th-ebrt.html | 2 | OK | 200 | URL-only |
| th-ebrt.html | 3 | OK | 200 | URL-only |
| th-ebrt.html | 4 | DEFECT D3 | 403 | EuropePMC |
| th-ebrt.html | 5 | OK | 403 | EuropePMC |
| th-ebrt.html | 6 | OK | 403 | EuropePMC |
| th-ebrt.html | 7 | OK | 403 | EuropePMC |
| th-ebrt.html | 8 | OK | 200 | EuropePMC |
| th-ebrt.html | 9 | OK | 200 | EuropePMC |
| th-fna.html | 1 | OK | 200 | EuropePMC |
| th-fna.html | 2 | OK | 200 | EuropePMC |
| th-fna.html | 3 | OK | 403 | EuropePMC |
| th-fna.html | 4 | OK | 200 | EuropePMC |
| th-fna.html | 5 | OK | 403 | EuropePMC |
| th-fna.html | 6 | OK | 403 | EuropePMC |
| th-fna.html | 7 | OK | 200 | EuropePMC |
| th-fna.html | 8 | OK | 200 | EuropePMC |
| th-fna.html | 9 | OK | 200 | EuropePMC |
| th-fna.html | 10 | OK | 200 | EuropePMC |
| th-fna.html | 11 | DEFECT D3 | 403 | EuropePMC |
| th-fna.html | 12 | OK | 200 | EuropePMC |
| th-followup.html | 1 | DEFECT D3 | 403 | EuropePMC |
| th-followup.html | 2 | OK | 403 | EuropePMC |
| th-followup.html | 3 | OK | 403 | EuropePMC |
| th-followup.html | 4 | OK | 403 | EuropePMC |
| th-followup.html | 5 | OK | 403 | EuropePMC |
| th-followup.html | 6 | OK | 403 | EuropePMC |
| th-followup.html | 7 | OK | 202 | EuropePMC |
| th-followup.html | 8 | DEFECT D5 | 403 | EuropePMC |
| th-lobectomy.html | 1 | DEFECT D4 | 403 | EuropePMC |
| th-lobectomy.html | 2 | DEFECT D3 | 403 | EuropePMC |
| th-lobectomy.html | 3 | DEFECT D8 | 403 | EuropePMC |
| th-lobectomy.html | 4 | OK | 200 | URL-only |
| th-lobectomy.html | 5 | OK | 403 | EuropePMC |
| th-lobectomy.html | 6 | OK | 403 | EuropePMC |
| th-lobectomy.html | 7 | OK | 403 | EuropePMC |
| th-lobectomy.html | 8 | OK | 403 | EuropePMC |
| th-lobectomy.html | 9 | OK | 200 | EuropePMC |
| th-lobectomy.html | 10 | OK | 200 | EuropePMC |
| th-lobectomy.html | 11 | OK | 200 | EuropePMC |
| th-lobectomy.html | 12 | OK | 403 | EuropePMC |
| th-lobectomy.html | 13 | OK | 403 | EuropePMC |
| th-lobectomy.html | 14 | OK | 403 | EuropePMC |
| th-lobectomy.html | 15 | OK | 403 | EuropePMC |
| th-mtc.html | 1 | DEFECT D10 | 000 | URL-only |
| th-mtc.html | 2 | OK | 403 | EuropePMC |
| th-mtc.html | 3 | OK | 403 | EuropePMC |
| th-mtc.html | 4 | OK | 200 | EuropePMC |
| th-mtc.html | 5 | OK | 403 | EuropePMC |
| th-mtc.html | 6 | OK | 403 | EuropePMC |
| th-mtc.html | 7 | OK | 403 | EuropePMC |
| th-mtc.html | 8 | OK | 403 | EuropePMC |
| th-mtc.html | 9 | OK | 403 | EuropePMC |
| th-mtc.html | 10 | OK | 403 | EuropePMC |
| th-mtc.html | 11 | OK | 403 | EuropePMC |
| th-mtc.html | 12 | DEFECT D6,D7 | 200 | EuropePMC |
| th-mtc.html | 13 | OK | 403 | DOI-handle |
| th-neck-dissection.html | 1 | DEFECT D3 | 403 | EuropePMC |
| th-neck-dissection.html | 2 | OK | 403 | EuropePMC |
| th-neck-dissection.html | 3 | OK | 200 | EuropePMC |
| th-neck-dissection.html | 4 | OK | 403 | EuropePMC |
| th-neck-dissection.html | 5 | OK | 200 | EuropePMC |
| th-neck-dissection.html | 6 | OK | 403 | EuropePMC |
| th-neck-dissection.html | 7 | OK | 200 | EuropePMC |
| th-neck-dissection.html | 8 | OK | 403 | EuropePMC |
| th-neck-dissection.html | 9 | DEFECT D2 | 200 | EuropePMC |
| th-neck-dissection.html | 10 | OK | 200 | EuropePMC |
| th-neck-dissection.html | 11 | DEFECT D4 | 403 | EuropePMC |
| th-neck-dissection.html | 12 | OK | 200 | EuropePMC |
| th-neck-dissection.html | 13 | OK | 200 | URL-only |
| th-neck-dissection.html | 14 | OK | 200 | URL-only |
| th-nodule.html | 1 | OK | 403 | EuropePMC |
| th-nodule.html | 2 | OK | 200 | EuropePMC |
| th-nodule.html | 3 | DEFECT D4 | 403 | EuropePMC |
| th-nodule.html | 4 | OK | 200 | EuropePMC |
| th-nodule.html | 5 | OK | 200 | EuropePMC |
| th-nodule.html | 6 | DEFECT D3 | 403 | EuropePMC |
| th-nodule.html | 7 | OK | 200 | EuropePMC |
| th-nodule.html | 8 | OK | 200 | EuropePMC |
| th-nodule.html | 9 | OK | 200 | EuropePMC |
| th-nodule.html | 10 | OK | 200 | EuropePMC |
| th-overdiagnosis.html | 1 | DEFECT D10 | 000 | URL-only |
| th-overdiagnosis.html | 2 | OK | 200 | EuropePMC |
| th-overdiagnosis.html | 3 | DEFECT D3 | 403 | EuropePMC |
| th-overdiagnosis.html | 4 | OK | 200 | EuropePMC |
| th-overdiagnosis.html | 5 | OK | 200 | EuropePMC |
| th-overdiagnosis.html | 6 | OK | 200 | EuropePMC |
| th-overdiagnosis.html | 7 | OK | 200 | EuropePMC |
| th-overdiagnosis.html | 8 | OK | 200 | EuropePMC |
| th-overdiagnosis.html | 9 | OK | 200 | EuropePMC |
| th-overdiagnosis.html | 10 | OK | 403 | EuropePMC |
| th-pathology.html | 1 | OK | 200 | URL-only |
| th-pathology.html | 2 | OK | 403 | EuropePMC |
| th-pathology.html | 3 | DEFECT D10 | 000 | URL-only |
| th-pathology.html | 4 | DEFECT D3 | 403 | EuropePMC |
| th-pathology.html | 5 | DEFECT D5 | 403 | EuropePMC |
| th-pathology.html | 6 | DEFECT D4 | 403 | EuropePMC |
| th-pathology.html | 7 | OK | 403 | EuropePMC |
| th-pathology.html | 8 | OK | 200 | EuropePMC |
| th-pathology.html | 9 | OK | 403 | EuropePMC |
| th-rai-days.html | 1 | DEFECT D3 | 403 | EuropePMC |
| th-rai-days.html | 2 | OK | 403 | EuropePMC |
| th-rai-days.html | 3 | OK | 200 | EuropePMC |
| th-rai-days.html | 4 | OK | 403 | EuropePMC |
| th-rai-days.html | 5 | OK | 200 | URL-only |
| th-rai-days.html | 6 | OK | 200 | URL-only |
| th-rai-days.html | 7 | OK | 200 | URL-only |
| th-rai-days.html | 8 | OK | 200 | URL-only |
| th-rai-days.html | 9 | OK | 200 | URL-only |
| th-rai-days.html | 10 | OK | 200 | EuropePMC |
| th-rai-days.html | 11 | OK | 200 | EuropePMC |
| th-rai-days.html | 12 | OK | 203 | EuropePMC |
| th-rai-days.html | 13 | OK | 403 | EuropePMC |
| th-rai-days.html | 14 | OK | 403 | EuropePMC |
| th-rai-days.html | 15 | OK | 403 | EuropePMC |
| th-rai-days.html | 16 | OK | 403 | EuropePMC |
| th-rai-refractory.html | 1 | DEFECT D3 | 403 | EuropePMC |
| th-rai-refractory.html | 2 | OK | 403 | EuropePMC |
| th-rai-refractory.html | 3 | OK | 200 | EuropePMC |
| th-rai-refractory.html | 4 | OK | 200 | EuropePMC |
| th-rai-refractory.html | 5 | OK | 403 | EuropePMC |
| th-rai-refractory.html | 6 | OK | 403 | EuropePMC |
| th-rai-refractory.html | 7 | DEFECT D6 | 200 | EuropePMC |
| th-rai-refractory.html | 8 | OK | 403 | EuropePMC |
| th-rai-refractory.html | 9 | OK | 200 | EuropePMC |
| th-rai-refractory.html | 10 | OK | 200 | EuropePMC |
| th-rai-refractory.html | 11 | OK | 403 | EuropePMC |
| th-rai-refractory.html | 12 | OK | 403 | EuropePMC |
| th-rai-refractory.html | 13 | OK | 403 | EuropePMC |
| th-rai-refractory.html | 14 | OK | 403 | EuropePMC |
| th-rai-whether.html | 1 | DEFECT D3 | 403 | EuropePMC |
| th-rai-whether.html | 2 | OK | 403 | EuropePMC |
| th-rai-whether.html | 3 | OK | 403 | EuropePMC |
| th-rai-whether.html | 4 | OK | 200 | EuropePMC |
| th-rai-whether.html | 5 | OK | 200 | EuropePMC |
| th-rai-whether.html | 6 | OK | 403 | EuropePMC |
| th-rai-whether.html | 7 | OK | 403 | EuropePMC |
| th-rai-whether.html | 8 | OK | 403 | EuropePMC |
| th-rai-whether.html | 9 | OK | 200 | EuropePMC |
| th-rai-whether.html | 10 | OK | 403 | EuropePMC |
| th-rai-whether.html | 11 | OK | 403 | EuropePMC |
| th-rai-whether.html | 12 | OK | 200 | EuropePMC |
| th-rai-whether.html | 13 | OK | 403 | EuropePMC |
| th-rai-whether.html | 14 | OK | 200 | EuropePMC |
| th-rai-whether.html | 15 | OK | 200 | EuropePMC |
| th-rai-whether.html | 16 | OK | 200 | EuropePMC |
| th-recurrence.html | 1 | DEFECT D3 | 403 | EuropePMC |
| th-recurrence.html | 2 | OK | 403 | EuropePMC |
| th-recurrence.html | 3 | OK | 403 | EuropePMC |
| th-recurrence.html | 4 | OK | 403 | EuropePMC |
| th-recurrence.html | 5 | OK | 403 | EuropePMC |
| th-recurrence.html | 6 | OK | 403 | EuropePMC |
| th-recurrence.html | 7 | OK | 403 | EuropePMC |
| th-recurrence.html | 8 | OK | 403 | EuropePMC |
| th-staging.html | 1 | DEFECT D3 | 403 | EuropePMC |
| th-staging.html | 2 | DEFECT D4 | 403 | EuropePMC |
| th-staging.html | 3 | OK | 403 | EuropePMC |
| th-staging.html | 4 | OK | 403 | EuropePMC |
| th-staging.html | 5 | OK | 403 | EuropePMC |
| th-staging.html | 6 | OK | 200 | EuropePMC |
| th-staging.html | 7 | OK | 403 | EuropePMC |
| th-staging.html | 8 | DEFECT D10 | 000 | URL-only |
| th-surgery-risks.html | 1 | OK | 403 | EuropePMC |
| th-surgery-risks.html | 2 | OK | 200 | EuropePMC |
| th-surgery-risks.html | 3 | OK | 200 | EuropePMC |
| th-surgery-risks.html | 4 | DEFECT D3 | 403 | EuropePMC |
| th-surgery-risks.html | 5 | OK | 200 | EuropePMC |
| th-surgery-risks.html | 6 | OK | 403 | EuropePMC |
| th-surgery-risks.html | 7 | OK | 403 | EuropePMC |
| th-surgery-risks.html | 8 | OK | 403 | EuropePMC |
| th-surgery-risks.html | 9 | OK | 200 | EuropePMC |
| th-surgery-risks.html | 10 | OK | 200 | EuropePMC |
| th-surgery-risks.html | 11 | OK | 200 | EuropePMC |
| th-surgery-risks.html | 12 | OK | 403 | EuropePMC |
| th-surgery-risks.html | 13 | OK | 200 | EuropePMC |
| th-surgery-risks.html | 14 | OK | 200 | EuropePMC |
| th-taiwan.html | 1 | OK | 200 | URL-only |
| th-taiwan.html | 2 | OK | 200 | URL-only |
| th-taiwan.html | 3 | OK | 200 | URL-only |
| th-taiwan.html | 4 | OK | 200 | URL-only |
| th-taiwan.html | 5 | OK | 200 | URL-only |
| th-taiwan.html | 6 | OK | 200 | URL-only |
| th-taiwan.html | 7 | DEFECT D9 | 403 | URL-only |
| th-taiwan.html | 8 | DEFECT D10 | 000 | URL-only |
| th-taiwan.html | 9 | UNVERIFIED U1 | 000 | URL-only |
| th-tsh.html | 1 | DEFECT D4 | 403 | EuropePMC |
| th-tsh.html | 2 | DEFECT D3 | 403 | EuropePMC |
| th-tsh.html | 3 | OK | 403 | EuropePMC |
| th-tsh.html | 4 | OK | 403 | EuropePMC |
| th-tsh.html | 5 | OK | 403 | EuropePMC |
| th-tsh.html | 6 | OK | 403 | EuropePMC |
| th-tsh.html | 7 | OK | 403 | EuropePMC |
| th-tsh.html | 8 | OK | 403 | EuropePMC |
| th-tsh.html | 9 | OK | 403 | EuropePMC |
| th-tsh.html | 10 | OK | 200 | EuropePMC |
| th-tsh.html | 11 | OK | 403 | EuropePMC |
| th-tsh.html | 12 | OK | 403 | EuropePMC |
| th-tsh.html | 13 | OK | 403 | EuropePMC |
| th-tsh.html | 14 | OK | 200 | EuropePMC |

---

*報告產出：2026-09-14。查核未修改 `/home/claude/th/body/` 下任何檔案。*