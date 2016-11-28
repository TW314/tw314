from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from service.ServicoService import servico_por_id
from service.TicketService import *
from service import AtendimentoService
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

template_name = 'home/funcionario/funcionario_principal.html'


def template(request):

    if request.session["user"]:
        user = request.session["user"]
        guiche = request.session["guiche"]
        servico = servico_por_id(request.session["servico"])
        fila = mostrar_fila(1, request.session["servico"])
        pegar_codigo = chamar_ticket(1, request.session["servico"])
        senha = mostrar_ticket(1, request.session["servico"])

        return render(request, template_name, params(guiche, servico, fila, senha, pegar_codigo, user))
    else:
        return HttpResponseRedirect(reverse("login"))


def chamar_proximo(request, pk):
    mudar_status_ticket(pk, 2)
    return HttpResponseRedirect(reverse('funcionario_principal'))


def iniciar_atendimento(request, ticket):
    AtendimentoService.cadastra(1, ticket, 1)
    return HttpResponseRedirect(reverse('funcionario_principal'))


def finalizar_atendimento(request, pk):
    mudar_status_ticket(pk, 3)
    return HttpResponseRedirect(reverse('funcionario_principal'))


def params(guiche, servico, fila, senha, pegar_codigo, user):
    return {"guiche": guiche, "servico": servico, 'fila': fila, 'senha': senha, 'pegar_codigo': pegar_codigo, "user": user}

