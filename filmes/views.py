from django.shortcuts import render, get_object_or_404, redirect
from .models import Filme, Genero
from .forms import FilmeForm

def lista_filmes(request):
    filmes = Filme.objects.all()
    return render(request, 'filmes/lista_filmes.html', {'filmes': filmes})

def cria_filme(request):
    if request.method == 'POST':
        form = FilmeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_filmes')
    else:
        form = FilmeForm()
    return render(request, 'filmes/cria_filme.html', {'form': form})

def edita_filme(request, id):
    filme = get_object_or_404(Filme, id=id)
    if request.method == 'POST':
        form = FilmeForm(request.POST, instance=filme)
        if form.is_valid():
            form.save()
            return redirect('lista_filmes')
    else:
        form = FilmeForm(instance=filme)
    return render(request, 'filmes/edita_filme.html', {'form': form})

def deleta_filme(request, id):
    filme = get_object_or_404(Filme, id=id)
    if request.method == 'POST':
        filme.delete()
        return redirect('lista_filmes')
    return render(request, 'filmes/deleta_filme.html', {'filme': filme})

import requests

OMDB_API_KEY = 'b3218645'  # Cadastre-se no OMDb para pegar sua chave

def buscar_filme_api(titulo):
    url = f"http://www.omdbapi.com/?t={titulo}&apikey={OMDB_API_KEY}"
    resposta = requests.get(url)
    return resposta.json()

def exibe_filme_api(request, titulo):
    dados_filme = buscar_filme_api(titulo)
    return render(request, 'filmes/exibe_filme_api.html', {'dados_filme': dados_filme})

