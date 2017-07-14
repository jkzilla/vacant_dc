# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class VacantLocation(models.Model):
	latitude = models.IntegerField(default=0)
	longitude = models.IntegerField(default=0)

	def __str__(self):
		return self.latitude + ", " + self.longitude
