from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.models import Conta
from .serializers import ContaSerializer



class ContaViewSet(ModelViewSet):

    serializer_class = ContaSerializer

    def get_queryset(self):
        conta = self.request.query_params.get('conta', None)
        titular = self.request.query_params.get('titular', None)
        queryset = Conta.objects.all()

        if conta:
            queryset = Conta.objects.filter(pk=conta)

        if titular:
            queryset = queryset.filter(titular=titular)

        return queryset

    def list(self, request, *args, **kwargs):
        return super(ContaViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(ContaViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(ContaViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(ContaViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(ContaViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(ContaViewSet, self).partial_update(request, *args, **kwargs)

    @action(methods=['get'], detail=True)
    def denunciar(self, request, pk):
        pass
