# Django
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

# Local Django
from user.models import Patient
from user.forms import UpdateUserForm


class UpdatePatient(UpdateView):
    model = Patient
    form_class = UpdateUserForm
    template_name = 'edit_patient.html'

    def get_success_url(self, **kwargs):
            return reverse_lazy('edit_patient', kwargs={'pk': self.object.id})
