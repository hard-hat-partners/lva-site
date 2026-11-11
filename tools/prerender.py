"""Bake the first render of each page into its HTML so visitors and search
engines get real content before JavaScript runs. dc.js then patches it in place.

Usage: python3 -I tools/prerender.py <site_dir>   (serves the folder on a local port)
"""
import asyncio, os, re, sys, threading, http.server, functools
from playwright.async_api import async_playwright

SITE = os.path.abspath(sys.argv[1])
PAGES = ['index', 'services', 'our-promise', 'projects', 'contact', 'privacy']

class Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a):
        pass
handler = functools.partial(Quiet, directory=SITE)
srv = http.server.ThreadingHTTPServer(('127.0.0.1', 0), handler)
threading.Thread(target=srv.serve_forever, daemon=True).start()
port = srv.server_address[1]


async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path=os.environ.get('CHROME', '/usr/bin/google-chrome'))
        for name in PAGES:
            path = os.path.join(SITE, name + '.html')
            src = open(path).read()
            src = re.sub(r'<div id="dc-root">.*?</div><!--/dc-root-->', '<div id="dc-root"></div>', src, flags=re.S)
            open(path, 'w').write(src)
            pg = await b.new_page(viewport={'width': 1440, 'height': 900})
            await pg.goto(f'http://127.0.0.1:{port}/{name}.html')
            await pg.wait_for_function("document.documentElement.classList.contains('dc-ready')")
            inner = await pg.evaluate("""() => {
                const r = document.getElementById('dc-root').cloneNode(true);
                r.querySelectorAll('[data-dc-started]').forEach(v => v.removeAttribute('data-dc-started'));
                return r.innerHTML;
            }""")
            await pg.close()
            src = src.replace('<div id="dc-root"></div>', '<div id="dc-root">' + inner + '</div><!--/dc-root-->', 1)
            open(path, 'w').write(src)
            print('prerendered', name, len(inner))
        await b.close()

asyncio.run(main())
srv.shutdown()
