from django.conf.urls import url
from chat.views import InboxView, ComposeView

urlpatterns = (
    url(r'^inbox/$', InboxView.as_view(), name='inbox'),
    url(r'^compose/$', ComposeView.as_view(), name='compose'),
)
