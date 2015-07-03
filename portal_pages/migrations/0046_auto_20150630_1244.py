# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('portal_pages', '0045_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogindexpage',
            name='submit_info',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='blogindexpage',
            name='thanks_info',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='highlightitem',
            name='target_page_external',
            field=models.CharField(verbose_name='External target page (leave blank if Target page is selected.)', blank=True, max_length=255),
        ),
    ]
