from django.shortcuts import render


# Index
def index(request):
    return render(request, 'home/index.html', {})


# Login
def login(request):
    return render(request, 'home/login.html', {})


# Admin

# Principal
def admin_principal(request):
    return render(request, 'home/admin/admin_principal.html', {})

# Cadastro de Usuario
def admin_cadastro_usuario(request):
    return render(request, 'home/admin/admin_cadastrar_usuario.html', {})

# Relatório
def admin_relatorio(request):
    return render(request, 'home/admin/admin_relatorio.html', {})

# Cadastro de Serviço
def admin_cadastro_servico(request):
    return render(request, 'home/admin/admin_cadastro_servico.html', {})

# Contatar suporte
def contatar_suporte(request):
    return render(request, 'home/admin/admin_contatar_suporte.html', {})


# Suporte

# Principal
def suporte_princpal(request):
    return render(request, 'home/suporte/suporte_principal.html', {})

# Cadastro de Administrador
def suporte_cadastro_admin(request):
    return render(request, 'home/suporte/suporte_cadastro_admin.html', {})

# Cadastro de Estabelecimento
def suporte_cadastro_estabelecimento(request):
    return render(request, 'home/suporte/suporte_cadastro_estabelecimento.html', {})

# Atendimento
def suporte_atendimento(request):
    return render(request, 'home/suporte/suporte_atendimento.html', {})


# ???
def demo_chart(request):
    return render(request, 'home/demo_chart.html', {})


# Funcionario

# Principal
def funcionario_principal(request):
    return render(request, "home/funcionario/funcionario_principal.html", {})

# Relatório
def funcionario_relatorio(request):
    return render(request, 'home/funcionario/funcionario_relatorio.html', {})


# Sobre
def sobre(request):
    return render(request, 'home/funcionario/funcionario_sobre.html', {})
