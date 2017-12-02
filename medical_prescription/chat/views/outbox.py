# Django
from django.views.generic import ListView
from chat.models import Message
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render

# Local Django
from user.decorators import is_health_professional
from user.models import User

@method_decorator(login_required, name='dispatch')
@method_decorator(is_health_professional, name='dispatch')
class OutboxView(ListView):
    '''
    View for list messages in outbox.
    '''

    template_name = 'outbox.html'
    context_object_name = 'outbox'
    model = Message
    paginate_by = 25

    def get(self, request, *args, **kwargs):

        context = {
            'outbox': Message.objects.filter(user_to=request.user),
            'image_profile': User.objects.get(email=request.user.email).image_profile.url
        }

        return render(request, self.template_name, context)

    # Return all send Message for the HealthProfessional.
    def get_queryset(self):
        return self.model.objects.filter(user_from=self.request.user,
                                         is_active_health_professional=True)
