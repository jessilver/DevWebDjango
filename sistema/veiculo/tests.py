from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from datetime import datetime
from veiculo.models import *
from veiculo.forms import *

class TestesModelVeiculo(TestCase):
    def setUp(self):
        self.veiculo = Veiculo.objects.create(
            marca=1, 
            modelo='ABCDE',
            ano=datetime.now().year,
            cor=2,   
            combustivel=3,
        )

    def test_is_new(self):
        self.assertTrue(self.veiculo.veiculo_novo)
        self.veiculo.ano = datetime.now().year - 5
        self.assertFalse(self.veiculo.veiculo_novo)

    def test_year_use(self):
        self.veiculo.ano = datetime.now().year - 10
        self.assertEqual(self.veiculo.anos_de_uso(), 10)

class TesteViewListarVeiculo(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.force_login(self.user)
        self.url = reverse('listar_veiculos')
        Veiculo.objects.create(
            marca=1,
            modelo='ABCDE',
            ano=datetime.now().year,
            cor=2,
            combustivel=3,
        )

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['veiculos']), 1)

class TesteViewCriarVeiculo(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.force_login(self.user)
        self.url = reverse('listar_veiculos')

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'veiculos/listar.html')
        self.assertIsInstance(response.context['form'], VeiculoForm)

        
    def test_post(self):
        data = {
            'marca': 1,
            'modelo': 'ABCDE',
            'ano': datetime.now().year,
            'cor': 2,
            'combustivel': 3,
        }
        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('listar_veiculos'))

        self.assertEqual(Veiculo.objects.count(), 1)
        self.assertEqual(Veiculo.objects.first().modelo, 'ABCDE')


class TesteEditarVeiculo(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.force_login(self.user) 
        self.veiculo = Veiculo.objects.create(
            marca=1,
            modelo='ABCDE',
            ano=datetime.now().year,
            cor=2,
            combustivel=3,
        )
        self.url = reverse('editar_veiculos', kwargs={'pk': self.veiculo.pk})


    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['object'], Veiculo)
        self.assertIsInstance(response.context['form'], VeiculoForm)
        self.assertEqual(response.context['object'].pk, self.veiculo.pk)
        self.assertEqual(response.context['object'].marca, 1)
 
    def test_post(self):
        data = {
            'marca': 2,
            'modelo': 'FGHIJ',
            'ano': datetime.now().year - 5,
            'cor': 3,
            'combustivel': 4,
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('listar_veiculos'))
        self.assertEqual(Veiculo.objects.count(), 1)
        self.assertEqual(Veiculo.objects.first().marca, 2)
        self.assertEqual(Veiculo.objects.first().pk, self.veiculo.pk)

class TesteViewDeletarVeiculo(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.force_login(self.user)
        self.veiculo = Veiculo.objects.create(
            marca=1,
            modelo='ABCDE',
            ano=datetime.now().year,
            cor=2,
            combustivel=3,
        )
        self.url = reverse('deletar_veiculos', kwargs={'pk': self.veiculo.pk})

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['object'], Veiculo)
        self.assertEqual(response.context['object'].pk, self.veiculo.pk)

    def test_post(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('listar_veiculos'))
        self.assertEqual(Veiculo.objects.count(), 0)
