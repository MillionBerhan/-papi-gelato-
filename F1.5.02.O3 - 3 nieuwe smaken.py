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

def geforceerde_input(vraag: str, toegestaan: list[str], niet_goed_bericht: str = 'Sorry, dat begreep ik niet.') -> str:
    while not ((antwoord := input(vraag).lower()) in toegestaan):
        print(niet_goed_bericht)

    return antwoord