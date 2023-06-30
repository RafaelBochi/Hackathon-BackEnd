from rest_framework.viewsets import ModelViewSet

from app.models import Livro
from app.serializers import LivroSerializer

class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    