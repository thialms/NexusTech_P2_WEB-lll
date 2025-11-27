from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UsuarioCustomizado

@admin.register(UsuarioCustomizado)
class UsuarioCustomizadoAdmin(UserAdmin):
    model = UsuarioCustomizado
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff']

