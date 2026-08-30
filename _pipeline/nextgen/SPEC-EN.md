# 次世代治療專題 — English edition spec

Supplementary. **Read `/home/claude/colon/SPEC-EN.md` first** — no-drift rules,
British spelling, structure, "if you think the Chinese is wrong" all apply.
Then `/home/claude/nextgen/SPEC.md` §二/§三/§六/§九 — every warning, disclosure
and red line binds the English text equally.

## 1. The fixed blocks — one English rendering, byte-identical across all six

Translate 警語一, the article-specific sentence, 警語二 and the disclosure ONCE,
then paste the three fixed blocks byte-identically into every article (the
article-specific sentence varies). Same `<p><strong>警語…</strong>…</p>` shape:
`<p><strong>Warning 1 (what this displaces):</strong> …</p>` etc. The key
sentences must keep full force: "the question is not whether this is worth
trying — it is what you give up by doing it"; "if they never once say who this
is NOT for, that is not a consultation, it is a sale"; "both proton therapy and
hyperthermia are my own fields… so I draw every line in this topic tighter, not
looser."

## 2. Hard rules

Citations `[n]` → same URLs, same order. Every number identical, with its
population/trial label. Every hedge at the same strength — the highest-drift
passages: N3's Frank 2026 三層 paragraph (non-inferiority first, OS secondary,
caveats in the same run — English will want "protons won"); N5's "no efficacy
comparison anywhere"; N6's "found no usable target is a common result, not bad
news, not a failed test"; N2's "有沒有 FDA 核准，兩個方向都會判斷錯". The
查證日期 line becomes "Facts checked: August 2026." before the references.

## 3. Canonical English titles

- nt-how-to-read → "New does not mean better"
- nt-approval → "Approved, covered, effective: three different things"
- nt-proton → "Protons: precise. Then what?"
- nt-carbon → "Carbon ions: heavier is not better"
- nt-flash → "FLASH: radiotherapy in under a second, still in phase 1"
- nt-bnct → "BNCT: the radiotherapy that does not aim"

Cross-references use these in double quotes. N3's pointer to the insight page
refers to the English insight page 「質子治療真的比較好嗎」's English counterpart
by role ("the site's research-update page on proton therapy") without series quotes.

## 4. Structure

Same `<h4>` count/order, headings rewritten not literal; 1,100–2,100 words
(faithfulness wins; the fixed blocks add ~120 words); `<h3>References</h3>`;
ends `<p></p>`. Metadata per group file `meta/<X>-en.json`, titles above verbatim.
