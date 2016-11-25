from django import forms


class GuicheServicoForm(forms.Form):
    guiche = forms.CharField(required=True)
    servico = forms.CharField(required=True)



