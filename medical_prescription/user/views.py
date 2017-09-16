from django.shortcuts import render, redirect, get_object_or_404
from user.models import Patient
from user.forms import PatientRegisterForm


def patient_view(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    template_name = ''
    context = {
        'patient': patient
    }
    return render(request, template_name, context)


def patient_register(request):
    template_name = 'templates/register.html'
    template_redirect = 'templates/register-sucess.html'

    if request.method == "POST":
        form = PatientRegisterForm(request.POST)

        if form.is_valid():
            patient = form.save(commit=False)
            patient.name = form.cleaned_data.get('name')
            patient.password = form.cleaned_data.get('password')
            patient.password_confirmation = form.cleaned_data.get('pass_conf')
            patient.date_of_birth = form.cleaned_data.get('date_of_birth')
            patient.phone = form.cleaned_data.get('phone')
            patient.sex = form.cleaned_data.get('sex')
            patient.id_document = form.cleaned_data.get('id_document')
            patient.save()
            return redirect(template_redirect)
        else:
            # Nothing to do.
            pass
    else:
        form = PatientRegisterForm()
    context = {
        'form': form
    }
    return render(request, template_name, context)


def patient_edit(request, pk):
    template_name = ''
    template_redirect = ''
    patient = get_object_or_404(Patient, pk=pk)

    if request.method == "POST":
        form = PatientRegisterForm(request.POST, instance=patient)

        if form.is_valid():
            patient.name = form.cleaned_data.get('name')
            patient.password = form.cleaned_data.get('password')
            patient.password_confirmation = form.cleaned_data.get('pass_conf')
            patient.date_of_birth = form.cleaned_data.get('date_of_birth')
            patient.phone = form.cleaned_data.get('phone')
            patient.sex = form.cleaned_data.get('sex')
            patient.id_document = form.cleaned_data.get('id_document')
            patient.save()
            return redirect(template_redirect)
        else:
            # Nothing to do.
            pass
    else:
        form = PatientRegisterForm(instance=patient)
    context = {
        'form':
        form
    }
    return render(request, template_name, context)
