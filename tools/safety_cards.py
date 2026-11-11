"""Safety page cards: OSHA rule labels and a scaffold outline on the card frame."""
import re, sys
f = sys.argv[1]
s = open(f).read()
labels = ['OSHA 1926.451', 'OSHA 1926.95', 'OSHA 1926.25']
seq = iter(labels * 2)  # template copy, then prerendered copy
s = re.sub(r'padding-top: 6px">Standard</span>', lambda m: 'padding-top: 6px">%s</span>' % next(seq), s)
assert 'padding-top: 6px">Standard<' not in s
frame = 'pointer-events: none; border-radius: 50% 50% 0 0 / 14% 14% 0 0"></div>'
n = s.count(frame)
s = s.replace(frame, frame + '\n        <div class="scaf" aria-hidden="true"></div>')
bay = ("<svg xmlns='http://www.w3.org/2000/svg' width='34' height='46' viewBox='0 0 34 46'>"
       "<g fill='none' stroke-width='1'>"
       "<path d='M1.5 0V46M32.5 0V46' stroke='rgba(244,104,156,0.75)'/>"
       "<path d='M1.5 .5H32.5M1.5 .5L32.5 46M32.5 .5L1.5 46' stroke='rgba(255,255,255,0.4)'/>"
       "</g></svg>")
from urllib.parse import quote
url = "url(\"data:image/svg+xml," + quote(bay, safe="='/:,() .") + "\")"
css = (".scaf{position:absolute;inset:14px;pointer-events:none;border-radius:50% 50% 0 0 / 14% 14% 0 0;"
       "background-image:BAY,BAY;background-repeat:repeat-y,repeat-y;background-size:34px 46px,34px 46px;"
       "background-position:10px 0,calc(100% - 10px) 0;"
       "-webkit-mask-image:linear-gradient(180deg,#000 0%,#000 42%,transparent 78%);mask-image:linear-gradient(180deg,#000 0%,#000 42%,transparent 78%)}"
       "@media (max-width:760px){.scaf{background-size:26px 36px,26px 36px;background-position:8px 0,calc(100% - 8px) 0}}").replace("BAY", url)
css += '.scaf + div > span:last-child{white-space:nowrap}.scaf + div .corner-num{font-size:100px !important}' + '.scaf + div{padding-left:74px !important;padding-right:74px !important}@media (max-width:760px){.scaf + div{padding-left:62px !important;padding-right:62px !important}}'
s = s.replace('</style>', css + '</style>', 1)
open(f, 'w').write(s)
print('frames', n)
