from django.conf.urls import url
from chat.views import (InboxHealthProfessionalView,
                        ComposeView,
                        AutoCompleteEmail,
                        OutboxView,
                        SentMessageDetailView,
                        InboxPatientView,
                        ViewMessagePatient,
                        ViewMessageHealthProfessional)

urlpatterns = (
    url(r'^inbox_health_professional/$', InboxHealthProfessionalView.as_view(), name='inbox_health_professional'),
    url(r'^inbox_patient/$', InboxPatientView.as_view(), name='inbox_patient'),
    url(r'^outbox/$', OutboxView.as_view(), name='outbox'),
    url(r'^compose/$', ComposeView.as_view(), name='compose'),
    url(r'^compose/ajax/autocomplete_email/$', AutoCompleteEmail.as_view(), name='autocomplete_email'),
    url(r'^view_message_patient/(?P<pk>[\w-]+)$', ViewMessagePatient.as_view(), name='view_message_patient'),
    url(r'^view_message_health_professional/(?P<pk>[\w-]+)$',
        ViewMessageHealthProfessional.as_view(),
        name='view_message_health_professional'),
    url(r'^view_sent_message/(?P<pk>[\w-]+)$', SentMessageDetailView.as_view(), name='view_sent_message'),
)
