# -*- coding: utf-8 -*-
"""A 組：原理（B1-B3）。只引用 brief/A.md 標記 PASS 的來源。"""

R_BARTH05 = ('<li><p>Barth, R. F., Coderre, J. A., Vicente, M. G. H., &amp; Blue, T. E. (2005). '
             '<a href="https://aacrjournals.org/clincancerres/article/11/11/3987/290719/" target="_blank" rel="noopener">'
             'Boron neutron capture therapy of cancer: current status and future prospects</a>. '
             'Clinical Cancer Research, 11(11), 3987-4002. DOI: 10.1158/1078-0432.CCR-05-0035</p></li>')
R_TERRA = ('<li><p>Terranova, M. L. (2026). '
           '<a href="https://www.mdpi.com/2673-4362/7/1/6" target="_blank" rel="noopener">'
           'From source to target: the neutron pathway for the clinical translation of boron neutron capture</a>. '
           'Journal of Nuclear Engineering, 7(1), 6. DOI: 10.3390/jne7010006</p></li>')
R_CURRONC = ('<li><p>Jin, W. H., Seldon, C., Butkus, M., Sauerwein, W., &amp; Giap, H. B. (2022). '
             '<a href="https://www.mdpi.com/1718-7729/29/10/622" target="_blank" rel="noopener">'
             'Boron neutron capture therapy: clinical application and research progress</a>. '
             'Current Oncology, 29(10), 7868-7886. DOI: 10.3390/curroncol29100622</p></li>')
R_BARTH12 = ('<li><p>Barth, R. F., Vicente, M. G. H., Harling, O. K., et al. (2012). '
             '<a href="https://doi.org/10.1186/1748-717X-7-146" target="_blank" rel="noopener">'
             'Current status of boron neutron capture therapy of high grade gliomas and recurrent head and neck cancer</a>. '
             'Radiation Oncology, 7, 146. DOI: 10.1186/1748-717X-7-146</p></li>')
R_MIT = ('<li><p>Massachusetts Institute of Technology OpenCourseWare (2004). '
         '<a href="https://ocw.mit.edu/courses/22-55j-principles-of-radiation-interactions-fall-2004/382568947f61a0473afc13cbe688b3e4_bnct_lect_so4.pdf" target="_blank" rel="noopener">'
         'Boron neutron capture therapy (22.55J Principles of Radiation Interactions 講義)</a>. MIT OpenCourseWare.</p></li>')

C_BARTH05 = '<a href="https://aacrjournals.org/clincancerres/article/11/11/3987/290719/" target="_blank" rel="noopener"><sup class="cit">[%d]</sup></a>'
C_TERRA = '<a href="https://www.mdpi.com/2673-4362/7/1/6" target="_blank" rel="noopener"><sup class="cit">[%d]</sup></a>'
C_CURRONC = '<a href="https://www.mdpi.com/1718-7729/29/10/622" target="_blank" rel="noopener"><sup class="cit">[%d]</sup></a>'
C_BARTH12 = '<a href="https://doi.org/10.1186/1748-717X-7-146" target="_blank" rel="noopener"><sup class="cit">[%d]</sup></a>'
C_MIT = '<a href="https://ocw.mit.edu/courses/22-55j-principles-of-radiation-interactions-fall-2004/382568947f61a0473afc13cbe688b3e4_bnct_lect_so4.pdf" target="_blank" rel="noopener"><sup class="cit">[%d]</sup></a>'

DISPLACE_REIRR = ('<p>BNCT 幾乎都用在已經照過一次的地方。所以它排擠掉的還有一樣東西，'
                  '是別的自費治療不會動到的：<strong>再照射的額度</strong>。'
                  '同一個部位能承受的放射線總量有上限，用掉了不會回來。'
                  '這一筆額度該花在哪裡，值得比錢想得更久。</p>')

ART = {}

# ------------------------------------------------------------------ B1 ------
ART["principle"] = dict(
    section="BNCT：原理",
    kicker="BNCT: HOW IT WORKS",
    h1="殺傷範圍不到一顆細胞",
    dek="它的精準來自把殺傷半徑縮到比一顆細胞還小。強項和弱點都從這裡長出來。",
    lead="這一篇講的是 BNCT 唯一真正特別的地方。看完你會知道，為什麼這個技術的每一個問題，最後都會回到同一句話：硼跑到哪裡去了。",
    tags=["bnct", "evidence"],
    displace=DISPLACE_REIRR,
    body="""
<p>光子、質子、重粒子，瞄準的邏輯都是幾何的：算出腫瘤在哪裡，把射束對準它。BNCT 不走這條路，它把「準」這件事從幾何搬到了化學。</p>

<h4>反應本身：一個很大的靶</h4>
<p>硼-10 這個同位素有一個特別的性質：它捕獲低能量中子的機率非常高。這個機率在核物理裡用「截面」表示，單位是 barn，可以理解成「靶看起來有多大」。硼-10 對熱中子的截面約 3837 barn""" + (C_MIT % 1) + (C_TERRA % 2) + """——比人體常見的元素大上好幾個數量級。但要立刻補一句：人體裡的硼只有百萬分之幾，所以中子穿過組織的時候，絕大多數並沒有打在硼上，而是打在氫和氮上。那些反應的代價，第二篇會算給你看。</p>
<p>捕獲之後，硼-10 分裂成一顆 α 粒子和一顆鋰-7 原子核。約九成四的機率走基態路徑，釋出的總能量約 2.31 兆電子伏特；約百分之六走激發態路徑，總能量約 2.79 兆電子伏特，並多放出一顆 0.48 兆電子伏特的加馬射線""" + (C_CURRONC % 3) + """。</p>

<h4>能量花在多短的距離裡，才是重點</h4>
<p>這兩顆碎片帶著這些能量，在組織裡只跑五到九微米就停下來""" + (C_BARTH05 % 4) + """。這個距離大約就是一顆哺乳類細胞的大小""" + (C_TERRA % 2) + """。</p>
<p>把能量塞進這麼短的路徑，意思是單位長度上的能量沉積極高——放射生物學上叫高線性能量轉移。它造成的損傷是一段一段的，斷點彼此靠得很近，修復機制常常接不回來。</p>
<p>但真正該記住的是幾何後果：<strong>殺傷半徑小於一顆細胞的直徑。</strong>吃進硼的那顆細胞會被摧毀，隔壁沒吃進去的那顆，不會挨到硼這一份的傷害——<strong>但它照樣挨到中子帶來的另外三種劑量。所謂「殺傷半徑小於一顆細胞」講的是硼那一項，不是整個治療。</strong></p>

<h4>所以它的選擇性不是被計畫出來的，是被代謝決定的</h4>
<p>這是 BNCT 最漂亮的地方。它所有的麻煩也從這裡開始。放射治療計畫可以畫出等劑量線，你看得到射束打到哪裡；BNCT 的「等劑量線」畫在細胞層級，而且是由哪些細胞把硼吃進去決定的。</p>
<p>吃得多的地方效果好，吃得少的地方效果就沒有。腫瘤裡不是每一顆細胞的攝取都一樣；同一種癌症，不同人的攝取也不一樣。這不是理論上的疑慮，它是可以事前量的——量的方法是第五篇的正子攝影。</p>
<p><strong>機器能保證射束打在哪裡。硼跑到哪裡，機器保證不了</strong>——那要事先量，量完才知道你適不適合。</p>

<h4>一個順帶的提醒，關於怎麼讀這個領域的文獻</h4>
<p>寫這一篇的時候我本來想把 α 粒子和鋰-7 各自跑多遠分開寫。結果是查不下去：兩篇被廣泛引用的綜論給的射程互相對得起來，但它們標的線性能量轉移歸屬剛好相反；另一篇綜論給的 α 射程比其他來源大了一個數量級。連這種最基礎的數字都會抄錯。</p>
<p>所以這一組文章裡，凡是不同來源對不起來的數字，我一律只寫大家一致的那一層——這裡就是「合計五到九微米」。這個原則後面幾篇會反覆用到，因為 BNCT 是一個新聞稿比論文多的領域。</p>
""",
    refs=[R_MIT, R_TERRA, R_CURRONC, R_BARTH05],
)

# ------------------------------------------------------------------ B2 ------
ART["dose"] = dict(
    section="BNCT：原理",
    kicker="BNCT: HOW IT WORKS",
    h1="這個劑量不能拿去跟放療比",
    dek="同樣寫成幾 Gy，意思完全不同。這一篇教你看懂 BNCT 的劑量單位，以免被一個看起來很小的數字誤導。",
    lead="這一篇要教你一件很小的事：看到 BNCT 的劑量數字，先看單位後面有沒有 Eq 那兩個字母。有沒有那兩個字母，整句話的意思會差很多。",
    tags=["bnct", "evidence"],
    displace=DISPLACE_REIRR,
    body="""
<p>放射治療的劑量單位是格雷（Gy），意思單純：每公斤組織吸收多少能量。BNCT 的劑量報表看起來也是格雷，但它其實是一個換算後的數字，而且換算的過程裡有好幾個估計值。</p>

<h4>照一次中子，身體其實同時吃到四種劑量</h4>
<p>中子束打進組織以後，不會只發生硼的那個反應。至少有四件事同時在發生""" + (C_MIT % 1) + """：</p>
<p>第一，硼的劑量——就是第一篇講的那個反應，高線性能量轉移，只發生在有硼的地方。第二，氮的劑量——組織裡的氮-14 捕獲中子後放出一顆約 0.54 兆電子伏特的質子。第三，快中子的劑量——中子撞到氫原子核，把質子撞飛出去。第四，加馬射線的劑量——一部分來自組織裡的氫捕獲中子，一部分是射束本身帶進來的污染。</p>
<p>後面三種跟你有沒有吃硼無關。<strong>它們打在所有被中子穿過的組織上，包括正常組織。</strong>這是 BNCT 不能被說成「完全不傷正常組織」的物理理由。</p>

<h4>四種劑量的生物效應不一樣，所以要各自加權</h4>
<p>同樣的能量，用不同方式沉積，生物效應差很多。所以每一種成分要乘上一個係數再相加，得到的數字叫做「光子等效劑量」，寫成 Gy-Eq""" + (C_MIT % 1) + """。</p>
<p>硼那一項的係數叫 CBE，它不是一個常數——它隨組織而變。常被引用的一組數值是：腫瘤 3.8、皮膚 2.5、口腔黏膜 2.5、腦與脊髓 1.3。射束裡高線性能量轉移的成分另外用一個係數，一律 3.2——那一個不叫 CBE""" + (C_BARTH05 % 2) + (C_MIT % 1) + """。</p>
<p>看出問題了嗎：<strong>同樣一顆硼、同樣一束中子，算在腫瘤上和算在皮膚上，換算出來的劑量相差約一點五倍（3.8 比 2.5）。</strong>這些係數是從動物實驗和早期臨床推出來的，不是量出來的常數。</p>

<h4>那些係數是推出來的，不是量出來的</h4>
<p>CBE 從哪裡來？來自動物實驗與早期臨床的推算。它不是一個像密度、像半衰期那樣可以直接量的常數。同一份 MIT 的教材寫著，硼的生物效應因子在文獻上的範圍是從 1.3 到超過 5""" + (C_MIT % 1) + """——這個跨度很大，而且它會直接乘進最後那個數字裡。</p>
<p>實務上的後果是：<strong>兩個中心報出來的「20 Gy-Eq」，如果用的係數不同，代表的生物效應就不同。</strong>這不是說那些數字沒有意義，而是說它們是一組有前提的估計值，前提要跟著數字一起讀。</p>
<h4>所以那個數字不能拿來比，也不能拿來加</h4>
<p>兩個實務上的結論。</p>
<p>第一，<strong>Gy-Eq 和你以前做放療時的 Gy 不是同一個單位</strong>，不能互相比較。看到「BNCT 一次給了二十幾 Gy-Eq」，不要理解成「一次抵得上二十幾次的放療」。</p>
<p>第二，它也不能簡單地跟你先前照過的劑量相加。再照射的風險評估在 BNCT 這裡沒有一個乾淨的公式，它是臨床判斷，不是算術。這也是為什麼第十五篇的副作用那一段，不能只用「劑量看起來不高」來安慰自己。</p>
<p>下次有人給你一個 BNCT 的劑量數字，可以接著問一句：<strong>「這是 Gy-Eq 嗎？用的是哪一組 CBE？」</strong>問得出這句話，對方大概就知道你讀過東西了。</p>
""",
    refs=[R_MIT, R_BARTH05],
)

# ------------------------------------------------------------------ B3 ------
ART["depth"] = dict(
    section="BNCT：原理",
    kicker="BNCT: HOW IT WORKS",
    h1="中子走不到的地方",
    dek="BNCT 的適應症清單為什麼這麼短？多數理由不在生物學，在中子能鑽多深。",
    lead="病人問我最多的一句是「我這個癌症可不可以做 BNCT」。在講任何癌別之前，先講這一篇——因為大部分的答案在這裡就決定了。",
    tags=["bnct", "evidence", "decision"],
    displace=DISPLACE_REIRR,
    body="""
<p>硼吃得進去只是條件之一。中子還得打得到。</p>

<h4>從熱中子到超熱中子：為了多鑽幾公分</h4>
<p>最早的 BNCT 用的是熱中子束，也就是能量最低、最容易被硼捕獲的那一種。問題是它衰減得非常快：通量的峰值大約落在皮下兩到三公分，到了十公分深處，只剩下峰值的十分之一左右""" + (C_CURRONC % 1) + """。對腦瘤來說，這意味著要開顱才照得到。</p>
<p>後來的解法是改用能量稍高的超熱中子（大約 0.5 電子伏特到 10 千電子伏特之間""" + (C_BARTH05 % 2) + """）。它進入組織後會先被慢化成熱中子，等於把「熱中子的峰值」往深處推。這一步讓皮下大約六到八公分的腫瘤進入了可照射的範圍""" + (C_CURRONC % 1) + """。</p>

<h4>「照得到」和「划得來」是兩件事</h4>
<p>更有意義的說法不是深度幾公分，是治療比——腫瘤拿到的劑量相對於正常組織拿到的劑量。以腦部中線的腫瘤來說，在大約八公分深的位置，這個比值仍然大於一""" + (C_BARTH12 % 3) + """。再深下去，正常組織付出的代價開始追上腫瘤得到的好處。要說清楚的是，八公分是文獻上找得到最深的可引用數據點，不是一條被量出來的界線。</p>
<p>所以請把 BNCT 的可及範圍想成一個從皮膚往內遞減的區域，而不是一個「打得到／打不到」的開關。愈深，效果愈稀薄，正常組織的負擔愈重。</p>

<h4>皮膚的兩公分和腦部的八公分，不是同一件事</h4>
<p>同樣講深度，兩個數字的意思不一樣。皮膚病灶談的是「病灶本身在不在中子還強的那一層」；腦部談的是「射束穿過頭皮、顱骨、正常腦之後，到達腫瘤時還剩多少」。中間隔著的組織愈多、愈厚，衰減就愈多，而那些組織自己也在吃劑量。</p><p>所以不要把「有人在八公分深的腦瘤做過」推論成「我身上八公分深的東西也可以」。<strong>路徑上經過什麼，和終點有多深，一樣重要。</strong></p>
<h4>這解釋了那張很短的適應症清單</h4>
<p>把這個物理限制套上去，日本核准的適應症是頭頸部、有人體資料的是腦瘤與皮膚病灶，就不意外了：<strong>它們都在中子還有力氣的那幾公分裡。</strong></p>
<p>反過來，深部的器官不是「還沒研究到」，是中子在到達之前就衰減掉了。哪些器官因此被排除在外、有人怎麼試著繞過去，第十四篇一個一個講。</p>
<p>所以「能不能做」這個問題，很多時候不是醫師在決定，是幾公分在決定。如果有人告訴你 BNCT「哪裡都能打」，那句話跟這一篇的物理是牴觸的。</p>
""",
    refs=[R_CURRONC, R_BARTH05, R_BARTH12],
)
