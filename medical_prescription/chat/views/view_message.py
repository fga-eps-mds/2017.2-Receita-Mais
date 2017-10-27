from django.views.generic.detail import DetailView

from chat.models import Message


class MessageDetailView(DetailView):

    model = Message
    template_name = "view_message.html"
