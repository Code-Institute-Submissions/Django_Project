# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-13 15:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20171106_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=b'images'),
        ),
    ]