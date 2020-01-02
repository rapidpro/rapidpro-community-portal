# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.utils.timezone
import wagtail.core.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal_pages', '0023_country_preset_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='home_content',
        ),
        migrations.AddField(
            model_name='homepage',
            name='featured_case_study',
            field=models.ForeignKey(null=True, blank=True, to='portal_pages.CaseStudyPage', on_delete=django.db.models.deletion.CASCADE),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='homepage',
            name='featured_case_study_blurb',
            field=wagtail.core.fields.RichTextField(blank=True, default=''),
            preserve_default=True,
        ),
    ]
