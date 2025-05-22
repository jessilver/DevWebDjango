from jessilver_django_seed.seeders.BaseSeeder import BaseSeeder
from veiculo.models import Veiculo

class VeiculosSeeder(BaseSeeder):
    @property
    def seeder_name(self):
        return 'VeiculosSeeder'

    def seed(self):
        veiculos_data = [
            {
                'combustivel': 1,
                'modelo': 'Fusca',
                'marca': 4,
                'cor': 1,
                'ano': 1970,
                'foto': 'veiculo/fotos/fusca.jpeg'
            },
            {
                'combustivel': 2,
                'modelo': 'Civic',
                'marca': 5,
                'cor': 2,
                'ano': 2020,
                'foto': 'veiculo/fotos/civic.jpeg'
            },
            {
                'combustivel': 3,
                'modelo': 'Corolla',
                'marca': 6,
                'cor': 3,
                'ano': 2021,
                'foto': 'veiculo/fotos/corola.jpeg'
            },
            {
                'combustivel': 4,
                'modelo': 'Palio',
                'marca': 3,
                'cor': 4,
                'ano': 2019,
                'foto': 'veiculo/fotos/palio.jpeg'
            }
        ]

        for veiculo_data in veiculos_data:
            Veiculo.objects.create(**veiculo_data)
        self.succes('Todos os veículos foram criados com sucesso.')