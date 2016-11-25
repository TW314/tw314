from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from service.ServicoService import servico_por_id
from service.TicketService import mostrar_fila

template_name = 'home/funcionario/funcionario_principal.html'


def template(request):
    guiche = request.session["guiche"]
    servico = servico_por_id(request.session["servico"])
    fila = filas(1, request.session["servico"])
    return render(request, template_name, params(guiche, servico, fila))


def filas(empresa, servico):
    return mostrar_fila(empresa, servico)


def params(guiche, servico, fila):
    return {"guiche": guiche, "servico": servico, 'fila': fila}
