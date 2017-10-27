from django.conf.urls import url
from chat.views import InboxView, ComposeView, AutoCompleteEmail, MessageDetailView, OutboxView, SentMessageDetailView

urlpatterns = (
    url(r'^inbox/$', InboxView.as_view(), name='inbox'),
    url(r'^outbox/$', OutboxView.as_view(), name='outbox'),
    url(r'^compose/$', ComposeView.as_view(), name='compose'),
    url(r'^compose/ajax/autocomplete_email/$', AutoCompleteEmail.as_view(), name='autocomplete_email'),
    url(r'^view_message/(?P<pk>[\w-]+)$', MessageDetailView.as_view(), name='view_message'),
    url(r'^view_sent_message/(?P<pk>[\w-]+)$', SentMessageDetailView.as_view(), name='view_sent_message'),
)
