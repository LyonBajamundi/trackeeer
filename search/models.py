# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Server(models.Model):
	tracked_user = models.CharField(max_length=50)
	desc = models.TextField()
	gen_location= models.CharField(max_length=50)
	last_update = models.DateTimeField(blank=True, null=True)

	def __str__(self):
		return "%s is in %s as of %s" % (self.tracked_user, self.gen_location, self.last_update)

	class Meta:
		get_latest_by = 'last_update'
		verbose_name_plural = "Server"
		db_table = 'trackeeed'
		managed = True

class Team(models.Model):
	name = models.CharField(max_length=50)
	AP = 'AP'
	AD = 'AD'
	SS = 'SS'
	UI = 'UI'
	TEAM_CHOICES = (
		(AP, 'Access Point Setup'),	
		(AD, 'Android App Dev'),
		(SS, 'Server Setup'),
		(UI, 'User Interface'),
	)
	team = models.CharField(
		max_length=2,
		choices=TEAM_CHOICES,
		default=AP,
	)

	def __str__(self):
		return self.name