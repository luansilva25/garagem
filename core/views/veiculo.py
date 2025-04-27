from core.models import Veiculo
from core.serializers import VeiculoSerializer
from rest_framework.viewsets import ModelViewSet

class VeiculoViewSet(ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer
