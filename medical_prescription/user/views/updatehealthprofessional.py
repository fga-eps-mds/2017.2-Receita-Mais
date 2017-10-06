# Django
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

# Local Django
from user.models import User
from user.forms import UpdateUserForm


class UpdateHealthProfessional(UpdateView):
    model = User
    form_class = UpdateUserForm
    template_name = 'edit_health_professional.html'

    def get_success_url(self, **kwargs):
            return reverse_lazy('edit', kwargs={'pk': self.object.id})
