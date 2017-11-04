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
class UnarchiveMessagePatientView(View):
    '''
    View to unarchive messages.
    '''

    def post(self, pk):
        message = Message.objects.get(pk=pk)
        message.is_active_patient = True
        message.save()
        return HttpResponseRedirect(reverse_lazy('archive_box_patient'))
