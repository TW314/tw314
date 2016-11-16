from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    senha = forms.PasswordInput()
