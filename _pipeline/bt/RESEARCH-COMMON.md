# 研究員共同規則（四組共用）

你是這個專題的研究員，產出一份查證 brief 給寫作者。寫作者**只能引用你標 PASS 的來源**，
所以你的 brief 決定了文章能說什麼、不能說什麼。

## 先讀
1. `/home/claude/bt/SPEC.md`（全部，特別是 §一 編輯立場、§四 紅線、你這組的篇目）
2. `/home/claude/repo/_pipeline/liver/brief-B.md` 的前 120 行——這是 brief 的格式範本
   （開頭「與 SPEC 假設不同形狀的事」、每篇 Key facts／Claim ceiling／Caveats、來源清單 PASS/FAIL 含查證路徑）

## 查證方法（硬規則）
- 期刊文獻一律走 Europe PMC REST，不走 PubMed 網頁（會 CAPTCHA）：
  `https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:<PMID>&resultType=core&format=json`
  或 `query=DOI:"10.xxxx/yyyy"` 或 `query=TITLE:"..."`。用 curl 或 python requests。
  每筆記下 title、journal、year、volume(issue)、pages、DOI、PMID、isOpenAccess，並從摘要（abstractText）
  抓出你要引用的每一個數字——**數字必須在摘要或可取得的全文裡看得到**，看不到就不能寫進 Key facts。
- 全文：Europe PMC 的 fullTextXML（`/webservices/rest/<PMCID>/fullTextXML`）對 OA 文章可用。
- 指引引官方 landing page（ESMO、ASCO、ASTRO、ESGE、JES 日本食道學會、AJCC），不引第三方 PDF。
  **NCCN 專業版對抓取回 403，不引 NCCN。**
- 台灣官方：hpa.gov.tw 常 TLS 失敗，改 mohw.gov.tw 對應頁；健保給付要抓「藥品給付規定」或
  「醫療服務給付項目及支付標準」正式條文（nhi.gov.tw 的 HTML 可能被 Cloudflare 擋，試直接 PDF 連結）。
  抓不到就標 gap，**永不推論有無給付**，媒體報導的價格不可用。
- ClinicalTrials.gov 可用 `https://clinicaltrials.gov/api/v2/studies/<NCT>` 查狀態。
- WebSearch／WebFetch 可用來找候選，但 PASS 的判定只能建立在你實際抓到的 API／官方頁內容上。
- 每個來源標 **PASS** 或 **FAIL**，寫查證路徑（Route: …）。FAIL 的留著不刪。
- 來源編號 [S1] [S2]… 全 brief 唯一。同一篇論文被多篇文章用，同一個編號。

## brief 結構
1. 標題、研究員、查證日期（2026-09-13）
2. **⚠ 與 SPEC 假設不同形狀的事**（動筆前必讀）——SPEC 裡任何一個假設被你的查證推翻或修正，列在這裡
3. 每篇文章一節：`## <slug>〈標題〉`
   - Key facts（每個數字帶 [Sn]、帶族群標籤：鱗癌／腺癌、期別、試驗名、n）
   - 反方向的資料（誠實必列）
   - Claim ceiling（可寫／不可寫，硬上限）
   - Caveats／safety notes（寫作者必寫）
   - 台灣端（給付、統計、官方資源；查不到的寫 gap）
   - 給繪圖組的數字（這篇的圖能用哪些 PASS 數字）
4. 來源清單（PASS/FAIL 逐條，含完整書目與 URL）

## 產出
寫到 `/home/claude/bt/brief/<你的組別>.md`。UTF-8、正體中文（書目資料原文）。
完成後回報：一段 300 字內的摘要——最重要的「與 SPEC 不同形狀的事」、每篇的 claim ceiling 一句、
台灣端查到與查不到的清單。

## 這個 session 的工具狀態

**PubMed MCP 工具本次不可用**（伺服器未連線），所以期刊文獻**一律走 Europe PMC REST**，
不要花時間找 PubMed MCP。WebSearch／WebFetch 可用來找候選，但 PASS 的判定只能建立在
你實際抓到的 API／官方頁內容上。

## 這個專題比前幾個多一件事

**這是三種病合寫的專題**（腦膜瘤、聽神經瘤、腦下垂體瘤），所以**每一個數字都必須帶「哪一種瘤」的標籤**，
而且不可以把某一種瘤的結論寫成三種通用。你這一組的 brief 若引用到別種瘤的資料當對照，
要在該筆明著標出來。
