from ingredient import Ingredient
from stap import Stap
from recept import Recept

def laadGerecht(gerecht):
    print(gerecht)

def laadKeuze(gerechten):
    print("--- Beschikbare recepten ---")

    for index in range(len(gerechten)):
        print(f"{index + 1}. {gerechten[index].getNaam()}")

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

    # Recept 1: Pannenkoeken
    recept1 = Recept("Pannenkoeken", "Lekkere, eenvoudige pannenkoeken.")
    stappen1 = [
        Stap('Meng de bloem en melk in een kom tot een glad beslag'),
        Stap('Voeg het ei toe en klop het geheel goed door'),
        Stap('Verhit een beetje boter of olie in een pan op middelhoog vuur'),
        Stap('Giet een kleine hoeveelheid beslag in de pan en draai de pan rond om het beslag gelijkmatig te verdelen'),
        Stap('Bak de pannenkoek ongeveer 2 minuten tot de randen loslaten en de onderkant goudbruin is'),
        Stap('Draai de pannenkoek om en bak nog 1-2 minuten aan de andere kant'),
        Stap('Haal de pannenkoek uit de pan en herhaal het proces met de rest van het beslag')
    ]
    ingredient1_1 = Ingredient("bloem", 100, "gram")
    ingredient1_2 = Ingredient("melk", 250, "ml")
    ingredient1_3 = Ingredient("ei", 1, "stuk")
    ingredienten1 = [ingredient1_1, ingredient1_2, ingredient1_3]
        
    for ingredient in ingredienten1:
        recept1.voegIngredientenToe(ingredient)
    for stap in stappen1:
        recept1.voegStappenToe(stap)
    
    gerechtenLijst.append(recept1)

    # Recept 2: Tomatensoep
    recept2 = Recept("Tomatensoep", "Verse, romige tomatensoep.")
    stappen2 = [
        Stap('Snijd de tomaten en ui in kleine stukken'),
        Stap('Verhit een beetje olie in een pan en fruit de ui en knoflook tot ze glazig zijn'),
        Stap('Voeg de tomaten en bouillon toe, breng aan de kook en laat 15 minuten sudderen'),
        Stap('Pureer de soep met een staafmixer tot een glad geheel'),
        Stap('Proef en breng eventueel op smaak met peper en zout'),
        Stap('Serveer de soep warm met een beetje verse basilicum of een scheutje plantaardige room')
    ]
    ingredient2_1 = Ingredient("tomaten", 250, "gram")
    ingredient2_2 = Ingredient("ui", 0.5, "stuk")
    ingredient2_3 = Ingredient("bouillon", 250, "ml")
    ingredient2_4 = Ingredient("knoflook", 0.5, "teen")
    ingredienten2 = [ingredient2_1, ingredient2_2, ingredient2_3, ingredient2_4]
        
    for ingredient in ingredienten2:
        recept2.voegIngredientenToe(ingredient)
    for stap in stappen2:
        recept2.voegStappenToe(stap)
    
    gerechtenLijst.append(recept2)

    # Recept 3: Omelet
    recept3 = Recept("Omelet", "Eenvoudige, luchtige omelet.")
    stappen3 = [
        Stap('Klop het ei los met melk in een kom'),
        Stap('Voeg zout en peper toe en klop nogmaals goed door'),
        Stap('Verhit een beetje boter of olie in een pan op middelhoog vuur'),
        Stap('Giet het eimengsel in de pan en laat het rustig stollen'),
        Stap('Gebruik een spatel om de randen voorzichtig los te maken en vouw de omelet dubbel'),
        Stap('Bak nog 1 minuut en haal de omelet uit de pan'),
        Stap('Serveer direct en geniet')
    ]
    ingredient3_1 = Ingredient("ei", 1, "stuk")
    ingredient3_2 = Ingredient("melk", 25, "ml")
    ingredient3_3 = Ingredient("zout", 1, "snufje")
    ingredient3_4 = Ingredient("peper", 1, "snufje")
    ingredienten3 = [ingredient3_1, ingredient3_2, ingredient3_3, ingredient3_4]
        
    for ingredient in ingredienten3:
        recept3.voegIngredientenToe(ingredient)
    for stap in stappen3:
        recept3.voegStappenToe(stap)
    
    gerechtenLijst.append(recept3)

    laadKeuze(gerechtenLijst)

main()