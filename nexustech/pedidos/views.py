from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.db import transaction
from django.db.models import F
from catalogo.models import ItemCatalogo
from .models import Pedido

class CompraView(LoginRequiredMixin, View):
    def get(self, request, item_id):
        item = get_object_or_404(ItemCatalogo, pk=item_id)
        
        if not item.is_disponivel:
            messages.error(request, f"O item '{item.nome}' está esgotado no momento.")
            return redirect('index')

        context = {'item': item}
        return render(request, 'pedidos/compra.html', context)

    def post(self, request, item_id):
        item = get_object_or_404(ItemCatalogo, pk=item_id)

        try:
            quantidade = int(request.POST.get('quantidade', 1))
            if quantidade <= 0:
                raise ValueError
        except ValueError:
            messages.error(request, "A quantidade deve ser um número inteiro positivo.")
            return redirect('compra', item_id=item.id)

        try:
            with transaction.atomic():
                item_para_atualizar = ItemCatalogo.objects.select_for_update().get(pk=item_id)
                
                if item_para_atualizar.estoque < quantidade:
                    messages.error(request, f"Estoque insuficiente para {quantidade} unidades de '{item.nome}'. Disponível: {item_para_atualizar.estoque}.")
                    return redirect('compra', item_id=item.id)

                Pedido.objects.create(
                    usuario=request.user,
                    produto=item_para_atualizar,
                    quantidade=quantidade,
                )

                item_para_atualizar.estoque = F('estoque') - quantidade
                item_para_atualizar.save()

            messages.success(request, f"Compra finalizada com sucesso! Você adquiriu {quantidade} unidade(s) de '{item.nome}'.")
            return redirect('perfil')

        except Exception as e:
            messages.error(request, f"Ocorreu um erro inesperado ao processar o pedido: {e}")
            return redirect('compra', item_id=item.id)