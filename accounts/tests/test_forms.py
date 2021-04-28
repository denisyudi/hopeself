from django.test import SimpleTestCase
from accounts.forms import AdminRegisterForm, MedicoRegisterForm, PacienteRegisterForm, PacienteForm, MedicoForm


# class AdminForm(forms.Form):
#     first_name = forms.CharField()
#     last_name = forms.CharField()
#     username = forms.CharField()
#     password = forms.PasswordInput()


class TestForms(SimpleTestCase):

    def test_paciente_form_valid_data(self):
        form = PacienteForm(data={
            'cpf': 123456, 'endereco': 'rua 123, 6', 'email': 'paciente@mail.com',
            'fone': 123, 'sintomas': 'nsd', 'status': 'ok'
        })

        self.assertTrue(form.is_valid())

    def test_medico_form_valid_data(self):
        form = MedicoForm(data={
            'crm': 65989, 'endereco': 'rua rua', 'email': 'medico@mail.org',
            'fone': 45698, 'especialidade': 'Cardiologista', 'status': 'ok'
        })

        self.assertTrue(form.is_valid())

    def test_admin_register_form_no_data(self):
        form = AdminRegisterForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)

    def test_medico_register_form_no_data(self):
        form = MedicoRegisterForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)

    def test_paciente_register_form_no_data(self):
        form = PacienteRegisterForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)
