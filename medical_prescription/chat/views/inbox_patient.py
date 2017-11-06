# Django
from django.views.generic import ListView
from chat.models import Message
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Local Django
from user.decorators import is_patient


@method_decorator(login_required, name='dispatch')
@method_decorator(is_patient, name='dispatch')
class InboxPatientView(ListView):
    '''
    View for list messages in inbox.
    '''

    template_name = 'inbox_patient.html'
    context_object_name = 'inbox'
    model = Message
    paginate_by = 25

    # Return all Messages for the Patient.
    def get_queryset(self):
        return self.model.objects.filter(user_to=self.request.user,
                                         is_active_patient=True)
