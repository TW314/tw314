from django import forms


class StsForm(forms.Form):
    pass


class EmpForm(forms.Form):
    pass


class RamForm(forms.Form):
    nome = forms.CharField(max_length=45, required=True, min_length=3)
    descricao = forms.CharField(required=True, min_length=5)
    status_ativacao = forms.CharField(required=True)


class UsuFormSuporte(forms.Form):
    pass


class UsuFormAdmin(forms.Form):
    nome = forms.CharField(max_length=80, required=True)
    email = forms.EmailField(max_length=100, required=True)
    data_ativacao = forms.DateField()
    senha = forms.CharField(max_length=45)
    data_inativacao = forms.DateField()
    status_ativacao = forms.CharField(required=True)


class SvcForm(forms.Form):
    nome = forms.CharField(max_length=45)
    descricao = forms.CharField(required=True, min_length=5)
    ramo_atividade = forms.CharField()
    sigla = forms.CharField(max_length=2)
    status_ativacao = forms.CharField(required=True)



