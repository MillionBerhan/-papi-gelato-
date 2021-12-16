from datetime import datetime, timedelta

ditjaar = datetime.now().year
xmasditjaar = datetime( ditjaar, 12, 25, 23, 59, 59 )
dezedag = datetime.now()
dagen = xmasditjaar - dezedag

w = 0
aantalliter = 0
aantalbolletje = 0
aantalbakjes = 0
aantalhorrentjes = 0
programmaopleveren= 0

if dagen.days < 0:
    print( "Kerst komt volgend jaar weer." )
elif dagen.days == 0:
    print( "Het is Kerst!" )
else:
    print( "Slechts", dagen.days, "dagen tot Kerst!" )


# Aantal bolletjes (-1 voor niks)
aantalbolletje = None

# Vorm - Bakje/Hoorntje
kieshouders = None

print('Welkom bij Papi Gelato')
gebruiksersnaam = input('Wat is uw naam?')

def geforceerde_input(vraag: str, toegestaan: list[str], niet_goed_bericht: str = 'Sorry, dat begreep ik niet.') -> str: # hier wotdt er
    while not ((antwoord := input(vraag).lower()) in toegestaan):
        print(niet_goed_bericht)

    return antwoord

#F1.5.02.O7 - Feature: Zakelijke markt bedienenFuncties

def zakelijk():
    global soortklant, aantalliter, w
    soortklant = geforceerde_input("Wat voor klant bent u? \nA) particulier \nB) zakelijk", ["a", "b"]) # hier wordt gevraagd naar het type klant
    if soortklant == "a":
        print ("U bent een particulier") # als je op  a klikt ben je een klant
    elif soortklant == "b":
        print ("u bent een zakelijke klant") # als je op b klikt ben je een zakelijke klant
        aantalliter = int(input("Hoeveel liters ijs wilt u?"))
        for z in range (aantalliter): # hier wordt een loop gebruikt
            w += 1
            kiessmaak = geforceerde_input(f"voor welke smaak wilt u voor liter  nummer {w}? \nA) Aardbei \nC) Chocolade\nM) Munt of \nV) Vanille",['a', 'c', 'm', 'v']) # smaken voor de aantal liters
        smaakjeskiezen()
        bonnetje()
        exit()

#F1.5.02.O2 - Een programma opleverenFuncties

def programmaopleveren():
    global aantalbolletje, kieshouders
    zakelijk()
    aantalbolletje = int(geforceerde_input(f'{gebruiksersnaam}, hoeveel bolletjes wilt u?', [str(i) for i in range(1, 8)])) # hier wordt gevraagd hoeveel bolletjes de klant wilt 

    if aantalbolletje < 4:
        # Gebruiker moet kiezen voor een hoorntje of een bakje
        keuzesoorthouder()
        smaakjeskiezen()
        toppings()
        bonnetje()
        einde()
    elif soortklant == "b":
        # het zakelijke process van Papi-Gelato
        smaakjeskiezen()
        bonnetje()
    else:
        # Alleen hoorntjes voor minder dan 4 bolletjes
        kieshouders = 'bakje'
        smaakjeskiezen()
        # Vragen of de gebruiker meer wilt
        toppings()
        bonnetje()
        einde()

#F1.5.02.O3 - 3 nieuwe smakenFuncties
def smaakjeskiezen():
    global kiessmaak
    for i in range(aantalbolletje):
        kiessmaak = geforceerde_input(f"Welke smaak wilt u voor bolletje nummer {i + 1}? \nA) Aardbei \nC) Chocolade\nM) Munt of \nV) Vanille",['a', 'c', 'm', 'v']) # er wordt hier gevraagd naar de smaken die de klant per bolletje wilt
        if kiessmaak == "a":
            print ("U heeft voor aardbei gekozen") #hier kiezen ze voor aardbei
        elif kiessmaak == "c":
            print ("u heeft voor chocolade gekozen") #hier kiezen ze voor choco
        elif kiessmaak == "m":
            print ("u heeft voor munt gekozen") # hier kiezen ze voor munt
        else:
            print ("U heeft voor vanille gekozen") # en tot slot voor vanille


def keuzesoorthouder(): # in deze functie kun je kiezen tussen bolletje(s) in een bakje of in een hoorntje
    global kieshouders,aantalbakjes,aantalhorrentjes
    kieshouders = geforceerde_input(f'{gebruiksersnaam}, wilt u deze {aantalbolletje} bolletje(s) in\n|hoorntje\n|bakje',
        ['hoorntje', 'bakje'])
    if kieshouders == "bakje": 
        aantalbakjes =1
    else: 
        aantalhorrentjes =1

#F1.5.02.O6 - Feature: Toppings
toppingsprijs= 0

def toppings(): 
    global toppingen,toppingsprijs
    toppingen = geforceerde_input(f'{gebruiksersnaam}, wat voor topping wilt u? \nA) Geen \nB) Slagroom \nC) Sprinkels \nD) Caramel Saus', ['a', 'b', 'c', 'd']) # wordt gevraagd naar elke topping
    if toppingen == "a":
        print ("u heeft voor geen topping gekozen")
    elif toppingen == "b":
        print ("u heeft voor slagroom gekozen")
        toppingsprijs+= 0.5
    elif toppingen == "c":
        print ("u heeft voor sprinkels gekozen")
        toppingsprijs+=(float(aantalbolletje*0.3))   
    elif toppingen == "d":
        print ("u heeft voor Caramel Saus gekozen")
        if kieshouders == "bakje":
            toppingsprijs+=0.90
        elif kieshouders == "hoorntje":
            toppingsprijs+=0.60


#F1.5.02.O5 - Feature: Een bonnetje
aantalbolletje = 0 # variabelen bon
aantalbakjes = 0
aantalhorrentjes = 0
litersprijs=9.80 


def bonnetje():# hier worden de prijzen van de klanten berekend van zijn/haar bestelling
    print ("--------------------------Papi Gelato--------------------------")
    if kieshouders == "bakje":
        print (f"bakje(s):    {float(aantalbakjes)} x {0.75} = {aantalbakjes*0.75}") # hier wordt de prijs van de aantal bolletjes berekend in deze functie
        print (f" bolletje(s):{float(aantalbolletje)} x {1.10} = {aantalbolletje*1.10}")
        print (f"toppingen: {toppingsprijs}  ")
        print ("totaalprijs:----------------------------------------=")
        print (f"             {float(aantalbakjes*0.75+aantalbolletje*1.10+toppingsprijs)}")
    elif kieshouders == "hoorntje":
        print (f"horrentjes:  {float(aantalhorrentjes)} x {1.25} = {aantalhorrentjes*1.25}")# hier wordt de prijs van de horrentjes berekend in deze functie
        print (f"bolletje(s): {float(aantalbolletje)} x {1.10} = {aantalbolletje*1.10}")
        print (f"topping: {toppingsprijs} ")
        print ("totaalprijs:----------------------------------------+=")
        print (f"             {float(aantalhorrentjes*1.25+aantalbolletje*1.10+toppingsprijs)}")
        print (f"klant:{gebruiksersnaam}")
        print ("geholpen door: Million Berhan")
        print (f"----------------------{dezedag}----------------------------") # datum en tijdstip van deze bestelling
    elif soortklant == "b":
        print (f"liters: {aantalliter} x {litersprijs}  =  {aantalliter*litersprijs} ")
        print (f" totaalprijs:                             ={aantalliter*litersprijs}")
        print (f"BTW (9%):                           {aantalliter*litersprijs/100*9} ")
        print (f"klant:{gebruiksersnaam}")
        print ("geholpen door: Million Berhan")
        print (f"----------------------{dezedag}----------------------------") # datum en tijdstip van deze bestelling

def einde(): #hier wordt de klant door het eindproces geleid
    nogDoor = geforceerde_input(
        f'Hier is uw {kieshouders} met {aantalbolletje} bolletje(s). Wilt u nog meer bestellen? (Y/N)', ['n', 'y'])

    if nogDoor == 'n':

        # Programma klaar
        print('Bedankt en tot ziens!!!')
    else:
        # Naar begin
        programmaopleveren()

programmaopleveren()


