# Django
from django.views.generic import UpdateView
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Local Django
from medication.models import Medication
from medication.forms import EditForm
from user.decorators import is_health_professional


class UpdateMedication(UpdateView):
    '''
        Edit Medication attributes with this class.
    '''

    sucess_url = 'list_medication'
    model = Medication
    template_name = 'edit_medication.html'
    form_class = EditForm

    @method_decorator(login_required)
    @method_decorator(is_health_professional)
    def dispatch(self, *args, **kwargs):
        return super(UpdateMedication, self).dispatch(*args, **kwargs)

    # Redirect for list _medications_by_health_professional.
    def get_success_url(self):
        return reverse(self.sucess_url)
