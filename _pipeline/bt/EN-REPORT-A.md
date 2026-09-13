# EN-REPORT-A — defects found while writing the English edition of group A

Report-don't-fix. Every item below was **translated into English exactly as the Chinese stands**;
nothing here was silently corrected in one language. Two exceptions are flagged explicitly as
"disclosed deviation" — both are heading rewrites, which the English spec requires anyway.

Ordered most dangerous first.

---

## A1 — `bt-watch`: an inference about Taiwanese practice drawn from a reimbursement clause, and a characterisation the same paragraph contradicts

**Sentence (final paragraph of 〈在台灣，立體定位放射手術不是第一線的預設路徑〉):**

> 翻成白話：條文把放射手術放在「開刀走不通或風險太大」之後，不是第一步，這解釋了為什麼台灣的第一步常是觀察或手術。

Two separate problems in one sentence.

1. **It is contradicted by the clause quoted immediately above it.** The paragraph itself quotes
   condition **F**: 「顱內單側小腦橋腦角聽神經瘤寬度小於 2.5 公分（不含內耳道）者」. Condition F is a
   size criterion in its own right and is **not** conditioned on surgery having failed or being too
   risky — a never-operated vestibular schwannoma under 2.5 cm satisfies it directly. So "條文把放射
   手術放在『開刀走不通或風險太大』之後" is true of A, B and C but not of F, and the article has
   already put F in front of the reader.
2. **「這解釋了為什麼台灣的第一步常是觀察或手術」 is an uncited empirical claim about practice
   patterns in Taiwan**, inferred from a payment clause. No citation supports it, and 固定紅線
   ("永不推論") plus 修正 1 ("不得以健保代碼推論") both point against reasoning from the schedule to
   anything other than what the schedule says. The defensible version is the first half of the
   sentence, restricted to conditions A to C, with the "why Taiwan does X" clause deleted.

Translated as it stands ("the provision places radiosurgery after 'surgery is not workable or is too
risky' rather than first, which explains why the first step in Taiwan is so often observation or an
operation").

## A2 — `bt-three-kinds`: the NHI stereotactic radiosurgery indications are cited without the conditions that 修正 1 makes mandatory

**Sentence (end of 〈台灣沒有這三個數字，而且那不是統計漏掉〉):**

> 倒是健保支付標準把這三種瘤寫進同一條立體定位放射手術的適應症裡——制度上同格，臨床上不同題。

修正 1 requires that wherever the 37028B/37029B indications are quoted, they carry **"且須符合下列
條件之一（A 到 F）"** and **"全部個案須事前專案向保險人申請"**. `bt-watch` does carry both;
`bt-three-kinds` carries neither. A reader who lands on the foundation article from a search engine
and reads only this sentence can take away "the NHI covers stereotactic radiosurgery for all three of
these tumours", which is exactly the inference 修正 1 exists to prevent. One clause — "但同一條接著
要求符合 A 到 F 之一，且全部個案須事前專案申請" — would close it.

Translated as it stands.

## A3 — `bt-incidental` and `bt-watch`: hearing-preservation probabilities carrying only two of the four labels 修正 10 requires

**`bt-incidental`, 〈哪些情況從一開始就不是觀察題〉:**

> 美國神經外科醫學會 2018 年的聽力保存指引指出，走觀察這條路的人到第十年還維持可用聽力的機率只剩
> 「中等偏低（超過 25% 到 50%）」

**`bt-watch`, 〈聽神經瘤的觀察，價格是聽力〉:**

> 美國神經外科醫學會的指引把觀察組維持可用聽力的機率列為第二年超過 75% 到 100%、第五年超過 50% 到
> 75%、第十年只剩超過 25% 到 50%

修正 10: 「每一個聽力保存率都必須帶：用哪一套評分系統、追蹤幾年、n、治療方式。缺一項不得進正文。」
These carry **treatment** (observation) and **follow-up length** (2/5/10 years), but **no scoring
system** and **no n**. That is the same defect FIXES 甲1 used to delete three ten-year hearing figures
from `bt-followup`. The mitigating difference is that these are single-arm (observation only) and so do
not rank the three roads, which was 甲1's other ground — but 修正 10's wording is "缺一項不得進正文",
not "不得排名次". Note also that `bt-watch` sets these bands **in the paragraph immediately after**
showing that the same 156 people score 34% or 58% depending on the ruler, which makes the missing
ruler on the guideline figures conspicuous.

Both translated as they stand. If the editor rules them out, the same deletion has to be made in both
languages in both files.

## A4 — `bt-where`: a hazard ratio with neither its outcome nor its increment

**Sentence (〈位置重要，不代表大小可以不管〉):**

> 而一個 441 人、459 顆偶然發現腦膜瘤的預後模型裡，腫瘤體積增加的風險比是 2.17（95% 信賴區間 1.53 到
> 3.09），風險比是兩組事件發生速度的比值。

A hazard ratio is uninterpretable without two things the sentence does not give:

- **the outcome** — hazard of *what*? Growth? Symptomatic progression? Receiving an intervention?
  Islim 2020 is a prognostic model for monitoring regimes, so the endpoint matters a great deal;
- **the increment** — 2.17 per what? Per cubic centimetre, per doubling, per pre-specified volume
  category? "腫瘤體積增加" names a direction, not a unit of exposure.

The gloss that follows ("兩組事件發生速度的比值") is correct in general but cannot rescue this
particular number, because there are no two named groups here.

Translated as it stands, gloss included.

## A5 — `bt-where`: 同側 where the source review very likely says "homonymous"

**Two sentences, both in the 逐個位置 list:**

> 矢狀竇旁腦膜瘤：…進展期特徵性地出現視乳突水腫與同側偏盲。

> 竇匯周圍腦膜瘤：枕部局部疼痛、視乳突水腫、同側視野缺損，加上失調與眼球震顫。

同側 means *ipsilateral*. 同向性偏盲 means *homonymous hemianopia*. A parasagittal or peri-torcular
meningioma classically produces a **contralateral homonymous** field defect, and "homonymous" is the
word the English literature uses. If Ogasawara 2021 says "homonymous hemianopia", then 同側 is a
translation slip that reverses the side a reader would expect, in a list that is otherwise
laterality-precise ("接著同側視力喪失" for lateral sphenoid wing is correct as ipsilateral).

Needs one look at the source. Translated as the Chinese stands, as "a hemianopia on the same side" and
"a visual field deficit on the same side" — deliberately literal so the editor can see the problem in
the English too.

## A6 — `bt-three-kinds`: the opening claim of 〈這三種病為什麼會被放在同一個專題〉 is one the paragraph then declines to support

**Sentence:**

> 因為它們合起來幾乎就是整個非惡性腦瘤的版圖。

The paragraph then, correctly, refuses to add the three figures ("兩份報告的分母不是同一個，所以我不把
三塊加起來") and falls back to a weaker, supportable claim ("這三種病合起來，在美國登記裡是原發腦瘤的
大宗"). So the topic sentence asserts something the rest of the paragraph explicitly says cannot be
computed from the numbers given. The fallback sentence is the one that is actually backed; the topic
sentence should be brought down to it.

Translated at the same strength as the Chinese ("Because between them they are very nearly the whole
map").

## A7 — `bt-three-kinds`: three malignancy figures in one sentence, in three different units

**Sentence (opening paragraph):**

> 腦膜瘤 195,297 例裡惡性 1,608 例；神經鞘瘤 37,436 例，每 10 萬人的發生率 2.02 裡惡性只佔 0.01；
> 垂體腫瘤 81,187 例裡非惡性佔 99.8% 以上

The whole point of the sentence is that **the proportions differ between the three**, but the three are
given as: a count out of a count; a rate out of a rate (after opening with a count that is then not
used); and an unquantified "99.8% 以上" of non-malignant. The reader cannot compare them, which is what
the sentence asks them to do. Each figure individually carries its denominator, so this is a
comparability defect rather than a labelling breach — but it sits in the first paragraph of the
foundation article.

Translated as it stands, including the "more than 99.8%" hedge.

## A8 — `bt-incidental` vs `bt-three-kinds`: D35 and D35.2 used for the same thing in two articles

`bt-incidental` writes 「D35（含腦下垂體良性腫瘤）」; `bt-three-kinds` writes 「垂體瘤（D35.2）」.
D35 is benign neoplasm of other and unspecified endocrine glands, of which the pituitary is only
`.2` — so the parenthetical gloss in `bt-incidental` is fair for a full-text search of the copayment
schedule (where D35 at any level returns zero hits), but the two articles now cite two different codes
for "benign pituitary tumour". Worth making consistent, with the reason for the difference stated where
the broader code is used.

Both translated as they stand (D35 in one, D35.2 in the other).

---

## Disclosed deviations (headings only)

1. **`bt-watch` h4 3.** Chinese heading: 「聽神經瘤：「生長」是最大徑增加 2 公釐」. The body of the
   same section, and the Tokyo 2001 consensus it cites, say 「線性測量增加**超過** 2 公釐」. A heading
   read on its own therefore states a threshold the body contradicts. The English heading uses the
   body's version — "'growth' means more than 2 mm on the longest diameter". **The Chinese heading
   should have 超過 added.**
2. **`bt-incidental`**, 〈「大多數不會出事」跟「大多數不會長大」〉, third paragraph. The Chinese reads
   「七成五會長大，跟十年有八成五不會惡化，同時是真的」. English renders these as "Seventy-five per cent"
   and "85%" rather than as "three-quarters"/"more than eight in ten", because the colloquial English
   fractions would have understated 八成五. No change to either number; noted because the register is
   slightly flatter than the Chinese here.

## Tool false positive

`check_bilingual.py` will flag, for `bt-incidental`:

```
? 比例 0.6 只出現在中文版，另一版最接近的是 0.507
```

This is the script's English proportion parser, not drift. `EN_IN` in `check_bilingual.py` only
recognises `one|two|three|1|2|3` before "in", so **"more than six in ten"** — the rendering SPEC-EN §3
mandates for 「超過六成」 — is invisible to it, while the Chinese 「超過六成」 is picked up by
`ZH_CHENG`. The number is identical in both languages. (The same script also reads 「七成五」 as 0.7 and
「八成五」 as 0.8 via `ZH_CHENG`; both land within tolerance of the English 0.75 and 0.857 and are not
reported, but they are the same class of artefact.)

No other errors or warnings: `check_article_html.py --lang en --min 1300 --max 2500` returns 0 errors
and 0 warnings for all four files; citation counts, citation URLs by position, reference counts,
reference URLs by position and `<h4>` counts are identical to the Chinese in all four.
