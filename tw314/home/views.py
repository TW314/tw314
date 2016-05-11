from django.shortcuts import render


def index(request):
    return render(request, 'home/index.html', {})


def cadastro_usuario(request):
    return render(request, 'home/admin/cadastrar_usuario.html', {})


def admin_principal(request):
    return render(request, 'home/admin/admin_principal.html', {})


def relatorio(request):
    return render(request, 'home/admin/relatorio.html', {})