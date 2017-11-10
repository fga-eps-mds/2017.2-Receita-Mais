# Django imports
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Local Django imports
from user.decorators import is_health_professional
from prescription.models import NoPatientPrescription


class ListPrescriptionNoPatient(ListView):
    '''
        View for list all prescriptions in database.
    '''
    template_name = 'list_prescription_no_patient.html'
    context_object_name = 'list_prescription'
    model = NoPatientPrescription
    paginate_by = 20

    @method_decorator(login_required)
    @method_decorator(is_health_professional)
    def dispatch(self, *args, **kwargs):
        return super(ListPrescriptionNoPatient, self).dispatch(*args, **kwargs)

    # Listing all objects Medication in database.
    def get_queryset(self):
        return self.model.objects.filter(health_professional=self.request.user)
