# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0006_add_verbose_names'),
        ('portal_pages', '0035_auto_20150521_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='cmspage',
            name='top_image',
            field=models.ForeignKey(null=True, related_name='+', to='wagtailimages.Image', on_delete=django.db.models.deletion.SET_NULL, blank=True),
        ),
    ]
