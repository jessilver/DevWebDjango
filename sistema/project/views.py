# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

class Index(View):
    def get(self, request):
        return redirect('login')

class Login(View):
    def get(self, request):

        context = {
            'title': 'Login',
        }

        return render(request, 'login.html', context)
    
    def post(self, request):
        pass