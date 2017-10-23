from django.conf.urls import url
from chat.views import InboxView

urlpatterns = (
    url(r'^chat/$', InboxView.as_view(), name='chat'),
)
