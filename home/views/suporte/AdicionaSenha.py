from django.shortcuts import render, redirect
from service import UsuarioService
from form.SenhaForm import SenhaForm
from django.views.decorators.http import require_POST

template_name = 'home/suporte/suporte_adicionar_senha.html'
redirect_route = 'http://127.0.0.1:8000'


def template(request, pk):

    form = SenhaForm()

    if request.method == "POST":
        adiciona_senha(request, pk)
        # return redirect(redirect_route)

    return render(request, template_name, params(form))


@require_POST
def adiciona_senha(request, pk):
    UsuarioService.adiciona_senha(request.POST, pk)


def params(form):
    return {'form': form}
