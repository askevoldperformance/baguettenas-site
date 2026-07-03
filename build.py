# -*- coding: utf-8 -*-
import json
from build_helpers import page, ukens_baguett_widget, menu_table, location_card
from content import (
    TAGLINE, BAGUETTES, OTHER_ITEMS, DRINKS, ALLERGEN_NOTE, ALLERGEN_CODES, LOCATIONS
)

BAGUETTES_JSON = json.dumps(BAGUETTES, ensure_ascii=False)


# ---------- FORSIDE ----------
def build_index():
    hours_moss = LOCATIONS[0]["hours"]
    hours_fred = LOCATIONS[1]["hours"]

    body = f"""
<section class="hero">
    <div class="hero-text">
        <h1>Baguetten AS</h1>
        <p class="hero-tagline">{TAGLINE}</p>
        <a href="/meny" class="btn-cta">Se meny</a>
    </div>
    <img class="hero-image" src="/images/baguetter.jpg" alt="Ferske baguetter fra Baguetten AS">
</section>

<section class="frontpage-grid">
    <div class="card">
        <span class="card-eyebrow">Åpningstider</span>
        <h3>Moss</h3>
        <p>{hours_moss}</p>
        <h3>Fredrikstad</h3>
        <p>{hours_fred}</p>
    </div>

    {ukens_baguett_widget(BAGUETTES_JSON)}

    <div class="card">
        <span class="card-eyebrow">Meny</span>
        <p>Bredt utvalg av ferske baguetter, snacks og drikke. Ønsker du noe annet, smører vi på bestilling.</p>
        <a href="/meny" class="card-link">Se full meny &rarr;</a>
    </div>

    <div class="card">
        <span class="card-eyebrow">Kontakt</span>
        <p>Besøk oss i Moss eller Fredrikstad, eller ta kontakt for bestilling.</p>
        <a href="/kontakt" class="card-link">Kontaktinfo &rarr;</a>
    </div>
</section>
"""
    page(
        "index.html",
        "Baguetten AS – Ferske baguetter i Moss og Fredrikstad",
        "Ferske og påsmurte baguetter, kaffe og mineralvann. Besøk oss i Moss eller Fredrikstad.",
        "/",
        body,
    )


# ---------- MENY ----------
def build_meny():
    baguett_rows = [[b["name"], b["price"], b["allergens"]] for b in BAGUETTES]
    other_rows = [[o["name"], o["price"]] for o in OTHER_ITEMS]
    drink_rows = [[d["name"], d["price"]] for d in DRINKS]

    allergen_note_html = "".join(
        f"<p><strong>{name}</strong>: {desc}</p>" for name, desc in ALLERGEN_NOTE
    )
    allergen_list_html = "".join(f"<li>{code}</li>" for code in ALLERGEN_CODES)

    body = f"""
<section class="page-header">
    <h1>Meny</h1>
    <p>Vi har et bredt utvalg av baguetter. Ønsker du noe annet løser vi dette, da vi også smører ferske baguetter på bestilling. Byens beste lunsj!</p>
</section>

<section class="menu-section">
    {ukens_baguett_widget(BAGUETTES_JSON)}

    <h2>Baguetter</h2>
    {menu_table(baguett_rows, ["Baguette", "Pris", "Allergener"])}

    <h2>Annet</h2>
    {menu_table(other_rows, ["Vare", "Pris"], css_class="other-items-table")}

    <h2>Drikke</h2>
    {menu_table(drink_rows, ["Drikke", "Pris"], css_class="other-items-table")}

    <div class="allergens">
        <h3>Allergener</h3>
        {allergen_note_html}
        <p><strong>Nummerkoder:</strong></p>
        <ul>{allergen_list_html}</ul>
    </div>
</section>
"""
    page(
        "meny.html",
        "Meny – Baguetten AS",
        "Full meny med baguetter, snacks og drikke fra Baguetten AS.",
        "/meny",
        body,
    )


# ---------- KONTAKT ----------
def build_kontakt():
    cards = "".join(location_card(loc) for loc in LOCATIONS)
    body = f"""
<section class="page-header">
    <h1>Kontakt</h1>
    <p>Besøk oss i Moss eller Fredrikstad, eller ta kontakt for bestilling.</p>
</section>

<section class="contact-locations">
    {cards}
</section>
"""
    page(
        "kontakt.html",
        "Kontakt – Baguetten AS",
        "Adresse, åpningstider og kontaktinfo for Baguetten AS i Moss og Fredrikstad.",
        "/kontakt",
        body,
    )


if __name__ == "__main__":
    build_index()
    build_meny()
    build_kontakt()
