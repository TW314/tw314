from django import forms


class SenhaForm(forms.Form):
    senha = forms.CharField(min_length=6, required=True)
