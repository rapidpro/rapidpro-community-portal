# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal_pages', '0016_marketplaceindexpage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='focusarea',
            name='name',
            field=models.CharField(max_length=255, unique=True),
            preserve_default=True,
        ),
    ]
