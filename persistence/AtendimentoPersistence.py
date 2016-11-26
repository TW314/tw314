from pip._vendor import requests


def cadastra(status, ticket, usuario):
    try:
        atendimento = requests.post('http://localhost:3000/atendimento/', json={"ticketCodigoAcesso": ticket, "usuarioId": usuario, "statusAtendimentoId": status})
        return atendimento
    except requests.exceptions.ConnectionError:  # verificar se funciona
        print("Erro ao tentar conectar com WebService")
