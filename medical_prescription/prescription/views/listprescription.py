# Django imports
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Local Django
from user.decorators import is_health_professional
from prescription.models import (PatientPrescription,
                                 NoPatientPrescription,
                                 PrescriptionRecommendation,
                                 PrescriptionHasMedicine)


@method_decorator(login_required, name='dispatch')
@method_decorator(is_health_professional, name='dispatch')
class ListPrescription(TemplateView):
    '''
        View for list all prescriptions in database.
    '''
    template_name = 'list_prescription.html'
    paginate_by = 20

    # Listing all objects related to prescriptions in database.
    def get_context_data(self, **kwargs):
        return{
              'list_prescription': PatientPrescription.objects.filter(health_professional=self.request.user),
              'list_prescription_no_patient': NoPatientPrescription.objects.filter(
                                                                                   health_professional=self.request.user
                                                                                  ),
              'list_recommendation': PrescriptionRecommendation.objects.all(),
              'list_medicine': PrescriptionHasMedicine.objects.all(),
              }
