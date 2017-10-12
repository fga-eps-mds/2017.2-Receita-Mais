# standard library
import logging
import hashlib
import datetime
import random

# Django from django.utils import timezone
from django.views.generic import FormView

# Local Django


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

    def register_activate_account():
        # Prepare the information needed to send the account verification
        # email.
        salt = hashlib.sha1(str(random.random()).
                            encode('utf-8')).hexdigest()[:5]
        activation_key = hashlib.sha1(str(salt+email).
                                      encode('utf‌​-8')).hexdigest()
        key_expires = datetime.datetime.today() + datetime.timedelta(2)
