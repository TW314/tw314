# from cups import require

from django.shortcuts import render, redirect
from service import UsuarioService
from service import EmpresaService
from form.UsuarioForm import UsuarioForm
from django.views.decorators.http import require_POST, require_GET
from django.core.mail import send_mail
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect

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


def enviar_email(request, pk):
    usuario = UsuarioService.usuario_por_id(pk)
    send_mail(
        'Nova Senha em TW314',
        'Olá, ' + usuario['nome'] + '! Para continuar e acessar sua conta no sistema TW314, acesso o link http://localhost:8000' + str(reverse('adiciona_senha', args=[usuario['id']])) + ' e cadastre sua nova senha. Se acredita que houve um engano, por favor, entre em contado pelo e-mail contato@tw314.com.br. Att, Time TW314',
        'contatotw314@gmail.com',
        [usuario['email']],
        fail_silently=False,
    )
    return redirect(reverse('cadastrar_admin'))

