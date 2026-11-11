"""Cast stone surround for arched cards (stepped molding, keystone, two-tier sill).

Usage: python3 -I tools/cast_frame.py <page.html> '<opening tag prefix of each card>' [rail]
Wraps every matching card (template copy and prerendered copy) and adds the styles once.
Pass "rail" when the cards sit in a .rail container that scrolls sideways on phones.
"""
import sys

def wrap(s, marker, rail=False):
    out, i, n = [], 0, 0
    while True:
        j = s.find(marker, i)
        if j < 0:
            out.append(s[i:]); return ''.join(out), n
        tag = s[j+1:s.find(' ', j)]
        depth, k = 0, j
        while True:
            o = s.find('<' + tag, k); c = s.find('</' + tag + '>', k)
            if o != -1 and o < c:
                depth += 1; k = o + len(tag) + 1
            else:
                depth -= 1; k = c + len(tag) + 3
                if depth == 0: break
        out.append(s[i:j]); out.append('<div class="cs-wrap"><span class="cs-key" aria-hidden="true"></span>' + s[j:k] + '<span class="cs-sill" aria-hidden="true"></span></div>')
        i = k; n += 1

STONE = "linear-gradient(180deg,rgba(255,255,255,0.3),rgba(90,76,60,0.1)),url(/img/stucco-white.jpg) center/512px repeat"
CSS = (
 ".cs-wrap{position:relative;padding:24px;border-radius:50% 50% 0 0 / 14% 14% 0 0;background:{ST};"
 "box-shadow:0 0 0 1px rgba(80,66,46,0.35),inset 0 3px 0 rgba(255,255,255,0.85),inset 3px 0 0 rgba(255,255,255,0.45),inset -3px 0 0 rgba(80,66,46,0.18),inset 0 -2px 0 rgba(80,66,46,0.3),0 2px 3px rgba(30,24,16,0.18),0 24px 40px rgba(30,24,16,0.28),0 50px 90px rgba(30,24,16,0.22);margin-bottom:34px}"
 ".cs-wrap::before{content:'';position:absolute;inset:9px;border-radius:50% 50% 0 0 / 14% 14% 0 0;pointer-events:none;box-shadow:0 0 0 1px rgba(80,66,46,0.28),inset 0 0 0 1px rgba(255,255,255,0.7)}"
 ".cs-wrap > .shp-arch{box-shadow:0 0 0 1px rgba(80,66,46,0.55),0 0 0 5px #FBFAF7,0 0 0 6px rgba(80,66,46,0.35),inset 0 10px 24px rgba(0,0,0,0.45) !important}"
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

RAIL_CSS = (".rail.cs-rail{padding-top:22px;padding-bottom:40px;padding-left:12px;margin-left:-12px}"
            ".rail.cs-rail .cs-sill{left:-10px;right:-10px}")

def apply(s, marker, rail=False):
    if 'class="cs-wrap"' not in s or marker not in s.split('class="cs-wrap"')[0] or True:
        s, n = wrap(s, marker, rail)
    if rail:
        s = s.replace('class="grid-3 rail"', 'class="grid-3 rail cs-rail"')
    add = ''
    if '.cs-wrap{' not in s: add += CSS
    if rail and '.rail.cs-rail{' not in s: add += RAIL_CSS
    if add: s = s.replace('</style>', add + '</style>', 1)
    return s, n

if __name__ == '__main__':
    f, marker = sys.argv[1], sys.argv[2]
    rail = len(sys.argv) > 3 and sys.argv[3] == 'rail'
    s = open(f).read()
    s, n = apply(s, marker, rail)
    open(f, 'w').write(s)
    print(f, 'wrapped', n)
