# Django
from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView

# Local Django
from user.forms import UpdatePasswordForm


# This class is responsible for making the user password change.
class UpdateUserPassword(UpdateView):

    # This method is responsible for making the patient password change.
    def edit_patient_password_view(request, email):

        # Getting the corresponding form to make the password change.
        form = UpdatePasswordForm(user=request.user, data=request.POST or None)

        # If the form is completed and valid, the patient password is changed.
        if request.method == "POST":
            if form.is_valid():
                password = form.cleaned_data.get('new_password')
                user = request.user
                print(user.name)
                user.set_password(password)
                user.save()

                return redirect('/')
            else:
                # Nothing to do.
                pass
        else:
            # Nothing to do.
            pass

        return render(request, 'edit_patient_password.html', {'form': form})

    # This method is responsible for making the health professional password change.
    def edit_health_professional_password_view(request, email):

        # Getting the corresponding form to make the password change.
        form = UpdatePasswordForm(user=request.user, data=request.POST or None)

        # If the form is completed and valid, the health professional password is changed.
        if request.method == "POST":
            print("Solicitado")
            if form.is_valid():
                password = form.cleaned_data.get('new_password')
                user = request.user
                print(user.name)
                user.set_password(password)
                user.save()

                return redirect('/')
            else:
                print("invalido")
                # Nothing to do.
                pass
        else:
            # Nothing to do.
            pass

        return render(request, 'edit_health_professional_password.html', {'form': form})
