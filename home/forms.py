from django import forms


class StsForm(forms.Form):
    pass


class EmpForm(forms.Form):
    nome_fantasia = forms.CharField(max_length=80, required=True)
    razao_social = forms.CharField(max_length=80, required=True)
    numero_cnpj = forms.CharField(max_length=14, required=True)
    logradouro = forms.CharField(max_length=255, required=True)
    numero_logradouro = forms.CharField(max_length=255, required=True)
    cidade = forms.CharField(max_length=100, required=True)
    uf = forms.CharField(max_length=2, required=True)
    cep = forms.CharField(max_length=8, required=True)
    pais = forms.CharField(max_length=255, required=True)
    telefone = forms.CharField(max_length=11, required=True)
    email = forms.EmailField(max_length=100, required=True)
    nome_responsavel = forms.CharField(max_length=80, required=True)
    cargo_responsavel = forms.CharField(max_length=45, required=True)
    cpf_responsavel = forms.CharField(max_length=11, required=True)
    data_abertura = forms.DateField(required=False)
    data_inativacao = forms.DateField(required=False)
    status_ativacao = forms.CharField(required=True)
    ramo_atividade = forms.CharField(required=True)


class RamForm(forms.Form):
    nome = forms.CharField(max_length=45, required=True, min_length=3)
    descricao = forms.CharField(required=True, min_length=5)
    status_ativacao = forms.CharField(required=True)


class UsuFormSuporte(forms.Form):
    nome = forms.CharField(max_length=80, required=True)
    email = forms.EmailField(max_length=100, required=True)
    data_inativacao = forms.DateField(required=False)
    status_ativacao = forms.CharField(required=True)
    empresa = forms.CharField(required=True)


class UsuFormAdmin(forms.Form):
    nome = forms.CharField(max_length=80, required=True)
    email = forms.EmailField(max_length=100, required=True)
    data_inativacao = forms.DateField(required=False)
    status_ativacao = forms.CharField(required=True)


class SvcForm(forms.Form):
    nome = forms.CharField(max_length=45)
    descricao = forms.CharField(required=True, min_length=5)
    sigla = forms.CharField(max_length=2)
    status_ativacao = forms.CharField(required=True)



