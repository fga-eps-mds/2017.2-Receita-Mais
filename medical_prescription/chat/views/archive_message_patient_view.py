# Django
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

# Local Django
from user.decorators import is_patient
from chat.models import Message


@method_decorator(login_required, name='dispatch')
@method_decorator(is_patient, name='dispatch')
class ArchiveMessagePatientView(View):
    '''
    View to archive messages.
    '''

    def post(self, pk):
        message = Message.objects.get(pk=pk)
        message.is_active_patient = False
        message.save()
        return HttpResponseRedirect(reverse_lazy('inbox_patient'))
