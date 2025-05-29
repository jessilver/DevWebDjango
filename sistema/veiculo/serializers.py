from rest_framework import serializers
from .models import Veiculo
from datetime import datetime

class VeiculoSerializer(serializers.ModelSerializer):

    marca_display = serializers.SerializerMethodField()
    cor_display = serializers.SerializerMethodField()
    combustivel_display = serializers.SerializerMethodField()

    class Meta:
        model = Veiculo
        exclude = []
        fields = '__all__'
        read_only_fields = ['id', 'foto']
    
    def validate_ano(self, value):
        if value < 1886 or value > datetime.now().year + 1:
            raise serializers.ValidationError("Ano inválido.")
        return value
    
    def validate(self, attrs):
        if not attrs.get('modelo'):
            raise serializers.ValidationError("O modelo é obrigatório.")
        return attrs
    
    def get_marca_display(self, obj):
        return obj.get_marca_display() if obj.marca else None
        # return display.capitalize() if display else None

    def get_cor_display(self, obj):
        return obj.get_cor_display() if obj.cor else None
        # return display.capitalize() if display else None

    # pode ser usado para recalcular o preço ou outras lógicas de negócio   
    def get_combustivel_display(self, obj):
        return obj.get_combustivel_display() if obj.combustivel else None
        # return display.capitalize() if display else None