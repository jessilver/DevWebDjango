from jessilver_django_seed.seeders.BaseSeeder import BaseSeeder
from anuncios.models import Anuncio
from veiculo.models import Veiculo

class AnunciosSeeder(BaseSeeder):
    @property
    def seeder_name(self):
        return 'AnunciosSeeder'

    def seed(self):
        # Seleciona alguns veículos existentes para associar aos anúncios
        veiculos = list(Veiculo.objects.all())
        if not veiculos:
            self.error('Nenhum veículo encontrado. Rode o seeder de veículos primeiro.')
            return
        anuncios_data = [
            {
            'veiculo': veiculos[0],
            'titulo': 'Fusca à venda',
            'descricao': 'Fusca antigo, bem conservado, ótimo para colecionadores.',
            'preco': 15000.00
            },
            {
            'veiculo': veiculos[1],
            'titulo': 'Civic seminovo',
            'descricao': 'Honda Civic 2020, único dono, baixa quilometragem.',
            'preco': 95000.00
            },
            {
            'veiculo': veiculos[2],
            'titulo': 'Corolla impecável',
            'descricao': 'Toyota Corolla 2021, revisões em dia, sem detalhes.',
            'preco': 110000.00
            },
            {
            'veiculo': veiculos[3],
            'titulo': 'Palio econômico',
            'descricao': 'Fiat Palio 2019, econômico e confortável.',
            'preco': 35000.00
            }
        ]
        for anuncio_data in anuncios_data:
            Anuncio.objects.create(**anuncio_data)
        self.succes('Todos os anúncios foram criados com sucesso.')
