# Django
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Local Django
from medication.models import Medication
from user.decorators import is_health_professional


class ListMedicationByHealthProfessional(ListView):
    '''
        View for listing medications created by the Health Professional.
    '''

    template_name = 'list_medication.html'
    context_object_name = 'list_medications'
    model = Medication
    paginate_by = 20

    @method_decorator(login_required)
    @method_decorator(is_health_professional)
    def dispatch(self, *args, **kwargs):
        return super(ListMedicationByHealthProfessional, self).dispatch(*args, **kwargs)

    # Listing objects created by the logged Health Professional.
    def get_queryset(self):
        return self.model.objects.filter(health_professional=self.request.user)
