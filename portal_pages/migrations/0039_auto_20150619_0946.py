# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal_pages', '0038_auto_20150528_1608'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='marketplaceentrypage',
            options={'verbose_name': 'marketplace', 'verbose_name_plural': 'marketplace'},
        ),
        migrations.AlterModelOptions(
            name='organization',
            options={'ordering': ('name',), 'verbose_name': 'organisation', 'verbose_name_plural': 'organisations'},
        ),
        migrations.AlterField(
            model_name='organizationcasestudy',
            name='organization',
            field=models.ForeignKey(related_name='+', verbose_name=b'organisation', to='portal_pages.Organization'),
        ),
    ]
