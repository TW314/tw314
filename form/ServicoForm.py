from django import forms

class ServicoForm(forms.Form):
    nome = forms.CharField(max_length=45)
    descricao = forms.CharField(required=True, min_length=5)
    ramo_atividade = forms.CharField()
    sigla = forms.CharField(max_length=2)
    status_ativacao = forms.CharField(required=True)