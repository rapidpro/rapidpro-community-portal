# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal_pages', '0029_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='marketplaceentrypage',
            name='state',
            field=models.CharField(max_length=255, blank=True),
            preserve_default=True,
        ),
    ]
