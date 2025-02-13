class Recept:
    def __init__(self, naam, omschrijving):
        self.__naam = naam
        self.__omschrijving = omschrijving
        self.__ingredientenLijst = []
        self.__stappenLijst = []
        self.__aantalPersonen = 1

    def voegIngredientenToe(self, ingredient):
        self.__ingredientenLijst.append(ingredient)

    def voegStappenToe(self, stap):
        self.__stappenLijst.append(stap)

    def getNaam(self):
        return self.__naam
    
    def getOmschrijving(self):
        return self.__omschrijving
    
    def setAantalPersonen(self, aantal):
        self.__aantalPersonen = aantal

        for ingredient in self.__ingredientenLijst:
            ingredient.setHoeveelheid(aantal)

    def getAantalPersonen(self):
        return self.__aantalPersonen
    
    def setPlantAardigRecept(self, plantaardig):
        plantAardigIngredientenLijst = []
        nietPlantAardigIngredientenLijst = []

        for ingredient in self.__ingredientenLijst:
            if plantaardig:
                alternatief = ingredient.getIngredient(True)
                alternatief.setHoeveelheid(self.__aantalPersonen)

                plantAardigIngredientenLijst.append(alternatief)
            else:
                nietPlantAardigIngredientenLijst.append(ingredient.getIngredient(False))

        if plantaardig:
            return plantAardigIngredientenLijst
        return nietPlantAardigIngredientenLijst

    def __str__(self):
        stappen = "\n".join(f"{index + 1}. {stap}" for index, stap in enumerate(self.__stappenLijst))
        
        return (f"Naam: {self.__naam}\n"
                f"Beschrijving: {self.__omschrijving}\n"
                f"Stappen:\n{stappen}")