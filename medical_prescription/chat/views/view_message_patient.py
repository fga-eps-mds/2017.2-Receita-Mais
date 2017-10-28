from django.urls import reverse
from django.utils.decorators import method_decorator
from chat.views import MessageDetailView
from user.decorators import is_patient
from django.contrib.auth.decorators import login_required


@method_decorator(login_required, name='dispatch')
@method_decorator(is_patient, name='dispatch')
class ViewMessagePatient(MessageDetailView):
    """
    Display details of the Message for Patient.
    """

    template_name = 'view_message_patient.html'

    def get_success_url(self):
        return reverse('view_message_patient', kwargs={'pk': self.object.pk})
