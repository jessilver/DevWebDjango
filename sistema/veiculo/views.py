from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views import View
from veiculo.models import *

# ListView é um mixin que permite listar objetos de um modelo

class ListarVeiculos(ListView):
    model = Veiculo
    context_object_name = 'veiculos'
    template_name = 'veiculos/listar.html'