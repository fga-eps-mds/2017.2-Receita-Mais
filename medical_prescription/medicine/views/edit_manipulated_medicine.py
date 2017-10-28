# Django
from django.views.generic import UpdateView
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Local Django
from user.decorators import is_health_professional
from medicine.forms import EditForm
from medicine.models import ManipulatedMedicine


class UpdateMedicine(UpdateView):
    '''
        Edit Medicine attributes with this class.
    '''

    sucess_url = 'list_all_medicines'
    model = ManipulatedMedicine
    template_name = 'edit_manipulated_medicine.html'
    form_class = EditForm

    @method_decorator(login_required)
    @method_decorator(is_health_professional)
    def dispatch(self, *args, **kwargs):
        return super(UpdateMedicine, self).dispatch(*args, **kwargs)

    # Redirect for list _medicine_by_health_professional.
    def get_success_url(self):
        return reverse(self.sucess_url)
