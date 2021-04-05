from django.db import models

# Create your models here.

class Medico(models.Model):
    nome = models.CharField(max_length=200, null=True)
    especialidade = models.CharField(max_length=200, null=True)
    crm = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    fone = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.nome

class Paciente(models.Model):
    nome = models.CharField(max_length=200, null=True)
    cpf = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    fone = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.nome

class Consulta(models.Model):
    STATUS = (
        ('Confirmado', 'Confirmado'),
        ('Cancelado', 'Cancelado'),
    )
    medico = models.ForeignKey(Medico, null=True, on_delete=models.SET_NULL)
    paciente = models.ForeignKey(Paciente, null=True, on_delete=models.SET_NULL)
    data = models.DateTimeField(null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS) 