from django.db import models

# Create your models here.
class Friend(models.Model):
	name = models.CharField(max_length=27)
	url = models.URLField()
	created_date = models.DateTimeField(auto_now_add=True)