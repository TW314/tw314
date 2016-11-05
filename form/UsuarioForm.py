from django import forms

class UsuarioFormSuporte(forms.Form):
    pass

class UsuarioFormAdmin(forms.Form):
    nome = forms.CharField(max_length=80, required=True)
    email = forms.EmailField(max_length=100, required=True)
    data_ativacao = forms.DateField()
    senha = forms.CharField(max_length=45)
    data_inativacao = forms.DateField()
    status_ativacao = forms.CharField(required=True)