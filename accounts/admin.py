from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Medico)
admin.site.register(Paciente)
admin.site.register(Consulta)