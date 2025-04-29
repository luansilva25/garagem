from django.db import models
from core.models import Cor, Modelo, Acessorio

class Veiculo(models.Model):
    ano = models.IntegerField(default=0, blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True, null=True)
    acessorio = models.ManyToManyField(Acessorio, blank=True, related_name='veiculos')
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, null=True, blank=True, related_name='veiculos')
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT, null=True, blank=True, related_name='veiculos')

    def __str__(self):
        return f'({self.id}) - {self.modelo.nome} - {self.cor.nome} - {self.ano}'