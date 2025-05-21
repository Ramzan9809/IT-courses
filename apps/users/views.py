from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.db import IntegrityError
from django.contrib.auth import authenticate, login as user_login, logout as user_logout, get_user_model
from apps.courses.models import Category


User = get_user_model()


def login_view(request):
     category = Category.objects.all()[:6]
     if request.method == 'POST':
         login = request.POST.get('login')
         password = request.POST.get('password')
         usr = authenticate(request, username=login, password=password)
         if usr is not None:
             user_login(request, usr)
             return HttpResponseRedirect('/')
         else:
             return render(request, 'auth/login.html', {'error':'Неверный логин или пароль', 'category':category})
     return render(request, 'auth/login.html', {'category':category})


def reg_view(request):
    if request.method == 'POST':
        login = request.POST.get('login')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password != password2:
            return render(request, 'auth/register.html', {'error': 'Пароли не совпадают'})

        if len(password) < 6:
            return render(request, 'auth/register.html', {'error': 'Пароль должен содержать минимум 6 символов'})

        if User.objects.filter(username=login).exists():
            return render(request, 'auth/register.html', {'error': 'Пользователь с таким логином уже существует'})

        if User.objects.filter(email=email).exists():
            return render(request, 'auth/register.html', {'error': 'Email уже используется'})

        try:
            user = User.objects.create_user(username=login, email=email, password=password)
            user_login(request, user)
            return redirect('home')
        except IntegrityError:
            return render(request, 'auth/register.html', {'error': 'Ошибка при создании пользователя'})

    return render(request, 'auth/register.html')



def logout_view(request):
    user_logout(request)
    return HttpResponseRedirect('/')

def forgot(request):
    if request.method == "POST":
        email = request.POST.get("email")
        user = User.objects.filter(email=email).first()

        if user:
            return redirect('password_reset_done')
        else:
            return render(request, "auth/forgot.html", {"error": "Пользователь с таким email не найден"})

    return render(request, "auth/forgot.html")
