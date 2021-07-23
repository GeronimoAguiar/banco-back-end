from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.models import Conta
from .serializers import ContaSerializer



class ContaViewSet(ModelViewSet):
    queryset = Conta.objects.all()
    serializer_class = ContaSerializer

    @action(methods=['put'], detail=True)
    def transacao(self, request, pk):
        return Response({'Hello': pk})

""" def get_queryset(self):
    return Conta.objects.all()

def list(self, request, *args, **kwargs):
    return Response({'Hello': request.data['nome']})

def create(self, request, *args, **kwargs):
    return Response({'Hello': request.data['nome']})

def destroy(self, request, *args, **kwargs):
    pass

def retrieve(self, request, *args, **kwargs):
    pass

def update(self, request, *args, **kwargs):
    pass

def partial_update(self, request, *args, **kwargs):
    pass

@action(methods=['get'], detail=True)
def denunciar(self, request, pk):
    pass"""
