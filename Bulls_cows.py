"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Magdalena Kreckova
email: kreckova.majda@gmail.com
discord: Majda_247
"""

import random

#Funkce pro pozdrav
def uvitani():
    """
    Uvítá uživatele ve hře a seznámí ho s pravidly.
    """
    print("Ahoj, vítej ve hře!")
    print("-"*100)
    print("Vygeneruji pro tebe 4 náhodné číslice v určitém pořadí (číslice se nesmí opakovat) a tvým úkolem bude je hádat.\n" 
          "Pokud číslici uhádneš, ale je na nesprávné pozici, program zahlásí 'Cow'.\n"
          "Pokud číslici uhádneš a je na správné pozici, program ti zahlácí 'Bull'\n"
          "Tvým úkolem je získat 4x Bulls")
    print("-"*100)

#Funkce pro vytvoření náhodného čísla
def generator():
    """
    Funkce vygeneruje 4 náhodné číslice, které nebudou začínat 0 a které bude hráč hádat.
    """
    prvni_cislice = random.choice(range(1, 10)) #první číslice není 0
    dalsi_cislice = random.sample(list(set(range(10)) - {prvni_cislice}), 3)
    tajne_cislo = str(prvni_cislice) + ''.join(map(str, dalsi_cislice))
    # print(tajne_cislo) #slouží pro lepší kontrolu pro další zápis kódu, až bude kód funkční, stačí odstranit z funkce 
    return tajne_cislo

#Kontrola formátu zadaného čísla
def kontrola_format(tip):
    """
    Zkontroluje, jestli zadaná hodnota uživatelem splňuje podmínky:
    -je to čtyřmístné číslo
    -první číslice není nula
    -číslice se neopakují. 
    Vrací True pokud vstup splňuje podmínky. Pokud ne, vrátí False a vypíše příslušnou zprávu.
    """
    #kontrola čtyřmístného čísla
    if not tip.isdigit() or len(tip) != 4:
        print("Tvůj tip musí být čtyřmístné číslo složené pouze z číslic.")
        return False
    
    #kontrola, zda první číslice není nula
    if tip[0] == '0':
        print("Tvůj tip nesmí začínat nulou.")
        return False
    
    #kontrola zda se číslice neopakují
    if len(set(tip)) != len(tip):
        print("Tvůj tip nesmí obsahovat opakující se číslice.")
        return False 
    
    #Všechny podmínky jsou splněny
    return True

#Funkce, která kontroluje totožnost zadaného čísla s číslem vygenerovaným 
def kontrola(uzivatelske_cislo, tajne_cislo):
    """
    Kontroluje, jestli je zadané uživatelské číslo totožné s tajným číslem.
    Zároveň vypisuje bull a cow pro jednotlivé typy. 
    """
    pocet_bull = 0
    pocet_cow = 0

    #počty bull a cow
    for i in range(4):
        if uzivatelske_cislo[i] == tajne_cislo[i]:
            pocet_bull += 1
        elif uzivatelske_cislo[i] in tajne_cislo:
            pocet_cow += 1
    
    #Jednotné a množné číslo bull a cow
    bull = "bull" if pocet_bull == 1 else "bulls"
    cow = "cow" if pocet_cow == 1 else "cows"

    print(f"{pocet_bull} {bull}, {pocet_cow} {cow}")

#Funkce pro hodnocení hry podle pokusů
def hodnoceni(pocet_pokusu):
    """
    Funkce zhodnotí průběh hry podle počtu pokusů zadání čísla.
    """
    if pocet_pokusu == 1:
        vyhodnoceni_vysledku = "Máš obří štěstí!"
    elif pocet_pokusu in (2, 3):
        vyhodnoceni_vysledku = "To ujde, máš štěstí!"
    elif pocet_pokusu in (4, 5):
        vyhodnoceni_vysledku = "To není špatné!"
    elif pocet_pokusu in (6, 7):
        vyhodnoceni_vysledku = "Uhádl jsi to celkem rychle!"
    elif pocet_pokusu in (8, 9):
        vyhodnoceni_vysledku = "To nebyla moc dobrá hra!"
    else:
        vyhodnoceni_vysledku = "Zkus být příště lepší..."
    return vyhodnoceni_vysledku

#Funkce na spuštění hry
def hraj_hru():
    """
    Zapojí všechny potřebné funkce a spustí hru. 
    """

    uvitani()
    tajne_cislo = generator()
    pocet_pokusu = 0

    while True:
        tip = input("Zadej svůj tip:")

        #Zkontroluje formát uživatelského čísla:
        if not kontrola_format(tip):
            continue
        
        #Zvýšení počtu pokusů a kontrola
        pocet_pokusu += 1
        kontrola(tip, tajne_cislo)

        #Kontrola výhry
        if tip == tajne_cislo:
            print("Gratuluji! Uhodl jsi správné číslo!")
            print(hodnoceni(pocet_pokusu))
            break

if __name__ == "__main__":
    hraj_hru()