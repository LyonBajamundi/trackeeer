# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.utils import timezone
from .models import Faculty
from .models import Server
from .models import Team

# Create your views here.

def search_list(request):
	faculty = Faculty.objects.order_by('name')
	team = [ ('Access Point Setup Team', (Team.objects.filter(team='AP'))),
		('Android App Dev Team', (Team.objects.filter(team='AD'))),
		('Server Setup Team', (Team.objects.filter(team='SS'))),
		('User Interface Team', (Team.objects.filter(team='UI'))) ]


	key = request.GET.get('search')
	if key:
		try:
			location = Server.objects.filter(name=key).latest('push_date')
		except Server.DoesNotExist:
			location = None

		if location:
			result = "%s is in %s." % (key, location)
		elif location == "offline":
			result = "%s is offline." % (key)
		else:
			result = "'%s' is not on TrackEEEr." % (key)
	else:
		result = "Track your EEE professors!"
	return render(request,'search/search_list.html', {'faculty':faculty,'result':result,'team':team})
