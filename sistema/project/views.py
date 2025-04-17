# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout

from django.conf import settings

class Index(View):
    def get(self, request):
        if not request.user.is_authenticated:  
            return redirect('login')
        return render(request, 'index.html')

class Login(View):
    def get(self, request):

        if request.user.is_authenticated:  
            return redirect('index')

        context = {
            'title': 'Login',
        }

        return render(request, 'login.html', context)
    
    def post(self, request):

        mensagem = {}

        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('listar_veiculos')
            mensagem['tag'] = 'danger'
            mensagem['content'] = 'Usuário inativo.'
            return render(request, 'login.html', {'mensagem': mensagem})
        else:
            mensagem['tag'] = 'danger'
            mensagem['content'] = 'Usuário ou senha incorretos.'
            return render(request, 'login.html', {'mensagem': mensagem})

class Logout(View):
    def get(self, request):
        logout(request)
        return redirect(settings.LOGIN_URL)
    def post(self, request):
        pass