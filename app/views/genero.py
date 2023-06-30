from rest_framework.viewsets import ModelViewSet

from app.models import Genero
from app.serializers import GeneroSerializer

class GeneroViewSet(ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer
    