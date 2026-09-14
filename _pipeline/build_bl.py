# -*- coding: utf-8 -*-
"""Build the bladder-cancer topic into the working clone, patch the two
topic index pages (card + JSON-LD hasPart), the sitemap and the two
pel-who pages, copy the figure SVGs in, and report the counts plus an
internal-link scan.

Same driver as build_bt.py / build_endo.py.  Differences for bl:
* the staging step (figure insertion + prefix/suffix strip) is run here
  first, so a single command produces everything;
* before the first patch, the pulled topics.html / topics-en.html /
  sitemap.xml / pel-who.html / pel-who-en.html are snapshotted to
  /home/claude/bl/prebackup, which the verifier diffs against;
* hub bl.html / bl-en.html shares the prefix, so no _hub_name override
  (checked: topicbuild._hub_name("bl", "zh") == "bl.html");
* the bl sitemap block goes in right after the bt block's last line
  (bt-nf2-en.html), before carc.html;
* disease-topic house priorities: 0.85/0.75 hubs, 0.75/0.65 articles;
* the topics pages' card goes after the bt card (the last one on the pulled
  topics pages, which carry 14 cards) -- bl becomes the 15th;
* pel-who.html gets three substitutions and pel-who-en.html two, from
  bl.PEL_WHO_EDITS -- the sentences that have promised this topic since the
  pelvic-radiotherapy round.  No <a> is added: pel-who's body carries zero
  in-body site links and every pointer on it is an unlinked title (re-checked
  2026-09-14, not inherited from the previous round's note).

THIS ROUND IS LOCAL ONLY: no upload mirror is written, nothing is staged,
committed or pushed.  The builder writes ONLY the bl- article pages and the
bl hubs, appends one card per topics page, one sitemap block and the five
pel-who substitutions -- no other topic's pages are ever rebuilt or touched
(the published pages are the master copies).
"""

import json
import os
import re
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import bl
import topicbuild as tb

os.environ["BL_STAGE"] = bl._STAGE
import stage_bl_figs

REPO = "/home/claude/repo"
FIGS = "/home/claude/bl/figs"
PRE = "/home/claude/bl/prebackup"
SHARED = ("topics.html", "topics-en.html", "sitemap.xml",
          "pel-who.html", "pel-who-en.html")
ART_TPL = {"zh": os.path.join(REPO, "cc-first-month.html"),
           "en": os.path.join(REPO, "cc-first-month-en.html")}
HUB_TPL = {"zh": os.path.join(REPO, "cc.html"),
           "en": os.path.join(REPO, "cc-en.html")}

# The bl sitemap block is inserted as one run after the bt block's last line.
SM_ANCHOR = "bt-nf2-en.html"
CARD_ANCHOR = {"zh": "bt.html", "en": "bt-en.html"}

RE_HREF = re.compile(r'href="([^"#?]+\.html)(?:[#?][^"]*)?"')


# ------------------------------------------------------- article-figure css --
def figure_css():
    """The .article-figure block, verbatim from hn-first-week.html: from the
    'article figures' comment up to (not including) the next comment."""
    h = open(os.path.join(REPO, "hn-first-week.html"), encoding="utf-8").read()
    a = h.index("/* ---------- article figures ---------- */")
    b = h.find("/* ----------", a + 10)
    e = h.index("</style>", a)
    if b < 0 or b > e:
        b = e
    return h[a:b]


def inject_css(path, block):
    """Idempotent: a template that already carries the block is left alone."""
    s = open(path, encoding="utf-8").read()
    if ".article-figure{" in s:
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


# ------------------------------------------------------------ pel-who chore --
def patch_pel_who(path, edits):
    """The pel-who chore.  Each replacement must match exactly once."""
    s = open(path, encoding="utf-8").read()
    done = 0
    for old, new in edits:
        if old not in s:
            if new in s:
                continue            # already applied
            raise RuntimeError("pel-who anchor not found in %s: %r"
                               % (os.path.basename(path), old[:40]))
        if s.count(old) != 1:
            raise RuntimeError("pel-who anchor not unique in %s: %r"
                               % (os.path.basename(path), old[:40]))
        s = s.replace(old, new)
        done += 1
    if not done:
        return False
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

    if any(loc("bl.html") in ln for ln in lines):
        return False

    block = ([sitemap_entry("bl.html", "0.85", topic.DATE),
              sitemap_entry("bl-en.html", "0.75", topic.DATE)]
             + [sitemap_entry("bl-%s.html" % s, "0.75", topic.DATE)
                for s in order]
             + [sitemap_entry("bl-%s-en.html" % s, "0.65", topic.DATE)
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
    # snapshot the shared files as pulled, once, before any patch -- the
    # verifier diffs the patched versions against these
    if not os.path.isdir(PRE):
        os.makedirs(PRE)
        for n in SHARED:
            shutil.copy2(os.path.join(REPO, n), os.path.join(PRE, n))

    stage_bl_figs.STAGE = bl._STAGE
    stage_bl_figs.stage()

    pages = []
    for lang in ("zh", "en"):
        pages += tb.build(bl, lang, ART_TPL[lang], REPO)
        pages.append(tb.build_index(bl, lang, HUB_TPL[lang], REPO))

    block = figure_css()
    for p in pages:
        inject_css(p, block)

    svgs = sorted(n for n in os.listdir(FIGS) if n.endswith(".svg"))
    for n in svgs:
        shutil.copy2(os.path.join(FIGS, n), os.path.join(REPO, n))

    changed = []
    for path, card, anchor, hp in (
        (os.path.join(REPO, "topics.html"),
         bl.TOPIC_CARD_ZH, CARD_ANCHOR["zh"], bl.HASPART_ZH),
        (os.path.join(REPO, "topics-en.html"),
         bl.TOPIC_CARD_EN, CARD_ANCHOR["en"], bl.HASPART_EN),
    ):
        if patch_topics(path, card, anchor, hp):
            changed.append(path)

    smap = os.path.join(REPO, "sitemap.xml")
    if patch_sitemap(smap, bl):
        changed.append(smap)

    for name, edits in bl.PEL_WHO_EDITS.items():
        if patch_pel_who(os.path.join(REPO, name), edits):
            changed.append(os.path.join(REPO, name))

    total_urls = open(smap, encoding="utf-8").read().count("<url>")
    bad = link_scan(REPO)

    print("pages produced      : %d" % len(pages))
    print("svgs copied         : %d" % len(svgs))
    print("other files changed : %d  (%s)"
          % (len(changed), ", ".join(os.path.basename(c) for c in changed)))
    print("sitemap <url> count : %d" % total_urls)
    if bad:
        print("broken internal links: %d" % len(bad))
        for a, b in bad:
            print("   %s -> %s" % (a, b))
    else:
        print("broken internal links: 0")


if __name__ == "__main__":
    main()
