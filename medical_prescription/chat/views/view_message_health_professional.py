from django.urls import reverse
from django.utils.decorators import method_decorator
from chat.views import MessageDetailView
from user.decorators import is_health_professional
from django.contrib.auth.decorators import login_required


@method_decorator(login_required, name='dispatch')
@method_decorator(is_health_professional, name='dispatch')
class ViewMessageHealthProfessional(MessageDetailView):
    """
    Display details of the Message for HealthProfessional.
    """

    template_name = 'view_message_health_professional.html'

    def get_success_url(self):
        return reverse('view_message_health_professional', kwargs={'pk': self.object.pk})
