# Django imports
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Local Django imports
from user.decorators import is_health_professional
from prescription.models import Prescription


class ListFavoritePrescription(ListView):
    '''
        View for list favorite prescriptions in database.
    '''
    template_name = 'list_favorite_prescriptions.html'
    context_object_name = 'list_favorite_prescriptions'
    model = Prescription
    paginate_by = 20
    ordering = ['-date_created']

    @method_decorator(login_required)
    @method_decorator(is_health_professional)
    def dispatch(self, *args, **kwargs):
        return super(ListFavoritePrescription, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        return self.model.objects.filter(health_professional=self.request.user, is_favorite=True)
