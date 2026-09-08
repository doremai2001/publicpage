# -*- coding: utf-8 -*-
"""BNCT 分組英文版 — 批次 A：principle / dose / depth / drugs / pet / newagents

引用連結的 HTML 逐字照抄 zhsrc/<slug>.html，順序與重複位置與中文一致。
只含 <h4> 與 <p>；雙警語、排擠句、揭露、日期、參考清單由建置程式加上。
"""

EN = {}

EN["principle"] = dict(
 title="Smaller than a single cell",
 dek="Its precision comes from shrinking the kill radius to less than the width of one cell. Every strength it has, and every weakness, grows out of that.",
 lead="This article is about the one thing that is genuinely unusual in BNCT. By the end you will see why every question anyone asks about it comes back to the same sentence: where did the boron go?",
 body="""<p>Photons, protons, heavy ions — the logic of aiming is geometric in all of them: work out where the tumour is, point the beam at it. BNCT does not do that. It moves the whole business of being on target out of geometry and into chemistry.</p>

<h4>The reaction itself: an unusually large target</h4>
<p>Boron-10 has one property that matters here: its probability of capturing a low-energy neutron is very high. In nuclear physics that probability is written as a cross-section, measured in barns, which you can read as how big the target looks. The cross-section of boron-10 for thermal neutrons is about 3837 barn<a href="https://ocw.mit.edu/courses/22-55j-principles-of-radiation-interactions-fall-2004/382568947f61a0473afc13cbe688b3e4_bnct_lect_so4.pdf" target="_blank" rel="noopener"><sup class="cit">[1]</sup></a><a href="https://www.mdpi.com/2673-4362/7/1/6" target="_blank" rel="noopener"><sup class="cit">[2]</sup></a> — several orders of magnitude larger than the elements a human body is mostly made of. And one sentence has to follow immediately: there are only a few parts per million of boron in the body, so when the neutrons pass through tissue, the overwhelming majority of them do not hit boron at all. They hit hydrogen and nitrogen. What those reactions cost is worked out for you in the second article of this series.</p>
<p>After capture, boron-10 splits into an alpha particle and a lithium-7 nucleus. About 94% of the time it takes the ground-state path and releases about 2.31 MeV in total; about 6% of the time it takes the excited-state path, releasing about 2.79 MeV in total and one further gamma ray of 0.48 MeV<a href="https://www.mdpi.com/1718-7729/29/10/622" target="_blank" rel="noopener"><sup class="cit">[3]</sup></a>.</p>

<h4>What matters is how short a distance that energy is spent over</h4>
<p>Carrying that energy, the two fragments travel only five to nine micrometres through tissue before they stop<a href="https://aacrjournals.org/clincancerres/article/11/11/3987/290719/" target="_blank" rel="noopener"><sup class="cit">[4]</sup></a>. That distance is roughly the size of one mammalian cell<a href="https://www.mdpi.com/2673-4362/7/1/6" target="_blank" rel="noopener"><sup class="cit">[2]</sup></a>.</p>
<p>Packing that much energy into that short a track means the energy deposited per unit length is extremely high — in radiobiology, high linear energy transfer. The damage it causes comes in clusters, with the break points sitting close together, and the repair machinery often cannot put them back.</p>
<p>But the thing to remember is the geometric consequence: <strong>the kill radius is smaller than the diameter of one cell.</strong> A cell that has taken boron up is destroyed. The cell next to it, which has not, takes no damage from that boron reaction — <strong>but it still takes the other three doses the neutron beam brings with it. A kill radius smaller than one cell describes the boron component, not the treatment.</strong></p>

<h4>So the selectivity is not planned, it is decided by metabolism</h4>
<p>This is the elegant part of BNCT, and it is where all of its trouble starts. A radiotherapy plan can draw isodose lines, and you can see where the beam lands. The isodose lines of BNCT are drawn at the level of the cell, and they are drawn by which cells took the boron in.</p>
<p>Where uptake is high the effect is there; where uptake is low it is not. Not every cell inside a tumour takes up the same amount, and for the same cancer, uptake differs from one person to the next. This is not a theoretical worry. It can be measured before treatment, and the way it is measured is the PET scan in the fifth article.</p>
<p><strong>A machine can guarantee where the beam goes. No machine can guarantee where the boron goes</strong> — that has to be measured first, and only once it is measured does anyone know whether you are suitable.</p>

<h4>A note on how to read the literature in this field</h4>
<p>When I began this article I meant to give the range of the alpha particle and the range of the lithium-7 nucleus separately. I could not. Two widely cited reviews give ranges that agree with each other, but assign the linear energy transfer values to the two particles the opposite way round; a third review gives an alpha range an order of magnitude larger than everyone else does. Even a number this basic gets copied across wrongly.</p>
<p>So throughout this set of articles, wherever sources fail to agree, I write only the layer they all share — here, five to nine micrometres for the two of them together. That rule comes up again in the articles that follow, because BNCT is a field with more press releases than papers.</p>
""",
)

EN["dose"] = dict(
 title="The Gy that is not a Gy",
 dek="Written the same way, in grays, it means something else entirely. This article teaches you to read the BNCT dose unit, so that a number which looks small does not mislead you.",
 lead="This article teaches one small thing: when you see a BNCT dose figure, look first for the two letters Eq after the unit. Whether they are there changes what the whole sentence means.",
 body="""<p>The unit of radiotherapy dose is the gray (Gy), and its meaning is plain: how much energy is absorbed per kilogram of tissue. BNCT reports its doses in what looks like grays too, but the figure has been converted, and several estimates sit inside that conversion.</p>

<h4>One neutron beam, and the body takes four doses at once</h4>
<p>Once the neutron beam is inside tissue, the boron reaction is not the only thing that happens. At least four things happen at the same time<a href="https://ocw.mit.edu/courses/22-55j-principles-of-radiation-interactions-fall-2004/382568947f61a0473afc13cbe688b3e4_bnct_lect_so4.pdf" target="_blank" rel="noopener"><sup class="cit">[1]</sup></a>:</p>
<p>First, the boron dose — the reaction described in the first article, high linear energy transfer, occurring only where there is boron. Second, the nitrogen dose — nitrogen-14 in tissue captures a neutron and emits a proton of about 0.54 MeV. Third, the fast-neutron dose — neutrons strike hydrogen nuclei and knock protons loose. Fourth, the gamma dose — partly from hydrogen in tissue capturing neutrons, partly contamination carried in by the beam itself.</p>
<p>The last three have nothing to do with whether you took up any boron. <strong>They land on every tissue the neutrons pass through, normal tissue included.</strong> That is the physical reason BNCT cannot be described as leaving normal tissue unharmed.</p>

<h4>Four doses, four biological effects, so four weightings</h4>
<p>The same quantity of energy, deposited in different ways, has very different biological effect. So each component is multiplied by a coefficient and then added together, and the number that comes out is called photon-equivalent dose, written Gy-Eq<a href="https://ocw.mit.edu/courses/22-55j-principles-of-radiation-interactions-fall-2004/382568947f61a0473afc13cbe688b3e4_bnct_lect_so4.pdf" target="_blank" rel="noopener"><sup class="cit">[1]</sup></a>.</p>
<p>The coefficient on the boron component is called the compound biological effectiveness factor, or CBE, and it is not a constant — it changes with the tissue. One set of values in common circulation: 3.8 for tumour, 2.5 for skin, 2.5 for oral mucosa, 1.3 for brain and spinal cord, while the high linear energy transfer components of the beam are all given 3.2<a href="https://aacrjournals.org/clincancerres/article/11/11/3987/290719/" target="_blank" rel="noopener"><sup class="cit">[2]</sup></a><a href="https://ocw.mit.edu/courses/22-55j-principles-of-radiation-interactions-fall-2004/382568947f61a0473afc13cbe688b3e4_bnct_lect_so4.pdf" target="_blank" rel="noopener"><sup class="cit">[1]</sup></a>.</p>
<p>You can see the problem: <strong>the same boron atom and the same neutron beam, scored against tumour and scored against skin, convert into doses that differ by nearly a factor of 1.5.</strong> These coefficients were derived from animal experiments and early clinical work. They are not constants anyone measured.</p>

<h4>Those coefficients were derived, not measured</h4>
<p>Where does CBE come from? From calculation on animal experiments and early clinical series. It is not a constant you can read off directly, the way you read off a density or a half-life. The same MIT teaching material notes that boron biological effectiveness factors in the literature run from 1.3 to over 5<a href="https://ocw.mit.edu/courses/22-55j-principles-of-radiation-interactions-fall-2004/382568947f61a0473afc13cbe688b3e4_bnct_lect_so4.pdf" target="_blank" rel="noopener"><sup class="cit">[1]</sup></a> — a wide span, and it multiplies straight into the final number.</p>
<p>The practical consequence: <strong>a 20 Gy-Eq reported by one centre and a 20 Gy-Eq reported by another stand for different biological effects if the two used different coefficients.</strong> That does not make the numbers meaningless. It makes them estimates with assumptions attached, and the assumptions have to be read alongside them.</p>
<h4>Which is why that number cannot be compared, or added</h4>
<p>Two conclusions you can use.</p>
<p>First, <strong>Gy-Eq and the Gy from the radiotherapy you had before are not the same unit</strong>, and they cannot be compared with each other. When you read that BNCT delivered twenty-something Gy-Eq in one session, do not turn that into "one session worth twenty-something sessions of radiotherapy".</p>
<p>Second, it cannot simply be added to the dose you have already received. Re-irradiation risk in BNCT has no clean formula behind it; it is a clinical judgement rather than arithmetic. Which is why, in the side-effects article — the fifteenth in this series — "the dose does not look high" is not a reassurance you can give yourself.</p>
<p>Next time somebody hands you a BNCT dose figure, you can follow it with one question: <strong>"Is that Gy-Eq? And which set of CBE values?"</strong> Ask that, and the person opposite you will know you have done some reading.</p>
""",
)

EN["depth"] = dict(
 title="Where the neutrons cannot reach",
 dek="Why is the list of BNCT indications so short? Most of the reason is not biology. It is how far into you a neutron can get.",
 lead="The question I am asked most often is whether this cancer of mine can have BNCT. Before any article about a particular cancer, read this one, because most of the answer is settled here.",
 body="""<p>Taking the boron up is only one of the conditions. The neutrons still have to reach it.</p>

<h4>From thermal to epithermal: buying a few more centimetres</h4>
<p>The earliest BNCT used thermal neutron beams, the lowest-energy neutrons and the ones boron captures most readily. The problem is how quickly they fall away: the flux peaks about two to three centimetres below the skin, and by ten centimetres deep only about a tenth of the peak is left<a href="https://www.mdpi.com/1718-7729/29/10/622" target="_blank" rel="noopener"><sup class="cit">[1]</sup></a>. For a brain tumour, that meant opening the skull in order to irradiate it.</p>
<p>The fix that came later was to use epithermal neutrons of slightly higher energy (roughly between 0.5 eV and 10 keV<a href="https://aacrjournals.org/clincancerres/article/11/11/3987/290719/" target="_blank" rel="noopener"><sup class="cit">[2]</sup></a>). They are moderated down to thermal energies after entering tissue, which pushes the thermal peak deeper in. That step brought tumours around six to eight centimetres below the skin into range<a href="https://www.mdpi.com/1718-7729/29/10/622" target="_blank" rel="noopener"><sup class="cit">[1]</sup></a>.</p>

<h4>Reaching it and being worth it are two different questions</h4>
<p>The more useful statement is not a depth in centimetres but the therapeutic ratio: the dose the tumour receives set against the dose the normal tissue receives. For a tumour at the midline of the brain, at a depth of about eight centimetres that ratio is still greater than one<a href="https://doi.org/10.1186/1748-717X-7-146" target="_blank" rel="noopener"><sup class="cit">[3]</sup></a>. Deeper than that, what normal tissue pays begins to catch up with what the tumour gains. To be clear about what that figure is: eight centimetres is the deepest citable data point I could find in the literature, not a boundary anyone has measured.</p>
<p>So picture the reach of BNCT as a region that thins out as it goes in from the skin, not as a switch between in range and out of range. The deeper it goes, the thinner the effect and the heavier the load carried by normal tissue.</p>

<h4>Two centimetres in skin and eight in brain are not the same thing</h4>
<p>Both are depths, and the two numbers mean different things. For a skin lesion the question is whether the lesion itself sits in the layer where the neutrons are still strong. For the brain the question is how much is left by the time the beam has crossed scalp, skull and normal brain and arrived at the tumour. The more tissue lies in between, and the thicker it is, the more attenuation there is — and all of that tissue is taking dose of its own.</p><p>So do not reason from someone having been treated for a brain tumour eight centimetres deep to the thing eight centimetres deep in you being treatable as well. <strong>What lies along the path matters as much as how deep the destination is.</strong></p>
<h4>This is what that very short list of indications is made of</h4>
<p>Apply the physical limit and the pattern stops being surprising. The indication approved in Japan is head and neck; the human data that exist are in brain tumours and skin lesions. <strong>All of them sit in the few centimetres where the neutrons still have strength.</strong></p>
<p>Turn it round, and the deep organs are not waiting to be studied. The neutrons have attenuated away before they arrive. Which organs that rules out, and how people have tried to get around it, is taken one by one in the fourteenth article.</p>
<p>So whether it can be done is often not a doctor deciding. It is a number of centimetres deciding. If somebody tells you BNCT "can be aimed anywhere", that sentence is in conflict with the physics in this article.</p>
""",
)

EN["drugs"] = dict(
 title="The other half that decides it",
 dek="What Japan approved is not a machine. It is a drug and a machine together. This article is about the drug, and about why sixty years have produced only two of them.",
 lead="In sixty years, only two boron drugs have gone into a human being. That fact is itself the puzzle this article sets out to explain.",
 body="""<p>The first article said that the selectivity of BNCT lives in the distribution of the boron. That distribution is decided by the drug. From the 1960s to today, only two boron drugs have been used in people.</p>

<h4>BPA: borrowing the cancer cell's appetite</h4>
<p>BPA is boronophenylalanine, and it is shaped like an amino acid. Cancer cells, in order to grow fast, over-express an amino-acid transporter called LAT1, and BPA rides in on it<a href="https://doi.org/10.3390/pharmaceutics14051106" target="_blank" rel="noopener"><sup class="cit">[1]</sup></a><a href="https://isnct.net/bnct-boron-compounds/" target="_blank" rel="noopener"><sup class="cit">[2]</sup></a>. It is a borrowed mechanism: the boron does not recognise the cancer cell, the cancer cell's appetite takes the boron in.</p>
<p>It comes with a very practical nuisance. BPA is almost insoluble in water, about 0.6 to 0.7 grams per litre, so in the clinic it has to be complexed with a sugar such as fructose before it can go into a vein<a href="https://doi.org/10.3390/pharmaceutics14051106" target="_blank" rel="noopener"><sup class="cit">[1]</sup></a>. That is not a chemist's footnote. The same paper notes that incompletely dissolved BPA can crystallise in the urine and cause haematuria, blood in the urine.</p>
<p>So how much does it actually accumulate? The <strong>tissue-to-blood</strong> boron concentration ratios measured in early clinical work were about 3.5 in tumour, about 1.5 in skin and about 1.0 in normal brain<a href="https://doi.org/10.1186/1748-717X-7-146" target="_blank" rel="noopener"><sup class="cit">[3]</sup></a>. <strong>Note that the denominator of this ratio is blood, not normal tissue</strong> — the 1.0 for normal brain in that same list is the proof of it, since with normal tissue as the denominator the figure could not mean anything. The T/N threshold of 2.5, which the fifth article covers, is the tumour-to-normal-tissue ratio, and the two cannot be exchanged for one another. Hold on to the order of magnitude: not thirty-fold, not a hundred-fold. The selectivity of BNCT is real, and this is about the size of it.</p>

<h4>BSH: it gets in because a door is broken</h4>
<p>The other drug is BSH, sodium borocaptate. It does not use a transporter, and cells do not take it up particularly well<a href="https://doi.org/10.1039/D2NA00839D" target="_blank" rel="noopener"><sup class="cit">[4]</sup></a>. It can be used in brain tumours because the blood-brain barrier at the tumour has already been broken — the drug leaks in there, while the door on the normal-brain side is still shut<a href="https://isnct.net/bnct-boron-compounds/" target="_blank" rel="noopener"><sup class="cit">[2]</sup></a>.</p>
<p>The regulatory standing of the two drugs is very different. What Japan approved in 2020 was BPA, under the drug name borofalan(10B); <strong>BSH has to this day received no drug approval at all, and is still used only inside clinical trials</strong><a href="https://doi.org/10.1039/D2NA00839D" target="_blank" rel="noopener"><sup class="cit">[4]</sup></a>. So when you meet the claim that "Japan has approved BNCT", the accurate version reads: one drug, one machine and one indication were approved.</p>

<h4>The thing neither drug solves</h4>
<p>BPA depends on the cancer cell's appetite and BSH on a broken door, and what the two routes have in common is this: <strong>neither molecule was designed for BNCT. Both were found to happen to work.</strong> So whether the boron goes in, how much of it goes in and how long it stays are largely outside anyone's control. They follow from what this particular tumour's metabolism and blood vessels look like.</p><p>Which is why the scan in the next article is not optional. <strong>The drug cannot guarantee selectivity, only offer an opportunity for it; whether it actually happened has to be measured.</strong></p>
<h4>The line on the label is worth more than the indication is</h4>
<p>The Japanese package insert carries one requirement, and word for word it reads: this drug must be used together with a "neutron irradiation device approved for boron neutron capture therapy"<a href="https://www.kegg.jp/medicus-bin/japic_med?japic_code=00068760" target="_blank" rel="noopener"><sup class="cit">[5]</sup></a><a href="https://www.pmda.go.jp/files/000237990.pdf" target="_blank" rel="noopener"><sup class="cit">[6]</sup></a>.</p>
<p>Which means the approval does not come apart. It is not the drug being approved so that any machine will do, and it is not the machine being approved so that any boron drug will do. <strong>What was approved is that one combination.</strong> Keep it in mind for the sixteenth article, on how four jurisdictions regulate this, because most of the world does not yet have even half of that combination.</p>
""",
)

EN["pet"] = dict(
 title="First, do you take it up?",
 dek="The PET scan measures whether the boron reaches your tumour. It is one of the few genuinely personalised steps in BNCT, and it is the step that keeps people out.",
 lead="I have had patients finish this scan and be told they are not suitable. I will still say it: what that patient saved that day was more than he knew at the time.",
 body="""<p>Most self-paid treatments cannot tell you in advance whether they will do anything for you. BNCT can, or at least it can measure its own necessary condition.</p>

<h4>What is being measured</h4>
<p>BPA is labelled with fluorine-18, injected, and followed on a PET scanner to see where it goes. The number that comes out of it is the ratio of uptake in tumour to uptake in normal tissue, usually written T/N.</p>
<p>The threshold in common use is 2.5. This is not only a recommendation in the literature. In the recurrent head and neck cancer trial sponsored by Taipei Veterans General Hospital and delivered on the Tsing Hua reactor, a "T/N greater than 2.5 measured on PET with fluorine-18-labelled BPA" is written into the eligibility criteria in black and white<a href="https://ctv.veeva.com/study/boron-neutron-capture-therapy-bnct-for-locally-recurrent-head-and-neck-cancer" target="_blank" rel="noopener"><sup class="cit">[1]</sup></a>. The review by Barth and colleagues records the same practice: BNCT goes ahead only when the ratio exceeds 2.5<a href="https://doi.org/10.1186/1748-717X-7-146" target="_blank" rel="noopener"><sup class="cit">[2]</sup></a>.</p>
<h4>Clearing the threshold does not mean it will work</h4>
<p><strong>This ratio is a necessary condition, not a sufficient one.</strong> It measures whether the boron gets in, not whether the treatment does anything. Every patient in the brain tumour trial in the tenth article cleared this hurdle, and the imaging response rate was still only 3.7%. Between "I am eligible" and "this will help me" sits the whole of this set of articles.</p>

<h4>The rest of that trial's eligibility criteria carry more information than the threshold does</h4>
<p>The same registry record lists the other conditions<a href="https://ctv.veeva.com/study/boron-neutron-capture-therapy-bnct-for-locally-recurrent-head-and-neck-cancer" target="_blank" rel="noopener"><sup class="cit">[1]</sup></a>: a histologically confirmed, locally recurrent malignant tumour of the head and neck; conventional radiotherapy already received; and all three salvage routes, surgery, radiotherapy and chemotherapy, unsuitable; a lesion no more than twelve centimetres in its longest diameter; age eighteen to eighty; performance status above a set level.</p>
<p>Read those together and you can see the place BNCT was given inside the trial: <strong>not the better option, but the one left when the others have run out.</strong> No marketing sentence will ever contain that, and it is written into the eligibility criteria.</p>

<h4>Being ruled out is not bad news</h4>
<p>I know how that reads as consolation, so let me give it substance. If someone whose boron uptake is too low goes ahead with BNCT, this is what happens: the normal tissue still takes the three doses the neutrons bring with them (the second article), and the tumour does not get the boron share. <strong>The whole price paid, none of the benefit taken.</strong></p>
<p>So if the scan comes back unsuitable, what you have saved is not only money. It is your re-irradiation allowance, and a stretch of physical reserve. This is one of the few parts of the technology that is genuinely fair to the patient.</p>
<p>And how the person opposite you answers when you ask what happens if the ratio comes in under the threshold will tell you more about the place you are sitting in than the scan itself does.</p>
""",
)

EN["newagents"] = dict(
 title="Not one has reached a person",
 dek="Targeted boron drugs, liposomes, antibody conjugates: the laboratory has made all of them. This article is about the three gates between the laboratory and the ward.",
 lead="Everything in this article is preclinical research. I put it in because this is the box the news reports most often, and it is the furthest of all of them from anything you can be given.",
 body="""<p>The previous article said that clinical practice has only two boron drugs, and that both belong to a generation sixty years old. People are of course making new ones.</p>

<h4>As of today's search, not one of them</h4>
<p>Boron-cluster liposomes, antibody-conjugated boron carriers, peptide-conjugated boron carriers — all of them have done well in cells and in animals. <strong>But as things stand, I can find no record of any one of them entering a human trial.</strong> A 2024 review of the current state of clinical BNCT trials puts it plainly: the boron carriers used in every clinical trial are still BPA and/or BSH<a href="https://link.springer.com/article/10.1007/s12553-024-00862-7" target="_blank" rel="noopener"><sup class="cit">[1]</sup></a>. Another review, from 2026, calls them third-generation carriers and says their preclinical performance is promising but that they still face challenges in translation<a href="https://www.mdpi.com/2072-6694/18/3/498" target="_blank" rel="noopener"><sup class="cit">[2]</sup></a>.</p>
<p>So if you meet the claim that "a new-generation targeted boron drug has reached the clinic", it is worth going back and checking. There is one thing in this field that is easy to misread: trial listings contain borofalan(10B), and that is BPA itself; they also contain fluorine-18-labelled BPA, and that is the imaging agent from the fifth article, not a carrier used for treatment. <strong>Neither of them is a new-generation carrier.</strong></p>

<h4>Where it is stuck: a new carrier has three gates to pass</h4>
<p>The first gate is toxicology. A new carrier has no therapeutic effect of its own, so an early human trial can only assess safety with the drug given and no neutrons delivered<a href="https://link.springer.com/article/10.1007/s12553-024-00862-7" target="_blank" rel="noopener"><sup class="cit">[1]</sup></a>. That is a structural difficulty: there is no efficacy signal available to hold an early trial up.</p>
<p>The second gate is pharmacokinetics. The boron has to be inside the tumour, at a high enough concentration, during the stretch of time when the beam is on. Cleared too early will not do, metabolised away will not do, drifting into normal tissue will not do. That is much harder than whether a tumour cell will take the molecule up.</p>
<p>The third gate is whether the ratio reproduces. A beautiful tumour-to-normal-tissue ratio in an animal model frequently fails to hold when it moves into people. The fourth article gave the human <strong>tissue-to-blood</strong> boron concentration ratio for BPA as about 3.5, and a new carrier has to beat that order of magnitude in people, and reproduce it reliably, before it counts as a step forward.</p>

<h4>What this box means for a decision you make this year</h4>
<p>Put those three gates together and there is a conclusion a patient can use: <strong>every BNCT treatment option available today uses the boron drugs of sixty years ago.</strong> However new the machine, reactor or accelerator, that has not changed.</p>
<p>So when somebody offers "new-generation targeted boron drugs" as a reason to have BNCT now, the reason has come loose from the drug that would actually be injected into you. That order of magnitude of about 3.5 in the fourth article is the ceiling as it currently stands.</p>
<h4>How to read that breast cancer cell story</h4>
<p>There has been a report from Taiwan of research on HER2-targeted BNCT in breast cancer cells. Work of this kind is real and worth doing, and it stands in front of gate zero of the three above.</p>
<p>There is a cheap way to judge news of this sort: <strong>look at what the denominator is.</strong> A cell line, a mouse, or a person? If you cannot find people in the report, it has nothing to do with the treatment decision you are making this year. The research matters, of course. Its moment for mattering has not arrived.</p>
""",
)
