from django import forms


class EmpresaForm(forms.Form):
    nome_fantasia = forms.CharField(max_length=80, required=True)
    razao_social = forms.CharField(max_length=80, required=True)
    nr_cnpj = forms.CharField(max_length=14, required=True)
    logradouro = forms.CharField(max_length=255, required=True)
    numero_logradouro = forms.CharField(max_length=255, required=True)
    cidade = forms.CharField(max_length=100, required=True)
    uf = forms.CharField(max_length=2, required=True)
    cep = forms.CharField(max_length=8, required=True)
    #pais = forms.CharField(max_length=255, required=True)
    telefone = forms.CharField(max_length=11, required=True)
    email = forms.EmailField(max_length=100, required=True)
    nome_responsavel = forms.CharField(max_length=80, required=True)
    cargo_responsavel = forms.CharField(max_length=45, required=True)
    cpf_responsavel = forms.CharField(max_length=11, required=True)
    data_abertura = forms.DateField(required=False)
    data_inativacao = forms.DateField(required=False)
    status_ativacao = forms.CharField(required=True)
    ramo_atividade = forms.CharField(required=True)


