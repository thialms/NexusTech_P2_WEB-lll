import os
import django
import sys
import urllib.request
from django.core.files.base import ContentFile

# Adiciona o diretório atual ao path para encontrar o settings
sys.path.append(os.getcwd())

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'litterae_libri.settings')
django.setup()

from institucional.models import Pagina
from catalogo.models import ItemCatalogo

def download_image(url):
    try:
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        )
        with urllib.request.urlopen(req) as response:
            return response.read()
    except Exception as e:
        print(f"Erro ao baixar imagem {url}: {e}")
        return None

def populate():
    print("Iniciando atualização do banco de dados...")

    # Limpar produtos antigos para garantir imagens corretas
    print("Removendo produtos antigos...")
    ItemCatalogo.objects.all().delete()

    # 1. Atualizar Página Institucional (se necessário)
    pagina, created = Pagina.objects.get_or_create(
        defaults={
            "nome_do_site": "Nexus Tech & Games",
            "texto_chamada": "A Evolução do Seu Setup Começa Aqui",
            "texto_sobre": "Somos a Nexus Tech & Games, líderes em hardware de alta performance e os lançamentos mais aguardados do mundo gamer. Desde 2025, trazemos o futuro da tecnologia para suas mãos.",
            "endereco": "Av. Paulista, 1000 - Loja 42 - São Paulo, SP",
            "email": "contato@nexustech.com.br",
            "whatsapp": "(11) 99999-8888",
            "maps_embed": '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3657.145683257343!2d-46.65496148502223!3d-23.56321028468196!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x94ce59c8da0aa315%3A0xd59f9431f2c9776a!2sAv.%20Paulista%2C%201000%20-%20Bela%20Vista%2C%20S%C3%A3o%20Paulo%20-%20SP%2C%2001310-100!5e0!3m2!1spt-BR!2sbr!4v1625688456789!5m2!1spt-BR!2sbr" width="100%" height="100%" style="border:0;" allowfullscreen="" loading="lazy"></iframe>'
        }
    )
    if not created:
        print("Página Institucional já existe.")

    # 2. Lista de Produtos Curada (Imagens Reais e Confiáveis)
    produtos = [
        {
            "nome": "PlayStation 5",
            "preco": 3799.90,
            "estoque": 15,
            "descricao": "O console da Sony com carregamento ultrarrápido e controle DualSense imersivo.",
            "image_url": "https://images.unsplash.com/photo-1606144042614-b2417e99c4e3?q=80&w=800&auto=format&fit=crop",
            "image_name": "ps5.jpg"
        },
        {
            "nome": "Xbox Series X",
            "preco": 4499.00,
            "estoque": 10,
            "descricao": "O Xbox mais rápido e poderoso de todos os tempos. Jogue milhares de títulos de quatro gerações de consoles.",
            "image_url": "https://images.unsplash.com/photo-1621259182978-fbf93132d53d?q=80&w=800&auto=format&fit=crop",
            "image_name": "xbox.jpg"
        },
        {
            "nome": "Nintendo Switch OLED",
            "preco": 2199.90,
            "estoque": 25,
            "descricao": "Tela OLED vibrante de 7 polegadas. Jogue em qualquer lugar com o modo portátil ou na TV.",
            "image_url": "https://images.unsplash.com/photo-1578303512597-81e6cc155b3e?q=80&w=800&auto=format&fit=crop",
            "image_name": "switch.jpg"
        },
        {
            "nome": "MacBook Pro M3",
            "preco": 18499.00,
            "estoque": 5,
            "descricao": "Desempenho profissional com o chip M3. Bateria para o dia todo e tela Liquid Retina XDR deslumbrante.",
            "image_url": "https://images.unsplash.com/photo-1517336714731-489689fd1ca4?q=80&w=800&auto=format&fit=crop",
            "image_name": "macbook.jpg"
        },
        {
            "nome": "iPad Pro 12.9",
            "preco": 9899.90,
            "estoque": 12,
            "descricao": "A experiência definitiva em tablet. Chip M2, tela XDR e suporte para Apple Pencil.",
            "image_url": "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?q=80&w=800&auto=format&fit=crop",
            "image_name": "ipad.jpg"
        },
        {
            "nome": "NVIDIA RTX 4090",
            "preco": 14999.90,
            "estoque": 3,
            "descricao": "A placa de vídeo mais potente do mundo. Ray Tracing, DLSS 3 e desempenho extremo para 4K.",
            "image_url": "https://images.unsplash.com/photo-1591488320449-011701bb6704?q=80&w=800&auto=format&fit=crop",
            "image_name": "gpu.jpg"
        },
        {
            "nome": "Teclado Mecânico RGB",
            "preco": 899.90,
            "estoque": 40,
            "descricao": "Switches mecânicos táteis e iluminação RGB personalizável para o setup perfeito.",
            "image_url": "https://images.unsplash.com/photo-1595225476474-87563907a212?q=80&w=800&auto=format&fit=crop",
            "image_name": "keyboard.jpg"
        },
        {
            "nome": "Headset Gamer Pro",
            "preco": 599.90,
            "estoque": 30,
            "descricao": "Áudio espacial imersivo e microfone com cancelamento de ruído para comunicação clara.",
            "image_url": "https://images.unsplash.com/photo-1612036782180-6f0b6cd846fe?q=80&w=800&auto=format&fit=crop",
            "image_name": "headset.jpg"
        }
    ]

    for prod_data in produtos:
        # Separa dados do modelo e dados auxiliares
        image_url = prod_data.pop("image_url")
        image_name = prod_data.pop("image_name")
        
        # Cria o produto
        item = ItemCatalogo.objects.create(**prod_data)
        print(f"Criando produto: {item.nome}")
        
        # Baixar e salvar imagem
        img_content = download_image(image_url)
        if img_content:
            item.foto.save(image_name, ContentFile(img_content), save=True)
            print(f"Imagem salva para {item.nome}")

    print("População de dados concluída!")

if __name__ == '__main__':
    populate()
