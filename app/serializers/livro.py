from rest_framework.serializers import ModelSerializer

from app.models import Livro

class LivroSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"
        depth = 1