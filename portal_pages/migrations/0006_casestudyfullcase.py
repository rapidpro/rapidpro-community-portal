# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.core.fields
import modelcluster.fields
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wagtaildocs', '0002_initial_data'),
        ('portal_pages', '0005_casestudyheroimageitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaseStudyFullCase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('blurb', wagtail.core.fields.RichTextField()),
                ('casestudy_page', modelcluster.fields.ParentalKey(related_name='case_study_full_case', to='portal_pages.CaseStudyPage')),
                ('full_case', models.ForeignKey(to='wagtaildocs.Document', on_delete=django.db.models.deletion.CASCADE)),
            ],
            options={
                'abstract': False,
                'ordering': ['sort_order'],
            },
            bases=(models.Model,),
        ),
    ]
