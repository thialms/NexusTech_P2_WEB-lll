from django.db import models


class Pagina(models.Model):
    nome_do_site = models.CharField(max_length=200, verbose_name="Nome do Site/Empresa")
    logo_do_site = models.ImageField(
        upload_to='institucional/logos/', 
        blank=True, 
        null=True,
        verbose_name="Logo (Opcional)"
    )
    
    texto_chamada = models.TextField(verbose_name="Texto de Chamada da Página Inicial", help_text="Exibido em destaque no topo.")
    texto_sobre = models.TextField(verbose_name="Texto Sobre a Empresa/Site")
    imagem_sobre = models.ImageField(
        upload_to='institucional/sobre/', 
        verbose_name="Imagem Sobre (Exibida ao lado do texto)"
    )

    endereco = models.CharField(max_length=255, verbose_name="Endereço Físico")
    email = models.EmailField(max_length=100, verbose_name="E-mail de Contato")
    whatsapp = models.CharField(max_length=20, verbose_name="WhatsApp para Contato", help_text="Ex: +55 (11) 98765-4321")
    maps_embed = models.TextField(
        blank=True,
        null=True,
        verbose_name="Embed do Google Maps",
        help_text="Cole aqui o código iframe de embed do Google Maps (opcional)."
    )

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Página Institucional"
        verbose_name_plural = "Página Institucional"

    def __str__(self):
        return self.nome_do_site

    def save(self, *args, **kwargs):
        if self._state.adding and Pagina.objects.exists():
            return
        super().save(*args, **kwargs)


class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    mensagem = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Mensagem de Contato"
        verbose_name_plural = "Mensagens de Contato"
        ordering = ['-criado_em']

    def __str__(self):
        return f"Mensagem de {self.nome} ({self.email})"