# Django
from django.views.generic import CreateView
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Local Django
from medication.forms import CreateMedicationForm
from user.models import HealthProfessional
from user.decorators import is_health_professional


class CreateMedicationView(CreateView):
    template_name = 'create_medication_form.html'
    sucesss_url = 'list_all_medications.html'
    form_class = CreateMedicationForm

    @method_decorator(login_required)
    @method_decorator(is_health_professional)
    def dispatch(self, *args, **kwargs):
        return super(CreateMedicationView, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse('list_medication')

    def form_valid(self, form):
        health_professional_object = HealthProfessional.objects.filter(pk=self.request.user.pk)[0]

        form.instance.health_professional = health_professional_object
        return super().form_valid(form)
