# standard library
import hashlib
import datetime
import random

# Django
from django.views.generic import View
from django.utils import timezone
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.contrib import messages

# Local Django
from user.models import User, UserActivateProfile


# This class is responsible for doing user account activation.
class ConfirmAccountView(View):

    # This method calls the methods resposible for creating the temporary user
    # profile and sending the confirmation email.
    def activate_account_request(email):
        profile = ConfirmAccountView.create_activate_account_profile(email)
        ConfirmAccountView.send_activation_account_email(email, profile)

    def create_activate_account_profile(email):
        print("Creating activate account profile")
        # Prepare the information needed to send the account verification
        # email.
        salt = hashlib.sha1(str(random.random()).
                            encode('utf-8')).hexdigest()[:5]
        activation_key = hashlib.sha1(str(salt+email).
                                      encode('utf‌​-8')).hexdigest()
        key_expires = datetime.datetime.today() + datetime.timedelta(2)

        user = User.objects.get(email=email)

        # Creating the temporary user.
        new_profile = UserActivateProfile(user=user, activation_key=activation_key,
                                          key_expires=key_expires)
        new_profile.save()

        return new_profile

    # Sending email for account activation.
    def send_activation_account_email(email, UserActivateProfile):
        email_subject = 'Confirmação de Conta'
        email_body = """
                     Obrigado por se registrar. Para ativar sua conta, clique
                     neste link: http://preskribe.herokuapp.com/user/confirm/%s
                     """

        send_mail(email_subject, email_body % UserActivateProfile.activation_key,
                  'medicalprescriptionapp@gmail.com', [email], fail_silently=False)

    # Activating account and deleting temporary profile when the account
    # confirmation link is requested.
    def activate_register_user(request, activation_key):

        # Getting ther user to be activated.
        try:
            user_profile = UserActivateProfile.objects.get(activation_key=activation_key)

        # If there is no user to be activated, an error message is displayed.
        except:
            messages.success(
                request, 'Não existe um usuário para ser ativado ou a conta ja foi ativada!', extra_tags='alert')
            return redirect('/')

        user = user_profile.user

        # Activating user account.
        if user_profile.key_expires > timezone.now():
            user.is_active = True
            user.save()
            user_profile.delete()
            messages.success(
                request, 'Conta ativada com sucesso!Realize login para acessar o sistema.', extra_tags='alert')

        # If the account activation time has expired, an error message is displayed.
        else:
            # TODO(João) Send message telling user that the time to activate account expired.
            #            And his register has been deleted.
            messages.success(
                request, 'O tempo de ativar essa conta expirou :( .Realize o registro novamente!).', extra_tags='alert')
            pass

        return redirect('/')
