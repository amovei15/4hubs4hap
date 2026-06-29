#!/usr/bin/env python3
# Static generator for 4hubs4hap.com (Happ hub). Outputs public/<slug>/index.html
import os, html

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
    "if(t==='light')document.documentElement.setAttribute('data-theme','light');}catch(e){}})();</script>"
)
THEME_TOGGLE_JS = (
    "<script>function toggleTheme(){var d=document.documentElement,l=d.getAttribute('data-theme')==='light';"
    "if(l){d.removeAttribute('data-theme');try{localStorage.setItem('theme','dark')}catch(e){}}"
    "else{d.setAttribute('data-theme','light');try{localStorage.setItem('theme','light')}catch(e){}}}</script>"
)

SUN = ('<svg class="sun" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>'
       '<svg class="moon" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M21 12.8A9 9 0 1 1 11.2 3 7 7 0 0 0 21 12.8z"/></svg>')

def ico(p):
    return f'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{p}</svg>'

CHECK = '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>'

def header(active):
    links = "".join(
        f'<a href="{u}"{" aria-current=\"page\"" if u==active else ""}>{html.escape(t)}</a>'
        for u, t in NAV
    )
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
        '<link rel="stylesheet" href="/assets/styles.css?v=1">'
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
