# -*- coding: utf-8 -*-
"""D 組：各癌別實證（B9-B14）。只引用 brief/B.md、brief/C.md 標 PASS 的來源。"""
from articles_a import DISPLACE_REIRR

U = dict(
 JHN002="https://doi.org/10.1016/j.radonc.2020.11.001",
 JRR22="https://academic.oup.com/jrr/article/63/3/393/6564355",
 PMS="https://www.mdpi.com/2072-6694/16/5/869",
 TW18="https://link.springer.com/article/10.1186/s40880-018-0295-y",
 TW23="https://www.mdpi.com/2072-6694/15/10/2762",
 JG002="https://academic.oup.com/noa/article/3/1/vdab067/6279119",
 JO22506="https://academic.oup.com/jjco/article/42/10/887/814954",
 JG25="https://academic.oup.com/noa/article/7/Supplement_6/vdaf236.031/8380849",
 TSUKUBA="https://doi.org/10.1016/j.apradiso.2025.112152",
 MIYA09="https://link.springer.com/article/10.1007/s11060-008-9699-x",
 KAWA09="https://www.jstage.jst.go.jp/article/jrr/50/1/50_08043/_article",
 MIYA16="https://www.jstage.jst.go.jp/article/nmc/56/7/56_ra.2015-0297/_article",
 CELLS21="https://www.mdpi.com/2073-4409/10/11/2881",
 FRONT21="https://doi.org/10.3389/fonc.2021.601820",
 CC18="https://link.springer.com/article/10.1186/s40880-018-0297-9",
 MENIN="https://academic.oup.com/neuro-oncology/article/24/1/90/6275296",
 TAOR="https://www0.mi.infn.it/~gadioli/Varenna2006/Proceedings/Altieri_S.pdf",
 LUNG="https://link.springer.com/article/10.1007/s13691-012-0048-8",
 THORLIVER="https://thor.site.nthu.edu.tw/p/406-1192-302043,r11030.php?Lang=zh-tw",
 SUZ14="https://academic.oup.com/jrr/article/55/1/146/917082",
)
def C(k, n): return '<a href="%s" target="_blank" rel="noopener"><sup class="cit">[%d]</sup></a>' % (U[k], n)

R = {
 "JHN002": '<li><p>Hirose, K., Konno, A., Hiratsuka, J., et al. (2021). <a href="%s" target="_blank" rel="noopener">Boron neutron capture therapy using cyclotron-based epithermal neutron source and borofalan (10B) for recurrent or locally advanced head and neck cancer (JHN002): an open-label phase II trial</a>. Radiotherapy and Oncology, 155, 182-187. DOI: 10.1016/j.radonc.2020.11.001</p></li>' % U["JHN002"],
 "JRR22": '<li><p>Hirose, K., et al. (2022). <a href="%s" target="_blank" rel="noopener">Determining a methodology of dosimetric quality assurance and adverse-event profile for the JHN002 trial</a>. Journal of Radiation Research, 63(3), 393-401.</p></li>' % U["JRR22"],
 "PMS": '<li><p>Hirose, K., et al. (2024). <a href="%s" target="_blank" rel="noopener">Safety of boron neutron capture therapy with borofalan(10B) and its efficacy on recurrent head and neck cancer: real-world outcomes from nationwide post-marketing surveillance</a>. Cancers, 16(5), 869. DOI: 10.3390/cancers16050869</p></li>' % U["PMS"],
 "TW18": '<li><p>Wang, L. W., Liu, Y. W. H., Chou, F. I., &amp; Jiang, S. H. (2018). <a href="%s" target="_blank" rel="noopener">Clinical trials for treating recurrent head and neck cancer with boron neutron capture therapy using the Tsing-Hua Open Pool Reactor</a>. Cancer Communications, 38, 37. DOI: 10.1186/s40880-018-0295-y</p></li>' % U["TW18"],
 "TW23": '<li><p>Wang, L. W., Liu, Y. W. H., Chu, P. Y., et al. (2023). <a href="%s" target="_blank" rel="noopener">Boron neutron capture therapy followed by image-guided intensity-modulated radiotherapy for locally recurrent head and neck cancer: a prospective phase I/II trial</a>. Cancers, 15(10), 2762. DOI: 10.3390/cancers15102762</p></li>' % U["TW23"],
 "JG002": '<li><p>Kawabata, S., Suzuki, M., Hirose, K., et al. (2021). <a href="%s" target="_blank" rel="noopener">Accelerator-based BNCT for patients with recurrent glioblastoma: a multicenter phase II study</a>. Neuro-Oncology Advances, 3(1), vdab067. DOI: 10.1093/noajnl/vdab067</p></li>' % U["JG002"],
 "JO22506": '<li><p>Nagane, M., Nishikawa, R., Narita, Y., et al. (2012). <a href="%s" target="_blank" rel="noopener">Phase II study of single-agent bevacizumab in Japanese patients with recurrent malignant glioma</a>. Japanese Journal of Clinical Oncology, 42(10), 887-895. DOI: 10.1093/jjco/hys121</p></li>' % U["JO22506"],
 "JG25": '<li><p><a href="%s" target="_blank" rel="noopener">JG002 延長追蹤（會議摘要）</a>. Neuro-Oncology Advances (2025), 7(Suppl 6), vdaf236.031.（<strong>會議摘要，非期刊全文；作者與標題未逐字查證</strong>）</p></li>' % U["JG25"],
 "TSUKUBA": '<li><p>Nakai, K., Kumada, H., Matsumoto, Y., et al. (2025). <a href="%s" target="_blank" rel="noopener">Boron neutron capture therapy (BNCT) phase I clinical trial for newly diagnosed glioblastoma by newly developed accelerator at University of Tsukuba</a>. Applied Radiation and Isotopes, 226, 112152.（<strong>試驗計畫書，無療效結果</strong>）</p></li>' % U["TSUKUBA"],
 "MIYA09": '<li><p>Miyatake, S. I., Kawabata, S., Yokoyama, K., et al. (2009). <a href="%s" target="_blank" rel="noopener">Survival benefit of boron neutron capture therapy for recurrent malignant gliomas</a>. Journal of Neuro-Oncology, 91, 199-206. DOI: 10.1007/s11060-008-9699-x</p></li>' % U["MIYA09"],
 "KAWA09": '<li><p>Kawabata, S., Miyatake, S. I., Kuroiwa, T., et al. (2009). <a href="%s" target="_blank" rel="noopener">Boron neutron capture therapy for newly diagnosed glioblastoma</a>. Journal of Radiation Research, 50(1), 51-60. DOI: 10.1269/jrr.08043</p></li>' % U["KAWA09"],
 "MIYA16": '<li><p>Miyatake, S. I., Wanibuchi, M., Hu, N., &amp; Ono, K. (2016). <a href="%s" target="_blank" rel="noopener">Boron neutron capture therapy for malignant brain tumors</a>. Neurologia medico-chirurgica, 56(7), 361-371. DOI: 10.2176/nmc.ra.2015-0297</p></li>' % U["MIYA16"],
 "CELLS21": '<li><p>Hiratsuka, J., Kamitani, N., Tanaka, R., et al. (2021). <a href="%s" target="_blank" rel="noopener">Boron neutron capture therapy (BNCT) for cutaneous malignant melanoma using 10B-p-boronophenylalanine (BPA) with special reference to the radiobiological basis and clinical results</a>. Cells, 10(11), 2881. DOI: 10.3390/cells10112881</p></li>' % U["CELLS21"],
 "FRONT21": '<li><p>Malouff, T. D., Seneviratne, D. S., Ebner, D. K., et al. (2021). <a href="%s" target="_blank" rel="noopener">Boron neutron capture therapy: a review of clinical applications</a>. Frontiers in Oncology, 11, 601820. DOI: 10.3389/fonc.2021.601820</p></li>' % U["FRONT21"],
 "CC18": '<li><p>Hiratsuka, J., Kamitani, N., Tanaka, R., et al. (2018). <a href="%s" target="_blank" rel="noopener">Boron neutron capture therapy for vulvar melanoma and genital extramammary Paget disease with curative responses</a>. Cancer Communications, 38, 38. DOI: 10.1186/s40880-018-0297-9</p></li>' % U["CC18"],
 "MENIN": '<li><p>Miyatake, S. I., Kawabata, S., Hiramatsu, R., et al. (2022). <a href="%s" target="_blank" rel="noopener">Reactor-based boron neutron capture therapy for 44 cases of recurrent and refractory high-grade meningiomas with long-term follow-up</a>. Neuro-Oncology, 24(1), 90-98. DOI: 10.1093/neuonc/noab108</p></li>' % U["MENIN"],
 "TAOR": '<li><p>Altieri, S. (2006). <a href="%s" target="_blank" rel="noopener">Application of neutron capture therapy to widespread tumours</a>. Varenna 會議論文集。</p></li>' % U["TAOR"],
 "LUNG": '<li><p>Suzuki, M., Suzuki, O., Sakurai, Y., et al. (2012). <a href="%s" target="_blank" rel="noopener">Reirradiation for locally recurrent lung cancer in the chest wall with boron neutron capture therapy</a>. International Cancer Conference Journal, 1, 235-238. DOI: 10.1007/s13691-012-0048-8</p></li>' % U["LUNG"],
 "SUZ14": '<li><p>Suzuki, M., Kato, I., Aihara, T., et al. (2014). <a href="%s" target="_blank" rel="noopener">Boron neutron capture therapy outcomes for advanced or recurrent head and neck cancer</a>. Journal of Radiation Research, 55(1), 146-153. DOI: 10.1093/jrr/rrt098</p></li>' % U["SUZ14"],
 "THORLIVER": '<li><p>國立清華大學水池式反應器（THOR）。<a href="%s" target="_blank" rel="noopener">肝癌學術性臨床試驗-第 1 期</a>。查證時狀態為「申請中」。</p></li>' % U["THORLIVER"],
}

ART = {}

ART["headneck"] = dict(
    section="BNCT：各癌別的實證", kicker="BNCT: THE EVIDENCE",
    h1="唯一有藥證的那個適應症",
    dek="這是 BNCT 證據最強的一格。而所謂最強，是一個 21 人的單臂試驗——這一篇把那 21 人拆開給你看。",
    lead="日本的核准建立在這裡，台灣的試驗也集中在這裡。看完你會知道這一格的證據有多重，也會知道它有多輕。",
    tags=["bnct", "evidence", "trial"],
    displace=DISPLACE_REIRR,
    body="""
<p>先標清楚這一篇的證據層級：<strong>單臂第二期試驗，加上一份真實世界的上市後監測，沒有隨機分派。</strong></p>

<h4>日本的 JHN002：21 個人</h4>
<p>這個試驗是開放標籤、單臂、沒有對照組的第二期試驗""" + C("JHN002", 1) + """。收案 21 人，分兩群：復發鱗狀細胞癌 8 人，復發或局部晚期的非鱗狀細胞癌 13 人。用的是迴旋加速器的超熱中子束，硼藥是 borofalan（10B），劑量每公斤 400 毫克。</p>
<p>主要終點是客觀反應率，全體 71%。分開看：鱗癌那 8 人裡完全緩解 50%、部分緩解 25%；非鱗癌那 13 人裡完全緩解 8%、部分緩解 62%。兩年總存活率，鱗癌 58%、非鱗癌 100%。鱗癌的中位局部區域無惡化存活是 11.5 個月""" + C("JHN002", 1) + """。</p>
<p><strong>兩件事要說清楚。</strong>第一，「非鱗癌兩年存活 100%」的分母是 13 人——這個數字看起來很漂亮，但它的信賴區間會很寬，而摘要裡沒有給。第二，這個試驗<strong>沒有報告中位總存活</strong>，我查遍原文摘要、審查文件與後續次分析都沒有。所以任何寫著「JHN002 中位存活多少個月」的說法，來源都不是這個試驗。</p>

<h4>副作用不小</h4>
<p>脫髮 95%、高澱粉酶血症 86%、噁心 81%""" + C("JHN002", 1) + """。次分析裡的第三級以上事件：高澱粉酶血症 76%，其中第四級佔 71%""" + C("JRR22", 2) + """。</p>
<p>順帶一提，有些二手評論寫這個試驗「沒有第四級毒性」，那和次分析的數字對不起來。第十五篇會完整處理。</p>

<h4>真實世界的 162 人</h4>
<p>日本核准後做了全國性的上市後監測，162 位有完整安全性資料的病人，其中復發頭頸鱗癌 144 位""" + C("PMS", 3) + """。在那 144 位鱗癌病人裡，客觀反應率 72.3%（完全緩解 46.0%、部分緩解 26.3%），一年與兩年總存活率 78.8% 和 60.7%。</p>
<p><strong>這不是拿來驗算 71% 的。</strong>JHN002 的 71% 是鱗癌與非鱗癌 21 人合起來算的，兩個百分比的分母不是同一群人。這份監測真正的價值是：分母變大之後，在真實世界裡反應率仍在同一個量級。它不能取代對照組，也不能把 71% 變成一個被驗證過的數字。</p>

<h4>台灣的兩個試驗，數字不能混用</h4>
<p>清大反應器這邊做過兩個不同的試驗，常被當成同一個引用。</p>
<p>第一個是分兩次照射的試驗，17 人、23 個復發病灶，<strong>單臂、單中心、沒有對照組</strong>（期別在可查證的來源裡沒有標明，我就不補）。6 人完全緩解、6 人部分緩解；<strong>兩年局部區域控制率 28%，兩年總存活率 47%</strong>；中位追蹤 19.9 個月""" + C("TW18", 4) + """。</p>
<p>第二個是第一／二期試驗，單次 BNCT 之後接續影像導引強度調控放療，14 人收案、12 人完成（就是第七篇說已完成的那一個）。5 人完全緩解、4 人部分緩解；<strong>一年總存活 56%、一年局部無惡化存活 21%</strong>；中位追蹤 11.8 個月""" + C("TW23", 5) + """。<strong>這個試驗只報一年，沒有兩年數字</strong>——看到有人引用它的「兩年存活率」，那是誤引。</p>

<h4>把兩年存活 47% 讀對</h4>
<p>這一格的病人已經照過一次放療、復發了、手術和化療都不適用。台灣那個試驗（17 人，單臂，沒有對照組）兩年存活 47%；但同樣是 BNCT 治療晚期或復發頭頸癌，日本一份 62 人的前瞻系列報的是中位存活 10.1 個月、兩年 24.2%""" + C("SUZ14", 6) + """。</p>
<p><strong>兩個數字差了將近一倍，而兩邊都是單臂。</strong>這個落差本身就是示範：沒有對照組的時候，數字會隨著收了誰而大幅移動。所以站得住的說法不是「兩年還有一半的人在」，是<strong>「這一格有一部分人撐得過兩年，而撐得過的比例還沒有被可靠地量出來」</strong>。</p>
<p>但要同時記得：局部反應率講的是腫瘤縮小，兩年存活講的是人還在，這兩件事在這個族群裡的落差很大——台灣那個試驗的兩年局部控制率只有 28%，總存活卻是 47%。<strong>腫瘤最後多半還是回來了。</strong>這句話難聽，但它是把期待放在對的位置上的必要條件。</p>
""",
    refs=[R["JHN002"], R["JRR22"], R["PMS"], R["TW18"], R["TW23"], R["SUZ14"]],
)

ART["gbm"] = dict(
    section="BNCT：各癌別的實證", kicker="BNCT: THE EVIDENCE",
    h1="影像沒縮小，人卻活得比較久",
    dek="這個試驗的影像反應率只有 3.7%，同一批人的中位存活是 18.9 個月。兩個數字都是真的，也都沒有對照組——搞懂這件事，你就會讀這一整個領域的資料了。",
    lead="這是這一組最長也最重要的一篇。它談的表面上是腦瘤，實際上是「怎麼判斷一個沒有對照組的試驗」。學會這一套，你看任何自費療法的宣傳都不會再被同一招騙到。",
    tags=["bnct", "evidence", "trial", "decision"],
    displace=DISPLACE_REIRR,
    body="""
<p>證據層級要標兩層：<strong>試驗本身是單臂第二期；它的存活比較是拿歷史世代當對照。</strong>後面那一層才是這篇的主題。</p>

<h4>JG002 的數字</h4>
<p>日本的多中心、開放標籤、單臂第二期試驗，收 27 人，其中復發膠質母細胞瘤 24 人，2016 到 2018 年收案""" + C("JG002", 1) + """。用的是迴旋加速器超熱中子源，硼藥每公斤 500 毫克。主要終點是復發膠質母細胞瘤的一年存活率。</p>
<p>結果：<strong>一年存活率 79.2%（95% 信賴區間 57.0 到 90.8），中位總存活 18.9 個月。</strong></p>
<p>同一份報告裡還有另外兩個數字：<strong>依 RANO 判讀的影像反應率，全體 27 人裡只有 3.7%（一位部分緩解）；中位無惡化存活 0.9 個月。</strong></p>
<p>0.9 個月。也就是說，用影像看，幾乎所有人在一個月內就「惡化」了；但一年後有近八成的人還活著。</p>

<h4>第一件事：影像和存活可以脫鉤</h4>
<p>腦部照射後常出現一種現象，影像上看起來腫瘤變大、對比劑吃得更明顯，實際上是治療造成的發炎與血腦障壁變化，不是腫瘤長大。這叫假性惡化。RANO 這套判讀標準會把它讀成惡化。</p>
<p>所以在 BNCT 之後的頭幾個月，影像判讀的可信度是低的。<strong>0.9 個月的無惡化存活，主要反映的是判讀標準在這個情境下失真，不是治療在一個月內就失效了。</strong></p>
<p>這件事有實用意義：如果你或家人在做這一類治療，治療後第一次的影像報告寫「惡化」，不要立刻當成定局，要問醫師這是不是假性惡化、要不要再追一次。</p>

<h4>第二件事：那個 18.9 個月，是跟誰比的</h4>
<p>JG002 沒有對照組。所以作者拿了另一個試驗當比較對象：JO22506，一個 2012 年發表的單臂第二期試驗，用 bevacizumab 單藥治療復發惡性膠質瘤，收 31 人，中位總存活 10.5 個月""" + C("JO22506", 2) + """。18.9 對 10.5，看起來差很多。</p>
<p>作者自己說明了為什麼認為可以比：兩個試驗收的都是沒用過 bevacizumab 的復發膠質母細胞瘤，族群相似""" + C("JG002", 1) + """。這個說法有它的道理。但有三個地方要放在心上。</p>
<p>第一，年代。JO22506 發表於 2012 年，JG002 收案在 2016 到 2018 年。中間隔了好幾年，支持性照護、後線用藥、影像追蹤的密度都變了。同一種病在不同年代治療，存活本來就會往上飄一點。</p>
<p>第二，收案條件不完全一樣。JG002 的體能狀態門檻比 JO22506 寬一些，但它收到的腫瘤體積中位數只有 7.3 毫升——那是相當小的病灶。能被收進 BNCT 試驗的人，本來就是經過篩選、狀況比較好的一群。</p>
<p>第三，也是最重要的一點：<strong>JG002 的 27 人裡，有 21 人（78%）在疾病惡化之後接受了 bevacizumab</strong>，其中 5 人還加上 temozolomide""" + C("JG002", 1) + """。</p>
<p>把這件事講白：<strong>這個比較的實際內容是「BNCT 之後再接 bevacizumab」對上「bevacizumab 單藥」。</strong>兩組存活相減，得到的不是 BNCT 單獨的效果。這一點在原始論文裡寫得清清楚楚，卻幾乎不會出現在任何二手的介紹裡。</p>

<h4>第三件事：代價</h4>
<p>第三級以上的治療相關不良事件發生在 22 人身上，佔 81.5%""" + C("JG002", 1) + """。腦水腫 48.1%（第三級 11.1%）；脫髮 66.7%；澱粉酶上升 81.5%，其中第三級以上 66.7%、光是第四級就佔 48.1%。嚴重不良事件 33.3%。</p>
<p>這不是一個溫和的治療。任何把 BNCT 描述成「副作用很少的精準療法」的說法，都可以拿這一組數字去對照。</p>

<h4>2025 年的延長追蹤</h4>
<p>同一批病人後來有一份延長追蹤：一年存活率仍是 79.2%（信賴區間變窄，63.3 到 88.7），中位總存活 19.2 個月""" + C("JG25", 3) + """。</p>
<p>要注意這是會議摘要，不是期刊全文；期刊版本我查證時取不到。而且延長追蹤和原始報告的信賴區間不同，引用的時候要標明是哪一份。這種細節看起來瑣碎，但它正是分辨「讀過原文」和「抄了二手」的地方。</p>

<h4>所以這個治療到底有沒有用</h4>
<p>能站得住的說法只有一句：<strong>在一群經過篩選、腫瘤不大、能接受後線治療的復發膠質母細胞瘤病人身上，BNCT 後接續 bevacizumab 這個組合，看起來比單用 bevacizumab 的歷史世代活得久。</strong>這是這個資料能支撐的最強說法，一個字都不能再加。</p>
<p>它不是隨機試驗，所以我們不知道差距裡有多少來自 BNCT、多少來自篩選、多少來自年代。要回答那個問題需要隨機分派，而這個領域到現在還沒有做出來。</p>
<p>把這一篇的方法帶著走，下次看到任何療法宣稱「存活從 X 拉到 Y」，你有三個問題可以問：<strong>對照組是哪一年的？收案條件一不一樣？實驗組後來還做了什麼別的治療？</strong></p>
""",
    refs=[R["JG002"], R["JO22506"], R["JG25"]],
)

ART["newgbm"] = dict(
    section="BNCT：各癌別的實證", kicker="BNCT: THE EVIDENCE",
    h1="剛診斷就查到 BNCT 的家屬",
    dek="復發腦瘤有第二期資料，新診斷沒有。這兩者之間的距離，比多數人以為的遠。",
    lead="會問到這一篇的，通常是剛被診斷、家屬在網路上查到 BNCT 的人。所以我把話講得直接一點。",
    tags=["bnct", "evidence", "trial"],
    displace=DISPLACE_REIRR,
    body="""
<p>證據層級：<strong>第一期／劑量探索，且尚無療效結果發表。</strong></p>

<h4>目前最前緣在哪裡</h4>
<p>日本筑波大學有一個以自行開發的直線加速器執行的第一期試驗，對象是新診斷的膠質母細胞瘤，做法是 BNCT 加上體外放射治療加上 temozolomide""" + C("TSUKUBA", 1) + """。</p>
<p>但要看清楚它的設計：<strong>主要終點是劑量限制毒性的發生率</strong>，前三位病人正常腦的最大劑量設在一個保守的上限，目標收案 12 到 18 人。而且我查到的那篇論文<strong>是試驗計畫書，不是結果報告</strong>——它自己寫著「結果將於國際會議發表並投稿同儕審查期刊」。</p>
<p>換句話說，這個試驗現在要回答的問題是「這樣做會不會出事」，還沒有到「這樣做有沒有用」。</p>

<h4>這個試驗現在問的是「會不會出事」</h4>
<p>這一段值得單獨講，因為它適用於所有新療法。</p>
<p>第一期試驗的目的是找出安全的劑量與可接受的毒性範圍。它的收案人數很少，通常沒有對照組，而且<strong>設計上就不是為了證明療效</strong>。所以「某某癌症的 BNCT 第一期試驗正在進行」這句話，翻譯過來是：<strong>目前還不知道它有沒有用，正在確認它安不安全。</strong></p>
<p>新聞稿常把「已進入臨床試驗」寫成一個里程碑。它確實是，但那個里程碑的位置，離「可以當成治療選項」還有很長一段。</p>

<h4>反應器時代留下的舊資料</h4>
<p>2000 年代日本用研究用反應器做過新診斷膠質母細胞瘤的病例序列：21 人，2002 到 2006 年，同時用 BSH 和 BPA 兩種硼藥。前 10 人只做 BNCT，後 11 人在 BNCT 之後加上 20 到 30 格雷的體外放療。兩組合計的中位存活 15.6 個月；加了放療的那 11 人是 23.5 個月""" + C("KAWA09", 2) + """。</p>
<p>這個 23.5 不能拿去和今天的標準治療相比，理由有兩個。<strong>那 11 人不是隨機分到加強放療的</strong>——是先撐過 BNCT、狀況還可以的人才做得成，所以這個數字裡有一部分是「誰活得夠久」造成的。而且那份報告的院內對照組數字我查不到，<strong>連它自己那個比較都還原不了。</strong></p>
<p>這是一份回溯性、拿院內歷史對照比較的資料，不是隨機試驗。而且要注意主要的死亡型態：腦脊髓液播散與局部復發""" + C("KAWA09", 2) + """。<strong>BNCT 打的是照射範圍內的東西，它處理不了已經散出去的部分。</strong></p>

<h4>如果你家人剛被診斷</h4>
<p><strong>先給結論：對新診斷的膠質母細胞瘤，BNCT 目前不是一個治療選項。</strong>標準治療是手術、放療加上 temozolomide。這套治療的證據是隨機試驗等級的，而 BNCT 在這一格連第一期都還沒做完。</p>
<p>第一篇警語裡「排擠掉還沒用完的標準治療」講的就是這種情況。<strong>現在不是二選一的時候</strong>——標準治療該做的先做完，這條路上真的走到後面，第十篇講的那些資料才會變成跟你有關的東西。</p>
""",
    refs=[R["TSUKUBA"], R["KAWA09"]],
)

ART["melanoma"] = dict(
    section="BNCT：各癌別的實證", kicker="BNCT: THE EVIDENCE",
    h1="數字最好看的一格，人數也最少",
    dek="完全緩解率六成八，病例數三十幾。這兩個數字要一起看。",
    lead="這一篇是全組分母最小的一篇。我把它寫出來，是因為它剛好示範了「反應率很高」和「證據很強」是兩件事。",
    tags=["bnct", "evidence"],
    displace=DISPLACE_REIRR,
    body="""
<p>證據層級：<strong>病例系列。沒有對照組，分母是個位數到二十幾人。</strong></p>

<h4>為什麼是這兩個癌別</h4>
<p>回到第三篇的物理：中子走不深。皮膚上的病灶剛好落在中子最有力氣的那幾公分裡。再加上黑色素細胞對 BPA 的攝取不錯，這兩個條件湊在一起，皮膚病灶就成了 BNCT 最早的適應症之一。</p>

<h4>黑色素瘤的數字</h4>
<p>日本最早那一組，1987 到 2002 年間 22 人：完全緩解 68.2%（15 人）、部分緩解 23.0%（5 人）""" + C("CELLS21", 1) + """。存活那一欄要換一副眼鏡看：這份報告給的是「五年癌症專一存活率」——<strong>只把死於黑色素瘤的人算進分子，死於其他原因的不算，所以它一定比總存活高，也不等於治癒。</strong>在這個定義下，整體 58%、原發性病灶 74%。這份報告沒有給總存活，我也查不到。同一團隊後來 2003 到 2014 年又做了 8 人，6 人完全緩解，其中 5 人在治療後 5.6 到 8.2 年仍無病存活""" + C("CELLS21", 1) + """。</p>
<p>阿根廷用他們的研究反應器做了 7 人，對象是四肢多發性的皮膚轉移。他們報的反應率約七成，<strong>但那是「以病灶計」</strong>——一個人身上有幾十顆結節，算的是結節縮了幾顆，不是七成的病人有效。同一批資料另報約三成出現第三級的潰瘍（來源沒有寫明這個三成是以人計還是以病灶計）""" + C("CELLS21", 1) + C("FRONT21", 2) + """。（這一系列的原始論文我調不到，數字是由兩篇綜論交叉支持的。）美國麻省理工那邊做過 4 人""" + C("CELLS21", 1) + """。</p>
<p>把這些加起來，<strong>全世界公開發表的黑色素瘤 BNCT 人體資料，大概在三、四十例的量級</strong>，而且集中在皮膚與四肢的病灶。<strong>不是內臟轉移。</strong>這一點很重要——現在黑色素瘤真正改變存活的是免疫治療，那才是全身性疾病的答案。</p>

<h4>乳房外柏哲德氏症</h4>
<p>這是一種長在生殖器、肛門周圍的少見皮膚癌。日本那個系列裡有 3 位，全部在六個月內達到完全緩解；其中一位 3.2 年後死於心臟病但腫瘤沒有復發，另外兩位分別追蹤到 6.5 年與 6.9 年仍無復發""" + C("CC18", 3) + """。副作用主要是局部糜爛與排尿困難，第二級""" + C("FRONT21", 2) + """。</p>
<p>更早還有 2 位的報告，但我無法確認那 2 位和後來這 3 位是不是同一批人（同一個體系、時間區間又重疊）。<strong>所以我不把它們相加。</strong>誠實的說法是：已發表的 BNCT 治療這個病的病例，只有個位數。</p>

<h4>這種漂亮數字的三個扣分項</h4>
<p>完全緩解率七成、八成，這是任何癌症治療都會羨慕的數字。但這些報告沒有回答的是：同樣的病灶用別的方式治療會怎樣。而個位數到二十幾人的病例系列，本來就擋不住選擇性報告——做得好的容易被寫出來。更要緊的是它們報的是<strong>局部</strong>反應：那位外陰黑色素瘤的病人局部確實沒有復發，但 1.1 年後死於全身轉移""" + C("CC18", 3) + """。局部處理得好，不等於病被控制住。</p>
<p>它在皮膚上做得最好看，也正是在皮膚上，它把自己的本質露了出來：<strong>它只處理它照得到的地方。</strong></p>
""",
    refs=[R["CELLS21"], R["FRONT21"], R["CC18"]],
)

ART["meningioma"] = dict(
    section="BNCT：各癌別的實證", kicker="BNCT: THE EVIDENCE",
    h1="腦膜瘤：等不到的那個大型試驗",
    dek="高分級腦膜瘤復發後沒有標準答案。BNCT 在這裡有 44 人的資料——這一篇講它的份量，也講它的天花板。",
    lead="這一篇也適用於其他罕見癌症的病人：當你的病少到做不出隨機試驗，該怎麼看待手上僅有的證據。",
    tags=["bnct", "evidence"],
    displace=DISPLACE_REIRR,
    body="""
<p>證據層級：<strong>病例系列，44 人，無對照組。</strong>這已經是這個適應症目前最大的一份資料。</p>

<h4>44 人的數字</h4>
<p>日本的團隊整理了 44 位復發或頑固性高分級腦膜瘤的病人，其中 WHO 第二級 20 人（45.5%）、第三級 24 人（54.5%）""" + C("MENIN", 1) + """。</p>
<p>BNCT 之後的中位總存活 29.6 個月（95% 信賴區間 16.1 到 40.4）；分開看，第二級 44.4 個月、第三級 21.6 個月，差異有統計意義。中位無惡化存活 13.7 個月。36 位可評估影像反應的病人裡，完全緩解 6 位（16.7%）、部分緩解 17 位（47.2%）、疾病穩定 13 位（36.1%）——三個數字加起來剛好是 36，也就是沒有任何一位被判為疾病惡化。可評估者是怎麼被選出來的，這件事本身就值得留意""" + C("MENIN", 1) + """。</p>
<p>代價那一欄也要看：<strong>第二級放射性壞死 34.1%、第三級放射性壞死 13.6%——兩級相加接近一半</strong>""" + C("MENIN", 1) + """。這不是罕見併發症，是接近半數的人會遇到的事。</p>

<h4>那個 98.4 個月不是療效</h4>
<p>同一份報告裡還有一個「從診斷起算的中位存活 98.4 個月」。這個數字不能拿來當療效——它包含了病人在復發之前那幾年的病程，也反映了能活到需要考慮 BNCT 的人本來就走得比較久。<strong>要看療效，看的是 BNCT 之後的 29.6 個月。</strong></p>

<h4>反應器時代的其他腦瘤資料</h4>
<p>順帶把背景補齊。日本用研究用反應器治療惡性腦瘤的總量，2002 年 1 月到 2014 年 5 月之間是 167 例，涵蓋復發惡性膠質瘤、新診斷惡性膠質瘤與復發高分級腦膜瘤""" + C("MIYA16", 2) + """——<strong>但這 167 例各佔多少、各自活多久，那份報告沒有拆開，我也查不到。</strong></p>
<p>另外有一份較早的報告，是同一批研究者從 2002 年起累積的 22 位復發惡性膠質瘤病人，中位存活 10.8 個月，對照取自別人發表的歷史資料""" + C("MIYA09", 3) + """。<strong>兩份報告的病人有沒有重疊，從公開資料判斷不出來，所以不要把它們相加或相除。</strong></p>
<p>這些都是十幾二十年前、用反應器做的。它們是這個領域的起點，不是現在的證據基礎。</p>

<h4>罕見癌症的證據，為什麼會停在這裡</h4>
<p>高分級腦膜瘤本來就少，復發之後又更少。要做一個有統計效力的隨機試驗，需要的病人數在這種病上湊不出來，或者要花上十幾年。這不是研究者不努力，是分母不夠。</p>
<p>所以如果你的病屬於這一類，你要面對的現實是：<strong>不會有那個決定性的試驗。</strong>你要做的判斷，永遠得建立在病例系列和專家共識上。</p>
<p>在那種處境下，我會做的事情是這樣：把數字的分母和有沒有對照組先弄清楚，像上面那樣；把副作用的比率看得跟療效一樣重，這裡是三分之一以上的人會出現放射性壞死；然後優先考慮把自己放進正在進行的臨床試驗裡，那樣至少你的經驗會累積成下一個人的證據。</p>
""",
    refs=[R["MENIN"], R["MIYA16"], R["MIYA09"]],
)

ART["others"] = dict(
    section="BNCT：各癌別的實證", kicker="BNCT: THE EVIDENCE",
    h1="名單為什麼幾乎是空的",
    dek="這一篇沒有好消息。但它可能是這一組裡最多人需要讀的一篇——因為問「我這個癌症可以做嗎」的人，多半屬於這一格。",
    lead="問我「我這個癌症可以做嗎」的人，多半不是頭頸癌也不是腦瘤。這一篇是寫給他們的，而它沒有好消息。",
    tags=["bnct", "evidence", "decision"],
    displace=DISPLACE_REIRR,
    body="""
<p>證據層級：<strong>個案報告。深部器官這一塊沒有系列，更沒有試驗結果。</strong></p>

<h4>先回到第三篇的那條線</h4>
<p>超熱中子在組織裡愈走愈弱。肝、肺、胰臟、深部骨盆腔——這些器官的位置，中子到不了，或者到得了但正常組織付出的代價已經超過腫瘤得到的好處。</p>
<p>所以這一塊空著的原因不是缺人研究，是<strong>研究過，然後被物理擋下來了</strong>。</p>

<h4>肝臟：有人真的試過繞過去</h4>
<p>2001 年和 2003 年，義大利的團隊各做了一位病人""" + C("TAOR", 1) + """。對象是大腸直腸癌的瀰漫性肝轉移、無法手術切除。</p>
<p>做法是這樣的：先注射硼藥，然後<strong>把整個肝臟從體內取出</strong>，洗掉血液，裝進袋子運到反應器旁邊照射約十分鐘，再運回手術室植回去。取出的肝臟量到的硼濃度，腫瘤約每百萬分之 45、正常肝約 8，比值超過 5。</p>
<p>結果：第一位病人存活 44 個月，生活品質不錯，最後死於腸道腫瘤的瀰漫性復發。<strong>第二位病人出現血管併發症，BNCT 後第 31 天再次手術，第 33 天因猝發心衰竭死亡。</strong></p>
<p>兩個人。一個活了將近四年，一個一個多月就走了。我把這件事寫出來，是因為它有時候會被引用成「BNCT 也能治肝癌」。<strong>需要把肝臟拿出來體外照射才能做到的事，本身就說明了限制有多硬。</strong></p>

<h4>台灣的肝癌試驗，現在在哪一格</h4>
<p>清大有一個肝癌的學術性臨床試驗，但我查證的時候，官方頁面上的狀態是<strong>「申請中」——還沒有通過審查、還沒有開始收案</strong>，目標收案 10 位可評估病人""" + C("THORLIVER", 2) + """。</p>
<p>這一點要特別講，因為 2024 年曾有「全球首例」的新聞出現。那則新聞講的是這個計畫，而不是已經完成的治療。<strong>一個試驗在申請中，和一個治療可以用，是兩件事。</strong>如果你或家人被介紹「去清大做肝癌 BNCT」，這是你要確認的第一件事。</p>

<h4>肺與胸膜</h4>
<p>日本有一則個案報告：一位 62 歲男性，左胸壁的復發肺腺癌，先前已經開過刀、照過 60 格雷。BNCT 分兩次做。七個月時正子攝影的攝取值從 22.1 降到 7.1、腫瘤大部分消退；<strong>但第八個月在照野邊緣再度復發</strong>，接著又做了一次強度調控放療""" + C("LUNG", 3) + """。</p>
<p>一位病人。反應是真的，復發也是真的。</p>
<p>至於惡性胸膜間皮瘤——有綜論提到曾經治療過瀰漫性胸膜腫瘤的病例，但我追不到可以引用的原始報告。所以我的寫法是：<strong>查無可確證的人體治療報告。</strong>不是說一定沒有，是說我拿不出來。</p>

<h4>所以，如果你的癌症在這一格</h4>
<p><strong>目前沒有資料支持 BNCT 用在深部器官。</strong>就是這樣。如果有人向你提議，這幾個問題值得問出口：這個病有多少人做過、發表在哪裡、我的腫瘤離皮膚幾公分、在那個深度腫瘤拿到的劑量相對正常組織是多少。</p>
<p>問到最後一題通常就結束了。這不是壞事——把時間和體力留給真的有機會的選項，本身就是一個治療決定。</p>
""",
    refs=[R["TAOR"], R["THORLIVER"], R["LUNG"]],
)
