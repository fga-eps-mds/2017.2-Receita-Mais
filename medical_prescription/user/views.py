from django.shortcuts import render, render_to_response
from django import forms
from .forms import UserLoginForm

#render html login
def login_view(request):
    '''
        Render Login template.
    '''

    form = UserLoginForm(request.POST)

    if form.is_valid() :
        form.email=request.POST['email']
        form.password = request.POST['password']

        return render_to_response('teste.html')

    return render( request,'login.html',{'form':form} )
