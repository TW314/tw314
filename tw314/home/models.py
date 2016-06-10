from django.db import models
from django.utils import timezone


class STS_STATUS(models.Model):
    STS_NOME = models.CharField(max_length=45)
    STS_DESCRICAO = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.title


class RMO_RAMO_ATIVIDADE(models.Model):
    RMO_NOME = models.CharField(max_length=45)
    STS_ID = models.ForeignKey('RMO_RAMO_ATIVIDADE', on_delete=models.CASCADE)

    def publish(self):
        """self.published_date = timezone.now()"""
        self.save()

    def __str__(self):
        return self.title


class EMP_EMPRESA(models.Model):
    EMP_NOME_FANTASIA = models.CharField(max_length=80)
    EMP_RAZAO_SOCIAL = models.CharField(max_length=80)
    EMP_NR_CNPJ = models.CharField(max_length=14)
    EMP_LOGRADOURO = models.CharField(max_length=255)
    EMP_NR_LOGRADOURO = models.CharField(max_length=255)
    EMP_CIDADE = models.CharField(max_length=100)
    EMP_UF = models.CharField(max_length=2)
    EMP_PAIS = models.CharField(max_length=100)
    EMP_TELEFONE = models.CharField(max_length=11)
    EMP_EMAIL = models.EmailField(max_length=100)
    EMP_NOME_RESPONSAVEL = models.CharField(max_length=80)
    EMP_CARGO_RESPONSAVEL = models.CharField(max_length=45)
    EMP_CPF_RESPONSAVEL = models.CharField(max_length=11)
    EMP_DT_ABERTURA = models.DateField(timezone.now())
    EMP_DT_ATIVACAO = models.DateField(timezone.now())
    EMP_DT_INATIVACAO = models.DateField().null

    STS_ID = models.ForeignKey('RMO_RAMO_ATIVIDADE', on_delete=models.CASCADE)
    RMO_ID = models.ForeignKey('STS_STATUS', on_delete=models.CASCADE)

    def publish(self):
        """self.published_date = timezone.now()"""
        self.save()

    def __str__(self):
        return self.title


class PFL_PERFIL(models.Model):
    PFL_NOME = models.CharField(max_length=80)
    PFL_DESCRICAO = models.TextField()

    def publish(self):
        """self.published_date = timezone.now()"""
        self.save()

    def __str__(self):
        return self.title


class USU_USUARIO(models.Model):
    USU_NOME = models.CharField(max_length=80)
    USU_EMAIL = models.EmailField(max_length=100)
    USU_LOGIN = models.CharField(max_length=45)
    USU_SENHA = models.CharField(max_length=45)
    USU_DT_ATIVACAO = models.DateField(timezone.now())
    USU_DT_INATIVACAO = models.DateField().null

    STS_ID = models.ForeignKey('RMO_RAMO_ATIVIDADE', on_delete=models.CASCADE)
    EMP_ID = models.ForeignKey('EMP_EMPRESA', on_delete=models.CASCADE)
    PFL_ID = models.ForeignKey('PFL_PERFIL', on_delete=models.CASCADE)

    def publish(self):
        """self.published_date = timezone.now()"""
        self.save()

    def __str__(self):
        return self.title


class SVC_SERVICO(models.Model):
    SVC_NOME = models.CharField(max_length=45)
    SVC_DESCRICAO =  models.TextField()
    RMO_ID = models.ForeignKey('RMO_RAMO_ATIVIDADE', on_delete=models.CASCADE)

    def publish(self):
        """self.published_date = timezone.now()"""
        self.save()

    def __str__(self):
        return self.title


class CHA_CHAMADO(models.Model):
    CHA_DT_ABERTURA = models.DateField(timezone.now())
    CHA_DT_ATUALIZACAO = models.DateField().null
    CHA_ASSUNTO = models.CharField(max_length=255)
    CHA_MENSAGEM = models.TextField()

    STS_ID = models.ForeignKey('STS_STATUS', on_delete=models.CASCADE)
    USU_ID_ABERTURA = models.ForeignKey('USU_USUARIO', on_delete=models.CASCADE)
    USU_ID_RESPOSTA = models.ForeignKey('USU_USUARIO', on_delete=models.CASCADE).null

    def publish(self):
        """self.published_date = timezone.now()"""
        self.save()

    def __str__(self):
        return self.title


class REL_EMPRESA_SERVICO():
    SVC_ID = models.ForeignKey('RMO_RAMO_ATIVIDADE', on_delete=models.CASCADE).primary_key
    EMP_ID = models.ForeignKey('EMP_EMPRESA', on_delete=models.CASCADE).primary_key


class TCK_TICKET(models.Model):
    TCK_NR_TICKET = models.IntegerField()
    TCK_DTHR_EMISSAO = models.DateTimeField(timezone.now())
    TCK_CD_ACESSO = models.CharField(max_length=8)


    EMP_ID = models.ForeignKey('EMP_EMPRESA', on_delete=models.CASCADE)
    SVC_ID = models.ForeignKey('SVC_SERVICO', on_delete=models.CASCADE, max_length=2)

    def publish(self):
        """self.published_date = timezone.now()"""
        self.save()

    def __str__(self):
        return self.title


class ATD_ATENDIMENTO(models.Model):
    ATD_DTHR_INICIO = models.DateTimeField(timezone.now())
    ATD_DTHR_FIM = models.DateTimeField(timezone.now()).null

    TCK_ID = models.ForeignKey('TCK_TICKET', on_delete=models.CASCADE).primary_key

    STS_ID = models.ForeignKey('STS_STATUS', on_delete=models.CASCADE)
    USU_ID = models.ForeignKey('USU_USUARIO', on_delete=models.CASCADE)

    def publish(self):
        """self.published_date = timezone.now()"""
        self.save()

    def __str__(self):
        return self.title
