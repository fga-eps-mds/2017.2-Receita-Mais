from django.conf.urls import url
from chat.views import InboxView, ComposeView, AutoCompleteEmail, MessageDetailView

urlpatterns = (
    url(r'^inbox/$', InboxView.as_view(), name='inbox'),
    url(r'^compose/$', ComposeView.as_view(), name='compose'),
    url(r'^compose/ajax/autocomplete_email/$', AutoCompleteEmail.as_view(), name='autocomplete_email'),
    url(r'^view_message/(?P<pk>[\w-]+)$', MessageDetailView.as_view(), name='view_message'),
)
