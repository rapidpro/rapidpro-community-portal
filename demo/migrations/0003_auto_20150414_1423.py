# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import modelcluster.fields
import wagtail.wagtailcore.fields
import modelcluster.tags
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0005_make_filter_spec_unique'),
        ('taggit', '0001_initial'),
        ('wagtaildocs', '0002_initial_data'),
        ('wagtailcore', '0013_update_golive_expire_help_text'),
        ('demo', '0002_auto_20150403_1029'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaseStudyIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(primary_key=True, serialize=False, parent_link=True, auto_created=True, to='wagtailcore.Page')),
                ('intro', wagtail.wagtailcore.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='CaseStudyIndexPageRelatedLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
                ('link_external', models.URLField(verbose_name='External link', blank=True)),
                ('title', models.CharField(max_length=255, help_text='Link title')),
                ('link_document', models.ForeignKey(related_name='+', blank=True, null=True, to='wagtaildocs.Document')),
            ],
            options={
                'abstract': False,
                'ordering': ['sort_order'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CaseStudyPage',
            fields=[
                ('page_ptr', models.OneToOneField(primary_key=True, serialize=False, parent_link=True, auto_created=True, to='wagtailcore.Page')),
                ('body', wagtail.wagtailcore.fields.RichTextField()),
                ('date', models.DateField(verbose_name='Post date')),
                ('feed_image', models.ForeignKey(related_name='+', blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='CaseStudyPageCarouselItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
                ('link_external', models.URLField(verbose_name='External link', blank=True)),
                ('embed_url', models.URLField(verbose_name='Embed URL', blank=True)),
                ('caption', models.CharField(max_length=255, blank=True)),
                ('image', models.ForeignKey(related_name='+', blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.Image')),
                ('link_document', models.ForeignKey(related_name='+', blank=True, null=True, to='wagtaildocs.Document')),
                ('link_page', models.ForeignKey(related_name='+', blank=True, null=True, to='wagtailcore.Page')),
                ('page', modelcluster.fields.ParentalKey(related_name='carousel_items', to='demo.CaseStudyPage')),
            ],
            options={
                'abstract': False,
                'ordering': ['sort_order'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CaseStudyPageRelatedLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
                ('link_external', models.URLField(verbose_name='External link', blank=True)),
                ('title', models.CharField(max_length=255, help_text='Link title')),
                ('link_document', models.ForeignKey(related_name='+', blank=True, null=True, to='wagtaildocs.Document')),
                ('link_page', models.ForeignKey(related_name='+', blank=True, null=True, to='wagtailcore.Page')),
                ('page', modelcluster.fields.ParentalKey(related_name='related_links', to='demo.CaseStudyPage')),
            ],
            options={
                'abstract': False,
                'ordering': ['sort_order'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CaseStudyPageTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('content_object', modelcluster.fields.ParentalKey(related_name='tagged_items', to='demo.CaseStudyPage')),
                ('tag', models.ForeignKey(related_name='demo_casestudypagetag_items', to='taggit.Tag')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='casestudypage',
            name='tags',
            field=modelcluster.tags.ClusterTaggableManager(verbose_name='Tags', blank=True, help_text='A comma-separated list of tags.', through='demo.CaseStudyPageTag', to='taggit.Tag'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='casestudyindexpagerelatedlink',
            name='link_page',
            field=models.ForeignKey(related_name='+', blank=True, null=True, to='wagtailcore.Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='casestudyindexpagerelatedlink',
            name='page',
            field=modelcluster.fields.ParentalKey(related_name='related_links', to='demo.CaseStudyIndexPage'),
            preserve_default=True,
        ),
    ]
