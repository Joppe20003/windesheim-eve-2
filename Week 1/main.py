from ingredient import Ingredient
from stap import Stap
from recept import Recept

def laadGerecht(gerecht):
    print(gerecht)

def laadKeuze(gerechten):
    print("--- Beschikbare recepten ---")

    for index in range(len(gerechten)):
        print(f"{index + 1}. {gerechten[0].getNaam()}")

    keuzeIndex = int(input("Kies een nummer: ")) - 1

    if keuzeIndex < 0 or keuzeIndex > len(gerechten):
        print('Ongeldige keuze')
        print("\n")

        laadKeuze(gerechten)
    else:
        print("\n")
        laadGerecht(gerechten[keuzeIndex])
    


def main():
    gerechtenLijst = []

    recept1 = Recept("Recept 1","Dit is een omschrijving van gerecht 1")
    ingredienten1 = [Ingredient("graan", 150.5, "gram"), Ingredient("melk", 1, "liter")]
    stappen1 = [Stap("stap 1"), Stap("stap 2")]

    for ingredient in ingredienten1:
        recept1.voegIngredientenToe(ingredient)
        
    for stap in stappen1:
        recept1.voegStappenToe(stap)

    gerechtenLijst.append(recept1)

    laadKeuze(gerechtenLijst)

main()