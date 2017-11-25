# Django imports
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Local Django imports
from user.decorators import is_health_professional
from medicine.models import CustomActivePrinciple


class ListCustomPrinciple(ListView):
    '''
        View for list all principle in database.
    '''
    template_name = 'list_custom_principle.html'
    context_object_name = 'list_custom_principle'
    model = CustomActivePrinciple
    paginate_by = 20

    @method_decorator(login_required)
    @method_decorator(is_health_professional)
    def dispatch(self, *args, **kwargs):
        return super(ListCustomPrinciple, self).dispatch(*args, **kwargs)

    # Listing all objects Custom Principle in database.
    def get_queryset(self):
        return self.model.objects.all()
