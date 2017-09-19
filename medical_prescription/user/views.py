import hashlib
import datetime
import random

from django.shortcuts import render, redirect, render_to_response
from django.contrib import auth
from django.core.mail import send_mail
from django.contrib import messages

from .models import HealthProfessional, User, ResetPasswordProfile
from .forms import HealthProfessionalForm, UserLoginForm, ResetPasswordForm

# render html login.


def register_view(request):

    form = UserLoginForm(request.POST or None)

    if form.is_valid():
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = User.objects.create_user(email=email, password=password)
        user.save()

    # return render(request, "register.html", {"form": form})


def login_view(request):
    '''
    Render Login template.
    '''

    # this is a 'MIGUE' REMOVE-ME
    if(request.method == 'POST'):
        register_view(request)
    # end of 'MIGUE'

    if request.user.id is not None:
        print("Id is not None")
    else:
        # Nothing to do
        pass

    form = UserLoginForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():

            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            user = auth.authenticate(email=email, password=password)

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

# reset the password of Users


def reset_password(request):
    if request.user.id is not None:
        return redirect('/home')
    else:
        # nothing to do
        pass

    form = ResetPasswordForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data.get('email')

        try:
            user = User.objects.get(email=email)
        except:
            return render(request, 'message.html', {"message": "usuário não encontrado"})

        try:
            # Prepare informations to send email
            salt = hashlib.sha1(str(random.random()).encode('utf-8')).hexdigest()[:5]

            activation_key = hashlib.sha1(str(salt+email).encode('utf‌​-8')).hexdigest()

            key_expires = datetime.datetime.today() + datetime.timedelta(2)

            new_profile = ResetPasswordProfile(user=user,
                                               activation_key=activation_key,
                                               key_expires=key_expires)
            new_profile.save()

            # TODO(lucas kishima) create constants for email_subject and email_body

            email_subject = 'Recuperar senha'
            email_body = """
                         Usuário: %s, para recuperar sua senha clique no seguinte link
                         em menos de 48 horas:\nhttp://0.0.0.0:8000/home/recover/%s
                         """ % (user.username, activation_key)

            send_mail(email_subject, email_body, 'medicalprescriptionapp@gmail.com', [email],
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
