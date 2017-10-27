# Django
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView

# Local Django
from chat.models import Message
from user.decorators import is_health_professional


class InboxView(ListView):
    '''
    View for list messages in inbox.
    '''

    template_name = 'inbox.html'
    context_object_name = 'inbox'
    model = Message
    paginate_by = 40

    @method_decorator(login_required)
    @method_decorator(is_health_professional)
    def get_queryset(self):
        return self.model.objects.filter(user_to=self.request.user)
