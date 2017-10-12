from django.views.generic import ListView
from .models import Medication


class ListMedication(ListView):

    '''
    Query and list objects Medication.
    '''

    template_name = 'list_medication.html'
    context_object_name = 'list_medications'
    model = Medication
    paginate_by = 20

    # Get 20 queries of objects Medication.
    def get_query_set(self, request):
        return self.model.objects.all()
