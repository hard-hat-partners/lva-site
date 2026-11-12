"""Nov 11, 2026: Laura asked to remove John R. Landon and Pegaso Group. Their projects, names, photos and video come off the site."""
import re, glob, json
def sub(s, a, b, f):
    return s.replace(a, b)
for f in sorted(glob.glob('site/*.html')):
    s = open(f).read(); o = s
    # shared craft-tab data and any other use of the Landon stonework photo
    s = s.replace('/img/landon-2.jpg', '/img/montgomery-2.jpg')
    s = s.replace('alt="Stonework, Landon Homes in Vickery"', 'alt="Stone veneer entry, Montgomery Farm Estates"')
    s = s.replace('See it at <span>Landon Homes in Vickery · Montgomery Farm Estates</span>', 'See it at <span>Montgomery Farm Estates</span>')
    s = s.replace('See it at <span>Star Trail by Toll Brothers · Vickery by Toll Brothers · Cabell Townhomes</span>', 'See it at <span>Star Trail by Toll Brothers · Vickery by Toll Brothers</span>')
    s = s.replace('Toll Brothers · Landon Homes · Brookfield Residential · Pegaso Group', 'Toll Brothers · Brookfield Residential')
    # Services hero
    s = s.replace('src="/img/landon-3.jpg" alt="Landon Homes in Vickery, aerial"', 'src="/img/hero-poster-3.jpg" alt="Finished stucco facade, Dallas Fort Worth"')
    # Home: Residential Tract card
    s = s.replace('src="/img/landon-1.jpg" alt="Landon Homes in Vickery Subdivision, aerial"', 'src="/img/oakbridge-4.jpg" alt="Oakbridge Subdivision by Toll Brothers, aerial"')
    # Home: marquee item
    s = re.sub(r'<span(?: style="[^"]*")?>Landon Homes</span><span aria-hidden="true"(?: style="[^"]*")?>▲</span>', '', s)
    # Home: video switcher row 5 -> Oakbridge
    s = s.replace('src="/video/v-landon-loop.mp4" poster="/img/landon-1.jpg"', 'src="/video/v-oakbridge-loop.mp4" poster="/img/oakbridge-2.jpg"')
    s = s.replace('class="sw-name">Landon Homes in Vickery Subdivision</span>', 'class="sw-name">Oakbridge Subdivision by Toll Brothers</span>')
    if 'index.html' in f:
        i = s.find('class="sw-name">Oakbridge Subdivision by Toll Brothers</span>')
        while i != -1:
            j = s.find('Residential Tract · Copper Canyon, TX', i)
            if j != -1 and j - i < 600: s = s[:j] + 'Residential Tract · Flower Mound, TX' + s[j+len('Residential Tract · Copper Canyon, TX'):]
            i = s.find('class="sw-name">Oakbridge Subdivision by Toll Brothers</span>', i + 10)
    # Projects: drop both projects from the data
    if 'projects.html' in f:
        s = re.sub(r'\{"name": "Landon Homes in Vickery Subdivision"[^{}]*\}, ', '', s)
        s = re.sub(r', \{"name": "Cabell Townhomes by Pegaso Group"[^{}]*\}', '', s)
        s = re.sub(r'\{"name": "Cabell Townhomes by Pegaso Group"[^{}]*\}, ', '', s)
    if s != o: open(f, 'w').write(s); print('updated', f)
