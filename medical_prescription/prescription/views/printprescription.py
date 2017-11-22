# Standard
from io import BytesIO

# Django
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Local Django imports
from user.decorators import is_health_professional
from prescription.models import Prescription
from prescription.views import HeaderFooter

# Third-Party
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.colors import (black, purple, white, yellow)


# @method_decorator(login_required)
# @method_decorator(is_health_professional)
def generate_pdf(request, pk, jk):
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
    styles.add(ParagraphStyle(
                name='centered', alignment=TA_CENTER,
                fontName='Times-Roman',
                fontSize=10,
                leading=12,
                leftIndent=0,
                rightIndent=0,
                firstLineIndent=0,
                spaceBefore=0,
                spaceAfter=0,
                bulletFontName='Times-Roman',
                bulletFontSize=10,
                bulletIndent=0,
                textColor=black,
                backColor=None,
                wordWrap=None,
                borderWidth=0,
                borderPadding=0,
                borderColor=None,
                borderRadius=None,
                allowWidows=1,
                allowOrphans=0,
                textTransform=None,
                endDots=None,
                splitLongWords=1,))

    # Generate a PDF
    if len(prescription.medicines.all()) != 0 or prescription.manipulated_medicines.all() != 0:
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
                if custom_prescription_medicine.manipulated_medicine == custom_medicine:
                    elements.append(Paragraph(custom_prescription_medicine.via, styles['Normal']))
                    elements.append(Paragraph(custom_prescription_medicine.posology, styles['Normal']))
                    elements.append(Paragraph(custom_prescription_medicine.get_quantity_display(), styles['Normal']))
            elements.append(Spacer(1, 12))
    else:
        # Nothing to do.
        pass

    elements.append(Spacer(1, 12))
    if len(prescription.recommendation_prescription.all()) != 0:
        elements.append(Paragraph('Recomendacoes', styles['Heading1']))
        for recommendation in prescription.recommendation_prescription.all():
            elements.append(Paragraph(recommendation.recommendation, styles['Normal']))
            elements.append(Spacer(1, 12))
    else:
        # Nothing to do.
        pass

    elements.append(Spacer(1, 12))
    if len(prescription.default_exams.all()) != 0 or len(prescription.custom_exams.all()) != 0:
        elements.append(Paragraph('Exames', styles['Heading1']))
        for default_exams in prescription.default_exams.all():
            elements.append(Paragraph(default_exams.description, styles['Normal']))
            elements.append(Spacer(1, 12))

        for custom_exams in prescription.custom_exams.all():
            elements.append(Paragraph(custom_exams.description, styles['Normal']))
            elements.append(Spacer(1, 12))

    else:
        # NOTHING TO DO
        pass

    doc.build(elements, canvasmaker=HeaderFooter)

    pdf = buffer.getvalue()
    buffer.close()

    response.write(pdf)
    return response
