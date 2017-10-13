from django.views.generic import CreateView
from medication.forms import CreateMedicationForm


class CreateMedicationView(CreateView):
    template_name = 'create_medication_form.html'
    sucesss_url = 'list_all_medications.html'
    form_class = CreateMedicationForm
