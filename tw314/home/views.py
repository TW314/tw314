import post as post
from django.shortcuts import render, redirect, get_object_or_404
from .forms import StsForm
from .models import STS_STATUS

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
    return render(request, 'home/admin/admin_cadastro_usuario.html', {})


# Relatorio
def admin_relatorio(request):
    return render(request, 'home/admin/admin_relatorio.html', {})


# Cadastro de Servico
def admin_cadastro_servico(request):
    return render(request, 'home/admin/admin_cadastro_servico.html', {})


# Contatar suporte
def admin_suporte(request):
    return render(request, 'home/admin/admin_contatar_suporte.html', {})


# Sobre
def admin_sobre(request):
    return render(request, 'home/admin/admin_sobre.html', {})

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



# Cadastro de Serviço
def suporte_cadastro_servico(request):
    return render(request, 'home/suporte/suporte_cadastro_servico.html', {})


# Cadastro de Status
def suporte_cadastro_status(request):
    status = STS_STATUS.objects.order_by('STS_NOME')
    if request.method == "POST":
        form = StsForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = StsForm()

    return render(request, 'home/suporte/suporte_cadastro_status.html', {'form': form, 'status': status})


def suporte_editar_status(request, pk):
    edit_status = get_object_or_404(STS_STATUS, pk=pk)
    if request.method == "POST":
        form = StsForm(request.POST, instance=edit_status)
        if form.is_valid():
            edit_status = form.save(commit=False)
            post.save()
            return redirect('blog.views.suporte_editar_status', pk=edit_status.pk)
    else:
        form = StsForm(instance=post)
    return render(request, 'home/suporte/suporte_cadastro_status.html', {'form': form})


# Atendimento
def suporte_atendimento(request):
    return render(request, 'home/suporte/suporte_atendimento.html', {})


# Cadastro de Serviço
def suporte_cadastro_ramo(request):
    return render(request, 'home/suporte/suporte_cadastro_ramo.html', {})


# ???
def demo_chart(request):
    return render(request, 'home/demo_chart.html', {})


# Funcionario

# Principal
def funcionario_principal(request):
    return render(request, "home/funcionario/funcionario_principal.html", {})


# Relatorio
def funcionario_relatorio(request):
    return render(request, 'home/funcionario/funcionario_relatorio.html', {})


# Sobre
def funcionario_sobre(request):
    return render(request, 'home/funcionario/funcionario_sobre.html', {})


# Contatar suporte
def funcionario_suporte(request):
    return render(request, 'home/funcionario/funcionario_contatar_suporte.html', {})