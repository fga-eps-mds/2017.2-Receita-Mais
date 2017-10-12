from .models import ActivePrinciple, CustomActivePrinciple
from django.views.generic import ListView


class ListActivePrinciple(ListView):
    model = ActivePrinciple  # Model default to use create list itens
    template_name = 'list_medicine.html'  # Define template where itens will be shown
    context_object_name = 'list_active_principle'  # List itens default to list
    paginate_by = 20  # Number of itens per page

    # This method is overridden by ListView. It defines list objects that are shown
    def get_queryset(self):
        return ActivePrinciple.objects.all()

    # This method get list from CustomActivePrinciple
    def get_context_data(self, **kwargs):
        context = super(ListActivePrinciple, self).get_context_data(**kwargs)
        context['custons'] = CustomActivePrinciple.objects.all()
        # And so on for more models
        return context
