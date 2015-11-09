# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('create', '0002_auto_20151028_1748'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='credit_card',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='weight',
        ),
        migrations.AddField(
            model_name='profile',
            name='position',
            field=models.CharField(choices=[('teacher', 'Teacher'), ('student', 'Student')], null=True, max_length=20),
        ),
    ]
