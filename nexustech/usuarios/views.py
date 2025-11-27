from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import UsuarioCustomizado
from .forms import CustomUserCreationForm
from pedidos.models import Pedido

class CadastroView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'usuarios/cadastro.html'
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        messages.success(self.request, "Cadastro realizado com sucesso! Faça login para continuar.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Erro no formulário de cadastro. Verifique os campos.")
        return super().form_invalid(form)


class CustomLoginView(LoginView):
    template_name = 'usuarios/login.html'
    
    def form_invalid(self, form):
        messages.error(self.request, "Nome de usuário ou senha inválidos. Tente novamente.")
        return super().form_invalid(form)


class PerfilView(LoginRequiredMixin, DetailView):
    """Exibe o perfil do usuário e seu histórico de pedidos."""
    
    model = UsuarioCustomizado
    template_name = 'usuarios/perfil.html'
    context_object_name = 'usuario'
    
    def get_object(self):
        return self.request.user
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['pedidos'] = Pedido.objects.filter(usuario=self.request.user).order_by('-data')
        
        return context
    
    