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
    if request.method == "POST":
        form = UsuFormAdmin(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UsuFormAdmin()

    usuarios = suporte_listar_usuario(request)
    perfis = Perfil.objects.all().exclude(id=1)
    return render(request, 'home/admin/admin_cadastro_usuario.html',
                  {'usuarios': usuarios, 'form': form, 'perfis': perfis})


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


# Cadastro de Estabelecimento
def suporte_cadastro_estabelecimento(request):
    # Cadastro
    if request.method == "POST":
        form = EmpForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = EmpForm()

    empresas = suporte_listar_empresas(request)
    ramos = RamoAtividade.objects.filter(status=1)
    return render(request, 'home/suporte/suporte_cadastro_estabelecimento.html',
                  {'empresas': empresas, 'form': form, 'ramos': ramos})


def suporte_listar_empresas(request):
    # Lista
    list_empresa = Empresa.objects.order_by('nome_fantasia')     # listagem de status ordenado por nome
    paginator = Paginator(list_empresa, 5)                       # 5 dados por pagina

    page = request.GET.get('page')

    try:
        empresas = paginator.page(page)
    except PageNotAnInteger:
        # Se pagina nao for inteiro, ira retornar a primeira pagina
        empresas = paginator.page(1)
    except EmptyPage:
        # Se ficarem muitas paginas
        empresas = paginator.page(paginator.num_pages)

    return empresas


# Cadastro de Servico
def suporte_cadastro_servico(request):
    #Cadastro
    if request.method == "POST":
        form = SvcForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SvcForm()

    servicos = suporte_listar_servico(request)
    ramos = RamoAtividade.objects.filter(status=1)

    return render(request, 'home/suporte/suporte_cadastro_servico.html',
                  {'servicos': servicos, 'form': form, 'ramos': ramos})


def suporte_editar_servicos(request, pk):
    # Editar
    servicos = get_object_or_404(Servico, pk=pk)
    if request.method == "POST":
        form = SvcForm(request.POST, instance=servicos)
        if form.is_valid():
            servicos = form
            servicos.save()
            return redirect('/suporte/cadastro_servico')

    ramos = RamoAtividade.objects.filter(status=1)
    return render(request, 'home/suporte/suporte_editar_servicos.html', {'servicos': servicos, 'ramos':ramos})


def suporte_listar_servico(request):
    # Lista
    list_servico = Servico.objects.order_by('nome')  # listagem de servico ordenado por nome
    paginator = Paginator(list_servico, 5)           # 5 dados por pagina

    page = request.GET.get('page')

    try:
        servico = paginator.page(page)
    except PageNotAnInteger:
        # Se pagina nao for inteiro, ira retornar a primeira pagina
        servico = paginator.page(1)
    except EmptyPage:
        # Se ficarem muitas paginas
        servico = paginator.page(paginator.num_pages)

    return servico


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
        # Se pagina nao for inteiro, ira retornar a primeira pagina
        status = paginator.page(1)
    except EmptyPage:
        # Se ficarem muitas paginas
        status = paginator.page(paginator.num_pages)

    return status


def suporte_editar_status(request, pk):
    # Editar
    status = get_object_or_404(Status, pk=pk)
    if request.method == "POST":
        form = StsForm(request.POST, instance=status)
        if form.is_valid():
            status = form
            status.save()
            return redirect('/suporte/status/')
    return render(request, 'home/suporte/suporte_editar_status.html', {'status': status})


def suporte_cadastro_ramo(request):
    # Cadastro
    if request.method == "POST":
        form = RamForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = RamForm()

    ramos = suporte_listar_ramo(request)

    return render(request, 'home/suporte/suporte_cadastro_ramo.html', {'ramos': ramos, 'form': form})


def suporte_editar_ramos(request, pk):
    # Editar
    ramos = get_object_or_404(RamoAtividade, pk=pk)
    if request.method == "POST":
        form = RamForm(request.POST, instance=ramos)
        if form.is_valid():
            ramos = form
            ramos.save()
            return redirect('/suporte/cadastro_ramos')
    return render(request, 'home/suporte/suporte_editar_ramos.html', {'ramos': ramos})


def suporte_listar_ramo(request):
    # Lista
    list_ramo = RamoAtividade.objects.order_by('nome')  # listagem de ramo ordenado por nome
    paginator = Paginator(list_ramo, 5)                 # 5 dados por pagina

    page = request.GET.get('page')

    try:
        ramos = paginator.page(page)
    except PageNotAnInteger:
        # Se pagina nao for inteiro, ira retornar a primeira pagina
        ramos = paginator.page(1)
    except EmptyPage:
        # Se ficarem muitas paginas
        ramos = paginator.page(paginator.num_pages)

    return ramos


def suporte_cadastro_usuario(request):
    # Cadastro

    if request.method == "POST":
        form = UsuFormSuporte(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UsuFormSuporte()

    usuarios = suporte_listar_usuario(request)

    estabelecimentos = Empresa.objects.filter(status=1)

    return render(request, 'home/suporte/suporte_cadastro_admin.html',
                  {'usuarios': usuarios, 'form': form, 'estabelecimentos': estabelecimentos})


def suporte_listar_usuario(request):
    # Lista
    list_usuario = Usuario.objects.order_by('nome').exclude(perfil=1)  # listagem de ramo ordenado por nome
    paginator = Paginator(list_usuario, 5)  # 5 dados por pagina

    page = request.GET.get('page')

    try:
        usuario = paginator.page(page)
    except PageNotAnInteger:
        # Se pagina nao for inteiro, ira retornar a primeira pagina
        usuario = paginator.page(1)
    except EmptyPage:
        # Se ficarem muitas paginas
        usuario = paginator.page(paginator.num_pages)

    return usuario


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
