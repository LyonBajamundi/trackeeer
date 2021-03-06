# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-18 21:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Faculty',
            },
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tracked_user', models.CharField(max_length=50)),
                ('desc', models.TextField()),
                ('gen_location', models.CharField(max_length=50)),
                ('last_update', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Server',
                'db_table': 'trackeeed',
                'get_latest_by': 'last_update',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('team', models.CharField(choices=[('AP', 'Access Point Setup'), ('AD', 'Android App Dev'), ('SS', 'Server Setup'), ('UI', 'User Interface')], default='AP', max_length=2)),
            ],
        ),
    ]
