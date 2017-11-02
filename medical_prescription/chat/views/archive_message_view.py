
# Django
from django.views.generic import UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy

# Local Django
from user.decorators import is_health_professional
from chat.models import Message


@method_decorator(login_required, name='dispatch')
@method_decorator(is_health_professional, name='dispatch')
class ArchiveMessageView(UpdateView):

    def post(self, pk, *args, **kwargs):
        message = Message.objects.get(pk=pk)
        message.is_active = False
        message.save()

        return reverse_lazy(ArchiveMessageView)
