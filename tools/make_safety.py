import re, sys, glob, os
os.chdir(sys.argv[1])
src = open('site/our-promise.html').read()
m = re.search(r'(<template id="dc-tpl">)(.*?)(</template>)', src, re.S)
tpl = m.group(2)

def rep(s, old, new, count=1):
    n = s.count(old)
    assert n == count, (old[:60], n)
    return s.replace(old, new)

# Hero
tpl = rep(tpl, 'src="/img/vickery-1.jpg" alt="Vickery by Toll Brothers, aerial"', 'src="/img/vickery-6.jpg" alt="Home wrapped in LVA pink scaffolds at Vickery, Flower Mound"')
tpl = rep(tpl, '>Our promise<', '>Safety<')
tpl = rep(tpl, '>A woman-owned crew with a standard you can see from the street.<', '>Safety is part of every wall we build.<')
i = tpl.find('>Every crew goes home')
j = tpl.find('LVA Mayan Stucco installs stucco, EIFS, plaster, and stone and brick veneers on commercial, industrial and residential buildings throughout Dallas Fort Worth.', i)
assert j > 0
tpl = tpl[:j] + 'We work to OSHA standards on every Dallas Fort Worth jobsite, from the first scaffold frame to the final coat.' + tpl[j+len('LVA Mayan Stucco installs stucco, EIFS, plaster, and stone and brick veneers on commercial, industrial and residential buildings throughout Dallas Fort Worth.'):]

# Standards cards
tpl = rep(tpl, 'Our cornerstones', 'Safety on site')
tpl = rep(tpl, 'Three words on<br>every job we take.', 'Safe work is<br>good work.')
tpl = rep(tpl, 'We work with you as a partner to find the best building solution for your project, with personalized service and support every day.', 'Stucco happens on scaffolds, around mixers and next to other trades. We plan every job so the people on it, and the people around it, stay safe.')
tpl = rep(tpl, '>Cornerstone<', '>Standard<', 3)
tpl = rep(tpl, 'src="/img/verandah-2.jpg" alt="LVA pink scaffolds on finished white stucco"', 'src="/img/marsh-3.jpg" alt="Pink scaffold frames braced along a two-story wall"')
tpl = rep(tpl, '>Professional<', '>Scaffolds<')
tpl = rep(tpl, 'Crews that show up ready, work clean and leave a site the way a builder would want their own home left.', 'Set on solid footing, fully planked and braced, and checked before each shift the way OSHA requires.')
tpl = rep(tpl, 'src="/img/hero-poster-3.jpg" alt="Finished stucco facade"', 'src="/img/svc-scratch.jpg" alt="LVA crew in high-visibility vests on a commercial roof"')
tpl = rep(tpl, '>Accountable<', '>Protection<')
tpl = rep(tpl, 'On-time delivery, safety first and a schedule-minded, cost-conscious approach on every job we take.', 'Hard hats, high-visibility vests, eye protection and gloves on every crew member, plus fall protection wherever the work is high.')
tpl = rep(tpl, 'src="/img/tru-1.jpg" alt="TRU by Hilton exterior"', 'src="/img/dixon-1.jpg" alt="Covered dumpster beside a home under construction"')
tpl = rep(tpl, '>Credible<', '>Clean sites<')
tpl = rep(tpl, 'Certified applicators for Total Wall, STO, Dryvit, Senergy and Parex. Fully licensed, insured including EIFS, and bonded.', 'Materials staged out of walkways, dust kept down when we mix and cut, and a clean site at the end of every day.')

# Pink scaffolds band
tpl = rep(tpl, 'Our trademark', 'Seen from the street')
tpl = rep(tpl, "When you see pink on a jobsite in Dallas Fort Worth, LVA Mayan Stucco's professional crews are on the job. It is our promise in plain sight.", 'Our pink scaffolds are hard to miss. Builders, inspectors and neighbors always know where our crew is working, and every frame goes up to the same standard.')

# One standard (founder block reused)
tpl = rep(tpl, 'src="/img/laura.jpg" alt="Laura Ayala, Founder and CEO"', 'src="/img/verandah-2.jpg" alt="LVA pink scaffolds along a home in Dallas Fort Worth"')
tpl = rep(tpl, 'Founder &#183; Owner &#183; CEO', 'OSHA &#183; Every site')
tpl = rep(tpl, 'Meet our founder', 'Every crew, every site')
tpl = rep(tpl, '>Laura Ayala</h2>', '>One standard on every site.</h2>')
tpl = rep(tpl, 'Founder, owner and CEO', 'OSHA certified crews')
tpl = rep(tpl, 'Laura is a Texas Latina with roots in El Salvador. She values tradition, and she built her company on it: honest work, done right, by a crew that shows up. She started as Mayan Stucco, Inc. and grew it into LVA Mayan Stucco, LLC, and the standard never changed. She keeps a finger on the pulse of local market conditions so builders get realistic schedules and cost-conscious pricing, and she is grateful every day to serve the Dallas Fort Worth communities she calls home.',
          'Every crew on an LVA site works to the same OSHA standard. Before work starts, the crew walks the site, checks the scaffolds and talks through the day. If something is not safe, the work stops until it is.')
tpl = rep(tpl, '“These cornerstones guide us in helping owners, contractors, developers and design professionals create beautiful interiors and exteriors for their projects.”', '“We build every wall to last, and we build it safely.”')
tpl = rep(tpl, '>Laura Ayala</span>', '>LVA Mayan Stucco</span>', 2)

# Standards grid
tpl = rep(tpl, '>Credentials<', '>On every jobsite<')
tpl = rep(tpl, 'Certified for the systems architects specify.', 'Our standards, on every job.')
tpl = rep(tpl, 'Five wall systems, one crew trained to install each of them, with the licensing, insurance and bonding to match.', 'These are the standards every LVA crew follows, on every project, whatever the size.')
tpl = rep(tpl, '>OSHA certified crews</span></div><div', '>Scaffolds checked before each shift</span></div><div')  # third item
tpl = rep(tpl, '>HUB certified, woman-owned<', '>OSHA certified crews<')
tiles = [('Total Wall','Scaffolds','Checked every shift'),('STO','Fall safety','Wherever the work is high'),('Dryvit','PPE','Hard hats, vests, eyes, hands'),('Senergy','Dust control','When we mix and cut'),('Parex','Safety data','Product sheets on every site')]
for old,new,sub in tiles:
    k = tpl.find('>'+old+'</span>'); assert k>0, old
    tpl = tpl[:k] + '>'+new+'</span>' + tpl[k+len(old)+8:]
    k2 = tpl.find('>Certified applicator<', k); assert k2>0
    tpl = tpl[:k2] + '>'+sub+'<' + tpl[k2+len('>Certified applicator<'):]
tpl = rep(tpl, 'Licensed, insured<br>and bonded', 'OSHA certified<br>crews')

# Active nav: Safety pink, Our Promise white (handled after nav insert)
out = src[:m.start(2)] + tpl + src[m.end(2):]
out = re.sub(r'<div id="dc-root">.*?</div><!--/dc-root-->', '<div id="dc-root"></div><!--/dc-root-->', out, flags=re.S)
desc = 'OSHA certified crews, pink scaffolds checked every shift, and clean, safe jobsites across Dallas Fort Worth. How LVA Mayan Stucco keeps every crew safe.'
out = out.replace('<title>Our Promise | LVA Mayan Stucco</title>', '<title>Safety | LVA Mayan Stucco</title>')
out = out.replace('content="Our Promise | LVA Mayan Stucco"', 'content="Safety | LVA Mayan Stucco"')
out = out.replace('content="Professional, accountable and credible. Meet founder Laura Ayala and the certified, licensed and insured crew behind LVA Mayan Stucco."', 'content="%s"' % desc)
out = out.replace('https://lvamayanstucco.com/our-promise"', 'https://lvamayanstucco.com/safety"')
open('site/safety.html','w').write(out)

# Nav + footer link on every page
def add_links(s, page):
    def desk(mm):
        a = mm.group(0)
        sty = mm.group(1) or ''
        white = re.sub(r'color: #F4689C', 'color: #FFFFFF', sty)
        new = '<a href="/safety"%s>Safety</a>' % white
        return a + new
    s = re.sub(r'<a href="/our-promise"( style="[^"]*")?>Our Promise</a>', desk, s)
    return s
for f in glob.glob('site/*.html'):
    s = open(f).read()
    if 'href="/safety"' in s and f.endswith('safety.html') is False: continue
    s2 = add_links(s, f)
    if f.endswith('safety.html'):
        # make Our Promise white and Safety pink in desktop nav (color #F4689C marks active)
        s2 = re.sub(r'(<a href="/our-promise" style="[^"]*?)color: #F4689C', r'\1color: #FFFFFF', s2)
        s2 = re.sub(r'(<a href="/safety" style="[^"]*?)color: #FFFFFF(; padding: 8px 2px")', r'\1color: #F4689C\2', s2)
    s2 = re.sub(r'(<a href="/safety" style="[^"]*?); border-bottom: 1px solid #E7286F"', r'\1"', s2) if not f.endswith('safety.html') else re.sub(r'(<a href="/our-promise" style="[^"]*?); border-bottom: 1px solid #E7286F"', r'\1"', s2)
    open(f,'w').write(s2)
    print(f, s2.count('href="/safety"'))
