# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0005_make_filter_spec_unique'),
        ('portal_pages', '0026_auto_20150518_1029'),
    ]

    operations = [
        migrations.AddField(
            model_name='casestudyindexpage',
            name='top_image',
            field=models.ForeignKey(to='wagtailimages.Image', null=True, related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True),
            preserve_default=True,
        ),
    ]
