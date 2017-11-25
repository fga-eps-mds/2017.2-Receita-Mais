# Django
from django.views.generic import DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.http import JsonResponse

# Local Django
from prescription.models import Pattern, Prescription
from user.decorators import is_health_professional


class ShowPatternsView(DetailView):
    """
    See all patterns.
    """
    template_name = 'show_patterns.html'
    context_object_name = 'list_patterns'
    model = Pattern

    @method_decorator(login_required)
    @method_decorator(is_health_professional)
    def dispatch(self, *args, **kwargs):
        return super(ShowPatternsView, self).dispatch(*args, **kwargs)

    # Return a JSON's prescription.
    def get(self, request, *args, **kwargs):
        data = dict()

        prescription = self.get_context(request)

        context = {
            'prescription': prescription,
            self.context_object_name: self.get_queryset(),
            }

        data['html_form'] = render_to_string(self.template_name, context, request=request)
        # Json to communication Ajax.
        return JsonResponse(data)

    # Get a Prescription object in database.
    def get_context(self, request):
        pk = self.kwargs['pk']
        return Prescription.objects.get(pk=pk)

    def get_queryset(self):
        return self.model.objects.filter(user_creator=self.request.user)
