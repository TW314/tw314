# from cups import require

from django.shortcuts import render, redirect
from service import UsuarioService
from service import EmpresaService
from form.UsuarioForm import UsuarioForm
from django.views.decorators.http import require_POST, require_GET
from django.core.mail import send_mail
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect

template_name = 'home/admin/admin_cadastro_funcionario.html'


def template(request):

    form = UsuarioForm()
    if request.method == "POST":
        cadastra(request)

    estabelecimentos = listar_empresa()

    funs = lista_por_empresa_perfil(request)
    return render(request, template_name, params(form, funs, estabelecimentos))


@require_POST
def cadastra(usuario):
    UsuarioService.administrador_cadastra(usuario.POST)


def lista_por_empresa_perfil(request):
    empresa = 1
    perfil = 3
    return UsuarioService.lista_por_empresa_perfil(empresa, perfil)


def busca_por_cnpj(request):
    cnpj = request.POST.cnpj
    return EmpresaService.busca_por_cnpj(cnpj)


def listar_empresa():
    return EmpresaService.lista()


def params(form, funs, estabelecimentos):
    return {'form': form, 'funs': funs, 'estabelecimentos': estabelecimentos}


