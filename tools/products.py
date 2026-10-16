# Generates the Shelf product pages, compare pages, home family section and sitemap.
# python3 tools/products.py   (BASE switches to https://convoshelf.com/ once DNS is live)
import json, os, html, re, datetime
BASE = "https://chumzygood.github.io/convoshelf/"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TODAY = datetime.date.today().isoformat()
E = html.escape
P = [
 dict(slug="x-bookmarks", name="X Bookmarks Shelf", tag="xbookmarks", color="#0f172a", acc="#38bdf8",
  title="X Bookmarks Shelf: search, folders and export for X (Twitter) bookmarks",
  desc="Search your X bookmarks, sort them into folders, and export them to Markdown, CSV or JSON. Keeps posts that get deleted. Local only, free plan, Pro $4.99 once.",
  h1="Search and sort your X bookmarks.",
  lead="X lets you bookmark a post but gives you no search, and bookmark folders need Premium. X Bookmarks Shelf saves each bookmark you scroll past into a library in your browser, with folders, tags and full-text search.",
  cards=[("Full-text search","Type “postgres” and get the tip you saved in March. Searches post text, author, tags and your notes."),("Folders, no Premium","Unlimited folders and subfolders, tags and pins. Nothing to do with X's paid folders."),("Keeps deleted posts","If the author deletes a post, your copy stays, marked “kept”."),("Export","Copy any post as Markdown, free. Pro exports everything to Markdown, Obsidian/Notion Markdown, CSV, JSON or HTML."),("Bulk un-bookmark","Pro: tick 200 posts and remove them from X's bookmarks, one every 1.5 seconds."),("Capture all","Press Capture all and it scrolls your bookmarks to the end for you.")],
  free=["Capture as you scroll, or Capture all","Full-text search","Unlimited folders and subfolders","Tags and pins","Keeps deleted posts","Copy a post as Markdown","Group by author","Dark mode, shortcut, backup"],
  pro=["Export all: Markdown, Obsidian, CSV, JSON, HTML","Notes on posts","Filters: author, date, media, deleted","Bulk move, tag, pin","Bulk un-bookmark on X","Auto-folders by author","Folder colors"],
  faq=[("Does X Bookmarks Shelf need my X password or an API key?","No. It reads the bookmarks page you already have open in Chrome. No login, no API key, no server."),("Where are my bookmarks stored?","In your browser's local storage on your computer. Nothing is uploaded. You can download a JSON backup any time."),("Can I export my X bookmarks to CSV or Notion?","Yes, with Pro ($4.99 once): Markdown, Obsidian/Notion-ready Markdown with front matter, CSV, JSON and HTML."),("What happens when a bookmarked post is deleted?","Your saved copy stays in the library, marked “kept”."),("Is Pro a subscription?","No. Pro is a single $4.99 payment.")],
  comp=[("X's built-in bookmarks","No search, no export, folders need Premium","Search, folders, tags and export on the free plan"),("Twillot","Many tools in one, subscription and AI upsells, mixed ratings","One job: bookmarks. Pro is $4.99 once"),("X Bookmark Manager & Exporter","Monthly subscription for search and delete","Search is free; bulk delete is in the $4.99 one-time Pro"),("Open-source scripts on GitHub","Load-unpacked, no updates through the store","Installs from the Chrome Web Store (once listed), self-check in the popup")]),
 dict(slug="reddit-saved", name="Saved Shelf", tag="savedshelf", color="#7c2d12", acc="#fb923c",
  title="Saved Shelf for Reddit: search, folders and export for saved posts",
  desc="Search your saved Reddit posts and comments, sort them into folders, and keep a copy past the 1,000-item cap. Local only, free plan, Pro $4.99 once.",
  h1="Search your saved Reddit posts.",
  lead="Reddit keeps saved posts in one long list with no search, and only shows the newest 1,000. Saved Shelf imports that list into your browser with one click, so you can search it and sort it into folders.",
  cards=[("One-click import","Open your saved page and press Capture all. Posts and comments come in 100 at a time, new Reddit or old."),("Search inside posts","Search titles, post text, comment text, subreddits and tags."),("Past the 1,000 cap","Your library keeps items after you unsave them, so Reddit's cap stops mattering."),("Folders and subreddits","Unlimited folders and tags, or group by subreddit. Pro makes one folder per subreddit for you."),("Export","Copy any item as Markdown, free. Pro exports to Markdown, CSV, JSON or HTML."),("Bulk unsave","Pro: unsave many items on Reddit after they're safe in your library.")],
  free=["One-click import of your saved list","Search posts and comments","Unlimited folders and subfolders","Tags and pins","Group by subreddit","Keeps items after you unsave","Copy as Markdown","Dark mode, shortcut, backup"],
  pro=["Export all: Markdown, CSV, JSON, HTML","Notes","Filters: subreddit, author, date, comments, hide NSFW","Bulk move, tag, pin","Bulk unsave on Reddit","Auto-folders by subreddit","Folder colors"],
  faq=[("How do I search my saved posts on Reddit?","Install Saved Shelf, open your saved page on reddit.com, press Capture all in the 📌 panel, then use the Search tab."),("Does it get around the 1,000 saved-post limit?","Reddit only shows your newest 1,000 saved items. Saved Shelf keeps everything it has imported, so after you unsave old items to make room, your copies stay searchable."),("Do I need a Reddit API key?","No. It reads your own saved list while you're signed in to reddit.com in Chrome."),("Is Saved Shelf made by Reddit?","No. It's an independent tool and isn't affiliated with Reddit, Inc."),("Is Pro a subscription?","No. Pro is a single $4.99 payment.")],
  comp=[("Reddit's saved list","No search, no folders, newest 1,000 only","Search, folders, tags, keeps items past the cap"),("savedposts.app","Free tier capped at 3 folders and 500 posts, cloud sync","Unlimited folders and items on the free plan, nothing uploaded"),("Readdit Later","Paid for unlimited use, AI upsell","Unlimited free plan, Pro $4.99 once"),("Reddit Saved Post Organizer","Extension with a time-limited paid unlock","Free plan with no time limit")]),
 dict(slug="watch-later", name="Watch Later Shelf", tag="watchlater", color="#450a0a", acc="#f87171",
  title="Watch Later Shelf: search, filter and bulk-clean YouTube Watch Later",
  desc="Search YouTube Watch Later by title or channel, filter by length or watched, find duplicates and bulk-remove videos with no monthly cap. Pro $4.99 once.",
  h1="Search and clean up YouTube Watch Later.",
  lead="Watch Later has no search, no filters and no way to remove more than one video at a time. Watch Later Shelf indexes the list as you scroll, then lets you search it, tag it and clear out what you've watched.",
  cards=[("Search Watch Later","Find a video by title, channel or your own tags."),("Filters","Length, channel, watched, started, Shorts and unavailable videos. Filters are Pro."),("Remove watched","Pro: filter Show → Watched, Select all, Remove. No monthly removal cap."),("Duplicate finder","Pro: the same video saved twice shows up as a pair."),("Folders on top","Unlimited local folders and tags on top of YouTube's list. Pro makes one per channel."),("Export","Copy a video link as Markdown, free. Pro exports CSV, JSON, Markdown or HTML.")],
  free=["Index Watch Later or any playlist","Search by title, channel, tag","Unlimited folders and tags","Pins","Group by channel","Watched, Shorts and unavailable flags","Copy as Markdown","Dark mode, shortcut, backup"],
  pro=["Bulk remove, no monthly cap","Remove watched in three clicks","Duplicate finder","Filters: length, channel, watched, Shorts","Auto-folders by channel","Export CSV, JSON, Markdown, HTML","Notes, folder colors"],
  faq=[("How do I search my Watch Later list?","Install Watch Later Shelf, open youtube.com/playlist?list=WL, press Capture all in the 🎞 panel, then use the Search tab."),("How do I delete all watched videos from Watch Later?","With Pro: in Search, set Show to Watched, press Select all, then Remove from playlist. Videos go one at a time, about 1.3 seconds each."),("Is there a removal limit?","No. Pro has no monthly cap."),("Does it work on other playlists?","Yes, any playlist page you can open."),("Is Pro a subscription?","No. Pro is a single $4.99 payment.")],
  comp=[("YouTube's Watch Later","No search, no filters, remove one video at a time, 5,000 cap","Search, filters, bulk remove"),("Watch Later Tidy","Subscription Pro; 1,000 removals per 30 days for new installs","$4.99 once, no removal cap"),("YouTube Watch Later Organizer","Manual scrolling, low ratings","Capture all scrolls for you; folders and tags"),("PocketTube","Organizes channels and playlists, not the videos inside","Works on the videos in Watch Later")]),
]
FAMILY = [("", "ConvoShelf", "Folders, search and export for ChatGPT, Claude, Gemini and Grok chats.")] + [(p["slug"] + "/", p["name"] + (" for Reddit" if p["slug"] == "reddit-saved" else ""), p["desc"].split(". ")[0] + ".") for p in P]
CSS = """body{margin:0;font:17px/1.6 system-ui,-apple-system,"Segoe UI",sans-serif;color:#0f172a}a{color:#4f46e5}header,main,footer{max-width:980px;margin:0 auto;padding:0 20px}header{display:flex;align-items:center;gap:10px;padding-top:18px}header nav{margin-left:auto;display:flex;gap:16px;font-size:15px;flex-wrap:wrap}header img{width:32px}.hero{padding:40px 0 10px}h1{font-size:40px;line-height:1.15;margin:0 0 12px}.cta{display:inline-block;background:var(--c);color:#fff;padding:12px 20px;border-radius:10px;text-decoration:none;font-weight:600}.muted{color:#64748b}img.shot,video{width:100%;height:auto;border:1px solid #e2e8f0;border-radius:12px;margin:24px 0;display:block}table{border-collapse:collapse;width:100%;font-size:15px}td,th{border-bottom:1px solid #e2e8f0;padding:8px;text-align:left;vertical-align:top}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:20px}.card{border:1px solid #e2e8f0;border-radius:12px;padding:16px 18px}.plans{display:grid;grid-template-columns:1fr 1fr;gap:20px}@media(max-width:700px){.plans{grid-template-columns:1fr}h1{font-size:32px}}.plan{border:1px solid #e2e8f0;border-radius:14px;padding:18px 22px}.plan.pro{border:2px solid var(--a)}footer{padding:40px 20px;font-size:14px;color:#64748b}h2{margin-top:44px}details{border-bottom:1px solid #e2e8f0;padding:10px 0}summary{font-weight:600;cursor:pointer}"""
def head(title, desc, url, img, extra_ld, color, icon):
    return f"""<!doctype html><html lang=en><head><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1"><title>{E(title)}</title><meta name=description content="{E(desc)}"><link rel=canonical href="{url}"><link rel=icon href="{icon}"><meta name=theme-color content="{color}">
<meta property=og:type content=website><meta property=og:site_name content=ConvoShelf><meta property=og:url content="{url}"><meta property=og:title content="{E(title)}"><meta property=og:description content="{E(desc)}"><meta property=og:image content="{img}"><meta property=og:image:width content=1200><meta property=og:image:height content=630>
<meta name=twitter:card content=summary_large_image><meta name=twitter:title content="{E(title)}"><meta name=twitter:description content="{E(desc)}"><meta name=twitter:image content="{img}">
""" + "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>\n' for x in extra_ld)
def crumbs(items): return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(items)]}
def nav(p): return f'<header><img src="icon.png" alt=""><b><a href="../" style="color:inherit;text-decoration:none">ConvoShelf</a> / <a href="./" style="color:inherit;text-decoration:none">{E(p["name"])}</a></b><nav><a href="./#features">Features</a><a href="./#pricing">Pricing</a><a href="./compare/">Compare</a><a href="./#faq">FAQ</a><a href="../#family">All tools</a></nav></header>'
def foot(p): return f'<footer>{E(p["name"])} · Support: <a href="mailto:toolshed+{p["tag"]}@mail.grokbot.com">toolshed+{p["tag"]}@mail.grokbot.com</a> · <a href="../privacy.html">Privacy</a> · <a href="../">ConvoShelf family</a><br>{ {"x-bookmarks":"Not affiliated with X Corp.","reddit-saved":"Saved Shelf is an independent tool, not made by or affiliated with Reddit, Inc.","watch-later":"Not affiliated with YouTube or Google. YouTube is a trademark of Google LLC."}[p["slug"]] }</footer></body></html>'
for p in P:
    d = os.path.join(ROOT, p["slug"]); os.makedirs(d + "/compare", exist_ok=True)
    url = BASE + p["slug"] + "/"; img = url + "og.jpg"
    app = {"@context": "https://schema.org", "@type": "SoftwareApplication", "name": p["name"], "applicationCategory": "BrowserApplication", "operatingSystem": "Google Chrome (desktop)", "softwareVersion": "1.0.0", "description": p["desc"], "url": url, "image": url + "shot-library.png",
           "offers": [{"@type": "Offer", "name": "Free", "price": "0", "priceCurrency": "USD"}, {"@type": "Offer", "name": "Pro (one-time)", "price": "4.99", "priceCurrency": "USD"}]}
    faq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p["faq"]]}
    vid = {"@context": "https://schema.org", "@type": "VideoObject", "name": p["name"] + " demo", "description": "Short demo: library, folders, search and export in " + p["name"] + ".", "thumbnailUrl": url + "demo-poster.jpg", "contentUrl": url + "demo.mp4", "uploadDate": TODAY + "T00:00:00-04:00"}
    body = f"""<style>:root{{--c:{p['color']};--a:{p['acc']}}}{CSS}</style></head><body>
{nav(p)}
<main><section class=hero><h1>{E(p['h1'])}</h1><p>{E(p['lead'])}</p><a class=cta href="#install">Add to Chrome, free</a> <span class=muted>&nbsp;Chrome Web Store listing coming soon</span></section>
<video controls muted playsinline preload=none poster="demo-poster.jpg" width=1280 height=720><source src="demo.mp4" type="video/mp4">Your browser can't play this video. <a href="demo.mp4">Download the demo</a>.</video>
<h2 id=features>What it does</h2><div class=grid>{''.join(f'<div class=card><b>{E(t)}</b><br>{E(x)}</div>' for t, x in p['cards'])}</div>
<img class=shot src="shot-search.png" alt="{E(p['name'])} search panel" loading=lazy width=1280 height=800>
<h2 id=pricing>Pricing</h2><div class=plans><div class=plan><h3>Free</h3><ul>{''.join(f'<li>{E(x)}</li>' for x in p['free'])}</ul></div><div class="plan pro"><h3>Pro, $4.99 once</h3><ul>{''.join(f'<li>{E(x)}</li>' for x in p['pro'])}</ul></div></div>
<p class=muted>Pro is a single payment, no subscription. Your license key unlocks it on your devices.</p>
<img class=shot src="shot-folders.png" alt="{E(p['name'])} folders" loading=lazy width=1280 height=800>
<h2 id=install>Install</h2><p>{E(p['name'])} is waiting for Chrome Web Store review. This page will link to the listing as soon as it's live. Questions: <a href="mailto:toolshed+{p['tag']}@mail.grokbot.com">toolshed+{p['tag']}@mail.grokbot.com</a>.</p>
<h2 id=faq>FAQ</h2>{''.join(f'<details><summary>{E(q)}</summary><p>{E(a)}</p></details>' for q, a in p['faq'])}
<p><a href="compare/">How {E(p['name'])} compares to the alternatives →</a></p></main>
{foot(p)}"""
    open(d + "/index.html", "w").write(head(p["title"], p["desc"], url, img, [app, faq, vid, crumbs([("ConvoShelf", BASE), (p["name"], url)])], p["color"], "../favicon.png") + body)
    curl = url + "compare/"; ct = f"{p['name']} vs alternatives: " + ", ".join(c[0] for c in p["comp"][:3])
    cdesc = f"How {p['name']} compares with " + ", ".join(c[0] for c in p["comp"]) + ". Free plan, Pro $4.99 once, local only."
    cbody = f"""<style>:root{{--c:{p['color']};--a:{p['acc']}}}{CSS}</style></head><body>
{nav(p).replace('href="./', 'href="../').replace('href="../"', 'href="../../"').replace('src="icon.png"', 'src="../icon.png"').replace('href="../#family"', 'href="../../#family"')}
<main><h1>{E(p['name'])} vs the alternatives</h1><p class=muted>Checked October 2026 from public store pages. Prices and limits change; tell us at toolshed+{p['tag']}@mail.grokbot.com if something here is out of date.</p>
<table><tr><th>Option</th><th>What you get</th><th>{E(p['name'])}</th></tr>{''.join(f'<tr><td><b>{E(a)}</b></td><td>{E(b)}</td><td>{E(c)}</td></tr>' for a, b, c in p['comp'])}</table>
<h2>Where {E(p['name'])} is weaker</h2><p>It only sees what the site has shown in your browser, so you need to open your list (or press Capture all) before items appear. If the site redesigns its page, capture can stop until we ship an update; the popup's self-check tells you when that happens.</p>
<p><a class=cta href="../">See {E(p['name'])}</a></p></main>
{foot(p).replace('href="../', 'href="../../')}"""
    open(d + "/compare/index.html", "w").write(head(ct, cdesc, curl, img, [{"@context": "https://schema.org", "@type": "WebPage", "name": ct, "url": curl, "description": cdesc}, crumbs([("ConvoShelf", BASE), (p["name"], url), ("Compare", curl)])], p["color"], "../../favicon.png") + cbody)
# Home: product family section (idempotent, between markers)
idx = open(ROOT + "/index.html").read()
fam = '<!--family--><h2 id=family>The Shelf family</h2><p class=muted>Same idea for each list: folders, search and export, kept in your browser. Free plan, Pro $4.99 once per tool.</p><div class=grid>' + "".join(f'<a class=card href="{s}" style="text-decoration:none;color:inherit"><b>{E(n)}</b><br>{E(t)}</a>' for s, n, t in FAMILY) + '</div><!--/family-->'
idx = re.sub(r"<!--family-->.*?<!--/family-->", "", idx, flags=re.S).replace("</main>", fam + "</main>", 1)
idx = idx.replace('<a href="faq.html">FAQ</a></nav>', '<a href="faq.html">FAQ</a><a href="#family">All tools</a></nav>') if '#family">All tools' not in idx else idx
open(ROOT + "/index.html", "w").write(idx)
# ConvoShelf home + faq/compare SEO: OG/Twitter cards, schema, demo video (idempotent, between markers)
FAQS = [("Where are my chats stored?", "In your browser's local storage. ConvoShelf has no account and no server."), ("Which AI sites does ConvoShelf work with?", "ChatGPT (including Projects), Claude, Gemini and Grok."), ("Is Pro a subscription?", "No. Pro is a single $4.99 payment.")]
seo = '<!--seo--><meta property=og:type content=website><meta property=og:site_name content=ConvoShelf><meta property=og:url content="' + BASE + '"><meta property=og:image:width content=1200><meta property=og:image:height content=630><meta name=twitter:card content=summary_large_image><meta name=twitter:image content="' + BASE + 'og.jpg"><meta name=theme-color content="#4f46e5">' + "".join('<script type="application/ld+json">' + json.dumps(x, ensure_ascii=False) + '</script>' for x in [
  {"@context": "https://schema.org", "@type": "SoftwareApplication", "name": "ConvoShelf", "applicationCategory": "BrowserApplication", "operatingSystem": "Google Chrome (desktop)", "softwareVersion": "1.0.0", "url": BASE, "description": "Folders, tags, full-text search and export for ChatGPT, Claude, Gemini and Grok chats.", "offers": [{"@type": "Offer", "name": "Free", "price": "0", "priceCurrency": "USD"}, {"@type": "Offer", "name": "Pro (one-time)", "price": "4.99", "priceCurrency": "USD"}]},
  {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQS]},
  {"@context": "https://schema.org", "@type": "VideoObject", "name": "ConvoShelf demo", "description": "Folders, search and export across ChatGPT, Claude, Gemini and Grok.", "thumbnailUrl": BASE + "demo-poster.jpg", "contentUrl": BASE + "demo.mp4", "uploadDate": TODAY + "T00:00:00-04:00"}]) + '<!--/seo-->'
idx = open(ROOT + "/index.html").read()
idx = re.sub(r"<!--seo-->.*?<!--/seo-->", "", idx, flags=re.S).replace("<style>", seo + "<style>", 1)
idx = idx.replace('content="https://chumzygood.github.io/convoshelf/folders-1280x800.png"', 'content="' + BASE + 'og.jpg"')
vid = '<!--vid--><video controls muted playsinline preload=none poster="demo-poster.jpg" width=1280 height=720 style="width:100%;height:auto;border:1px solid #e2e8f0;border-radius:12px;margin:24px 0"><source src="demo.mp4" type="video/mp4"><a href="demo.mp4">Download the demo</a></video><!--/vid-->'
idx = re.sub(r"<!--vid-->.*?<!--/vid-->", "", idx, flags=re.S).replace('<img class=shot src="folders-1280x800.png"', vid + '<img class=shot src="folders-1280x800.png"', 1)
open(ROOT + "/index.html", "w").write(idx)
for f, t in [("faq.html", "ConvoShelf FAQ"), ("compare.html", "ConvoShelf compared")]:
    s2 = open(ROOT + "/" + f).read()
    blk = '<!--seo--><meta property=og:type content=website><meta property=og:title content="' + t + '"><meta property=og:url content="' + BASE + f + '"><meta property=og:image content="' + BASE + 'og.jpg"><meta name=twitter:card content=summary_large_image><meta name=twitter:image content="' + BASE + 'og.jpg"><!--/seo-->'
    s2 = re.sub(r"<!--seo-->.*?<!--/seo-->", "", s2, flags=re.S).replace("</head>", blk + "</head>", 1)
    open(ROOT + "/" + f, "w").write(s2)
# Sitemap
pages = ["", "faq.html", "compare.html", "privacy.html"] + [p["slug"] + "/" for p in P] + [p["slug"] + "/compare/" for p in P]
vids = {p["slug"] + "/": p for p in P}
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:video="http://www.google.com/schemas/sitemap-video/1.1">\n'
for u in pages:
    sm += f"<url><loc>{BASE}{u}</loc><lastmod>{TODAY}</lastmod>"
    if u in vids: sm += f"<video:video><video:thumbnail_loc>{BASE}{u}demo-poster.jpg</video:thumbnail_loc><video:title>{E(vids[u]['name'])} demo</video:title><video:description>{E(vids[u]['desc'])}</video:description><video:content_loc>{BASE}{u}demo.mp4</video:content_loc></video:video>"
    if u == "" and os.path.exists(ROOT + "/demo.mp4"): sm += f"<video:video><video:thumbnail_loc>{BASE}demo-poster.jpg</video:thumbnail_loc><video:title>ConvoShelf demo</video:title><video:description>Folders, search and export for ChatGPT, Claude, Gemini and Grok chats.</video:description><video:content_loc>{BASE}demo.mp4</video:content_loc></video:video>"
    sm += "</url>\n"
open(ROOT + "/sitemap.xml", "w").write(sm + "</urlset>\n")
print("ok", len(pages), "urls")
# Uninstall pages per product (no form, no tracking)
for p in P:
    open(os.path.join(ROOT, p["slug"], "bye.html"), "w").write(f'<!doctype html><html lang=en><head><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1"><meta name=robots content=noindex><title>{E(p["name"])} was removed</title><style>:root{{--c:{p["color"]};--a:{p["acc"]}}}{CSS}</style></head><body><main><h1>{E(p["name"])} was removed</h1><p>Your saved items were stored only in that browser and were deleted with the extension. If something didn\'t work, a two-line email helps a lot: <a href="mailto:toolshed+{p["tag"]}@mail.grokbot.com?subject=Uninstall%20feedback">toolshed+{p["tag"]}@mail.grokbot.com</a>.</p><p><a href="./">Back to {E(p["name"])}</a></p></main></body></html>')
