# Django imports
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Local Django imports
from user.decorators import is_patient
from prescription.models import PatientPrescription


class ListPatientPrescription(ListView):
    '''
        A list of all patient prescriptions.
    '''
    template_name = 'list_patient_prescription.html'
    context_object_name = 'list_patient_prescription'
    model = PatientPrescription
    paginate_by = 20
    ordering = ['-date_created']

    @method_decorator(login_required)
    @method_decorator(is_patient)
    def dispatch(self, *args, **kwargs):
        return super(ListPatientPrescription, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        return self.model.objects.filter(patient=self.request.user)
