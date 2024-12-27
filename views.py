from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from web_artemis.models import Relato, Usuario

def index(request):
    context = {
        'relatos': [
            {'titulo': 'Relato 1', 'conteudo': 'Conteúdo do relato 1', 'autor': {'username': 'João'}, 'criado_em': '2024-12-26'},
            {'titulo': 'Relato 2', 'conteudo': 'Conteúdo do relato 2', 'autor': {'username': 'Maria'}, 'criado_em': '2024-12-25'}
        ]
    }
    return render(request, 'ARTEMIS_TEMPLATE/index.html', context)



@login_required
def novo_relato(request):
    if request.method == "POST":
        titulo = request.POST["titulo"]
        conteudo = request.POST["conteudo"]
        
        # Tentar buscar a instância de Usuario associada ao request.user
        try:
            usuario = Usuario.objects.get(user=request.user)  # Supondo que tenha um campo 'user' no modelo Usuario
        except Usuario.DoesNotExist:
            # Caso não encontre o usuário associado, pode criar ou retornar erro
            return redirect("/")  # Ou outra lógica de erro

        # Criação do relato com a instância de Usuario
        Relato.objects.create(titulo=titulo, conteudo=conteudo, autor=usuario)
        return redirect("/")
    
    return render(request, "artemis_template/novo_relato.html")

def disque_denuncia(request):
    return render(request, "artemis_template/disque_denuncia.html")

