# Django imports
from django.views.generic import DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Local Django imports
from user.decorators import is_health_professional
from prescription.models import Prescription


class PrintPrescription(DetailView):
    template_name = 'list_prescription.html'
    context_object_name = 'prescription'
    model = Prescription

    def print_prescription(self):
        pass
