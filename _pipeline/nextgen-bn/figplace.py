# -*- coding: utf-8 -*-
"""六張圖在正文裡的位置與說明文字。插入點是「該小標的下一段之後」。"""

# slug: (fig key, 插入點的小標, 圖說 zh, 圖說 en)
PLACE = {
 "principle": ("reaction", "<h4>能量花在多短的距離裡，才是重點</h4>",
   "示意圖，碎片射程與細胞大小為示意，非按比例；依 Barth 等 2005 與 Terranova 2026 的敘述重繪。",
   "Schematic; fragment range and cell size are indicative, not to scale. Redrawn from the descriptions in Barth et al. 2005 and Terranova 2026."),
 "dose": ("dose", "<h4>照一次中子，身體其實同時吃到四種劑量</h4>",
   "示意圖，長條長度為示意，非實際劑量比例；依 MIT OpenCourseWare 22.55J 講義與 Barth 等 2005 重繪。",
   "Schematic; bar lengths are indicative, not actual dose ratios. Redrawn from the MIT OpenCourseWare 22.55J lecture notes and Barth et al. 2005."),
 "depth": ("depth", "<h4>從熱中子到超熱中子：為了多鑽幾公分</h4>",
   "示意圖，長條長度為示意，非深度比例尺；依 Current Oncology 2022 與 Barth 等 2012 重繪。",
   "Schematic; bar lengths are indicative, not a depth scale. Redrawn from Current Oncology 2022 and Barth et al. 2012."),
 "pet": ("pathway", "<h4>那個試驗的收案條件，比門檻本身更有資訊</h4>",
   "示意圖，依 NCT01173172 的收案條件與 Barth 等 2012 的敘述整理重繪。",
   "Schematic, compiled and redrawn from the eligibility criteria of NCT01173172 and the descriptions in Barth et al. 2012."),
 "gbm": ("gbm", "<h4>第二件事：那個 18.9 個月，是跟誰比的</h4>",
   "示意圖，長條為存活月數的相對長度，歷史對照以斜線標示；依 Kawabata 等 2021 與 Nagane 等 2012 重繪。",
   "Schematic; bar lengths show relative median survival in months and the historical control is hatched. Redrawn from Kawabata et al. 2021 and Nagane et al. 2012."),
 "others": ("evidence", "<h4>先回到第三篇的那條線</h4>",
   "示意圖，分母為各該報告的收案人數；依本專題各篇引用的原始文獻整理。",
   "Schematic; denominators are the enrolled numbers in each report, compiled from the primary literature cited across this topic."),
}

ALT = {
 "reaction": ("示意圖：硼-10 加熱中子分裂成 α 粒子與鋰-7，兩顆碎片的合計射程五到九微米，"
              "與一顆哺乳類細胞的直徑並排比較。",
              "Schematic: boron-10 plus a thermal neutron splits into an alpha particle and lithium-7; "
              "the combined range of 5-9 micrometres is shown beside the diameter of one mammalian cell."),
 "dose": ("示意圖：四條長條分別代表硼劑量、氮劑量、快中子劑量與光子劑量，後三種標示為與硼無關；"
          "下方列出 CBE 與 RBE 的常用數值。",
          "Schematic: four bars for the boron, nitrogen, fast-neutron and photon dose components, "
          "the last three labelled as independent of boron; the commonly used CBE and RBE values are listed below."),
 "depth": ("示意圖：三條長條分別是熱中子束的峰值深度約二到三公分、超熱中子可涵蓋約六到八公分、"
           "腦部中線約八公分處治療比仍大於一。",
           "Schematic: three bars showing the thermal beam peaking at about 2-3 cm, the epithermal beam "
           "reaching about 6-8 cm, and a therapeutic ratio still above 1 at about 8 cm for midline brain tumours."),
 "pathway": ("示意圖：照射前的四道關卡依序為標準治療用盡、位置與深度評估、正子攝影量 T/N、"
             "再照射風險評估；另有一個以斜線標示的分支，代表未達門檻、不適合。",
             "Schematic: four gates before irradiation - standard treatment exhausted, site and depth assessment, "
             "PET measurement of the T/N ratio, and re-irradiation risk assessment - plus a hatched branch for "
             "those below the threshold, who are not suitable."),
 "gbm": ("示意圖：左面板是影像看到的（RANO 反應率 3.7%、中位無惡化存活 0.9 個月），"
         "右面板是存活看到的（一年存活率 79.2%、中位總存活 18.9 個月）；"
         "下方兩條長條比較 JG002 的 18.9 個月與歷史對照 JO22506 的 10.5 個月，後者以斜線標示為非同期對照。",
         "Schematic: the left panel shows what imaging saw (RANO response rate 3.7%, median progression-free "
         "survival 0.9 months), the right panel what survival saw (one-year survival 79.2%, median overall "
         "survival 18.9 months); two bars below compare JG002's 18.9 months with the historical control "
         "JO22506's 10.5 months, the latter hatched to mark it as non-contemporaneous."),
 "evidence": ("示意圖：七列癌別依證據設計排列，從單臂第二期加上市後監測，到病例系列，"
              "再到尚無療效結果的第一期與個案報告；後兩類以斜線標示。",
              "Schematic: seven rows of cancers ordered by study design, from single-arm phase II plus "
              "post-marketing surveillance, through case series, to phase I with no efficacy results and "
              "case reports; the last two are hatched."),
}


def figure_html(key, lang, caption, alt, sizes):
    w, h = sizes
    suffix = "-en" if lang == "en" else ""
    return ('<figure class="article-figure">\n'
            '  <picture>\n'
            '    <source media="(max-width:620px)" srcset="fig-bn-%s%s-mobile.svg">\n'
            '    <img src="fig-bn-%s%s.svg" width="%d" height="%d" loading="lazy" decoding="async" alt="%s">\n'
            '  </picture>\n'
            '  <figcaption>%s</figcaption>\n'
            '</figure>' % (key, suffix, key, suffix, w, h, alt, caption))
