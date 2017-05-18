	# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Server
from .models import Team

# Create your views here.

def search_list(request):
	faculty = Server.objects.order_by('tracked_user').values_list('tracked_user', flat=True).distinct()

	team = [ ('Access Point Setup Team', (Team.objects.filter(team='AP'))),
		('Android App Dev Team', (Team.objects.filter(team='AD'))),
		('Server Setup Team', (Team.objects.filter(team='SS'))),
		('User Interface Team', (Team.objects.filter(team='UI'))) ]

	key = request.GET.get('search')
	if key:
		try:
			result = Server.objects.filter(tracked_user=key).latest('last_update')
		except Server.DoesNotExist:
			result = None

		if not result:
			result = "'%s' is not on TrackEEEr." % (key)

	else:
		result = "Track your EEE professors!"
	return render(request,'search/search_list.html', {'faculty':faculty,'result':result,'team':team})
