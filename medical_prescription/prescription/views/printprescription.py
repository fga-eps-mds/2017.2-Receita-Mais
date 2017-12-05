# Standard
from io import BytesIO

# Django
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Local Django imports
from user.decorators import is_health_professional
from prescription.models import Prescription, Pattern, NoPatientPrescription, PatientPrescription
from prescription.views import NumberedCanvas

# Third-Party
from reportlab.lib.pagesizes import letter, A4, A5
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.colors import (black, purple, white, yellow)
from reportlab.lib.units import inch, mm
from reportlab.lib.utils import ImageReader


class PrintPrescription:
    """
     Print PDF.
     """
    def __init__(self, buffer, prescription, pattern):
        self.buffer = buffer
        self.prescription = prescription
        self.pattern = pattern
        self.width = pattern.pagesize
        self.height = pattern.pagesize
        if pattern.pagesize == 'A4':
            self.pagesize = A4
        elif pattern.pagesize == 'A5':
            self.pagesize = A5
        elif pattern.pagesize == 'letter':
            self.pagesize = letter

    def _header_footer(self, canvas, doc):
        # Save the state of our canvas so we can draw on it.
        canvas.saveState()
        self.styles = getSampleStyleSheet()
        self.styles.add(ParagraphStyle(name='centered', alignment=TA_CENTER))
        self.styles.add(ParagraphStyle(name='right', alignment=TA_RIGHT))

        self.header = Paragraph(self.pattern.header, self.styles['right'])
        self.w, self.h = self.header.wrap(doc.width, doc.topMargin)

        try:
            specialize_prescription = NoPatientPrescription.objects.get(prescription_ptr=self.prescription)
        except:
            specialize_prescription = None

        if specialize_prescription is None:
            specialize_prescription = PatientPrescription.objects.get(prescription_ptr=self.prescription)
            self.patient_name = Paragraph("Paciente: " + specialize_prescription.patient.name, self.styles['right'])
        else:
            self.patient_name = Paragraph("Paciente: " + specialize_prescription.patient, self.styles['right'])

        self.w, self.h = self.patient_name.wrap(doc.width, doc.topMargin)

        self.medic_name = Paragraph(self.prescription.health_professional.name, self.styles['centered'])
        self.w, self.h = self.medic_name.wrap(doc.width, doc.bottomMargin)

        specialty = self.prescription.health_professional.specialty_second

        if specialty != 'Nao Possui':
            specialty = self.prescription.health_professional.specialty_first + ' / ' + specialty
        else:
            specialty = self.prescription.health_professional.specialty_first

        self.medic_specialty = Paragraph(specialty, self.styles['centered'])
        self.w, self.h = self.medic_specialty.wrap(doc.width, doc.bottomMargin)

        self.medic_crm = Paragraph(
            self.prescription.health_professional.crm + ' / ' + self.prescription.health_professional.crm_state,
            self.styles['centered'])
        self.w, self.h = self.medic_crm.wrap(doc.width, doc.bottomMargin)

        self.footer = Paragraph(self.pattern.footer, self.styles['centered'])
        self.w, self.h = self.footer.wrap(doc.width, doc.bottomMargin)

        # Draw on the canvas.
        self.draw_canvas(doc, canvas)

        # Release the canvas.
        canvas.restoreState()

    def draw_canvas(self, doc, canvas):
        if self.pagesize == A4:
            self.draw_page_size_A4(doc, canvas)

        elif self.pagesize == A5:
            self.draw_page_size_A5(doc, canvas)

        elif self.pagesize == letter:
            self.draw_page_size_letter(doc, canvas)

    def draw_page_size_A4(self, doc, canvas):
        # Header.
        self.header.drawOn(canvas, doc.leftMargin + 40, doc.height + doc.topMargin - self.h)
        self.patient_name.drawOn(canvas, doc.leftMargin + 40, doc.height + doc.topMargin - 60)

        # Footer.
        self.medic_name.drawOn(canvas, doc.leftMargin + 10, 60)
        self.medic_specialty.drawOn(canvas, doc.leftMargin + 10, 48)
        self.medic_crm.drawOn(canvas, doc.leftMargin + 10, 36)
        self.footer.drawOn(canvas, doc.leftMargin + 10, 12)

        # Draw Lines.
        canvas.setLineWidth(0.5)
        canvas.line(66, 78, letter[0] - 66, 78)
        canvas.setLineWidth(.3)
        canvas.line(30, 750, 580, 750)

        if self.pattern.logo:
            img = ImageReader(self.pattern.logo.path)
            canvas.drawImage(img, 30, 760, 1 * inch, 1 * inch, mask='auto')

    def draw_page_size_A5(self, doc, canvas):
        # Header
        self.header.drawOn(canvas, doc.leftMargin + 40, doc.height + doc.topMargin + 20)
        self.patient_name.drawOn(canvas, doc.leftMargin + 40, doc.height + doc.topMargin - 15)

        # Footer
        self.medic_name.drawOn(canvas, doc.leftMargin + 10, 64)
        self.medic_specialty.drawOn(canvas, doc.leftMargin + 10, 52)
        self.medic_crm.drawOn(canvas, doc.leftMargin + 10, 40)
        self.footer.drawOn(canvas, doc.leftMargin + 10, 18)

        # Draw Lines.
        canvas.setLineWidth(0.5)
        canvas.line(66, 78, A5[0] - 66, 78)
        canvas.setLineWidth(.3)
        canvas.line(30, 500, 390, 500)
        if self.pattern.logo:
            img = ImageReader(self.pattern.logo.path)
            canvas.drawImage(img, 30, 510, 0.75 * inch, 0.75 * inch, mask='auto')

    def draw_page_size_letter(self, doc, canvas):
        # Header
        self.header.drawOn(canvas, doc.leftMargin + 40, doc.height + doc.topMargin - self.h)
        self.patient_name.drawOn(canvas, doc.leftMargin + 40, doc.height + doc.topMargin - 60)

        # Footer
        self.medic_name.drawOn(canvas, doc.leftMargin + 10, 60)
        self.medic_specialty.drawOn(canvas, doc.leftMargin + 10, 48)
        self.medic_crm.drawOn(canvas, doc.leftMargin + 10, 36)
        self.footer.drawOn(canvas, doc.leftMargin + 10, 12)

        # Draw Lines.
        canvas.setLineWidth(0.5)
        canvas.line(66, 78, letter[0] - 66, 78)
        canvas.setLineWidth(.3)
        canvas.line(30, 700, 580, 700)
        if self.pattern.logo:
            img = ImageReader(self.pattern.logo.path)
            canvas.drawImage(img, 30, 710, 1 * inch, 1 * inch, mask='auto')

    def print_users(self):
        doc = self.choose_pagesize()
        self.elements = []
        self.styles = getSampleStyleSheet()
        self.styles.add(ParagraphStyle(name='centered', alignment=TA_CENTER))
        self.styles.add(ParagraphStyle(
                        'default',
                        fontName=self.pattern.font,
                        fontSize=int(self.pattern.font_size),
                        leading=12,
                        alignment=TA_LEFT,
                        bulletFontName=self.pattern.font,
                        bulletFontSize=int(self.pattern.font_size),
                        textColor=black,
                        endDots=None,
                        splitLongWords=1,)
        )

        # Draw things on the PDF. Here's where the PDF generation happens.
        self.list_medicines_pdf()
        self.list_recommendation_pdf()
        self.list_exam_pdf()

        doc.build(self.elements, onFirstPage=self._header_footer, onLaterPages=self._header_footer,
                  canvasmaker=NumberedCanvas)

        # Get the value of the BytesIO buffer and write it to the response.
        pdf = self.buffer.getvalue()
        self.buffer.close()
        return pdf

    def list_medicines_pdf(self):
        self.elements.append(Spacer(1, 50))
        if self.prescription.medicines.all() or self.prescription.manipulated_medicines.all():
            self.elements.append(Paragraph('Medicamentos', self.styles['Heading1']))
            for medicine in self.prescription.medicines.all():
                self.elements.append(Paragraph(medicine.name, self.styles['default']))

                for prescription_medicine in self.prescription.prescriptionhasmedicine_set.all():
                    if prescription_medicine.medicine == medicine:
                        self.elements.append(Paragraph(prescription_medicine.via, self.styles['default']))
                        self.elements.append(Paragraph(prescription_medicine.posology, self.styles['default']))
                        self.elements.append(Paragraph(prescription_medicine.get_quantity_display(), self.styles['default']))
                self.elements.append(Spacer(1, 12))

            for custom_medicine in self.prescription.manipulated_medicines.all():
                self.elements.append(Paragraph(custom_medicine.recipe_name, self.styles['default']))

                for custom_prescription_medicine in self.prescription.prescriptionhasmanipulatedmedicine_set.all():
                    if custom_prescription_medicine.manipulated_medicine == custom_medicine:
                        self.elements.append(Paragraph(custom_prescription_medicine.via, self.styles['default']))
                        self.elements.append(Paragraph(custom_prescription_medicine.posology, self.styles['default']))
                        self.elements.append(Paragraph(custom_prescription_medicine.get_quantity_display(), self.styles['default']))
                self.elements.append(Spacer(1, 12))
            self.elements.append(PageBreak())
            self.elements.append(Spacer(1, 32))
        else:
            # Nothing to do.
            pass

    def list_recommendation_pdf(self):
        self.elements.append(Spacer(1, 12))
        if self.prescription.new_recommendations.all() or self.prescription.custom_recommendations.all():
            self.elements.append(Paragraph('Recomendacoes', self.styles['Heading1']))

            for recommendation in self.prescription.new_recommendations.all():
                self.elements.append(Paragraph(recommendation.recommendation_description, self.styles['default']))
                self.elements.append(Spacer(1, 12))

            for recommendation in self.prescription.custom_recommendations.all():
                self.elements.append(Paragraph(recommendation.recommendation, self.styles['default']))
                self.elements.append(Spacer(1, 12))
            self.elements.append(PageBreak())
            self.elements.append(Spacer(1, 32))
        else:
            # Nothing to do.
            pass

    def list_exam_pdf(self):
        self.elements.append(Spacer(1, 12))
        if self.prescription.default_exams.all() or self.prescription.custom_exams.all()or self.prescription.new_exams.all():
            self.elements.append(Paragraph('Exames', self.styles['Heading1']))
            for default_exams in self.prescription.default_exams.all():
                self.elements.append(Paragraph(default_exams.description, self.styles['default']))
                self.elements.append(Spacer(1, 12))

            for custom_exams in self.prescription.custom_exams.all():
                self.elements.append(Paragraph(custom_exams.description, self.styles['default']))
                self.elements.append(Spacer(1, 12))

            for new_exams in self.prescription.new_exams.all():
                self.elements.append(Paragraph(new_exams.exam_description, self.styles['default']))
                self.elements.append(Spacer(1, 12))
        else:
            # Nothing to do.
            pass

    def choose_pagesize(self):
        if self.pagesize == A4:
            doc = SimpleDocTemplate(self.buffer,
                                    rightMargin=100,
                                    leftMargin=100,
                                    topMargin=50,
                                    bottomMargin=50,
                                    pagesize=self.pagesize)

        elif self.pagesize == A5:
            doc = SimpleDocTemplate(self.buffer,
                                    rightMargin=50,
                                    leftMargin=50,
                                    topMargin=50,
                                    bottomMargin=100,
                                    pagesize=self.pagesize)

        elif self.pagesize == letter:
            doc = SimpleDocTemplate(self.buffer,
                                    rightMargin=100,
                                    leftMargin=100,
                                    topMargin=50,
                                    bottomMargin=50,
                                    pagesize=self.pagesize)
        return doc

    def generate_pdf(request, pk, jk):
        # Create the HttpResponse object with the appropriate PDF headers.
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="PrescriptionPDF.pdf"'
        prescription = Prescription.objects.get(pk=pk)
        pattern = Pattern.objects.get(pk=jk)
        buffer = BytesIO()

        report = PrintPrescription(buffer, prescription, pattern)
        pdf = report.print_users()

        response.write(pdf)
        return response
