from pip._vendor import requests
from datetime import date
from django.conf import settings


def mostrar_fila(empresa, servico):
    fila = requests.get("{0}ticket/fila/1&{1}&{2}&{3}".format(settings.NODEJS_SOCKET_URL, empresa, servico, date.today())).json()

    return fila


def mostrar_ticket(empresa, servico):
    ticket = requests.get("{0}ticket/ticket/2&{1}&{2}&{3}".format(settings.NODEJS_SOCKET_URL, empresa, servico, date.today())).json()

    return ticket


def chamar_ticket(empresa, servico):
    ticket = requests.get("{0}ticket/ticket/1&{1}&{2}&{3}".format(settings.NODEJS_SOCKET_URL, empresa, servico, date.today())).json()

    return ticket


def mudar_status_ticket(pk, status):
        try:
            ticket = requests.put(settings.NODEJS_SOCKET_URL + 'ticket/' + pk, json={"statusTicketId": status})
            return ticket
        except requests.exceptions.ConnectionError:  # verificar se funciona
            print("<h3>Erro ao tentar conectar com WebService</h3>")
