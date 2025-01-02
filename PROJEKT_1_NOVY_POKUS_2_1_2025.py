users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}

texts = [
    """Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30N and the Union Pacific Railroad,
    which traverse the valley.""",
    """At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.""",
    """The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present."""
]

def analyzuj_text(text):
    slova = text.split()
    pocet_slov = len(slova)
    pocet_velke_pismeno = sum(1 for slovo in slova if slovo[0].isupper())
    pocet_velkymi_pismeny = sum(1 for slovo in slova if slovo.isupper())
    pocet_malymi_pismeny = sum(1 for slovo in slova if slovo.islower())
    pocet_cisel = sum(1 for slovo in slova if slovo.isdigit())
    soucet_cisel = sum(int(slovo) for slovo in slova if slovo.isdigit())
    delky_slov = sorted(len(slovo) for slovo in slova)
    frekvence_delky = {}
    for delka in delky_slov:
        frekvence_delky[delka] = frekvence_delky.get(delka, 0) + 1
    return {
        "pocet_slov": pocet_slov,
        "pocet_velke_pismeno": pocet_velke_pismeno,
        "pocet_velkymi_pismeny": pocet_velkymi_pismeny,
        "pocet_malymi_pismeny": pocet_malymi_pismeny,
        "pocet_cisel": pocet_cisel,
        "soucet_cisel": soucet_cisel,
        "frekvence_delky": frekvence_delky
    }

def zobraz_vysledky(analyza):
    print(f"Celkový počet slov v textu: {analyza['pocet_slov']}.")
    print(f"Počet slov začínajících velkými písmeny: {analyza['pocet_velke_pismeno']}.")
    print(f"Počet slov napsaných velkými písmeny: {analyza['pocet_velkymi_pismeny']}.")
    print(f"Počet slov napsaných malými písmeny: {analyza['pocet_malymi_pismeny']}.")
    print(f"Počet čísel: {analyza['pocet_cisel']}.")
    print(f"Součet čísel: {analyza['soucet_cisel']}.")
    print("-" * 40)
    print("DÉLKA | POČET")
    print("-" * 40)
    for delka, pocet in analyza["frekvence_delky"].items():
        hvezdicky = '*' * pocet
        print(f"{delka:2} | {hvezdicky} {pocet}")

print("Dobrý den, vítejte v textovém analyzátoru.")
jmeno = input("Zadejte uživatelské jméno: ")
heslo = input("Zadejte heslo: ")

if jmeno in users and users[jmeno] == heslo:
    print("Přihlášení bylo úspěšné.")
    cislo_textu = int(input("Zvolte text č. 1, 2 nebo 3: "))
    if 1 <= cislo_textu <= 3:
        analyza = analyzuj_text(texts[cislo_textu - 1])
        zobraz_vysledky(analyza)
    else:
        print("Toto není platné číslo textu. Musíte zadat 1, 2, nebo 3.")
else:
    print("Neznámý uživatel. Program nemůže pokračovat.")
