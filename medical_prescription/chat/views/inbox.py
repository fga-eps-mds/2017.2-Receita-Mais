from django.views.generic import ListView
from chat.models import Message


class InboxView(ListView):
    '''
        View for list messages in inbox.
    '''

    template_name = 'chat_box.html'
    context_object_name = 'chat'
    model = Message
    paginate_by = 40

    def get_queryset(self):
        return self.model.objects.filter(user_to=self.request.user)
