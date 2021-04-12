from django.db import models
from django.contrib.auth.models import User

class Medico(models.Model):
    ESPECIALIDADES = (
        ('Cardiologista', 'Cardiologista'),
        ('Clínico Geral', 'Clínico Geral'),
        ('Dermatologista', 'Dermatologista'),
        ('Ortopedista', 'Ortopedista'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    crm = models.CharField(max_length=15, null=True)
    endereco = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    fone = models.CharField(max_length=20, null=True)
    especialidade = models.CharField(max_length=50, choices=ESPECIALIDADES, null=True)
    status = models.BooleanField(default=True)
    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return "{} ({})".format(self.user.first_name, self.especialidade)

class Paciente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    cpf = models.CharField(max_length=15, null=True)
    endereco = models.CharField(max_length=40, null=True)
    email = models.CharField(max_length=100, null=True)
    fone = models.CharField(max_length=20, null=True)
    sintomas = models.CharField(max_length=100, null=True)
    assignedDoctorId = models.PositiveIntegerField(null=True)
    status = models.BooleanField(default=True)
    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name + " (" + self.sintomas + ")"

class Consulta(models.Model):
    id_paciente = models.PositiveIntegerField(null=True)
    id_medico = models.PositiveIntegerField(null=True)
    nome_paciente = models.CharField(max_length=40,null=True)
    nome_medico = models.CharField(max_length=40,null=True)
    data = models.DateTimeField(null=True)
    descricao = models.TextField(max_length=500, null=True)
    status = models.BooleanField(default=True)