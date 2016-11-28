from django.shortcuts import render
from service import EmpresaService
from form.EmpresaForm import EmpresaForm
from service import RamoAtividadeService
from django.views.decorators.http import require_POST

template_name = 'home/suporte/suporte_cadastro_estabelecimento.html'


def template(request):
    user = request.session["user"]
    if request.method == "POST":
        cadastra(request)

    form = EmpresaForm()
    empresas = EmpresaService.lista()
    ramos = RamoAtividadeService.lista()

    return render(request, template_name, params(form, empresas, ramos, user))


@require_POST
def cadastra(empresas):
    EmpresaService.cadastra(empresas.POST)


def params(form, empresas, ramos, user):
    return {'form': form, 'empresas': empresas, 'ramos': ramos, "user": user}
