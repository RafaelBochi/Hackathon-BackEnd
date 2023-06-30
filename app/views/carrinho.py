from rest_framework.viewsets import ModelViewSet

from app.models import Carrinho
from app.serializers import CarrinhoSerializer

class CarrinhoViewSet(ModelViewSet):
    queryset = Carrinho.objects.all()
    serializer_class = CarrinhoSerializer
    