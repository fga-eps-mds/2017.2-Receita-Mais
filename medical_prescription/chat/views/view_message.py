from django.views.generic.detail import DetailView

from chat.models import Message


class MessageDetailView(DetailView):

    model = Message
    template_name = "view_message.html"

    context_object_name = 'list'
    model = Message
    paginate_by = 40

    def get_queryset(self):
        return self.model.objects.filter(user_to=self.request.user)
