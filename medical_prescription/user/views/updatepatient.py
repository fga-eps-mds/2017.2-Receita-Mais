# Django
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

# Local Django
from user.models import Patient
from user.forms import UpdateUserForm


class UpdatePatient(UpdateView):
    model = Patient
    form_class = UpdateUserForm
    success_url = reverse_lazy('view')
    template_name = 'edit_patient.html'
