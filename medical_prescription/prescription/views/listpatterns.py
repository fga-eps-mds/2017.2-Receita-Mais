# Django imports
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Local Django imports
from user.decorators import is_health_professional
from prescription.models import Pattern


class ListPatterns(ListView):
    '''
        View for list created of health professional in database.
    '''
    template_name = 'list_patterns.html'
    context_object_name = 'list_patterns'
    model = Pattern
    paginate_by = 20
    ordering = ['-date_created']

    @method_decorator(login_required)
    @method_decorator(is_health_professional)
    def dispatch(self, *args, **kwargs):
        return super(ListPatterns, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        return self.model.objects.filter(user_creator=self.request.user)
