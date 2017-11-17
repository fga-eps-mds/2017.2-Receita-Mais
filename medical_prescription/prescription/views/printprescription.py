from io import BytesIO
# Django imports
from django.http import HttpResponse
from django.views.generic import DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

import time
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

from reportlab.lib.enums import TA_RIGHT
from reportlab.lib.enums import TA_CENTER

# Local Django imports
from user.decorators import is_health_professional
from prescription.models import Prescription

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import cm


class PrintPrescription():

    def __init__(self, buffer, pagesize):
        self.buffer = buffer
        if pagesize == 'A4':
            self.pagesize = A4
        elif pagesize == 'Letter':
            self.pagesize = letter
        self.width, self.height = self.pagesize

    @staticmethod
    def _header_footer(canvas, doc):
        # Save the state of our canvas so we can draw on it
        canvas.saveState()
        styles = getSampleStyleSheet()

        # Header
        header = Paragraph('This is a multi-line header.  It goes on every page.   ' * 5, styles['Normal'])
        w, h = header.wrap(doc.width, doc.topMargin)
        header.drawOn(canvas, doc.leftMargin, doc.height + doc.topMargin - h)

        # Footer
        footer = Paragraph('This is a multi-line footer.  It goes on every page.   ' * 5, styles['Normal'])
        w, h = footer.wrap(doc.width, doc.bottomMargin)
        footer.drawOn(canvas, doc.leftMargin, h)

        # Release the canvas
        canvas.restoreState()

    # def generate_pdf(self, pk):
    #     response = HttpResponse(content_type='application/pdf')
    #     response['Content-Disposition'] = 'inline; filename="mypdf.pdf"'
    #
    #     prescription = Prescription.objects.get(pk=pk)
    #
    #     buffer = BytesIO()
    #
    #     # # Start writing the PDF here
    #     # p = canvas.Canvas(buffer, pagesize=letter)
    #     # p.setLineWidth(.3)
    #     # p.setFont('Helvetica', 12)
    #     #
    #     # p.drawString(30, 750, 'OFFICIAL COMMUNIQUE')
    #     # p.drawString(30, 735, 'OF ACME INDUSTRIES')
    #     # p.drawString(500, 750, "12/12/2010")
    #     # p.line(480, 747, 580, 747)
    #     #
    #     # p.drawString(275, 725, 'AMOUNT OWED:')
    #     # p.drawString(500, 725, "$1,000.00")
    #     # p.line(378, 723, 580, 723)
    #     #
    #     # p.drawString(30, 703, 'RECEIVED BY:')
    #     # p.line(120, 700, 580, 700)
    #     # p.drawString(120, 703, "JOHN DOE")
    #
    #     # End writing
    #     # p.drawString(10.5*cm, 28*cm, 'Receituário')
    #     # x = 4
    #     #
    #     # for prescription_medicine in prescription.prescriptionhasmedicine_set.all():
    #     #     p.drawString(x*cm, x*cm, prescription_medicine.via)
    #     #     x += 1
    #     #     p.drawString(x * cm, x * cm, prescription_medicine.posology)
    #     #     x += 1
    #     #     p.drawString(x * cm, x * cm, prescription_medicine.get_quantity_display())
    #     #     x+=1
    #     #
    #     # for medicine in prescription.medicines.all():
    #     #     p.drawString(x*cm, x*cm, medicine.name)
    #     #     x+=1
    #
    #
    #     # A large collection of style sheets pre-made for us
    #     styles = getSampleStyleSheet()
    #     # Our Custom Style
    #     styles.add(ParagraphStyle(name='RightAlign', fontName='Helvetica', align=TA_RIGHT))
    #
    #     doc = SimpleDocTemplate(buffer,
    #                             rightMargin=72,
    #                             leftMargin=72,
    #                             topMargin=72,
    #                             bottomMargin=72,
    #                             pagesize=letter)
    #
    #     # Our container for 'Flowable' objects
    #     elements = []
    #
    #     # A large collection of style sheets pre-made for us
    #     styles = getSampleStyleSheet()
    #     styles.add(ParagraphStyle(name='RightAlign', fontName='Helvetica', alignment = TA_RIGHT))
    #
    #     # Draw things on the PDF. Here's where the PDF generation happens.
    #     # See the ReportLab documentation for the full list of functionality.
    #     elements.append(Paragraph('My User Names', styles['RightAlign']))
    #     for medicine in prescription.medicines.all():
    #         elements.append(Paragraph(medicine.name, styles['Normal']))
    #
    #     doc.build(elements, onFirstPage=self._header_footer, onLaterPages=self._header_footer,
    #               canvasmaker=NumberedCanvas)
    #     # Get the value of the BytesIO buffer and write it to the response.
    #
    #     # p.showPage()
    #     # p.save()
    #
    #     pdf = buffer.getvalue()
    #     buffer.close()
    #     response.write(pdf)
    #
    #     return response

    def generate_pdf(self, pk):
        buffer = BytesIO()
        doc = SimpleDocTemplate(buffer,
                                rightMargin=72,
                                leftMargin=72,
                                topMargin=72,
                                bottomMargin=72,
                                pagesize=letter)

        # Our container for 'Flowable' objects
        elements = []

        # A large collection of style sheets pre-made for us
        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(name='centered', alignment=TA_CENTER))

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        users = [
            {'name': 'Teste'},
            {'name': 'Teste1'},
            {'name': 'Teste2'}
        ]
        elements.append(Paragraph('My User Names', styles['Heading1']))
        for i, user in enumerate(users):
            elements.append(Paragraph(user['name'], styles['Normal']))

        doc.build(elements, onFirstPage=_header_footer(), onLaterPages=_header_footer(),
                  canvasmaker=NumberedCanvas)

        # Get the value of the BytesIO buffer and write it to the response.
        # pdf = buffer.getvalue()
        # buffer.close()
        # return pdf


class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        """add page info to each page (page x of y)"""
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_page_number(self, page_count):
        # Change the position of this to wherever you want the page number to be
        self.drawRightString(211 * mm, 15 * mm + (0.2 * inch),
                             "Page %d of %d" % (self._pageNumber, page_count))