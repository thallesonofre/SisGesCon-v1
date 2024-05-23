from django.db import models
from django.contrib.auth.models import User


# cria a área de perfil do usuário
class Perfil(models.Model):
    nome_completo = models.CharField(max_length=50, null=True)
    cpf = models.CharField(max_length=14, null=True, verbose_name="CPF")
    telefone = models.CharField(max_length=17, null=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.nome_completo