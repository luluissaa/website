# Goblin Market website

One-page site for Goblin Market and the Goblins Everywhere Lab, a Luisa Ji initiative delivered via UKAI Projects.

## What's in this folder

| File | Purpose |
| --- | --- |
| `index.html` | The home page. Logos and the wordmark are built in. |
| `letters/` | *Dispatch from Goblin Market*, the newsletter archive: 19 letters plus the About page, one folder each. |
| `assets/letters.css` | Styles for the archive pages. |
| `assets/letters/` | Not used at the moment: the letters are text only. Holds the list of the original Ghost images, in case you want to bring them back later. |
| `favicon.svg`, `apple-touch-icon.png` | Browser tab and phone home-screen icons. |
| `og-image.png` | The preview image shown when the link is shared (Instagram, Slack, iMessage, LinkedIn). |
| `404.html` | Shown for any wrong address. |
| `robots.txt` | Lets search engines index the site. |
| `set-site-url.py` | Run once the web address is decided (see step 3). |
| `download-letter-images.py` | Optional: copies the original newsletter images from Ghost (see "Newsletter archive" below). |
| `.nojekyll` | Tells GitHub Pages to serve the files as they are. |

## Publish on GitHub Pages

The site address is **https://goblinseverywhere.ca/**. It is already written into every page, the sitemap, `robots.txt` and the `CNAME` file. (If the address ever changes, run `python3 set-site-url.py https://NEW-ADDRESS/` in this folder.)

1. Create a GitHub organization or account called `goblins-everywhere` (free), then a new public repository in it, for example `website`.
2. Upload everything in this folder to the repository root (drag and drop on github.com works). Include the hidden `.nojekyll` file and `CNAME`: on a Mac, press **Cmd + Shift + .** in Finder to show hidden files.
3. In the repository: **Settings → Pages → Build and deployment → Source: Deploy from a branch → Branch: main, folder: / (root) → Save.** Under **Custom domain**, enter `goblinseverywhere.ca` and save.
4. At your domain registrar, add these DNS records for `goblinseverywhere.ca`:

   | Type | Name | Value |
   | --- | --- | --- |
   | A | @ | 185.199.108.153 |
   | A | @ | 185.199.109.153 |
   | A | @ | 185.199.110.153 |
   | A | @ | 185.199.111.153 |
   | AAAA | @ | 2606:50c0:8000::153 |
   | AAAA | @ | 2606:50c0:8001::153 |
   | AAAA | @ | 2606:50c0:8002::153 |
   | AAAA | @ | 2606:50c0:8003::153 |
   | CNAME | www | goblins-everywhere.github.io |

   Remove any parking or "coming soon" records the registrar added for `@` or `www`. Check these values against GitHub's current guide (docs.github.com, "Managing a custom domain for your GitHub Pages site") before saving.
5. DNS can take up to a day. When GitHub shows the domain check as successful, tick **Enforce HTTPS**.
6. Recommended: verify the domain under the organization's **Settings → Pages → Add a domain**, so no one else can point it at their own GitHub site.
7. Once it's live, add the site to Google Search Console and submit `https://goblinseverywhere.ca/sitemap.xml`.

## Background video

The background plays the YouTube Short `QLsh-tcXfEU`, muted and looping. It only plays once the site is on a real web address (not when `index.html` is opened from your computer). To change it, edit the `BACKGROUND` settings near the bottom of `index.html`:

- `YOUTUBE_ID`: the video's ID
- `VIDEO_FILE`: path to an .mp4 in this folder (more reliable than YouTube; takes priority)
- `PHOTO`: path to a backup photo, shown if the video can't play

If neither video nor photo works, the page shows plain indigo.

## Newsletter archive

The archive was converted from the Ghost export of 22 February 2026. All letters are public here, including ones that were members-only on Ghost. Sign-up forms and the "leave us some coins" tip button were removed because they only worked on Ghost. The letters are **text only**: photos, galleries and GIFs were left out because the images couldn't be copied from Ghost.

To bring the images back later, while the Ghost site (notesonend.ghost.io) is still online:
1. In this folder run `python3 download-letter-images.py https://notesonend.ghost.io`.
2. Ask Claude to regenerate the archive with images switched on. No new letters are planned, so the pages are plain HTML and need no build step.
