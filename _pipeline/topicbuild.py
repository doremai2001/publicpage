# -*- coding: utf-8 -*-
"""
Shared page builder for the bilingual disease-topic pages.

The site has no build system left, so every page is produced by *patching an
existing page* rather than by re-typing its markup: the template file is read
verbatim and only the known slots are substituted.  Everything else -- the
inline <style> block, the background SVG, the nav, the footer, the trailing
swirl script, the hub's tag-filter script -- survives byte-for-byte.

Public entry points:
    build(topic, lang, article_tpl, out_dir, zhonly=False)   -> [paths]
    build_index(topic, lang, hub_tpl, out_dir, zhonly=False)  -> path
"""

import html
import json
import os
import re

BASE = "https://doremai2001.github.io/publicpage/"

# ---------------------------------------------------------------- escaping --
# Text nodes on this site keep raw quotes and apostrophes; attributes (and,
# as the existing insight-*.html pages show, <title>) use &quot; but never
# &#x27;.  So: escape &, < and > everywhere, and " only where it matters.

def esc(s):
    """Escape for a text node."""
    return html.escape(s, quote=False)


def esca(s):
    """Escape for an attribute value (and for <title>)."""
    return html.escape(s, quote=False).replace('"', "&quot;")


# ------------------------------------------------------------- head slots --
RE_TITLE = re.compile(r"<title>(.*?)</title>", re.S)
RE_DESC = re.compile(r'<meta name="description" content="(.*?)">', re.S)
RE_OGT = re.compile(r'<meta property="og:title" content="(.*?)">', re.S)
RE_OGD = re.compile(r'<meta property="og:description" content="(.*?)">', re.S)
RE_OGU = re.compile(r'<meta property="og:url" content="(.*?)">', re.S)
RE_CANON = re.compile(r'<link rel="canonical" href="(.*?)">')
RE_ALTS = re.compile(
    r'<link rel="alternate" hreflang="zh-Hant" href="[^"]*">\n'
    r'<link rel="alternate" hreflang="en" href="[^"]*">\n'
    r'<link rel="alternate" hreflang="x-default" href="[^"]*">\n'
)
RE_LD = re.compile(r'<script type="application/ld\+json">.*?</script>', re.S)
RE_LANG = re.compile(r'\n\s*<div class="lang">.*?</div>', re.S)
RE_STYLE = re.compile(r"<style>.*?</style>", re.S)

# ---------------------------------------------------------- article slots --
RE_ART_KICKER = re.compile(r'(<div class="kicker">)(.*?)(</div>)', re.S)
RE_ART_H1 = re.compile(r"(<h1>)(.*?)(</h1>)", re.S)
RE_ART_DEK = re.compile(r'(<p class="dek">)(.*?)(</p>)', re.S)
RE_ART_META = re.compile(r'(<div class="meta">)(.*?)(</div>)', re.S)
RE_ART_TAGLIST = re.compile(r'(<div class="taglist">)(.*?)(</div>\n)', re.S)
RE_ART_LEAD = re.compile(r'(<div class="leadbox"><p>)(.*?)(</p></div>)', re.S)
RE_ART_BODY = re.compile(r'(<div class="body-html">\n)(.*?)(\n    </div>)', re.S)
RE_ART_MDNOTE = re.compile(
    r'(<div class="mdnote">\s*<div class="h">.*?</div>\s*<p>)(.*?)(</p>)', re.S
)
RE_ART_REFS = re.compile(r'(<div class="refs">\s*<h3>.*?</h3>\s*<ol>)(.*?)(</ol>)', re.S)
RE_ART_NOTE = re.compile(r'(<p class="note">)(.*?)(</p>)', re.S)
RE_ART_PNAV = re.compile(r'(<div class="pnav">)(.*?)(</div>)', re.S)
RE_ART_BACK = re.compile(r'(<a class="backlink" href=")([^"]*)(">)(.*?)(</a>)', re.S)
RE_ART_PVLBL = re.compile(r'<a class="pv" href="[^"]*"><span>(.*?)</span>')
RE_ART_NXLBL = re.compile(r'<a class="nx" href="[^"]*"><span>(.*?)</span>')

# -------------------------------------------------------------- hub slots --
RE_HUB_H2 = re.compile(r'(<h2>)(.*?)(<span class="sub">)(.*?)(</span></h2>)', re.S)
RE_HUB_INTRO = re.compile(
    r'(<p class="note" style="margin-top:18px">)(.*?)(</p>)', re.S
)
RE_HUB_TAGH = re.compile(r'(<div class="tagbar-h">)(.*?)(</div>)', re.S)
RE_HUB_TAGC = re.compile(r'(<div class="tagbar-c">)(.*?)(</div>)', re.S)
RE_HUB_ALLBTN = re.compile(
    r'<button class="tagf on" data-tag="">(.*?) <i>\d+</i></button>'
)
RE_HUB_BTN = re.compile(
    r'<button class="tagf(?: on)?" data-tag="([^"]*)">(.*?) <i>\d+</i></button>'
)
RE_HUB_CARDM = re.compile(r'<div class="m">(.*?)</div>')
RE_HUB_GROUPS = re.compile(
    r'(  <div class="postgroup hnstep">.*\n  </div>)(\n\n  <p class="note">)(.*?)(</p>)',
    re.S,
)

RE_DIGITS = re.compile(r"\d+")


def _sub1(rx, text, repl_fn, what):
    out, n = rx.subn(repl_fn, text, count=1)
    if n != 1:
        raise RuntimeError("slot not found exactly once: %s" % what)
    return out


# ------------------------------------------------------------ tag labels ---
def harvest_tag_labels(zh_hubs, en_hubs):
    """Pull {key: (zh_label, en_label)} and a canonical key order out of the
    existing hub pages, so no label is ever retyped.

    Labels come back as plain text, not markup: the harvested button text is
    HTML-unescaped here so that the escaping done at write time (esc()) puts
    exactly one level of entity back.  Without this, a label containing an
    ampersand -- "Genetics &amp; Family", "Sexual &amp; Fertility" -- would be
    written out as "&amp;amp;".
    """
    zh, order = {}, []
    for path in zh_hubs:
        s = open(path, encoding="utf-8").read()
        for key, label in RE_HUB_BTN.findall(RE_HUB_TAGC.search(s).group(2)):
            if not key:
                continue
            if key not in zh:
                zh[key] = html.unescape(label.lstrip("#"))
                order.append(key)
    en = {}
    for path in en_hubs:
        s = open(path, encoding="utf-8").read()
        for key, label in RE_HUB_BTN.findall(RE_HUB_TAGC.search(s).group(2)):
            if key and key not in en:
                en[key] = html.unescape(label.lstrip("#"))
    labels = {k: (zh[k], en.get(k, zh[k])) for k in zh}
    return labels, order


# ------------------------------------------------------------ body split ---
def split_fragment(fragment):
    """Split a source fragment at its <hr> into (body_html, ref_items, n).

    The fragment carries its own <ol>...</ol> around the reference list and a
    trailing empty <p></p>; both are dropped here, because the page template
    supplies the <div class="refs"><h3>..</h3><ol> wrapper itself.
    """
    i = fragment.find("<hr>")
    if i < 0:
        raise RuntimeError("fragment has no <hr>")
    body = fragment[:i].strip()
    tail = fragment[i:]
    m = re.search(r"<ol>(.*)</ol>", tail, re.S)
    if not m:
        raise RuntimeError("fragment has no reference <ol>")
    items = m.group(1).strip("\n")
    n_line = len(re.findall(r"(?m)^<li>", items))
    n_all = len(re.findall(r"<li>", items))
    if n_line != n_all:
        raise RuntimeError("unexpected nested <li> in reference list")
    return body, items, n_all


# --------------------------------------------------------- template facts --
class ArticleTemplate(object):
    """The reusable, language-specific facts carried by an article template."""

    def __init__(self, path):
        self.path = path
        self.text = open(path, encoding="utf-8").read()
        t = self.text
        meta = RE_ART_META.search(t).group(2)
        parts = meta.split(" · ")
        self.topic = parts[0]                 # e.g. 直腸癌專題 / Rectal Cancer Guide
        self.section = parts[1]               # e.g. 手術與之後 / Surgery and After
        self.refs_bit = parts[2]              # e.g. 參考文獻 14 篇 / 14 references
        self.h1 = RE_ART_H1.search(t).group(2)
        self.title = RE_TITLE.search(t).group(1)
        self.backlink = RE_ART_BACK.search(t).group(4)
        self.prev_label = RE_ART_PVLBL.search(t).group(1)
        self.next_label = RE_ART_NXLBL.search(t).group(1)
        self.disclaimer = RE_ART_NOTE.search(t).group(2)
        # title pattern, derived rather than retyped
        pat = self.title.replace(self.h1, "\x00T\x00")
        pat = pat.replace(self.topic, "\x00G\x00").replace(self.section, "\x00S\x00")
        self.title_pattern = pat

    def make_title(self, title, section):
        return (
            self.title_pattern.replace("\x00T\x00", title)
            .replace("\x00G\x00", self.topic_name)
            .replace("\x00S\x00", section)
        )

    def make_meta(self, section, n):
        return " · ".join(
            [self.topic_name, section, RE_DIGITS.sub(str(n), self.refs_bit)]
        )

    def make_backlink(self, name):
        return self.backlink.replace(self.topic, name)


class HubTemplate(object):
    def __init__(self, path):
        self.path = path
        self.text = open(path, encoding="utf-8").read()
        t = self.text
        self.h2_name = RE_HUB_H2.search(t).group(2)
        self.tag_head = RE_HUB_TAGH.search(t).group(2)
        self.all_label = RE_HUB_ALLBTN.search(t).group(1)
        self.card_m = RE_HUB_CARDM.search(t).group(1)

    def make_card_m(self, n):
        return RE_DIGITS.sub(str(n), self.card_m)


# ------------------------------------------------------------ head patch ---
def _patch_head(text, *, title, desc, url, alt_zh, alt_en, ld, zhonly):
    t = text
    ti, de, ur = esca(title), esca(desc), esca(url)
    t = _sub1(RE_TITLE, t, lambda m: "<title>%s</title>" % ti, "title")
    t = _sub1(RE_DESC, t,
              lambda m: '<meta name="description" content="%s">' % de, "description")
    t = _sub1(RE_OGT, t,
              lambda m: '<meta property="og:title" content="%s">' % ti, "og:title")
    t = _sub1(RE_OGD, t,
              lambda m: '<meta property="og:description" content="%s">' % de,
              "og:description")
    t = _sub1(RE_OGU, t,
              lambda m: '<meta property="og:url" content="%s">' % ur, "og:url")
    t = _sub1(RE_CANON, t,
              lambda m: '<link rel="canonical" href="%s">' % ur, "canonical")
    if zhonly:
        t = _sub1(RE_ALTS, t, lambda m: "", "hreflang block")
    else:
        alts = (
            '<link rel="alternate" hreflang="zh-Hant" href="%s">\n'
            '<link rel="alternate" hreflang="en" href="%s">\n'
            '<link rel="alternate" hreflang="x-default" href="%s">\n'
        ) % (esca(alt_zh), esca(alt_en), esca(alt_zh))
        t = _sub1(RE_ALTS, t, lambda m: alts, "hreflang block")
    raw = json.dumps(ld, ensure_ascii=False, separators=(",", ":"))
    t = _sub1(RE_LD, t,
              lambda m: '<script type="application/ld+json">%s</script>' % raw,
              "json-ld")
    return t


def _patch_lang_switch(text, other_href, lang, zhonly):
    if zhonly:
        return _sub1(RE_LANG, text, lambda m: "", "lang switch")
    if lang == "zh":
        div = ('<div class="lang"><span class="on">中</span>'
               '<a href="%s" hreflang="en">EN</a></div>' % esca(other_href))
    else:
        div = ('<div class="lang"><a href="%s" hreflang="zh-Hant">中</a>'
               '<span class="on">EN</span></div>' % esca(other_href))
    def repl(m):
        indent = m.group(0).split("<div", 1)[0]
        return indent + div
    return _sub1(RE_LANG, text, repl, "lang switch")


# ------------------------------------------------------- article building --
def _flatten(topic):
    """Reading order: [(index, slug, section_i)]"""
    out = []
    for si, sec in enumerate(topic.SECTIONS):
        for slug in sec["slugs"]:
            out.append((len(out), slug, si))
    return out


def _page_name(prefix, slug, lang):
    return "%s-%s%s.html" % (prefix, slug, "-en" if lang == "en" else "")


def _hub_name(prefix, lang):
    return "%s%s.html" % (prefix, "-en" if lang == "en" else "")


def build(topic, lang, article_tpl, out_dir, zhonly=False):
    """Write the topic's article pages for one language. Returns file paths."""
    tpl = ArticleTemplate(article_tpl)
    labels, _ = harvest_tag_labels(topic.TAG_SOURCES["zh"], topic.TAG_SOURCES["en"])
    labels.update(topic.LABEL_ADD)

    if lang == "zh":
        tpl.topic_name = topic.NAME_ZH
        meta = {s: topic.ART[s] for s in topic.ART}
        sections = [s["zh"] for s in topic.SECTIONS]
        cond = topic.CONDITION_ZH
        inlang = "zh-Hant"
        lab_i = 0
    else:
        tpl.topic_name = topic.NAME_EN
        meta = topic.EN
        sections = [s["en"] for s in topic.SECTIONS_EN]
        cond = topic.CONDITION_EN
        inlang = "en"
        lab_i = 1

    about_type = getattr(topic, "ABOUT_TYPE", "MedicalCondition")

    order = _flatten(topic)
    titles = {slug: meta[slug]["title"] for _, slug, _ in order}
    hub = _hub_name(topic.PREFIX, lang)
    written = []

    for idx, slug, si in order:
        frag_dir = topic.SRC["body_zh"] if lang == "zh" else topic.SRC["body_en"]
        fragment = open(os.path.join(frag_dir, slug + ".html"), encoding="utf-8").read()
        body, items, nrefs = split_fragment(fragment)
        for old, new in topic.BODY_EDITS[lang]:
            body = body.replace(old, new)

        m = meta[slug]
        section = sections[si]
        kicker = topic.SECTIONS_EN[si]["en"].upper()
        tags = topic.ART[slug]["tags"]
        name = _page_name(topic.PREFIX, slug, lang)
        url = BASE + name
        alt_zh = BASE + _page_name(topic.PREFIX, slug, "zh")
        alt_en = BASE + _page_name(topic.PREFIX, slug, "en")

        ld = {
            "@context": "https://schema.org",
            "@type": "MedicalWebPage",
            "headline": m["title"],
            "description": m["dek"],
            "url": url,
            "inLanguage": inlang,
            "datePublished": topic.DATE,
            "dateModified": topic.DATE,
            "image": BASE + "og.jpg",
            "about": {"@type": about_type, "name": cond},
            "author": {
                "@type": "Physician",
                "name": "吳正友 Robert Jeng-You Wu",
                "url": BASE,
            },
            "audience": {"@type": "Patient"},
            "isAccessibleForFree": True,
        }

        t = _patch_head(
            tpl.text,
            title=tpl.make_title(m["title"], section),
            desc=m["dek"],
            url=url,
            alt_zh=alt_zh,
            alt_en=alt_en,
            ld=ld,
            zhonly=zhonly,
        )
        other = _page_name(topic.PREFIX, slug, "en" if lang == "zh" else "zh")
        t = _patch_lang_switch(t, other, lang, zhonly)

        chips = "".join(
            '<a class="tagchip" href="%s?tag=%s">#%s</a>'
            % (esca(hub), esca(k), esc(labels[k][lab_i]))
            for k in tags
        )
        if idx == 0:
            prev = "<span></span>"
        else:
            p = order[idx - 1][1]
            prev = '<a class="pv" href="%s"><span>%s</span>%s</a>' % (
                esca(_page_name(topic.PREFIX, p, lang)),
                esc(tpl.prev_label),
                esc(titles[p]),
            )
        if idx == len(order) - 1:
            nxt = "<span></span>"
        else:
            nx = order[idx + 1][1]
            nxt = '<a class="nx" href="%s"><span>%s</span>%s</a>' % (
                esca(_page_name(topic.PREFIX, nx, lang)),
                esc(tpl.next_label),
                esc(titles[nx]),
            )

        t = _sub1(RE_ART_KICKER, t,
                  lambda mm: mm.group(1) + esc(kicker) + mm.group(3), "kicker")
        t = _sub1(RE_ART_H1, t,
                  lambda mm: mm.group(1) + esc(m["title"]) + mm.group(3), "h1")
        t = _sub1(RE_ART_DEK, t,
                  lambda mm: mm.group(1) + esc(m["dek"]) + mm.group(3), "dek")
        t = _sub1(RE_ART_META, t,
                  lambda mm: mm.group(1) + esc(tpl.make_meta(section, nrefs))
                  + mm.group(3), "meta")
        t = _sub1(RE_ART_TAGLIST, t,
                  lambda mm: mm.group(1) + chips + mm.group(3), "taglist")
        t = _sub1(RE_ART_LEAD, t,
                  lambda mm: mm.group(1) + esc(m["lead"]) + mm.group(3), "leadbox")
        t = _sub1(RE_ART_BODY, t,
                  lambda mm: mm.group(1) + body + mm.group(3), "body-html")
        t = _sub1(RE_ART_MDNOTE, t,
                  lambda mm: mm.group(1) + esc(m["note"]) + mm.group(3), "mdnote")
        t = _sub1(RE_ART_REFS, t,
                  lambda mm: mm.group(1) + items + mm.group(3), "refs")
        t = _sub1(RE_ART_PNAV, t,
                  lambda mm: mm.group(1) + prev + nxt + mm.group(3), "pnav")
        t = _sub1(RE_ART_BACK, t,
                  lambda mm: mm.group(1) + esca(hub) + mm.group(3)
                  + esc(tpl.make_backlink(tpl.topic_name)) + mm.group(5), "backlink")

        path = os.path.join(out_dir, name)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(t)
        written.append(path)
    return written


# ----------------------------------------------------------- hub building --
def build_index(topic, lang, hub_tpl, out_dir, zhonly=False):
    tpl = HubTemplate(hub_tpl)
    labels, order_keys = harvest_tag_labels(
        topic.TAG_SOURCES["zh"], topic.TAG_SOURCES["en"]
    )
    labels.update(topic.LABEL_ADD)
    order_keys = order_keys + [k for k in topic.LABEL_ADD if k not in order_keys]

    if lang == "zh":
        name_topic = topic.NAME_ZH
        meta = topic.ART
        sections = topic.SECTIONS
        seckey, subkey = "zh", "stepsub_zh"
        cond = topic.CONDITION_ZH
        inlang = "zh-Hant"
        hub_copy = topic.HUB
        lab_i = 0
    else:
        name_topic = topic.NAME_EN
        meta = topic.EN
        sections = topic.SECTIONS_EN
        seckey, subkey = "en", "stepsub_en"
        cond = topic.CONDITION_EN
        inlang = "en"
        hub_copy = topic.HUB_EN
        lab_i = 1

    about_type = getattr(topic, "ABOUT_TYPE", "MedicalCondition")

    order = _flatten(topic)
    nrefs = {}
    for _, slug, _ in order:
        d = topic.SRC["body_zh"] if lang == "zh" else topic.SRC["body_en"]
        frag = open(os.path.join(d, slug + ".html"), encoding="utf-8").read()
        nrefs[slug] = split_fragment(frag)[2]

    counts = {}
    for _, slug, _ in order:
        for k in topic.ART[slug]["tags"]:
            counts[k] = counts.get(k, 0) + 1
    used = [k for k in order_keys if k in counts]
    missing = [k for k in counts if k not in used]
    if missing:
        raise RuntimeError("tag keys without a label: %s" % sorted(missing))

    name = _hub_name(topic.PREFIX, lang)
    url = BASE + name
    ld = {
        "@context": "https://schema.org",
        "@type": "CollectionPage",
        "name": name_topic,
        "url": url,
        "inLanguage": inlang,
        "about": {"@type": about_type, "name": cond},
        "author": {
            "@type": "Physician",
            "name": "吳正友 Robert Jeng-You Wu",
            "url": BASE,
        },
        "hasPart": [
            {
                "@type": "MedicalWebPage",
                "name": meta[slug]["title"],
                "url": BASE + _page_name(topic.PREFIX, slug, lang),
            }
            for _, slug, _ in order
        ],
    }

    t = _patch_head(
        tpl.text,
        title=hub_copy["title"],
        desc=hub_copy["desc"],
        url=url,
        alt_zh=BASE + _hub_name(topic.PREFIX, "zh"),
        alt_en=BASE + _hub_name(topic.PREFIX, "en"),
        ld=ld,
        zhonly=zhonly,
    )
    t = _patch_lang_switch(
        t, _hub_name(topic.PREFIX, "en" if lang == "zh" else "zh"), lang, zhonly
    )

    t = _sub1(RE_ART_KICKER, t,
              lambda mm: mm.group(1) + esc(topic.KICKER) + mm.group(3), "hub kicker")
    t = _sub1(RE_HUB_H2, t,
              lambda mm: mm.group(1) + esc(name_topic) + mm.group(3)
              + esc(hub_copy["sub"]) + mm.group(5), "hub h2")
    t = _sub1(RE_HUB_INTRO, t,
              lambda mm: mm.group(1) + hub_copy["intro"] + mm.group(3), "hub intro")

    buttons = ['<button class="tagf on" data-tag="">%s <i>%d</i></button>'
               % (esc(tpl.all_label), len(order))]
    for k in used:
        buttons.append(
            '<button class="tagf" data-tag="%s">#%s <i>%d</i></button>'
            % (esca(k), esc(labels[k][lab_i]), counts[k])
        )
    t = _sub1(RE_HUB_TAGC, t,
              lambda mm: mm.group(1) + "".join(buttons) + mm.group(3), "tagbar")

    groups = []
    for si, sec in enumerate(sections):
        rows = ['  <div class="postgroup hnstep">',
                "    <h3><b>%d</b>%s</h3>" % (si + 1, esc(sec[seckey])),
                '    <p class="stepsub">%s</p>' % esc(sec[subkey])]
        for slug in topic.SECTIONS[si]["slugs"]:
            tags = topic.ART[slug]["tags"]
            m = meta[slug]
            rows.append(
                '    <a class="postcard" data-tags="%s" href="%s">'
                % (esca(" ".join(tags)), esca(_page_name(topic.PREFIX, slug, lang)))
            )
            rows.append('      <div class="t">%s</div>' % esc(m["title"]))
            rows.append('      <div class="d">%s</div>' % esc(m["dek"]))
            rows.append('      <div class="m">%s</div>' % esc(tpl.make_card_m(nrefs[slug])))
            rows.append(
                '      <div class="cardtags">%s</div>'
                % "".join("<span>#%s</span>" % esc(labels[k][lab_i]) for k in tags)
            )
            rows.append("    </a>")
        rows.append("  </div>")
        groups.append("\n".join(rows))
    groups_html = "\n".join(groups)

    t = _sub1(RE_HUB_GROUPS, t,
              lambda mm: groups_html + mm.group(2) + hub_copy["closing"] + mm.group(4),
              "postgroups")

    path = os.path.join(out_dir, name)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(t)
    return path
