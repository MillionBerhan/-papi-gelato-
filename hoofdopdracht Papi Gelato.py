from datetime import datetime, timedelta

ditjaar = datetime.now().year
xmasditjaar = datetime( ditjaar, 12, 25, 23, 59, 59 )
dezedag = datetime.now()
dagen = xmasditjaar - dezedag


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


def programmaopleveren():
    global aantalbolletje, kieshouders
    aantalbolletje = int(geforceerde_input(f'{gebruiksersnaam}, hoeveel bolletjes wilt u?', [str(i) for i in range(1, 8)])) # hier wordt gevraagd hoeveel bolletjes de klant wilt 

    if aantalbolletje < 4:
        # Gebruiker moet kiezen voor een hoorntje of een bakje
        keuzesoorthouder()
        smaakjeskiezen()
        bonnetje()
        einde()
    else:
        # Alleen hoorntjes voor minder dan 4 bolletjes
        kieshouders = 'bakje'
        smaakjeskiezen()
        # Vragen of de gebruiker meer wilt
        bonnetje()
        einde()

#F1.5.02.O3 - 3 nieuwe smakenFuncties
def smaakjeskiezen():
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

aantalbakjes = 0
aantalhorrentjes = 0

def keuzesoorthouder(): # in deze functie kun je kiezen tussen bolletje(s) in een bakje of in een hoorntje
    global kieshouders,aantalbakjes,aantalhorrentjes
    kieshouders = geforceerde_input(f'{gebruiksersnaam}, wilt u deze {aantalbolletje} bolletje(s) in\n|hoorntje\n|bakje',
        ['hoorntje', 'bakje'])
    if kieshouders == "bakje": 
        aantalbakjes +=1
    else: 
        aantalhorrentjes +=1

#F1.5.02.O5 - Feature: Een bonnetje

def bonnetje():# hier worden de prijzen van de klanten berekend van zijn/haar bestelliung
    print ("--------------------------Papi Gelato--------------------------")
    if kieshouders == "bakje":
        print (f"bakje(s):    {float(aantalbakjes*0.75)}") # hier wordt de prijs van de aantal bolletjes berekend in deze functie
        print (f" bolletje(s):{float(aantalbolletje*1.10)} ")
        print ("totaalprijs:----------------------------------------=")
        print (f"             {float(0.75*aantalbakjes+aantalbolletje*1.10)}")
    else:
        print (f"horrentjes   {float(aantalhorrentjes*1.25)}")# hier wordt de prijs van de horrentjes berekend in deze functie
        print (f"bolletje(s)  {float(aantalbolletje*1.10)}")
        print ("totaalprijs:----------------------------------------=")
        print (f"             {float(aantalhorrentjes*1.25 + aantalbolletje*1.10)}")
        print (f"----------------------{dezedag}-------------------------") # datum en tijdstip van deze bestelling

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

