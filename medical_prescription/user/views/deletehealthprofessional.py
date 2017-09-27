# Django
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

# Local Django
from user.models import HealthProfessional


class DeleteHealthProfessional(DeleteView):
    model = HealthProfessional
    success_url = reverse_lazy('landing_page')
    template_name = 'health_professional_confirm_delete.html'
