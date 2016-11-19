from pip._vendor import requests

from form.EmpresaForm import EmpresaForm


def cadastra(empresa):
    form = EmpresaForm(empresa)

    if form.is_valid():
        ramo_atividade = form.cleaned_data['ramo_atividade']
        numero_cnpj = form.cleaned_data["numero_cnpj"]
        nome_fantasia = form.cleaned_data['nome_fantasia']
        razao_social = form.cleaned_data['razao_social']
        status_ativacao = form.cleaned_data['status_ativacao']
        cep = form.cleaned_data['cep']
        logradouro = form.cleaned_data['logradouro']
        numero_logradouro = form.cleaned_data['numero_logradouro']
        bairro = form.cleaned_data['bairro']
        cidade = form.cleaned_data['cidade']
        uf = form.cleaned_data['uf']
        email = form.cleaned_data['email']
        telefone = form.cleaned_data['telefone']
        nome_responsavel = form.cleaned_data['nome_responsavel']
        cargo_responsavel = form.cleaned_data['cargo_responsavel']
        cpf_responsavel = form.cleaned_data['cpf_responsavel']

        data = monta_json(nome_fantasia, razao_social, numero_cnpj, logradouro, numero_logradouro, bairro, cidade, uf, cep, telefone, email, nome_responsavel, cargo_responsavel, cpf_responsavel, ramo_atividade, status_ativacao)
        try:
            form = requests.post('http://localhost:3000/empresa', json=data)
        except requests.exceptions.ConnectionError: # verificar se funciona
            form = "Erro ao tentar conectar com WebService"
    else:
        form = "Campos de Empresa nao preenchidos corretamente"
    return form


def atualiza(empresa_novo, empresa, pk):

    form = EmpresaForm(empresa_novo)

    if form.is_valid():
        ramo_atividade = form.cleaned_data['ramo_atividade']
        numero_cnpj = form.cleaned_data["numero_cnpj"]  # todo: remover da edicao
        nome_fantasia = form.cleaned_data['nome_fantasia']
        razao_social = form.cleaned_data['razao_social']
        status_ativacao = empresa['status_ativacao']
        cep = form.cleaned_data['cep']
        logradouro = form.cleaned_data['logradouro']
        numero_logradouro = form.cleaned_data['numero_logradouro']
        bairro = form.cleaned_data['bairro']
        cidade = form.cleaned_data['cidade']
        uf = form.cleaned_data['uf']
        email = form.cleaned_data['email']
        telefone = form.cleaned_data['telefone']
        nome_responsavel = form.cleaned_data['nome_responsavel']
        cargo_responsavel = form.cleaned_data['cargo_responsavel']
        cpf_responsavel = form.cleaned_data['cpf_responsavel']

        data = monta_json(nome_fantasia, razao_social, numero_cnpj, logradouro, numero_logradouro, bairro, cidade, uf, cep, telefone, email, nome_responsavel, cargo_responsavel, cpf_responsavel, ramo_atividade, status_ativacao)

        try:
            form = requests.put('http://localhost:3000/empresa/' + pk, json=data)

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


def monta_json(nome_fantasia, razao_social, numero_cnpj, logradouro,  numero_logradouro, bairro, cidade, uf, cep, telefone, email, nome_responsavel, cargo_responsavel, cpf_responsavel, ramo_atividade, status_ativacao):
    data = {'nome_fantasia': nome_fantasia, 'razao_social': razao_social, 'numero_cnpj': numero_cnpj, 'logradouro': logradouro, 'numero_logradouro': numero_logradouro, 'bairro': bairro, 'cidade': cidade, 'uf': uf, 'cep': cep, 'telefone': telefone, 'email': email, 'nome_responsavel': nome_responsavel, 'cargo_responsavel': cargo_responsavel, 'cpf_responsavel': cpf_responsavel, 'ramoAtividadeId': ramo_atividade, 'status_ativacao': status_ativacao}
    return data
