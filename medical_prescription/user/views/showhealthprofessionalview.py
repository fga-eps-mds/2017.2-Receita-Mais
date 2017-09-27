# Django
from django.views.generic import ListView

# Local Django
from user.models import HealthProfessional


class ShowHealthProfessionalView(ListView):
    model = HealthProfessional
    template_name = 'view_health_professional.html'
    context_object_name = 'health_professionals'
    paginate_by = 10
