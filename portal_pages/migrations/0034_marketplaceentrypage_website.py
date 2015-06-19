# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal_pages', '0033_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='marketplaceentrypage',
            name='website',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
