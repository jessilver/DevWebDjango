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
                'marca': 1,
                'cor': 1,
                'ano': 1970
            },
            {
                'combustivel': 2,
                'modelo': 'Civic',
                'marca': 2,
                'cor': 2,
                'ano': 2020
            },
            {
                'combustivel': 3,
                'modelo': 'Corolla',
                'marca': 3,
                'cor': 3,
                'ano': 2021
            }
        ]

        for veiculo_data in veiculos_data:
            Veiculo.objects.create(**veiculo_data)
        self.succes('Todos os veículos foram criados com sucesso.')