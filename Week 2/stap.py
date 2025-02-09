class Stap:
    def __init__(self, beschrijving, tip = None):
        self.__beschrijving = beschrijving
        self.__tip = tip

    def __str__(self):
        return f"{self.__beschrijving}{', ' + "tip: " + self.__tip if self.__tip != None else ""}"