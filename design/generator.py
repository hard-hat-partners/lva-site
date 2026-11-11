import json, os, sys

OUT = sys.argv[1]
NOW = sys.argv[2]
A = json.load(open('/home/claude/media/assets.json'))
os.makedirs(OUT, exist_ok=True)

OBS = "#121216"      # obsidian
BAS = "#1D1D23"      # basalt
LIME = "#FBFAF8"     # limestone
SAND = "#ECEBE9"
STUC = "#FBF9F6"
PINK = "#E7286F"     # brand pink, large type and lines
PINKTX = "#C21C5A"   # pink for small text on light
PINKDK = "#F4689C"   # pink for small text on dark
INK = "#1A1A20"
MUTED = "#55525A"
LINE = "#DCD3C7"
ONDARK = "#C8C4CC"
SERIF = "'Cinzel', 'Times New Roman', serif"
ITAL = "'Cormorant Garamond', Georgia, serif"
SANS = "'Jost', system-ui, sans-serif"

PHONE = "(214) 875-3606"
TEL = "tel:2148753606"
EMAIL = "laura@lvamayanstucco.com"
ADDR1 = "11258 Goodnight"
ADDR2 = "Dallas, Texas 75229"

PAGES = [
    ("home", "Main", "Home", "LVA Mayan Stucco | Stucco, EIFS and Stone in Dallas Fort Worth"),
    ("services", "Services", "Services", "Stucco, EIFS, Stone and Cast Stone Services | LVA Mayan Stucco"),
    ("why", "Why", "Our Promise", "Our Promise | LVA Mayan Stucco"),
    ("projects", "Projects", "Projects", "Projects | LVA Mayan Stucco"),
    ("contact", "Contact", "Contact", "Contact | LVA Mayan Stucco"),
    ("privacy", "Privacy", "Privacy & Terms", "Privacy Policy and Terms of Use | LVA Mayan Stucco"),
]
NAV = ["home", "services", "why", "projects"]
STEM = {p[0]: p[1] for p in PAGES}
LABEL = {p[0]: p[2] for p in PAGES}


def img(k):
    return A[k]


def ph(n, prefix):
    return [img(f"{prefix}-{i}") for i in range(1, n + 1)]


PROJECTS = [
    ("Vickery by Toll Brothers", "Residential Tract", "Flower Mound, TX", ph(8, "vickery")),
    ("TRU by Hilton", "Commercial", "Dallas, TX", ph(8, "tru")),
    ("Town Lake Subdivision by Toll Brothers", "Residential Tract", "Flower Mound, TX", ph(6, "townlake")),
    ("Starwood Village", "Commercial", "Frisco, TX", ph(3, "starwood")),
    ("Landon Homes in Vickery Subdivision", "Residential Tract", "Copper Canyon, TX", ph(5, "landon")),
    ("Holiday Inn Express", "Commercial", "Garland, TX", ph(2, "hie")),
    ("Oakbridge Subdivision by Toll Brothers", "Residential Tract", "Flower Mound, TX", ph(4, "oakbridge")),
    ("Verandah Way", "Residential Tract", "Irving, TX", ph(4, "verandah")),
    ("Montgomery Farm Estates", "Residential Tract", "Allen, TX", ph(3, "montgomery")),
    ("Marsh Lane Plaza", "Commercial", "Dallas, TX", ph(8, "marsh")),
    ("Star Trail by Toll Brothers", "Residential Tract", "Prosper, TX", ph(2, "startrail")),
    ("Brookfield Residential Model Home", "Residential Tract", "Frisco, TX", ph(2, "brookfield")),
    ("Cabell Townhomes by Pegaso Group", "Residential Tract", "Dallas, TX", ph(1, "cabell")),
    ("Travis Street", "Residential Custom", "Garland, TX", ph(3, "travis")),
    ("Walnut Hill", "Residential Custom", "Dallas, TX", ph(2, "walnut")),
    ("Comanche Way", "Residential Custom", "McKinney, TX", ph(2, "comanche")),
    ("Mount Gilead", "Residential Custom", "Keller, TX", ph(2, "gilead")),
    ("Gucci", "Commercial", "NorthPark Center, Dallas, TX", ph(1, "gucci")),
    ("Frisco Pet Hospital", "Commercial", "Frisco, TX", ph(1, "friscopet")),
    ("CSL Plasma", "Commercial", "Dallas, TX", ph(1, "csl")),
    ("Double Door Custom Homes", "Residential Custom", "Dallas, TX", ph(2, "doubledoor")),
    ("Dixon Model Home", "Residential Tract", "Flower Mound, TX", ph(2, "dixon")),
    ("Catina", "Residential Custom", "Preston Hollow, TX", []),
    ("Potomac", "Residential Custom", "Highland Park, TX", []),
]


CREDIT = {"Gucci": "Nomad Studio via designboom", "Frisco Pet Hospital": "Yelp", "CSL Plasma": "CSL Plasma on Nextdoor", "Mount Gilead": "Zillow", "Travis Street": "Zillow", "Walnut Hill": "Redfin", "Comanche Way": "Realtor.com"}


def link(key, sfx):
    return f"{STEM[key]}{sfx}.dc.html"


ICON = {
    "phone": '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"></path>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="1"></rect><path d="m3 7 9 6 9-6"></path>',
    "pin": '<path d="M12 21s-7-6.5-7-12a7 7 0 0 1 14 0c0 5.5-7 12-7 12z"></path><circle cx="12" cy="9" r="2.5"></circle>',
    "menu": '<path d="M3 7h18M3 12h18M3 17h18"></path>',
    "close": '<path d="M6 6l12 12M18 6 6 18"></path>',
    "arrow": '<path d="M4 12h16M14 6l6 6-6 6"></path>',
    "left": '<path d="M15 5l-7 7 7 7"></path>',
    "right": '<path d="M9 5l7 7-7 7"></path>',
    "play": '<path d="M7 4v16l13-8z"></path>',
}


def ic(name, size=20, color="currentColor", sw=1.6):
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="{sw}" '
            f'stroke-linecap="square" stroke-linejoin="miter" aria-hidden="true">{ICON[name]}</svg>')


def fret(color=PINK, h=18, op=1.0, pid="f"):
    # Mayan stepped fret band, repeating pyramids with a stepped hook
    return (f'<svg width="100%" height="{h}" aria-hidden="true" style="display: block; opacity: {op}">'
            f'<defs><pattern id="{pid}" width="56" height="{h}" patternUnits="userSpaceOnUse">'
            f'<path d="M0 {h-1} H6 V{h-6} H12 V{h-11} H18 V{h-16} H38 V{h-11} H44 V{h-6} H50 V{h-1} H56" fill="none" stroke="{color}" stroke-width="1.4"></path>'
            f'<path d="M24 {h-1} V{h-9} H32 V{h-1}" fill="none" stroke="{color}" stroke-width="1.4"></path>'
            f'</pattern></defs><rect width="100%" height="{h}" fill="url(#{pid})"></rect></svg>')


def eyebrow(t, color=PINKTX, center=False):
    al = "justify-content: center;" if center else ""
    return (f'<div style="display: flex; align-items: center; gap: 14px; {al}font-family: {SANS}; font-size: 13px; font-weight: 500; letter-spacing: 0.32em; '
            f'text-transform: uppercase; color: {color}"><span style="width: 36px; height: 1px; background: {color}; flex: none"></span>{t}</div>')


def h2(t, color=INK, size="clamp(34px, 4.4vw, 58px)", center=False):
    al = "text-align: center;" if center else ""
    return f'<h2 style="margin: 0; font-family: {SERIF}; font-weight: 500; font-size: {size}; line-height: 1.12; letter-spacing: 0.02em; color: {color}; {al}">{t}</h2>'


def lede(t, color=MUTED, size="20px", maxw="620px", center=False):
    al = "text-align: center; margin-left: auto; margin-right: auto;" if center else ""
    return f'<p style="margin: 0; font-family: {SANS}; font-weight: 300; font-size: {size}; line-height: 1.75; color: {color}; max-width: {maxw}; {al}">{t}</p>'


def accent(t, color=INK, size="clamp(24px, 2.6vw, 34px)"):
    return f'<p style="margin: 0; font-family: {ITAL}; font-style: italic; font-weight: 400; font-size: {size}; line-height: 1.4; color: {color}">{t}</p>'


def btn(text, href, kind="pink"):
    base = (f"display: inline-flex; align-items: center; gap: 14px; min-height: 54px; padding: 0 32px; font-family: {SANS}; font-size: 13px; "
            f"font-weight: 500; letter-spacing: 0.24em; text-transform: uppercase; text-decoration: none; border-radius: 0")
    s = {"pink": f"background: {PINKTX}; color: #FFFFFF; border: 1px solid {PINKTX}",
         "ghost": "background: transparent; color: #FFFFFF; border: 1px solid rgba(255,255,255,0.55)",
         "dark": f"background: transparent; color: {INK}; border: 1px solid {INK}",
         "obs": f"background: {OBS}; color: #FFFFFF; border: 1px solid {OBS}"}[kind]
    return f'<a class="btn" href="{href}" style="{base}; {s}">{text}{ic("arrow", 16)}</a>'


def photo(src, alt, h="100%", minh="0", ratio=None, extra="", cls=""):
    r = f"aspect-ratio: {ratio};" if ratio else f"height: {h};"
    return (f'<div class="zoom {cls}" style="position: relative; width: 100%; {r} min-height: {minh}; overflow: hidden; background: {SAND}; {extra}">'
            f'<img src="{src}" alt="{alt}" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; display: block"></div>')


def header(page, sfx, overlay=False):
    col = "#FFFFFF" if overlay else INK
    bg = "transparent" if overlay else STUC
    pos = "position: absolute; top: 0; left: 0; right: 0; z-index: 20;" if overlay else "position: relative;"
    bord = "rgba(255,255,255,0.18)" if overlay else LINE
    logo = img("logo-pink")
    links = "".join(
        f'<a href="{link(k, sfx)}" style="font-family: {SANS}; font-size: 13px; font-weight: 500; letter-spacing: 0.24em; text-transform: uppercase; text-decoration: none; '
        f'color: {col}; padding: 10px 2px; border-bottom: 1px solid {(PINK if k == page else "transparent")}">{LABEL[k]}</a>' for k in NAV)
    mlinks = "".join(
        f'<a href="{link(k, sfx)}" style="display: block; padding: 20px 28px; font-family: {SERIF}; font-size: 22px; text-decoration: none; letter-spacing: 0.04em; '
        f'color: {PINKDK if k == page else "#FFFFFF"}; border-bottom: 1px solid rgba(255,255,255,0.1)">{LABEL[k]}</a>' for k in NAV + ["contact"])
    return f'''
<header style="{pos} background: {bg}; border-bottom: 1px solid {bord}">
  <div class="wrap" style="display: flex; align-items: center; justify-content: space-between; gap: 24px; padding-top: 22px; padding-bottom: 22px">
    <a href="{link("home", sfx)}" aria-label="LVA Mayan Stucco home" style="display: block; line-height: 0"><img src="{logo}" alt="Mayan Stucco" class="hdr-logo" style="width: 210px; height: auto; display: block"></a>
    <nav class="hide-sm" aria-label="Main" style="display: flex; align-items: center; gap: 40px">
      {links}
      <a href="{link("contact", sfx)}" style="font-family: {SANS}; font-size: 13px; font-weight: 500; letter-spacing: 0.24em; text-transform: uppercase; text-decoration: none; color: #FFFFFF; background: {PINKTX}; padding: 15px 24px">Start a Project</a>
    </nav>
    <button class="show-sm" type="button" aria-label="Open menu" onClick="{{{{toggleMenu}}}}" style="width: 48px; height: 48px; border: 1px solid {bord}; background: transparent; color: {col}; cursor: pointer; align-items: center; justify-content: center">{ic("menu", 22)}</button>
  </div>
  <sc-if value="{{{{menuOpen}}}}" hint-placeholder-val="{{{{false}}}}">
    <nav aria-label="Mobile" style="position: fixed; inset: 0; z-index: 60; background: {OBS}; display: flex; flex-direction: column">
      <div style="display: flex; justify-content: space-between; align-items: center; padding: 22px 20px; border-bottom: 1px solid rgba(255,255,255,0.1)">
        <img src="{img("logo-white")}" alt="Mayan Stucco" style="width: 180px; height: auto">
        <button type="button" aria-label="Close menu" onClick="{{{{toggleMenu}}}}" style="width: 48px; height: 48px; border: 1px solid rgba(255,255,255,0.25); background: transparent; color: #FFFFFF; cursor: pointer; display: inline-flex; align-items: center; justify-content: center">{ic("close", 22)}</button>
      </div>
      {mlinks}
      <div style="padding: 28px; display: flex; flex-direction: column; gap: 14px; font-family: {SANS}; font-size: 17px">
        <a href="{TEL}" style="color: {ONDARK}; text-decoration: none">{PHONE}</a>
        <a href="mailto:{EMAIL}" style="color: {ONDARK}; text-decoration: none">{EMAIL}</a>
      </div>
      <div style="margin-top: auto; padding-bottom: 24px">{fret(PINK, 18, 0.7, "fm")}</div>
    </nav>
  </sc-if>
</header>'''


SOCIAL = [
    ("Instagram", "https://www.instagram.com/lvamayanstucco/"),
    ("Facebook", "https://www.facebook.com/LVAMayanStucco/"),
    ("LinkedIn", "https://www.linkedin.com/company/lva-mayan-stucco"),
    ("YouTube", "https://www.youtube.com/channel/UCnYdd0J-kFnJsXYOpCXdUvw"),
]


def creds_footer():
    creds = [("seal", "Certified", "Woman-owned and operated"), ("shield", "Licensed", "Insured, including EIFS, and bonded"), ("hat", "OSHA", "Certified, safety first on every site"), ("pin", "DFW", "Commercial, industrial and residential")]
    CICON = {
        "seal": '<circle cx="12" cy="9" r="5.5"></circle><path d="M8.6 13.4 7 21l5-2.8 5 2.8-1.6-7.6"></path><path d="m9.6 9 1.6 1.6 3.2-3.2"></path>',
        "shield": '<path d="M12 3 4.5 6v5.5c0 4.6 3.2 8 7.5 9.5 4.3-1.5 7.5-4.9 7.5-9.5V6z"></path><path d="m8.8 12 2.2 2.2 4.3-4.4"></path>',
        "hat": '<path d="M3 17.5h18"></path><path d="M5 17.5V15a7 7 0 0 1 14 0v2.5"></path><path d="M10 8.3V6h4v2.3"></path><path d="M12 8v5"></path>',
        "pin": '<path d="M12 21s-6.5-6-6.5-11.2a6.5 6.5 0 0 1 13 0C18.5 15 12 21 12 21z"></path><path d="M9.2 10.6 12 6.6l2.8 4z"></path>',
    }
    cr = "".join(f'''<div class="cred" style="display: flex; align-items: center; gap: 22px; padding: 6px 26px; border-left: 1px solid rgba(255,255,255,0.14)">
          <span class="dia" aria-hidden="true" style="flex: none; width: 52px; height: 52px; border: 1px solid rgba(231,40,111,0.7); transform: rotate(45deg); display: flex; align-items: center; justify-content: center; background: rgba(18,18,22,0.6)"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="{PINK}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" style="transform: rotate(-45deg)">{CICON[ic_]}</svg></span>
          <div style="display: flex; flex-direction: column; gap: 6px; min-width: 0"><span style="font-family: {SERIF}; font-size: 26px; color: #FFFFFF; letter-spacing: 0.05em; line-height: 1">{a}</span><span style="font-family: {SANS}; font-weight: 300; font-size: 15px; line-height: 1.45; color: {ONDARK}">{b}</span></div>
        </div>''' for ic_, a, b in creds)
    return f'''
  <div style="position: relative; border-top: 1px solid rgba(255,255,255,0.08)">
    <div class="wrap grid-4 creds" style="position: relative; display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); padding-top: 52px; padding-bottom: 52px">{cr}</div>
  </div>'''


def footer(sfx):
    soc = "".join(f'<a href="{u}" style="color: {ONDARK}; text-decoration: none">{n.title() if n.isupper() else n}</a>' for n, u in SOCIAL)
    ql = "".join(f'<a href="{link(k, sfx)}" style="color: {ONDARK}; text-decoration: none">{LABEL[k]}</a>' for k in ["home", "services", "why", "projects", "contact"])
    lab = f"font-family: {SANS}; font-size: 12px; font-weight: 500; letter-spacing: 0.3em; text-transform: uppercase; color: {PINKDK}; margin-bottom: 8px"
    col = "display: flex; flex-direction: column; gap: 14px; font-size: 17px; font-weight: 300"
    return f'''
<footer style="position: relative; overflow: hidden; background: {BAS}; color: {ONDARK}; font-family: {SANS}">
  <div aria-hidden="true" style="position: absolute; inset: 0; background-image: url({img("monogram")}); background-size: 240px 240px; background-repeat: repeat; background-position: center top; filter: brightness(1.7)"></div>
  <div aria-hidden="true" style="position: absolute; inset: 0; background: rgba(29,29,35,0.55)"></div>
  <div style="position: relative">{fret(PINK, 18, 0.55, "ff")}</div>
  <div class="wrap grid-foot" style="position: relative; display: grid; grid-template-columns: minmax(0, 1.5fr) repeat(3, minmax(0, 1fr)); gap: 56px; align-items: start; padding-top: 88px; padding-bottom: 72px">
    <div style="display: flex; flex-direction: column; gap: 22px">
      <img src="{img("logo-stacked-white")}" alt="Mayan Stucco" style="width: 170px; height: auto">
      <p style="margin: 0; font-size: 16px; font-weight: 300; line-height: 1.75; max-width: 360px">LVA Mayan Stucco LLC is a certified woman-owned company installing stucco, EIFS, plaster, and stone and brick veneers on commercial, industrial and residential buildings throughout Dallas Fort Worth.</p>
    </div>
    <div style="{col}">
      <div style="{lab}">Explore</div>
      {ql}
    </div>
    <div style="{col}">
      <div style="{lab}">Contact</div>
      <a href="{TEL}" style="color: {ONDARK}; text-decoration: none">{PHONE}</a>
      <a href="mailto:{EMAIL}" style="color: {ONDARK}; text-decoration: none; word-break: break-all">{EMAIL}</a>
      <span>{ADDR1}<br>{ADDR2}</span>
    </div>
    <div style="{col}">
      <div style="{lab}">Follow</div>
      {soc}
    </div>
  </div>
  <div style="position: relative; border-top: 1px solid rgba(255,255,255,0.1)">
    <div class="wrap" style="display: flex; justify-content: space-between; flex-wrap: wrap; gap: 12px; padding-top: 22px; padding-bottom: 22px; font-size: 14px; font-weight: 300">
      <span>© LVA Mayan Stucco LLC. All Rights Reserved. · <a href="{link("privacy", sfx)}" style="color: {ONDARK}">Privacy &amp; Terms</a></span>
      <span>Website by USA-REM</span>
    </div>
  </div>
</footer>'''


def cta_band(sfx):
    seal_txt = "Certified woman-owned &#183; Dallas Fort Worth &#183; Stucco &#183; EIFS &#183; Plaster &#183; "
    seal = f'''<svg class="seal" viewBox="0 0 200 200" width="150" height="150" aria-hidden="true" style="display: block">
          <defs><path id="sealc{sfx}" d="M100 100 m-78 0 a78 78 0 1 1 156 0 a78 78 0 1 1 -156 0"></path></defs>
          <circle cx="100" cy="100" r="98" fill="{OBS}"></circle>
          <circle cx="100" cy="100" r="92" fill="none" stroke="rgba(244,104,156,0.6)" stroke-width="0.8"></circle>
          <circle cx="100" cy="100" r="60" fill="none" stroke="rgba(244,104,156,0.6)" stroke-width="0.8"></circle>
          <image href="{img("tri-pink")}" x="78" y="72" width="44" height="56"></image>
          <text style="font-family: {SANS}; font-size: 11px; text-transform: uppercase" fill="#FFFFFF"><textPath href="#sealc{sfx}" textLength="486" lengthAdjust="spacing">{seal_txt}</textPath></text>
        </svg>'''
    det = "".join(f'''<div style="display: flex; flex-direction: column; gap: 8px"><span style="font-family: {SANS}; font-size: 12px; font-weight: 500; letter-spacing: 0.3em; text-transform: uppercase; color: {PINKTX}">{k}</span><span style="font-family: {SANS}; font-weight: 400; font-size: 17px; line-height: 1.5; color: {INK}">{v}</span></div>''' for k, v in [("Call", f'<a href="{TEL}" style="color: {INK}; text-decoration: none">{PHONE}</a>'), ("Write", f'<a href="mailto:{EMAIL}" style="color: {INK}; text-decoration: none">{EMAIL}</a>'), ("Visit", f"{ADDR1}<br>Dallas, Texas")])
    return f'''
<section style="position: relative; background: #FBFAF8 url({img("stucco-white")}) repeat; background-size: 512px 512px; overflow: hidden">
  <div aria-hidden="true" style="position: absolute; left: 0; right: 0; top: 0; height: 3px; background: {PINK}"></div>
  
  <div class="wrap grid-intro" style="position: relative; display: grid; grid-template-columns: repeat(12, minmax(0, 1fr)); gap: 48px; align-items: center; padding-top: 150px; padding-bottom: 150px">
    <div style="grid-column: span 6; display: flex; flex-direction: column; gap: 30px; align-items: flex-start">
      {eyebrow("Begin your project", PINKTX)}
      <h2 style="margin: 0; font-family: {SERIF}; font-weight: 500; font-size: clamp(38px, 4.8vw, 66px); line-height: 1.08; letter-spacing: 0.02em; color: {INK}">Your walls deserve<br><span style="font-family: {ITAL}; font-style: italic; font-weight: 400; text-transform: none; letter-spacing: 0; font-size: 1.12em; color: {PINKTX}">a crew in pink.</span></h2>
      <p style="margin: 0; font-family: {SANS}; font-weight: 400; font-size: 20px; line-height: 1.7; color: #2A2A31; max-width: 540px">Tell us what you are building. We will walk you through scope, schedule and the right system, from the first estimate to the final coat.</p>
      <div style="display: flex; gap: 16px; flex-wrap: wrap; margin-top: 4px">{btn("Start a project", link("contact", sfx))}{btn("View our work", link("projects", sfx), "dark")}</div>
      <div style="display: flex; flex-wrap: wrap; gap: 24px 48px; width: 100%; margin-top: 18px; padding-top: 30px; border-top: 1px solid rgba(18,18,22,0.16)">{det}</div>
    </div>
    <div class="cta-art" style="grid-column: 8 / span 5; position: relative; padding: 0 28px 0 0">
      <div aria-hidden="true" class="deco" class="shp-step" style="position: absolute; top: -28px; right: 0; bottom: 56px; left: 56px; background: {BAS}; overflow: hidden">{monogram("mgcta" + sfx)}</div>
      {photo(img("vickery-1"), "Finished home by LVA Mayan Stucco", ratio="4 / 5")}
      <div class="deco" style="position: absolute; left: -64px; bottom: -48px">{seal}</div>
    </div>
  </div>
</section>'''


def page_hero(eb, title, sub, src, alt, sfx, page):
    return f'''
<section class="hero-sub" style="position: relative; background: {OBS}; overflow: hidden">
  <img src="{src}" alt="{alt}" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover">
  <div style="position: absolute; inset: 0; background: linear-gradient(180deg, rgba(12,12,15,0.88) 0%, rgba(12,12,15,0.55) 22%, rgba(12,12,15,0.42) 50%, rgba(12,12,15,0.88) 100%)"></div>
  {header(page, sfx, overlay=True)}
  <div class="wrap" style="position: relative; z-index: 2; height: 100%; display: flex; flex-direction: column; justify-content: flex-end; gap: 22px; padding-bottom: 88px">
    {eyebrow(eb, PINKDK)}
    <h1 style="margin: 0; font-family: {SERIF}; font-weight: 500; font-size: clamp(40px, 5vw, 72px); line-height: 1.04; letter-spacing: 0.02em; color: #FFFFFF; max-width: 1160px">{title}</h1>
    {lede(sub, "#E9E5EC", "21px", "660px")}
  </div>
</section>'''


def monogram(pid, *args, **kw):
    # luxury-canvas repeat built from the LVA logo mark: eye-pyramid and pink four-point star on a half-drop grid
    return f'<div aria-hidden="true" style="position: absolute; inset: 0; background-image: url({img("monogram")}); background-size: 240px 240px; background-repeat: repeat; background-position: center top"></div>'

def creds_block():
    brands = ["Total Wall", "STO", "Dryvit", "Senergy", "Parex"]
    tiles = "".join(f'''
        <div class="cred-tile" style="position: relative; background: rgba(29,29,35,0.82); display: flex; flex-direction: column; justify-content: space-between; gap: 40px; padding: 30px 26px; min-height: 190px; border-right: 1px solid rgba(255,255,255,0.12); border-bottom: 1px solid rgba(255,255,255,0.12)">
          <div style="display: flex; justify-content: space-between; align-items: center"><span style="font-family: {SANS}; font-size: 12px; letter-spacing: 0.3em; color: {PINKDK}">0{i+1}</span><span aria-hidden="true" style="width: 0; height: 0; border-left: 7px solid transparent; border-right: 7px solid transparent; border-bottom: 12px solid {PINK}"></span></div>
          <div style="display: flex; flex-direction: column; gap: 8px"><span style="font-family: {SERIF}; font-size: clamp(24px, 2.2vw, 32px); letter-spacing: 0.06em; color: #FFFFFF; line-height: 1.1">{b}</span><span style="font-family: {SANS}; font-weight: 300; font-size: 13px; letter-spacing: 0.22em; text-transform: uppercase; color: {ONDARK}">Certified applicator</span></div>
          <img class="cred-logo" src="{img("tri-white")}" alt="" aria-hidden="true" style="position: absolute; right: 22px; bottom: 24px; width: 34px; height: auto">
        </div>''' for i, b in enumerate(brands))
    tiles += f'''
        <div class="cred-tile" style="display: flex; flex-direction: column; justify-content: center; align-items: center; gap: 14px; padding: 30px 26px; min-height: 190px; background: {PINK}; border-bottom: 1px solid rgba(255,255,255,0.12)">
          <img src="{img("tri-white")}" alt="" aria-hidden="true" style="width: 40px; height: auto">
          <span style="font-family: {SERIF}; font-size: 20px; letter-spacing: 0.06em; color: #FFFFFF; text-align: center; line-height: 1.3">Licensed, insured<br>and bonded</span>
        </div>'''
    facts = "".join(f'<div style="display: flex; align-items: center; gap: 14px"><span aria-hidden="true" style="width: 8px; height: 8px; background: {PINK}; transform: rotate(45deg); flex: none"></span><span style="font-family: {SANS}; font-weight: 300; font-size: 17px; color: {ONDARK}">{t}</span></div>' for t in ["Certified woman-owned", "Insured, including EIFS", "OSHA certified crews", "Commercial, industrial and residential"])
    return f'''
<section style="position: relative; background: {BAS}; overflow: hidden">
  {monogram("mg1")}
  <div aria-hidden="true" style="position: absolute; inset: 0; background: radial-gradient(ellipse at 22% 50%, rgba(29,29,35,0.9) 0%, rgba(29,29,35,0.5) 38%, rgba(29,29,35,0) 70%)"></div>
  <div class="wrap grid-intro" style="position: relative; display: grid; grid-template-columns: repeat(12, minmax(0, 1fr)); gap: 48px; align-items: center; padding-top: 128px; padding-bottom: 128px">
    <div style="grid-column: span 4; display: flex; flex-direction: column; gap: 26px">
      {eyebrow("Credentials", PINKDK)}
      {h2("Certified for the systems architects specify.", "#FFFFFF", "clamp(30px, 3.2vw, 46px)")}
      {lede("Five wall systems, one crew trained to install each of them, with the licensing, insurance and bonding to match.", ONDARK, "18px", "420px")}
      <div style="display: flex; flex-direction: column; gap: 14px; margin-top: 6px">{facts}</div>
    </div>
    <div class="cred-grid" style="grid-column: 6 / span 7; display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); border-top: 1px solid rgba(255,255,255,0.12); border-left: 1px solid rgba(255,255,255,0.12)">{tiles}
    </div>
  </div>
</section>'''


SERVICES = [
    ("Stucco", "Walls built coat by coat, from lath to finish, for the homes families come back to every night.", "home-21-4"),
    ("EIFS", "Insulated exterior finish systems for the hotels, clinics and storefronts people step into every day. Fully insured for EIFS.", "tru-1"),
    ("Exterior Molding", "Trim, bands and surrounds that give a facade its character from the street.", "oakbridge-2"),
    ("Stonework", "Stone and brick veneers that make an entry feel like home the moment you pull in.", "home-22-1"),
    ("Cast Stone", "Cast stone accents finished to the line the designer drew.", "starwood-1"),
]


def castband():
    # cast stone belt course: limestone band with molded fillet, cove shadow, stone face and bead, scored into blocks
    tex = f"url({img('stucco-white')})"
    return (f'<div aria-hidden="true" style="position: relative; height: 64px; background: #E8E0D4 {tex} repeat; background-size: 512px 512px; box-shadow: 0 14px 22px rgba(0,0,0,0.45), 0 -10px 18px rgba(0,0,0,0.35); z-index: 2">'
            f'<div style="position: absolute; left: 0; right: 0; top: 0; height: 8px; background: linear-gradient(180deg, rgba(255,255,255,0.55), rgba(120,104,86,0.35))"></div>'
            f'<div style="position: absolute; left: 0; right: 0; top: 8px; height: 6px; background: linear-gradient(180deg, rgba(70,58,46,0.45), rgba(70,58,46,0))"></div>'
            f'<div style="position: absolute; left: 0; right: 0; top: 14px; bottom: 12px; background: repeating-linear-gradient(90deg, rgba(0,0,0,0) 0 238px, rgba(90,76,60,0.28) 238px 239px, rgba(255,255,255,0.4) 239px 240px), linear-gradient(180deg, rgba(255,255,255,0.18), rgba(90,76,60,0.12))"></div>'
            f'<div style="position: absolute; left: 0; right: 0; bottom: 4px; height: 8px; border-radius: 4px; background: linear-gradient(180deg, rgba(255,255,255,0.6), rgba(110,94,76,0.4))"></div>'
            f'<div style="position: absolute; left: 0; right: 0; bottom: 0; height: 4px; background: rgba(60,48,36,0.5)"></div></div>')


def home(sfx):
    svc = "".join(f'''
      <div class="acc-p" tabindex="0" style="position: relative; flex: 1 1 0; min-width: 0; overflow: hidden; background: {OBS}; cursor: default">
        <img src="{img(k)}" alt="{n} by LVA Mayan Stucco" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; display: block">
        <div class="acc-shade" aria-hidden="true" style="position: absolute; inset: 0; background: linear-gradient(180deg, rgba(12,12,15,0.2) 0%, rgba(12,12,15,0.35) 45%, rgba(12,12,15,0.92) 100%)"></div>
        <div aria-hidden="true" style="position: absolute; inset: 12px; border: 1px solid rgba(255,255,255,0.22); pointer-events: none"></div>
        <span style="position: absolute; top: 30px; left: 28px; font-family: {SERIF}; font-size: 16px; letter-spacing: 0.14em; color: {PINKDK}">0{i + 1}</span>
        <div style="position: absolute; left: 28px; right: 28px; bottom: 30px; display: flex; flex-direction: column; gap: 14px">
          <span class="acc-rule" aria-hidden="true" style="display: block; height: 2px; width: 40px; background: {PINK}"></span>
          <span class="acc-name" style="font-family: {SERIF}; font-weight: 500; font-size: 18px; letter-spacing: 0.06em; text-transform: uppercase; color: #FFFFFF; line-height: 1.15">{n}</span>
          <span class="acc-desc" style="font-family: {SANS}; font-weight: 300; font-size: 17px; line-height: 1.65; color: rgba(255,255,255,0.88); max-width: 420px">{d}</span>
        </div>
      </div>''' for i, (n, d, k) in enumerate(SERVICES))
    feat = [PROJECTS[0], PROJECTS[1], PROJECTS[2], PROJECTS[3], PROJECTS[4], PROJECTS[5]]
    def fcard(p, cls, ratio):
        n, c, l, ims = p
        return f'''
        <a class="{cls}" href="{link("projects", sfx)}" style="position: relative; display: block; text-decoration: none; overflow: hidden; background: {OBS}">
          {photo(ims[0], n, ratio=ratio)}
          <div style="position: absolute; inset: 0; background: linear-gradient(180deg, rgba(18,18,22,0) 30%, rgba(18,18,22,0.94) 100%)"></div>
          <div style="position: absolute; left: 28px; right: 28px; bottom: 26px; display: flex; flex-direction: column; gap: 6px">
            <span style="font-family: {SANS}; font-size: 12px; letter-spacing: 0.3em; text-transform: uppercase; color: #FFFFFF; opacity: 0.85; text-shadow: 0 1px 8px rgba(0,0,0,0.6)">{c} · {l}</span>
            <span style="font-family: {SERIF}; font-size: clamp(22px, 2.2vw, 30px); color: #FFFFFF; letter-spacing: 0.03em; text-shadow: 0 1px 12px rgba(0,0,0,0.5)">{n}</span>
          </div>
        </a>'''
    SW = [("Vickery by Toll Brothers", "vickery"), ("TRU by Hilton", "tru"), ("Town Lake Subdivision by Toll Brothers", "townlake"), ("Starwood Village", "starwood"), ("Landon Homes in Vickery Subdivision", "landon")]
    pmap = {p[0]: p for p in PROJECTS}
    swstage = "".join(f'<video class="sw-v v{i + 1}" src="{img("v-" + k + "-loop")}" poster="{pmap[n][3][0]}" autoplay muted loop playsinline aria-hidden="true" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; display: block"></video>' for i, (n, k) in enumerate(SW))
    swlist = "".join(f'''
        <li class="sw-row r{i + 1}" style="position: relative; flex: 1; border-bottom: 1px solid rgba(255,255,255,0.14)">
          <a href="{link("projects", sfx)}" style="display: grid; grid-template-columns: 44px minmax(0, 1fr); gap: 14px; align-items: center; height: 100%; padding: 20px 0; text-decoration: none">
            <span style="font-family: {SERIF}; font-size: 15px; letter-spacing: 0.12em; color: {PINKDK}">0{i + 1}</span>
            <span style="display: flex; flex-direction: column; gap: 6px; min-width: 0">
              <span class="sw-name" style="font-family: {SERIF}; font-size: clamp(19px, 1.7vw, 24px); letter-spacing: 0.04em; color: #FFFFFF; line-height: 1.2">{n}</span>
              <span style="font-family: {SANS}; font-size: 11px; letter-spacing: 0.26em; text-transform: uppercase; color: rgba(255,255,255,0.6)">{pmap[n][1]} · {pmap[n][2]}</span>
              <span class="sw-thumb" style="display: none; margin-top: 10px; aspect-ratio: 16 / 9; overflow: hidden; background: #000"><video src="{img("v-" + k + "-loop")}" poster="{pmap[n][3][0]}" autoplay muted loop playsinline aria-hidden="true" style="width: 100%; height: 100%; object-fit: cover; display: block"></video></span>
            </span>
          </a>
        </li>''' for i, (n, k) in enumerate(SW))
    mosaic = (fcard(feat[0], "m-a", "16 / 11") + fcard(feat[1], "m-b", "3 / 4") + fcard(feat[2], "m-c", "4 / 3")
              + fcard(feat[3], "m-d", "4 / 3") + fcard(feat[4], "m-e", "4 / 3"))
    sectors = [("Commercial", "Hotels, clinics, retail and shopping centers where travelers rest, patients heal and neighbors shop.", "hero-poster-2"),
               ("Residential Tract", "Whole neighborhoods for builders like Toll Brothers, delivered home after home on the builder's schedule.", "townlake-1"),
               ("Residential Custom", "One-of-a-kind homes where every wall carries an owner's vision.", "home-36-1")]
    sec = "".join(f'''
      <a class="shp-arch" href="{link("projects", sfx)}" style="position: relative; display: block; text-decoration: none; overflow: hidden; background: {OBS}">
        {photo(img(k), n, ratio="3 / 4")}
        <div style="position: absolute; inset: 0; background: linear-gradient(180deg, rgba(18,18,22,0.15) 0%, rgba(18,18,22,0.9) 100%)"></div>
        <div style="position: absolute; left: 32px; right: 32px; bottom: 32px; display: flex; flex-direction: column; gap: 12px">
          <span style="font-family: {SERIF}; font-size: 30px; color: #FFFFFF; letter-spacing: 0.03em">{n}</span>
          <span style="font-family: {SANS}; font-weight: 300; font-size: 17px; line-height: 1.6; color: #E4E0E8">{d}</span>
          <span style="display: inline-flex; gap: 10px; align-items: center; font-family: {SANS}; font-size: 12px; letter-spacing: 0.3em; text-transform: uppercase; color: {PINKDK}">View projects {ic("arrow", 14)}</span>
        </div>
      </a>''' for n, d, k in sectors)
    CICON = {
        "seal": '<circle cx="12" cy="9" r="5.5"></circle><path d="M8.6 13.4 7 21l5-2.8 5 2.8-1.6-7.6"></path><path d="m9.6 9 1.6 1.6 3.2-3.2"></path>',
        "shield": '<path d="M12 3 4.5 6v5.5c0 4.6 3.2 8 7.5 9.5 4.3-1.5 7.5-4.9 7.5-9.5V6z"></path><path d="m8.8 12 2.2 2.2 4.3-4.4"></path>',
        "hat": '<path d="M3 17.5h18"></path><path d="M5 17.5V15a7 7 0 0 1 14 0v2.5"></path><path d="M10 8.3V6h4v2.3"></path><path d="M12 8v5"></path>',
        "pin": '<path d="M12 21s-6.5-6-6.5-11.2a6.5 6.5 0 0 1 13 0C18.5 15 12 21 12 21z"></path><path d="M9.2 10.6 12 6.6l2.8 4z"></path>',
    }
    creds = [("seal", "Certified", "Woman-owned and operated"), ("shield", "Licensed", "Insured, including EIFS, and bonded"), ("hat", "OSHA", "Certified, safety first on every site"), ("pin", "DFW", "Commercial, industrial and residential")]
    cr = "".join(f'''<div class="cred" style="display: flex; align-items: center; gap: 22px; padding: 6px 26px; border-left: 1px solid rgba(255,255,255,0.14)">
          <span class="dia" aria-hidden="true" style="flex: none; width: 52px; height: 52px; border: 1px solid rgba(231,40,111,0.7); transform: rotate(45deg); display: flex; align-items: center; justify-content: center; background: rgba(18,18,22,0.6)"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="{PINK}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" style="transform: rotate(-45deg)">{CICON[ic_]}</svg></span>
          <div style="display: flex; flex-direction: column; gap: 6px; min-width: 0"><span style="font-family: {SERIF}; font-size: 26px; color: #FFFFFF; letter-spacing: 0.05em; line-height: 1">{a}</span><span style="font-family: {SANS}; font-weight: 300; font-size: 15px; line-height: 1.45; color: {ONDARK}">{b}</span></div>
        </div>''' for ic_, a, b in creds)
    names = ["Vickery", "TRU by Hilton", "Town Lake", "Starwood Village", "Holiday Inn Express", "Oakbridge", "Montgomery Farm Estates", "Verandah Way", "Landon Homes"]
    marquee = "".join(f'<span style="font-family: {SERIF}; font-size: clamp(26px, 3vw, 40px); color: #FFFFFF; letter-spacing: 0.04em; white-space: nowrap">{n}</span><span aria-hidden="true" style="color: {PINK}; font-size: 20px; text-shadow: 0 0 12px rgba(231,40,111,0.6)">▲</span>' for n in names)
    return f'''
<section class="hero" style="position: relative; background: {OBS}; overflow: hidden; min-height: {{{{heroH}}}}; display: flex; flex-direction: column">
  <video src="{img("hero-finished")}" poster="{img("hero-poster-3")}" autoplay muted loop playsinline aria-label="Aerial view of Starwood Village in Frisco" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover"></video>
  <div style="position: absolute; inset: 0; background: rgba(12,12,15,0.42)"></div>
  <div style="position: absolute; inset: 0; background: linear-gradient(180deg, rgba(12,12,15,0.78) 0%, rgba(12,12,15,0.35) 38%, rgba(12,12,15,0.55) 62%, rgba(12,12,15,0.95) 100%)"></div>
  {header("home", sfx, overlay=True)}
  <div class="wrap" style="position: relative; z-index: 2; flex: 1; display: flex; flex-direction: column; justify-content: flex-end; gap: 26px; padding-top: 140px; padding-bottom: 88px">
    {eyebrow("Stucco · EIFS · Stone · Dallas Fort Worth", PINKDK)}
    <h1 style="margin: 0; font-family: {SERIF}; font-weight: 500; font-size: clamp(42px, 6.6vw, 96px); line-height: 1.02; letter-spacing: 0.02em; color: #FFFFFF; max-width: 1080px">When you see pink, the job is being done right.</h1>
    {lede("A certified woman-owned crew building the walls of Dallas Fort Worth homes, hotels and storefronts, one relationship at a time through personal integrity and open communication.", "#E9E5EC", "21px", "680px")}
    <div style="display: flex; gap: 16px; flex-wrap: wrap">{btn("Explore our work", link("projects", sfx))}{btn("Start a project", link("contact", sfx), "ghost")}</div>
  </div>
</section>



<section style="background: #FBFAF8 url({img("stucco-white")}) repeat; background-size: 512px 512px">
  <div class="wrap grid-intro" style="display: grid; grid-template-columns: repeat(12, minmax(0, 1fr)); gap: 32px; align-items: center; padding-top: 140px; padding-bottom: 140px">
    <div style="grid-column: span 5; display: flex; flex-direction: column; gap: 28px">
      {eyebrow("Our promise")}
      {h2("The future of<br>stucco application.")}
      {accent("Professional. Accountable. Credible.", PINKTX)}
      <p style="margin: 0; font-family: {SANS}; font-weight: 400; font-size: 20px; line-height: 1.75; color: #2A2A31; max-width: 620px">Your building carries your name long after we pack up the scaffolds. That's why owners, builders, developers and designers across Dallas Fort Worth trust us with their walls: we show up when we say we will, we finish to the line you drew, and we treat your project like our reputation rides on it. Because it does.</p>
      <div>{btn("Our promise", link("why", sfx), "dark")}</div>
    </div>
    <div class="intro-art" style="grid-column: 7 / span 6; position: relative; padding-bottom: 90px">
      {photo(img("landon-1"), "Landon Homes in Vickery Subdivision, aerial", ratio="5 / 4", cls="shp-quoin")}
      <div class="float-img deco" style="position: absolute; left: -64px; bottom: 0; width: 44%; filter: drop-shadow(0 24px 40px rgba(18,18,22,0.3))">{photo(img("verandah-3"), "LVA crew on scaffolds at Verandah Way", ratio="3 / 4", cls="shp-arch")}</div>
      <img src="{img("tri-pink")}" alt="" aria-hidden="true" class="deco" style="position: absolute; right: -18px; top: -40px; width: 74px; height: auto; opacity: 0.9">
    </div>
  </div>
</section>

<section style="position: relative; background: {OBS}; overflow: hidden">
  <div style="position: relative; opacity: 0.6">{fret(PINK, 14, 0.7, "fmq1")}</div>
  <div style="display: flex; align-items: center; gap: 40px; padding: 30px 0; width: max-content" class="marquee">{marquee}{marquee}</div>
  <div style="position: relative; opacity: 0.6">{fret(PINK, 14, 0.7, "fmq2")}</div>
</section>

<section class="atelier" style="position: relative; background: #FBFAF8 url({img("stucco-white")}) repeat; background-size: 512px 512px; overflow: hidden">
  <div class="wrap" style="position: relative; padding-top: 130px; padding-bottom: 130px; display: flex; flex-direction: column; gap: 52px">
    <div style="display: flex; flex-direction: column; align-items: center; text-align: center; gap: 20px">
      {eyebrow("What we install")}
      {h2("Explore our craft.")}
      <p style="margin: 0; font-family: {SANS}; font-weight: 400; font-size: 18px; line-height: 1.7; color: #2A2A31; max-width: 560px">Five disciplines, one standard. Choose a craft to see where it lives and how we install it.</p>
    </div>
    <div role="tablist" aria-label="Our disciplines" class="at-tabs" style="display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 2px; padding: 2px; background: {OBS}; box-shadow: 0 24px 50px rgba(18,18,22,0.18)">
      <sc-for list="{{{{at.tabs}}}}" as="t" hint-placeholder-count="5">
        <button type="button" role="tab" aria-selected="{{{{t.sel}}}}" onClick="{{{{t.pick}}}}" class="at-tab" style="{{{{t.style}}}}"><span style="font-family: {SERIF}; font-size: 13px; letter-spacing: 0.14em; color: {PINKDK}">{{{{t.num}}}}</span><span style="font-family: {SERIF}; font-size: clamp(14px, 1.3vw, 19px); letter-spacing: 0.1em; text-transform: uppercase">{{{{t.name}}}}</span></button>
      </sc-for>
    </div>
    <div class="grid-intro at-body" style="display: grid; grid-template-columns: repeat(12, minmax(0, 1fr)); gap: 56px; align-items: center">
      <div style="grid-column: span 7; position: relative">
        <div aria-hidden="true" class="deco" style="position: absolute; top: -22px; left: -22px; right: 22px; bottom: 22px; border: 1px solid rgba(231,40,111,0.55)"></div>
        <div class="shp-quoin" style="position: relative; aspect-ratio: 16 / 11; overflow: hidden; background: #000">
          <sc-for list="{{{{at.imgs}}}}" as="m" hint-placeholder-count="5">
            <img src="{{{{m.src}}}}" alt="{{{{m.alt}}}}" style="{{{{m.style}}}}">
          </sc-for>
        </div>
        <div style="position: relative; display: flex; gap: 12px; margin-top: 14px">
          <sc-for list="{{{{at.thumbs}}}}" as="th" hint-placeholder-count="3">
            <button type="button" onClick="{{{{th.pick}}}}" aria-label="{{{{th.label}}}}" style="{{{{th.style}}}}"><img src="{{{{th.src}}}}" alt="" style="width: 100%; height: 100%; object-fit: cover; display: block"></button>
          </sc-for>
        </div>
      </div>
      <div role="tabpanel" style="grid-column: span 5; display: flex; flex-direction: column; gap: 26px">
        <div style="display: flex; align-items: flex-end; gap: 18px">
          <span style="font-family: {SERIF}; font-size: 110px; line-height: 0.8; color: transparent; -webkit-text-stroke: 1px rgba(194,28,90,0.85)">{{{{at.num}}}}</span>
          <span style="font-family: {SANS}; font-size: 12px; letter-spacing: 0.3em; text-transform: uppercase; color: {MUTED}; padding-bottom: 6px">of 05</span>
        </div>
        <h3 style="margin: 0; font-family: {SERIF}; font-weight: 500; font-size: clamp(34px, 3.6vw, 54px); letter-spacing: 0.05em; text-transform: uppercase; color: {INK}; line-height: 1.04">{{{{at.name}}}}</h3>
        <span aria-hidden="true" style="display: block; width: 72px; height: 2px; background: {PINK}"></span>
        <p style="margin: 0; font-family: {SANS}; font-weight: 400; font-size: 19px; line-height: 1.75; color: #2A2A31">{{{{at.desc}}}}</p>
        <div style="display: flex; flex-direction: column; gap: 12px">
          <span style="font-family: {SANS}; font-size: 12px; font-weight: 500; letter-spacing: 0.3em; text-transform: uppercase; color: {PINKTX}">Where you'll see it</span>
          <div style="display: flex; flex-wrap: wrap; gap: 10px">
            <sc-for list="{{{{at.uses}}}}" as="u" hint-placeholder-count="3">
              <span style="font-family: {SANS}; font-size: 13px; letter-spacing: 0.14em; text-transform: uppercase; color: {INK}; background: rgba(255,255,255,0.6); border: 1px solid rgba(18,18,22,0.22); padding: 9px 14px">{{{{u.t}}}}</span>
            </sc-for>
          </div>
        </div>
        <div style="display: flex; align-items: center; gap: 14px; margin-top: 6px; flex-wrap: wrap">
          {btn("See the projects", link("projects", sfx))}
          <button type="button" aria-label="Previous discipline" onClick="{{{{at.prev}}}}" class="at-arrow" style="width: 54px; height: 54px; background: transparent; color: {INK}; border: 1px solid rgba(18,18,22,0.35); cursor: pointer; display: inline-flex; align-items: center; justify-content: center">{ic("left", 20)}</button>
          <button type="button" aria-label="Next discipline" onClick="{{{{at.next}}}}" class="at-arrow" style="width: 54px; height: 54px; background: transparent; color: {INK}; border: 1px solid rgba(18,18,22,0.35); cursor: pointer; display: inline-flex; align-items: center; justify-content: center">{ic("right", 20)}</button>
        </div>
      </div>
    </div>
  </div>
</section>

<section style="position: relative; background: {BAS}; overflow: hidden">
  {monogram("mgsw")}
  <div aria-hidden="true" style="position: absolute; inset: 0; background: radial-gradient(ellipse at 22% 30%, rgba(29,29,35,0.9) 0%, rgba(29,29,35,0.5) 38%, rgba(29,29,35,0) 70%)"></div>
  <div class="wrap" style="position: relative; padding-top: 140px; padding-bottom: 140px; display: flex; flex-direction: column; gap: 64px">
    <div class="stack-sm" style="display: flex; justify-content: space-between; align-items: flex-end; gap: 32px">
      <div style="display: flex; flex-direction: column; gap: 24px">
        {eyebrow("Selected work", PINKDK)}
        {h2("Walls you can<br>drive past today.", "#FFFFFF")}
      </div>
      {btn("View full portfolio", link("projects", sfx), "ghost")}
    </div>
    <div class="sw grid-intro" style="display: grid; grid-template-columns: repeat(12, minmax(0, 1fr)); gap: 48px; align-items: stretch">
      <div class="sw-stage" style="grid-column: span 8; position: relative; min-height: 560px; overflow: hidden; background: #000">{swstage}
        <div aria-hidden="true" style="position: absolute; inset: 0; background: linear-gradient(180deg, rgba(12,12,15,0.15) 0%, rgba(12,12,15,0) 40%, rgba(12,12,15,0.75) 100%); pointer-events: none"></div>
        <div aria-hidden="true" style="position: absolute; inset: 16px; border: 1px solid rgba(255,255,255,0.22); pointer-events: none"></div>
        <div style="position: absolute; left: 40px; bottom: 34px; display: flex; align-items: center; gap: 12px; pointer-events: none"><span class="pulse" aria-hidden="true" style="width: 9px; height: 9px; border-radius: 50%; background: {PINK}"></span><span style="font-family: {SANS}; font-size: 11px; font-weight: 500; letter-spacing: 0.3em; text-transform: uppercase; color: #FFFFFF">Project films, shot on site</span></div>
      </div>
      <ol class="sw-list" style="grid-column: span 4; list-style: none; margin: 0; padding: 0 24px; display: flex; flex-direction: column; background: rgba(18,18,22,0.88); border-top: 1px solid rgba(255,255,255,0.14); box-shadow: 0 30px 60px rgba(0,0,0,0.35)">{swlist}</ol>
    </div>
  </div>
</section>



<section style="background: #FBFAF8 url({img("stucco-white")}) repeat; background-size: 512px 512px">
  <div class="wrap" style="padding-top: 140px; padding-bottom: 140px; display: flex; flex-direction: column; gap: 64px">
    <div style="display: flex; flex-direction: column; gap: 24px; align-items: center; text-align: center">
      {eyebrow("Who we build for", PINKTX, True)}
      {h2("Commercial, tract and custom.", INK, center=True)}
    </div>
    <div class="grid-3 rail" style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 24px">{sec}
    </div>
  </div>
</section>

{creds_block()}
{cta_band(sfx)}'''


def cornice(sill=False):
    # cast stone cornice: fascia, shadow reveal, dentil course, bead. Sill is a slimmer mirrored band.
    tex = f"url({img('stucco-white')})"
    if sill:
        return (f'<div aria-hidden="true" style="position: absolute; left: 0; right: 0; bottom: 0; height: 30px; background: {tex}; background-size: 512px 512px; '
                f'box-shadow: 0 -6px 14px rgba(60,48,36,0.12)">'
                f'<div style="position: absolute; left: 0; right: 0; top: 0; height: 8px; background: linear-gradient(180deg, rgba(255,255,255,0.7), rgba(120,104,86,0.25))"></div>'
                f'<div style="position: absolute; left: 0; right: 0; top: 8px; bottom: 0; background: linear-gradient(180deg, rgba(255,255,255,0.25), rgba(90,76,60,0.22))"></div></div>')
    return (f'<div aria-hidden="true" style="position: absolute; left: 0; right: 0; top: 0; height: 64px; z-index: 1; filter: drop-shadow(0 10px 12px rgba(60,48,36,0.18))">'
            f'<div style="height: 22px; background: {tex}; background-size: 512px 512px; position: relative"><div style="position: absolute; inset: 0; background: linear-gradient(180deg, rgba(90,76,60,0.18) 0%, rgba(255,255,255,0.35) 45%, rgba(110,94,76,0.28) 100%)"></div></div>'
            f'<div style="height: 4px; background: rgba(70,58,46,0.35)"></div>'
            f'<div style="height: 26px; position: relative; background: rgba(150,134,114,0.55)">'
            f'<div style="position: absolute; inset: 0 0 4px 0; background: repeating-linear-gradient(90deg, rgba(0,0,0,0) 0 10px, {LIME} 10px 28px); "></div>'
            f'<div style="position: absolute; inset: 0 0 4px 0; background: repeating-linear-gradient(90deg, rgba(0,0,0,0) 0 10px, rgba(255,255,255,0.55) 10px 12px, rgba(0,0,0,0) 12px 25px, rgba(90,76,60,0.35) 25px 28px), linear-gradient(180deg, rgba(255,255,255,0.3), rgba(90,76,60,0.18))"></div></div>'
            f'<div style="height: 8px; background: {tex}; background-size: 512px 512px; position: relative"><div style="position: absolute; inset: 0; background: linear-gradient(180deg, rgba(255,255,255,0.6), rgba(110,94,76,0.3)); border-radius: 0 0 4px 4px"></div></div>'
            f'<div style="height: 4px; background: {PINK}; opacity: 0.85"></div></div>')


def why(sfx):
    corners = [
        ("Professional", "Crews that show up ready, work clean and leave a site the way a builder would want their own home left."),
        ("Accountable", "On-time delivery, safety first and a schedule-minded, cost-conscious approach on every job we take."),
        ("Credible", "Certified applicators for Total Wall, STO, Dryvit, Senergy and Parex. Fully licensed, insured including EIFS, and bonded."),
    ]
    cimg = [("verandah-2", "LVA pink scaffolds on finished white stucco"), ("hero-poster-3", "Finished stucco facade"), ("tru-1", "TRU by Hilton exterior")]
    cc = "".join(f'''
      <div class="corner shp-arch" style="position: relative; overflow: hidden; min-height: 600px; background: {OBS}; display: flex; flex-direction: column; justify-content: space-between; box-shadow: 0 30px 60px rgba(40,32,24,0.22)">
        <img class="corner-img" src="{img(cimg[i][0])}" alt="{cimg[i][1]}" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; display: block">
        <div aria-hidden="true" style="position: absolute; inset: 0; background: linear-gradient(180deg, rgba(12,12,15,0.55) 0%, rgba(12,12,15,0.25) 38%, rgba(12,12,15,0.94) 100%)"></div>
        <div aria-hidden="true" style="position: absolute; inset: 14px; border: 1px solid rgba(255,255,255,0.22); pointer-events: none; border-radius: 50% 50% 0 0 / 14% 14% 0 0"></div>
        <div style="position: relative; display: flex; justify-content: space-between; align-items: flex-start; padding: 70px 40px 0">
          <span class="corner-num" style="font-family: {SERIF}; font-size: 120px; line-height: 0.8; color: transparent; -webkit-text-stroke: 1px rgba(255,255,255,0.75)">{["I", "II", "III"][i]}</span>
          <span style="font-family: {SANS}; font-size: 12px; letter-spacing: 0.32em; text-transform: uppercase; color: {PINKDK}; padding-top: 6px">Cornerstone</span>
        </div>
        <div style="position: relative; display: flex; flex-direction: column; gap: 18px; padding: 0 40px 44px">
          <span class="corner-rule" style="display: block; height: 2px; width: 48px; background: {PINK}"></span>
          <h3 style="margin: 0; font-family: {SERIF}; font-weight: 500; font-size: clamp(26px, 2.2vw, 34px); letter-spacing: 0.1em; text-transform: uppercase; color: #FFFFFF">{n}</h3>
          <p style="margin: 0; font-family: {SANS}; font-weight: 300; font-size: 17px; line-height: 1.75; color: rgba(255,255,255,0.82)">{d}</p>
        </div>
      </div>''' for i, (n, d) in enumerate(corners))
    gal = "".join(photo(img(k), a, ratio=r) for k, a, r in [("verandah-4", "Stucco wall finish at Verandah Way", "3 / 4"), ("tru-4", "Facade detail at TRU by Hilton", "3 / 4"), ("verandah-3", "LVA crew on scaffolds", "3 / 4")])
    film = "".join(f'<div class="film-card" style="flex: none; width: 300px; aspect-ratio: 4 / 5; overflow: hidden; position: relative"><img src="{img(k)}" alt="{a}" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; display: block"></div>' for k, a in [("verandah-4", "Stucco wall finish at Verandah Way"), ("tru-4", "Facade detail at TRU by Hilton"), ("verandah-3", "LVA crew on scaffolds"), ("starwood-1", "Starwood Village facade"), ("landon-1", "Landon project exterior"), ("townlake-1", "Town Lake project exterior"), ("oakbridge-1", "Oakbridge project exterior"), ("tru-2", "TRU by Hilton exterior")])
    tmfacts = "".join(f'<div style="display: flex; align-items: center; gap: 14px"><span aria-hidden="true" style="width: 8px; height: 8px; background: {PINK}; transform: rotate(45deg); flex: none"></span><span style="font-family: {SANS}; font-weight: 300; font-size: 17px; color: {ONDARK}">{t}</span></div>' for t in ["OSHA certified crews", "Safety first on every site", "Seen across Dallas Fort Worth"])
    return f'''{page_hero("Our promise", "A woman-owned crew with a standard you can see from the street.", "LVA Mayan Stucco installs stucco, EIFS, plaster, and stone and brick veneers on commercial, industrial and residential buildings throughout Dallas Fort Worth.", img("vickery-1"), "Vickery by Toll Brothers, aerial", sfx, "why")}

<section style="position: relative; background: #FBFAF8 url({img("stucco-white")}) repeat; background-size: 512px 512px">
  <div aria-hidden="true" class="deco caststone" style="position: absolute; inset: 0; pointer-events: none">
    <div style="position: absolute; left: 0; right: 0; top: 0; height: 26px; background: linear-gradient(180deg, rgba(29,29,35,0.05) 0%, rgba(255,255,255,0.7) 40%, rgba(29,29,35,0.07) 100%); border-bottom: 1px solid rgba(29,29,35,0.08)"></div>
    <div style="position: absolute; left: 0; right: 0; top: 26px; height: 8px; background: linear-gradient(180deg, rgba(29,29,35,0.07), rgba(29,29,35,0))"></div>
    <div style="position: absolute; left: 0; right: 0; bottom: 0; height: 22px; background: linear-gradient(180deg, rgba(29,29,35,0.06) 0%, rgba(255,255,255,0.7) 45%, rgba(29,29,35,0.06) 100%); border-top: 1px solid rgba(29,29,35,0.08)"></div>
  </div>
  <div class="wrap" style="position: relative; padding-top: 150px; padding-bottom: 150px; display: flex; flex-direction: column; gap: 64px">
    <div class="stack-sm" style="display: flex; justify-content: space-between; align-items: flex-end; gap: 32px">
      <div style="display: flex; flex-direction: column; gap: 24px; max-width: 720px">
        {eyebrow("Our cornerstones")}
        {h2("Three words on<br>every job we take.")}
      </div>
      <p style="margin: 0; font-family: {SANS}; font-weight: 400; font-size: 21px; line-height: 1.7; color: #2A2A31; max-width: 460px">We work with you as a partner to find the best building solution for your project, with personalized service and support every day.</p>
    </div>
    <div class="grid-3 corners" style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 36px; align-items: stretch">{cc}
    </div>
  </div>
  {cornice(True)}
</section>

<section class="tm-home" style="position: relative; background: {OBS}; overflow: hidden; min-height: 760px; display: flex; align-items: center">
  <img class="tm-img" src="{img("sig-scaffold")}" alt="LVA pink scaffolds at Starwood Village, Frisco" style="position: absolute; top: 0; bottom: 0; left: 22%; width: 100%; height: 100%; object-fit: cover; object-position: 20% center; display: block; -webkit-mask-image: linear-gradient(90deg, transparent 0%, #000 30%); mask-image: linear-gradient(90deg, transparent 0%, #000 30%)">
  <div class="tm-ov" aria-hidden="true" style="position: absolute; inset: 0; background: linear-gradient(90deg, rgba(12,12,15,0.95) 0%, rgba(12,12,15,0.86) 46%, rgba(12,12,15,0.3) 76%, rgba(12,12,15,0.1) 100%)"></div>
  <div class="wrap" style="position: relative; padding-top: 140px; padding-bottom: 140px">
    <div style="display: flex; flex-direction: column; gap: 28px; max-width: 560px; padding-left: 32px; border-left: 2px solid {PINK}">
      {eyebrow("Our trademark", PINKDK)}
      <h2 style="margin: 0; font-family: {SERIF}; font-weight: 500; font-size: clamp(38px, 4.6vw, 66px); line-height: 1.06; letter-spacing: 0.02em; color: #FFFFFF">Look for the<br><span style="font-family: {ITAL}; font-style: italic; font-weight: 400; letter-spacing: 0; font-size: 1.14em; color: {PINKDK}">pink scaffolds.</span></h2>
      <p style="margin: 0; font-family: {SANS}; font-weight: 300; font-size: 20px; line-height: 1.75; color: #E9E5EC">When you see pink on a jobsite in Dallas Fort Worth, LVA Mayan Stucco's professional crews are on the job. It is our promise in plain sight.</p>
      <div style="display: flex; align-items: center; gap: 14px; margin-top: 6px">
        <span class="pulse" aria-hidden="true" style="width: 10px; height: 10px; border-radius: 50%; background: {PINK}"></span>
        <span style="font-family: {SANS}; font-size: 12px; font-weight: 500; letter-spacing: 0.3em; text-transform: uppercase; color: #FFFFFF">On the job across Dallas Fort Worth</span>
      </div>
    </div>
  </div>
</section>

<section style="background: #FBFAF8 url({img("stucco-white")}) repeat; background-size: 512px 512px">
  <div class="wrap grid-intro" style="display: grid; grid-template-columns: repeat(12, minmax(0, 1fr)); gap: 32px; align-items: center; padding-top: 140px; padding-bottom: 140px">
    <div class="laura-art" style="grid-column: span 5; position: relative; padding: 0 36px 36px 0">
      <div aria-hidden="true" class="deco" style="position: absolute; top: 36px; left: 36px; right: 0; bottom: 0; background: {BAS}; overflow: hidden">{monogram("mglaura")}</div>
      <div aria-hidden="true" class="deco" style="position: absolute; top: -18px; left: -18px; width: 46%; height: 46%; border-top: 2px solid {PINK}; border-left: 2px solid {PINK}"></div>
      <div class="laura-photo" style="position: relative; box-shadow: 0 34px 60px rgba(18,18,22,0.28)">{photo(img("laura"), "Laura Ayala, Founder and CEO", ratio="1 / 1")}</div>
      <div class="deco" style="position: absolute; right: -6px; bottom: 70px; writing-mode: vertical-rl; transform: rotate(180deg); font-family: {SANS}; font-size: 11px; font-weight: 500; letter-spacing: 0.42em; text-transform: uppercase; color: #FFFFFF; mix-blend-mode: normal">Founder &#183; Owner &#183; CEO</div>
      <div class="deco" style="position: absolute; left: -28px; bottom: 0; background: {PINK}; color: #FFFFFF; padding: 16px 22px; display: flex; align-items: center; gap: 12px; box-shadow: 0 20px 40px rgba(194,28,90,0.35)"><img src="{img("tri-white")}" alt="" aria-hidden="true" style="width: 20px; height: auto"><span style="font-family: {ITAL}; font-style: italic; font-size: 22px; line-height: 1">Laura Ayala</span></div>
    </div>
    <div style="grid-column: 7 / span 6; display: flex; flex-direction: column; gap: 28px">
      {eyebrow("Meet our founder")}
      {h2("Laura Ayala")}
      {accent("Founder, owner and CEO", PINKTX, "26px")}
      {lede("As founder and owner, Laura is fully committed to getting the job done. She keeps a finger on the pulse of local market conditions so builders get realistic schedules and cost-conscious pricing. She built LVA to be the crew developers and builders trust with their most visible walls.", MUTED, "19px", "580px")}
      <div style="display: flex; flex-direction: column; gap: 14px; margin-top: 10px; padding-left: 28px; border-left: 2px solid {PINK}">
        <p style="margin: 0; font-family: {ITAL}; font-style: italic; font-size: clamp(24px, 2.4vw, 32px); line-height: 1.35; color: {INK}">“These cornerstones guide us in helping owners, contractors, developers and design professionals create beautiful interiors and exteriors for their projects.”</p>
        <span style="font-family: {SANS}; font-size: 13px; letter-spacing: 0.28em; text-transform: uppercase; color: {PINKTX}">Laura Ayala</span>
      </div>
    </div>
  </div>
</section>


{creds_block()}
{cta_band(sfx)}'''


CICON_L = {
    "seal": '<circle cx="12" cy="9" r="5.5"></circle><path d="M8.6 13.4 7 21l5-2.8 5 2.8-1.6-7.6"></path><path d="m9.6 9 1.6 1.6 3.2-3.2"></path>',
    "shield": '<path d="M12 3 4.5 6v5.5c0 4.6 3.2 8 7.5 9.5 4.3-1.5 7.5-4.9 7.5-9.5V6z"></path><path d="m8.8 12 2.2 2.2 4.3-4.4"></path>',
    "hat": '<path d="M3 17.5h18"></path><path d="M5 17.5V15a7 7 0 0 1 14 0v2.5"></path><path d="M10 8.3V6h4v2.3"></path><path d="M12 8v5"></path>',
    "pin": '<path d="M12 21s-6.5-6-6.5-11.2a6.5 6.5 0 0 1 13 0C18.5 15 12 21 12 21z"></path><path d="M9.2 10.6 12 6.6l2.8 4z"></path>',
}


def creds_light_items():
    items = [("seal", "Certified", "Woman-owned and operated"), ("shield", "Licensed", "Insured, including EIFS, and bonded"), ("hat", "OSHA", "Certified, safety first on every site"), ("pin", "DFW", "Commercial, industrial and residential")]
    cr = "".join(f'''<div class="cred cred-l" style="display: flex; align-items: center; gap: 22px; padding: 6px 26px; border-left: 1px solid rgba(18,18,22,0.14)">
          <span class="dia" aria-hidden="true" style="flex: none; width: 52px; height: 52px; border: 1px solid {PINKTX}; transform: rotate(45deg); display: flex; align-items: center; justify-content: center; background: rgba(255,255,255,0.7)"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="{PINKTX}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" style="transform: rotate(-45deg)">{CICON_L[k]}</svg></span>
          <div style="display: flex; flex-direction: column; gap: 6px; min-width: 0"><span style="font-family: {SERIF}; font-size: 26px; color: {INK}; letter-spacing: 0.05em; line-height: 1">{a}</span><span style="font-family: {SANS}; font-weight: 400; font-size: 15px; line-height: 1.45; color: #3A3A42">{b}</span></div>
        </div>''' for k, a, b in items)
    return cr


def creds_light():
    items = [("seal", "Certified", "Woman-owned and operated"), ("shield", "Licensed", "Insured, including EIFS, and bonded"), ("hat", "OSHA", "Certified, safety first on every site"), ("pin", "DFW", "Commercial, industrial and residential")]
    cr = "".join(f'''<div class="cred cred-l" style="display: flex; align-items: center; gap: 22px; padding: 6px 26px; border-left: 1px solid rgba(18,18,22,0.14)">
          <span class="dia" aria-hidden="true" style="flex: none; width: 52px; height: 52px; border: 1px solid {PINKTX}; transform: rotate(45deg); display: flex; align-items: center; justify-content: center; background: rgba(255,255,255,0.7)"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="{PINKTX}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" style="transform: rotate(-45deg)">{CICON_L[k]}</svg></span>
          <div style="display: flex; flex-direction: column; gap: 6px; min-width: 0"><span style="font-family: {SERIF}; font-size: 26px; color: {INK}; letter-spacing: 0.05em; line-height: 1">{a}</span><span style="font-family: {SANS}; font-weight: 400; font-size: 15px; line-height: 1.45; color: #3A3A42">{b}</span></div>
        </div>''' for k, a, b in items)
    return f'''
<section style="position: relative; background: {LIME} url({img("monogram-light")}) repeat; background-size: 240px 240px; background-position: center center; border-bottom: 1px solid rgba(18,18,22,0.1)">
  <div aria-hidden="true" style="position: absolute; inset: 0; background: rgba(251,250,248,0.35)"></div>
  <div class="wrap grid-4 creds" style="position: relative; display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); padding-top: 48px; padding-bottom: 48px">{cr}</div>
</section>'''


def projects_close(sfx):
    cr = creds_light_items()
    return f'''
<section style="position: relative; background: #FBFAF8 url({img("stucco-white")}) repeat; background-size: 512px 512px; overflow: hidden">
  <div class="wrap" style="position: relative; padding-top: 140px; padding-bottom: 120px; display: flex; flex-direction: column; align-items: center; text-align: center; gap: 30px">
    {eyebrow("Your project is next", PINKTX, True)}
    <h2 style="margin: 0; font-family: {SERIF}; font-weight: 500; font-size: clamp(36px, 4.8vw, 66px); line-height: 1.08; letter-spacing: 0.02em; color: {INK}">You have seen the work.<br><span style="font-family: {ITAL}; font-style: italic; font-weight: 400; letter-spacing: 0; font-size: 1.12em; color: {PINKTX}">Now picture your facade.</span></h2>
    <p style="margin: 0; font-family: {SANS}; font-weight: 400; font-size: 19px; line-height: 1.7; color: #2A2A31; max-width: 620px">Every project on this page started with one conversation. Tell us what you are building, and we will bring the same crews, the same standard and the same pink scaffolds to your site.</p>
    <div style="display: flex; gap: 16px; flex-wrap: wrap; justify-content: center; margin-top: 6px">{btn("Start your project", link("contact", sfx))}<a class="btn" href="{TEL}" style="display: inline-flex; align-items: center; gap: 12px; min-height: 54px; padding: 0 28px; font-family: {SANS}; font-size: 15px; letter-spacing: 0.12em; color: {INK}; text-decoration: none; border: 1px solid {INK}">{ic("phone", 16)} {PHONE}</a></div>
  </div>
  <div style="position: relative; border-top: 1px solid rgba(18,18,22,0.12)">
    <div class="wrap grid-4 creds" style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); padding-top: 44px; padding-bottom: 60px">{cr}</div>
  </div>
</section>'''


def projects(sfx):
    return f'''{page_hero("Our projects", "Proof you can drive past.", "Hotels, clinics, storefronts, whole neighborhoods and custom homes across Dallas Fort Worth. Choose a project to see the gallery.", img("townlake-1"), "Town Lake Subdivision by Toll Brothers, aerial", sfx, "projects")}

<section style="position: relative; background: #FBFAF8 url({img("stucco-white")}) repeat; background-size: 512px 512px">
  <div class="wrap" style="position: relative; padding-top: 96px; padding-bottom: {{{{gridPadB}}}}; display: flex; flex-direction: column; gap: 40px">
    <div class="stack-sm" style="display: flex; justify-content: space-between; align-items: center; gap: 24px">
      <div role="group" aria-label="Filter projects" style="display: flex; flex-wrap: wrap; gap: 10px">
        <sc-for list="{{{{filters}}}}" as="f" hint-placeholder-count="4">
          <button type="button" onClick="{{{{f.pick}}}}" aria-pressed="{{{{f.pressed}}}}" style="{{{{f.style}}}}">{{{{f.label}}}}</button>
        </sc-for>
      </div>
      <div style="font-family: {SANS}; font-weight: 300; font-size: 16px; color: {MUTED}">{{{{countLabel}}}}</div>
    </div>
    <sc-if value="{{{{hasWithPhotos}}}}" hint-placeholder-val="{{{{true}}}}">
    <div class="grid-3 pgrid" style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 44px 24px">
      <sc-for list="{{{{withPhotos}}}}" as="p" hint-placeholder-count="9">
        <article style="{{{{p.artStyle}}}}">
          <sc-if value="{{{{p.hasPhotos}}}}" hint-placeholder-val="{{{{true}}}}">
          <div style="position: relative">
            <button type="button" onClick="{{{{p.open}}}}" aria-label="{{{{p.openLabel}}}}" class="zoom" style="position: relative; display: block; width: 100%; aspect-ratio: 4 / 3; padding: 0; border: none; cursor: pointer; overflow: hidden; background: {SAND}">
              <img src="{{{{p.cover}}}}" alt="{{{{p.name}}}}" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover">
              <sc-if value="{{{{p.hasFilm}}}}" hint-placeholder-val="{{{{false}}}}">
                <video src="{{{{p.loop}}}}" poster="{{{{p.cover}}}}" autoplay muted loop playsinline preload="metadata" aria-hidden="true" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover"></video>
                <span style="position: absolute; left: 16px; top: 16px; display: inline-flex; align-items: center; gap: 8px; font-family: {SANS}; font-size: 11px; font-weight: 500; letter-spacing: 0.26em; text-transform: uppercase; color: #FFFFFF; background: {PINKTX}; padding: 8px 12px"><svg width="10" height="10" viewBox="0 0 10 10" aria-hidden="true"><path d="M2 1 9 5 2 9z" fill="#FFFFFF"></path></svg>Film</span>
              </sc-if>
              <span style="position: absolute; right: 16px; bottom: 16px; font-family: {SANS}; font-size: 12px; letter-spacing: 0.24em; text-transform: uppercase; color: #FFFFFF; background: rgba(18,18,22,0.72); padding: 9px 14px">{{{{p.countText}}}}</span>
            </button>
            <sc-if value="{{{{p.hasCredit}}}}" hint-placeholder-val="{{{{false}}}}">
              <button type="button" class="credit-tag" onClick="{{{{p.toggleCredit}}}}" aria-expanded="{{{{p.creditOpen}}}}" aria-label="{{{{p.creditLabel}}}}" title="{{{{p.creditLabel}}}}" style="position: absolute; left: 12px; top: 12px; z-index: 2; display: inline-flex; align-items: center; gap: 8px; height: 26px; padding: 0 9px; border: 1px solid rgba(255,255,255,0.45); background: rgba(18,18,22,0.55); color: #FFFFFF; cursor: pointer; font-family: {SANS}; font-size: 11px; letter-spacing: 0.14em; backdrop-filter: blur(4px); -webkit-backdrop-filter: blur(4px)"><span aria-hidden="true" style="font-size: 13px; letter-spacing: 0">©</span><sc-if value="{{{{p.creditOpen}}}}" hint-placeholder-val="{{{{false}}}}"><span style="text-transform: uppercase; white-space: nowrap">Photos courtesy of {{{{p.credit}}}}</span></sc-if></button>
            </sc-if>
          </div>
          </sc-if>
          <sc-if value="{{{{p.noPhotos}}}}" hint-placeholder-val="{{{{false}}}}">
            <div class="plaque" style="{{{{p.plaqueStyle}}}}">
              <div aria-hidden="true" style="position: absolute; inset: 0; background-image: url({img("monogram-light")}); background-size: 240px 240px; background-position: center center"></div>
              <div aria-hidden="true" style="position: absolute; inset: 0; background: radial-gradient(ellipse at 50% 50%, rgba(251,250,248,0.96) 0%, rgba(251,250,248,0.65) 60%, rgba(251,250,248,0.2) 100%)"></div>
              <div aria-hidden="true" style="position: absolute; inset: 14px; border: 1px solid rgba(194,28,90,0.45)"></div>
              <div style="position: relative; display: flex; flex-direction: column; align-items: center; gap: 14px; text-align: center; padding: 28px">
                <img src="{img("tri-pink")}" alt="" aria-hidden="true" style="width: 30px; height: auto">
                <span style="font-family: {SERIF}; font-size: {{{{p.plaqueSize}}}}; letter-spacing: 0.12em; text-transform: uppercase; color: {INK}; line-height: 1.1">{{{{p.name}}}}</span>
                <span style="font-family: {SANS}; font-size: 12px; letter-spacing: 0.32em; text-transform: uppercase; color: {PINKTX}">{{{{p.plaqueNote}}}}</span>
              </div>
            </div>
          </sc-if>

          <div style="display: flex; flex-direction: column; gap: 6px">
            <span style="font-family: {SANS}; font-size: 12px; letter-spacing: 0.3em; text-transform: uppercase; color: {PINKTX}">{{{{p.cat}}}} · {{{{p.loc}}}}</span>
            <h3 style="margin: 0; font-family: {SERIF}; font-weight: 500; font-size: 24px; letter-spacing: 0.03em; color: {INK}">{{{{p.name}}}}</h3>
          </div>
        </article>
      </sc-for>
    </div>
    </sc-if>
  </div>
</section>
<sc-if value="{{{{hasPlaques}}}}" hint-placeholder-val="{{{{true}}}}">
<section style="position: relative; background: {BAS}; overflow: hidden">
  <div aria-hidden="true" style="position: absolute; inset: 0; background-image: url({img("monogram")}); background-size: 240px 240px; background-position: center top; filter: brightness(1.7)"></div>
  <div aria-hidden="true" style="position: absolute; inset: 0; background: rgba(29,29,35,0.4)"></div>
  <div class="wrap" style="position: relative; padding-top: 110px; padding-bottom: 140px; display: flex; flex-direction: column; gap: 48px">
    <div style="display: flex; flex-direction: column; gap: 18px; align-items: center; text-align: center">
      {eyebrow("The portfolio continues", PINKDK, True)}
      {h2("More walls with our name on them.", "#FFFFFF", "clamp(28px, 3.4vw, 46px)", center=True)}
      <p style="margin: 0; font-family: {SANS}; font-weight: 300; font-size: 17px; line-height: 1.7; color: {ONDARK}; max-width: 560px">Commercial landmarks and private residences across Dallas Fort Worth. Private residences, galleries coming soon.</p>
    </div>
    <div class="pgrid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 44px 24px; width: 100%; max-width: 920px; margin: 0 auto">
      <sc-for list="{{{{noPhotos}}}}" as="p" hint-placeholder-count="6">
        <article style="{{{{p.artStyle}}}}">
          <sc-if value="{{{{p.hasPhotos}}}}" hint-placeholder-val="{{{{true}}}}">
            <button type="button" onClick="{{{{p.open}}}}" aria-label="{{{{p.openLabel}}}}" class="zoom" style="position: relative; display: block; width: 100%; aspect-ratio: 4 / 3; padding: 0; border: none; cursor: pointer; overflow: hidden; background: {SAND}">
              <img src="{{{{p.cover}}}}" alt="{{{{p.name}}}}" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover">
              <sc-if value="{{{{p.hasFilm}}}}" hint-placeholder-val="{{{{false}}}}">
                <video src="{{{{p.loop}}}}" poster="{{{{p.cover}}}}" autoplay muted loop playsinline preload="metadata" aria-hidden="true" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover"></video>
                <span style="position: absolute; left: 16px; top: 16px; display: inline-flex; align-items: center; gap: 8px; font-family: {SANS}; font-size: 11px; font-weight: 500; letter-spacing: 0.26em; text-transform: uppercase; color: #FFFFFF; background: {PINKTX}; padding: 8px 12px"><svg width="10" height="10" viewBox="0 0 10 10" aria-hidden="true"><path d="M2 1 9 5 2 9z" fill="#FFFFFF"></path></svg>Film</span>
              </sc-if>
              <span style="position: absolute; right: 16px; bottom: 16px; font-family: {SANS}; font-size: 12px; letter-spacing: 0.24em; text-transform: uppercase; color: #FFFFFF; background: rgba(18,18,22,0.72); padding: 9px 14px">{{{{p.countText}}}}</span>
            </button>
          </sc-if>
          <sc-if value="{{{{p.noPhotos}}}}" hint-placeholder-val="{{{{false}}}}">
            <div class="plaque" style="{{{{p.plaqueStyle}}}}">
              <div aria-hidden="true" style="position: absolute; inset: 0; background-image: url({img("monogram-light")}); background-size: 240px 240px; background-position: center center"></div>
              <div aria-hidden="true" style="position: absolute; inset: 0; background: radial-gradient(ellipse at 50% 50%, rgba(251,250,248,0.96) 0%, rgba(251,250,248,0.65) 60%, rgba(251,250,248,0.2) 100%)"></div>
              <div aria-hidden="true" style="position: absolute; inset: 14px; border: 1px solid rgba(194,28,90,0.45)"></div>
              <div style="position: relative; display: flex; flex-direction: column; align-items: center; gap: 14px; text-align: center; padding: 28px">
                <img src="{img("tri-pink")}" alt="" aria-hidden="true" style="width: 30px; height: auto">
                <span style="font-family: {SERIF}; font-size: {{{{p.plaqueSize}}}}; letter-spacing: 0.12em; text-transform: uppercase; color: {INK}; line-height: 1.1">{{{{p.name}}}}</span>
                <span style="font-family: {SANS}; font-size: 12px; letter-spacing: 0.32em; text-transform: uppercase; color: {PINKTX}">{{{{p.plaqueNote}}}}</span>
              </div>
            </div>
          </sc-if>

          <div style="display: flex; flex-direction: column; gap: 6px">
            <span style="font-family: {SANS}; font-size: 12px; letter-spacing: 0.3em; text-transform: uppercase; color: {PINKDK}">{{{{p.cat}}}} · {{{{p.loc}}}}</span>
            <h3 style="margin: 0; font-family: {SERIF}; font-weight: 500; font-size: 24px; letter-spacing: 0.03em; color: #FFFFFF">{{{{p.name}}}}</h3>
          </div>
        </article>
      </sc-for>
    </div>
  </div>
</section>
</sc-if>


<sc-if value="{{{{lb.on}}}}" hint-placeholder-val="{{{{false}}}}">
  <div role="dialog" aria-modal="true" aria-label="{{{{lb.name}}}} gallery" style="position: fixed; inset: 0; z-index: 80; background: rgba(12,12,15,0.97); display: flex; flex-direction: column">
    <div style="display: flex; justify-content: space-between; align-items: center; gap: 16px; padding: 18px clamp(16px, 3vw, 40px); border-bottom: 1px solid rgba(255,255,255,0.1)">
      <div style="display: flex; flex-direction: column; gap: 4px; min-width: 0">
        <span style="font-family: {SANS}; font-size: 12px; letter-spacing: 0.3em; text-transform: uppercase; color: {PINKDK}">{{{{lb.cat}}}} · {{{{lb.loc}}}}</span>
        <span style="font-family: {SERIF}; font-size: clamp(18px, 2vw, 26px); color: #FFFFFF">{{{{lb.name}}}}</span>
      </div>
      <button type="button" aria-label="Close gallery" onClick="{{{{lb.close}}}}" style="flex: none; width: 48px; height: 48px; background: transparent; color: #FFFFFF; border: 1px solid rgba(255,255,255,0.3); cursor: pointer; display: inline-flex; align-items: center; justify-content: center">{ic("close", 22)}</button>
    </div>
    <div style="flex: 1; min-height: 0; position: relative; display: flex; align-items: center; justify-content: center; padding: 20px clamp(56px, 6vw, 96px)">
      <sc-if value="{{{{lb.isImg}}}}" hint-placeholder-val="{{{{true}}}}">
        <img src="{{{{lb.src}}}}" alt="{{{{lb.alt}}}}" style="max-width: 100%; max-height: 100%; object-fit: contain; display: block">
        <sc-if value="{{{{lb.hasCredit}}}}" hint-placeholder-val="{{{{false}}}}">
          <span style="position: absolute; right: clamp(56px, 6vw, 96px); bottom: 26px; font-family: {SANS}; font-size: 11px; letter-spacing: 0.18em; text-transform: uppercase; color: rgba(255,255,255,0.75); background: rgba(12,12,15,0.6); padding: 6px 10px">© {{{{lb.creditText}}}}</span>
        </sc-if>
      </sc-if>
      <sc-if value="{{{{lb.isVid}}}}" hint-placeholder-val="{{{{false}}}}">
        <video src="{{{{lb.src}}}}" poster="{{{{lb.poster}}}}" controls autoplay playsinline preload="auto" aria-label="{{{{lb.alt}}}}" style="max-width: 100%; max-height: 100%; display: block; background: #000"></video>
      </sc-if>
      <button type="button" aria-label="Previous photo" onClick="{{{{lb.prev}}}}" style="position: absolute; left: clamp(4px, 1.5vw, 24px); top: 50%; transform: translateY(-50%); width: 48px; height: 48px; background: rgba(255,255,255,0.08); color: #FFFFFF; border: 1px solid rgba(255,255,255,0.25); cursor: pointer; display: inline-flex; align-items: center; justify-content: center">{ic("left", 22)}</button>
      <button type="button" aria-label="Next photo" onClick="{{{{lb.next}}}}" style="position: absolute; right: clamp(4px, 1.5vw, 24px); top: 50%; transform: translateY(-50%); width: 48px; height: 48px; background: rgba(255,255,255,0.08); color: #FFFFFF; border: 1px solid rgba(255,255,255,0.25); cursor: pointer; display: inline-flex; align-items: center; justify-content: center">{ic("right", 22)}</button>
    </div>
    <div style="padding: 14px 20px 22px; display: flex; gap: 10px; justify-content: center; overflow-x: auto">
      <sc-for list="{{{{lb.thumbs}}}}" as="t" hint-placeholder-count="5">
        <button type="button" onClick="{{{{t.pick}}}}" aria-label="{{{{t.label}}}}" style="{{{{t.style}}}}"><img src="{{{{t.src}}}}" alt="" style="width: 100%; height: 100%; object-fit: cover; display: block"><sc-if value="{{{{t.vid}}}}" hint-placeholder-val="{{{{false}}}}"><span aria-hidden="true" style="position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; background: rgba(194,28,90,0.55)"><svg width="16" height="16" viewBox="0 0 10 10"><path d="M2 1 9 5 2 9z" fill="#FFFFFF"></path></svg></span></sc-if></button>
      </sc-for>
    </div>
  </div>
</sc-if>
{projects_close(sfx)}'''


def contact_creds():
    items = [("Certified", "Woman-owned and operated"), ("Licensed", "Insured, including EIFS, and bonded"), ("OSHA", "Certified, safety first on every site"), ("DFW", "Commercial, industrial and residential")]
    return "".join(f'<div class="cred" style="display: flex; align-items: center; gap: 18px"><span class="dia" aria-hidden="true" style="flex: none; width: 14px; height: 14px; border: 1px solid {PINK}; transform: rotate(45deg); background: rgba(231,40,111,0.18)"></span><div style="display: flex; flex-direction: column; gap: 2px"><span style="font-family: {SERIF}; font-size: 19px; letter-spacing: 0.06em; color: #FFFFFF">{a}</span><span style="font-family: {SANS}; font-weight: 300; font-size: 14px; color: {ONDARK}">{b}</span></div></div>' for a, b in items)


def contact(sfx):
    field = f"width: 100%; box-sizing: border-box; min-height: 54px; padding: 14px 0; font-family: {SANS}; font-weight: 300; font-size: 18px; color: {INK}; background: transparent; border: none; border-bottom: 1px solid #A9A1A8; border-radius: 0"
    lab = f"display: flex; flex-direction: column; gap: 6px; font-family: {SANS}; font-size: 12px; font-weight: 500; letter-spacing: 0.28em; text-transform: uppercase; color: {MUTED}"
    item = lambda t, v, h, f=SERIF, sz="24px": f'''<a href="{h}" style="display: flex; flex-direction: column; gap: 8px; text-decoration: none; padding: 26px 0; border-bottom: 1px solid rgba(255,255,255,0.12)"><span style="font-family: {SANS}; font-size: 12px; letter-spacing: 0.3em; text-transform: uppercase; color: {PINKDK}">{t}</span><span style="font-family: {f}; font-weight: 300; font-size: {sz}; color: #FFFFFF; overflow-wrap: anywhere">{v}</span></a>'''
    return f'''{page_hero("Start a project", "Your walls are in good hands.", "Tell us what you are building. A certified, licensed and insured crew is ready to bring your project to life across Dallas Fort Worth.", img("tru-2"), "TRU by Hilton, Dallas", sfx, "contact")}

<section style="background: #FBFAF8 url({img("stucco-white")}) repeat; background-size: 512px 512px">
  <div class="wrap grid-contact" style="display: grid; grid-template-columns: repeat(12, minmax(0, 1fr)); gap: 0; padding-top: 0; padding-bottom: 90px">
    <div class="lift" style="grid-column: span 5; background: {OBS}; padding: clamp(32px, 4vw, 64px); display: flex; flex-direction: column; margin-top: -80px; position: relative; z-index: 3">
      <img src="{img("tri-pink")}" alt="" aria-hidden="true" style="width: 46px; height: auto; margin-bottom: 18px">
      {item("Call", PHONE, TEL)}
      {item("Email", EMAIL, "mailto:" + EMAIL, SANS, "20px")}
      <div style="display: flex; flex-direction: column; gap: 8px; padding: 26px 0"><span style="font-family: {SANS}; font-size: 12px; letter-spacing: 0.3em; text-transform: uppercase; color: {PINKDK}">Office</span><span style="font-family: {SERIF}; font-size: 22px; color: #FFFFFF; line-height: 1.4">{ADDR1}<br>{ADDR2}</span></div>
      <p style="margin: 18px 0 0; font-family: {SANS}; font-weight: 300; font-size: 16px; line-height: 1.7; color: {ONDARK}">Serving commercial, industrial and residential projects throughout Dallas Fort Worth.</p>
      <div style="display: flex; flex-direction: column; gap: 14px; margin-top: 30px; padding-top: 28px; border-top: 1px solid rgba(255,255,255,0.12)"><span style="font-family: {SANS}; font-size: 12px; letter-spacing: 0.3em; text-transform: uppercase; color: {PINKDK}">Certified applicator for</span><div style="display: flex; flex-wrap: wrap; gap: 8px">{"".join(f'<span style="font-family: {SERIF}; font-size: 16px; letter-spacing: 0.08em; color: #FFFFFF; border: 1px solid rgba(244,104,156,0.5); padding: 8px 12px">{b}</span>' for b in ["Total Wall", "STO", "Dryvit", "Senergy", "Parex"])}</div></div>
    </div>
    <form name="contact" method="POST" data-netlify="true" netlify-honeypot="company-website" style="grid-column: 7 / span 6; padding-top: 96px; display: flex; flex-direction: column; gap: 30px; position: relative">
      {eyebrow("Start a project")}
      {h2("Tell us what you are building.", INK, "clamp(28px, 3vw, 40px)")}
      <p style="margin: -8px 0 0; font-family: {SANS}; font-weight: 400; font-size: 18px; line-height: 1.7; color: #2A2A31; max-width: 560px">Every project in our portfolio started with a note like this one. Share a few details and Laura's team will follow up personally. Prefer the phone? Call <a href="{TEL}" style="color: {PINKTX}">{PHONE}</a>.</p>
      <div class="grid-2" style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 30px">
        <label style="{lab}">Name<input type="text" name="name" autocomplete="name" required style="{field}"></label>
        <label style="{lab}">Company<input type="text" name="company" autocomplete="organization" style="{field}"></label>
        <label style="{lab}">Email<input type="email" name="email" autocomplete="email" required style="{field}"></label>
        <label style="{lab}">Phone<input type="tel" name="phone" autocomplete="tel" style="{field}"></label>
      </div>
      <label style="{lab}">Project type
        <select name="project-type" style="{field}">
          <option>Commercial</option><option>Residential Tract</option><option>Residential Custom</option><option>Other</option>
        </select></label>
      <label style="{lab}">Tell us about your project<textarea name="message" rows="4" style="{field}; min-height: 120px; resize: vertical"></textarea></label>
      <label style="position: absolute; left: -9999px" aria-hidden="true">Leave this empty<input type="text" name="company-website" tabindex="-1" autocomplete="off"></label>
      <div><button type="submit" class="btn" style="display: inline-flex; align-items: center; gap: 14px; min-height: 56px; padding: 0 34px; background: {PINKTX}; color: #FFFFFF; border: none; font-family: {SANS}; font-size: 13px; font-weight: 500; letter-spacing: 0.24em; text-transform: uppercase; cursor: pointer">Send message {ic("arrow", 16)}</button></div>
    </form>
  </div>
  <div class="wrap" style="padding-bottom: 130px; display: flex; flex-direction: column; gap: 40px">
    <div style="display: flex; flex-direction: column; align-items: center; text-align: center; gap: 18px; padding-top: 70px; border-top: 1px solid rgba(18,18,22,0.12)">
      {eyebrow("Why builders call us", PINKTX, True)}
      {h2("Qualified for the walls that matter.", INK, "clamp(28px, 3.4vw, 46px)", center=True)}
      <p style="margin: 0; font-family: {SANS}; font-weight: 400; font-size: 18px; line-height: 1.7; color: #2A2A31; max-width: 600px">Woman-owned, OSHA certified and fully insured, including EIFS. Owners, builders and designers across Dallas Fort Worth trust us because every credential is backed by crews who show up and finish right.</p>
    </div>
    <div class="grid-4 creds" style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr))">{creds_light_items()}</div>
  </div>
</section>'''


def privacy(sfx):
    secs = [
        ("Introduction", "LVA Mayan Stucco LLC is committed to being transparent about how our website operates. This page explains how we handle information and the terms under which you use our website."),
        ("Information We Collect", "When you contact us through our website, we collect the information you provide directly, such as your name, email address, phone number, and any details you include in your message. We use this information solely to respond to your inquiry and communicate with you about your project or request."),
        ("How We Use Your Information", "We use the information you provide to respond to inquiries, provide requested information, and communicate with you. We do not sell, rent, or share your personal information with third parties for marketing purposes."),
        ("Security and Analytics Tools", "Our website may use industry standard security and analytics tools to protect against spam and unauthorized use and to understand how visitors interact with our site. These tools help us maintain a secure and functional website."),
        ("Third Party Links", "Our website may contain links to third party websites, such as our Instagram, Facebook, LinkedIn, and YouTube pages. We are not responsible for the privacy practices or content of those sites and encourage you to review their policies directly."),
        ("Terms of Use", "By accessing and using lvamayanstucco.com, you agree to the following terms."),
        ("Acceptable Use", "This website is provided for informational purposes about LVA Mayan Stucco LLC and its services. You agree to use this site only for lawful purposes and in a manner that does not infringe on the rights of others."),
        ("Intellectual Property", "All content on this website, including text, images, graphics, logos, and video, is the property of LVA Mayan Stucco LLC or its content suppliers and is protected by applicable intellectual property laws. Unauthorized reproduction or distribution of any content is prohibited."),
        ("Accuracy of Information", "We make every effort to ensure the information on this site is current and accurate. However, we make no warranties regarding the completeness or accuracy of any content and reserve the right to make changes at any time without notice."),
        ("Limitation of Liability", "LVA Mayan Stucco LLC and its web services provider shall not be held liable for any direct, indirect, or incidental damages arising from your use of or inability to use this website."),
        ("Changes to This Policy", "We reserve the right to update this Privacy Policy and Terms of Use at any time. Updates will be reflected in the Last Updated date at the top of this page."),
    ]
    hs = f"margin: 48px 0 12px; font-family: {SERIF}; font-weight: 500; font-size: 26px; letter-spacing: 0.03em; color: {INK}"
    ps = f"margin: 0; font-family: {SANS}; font-weight: 300; font-size: 19px; line-height: 1.8; color: {MUTED}"
    body = "".join(f'<h2 style="{hs}">{h}</h2><p style="{ps}">{t}</p>' for h, t in secs)
    body += f'<h2 style="{hs}">Contact Us</h2><p style="{ps}">If you have any questions about this policy or how your information is handled, please email us at <a href="mailto:{EMAIL}" style="color: {PINKTX}">{EMAIL}</a>.</p>'
    return f'''
<section style="background: {OBS}; position: relative">
  {header("privacy", sfx, overlay=True)}
  <div class="wrap" style="position: relative; padding-top: 200px; padding-bottom: 80px; display: flex; flex-direction: column; gap: 20px">
    {eyebrow("Legal", PINKDK)}
    <h1 style="margin: 0; font-family: {SERIF}; font-weight: 500; font-size: clamp(36px, 5vw, 64px); line-height: 1.08; color: #FFFFFF">Privacy Policy and Terms of Use</h1>
    <div style="font-family: {SANS}; font-weight: 300; color: {ONDARK}; font-size: 17px">Last Updated: November 2026</div>
  </div>
  {fret(PINK, 18, 0.55, "fpr")}
</section>
<section style="background: {STUC}">
  <div class="wrap" style="padding-top: 40px; padding-bottom: 140px; max-width: 860px">{body}</div>
</section>'''


SVC = [
    ("01", "Stucco", "stucco", "Hand-applied, three-coat stucco over lath: scratch coat, brown coat and finish. We keep every coat hydrated so it cures hard, and we finish to the texture and color on your plans. Interior and exterior plaster too.", ["Custom homes", "Tract neighborhoods", "Commercial"], ("startrail-1", "Finished stucco, Star Trail by Toll Brothers"), ("svc-browncoat", "LVA crew applying brown coat"), ["Star Trail by Toll Brothers", "Vickery by Toll Brothers", "Cabell Townhomes"]),
    ("02", "EIFS", "eifs", "Exterior insulation and finish systems for hotels, retail centers, clinics and multifamily. We install as certified applicators for the leading system makers, and we are fully insured for EIFS.", ["Hotels", "Retail centers", "Multifamily"], ("tru-1", "TRU by Hilton, Dallas"), ("marsh-3", "Marsh Lane Plaza during installation"), ["TRU by Hilton", "Marsh Lane Plaza", "Holiday Inn Express"]),
    ("03", "Exterior Molding", "molding", "Trim, bands, sills and window surrounds, shaped and finished to match the wall around them. Molding is where a facade gets its character from the street.", ["Window surrounds", "Bands and sills", "Trim"], ("oakbridge-2", "Exterior molding at Oakbridge by Toll Brothers"), ("verandah-4", "Window surrounds at Verandah Way"), ["Oakbridge by Toll Brothers", "Verandah Way"]),
    ("04", "Stonework", "stone", "Stone and brick veneers set course by course for entries, facades and accent walls. Clean joints, level lines and a finish that makes a home feel settled the day it is done.", ["Entries", "Facades", "Accent walls"], ("home-22-1", "Stone veneer entry"), ("landon-2", "Stonework, Landon Homes in Vickery"), ["Landon Homes in Vickery", "Montgomery Farm Estates"]),
    ("05", "Cast Stone", "caststone", "Cast stone columns, caps and accents, set plumb and finished to the line the designer drew. The details people notice when they walk up to the door.", ["Columns", "Caps and accents", "Retail centers"], ("starwood-1", "Cast stone at Starwood Village"), ("starwood-2", "Starwood Village, Frisco"), ["Starwood Village"]),
]

SVID = {"eifs": "svc-tru", "caststone": "svc-starwood"}

PROC = [
    ("01", "Wrap and lath", "Weather barrier and metal lath go on first, fastened tight so every coat that follows has something solid to grip.", "marsh-7", "Lath at Marsh Lane Plaza"),
    ("02", "Scratch coat", "The first coat is scored and kept hydrated while it cures, so it bonds hard to the lath and to the coat that comes next.", "svc-scratch", "Scratch coat on a commercial parapet"),
    ("03", "Brown coat", "The brown coat builds the wall flat and true. This is where straight lines and clean corners are made.", "svc-browncoat", "Brown coat on a two-story home"),
    ("04", "Finish", "Texture and color go on last, matched to your plans and checked in daylight before our crew calls it done.", "startrail-2", "Finished stucco, Star Trail by Toll Brothers"),
]

WIP = [
    ("doubledoor-1", "Spanish colonial custom home", "Dallas"),
    ("doubledoor-2", "Double Door Custom Homes", "Dallas"),
    ("marsh-5", "Marsh Lane Plaza", "Dallas"),
    ("brookfield-2", "Brookfield Residential model", "Frisco"),
    ("marsh-6", "Marsh Lane Plaza", "Dallas"),
]


def services(sfx):
    idx = "".join(f'<a href="#{k}" class="svc-tab" style="display: flex; align-items: baseline; justify-content: center; gap: 12px; padding: 22px 18px; text-decoration: none; background: {BAS}"><span style="font-family: {SERIF}; font-size: 14px; color: {PINKDK}">{n}</span><span style="font-family: {SERIF}; font-size: 18px; letter-spacing: 0.06em; color: #FFFFFF">{t}</span></a>' for n, t, k, *_ in SVC)
    rows = ""
    for i, (n, t, k, d, uses, a, b, see) in enumerate(SVC):
        flip = i % 2 == 1
        u = "".join(f'<span style="font-family: {SANS}; font-size: 12px; letter-spacing: 0.22em; text-transform: uppercase; color: {INK}; border: 1px solid rgba(18,18,22,0.2); padding: 8px 12px">{x}</span>' for x in uses)
        seen = " · ".join(see)
        acol = "8 / span 5" if flip else "span 7"
        apad = "0 0 70px 70px" if flip else "0 70px 70px 0"
        iside = "left: 0" if flip else "right: 0"
        tcol = "1 / span 6" if flip else "9 / span 4"
        vk = SVID.get(k)
        if vk:
            media = f'<video src="{img(vk)}" poster="{img(vk + "-poster")}" autoplay muted loop playsinline preload="metadata" aria-label="{t} work in progress" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover"></video><span style="position: absolute; left: 50%; bottom: 18px; transform: translateX(-50%); display: inline-flex; align-items: center; gap: 8px; font-family: {SANS}; font-size: 10px; font-weight: 500; letter-spacing: 0.24em; text-transform: uppercase; color: #FFFFFF; background: rgba(18,18,22,0.7); padding: 7px 11px"><span style="width: 6px; height: 6px; border-radius: 50%; background: {PINK}"></span>On site</span>'
        else:
            media = f'<img src="{img(a[0])}" alt="{a[1]}" loading="lazy" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover">'
        art = f'''<div class="svc-art" style="grid-column: {acol}; grid-row: 1; position: relative; padding: {apad}">
        <div class="zoom shp-arch" style="position: relative; aspect-ratio: 5 / 4; overflow: hidden; background: {SAND}">{media}</div>
        <div class="svc-inset" style="position: absolute; {iside}; bottom: 0; width: 44%; aspect-ratio: 4 / 5; overflow: hidden; border: 8px solid #FBFAF8; box-shadow: 0 24px 50px rgba(18,18,22,0.22)"><img src="{img(b[0])}" alt="{b[1]}" loading="lazy" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover"></div>
      </div>'''
        txt = f'''<div style="grid-column: {tcol}; grid-row: 1; display: flex; flex-direction: column; gap: 22px; align-self: center">
        <span aria-hidden="true" style="font-family: {SERIF}; font-size: 92px; line-height: 0.8; color: rgba(194,28,90,0.16)">{n}</span>
        {h2(t, INK, "clamp(32px, 3.6vw, 50px)")}
        <p style="margin: 0; font-family: {SANS}; font-weight: 400; font-size: 18px; line-height: 1.75; color: #2A2A31">{d}</p>
        <div style="display: flex; flex-wrap: wrap; gap: 8px">{u}</div>
        <a href="{link("projects", sfx)}" style="font-family: {SANS}; font-size: 15px; line-height: 1.6; color: {MUTED}; text-decoration: none; border-top: 1px solid rgba(18,18,22,0.12); padding-top: 16px">See it at <span style="color: {PINKTX}">{seen}</span></a>
      </div>'''
        rows += f'''
    <div id="{k}" class="svc-row" style="display: grid; grid-template-columns: repeat(12, minmax(0, 1fr)); gap: 0 24px; scroll-margin-top: 40px">
      {art}
      {txt}
    </div>'''
    steps = "".join(f'''<div style="display: flex; flex-direction: column; gap: 18px">
        <div class="zoom" style="position: relative; aspect-ratio: 4 / 5; overflow: hidden; background: {BAS}"><img src="{img(k)}" alt="{alt}" loading="lazy" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover"><span style="position: absolute; left: 0; top: 0; font-family: {SERIF}; font-size: 15px; letter-spacing: 0.1em; color: #FFFFFF; background: {PINKTX}; padding: 10px 14px">{n}</span></div>
        <span style="font-family: {SERIF}; font-size: 22px; letter-spacing: 0.06em; color: #FFFFFF">{t}</span>
        <p style="margin: 0; font-family: {SANS}; font-weight: 300; font-size: 16px; line-height: 1.7; color: {ONDARK}">{d}</p>
      </div>''' for n, t, d, k, alt in PROC)
    wip = "".join(f'''<figure class="wip-{i}" style="margin: 0; position: relative; overflow: hidden; background: {BAS}; {'grid-row: span 2; min-height: 560px' if i == 0 else 'aspect-ratio: 4 / 3'}">
          <img src="{img(k)}" alt="{t} under construction" loading="lazy" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover">
          <div aria-hidden="true" style="position: absolute; inset: 0; background: linear-gradient(180deg, rgba(12,12,15,0) 50%, rgba(12,12,15,0.82) 100%)"></div>
          <span style="position: absolute; left: 14px; top: 14px; font-family: {SANS}; font-size: 10px; font-weight: 500; letter-spacing: 0.24em; text-transform: uppercase; color: #FFFFFF; background: {PINKTX}; padding: 7px 10px">In progress</span>
          <figcaption style="position: absolute; left: 18px; right: 18px; bottom: 16px; display: flex; flex-direction: column; gap: 2px"><span style="font-family: {SERIF}; font-size: {'24px' if i == 0 else '17px'}; color: #FFFFFF">{t}</span><span style="font-family: {SANS}; font-size: 12px; letter-spacing: 0.2em; text-transform: uppercase; color: {PINKDK}">{loc}</span></figcaption>
        </figure>''' for i, (k, t, loc) in enumerate(WIP))
    brands = "".join(f'<span style="font-family: {SERIF}; font-size: 18px; letter-spacing: 0.08em; color: {INK}; border: 1px solid rgba(194,28,90,0.4); background: #FFFFFF; padding: 12px 18px">{b}</span>' for b in ["Total Wall", "STO", "Dryvit", "Senergy", "Parex"])
    sect = [("Commercial and retail", "Hotels, shopping centers and storefronts, built on schedule around tenants and inspections.", "TRU by Hilton · Marsh Lane Plaza · Starwood Village"),
            ("Residential neighborhoods", "Model homes and whole communities for the builders who need every lot to match.", "Toll Brothers · Landon Homes · Brookfield Residential · Pegaso Group"),
            ("Custom homes", "Private residences where every arch, sill and corner is seen up close.", "Double Door Custom Homes · Travis Street · Walnut Hill")]
    simg = ["marsh-2", "townlake-2", "home-22-1"]
    sc = "".join(f'''<div class="sect-card" style="display: flex; flex-direction: column; background: {BAS}; overflow: hidden; box-shadow: 0 24px 50px rgba(18,18,22,0.16)">
        <div class="zoom" style="position: relative; aspect-ratio: 16 / 10; overflow: hidden"><img src="{img(simg[i])}" alt="{a}" loading="lazy" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover"><span style="position: absolute; left: 0; bottom: 0; font-family: {SERIF}; font-size: 15px; letter-spacing: 0.1em; color: #FFFFFF; background: {PINKTX}; padding: 10px 14px">0{i + 1}</span></div>
        <div style="display: flex; flex-direction: column; gap: 14px; padding: 30px 28px 34px; border-top: 3px solid {PINK}; flex: 1">
          <span style="font-family: {SERIF}; font-size: 22px; letter-spacing: 0.04em; color: #FFFFFF">{a}</span>
          <p style="margin: 0; font-family: {SANS}; font-weight: 300; font-size: 16px; line-height: 1.7; color: {ONDARK}">{b}</p>
          <span style="margin-top: auto; padding-top: 14px; border-top: 1px solid rgba(255,255,255,0.12); font-family: {SANS}; font-size: 13px; letter-spacing: 0.08em; color: {PINKDK}">{c}</span>
        </div>
      </div>''' for i, (a, b, c) in enumerate(sect))
    stucco = f'background: #FBFAF8 url({img("stucco-white")}) repeat; background-size: 512px 512px'
    return f'''{page_hero("Our services", "Five crafts. One standard.", "Stucco, EIFS, exterior molding, stonework and cast stone for commercial, industrial and residential projects across Dallas Fort Worth.", img("landon-3"), "Landon Homes in Vickery, aerial", sfx, "services")}

<section style="{stucco}">
  <div class="wrap" style="padding-top: 110px; padding-bottom: 140px; display: flex; flex-direction: column; gap: 120px">
    <div style="display: flex; flex-direction: column; align-items: center; text-align: center; gap: 22px">
      {eyebrow("What we install", PINKTX, True)}
      {h2("Every wall, from the lath out.", INK, "clamp(32px, 4vw, 54px)", center=True)}
      <p style="margin: 0; font-family: {SANS}; font-weight: 400; font-size: 18px; line-height: 1.7; color: #2A2A31; max-width: 620px">One crew for the whole exterior. We handle the system, the details and the finish, so builders work with one team and one standard from first coat to final walk.</p>
      <nav aria-label="Services" class="svc-idx" style="display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 2px; padding: 2px; background: {OBS}; width: 100%; margin-top: 16px; box-shadow: 0 24px 50px rgba(18,18,22,0.18)">{idx}</nav>
    </div>{rows}
  </div>
</section>

<section style="position: relative; background: {BAS}; overflow: hidden">
  <div aria-hidden="true" style="position: absolute; inset: 0; background-image: url({img("monogram")}); background-size: 240px 240px; background-position: center top; filter: brightness(1.7)"></div>
  <div aria-hidden="true" style="position: absolute; inset: 0; background: rgba(29,29,35,0.55)"></div>
  <div class="wrap" style="position: relative; padding-top: 120px; padding-bottom: 130px; display: flex; flex-direction: column; gap: 56px">
    <div class="crew grid-intro" style="display: grid; grid-template-columns: repeat(12, minmax(0, 1fr)); gap: 48px; align-items: center">
      <div style="grid-column: span 7; display: flex; flex-direction: column; gap: 22px">
        {eyebrow("How a wall comes together", PINKDK)}
        {h2("From lath to last coat.", "#FFFFFF", "clamp(32px, 4vw, 54px)")}
        <p style="margin: 0; font-family: {SANS}; font-weight: 300; font-size: 18px; line-height: 1.7; color: {ONDARK}; max-width: 560px">Every stucco wall we build goes up the same way, in four stages, with nothing skipped and nothing rushed. Our own crews do the work, on our own pink scaffolds.</p>
        <div style="display: flex; align-items: center; gap: 14px; margin-top: 8px"><span style="width: 8px; height: 8px; border-radius: 50%; background: {PINK}; box-shadow: 0 0 0 6px rgba(231,40,111,0.18)"></span><span style="font-family: {SANS}; font-size: 12px; letter-spacing: 0.28em; text-transform: uppercase; color: #FFFFFF">LVA crew on the wall, Dallas</span></div>
      </div>
      <div class="crew-v" style="grid-column: 8 / span 5; position: relative; padding: 0 0 28px 28px">
        <div aria-hidden="true" style="position: absolute; left: 0; bottom: 0; width: 70%; height: 70%; border: 1px solid {PINK}"></div>
        <div style="position: relative; aspect-ratio: 4 / 5; overflow: hidden; background: #000; box-shadow: 0 30px 60px rgba(0,0,0,0.4)"><video src="{img("svc-crew")}" poster="{img("svc-crew-poster")}" autoplay muted loop playsinline preload="metadata" aria-label="LVA crew applying stucco on pink scaffolds" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover"></video></div>
      </div>
    </div>
    <div class="grid-4 proc" style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 28px">{steps}</div>
    <div style="display: flex; flex-direction: column; gap: 26px; padding-top: 56px; border-top: 1px solid rgba(255,255,255,0.14)">
      <div class="stack-sm" style="display: flex; justify-content: space-between; align-items: flex-end; gap: 24px">
        <div style="display: flex; flex-direction: column; gap: 14px">{eyebrow("On the wall right now", PINKDK)}<span style="font-family: {SERIF}; font-size: clamp(24px, 2.6vw, 34px); color: #FFFFFF">Pink scaffolds across Dallas Fort Worth.</span></div>
        <a href="https://www.instagram.com/lvamayanstucco/" target="_blank" rel="noopener" style="display: inline-flex; align-items: center; gap: 10px; font-family: {SANS}; font-size: 13px; letter-spacing: 0.24em; text-transform: uppercase; color: {PINKDK}; text-decoration: none; white-space: nowrap">Follow along on Instagram {ic("arrow", 14)}</a>
      </div>
      <div class="wip" style="display: grid; grid-template-columns: 2fr 1fr 1fr; gap: 16px">{wip}</div>
    </div>
  </div>
</section>

<section style="{stucco}">
  <div class="wrap" style="padding-top: 120px; padding-bottom: 130px; display: flex; flex-direction: column; gap: 64px">
    <div style="display: flex; flex-direction: column; align-items: center; text-align: center; gap: 18px">
      {eyebrow("Who we build for", PINKTX, True)}
      {h2("Built for the builders.", INK, "clamp(32px, 4vw, 54px)", center=True)}
    </div>
    <div class="grid-3" style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 24px">{sc}</div>
    <div style="display: flex; flex-direction: column; align-items: center; gap: 20px; text-align: center">
      <span style="font-family: {SANS}; font-size: 12px; letter-spacing: 0.3em; text-transform: uppercase; color: {MUTED}">Certified applicator for</span>
      <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 10px">{brands}</div>
    </div>
    <div style="display: flex; flex-direction: column; align-items: center; text-align: center; gap: 26px; padding-top: 64px; border-top: 1px solid rgba(18,18,22,0.12)">
      <h2 style="margin: 0; font-family: {SERIF}; font-weight: 500; font-size: clamp(32px, 4.2vw, 58px); line-height: 1.1; letter-spacing: 0.02em; color: {INK}">Tell us what you are building.<br><span style="font-family: {ITAL}; font-style: italic; font-weight: 400; letter-spacing: 0; font-size: 1.1em; color: {PINKTX}">We will bring the crew.</span></h2>
      <div style="display: flex; gap: 16px; flex-wrap: wrap; justify-content: center">{btn("Start your project", link("contact", sfx))}<a class="btn" href="{link("projects", sfx)}" style="display: inline-flex; align-items: center; gap: 12px; min-height: 54px; padding: 0 28px; font-family: {SANS}; font-size: 13px; font-weight: 500; letter-spacing: 0.24em; text-transform: uppercase; color: {INK}; text-decoration: none; border: 1px solid {INK}">See our projects</a></div>
    </div>
  </div>
</section>'''


BODY = {"home": home, "services": services, "why": why, "projects": projects, "contact": contact, "privacy": privacy}

HELMET = f'''<helmet>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;500;600&amp;family=Cormorant+Garamond:ital,wght@1,400;1,500&amp;family=Jost:wght@300;400;500&amp;display=swap" rel="stylesheet">
<style>
@media (hover: none){{.laura-photo img{{filter:none !important}}}}

.laura-photo img{{filter:grayscale(1) contrast(1.05);transition:filter 1s ease, transform 1.4s cubic-bezier(.2,.7,.2,1)}}
.laura-art:hover .laura-photo img{{filter:none;transform:scale(1.03)}}

.at-tab:hover{{background:#2A2A33 !important;color:#FFFFFF !important}}
.at-tab[aria-selected="true"]:hover{{background:#C21C5A !important}}
.at-tab[aria-selected="true"] span:first-child{{color:#FFFFFF !important}}
.at-arrow{{transition:background-color .3s ease,border-color .3s ease}}
.at-arrow:hover{{background:#E7286F !important;border-color:#E7286F !important;color:#FFFFFF !important}}

.cred-logo{{opacity:0;transform:translateY(10px) scale(.85);transition:opacity .45s ease, transform .55s cubic-bezier(.2,.7,.2,1)}}
.cred-grid .cred-tile:hover .cred-logo{{opacity:1;transform:none}}

.acc-p:hover,.acc-p:focus,.acc:not(:hover) .acc-p:first-child{{flex-grow:3.4 !important;outline:none}}
.acc-p:hover img,.acc-p:focus img,.acc:not(:hover) .acc-p:first-child img{{filter:none;transform:scale(1.04)}}
.acc-p:hover .acc-desc,.acc-p:focus .acc-desc,.acc:not(:hover) .acc-p:first-child .acc-desc{{opacity:1;max-height:200px}}
.acc-p:hover .acc-rule,.acc-p:focus .acc-rule,.acc:not(:hover) .acc-p:first-child .acc-rule{{width:110px}}

.sw-v{{opacity:0;transition:opacity .8s ease}}
.sw-v.v1{{opacity:1}}
.sw:has(.sw-row:hover) .sw-v.v1{{opacity:0}}
.sw:has(.r1:hover) .sw-v.v1,.sw:has(.r2:hover) .sw-v.v2,.sw:has(.r3:hover) .sw-v.v3,.sw:has(.r4:hover) .sw-v.v4,.sw:has(.r5:hover) .sw-v.v5{{opacity:1 !important}}
.sw-row{{transition:background-color .4s ease}}
.sw-row > a{{transition:padding-left .5s cubic-bezier(.2,.7,.2,1)}}
.sw-row:hover{{background:rgba(255,255,255,0.04)}}
.sw-row:hover > a{{padding-left:14px !important}}
.sw-row .sw-name{{transition:color .4s ease}}
.sw-row:hover .sw-name{{color:#F4689C !important}}
.sw-row::before{{content:"";position:absolute;left:0;top:-1px;height:2px;width:0;background:#E7286F;transition:width .6s cubic-bezier(.2,.7,.2,1)}}
.sw-row:hover::before{{width:100%}}
.sw:not(:has(.sw-row:hover)) .r1::before{{width:100%}}
.sw:not(:has(.sw-row:hover)) .r1 .sw-name{{color:#F4689C !important}}


.shp-step{{clip-path:polygon(0 54px,10% 54px,10% 36px,20% 36px,20% 18px,30% 18px,30% 0,70% 0,70% 18px,80% 18px,80% 36px,90% 36px,90% 54px,100% 54px,100% 100%,0 100%)}}
.shp-arch{{border-radius:50% 50% 0 0 / 14% 14% 0 0}}
.shp-step-sm{{clip-path:polygon(0 33px,12% 33px,12% 22px,24% 22px,24% 11px,36% 11px,36% 0,64% 0,64% 11px,76% 11px,76% 22px,88% 22px,88% 33px,100% 33px,100% 100%,0 100%)}}
.shp-base{{clip-path:polygon(0 0,100% 0,100% calc(100% - 33px),88% calc(100% - 33px),88% calc(100% - 22px),76% calc(100% - 22px),76% calc(100% - 11px),64% calc(100% - 11px),64% 100%,36% 100%,36% calc(100% - 11px),24% calc(100% - 11px),24% calc(100% - 22px),12% calc(100% - 22px),12% calc(100% - 33px),0 calc(100% - 33px))}}
.shp-quoin{{clip-path:polygon(0 28px,14px 28px,14px 14px,28px 14px,28px 0,calc(100% - 28px) 0,calc(100% - 28px) 14px,calc(100% - 14px) 14px,calc(100% - 14px) 28px,100% 28px,100% calc(100% - 28px),calc(100% - 14px) calc(100% - 28px),calc(100% - 14px) calc(100% - 14px),calc(100% - 28px) calc(100% - 14px),calc(100% - 28px) 100%,28px 100%,28px calc(100% - 14px),14px calc(100% - 14px),14px calc(100% - 28px),0 calc(100% - 28px))}}


.scaf path{{stroke-dasharray:1400;stroke-dashoffset:1400;animation:scafdraw 7s ease-in-out infinite alternate}}
@keyframes scafdraw{{0%{{stroke-dashoffset:1400}}55%,100%{{stroke-dashoffset:0}}}}
.pulse{{box-shadow:0 0 0 0 rgba(231,40,111,0.7);animation:pulse 2s ease-out infinite}}
@keyframes pulse{{to{{box-shadow:0 0 0 14px rgba(231,40,111,0)}}}}
.film{{animation-duration:70s}}
.film:hover{{animation-play-state:paused}}
.film-card img{{filter:grayscale(0.6) brightness(0.8);transition:filter .6s ease,transform 1s ease}}
.film-card:hover img{{filter:none;transform:scale(1.05)}}

.seal{{animation:sealspin 40s linear infinite}}
@keyframes sealspin{{to{{transform:rotate(360deg)}}}}

.corner .corner-img{{transform:scale(1.02);filter:grayscale(0.35) brightness(0.9);transition:transform 1.4s cubic-bezier(.2,.7,.2,1),filter .8s ease}}
.corner:hover .corner-img{{transform:scale(1.09);filter:grayscale(0) brightness(1)}}
.corner .corner-rule{{transition:width .7s cubic-bezier(.2,.7,.2,1)}}
.corner:hover .corner-rule{{width:120px !important}}
.corner .corner-num{{transition:color .6s ease,-webkit-text-stroke-color .6s ease}}
.corner:hover .corner-num{{color:rgba(231,40,111,0.9) !important;-webkit-text-stroke-color:rgba(231,40,111,0.9) !important}}

body{{margin:0;background:{STUC}}}
a{{color:{PINKTX}}}a:hover{{color:{INK}}}
.wrap{{max-width:1320px;margin:0 auto;padding-left:clamp(20px,4.5vw,64px);padding-right:clamp(20px,4.5vw,64px);box-sizing:border-box;width:100%}}
.show-sm{{display:none !important}}
.hero{{height:auto}}
.hero-sub{{height:720px;min-height:720px}}
.hero-sub > .wrap{{padding-top:150px;box-sizing:border-box}}
.btn{{transition:filter .2s ease, background-color .2s ease}}
.cred .dia{{transition:background-color .35s ease, box-shadow .35s ease, border-color .35s ease}}
.cred-tile{{transition:background-color .35s ease, box-shadow .35s ease;cursor:default}}
.cred-tile span{{transition:color .35s ease, border-color .35s ease}}
.cred-grid .cred-tile:not(:last-child):hover{{background:#E7286F !important;box-shadow:0 0 34px rgba(231,40,111,0.35);z-index:1}}
.cred-grid .cred-tile:not(:last-child):hover span{{color:#FFFFFF !important;border-bottom-color:#FFFFFF !important}}
.cred-grid .cred-tile:last-child{{transition:background-color .35s ease}}
.cred-grid .cred-tile:last-child:hover{{background:#C21C5A !important}}
.cred:hover .dia{{background:rgba(231,40,111,0.16) !important;border-color:#E7286F !important;box-shadow:0 0 22px rgba(231,40,111,0.35)}}
.btn:hover{{filter:brightness(1.12)}}
.pgrid article[style*='span 2'] .zoom{{aspect-ratio:auto !important;height:100%;min-height:260px}}
.pgrid article[style*='span 2'] > div{{flex:1}}
.pgrid article[style*='span 2'] .zoom img{{object-position:center 22%}}
.pgrid article:has(img[alt='Marsh Lane Plaza']) .zoom img{{object-position:center 78%}}
.svc-tab{{transition:background .3s ease}}.svc-tab:hover{{background:{PINKTX} !important}}
.stick{{animation:stickIn .45s cubic-bezier(.2,.7,.2,1)}}
@keyframes stickIn{{from{{transform:translateY(-100%);opacity:0}}to{{transform:none;opacity:1}}}}
.mbar{{animation:mbarIn .45s cubic-bezier(.2,.7,.2,1)}}
@keyframes mbarIn{{from{{transform:translateY(120%)}}to{{transform:none}}}}
a,button{{-webkit-tap-highlight-color:transparent}}
html{{scroll-behavior:smooth}}
@media (prefers-reduced-motion: reduce){{html{{scroll-behavior:auto}}.stick,.mbar{{animation:none}}}}
.zoom img{{transition:transform 1.2s cubic-bezier(.2,.7,.2,1)}}
.zoom:hover img,a:hover .zoom img{{transform:scale(1.045)}}
.m-a{{grid-column:span 7}}.m-b{{grid-column:span 5;grid-row:span 2}}.m-c{{grid-column:span 7}}.m-d{{grid-column:span 6}}.m-e{{grid-column:span 6}}
.m-b .zoom{{aspect-ratio:auto !important;height:100%}}
.marquee{{animation:mq 48s linear infinite}}
@keyframes mq{{from{{transform:translateX(0)}}to{{transform:translateX(-50%)}}}}
@media (prefers-reduced-motion: reduce){{.marquee{{animation:none}}.zoom img{{transition:none}}}}
@media (max-height: 800px) and (min-width: 761px){{
 .hero h1{{font-size:clamp(40px,5.4vw,74px) !important}}
 .hero > .wrap{{padding-top:118px !important;padding-bottom:52px !important;gap:20px !important}}
}}
@media (max-width: 1100px){{
 .grid-5{{grid-template-columns:repeat(3,minmax(0,1fr)) !important}}
 .grid-foot{{grid-template-columns:repeat(2,minmax(0,1fr)) !important}}
 .grid-4{{grid-template-columns:repeat(2,minmax(0,1fr)) !important;row-gap:24px}}
 .hide-sm{{display:none !important}}
 .show-sm{{display:inline-flex !important}}
 .pgrid{{grid-template-columns:repeat(2,minmax(0,1fr)) !important}}
 .rail{{display:flex !important;overflow-x:auto;scroll-snap-type:x mandatory;gap:20px !important;margin-right:calc(-1 * clamp(20px,4.5vw,64px));padding-right:clamp(20px,4.5vw,64px);padding-bottom:6px;scrollbar-width:none;-webkit-overflow-scrolling:touch}}
 .rail::-webkit-scrollbar{{display:none}}
 .rail > *{{flex:0 0 46%;min-width:0;scroll-snap-align:start}}
 .corners{{grid-template-columns:minmax(0,1fr) !important;gap:24px !important}}
 .corners .corner{{min-height:440px !important;margin-top:0 !important}}
 .sw{{grid-template-columns:minmax(0,1fr) !important}}
 .sw > *{{grid-column:auto !important}}
 .sw-stage{{display:none !important}}
 .sw-thumb{{display:block !important}}
 .sw-list{{display:grid !important;grid-template-columns:repeat(2,minmax(0,1fr));column-gap:28px;padding:0 24px 12px !important}}
 .sw-row > a{{align-items:start !important}}
 .svc-row > div{{grid-column:1 / -1 !important;grid-row:auto !important}}
 .svc-row{{row-gap:28px !important}}
 .svc-art{{padding:0 120px 60px 0 !important}}
 .svc-inset{{width:38% !important;right:0 !important;left:auto !important;bottom:0 !important}}
 .wip{{grid-template-columns:1fr 1fr !important}}
 .wip .wip-0{{grid-column:1 / -1;grid-row:auto !important;min-height:0 !important;aspect-ratio:16 / 9}}
 .wip figure:not(.wip-0){{aspect-ratio:4 / 3 !important}}
 .grid-intro{{gap:40px !important}}
 .crew{{grid-template-columns:minmax(0,1fr) !important}}
 .crew > div{{grid-column:auto !important}}
 .crew-v{{max-width:520px}}
}}
@media (max-width: 760px){{
 .laura-art{{padding:0 20px 20px 0 !important}}
 .laura-photo img{{filter:none !important}}
 .caststone svg{{display:none}}
 .sw-stage{{display:none !important}}
 .sw-thumb{{display:block !important}}
 .sw-row > a{{align-items:start !important}}
 .at-tabs{{grid-template-columns:repeat(5,minmax(132px,1fr)) !important;overflow-x:auto;margin:0 -20px;padding:0 20px}}
 .at-body > div{{grid-column:1 / -1 !important}}
 .hero-sub h1{{font-size:clamp(30px,9vw,38px) !important;line-height:1.08 !important}}
 .hero-sub > .wrap{{gap:16px !important}}
 .hero-sub > .wrap > div:first-child{{font-size:11px !important;letter-spacing:0.2em !important}}
 .tm-ov{{background:rgba(12,12,15,0.8) !important}}
 .grid-foot{{grid-template-columns:repeat(2,minmax(0,1fr)) !important;gap:36px 24px !important}}
 .grid-foot > div:first-child,.grid-foot > div:nth-child(3){{grid-column:1 / -1 !important}}
 .grid-foot > div:nth-child(4){{grid-row:2;grid-column:2}}
 .wrap[style*="padding-top: 1"],.wrap[style*="padding-top: 8"],.wrap[style*="padding-top: 9"]{{padding-top:60px !important;padding-bottom:60px !important}}
 [style*="gap: 64px"],[style*="gap: 56px"]{{gap:32px !important}}
 [style*="gap: 48px"]{{gap:28px !important}}
 .grid-intro,.grid-contact{{row-gap:32px !important}}
 .tm-home{{min-height:0 !important}}
 .corner{{min-height:420px !important}}
 .film-wrap,[style*="padding-bottom: 150px"]{{padding-bottom:60px !important}}
 .cta-art{{padding:0 0 24px 0 !important}}
 h2{{font-size:clamp(30px,8.4vw,40px) !important}}
 .btn{{min-height:48px !important;padding:0 18px !important;font-size:11.5px !important;letter-spacing:0.16em !important;gap:10px !important}}
 .hero > .wrap{{padding-top:112px !important;padding-bottom:32px !important;gap:16px !important}}
 .hero h1{{font-size:clamp(30px,9vw,38px) !important;line-height:1.08 !important}}
 .hero > .wrap > div:first-child{{font-size:10px !important;letter-spacing:0.12em !important;gap:8px !important;white-space:nowrap}}
 .hero > .wrap > div:first-child > span{{width:20px !important}}
 .hero p{{font-size:16px !important;line-height:1.6 !important}}
 .hero > .wrap > div:last-child{{flex-wrap:nowrap !important;gap:10px !important}}
 .hero > .wrap > div:last-child .btn{{padding:0 12px !important;font-size:11px !important;letter-spacing:0.12em !important;flex:1 1 0;justify-content:center;white-space:nowrap}}
 .hero > .wrap > div:last-child .btn svg{{display:none}}
 .hero-sub > .wrap{{padding-top:150px !important;padding-bottom:40px !important}}
 .tm-img{{left:0 !important;object-position:60% center !important;-webkit-mask-image:none !important;mask-image:none !important}}
 article[style*='span 2']{{grid-column:auto !important;grid-row:auto !important}}
 .foot-mid,.foot-end{{align-items:flex-start !important;text-align:left !important;justify-content:flex-start !important}}
 .corners .corner{{margin-top:0 !important}}
 .film-card{{width:220px !important}}
 .corner .corner-num{{font-size:84px !important}}
 .hero-sub{{height:auto !important}}
 .hero-sub p{{font-size:17px !important}}
 .hdr-logo{{width:168px !important}}
 .svc-row > div{{grid-column:1 / -1 !important;grid-row:auto !important}}
 .svc-row{{row-gap:28px !important}}
 .svc-inset{{width:42% !important;right:0 !important;left:auto !important;bottom:0 !important}}
 .svc-art{{padding:0 0 56px 0 !important}}
 .rail > *{{flex:0 0 82% !important}}
 .sw-list{{grid-template-columns:minmax(0,1fr) !important}}
 .mbar{{display:flex !important}}
 footer{{padding-bottom:84px}}
 .stick .wrap{{padding-top:10px !important;padding-bottom:10px !important}}
 .svc-idx{{grid-template-columns:repeat(2,minmax(0,1fr)) !important}}
 .svc-idx a:last-child{{grid-column:1 / -1}}
 .wip{{grid-template-columns:1fr 1fr !important;gap:10px !important}}
 .wip .wip-0{{grid-column:1 / -1;grid-row:auto !important;min-height:0 !important;aspect-ratio:4 / 3}}
 .wip figcaption span:first-child{{font-size:15px !important}}
 .wip figure:not(.wip-0){{aspect-ratio:4 / 5 !important}}
 .wip figure:not(.wip-0) > span{{display:none}}
 .deco{{display:none !important}}
 .lift{{margin-top:0 !important}}
 .cred-grid{{grid-template-columns:repeat(2,minmax(0,1fr)) !important}}
 .cred-tile{{min-height:150px !important;padding:22px 18px !important;gap:24px !important}}
 .grid-contact{{padding-top:0 !important}}
 .intro-art{{padding-bottom:0 !important}}
 .grid-split > div:first-child,.grid-split .zoom{{min-height:420px !important}}
 .rail{{display:flex !important;overflow-x:auto;scroll-snap-type:x mandatory;gap:16px !important;margin-right:calc(-1 * clamp(20px,4.5vw,64px));padding-right:20px;padding-bottom:6px;scrollbar-width:none;-webkit-overflow-scrolling:touch}}
 .rail::-webkit-scrollbar{{display:none}}
 .rail > *{{flex:0 0 82%;min-width:0;scroll-snap-align:start}}
 .mosaic.rail .zoom{{aspect-ratio:4 / 5 !important;height:auto !important}}
 .hide-sm{{display:none !important}}
 .show-sm{{display:inline-flex !important}}
 .hero-sub{{height:560px}}
 .grid-2,.grid-3,.grid-5,.grid-split{{grid-template-columns:minmax(0,1fr) !important}}
 .grid-4{{grid-template-columns:repeat(2,minmax(0,1fr)) !important}}
 .creds{{row-gap:22px !important;padding-top:32px !important;padding-bottom:32px !important}}
 .creds{{grid-template-columns:minmax(0,1fr) !important;row-gap:26px !important}}
 .cred{{padding:0 0 0 6px !important;border-left:none !important;gap:20px !important}}
 .cred .dia{{width:44px !important;height:44px !important;margin-left:6px}}
 .grid-intro,.grid-contact{{grid-template-columns:minmax(0,1fr) !important;row-gap:48px !important}}
 .grid-intro > div,.grid-contact > div,.grid-contact > form{{grid-column:auto !important}}
 .grid-contact > form{{padding-top:24px !important}}
 .float-img{{left:-8px !important;width:48% !important}}
 .mosaic{{grid-template-columns:minmax(0,1fr) !important}}
 .m-a,.m-b,.m-c,.m-d,.m-e{{grid-column:auto !important;grid-row:auto !important}}
 .m-b .zoom{{aspect-ratio:4 / 5 !important;height:auto}}
 .stack-sm{{flex-direction:column !important;align-items:flex-start !important}}
}}
</style>
</helmet>'''


AT = [('Stucco', 'Walls built coat by coat, from lath to finish, for the homes families come back to every night.', ['home-21-4', 'vickery-2', 'townlake-2'], ['Custom homes', 'Tract neighborhoods', 'Commercial']), ('EIFS', 'Insulated exterior finish systems for the hotels, clinics and storefronts people step into every day. Fully insured for EIFS.', ['tru-1', 'tru-3', 'tru-5'], ['Hotels', 'Clinics', 'Storefronts']), ('Exterior Molding', 'Trim, bands and surrounds that give a facade its character from the street.', ['oakbridge-2', 'oakbridge-3', 'verandah-4'], ['Window surrounds', 'Bands', 'Trim']), ('Stonework', 'Stone and brick veneers that make an entry feel like home the moment you pull in.', ['home-22-1', 'landon-2', 'home-36-1'], ['Entries', 'Facades', 'Custom homes']), ('Cast Stone', 'Cast stone accents finished to the line the designer drew.', ['starwood-1', 'starwood-2', 'starwood-3'], ['Accents', 'Columns', 'Retail centers'])]

def logic(key):
    base = "stuck: !!this.state.stuck, menuOpen: !!this.state.menuOpen, toggleMenu: () => this.setState({ menuOpen: !this.state.menuOpen }), heroH: this.heroH(), progress: (this.state.progress || 0).toFixed(2) + '%'"
    atdata = json.dumps([{"name": n, "desc": d, "imgs": [img(k) for k in ks], "uses": u} for n, d, ks, u in AT])
    if key != "projects":
        return f'''class Component extends DCLogic {{
  constructor(p) {{ super(p); this.state = {{ menuOpen: false }}; }}
  heroH() {{
    const ih = (typeof window !== 'undefined' && window.innerHeight) || 0;
    const sh = (typeof screen !== 'undefined' && screen.availHeight) || 900;
    const h = ih > 300 && ih < 1300 ? ih : Math.round(sh * 0.88);
    return Math.max(620, Math.min(h, 1200)) + 'px';
  }}
  componentDidMount() {{
    this._r = () => this.forceUpdate();
    window.addEventListener('resize', this._r);
    this._s = () => {{
      if (this._raf) return;
      this._raf = requestAnimationFrame(() => {{
        this._raf = 0;
        const d = document.documentElement;
        const max = Math.max(1, d.scrollHeight - window.innerHeight);
        const pct = Math.min(100, Math.max(0, (window.scrollY / max) * 100));
        const st = window.scrollY > 560;
        if (Math.abs(pct - (this.state.progress || 0)) >= 0.4 || st !== !!this.state.stuck) this.setState({{ progress: pct, stuck: st }});
      }});
    }};
    window.addEventListener('scroll', this._s, {{ passive: true }});
    this._s();
    this._rv();
  }}
  _rv() {{
    if (typeof IntersectionObserver === 'undefined') return;
    if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    const sel = 'main section h2, main section .eyebrow-rv, main .zoom, main .svc-row, main .corner, main .sect-card, main .proc > div, main .wip figure, main article, main .cred, main .cred-tile, main .film-card, main .rv';
    const vh = window.innerHeight || 800;
    const els = Array.from(document.querySelectorAll(sel)).filter((el) => {{
      if (el.closest('.hero') || el.closest('.hero-sub') || el.closest('header')) return false;
      const r = el.getBoundingClientRect();
      return r.top > vh * 0.92;
    }});
    if (!els.length) return;
    const io = new IntersectionObserver((entries) => {{
      entries.forEach((e) => {{
        if (!e.isIntersecting) return;
        io.unobserve(e.target);
        const el = e.target;
        const sib = el.parentElement ? Array.prototype.indexOf.call(el.parentElement.children, el) : 0;
        const delay = Math.min(sib, 4) * 80;
        if (el.animate) el.animate([{{ opacity: 0, transform: 'translateY(26px)' }}, {{ opacity: 1, transform: 'translateY(0)' }}], {{ duration: 900, delay: delay, easing: 'cubic-bezier(.2,.7,.2,1)', fill: 'backwards' }});
      }});
    }}, {{ rootMargin: '0px 0px -8% 0px', threshold: 0.12 }});
    els.forEach((el) => io.observe(el));
    this._io = io;
  }}
  componentWillUnmount() {{ window.removeEventListener('resize', this._r); window.removeEventListener('scroll', this._s); if (this._io) this._io.disconnect(); }}
  renderVals() {{
    const D = {atdata};
    const n = D.length;
    const cur = ((this.state.at || 0) % n + n) % n;
    const ph = this.state.ph || 0;
    const d = D[cur];
    const at = {{
      num: '0' + (cur + 1), name: d.name, desc: d.desc,
      uses: d.uses.map((t) => ({{ t }})),
      prev: () => this.setState({{ at: cur - 1, ph: 0 }}),
      next: () => this.setState({{ at: cur + 1, ph: 0 }}),
      tabs: D.map((x, i) => ({{
        num: '0' + (i + 1), name: x.name, sel: i === cur ? 'true' : 'false',
        style: 'position: relative; display: flex; flex-direction: column; align-items: center; gap: 8px; padding: 24px 8px; background: ' + (i === cur ? '#C21C5A' : '#1D1D23') + '; color: ' + (i === cur ? '#FFFFFF' : 'rgba(255,255,255,0.72)') + '; border: none; cursor: pointer; transition: background-color .4s ease, color .4s ease; box-shadow: ' + (i === cur ? 'inset 0 -3px 0 #F4689C' : 'none'),
        pick: () => this.setState({{ at: i, ph: 0 }})
      }})),
      imgs: D.flatMap((x, i) => x.imgs.map((src, j) => ({{
        src, alt: x.name + ' by LVA Mayan Stucco',
        style: 'position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; display: block; transition: opacity .8s ease, transform 1.6s cubic-bezier(.2,.7,.2,1); opacity: ' + (i === cur && j === ph ? '1' : '0') + '; transform: scale(' + (i === cur && j === ph ? '1' : '1.05') + ')'
      }}))),
      thumbs: d.imgs.map((src, j) => ({{
        src, label: 'Show ' + d.name + ' photo ' + (j + 1),
        style: 'flex: 1; aspect-ratio: 16 / 10; padding: 0; overflow: hidden; cursor: pointer; background: #000; border: 2px solid ' + (j === ph ? '#E7286F' : 'transparent') + '; opacity: ' + (j === ph ? '1' : '0.55') + '; transition: opacity .4s ease, border-color .4s ease',
        pick: () => this.setState({{ ph: j }})
      }}))
    }};
    return {{ {base}, at }};
  }}
}}'''
    VID = {"Vickery by Toll Brothers": "vickery", "TRU by Hilton": "tru", "Town Lake Subdivision by Toll Brothers": "townlake", "Starwood Village": "starwood", "Landon Homes in Vickery Subdivision": "landon", "Oakbridge Subdivision by Toll Brothers": "oakbridge"}
    data = json.dumps([{"name": n, "cat": c, "loc": l, "photos": ims, "credit": CREDIT.get(n, ""), "loop": img("v-" + VID[n] + "-loop") if n in VID else "", "film": img("v-" + VID[n] + "-full") if n in VID else ""} for n, c, l, ims in PROJECTS])
    return f'''class Component extends DCLogic {{
  constructor(p) {{ super(p); this.state = {{ menuOpen: false, filter: 'All', open: -1, idx: 0 }}; }}
  heroH() {{
    const ih = (typeof window !== 'undefined' && window.innerHeight) || 0;
    const sh = (typeof screen !== 'undefined' && screen.availHeight) || 900;
    const h = ih > 300 && ih < 1300 ? ih : Math.round(sh * 0.88);
    return Math.max(620, Math.min(h, 1200)) + 'px';
  }}
  componentDidMount() {{
    this._r = () => this.forceUpdate();
    window.addEventListener('resize', this._r);
    this._s = () => {{
      if (this._raf) return;
      this._raf = requestAnimationFrame(() => {{
        this._raf = 0;
        const d = document.documentElement;
        const max = Math.max(1, d.scrollHeight - window.innerHeight);
        const pct = Math.min(100, Math.max(0, (window.scrollY / max) * 100));
        const st = window.scrollY > 560;
        if (Math.abs(pct - (this.state.progress || 0)) >= 0.4 || st !== !!this.state.stuck) this.setState({{ progress: pct, stuck: st }});
      }});
    }};
    window.addEventListener('scroll', this._s, {{ passive: true }});
    this._s();
    this._rv();
  }}
  _rv() {{
    if (typeof IntersectionObserver === 'undefined') return;
    if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    const sel = 'main section h2, main section .eyebrow-rv, main .zoom, main .svc-row, main .corner, main .sect-card, main .proc > div, main .wip figure, main article, main .cred, main .cred-tile, main .film-card, main .rv';
    const vh = window.innerHeight || 800;
    const els = Array.from(document.querySelectorAll(sel)).filter((el) => {{
      if (el.closest('.hero') || el.closest('.hero-sub') || el.closest('header')) return false;
      const r = el.getBoundingClientRect();
      return r.top > vh * 0.92;
    }});
    if (!els.length) return;
    const io = new IntersectionObserver((entries) => {{
      entries.forEach((e) => {{
        if (!e.isIntersecting) return;
        io.unobserve(e.target);
        const el = e.target;
        const sib = el.parentElement ? Array.prototype.indexOf.call(el.parentElement.children, el) : 0;
        const delay = Math.min(sib, 4) * 80;
        if (el.animate) el.animate([{{ opacity: 0, transform: 'translateY(26px)' }}, {{ opacity: 1, transform: 'translateY(0)' }}], {{ duration: 900, delay: delay, easing: 'cubic-bezier(.2,.7,.2,1)', fill: 'backwards' }});
      }});
    }}, {{ rootMargin: '0px 0px -8% 0px', threshold: 0.12 }});
    els.forEach((el) => io.observe(el));
    this._io = io;
  }}
  componentWillUnmount() {{ window.removeEventListener('resize', this._r); window.removeEventListener('scroll', this._s); if (this._io) this._io.disconnect(); }}
  renderVals() {{
    const all = {data};
    const cur = this.state.filter;
    const cats = ['All', 'Commercial', 'Residential Tract', 'Residential Custom'];
    const base = 'min-height: 46px; padding: 0 22px; font-family: Jost, system-ui, sans-serif; font-size: 12px; font-weight: 500; letter-spacing: 0.22em; text-transform: uppercase; cursor: pointer; border-radius: 0; ';
    const on = base + 'background: {OBS}; color: #FFFFFF; border: 1px solid {OBS}';
    const off = base + 'background: transparent; color: {INK}; border: 1px solid #A9A1A8';
    const filters = cats.map((c) => ({{
      label: c === 'All' ? 'All' : c,
      pressed: cur === c ? 'true' : 'false',
      style: cur === c ? on : off,
      pick: () => this.setState({{ filter: c }})
    }}));
    const inCat = all.map((x, i) => ({{ ...x, i }})).filter((x) => cur === 'All' || x.cat === cur);
    const more = [];
    const ordered = inCat.filter((x) => x.photos.length > 0).concat(inCat.filter((x) => x.photos.length === 0));
    const plaqueCount = inCat.filter((x) => x.photos.length === 0).length;
    const tall = plaqueCount % 3 === 0;
    const shown = ordered.map((x) => ({{
      ...x,
      artStyle: 'display: flex; flex-direction: column; gap: 18px' + ((x.name === 'Gucci' || x.name === 'Marsh Lane Plaza') && x.photos.length > 0 && cur === 'All' ? '; grid-column: span 2' : '') + (x.name === 'Gucci' && x.photos.length === 0 ? (tall ? '; grid-column: span 2; grid-row: span 2' : '; grid-column: span 2') : ''),
      plaqueStyle: 'position: relative; overflow: hidden; display: flex; align-items: center; justify-content: center; background: {LIME}; ' + (x.name === 'Gucci' ? (tall ? 'flex: 1; min-height: 0' : 'aspect-ratio: 8 / 3') : 'aspect-ratio: 4 / 3'),
      plaqueSize: x.name === 'Gucci' ? 'clamp(40px, 5vw, 72px)' : 'clamp(22px, 2vw, 28px)',
      plaqueNote: x.name === 'Gucci' ? 'NorthPark Center · Dallas' : (x.cat === 'Residential Custom' ? 'Private residence' : 'Commercial project'),
      hasPhotos: x.photos.length > 0,
      noPhotos: x.photos.length === 0,
      hasFilm: !!x.loop,
      cover: x.photos[0] || '',
      hasCredit: !!x.credit,
      creditOpen: this.state.credit === x.i,
      creditLabel: 'Photos courtesy of ' + x.credit,
      toggleCredit: () => this.setState({{ credit: this.state.credit === x.i ? -1 : x.i }}),
      countText: (x.film ? 'Film + ' : '') + x.photos.length + (x.photos.length === 1 ? ' photo' : ' photos'),
      openLabel: 'Open ' + x.name + ' gallery',
      open: () => this.setState({{ open: x.i, idx: 0 }})
    }}));
    const withPhotos = shown.filter((x) => x.hasPhotos);
    const noPhotos = shown.filter((x) => !x.hasPhotos).sort((a, b) => (b.name === 'Gucci') - (a.name === 'Gucci'));
    const hasPlaques = noPhotos.length > 0;
    const hasWithPhotos = withPhotos.length > 0;
    const gridPadB = hasWithPhotos ? '110px' : '64px';
    const countLabel = inCat.length + (inCat.length === 1 ? ' project' : ' projects');
    let lb = {{ on: false }};
    if (this.state.open >= 0) {{
      const pr = all[this.state.open];
      const media = (pr.film ? [{{ vid: true, src: pr.film, thumb: pr.photos[0] }}] : []).concat(pr.photos.map((p) => ({{ vid: false, src: p, thumb: p }})));
      const n = media.length;
      const idx = ((this.state.idx % n) + n) % n;
      const m = media[idx];
      lb = {{
        on: true, name: pr.name, cat: pr.cat, loc: pr.loc, hasCredit: !!pr.credit && !m.vid, creditText: 'Photo courtesy of ' + pr.credit,
        isVid: m.vid, isImg: !m.vid, poster: pr.photos[0],
        src: m.src, alt: m.vid ? pr.name + ' project film' : pr.name + ', photo ' + (idx + 1) + ' of ' + n,
        close: () => this.setState({{ open: -1 }}),
        prev: () => this.setState({{ idx: idx - 1 }}),
        next: () => this.setState({{ idx: idx + 1 }}),
        thumbs: media.map((mm, j) => ({{
          src: mm.thumb, vid: mm.vid, label: mm.vid ? 'Play project film' : 'Show photo ' + (j + 1),
          style: 'position: relative; flex: none; width: 76px; height: 54px; padding: 0; cursor: pointer; background: none; overflow: hidden; border: 2px solid ' + (j === idx ? '{PINK}' : 'transparent') + '; opacity: ' + (j === idx ? '1' : '0.55'),
          pick: () => this.setState({{ idx: j }})
        }}))
      }};
    }}
    return {{ {base}, filters, shown, withPhotos, noPhotos, hasPlaques, hasWithPhotos, gridPadB, more, countLabel, lb }};
  }}
}}'''


def sticky(page, sfx):
    links = "".join(f'<a href="{link(k, sfx)}" style="font-family: {SANS}; font-size: 12px; font-weight: 500; letter-spacing: 0.24em; text-transform: uppercase; text-decoration: none; color: {PINKDK if k == page else "#FFFFFF"}; padding: 8px 2px">{LABEL[k]}</a>' for k in NAV)
    return f'''<sc-if value="{{{{stuck}}}}" hint-placeholder-val="{{{{false}}}}">
<div class="stick" role="navigation" aria-label="Quick navigation" style="position: fixed; top: 0; left: 0; right: 0; z-index: 50; background: rgba(18,18,22,0.86); backdrop-filter: blur(14px) saturate(140%); -webkit-backdrop-filter: blur(14px) saturate(140%); border-bottom: 1px solid rgba(255,255,255,0.08); box-shadow: 0 10px 30px rgba(0,0,0,0.25)">
  <div class="wrap" style="display: flex; align-items: center; justify-content: space-between; gap: 20px; padding-top: 12px; padding-bottom: 12px">
    <a href="{link("home", sfx)}" aria-label="LVA Mayan Stucco home" style="line-height: 0"><img src="{img("logo-white")}" alt="Mayan Stucco" style="width: 150px; height: auto; display: block"></a>
    <nav class="hide-sm" style="display: flex; align-items: center; gap: 32px">{links}<a href="{link("contact", sfx)}" class="btn" style="font-family: {SANS}; font-size: 12px; font-weight: 500; letter-spacing: 0.22em; text-transform: uppercase; text-decoration: none; color: #FFFFFF; background: {PINKTX}; padding: 12px 20px">Start a Project</a></nav>
    <button class="show-sm" type="button" aria-label="Open menu" onClick="{{{{toggleMenu}}}}" style="width: 44px; height: 44px; border: 1px solid rgba(255,255,255,0.25); background: transparent; color: #FFFFFF; cursor: pointer; align-items: center; justify-content: center">{ic("menu", 20)}</button>
  </div>
</div>
<div class="mbar" style="display: none; position: fixed; left: 12px; right: 12px; bottom: 12px; z-index: 50; gap: 8px; padding: 8px; background: rgba(18,18,22,0.9); backdrop-filter: blur(14px); -webkit-backdrop-filter: blur(14px); box-shadow: 0 16px 40px rgba(0,0,0,0.35)">
  <a href="{TEL}" style="flex: 1; display: inline-flex; align-items: center; justify-content: center; gap: 10px; min-height: 48px; font-family: {SANS}; font-size: 12px; font-weight: 500; letter-spacing: 0.2em; text-transform: uppercase; color: #FFFFFF; text-decoration: none; border: 1px solid rgba(255,255,255,0.25)">{ic("phone", 16)} Call</a>
  <a href="{link("contact", sfx)}" style="flex: 1.4; display: inline-flex; align-items: center; justify-content: center; gap: 10px; min-height: 48px; font-family: {SANS}; font-size: 12px; font-weight: 500; letter-spacing: 0.2em; text-transform: uppercase; color: #FFFFFF; text-decoration: none; background: {PINKTX}">Start a project {ic("arrow", 14)}</a>
</div>
</sc-if>'''


def build(key, sfx, title, h):
    w = 390 if sfx else 1440
    props = json.dumps({"$preview": {"width": w, "height": h}})
    no_hdr = key in ("home", "why", "projects", "contact", "privacy")
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title}</title>
<meta name="description" content="LVA Mayan Stucco LLC, a certified woman-owned stucco, EIFS and stone contractor serving Dallas Fort Worth.">
<script src="./support.js"></script>
</head>
<body>
<x-dc>
{HELMET}
<div style="font-family: {SANS}; color: {INK}; background: {STUC}; width: 100%; overflow-x: hidden">
<div aria-hidden="true" style="position: fixed; top: 0; left: 0; right: 0; height: 3px; z-index: 100; background: rgba(255,255,255,0.08); pointer-events: none"><div style="height: 100%; width: {{{{progress}}}}; background: linear-gradient(90deg, #C21C5A, #E7286F); box-shadow: 0 0 10px rgba(231,40,111,0.55)"></div></div>
{sticky(key, sfx)}
<main>
{BODY[key](sfx)}
</main>
{footer(sfx)}
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{props}'>
{logic(key)}
</script>
</body>
</html>
'''


HEIGHTS = {"home": (7600, 8800), "services": (6200, 9800), "why": (4900, 6800), "projects": (4400, 9800), "contact": (2300, 3400), "privacy": (3100, 5300)}
boards, order = {}, []
x = 0
for key, stem, label, title in PAGES:
    for sfx in ["", "-Phone"]:
        h = HEIGHTS[key][1 if sfx else 0]
        open(os.path.join(OUT, f"{stem}{sfx}.dc.html"), "w").write(build(key, sfx, title, h))
    boards[f"{stem}.dc.html"] = {"x": x, "y": 0, "w": 1440, "h": HEIGHTS[key][0], "title": f"{label} · Desktop", "expand": "fill", "is_interactive": True}
    boards[f"{stem}-Phone.dc.html"] = {"x": x, "y": HEIGHTS["home"][0] + 420, "w": 390, "h": HEIGHTS[key][1], "title": f"{label} · Phone", "expand": "fill", "is_interactive": True}
    order += [f"{stem}.dc.html", f"{stem}-Phone.dc.html"]
    x += 1440 + 160

canvas = {"v": 3, "createdOnFiles": {"v": 1, "at": NOW}, "title": "LVA Mayan Stucco Website, Modernized",
          "launch": {"view": "focused", "file": "Main.dc.html"}, "pages": [], "boards": boards, "order": order,
          "notes": {"t1": {"x": 0, "y": -300, "text": "LVA Mayan Stucco · Desktop", "kind": "title1", "maxW": 8000},
                    "t2": {"x": 0, "y": HEIGHTS["home"][0] + 120, "text": "Phone", "kind": "title1", "maxW": 8000}},
          "designSystems": []}
print("ok")
json.dump(canvas, open(os.path.join(OUT, "canvas.json"), "w"), indent=1)
