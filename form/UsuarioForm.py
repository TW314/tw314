from django import forms


class UsuarioForm(forms.Form):
    nome = forms.CharField(max_length=80, required=True)
    email = forms.EmailField(max_length=100, required=True)
    status_ativacao = forms.CharField(required=False)
    empresa = forms.CharField(required=False)
