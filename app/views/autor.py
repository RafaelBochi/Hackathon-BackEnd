from rest_framework.viewsets import ModelViewSet

from app.models import Autor
from app.serializers import AutorSerializer

class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    