# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-23 22:29
from __future__ import unicode_literals

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0023_product_image_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image_thumbnail',
            field=django_resized.forms.ResizedImageField(blank=True, null=True, upload_to=b''),
        ),
    ]
