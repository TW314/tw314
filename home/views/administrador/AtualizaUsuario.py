from django.shortcuts import render, redirect
from service import UsuarioService
from service import EmpresaService
from form.UsuarioForm import UsuarioForm
from django.views.decorators.http import require_POST

template_name = 'home/admin/admin_editar_funcionarios.html'
redirect_admin = 'http://127.0.0.1:8000/administrador/cadastro/funcionario'


def template(request, pk):

    form = UsuarioForm()
    funs = UsuarioService.usuario_por_id(pk)
    if request.method == "POST":
        atualiza(request, funs, pk)
        return redirect(redirect_admin)

    return render(request, template_name, params(form, funs))


@require_POST
def atualiza(request, usuario, pk):
    UsuarioService.administrador_atualiza(request.POST, usuario, pk)


def params(form, funs):
    return {'form': form, 'funs': funs}
