# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal_pages', '0048_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='casestudypage',
            name='submitter_email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
