from core.models import Cor
from core.serializers import CorSerializer
from rest_framework.viewsets import ModelViewSet

class CorViewSet(ModelViewSet):
    queryset = Cor.objects.all()
    serializer_class = CorSerializer
