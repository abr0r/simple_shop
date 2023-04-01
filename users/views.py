from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from users.forms import LoginForm


def login(request):
    context = {
        'title': 'AngrenShop - Авторизация'
    }
    return render(request, 'users/login.html', context)


def register(request):
    context = {
        'title': 'AngrenShop - Регистрация'
    }
    return render(request, 'users/register.html', context)
