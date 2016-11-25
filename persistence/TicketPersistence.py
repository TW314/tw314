from pip._vendor import requests
from datetime import date


def mostrar_fila(empresa, servico):
    fila = requests.get("http://localhost:3000/ticket/fila/1&{0}&{1}&{2}".format(empresa, servico, date(2016, 11, 23))).json()

    return fila
