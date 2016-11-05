from django.shortcuts import render
from service import ServicoService
from service import RamoAtividadeService
from form.ServicoForm import ServicoForm
from django.views.decorators.http import require_POST

template_name = 'home/suporte/suporte_cadastro_servico.html'


def template(request):

    if request.method == "POST":
        cadastra(request)

    form = ServicoForm()
    servicos = ServicoService.lista()
    ramos = RamoAtividadeService.lista()

    return render(request, template_name, params(form, servicos, ramos))


@require_POST
def cadastra(servico):
    ServicoService.cadastra(servico.POST)


def params(form, servicos, ramos):
    return {'form': form, 'servicos': servicos, 'ramos': ramos}
