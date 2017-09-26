# Django
from django.views.generic import ListView

# Local Django
from user.models import Patient


class ShowPatientsView(ListView):
    model = Patient
    template_name = 'view_patient.html'
    context_object_name = 'patients'
    paginate_by = 10
