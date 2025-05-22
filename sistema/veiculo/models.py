from django.db import models
from veiculo.consts import *
from datetime import datetime

class Veiculo(models.Model):
    combustivel = models.SmallIntegerField(choices=OPCOES_COMBUSTIVEIS, verbose_name='Combustível')
    modelo = models.CharField(max_length=100, verbose_name='Modelo')
    marca = models.SmallIntegerField(choices=OPCOES_MARCAS, verbose_name='Marca', null=False)
    cor = models.SmallIntegerField(choices=OPCOES_CORES, verbose_name='Cor', null=False)
    ano = models.IntegerField(verbose_name='Ano', null=False)
    foto = models.ImageField(upload_to='veiculo/fotos', verbose_name='Foto', blank=True, null=True)

    class Meta:
        verbose_name = 'Veículo'
        verbose_name_plural = 'Veículos'
        ordering = ['modelo']
        db_table = 'veiculos'

    @property
    def veiculo_novo(self):
        return self.ano == datetime.now().year

    def anos_de_uso(self):
        return datetime.now().year - self.ano
    
    def __str__(self):
        return f"{self.modelo} ({self.ano})"
