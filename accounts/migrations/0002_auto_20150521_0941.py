# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rapidprouser',
            name='groups',
            field=models.ManyToManyField(related_name='user_set', to='auth.Group', related_query_name='user', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', blank=True, verbose_name='groups'),
        ),
        migrations.AlterField(
            model_name='rapidprouser',
            name='last_login',
            field=models.DateTimeField(verbose_name='last login', blank=True, null=True),
        ),
    ]
