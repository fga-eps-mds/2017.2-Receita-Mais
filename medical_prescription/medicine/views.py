from .models import ActivePrinciple
from django.views.generic import ListView


class ListActivePrinciple(ListView):
    model = ActivePrinciple
    template_name = 'list_medicine.html'
    context_object_name = 'list_active_principle'
    paginate_by = 20

    def get_queryset(self):
        return ActivePrinciple.objects.all()
