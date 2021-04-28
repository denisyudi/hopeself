from django import forms
from django.contrib.auth.models import User
from . import models


class AdminRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }


class MedicoRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }


class MedicoForm(forms.ModelForm):
    class Meta:
        model = models.Medico
        fields = ['crm', 'endereco', 'email', 'fone', 'especialidade', 'status']


class PacienteRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }


class PacienteForm(forms.ModelForm):
    class Meta:
        model = models.Paciente
        fields = ['cpf', 'endereco', 'email', 'fone', 'sintomas', 'status']


class ConsultaForm(forms.ModelForm):
    id_medico = forms.ModelChoiceField(queryset=models.Medico.objects.all().filter(status=True), empty_label="Doctor Name and Department", to_field_name="user_id")
    id_paciente = forms.ModelChoiceField(queryset=models.Paciente.objects.all().filter(status=True), empty_label="Patient Name and Symptoms", to_field_name="user_id")

    class Meta:
        model = models.Consulta
        fields = ['descricao', 'status']
