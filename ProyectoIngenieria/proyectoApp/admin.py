

# Register your models here.
from django.contrib import admin

# Register your models here.
from proyectoApp.models import Area, Cuestionario, Pregunta, Puesto, Empleado, Pregunta_Filtro,  CuestionarioRespondido, TipoPregunta
from proyectoApp.models import PreguntaRespondida

admin.site.site_header = 'Panel de administracion'

class Preguntas(admin.ModelAdmin):
    list_display = ['pregunta','tipoPregunta']
    list_filter= [
        'cuestionario'
    ]

admin.site.register(Area)
admin.site.register(Cuestionario)
admin.site.register(Pregunta,Preguntas)
admin.site.register(Puesto)
admin.site.register(Empleado)
admin.site.register(Pregunta_Filtro)
admin.site.register(CuestionarioRespondido)
admin.site.register(PreguntaRespondida)
admin.site.register(TipoPregunta)
