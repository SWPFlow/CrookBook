# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-28 07:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0015_auto_20171128_0708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
