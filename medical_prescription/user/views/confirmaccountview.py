# standard library
import logging
import hashlib
import datetime
import random

# Django from django.utils import timezone
from django.views.generic import FormView
from django.core.email import send_email

# Local Django
from .models import UserActivateProfile


class ConfirmAccountView(FormView):
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

    def register_activate_account(user):
        # Prepare the information needed to send the account verification
        # email.
        salt = hashlib.sha1(str(random.random()).
                            encode('utf-8')).hexdigest()[:5]
        activation_key = hashlib.sha1(str(salt+user.email).
                                      encode('utf‌​-8')).hexdigest()
        key_expires = datetime.datetime.today() + datetime.timedelta(2)

        new_profile = UserActivateProfile(user=user, activation_key=activation_key,
                                          key_expires=key_expires)
        new_profile.save()

    def send_activation_account_email(user):
        email_subject = 'Oi'
        email_body = 'Alo'

        send_email(email_subject, email_body, 'codamaisapp@gmail.com', user.email,
                   fail_silently=False)
