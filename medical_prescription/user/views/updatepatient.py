# Django
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


# Local Django
from user.models import Patient
from user.forms import UpdateUserForm
from user.decorators import patient_is_account_owner_with_pk


class UpdatePatient(UpdateView):
    model = Patient
    form_class = UpdateUserForm
    template_name = 'edit_patient.html'

    @method_decorator(login_required)
    @method_decorator(patient_is_account_owner_with_pk)
    def dispatch(self, *args, **kwargs):
        return super(UpdatePatient, self).dispatch(*args, **kwargs)

    def get_success_url(self, **kwargs):
            return reverse_lazy('edit_patient', kwargs={'pk': self.object.id})
