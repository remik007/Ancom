# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-23 19:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0014_slider_first'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slider',
            old_name='title',
            new_name='name',
        ),
    ]