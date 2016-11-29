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
    user = request.session["user"]

    form = UsuarioForm()
    if request.method == "POST":
        cadastra(request)

    estabelecimentos = listar_empresa()

    funs = lista_por_empresa_perfil(request)
    return render(request, template_name, params(form, funs, estabelecimentos, user))


@require_POST
def cadastra(request):
    UsuarioService.administrador_cadastra(request, request.POST)


def lista_por_empresa_perfil(request):
    empresa = request.session["user"]["empresa"]["id"]
    perfil = 3
    return UsuarioService.lista_por_empresa_perfil(empresa, perfil)


def busca_por_cnpj(request):
    cnpj = request.POST.cnpj
    return EmpresaService.busca_por_cnpj(cnpj)


def listar_empresa():
    return EmpresaService.lista()


def params(form, funs, estabelecimentos, user):
    return {'form': form, 'funs': funs, 'estabelecimentos': estabelecimentos, "user": user}


