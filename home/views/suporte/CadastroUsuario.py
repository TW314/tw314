# from cups import require

from django.shortcuts import render
from service import UsuarioService
from service import EmpresaService
from form.UsuarioForm import UsuarioForm
from django.views.decorators.http import require_POST, require_GET

template_name = 'home/suporte/suporte_cadastro_admin.html'


def template(request):

    form = UsuarioForm()
    if request.method == "POST":
        cadastra(request)

    estabelecimentos = listar_empresa()

    admins = lista_por_perfil()
    return render(request, template_name, params(form, admins, estabelecimentos))


@require_POST
def cadastra(usuario):
    UsuarioService.suporte_cadastra(usuario.POST)


"""def lista_por_empresa_perfil(request):
    empresa = request.POST.empresa
    perfil = 2
    return UsuarioService.lista_por_empresa_perfil(empresa, perfil)"""


def lista_por_perfil():
    perfil = 2
    return UsuarioService.lista_por_perfil(perfil)


def busca_por_cnpj(request):
    cnpj = request.POST.cnpj
    return EmpresaService.busca_por_cnpj(cnpj)


def listar_empresa():
    return EmpresaService.lista()


def params(form, admins, estabelecimentos):
    return {'form': form, 'admins': admins, 'estabelecimentos': estabelecimentos}
