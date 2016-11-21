from django.shortcuts import render
from service import EmpresaServicoService
from service import ServicoService
from form.UsuarioForm import UsuarioForm
from django.views.decorators.http import require_POST

# TODO: terminar
template_name = ''


def template(request):

    form = UsuarioForm()
    if request.method == "POST":
        cadastra(request)

    servicos = listar()

    funs = lista_por_empresa_perfil(request)
    return render(request, template_name, params(form, funs, estabelecimentos))

@require_POST
def cadastra(usuario):
    # UsuarioService.administrador_cadastra(usuario.POST)
    pass