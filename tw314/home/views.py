from django.shortcuts import render


def index(request):
    return render(request, 'home/index.html', {})


def cadastro_usuario(request):
    return render(request, 'home/admin/cadastrar_usuario.html', {})


def admin_principal(request):
    return render(request, 'home/admin/admin_principal.html', {})


def suporte_princpal(request):
    return render(request, 'home/suporte/suporte_principal.html', {})



