# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogindexpagerelatedlink',
            name='link_external',
            field=models.URLField(verbose_name='External link', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blogindexpagerelatedlink',
            name='title',
            field=models.CharField(max_length=255, help_text='Link title'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='date',
            field=models.DateField(verbose_name='Post date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blogpagecarouselitem',
            name='embed_url',
            field=models.URLField(verbose_name='Embed URL', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blogpagecarouselitem',
            name='link_external',
            field=models.URLField(verbose_name='External link', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blogpagerelatedlink',
            name='link_external',
            field=models.URLField(verbose_name='External link', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blogpagerelatedlink',
            name='title',
            field=models.CharField(max_length=255, help_text='Link title'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventindexpagerelatedlink',
            name='link_external',
            field=models.URLField(verbose_name='External link', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventindexpagerelatedlink',
            name='title',
            field=models.CharField(max_length=255, help_text='Link title'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='audience',
            field=models.CharField(max_length=255, choices=[('public', 'Public'), ('private', 'Private')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='date_from',
            field=models.DateField(verbose_name='Start date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='date_to',
            field=models.DateField(null=True, verbose_name='End date', help_text='Not required if event is on a single day', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='time_from',
            field=models.TimeField(null=True, verbose_name='Start time', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='time_to',
            field=models.TimeField(null=True, verbose_name='End time', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventpagecarouselitem',
            name='embed_url',
            field=models.URLField(verbose_name='Embed URL', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventpagecarouselitem',
            name='link_external',
            field=models.URLField(verbose_name='External link', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventpagerelatedlink',
            name='link_external',
            field=models.URLField(verbose_name='External link', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventpagerelatedlink',
            name='title',
            field=models.CharField(max_length=255, help_text='Link title'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventpagespeaker',
            name='first_name',
            field=models.CharField(max_length=255, verbose_name='Name', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventpagespeaker',
            name='last_name',
            field=models.CharField(max_length=255, verbose_name='Surname', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventpagespeaker',
            name='link_external',
            field=models.URLField(verbose_name='External link', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='formfield',
            name='field_type',
            field=models.CharField(max_length=16, choices=[('singleline', 'Single line text'), ('multiline', 'Multi-line text'), ('email', 'Email'), ('number', 'Number'), ('url', 'URL'), ('checkbox', 'Checkbox'), ('checkboxes', 'Checkboxes'), ('dropdown', 'Drop down'), ('radio', 'Radio buttons'), ('date', 'Date'), ('datetime', 'Date/time')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='homepagecarouselitem',
            name='embed_url',
            field=models.URLField(verbose_name='Embed URL', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='homepagecarouselitem',
            name='link_external',
            field=models.URLField(verbose_name='External link', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='homepagerelatedlink',
            name='link_external',
            field=models.URLField(verbose_name='External link', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='homepagerelatedlink',
            name='title',
            field=models.CharField(max_length=255, help_text='Link title'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='personpagerelatedlink',
            name='link_external',
            field=models.URLField(verbose_name='External link', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='personpagerelatedlink',
            name='title',
            field=models.CharField(max_length=255, help_text='Link title'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='standardindexpagerelatedlink',
            name='link_external',
            field=models.URLField(verbose_name='External link', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='standardindexpagerelatedlink',
            name='title',
            field=models.CharField(max_length=255, help_text='Link title'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='standardpagecarouselitem',
            name='embed_url',
            field=models.URLField(verbose_name='Embed URL', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='standardpagecarouselitem',
            name='link_external',
            field=models.URLField(verbose_name='External link', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='standardpagerelatedlink',
            name='link_external',
            field=models.URLField(verbose_name='External link', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='standardpagerelatedlink',
            name='title',
            field=models.CharField(max_length=255, help_text='Link title'),
            preserve_default=True,
        ),
    ]
