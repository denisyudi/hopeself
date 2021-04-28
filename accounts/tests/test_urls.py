from django.test import SimpleTestCase
from django.urls import reverse, resolve
from accounts.views import home, medico_confirm, admin_confirm, paciente_confirm, admin_main, medico_main, paciente_main


class TestUrls(SimpleTestCase):

    def test_home_url_resolves(self):
        url = reverse('home')
        # print(resolve(url))
        self.assertEqual(resolve(url).func, home)

    def test_admin_confirm_url_resolves(self):
        url = reverse('adminconfirm')
        # print(resolve(url))
        self.assertEqual(resolve(url).func, admin_confirm)

    def test_medico_confirm_url_resolves(self):
        url = reverse('medicoconfirm')
        # print(resolve(url))
        self.assertEqual(resolve(url).func, medico_confirm)

    def test_paciente_confirm_url_resolves(self):
        url = reverse('pacienteconfirm')
        # print(resolve(url))
        self.assertEqual(resolve(url).func, paciente_confirm)

    def test_sdmin_main_url_resolves(self):
        url = reverse('admin-main')
        # print(resolve(url))
        self.assertEqual(resolve(url).func, admin_main)

    def test_medico_main_url_resolves(self):
        url = reverse('medico-main')
        # print(resolve(url))
        self.assertEqual(resolve(url).func, medico_main)

    def test_paciente_main_url_resolves(self):
        url = reverse('paciente-main')
        # print(resolve(url))
        self.assertEqual(resolve(url).func, paciente_main)
