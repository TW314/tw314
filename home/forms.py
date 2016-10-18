from django import forms

status = ('Ativo', 'Inativo')


class StsForm(forms.Form):
    pass


class EmpForm(forms.Form):
    pass


class RamForm(forms.Form):
    nome = forms.CharField(max_length=45)
    descricao = forms.CharField()
    status = forms.ChoiceField()


class UsuFormSuporte(forms.Form):
    pass


class UsuFormAdmin(forms.Form):
    pass


class SvcForm(forms.Form):
    pass
