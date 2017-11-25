# Django imports
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Local Django imports
from user.decorators import is_health_professional
from medicine.models import ActivePrinciple


class ListAllPrinciple(ListView):
    '''
        View for list all principle in database.
    '''
    template_name = 'list_all_principle.html'
    context_object_name = 'list_all_principle'
    model = ActivePrinciple
    paginate_by = 20

    @method_decorator(login_required)
    @method_decorator(is_health_professional)
    def dispatch(self, *args, **kwargs):
        return super(ListAllPrinciple, self).dispatch(*args, **kwargs)

    # Listing all objects Principle in database.
    def get_queryset(self):
        return self.model.objects.all()
