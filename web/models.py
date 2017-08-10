from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Token(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	token = models.CharField(max_length = 48)
	def __str__(self):
		return "{}_Token".format(self.user)
class Kharj(models.Model):
	text = models.CharField(max_length = 255)
	date = models.DateTimeField()
	amount = models.BigIntegerField()
	user = models.ForeignKey(User)
	def __str__(self):
		return '{}-{}'.format(self.text,self.date)

class Dakhl(models.Model):
	text = models.CharField(max_length = 255)
	date = models.DateTimeField()
	amount = models.BigIntegerField()
	user = models.ForeignKey(User)
	def __str__(self):
		return '{}-{}'.format(self.text,self.date)