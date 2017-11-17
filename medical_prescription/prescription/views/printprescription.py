import os
from io import BytesIO
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.units import mm, inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.pdfgen import canvas
from reportlab.platypus import (SimpleDocTemplate, Paragraph, PageBreak, Spacer, Image)
from reportlab.lib.pagesizes import LETTER
from django.http import HttpResponse
from reportlab.lib.utils import ImageReader

# Local Django imports
from user.decorators import is_health_professional
from prescription.models import Prescription


class NumberedCanvas(canvas.Canvas):
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
        logo = ImageReader("medical_prescription/static/img/user.png")

        x = 128
        self.saveState()
        self.setStrokeColorRGB(0, 0, 0)
        self.setLineWidth(0.5)
        self.line(66, 78, LETTER[0] - 66, 78)
        self.setFont('Times-Roman', 10)
        self.drawString(LETTER[0]-x, 65, page)
        self.setLineWidth(.3)

        self.drawImage(logo, 30, 730, 0.75*inch, 0.75*inch, mask='auto')

        self.drawString(30, 715, 'CLINICA ALGUM')
        self.drawString(30, 705, 'NOME LOGO')
        self.drawString(500, 750, "12/12/2010")

        self.drawString(275, 725, 'PACIENTE:')
        self.drawString(500, 725, "ALGUM NOME")
        self.line(378, 723, 580, 723)

        self.line(30, 703, 580, 700)

        self.restoreState()


def generate_pdf(self, pk):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="My Users.pdf"'

    prescription = Prescription.objects.get(pk=pk)

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer,
                            rightMargin=100,
                            leftMargin=100,
                            topMargin=100,
                            bottomMargin=100,
                            pagesize=letter)

    elements = []

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='centered', alignment=TA_CENTER))

    # Draw things on the PDF. Here's where the PDF generation happens.

    elements.append(Paragraph('Medicamentos', styles['Heading1']))
    for medicine in prescription.medicines.all():
        elements.append(Paragraph(medicine.name, styles['Normal']))

        for prescription_medicine in prescription.prescriptionhasmedicine_set.all():
            if prescription_medicine.medicine == medicine:
                elements.append(Paragraph(prescription_medicine.via, styles['Normal']))
                elements.append(Paragraph(prescription_medicine.posology, styles['Normal']))
                elements.append(Paragraph(prescription_medicine.get_quantity_display(), styles['Normal']))
        elements.append(Spacer(1, 12))

    for custom_medicine in prescription.manipulated_medicines.all():
        elements.append(Paragraph(custom_medicine.recipe_name, styles['Normal']))

        for custom_prescription_medicine in prescription.prescriptionhasmanipulatedmedicine_set.all():
            if prescription_medicine.medicine == medicine:
                elements.append(Paragraph(custom_prescription_medicine.via, styles['Normal']))
                elements.append(Paragraph(custom_prescription_medicine.posology, styles['Normal']))
                elements.append(Paragraph(custom_prescription_medicine.get_quantity_display(), styles['Normal']))
        elements.append(Spacer(1, 12))


    elements.append(Spacer(1, 12))
    elements.append(Paragraph('Recomendacoes', styles['Heading1']))
    for recommendation in prescription.recommendation_prescription.all():
        elements.append(Paragraph(recommendation.recommendation, styles['Normal']))
        elements.append(Spacer(1, 12))

    elements.append(Spacer(1, 12))
    elements.append(Paragraph('Exames', styles['Heading1']))
    for default_exams in prescription.default_exams.all():
        elements.append(Paragraph(default_exams.description, styles['Normal']))
        elements.append(Spacer(1, 12))

    for custom_exams in prescription.custom_exams.all():
        elements.append(Paragraph(custom_exams.description, styles['Normal']))
        elements.append(Spacer(1, 12))

    doc.build(elements, canvasmaker=NumberedCanvas)

    pdf = buffer.getvalue()
    buffer.close()

    response.write(pdf)
    return response
