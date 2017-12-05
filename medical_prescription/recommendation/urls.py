# Django
from django.conf.urls import url

# Django Local
from .views import (CustomRecommendationCreateView,
                    ListCustomRecommendations,
                    CustomRecommendationDeleteView,
                    UpdateCustomRecommendation,
                    )

urlpatterns = (
    url(r'^create_custom_recomendation/$', CustomRecommendationCreateView.as_view(),
        name='create_custom_recomendation'),
    url(r'^list_custom_recommendations/$', ListCustomRecommendations.as_view(), name='list_custom_recommendations'),
    url(r'^delete_custom_recommendation/(?P<pk>[0-9]+)/$', CustomRecommendationDeleteView.post,
        name='delete_custom_recommendation'),
    url(r'^update_custom_recommendation/(?P<pk>[0-9]+)/$', UpdateCustomRecommendation.as_view(),
        name='update_custom_recommendation'),
)
