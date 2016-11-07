#from cups import require

from django.shortcuts import render
from service import UsuarioService
from service import EmpresaService
from form.UsuarioForm import UsuarioForm
from django.views.decorators.http import require_POST, require_GET


def template(request):
    form = UsuarioForm()
    estabelecimentos = listar_empresa()
    if request.method == "POST":
        cadastra(request)
    elif request.method == "GET":
        admins = lista_por_perfil()
        # estabelecimentos = busca_por_cnpj(request)
        return render(request, 'home/suporte/suporte_cadastro_admin.html', {'form': form, 'admins': admins, 'estabelecimentos': estabelecimentos})

    return render(request, 'home/suporte/suporte_cadastro_admin.html', {'form': form, 'estabelecimentos': estabelecimentos})


@require_POST
def cadastra(usuario):
    UsuarioService.suporte_cadastra(usuario.POST)


def listar(request):
    return UsuarioService


def lista_por_empresa_perfil(request):
    empresa = request.POST.empresa
    perfil = 2
    return UsuarioService.lista_por_empresa_perfil(empresa, perfil)


def lista_por_perfil():
    perfil = 2
    return UsuarioService.lista_por_perfil(perfil)


def busca_por_cnpj(request):
    cnpj = request.POST.cnpj
    return EmpresaService.busca_por_cnpj(cnpj)


def listar_empresa():
    return EmpresaService.lista()


def params(form, servicos, ramos):
    return {'form': form, 'servicos': servicos, 'ramos': ramos}

