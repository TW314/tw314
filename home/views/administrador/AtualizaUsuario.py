from django.shortcuts import render, redirect
from service import UsuarioService
from service import EmpresaService
from form.UsuarioForm import UsuarioForm
from django.views.decorators.http import require_POST

template_name = 'home/suporte/suporte_editar_admins.html'
redirect_admin = 'http://127.0.0.1:8000/suporte/cadastro/administrador'


def template(request, pk):

    form = UsuarioForm()
    admins = UsuarioService.usuario_por_id(pk)
    empresas = EmpresaService.lista()
    if request.method == "POST":
        atualiza(request, admins, pk)
        return redirect(redirect_admin)

    return render(request, template_name, params(form, admins, empresas))


@require_POST
def atualiza(request, usuario, pk):
    UsuarioService.suporte_atualiza(request.POST, usuario, pk)


def params(form, admins, estabelecimentos):
    return {'form': form, 'admins': admins, 'estabelecimentos': estabelecimentos}
