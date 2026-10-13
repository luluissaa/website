#!/usr/bin/env python3
"""Downloads the newsletter images from the old Ghost site into assets/letters/.

    python3 download-letter-images.py https://your-ghost-site.ghost.io

Run it while the Ghost site is still online. Already-downloaded images are skipped,
so it is safe to run again if the connection drops.
"""
import sys, pathlib, urllib.request, urllib.error

if len(sys.argv) != 2 or not sys.argv[1].startswith('http'):
    sys.exit('Usage: python3 download-letter-images.py https://your-ghost-site.ghost.io')
base = sys.argv[1].rstrip('/')
here = pathlib.Path(__file__).parent
dest = here / 'assets' / 'letters'
paths = [p.strip() for p in (dest / 'image-manifest.txt').read_text().splitlines() if p.strip()]

ok, skipped, failed = 0, 0, []
for p in paths:
    out = dest / p
    if out.exists() and out.stat().st_size > 0:
        skipped += 1
        continue
    out.parent.mkdir(parents=True, exist_ok=True)
    url = f'{base}/content/images/{urllib.request.quote(p)}'
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'goblin-market-archive'})
        with urllib.request.urlopen(req, timeout=60) as r:
            out.write_bytes(r.read())
        ok += 1
        print('saved', p)
    except (urllib.error.URLError, TimeoutError) as e:
        failed.append((p, str(e)))
        print('FAILED', p, e)

print(f'\n{ok} downloaded, {skipped} already there, {len(failed)} failed (of {len(paths)})')
if failed:
    print('Run the same command again to retry the failed ones.')
