# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-05 08:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clases', '0002_auto_20160328_2136'),
    ]

    operations = [
        migrations.AddField(
            model_name='aerobicos',
            name='titulo',
            field=models.CharField(default='Aerobicos', max_length=15),
        ),
        migrations.AddField(
            model_name='bestcyclng',
            name='titulo',
            field=models.CharField(default='Bestcycling', max_length=20),
        ),
        migrations.AddField(
            model_name='deportesdecontacto',
            name='titulo',
            field=models.CharField(default='Deportes de Contacto', max_length=40),
        ),
        migrations.AddField(
            model_name='talleres',
            name='titulo',
            field=models.CharField(default='Talleres', max_length=15),
        ),
    ]
