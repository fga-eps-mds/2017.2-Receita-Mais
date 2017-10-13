# Django
from django.conf.urls import url

# Local Django

from .views import (ListExams,
                    ListCustomExams,
                    CreateCustomExamsView,
                    UpdateCustomExam)


urlpatterns = (
    url(r'^list_exams/$', ListExams.as_view(), name='list_exams'),
    url(r'^list_custom_exams/$', ListCustomExams.as_view(), name='list_custom_exams'),
    url(r'^create_custom_exams/$', CreateCustomExamsView.as_view(), name='create_custom_exams'),
    url(r'^update_custom_exams/(?P<pk>[0-9]+)/$', UpdateCustomExam.as_view(), name='update_custom_exams'),
)
