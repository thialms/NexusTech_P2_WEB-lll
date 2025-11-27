from django.urls import path
from django.contrib.auth import views as auth_views
from .views import CadastroView, CustomLoginView, PerfilView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('cadastro/', CadastroView.as_view(), name='cadastro'),
    path('perfil/', PerfilView.as_view(), name='perfil'),
]