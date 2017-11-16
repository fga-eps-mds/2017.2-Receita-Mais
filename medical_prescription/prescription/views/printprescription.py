from io import BytesIO
# Django imports
from django.http import HttpResponse
from django.views.generic import DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Local Django imports
from user.decorators import is_health_professional
from prescription.models import Prescription

from reportlab.pdfgen import canvas


def generate_pdf(request, pk):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="mypdf.pdf"'

    prescription = Prescription.objects.get(pk=pk)

    buffer = BytesIO()
    p = canvas.Canvas(buffer)

    # Start writing the PDF here
    p.drawString(300, 300, 'Texto de teste.')
    # End writing

    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response
