# Django
import time
from django.views.generic import FormView

from medicine.forms import CustomActivePrincipleForm


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
