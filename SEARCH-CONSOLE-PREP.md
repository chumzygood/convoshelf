# Search Console / Bing prep (convoshelf site)
- Sitemap: https://chumzygood.github.io/convoshelf/sitemap.xml (10 URLs incl. 3 product pages, 3 compare pages, video entries). robots.txt points to it.
- IndexNow key file: /74280afd280c48aa0b2ad5c97d984ec2.txt (same setup as WA Folders). Submit with: curl "https://api.indexnow.org/indexnow?url=<page>&key=74280afd280c48aa0b2ad5c97d984ec2" (free, no account). Not pinged yet.
- Google Search Console: needs Chanoch's Google sign-in. Add a URL-prefix property for https://chumzygood.github.io/convoshelf/ (or a Domain property for convoshelf.com after DNS), choose "HTML file", and drop the google*.html file it gives into this repo root. The WA Folders file (googlefd7b3bbaee78af02.html) is tied to the wafolders property and can't be reused.
- Bing Webmaster Tools: import from Search Console once verified, or add BingSiteAuth.xml from Bing.
- When convoshelf.com DNS is live: set BASE in tools/products.py, add CNAME, rerun python3 tools/products.py, update robots.txt.
