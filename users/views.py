from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model, login, authenticate, logout


def home(request):
    return render(request, 'users/home.html')


def register(request):
    if request.method == 'POST':
        email = request.POST["email"]
        password = request.POST["password"]
        user = get_user_model()

        user_created = user.objects.create(
            email=email,
        )
        user_created.set_password(password)
        user_created.save()
        return redirect(reverse('login'))
    return render(request, 'users/register.html')


def login(request):
    if request.method == 'POST':
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(username=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login realizado com sucesso!')
            return redirect('list_articles')
        else:
            messages.warning(request, 'Usuário ou senha inválidos!')
    return render(request, 'users/login.html')


def logout(request):
    logout(request)
    return render(request, 'users/logout.html')
