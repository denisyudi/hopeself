from django.contrib import admin
from .models import Medico, Paciente, Consulta


# Register your models here.
class MedicoAdmin(admin.ModelAdmin):
    pass


admin.site.register(Medico, MedicoAdmin)


class PacienteAdmin(admin.ModelAdmin):
    pass


admin.site.register(Paciente, PacienteAdmin)


class ConsultaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Consulta, ConsultaAdmin)
