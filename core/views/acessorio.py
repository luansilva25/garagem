from core.models import Acessorio
from core.serializers import AcessorioSerializer
from rest_framework.viewsets import ModelViewSet

class AcessorioViewSet(ModelViewSet):
    queryset = Acessorio.objects.all()
    serializer_class = AcessorioSerializer