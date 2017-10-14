# Django
from django.views.generic import ListView

from medicine.models import ActivePrinciple, CustomActivePrinciple


class ListActivePrinciple(ListView):
    model = ActivePrinciple  # Model default to use create list itens
    template_name = 'list_medicine.html'  # Define template where itens will be shown
    context_object_name = 'list_active_principle'  # List itens default to list
    paginate_by = 20  # Number of itens per page

    # This method is overridden by ListView. It defines list objects that are shown
    def get_queryset(self):
        list_all_principle = ActivePrinciple.objects.all()
        list_general = [geactivePrinciple for geactivePrinciple in list_all_principle if not
                        hasattr(geactivePrinciple, 'customactiveprinciple')]
        return list_general

    # This method get list from CustomActivePrinciple
    def get_context_data(self, **kwargs):
        context = super(ListActivePrinciple, self).get_context_data(**kwargs)
        try:
            context['custons'] = CustomActivePrinciple.objects.filter(created_by=self.request.user.healthprofessional)
        except Exception as e:
            context['custons'] = ''
        # And so on for more models
        return context
