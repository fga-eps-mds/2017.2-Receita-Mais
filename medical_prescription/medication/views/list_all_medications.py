# Django imports
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Local Django imports
from medication.models import Medication
from user.decorators import is_health_professional


class ListAllMedications(ListView):
    '''
        View for list all medicatons in database.
    '''
    template_name = 'list_all_medications.html'
    context_object_name = 'list_medications'
    model = Medication
    paginate_by = 20

    @method_decorator(login_required)
    @method_decorator(is_health_professional)
    def dispatch(self, *args, **kwargs):
        return super(ListAllMedications, self).dispatch(*args, **kwargs)

    # Listing all objects Medication in database.
    def get_queryset(self):
        return self.model.objects.all()
