# Django
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


# Local Django
from user.models import HealthProfessional
from user.decorators import health_professional_is_account_owner_with_pk


class DeleteHealthProfessional(DeleteView):
    model = HealthProfessional
    success_url = reverse_lazy('landing_page')
    template_name = 'health_professional_confirm_delete.html'

    @method_decorator(login_required)
    @method_decorator(health_professional_is_account_owner_with_pk)
    def dispatch(self, *args, **kwargs):
        return super(DeleteHealthProfessional, self).dispatch(*args, **kwargs)
