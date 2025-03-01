from ingredient import Ingredient
from stap import Stap
from recept import Recept

class Main:
    def __init__(self):
        self.gerechtenLijst = []

        recept1 = Recept("Recept 1","Dit is een omschrijving van gerecht 1")
        stappen1 = [Stap('Stap 1'), Stap('Stap 2', 'Tip 1')]
        ingredient1_1 = Ingredient("graan", 150.5, "gram", 75)
        ingredient1_1.setPlantaardigAlternatief(Ingredient("havergraan", 50, "gram", 25))
        ingredient1_2 = Ingredient("melk", 1, "liter", 120.5)
        #ingredient1_2.setPlantaardigAlternatief(Ingredient("havermelk", 100, "gram", 35))
        ingredienten1 = [ingredient1_1, ingredient1_2]

        for ingredient in ingredienten1:
            recept1.voegIngredientenToe(ingredient)
            
        for stap in stappen1:
            recept1.voegStappenToe(stap)

        self.gerechtenLijst.append(recept1)

    def laadGerecht(self, gerecht, index):
        print("\n")
        print("--- Recept ---")
        print(gerecht)

        print("\n")
        print('--- Verwijder het recept ---')
        print('1. Ja')
        print('2. Nee, terug naar home')

        self.laadVerwijderOfHomeKeuze(index)

    def laadVerwijderOfHomeKeuze(self, index):
        try:
            keuze = int(input("Typ cijfer van u keuze: "))

            if keuze == 1:
                self.verwijder(index)
            elif keuze == 2:
                self.laadBeginKeuzeScherm()
            else:
                print('Ongeldige keuze')

        except ValueError:
            print("Foutieve invoer")

            self.laadVerwijderOfHomeKeuze(index)

    def verwijder(self, index):
        print("\n")
        print("--- Bevestiging ---")
        keuze = input("Weet je zeker je wilt verwijderen? Type dan Ja, anders Nee: ").strip()

        if keuze.upper() == "JA":
            self.gerechtenLijst.pop(index)

            self.laadBeginKeuzeScherm()
        elif keuze.upper() == "NEE":
            self.laadBeginKeuzeScherm()
        else:
            print("Foutieve invoer")
            self.verwijder(index)

    def laadAantalPersonen(self, gerecht, index):
        try:
            aantalPersonen = int(input("Aantal mensen: "))
            gerecht.setAantalPersonen(aantalPersonen)

            self.laadStappen(gerecht, index)
        except ValueError:
            print("Foutieve invoer")

            self.laadAantalPersonen(gerecht, index)

    def laadStappen(self, gerecht, index):
        plantAardig = input("Plantaardig gewenst?: (Ja / Nee) ")

        if plantAardig.upper() == "JA":
            gerecht.setPlantAardigRecept(True)

            self.laadGerecht(gerecht, index)
            return

        if plantAardig.upper() == "NEE":
            gerecht.setPlantAardigRecept(False)

            self.laadGerecht(gerecht, index)
            return
        
        if plantAardig.upper() != "NEE" or plantAardig.upper() != "JA":
            print("Foutieve invoer")
            self.laadStappen(gerecht, index)
            return

    def laadOverizcht(self):
        print("\n")
        print("--- Beschikbare recepten ---")

        if len(self.gerechtenLijst) > 0:
            for index in range(len(self.gerechtenLijst)):
                print(f"{index + 1}. {self.gerechtenLijst[index].getNaam()}")
        else:
            print('Geen gerechten nog beschikbaar!')

        keuzeIndex = int(input("Kies een nummer: ")) - 1

        if keuzeIndex < 0 or keuzeIndex > len(self.gerechtenLijst):
            print('Ongeldige keuze')

            self.laadOverizcht()
        else:
            self.laadAantalPersonen(self.gerechtenLijst[keuzeIndex], keuzeIndex)

    def laadBeginKeuzeScherm(self):
        print("\n")
        print("--- Menu ---")
        print("1. Overzicht")
        print("2. Toevoegen")
        print("3. Exit")

        try:
            keuze = int(input("Typ cijfer van u keuze: "))

            if keuze == 1:
                self.laadOverizcht()
            elif keuze == 2:
                self.toevoegen()
            elif keuze == 3:
                self.exit()
            else:
                print("Foutieve invoer")

                self.laadBeginKeuzeScherm()

        except ValueError:
            print("Foutieve invoer")

            self.laadBeginKeuzeScherm()

    def toevoegen(self):
        print("\n")
        print("--- Toevoeging ---")

        naam = input("Naam: ")
        beschrijving = input("Beschrijving: ")

        nieuw_recept = Recept(naam, beschrijving)

        ingredienten_lijst = []
        stappen_lijst = []

        ingredient_condition = True
        stappen_condition = True
        
        print("\n")
        print("Ingredienten:")

        while(ingredient_condition):
            ingredient_naam = input("Naam: ")
            ingredient_hoeveelheid = float(input("Hoeveelheid: "))
            ingredient_eenheid = input("Eenheid: ")
            ingredient_kcal = float(input("KCAL: "))

            ingredient = Ingredient(ingredient_naam, ingredient_hoeveelheid, ingredient_eenheid, ingredient_kcal)

            print(f"{ingredient_naam} is toegevoegd als ingredient voor het recept {naam}")

            keuze = input(f"Wilt u plantaardig variant voor {ingredient_naam} opgeven?, Type ja om door te gaan als je dat niet wil druk op enter: ")

            if keuze.upper() == "JA":
                plantaardig_naam = input("Naam: ")
                plantaardig_hoeveelheid = float(input("Hoeveelheid: "))
                plantaardig_eenheid = input("Eenheid: ")
                plantaardig_kcal = float(input("KCAL: "))

                ingredient.setPlantaardigAlternatief(Ingredient(plantaardig_naam, plantaardig_hoeveelheid, plantaardig_eenheid, plantaardig_kcal))
                
                print(f"{plantaardig_naam} is toegevoegd als plantaardig alternatief voor {ingredient_naam} in het recept {naam}")

            ingredienten_lijst.append(ingredient)

            keuze_stoppen = input("Typ stop om te stoppen met het toevoegen van ingredienten: ")

            if keuze_stoppen.upper() == "STOP":
                ingredient_condition = False
        
        print("\n")
        print("Stappen:")
        
        while(stappen_condition):
            stap = input("Stap: ")

            print(f"{stap} is toegevoegd als stap voor het recept {naam}")

            keuze = input("Wilt u een tip toevoegen aan de stap?, Typ dan ja als je niet wil druk op enter: ")

            if keuze.upper() == "JA":
                invoer = input("Tip: ")

                stap_object = Stap(stap, invoer)
            else:
                stap_object = Stap(stap)

            stappen_lijst.append(stap_object)
            
            keuze_stoppen = input("Typ stop om te stoppen met het toevoegen van ingredienten: ")

            if keuze_stoppen.upper() == "STOP":
                stappen_condition = False
        
        for ingredient in ingredienten_lijst:
            nieuw_recept.voegIngredientenToe(ingredient)
        
        for stap in stappen_lijst:
            nieuw_recept.voegStappenToe(stap)

        self.gerechtenLijst.append(nieuw_recept)

        print(f"{naam} is toegevoegd.")

        self.laadBeginKeuzeScherm()


    def exit(self):
        print("\n")
        print("Programma gestopt!")
        exit()

    def main(self):
        self.laadBeginKeuzeScherm()

if __name__ == "__main__":
    main = Main()
    main.main()
