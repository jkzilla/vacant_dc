# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class VacantLocation(models.Model):
	""" CSV Data Fields, Example
	XCoord, -77.00836160
	YCoord, 38.82424784
	FID, 0
	OBJECTID, 818429
	BBL_LICENS, 216370
	LICENSESTA, EXPIRED 
	LICENSECAT, Apartment
	CUST_NUM, 70102652
	LICENSE_ST, 010-04-01T00:00:00.000Z
	LICENSE_EX, 2
	LICENSE_IS, 2012-03-31T00:00:00.000Z
	AGENT_PHON, 2012-05-06T00:00:00.000Z
	LASTMODIFI, 2012-05-15T09:49:47.000Z
	CITY, WASHINGTON
	STATE, DC
	SITEADDRES, 26 GALVESTON PLACE SW
	LATITUDE, 38.824240
	LONGITUDE, -77.008359
	XCOORD, 399274.110000
	YCOORD, 128495.430000
	ZIPCODE, 20032
	MARADDRESS, 46110
	DCSTATADDR, 1068
	DCSTATLOCA, 1068
	WARD, 8
	ANC, 8D
	SMD, 8D04
	DISTRICT, SEVENTH
	PSA, 708
	NEIGHBORHO, 39
	HOTSPOT200, NONE
	HOTSPOT2_1, NONE
	HOTSPOT2_2, NONE
	BUSINESSIM, NONE
	"""
	latitude = models.IntegerField(default=0)
	longitude = models.IntegerField(default=0)
	site_address = models.CharField(max_length=200)
	city = models.CharField(max_length=200)
	state = models.CharField(max_length=200)

	def __str__(self):
		return self.site_address + ", " + self.city + ", " + self.state 
