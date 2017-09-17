from django.shortcuts import render, redirect, render_to_response
from django.contrib import auth
from .models import HealthProfessional, User
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


def recover_password_view(request):

    if request.user.id is not None:
        return redirect('/home')
    else:
        # Nothing to do
        pass

    form = ResetPasswordForm(request.POST or None)

    if(request.method == 'POST'):
        if form.is_valid():
            print("Formulário Válido")
            email = form.cleaned_data.get('email')
            

        else:
            print("Formulário não Válido")
    else:
        return render(request, 'login.html', {'form': form})


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
