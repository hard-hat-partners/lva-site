"""Safety page cards: OSHA rule labels and a cast stone surround (arch, keystone, sill) around each photo card.
Run on site/safety.html built from main (cards still say "Standard")."""
import re, sys
f = sys.argv[1]
s = open(f).read()

labels = ['OSHA 1926.451', 'OSHA 1926.95', 'OSHA 1926.25']
seq = iter(labels * 2)  # template copy, then prerendered copy
s = re.sub(r'padding-top: 6px">Standard</span>', lambda m: 'padding-top: 6px">%s</span>' % next(seq), s)

def wrap_cards(s):
    out, i = [], 0
    while True:
        j = s.find('<div class="corner shp-arch"', i)
        if j < 0:
            out.append(s[i:]); return ''.join(out)
        depth, k = 0, j
        while True:
            o = s.find('<div', k); c = s.find('</div>', k)
            if o != -1 and o < c:
                depth += 1; k = o + 4
            else:
                depth -= 1; k = c + 6
                if depth == 0: break
        out.append(s[i:j]); out.append('<div class="cs-wrap"><span class="cs-key" aria-hidden="true"></span>' + s[j:k] + '<span class="cs-sill" aria-hidden="true"></span></div>')
        i = k
s = wrap_cards(s)

STONE = "#E7E0D3 url(/img/stucco-white.jpg) center/420px repeat"
css = (
 ".cs-wrap{position:relative;padding:18px;border-radius:50% 50% 0 0 / 14% 14% 0 0;background:{ST};background-blend-mode:multiply;"
 "box-shadow:inset 0 2px 0 rgba(255,255,255,0.75),inset 0 -1px 0 rgba(90,78,60,0.25),inset 2px 0 0 rgba(255,255,255,0.4),inset -2px 0 0 rgba(90,78,60,0.12),0 30px 60px rgba(40,32,24,0.22);margin-bottom:22px}"
 ".cs-wrap > .corner{box-shadow:0 0 0 1px rgba(90,78,60,0.45),0 0 0 6px #F2EDE4,0 0 0 7px rgba(90,78,60,0.3) !important}"
 ".cs-key{position:absolute;z-index:3;left:50%;top:-14px;width:58px;height:74px;transform:translateX(-50%);background:{ST};background-blend-mode:multiply;"
 "clip-path:polygon(0 0,100% 0,80% 100%,20% 100%);filter:drop-shadow(0 6px 8px rgba(0,0,0,0.25))}"
 ".cs-key::after{content:'';position:absolute;inset:8px 14px 10px;clip-path:polygon(0 0,100% 0,82% 100%,18% 100%);border-top:1px solid rgba(90,78,60,0.35);background:linear-gradient(180deg,rgba(255,255,255,0.35),rgba(90,78,60,0.08))}"
 ".cs-sill{position:absolute;z-index:3;left:-16px;right:-16px;bottom:-22px;height:26px;background:{ST};background-blend-mode:multiply;"
 "box-shadow:inset 0 2px 0 rgba(255,255,255,0.8),inset 0 -3px 0 rgba(90,78,60,0.18),0 12px 18px rgba(40,32,24,0.22)}"
 ".cs-sill::before{content:'';position:absolute;left:10px;right:10px;top:-6px;height:6px;background:#DDD5C6;box-shadow:inset 0 1px 0 rgba(255,255,255,0.7)}"
 "@media (max-width:760px){.cs-wrap{padding:13px;margin-bottom:30px}.cs-key{width:46px;height:60px;top:-11px}.cs-sill{left:-10px;right:-10px;height:22px;bottom:-18px}}"
).replace('{ST}', STONE)
s = s.replace('</style>', css + '</style>', 1)
open(f, 'w').write(s)
print('wrapped', s.count('class="cs-wrap"'))
