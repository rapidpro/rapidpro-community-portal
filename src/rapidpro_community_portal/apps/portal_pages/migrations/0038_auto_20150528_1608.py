# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import wagtail.core.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal_pages', '0037_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='youtube_blurb',
            field=wagtail.core.fields.RichTextField(default='', blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='youtube_video_id',
            field=models.CharField(default='', max_length=512, blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='youtube_video_title',
            field=models.CharField(default='', max_length=512, blank=True),
        ),
    ]
