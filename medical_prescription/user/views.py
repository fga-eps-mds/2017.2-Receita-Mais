from django.shortcuts import render, render_to_response, redirect
from django.contrib import auth
from django import forms
from .forms import UserLoginForm


#render html login
def login_view(request):
    '''
        Render Login template.
    '''

    form = UserLoginForm(request.POST)

    if form.is_valid() :
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email = email, password = password)


        if user is not None:
            if user.is_active:
                auth.login(request, user)
                return redirect('erro.html')

            else:
                #Nothing to do.
                pass
        else:
            #Nothing to do.
            pass

        return render_to_response('teste.html')

    return render( request,'login.html',{'form':form} )
