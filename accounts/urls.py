from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('historico/', views.historico),
    path('consultas/', views.consultas),
    path('dashboard/', views.dashboard),
]