# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import wagtail.core.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal_pages', '0042_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='casestudyindexpage',
            name='submit_info',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='casestudyindexpage',
            name='thanks_info',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
    ]
