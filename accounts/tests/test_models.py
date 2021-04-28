from django.test import TestCase
from accounts.models import Medico, Paciente, Consulta
from django.contrib.auth.models import User


class TestModels(TestCase):

    def setUp(self):
        self.consulta6 = Consulta.objects.create(
            id_paciente=1,
            id_medico=1,
            nome_paciente='paciente1',
            nome_medico='medico1'
        )

    def test_consulta_add(self):
        return self.assertEquals(self.consulta6.nome_medico, 'medico1')
