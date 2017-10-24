from django.views.generic import ListView

from medicine.models import Medicine


class ListAllMedicines(ListView):
    '''
        View for list all medicatons in database.
    '''
    template_name = 'list_all_medicines.html'
    context_object_name = 'list_medicines'
    model = Medicine
    paginate_by = 20

    # Listing all objects Medication in database.
    def get_queryset(self):
        return self.model.objects.all()
