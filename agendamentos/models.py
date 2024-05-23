from datetime import date, time, datetime
from django.db import models
from django.contrib.auth.models import User



class Paciente(models.Model):
    data_cadastro = models.DateField(null=False, blank=False)
    nome_paciente = models.CharField(verbose_name="Paciente", max_length=55, null=False, blank=False)
    idade = models.CharField(max_length=5, null=False, blank=False)
    telefone = models.CharField(max_length=14, null=False, blank=False)
    edereco = models.CharField(max_length=100, null=False, blank=False)
    cadastrado_por = models.ForeignKey(User, on_delete=models.PROTECT)
    
    class Meta:
        ordering = ['data_cadastro']
    
    def __str__(self) -> str:
        return self.nome_paciente
    
    
class Procedimento(models.Model):
    nome_procedimento = models.CharField(max_length=50, null=False, blank=False)
    valor_procedimento = models.IntegerField(null=False, blank=False)
    
    class Meta:
        ordering = ['nome_procedimento']
    
    def __str__(self) -> str:
        return self.nome_procedimento

    
class Agenda(models.Model):
    data = models.DateField(null=False, blank=False)
    inicio_atendimento = models.TimeField(null=False, blank=False)
    nome_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    tipo_consulta = models.ForeignKey(Procedimento, on_delete=models.CASCADE)
    valor_consulta = models.IntegerField(null=False, blank=False)
    fim_atendimento = models.DateTimeField(null=True,blank = True)
    profissional = models.ForeignKey(User, on_delete=models.PROTECT)
    
    class Meta:
        ordering = ['data']
        
     
     
    def fim_sessao(self):
        if not self.fim_atendimento:
            self.fim_atendimento = datetime.now()
            self.save()   

      
        

