# Django
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views.generic import FormView

# Local Django
from user.models import ResetPasswordProfile
from user.forms import ConfirmPasswordForm


class ConfirmPasswordView(FormView):
    '''
    Reset the user password.
    '''
    form_class = ConfirmPasswordForm
    template_name = 'password_confirm.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    # Validate key and update the new password of 'User'.
    def post(self, request, activation_key, *args, **kwargs):

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

                else:
                    return redirect('/')
            else:
                # Nothing to do.
                pass
        else:
            # Nothing to do.
            pass

        return render(request, 'password_confirm.html', {'form': form})

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
