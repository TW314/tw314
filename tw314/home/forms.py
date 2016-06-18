from django import forms

from . import models


class StsForm(forms.ModelForm):
    class Meta:
        model = models.Status
        fields = ('nome', 'descricao',)


class EmpForm(forms.ModelForm):
    class Meta:
        model = models.Empresa
        fields = ('nome_fantasia', 'razao_social', 'nr_cnpj', 'logradouro',
                  'nr_logradouro', 'cidade', 'uf', 'pais', 'telefone', 'email',
                  'nome_responsavel', 'cargo_responsavel', 'cpf_responsavel',
                  'data_abertura', 'data_ativacao', #'data_inativacao'
                  'ramo_atividade_id', 'status_id')


class RamForm(forms.ModelForm):
    class Meta:
        model = models.RamoAtividade
        fields = ('nome',)
