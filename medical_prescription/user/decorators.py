# Django
from django.shortcuts import redirect
from user.models import HealthProfessional


def is_health_professional(method):
    """
    Verify if user is a health professional.
    """
    def wrap(request, *args, **kwargs):
        is_health_professional = hasattr(request.user, 'healthprofessional')
        if is_health_professional:
            return method(request, *args, **kwargs)
        else:
            return redirect('/')

    return wrap
