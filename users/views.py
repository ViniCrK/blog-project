from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model, login, authenticate, logout


def home(request):
    return render(request, 'users/home.html')


def register_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = get_user_model()

        user_created = user.objects.create(
            username=username,
            email=email,
        )
        user_created.set_password(password)
        user_created.save()
        return redirect(reverse('login'))
    return render(request, 'users/register.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, 'Login realizado com sucesso!')
            return redirect(reverse('home'))
        else:
            messages.warning(request, 'Usuário ou senha inválidos!')
    return render(request, 'users/login.html')


def logout_user(request):
    logout(request)
    return redirect('login')
