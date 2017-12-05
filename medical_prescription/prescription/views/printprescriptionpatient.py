# Standard
from io import BytesIO

# Django
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Local Django imports
from user.decorators import is_health_professional
from prescription.models import Prescription, NoPatientPrescription, PatientPrescription
from prescription.views import NumberedCanvas

# Third-Party
from reportlab.lib.pagesizes import letter, A4, A5
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.colors import (black, purple, white, yellow)
from reportlab.lib.units import inch, mm


class PrintPrescriptionPatient:
    """
     Print PDF.
     """
    def __init__(self, buffer, prescription):
        self.buffer = buffer
        self.prescription = prescription
        self.width = A4
        self.height = A4

    def _header_footer(self, canvas, doc):
        # Save the state of our canvas so we can draw on it.
        canvas.saveState()
        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(name='centered', alignment=TA_CENTER))
        styles.add(ParagraphStyle(name='right', alignment=TA_RIGHT))

        try:
            specialize_prescription = NoPatientPrescription.objects.get(prescription_ptr=self.prescription)
        except:
            specialize_prescription = None

        if specialize_prescription is None:
            specialize_prescription = PatientPrescription.objects.get(prescription_ptr=self.prescription)
            patient_name = Paragraph("Paciente: " + specialize_prescription.patient.name, styles['right'])
        else:
            patient_name = Paragraph("Paciente: " + specialize_prescription.patient, styles['right'])

        w, h = patient_name.wrap(doc.width, doc.topMargin)

        medic_name = Paragraph(self.prescription.health_professional.name, styles['centered'])
        w, h = medic_name.wrap(doc.width, doc.bottomMargin)

        specialty = self.prescription.health_professional.specialty_second

        if(specialty != 'Nao Possui'):
            specialty = self.prescription.health_professional.specialty_first + ' / ' + specialty
        else:
            specialty = self.prescription.health_professional.specialty_first

        medic_specialty = Paragraph(specialty, styles['centered'])
        w, h = medic_specialty.wrap(doc.width, doc.bottomMargin)

        medic_crm = Paragraph(
            self.prescription.health_professional.crm + ' / ' + self.prescription.health_professional.crm_state,
            styles['centered'])
        w, h = medic_crm.wrap(doc.width, doc.bottomMargin)

        # Footer.
        medic_name.drawOn(canvas, doc.leftMargin + 10, 60)
        medic_specialty.drawOn(canvas, doc.leftMargin + 10, 48)
        medic_crm.drawOn(canvas, doc.leftMargin + 10, 36)

        # Draw Lines.
        canvas.setLineWidth(0.5)
        canvas.line(66, 78, letter[0] - 66, 78)
        canvas.setLineWidth(.3)
        canvas.line(30, 750, 580, 750)

        # Release the canvas.
        canvas.restoreState()

    def print_users(self):
        doc = SimpleDocTemplate(self.buffer,
                                rightMargin=100,
                                leftMargin=100,
                                topMargin=50,
                                bottomMargin=50,
                                pagesize=A4
                                )
        self.elements = []
        self.styles = getSampleStyleSheet()
        self.styles.add(ParagraphStyle(name='centered', alignment=TA_CENTER))
        self.styles.add(ParagraphStyle(
                        'default',
                        fontSize=12,
                        leading=12,
                        alignment=TA_LEFT,
                        bulletFontSize=12,
                        bulletIndent=0,
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
        if self.prescription.new_recommendations.all():
            self.elements.append(Paragraph('Recomendacoes', self.styles['Heading1']))
            for recommendation in self.prescription.new_recommendations.all():
                self.elements.append(Paragraph(recommendation.recommendation_description, self.styles['default']))
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

    def generate_pdf(request, pk):
        # Create the HttpResponse object with the appropriate PDF headers.
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="PrescriptionPDF.pdf"'
        prescription = Prescription.objects.get(pk=pk)
        buffer = BytesIO()

        report = PrintPrescriptionPatient(buffer, prescription)
        pdf = report.print_users()

        response.write(pdf)
        return response
