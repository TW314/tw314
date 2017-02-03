from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from service.ServicoService import servico_por_id
from service.TicketService import *
from service import AtendimentoService
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from socketIO_client import SocketIO, LoggingNamespace
from urllib.parse import urlparse
from django.conf import settings
import json

template_name = 'home/funcionario/funcionario_principal.html'


def template(request):
    if request.session["user"]:
        user = request.session["user"]
        guiche = request.session["guiche"]
        servico = servico_por_id(request.session["servico"])
        fila = mostrar_fila(request.session["user"]["empresa"]["id"], request.session["servico"])
        pegar_codigo = chamar_ticket(request, request.session["user"]["empresa"]["id"], request.session["servico"])
        senha = mostrar_ticket(request.session["user"]["empresa"]["id"], request.session["servico"])

        return render(request, template_name, params(guiche, servico, fila, senha, pegar_codigo, user))
    else:
        return HttpResponseRedirect(reverse("login"))


def chamar_proximo(request, pk):
    mudar_status_ticket(pk, 2)
    with SocketIO('192.168.0.104', 3000, LoggingNamespace) as socketIO:
        socketIO.emit('proximo', {
            "empresa": request.session["user"]["empresa"]["id"],
            "servico": request.session["servico"]
        })
    return HttpResponseRedirect(reverse('funcionario_principal'))


def iniciar_atendimento(request, ticket):
    AtendimentoService.cadastra(1, ticket, 1)
    return HttpResponseRedirect(reverse('funcionario_principal'))


def finalizar_atendimento(request, pk):
    mudar_status_ticket(pk, 3)
    return HttpResponseRedirect(reverse('funcionario_principal'))


def params(guiche, servico, fila, senha, pegar_codigo, user, node = settings.NODEJS_SOCKET_URL):
    return {"guiche": guiche, "servico": servico, 'fila': fila, 'senha': senha, 'pegar_codigo': pegar_codigo,
            "user": user}


# def save(request, *args, **kwargs):
#     # Check if the Special already exists
#     if not mostrar_fila:
#         # No pk so Speical is new, push update to node.js socket
#         # Parse the NODEJS_SOCKET_URL value
#         parsedurl = urlparse(settings.NODEJS_SOCKET_URL)
#         baseurl = "%s://%s" % (parsedurl.scheme, parsedurl.hostname)
#         baseport = parsedurl.port if parsedurl.port != None else 80
#         # Publish record to node.js socket
#         with SocketIO('192.168.0.104', 3000, LoggingNamespace) as socketIO:
#             socketIO.emit('proximo', {
#                 "empresa": request.session["user"]["empresa"]["id"],
#                 "servico": request.session["servico"]
#             })
#     save(request, *args, **kwargs)
