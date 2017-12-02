# Django
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

# Local Django
from user.decorators import is_health_professional
from chat.models import Message


@method_decorator(login_required, name='dispatch')
@method_decorator(is_health_professional, name='dispatch')
class ArchiveMessageOutboxView(View):
    '''
    View to archive messages.
    '''

    def post(self, pk):
        message = Message.objects.get(pk=pk)
        message.is_active_health_professional = False
        message.save()
        return HttpResponseRedirect(reverse_lazy('outbox'))
