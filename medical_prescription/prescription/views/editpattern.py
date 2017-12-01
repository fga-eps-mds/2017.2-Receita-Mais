# Django
from django.views.generic import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

# Local
from user.decorators import is_health_professional
from prescription.forms import UpdatePatternForm
from prescription.models import Pattern


class EditPatternView(UpdateView):
    '''
        This class updates a pattern.
    '''

    model = Pattern
    template_name = 'create_prescription_model.html'
    form_class = UpdatePatternForm

    @method_decorator(login_required)
    @method_decorator(is_health_professional)
    def dispatch(self, *args, **kwargs):
        return super(EditPatternView, self).dispatch(*args, **kwargs)

    def get_success_url(self, **kwargs):
        return reverse_lazy('list_patterns')
