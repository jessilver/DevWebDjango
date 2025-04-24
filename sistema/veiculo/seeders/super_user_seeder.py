from jessilver_django_seed.seeders.BaseSeeder import BaseSeeder
from django.contrib.auth.models import User

class SuperUserSeeder(BaseSeeder):
    @property
    def seeder_name(self):
        return 'SuperUserSeeder'

    def seed(self):
        if not User.objects.filter(is_superuser=True).exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='05052005',
                first_name='Admin',
                last_name='User'
            )
            self.succes(f'Super User Criado com sucesso')
        else:
            self.error(f'Super User já existe')