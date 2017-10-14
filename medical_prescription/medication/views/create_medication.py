from django.views.generic import CreateView
from django.urls import reverse

from medication.forms import CreateMedicationForm

from user.models import HealthProfessional


class CreateMedicationView(CreateView):
    template_name = 'create_medication_form.html'
    sucesss_url = 'list_all_medications.html'
    form_class = CreateMedicationForm

    def get_success_url(self):
        return reverse('list_medication')

    def form_valid(self, form):
        health_professional_object = HealthProfessional.objects.filter(pk=self.request.user.pk)[0]

        form.instance.health_professional = health_professional_object
        return super().form_valid(form)
