# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal_pages', '0030_marketplaceentrypage_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marketplaceentrypage',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
