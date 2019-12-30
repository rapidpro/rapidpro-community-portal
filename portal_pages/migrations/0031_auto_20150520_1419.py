# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import modelcluster.contrib.taggit
import django.db.models.deletion
import wagtail.core.fields
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0005_make_filter_spec_unique'),
        ('taggit', '0001_initial'),
        ('wagtailcore', '0013_update_golive_expire_help_text'),
        ('portal_pages', '0030_marketplaceentrypage_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(primary_key=True, parent_link=True, serialize=False, to='wagtailcore.Page', auto_created=True, on_delete=django.db.models.deletion.CASCADE)),
                ('intro', wagtail.core.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='BlogPage',
            fields=[
                ('page_ptr', models.OneToOneField(primary_key=True, parent_link=True, serialize=False, to='wagtailcore.Page', auto_created=True, on_delete=django.db.models.deletion.CASCADE)),
                ('body', wagtail.core.fields.RichTextField()),
                ('date', models.DateField(verbose_name='Post date')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='BlogPageTag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('content_object', modelcluster.fields.ParentalKey(related_name='tagged_items', to='portal_pages.BlogPage')),
                ('tag', models.ForeignKey(related_name='portal_pages_blogpagetag_items', to='taggit.Tag', on_delete=django.db.models.deletion.CASCADE)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(help_text='A comma-separated list of tags.', blank=True, to='taggit.Tag', verbose_name='Tags', through='portal_pages.BlogPageTag'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blogpage',
            name='top_image',
            field=models.ForeignKey(related_name='+', blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.Image'),
            preserve_default=True,
        ),
    ]
