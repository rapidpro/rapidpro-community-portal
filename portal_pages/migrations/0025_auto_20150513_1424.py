# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal_pages', '0024_auto_20150512_1426'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='expertise',
            options={'ordering': ('name',), 'verbose_name_plural': 'expertise'},
        ),
    ]
