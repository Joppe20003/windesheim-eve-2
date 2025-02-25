from ingredient import Ingredient
from stap import Stap
from recept import Recept

def laadGerecht(gerecht, ingredientenLijst):
    print("\n")
    print("---Recept---")
    print(gerecht)
    print("Ingredienten:")
    
    for ingredient in ingredientenLijst:
        print(ingredient)

def laadAantalPersonen(gerecht):
    try:
        aantalPersonen = int(input("Aantal mensen: "))
        gerecht.setAantalPersonen(aantalPersonen)

        laadStappen(gerecht)
    except ValueError:
        print("Foutieve invoer")
        laadAantalPersonen(gerecht)

def laadStappen(gerecht):
    plantAardig = input("Plantaardig gewenst?: (Ja / Nee) ")
    ingredientenLijst = None

    if plantAardig == "Ja":
        ingredientenLijst = gerecht.setPlantAardigRecept(True)
        laadGerecht(gerecht, ingredientenLijst)
        return

    if plantAardig == "Nee":
        ingredientenLijst = gerecht.setPlantAardigRecept(False)
        laadGerecht(gerecht, ingredientenLijst)
        return
    
    if plantAardig != "Nee" or plantAardig != "Ja":
        print("Foutieve invoer")
        laadStappen(gerecht)
        return

def laadKeuze(gerechten):
    print("--- Beschikbare recepten ---")

    for index in range(len(gerechten)):
        print(f"{index + 1}. {gerechten[0].getNaam()}")

    keuzeIndex = int(input("Kies een nummer: ")) - 1

    if keuzeIndex < 0 or keuzeIndex > len(gerechten):
        print('Ongeldige keuze')

        laadKeuze(gerechten)
    else:
        laadAantalPersonen(gerechten[keuzeIndex])

def main():
    gerechtenLijst = []

    recept1 = Recept("Recept 1","Dit is een omschrijving van gerecht 1")
    stappen1 = [Stap('Stap 1'), Stap('Stap 2', 'Tip 1')]
    ingredient1_1 = Ingredient("graan", 150.5, "gram", 75)
    ingredient1_1.setPlantaardigAlternatief(Ingredient("havergraan", 50, "gram", 25))
    ingredient1_2 = Ingredient("melk", 1, "liter", 120.5)
    ingredient1_2.setPlantaardigAlternatief(Ingredient("havermelk", 100, "gram", 35))
    ingredienten1 = [ingredient1_1, ingredient1_2]

    for ingredient in ingredienten1:
        recept1.voegIngredientenToe(ingredient)
        
    for stap in stappen1:
        recept1.voegStappenToe(stap)

    gerechtenLijst.append(recept1)

    laadKeuze(gerechtenLijst)

main()