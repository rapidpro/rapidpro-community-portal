# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0006_add_verbose_names'),
        ('wagtailcore', '0015_add_more_verbose_names'),
        ('portal_pages', '0052_blogpage_submitter_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='TechChangePage',
            fields=[
                ('page_ptr', models.OneToOneField(primary_key=True, parent_link=True, auto_created=True, to='wagtailcore.Page', serialize=False, on_delete=django.db.models.deletion.CASCADE)),
                ('body', wagtail.core.fields.RichTextField(default='', blank=True)),
                ('tech_change_link', models.CharField(max_length=255)),
                ('top_image', models.ForeignKey(related_name='+', null=True, to='wagtailimages.Image', blank=True, on_delete=django.db.models.deletion.SET_NULL)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page', models.Model),
        ),
    ]
