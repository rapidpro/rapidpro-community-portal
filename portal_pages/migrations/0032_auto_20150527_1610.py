# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0006_add_verbose_names'),
        ('portal_pages', '0031_auto_20150520_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogindexpage',
            name='top_image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, null=True, to='wagtailimages.Image', blank=True, related_name='+'),
        ),
    ]
