from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^health_professional/', include('user.urls')),
    url(r'^admin/', admin.site.urls),
]
