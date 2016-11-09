from django import forms


class EmpresaForm(forms.Form):
    ramo_atividade = forms.CharField(required=True)
    numero_cnpj = forms.CharField(max_length=14, required=True)
    nome_fantasia = forms.CharField(max_length=80, required=True)
    razao_social = forms.CharField(max_length=80, required=True)
    status_ativacao = forms.CharField(required=True)
    cep = forms.CharField(max_length=8, required=True)
    logradouro = forms.CharField(max_length=255, required=True)
    numero_logradouro = forms.CharField(max_length=255, required=True)
    bairro = forms.CharField(max_length=100, required=True)
    cidade = forms.CharField(max_length=100, required=True)
    uf = forms.CharField(max_length=2, required=True)
    email = forms.EmailField(max_length=100, required=True)
    telefone = forms.CharField(max_length=11, required=True)
    nome_responsavel = forms.CharField(max_length=80, required=True)
    cargo_responsavel = forms.CharField(max_length=45, required=True)
    cpf_responsavel = forms.CharField(max_length=11, required=True)


