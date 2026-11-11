"""Turn the Claude Design artboards for LVA Mayan Stucco into the static site.

Usage: python3 -I tools/build.py <design_project_dir> <media_dir> <assets.json> <fontsource_dir> <out_site_dir>

- One HTML file per page, clean URLs (/services, /our-promise, ...)
- Template + logic run by /js/dc.js; first paint is prerendered later by tools/prerender.py
- Fonts, images and videos self-hosted (no third-party loads before a click)
- Titles, descriptions, canonical, Open Graph, sitemap, robots, 404, redirects
"""
import sys, os, re, json, shutil, html

PROJ, MEDIA, ASSETS, FONTSRC, OUT = sys.argv[1:6]
SITE = 'https://lvamayanstucco.com'
A = json.load(open(ASSETS))
BLOB = {v.split('/')[-1]: k for k, v in A.items()}
files = {os.path.splitext(f)[0]: f for f in os.listdir(MEDIA)}

PAGES = {
    'Main': ('index', '/', 'LVA Mayan Stucco | Stucco, EIFS and Stone Contractor in Dallas Fort Worth',
             'Certified woman-owned stucco, EIFS, stone and cast stone contractor building for Toll Brothers, Hilton and Gucci across Dallas Fort Worth.'),
    'Services': ('services', '/services', 'Stucco, EIFS, Stone and Cast Stone Services | LVA Mayan Stucco',
                 'Three-coat stucco, EIFS, exterior molding, stonework and cast stone for commercial, residential and custom projects across Dallas Fort Worth.'),
    'Why': ('our-promise', '/our-promise', 'Our Promise | LVA Mayan Stucco',
            'Professional, accountable and credible. Meet founder Laura Ayala and the certified, licensed and insured crew behind LVA Mayan Stucco.'),
    'Projects': ('projects', '/projects', 'Projects | LVA Mayan Stucco',
                 'Hotels, retail centers, whole neighborhoods and custom homes across Dallas Fort Worth, finished by LVA Mayan Stucco.'),
    'Contact': ('contact', '/contact', 'Start a Project | LVA Mayan Stucco',
                'Tell us what you are building. Call (214) 875-3606 or send a note and Laura Ayala\'s team will follow up personally.'),
    'Privacy': ('privacy', '/privacy', 'Privacy Policy and Terms of Use | LVA Mayan Stucco',
                'How LVA Mayan Stucco handles the information you share through this website, and the terms for using it.'),
}
LINKS = {stem: path for stem, (_, path, _, _) in PAGES.items()}

if os.path.exists(OUT):
    for n in os.listdir(OUT):
        p = os.path.join(OUT, n)
        shutil.rmtree(p) if os.path.isdir(p) else os.remove(p)
os.makedirs(OUT, exist_ok=True)
for d in ('img', 'video', 'fonts', 'js'):
    os.makedirs(os.path.join(OUT, d), exist_ok=True)

used = set()
def blob(m):
    key = BLOB[m.group(1)]
    fn = files[key]
    used.add(fn)
    sub = 'video' if fn.endswith('.mp4') else 'img'
    return f'/{sub}/{fn}'

# fonts
css = []
for fam, slug, specs in [('Cinzel', 'cinzel', [(400, 'normal'), (500, 'normal'), (600, 'normal')]),
                         ('Cormorant Garamond', 'cormorant-garamond', [(400, 'italic'), (500, 'italic')]),
                         ('Jost', 'jost', [(300, 'normal'), (400, 'normal'), (500, 'normal')])]:
    for w, s in specs:
        fn = f'{slug}-latin-{w}-{s}.woff2'
        shutil.copy(os.path.join(FONTSRC, slug, 'files', fn), os.path.join(OUT, 'fonts'))
        css.append(f"@font-face{{font-family:'{fam}';font-style:{s};font-weight:{w};font-display:swap;src:url(/fonts/{fn}) format('woff2')}}")
open(os.path.join(OUT, 'fonts', 'fonts.css'), 'w').write('\n'.join(css) + '\n')
shutil.copy(os.path.join(os.path.dirname(__file__), 'dc.js'), os.path.join(OUT, 'js', 'dc.js'))

def head_meta(path, title, desc):
    e = html.escape
    url = SITE + path
    return '\n'.join([
        f'<title>{e(title)}</title>',
        f'<meta name="description" content="{e(desc)}">',
        '<meta name="viewport" content="width=device-width, initial-scale=1">',
        f'<link rel="canonical" href="{url}">',
        '<meta property="og:type" content="website">',
        '<meta property="og:site_name" content="LVA Mayan Stucco">',
        f'<meta property="og:title" content="{e(title)}">',
        f'<meta property="og:description" content="{e(desc)}">',
        f'<meta property="og:url" content="{url}">',
        f'<meta property="og:image" content="{SITE}/img/og-image.jpg">',
        '<meta property="og:image:width" content="1200">',
        '<meta property="og:image:height" content="630">',
        '<meta name="twitter:card" content="summary_large_image">',
        f'<meta name="twitter:title" content="{e(title)}">',
        f'<meta name="twitter:description" content="{e(desc)}">',
        f'<meta name="twitter:image" content="{SITE}/img/og-image.jpg">',
        '<link rel="icon" type="image/png" href="/img/favicon.png">',
        '<link rel="preload" href="/fonts/cinzel-latin-500-normal.woff2" as="font" type="font/woff2" crossorigin>',
        '<link href="/fonts/fonts.css" rel="stylesheet">',
    ])

LD = {
    "@context": "https://schema.org", "@type": "GeneralContractor", "name": "LVA Mayan Stucco LLC",
    "url": SITE, "telephone": "+1-214-875-3606", "email": "laura@lvamayanstucco.com",
    "image": SITE + "/img/og-image.jpg",
    "address": {"@type": "PostalAddress", "streetAddress": "11258 Goodnight Ln", "addressLocality": "Dallas", "addressRegion": "TX", "postalCode": "75229", "addressCountry": "US"},
    "areaServed": "Dallas Fort Worth, Texas",
    "founder": {"@type": "Person", "name": "Laura Ayala"},
    "sameAs": ["https://www.instagram.com/lvamayanstucco/", "https://www.facebook.com/LVAMayanStucco/", "https://www.linkedin.com/company/lva-mayan-stucco"],
}

for stem, (slug, path, title, desc) in PAGES.items():
    src = open(os.path.join(PROJ, stem + '.dc.html')).read()
    src = re.sub(r'/_blob/([0-9a-f]+)', blob, src)
    src = re.sub(r'href="([A-Za-z]+)\.dc\.html', lambda m: 'href="' + LINKS[m.group(1)], src)
    helmet = re.search(r'<helmet>(.*?)</helmet>', src, re.S).group(1)
    helmet = re.sub(r'<link rel="preconnect"[^>]*>\s*', '', helmet)
    helmet = re.sub(r'<link href="https://fonts\.googleapis\.com/css2[^"]*" rel="stylesheet">\s*', '', helmet)
    body = re.search(r'<x-dc>(.*?)</x-dc>', src, re.S).group(1)
    body = re.sub(r'<helmet>.*?</helmet>', '', body, flags=re.S)
    assert '<div style="height: 100%; width: {{progress}};' in body
    body = body.replace('<div style="height: 100%; width: {{progress}};', '<div id="pbar" style="height: 100%; width: 0%;')
    if stem == 'Contact':
        body = body.replace('netlify-honeypot="company-website"', 'netlify-honeypot="company-website" action="/thank-you"', 1)
        body = re.sub(r'(<form name="contact"[^>]*>)', r'\1\n      <input type="hidden" name="form-name" value="contact">', body, count=1)
    logic = re.search(r'<script type="text/x-dc" data-dc-script[^>]*>(.*?)</script>', src, re.S).group(1)
    old = "if (Math.abs(pct - (this.state.progress || 0)) >= 0.4 || st !== !!this.state.stuck) this.setState({ progress: pct, stuck: st });"
    assert old in logic, stem
    logic = logic.replace(old, "const pb = document.getElementById('pbar'); if (pb) pb.style.width = pct.toFixed(2) + '%'; if (st !== !!this.state.stuck) this.setState({ stuck: st });")
    assert 'fonts.googleapis' not in helmet + body and '/_blob/' not in body + logic
    ld = f'<script type="application/ld+json">{json.dumps(LD)}</script>' if stem == 'Main' else ''
    page = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
{head_meta(path, title, desc)}
{helmet.strip()}
<style>#dc-root:empty{{min-height:100vh;background:#121216}}</style>
{ld}
</head>
<body>
<div id="dc-root"></div>
<template id="dc-tpl">{body}</template>
<script type="text/plain" id="dc-logic">{logic}</script>
<script src="/js/dc.js" defer></script>
</body>
</html>
'''
    open(os.path.join(OUT, slug + '.html'), 'w').write(page)

from PIL import Image
for fn in sorted(used):
    sub = 'video' if fn.endswith('.mp4') else 'img'
    dst = os.path.join(OUT, sub, fn)
    src_p = os.path.join(MEDIA, fn)
    if fn.endswith('.jpg') and os.path.getsize(src_p) > 300000:
        im = Image.open(src_p).convert('RGB')
        if im.size[0] > 2000:
            im = im.resize((2000, round(im.size[1] * 2000 / im.size[0])), Image.LANCZOS)
        im.save(dst, quality=80, optimize=True, progressive=True)
    else:
        shutil.copy(src_p, dst)

# share image and favicon
from PIL import Image
im = Image.open(os.path.join(MEDIA, files['vickery-1'])).convert('RGB')
w, h = im.size
ch = int(w * 630 / 1200)
im.crop((0, (h - ch) // 2, w, (h - ch) // 2 + ch)).resize((1200, 630), Image.LANCZOS).save(os.path.join(OUT, 'img', 'og-image.jpg'), quality=84, optimize=True)
tri = Image.open(os.path.join(MEDIA, files['tri-pink'])).convert('RGBA')
tri.thumbnail((180, 180))
fav = Image.new('RGBA', (192, 192), (18, 18, 22, 255))
fav.paste(tri, ((192 - tri.size[0]) // 2, (192 - tri.size[1]) // 2), tri)
fav.save(os.path.join(OUT, 'img', 'favicon.png'))

# simple pages: 404 and thank you, built on the site's look
def simple(slug, title, eyebrow, heading, text, noindex=True):
    page = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{html.escape(title)}</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
{'<meta name="robots" content="noindex">' if noindex else ''}
<link rel="icon" type="image/png" href="/img/favicon.png">
<link href="/fonts/fonts.css" rel="stylesheet">
<style>
body{{margin:0;min-height:100vh;display:flex;align-items:center;justify-content:center;background:#121216 url(/img/{files['monogram']}) repeat;background-size:240px 240px;font-family:'Jost',system-ui,sans-serif;color:#C8C4CC}}
.card{{background:rgba(18,18,22,0.92);border:1px solid rgba(231,40,111,0.45);padding:56px 40px;max-width:560px;margin:24px;text-align:center;display:flex;flex-direction:column;gap:20px;align-items:center}}
.eb{{font-size:12px;letter-spacing:.3em;text-transform:uppercase;color:#F4689C}}
h1{{margin:0;font-family:'Cinzel',serif;font-weight:500;font-size:clamp(30px,5vw,46px);line-height:1.1;color:#fff}}
p{{margin:0;font-size:18px;line-height:1.7;font-weight:300}}
a.btn{{display:inline-flex;align-items:center;min-height:54px;padding:0 30px;background:#C21C5A;color:#fff;text-decoration:none;font-size:13px;font-weight:500;letter-spacing:.24em;text-transform:uppercase}}
</style>
</head>
<body>
<div class="card">
<img src="/img/{files['logo-white']}" alt="LVA Mayan Stucco" style="width:200px;height:auto">
<span class="eb">{eyebrow}</span>
<h1>{heading}</h1>
<p>{text}</p>
<a class="btn" href="/">Back to home</a>
</div>
</body>
</html>
'''
    open(os.path.join(OUT, slug + '.html'), 'w').write(page)
    used.update([files['monogram'], files['logo-white']])
    for k in ('monogram', 'logo-white'):
        shutil.copy(os.path.join(MEDIA, files[k]), os.path.join(OUT, 'img', files[k]))

simple('404', 'Page not found | LVA Mayan Stucco', 'Page not found', 'This wall is not on our map.', 'The page you were looking for has moved or no longer exists. Our projects, services and contact details are a click away.')
simple('thank-you', 'Thank you | LVA Mayan Stucco', 'Message received', 'Thank you. We will be in touch.', 'Laura\'s team reads every note personally and will follow up soon. Need us sooner? Call (214) 875-3606.')

# robots, sitemap, redirects, headers
open(os.path.join(OUT, 'robots.txt'), 'w').write(f'User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n')
urls = ''.join(f'<url><loc>{SITE}{p[1]}</loc></url>' for p in PAGES.values())
open(os.path.join(OUT, 'sitemap.xml'), 'w').write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
open(os.path.join(OUT, '_redirects'), 'w').write('''# Old WordPress pages
/why-choose-us      /our-promise   301
/why-choose-us/     /our-promise   301
/contact-us         /contact       301
/contact-us/        /contact       301
/privacy-policy     /privacy       301
/privacy-policy/    /privacy       301
/portfolio/*        /projects      301
/projects/          /projects      301
/wp-admin/*         /              301
/wp-login.php       /              301
''')
print('built', len(PAGES), 'pages,', len(used), 'media files')
