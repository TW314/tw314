from django import forms


class EmpresaServicoForm(forms.Form):
    status_ativacao = forms.CharField(required=False)
    servico = forms.CharField(required=True)



