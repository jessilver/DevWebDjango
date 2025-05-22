# filepath: /home/jesse/codding/github/uft/webmobile/DebWebDjango/sistema/veiculo/forms.py
from django import forms
from veiculo.models import Veiculo
from veiculo.consts import OPCOES_COMBUSTIVEIS, OPCOES_MARCAS, OPCOES_CORES

class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = ['combustivel', 'modelo', 'marca', 'cor', 'ano', 'foto']  # Campos do formulário
        widgets = {
            'modelo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o modelo do veículo'}),
            'ano': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Digite o ano de fabricação'}),
            'combustivel': forms.Select(attrs={'class': 'form-control'}),
            'marca': forms.Select(attrs={'class': 'form-control'}),
            'cor': forms.Select(attrs={'class': 'form-control'}, choices=[]),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'combustivel': 'Tipo de Combustível',
            'modelo': 'Modelo do Veículo',
            'marca': 'Marca',
            'cor': 'Cor',
            'ano': 'Ano de Fabricação',
            'foto': 'Foto do Veículo',
        }