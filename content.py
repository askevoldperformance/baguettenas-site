# -*- coding: utf-8 -*-

SITE_URL = "https://baguettenas.no"  # oppdater til faktisk domene før deploy
SITE_NAME = "Baguetten AS"
GTM_ID = ""  # legg inn GTM-container-ID når klar

TAGLINE = "Alltid ferske og påsmurte baguetter, kaffe og mineralvann. Velkommen!"

# --- UKENS BAGUETT ---
# Rekkefølgen under er dagens rekkefølge fra menyen.
# Rulleringen er ISO-ukebasert (uke % antall baguetter) og kjøres i nettleseren,
# så den går videre automatisk hver mandag uten redeploy.
# Bytt rekkefølge/liste her når dere har bestemt fast rullering.
BAGUETTES = [
    {"name": "Reker m/majones", "price": "89,-", "allergens": "1, 10"},
    {"name": "Roastbeef m/remulade", "price": "87,-", "allergens": "1, 3, 11"},
    {"name": "Kylling m/potetsalat", "price": "87,-", "allergens": "1, 8"},
    {"name": "Brie m/bacon", "price": "87,-", "allergens": "4, 5"},
    {"name": "Karbonade m/løk", "price": "87,-", "allergens": "1, 3, 4, 8, 11"},
    {"name": "Omelette m/bacon", "price": "83,-", "allergens": "1"},
    {"name": "Leverpostei m/bacon", "price": "87,-", "allergens": "3, 4, 7, 11"},
    {"name": "Kylling tandoori", "price": "83,-", "allergens": "1"},
    {"name": "Egg/majones", "price": "73,-", "allergens": "1"},
    {"name": "Tunfisk", "price": "73,-", "allergens": "1, 2"},
    {"name": "Ost og skinke", "price": "76,-", "allergens": "4"},
    {"name": "Krepshaler i chilimajones m/egg", "price": "92,-", "allergens": "1, 4, 8, 10"},
    {"name": "Egg m/rekesalat", "price": "73,-", "allergens": "1, 10"},
]

OTHER_ITEMS = [
    {"name": "1 brett egg / 30 egg", "price": "100,-"},
]

DRINKS = [
    {"name": "Mineralvann", "price": "32,-"},
    {"name": "Brus", "price": "35,-"},
    {"name": "Iste", "price": "36,-"},
    {"name": "Iskaffe", "price": "28,-"},
    {"name": "Vann", "price": "32,-"},
    {"name": "Cocio", "price": "36,-"},
    {"name": "Monster", "price": "37,-"},
    {"name": "Kaffe", "price": "25,-"},
    {"name": "Litago", "price": "28,-"},
    {"name": "Eplemost fra Dyre Gård", "price": "39,-"},
    {"name": "Energidrikker", "price": "36,-"},
]

ALLERGEN_NOTE = [
    ("Baguett 'fin'", "inneholder bygg og hvete"),
    ("Baguett 'grov'", "inneholder hvete og kli"),
]

ALLERGEN_CODES = [
    "1. Egg", "2. Fisk", "3. Glutenholdig korn, bygg og hvete", "4. Melk",
    "5. Nøtter - valnøtter", "6. Peanøtter", "7. Selleri", "8. Sennep",
    "9. Sesamfrø", "10. Skalldyr", "11. Soya", "12. Sulfitt",
    "13. Bløtdyr", "14. Lupiner",
]

LOCATIONS = [
    {
        "name": "Moss",
        "address": "Varnaveien 27, 1526 Moss, Norge",
        "hours": "Mandag–Fredag: 07:00–16:00<br>Lørdag: 09:00–15:00",
        "phone": "69 26 64 70",
        "emails": ["post@baguettenmoss.no", "bestilling@baguettenmoss.no"],
        "map_query": "Varnaveien+27,+Moss,+Norge",
    },
    {
        "name": "Fredrikstad",
        "address": "Apenes gate 20, 1607 Fredrikstad, Norge",
        "hours": "Mandag–Fredag: 07:00–16:00<br>Lørdag: 09:00–15:00",
        "phone": "69 26 64 70",
        "emails": ["post@baguettenfredrikstad.no", "bestilling@baguettenfredrikstad.no"],
        "map_query": "Apenes+gate+20,+Fredrikstad,+Norge",
    },
]
