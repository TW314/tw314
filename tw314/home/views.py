from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect, get_object_or_404

from .forms import *
from .models import *


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


def suporte_cadastro_status(request):
    # Cadastro

    if request.method == "POST":
        form = StsForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = StsForm()

    status = suporte_listar_status(request)

    return render(request, 'home/suporte/suporte_cadastro_status.html',
                  {'status': status, 'form': form})


def suporte_listar_status(request):
    # Lista
    list_status = Status.objects.order_by('nome')   # listagem de status ordenado por nome
    paginator = Paginator(list_status, 5)           # 5 dados por pagina

    page = request.GET.get('page')

    try:
        status = paginator.page(page)
    except PageNotAnInteger:
        # Se página não for inteiro, irá retornar a primeira pagina
        status = paginator.page(1)
    except EmptyPage:
        # Se ficarem muitas paginas
        status = paginator.page(paginator.num_pages)

    return status


def suporte_editar_status(request, pk):
    # Editar
    edit_status = get_object_or_404(Status, pk=pk)
    if request.method == "POST":
        form = StsForm(request.POST, instance=edit_status)
        if form.is_valid():
            edit_status = form.save(commit=False)
            edit_status.save()
            pk = edit_status.pk
            return render('home/suporte/suporte_cadastro_status.html', {'pk': pk})
    else:
        form = StsForm(instance=edit_status)

    suporte_listar_status(request)
    return {'pk': pk}


def suporte_cadastro_ramo(request):
    # Cadastro

    if request.method == "POST":
        form = RamForm(request.POST)
        if form.is_valid():
            ramo = form.save(commit=False)
            ramo.save()
    else:
        form = RamForm()

    ramos = suporte_listar_ramo(request)

    return render(request, 'home/suporte/suporte_cadastro_ramo.html',
                  {'ramos': ramos, 'form': form})


def suporte_listar_ramo(request):
    # Lista
    list_ramo = RamoAtividade.objects.order_by('nome')      # listagem de ramo ordenado por nome
    paginator = Paginator(list_ramo, 5)                     # 5 dados por pagina

    page = request.GET.get('page')

    try:
        ramos = paginator.page(page)
    except PageNotAnInteger:
        # Se página não for inteiro, irá retornar a primeira pagina
        ramos = paginator.page(1)
    except EmptyPage:
        # Se ficarem muitas paginas
        ramos = paginator.page(paginator.num_pages)

    return ramos


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


# Relatorio
def funcionario_relatorio(request):
    return render(request, 'home/funcionario/funcionario_relatorio.html', {})


# Sobre
def funcionario_sobre(request):
    return render(request, 'home/funcionario/funcionario_sobre.html', {})


# Contatar suporte
def funcionario_suporte(request):
    return render(request, 'home/funcionario/funcionario_contatar_suporte.html', {})
