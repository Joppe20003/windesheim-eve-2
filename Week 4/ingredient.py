class Ingredient:
    def __init__(self, naam, hoeveelheid, eenheid, kcal):
        self.__naam = naam
        self.__hoeveelheid = hoeveelheid
        self.__eenheid = eenheid
        self.__kcal = kcal
        self.__plantaardigAlternatief = None

    def setHoeveelheid(self, hoeveelheid):
        self.__hoeveelheid =  hoeveelheid
        self.__kcal = hoeveelheid

    def getHoeveelheid(self):
        return self.__hoeveelheid
    
    def getKcal(self):
        return self.__kcal
    
    def setPlantaardigAlternatief(self, alternatief):
        self.__plantaardigAlternatief = alternatief

    def getIngredient(self, plantaardig):
        if plantaardig:
            return self.__plantaardigAlternatief
        return self

    def __str__(self):
        return f"* {self.__hoeveelheid} {self.__eenheid} {self.__naam}"