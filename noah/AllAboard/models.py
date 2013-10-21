from django.db import models

class Animal(models.Model):
	name = models.CharField(max_length=40)
	numberOfLegs = models.IntegerField()
	onBoard = models.BooleanField()
	def __unicode__(self):
	       return self.name

