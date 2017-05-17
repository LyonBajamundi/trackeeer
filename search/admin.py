# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Server
from .models import Faculty
from .models import Team

admin.site.register(Server)
admin.site.register(Faculty)
admin.site.register(Team)
