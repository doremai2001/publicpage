# -*- coding: utf-8 -*-
"""Build the endometrial-cancer topic into the working clone, patch the two
topic index pages (card + JSON-LD hasPart), the sitemap and the two
pel-who pages, copy the figure SVGs in, and report the counts plus an
internal-link scan.

Same driver as build_esoph.py / build_gbm.py.  Differences for em:
* the staging step (figure insertion + prefix strip) is run here first, so a
  single command produces everything;
* before the first patch, the pulled topics.html / topics-en.html /
  sitemap.xml / pel-who.html / pel-who-en.html are snapshotted to
  /home/claude/endo/prebackup, which the verifier diffs against;
* hub em.html / em-en.html shares the prefix, so no _hub_name override
  (checked: topicbuild._hub_name("em", "zh") == "em.html");
* the em sitemap block goes in right after the gb block's last line
  (gb-recurrence-en.html), before carc.html;
* disease-topic house priorities: 0.85/0.75 hubs, 0.75/0.65 articles;
* the topics pages' card goes after the gbm card (the last one on the pulled
  topics pages, which carry 12 cards) -- em becomes the 13th;
* SPEC.md 修正 20: pel-who.html and pel-who-en.html each get exactly two
  substitutions, from endo.PEL_WHO_EDITS.

THIS ROUND IS LOCAL ONLY: no upload mirror is written, nothing is staged,
committed or pushed.  The builder writes ONLY the em- article pages and the
em hubs, appends one card per topics page, one sitemap block and the four
pel-who substitutions -- no other topic's pages are ever rebuilt or touched
(the published pages are the master copies).
"""

import json
import os
import re
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import endo
import topicbuild as tb

os.environ["EM_STAGE"] = endo._STAGE
import stage_endo_figs

REPO = "/home/claude/repo"
FIGS = "/home/claude/endo/figs"
PRE = "/home/claude/endo/prebackup"
SHARED = ("topics.html", "topics-en.html", "sitemap.xml",
          "pel-who.html", "pel-who-en.html")
ART_TPL = {"zh": os.path.join(REPO, "cc-first-month.html"),
           "en": os.path.join(REPO, "cc-first-month-en.html")}
HUB_TPL = {"zh": os.path.join(REPO, "cc.html"),
           "en": os.path.join(REPO, "cc-en.html")}

# The em sitemap block is inserted as one run after the gb block's last line.
SM_ANCHOR = "gb-recurrence-en.html"
CARD_ANCHOR = {"zh": "gbm.html", "en": "gbm-en.html"}

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
    """SPEC.md 修正 20.  Each replacement must match exactly once."""
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

    if any(loc("em.html") in ln for ln in lines):
        return False

    block = ([sitemap_entry("em.html", "0.85", topic.DATE),
              sitemap_entry("em-en.html", "0.75", topic.DATE)]
             + [sitemap_entry("em-%s.html" % s, "0.75", topic.DATE)
                for s in order]
             + [sitemap_entry("em-%s-en.html" % s, "0.65", topic.DATE)
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

    stage_endo_figs.STAGE = endo._STAGE
    stage_endo_figs.stage()

    pages = []
    for lang in ("zh", "en"):
        pages += tb.build(endo, lang, ART_TPL[lang], REPO)
        pages.append(tb.build_index(endo, lang, HUB_TPL[lang], REPO))

    block = figure_css()
    for p in pages:
        inject_css(p, block)

    svgs = sorted(n for n in os.listdir(FIGS) if n.endswith(".svg"))
    for n in svgs:
        shutil.copy2(os.path.join(FIGS, n), os.path.join(REPO, n))

    changed = []
    for path, card, anchor, hp in (
        (os.path.join(REPO, "topics.html"),
         endo.TOPIC_CARD_ZH, CARD_ANCHOR["zh"], endo.HASPART_ZH),
        (os.path.join(REPO, "topics-en.html"),
         endo.TOPIC_CARD_EN, CARD_ANCHOR["en"], endo.HASPART_EN),
    ):
        if patch_topics(path, card, anchor, hp):
            changed.append(path)

    smap = os.path.join(REPO, "sitemap.xml")
    if patch_sitemap(smap, endo):
        changed.append(smap)

    for name, edits in endo.PEL_WHO_EDITS.items():
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
