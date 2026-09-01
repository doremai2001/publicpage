# -*- coding: utf-8 -*-
"""Build the next-generation-therapy topic into the working clone, patch the
two topic index pages (card + JSON-LD hasPart) and the sitemap, copy the
figure SVGs in, mirror everything new/changed into the upload directory, and
report the counts plus an internal-link scan.

Same driver as build_breast.py; the additions this topic needs are
(a) the article-figure CSS block, copied verbatim out of hn-first-week.html
    and injected into all 14 generated pages' <style> (the cc templates
    pre-date the figure pattern), and
(b) the 20 figure SVGs themselves, and
(c) a hasPart entry appended to each topics page's CollectionPage JSON-LD.
"""

import json
import os
import re
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import nextgen
import topicbuild as tb

REPO = "/home/claude/repo"
UPLOAD = "/home/claude/upload-nextgen"
FIGS = "/home/claude/nextgen/figs"
ART_TPL = {"zh": os.path.join(REPO, "cc-first-month.html"),
           "en": os.path.join(REPO, "cc-first-month-en.html")}
HUB_TPL = {"zh": os.path.join(REPO, "cc.html"),
           "en": os.path.join(REPO, "cc-en.html")}

# Where the new sitemap entries go: immediately after the breast ones, keeping
# the file's existing hub-block / article-block grouping.
SM_ANCHORS = {
    "hub_zh": "bc.html",
    "arts_zh": "bc-metastatic-outlook.html",
    "hub_en": "bc-en.html",
    "arts_en": "bc-metastatic-outlook-en.html",
}

RE_HREF = re.compile(r'href="([^"#?]+\.html)(?:[#?][^"]*)?"')


# ------------------------------------------------------- article-figure css --
def figure_css():
    """The .article-figure block, verbatim from hn-first-week.html: from the
    'article figures' comment up to (not including) the next comment."""
    h = open(os.path.join(REPO, "hn-first-week.html"), encoding="utf-8").read()
    a = h.index("/* ---------- article figures ---------- */")
    # the block is the last one in that file's <style> now, so stop at the
    # next section comment if there is one and at </style> otherwise
    b = h.find("/* ----------", a + 10)
    e = h.index("</style>", a)
    if b < 0 or b > e:
        b = e
    return h[a:b]


def inject_css(path, block):
    s = open(path, encoding="utf-8").read()
    assert ".article-figure{" not in s, path
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

    def insert_after(lines, name, block):
        for i, ln in enumerate(lines):
            if loc(name) in ln:
                return lines[: i + 1] + block + lines[i + 1:]
        raise RuntimeError("anchor not found in sitemap: %s" % name)

    if any(loc("nt.html") in ln for ln in lines):
        return False

    lines = insert_after(lines, SM_ANCHORS["hub_zh"],
                         [sitemap_entry("nt.html", "0.85", topic.DATE)])
    lines = insert_after(
        lines, SM_ANCHORS["arts_zh"],
        [sitemap_entry("nt-%s.html" % s, "0.75", topic.DATE) for s in order])
    lines = insert_after(lines, SM_ANCHORS["hub_en"],
                         [sitemap_entry("nt-en.html", "0.75", topic.DATE)])
    lines = insert_after(
        lines, SM_ANCHORS["arts_en"],
        [sitemap_entry("nt-%s-en.html" % s, "0.65", topic.DATE) for s in order])

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
        # figure image targets
        for target in re.findall(r'(?:src|srcset)="([^"]+\.svg)"', s):
            if target not in files:
                bad.append((name, target))
    return bad


def main():
    pages = []
    for lang in ("zh", "en"):
        pages += tb.build(nextgen, lang, ART_TPL[lang], REPO)
        pages.append(tb.build_index(nextgen, lang, HUB_TPL[lang], REPO))

    block = figure_css()
    for p in pages:
        inject_css(p, block)

    svgs = sorted(n for n in os.listdir(FIGS) if n.endswith(".svg"))
    for n in svgs:
        shutil.copy2(os.path.join(FIGS, n), os.path.join(REPO, n))

    changed = []
    for path, card, anchor, hp in (
        (os.path.join(REPO, "topics.html"),
         nextgen.TOPIC_CARD_ZH, "bc.html", nextgen.HASPART_ZH),
        (os.path.join(REPO, "topics-en.html"),
         nextgen.TOPIC_CARD_EN, "bc-en.html", nextgen.HASPART_EN),
    ):
        if patch_topics(path, card, anchor, hp):
            changed.append(path)

    smap = os.path.join(REPO, "sitemap.xml")
    if patch_sitemap(smap, nextgen):
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
