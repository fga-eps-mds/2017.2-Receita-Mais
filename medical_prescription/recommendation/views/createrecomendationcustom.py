from django.views.generic import FormView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from recommendation.models import CustomRecommendation
from recommendation.forms import CreateRecomendationCustomForm
from user.decorators import is_health_professional


class CustomRecommendationCreateView(FormView):
    model = CustomRecommendation
    form_class = CreateRecomendationCustomForm
    success_url = '/dashboard_health_professional/health_professional/'
    template_name = 'createcustomrecomendatiom.html'

    @method_decorator(login_required)
    @method_decorator(is_health_professional)
    def dispatch(self, *args, **kwargs):
        return super(CustomRecommendationCreateView, self).dispatch(*args, **kwargs)
