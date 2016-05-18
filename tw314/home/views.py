from django.shortcuts import render


# Index
def index(request):
    return render(request, 'home/index.html', {})


# Login
def login(request):
    return render(request, 'home/login.html', {})


# Admin
def admin_principal(request):
    return render(request, 'home/admin/admin_principal.html', {})


def admin_cadastro_usuario(request):
    return render(request, 'home/admin/admin_cadastrar_usuario.html', {})


def admin_relatorio(request):
    return render(request, 'home/admin/admin_relatorio.html', {})


def admin_cadastro_servico(request):
    return render(request, 'home/admin/admin_cadastro_servico.html', {})


# Suporte
def suporte_princpal(request):
    return render(request, 'home/suporte/suporte_principal.html', {})


def suporte_cadastro_admin(request):
    return render(request, 'home/suporte/suporte_cadastro_admin.html', {})


def suporte_cadastro_estabelecimento(request):
    return render(request, 'home/suporte/suporte_cadastro_estabelecimento.html', {})


def suporte_atendimento(request):
    return render(request, 'home/suporte/suporte_atendimento.html', {})


# ???
def demo_chart(request):
    return render(request, 'home/demo_chart.html', {})


# Funcionario
def funcionario_principal(request):
    return render(request, "home/funcionario/funcionario_principal.html", {})


def funcionario_relatorio(request):
    return render(request, 'home/funcionario/funcionario_relatorio.html', {})


# Sobre
def sobre(request):
    return render(request, 'home/funcionario/funcionario_sobre.html', {})
