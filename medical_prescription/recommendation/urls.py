# Django
from django.conf.urls import url

# Django Local
from .views import (CustomRecommendationCreateView,
                    ListCustomRecommendations)

urlpatterns = (
    url(r'^create_custom_recomendation/$', CustomRecommendationCreateView.as_view(),
        name='create_custom_recomendation'),
    url(r'^list_custom_recommendations/$', ListCustomRecommendations.as_view(), name='list_custom_recommendations'),

)
