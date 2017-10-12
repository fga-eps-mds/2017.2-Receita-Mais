# standard library
import logging
import hashlib
import datetime
import random

# Django from django.utils import timezone
from django.views.generic import View
from django.core.mail import send_mail

# Local Django
from user.models import User, UserActivateProfile


class ConfirmAccountView(View):
    # REGISTRAR
    # 1 - Criar um identificador único daquele usuário.
    # 2 - Criar um "perfil" temporário que vai ser responsável por linkar o usuário com essa chave.
    # 3 - Salvar Esse perfil temporário.
    # 4 - Enviar email com as informações.

    # NA HORA DE CONFIRMAR:
    # 1 - Identificar o perfil que possui aquela URL.
    # 2 - Obter Usuário
    # 3 - Ativar o usuário
    # 3.5 - Informar o usuário que sua conta foi ativada.
    # 4 - Redirecionar ele para a página de X.
    def activate_account_request(self, email):
        profile = self.create_activate_account_profile(email)
        self.send_activation_account_email(email, profile)

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

        new_profile = UserActivateProfile(user=user, activation_key=activation_key,
                                          key_expires=key_expires)
        new_profile.save()
        print("PROFILE SAVED")
        print(user.email)
        print(new_profile.activation_key)

        return new_profile

    def send_activation_account_email(email, UserActivateProfile):
        print("Sending email")
        email_subject = 'Oi'
        email_body = 'Alo'

        send_mail(email_subject, email_body, 'codamaisapp@gmail.com', email, fail_silently=False)
