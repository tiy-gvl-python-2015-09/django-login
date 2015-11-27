# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='weight',
            field=models.FloatField(null=True),
        ),
    ]
