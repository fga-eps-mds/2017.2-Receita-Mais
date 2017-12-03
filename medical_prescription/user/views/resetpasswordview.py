# standard library
import hashlib
import datetime
import random
import logging

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

# Set level logger.
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(constants.DEFAULT_LOGGER)


class ResetPasswordView(FormView):
    '''
    Send an e-mail to reset user password.
    '''
    form_class = ResetPasswordForm
    template_name = 'reset_password.html'

    # Render password reset page.
    def get(self, request, *args, **kwargs):
        logger.debug("Start get method.")
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    # Get form information.
    def post(self, request, *args, **kwargs):
        logger.debug("Start post method.")

        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']

        # Search the user in database.
        try:
            user = User.objects.get(email=email)
        except:
            logger.exception("User not found.")
            messages.error(request, constants.EMAIL_NOT_EXIST_MESSAGE)
            return render(request, 'reset_password.html',
                          {"form": form})

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

            return redirect('/')
        except:
            logger.exception("Confirmation already sent.")
            messages.error(request, constants.EMAIL_MESSAGE_EXIST)
            return render(request, 'reset_password.html',
                          {"form": form})
        else:
            # nothing to do
            pass

    # Create recover key in database.
    def _create_recover_profile(self, user):
            logger.debug("Start recover profile.")

            email = user.email
            # Create a random sha1 code.
            salt = hashlib.sha1(str(random.random()).encode('utf-8')).hexdigest()[:5]

            # Join 'salt' and 'email' to create the activation key.
            activation_key = hashlib.sha1(str(salt + email).encode('utf‌​-8')).hexdigest()

            # Make a expire parameter for the activation key.
            key_expires = datetime.datetime.today() + datetime.timedelta(2)

            new_profile = ResetPasswordProfile(user=user,
                                               activation_key=activation_key,
                                               key_expires=key_expires)

            logger.debug("Exit recover profile.")
            return new_profile
