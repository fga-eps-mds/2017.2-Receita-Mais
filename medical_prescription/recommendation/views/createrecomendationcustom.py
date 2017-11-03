from django.views.generic import FormView

from recommendation.models import CustomRecommendation
from recommendation.forms import CreateRecomendationCustomForm


class CustomRecommendationCreateView(FormView):
    model = CustomRecommendation
    form_class = CreateRecomendationCustomForm
    success_url = 'dashboard_health_professional/health_professional/'
    template_name = 'createcustomrecomendatiom.html'
