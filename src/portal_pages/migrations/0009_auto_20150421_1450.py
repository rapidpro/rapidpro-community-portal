# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtaildocs', '0002_initial_data'),
        ('portal_pages', '0008_auto_20150421_1414'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='casestudydownloadablepackage',
            name='casestudy_page',
        ),
        migrations.RemoveField(
            model_name='casestudydownloadablepackage',
            name='downloadable_package',
        ),
        migrations.DeleteModel(
            name='CaseStudyDownloadablePackage',
        ),
        migrations.RemoveField(
            model_name='casestudyfullcase',
            name='casestudy_page',
        ),
        migrations.RemoveField(
            model_name='casestudyfullcase',
            name='full_case',
        ),
        migrations.DeleteModel(
            name='CaseStudyFullCase',
        ),
        migrations.AddField(
            model_name='casestudypage',
            name='downloadable_package',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='wagtaildocs.Document', related_name='+', blank=True, null=True),
            preserve_default=True,
        ),
    ]
