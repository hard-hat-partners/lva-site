"""Contact form as a raised light cast-stone card with boxed fields.
Usage: python3 -I tools/form_card.py site/contact.html"""
import sys
CSS = (
 ".grid-contact > form{background:#FFFFFF;padding:clamp(28px,3.6vw,52px) !important;margin-top:56px;align-self:start;gap:24px !important;"
 "box-shadow:0 0 0 1px rgba(80,66,46,0.18),0 0 0 7px #F4F0E9,0 0 0 8px rgba(80,66,46,0.16),0 2px 3px rgba(30,24,16,0.12),0 24px 40px rgba(30,24,16,0.16),0 50px 90px rgba(30,24,16,0.14)}"
 ".grid-contact > form::before{content:'';position:absolute;left:0;right:0;top:0;height:4px;background:linear-gradient(90deg,#C21C5A,#E7286F)}"
 ".grid-contact > form label:not([aria-hidden]){color:#3A3A42 !important;letter-spacing:0.22em !important}"
 ".grid-contact > form input:not([type=hidden]):not([name=company-website]),.grid-contact > form select,.grid-contact > form textarea{"
 "background:#FFFFFF !important;border:1px solid #CFCCD3 !important;border-radius:2px !important;padding:14px 16px !important;margin-top:4px;"
 "box-shadow:inset 0 1px 2px rgba(18,18,22,0.06);transition:border-color .2s ease,box-shadow .2s ease,background .2s ease}"
 ".grid-contact > form select{padding-right:40px !important}"
 ".grid-contact > form input:focus,.grid-contact > form select:focus,.grid-contact > form textarea:focus{outline:none;background:#FFFFFF !important;border-color:#E7286F !important;box-shadow:0 0 0 3px rgba(231,40,111,0.15) !important}"
 ".grid-contact > form textarea{min-height:140px}"
 "@media (max-width:760px){.grid-contact > form{margin-top:36px;padding:26px 20px 30px !important;box-shadow:0 0 0 1px rgba(80,66,46,0.18),0 0 0 5px #F4F0E9,0 0 0 6px rgba(80,66,46,0.16),0 20px 40px rgba(30,24,16,0.16)}}"
)
f = sys.argv[1]; s = open(f).read()
if '.grid-contact > form{background:#FFFFFF' not in s:
    s = s.replace('</style>', CSS + '</style>', 1); open(f, 'w').write(s); print('added')
