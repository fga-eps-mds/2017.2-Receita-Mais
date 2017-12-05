from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Local Django imports
from recommendation.models import CustomRecommendation
from user.decorators import is_health_professional


class ListCustomRecommendations(ListView):
    '''
    Query and list objects Custom Recommendations.
    '''

    template_name = 'listcustomrecommendation.html'
    context_object_name = 'list_custom_recommendation'
    model = CustomRecommendation
    paginate_by = 20

    @method_decorator(login_required)
    @method_decorator(is_health_professional)
    def dispatch(self, *args, **kwargs):
        return super(ListCustomRecommendations, self).dispatch(*args, **kwargs)

    # Get 20 queries of objects Custom Recommendation.
    def get_queryset(self):
        return self.model.objects.filter(health_professional=self.request.user, is_active=True)
