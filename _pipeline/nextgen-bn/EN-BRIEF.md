# BNCT 分組英文版撰稿指示

工作目錄：`/root/publicpage/_pipeline/nextgen-bn`

## 先讀
- `SPEC.md`（尤其第四節八條紅線、第八節查證後修正）——英文同樣受約束
- `FIXES.md`——安全查核 S1–S15 已經改在中文裡了，英文不要改回去
- `zhsrc/<slug>.html`：中文定稿。檔首四行註解是 h1／dek／lead／section／kicker
- `zhsrc/INDEX.json`：每篇的 `<h4>` 數、引用 URL 的首次出現順序、參考條目數
- 已上線的英文聲音標準：`/root/publicpage/nt-proton-en.html`、`nt-how-to-read-en.html`

## 你不用寫的東西
兩則警語、專屬排擠句、利益揭露、文末查證日期、參考清單——建置程式會自動加上。
**只翻譯正文的 `<h4>` 與 `<p>`。**

## 硬規則（違反是事實錯誤，不是文風問題）
1. **引用連結的 HTML 原封不動照抄中文的那一段**，包括 `href`、`target`、`rel` 與 `[n]`。
   出現順序必須與中文完全一致（`zhsrc/INDEX.json` 的 `cites` 就是那個順序）。
   同一個來源在中文重複引用幾次、在哪幾段，英文也要一樣。編號我最後會用程式重編，
   你照抄中文現有的號碼即可。
2. **每一個數字完全相同**，包含寫成國字的比例（「近八成」= nearly eight in ten）。
3. **保留語氣強度相同。** 「查不到」不可以寫成 "there is limited evidence"；
   「可能」不可以變成 "is"。弱化保留＝事實漂移。特別注意這幾句必須保持同樣的硬度：
   - 「查無 FDA 核准之 BNCT 藥品或器材」→ "I can find no FDA-approved BNCT drug or device"
     （不可寫成 "the FDA has not approved"）
   - 歐盟不可以寫 "the EMA has not approved"，只能寫查不到可引用的紀錄
   - 台灣的專案途徑**不得指名法條**
   - 「以病灶計」的反應率不可以寫成以人計
   - 「五年癌症專一存活率」必須保留 cause-specific 的定義說明
4. **`<h4>` 的數量與順序與中文一致**（見 INDEX.json）。標題重寫成有張力的英文，不要逐字直譯。
5. 英式拼字：tumour、randomised、oedema、oesophagus、haematological、programme、paediatric。
6. 第一人稱門診口吻。禁止 "With advances in modern medicine"、"It is important to note that" 這類套語。
7. 每篇 1,000–1,600 字（`gbm` 那篇約 1.5 倍）。忠實優先於字數。
8. **不得出現任何金額數字**（作者要求整組避開）。
9. **不得寫台北榮總以外的台灣機台，也不得提 2027 年的加速器中心。**
10. 如果你認為中文寫錯了，**不要單邊修正**——在回報裡列出來。

## 輸出格式
在本資料夾寫 `en_<批次名>.py`：

```python
# -*- coding: utf-8 -*-
EN = {}
EN["<slug>"] = dict(
 title="…",   # 英文主標，18 字以內的鉤子，不要副標
 dek="…",     # 一句話說清楚這篇解決什麼問題
 lead="…",    # 引言框，不可以是正文第一段的改寫
 body="""…""",  # 只有 <h4> 與 <p>，引用連結照抄
)
```

## 交件前自己跑這個
```python
import re, importlib, json
m = importlib.import_module("en_<批次名>")
idx = json.load(open("zhsrc/INDEX.json"))
for slug, a in m.EN.items():
    b = a["body"]
    seen = []
    for u in re.findall(r'<a href="([^"]+)" target="_blank" rel="noopener"><sup class="cit">', b):
        if u not in seen: seen.append(u)
    print(slug,
          "h4", b.count("<h4>"), "vs", idx[slug]["h4"],
          "| cites", seen == idx[slug]["cites"])
```
兩項都對才回報。
