
# Django
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect

# Local Django
from user.decorators import is_health_professional
from chat.models import Message, ArchiveMessage


@method_decorator(login_required, name='dispatch')
@method_decorator(is_health_professional, name='dispatch')
class ArchiveMessageView(View):

    def post(self, pk, *args, **kwargs):
        message = Message.objects.get(pk=pk)

        user_from = message.user_from
        user_to = message.user_to
        subject = message.subject
        date = message.date
        # messages = message.messages

        archived_message = ArchiveMessage(archive_user_from=user_from,
                                          archive_user_to=user_to,
                                          subject=subject, date=date)
        archived_message.save()
        message.delete()

        return HttpResponseRedirect("")
