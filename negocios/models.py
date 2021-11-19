from django.db import models

class Negocio(models.Model):
    area_choices = (
        ('Alimentos', 'Alimentos'),
        ('Artesanias', 'Artesanias'),
    )

    planta_choices = (
        ('Baja', 'Baja'),
        ('Alta', 'Alta'),
    )
    nombre = models.CharField(max_length=30)
    area = models.CharField(max_length=30, choices=area_choices)
    propietario = models.CharField(max_length=30)
    descripcion = models.TextField()
    planta = models.CharField(max_length=5, choices=planta_choices)
    numero_local = models.IntegerField()

    email = models.EmailField(max_length=30)

    realiza_envios = models.BooleanField()
    fotografia = models.ImageField()

class Horario(models.Model):
    dias_choices = (
        ('Lunes', 'Lunes'),
        ('Martes', 'Martes'),
        ('Miercoles', 'Miercoles'),
        ('Jueves', 'Jueves'),
        ('Viernes', 'Viernes'),
        ('Sabado', 'Sabado'),
        ('Domingo', 'Domingo'),
        ('Todos los dias', 'Todos los dias'),
    )
    negocio = models.ForeignKey(Negocio, on_delete=models.CASCADE)
    dia_inicio = models.CharField(max_length=14, choices=dias_choices)
    dia_fin = models.CharField(max_length=14, choices=dias_choices)