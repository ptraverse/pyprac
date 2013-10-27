from django.db import models

class Ad(models.Model):
	id_num = models.IntegerField()
	point_worth = models.IntegerField()
	ppv_cost = models.FloatField()
	def __unicode__(self):
		return self.id_num+","+self.point_worth+","+self.ppv_cost

class Person(models.Model):
	name = models.CharField(max_length=12)
	pc = models.IntegerField()
	def __unicode__(self):
                return self.name

class Lottery(models.Model):
	pool_total = models.FloatField()
	def __unicode__(self):
                return self.pool_total
