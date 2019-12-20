from django.db import models

class Relator(models.Model):
	nombre=models.CharField(max_length=10,blank=False,null=True)
	edad=models.IntegerField(blank=False,null=True)
	def __str__(self):
		return u'%s' % (self.nombre)

		