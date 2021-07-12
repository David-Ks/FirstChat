from django.db import models
from django.contrib.auth.models import User

class ChatModel(models.Model):
	name = models.CharField(max_length=60, verbose_name='Имя', blank=True, default="Noname")
	text = models.CharField(max_length=200, verbose_name='')
	data = models.DateField(auto_now_add=True)
	refreshrate = models.IntegerField(verbose_name='PRR', default=2000)
	is_published = models.BooleanField(default=True)


	def __str__(self):
		return str(self.pk)


	class Meta:
		verbose_name = 'Чат'
		verbose_name_plural = 'Чаты'
		#ordering = [-1]
