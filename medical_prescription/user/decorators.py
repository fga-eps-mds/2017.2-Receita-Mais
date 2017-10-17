# Django
from django.shortcuts import redirect
from user.models import HealthProfessional


def health_professional_is_account_owner(method):
    """
    Verify if user is a health professional.
    """
    def wrap(request, pk, *args, **kwargs):
        is_health_professional = hasattr(request.user, 'health_professional')
        print(is_health_professional)
        is_owner = request.user.pk == pk
        print(is_owner)
        print(pk)
        print(request.user.pk)
        if is_owner:
            return method(request, pk, *args, **kwargs)
        else:
            return redirect('/')

    return wrap
