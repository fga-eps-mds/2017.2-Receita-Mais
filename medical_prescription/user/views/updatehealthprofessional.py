# Django
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

# Local Django
from user.models import User
from user.forms import UpdateUserForm


class UpdateHealthProfessional(UpdateView):
    model = User
    form_class = UpdateUserForm
    success_url = reverse_lazy('view')
    template_name = 'edit_health_professional.html'
