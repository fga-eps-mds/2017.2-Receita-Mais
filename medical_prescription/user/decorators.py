# Django imports
from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied


def is_health_professional(method):
    """
    Verify if user is a health professional.
    """
    def wrap(request, *args, **kwargs):
        is_health_professional = hasattr(request.user, 'healthprofessional')
        if is_health_professional:
            return method(request, *args, **kwargs)
        else:
            raise PermissionDenied

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
            raise PermissionDenied

    return wrap


def health_professional_is_account_owner_with_pk(method):
    """
    Verify if health professional is a owner of request with pk
    """
    def wrap(request, *args, **kwargs):
        is_health_professional = hasattr(request.user, 'healthprofessional')
        is_owner = int(request.user.pk) == int(kwargs.get('pk'))
        if is_owner and is_health_professional:
            return method(request, *args, **kwargs)
        else:
            raise PermissionDenied

    return wrap


def patient_is_account_owner_with_pk(method):
    """
    Verify if patient is a owner of request with pk
    """
    def wrap(request, *args, **kwargs):
        is_patient = hasattr(request.user, 'patient')
        is_owner = int(request.user.pk) == int(kwargs.get('pk'))
        if is_owner and is_patient:
            return method(request, *args, **kwargs)
        else:
            raise PermissionDenied

    return wrap


def health_professional_is_account_owner_with_email(method):
    """
    Verify if health professional is a owner of request with email
    """
    def wrap(request, email, *args, **kwargs):
        is_health_professional = hasattr(request.user, 'healthprofessional')
        is_owner = email == request.user.email
        if is_owner and is_health_professional:
            return method(request, email, *args, **kwargs)
        else:
            raise PermissionDenied

    return wrap


def patient_is_account_owner_with_email(method):
    """
    Verify if patient is a owner of request with email
    """
    def wrap(request, email, *args, **kwargs):
        is_patient = hasattr(request.user, 'patient')
        is_owner = email == request.user.email
        if is_owner and is_patient:
            return method(request, email, *args, **kwargs)
        else:
            raise PermissionDenied

    return wrap


def user_is_logged(method):
    """
    Make sure the user is logged in and redirects it to the dashboard
    """
    def wrap(request, *args, **kwargs):
        if 'user' in request.__dict__:
            if request.user.is_authenticated():
                is_health_professional = hasattr(request.user, 'healthprofessional')
                is_patient = hasattr(request.user, 'patient')
                if is_health_professional:
                    return redirect('/dashboard_health_professional/health_professional/')
                elif is_patient:
                    return redirect('/dashboard_patient/patient/')
                else:
                    return method(request, *args, **kwargs)
            else:
                return method(request, *args, **kwargs)
        else:
            return method(request, *args, **kwargs)

    return wrap
