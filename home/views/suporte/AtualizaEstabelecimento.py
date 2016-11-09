from django.shortcuts import render, redirect
from service import EmpresaService
from service import RamoAtividadeService
from form.EmpresaForm import EmpresaForm
from django.views.decorators.http import require_POST

template_name = 'home/suporte/suporte_editar_estabelecimento.html'
redirect_cadastro = 'http://127.0.0.1:8000/suporte/cadastro/empresa'


def template(request, pk):

    form = EmpresaForm()
    empresa = EmpresaService.busca_por_id(pk)
    ramos = RamoAtividadeService.lista()

    if request.method == "POST":
        atualiza(request, empresa, pk)
        return redirect(redirect_cadastro)

    return render(request, template_name, params(form, empresa, ramos))


@require_POST
def atualiza(request, empresa, pk):
    EmpresaService.atualiza(request.POST, empresa, pk)


def params(form, empresas, ramos):
    return {'form': form, 'empresas': empresas, 'ramos': ramos}
