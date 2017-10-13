# Django
from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView

# Local Django
from user.forms import UpdatePasswordForm


class UpdateUserPassword(UpdateView):

    def edit_password_view(request, email):
        form = UpdatePasswordForm(user=request.user, data=request.POST or None)

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
                # Nothing to do.
                pass
        else:
            # Nothing to do.
            pass

        return render(request, 'edit_health_professional_password.html', {'form': form})
