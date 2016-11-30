from pip._vendor import requests
from datetime import date


def mostrar_fila(empresa, servico):
    fila = requests.get("http://localhost:3000/ticket/fila/1&{0}&{1}&{2}".format(empresa, servico, date.today())).json()

    return fila


def mostrar_ticket(empresa, servico):
    ticket = requests.get("http://localhost:3000/ticket/ticket/2&{0}&{1}&{2}".format(empresa, servico, date.today())).json()

    return ticket


def chamar_ticket(empresa, servico):
    ticket = requests.get("http://localhost:3000/ticket/ticket/1&{0}&{1}&{2}".format(empresa, servico, date.today())).json()

    return ticket


def mudar_status_ticket(pk, status):
        try:
            ticket = requests.put('http://localhost:3000/ticket/' + pk, json={"statusTicketId": status})
            return ticket
        except requests.exceptions.ConnectionError:  # verificar se funciona
            print("Erro ao tentar conectar com WebService</h3>")
