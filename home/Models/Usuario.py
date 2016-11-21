from django.db import models
from django.contrib.auth.models import User

 
class Usuario(models.Model):
    user = models.OneToOneField(User)
    empresaId = models.ForeignKey()

