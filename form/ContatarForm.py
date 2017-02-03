from django import forms


class ContatarForm(forms.Form):
    nome = forms.CharField(max_length=80, required=True)
    email = forms.EmailField(max_length=100, required=True)
    assunto = forms.CharField(required=True)
    mensagem = forms.CharField(required=True)
