# Django
from django.conf.urls import url

# Local Django

from .views import (ListExams)


urlpatterns = (
    url(r'^list_exams/$', ListExams.as_view(), name='list_exams'),
    url(r'^create_custom_exams/$', ListExams.as_view(), name='create_custom_exams'),
)
