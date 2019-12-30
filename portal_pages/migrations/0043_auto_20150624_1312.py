# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portal_pages', '0042_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='highlightitem',
            name='target_page_external',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='highlightitem',
            name='target_page',
            field=models.ForeignKey(blank=True, null=True, to='wagtailcore.Page', on_delete=django.db.models.deletion.CASCADE),
        ),
    ]
