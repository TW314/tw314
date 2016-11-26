from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    senha = forms.CharField(widget=forms.PasswordInput, min_length=6, required=True)
