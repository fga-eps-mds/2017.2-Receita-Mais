# Django
from django.conf.urls import url

# Local Django

from .views import (ListExams)


urlpatterns = (
    url(r'^list_exams/$', ListExams.as_view(), name='list_exams'),
)
