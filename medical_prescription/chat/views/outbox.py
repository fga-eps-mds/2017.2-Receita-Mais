from django.views.generic import ListView
from chat.models import Message


class OutboxView(ListView):
    '''
    View for list messages in outbox.
    '''

    template_name = 'outbox.html'
    context_object_name = 'outbox'
    model = Message
    paginate_by = 40

    def get_queryset(self):
        return self.model.objects.filter(user_from=self.request.user)
