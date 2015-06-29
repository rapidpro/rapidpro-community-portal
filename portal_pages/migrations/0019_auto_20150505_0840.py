# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal_pages', '0018_auto_20150504_1518'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='techfirmcasestudy',
            name='page',
        ),
        migrations.RemoveField(
            model_name='techfirmcasestudy',
            name='techfirm',
        ),
        migrations.DeleteModel(
            name='TechFirmCaseStudy',
        ),
    ]
