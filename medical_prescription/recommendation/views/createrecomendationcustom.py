from django.views.generic import CreateView

from recommendation.models import CustomRecommendation
from recommendation.forms import CreateRecomendationCustomForm


class CustomRecommendationCreateView(CreateView):
    model = CustomRecommendation
    form_class = CreateRecomendationCustomForm
    success_url = 'dashboard_health_professional/health_professional/'
    template_name = 'createrecoment'
