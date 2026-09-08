# -*- coding: utf-8 -*-
"""BNCT 分組的六張自繪圖（中英 × 桌機/手機 = 24 檔）。

沿用熱治療那一組的房屋樣式：米色漸層底、金色 kicker、襯線大標、
分類色只用通過驗證器的三色（#A98722 金／#5C77C4 藍／#00806B 綠），
無療效結果或非同期對照一律加斜線紋理並附文字標籤，不靠顏色分辨。
"""
import json, os, html

GOLD, BLUE, TEAL = "#A98722", "#5C77C4", "#00806B"
INK, SUB, MUTE, DEEP = "#123641", "#527078", "#6B8084", "#345963"

DEFS = ('<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">'
        '<stop stop-color="#F4EFE3"/><stop offset="1" stop-color="#E8E1D1"/></linearGradient>'
        '<pattern id="hatch" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
        '<rect width="8" height="8" fill="#123641" opacity=".10"/>'
        '<line x1="0" y1="0" x2="0" y2="8" stroke="#123641" stroke-width="2.2" opacity=".75"/></pattern><pattern id="hatchlite" width="10" height="10" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="10" stroke="#123641" stroke-width="1.4" opacity=".22"/></pattern>'
        '<style>.z{font-family:"Noto Sans TC","Noto Sans CJK TC","PingFang TC","Microsoft JhengHei",sans-serif}'
        '.r{font-family:"Noto Serif TC","Noto Serif CJK TC","PingFang TC","Microsoft JhengHei",serif}</style></defs>')


def esc(s):
    return html.escape(s, quote=False)


def _cw(ch, size):
    """單一字元的估計寬度。CJK 與全形標點約一個字寬，拉丁字母約 0.55。"""
    o = ord(ch)
    if o > 0x2E00 or o in (0xFF0C, 0xFF08, 0xFF09):
        return size * 1.0
    if ch in "iIl.,;:'|!":
        return size * 0.30
    if ch in "mMWw@":
        return size * 0.88
    return size * 0.55


def wrap(s, size, maxw):
    """把字串切成不超過 maxw 的多行。拉丁字以空白斷行，CJK 可任意斷。"""
    lines, cur, curw = [], "", 0.0
    i = 0
    while i < len(s):
        ch = s[i]
        w = _cw(ch, size)
        if curw + w > maxw and cur:
            # 拉丁字中間不斷詞：往回找最後一個空白
            if ch not in " \u3000" and ord(ch) < 0x2E00:
                j = cur.rfind(" ")
                if j > len(cur) * 0.35:
                    lines.append(cur[:j])
                    cur = cur[j + 1:]
                    curw = sum(_cw(x, size) for x in cur)
                    continue
            lines.append(cur.rstrip())
            cur, curw = "", 0.0
            if ch == " ":
                i += 1
                continue
        cur += ch
        curw += w
        i += 1
    if cur.strip():
        lines.append(cur.rstrip())
    return lines or [""]


class Canvas(object):
    def __init__(self, w, mobile=False):
        self.w = w
        self.mobile = mobile
        self.m = 48 if mobile else 84
        self.inner = w - 2 * self.m
        self.o = []
        self.y = 0

    def t(self, x, y, s, size, fill, weight=None, cls=None, ls=None, anchor=None):
        a = ['x="%s"' % x, 'y="%s"' % y, 'font-size="%s"' % size, 'fill="%s"' % fill]
        if weight: a.append('font-weight="%s"' % weight)
        if cls: a.append('class="%s"' % cls)
        if ls: a.append('letter-spacing="%s"' % ls)
        if anchor: a.append('text-anchor="%s"' % anchor)
        self.o.append('<text %s>%s</text>' % (" ".join(a), esc(s)))

    def tw(self, x, y, s, size, fill, maxw, weight=None, cls=None, lh=None, anchor=None):
        """自動換行的文字，回傳下一行的 y。"""
        lh = lh or int(size * 1.45)
        for ln in wrap(s, size, maxw):
            self.t(x, y, ln, size, fill, weight, cls, anchor=anchor)
            y += lh
        return y

    def rect(self, x, y, w, h, fill, rx=8, op=None, stroke=None, sw=None):
        a = ['x="%s"' % x, 'y="%s"' % y, 'width="%s"' % w, 'height="%s"' % h,
             'rx="%s"' % rx, 'fill="%s"' % fill]
        if op is not None: a.append('opacity="%s"' % op)
        if stroke: a.append('stroke="%s"' % stroke)
        if sw: a.append('stroke-width="%s"' % sw)
        self.o.append('<rect %s/>' % " ".join(a))

    def line(self, x1, y1, x2, y2, stroke, sw=1.6, dash=None, op=None):
        a = ['x1="%s"' % x1, 'y1="%s"' % y1, 'x2="%s"' % x2, 'y2="%s"' % y2,
             'stroke="%s"' % stroke, 'stroke-width="%s"' % sw, 'stroke-linecap="round"']
        if dash: a.append('stroke-dasharray="%s"' % dash)
        if op is not None: a.append('opacity="%s"' % op)
        self.o.append('<line %s/>' % " ".join(a))

    # ---- 標準區塊 ----
    def head(self, kicker, title, subs):
        f = 0.86 if self.mobile else 1.0
        self.t(self.m, int(78 * f) + (14 if self.mobile else 0), kicker, int(18 * f), GOLD, 800, ls="5px")
        ty = int(140 * f) + (18 if self.mobile else 0)
        tsize = int(44 * f)
        # 襯線字略寬，估寬時放大一成再換行；仍過寬就縮字級
        while tsize > int(26 * f) and len(wrap(title, int(tsize * 1.12), self.inner)) > 2:
            tsize -= 2
        tlines = wrap(title, int(tsize * 1.12), self.inner)
        for k, ln in enumerate(tlines):
            self.t(self.m, ty + k * int(tsize * 1.24), ln, tsize, INK, 800, cls="r")
        y = ty + (len(tlines) - 1) * int(tsize * 1.24) + int(52 * f)
        for s in subs:
            y = self.tw(self.m, y, s, int(21 * f), SUB, self.inner, lh=int(31 * f))
        self.y = y + int(28 * f)

    def note(self, lines, source):
        f = 0.86 if self.mobile else 1.0
        y = self.y + int(24 * f)
        self.rect(self.m, y, self.inner, 2, GOLD, rx=1, op=.5)
        y += int(34 * f)
        for s in lines:
            y = self.tw(self.m, y, s, int(19 * f), DEEP, self.inner, 700, lh=int(30 * f))
        y += int(8 * f)
        y = self.tw(self.m, y, source, int(16 * f), MUTE, self.inner, lh=int(24 * f))
        self.y = y

    def render(self, title, desc):
        h = int(self.y + (34 if self.mobile else 40))
        return ('<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d" '
                'role="img" aria-labelledby="t d">\n  <title id="t">%s</title>\n  <desc id="d">%s</desc>\n  %s\n'
                '  <rect width="%d" height="%d" rx="36" fill="url(#bg)"/>\n  <g class="z">\n%s\n  </g>\n</svg>\n'
                % (self.w, h, self.w, h, esc(title), esc(desc), DEFS, self.w, h, "\n".join(self.o)))


def barrow(c, y, label, frac, color, sub=None, hatch=False, f=1.0):
    """一條水平長條 + 左上標籤。frac 是佔滿版寬的比例。"""
    bh = int(38 * f)
    c.t(c.m, y, label, int(19 * f), INK, 700)
    yy = y + int(12 * f)
    c.rect(c.m, yy, c.inner, bh, INK, rx=8, op=.05)
    w = max(int(c.inner * frac), 8)
    c.rect(c.m, yy, w, bh, color, rx=8, op=.88)
    if hatch:
        c.rect(c.m, yy, w, bh, "url(#hatch)", rx=8)
    if sub:
        c.t(c.m + int(14 * f), yy + int(26 * f), sub, int(17 * f), "#FFFFFF", 700)
    return yy + bh + int(26 * f)


# ============================== 文案 ==============================
TXT = {
"reaction": {
 "kicker": "NEUTRON CAPTURE",
 "zh": dict(title="殺傷範圍不到一顆細胞",
   subs=["硼-10 捕獲一顆熱中子後分裂成兩顆碎片。它們帶著能量，",
         "在組織裡只跑五到九微米就停下來——大約一顆哺乳類細胞的大小。"],
   chain=["硼-10", "＋ 熱中子", "→ α 粒子 ＋ 鋰-7"],
   branch=["基態 93.7%：總能量約 2.31 MeV", "激發態 6.3%：約 2.79 MeV，另放出 0.48 MeV 加馬射線"],
   scale=["兩顆碎片的合計射程：5–9 微米", "一顆哺乳類細胞的直徑（示意）"],
   notes=["所以選擇性是生物性的：吃進硼的細胞被摧毀，沒吃進去的隔壁細胞不會挨到硼這一份。",
          "但同一束中子在組織裡還產生另外三種劑量，那三種和硼無關（見劑量那張圖）。"],
   src="示意圖，依 Barth 等 2005、Terranova 2026 與 Current Oncology 2022 的敘述重繪；長度為示意，非按比例。"),
 "en": dict(title="A kill radius smaller than one cell",
   subs=["Boron-10 captures a thermal neutron and splits into two fragments.",
         "They travel only 5-9 micrometres in tissue - about the size of one mammalian cell."],
   chain=["Boron-10", "+ thermal neutron", "→ alpha particle + lithium-7"],
   branch=["Ground state 93.7%: total energy about 2.31 MeV",
           "Excited state 6.3%: about 2.79 MeV, plus a 0.48 MeV gamma ray"],
   scale=["Combined range of the two fragments: 5-9 micrometres",
          "Diameter of one mammalian cell (schematic)"],
   notes=["So the selectivity is biological: the cell that took up boron is destroyed, its neighbour is not.",
          "But the same neutron beam produces three other dose components that have nothing to do with boron."],
   src="Schematic, redrawn from the descriptions in Barth et al. 2005, Terranova 2026 and Current Oncology 2022; lengths are indicative, not to scale."),
},
"dose": {
 "kicker": "DOSE",
 "zh": dict(title="一次照射，四種劑量",
   subs=["只有第一種需要硼。其餘三種打在所有被中子穿過的組織上，",
         "包括正常組織——這是 BNCT 不能被說成「不傷正常組織」的物理理由。"],
   bars=[("硼劑量（高 LET）", .95, GOLD, "只發生在有硼的地方"),
         ("氮劑量　14N(n,p)14C，質子約 0.54 MeV", .62, BLUE, "與硼無關"),
         ("快中子劑量　中子撞氫、撞飛質子", .48, BLUE, "與硼無關"),
         ("光子劑量　組織內 1H(n,γ)2H 與射束污染", .40, BLUE, "與硼無關")],
   cbe=["各成分乘上係數再相加，得到「光子等效劑量」Gy-Eq",
        "CBE：腫瘤 3.8　皮膚 2.5　口腔黏膜 2.5　腦與脊髓 1.3　　射束高 LET 成分 RBE 3.2"],
   notes=["Gy-Eq 和放射治療的 Gy 不是同一個單位：不能互相比較，也不能相加。",
          "這些係數是從動物與早期臨床推出來的估計值，不是量出來的常數。"],
   src="示意圖，依 MIT OpenCourseWare 22.55J 講義與 Barth 等 2005 重繪；長條長度為示意，非實際劑量比例。"),
 "en": dict(title="One irradiation, four dose components",
   subs=["Only the first one needs boron. The other three deposit in every tissue the beam passes through,",
         "including normal tissue - which is why BNCT cannot be described as sparing normal tissue entirely."],
   bars=[("Boron dose (high LET)", .95, GOLD, "only where boron is"),
         ("Nitrogen dose  14N(n,p)14C, proton about 0.54 MeV", .62, BLUE, "independent of boron"),
         ("Fast neutron dose  recoil protons from hydrogen", .48, BLUE, "independent of boron"),
         ("Photon dose  1H(n,gamma)2H in tissue and beam contamination", .40, BLUE, "independent of boron")],
   cbe=["Each component is weighted and summed into a photon-equivalent dose, Gy-Eq",
        "CBE: tumour 3.8  skin 2.5  oral mucosa 2.5  brain and spinal cord 1.3   RBE 3.2 for high-LET beam components"],
   notes=["Gy-Eq is not the same unit as the Gy of external-beam radiotherapy: the numbers cannot be compared or added.",
          "These factors are estimates derived from animal and early clinical work, not measured constants."],
   src="Schematic, redrawn from the MIT OpenCourseWare 22.55J lecture notes and Barth et al. 2005; bar lengths are indicative, not actual dose ratios."),
},
"depth": {
 "kicker": "PENETRATION",
 "zh": dict(title="中子走得到哪裡",
   subs=["深度限制不是「還沒研究到」，是物理。這張圖是 BNCT 適應症清單",
         "為什麼這麼短的主要理由。"],
   bars=[("熱中子束　通量峰值在皮下約 2–3 公分", .28, BLUE, "十公分處只剩峰值約十分之一"),
         ("超熱中子　可涵蓋皮下約 6–8 公分的腫瘤", .70, GOLD, "現行治療用的就是這一種"),
         ("腦部中線腫瘤　約 8 公分深處，治療比仍大於 1", .80, TEAL, "文獻上找得到最深的可引用數據點")],
   notes=["八公分是可引用的最深數據點，不是一條被量出來的界線；再深下去，正常組織的代價開始追上好處。",
          "肝、肺、胰臟、深部骨盆腔落在這條線之外——那不是還沒輪到，是中子到不了。"],
   src="示意圖，依 Current Oncology 2022 與 Barth 等 2012 的敘述重繪；長條長度為示意，非深度比例尺。"),
 "en": dict(title="How far the neutrons get",
   subs=["The depth limit is physics, not a gap in the research. It is the main reason",
         "the list of BNCT indications is as short as it is."],
   bars=[("Thermal beam  flux peaks about 2-3 cm below the skin", .28, BLUE, "at 10 cm, about one tenth of the peak"),
         ("Epithermal beam  reaches tumours about 6-8 cm deep", .70, GOLD, "this is what clinical treatment uses"),
         ("Midline brain tumour  therapeutic ratio still above 1 at about 8 cm", .80, TEAL, "the deepest citable data point")],
   notes=["Eight centimetres is the deepest citable data point, not a measured boundary; deeper than that, the cost to normal tissue catches up with the benefit.",
          "Liver, lung, pancreas and the deep pelvis sit outside this line - not yet to be studied, but out of reach."],
   src="Schematic, redrawn from Current Oncology 2022 and Barth et al. 2012; bar lengths are indicative, not a depth scale."),
},
}

TXT["pathway"] = {
 "kicker": "SCREENING",
 "zh": dict(title="照射之前的那幾關",
   subs=["BNCT 少數對病人公道的地方，是它的必要條件事前量得到。",
         "這也表示：有人會在這裡被判定不適合。"],
   steps=[("1", "標準治療用盡或不適用", "已接受過常規放療，且手術、放療、化療三條救援路線都不適用"),
          ("2", "位置與深度評估", "病灶要在中子還有力氣的那幾公分內"),
          ("3", "¹⁸F-BPA 正子攝影，量腫瘤／正常組織攝取比 T/N", "臨床試驗常用的門檻是 T/N 大於 2.5"),
          ("4", "再照射風險評估", "要有人拿著你先前的放療劑量分布坐下來算過")],
   branch=("未達門檻：不適合", "代價全付，好處沒拿——省下的不只是錢，還有再照射的額度與一段體力"),
   notes=["過了門檻只是必要條件，不是充分條件：它量的是硼進不進得去，不是治療有沒有效。",
          "第四關最常被跳過。評估你的人手上沒有先前的放療計畫，那一題就還沒開始。"],
   src="示意圖，依 NCT01173172 的收案條件與 Barth 等 2012 的敘述整理重繪。"),
 "en": dict(title="The gates before irradiation",
   subs=["One of the fairer things about BNCT is that its necessary condition can be measured in advance.",
         "Which also means some people are told here that they are not suitable."],
   steps=[("1", "Standard treatment exhausted or unsuitable", "prior conventional radiotherapy, and surgery, radiotherapy and chemotherapy all unsuitable as salvage"),
          ("2", "Site and depth assessment", "the lesion has to sit within the few centimetres the neutrons still reach"),
          ("3", "18F-BPA PET, tumour-to-normal uptake ratio", "trials commonly use a threshold of T/N above 2.5"),
          ("4", "Re-irradiation risk assessment", "someone has to sit down with your previous dose distribution")],
   branch=("Below the threshold: not suitable", "full cost, no benefit - what is saved is not only money but the one re-irradiation allowance and a stretch of physical reserve"),
   notes=["Clearing the threshold is a necessary condition, not a sufficient one: it measures whether boron gets in, not whether treatment works.",
          "Gate four is the one most often skipped. If the person assessing you does not have your previous plan, that question has not been answered."],
   src="Schematic, compiled and redrawn from the eligibility criteria of NCT01173172 and the descriptions in Barth et al. 2012."),
}

TXT["gbm"] = {
 "kicker": "HOW TO READ A TRIAL",
 "zh": dict(title="兩個都是真的數字",
   subs=["同一個試驗，同一批 27 位復發膠質母細胞瘤病人。",
         "影像幾乎沒有反應，一年後卻有近八成的人還活著。"],
   panels=[("影像看到的", [("RANO 影像反應率", "3.7%"), ("中位無惡化存活", "0.9 個月")], BLUE,
            "腦部照射後常有假性惡化，RANO 在這個情境下會失真"),
           ("存活看到的", [("1 年存活率", "79.2%"), ("中位總存活", "18.9 個月")], GOLD,
            "95% 信賴區間 57.0–90.8")],
   compare=[("JG002（BNCT，n=27）", .90, GOLD, False, "18.9 個月"),
            ("JO22506（bevacizumab 單藥，n=31，2012 年）", .50, INK, True, "10.5 個月　非同期歷史對照")],
   notes=["27 人裡有 21 人（78%）在惡化後接受了 bevacizumab。所以這個比較的實際內容是",
          "「BNCT 之後再接 bevacizumab」對上「bevacizumab 單藥」，而且對照組是四到六年前的世代。",
          "第三級以上治療相關不良事件 81.5%；腦水腫 48.1%。"],
   src="示意圖，依 Kawabata 等 2021（Neuro-Oncology Advances）與 Nagane 等 2012（Jpn J Clin Oncol）重繪；長條為存活月數的相對長度。"),
 "en": dict(title="Both numbers are true",
   subs=["One trial, the same 27 patients with recurrent glioblastoma.",
         "Almost no imaging response, yet nearly eight in ten were alive at one year."],
   panels=[("What imaging saw", [("RANO response rate", "3.7%"), ("Median progression-free survival", "0.9 months")], BLUE,
            "pseudoprogression is common after brain irradiation, and RANO misreads it"),
           ("What survival saw", [("One-year survival", "79.2%"), ("Median overall survival", "18.9 months")], GOLD,
            "95% CI 57.0-90.8")],
   compare=[("JG002 (BNCT, n=27)", .90, GOLD, False, "18.9 months"),
            ("JO22506 (bevacizumab alone, n=31, 2012)", .50, INK, True, "10.5 months  non-contemporaneous historical control")],
   notes=["21 of the 27 patients (78%) received bevacizumab after progression. So what this comparison actually contrasts is",
          "BNCT followed by bevacizumab against bevacizumab alone - and the control cohort is four to six years older.",
          "Grade 3 or higher treatment-related adverse events: 81.5%. Brain oedema: 48.1%."],
   src="Schematic, redrawn from Kawabata et al. 2021 (Neuro-Oncology Advances) and Nagane et al. 2012 (Jpn J Clin Oncol); bar lengths show relative median survival in months."),
}

TXT["evidence"] = {
 "kicker": "EVIDENCE",
 "zh": dict(title="各癌別走到哪一格",
   subs=["這個領域沒有隨機分派試驗。所以要看的不是有沒有數字，",
         "是那個數字後面站著幾個人、用什麼設計得到的。"],
   rows=[("復發頭頸癌", "單臂第二期 ＋ 上市後監測", "21 人 ／ 162 人", GOLD, False),
         ("復發膠質母細胞瘤", "單臂第二期 ＋ 歷史世代對照", "27 人", GOLD, False),
         ("復發高分級腦膜瘤", "病例系列", "44 人", BLUE, False),
         ("黑色素瘤", "病例系列", "全球約三、四十例", BLUE, False),
         ("乳房外柏哲德氏症", "病例系列", "個位數", BLUE, False),
         ("新診斷膠質母細胞瘤", "第一期，尚無療效結果", "目標 12–18 人", TEAL, True),
         ("肝、肺與深部器官", "個案報告", "個位數", TEAL, True)],
   legend=["斜線＝尚無療效結果或僅個案報告"],
   notes=["只有第一列有藥證，而且只限「不可切除的局部進行或局部復發頭頸癌」這一個適應症。",
          "分母愈小，數字愈容易好看——因為做得好的比較容易被寫出來。"],
   src="示意圖，依本專題各篇引用的原始文獻整理；分母為各該報告的收案人數。"),
 "en": dict(title="Where each cancer actually stands",
   subs=["There are no randomised trials in this field. So the question is not whether there is a number,",
         "but how many people stand behind it and what design produced it."],
   rows=[("Recurrent head and neck cancer", "single-arm phase II + post-marketing surveillance", "21 / 162 patients", GOLD, False),
         ("Recurrent glioblastoma", "single-arm phase II + historical cohort control", "27 patients", GOLD, False),
         ("Recurrent high-grade meningioma", "case series", "44 patients", BLUE, False),
         ("Melanoma", "case series", "roughly 30-40 cases worldwide", BLUE, False),
         ("Extramammary Paget disease", "case series", "single digits", BLUE, False),
         ("Newly diagnosed glioblastoma", "phase I, no efficacy results yet", "target 12-18 patients", TEAL, True),
         ("Liver, lung and deep organs", "case reports", "single digits", TEAL, True)],
   legend=["Hatching = no efficacy results yet, or case reports only"],
   notes=["Only the first row has a drug approval, and only for one indication: unresectable locally advanced or locally recurrent head and neck cancer.",
          "The smaller the denominator, the better the numbers tend to look - the ones that went well are the ones that get written up."],
   src="Schematic, compiled from the primary literature cited across this topic; denominators are the enrolled numbers in each report."),
}


# ============================== 繪圖 ==============================
def draw_reaction(c, d):
    f = 0.86 if c.mobile else 1.0
    y = c.y
    if c.mobile:
        for i, part in enumerate(d["chain"]):
            col = [GOLD, MUTE, TEAL][i]
            c.rect(c.m, y, c.inner, int(56 * f), INK, rx=12, op=.05)
            c.t(int(c.m + c.inner / 2), y + int(37 * f), part, int(22 * f), col, 800, anchor="middle")
            y += int(56 * f) + int(10 * f)
        y += int(12 * f)
    else:
        c.rect(c.m, y, c.inner, 96, INK, rx=16, op=.05)
        cw = c.inner / 3.0
        for i, part in enumerate(d["chain"]):
            col = [GOLD, MUTE, TEAL][i]
            c.t(int(c.m + cw * i + cw / 2), y + 58, part, 24, col, 800, anchor="middle")
            if i < 2:
                c.line(int(c.m + cw * (i + 1)), y + 24, int(c.m + cw * (i + 1)), y + 72, INK, 1.2, "4 6", .3)
        y += 96 + 24
    for s_ in d["branch"]:
        y = c.tw(c.m, y, "・" + s_, int(18 * f), SUB, c.inner, lh=int(28 * f))
    y += int(18 * f)
    for i, (lab, frac, col) in enumerate([(d["scale"][0], .30, GOLD), (d["scale"][1], .34, MUTE)]):
        y = c.tw(c.m, y, lab, int(19 * f), INK, c.inner, 700, lh=int(28 * f))
        yy = y + int(6 * f)
        c.rect(c.m, yy, c.inner, int(30 * f), INK, rx=8, op=.05)
        c.rect(c.m, yy, int(c.inner * frac), int(30 * f), col, rx=8, op=.88 if i == 0 else .35)
        y = yy + int(30 * f) + int(24 * f)
    c.y = y
    c.note(d["notes"], d["src"])


def draw_bars(c, d):
    f = 0.86 if c.mobile else 1.0
    y = c.y
    bh = int(38 * f)
    for lab, frac, col, sub in d["bars"]:
        y = c.tw(c.m, y, lab, int(19 * f), INK, c.inner, 700, lh=int(27 * f))
        yy = y + int(6 * f)
        c.rect(c.m, yy, c.inner, bh, INK, rx=8, op=.05)
        w = max(int(c.inner * frac), 8)
        c.rect(c.m, yy, w, bh, col, rx=8, op=.88)
        c.t(c.m + int(14 * f), yy + int(26 * f), sub, int(16 * f), "#FFFFFF", 700)
        y = yy + bh + int(24 * f)
    if "cbe" in d:
        c.rect(c.m, y, c.inner, 2, INK, rx=1, op=.12)
        y += int(30 * f)
        for s_ in d["cbe"]:
            y = c.tw(c.m, y, s_, int(18 * f), SUB, c.inner, lh=int(27 * f))
        y += int(6 * f)
    c.y = y
    c.note(d["notes"], d["src"])


def draw_pathway(c, d):
    f = 0.86 if c.mobile else 1.0
    y = c.y
    pad = int(26 * f)
    tw = c.inner - pad - int(24 * f)
    for num, head, body in d["steps"]:
        hl = wrap(head, int(20 * f), tw - int(32 * f))
        bl = wrap(body, int(17 * f), tw)
        h = int(26 * f) + len(hl) * int(28 * f) + len(bl) * int(25 * f) + int(16 * f)
        c.rect(c.m, y, c.inner, h, INK, rx=14, op=.05)
        c.rect(c.m, y, int(8 * f), h, GOLD, rx=4, op=.9)
        yy = y + int(34 * f)
        c.t(c.m + pad, yy, num, int(20 * f), GOLD, 800)
        for k, ln in enumerate(hl):
            c.t(c.m + pad + int(30 * f), yy + k * int(28 * f), ln, int(20 * f), INK, 700)
        yy += len(hl) * int(28 * f) + int(4 * f)
        for ln in bl:
            c.t(c.m + pad + int(30 * f), yy, ln, int(17 * f), SUB)
            yy += int(25 * f)
        y += h + int(12 * f)
        c.t(int(c.m + c.inner / 2), y + int(12 * f), "▼", int(14 * f), MUTE, anchor="middle")
        y += int(24 * f)
    bh_, bt = d["branch"]
    hl = wrap(bh_, int(20 * f), tw)
    bl = wrap(bt, int(17 * f), tw)
    h = int(26 * f) + len(hl) * int(28 * f) + len(bl) * int(25 * f) + int(16 * f)
    c.rect(c.m, y, c.inner, h, TEAL, rx=14, op=.09, stroke=TEAL, sw=2)
    c.rect(c.m, y, c.inner, h, "url(#hatchlite)", rx=14)
    yy = y + int(34 * f)
    for ln in hl:
        c.t(c.m + pad, yy, ln, int(20 * f), "#00604F", 800)
        yy += int(28 * f)
    yy += int(4 * f)
    for ln in bl:
        c.t(c.m + pad, yy, ln, int(17 * f), DEEP)
        yy += int(25 * f)
    c.y = y + h
    c.note(d["notes"], d["src"])


def draw_gbm(c, d):
    f = 0.86 if c.mobile else 1.0
    y = c.y
    pw = c.inner if c.mobile else int((c.inner - 32) / 2)
    ph = 0
    for i, (head, rows, col, foot) in enumerate(d["panels"]):
        fl = wrap(foot, int(15 * f), pw - int(36 * f))
        h = int(88 * f) + len(rows) * int(38 * f) + len(fl) * int(21 * f) + int(18 * f)
        px = c.m if c.mobile else c.m + i * (pw + 32)
        py = y
        c.rect(px, py, pw, h, INK, rx=16, op=.05)
        c.rect(px, py, pw, int(6 * f), col, rx=3, op=.9)
        c.t(px + int(22 * f), py + int(46 * f), head, int(20 * f), col, 800)
        yy = py + int(88 * f)
        for lab, val in rows:
            c.t(px + int(22 * f), yy, lab, int(16 * f), SUB)
            c.t(px + pw - int(22 * f), yy, val, int(25 * f), INK, 800, anchor="end")
            yy += int(38 * f)
        yy += int(4 * f)
        for ln in fl:
            c.t(px + int(22 * f), yy, ln, int(15 * f), MUTE)
            yy += int(21 * f)
        ph = max(ph, h)
        if c.mobile:
            y = py + h + int(18 * f)
    if not c.mobile:
        y += ph + int(32 * f)
    else:
        y += int(12 * f)
    for lab, frac, col, hatch, val in d["compare"]:
        y = c.tw(c.m, y, lab, int(18 * f), INK, c.inner, 700, lh=int(26 * f))
        yy = y + int(6 * f)
        bh = int(34 * f)
        c.rect(c.m, yy, c.inner, bh, INK, rx=8, op=.05)
        w = int(c.inner * frac)
        if hatch:
            c.rect(c.m, yy, w, bh, col, rx=8, op=.14, stroke=col, sw=2)
            c.rect(c.m, yy, w, bh, "url(#hatchlite)", rx=8)
            y = c.tw(c.m + int(14 * f), yy + int(23 * f), val, int(16 * f), DEEP,
                     w - int(28 * f), 700, lh=int(22 * f))
            y = yy + bh + int(22 * f)
        else:
            c.rect(c.m, yy, w, bh, col, rx=8, op=.88)
            c.t(c.m + int(14 * f), yy + int(23 * f), val, int(16 * f), "#FFFFFF", 700)
            y = yy + bh + int(22 * f)
    c.y = y
    c.note(d["notes"], d["src"])


def draw_evidence(c, d):
    f = 0.86 if c.mobile else 1.0
    y = c.y
    for name, design, n, col, hatch in d["rows"]:
        if c.mobile:
            nl = wrap(name, int(19 * f), c.inner - int(50 * f))
            dl = wrap(design, int(16 * f), c.inner - int(50 * f))
            h = int(20 * f) + len(nl) * int(26 * f) + len(dl) * int(23 * f) + int(30 * f)
        else:
            nl, dl = [name], wrap(design, 17, 420)
            h = max(int(64 * f), int(24 * f) + len(dl) * int(24 * f) + int(24 * f))
        c.rect(c.m, y, c.inner, h, INK, rx=12, op=.05)
        c.rect(c.m, y, int(8 * f), h, col, rx=4, op=.9)
        if hatch:
            c.rect(c.m, y, c.inner, h, "url(#hatchlite)", rx=12)
        if c.mobile:
            yy = y + int(30 * f)
            for ln in nl:
                c.t(c.m + int(26 * f), yy, ln, int(19 * f), INK, 700); yy += int(26 * f)
            for ln in dl:
                c.t(c.m + int(26 * f), yy, ln, int(16 * f), SUB); yy += int(23 * f)
            c.t(c.m + int(26 * f), yy + int(16 * f), n, int(17 * f), col, 800)
        else:
            c.t(c.m + 26, y + int(h / 2) + 7, name, 20, INK, 700)
            yy = y + int(h / 2) - (len(dl) - 1) * 12 + 6
            for ln in dl:
                c.t(c.m + 400, yy, ln, 17, SUB); yy += 24
            c.t(c.m + c.inner - 20, y + int(h / 2) + 7, n, 18, col, 800, anchor="end")
        y += h + int(12 * f)
    y += int(10 * f)
    for s_ in d["legend"]:
        y = c.tw(c.m, y, s_, int(16 * f), MUTE, c.inner, lh=int(24 * f))
    c.y = y
    c.note(d["notes"], d["src"])


DRAW = {"reaction": draw_reaction, "dose": draw_bars, "depth": draw_bars,
        "pathway": draw_pathway, "gbm": draw_gbm, "evidence": draw_evidence}


def build(outdir="figs"):
    if not os.path.isdir(outdir):
        os.makedirs(outdir)
    manifest = {}
    for key, spec in TXT.items():
        manifest[key] = {}
        for lang in ("zh", "en"):
            d = spec[lang]
            for mobile in (False, True):
                c = Canvas(720 if mobile else 1440, mobile)
                c.head(spec["kicker"], d["title"], d["subs"])
                DRAW[key](c, d)
                name = "fig-bn-%s%s%s.svg" % (key, "-en" if lang == "en" else "",
                                              "-mobile" if mobile else "")
                desc = " ".join(d["subs"]) + " " + " ".join(d["notes"])
                open(os.path.join(outdir, name), "w", encoding="utf-8").write(
                    c.render(d["title"], desc))
                manifest[key]["%s%s" % (lang, "_mobile" if mobile else "")] = name
    open("figs-manifest.json", "w", encoding="utf-8").write(
        json.dumps(manifest, ensure_ascii=False, indent=2))
    return manifest


if __name__ == "__main__":
    m = build()
    print("圖檔 %d 個" % sum(len(v) for v in m.values()))
    for k in m: print(" ", k, "→", m[k]["zh"])
