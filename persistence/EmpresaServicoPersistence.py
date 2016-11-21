from pip._vendor import requests

from form.EmpresaServicoForm import EmpresaServicoForm
# TODO MASTER: MUDAR AS ROTAS DE REQUEST DO


def cadastra(rel_emp_svc):
    form = EmpresaServicoForm(rel_emp_svc)

    if form.is_valid():
        status_ativacao = form.cleaned_data['status_ativacao']
        servico = form.cleaned_data['servico']

        data = monta_json(status_ativacao, servico)

        try:
            form = requests.post('http://localhost:3000/servicos_empresa', json=data)
        except requests.exceptions.ConnectionError:  # verificar se funciona
            form = "Erro ao tentar conectar com WebService"
    else:
        form = "Campos de Empresa nao preenchidos corretamente"
    return form


def atualiza(rel_novo, rel, pk):

    form = EmpresaServicoForm(rel_novo)

    if form.is_valid():
        status_ativacao = rel['status_ativacao']
        servico = form.cleaned_data['servico']

        data = monta_json(status_ativacao, servico)

        try:
            form = requests.put('http://localhost:3000/rel/' + pk, json=data)

        except requests.exceptions.ConnectionError:  # verificar se funciona
            form = "<h3>Erro ao tentar conectar com WebService</h3>"
    else:
        form = "<h3>Campos de Empresa nao preenchidos corretamente</h3>"

    return form


def lista():
    empresa = requests.get('http://localhost:3000/empresa').json()
    return empresa


def busca_por_cnpj(cnpj):
    empresa = requests.get('http://localhost:3000/empresa/' + cnpj).json()
    return empresa


def empresa_por_id(id):
    return requests.get('http://localhost:3000/empresa/' + str(id)).json()


def monta_json(status_ativacao, servico):
    data = {'status_ativacao': status_ativacao, 'empresaId': 1, 'servicoId': servico}
    return data
