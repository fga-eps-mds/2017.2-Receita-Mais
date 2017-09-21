import hashlib
import datetime
import random

from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.contrib import auth
from django.core.mail import send_mail
from django.contrib import messages
from django.utils import timezone

from .models import HealthProfessional, User, ResetPasswordProfile
from .forms import (HealthProfessionalForm,
                    UserLoginForm,
                    ResetPasswordForm,
                    ConfirmPasswordForm)


def register_view(request):
    '''
    Function to register a user in the database.
    '''
    # Get form.
    form = UserLoginForm(request.POST or None)

    # If the form is valid, create a user.
    if form.is_valid():
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = User.objects.create_user(email=email, password=password)
        user.save()
    else:
        # Nothing to do.
        pass

    return render(request, "register.html", {"form": form})


def login_view(request):
    '''
    Render Login template.
    '''

    if request.user.id is not None:
        print("Id is not None")
    else:
        # Nothing to do
        pass

    form = UserLoginForm(request.POST or None)

    # If POST request the method login user.
    if request.method == 'POST':
        if form.is_valid():

            # Get form information.
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            # Authenticate the user.
            user = auth.authenticate(email=email, password=password)

            # Case user is authentic login.
            if(user is not None):
                if user.is_active:
                    auth.login(request, user)
                    return render_to_response('message.html', {'message': 'Usuário logou'})
                else:
                    return render_to_response('message.html', {'message'}, 'Usuário não ativo')
            else:
                return render_to_response('message.html', {'message': 'O usuário não foi autenticado'})

        else:
            # Not authenticate
            return render_to_response('message.html', {'message': 'formulário não é valido'})
    else:
        return render(request, 'login.html', {'form': form})


def reset_password(request):
    '''
    Send an e-mail to reset user password.
    '''

    # Get form information.
    form = ResetPasswordForm(request.POST or None)

    if form.is_valid():

        email = form.cleaned_data.get('email')

        # Search the user in database
        try:
            user = User.objects.get(email=email)
        except:
            return render(request, 'message.html', {"message": "usuário não encontrado"})

        # Create a hash with the 'salt' and the user e-mail and send the same to the user.

        try:

            # Create a random sha1 code.
            salt = hashlib.sha1(str(random.random()).encode('utf-8')).hexdigest()[:5]

            # Join 'salt' and 'email' to create the activation key.
            activation_key = hashlib.sha1(str(salt+email).encode('utf‌​-8')).hexdigest()

            # Make a expire parameter for the activation key.
            key_expires = datetime.datetime.today() + datetime.timedelta(2)

            new_profile = ResetPasswordProfile(user=user,
                                               activation_key=activation_key,
                                               key_expires=key_expires)

            new_profile.save()

            # Standar e-mail text.
            email_subject = 'Recuperar senha'
            email_body = ('Segue sua chave de ativaçãohttp://0.0.0.0:8000/home/reset_confirm/%s.' % activation_key)

            send_mail(email_subject,
                      email_body,
                      'medicalprescriptionapp@gmail.com',
                      [email],
                      fail_silently=False)

            messages.success(request,
                             'Verifique a caixa de entrada do seu email para recuperar sua senha.')

            return redirect('/home')
        except:

            messages.error(request, 'um email de recuperação de senha já foi enviado para este endereço!')
            return render(request, 'reset_password.html',
                          {"form": form})
    else:
        # nothing to do
        pass

    return render(request, 'reset_password.html', {"form": form})


def confirm_password(request, activation_key):
    '''
    Confirm change password user.
    '''

    form = ConfirmPasswordForm(request.POST or None)

    # Get reset object.
    user_profile = get_object_or_404(ResetPasswordProfile, activation_key=activation_key)

    user = user_profile.user

    # Case key expires.
    if(user_profile.key_expires < timezone.now()):
        # key expires.
        user.profile.delete()
        return redirect('/')
    else:
        # Nothing to do.
        pass

    # Change user password and save in database.
    if(request.method == 'POST'):
        if(form.is_valid()):
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            user_profile.delete()
            return redirect('/')
        else:
            # Nothing to do.
            pass
    else:
        # Nothing to do.
        pass

    return render(request, 'password_confirm.html', {'form': form})


def logout_view(request):
    auth.logout(request)
    return redirect('/home')


def register_health_professional(request):
    form = HealthProfessionalForm()
    context = {
        'form': form
    }
    return render(request, 'register_health_professional.html', context)


def view_health_professional(request):
    health_professionals = HealthProfessional.objects.all()
    context = {
        'health_professionals': health_professionals
    }
    return render(request, 'view_health_professional.html', context)


def edit_health_professional(request):
    return render(request, 'edit_health_professional.html')


def delete_health_professional(request):
    return render(request, 'delete_health_professional.html')
