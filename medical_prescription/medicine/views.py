from django.shortcuts import render
from .models import ActivePrinciple


class ListActivePrinciple(ListView):
    model = ActivePrinciple
    template_name = "list_medicine.html"
    context_object_name = 'list_active_principle'
    paginate_by = 20

    def get_queryset(self):
        return ActivePrinciple.objects.all()
