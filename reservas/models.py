from django.db import models

# Create your models here.
class Docente(models.Model):
	nombre = models.CharField(max_length=100)
	apellido = models.CharField(max_length=100)

	def __str__(self):
		return "{0}, {1}".format(self.apellido, self.nombre)

class Bedel(models.Model):
	nombre = models.CharField(max_length=100)
	apellido = models.CharField(max_length=100)

	def __str__(self):
		return "{0}, {1}".format(self.apellido, self.nombre)

class Aula(models.Model):
	nombre = models.CharField(max_length=15)
	plazas = models.IntegerField()
	tipo_pizarra = models.CharField(max_length=1, choices=[('1','pizarra verde'),('2','pizarra blanca')],default=1)
	tipo_aula = models.CharField(max_length=1, choices=[('1','pupitres'),('2','mesa compartida'),('3','mesa dibujo'),('4','solo silla')], default=1)
	ubicacion = models.TextField()

	def __str__(self):
		return "{0} ({1})".format(self.nombre, self.plazas)

class Reserva(models.Model):
	aula = models.ForeignKey(Aula,on_delete=models.PROTECT)
	docente = models.ForeignKey(Docente,on_delete=models.PROTECT)
	fecha = models.DateField()
	hora_inicio = models.TimeField()
	hora_fin = models.TimeField()

	def __str__(self):
		return "{0} {1} {2} {3} {4}".format(self.aula, self.docente, self.fecha, self.hora_inicio, self.hora_fin)

class Feriado(models.Model):
	fecha = models.DateField()
	descripcion = models.CharField(max_length=300)