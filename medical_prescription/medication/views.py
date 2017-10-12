from django.views.generic import ListView
from .models import Medication


class ListMedicationByHealthProfessional(ListView):
    '''
        View for listing medications created by the Health Professional.
    '''

    template_name = 'list_medication.html'
    context_object_name = 'list_medications'
    model = Medication
    paginate_by = 20

    # Listing objects created by the logged Health Professional.
    def get_queryset(self):
        return self.model.objects.filter(health_professional=self.request.user)


class ListAllMedications(ListView):
    '''
        View for list all medicatons in database.
    '''
    template_name = 'list_all_medication'
    context_object_name = 'list_medications'
    model = Medication
    paginate_by = 20

    # Listing all objects Medication in database.
    def get_queryset(self):
        return self.model.objects.all()
