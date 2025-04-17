from django.db import models
from veiculo.consts import *

class Veiculo(models.Model):
    combustivel = models.SmallIntegerField(choices=OPCOES_COMBUSTIVEIS, verbose_name='Combustível')
    modelo = models.CharField(max_length=100, verbose_name='Modelo')
    marca = models.SmallIntegerField(choices=OPCOES_MARCAS, verbose_name='Marca')
    cor = models.SmallIntegerField(choices=OPCOES_CORES, verbose_name='Cor')
    ano = models.IntegerField(verbose_name='Ano')
