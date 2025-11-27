from django.views.generic import TemplateView
from institucional.models import Pagina, Contato
from catalogo.models import ItemCatalogo
from .forms import ContatoForm
from django.conf import settings
from django.shortcuts import redirect
from django.contrib import messages
from django.db import IntegrityError
from django.http import HttpResponse


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        try:
            context['pagina'] = Pagina.objects.first() 
        except Pagina.DoesNotExist:
            context['pagina'] = None
            if settings.DEBUG:
                 messages.warning(self.request, "Atenção: Cadastre a Página Institucional no Admin para exibir o conteúdo da Home.")

        context['itens_catalogo'] = ItemCatalogo.objects.filter(estoque__gt=0).order_by('-criado_em')

        context['form_contato'] = ContatoForm()
        
        return context

    def post(self, request, *args, **kwargs):
        form = ContatoForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Sua mensagem foi enviada com sucesso! Em breve entraremos em contato.")
                return redirect('index') 
            except IntegrityError:
                messages.error(request, "Ocorreu um erro ao salvar a mensagem. Tente novamente.")
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Erro no campo {field}: {error}")
            
            context = self.get_context_data()
            context['form_contato'] = form
            return self.render_to_response(context)

        return redirect('index')