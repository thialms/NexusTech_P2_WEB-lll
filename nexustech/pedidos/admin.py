from django.contrib import admin
from .models import Pedido

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = (
        'produto', 
        'id',
        'usuario', 
        'quantidade', 
        'total', 
        'data'
    )

    list_filter = (
        'data', 
        'usuario'
    )

    search_fields = (
        'produto__nome',
        'usuario__username', 
        'pk'
    )
    
    readonly_fields = (
        'usuario', 
        'produto', 
        'quantidade', 
        'total', 
        'data'
    )
    
    ordering = ('-data',)

    def has_add_permission(self, request):
        return False