# Django
from django.views.generic import ListView
from chat.models import Message
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Local Django
from user.decorators import is_health_professional


@method_decorator(login_required, name='dispatch')
@method_decorator(is_health_professional, name='dispatch')
class InboxHealthProfessionalView(ListView):
    '''
    View for list messages in inbox.
    '''

    template_name = 'inbox_health_professional.html'
    context_object_name = 'inbox'
    model = Message
    paginate_by = 40

    # Return all Messages for the user.
    def get_queryset(self):
        return self.model.objects.filter(user_to=self.request.user)
