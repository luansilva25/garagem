from core.models import Modelo
from core.serializers import ModeloSerializer
from rest_framework.viewsets import ModelViewSet

class ModeloViewSet(ModelViewSet):
    queryset = Modelo.objects.all()
    serializer_class = ModeloSerializer