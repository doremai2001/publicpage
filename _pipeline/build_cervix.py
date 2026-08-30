# -*- coding: utf-8 -*-
"""Build the cervical-cancer topic into the working clone, patch the two topic
index pages (card + JSON-LD hasPart) and the sitemap, copy the figure SVGs in,
mirror everything new/changed into the upload directory, and report the counts
plus an internal-link scan.

Same driver as build_nextgen.py.  Differences for cx:
* the sitemap has since been regrouped per topic ([hub zh, hub en, arts zh,
  arts en] contiguous blocks); the whole cx block goes in right after the nt
  block's last line (nt-bnct-en.html), before bc.html;
* disease-topic house priorities: 0.85/0.75 hubs, 0.75/0.65 articles;
* the topics pages' card goes after the lung-cancer card (the nt card the
  original instructions anchored on no longer lives on topics.html).
"""

import json
import os
import re
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import cervix
import topicbuild as tb

REPO = "/home/claude/repo"
UPLOAD = "/home/claude/upload-cervix"
FIGS = "/home/claude/cervix/figs"
ART_TPL = {"zh": os.path.join(REPO, "cc-first-month.html"),
           "en": os.path.join(REPO, "cc-first-month-en.html")}
HUB_TPL = {"zh": os.path.join(REPO, "cc.html"),
           "en": os.path.join(REPO, "cc-en.html")}

# The cx sitemap block is inserted as one run after the nt block's last line.
SM_ANCHOR = "nt-bnct-en.html"

RE_HREF = re.compile(r'href="([^"#?]+\.html)(?:[#?][^"]*)?"')


# ------------------------------------------------------- article-figure css --
def figure_css():
    """The .article-figure block, verbatim from hn-first-week.html: from the
    'article figures' comment up to (not including) the next comment."""
    h = open(os.path.join(REPO, "hn-first-week.html"), encoding="utf-8").read()
    a = h.index("/* ---------- article figures ---------- */")
    b = h.index("/* ----------", a + 10)
    return h[a:b]


def inject_css(path, block):
    s = open(path, encoding="utf-8").read()
    if ".article-figure{" in s:      # template already carries the block
        return
    i = s.index("</style>")
    s = s[:i] + block + s[i:]
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(s)


# ------------------------------------------------------------- topics pages --
def patch_topics(path, card, anchor_href, haspart):
    s = open(path, encoding="utf-8").read()
    if 'href="%s"' % card.split('href="', 1)[1].split('"', 1)[0] in s:
        return False
    marker = '  <a class="topiccard" href="%s">' % anchor_href
    i = s.index(marker)
    j = s.index("  </a>\n", i) + len("  </a>\n")
    s = s[:j] + card + s[j:]
    # append the new hub to the CollectionPage's hasPart, matching the
    # existing entries' compact-JSON formatting exactly
    entry = json.dumps(haspart, ensure_ascii=False, separators=(",", ":"))
    old = '"hasPart":['
    k = s.index(old) + len(old)
    end = s.index("]", k)
    s = s[:end] + "," + entry + s[end:]
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(s)
    return True


# ------------------------------------------------------------------ sitemap --
def sitemap_entry(name, prio, date):
    return ('  <url><loc>%s%s</loc><lastmod>%s</lastmod>'
            '<changefreq>monthly</changefreq><priority>%s</priority></url>\n'
            % (tb.BASE, name, date, prio))


def patch_sitemap(path, topic):
    lines = open(path, encoding="utf-8").read().splitlines(True)
    order = [slug for sec in topic.SECTIONS for slug in sec["slugs"]]

    def loc(name):
        return "<loc>%s%s</loc>" % (tb.BASE, name)

    if any(loc("cx.html") in ln for ln in lines):
        return False

    block = ([sitemap_entry("cx.html", "0.85", topic.DATE),
              sitemap_entry("cx-en.html", "0.75", topic.DATE)]
             + [sitemap_entry("cx-%s.html" % s, "0.75", topic.DATE)
                for s in order]
             + [sitemap_entry("cx-%s-en.html" % s, "0.65", topic.DATE)
                for s in order])

    for i, ln in enumerate(lines):
        if loc(SM_ANCHOR) in ln:
            lines = lines[: i + 1] + block + lines[i + 1:]
            break
    else:
        raise RuntimeError("anchor not found in sitemap: %s" % SM_ANCHOR)

    with open(path, "w", encoding="utf-8") as fh:
        fh.write("".join(lines))
    return True


# ------------------------------------------------------------------- linkscan
def link_scan(root):
    files = set(os.listdir(root))
    bad = []
    for name in sorted(files):
        if not name.endswith(".html"):
            continue
        s = open(os.path.join(root, name), encoding="utf-8").read()
        for target in RE_HREF.findall(s):
            if "://" in target or target.startswith("/"):
                continue
            if target not in files:
                bad.append((name, target))
        for target in re.findall(r'(?:src|srcset)="([^"]+\.svg)"', s):
            if target not in files:
                bad.append((name, target))
    return bad


def main():
    pages = []
    for lang in ("zh", "en"):
        pages += tb.build(cervix, lang, ART_TPL[lang], REPO)
        pages.append(tb.build_index(cervix, lang, HUB_TPL[lang], REPO))

    block = figure_css()
    for p in pages:
        inject_css(p, block)

    svgs = sorted(n for n in os.listdir(FIGS) if n.endswith(".svg"))
    for n in svgs:
        shutil.copy2(os.path.join(FIGS, n), os.path.join(REPO, n))

    changed = []
    for path, card, anchor, hp in (
        (os.path.join(REPO, "topics.html"),
         cervix.TOPIC_CARD_ZH, "lc.html", cervix.HASPART_ZH),
        (os.path.join(REPO, "topics-en.html"),
         cervix.TOPIC_CARD_EN, "lc-en.html", cervix.HASPART_EN),
    ):
        if patch_topics(path, card, anchor, hp):
            changed.append(path)

    smap = os.path.join(REPO, "sitemap.xml")
    if patch_sitemap(smap, cervix):
        changed.append(smap)

    if not os.path.isdir(UPLOAD):
        os.makedirs(UPLOAD)
    for p in (pages
              + [os.path.join(REPO, n) for n in svgs]
              + [os.path.join(REPO, n) for n in
                 ("topics.html", "topics-en.html", "sitemap.xml")]):
        shutil.copy2(p, os.path.join(UPLOAD, os.path.basename(p)))

    total_urls = open(smap, encoding="utf-8").read().count("<url>")
    bad = link_scan(REPO)

    print("pages produced      : %d" % len(pages))
    print("svgs copied         : %d" % len(svgs))
    print("other files changed : %d  (%s)"
          % (len(changed), ", ".join(os.path.basename(c) for c in changed)))
    print("sitemap <url> count : %d" % total_urls)
    print("upload dir files    : %d" % len(os.listdir(UPLOAD)))
    if bad:
        print("broken internal links: %d" % len(bad))
        for a, b in bad:
            print("   %s -> %s" % (a, b))
    else:
        print("broken internal links: 0")


if __name__ == "__main__":
    main()
