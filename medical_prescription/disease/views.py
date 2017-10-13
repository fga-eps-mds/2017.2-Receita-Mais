# Django imports.
from django.views.generic import ListView

# Local Django imports
from .models import Disease


# List disease class.
class ListDisease(ListView):
    model = Disease
    template_name = 'list_disease.html'
    context_object_name = 'list_disease'
    paginate_by = 20

    def get_queryset(self):
        return Disease.objects.all()
