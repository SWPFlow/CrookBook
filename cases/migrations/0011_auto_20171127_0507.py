# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-27 05:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0010_auto_20171127_0358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='suspects',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='suspects1', to='cases.Person'),
        ),
        migrations.AlterField(
            model_name='case',
            name='victims',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='victims1', to='cases.Person'),
        ),
    ]