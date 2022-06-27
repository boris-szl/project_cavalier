from django.db import models


# Create your models here
class RoicData(models.Model):
	# pandas to sql
	data = models.CharField(max_length=255)