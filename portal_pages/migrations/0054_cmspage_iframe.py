# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal_pages', '0053_techchangepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='cmspage',
            name='iframe',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
