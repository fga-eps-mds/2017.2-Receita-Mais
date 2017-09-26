from django.conf.urls import include, url
from django.contrib import admin

from landing.views import home

urlpatterns = [
    url(r'^user/', include('user.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='landing_page'),
]
