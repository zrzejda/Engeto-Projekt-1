"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Petra Voldánová
email: petra.voldanova@gmail.com
discord: Petra V.
"""

users = {"bob":"123", "ann":"pass123", "mike":"password123", "liz":"pass123"}
text_1 = """Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley."""
slova_text_1 = text_1.split()
pocet_slov_text_1 = len(slova_text_1)
pocet_slov_text_1_velke_pismeno = sum(1 for slovo in slova_text_1 if slovo[0].isupper())
pocet_slov_text_1_velkymi_pismeny = sum(1 for slovo in slova_text_1 if slovo.isupper())
pocet_slov_text_1_malymi_pismeny = sum(1 for slovo in slova_text_1 if slovo.islower())
pocet_cisel_text_1 = sum(1 for slovo in slova_text_1 if slovo.isdigit())
soucet_cisel_text_1 = sum(int(slovo) for slovo in slova_text_1 if slovo.isdigit())
delky_slov_text_1 = [len(slovo) for slovo in slova_text_1]
delky_slov_text_1.sort()
 
text_2 = """At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick."""
slova_text_2 = text_2.split()
pocet_slov_text_2 = len(slova_text_2)
pocet_slov_text_2_velke_pismeno = sum(1 for slovo in slova_text_2 if slovo[0].isupper())
pocet_slov_text_2_velkymi_pismeny = sum(1 for slovo in slova_text_2 if slovo.isupper())
pocet_slov_text_2_malymi_pismeny = sum(1 for slovo in slova_text_2 if slovo.islower())
pocet_cisel_text_2 = sum(1 for slovo in slova_text_2 if slovo.isdigit())
soucet_cisel_text_2 = sum(int(slovo) for slovo in slova_text_2 if slovo.isdigit())
delky_slov_text_2 = [len(slovo) for slovo in slova_text_2]

delky_slov_text_2.sort()
frekvence_2 = {}
for item in delky_slov_text_2:
   if item in frekvence_2:
      frekvence_2[item] = frekvence_2[item] + 1
   else:
      frekvence_2[item] = 1

for delka, cetnost in frekvence_2.items():
   hvezdicky = "*" * cetnost

text_3 = """The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present."""
slova_text_3 = text_3.split()
pocet_slov_text_3 = len(slova_text_3)
pocet_slov_text_3_velke_pismeno = sum(1 for slovo in slova_text_3 if slovo[0].isupper())
pocet_slov_text_3_velkymi_pismeny = sum(1 for slovo in slova_text_3 if slovo.isupper())
pocet_slov_text_3_malymi_pismeny = sum(1 for slovo in slova_text_3 if slovo.islower())
pocet_cisel_text_3 = sum(1 for slovo in slova_text_3 if slovo.isdigit())
soucet_cisel_text_3 = sum(int(slovo) for slovo in slova_text_3 if slovo.isdigit())
delky_slov_text_3 = [len(slovo) for slovo in slova_text_3]
delky_slov_text_3.sort()

frekvence_3 = {}
for item in delky_slov_text_3:
   if item in frekvence_3:
      frekvence_3[item] = frekvence_3[item] + 1
   else:
      frekvence_3[item] = 1

for delka, cetnost in frekvence_3.items():
   hvezdicky = str("*" * cetnost)

print("Dobrý den, vítejte v textovém analyzátoru. ")
jmeno = input("Zadejte uživatelské jméno: ")
heslo = input("Zadejte heslo: ")
if jmeno in users and users[jmeno] == heslo:
   print("Přihlášení bylo úspěšné.")
   cislo_textu = int(input("Zvolte text č. 1, 2 nebo 3. "))
   if cislo_textu == 1:
      print("Celkový počet slov v textu: ", pocet_slov_text_1, ".", sep="")
      print("Počet slov začínajících velkými písmeny: ", pocet_slov_text_1_velke_pismeno, ".", sep="")
      print("Počet slov napsaných velkými písmeny: ", pocet_slov_text_1_velkymi_pismeny, ".", sep="")
      print("Počet slov napsaných malými písmeny: ", pocet_slov_text_1_malymi_pismeny, ".", sep="")
      print("Počet čísel: ", pocet_cisel_text_1, ".", sep="")
      print("Součet čísel: ", soucet_cisel_text_1, ".", sep="")
      print("-" * 40)
      print("DÉLKA | POČET") 
      print("-" * 40)
      frekvence_1 = {}
      for item in delky_slov_text_1:
         if item in frekvence_1:
            frekvence_1[item] = frekvence_1[item] + 1
         else:
            frekvence_1[item] = 1
      for delka, pocet in frekvence_1.items():
         hvezdicky = '*' * pocet
         print(f"{delka:2}| {hvezdicky} {pocet}")
                  
   elif cislo_textu == 2:
      print("Celkový počet slov v textu: ", pocet_slov_text_2, ".", sep="")
      print("Počet slov začínajících velkými písmeny: ", pocet_slov_text_2_velke_pismeno, ".", sep="")
      print("Počet slov napsaných velkými písmeny: ", pocet_slov_text_2_velkymi_pismeny, ".", sep="")
      print("Počet slov napsaných malými písmeny: ", pocet_slov_text_2_malymi_pismeny, ".", sep="")
      print("Počet čísel: ", pocet_cisel_text_2, ".", sep="")
      print("Součet čísel: ", soucet_cisel_text_2, ".", sep="")
      print("-" * 40)
      print("DÉLKA | POČET") 
      print("-" * 40)
      frekvence_2 = {}
      for item in delky_slov_text_2:
         if item in frekvence_2:
            frekvence_2[item] = frekvence_2[item] + 1
         else:
            frekvence_2[item] = 1
      for delka, pocet in frekvence_2.items():
         hvezdicky = '*' * pocet
         print(f"{delka:2}| {hvezdicky} {pocet}")
      
   elif cislo_textu == 3:
      print("Celkový počet slov v textu: ", pocet_slov_text_3, ".", sep="")
      print("Počet slov začínajících velkými písmeny: ", pocet_slov_text_3_velke_pismeno, ".", sep="")
      print("Počet slov napsaných velkými písmeny: ", pocet_slov_text_3_velkymi_pismeny, ".", sep="")
      print("Počet slov napsaných malými písmeny: ", pocet_slov_text_3_malymi_pismeny, ".", sep="")
      print("Počet čísel: ", pocet_cisel_text_3, ".", sep="")
      print("Součet čísel: ", soucet_cisel_text_3, ".", sep="")
      print("-" * 40)
      print("DÉLKA | POČET") 
      print("-" * 40)
      frekvence_3 = {}
      for item in delky_slov_text_3:
         if item in frekvence_3:
            frekvence_3[item] = frekvence_3[item] + 1
         else:
            frekvence_3[item] = 1
      for delka, pocet in frekvence_3.items():
         hvezdicky = '*' * pocet
         print(f"{delka:2}| {hvezdicky} {pocet}")
      
   else:
      print("Toto není platné číslo textu. Musíte zadat 1, 2, nebo 3.")
else:
   print("Neznámý uživatel. Program nemůže pokračovat. ")