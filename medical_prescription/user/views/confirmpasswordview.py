# standard library
import logging

# Django
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views.generic import FormView

# Local Django
from user.models import ResetPasswordProfile, Patient
from user.forms import ConfirmPasswordForm
from user import constants

# Set level logger.
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(constants.DEFAULT_LOGGER)


class ConfirmPasswordView(FormView):
    '''
    Reset the user password.
    '''
    form_class = ConfirmPasswordForm
    template_name = 'password_confirm.html'

    def get(self, request, *args, **kwargs):
        logger.debug("Start get method.")
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    # Validate key and update the new password of 'User'.
    def post(self, request, activation_key, *args, **kwargs):
        logger.debug("Start get method.")

        form = ConfirmPasswordForm(request.POST or None)

        # Get reset object.
        user_profile = get_object_or_404(ResetPasswordProfile, activation_key=activation_key)

        user = user_profile.user

        if(request.method == 'POST' and user is not None):
            if(form.is_valid()):
                if(self._validate_activation_key(user_profile)):

                    user_profile.delete()
                    # Change user password and save in database
                    self._save_user_password(user, form)
                    # Change user password and save in database.

                    # Redirect for especific login page.
                    template_redirect = self.get_type_user(user.email)

                    return redirect(template_redirect)

                else:
                    logger.debug("Exit get method - not validate key.")
                    return redirect('/')
            else:
                # Nothing to do.
                pass
        else:
            # Nothing to do.
            pass
        logger.debug("Exit get method.")
        return render(request, 'password_confirm.html', {'form': form})

    # Return login page of especific user type.
    def get_type_user(self, email):
        query = Patient.objects.filter(email=email)

        if(query.exists()):
            return 'login_patient'
        else:
            return 'login_healthprofessional'

    # Validate key expiration time.
    def _validate_activation_key(self, user_p, *args):
        # Case key expires.
        if(user_p.key_expires < timezone.now()):
            # key expires.
            user_p.delete()
            return False
        else:
            return True

    # Update user password in databe.
    def _save_user_password(self, user, form):
        if(form.is_valid()):
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            return redirect('/')
        else:
            # Nothing to do.
            pass
