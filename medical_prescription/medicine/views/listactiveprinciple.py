# Django imports
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Local Django imports
from medicine.models import ActivePrinciple, CustomActivePrinciple
from user.decorators import is_health_professional


class ListActivePrinciple(ListView):
    model = ActivePrinciple  # Model default to use create list itens
    template_name = 'list_medicine.html'  # Define template where itens will be shown
    context_object_name = 'list_active_principle'  # List itens default to list
    paginate_by = 20  # Number of itens per page

    @method_decorator(login_required)
    @method_decorator(is_health_professional)
    def dispatch(self, *args, **kwargs):
        return super(ListActivePrinciple, self).dispatch(*args, **kwargs)

    # This method is overridden by ListView. It defines list objects that are shown
    def get_queryset(self, *args, **kwargs):
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
