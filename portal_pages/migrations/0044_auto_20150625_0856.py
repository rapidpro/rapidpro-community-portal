# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal_pages', '0043_auto_20150624_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='highlightitem',
            name='target_page_external',
            field=models.CharField(verbose_name='Target Page External - Please complete either Target Page or External Page URL', max_length=255, blank=True),
        ),
    ]
