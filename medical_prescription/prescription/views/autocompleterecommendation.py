# standard library
import json

# Django imports
from django.views.generic import View
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# local django
from user.decorators import is_health_professional
from recommendation.models import NewRecommendation, CustomRecommendation
from prescription import constants


class AutoCompleteRecommendation(View):
    """
    Responsible for getting Recommendations similar to digits entered.
    """

    @method_decorator(login_required)
    @method_decorator(is_health_professional)
    def dispatch(self, *args, **kwargs):
        return super(AutoCompleteRecommendation, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            search = request.GET.get('term', '')
            list_recommendations = []

            # self.get_new_recommendations(search, list_recommendations)
            self.get_custom_recommendations(search, request.user, list_recommendations)

            data = json.dumps(list_recommendations)
            mimetype = 'application/json'

            return HttpResponse(data, mimetype)

    def get_custom_recommendations(self, search, health_professional, list_recommendations):
        queryset = CustomRecommendation.objects.filter(recommendation__icontains=search,
                                                       health_professional=health_professional,
                                                       is_active=True)[:5]

        # Encapsulates in a json needed to be sent.
        for custom_recommendation in queryset:
            custom_recommendation_item = {}
            custom_recommendation_item['value'] = self.parse_description(custom_recommendation.recommendation)
            custom_recommendation_item['type'] = 'custom_recommendation'
            custom_recommendation_item['id'] = custom_recommendation.auto_increment_id
            custom_recommendation_item['description'] = self.parse_description(custom_recommendation.recommendation)

            list_recommendations.append(custom_recommendation_item)

    # def get_new_recommendations(self, search, list_recommendations):
    #     queryset = NewRecommendation.objects.filter(description__icontains=search)[:5]
    #
    #     # Encapsulates in a json needed to be sent.
    #     for new_recommendation in queryset:
    #         new_recommendation_item = {}
    #         new_recommendation_item['value'] = self.parse_description(new_recommendation.recommendation_description)
    #         new_recommendation_item['type'] = 'new_recommendation'
    #         new_recommendation_item['description'] = self.parse_description(new_recommendation.recommendation_description)
    #
    #         list_recommendations.append(new_recommendation_item)

    # Print only the first 175 characters of the exam description.
    def parse_description(self, description):
        if len(description) > constants.MAX_LENGTH_DESCRIPTION_AUTOCOMPLETE:
            return description[:175] + '...'
        else:
            return description
