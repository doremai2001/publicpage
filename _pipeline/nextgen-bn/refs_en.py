# -*- coding: utf-8 -*-
"""參考條目的中文敘述部分 → 英文。只改敘述，不改書目本體與連結。"""

SUB = [
 ("(22.55J Principles of Radiation Interactions 講義)", "(22.55J Principles of Radiation Interactions, lecture notes)"),
 ("ISNCT 學會網頁（非同儕審查來源）。", "ISNCT society web page (not a peer-reviewed source)."),
 ("KEGG／JAPIC 醫療用醫薬品資料庫。", "KEGG / JAPIC drug information database. "),
 ("。ステラファーマ株式会社。", " [Steboronine infusion bag 9000 mg/300 mL, borofalan(10B); in Japanese]. Stella Pharma Corporation."),
 ("PMDA 審議結果報告書。", "PMDA report on the deliberation results."),
 ("臨床試驗登錄資料（鏡像頁）。", "Clinical trial registry record (mirror page)."),
 ("國立清華大學水池式反應器（THOR）。", "National Tsing Hua University, Tsing Hua Open-pool Reactor (THOR). "),
 ("BNCT 治療現況", "BNCT treatment status"),
 ("腦瘤臨床試驗-第 1 期", "Brain tumour clinical trial, phase 1"),
 ("頭頸癌學術性臨床試驗-第 2 期", "Head and neck cancer academic clinical trial, phase 2"),
 ("肝癌學術性臨床試驗-第 1 期", "Liver cancer academic clinical trial, phase 1"),
 ("緊急治療", "Emergency treatment"),
 ("。統計至 2026 年 8 月 19 日。（BNCT 相關數據屬 THOR 所有）",
  ". Figures as of 19 August 2026. (BNCT data belongs to THOR)"),
 ("。統計至 2026 年 8 月 28 日。（BNCT 相關數據屬 THOR 所有）",
  ". Figures as of 28 August 2026. (BNCT data belongs to THOR)"),
 ("。（BNCT 相關數據屬 THOR 所有）", ". (BNCT data belongs to THOR)"),
 ("。查證時狀態為「申請中」。", ". Status at the time of checking: application pending."),
 ("學會網頁，查證日 2026 年 9 月 8 日。", "Society web page, checked 8 September 2026."),
 ("國立清華大學（2023）。", "National Tsing Hua University (2023). "),
 ("清華 BNCT 獲醫材許可證", "NTHU BNCT granted a medical device licence"),
 ("。首頁故事，2023 年 8 月 16 日。", ". University news story, 16 August 2023."),
 ("企業新聞稿，核准日 2020 年 3 月 12 日。", "Company press release; approval date 12 March 2020."),
 ("企業新聞稿，2025 年 6 月 16 日。", "Company press release, 16 June 2025."),
 ("企業新聞稿，2025 年 9 月 25 日。", "Company press release, 25 September 2025."),
 ("JG002 延長追蹤（會議摘要）", "JG002 extended follow-up (conference abstract)"),
 ("（<strong>會議摘要，非期刊全文；作者與標題未逐字查證</strong>）",
  " (<strong>conference abstract, not a full journal paper; authors and title not verified verbatim</strong>)"),
 ("（<strong>試驗計畫書，無療效結果</strong>）", " (<strong>study protocol; no efficacy results</strong>)"),
 ("Varenna 會議論文集。", "Varenna conference proceedings."),
 ("日経メディカル（2020）。", "Nikkei Medical (2020). "),
 ("頭頸部癌の治療に世界初の BNCT 用ホウ素薬剤",
  "World's first boron drug for BNCT in head and neck cancer (in Japanese)"),
 ("。薬価基準収載・発売日 2020 年 5 月 20 日。",
  ". Listed on the NHI drug price standard and launched 20 May 2020."),
 ("衛生福利部（2010）。", "Ministry of Health and Welfare, Taiwan (2010). "),
 ("關於硼中子捕獲治療設備之說明", "Statement on boron neutron capture therapy equipment (in Chinese)"),
 ("。2010 年 3 月 23 日發布（<strong>此為 2010 年的立場，引用須標年份</strong>）。",
  ". Published 23 March 2010 (<strong>this is the 2010 position; cite it with its year</strong>)."),
]


def to_en(item):
    for a, b in SUB:
        item = item.replace(a, b)
    return item
