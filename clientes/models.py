#from djongo import models
from django.db import models

# Create your models here.

class Cliente(models.Model):
	nombre = models.CharField(max_length=100,)
	numero = models.IntegerField()
	password = models.CharField(max_length=10)
	ip = models.CharField(max_length=20)

	def __str__(self):
		return self.nombre


class Main(models.Model):
	nombre = models.ForeignKey('Cliente', on_delete=models.PROTECT, default="MOSAYK")
	numero = models.IntegerField()
	frase1menu = models.CharField(max_length=100)
	frase2menu = models.CharField(max_length=100)
	im = models.ImageField(upload_to='',default ='logo_M.png')

	def __str__(self):
		return str(self.numero)
# Create your models here.
