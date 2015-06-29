# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal_pages', '0031_region_regioncasestudy_regionmarketplaceentry'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='region',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='region',
            name='longitude',
        ),
    ]
