# Django
from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User

# Local Django
from user.forms import UpdatePasswordForm


class UpdateUserPassword(UpdateView):

    def edit_password_view(request, email):
        form = UpdatePasswordForm(user=request.user, data=request.POST or None)
        print("Renderizando password")

        if request.method == "POST":
            print("Solicitado")
            if form.is_valid():
                password = form.cleaned_data.get('new_password')
                user = request.user
                print(user.name)
                user.set_password(password)
                user.save()
                print("password atualizado")

                return redirect('/')
            else:
                print("form invalid")
                # Nothing to do.
                pass
        else:
            # Nothing to do.
            pass

        return render(request, 'editpassword.html', {'form': form})
