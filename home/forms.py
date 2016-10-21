from django import forms
from splitjson.widgets import SplitJSONWidget


class StsForm(forms.Form):
    pass


class EmpForm(forms.Form):
    pass


class RamForm(forms.Form):
    # tentando usar splitjson
    nome = forms.CharField(widget=SplitJSONWidget(), max_length=45, required=True, min_length=3)
    descricao = forms.CharField(widget=SplitJSONWidget(), required=True, min_length=5)
    status = forms.CharField(widget=SplitJSONWidget())


class UsuFormSuporte(forms.Form):
    pass


class UsuFormAdmin(forms.Form):
    pass


class SvcForm(forms.Form):
    pass
