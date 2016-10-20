from django import forms


class StsForm(forms.Form):
    pass


class EmpForm(forms.Form):
    pass


class RamForm(forms.Form):
    nome = forms.CharField(max_length=45, required=True, min_length=3)
    descricao = forms.CharField(required=True, min_length=5)
    status = forms.CharField()


class UsuFormSuporte(forms.Form):
    pass


class UsuFormAdmin(forms.Form):
    pass


class SvcForm(forms.Form):
    pass
