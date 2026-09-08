# -*- coding: utf-8 -*-
"""E 組：現實面（B15-B17）。只引用 brief 標 PASS 的來源。"""
from articles_a import DISPLACE_REIRR

U = dict(
 SUZ14="https://academic.oup.com/jrr/article/55/1/146/917082",
 PMS="https://www.mdpi.com/2072-6694/16/5/869",
 JG002="https://academic.oup.com/noa/article/3/1/vdab067/6279119",
 FRONT21="https://doi.org/10.3389/fonc.2021.601820",
 MENIN="https://academic.oup.com/neuro-oncology/article/24/1/90/6275296",
 KEGG="https://www.kegg.jp/medicus-bin/japic_med?japic_code=00068760",
 NIKKEI="https://medical.nikkeibp.co.jp/leaf/all/series/drug/update/202006/566060.html",
 SHI="https://www.shi.co.jp/english/info/2019/6kgpsq0000002ji0.html",
 TAE="https://www.businesswire.com/news/home/20250925542671/en/",
 ISNCT="https://isnct.net/bnct-clinical-centers/",
 RAY="https://www.raysearchlabs.com/media/press-releases/2025/raystation-used-for-pioneering-clinical-milestone-at-helsinki-university-hospital--first-treatment-with-accelerator-based-bnct-in-europe/",
 MOHW="https://www.mohw.gov.tw/cp-3161-26718-1.html",
 NTHU="https://www.nthu.edu.tw/hotNews/content/1141",
 THORLIST="https://thor.site.nthu.edu.tw/p/403-1192-11030-1.php?Lang=zh-tw",
 NCT="https://ctv.veeva.com/study/boron-neutron-capture-therapy-bnct-for-locally-recurrent-head-and-neck-cancer",
)
def C(k, n): return '<a href="%s" target="_blank" rel="noopener"><sup class="cit">[%d]</sup></a>' % (U[k], n)

R = {
 "SUZ14": '<li><p>Suzuki, M., Kato, I., Aihara, T., et al. (2014). <a href="%s" target="_blank" rel="noopener">Boron neutron capture therapy outcomes for advanced or recurrent head and neck cancer</a>. Journal of Radiation Research, 55(1), 146-153. DOI: 10.1093/jrr/rrt098</p></li>' % U["SUZ14"],
 "PMS": '<li><p>Hirose, K., et al. (2024). <a href="%s" target="_blank" rel="noopener">Safety of boron neutron capture therapy with borofalan(10B) and its efficacy on recurrent head and neck cancer: real-world outcomes from nationwide post-marketing surveillance</a>. Cancers, 16(5), 869. DOI: 10.3390/cancers16050869</p></li>' % U["PMS"],
 "JG002": '<li><p>Kawabata, S., Suzuki, M., Hirose, K., et al. (2021). <a href="%s" target="_blank" rel="noopener">Accelerator-based BNCT for patients with recurrent glioblastoma: a multicenter phase II study</a>. Neuro-Oncology Advances, 3(1), vdab067. DOI: 10.1093/noajnl/vdab067</p></li>' % U["JG002"],
 "FRONT21": '<li><p>Malouff, T. D., Seneviratne, D. S., Ebner, D. K., et al. (2021). <a href="%s" target="_blank" rel="noopener">Boron neutron capture therapy: a review of clinical applications</a>. Frontiers in Oncology, 11, 601820. DOI: 10.3389/fonc.2021.601820</p></li>' % U["FRONT21"],
 "MENIN": '<li><p>Miyatake, S. I., Kawabata, S., Hiramatsu, R., et al. (2022). <a href="%s" target="_blank" rel="noopener">Reactor-based boron neutron capture therapy for 44 cases of recurrent and refractory high-grade meningiomas with long-term follow-up</a>. Neuro-Oncology, 24(1), 90-98. DOI: 10.1093/neuonc/noab108</p></li>' % U["MENIN"],
 "KEGG": '<li><p>KEGG／JAPIC 醫療用醫薬品資料庫。<a href="%s" target="_blank" rel="noopener">ステボロニン点滴静注バッグ9000mg／300mL（ボロファラン（10B））</a>。ステラファーマ株式会社。</p></li>' % U["KEGG"],
 "NIKKEI": '<li><p>日経メディカル（2020）。<a href="%s" target="_blank" rel="noopener">頭頸部癌の治療に世界初の BNCT 用ホウ素薬剤</a>。薬価基準収載・発売日 2020 年 5 月 20 日。</p></li>' % U["NIKKEI"],
 "SHI": '<li><p>Sumitomo Heavy Industries, Ltd. (2020). <a href="%s" target="_blank" rel="noopener">Obtains medical device approval for accelerator based BNCT system and the dose calculation program in Japan</a>. 企業新聞稿，核准日 2020 年 3 月 12 日。</p></li>' % U["SHI"],
 "TAE": '<li><p>TAE Life Sciences / University of Wisconsin-Madison (2025). <a href="%s" target="_blank" rel="noopener">Bringing boron neutron capture therapy to the United States</a>. 企業新聞稿，2025 年 9 月 25 日。</p></li>' % U["TAE"],
 "ISNCT": '<li><p>International Society for Neutron Capture Therapy. <a href="%s" target="_blank" rel="noopener">BNCT clinical centres</a>. 學會網頁，查證日 2026 年 9 月 8 日。</p></li>' % U["ISNCT"],
 "RAY": '<li><p>RaySearch Laboratories (2025). <a href="%s" target="_blank" rel="noopener">First treatment with accelerator-based BNCT in Europe, Helsinki University Hospital</a>. 企業新聞稿，2025 年 6 月 16 日。</p></li>' % U["RAY"],
 "MOHW": '<li><p>衛生福利部（2010）。<a href="%s" target="_blank" rel="noopener">關於硼中子捕獲治療設備之說明</a>。2010 年 3 月 23 日發布（<strong>此為 2010 年的立場，引用須標年份</strong>）。</p></li>' % U["MOHW"],
 "NTHU": '<li><p>國立清華大學（2023）。<a href="%s" target="_blank" rel="noopener">清華 BNCT 獲醫材許可證</a>。首頁故事，2023 年 8 月 16 日。</p></li>' % U["NTHU"],
 "THORLIST": '<li><p>國立清華大學水池式反應器（THOR）。<a href="%s" target="_blank" rel="noopener">BNCT 治療現況</a>。（BNCT 相關數據屬 THOR 所有）</p></li>' % U["THORLIST"],
 "NCT": '<li><p>Taipei Veterans General Hospital. <a href="%s" target="_blank" rel="noopener">Boron neutron capture therapy (BNCT) for locally recurrent head and neck cancer (NCT01173172)</a>. 臨床試驗登錄資料（鏡像頁）。</p></li>' % U["NCT"],
}

ART = {}

ART["safety"] = dict(
    section="BNCT：現實面", kicker="BNCT: THE REALITY",
    h1="副作用不是比較少，是不一樣",
    dek="「殺傷範圍只有一個細胞」不等於「不傷正常組織」。這一篇把已發表的不良事件攤開，包括最嚴重的那一個。",
    lead="這是這一組我最希望你讀完的一篇。BNCT 的行銷語言裡幾乎不會出現這些數字，但它們全部來自支持這個療法的試驗自己。",
    tags=["bnct", "evidence", "decision"],
    displace=DISPLACE_REIRR,
    body="""
<p>先把物理講回來。第二篇說過，中子打進組織，同時產生四種劑量，其中三種跟你有沒有吃硼無關。<strong>那三種打在所有被中子穿過的組織上。</strong>所以「殺傷半徑小於一個細胞」講的是硼那一項，不是整個治療。</p>

<h4>常見的那些</h4>
<p>日本核准後的全國上市後監測，162 位病人的資料""" + C("PMS", 1) + """：高澱粉酶血症 84.0%、口腔黏膜炎 51.2%、唾液腺炎 50.6%、脫髮 49.4%。晚期的部分：吞嚥困難 4.5%、口渴 2.6%、皮膚障礙 1.9%。（這份資料沒有分級，所以上面是總發生率。）</p>
<p>澱粉酶那一項值得解釋一下：BPA 會被唾液腺攝取，所以唾液腺跟著吃到劑量。這也是口乾與唾液腺炎的來源。<strong>它不是意外，是這個藥的分布決定的。</strong></p>
<p>腦部治療的樣子完全不同：主要是腦水腫與放射性壞死，不是黏膜炎和唾液腺炎。那個復發膠質母細胞瘤試驗裡，將近半數的人出現腦水腫，第三級以上的不良事件超過八成，實際比率在第十篇""" + C("JG002", 2) + """。腦膜瘤那個 44 人的系列，第二級與第三級放射性壞死相加接近一半，數字在第十三篇""" + C("MENIN", 3) + """。</p>

<h4>最嚴重的那一個：頸動脈破裂</h4>
<p>這一段請慢慢看。</p>
<p>日本一份 62 人的前瞻系列裡，<strong>3 位病人發生頸動脈出血，其中 2 位死於感染性的頸動脈破裂</strong>，1 位靠手術救回來。發生率 4.8%""" + C("SUZ14", 4) + """。同一份報告裡治療相關死亡共 3 例。</p>
<p>關鍵在下一句：<strong>這 3 位病人都是腫瘤侵犯到頸動脈、而且先前已經接受過再照射的人</strong>""" + C("SUZ14", 4) + """。另一份 33 人的系列也報告過 2 例，發生在治療後一到三個月"""+ C("FRONT21", 5) + """——不過這一筆我只在一篇綜論的轉述裡看到，原始報告調不到，所以請把它當旁證，不是可以拿去算比率的數字。</p>
<p>而前面那份 162 人的上市後監測，明確寫著<strong>沒有遇到頸動脈破裂</strong>""" + C("PMS", 1) + """。</p>
<p>這兩個數字看起來矛盾，其實不是。它們告訴你的是：<strong>這個風險不是平均分布在所有病人身上的，它高度集中在特定的一群人——腫瘤包住頸動脈、而且那個地方已經照過的人。</strong>所以問「BNCT 的頸動脈破裂機率是多少」這個問題本身就問錯了，該問的是「我是不是那一群人」。</p>

<h4>再照射的額度</h4>
<p>所以警語裡那筆額度，在這一篇有具體的長相：超過了就是壞死、潰瘍、大血管破裂這一類的事。</p>
<p>第二篇說過，BNCT 的 Gy-Eq 沒辦法乾淨地加到你先前的劑量上。所以再照射的判斷在這裡不是算術，是臨床判斷——而且是需要一位熟悉你先前放療範圍的醫師來做的判斷。<strong>如果評估你的人手上沒有你先前的放療計畫，那個評估是不完整的。</strong></p>

<h4>我在查證時撞到的一個矛盾</h4>
<p>整理這一篇的時候我遇到一件事，值得記下來。有一份針對日本那個核准試驗的評論寫著「沒有第四級或第五級毒性」，但同一個試驗的不良事件次分析裡，第四級高澱粉酶血症佔了七成（數字與出處在第九篇）。兩邊對不起來——最可能的解釋是評論指的是「有症狀的」事件，但它沒有這樣寫。</p>
<p>所以看到「沒有嚴重副作用」這種說法，值得回頭找原始報告。我查過的每一次，原始論文都比介紹它的文章寫得更難聽。這件事有它的道理：<strong>論文要通過審查，介紹不用。</strong></p>
""",
    refs=[R["PMS"], R["JG002"], R["MENIN"], R["SUZ14"], R["FRONT21"]],
)

ART["approval"] = dict(
    section="BNCT：現實面", kicker="BNCT: THE REALITY",
    h1="同一個技術，四種身分",
    dek="核准、給付、有效，是三件不同的事。這一篇把 BNCT 放進那張地圖裡，每一格都標了查證日期。",
    lead="這是這個專題的固定動作：任何新技術都要問它在哪裡是什麼身分。BNCT 的答案特別清楚，因為全世界只有一個地方核准了它。",
    tags=["bnct", "regulation", "nhi", "cost"],
    displace=DISPLACE_REIRR,
    body="""
<p>本篇所有法規狀態的查證日期是 2026 年 9 月 8 日。法規變動快，看到這篇的時候請重新確認。</p>

<h4>日本：唯一核准，而且是藥加機器一起核准</h4>
<p>硼藥 borofalan（10B）的製造販賣承認是 2020 年 3 月 25 日，藥證持有者是一家日本藥廠""" + C("KEGG", 1) + """。核准的適應症逐字是：<strong>「切除不能な局所進行又は局所再発の頭頸部癌」</strong>——不可切除的局部進行或局部復發頭頸部癌。<strong>就這一個適應症。</strong>不是「頭頸癌」，是「不可切除的局部進行或局部復發」的頭頸癌。</p>
<p>同一份仿單規定，本藥必須與經核准的中子照射裝置併用""" + C("KEGG", 1) + """。那個裝置在 2020 年 3 月 12 日取得醫療器材核准""" + C("SHI", 2) + """。</p>
<p>給付方面，這個藥在 2020 年 5 月 20 日納入薬価基準並上市""" + C("NIKKEI", 3) + """。<strong>藥證、器材證、給付，日本三樣都有了，而且只給一個適應症。</strong>這在全世界是唯一的。</p>

<h4>美國：查無核准</h4>
<p>我查不到任何取得美國食品藥物管理局核准的 BNCT 藥品或器材。</p>
<p>比較有說服力的旁證是這個：2025 年 9 月，一家美國廠商與威斯康辛大學麥迪遜分校宣布要讓該校成為<strong>「美國第一個」</strong>裝設其加速器型 BNCT 系統並執行<strong>「第一批臨床試驗」</strong>的場域，新聞稿裡明文寫著該系統與新型硼藥「僅供研究用途，不供販售」""" + C("TAE", 4) + """。國際學會列出的現行 BNCT 治療中心名單裡，也沒有美國""" + C("ISNCT", 5) + """。</p>
<p>用詞我要精確一點：這是「<strong>查無</strong>核准」，不是「確認未核准」——我無法直接查詢該國的器材與藥品資料庫。</p>

<h4>歐盟：試驗階段，而且才剛開始</h4>
<p>歐洲的第一例加速器型 BNCT 治療發生在 2025 年 6 月，赫爾辛基大學醫院。那幾位病人是<strong>一個進行中臨床試驗的收案者</strong>，適應症是不可切除、局部復發的頭頸癌""" + C("RAY", 6) + """。</p>
<p>歐洲藥品管理局那一側我查不到可以引用的紀錄，所以我不寫「已核准」也不寫「未核准」。<strong>能確定的是：歐洲目前是試驗，不是常規治療。</strong></p>

<h4>台灣：器材有證，藥沒有證，治療靠兩條路</h4>
<p>台灣這一欄最容易被誤讀，值得拆成三句話。</p>
<p>一、器材有證。「清大中子放射照射系統」在 2023 年 6 月取得衛福部醫療器材許可證""" + C("NTHU", 7) + """。</p>
<p>二、器材有證不等於治療被核准。器材許可講的是設備本身可以合法使用，它沒有回答「以 BNCT 治療某某癌症」是不是一個被核准的適應症。而在藥的那一側——日本核准的是藥加機器的組合——我查不到台灣有任何 BNCT 硼藥的藥證。</p>
<p>三、那病人現在是怎麼被治療的。兩條路：學術性臨床試驗，以及官方頁面稱為「緊急治療」的專案途徑""" + C("THORLIST", 8) + """。它不是健保給付項目。官方頁面沒有寫明這條專案途徑在法規上的確切類別，我也查不到可以引用的正式條文，所以不替它命名。</p>
<p>順帶一提歷史：2010 年衛生署曾公開表示，當時只同意該設備用於執行藥品臨床試驗，尚未核准用於常規放射治療業務""" + C("MOHW", 9) + """。那是十六年前的立場，中間顯然有變化，但我要標明年份，因為這是這一格唯一找得到的官方文字。</p>

<h4>把三件事分開</h4>
<p><strong>核准是法規說了算，給付是財務說了算，有效只有證據說了算。</strong>BNCT 在日本三樣都有，只是那個「有效」的欄位裡，裝的是一個 21 人的單臂試驗。在台灣是器材有證、治療走專案；在歐美是試驗。</p>
<p>而「有效」那一格——第九篇到第十四篇講的就是它，答案是：一個適應症有單臂第二期資料，其他都是病例系列或更少。</p>
""",
    refs=[R["KEGG"], R["SHI"], R["NIKKEI"], R["TAE"], R["ISNCT"], R["RAY"], R["NTHU"], R["THORLIST"], R["MOHW"]],
)

ART["who"] = dict(
    section="BNCT：現實面", kicker="BNCT: THE REALITY",
    h1="我該不該去問 BNCT：四個先決條件",
    dek="這一篇把前面十六篇收成一張檢查表。四個條件不是全部符合就該做，是有一個不符合就不必往下走。",
    lead="寫這個專題最實際的目的就是這一篇。如果你只讀一篇，讀這篇；但如果四個條件裡有一個不清楚，請回去讀對應的那一篇。",
    tags=["bnct", "decision", "cost"],
    displace=DISPLACE_REIRR,
    body="""
<p>這四題我在門診會照順序問。第一題答不上來，後面三題就不必問了。</p>

<h4>條件一：標準治療走完了嗎</h4>
<p>所有 BNCT 的人體資料，收的都是標準治療用盡或不適用的病人。台灣那個復發頭頸癌試驗的收案條件寫得最直白：必須已經接受過常規放射治療，而且手術、放療、化療三條救援路線<strong>都不適用</strong>""" + C("NCT", 1) + """。</p>
<p>所以如果標準治療還有選項沒用，這個問題現在不成立。這不是保守，是那些數字本來就是在那個位置上產生的——把它挪到前面來用，等於用一組不適用的資料在做決定。</p>

<h4>條件二：位置夠淺嗎</h4>
<p>中子走不深（第三篇）。腦部中線大約八公分的深度是文獻上還撐得住治療比的極限，再深下去正常組織的代價開始超過腫瘤的好處。</p>
<p>可以問的具體問題：<strong>「我的腫瘤離皮膚表面幾公分？在那個深度，腫瘤拿到的劑量相對正常組織是多少？」</strong>如果對方答不出來，或是給你一個「都可以打」的答案，那就是答案了。</p>

<h4>條件三：硼進得去嗎</h4>
<p>用氟-18 標記 BPA 的正子攝影量腫瘤和正常組織的攝取比值，常用門檻是 2.5""" + C("NCT", 1) + """（第五篇）。</p>
<p>這一步是可以事前做的，而且應該事前做。<strong>攝取不夠的人去照中子，會拿到全部的代價和幾乎沒有的好處。</strong>被判定不適合，省下的是錢、體力，還有下一個條件講的那個東西。</p>

<h4>條件四：再照射的風險，你和醫師都算過了嗎</h4>
<p>這是四個條件裡最容易被跳過的。BNCT 的病人幾乎都照過一次，而同一個部位能承受的總劑量有上限。第十五篇那份 62 人的系列裡，有 3 位發生頸動脈出血（其中 2 位死於感染性破裂）——<strong>而這 3 位全部是腫瘤侵犯頸動脈、那個部位又已經照過一次的人。所以要問的不是「機率是多少」，是「我是不是那一群人」。</strong></p>
<p>這一題沒有標準答案，只有「有沒有人真的坐下來算過」。要問的是：<strong>「我先前的放療範圍和劑量，你看過嗎？」</strong>對方拿不出你上一次的劑量分布，這題就還沒開始。</p>

<h4>四個都符合之後，還有一件事</h4>
<p>就算四個條件都過了，還是要回到警語一：<strong>做了這個，我放棄掉什麼。</strong></p>
<p>對走到後線的人，這個療程佔掉的是一段體力、一段時間、一筆錢，以及一次再照射的機會。這幾樣東西同時也是後線自費藥物、或參加臨床試驗會用到的。我不會替你排順序——但在簽字之前，把總額問到一個確切的數字，再把同一段時間、同一筆錢的另外兩三種用法寫下來比一次。</p>

<h4>帶去門診的三個問題</h4>
<p>如果你只記三句話，記這三句：</p>
<p><strong>「我的標準治療真的走完了嗎，還是還有沒用的？」</strong></p>
<p><strong>「要先做正子攝影量硼的攝取嗎？比值不到門檻的話你們的建議是什麼？」</strong></p>
<p><strong>「以我先前照過的範圍，這次再照的風險你怎麼評估？」</strong></p>
<p>後面兩題不是刁難，是最省時間的分辨方式。<strong>答得出來的人，通常也答得出你不適合的理由。</strong></p>
""",
    refs=[R["NCT"]],
)
