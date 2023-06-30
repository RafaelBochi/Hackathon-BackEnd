from rest_framework.viewsets import ModelViewSet

from app.models import CarrinhoLivro
from app.serializers import CarrinhoLivroSerializer, CarrinhoLivroSerializerCreate

class CarrinhoLivroViewSet(ModelViewSet):
    queryset = CarrinhoLivro.objects.all()
    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return CarrinhoLivroSerializerCreate
        return CarrinhoLivroSerializer
    
