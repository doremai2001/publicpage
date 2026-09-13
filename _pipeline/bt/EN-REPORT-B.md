# EN-REPORT-B — defects found in the Chinese masters of group B while writing the English edition

Pass: English edition of group B (`bt-mg-grade`, `bt-mg-surgery`, `bt-mg-rt`, `bt-mg-adjuvant`,
`bt-mg-hormone`), 2026-09-13. **Nothing below has been "fixed" in the English.** Every item was
translated exactly as the Chinese stands, so that both languages can be corrected together.

Severity key: **A** = safety-relevant / breaks a 紅線 or 修正; **B** = missing label or
internal inconsistency; **C** = editorial / spec-compliance.

---

## A1 — `bt-mg-hormone`, §「有訊號的那幾個，絕對風險長這樣」: the three headline ratios have no measure label

Sentences (lines 7, 8, 9):

> 「沒用藥的一群，每 10 萬人一年出現 4.5 例；用藥那一群是 23.8 例，**校正後差 6.6 倍**（4.0 到 11.1）。……累積吃超過 60 公克的那一群，**倍數跳到 21.7**（10.8 到 43.5）。」
> 「……用藥那一群是 19.3 例，**年齡校正後差 2.9 倍**（2.4 到 3.7）。累積吃超過 6 公克的人，**倍數跳到 12.0**（9.9 到 16.0）。」
> 「對照組每 10 萬人年 6.8 例，用藥組 18.5 例，**差 3.1 倍**（2.4 到 4.0）。」

**What is wrong.** None of these five ratios says what kind of ratio it is — hazard ratio,
relative risk, or incidence rate ratio. They are written only as 「倍」/"-fold". This is the exact
failure mode SPEC §四 固定紅線 and SPEC §九 (「勝算比不是機率倍數」) are written to block, and
the same article is scrupulous about labelling the *other* ratios in it (相對風險 line 3,
勝算比 line 3 and line 12, 風險比 line 21). The inconsistency makes the unlabelled ones read as
plain multiples of probability — and these are the biggest numbers in the article (21.7, 12.0).
In English "6.6-fold" reads harder still than 「6.6 倍」.

**Recommendation (both languages together).** Name the measure the source reports for each
(Weill 2021 BMJ, Nguyen 2024 Lancet Reg Health Eur, Roland 2025 Eur J Neurol) and gloss it on
first use, as the article already does for OR and RR.

**What the English currently says:** "an adjusted difference of 6.6-fold (4.0 to 11.1)",
"the multiple jumped to 21.7", "an age-adjusted difference of 2.9-fold", "a difference of
3.1-fold" — i.e. the Chinese, unchanged.

## A2 — `bt-mg-grade`, §「三個級別各佔多少」: the CBTRUS figures carry no citation, and the report-year attribution conflicts with FIXES 丙2

Sentence (line 16):

> 「2018 到 2022 年那一版寫的是腦膜瘤佔全部原發腦與其他中樞神經系統腫瘤的 42.6%、佔全部非惡性腫瘤的 57.4%；**2017 到 2021 年那一版的發生率是每 10 萬人 10.15 例**。分母與出處寫在〈三種病，三套邏輯〉。」

Two problems.

1. **No `[n]`.** Three numeric claims (42.6%, 57.4%, 10.15/100,000) sit in the body with no
   citation attached; the only pointer is a cross-reference to another article in the topic.
   Every other number in this article is cited.
2. **FIXES 丙2 says the whole topic unifies on A 組's version, described as
   「2018–2022：腦膜瘤佔 42.6%、發生率 10.15／10 萬」** — i.e. 丙2 puts 10.15 in the *same*
   report year as 42.6%. This article splits them across two report years (10.15 attributed to
   2017–2021). One of the two is wrong, and the article's own next sentence
   (「不同報告年份的百分比不可以互相加減」) is precisely about why that matters.

**Recommendation.** Settle which report year carries 10.15 against A 組's actual source, make
B1 and A2 agree, and attach the citation in both languages.

## A3 — `bt-mg-rt`, §「台灣端」: the availability formula is truncated

Sentence (line 22):

> 「至於哪裡做得到，**不是每家醫院都有**。」

SPEC §一.4 and SPEC-EN §3 (Institutions) both fix the wording as
「不是每家醫院都有，**要用得先問你的主治醫師轉去哪裡**」 / "not every hospital has this — ask
your own doctor where to be referred". The second half, which is the actionable half, is missing
here. A reader is left with "not everywhere has it" and no next step.

**What the English currently says:** "As for where it can be done, not every hospital has it." —
the truncated Chinese, unchanged.

## A4 — `bt-mg-adjuvant`: 修正 7's requirement that the Simpson-grade/recurrence association be labelled observational does not appear in this article

修正 7 (and 紅線 8) end with 「Simpson 與復發的關聯是觀察性的」, and the ruling is written against
**B4**. The Chinese B4 labels its own datasets carefully (隨機/第二期/觀察性/單中心回溯), but the
Simpson-and-recurrence sentence itself lives only in B2 (`bt-mg-surgery` line 13, where it *is*
labelled correctly). B4 discusses Simpson 1–3 versus GTR as trial entry criteria without the
observational label anywhere near it.

**Recommendation.** Either add the one-clause label in B4, or record the editorial decision that
the label is delegated to B2 and B4 points at it. Not fixed in the English.

---

## B1 — `bt-mg-grade`: the mitotic thresholds leave a count of exactly 20 unassigned

Sentence (line 7):

> 「每 10 個高倍視野 **4 到 19 個落在第 2 級，超過 20 個落在第 3 級**」

"4 to 19" and "more than 20" leave 20 mitoses per 10 HPF in neither box. The criterion is
≥20 for grade 3; the Chinese should read 「20 個以上」. Translated as written ("more than 20
lands in grade 3").

## B2 — `bt-mg-rt`: the 視路旁腦膜瘤 pooled figure has no n and no follow-up length

Sentence (line 13):

> 「**視路旁腦膜瘤**用常規分次的統合資料（……），**合併局部控制 99.8%**、大約 90% 的人視力維持或改善……」

SPEC §四 固定紅線 requires every number to carry 瘤別／分級／大小分層／研究設計／追蹤時間／n.
This one carries tumour type and study design (and is honestly marked as a review's relay), but
has **no n and no follow-up length** — and 99.8% is the highest control figure anywhere in the
group. Translated as written.

## B3 — `bt-mg-rt`: two proton local-control figures sit two sentences apart with no "not comparable" marker

Line 15 gives 「常規分次質子 95.9%」 (5-year, grade 1 only, 24 studies / 4,673 people) and then
「影像上局部控制平均 71%」 (19 studies / 1,431 people, mixed grades 1–3, a mean rather than a
5-year rate). Both are called 局部控制 and both are about protons. The article does not say they
are measured on different rulers, although it does elsewhere for other pairs (line 13:
「兩組數字不能直接對打」). A reader can arrive at "protons control 95.9% or 71%, which is it?"

**Recommendation.** Add the same one-clause marker used at line 13. Not added in the English.

## B4 — `bt-mg-rt`: the 4,565-patient series mixes per-patient and per-tumour denominators

Line 9: 4,565 病人／5,300 顆腫瘤 → 分析 3,768 **顆** → 控制率 92.5%、五年 PFS 95.2%、
**永久性併發症 6.6%**. Control is per tumour; permanent complications are almost certainly per
patient. The denominator switch is not signposted. Translated as written.

## B5 — `bt-mg-surgery`: an odds ratio quoted to four significant figures with a very wide interval, and the imprecision is not flagged

Line 22: 「新缺損的勝算是其他人的 **6.667 倍**（95% 信賴區間 **1.408 到 31.556**，p=0.017）」.
The cohort is n=152 with 11.8% new deficits (≈18 events). An interval running from 1.4 to 31.6 is
extremely imprecise, and the article says nothing about that — while the *sister* article
`bt-mg-grade` does flag equivalent imprecision elsewhere. Spurious precision (three decimals on
the point estimate) also carries over into English, where it reads as measured rather than
modelled.

**Recommendation.** Round as the source rounds, and add the imprecision hedge. Neither done in
the English.

## B6 — `bt-mg-surgery`: reference [2] (Simpson 1957) is cited on a sentence that says its full text could not be obtained

Line 3: 「Simpson 原文的全文我取不到，以下引的是 2024 年一篇回顧對它的逐字轉述[1][2]」.
Attaching `[2]` — the 1957 paper itself — to a sentence stating that the 1957 paper could not be
read makes the citation marker claim support the source cannot give. It is defensible as a
pointer to the original, but it is not how the rest of the topic uses `[n]`.

**Recommendation.** Either drop `[2]` from that sentence and keep the entry as a bibliographic
pointer only, or reword the sentence. Kept exactly as the Chinese has it (both markers present,
same order, same hrefs).

## B7 — `bt-mg-hormone`: two odds ratios in the same list have no confidence interval

Line 12: 「cyproterone 19.21（16.61 到 22.22）、**nomegestrol 4.93、chlormadinone 3.87**」.
The first carries an interval and the other two do not, in the same clause of the same sentence
from the same study. Translated as written.

## B8 — `bt-mg-adjuvant`: the sign convention on 「最大差異 −2.7%」 is not explained

Line 16: the uncorrected five-year recurrence is **higher** in the irradiated group (25.5% vs
22.8%), and the adjusted result is then given as 「最大差異 **−2.7%**（95% 信賴區間 −5.6 到
0.2）」. Without a stated convention, a reader can take the minus sign either way — 2.7 points
fewer recurrences with radiotherapy, or 2.7 points worse. In English the ambiguity is, if
anything, sharper. The surrounding sentences do carry the correct interpretation
(「沒有證據顯示輔助分次放療降低了復發風險」), so the meaning is recoverable, but the number itself
is not self-labelling. Translated as written.

---

## C1 — statistical terms the Chinese does not gloss on first use (SPEC-EN §5 requires a gloss in **every** article)

The English adds a short plain-language gloss where the spec requires one and the Chinese has
none. These are additions the editor should mirror back into the Chinese rather than treat as
English-side drift:

| file | term unglossed in Chinese | where |
| --- | --- | --- |
| `bt-mg-grade` | 95% 信賴區間；無惡化存活；相對存活率；Brier 分數 | lines 13, 13, 16, 19 |
| `bt-mg-surgery` | 風險比；95% 信賴區間；無惡化存活 | lines 7, 22, 6 |
| `bt-mg-rt` | 無惡化存活；選擇偏差 (explained in words but not named as such) | lines 9, 10 |
| `bt-mg-adjuvant` | 風險比；95% 信賴區間；無惡化存活／整體存活 | lines 14, 13, 9 |
| `bt-mg-hormone` | 95% 信賴區間；標準化發生比；風險比 | lines 3, 19, 21 |

(勝算比 and 相對風險 **are** glossed in the Chinese wherever they first appear, and those glosses
are carried across unchanged.)

## C2 — `bt-mg-hormone`: the lead in `meta/B.json` still duplicates a body sentence

FIXES §五 flagged 「`bt-mg-hormone` lead 首句對 p7」 as one of three verbatim duplications to be
removed in one of the two places. The Chinese lead still reads
「風險最高的那一格，換算下來是一個人一年大約萬分之二點四」 against body line 10
「風險最高的那一格，每 10 萬人年 23.8 例，換算成一個人一年大約是萬分之二點四」 — still
near-verbatim. The English `meta/B-en.json` lead carries the same content and the same number but
is worded so it does not echo the body (5-gram overlap 1.7%), so the two language editions now
differ in shape at this one point. Flagging rather than silently re-aligning.

## C3 — `bt-mg-grade`: two registry figures relayed by ICOM without report year or n

Lines 15 and 16: the 80.1% / 18.3% / 1.5% split and the 「非惡性腦膜瘤的十年相對存活率 83.4%」.
The article says so itself for both, which is the right instinct — but 83.4% still enters the
body with neither n, report year, nor follow-up cohort, which SPEC §四 固定紅線 does not permit.
Either keep it with an explicit "I cannot give you the denominator for this one" or drop it.
Kept as written.

---

## Checker output — tool false positives

`python3 check_article_html.py en/bt-mg-*-en.html --lang en --min 1300 --max 2500` returns
**0 errors, 0 warnings** for all five files, so there is nothing to declare as a false positive
this round. (The soft-banned-word scan in the script only runs for `--lang zh`, so it produced no
English output at all.)
