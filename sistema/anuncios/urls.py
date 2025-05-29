from django.urls import path
from anuncios.views import *

urlpatterns = [
    path('', ListarAnuncios.as_view(), name='listar_anuncios'),
    path('editar/<int:pk>/', EditarAnuncio.as_view(), name='editar_anuncio'),
    path('deletar/<int:pk>/', DeletarAnuncio.as_view(), name='deletar_anuncio'),

    path('api/licr/', AnuncioListCreateView.as_view(), name='anuncio_listar_create_api'),
    path('api/upde/<int:pk>', AnuncioRetrieveUpdateDestroyView.as_view(), name='anuncio_update_destroy_api'),
]
