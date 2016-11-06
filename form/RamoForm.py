from django import forms


class RamoForm(forms.Form):
    nome = forms.CharField(max_length=45, required=True, min_length=3)
    descricao = forms.CharField(required=True, min_length=5)
    status_ativacao = forms.CharField(required=False)
