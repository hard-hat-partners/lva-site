# lvamayanstucco.com

Static site for LVA Mayan Stucco LLC, served by Netlify. Every push to `main` deploys.

## Layout

- `site/` is exactly what visitors get. Netlify publishes this folder only.
- `site/js/dc.js` is the small runtime that runs each page's template (menus, project filters, gallery, tabs, sticky header).
- `tools/build.py` turns the Claude Design artboards into `site/`.
- `tools/prerender.py` bakes the first render into each page so content shows before JavaScript runs.
- `tools/dc.js` is the source of the runtime; build copies it into `site/js/`.

## Rebuilding from Claude Design

1. Pull the artboards (`project/*.dc.html`), the media files and the asset map (`assets.json`, upload key to `/_blob/` id).
2. `npm i @fontsource/cinzel @fontsource/cormorant-garamond @fontsource/jost` in a scratch folder.
3. `python3 -I tools/build.py <project_dir> <media_dir> <assets.json> <scratch>/node_modules/@fontsource site`
4. `python3 -I tools/prerender.py site` (needs Playwright and Chrome)
5. Commit and push to `main`.

After launch the Design project is retired and edits are made here directly, through Site Care.

## What the build adds

- Fonts, images and videos self-hosted (no third-party loads before a click, per our CIPA standard)
- Clean URLs: `/services`, `/our-promise`, `/projects`, `/contact`, `/privacy`
- Titles, descriptions, canonical URLs, Open Graph and Twitter tags, LocalBusiness structured data on the home page
- Netlify form `contact` with honeypot, landing on `/thank-you`
- `404.html`, `robots.txt`, `sitemap.xml`, `_redirects` for the old WordPress URLs

## Launch checklist

- Delete the `X-Robots-Tag` block in `netlify.toml`
- Point lvamayanstucco.com DNS at Netlify (A record 75.2.60.5, `www` CNAME to the Netlify site)
- Set form notifications in Netlify to laura@lvamayanstucco.com
