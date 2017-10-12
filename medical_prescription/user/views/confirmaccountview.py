# standard library
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

        new_profile = UserActivateProfile(user=user, activation_key=activation_key,
                                          key_expires=key_expires)
        new_profile.save()
        print("PROFILE SAVED")
        print(user.email)
        print(new_profile.activation_key)

        return new_profile

    def send_activation_account_email(email, UserActivateProfile):
        print("Sending email")
        email_subject = 'Confirmação de Conta'
        email_body = """
                     Obrigado por se registrar.Para ativar sua conta, clique neste link
                     para ativar sua conta: http://localhost:8000/user/confirm/%s
                     """
        print("Chave:")
        print(UserActivateProfile.activation_key)

        send_mail(email_subject, email_body % UserActivateProfile.activation_key , 'codamaisapp@gmail.com', [email] , fail_silently=False)
