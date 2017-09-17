from django.conf.urls import url
from .views import login_view
from .views import logout_view

urlpatterns = (
    url(r'^login/$', login_view, name='login'),
    url(r'^logout/', logout_view, name='logout_view'),
)
