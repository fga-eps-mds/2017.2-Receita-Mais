from django.views.generic import ListView
from .models import Disease
# Create your views here.


class ListDisease(ListView):
    model = Disease
    template_name = 'list_disease.html'
    context_object_name = 'list_disease'
    paginate_by = 20

    def get_queryset(self):
        return Disease.objects.all()
