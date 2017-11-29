# Django
from django.views.generic import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

#Local
from user.decorators import is_health_professional
from prescription.forms import PatternForm
from prescription.models import Pattern


class EditPatternView(UpdateView):
    '''
        This class updates a pattern.
    '''

    success_url = 'list_patterns'
    model = Pattern
    template_name = 'create_prescription_model.html'
    form_class = PatternForm

    @method_decorator(login_required)
    @method_decorator(is_health_professional)
    def dispatch(self, *args, **kwargs):
        return super(EditPatternView, self).dispatch(*args, **kwargs)