
# Create your models here.
from django.contrib.auth.models import User
from django.db import models


enum = (('1','M'),('2','F'))


class Area (models.Model):
    nombreArea = models.CharField(max_length=45)
    descripcionArea = models.TextField()
    estado=models.BooleanField()

    class Meta:
        verbose_name = 'Area'
        verbose_name_plural = 'Areas'

    def __str__(self):
        return self.nombreArea

class Cuestionario(models.Model):
    area = models.OneToOneField(Area,blank=True,null=True,on_delete=models.CASCADE)
    titulo = models.CharField(max_length=45)
    fechaRealizacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Cuestionario'
        verbose_name_plural = 'Cuestionarios'

    def __str__(self):
        return self.titulo

#Agrega Modelo tipo pregunta
class TipoPregunta(models.Model):
    tipo = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Tipo Pregunta'
        verbose_name_plural = 'Tipo Preguntas'


    def __str__(self):
        return self.tipo
#Crear modelo de cuestionariorspondido y en
# ella gregar el usuario y cuestionario

class CuestionarioRespondido(models.Model):
    es_supervisor = models.BooleanField(default=False)
    area = models.ForeignKey(Area,blank=False,null=False,on_delete=models.CASCADE)
    usuario = models.ForeignKey(User,blank=False,null=False, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=45)
    fechaRealizacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class PreguntaRespondida(models.Model):

    pregunta = models.CharField(max_length=50)
    respuesta =  models.CharField(max_length=20)
    CuestionarioRespondido = models.ForeignKey(CuestionarioRespondido,blank=False, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.pregunta


class Pregunta(models.Model):
    pregunta = models.CharField(max_length=100)
    cuestionario = models.ForeignKey(Cuestionario, blank=True, null=True, on_delete=models.CASCADE)
    tipoPregunta = models.ForeignKey(TipoPregunta, related_name='interviews', blank=False, null=False,  on_delete = models.CASCADE)

    class Meta:
        verbose_name = 'Pregunta'
        verbose_name_plural = 'Preguntas'

    def __str__(self):
        return self.pregunta

class Puesto (models.Model):
    nombrePuesto = models.CharField(max_length=45)


    class Meta:
        verbose_name = 'Puesto'
        verbose_name_plural = 'Puestos'

    def __str__(self):
        return self.nombrePuesto

class Empleado(models.Model):
    user = models.OneToOneField(User,blank=False,null=False, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=45)
    email = models.CharField(max_length=70, blank=False, null=False)
    puesto = models.ForeignKey(Puesto, blank=False, null=False, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
        return self.user.username


class Pregunta_Filtro(models.Model):
    preguntaFiltro = models.CharField(max_length=200)
    estado = models.BooleanField()

    class Meta:
        verbose_name = 'Pregunta Filtro'


    def __str__(self):
        return self.preguntaFiltro


class Personal(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    fecha_date = models.DateTimeField()
    fecha_ingreso = models.DateTimeField()
    sexo = models.CharField(max_length= 2, choices =enum)
    no_empleado = models.CharField(max_length=10)


class Posicion(models.Model):
    posicion = models.CharField(max_length=50)

class Turnos(models.Model):
    turno = models.CharField(max_length=25)
    hora_inicio = models.TimeField()
    hora_final = models.TimeField()
    activo = models.BooleanField()

class Seglog(models.Model):
    SegLogKey = models.IntegerField()
    SegLogFecha = models.DateTimeField()
    SegLogHora = models.TimeField()
    SegLogDetall = models.CharField(max_length=400)
    SegLogComando = models.CharField(max_length=400)
    SegLogComando = models.CharField(max_length=400)
    SegLogIp = models.CharField(max_length=20)
