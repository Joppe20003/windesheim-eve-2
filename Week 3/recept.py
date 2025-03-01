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
        oudeAantal = self.__aantalPersonen

        self.__aantalPersonen = aantal

        nieuweAantal = self.__aantalPersonen

        for ingredient in self.__ingredientenLijst:
            oudeHoeveelheid = ingredient.getHoeveelheid()

            ingredient.setHoeveelheid(oudeHoeveelheid / oudeAantal * nieuweAantal)

        self.__aantalPersonen = aantal

    def getAantalPersonen(self):
        return self.__aantalPersonen
    
    def setPlantAardigRecept(self, plantaardig):
        nieuweLijst = []

        for ingredient in self.__ingredientenLijst:
            if plantaardig:
                # Controleer of er een plantaardig alternatief is
                alternatief = ingredient.getIngredient(True)
                
                if alternatief is not None:
                    # Pas de hoeveelheid van het plantaardige alternatief aan op basis van aantal personen
                    alternatief.setHoeveelheid(alternatief.getHoeveelheid() * self.__aantalPersonen)
                    nieuweLijst.append(alternatief)
            else:
                # Voeg het originele ingrediënt toe als plantaardig niet gewenst is
                alternatief = ingredient.getIngredient(False)
                nieuweLijst.append(alternatief)

        # Werk de ingredientenlijst bij met de nieuwe lijst van ingrediënten
        self.__ingredientenLijst = nieuweLijst
                    

    def __str__(self):
        stappen = "\n".join(f"{index + 1}. {stap}" for index, stap in enumerate(self.__stappenLijst))
        ingredienten = "\n".join(f"{ingredient}" for ingredient in self.__ingredientenLijst)
        
        return (f"Naam: {self.__naam}\n"
                f"Beschrijving: {self.__omschrijving}\n"
                f"Stappen:\n{stappen}\n"
                f"Ingredienten:\n{ingredienten}")