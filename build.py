#!/usr/bin/env python3
# Static generator for 4hubs4hap.com (Happ hub). Outputs public/<slug>/index.html
import os, html, json

SITE = "https://4hubs4hap.com"
COUNTER = "110249461"
LK = "https://lk.chekdns.click/"
TG = "https://t.me/tgbpn_bot?start=utm_4hubs4hap"
OUT = os.path.join(os.path.dirname(__file__), "public")

NAV = [
    ("/", "Главная"),
    ("/skachat/", "Скачать"),
    ("/tarify/", "Тарифы"),
    ("/config/", "Конфигурации"),
    ("/podkluchenie/", "Подключение"),
    ("/windows/", "Windows"),
    ("/android/", "Android"),
    ("/iphone/", "iPhone"),
    ("/tv/", "TV"),
    ("/oshibki/", "Ошибки"),
    ("/faq/", "FAQ"),
]

METRIKA = (
    '<!-- Yandex.Metrika --><script>(function(m,e,t,r,i,k,a){m[i]=m[i]||function(){(m[i].a=m[i].a||[]).push(arguments)};'
    'm[i].l=1*new Date();for(var j=0;j<document.scripts.length;j++){if(document.scripts[j].src===r){return;}}'
    'k=e.createElement(t),a=e.getElementsByTagName(t)[0],k.async=1,k.src=r,a.parentNode.insertBefore(k,a)})'
    '(window,document,"script","https://mc.yandex.ru/metrika/tag.js","ym");'
    f'ym({COUNTER},"init",{{clickmap:true,trackLinks:true,accurateTrackBounce:true,webvisor:true}});'
    "document.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('a');if(!a)return;"
    "var h=a.href||'';if(h.indexOf('lk.chekdns.click')>-1){ym(" + COUNTER + ",'reachGoal','go_lk');}"
    "else if(h.indexOf('t.me/')>-1){ym(" + COUNTER + ",'reachGoal','tg_click');}});</script>"
    f'<noscript><div><img src="https://mc.yandex.ru/watch/{COUNTER}" style="position:absolute;left:-9999px;" alt=""/></div></noscript><!-- /Yandex.Metrika -->'
)

THEME_JS = (
    "<script>(function(){try{var t=localStorage.getItem('theme');"
    "if(t==='dark')document.documentElement.setAttribute('data-theme','dark');}catch(e){}})();</script>"
)
THEME_TOGGLE_JS = (
    "<script>function toggleTheme(){var d=document.documentElement,dark=d.getAttribute('data-theme')==='dark';"
    "if(dark){d.removeAttribute('data-theme');try{localStorage.setItem('theme','light')}catch(e){}}"
    "else{d.setAttribute('data-theme','dark');try{localStorage.setItem('theme','dark')}catch(e){}}}</script>"
)

SUN = ('<svg class="sun" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>'
       '<svg class="moon" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M21 12.8A9 9 0 1 1 11.2 3 7 7 0 0 0 21 12.8z"/></svg>')

with open(os.path.join(os.path.dirname(__file__), "keywords.json"), encoding="utf-8") as _kf:
    KEYWORDS = json.load(_kf)

def kw_block(page_key, title, intro):
    items = KEYWORDS.get(page_key, [])
    if not items:
        return ""
    spans = "".join(f'<span>{html.escape(p)}</span>' for p in items)
    return (
        '<section class="kw-sec"><div class="wrap">'
        f'<div class="sec-head"><h2>{title}</h2><p>{intro}</p></div>'
        f'<div class="kwc">{spans}</div></div></section>'
    )

def ico(p):
    return f'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{p}</svg>'

CHECK = '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>'

TG_ICON = '<svg width="26" height="26" viewBox="0 0 24 24" fill="currentColor"><path d="M21.94 4.34 18.9 19.2c-.23 1.02-.84 1.27-1.7.79l-4.7-3.46-2.27 2.18c-.25.25-.46.46-.94.46l.33-4.78L18.6 6.2c.38-.34-.08-.53-.59-.19L7.4 12.86l-4.64-1.45c-1.01-.32-1.03-1.01.21-1.49l18.15-7c.84-.31 1.58.2 1.31 1.41z"/></svg>'
KEY_ICON = '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="7.5" cy="15.5" r="5.5"/><path d="M11.5 11.5 21 2M16 7l3 3"/></svg>'
ARROW = '<svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'

def cta_duo():
    return (
        '<div class="cta-duo">'
        f'<a href="{LK}" class="cta-card cta-lk"><span class="cta-ic">{KEY_ICON}</span>'
        '<span class="cta-tx"><b>Личный кабинет</b><span>Оформить доступ и получить конфигурацию</span></span>'
        f'<span class="cta-go">{ARROW}</span></a>'
        f'<a href="{TG}" class="cta-card cta-tg"><span class="cta-ic">{TG_ICON}</span>'
        '<span class="cta-tx"><b>Telegram-бот</b><span>Быстрый доступ и поддержка 24/7</span></span>'
        f'<span class="cta-go">{ARROW}</span></a>'
        '</div>'
    )

PLATFORMS = [("/windows/", "Windows"), ("/android/", "Android"), ("/iphone/", "iPhone"), ("/tv/", "TV")]
NAV_MAIN = [("/", "Главная"), ("/skachat/", "Скачать"), ("/tarify/", "Тарифы"), ("/config/", "Конфигурации"), ("/podkluchenie/", "Подключение")]
NAV_TAIL = [("/oshibki/", "Ошибки"), ("/faq/", "FAQ")]
CHEV = '<svg class="chev" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M6 9l6 6 6-6"/></svg>'

def header(active):
    def lnk(u, t):
        return f'<a href="{u}"{" aria-current=\"page\"" if u==active else ""}>{html.escape(t)}</a>'
    plat_active = ' data-active="1"' if active in [u for u, _ in PLATFORMS] else ''
    plat_sub = "".join(lnk(u, t) for u, t in PLATFORMS)
    links = "".join(lnk(u, t) for u, t in NAV_MAIN)
    links += (
        '<div class="nav-drop">'
        f'<button type="button" class="nav-drop-btn"{plat_active} aria-haspopup="true">Платформы{CHEV}</button>'
        f'<div class="nav-sub">{plat_sub}</div></div>'
    )
    links += "".join(lnk(u, t) for u, t in NAV_TAIL)
    drawer = "".join(f'<a href="{u}">{html.escape(t)}</a>' for u, t in NAV)
    return (
        '<header class="nav"><div class="nav-inner">'
        '<a href="/" class="brand"><span class="brand-mark">H</span>Happ&nbsp;Hub</a>'
        f'<nav class="nav-links" aria-label="Главное меню">{links}</nav>'
        '<div class="nav-right">'
        f'<button class="theme-btn" type="button" aria-label="Сменить тему" onclick="toggleTheme()">{SUN}</button>'
        f'<a href="{LK}" class="nav-cta">Получить доступ</a>'
        '<button class="nav-burger" type="button" aria-label="Меню" onclick="document.querySelector(\'.drawer\').classList.toggle(\'open\')">'
        '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg></button>'
        '</div></div>'
        f'<div class="drawer">{drawer}<a href="{LK}" style="color:var(--accent)">Получить доступ →</a></div>'
        '</header>'
    )

FOOT_COLS = [
    ("Платформы", [("/windows/","Windows"),("/android/","Android"),("/iphone/","iPhone"),("/tv/","Android TV")]),
    ("Помощь", [("/podkluchenie/","Подключение"),("/config/","Конфигурации"),("/oshibki/","Ошибки"),("/faq/","FAQ")]),
    ("Сервис", [("/skachat/","Скачать Happ"),("/tarify/","Тарифы"),(LK,"Личный кабинет"),(TG,"Telegram")]),
]
def footer():
    cols = ""
    for title, items in FOOT_COLS:
        links = "".join(f'<a href="{u}">{html.escape(t)}</a>' for u, t in items)
        cols += f'<div><h4>{title}</h4>{links}</div>'
    return (
        '<footer class="foot"><div class="wrap"><div class="foot-grid">'
        '<div><a href="/" class="brand" style="margin-bottom:10px"><span class="brand-mark">H</span>Happ&nbsp;Hub</a>'
        '<p class="muted" style="font-size:.92rem;max-width:280px">Справочный центр по приложению Happ: установка на любые устройства, '
        'загрузка конфигураций и решение типичных ошибок подключения.</p></div>'
        f'{cols}</div>'
        '<div class="foot-bottom"><span>© 2026 Happ Hub. Информационный проект, не является официальным сайтом разработчика Happ.</span>'
        '<span>4hubs4hap.com</span></div></div></footer>'
    )

def page(slug, title, desc, body, active=None):
    active = active if active is not None else slug
    canonical = SITE + ("/" if slug == "/" else slug)
    doc = (
        '<!doctype html><html lang="ru"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        f'<title>{html.escape(title)}</title>'
        f'<meta name="description" content="{html.escape(desc)}">'
        f'<link rel="canonical" href="{canonical}">'
        f'<meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}">'
        f'<meta property="og:type" content="website"><meta property="og:url" content="{canonical}">'
        '<link rel="icon" type="image/svg+xml" href="/favicon.svg">'
        '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
        '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700&family=Sora:wght@600;700&family=JetBrains+Mono:wght@500&display=swap">'
        '<link rel="stylesheet" href="/assets/styles.css?v=6">'
        '<link rel="preconnect" href="https://mc.yandex.ru" crossorigin>'
        + THEME_JS + METRIKA +
        '</head><body>'
        + header(active) + "<main>" + body + "</main>" + footer() + THEME_TOGGLE_JS +
        '</body></html>'
    )
    d = OUT if slug == "/" else os.path.join(OUT, slug.strip("/"))
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
        f.write(doc)

def crumbs(*parts):
    items = ['<a href="/">Главная</a>']
    for u, t in parts:
        items.append(f'<a href="{u}">{html.escape(t)}</a>' if u else f'<span>{html.escape(t)}</span>')
    return '<div class="wrap"><nav class="crumbs">' + ' / '.join(items) + '</nav></div>'

# ---- content imported from pages.py ----
import pages
pages.build(globals())
print("done")
