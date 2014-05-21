from django.db import models

# Create your models here.


class Polygon(models.Model):
	points = models.CharField(max_length=1000)
	border_color = models.CharField(max_length=7)
	background_color = models.CharField(max_length=7)
	info_text = models.TextField(max_length=300)
	date = models.DateTimeField(auto_now=True)
