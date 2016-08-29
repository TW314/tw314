from django import forms

from . import models


class StsForm(forms.ModelForm):
    class Meta:
        model = models.Status
        fields = ('nome', 'descricao',)


class EmpForm(forms.ModelForm):
    class Meta:
        model = models.Empresa
        fields = ('nome_fantasia', 'razao_social', 'nr_cnpj', 'logradouro', 'nr_logradouro', 'cidade', 'bairro', 'uf', 'cep', 'telefone', 'email', 'nome_responsavel', 'cargo_responsavel', 'cpf_responsavel', 'ramo_atividade')


class RamForm(forms.ModelForm):
    class Meta:
        model = models.RamoAtividade
        fields = ('nome',)


class UsuFormSuporte(forms.ModelForm):
    class Meta:
        model = models.Usuario
        fields = ('nome', 'empresa', 'email')


class UsuFormAdmin(forms.ModelForm):
    class Meta:
        model = models.Usuario
        fields = ('nome', 'email', 'perfil')


class SvcForm(forms.ModelForm):
    class Meta:
        model = models.Servico
        fields = ('nome', 'descricao', 'ramo_atividade', 'sigla',)
