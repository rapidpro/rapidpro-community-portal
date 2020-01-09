# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0015_add_more_verbose_names'),
        ('portal_pages', '0046_auto_20150630_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='get_started_now_page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='wagtailcore.Page', null=True, blank=True, related_name='homepages'),
        ),
    ]
