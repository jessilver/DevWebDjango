from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views import View
from veiculo.models import *
# Create your views here.

class ListarVeiculos(ListView):

    model = Veiculo
    context_object_name = 'veiculos'
    template_name = 'veiculos/listar.html'

    def get(self, request):
        return render(request, self.template_name)
    def post(self, request):
        pass
