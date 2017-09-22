# Django
from django.shortcuts import render
from django.views.generic.edit import DeleteView, UpdateView
from django.urls import reverse_lazy

# local Django
from .models import HealthProfessional
from .models import User
from .models import Patient
from .forms import HealthProfessionalForm, PatientForm, UserForm, UpdateUserForm


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


def register_patient(request):
    user_form = UserForm(request.POST or None)
    patient_form = PatientForm(request.POST or None)
    context = {
        'patient_form': patient_form,
        'user_form': user_form
    }

    if user_form.is_valid() and patient_form.is_valid():
        email = user_form.cleaned_data.get('email')
        password = user_form.cleaned_data.get('password')
        name = user_form.cleaned_data.get('name')
        sex = user_form.cleaned_data.get('sex')
        phone = user_form.cleaned_data.get('phone')
        date_of_birth = user_form.cleaned_data.get('date_of_birth')
        id_document = patient_form.cleaned_data.get('id_document')

        User.objects.create_user(
            email=email, password=password, name=name,
            sex=sex, date_of_birth=date_of_birth, phone=phone)

        user = User.objects.get(email=email)

        patient = Patient(user=user, id_document=id_document)

        patient.save()

    return render(request, 'register_patient.html', context)


def view_patient(request):
    patients = Patient.objects.all()
    context = {
        'patient': patients
    }
    return render(request, 'view_patient.html', context)

class DeletePatient(DeleteView):
    model = Patient
    success_url = reverse_lazy('view')
    template_name = 'patient_confirm_delete.html'

class UpdatePatient(UpdateView):
    model = User
    form_class = UpdateUserForm
    success_url = reverse_lazy('view')
    template_name = 'edit_patient.html'
