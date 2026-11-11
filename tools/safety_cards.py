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

STONE = "linear-gradient(180deg,rgba(255,255,255,0.3),rgba(90,76,60,0.1)),url(/img/stucco-white.jpg) center/512px repeat"
css = (
 ".cs-wrap{position:relative;padding:24px;border-radius:50% 50% 0 0 / 14% 14% 0 0;background:{ST};"
 "box-shadow:0 0 0 1px rgba(80,66,46,0.35),inset 0 3px 0 rgba(255,255,255,0.85),inset 3px 0 0 rgba(255,255,255,0.45),inset -3px 0 0 rgba(80,66,46,0.18),inset 0 -2px 0 rgba(80,66,46,0.3),0 2px 3px rgba(30,24,16,0.18),0 24px 40px rgba(30,24,16,0.28),0 50px 90px rgba(30,24,16,0.22);margin-bottom:34px}"
 ".cs-wrap::before{content:'';position:absolute;inset:9px;border-radius:50% 50% 0 0 / 14% 14% 0 0;pointer-events:none;box-shadow:0 0 0 1px rgba(80,66,46,0.28),inset 0 0 0 1px rgba(255,255,255,0.7)}"
 ".cs-wrap > .corner{box-shadow:0 0 0 1px rgba(80,66,46,0.55),0 0 0 5px #FBFAF7,0 0 0 6px rgba(80,66,46,0.35),inset 0 10px 24px rgba(0,0,0,0.45) !important}"
 ".cs-key{position:absolute;z-index:3;left:50%;top:-18px;width:70px;height:92px;transform:translateX(-50%);background:{ST};"
 "clip-path:polygon(0 0,100% 0,78% 100%,22% 100%);filter:drop-shadow(0 8px 10px rgba(0,0,0,0.35))}"
 ".cs-key::before{content:'';position:absolute;left:0;right:0;top:0;height:12px;background:linear-gradient(180deg,rgba(255,255,255,0.8),rgba(255,255,255,0))}"
 ".cs-key::after{content:'';position:absolute;inset:16px 18px 14px;clip-path:polygon(0 0,100% 0,80% 100%,20% 100%);background:linear-gradient(180deg,rgba(80,66,46,0.18),rgba(255,255,255,0.25))}"
 ".cs-sill{position:absolute;z-index:3;left:-22px;right:-22px;bottom:-30px;height:30px;background:{ST};"
 "box-shadow:0 0 0 1px rgba(80,66,46,0.3),inset 0 3px 0 rgba(255,255,255,0.9),inset 0 -4px 0 rgba(80,66,46,0.22),0 14px 22px rgba(30,24,16,0.32)}"
 ".cs-sill::before{content:'';position:absolute;left:12px;right:12px;top:-9px;height:9px;background:#FAF8F4;box-shadow:0 0 0 1px rgba(80,66,46,0.25),inset 0 2px 0 rgba(255,255,255,0.85)}"
 ".cs-sill::after{content:'';position:absolute;left:30px;right:30px;bottom:-10px;height:10px;background:linear-gradient(180deg,#F1EEE8,#DCD6CC);box-shadow:0 8px 12px rgba(30,24,16,0.25)}"
 ".cs-wrap .corner-num + span{white-space:nowrap}.cs-wrap .corner-num{font-size:100px !important}"
 "@media (max-width:760px){.cs-wrap{padding:16px;margin-bottom:42px}.cs-wrap::before{inset:6px}.cs-key{width:54px;height:72px;top:-14px}.cs-sill{left:-12px;right:-12px;height:24px;bottom:-24px}.cs-sill::after{left:22px;right:22px}}"
).replace('{ST}', STONE)
s = s.replace('</style>', css + '</style>', 1)
open(f, 'w').write(s)
print('wrapped', s.count('class="cs-wrap"'))
