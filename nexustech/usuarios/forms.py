from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UsuarioCustomizado

def estilizar_formulario(form_instance):
    for field_name, field in form_instance.fields.items():
        if field.widget.__class__.__name__ in ['TextInput', 'EmailInput', 'PasswordInput', 'Textarea']:
            field.widget.attrs.update({
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-indigo-500 focus:border-indigo-500 transition duration-150 shadow-sm mt-1',
            })


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = UsuarioCustomizado
        fields = ('username', 'email', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        estilizar_formulario(self)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = UsuarioCustomizado
        fields = ('username', 'email', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        estilizar_formulario(self)