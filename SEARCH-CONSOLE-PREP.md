# Search Console / Bing / IndexNow (convoshelf site)
Updated 2026-10-18.
- Live at https://convoshelf.com/ (Cloudflare DNS, GitHub Pages, CNAME in repo, HTTPS enforced). www redirects to the apex.
- Sitemap: https://convoshelf.com/sitemap.xml (10 URLs: ConvoShelf pages plus the other Shelf product and compare pages, with video entries). robots.txt allows all and points to it.
- IndexNow key file: /74280afd280c48aa0b2ad5c97d984ec2.txt. Ping log: /workspace/convoshelf-owner/indexnow-2026-10-18/ on the box.
- Google Search Console: index.html has meta google-site-verification fzeImh6_..., and googlefd7b3bbaee78af02.html is in the root (Google HTML-file tokens belong to a Google account, so it verifies only for the account that issued it). Preferred: Domain property convoshelf.com via a Cloudflare TXT record. Then submit sitemap.xml.
- Bing Webmaster Tools: index.html has meta msvalidate.01 E53FD6DE.... Add the site (or import from GSC) and submit the sitemap.
- tools/products.py regenerates product pages, compare pages, the home family section and sitemap.xml. It sets every lastmod to the run date.
