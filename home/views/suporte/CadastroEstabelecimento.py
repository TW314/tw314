from django.shortcuts import render
from service import EmpresaService
from form.EmpresaForm import EmpresaForm
from django.views.decorators.http import require_POST

template_name = 'home/suporte/suporte_cadastro_estabelecimento.html'


def template(request):

    if request.method == "POST":
        cadastra(request)

    form = EmpresaForm()
    empresas = EmpresaService.lista()

    return render(request, template_name, params(form, empresas))


@require_POST
def cadastra(empresas):
    EmpresaService.cadastra(empresas.POST)


def params(form, empresas):
    return {'form': form, 'empresas': empresas}