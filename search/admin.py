# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Server
from .models import Team

admin.site.register(Server)
admin.site.register(Team)