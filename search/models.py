# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone

class Faculty(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = "Faculty"

class Server(models.Model):
	name = models.CharField(max_length=50)
	desc = models.TextField()
	location = models.CharField(max_length=50)
	push_date = models.DateTimeField(blank=True, null=True)

	def pubish(self):
		self.publish_date = timezone.now()
		self.save()

	def __str__(self):
		return self.location

	class Meta:
		get_latest_by = 'push_date'
		verbose_name_plural = "Server"

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