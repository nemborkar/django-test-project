from django.db import models

# Create your models here.

# the following will be used to connect to the database
class Product(models.Model):
	title = models.CharField(max_length=80)
	description = models.TextField(blank=True, null=True)
	price = models.DecimalField(max_digits=8, decimal_places=2)
	summary = models.TextField(default='This is cool!')
	features = models.BooleanField(default=0)