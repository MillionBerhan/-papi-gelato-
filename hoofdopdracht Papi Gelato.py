# Aantal bolletjes (-1 voor niks)
aantalbolletje = None

# Vorm - Bakje/Hoorntje
kieshouders = None

print('Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.')
gebruiksersnaam = input('Wat is uw naam?')


def geforceerde_input(vraag: str, toegestaan: list[str], niet_goed_bericht: str = 'Sorry, dat begreep ik niet.') -> str:
    while not ((antwoord := input(vraag).lower()) in toegestaan):
        print(niet_goed_bericht)

    return antwoord


def programmaopleveren():
    global aantalbolletje, kieshouders
    aantalbolletje = int(
        geforceerde_input(f'{gebruiksersnaam}, hoeveel bolletjes wilt u?', [str(i) for i in range(1, 8)]))

    if aantalbolletje < 4:

        # Gebruiker moet kiezen voor een hoorntje of een bakje
        keuzesoorthouder()
    else:

        # Alleen hoorntjes voor minder dan 4 bolletjes
        kieshouders = 'bakje'

        # Vragen of de gebruiker meer wilt
        einde()


def keuzesoorthouder():
    global kieshouders
    kieshouders = geforceerde_input(
        f'{gebruiksersnaam}, wilt u deze {aantalbolletje} bolletje(s) in\n|hoorntje\n|bakje',
        ['hoorntje', 'bakje'])

    # Vragen of de gebruiker meer wilt
    einde()


def einde():
    nogDoor = geforceerde_input(
        f'Hier is uw {kieshouders} met {aantalbolletje} bolletje(s). Wilt u nog meer bestellen? (Y/N)', ['n', 'y'])

    if nogDoor == 'n':

        # Programma klaar
        print('Bedankt en tot ziens!!!')
    else:

        # Naar begin
        programmaopleveren()


if __name__ == '__main__':
    programmaopleveren()