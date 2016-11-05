from django.shortcuts import render
from service import RamoAtividadeService
from form.RamoForm import RamoForm
from django.views.decorators.http import require_POST

template_name = 'home/suporte/suporte_cadastro_ramo.html'


def template(request):

    if request.method == "POST":
        cadastra(request)

    form = RamoForm()
    ramos = RamoAtividadeService.lista()

    return render(request, template_name, params(form, ramos))


@require_POST
def cadastra(ramo_atividade):
    RamoAtividadeService.cadastra(ramo_atividade.POST)


def params(form, ramos):
    return {'form': form, 'ramos': ramos}