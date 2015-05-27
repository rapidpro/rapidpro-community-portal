# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0006_add_verbose_names'),
        ('portal_pages', '0033_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='DefaultTopImage',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('default_top_image', models.ForeignKey(null=True, to='wagtailimages.Image', related_name='+', blank=True, on_delete=django.db.models.deletion.SET_NULL)),
            ],
        ),
    ]
