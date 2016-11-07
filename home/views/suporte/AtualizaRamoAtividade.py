from django.shortcuts import render, redirect
from service import RamoAtividadeService
from form.RamoForm import RamoForm
from django.views.decorators.http import require_POST

template_name = 'home/suporte/suporte_editar_ramos.html'
template_cadastro = 'http://127.0.0.1:8000/suporte/cadastro/ramo'


def template(request, pk):

    form = RamoForm()
    ramo_atividade = RamoAtividadeService.ramo_por_id(pk)

    if request.method == "POST":
        atualiza(request, ramo_atividade, pk)
        return redirect(template_cadastro)

    return render(request, template_name, params(form, ramo_atividade))


@require_POST
def atualiza(request, ramo_atividade, pk):
    RamoAtividadeService.atualiza(request.POST, ramo_atividade, pk)


def params(form, ramos):
    return {'form': form, 'ramos': ramos}
