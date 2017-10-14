from django.views.generic import ListView
from medication.models import Medication


class ListAllMedications(ListView):
    '''
        View for list all medicatons in database.
    '''
    template_name = 'list_all_medications.html'
    context_object_name = 'list_medications'
    model = Medication
    paginate_by = 20

    # Listing all objects Medication in database.
    def get_queryset(self):
        return self.model.objects.all()
