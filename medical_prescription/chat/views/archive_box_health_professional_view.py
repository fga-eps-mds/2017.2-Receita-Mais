# Django
from django.views.generic import ListView
from chat.models import Message
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Local Django
from user.decorators import is_health_professional


@method_decorator(login_required, name='dispatch')
@method_decorator(is_health_professional, name='dispatch')
class ArchiveBoxHealthProfessionalView(ListView):
    '''
    View for archived messages box.
    '''

    template_name = 'archive_health_professional.html'
    context_object_name = 'archive_message'
    model = Message
    paginate_by = 40

    # Return all Messages for the user.
    def get_queryset(self):
        query_to_inbox = self.model.objects.filter(user_to=self.request.user,
                                                   is_active_inbox_health_professional=False)
        query_from_outbox = self.model.objects.filter(user_from=self.request.user,
                                                      is_active_outbox_health_professional=False)

        records = (query_to_inbox | query_from_outbox).distinct()
        return records
