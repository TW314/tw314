from django.shortcuts import render


def index(request):
    return render(request, 'home/index.html', {})


def cadastro_usuario(request):
    return render(request, 'home/admin/cadastrar_usuario.html', {})

