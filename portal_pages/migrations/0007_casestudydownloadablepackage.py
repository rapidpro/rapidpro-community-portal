# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtaildocs', '0002_initial_data'),
        ('portal_pages', '0006_casestudyfullcase'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaseStudyDownloadablePackage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('sort_order', models.IntegerField(null=True, blank=True, editable=False)),
                ('blurb', wagtail.wagtailcore.fields.RichTextField()),
                ('casestudy_page', modelcluster.fields.ParentalKey(to='portal_pages.CaseStudyPage', related_name='case_study_downloadable_package')),
                ('downloadable_package', models.ForeignKey(to='wagtaildocs.Document')),
            ],
            options={
                'abstract': False,
                'ordering': ['sort_order'],
            },
            bases=(models.Model,),
        ),
    ]
