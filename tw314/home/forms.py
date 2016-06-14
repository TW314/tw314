from django import forms

from . import models


class StsForm(forms.ModelForm):
    class Meta:
        model = models.Status
        fields = ('nome', 'descricao',)
