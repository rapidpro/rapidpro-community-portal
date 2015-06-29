# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal_pages', '0024_auto_20150512_1426'),
    ]

    operations = [
        migrations.RenameField(
            model_name='casestudypage',
            old_name='hero_image',
            new_name='top_image',
        ),
    ]
