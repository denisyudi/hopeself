from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('', views.home),
    path('adminconfirm', views.admin_confirm),
    path('medicoconfirm', views.medico_confirm),
    path('pacienteconfirm', views.paciente_confirm),

    path('adminregister', views.admin_register),
    path('medicoregister', views.medico_register,name='medicoregister'),
    path('pacienteregister', views.paciente_register),

    path('adminlogin', LoginView.as_view(template_name='accounts/adminlogin.html')),
    path('medicologin', LoginView.as_view(template_name='accounts/medicologin.html')),
    path('pacientelogin', LoginView.as_view(template_name='accounts/pacientelogin.html')),

    path('afterlogin', views.after_login, name='afterlogin'),
    path('logout', LogoutView.as_view(template_name='accounts/index.html'), name='logout'),

    path('admin-main', views.admin_main, name='admin-main'),
    path('admin-medicos', views.admin_medicos, name='admin-medicos'),
    path('admin-lista-medicos', views.admin_lista_medicos, name='admin-lista-medicos'),
    path('admin-aceita-medico', views.admin_aceita_medico, name='admin-aceita-medico'),
    path('aceita-medico/<int:pk>', views.aceita_medico, name='aceita-medico'),
    path('admin-pacientes', views.admin_pacientes, name='admin-pacientes'),
    path('admin-lista-pacientes', views.admin_lista_pacientes, name='admin-lista-pacientes'),
    path('admin-consultas', views.admin_consultas, name='admin-consultas'),
    path('admin-lista-consultas', views.admin_lista_consultas, name='admin-lista-consultas'),

    #medico
    path('medico-main', views.medico_main, name='medico-main'),

    path('medico-pacientes', views.medico_pacientes, name='medico-pacientes'),
    path('medico-lista-pacientes', views.medico_lista_pacientes, name='medico-lista-pacientes'),
]