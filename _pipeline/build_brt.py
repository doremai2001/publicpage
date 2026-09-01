# -*- coding: utf-8 -*-
"""Build the breast-radiotherapy topic into the working clone, patch the
topic index page (card + JSON-LD hasPart) and the sitemap, copy the figure
SVGs in, mirror everything new/changed into the upload directory, and report
the counts plus an internal-link scan.

Same driver as build_liver.py.  Differences for brt:

* brt.ZH_ONLY drives the round.  True (round 1): 10 Chinese articles +
  brt.html, no hreflang / English canonical partner / language-switch chip,
  topics.html only, 11 sitemap URLs.  False (round 2): LANGS becomes
  ("zh", "en"), all 22 pages are rewritten with hreflang and the language
  switch back on the Chinese ones, topics-en.html gets its card, and the
  sitemap picks up the 11 English URLs.  Both patchers are idempotent, so
  round 2 leaves topics.html and the already-present sitemap lines alone.
* The baseline for "what changed" is the git HEAD blob of each file, not a
  scratch snapshot -- round 1 is published, so HEAD is what the site is
  serving.  The upload directory is rebuilt each round to hold EXACTLY the
  files whose bytes differ from HEAD (or that HEAD does not have), i.e. the
  set that actually needs uploading; anything already live is dropped from
  it.  In round 1 that was all 33 outputs; in round 2 the 20 SVGs and
  topics.html fall out because they are unchanged.
* the hub shares the prefix (brt.html / brt-en.html), so no _hub_name
  override -- see brt.py.
* the brt sitemap block goes in right after the lv block's last line
  (lv-bridging-en.html), before carc.html.
* disease-topic house priorities: 0.85/0.75 hubs, 0.75/0.65 articles.
* the topics card goes after the liver card (the last one on the pulled
  topics.html).

This builder writes ONLY the brt- article pages and the brt hub, appends one
card to topics.html and one sitemap block -- no other topic's pages are ever
rebuilt or touched (the published pages are the master copies).
"""

import json
import os
import re
import shutil
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import brt
import topicbuild as tb

os.environ["BRT_STAGE"] = brt._STAGE
import stage_brt_figs

REPO = "/home/claude/repo"
UPLOAD = "/home/claude/upload-brt"
FIGS = "/home/claude/brt/figs"
BASE_REF = "HEAD"          # round 1 is published, so HEAD == what is live
ART_TPL = {"zh": os.path.join(REPO, "cc-first-month.html"),
           "en": os.path.join(REPO, "cc-first-month-en.html")}
HUB_TPL = {"zh": os.path.join(REPO, "cc.html"),
           "en": os.path.join(REPO, "cc-en.html")}

LANGS = ("zh",) if brt.ZH_ONLY else ("zh", "en")

# The brt sitemap block is inserted as one run after the lv block's last line.
SM_ANCHOR = "lv-bridging-en.html"

RE_HREF = re.compile(r'href="([^"#?]+\.html)(?:[#?][^"]*)?"')


def head_blob(name):
    """The file's bytes at BASE_REF, or None when BASE_REF does not have it."""
    r = subprocess.run(["git", "-C", REPO, "show", "%s:%s" % (BASE_REF, name)],
                       capture_output=True)
    return r.stdout if r.returncode == 0 else None


def differs_from_head(path):
    b = head_blob(os.path.basename(path))
    if b is None:
        return True
    with open(path, "rb") as fh:
        return fh.read() != b


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
    """Idempotent: a template that already carries the block is left alone."""
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

    have = set()
    for ln in lines:
        m = re.search(re.escape(tb.BASE) + r"([^<]*)</loc>", ln)
        if m:
            have.add(m.group(1))

    block = [sitemap_entry("brt.html", "0.85", topic.DATE)]
    if "en" in LANGS:
        block.append(sitemap_entry("brt-en.html", "0.75", topic.DATE))
    block += [sitemap_entry("brt-%s.html" % s, "0.75", topic.DATE)
              for s in order]
    if "en" in LANGS:
        block += [sitemap_entry("brt-%s-en.html" % s, "0.65", topic.DATE)
                  for s in order]
    block = [b for b in block
             if re.search(re.escape(tb.BASE) + r"([^<]*)</loc>", b).group(1)
             not in have]
    if not block:
        return False

    # round 2 appends its new URLs after the last brt line already present,
    # round 1 puts the whole block after the lv block
    anchor = SM_ANCHOR
    for name in reversed([re.search(re.escape(tb.BASE) + r"([^<]*)</loc>",
                                    ln).group(1)
                          for ln in lines
                          if re.search(re.escape(tb.BASE) + r"([^<]*)</loc>",
                                       ln)]):
        if name == "brt.html" or name.startswith("brt-"):
            anchor = name
            break

    for i, ln in enumerate(lines):
        if loc(anchor) in ln:
            lines = lines[: i + 1] + block + lines[i + 1:]
            break
    else:
        raise RuntimeError("anchor not found in sitemap: %s" % anchor)

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
    stage_brt_figs.STAGE = brt._STAGE
    stage_brt_figs.stage(zh_only=brt.ZH_ONLY)

    pages = []
    for lang in LANGS:
        pages += tb.build(brt, lang, ART_TPL[lang], REPO, zhonly=brt.ZH_ONLY)
        pages.append(tb.build_index(brt, lang, HUB_TPL[lang], REPO,
                                    zhonly=brt.ZH_ONLY))

    block = figure_css()
    for p in pages:
        inject_css(p, block)

    # every SVG (both languages) is copied in this round, so round 2 needs no
    # further file transfer
    svgs = sorted(n for n in os.listdir(FIGS) if n.endswith(".svg"))
    for n in svgs:
        shutil.copy2(os.path.join(FIGS, n), os.path.join(REPO, n))

    targets = [(os.path.join(REPO, "topics.html"),
                brt.TOPIC_CARD_ZH, "liver.html", brt.HASPART_ZH)]
    if "en" in LANGS:
        targets.append((os.path.join(REPO, "topics-en.html"),
                        brt.TOPIC_CARD_EN, "liver-en.html", brt.HASPART_EN))

    changed = []
    for path, card, anchor, hp in targets:
        if patch_topics(path, card, anchor, hp):
            changed.append(path)

    smap = os.path.join(REPO, "sitemap.xml")
    if patch_sitemap(smap, brt):
        changed.append(smap)

    if not os.path.isdir(UPLOAD):
        os.makedirs(UPLOAD)
    shared = ["topics.html", "sitemap.xml"]
    if "en" in LANGS:
        shared.insert(1, "topics-en.html")
    produced = (pages
                + [os.path.join(REPO, n) for n in svgs]
                + [os.path.join(REPO, n) for n in shared])
    # the upload dir holds exactly what differs from what is already live
    to_upload = [p for p in produced if differs_from_head(p)]
    unchanged = [os.path.basename(p) for p in produced
                 if p not in to_upload]
    keep = set(os.path.basename(p) for p in to_upload)
    for n in sorted(os.listdir(UPLOAD)):
        if n not in keep:
            os.remove(os.path.join(UPLOAD, n))
    for p in to_upload:
        shutil.copy2(p, os.path.join(UPLOAD, os.path.basename(p)))

    total_urls = open(smap, encoding="utf-8").read().count("<url>")
    bad = link_scan(REPO)

    print("mode                : %s" % ("ZH-ONLY (round 1)" if brt.ZH_ONLY
                                        else "zh + en"))
    print("pages produced      : %d" % len(pages))
    print("svgs copied         : %d" % len(svgs))
    print("other files changed : %d  (%s)"
          % (len(changed), ", ".join(os.path.basename(c) for c in changed)))
    print("sitemap <url> count : %d" % total_urls)
    print("upload dir files    : %d  (differ from %s; %d produced files "
          "already live and dropped)"
          % (len(os.listdir(UPLOAD)), BASE_REF, len(unchanged)))
    if bad:
        print("broken internal links: %d" % len(bad))
        for a, b in bad:
            print("   %s -> %s" % (a, b))
    else:
        print("broken internal links: 0")


if __name__ == "__main__":
    main()
