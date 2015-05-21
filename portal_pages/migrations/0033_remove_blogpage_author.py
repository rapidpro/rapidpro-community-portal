# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal_pages', '0032_blogpage_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpage',
            name='author',
        ),
    ]
