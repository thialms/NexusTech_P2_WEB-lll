from django.db import models
from decimal import Decimal

class ItemCatalogo(models.Model):
    nome = models.CharField(max_length=255, verbose_name="Título / Nome do Item")
    estoque = models.IntegerField(default=0, verbose_name="Estoque Disponível")
    
    preco = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        default=Decimal('0.00'), 
        verbose_name="Preço (R$)"
    )
    
    descricao = models.TextField(verbose_name="Descrição Detalhada do Item")
    foto = models.ImageField(
        upload_to='catalogo/itens/', 
        verbose_name="Capa / Foto do Item"
    )
    
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Item de Catálogo"
        verbose_name_plural = "Itens do Catálogo"
        ordering = ['nome']

    def __str__(self):
        return self.nome
    
    @property
    def is_disponivel(self):
        """Propriedade que retorna se o item está em estoque."""
        return self.estoque > 0