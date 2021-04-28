from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import Medico, Paciente, Consulta
import json


class TestViews(TestCase):

    def setUp(self):
        self.user = Client()


    def test_home_GET(self):

        response = self.user.get(reverse('home'))
        #print(response)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/index.html')

    def test_admin_confirm_GET(self):

            response = self.user.get(reverse('adminconfirm'))
            # print(response)

            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'accounts/adminconfirm.html')


    def test_medico_confirm_GET(self):

            response = self.user.get(reverse('medicoconfirm'))
            # print(response)

            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'accounts/medicoconfirm.html')


    def test_pacinte_confirm_GET(self):

            response = self.user.get(reverse('pacienteconfirm'))
            # print(response)

            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'accounts/pacienteconfirm.html')




    def test_admin_register_GET(self):

            response = self.user.get(reverse('adminregister'))
            # print(response)

            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'accounts/adminregister.html')



    def test_medico_register_GET(self):

            response = self.user.get(reverse('medicoregister'))
            # print(response)

            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'accounts/medicoregister.html')

    def test_paciente_register_GET(self):

            response = self.user.get(reverse('pacienteregister'))
            # print(response)

            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'accounts/pacienteregister.html')


