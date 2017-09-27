# standard library
import hashlib
import datetime
import random

# Django
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.views.generic import FormView

# Local Django
from user.models import (User,
                         ResetPasswordProfile,
                         )
from user.forms import ResetPasswordForm
from user import constants


class ResetPasswordView(FormView):
    '''
    Send an e-mail to reset user password.
    '''
    form_class = ResetPasswordForm
    template_name = 'reset_password.html'

    # Render password reset page.
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    # Get form information.
    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')

        # Search the user in database.
        try:
            user = User.objects.get(email=email)
        except:
            return render(request, 'message.html', {"message": "usuário não encontrado"})

        try:

            # Get informations and create recover key.
            new_profile = self._create_recover_profile(user)
            new_profile.save()

            send_mail(constants.EMAIL_SUBJECT,
                      (constants.EMAIL_BODY % new_profile.activation_key),
                      constants.EMAIL_ADRESS,
                      [email],
                      fail_silently=False)

            messages.success(request, constants.EMAIL_SUCESS_MESSAGE)

            return redirect('/home')
        except:
            messages.error(request, constants.EMAIL_MESSAGE_EXIST)
            return render(request, 'reset_password.html',
                          {"form": form})
        else:
            # nothing to do
            pass

    # Create recover key in database.
    def _create_recover_profile(self, user):
            email = user.email
            # Create a random sha1 code.
            salt = hashlib.sha1(str(random.random()).encode('utf-8')).hexdigest()[:5]

            # Join 'salt' and 'email' to create the activation key.
            activation_key = hashlib.sha1(str(salt+email).encode('utf‌​-8')).hexdigest()

            # Make a expire parameter for the activation key.
            key_expires = datetime.datetime.today() + datetime.timedelta(2)

            new_profile = ResetPasswordProfile(user=user,
                                               activation_key=activation_key,
                                               key_expires=key_expires)

            return new_profile
