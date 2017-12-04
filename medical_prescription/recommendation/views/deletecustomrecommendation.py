from django.views.generic import DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from recommendation.models import CustomRecommendation
from user.decorators import is_health_professional


class CustomRecommendationDeleteView(DeleteView):
    """
    Inactive custom recommendation.
    """
    model = CustomRecommendation
    template_name = 'deletecustomrecommendation.html'

    @method_decorator(login_required)
    @method_decorator(is_health_professional)
    def dispatch(self, *args, **kwargs):
        return super(CustomRecommendationDeleteView, self).dispatch(*args, **kwargs)
