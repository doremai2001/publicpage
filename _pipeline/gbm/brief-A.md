# Brief A — GBM 專題「確診與分類」群（A1–A5）

研究員：Group A｜查證日期：**2026-09-03**
期刊書目資料全部經 Europe PMC REST 逐筆核對（title／journal／year／volume(issue)／pages／DOI／PMID／isOpenAccess）；
可取得全文者（Europe PMC fullTextXML 或 PMC HTML）已抓下逐句核對，引語為原文。
指引與官方身分引官方 landing page（EANO 論文全文、FDA、EMA、衛福部健保署 PDF）。**未引用 NCCN。**

**引用規則：只有標 PASS 的來源可以進正文。** FAIL / NOT-CITABLE 條目保留在最後，讓寫作者知道查過什麼、
哪幾句只能寫「我查不到可以引用的來源」。所有 [Sn] 編號全 brief 唯一。

---

## ⚠ 與 SPEC 假設不同形狀的事（動筆前必讀，共 11 條）

> 每一條都在下面的篇章節裡有完整原文與 [Sn]；這裡只列「哪裡跟 SPEC 不一樣」。

**1. GBM 的分子定義多一個入口前提，而且「五選一」不是平的。**
WHO CNS5 原文要求先是「**成人的、瀰漫性的、星細胞性的**」膠質瘤，才輪到五選一（微血管增生／壞死／TERT 啟動子
突變／EGFR 擴增／+7−10）[S1]；年輕病人要先排除小兒型瀰漫性膠質瘤，且「glioblastoma」這個詞已不用於小兒型
腫瘤[S1]。cIMPACT-NOW 明文：**IDH-wildtype 本身不足以定 grade 4**（很多良性一點的腫瘤也是 IDH-wildtype）[S2]；
**EGFR 必須是局部高倍數擴增，trisomy 7 不算，免疫組化不可用來判定**[S2]。
→ `fig-gb-classification` 必須有「成人／瀰漫性／星細胞性」的入口框，EGFR 那一格要有旁註。

**2.「間變性星細胞瘤去哪裡了」是兩條路，不是一句話。**
CNS5 把 "anaplastic" 這個修飾詞**整個從命名系統移除**（anaplastic astrocytoma 與 anaplastic oligodendroglioma
都不再出現）[S1]。舊的間變性星細胞瘤依 IDH 狀態拆成兩個病：IDH-mutant → Astrocytoma, IDH-mutant, grade 3；
IDH-wildtype ＋ 三個分子標記任一 → 直接叫 Glioblastoma, IDH-wildtype, grade 4[S1][S2]。
同時 CNS5 **刪掉「Glioblastoma, IDH-mutant」這個名字**，改叫 Astrocytoma, IDH-mutant（涵蓋 grade 2–4）[S1]。

**3. 還有兩個名詞改動，病人的報告上看得到，SPEC 沒列。**
(a) **羅馬數字改阿拉伯數字**（grade 4，不是 IV），CNS5 給的理由是「II 與 III、III 與 IV 容易看錯，
沒被抓到的打字錯誤會有臨床後果」[S1]。(b) **NOS 後綴＝該做的分子檢測沒做或失敗；NEC＝做完了但湊不出標準
WHO 診斷**[S1]——**「NOS」不是「查不出來」，是「還沒測完」**，這句對 A4 很重要。

**4. 美國癌症登記自己還在用被廢掉的碼。**
CBTRUS 2018–2021 分子資料：被登記為 glioblastoma 的病例中，**1,194 例（2.4%）仍編為 9445/3
「Glioblastoma, IDH-mutant」**（CNS5 已取消的名稱），80.4% 編為 IDH-wildtype，**14.6% IDH 狀態不明**[S4]。
→ 可以誠實寫：分類 2021 年換了，**全世界的報表都還在追**；也順帶說明為什麼老文獻的「GBM」跟今天的不是同一群人。

**5. 預防性抗癲癇藥：SPEC 指名要引的 AAN 那份已經被撤回。**
Glantz 2000 的 AAN practice parameter 在 PubMed／Europe PMC 標題已標 **[RETIRED]**[S8]，**不可當現行指引引用**。
改用 EANO 2021 原文（「Primary prophylaxis does not reduce the risk of a first seizure in patients with glioma
without a history of seizures」）[S5] 與 SNO 2024 共識[S9]。

**6. RANO resect 的分級名稱與 SPEC 寫的不一樣，而且「切幾成」已經被踢出去了。**
2023 年的「RANO categories for EOR in glioblastoma」**只有四級**：supramaximal／maximal／submaximal／biopsy
——**沒有 "total resection" 這一級**[S11]。更關鍵：這套分級**只看術後絕對殘餘體積（cm³）**，
多變項分析裡「相對切除百分比失去預後意義」[S11]。
→ **A3 應該把病人最直覺的「切掉幾成」換成「還剩多少」。** 這是這一篇最好的轉折點。

**7. 紅線 2 要更精確：能隨機的是「工具」，不是「切除量」。**
Stummer 2006 隨機的是**用不用螢光劑**；兩個主要終點是完全切除率與 6 個月 PFS，**存活是次要終點**，
且試驗依規約在期中分析後終止[S14]。2023 年 JCO 的前瞻對照試驗進一步顯示 iMRI 與 5-ALA 的完全切除率沒有差別
（81% vs 78%，P=.79），真正有預後意義的是**殘餘 0 cm³**[S33]。
→ 正確措辭：「切除程度與存活的關聯全是觀察性；**隨機試驗能證明的是某個工具讓你切得比較乾淨，
不是切得乾淨讓你活得比較久。**」

**8. supramaximal 的好處有年齡邊界（2026 年新資料）。**
RANO resect group 年齡分層報告（n=1,260，≥65 歲 512 人）：「**Only in patients <65 years, supramaximal resection
was associated with more favorable survival (40 vs 20 months, P = .001)**」；復發手術情境下兩個年齡層都看不到
supramaximal 的好處[S18]。→ A3 不能寫成「切越多越好」的通則。

**9. INDIGO 的收案條件比 SPEC 列的多兩條硬條件，而且 FDA 仿單比試驗寬。**
SPEC 列的四項（grade 2、IDH-mutant、術後未接受放化療、無需立即治療）都對，但漏了
**最近一次手術須在隨機分派前 1–5 年**、**必須有可測量的非增強病灶（≥1×1 cm）**、KPS ≥80、不需類固醇[S23]。
而 **FDA 核准的適應症沒有這些限制**——ASCO-SNO 2025 逐條指出落差，並明說「**對已接受過放療或化療的人，
本小組無法做出建議**」[S7]。**EMA 的適應症則比 FDA 窄**，把「以非增強為主／只做過手術／不需立即放化療」
寫進了適應症本文[S29]。→ A5 必須寫「同一個藥，美國跟歐盟的適應症寫法不一樣，而試驗真正證明過的族群
比兩邊的仿單都窄」。

**10. ASCO-SNO 對 vorasidenib 的建議強度是「條件式」，不是「應該給」。**
新增的 Recommendation 1.2.1／1.5.1：「**Vorasidenib may be offered**...（**Evidence quality: High;
Strength of recommendation: Conditional**）」[S7]。**證據品質 High ＋ 建議強度 Conditional** 這個組合本身就是內容。
同一份更新也寫進實務條件：頭兩個月每兩週、之後每月監測肝功能；備孕／懷孕／哺乳者不應使用[S7]。

**11. 台灣端：一項查到、四項查不到（不可推論）。**
✅ **重大傷病**查到官方原文：腦惡性腫瘤走第一大項「需積極或長期治療之癌症」第（五）小項
（C00.0–C96.9，不含 C73／C94.4／C94.6），**證明有效期限五年**（114/1/1 起適用）[S30]；
效期二年以上者可於**屆滿前三個月**重新申請[S34]。
❌ vorasidenib 台灣藥證（FAIL-1）／❌ vorasidenib 健保給付（FAIL-2）／❌ 5-ALA 藥證與給付（FAIL-3）／
❌ 台灣癌登腦瘤發生數（FAIL-4）——**全部寫成「我查不到可以引用的官方資料」，永不推論有無。**

## gb-what-it-is〈膠質母細胞瘤是什麼，不是什麼〉（A1，地基篇）

### Key facts

**A. 2021 WHO CNS5 的定義（全部逐字可引）**

1. **成人型瀰漫性膠質瘤在 CNS5 只剩三個 type**：
   「WHO CNS5... includes only 3 types: *Astrocytoma, IDH-mutant*; *Oligodendroglioma, IDH-mutant and 1p/19q-codeleted*;
   and *Glioblastoma, IDH-wildtype*.」（2016 年版是 15 個 entity）[S1]
2. **GBM 的診斷條件**（原文見上方「不同形狀的事 1」）：IDH-wildtype 的成人瀰漫性星細胞膠質瘤，加上
   微血管增生 **或** 壞死 **或** TERT 啟動子突變 **或** EGFR 基因擴增 **或** +7/−10 染色體套數變化，任一即可[S1]。
3. **分子條件可以直接跳過組織學的等級**：「TERT promoter mutation, EGFR amplification, and +7/−10 copy number
   changes in IDH-wildtype diffuse astrocytomas (**allowing a glioblastoma, IDH-wildtype CNS WHO grade 4
   designation even in cases that otherwise appear histologically lower grade**)」[S1]。
4. **IDH-mutant 這一側**：所有 IDH-mutant 瀰漫性星細胞腫瘤都是同一個 type（*Astrocytoma, IDH-mutant*），
   然後分 CNS WHO grade 2／3／4；「grading is no longer entirely histological, since **the presence of
   CDKN2A/B homozygous deletion results in a CNS WHO grade of 4, even in the absence of microvascular
   proliferation or necrosis**」[S1]。
5. **分級改用阿拉伯數字**、**在 type 之內分級**（不再跨 entity 分級）[S1]。
6. **"anaplastic" 這個字被移除**（見上方第 2 條）[S1]。

**B. cIMPACT-NOW 的來歷（A1 要交代「這套規則從哪來的」）**

- cIMPACT-NOW（Consortium to Inform Molecular and Practical Approaches to CNS Tumor Taxonomy）2016 年成立，
  目的是在兩次 WHO 改版之間更快把分子病理的進展帶進臨床[S2]。
- **Update 3（2018，Acta Neuropathol 136:805–810）就是 GBM 三個分子條件的出處**。原文結論：
  「We reached consensus that the following were the minimal molecular criteria for identifying an IDH-wildtype
  diffuse astrocytic glioma that, despite appearing histologically as a WHO grade II or III neoplasm, would follow
  an aggressive clinical course more closely resembling that of an IDH-wildtype glioblastoma: **EGFR amplification
  OR Combined whole chromosome 7 gain and whole chromosome 10 loss (+7/−10) OR TERT promoter mutation**」[S2]。
- cIMPACT-NOW 自己留了誠實註記：「we were cautious in our interpretation of the literature, since **most large
  studies on the relationship between genetic alterations and clinical outcomes have relied on retrospective
  cohorts** in which patients were treated differently depending on institution, era and histologic
  classification」[S2]。→ 這句可以直接用在 A1 收尾，把「分類是共識、不是實驗結果」講清楚。
- WHO CNS5 明說自己是建立在 cIMPACT-NOW 之上：「Building on the 2016 updated fourth edition and the work of the
  Consortium to Inform Molecular and Practical Approaches to CNS Tumor Taxonomy」[S1]。

**C. 發生率與好發年齡（全部帶年份與地區標籤）**

美國 CBTRUS，2018–2022 年資料（最新一版，2025 年 10 月出版）[S3]：
- 所有原發性腦與其他中樞神經系統腫瘤（含良性）年齡標準化發生率 **26.05／10 萬人**（惡性 6.86、非惡性 19.19）
- **膠質母細胞瘤佔全部腦瘤的 13.7%，佔惡性腦瘤的 52.2%**
- 腦膜瘤佔全部腦瘤的 42.6%、佔非惡性腦瘤的 57.4%
- **膠質母細胞瘤男性較多，腦膜瘤女性較多**
- 神經膠質瘤（gliomas）合計佔全部腫瘤的 22.2%

CBTRUS，2017–2021 年資料（上一版，有全文可查細項）[S4]：
- **膠質母細胞瘤發生率 3.27／10 萬人**（男 4.07、女 2.58）
- **膠質母細胞瘤佔全部腦瘤 14.0%、佔惡性腦瘤 51.5%、佔所有膠質瘤 61.0%**
- **診斷時中位年齡 66 歲**（腦膜瘤 68、淋巴瘤 69）
- **發生率最高的年齡層是 70–74 歲**
- 「There was no significant change over time in the incidence of glioblastomas.」（**發生率沒有隨時間顯著變化**）

**D. 為什麼它不是腦轉移、不是腦膜瘤（各一句的正確說法）**

- **腦轉移**：美國的癌症登記「only collect data on primary CNS tumors (meaning tumors that originate within the
  brain and spinal cord) and **do not collect data on tumors that metastasize to the brain or spinal cord from
  other primary sites**」[S4]。→ 正確一句：「腦轉移是別的器官的癌細胞跑到腦子裡，**登記上根本不算腦瘤**；
  它治療的是原來那個癌，不是這個。詳見站上〈腦轉移〉。」
- **腦膜瘤**：CNS5 把它放在完全不同的 type，分級範圍是 CNS WHO grade 1–3，而且原文明說「there is neither a
  CNS WHO grade 1 IDH-mutant astrocytoma **nor a CNS WHO grade 4 meningioma**」[S1]；流行病學上它是最常見的
  非惡性腦瘤（佔全部腫瘤 42.6%）[S3]。→ 正確一句：「腦膜瘤長在腦子外面的膜上，**分級最高到 3，沒有 grade 4**，
  是完全不同的病；本站另開專題。」
- **腦下垂體瘤／聽神經瘤**：CNS5 把腦下垂體腫瘤改稱「Pituitary adenoma/PitNET」[S1]；CBTRUS 2017–2021 顯示
  腦下垂體腫瘤發生率 4.67／10 萬人、**99% 為非惡性**，神經鞘瘤（含聽神經瘤）2.02／10 萬人[S4]，
  且神經鞘瘤五年相對存活率 99.2%[S4]。→ 各一句指路即可。

**E.「分子報告會改掉診斷名稱」的伏筆（交給 A4）**

- 甲基化圖譜（methylome profiling）：「the availability of this method may have a substantial impact on
  diagnostic precision compared to standard methods, **resulting in a change of diagnosis in up to 12% of
  prospective cases**」[S19]。A1 只放一句伏筆，完整寫法歸 A4。

### 反方向的資料（誠實必列）

- **這套分類是專家共識，不是隨機試驗的產物。** cIMPACT-NOW 自己承認底層文獻多為回溯性世代、各機構治療不一[S2]。
- **登記系統還沒跟上**：CBTRUS 2018–2021 資料中 2.4% 的 GBM 仍被編為已被廢除的「Glioblastoma, IDH-mutant」碼，
  14.6% IDH 狀態不明[S4]。→ 誠實地說：「你手上如果是幾年前的報告，名字可能跟現在不一樣，**不代表病變了**。」
- **甲基化圖譜不是萬能**：WHO CNS5 原文：「**caveats remain that optimal methodologic approaches and regulatory
  issues for methylome profiling have yet to be resolved and that the technology is currently not widely
  available**」，且「methylome profiling can struggle with classification of low-grade diffuse gliomas」[S1]。

### Claim ceiling（A1）

**可寫**：IDH-wildtype 才叫 GBM／IDH-mutant 改叫星細胞瘤（grade 2–4）[S1]；分子條件可跳過組織學等級直接定
grade 4[S1][S2]；「間變性星細胞瘤」這個名字在 2021 年分類裡不見了[S1]；grade 改寫阿拉伯數字[S1]；
美國資料的佔比、發生率 3.27／10 萬（2017–2021）、中位年齡 66 歲、70–74 歲最多、男多於女[S3][S4]；
腦轉移在癌症登記裡不算腦瘤[S4]。

**不可寫**
- ❌「IDH-wildtype 就是膠質母細胞瘤」——漏掉「成人／瀰漫性／星細胞性」的入口條件，也違反 cIMPACT-NOW 明文
  「lack of IDH mutation alone is thus insufficient」[S2]
- ❌「驗 EGFR 免疫染色陽性就算 EGFR 擴增」——cIMPACT-NOW 明文禁止用 IHC 判定[S2]
- ❌ 任何台灣的發生率、人數、比例數字（**查不到，見 FAIL-4**）。要提就寫「台灣的腦瘤登記數字我這次查不到可以
  引用的官方版本」
- ❌ **任何存活數字當結論**（SPEC §六：預後數字歸 B4）。A1 若需帶到，只能寫一句「這個病的數字怎麼讀，
  我另外寫了一篇」並指向 `gb-numbers`
- ❌ 把 CNS5 寫成「新研究證明」——它是分類共識文件

### Caveats／safety notes（寫作者必寫）

- 讀者最可能誤讀的一句是「分子檢測可以把看起來低等級的腫瘤升級成 grade 4」。**要同時寫清楚它為什麼要這樣做**：
  因為那群病人的臨床病程本來就跟 GBM 一樣（cIMPACT-NOW 的原始論證）[S2]，**升級的是名字，不是病情惡化**。
- 「舊報告上寫的名字跟現在不一樣」在門診很常見，必須一句安撫並指向 A4。
- 不要把「發生率沒有隨時間顯著變化」[S4]寫成「所以跟環境／手機／飲食無關」——那是另一個問題，本篇不處理。

### 台灣端（A1）

- 台灣癌症登記的腦瘤發生數與 GBM 比例：**gap**（FAIL-4）。
- 重大傷病歸 A2 主場。

### 給繪圖組的數字（A1，`fig-gb-classification`）

可用的 PASS 數字與結構：
1. 入口框：**成人 ＋ 瀰漫性 ＋ 星細胞性膠質瘤**[S1]
2. 第一個分岔：**IDH 突變？**
   - IDH-mutant → 再問 **1p/19q 共缺失？** → 有 ＝ 寡樹突膠質瘤（IDH-mutant, 1p/19q-codeleted）；
     無 ＝ 星細胞瘤（IDH-mutant），grade 2／3／4（CDKN2A/B 同型合子缺失 → 直接 grade 4）[S1]
   - IDH-wildtype → 五選一（微血管增生／壞死／TERT 啟動子突變／EGFR 擴增／+7−10）→ **膠質母細胞瘤,
     IDH-wildtype, CNS WHO grade 4**[S1]
3. 旁註框（**不要畫進主流程**）：EGFR 必須是局部高倍數擴增，trisomy 7 不算，免疫染色不能用[S2]
4. 旁註框：年輕病人先想小兒型瀰漫性膠質瘤[S1]
5. 佔比條：GBM 13.7% of all／52.2% of malignant；meningioma 42.6% of all（CBTRUS 2018–2022）[S3]

---

## gb-first-days〈發現那顆瘤之後的頭幾天〉（A2）

### Key facts

**A. 影像（MRI 的角色與限制）**

- **標準是什麼**：EANO 2021 原文：「Brain MRI, including T2-weighted, T2-weighted fluid-attenuated inversion
  recovery (FLAIR) sequences and **3D T1-weighted sequences before and after application of a gadolinium-based
  contrast agent, is the diagnostic gold standard to detect a brain tumour**」；建議欄位：「The first choice of
  diagnostic imaging modality is MRI without and with the administration of a gadolinium-based contrast
  agent.」[S5]
- **perfusion／PET 的角色（很窄，要照原文寫）**：EANO 只給它一個具體用途——**幫忙決定「切片要扎哪裡」**：
  「**Perfusion MRI and amino acid PET can help to define metabolic hotspots for specific tumour tissue sampling,
  a technique that can be particularly useful if biopsy rather than open resection is considered**」[S5]。
  另一個用途是後續分辨假性惡化：「Perfusion MRI and amino acid PET **might help** to distinguish
  pseudoprogression from true disease progression」[S5]（**這一句歸 D1，A2 只指路**）。
- **限制的正確寫法**：EANO 通篇沒有把 perfusion 或 spectroscopy 放進「診斷」的建議條目；診斷靠組織：
  「**Treatment decisions in patients with glioma are made based on tissue diagnosis**, including the assessment
  of molecular markers relevant for diagnosis」[S5]。
  → 正確一句：「影像可以讓我們**猜得很準**，也可以幫忙決定針要扎哪裡，但**它不能取代那塊組織**。」
- **液態切片還不能用**：「a large number of studies has shown that cell-free tumour DNA can be detected in the
  plasma and cerebrospinal fluid of patients with glioma; however, **the benefits of using liquid biopsies for the
  screening, early detection or preoperative work-up of patients with gliomas remain to be proven**」[S5]。
- **術後 MRI 要有 DWI**：「MRI should include diffusion-weighted sequences to enable the detection of perioperative
  ischaemia」[S5]。（可放在「開完刀為什麼馬上又要照一次」那段。）

**B. 什麼情況先切片，什麼情況直接切除（EANO 原文，逐條可引）**

- 預設是**同時做診斷與治療的手術**：「upfront surgery is commonly performed with **both diagnostic and
  therapeutic intent**」[S5]
- **改做切片的條件**：「When microsurgical resection is **not safely feasible** (for example, owing to the tumour
  location or the impaired clinical condition of the patient), a **stereotactic biopsy** should be performed」；
  切片本身「is associated with **a low risk of morbidity and a high level of diagnostic accuracy**」[S5]
- **切片的技術要求**：沿針道分段取樣（「Serial samples... along the trajectory of the biopsy needle **in order to
  avoid sampling bias**」）；5-ALA 也可用來確認取到腫瘤[S5]
- **取樣誤差對關鍵標記其實不大**（對「會不會扎不準」的恐懼很有用）：「IDH mutations and 1p/19q codeletion...
  as well as MGMT promoter methylation **are homogeneously present within tumours** and, thus, **the risk of
  sampling error for these markers is low**」[S5]
- **不取組織就決定的門檻很高**：「A decision for palliative care management without histological diagnosis
  **should be avoided unless** the risk of adverse outcomes from biopsy sampling is considered too high or if the
  prognosis is likely to be very unfavourable...」；且「**Definitive histological diagnoses aid in the counselling
  of patients and caregivers, even when no further tumour-specific therapy is recommended.**」；
  建議欄位：「Clinical decision-making without obtaining a tissue diagnosis should be considered **only in very
  exceptional situations**」[S5]
- **在哪裡開**：「should take place in **high-volume specialist centres**」[S5]

**C. 多專科團隊**

EANO 原文：「Patient management before surgery should follow written local standard operating procedures and
**involve multidisciplinary discussions, ideally by a dedicated multidisciplinary tumour board including
neuroradiologists and neuropathologists as well as neurosurgeons, radiation oncologists and dedicated
neuro-oncologists from neurology or medical oncology services** and from paediatric oncology as needed.」[S5]

→ 這一句可以直接翻成病人語言：「你的片子跟報告會被一群人一起看過，不是一個人決定。」

**D. 術前類固醇的起始邏輯（劑量當背景，不可寫成用法用量）**

- EANO 原文（**唯一一句、要逐字**）：「**Prior to surgery, corticosteroids can be administered to decrease
  symptomatic tumour-associated oedema unless primary cerebral lymphoma or inflammatory lesions are suspected.**
  Alternative pharmacological measures, such as osmotic agents, are rarely necessary.」[S5]
- 兩個可以展開成白話的重點：
  1. **它治的是「腫脹」，不是腫瘤**（decrease symptomatic tumour-associated oedema）——所以症狀改善不等於腫瘤變小。
  2. **懷疑是原發性中樞神經淋巴瘤或發炎性病灶時，先不要給**——因為類固醇會讓淋巴瘤在影像與病理上「消失」，
     反而診斷不出來。這一句是 A2 最有臨床味道的一段，而且有原文可引。
- **不寫劑量、不寫給藥時程。** 完整的類固醇內容（減量、副作用、什麼時候聯絡團隊）歸 C2（SPEC §六）。
- 一個相關但要小心的事實：EANO 的參考文獻中收錄了 Pitter 等「**Corticosteroids compromise survival in
  glioblastoma**」（Brain 2016;139:1458–1471）[S5 之引文]。**這是回溯性資料**，A2 不要引用它的結論，
  只要在 C2 交代「類固醇不是越多越好、能減就要減」時由 C 組自行查證。**A2 不寫。**

**E. 預防性抗癲癇藥**

- EANO 2021 原文（逐字）：「**Patients who have suffered epileptic seizures should receive anticonvulsant drugs
  preoperatively. Primary prophylaxis does not reduce the risk of a first seizure in patients with glioma without
  a history of seizures.**」[S5]
- SNO 2024 共識（摘要層級）：「Initial treatment with antiseizure medications (ASM) in conjunction with surgery
  and/or chemoradiotherapy is typical. **The first choice of ASM is critical to optimize seizure control and
  tolerability considering the effects of the tumor itself. These agents carry a potential for drug-drug
  interactions** and therefore knowledge of mechanisms of action and interactions is needed.」[S9]
- **不引 AAN 2000**（已標 RETIRED）[S8]。

**F. 臨床表現與術前評估**

- EANO：「Characteristic modes of clinical presentation include **new-onset epilepsy, focal deficits (such as
  pareses or sensory disturbances), neurocognitive impairment, and symptoms and signs of increased intracranial
  pressure.**」[S5]
- 理學檢查的兩個目的（原文）：「The physical examination of patients with brain tumours focuses on **the detection
  of systemic cancer to differentiate primary brain tumours from brain metastases** and contraindications for
  neurosurgical procedures.」[S5] → 這解釋了「為什麼還要照胸部、抽血、看全身」，是很好的一段。
- 決策要看什麼：「**Karnofsky performance score (KPS), neurological function, age, and individual risks and
  benefits should be considered for clinical decision-making.**」[S5]
- 篩檢沒有角色：「Screening and prevention have no major role for patients with gliomas.」[S5]
- 有家族／遺傳疑慮者：「Patients with relevant germline variants or suspected hereditary cancer syndromes should
  receive genetic counselling」[S5]

### 反方向的資料（誠實必列）

- **EANO 對術前類固醇的措辭是「can be administered」，不是「should」**[S5]——不能寫成「一定要先吃類固醇」。
  正確寫法：「有症狀性水腫的時候可以先給；沒有症狀的時候不是非給不可。」
- **切片不是零風險**，EANO 的原文是「low risk of morbidity」，不是 no risk[S5]。
- 「多專科團隊」EANO 用的是「ideally」[S5]——不能寫成「每一家醫院都一定有」。

### Claim ceiling（A2）

**可寫**：打顯影劑的腦部 MRI 是診斷黃金標準[S5]；灌流 MRI／胺基酸 PET 的用途之一是決定切片扎哪一點[S5]；
治療決定要建立在組織診斷上，不取組織就決定只能是非常例外[S5]；開不安全時改做立體定位切片、沿針道分段
取樣[S5]；IDH／1p19q／MGMT 在腫瘤內分布相對均勻，取樣偏差風險低[S5]；類固醇術前是為了消腫脹，疑淋巴瘤或
發炎性病灶先不給[S5]；沒發作過的人預防性抗癲癇藥不降低第一次發作風險[S5]；片子會被多科一起看[S5]；
台灣：腦惡性腫瘤屬重大傷病第一大項第（五）小項，**證明有效期限五年**[S30]，效期屆滿前三個月可重新申請[S34]。

**不可寫**
- ❌ 任何類固醇的劑量、次數、減量時程（歸 C2；紅線 4）
- ❌ 任何抗癲癇藥的藥名選擇與劑量（歸 C3；紅線 5）
- ❌「MRI 就能確診」——違反 EANO 的組織診斷原則[S5]
- ❌「灌流 MRI／磁振頻譜可以分辨良惡性」——EANO 沒有給這個用途，**查不到可引用的原文**
- ❌ 任何存活數字（歸 B4）
- ❌ 任何自費金額（費用紀律：全文檔搜尋零筆＝寫零筆＋「問醫務課」）

### Caveats／safety notes（寫作者必寫）

- **不可自行加減類固醇**（紅線 4 的第一次出現點）——A2 只寫一句並指向 C2。
- 「類固醇讓我馬上好很多」是最危險的一個讀法：**它壓的是水腫，不是腫瘤**[S5]。這句一定要寫。
- 急症警訊（顱內壓升高等）**一句指向 C4**〈哪些狀況要當天回來〉，A2 不展開（SPEC §六）。
- 這一篇的讀者很多是「前一週還在上班」的人。EANO 的「high-volume specialist centres」那句可以用來回答
  「要不要轉院」，但**不可點名機構**（固定紅線）。

### 台灣端（A2，重大傷病主場）

**PASS。** 來源：衛生福利部中央健康保險署，《全民健康保險保險對象免自行負擔費用辦法》第二條附表一
「全民健康保險重大傷病項目及其證明有效期限」（113 年 9 月 16 日發布修訂，**一百十四年一月一日以後適用**）[S30]。

原文結構（逐字）：
```
一、需積極或長期治療之癌症。
  (一) 甲狀腺惡性腫瘤                      C73                          三年
  (二) 口腔、口咽及下咽惡性腫瘤第一期        C00.0-C06.9 等                三年
  (三) 乳房惡性腫瘤第一期                  C50.011-C50.929               三年
  (四) 子宮頸惡性腫瘤第一期                C53.0-C53.9、C55              三年
  (五) 除(一)-(四)之其他惡性腫瘤            C00.0-C96.9                   五年
       (不含 C73、C94.4、C94.6)
```
→ 腦與中樞神經系統惡性腫瘤（ICD-10-CM C71）落在第（五）項，**證明有效期限五年**[S30]。

同一份法規（全國法規資料庫，《全民健康保險保險對象免自行負擔費用辦法》）第八條：
「重大傷病證明有效期間屆滿，申請人得於下列期限內…重新申請：一、**有效期間為二年以上者：效期屆滿三個月前**。
二、有效期間為一年或六個月者：效期屆滿一個月前。三、有效期間為三個月以下者：效期屆滿十四日前。」[S34]
→ 五年效期者，**屆滿前三個月**可重新申請。這一句對病人非常實用。

**gap**：申請流程細節、需附哪些文件、由誰送件——本次未取得可引用的官方原文（NHI 申請須知頁被 Cloudflare 擋，
見 FAIL-6）。文章寫成「請問個管師或醫院的重大傷病窗口」。

### 給繪圖組的數字（A2）

本篇 SPEC 未指定自繪圖。若要一張流程小圖，可用的 PASS 素材：
「有症狀 → MRI（含顯影）→ 多專科討論 → 能安全切除？→ 是：手術（診斷＋治療）／否：立體定位切片 →
組織＋分子報告 → 治療決定」[S5]，旁註「類固醇：有症狀性水腫才給；疑淋巴瘤先不給」[S5]、
「沒發作過不常規給抗癲癇藥」[S5]。

---

## gb-surgery〈開刀能拿掉多少，「全部拿掉」是什麼意思〉（A3）【紅線 2】

> **利益揭露段（SPEC §二）放在本篇第一個 h4 之前，逐字照抄。**

### Key facts

**A. 切除程度的分類：從「切幾成」變成「還剩多少」**

*A-1. 2021 年 EJC 的六級描述性系統（Karschnia 等，RANO resect group）*[S10][S11]

摘要層級（[S10]）：六個類別為 biopsy／partial／subtotal／near total／complete／supramaximal resection；
定義建立在「顯影與非顯影腫瘤的縮減」（grade 2/3 則用 T2/FLAIR 高訊號），同時納入**相對縮減百分比**與
**絕對殘餘體積（cm³）**；**「Class of evidence for the proposed categories ranges from class IIB to IV.」**

各級門檻（2023 年論文 Methods 段逐字複述 2021 年定義）[S11]：
| 名稱 | 定義 |
|---|---|
| supramaximal resection of CE tumor | 超出顯影腫瘤邊界（**2021 年時 cut-off 尚未定義**） |
| complete resection of CE tumor | 移除全部顯影腫瘤 |
| near total resection of CE tumor | 顯影腫瘤縮減 95%–99.9% **＋ 殘餘 ≤1 cm³** |
| subtotal resection of CE tumor | 顯影腫瘤縮減 80%–94.9% **＋ 殘餘 ≤5 cm³** |
| partial resection of CE tumor | 縮減 <80% **或** 殘餘 >5 cm³（為緩解壓迫症狀而做） |
| biopsy | 沒有縮減腫瘤（只為取組織） |

*A-2. 2023 年 Neuro-Oncology 的「RANO categories for EOR in glioblastoma」——四級，只看殘餘體積*[S11]

- 世代：7 個歐美神經腫瘤中心，**回溯性**收集 **1,008 位**依 WHO 2021 分類的新診斷 IDH-wildtype 膠質母細胞瘤；
  其中 **744 位**術後接受 EORTC-26981/22981 標準放化療（TMZ/RT→TMZ），主分析在這 744 人身上做[S11]
- **supramaximal（class 1）的門檻是這篇定出來的**：在「顯影腫瘤完全切除」的病人中（n=356/365），
  再多切非顯影腫瘤，**≥60% 非顯影腫瘤縮減 ＋ 殘餘非顯影腫瘤 ≤5 cm³** 者預後明顯較好[S11]
- 四級的存活分層（**中位 OS：24 / 19 / 15 / 10 個月，P=.001**；中位 PFS：11 / 9 / 8 / 5 個月，P=.001）[S11]
  ——**這些絕對數字的使用受限，見 Claim ceiling**
- 多變項（以 class 1 為參考）：class 2 HR 1.58（CI 1.1–2.3，P=.013）／class 3 HR 1.89（CI 1.2–2.9，P=.003）／
  class 4 HR 2.4（CI 0.7–10.9，**P=.205，不顯著**）[S11]
- 連續變項版本：每上升一級 HR 1.46（CI 1.3–1.7，P=.001）；納入多變項模型後仍保留 HR 1.34（CI 1.1–1.6，P=.004）[S11]
- **關鍵反直覺結果**：多變項模型中「術後殘餘顯影腫瘤體積（cm³）」仍顯著（HR 1.03），而
  「**相對切除百分比失去預後意義**」[S11]。原文結論：「the RANO categories stratify patients solely on the volume
  of residual tumor」[S11]
- 同一模型中其他顯著因子：年齡（每歲 HR 1.02）、術前 KPS ≥90%（HR 0.76）、腫瘤位置（皮質下 vs 多發 HR 0.67）、
  **MGMT 啟動子未甲基化（HR 1.53）**[S11]（MGMT 的意義歸 B2）
- 作者自陳的方向性限制：「the favorable effects of "supramaximal CE resection" on survival are **probably limited
  to patients with less eloquent localized tumors**」；且「several factors including age, preoperative CE volume,
  tumor localization, and MGMT promotor methylation status **were associated with EOR**」[S11]
  → **這一句就是紅線 2 的自證：切得多的人本來條件就比較好。**

*A-3. 年齡分層（2026）*[S18]
- n=1,260（新診斷），其中 512 人 ≥65 歲；另 310 人為第一次復發（≥65 歲 92 人）
- 「Lower postoperative contrast-enhancing tumor volumes were favorably associated with survival on uni- and
  multivariate analyses; however, **the associations with outcome were more pronounced in younger patients.
  Only in patients <65 years, supramaximal resection was associated with more favorable survival
  (40 vs 20 months, P = .001).**」
- 復發手術：**兩個年齡層都看不到 supramaximal 的好處**；但「maximal resection of contrast-enhancing tumor was
  associated with favorable outcomes, particularly in younger patients」
- 已用傾向分數配對降低混雜[S18]

**B. Molinaro 2020（JAMA Oncol）——年齡與 IDH 分層的切除量效益**[S12]

- 設計：**回溯性、多中心世代**。發展世代 UCSF n=761（1997–2017，追蹤 9.6 年）；外部驗證 Mayo Clinic n=107、
  Ohio Brain Tumor Study n=99[S12]
- 發展世代基本資料：男性 468 人（61.5%），**中位年齡 60 歲**（IQR 51.6–67.7）
- 主要結果（**全部帶族群標籤**）：
  - **年輕 ＋ IDH-wildtype ＋ 顯影與非顯影腫瘤都積極切除**：中位 OS **37.3 個月**（95% CI 31.6–70.7）
    ——「survival similar to that of patients with IDH-mutant tumors」
  - **年輕 ＋ IDH-wildtype ＋ 顯影腫瘤切乾淨但非顯影腫瘤殘留**：中位 OS **16.5 個月**（95% CI 14.7–18.3）
  - **年長 ＋ IDH-wildtype**：從「切除顯影腫瘤」得益，中位 OS **12.4 個月**（95% CI 11.4–14.0）
  - 「the association between aggressive CE and NCE in patients with IDH-wild-type tumors **was not attenuated by
    the methylation status of the MGMT promoter**」[S12]
- 論文自己的定位語（誠實必引）：「These conclusions **may help reassess surgical strategies**」——是「重新思考」，
  不是「證明」[S12]
- 這篇也是全文獻裡「WHO 2016 分類下 GBM 的 IDH 分層中位存活」的一個引用點：
  「median patient survival of **1.2 and 3.6 years**」（IDH-wildtype vs IDH-mutant）[S12]
  ——**這個數字歸 B4，A3 不用**

**C. Brown 2016（JAMA Oncol）系統性回顧與統合分析**[S13]

- 37 篇研究、**41,117 位獨立病人**；成人新診斷幕上 GBM
- **1 年死亡率**：GTR vs STR，**RR 0.62（95% CI 0.56–0.69，P<.001，NNT 9）**
- **2 年死亡率**：GTR vs STR，**RR 0.84（95% CI 0.79–0.89，P<.001，NNT 17）**
- STR vs 切片，1 年死亡率 RR 0.85（0.80–0.91，P<.001）
- 任何切除 vs 切片：1 年 RR 0.77（0.71–0.84，P<.001，NNT 21）；2 年 RR 0.94（0.89–1.00，**P=.04**，**NNT 593**)
- 惡化風險：GTR vs STR，6 個月 RR 0.72（0.48–1.09，**P=.12，不顯著**）；1 年 RR 0.66（0.43–0.99，P<.001，NNT 26)
- **作者自己給的證據等級（必引）**：「**The quality of the body of evidence by the GRADE criteria was moderate to
  low.**」[S13]
- **NNT 593 這個數字是本篇最誠實的一根柱子**：切除 vs 切片在「2 年存活」這一格上，要治療 593 個人才多救到 1 個。
  這跟 1 年的 NNT 21 放在一起，正好教會讀者「同一個治療、不同時間點、差很多」。

**D. 5-ALA 螢光導引：Stummer 2006（Lancet Oncol）**[S14]

- 設計：**隨機對照、多中心、第三期**。322 位 23–73 歲、疑似惡性膠質瘤且**顯影腫瘤可完全切除**者，
  隨機分到 5-ALA 20 mg/kg 螢光導引（n=161）或傳統白光顯微手術（n=161）
- **兩個主要終點**：(1) 術後 72 小時內早期 MRI 上沒有殘餘顯影腫瘤的人數；(2) MRI 判定的 6 個月無惡化存活
- 次要終點：術後殘餘腫瘤體積、**整體存活**、神經功能缺損、毒性
- 分析族群：期中分析的 270 人 full-analysis population（5-ALA 139／白光 131），排除中央盲讀認定
  組織學或影像不合格者；**期中分析結果依規約導致試驗終止**
- 中位追蹤 35.4 個月（95% CI 1.0–56.7）
- **結果 1（完全切除率）**：5-ALA **90/139（65%）** vs 白光 **47/131（36%）**；
  **組間差 29%（95% CI 17–40），p<0.0001**
- **結果 2（6 個月 PFS）**：**41.0%（32.8–49.2）vs 21.1%（14.0–28.2）**；
  組間差 **19.9%（9.1–30.7），p=0.0003（Z test）**
- **安全性**：「Groups did not differ in the frequency of severe adverse events or adverse events in any organ
  system class reported within 7 days after surgery.」
- **作者的結論措辭（要照抄，不要放大）**：「Tumour fluorescence derived from 5-aminolevulinic acid enables more
  complete resections of contrast-enhancing tumour, **leading to improved progression-free survival** in patients
  with malignant glioma.」——**寫的是 PFS，不是 OS**[S14]

**限制（必寫）**
1. **隨機的是工具，不是切除量。** 這個試驗證明的是「用螢光的人切得比較乾淨、6 個月無惡化的比例比較高」，
   **不是「切得乾淨所以活得久」**。
2. **收案本身有選擇**：只收「顯影腫瘤可完全切除」的病人[S14]——位置差、切不乾淨的人一開始就不在裡面。
3. **試驗提前終止**（期中分析達標即依規約停止）[S14]——提前終止的試驗傾向高估效果量。
4. **整體存活是次要終點，主論文摘要未報告其結果**。→ **不可寫「5-ALA 延長存活」。**
5. 對照組是 2006 年的「白光顯微手術」[S14]；今天的對照（神經導航、術中 MRI、術中超音波）不一樣。

**E. 螢光 vs 術中 MRI：2023 年 JCO 的前瞻對照試驗**[S33]

- 設計：**前瞻性、多中心、平行組、中心別分派**（不是個別隨機）＋ 盲化中央影像判讀；德國 11 個中心，
  收 314 位新診斷膠質母細胞瘤；as-treated 分析 5-ALA 127 人、iMRI 150 人
- 主要終點：早期術後 MRI 上顯影腫瘤完全切除
- **結果**：完全切除（定義為殘餘 ≤0.175 cm³）5-ALA **90 人（78%）** vs iMRI **115 人（81%）**，**P=.79**
- 手術時間：iMRI 顯著較長（**316 分鐘 vs 215 分鐘**，P<.001）
- 中位 PFS 與 OS 兩組相當
- **最重要的一句**：「**The lack of any residual contrast enhancing tumor (0 cm³) was a significant favorable
  prognostic factor for PFS (P < .001) and OS (P = .048), especially in methylguanine-DNA-methyltransferase
  unmethylated tumors (P = .006).**」；結論「Neurosurgical interventions in newly diagnosed glioblastoma shall aim
  for **safe complete resections with 0 cm³ contrast-enhancing residual disease**」[S33]

→ 這篇讓 A3 有一個很乾淨的收束：**目標是「0」，工具可以有很多種，而工具之間分不出高下。**

**F. 喚醒手術與功能保留**

*F-1. De Witt Hamer 2012（JCO）統合分析*[S15]
- **90 篇 1990–2010 年發表的研究、8,091 位成人**幕上浸潤性膠質瘤切除手術，有或沒有術中電刺激定位（ISM）
- **晚期嚴重神經功能缺損**：有 ISM **3.4%（95% CI 2.3%–4.8%）** vs 沒有 ISM **8.2%（95% CI 5.7%–11.4%）**；
  **校正後 OR 0.39（95% CI 0.23–0.64）**
- 影像確認的全切除率：**ISM 75%（66%–82%）** vs 非 ISM **58%（48%–69%）**
- **關鍵誠實數字**：ISM 組有 **99.9%（99.9%–100%）** 的手術涉及功能區，非 ISM 組 95.8%（73.1%–99.8%）
  ——「Eloquent locations were involved in...」[S15]。→ 兩組不是同一群病人。
- 這是**觀察性研究的統合分析**（原文：「This study addresses glioma surgery outcome on the basis of a
  meta-analysis of **observational studies**」）；作者結論用的是「should be universally implemented as standard of
  care」，**強度高於資料等級**，寫作者要標明這是作者的主張[S15]

*F-2. GLIOMAP 2022（Lancet Oncol）傾向分數配對*[S16]
- 4 個中心（荷蘭 2、比利時 1、美國 1），2010-01-01 至 2020-10-31 收 3,919 人，
  **1,047 位功能區／近功能區原發性膠質母細胞瘤**進入分析；1:3 傾向分數配對後 **536 人**（喚醒 134／睡著 402）
- **配對世代主要結果**：
  - 術後 **3 個月**神經功能缺損：喚醒 **26/120（22%）** vs 睡著 **107/323（33%）**，**p=0.019**
  - 術後 **6 個月**：喚醒 **30/115（26%）** vs 睡著 **125/305（41%）**，**p=0.0048**
  - 中位 OS：**17.0 個月（95% CI 15.0–24.0）vs 14.0 個月（13.0–16.0）**，p=0.00054
  - 中位 PFS：**9.0 個月（8.0–11.0）vs 7.3 個月（6.0–8.8）**，p=0.0060
- 次族群（<70 歲、NIHSS 0–1、KPS 90–100）方向一致[S16]
- **限制**：傾向分數配對 ≠ 隨機；由主治醫師或多專科會議決定用哪一種麻醉方式（原文：「as per treating
  physician or multidisciplinary tumour board decision」）[S16]

*F-3. 隨機證據的狀態（必寫）*
- **SAFE trial**（NCT03861299，喚醒開顱 vs 全身麻醉手術，膠質母細胞瘤）：ClinicalTrials.gov 於 2026-09-03
  查詢顯示狀態 **RECRUITING**，最後更新提交日 **2023-11-18**[S31]。
  → **到目前為止，喚醒手術 vs 睡著手術在膠質母細胞瘤沒有已發表的隨機試驗結果。**

**G. 手術的併發症與安全性**

- RANO resect 2023 世代（n=1,008 新診斷 IDH-wildtype GBM）：「Surgical resection was well tolerated with
  **161 patients (15.8%) experiencing new neurologic deficits which were generally mild**」[S11]
- RANO 風險模型 2025 訓練世代（n=1,003）：「In **156 patients (15.6%)**, surgical intervention resulted in new
  postoperative deficits of any kind」[S17]
- RANO 2023 另一個重要觀察：做到 supramaximal 切除的病人，**新發神經缺損的比率沒有增加**
  （「the rate of new postoperative neurologic deficits was not increased in such patients」）[S11]
  ——但同一篇作者也提醒這可能反映「醫師只在不危險的位置才敢多切」[S11]
- 術後風險分層（RANO risk model 2025）：由**殘餘腫瘤、MGMT 啟動子甲基化狀態、年齡、術後 KPS** 四項組成的
  0–9 分加總分數，分為低風險（0–2）、中風險（3–5）、高風險（6–9）；在 258 人的外部世代驗證[S17]
- EANO：立體定位切片「is associated with a low risk of morbidity and a high level of diagnostic accuracy」[S5]

**手術死亡率**：本次查證**未取得可引用的 30 天／院內死亡率數字**（RANO 兩份世代論文均未在可取得文字中報告，
見 FAIL-7）。→ **文章不可寫手術死亡率的百分比。** 只能寫「開顱手術有風險，包括出血、感染、
新的神經功能缺損（上述兩個大型世代都約一成五，且多為輕度）」[S11][S17]。

### 反方向的資料（誠實必列）

1. **全部是觀察性。** Brown 2016 自陳 GRADE moderate-to-low[S13]；Karschnia 2021 自陳 class of evidence
   IIB–IV[S10]；RANO 2023、Molinaro 2020、GLIOMAP 2022 全為回溯或非隨機[S11][S12][S16]；
   De Witt Hamer 2012 是觀察性研究的統合分析[S15]。**沒有任何隨機試驗把病人隨機分到「切多」與「切少」。**
2. **切得多的人本來就不一樣。** RANO 2023 自己算出來：年齡、術前腫瘤體積、腫瘤位置、MGMT 甲基化狀態
   **都與切除程度相關**[S11]；GLIOMAP 的喚醒組與睡著組由醫師選擇[S16]；De Witt Hamer 的 ISM 組幾乎 100%
   都在功能區[S15]。
3. **2 年存活這一格的效果小得多。** Brown 2016：任何切除 vs 切片，2 年死亡率 RR 0.94、**P=.04、NNT 593**[S13]。
4. **切除量的好處有年齡界線。** ≥65 歲者，supramaximal 切除的存活關聯不成立[S18]。
5. **兩種「切得乾淨」的工具打平。** iMRI 與 5-ALA 的完全切除率沒有差別（81% vs 78%，P=.79）[S33]。
6. **喚醒手術沒有隨機證據**（SAFE trial 仍在收案）[S31]。
7. **切片不是「放棄」。** EANO 明文：即使不打算做腫瘤特異性治療，確定的組織診斷仍有助於與病人及照顧者
   討論[S5]；而 RANO 2023 也觀察到 class 4（切片）的病人比較常直接轉安寧[S11]——這是**臨床選擇**造成的分布，
   不是切片本身的效果。**這一條對紅線 2 的下半段（不可讓「切不乾淨」讀成沒救）非常重要。**

### Claim ceiling（A3）

**可寫**
- 「現在國際上描述切除程度的分級（RANO），**看的是術後 MRI 上還剩多少（cm³），不是切掉了幾成**；
  在多變項分析裡，切掉幾成失去了預後意義」[S11]
- 「四個等級：supramaximal（超出顯影邊界再多切）／maximal（顯影腫瘤幾乎全清）／submaximal／biopsy，
  級數越高（切得越少）預後越差，每上一級的死亡風險比 1.46；納入年齡、體能、位置、MGMT 之後仍保留 1.34」[S11]
- 「supramaximal 的門檻是：顯影腫瘤全部切掉，**再加上非顯影腫瘤縮減六成以上且殘餘 ≤5 cm³**」[S11]
- 「這個好處在 65 歲以下才看得到；65 歲以上，把顯影腫瘤清乾淨仍有關聯，但『再多切』沒有」[S18]
- 「統合分析（37 篇、41,117 人）：全切除比次全切除，1 年死亡風險 RR 0.62、2 年 0.84；
  **但作者自己給的證據等級是中到低**」[S13]
- 「同一份統合分析裡，『任何切除 vs 只做切片』在 2 年存活這一格，NNT 是 593」[S13]
- 「Molinaro 2020：年輕、IDH-wildtype、顯影與非顯影腫瘤都切得多的那一組，中位存活 37.3 個月；
  同樣年輕、顯影切乾淨但非顯影殘留的是 16.5 個月；年長者從清掉顯影腫瘤得益，12.4 個月
  ——**回溯性資料，且切得多的人本來條件就不同**」[S12]（**如引用這些絕對月數，必須同段標「回溯性」＋
  「數字怎麼讀見〈那個數字，我要怎麼跟你講〉」**）
- 「5-ALA 隨機試驗：完全切除率 65% vs 36%（差 29%，p<0.0001）；6 個月無惡化存活 41.0% vs 21.1%
  （差 19.9%，p=0.0003）；嚴重不良事件兩組沒有差別」[S14]
- 「5-ALA 那個試驗隨機的是**用不用螢光**，主要終點是完全切除率與 6 個月 PFS，**存活是次要終點**，
  而且試驗在期中分析後依規約終止」[S14]
- 「術中 MRI 沒有比 5-ALA 好：完全切除率 81% vs 78%（P=.79），但手術長了一百分鐘；
  真正有預後意義的是**殘餘 0 cm³**」[S33]
- 「術中電刺激定位（喚醒手術用的技術）：統合分析顯示晚期嚴重神經缺損 3.4% vs 8.2%（OR 0.39），
  全切除率 75% vs 58%——**但這是觀察性研究的統合分析，而且有做定位的手術幾乎 100% 在功能區**」[S15]
- 「GLIOMAP 傾向分數配對：喚醒組 6 個月神經缺損 26% vs 41%（p=0.0048）——**不是隨機試驗**；
  真正的隨機試驗（SAFE）到 2026 年 9 月仍在收案」[S16][S31]
- 「兩個各約一千人的大型世代：術後新發神經功能缺損約 15.6%–15.8%，多為輕度」[S11][S17]

**不可寫（硬上限）**
- ❌「切得越乾淨活得越久」的**因果**寫法。所有資料都是觀察性；**沒有隨機分派切除量的試驗**[S10][S13]
- ❌「5-ALA 延長存活」。試驗的存活是次要終點且未在可引用的摘要中報告結果[S14]
- ❌「喚醒手術比較安全／活得久」的**因果**寫法。無隨機證據[S31]，觀察性資料的兩組不是同一群人[S15][S16]
- ❌「切不乾淨就沒救」。RANO class 4 的多變項 HR 是 2.4，**95% CI 0.7–10.9，P=.205，不顯著**[S11]；
  且 class 4 的病人分布本身受臨床決策影響[S11]
- ❌ 任何**手術死亡率的百分比**（查不到可引用來源，FAIL-7）
- ❌ 把 RANO 的中位 OS（24/19/15/10 個月）當成「你會活多久」丟給讀者。SPEC §六：預後數字歸 B4。
  **A3 使用時必須(a)標明是回溯世代、(b)同段一句指向 `gb-numbers`**
- ❌ 台灣的 5-ALA 藥證、給付、自費金額（**查不到**，FAIL-1／FAIL-3）
- ❌ 不點名醫院、不寫「本院有沒有這台機器」（固定紅線）

### Caveats／safety notes（寫作者必寫）

- **紅線 2 的雙向**：既不可寫成「切乾淨＝活久」的保證，也不可讓「只做了切片」的讀者讀成沒救。
  建議收尾邏輯：「切除程度是我們**可以努力**的少數幾件事之一；但它不是唯一一件，也不是保證。
  而且切多少能安全地切，很大一部分在腫瘤長的位置，不在你或醫師的意志。」
- **一定要寫出「切得多的人本來就不一樣」**——RANO 2023 自己算出年齡／體積／位置／MGMT 都與切除程度相關[S11]。
- **切片不是放棄**：EANO 原文可引[S5]。
- 「supramaximal」在中文很容易被讀成「切得比腫瘤多，等於傷到好的腦」。要解釋：那是切掉**影像上不顯影、
  但已經被腫瘤浸潤**的區域，而且 RANO 的資料顯示這樣做的病人**新發神經缺損沒有增加**[S11]——同時說明
  這很可能是因為醫師只在相對安全的位置才這樣做[S11]。
- 急症與術後照護指向 C4。

### 台灣端（A3）

- **5-ALA（Gliolan）的台灣藥證**：**gap**。食藥署西藥許可證查詢（info.fda.gov.tw）DNS 無法解析、
  data.fda.gov.tw 開放資料 API 301 導向且無可用端點，2026-09-03 兩路均失敗（FAIL-1／FAIL-3）。
- **5-ALA 的健保給付／自費**：**gap**（FAIL-2）。
- **術中 MRI、術中神經監測、喚醒手術的給付**：本次未查（不在 SPEC §八 清單）；文章一律寫「問醫務課／個管師」。
- → 正文寫法（照 SPEC 紅線 3 的精神類推）：「**5-ALA 在台灣的藥證與給付狀態，我這次查不到可以引用的官方
  資料，請直接問你的神經外科團隊或醫院醫務課。**」**不可寫「台灣有／沒有」。**

### 給繪圖組的數字（A3）

SPEC §七 沒有指定 A3 的自繪圖，但若補一張，最有價值的是**「切幾成」→「還剩多少」的觀念轉換圖**：

- 四級 RANO 分級與其定義[S11]：
  - class 1 supramaximal：顯影腫瘤 0 殘餘 ＋ 非顯影腫瘤縮減 ≥60% 且殘餘 ≤5 cm³
  - class 2 maximal：顯影腫瘤幾乎清空（原 complete ＋ near total，near total 門檻為 ≤1 cm³ 殘餘）
  - class 3 submaximal：原 subtotal（≤5 cm³ 殘餘）＋ partial
  - class 4 biopsy
- 分層 HR（以 class 1 為參考）：1.58 / 1.89 / 2.4（後者不顯著）[S11]
- 對照條：Brown 2016 的 GTR vs STR，1 年 RR 0.62（NNT 9）、2 年 RR 0.84（NNT 17）；
  任何切除 vs 切片 2 年 RR 0.94（NNT 593）[S13]
- 5-ALA 對照條：完全切除率 65% vs 36%[S14]；iMRI vs 5-ALA 81% vs 78%[S33]
- 併發症條：新發神經缺損約 15.6%–15.8%（多為輕度）[S11][S17]
- **圖上必須有一行**：「以上全部來自回溯性／非隨機資料」


---

## gb-pathology〈報告等兩週，在等什麼〉（A4）

### Key facts

**A. IDH 檢測：免疫組化 vs 定序（EANO 有可逐字引的判準）**

- **常規第一步是免疫組化**：「Tissue specimens obtained through biopsy sampling in patients with diffuse gliomas
  are routinely assessed by immunohistochemistry for the presence of **R132H-mutant IDH1 and loss of nuclear
  ATRX**.」[S5]
- **什麼情況免疫組化陰性就可以定案**（原文，這是最實用的一段）：
  「In patients aged **>55 years** with a histologically typical glioblastoma, without a pre-existing lower grade
  glioma, with a **non-midline tumour location** and with **retained nuclear ATRX expression**, immunohistochemical
  negativity for IDH1 R132H **suffices** for the classification as IDH-wild-type glioblastoma.」[S5]
- **其他所有情況都要定序**：「In all other instances of diffuse gliomas, a lack of IDH1 R132H immunopositivity
  should be followed by **IDH1 and IDH2 DNA sequencing** to detect or exclude the presence of **non-canonical
  mutations**.」[S5]
  建議欄位（帶等級）：「If immunohistochemistry for IDH1 R132H is negative, sequencing of IDH1 codon 132 and
  IDH2 codon 172 should be conducted in **all WHO grade 2 and 3 diffuse astrocytic and oligodendroglial gliomas as
  well as in all glioblastomas of patients aged <55 years**（C: IV; L: B）」[S5]
- **為什麼**：R132H 只是最常見的那一種。CATNON 的實測分布可以當旁證——在該試驗的 IDH1 陽性者中，
  **R132H 佔 86.9%／84.7%**，其餘為 R132C（4.8%／4.3%）、R132G、R132L、R132S；另有約 3% 是 IDH2
  （R172K、R172W、R172G）[S26]。→ **免疫組化只認得其中一種；剩下那一成多，只有定序看得到。**
- **後顱窩／腦幹的特別提醒**：「Infratentorial diffuse gliomas therefore tend to be classified incorrectly if
  examined by IDH1 R132H immunohistochemistry only; accordingly, **DNA sequencing for rare mutations in IDH1 and
  IDH2 is required**.」[S5]

**B. MGMT 啟動子甲基化：方法差異與 cut-off 不一致（A4 的核心誠實段）**

- **EANO 認可的方法**：「MGMT promoter methylation status should be tested using **methylation-specific PCR,
  pyrosequencing or methylation arrays (such as the MGMT-STP27 model)**.」[S5]
- **EANO 自己列出兩個未解問題**：「challenges remain, including: (1) **establishing reliable MGMT promoter
  methylation status assays that can be used with high interlaboratory agreement**, and (2) estimating the effect
  of **limited MGMT promoter methylation, an intermediate state between the non-methylated and methylated
  phenotypes**, on outcomes.」[S5]
- **免疫組化不能用來測 MGMT**：「**Immunocytochemistry is not an adequate method to determine the MGMT promoter
  methylation status.**」[S5]
- **具體的方法學差異（Mansouri 2019，Neuro-Oncology）**[S20]：
  - 摘要層級：「**The methods and optimal cutoff definitions for MGMT status determination remain controversial.
    Variation in detection methods between laboratories presents a major challenge for consensus.**」
  - 生物學背景：MGMT 啟動子的 CpG island 長 **777 bp、含 97 個 CpG 二核苷酸**；影響轉錄的主要是 DMR1、DMR2
    兩個區段——**不同方法測的是不同的 CpG 位點**，這就是不一致的根源
  - **MSP（甲基化特異性 PCR）**：多個隨機試驗用的方法，結果是**質性判讀**（跑膠、看有沒有帶）。
    誠實數字：「Retrospectively assessing 465 GBM samples in which MGMT status was determined using MSP,
    **Xia et al demonstrated an inconsistency rate of 12% among their MSP replicates.**
    The survival of patients with inconsistent results paralleled that of patients with unmethylated samples.」
  - **qMSP（定量 MSP）**：以標準曲線把甲基化 MGMT 對未甲基化基因（如 ACTB）做正規化；
    「The **technical cutoff**, where the probability of being methylated/unmethylated is 50%, is usually applied
    to dichotomize the test result... The term "**equivocal**" or "**gray zone**" has also been applied to the
    qMSP method, as **the uncertainty in the vicinity of the cutoff is high.**」
  - **Pyrosequencing（焦磷酸定序）**：可以量到每一個 CpG 位點的甲基化百分比。
    「Reifenberger et al demonstrated a strong concordance between both assays when a cutoff of **<8% vs ≥8%**
    methylated alleles was used for the pyrosequencing method. Furthermore, a significantly better outcome was
    achieved in response to alkylating chemotherapy when a cutoff of **>25%** methylated alleles was used.
    **However... there is uncertainty regarding the cutoff to define MGMT "methylated" versus "unmethylated" status
    for stratifying patients into treatment groups.**」
    另外：「"**partial methylation**," wherein not all CpG sites are methylated, is a scenario that arises with
    pyrosequencing that is **difficult to interpret in terms of clinical relevance**.」
  - 各方法的優缺點表（原文欄位）：qMSP「Cutoff point validated in clinical trials」；
    pyrosequencing「**Cutoff threshold not validated in clinical trials**」＋高成本、耗時；
    HRM 與甲基化陣列同樣標「**Cutoff not validated in clinical trials**」[S20]
  - 作者自己的立場：「In our opinion, **qMSP provides a good and reproducible balance between reliability,
    availability, and cost.**」[S20]
- **同一個檢體、兩種方法只有中度一致的實測**：CATNON 在 IDH-wildtype 腫瘤中比較 MS-PCR 與 MGMT-STP27
  演算法，「percentage concordance **85%**, κ statistics **0.67 (95% CI 0.55–0.80)**」[S26]

→ **A4 可以誠實地說：「MGMT 這一行不是量血糖，它是『不同實驗室用不同尺量、而且那把尺的刻度還沒有共識』。」**
**MGMT 對治療的意義歸 B2（SPEC §六），A4 只寫「這個數字怎麼來的、為什麼會不一樣」。**

**C. 1p/19q 共缺失：為什麼要驗、以及 FISH 的假陽性**

- **驗誰**：EANO 建議「1p/19q codeletion status should be determined in **all IDH-mutant gliomas with retained
  nuclear expression of ATRX**（C: II; L: B）」[S5]
- **定義是「整臂」缺失**：「Oligodendroglioma is genetically defined by concomitant IDH (IDH1/IDH2) mutation and
  **whole-arm** 1p/19q codeletion.」[S21]
- **FISH 的結構性限制**：「Codeletion of 1p/19q traditionally evaluated by fluorescence in situ hybridization
  (FISH) **cannot distinguish partial from whole-arm 1p/19q codeletion. Partial 1p/19q codeletion called positive
  by FISH is diagnostically a "false-positive" result.**」[S21]
- **假陽性的量**（Mayo Clinic，n=223 成人瀰漫性星細胞膠質瘤，以染色體微陣列對照）：
  「The overall estimated **false-positive FISH 1p/19q codeletion rate was 3.6% (8/223)**」；
  IDH-mutant 4.6%（4/86）vs IDH-wildtype 2.9%（4/137），差異不顯著（P=.49）[S21]
  結論：「**Selective 1p/19q codeletion testing and cautious interpretation for conflicting FISH and
  histopathological findings are recommended to avoid potential misdiagnosis.**」[S21]
- **另一組資料（義大利，n=65 膠質瘤，NGS SNP panel vs FISH）**：60 個可比對案例中 **49 例（81.7%）** 兩法一致；
  **其餘 11 例**，NGS 顯示只是 FISH 探針落點附近的**間質性擴增或缺失**，「leading to a **mistaken overdiagnosis
  of 1p/19q codeletion by FISH**」[S22]
- **臨床意義（不可省）**：1p/19q 決定的是「這是不是寡樹突膠質瘤」，而寡樹突膠質瘤的治療與預後跟星細胞瘤
  **不一樣**（見 A5）。所以這一項驗錯，走的是另一條路。

**D. ATRX、TERT、EGFR、+7/−10**

- **ATRX**：常規免疫組化項目之一（與 IDH1 R132H 一起做）[S5]；**若 IDH 突變與 1p/19q 狀態已經由更完整的分子套組
  一次涵蓋，ATRX 免疫組化就不是必要的**（「ATRX immunohistochemistry is not necessary if IDH mutation and 1p/19q
  codeletion status are captured within one more extensive molecular marker panel assay」）[S5]
  在 EANO 的判準裡，**ATRX 核染色保留**是「>55 歲、IDH1 R132H 免疫組化陰性即可定案為 IDH-wildtype GBM」
  的四個條件之一[S5]
- **TERT 啟動子突變／EGFR 擴增／+7−10**：三者任一即可讓 IDH-wildtype 的成人瀰漫性星細胞膠質瘤被定為
  glioblastoma, CNS WHO grade 4[S1][S2]。技術注意事項（cIMPACT-NOW 原文）：
  - EGFR 必須是 **focal high-level** 擴增；trisomy 7 這種低倍數增加不算；**EGFR 免疫組化不足以判定擴增**[S2]
  - +7/−10 的特異性佳，「with the rare exception of PXAs, where additional testing (e.g. **BRAF V600E**) may be
    warranted in diagnostically challenging cases」[S2]
  - +7q/−10 與 +7/−10q 這類「不完整」的組合，各約出現在 10% 的組織學 grade II/III IDH-wildtype 瀰漫性星細胞
    膠質瘤，預後與完整的 +7/−10 相似[S2]
- **CDKN2A/B 同型合子缺失**：在 IDH-mutant 星細胞瘤，**即使沒有微血管增生或壞死，也直接定 CNS WHO grade 4**[S1]
  → 這是 A5 讀者最需要知道的一個字（也是 A4 的「為什麼分子報告會改掉診斷名稱」的第二個例子）

**E. Ki-67**

- **WHO CNS5 的分級與診斷判準裡沒有 Ki-67。** CNS5 列出的分子分級參數是 CDKN2A/B 同型合子缺失（IDH-mutant
  星細胞瘤）與 TERT 啟動子突變／EGFR 擴增／+7−10（IDH-wildtype 瀰漫性星細胞瘤）[S1]；
  組織學參數是微血管增生與壞死[S1][S2]。**Ki-67 不在任一份判準裡。**
- **可寫的上限**：「Ki-67 是在數『正在分裂的細胞比例』，它讓病理科對腫瘤的活躍程度有個感覺；
  **但它不是 2021 年這套分類拿來定名字或定等級的依據**。」
- **不可寫**：任何 Ki-67 的百分比門檻（例如「超過 X% 就是高惡性度」）——**本次查證未取得可引用的閾值來源**
  （FAIL-8）。

**F. 甲基化圖譜（methylation profiling）在哪些情況會改診斷**

- **量的證據**：Capper 2018（Nature 555:469–474，OA）：跨全部 entity 與年齡層的 CNS 腫瘤 DNA 甲基化分類法，
  「we show that the availability of this method may have a substantial impact on diagnostic precision compared to
  standard methods, **resulting in a change of diagnosis in up to 12% of prospective cases**」；
  並提供免費線上分類工具[S19]
- **WHO CNS5 對它的定位（要照原文，很節制）**[S1]：
  - 「At this time, methylome profiling is **an effective ancillary method** for brain and spinal cord tumor
    classification **when used alongside other, standard technologies, including histology**.」
  - **什麼時候它最有價值**：「methylome profiling may be **the most effective way to characterize some tumors with
    unusual morphological features** and may be **the only current way to identify some rare tumor types and
    subtypes**. The method also has utility **when small biopsy samples are limiting** for standard technologies.」
  - **它可以當替身，但有界線**：「Methylome profiling may also be used as a surrogate marker for genetic events,
    for instance when a methylome signature is characteristic of an IDH-wildtype glioblastoma in the absence of
    IDH mutation testing—**but methylome profiling cannot serve as a surrogate when targeted therapies and clinical
    trials require the demonstration of specific mutations prior to patient treatment.**」
  - **判讀有分數門檻**：「thresholds may be set at **0.84 or 0.90**, and pathologists should be **wary about
    endorsing suggested diagnoses with scores below 0.84** and should **probably discard recommendations if scores
    are below 0.50**.」
  - **它做不好的地方**：「methylome profiling **can struggle with classification of low-grade diffuse gliomas**.」
  - **可及性**：「the technology is **currently not widely available**」
- **衛生科技評估層級（加拿大安大略，2025）**[S32]：系統性回顧納入 38 篇研究。
  「Compared with conventional testing alone, DNA methylation-based classifier tests are an adjunct tool that
  **may improve CNS tumour classification (GRADE: Moderate)**. The tests may improve downstream patient outcomes,
  although the evidence is **very uncertain (GRADE: Very low)**. **Unclassifiable test results may increase time
  to treatment**, but the evidence is very uncertain (GRADE: Very low).」
  規模與成本：估計安大略每年約 716 位「診斷困難」的原發性 CNS 腫瘤病人；每人費用 CAD $1,500；
  若對全部困難案例做第二線甲基化分類，**可改善其中 195 人的診斷**，每改善一例的增量成本效果比 CAD $5,521[S32]
  → **這組數字是外國制度的成本資料，寫進台灣文章時必須標明是加拿大安大略省的評估，且不可換算成台幣或
  暗示台灣的價格（費用紀律）。**

**G.「報告要等多久」——沒有可引用來源**

本次查證**未取得任何可引用的病理報告週轉時間資料**（無論國際或台灣）。
→ **文章寫成診間語言，不要編數字。** 建議寫法（不含任何時間數字）：

> 「冷凍切片當天可以講一個大方向。真正的報告要等，因為它不是一份報告，是好幾層疊起來的：
> 先固定、包蠟、切片、染色，看形態；然後做免疫染色；不夠的再送分子檢測——有些要定序，有些要跑陣列，
> 有些要送出去做。**每多一層，就多等一次。** 每一層都可能改掉上一層的結論，所以我們不會半路先講一個
> 可能要收回的答案。」

（EANO 的一句可以佐證這個「不要為了快而犧牲完整」但也「不要拖到延誤治療」的張力：
「molecular diagnostic algorithms for patients with glioma should be standardized and **should not result in
delays in the administration of radiotherapy or tumour-specific pharmacotherapy**」[S5]。）

**H.「為什麼報告會改掉診斷名稱」——A4 的收束**

三個可引的機制：
1. **分子條件會蓋過組織學等級**：看起來像 grade 2/3，驗到 TERT／EGFR 擴增／+7−10 任一 → 名字變成
   glioblastoma, IDH-wildtype, CNS WHO grade 4[S1][S2]
2. **CDKN2A/B 同型合子缺失** → IDH-mutant 星細胞瘤直接變 grade 4，即使沒有壞死或微血管增生[S1]
3. **甲基化圖譜**在最多 12% 的前瞻案例中改變診斷[S19]
4. 加上一個「不是改診斷、是補完診斷」的情況：報告上的 **NOS 後綴**代表分子檢測還沒做完或做失敗；
   **NEC** 代表做完了但湊不出標準 WHO 診斷[S1]

### 反方向的資料（誠實必列）

- 免疫組化不是壞方法，只是**認得的範圍窄**：EANO 明文允許在特定條件下（>55 歲、典型 GBM、非中線、ATRX 保留）
  只靠免疫組化陰性就定案[S5]。不要把 A4 寫成「免疫組化不可靠」。
- MGMT 的方法學爭議**不代表這個檢測沒有用**：qMSP 的技術 cut-off 在多個 GBM 試驗中被證明是良好的預後預測
  （「The technical cutoff has shown to be a good predictor of outcome in GBM trials where patients have been
  treated with TMZ」）[S20]。
- 甲基化圖譜的**下游病人結果證據等級是 Very low**[S32]；WHO CNS5 也只把它定位為 ancillary method[S1]。
  不可寫成「做了甲基化圖譜就準了」。
- FISH 的 1p/19q 假陽性率 **3.6%**[S21]——是「要注意」，不是「不可信」。

### Claim ceiling（A4）

**可寫**
- 「IDH 先做免疫組化（只認 IDH1 R132H 這一種）；55 歲以下、或組織學不典型、或中線位置、或 ATRX 有變化的，
  免疫組化陰性還要再定序」[S5]
- 「免疫組化只認得最常見的那一種 IDH 突變；在一個大型試驗裡，R132H 大約佔八成五，其餘要靠定序」[S26]
- 「MGMT 可以用 MSP、焦磷酸定序或甲基化陣列測；**免疫組化不能拿來測 MGMT**」[S5]
- 「不同實驗室的一致性、以及『部分甲基化』這個中間狀態，是指引自己列出來還沒解決的問題」[S5]
- 「MSP 重複做同一批檢體，有 12% 不一致；焦磷酸定序的門檻在 8% 與 25% 之間有不同用法，
  而且這些門檻**沒有在臨床試驗裡被驗證過**」[S20]
- 「同一批 IDH-wildtype 檢體，MS-PCR 與甲基化陣列演算法的一致率 85%（κ 0.67）」[S26]
- 「1p/19q 要驗的是**整臂**缺失；FISH 分不出整臂與部分缺失，假陽性率約 3.6%」[S21]；
  「另一組資料裡，60 個 FISH 判讀中有 11 個被 NGS 認定是過度診斷」[S22]
- 「ATRX 如果已經被更完整的分子套組涵蓋，就不一定要單獨做免疫染色」[S5]
- 「EGFR 那一格要的是局部高倍數擴增，trisomy 7 不算，免疫染色不能用」[S2]
- 「CDKN2A/B 同型合子缺失會讓 IDH-mutant 星細胞瘤直接變成 grade 4」[S1]
- 「甲基化圖譜在最多 12% 的前瞻案例中改變診斷；它的判讀有分數門檻（低於 0.84 要小心、低於 0.50 建議捨棄）；
  它對低惡性度瀰漫性膠質瘤反而吃力；而且它不能取代『試驗或標靶治療要求的特定突變證明』」[S19][S1]
- 「報告上的 NOS ＝ 分子檢測還沒做完或失敗；NEC ＝ 做完了但湊不出標準診斷」[S1]

**不可寫**
- ❌ **任何病理報告的等待天數／週數**（查不到來源，FAIL-9）——寫成診間語言
- ❌ **任何 Ki-67 的百分比門檻**（查不到來源，FAIL-8）
- ❌ **MGMT 甲基化與治療效果／存活的數字**——歸 B2（SPEC §六）。A4 只寫「這個數字怎麼測出來的」
- ❌ 任何檢測的**台灣自費金額或給付狀態**（本次未查到可引用官方條文）——寫「問醫務課」
- ❌「甲基化圖譜比病理科醫師準」——WHO CNS5 明文是 ancillary、要與組織學並用[S1]
- ❌ 把加拿大安大略的 CAD $1,500／$5,521 換算成台幣或暗示台灣價格[S32]

### Caveats／safety notes（寫作者必寫）

- **等報告的焦慮是這一篇的真正主題。** 不要用「請耐心等候」帶過；要具體說明每一層在做什麼、為什麼不能跳。
- 「報告改了名字」在病人耳裡等於「病變嚴重了」。**一定要明說：改的是分類的規則，不是你的病在那兩週裡變壞。**
  可以用 A1 的 CBTRUS 資料佐證「連美國的癌症登記都還在追這套新規則」[S4]。
- 「NOS」很容易被讀成「查不出來」。要寫清楚是「還沒測完」[S1]。
- 若讀者的報告寫 **IDH-mutant**，一句指向 A5〈報告寫 IDH-mutant：你走的是另一條路〉。
- 若報告寫 **MGMT**，一句指向 B2。

### 台灣端（A4）

- 台灣各醫院的分子檢測可及性、健保給付、自費金額：**gap**（本次未取得可引用的官方條文；
  data.nhi.gov.tw 502、info.fda.gov.tw DNS 失敗）。文章寫「問醫務課／個管師」。
- 病理報告週轉時間的台灣數據：**gap**。

### 給繪圖組的數字（A4）

SPEC §七 未指定 A4 圖。若補一張「報告的層次圖」，可用的 PASS 結構：
- 第 1 層 組織形態（微血管增生／壞死）[S1][S2]
- 第 2 層 免疫組化（IDH1 R132H、ATRX；**MGMT 不能用免疫組化**[S5]；**EGFR 不能用免疫組化判擴增**[S2]）
- 第 3 層 定序／FISH／陣列（IDH1 codon 132、IDH2 codon 172[S5]；1p/19q 整臂[S21]；TERT／EGFR／+7−10[S1][S2]；
  CDKN2A/B[S1]；MGMT 甲基化[S5][S20]）
- 第 4 層 甲基化圖譜（改診斷最多 12%[S19]；分數門檻 0.84／0.50[S1]）
- 出口：整合式診斷（integrated diagnosis）＋分層報告（layered report）[S1]；NOS／NEC 後綴的意思[S1]
- 旁註條：MSP 重複性不一致 12%[S20]；FISH 1p/19q 假陽性 3.6%[S21]；MS-PCR vs 陣列一致率 85%（κ 0.67）[S26]

---

## gb-lowgrade〈報告寫 IDH-mutant：你走的是另一條路〉（A5）【紅線 3】

### Key facts

**A. 兩種病，不是一種**

- **定義（INDIGO 論文的教科書式一句，可直接引）**：「Gliomas that harbor a mutation in IDH1/IDH2 and an
  unbalanced translocation between chromosomes 1 and 19 ("1p/19q-codel") are defined as **oligodendrogliomas**,
  while IDH-mutant gliomas **without** 1p/19q codeletion ("1p/19q-non-codel") are defined as **astrocytomas**.」[S23]
- **這不是良性**（紅線 3 的第一句）：「IDH-mutant grade 2 oligodendrogliomas and astrocytomas **grow continuously,
  albeit slowly, infiltrate the normal brain, and eventually become aggressive tumors with accelerated tumor growth
  and neovascularization**, reflected by appearance of contrast enhancement on MRI.」[S23]
  以及：「Isocitrate dehydrogenase (IDH)-mutant grade 2 gliomas are **malignant brain tumors that cause
  considerable disability and premature death**.」[S23]
- **兩條路的治療建議不一樣**（ASCO-SNO 2022／2025，逐字）[S6][S7]：
  - 寡樹突膠質瘤 grade 2：「should be offered **radiation in combination with procarbazine, lomustine, and
    vincristine (PCV)**（Evidence quality: Moderate; Strength: **Strong**）」；
    「**Temozolomide is a reasonable alternative to PCV when toxicity is a concern**（Evidence quality: Low;
    Strength: Conditional）」[S7]
  - 星細胞瘤（IDH-mutant, 1p/19q non-codeleted）grade 2：「should be offered **radiation therapy with adjuvant
    chemotherapy (temozolomide or PCV)**（Evidence quality: Moderate; Strength: **Strong**）」[S7]
  - 星細胞瘤 grade 3：「should be offered **RT and adjuvant TMZ**」[S6]
  - 星細胞瘤 grade 4（IDH-mutant）：「may follow recommendations for **either** astrocytoma, IDH-mutant, 1p19q
    non-codeleted CNS WHO grade 3 **or** glioblastoma, IDH-wildtype, CNS WHO grade 4」[S6]
    → 這一句很重要：**IDH-mutant grade 4 是灰帶，指引自己說可以走兩邊。**
- **CDKN2A/B 同型合子缺失**會讓 IDH-mutant 星細胞瘤直接被定為 grade 4，即使沒有壞死或微血管增生[S1]

**B. RTOG 9802（Buckner 2016, NEJM）——放療加 PCV 的長期存活**[S24]

- 收案條件（**族群標籤要帶**）：grade 2 星細胞瘤／寡星細胞瘤／寡樹突膠質瘤；
  **<40 歲且次全切除或僅切片者**，**或 ≥40 歲不論切除程度者**。1998–2002 年收 **251 位可評估病人**
- 隨機：單獨放療 vs 放療後接 **6 個療程 PCV**
- 中位追蹤 **11.9 年**，55% 病人已死亡
- **主要結果**：中位整體存活 **13.3 年 vs 7.8 年**（HR for death **0.59**，**P=0.003**）
- **10 年無惡化存活 51% vs 21%**；**10 年整體存活 60% vs 40%**
- Cox 模型：放療＋化療、以及寡樹突膠質瘤的組織學，是 PFS 與 OS 兩者的有利預後因子[S24]
- **時代標籤（必寫）**：這是 **2016 年以 WHO 2007 組織學分類收的病人**（診斷名稱含「oligoastrocytoma」，
  一個 CNS5 已經不用的名字[S1]），**不是依 2021 年分子分類收的**。分子亞群的效益要靠事後分析。

**C. EORTC 22033-26033（Baumert 2016, Lancet Oncol）——單獨放療 vs 單獨 TMZ**[S25]

- 設計：隨機、開放標籤、第三期，19 國 78 個中心；**高風險 grade 2 膠質瘤**
  （高風險定義：>40 歲、疾病進展、腫瘤 >5 cm、腫瘤跨中線、或有神經症狀，任一）
- 隨機 **477 人**：適形放療（最高 50.4 Gy／28 次）**240 人** vs 高密度口服 TMZ（75 mg/m² 連續 21 天，
  每 28 天一循環，最多 12 循環）**237 人**
- 中位追蹤 48 個月（IQR 31–56）
- **主要終點（PFS）沒有差別**：TMZ 39 個月（95% CI 35–44）vs 放療 46 個月（40–56），
  **未校正 HR 1.16（95% CI 0.9–1.5），p=0.22**；分析時中位 OS 尚未達到
- **分子亞群的探索性分析（318 位分子已定義者）**：三個亞群預後顯著不同（p=0.013）；
  **IDHmt／非共缺失（＝IDH-mutant 星細胞瘤）者，放療的 PFS 優於 TMZ：HR 1.86（95% CI 1.21–2.87），
  log-rank p=0.0043**；IDHmt/codel（寡樹突）與 IDHwt 兩群看不出治療差異
- 毒性：TMZ 組 grade 3–4 血液毒性 **32/236（14%）** vs 放療 **1/228（<1%）**；
  grade 3–4 感染 8/236（3%）vs 2/228（1%）；中重度疲倦 放療 8 人（3%）vs TMZ 16 人（7%）
- **這是探索性分析**（原文用 exploratory），不可寫成確證[S25]

**D. CATNON（EORTC 26053-22054，van den Bent 2021, Lancet Oncol）——IDH-mutant 亞群的 TMZ 效益**[S26]

- 設計：隨機（1:1:1:1）、開放標籤、第三期；澳／歐／北美 137 個機構；**新診斷 1p/19q 非共缺失的
  間變性膠質瘤**（依當時的組織學分類）
- 四臂：單純放療（59.4 Gy／33 次）／放療＋同步 TMZ（75 mg/m²/日）／放療＋輔助 TMZ（12 個 4 週循環，
  150–200 mg/m² 第 1–5 天）／同步＋輔助都給
- 2007-12-04 至 2015-09-11 隨機 **751 人**（189／188／186／188）；中位追蹤 **55.7 個月**（IQR 41.0–77.3）
- **總體結果**：
  - **同步 TMZ 無效（宣告 futility）**：中位 OS 66.9 個月（95% CI 45.7–82.3）vs 60.4 個月（45.7–71.5），
    **HR 0.97（99.1% CI 0.73–1.28），p=0.76**
  - **輔助 TMZ 有效**：中位 OS **82.3 個月（95% CI 67.2–116.6）vs 46.9 個月（37.9–56.9）**，
    **HR 0.64（95% CI 0.52–0.79），p<0.0001**
- **IDH 分層（這是 SPEC 要的那一段，數字全部來自全文）**：
  - 660 個間變性星細胞瘤有 IDH 狀態：**216（33%）IDH-wildtype、444（67%）IDH-mutant**
  - 分析時仍存活：IDH-wildtype **32/216（15%）**；IDH-mutant **292/444（66%）**
  - **中位 OS：IDH-wildtype 19.9 個月（95% CI 16.8–22.7）vs IDH-mutant 98.4 個月（85.2–116.6）；
    HR 0.14（95% CI 0.12–0.18），p<0.0001**
  - **IDH-wildtype 組：同步或輔助 TMZ 都沒有改善存活**
  - **IDH-mutant 組：輔助 TMZ 改善存活，同步 TMZ 沒有**
  - **交互作用檢定：IDH 狀態對「輔助 TMZ 的效益」高度顯著（p=0.001），對「同步 TMZ」不顯著（p=0.29）**
  - IDH-mutant 且已用輔助 TMZ 者，再加同步 TMZ 沒有改善（HR 0.82，95% CI 0.49–1.36，p=0.44）；
    5 年存活 80.5%（71.3–87.0）vs 82.8%（73.7–89.0）
  - IDH-mutant 且已用同步 TMZ 者，加上輔助 TMZ 有改善（HR 0.49，95% CI 0.30–0.81，p=0.0050）；
    5 年存活 64.8%（54.3–73.5）vs 82.8%（73.7–89.0）
  - IDH-mutant 全體：初始治療含任何 TMZ 者（n=337）中位 OS **114.4 個月**（95% CI 90.3–未達）vs
    單純放療者（n=107）**68.2 個月**（55.7–91.8），**HR 0.53（95% CI 0.38–0.74），p<0.0001**；
    中位 PFS **77.0 個月**（60.3–86.7）vs **34.2 個月**（19.9–42.8），**HR 0.48（95% CI 0.37–0.63），p<0.0001**
- **毒性**：grade 3–4 以血液毒性為主——單純放療組 0 人；同步 TMZ 組 16/185（9%）；
  兩個含輔助 TMZ 的組別合計 55/368（15%）；**無治療相關死亡**[S26]
- **限制**：IDH 分層分析是**依規約修訂加入的**（2011 年 protocol version 8）且屬探索性／預後-預測性分析[S26]；
  這是**第二次期中分析**[S26]

**E. vorasidenib：INDIGO（Mellinghoff 2023, NEJM）**[S23]

*收案條件（逐條，SPEC 要求「精確」——這是紅線 3 的核心）*
- 年齡 **≥12 歲**
- **殘餘或復發的、組織學確認的 grade 2 寡樹突膠質瘤或星細胞瘤**（依 WHO 2016 判準），
  **IDH1／IDH2 突變狀態經中央確認**
- **KPS ≥ 80**
- **至少一次先前手術，且最近一次手術在隨機分派前 1 到 5 年之間**
- **除手術外未接受任何其他抗癌治療**
- **不需因腫瘤徵象／症狀使用類固醇**
- **依主治醫師判斷不需要立即化療或放療**
- 肝腎功能足夠
- **必須有可測量的非增強病灶**（至少一個目標病灶 ≥1 cm × ≥1 cm），經中央盲讀確認；
  影像至少須含 2D T1 顯影前後、2D T2、FLAIR
- 排除條件包含：可測量或結節狀顯影、癲癇未控制、腦幹侵犯[S7]

*設計與族群*
- 雙盲、隨機、安慰劑對照、第三期（NCT04164901）；vorasidenib 40 mg 口服每日一次 vs 相配安慰劑，28 天為一循環
- 2020-01 至 2022-02，**10 國 77 個中心收 331 人**（北美 58.3%、西歐 29.3%、以色列 12.4%）；
  vorasidenib 168／安慰劑 163
- 組織亞型分布：寡樹突／星細胞 約 52.4%／47.6%（vorasidenib 組）與 51.5%／48.5%（安慰劑組）
- 距上次手術的中位時間 2.5 年（範圍 0.2–5.2）與 2.2 年（0.9–5.0）
- 全部病人都開過刀，**21.5% 開過兩次以上**
- 安慰劑組在盲讀確認影像惡化後**可以交叉**到 vorasidenib

*結果*
- 中位追蹤 **14.2 個月**時，226 人（68.3%）仍在服藥
- **主要終點（影像判定的無惡化存活，由獨立審查委員會盲讀）：中位 27.7 個月（95% CI 17.0–未達）
  vs 11.1 個月（95% CI 11.0–13.7）；HR 0.39（95% CI 0.27–0.56），P<0.001**
- **關鍵次要終點（到下一次抗癌介入的時間）：HR 0.26（95% CI 0.15–0.43），P<0.001**
- **安全性**：grade ≥3 不良事件 **22.8% vs 13.5%**；
  grade ≥3 的 ALT 上升 **9.6%（另一處報 10%）vs 0%**（最常見的 grade ≥3 事件）；
  因治療相關不良事件停藥 **6 人（3.6%）vs 2 人（1.2%）**
- 檢定力設定：約 340 人、164 個 PFS 事件，可在單尾 α=0.025 下以 ≥90% 檢定力偵測 HR 0.6[S23]

*限制（必寫，全部有原文）*
1. **沒有整體存活結果。**「Follow-up for overall survival remains ongoing.」[S23]
2. **沒有生活品質、認知、癲癇的結果。**「Additional endpoints, including the impact of treatment on seizures,
   health-related quality of life and neurocognition, are planned to be reported at a later time.」[S23]
3. **次族群分析沒有預設統計檢定**：「no formal statistical testing was planned for subgroup analyses」；
   且「In some subgroups, such as those with tumors <2 cm, results should be interpreted with caution due to the
   small number of events.」[S23]
4. **追蹤很短**（中位 14.2 個月），對一個中位存活以「年」計的病要小心[S23]
5. **對照組是安慰劑，不是放化療。** 它證明的是「在觀察等待期間吃這個藥，比什麼都不吃能拖比較久」，
   **不是「它比放療加化療好」**——INDIGO 全文的定位就是「watch-and-wait 期間的機會」[S23]
6. **主要終點是影像上的無惡化**（imaging-based PFS），不是症狀或功能[S23]
7. **收案是 WHO 2016 判準的 grade 2**[S23]
8. **沒有任何隨機資料支持用在已接受過放療／化療的人**[S7]

**F. 監管身分（兩個地區寫法不一樣，這是 A5 的高潮）**

- **美國 FDA：2024 年 8 月 6 日核准**（vorasidenib，商品名 VORANIGO）。
  適應症原文：「**Grade 2 astrocytoma or oligodendroglioma with a susceptible IDH1 or IDH2 mutation,
  following surgery**」。核准依據為 INDIGO（NCT04164901，331 人）[S28]。
  ASCO-SNO 補充：核准涵蓋「following surgery **including biopsy, subtotal resection, or gross total
  resection**」[S7]。
- **歐盟 EMA／執委會：2025 年 9 月 17 日取得歐盟藥證**，具**孤兒藥（orphan）**資格。
  適應症原文：「**Voranigo as monotherapy is indicated for the treatment of predominantly non-enhancing Grade 2
  astrocytoma or oligodendroglioma with an IDH1 R132 or IDH2 R172 mutation in adult and adolescent patients aged
  12 years and older and weighing at least 40 kg who only had surgical intervention and are not in immediate need
  of radiotherapy or chemotherapy**」[S29]。
- **落差本身就是內容**：EMA 把 INDIGO 的三個族群條件（以非增強為主、只做過手術、不需立即放化療）寫進了
  適應症；**FDA 沒有**。ASCO-SNO 2025 逐條指出 FDA 仿單比試驗寬的四個地方（可測量病灶／1–5 年時間窗／
  未接受非手術治療／排除條件），並明說「**The panel cannot make a recommendation about vorasidenib in those
  patients**（指接受過放療或化療者）」[S7]。

**G. 指引怎麼說（ASCO-SNO 2025 快速建議更新，逐字）**[S7]

- **新增 Recommendation 1.2.1（寡樹突膠質瘤 grade 2）** 與 **1.5.1（星細胞瘤 grade 2）**：
  「**Vorasidenib may be offered** to people with [該亞型], IDH-mutant, ... CNS WHO grade 2, **where, after one or
  more surgeries, further treatment with radiation and chemotherapy has been or can be deferred**
  (**Evidence quality: High; Strength of recommendation: Conditional**).」
- **更新後的 1.2／1.5**（延後放化療的條件）：「initial radiation therapy and chemotherapy ... **may be deferred
  until radiographic or symptomatic progression in some people with favorable prognostic factors (eg, complete
  resection and younger age) or concerns about toxicity**（Evidence quality: Low; Strength: Conditional）」
- **實務條件**：「**Regular monitoring for liver function is necessary every 2 weeks in the first 2 months of
  treatment and monthly thereafter.**」；「**People who are seeking pregnancy as either father or mother and people
  who are pregnant or breast feeding should not be offered vorasidenib.**」
- **關於沒有可測量腫瘤的人**：「Patients without measurable tumor and their clinicians should **carefully weigh the
  potential but uncertain benefits** of beginning vorasidenib immediately versus continued observation until there
  is documented measurable tumor to allow for monitoring for response.」
- **關於 1–5 年時間窗**：「**The panel believes this time window is arbitrary**, and that it is reasonable to
  discuss vorasidenib at any time point after postoperative recovery.」
- **年齡範圍**：「the FDA approval and the INDIGO trial itself included patients as young as age 12 years;
  the ASCO-SNO guideline and this update **only address adult patients**.」

**H. 什麼時候該開始放療（觀察 vs 早期治療的證據）**

- **EORTC 22845（van den Bent 2005, Lancet）** ——這是「等一等」這件事的原始隨機證據[S27]：
  - 24 個歐洲中心；低惡性度星細胞瘤、寡樹突膠質瘤、混合型寡星細胞瘤、切除不完全的毛細胞星細胞瘤，
    WHO 體能狀態 0–2；**早期放療 54 Gy／1.8 Gy 分次（157 人）vs 惡化時才放療（157 人）**
  - **中位無惡化存活 5.3 年 vs 3.4 年（HR 0.59，95% CI 0.45–0.77，p<0.0001）**
  - **中位整體存活 7.4 年 vs 7.2 年（HR 0.97，95% CI 0.71–1.34，p=0.872）——沒有差別**
  - **對照組有 65% 在惡化時接受了放療**
  - **一年時，早期放療組的癲癇控制較好**
  - 作者結論原文：「Early radiotherapy after surgery lengthens the period without progression but does not affect
    overall survival. **Because quality of life was not studied, it is not known whether time to progression
    reflects clinical deterioration.** Radiotherapy **could be deferred for patients with low-grade glioma who are
    in a good condition, provided they are carefully monitored.**」[S27]
  - **時代標籤**：1986 年啟動的試驗，**沒有分子分型**[S27]
- **現行指引的立場**：延後初始放化療是 Conditional 建議、證據品質 Low，適用對象是「**有利預後因子
  （如完全切除、較年輕）或擔心毒性**」的人[S7]。
- **為什麼會想延後（INDIGO 的背景段，可引）**：「While adjuvant chemoradiation can result in long-lasting disease
  remissions, treatment is not curative and is associated with **radiation-induced neurocognitive dysfunction,
  chemotherapy-associated DNA hypermutation, and other toxicities**. To delay these potential long-term
  toxicities, many patients with IDH-mutant grade 2 gliomas do not receive immediate adjuvant chemoradiation
  following their initial diagnosis, and are instead **monitored with serial brain MRI scans**.」[S23]
- **風險分層的誠實話（ASCO-SNO 引 INDIGO 全文的觀察）**：「Current treatment recommendations for IDH-mutant
  glioma define "risk" based on age, extent of resection, and grade of disease; however, **limited data justify
  categorizing risk based on these factors alone.**」[S23]

### 反方向的資料（誠實必列）

1. **「低惡性度」不等於良性**：INDIGO 原文兩處明講會造成失能與早逝、會持續生長、最終轉為侵襲性[S23]。
2. **早期放療不延長存活**（EORTC 22845，HR 0.97，p=0.872）[S27]——但那是 1986 年的試驗、沒有分子分型、
   而且對照組六成五後來也放了療；**不可寫成「放療沒用」**。RTOG 9802 的放療＋PCV 對 OS 有效（HR 0.59）[S24]。
3. **TMZ 不能拿來當放療的替代品**：EORTC 22033 的主要終點沒差，而 IDH-mutant 非共缺失的探索性分析裡
   **放療的 PFS 反而優於 TMZ（HR 1.86）**[S25]。
4. **CATNON 的「同步 TMZ 無效」是 futility 宣告**[S26]——一個試驗做完之後把自己的一隻手臂否定掉，
   這件事本身值得寫給讀者看（「我們也會證明自己想的是錯的」）。
5. **vorasidenib 沒有存活資料、沒有生活品質資料、追蹤只有 14.2 個月中位**[S23]。
6. **vorasidenib 有肝毒性**：grade ≥3 ALT 上升 9.6%，且需要頭兩個月每兩週、之後每月抽血監測肝功能[S23][S7]。
7. **建議強度是 Conditional，不是 Strong**[S7]。
8. **RTOG 9802 與 EORTC 22845 收的是舊分類的病人**（含 oligoastrocytoma 這個已廢除的名稱[S1]）——
   把它們的數字直接套到 2021 年分子分類下的病人，是外推。

### Claim ceiling（A5）

**可寫**
- 「IDH-mutant 有兩種：有 1p/19q 共缺失的是寡樹突膠質瘤，沒有的是星細胞瘤。**這是兩種病，治療建議不一樣**」[S23][S7]
- 「低惡性度不等於良性：它會持續長、會浸潤、最後會變成侵襲性的腫瘤」[S23]
- 「RTOG 9802：放療後加 6 個療程 PCV，中位存活 13.3 年 vs 單獨放療 7.8 年（HR 0.59，P=0.003）；
  10 年存活 60% vs 40%——**中位追蹤 11.9 年，但收的是 2007 年組織學分類的病人**」[S24]
- 「EORTC 22033：單獨 TMZ 沒有比單獨放療好（PFS 39 vs 46 個月，HR 1.16，p=0.22）；
  在 IDH-mutant、非共缺失那一群的**探索性**分析裡，放療的 PFS 反而優於 TMZ（HR 1.86）」[S25]
- 「CATNON：IDH-mutant 的人，**輔助** TMZ 有效（HR 0.53，PFS 77.0 vs 34.2 個月），**同步** TMZ 沒有；
  IDH-wildtype 的人，兩種都沒有。IDH 狀態對輔助 TMZ 效益的交互作用 p=0.001」[S26]
- 「CATNON 裡，IDH-wildtype 的中位存活 19.9 個月，IDH-mutant 98.4 個月——**同一個組織學名稱、兩個世界**」[S26]
  （**若使用這組絕對數字，同段必須一句指向 B4 的讀法**）
- 「vorasidenib 的 INDIGO 試驗收的是：grade 2、IDH-mutant、KPS ≥80、**只開過刀沒做過別的治療**、
  **最近一次手術在 1 到 5 年前**、**有可測量的非增強病灶**、**不需要類固醇**、**醫師判斷不需要立即放化療**」[S23]
- 「結果：影像判定的無惡化存活中位 27.7 vs 11.1 個月（HR 0.39）；到下一次治療介入的時間 HR 0.26」[S23]
- 「限制：**沒有存活結果、沒有生活品質與認知結果、追蹤中位只有 14.2 個月、對照組是安慰劑不是放化療、
  次族群分析沒有預設檢定**」[S23]
- 「grade ≥3 不良事件 22.8% vs 13.5%；最常見的是肝指數上升（9.6% vs 0%）；頭兩個月要每兩週抽血」[S23][S7]
- 「FDA 2024 年 8 月 6 日核准；EMA／歐盟執委會 2025 年 9 月 17 日核准。**兩邊的適應症寫法不一樣**——
  歐盟把『以非增強為主』『只做過手術』『不需要立即放化療』寫進了適應症，美國沒有」[S28][S29]
- 「ASCO-SNO 2025 把 vorasidenib 列為『**可以提供**』（may be offered），證據品質 High、
  **建議強度 Conditional**；並且明說對『已經接受過放療或化療的人，無法做出建議』」[S7]
- 「EORTC 22845：術後早期放療 vs 惡化才放療，無惡化存活 5.3 年 vs 3.4 年（HR 0.59），
  **但整體存活 7.4 年 vs 7.2 年，沒有差別**；對照組有 65% 後來也放了療；早期放療組一年時癲癇控制較好」[S27]
- 「現行指引：對有利預後因子（完全切除、較年輕）或擔心毒性的人，**初始放化療可以延後到影像或症狀惡化時**
  ——證據品質 Low、建議強度 Conditional」[S7]

**不可寫（硬上限，紅線 3）**
- ❌「低惡性度＝良性」「不用治療」「觀察就好」
- ❌ 把 IDH-mutant 星細胞瘤與寡樹突膠質瘤混為一談
- ❌「vorasidenib 延長存活」——**沒有 OS 資料**[S23]
- ❌「vorasidenib 可以取代放療／化療」——對照組是安慰劑[S23]
- ❌ 把 vorasidenib 寫給「已經做過放療或化療的人」——ASCO-SNO 明說無法建議[S7]
- ❌「台灣有／沒有 vorasidenib」「健保有／沒有給付」——**查不到，見台灣端與 FAIL-1／FAIL-2**。
  必須寫成「我查不到可以引用的官方資料」
- ❌ 任何 vorasidenib 的自費金額（費用紀律；媒體價格不可引）
- ❌ 把 RTOG 9802 的 13.3 年寫成「你可以活 13 年」——那是 2016 年公布、以舊分類收案的**中位數**，
  且該世代的入組條件是「<40 歲切不乾淨或 ≥40 歲」[S24]。使用時一句指向 B4
- ❌ 任何劑量與用法（40 mg／日 只能當「試驗用的劑量」寫在背景，不寫成用法用量）

### Caveats／safety notes（寫作者必寫）

- **紅線 3 的三句話**要在同一篇裡都出現：(1) 低惡性度不等於良性、不等於不用治療；(2) 星細胞瘤與寡樹突膠質瘤
  是兩種病、分開講；(3) vorasidenib 的適應族群要精確、台灣身分查不到就寫查不到。
- **「延後治療」不是「不治療」**：EORTC 22845 的作者原文加了條件——「**provided they are carefully
  monitored**」[S27]；而且該試驗沒有測生活品質，所以「無惡化期比較長」不等於「過得比較好」[S27]。
  這一點要寫進去，否則讀者會把「觀察」讀成「不用回診」。
- **肝功能監測不是選配**：頭兩個月每兩週、之後每月[S7]。以及備孕／懷孕／哺乳者不應使用[S7]。
- **這一篇的讀者很可能不是 GBM 病人**，而是拿到 IDH-mutant 報告、被推進這個專題的人。開頭要立刻讓他知道
  「**這個專題的主線不是你的病**」，並且說明為什麼還是寫了這一篇（因為報告出來之前，兩群人是同一群人）。
- **不可出現「治癒」兩個字**（SPEC 紅線 1 的用詞紀律，全專題適用）。
- 認知副作用與長期毒性的完整討論歸 D2；本篇只在解釋「為什麼有人想延後放療」時一句帶過[S23]。

### 台灣端（A5）

**全部 gap，且必須寫成「查不到」而不是「沒有」。**

| 項目 | 結果 | 查證路徑 |
|---|---|---|
| vorasidenib 的台灣藥證 | **gap** | 食藥署西藥許可證查詢 info.fda.gov.tw：DNS 無法解析；data.fda.gov.tw 開放資料 API `exportDataList.do` 已改版並 301 導向 `data.fda.gov.tw/`，swagger 頁無可用端點說明。2026-09-03 兩路均失敗（FAIL-1） |
| vorasidenib 的健保給付 | **gap** | 現行「藥品給付規定」第 9 節抗癌瘤藥物全文取不到；data.nhi.gov.tw 回 CONNECT 502。已取得 113/10、114/1、114/2、114/6、114/7、114/8 生效的六份「修訂對照表」PDF 並全文搜尋，**查無 vorasidenib**——但修訂對照表只列該次異動條文，**查無不等於沒有給付**（FAIL-2） |
| 5-ALA 的台灣藥證與給付 | **gap** | 同上（FAIL-1／FAIL-2／FAIL-3） |
| 台灣 IDH-mutant 膠質瘤的登記數字 | **gap** | hpa.gov.tw 與 cris.hpa.gov.tw TLS 憑證驗證失敗；衛福部 111 年癌症登記新聞稿無腦瘤數字（FAIL-4） |

**已查到可用的台灣端唯一一項**：重大傷病（見 A2）——IDH-mutant 膠質瘤只要 ICD-10-CM 落在 C71，
同樣走第一大項第（五）小項，**證明有效期限五年**[S30]。

**正文建議寫法**（照紅線 3）：
> 「vorasidenib 在美國 2024 年 8 月核准、歐盟 2025 年 9 月核准。**它在台灣有沒有藥證、健保給不給付，
> 我這次查不到可以引用的官方資料**——不是『沒有』，是我查不到。請直接問你的神經腫瘤科醫師，
> 或請個管師幫你問醫院醫務課。」

### 給繪圖組的數字（A5）

SPEC §七 未指定 A5 圖。若補一張「兩條路」的對照圖，PASS 數字：
- 分岔：IDH-mutant → 1p/19q 共缺失？→ 是＝寡樹突膠質瘤／否＝星細胞瘤[S23]
- 寡樹突 grade 2 建議：RT ＋ PCV（Strong）；TMZ 為毒性考量時的替代（Conditional）[S7]
- 星細胞瘤 grade 2 建議：RT ＋ 輔助化療（TMZ 或 PCV）（Strong）[S7]
- RTOG 9802 條：13.3 年 vs 7.8 年（HR 0.59）；10 年 OS 60% vs 40%[S24]
- CATNON 條（IDH-mutant）：任何 TMZ vs 單純放療，中位 OS 114.4 vs 68.2 個月（HR 0.53）；
  PFS 77.0 vs 34.2 個月（HR 0.48）[S26]
- EORTC 22845 條：PFS 5.3 vs 3.4 年（HR 0.59）；**OS 7.4 vs 7.2 年（HR 0.97，無差別）**[S27]
- INDIGO 條：PFS 27.7 vs 11.1 個月（HR 0.39）；到下一次介入 HR 0.26；grade ≥3 AE 22.8% vs 13.5%[S23]
- **圖上必須有三行註記**：(1) RTOG 9802／EORTC 22845 收的是舊分類病人；(2) INDIGO 沒有存活資料；
  (3) 台灣藥證與給付狀態查不到

---

# 來源清單

## PASS（可引用）

> 全部經 Europe PMC REST `search?query=...&resultType=core&format=json` 核對書目（2026-09-03）。
> 標「**全文**」者已抓下全文逐字核對；未標者**只有摘要層級可引**，本 brief 中該來源的每個數字都在摘要內。
> PMC HTML 抓取會間歇回 reCAPTCHA（約 20 KB 的挑戰頁），每次抓取都以下載大小驗證（>90 KB 才視為成功）、必要時重試 2–3 次。

**[S1] Louis DN, Perry A, Wesseling P, et al.** The 2021 WHO Classification of Tumors of the Central Nervous
System: a summary. *Neuro-Oncology.* 2021;23(8):1231–1251. DOI 10.1093/neuonc/noab106. PMID 34185076.
PMCID PMC8328013. isOpenAccess: N。
**Route**：Europe PMC `TITLE:"The 2021 WHO Classification of Tumors of the Central Nervous System: a summary"`
＋ **全文** `https://pmc.ncbi.nlm.nih.gov/articles/PMC8328013/`（278,160 bytes；第 3 次嘗試成功）。
本 brief 所有 CNS5 引語逐字取自該全文。

**[S2] Brat DJ, Aldape K, Colman H, et al.** cIMPACT-NOW update 3: recommended diagnostic criteria for "Diffuse
astrocytic glioma, IDH-wildtype, with molecular features of glioblastoma, WHO grade IV". *Acta Neuropathologica.*
2018;136(5):805–810. DOI 10.1007/s00401-018-1913-0. PMID 30259105. PMCID PMC6204285. isOpenAccess: N。
**Route**：Europe PMC `EXT_ID:30259105` ＋ **全文** `https://pmc.ncbi.nlm.nih.gov/articles/PMC6204285/`
（166,670 bytes，作者手稿版）。三選一原文、「lack of IDH mutation alone is insufficient」、EGFR 技術限制
均逐字取自該全文。

**[S3] Price M, Ballard CAP, Benedetti JR, Kruchko C, Barnholtz-Sloan JS, Ostrom QT.** CBTRUS Statistical Report:
Primary Brain and Other Central Nervous System Tumors Diagnosed in the United States in **2018-2022**.
*Neuro-Oncology.* 2025;27(Supplement_4):iv1–iv66. DOI 10.1093/neuonc/noaf194. PMID 41092086. isOpenAccess: N。
**Route**：Europe PMC `TITLE:"CBTRUS Statistical Report" AND PUB_YEAR:2025`。無 PMCID，僅摘要。

**[S4] Price M, Ballard C, Benedetti J, et al.** CBTRUS Statistical Report: Primary Brain and Other Central
Nervous System Tumors Diagnosed in the United States in **2017-2021**. *Neuro-Oncology.*
2024;26(Supplement_6):vi1–vi85. DOI 10.1093/neuonc/noae145. PMID 39371035. PMCID PMC11456825. isOpenAccess: N。
**Route**：Europe PMC ＋ **全文** `https://pmc.ncbi.nlm.nih.gov/articles/PMC11456825/`（1,023,221 bytes）。
GBM 發生率 3.27（男 4.07／女 2.58）、中位年齡 66、70–74 歲最高、佔膠質瘤 61.0%、IDH 編碼分布
（2.4%／80.4%／14.6%）、「registries... do not collect data on tumors that metastasize to the brain」
均逐字取自全文。

**[S5] Weller M, van den Bent M, Preusser M, et al.** EANO guidelines on the diagnosis and treatment of diffuse
gliomas of adulthood. *Nature Reviews Clinical Oncology.* 2021;18(3):170–186. DOI 10.1038/s41571-020-00447-z.
PMID 33293629. PMCID PMC7904519. **isOpenAccess: Y**。
（Author Correction：*Nat Rev Clin Oncol.* 2022;19(5):357–358. DOI 10.1038/s41571-022-00623-3. PMID 35322237.）
**Route**：Europe PMC ＋ **全文** `.../rest/PMC7904519/fullTextXML`（228,623 bytes）。本 brief 所有 EANO 引語
逐字取自該 XML。

**[S6] Mohile NA, Messersmith H, Gatson NT, et al.** Therapy for Diffuse Astrocytic and Oligodendroglial Tumors in
Adults: ASCO-SNO Guideline. *Journal of Clinical Oncology.* 2022;40(4):403–426. DOI 10.1200/JCO.21.02036.
PMID 34898238. isOpenAccess: N。**Route**：Europe PMC 標題查詢。無 PMCID，僅摘要。

**[S7] Blakeley J, Mohile NA, Messersmith H, Lassman AB, Schiff D, et al.** Therapy for Diffuse Astrocytic and
Oligodendroglial Tumors in Adults: ASCO-SNO Guideline **Rapid Recommendation Update**. *Neuro-Oncology.*
2025;27(6):1412–1418. DOI 10.1093/neuonc/noaf072. PMID 40304440. PMCID PMC12309703.
（同步：*J Clin Oncol.* 2025;43(18):2129–2133. DOI 10.1200/JCO-25-00250. PMID 40300117；Clinical Insights：
*JCO Oncol Pract.* 2026;22(1):16–18. DOI 10.1200/OP-25-00185. PMID 40300119。）isOpenAccess: N。
**Route**：Europe PMC ＋ **全文** `https://pmc.ncbi.nlm.nih.gov/articles/PMC12309703/`（138,549 bytes）。
Rec 1.2.1／1.5.1 原文、Evidence quality High／Strength Conditional、FDA 仿單與試驗的四處落差、
肝功能監測頻率均逐字取自全文。

**[S9] Avila EK, Tobochnik S, Inati SK, et al.** Brain tumor-related epilepsy management: A Society for
Neuro-oncology (SNO) consensus review on current management. *Neuro-Oncology.* 2024;26(1):7–24.
DOI 10.1093/neuonc/noad154. PMID 37699031. PMCID PMC10768995. isOpenAccess: N。
**Route**：Europe PMC `EXT_ID:37699031`。僅摘要。

**[S10] Karschnia P, Vogelbaum MA, van den Bent M, et al.** Evidence-based recommendations on categories for
extent of resection in diffuse glioma. *European Journal of Cancer.* 2021;149:23–33.
DOI 10.1016/j.ejca.2021.03.002. PMID 33819718. isOpenAccess: N。**Route**：Europe PMC 標題查詢。無 PMCID，
僅摘要（六級名稱、「class of evidence ranges from class IIB to IV」）；各級體積門檻由 [S11] 全文的 Methods 段
逐字複述取得。

**[S11] Karschnia P, Young JS, Dono A, et al.** Prognostic validation of a new classification system for extent of
resection in glioblastoma: A report of the RANO resect group. *Neuro-Oncology.* 2023;25(5):940–954.
DOI 10.1093/neuonc/noac193. PMID 35961053. PMCID PMC10158281. **isOpenAccess: Y**（CC BY-NC）。
**Route**：Europe PMC ＋ **全文** `.../rest/PMC10158281/fullTextXML`（127,415 bytes）。四級定義、supramaximal
門檻、中位 PFS/OS、各級 HR、多變項結果、15.8% 新發神經缺損均逐字取自全文。

**[S12] Molinaro AM, Hervey-Jumper S, Morshed RA, et al.** Association of Maximal Extent of Resection of
Contrast-Enhanced and Non-Contrast-Enhanced Tumor With Survival Within Molecular Subgroups of Patients With
Newly Diagnosed Glioblastoma. *JAMA Oncology.* 2020;6(4):495–503. DOI 10.1001/jamaoncol.2019.6143. PMID 32027343.
PMCID PMC7042822. isOpenAccess: N。**Route**：Europe PMC 標題查詢。僅摘要。

**[S13] Brown TJ, Brennan MC, Li M, et al.** Association of the Extent of Resection With Survival in Glioblastoma:
A Systematic Review and Meta-analysis. *JAMA Oncology.* 2016;2(11):1460–1469. DOI 10.1001/jamaoncol.2016.1373.
PMID 27310651. PMCID PMC6438173. isOpenAccess: N。**Route**：Europe PMC 標題查詢。僅摘要（含所有 RR、NNT
與 GRADE 自評）。

**[S14] Stummer W, Pichlmeier U, Meinel T, Wiestler OD, Zanella F, Reulen HJ; ALA-Glioma Study Group.**
Fluorescence-guided surgery with 5-aminolevulinic acid for resection of malignant glioma: a randomised controlled
multicentre phase III trial. *The Lancet Oncology.* 2006;7(5):392–401. DOI 10.1016/S1470-2045(06)70665-9.
PMID 16648043. isOpenAccess: N。NCT00241670。**Route**：Europe PMC 標題查詢。僅摘要（含兩個主要終點定義、
65% vs 36%、41.0% vs 21.1%、期中終止、安全性）。

**[S15] De Witt Hamer PC, Robles SG, Zwinderman AH, Duffau H, Berger MS.** Impact of intraoperative stimulation
brain mapping on glioma surgery outcome: a meta-analysis. *Journal of Clinical Oncology.* 2012;30(20):2559–2565.
DOI 10.1200/JCO.2011.38.4818. PMID 22529254. isOpenAccess: N。**Route**：Europe PMC 標題查詢。僅摘要。

**[S16] Gerritsen JKW, Zwarthoed RH, Kilgallon JL, et al.** Effect of awake craniotomy in glioblastoma in eloquent
areas (GLIOMAP): a propensity score-matched analysis of an international, multicentre, cohort study.
*The Lancet Oncology.* 2022;23(6):802–817. DOI 10.1016/S1470-2045(22)00213-3. PMID 35569489. isOpenAccess: N。
**Route**：Europe PMC `EXT_ID:35569489`。僅摘要。

**[S17] Karschnia P, Young JS, Youssef GC, et al.** Development and validation of a clinical risk model for
postoperative outcome in newly diagnosed glioblastoma: A report of the RANO resect group. *Neuro-Oncology.*
2025;27(4):1046–1060. DOI 10.1093/neuonc/noae231. PMID 39492786. PMCID PMC12083231. **isOpenAccess: Y**。
**Route**：Europe PMC ＋ **全文** `.../rest/PMC12083231/fullTextXML`（138,836 bytes）。15.6% 新發缺損逐字取自
全文；四因子 0–9 分風險模型與外部驗證 n=258 出自摘要。

**[S18] Teske N, Dono A, Young JS, et al.** Associations of supramaximal resection with outcome in glioblastoma
across age groups: A report of the RANO resect group. *Neuro-Oncology.* 2026;28(2):470–484.
DOI 10.1093/neuonc/noaf239. PMID 41137668. isOpenAccess: N。**Route**：Europe PMC `EXT_ID:41137668`。僅摘要。

**[S19] Capper D, Jones DTW, Sill M, et al.** DNA methylation-based classification of central nervous system
tumours. *Nature.* 2018;555(7697):469–474. DOI 10.1038/nature26000. PMID 29539639. PMCID PMC6093218.
**isOpenAccess: Y**。**Route**：Europe PMC 標題查詢。僅摘要（含「change of diagnosis in up to 12% of
prospective cases」）。

**[S20] Mansouri A, Hachem LD, Mansouri S, et al.** MGMT promoter methylation status testing to guide therapy for
glioblastoma: refining the approach based on emerging evidence and current challenges. *Neuro-Oncology.*
2019;21(2):167–178. DOI 10.1093/neuonc/noy132. PMID 30189035. PMCID PMC6374759. isOpenAccess: N。
**Route**：Europe PMC ＋ **全文** `https://pmc.ncbi.nlm.nih.gov/articles/PMC6374759/`（238,560 bytes）。
777 bp／97 CpG、MSP 重複不一致 12%、qMSP 的 technical cutoff 與 gray zone、pyrosequencing 的 8%／25%、
partial methylation、各法「cutoff not validated in clinical trials」均逐字取自全文。

**[S21] Ball MK, Kollmeyer TM, Praska CE, et al.** Frequency of false-positive FISH 1p/19q codeletion in adult
diffuse astrocytic gliomas. *Neuro-Oncology Advances.* 2020;2(1):vdaa109. DOI 10.1093/noajnl/vdaa109.
PMID 33205043. PMCID PMC7654379. **isOpenAccess: Y**。**Route**：Europe PMC `EXT_ID:33205043`。僅摘要。

**[S22] de Biase D, Acquaviva G, Visani M, et al.** Next-Generation Sequencing Panel for 1p/19q Codeletion and
IDH1-IDH2 Mutational Analysis Uncovers Mistaken Overdiagnoses of 1p/19q Codeletion by FISH. *The Journal of
Molecular Diagnostics.* 2021;23(9):1185–1194. DOI 10.1016/j.jmoldx.2021.06.004. PMID 34186176. isOpenAccess: N。
**Route**：Europe PMC `EXT_ID:34186176`。僅摘要。

**[S23] Mellinghoff IK, van den Bent MJ, Blumenthal DT, et al.; INDIGO Trial Investigators.** Vorasidenib in
IDH1- or IDH2-Mutant Low-Grade Glioma. *The New England Journal of Medicine.* 2023;389(7):589–601.
DOI 10.1056/NEJMoa2304194. PMID 37272516. PMCID PMC11445763. isOpenAccess: N。NCT04164901。
**Route**：Europe PMC 標題查詢 ＋ **全文** `https://pmc.ncbi.nlm.nih.gov/articles/PMC11445763/`
（209,800 bytes；`fullTextXML` 端點回 404，改走 PMC HTML）。完整收案條件（KPS ≥80／1–5 年手術時間窗／
可測量非增強病灶／不需類固醇／不需立即放化療）、77 中心 10 國、21.5% 開過兩次以上、ALT 9.6%、
停藥 3.6% vs 1.2%、「Follow-up for overall survival remains ongoing」、「no formal statistical testing was
planned for subgroup analyses」均逐字取自全文。

**[S24] Buckner JC, Shaw EG, Pugh SL, et al.** Radiation plus Procarbazine, CCNU, and Vincristine in Low-Grade
Glioma. *The New England Journal of Medicine.* 2016;374(14):1344–1355. DOI 10.1056/NEJMoa1500925. PMID 27050206.
PMCID PMC5170873. isOpenAccess: N。NCT00003375（RTOG 9802）。**Route**：Europe PMC 標題查詢。僅摘要
（含收案條件、11.9 年追蹤、13.3 vs 7.8 年、HR 0.59、10 年 PFS/OS）。

**[S25] Baumert BG, Hegi ME, van den Bent MJ, et al.** Temozolomide chemotherapy versus radiotherapy in high-risk
low-grade glioma (EORTC 22033-26033): a randomised, open-label, phase 3 intergroup study. *The Lancet Oncology.*
2016;17(11):1521–1532. DOI 10.1016/S1470-2045(16)30313-8. PMID 27686946. PMCID PMC5124485. **isOpenAccess: Y**。
EudraCT 2004-002714-11；NCT00182819。**Route**：Europe PMC 標題查詢。僅摘要（含高風險定義、477 人、
39 vs 46 個月、HR 1.16、IDHmt/non-codel 的 HR 1.86、毒性）。

**[S26] van den Bent MJ, Tesileanu CMS, Wick W, et al.** Adjuvant and concurrent temozolomide for 1p/19q
non-co-deleted anaplastic glioma (CATNON; EORTC study 26053-22054): second interim analysis of a randomised,
open-label, phase 3 study. *The Lancet Oncology.* 2021;22(6):813–823. DOI 10.1016/S1470-2045(21)00090-5.
PMID 34000245. PMCID PMC8191233. isOpenAccess: N。NCT00626990。
**Route**：Europe PMC 標題查詢 ＋ **全文** `https://pmc.ncbi.nlm.nih.gov/articles/PMC8191233/`（229,537 bytes）。
IDH 分層全部數字、IDH1 各突變型比例、MS-PCR 與 MGMT-STP27 一致率 85%（κ 0.67）均逐字取自全文；
總體 futility 與輔助 TMZ 結果在摘要。

**[S27] van den Bent MJ, Afra D, de Witte O, et al.; EORTC Radiotherapy and Brain Tumor Groups and the UK MRC.**
Long-term efficacy of early versus delayed radiotherapy for low-grade astrocytoma and oligodendroglioma in
adults: the EORTC 22845 randomised trial. *The Lancet.* 2005;366(9490):985–990.
DOI 10.1016/S0140-6736(05)67070-5. PMID 16168780. isOpenAccess: N。**Route**：Europe PMC 標題查詢。僅摘要
（含 157/157、5.3 vs 3.4 年、7.4 vs 7.2 年、對照組 65% 後來接受放療、作者結論原文）。

**[S28] U.S. Food and Drug Administration.** FDA approves vorasidenib for Grade 2 astrocytoma or oligodendroglioma
with a susceptible IDH1 or IDH2 mutation. **核准日：2024-08-06。**
`https://www.fda.gov/drugs/resources-information-approved-drugs/fda-approves-vorasidenib-grade-2-astrocytoma-or-oligodendroglioma-susceptible-idh1-or-idh2-mutation`
**Route**：直接抓取 FDA 官方 landing page（2026-09-03）。適應症原文、核准日、依據試驗均取自該頁。

**[S29] European Medicines Agency.** Voranigo (vorasidenib) — EPAR / medicine overview。
**歐盟藥證日：2025-09-17**；孤兒藥資格：是。`https://www.ema.europa.eu/en/medicines/human/EPAR/voranigo`
**Route**：直接抓取 EMA 官方 landing page（2026-09-03）。適應症原文逐字取自該頁。

**[S30] 衛生福利部中央健康保險署.**《全民健康保險保險對象免自行負擔費用辦法》第二條附表一修正規定——
**附表一、全民健康保險重大傷病項目及其證明有效期限**（113 年 9 月 16 日發布修訂；**一百十四年一月一日
以後適用**；ICD-10-CM/PCS 碼 2023 年版）。PDF，13 頁。
`https://www.nhi.gov.tw/ch/dl-74911-9ea79f859a24431497ef0304ce4b7981-1.pdf`
（列於「全民健康保險重大傷病項目」頁 `https://www.nhi.gov.tw/ch/cp-6086-caf5f-2957-1.html`）
**Route**：直接下載 PDF（466,471 bytes，2026-09-03）＋ pdftotext -layout 轉文字逐字核對。

**[S31] ClinicalTrials.gov.** NCT03861299 — The SAFE-Trial: Awake Craniotomy Versus Surgery Under General
Anesthesia for Glioblastoma Patients。**Overall status: RECRUITING**（last update submitted **2023-11-18**）。
**Route**：`https://clinicaltrials.gov/api/v2/studies/NCT03861299`（2026-09-03）。
（計畫書：Gerritsen JKW, et al. *Contemp Clin Trials.* 2020. DOI 10.1016/j.cct.2019.105876. PMID 31676314。）

**[S32] Ontario Health (Quality).** DNA Methylation-Based Classification for Central Nervous System Tumours:
A Health Technology Assessment. *Ontario Health Technology Assessment Series.* 2025;25(5):1–93. PMID 41312229.
PMCID PMC12647934. isOpenAccess: N。**Route**：Europe PMC 標題查詢。僅摘要。
**加拿大安大略省資料，不可換算或外推至台灣。**

**[S33] Roder C, Stummer W, Coburger J, et al.** Intraoperative MRI-Guided Resection Is Not Superior to
5-Aminolevulinic Acid Guidance in Newly Diagnosed Glioblastoma: A Prospective Controlled Multicenter Clinical
Trial. *Journal of Clinical Oncology.* 2023;41(36):5512–5523. DOI 10.1200/JCO.22.01862. PMID 37335962.
PMCID PMC10730068. **isOpenAccess: Y**。**Route**：Europe PMC `EXT_ID:37335962`。僅摘要（含 314 人、
78% vs 81%、P=.79、316 vs 215 分鐘、殘餘 0 cm³ 的預後意義）。

**[S34] 全國法規資料庫（法務部）.**《全民健康保險保險對象免自行負擔費用辦法》。
`https://law.moj.gov.tw/LawClass/LawAll.aspx?PCode=L0060015`
**Route**：直接抓取（2026-09-03）。第二條、第八條為原文。

## FAIL / NOT-CITABLE（保留，供作者知道查過什麼）

**[S8] Glantz MJ, Cole BF, Forsyth PA, et al.** Practice parameter: anticonvulsant prophylaxis in patients with
newly diagnosed brain tumors **[RETIRED]**. Report of the Quality Standards Subcommittee of the American Academy
of Neurology. *Neurology.* 2000;54(10):1886–1893. DOI 10.1212/WNL.54.10.1886. PMID 10822423.
**FAIL 理由**：Europe PMC／PubMed 的標題已標記 `[RETIRED]`（AAN 已撤回）。
**不可作為現行指引引用。** SPEC §五 A2 指名要引「AAN 的原文」——**這一條要改用 EANO 2021[S5] 與 SNO 2024[S9]**。
**Route**：Europe PMC REST `query=TITLE:"Practice parameter: anticonvulsant prophylaxis in patients with newly
diagnosed brain tumors"`（2026-09-03）。

**FAIL-1｜台灣食藥署西藥許可證（vorasidenib、5-ALA）**
- `https://info.fda.gov.tw/MLMS/H0001.aspx` → DNS 無法解析（Name or service not known）
- `https://data.fda.gov.tw/opendata/exportDataList.do?method=openData&InfoId=36[&logType=1|2]` → HTTP 301
  導向 `http://data.fda.gov.tw/`；跟隨後落到 swagger-ui 首頁，無可用端點文件
- `https://data.fda.gov.tw/api/v1/openData?infoId=36`、`https://data.fda.gov.tw/cacheData/{175_1,175_2,36_1,36_2}.json`
  → 404
- `https://data.gov.tw/dataset/13030` → WebFetch ROBOTS_DISALLOWED（robots.txt 取得失敗 HTTP 500）
→ **vorasidenib 與 5-ALA 的台灣藥證狀態：gap。永不推論。**

**FAIL-2｜健保「藥品給付規定」第 9 節抗癌瘤藥物（現行全文）**
- `https://data.nhi.gov.tw/...` → curl CONNECT tunnel failed, response 502（兩個端點皆是）
- `https://www.nhi.gov.tw/ch/cp-6086-caf5f-2957-1.html` 以 curl 直取 → HTTP 403（Cloudflare）；
  改用 WebFetch 可讀（本 brief 的 [S30] PDF 連結即由此取得）
- 已成功下載並全文搜尋的六份「修訂對照表」PDF（皆為 nhi.gov.tw/ch/dl-… 直連）：
  114/8/1 生效（dl-87133）、114/7/1（dl-85832）、114/6/1（dl-84779）、114/2/1（dl-81550）、
  114/1/1（dl-78965）、113/10/1（dl-74452）。**六份中 vorasidenib、temozolomide、「膠質」皆 0 筆。**
  **但修訂對照表只列該次異動條文，查無 ≠ 沒有給付。**
→ **vorasidenib（與 temozolomide、5-ALA）的健保給付狀態：gap。永不推論。**
（temozolomide 與 bevacizumab 的給付條文屬 B 組／D 組的查證範圍，本 brief 不代查。）

**FAIL-3｜5-ALA（Gliolan）的台灣藥證與給付**：同 FAIL-1／FAIL-2。
另以 WebSearch 檢索繁體中文官方來源，僅得義大利 AIFA、英國 NHS、荷蘭 CBG-MEB 等外國文件與中國大陸網站，
**無台灣官方頁面**。→ gap。

**FAIL-4｜台灣癌症登記的腦瘤發生數與 GBM 比例**
- `https://www.hpa.gov.tw/Pages/List.aspx?nodeid=269`（歷年癌症登記報告）→ curl 以 `/root/.ccr/ca-bundle.crt`
  仍 TLS 失敗，HTTP 000
- `https://cris.hpa.gov.tw/`（癌症登記線上互動查詢系統）→ WebFetch ROBOTS_DISALLOWED
  （SSL: CERTIFICATE_VERIFY_FAILED）
- `https://www.mohw.gov.tw/cp-2704-80902-1.html`（衛福部「公布 111 年國人癌症登記資料分析結果」）→ 可讀，
  但**只公布十大癌症，腦及中樞神經系統不在其中，全文無腦瘤數字**，亦未提供年報全文連結
→ **台灣的腦瘤發生數、GBM 佔比、好發年齡：gap。文章寫「我查不到可以引用的官方版本」。**

**FAIL-5｜若干期刊全文無法取得（只能用摘要）**
- SNO 2024 腦瘤相關癲癇共識（PMC10768995）：未嘗試／未取得全文，本 brief 僅用摘要[S9]
- CBTRUS 2025（2018–2022 年報，PMID 41092086）：無 PMCID，全文未取得，僅用摘要[S3]
- ASCO-SNO 2022 原始指引（PMID 34898238）：無 PMCID，僅用摘要[S6]
- Karschnia 2021 EJC（PMID 33819718）：無 PMCID，僅用摘要[S10]
- Molinaro 2020、Brown 2016、Stummer 2006、De Witt Hamer 2012、GLIOMAP 2022、Teske 2026、Ball 2020、
  de Biase 2021、Buckner 2016、Baumert 2016、van den Bent 2005、Capper 2018、Ontario HTA 2025：僅用摘要
- **注意**：PMC HTML 抓取會間歇性回 reCAPTCHA 挑戰頁（約 20 KB）。本 brief 的每一次 PMC 全文抓取都以
  下載大小驗證（>90 KB 才視為成功），並在必要時重試 2–3 次。

**FAIL-6｜健保重大傷病申請流程細節**
`https://www.nhi.gov.tw/ch/cp-6091-08ad9-2957-1.html`（申請須知及文件下載）未取得可引用內容。
→ 申請要附什麼文件、誰送件：gap。文章寫「問個管師或醫院重大傷病窗口」。

**FAIL-7｜膠質母細胞瘤手術的 30 天／院內死亡率**
RANO resect 2023（PMC10158281 全文）與 RANO risk model 2025（PMC12083231 全文）均**只報告新發神經功能缺損**，
未在可取得文字中報告手術死亡率。Europe PMC 未檢出可引用的專門來源。
→ **A3 不可寫手術死亡率的百分比。**

**FAIL-8｜Ki-67 在膠質瘤的判讀門檻與再現性**
Europe PMC 檢索 `(TITLE:"Ki-67" OR TITLE:"Ki67") AND (TITLE:"glioma" OR "glioblastoma") AND
(ABSTRACT:"reproducibility" OR "interobserver" OR "variability")` → **0 筆**；
`TITLE:"Ki-67" AND TITLE:"glioma"` 的前 8 筆全為影像深度學習預測或單中心預後 nomogram，**無方法學／
再現性／臨床門檻的可引用來源**。
→ **A4 不可寫任何 Ki-67 的百分比門檻。** 只能寫「它不在 WHO CNS5 的診斷與分級判準裡」[S1]。

**FAIL-9｜病理報告週轉時間（turnaround time）**
本次未檢索到可引用的國際或台灣資料。
→ **A4「報告要等多久」一節寫成診間語言，不編數字**（SPEC §五 A4 已如此要求）。

**NOT-CITABLE-1｜Pitter KL, et al. "Corticosteroids compromise survival in glioblastoma." Brain.
2016;139:1458–1471.**
出現在 EANO 2021 的參考文獻中[S5]，**回溯性資料**。A2 不引用其結論；若 C2 要用，由 C 組自行查證原文。

**NOT-CITABLE-2｜Aldave G, et al. Neurosurgery. 2013;72(6):915–920（5-ALA 殘餘螢光與存活）。**
PMID 23685503。回溯性、單中心 52 人。本 brief 不列為 A3 的 PASS 來源（世代太小、單中心、回溯），
但保留供作者知道存在。

**NOT-CITABLE-3｜Molica C, et al. Sci Rep. 2023;13:20101（cIMPACT-NOW Update 3 signature 的單中心驗證）。**
PMID 37973912，isOpenAccess Y。單中心 313 例。可信但非必要；A1 已有 cIMPACT-NOW 原文[S2]與 WHO CNS5[S1]，
不需要再加單中心資料。

---

## 交叉引用與歸屬提醒（給寫作者）

依 SPEC §六，本 brief 中下列材料**不屬於 A 組**，請只在必要時一句指路，不要展開：

| 材料 | 歸屬 | A 組的處理 |
|---|---|---|
| 中位存活、5 年存活、存活曲線讀法 | **B4** `gb-numbers` | A1/A3/A5 若引用絕對月數，同段一句「這個數字怎麼讀，見〈那個數字，我要怎麼跟你講〉」 |
| MGMT 甲基化與治療效果／存活 | **B2** `gb-mgmt` | A4 只寫「這個數字是怎麼測出來的、為什麼會不一樣」 |
| Stupp 療程、60 Gy/30 次 | **B1** `gb-standard` | A2/A3 不提療程細節 |
| 高齡減量療程 | **B3** `gb-elderly` | A3 只寫「supramaximal 的好處在 65 歲以下才看得到」[S18]，不談療程 |
| 類固醇減量、副作用、聯絡時機 | **C2** `gb-steroid`（紅線 4） | A2 只寫「術前為什麼先給、什麼時候先不給」[S5]，一句指路 |
| 抗癲癇藥選擇、開車 | **C3** `gb-seizure`（紅線 5） | A2 只寫「沒發作過不常規給」[S5]，一句指路 |
| 顱內壓升高等急症 | **C4** `gb-warning-signs`（紅線 6） | A1–A5 各一句「見〈哪些狀況要當天回來〉」 |
| 假性惡化、追蹤 MRI | **D1** `gb-followup`（紅線 8） | A2 提到 perfusion MRI 可協助分辨假性惡化時[S5]，一句指路，不展開 |
| 認知副作用、海馬迴保護 | **D2** `gb-cognition` | A5 解釋「為什麼想延後放療」時一句帶過[S23]，不展開 |
| 腦轉移 | 站上 `lc-brainmet` | A1 一句指路[S4] |
| 腦膜瘤 | 另開專題 | A1 一句[S1][S3] |
| 再照射、TTFields、質子、BNCT | B5／D3／站上 `nt-*`、`sit-*` | A 組完全不提 |

