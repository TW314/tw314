from django import forms


class StsForm(forms.Form):
    pass


class EmpForm(forms.Form):
    nome_fantasia = forms.CharField(max_length=80)
    razao_social = forms.CharField(max_length=80)
    nr_cnpj = forms.CharField(max_length=14)
    logradouro = forms.CharField(max_length=255)
    nr_logradouro = forms.CharField(max_length=255)
    cidade = forms.CharField(max_length=100)
    bairro = forms.CharField(max_length=100)
    uf = forms.CharField(max_length=2)
    cep = forms.CharField(max_length=8)
    telefone = forms.CharField(max_length=11)
    email = forms.EmailField(max_length=100)
    nome_responsavel = forms.CharField(max_length=80)
    cargo_responsavel = forms.CharField(max_length=45)
    cpf_responsavel = forms.CharField(max_length=11)
    data_abertura = forms.DateField()
    data_ativacao = forms.DateField()
    data_inativacao = forms.DateField()


class RamForm(forms.Form):
    nome = forms.CharField(max_length=45, required=True, min_length=3)

    status_ativacao = forms.CharField(required=True)


class UsuFormSuporte(forms.Form):
    pass


class UsuFormAdmin(forms.Form):
    nome = forms.CharField(max_length=80, required=True)
    email = forms.EmailField(max_length=100, required=True)
    status_ativacao = forms.CharField(required=True)


class SvcForm(forms.Form):
    nome = forms.CharField(max_length=45)
    descricao = forms.CharField(required=True, min_length=5)
    ramo_atividade = forms.CharField()
    sigla = forms.CharField(max_length=2)
    status_ativacao = forms.CharField(required=True)



