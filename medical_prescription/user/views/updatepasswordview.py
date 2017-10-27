# Django
from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView
from django.contrib import auth
from django.contrib.auth.decorators import login_required


# Local Django
from user.forms import UpdatePasswordForm
from user.decorators import (
    health_professional_is_account_owner_with_email,
    patient_is_account_owner_with_email
    )


# This class is responsible for making the user password change.
class UpdateUserPassword(UpdateView):

    # This method is responsible for making the patient password change.
    @login_required
    @patient_is_account_owner_with_email
    def edit_patient_password_view(request, email):

        # Getting the corresponding form to make the password change.
        form = UpdatePasswordForm(user=request.user, data=request.POST or None)

        # If the form is completed and valid, the patient password is changed.
        if request.method == "POST":
            if form.is_valid():
                password = form.cleaned_data.get('password')
                user = request.user
                print(user.name)
                user.set_password(password)
                user.save()

                auth.login(request, user)

                return redirect('/dashboard_patient/patient')
            else:
                # Nothing to do.
                pass
        else:
            # Nothing to do.
            pass

        return render(request, 'edit_patient_password.html', {'form': form})

    # This method is responsible for making the health professional password change.
    @login_required
    @health_professional_is_account_owner_with_email
    def edit_health_professional_password_view(request, email):

        # Getting the corresponding form to make the password change.
        form = UpdatePasswordForm(user=request.user, data=request.POST or None)

        # If the form is completed and valid, the health professional password is changed.
        if request.method == "POST":
            if form.is_valid():
                password = form.cleaned_data.get('password')

                user = request.user
                user.set_password(password)
                user.save()

                auth.login(request, user)

                return redirect('/dashboard_health_professional/health_professional')
            else:
                # Nothing to do.
                pass
        else:
            # Nothing to do.
            pass

        return render(request, 'edit_health_professional_password.html', {'form': form})
