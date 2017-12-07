# Django imports
import time
from django.views.generic import FormView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Local Django imports
from medicine.forms import CustomActivePrincipleForm
from user.decorators import is_health_professional


class CreateCustomActivePrinciple(FormView):
    form_class = CustomActivePrincipleForm  # Class forms.py define how the form will be
    template_name = 'register_custom_principle.html'  # Template define html redirect create
    success_url = '/medicine/list_custom_principle/'  # Redirect this url when post is success

    @method_decorator(login_required)
    @method_decorator(is_health_professional)
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
