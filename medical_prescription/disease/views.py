# Django imports.
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Local Django imports
from .models import Disease
from user.decorators import is_health_professional


# List disease class.
class ListDisease(ListView):
    model = Disease
    template_name = 'list_disease.html'
    context_object_name = 'list_disease'
    paginate_by = 20

    @method_decorator(login_required)
    @method_decorator(is_health_professional)
    def dispatch(self, *args, **kwargs):
        return super(ListDisease, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        return Disease.objects.all()
