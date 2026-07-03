# -*- coding: utf-8 -*-
from content import SITE_URL, SITE_NAME, GTM_ID


def head_html(title, description, canonical_path):
    gtm_snippet = ""
    if GTM_ID:
        gtm_snippet = f"""
    <script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);}})(window,document,'script','dataLayer','{GTM_ID}');</script>"""
    return f"""<!DOCTYPE html>
<html lang="no">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{description}">
    <link rel="canonical" href="{SITE_URL}{canonical_path}">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="og:url" content="{SITE_URL}{canonical_path}">
    <meta property="og:type" content="website">
    <link rel="icon" href="/images/logo.png">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/style.css">{gtm_snippet}
</head>
<body>
"""


def nav_html(active_path="/"):
    def cls(path):
        return "active" if path == active_path else ""

    return f"""<nav class="site-nav">
    <div class="nav-inner">
        <a href="/" class="nav-logo">
            <span>{SITE_NAME}</span>
        </a>
        <ul class="nav-links">
            <li><a href="/" class="{cls('/')}">Forside</a></li>
            <li><a href="/meny" class="{cls('/meny')}">Meny</a></li>
            <li><a href="/kontakt" class="nav-pill {cls('/kontakt')}">Kontakt</a></li>
        </ul>
        <button class="nav-hamburger" aria-label="Meny">&#9776;</button>
    </div>
</nav>
"""


def footer_html():
    return """<footer class="site-footer">
    <div class="footer-inner">
        <div class="footer-brand">
            <span>Baguetten AS</span>
        </div>
        <nav class="footer-links">
            <a href="/">Forside</a>
            <a href="/meny">Meny</a>
            <a href="/kontakt">Kontakt</a>
        </nav>
        <p class="footer-copy">&copy; 2026 Baguetten AS</p>
    </div>
</footer>
<script src="/main.js" defer></script>
<script src="/ukens-baguett.js" defer></script>
"""


def page(filepath, title, description, canonical_path, body_html, extra_scripts=""):
    import os
    html = head_html(title, description, canonical_path)
    html += nav_html(canonical_path)
    html += body_html
    html += footer_html()
    html += extra_scripts
    html += "</body>\n</html>\n"
    os.makedirs(os.path.dirname(filepath) or ".", exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"built {filepath}")


def ukens_baguett_widget(baguettes_json):
    """Placeholder box filled client-side by ukens-baguett.js (auto-rotates weekly)."""
    return f"""<div class="ukens-baguett" id="ukens-baguett">
    <span class="ukens-baguett-eyebrow">Ukens baguett</span>
    <div class="ukens-baguett-body">
        <h3 id="ukens-baguett-name">Laster...</h3>
        <div class="ukens-baguett-meta">
            <span id="ukens-baguett-price"></span>
            <span id="ukens-baguett-allergens"></span>
        </div>
    </div>
</div>
<script>window.__BAGUETTES__ = {baguettes_json};</script>
"""


def menu_table(rows, headers, css_class="menu-table"):
    head_cells = "".join(f"<th>{h}</th>" for h in headers)
    body_rows = ""
    for r in rows:
        cells = "".join(f"<td>{c}</td>" for c in r)
        body_rows += f"<tr>{cells}</tr>\n"
    return f"""<table class="{css_class}">
    <thead><tr>{head_cells}</tr></thead>
    <tbody>
{body_rows}    </tbody>
</table>
"""


def location_card(loc):
    emails = "<br>".join(loc["emails"])
    return f"""<div class="location-card">
    <h3>{loc['name']}</h3>
    <p><strong>Adresse:</strong> {loc['address']}</p>
    <p><strong>Åpningstider:</strong><br>{loc['hours']}</p>
    <p><strong>Telefon:</strong> <a href="tel:{loc['phone'].replace(' ', '')}">{loc['phone']}</a></p>
    <p><strong>E-post:</strong><br>{emails}</p>
    <iframe src="https://www.google.com/maps?q={loc['map_query']}&output=embed" width="100%" height="220" style="border:0;" loading="lazy"></iframe>
</div>
"""
