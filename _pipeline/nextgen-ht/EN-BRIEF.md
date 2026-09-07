# 英文版撰稿指示（給協作者）

工作目錄：`/home/claude/publicpage/_pipeline/nextgen-ht`

## 先讀這三份，全部都是硬規則
1. `/home/claude/publicpage/_pipeline/colon/SPEC-EN.md` — 不漂移三原則、英式拼字、語氣
2. `/home/claude/publicpage/_pipeline/nextgen/SPEC-EN.md` — 本專題英文版的固定段落與紀律
3. `SPEC.md`（本資料夾）— 分組規格與九條紅線，英文同樣受約束

已上線的英文範例（聲音的標準）：`/home/claude/publicpage/nt-proton-en.html`、`nt-how-to-read-en.html`
已完成的英文版範例（就照這個寫法）：`articles_en.py` 裡的 `nt-ht-what`、`nt-ht-history`、`nt-ht-biology`、`nt-ht-chemo`

## 你的來源
中文定稿在 `body/<slug>.html`。**只翻譯 `<h4>`／`<p>`／`<li>` 的正文**——
檔案最前面四段（兩則警語、專屬排擠句、利益揭露）與文末的查證日期、參考資料，
由建置程式自動加上，你不要寫。

## 硬規則（違反就是事實錯誤，不是文風問題）
- **引用 URL 的出現順序必須與中文完全一致。** 用 `cite(U["key"], n)` 產生，n 依首次出現順序。
  最後我會用程式比對兩邊的 URL 順序，不一致就退回。
- **每一個數字完全相同**，包含用字寫出來的比例（「四分之一」是 one in four）。
- **每一個保留語氣強度相同。** 不可以把「這件事目前沒有定論」寫成 "evidence suggests"，
  也不可以把「可能更差」寫成 "is worse"。弱化保留＝事實漂移。
- 英式拼字：tumour、randomised、oesophagus、haematological、paediatric、programme、oedema。
- 第一人稱門診口吻。禁止 "With advances in modern medicine" 這類開場。
- `<h4>` 數量與順序與中文一致，標題重寫成有張力的英文，不要逐字直譯。
- 每篇 1,000–1,600 字。忠實優先於字數。
- **如果你認為中文寫錯了，不要單邊修正——在回報裡列出來，兩邊一起改。**

## 輸出格式
在本資料夾寫一個檔案 `en_<你的批次名>.py`，內容如下（不要 import fixes 以外的東西）：

```python
# -*- coding: utf-8 -*-
from build_ht import cite
from fixes import U, R
EN = {}
EN["<slug>"] = dict(
 title="…",            # 英文標題，簡短有鉤子，不要副標
 dek="…",              # 一句話說清楚這篇解決什麼問題
 lead="…",             # 引言框，不可以是正文第一段的改寫
 note="…",             # 文末「醫師的話」，個別化提醒＋一個具體下一步
 squeeze="…",          # 該篇專屬的排擠句（翻譯中文檔第二段那句）
 body=["<p>…</p>", "<h4>…</h4>", …],
)
```

`U` 的 key 對照：在 `fixes.py`／`articles_a.py`／`articles_c.py`／`articles_d.py`／`articles_e.py`
裡的 `U` 字典可以查到 URL 對應的 key。最快的做法是先用下面這段列出該篇中文用到的 key 與順序：

```python
import re
from fixes import U, ARTICLES
inv={v:k for k,v in U.items()}
body=''.join(ARTICLES['<slug>']['body'])
seen=[]
for u in re.findall(r'href="([^"]+)"', body):
    if u not in seen: seen.append(u)
print([(i+1, inv[u]) for i,u in enumerate(seen)])
```

## 交件前自己跑這個檢查，過了才回報
```python
import re, importlib
m = importlib.import_module("en_<你的批次名>")
from fixes import ARTICLES
def order(l):
    o=[]
    for u in l:
        if u not in o: o.append(u)
    return o
for s,v in m.EN.items():
    zu=order(re.findall(r'href="([^"]+)"', ''.join(ARTICLES[s]['body'])))
    eu=order(re.findall(r'href="([^"]+)"', ''.join(v['body'])))
    zn=sorted(re.findall(r'\d+\.?\d*', re.sub(r'href="[^"]+"','',''.join(ARTICLES[s]['body']))))
    en=sorted(re.findall(r'\d+\.?\d*', re.sub(r'href="[^"]+"','',''.join(v['body']))))
    print(s, 'URL順序', 'OK' if zu==eu else 'DRIFT',
          '| h4', ''.join(ARTICLES[s]['body']).count('<h4>'), v['body'].count if 0 else ''.join(v['body']).count('<h4>'),
          '| 字數', len(re.sub(r'<[^>]+>','',''.join(v['body'])).split()))
    print('   中文數字', zn); print('   英文數字', en)
```
數字清單不會完全相同（中文有「第十一篇」這種序數、英文寫成 the eleventh article），
但**所有臨床數據的數字必須都出現在英文那一側**。逐條看過再回報。

## 回報
一句話說明完成哪幾篇、檢查結果、以及你認為中文有問題的地方（如果有）。
