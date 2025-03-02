from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

class PdfCreator:
    def __init__(self):
        self.BESTAND_NAAM = "Recept.pdf"
        self.RAND_AFSTAND_VERTICAAL = 40
        self.RAND_AFSTAND_HORIZONTAAL = 30
        self.W, self.H = A4
        self.canvas = canvas.Canvas(self.BESTAND_NAAM, pagesize=A4)
        self.tekst = self.canvas.beginText(self.RAND_AFSTAND_HORIZONTAAL, self.H - self.RAND_AFSTAND_VERTICAAL)

    def schrijfTekst(self, tekst, fontSize = 15, fontName = "Helvetica"):
        self.zetFont(fontSize, fontName)
        
        text_width = self.W - 2 * self.RAND_AFSTAND_HORIZONTAAL
        words = tekst.split(" ")
        current_line = ""
        
        for word in words:
            if self.canvas.stringWidth(current_line + word, fontName, fontSize) < text_width:
                current_line += word + " "
            else:
                self.tekst.textLine(current_line.strip())
                current_line = word + " "
        
        if current_line:
            self.tekst.textLine(current_line.strip())

    def zetFont(self, fontSize, fontName):
        self.tekst.setFont(fontName, fontSize)

    def maakWitRegel(self, afstand = 15):
        self.schrijfTekst(" ", afstand)

    def maakPDF(self, object):
        i = 1

        self.schrijfTekst(object.getNaam(), 25, 'Helvetica-Bold')
        self.schrijfTekst(f"Omschrijving: {object.getOmschrijving()}")
        self.schrijfTekst(f"Aantal personen: {object.getAantalPersonen()}")
        self.schrijfTekst(f"Plantaardig: {object.getPlantAardig()}")
        self.maakWitRegel()
        self.schrijfTekst("Ingredienten:", 15, 'Helvetica-Bold')

        for ingredient in object.getIngredienten():
            self.schrijfTekst(f"{ingredient}")
            
        self.maakWitRegel()
        self.schrijfTekst("Stappen:", 15, 'Helvetica-Bold')

        for stap in object.getStappen():
            self.schrijfTekst(f"{i}. {stap}")

            i += 1

        self.upload()

    def upload(self):
        self.canvas.drawText(self.tekst)

        self.canvas.showPage()
        self.canvas.save()

    