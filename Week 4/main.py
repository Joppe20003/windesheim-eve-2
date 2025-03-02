from ingredient import Ingredient
from stap import Stap
from recept import Recept
from pdfCreator import PdfCreator
import os

class Main:
    def __init__(self):
        self.pdfCreator = PdfCreator()
        self.gerechtenLijst = []
        self.index = None

        # Recept 1: Pannenkoeken
        recept1 = Recept("Pannenkoeken", "Lekkere, eenvoudige pannenkoeken.")
        stappen1 = [
            Stap('Meng de bloem en melk in een kom tot een glad beslag'),
            Stap('Voeg het ei toe en klop het geheel goed door', 'Gebruik een plantaardig ei-alternatief zoals lijnzaad of banaan voor een vegan optie'),
            Stap('Verhit een beetje boter of olie in een pan op middelhoog vuur'),
            Stap('Giet een kleine hoeveelheid beslag in de pan en draai de pan rond om het beslag gelijkmatig te verdelen'),
            Stap('Bak de pannenkoek ongeveer 2 minuten tot de randen loslaten en de onderkant goudbruin is', 'Gebruik een spatel om de randen los te maken voordat je draait'),
            Stap('Draai de pannenkoek om en bak nog 1-2 minuten aan de andere kant'),
            Stap('Haal de pannenkoek uit de pan en herhaal het proces met de rest van het beslag')
        ]
        ingredient1_1 = Ingredient("bloem", 100, "gram", 50)
        ingredient1_2 = Ingredient("melk", 250, "ml", 125)
        ingredient1_2.setPlantaardigAlternatief(Ingredient("havermelk", 250, "ml", 90))
        ingredient1_3 = Ingredient("ei", 1, "stuk", 70)
        ingredient1_3.setPlantaardigAlternatief(Ingredient("lijnzaad-ei", 1, "stuk", 25))
        ingredienten1 = [ingredient1_1, ingredient1_2, ingredient1_3]
        
        for ingredient in ingredienten1:
            recept1.voegIngredientenToe(ingredient)
        for stap in stappen1:
            recept1.voegStappenToe(stap)
        self.gerechtenLijst.append(recept1)

        # Recept 2: Tomatensoep
        recept2 = Recept("Tomatensoep", "Verse, romige tomatensoep.")
        stappen2 = [
            Stap('Snijd de tomaten en ui in kleine stukken'),
            Stap('Verhit een beetje olie in een pan en fruit de ui en knoflook tot ze glazig zijn', 'Voeg een snufje zout toe om de ui sneller te laten zweten'),
            Stap('Voeg de tomaten en bouillon toe, breng aan de kook en laat 15 minuten sudderen'),
            Stap('Pureer de soep met een staafmixer tot een glad geheel'),
            Stap('Proef en breng eventueel op smaak met peper en zout'),
            Stap('Serveer de soep warm met een beetje verse basilicum of een scheutje plantaardige room')
        ]
        ingredient2_1 = Ingredient("tomaten", 250, "gram", 45)
        ingredient2_2 = Ingredient("ui", 0.5, "stuk", 20)
        ingredient2_3 = Ingredient("bouillon", 250, "ml", 10)
        ingredient2_3.setPlantaardigAlternatief(Ingredient("groentebouillon", 250, "ml", 7))
        ingredient2_4 = Ingredient("knoflook", 0.5, "teen", 3)
        ingredienten2 = [ingredient2_1, ingredient2_2, ingredient2_3, ingredient2_4]
        
        for ingredient in ingredienten2:
            recept2.voegIngredientenToe(ingredient)
        for stap in stappen2:
            recept2.voegStappenToe(stap)
        self.gerechtenLijst.append(recept2)

        # Recept 3: Omelet
        recept3 = Recept("Omelet", "Eenvoudige, luchtige omelet.")
        stappen3 = [
            Stap('Klop het ei los met melk in een kom', 'Gebruik kikkererwtenmeel met water als plantaardig alternatief voor ei'),
            Stap('Voeg zout en peper toe en klop nogmaals goed door'),
            Stap('Verhit een beetje boter of olie in een pan op middelhoog vuur'),
            Stap('Giet het eimengsel in de pan en laat het rustig stollen'),
            Stap('Gebruik een spatel om de randen voorzichtig los te maken en vouw de omelet dubbel', 'Schud de pan lichtjes om te voorkomen dat de omelet blijft plakken'),
            Stap('Bak nog 1 minuut en haal de omelet uit de pan'),
            Stap('Serveer direct en geniet')
        ]
        ingredient3_1 = Ingredient("ei", 1, "stuk", 70)
        ingredient3_1.setPlantaardigAlternatief(Ingredient("kikkererwtenmeel", 50, "gram", 75))
        ingredient3_2 = Ingredient("melk", 25, "ml", 15)
        ingredient3_2.setPlantaardigAlternatief(Ingredient("havermelk", 25, "ml", 12))
        ingredient3_3 = Ingredient("zout", 1, "snufje", 1)
        ingredient3_4 = Ingredient("peper", 1, "snufje", 1)
        ingredienten3 = [ingredient3_1, ingredient3_2, ingredient3_3, ingredient3_4]
        
        for ingredient in ingredienten3:
            recept3.voegIngredientenToe(ingredient)
        for stap in stappen3:
            recept3.voegStappenToe(stap)
        self.gerechtenLijst.append(recept3)

    def laadGerecht(self):
        self.pdfCreator.maakPDF(self.gerechtenLijst[self.index])

        print("\n")
        print("--- Recept ---")
        print(self.gerechtenLijst[self.index])

        print("\n")
        print(f'Het is in een PDF voor u gezet!, Op de locatie: {os.getcwdb()}')

        print("\n")
        print('--- Verwijder het recept ---')
        print('1. Ja')
        print('2. Nee, terug naar home')

        self.laadVerwijderOfHomeKeuze()

    def laadVerwijderOfHomeKeuze(self):
        try:
            keuze = int(input("Typ cijfer van u keuze: "))

            if keuze == 1:
                self.verwijder()
            elif keuze == 2:
                self.laadBeginKeuzeScherm()
            else:
                print('Foutieve keuze')
                
                self.laadVerwijderOfHomeKeuze()

        except ValueError:
            print("Foutieve invoer")

            self.laadVerwijderOfHomeKeuze()

    def verwijder(self):
        print("\n")
        print("--- Bevestiging ---")
        keuze = input("Weet je zeker je wilt verwijderen? Type dan Ja, anders Nee: ").strip()

        if keuze.upper() == "JA":
            self.gerechtenLijst.pop(self.index)

            self.laadBeginKeuzeScherm()
        elif keuze.upper() == "NEE":
            self.laadBeginKeuzeScherm()
        else:
            print("Foutieve invoer")
            self.verwijder()

    def laadAantalPersonen(self):
        gerecht = self.gerechtenLijst[self.index]

        try:
            aantalPersonen = int(input("Aantal mensen: "))
            gerecht.setAantalPersonen(aantalPersonen)

            self.laadStappen()
        except ValueError:
            print("Foutieve invoer")

            self.laadAantalPersonen()

    def laadStappen(self):
        plantAardig = input("Plantaardig gewenst?: (Ja / Nee) ")
        gerecht = self.gerechtenLijst[self.index]

        if plantAardig.upper() == "JA":
            gerecht.setPlantAardigRecept(True)

            self.laadGerecht()
            return

        if plantAardig.upper() == "NEE":
            gerecht.setPlantAardigRecept(False)

            self.laadGerecht()
            return
        
        if plantAardig.upper() != "NEE" or plantAardig.upper() != "JA":
            print("Foutieve invoer")
            self.laadStappen()
            return

    def laadOverizcht(self):
        print("\n")
        print("--- Beschikbare recepten ---")

        if len(self.gerechtenLijst) > 0:
            for index in range(len(self.gerechtenLijst)):
                print(f"{index + 1}. {self.gerechtenLijst[index].getNaam()}")
        else:
            print('Geen gerechten nog beschikbaar!')

        index = int(input("Kies een nummer: ")) - 1

        if index < 0 or index > len(self.gerechtenLijst):
            print('Foutieve keuze')

            self.laadOverizcht()
        else:
            self.index = index

            self.laadAantalPersonen()

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

            keuze = input(f"Wilt u plantaardig variant voor {ingredient_naam} opgeven?: (Ja / Nee) ")

            if keuze.upper() == "JA":
                plantaardig_naam = input("Naam: ")
                plantaardig_hoeveelheid = float(input("Hoeveelheid: "))
                plantaardig_eenheid = input("Eenheid: ")
                plantaardig_kcal = float(input("KCAL: "))

                ingredient.setPlantaardigAlternatief(Ingredient(plantaardig_naam, plantaardig_hoeveelheid, plantaardig_eenheid, plantaardig_kcal))


            ingredienten_lijst.append(ingredient)

            keuze_stoppen = input("Wilt u nog een ingredient toevoegen?: (Ja / Nee) ")

            if keuze_stoppen.upper() == "NEE":
                ingredient_condition = False
        
        print("\n")
        print("Stappen:")
        
        while(stappen_condition):
            stap = input("Stap: ")

            keuze = input("Wilt u een tip toevoegen aan de stap?: (Ja / Nee) ")

            if keuze.upper() == "JA":
                invoer = input("Tip: ")

                stap_object = Stap(stap, invoer)
            else:
                stap_object = Stap(stap)

            stappen_lijst.append(stap_object)
            
            keuze_stoppen = input("wilt u nog een stap toevoegen?: (Ja / Nee) ")

            if keuze_stoppen.upper() == "NEE":
                stappen_condition = False
        
        for ingredient in ingredienten_lijst:
            nieuw_recept.voegIngredientenToe(ingredient)
        
        for stap in stappen_lijst:
            nieuw_recept.voegStappenToe(stap)

        self.gerechtenLijst.append(nieuw_recept)

        self.laadGerecht(len(self.gerechtenLijst) - 1)

    def exit(self):
        print("\n")
        print("Programma gestopt!")
        exit()

    def main(self):
        self.laadBeginKeuzeScherm()

if __name__ == "__main__":
    main = Main()
    main.main()
