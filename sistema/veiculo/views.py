from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.http import FileResponse, Http404
from django_dump_die.middleware import dd
from django.views.generic.edit import *
from veiculo.forms import VeiculoForm
from django.urls import reverse_lazy
from veiculo.models import Veiculo
from django.views import View

class ListarVeiculos(LoginRequiredMixin,View):
    template_name = 'veiculos/listar.html'
    form_class = VeiculoForm
    context_object_name = 'veiculos'

    def get(self, request, *args, **kwargs):
        veiculos = Veiculo.objects.all()

        context = {
            'form': self.form_class(),
            'veiculos': veiculos,
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()  
            return redirect('listar_veiculos')
        else:
            dd(form.errors)
        veiculos = Veiculo.objects.all()
        return render(request, self.template_name, {'veiculos': veiculos, 'form': form})

class FotoVeiculo(View):
    def get(self, request, arquivo):
        try:
            veiculo = Veiculo.objects.get(foto='veiculo/fotos/{}'.format(arquivo))
            return FileResponse(veiculo.foto)
        except ObjectDoesNotExist:
            raise Http404('Arquivo não encontrado.')
        except Exception as exeption:
            raise exeption
        
class EditarVeiculos(LoginRequiredMixin, UpdateView):
    model = Veiculo
    form_class = VeiculoForm
    template_name = 'veiculos/editar.html'
    success_url = reverse_lazy('listar_veiculos')

class DeletarVeiculos(LoginRequiredMixin, DeleteView):
    model = Veiculo
    template_name = 'veiculos/deletar.html'
    success_url = reverse_lazy('listar_veiculos')
