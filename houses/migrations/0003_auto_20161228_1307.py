# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-28 10:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0002_auto_20161228_1223'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='house',
            options={'ordering': ['name'], 'verbose_name': 'дом', 'verbose_name_plural': 'дома'},
        ),
        migrations.AddField(
            model_name='house',
            name='photo',
            field=models.ImageField(blank=True, default='', upload_to='houses/photos', verbose_name='фотография'),
        ),
    ]
