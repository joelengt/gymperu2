# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-05 08:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='convenio',
            name='titulo',
            field=models.CharField(default='Convenio', max_length=20),
        ),
        migrations.AddField(
            model_name='entrenar',
            name='titulo',
            field=models.CharField(default='Entrenar', max_length=20),
        ),
        migrations.AddField(
            model_name='nutricion',
            name='titulo',
            field=models.CharField(default='Nutricion', max_length=20),
        ),
    ]
