from django.db import models
from django.conf import settings
from catalogo.models import ItemCatalogo
from decimal import Decimal

class Pedido(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='pedidos',
        verbose_name="Comprador"
    )
    
    produto = models.ForeignKey(
        ItemCatalogo, 
        on_delete=models.PROTECT,
        verbose_name="Item Comprado"
    )
    
    quantidade = models.IntegerField(verbose_name="Quantidade", default=1)
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor Total")
    data = models.DateTimeField(auto_now_add=True, verbose_name="Data do Pedido")

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"
        ordering = ['-data']

    def __str__(self):
        return f"Pedido #{self.pk} por {self.usuario.username}"

    def calcular_total(self):
        return self.produto.preco * self.quantidade

    def save(self, *args, **kwargs):
        if not self.total:
            self.total = self.calcular_total()
        super().save(*args, **kwargs)