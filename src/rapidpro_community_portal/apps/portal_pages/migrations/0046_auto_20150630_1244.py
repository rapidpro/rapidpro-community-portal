# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import wagtail.core.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal_pages', '0045_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogindexpage',
            name='submit_info',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='blogindexpage',
            name='thanks_info',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='highlightitem',
            name='target_page_external',
            field=models.CharField(verbose_name='External target page (leave blank if Target page is selected.)', blank=True, max_length=255),
        ),
    ]
