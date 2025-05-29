from django.urls import path, include
from veiculo.views import *

urlpatterns = [
    path('', ListarVeiculos.as_view(), name='listar_veiculos'),
    path('edit/<int:pk>', EditarVeiculos.as_view(), name='editar_veiculos'),
    path('delete/<int:pk>', DeletarVeiculos.as_view(), name='deletar_veiculos'),
    path('fotos/<str:arquivo>', FotoVeiculo.as_view(), name='foto_veiculo'),
    path('api/', VeiculoListView.as_view(), name='veiculo_listar_api'),

    path('api/licr/', VeiculoListCreateView.as_view(), name='veiculo_listar_create_api'),
    path('api/upde/<int:pk>', VeiculoRetrieveUpdateDestroyView.as_view(), name='veiculo_update_destroy_api'),
]