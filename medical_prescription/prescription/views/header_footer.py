import os

# Third-Party
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.utils import ImageReader


class HeaderFooter(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self.pages = []

    def showPage(self):
        self.pages.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        page_count = len(self.pages)
        for page in self.pages:
            self.__dict__.update(page)
            self.draw_canvas(page_count)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_canvas(self, page_count):
        page = "Page %s of %s" % (self._pageNumber, page_count)
        # logo = ImageReader("medical_prescription/static/img/user.png")

        x = 128
        self.saveState()
        self.setStrokeColorRGB(0, 0, 0)
        self.setLineWidth(0.5)
        self.line(66, 78, LETTER[0] - 66, 78)
        self.setFont('Times-Roman', 10)
        self.drawString(LETTER[0]-x, 65, page)
        self.setLineWidth(.3)

        # self.drawImage(logo, 30, 730, 0.75*inch, 0.75*inch, mask='auto')

        self.drawString(30, 715, 'CLINICA ALGUM')
        self.drawString(30, 705, 'NOME LOGO')
        self.drawString(500, 750, "12/12/2010")

        self.drawString(275, 725, 'PACIENTE:')
        self.drawString(500, 725, "ALGUM NOME")
        self.line(378, 723, 580, 723)

        self.line(30, 703, 580, 700)

        self.restoreState()
