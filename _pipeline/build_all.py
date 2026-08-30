# -*- coding: utf-8 -*-
"""Build the colon-cancer topic into the working clone, patch the two topic
index pages and the sitemap, mirror everything that changed into the upload
directory, and report the counts plus an internal-link scan."""

import os
import re
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import colon
import topicbuild as tb

REPO = "/home/claude/repo"
UPLOAD = "/home/claude/upload"
ART_TPL = {"zh": os.path.join(REPO, "rc-lars.html"),
           "en": os.path.join(REPO, "rc-lars-en.html")}
HUB_TPL = {"zh": os.path.join(REPO, "rc.html"),
           "en": os.path.join(REPO, "rc-en.html")}

RE_HREF = re.compile(r'href="([^"#?]+\.html)(?:[#?][^"]*)?"')


# ------------------------------------------------------------- topics pages --
def patch_topics(path, card, anchor_href):
    s = open(path, encoding="utf-8").read()
    if 'href="%s"' % card.split('href="', 1)[1].split('"', 1)[0] in s:
        return s, False
    marker = '  <a class="topiccard" href="%s">' % anchor_href
    i = s.index(marker)
    j = s.index("  </a>\n", i) + len("  </a>\n")
    out = s[:j] + card + s[j:]
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(out)
    return out, True


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

    if any(loc("cc.html") in ln for ln in lines):
        return False

    # Chinese: hub beside rc.html, articles after the rc article block.
    lines = insert_after(lines, "rc.html",
                         [sitemap_entry("cc.html", "0.85", topic.DATE)])
    lines = insert_after(
        lines, "rc-late-effects.html",
        [sitemap_entry("cc-%s.html" % s, "0.75", topic.DATE) for s in order])
    # English: hub beside rc-en.html, articles after the rc-en article block.
    lines = insert_after(lines, "rc-en.html",
                         [sitemap_entry("cc-en.html", "0.75", topic.DATE)])
    lines = insert_after(
        lines, "rc-late-effects-en.html",
        [sitemap_entry("cc-%s-en.html" % s, "0.65", topic.DATE) for s in order])

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
    return bad


def main():
    pages = []
    for lang in ("zh", "en"):
        pages += tb.build(colon, lang, ART_TPL[lang], REPO)
        pages.append(tb.build_index(colon, lang, HUB_TPL[lang], REPO))

    changed = []
    for path, card, anchor in (
        (os.path.join(REPO, "topics.html"), colon.TOPIC_CARD_ZH, "rc.html"),
        (os.path.join(REPO, "topics-en.html"), colon.TOPIC_CARD_EN, "rc-en.html"),
    ):
        _, did = patch_topics(path, card, anchor)
        if did:
            changed.append(path)

    smap = os.path.join(REPO, "sitemap.xml")
    if patch_sitemap(smap, colon):
        changed.append(smap)

    if not os.path.isdir(UPLOAD):
        os.makedirs(UPLOAD)
    for p in pages + changed:
        shutil.copy2(p, os.path.join(UPLOAD, os.path.basename(p)))

    total_urls = open(smap, encoding="utf-8").read().count("<url>")
    bad = link_scan(REPO)

    print("pages produced      : %d" % len(pages))
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
