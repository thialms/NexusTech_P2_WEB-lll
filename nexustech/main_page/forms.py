from django import forms
from institucional.models import Contato

class ContatoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'w-full px-4 py-3 bg-slate-900 border border-slate-700 rounded-lg text-white placeholder-slate-500 focus:ring-2 focus:ring-cyan-500 focus:border-transparent transition duration-150',
                'placeholder': field.label
            })
        self.fields['mensagem'].widget.attrs.update({'rows': 4})

    class Meta:
        model = Contato
        fields = ['nome', 'email', 'mensagem']
        labels = {
            'nome': 'Seu Nome Completo',
            'email': 'Seu Melhor E-mail',
            'mensagem': 'Sua Mensagem ou Dúvida',
        }