# Django
from django.conf.urls import url

# Django Local
from .views import (CustomRecommendationCreateView)

urlpatterns = (
    url(r'^create_custom_recomendation/$', CustomRecommendationCreateView.as_view(),
        name='create_custom_recomendation'),
)
