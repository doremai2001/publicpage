# -*- coding: utf-8 -*-
"""B 組：硼藥物（B4-B6）與 C 組：機器（B7-B8）。只引用 brief 標 PASS 的來源。"""
from articles_a import DISPLACE_REIRR, R_BARTH05, R_BARTH12, C_BARTH05, C_BARTH12

def _li(txt, url):
    return '<li><p>%s</p></li>' % txt.replace('@@', '<a href="%s" target="_blank" rel="noopener">' % url).replace('##', '</a>')

def _c(url):
    return '<a href="%s" target="_blank" rel="noopener"><sup class="cit">%%d</sup></a>'.replace('%%d', '<!--N-->') and \
           '<a href="%s" target="_blank" rel="noopener"><sup class="cit">[%%d]</sup></a>' % url

U_KONDO = "https://doi.org/10.3390/pharmaceutics14051106"
U_ISNCT = "https://isnct.net/bnct-boron-compounds/"
U_LAIRD = "https://doi.org/10.1039/D2NA00839D"
U_KEGG = "https://www.kegg.jp/medicus-bin/japic_med?japic_code=00068760"
U_PMDA = "https://www.pmda.go.jp/files/000237990.pdf"
U_NCT = "https://ctv.veeva.com/study/boron-neutron-capture-therapy-bnct-for-locally-recurrent-head-and-neck-cancer"
U_KARI = "https://link.springer.com/article/10.1007/s12553-024-00862-7"
U_ZHENGD = "https://www.mdpi.com/2072-6694/18/3/498"
U_SHI = "https://www.shi.co.jp/english/info/2019/6kgpsq0000002ji0.html"
U_RAY = "https://www.raysearchlabs.com/media/press-releases/2025/raystation-used-for-pioneering-clinical-milestone-at-helsinki-university-hospital--first-treatment-with-accelerator-based-bnct-in-europe/"
U_THOR_LIST = "https://thor.site.nthu.edu.tw/p/403-1192-11030-1.php?Lang=zh-tw"
U_THOR_EMG = "https://thor.site.nthu.edu.tw/p/406-1192-278370,r11030.php?Lang=zh-tw"
U_THOR_HN2 = "https://thor.site.nthu.edu.tw/p/406-1192-278368,r11030.php?Lang=zh-tw"
U_THOR_BRAIN = "https://thor.site.nthu.edu.tw/p/406-1192-278369,r11030.php?Lang=zh-tw"
U_NTHU_LIC = "https://www.nthu.edu.tw/hotNews/content/1141"
U_ISNCT_TW = "https://isnct.net/clinical-centres-in-taiwan/"

C = lambda u, n: '<a href="%s" target="_blank" rel="noopener"><sup class="cit">[%d]</sup></a>' % (u, n)

R = {
 U_KONDO: '<li><p>Kondo, N., Hirano, F., &amp; Temma, T. (2022). <a href="%s" target="_blank" rel="noopener">Evaluation of 3-borono-L-phenylalanine as a water-soluble boron neutron capture therapy agent</a>. Pharmaceutics, 14(5), 1106. DOI: 10.3390/pharmaceutics14051106</p></li>' % U_KONDO,
 U_ISNCT: '<li><p>International Society for Neutron Capture Therapy. <a href="%s" target="_blank" rel="noopener">BNCT: boron compounds</a>. ISNCT 學會網頁（非同儕審查來源）。</p></li>' % U_ISNCT,
 U_LAIRD: '<li><p>Laird, M., Komatsu, A., Matsumoto, K., et al. (2023). <a href="%s" target="_blank" rel="noopener">Organosilica nanoparticles containing sodium borocaptate (BSH) provide new prospects for boron neutron capture therapy (BNCT)</a>. Nanoscale Advances, 5, 2537-2546. DOI: 10.1039/D2NA00839D</p></li>' % U_LAIRD,
 U_KEGG: '<li><p>KEGG／JAPIC 醫療用醫薬品資料庫。<a href="%s" target="_blank" rel="noopener">ステボロニン点滴静注バッグ9000mg／300mL（ボロファラン（10B））</a>。ステラファーマ株式会社。</p></li>' % U_KEGG,
 U_PMDA: '<li><p>Pharmaceuticals and Medical Devices Agency, Japan. <a href="%s" target="_blank" rel="noopener">Report on the deliberation results: Steboronine 9000 mg/300 mL for infusion</a>. PMDA 審議結果報告書。</p></li>' % U_PMDA,
 U_NCT: '<li><p>Taipei Veterans General Hospital. <a href="%s" target="_blank" rel="noopener">Boron neutron capture therapy (BNCT) for locally recurrent head and neck cancer (NCT01173172)</a>. 臨床試驗登錄資料（鏡像頁）。</p></li>' % U_NCT,
 U_KARI: '<li><p>Karihtala, P. (2024). <a href="%s" target="_blank" rel="noopener">The current status and future perspectives of clinical boron neutron capture therapy trials</a>. Health and Technology. DOI: 10.1007/s12553-024-00862-7</p></li>' % U_KARI,
 U_ZHENGD: '<li><p>Zheng, D., Han, G., Lemus, O. D. M., et al. (2026). <a href="%s" target="_blank" rel="noopener">Boron neutron capture therapy: a technology-driven renaissance</a>. Cancers, 18(3), 498. DOI: 10.3390/cancers18030498</p></li>' % U_ZHENGD,
 U_SHI: '<li><p>Sumitomo Heavy Industries, Ltd. (2020). <a href="%s" target="_blank" rel="noopener">Obtains medical device approval for manufacturing and sales of accelerator based BNCT system and the dose calculation program in Japan</a>. 企業新聞稿。</p></li>' % U_SHI,
 U_RAY: '<li><p>RaySearch Laboratories (2025). <a href="%s" target="_blank" rel="noopener">RayStation used for pioneering clinical milestone at Helsinki University Hospital — first treatment with accelerator-based BNCT in Europe</a>. 企業新聞稿，2025 年 6 月 16 日。</p></li>' % U_RAY,
 U_THOR_LIST: '<li><p>國立清華大學水池式反應器（THOR）。<a href="%s" target="_blank" rel="noopener">BNCT 治療現況</a>。（BNCT 相關數據屬 THOR 所有）</p></li>' % U_THOR_LIST,
 U_THOR_EMG: '<li><p>國立清華大學水池式反應器（THOR）。<a href="%s" target="_blank" rel="noopener">緊急治療</a>。統計至 2026 年 8 月 28 日。（BNCT 相關數據屬 THOR 所有）</p></li>' % U_THOR_EMG,
 U_THOR_HN2: '<li><p>國立清華大學水池式反應器（THOR）。<a href="%s" target="_blank" rel="noopener">頭頸癌學術性臨床試驗-第 2 期</a>。（BNCT 相關數據屬 THOR 所有）</p></li>' % U_THOR_HN2,
 U_THOR_BRAIN: '<li><p>國立清華大學水池式反應器（THOR）。<a href="%s" target="_blank" rel="noopener">腦瘤臨床試驗-第 1 期</a>。統計至 2026 年 8 月 19 日。（BNCT 相關數據屬 THOR 所有）</p></li>' % U_THOR_BRAIN,
 U_ISNCT_TW: '<li><p>International Society for Neutron Capture Therapy. <a href="%s" target="_blank" rel="noopener">BNCT clinical centres in Taiwan</a>. 學會網頁，查證日 2026 年 9 月 8 日。</p></li>' % U_ISNCT_TW,
 U_NTHU_LIC: '<li><p>國立清華大學（2023）。<a href="%s" target="_blank" rel="noopener">清華 BNCT 獲醫材許可證</a>。首頁故事，2023 年 8 月 16 日。</p></li>' % U_NTHU_LIC,
}

ART = {}

ART["drugs"] = dict(
    section="BNCT：硼藥物", kicker="BNCT: THE BORON DRUGS",
    h1="真正決定成敗的另外一半",
    dek="日本核准的不是一台機器，是藥加機器的組合。這一篇講那個藥——以及為什麼六十年來能用的只有兩種。",
    lead="六十年來，真正打進人體的硼藥只有兩種。這件事本身就是這一篇要解釋的謎。",
    tags=["bnct", "evidence", "regulation"],
    displace=DISPLACE_REIRR,
    body="""
<p>第一篇說過，BNCT 的選擇性住在硼的分布裡。那個分布是藥決定的。從 1960 年代到今天，真正用在人身上的硼藥只有兩種。</p>

<h4>BPA：借用癌細胞的胃口</h4>
<p>BPA 的全名是硼苯丙胺酸，它長得像一種胺基酸。癌細胞為了長得快，會大量表現一種叫 LAT1 的胺基酸轉運蛋白，而 BPA 就搭這班車進去""" + C(U_KONDO, 1) + C(U_ISNCT, 2) + """。這是一個借力的設計：不是硼認得癌細胞，是癌細胞的胃口把硼吃進去。</p>
<p>它有個很實際的麻煩：BPA 幾乎不溶於水（每公升約 0.6 到 0.7 公克），所以臨床上要先跟果糖之類的糖形成複合物才能打進血管""" + C(U_KONDO, 1) + """。這不是化學上的小細節——同一篇文獻提到，溶解不完全的 BPA 可能在尿中結晶，造成血尿。</p>
<p>那它到底累積得多不多？早期臨床量到的<strong>組織對血液</strong>硼濃度比是：腫瘤約 3.5、皮膚約 1.5、正常腦約 1.0""" + C_BARTH12 % 3 + """。<strong>請注意這個比的分母是血液，不是正常組織</strong>——正文列的「正常腦 1.0」就是證明，若分母是正常組織，這個數字不會有意義。第五篇要講的 T/N 門檻 2.5 才是腫瘤對正常組織的比，兩個數字不能互換。請把量級記住：不是三十倍，不是一百倍。BNCT 的選擇性是真的，但它大概就是這樣的量級。</p>

<h4>BSH：靠的是門壞了</h4>
<p>另一種是 BSH，巰基十一氫十二硼酸鈉。它不走轉運蛋白，細胞其實不太吃它""" + C(U_LAIRD, 4) + """。它能用在腦瘤，靠的是腫瘤處的血腦障壁已經被破壞——藥漏得進去，而正常腦組織那一側的門還關著""" + C(U_ISNCT, 2) + """。</p>
<p>兩種藥的法規身分差很多。2020 年日本核准的是 BPA（藥品名 borofalan（10B））；<strong>BSH 至今沒有取得任何藥品核准，仍然只用在臨床試驗裡</strong>""" + C(U_LAIRD, 4) + """。所以看到「日本已核准 BNCT」的說法時，準確的版本是：核准了一個藥、一台機器，以及一個適應症。</p>

<h4>兩種藥都沒有解決的那件事</h4>
<p>BPA 靠癌細胞的胃口、BSH 靠門壞了，兩條路徑的共同點是：<strong>它們都不是為了 BNCT 設計的分子，是被發現剛好可以用。</strong>所以硼會不會進去、進去多少、待多久，很大程度上不受控制——它取決於這顆腫瘤的代謝和血管長什麼樣子。</p><p>這也是為什麼下一篇那個檢查非做不可。<strong>藥不能保證選擇性，只能提供選擇性的機會；有沒有真的發生，要量了才知道。</strong></p>
<h4>藥證上寫的那一句，比適應症本身更值得看</h4>
<p>日本的仿單裡有一條規定，逐字是這樣寫的：本藥必須與「經核准用於硼中子捕獲療法的中子照射裝置」併用""" + C(U_KEGG, 5) + C(U_PMDA, 6) + """。</p>
<p>意思是這個核准不能拆開。不是「這個藥被核准了，配哪台機器都行」，也不是「這台機器被核准了，配哪種硼藥都行」。<strong>被核准的是那一個組合。</strong>把這件事放在心上，第十六篇談各國法規身分的時候會用到——因為世界上大部分地方連這個組合的一半都還沒有。</p>
""",
    refs=[R[U_KONDO], R[U_ISNCT], R_BARTH12, R[U_LAIRD], R[U_KEGG], R[U_PMDA]],
)

ART["pet"] = dict(
    section="BNCT：硼藥物", kicker="BNCT: THE BORON DRUGS",
    h1="治療之前，先看你吃不吃得進去",
    dek="正子攝影量的是硼會不會跑到你的腫瘤裡。它是 BNCT 少數真正個人化的一步，也是把人擋在門外的那一步。",
    lead="有病人做完這個檢查，被告知不適合。我還是要說：那一天他省下的東西，比他當時知道的多。",
    tags=["bnct", "decision", "trial"],
    displace=DISPLACE_REIRR,
    body="""
<p>大部分自費療法沒辦法事先告訴你「這對你有沒有用」。BNCT 可以，至少可以量出它的必要條件。</p>

<h4>量的是什麼</h4>
<p>做法是把 BPA 標上氟-18，打進去，用正子攝影看它跑到哪裡。得到的關鍵數字是腫瘤和正常組織的攝取比值，一般寫成 T/N。</p>
<p>常用的門檻是 2.5。這不是文獻上的建議而已——在台北榮總主持、以清大反應器執行的那個復發頭頸癌試驗裡，「以氟-18 標記 BPA 的正子攝影測得 T/N 大於 2.5」是白紙黑字的收案條件""" + C(U_NCT, 1) + """。Barth 等人的綜論也記載同樣的做法：比值超過 2.5 才啟動 BNCT""" + C_BARTH12 % 2 + """。</p>
<h4>過了門檻，不代表會有效</h4>
<p><strong>這個比值是必要條件，不是充分條件。</strong>它量的是硼進不進得去，不是治療有沒有效。第十篇那個腦瘤試驗的病人全部通過了這一關，全體 27 人的影像反應率仍然只有 3.7%。「我可以做」和「這對我有用」中間，還隔著這一整組文章。</p>

<h4>那個試驗的收案條件，比門檻本身更有資訊</h4>
<p>同一份登錄資料裡還列著其他條件""" + C(U_NCT, 1) + """：必須是組織學確認的局部復發頭頸部惡性腫瘤；必須已經接受過常規放射治療；而且手術、放療、化療三條救援路線都不適用；病灶最大徑不超過十二公分；年齡十八到八十歲；體能狀態在一定水準以上。</p>
<p>把這幾條連起來讀，你會看到 BNCT 在臨床試驗裡被放的位置：<strong>不是「比較好的選擇」，是「其他選擇都沒有了」。</strong>這一點在任何行銷語言裡都不會出現，但它就寫在收案條件裡。</p>

<h4>被判定不適合，不是壞消息</h4>
<p>我知道這句話聽起來像安慰，但它有實質意義。硼攝取不夠的人去做 BNCT，會發生的事情是：正常組織照樣吃到中子帶來的那三種劑量（第二篇），腫瘤卻沒有拿到硼的那一份。<strong>代價全付，好處沒拿。</strong></p>
<p>所以檢查結果如果是不適合，你省下的不只是錢，還有再照射的額度和一段體力。這是這個技術少數對病人很公道的設計。</p>
<p>而對方聽到「比值不到門檻怎麼辦」時怎麼回答，比檢查本身更能告訴你這是什麼樣的單位。</p>
""",
    refs=[R[U_NCT], R_BARTH12],
)

ART["newagents"] = dict(
    section="BNCT：硼藥物", kicker="BNCT: THE BORON DRUGS",
    h1="新一代硼藥，還沒有一個進到人身上",
    dek="標靶硼藥、脂質體、抗體偶聯——實驗室裡都做出來了。這一篇講的是實驗室到病房之間那三道關卡。",
    lead="這一篇全篇都是臨床前的研究。我把它放進來，是因為新聞最常出現的就是這一格，而它離你能用到的東西最遠。",
    tags=["bnct", "evidence"],
    displace=DISPLACE_REIRR,
    body="""
<p>前一篇說臨床上只有兩種硼藥，而且都是六十年前那一代的東西。當然有人在做新的。</p>

<h4>查到今天，一個都沒有</h4>
<p>硼簇脂質體、抗體偶聯的硼載體、胜肽偶聯的硼載體——這些在細胞和動物身上都有不錯的成績。<strong>但截至目前，我查不到任何一個進入人體試驗。</strong>2024 年一篇整理臨床 BNCT 試驗現況的綜論寫得很清楚：所有臨床試驗使用的硼載體，都還是 BPA 和／或 BSH""" + C(U_KARI, 1) + """。2026 年的另一篇綜論用「第三代載體」稱呼它們，並說它們的臨床前表現有前景，但仍面臨轉譯上的挑戰""" + C(U_ZHENGD, 2) + """。</p>
<p>所以如果你看到「新一代標靶硼藥已進入臨床」這種說法，值得回頭確認一次。這個領域有一個很容易誤讀的地方：試驗清單上會出現 borofalan（10B）——那就是 BPA 本身；也會出現氟-18 標記的 BPA——那是第五篇講的顯影劑，不是治療用的載體。<strong>兩個都不是新一代載體。</strong></p>

<h4>為什麼卡住：新載體要過三關</h4>
<p>第一關是毒理。新載體本身沒有治療效果，所以早期的人體試驗只能在「打了藥但不照中子」的情況下做安全性評估""" + C(U_KARI, 1) + """。這是一個結構性的難處：你沒辦法用療效訊號去支撐一個早期試驗。</p>
<p>第二關是藥物動力學。硼要在照射的那一段時間裡、待在腫瘤裡、濃度夠高。太早排掉不行，代謝掉不行，跑進正常組織也不行。這比「腫瘤細胞會不會吃」難得多。</p>
<p>第三關是那個比值複製得出來嗎。動物模型上做出很漂亮的腫瘤／正常組織比，換到人身上常常不成立。第四篇提到 BPA 在人體的<strong>組織／血液</strong>硼濃度比大約 3.5——新載體要在人身上超過這個量級並且穩定重現，才算真的往前走了一步。</p>

<h4>對你今年的決定，這一格意味著什麼</h4>
<p>把上面三關連起來，可以得到一個對病人有用的結論：<strong>今天任何一個 BNCT 的治療選項，用的都是六十年前那一代的硼藥。</strong>不管機器多新、不管是反應器還是加速器，這一點都沒有變。</p>
<p>所以當有人用「新一代標靶硼藥」當作理由，說服你現在就做 BNCT，那個理由和你實際會被打進去的藥是脫節的。第四篇那個大約 3.5 的量級，就是目前的天花板。</p>
<h4>那則乳癌細胞的新聞，怎麼讀</h4>
<p>台灣有過一則以 HER2 為標靶、在乳癌細胞上做 BNCT 的研究報導。這一類研究是真的、也值得做，但它站在上面那三關的第零關前面。</p>
<p>判斷這類消息有一個很省力的方法：<strong>看它的分母是什麼。</strong>是細胞株、是小鼠、還是人？如果報導裡找不到人，那它跟你今年的治療決定沒有關係。研究當然重要。只是它重要的時間點還沒到。</p>
""",
    refs=[R[U_KARI], R[U_ZHENGD]],
)

ART["thor"] = dict(
    section="BNCT：機器", kicker="BNCT: THE MACHINES",
    h1="台灣的中子源在校園裡，不在醫院裡",
    dek="它是一座研究用反應器，不是醫院裡的治療機。這個差別決定了台灣現在能走的兩條路各自長什麼樣子。",
    lead="這是這一組唯一寫台灣現況的文章。我把官方頁面上查得到的數字整理在這裡，包括那些容易被誤讀的。",
    tags=["bnct", "regulation", "cost", "trial"],
    displace=DISPLACE_REIRR,
    body="""
<p>台灣的 BNCT 中子源是國立清華大學的水池式反應器，簡稱 THOR。它在校園裡，不在醫院裡；病人是被送過去照射，照完再回醫院。</p>

<h4>兩條路，性質完全不同</h4>
<p>第一條是學術性臨床試驗。目前官方頁面上列著的有""" + C(U_THOR_LIST, 1) + """：頭頸癌第一期（2026 年 1 月開始，統計到 2026 年 8 月為止收了 2 位，預計 16 人次）；腦瘤第一期（2024 年 1 月開始，收了 17 位，預計 55 人次）""" + C(U_THOR_BRAIN, 2) + """；肝癌第一期則<strong>還在申請中、尚未開始收案</strong>。另外有一個頭頸癌第二期已經完成（14 人，2014 到 2021 年）""" + C(U_THOR_HN2, 3) + """。</p>
<p>第二條是官方頁面稱為「緊急治療」的專案途徑，由合作醫院的醫師評估、轉介。自 2017 年 1 月起累計 629 人次，其中腦瘤 402、頭頸癌 207、其他 20""" + C(U_THOR_EMG, 4) + """。那 20 人次的「其他」，官方頁面列的是肝癌、黑色素瘤與乳癌。</p>
<p>這裡要接一句很重要的話：<strong>一個癌別出現在這份統計裡，不代表那個癌別有證據支持。</strong>專案途徑處理的是個案的急迫性，不是療效的判斷。第十四篇會說明，深部器官的人體資料目前只有個位數的個案報告。走這條路之前，第三篇的深度問題和第十七篇的四個條件一樣要先問完。</p>

<h4>同一個病人做兩次，算兩次</h4>
<p>這個區別重要到值得單獨一段。官方頁面用的單位是<strong>人次</strong>——同一個病人做兩次就算兩次。一份國際學會的整理則用「病人數」寫成接近 500 人""" + C(U_ISNCT_TW, 5) + """。兩個數字單位不同，不能互相驗算，也不能拿其中一個去除另一個算出什麼比率。</p>
<p>同樣的道理適用於偶爾被引用的緩解率：那是跨癌別、以人次計的專案治療統計，不是前瞻試驗的療效。<strong>它和第九、第十篇要講的那些試驗數字，不是同一種東西。</strong></p>

<h4>2023 年拿到的那張證，是哪一種證</h4>
<p>2023 年 6 月，「清大中子放射照射系統」取得衛福部的醫療器材許可證""" + C(U_NTHU_LIC, 6) + """。這件事常被寫成「BNCT 在台灣核准了」，那是兩回事。</p>
<p><strong>這張證是器材的證，不是治療的證，也不是藥的證。</strong>三者的差別第十六篇整篇在講，那裡也會說明這條專案途徑在法規上為什麼連個名字都很難給。</p>

<h4>關於費用，要問的不是公告上那個數字</h4>
<p>THOR 有公告的收費辦法，但那份公告涵蓋的是<strong>反應器端的照射服務</strong>：射束品質保證、反應器運轉、治療計畫、擺位、血中硼濃度分析、劑量監測、照後體表輻射量測。</p>
<p>硼藥、住院、往返、以及合作醫院端的診療費用，都不在那份公告裡。所以真正該問到的是整趟走完的總額，不是公告上的單一數字。它不是健保項目，也不是掛號就排得到的常規自費項目。</p>
""",
    refs=[R[U_THOR_LIST], R[U_THOR_BRAIN], R[U_THOR_HN2], R[U_THOR_EMG], R[U_ISNCT_TW], R[U_NTHU_LIC]],
)

ART["accelerator"] = dict(
    section="BNCT：機器", kicker="BNCT: THE MACHINES",
    h1="加速器換掉了反應器，換不掉的是什麼",
    dek="不用核子反應器也能產生中子，這是 BNCT 這十年最大的改變。但改變的是可近性，不是療效。",
    lead="加速器型 BNCT 常被講成「新一代」。它確實是關鍵的一步，只是那一步邁的方向和多數人以為的不一樣。",
    tags=["bnct", "evidence", "regulation"],
    displace=DISPLACE_REIRR,
    body="""
<p>BNCT 卡了幾十年，最硬的一道門檻不是生物學，是中子從哪裡來。核子反應器蓋在醫院裡不現實，於是這個療法一直被綁在研究機構旁邊。</p>

<h4>做法：拿質子去撞鈹靶</h4>
<p>加速器型的原理是把質子加速到一定能量，打在鈹之類的靶材上，撞出中子，再經過慢化器整形成適合治療的超熱中子束。</p>
<p>2020 年 3 月，日本厚生勞動省核准了住友重機械的一套加速器型 BNCT 系統與它的劑量計算程式，號稱是全球第一個取得醫療器材身分的 BNCT 系統""" + C(U_SHI, 1) + """。那套系統用的是 30 兆電子伏特的質子迴旋加速器加鈹靶。</p>
<p>這台就是第四篇說的「那個裝置」——藥證和器材證是同一組核准的兩半。</p>

<h4>換掉反應器，換到的是什麼</h4>
<p>換到的是三樣東西：<strong>可近性、建置門檻、排程。</strong>加速器可以蓋在醫院院區裡，不需要核子反應器那一整套管制與運轉條件。這對一個療法能不能長大是決定性的。</p>
<p>但它沒有改變的東西更多。硼還是那個硼，選擇性的量級沒有變（第四篇）；中子在組織裡的衰減沒有變，深度限制一模一樣（第三篇）；四種劑量成分還是四種（第二篇）。<strong>「加速器型」不是療效的形容詞，是取得中子的方式。</strong>看到宣傳把「加速器」和「更好」放在同一句話裡，那是兩件事被接在一起了。</p>

<h4>同樣叫「加速器型」，機器之間仍然不一樣</h4>
<p>已經在治療病人的加速器，質子能量從幾個兆電子伏特到三十兆電子伏特都有，靶材與慢化器設計也不同。這些差異會反映在射束的能譜、劑量率與可照射的深度上——也就是第三篇那條衰減曲線的形狀。</p><p>對病人來說麻煩的是：<strong>這些規格幾乎問不到，也沒有一個跨機型的公開比較。</strong>所以「加速器型」四個字本身不構成任何療效訊息。真正該問的還是回到第三篇與第五篇那兩題：我的病灶在那個深度拿得到多少劑量、硼進不進得去。</p>
<h4>目前世界上走到哪裡</h4>
<p>日本是唯一把藥和機器都核准、並納入給付的地方。歐洲的第一例發生在 2025 年 6 月的赫爾辛基""" + C(U_RAY, 2) + """——那是試驗，不是常規治療。法規細節在第十六篇。</p>
<p>日本筑波大學另有一條直線加速器的路線，用 8 兆電子伏特的質子，目前在做新診斷膠質母細胞瘤的第一期試驗。<strong>該試驗的論文是試驗計畫書，還沒有報告任何療效結果</strong>，目標收案 12 到 18 人（第十一篇會再談）。</p>
<p>這一段的重點是時間感：<strong>把中子搬進醫院這件事，全世界也才剛開始幾年。</strong>加速器讓更多醫院蓋得起這台機器。它沒有讓任何一篇論文的數字變好看。</p>
""",
    refs=[R[U_SHI], R[U_RAY]],
)
