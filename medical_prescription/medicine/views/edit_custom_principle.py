# Django imports
import time
from django.views.generic import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Local Django imports
from medicine.models import CustomActivePrinciple
from medicine.forms import CustomActivePrincipleForm
from user.decorators import is_health_professional


class EditCustomActivePrinciple(UpdateView):
    model = CustomActivePrinciple  # Defines which model will be edited
    form_class = CustomActivePrincipleForm  # Class forms.py define how the form will be
    template_name = 'register_custom_principle.html'   # Template define html redirect create
    success_url = '/medicine/list_custom_principle/'  # Redirect this url when post is success

    @method_decorator(login_required)
    @method_decorator(is_health_professional)
    def get(self, request, *args, **kwargs):
        return super(EditCustomActivePrinciple, self).post(request, *args, **kwargs)

    @method_decorator(login_required)
    @method_decorator(is_health_professional)
    def post(self, request, *args, **kwargs):
        time.sleep(0.4)  # Time to wait to inform the creation of the principle
        return super(EditCustomActivePrinciple, self).post(request, *args, **kwargs)
