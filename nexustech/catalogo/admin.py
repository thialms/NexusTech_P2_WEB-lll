from django.contrib import admin
from .models import ItemCatalogo

@admin.register(ItemCatalogo)
class ItemCatalogoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'id', 'preco', 'estoque', 'is_disponivel', 'criado_em')
    list_filter = ('criado_em', 'atualizado_em', 'estoque')
    search_fields = ('nome', 'descricao')
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('nome', 'descricao', 'foto')
        }),
        ('Controle de Vendas', {
            'fields': ('preco', 'estoque'),
            'classes': ('wide', 'extrapretty'), 
        }),
    )

