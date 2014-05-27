from django.db import models


QUARRY_NAMES = (
		(1, 'Nelson Aggregate'),
		(2, 'Waynco Aggregate'),
		(3, 'Uhthoff Quarry'),
		(4, 'Oneida Quarry'),
		(5, 'Lincoln Quarry'),
	)


class Price(models.Model):
	quarry = models.IntegerField(max_length=1, choices=QUARRY_NAMES, verbose_name='Quarry')
	tri_axel = models.IntegerField(max_length=10, verbose_name='Tri-axel')
	tractor_trailer = models.IntegerField(max_length=10, verbose_name='Tractor Trailer')
	stone_slinger = models.IntegerField(max_length=10, verbose_name='Stone Slinger')


class Polygon(models.Model):
	points = models.CharField(max_length=1000)
	title = models.CharField(max_length=10)
	color = models.CharField(max_length=7)
	prices = models.ManyToManyField('Price', null=True, blank=True)
	date = models.DateTimeField(auto_now=True)


class Quarry(models.Model):
	name = models.CharField(max_length=100)
	delivery_address = models.CharField(max_length=200)
	mailing_address = models.CharField(max_length=200)
	office = models.CharField(max_length=15)
	toll = models.CharField(max_length=15)
	fax = models.CharField(max_length=15)
	sales = models.CharField(max_length=50)
	latitude = models.CharField(max_length=50)
	longitude = models.CharField(max_length=50)