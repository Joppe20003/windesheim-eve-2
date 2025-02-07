class Recept:
    def __init__(self, naam, omschrijving):
        self.__naam = naam
        self.__omschrijving = omschrijving
        self.__ingredientenLijst = []
        self.__stappenLijst = []

    def voegIngredientenToe(self, ingredient):
        self.__ingredientenLijst.append(ingredient)

    def voegStappenToe(self, stap):
        self.__stappenLijst.append(stap)

    def getNaam(self):
        return self.__naam
    
    def getOmschrijving(self):
        return self.__omschrijving

    def __str__(self):
        ingredienten = "\n".join(f"* {ingredient}" for ingredient in self.__ingredientenLijst)
        stappen = "\n".join(f"{index + 1}. {stap}" for index, stap in enumerate(self.__stappenLijst))
        
        return (f"Naam: {self.__naam}\n"
                f"Beschrijving: {self.__omschrijving}\n"
                f"Ingrediënten:\n{ingredienten}\n"
                f"Stappen:\n{stappen}")