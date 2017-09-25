import hashlib
import datetime
import random

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.core.mail import send_mail
from django.contrib import messages
from django.utils import timezone
from django.views.generic import FormView, View
from django.views.generic.edit import DeleteView, UpdateView
from django.urls import reverse_lazy

from .models import (HealthProfessional,
                     User,
                     ResetPasswordProfile,
                     Patient)
from .forms import (HealthProfessionalForm,
                    UserForm,
                    UpdateUserForm,
                    PatientForm,
                    UserLoginForm,
                    ResetPasswordForm,
                    ConfirmPasswordForm)
from . import constants


class LoginView(FormView):
    '''
    Render and log user.
    '''

    form_class = UserLoginForm
    template_name = 'login.html'

    # Render the login page.
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    # Login user.
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        # Authenticate user.
        if form.is_valid():
            user = auth.authenticate(
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                return self.user_authentication(request, user)
            else:
                return render(request, 'message.html', {"message": "usuário não none"})
        else:
            return render(request, self.template_name, {'form': form})

    # Login valid user.
    def user_authentication(self, request, user):
        if user.is_active:
            auth.login(request, user)
            return render(request, 'home.html')


class ResetPasswordView(FormView):
    '''
    Send an e-mail to reset user password.
    '''
    form_class = ResetPasswordForm
    template_name = 'reset_password.html'

    # Render password reset page.
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    # Get form information.
    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')

        # Search the user in database.
        try:
            user = User.objects.get(email=email)
        except:
            return render(request, 'message.html', {"message": "usuário não encontrado"})

        try:

            # Get informations and create recover key.
            new_profile = self._create_recover_profile(user)
            new_profile.save()

            send_mail(constants.EMAIL_SUBJECT,
                      (constants.EMAIL_BODY % new_profile.activation_key),
                      constants.EMAIL_ADRESS,
                      [email],
                      fail_silently=False)

            messages.success(request, constants.EMAIL_SUCESS_MESSAGE)

            return redirect('/home')
        except:
            messages.error(request, constants.EMAIL_MESSAGE_EXIST)
            return render(request, 'reset_password.html',
                          {"form": form})
        else:
            # nothing to do
            pass

    # Create recover key in database.
    def _create_recover_profile(self, user):
            email = user.email
            # Create a random sha1 code.
            salt = hashlib.sha1(str(random.random()).encode('utf-8')).hexdigest()[:5]

            # Join 'salt' and 'email' to create the activation key.
            activation_key = hashlib.sha1(str(salt+email).encode('utf‌​-8')).hexdigest()

            # Make a expire parameter for the activation key.
            key_expires = datetime.datetime.today() + datetime.timedelta(2)

            new_profile = ResetPasswordProfile(user=user,
                                               activation_key=activation_key,
                                               key_expires=key_expires)

            return new_profile


class ConfirmPasswordView(FormView):
    '''
    Reset the user password.
    '''
    form_class = ConfirmPasswordForm
    template_name = 'password_confirm.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    # Validate key and update the new password of 'User'.
    def post(self, request, activation_key, *args, **kwargs):

        form = ConfirmPasswordForm(request.POST or None)

        # Get reset object.
        user_profile = get_object_or_404(ResetPasswordProfile, activation_key=activation_key)

        user = user_profile.user

        if(request.method == 'POST' and user is not None):
            if(form.is_valid()):
                if(self._validate_activation_key(user_profile)):

                    user_profile.delete()
                    # Change user password and save in database
                    self._save_user_password(user, form)
                    # Change user password and save in database.

                else:
                    return redirect('/')
            else:
                # Nothing to do.
                pass
        else:
            # Nothing to do.
            pass

        return render(request, 'password_confirm.html', {'form': form})

    # Validate key expiration time.
    def _validate_activation_key(self, user_p, *args):
        # Case key expires.
        if(user_p.key_expires < timezone.now()):
            # key expires.
            user_p.delete()
            return False
        else:
            return True

    # Update user password in databe.
    def _save_user_password(self, user, form):
        if(form.is_valid()):
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            return redirect('/')
        else:
            # Nothing to do.
            pass


class LogoutView(View):
    '''
    Logout of User.
    '''

    # Exit user and render 'home' page.
    def get(self, request):
        auth.logout(request)
        return redirect('/home/login')  


def show_homepage(request):
    return render(request, 'home.html')


def register_health_professional(request):
    user_form = UserForm(request.POST or None)
    health_professional_form = HealthProfessionalForm(request.POST or None)
    context = {
        'health_professional_form': health_professional_form,
        'user_form': user_form
    }

    if user_form.is_valid() and health_professional_form.is_valid():
        email = user_form.cleaned_data.get('email')
        password = user_form.cleaned_data.get('password')
        name = user_form.cleaned_data.get('name')
        sex = user_form.cleaned_data.get('sex')
        phone = user_form.cleaned_data.get('phone')
        date_of_birth = user_form.cleaned_data.get('date_of_birth')

        crm = health_professional_form.cleaned_data.get('crm')
        crm_state = health_professional_form.cleaned_data.get('crm_state')

        User.objects.create_user(
            email=email, password=password, name=name,
            sex=sex, date_of_birth=date_of_birth, phone=phone)

        user = User.objects.get(email=email)

        health_professional = HealthProfessional(
            user=user, crm=crm, crm_state=crm_state)

        health_professional.save()

    return render(request, 'register_health_professional.html', context)


def view_health_professional(request):
    health_professionals = HealthProfessional.objects.all()
    context = {
        'health_professionals': health_professionals
    }
    return render(request, 'view_health_professional.html', context)


class DeleteHealthProfessional(DeleteView):
    model = HealthProfessional
    success_url = reverse_lazy('view')
    template_name = 'health_professional_confirm_delete.html'


class UpdateHealthProfessional(UpdateView):
    model = User
    form_class = UpdateUserForm
    success_url = reverse_lazy('view')
    template_name = 'edit_health_professional.html'


def register_patient(request):
    patient_form = PatientForm(request.POST or None)
    context = {
        'patient_form': patient_form
        }

    if patient_form.is_valid():
        email = patient_form.cleaned_data.get('email')
        password = patient_form.cleaned_data.get('password')
        name = patient_form.cleaned_data.get('name')
        sex = patient_form.cleaned_data.get('sex')
        phone = patient_form.cleaned_data.get('phone')
        date_of_birth = patient_form.cleaned_data.get('date_of_birth')
        id_document = patient_form.cleaned_data.get('id_document')

        Patient.objects.create_user(email=email, password=password, name=name,
                                    sex=sex, date_of_birth=date_of_birth,
                                    phone=phone, id_document=id_document)

    return render(request, 'register_patient.html', context)


def view_patient(request):
    patients = Patient.objects.all()
    print(patients)
    context = {
        'patients': patients
    }
    return render(request, 'view_patient.html', context)


class UpdatePatient(UpdateView):
    model = Patient
    form_class = UpdateUserForm
    success_url = reverse_lazy('view')
    template_name = 'edit_patient.html'
