# Django
from django.shortcuts import redirect
from django.contrib import auth
from django.views.generic import View


class LogoutView(View):
    '''
    Logout of User.
    '''

    # Exit user and render 'home' page.
    def get(self, request):
        auth.logout(request)
        return redirect('/')
