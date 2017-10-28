from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Local Django imports
from user.decorators import is_health_professional

from medicine.models import ManipulatedMedicine


class ListManipulatedMedicinenByHealthProfessional(ListView):
    '''
        View for listing medications created by the Health Professional.
    '''

    template_name = 'list_manipulated_medicines.html'
    context_object_name = 'list_medicines'
    model = ManipulatedMedicine
    paginate_by = 20

    @method_decorator(login_required)
    @method_decorator(is_health_professional)
    def dispatch(self, *args, **kwargs):
        return super(ListManipulatedMedicinenByHealthProfessional, self).dispatch(*args, **kwargs)

    # Listing objects created by the logged Health Professional.
    def get_queryset(self):
        return self.model.objects.filter(health_professional=self.request.user)
