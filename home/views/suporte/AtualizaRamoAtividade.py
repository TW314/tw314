from django.shortcuts import render, redirect
from service import RamoAtividadeService
from form.RamoForm import RamoForm
from django.views.decorators.http import require_POST

template_name = 'home/suporte/suporte_editar_ramos.html'
template_cadastro = 'http://127.0.0.1:8000/suporte/cadastro_ramos'


def template(request, pk):

    if request.method == "POST":
        atualiza(request, pk)
        return redirect(template_cadastro)
    form = RamoForm()
    ramo = RamoAtividadeService.ramo_por_id(pk)

    return render(request, template_name, params(form, ramo))


@require_POST
def atualiza(ramo_atividade, pk):
    RamoAtividadeService.atualiza(ramo_atividade.POST, pk)


def params(form, ramos):
    return {'form': form, 'ramos': ramos}