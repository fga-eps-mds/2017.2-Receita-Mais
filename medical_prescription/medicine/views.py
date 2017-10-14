import time
from django.views.generic import ListView, FormView, UpdateView

from .models import ActivePrinciple, CustomActivePrinciple
from medicine.forms import CustomActivePrincipleForm


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


class CreateCustomActivePrinciple(FormView):
    form_class = CustomActivePrincipleForm  # Class forms.py define how the form will be
    template_name = 'register_custom_principle.html'  # Template define html redirect create
    success_url = '/medicine/list/'  # Redirect this url when post is success

    def dispatch(self, *args, **kwargs):
        time.sleep(0.4)  # Time to wait to inform the creation of the principle
        return super(CreateCustomActivePrinciple, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        self.customactiveprinciple = form.save(commit=False)
        self.customactiveprinciple.created_by = self.request.user.healthprofessional
        self.customactiveprinciple.save()

        return super(CreateCustomActivePrinciple, self).form_valid(form)


class EditCustomActivePrinciple(UpdateView):
    model = ActivePrinciple  # Defines which model will be edited
    form_class = CustomActivePrincipleForm  # Class forms.py define how the form will be
    template_name = 'register_custom_principle.html'   # Template define html redirect create
    success_url = '/medicine/list/'  # Redirect this url when post is success

    def get(self, request, *args, **kwargs):
        return super(EditCustomActivePrinciple, self).post(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        time.sleep(0.4)  # Time to wait to inform the creation of the principle
        return super(EditCustomActivePrinciple, self).post(request, *args, **kwargs)
