# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal_pages', '0009_auto_20150421_1450'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='casestudypage',
            name='feed_image',
        ),
    ]
