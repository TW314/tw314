from django import forms

from .models import STS_STATUS, EMP_EMPRESA, RMO_RAMO_ATIVIDADE, USU_USUARIO, PFL_PERFIL, SVC_SERVICO, CHA_CHAMADO, REL_EMPRESA_SERVICO, TCK_TICKET, ATD_ATENDIMENTO


class StsForm(forms.ModelForm):
    class Meta:
        model = STS_STATUS
        fields = ('STS_NOME', 'STS_DESCRICAO',)
