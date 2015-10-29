# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0002_auto_20151028_1811'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='weight',
        ),
        migrations.AddField(
            model_name='profile',
            name='classification',
            field=models.IntegerField(choices=[(1, 'Teacher'), (2, 'Student')], default=1),
            preserve_default=False,
        ),
    ]
