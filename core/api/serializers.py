from rest_framework.serializers import ModelSerializer
from core.models import Conta

class ContaSerializer(ModelSerializer):
    class Meta:
        model = Conta
        fields = ('conta', 'titular', 'tipo', 'saldo', 'limite', 'fatura')