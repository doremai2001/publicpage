# -*- coding: utf-8 -*-
"""BNCT 分組英文版 — 批次 C：newgbm / melanoma / meningioma / others / safety / approval / who"""

EN = {}

EN["newgbm"] = dict(
 title="Newly diagnosed, and someone just sent you a BNCT link",
 dek="Recurrent brain tumours have phase 2 data. Newly diagnosed ones do not. The distance between those two is longer than most people assume.",
 lead="The people who reach this article are usually newly diagnosed, with a relative who has just found BNCT online. So I will put it bluntly.",
 body="""<p>Level of evidence: <strong>phase 1 / dose-finding, and no efficacy results have been published.</strong></p>

<h4>How far this has actually got</h4>
<p>The University of Tsukuba in Japan is running a phase 1 trial on a linear accelerator it developed itself, in newly diagnosed glioblastoma, giving BNCT plus external-beam radiotherapy plus temozolomide<a href="https://doi.org/10.1016/j.apradiso.2025.112152" target="_blank" rel="noopener"><sup class="cit">[1]</sup></a>.</p>
<p>But look carefully at the design: <strong>the primary endpoint is the incidence of dose-limiting toxicity</strong>, the maximum normal-brain dose for the first three patients was set at a conservative ceiling, and the target accrual is 12 to 18 people. And the paper I found <strong>is the trial protocol, not a results report</strong> — it says of itself that the results "will be presented at international conferences and submitted to a peer-reviewed journal".</p>
<p>In other words, the question this trial is asking right now is whether this goes wrong. It has not got as far as whether it works.</p>

<h4>What a phase 1 trial is for, and what it is not for</h4>
<p>This deserves its own section, because it applies to every new treatment.</p>
<p>A phase 1 trial exists to find a safe dose and an acceptable range of toxicity. It enrols very few people, usually has no control arm, and <strong>is not designed to demonstrate efficacy in the first place</strong>. So the sentence "a phase 1 trial of BNCT in such-and-such cancer is under way" translates as: <strong>nobody knows yet whether it works; they are checking whether it is safe.</strong></p>
<p>Press releases like to write "has entered clinical trials" as a milestone. It is one. But that milestone sits a long way short of "can be treated as an option".</p>

<h4>What the reactor years left behind</h4>
<p>In the 2000s Japan ran a case series in newly diagnosed glioblastoma on a research reactor: 21 people, 2002 to 2006, using both BSH and BPA. The first 10 had BNCT alone; the next 11 had 20 to 30 gray of external-beam radiotherapy added after BNCT. Median survival for the two groups combined was 15.6 months; for the 11 who had the added radiotherapy it was 23.5 months<a href="https://www.jstage.jst.go.jp/article/jrr/50/1/50_08043/_article" target="_blank" rel="noopener"><sup class="cit">[2]</sup></a>.</p>
<p>That 23.5 cannot be set beside today's standard treatment, for two reasons. <strong>Those 11 were not randomised to the extra radiotherapy</strong> — only people who had come through BNCT and were still in reasonable shape could have it, so part of that number is simply a matter of who lived long enough. And I cannot find the in-house control figures from that report, so <strong>even its own comparison cannot be reconstructed.</strong></p>
<p>This is retrospective data compared against an institutional historical control, not a randomised trial. And note the dominant pattern of death: cerebrospinal fluid dissemination and local recurrence<a href="https://www.jstage.jst.go.jp/article/jrr/50/1/50_08043/_article" target="_blank" rel="noopener"><sup class="cit">[2]</sup></a>. <strong>BNCT hits what is inside the irradiated field. It does nothing about what has already gone elsewhere.</strong></p>

<h4>If your family member was diagnosed last week</h4>
<p><strong>The conclusion first: for newly diagnosed glioblastoma, BNCT is not currently a treatment option.</strong> Standard treatment is surgery, radiotherapy plus temozolomide. The evidence behind that is randomised-trial grade, and in this box BNCT has not yet finished phase 1.</p>
<p>"Standard treatment you have not yet used up", in the first warning, is describing exactly this situation. <strong>This is not the moment for either/or</strong> — do what standard treatment has to offer first, and if this road really does run on that far, the data in article ten becomes something that concerns you then.</p>""",
)

EN["melanoma"] = dict(
 title="The best-looking numbers, the smallest denominators",
 dek="A sixty-eight per cent complete response rate, and a case count in the thirties. Those two numbers have to be read together.",
 lead="This article has the smallest denominators in the whole topic. I am writing it because it happens to show cleanly that a high response rate and strong evidence are two different things.",
 body="""<p>Level of evidence: <strong>case series. No control arm, and denominators running from single figures to twenty-odd people.</strong></p>

<h4>Why these two cancers and not others</h4>
<p>Back to the physics in article three: neutrons do not travel deep. A lesion on the skin sits exactly in the few centimetres where neutrons still have force behind them. Add that melanocytes take up BPA reasonably well, and those two conditions together made skin lesions one of the earliest indications BNCT had.</p>

<h4>The melanoma numbers, and the glasses you need to read them</h4>
<p>The earliest Japanese group, 22 people between 1987 and 2002: complete response 68.2% (15 people), partial response 23.0% (5 people)<a href="https://www.mdpi.com/2073-4409/10/11/2881" target="_blank" rel="noopener"><sup class="cit">[1]</sup></a>. The survival column needs a different pair of glasses. What that report gives is a five-year cause-specific survival — <strong>only people who died of melanoma go into the numerator, deaths from other causes do not, so it is always higher than overall survival, and it is not the same thing as cure.</strong> On that definition it was 58% overall and 74% for primary lesions. The report gives no overall survival, and I cannot find one. The same team went on to treat 8 more people between 2003 and 2014, 6 of them complete responses, and 5 of those still disease-free 5.6 to 8.2 years after treatment<a href="https://www.mdpi.com/2073-4409/10/11/2881" target="_blank" rel="noopener"><sup class="cit">[1]</sup></a>.</p>
<p>Argentina treated 7 people on their own research reactor, for multiple cutaneous metastases on the limbs. They report a response rate of about seventy per cent, <strong>but that is counted per lesion</strong> — one person carries dozens of nodules, and what is being counted is how many nodules shrank, not that seventy per cent of the patients responded. The same dataset separately reports grade 3 ulceration in three in ten<a href="https://www.mdpi.com/2073-4409/10/11/2881" target="_blank" rel="noopener"><sup class="cit">[1]</sup></a><a href="https://doi.org/10.3389/fonc.2021.601820" target="_blank" rel="noopener"><sup class="cit">[2]</sup></a>. (I could not obtain the primary papers for this series; the figures are cross-supported by two review articles.) MIT in the United States treated 4 people<a href="https://www.mdpi.com/2073-4409/10/11/2881" target="_blank" rel="noopener"><sup class="cit">[1]</sup></a>.</p>
<p>Add all of that up and <strong>the published human data on BNCT for melanoma worldwide is of the order of thirty or forty cases</strong>, concentrated in lesions of the skin and the limbs. <strong>Not visceral metastases.</strong> That distinction matters, because what actually changes survival in melanoma now is immunotherapy, and that is the answer for systemic disease.</p>

<h4>Extramammary Paget's disease: numbers I will not add up</h4>
<p>This is an uncommon skin cancer that grows on the genitals and around the anus. The Japanese series included 3 patients, all of whom reached complete response within six months; one of them died of heart disease 3.2 years later with no tumour recurrence, and the other two were still free of recurrence at 6.5 and 6.9 years<a href="https://link.springer.com/article/10.1186/s40880-018-0297-9" target="_blank" rel="noopener"><sup class="cit">[3]</sup></a>. The side effects were mainly local erosion and difficulty passing urine, grade 2<a href="https://doi.org/10.3389/fonc.2021.601820" target="_blank" rel="noopener"><sup class="cit">[2]</sup></a>.</p>
<p>There is an earlier report of 2 more, but I cannot confirm whether those 2 and these 3 are the same people (same system, overlapping period). <strong>So I do not add them together.</strong> The honest way to say it is that the published cases of BNCT for this disease are in single figures.</p>

<h4>Three marks off these pretty numbers</h4>
<p>Complete response in seven or eight out of ten is a figure any cancer treatment would envy. But what these reports do not answer is what would have happened to the same lesions treated another way. And a case series of single figures to twenty-odd people has no defence at all against selective reporting — the ones that go well are the ones that get written up. More to the point, what they report is <strong>local</strong> response: that patient with vulvar melanoma genuinely had no local recurrence, and died of systemic metastases 1.1 years later<a href="https://link.springer.com/article/10.1186/s40880-018-0297-9" target="_blank" rel="noopener"><sup class="cit">[3]</sup></a>. Handling the local disease well is not the same as the disease being controlled.</p>
<p>It looks best on the skin, and it is on the skin that it shows what it is: <strong>it only deals with what it can reach.</strong></p>""",
)

EN["meningioma"] = dict(
 title="Meningioma: the big trial that is never coming",
 dek="After a high-grade meningioma recurs there is no standard answer. BNCT has 44 patients' worth of data here — this is what that weighs, and where its ceiling is.",
 lead="This one also applies if you have some other rare cancer: how to read the only evidence you have, when your disease is too uncommon for a randomised trial to be possible.",
 body="""<p>Level of evidence: <strong>case series, 44 patients, no control arm.</strong> That is already the largest dataset this indication has.</p>

<h4>What the 44 patients bought</h4>
<p>A Japanese team put together 44 patients with recurrent or refractory high-grade meningioma, of whom 20 were WHO grade 2 (45.5%) and 24 were grade 3 (54.5%)<a href="https://academic.oup.com/neuro-oncology/article/24/1/90/6275296" target="_blank" rel="noopener"><sup class="cit">[1]</sup></a>.</p>
<p>Median overall survival after BNCT was 29.6 months (95% confidence interval 16.1 to 40.4); split out, 44.4 months for grade 2 and 21.6 months for grade 3, a difference that was statistically significant. Median progression-free survival was 13.7 months. Among the 36 patients whose imaging response could be assessed, 6 had a complete response (16.7%), 17 a partial response (47.2%) and 13 stable disease (36.1%)<a href="https://academic.oup.com/neuro-oncology/article/24/1/90/6275296" target="_blank" rel="noopener"><sup class="cit">[1]</sup></a>.</p>
<p>The price column has to be read as well: <strong>grade 2 radiation necrosis 34.1%, grade 3 radiation necrosis 13.6% - the two grades together come to nearly half</strong><a href="https://academic.oup.com/neuro-oncology/article/24/1/90/6275296" target="_blank" rel="noopener"><sup class="cit">[1]</sup></a>. That is not a rare complication; it is something close to half of these patients ran into.</p>

<h4>The 98.4 months is not a treatment result</h4>
<p>The same report also carries a median survival of 98.4 months counted from diagnosis. That number cannot be used as a treatment result — it takes in the years of disease course before the recurrence, and it reflects the fact that people who live long enough to be considered for BNCT were already travelling slowly. <strong>For the treatment effect, the number to look at is the 29.6 months after BNCT.</strong></p>

<h4>Two reactor-era reports that must not be stacked</h4>
<p>To fill in the background. Japan's total volume of malignant brain tumours treated on research reactors between January 2002 and May 2014 was 167 cases, covering recurrent malignant glioma, newly diagnosed malignant glioma and recurrent high-grade meningioma<a href="https://www.jstage.jst.go.jp/article/nmc/56/7/56_ra.2015-0297/_article" target="_blank" rel="noopener"><sup class="cit">[2]</sup></a> — <strong>but how those 167 break down, and how long each group lived, that report does not separate out, and I cannot find it either.</strong></p>
<p>Separately there is an earlier report, from the same researchers, of 22 patients with recurrent malignant glioma accumulated from 2002 onwards, median survival 10.8 months, with the comparison drawn from historical data published by others<a href="https://link.springer.com/article/10.1007/s11060-008-9699-x" target="_blank" rel="noopener"><sup class="cit">[3]</sup></a>. <strong>Whether the patients in the two reports overlap cannot be worked out from what is public, so do not add them together and do not divide one by the other.</strong></p>
<p>All of this is fifteen or twenty years old and was done on reactors. It is where the field started, not the evidence base it stands on now.</p>

<h4>Why the evidence for a rare cancer stops here</h4>
<p>High-grade meningioma is uncommon to begin with, and rarer again once it recurs. A randomised trial with real statistical power needs a number of patients that a disease like this cannot produce, or could only produce over fifteen years or so. This is not researchers failing to try. The denominator is not there.</p>
<p>So if your disease belongs in this category, the reality you have to face is that <strong>the decisive trial is not coming.</strong> The judgement you have to make will always rest on case series and expert consensus.</p>
<p>In that position, here is what I do. Get the denominator and the presence or absence of a control arm clear first, the way I have above. Give the side-effect rates the same weight as the efficacy figures — here, close to half of the patients developed radiation necrosis. Then look first at putting yourself into a trial that is actually running, because at least that way your experience accumulates into evidence for the next person.</p>""",
)

EN["others"] = dict(
 title="Why the list is almost empty",
 dek="This article has no good news in it. It may also be the one most people here need, because the people who ask whether their cancer qualifies mostly belong in this box.",
 lead="The people who ask me whether this can be done for their cancer mostly do not have head and neck cancer or a brain tumour. This is written for them, and it has no good news.",
 body="""<p>Level of evidence: <strong>case reports. For the deep organs there is no series, let alone trial results.</strong></p>

<h4>Back to the line drawn in article three</h4>
<p>Epithermal neutrons weaken the further they travel through tissue. Liver, lung, pancreas, deep pelvis — at those positions the neutrons either do not arrive, or arrive at a cost to normal tissue that already exceeds what the tumour gains.</p>
<p>So the reason this box is empty is not that nobody studied it. It is that <strong>people did study it, and the physics stopped them.</strong></p>

<h4>The liver: someone did try to go around the physics</h4>
<p>In 2001 and in 2003, an Italian team treated one patient each<a href="https://www0.mi.infn.it/~gadioli/Varenna2006/Proceedings/Altieri_S.pdf" target="_blank" rel="noopener"><sup class="cit">[1]</sup></a>. Both had diffuse liver metastases from colorectal cancer that could not be resected.</p>
<p>The method was this: inject the boron drug, then <strong>take the entire liver out of the body</strong>, wash the blood out of it, put it in a bag, carry it to the reactor, irradiate it for about ten minutes, and carry it back to theatre to be re-implanted. Boron concentrations measured in the explanted liver were about 45 parts per million in tumour and about 8 in normal liver, a ratio above 5.</p>
<p>What happened: the first patient survived 44 months with reasonable quality of life, and died in the end of diffuse recurrence of the bowel tumour. <strong>The second developed a vascular complication, was operated on again on day 31 after BNCT, and died of sudden heart failure on day 33.</strong></p>
<p>Two people. One lived nearly four years, one was gone in a little over a month. I write it out because it sometimes gets cited as evidence that BNCT can treat liver cancer too. <strong>A thing that can only be done by lifting the liver out and irradiating it outside the body tells you by itself how hard the limit is.</strong></p>

<h4>Where Taiwan's liver trial actually stands</h4>
<p>Tsing Hua University has an academic clinical trial in liver cancer, but when I checked, the status on the official page was <strong>"under application" — not yet through review, not yet enrolling</strong>, with a target of 10 evaluable patients<a href="https://thor.site.nthu.edu.tw/p/406-1192-302043,r11030.php?Lang=zh-tw" target="_blank" rel="noopener"><sup class="cit">[2]</sup></a>.</p>
<p>This is worth saying out loud, because in 2024 there were news reports of a "world first". Those reports were about this programme, not about a treatment that had been completed. <strong>A trial being under application and a treatment being available are two different things.</strong> If you or a family member is being pointed towards liver BNCT at Tsing Hua, that is the first thing to check.</p>

<h4>Lung and pleura</h4>
<p>There is one Japanese case report: a 62-year-old man with recurrent lung adenocarcinoma in the left chest wall, previously operated on and irradiated to 60 gray. BNCT was given in two fractions. At seven months the PET uptake value had fallen from 22.1 to 7.1 and most of the tumour had regressed; <strong>but in the eighth month it recurred at the edge of the field</strong>, and he went on to have intensity-modulated radiotherapy<a href="https://link.springer.com/article/10.1007/s13691-012-0048-8" target="_blank" rel="noopener"><sup class="cit">[3]</sup></a>.</p>
<p>One patient. The response was real and so was the recurrence.</p>
<p>As for malignant pleural mesothelioma — reviews mention that diffuse pleural tumours have been treated, but I cannot trace a primary report I am able to cite. So the way I put it is: <strong>I can find no verifiable human treatment report.</strong> That is not the same as saying there is none. It is saying I cannot produce one.</p>

<h4>So if your cancer is in this box</h4>
<p><strong>There is at present no data supporting BNCT in the deep organs.</strong> That is the whole of it. If someone proposes it to you, these questions are worth saying out loud: how many people with this disease have had it, where was that published, how many centimetres is my tumour from the skin, and at that depth what dose does the tumour get relative to normal tissue?</p>
<p>The last question usually ends the conversation. That is not a bad thing — keeping your time and your physical reserve for the options that have a real chance is itself a treatment decision.</p>""",
)

EN["safety"] = dict(
 title="The side effects are not fewer, they are different",
 dek="A kill radius of one cell does not mean normal tissue goes untouched. This lays the published adverse events out, including the worst one.",
 lead="If you finish only one article in this topic, I would like it to be this one. These numbers almost never appear in BNCT marketing language, and every one of them comes from the trials that support the treatment.",
 body="""<p>Start with the physics again. Article two set out that when neutrons go into tissue they produce four kinds of dose at once, and three of them have nothing to do with whether you took up any boron. <strong>Those three land on every tissue the neutrons pass through.</strong> So "a kill radius smaller than one cell" is describing the boron component, not the treatment.</p>

<h4>The ones almost everybody gets</h4>
<p>Japan's national post-marketing surveillance after approval, data on 162 patients<a href="https://www.mdpi.com/2072-6694/16/5/869" target="_blank" rel="noopener"><sup class="cit">[1]</sup></a>: hyperamylasaemia 84.0%, oral mucositis 51.2%, sialadenitis 50.6%, alopecia 49.4%. Among the late effects: difficulty swallowing 4.5%, thirst 2.6%, skin disorder 1.9%. (That dataset is not graded, so those are total incidences.)</p>
<p>The amylase item is worth a word of explanation: BPA is taken up by the salivary glands, so the salivary glands take dose along with everything else. That is also where the dry mouth and the sialadenitis come from. <strong>It is not an accident. It is what the distribution of the drug dictates.</strong></p>
<p>Treatment in the brain looks nothing like this: it is brain oedema and radiation necrosis, not mucositis and sialadenitis. In that recurrent glioblastoma trial, nearly half the patients developed brain oedema and grade 3 or higher adverse events ran above eight in ten; the actual rates are in article ten<a href="https://academic.oup.com/noa/article/3/1/vdab067/6279119" target="_blank" rel="noopener"><sup class="cit">[2]</sup></a>. In the 44-patient meningioma series, grade 2 and grade 3 radiation necrosis together come to nearly half; that figure is in article thirteen<a href="https://academic.oup.com/neuro-oncology/article/24/1/90/6275296" target="_blank" rel="noopener"><sup class="cit">[3]</sup></a>.</p>

<h4>The worst one: carotid blowout</h4>
<p>Read this section slowly.</p>
<p>In a Japanese prospective series of 62 patients, <strong>3 patients had carotid haemorrhage, and 2 of them died of infected carotid rupture</strong>; 1 was saved by surgery. That is a rate of 4.8%<a href="https://academic.oup.com/jrr/article/55/1/146/917082" target="_blank" rel="noopener"><sup class="cit">[4]</sup></a>. The same report had 3 treatment-related deaths in all.</p>
<p>The next sentence is the one that matters: <strong>all 3 of those patients had tumour invading the carotid artery, and had already been re-irradiated there</strong><a href="https://academic.oup.com/jrr/article/55/1/146/917082" target="_blank" rel="noopener"><sup class="cit">[4]</sup></a>. Another series of 33 patients has reported 2 further cases, occurring one to three months after treatment<a href="https://doi.org/10.3389/fonc.2021.601820" target="_blank" rel="noopener"><sup class="cit">[5]</sup></a> — though I have seen this one only as it is relayed in a review article and could not obtain the primary report, so treat it as corroboration rather than a number you can compute a rate from.</p>
<p>And that 162-patient post-marketing surveillance states in as many words that <strong>no carotid rupture occurred</strong><a href="https://www.mdpi.com/2072-6694/16/5/869" target="_blank" rel="noopener"><sup class="cit">[1]</sup></a>.</p>
<p>The two look contradictory and are not. What they are telling you is this: <strong>the risk is not spread evenly over all patients. It is heavily concentrated in one particular group — people whose tumour wraps around the carotid artery, and whose carotid has already been irradiated.</strong> Which is why asking what the chance of carotid rupture with BNCT is, is asking the wrong question. The question is whether you are in that group.</p>

<h4>The re-irradiation allowance</h4>
<p>So the allowance in the warning has a concrete shape in this article: go past it and what you get is necrosis, ulceration, rupture of a large vessel.</p>
<p>Article two explained that BNCT's Gy-Eq cannot be added cleanly onto the dose you had before. So the re-irradiation judgement here is not arithmetic, it is clinical judgement — and it is judgement that needs a doctor who knows the field you were irradiated in last time. <strong>If the person assessing you does not have your previous radiotherapy plan in front of them, that assessment is incomplete.</strong></p>

<h4>A contradiction I ran into while fact-checking</h4>
<p>Putting this article together I hit something worth writing down. A commentary on JHN002 states that there was no grade 4 or grade 5 toxicity, while the adverse-event sub-analysis of the same trial has grade 4 hyperamylasaemia in seven out of ten patients. The two do not reconcile — the likeliest explanation is that the commentary meant symptomatic events, but it does not say so.</p>
<p>So when you see a claim that there are no serious side effects, it is worth going back to the primary report. Every time I have done that, the original paper reads worse than the piece describing it. There is a reason for that: <strong>papers have to pass review, write-ups do not.</strong></p>""",
)

EN["approval"] = dict(
 title="One technology, four different identities",
 dek="Approved, covered and effective are three separate things. This puts BNCT on that map, with a check date on every box.",
 lead="This is the fixed move in this topic: for any new technology, ask what its status is, where. For BNCT the answer is unusually clean, because exactly one place in the world has approved it.",
 body="""<p>Every regulatory status in this article was checked on 8 September 2026. Regulation moves quickly, so please confirm it again by the time you are reading this.</p>

<h4>Japan: the only approval, and it is a drug plus a machine</h4>
<p>Manufacturing and marketing approval for the boron drug borofalan (10B) was granted on 25 March 2020, and the licence is held by a Japanese pharmaceutical company<a href="https://www.kegg.jp/medicus-bin/japic_med?japic_code=00068760" target="_blank" rel="noopener"><sup class="cit">[1]</sup></a>. The approved indication reads, word for word: <strong>「切除不能な局所進行又は局所再発の頭頸部癌」</strong> — unresectable locally advanced or locally recurrent head and neck cancer. <strong>That one indication.</strong> Not "head and neck cancer": head and neck cancer that is "unresectable, locally advanced or locally recurrent".</p>
<p>The same package insert requires that the drug be used together with an approved neutron irradiation device<a href="https://www.kegg.jp/medicus-bin/japic_med?japic_code=00068760" target="_blank" rel="noopener"><sup class="cit">[1]</sup></a>. That device obtained medical device approval on 12 March 2020<a href="https://www.shi.co.jp/english/info/2019/6kgpsq0000002ji0.html" target="_blank" rel="noopener"><sup class="cit">[2]</sup></a>.</p>
<p>On reimbursement, the drug was added to the national drug price standard and put on the market on 20 May 2020<a href="https://medical.nikkeibp.co.jp/leaf/all/series/drug/update/202006/566060.html" target="_blank" rel="noopener"><sup class="cit">[3]</sup></a>. <strong>Japan has all three, and gives them to one indication only.</strong> That is the only such case in the world.</p>

<h4>The United States: nothing I can find</h4>
<p>I can find no FDA-approved BNCT drug or device.</p>
<p>The more persuasive indirect evidence is this. In September 2025 an American manufacturer and the University of Wisconsin–Madison announced that the university would become the <strong>"first in the United States"</strong> to install their accelerator-based BNCT system and run the <strong>"first clinical trials"</strong> with it, and the press release states in as many words that the system and the new boron drug are for research use only and not for sale<a href="https://www.businesswire.com/news/home/20250925542671/en/" target="_blank" rel="noopener"><sup class="cit">[4]</sup></a>. The list of currently operating BNCT treatment centres published by the international society does not include the United States either<a href="https://isnct.net/bnct-clinical-centers/" target="_blank" rel="noopener"><sup class="cit">[5]</sup></a>.</p>
<p>I want to be exact about the wording here: this is "<strong>I can find no</strong> approval", not "confirmed not approved" — I have no way of querying that country's device and drug databases directly.</p>

<h4>Europe: in trials, and only just started</h4>
<p>The first accelerator-based BNCT treatment in Europe took place in June 2025, at Helsinki University Hospital. Those patients were <strong>enrolled in an ongoing clinical trial</strong>, with unresectable locally recurrent head and neck cancer as the indication<a href="https://www.raysearchlabs.com/media/press-releases/2025/raystation-used-for-pioneering-clinical-milestone-at-helsinki-university-hospital--first-treatment-with-accelerator-based-bnct-in-europe/" target="_blank" rel="noopener"><sup class="cit">[6]</sup></a>.</p>
<p>On the European Medicines Agency side I can find no record I am able to cite, so I write neither "approved" nor "not approved". <strong>What can be established is that Europe is running trials at present, not routine treatment.</strong></p>

<h4>Taiwan: the device is licensed, the drug is not</h4>
<p>This is the column most easily misread, and it is worth taking apart into three sentences.</p>
<p>First, the device is licensed. The "NTHU neutron radiation irradiation system" received a medical device licence from the Ministry of Health and Welfare in June 2023<a href="https://www.nthu.edu.tw/hotNews/content/1141" target="_blank" rel="noopener"><sup class="cit">[7]</sup></a>.</p>
<p>Second, a licensed device is not an approved treatment. A device licence says the equipment itself may lawfully be used; it does not answer whether treating some particular cancer with BNCT is an approved indication. And on the drug side — what Japan approved was a drug together with a machine — I can find no marketing licence for any BNCT boron drug in Taiwan.</p>
<p>Third, how patients are being treated at the moment. Two routes: academic clinical trials, and the case-by-case route that the official page calls "emergency treatment"<a href="https://thor.site.nthu.edu.tw/p/403-1192-11030-1.php?Lang=zh-tw" target="_blank" rel="noopener"><sup class="cit">[8]</sup></a>. It is not covered by National Health Insurance. The official page does not state which regulatory category that case-by-case route falls under, and I can find no formal text I am able to cite, so I do not give it a name.</p>
<p>A note on history: in 2010 the Department of Health stated publicly that it had at that point agreed to the equipment being used only for conducting drug clinical trials, and had not approved it for routine radiotherapy practice<a href="https://www.mohw.gov.tw/cp-3161-26718-1.html" target="_blank" rel="noopener"><sup class="cit">[9]</sup></a>. That is a position from sixteen years ago and things have evidently moved since, but I mark the year, because it is the only official wording I can find for this box.</p>

<h4>Keep the three apart</h4>
<p><strong>Approval is settled by regulators, coverage by money, and effectiveness only by evidence.</strong> Japan has all three, except that the box marked "effective" holds a single-arm trial of 21 people. In Taiwan the device is licensed and treatment runs case by case; in Europe and the United States it is in trials.</p>
<p>And that "effective" box — articles nine through fourteen are about it, and the answer is that one indication has single-arm phase 2 data and everything else is case series or less.</p>""",
)

EN["who"] = dict(
 title="Should I be asking about BNCT? Four preconditions",
 dek="This gathers the previous sixteen articles into one checklist. Meeting all four is not a reason to do it; failing one is a reason not to go further.",
 lead="This article is the most practical reason I wrote the topic at all. If you read only one, read this one — but if any of the four conditions is unclear to you, go back to the article that covers it.",
 body="""<p>These are the four I ask in clinic, in this order. If the first has no answer, the other three do not need asking.</p>

<h4>One: has standard treatment actually run out?</h4>
<p>All the human data on BNCT enrolled patients for whom standard treatment was exhausted or unsuitable. The eligibility criteria of the Taiwanese recurrent head and neck cancer trial put it most plainly: the patient must already have had conventional radiotherapy, and all three salvage routes — surgery, radiotherapy, chemotherapy — must be <strong>unsuitable</strong><a href="https://ctv.veeva.com/study/boron-neutron-capture-therapy-bnct-for-locally-recurrent-head-and-neck-cancer" target="_blank" rel="noopener"><sup class="cit">[1]</sup></a>.</p>
<p>So if standard treatment still has an option you have not used, the question does not arise yet. That is not conservatism. Those numbers were produced in that position, and moving them forward means deciding on a set of data that does not apply to you.</p>

<h4>Two: is it shallow enough?</h4>
<p>Neutrons do not travel deep (article three). For a midline brain tumour, around eight centimetres is the depth at which the literature still holds a therapeutic ratio; go deeper and the cost to normal tissue starts to exceed the gain to the tumour.</p>
<p>The concrete question to ask: <strong>"How many centimetres is my tumour from the skin surface, and at that depth what dose does the tumour get relative to normal tissue?"</strong> If the person cannot answer, or gives you an answer along the lines of "it can be used anywhere", that is your answer.</p>

<h4>Three: can the boron get in?</h4>
<p>A PET scan using fluorine-18-labelled BPA measures the uptake ratio between tumour and normal tissue, and the threshold in common use is 2.5<a href="https://ctv.veeva.com/study/boron-neutron-capture-therapy-bnct-for-locally-recurrent-head-and-neck-cancer" target="_blank" rel="noopener"><sup class="cit">[1]</sup></a> (article five).</p>
<p>This step can be done in advance, and it should be. <strong>Someone whose uptake is insufficient, going ahead into the neutron beam, takes the whole cost and gets almost none of the benefit.</strong> Being judged unsuitable saves money, saves physical reserve, and saves the thing the next condition is about.</p>

<h4>Four: has anyone actually done the re-irradiation arithmetic?</h4>
<p>This is the one most easily skipped. Almost every BNCT patient has been irradiated once already, and there is a ceiling on the total dose any one site can take. In the 62-patient series in article fifteen, 3 patients had carotid haemorrhage (2 of them died of infected rupture) — <strong>and all 3 of them had tumour invading the carotid artery and had already been irradiated once in that same place. So the question to ask is not what the probability is, it is whether you are in that group.</strong></p>
<p>There is no standard answer to this one, only whether anyone has genuinely sat down and worked it out. What to ask: <strong>"Have you seen the field and the dose from my previous radiotherapy?"</strong> If they cannot produce your last dose distribution, this question has not started yet.</p>

<h4>Once all four are met, there is still one thing</h4>
<p>Even with all four conditions passed, we come back to warning one: <strong>what am I giving up by doing this.</strong></p>
<p>For someone in the later lines, a course of this takes up a stretch of physical reserve, a stretch of time, a sum of money, and one use of the re-irradiation allowance. Those same things are what later-line self-paid drugs, or joining a clinical trial, would also draw on. I will not rank them for you — but before you sign, get the total down to an exact figure, and then write down two or three other uses of that same stretch of time and that same money to set beside it.</p>

<h4>Three questions to take to clinic</h4>
<p>If you remember only three sentences, remember these.</p>
<p><strong>"Has my standard treatment really run out, or is there something I have not used?"</strong></p>
<p><strong>"Should I have a PET scan first to measure the boron uptake? If the ratio comes back below the threshold, what do you recommend?"</strong></p>
<p><strong>"Given the field I have already been irradiated in, how do you assess the risk of irradiating it again?"</strong></p>
<p>The last two are not there to be awkward; they are the fastest way to tell. <strong>Someone who can answer them can usually also tell you why you are not suitable.</strong></p>""",
)
