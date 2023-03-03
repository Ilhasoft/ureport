# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-15 14:55
from __future__ import absolute_import, division, print_function, unicode_literals

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("countries", "0002_auto_20150722_1524")]

    operations = [
        migrations.AlterField(
            model_name="countryalias",
            name="created_on",
            field=models.DateTimeField(
                blank=True,
                default=django.utils.timezone.now,
                editable=False,
                help_text="When this item was originally created",
            ),
        ),
        migrations.AlterField(
            model_name="countryalias",
            name="modified_on",
            field=models.DateTimeField(
                blank=True,
                default=django.utils.timezone.now,
                editable=False,
                help_text="When this item was last modified",
            ),
        ),
    ]
