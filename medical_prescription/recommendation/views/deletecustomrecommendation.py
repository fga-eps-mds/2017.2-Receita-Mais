from django.views.generic import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from recommendation.models import CustomRecommendation
from user.decorators import is_health_professional


@method_decorator(login_required, name='dispatch')
@method_decorator(is_health_professional, name='dispatch')
class CustomRecommendationDeleteView(View):
    """
    Inactive custom recommendation.
    """

    def post(self, pk):
        custom_recommendation = CustomRecommendation.objects.get(pk=pk)
        custom_recommendation.is_active = False
        custom_recommendation.save()
        return HttpResponseRedirect(reverse_lazy('list_custom_recommendations'))
