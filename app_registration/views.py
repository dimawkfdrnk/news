from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.db import transaction
from django.contrib.auth.models import User



@transaction.atomic()
def registration_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Аккаунт успешно создан!')
            return redirect('login_user')
        else:
            messages.warning(request, f'Ошибка регистрации, проверьте правильность введенных данных.')

    else:
        form = UserCreationForm()
    return render(request, 'registration/registration_user.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        request.session['username_session'] = request.POST
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main_page')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login_user.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('main_page')