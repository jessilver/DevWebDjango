from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import View
from .models import Anuncio
from .forms import AnuncioForm
from .serializers import AnuncioSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework import permissions

class ListarAnuncios(LoginRequiredMixin, View):
    template_name = 'anuncios/listar.html'
    form_class = AnuncioForm
    context_object_name = 'anuncios'

    def get(self, request, *args, **kwargs):
        anuncios = Anuncio.objects.all()

        context = {
            'form': self.form_class(),
            'anuncios': anuncios,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_anuncios')
        anuncios = Anuncio.objects.all()
        return render(request, self.template_name, {'anuncios': anuncios, 'form': form})

class EditarAnuncio(LoginRequiredMixin, UpdateView):
    model = Anuncio
    form_class = AnuncioForm
    template_name = 'anuncios/editar.html'
    success_url = reverse_lazy('listar_anuncios')

class DeletarAnuncio(LoginRequiredMixin, DeleteView):
    model = Anuncio
    template_name = 'anuncios/deletar.html'
    success_url = reverse_lazy('listar_anuncios')


class AnuncioListCreateView(ListCreateAPIView):
    serializer_class = AnuncioSerializer
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Anuncio.objects.all()

class AnuncioRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = AnuncioSerializer
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Anuncio.objects.all()