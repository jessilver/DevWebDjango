from django import forms
from .models import Anuncio

class AnuncioForm(forms.ModelForm):
    class Meta:
        model = Anuncio
        fields = ['veiculo', 'titulo', 'descricao', 'preco']
        widgets = {
            'veiculo': forms.Select(attrs={'class': 'form-control'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o título do anúncio'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Digite a descrição do anúncio', 'rows': 3}),
            'preco': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Digite o preço'}),
        }
        labels = {
            'veiculo': 'Veículo',
            'titulo': 'Título do Anúncio',
            'descricao': 'Descrição',
            'preco': 'Preço',
        }