from django.shortcuts import render, render_to_response, redirect
from django.contrib import auth

from .forms import UserLoginForm

# import for test.
from .models import User


# render html login.


def login_view(request):
    '''
    Render Login template.
    '''
    form = UserLoginForm(request.POST or None)

    if form.is_valid():

        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')

        # begin authenticate MOC- Remove-me

        user = None
        # if the password and emails is authentic, create a user and set user.is_active=True.
        if('teste@gmail.com' == email and 'senha' == password):
            user = User()
            user.password = email
            user.email = password
            user.is_active = False
        else:
            # Nothing to do.
            pass
        # end debugger MOC

        # if user is activate, redirect for login again.
        if(user is not None):
            if user.is_active:
                # auth.login(request, user)
                return render_to_response('message.html', {'message': 'Usuário já estava ativado'})
            else:
                return render_to_response('message.html', {'message': 'O usuário foi autenticado'})

        else:
            # Not authenticate
            return render_to_response('message.html', {'message': 'Usuário não foi autenticado'})

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    auth.logout(request)
    return redirect('/home')
