from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListarAnuncios.as_view(), name='listar_anuncios'),
    path('editar/<int:pk>/', views.EditarAnuncio.as_view(), name='editar_anuncio'),
    path('deletar/<int:pk>/', views.DeletarAnuncio.as_view(), name='deletar_anuncio'),
]
