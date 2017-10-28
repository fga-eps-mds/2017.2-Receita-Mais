# Django
from django.views.generic import CreateView
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Local Django
from user.decorators import is_health_professional
from medicine.forms import CreateManipulatedMedicineForm


class CreateMedicineView(CreateView):
    template_name = 'create_manipulated_medicine_form.html'
    sucesss_url = 'list_all_medicines.html'
    form_class = CreateManipulatedMedicineForm

    @method_decorator(login_required)
    @method_decorator(is_health_professional)
    def dispatch(self, *args, **kwargs):
        return super(CreateMedicineView, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse('list_all_medicines')

    def form_valid(self, form):
        form.instance.health_professional = self.request.user.healthprofessional
        return super().form_valid(form)
