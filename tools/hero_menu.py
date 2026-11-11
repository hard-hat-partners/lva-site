"""Shorter subpage heroes (not the homepage) and a solid black scrolled menu bar.
Usage: python3 -I tools/hero_menu.py site/*.html"""
import sys
HERO = (".hero-sub{height:640px !important;min-height:0 !important}"
        "@media (max-width:1100px){.hero-sub{height:460px !important}}"
        "@media (max-width:760px){.hero-sub{height:460px !important;min-height:0 !important}.hero-sub > .wrap{padding-top:118px !important;padding-bottom:34px !important}}")
STICK = ".stick{background:#000 !important;-webkit-backdrop-filter:none !important;backdrop-filter:none !important}div:has(> #pbar){background:#000 !important}.mbar{bottom:calc(18px + env(safe-area-inset-bottom, 0px)) !important}div:has(> #pbar){opacity:0;transition:opacity .25s ease}body:has(.stick) div:has(> #pbar){opacity:1}"
for f in sys.argv[1:]:
    s = open(f).read()
    add = ''
    if 'class="hero-sub"' in s and '.hero-sub{height:540px' not in s: add += HERO
    if 'class="stick"' in s and '.stick{background:#000' not in s: add += STICK
    if add:
        s = s.replace('</style>', add + '</style>', 1); open(f, 'w').write(s)
    print(f, 'hero' if HERO in add else '-', 'stick' if STICK in add else '-')
