# coding=utf-8
from pip._vendor import requests

from form.UsuarioForm import UsuarioForm


def administrador_cadastra(usuario):

    form = UsuarioForm(usuario)
    if form.is_valid():
        nome = form.cleaned_data['nome']
        email = form.cleaned_data['email']
        status_ativacao = form.cleaned_data['status_ativacao']
        data_inativacao = form.cleaned_data['data_inativacao']

        data = administrador_monta_json(nome, email, status_ativacao, data_inativacao)

        form = requests.post('http://localhost:3000/usuario', json=data)
    else:
        form = "Campos de Usuario nao preenchidos corretamente"

    return form


def suporte_cadastra(usuario):

    form = UsuarioForm(usuario)
    if form.is_valid():
        nome = form.cleaned_data['nome']
        email = form.cleaned_data['email']
        status_ativacao = form.cleaned_data['status_ativacao']
        data_inativacao = form.cleaned_data['data_inativacao']
        empresa = form.cleaned_data['empresa']

        data = suporte_monta_json(nome, email, empresa, status_ativacao, data_inativacao)

        form = requests.post('http://localhost:3000/usuario', json=data)
    else:
        form = "Campos de Usuario nao preenchidos corretamente"

    return form


def atualiza(servico, pk):
    pass


def lista_por_empresa_perfil(empresa, perfil):
    usuario = requests.get('http://localhost:3000/usuario/empresa/'+empresa+"&"+perfil).json()
    return usuario


def lista_por_perfil(perfil):
    # fixme: arrumar esse retorno - todo: descobrir o que esta acontecendo
    return requests.get('http://localhost:3000/usuario/perfil/'+perfil).json()


def suporte_monta_json(nome, email, empresa, status_ativacao, data_inativacao):
    data = {'nome': nome, 'email': email, 'status_ativacao': status_ativacao,
            'data_inativacao': data_inativacao, 'empresaId': empresa, 'perfilId': 2}
    return data


def administrador_monta_json(nome, email, status_ativacao, data_inativacao):
    data = {'nome': nome, 'email': email, 'status_ativacao': status_ativacao, 'data_inativacao': data_inativacao,
            'perfilId': 3, 'empresaId': 1}

    return data
