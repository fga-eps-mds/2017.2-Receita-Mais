from .model import Medication
from django.views.generic import ListView


class ListMedication(ListView):

    '''
    Query and list objects Medication.
    '''

    template_name = 'list_medication.html'
    model = Medication

    # Get 20 queries of objects Medication.
    def get_20_query_set(self, request):
        return self.model.objects.all()[:20]
