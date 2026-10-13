#!/usr/bin/env python3
"""Run once the site's address is known, e.g.

    python3 set-site-url.py https://goblinmarket.ca/

Adds the canonical link and og:url, makes the share-image links absolute,
writes sitemap.xml and points robots.txt at it. Safe to run again with a new address.
For a custom domain it also writes the CNAME file GitHub Pages needs.
"""
import re, sys, datetime, pathlib
from urllib.parse import urlparse

if len(sys.argv) != 2 or not sys.argv[1].startswith('https://'):
    sys.exit('Usage: python3 set-site-url.py https://your-address/')
url = sys.argv[1].rstrip('/') + '/'
here = pathlib.Path(__file__).parent
pages = sorted(here.glob('**/index.html'))

def page_url(f):
    rel = f.parent.relative_to(here).as_posix()
    return url if rel == '.' else f'{url}{rel}/'

for f in pages:
    html = f.read_text(encoding='utf-8')
    if '<!-- SITE_URL_TAGS' not in html:
        continue
    # remove anything a previous run added
    html = re.sub(r'<link rel="canonical"[^>]*>\n|<meta property="og:url"[^>]*>\n', '', html)
    html = re.sub(r'(<meta (?:property="og:image"|name="twitter:image") content=")https://[^"]*?/((?:assets/|og-image)[^"]*")', r'\1\2', html)
    html = re.sub(r'(<meta (?:property="og:image"|name="twitter:image") content=")(?:\.\./)*', r'\1', html)
    me = page_url(f)
    i = html.index('<!-- SITE_URL_TAGS')
    html = html[:i] + f'<link rel="canonical" href="{me}">\n<meta property="og:url" content="{me}">\n' + html[i:]
    html = re.sub(r'(<meta (?:property="og:image"|name="twitter:image") content=")((?:assets/|og-image)[^"]*")', lambda m: m.group(1) + url + m.group(2), html)
    f.write_text(html, encoding='utf-8')

today = datetime.date.today().isoformat()
(here / 'sitemap.xml').write_text(
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
    ''.join(f'  <url><loc>{page_url(f)}</loc><lastmod>{today}</lastmod></url>\n' for f in pages if f.parent.name != '404') +
    '</urlset>\n', encoding='utf-8')
(here / 'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {url}sitemap.xml\n', encoding='utf-8')

host = urlparse(url).hostname
cname = here / 'CNAME'
if host.endswith('github.io'):
    if cname.exists():
        cname.unlink()
        print('Removed CNAME (GitHub address, no custom domain)')
else:
    cname.write_text(host + '\n', encoding='utf-8')
    print(f'Wrote CNAME for {host}')
print(f'Site address set to {url}')
