

from django.db import models
from django.utils import timezone


class ramo_atividade(models.Model):
    nome = models.CharField(max_length=45)
    descricao = models.CharField(max_length=200)
    status = models.CharField(max_length=8)





