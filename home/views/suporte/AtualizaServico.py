from django.shortcuts import render, redirect
from service import ServicoService
from service import RamoAtividadeService
from form.ServicoForm import ServicoForm
from django.views.decorators.http import require_POST

template_name = 'home/suporte/suporte_editar_servicos.html'
template_cadastro = 'http://127.0.0.1:8000/suporte/cadastro/servico'


def template(request, pk):

    form = ServicoForm()
    servico = ServicoService.servico_por_id(pk)
    ramos = RamoAtividadeService.lista()

    if request.method == "POST":
        atualiza(request, servico, pk)
        return redirect(template_cadastro)

    return render(request, template_name, params(form, servico, ramos))


@require_POST
def atualiza(request, servico, pk):
    ServicoService.atualiza(request.POST, servico, pk)


def params(form, servico, ramos):
    return {'form': form, 'servicos': servico, 'ramos': ramos}
