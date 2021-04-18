from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('', views.home),
    path('adminconfirm', views.admin_confirm),
    path('medicoconfirm', views.medico_confirm),
    path('pacienteconfirm', views.paciente_confirm),

    path('adminregister', views.admin_register),
    path('medicoregister', views.medico_register, name='medicoregister'),
    path('pacienteregister', views.paciente_register),

    path('adminlogin', LoginView.as_view(template_name='accounts/adminlogin.html')),
    path('medicologin', LoginView.as_view(template_name='accounts/medicologin.html')),
    path('pacientelogin', LoginView.as_view(template_name='accounts/pacientelogin.html')),

    path('afterlogin', views.after_login, name='afterlogin'),
    path('logout', LogoutView.as_view(template_name='accounts/index.html'), name='logout'),

    #admin
    path('admin-main', views.admin_main, name='admin-main'),
    path('admin-medicos', views.admin_medicos, name='admin-medicos'),
    path('admin-pacientes', views.admin_pacientes, name='admin-pacientes'),
    path('admin-notificacoes', views.admin_notificacoes, name='admin-notificacoes'),
    path('admin-dados', views.admin_dados, name='admin-dados'),

    #medico
    path('medico-main', views.medico_main, name='medico-main'),
    path('medico-pacientes', views.medico_pacientes, name='medico-pacientes'),
    path('medico-consultas', views.medico_consultas, name='medico-consultas'),
    path('medico-notificacoes', views.medico_notificacoes, name='medico-notificacoes'),
    path('medico-dados', views.medico_dados, name='medico-dados'),
    
    #paciente
    path('paciente-main', views.paciente_main, name='paciente-main'),
    path('paciente-consultas', views.paciente_consultas, name='paciente-consultas'),
    path('paciente-notificacoes', views.paciente_notificacoes, name='paciente-notificacoes'),
    path('paciente-historico', views.paciente_historico, name='paciente-historico'),
    path('paciente-agendar-consulta', views.paciente_agendar_consulta, name='paciente-agendar-consulta'),
    path('paciente-dados', views.paciente_dados, name='paciente-dados'),
]