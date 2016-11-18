from pip._vendor import requests

from form.ServicoForm import ServicoForm


def cadastra(servico):

    form = ServicoForm(servico)
    if form.is_valid():
        nome = form.cleaned_data['nome']
        descricao = form.cleaned_data['descricao']
        ramo_atividade = form.cleaned_data['ramo_atividade']
        sigla = form.cleaned_data['sigla']
        status_ativacao = form.cleaned_data['status_ativacao']

        data = monta_json(nome, descricao, ramo_atividade, sigla, status_ativacao)

        form = requests.post('http://localhost:3000/servico/', json=data)
    else:
        form = "Campos de Servico nao preenchido corretamente"

    return form


def atualiza(servico_novo, servico, pk):

    form = ServicoForm(servico_novo)

    if form.is_valid():
        nome = form.cleaned_data['nome']
        descricao = form.cleaned_data['descricao']
        ramoAtividadeId = form.cleaned_data['ramo_atividade']
        sigla = form.cleaned_data['sigla']

        data = monta_json(nome, descricao, ramoAtividadeId, sigla)

        try:
            form = requests.put('http://localhost:3000/servico/' + pk, json=data)

        except requests.exceptions.ConnectionError:  # verificar se funciona
            form = "Erro ao tentar conectar com WebService"
    else:
        form = "Campos de Servico nao preenchidos corretamente"

    return form


def servico_por_id(pk):
    servico = requests.get('http://localhost:3000/servico/' + pk).json()
    return servico


def lista():
    servico = requests.get('http://localhost:3000/servico').json()
    return servico


def monta_json(nome, descricao, ramoAtividadeId, sigla):
    data = {'nome': nome, 'descricao': descricao, 'ramoAtividadeId': ramoAtividadeId, 'sigla': sigla}

    return data
