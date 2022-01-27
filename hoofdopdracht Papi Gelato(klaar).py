from datetime import datetime, timedelta,time
import time

ditjaar = datetime.now().year
xmasditjaar = datetime( ditjaar, 12, 25, 23, 59, 59 )
dezedag = datetime.now()
dagen = xmasditjaar - dezedag

w = 0
aantalliter = 0
aantalbolletje = 0
aantalbakjes = 0
aantalhorrentjes = 0
programmaopleveren = 0

if dagen.days < 0:
    print("Kerst komt volgend jaar weer.")
elif dagen.days == 0:
    print("Het is Kerst!")
else:
    print("Slechts", dagen.days, "dagen tot Kerst!")
    
# Aantal bolletjes (-1 voor niks)
aantalbolletje = None

# Vorm - Bakje/Hoorntje
kieshouders = None

print('Welkom bij Papi Gelato')
gebruiksersnaam = input('Wat is uw naam? :')


def geforceerde_input(vraag: str, toegestaan: list[str],
        niet_goed_bericht: str = 'Sorry dat is geen optie die we aanbieden...') -> str:  # hier wordt er gecontroleerd op een bug
    while not ((antwoord := input(vraag).lower()) in toegestaan):
        print(niet_goed_bericht)

    return antwoord

def bonnetjeparticulier():  # hier worden de prijzen van de klanten berekend van zijn/haar bestelling
    global aantalBolletjesOptel
    aantalBolletjesOptel += aantalbolletje
    print("---------['Papi Gelato']---------")
    if aantalBolletjesOptel > 0:
        print(f'bolletjes   {aantalBolletjesOptel} x €0.95   = €{round(aantalBolletjesOptel * 0.95, 2)} ')
    if aantalhorrentjes > 0:
        print (f"hoorntjes  {aantalhorrentjes} x €1.10 = €{round(aantalhorrentjes * 1.10, 2)} ")
    if aantalbakjes > 0:
        print (f"bakjes     {aantalbakjes} x €0.75 = €{round(aantalbakjes * 0.75 , 2)}")
    if toppingsprijs > 0.01:
        print (f"topping(en) = €{round(toppingsprijs , 2)}")
    print ("------------------------------")
    print (f"totaalprijs: €{round(aantalBolletjesOptel * 0.95 + aantalhorrentjes * 1.10 + aantalbakjes * 0.75 + toppingsprijs,2)}")
    print (dezedag)
    

def zakelijkbon(): # hier wordt de bon voor de klant uitgeprint als hij/zij een zakelijke bestelling plaatst
    totaalbedrag = round(aantalliter * 9.80, 2)
    print("---------['Papi Gelato']---------")
    print(f'liters   {aantalliter} x 9,80   = {totaalbedrag} €')
    print('                        -------- +')
    print(f'                        {totaalbedrag}€')
    print(f'btw (6%)                {round(totaalbedrag / 106 * 6 , 2)}€')
    print (dezedag)

# F1.5.02.O7 - Feature: Zakelijke markt bedienenFuncties
def zakelijk():
    global soortklant, aantalliter, w
    soortklant = geforceerde_input("Wat voor klant bent u?  \nA) particulier \nB) zakelijk : ",
                                   ["a", "b"])  # hier wordt gevraagd naar het type klant
    if soortklant == "a":
        print("U bent een particulier")  # als je op  a klikt ben je een klant
    elif soortklant == "b":
        print("u bent een zakelijke klant")  # als je op b klikt ben je een zakelijke klant
        aantalliter = int(geforceerde_input("Hoeveel liters ijs wilt u? : ", [str(q) for q in range (1,88888)]))
        for z in range(aantalliter):  # hier wordt een loop gebruikt
            w += 1
            kiessmaak = geforceerde_input(
                f"voor welke smaak wilt u voor liter  nummer {w}? \nA) Aardbei \nC) Chocolade\nV) Vanille \n : " ,
                ['a', 'c', 'v'])  # smaken voor de aantal liters
        zakelijkbon()
        time.sleep(15)
        exit()

# F1.5.02.O2 - Een programma opleverenFuncties
zakelijk()
def programmaopleveren():
    global aantalbolletje, kieshouders, aantalbakjes
    aantalbolletje = int(geforceerde_input(f'{gebruiksersnaam}, hoeveel bolletjes wilt u? : ', [str(i) for i in range(1,
                                                                                                                      9)]))  # hier wordt gevraagd hoeveel bolletjes de klant wilt

    while aantalbolletje < 4:
        # Gebruiker moet kiezen voor een hoorntje of een bakje
        keuzesoorthouder()
        smaakjeskiezen()
        toppings()
        einde()
        bonnetjeparticulier()
        exit()
    if soortklant == "b":
        # het zakelijke process van Papi-Gelato
        smaakjeskiezen()
        zakelijkbon()
        exit()
    else:
        # Alleen hoorntjes voor minder dan 4 bolletjes
        kieshouders = 'bakje'
        aantalbakjes += 1
        smaakjeskiezen()
        # Vragen of de gebruiker meer wilt
        toppings()
        einde()
        bonnetjeparticulier()
        exit()

# F1.5.02.O3 - 3 nieuwe smakenFuncties
def smaakjeskiezen():
    for i in range(aantalbolletje):
        kiessmaak = geforceerde_input(
            f"Welke smaak wilt u voor bolletje nummer {i + 1}? \nA) Aardbei \nC) Chocolade\nV) Vanille : ",
            ['a', 'c', 'v'])  # er wordt hier gevraagd naar de smaken die de klant per bolletje wilt
        if kiessmaak == "a":
            print("U heeft voor aardbei gekozen")  # hier kiezen ze voor aardbei
        elif kiessmaak == "c":
            print("u heeft voor chocolade gekozen")  # hier kiezen ze voor choco
        else:
            print("U heeft voor vanille gekozen")  # en tot slot voor vanille


def keuzesoorthouder():  # in deze functie kun je kiezen tussen bolletje(s) in een bakje of in een hoorntje
    global kieshouders, aantalbakjes, aantalhorrentjes
    kieshouders = geforceerde_input(
        f'{gebruiksersnaam}, wilt u deze {aantalbolletje} bolletje(s) in\n|hoorntje\n|bakje :',
        ['hoorntje', 'bakje'])
    if kieshouders == "bakje":
        aantalbakjes += 1
    else:
        aantalhorrentjes += 1


# F1.5.02.O6 - Feature: Toppings
toppingsprijs = 0


def toppings():
    global toppingen, toppingsprijs
    toppingen = geforceerde_input(
        f'{gebruiksersnaam}, wat voor topping wilt u? \nA) Geen \nB) Slagroom \nC) Sprinkels \nD) Caramel Saus : ',
        ['a', 'b', 'c', 'd'])  # wordt gevraagd naar elke topping
    if toppingen == "a":
        print("u heeft voor geen topping gekozen")
    elif toppingen == "b":
        print("u heeft voor slagroom gekozen")
        toppingsprijs += 0.50
    elif toppingen == "c":
        print("u heeft voor sprinkels gekozen")
        toppingsprijs += (float(aantalbolletje * 0.3))
    elif toppingen == "d":
        print("u heeft voor Caramel Saus gekozen")
        if kieshouders == "bakje":
            toppingsprijs += 0.90
        elif kieshouders == "hoorntje":
            toppingsprijs += 0.60


# F1.5.02.O5 - Feature: Een bonnetje
aantalbolletje = 0  # variabelen bon
aantalBolletjesOptel = 0
aantalbakjes = 0
aantalhorrentjes = 0
litersprijs = 9.80

def einde():  # hier wordt de klant door het eindproces geleid
    global aantalBolletjesOptel
    nogDoor = geforceerde_input(
        f'Hier is uw {kieshouders} met {aantalbolletje} bolletje(s). Wilt u nog meer bestellen? (Y/N) : ',
        ['n', 'y'])  # wordt gevraagd of de klant nog meer ijsjes wilt bestellen

    if nogDoor == 'n':  # matige keus maar we kunnen ze niet verplichten

        # Programma klaar
        bonnetjeparticulier()
        print('Bedankt en tot ziens!!!')
        time.sleep(15)
    else:
        # Naar begin
        aantalBolletjesOptel += aantalbolletje
        programmaopleveren()


programmaopleveren()


