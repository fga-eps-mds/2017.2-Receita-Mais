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


def is_patient(method):
    """
    Verify if user is a patient.
    """
    def wrap(request, *args, **kwargs):
        is_patient = hasattr(request.user, 'patient')
        if is_patient:
            return method(request, *args, **kwargs)
        else:
            return redirect('/')

    return wrap


def health_professional_is_account_owner(method):
    """
    Verify if health professional is a owner of request
    """
    def wrap(request, *args, **kwargs):
        is_health_professional = hasattr(request.user, 'healthprofessional')
        is_owner = int(request.user.pk) == int(kwargs.get('pk'))
        if is_owner and is_health_professional:
            return method(request, *args, **kwargs)
        else:
            return redirect('/')

    return wrap


def patient_is_account_owner(method):
    """
    Verify if patient is a owner of request
    """
    def wrap(request, *args, **kwargs):
        is_patient = hasattr(request.user, 'patient')
        is_owner = int(request.user.pk) == int(kwargs.get('pk'))
        if is_owner and is_patient:
            return method(request, *args, **kwargs)
        else:
            return redirect('/')

    return wrap
